# Decision-Driven Design: Entity Reference

The framework's vocabulary, organized around its central inversion: decisions are the work, value actions are the terminus.

## The inversion

Current LLM agent frameworks treat the **tool call** as the primary output unit. An agent reasons — ephemerally, inside its context — and then acts via a tool call. The tool call is the thing: the function, the API invocation, the side effect. Everything before it is preamble.

Decision-Driven Design inverts this. The **decision** is the primary output unit. A decision is a context-conditioned forecast that produces a durable, inspectable artifact. Most decisions never touch the world; they shape the context for other decisions. Tool calls — the moments the world actually changes — sit only at the terminal nodes of the graph, where a chain of decisions finally executes against external reality.

This isn't a refinement of agentic design. It's a different geometry. The agent loop is one node in the graph; the graph is the system. The work is the decisions, plural, distributed across roles, recorded as artifacts. The tool call is just where value lands.

The vocabulary below makes this geometry precise.

---

## Primary Entities

### Process

The real-world activity being modeled. A process is defined by its terminal value actions — the things it produces that create value outside itself.

Software development is a process; its terminal value action is a shipped feature. Sales is a process; its terminal value action is a closed deal. Hiring is a process; its terminal value action is a signed offer.

A process is what gets mapped. It's the unit a system maps one-to-one.

**Gating process.** A process upstream of a value action that decides whether the value action should happen. Validation gates implementation. Deal review gates a closed sale. Peer review gates publication. Safety evaluation gates model deployment. The gating process is its own decision graph with its own roles, artifacts, and terminal value action (the verdict).

**Observing process.** For digital products, a process downstream of a value action that watches what happens and feeds back. Monitoring observes deployed features. Incident response observes production behavior. The observing process exists as a first-class graph because the feedback loop is continuous; the analog for physical products has slower cadence and different structure.

### Value Action

The terminal world-changing act. The thing the organization gets paid, judged, or graded on. The moment a decision chain actualizes against external reality.

In software: deploying code, releasing a feature, sending a customer notification. In sales: signing a contract, taking payment. In healthcare: administering treatment, discharging a patient. In an LLM agent context: invoking a tool that has external effect — sending an email, creating a ticket, transferring funds, deploying code.

The crucial property: value actions are external. They cross a boundary out of the system. A handoff between two internal roles is not a value action; sending a finished deliverable to a customer is.

Three tests:
- Does the organization get paid, judged, or graded on it?
- Does it cross an external boundary?
- If it stopped happening, would someone outside the team notice?

In current LLM systems, value actions correspond to tool calls with side effects. They are what agent frameworks make first-class. DDD makes them last-class — important, but terminal, not central.

### Decision

A context-conditioned forecast made by a role. The unit of work in DDD.

A decision is structurally a forecast: given this context (these artifacts), what is the right next move? Roles produce decisions by reasoning over their bundles. Whether the role is filled by a human or an LLM, the structure is the same — context in, decision out.

Decisions are private to the role. They happen inside the role's reasoning. They only become visible — to other roles, to the system, to audit — when they're externalized as an artifact.

**Decision vs value action.** A decision is internal; a value action is external. Most decisions in a system never become value actions. They produce artifacts that condition other decisions. Only the terminal decision in a chain results in a value action. This is the inversion in operational form.

**Granularity.** Decisions can be traced backwards indefinitely. The framework stops where decisions either become trivial (routine execution within an established frame) or fold into a role's standing authority. Below that line is execution; above it is the graph being modeled.

### Action

The execution of a state change against external reality. Distinct from a decision because its outcome is uncertain — actions interact with reality, and reality is partially unknown.

Implementing code is an action. Executing a deployment is an action. Running tests is an action. Sending a notification is an action. Classifying a high-volume signal is an action (interpretive flavor).

The distinction between decision and action is structural, not gradient:
- Decisions produce deterministic artifacts. The artifact exists in exactly the form it was written.
- Actions produce uncertain outcomes. The action might succeed, fail, succeed partially, or succeed in ways that introduce unexpected state.

This asymmetry is why every action structurally pairs with an **interpretation** (see below). Decisions don't need that — their products are knowable; their consequences propagate over time and are evaluated asynchronously through audits and downstream consumption.

### Interpretation

