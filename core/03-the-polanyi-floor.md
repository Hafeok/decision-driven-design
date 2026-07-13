# The Polanyi Floor: The Lower Bound

> **Core §3 — normative track, projected.** The [law](01-the-law.md) allocates a constant demand across four stores. This document names the boundary below which knowledge cannot move *out* of the judgment store into the encoded store — at any effort. It is the asymptote of what any specification can promise, and the per-task autonomy ceiling.

**Status:** Proposed, normative track. *Projected* per the [Completeness Exercise](02-completeness.md) tier definitions.

## The observation

Michael Polanyi: *we know more than we can tell.* A person recognizes a face instantly and cannot write down how. A reviewer rejects a design as wrong for the codebase and cannot enumerate the rule it violated. The knowledge is real, operative, and tacit — usable by its holder, unavailable to articulation.

Any discipline whose first principle is *encode the knowledge* ([No tacit dependencies](01-the-law.md#principle-1-no-tacit-dependencies-the-input-boundary)) collides with this immediately. The collision has two outcomes: deny the limit and hide it, or name the limit and map it. The framework does the second. The **Polanyi Floor** is the boundary, per task type, below which knowledge cannot be moved into machine-readable form — not because nobody has tried, but because *trying is how the boundary is found.* In the law's denomination it is a subset of the [governing decision set](01-the-law.md#the-demand-is-denominated-in-decisions): decisions that provably govern the action yet are made below articulation — owned, operative, and unencodable past some fidelity.

## Position in the law

The [conservation of specification](01-the-law.md#the-law) allocates a constant demand across four stores: encoded, mechanical, judgment, escaped. The floor is the reason the judgment store exists as a *permanent* store rather than a staging area: knowledge below the floor cannot migrate to encoded, at any effort. It lives in judgment legitimately — provided it is declared there.

At any moment the judgment store holds two populations:

- **Unconverted** — encodable knowledge that has not yet been encoded, because conversion has not paid for itself: the task type has not recurred enough to amortize. Exploration is almost entirely this.
- **Irreducible** — knowledge below the floor. No recurrence count converts it.

[Maturation](04-projections.md#maturation-allocation-over-recurrence) moves mass out of the first population and cannot touch the second.

## The convergence result

> **As a task type matures, its judgment store converges to its Polanyi Floor.** Judgment is not the floor; judgment *becomes* the floor in the limit, because everything else has moved to specification.

Three consequences:

1. **The floor is the asymptote of the maturation curve.** A corpus never reaches fully-encoded; it reaches (1 − floor). The least-cost routing fraction of a mature corpus is bounded by the floor, not by effort.

2. **A diagnostic fork.** Persistent judgment at high recurrence is *either* floor content *or* conversion negligence. The two are distinguishable mechanically: attempt the encoding and exercise it. Negligence converts and stays converted; floor content regrows the annotation-needed list after every honest attempt.

3. **An autonomy ceiling per task type.** Full autonomy requires the judgment share at zero ([Completeness gates action](01-the-law.md#principle-2-completeness-gates-action-the-output-boundary)). A task type with a nonzero floor therefore has a *maximum certifiable autonomy level*. The ceiling is not a policy choice; it is a measured property. *Claimed at the contracts tier:* the durable measurement is proposed to `ai-development-contracts` as the **FloorRecord** contract on the Build seam — see the handover proposal; the `frozen-as` edge lands here once accepted.

## The floor is measured, not declared

Nothing entitles a designer to assert where the floor sits. It is found empirically, by encode-exercise cycles: encode what appears encodable, run the [exercise](02-completeness.md), attribute the residual, encode again. What survives repeated cycles — the residual that reappears after every honest encoding attempt — is the floor for that task type, at that time.

A floor claim is itself *projected* until exercised, and floors can **move**: a better representation occasionally encodes what a worse one could not. The floor is an observation with a date on it, not a law of nature per task.

The canonical instance: the Figma-to-UIIntent bridge (`interface-framework`) extracts what it can mechanically, at two confidence tiers. Everything it cannot infer from the design file — intent that exists only in the designer's head — lands in an explicit `annotation-needed.json`. That file *is* the floor made visible: not a claim that the knowledge is absent, but a measured list of where encoding ran out and a declared judgment point begins. The unstated house convention and the annotation-needed entry are the same residue with opposite epistemic status — one is on the ledger, one is not.

## The floor is actor- and environment-relative

Polanyi's observation carries an assumption he had no reason to notice: one kind of actor. *We know more than we can tell* is a statement about humans transferring knowledge to humans, and its mechanism is specific — tacit knowledge is knowledge where the **experience of the action cannot be shared**, and therefore neither can the decisions made inside it. A body's experience of an action is embodied, continuous, and unserializable; the decisions trained into it resist articulation *because the channel cannot carry the experience they were made in*.

That locates the floor in the transfer channel, not in the knowledge. Once there is more than one kind of actor, the floor splits into two quantities that must not be conflated:

- **The intrinsic floor of an action** — whether the action's [governing decision set](01-the-law.md#the-demand-is-denominated-in-decisions) admits finite encoding *at all*. A property of the action's environment.
- **The transfer floor of a source actor** — whether the *current owner* of a governing decision can articulate it. A property of the channel between that actor and the encoding. This is Polanyi's original, and it is human-relative.

Every floor measurement made by encode-exercise cycles observes the *sum*. The decomposition matters because the two components have entirely different fates: transfer floor is contingent — a better representation, a better elicitation, a different channel can move it — while intrinsic floor is final.

The transfer floor is not only found; it is **manufactured**. Training amortizes a decision's per-run cost by embodying it ([the judgment store's cost structure](01-the-law.md#the-demand-is-denominated-in-decisions)), and embodiment pushes the decision below the actor's own articulate reach. The more trained the expert, the higher their transfer floor on exactly the decisions they execute best — expertise and articulability move in opposite directions by mechanism, not by accident. This is why elicitation from masters fails hardest where their performance is strongest, and why the floor of a mature human practice *grows* over the practice's lifetime even as its execution quality climbs.

The name survives the split, and sharpens under it. Both components are Polanyi's mechanism — unsharable experience — operating on different channels: the transfer floor is his condition on the human-to-encoding channel; the intrinsic floor of physical actions is his condition on the action itself, embodied experience that admits no serialization. After the generalization the floor is not a gesture at "tacit knowledge"; it is the measured reach of Polanyi's condition per (task, actor) pair — which also demotes it from a primitive limit to a **derived** one, derived from the sharability of the action's experience. That derivation is exactly what makes the zero-floor postulate below statable: a floor can only be postulated to zero once it has a mechanism, and the mechanism's precondition can be shown absent.

## The zero-floor postulate: the floor is in the predicate

> **Postulate (narrowed).** The intrinsic floor is a property of the **acceptance predicate**, not of the decision. It is **zero wherever the predicate is decidable over digital ground**, and **non-zero exactly where the predicate does not close — and whether it closes is, in general, undecidable** (Rice).

This is the corrected form of an earlier, stronger conjecture — *"if the governing decision set and the acceptance predicate both close over digital state, the intrinsic floor is zero"* — which external review found too strong. The retreat is recorded in full at [lineage §2.2](06-lineage-and-limits.md#22-the-zero-floor-postulate-retreat-to-the-acceptance-predicate); what survives is **sharper and more useful**, because it locates the floor precisely: in the predicate, not the decision. "Does it compile," "is this valid JSON," "do the tests pass" are decidable predicates — floor zero. "Is this the right architecture," "is this secure against an adversary who has not attacked yet" — the predicate does not close, and the floor is non-zero *for that reason*.

**Path-degeneracy makes the surviving claim robust.** Where the predicate *does* close, the floor is not merely zero — it is **robustly** zero, by [degeneracy](06-lineage-and-limits.md#6-required-citations) (Edelman & Gally, *PNAS* 2001: structurally different elements yielding the same function). Infinitely many distinct decision paths converge on an adequate act, so **no *particular* judgment is required — only an *adequate* one.** This is why a bound actor can be superhuman on closing-predicate tasks without "understanding" in any demanding sense: **adequacy is cheap when adequacy is checkable.** The consequence for how you obtain actors — *selection intensity is inversely proportional to predicate closure* — is worked out in [actors §2–3](05-actors.md#2-the-floor-is-in-the-predicate).

**The bound is three results, none about determinism.** They all hold in a fully deterministic universe, because they concern *decidability and knowability*, not whether the future is fixed:

1. **Rice's theorem** — all non-trivial semantic properties of programs are undecidable ([the Rice boundary](01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable)). The acceptance predicate can itself be uncomputable, and deciding whether it "closes" can require solving the halting problem.
2. **Inevitable model error** (Xu, Jain & Kankanhalli 2024; Kalai & Vempala) — a calibrated model must err on rare facts, with a non-zero lower bound. Even the leading rebuttal reduces the probability to *negligible*, not zero.
3. **Collective tacit knowledge** (Collins) — cannot be rendered explicit without socialization. The framework's floor decomposition (intrinsic + transfer) maps onto *relational and somatic* tacit knowledge but must not deny the *collective* kind.

*The determinism objection does not rescue the strong version.* A "know every variable and the future is fixed" premise imports the entire physical state, which is the opposite of *"closes over **digital** ground"* — the whole content of the postulate is that the relevant ground is **small and closed**, and universal determinism makes it **maximal and open**. And the objections above are about decidability, which determinism does not touch.

**The scoping condition is still load-bearing.** The predicate must close over *digital* ground. An action that emits digital artifacts against a criterion referencing human experience — "make the interface feel calm" — is exactly a predicate that does not close: it re-imports tacitness through the verification decision, which is a human judging action. In a hybrid chain the floor is carried entirely by its open-predicate nodes; the decidable-predicate nodes contribute none.

**The obvious objection, pre-empted.** "LLMs are the ultimate tacit system — they cannot articulate their own weights." True, and already separated: model internals are the [last wind](#two-limits-not-one) — a stochastic limit on *pinning*, answered by Tier-3 sampling — not a floor, which is an epistemic limit on *encoding*. The postulate claims nothing about the model's self-knowledge; it claims the floor is set by whether the *task's acceptance predicate* is decidable.

**The retired slogan.** *"There is no tacit knowledge in digital work"* is **retired** — it is not defensible against Collins's collective tacit knowledge. Its replacement: the relational and somatic tacit component can approach zero on decidable-predicate tasks; a floor remains from undecidable predicates, inevitable model error, and collective tacit knowledge.

**The consequence, where the predicate closes.** For a task type whose acceptance predicate is decidable over digital ground, every floor ever measured is *transfer* floor — a human articulation problem, in principle movable — never intrinsic remainder. The [diagnostic fork](#the-convergence-result) sharpens accordingly: a residual that regrows after honest encoding attempts is attributable to representation or elicitation failure, never to the task. The maturation asymptote is 1 — full encoding — and the autonomy ceiling is, in principle, unbounded: Level 5 is reachable. Task types whose predicate does not close retain a nonzero intrinsic floor; the closing/non-closing seam of a system is exactly where its floor budget lives.

**The falsification route.** The narrowed postulate is broken either way it could fail: exhibit a task type with a **decidable** acceptance predicate whose annotation-needed residual nonetheless regrows under every representation across sustained encode-exercise cycles (with residual variance verified attributable, ruling out the last wind) — *or* exhibit an **open** predicate whose performance can nonetheless be reliably assessed (it was not open after all). Either is a measurable program, which is what keeps this a postulate rather than a position.

## Two limits, not one

The floor is not the model-as-last-wind ([environment clause](01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable)), and conflating them corrupts attribution:

| | The Polanyi Floor | The last wind |
|---|---|---|
| Limit on | what can be **encoded** | what can be **pinned** |
| Located at | the input boundary | the model binding |
| Nature | epistemic — the knowledge resists articulation | stochastic — the component varies under identical input |
| Detected by | residual that survives encoding attempts | variance under a fully pinned input |
| Answered by | declared judgment points | Tier-3 sampling |

A perfectly encoded spec still samples, because of the wind. A perfectly pinned model still cannot be handed what is below the floor. These are the two independent reasons a residual is never provably empty by construction — and the reason the exercise *measures* rather than *proves*.
