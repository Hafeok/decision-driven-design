# Apparatus — DDD Applied

**This directory is the concrete apparatus** for running the [core](../core/) law against a real domain. The core is the framework: one law (conservation of specification), measured by completeness, bounded by the Polanyi floor, projected as the funnel and maturation. This tier is *how you actually build it* — the roles, artifacts, sessions, bundles, phases, and orchestration that move a domain's decisions out of judgment and into the encoded store while keeping the ledger inspectable.

Read in order:

1. [**Decisions, Roles, and Artifacts**](01-decisions-and-artifacts.md) — *informative.* The geometry the apparatus sits in: work as a decision graph between two world boundaries, the inversion (decision as the unit, tool call as terminal), decisions private / artifacts as the interface, and the two graphs that meet at the session. **Start here.**
2. [**Entity Reference**](02-entities.md) — *normative.* Every entity, made precise. The vocabulary anything claiming conformance must use.
3. [**Encoding a Domain**](03-encoding-the-domain.md) — *informative.* The practical encoding layer: context, the bundle, SPMC, phases, and task types — the concrete form the law's "encoded" store takes.
4. [**The Autonomy Ladder**](04-autonomy.md) — *informative.* Per-role autonomy 0–5, why the unit is the role, and why each role's ceiling is its task type's measured Polanyi floor.
5. [**Conformance Capabilities**](05-conformance.md) — *normative.* The substrate a system must provide: artifact graph, declarative queries, shape constraints, provenance, session-scoped lineage, durable events.

Modeling toolkit:

- [**method/01 — Applying DDD to a real process**](method/01-applying.md) — *informative.* Pick one value action, walk backward, let artifacts and roles fall out of three questions per node. Worked on hiring.
- [**method/02 — The notation**](method/02-notation.md) — *informative.* A thin profile over DMN, BPMN, and C4, rendered as Mermaid, for drawing the result.

Composition — what multiple actors buy when composed, and what the seams cost (all *projected*; consumes the [seam-demand identity](../core/01-the-law/seam-demand.md) from core):

- [**Partition**](composition/partition.md) — actor composition for reach. A composite is an actor iff the joint action has a decidable acceptance predicate; partition buys reach (`⋃ Dᵢ`) at the cost of seam `|S|`; composition buys reach, not resolution. Good module boundaries are where `|S|` is locally minimal.
- [**Seam Allocation**](composition/seam-allocation.md) — the four-motive law: reach, speed, assurance, and failover are four allocations of the same seam demand. Assurance can be worse than one actor; failover is monotone-safe; hedged failover pays in compute, gated on idempotency. Carries `plan_composition`.
- [**Seam–Tier Coupling**](composition/seam-tier-coupling.md) — unencoded seam raises required tier *at the boundary* (why integration roles are senior); no free decomposition in tier currency; the interface contract as a one-time buy-down of recurring boundary cost; the seam as one object on two ledgers.

Projected notes and campaign instruments:

- [**Model-Actor Capacity**](model-actor-capacity.md) — *projected.* The active/total decomposition: the context window resolves into reach (total parameters) and resolution (active parameters), with a pre-declared escape-split prediction against dense vs MoE bindings.
- [**Task-Shape Corpus**](task-shape-corpus.md) — *instrument.* The two task shapes (breadth, depth) the escape-split campaign attributes against, the tagging discipline, and the capacity-selective seed corpus.
- [**Difficulty-Ladder Protocol**](difficulty-ladder-protocol.md) — *instrument.* Laddering seeds into the measurable escape band, and the sub-step verification that makes depth-shape attribution valid.

Appendices:

- [**Biology contrast**](biology-contrast.md) — *informative.* Why DDD doesn't model the harness as a body.
- [**Glossary**](glossary.md) — *informative.* Borrowed terms (DAG, DMN, BPMN, C4, RDF/SPARQL, …).
