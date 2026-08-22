# Downstream merge checklist — the three tag-dependent steps

**Session** `2026-08-21-floor-lineage` · governed by `DDD-dec-29`

> **RUN AND COMPLETE, 2026-08-22.** Upstream PR #17 merged as `bce18fe`; `releases/v5.9.0.yaml`
> landing on the default branch cut **`v5.9.0`** at that commit, verified as an ancestor of the
> default branch. All three steps below were taken in order and every expected result was met —
> including the prediction test, which was run by advancing `ref` **first** and re-instrumenting the
> hash **second**, so the W6 firing was observed rather than assumed. `DDD-dec-29` records the
> observation alongside the prediction it was written to test, and its `[PROPOSED]` banner is
> struck. The checklist is kept as the record of what was done, not as outstanding work.

The downstream pull request is complete **except** for three steps that cannot be taken until the
upstream tag exists. This file is the checklist, with each step's expected result already verified
against the staged upstream branch, so the person running them can tell a correct outcome from a
plausible one.

## Why these three wait

`graph/upstream.yaml` pins **a tag, never a branch**, and the checker shallow-clones that ref, so
naming `v5.9.0` before the tag is cut fails E12 on all 67 pins at once. Two of the three steps also
write the ref into a **published manuscript** — `papers/paper-a/paper-a.md`'s front matter and
Appendix A's generated footer — and a branch sha in a paper is the defect the pin discipline exists
to prevent. Per `CLAUDE.md`, merging `releases/v5.9.0.yaml` to the upstream default branch is what
cuts the tag; there is no manual `git tag` step.

**Order:** upstream PR merges → `v5.9.0` is cut → steps 1–3 below → verify the `DDD-dec-29`
prediction → downstream PR is mergeable.

---

## Step 1 — advance the pin and re-instrument `term:floor`

In `graph/upstream.yaml`:

- `ref: v5.8.0` → `ref: v5.9.0`
- `term:floor`'s `content_hash`:
  - from `sha256:daf43e076f83b338c1b37e826492083e05ea080ccf26cd911bbe632bf7c339b0`
  - to `sha256:917f7e4d23d4af877480591deb3ba72d63f50894488c42c2c8c03c6634b50d86`
- `status_at_pin: settled` — **unchanged**, and it should not move.

Add the header comment recording the advance, per the file's own convention.

**Expected:** `python3 validate-core-order.py core/` reports **67 pins resolved, 0 basis-loss, 0
content-drift, 1 shadowed id** — the same as the v5.8.0 baseline. Content-drift returns to **0**
because the pin has been advanced to match, which is the point: W6 fired once, as a governed advance,
and is then quiet.

**If anything other than `term:floor` drifts, stop.** `DDD-dec-29` predicts exactly one W6 and
nothing else, and a second firing means the release moved something this session did not account
for.

## Step 2 — regenerate Appendix A against the tag

```
python3 papers/paper-a/gen-appendix.py papers/paper-a/paper-a.md \
        <upstream-repo> v5.9.0
```

**Expected diff: exactly two lines**, verified against the staged branch on 2026-08-21 —

1. `term:floor`'s row gains the definition ahead of the claim sentence;
2. the generated footer's ref changes from `v5.8.0` to `v5.9.0`.

**No other row moves.** Appendix A is generated and never hand-edited; if the diff is larger, do not
edit it back — find out why.

## Step 3 — the manuscript's declared ref

`papers/paper-a/paper-a.md:7` declares *"a projection of `actor-indexed-determination` at
`v5.8.0`"*. Advance to `v5.9.0`. Check the surrounding sentence for any second mention.

---

## Verification, after all three

| Check | Expected |
|---|---|
| `validate-core-order.py core/` (downstream) | 67 pins, 0 basis-loss, **0 content-drift**, 1 shadowed id |
| `validate-claims.py core/decisions/ --decisions` | 21 decisions valid |
| `check-appendix.py … v5.9.0` | 72 rendered, 72 cited, **0 discrepancies** |
| `check-quotations.py … v5.9.0` | **29 verbatim, 0 disclosed-partial, 0 failing** |

**The last row is measured, not predicted**, and it is worth saying why it did not change. `§6.1`'s
quotation now carries a `closing clause` disclosure and a leading `…`, so a reader might expect it to
move into the disclosed-partial column. It does not, and should not: `contains` matches it before the
disclosure branch is ever reached, because it is still a verbatim *run* of the canonical text. **The
disclosure is carried for the reader, not for the checker** — which is exactly the finding routed to
Paper A's freight item 1 as *verbatim is not complete*. Run on the staged branch on 2026-08-21: 29
verbatim, 0 disclosed-partial, 0 failing.

## Last step

Flip `DDD-dec-29` from `[PROPOSED]` to ratified, replacing "predicted" with what was observed. If the
prediction did **not** hold, record the divergence in the same file rather than editing the
prediction — that is the whole reason it was written down first.
