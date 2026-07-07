# Decision-Driven Design

> **§1. Introduction and motivation** — *informative.* The premise the rest of the specification rests on: LLMs as forecasters, work as a chain of context-conditioned decisions, value actions as the terminus, the two graphs that meet at the session.
>
> Borrowed terms (DAG, DMN, RDF, MCP, OCI, …) — see [Appendix C: Glossary](glossary.md).

A framework for building systems with LLMs.

## Premise: LLMs as forecasters

An LLM is a knowledge forecaster: given a context, it predicts what comes next. Humans work the same way. We reach decisions by forecasting from the knowledge we hold and the context we're operating in.

## Implication for work

A human work process is a chain of context-conditioned decisions. Roles (UXer, designer, PM, developer) are labels for context bundles plus authority to act on them. The decision is a forecast over the bundle.

## What organizations actually do

Organizations exist to perform value actions — the things that create value: shipping a product, closing a deal, treating a patient, publishing a paper. Every value action is preceded by a chain of decisions that determines whether, when, and how it happens. So the work to model is not the org chart and not the process flow, but the decision graph upstream of each value action. Map value-backwards: start from what the organization actually produces, and trace back through the decisions that had to occur for it to happen.

## The other boundary: sensing

Value actions are where the system acts on the world. The dual boundary is where the system reads from the world — sensing actions. Monitoring a deployed feature. Pulling production logs. Querying an API for current state. Interviewing a user. Polling a market signal. Reading a sensor.

Sensing actions execute against external reality the same way value actions do, their outcomes are equally uncertain, and they need the same kind of interpretation to be useful. Their job is to bring information *in* rather than push value *out*. The geometry of a real process has two world boundaries: sensing on the input side, value actions on the output side, decisions in between.

Value-anchoring still holds — every subgraph terminates in a value action, and sensing actions aren't terminal in the value-delivery sense. They're upstream nodes whose artifacts feed forward through decision chains that eventually land at value. The dual is also worth stating: every subgraph originates in sensing — a continuous sense (monitoring), a triggered sense (a probe authorized by an upstream decision), or an initial request (which is itself sensing an upstream party: customer, PM, calling process). Map value-backwards to find the chain; map sensing-forwards to find the chain's origin.

## The shift this enables

Most of the hard problems in knowledge work aren't automation problems — they're decision problems. Automation works when you already know what to build and just need to execute reliably. But the work of figuring out *what* to build, what's good, what's worth doing, who needs to weigh in — that's decisions, all the way down. Treating LLMs as forecasters lets us tackle that layer directly.

This is also why LLMs feel categorically different from prior automation. Industrial automation was good at the value action itself — the assembly, the transaction, the routing — and the upstream decisions were a human bottleneck the factory couldn't touch. In knowledge work the action and the decision often collapse into the same step ("send this email" is both), and the chain of decisions upstream is most of the work. Factory automation can't help with that because it can't decide. LLMs can.

## Contrast with the factory metaphor

The dominant AI-factory framing reaches for assembly lines and workstations: discrete tasks, deterministic flow, machines that execute. That metaphor fits when the answer is known and the goal is throughput. It fits poorly when the goal is to *decide*, because decisions are shaped by which context arrives and in what form — not by repeatable mechanical steps. The factory isn't wrong; it's just answering a different question.

## The alternative: a digital twin of the process

Map the real process — the roles, the decisions each role makes, and the artifacts that flow between them (briefs, specs, designs, reviews, tickets, decision records). Artifacts are not incidental; they are the medium by which context transfers between roles. Once the process and its artifacts are mapped, we have a digital twin: a structure we can simulate, with LLMs filling roles and producing the same artifacts a competent human would.

## The unit of work and the unit of composition

The unit of work is the decision. The unit of composition is the artifact. Decisions are private to a role — they're what the role does, internally, by forecasting over its context. Artifacts are how decisions cross role boundaries: a decision becomes an artifact (a spec, an ADR, a ticket, a review) the moment it needs to inform someone else's decision. Across boundaries, artifacts are the only thing that flows.

This makes the system composable. Stable artifact schemas — form, required fields, provenance, the model or human that produced it — are the interface contracts that let any role consume the output of any other, regardless of how that output was produced. Swap the reviewer's model; the spec it produces still slots into the same downstream graph. This is the same property that makes Unix pipes and microservice APIs work: composition follows interface stability.

