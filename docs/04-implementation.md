# Implementation

A reference for the implementation architecture that emerged from applying Decision-Driven Design to a concrete system. Companion to the foundational documents ([`01-foundations.md`](01-foundations.md), [`02-entity-reference.md`](02-entity-reference.md), [`03-autonomy-levels.md`](03-autonomy-levels.md)).

## 1. What this document is

The foundational DDD documents articulate a framework: decisions are the work, artifacts are the unit of composition, value actions are the terminus, and the framework applies recursively to itself. They do not specify how to build the framework. This document fills that gap.

What follows is the implementation architecture that resulted from working through how to actually build a DDD-shaped system. It covers the capabilities the implementation depends on, the structural patterns that organize them, and the few non-obvious decisions that shape everything downstream. It is deliberately technology-neutral: it names the capabilities a system needs, not the specific products that supply them. It is not a tutorial; it is the implementation analogue of the entity reference — vocabulary and patterns to refer back to.

The architecture is realized as three components: an **orchestration system** (invokes roles, routes artifacts, records sessions), one or more **process systems** (each owning a single process, e.g. Engineering), and a reusable **event substrate** factored out as a shared library. Concrete bounds for the first build slice live in a companion document.

---

## 2. Capability requirements

An implementation does not require specific languages or products, but it does require a specific set of capabilities. The substrate must provide:

- **An artifact graph** — a store where artifacts are nodes and their relationships are typed, queryable edges (a DAG, not a pipeline), so relationships are first-class data rather than foreign keys or buried document fields. This is the system of record.
- **A declarative query capability** over the artifact graph, expressive enough to assemble sub-graphs deterministically from focal artifacts and their lineage. Bundle assembly (§4) depends on this.
- **A shape-constraint mechanism** for validating artifacts against schemas at write time and for expressing audit rules in the same language used for everything else.
- **A provenance model** capable of recording, for every artifact, the session that produced it, the role and model responsible, and the artifacts it consumed.
- **Session-scoped lineage** — the ability to group every change a session produced into a single addressable unit, so versioning, rollback, and bidirectional session-artifact reference are cheap.
- **A durable event capability** so that changes to the artifact graph can fan out to consumers without a separate source of truth (§7).

The implementation language for each layer follows the work, not a house style:

