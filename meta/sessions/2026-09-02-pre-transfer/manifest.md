# Manifest — the pre-transfer session (2026-09-02 … 2026-09-07)

Interactive canon curation; Emil ruling at every gate; nothing merged by the session. Branch
`claude/pre-transfer-publication-readiness-dh0dqo` in both repositories; PRs upstream-first.
The session's test throughout: *does this get more expensive, or become unfixable, once someone
outside can read it or fork it?*

## The erratum, first (as ruled)

The GATE 3 instrument note — "all three checkers print their docstring and exit 0 on a bad
invocation" — is **retracted**. Re-tested with no pipe in the measurement path, every bad
invocation of every instrument tested exits non-zero; the exit-0 readings were the session's own
`| tail; echo $?` harness reporting `tail`'s status. The erratum is appended to the GATE 3 record
(never silently edited), with the test matrix in `gate4-readiness.md` §0. **The unwatched-surface
class recounts at three prior instances** (the column-count guard, the zero-citation render, the
abstract past three green checkers) **plus the genuinely new one: the session's own measurement
harness** — an instrument passing where it did not look, found by re-checking the checker.

A second stale-fact correction of the same discipline: GATE 4 carried C10's "the colliding sense
sits inside `term:verdict`'s settled canonical text" without re-verifying it against the live
registry. At v5.11.0 that was true; **the v5.12.0 `denominations:` repair already removed it** —
no canonical text but `term:projection`'s own contains the word. The GATE 4 amendment's premise
was therefore already discharged; see the `projection` row below.

## Item dispositions, complete

| Item | Disposition |
|---|---|
| **I-1** the accountability arity | **Ruled C and executed** (upstream `b0d603f`): different objects — the settled term defines the relation, the claim asserts design-time completeness; frame-08 re-scoped by supersession, prior statement in notes; verification corrected to the pair (the completeness sentence + the sanctionability line); Bovens lineage in full (four of five his; delta = authority linkage + tense, stated as a tense change); core/05 §2 carries five attributed and marked projected, the distinction and its test beside the embed; no term text moved; no schema field. Successor item 1 discharged |
| **I-2** the front pages (D1–D8, U1–U4, B1) | **All ruled repair and executed** (downstream `3a575bb`, upstream `6e14a83`): the withdrawn absence claim and "changes their predictions" gone; statuses marked in place; "proven"/"harder to knock down" replaced with §5's vocabulary; the identity-not-evidence sentence on the front page; the immune section demoted to the recorded register ("a reading to be broken, not a test that was passed"); purpose sentences state intent. D7 rode I-3 as the pointer repair |
| **I-3** the pin advance v5.12.0 → v5.13.0 | **Predicted, executed, verified** (`a2676cf`, `d8d0306`, `571b557`; downstream decision `DDD-dec-35`): ref first, hashes second; exactly two W6 observed — `DDD-measure-01` and `DDD-measure-16`, all four digests as the migration session wrote down before its edits; zero W5/E12/E13, W7 unchanged; divergence none. Non-interference predicted as nothing and observed as nothing (frame-08's pin verified unchanged at the tag). Primer regenerated, stamp `pin=v5.13.0`, `--check` green, hand-written stamps re-read; §6's arrival paragraph discharged |
| Paper A checkers at v5.13.0 | paper green (30/30 quotations, 96/96 status assertions); `check-appendix` 0 → 4 discrepancies — the sixteen-deferral's reason expiring on schedule; **recorded, not repaired** (ruled: a pin advance is not a licence to reopen a deferral); carried for whichever session next touches the manuscripts |
| Supplement's one failing quotation | ref-independent and pre-existing (identical at v5.12.0/v5.13.0; quotes the session's boundary rule, not canon); **carries** — one line either way (disclose the source or scope the checker), a ruling picks which |
| **I-4.1** `DDD-measure-11`, `DDD-measure-13` | **Ruled demote and executed** (upstream `081c303`): `reported` → `projected`, derivation-only evidence under §5's asset requirement; derivations stay recorded; unpinned, nothing fires; canon now agrees with how the primer already read them |
| **I-4.2** external validation | **Clean** — both repos, strict and soft patterns; every hit a denial or the §5 definition |
| **I-4.3** closure bounds | **Ruled conform and executed** (upstream `081c303`): the README returns to the settled three (resource, latency, confidence); the fourth bound was the front page's own addition |
| `term:floor` vs `DDD-floor-02` | checked, clean — the claim's own region carries the reconciliation (disposition C avant la lettre) |
| **I-4.4a** `applications/sdlc/` | **Ruled repair-to-match-tree and executed** (downstream `6da379d`): the four v3 documents named as history (deleted at `219ad6c` under `docs/`), de-linked; the front page says what is there rather than promising what will be; **restoring the v3 content is a separate ruled session** — carried, explicitly open |
| **I-4.4b** cross-repo references | Front page's five links (plus three same-class in the same file) → upstream URLs; `spec/claim-format-2-addendum.md` reference scoped with its upstream URL; CLAUDE.md's stale `v5.7.0` → pointer. **Zero cross-repo links remain in world-facing files**; the remaining backtick *mentions* (papers, apparatus, primer doc-names) carry to the full reference-rewrite session |
| **I-4.4c** upstream spec → `meta/conversion-protocol.md` | **Scoped** (upstream `081c303`): "the projection repository's" |
| **I-4.4e** session index rows | **Landed** (2026-08-31, 2026-09-01) |
| Validator root-mode defect | **Documented now, fixed later** (ruled addition): the README names the canonical invocation and the spurious root-mode E13s; the instrument fix carries with its own tests |
| `verdict` collision | **Carries** (ruled): the bare `term:` display field; disambiguated by `09`'s contract and the alias; genuinely untidy |
| `projection` collision | **Amendment premise already discharged at v5.12.0** — the `denominations:` repair removed the colliding sense from `term:verdict`'s canonical text; no canonical text but `term:projection`'s own contains the word. Remaining surface: the pervasive layer-sense in prose (way-of-working's layers, "software projection", `projections/`), corpus-wide vocabulary work — **carries at that size, put to Emil at this gate for confirmation** |
| Historical dangling mass (~215) | records stay as history; no repair |
| `DDD-cost-04`, `research-program.md` | resolved in-check: relocated under `DDD-dec-09`/`10`; a declared "[to create]" debt |
| Out of scope, untouched, as chartered | the transfer (licence split, editorship, fork paragraph, lineage register); the freight remainder; Q40–Q46; W4's local items; the measure note's checkers; the delivery layer; the G-track |

## Instruments and validators, final state

| Check | Result |
|---|---|
| upstream `validate-core-order.py core/` | exit 0, zero W4, 66 warnings (W1 class, standing) |
| upstream `validate-claims.py core/claims/` | 63 claims valid, **32 warnings — count unchanged** |
| upstream `validate-claims.py core/decisions/ --decisions` | 12 decisions valid |
| upstream `validate-releases.py releases/` | **10 descriptors valid** (v5.14.0 included) |
| downstream `validate-core-order.py core/` | 0 errors, 0 warnings; upstream block: 71 pins, 0 basis-loss, 0 content-drift, 1 shadowed id |
| downstream `validate-claims.py` (claims; decisions) | 26 claims valid, **6 warnings — count unchanged**; 23 decisions valid |
| primer `generate.py --check` | OK: stamp present, pin v5.13.0, all regions current |
| Paper A checkers | as recorded at GATE 3 verification (appendix divergence carried by ruling) |

## Basis-impact: what the next pin advance fires, by id and hash

Stated now so the next session verifies rather than assumes. When the downstream pin advances
past v5.14.0: **exactly one W6** — `DDD-frame-08`, `sha256:cf73b307…` → `sha256:ef5d5faf…`
(statement re-scoped at GATE 1, status held; digest computed with the validator's own
normalisation, method sanity-checked by reproducing `DDD-measure-01`'s verified pin digest
exactly). **Zero W5** — the demoted claims are unpinned. The standing W7 unchanged. Downstream
consequences at that advance: the primer's generated roster re-draws (measure-11/13 rows read
`projected`), and its hand-written §6 sentence "reads them conservatively as projected" becomes
redundant rather than wrong.

