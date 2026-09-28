# GATE 3 — predicted firing of the pin advance (act address landing)

**Written and committed before the ref moves.** This file is the prediction. The staging commit,
and later the bump at GATE 4, are the operation. Verification at GATE 4 compares the observed
firing with this file limb by limb, and records any divergence rather than reconciling it.

## The advance

| | Value |
|---|---|
| From | `v5.13.0` (the pin at `cba63ef`) |
| Staged at | upstream branch `claude/act-address-landing-bla6io`, head `cc0abf8` (PR #24) |
| To, at GATE 4 | tag `v5.15.0`, cut when PR #24 merges |
| Releases crossed | v5.14.0, v5.14.1, v5.15.0 |
| Pins before | 71 |
| Pins added | 3 |
| Pins after | 74 |

## How it was computed

Each pin's upstream object was loaded at `v5.13.0` and at `cc0abf8` with the checker's own
`load_upstream_graph`, and hashed with its own `pinned_content_digest` (statement, region,
`canonical_md`). Every pin was compared on existence (E12), status (W5) and digest (W6). Upstream
objects that changed between the two refs without being pinned were listed separately. They fire
nothing, because only pinned ids are instrumented.

## Prediction, limb by limb

| Limb | Predicted | Why |
|---|---|---|
| **E12** | **0** | All 71 existing pins exist at `cc0abf8`. The 3 added pins exist there and not at `v5.13.0`, so they are added only with the ref advance. |
| **E13** | **0** | No document in this repository embeds a pinned upstream id whose `canonical_md` moved. None embeds `term:act-address`. |
| **W5** | **0** | No pinned status moves. `DDD-measure-11` and `DDD-measure-13` were demoted at v5.14.0, but they are not pinned. |
| **W6** | **exactly 1**: `DDD-frame-08`, `sha256:cf73b307…` → `sha256:ef5d5faf…` | Its statement was re-scoped at v5.14.0 while its status held. This is v5.14.0's published prediction, carried forward because the pin never crossed v5.14. Full new digest: `sha256:ef5d5fafedb588994141c8f4df504c7589ab3ea7b5257f3ea97f37ba3db07ff7`. |
| **W7** | **1, unchanged** | The one standing shadowed id. `term:act-address` shadows nothing here. |

Summary line expected from the checker, with the ref advanced and `DDD-frame-08` not yet
re-instrumented: **74 pins resolved, 0 basis-loss, 1 content-drift, 1 shadowed id**. After
re-instrumenting `DDD-frame-08` at GATE 4: **74 pins, 0 basis-loss, 0 content-drift, 1 shadowed
id**.

## Pins added

| Id | `status_at_pin` | `content_hash` at `cc0abf8` | Why |
|---|---|---|---|
| `DDD-ground-06` | projected | `sha256:87a6adab30551a4f464cdc1020ae0155f22d6a86d3baac30917894a1cb3b6609` | Basis of `DDD-address-01…05` and `DDD-dec-38` |
| `term:act-address` | draft | `sha256:d66ddee2ca634dc8ab84d96798b5ca0af36403551c826fb3affd86758f1df00c` | The term the five claims presuppose |
| `DDD-ground-01` | projected | `sha256:eb4679f9878a220b8a4c39e785b1d3cd9f6ad7eb717a02d1eff6ff97ef359d93` | `DDD-dec-38`'s basis, unpinned until now (`DDD-agent-01`) |

`DDD-dec-37` is not pinned: the checker indexes upstream claims and terms, not decisions.

## Unpinned upstream movement between the refs (fires nothing)

| Id | Movement |
|---|---|
| `DDD-measure-11`, `DDD-measure-13` | Demoted `reported` → `projected` at v5.14.0 |
| `DDD-ground-06`, `term:act-address` | Added at v5.15.0 (and pinned by this advance) |

## Conditions that void part of this prediction

- **PR #24 changes before merge.** The added pins' digests are taken at `cc0abf8`. If a ruled
  change to PR #24 moves `DDD-ground-06`'s statement or region, or `term:act-address`'s
  `canonical_md`, those two hashes are re-stated in a new commit to this directory before the
  bump. Notes-only changes do not move them.
- **Another release lands first.** If any upstream release is cut between `v5.14.1` and the tag
  this advance targets, the prediction is re-run against it before the bump.

## What staging is expected to show

The staging run resolves against the branch, not the tag, so it previews the firing but does not
verify it. It should show the same limbs as above. The verification of record is at GATE 4,
against the tag.
