# GATE 3 — the pin advance to v5.13.0 (I-3): the prediction, before the operation

**Status: draft-pending-ruling. Nothing advanced yet.** The `DDD-dec-29`/`DDD-dec-34` pattern:
prediction stated and committed before the operation; ref advanced first and hashes re-instrumented
second, so a pass is distinguishable from a skip; verified after; divergence recorded, never
reconciled.

## The operation

`graph/upstream.yaml` `ref: v5.12.0` → `ref: v5.13.0`. Tag verified at session start: `v5.13.0` =
`5c7fe46`, exactly the head of the upstream default branch.

## Baseline, run fresh before anything moves

`python3 validate-core-order.py core/` at `ref: v5.12.0`, this session, matches the migration
record's in-session observables exactly:

> upstream: 71 pins resolved against the pinned ref, 0 basis-loss, 0 content-drift, 1 shadowed id(s)
> 5 documents, 5 terms, 5 graph objects, 4 embedded, 0 errors, 0 warnings

## The prediction

Quoted from the ground-migration execution record
(`meta/sessions/2026-08-31-ground-migration-exec/gate3-prediction.md` §2), stated there before the
upstream edits were made, and owed its verification by "a session that can verify its own
prediction, which is this one":

> **Prediction: when the downstream pin next advances past these commits, exactly two W6 fire and
> no more, both from W1:**
>
> | id | occurrences in hashed fields | pinned hash (= live, verified) | predicted hash after edit |
> |---|---|---|---|
> | `DDD-measure-01` | 1 (statement) | `sha256:66b01ede631c0173d86696dca945ade53c9ffe37462bbe290a6df6b6de4b41ea` | `sha256:d78274d2350cb867c9ec3497aaf13caeafb4792f9e20c20697ba54114a58c198` |
> | `DDD-measure-16` | 2 (statement) | `sha256:2d763d1adf9e1c68c88d1f5c3e30550a5079e274d84e688c31f5f5bb51f1d94e` | `sha256:6828d06649045bfdf374f985a7984d337d01fdb42be29ef8f051a185411fe674` |
>
> **Zero W5** (no status moves), **zero W7** (no id added or shadowed), **zero E12/E13.** Of the
> 71 pins, exactly these two digests move; the other 69 are verified unchanged after the edits.
> The edit is the phrase `ground distribution` → `deployment distribution`, verbatim, nothing else
> in any hashed field.

Restated for this operation's observables: at step (b) below the validator must report **71 pins,
0 basis-loss, exactly 2 content-drift — `DDD-measure-01` and `DDD-measure-16`, old and new digests
exactly as tabled — 0 status movement, the one standing W7 unchanged**. Any other id firing, any
other digest, or a silent pass is divergence, to be recorded and held, not reconciled.

