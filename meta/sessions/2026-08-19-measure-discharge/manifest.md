# Manifest — the measure note: the discharge section (2026-08-19)

Session type: interactive paper drafting, five gates, Emil ruling at each. **Projection work
throughout — no claim was filed in either repository.** Merged by Emil.

- **Branch (both repos):** `claude/measure-discharge-section-o0y0f7`
- **Bases:** upstream `4d0d177` (= `v5.7.0`); downstream `8e348ce`
- **Prompt identity:** 128 lines, sha256 `bd30d4e8…95a40b02`, committed as the session's first act
  per `DDD-dec-20`

---

## What landed

### Upstream — `actor-indexed-determination`

| File | Change |
|---|---|
| `core/assets/measure-aggregate-discharge.py` | **new** — the sixth measure asset |

Nothing else upstream. No claim, no term, no decision, no release descriptor.

### Downstream — `decision-driven-design`

| File | Change |
|---|---|
| `papers/measure-note/measure-note.md` | new §6; §6–§10 renumbered to §7–§11; §8 refinement; five citation upgrades; two repairs; pin advance; Appendix A regenerated; `N` into Notation |
| `papers/measure-note/measure-paper-context.md` | regenerated as **v3** |
| `meta/sessions/2026-08-19-measure-discharge/` | prompt, bootstrap, five gate reports, this manifest |
| `meta/sessions/README.md` | index row |

## The five items

| | Item | Outcome |
|---|---|---|
| **M-1** | The discharge section | **§6 "Discharge over many acts"**, 1,229 words, six subsections, with a new reproducing asset |
| **M-2** | §8 constructive-closure refinement | **Drafted, gap flagged, nothing filed** — canon carries no constructive/verification split |
| **M-3** | Citation upgrades | **Five applied** (U-1, U-2, U-3, U-4, U-6); U-5 dropped as a marker with no work to do |
| **M-4** | Front matter and Appendix A | Pin to **`v5.7.0` / `v0.4.0`**; Appendix A **20→27 claims, 15→17 terms**, regenerated from the graph |
| **M-5** | Context doc v3 | Rewritten, superseding v2 |

## Verification at close

| Check | Result |
|---|---|
| Upstream `validate-core-order.py` | 0 errors, **0 W4** |
| Upstream `validate-claims.py` | 60 claims valid |
| Upstream `validate-claims.py --decisions` | 7 decisions valid |
| Upstream `validate-releases.py` | 3 descriptors valid |
| Downstream `validate-core-order.py` | 0 errors, 0 warnings |
| Downstream claims / decisions | 25 claims, 18 decisions valid |
| All six assets, fresh run | **all reproduce, exit 0** |
| Stated figures vs fresh output | **35/35 found** |
| Reference closure (27 claims, 17 terms) | **clean** |
| Appendix A verbatim against the graph | **44/44** |
| Dangling section references | **none** |
| Stale pin references | **none** |
| Pending-node flags remaining | **1** — the genuinely open one |

## Length

7,443 → **9,122** prose words (tables excluded; 9,662 including). Every increment is booked
content: §6 (+1,295), the §8 refinement (+319), M-4's apparatus (+65). The five upgrades and two
repairs net **−4**. Method recorded in context v3 so future counts are comparable.

---

## Findings worth carrying

**The Ashby renumbering hazard.** The Gate 1 estimate of 19 cross-references was wrong: the true
count is **16**. Three of five `§7` hits and all five `§11` hits are **Ashby's own section
numbers** (`§7/7`, `§11/7`, `§11/9`), inside the citations the external review specifically made
us verify. A naive substitution would have silently corrupted them. The rule — exclude `§N`
followed by `/` — is now a **working convention in context v3**, where the next renumber will find
it without this session's context.

**The pin could not be made uniformly true.** `measure-aggregate-discharge.py` does not exist at
`v5.7.0`; it was created this session. The old front-matter sentence pinned *"claim identifiers
and the assets named under Reproduction"* — left as written, it would have been **false**. The
front matter now pins claim identifiers and defers assets to Reproduction, which states the split.
An upstream release descriptor would have let it pin uniformly; that was **raised and deliberately
not taken** (do-not-bundle).

**Appendix A is now generated, not edited.** Regenerating both tables wholesale from the graph
makes every row verbatim by construction and corrects drifted rows in the same pass that adds new
ones. **Standing convention**, recorded in context v3.

**Three canon drifts from `v5.6.0` were carried by the manuscript**, all found at Gate 1:
`term:verdict`'s wording (the appendix said *decidable* where §8 argues decidability is the wrong
criterion), and the `DDD-dec-15` re-scopings of `DDD-cost-05` and `DDD-floor-01` — the first
reproduced at **two body sites**, repaired per the R-5 ruling in site-appropriate forms.

**Caveat 3 verified against `DDD-frame-15`/`16` and unchanged.** Those claims partition
*discharge*; the caveat cleaves *within the residual*. Reported, not rewritten; the check is filed
in context v3 so it need not be redone.

---

## Open items this session created or carried

| Item | Home |
|---|---|
| **The constructive-closure node (Q32)** — canon carries no constructive/verification split; the word *constructive* occurs nowhere in `core/` | **Q-wave.** Not a paper session's act |
| **The sixth asset's pin** — a release descriptor cutting a tag that carries `measure-aggregate-discharge.py` would let the front matter pin uniformly | **Emil.** Absorbed by the next upstream release |
| **The second correspondence** — do measured verdict correlations predict realised amortisation? | Stated in §6.6 with its falsifier; untested |
| The first correspondence campaign; information-theorist certification; multi-actor composition | Carried unchanged in context v3 |

## For Paper A

**§6's `O(1)`/`O(N)` material is the measure-register form of *paid once, inherited by every
run*.** Where Paper A's structure treats standing against occasioned supply, it can now cite a
worked projection — with a reproducing asset behind it — rather than restate the arithmetic.
`DDD-frame-16`'s region field routed that content here deliberately, so the citation direction is
canon's own.

## Out of scope, untouched

Paper A · the correspondence campaign · the escape/judgment split's content · multi-actor
composition · the carve · the Q-wave · S-1 · G-track · any canon filing, including the Q32 node.
