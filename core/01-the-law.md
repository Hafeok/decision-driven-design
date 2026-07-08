# The Law: Conservation of Specification

> **Core §1 — normative.** The one law the whole framework rests on. Everything else in `core/` is this law measured (Completeness), bounded (the Polanyi Floor), or projected onto an axis (the Funnel and Maturation). Everything in `apparatus/` is this law *run against a real domain*.

Decision-Driven Design has exactly one primitive claim. State it first, because the rest of the framework is machinery for keeping it.

## The unit: a decision

A **decision** is a context-conditioned forecast: a call made from knowledge, in a situation. It is the unit of work. An **actor** is anything that makes decisions — the law quantifies over all of them, and it hard-codes none.

Three instances span the space. A *human* decides by forecasting from knowledge held in the head, gathered over a lifetime, much of it never articulated. A *language model* decides by forecasting from knowledge transmitted in its context — it consumes what it is given. A *classical program* is the degenerate actor: every decision it will ever make was pre-made by its author and frozen into the code; execution replays them. New actor types may appear; the law will quantify over those too, because nothing in it depends on what kind of thing is doing the deciding.

A decision does not have to be encoded to be made. The knowledge required to make it *well* is the same for every actor — what differs per actor is only **where that knowledge can live** and how it gets there. That is the entire subject of the framework: for a given decision, where does the required knowledge live, and what does it cost to move it from one place to another.

## The law

> **Conservation of Specification** — in full, the **Conservation of Specification Demand**. For a given task at a given assurance level, the specification demand is constant — fixed by the task, never by the system. Every system allocates that demand fully across four stores. Nothing is ever removed from the total; it is only moved between stores.

The full name marks the conserved quantity precisely: it is the *demand* that is conserved, not any specification artifact. The law is a pair — an invariance premise (the demand is fixed by the task and assurance level, never by the system) and a conservation consequence (allocation moves between stores; the total never shrinks). The consequence is the load-bearing half, so the conservation word keeps the short name. Two things the law does *not* say: the constant is **known** (it is discovered, by encode-exercise cycles — the gap between fixed and known is the [Polanyi Floor](03-the-polanyi-floor.md)), and the constant is **freezable** (whether it can be encoded ahead of fire time is an environment property — next section).

The four stores are the four places the knowledge required for a decision can live:

