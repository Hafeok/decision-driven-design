# DDD Applied: Decisions, Roles, and Artifacts

> **Apparatus §1 — informative.** The [core](../core/) states one law: for a decision, the determination demand is constant and lives across four stores. This tier is that law *run against a real domain*. Before the roles, bundles, and orchestration, this document establishes the geometry they all sit in: work is a graph of decisions between two world boundaries, decisions are private and artifacts are what crosses between them, and an LLM-run process makes a second graph — the decisions themselves — recordable for the first time.

## From law to apparatus

The core answers *what it takes* to make a decision well: move its required knowledge out of judgment and into the encoded and mechanically-verified stores, down to the [Polanyi floor](../core/03-the-polanyi-floor.md). It does not say *how to arrange a real organization's work* so that happens. That is this tier's job.

Applying the law to a domain means answering, concretely: which decisions exist, who owns each, what knowledge each consumes, how that knowledge is packaged and transmitted, and how the whole thing is kept inspectable while it runs. The vocabulary for that — role, artifact, session, bundle, phase, orchestration — is the apparatus. It is *one* concrete way to run the law; the law is the invariant, the apparatus is the application.

## The premise, applied

An LLM is a knowledge forecaster; so is a person. A work process — sales, design, research, engineering — is a chain of context-conditioned decisions that eventually produces something the world cares about. Organizations exist to perform **value actions**: shipping a product, closing a deal, treating a patient, publishing a paper. Every value action is preceded by a chain of decisions that determines whether, when, and how it happens.

So the thing to model is not the org chart and not the process flow, but the **decision graph upstream of each value action.** Map value-backward: start from what the organization actually produces, and trace back through the decisions that had to occur for it to happen.

## The two world boundaries

Value actions are where the system acts *on* the world. The dual boundary is where it reads *from* the world — **sensing actions**: monitoring a deployed feature, pulling production logs, querying an API, interviewing a user, polling a market signal.

Sensing actions execute against external reality the same way value actions do; their outcomes are equally uncertain; they need the same interpretation to be useful. Their job is to bring information *in* rather than push value *out*. The geometry of a real process therefore has two world boundaries: **sensing on the input side, value actions on the output side, decisions in between.** This is the law's temporal structure — inspect facts, decide, act, verify ([core §1](../core/01-the-law.md#the-demand-is-denominated-in-decisions)) — made spatial: sensing is fact-inspection, the value action is the constrained act, and the graph between them is where the governing decisions get made and owned. The [environment clause](../core/01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable) rides the same geometry: sensed facts bind at fire-time at the input boundary; everything between the boundaries is where frozen context is authored.

Value-anchoring holds: every subgraph terminates in a value action. The dual holds too: every subgraph *originates* in sensing — a continuous sense (monitoring), a triggered sense (a probe authorized upstream), or an initial request (itself a sense of an upstream party: customer, PM, calling process). Map value-backward to find the chain; map sensing-forward to find its origin.

## The inversion

Current LLM agent frameworks treat the **tool call** as the primary output unit. An agent reasons — ephemerally, inside its context — then acts via a tool call. Everything before it is preamble.

DDD inverts this. The **decision** is the primary output unit: a context-conditioned forecast that produces a durable, inspectable artifact. Most decisions never touch the world; they shape the context for other decisions. Tool calls — the moments the world changes — sit only at the terminal nodes of the graph. This is not a refinement of agentic design; it is a different geometry. The agent loop is *one node* in the graph; the graph is the system.

| | Agent-centric design | Decision-Driven Design |
|---|---|---|
| **Primary unit** | The tool call | The decision |
| **System shape** | An agent loop | A DAG of roles |
| **Role boundary** | "The agent" | Many roles, swappable |
| **Composition** | Tool wrapping | Artifacts with schemas |
| **What's audited** | The trajectory | Each session, bundle, artifact, decision |
| **Where humans fit** | Approval at the end | Any role, any checkpoint, per-role autonomy |
| **Failure mode** | Opaque | Localized to a role and a bundle |

Agent loops are not wrong — they are one valid node. The point is that for real organizational work, the graph *upstream* of the loop is most of the engineering, and treating it as first-class is what makes the system bounded, auditable, and improvable.

![Overview of the role pattern and the DAG composition.](assets/overview.svg)

