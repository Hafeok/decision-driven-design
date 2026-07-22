# v4.2 Patch Application Report

Applied per `PATCH.md` in the v4.2 patch package. All new files were copied verbatim
(byte-identical to the package, verified with `diff`). No prose, numbers, tables, or equations in
`core/09-the-floor-mechanism.md` or `apparatus/the-skill-floor.md` were altered. This file
replaces the v4.1 report, which remains available in git history.

## 1. Prerequisite check

`core/08-the-measure.md` **existed** before any patch action was taken (v4.1 is applied), so
`core/09`'s cross-references to it resolve. Proceeded.

## 2. Script verification — both ran; boundary values exact

- `python3 core/assets/floor-mechanism.py` — ran clean (exit 0). Hard-capacity table shows
  escape 0.000 only at C=40 with escape and retries rising together as C falls, and the
  **all-verified (`n_B=0`) case shows escape = 0 at every capacity, including C=0**
  (`check: all-verified at C=0 -> escape=0.000`) — overflow alone is retries, not floor. ✔
- `python3 core/assets/perr-rate-distortion.py` — ran clean (exit 0). Derived bound prints
  **p_err = 0.0000 at r = 1.000** and **p_err = 0.5000 at r = 0.000**, exactly the required
  boundary values; both structural re-runs print STRUCTURE SURVIVES. ✔
- The tables in `core/09` §3, §4.1, and §4.2 match the script outputs figure-for-figure
  (e.g. 2.49/2.51 at C=30; p_err 0.0130 at r=0.90; escape 6.96 → 2.70 → 0.00 on the
  fixed-budget encode shift).

## 3. Attribution merge — merged AND deleted

- **Merged.** The full contents of `meta/lineage-addendum-v41-v42.md` are now in
  `meta/lineage-and-limits.md`: the addendum preamble and governing sentence, sections
  **§1.8** (Shannon, information theory), **§1.9** (Shannon, rate-distortion), **§1.10**
  (Cover & Thomas), **§1.11** (hallucination taxonomies), the "Additional context worth
  acknowledging" block (Kolmogorov/MDL; Simon/Sims), and "The register sentence, for every
  future write-up" — inserted between §1.7 and §2, with heading levels matched to the file's
  existing `### 1.x` style. The **§6 citation table** was extended with all seven addendum rows
  (Shannon 1948 ×2, Shannon 1959, Sims 2003/Simon 1955, Ji/Huang 2023, Xu et al./Kalai &
  Vempala, Kolmogorov/MDL).
- **Governing sentence survives verbatim:** "The mathematics is Shannon's. The claim is the
  *identification* — that specification demand *is* verdict entropy, seam demand *is* mutual
  information, and resolve-overflow error *is* the rate-distortion bound. …" — present once, in
  the §1.8 preamble blockquote.
- **Deleted.** `meta/lineage-addendum-v41-v42.md` was removed after the merge. The attribution
  now lives in exactly one place.
- One adaptation, disclosed: the addendum's delivery-vehicle framing (its title and its
  "**Location:** append to…" line) was dropped, and its lead-in label "**Why this exists.**" —
  which referred to the addendum file itself — became "**Why §1.8–§1.11 exist.**" so the merged
  text has an antecedent. Every sentence after the label is verbatim.

## 4. Ledger edits to `meta/consolidated-state.md` — all three landed

All three sub-edits are present in §5, verified in the final file:

**(a) CLOSED — the p_err item** (note: the pre-patch ledger carried no literal "soft error
curve is assumed" line — PATCH.md's wording anticipates this with "If the open-items list
carries…" — so the closure entry was added to the open-items list as the record of closure):

> - The soft error model p_err. **CLOSED (v4.2).** Derived from binary rate-distortion:
>   p_err = H_b^-1(1 - C/n), the information-theoretic lower bound on per-decision error at
>   available rate r = C/n. Limits are exact (r>=1 -> 0; r->0 -> 0.5, recovering the hard-case
>   coin flip). Substituting it for the earlier assumed logistic changes the numbers and no
>   structural claim. See core/09 §4.1.

**(b) RECLASSIFIED — restated, not deleted.** The entry asking for demand measurement on open
predicates (the open-predicate residual of §5's former item 1, the counting-procedure debt) was
**replaced** with the stated-boundary entry, reasoning intact:

> - Measuring demand on OPEN predicates. **NOT A DEBT — A STATED BOUNDARY.** core/08 measures
>   demand as verdict entropy, which requires a verdict function; an open predicate is precisely
>   one that lacks it. Asking to measure demand there is asking for entropy without a random
>   variable. Measurement and closure have the same domain (core/08 §7). This is the framework's
>   limit, correctly drawn, and it coincides exactly with the floor. It should not appear on the
>   ledger as unpaid work.

The remaining numbered debts (operationalise closure; selection/training ratio) were renumbered
1–2; the closing-predicate discharge remains recorded inside the replacement text ("core/08
measures demand as verdict entropy") and in CHANGELOG 4.1.

**(c) ADDED — the new open item:**

> - Calibrating C_resolve and C_hold for a real actor. EMPIRICAL, not a proof: construct tasks of
>   known bit-demand, find where error rate departs from zero; that value is C_resolve for that
>   actor. Nobody has published such a measurement. Needs a rig, not more theory. This is now the
>   framework's principal open empirical item, alongside the selection/training study.

## 5. Dead-link check — no dead links

Neither new doc uses `[…](…)` markdown links; all internal references are backtick path/section
references. Every referenced target was checked and exists:

- `core/09-the-floor-mechanism.md` references: `core/03`, `core/05`, `core/06`, `core/08`
  (including `core/08` §7, which exists: "Where the measure stops"), `core/01` (via skill-floor),
  `apparatus/closure-principle.md`, `apparatus/the-skill-floor.md`, `assets/floor-mechanism.py`,
  `assets/perr-rate-distortion.py` (both relative to `core/`) — all resolve.
- `apparatus/the-skill-floor.md` references: `core/01`, `core/03`, `core/05`,
  `apparatus/encode-verify.md`, `apparatus/closure-principle.md`, `applications/sdlc` — all
  resolve.
- The new README rows link to `core/09-the-floor-mechanism.md` and `apparatus/the-skill-floor.md`
  — both resolve.

**Dead links found: none.** One non-link mention: `apparatus/the-skill-floor.md` cites
"`ground-prd`", which is not a file in this repository — a pre-existing pattern
(`meta/consolidated-state.md` §5 already references `ground-prd.md`); backtick mention, not a
markdown link, left as shipped.

## 6. Flagged but not changed

- **`meta/consolidated-state.md` §5, the judgment/escape-split bullet** still ends "Not yet done —
  the natural next result." `core/09` §7 now closes exactly that seam, so the bullet is arguably
  stale — but PATCH.md §4 specifies only sub-edits (a), (b), (c) and does not touch this bullet,
  so it was left as-is.
- **`core/09` §4 heading uses "law"** ("The soft-capacity law"). This is the shipped document's
  own text, sanctioned by PATCH.md ("the soft law with `p_err` derived from rate-distortion"),
  copied verbatim per the hard constraint. None of the wiring or ledger text added by this patch
  uses "law" for the framework's claim; the CHANGELOG "law" hits are the historical 4.0/4.1
  entries.
- **`apparatus/README.md`** closing line still reads "All three are instances of one discipline…"
  though the index now lists four documents. PATCH.md specifies only the added index line; left
  as-is.
- **`README.md` "Status" / "What this is, and is not"** carry-overs flagged in the v4.1 report
  (the "no measurable unit" sentence; the counting-procedure debt as "most important") remain, and
  are not in PATCH.md's v4.2 edit list; left as-is.
- No number, table, or equation discrepancies were found between the new docs and the script
  outputs — nothing to report under the copy-error rule.

## Summary

The v4.2 patch applied cleanly on a verified v4.1 base: `core/09-the-floor-mechanism.md`,
`apparatus/the-skill-floor.md`, and the two reproduction scripts were dropped in byte-identical
to the package; the README, core index, and apparatus index were wired with PATCH.md's exact
rows; the attribution addendum was merged into `meta/lineage-and-limits.md` as §1.8–§1.11 plus
seven §6 citation rows — with the governing "The mathematics is Shannon's…" sentence surviving
verbatim — and the addendum file was then deleted; all three consolidated-state ledger sub-edits
landed (p_err CLOSED, open-predicate measurement RECLASSIFIED as a stated boundary rather than
deleted, and the C_resolve/C_hold calibration item ADDED as the principal open empirical item);
and the v4.2 changelog entry was added with its Attribution and Reclassified subsections. Both
scripts run on stdlib Python with the exact required boundary behaviour — escape is zero for the
all-verified case at every capacity, and the derived p_err is 0.0000 at r ≥ 1.0 and 0.5000 at
r = 0 — every internal reference in the new documents resolves, and the register is unchanged:
the framework's own claim remains a principle, with "law" appearing only in the shipped
documents' homage sense.
