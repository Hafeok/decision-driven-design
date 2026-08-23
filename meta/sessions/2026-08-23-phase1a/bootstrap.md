# Bootstrap — Phase 1a: the discharge partition and `DDD-measure-06` (2026-08-23)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any canon edit, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/phase-1a-claim-repairs-i6ilkv` (both repositories)
- **Base commits:**
  - `actor-indexed-determination` — head `bce18fe80bf96a0f3106029a655f8749b34487d0`; **canon pinned
    at tag `v5.9.0`, which is that same commit** — head and tag coincide, so there is no unreleased
    delta upstream at arrival.
  - `decision-driven-design` — head `8a4c8f507046d34bee6bc469798ab9422f26ff16` (the floor-lineage
    merge, PR #27)
  - `product-cli` — untouched
- **Gates:** 4 (survey and the R-1/R-3 dispositions · R-1 and R-2 drafted together · R-3 · close)
- **Principal:** Emil
- **Session type:** interactive canon curation — hold at every gate, merge nothing
- **Prompt identity:** `prompt.md`, 113 lines, sha256
  `b94d7a02ff5183c6822f42f82481afd89d5aff313b473bae8042d1ec270df4d1`

## Tag verification, at fetch

Emil reported canon at **v5.9.0**. Fetched and verified: `v5.9.0` is the newest tag in
`actor-indexed-determination`, an annotated tag dated 2026-08-22, message *"v5.9.0 — The floor: its
definition, and its ancestry"*, pointing at commit `bce18fe`. **Head is that commit** — unlike the
floor-lineage session's arrival, there are no post-tag canon commits, so canon-at-head and
canon-at-tag are the same object for this session's whole run.

## Input arrival — one failure, recorded at arrival rather than at close

The prompt names two uploaded inputs: `paper-a-objective-review.md` and `paper-a-review-triage.md`.
**Neither arrived.** The session's upload directory holds exactly one file, the prompt itself
(`eff695d8-promptphase1a.md`), and neither review nor triage is present anywhere in either
repository.

This is `DDD-dec-17`'s arrival-failure class, recurring — the sixth instance, and the first since
`DDD-dec-20` filed the convention. It is recorded here at arrival, before work, because that is what
the convention is for.

**Consequence for this session's work, stated plainly.** The prompt itself quotes the review's
substance for every repair it commissions: the three R-1 overlaps with their reasoning, the six test
cases, R-2's four conflated phenomena and its decisive hash case, R-3's §7 revision and its two
conceded directions, and R-4's axis error. That is enough to do the work. It is **not** enough to
quote the reviewer, so:

- Every claim about what the review says is sourced to the **prompt's** rendering of it, never
  presented as a quotation of the review, and is marked as such wherever it appears in canon.
- No `notes:` or evidence field in any drafted claim cites `paper-a-objective-review.md` as a
  locatable artefact, because it is not one in this repository.
- The triage's advisory readings are unavailable and no ruling in this session rests on them.

If Emil uploads either file mid-session, it is filed under this directory with its identity —
line count and sha256 — recorded in the commit body, per the `holding-note-ground-axes-rev18`
precedent in `DDD-dec-20`'s notes, and the affected drafts are re-read against it.

## Scope, as committed

Four items from the Paper A external review, of which **two repair, one separates, one records**:

- **R-1** — `DDD-frame-15`'s four discharge modes do not partition. Two dispositions drafted, Emil
  rules: **(a)** a priority rule, or **(b)** the modes recast as orthogonal axes. The disposition is
  **tested against six cases before it is proposed** — trained inference, lookup tables, declared
  defaults, randomised search with checking, abstention, timeout — and one that cannot classify all
  six exactly once is not ready. The session additionally reports whether **distinct names** for the
  discharge modes would carry more of the repair than a priority rule does, the store vocabulary
  being shared.
- **R-2** — `residual discretion` conflates four phenomena. **Separate first; mint after, never
  before.** Drafted in the same gate as R-1 because the trained-inference case is common to both.
- **R-3** — `DDD-measure-06` is contradicted by its own companion projection. Report verbatim
  first — statement, region, evidence note, falsifier, status, and the measure note's §7 as merged —
  then propose the narrowed statement and a re-examined status. **The status is Emil's to rule.**
- **R-4** — the closure ladder's axis error is **recorded as a constraint on Q32's eventual filing**,
  not repaired. It is Paper A prose and repairs at the paper's revision.

**Untouched: the seam guard.** It is correctly ratified and orthogonal to these overlaps. The
manifest records that an external reader met the guard and still reported "determined never, by
nobody" as conflicting — a finding about the guard's audience, not its content.

**Supersession, never rewriting**, for ratified text (`DDD-dec-09`, `DDD-dec-10`, `DDD-dec-15`).

**Out of scope, not to be bundled:** the ground audit and migration (Phase 1b, item 5); the
status/kind separation (item 4); the measure's decoder repair (item 8 — arrangement-relative
admissibility, explicitly not attempted); the Q-wave; the primer; Paper A's revision in all its
parts; the carve; the freight successor list.

---

Read prompt-phase1a.md in its entirety — this session follows it exactly, including every gate.

This is Phase 1a: two claim-level repairs from the Paper A external review, taken now because both
are cheapest now. DDD-frame-15's four discharge modes do not partition (declared defaults overlap
filed decisions; a thermostat reads ground at the act under a rule fixed beforehand; trained
inference is policy, standing encoding and judgment at once), and residual discretion conflates four
phenomena. DDD-measure-06 still carries a boundary claim at established that its own companion
projection — the measure note's revised §7 — concedes in both directions.

First act, before anything else: commit this prompt and bootstrap to
meta/sessions/2026-08-23-phase1a/ in decision-driven-design, per DDD-dec-20.

Fetch both repos at head — actor-indexed-determination at v5.9.0 (verify and report the tag found)
and decision-driven-design at head.

Rules that override anything you might infer:
- Interactive canon curation. Stop at every gate for Emil's ruling. Merge nothing.
- Supersession, never rewriting, for ratified text (DDD-dec-09, DDD-dec-10, DDD-dec-15).
- R-1's disposition — priority rule or orthogonal axes — must be tested against six cases BEFORE it
  is proposed: trained inference, lookup tables, declared defaults, randomised search with checking,
  abstention, timeout. A disposition that cannot classify all six exactly once is not ready.
- Residual discretion separates into four phenomena first; minting comes after the separation, never
  before.
- DDD-measure-06: report statement, region, evidence note, falsifier and status verbatim alongside
  the measure note's §7 as merged, then propose. The status proposal is Emil's to rule.
- The seam guard is untouched. The closure ladder's axis error is recorded as a constraint on Q32's
  eventual filing, not repaired here — it is Paper A prose.
- The decoder repair (arrangement-relative admissibility) is out of scope. Do not attempt it.
- State the predicted W6/W7 result before any pin operation, per the convention.
- Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

Begin with step 1 and end your first report at GATE 1: the verbatim survey, every dependent node,
and the proposed dispositions for R-1 and R-3.
