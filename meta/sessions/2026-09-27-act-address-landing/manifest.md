# Manifest — act address landing (2026-09-27 … 2026-09-28)

Interactive canon curation. Emil ruled at every gate. The session merged nothing. Branch
`claude/act-address-landing-bla6io` in both repositories, plus
`claude/act-address-landing-bla6io-v5.15.1` upstream for the correction release.

## Weakest point, named first

**The session's own release process failed once, in the way it failed before.** PR #24 merged
one commit behind the head that carried the GATE 2 ruling, so `v5.15.0` shipped a flag Emil had
struck. The correction is `v5.15.1`, and the pin names it. Nothing in the tooling would have
stopped it. The same shape as v5.14.0 means it is a class, not an accident. The release-head
guard (successor item S-1) is its remedy, and until it exists, every release depends on someone
checking the head by hand.

## What landed

| Where | Object | Status | Commit or release |
|---|---|---|---|
| Upstream | `DDD-ground-06` — the act address | conceptual, projected | `d30efe7` (v5.15.0); notes corrected `7cfc828` (v5.15.1) |
| Upstream | `term:act-address`, established by `core/14` §5 | draft | `d30efe7` (v5.15.0) |
| Upstream | `DDD-dec-37` — the ruling | decision | `d30efe7` (v5.15.0) |
| Upstream | Glossary: `handlingsadresse`, `lagsti`; notes "Se core/14." | — | `d30efe7` (v5.15.0); notes `7266306` (v5.15.1) |
| Upstream | `releases/v5.15.0.yaml`, `releases/v5.15.1.yaml` | tagged | `v5.15.0` at `13128a7`; `v5.15.1` at `1cb3819` |
| Downstream | `meta/sessions/2026-09-27-act-address/`, byte-identical to the bundle | — | `fd194df` |
| Downstream | `DDD-address-01` to `05` | projected | `76d644e` |
| Downstream | `DDD-dec-38` — the filing and the advance | decision | `76d644e`; finalised with this manifest |
| Downstream | `graph/upstream.yaml` — v5.13.0 → v5.15.1, three pins added | — | staged `1419dbb`; bumped `662f8b2`; re-instrumented `50e90ca` |

The pre-registration's SHA-256 was verified at arrival, at landing and after landing:
`ef34e3bc14ab793800edd8c096e82adf0652ef8bc284d54d52efd20f8bf5f5eb`. It was never edited.

## The pin advance, verified limb by limb

Prediction of record: `gate3-prediction.md` (`ef0d444`, committed before the ref first moved).
Change of target: `gate4-target-deviation.md` (`4b94593`, committed before the bump).

| Limb | Predicted | Observed at `v5.15.1`, ref first, hashes second | Held |
|---|---|---|---|
| E12 | 0 | 0 | Yes |
| E13 | 0 | 0 | Yes |
| W5 | 0 | 0 | Yes |
| W6 | Exactly 1: `DDD-frame-08`, `cf73b307…` → `ef5d5faf…` | Exactly 1: `DDD-frame-08`, `cf73b307…` → `ef5d5faf…` | Yes, both digests |
| W7 | 1, unchanged | 1 shadowed id | Yes |
| Pins | 74 | 74 resolved | Yes |
| Added-pin digests | `DDD-ground-06` `87a6adab…`, `term:act-address` `d66ddee2…`, `DDD-ground-01` `eb4679f9…` | No drift on any of the three at the tag | Yes |

After re-instrumenting `DDD-frame-08`: 74 pins, 0 basis-loss, 0 content-drift, 1 shadowed id.
`validate-core-order.py` reports 0 errors and 0 warnings.

**Deviation: one, in the target, not in the firing.** The prediction targeted `v5.15.0`. The pin
names `v5.15.1`, on Emil's GATE 3 ruling, because `v5.15.0` lacks the GATE 2 fix. Only notes and
`i18n/` separate the two, and neither is in the pinned digest, so the prediction was restated
unchanged before the bump and held unchanged after it. The v5.14.0 descriptor's published W6 for
`DDD-frame-08` is discharged here, two releases after it was written.

## Rulings, by gate

| Gate | Record | Rulings |
|---|---|---|
| 0 | `prompt.md`, `bootstrap.md` | Arrival committed before any canon. Push blocked by a 403 until GitHub access was fixed. |
| 1 | `gate1-survey.md`, `gate1-rulings.md` | Nine: falsifier repair, neutral upstream wording, citation, rule 1 kept joined, `address-05` filed, `address-03` filed, dry-run items, term home, glossary |
| 2 | `gate2-rulings.md` | Wider neutral wording and README row confirmed; `term:act` narrowing struck; the T2b escalation-rule item; PR watching; GATE 3 authorised |
| 3 | `gate3-rulings.md` | GATE 3 accepted; v5.15.1; GATE 4 against v5.15.1; the Danish notes struck; three successor items |
| 4 | This file, `successor-items.md` | — |

## Corrections the session made to its own work

| What | Correction |
|---|---|
| GATE 0 push loop reported "pushed" on a 403 | The loop tested for "ahead" on a branch with no upstream. Corrected in the next report; the push was verified with `ls-remote` from then on. |
| Survey's narrowing of the `term:act` flag | Struck at GATE 2 and restored in `v5.15.1`. |
| First GATE 3 message's Danish-notes placeholder | Not guessed. Flagged and held until ruled. |

## Validators at close

| Gate | Upstream `v5.15.1` | Downstream head |
|---|---|---|
| `validate-core-order.py` | 0 errors, 66 warnings (baseline), 0 W4 | 0 errors, 0 warnings; 74 pins clean |
| `validate-claims.py` claims | 64 claims, 32 warnings (baseline 32) | 31 claims, 6 warnings (baseline 6) |
| `validate-claims.py --decisions` | 14 decisions, clean | 24 decisions, clean |
| `validate-releases.py` | 13 descriptors, clean | — |

## Open

Everything open is in `successor-items.md`, S-1 to S-10. S-1 (the release-head guard) is the
priority. S-2 (T2b) is the item the whole act address set now waits on.
