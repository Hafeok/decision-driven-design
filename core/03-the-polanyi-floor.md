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

The name survives the split, and sharpens under it. Both components are Polanyi's mechanism — unsharable experience — operating on different channels: the transfer floor is his condition on the human-to-encoding channel; the intrinsic floor of physical actions is his condition on the action itself, embodied experience that admits no serialization. After the generalization the floor is not a gesture at "tacit knowledge"; it is the measured reach of Polanyi's condition per (task, actor) pair — which also demotes it from a primitive limit to a **derived** one, derived from the sharability of the action's experience. That derivation is exactly what makes the zero-floor postulate below statable: a floor can only be postulated to zero once it has a mechanism, and the mechanism's precondition can be shown absent.

## The zero-floor postulate for digital actions

> **Postulate.** For an action whose governing decision set and acceptance predicate both close over digital state, the intrinsic floor is **zero**: every governing decision admits finite encoding.

This is a conjecture, stated as one. It sits below *projected* on the evidence scale — no completeness tier can currently settle it — and it is offered with its derivation sketch and its falsification route, to be proven or broken later.

**The derivation sketch.** Three properties of the digital case, each already granted elsewhere in core, jointly remove Polanyi's precondition:

1. The governing decision set is **finite** — discrete state, finite alphabet, and the assurance level bounds the set ([the granularity bound](01-the-law.md#the-demand-is-denominated-in-decisions)).
2. The action is **totally describable** — the program is its own complete description ([the Rice boundary](01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable)).
3. The **experience of the action is itself a digital artifact** — the context, the sampled tokens, the tool results — and is therefore sharable by construction. Polanyi's mechanism (unsharable experience → unarticulable decisions) is not refuted; its precondition never obtains.

**The scoping condition is load-bearing.** *Both* the action and its acceptance predicate must close over digital state. An action that emits digital artifacts against a criterion referencing human experience — "make the interface feel calm" — re-imports tacitness through the verification decision, which is a human judging action, not a digital one. In a hybrid chain the floor is carried entirely by its human-experiential nodes; the digital nodes contribute none.

**The obvious objection, pre-empted.** "LLMs are the ultimate tacit system — they cannot articulate their own weights." True, and already separated: model internals are the [last wind](#two-limits-not-one) — a stochastic limit on *pinning*, answered by Tier-3 sampling — not a floor, which is an epistemic limit on *encoding*. The postulate claims nothing about the model's self-knowledge; it claims that the governing decisions of the task admit encoding.

**The consequence, if it holds.** Every floor ever measured on a purely digital task type is *transfer* floor — a human articulation problem, in principle movable — never intrinsic remainder. The [diagnostic fork](#the-convergence-result) sharpens accordingly: for digital task types, a residual that regrows after honest encoding attempts is always attributable to representation or elicitation failure, never to the task itself. The maturation asymptote for purely digital task types is 1 — full encoding — not (1 − floor). And the autonomy ceiling for every purely digital task type is, in principle, unbounded: Level 5 is reachable. Physical-world interactions retain their nonzero intrinsic floor; the digital/physical seam of a system is exactly where its floor budget lives.

**The falsification route.** The postulate is broken by exhibiting one purely digital task type whose annotation-needed residual regrows under every representation across sustained encode-exercise cycles — with the acceptance predicate verified mechanical, ruling out the scoping condition, and residual variance verified attributable, ruling out the last wind. That is a measurable program, which is what makes this a postulate rather than a position.

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