The decision session that consumes an action's output and produces a verdict about what it means.

A test runner executes tests (action) and produces results. A gatekeeper interprets the results and decides whether to ship (interpretation). An implementer produces code (action). A reviewer interprets whether the code matches specification (interpretation). A deployer rolls out a release (action). A post-deploy verifier interprets system health (interpretation).

Interpretation is its own decision session, paired with the action. Same role catalog mechanics. Same decision-type measurement weighting (quality dominates). Same audit expectations.

**When interpretation folds inline.** For actions with binary success and tight contracts (a schema-validated API call, a deterministic deployment to a fully-managed platform), interpretation can collapse into the action session itself — the action captures the outcome and the orchestration system treats reported success as the default disposition. The default is to split interpretation out; folding it in trades auditability for fewer sessions and is appropriate only when judgment is genuinely mechanical.

### Role

A context bundle plus authority to act on it. The unit of organization.

A role is identified by what it decides, not by an org-chart title. Architect, reviewer, triager, implementer, design lead — these are roles when they correspond to a specific decision class. One person can fill multiple roles. One role can be filled by multiple people or models.

A role has these properties:
- **Context bundle** — the artifacts it consumes to decide
- **Authority** — the artifacts it is allowed to produce
- **Form requirements** — the artifact forms it must be able to read
- **Session type** — decision or action
- **Action flavor** (for action roles) — pure_execution, generative, or interpretive
- **Interpretation pairing** (for action roles) — which decision role interprets its outputs
- **Autonomy level** — currently 0-5, set per-role based on measurement evidence
- **Model binding** — the model currently filling this role, when AI-filled

Form requirements determine which models can fill the role. A design lead consuming Figma files needs a frontier multimodal model. A ticket triager consuming structured text needs almost nothing.

Note the vocabulary clash with current LLM frameworks: "agent" in that world means the whole reasoning-and-acting loop; in DDD, an agent is the implementation choice for filling a single role. The system is composed of many roles, only some of which are filled by agents.

### Artifact

The medium by which decisions cross role boundaries. The unit of composition.

An artifact is a durable, inspectable record with a schema, provenance, and form. When a role makes a decision, the decision becomes an artifact the moment it needs to inform another role's decision.

The key principle: artifacts are the only thing that flows between roles. Roles don't talk to each other; they produce and consume artifacts. This is what makes the system composable — swap the model behind a role, the artifact it produces still slots into the same downstream graph.

Artifacts have types. In software development: feature, ADR, test criterion, dependency. In sales: lead, account plan, proposal, contract. In research: hypothesis, protocol, results, manuscript. Each type has a schema.

### Context

The set of artifacts that condition a specific decision.

Context is what the role sees when it forecasts. Same role, different decisions, different contexts. The architect deciding whether to approve a design reads a different context than the architect deciding whether to retire a deprecated module.

Context isn't free-form — it's a deterministic assembly of artifacts following the graph. "Context for feature X" means "X plus its linked decisions plus their tests plus relevant dependencies." Reproducible because the graph is reproducible.

### Bundle

The packaged, deliverable form of context. An artifact in its own right, assembled from other artifacts.

Where context is the abstract concept, the bundle is the concrete thing: the markdown document, the JSON blob, the file that goes into the role's input. Bundles are deterministically assembled — same graph, same arguments, same bundle. They have their own format and ordering rules. They're measurable: dimensions, size, density, token estimate.

The bundle is the operationalized interface between the graph and the role.

### Session

One complete invocation of one role on one artifact, from bundle assembly to write-back. The unit of measurement.

A session has a beginning (the harness dispatches the role) and an end (the system accepts the output, rejects it, or escalates it). Sessions are the smallest unit where role-model fit is meaningfully evaluable. They correspond to one role's decision over one bundle — the framework's primary unit of work.

Sessions split into two types:

**Decision session.** Produces an artifact that conditions future decisions. Evaluation is asynchronous (audits, downstream consumption). Quality dominates the fit profile.

**Action session.** Produces a state change in the world. Evaluation is synchronous through a paired interpretation session. Quality is more binary; cost and latency matter more.

