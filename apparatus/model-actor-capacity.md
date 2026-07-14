# Model-Actor Capacity: The Active/Total Decomposition

> apparatus note — projected. Derives a second capacity bound for the model actor
> from the law, splitting the single "context window" budget into two stores that
> current architectures (dense vs MoE) allocate independently. Predicts a measurable
> escape-class split. Not yet exercised.

---

## Cross-references

Drop-in stubs for the three documents this note hangs off. Directional: this note
*depends on* all three; none of them depend on it (it is projected apparatus material,
they are established). The first two are applied in place ([the actor's capacity](../core/context-window.md),
[encoding §intent mode](03-encoding-the-domain.md)); the third awaits integration in decision-cli.

**Into the context-length result** (core, the model-actor allocation-budget section) —
append after the "context length bounds action size" theorem:

> The window is a single budget, but it resolves into two independently-bound stores once
> the actor's architecture is pinned: reach (total parameters) and resolution (active
> parameters). See [Model-Actor Capacity](../apparatus/model-actor-capacity.md) for the
> decomposition and its escape-split prediction.

**Into `apparatus/03-encoding-the-domain.md`** (intent mode / maneuvering room) — append to
the landscape bullet, after "judgment is window-resident, and the window is the search's
working set":

> The working set has two capacities, not one: total parameters bound how much of the
> landscape the actor *knows* (reach), active parameters bound how much decision work one
> search step performs (resolution). An MoE buys a wide landscape cheaply; a dense model
> buys deep per-step search. See [Model-Actor Capacity](model-actor-capacity.md).

**Into the SPMC Model axis** (spec-framework / decision-cli `02-entity-reference.md`) —
append to the architecture field description, after the dense/MoE active-versus-total split
is introduced:

> The split is not bookkeeping. Total parameters bound the reach of the judgment store;
> active parameters bound its per-pass resolution. The two are independently sized by the
> task's demand shape — see [Model-Actor Capacity](../../decision-driven-design/apparatus/model-actor-capacity.md)
> — which is what makes the architecture field a capability determinant, not a label.
> *(Fix the relative path to the actual cross-repo location at integration.)*

---

## Where this sits

Two prior results are assumed:

1. **Context length is the model actor's allocation budget** (see the context-length
   note). For a single action, every window-resident store's share — encoded
   specification transmitted in, facts sensed at fire time, and the working room in
   which per-run judgment happens — competes for one space. The window is *capacity*,
   not speed or quality.

2. **The SPMC Model axis pins architecture** — dense or MoE, with the active-versus-total
   parameter split recorded as part of the model binding, not just a name.

This note connects them. The context-length result treats the model as a single
budget of size *W*. But the SPMC Model axis already records that two models with the
same *W* can differ in a way that matters: one dense, one sparse. The claim here is
that the dense/MoE split is not an efficiency footnote — it names a **second capacity
bound**, orthogonal to the window, that the law was already quantifying over without
a place to put it.

---

## The single budget was hiding two

The window bounds *how much determination demand can be present at fire time* — the
mass of stores that must physically co-reside. But being present is not being
processed. A decision that is resident in the window still has to be *made*, and
for a model actor the act of making it is computation over the resident material.

Two distinct things are therefore bounded, and dense architectures fuse them:

- **Reach** — how much stored knowledge the judgment store can draw on to make a
  decision. Bounded by **total** parameters. This is the breadth the actor can bring
  to bear: what it knows, across how many domains, as unencoded substrate available
  for inspection.

- **Resolution** — how much unencoded decision work a single forward pass can perform
  before the decision escapes. Bounded by **active** parameters. This is the depth of
  per-token judgment: the width available to sense facts, hold intermediate decisions,
  and steer toward intent, *for one step of one action*.

A dense model sets reach = resolution; every parameter is active, so stored capacity
and per-token compute are the same number. An MoE unbinds them: total parameters buy
reach, active parameters buy resolution, and the two can be scaled independently.

This is why the earlier "reach for a large model in explore mode" result was slightly
underspecified. Explore mode is judgment-heavy, and judgment is window-resident — true.
But *which* dimension of the model must grow depends on **what the judgment is bottlenecked
on**. Breadth-bound judgment (recall across many domains, heterogeneous inputs) wants
total parameters. Depth-bound judgment (tight multi-step reasoning where each step needs
full-width compute) wants active parameters. "A bigger model" conflates these; the
active/total split resolves them.

---

## The prediction: escape splits along the axis

The law's escape store is the decision decided by nobody — defect exposure, surfaced as
output. The escape taxonomy already distinguishes two classes: **escape-hallucination**
(reducible by allocation) and **wind-hallucination** (irreducible actor residual variance).

The decomposition above predicts that *escape-hallucination itself splits along the
active/total axis*, and that the split is architecturally legible:

> **Reach-bound escape** occurs when the governing decision required knowledge the actor
> could not reach — its total capacity was exhausted. Reducible by adding reach (total
> parameters) or by encoding the missing knowledge into the transmitted specification.
>
> **Resolution-bound escape** occurs when the knowledge was reachable but a single forward
> pass could not do the decision work — per-token active budget was exhausted. Reducible
> by adding resolution (active parameters) or by decomposing the action so each step's
> judgment fits one pass.

The testable consequence, at **equal serving cost**:

- An MoE (high total, low active) should show **lower reach-bound escape** and **higher
  resolution-bound escape** than a dense model of the same active-parameter class.
