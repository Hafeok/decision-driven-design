# GATE 2 report — Batch Q drafted (draft-pending-ruling)

Upstream commit: `dba00c5` on `claude/wave3-principle-filings-edewf2`. Validators at the draft:
`validate-core-order.py` 0 errors; 54 claims valid. All five claims file `projected` with the
derivation as evidence, bodies marked DRAFT-PENDING-RULING. Order followed: Q-E → Q-D → Q-A →
Q-B → Q-F; Q-C files as one exposition paragraph, not a claim.

## The filings

| Item | Node | Terms | Home |
|---|---|---|---|
| Q-E | `DDD-frame-13` | `term:determinable`, `term:determinate` (draft) | `core/00` §4a |
| Q-D | `DDD-frame-14` | `term:outcome` (draft) | `core/09` §7a |
| Q-A | `DDD-frame-15` | — | `core/13` §4 |
| Q-B | `DDD-frame-16` | — | `core/13` §4 |
| Q-C | exposition paragraph | — | `core/13` §4, closing paragraph |
| Q-F | `DDD-ground-05` | — | `core/00` §4a (corollary) |

## The seam-guard sentence (Q-A), verbatim, for line-level scrutiny

From `core/13` §4 (the claim's region carries the same content):

> **The seam this claim must not cross.** The four supply modes partition **discharge** — the
> production of a determinate at the act. They do not partition **governance-supply**, and the
> store partition (`{rule, check, actor, nothing}` — no fifth source) is not this partition
> under new names: there, escape is *nothing*, because the question is what governance supplied,
> and nothing did; here, the same act's demand is discharged by an *uncontrolled draw*, because
> the question is what the world produced, and the world never produces nothing. A check,
> likewise, is an assurance position, not a discharge mode. The two partitions answer different
> questions about the same act, and neither reduces to the other.

## Derivation-check outcomes, per the discipline

- **Q-E:** clean. Premises admission-test / granularity-bound / verdict; falsifier spot-check
  run against canonical uses of demand (conservation, verdict, seam-information, cost-05) —
  none resists the parse. Locators verified at Gate 1 and carried in `credits`.
- **Q-D:** clean. The one drafting judgment for the ruling: statement carries the register
  split *and* the diachronic consequence in one sentence — the falsifier tests the consequence,
  so I kept it; a split files the consequence as its own claim citing this one if preferred.
- **Q-A:** clean, with two things surfaced rather than smoothed. (1) The luck ruling is
  restated as a stated step with provenance (rev18 correction 1, unratified); the ruling's own
  wording "a drawn verdict" is corrected to "a drawn outcome" under frame-14's registers — the
  rewording is reported in the notes. (2) Source-material divergence: foundation §4.1's four
  resolution sources do not map 1:1 onto the four modes (its third mixes declared defaults with
  uncontrolled dynamics; its fourth, non-resolution, is not a discharge mode under frame-14).
  The claim splits the third along the luck ruling's line and absorbs the fourth into the draw;
  canon governs, divergence recorded in the claim's notes.
- **Q-B:** clean. Aggregate formal content (N·H(V), correlation inequality) explicitly
  regioned out to the measure paper per the rev18 routing.
- **Q-F:** clean. Priority stated as logical-per-act, not temporal ceremony; the symmetry
  (ground prior in constitution, decisions prior in history) carried in the statement so the
  bootstrap is not circular; ground-01's gate cited as the mechanical form.

## Dispositions asked of the ruling

1. **The seam guard** — as drafted above, in both the doc prose and frame-15's region.
2. **Q-D's one-sentence statement** — keep the diachronic consequence in the statement
   (recommendation) or split.
3. **W1 disposition** — `term:outcome` adds 7 advisory W1 warnings (docs 00–07 use the word;
   the linter now sees the term). Options: accept as honest forward pointers; suppress via the
   `instances:` contract field per doc; or rename the term (not recommended — "outcome" is the
   ruled name). Errors are zero either way.
4. **Term statuses** — the three new terms enter `draft`; whether they settle at PR acceptance
   (ratification) or await a later act is the ruling's.
5. **13 §5 amendment** — the old closer's maturation clause now points at `core/09` §7a
   (frame-14 names the consuming-side consequence in canon); one clause changed, reported here.
6. **Downstream annotation** (cost-16 naming frame-14 as its mechanism) — staged for the
   downstream commit at Gate 5, per the citation-scope convention.