Action sessions have a flavor:
- *pure_execution* — nearly mechanical (deployer running infrastructure-as-code, test runner invoking a suite). Measured on reliability plus cost/latency.
- *generative* — the session generates the artifact that is the action (implementer producing code, drafter producing release notes). Measured on quality plus cost/latency.
- *interpretive* — maps a real-world signal onto a defined response framework (signal triager classifying an alert, failure triager interpreting a test result). Measured on classification accuracy plus latency.

### System

The implementation of the graph. One system per process.

A system is bounded by its process. It has a schema, a graph, an artifact catalog, an interface (typically dual: CLI/UI for humans, MCP/API for LLMs), and audit infrastructure. Product-cli is a system for the software development process. A hypothetical sales-cli would be a system for the sales process — same shape, different schema.

Systems are not application instances; they're the persistent infrastructure of a process. Multiple agents, harnesses, and tools can compose against one system. Where artifacts cross to a different value-action cluster, you have a different system, with an artifact bus between them.

**Orchestration System.** A specific system whose process is the orchestration of all other systems. Its decisions are dispatch (which model for which role for which artifact), schedule (what advances next), escalate (when to route to humans or stronger models), feedback routing (where feedback artifacts go), and policy (standing rules for routing). It is the brain of the composition; the five process systems own their domains; the orchestration system owns the cross-cutting routing decisions. Treated with the same catalog format as any process system.

The orchestration system terminates the regress: there is no meta-orchestration system. The bootstrap layer underneath the orchestration system is a mechanical event loop that executes its decisions. The framework's granularity rule terminates at standing authority, exactly where it terminates for every other system.

---

## Structural Entities

These describe the shape and connection of primary entities.

### Schema

The contract for an artifact type. Fields (required, optional, format), edges (typed relationships to other artifact types), constraints (validation rules), provenance fields.

A schema is the interface contract that lets any role consume the output of any other. Stable schemas are what make the system composable. Schemas evolve; the system tracks schema versions and migrates artifacts forward.

### Edge

A typed relationship between artifacts. Declared in the source artifact's representation. Traversable in both directions at query time.

Edge types are part of the schema. They encode specific semantics — not just "connects to" but "this feature is implemented by that decision," "this decision supersedes that one," "this test validates this feature." The graph is the closure over all declared edges.

### Provenance

The record of how an artifact was produced. Who or what produced it, when, from what inputs, at what version, with what configuration.

Provenance is what makes the audit principle operational. When a step fails, you can read what flowed in and what produced it. Without provenance, the graph is a static map; with it, the graph is an executable history.

Provenance fields are part of the schema. Content hashes (for tamper-evidence on artifacts that should be stable once accepted) are part of provenance. Provenance references the session that produced the artifact, bidirectionally — the session record references the artifact, and the artifact references the session record.

### Form

The structural type of an artifact's content: text, structured, visual, or mixed.

Form determines which models can consume the artifact:
- **Text** — widest model menu, including small models
- **Structured** — cheapest to consume; smallest reliable model works
- **Visual** — requires frontier multimodal capability
- **Mixed** — inherits its strongest form requirement

Form is per-artifact-type, not per-instance. Classifying form is a step in mapping a process: it's the column that tells you which models can fill which roles.

### Domain

A concern category that cross-cuts artifacts. Orthogonal to the primary decomposition.

In software: security, networking, observability, error-handling. In enterprise sales: compliance, pricing, technical-fit, deal-terms. Domains let the system check coverage orthogonally — a feature decomposed by what-it-does can still be audited for whether the cross-cutting concerns are addressed.

The feature × domain coverage matrix is the portfolio-level view. Gaps become visible across the whole graph, not just within one artifact.

Domains are explicitly declared in the system's configuration. Artifacts claiming a domain must either link to coverage in that domain or acknowledge its non-applicability with reasoning.

### Phase

A stage in the process with exit criteria. A sequencing mechanism for the graph.

Phases let the graph express "X must complete before Y" at a coarser grain than individual artifact dependencies. Each phase has artifacts (typically a set of features or their equivalent), exit criteria (artifacts of type test or equivalent that must pass), and a gate state (open/locked). The system enforces phase gates by refusing to surface phase-N+1 work while phase-N exit criteria are failing.

Phases are how value-delivery order gets encoded structurally.

### Acknowledgement

Explicit recognition that a concern doesn't apply, with reasoning. Negative space made positive.