The composition is a graph, not a pipeline. Multiple artifacts feed a single decision (an architect reads a spec, a constraint doc, and three prior ADRs); one decision spawns multiple artifacts (a design produces a mockup, a spec, and a list of open questions). Pipelines are the factory's geometry. DAGs are this system's.

## Two graphs: artifacts and decisions

The composition above is the **artifact graph** — what was produced, from what inputs, by which session. It is the lineage a provenance vocabulary like PROV-O captures: artifact *generated by* activity, activity *used* bundle, activity *associated with* role and model. For a process run by humans this is the whole of the recoverable record, because the decisions themselves lived in people's heads and the artifacts were the only durable trace. The reasoning was never written down except where someone chose to write an ADR.

An LLM-run process breaks that limitation, and the break is the point of this framework. When a worker fills a role, its decisions are *made in the open* — produced by a recordable session against a recorded bundle. The reasoning is no longer ambient; it is capturable at the moment it happens. A system that records only the artifact graph throws away exactly the part that became newly recordable because a machine made the call. So DDD makes a second graph first-class: the **decision graph**.

The two graphs are different shapes over the same work. One decision can span several artifacts; several decisions can collapse into one artifact. The artifact graph answers *what flowed and from where*; the decision graph answers *what was decided and why*, and lets you walk up the reasoning independent of which artifacts happened to carry it. They are orthogonal, and they **intersect at the session** — the production event is the shared node. A session produces an artifact (its place in the artifact graph) and records the decisions made in it (their place in the decision graph), and both are anchored to that one event. The session is the seam that stitches the two graphs together.

Decisions stand in two relations, and the distinction is the whole structure:

- **Generation decisions** govern *how an artifact of a given type is produced* — how many test cases to write, what they should focus on, what counts as adequate coverage. They are durable, low in number, and attach to the role's execution guidance rather than to any one output. They are the layer that governs the *quality of the system itself*.
- **Subject-matter decisions** are the *content* — for this feature, the token expires at fifteen minutes because of the threat model; this test targets that boundary because that is where the risk concentrates. They are per-artifact, many, and are what a downstream role actually consumes. They are the *how and why of the domain* being worked in.

A session is precisely where a generation decision is *applied to* a domain to yield subject-matter decisions. "Write four cases focused on boundaries" (generation) meets "this feature's risk surface" (domain context) and produces "test the fifteen-minute expiry edge" (subject-matter). So a concrete subject-matter decision has two kinds of antecedent, walked by two different edges: one rises to the generation decision that *governed its shape*, terminating at role and system-quality authority; the other rises through *prior subject-matter decisions* that supplied its content, terminating at domain origin or a sensing action. The meta-layer and the content-layer are not two points on one chain — they are two axes that cross at the session.

This is not a second provenance vocabulary bolted onto the first. Decisions interoperate with PROV-O at the session seam — they share its activity node — but neither edge reduces to it. The content edge often parallels artifact derivation but not always, because the two graphs have different shapes. The governance edge has no PROV-O analogue at all: "this choice was governed by that policy" is motivational provenance one level below anything the artifact graph expresses. A decision *can* be expressed as a provenance entity, but the governance edge, the two-axis structure, and decision kind all have to be added as extensions regardless — so the honest design states decisions as first-class and lets them meet PROV-O at the session, rather than pretending they are a dialect of it.

The payoff is a sharper definition of completeness. A process is **provenance-complete** when every value-anchored artifact can be walked backward through *both* graphs: through the artifact graph to its full chain of upstream artifacts, and through the decision graph to its full chain of upstream decisions — governance and content both — terminating at value anchoring on one side and at registered generation authority and domain origin on the other. The artifact graph alone is half the provenance, and for an agentic system it is the half that was always recoverable. The decision graph is the half the machine made newly recordable. Recording both is what full compliance means for a system that decides; this is the backbone the rest of the framework builds provenance on.

Two disciplines keep the graph honest:

**Granularity.** You can trace decisions backwards forever, since every action presupposes a context that was itself decided. The natural stopping points are three: decisions become trivial (routine execution within an established frame), decisions get absorbed into a single role's standing authority, or the chain reaches a sensing action where external reality enters the graph. Below the execution line is execution; above it is the graph you're modeling.

