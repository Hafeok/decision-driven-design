# Completeness: Measuring the Allocation

> **Core §2 — normative track.** The [law](01-the-law.md) says the specification demand is constant and allocated across four stores. This document is the instrument that *reads* that allocation. A specification is **conformant** when it is legal; it is **complete** when, exercised against its pinned binding, the residual is empty. Everything not encoded shows up here, priced.

**Status:** Proposed, normative track. By its own definitions this document is *projected* — Tier-1 evidence only. It becomes *reported* when a named system runs the exercise and the run is cited here. Candidate for promotion to the Specification Framework foundation once a second framework consumes it — the same route the two pillars themselves traveled (see § Genealogy).

## The gap this closes

A specification can satisfy every static criterion — schema-valid, derivation-clean, structurally coherent — and still force the consuming actor to invent, because something the *consumer* needed was not in the input. Static criteria check the spec against the spec. Nothing static checks the spec against the consumer.

Today that failure is detected downstream: as output-quality variance, as escalation to a larger model, as re-prompting until something sticks. By the [funnel principle](04-projections.md#the-funnel-allocation-over-position) every one of those is upstream under-specification wearing a model-capability costume. There is no gate at the seam that catches it *before* execution. The Completeness Exercise is that gate.

Two properties, two independent checks:

| Property | Question | Check |
|---|---|---|
| **Conformance** | Is the artifact legal per its contract? | Conformance harness (schema + shape constraints) |
| **Completeness** | Is the artifact sufficient for its declared consumer? | The Completeness Exercise |

Independent failure modes. Independent gates. Neither implies the other.

## Definition

Completeness is a relation, not a property:

> **complete(spec, binding)** — a specification is complete for a pinned binding when exercising the spec against that binding produces an empty residual.

There is no unparameterized "complete." A specification can be complete for one consumer and open for another — one model binding versus the next, a senior versus a junior human. This is not a weakness of the definition; it is the funnel principle in predicate form. Constraint density in the spec and required capability in the consumer trade off — completeness names the point where the spec has discharged every obligation the pinned consumer cannot.

The binding must be **pinned**: a specific version of each of the four axes output quality rides on — **Schema** (the target shape), **Prompt** (the execution guidance), **Model**, and **Context** (the assembled input). The tuple is Specification Framework vocabulary (SPMC); the binding is pinned per `ai-development-foundations` RFC 0002. The exercise unit is one cell's bundle: one prompt, one artifact type, assembled in dependency order, with its own model binding — one cell, one binding, one verdict. At the contracts seam the serialized form of the exercised bundle is the WorkUnit with its CapabilityManifest (`ai-development-contracts`, Build seam); this document uses the framework vocabulary and notes the seam mapping once, here. Because the binding is pinned, the verdict is stable and cacheable — same spec, same binding, same result. When the binding changes — a model upgrade, a capability change — every cached completeness verdict against the old binding is void. Unpinned targets are exactly why informal completeness claims decay silently: there is no stable thing to have been complete *for*.

### Why not "closure"

The Execution Contract already owns the word: its governing rule is the closure contract (every unit traced end to end, every grant traced to a need, every verdict with a declared consequence). Closure is an execution-pillar property about the *environment*. Completeness is a specification-pillar property about the *input*. The pillars are peers with independent vocabularies; this document keeps them independent.

## The exercise: three tiers

![The Completeness Exercise: a bundle (Schema, Prompt, Model, Context) is exercised against a pinned binding through three tiers — structural check, dry-run, sampled — producing a residual that is either empty (complete) or attributed per axis and fed back upstream.](assets/completeness-exercise.svg)

The exercise runs in three tiers of increasing cost and increasing evidential strength. Each tier emits a **residual** — the set of obligations the spec left open. An empty residual at a tier passes that tier.

### Tier 1 — Structural check *(static, decidable)*

Walk the input as a graph. Every referent in the bound prompt resolves into the context. Every output declaration has its inputs bound. Every schema type referenced is defined. No dangling edges.

- **Proves:** every obligation the spec *names* is discharged.
- **Cannot prove:** that the spec names every obligation the consumer has.
- **Cost:** milliseconds. Enforceable in the harness alongside conformance.
- **Residual form:** unresolved references, unbound inputs, undefined types.

### Tier 2 — Dry-run exercise *(dynamic, effect-free)*

Execute the input against the pinned binding with all effectors disabled — the Prospector posture: read-only capabilities, no committed side effects. Observe what the model does when it may look but not touch.

- **Proves:** the pinned consumer can produce conformant output without requesting information outside the input.
- **Cannot prove:** that the output is *correct* — only that nothing was missing or invented on the way to producing it.
- **Cost:** one model call per exercise. Cheap enough to gate every seam crossing.
- **Residual form:** clarification requests, references to facts not in the context, capability requests outside the declared scope.

### Tier 3 — Sampled exercise *(dynamic, statistical)*

Execute the input N times against the pinned binding, with real or sandboxed effects, and measure the residual distribution. A spec that passes dry-run once and fails one run in five is not complete — it is complete-*shaped*.

- **Proves:** semantic sufficiency at the declared confidence. This is the only honest test of it; Tiers 1–2 cannot reach past the [Polanyi Floor](03-the-polanyi-floor.md). Sampling is required because, in a fully pinned input, the model is the last stochastic component — the one element of the closed box that still has weather in it — which is also what makes residual variance attributable.
- **Cost:** N model calls plus verification. Certification-grade, not per-commit.
- **Residual form:** invention rate, escalation rate, verdict variance across runs.

Tier discipline: **Tier 1 gates authoring. Tier 2 gates the seam. Tier 3 certifies** before a specification is trusted at high autonomy, where no human inspects each output.

## The residual is the product

The residual is the useful artifact — the exercise exists to produce it. A non-empty residual is not a rejection; it is a **work order** against the specification. Every residual entry attributes to exactly one SPMC axis, reusing the Specification Framework's existing diagnostic table:

| Residual signal | Open axis |
|---|---|
| Output shape wrong or underdetermined | Schema |
| Model asked what to do, or did the wrong thing confidently | Prompt |
| Correct input, inconsistent reasoning across samples | Model (floor too low — or spec not decomposed far enough) |
| Model invented facts, or requested information mid-run | Context |

The residual re-enters as *input* to a fresh forward chain — it does not travel the funnel backwards. Feedback does not invert the funnel; the funnel [composes with itself](04-projections.md#the-funnel-allocation-over-position).

## Why ordinary practice fails the exercise

Every case below is standard, everyday LLM-assisted development. Each fails a specific tier with a specific open axis. That is the diagnostic value of the concept: "that doesn't work reliably" becomes "that is open on these axes, detectable at this tier."

**Case 1 — Single prompt to a coding CLI, output taken on faith.** `add rate limiting to the API`, one shot. No schema, no pinned model, no frozen context, no verification. **Open axes: all four.** Fails Tier 1 — there is no input to walk; the referents ("the API", "rate limiting" per whose policy?) resolve into nothing. This is the degenerate case: not an incomplete spec but the absence of one. Exploration tools operate here permanently — which is precisely why exploration output may enter engineered mode only through a frozen discovery record, never directly.

**Case 2 — "Fix this bug" with a pasted stack trace.** The trace names frames the model cannot see; it reconstructs the surrounding code from its training distribution, confidently, against a codebase that does not exist. **Open axis: Context.** Caught at Tier 2: the dry-run either requests the missing files or fabricates them, and fabrication is a residual entry.

**Case 3 — House conventions live in heads, not in the input.** "Write the endpoint handler." Error-handling conventions, naming scheme, logging discipline — none in the input. The model supplies its own: coherent, defensible, wrong for this codebase. **Open axis: Context** shading into **Prompt** (the obligation to follow them is never stated). Tier 3 exposes it as cross-sample variance: five runs, five internally consistent, mutually incompatible convention sets.

**Case 4 — The silent model upgrade.** Prompts tuned for months against one model; the provider ships a new default, or a teammate switches the binding. Half the prompts degrade — no code changed, nothing detected it, because the completeness claim was never parameterized on a binding. **Open axis: Model — specifically, unpinned.** This is `ai-development-foundations` RFC 0002's argument restated as a detection problem: without a pinned binding there is no stable target to exercise against, so completeness cannot even be *claimed*, only felt. Caught by re-running Tier 2/3 on binding change — which requires the binding to be a declared, versioned thing.

**Case 5 — "Make it production-ready."** An unbounded predicate. The model picks a plausible basket and the human accepts whatever subset looks busy. **Open axis: Prompt.** No acceptance criteria means no dischargeable obligation, so the residual is not even well-defined. Fails Tier 1 the moment obligations are required to bind to declared output criteria.

**Case 6 — Verification by eyeball, at scale.** Output pasted from a chat window, "looks right," committed. The only verifier is the same human whose attention the tool was adopted to save. When the model also generates the tests, verification becomes circular: the output grades itself. **Open axis: Schema** (no declared shape to verify against) — and past the seam, an output-boundary failure: no declared verification. This is where the two principles visibly meet — the exercise can prove the spec complete, and the environment must *still* refuse to trust unverified output.

**Case 7 — Works in the demo, dies on real data.** The prompt was exercised once, informally, on the friendly example. Real inputs hit unhappy paths the spec never declared, and the model improvises a policy per run. **Open axes: Prompt and Context** (undeclared unhappy paths). A Tier-2 pass on one input proved nothing about the input distribution; only Tier 3 samples it.

**Case 8 — The retry slot machine.** The prompt fails, the human re-rolls, the third output looks good, ship it. Re-rolling *is* sampled exercise — run informally, unmeasured, residual discarded. A spec needing three pulls has a measurable invention or variance rate that Tier 3 would have quantified and attributed. **Open axis: whichever one the discarded residual would have named.** The practice is not wrong because sampling is wrong; it is wrong because the sample is not treated as a measurement.

The pattern across all eight: today's tooling makes execution effortless and completeness invisible. Every case is a residual that existed before the run and was discovered after it — or never. The exercise moves discovery to the seam.

## Application status is defined by these tiers

When an [application](../applications/) document makes a claim, its evidential status is defined here, in tier terms. Two orthogonal axes; fusing them is an error.

**Status — the evidence axis.**

- **projected** — Tier-1 evidence only: the derivation is clean, no dangling edges. A design.
- **reported** — Tier-2 or Tier-3 evidence from a named system: the exercise was run, the residual recorded, the run cited. A reported claim without a citation is a projected claim wearing the wrong label.

Frozen records — RFCs, contracts — are derivations, not runs. Freezing a projection never changes its status.

**Promotion — the location axis.** A projection frozen into a more stable tier is recorded as a `frozen-as` edge: projection → landing artifact. The edge records genealogy — where the claim now lives — not evidence, and adds no dependency: the authoring document never depends on the artifacts its projections landed in. There is no third status value; "promoted" is an edge, not a state.

---

## Genealogy

The two-pillar split — specification and execution as independent foundations — was precipitated by working the SDLC through the decision-first lens ([applications/sdlc.md](../applications/sdlc.md)). That derivation is *projected* by this document's own definitions: clean, not yet reported by a running system. The route it traveled is the promotion mechanism this document formalizes: exercised at the framework tier, frozen downward into `ai-development-foundations` as RFCs, with the framework thereafter depending on what it authored. Authorship is directional; dependency is downward (RFC 0001). This document follows the same route and claims no more evidence than its status line grants.

## Placement in the stack

- The **Specification Framework** (foundation) owns the static completeness criteria and the SPMC attribution table. This document adds nothing to the foundation yet; it consumes both.
- **Decision-Driven Design** (`core/`) defines the exercise, its tiers, the residual as a first-class recorded artifact — a decision-shaped record, kind as data, entering the graph like any other — and the application-status vocabulary above.
- The **contracts tier** (`ai-development-contracts`) is where the residual schema would land if a second consumer appears: a residual is structurally a VerdictEvent variant pointed at the specification pillar, and should be specified as such rather than as a new contract.
- The **Execution Contract** is untouched. Closure remains its word. The exercise's Tier 2 borrows the execution pillar's read-only posture (Prospector) but claims none of its vocabulary.

## Open questions

1. Tier 3 sample size and confidence thresholds per autonomy level — is N declared in the CapabilityManifest, the bundle, or the transition contract?
2. Whether a Tier-2 pass should be a hard gate on the Build seam (bundle rejected at dispatch) or an advisory verdict at first.
3. Residual record schema: VerdictEvent variant vs. dedicated contract. Default position: variant, per the seam pattern (`ai-development-foundations` RFC 0004) — new domains add seams, not pillars, and this is not even a new domain.
