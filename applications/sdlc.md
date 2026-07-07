# Application: the software development lifecycle

> **Non-normative example · Status: projected.** This is DDD's origin domain and its most-frozen application. The derivation below did not stay in this document: it precipitated a real ecosystem — a foundation ([`ai-development-foundations`](https://github.com/Hafeok/ai-development-foundations)), a contracts tier ([`ai-development-contracts`](https://github.com/Hafeok/ai-development-contracts)), and a conformant specification framework ([`product-framework`](https://github.com/Hafeok/product-framework)). Frozen records are derivations, not runs: by the [status discipline](../core/02-completeness.md#application-status-is-defined-by-these-tiers) everything here remains *projected* until a named system reports against it. Status terms (*projected* / *reported*) are normative, defined by the [Completeness Exercise](../core/02-completeness.md) tiers.
>
> Relies on framework concepts defined in the spec: [the law and its two principles](../core/01-the-law.md), [Task and TaskType](../apparatus/02-entities.md#task), [the maturation curve](../core/04-projections.md#maturation-allocation-over-recurrence), [the funnel](../core/04-projections.md#the-funnel-allocation-over-position), [Decision and the two graphs](../apparatus/01-decisions-and-artifacts.md#two-graphs-artifacts-and-decisions), and [SPMC](../apparatus/02-entities.md#spmc-schema-prompt-model-context). This doc applies them; it does not re-derive them.

---

## The domain

Software development; the terminal value action is `shipped feature`. It is the framework's origin domain by design, not accident. The [environment clause](../core/01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable) says software is the one domain where closure can be *manufactured* — pinned toolchain, frozen repo state, content-addressed context, pinned model binding — so it is the one place the law's endpoint, judgment share zero at full autonomy, is actually reachable. Build first where the environment is maximally closable. The SDLC is that place, which is why this application's projections froze first.

## The practice this replaces

The standard shape of LLM code generation is a harness — a coding agent handed a feature and a tool belt and steered toward a goal. One worker, broad authority, a long agentic loop, human steering when it drifts. In DDD terms that is *one role making many kinds of decision in one session* — infrastructure, API shape, test strategy, error handling, naming, all fused. The session's decision graph is a black box: when the output is wrong you cannot tell whether the infrastructure reasoning or the test strategy was at fault, because they were never separated.

DDD says code is an artifact like any other — schema, producing session, subject-matter decisions, a place in both graphs. Once code is an artifact, a unit of implementation is not one artifact but a cluster of typed artifacts, each its own `(role, artifact type)` cell with its own prompt and generation decisions. The single steered agent decomposes into a small graph of single-purpose generators.

## The derivation, in brief

The framework's [composition levels](../apparatus/02-entities.md#task) land in the SDLC as **feature** (the value-anchored unit), **task** (the typed unit: *add-an-entity*, *expose-a-CRUD-API*, *wire-a-migration*, each owning a cell cluster), and **cell** (one prompt, one artifact: the contract, the handler, the test cases). Cell boundaries fall where the crossing test puts them — a boundary exists where a sub-artifact crosses to inform a different downstream decision. The API contract is a cell (tests, handler, and clients all read it); variable naming inside one function is not (it crosses nothing, and is absorbed into the handler generator's standing authority).

