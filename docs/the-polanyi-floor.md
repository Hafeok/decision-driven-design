# The Polanyi Floor

> Some knowledge can be used but not told. The Polanyi floor is the framework's name for the empirical boundary of what can be encoded — mapped, never denied, and measured per task type.

**Status:** Proposed, normative track. *Projected* per the [Completeness Exercise](completeness-exercise.md) tier definitions.

---

## The observation

Michael Polanyi: *we know more than we can tell.* A person can recognize a face instantly and cannot write down how. A reviewer can reject a design as wrong for the codebase and cannot enumerate the rule it violated. The knowledge is real, operative, and tacit — usable by its holder, unavailable to articulation.

Any discipline whose first principle is *encode the knowledge* ([No tacit dependencies](01-foundations.md#principle-1--no-tacit-dependencies-specification-pillar-the-input-boundary)) collides with this immediately. The collision has two possible outcomes: deny the limit and hide it, or name the limit and map it. The framework does the second. The **Polanyi floor** is the boundary, per task type, below which knowledge cannot be moved into machine-readable form — not because nobody has tried, but because trying is how the boundary is found.

## The canonical instance

The Figma-to-UIIntent bridge (`interface-framework`) extracts what it can mechanically, at two confidence tiers. Everything it cannot infer from the design file — intent that exists only in the designer's head — lands in an explicit `annotation-needed.json`. That file *is* the floor, made visible: not a claim that the knowledge is absent, but a measured list of where encoding ran out and a declared judgment point begins. The unstated house convention and the annotation-needed entry are the same residue with opposite epistemic status — one is on the ledger, one is not.

## Position in the conservation law

The [conservation of specification](01-foundations.md#the-conservation-of-specification) allocates a constant demand across four stores: encoded, mechanical, judgment, escaped. The floor is the reason the judgment store exists as a *permanent* store rather than a staging area: knowledge below the floor cannot migrate to encoded, at any effort. It lives in judgment legitimately — provided it is declared there.

## The convergence result

At any time, the judgment store holds two populations:

- **Unconverted** — encodable knowledge that has not yet been encoded, because conversion has not paid for itself: the task type has not recurred enough to amortize, or the catalog is young. Explorer mode is almost entirely this.
- **Irreducible** — knowledge below the floor. No recurrence count converts it.

Maturation moves mass out of the first population and cannot touch the second. Therefore:

> **As a task type matures, its judgment store converges to its Polanyi floor.** Judgment is not the floor; judgment *becomes* the floor in the limit, because everything else has moved to specification.

Three consequences:

1. **The floor is the asymptote of the maturation curve.** A corpus never reaches fully-encoded; it reaches (1 − floor). The least-cost routing fraction of a mature corpus is bounded by the floor, not by effort.
2. **A diagnostic fork.** Persistent judgment at high recurrence is either floor content or conversion negligence. They are distinguishable mechanically: attempt the encoding and exercise it. Negligence converts and stays converted; floor content regrows the annotation-needed list.
3. **An autonomy ceiling per task type.** Full autonomy requires the judgment share at zero ([Completeness gates action](01-foundations.md#principle-2--completeness-gates-action-execution-pillar-the-output-boundary)). A task type with a nonzero floor therefore has a maximum certifiable autonomy level. The ceiling is not a policy choice; it is a measured property. *Claimed at the contracts tier:* the durable measurement is proposed to `ai-development-contracts` as the **FloorRecord** contract on the Build seam — see the handover proposal; the `frozen-as` edge lands here once accepted.

## The floor is measured, not declared

Nothing entitles a designer to assert where the floor sits. It is found empirically, by encode-exercise cycles: encode what appears encodable, run the [exercise](completeness-exercise.md), attribute the residual, encode again. What survives repeated cycles — the residual that reappears after every honest encoding attempt — is the floor for that task type, at that time. A floor claim is itself *projected* until exercised, and floors can move: better representations occasionally encode what a worse representation could not. The floor is an observation with a date on it, not a law of nature per task.

## Two limits, not one

The floor is not the model-as-last-wind, and conflating them corrupts attribution:

| | The Polanyi floor | The last wind |
|---|---|---|
| Limit on | what can be **encoded** | what can be **pinned** |
| Pillar | specification | execution-facing (the binding) |
| Nature | epistemic — the knowledge resists articulation | stochastic — the component varies under identical input |
| Detected by | residual that survives encoding attempts | variance under a fully pinned bundle |
| Answered by | declared judgment points | Tier-3 sampling |

A perfectly encoded spec still samples, because of the wind. A perfectly pinned model still cannot be handed what is below the floor. These are the two independent reasons a residual is never provably empty by construction — and the reason the exercise measures rather than proves.