**Value anchoring.** Every subgraph must terminate in a value action. That's what keeps the system from sprawling, and it's a useful audit: if you can't trace a decision back to a value action it eventually serves, either the map is wrong or the decision shouldn't exist.

## Chain termini: ready and done

Value anchoring says every chain terminates in a value action. True in the long run, but the cadence of actual work distinguishes two terminus patterns, borrowed from agile's vocabulary:

**Done.** A chain ends when its value action has fired, its outcome has been interpreted, and post-action audits pass. The world has changed and the system has confirmed it.

**Ready.** A chain ends — or, more precisely, pauses — when the focal artifact's upstream context graph is complete: design, spec, verification approach, test criteria, acknowledgements, all coherent and audit-passing. No external action has occurred; the system has converged on a fully contextualized artifact suitable for downstream work.

Ready isn't a true terminus. Value-anchoring still holds; the chain resumes from ready toward the value action. But ready is the natural plateau where work batches, where human checkpoints most naturally sit, and where downstream feedback can re-open upstream context. Ready is continuously evaluated, not stamped: if implementation reveals the design is wrong, feedback flows upstream and invalidates the ready state, pausing dependent done-chains until the upstream re-converges. The DAG isn't strictly forward.

The two patterns have different audit profiles, different fitness signals, and different per-role autonomy implications. Naming them earns its keep because it's where a lot of the operational architecture hinges.

## Context has a form

Written context — briefs, specs, decision logs, code, tickets — is LLMs' native medium and moves into them at near-zero loss. Visual context — sketches, mockups, layouts, the felt sense of a design — used to be a hard wall. Modern frontier multimodal models (Claude Opus 4.7 and peers) read images and design files with enough fidelity to participate in visually-driven roles. Smaller, cheaper models often don't, or do so poorly.

So form-of-context becomes a model-selection constraint per role: a role mediated by text-only artifacts has a wide menu of models; a role mediated by visual artifacts needs a frontier multimodal model, with the cost and latency tradeoffs that implies. Some visual artifacts (Figma component trees, prototype interactions, motion) carry meaning that a screenshot still misses, so even capable models may need a translation layer — annotated specs, structured tokens, design rationale.

When mapping the process, classify each artifact by its form. The form tells you which model can fill that role and how much engineering the handoff needs.

## Model selection is per-role

Form of context is one dimension; there are others. Some roles need deep reasoning over ambiguous, multi-source context (architectural calls, prioritization, design critiques); others make narrow, high-frequency judgments (classifying a ticket, drafting a routine reply, sanity-checking output). Some need vision, others don't. Some sit on a critical path with strict latency requirements; others run in batch and can spend more compute. Some are cost-sensitive at scale; others are rare and high-stakes.

The role-as-context-bundle framing extends naturally: the bundle dictates the model. A digital twin of a real process will typically use a mix — a frontier multimodal model for the design lead, a strong reasoning model for the architect, a fast cheap model for the triage step, perhaps a code-specialized model for the developer. Picking one model for the whole twin is the equivalent of staffing every role with the same person regardless of skill, seniority, or specialty. It works, but it leaves capability on the table and burns cost where it doesn't need to.

Treat model selection as a per-role design decision, not a deployment detail.

## The conservation of specification

> **The conservation of specification.** For a given task at a given assurance level, the specification demand is constant — fixed by the task, never by the system. Every system allocates that demand fully across four stores: **encoded** upstream (schema, prompt, context, binding — paid once, amortized over runs), **mechanical verification** (acceptance predicates — specification applied at the end instead of the beginning), **judgment** (a human head — the spec exists, unencoded, paid per run), and **escaped** (unallocated — transferred to the user as defect exposure). Nothing is ever removed from the total; it is only moved between stores. "We saved on spec and on review" parses as "we shipped the difference."

![The conservation of specification: for a given task the total is constant — encoded specification before the model, mechanical verification after it, judgment paid per run, and what no store covers escapes as defect exposure. Allocation profiles for Explorer mode, under-engineered systems, and complete(spec, binding) at Level 4+](assets/conservation-of-specification.svg)

The exercise residual ([Completeness Exercise](completeness-exercise.md)) measures the allocation: everything not encoded, priced. Maturation moves mass from judgment to encoded, because amortization wins the moment n > 1. Autonomy levels constrain the allocation: Level 4+ forces the judgment share to zero, leaving only encoded and mechanical. Circular verification — model-generated tests grading model-generated output — is allocation forgery: mass claimed in mechanical verification that was never in the system.

