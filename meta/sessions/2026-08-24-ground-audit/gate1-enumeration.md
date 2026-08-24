# GATE 1 — raw enumeration, and the sense definitions as they will be applied

**Status: ratified at its gate (Emil).** Nothing is classified yet, deliberately: the raw counts land first
so the classification's coverage at GATE 2 can be checked against them rather than trusted.

**Nothing outside this directory has been touched.** Read at `actor-indexed-determination` `37f508e`
(= `v5.10.0`), `decision-driven-design` `92c7b2e`, `product-cli` `d0f4297` (read-only).

---

## 0. The instrument, and three defects it had before it was trusted

The count is produced by `count-ground.py`, committed beside this report so it can be re-run. It was
**wrong three times**, and each correction changed the number. Recording that is not
self-flagellation — Phase 1a ruled that a checker's defect history belongs with the instrument, and
this instrument's history is one gate old.

**Defect 1 — `_` is a word character.** The first pattern was `\bground\w*`. Its own
exclusion report showed `parse_ground`, `bi_param_ground_provenance_maps_per_the_table` and a dozen
snake_case Rust test names being discarded as "false positives". **They are not false positives.** In
regex `_` is a word character, so `\b` does not fire between `parse_` and `ground`, and the pattern
silently under-counted **every snake_case identifier** — which is most of the software surface. The
boundary is now stated as "not a letter and not a digit", which makes `_` a boundary while still
excluding `background`.

**Defect 2 — escaped newlines hide field names.** `ledger-core` holds embedded YAML inside Rust
string literals: `"tolerance_floor: T1\nground: characterised"`. The `n` of `\n` sits immediately
before `ground`, so no boundary fires. Four occurrences of the **real YAML field name `ground:`**
were being dropped. `\n`, `\t` and `\r` are now unescaped to whitespace before matching.

**Defect 3 — the audit counted itself.** The instrument quotes its own regex in its docstring, so
`\bground\w*` scored as occurrences and this report's own prose would have scored too. The audit's
own directory is now excluded, and the exclusion is stated in the script.

| | total | upstream | downstream | product-cli |
|---|---|---|---|---|
| naive first pattern | 2,932 | 523 | 1,137 | 1,272 |
| **after all three corrections** | **2,845** | **523** | **1,036** | **1,286** |

The net is small and the gross is not: **+14 recovered** from defects 1 and 2, **−101 removed** by
defect 3. A single number would have concealed both.

**What is still excluded, and why.** `background` (360), `foreground` (8), `underground` (2),
`playground` (3), `backgroundfetch*` (3) — a letter precedes `ground`, so no boundary exists. One
filename, `holdingnotegroundaxesrev5copy`, is excluded on the same rule and is a genuine near-miss
worth a manual row at GATE 2.

---

## 1. Raw counts — the headline

> **2,845 occurrences across 394 files in three repositories.**

| Repository | Occurrences | Files |
|---|---|---|
| `actor-indexed-determination` (canon) | **523** | 82 |
| `decision-driven-design` (projection) | **1,036** | 104 |
| `product-cli` (software) | **1,286** | 208 |
| **total** | **2,845** | **394** |

**Morphological variants, counted separately rather than merged:**

| Token | Count |
|---|---|
| `ground` | 2,745 |
| `grounding` | 50 |
| `grounds` | 23 |
| `grounded` | 13 |
| `ground_provenance` and longer snake_case identifiers | 13 |
| `groundwork` | 1 |

---

## 2. Per artefact class — the coverage check for GATE 2

### `actor-indexed-determination` — 523 in 82 files

| Class | Count | Files |
|---|---|---|
| A6 core documents (`core/*.md`) | **161** | 16 |
| A7 upstream meta / holding notes | **131** | 10 |
| A3 claim files | **102** | 32 |
| A4 decision files | 40 | 6 |
| **A1 term registry** (`core/graph/terms.yaml`) | **29** | 1 |
| A9 release descriptors — **immutable, never edited** | 21 | 5 |
| A5 upstream assets (executable) | 20 | 6 |
| A12 upstream root docs | 15 | 4 |
| A10 i18n | 3 | 1 |
| A8 spec | 1 | 1 |

### `decision-driven-design` — 1,036 in 104 files

| Class | Count | Files |
|---|---|---|
| B14 downstream meta / holding notes | **269** | 9 |
| B13 session records — **historical, never rewritten** | **239** | 42 |
| B7 apparatus | **141** | 9 |
| B8 **Paper A (merged)** | **100** | 2 |
| B11 projections / tracks | 65 | 2 |
| B9 **measure note (merged)** | 64 | 5 |
| B18 downstream root docs | 38 | 6 |
| B12 applications | 31 | 2 |
| B4 decision files | 29 | 8 |
| B3 claim files | 22 | 8 |
| B6 core documents | 20 | 4 |
| B5 downstream assets (executable) | 8 | 3 |
| B15 migration | 5 | 2 |
| B2 downstream graph (pins) | 4 | 1 |
| **B1 axis registry** | **1** | 1 |