- **Encoded** — explicit, transmitted in the action's input, in a form the executing actor can consume: a checklist or procedure for a human, a program for a machine, a schema-prompt-context bundle for a model. Paid once, amortized over every run.
- **Mechanical verification** — the same specification applied at the *end* instead of the beginning: an encoded acceptance predicate that checks the output rather than shaping the input, evaluable without any actor's discretion.
- **Judgment** — made per run by a **designated, accountable actor** from knowledge that is not encoded. Paid every run, as attention. Today the only actor type that can carry accountable unencoded specification is a human; whether any other actor type can qualify is an actor-relative question — the same relativity that governs the [floor](03-the-polanyi-floor.md#the-floor-is-actor--and-environment-relative).
- **Escaped** — unallocated. Decided by no designated actor: it falls to a prior, a default, chance, or physics — and is therefore transferred to the user as defect exposure.

![The conservation of specification: for a given task the total is constant — encoded specification before the executing actor, mechanical verification after it, judgment paid per run, and what no store covers escapes as defect exposure. Allocation profiles for exploration, under-engineered systems, and complete(spec, binding) at full autonomy.](assets/conservation-of-specification.svg)

The consequence that makes the law useful: **you cannot reduce the total, only relocate it.** "We saved on specification *and* on review" does not parse. It reads as "we shipped the difference" — the demand that left the encoded and judgment stores did not vanish; it moved to *escaped*, and escaped is defect exposure the user pays for.

This turns a vague quality conversation into an allocation audit. For any piece of work the four stores are the *terms of the agreement*: this much is encoded, this much is mechanically verified, this much is a designated actor's judgment, and nothing escapes unpriced. A system is trustworthy not because its executing actor is capable but because its allocation is fully accounted for and inspectable.

## The demand is denominated in decisions

The law states the demand is constant. This section states what the constant *is made of*: **the specification demand for an action is the set of decisions that govern it.** The constant is not an amount of text; it is a decision set, fixed by the task and the assurance level. What varies by system is where each decision gets made.

This gives the law its decision-side reading, equivalent to the specification-side statement above: **every governing decision gets made — the only choice is by whom, when, and at what price.** To specify is to pre-make decisions; a specification is decisions in encoded, transmissible form. The two vocabularies are the same claim at two moments, which is why the framework is named for the unit (decisions) and the law for the demand (specification): Decision-Driven Design rests on the Conservation of Specification Demand precisely because that demand is denominated in decisions.

Take a physical action to see the grain of it. Firing a rifle is one action, governed by many decisions: kneel or lie prone; how firmly the stock sits against the shoulder; how far the eye sits from the scope; when in the breathing cycle to squeeze. Each is a decision whether it is made deliberately, made tacitly by a trained body, or made by nobody at all. The action's specification — *how to do it to the declared standard* — decomposes exhaustively into these governing decisions.

Three terms, in temporal order, and they must not be conflated:

- **Facts** are what the action operates *on and in* — the target's distance, the wind reading, the repo's state. Facts are not demand items; they are the substrate, **inspected in order to act**. Inspecting them is the sensing side of the system.
- **Decisions** are the demand — the constraints applied *before* the act that steer it toward the perfect outcome. Each decision consumes facts as input and contributes constraint as output.
- **Verification** comes *after* the act — the encoded criterion the outcome is checked against.

Inspect facts, decide, act, verify. The four stores are then four answers to the question *who made this decision*:

- **Encoded** — decided once, upstream, frozen; execution replays a pre-made decision.
- **Mechanical verification** — the decision is delegated to the executor, but its *outcome* is gated by an encoded criterion after the act.
- **Judgment** — decided per-run, in a human head, unencoded.
- **Escaped** — decided by *nobody*: it falls to a prior, a default, chance, or physics. Defect exposure is precisely the set of unowned decisions.

Denominating the demand in decisions also derives two things the law otherwise had to stipulate:

**Assurance level is the granularity bound.** A decision belongs to the governing set if and only if varying it moves the outcome beyond the declared assurance tolerance. At barn-door assurance, eye relief is not in the set; at marksman assurance it is. This is *why* the law is parameterized on assurance: raising the assurance level admits more decisions into the demand. It also dissolves the infinite-regress objection — muscle-fiber recruitment is not a governing decision at any assurance level a shooter declares, because varying it within the body's trained envelope does not move the outcome past tolerance.

**The [Polanyi Floor](03-the-polanyi-floor.md) is denominated in the same unit.** The floor is the subset of the governing decision set that provably governs — vary it and the outcome moves — yet resists articulation. The marksman's eye relief is a decision made below consciousness: real, operative, trained into the body, encodable only down to some fidelity and no further. The floor is not missing knowledge; it is owned-but-unarticulable decisions.

This is also the theorem behind the framework's name. Specification decomposes into decisions; therefore driving a system by its specification *is* driving it by its decisions — decision-driven design, as derivation rather than slogan.

## The environment clause: when the demand is finitely encodable

The law says the demand is constant. It does not say the demand is *finite*. Whether the specification for a decision can be **finitely encoded** is a property of the environment, not of the decision.

- **Closed environment** — stable for the duration of the action. The action and its context can be described to their full extent; perfection has finite specification demand. Encode it all and the demand is met.
- **Open environment** — the environment can change while the action is in flight. The demand **diverges** only in the limit, as required assurance approaches 1: no finite knowledge fully specifies the outcome, because the change after commitment is irreducible. Firing a gun in wind is this case — the gust after the bullet leaves the barrel cannot be pre-encoded. At any *declared* assurance below the limit, the demand is finite and constant again — evaluated at fire time — and the law holds unchanged. What wind destroys is not the constancy of the demand but its **pre-encodability**: the flow variables cannot be frozen at authoring time, so their share of the demand must be either sensed at fire time, carried in judgment, or priced as escape. Open environments are the law's limit case, not its counterexample.

Software is not found closed — it is **closable**. "Writing code" is fully describable only against a frozen boundary: pinned toolchain, frozen repo state, content-addressed context, pinned model binding. Remove the pins and software is windy — a silent model upgrade, a drifting external API, another writer mutating shared state are all gusts. Computation is the one domain where closure can be *manufactured*, and most of the framework's machinery is exactly that manufacture: content-addressing, binding pinning, hermetic bundles, frozen discovery records are wind-removal equipment. The discipline does not assume a stable environment; it builds one. This is the environment half of why the judgment-share-zero endpoint is reachable in software and nowhere physical; the floor half is the [zero-floor postulate](03-the-polanyi-floor.md#the-zero-floor-postulate-for-digital-actions).

Open environments do not break the law; they split the context by **binding time**. What cannot be encoded is the *value*; what can be encoded is the *policy* plus the *sensing obligation*. In decision terms: the governing decision stays in the demand, but the **facts** it consumes can only be inspected at fire time — the wind-correction decision is encodable as policy; the wind reading is not. Frozen context binds when the spec is authored; sensed context binds when the action fires. A domain's exposure to wind is measured by how much of its context is necessarily sensed rather than frozen.

**The last wind.** In a fully pinned system every component is deterministic by construction except one: the executing actor. Actors differ not in *whether* they can be pinned but in the **resolution** of their tightest available pinning — a spectrum:

- **Pinnable by value** — the classical program: its behavior *is* its description; pinning the code pins the actor entirely.
- **Pinnable by binding** — the model: it cannot be pinned by value, but the same weights under the same binding yield the same distribution — for every instance, until the binding changes. The language model is historically significant here as the first non-deterministic actor whose *distribution* can be frozen.
- **Pinnable by classification** — the human: the binding is a certified capability envelope — rank, seniority title, type rating, board certification, qualification level. Humanity has run this binding regime for centuries: qualification testing *is* the sampled exercise performed on a human actor — N trials against a declared acceptance predicate — and the classification is the cached verdict. The resolution is coarser in three specific ways: the verdict pins an **envelope**, not a distribution; it holds for **one individual**, not every instance; and it **expires** — the actor drifts within their own binding, which is exactly what recertification cadences and currency requirements exist to re-measure. And unlike any machine binding, the human binding vocabulary is **normatively constrained**: law excludes certain predictive attributes from capability matching outright. Human bindings are governed institutions, not mere measurements.

The last wind is the executing actor's residual variance under its tightest available pinning. This is why the highest tier of the Completeness Exercise is *sampled*: the sampling burden exists because, and only because, the actor still has weather in it — and qualification regimes show the sampling tier is older than the framework, generalizing over actors just as the law does. It is also why residual variance is attributable at all: with everything else frozen, whatever varies is the actor's. The case for a bound model as executor, where the demand permits, is therefore not that human wind is unmeasurable — qualification measures it — but that the model's verdict is **higher-resolution, instance-general, and stable until the binding changes**, where the human's is envelope-coarse, individual, and decaying.

**The Rice boundary.** For computation, *describability* is total — the program is its own complete description. *Universal mechanical verifiability* is not: Rice's theorem bars any general decision procedure for non-trivial semantic properties of programs. This is not a hole in the law; it is why the mechanical-verification store is scoped as **declared, per-task acceptance predicates**, each individually decidable — never a proof of everything. Verification is chosen property by property; the properties not chosen sit in judgment or escape, on the ledger like everything else.

Sequencing consequence: build first where the environment is maximally closable — software — because it is the one place the law's endpoint is reachable; extend outward in order of wind.

## The two boundaries, the two principles

A system has two boundaries with the world: knowledge comes *in*, effects go *out*. The law has one design principle guarding each. Both are corollaries of the law — they are how it is enforced rather than merely stated.

### Principle 1 — No tacit dependencies *(the input boundary)*

> Every piece of knowledge the system's behavior depends on is either **encoded** — explicit, machine-readable, transmitted in the input — or **declared** as a judgment point with a named owner. Nothing the system depends on may live only in someone's head.

The executing actor works from what it holds plus what is transmitted; whatever the task requires beyond that is either declared as a designated actor's judgment or simply absent. For an actor that holds nothing of its own — a model consuming its context, a new hire on day one — the input *is* the knowledge. Knowledge that is neither encoded nor declared does not disappear — it silently converts into per-run judgment, paid in review attention at every execution and discovered only when review misses.

This is not an obligation to *eliminate* tacit knowledge. The [Polanyi Floor](03-the-polanyi-floor.md) is real: some knowledge cannot be made explicit, and a principle that denies this just invites hiding the floor to claim conformance. The obligation is to **map** the floor. A declared "annotation needed" list is conformant; an unstated house convention is not. Explicit residue is a declared judgment point; silent residue is a defect.

### Principle 2 — Completeness gates action *(the output boundary)*

> An actor may commit an effect only through a specification that is **complete for its pinned binding** — complete(spec, binding), verified by the [exercise](02-completeness.md) at the tier the autonomy level demands — with **declared verification** of the output. Where human judgment substitutes for either, the substitution is declared and bounded by autonomy level. At full autonomy the judgment share is zero: encoded specification and mechanical verification cover the effect entirely.

The gate sits at the *effector*, not at generation. Generation is cheap and reversible; effects are neither. This is what makes exploration legitimate rather than exempt: exploratory work carries no completeness obligation *because it commits no effects* — all spec, all verification, all judgment collapse into the human reading the output. The obligation attaches the moment an effector does.

Completeness is a *relation*, never an absolute. An unparameterized "the spec is complete" is a claim about no consumer and is void.

### The pair

Principle 1 makes the measurement *possible* — a system with undeclared tacit dependencies cannot be walked, so its allocation cannot even be read. Principle 2 makes the measurement *consequential* — an allocation that gates nothing is a report. Between them they hold the law's ledger honest at both boundaries.

## What the rest of core does

The remaining core documents are this one law, viewed three ways:

- [**Completeness**](02-completeness.md) is the law's **measurement instrument**. It reads the allocation: everything not encoded, priced. `complete(spec, binding)` is the empty-residual condition.
- [**The Polanyi Floor**](03-the-polanyi-floor.md) is the law's **lower bound**. It is the boundary below which knowledge cannot move from judgment to encoded at any effort — the asymptote of what any agreement can promise, and the per-task autonomy ceiling.
- [**The two projections**](04-projections.md) are the law along its two axes. The **funnel** is allocation over *position* in a chain; **maturation** is allocation over *recurrence* in time. One law, two pictures.

Then [`apparatus/`](../apparatus/) runs the law against a real domain: what roles, artifacts, sessions, bundles, and orchestration it takes to actually move a domain's decisions from judgment into specification and keep the ledger inspectable while doing it.
