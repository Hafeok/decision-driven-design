# GATE 4 — deviation: the advance's target changes from v5.15.0 to v5.15.1

**Written and committed before the ref moves to the tag.** The prediction of record is
`gate3-prediction.md` (commit `ef0d444`), whose target was `v5.15.0`. This file records the
change of target and restates the prediction for the new target. It does not edit the original.

## The deviation

| | Predicted (`ef0d444`) | Now |
|---|---|---|
| Target tag | `v5.15.0` | `v5.15.1` |
| Staged at | upstream `cc0abf8` (the landing branch) | unchanged until the bump |
| Releases crossed | v5.14.0, v5.14.1, v5.15.0 | v5.14.0, v5.14.1, v5.15.0, v5.15.1 |

## Cause

PR #24 merged from `e484ca5`. The GATE 2 ruling 3 fix (`cc0abf8`) reached the branch after that
head and was never merged, so `v5.15.0` was cut carrying the narrowing Emil had struck. The fix
ships as `v5.15.1` (PR #25, merge `1cb3819`, ratified head `7266306`; merged with exactly that
head, no content difference). v5.15.1 also carries Emil's GATE 3 glossary ruling. Emil ruled at
GATE 3 that GATE 4 runs against v5.15.1, so the pin should name the release that carries the
ruled canon.

This is the second head-moved miss after v5.14.0. The release-head guard is a priority successor
item.

## Restated prediction for v5.15.1

v5.15.0 → v5.15.1 changes `DDD-ground-06`'s notes, two glossary notes, and adds a release
descriptor. Notes and `i18n/` are outside the pinned digest (statement, region, `canonical_md`),
so **the restated prediction is identical to the original in every limb**:

| Limb | Predicted |
|---|---|
| E12 | 0 |
| E13 | 0 |
| W5 | 0 |
| W6 | exactly 1: `DDD-frame-08`, `sha256:cf73b307…` → `sha256:ef5d5faf…` |
| W7 | 1, unchanged |
| Pins | 74 (71 + `DDD-ground-06`, `term:act-address`, `DDD-ground-01`), with the three new digests exactly as in `gate3-prediction.md` |

A pre-computation against merged `main` (`1cb3819`, the content v5.15.1 will tag) with the
checker's own loader and digest gives exactly this: 74 pins, one W6 on `DDD-frame-08`, nothing
else. That was a dry computation; the verification of record runs against the tag.