### The environment clause: when the demand is finitely encodable

For any given action, the knowledge required to perform it perfectly is a constant. Whether that constant can be **finitely encoded** is a property of the environment, not of the action:

- **Closed environment** — stable and non-changing for the duration of the action. The action and its context can be described to their full extent; perfection has finite specification demand. Encode it all, and the demand is met.
- **Open environment** — the environment can change while the action is in flight. The demand **diverges** as required assurance approaches 1: no finite knowledge fully specifies the shot, because the gust after the bullet leaves the barrel is irreducible. Firing a gun in wind is this case. Here an assurance level must be declared, and the residual demand carried in judgment or accepted as escape.

Software is not found closed — it is **closable**. "Writing code" is fully describable only against a frozen boundary: pinned toolchain, frozen repo state, content-addressed context, pinned model binding. Remove the pins and software is windy — a silent model upgrade, a drifting external API, another writer mutating shared state are gusts. Computation is the one domain where closure can be **manufactured**, and the framework's machinery is exactly that manufacture: content-addressing, binding pinning (`ai-development-foundations` RFC 0002), hermetic bundles, frozen discovery records are wind-removal equipment. The discipline does not assume a stable environment; it builds one. This is why the judgment-share-zero endpoint is reachable in software and nowhere physical.

Open environments do not break the law; they split the **Context axis by binding time**. What cannot be encoded is the value; what can be encoded is the policy plus the sensing obligation: the control law is specification, the wind reading is context that binds at fire-time instead of spec-time. **Frozen context** binds when the spec is authored; **sensed context** binds when the action fires. A domain's wind is measured by how much of its context is necessarily sensed — which orders the flow domains by exposure and explains why a flow over live external state carries conditional judgment where code authoring over a frozen repo carries none.

**The last wind.** In a fully pinned software system every component is deterministic by construction except one: the model. It cannot be pinned by value, only by binding — the single stochastic element left inside the closed box. This is why Tier 3 of the Completeness Exercise is *sampled*: the sampling burden exists because, and only because, one component still has weather in it. It is also why residual variance is attributable at all — with everything else frozen, whatever varies is the model's.

**The Rice boundary.** For computation, *describability* is total — the program is its own complete description. *Universal mechanical verifiability* is not: Rice's theorem bars any general decision procedure for non-trivial semantic properties of programs. This is not a hole in the law; it is why the mechanical store is scoped as it is — **declared, per-task acceptance predicates**, each individually decidable, never a proof of everything. Verification is chosen property by property; the properties not chosen sit in judgment or escape, on the ledger like everything else.

Consequence for sequencing: build first where the environment is maximally closable — software — because it is the one place the law's endpoint is reachable; extend outward in order of wind.

### Two projections, one law

The two structures the rest of this document builds on are the same law viewed along different axes:

- **The funnel is the law projected along the chain.** Constraint density rising toward the value action *is* the encoded store growing with position: each step downstream, more of the demand has already been allocated upstream, so the judgment and capability required of the next consumer falls. When an implementer role requires a large model, the allocation at that position is wrong — mass sitting in judgment that belongs in encoded.
- **Maturation is the law projected along recurrence.** The maturation curve *is* mass moving from the judgment store to the encoded store as a task type recurs and amortization pays for conversion. Its asymptote is the [Polanyi floor](the-polanyi-floor.md): the curve converges to (1 − floor), never to 1.

One law, two axes: allocation over *position* is the funnel; allocation over *time* is maturation. The [Completeness Exercise](completeness-exercise.md) is the law's measurement instrument, and the design principles below are its boundary enforcement.

## The funnel: model capability tracks constraint density

Model selection per-role isn't independent across roles in a chain. There's a structural pattern that emerges when the chain is well-designed: constraint density rises monotonically from the input boundary to the value action, and the model capability needed falls correspondingly. Discovery roles work in open problem space and need frontier reasoning. Architecture and design narrow the space through synthesis. Specifications pin remaining problem-domain decisions. Implementation translates a well-specified problem into code in a known idiom. Deployment, at the limit, is `terraform apply`. The value action itself is deterministic code.

