# DDD Applied: Entity Reference

> **Apparatus §2 — normative.** The apparatus vocabulary, made precise. Anything claiming DDD conformance uses these entities as defined here. This is the reference you return to once [Decisions, Roles, and Artifacts](01-decisions-and-artifacts.md) has established the geometry and the [core](../core/) has established the law these entities exist to keep.
>
> Borrowed terms (DAG, DMN, RDF, MCP, OCI, …) — see [Glossary](glossary.md).

The apparatus vocabulary, organized around the inversion established in [§1](01-decisions-and-artifacts.md#the-inversion): decisions are the work, value actions are the terminus, and everything between the two world boundaries is decisions recorded as artifacts. These entities are how a real domain is arranged so that the [conservation law](../core/01-the-law.md) can actually be run and its allocation kept inspectable.

---

## Index

**Alphabetical.**
[Acknowledgement](#acknowledgement) · [Action](#action) · [Action-Interpretation Agreement](#action-interpretation-agreement) · [Application Status](#application-status) · [Artifact](#artifact) · [Audit](#audit) · [Autonomy Level](#autonomy-level) · [Bundle](#bundle) · [Bus](#bus) · [Context](#context) · [Convergence State](#convergence-state) · [Decision](#decision) · [Domain](#domain) · [Domain Knowledge](#domain-knowledge) · [Edge](#edge) · [Eligible](#eligible) · [Feedback](#feedback) · [Fitness Function](#fitness-function) · [Flow Class](#flow-class) · [Form](#form) · [Harness](#harness) · [Interface (System Interface)](#interface-system-interface) · [Interpretation](#interpretation) · [Inter-system Schema](#inter-system-schema) · [Phase](#phase) · [Policy](#policy) · [Process](#process) · [Prompt](#prompt) · [Provenance](#provenance) · [Role](#role) · [Schema](#schema) · [Sensing Action](#sensing-action) · [Session](#session) · [Session Record](#session-record) · [SPMC](#spmc-schema-prompt-model-context) · [System](#system) · [Task](#task) · [TaskType](#tasktype) · [Transport](#transport) · [Value Action](#value-action) · [Worker](#worker)

**By category.**

- *Primary entities* — the actors, work units, and outputs of the graph: [Action](#action) · [Artifact](#artifact) · [Bundle](#bundle) · [Context](#context) · [Convergence State](#convergence-state) · [Decision](#decision) · [Domain Knowledge](#domain-knowledge) · [Interpretation](#interpretation) · [Process](#process) · [Role](#role) · [Sensing Action](#sensing-action) · [Session](#session) · [System](#system) · [Task](#task) · [TaskType](#tasktype) · [Value Action](#value-action) · [Worker](#worker)
- *Structural entities* — the shape and connection of the primary entities: [Acknowledgement](#acknowledgement) · [Application Status](#application-status) · [Domain](#domain) · [Edge](#edge) · [Eligible](#eligible) · [Form](#form) · [Phase](#phase) · [Prompt](#prompt) · [Provenance](#provenance) · [Schema](#schema)
- *Flow entities* — how artifacts and signals move through and between systems: [Bus](#bus) · [Feedback](#feedback) · [Flow Class](#flow-class) · [Inter-system Schema](#inter-system-schema)
- *Operational entities* — the runtime and process layer: [Action-Interpretation Agreement](#action-interpretation-agreement) · [Audit](#audit) · [Autonomy Level](#autonomy-level) · [Fitness Function](#fitness-function) · [Harness](#harness) · [Interface (System Interface)](#interface-system-interface) · [Policy](#policy) · [Session Record](#session-record) · [SPMC](#spmc-schema-prompt-model-context) · [Transport](#transport)

[The Lifecycle](#the-lifecycle) — how the entities compose into work.

---

## Entities

### Acknowledgement
*Structural.*

Explicit recognition that a concern doesn't apply, with reasoning. Negative space made positive.

Saying "security doesn't apply to this feature because no trust boundaries are introduced" is a different artifact than silence. The system requires acknowledgements to carry reasoning — bare acknowledgement is rejected as an error.

This entity exists because the audit principle ("did the role have the context a competent human would have?") requires explicit handling of the things deliberately excluded. Silence about a domain is indistinguishable from oversight; acknowledgement makes the choice visible.

### Action
*Primary.*

The execution of a state change against external reality. Distinct from a decision because its outcome is uncertain — actions interact with reality, and reality is partially unknown.

Implementing code is an action. Executing a deployment is an action. Running tests is an action. Sending a notification is an action. Classifying a high-volume signal is an action (interpretive flavor). Reading production logs is an action (sensing flavor).

The distinction between decision and action is structural, not gradient:
- Decisions produce deterministic artifacts. The artifact exists in exactly the form it was written.
- Actions produce uncertain outcomes. The action might succeed, fail, succeed partially, or succeed in ways that introduce unexpected state.

This asymmetry is why every action structurally pairs with an **interpretation** (see below). Decisions don't need that — their products are knowable; their consequences propagate over time and are evaluated asynchronously through audits and downstream consumption.

Actions split along two orthogonal dimensions:
- **Direction** — value actions push outward (system → world); sensing actions pull inward (world → system); some actions sit internal to the graph (e.g., an implementer producing code that other roles consume).
- **Flavor** — pure_execution, generative, or interpretive (see Session below).

The framework's action semantics — uncertainty, interpretation pairing, session record, audit — apply uniformly across both direction and flavor.

### Action-Interpretation Agreement
*Operational.*

A first-class measurement: for action sessions reporting success, how often does the paired interpretation session agree?

Low agreement rates are diagnostic signals. Possible causes split by action direction:
- For value actions: the action is unreliable (claiming success when something went wrong), the interpretation criteria are miscalibrated (rejecting outcomes that should be accepted), or the specification was incomplete (action did exactly what it was told but interpretation has additional standards that weren't expressed upstream).
- For sensing actions: the source is wrong (returning incorrect or stale readings), the interpretation criteria are stale (the response framework doesn't match current reality), or the signal is genuinely ambiguous (no defensible classification exists).

This metric is what makes the framework's audit principle measurable at action boundaries, on both sides of the system/world boundary.

### Application Status
*Structural.*

Every application document carries a status. The status vocabulary is defined normatively by the [Completeness Exercise](../core/02-completeness.md) tiers. Two orthogonal axes; fusing them is a spec error.

**Status — the evidence axis.**

- **projected** — Tier-1 evidence only: derivation clean, no dangling edges. A design.
- **reported** — Tier-2 or Tier-3 evidence from a named system: exercise run, residual recorded, run cited. No citation, no status.

Frozen records — RFCs, contracts — are derivations, not runs. Freezing never changes status.

**Promotion — the location axis.**

A projection frozen into a more stable tier is recorded as a `frozen-as` edge: projection → landing artifact, kept in the application document's Promotion record. The edge records genealogy, not evidence, and adds no dependency: the authoring document never depends on the artifacts its projections landed in. There is no third status value — "promoted" is an edge, not a state.

### Artifact
*Primary.*

The medium by which decisions cross role boundaries. The unit of composition.

An artifact is a durable, inspectable record with a schema, provenance, and form. When a role makes a decision, the decision becomes an artifact the moment it needs to inform another role's decision.

The key principle: artifacts are the only thing that flows between roles. Roles don't talk to each other; they produce and consume artifacts. This is what makes the system composable — swap the model behind a role, the artifact it produces still slots into the same downstream graph.

Artifacts have types. In software development: feature, ADR, test criterion, dependency. In sales: lead, account plan, proposal, contract. In research: hypothesis, protocol, results, manuscript. Each type has a schema.

### Audit
*Operational.*

The infrastructure that checks whether the graph is honest. Three layers, three questions:

**Preflight** — does this role have the context it needs *now*? Checks declared coverage, acknowledgements, link completeness. Runs before a role begins work.

**Gap analysis** — is the context internally complete and consistent? LLM-driven analysis of artifacts against their context bundles, checking for specific gap classes: missing tests, untested invariants, contradictions, unaddressed aspects, stale rationale.

**Drift detection** — does the context still match reality? LLM-driven comparison of artifact claims to the actual implemented state.

Audits produce findings with stable IDs (so suppressions survive across runs), severity levels, and structured output for CI integration. They are the operational expression of "the failure criterion is whether the role had the right context."

The audit principle has a typed version: for decision sessions, the audit asks whether the bundle gave enough basis for the decision; for action sessions, the audit asks whether the specification produced by upstream decision sessions was complete enough to execute against. Action session failures often trace back to decision session inadequacy — the implementer couldn't write working code because the ADR was ambiguous about an error path.

**Audit primitives compose differently at the two convergence boundaries** (see Convergence State). At the **ready boundary**, preflight and gap analysis dominate: the question is whether the focal artifact's upstream context graph is complete and internally consistent enough for downstream work to proceed. Drift detection participates — stale upstream claims block ready. At the **done boundary**, action-interpretation agreement and drift dominate: did the value action's intended state change actually occur, and does the graph now correctly reflect reality? Same primitives, different compositions, evaluated at different points in the chain. The ready predicate and the done predicate are both computable functions over audit outcomes; they're not separate machinery, just different gates the same machinery produces.

### Autonomy Level
*Operational.*

A per-role property, not a per-system property. Currently 0-5, set based on measurement evidence.

- Level 0: human-filled, no AI involvement.
- Level 1: human-filled with AI assistance.
- Level 2: AI-filled with constant human supervision (every output reviewed).
- Level 3: AI-filled with checkpointed human review (specific outputs reviewed).
- Level 4: AI-filled with escalation-based human involvement (humans intervene only on signals the system surfaces).
- Level 5: AI-filled including the meta-work of defining and improving the role.

The system's autonomy level is the floor — the level of its most-supervised role. The path to higher levels is per-role graduation: a role with consistent quality and stable performance moves up; a role with degrading evidence moves down. The orchestration system's policy declarations record the autonomy level per role and the evidence supporting the binding.

The ready boundary is the architecturally privileged location for the most common human-in-the-loop checkpoint — see Convergence State for the typical autonomy-split pattern.

### Bundle
*Primary.*

The packaged, deliverable form of context. An artifact in its own right, assembled from other artifacts.

Where context is the abstract concept, the bundle is the concrete thing: the markdown document, the JSON blob, the file that goes into the role's input. Bundles are deterministically assembled — same graph, same arguments, same bundle. They have their own format and ordering rules. They're measurable: dimensions, size, density, token estimate.

The bundle is the operationalized interface between the graph and the role.

### Bus
*Flow.*

The infrastructure that moves artifacts between systems. Distinct from the harness.

The bus has three responsibilities: terminal artifact pickup (when a system reaches a value action), schema-conformant handoff (validating the inter-system schema before delivery), and receiving-system trigger (creating the inbound artifact in the target system).

The bus is intentionally thin. It does not transform artifacts beyond schema validation. It does not store state beyond what's needed for delivery confirmation. It carries both forward-flow and feedback-flow artifacts identically because from the bus's perspective they are the same: artifacts that orchestration has decided should move between systems.

### Context
*Primary.*

The set of artifacts that condition a specific decision.

Context is what the role sees when it forecasts. Same role, different decisions, different contexts. The architect deciding whether to approve a design reads a different context than the architect deciding whether to retire a deprecated module.

Context isn't free-form — it's a deterministic assembly of artifacts following the graph. "Context for feature X" means "X plus its linked decisions plus their tests plus relevant dependencies." Reproducible because the graph is reproducible.

### Convergence State
*Primary.*

A predicate on a focal artifact's chain, computed continuously from the graph. Convergence states name the cadence-relevant moments where a chain "lands." Two forms.

**Ready.** The focal artifact's upstream context graph is complete and audit-passing — design, spec, verification approach, test criteria, acknowledgements, and any other context downstream work requires are present, coherent, and pass the relevant audits. Ready predicates the focal artifact for downstream work: implementation, deployment, or whatever the next phase calls for.

**Done.** The terminal value action of the chain has fired, its paired interpretation confirms success, and post-action audits (drift, health, action-interpretation agreement) pass. The world has changed and the system has confirmed it.

The framework already supplied the underlying mechanism — phase exit criteria, the feature×domain coverage matrix, gap analysis, preflight audits, drift detection, paired interpretation. Naming the convergence states makes the operational pattern explicit: chains land at ready before they continue to done, and the cadence of work, the audit profiles, and the typical autonomy boundaries all hinge on this distinction.

The vocabulary borrows from agile's "definition of ready" and "definition of done." The fit is good, with the precision DDD adds: ready and done are computable predicates over the graph, not informal team agreements, and the framework's audit and feedback infrastructure operationalizes both.

**The agile refinement parallel.** The ready-chain with feedback iteration is structurally what backlog refinement is in agile, with the framework's discipline applied. Refinement maps to the ready-chain — multiple roles producing upstream context with iterative back-and-forth as gaps surface. Sprint planning maps to the human checkpoint at the ready boundary, the moment work crosses from refinement into execution. Sprint execution maps to the done-chain. Sprint review and demo map to post-action interpretation plus discovery sensing for the next iteration. Retrospective maps to the meta-loop — both observe patterns from completed work and revise the process, with the meta-loop bringing more rigor about evidence. The daily standup has no direct equivalent because the graph itself maintains continuous status visibility; status is observed by querying, not synchronized at 9am.

What DDD makes precise that agile leaves informal: refinement gains a controlled vocabulary (`gap`, `contradiction`, `unimplementable`, `scope-issue`, `unverifiable`) with lifecycle and audit trail per feedback artifact; DoR becomes a computable predicate rather than a team checklist; re-opening ready is a structural feedback mechanism rather than a meeting and a backlog edit; and refinement stops being the PO bottleneck — the chain of decision roles can be filled by workers, shifting human attention to the actually hard decisions (prioritization, strategic choice) rather than mechanical specification work. The framework also addresses several common agile failure modes structurally: items stuck in "almost ready" surface their blocking conditions concretely because the predicate is computable; feedback surfaced in execution gets a permanent audit trail and aggregate pattern visibility rather than being lost; DoR drift across teams disappears because the predicate is shared infrastructure; and the refinement-execution gap closes because the same mechanism gates both.

**Ready isn't a true terminus.** Value-anchoring still holds: every chain ultimately traces to a value action. Ready is the staging plateau where work pauses, possibly batches, possibly waits for a human gate, then continues. The done-chain begins where the ready-chain ends.

**Ready is continuously evaluated.** Downstream feedback can invalidate it. If the verifier can't write verification because the design is underspecified, that's `gap` feedback flowing upstream — it re-opens the readiness gate on the focal artifact. The orchestration system pauses dependent done-chains, re-dispatches upstream roles, and re-converges on a new ready state before resuming. Drift detection plays the symmetric role from the other direction: when implementation reveals reality has moved, upstream context is no longer ready and needs revision.

**Audit profiles differ at the two boundaries.** Ready-boundary audits ask "is this artifact ready for downstream context consumption?" — gap analysis, coverage, link completeness, acknowledgements, traceability. Done-boundary audits ask "did the action succeed and is the resulting state coherent?" — action-interpretation agreement, drift, post-action health. The same audit primitives compose into different gates at the two boundaries; see Audit below.

**Autonomy commonly splits at the ready boundary.** The natural human-checkpoint location for many processes is at ready: the system fully drafts the upstream context (design, spec, verification approach, TCs), a human approves the ready bundle, then the done-chain proceeds. The inverse is also common for low-stakes work: human writes the spec, the system autonomously implements and ships. The ready boundary is architecturally privileged because it's where the most context is concentrated for a single review decision. Orchestration policy declares the split per-feature-type or per-domain.

### Decision
*Primary.*

A context-conditioned forecast made by a role. The unit of work in DDD.

A decision is structurally a forecast: given this context (these artifacts), what is the right next move? Roles produce decisions by reasoning over their bundles. Whether the role is filled by a human or an LLM, the structure is the same — context in, decision out.

Decisions are private to the role. They happen inside the role's reasoning. They only become visible — to other roles, to the system, to audit — when they're externalized as an artifact.

**Decision vs value action.** A decision is internal; a value action is external. Most decisions in a system never become value actions. They produce artifacts that condition other decisions. Only the terminal decision in a chain results in a value action. This is the inversion in operational form.

**Granularity.** Decisions can be traced backwards indefinitely. The framework stops where decisions either become trivial (routine execution within an established frame), fold into a role's standing authority, or reach a sensing action where external reality enters the graph. Below that line is execution; above it is the graph being modeled.

**Decisions are first-class and recorded.** "Private to the role" means a decision is not consumable mid-session by another worker — not that it goes unrecorded. When a worker fills a role, its decisions are made against a recorded bundle in a recorded session, so they are captured the moment they happen. The decision graph (foundations, *Two graphs*) is that capture made total: a queryable record alongside the artifact graph, sharing the session as its seam. What stays private is live access during another role's session; what becomes durable is the decision itself.

**Shared shape.** Every decision, whatever its kind, carries the same core: a `rationale`, the `role` that made it (`madeBy`), a `status` (active, superseded, retracted), an optional `supersededBy`, a `kind` (below), and the session it was made in. Specific kinds add fields — an ADR adds `context`, `consequences`, `alternatives` — but they extend this supertype rather than replacing it. Decision kind is *data on this shape*, not a class hierarchy: the catalog of kinds is open and extensible, and the supertype is the one stable contract. This is the same instinct as capability tags over model identities — encode the invariant structure, push the varying taxonomy into data.

**Two edges, two axes.** A decision relates to its antecedents by two distinct predicates:
- `governed_by` — rises to the **generation decision** that governed its shape (how this kind of artifact is produced). Terminates at role and system-quality authority.
- `derived_from` — rises through prior **subject-matter decisions** that supplied its content. Terminates at domain origin or a sensing action.

These are not two points on one chain; they are orthogonal axes that cross at the session, where a generation decision is applied to domain context to yield subject-matter decisions (foundations, *Two graphs*). The generation/subject-matter distinction is therefore **read from edge topology, not stored as a subtype**: a decision plays the generation role when prompts and produced artifacts hang off its `governed_by`; it plays the subject-matter role when it sits on a produced artifact with a `governed_by` edge of its own. A SPARQL projection over the two edge predicates derives the meta/content layering — never a separately maintained classification, same provenance discipline as everything else.

**Decision kind is keyed by the production unit.** Generation guidance is owned by one role and dispatched as one prompt per artifact type (see Prompt), and that `(role, artifact type)` cell *is* a decision kind. The kind catalog is the projection of the prompt–artifact grid, not a hand-curated list: defining the prompt registers the kind, so a kind cannot exist without the prompt that produces it (open vocabulary, closed registration). An ADR is not a primitive — it is the kind generated by the ADR-writer prompt, sitting wherever its edges place it (subject-matter when it has `derived_from` into a feature's decisions; generation when it governs the system's own construction). The borrowed ADR format gets no special standing; it is one kind among many, registered like the rest.

### Domain
*Structural.*

A concern category that cross-cuts artifacts. Orthogonal to the primary decomposition.

In software: security, networking, observability, error-handling. In enterprise sales: compliance, pricing, technical-fit, deal-terms. Domains let the system check coverage orthogonally — a feature decomposed by what-it-does can still be audited for whether the cross-cutting concerns are addressed.

The feature × domain coverage matrix is the portfolio-level view. Gaps become visible across the whole graph, not just within one artifact.

Domains are explicitly declared in the system's configuration. Artifacts claiming a domain must either link to coverage in that domain or acknowledge its non-applicability with reasoning.

### Domain Knowledge
*Primary.*

An artifact carrying out-of-graph domain expertise, produced to condition a downstream decision.

Some decisions need knowledge that is neither in the graph nor in the model — current platform specifics, a specialist's read on a design. The rule is that such knowledge enters only through the bundle, never through a live call inside the session that consumes it: a live retrieval mid-session would make the worker's output depend on something its bundle doesn't capture, breaking the replayability of the session.

Knowledge therefore enters in one of two frozen forms, chosen by whether producing it is a judgment:
- When producing it is itself a decision — "does this architecture hold up against the platform's guidance, and what should change" — it is the output of a subject-matter-expert *role* (a human, or a worker bound to a knowledge source), captured as a Domain Knowledge artifact that downstream bundles consume.
- When it is a fact lookup with a single correct answer, the bundle assembler retrieves it at assembly time and freezes it into the bundle, hashed with the rest.

A Domain Knowledge artifact carries snapshot provenance for its out-of-graph origin — the source, the query, the time, a content hash — so it stays auditable after the live source has moved on. A subject-matter expert is not new machinery: it is a role, defined by what it decides, producing a Domain Knowledge artifact (forward-flow) or a verification verdict (gating). The distinction that decides where knowledge goes is decision-content first — if there is a call being made, it owes an artifact; if any two lookups would agree, it belongs in bundle assembly.

### Edge
*Structural.*

A typed relationship between artifacts. Declared in the source artifact's representation. Traversable in both directions at query time.

Edge types are part of the schema. They encode specific semantics — not just "connects to" but "this feature is implemented by that decision," "this decision supersedes that one," "this test validates this feature." The graph is the closure over all declared edges.

Two edge types carry the decision graph specifically (see Decision): `governed_by`, from a subject-matter decision up to the generation decision that shaped it, and `derived_from`, from a decision up to the prior subject-matter decisions that supplied its content. The generation/subject-matter layering is the projection over these two predicates, not a stored attribute.

### Eligible
*Structural.*

The shared shape of every registerable, versioned, evidence-gated catalog entry — the abstract supertype behind the model catalog, the worker registry, and the prompt catalog.

Each carries identity and version, a capability surface (capability *tags* for what it offers, capability *requirements* for what it needs), an eligibility status earned through a registration audit (qualified, candidate, deprecated, pulled), and provenance. None of them hard-references another catalog's identities — capabilities are the join, eligibility is the proof. A newly qualified model is automatically a candidate for any prompt whose requirements it meets, with no edits to existing entries.

### Feedback
*Flow.*

An artifact whose semantic purpose is to inform another system's decisions, distinct from the producing system's terminal value action. A first-class flow class, not a peripheral concern.

Every system can produce feedback for every other system. Feedback has its own schema:

- *Identity and provenance* — feedback ID, source system, source artifact, source role, producer (model + version or human), timestamp.
- *Routing target* — target system, target reference (a specific artifact, an artifact type with context, or unspecified for the target's intake to decide).
- *Class* — controlled vocabulary: defect, gap, contradiction, unverifiable, undeployable, unimplementable, operational-finding, capability-request, scope-issue.
- *Severity* — affects routing priority.
- *Evidence* — concrete observations supporting the feedback.
- *Recommendation* — optional; the target system decides what to actually do.
- *Lifecycle state* — produced → routed → received → addressed → closed. Or rejected at any state with reason.
- *Addressing artifact reference* — the artifact in the target system that addresses this feedback.

The lifecycle makes feedback completion trackable. Open feedback is a tracked metric; dropped feedback is a fitness function failure. Rejection from a target produces counter-feedback, which is itself an auditable signal — patterns of rejection from one direction suggest either producer miscalibration or target blind spots.

Feedback also drives readiness re-evaluation. When feedback arrives against a focal artifact in a done-chain, the orchestration system re-evaluates the upstream ready predicate; if the feedback invalidates ready, dependent done-chains pause until the upstream re-converges. This is the structural connection between feedback flow and Convergence State.

### Fitness Function
*Operational.*

Architectural quality metric with a declared threshold, evaluated continuously.

Spec coverage, test coverage, exit-criteria coverage, formal-block coverage, gap density, drift density, gap-resolution rate, action-interpretation agreement rate, dispatch latency, escalation rate, feedback closure rate, ready-state stability (rate at which ready predicates get invalidated by downstream feedback), done-chain duration from ready (cycle time for the done half of a chain), type-decomposability (the fraction of incoming work that decomposes entirely into known TaskTypes — the operational measure of architectural maturity; it climbs as the catalog fills and drops on entry to a new domain, where a sustained drop is an early warning of architectural drift). Each metric has a threshold and a severity (error/warning). The CI gate fails when error-severity thresholds are breached. Trends are tracked over time.

Fitness functions operationalize "the graph stays honest at scale" — not just at any one moment, but over the system's lifetime.

### Flow Class
*Flow.*

The kind of movement an artifact is doing through the graph. Two classes:

**Forward flow.** Artifacts moving toward value actions. The natural direction of work — request becomes feature becomes implementation becomes deployment.

**Feedback flow.** Artifacts moving against the forward direction, carrying information that conditions upstream decisions. A validation rejection routes back to engineering; an operational finding routes back to discovery; a defect report routes back to whichever system produced the defective artifact.

Sensing-action outputs typically enter the graph as forward flow when they originate decision chains (a discovery interview producing a feature request), and as feedback flow when they observe the consequences of prior value actions (a monitoring read producing an operational finding). The classification is by intent and routing, not by the action that produced the artifact.

Both classes use the same artifact-as-interface mechanism. Distinguishing them at the bus and orchestration layers makes routing and auditing cleaner.

### Form
*Structural.*

The structural type of an artifact's content: text, structured, visual, or mixed.

Form determines which models can consume the artifact:
- **Text** — widest model menu, including small models
- **Structured** — cheapest to consume; smallest reliable model works
- **Visual** — requires frontier multimodal capability
- **Mixed** — inherits its strongest form requirement

Form is per-artifact-type, not per-instance. Classifying form is a step in mapping a process: it's the column that tells you which models can fill which roles.

### Harness
*Operational.*

The orchestration executor that invokes models. Outside the systems proper.

The harness owns invocation — which model to call, with what bundle, what to do with the output. It does not own knowledge (that lives in the systems) and it does not own routing decisions (those live in the orchestration system).

In the generic plug-in architecture, the harness is a single reusable implementation that drives any registered system through the stable system interface. Per-role model selection happens via the orchestration system's policy declarations, not in the harness itself; the harness reads the binding and executes the dispatch.

### Interface (System Interface)
*Operational.*

The contract every process system must satisfy to be driven by the generic harness. A small set of operations, domain-independent.

The core operations:
- *list_pending_work* — enumerate artifacts that need a role's attention
- *assemble_bundle* — return the deterministic context bundle for an artifact and role
- *preflight* — run the pre-dispatch audit
- *validate_output* — check whether a proposed output conforms to schema
- *write_output* — persist the output, running post-write audits
- *get_role_definition* — return a role's input/output schemas, form requirements, and session type
- *subscribe_terminal_events* — notify when artifacts reach value actions
- *subscribe_feedback_events* — notify when feedback artifacts are produced
- *receive_inbound* — accept an inbound artifact from another system
- *receive_feedback* — accept a feedback artifact from another system
- *evaluate_ready* — compute the ready predicate for a focal artifact
- *evaluate_done* — compute the done predicate for a focal artifact

Plug-in systems implement the interface against their domain. The orchestration system, harness, and bus depend only on the interface. Adding a new process is implementing the interface and registering.

### Interpretation
*Primary.*

The decision session that consumes an action's output and produces a verdict about what it means.

A test runner executes tests (action) and produces results. A gatekeeper interprets the results and decides whether to ship (interpretation). An implementer produces code (action). A reviewer interprets whether the code matches specification (interpretation). A deployer rolls out a release (action). A post-deploy verifier interprets system health (interpretation). A log query worker pulls metrics (sensing action). An anomaly analyst interprets whether the metrics indicate a problem (interpretation).

Interpretation is its own decision session, paired with the action. Same role catalog mechanics. Same decision-type measurement weighting (quality dominates). Same audit expectations.

**When interpretation folds inline.** For actions with binary success and tight contracts (a schema-validated API call, a deterministic deployment to a fully-managed platform), interpretation can collapse into the action session itself — the action captures the outcome and the orchestration system treats reported success as the default disposition. The default is to split interpretation out; folding it in trades auditability for fewer sessions and is appropriate only when judgment is genuinely mechanical.

### Inter-system Schema
*Flow.*

The schema for an artifact at a system boundary. The contract between producer and consumer systems.

Inter-system schemas are stable interface contracts. A feature specification leaving Discovery must conform to Engineering's intake schema. A validation verdict leaving Validation must conform to Release's intake schema. Schema mismatches at boundaries are the most common cross-system failure mode and are caught at the bus, not inside the receiving system.

### Phase
*Structural.*

A stage in the process with exit criteria. A sequencing mechanism for the graph.

Phases let the graph express "X must complete before Y" at a coarser grain than individual artifact dependencies. Each phase has artifacts (typically a set of features or their equivalent), exit criteria (artifacts of type test or equivalent that must pass), and a gate state (open/locked). The system enforces phase gates by refusing to surface phase-N+1 work while phase-N exit criteria are failing.

Phases are how value-delivery order gets encoded structurally. Phase exit criteria are a coarse-grained instance of the ready predicate (see Convergence State): phase N can't surface its successor's work until its constituent focal artifacts are in done state and its phase-level artifacts are in ready state.

### Policy
*Operational.*

A standing declaration about how the orchestration system behaves. A first-class artifact in the orchestration system.

Policies cover role-to-filler bindings (for a worker: its model, prompt, and permission scope), SLA thresholds, escalation policies, retry policies, autonomy levels, capacity allocations, dispatch triggers (forward-dispatch subscriptions and readiness-re-evaluation subscriptions). Each policy is versioned, has provenance, and can be revised based on measurement evidence.

The policy owner role consumes measurement evidence and produces policy update artifacts. Policy changes are themselves decisions, with their own context (the fit evidence), their own audit (does the evidence actually support the change), and their own provenance. At Level 5 autonomy, the policy owner role itself becomes AI-filled; at lower levels it is human-owned for governance reasons.

### Process
*Primary.*

The real-world activity being modeled. A process is defined by its terminal value actions — the things it produces that create value outside itself.

Software development is a process; its terminal value action is a shipped feature. Sales is a process; its terminal value action is a closed deal. Hiring is a process; its terminal value action is a signed offer.

A process is what gets mapped. It's the unit a system maps one-to-one.

**Gating process.** A process upstream of a value action that decides whether the value action should happen. Validation gates implementation. Deal review gates a closed sale. Peer review gates publication. Safety evaluation gates model deployment. The gating process is its own decision graph with its own roles, artifacts, and terminal value action (the verdict).

**Observing process.** For digital products, a process downstream of a value action that watches what happens and feeds back. Monitoring observes deployed features. Incident response observes production behavior. The observing process exists as a first-class graph because the feedback loop is continuous; the analog for physical products has slower cadence and different structure. Observing processes are sensing-heavy by definition — their primary work is sensing actions that produce operational findings.

### Prompt
*Structural.*

The versioned execution guidance for one role. The *how* that pairs with the schema's *what*.

Prompts live in a catalog parallel to the model catalog: identity-versioned, eligibility-tracked, with provenance. A prompt targets exactly one role *and exactly one artifact type*; reuse across roles is by composition (a shared fragment plus a role-specific body), not by one prompt claiming several roles or several outputs.

**One prompt, one artifact type.** A role that produces three artifact types — say a feature, its test criteria, and an ADR — dispatches three prompts, not one. This is single responsibility applied to the decision graph: a prompt that emitted all three would fuse three distinct sets of generation decisions into one session, and quality triage could no longer separate sound test-case decisions from weak ADR reasoning. The role stays the authority; the prompts are its per-artifact execution units. Each `(role, artifact type)` cell is exactly one decision kind (see Decision), and the generation decisions the prompt encodes are the durable, governing layer that per-artifact subject-matter decisions hang off via `governed_by`. Defining the prompt is what registers the kind — there is no kind without a prompt, and no prompt without a kind.

A consequence worth stating: for any role, the count of artifact types it produces, the count of prompts it dispatches, and the count of decision kinds it originates are the *same number*. A divergence among the three is a malformed graph and a staleness signal.

The split that earns the prompt its own catalog: the role owns the output schema — what a good artifact *is* — so the prompt focuses on execution, how to reason toward the artifact, and the schema-bound part is derived from the role's authority rather than restated.

A prompt declares **capability requirements** against model capability tags (tool-calling, vision, long-context, a reasoning-effort floor) — never specific model identities, which would re-couple the model and prompt catalogs and go stale on every model release. Whether a given model and prompt actually work together is a property of the worker, proven by eligibility, not asserted on the prompt.

Holding schema, model, and bundle fixed, two prompt versions are directly comparable on output quality. The prompt version is therefore the measurement unit for execution, and prompt revision is a normal instance of the meta-loop — measure, propose, validate, apply.

### Provenance
*Structural.*

The record of how an artifact was produced. Who or what produced it, when, from what inputs, at what version, with what configuration.

Provenance is what makes the audit principle operational. When a step fails, you can read what flowed in and what produced it. Without provenance, the graph is a static map; with it, the graph is an executable history.

Provenance fields are part of the schema. Content hashes (for tamper-evidence on artifacts that should be stable once accepted) are part of provenance. Provenance references the session that produced the artifact, bidirectionally — the session record references the artifact, and the artifact references the session record.

Provenance has two axes that meet at the session. The **artifact axis** is the PROV-O lineage above — generated-by, used, associated-with. The **decision axis** is the decision graph (foundations, *Two graphs*; see Decision): what was decided in the session and why, walked by `governed_by` and `derived_from`. The session is the shared node; the artifact axis records what the session produced, the decision axis records the decisions it made, and a process is provenance-complete only when a value-anchored artifact is walkable backward through both. The decision axis is not a second vocabulary layered on PROV-O — it interoperates at the session seam and is recorded as first-class, because the governance edge has no PROV-O analogue.

### Role
*Primary.*

A context bundle plus authority to act on it. The unit of organization.

A role is identified by what it decides, not by an org-chart title. Architect, reviewer, triager, implementer, design lead — these are roles when they correspond to a specific decision class. One person can fill multiple roles. One role can be filled by multiple people or models.

A role has these properties:
- **Context bundle** — the artifacts it consumes to decide
- **Authority** — the artifacts it is allowed to produce
- **Form requirements** — the artifact forms it must be able to read
- **Session type** — decision or action
- **Action flavor** (for action roles) — pure_execution, generative, or interpretive
- **Action direction** (for action roles) — value, sensing, or internal
- **Interpretation pairing** (for action roles) — which decision role interprets its outputs
- **Autonomy level** — currently 0-5, set per-role based on measurement evidence
- **Filler binding** — the human or worker filling this role; a worker carries a model, a prompt, and a permission scope (see Worker)

Form requirements determine which models can fill the role. A design lead consuming Figma files needs a frontier multimodal model. A ticket triager consuming structured text needs almost nothing.

When a role is AI-filled, the thing filling it is a worker (see Worker). The system is composed of many roles, only some of which are filled by workers; one role can be filled by a human or a worker interchangeably, because the interface is the artifact, not the filler.

### Schema
*Structural.*

The contract for an artifact type. Fields (required, optional, format), edges (typed relationships to other artifact types), constraints (validation rules), provenance fields.

A schema is the interface contract that lets any role consume the output of any other. Stable schemas are what make the system composable. Schemas evolve; the system tracks schema versions and migrates artifacts forward.

The schema is owned by the role and versioned with it. Because the role owns the schema, the schema-bound portion of a worker's prompt is derived from it rather than written by hand — schema and prompt cannot drift. A schema-version change moves the target of the work, so it resets the quality baseline for that role rather than being compared across the boundary; a prompt or model change, which holds the target fixed, does not.

### Sensing Action
*Primary.*

The terminal action on the input side. The moment a system reads from external reality, producing an artifact that feeds back into the decision graph as context rather than out into the world as value.

Examples. Monitoring a deployed service. Querying an API for current state. Pulling production logs. Running a user interview. Polling a market signal. Reading a sensor. Compiling research on a technology choice. Receiving an inbound request from a customer or upstream process.

Sensing actions are actions in the strict sense — they execute against external reality, their outcomes are uncertain, and they pair with an interpretation session that turns the raw signal into an inspectable artifact. They take the same three flavors:

- *pure_execution* — mechanical reads against a known interface (log query, metric pull, API fetch). Reliability and latency dominate.
- *generative* — synthesis-shaped reads where the action constructs the artifact from a body of source material (research compilation, market summary). Quality dominates.
- *interpretive* — classification of an incoming signal against a defined response framework (signal triager, anomaly classifier). Accuracy dominates.

The distinction from value actions is direction, not kind. Value actions push value *out* of the system; sensing actions pull information *in*. Both are external; both have uncertain outcomes; both follow the action-interpretation pattern.

**Value-anchoring still holds.** Sensing actions are not terminal in the value-delivery sense — they're upstream nodes whose artifacts feed forward through decisions that eventually land at value. Every subgraph still terminates in a value action. The dual is that every subgraph *originates* in sensing (or an initial request, which is itself sensing the upstream party).

**Interpretation profile differs.** A value-action interpretation asks "did the world change as intended?" A sensing-action interpretation asks "is this reading trustworthy, and what does it mean?" Failure modes split accordingly: a value action can fail because the executor broke; a sensing action can fail because the source is wrong, the interpretation criteria are stale, or the signal is genuinely ambiguous. This argues for a distinct measurement profile per direction when designing the role.

**Where they cluster.** Operations is sensing-heavy downstream of value actions — continuous monitoring producing operational findings that route back via feedback flow. Discovery is sensing-heavy upstream of value actions — user research, technology evaluation, market signals. Both follow the same action semantics; they sit at opposite ends of the graph.

### Session
*Primary.*

One complete invocation of one role on one artifact, from bundle assembly to write-back. The unit of measurement.

A session has a beginning (the harness dispatches the role) and an end (the system accepts the output, rejects it, or escalates it). Sessions are the smallest unit where role-model fit is meaningfully evaluable. They correspond to one role's decision over one bundle — the framework's primary unit of work.

Sessions split into two types:

**Decision session.** Produces an artifact that conditions future decisions. Evaluation is asynchronous (audits, downstream consumption). Quality dominates the fit profile.

**Action session.** Produces a state change in the world or pulls in a reading from the world. Evaluation is synchronous through a paired interpretation session. Quality is more binary; cost and latency matter more.

Action sessions have a flavor:
- *pure_execution* — nearly mechanical (deployer running infrastructure-as-code, test runner invoking a suite, log query worker pulling metrics). Measured on reliability plus cost/latency.
- *generative* — the session generates the artifact that is the action (implementer producing code, drafter producing release notes, research compiler synthesizing a market summary). Measured on quality plus cost/latency.
- *interpretive* — maps a real-world signal onto a defined response framework (signal triager classifying an alert, failure triager interpreting a test result). Measured on classification accuracy plus latency.

Action sessions also carry a direction — value (outward), sensing (inward), or internal — orthogonal to flavor. Direction informs the measurement profile: a value-direction interpretation asks "did the world change as intended"; a sensing-direction interpretation asks "is this reading trustworthy."

### Session Record
*Operational.*

The measurement artifact produced for every session. Lives in the orchestration system.

Four classes of measurement:

**Identity and context.** Session ID, system, role, artifact ID, model + version, prompt + version, schema version, configuration, bundle hash, bundle size, bundle form profile, timestamps, dispatcher rationale. Stamping the full version tuple — Schema, Prompt, Model, Context (SPMC; see below) — is what lets a later quality change be attributed to the one axis that moved; a change touching two of them at once is recorded as confounded.

**Cost.** Input tokens, output tokens, wall-clock time, model time, retry count, tool call costs, dollar cost.

**Quality (immediate, from audits).** Validation outcome, preflight result, post-write audit results, schema conformance, required field population, audit severity distribution.

**Quality (lagging, from downstream consequences).** Downstream rejection, feedback received, amendment rate, drift detection, operational impact, human override. Lagging measurements attach to the session record over time as consequences emerge.

Session records are bidirectionally referenced with the artifacts they produced. Given an artifact, you can find the session that produced it; given a session, you can find its artifact.

### SPMC (Schema, Prompt, Model, Context)
*Operational.*

The four independently-versioned axes a worker session's output quality depends on. Stamped on every session record (above) as one attribution tuple, so a drop in a role's output can be triaged to the single axis that changed.

- **Schema** — what a good artifact *is*, owned by the role (see Schema). A schema-version change moves the target, so it resets the quality baseline rather than being compared across the change.
- **Prompt** — the *how*, the versioned execution guidance, one per `(role, artifact type)` cell (see Prompt).
- **Model** — the concrete, capability-tagged model behind the worker.
- **Context** — the deterministically-assembled, hashable incoming bundle (see Bundle).

The discipline is hold three fixed, vary one: any change in output quality is then attributable to the axis that moved, which is what turns a model migration into a measured swap and a prompt revision into a clean meta-loop instance. The axes are not equal in kind, and the order is read target-first — Schema is the target the worker aims at, Context is the input, Model and Prompt are the worker that maps input to target. Permission scope is a fifth dimension of the worker binding but not an SPMC axis: it governs what a session may *touch*, not the quality of what it produces.

SPMC is the flat, stamped form of an attribution the two graphs also carry structurally. A session's named graph binds Schema, Model, and Context; `governed_by` reaches the Prompt's generation guidance (see Decision, Provenance). So with the decision graph in place the tuple is recoverable by traversal as well as by stamp — the stamp is the fast path, the graph-walk is the audit of record. SPMC is DDD's own term, not borrowed.

### System
*Primary.*

The implementation of the graph. One system per process.

A system is bounded by its process. It has a schema, a graph, an artifact catalog, an interface (typically dual: CLI/UI for humans, MCP/API for LLMs), and audit infrastructure. Product-cli is a system for the software development process. A hypothetical sales-cli would be a system for the sales process — same shape, different schema.

Systems are not application instances; they're the persistent infrastructure of a process. Multiple agents, harnesses, and tools can compose against one system. Where artifacts cross to a different value-action cluster, you have a different system, with an artifact bus between them.

**Orchestration System.** A specific system whose process is the orchestration of all other systems. Its decisions are dispatch (which model for which role for which artifact), schedule (what advances next), escalate (when to route to humans or stronger models), feedback routing (where feedback artifacts go), and policy (standing rules for routing). It is the brain of the composition; the five process systems own their domains; the orchestration system owns the cross-cutting routing decisions. Treated with the same catalog format as any process system.

The orchestration system terminates the regress: there is no meta-orchestration system. The bootstrap layer underneath the orchestration system is a mechanical event loop that executes its decisions. The framework's granularity rule terminates at standing authority, exactly where it terminates for every other system.

### Task
*Primary.*

A recurring sub-unit of work within a process. The composable middle layer between the unit of delivered work and the leaf cell.

A unit of delivered work is rarely a single artifact. A shipped feature is "add an entity" plus "expose an API" plus "wire a migration"; a closed deal is "qualify the lead" plus "scope the solution" plus "negotiate terms." Each of those sub-units is a **task**: a coherent piece of work that produces a *cluster* of related artifacts, not just one. A task sits below the delivered unit (which value-anchors the chain) and above the individual `(role, artifact type)` cell — each cell being one prompt producing one artifact (see Prompt, Decision).

This makes three composition levels, and they form a Stable Dependency stack — dependencies point down the stability gradient and never up. A **cell** depends on nothing above it (a prompt is the most stable thing and changes least). A **task** is defined purely by its cell cluster and their ordering; it composes cells but never reaches up into the delivered unit. The **delivered unit** composes tasks but never reaches down past a task into its cells. This is the same discipline as the crate and slice boundaries in the implementation doc, applied to work decomposition — and it is what lets each layer's catalog stabilize without thrashing the layer beneath it.

A task is not a system. Tasks and cells are sub-processes serving one terminal value action — modules within a system, not independent systems, by the boundary rule (a system boundary exists only where artifacts cross to a different value-action cluster). Decomposing work into tasks never spawns new systems; it is internal structure.

### TaskType
*Primary.*

The registered, versioned definition of how a recurring task decomposes. A catalog entry, in the `Eligible` family alongside the model, worker, and prompt catalogs.

When a task recurs often enough to be worth standardizing, its structure is captured once as a TaskType carrying:
- **The cell cluster** — which artifact types this task decomposes into.
- **The dependency order** — the `derived_from` edges among the cells (what must precede what; what runs in parallel). This is the task's own internal decision graph, declared once.
- **The prompt binding per cell** — which `(role, artifact type)` prompt fills each cell. Because one prompt is one decision kind (see Prompt, Decision), the cell cluster is also a set of decision kinds.
- **The coherence audit** — the cross-cell consistency shape the task requires (the artifacts in the cluster must agree where they overlap).
- **A recognition signature** — what marks an incoming task as being of this type, so a classifier can match it.

A TaskType is *born* through a frozen boundary like all domain knowledge: typifying an exploratory build is a judgment call, so it is produced as Pattern A — an architect-as-SME role generalizing from the originating session into a TaskType artifact, with provenance, not auto-derived from one example. It is *reused* mechanically: a classifier matches incoming work to a type, and dispatch instantiates the cluster, assembles bundles in the declared order, binds the prompts, and runs the coherence audit. It is *evolved* on the meta-loop: a coherence audit that keeps failing means the decomposition is wrong (a cell deciding things that should be split out, or two cells that are really one), and the architect revises the type as a normal versioned change.

TaskTypes are why a system gets cheaper over time rather than just bigger (see Foundations, maturation). They are not specific to software: any process with complex, recurring artifact generation — engineering, sales proposals, clinical documentation, research protocols — accumulates a TaskType catalog as its recurring work gets recognized and standardized. Work whose type is known dispatches its cluster cheaply; work whose type is unknown routes to a broad worker that handles it and may mint a new type.

### Transport
*Operational.*

The protocol by which clients access a system. Multiple transports, one tool surface.

CLI for humans on the same machine. MCP/stdio for local agents. MCP/HTTP for remote agents — including phone-based clients. Same operations underneath; the transport is just delivery.

This is the operational expression of the single-interface principle. Multiple transports for multiple populations, one tool surface so they can't diverge.

### Value Action
*Primary.*

The terminal world-changing act. The thing the organization gets paid, judged, or graded on. The moment a decision chain actualizes against external reality.

In software: deploying code, releasing a feature, sending a customer notification. In sales: signing a contract, taking payment. In healthcare: administering treatment, discharging a patient. In an LLM agent context: invoking a tool that has external effect — sending an email, creating a ticket, transferring funds, deploying code.

The crucial property: value actions are external. They cross a boundary out of the system. A handoff between two internal roles is not a value action; sending a finished deliverable to a customer is.

Three tests:
- Does the organization get paid, judged, or graded on it?
- Does it cross an external boundary?
- If it stopped happening, would someone outside the team notice?

In current LLM systems, value actions correspond to tool calls with side effects. They are what agent frameworks make first-class. DDD makes them last-class — important, but terminal, not central.

**Contrast with sensing action.** Sensing actions are the dual — terminal-flavored actions whose product flows back into the graph as context rather than out into the world as value. Together they define the system's two boundaries with the world.

### Worker
*Primary.*

The concrete realization of a role when an LLM fills it. A role is filled by either a human or a worker — and under the law's [actor spectrum](../core/01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable), these are not two mechanisms but **one dispatch decision at two binding resolutions**. Filling a role means designating an actor whose certified capability envelope covers the role's requirements. For a worker the binding pins a distribution (model version + prompt version — instance-general, stable until changed); for a human it pins a classification envelope (seniority, certification, qualification — individual, expiring, institutionally maintained). Same selection logic, different verdict resolution.

A worker is the binding of three things: a model (selected by capability tag, not by name), a prompt (the versioned execution guidance), and a permission scope (the tools and side effects it may use). It runs as the stateless `bundle → artifact` function of the worker contract (conformance doc §5); the model and prompt are resolved from the binding at dispatch, not baked into the worker.

**Capability tags are the actor-general concept here, not a model-catalog convenience.** Human role-matching has run on them for centuries — rank, title, type rating, board certification are capability tags over human actors, cached verdicts of sampled qualification. The model catalog's tags extend an existing institution to the first bindable non-human actor; declaring requirements against tags rather than identities is what lets one role interface dispatch over both actor types without knowing which it got.

A worker sits behind the role interface. The only thing crossing a role boundary is the artifact, and that is governed by the role's authority — not the worker. Swap the worker, or replace it with a human, and the downstream graph is unaffected. This is the single-interface principle made literal: humans and workers are two fillers of one interface.

Two authorities stay separate:
- **Artifact authority** — what may be produced. Lives on the role. Interface-level; identical whether a human or a worker fills it.
- **Permission scope** — what may be touched during execution: which tools and effect-producing actions, which secrets, which sandbox. Lives on the worker. Implementation-level.

A worker binding is *valid* when its prompt targets the role, its model satisfies the role's form requirements and the prompt's capability requirements, and its permission scope covers the role's value actions. Validity is a static check. *Eligibility* — whether the binding is trusted to run, and at what autonomy level — is earned separately from session evidence, the same qualified/candidate/deprecated lifecycle the model catalog uses. This lifecycle is the machine instance of human certification, with one resolution difference the [actor spectrum](../core/01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable) predicts: a worker's eligibility verdict is stable until an SPMC axis changes (re-qualification is *event-driven*), while a human's decays with drift (re-qualification is *cadence-driven* — recertification, currency windows). A conformant system dispatching humans in roles should therefore attach expiry to human eligibility where it attaches version-invalidation to worker eligibility.

Vocabulary note: "agent" in current LLM frameworks means the whole reasoning-and-acting loop; in DDD that loop is a worker filling one role.

---

## The Lifecycle

How the entities compose into work. A chain originates at the input boundary — either a sensing action reading from external reality, or an initial request arriving from an upstream party — and terminates at a value action, the output boundary where the world changes:

1. A **role** receives a **bundle** assembled from **artifacts** via the **graph**.
2. The role makes a **decision** (or executes an **action** — value, sensing, or internal) — a **session** is recorded.
3. The session's output is externalized as a new **artifact** with **provenance**.
4. **Audits** check whether the bundle was sufficient and the output is sound.
5. If the session was an action, an **interpretation** session pairs with it to produce a verdict.
6. The new artifact enters the graph and becomes context for downstream **roles**.
7. If the artifact is a **feedback** artifact, it routes through the **bus** to a target system via **orchestration**.
8. If the artifact reaches a terminal value action, it crosses the bus to the next system.
9. **Session records** accumulate measurement evidence; **policy** decisions revise **model bindings** and **autonomy levels** based on the evidence.
10. Eventually, a terminal decision in a chain produces an artifact that triggers a **value action** — a deployment, a sent message, a closed deal. The world changes.

Chains commonly land at a **ready convergence state** before continuing toward **done**. The ready-chain produces the validated upstream context (design, spec, verification approach, TCs, acknowledgements) and pauses; the done-chain runs from there through the value action and its interpretation. The pause at ready is the natural place for human checkpoints and batched commitment. Downstream feedback can re-open the ready state, causing the orchestration system to pause dependent done-chains until the upstream re-converges.

The crucial pattern: most decisions don't trigger value actions. They condition other decisions. The graph is mostly internal forecasting; only the leaves cross out into the world (value actions), and only the roots cross in from it (sensing actions). The framework's discipline applies to itself — the orchestration system, the measurement system, the policy decisions are all themselves decisions, audited and improvable through the same mechanisms.

This is the inversion stated structurally. Current LLM agent design optimizes the tool call. DDD optimizes the chain of decisions between the sensing actions that bring information in and the value actions that push value out — that determines whether the tool call should happen, what it should look like, and whether anyone should care.
