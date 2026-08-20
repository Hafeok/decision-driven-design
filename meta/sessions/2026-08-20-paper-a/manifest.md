# Manifest — Paper A: the statement paper (2026-08-20)

Session type: interactive paper drafting, five gates, Emil ruling at each. **Projection work
throughout — no claim, term, decision or release descriptor was filed in either repository.**

- **Branch (downstream only):** `claude/paper-a-framework-projection-q2fxvw`
- **Bases:** upstream head `33b6d28`, canon pinned at **`v5.8.0`** = `9e92099`; downstream `aa7e135`
- **Prompt identity:** 117 lines, sha256 `875f633f…9852eb3ed`, committed as the session's first act
  per `DDD-dec-20`
- **Upstream:** **untouched.** No commit, no file, no branch. The paper is a projection and needed
  nothing from the principle repository but a pinned ref to read.

---

## What landed

| File | Change |
|---|---|
| `papers/paper-a/paper-a.md` | **new** — the manuscript, twelve sections |
| `papers/paper-a/reviewer-brief.md` | **new** — P-5, one page, aimed at the framework's natural critic |
| `papers/paper-a/check-quotations.py` | **new** — every block quotation verified against the graph |
| `papers/paper-a/gen-appendix.py` | **new** — Appendix A generated from the graph |
| `papers/paper-a/check-appendix.py` | **new** — the appendix re-read independently of its generator |
| `meta/sessions/2026-08-20-paper-a/` | prompt, bootstrap, four gate reports, successor items, this manifest |
| `meta/sessions/README.md` | index row |

## The five items

| | Item | Outcome |
|---|---|---|
| **P-1** | Structure ratification | Twelve sections against the foundation's §12, amended by everything that landed since; per-section bills of materials; both authored sections outlined |
| **P-2** | The two authored sections | **§2.4** ground provenance (479 w) and **§5.2** the closure strength ladder (642 w) — prose, not claims; **two pending-node flags, both at the point of use** |
| **P-3** | The substitution and the divergence closures | **Three closures, one hunk each** — see below |
| **P-4** | Apparatus | Pin corrected to one ref; bibliography 9 verified / 1 flagged; **Appendix A generated then independently re-read**; the H-set's six rows with `projected` and empty evidence visible |
| **P-5** | Reviewer brief | 1,017 words; names the vacuity objection as the strongest and points at four places it is pre-answered |

## P-3's three closures

| | Foundation carried | The paper carries | Where |
|---|---|---|---|
| **C-1** | §4.1's four-source table | `DDD-frame-15`'s four discharge modes, seam guard in prose; canon's own words quoted as the reason | §4.1 |
| **C-2** | §4.4's hedge, avoiding conservation "until an independently motivated measure exists" | `term:conservation` with `DDD-measure-01` as the modelling claim, `DDD-measure-02` as arithmetic, the bound via `DDD-measure-06`, `DDD-frame-11` outside it | §4.4 |
| **C-3** | §8's H5 softening of the training gate | `term:training` settled; the softening named, **declined rather than rebutted**, routed to the supersession question | §9.3 |

## Verification at close

| Check | Result |
|---|---|
| Upstream `validate-core-order.py` | 0 errors, **0 W4** (59 W1 + 7 W2 — byte-identical to the GATE 1 baseline) |
| Upstream `validate-claims.py` / `--decisions` / `validate-releases.py` | 60 claims, 8 decisions, 4 descriptors valid |
| Downstream `validate-core-order.py` | 0 errors, 0 warnings |
| Downstream claims / decisions | 26 claims, 20 decisions valid |
| `check-quotations.py` at `v5.8.0` | **29 verbatim, 0 failing** |
| `check-appendix.py` at `v5.8.0` | **72 rendered / 72 cited, 0 discrepancies** |
| Appendix generator idempotence | **byte-identical over three runs** |
| Negative controls (quotations 2, appendix 6) | **8 / 8 fail as they should** |
| Cited IDs resolving at `v5.8.0` | 48 claims + decisions, 24 terms, **all** |
| Status labels vs the graph | **0 mismatches** |
| Internal `§N.M` cross-references | **none dangling** (54 headings) |
| External references (measure note §4/§6/§7/§8/§8.2, `core/09` §3) | **all resolve** |
| Bibliographic locators | 9 verified, **1 flagged unverified in its own entry** |
| Figures minted by this paper | **none** — the five cited were re-verified against a fresh `measure-toy.py` run |
| Pending-node flags | **2**, both genuinely open |
| Upstream working tree | clean — nothing filed, nothing touched |

## Length, with the method and the sequence

Method: **prose words, tables excluded**.

| Part | Words |
|---|---|
| Front matter (title, subtitle, pin) | 121 |
| **Body — Abstract through §12** | **10,992** |
| Apparatus — Reproduction, References, Appendix A | 630 |
| Whole file, tables excluded | 11,745 |