**Non-interference, stated so it is checkable:** this session's I-1 change to `DDD-frame-08` lives
on the upstream session branch only; the pin resolves against the `v5.13.0` tag, which does not
carry it. Predicted contribution of I-1 to this operation: **nothing**. (`DDD-frame-08`'s pinned
hash `cf73b307…` stays verified at the tag; its supersession fires at a *later* advance, after the
close's version proposal is cut.)

## Order of operations

a. This file commits (the prediction is a repo object before the operation — `DDD-dec-20`'s logic
   applied to `DDD-dec-29`'s pattern).
b. **Ref advances alone** (`ref: v5.13.0`, no hash touched), one commit; validator runs; the two
   predicted firings are **observed**, not assumed.
c. **Re-instrumentation second:** the two `content_hash` values move to the predicted digests, one
   commit; validator returns to baseline shape (71 pins, 0 basis-loss, 0 content-drift, 1 shadowed
   id).
d. The advance files as a decision, `core/decisions/DDD-dec-35` (the DDD-dec-10/16/18/25/28/29/34
   convention: an advance is governed, not mechanical), and the `upstream.yaml` comment block takes
   the advance record with prediction and verification, as every prior advance has.
e. **The primer regenerates at the new pin** (`generate.py --upstream` on the local clone at
   `v5.13.0`): generated blocks re-draw, the stamp's `pin=` moves to v5.13.0. The hand-written
   sections carry the pin in their own text by design, so their `v5.12.0` references move by hand,
   and §6's "the migration's changes arrive at the next advance" paragraph updates — **this is
   that advance**, as §6 itself anticipates.
f. **Paper A's three checkers re-run at the new pin** (`check-quotations.py`, `check-appendix.py`,
   `check-status.py`). Expected: the sixteen deferred manuscript occurrences were deferred *for*
   this advance ("they quote canon at the pinned ref and regenerate when the pin next advances").
   Whatever the checkers report is **recorded verbatim at the verification hold**; which passages
   move now versus carry is Emil's ruling, not this session's reconciliation.
g. **D7 repairs here** (GATE 2 ruling): the front page's "(`v5.5.0` at time of writing)" — the
   version parenthetical is dropped in favour of pointing at `graph/upstream.yaml`, which is
   authoritative and cannot go stale.
h. The successor item "passages quoting a live claim verbatim — `DDD-measure-12` and
   `term:verdict` still read `ground distribution` at `v5.12.0`" **discharges at this advance**:
   at v5.13.0 both nodes read `deployment distribution`, so the blocker the deferral named is
   gone. Recorded in the successor file at the verification step.

**HOLD — awaiting Emil's ruling on the prediction before the ref moves.**

---

## RULING (Emil, 2026-09-04): prediction approved; advance

As stated, with two additions: (f) none of the sixteen deferred occurrences moves here — a pin
advance is not a licence to reopen a deferral; what the checkers report is evidence, recorded for
whichever session next touches that manuscript; this session repairs no manuscript prose. (g) the
pointer repair is the better one — a stale version number recurs, a pointer does not.

## VERIFICATION (executed 2026-09-04)

**Step (b) — ref alone (`a2676cf`), observed:**

> upstream: 71 pins resolved against the pinned ref, 0 basis-loss, **2 content-drift**, 1 shadowed id(s)
> W6 `DDD-measure-01`: pinned `sha256:66b01ede…` → resolves `sha256:d78274d2…`
> W6 `DDD-measure-16`: pinned `sha256:2d763d1a…` → resolves `sha256:6828d066…`
> total warnings: exactly 2; errors: 0

Both ids and all four digests exactly as tabled. Zero W5, zero E12/E13, the standing W7 unchanged
at 1. **The prediction held in every limb.** Divergence: none.

**Step (c)–(d) — re-instrumented (`d8d0306`):** validator back to baseline shape — 71 pins, 0
basis-loss, 0 content-drift, 1 shadowed id; 0 errors, 0 warnings. The advance filed as
`core/decisions/DDD-dec-35` (23 decisions valid) and recorded in `graph/upstream.yaml`'s comment
block in the house pattern. Non-interference verified: `DDD-frame-08`'s pinned hash unchanged at
the tag — predicted nothing, observed nothing.

**Step (e) — primer (`571b557`):** 13 generated regions re-drawn; stamp `pin=v5.13.0`; `--check`:
"OK: stamp present, pin v5.13.0, all regions current." Hand-written sections verified to hold at
v5.13.0 (zero pre-migration vocabulary) and their pin references moved; §6's "arrives at the next
advance" paragraph discharged. Roster unchanged: 89 claims, `established` still the same four.

**Step (f) — Paper A checkers at v5.13.0, recorded as evidence, nothing repaired:**

| Checker | Target | v5.12.0 | v5.13.0 |
|---|---|---|---|
| `check-quotations` | paper-a.md | 30 verbatim, 0 failing | **30 verbatim, 0 failing** (rc 0) |
| `check-status` | paper-a.md | 96 assertions, 0 wrong | **96 assertions, 0 wrong** (rc 0) |
| `check-appendix` | paper-a.md + supplement | 75 rendered, 75 cited, 0 discrepancies | **4 discrepancies** (rc 1): `DDD-measure-01`, `DDD-measure-11`, `DDD-measure-16` statements; `term:verdict` canonical wording |
| `check-quotations` | supplement | 1 failing (UNCITED, the boundary rule) | 1 failing, **identical** |

The four appendix discrepancies are the sixteen-deferral's expected expiry — the rows render canon
at v5.12.0 wording and canon moved. Per the ruling they are **recorded, not repaired**; noted in
the successor file for whichever session next touches the manuscripts. The supplement's one
failing quotation is identical at both refs — ref-independent and pre-existing, not this advance's
divergence; booked for the I-4 sweep (the supplement quotes the session's own boundary rule, which
is not a canon node, and the supplement was not a declared target of that checker).

**Step (g) — D7:** the front page now points at `graph/upstream.yaml` as authoritative, no version
named. **Step (h):** the successor item's blocker recorded as discharged at `DDD-dec-35`.

**Also recorded, an instrument note for I-4:** all three checkers print their docstring and exit
**0** when invoked with wrong arguments (e.g. an unrecognised `--upstream` flag) — a bad
invocation is indistinguishable from a pass by exit code alone. Found by making exactly that
mistake in this session; the counts above are from corrected invocations with directly captured
exit codes.

**HOLD at GATE 3 (verification) — awaiting Emil's ruling on the verification record.**
