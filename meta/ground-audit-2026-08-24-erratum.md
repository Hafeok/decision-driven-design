# Erratum — the ground audit, 2026-08-24

**Filed 2026-08-27 by the ground-migration session**
(`meta/sessions/2026-08-27-ground-migration/`), ruled by Emil at that session's GATE 1.

**This is an erratum, not a repair.** `meta/ground-audit-2026-08-24.md` is a merged artefact and its
history is not edited. It stands as filed; this note stands beside it and records what the full
classification found to be wrong in it. Both are canon-adjacent; neither supersedes the other.

**Why it exists at all.** The audit classified 64% of occurrences by rule and sampled the rest. The
migration session completed the classification — all 2,845 occurrences, each read in its own file —
and in doing so re-read the registry the audit's central finding rests on. Three of the audit's
statements did not survive that reading.

---

## E-1 — the definition layer is **17 settled terms and one draft**, not fifteen

The audit's §3.1 gives a table headed *"Every use of the word in `core/graph/terms.yaml`, the settled
layer"*, and concludes **"Fifteen settled terms. Four senses. One registry."**

The count is wrong **in both directions**, measured at `v5.11.0`.

**Two terms it named do not use the word at all:**

| Named by the audit | Occurrences of the word in its registry entry |
|---|---|
| `term:attribution` | **0** |
| `term:accountability` | **0** |

The *"ground channels"* the audit credited to `term:accountability` is in **`term:arrangement`**:
*"executor, prior commitments, **ground channels**, checks, reviewers, record, and accountable
principal"*.

**Six terms it omitted do use it:**

| Omitted | Status | Sense |
|---|---|---|
| `term:tolerance` | settled | **S1** — *"a fact is ground only relative to a declared tolerance"* |
| `term:arrangement` | settled | **S2** — *"ground channels"* |
| `term:answerability` | settled | **S1** — *"against what ground"* |
| `term:capability` | settled | **S3** — *"the class of ground a pathway can read"* |
| `term:swarm-gate` | settled | **S1** — *"genuinely determines choices against ground"* |
| `term:residual-discretion` | **draft** | **S3** — *"held at fixed ground"* |

**Corrected:** 18 registry entries use the word — **17 settled and one draft** — carrying **four
senses**. The sense count, which is the load-bearing half of the finding, is unchanged.

**The correction makes the finding worse, not weaker.** `term:tolerance` is S1 and `term:arrangement`
is S2, and **both are established by `00-primitives.md`** — the first document a reader meets. The
multi-sense defect is not distributed across the registry; it is on one page of it.

**One consequence for the audit's reasoning.** Its §3.1 closes: *"The registry alone uses S3 twice as
often as S1 (12 against 6), so there is no clean origin to have drifted from."* Corrected, the split
is **7 entries S1 and 7 entries S3** (9 and 16 by occurrence). **The conclusion survives and the
asymmetry that supported it does not** — there is no clean origin because there are two equal ones,
which is a stronger statement of the same finding.

---

## E-2 — `ground channel` occurs **10 times**, not zero

The audit's §2 states: *"Two compounds the proposal named — `ground channel` and `ground coverage` —
occur **zero times anywhere**."*

**`ground coverage` is indeed zero.** `ground channel` is not:

| | |
|---|---|
| `upstream/core/graph/terms.yaml:62` | **inside `term:arrangement`'s settled canonical text** |
| `upstream/core/00-primitives.md:129` | the same text, embedded |
| `downstream/projections/tracks/01-determination.md` | 3 occurrences |
| `downstream/papers/paper-a/paper-a.md` | 3 occurrences (one is the appendix's `term:arrangement` row) |
| `downstream/meta/holding-note-ground-axes-rev18.md:891` | 1 |
| `downstream/meta/sessions/2026-08-18-wave3/revision-foundation.md:125` | 1 (immutable) |

All ten are S2. **The audit told the migration plan it had no `ground channel` surface; it has one,
and it is in the registry**, which is the most expensive place for a surface to be missed.

---

## E-3 — the audit counted itself once more than it caught

The audit's §1 records three instrument corrections, the third being *"the audit counted itself,
because its own instrument quotes its own regex"*, and reports **−101** self-occurrences removed by a
`SELF` skip on `meta/sessions/2026-08-24-ground-audit/`.

Re-running `extract-occurrences.py` unchanged, at the audit's own read commits, yields **2,843**.
The two missing rows are both `meta/sessions/README.md:34` — the audit's own session-index line,
*"`2026-08-24-ground-audit/` | Interactive audit — Phase 1b: the ground audit"* — which it wrote in
its working tree, **outside the directory its `SELF` skip excluded**.

**Corrected:** 103 self-occurrences, and the corpus proper at the audit's read commits is **2,843**.

**Nothing else moves.** Both rows are immutable-class and both classify U. The migration session
classifies the committed 2,845-row extract in full, so the two are visible rather than quietly
dropped, and excludes its own directory from every count it takes.

---

## What is *not* corrected

The audit's four rulings (§4), its cost analysis, its wave shape (§6) and its §5 report of the
§7/Q27 collision are untouched by this note. So is its central finding, which the full
classification corroborated: **the remedy is definitional, because the definition layer was never
single-sensed.**

Two of the audit's own numbers were re-derived exactly over all 2,845 rather than over the
rule-assigned 1,823, and one moved: **canonical text is 222, not 240** — the audit's figure
double-counted across the two repositories' claim directories. Identifiers (820), immutable (260),
merged papers (164), embeds (26) and pinned objects (4) are unchanged.

**Basis:** the migration session's `gate1-classification.md` §3, §4.2 and §4.4, and its
`w0-full.json`. Reproducible from `meta/sessions/2026-08-27-ground-migration/w0-classify.py`.