### `product-cli` — 1,286 in 208 files

| Class | Count | Files |
|---|---|---|
| C2 YAML — schema, fixtures, config | **685** | 94 |
| C3 markdown docs | **297** | 24 |
| C1 Rust source | **282** | 84 |
| C4 JSON / RDF schema | 4 | 2 |
| C5 manifests | 4 | 2 |
| C6 other | 14 | 2 |

By tree, which matters more than by file type:

| Tree | Count | Files |
|---|---|---|
| `.ddd/` — the repository's own decision ledger | **660** | 70 |
| `docs/` other | 162 | 14 |
| **`docs/g-track/`** | **143** | 13 |
| `product-core/` | 103 | 26 |
| `ledger-core/` | 66 | 20 |
| `ledger-cli/` | 37 | 17 |
| `ddd-core/` | 35 | 13 |
| `.decisions/` | 21 | 11 |
| `product-cli/` | 17 | 5 |
| **`ground-cli/`** — a crate named for the word | 16 | 8 |
| `ddd-cli/` | 15 | 4 |
| `ddd-lsp/` | 7 | 4 |
| `ddd-mcp/` | 2 | 1 |

---

## 3. Three findings the enumeration produced before any classification

### 3.1 `product-cli` is 45% of the surface and is absent from the proposal's cost list

The assessment's §6 prices the migration as "the term registry, every core document, claim
statements citing ground, the axis registry, the G-track PRD, the primer's planned §4, and two
merged papers". **The software repository is not on that list, and it carries 1,286 occurrences —
more than either canon repository, and 45% of the total.**

It is also the most expensive kind of occurrence, because the word is in **identifiers, not prose**:

- a **crate directory** named `ground-cli`, referenced 120 times;
- **67 path components** containing the word — 58 in `product-cli`, 6 upstream, 3 downstream —
  including 12 `.ddd/seams/seam-rust-product-core-src-ground-*.yaml` seam files whose *filenames*
  encode module paths;
- **Rust module paths** — `product-core/src/ground/{apply,axes,batch,declared,derivation,entail,facts,mint,mod}.rs`;
- a **YAML field name** `ground:` in the ledger format, appearing in fixtures and in test literals;
- `ground_provenance` as a **struct or column name**.

**Renaming prose is a rewrite. Renaming a field name in a serialised ledger format is a data
migration**, and `.ddd/` alone carries 660 occurrences of it across 70 files. This is a cost
category the proposal does not have, and it should be reported to Emil before any migration shape is
proposed at GATE 3.

### 3.2 The G-track PRD exists — in the software repository

The prompt's D-1 lists "the G-track PRD" as an artefact to audit. **It is in neither canon
repository.** It is `product-cli/docs/g-track/prd-ground-as-ontology.md`, 1,094 lines, and its
`docs/g-track/` directory carries 143 occurrences across 13 files.

That places the artefact the assessment names as a migration cost **inside the repository the
assessment does not price**, which is the same finding as §3.1 arriving from the other end.

### 3.3 Two named compounds do not exist

| Compound | Named in the prompt | Occurrences |
|---|---|---|
| `ground channel` | yes | **0** |
| `ground coverage` | yes | **0** |

