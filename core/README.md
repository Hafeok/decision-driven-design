# Core — Decision-Driven Design

**Decision-Driven Design is one law and its consequences.** This directory is the framework itself, in the abstract and domain-independent. [`../apparatus/`](../apparatus/) is DDD *applied* — the concrete apparatus (roles, artifacts, sessions, bundles, orchestration) that runs this law against a real domain.

Read in order:

1. [**The Law**](01-the-law.md) — *normative.* Conservation of specification: for a task at an assurance level, the specification demand is constant and allocated across four stores (encoded, mechanical verification, judgment, escaped). The environment clause (closed vs. open, the last wind, the Rice boundary) and the two design principles, one per boundary. **Start here.**
2. [**Completeness**](02-completeness.md) — *normative.* The instrument that reads the allocation. `complete(spec, binding)`, the three-tier exercise, the residual with per-axis attribution, eight ordinary failure cases, and the projected/reported status vocabulary.
3. [**The Polanyi Floor**](03-the-polanyi-floor.md) — *normative track, projected.* The lower bound: knowledge that cannot move from judgment to encoded at any effort. The maturation asymptote and the per-task autonomy ceiling — measured, never asserted.
4. [**The Two Projections**](04-projections.md) — *informative.* The one law along two axes: the **funnel** (allocation over position in a chain) and **maturation** (allocation over recurrence in time).

The through-line: the law states what any specification must account for; completeness measures it; the floor bounds it; the projections are how it shows up as a design discipline along a chain and across a system's life. Nothing in `apparatus/` adds a new law — it is all machinery for keeping this one.
