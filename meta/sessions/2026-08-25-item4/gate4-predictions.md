# GATE 4 — predictions, stated before the operations they predict

**Committed before `gen-appendix.py`, `check-appendix.py`, `check-quotations.py` or
`validate-core-order.py`'s cross-repo pass is run in this session's closing sweep.** A prediction
recorded after its instrument has spoken is not a prediction, and the whole value of stating one is
that a surprise is visible as a surprise.

**No pin operation occurs in this session.** The pin is held at `v5.9.0` by standing ruling. Nothing
below advances, adds or removes a pin, and `graph/upstream.yaml` is not edited.

---

## P1 — W6 (pinned content movement): **unchanged from this session's start. No new W6.**

The reasoning, so a wrong prediction is diagnosable rather than merely wrong:

1. **`pinned_content_digest` hashes `statement`, `region` and `canonical_md`, and nothing else.**
   The docstring says why status is excluded; `notes` and every other field are excluded too.
2. **This session touched no `statement` and no `region`.** Verified mechanically against `v5.10.0`:
   seven canon files changed upstream, of which four are claims, and all four are unchanged in
   `statement`, `status` and `region`. What changed on them is `retired_from` (a new field) and an
   appended `notes` paragraph — neither is hashed.
3. **The pin resolves at `v5.9.0`, which this session does not touch at all.** The comparison W6
   makes is between `content_hash` in `graph/upstream.yaml` and the object as it stands *at the
   pinned ref*. This session's commits are on a branch that is not that ref and will not be that
   ref.

**Of the four retired claims, exactly one is pinned: `DDD-frame-15`**, at
`status_at_pin: projected`, `content_hash: sha256:6d14509d…`. It was `projected` at `v5.9.0` and
was retired at `v5.10.0`, so the pin is *already* behind head by a status — and that is Phase 1a's
predicted state, held deliberately, not something this session creates or repairs.

## P2 — W7 (local term ids shadowing the pinned upstream registry): **unchanged. No new W7.**

**This session mints no term in either repository.** `core/graph/terms.yaml` is untouched upstream
and downstream. W7 fires on a local term id shadowing a pinned upstream id with no declaration;
with no new local term, the set it quantifies over has not changed.

## P3 — W5 (basis loss): **unchanged.**

Same reason as P1's third point: W5 compares upstream status *at the pinned ref* against
`status_at_pin`. `v5.9.0` is untouched.

## P4 — `check-quotations.py` against the pin: **passes, and the four known failures do not appear.**

The four known-failing quotations fail against **`v5.10.0`**, because Phase 1a retired
`DDD-frame-15` and rewrote its statement into a retirement record while Paper A block-quotes the
live statement. **Paper A is pinned at `v5.9.0`**, where that statement still stands. Run against the
pin, the checker should pass. If it fails, something other than this session has moved.

**This session does not touch any quotation and does not touch the manuscript body.** Only Appendix
A is regenerated, and `check-quotations.py` reads the body.

## P5 — `check-appendix.py` after the `kind` column lands: **fails unless the checker is updated
in the same commit, and the failure mode is silence rather than noise.**

This is a prediction about a defect, made before running, because the defect is visible from
reading the checker and is the kind that a passing run would hide.

`check-appendix.py` parses a claims row into `cols` and then does:

```python
if unescape(cols[-1]) != flat(node.get('statement')): ...
if len(cols) == 2 and cols[0] != str(node.get('status')): ...
```

Adding a `kind` column makes `len(cols) == 3`. The statement check still fires, because it reads
`cols[-1]`. **The status check silently stops firing**, because its guard is an equality on the
column count. The appendix would then be re-read by an instrument that had quietly stopped checking
one of the two columns it exists to check — and it would report success.

**So the prediction is: if `gen-appendix.py` gains the column and `check-appendix.py` is left alone,
the run passes and the verification is weaker than it was.** The independent re-read must learn the
new shape in the same commit as the generator, and the status check must be re-anchored so that a
future column cannot silence it again.

## P6 — the appendix regeneration is idempotent

`gen-appendix.py` carries a defect history recording that its first version was not idempotent.
Running it three times and comparing bytes should produce identical output, as its own docstring
requires. Predicted: identical.
