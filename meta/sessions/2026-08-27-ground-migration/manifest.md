# Manifest — item 5, the ground migration

**Session type:** interactive canon curation with an execution phase. Six gates, Emil ruling at each.
**Merged nothing.** Branch `claude/ground-migration-item-5-jpa9tc` in all three repositories;
`product-cli` carries **no commit** and no working-tree change.

**Read at:** `actor-indexed-determination` `ce2c477` (= annotated tag **`v5.11.0`**, verified — head
and tag are the same commit) · `decision-driven-design` `e81a454` · `product-cli` `d0f4297`.

---

## The session's principal finding

> **The migration is planned in full and deferred whole. That is the finding, not the failure.**

The plan is complete, the classification is execution-grade, every pin and firing is named, and the
design rulings the audit said were the point are **answered**. **A successor starts at execution.**

What ships instead is the set of repairs that surfaced while planning it and that stand on their own
evidence — proposed as **`v5.12.0`**. **No occurrence of `ground` changed sense or wording anywhere
in either repository.**

---

## What the session found

| | |
|---|---|
| **The definition layer is 17 settled terms and one draft, not fifteen** | The audit named two that do not use the word and omitted six that do. `term:tolerance` (S1) and `term:arrangement` (S2) are both in `00-primitives.md` — **the defect is on one page, not spread across the registry** |
| **Two further objects under the word**, both in `product-cli` | the RDF/logic **`ground term`** (11) and a **CSS surface colour** (6). Neither is any of S1–S5 |
| **`ground channel` occurs 10 times, not zero** | one inside `term:arrangement`'s settled canonical text. A migration surface the plan was told it did not have |
| **The defect is translated** | the Danish glossary gave two definitions in one entry, the second being the one the audit found miscited to `core/00` |
| **The audit counted itself a third time** | the corpus at its own read commits is **2,843** |
| **`judgment`'s collision was already closed** | by `DDD-frame-17`, the node it was recorded against; `DDD-dec-30` says so in canon's own words. Cost zero |
| **`projection` and `verdict` are two new live collisions** | both unpinned; `denominations:` repaired `projection`'s half as a side effect |
| **The classification instrument had three failure mechanisms** | clause-crossing windows, rule ordering, and uncorrelated size-and-quality |
| **S1 is canon's largest sense** | +16% over the audit, **182 S1 : 154 S3** upstream. The authority-over-volume ruling was made on the definition layer and **the corrected corpus agrees** |
| **Canon's S4 is mechanically zero** | agreeing with GATE 3's independent reading of the reconciliation. **Two methods converging** is what makes the S4 dissolution safe rather than convenient |
| **`13-delivery.md` declared a dependency it never had** | and the collision masked it: the body linter sees the word and cannot see which object. **Discovered, not planned** |

---

## The twenty-three carried items, closed

| | Item | Closed how |
|---|---|---|
| C1 | `apparatus/` re-booked | W2's tail. In the seed |
| C2 | why S3's estimate was low | Recorded; superseded by C19 |
| C3 | `ground channel` ×10 | In W2 via `term:arrangement`. Erratum E-2 |
| C4 | the i18n gloss | **Landed** — the second definition removed |
| C5 | `README.md` | **Landed** — judgment row and closure paraphrase |
| C6 | SR-4's warrant | Recorded; dissolves with S4 |
| C7 | the head delta | **Discharged** — 106 of 133 immutable or audit output |
| C8 | sweep 1's grades | **Grade A landed**; B and C to freight with grading intact |
| C9 | `mechanical` → `act-triggered` | **Landed.** `DDD-dec-30` the warrant; the discipline **existed before the violation** |
| C10 | `projection`, `verdict` | To freight; `projection`'s half repaired by `denominations:` **as a side effect** |
| C11 | `judgment` closed | No work |
| C12 | five drafting-warning exceptions | In the seed |
| C13 | `floor` in `product-cli` | W4's assessment |
| C14 | Q-1, Q-2 | Q-1 **filed** (the erratum pointer); Q-2 **landed** (`denominations:`) |
| C15 | the §7/Q27 reconciliation | **Settled.** Q27 cleared to file |
| C16 | S4 dissolves | Four senses plus attributes |
| C17 | W0-bis blocking | **Discharged** |
| C18 | the classification whole; C17's estimate corrected | 29% reported, **71.7% measured** |
| C19 | S3 moved back | +11%, not +26%. SR-2 untouched |
| C20 | S1 the largest movement | Canon S1-led. **Strengthens SR-1** |
| C21 | canon's S4 zero | Two methods converging |
| C22 | identifiers are **142**, not 116 | Rule ordering, both directions enumerated |
| C23 | the method rule | In the seed, all three mechanisms named |