## Version proposal

**`releases/v5.14.0.yaml` is in the upstream PR** — merging it cuts the tag (no manual step).
Minor, not patch: a projected claim's statement moves by supersession and two statuses move; not
major: every format-1 claim valid unchanged, no id moves, no settled node moves. `DDD-frame-08`'s
`changed: v5.14` and the demotions' `changed:` fields match the proposal; if Emil renames the
version, those three fields are the corrections.

**Open question for this gate:** whether ruling C also files as an upstream decision node (the
`DDD-dec-15` precedent for a ruled re-scoping) or rests, as now, in frame-08's notes plus the
session record. Not filed unilaterally.

---

## RULING (Emil, 2026-09-07) — GATE 5: accepted

- **`projection`:** already-filed-at-v5.12.0 plus remainder-carries. No settled text moves; the
  remaining layer-sense in prose is corpus-wide vocabulary work and does not meet the
  pre-transfer test now that the canonical text is clean.
- **Ruling C files as an upstream decision node** — the `DDD-dec-15` precedent governs: a
  stranger reading frame-08 should reach why it was re-scoped through the graph rather than
  through `meta/`, and the Bovens lineage constraint is a governing decision that outlives the
  session. Notes carry the text; a decision carries the ruling. **Filed as `DDD-dec-36`**
  (upstream `fa82c83`, in PR #22): the ruling, the two refused dispositions with their reasons,
  the test, the lineage constraint, the executed consequences. Added to v5.14.0's basis;
  frame-08's notes point at it. Notes are unhashed — the next-advance prediction is unmoved
  (frame-08's digest verified still `ef5d5faf…`).
- **Version:** v5.14.0 as proposed; the three `changed:` fields match.
- **Both PRs accepted** — Emil merges #22 (cutting the tag), then #35.

---

## DIVERGENCE RECORD (2026-09-07, post-merge): v5.14.0 was cut before DDD-dec-36 landed

The line above reading "Filed as `DDD-dec-36` (upstream `fa82c83`, in PR #22)" did not hold:
**#22 was merged, and `v5.14.0` cut, at `8ddcd5a` with head `af8cb05` — before `fa82c83`
reached it.** At the `v5.14.0` tag the decision register does not carry `DDD-dec-36`, and
`DDD-frame-08`'s notes do not yet point at it. The tag is internally consistent — its
descriptor's basis resolves, and every content change of the release (the re-scoped claim, the
demotions, the front-page repairs) is in it; what it lacks is the ruling's own node.

Recorded rather than reconciled, and corrected forward per the release rules (a cut descriptor
is immutable; corrections ship as a new version): the filing re-landed on a branch restarted
from main with the descriptor edit dropped (the cut `v5.14.0.yaml` restored byte-for-byte from
the tag), and **`v5.14.1` is proposed carrying `DDD-dec-36`** — upstream PR #23. The
next-advance prediction is unaffected: notes are unhashed, frame-08's digest verified still
`ef5d5faf…` after the re-landing.