Inside one feature the cells sit at different points on the [funnel](../core/04-projections.md#the-funnel-allocation-over-position): the contract upstream, where the hard problem-domain calls concentrate; the handler downstream of it, translating a well-specified problem into a known idiom on a small code-specialized model. The funnel is a forcing function — if the handler cell needs a frontier model, the first question is whether the contract pinned the calls it should have.

At the task level, work routes by recognition: a **known task type** dispatches its cell cluster mechanically — instantiate the cells, assemble bundles in the declared `derived_from` order, bind the prompts, run the coherence audit. An **unknown task type** goes to a broad worker — the principled standing of the broad-authority coding agent — which one-shots the task or explores it and mints a new [TaskType](../apparatus/02-entities.md#tasktype) for the catalog. The mixed feature is the normal case; the broad path feeds the typed path. Over time this is the [maturation curve](../core/04-projections.md#maturation-allocation-over-recurrence): the catalog fills, the broad worker retires from the common cases, and "the architecture supports 80% of new features" becomes the measured [type-decomposability fraction](../apparatus/02-entities.md#fitness-function).

![Maturation curve](../core/assets/maturation.svg)

## Where the derivation froze

Working this application through the decision-first lens is what precipitated the two-pillar split — specification and execution as independent foundations (see the [genealogy](../core/02-completeness.md#genealogy)). The derivation was exercised at this tier, then frozen *downward* into more stable tiers of a real ecosystem:

```
ACTUAL IMPLEMENTATIONS      project specs, running pipelines           most volatile
FRAMEWORK IMPLEMENTATIONS   Decision-Driven Design · product-framework
SHARED CONTRACTS            ai-development-contracts  (WorkUnit · VerdictEvent · seam schemas)
FOUNDATION                  ai-development-foundations  (the two pillars)   most stable
```

Authorship is directional; dependency is downward (`ai-development-foundations` RFC 0001). This framework authored the foundation's claims, and thereafter depends on them like any other framework implementation. The lower tiers accordingly do not cite this repository — the foundation names Decision-Driven Design only as an illustrative framework implementation, and `product-framework` conforms to the foundation, never to DDD. That silence is not an omission; it is the Stable Dependency Principle holding. The genealogy lives here, in this document's promotion record, which is the only correct place for it.

## The foundation: `ai-development-foundations`

The foundation splits building software with AI into exactly two problems — **getting intent into the machine correctly** (specification) and **letting the machine act without losing control** (execution) — held as peer pillars, neither containing the other. This is the [law's two boundaries](../core/01-the-law.md#the-two-boundaries-the-two-principles), frozen as governance:

- **Pillar One, the Specification Framework**, governs the input. Its governing rule, the **derivation contract**, is Principle 1 in foundation vocabulary: every How traces to a What; every SPMC bundle traces to a How; a How element with no What anchor is flagged as an *undeclared product decision* and escalated — tacit knowledge surfaced, not silently absorbed.
- **Pillar Two, the Execution Contract**, governs the effects. Its governing rule, the **closure contract**, is Principle 2: every capability grant traces to a need, every output is judged by a declared verifier before acceptance, every verdict maps to a declared consequence. Its sharpest line — *"the autonomy level is not a setting; it is the shape of the transition contract"* — is the [autonomy ladder](../apparatus/04-autonomy.md) restated as the set of verdict→consequence bindings that may proceed without a human.

Four accepted RFCs carry the frozen projections: **RFC 0001** (the seam between the pillars is producer-owned), **RFC 0002** (each SPMC axis pinned to the precision at which it affects output — the Model axis is a *binding*, not a name, which is the precondition for [complete(spec, binding)](../core/02-completeness.md#definition) having a stable target), **RFC 0003** (the three design principles: Stable Dependency, Loose Coupling, High Cohesion), and **RFC 0004** (the seam pattern — a new domain adds a seam, never a third pillar). Conformance is self-declared against published checklists and indexed in a registry; the ledger is inspectable by anyone who reads a framework against the checklist.

## The specification framework: `product-framework`

The registry's one listed framework. It instantiates Pillar One for software — an open standard describing a product as three connected, machine-readable models — and is the clearest picture available of what the law's **encoded store** looks like when someone actually writes it down for the SDLC:

- **The What** (systems, a domain model with reference data, an event model) and **the How** (decisions, patterns, contracts, a repository layout model) are one typed graph. The framework's representation rule is Principle 1 with teeth: a specification that merely *describes* the graph in prose, on which footprint and `done` are not computable, is non-conformant *regardless of content* — a spec that cannot be walked cannot have its allocation read.
- **The Decider** is the funnel run inside the spec. Its signature is derived from the event model; only the decision *logic* is authored; it is simulated sound and complete *before any code*, and then becomes the oracle the realised code is verified against — the hard problem-domain calls pinned upstream, then converted into the **mechanical-verification store**. The UI step is its symmetric twin, and what the symmetry cannot reach — *intent* — is treated as marked specification debt with a measured **intent-reliance rate**: the [residual](../core/02-completeness.md#the-residual-is-the-product), priced. The spec's §3.5 names its own encodability limit "the Polanyi floor," which is [core §3](../core/03-the-polanyi-floor.md) landing in a downstream tier under its own name.
- **Delivery** makes the ledger computable: features are graph partitions with *derived* footprints, "done" is a computed predicate (the [convergence states](../apparatus/02-entities.md#convergence-state) as a conformance requirement), version bumps are derivable from what the diff touched, direction is a computed gap to a declared target version, and generated artifacts carry the graph hash they were generated from so a **drift gate** can refuse a stale realisation — [drift detection](../apparatus/02-entities.md#audit) as a wire-checkable claim.
- **Data conformance** is the sensing boundary: a domain structure asserted continuously against production data, where a failure reads both ways — the data is wrong *or the spec has gone stale*. Production data as a witness that can indict the model is a [sensing action](../apparatus/02-entities.md#sensing-action) feeding the graph, and the **data-divergence rate** is a fitness function on spec honesty.
- **Authoring scopes** apply no-tacit-dependencies at intake: external tools (a Figma file, an event-modeling board) are bounded co-authors of the What, each with a declared scope, and a **completeness join** reports every required kind as covered, coverable-but-unauthored, or uncovered — the floor mapped, not hidden.
- At the **Build seam** it is a conformant *producer*: a **WorkUnit** is "a complete, executable SPMC package," frozen by value with a content-hash identity, carrying a sealed interior **cell-graph** whose cells each hold their own Schema and Prompt — the exercised [bundle](../apparatus/03-encoding-the-domain.md#the-bundle-context-made-deliverable) of this framework, serialized. The **VerdictEvent** that crosses back (accepted / rejected / escalate, with a declared next consequence) is the [interpretation](../apparatus/02-entities.md#interpretation) verdict on the wire. And its **coherence bar** — a split composition must hold "at least as well as a single unsplit author" — is the coherence audit this application named as its load-bearing risk, frozen as a conformance requirement.
- It claims Pillar One and producer conformance only; **no Pillar Two claim**. It stops at the seam it hands the WorkUnit across. That refusal is High Cohesion observed, not a gap.

## Promotion record

A `frozen-as` edge records **location, not evidence**: a frozen claim remains *projected* until a named system reports against it. This document derives from the DDD spec alone and depends on none of the artifacts below.

| Projection in this document | Frozen as | Status here |
|---|---|---|
| Specification and execution as independent peer concerns (the law's two principles, one per boundary) | `ai-development-foundations` · the Two Pillars; derivation contract / closure contract | projected |
| SPMC as the execution unit, binding pinned per axis | `ai-development-foundations` · Pillar One SPMC; RFC 0002 | projected |
| Cell-cluster handoff, producer-owned, gated by an independent verifier | `ai-development-contracts` · Build seam (WorkUnit / VerdictEvent), per RFC 0001; `product-framework` §5–§6 as producer | projected |
| Cell = one prompt, one artifact type | WorkUnit interior cell-graph: Schema and Prompt per cell. *Delta on freeze:* Model and Context pinned per unit, not per cell — the per-cell model binding of the funnel remains projected above the seam | projected |
| The coherence audit as the load-bearing check on decomposition | `product-framework` · the coherence bar ("at least as well as a single unsplit author") | projected |
| Ready/done as computed predicates | `product-framework` §7 · `feature_done` / `release_done` | projected |
| The Polanyi floor as declared, priced residue | `product-framework` · named-algorithm primitives (§3.5), intent-as-specification-debt, `annotation-needed` at the authoring boundary | projected |

Not yet frozen anywhere: **classify-and-dispatch at the task level** (recognition signatures, the known/unknown routing gate) and the **broad worker as explorer-and-typifier**. Those projections currently live only in this document, and their open questions below are still open.

**Reported-flip candidates.** `product-framework` ships runnable surfaces — the authoring-scope oracles (with `--self-test`), the checkout worked example doubling as its conformance demonstration, the behavioural-conformance wire protocol — and [product-cli](https://github.com/Hafeok/product-cli) already assembles bundles in `derived_from` order against the graph. Any of these, run and cited, flips the corresponding row. A flip is a separate commit citing the run; it is never bundled with a promotion edge.

## The costs this decomposition introduces

Real, and now partly owned by the ecosystem rather than merely predicted. Ordering is explicit — and it is just `derived_from`, declared once per TaskType and sealed into the WorkUnit's cell-graph. Cross-cell consistency, which one agent's shared context gave for free, is an explicit audit — the coherence bar above, still the thing to validate before trusting any decomposition. Emergent decisions cost a round-trip: the handler surfaces a problem the contract didn't anticipate, and instead of an inline fix it is `gap`/`unimplementable` feedback re-opening the upstream cell. Better for auditability, slower than inline — the standing argument for keeping the broad worker available as one node.

## Open questions specific to this application

- **Recognition is the soft spot, at two levels** — matching a task to a TaskType, and a feature to a feature-type-shaped decomposition. Signature by schema shape, embedding similarity, or an explicit requester-set field? Misclassification dispatches a confidently-wrong cluster, so the low-confidence escape hatch to the broad worker matters. Unfrozen; no landing artifact yet.
- **Task-type granularity.** Too many narrow types and recognition is hopeless; too few and clusters are vague. Likely coarse, parameterized types over proliferation.
- **The per-cell model binding.** The Build seam pins Model at the unit level. Whether the funnel's per-cell descent (contract on a strong reasoning model, handler on a small code model) needs per-cell bindings within one unit, or splits into multiple units, is a seam-design question the first reported runs should answer.
- **Decomposition quality is its own measurement.** A feature→task breakdown can be wrong independently of the tasks being right. The decomposer role needs measurement separate from cell-level quality.
- **The coherence bar's teeth** are the thing to validate before trusting any decomposition. Prototype it first.