## The unit of work and the unit of composition

**The unit of work is the decision. The unit of composition is the artifact.**

Decisions are private to a role — they are what the role does, internally, by forecasting over its context. Artifacts are how decisions cross role boundaries: a decision becomes an artifact (a spec, an ADR, a ticket, a review) the moment it needs to inform someone else's decision. **Across boundaries, artifacts are the only thing that flows.**

This is what makes the system composable. Stable artifact schemas — form, required fields, provenance, the model or human that produced it — are the interface contracts that let any role consume the output of any other, regardless of how it was produced. Swap the reviewer's model; the spec it produces still slots into the same downstream graph. Same property that makes Unix pipes and microservice APIs work: composition follows interface stability.

And the composition is a **graph, not a pipeline.** Multiple artifacts feed one decision (an architect reads a spec, a constraint doc, three prior ADRs); one decision spawns multiple artifacts (a design produces a mockup, a spec, a list of open questions). Pipelines are the factory's geometry; DAGs are this system's.

## Two graphs: artifacts and decisions

The composition above is the **artifact graph** — what was produced, from what inputs, by which session. It is the lineage a provenance vocabulary like PROV-O captures. For a process run by humans this is the *whole* of the recoverable record, because the decisions themselves lived in people's heads; the reasoning was never written down except where someone chose to write an ADR.

An LLM-run process breaks that limitation, and the break is the point. When a worker fills a role, its decisions are *made in the open* — produced by a recordable session against a recorded bundle. The reasoning is no longer ambient; it is capturable at the moment it happens. A system that records only the artifact graph throws away exactly the half that became newly recordable because a machine made the call. So DDD makes a second graph first-class: the **decision graph.**

The two graphs are different shapes over the same work — one decision can span several artifacts; several decisions can collapse into one artifact — and they **intersect at the session.** The production event is the shared node: a session produces an artifact (its place in the artifact graph) and records the decisions made in it (their place in the decision graph), both anchored to that one event. The session is the seam that stitches the two graphs together.

Decisions stand in two relations, and the distinction is the whole structure:

- **Generation decisions** govern *how an artifact of a given type is produced* — how many test cases to write, what they should focus on, what counts as adequate coverage. Durable, few, attached to the role's execution guidance rather than to any one output. They govern the *quality of the system itself*.
- **Subject-matter decisions** are the *content* — for this feature, the token expires at fifteen minutes because of the threat model; this test targets that boundary because that is where the risk concentrates. Per-artifact, many, and what a downstream role actually consumes. They are the *how and why of the domain*.

A session is precisely where a generation decision is *applied to* a domain to yield subject-matter decisions. "Write four cases focused on boundaries" (generation) meets "this feature's risk surface" (domain context) and produces "test the fifteen-minute expiry edge" (subject-matter). So a subject-matter decision has two kinds of antecedent, walked by two different edges: one rises to the generation decision that *governed its shape* (terminating at role and system-quality authority); the other rises through *prior subject-matter decisions* that supplied its content (terminating at domain origin or a sensing action). The meta-layer and the content-layer are not two points on one chain — they are two axes that cross at the session.

The payoff is a sharper definition of completeness at the process level. A process is **provenance-complete** when every value-anchored artifact can be walked backward through *both* graphs: through the artifact graph to its full chain of upstream artifacts, and through the decision graph to its full chain of upstream decisions — governance and content both — terminating at value-anchoring on one side and at registered generation authority and domain origin on the other. The artifact graph alone is half the provenance, and for an agentic system it is the half that was always recoverable. The decision graph is the half the machine made newly recordable. Recording both is what full compliance means for a system that decides.

## Two disciplines keep the graph honest

**Granularity.** You can trace decisions backwards forever, since every action presupposes a context that was itself decided. The natural stopping points are three: decisions become trivial (routine execution within an established frame), decisions get absorbed into a role's standing authority, or the chain reaches a sensing action where external reality enters. Below the execution line is execution; above it is the graph being modeled.

**Value anchoring.** Every subgraph must terminate in a value action. That keeps the system from sprawling, and it is a useful audit: if you cannot trace a decision back to a value action it eventually serves, either the map is wrong or the decision should not exist.

## Chain termini: ready and done

Value-anchoring says every chain terminates in a value action. True in the long run, but the cadence of real work distinguishes two terminus patterns, borrowed from agile:

