# Core — Decision-Driven Design

**Decision-Driven Design is one law and its consequences.** This directory is the framework itself, in the abstract and domain-independent. [`../apparatus/`](../apparatus/) is DDD *applied* — the concrete apparatus (roles, artifacts, sessions, bundles, orchestration) that runs this law against a real domain.

Read in order:

1. [**The Law**](01-the-law.md) — *normative.* Conservation of specification: for a task at an assurance level, the specification demand is constant and allocated across four stores (encoded, mechanical verification, judgment, escaped). The environment clause (closed vs. open, the last wind, the Rice boundary) and the two design principles, one per boundary. **Start here.**
2. [**Completeness**](02-completeness.md) — *normative.* The instrument that reads the allocation. `complete(spec, binding)`, the three-tier exercise, the residual with per-axis attribution, eight ordinary failure cases, and the projected/reported status vocabulary.
3. [**The Polanyi Floor**](03-the-polanyi-floor.md) — *normative track, projected.* The lower bound: knowledge that cannot move from judgment to encoded at any effort. The maturation asymptote and the per-task autonomy ceiling — measured, never asserted.
4. [**The Two Projections**](04-projections.md) — *informative.* The one law along two axes: the **funnel** (allocation over position in a chain) and **maturation** (allocation over recurrence in time).

Actor-type readings — the same law, read against one actor's physics:

- [**The Actor's Capacity**](context-window.md) — *normative.* Context length as the model actor's total allocation budget: three of the four stores compete for one window. Why explore mode wants long context, why context length bounds action size, and the funnel's physical necessity (decomposition as capacity management).
- [**Escape Under Pressure**](escape-under-pressure.md) — *normative.* The escaped store at fire time, actor-general: when demand exceeds capacity, the prior decides — defaults for a program, habit for a human, the weights for a model. Hallucination as an escaped decision surfaced as output, and the escape/wind taxonomy. Falsification design: [experiments/escape-wind](../experiments/escape-wind/DESIGN.md).

Chapter extensions — insertion blocks and lemmas, each living in its chapter's subdirectory (all *projected*):

- [**Seam Demand Under Decomposition**](01-the-law/seam-demand.md) — the conservation identity for decomposition: splitting a decision set into separately-discharged parts manufactures seam demand, `|D_comp| = |D_single| + |S|`. Actor-neutral; consumed by [`apparatus/composition/`](../apparatus/composition/).
- [**Action, Target, and the Two Levers**](01-the-law/action-target-and-levers.md) — what an action is (a decidable acceptance predicate — intents lack one), the success decomposition `1 − success = esc_escape + esc_wind`, `plan(p*)`, and the two levers (specification vs actor) priced per residual class.
- [**The Finite-Index Lemma**](02-completeness/finite-index-lemma.md) — KC1, finiteness: when a task's governing decision set is finite, and therefore knowable in finite terms.
- [**The Decidability Corollary (KC2 + KC3)**](02-completeness/decidability-corollary.md) — membership decidability and loop termination as a corollary of the zero-floor postulate; assembles the Knowability Theorem (KC1 + KC2 + KC3).
- [**The Tier–Specification Inverse Law**](03-the-polanyi-floor/tier-specification-inverse-law.md) — derives, rather than asserts, why withholding encoded specification forces required actor tier upward — and why past a point that demand is met only by selection, not training.

The through-line: the law states what any specification must account for; completeness measures it; the floor bounds it; the projections are how it shows up as a design discipline along a chain and across a system's life. Nothing in `apparatus/` adds a new law — it is all machinery for keeping this one.
