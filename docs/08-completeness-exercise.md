# The Completeness Exercise

> A specification is conformant when it is legal. It is complete when, exercised against its pinned SPMC binding, the residual is empty. This document defines the property, the exercise that verifies it, the ordinary practices that fail it today, and the normative definition of application status in terms of the exercise tiers.

**Status:** Proposed, normative track. By its own definitions this document is *projected* — Tier-1 evidence only. It becomes *reported* when a named system runs the exercise and the run is cited here. Candidate for promotion to the Specification Framework foundation once a second framework consumes it — the same route the two pillars themselves traveled (see § Genealogy).

---

## The gap this closes

The Specification Framework defines completeness criteria per section: every behavior has an unhappy path, every constraint has a measurable threshold, every How element traces to a What anchor. These criteria are static. They are checked by reading the spec.

A spec can satisfy every static criterion and still force the consuming model to invent. Schema-valid, derivation-clean, structurally coherent — and the model still guesses, because something the *consumer* needed was not in the bundle. Static criteria check the spec against the spec. Nothing checks the spec against the consumer.

Today that failure is detected downstream, as output-quality variance, as escalation to a larger model, as re-prompting until something sticks. By the funnel principle ([§1 Foundations](01-foundations.md#the-funnel-model-capability-tracks-constraint-density)), every one of those is upstream under-specification wearing a model-capability costume. There is no gate at the seam that catches it before execution. The Completeness Exercise is that gate.

Two properties, two checks:

| Property | Question | Check |
|---|---|---|
| **Conformance** | Is the artifact legal per its contract? | Conformance harness (schema + SHACL) |
| **Completeness** | Is the artifact sufficient for its declared consumer? | The Completeness Exercise |

Independent failure modes. Independent gates. Neither implies the other.

---

## Definition

Completeness is a relation, not a property:

> **complete(spec, binding)** — a specification is complete for a pinned SPMC binding when exercising the spec against that binding produces an empty residual.

There is no unparameterized "complete." A bundle can be complete for one Model-axis binding and open for another. This is not a weakness of the definition; it is the funnel principle in predicate form. Constraint density in the spec and required capability in the consumer trade off — completeness names the point where the spec has discharged every obligation the pinned consumer cannot.

The exercise unit is the cell's bundle: one prompt, one artifact type, assembled in `derived_from` order, with its own model binding ([§2 Entity Reference](02-entity-reference.md#prompt)). The binding is pinned per `ai-development-foundations` RFC 0002. One cell, one binding, one verdict. At the contracts seam the serialized form of the exercised bundle is the WorkUnit with its CapabilityManifest (`ai-development-contracts`, Build seam); this document uses the framework vocabulary and notes the seam mapping once, here.

Because the binding is pinned, the verdict is stable and cacheable: same spec, same binding, same result. When the binding changes — a model upgrade, a capability change — every cached completeness verdict against the old binding is void. Unpinned targets are why informal completeness claims decay silently.

### Why not "closure"

The Execution Contract already owns the word: its governing rule is the closure contract (every unit traced end to end, every grant traced to a need, every verdict with a declared consequence). Closure is an execution-pillar property about the *environment*. Completeness is a specification-pillar property about the *input*. The pillars are peers with independent vocabularies; this document keeps them independent.

---

## The exercise: three tiers

![The Completeness Exercise: a bundle (Schema, Prompt, Model, Context) is exercised against a pinned SPMC binding through three tiers — structural check, dry-run, sampled — producing a residual that is either empty (complete) or attributed per SPMC axis and fed back upstream](assets/completeness-exercise.svg)

The exercise runs in three tiers of increasing cost and increasing evidential strength. Each tier emits a **residual** — the set of obligations the spec left open. Empty residual at a tier passes that tier.

### Tier 1 — Structural check (static, decidable)

Walk the bundle as a graph. Every referent in the bound prompt resolves into the context pool. Every output declaration has its inputs bound. Every schema type referenced is defined. No dangling edges.

- **Proves:** every obligation the spec *names* is discharged.
- **Cannot prove:** that the spec names every obligation the consumer has.
- **Cost:** milliseconds. Harness-enforceable alongside conformance.
- **Residual form:** unresolved references, unbound inputs, undefined types.

### Tier 2 — Dry-run exercise (dynamic, effect-free)

Execute the bundle against the pinned binding with all effectors disabled — the Prospector posture: read-only capabilities, no committed side effects. Observe what the model does when it may look but not touch.

- **Proves:** the pinned consumer can produce schema-conformant output without requesting information outside the bundle.
- **Cannot prove:** that the output is *correct* — only that nothing was missing or invented on the way to producing it.
- **Cost:** one model call per exercise. Cheap enough to gate every seam crossing.
- **Residual form:** clarification requests, references to facts not in the context pool, capability requests outside the manifest.

### Tier 3 — Sampled exercise (dynamic, statistical)

Execute the bundle N times against the pinned binding, real or sandboxed effects, and measure the residual distribution. A spec that passes dry-run once and fails one run in five is not complete — it is complete-shaped.

- **Proves:** semantic sufficiency at the declared confidence. This is the only honest test of it; Tiers 1–2 cannot reach past the [Polanyi floor](09-the-polanyi-floor.md). Sampling is required because, in a fully pinned bundle, the model is the last stochastic component — the one element of the closed box that still has weather in it — which is also what makes residual variance attributable.
- **Cost:** N model calls plus verification. Certification-grade, not per-commit.
- **Residual form:** invention rate, escalation rate, verdict variance across runs.

Tier discipline: Tier 1 gates authoring. Tier 2 gates the seam. Tier 3 certifies before a bundle is trusted at Level 4+ autonomy, where no human inspects each output.

---

## Application status is defined by these tiers

This section is normative for the repository. Application documents carry a status; the status vocabulary is defined here, in tier terms. Two orthogonal axes; do not fuse them.

**Status — the evidence axis.**

- ***projected*** — Tier-1 evidence only: the derivation is clean, no dangling edges. A design.
- ***reported*** — Tier-2 or Tier-3 evidence from a named system: the exercise was run, the residual recorded, the run cited. A reported claim without a citation is a projected claim wearing the wrong label.

Frozen records — RFCs, contracts — are derivations, not runs. Freezing a projection into a foundation RFC never changes its status.

**Promotion — the location axis.**

A projection may be frozen into a more stable tier of the ecosystem. This is recorded as a **`frozen-as` edge**: projection → landing artifact. The edge records genealogy — where the claim now lives — not evidence. Dependency remains downward: the authoring document never depends on the artifacts its projections landed in. There is no third status value; "promoted" is an edge, not a state.

---

## The residual

The residual is the useful artifact — the exercise exists to produce it. A non-empty residual is not a rejection; it is a work order against the specification pillar.

Every residual entry attributes to exactly one SPMC axis, reusing the Specification Framework's existing diagnostic table:

| Residual signal | Open axis |
|---|---|
| Output shape wrong or underdetermined | Schema |
| Model asked what to do, or did the wrong thing confidently | Prompt |
| Correct bundle, inconsistent reasoning across samples | Model (floor too low — or spec not decomposed far enough) |
| Model invented facts, or requested information mid-run | Context |

Structurally, an exercise verdict is a VerdictEvent pointed upstream — at the specification pillar instead of at the output (`ai-development-contracts`). The residual re-enters as input to a fresh forward chain. Feedback does not invert the funnel; the funnel composes with itself.

---

## Why ordinary practice fails the exercise

Every case below is standard, everyday LLM-assisted development. Each one fails a specific tier with a specific open axis. This is the diagnostic value of the concept: "that doesn't work reliably" becomes "that is open on these axes, detectable at this tier."

### Case 1 — Single prompt to a coding CLI, output taken on faith

`claude "add rate limiting to the API"` — or any coding CLI, any one-shot prompt. No schema: the output shape is whatever the model felt like. No pinned model: the same prompt against next month's default binding is a different system. No frozen context: the CLI retrieved whatever it retrieved. No verification: the human eyeballs a diff, or worse, doesn't.

**Open axes: all four.** Fails Tier 1 — there is no bundle to walk; the referents ("the API", "rate limiting" per whose policy?) resolve into nothing. This is the degenerate case: not an incomplete spec but the absence of one. Explorer-mode tools operate here permanently — which is precisely why exploration output may enter engineered mode only through a frozen discovery record, never directly.

### Case 2 — "Fix this bug" with a pasted stack trace

The trace names frames the model cannot see. The model reconstructs the surrounding code from its training distribution — confidently, plausibly, and against a codebase that does not exist.

**Open axis: Context.** Caught at Tier 2: the dry-run either requests the missing files or fabricates their contents, and fabrication is a residual entry. Today this failure is invisible until the patch doesn't apply.

### Case 3 — House conventions live in heads, not in the bundle

"Write the endpoint handler." The team has error-handling conventions, a naming scheme, a logging discipline, a house style for validation. None of it is in the bundle. The model supplies its own — coherent, defensible, and wrong for this codebase. Review catches it, sometimes, at review cost, every time.

**Open axis: Context** (the conventions are decided but not transmitted) shading into **Prompt** (the obligation to follow them is never stated). Tier 3 exposes it as cross-sample variance: five runs, five internally consistent, mutually incompatible convention sets.

### Case 4 — The silent model upgrade

Prompts tuned for months against one model. The provider ships a new default, or a teammate switches the CLI binding. Half the prompts degrade — no code changed, no spec changed, and nothing detected anything, because the completeness claim was never parameterized on a binding.

**Open axis: Model — specifically, unpinned.** This is `ai-development-foundations` RFC 0002's argument restated as a detection problem: without a pinned binding there is no stable target to exercise against, so completeness cannot even be *claimed*, only felt. Caught by re-running Tier 2/3 on binding change — which requires the binding to be a declared, versioned thing.

### Case 5 — "Make it production-ready"

An unbounded predicate. Production-ready per which checklist? The model picks a plausible basket — some logging, a try/except, maybe a Dockerfile — and the human accepts whatever subset looks busy.

**Open axis: Prompt.** No acceptance criteria means no dischargeable obligation, which means the residual is not even well-defined. Fails Tier 1 the moment the prompt's obligations are required to bind to declared output criteria: they bind to nothing.

### Case 6 — Verification by eyeball, at scale

Model output pasted from a chat window into the IDE, "looks right," committed. The only verifier is the same human whose attention the tool was adopted to save — and attention is exactly what does not scale. When the model also generates the tests, verification becomes circular: the output grades itself.

**Open axis: Schema** (no declared shape to verify against) — and past the seam, an execution-pillar failure: no declared verification, no Jidoka. This case is where the two pillars visibly meet: the exercise can prove the spec is complete, and the environment must still refuse to trust unverified output.

### Case 7 — Works in the demo, dies on real data

The prompt was exercised — once, informally, on the friendly example. Real inputs hit the unhappy paths the spec never declared, and the model improvises a policy per run: skip the row, null the field, halt, guess.

**Open axes: Prompt and Context** (undeclared unhappy paths — the What-spec's own completeness criterion, unenforced). A Tier-2 pass on one input proved nothing about the input distribution; only Tier 3 samples it. One dry-run is an anecdote.

### Case 8 — The retry slot machine

The prompt fails, the human re-rolls, the third output looks good, ship it. Re-rolling *is* sampled exercise — run informally, unmeasured, with the residual discarded instead of recorded. The signal was there: a spec needing three pulls has a measurable invention or variance rate that Tier 3 would have quantified and attributed to an axis. Instead the evidence is thrown away and the same slot machine is played tomorrow.

**Open axis: whichever one the discarded residual would have named.** The practice is not wrong because sampling is wrong; it is wrong because the sample is not treated as a measurement.

The pattern across all eight: today's tooling makes execution effortless and completeness invisible. Every case is a residual that existed before the run and was discovered after it — or never. The exercise moves discovery to the seam.

---

## Genealogy

The two-pillar split — specification and execution as independent foundations — was precipitated by working the SDLC through the decision-first lens ([applications/sdlc.md](../applications/sdlc.md)). That derivation is *projected* by this document's own definitions: clean, not yet reported by a running system. The route it traveled is the promotion mechanism this document now formalizes: exercised at the framework tier, frozen downward into `ai-development-foundations` as RFCs, with the framework thereafter depending on what it authored. Authorship is directional; dependency is downward (RFC 0001). This document follows the same route and claims no more evidence than its status line grants.

---

## Placement in the stack

- The **Specification Framework** (foundation) owns the static completeness criteria and the SPMC attribution table. This document adds nothing to the foundation yet; it consumes both.
- **Decision-Driven Design** (this framework) defines the exercise, its tiers, the residual as a first-class recorded artifact — a decision-shaped record, kind as data, entering the graph like any other — and the application-status vocabulary above.
- The **contracts tier** (`ai-development-contracts`) is where the residual schema would land if a second consumer appears: a residual is structurally a VerdictEvent variant pointed at the specification pillar, and should be specified as such rather than as a new contract.
- The **Execution Contract** is untouched. Closure remains its word. The exercise's Tier 2 borrows the execution pillar's read-only posture (Prospector) but claims none of its vocabulary.

## Open questions

1. Tier 3 sample size and confidence thresholds per autonomy level — is N declared in the CapabilityManifest, the bundle, or the transition contract?
2. Whether a Tier-2 pass should be a hard gate on the Build seam (bundle rejected at dispatch) or an advisory verdict at first.
3. Residual record schema: VerdictEvent variant vs. dedicated contract. Default position: variant, per the seam pattern (`ai-development-foundations` RFC 0004) — new domains add seams, not pillars, and this is not even a new domain.
