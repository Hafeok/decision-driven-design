# GATE 2 — M-1 drafted

**draft-pending-ruling.** Held for line-level ratification. Nothing merged; no claim filed in
either repository.

Commits: upstream `2586c4b` (the asset), downstream `690ff02` (the section and the renumber).

---

## 1. The asset — built first, as licensed

`core/assets/measure-aggregate-discharge.py`, landed beside the other five. It **reproduces**,
and it carries its content as **assertions** rather than as printed claims, so it fails loudly if
the arithmetic ever stops holding:

| Assertion | What it guards |
|---|---|
| per-act baselines × `n` = 25.493 / 20.593 / 4.901 | the aggregate rests on §4's decomposition A and introduces no new task |
| `H(V₁…V_N) ≤ N·H(V)` at every `N` | subadditivity |
| i.i.d. control returns `N·H(V)` to floating point | the equality limb — **computed, not stated** |
| gap `= 0` at `N = 1` | a batch of one is not correlated |
| `I(V₁…V_N;M) ∈ [0, H(M)]` | the withheld term is a one-off and cannot grow |

Entropies are exact and computed in log space — nothing is sampled, so there is no estimator
story to tell and no error bar to report. Upstream validators after the add: **0 errors, 0 W4**.

## 2. The renumber — and a correction to my Gate 1 estimate

I reported 19 cross-references at Gate 1. **The true number is 16**, and the discrepancy is worth
recording because it was a trap rather than a miscount: three of the five `§7` hits and *all five*
`§11` hits are **Ashby's own section numbers** — `§7/7`, `§11/7`, `§11/9` — not this paper's
sections. Renumbering them would have corrupted the Ashby citations in §9 and the References.

The substitution excludes any `§N` followed by `/`, and I verified all five Ashby references
survive byte-identical. Seven headings moved. **A sweep confirms every `§`-reference in the
manuscript now resolves to a heading that exists** — zero dangling.

## 3. The section

§6, six subsections, 1,229 prose words. Structure as ratified at Gate 1:

- **§6.1 Discharge is act-indexed** — `DDD-frame-16` cited, §2's Scale paragraph **cited and not
  restated**, the unit fixed by `term:act-individuation` (*batch boundaries are verdict
  boundaries*), which is what licenses §6.3's batch model.
- **§6.2 Aggregate demand over `N` acts** — opens by separating **`N` from `n`**, then quotes §2's
  settled reading of `nH(V)` (*the entropy of `n` independent draws*) and **builds from it**. The
  paragraph is written so a reader who remembers the `nH(V)` correction sees it being used.
- **§6.3 The correlation inequality** — **first sentence is "The theorem is Shannon's."** Then:
  nothing here strengthens or tests it, and if the reading fails the inequality is untouched.
  Then the reading, then the worked table, then the seam identification.
- **§6.4 The `O(1)`/`O(N)` asymmetry** — the algebra `gap = N·I(V;M) − I(V₁…V_N;M)` with the
  subtracted term bounded by `H(M) = 2` bits. **Stays in the demand register**: it points at
  §2.1 and `DDD-cost-06/07` for pricing and computes no crossover.
- **§6.5 Where demand comes due** — Q-C's exposition, one paragraph, **explicitly not a claim**,
  in canon's own posture (`core/13` §4 carries it the same way).
- **§6.6 What this section does not claim** — below.

**The centre of the section, and the reason it belongs to this paper:** the gap is §4's seam.
Per act `H(V) = 0.205593`, `H(V|M) = 0.166070`, `I(V;M) = 0.039523`; times `n = 124` those are
25.493 / 20.593 / 4.901. The seam a decomposition **pre-pays** in §4 is the quantity a correlated
run **amortises** in §6 — the same object from the direction of repetition rather than
decomposition. No new machinery.

## 4. The honesty paragraph, and the two identifications

§6.6 states three things and concedes on the third:

1. The inequality is Shannon's; computing it establishes nothing about the framework — *the same
   discipline §7 applies to the identity applies here, and for the same reason.*
2. **The modelling claim is a *second* identification**, layered on §2's and **not implied by
   it**. §2 identified demand with verdict entropy; §6 additionally reads the gap as amortisable
   work. *The first identification could hold while the second fails, and a reader is entitled to
   the distinction.*
3. The correspondence — do measured verdict correlations predict realised amortisation? — is
   **untested**, with `DDD-measure-07`'s falsifier shape: if runs with a large measured gap
   reliably show no more amortisation than runs with a small one, the second identification is
   wrong and Shannon is untouched.

The section closes on the concession, not on the result: *"Whether that gap is the thing engineers
recover when they cache is open, stated, and untested here."*

**Nothing is filed.** The second identification is register-native with its falsifier stated, and
the gap is flagged.

## 5. Reviewed text touched — two places, both pre-ruled

- **§7's honesty table gains one row** — for the second identification, **not** for an instance
  count. *"Five worked instances"* stands unchanged in §5.5, §7's last row, caveat 4 and the
  abstract, per R-1.
- **Reproduction** extends to six scripts and records what the new asset asserts.

## 6. Length — the ceiling question, put explicitly

| | Before | After | Δ |
|---|---|---|---|
| Prose words (tables excluded) | 7,443 | **8,738** | +1,295 |
| §6 alone | — | 1,229 | — |

**This lands past the 8,300 you named, so I am raising it rather than letting it drift.**

My Gate 1 estimate of 700–900 words for §6 was wrong by about 40%. I am not going to dress that
up: I under-estimated, and the section as outlined at Gate 1 could not have been written to 900
words without dropping something you ratified. What §6 actually carries is a cited primitive, a
notation distinction, a theorem with a worked table and the seam identification, an asymmetry
with its algebra, an exposition paragraph, and a full honesty subsection covering two
identifications and a falsifier. Reading it back, I do not find padding to cut — the subsection
weights (§6.3 at 287 and §6.6 at 270, everything else 87–194) sit where the content is.

**Three options, and my recommendation is the first:**

1. **Accept 8,738.** The growth is one ratified section plus one table row. No reviewed content
   is trimmed to pay for it, which you ruled out anyway.
2. **Trim §6 only**, at the cost of the seam-identification paragraph or part of §6.4's algebra —
   I would be cutting the two things that make the section belong to this paper.
3. **Reopen the target band** in the context doc, which currently records 5,000–7,000 against a
   manuscript that passed 7,000 at the review revision, before this session.

Option 3 may be worth doing regardless of 1 or 2: **the band is already stale by the review's own
merge**, not by this session's work.

## 7. Corrections and carried items

- **Commit `690ff02`'s body quotes 8,723 / 1,214.** Those figures were measured before three
  line-level wording fixes in §6.3 that I made in the same working tree; the committed text is
  8,738 / 1,229. The message understates its own content by 15 words. Recorded rather than
  rewritten — the numbers above are the ones of record.
- **`N` is used in §9's MDL paragraph and §7's table but is not in §2's Notation list.** §6.2 now
  defines it in place. Adding `N` to §2's notation paragraph would satisfy the *notation stated
  once* convention properly. **Not done** — it touches reviewed text outside this gate's scope.
  Proposed for Gate 4 as apparatus.
- **Appendix A will need rows for `DDD-frame-16` and `term:act-individuation`**, both newly cited
  by §6. Booked for M-4 with the three verbatim refreshes.
- **R-5 (the two `DDD-cost-05` body sites) is queued for Gate 3** with M-3, per the walk. Not
  touched here.

## 8. Gate 3 preview

M-2's §8 refinement (constructive closure — now §8, post-renumber) and M-3's upgrades U-1, U-2,
U-3, U-4, U-6, plus R-5's two repairs, as diffs.
