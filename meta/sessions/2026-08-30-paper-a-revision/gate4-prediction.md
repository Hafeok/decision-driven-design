# GATE 4 — the pin advance, predicted before it is run

**Status: prediction, committed before the operation.** `graph/upstream.yaml` still reads
`ref: v5.9.0` at this commit. Nothing has been advanced. This document exists so the advance can be
**observed rather than assumed**, which is the `DDD-dec-29` pattern: state the firing, advance the
ref, re-instrument, and compare.

Computed by `predict-pin-advance.py` in this directory, which reads the pin list at the current ref
and re-implements `validate-core-order.py`'s own `pinned_content_digest` — sha256 over
`statement`, `region` and `canonical_md`, joined with `\x00`, with `status` deliberately excluded
because `W5` already instruments it.

---

## The prediction

**`E12` — 0.** Every one of the 67 pinned ids still exists at `v5.12.0`. Verified independently at
Gate 1 by a different route: `gen-appendix.py` resolved all 72 nodes the paper cites, and would
have exited had one been missing.

**`W5` basis loss — exactly 1.**

| id | pinned at | at `v5.12.0` |
|---|---|---|
| `DDD-frame-15` | `projected` | **`retired`** |

`DDD-measure-06` also retires at `v5.12.0` and **will not fire `W5`, because it is not pinned.**
That is worth stating plainly: the node whose retirement forces the largest prose repair in this
revision is invisible to the pin instrument, and Gate 1 found it only because a sweep was written
for inline status assertions. A claim a projection leans on without pinning is a claim that can
move silently — `DDD-agent-01` applied to this repository's own instruments. **Pinning
`DDD-measure-06`, `DDD-measure-16` and `DDD-measure-17` is proposed at this advance** and is a
ruling, not a mechanical step.

**`W6` content drift — exactly 6**, on the three fields the digest covers.

| id | field that moved | from → to |
|---|---|---|
| `DDD-cost-09` | `region` | `fecb317f…` → `f6cc24f0…` |
| `DDD-delivery-01` | `statement` | `67377ef2…` → `1340d483…` |
| `DDD-frame-02` | `statement` | `f45492ee…` → `0002f60b…` |
| `DDD-frame-15` | `statement`, `region` | `6d14509d…` → `2a65878d…` |
| `term:delivery` | `canonical_md` | `1e7b2e4d…` → `c56909e5…` |
| `term:residual-discretion` | `canonical_md` | `77284b14…` → `9bbe31e3…` |

**`W7` shadowed ids — 1, unchanged.** `term:maturation`, declared against `DDD-dec-21`. It has
stood at every advance since and this one does not touch it.

**Unchanged pins: 61 of 67.**

---

## Reconciliation against the migration seed's own prediction

`meta/migration-plan-ground.md` predicts the next advance past both sessions: *"Add three that this
session created and did not fire, because the pin stays at `v5.9.0`: `term:delivery`,
`DDD-cost-09`, `DDD-delivery-01`."*

**Those three appear, exactly.** The other three — `DDD-frame-02`, `DDD-frame-15` and
`term:residual-discretion` — are the Phase 1a session's repairs and are not ground-migration work,
which is why the seed does not list them. The seed also names **seven** W6 that fire when W1
executes in canon (`term:actor`, `term:arrangement`, `term:capability`, `term:capacity`,
`term:closure`, `term:judgment`, `term:residual-discretion`). **None of those seven fires here**,
because W1 renames nothing in the principle repository in this session: this session carries W1 in
the two manuscripts only. If any of the seven fires at this advance, the prediction is wrong and
something has moved that this session does not understand.

## What would make this prediction wrong, and what happens then

Any count other than `E12` 0 · `W5` 1 · `W6` 6 · `W7` 1, or any id outside the six named above.
If that happens the advance stops and the difference is reported at this gate rather than
reconciled afterwards. **The prediction is the instrument here; the advance is only the reading.**
