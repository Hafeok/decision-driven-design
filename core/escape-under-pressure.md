# Escape Under Pressure: The Prior Decides

Core §N — normative. A property of the law read at the moment an actor's capacity is exceeded. The Conservation of Specification law defines the escaped store as decisions that fall to "a prior, a default, chance, or physics." This section works out what that clause costs when an actor is capacity-bound: escape is not only an authoring-time allocation failure but a fire-time mechanism, actor-general, with a distinct observable per actor type. The model actor's observable is hallucination. The human actor's observable is the skipped step. They are the same store wearing different faces.

## The mechanism, actor-general

Every actor has finite capacity: the space in which encoded specification is held, sensed facts are inspected, and per-run judgment actually happens. For a model this capacity is the context window. For a human it is working memory under attention. For a classical program it is whatever state its author gave it. The law quantifies over actors, and so does capacity: there is no actor without a bound.

When an action's demand exceeds what the actor can hold — encoded plus sensed plus judgment-in-flight — conservation forbids the residual from vanishing. The decisions that no longer fit do not become unnecessary; they become **unowned**. They fall out of the priced stores and into escape, and escape resolves the way the law already says it does: by the actor's prior.

This is the fire-time face of a clause the law states at authoring time. An allocation audit reads escape as a static quantity — the decisions nobody was assigned. Under capacity pressure, escape acquires a dynamics: decisions that *were* assigned to judgment get shed when the capacity to hold them runs out. The demand did not shrink. The ownership did.

The spatial incentive makes this structural rather than accidental. Of the four stores, escape is the only one that costs no capacity — an unowned decision occupies no window, no working memory, no state. Under pressure, escape is the cheapest store. An actor near its bound will therefore *structurally tend* to shed decisions to its prior, not through carelessness but because the stores compete for a finite resource and one of them is free. The completeness gate exists, among other reasons, to forbid this cheap path: it refuses to let an effect commit through an allocation with unpriced escape, regardless of how tight the capacity.

## The prior, per actor

What escape resolves to is actor-specific. The mechanism is general; the prior is not.

**The classical program's prior is its defaults.** The unhandled case falls through to whatever the author left in place — a default branch, an uninitialized value, an implicit conversion. This is the one honest prior: it is written down. Program escape is inspectable in the source, before it ever fires.

**The human's prior is habit.** The trained default, the heuristic, the way-we-always-do-it. Under load, decisions that should have been made deliberately are made by the body or the pattern instead. The human prior is often *good* — that is what training is for — but it is unaudited at the moment it fires. The danger is not that habit is wrong; it is that **nobody decided to use it**. The decision to fall back was itself never made. Human factors research has documented this dynamics for decades without the allocation vocabulary: stress narrows attention; load induces heuristic substitution; time pressure produces procedural shortcuts. The framework's contribution is naming it as conservation — the decisions did not get cheaper under pressure; they got unowned.

**The model's prior is the weights.** An escaped decision falls to the training distribution, and the training distribution always answers. This is the actor-specific physics that makes model escape uniquely dangerous: the prior's answer is a fluent, confident token sequence, because producing fluent continuations is what the prior *does*. Where a program's default is visible and a human's reversion is at least reconstructable, the model's escaped decision arrives **indistinguishable in surface form from an owned one**.

## The observable, per actor

Same store, three faces:

- Program escape looks like a default firing — a fallthrough, a silent coercion.
- Human escape looks like a skipped step, a reversion to the more-practiced procedure, an "I didn't think of it."
- Model escape looks like fluent confabulation — **hallucination**.

The visibility ordering is the risk ordering. Program escape is inspectable before fire time. Human escape is invisible at fire time but reconstructable in hindsight — the skipped checklist item can be found in the incident review. Model escape is camouflaged at the moment of production: the defect ships wearing the markings of an owned decision. Hallucination is not a malfunction under this reading. It is **the escaped store made observable in this actor type** — defect exposure with the defect's markings removed.

This yields the claim in one line:

> **A hallucination is an escaped decision surfaced as output.** When an action's demand exceeds what is encoded, sensed, and within the actor's judgment capacity, conservation forbids the residual from vanishing — it is decided by the prior, and the model's prior produces output indistinguishable in form from an owned decision.

## The predictions

A law-candidate earns its standing by predicting the known empirics from the store structure alone:

- **Demand not encoded** → under-specified prompts hallucinate more. Known.
- **Facts not sensed** → questions whose facts are absent from context confabulate; retrieval reduces hallucination *because* it relocates the facts from escape into the sensed store. Grounding works by allocation, not by magic. Known.
- **Capacity pressure** → near the context bound, the spatial incentive applies: escape is the only free store, so the actor structurally sheds decisions to the prior. Predicts hallucination increasing near context limits and degrading retrieval from the middle of overlong contexts. Known.
- **The human parallel** → checklists reduce error not by adding knowledge the operator lacks but by **relocating decisions out of the capacity-pressured judgment store into encoding**, where load cannot shed them. Predicts checklists matter most exactly where load is highest — which is where they were empirically discovered to matter: surgery, aviation. Known, retroactively explained.

## The taxonomy: escape versus wind

The frame must draw one boundary honestly, and drawing it makes the account stronger: **not all confabulation is escape.** Models also err when the fact is in context and the demand is encoded — a retrieval-from-window failure, an attention failure. That is not the escaped store. That is the **last wind**: the actor's residual variance under its tightest available pinning.

So the account yields a two-class taxonomy, and the classes have different owners and different remedies:

**Escape-hallucination** — structural. Predicted by the allocation and *reducible by allocation*: encode more of the demand, sense more of the facts, decompose the action to relieve capacity. This is the class the framework can drive toward zero, because it was never an actor problem — it was an allocation problem wearing the actor's face.

**Wind-hallucination** — residual. The actor's variance with the allocation fully accounted for. Not reducible by allocation at all — only by binding choice (a better-pinned actor) or absorbed by the sampled tier of the Completeness Exercise, which exists precisely because the actor still has weather in it.

The taxonomy is actor-general, as it must be. The human equivalent of wind is the qualified operator's residual error rate with the checklist fully followed — which is exactly what the human binding regime's recertification cadence exists to re-measure.

The operational rule that falls out: **audit the allocation first.** If the allocation has unpriced escape, the hallucination was specified in — no model upgrade fixes it, and blaming the actor is a category error. This is the funnel principle's sibling: hallucination at the implementation role signals upstream under-allocation, not a capability gap. Only once the allocation is clean is residual confabulation attributable to wind — and then, and only then, is it a binding question: measurable by sampling, answerable by actor choice.

## Epistemic guardrail

This is a specification-level account: it states when confabulation is structurally licensed and who owns the decision that produced it. It is not a mechanistic account of transformer sampling. The law predicts *where* the prior gets to decide; it does not explain the prior's internals. The two claims must not be fused — asserting the mechanistic reading would be a status upgrade this section has not earned. The account's standing rests on its predictions matching the known empirics from the store structure alone, and on nothing further.

---

## Placement note

This section belongs after the four stores and the environment clause (it reuses the escaped store's definition and the last-wind spectrum) and is a sibling of the actor-capacity section (context length as allocation budget), which cites it for the model case. The dependency is directional: this section stands on the store structure alone and does not require the window argument; the window section's escape-trap passage is the model-actor instance of the mechanism stated generally here. It is core, not apparatus: it is the law read at fire time under capacity pressure, quantified over actors.
