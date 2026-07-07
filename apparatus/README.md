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

Appendices:

- [**Biology contrast**](biology-contrast.md) — *informative.* Why DDD doesn't model the harness as a body.
- [**Glossary**](glossary.md) — *informative.* Borrowed terms (DAG, DMN, BPMN, C4, RDF/SPARQL, …).
