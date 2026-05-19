# Implementing Decision-Driven Design

A reference for the implementation architecture that emerged from applying Decision-Driven Design to a concrete system. Companion to the foundational DDD documents (*Decision-Driven Design*, *DDD and the Five Levels of AI Autonomy*, *Decision-Driven Design: Entity Reference*).

## 1. What this document is

The foundational DDD documents articulate a framework: decisions are the work, artifacts are the unit of composition, value actions are the terminus, and the framework applies recursively to itself. They do not specify how to build the framework. This document fills that gap.

What follows is the implementation architecture that resulted from working through how to actually build a DDD-shaped system. It covers technology choices, structural patterns, and the few non-obvious decisions that shape everything downstream. It is not a tutorial; it is the implementation analogue of the entity reference — vocabulary and patterns to refer back to.

The concrete system this architecture targets is **pipeline-cli** (the orchestration system), **product-cli** (the Engineering process system, which already exists), and **oxi-events** (a reusable event substrate extracted as a separate Rust crate). Slice 1 bounds for that work are in a companion document.

---

## 2. Technology stack

The choice is uniform across the orchestration layer and the system implementations:

- **Rust** for the harness, orchestration system, and process system implementations (pipeline-cli, product-cli, future plug-ins). Performance and type safety matter at the orchestration layer; durability and audit-criticality of routing decisions argue for strong guarantees.
- **Oxigraph** as the embedded RDF triple store and SPARQL engine. Apache 2.0, Rust-native, embeddable, SPARQL 1.1 conformant.
- **Python** for LLM-driven action workers. The Anthropic and OpenAI SDKs, structured output libraries (Pydantic, instructor, BAML), and the prompt-engineering / eval ecosystem are most mature in Python.
- **Any language for mechanical action workers** — workers communicate with the orchestration layer via a stable JSON contract over the message transport. Language follows ecosystem fit for the action (Terraform for deployment, the codebase's language for test runners, etc.).

Rejected alternatives and reasoning:

- **Temporal-style workflow engines** (Temporal, Prefect, Dagster): the graph already serves as the durable workflow state. Adding a workflow engine creates a second source of truth that must be kept in sync.
- **LLM agent frameworks** (LangChain, AutoGen, CrewAI, LangGraph): these impose a composition model that conflicts with DDD's "the graph is yours, artifacts are the interface" stance. They optimize for the agent loop; DDD optimizes for the decision graph upstream of it.
- **Property graph databases** (Neo4j, etc.): RDF wins on stable semantics, federation, W3C ontology standards (PROV-O, SHACL), and the structural fit with DDD's artifact-and-edge model.
- **Redis Streams** as a message bus: licensing is contested (SSPL → AGPL); more fundamentally, no broker is needed (see §7). Valkey would solve the licensing issue without solving the architectural one.
- **Existing Rust event-sourcing crates** (cqrs-es, eventually-rs, esrs, eventsourced): all aggregate-centric with typed serde events and Postgres backends. They assume event-sourced rebuild as the value proposition; we explicitly chose graph-as-state instead. Adapting them is more expensive than greenfielding what we actually need.

---

## 3. The RDF substrate

RDF is the data model. This is not just a storage choice; it shapes the architecture.

What RDF gives that other models don't:

- **Typed edges as first-class triples.** Artifact relationships are queryable, not buried in foreign keys or document fields.
- **SHACL for shape constraints.** Inter-system schema validation, intra-system write-time validation, and audit rules all use the same mechanism.
- **PROV-O for provenance.** `wasGeneratedBy`, `used`, `wasAssociatedWith` map directly onto session → artifact → role → model. The audit infrastructure inherits W3C standards that already model what DDD requires.
- **Named graphs for session-level lineage.** One named graph per session carries every triple that session produced, plus PROV-O metadata. Versioning, rollback, and bidirectional session-artifact reference fall out for free.
- **SPARQL CONSTRUCT for deterministic bundle assembly.** Bundles aren't ad-hoc JSON blobs; they're sub-graphs assembled by declarative queries (§4).
- **Federation in SPARQL** for cross-system queries when the artifact bus eventually carries them.

What it costs:

- **Tooling is sparser than for SQL.** LLMs are weaker at SPARQL than SQL — if any role needs to query the graph directly, give it curated query templates or a typed query layer rather than raw SPARQL.
- **The temptation to over-ontologize is real.** Start with PROV-O plus a thin domain vocabulary and grow only under pressure from queries that need to run, not anticipated ones.
- **Triple stores are slower for high-write workloads than purpose-built event stores.** For this system's cadence (sessions per minute, not events per second), this is irrelevant.

The Oxigraph commitment specifically: embedded in the Rust orchestration process, exposed as a SPARQL HTTP endpoint for polyglot workers, named-graph-per-session for provenance, PROV-O annotations on every session-produced triple.

---

## 4. Bundle assembly: curated SPARQL queries

The bundle each role receives is assembled by a curated SPARQL query that the system implementation owns. This is the single most important pattern in the architecture.

Properties that matter:

- **Per-role queries, not per-artifact queries.** Same focal artifact, different roles, different bundles. The implementer pulls different triples from a feature node than the reviewer or architect would.
- **Curated, not auto-derived.** Queries are deliberate encodings of "what a competent role-holder needs to see to make this decision." They are the operational form of the hard-won process judgment DDD claims to inherit. Not embeddings, not schema introspection — judgment, written down.
- **Deterministic.** ORDER BY everywhere ordering matters; no timestamps or nondeterministic functions in the query body. Same graph state + same query = byte-identical bundle. This is what lets bundles be hashed into session records and historical context to be reproduced.
- **Multiple queries plus composition, not one giant CONSTRUCT.** A bundle is typically several queries — focal artifact, decision lineage, relevant ADRs, applicable test criteria — each producing a sub-graph, then a serialization step composes them into the document the role consumes.
- **The query is itself an audit artifact.** When a role decides badly, "what did this role see?" is answered by re-running the query against the named-graph state at decision time. Reviewing the query when a role underperforms is often where the fix lives — not in the model, in what you gave it.

Per-role queries are the unit of evolution. Quality on a role flagging? Adjust its query, measure whether quality improves, version the change. Every encoded query is a permanent capture of process context any model can consume.

---

## 5. Action execution and the worker contract

Workers are stateless functions: `bundle → artifact`. The contract is intentionally narrow.

- Workers receive a serialized bundle via the dispatch event payload.
- Workers do not talk to the graph. The harness assembles bundles and writes artifacts on their behalf.
- Workers produce structured output conforming to the role's output schema, validated against SHACL by the harness on write.
- Workers report session telemetry: tokens, latency, tool call history, errors.

Centralizing graph reads and writes in the harness keeps named-graph management, transaction boundaries, and PROV-O annotation consistent. Workers stay simple — they produce data, not triples.

Language choice by action flavor:

- **Generative/interpretive LLM actions** (implementer, drafter, triager, classifier): Python. SDK maturity, structured output tooling, eval ecosystem.
- **Pure execution against external systems** (deployer, test runner, email sender, ticket creator): whatever has the best SDK for the target system.
- **Code-shaped actions** (search, AST manipulation, patch application): Rust if performance matters or it's reused heavily, Python otherwise.

For LLM actions that use tools mid-session (an implementer writing code, running tests, iterating), tools are local to the worker, implemented in whatever language fits. The whole tool-use exchange is one session from the harness's perspective: one dispatch, one artifact returned, one session record capturing the full tool-call lineage.

Worker registration is the orchestration analogue of model selection: workers announce capabilities (`code-writer`, `email-sender`, `terraform-applier`) on a registry the orchestration system reads. Roles bind to capabilities, not specific worker instances. The binding from role to specific worker is an orchestration policy decision — same mechanism as model selection, same measurement evidence, same versioning.

---

## 6. Emergent decisions during action

Action sessions encounter decisions during execution: the implementer chooses an async pattern, the deployer chooses a retry strategy, the triager classifies an ambiguous signal. The framework has two distinct mechanisms for two distinct kinds of emergent decision.

**In-authority judgments** — idiomatic choices the role is permitted to make. Captured in session telemetry via `record_emergent_judgment(decision, rationale)`. They surface in the produced artifact's metadata; the paired interpretation session reviews them. If the interpreter flags one as exceeding authority, that itself becomes feedback against the role definition.

**Out-of-authority issues** — gaps in the spec, contradictions between bundle artifacts, unimplementable requirements, scope creep. These emit proper feedback artifacts via the framework's controlled vocabulary (`gap`, `contradiction`, `unimplementable`, `scope-issue`). Blocking feedback pauses the action; orchestration routes to the right upstream role; when the upstream decision lands, the worker resumes with the expanded bundle. Non-blocking feedback flows in parallel.

The bundle should carry an explicit **authority declaration** — what kinds of judgment calls fall within the role's scope vs. require escalation. This is part of the role catalog. Mis-bucketing (proceeded when should have escalated, or vice versa) is itself measurable: the interpretation session catches it, and the rate becomes a fitness function on the role.

Compounding value lives in what feedback patterns reveal:

- Repeated `gap` feedback from one role in one feature area → the upstream bundle assembly is inadequate there.
- Repeated authority-exceedance flags → the role definition is too loose.
- Repeated `contradiction` feedback → the upstream artifact graph has an unresolved tension that an audit should have caught.

Each signal drives an upstream change. The framework doesn't just tolerate emergent decisions; it learns from them.

---

## 7. The event substrate

Polling is a workaround, not a design. The native pattern: graph mutations are events; subscriptions over the graph are derived event streams; consumers react.

Architecture: all mutations route through a single chokepoint — pipeline-cli's `GraphWriter`. Every transaction follows this shape:

1. Write triples (with named graph for provenance)
2. Identify which subscriptions are affected (by artifact type touched)
3. Evaluate those subscriptions against the new state
4. Diff against the previous result set — compute new matches
5. Emit events for new matches; log each event into the graph as an `Event` artifact with PROV-O
6. Commit transaction, then publish events to subscribers

Subscriptions are themselves first-class artifacts: a `Subscription` carries a SPARQL query, declared trigger types (which artifact mutations should re-evaluate it), and a delivery target. The orchestration system maintains the subscription registry as standing policy.

### Graph-as-state, not event-sourced

Current graph is the truth; events are derived signals that fire as side-effects of mutations. Named graphs preserve mutation history; PROV-O links events to causing mutations and to triggered artifacts. There is no separate event log — one substrate, the graph. Consequences:

- Replay is just SPARQL over historical named graphs.
- Consumer offsets are monotonic event sequence numbers, tracked per consumer.
- No event-sourced rebuild needed — backups and named graph history cover recovery.

### Transactional outbox

Handles delivery durability. Events are written into the graph with `published=false`, flipped to `published=true` by the publisher daemon after successful delivery. Crash mid-batch? On restart the publisher SPARQL-queries for unpublished events and resumes. (Structurally identical to Marten's pattern on PostgreSQL, with RDF as the substrate.)

### Delivery is transport-flexible

In-process tokio broadcast channels for co-located consumers, SSE via axum for remote consumers (Python workers). Both serve the same logical stream. Workers that miss events while offline replay them via SPARQL on reconnect — the graph is the durable event log; no broker required.

### Wake-up is push; commitment is atomic-graph-claim

Events tell workers "something is available." The SPARQL UPDATE conditional on current status is what commits a specific worker to a specific dispatch. This separation cleanly handles duplicate notifications and out-of-order delivery.

This substrate is what oxi-events provides as a separable Rust crate (§10).

---

## 8. Learning: the meta-loop

The framework applies recursively to itself. There is no separate "learning subsystem"; learning is the framework operating on its own artifacts.

The meta-loop mirrors the product loop:

1. **Aggregation** — a continuous Rust process runs SPARQL over the orchestration graph, maintaining rolling statistics on session records, feedback artifacts, and fitness function evaluations.
2. **Pattern detection** — a scheduled action role surfaces candidate-improvement artifacts when thresholds breach.
3. **Change proposal** — a decision role produces a concrete change artifact: target, revised query/definition/policy, rationale, expected effect, success criteria.
4. **Validation** — a gating process. For bundle queries: offline replay against historical sessions. For policies: simulation against measurement history. For schema: SHACL re-conformance and audit replay.
5. **Application** — once validated, the change is committed as a new version. Named graphs make this clean; old version stays in history, new is the active reference. No deployment or migration, just a version pointer flip.
6. **Post-change monitoring** — measurement tracks the post-change cohort against pre-change baseline. Signal didn't move? Roll back or revise.

Ownership by what's changing:

- **Policy** (model bindings, thresholds, autonomy levels): policy owner role in the orchestration system.
- **Bundle queries and role definitions**: architect role in the system that owns them; Engineering's architect owns Engineering's queries.
- **Ontology / schema**: a framework-level ontology architect role; heavier change, ripples through every consumer.
- **System implementations themselves** (Rust code): the Engineering system applied to itself — the factory building and evolving itself.

The autonomy structure applies recursively. The pattern detector might run autonomously at Level 4. The change proposer might sit at Level 3 with human approval before validation. The applier is usually Level 4 once validation passes. Different meta-roles graduate independently on their own measurement evidence.

The compounding result: bundles get better as the system operates, role definitions tighten under empirical pressure, model bindings improve as evidence accumulates, and the audit infrastructure that governs the product graph also governs the meta-graph.

---

## 9. Per-component autonomy

Per-component, not per-system. Different parts of the system live at different autonomy levels, governed by the same per-role mechanism that governs everything else.

- **Configuration-shaped artifacts** (bundle query templates, audit rule definitions, role catalog edits, policy artifacts): Level 4 autonomous behind validation gates. These are data, not infrastructure.
- **System implementation Rust code** (harness internals, dispatch logic, bus, system plug-in code): Level 3, human-approved at change. Higher blast radius, harder to roll back cleanly.
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

## 10. System composition: pipeline-cli, product-cli, oxi-events

The concrete shape of the architecture:

**product-cli** — the system implementation for the Engineering process. Already exists; manages feature/ADR/TC/dep artifacts, builds the derived in-memory graph, exports RDF, assembles curated context bundles, runs preflight/gap/drift audits, computes fitness metrics, serves the engineering graph via MCP. Its PRD draws an explicit line: *"Product does not invoke agents."*

**pipeline-cli** — the orchestration system. Invokes agents, records sessions, routes artifacts between roles, manages model bindings, manages policy, runs the event substrate, surfaces work to humans for checkpoints, improves itself via the meta-loop. *Does not own engineering artifact knowledge* — calls product-cli for what product-cli already knows.

**oxi-events** — the event substrate, extracted as a separate Rust crate intended for community contribution. Provides `GraphWriter`, `Subscription`, the outbox-pattern publisher, and delivery transports. No DDD-specific vocabulary; speaks only of mutations, subscriptions, events, delivery.

### Stable Dependency Principle

Governs the dependency direction:

- oxi-events depends only on substrates more stable than itself (oxigraph, tokio, tokio-stream, axum, serde, tracing). No dependency on pipeline-cli; no awareness of DDD concepts.
- pipeline-cli depends on oxi-events and on product-cli (initially via subprocess invocation).
- The framework crate lives inside pipeline-cli's workspace initially; separate-repo extraction is deferred until the API has been pressure-tested by more than one consumer.

### The platform property

pipeline-cli + product-cli is a software engineering platform, not a single-product tool. The first product it operates on is itself. The second is the oxi-events framework it extracts. The third is whatever else you point it at. The DDD recursion — process that operates on itself — generalizes to "process that operates on any product, including its own internals." The OSS maintenance burden of extracting oxi-events is absorbed into the same loop that runs everything else.

---

## 11. Implementation strategy

Thin vertical slice first, then thicken — risk-driven, not feature-driven.

The temptation with a complete architecture is to build Phase 0 perfectly (full ontology, role catalog, audits, meta-loop) before any artifact flows through. That is a year-long detour. The faster path is to push one artifact through one role end-to-end early, then add the missing concerns under pressure from real use.

**Slice 1 — single role end-to-end:**

- Rust harness with embedded Oxigraph, single mutation chokepoint via `GraphWriter`
- One artifact type and one downstream artifact type with SHACL shapes
- One curated CONSTRUCT query for bundle assembly
- One Python worker calling Claude with structured output
- Named-graph-per-session with PROV-O annotations
- Hardcoded model binding, hardcoded routing

**Deliberately deferred:** interpretation pairing, feedback flow lifecycle, audits beyond SHACL, model catalog as artifact, policy as artifact, multi-role flow, human checkpoints, the meta-loop, multi-product orchestration.

### The bootstrap consequence

Slice 1 is the only slice built entirely by humans. Slice 2 onward, the system processes its own feature_specs. So the first artifact the system processes is a feature_spec describing slice 2 — interpretation pairing, or feedback flow, or whatever is chosen. Drafting that spec is the first design exercise, before any Rust gets written, because it surfaces what `FeatureSpec` needs to express.

Slice 1 specifics are in the companion bounds document.

### Author workflow

The slice 1 specification itself is authored using product-cli (`product author` mode), not as free-form markdown. This dogfoods product-cli from day one and produces artifacts already in the right form for the system to ingest. Two-document setup:

1. A short bounds document (free-form markdown) — the architectural narrative and "out of bounds" framing.
2. The product-cli graph — features, ADRs, TCs in proper structured form.

The bounds document references the graph as the operational specification.

---

## 12. Where this leads

The shape of this system at maturity:

- Multiple system implementations, each owning one process (Engineering, Validation, Operations, Discovery, Release), all driven by one orchestration system.
- A bus between systems carrying inter-system artifacts (feature requests, validation verdicts, operational findings, deployment requests).
- Per-role autonomy graduated independently based on measurement evidence — some roles fully autonomous, others human-checkpointed, the system's overall level being the floor across roles.
- A meta-loop that revises queries, role definitions, model bindings, and policies under empirical pressure, with the framework's discipline applied to itself.
- An ontology that grows under human curation as new artifact types and edge types become necessary.

What this gives that current AI systems don't:

- **Bounded autonomy.** The orchestration system's policy declarations make the boundary explicit. Outside the boundary, escalation. Inside, autonomous operation.
- **Auditable autonomy.** Every session is recorded. Every artifact has provenance. Every routing decision is itself an artifact. When autonomous operation produces a bad outcome, the audit trail explains what and why.
- **Improvable autonomy.** Measurement makes role-model fit empirically evaluable. Policy decisions consume measurement evidence. The system improves through structured feedback rather than ad-hoc tweaking.
- **Localized failure.** When the autonomous system fails, failure localizes to a specific role, a specific session, a specific bundle. Recovery is bounded.

Most attempts at autonomous AI jump straight to Level 5 ambitions and fail because they lack the structure to make autonomy bounded, auditable, and improvable. This architecture addresses each failure mode structurally, because the structure is the substrate. The cognitive properties — adaptation, bounded improvement, structured learning — are emergent from the substrate, not bolted onto an agent loop.

---

## 13. Open questions

A few decisions surfaced during design that may shift as slice 1 contacts reality:

- **Where does `CodeChange` live?** It's an Engineering artifact about a feature, which argues for product-cli's schema. But the session that produced it lives in pipeline-cli. Slice 1 leans toward extending product-cli with the new type for symmetry; could reverse if it creates friction.
- **Subscription evaluation cost at scale.** Currently expected to be cheap (~10–100 subscriptions, ~10–100 mutations per session). If subscription count grows substantially, true incremental view maintenance (differential dataflow style) may be needed rather than naive re-evaluation.
- **NATS or no NATS.** Current decision is no broker. If push-latency requirements ever exceed what graph-poll-on-event-delivery can provide, NATS with JetStream is the licensing-clean addition. State stays in Oxigraph; NATS only carries wake-up signals.
- **When to extract oxi-events to a separate repo.** Currently lives in pipeline-cli's workspace. Right time is "after a second consumer exists and the API has been pressure-tested" — concretely, sometime around slice 3 or 4.

---

*This document captures decisions and patterns as of slice 1 design. It will be revised under the same discipline as anything else in the system: as a versioned artifact, with provenance, in response to measurement evidence from the work it enables.*