---

## Deliverables

**Upstream** (`actor-indexed-determination`, 2 commits): `core/graph/terms.yaml` — three Grade A
definitions promoted, `term:delivery`'s value renamed, `term:verdict`'s `denominations:` field;
`core/06`, `core/08`, `core/09`, `core/13` re-projected; `DDD-cost-09`, `DDD-delivery-01`,
`DDD-delivery-03`; `spec/claim-format-2-addendum.md`; `README.md`; `i18n/ordliste-dansk.md`;
`releases/v5.12.0.yaml`.

**Downstream** (`decision-driven-design`, 7 commits): the session record and its six gate reports;
`w0-classify.py` with `rulings/r001…r021.py` and `rulings-bis/b001…b009.py`;
`w0-full-v2.json`; `meta/ground-audit-2026-08-24-erratum.md` and the audit's forward reference;
`meta/migration-plan-ground.md`, the successor's seed; `DDD-delivery-04`; `DDD-track-01`.

**`product-cli`:** nothing. Read-only throughout, as the prompt requires.

---

## Instruments

| | |
|---|---|
| `w0-classify.py` | merges `rulings/` and `rulings-bis/`, asserts the two sets do not overlap and that no row is unruled. **Residual zero by construction** |
| `rulings/r001…r021.py` | W0 — 1,022 rows, one ruling and its reason each |
| `rulings-bis/b001…b009.py` | W0-bis — 427 prose-context rows plus 29 anchored-class ordering corrections |
| `w0-extract-head.py` | the head delta, with **this session excluded from its own count** |
| `sweep2.py` | the G2 registry sweep |

---

## Gates

| | |
|---|---|
| upstream `validate-core-order.py` | **0 errors, 66 warnings** — identical to the pre-session baseline, verified by stash |
| upstream `validate-claims.py` | **63 claims valid, 32 warnings** · **12 decisions valid** |
| upstream `validate-releases.py` | **8 descriptors valid, versions unique, basis resolves** |
| downstream `validate-core-order.py` | **0 errors, 0 warnings**; 67 pins resolved, **0 content-drift**, 1 governed shadow |
| downstream `validate-claims.py` | **26 claims valid, 6 warnings** · **21 decisions valid** |

**Basis-impact sweep: no basis edge breaks.** No id moved, so every citing node still resolves;
`releases/v5.5.0.yaml`'s historical basis list is unaffected. Nothing quotes the moved denomination
verbatim.

**Predicted before operating, verified after: zero W5, zero W6, zero W7.** The downstream pin resolves
against `ref: v5.9.0`; this session neither advances it nor cuts a tag. **When it is next advanced
past these commits, exactly three fire — `term:delivery`, `DDD-cost-09`, `DDD-delivery-01`.**

---

## Three sentences worth keeping

> **Hand-editing Appendix A would forge agreement the pin does not yet have, which is the pin's
> entire purpose.**

> A classification rule whose match window can cross a clause boundary is not an anchored rule, and
> the two classes cannot share an acceptance standard.

> Repair what contradicts itself; never resolve what is merely unqualified.

---

## Three naming attempts, three registry checks

**`fixed`** died against `term:encoded`. **`resolved`** died against `term:determination`.
**`posterior`** died against the live Bayesian register — `prior` is used in that sense in four
places, one of them ratified canon (`DDD-measure-05`), and `term:calibration-ledger` is the
**estimator** in that same prior→update pipeline.

**Three is a pattern, and the pattern is the argument for the check.** The one name that survived,
`act-triggered`, survived because it was **not minted**: canon was already using it.
