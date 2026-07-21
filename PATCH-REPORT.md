# v4.1 Patch Application Report

Applied per `PATCH.md` in the v4.1 patch package. All new files were copied verbatim
(byte-identical to the package, verified with `diff`). No prose, numbers, tables, or equations in
`core/07-projections.md` or `core/08-the-measure.md` were altered.

## 1. Script verification — all three ran; sums constant

- `python3 core/assets/measure-toy.py` — ran clean. Total demand H(verdict) = **25.493 bits**.
  Both decompositions (split by month: 20.593 + 4.901; split by day≤28|≥29: 11.020 + 14.474) sum
  to exactly 25.493. Constant. ✔
- `python3 core/assets/measure-actor-allocation.py` — ran clean. All three actors (program:
  25.493 + 0.000; weak model: 14.474 + 11.020; mid model: 20.964 + 4.529) sum to exactly
  **25.493 bits**. Constant. ✔
- `python3 core/assets/measure-rag.py` — ran clean. Across all six retrieval settings, each row's
  encoded I(A;R) + judged H(A|R) equals that row's H(A), **~2.61 bits** throughout (row values
  2.602–2.616, the expected third-decimal jitter of a 40k-sample estimate; within each row the sum
  matches H(A) exactly). Constant. ✔

## 2. Dead-link check — no dead links

Neither new doc uses `[…](…)` markdown links; all internal references are backtick path/section
references. Every referenced target was checked and exists:

- `core/07-projections.md` references: `01`, `03`, `05` (twice more at lines 124/143/182),
  `assets/projections.svg`, `assets/projections.html` — all resolve.
- `core/08-the-measure.md` references: `core/assets/measure-*.py`, `core/01`, `core/07`,
  `core/05`, `core/04`, `core/03`, `assets/measure-toy.py`, `assets/measure-actor-allocation.py`,
  `assets/measure-rag.py` — all resolve.

**Dead links found: none.**

## 3. Exact edits made to existing files

### `README.md`
1. Added the `07` and `08` rows to the **Core — the theory** table, immediately after the `06`
   row, using PATCH.md's text character-for-character.
2. Added the "And, new in 4.1: …" paragraph in the **one idea** section, immediately after the
   two-consequences list (i.e. before the pre-existing "And a prediction:" paragraph), using
   PATCH.md's text character-for-character.
3. Added the i18n pointer as a single line after the **Meta — the honesty layer** table:
   `Danish glossary: [`i18n/ordliste-dansk.md`](i18n/ordliste-dansk.md).`

### `meta/consolidated-state.md`
1. Replaced §5 item 1 (the counting-procedure debt) with PATCH.md's **PARTIALLY DISCHARGED
   (v4.1)** text, character-for-character.
2. Appended the two v4.1 rows ("A better decomposition destroys demand" → Corrected; "The funnel
   as a *count* projection" → Corrected) to the end of the §2 superseded/corrected table,
   character-for-character.
3. Added the judgment/escape-split bullet (the still-open next step) in §5, after numbered item 3
   and before the **Product** paragraph, character-for-character.

### `core/README.md`
1. Added the `07` and `08` index lines after the `06` line, character-for-character.
2. Updated the load-bearing line: "The load-bearing, falsifiable claims are in **03** and
   **04**." → "…in **03**, **04**, and **08**."

### `CHANGELOG.md`
Added a **4.1 — The measure** entry above 4.0 with the specified summary (verdict entropy /
chain rule for the closing-predicate case; funnel/maturation corrected to judgment-demand
projections; Danish glossary), noting the counting-procedure debt moves from open to partially
discharged, the two v4.1 corrections, the unchanged principle-not-law register, and the
judgment/escape split as the booked next open debt.

## 4. Flagged but not changed

- **`README.md` "What this is, and is not"** still states the conservation claim "has **no
  measurable unit**". v4.1 gives a unit (bits) on the closing-predicate region, so this sentence
  is now partially outdated — but PATCH.md's edit list does not touch it and the register is
  unchanged, so it was left as-is.
- **`README.md` "Status"** still names "a counting procedure for governing decisions" as the most
  important open debt. Now partially discharged per v4.1; not in PATCH.md's edit list, left as-is.
- **`meta/consolidated-state.md` §1.4** still says "a better decomposition genuinely *destroys*
  demand" — now contradicted by the v4.1 correction row added to §2 (the doc's own rule is that
  the superseded/corrected table wins). PATCH.md only specified the table row, so §1.4's body
  text was left untouched.
- **`meta/consolidated-state.md` §1.2** heading contains a pre-existing use of "law" ("the
  discipline that keeps this a law"). Pre-existing v4.0 text, not a reintroduction; left as-is.
- **CHANGELOG 4.0 entry** still lists the counting procedure under its open debts — left as-is,
  since it is a historical record of the 4.0 release.
- The word "law" does not appear anywhere in the two new core docs; nothing added in this patch
  uses "law" for the framework's own claim.

## Summary

The v4.1 patch applied cleanly: the two new core documents (`07-projections`, `08-the-measure`),
five assets (three reproduction scripts and two figures), and the Danish glossary were dropped in
verbatim; the three surgical edits to `README.md`, `meta/consolidated-state.md`, and
`core/README.md` were made with PATCH.md's exact insert text; and a v4.1 changelog entry was
added. All three reproduction scripts run on stdlib Python and their tables sum to the constant
totals the docs claim (25.493 bits for the toy and actor-allocation cases, ~2.61 bits at every
retrieval setting for RAG), every internal reference in the new docs resolves to an existing
file, and the register is unchanged — the framework's claim remains a principle, with the
counting-procedure debt moved from open to partially discharged for exactly the region where the
acceptance predicate closes.