Saying "security doesn't apply to this feature because no trust boundaries are introduced" is a different artifact than silence. The system requires acknowledgements to carry reasoning — bare acknowledgement is rejected as an error.

This entity exists because the audit principle ("did the role have the context a competent human would have?") requires explicit handling of the things deliberately excluded. Silence about a domain is indistinguishable from oversight; acknowledgement makes the choice visible.

---

## Flow Entities

These describe how artifacts and signals move through and between systems.

### Flow Class

The kind of movement an artifact is doing through the graph. Two classes:

**Forward flow.** Artifacts moving toward value actions. The natural direction of work — request becomes feature becomes implementation becomes deployment.

**Feedback flow.** Artifacts moving against the forward direction, carrying information that conditions upstream decisions. A validation rejection routes back to engineering; an operational finding routes back to discovery; a defect report routes back to whichever system produced the defective artifact.

Both classes use the same artifact-as-interface mechanism. Distinguishing them at the bus and orchestration layers makes routing and auditing cleaner.

### Feedback

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

### Bus

The infrastructure that moves artifacts between systems. Distinct from the harness.

The bus has three responsibilities: terminal artifact pickup (when a system reaches a value action), schema-conformant handoff (validating the inter-system schema before delivery), and receiving-system trigger (creating the inbound artifact in the target system).

The bus is intentionally thin. It does not transform artifacts beyond schema validation. It does not store state beyond what's needed for delivery confirmation. It carries both forward-flow and feedback-flow artifacts identically because from the bus's perspective they are the same: artifacts that orchestration has decided should move between systems.

### Inter-system Schema

The schema for an artifact at a system boundary. The contract between producer and consumer systems.

Inter-system schemas are stable interface contracts. A feature specification leaving Discovery must conform to Engineering's intake schema. A validation verdict leaving Validation must conform to Release's intake schema. Schema mismatches at boundaries are the most common cross-system failure mode and are caught at the bus, not inside the receiving system.

---

## Operational Entities

These describe the runtime and process layer.

### Audit

The infrastructure that checks whether the graph is honest. Three layers, three questions:

**Preflight** — does this role have the context it needs *now*? Checks declared coverage, acknowledgements, link completeness. Runs before a role begins work.

**Gap analysis** — is the context internally complete and consistent? LLM-driven analysis of artifacts against their context bundles, checking for specific gap classes: missing tests, untested invariants, contradictions, unaddressed aspects, stale rationale.

**Drift detection** — does the context still match reality? LLM-driven comparison of artifact claims to the actual implemented state.

Audits produce findings with stable IDs (so suppressions survive across runs), severity levels, and structured output for CI integration. They are the operational expression of "the failure criterion is whether the role had the right context."

The audit principle has a typed version: for decision sessions, the audit asks whether the bundle gave enough basis for the decision; for action sessions, the audit asks whether the specification produced by upstream decision sessions was complete enough to execute against. Action session failures often trace back to decision session inadequacy — the implementer couldn't write working code because the ADR was ambiguous about an error path.

### Harness

The orchestration executor that invokes models. Outside the systems proper.

The harness owns invocation — which model to call, with what bundle, what to do with the output. It does not own knowledge (that lives in the systems) and it does not own routing decisions (those live in the orchestration system).

In the generic plug-in architecture, the harness is a single reusable implementation that drives any registered system through the stable system interface. Per-role model selection happens via the orchestration system's policy declarations, not in the harness itself; the harness reads the binding and executes the dispatch.

### Transport

The protocol by which clients access a system. Multiple transports, one tool surface.

CLI for humans on the same machine. MCP/stdio for local agents. MCP/HTTP for remote agents — including phone-based clients. Same operations underneath; the transport is just delivery.

This is the operational expression of the single-interface principle. Multiple transports for multiple populations, one tool surface so they can't diverge.

### Interface (System Interface)

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

Plug-in systems implement the interface against their domain. The orchestration system, harness, and bus depend only on the interface. Adding a new process is implementing the interface and registering.

### Policy

A standing declaration about how the orchestration system behaves. A first-class artifact in the orchestration system.

Policies cover role-to-model bindings, SLA thresholds, escalation policies, retry policies, autonomy levels, capacity allocations. Each policy is versioned, has provenance, and can be revised based on measurement evidence.