**The band governs the body, and the body is inside it.** Emil's GATE 4 ruling: a pin line and a
generated appendix are apparatus, not argument, and the measure note established that split when its
bibliography and Appendix A were counted separately.

**The ceiling raise is recorded as granted and unused — not rescinded.** The honest sequence was:
an overage was reported at GATE 3 (11,075, front matter included); the ceiling was raised
explicitly to cover it; better measurement at GATE 4 separated the parts and showed the body at
10,992, inside 11,000, so the raise was not needed. **That is a correction to the measurement, not
to the ruling.**

**The trim is recorded as −300, not −400, with the reason.** The four named register-native sites
held ~895 words; taking 400 would have removed 45% of them, and past 300 the cuts stopped removing
padding and started removing argument. No citation and no closure was touched — verified by the
cited-node census being identical before and after. §6.3 lost its Ashby/Tesler/Meyer walk-through
(all three have their own §11 entries), §10.3 went from eight boundary cases to five, §1 lost its
roll-call, §8.1–§8.3 lost what their tables already carry.

---

## Findings worth carrying

**Quotation fidelity is not checked by anything, and a paper is where it fails.** A first drafting
pass produced **nine** block quotations that were not verbatim — three divergent, five silently
truncated, one composed from two claims and formatted as one. No existing instrument could have
caught any: `E13` covers `ddd:embed` only, `W5`/`W6` resolve inside the pinned ref's contents, and a
prose citation carries no marker. **The near-miss that justifies the rule:** `DDD-floor-01` was
truncated exactly at the `DDD-dec-15` scope clause, so the quotation would have restored the
superseded universal quantifier — asserting that overflow ∩ open is *the* mechanism of escape rather
than *one generator* — while the paper's own gloss two paragraphs below said the opposite. Freight
item 1.

**An independent re-read is worth more than a re-read.** `check-appendix.py` reported four
discrepancies on its first run, and **all four were its own parser's fault** — it split table cells
on the escaped pipes inside `H(V|X)` and `H(V|S)`. The appendix was correct. A checker that can be
wrong about a correct artefact could have been wrong about an incorrect one, and only independence
surfaces which of the two is at fault. Freight item 1a.

**A generator serving "regenerate wholesale" must be idempotent.** The appendix generator appended a
second horizontal rule on a second run. Found at the close, fixed, and idempotence now demonstrated
by three runs and a byte comparison rather than by reading the code. Freight item 1a.

**All three instruments carry their own defect history in their docstrings**, because an instrument
ratified as a standing requirement should not present itself as having always been right. Two of the
three bugs were in the checkers, not in what they checked.

**The pin's inherited half was unearned.** The measure note pins a downstream ref because it cites
downstream claims. Paper A cites **none** — tested, not assumed: the intersection between its 48
cited claim and decision IDs and the downstream repository's own is empty. Copying the note's pin
would have asserted that identifiers resolve against a ref against which none of them do.

**Tesler has no primary publication, and the entry says so.** Flagged in the bibliography rather
than in a footnote, with the earliest substantial published discussion named and the exposure
limited in the entry itself — *cited for the allocation question only, no result taken*. Inventing a
locator was the alternative.

**`paper-a-draft.md` never existed.** The foundation names it as its predecessor; it is absent from
both repositories across full unshallowed history. Recorded at GATE 1, confirmed by Emil, and
**closed rather than carried** — successor item 5.

**`DDD-dec-26` carries `[PROPOSED]` banners inside a cut tag.** Its body records the rulings as made;
its banners say nothing is ratified. Reported, not repaired — a paper session does not reach into
canon to tidy banners. Freight item 4.

## Open items this session created or carried

| Item | Home |
|---|---|
| **Quotation fidelity as a standing requirement** — verify verbatim or declare partial | **Freight**, next canon session |
| **Appendix generated, re-read independently, idempotent**; hypothesis rows fail on evidence the graph lacks | **Freight**, rides with the above |
| **`DDD-dec-26`'s `[PROPOSED]` banners**, and `DDD-frame-02`'s duplicated word | **Freight**, next canon session |
| The constructive-closure node (Q32) | **Q-wave** — carried, not created; a second projection now depends on it |
| The institutional-provenance mechanism (Q27) | **Q-wave** — carried, not created; a Q27 landing forces a §2.4 revision |
| The measure note has no downstream tag | **Emil**, unbundled |
| The `term:training` supersession question | Wave 3 successor item 1, untouched |

## Out of scope, untouched

Any canon filing · the measure note itself (cited, never touched) · the training-gate supersession ·
the carve · S-1 · Q37 · G-track · the DDD-method paper · Q38b's asymmetry material (one forward
sentence in §1.2, as permitted) · the correspondence campaign · paper-4's study.
