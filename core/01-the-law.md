# The Law: Conservation of Specification

> **Core §1 — normative.** The one law the whole framework rests on. Everything else in `core/` is this law measured (Completeness), bounded (the Polanyi Floor), or projected onto an axis (the Funnel and Maturation). Everything in `apparatus/` is this law *run against a real domain*.

Decision-Driven Design has exactly one primitive claim. State it first, because the rest of the framework is machinery for keeping it.

## The unit: a decision

An LLM is a knowledge forecaster: given a context, it predicts what comes next. Humans work the same way — we reach a decision by forecasting from the knowledge we hold and the context we are in. A **decision** is a context-conditioned forecast. It is the unit of work.

A decision does not have to be encoded to be made. A human makes it by holding the relevant knowledge in their head. A model makes it by having that knowledge transmitted in its context. The knowledge required to make the decision *well* is the same in both cases — what differs is only **where the knowledge lives**.

That is the entire subject of the framework: for a given decision, where does the knowledge required to make it live, and what does it cost to move it from one place to another.

## The law

> **Conservation of Specification.** For a given task at a given assurance level, the specification demand is constant — fixed by the task, never by the system. Every system allocates that demand fully across four stores. Nothing is ever removed from the total; it is only moved between stores.

The four stores are the four places the knowledge required for a decision can live:

- **Encoded** — explicit and machine-readable, transmitted in the input: schema, prompt, context, model binding. Paid once, amortized over every run.
- **Mechanical verification** — the same specification applied at the *end* instead of the beginning: an acceptance predicate that checks the output rather than shaping the input.
- **Judgment** — a human head. The specification exists, unencoded, and is paid *per run* as review attention.
- **Escaped** — unallocated. Covered by no store, and therefore transferred to the user as defect exposure.

![The conservation of specification: for a given task the total is constant — encoded specification before the model, mechanical verification after it, judgment paid per run, and what no store covers escapes as defect exposure. Allocation profiles for exploration, under-engineered systems, and complete(spec, binding) at full autonomy.](assets/conservation-of-specification.svg)

The consequence that makes the law useful: **you cannot reduce the total, only relocate it.** "We saved on specification *and* on review" does not parse. It reads as "we shipped the difference" — the demand that left the encoded and judgment stores did not vanish; it moved to *escaped*, and escaped is defect exposure the user pays for.

This turns a vague quality conversation into an allocation audit. For any piece of work the four stores are the *terms of the agreement*: this much is encoded, this much is mechanically verified, this much is a named human's judgment, and nothing escapes unpriced. A system is trustworthy not because its model is good but because its allocation is fully accounted for and inspectable.

## The environment clause: when the demand is finitely encodable

The law says the demand is constant. It does not say the demand is *finite*. Whether the specification for a decision can be **finitely encoded** is a property of the environment, not of the decision.

- **Closed environment** — stable for the duration of the action. The action and its context can be described to their full extent; perfection has finite specification demand. Encode it all and the demand is met.
- **Open environment** — the environment can change while the action is in flight. The demand **diverges** as required assurance approaches 1: no finite knowledge fully specifies the outcome, because the change after commitment is irreducible. Firing a gun in wind is this case — the gust after the bullet leaves the barrel cannot be pre-encoded. Here an assurance level must be *declared*, and the residual demand carried in judgment or accepted as escape.

Software is not found closed — it is **closable**. "Writing code" is fully describable only against a frozen boundary: pinned toolchain, frozen repo state, content-addressed context, pinned model binding. Remove the pins and software is windy — a silent model upgrade, a drifting external API, another writer mutating shared state are all gusts. Computation is the one domain where closure can be *manufactured*, and most of the framework's machinery is exactly that manufacture: content-addressing, binding pinning, hermetic bundles, frozen discovery records are wind-removal equipment. The discipline does not assume a stable environment; it builds one. This is why the judgment-share-zero endpoint is reachable in software and nowhere physical.

Open environments do not break the law; they split the context by **binding time**. What cannot be encoded is the *value*; what can be encoded is the *policy* plus the *sensing obligation*. Frozen context binds when the spec is authored; sensed context binds when the action fires. A domain's exposure to wind is measured by how much of its context is necessarily sensed rather than frozen.

**The last wind.** In a fully pinned software system every component is deterministic by construction except one: the model. It cannot be pinned by value, only by binding — the single stochastic element left inside the closed box. This is why the highest tier of the Completeness Exercise is *sampled*: the sampling burden exists because, and only because, one component still has weather in it. It is also why residual variance is attributable at all — with everything else frozen, whatever varies is the model's.

**The Rice boundary.** For computation, *describability* is total — the program is its own complete description. *Universal mechanical verifiability* is not: Rice's theorem bars any general decision procedure for non-trivial semantic properties of programs. This is not a hole in the law; it is why the mechanical-verification store is scoped as **declared, per-task acceptance predicates**, each individually decidable — never a proof of everything. Verification is chosen property by property; the properties not chosen sit in judgment or escape, on the ledger like everything else.

Sequencing consequence: build first where the environment is maximally closable — software — because it is the one place the law's endpoint is reachable; extend outward in order of wind.

## The two boundaries, the two principles

A system has two boundaries with the world: knowledge comes *in*, effects go *out*. The law has one design principle guarding each. Both are corollaries of the law — they are how it is enforced rather than merely stated.

### Principle 1 — No tacit dependencies *(the input boundary)*

> Every piece of knowledge the system's behavior depends on is either **encoded** — explicit, machine-readable, transmitted in the input — or **declared** as a judgment point with a named owner. Nothing the system depends on may live only in someone's head.

The model consumes what is transmitted; it has no access to what is assumed. Knowledge that is neither encoded nor declared does not disappear — it silently converts into per-run judgment, paid in review attention at every execution and discovered only when review misses.

This is not an obligation to *eliminate* tacit knowledge. The [Polanyi Floor](03-the-polanyi-floor.md) is real: some knowledge cannot be made explicit, and a principle that denies this just invites hiding the floor to claim conformance. The obligation is to **map** the floor. A declared "annotation needed" list is conformant; an unstated house convention is not. Explicit residue is a declared judgment point; silent residue is a defect.

### Principle 2 — Completeness gates action *(the output boundary)*

> A model may commit an effect only through a specification that is **complete for its pinned binding** — complete(spec, binding), verified by the [exercise](02-completeness.md) at the tier the autonomy level demands — with **declared verification** of the output. Where human judgment substitutes for either, the substitution is declared and bounded by autonomy level. At full autonomy the judgment share is zero: encoded specification and mechanical verification cover the effect entirely.

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
