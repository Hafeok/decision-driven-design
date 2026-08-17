# Wave 3 session manifest (2026-08-18)

**Session type:** interactive canon curation, five gates, Emil ruling at every gate; nothing
merged by the session. Branch `claude/wave3-principle-filings-edewf2`, both repositories.
Base: upstream `01db788` (= v5.6.0), downstream `0452a40`.

## Filings, upstream (`actor-indexed-determination`)

| Node | What | Grade | Gate |
|---|---|---|---|
| `DDD-frame-13` + `term:determinable`, `term:determinate` | The determinable: demand's object, its determinate product; demand a measure over unresolved determinables | derivation | 2 |
| `DDD-frame-14` + `term:outcome` | The determinate's two registers; every diachronic instrument runs on verdicts | derivation | 2 |
| `DDD-frame-15` | Supply-mode exhaustiveness; *demand is never unmet, only ungoverned*; seam guard passed verbatim | derivation | 2 |
| `DDD-frame-16` | Discharge is act-indexed | derivation | 2 |
| `DDD-ground-05` | Constitutive priority of ground, symmetry stated | derivation | 2 |
| `DDD-floor-02` | The relational floor over frame-01's tuple | derivation | 3 |
| `DDD-hyp-01`–`05` | The hypothesis set (new `hyp` area), preregistration-shaped falsifiers, owner paper-4 | statement | 4 |
| `core/14-indexed-determination.md` | Establishing document, minimal; `establishes: []` | — | 3–4 |
| `core/13` §4 | The discharge section (Q-A/Q-B exposition; Q-C as its flagged paragraph) | — | 2 |
| `core/00` §4a, `core/09` §7a | Determinable and register exposition | — | 2 |
| `DDD-dec-24` | The session decision | — | 5 |

Amendments: `DDD-frame-01` (notes; flag cleared), `DDD-frame-02` (residual-discretion clause;
flag cleared), `DDD-frame-03` (historical clause softened; flag cleared), `DDD-frame-07`
(umbrella citation; flag cleared), `core/13` §5 closer (maturation consequence now points at
09 §7a). Terms settled at acceptance per the GATE 4 ruling: the three new terms enter
`settled`; Emil's merge is the ratification act.

## Filings, downstream (`decision-driven-design`)

- `DDD-dec-25` — the pin advance v5.5.0 → v5.6.0, **the miss recorded**: the advance should
  have accompanied the freight PR's acceptance and did not. It was caught by this session's
  GATE 1 survey, not by the instrument — W6 resolves against the ref you pinned, so a missed
  advance is exactly the movement it cannot see. One honest sentence, as ruled: **W6's first
  live gap was found by a survey doing the instrument's job.**
- `DDD-cost-16` annotated: mechanism named by `DDD-frame-14`.
- `DDD-cost-24` annotated: qualification restated upstream on `DDD-hyp-04/05`, cross-link here.
- Session record: prompt, bootstrap, foundation (identity: 742 lines / 5021 words / sha256
  `f79301e0…`), five gate reports, Batch P map, this manifest, successor items.

## Validator state at close

- Upstream: 15 documents, 0 errors; 60 claims valid; 7 decisions valid. **W1 baseline moves
  52 → 59** (accepted at GATE 2 as honest forward pointers: docs 00–07 use the word
  `term:outcome` now owns; each doc gains its pointers when next touched, not in a sweep).
- Downstream: 0 errors, 0 warnings except the standing `term:maturation` shadow; 25 claims, 18
  decisions valid; 32 pins resolved at v5.6.0 with 0 basis-loss, 0 content-drift.

## On acceptance of the upstream PR (the staged steps — performed)

1. Upstream PR #14 merged (4d0d177); the release descriptor `releases/v5.7.0.yaml` — added at
   the acceptance ruling, with the CLAUDE.md release runbook — cut tag `v5.7.0` at the merge
   commit via CI. The three term settlements are thereby ratified.
2. Downstream ref bumped v5.6.0 → v5.7.0. The content prediction held: nothing pinned moved.
3. Three pins added: `DDD-frame-14`, `DDD-hyp-04`, `DDD-hyp-05`. **Incident, recorded:** the
   three were born stale — hashed without the instrument's field normalisation — and W6 fired
   on all three in the first run. Corrected with the instrument's own normalisation; second
   run clean (35 pins, 0 basis-loss, 0 content-drift). W6 thereby caught a mis-transcribed
   pin within one run of its creation — a live verification on a failure class the session
   had not predicted. Full record in `DDD-dec-25`'s notes.
4. The downstream PR stands on its green.

## Post-merge residue, flagged

`DDD-dec-24` merged upstream carrying its `DRAFT-PENDING-RULING (GATE 5)` marker — the
acceptance that ratified it happened after the branch's last upstream commit. Its own notes
state the acceptance is the ratification act, so the marker is self-resolving in content but
stale in form; one line to repair at the next upstream touch, not worth a post-merge commit
to main now.