Both appear in the proposal's migration table as expressions to be replaced. **Neither occurs in any
of the three repositories.** They are the proposal's own coinages, or paraphrases of `ground
channels` (10, plural) and something the audit has not yet matched. Reported rather than
silently dropped, because a migration table containing rows for expressions that do not exist
overstates its own coverage.

---

## 4. Compound inventory — counted, including compounds nobody named

Named in the prompt, with counts:

| Compound | Total | up | down | pcli |
|---|---|---|---|---|
| `poisoned ground` | **61** | 37 | 24 | 0 |
| `ground distribution` | **51** | 20 | 30 | 1 |
| `ground registry` | **46** | 1 | 7 | **38** |
| `ground provenance` | **38** | 3 | 24 | 11 |
| `declared ground` | 31 | 4 | 27 | 0 |
| `accessible ground` | 13 | 1 | 12 | 0 |
| `institutional ground` | 13 | 0 | 11 | 2 |
| `missing ground` | 11 | 2 | 9 | 0 |
| `ground channel` | **0** | — | — | — |
| `ground coverage` | **0** | — | — | — |

**Found and not named — the "any others found" clause, and it is where the volume is:**

| Compound | Total | up | down | pcli |
|---|---|---|---|---|
| `DDD-ground-*` (claim IDs) | **142** | 44 | 66 | 32 |
| `ground-cli` (crate) | **120** | 0 | 0 | 120 |
| `ground axes` | **68** | 19 | 42 | 7 |
| `reading ground` | 35 | 16 | 19 | 0 |
| `ground truth` | 22 | 4 | 12 | 6 |
| `uncontrolled ground` | 22 | 2 | 20 | 0 |
| `ground item` | 21 | 0 | 0 | **21** |
| `relevant ground` | 20 | 5 | 15 | 0 |
| `raw ground` | 18 | 13 | 5 | 0 |
| `digital ground` | 15 | 12 | 3 | 0 |
| `adversarial ground` | 14 | 3 | 11 | 0 |
| `ground assurance` | 14 | 1 | 13 | 0 |
| `predicted ground` | 14 | 7 | 7 | 0 |
| `ground applicability` | 13 | 11 | 2 | 0 |
| `grounding edge` | 13 | 0 | 1 | 12 |
| `ground accessibility` | 11 | 3 | 8 | 0 |
| `ground state` | 11 | 0 | 2 | 9 |
| `ground table` | 9 | 0 | 0 | 9 |
| `ground note` | 8 | 4 | 4 | 0 |
| `ground axis` | 7 | 1 | 5 | 1 |
| `base ground` | 3 | 0 | 3 | 0 |

**`DDD-ground-*` is the row worth pausing on.** Five claim IDs — `DDD-ground-01` through
`DDD-ground-05` — carry the word in their **identifiers**, cited 142 times across all three
repositories. `CLAUDE.md` is explicit: *"IDs are never reused; renumbering is forbidden."* **Those
142 occurrences cannot be migrated at any price.** Whatever the ruling, the word survives in the
graph's own identifiers permanently, and the migration must state that it is renaming the *concept*
and not the *node names*.

---

## 5. The five senses, as this session will apply them

Stated before classification so the classification can be checked against a fixed rule rather than
against its own results.

| # | Sense | Test the classifier applies | Canonical anchor |
|---|---|---|---|
| **S1** | **Conditions in the case** whose variation moves the outcome past τ | Would varying *the world* change whether the outcome is acceptable? The occurrence is about what is true, not about what anyone holds | `term:admission-test` — *"A fact is ground iff varying the world moves the outcome past tolerance"* |
| **S2** | **Representations the arrangement holds** | Is the occurrence about records, observations or retrieved material that exist *somewhere in the arrangement*, whether or not they reach the act? | "accessible ground"; the ledger |
| **S3** | **Representations delivered at the act** | Is the occurrence about what actually reaches the resolver at *this* act? | "reading ground"; `term:delivery`'s act-site indexing |
| **S4** | **Institutional rules and standards** | Is the occurrence a criterion of judgement rather than material judged? | "institutional ground"; Q27's trust material |
| **S5** | **The population** over which demand is measured | Is the occurrence about a distribution over cases rather than about one case? | the measure's `P`; "ground distribution" |
| **U** | **Unassignable** | Sits in more than one, or in none, with the reason recorded | — |

**Four rules the classifier will follow, stated now:**

1. **Exactly one sense, or `U` with a reason.** No occurrence is forced. Per the charter, an
   unassignable row is the most valuable row in the table.
2. **Sense is read from the sentence, not from the compound.** `declared ground` will not be
   assumed S1 because it usually is; each occurrence is read where it sits. Where a compound turns
   out to be consistently one sense, that is a *result*, not an input.
3. **Historical text is classified and flagged, never migrated.** Session records (239), release
   descriptors (21) and retired-claim notes are immutable by this repository's own rules. They are
   counted, classified, and marked **not-migratable** — a cost table that includes them as work
   would overstate the migration by roughly a quarter of the downstream total.
4. **Identifiers are a separate column from prose.** `DDD-ground-03`, `ground-cli`,
   `ground_provenance` and the YAML field `ground:` are classified by sense like anything else, but
   the cost table separates them, because renaming an identifier is a different operation from
   rewriting a sentence.

---

## 6. What is asked at this gate

1. **Rule the sense definitions and the four classifier rules** at §5, before any classification runs.
2. **`product-cli` is 45% of the surface and is not in the proposal's cost list** (§3.1). The
   session proposes auditing it fully — it is already counted — and reporting it as its own cost
   category at GATE 2, because renaming a serialised field name is a data migration and not a
   rewrite. Confirm, or scope it out.
3. **`DDD-ground-01`…`05` cannot be renamed** (§4): 142 occurrences in identifiers, and renumbering
   is forbidden by `CLAUDE.md`. Confirm that the migration is understood to rename the concept and
   not the node names, so GATE 3's rulings are framed correctly.
4. **Two named compounds do not exist** (§3.3). Confirm they are dropped from the working inventory
   rather than hunted further.