> This is the [conservation of specification](#the-conservation-of-specification) projected along the chain: allocation as a function of position.

![The funnel principle: constraint density rises and model capability falls from the sensing/request boundary to the value action terminus](assets/funnel.svg)

The principle is sharper than "smaller models can do simpler things." The claim is that upstream decisions reduce the cognitive load downstream, and a well-designed chain pushes hard calls upstream so the terminus needs only execution. If implementation requires a frontier model, the question isn't whether the model is good enough — it's whether the spec pinned the calls that should have been pinned. The funnel is a design discipline before it's a model-selection heuristic.

This turns model bindings into a forcing function on chain rigor. Bind the implementer role to a small code-specialized model. If it fails, the first move is upstream — tighten the spec, enrich the bundle — not reach for a bigger model. The binding makes under-specification visible. And the framework already measures the relevant signals: `gap` and `contradiction` feedback flag spec incompleteness; idiomatic drift and amendment churn flag bundle incompleteness; action-interpretation disagreement quantifies the gap.

Two wrinkles and one composition rule are worth declaring rather than ignoring.

**Generative actions late in the chain.** Implementation produces a complex artifact even from a perfect spec — naming, structure, integration with existing code. Some baseline implementer judgment doesn't go away because it's about the implementation domain, not the problem domain. The spec encodes decisions over the problem; the bundle (including codebase context) supports decisions over implementation. The asymptote isn't "spec encodes everything" — that's a 4GL, and it has been tried. It's "spec encodes every problem-domain decision, leaving only implementation-domain decisions to the implementer."

**Interpretation sessions can spike.** A value-action interpretation ("did deploy succeed") is small-model trivial. An interpretation of user research or an ambiguous architectural call can need more reasoning than the action it pairs with. These are bumps in the funnel, not violations of it — they're declared, not mysterious.

**Feedback re-enters the funnel rather than reversing it.** An operational finding doesn't traverse the funnel backwards on its way upstream — it lands at an upstream role's input and triggers a fresh forward chain. The receiving role uses its normal binding. Feedback isn't counter-funnel; the funnel just composes with itself.

The design target is the bottom of the funnel: the value action should be deterministic code. Anywhere the value action still requires LLM judgment, an upstream decision was deferred into execution. The funnel discipline pushes that judgment back where it belongs.

## The funnel over time: maturation

The funnel describes one chain at one moment — constraint rising and model capability falling along its length. The same descent happens to a *system* over time, and it is worth naming separately because it is where the framework's cost curve comes from.

> This is the same law projected along recurrence: allocation as a function of time. Its asymptote is the [Polanyi floor](the-polanyi-floor.md).

Complex artifact generation decomposes: a unit of delivered work (a feature, a campaign, a case) is rarely one artifact but a composition of recurring *sub-units of work* — call them tasks — each of which is itself a cluster of typed artifacts. Early in a system's life, none of these tasks are recognized. Each one is open problem space, so each needs a broad, high-capability worker (or a human) to work it out from scratch. As the same tasks recur, they get *typed* — their decomposition, ordering, and quality criteria get made once and frozen into a reusable type (see Task and TaskType in the entity reference). The next instance of a typed task inherits all that prior constraint for free and slides down to a small, cheap model.

So constraint accumulates not only along a chain (the funnel) but across time, **as catalog structure**. The hard calls migrate out of the model's live reasoning and into versioned types that any model can execute against. The funnel is the spatial view of one chain constraining itself toward its terminus; maturation is the temporal view of a whole system constraining itself toward a stable architecture, where most incoming work decomposes entirely into already-known types and only the genuinely novel remainder needs a broad worker.

This gives a measurable definition of architectural maturity: the fraction of incoming work that decomposes into entirely known types. It rises as the type catalogs fill and falls when the system enters a new domain — an operational signal, not a vibe (see Implementation, fitness functions). The broad worker never disappears; it becomes the explorer that handles the novel remainder and, in doing so, mints the new types that let the next instance descend. Cost and opacity are front-loaded into exploration and amortized into reusable structure.

The maturation curve is the funnel's companion picture:

![Maturation: the broad-worker stream narrows over time as recurring work is typed and descends into a widening fan of cheap, decomposed known-task clusters](assets/maturation.svg)

## Design principles

Both principles are corollaries of [the law](#the-conservation-of-specification), enforcing it at the system's two boundaries — knowledge in, effects out. One per pillar.

### Principle 1 — No tacit dependencies *(specification pillar: the input boundary)*

> Every piece of knowledge the system's behavior depends on is either **encoded** — explicit, machine-readable, transmitted in the bundle — or **declared** as a judgment point with a named owner. Nothing the system depends on may live only in someone's head.

The model consumes what is transmitted; it has no access to what is assumed. Knowledge that is neither encoded nor declared does not disappear — it silently converts into per-run judgment verification, paid in review attention at every execution, discovered only when review misses.

This is not an obligation to eliminate tacit knowledge. The [Polanyi floor](the-polanyi-floor.md) is real: some knowledge cannot be made explicit, and a principle that denies this invites hiding the floor to claim conformance. The obligation is to **map** the floor — the `annotation-needed` list is conformant; the unstated house convention is not. Explicit residue is a declared judgment point; silent residue is a defect.

**Exercisable:** Tier 1 walks the encoded portion — every referent resolves or appears on the declared judgment list. Tier 3 detects violations empirically as cross-sample variance: N runs producing N internally consistent, mutually incompatible convention sets is the signature of an undeclared tacit dependency.

### Principle 2 — Completeness gates action *(execution pillar: the output boundary)*

> An LLM may commit an effect only through a specification that is **complete for its pinned binding** — complete(spec, binding), verified by the exercise at the tier the autonomy level demands — with **declared verification** of the output. Where human judgment substitutes for either, the substitution is declared and bounded by autonomy level. At full autonomy the judgment share is zero: encoded specification and mechanical verification cover the effect entirely.

The gate sits at the effector, not at generation. Generation is cheap and reversible; effects are neither. This is what makes exploration legitimate rather than exempt: Explorer mode carries no completeness obligation *because* it commits no effects — all spec, all verification, all judgment collapse into the human reading the output. The obligation attaches the moment an effector does.

Completeness is a relation, never an absolute. An unparameterized "the spec is complete" is a claim about no consumer and is void. And completeness of the spec does not verify the spec itself: validation — was the intent right, not merely met — remains outside this principle's scope. The principle governs whether under-specification can reach an effector, not total assurance.

**Exercisable:** dispatch refuses a bundle lacking a completeness verdict at the required tier; every effect traces to a verdict with a declared consequence. Tier discipline follows autonomy: Tier 2 gates the seam for supervised operation; Tier 3 certifies before Level 4+, where no human inspects each output.

### The pair

Principle 1 makes the exercise possible — a graph containing undeclared tacit dependencies cannot be walked, so completeness cannot even be measured. Principle 2 makes the exercise consequential — a measurement that gates nothing is a report. Maturation is motion under both: the catalog is accumulated converted judgment, tacit knowledge migrating into encoded specification as task types recur, driving the judgment share toward zero on exactly the paths that run most.

## Design method

1. **Identify the value actions.** What does the organization actually produce that creates value.
2. **Trace backwards.** For each value action, what decisions had to happen for it to occur, and in what order. The chain ends at standing authority, at trivial execution, or at a sensing action — the input boundary where external reality enters the graph.
3. **Map the roles and artifacts.** Each decision belongs to a role; each role consumes and produces artifacts. Artifacts are the interface.
4. **Classify artifact form.** Text, visual, structured, mixed — this constrains which models can fill the role.
5. **Choose a model per role** whose capabilities match the context shape and decision profile. Along a single chain, this typically follows the funnel — bigger models upstream, smaller toward the value action.
6. **Wire them up.** Feed each role its context, and let the artifacts flow.

## Why this works

- Existing processes already encode hard-won judgments about which context belongs where. We inherit that for free.
- Artifacts make context transfer concrete and inspectable. If a step fails, you can read what it had to work with — and what it didn't.
- Stable artifact schemas make the system composable. Roles can be swapped, models upgraded, branches added, without rewriting the graph.
- Value anchoring prevents sprawl. Every chain has to pay out in something the organization actually values.
- The funnel turns model bindings into a forcing function on upstream rigor — under-specification surfaces as model-size escalation rather than as silent failures.
- It gives an honest failure criterion. When an LLM step underperforms, the first question is "did it have the context a competent human in this role would have?" — not "is the model good enough?" Most of the time, the gap is contextual, and that's where the engineering is.
- It's honest about the problem. We're not building a faster assembly line. We're building a system that can decide.
