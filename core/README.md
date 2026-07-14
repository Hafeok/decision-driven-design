# Core — Decision-Driven Design

**Decision-Driven Design is one law and its consequences.** This directory is the framework itself, in the abstract and domain-independent. [`../apparatus/`](../apparatus/) is DDD *applied* — the concrete apparatus (roles, artifacts, sessions, bundles, orchestration) that runs this law against a real domain.

Read in order:

0. [**Determination**](00-determination.md) — *normative.* The foundation: the two primitives (**decisions** and **ground**), the admission tests that keep them from becoming a universal solvent, the four stores restated ({rule, check, actor, nothing}), and the naming resolution (Principle, not physical Law). **Start here.**
1. [**The Law**](01-the-law.md) — *normative.* Conservation of determination demand: for a task at an assurance level, the demand is constant and allocated across the four stores. The environment clause (closed vs. open, the last wind, the Rice boundary), the register/lineage, the fixed-decomposition scope, and the two design principles, one per boundary.
2. [**Completeness**](02-completeness.md) — *normative.* The instrument that reads the allocation. `complete(spec, binding)`, the three-tier exercise, the residual with per-axis attribution, eight ordinary failure cases, and the projected/reported status vocabulary.
3. [**The Polanyi Floor**](03-the-polanyi-floor.md) — *normative track, projected.* The lower bound: knowledge that cannot move from judgment to encoded at any effort. The maturation asymptote and the per-task autonomy ceiling — measured, never asserted. Sharpened into *the floor is in the predicate* by Actors §2.
4. [**Actors**](04-actors.md) — *normative.* The **actor parameter** the law leaves open: the pinning-resolution spectrum (by value → by binding → by classification), the intrinsic floor's location in the acceptance predicate, selection versus training (*selection intensity is inversely proportional to predicate closure*), and how composite actors allocate seam demand. The part of the framework with the least prior art.
5. [**Lineage and Limits**](05-lineage-and-limits.md) — *normative.* The law's ledger: what it stands on (Ashby, Tesler, Brooks, Meyer, Kalman), where it was corrected, where it retreated (the zero-floor postulate → the floor is in the predicate; "Law" → "Principle"), and the falsification debts it still owes.
6. [**Determination and Intelligence**](06-determination-and-intelligence.md) — *normative.* The boundary the primitives imply: a thermostat determines and is not intelligent, so determination is necessary and nowhere near sufficient — and the LLM-intelligence debate is structurally undecidable, because every benchmark is a closing predicate.

Topic chapters — a determination the framework makes often enough to state once:

- [**The Closure Principle**](closure-principle.md) — *normative.* An actor's own prior output is not ground; consuming it closes a loop with no corrective term. Estimator divergence / observability failure — cite **Kalman**.
- [**Adversarial Ground**](adversarial-ground.md) — *normative.* Ground is an attack surface: you can encode ground you control, but must mechanically verify ground you don't — and "poisoned ground" is a *family* of failures, not one mechanism.
- [**The Two Projections**](projections.md) — *informative.* The one law along two axes: the **funnel** (allocation over position in a chain) and **maturation** (allocation over recurrence in time).

Actor-type readings — the same law, read against one actor's physics; each specializes [Actors](04-actors.md) to one store:

- [**The Actor's Capacity**](context-window.md) — *normative.* Context length as the model actor's total allocation budget: three of the four stores compete for one window. Why explore mode wants long context, why context length bounds action size, and the funnel's physical necessity (decomposition as capacity management).
- [**Escape Under Pressure**](escape-under-pressure.md) — *normative.* The escaped store at fire time, actor-general: when demand exceeds capacity, the prior decides — defaults for a program, habit for a human, the weights for a model. Hallucination as an escaped decision surfaced as output, and the escape/wind taxonomy. Falsification design: [experiments/escape-wind](../experiments/escape-wind/DESIGN.md).

Chapter extensions — insertion blocks and lemmas, each living in its chapter's subdirectory (all *projected*):

- [**Seam Demand Under Decomposition**](01-the-law/seam-demand.md) — the conservation identity for decomposition: splitting a decision set into separately-discharged parts manufactures seam demand, `|D_comp| = |D_single| + |S|`. Actor-neutral; consumed by [`apparatus/composition/`](../apparatus/composition/).
- [**Action, Target, and the Two Levers**](01-the-law/action-target-and-levers.md) — what an action is (a decidable acceptance predicate — intents lack one), the success decomposition `1 − success = esc_escape + esc_wind`, `plan(p*)`, and the two levers (specification vs actor) priced per residual class.
- [**The Finite-Index Lemma**](02-completeness/finite-index-lemma.md) — KC1, finiteness: when a task's governing decision set is finite, and therefore knowable in finite terms.
- [**The Decidability Corollary (KC2 + KC3)**](02-completeness/decidability-corollary.md) — membership decidability and loop termination as a corollary of the zero-floor postulate; assembles the Knowability Theorem (KC1 + KC2 + KC3).
- [**The Tier–Specification Inverse Law**](03-the-polanyi-floor/tier-specification-inverse-law.md) — derives, rather than asserts, why withholding encoded specification forces required actor tier upward — and why past a point that demand is met only by selection, not training.

The through-line: determination gives the primitives; the law conserves the demand they constitute; completeness measures it; the floor bounds it; actors indexes it to the thing doing the deciding; lineage-and-limits keeps it honest — cited where additive, retreated where not; and determination-and-intelligence marks the boundary the framework refuses to cross. The projections show it as a design discipline along a chain and across a system's life. Nothing in `apparatus/` adds a new law — it is all machinery for keeping this one.