**Done.** A chain ends when its value action has fired, its outcome has been interpreted, and post-action audits pass. The world has changed and the system has confirmed it.

**Ready.** A chain pauses when the focal artifact's upstream context graph is complete: design, spec, verification approach, test criteria, acknowledgements, all coherent and audit-passing. No external action has occurred; the system has converged on a fully contextualized artifact suitable for downstream work.

Ready is not a true terminus — value-anchoring still holds, and the chain resumes from ready toward the value action. But ready is the natural plateau where work batches, where human checkpoints most naturally sit, and where downstream feedback can re-open upstream context. Ready is continuously evaluated, not stamped: if implementation reveals the design is wrong, feedback flows upstream and invalidates the ready state, pausing dependent done-chains until the upstream re-converges. The DAG is not strictly forward. These two patterns have different audit profiles and different autonomy implications — see [Convergence State](02-entities.md#convergence-state).

## Context has a form

Written context — briefs, specs, decision logs, code, tickets — is LLMs' native medium and moves into them at near-zero loss. Visual context — sketches, mockups, layouts, the felt sense of a design — used to be a hard wall. Modern frontier multimodal models read images and design files with enough fidelity to participate in visually-driven roles; smaller, cheaper models often don't, or do so poorly.

So **form-of-context becomes a model-selection constraint per role**: a role mediated by text-only artifacts has a wide menu of models; a role mediated by visual artifacts needs a frontier multimodal model, with the cost and latency tradeoffs that implies. Some visual artifacts (component trees, prototype interactions, motion) carry meaning a screenshot still misses, so even capable models may need a translation layer — annotated specs, structured tokens, design rationale. When mapping a process, classify each artifact by its form; the form tells you which model can fill that role and how much engineering the handoff needs.

## Model selection is per-role

Form is one dimension; there are others. Some roles need deep reasoning over ambiguous, multi-source context (architectural calls, prioritization, design critiques); others make narrow, high-frequency judgments (classifying a ticket, sanity-checking output). Some sit on a critical path with strict latency requirements; others run in batch. The role-as-context-bundle framing extends naturally: **the bundle dictates the model.** A digital twin of a real process will typically use a mix — a frontier multimodal model for the design lead, a strong reasoning model for the architect, a fast cheap model for triage, a code-specialized model for the implementer. Picking one model for the whole twin is the equivalent of staffing every role with the same person regardless of skill, seniority, or specialty. Along a single chain the selection typically follows the [funnel](../core/projections.md#the-funnel-allocation-over-position) — bigger models upstream, smaller toward the value action.

Treat model selection as a per-role design decision, not a deployment detail.

## Design method, in six steps

The full method is worked in [method/01](method/01-applying.md); the shape of it:

1. **Identify the value actions.** What does the organization actually produce that creates value.
2. **Trace backwards.** For each value action, what decisions had to happen, in what order. The chain ends at standing authority, at trivial execution, or at a sensing action.
3. **Map the roles and artifacts.** Each decision belongs to a role; each role consumes and produces artifacts. Artifacts are the interface.
4. **Classify artifact form.** Text, visual, structured, mixed — this constrains which models can fill the role.
5. **Choose a model per role** whose capabilities match the context shape and decision profile — along a chain, typically the funnel.
6. **Wire them up.** Feed each role its context, and let the artifacts flow.

## Why this works

- Existing processes already encode hard-won judgments about which context belongs where. The apparatus inherits that for free.
- Artifacts make context transfer concrete and inspectable. If a step fails, you can read what it had to work with — and what it didn't.
- Stable schemas make the system composable: roles swapped, models upgraded, branches added, without rewriting the graph.
- Value anchoring prevents sprawl.
- The [funnel](../core/projections.md#the-funnel-allocation-over-position) turns model bindings into a forcing function on upstream rigor — under-specification surfaces as model-size escalation rather than silent failure.
- It gives an honest failure criterion: when a step underperforms, the first question is "did it have the context a competent human in this role would have?" — not "is the model good enough?" Most of the time the gap is contextual, and that is where the engineering is.

Next: [the entity reference](02-entities.md) makes this vocabulary precise, then [encoding the domain](03-encoding-the-domain.md) covers how context, the bundle, phases, and task types actually package a domain for the graph.