The policy owner role consumes measurement evidence and produces policy update artifacts. Policy changes are themselves decisions, with their own context (the fit evidence), their own audit (does the evidence actually support the change), and their own provenance. At Level 5 autonomy, the policy owner role itself becomes AI-filled; at lower levels it is human-owned for governance reasons.

### Session Record

The measurement artifact produced for every session. Lives in the orchestration system.

Four classes of measurement:

**Identity and context.** Session ID, system, role, artifact ID, model + version, configuration, bundle hash, bundle size, bundle form profile, timestamps, dispatcher rationale.

**Cost.** Input tokens, output tokens, wall-clock time, model time, retry count, tool call costs, dollar cost.

**Quality (immediate, from audits).** Validation outcome, preflight result, post-write audit results, schema conformance, required field population, audit severity distribution.

**Quality (lagging, from downstream consequences).** Downstream rejection, feedback received, amendment rate, drift detection, operational impact, human override. Lagging measurements attach to the session record over time as consequences emerge.

Session records are bidirectionally referenced with the artifacts they produced. Given an artifact, you can find the session that produced it; given a session, you can find its artifact.

### Action-Interpretation Agreement

A first-class measurement: for action sessions reporting success, how often does the paired interpretation session agree?

Low agreement rates are diagnostic signals. Possible causes: the action is unreliable (claiming success when something went wrong), the interpretation criteria are miscalibrated (rejecting outcomes that should be accepted), or the specification was incomplete (action did exactly what it was told but interpretation has additional standards that weren't expressed upstream).

This metric is what makes the framework's audit principle measurable at action boundaries.

### Fitness Function

Architectural quality metric with a declared threshold, evaluated continuously.

Spec coverage, test coverage, exit-criteria coverage, formal-block coverage, gap density, drift density, gap-resolution rate, action-interpretation agreement rate, dispatch latency, escalation rate, feedback closure rate. Each metric has a threshold and a severity (error/warning). The CI gate fails when error-severity thresholds are breached. Trends are tracked over time.

Fitness functions operationalize "the graph stays honest at scale" — not just at any one moment, but over the system's lifetime.

### Autonomy Level

A per-role property, not a per-system property. Currently 0-5, set based on measurement evidence.

- Level 0: human-filled, no AI involvement.
- Level 1: human-filled with AI assistance.
- Level 2: AI-filled with constant human supervision (every output reviewed).
- Level 3: AI-filled with checkpointed human review (specific outputs reviewed).
- Level 4: AI-filled with escalation-based human involvement (humans intervene only on signals the system surfaces).
- Level 5: AI-filled including the meta-work of defining and improving the role.

The system's autonomy level is the floor — the level of its most-supervised role. The path to higher levels is per-role graduation: a role with consistent quality and stable performance moves up; a role with degrading evidence moves down. The orchestration system's policy declarations record the autonomy level per role and the evidence supporting the binding.

---

## The Lifecycle

How the entities compose into work:

1. A **role** receives a **bundle** assembled from **artifacts** via the **graph**.
2. The role makes a **decision** (or executes an **action**) — a **session** is recorded.
3. The session's output is externalized as a new **artifact** with **provenance**.
4. **Audits** check whether the bundle was sufficient and the output is sound.
5. If the session was an action, an **interpretation** session pairs with it to produce a verdict.
6. The new artifact enters the graph and becomes context for downstream **roles**.
7. If the artifact is a **feedback** artifact, it routes through the **bus** to a target system via **orchestration**.
8. If the artifact reaches a terminal value action, it crosses the bus to the next system.
9. **Session records** accumulate measurement evidence; **policy** decisions revise **model bindings** and **autonomy levels** based on the evidence.
10. Eventually, a terminal decision in a chain produces an artifact that triggers a **value action** — a deployment, a sent message, a closed deal. The world changes.

The crucial pattern: most decisions don't trigger value actions. They condition other decisions. The graph is mostly internal forecasting; only the leaves cross out into the world. And the framework's discipline applies to itself — the orchestration system, the measurement system, the policy decisions are all themselves decisions, audited and improvable through the same mechanisms.

This is the inversion stated structurally. Current LLM agent design optimizes the tool call. DDD optimizes the chain of decisions that determines whether the tool call should happen, what it should look like, and whether anyone should care.