- A dense model should show the mirror image.
- The crossover is a function of task shape: recall-and-breadth tasks favor the MoE;
  decision-dense reasoning chains favor the dense model.

This is not what the scaling-law literature measures. Those results are denominated in
*loss over facts-as-substrate*; this is denominated in *governing decisions that escaped
under a declared assurance level*. Loss says nothing about who was accountable for a
decision or whether it was decided at all. The prediction here is a statement about the
escape store, and it is only visible if escape is attributed by cause, not aggregated.

---

## Why this matters if it holds

The through-line the law has been driving toward: **determination demand is fixed by the
task, and the only choice is store allocation.** For a model actor, "which model" has so
far been an experience-driven guess. If the active/total decomposition holds against
evidence, the guess becomes a derivation:

Given a task's governing decision set and its assurance level, and given the shape of the
demand — how much of it is reach (breadth of knowledge the decisions require) versus
resolution (depth of per-step decision work) — the required model is the one whose total
parameters cover the reach demand and whose active parameters cover the resolution demand,
at the window capacity that holds the whole action.

That is a computed model requirement, not a benchmark lookup. It is the model-selection
analogue of the funnel: as demand shape is characterized, the actor requirement falls out
of the allocation, rather than being chosen and then justified. The escape-split campaign
is the falsification test standing between the projection and that claim.

---

## Evidence: E-campaign observable

Pre-declared observable for the E1–E4 campaign against product-cli. This overlaps E2–E3
(attributed residual, convergence cycle) — it is an attribution refinement, not a new run.

**The pairing problem.** The test requires two bindings that differ in the active/total
split and in *nothing else that moves capability*. This rules out the obvious in-stack
pairing: Qwen3.6-35B-A3B (3B active) against Qwen3.6-27B-FP8 dense (~27B active) is **not**
a matched-active test — the dense model has roughly 9× the active budget, so any escape
difference is dominated by the active-parameter gap, not the architecture. That pairing
measures *resolution*, not the dense/MoE unbinding. It is a useful second run, but it is
not the falsification test.

The falsification test needs **matched active parameters, differing total** — hold
resolution fixed, vary reach. It also wants the two bindings to share training corpus,
tokenizer, and instruction tuning, or the confound moves off-architecture. That points to
one family:

| Role | Binding | Active | Total | Serves on |
|---|---|---|---|---|
| Dense (reach = resolution) | `Qwen3-4B` (dense) | ~4B | ~4B | single GPU, vLLM |
| MoE (reach ≫ resolution) | `Qwen3-30B-A3B` | ~3B | ~30B | single GPU, vLLM |

Same family, same tokenizer, same Apache-2.0 lineage; the dense 4B and the A3B sit at the
same active-parameter class (~3–4B) while the MoE carries ~10× the total. The residual
active-parameter mismatch (4B vs 3B) is small and runs *against* the prediction — it
slightly favors the dense model on resolution — so a resolution-bound-escape win for the
MoE would be conservative. FP8 checkpoints exist for both; pin quantization identically in
the SPMC Model binding so precision is not a free variable.

The published concurrency-cost study (arXiv 2606.11690) already ran the cross-family
analogue — Llama 3.1 8B dense vs Qwen3-30B-A3B on one H100 — establishing that both serve
in the same cost regime. That result stands as external corroboration of the serving
symmetry; the in-family Qwen3-4B / 30B-A3B pairing is preferred here because it removes the
cross-family capability confound.

**Setup.** The two bindings above run the same exercise set spanning two task shapes:
- **Breadth shape** — decisions requiring recall across many domains, shallow per-step.
- **Depth shape** — decisions requiring multi-step reasoning, narrow domain, deep per-step.

**Attribution.** Each escaped decision is classified reach-bound vs resolution-bound by the
reducibility test: does adding transmitted knowledge (encoding into context) close it
[reach-bound], or does decomposing the action into smaller per-pass steps close it
[resolution-bound]?

**Kill condition (pre-declared).** The prediction is falsified if the MoE and dense bindings
show **no significant difference** in the reach-bound / resolution-bound escape ratio across
the two task shapes — i.e. if escape class is independent of architecture at matched active
class. Use TOST against a pre-declared equivalence margin on the ratio; if the two
architectures fall inside the equivalence band, the decomposition adds no predictive content
over the single-budget model and is retracted.

**No-silent-residual check.** Every escaped decision must land in exactly one of
{reach-bound, resolution-bound, wind-class}; an unclassifiable escape is itself a finding —
it means the reducibility test is underspecified, not that the decision escaped for a third
reason.

**Second run (in-stack, resolution axis).** Separately from the falsification test, the
production stack's own pairing — Qwen3.6-35B-A3B (3B active) vs Qwen3.6-27B-FP8 dense
(~27B active) — isolates the *resolution* axis at roughly fixed reach-order. Prediction:
resolution-bound escape falls sharply from the A3B to the 27B dense on depth-shape tasks,
while reach-bound escape moves little. This is not the architecture test — it is the
active-parameter test — but it validates the resolution half of the decomposition on the
hardware customers actually see, and the two runs together separate the two bounds cleanly:
the 4B/30B-A3B pair varies total at fixed active; the A3B/27B-dense pair varies active at
high total. Neither alone identifies both bounds; the pair of runs does.

---

## Status

**Projected.** Clean derivation from the context-length result and the SPMC Model axis;
not yet exercised. Promotes to **reported** only when the escape-split campaign runs with
the kill condition live and the ratio difference (or its absence) is attributed against the
pre-declared margin.
