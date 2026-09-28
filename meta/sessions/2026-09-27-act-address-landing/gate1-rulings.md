# GATE 1 — rulings (act address landing)

Principal: Emil. Given 2026-09-28 in reply to `gate1-survey.md`, prefaced "all approved". The
rulings are transcribed here and not paraphrased into more than was said. The numbers follow the
survey's "Rulings requested".

| # | Subject | Ruling |
|---|---|---|
| 1 | The weakest point | Repair `DDD-ground-06`'s falsifier limb 1 to "address, ground readings and predicates, without the verdict itself". Amend `DDD-address-01` so that occurrence B depends on A iff a state change produced by A is in B's ground reading, with the time index as the resulting order over state changes. Flag the reading/verdict-input line `UNVERIFIED — Emil review`. |
| 2 | Phoenix out of upstream `core/` | Neutral upstream wording: "the first independent application case, pre-registered in the projection's session records". Phoenix is named downstream only. |
| 3 | Citation | Cite `DDD-ground-05` and `DDD-ground-02` for the declared-space limit. |
| 4 | Rule 1 | Keep `DDD-ground-06` and `DDD-address-01` joined. |
| 5 | `DDD-address-05` | File, with the behaviour-term dependency named. |
| 6 | `DDD-address-03` | File, with seam decay as a successor item. Do not cite `DDD-cost-27` as support. |
| 7 | Unruled dry-run items | Accept E-1. Accept F-3 as `[PROPOSED]`. Accept the T2a act map, with a1's gateway axis recorded as not read. Hold F-1 as a T2b test item: an act that never reads an axis a governing predicate uses. Hold F-2, and strike the 14 s figure. |
| 8 | Registry fit | Home `term:act-address` in `core/14`. Drop the bare `address` alias. The small `core/14` prose edit is allowed. |
| 9 | Danish glossary | `handlingsadresse` = act address; `lagsti` = layer path. |

**Standing instruction for GATE 3.** The predicted firing includes the `DDD-frame-08` W6 from
crossing v5.14.0 and v5.14.1.

**Instruction.** Proceed to GATE 2.

## How the rulings land

| Ruling | Lands at | Where |
|---|---|---|
| 1 (limb 1), 2, 3, 4, 8, 9 | GATE 2 | Upstream: `DDD-ground-06`, `DDD-dec-37`, `core/graph/terms.yaml`, `core/14`, `i18n/ordliste-dansk.md` |
| 1 (`DDD-address-01`), 4, 5, 6 | GATE 3 | Downstream: `DDD-address-01…05`, `DDD-dec-38` |
| 7 | GATE 3 | This directory. The 2026-09-27 session record lands exactly as bundled; the rulings on its findings are recorded here, not written into it. |
| Seam decay (6), F-1 as a T2b item (7), the behaviour term (5) | GATE 4 | Successor items |
