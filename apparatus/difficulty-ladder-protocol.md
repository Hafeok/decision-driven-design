# Difficulty-Ladder Protocol and Sub-Step Verification

> apparatus note — campaign instrument, second stage. Turns the twelve seed decisions into
> laddered families whose escape rates land in a measurable band, and specifies the
> sub-step verification that makes depth-shape attribution valid. Without this, escape
> rates floor or ceiling (testifying to nothing) and depth escapes cannot be distinguished
> from reach escapes. Feeds E2–E3 / F1–F4. Projected instrument.

---

## Two failure modes this closes

The seed corpus is capacity-selective but not yet *calibrated*, and one of its shapes is not
yet *attributable*. Two separate problems:

1. **Uncalibrated difficulty → uninformative escape rate.** A seed that never escapes (0%)
   and a seed that always escapes (100%) both testify to nothing about the split — the first
   says the capacity wasn't loaded, the second says it was swamped past the point where
   attribution means anything. The signal lives in the middle band, where the binding's
   capacity is the *marginal* constraint. Each seed must be laddered until it lands there.

2. **Unverified depth-shape reach → attribution collapse.** A depth-shape decision only
   isolates resolution *if the actor actually knows every sub-step*. If it silently doesn't,
   an escape attributed to resolution ("couldn't hold the chain") is really reach ("didn't
   know step 4") — and the reducibility test misclassifies it, because decomposition happens
   to also surface the missing knowledge. Depth attribution is invalid until reach is proven
   present.

---

## Part 1 — The difficulty ladder

### The dial is shape-specific

Each shape has exactly one difficulty dial, and it is the *selective* dimension — the one
that loads the target capacity. Turning any other knob would contaminate the isolation.

- **Breadth-shape dial: span width.** Number of distinct domains / entities / foreign schemas
  the decision must reach across. Rungs add domains, holding per-fact depth flat. More rungs =
  more total-parameter reach demanded.
- **Depth-shape dial: chain length.** Number of dependent steps in the derivation. Rungs add
  hops / constraints / operations, holding per-step knowledge flat and single-domain. More
  rungs = more active-parameter resolution demanded per pass.

Turning the breadth dial must not deepen any step; turning the depth dial must not widen the
domain. If a ladder rung changes both, the rung is malformed — it has stopped being a pure
difficulty increase and become a shape change.

### The banding procedure

For each seed, per binding, find the rung where escape rate lands in the **measurable band**.

- **Band definition:** escape rate in **[20%, 80%]** across a fixed run count (start n=20 per
  rung; raise if the confidence interval on the rate is too wide to place it in-band). The
  band is where the binding's capacity is marginal — small changes in load move the rate, so
  the rate *carries information* about the capacity.
- **Ascend:** start at the seed's baseline rung. If escape < 20%, add one unit on the shape's
  dial (one domain / one hop) and re-run. Repeat until the rate enters the band or exceeds it.
- **Overshoot handling:** if a rung jumps from < 20% to > 80% with no in-band rung between,
  the dial granularity is too coarse — subdivide (add half-steps: for breadth, a partially-
  specified extra domain; for depth, a step that reuses a prior result rather than a fully
  new hop) until an in-band rung exists.
- **Per-binding ladders differ, and that is the point.** The 30B-A3B and the 4B dense will
  land in-band at *different rungs* — the MoE tolerates wider breadth ladders before escaping
  (more reach), the dense model tolerates deeper depth ladders (more resolution per pass). The
  rung offset between bindings is itself a measurement: **the horizontal distance between two
  bindings' in-band rungs on a given shape's ladder is a direct read of their capacity gap on
  that axis.** Record it; it is a second, continuous corroboration of the escape-ratio split,
  independent of the reducibility A/B.

### What the ladder produces per seed

A small table per seed × binding: the in-band rung, the escape rate at that rung with CI, and
the rung offset against the other bindings. Twelve seeds × four bindings, each banded, is the
E2 substrate. The prediction is legible two ways from this table: escape *ratio* (reducibility
A/B, per the capacity note) and rung *offset* (the ladder). Agreement between the two is the
campaign's internal consistency check — if the reducibility A/B says MoE is reach-strong but
the ladder says the MoE escapes at shallow breadth rungs, something in the instrument is
wrong, not the model.

---

## Part 2 — Sub-step verification (depth-shape only)

Depth attribution is invalid until every sub-step's knowledge is proven resident in the
binding. This is a gate that runs *before* the depth seed is admitted to the ladder, per
binding.

### The isolation probe

For a depth seed with steps s₁…sₙ, before running the full chain:

1. **Decompose to atoms.** Break the decision into its n dependent steps, each a standalone
   micro-decision (this decomposition already exists — it is the resolution-bound closing
   intervention; here it is reused as a probe).
2. **Present each atom in isolation**, with the output of its predecessor *supplied as a given*
   (not derived — supplied, so the step tests only its own knowledge, not the chain). Run each
   atom at n=20.
3. **Pass criterion:** every atom must clear a high isolated-success bar (pre-declare — e.g.
   ≥ 95%). An atom below the bar means the binding does not reliably know that step, so the
   seed is **not reach-clean** for this binding.

### Verdict handling

- **All atoms pass → depth seed admitted.** Reach is proven present; any full-chain escape is
  now validly attributable to resolution, because every step's knowledge was independently
  confirmed. The chain escapes only because the *chain* exceeds one pass, not because a step
  was unknown.
- **An atom fails → seed rejected for this binding, and the failure is recorded, not
  discarded.** A failed atom is a *reach* finding hiding in a depth seed — it says this
  binding lacks that specific knowledge. It moves to the breadth column as evidence (the
  binding's reach gave out on that atom) and the depth seed is either dropped for this binding
  or repaired by transmitting that atom's knowledge into every rung's bundle (converting the
  unknown step into a supplied fact, restoring reach-cleanliness).

### Why "supplied predecessor" is load-bearing

If step sₖ were run with its predecessor's output *derived in-context* rather than supplied,
a failure at sₖ could be sₖ's own ignorance *or* contamination from a slip at sₖ₋₁ — the two
reconflate exactly the way the whole procedure is trying to prevent. Supplying each
predecessor as a given breaks the chain into genuinely independent knowledge tests. The full
chain is run *once, separately*, as the actual depth trial; the atom probes are only the
admission gate.

---

## Sequencing

Per binding, per seed:

1. **(Depth only) Sub-step verification gate** — probe atoms, admit or repair-or-reject.
2. **Ladder to band** — turn the shape dial until escape rate ∈ [20%, 80%].
3. **Record** in-band rung, escape rate + CI, rung offset vs other bindings.
4. **(E2) Reducibility A/B** on every escape at the in-band rung — reach / resolution / wind /
   discard.
5. **Consistency check** — ratio split (step 4) agrees in direction with rung offset (step 3).

Breadth seeds skip step 1 (their knowledge is transmitted by construction — reach-boundness is
the point, not a contaminant). Depth seeds cannot skip it.

---

## Inherited kill condition, restated at instrument level

The prediction dies if either legibility path fails to separate by architecture:

- reducibility ratio inside the TOST equivalence margin (per the capacity note), **or**
- zero rung offset between bindings across both shapes' ladders.

A calibrated corpus with a working sub-step gate that *still* shows no separation is the
strongest possible falsification — it means the active/total decomposition adds no predictive
content over the single-window budget, and the note is retracted. The instrument is built to
be able to kill the claim, not to protect it.

---

## Status

**Projected instrument, second stage.** Ladder procedure and sub-step gate are derived and
authored; unexercised. Promotes to **reported** when a first binding has been laddered to band
on at least one seed per shape and the sub-step gate has admitted or repaired every depth seed
for that binding. That first banded, gated seed pair is the go/no-go for the full E2 run.