- The **orchestration layer and process systems** want a language with strong type guarantees and predictable performance, because routing decisions are durable and audit-critical.
- **Generative and interpretive action workers** (those driven by LLMs) want whatever ecosystem has the most mature SDKs, structured-output tooling, and evaluation libraries.
- **Mechanical action workers** want whatever fits the target system best (infrastructure tooling for deployment, the codebase's own language for test runners, and so on). They communicate with the orchestration layer through a stable, language-neutral contract over the message transport.

Rejected categories of off-the-shelf solution, and the reasoning:

- **External workflow engines.** The artifact graph already serves as durable workflow state. A separate workflow engine creates a second source of truth that must be kept in sync.
- **LLM agent frameworks.** These impose a composition model that conflicts with DDD's "the graph is yours, artifacts are the interface" stance. They optimize for the agent loop; DDD optimizes for the decision graph upstream of it.
- **Property-graph databases.** A semantic-graph model wins on stable semantics, federation, standardized vocabularies for provenance and shape validation, and structural fit with DDD's artifact-and-edge model.
- **Dedicated message brokers.** No broker is needed (see §7); the artifact graph itself is the durable event log. A broker can be added later purely as a wake-up signal carrier if push-latency requirements ever demand it, with state remaining in the graph.
- **Existing event-sourcing toolkits.** These are aggregate-centric and assume event-sourced rebuild as the value proposition. DDD chose graph-as-state instead, so adapting them costs more than building the narrow capability actually needed.

---

## 3. The artifact graph

The artifact graph is the data model. This is not just a storage choice; it shapes the architecture. The capabilities it must provide:

- **Typed edges as first-class data.** Artifact relationships are queryable directly, not reconstructed from foreign keys.
- **Shape constraints for schema enforcement.** Inter-system schema validation, intra-system write-time validation, and audit rules all use one mechanism.
- **A provenance vocabulary.** "Generated by," "used," and "associated with" map directly onto session → artifact → role → model. The audit infrastructure inherits a model that already captures what DDD requires, rather than reinventing it.
- **Session-scoped sub-graphs for lineage.** One sub-graph per session carries every change that session produced plus its provenance metadata. Versioning, rollback, and bidirectional session-artifact reference fall out for free.
- **Deterministic sub-graph construction.** Bundles aren't ad-hoc blobs; they're sub-graphs assembled by declarative queries (§4).
- **Cross-system query federation** for when the artifact bus eventually carries inter-system queries.

What the choice costs:

- **Tooling is sparser than for relational stores.** LLMs are weaker at writing graph queries than relational ones — if any role needs to query the artifact graph directly, give it curated query templates or a typed query layer rather than raw query access.
- **The temptation to over-model is real.** Start with a minimal provenance vocabulary plus a thin domain vocabulary and grow only under pressure from queries that need to run, not anticipated ones.
- **Graph stores are slower for high-write workloads** than purpose-built event stores. For this system's cadence (sessions per minute, not events per second), this is irrelevant.

The concrete commitment: an embedded artifact graph inside the orchestration process, exposed through a query endpoint for out-of-process workers, with session-scoped sub-graphs and provenance annotations on every session-produced change.

---

## 4. Bundle assembly: curated graph queries

The bundle each role receives is assembled by a curated query that the process system owns. This is the single most important pattern in the architecture.

Properties that matter:

- **Per-role queries, not per-artifact queries.** Same focal artifact, different roles, different bundles. The implementer pulls different facts from a feature node than the reviewer or architect would.
- **Curated, not auto-derived.** Queries are deliberate encodings of "what a competent role-holder needs to see to make this decision." They are the operational form of the hard-won process judgment DDD claims to inherit. Not embeddings, not schema introspection — judgment, written down.
- **Deterministic.** Ordering fixed everywhere it matters; no timestamps or nondeterministic functions in the query body. Same graph state + same query = byte-identical bundle. This is what lets bundles be hashed into session records and historical context to be reproduced.
- **Multiple queries plus composition, not one giant query.** A bundle is typically several queries — focal artifact, decision lineage, relevant decision records, applicable test criteria — each producing a sub-graph, then a serialization step composes them into the document the role consumes.
- **The query is itself an audit artifact.** When a role decides badly, "what did this role see?" is answered by re-running the query against the session sub-graph state at decision time. Reviewing the query when a role underperforms is often where the fix lives — not in the model, in what you gave it.

Per-role queries are the unit of evolution. Quality on a role flagging? Adjust its query, measure whether quality improves, version the change. Every encoded query is a permanent capture of process context any model can consume.

---

## 5. Action execution and the worker contract

Workers are stateless functions: `bundle → artifact`. The contract is intentionally narrow.

- Workers receive a serialized bundle via the dispatch event payload.
- Workers do not talk to the artifact graph. The harness assembles bundles and writes artifacts on their behalf.
- Workers produce structured output conforming to the role's output schema, validated against the shape constraints by the harness on write.
- Workers report session telemetry: tokens, latency, tool call history, errors.

Centralizing graph reads and writes in the harness keeps session-scope management, transaction boundaries, and provenance annotation consistent. Workers stay simple — they produce data, not graph structure.

Worker implementation by action flavor:

- **Generative/interpretive LLM actions** (implementer, drafter, triager, classifier): the ecosystem with the strongest SDK, structured-output, and eval support.
- **Pure execution against external systems** (deployer, test runner, email sender, ticket creator): whatever has the best SDK for the target system.
- **Code-shaped actions** (search, AST manipulation, patch application): a performance-oriented language if it's hot or heavily reused, a convenience-oriented one otherwise.

For LLM actions that use tools mid-session (an implementer writing code, running tests, iterating), tools are local to the worker, implemented in whatever fits. The whole tool-use exchange is one session from the harness's perspective: one dispatch, one artifact returned, one session record capturing the full tool-call lineage.

Worker registration is the orchestration analogue of model selection: workers announce capabilities (`code-writer`, `email-sender`, `deployer`) on a registry the orchestration system reads. Roles bind to capabilities, not specific worker instances. The binding from role to specific worker is an orchestration policy decision — same mechanism as model selection, same measurement evidence, same versioning.

---

## 6. Emergent decisions during action

Action sessions encounter decisions during execution: the implementer chooses an async pattern, the deployer chooses a retry strategy, the triager classifies an ambiguous signal. The framework has two distinct mechanisms for two distinct kinds of emergent decision.

**In-authority judgments** — idiomatic choices the role is permitted to make. Captured in session telemetry via a `record_emergent_judgment(decision, rationale)` call. They surface in the produced artifact's metadata; the paired interpretation session reviews them. If the interpreter flags one as exceeding authority, that itself becomes feedback against the role definition.

**Out-of-authority issues** — gaps in the spec, contradictions between bundle artifacts, unimplementable requirements, scope creep. These emit proper feedback artifacts via the framework's controlled vocabulary (`gap`, `contradiction`, `unimplementable`, `scope-issue`). Blocking feedback pauses the action; orchestration routes to the right upstream role; when the upstream decision lands, the worker resumes with the expanded bundle. Non-blocking feedback flows in parallel.

The bundle should carry an explicit **authority declaration** — what kinds of judgment calls fall within the role's scope vs. require escalation. This is part of the role catalog. Mis-bucketing (proceeded when should have escalated, or vice versa) is itself measurable: the interpretation session catches it, and the rate becomes a fitness function on the role.

Compounding value lives in what feedback patterns reveal:

- Repeated `gap` feedback from one role in one feature area → the upstream bundle assembly is inadequate there.
- Repeated authority-exceedance flags → the role definition is too loose.
- Repeated `contradiction` feedback → the upstream artifact graph has an unresolved tension that an audit should have caught.

Each signal drives an upstream change. The framework doesn't just tolerate emergent decisions; it learns from them.

---

## 7. The event substrate

Polling is a workaround, not a design. The native pattern: mutations to the artifact graph are events; subscriptions over the graph are derived event streams; consumers react.

Architecture: all mutations route through a single chokepoint — the orchestration system's graph writer (the one component permitted to write to the artifact graph). Every transaction follows this shape:

1. Write the change (within its session-scoped sub-graph for provenance)
2. Identify which subscriptions are affected (by artifact type touched)
3. Evaluate those subscriptions against the new state
4. Diff against the previous result set — compute new matches
5. Emit events for new matches; log each event into the artifact graph as an `Event` artifact with provenance
6. Commit transaction, then publish events to subscribers

Subscriptions are themselves first-class artifacts: a `Subscription` carries a query, declared trigger types (which artifact mutations should re-evaluate it), and a delivery target. The orchestration system maintains the subscription registry as standing policy.

### Graph-as-state, not event-sourced

Current state of the artifact graph is the truth; events are derived signals that fire as side-effects of mutations. Session-scoped sub-graphs preserve mutation history; provenance links events to causing mutations and to triggered artifacts. There is no separate event log — one store, the artifact graph. Consequences:

- Replay is just a query over historical session sub-graphs.
- Consumer offsets are monotonic event sequence numbers, tracked per consumer.
- No event-sourced rebuild needed — backups and sub-graph history cover recovery.

### Transactional outbox

Handles delivery durability. Events are written into the artifact graph marked unpublished, flipped to published by the publisher daemon after successful delivery. Crash mid-batch? On restart the publisher queries for unpublished events and resumes.

### Delivery is transport-flexible

In-process channels for co-located consumers, a streaming HTTP transport for remote consumers (out-of-process workers). Both serve the same logical stream. Workers that miss events while offline replay them by querying the artifact graph on reconnect — the graph is the durable event log; no broker required.

### Wake-up is push; commitment is atomic-graph-claim

Events tell workers "something is available." A conditional update against current status is what commits a specific worker to a specific dispatch. This separation cleanly handles duplicate notifications and out-of-order delivery.

This substrate is what the reusable event library provides as a separable component (§10).

---

## 8. Learning: the meta-loop

The framework applies recursively to itself. There is no separate "learning subsystem"; learning is the framework operating on its own artifacts.

The meta-loop mirrors the product loop:

1. **Aggregation** — a continuous process queries the orchestration system's artifact graph, maintaining rolling statistics on session records, feedback artifacts, and fitness function evaluations.
2. **Pattern detection** — a scheduled action role surfaces candidate-improvement artifacts when thresholds breach.
3. **Change proposal** — a decision role produces a concrete change artifact: target, revised query/definition/policy, rationale, expected effect, success criteria.
4. **Validation** — a gating process. For bundle queries: offline replay against historical sessions. For policies: simulation against measurement history. For schema: shape re-conformance and audit replay.
5. **Application** — once validated, the change is committed as a new version. Session-scoped sub-graphs make this clean; old version stays in history, new is the active reference. No deployment or migration, just a version pointer flip.
6. **Post-change monitoring** — measurement tracks the post-change cohort against pre-change baseline. Signal didn't move? Roll back or revise.

Ownership by what's changing:

- **Policy** (model bindings, thresholds, autonomy levels): policy owner role in the orchestration system.
- **Bundle queries and role definitions**: architect role in the system that owns them; Engineering's architect owns Engineering's queries.
- **Schema / shared vocabulary**: a framework-level vocabulary architect role; heavier change, ripples through every consumer.
- **System implementations themselves** (code): the Engineering system applied to itself — the factory building and evolving itself.

The autonomy structure applies recursively. The pattern detector might run autonomously at Level 4. The change proposer might sit at Level 3 with human approval before validation. The applier is usually Level 4 once validation passes. Different meta-roles graduate independently on their own measurement evidence.

The compounding result: bundles get better as the system operates, role definitions tighten under empirical pressure, model bindings improve as evidence accumulates, and the audit infrastructure that governs the product graph also governs the meta-graph.

---

## 9. Per-component autonomy

Per-component, not per-system. Different parts of the system live at different autonomy levels, governed by the same per-role mechanism that governs everything else.

- **Configuration-shaped artifacts** (bundle query templates, audit rule definitions, role catalog edits, policy artifacts): Level 4 autonomous behind validation gates. These are data, not infrastructure.
- **System implementation code** (harness internals, dispatch logic, bus, system plug-in code): Level 3, human-approved at change. Higher blast radius, harder to roll back cleanly.
- **Bootstrap layer** (the mechanical event loop under the orchestration system): always human-approved at change, never autonomous. This is the trust anchor; if it goes wrong, the framework loses its own audit capability.
- **Release / version cutover**: Level 3 regardless of what's in the release. A human signs off on promoting a version to production, reviewing the change set, validation evidence, and test results in aggregate.

Both/and rather than either/or: high-blast-radius code is reviewed at change *and* at release; configuration flows autonomously through validation and gets bundled into the same release for human cutover approval. The release-approver role is the universal checkpoint; per-change approval scales with risk.

### The model catalog

A first-class entity in the architecture, parallel to the role catalog. A `Model` artifact in the orchestration system carries:

- Identity and version (exact versions, not families)
- Capability tags (text-only, multimodal, code-specialized, long-context, fast-cheap)
- Cost profile (token costs, latency)
- Eligibility status (qualified, candidate, deprecated, pulled)
- Provenance — the eval evidence that qualified it

Bundle queries and role bindings reference **capability tags**, not model names. "Requires frontier multimodal reasoning" is the binding; the catalog maps that to the current best concrete model. When a new model qualifies, the policy owner re-evaluates affected role bindings as a normal meta-decision — no edits to system implementations needed. Models enter the catalog by passing a registration audit; the catalog represents the eligible set, not the universe of LLMs anyone could call.

---

## 10. System composition: orchestration, process systems, event substrate

The concrete shape of the architecture is three kinds of component:

**Process system** — the system implementation for a single process (e.g. Engineering). Manages that process's artifact types, builds its derived in-memory view, exports its artifacts, assembles curated context bundles, runs preflight/gap/drift audits, computes fitness metrics, serves its slice of the artifact graph to the orchestration system. It draws an explicit line: *a process system does not invoke agents.*

**Orchestration system** — invokes agents, records sessions, routes artifacts between roles, manages model bindings, manages policy, runs the event substrate, surfaces work to humans for checkpoints, improves itself via the meta-loop. It *does not own process-specific artifact knowledge* — it calls the relevant process system for what that system already knows.

**Event substrate** — factored out as a separate, reusable library intended for community contribution. Provides the graph writer, subscription machinery, the outbox-pattern publisher, and delivery transports. It carries no DDD-specific vocabulary; it speaks only of mutations, subscriptions, events, and delivery.

### Stable Dependency Principle

Governs the dependency direction:

- The event substrate depends only on layers more stable than itself (the artifact graph store and generic async/transport infrastructure). It has no dependency on the orchestration system and no awareness of DDD concepts.
- The orchestration system depends on the event substrate and on the process systems (initially via subprocess invocation).
- The framework library lives inside the orchestration system's workspace initially; separate-repo extraction is deferred until the API has been pressure-tested by more than one consumer.

### The platform property

Orchestration plus a process system is a software engineering platform, not a single-product tool. The first product it operates on is itself. The second is the event substrate it extracts. The third is whatever else you point it at. The DDD recursion — process that operates on itself — generalizes to "process that operates on any product, including its own internals." The maintenance burden of extracting the event substrate as open source is absorbed into the same loop that runs everything else.

---

## 11. Implementation strategy

Thin vertical slice first, then thicken — risk-driven, not feature-driven.

The temptation with a complete architecture is to build Phase 0 perfectly (full vocabulary, role catalog, audits, meta-loop) before any artifact flows through. That is a year-long detour. The faster path is to push one artifact through one role end-to-end early, then add the missing concerns under pressure from real use.

**Slice 1 — single role end-to-end:**

- Harness with an embedded artifact graph, single mutation chokepoint via the graph writer
- One artifact type and one downstream artifact type with shape constraints
- One curated query for bundle assembly
- One worker calling an LLM with structured output
- Session-scoped sub-graph with provenance annotations
- Hardcoded model binding, hardcoded routing

**Deliberately deferred:** interpretation pairing, feedback flow lifecycle, audits beyond shape validation, model catalog as artifact, policy as artifact, multi-role flow, human checkpoints, the meta-loop, multi-product orchestration.

### The bootstrap consequence

Slice 1 is the only slice built entirely by humans. Slice 2 onward, the system processes its own feature specs. So the first artifact the system processes is a feature spec describing slice 2 — interpretation pairing, or feedback flow, or whatever is chosen. Drafting that spec is the first design exercise, before any code gets written, because it surfaces what the feature-spec artifact needs to express.

Slice 1 specifics are in the companion bounds document.

### Author workflow

The slice 1 specification itself is authored using the process system's authoring mode, not as free-form prose. This dogfoods the process system from day one and produces artifacts already in the right form for the system to ingest. Two-document setup:

1. A short bounds document (free-form) — the architectural narrative and "out of bounds" framing.
2. The process-system artifacts — features, decision records, test criteria in proper structured form.

The bounds document references the artifact graph as the operational specification.

---

## 12. Where this leads

The shape of this system at maturity:

- Multiple system implementations, each owning one process (Engineering, Validation, Operations, Discovery, Release), all driven by one orchestration system.
- A bus between systems carrying inter-system artifacts (feature requests, validation verdicts, operational findings, deployment requests).
- Per-role autonomy graduated independently based on measurement evidence — some roles fully autonomous, others human-checkpointed, the system's overall level being the floor across roles.
- A meta-loop that revises queries, role definitions, model bindings, and policies under empirical pressure, with the framework's discipline applied to itself.
- A shared vocabulary that grows under human curation as new artifact types and edge types become necessary.

What this gives that current AI systems don't:

- **Bounded autonomy.** The orchestration system's policy declarations make the boundary explicit. Outside the boundary, escalation. Inside, autonomous operation.
- **Auditable autonomy.** Every session is recorded. Every artifact has provenance. Every routing decision is itself an artifact. When autonomous operation produces a bad outcome, the audit trail explains what and why.
- **Improvable autonomy.** Measurement makes role-model fit empirically evaluable. Policy decisions consume measurement evidence. The system improves through structured feedback rather than ad-hoc tweaking.
- **Localized failure.** When the autonomous system fails, failure localizes to a specific role, a specific session, a specific bundle. Recovery is bounded.

Most attempts at autonomous AI jump straight to Level 5 ambitions and fail because they lack the structure to make autonomy bounded, auditable, and improvable. This architecture addresses each failure mode structurally, because the structure is the substrate. The cognitive properties — adaptation, bounded improvement, structured learning — are emergent from the substrate, not bolted onto an agent loop.

---

## 13. Open questions

A few decisions surfaced during design that may shift as slice 1 contacts reality:

- **Where does the `CodeChange` artifact live?** It's an Engineering artifact about a feature, which argues for the Engineering process system's schema. But the session that produced it lives in the orchestration system. Slice 1 leans toward extending the process system with the new type for symmetry; could reverse if it creates friction.
- **Subscription evaluation cost at scale.** Currently expected to be cheap (~10–100 subscriptions, ~10–100 mutations per session). If subscription count grows substantially, true incremental view maintenance may be needed rather than naive re-evaluation.
- **Broker or no broker.** Current decision is no broker. If push-latency requirements ever exceed what graph-poll-on-event-delivery can provide, a lightweight signal broker is the clean addition. State stays in the artifact graph; the broker only carries wake-up signals.
- **When to extract the event substrate to a separate repo.** Currently lives in the orchestration system's workspace. Right time is "after a second consumer exists and the API has been pressure-tested" — concretely, sometime around slice 3 or 4.

---

*This document captures decisions and patterns as of slice 1 design. It will be revised under the same discipline as anything else in the system: as a versioned artifact, with provenance, in response to measurement evidence from the work it enables.*
