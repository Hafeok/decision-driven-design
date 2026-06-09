# Glossary — borrowed and external concepts

> **Appendix C. Glossary of borrowed terms** — *informative.* Definitions for terms the specification uses but does not itself define, because they come from external work.

A short reference for terms the DDD docs use but do not define, because they come from outside the framework. The [Entity Reference](02-entity-reference.md) covers DDD's own vocabulary; this page covers everything the docs *reference* from established work elsewhere.

Each entry is one paragraph: what it is, and how DDD uses it.

---

### DAG — Directed Acyclic Graph

A graph of nodes connected by directed edges, with no cycles — you can never follow edges out of a node and end up back at it. In DDD, the decision graph is a DAG: artifacts feed into decisions, which produce artifacts that feed into other decisions, terminating at value actions. The acyclic property is what makes the graph traversable for bundle assembly, replayable for audit, and finite for analysis. The DAG is contrasted with the **pipeline** — a linear sequence of stages — throughout the foundations doc; multiple artifacts can feed one decision, and one decision can spawn multiple artifacts, which a pipeline cannot express.

The DAG isn't strictly forward-only in the runtime sense: feedback flow can re-open upstream artifacts and pause dependent downstream chains until they re-converge. The acyclicity is a property of the *artifact dependency* edges; feedback travels as new artifacts, not as edges back through existing ones.

### DMN — Decision Model and Notation

An OMG standard for modeling decisions, originally aimed at business-rule engines. DDD borrows DMN's **Decision Requirements Diagram (DRD)** — the sub-notation whose nodes are decisions and whose edges are *information-requirement dependencies* (B requires A's output), not control-flow tokens. That edge semantic is exactly the "DAG, not a pipeline" property the framework rests on. DDD redefines the node: a DDD decision is a context-conditioned forecast performed by a role, not a decision table. See [Notation §Decision graph](05-notation.md).

### BPMN — Business Process Model and Notation

Another OMG standard, this one for flow-style business processes. DDD borrows BPMN's **lane** glyph for the session view — when a diagram needs to show who acts when (handoffs, the action↔interpretation pairing), lanes are the cleanest existing notation. Used sparingly, because BPMN's spine is *token flow*, which is the factory metaphor DDD exists to leave behind. See [Notation §Session view](05-notation.md).

### C4 — the C4 model

Simon Brown's four-level architectural model: Context, Containers, Components, Code. DDD borrows the container/component framing for the system view — when a diagram needs to show systems, their internal pieces, and the buses between them, C4's conventions apply unchanged. See [Notation §System composition view](05-notation.md).

### Mermaid

A text-based diagram language that renders to SVG. Chosen as the rendering target for the notation profile because Mermaid diagrams are diff-friendly, render natively in GitHub and most doc tools, and stay co-located with the prose. Every diagram in the docs is authored as Mermaid source and rendered at view time. See [Notation](05-notation.md).

### RDF, triple store, SPARQL

The W3C semantic-web stack DDD's reference implementation builds on.

- **RDF (Resource Description Framework)** — a graph data model where everything is a `(subject, predicate, object)` triple. Suits DDD because artifacts and edges are natively triple-shaped: `(feature-42, decomposes_from, brief-9)`.
- **Triple store** — a database that stores and queries RDF. The implementation uses **Oxigraph**, an embedded Rust triple store.
- **SPARQL** — the standard query language for RDF. Bundle assembly is implemented as curated SPARQL queries against the triple store: deterministic, reviewable, version-controlled. See [Implementation §3](04-implementation.md).

### SHACL — Shapes Constraint Language

A W3C standard for validating RDF graphs against declared shape constraints. DDD uses SHACL as the first layer of audit in the reference implementation: schema conformance and edge-cardinality checks are SHACL shapes the triple store evaluates directly. Heavier audits (gap analysis, drift detection) compose on top of SHACL but are LLM-driven. The decision-graph invariants — kind-resolves-to-cell, every-prompt-has-generation-guidance, every-artifact-governed-and-rooted, per-role count agreement — are also SHACL shapes, constraining edge topology rather than classes. See [Implementation §3](04-implementation.md).

### PROV-O — the Provenance Ontology

A W3C standard vocabulary for describing the lineage of things — its core terms are *Entity*, *Activity*, and *Agent*, related by predicates like `wasGeneratedBy`, `used`, and `wasAssociatedWith`. DDD's reference implementation annotates every session-produced triple with PROV-O, so the artifact graph maps directly onto it: artifact (Entity) `wasGeneratedBy` session (Activity), which `used` the bundle and `wasAssociatedWith` the role and model. PROV-O captures the **artifact axis** of provenance completely. It is deliberately *not* stretched to cover the **decision axis**: the `governed_by` edge — "this choice was governed by that generation guidance" — has no PROV-O analogue, so DDD records decisions as first-class and lets the two axes meet at the session rather than forcing decisions into a provenance dialect. See [Entity Reference §Provenance](02-entity-reference.md) and [Foundations §Two graphs](01-foundations.md).

### MCP — Model Context Protocol

Anthropic's open protocol for connecting LLM agents to tools, data sources, and services through a uniform interface. DDD's plug-in transports use MCP — both **MCP/stdio** for local agents and **MCP/HTTP** for remote ones — so the same tool surface a CLI exposes to humans is exposed to LLM clients without divergence. The protocol distinction the entity reference draws between *effect-MCPs* (value-action tools) and *knowledge-MCPs* (context acquisition) is DDD's own typology layered on top of MCP. See [Entity Reference §Transport](02-entity-reference.md) and §Worker.

### OCI — Open Container Initiative

The standards body behind the container image format and runtime spec popularized by Docker. In DDD, **WorkerImage** — the packaged realization of a worker — is an OCI image: the SDK, the wire protocol, the worker code, and the capability claims, distributable through any OCI registry. Worker (the binding) is distinct from WorkerImage (the package); one image can realize many workers. See [Entity Reference §Worker](02-entity-reference.md).

### Frontier model

Informal industry term for the most capable LLMs currently available — the leading multimodal, long-context, tool-using models from major labs. DDD uses "frontier" only as a capability descriptor in role-binding examples ("a design lead consuming Figma files needs a frontier multimodal model"), never as a model identity. The model catalog resolves capability tags to concrete models, so "frontier" in the docs is a shorthand for a capability profile, not a permanent recommendation.
