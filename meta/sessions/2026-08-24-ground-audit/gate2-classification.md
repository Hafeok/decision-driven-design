# GATE 2 — D-1 the classification, D-2 the cost table

**Status: ratified at its gate (Emil).** Nothing outside this directory has been touched.

Artefacts committed beside this report, so every number can be re-derived rather than trusted:
`count-ground.py`, `extract-occurrences.py`, `classify.py`, `classification.json` (2,845 rows,
one per occurrence), `residual-adjudication.json`.

---

## 0. Method, and its honest coverage

**The classification is 64% deterministic and 36% sampled, and the two are never mixed in a
number.**

- **1,823 occurrences (64%) are rule-assigned.** `classify.py` carries an ordered rule table; each
  rule states the sense it assigns and **why that assignment is safe**, and every rule was written
  by reading real occurrences out of the extract rather than invented. **There is no default
  rule** — an unmatched occurrence falls to a named residual bucket, because a default is the one
  thing that could make this table lie.
- **1,022 occurrences (36%) matched no rule.** They are bare `ground` in prose, whose sense is
  carried by the sentence. They are spread across **249 files** with a long tail — the top ten
  files hold only 31% — so file-level adjudication would not have closed them either.
- **100 of those 1,022 were drawn at random (seed 2026) and hand-read**, one at a time, in context.
  The adjudication is committed as `residual-adjudication.json` with the sample indices, so it can
  be re-checked occurrence by occurrence.

**Per GATE 1 rule 2 (ratified): sense was read from the sentence, never assumed from the compound.**
§4 reports what that produced, and it is the session's most useful result.

**Counts of occurrences are counted.** 2,845 is exact. **Sense shares of the residual are
estimated** from the sample, with 95% intervals shown and never quietly folded into an exact-looking
total.

---

## 1. D-1 — the classification

| Sense | Rule-assigned (exact) | Residual sample (n=100) | Residual estimate | 95% CI | **Projected total** | Share |
|---|---|---|---|---|---|---|
| **S2** representations the arrangement holds | **1,004** | 62 | 634 | [536, 731] | **1,638** | **57.6%** |
| **S1** conditions in the case | 273 | 21 | 215 | [133, 296] | **488** | 17.2% |
| **S3** representations delivered at the act | 270 | 6 | 61 | [14, 109] | **331** | 11.6% |
| **U** unassignable | 172 | 7 | 72 | [20, 123] | **244** | 8.6% |
| **S5** the population | 74 | 3 | 31 | [0, 65] | **105** | 3.7% |
| **S4** institutional rules | 30 | 1 | 10 | [0, 30] | **40** | 1.4% |
| | **1,823** | **100** | **1,022** | | **2,845** | |

**S2 is the majority sense, and it is not close.** Nothing in the proposal or the assessment
predicted that; both treat S1 as the centre of gravity.

### 1.1 The split by repository — the finding that reframes the ruling

Rule-assigned occurrences only, so these are exact:

| | S1 | S2 | S3 | S4 | S5 | U |
|---|---|---|---|---|---|---|
| `actor-indexed-determination` (canon) | **101** | 24 | **110** | 3 | 31 | 49 |
| `decision-driven-design` (projection) | **165** | 116 | **134** | 22 | 42 | 86 |
| `product-cli` (software) | 7 | **864** | 26 | 5 | 1 | 37 |

> **Canon is bilingual in S1 and S3, with S2 barely present. The software repository is
> monolingual in S2 — 864 of its 939 rule-assigned occurrences, 92%.**

The two halves of the programme are not using one overloaded word in the same way. **They are using
two different senses of it, and each is nearly consistent within itself.** The overload is between
the repositories at least as much as inside either.

---

## 2. D-2 — the cost table

Rule-assigned only, so every cell is exact.

| Sense | Total | In identifiers | Immutable (never migrated) | In merged papers | In canonical text | In `product-cli` |
|---|---|---|---|---|---|---|
| **S1** | 273 | 13 | 45 | 31 | 58 | 7 |
| **S2** | 1,004 | **592** | 42 | 20 | 23 | **864** |
| **S3** | 270 | 25 | 45 | 19 | 29 | 26 |
| **S4** | 30 | 4 | 10 | 3 | 3 | 5 |
| **S5** | 74 | 0 | 5 | **29** | 10 | 1 |
| **U** | 172 | 104 | 24 | 8 | 34 | 37 |

Across all 2,845 occurrences, whether rule-assigned or not:

| Column | Count | What it means for cost |
|---|---|---|
| **identifiers** | **820** | Not prose. Claim IDs, crate and binary names, module paths, YAML field names, code symbols. A rename here is a data migration or an ID change, never an edit |
| **immutable** | **260** | Session records (239) and release descriptors (21). **Classified and flagged, never migrated** — this repository's own rules forbid rewriting them. Counting them as work would overstate the downstream total by roughly a quarter |
| **merged papers** | **164** | Paper A and the measure note. Both are merged; both are already owed a revision |
| **canonical text** | **240** | Term registry, claim and decision files across both repos — the expensive-to-move class |
| **embeds** | **26** | Occurrences inside `ddd:embed` blocks, requiring re-projection rather than editing |
| **pinned graph objects** | **4** | Downstream `graph/upstream.yaml` — the only occurrences that would fire **W6 content-drift** directly |

**W6/W7 exposure is small and is not where the cost is.** Only four occurrences sit in the pin file.
The real exposure is that **`term:ground` is pinned downstream**, so any change to its canonical
text is one W6 — and every re-projected embed follows from that single edit rather than from the
2,845.

---

## 3. Three findings the classification produced

### 3.1 The apparatus defines `ground` differently from canon — and cites canon for it

`apparatus/encode-verify.md:21`:

> Ground is the read-only surface an actor inspects in order to act (`core/00`).

`apparatus/closure-principle.md:21` repeats it:

> The current treatment defines **ground** as *the read-only surface actors inspect in order to
> act* …

`core/00-primitives.md`, `term:ground`, **settled**:

> **Ground** — what they are determined against.

and `term:admission-test`, **settled**:

> **A fact is ground iff varying *the world* moves the outcome past tolerance.**

**These are not the same definition.** "The read-only surface an actor inspects" is S2 — material
held and inspected. "What they are determined against", tested by *varying the world*, is S1. **The
apparatus attributes an S2 definition to a source that states an S1 one**, by name, with a citation.

This is the strongest single piece of evidence the audit produces, and it is stronger than any of
the three arrivals SR-1 records: **the split is not a future risk, it has already produced a live
miscitation across the seam.** It was invisible to the proposal and the assessment because both
reasoned about the word and neither read the two definitions side by side.

### 3.2 Canon's own registry carries two senses in one document

`00-primitives.md` establishes both:

- `term:ground` — *"what they are determined against"* — **S1**;
- `term:poisoned-ground` — *"ground that is **present** but false: **the substrate a determination
  reads** has been corrupted"* — **present** and **read** are the delivered object, **S3**.

Two settled terms, one document, two senses of the head word, with the compound silently shifting
sense from its own root. **The proposal argues the overload from usage; canon demonstrates it from
its own registry.**

### 3.3 The five `DDD-ground-*` claims do not share a sense

Confirmed against their statements:

| Claim | Statement is about | Sense |
|---|---|---|
| `DDD-ground-02` | *"orthogonal properties of ground **relative to a filed decision**"* — coverage, resolution, assurance | **S2** |
| `DDD-ground-05` | *"Declaring the **determinable space** is constitutively prior to determination over it"* | **S1** |

GATE 1 established that these identifiers can never be renamed (142 citations; renumbering
forbidden). §3.3 adds the sharper fact: **the permanent identifiers do not even name one sense
between them.** `DDD-ground-*` classifies as **U at 70%** for exactly this reason.

---

## 4. Emil's addition — the unnamed compounds, and they cluster

Ordered by purity. The dominant-sense share is over all occurrences of each compound.

| Compound | Occurrences | Distribution | Dominant | Purity |
|---|---|---|---|---|
| `ground-cli` | 122 | S2 122 | **S2** | **100%** |
| `ground registry` | 58 | S2 58 | **S2** | **100%** |
| `grounding edge` | 21 | S2 21 | **S2** | **100%** |
| `ground table` | 13 | S2 13 | **S2** | **100%** |
| `reading ground` | 58 | S3 56, S4 2 | **S3** | **96%** |
| `ground axes` | 82 | S1 78, S2 3, S3 1 | **S1** | **95%** |
| `ground provenance` | 44 | S2 42, S4 2 | **S2** | **95%** |
| `uncontrolled ground` | 35 | S1 33, S3 2 | **S1** | **94%** |
| `relevant ground` | 30 | S1 28, S3 2 | **S1** | **93%** |
| `raw ground` | 21 | S1 19, S3 2 | **S1** | **90%** |
| `ground item` | 22 | S2 20, S4 2 | **S2** | **90%** |
| `ground truth` | 22 | U 17, S3 3, S4 2 | **U** | 77% |
| `DDD-ground-*` | 167 | U 117, S1 17, S3 17, S2 16 | **U** | 70% |

**The compounds are 90–100% pure, and that is a result rather than an artefact of the rules** —
GATE 1 rule 2 forbade assuming sense from the compound, and each of these was assigned occurrence by
occurrence from its sentence.

**What follows for the migration.** The compounds are its **real, mechanically separable surface**,
and they were invisible to both the proposal and the assessment, which enumerated named compounds
and missed the volume: the five unnamed compounds Emil asked about carry **236 occurrences**, more
than the named compounds `declared ground`, `accessible ground`, `missing ground` and `institutional
ground` combined (68).

**The two exceptions are the two that matter.** `ground truth` and `DDD-ground-*` are the only
compounds that do not cluster, and both are unmigratable for different reasons — the first is an
imported machine-learning idiom whose whole point is that it conflates the label set with the world,
the second is a permanent identifier.

---

## 5. The unassignable rows — the most valuable ones, per the charter

**244 projected (8.6%).** Four named clusters, each adjudicated once with its reason:

| Cluster | Rule-assigned | Why it will not sit in one sense |
|---|---|---|
| **`DDD-ground-*` identifiers** | 116 | A node identifier, not a use of the word. The five claims it names are themselves split (S2 and S1), so the ID inherits no sense |
| **ordinary English** | 32 | *"new ground"*, *"common ground"*, *"its ground has changed"*, *"the claim it grounds"*. **Not the technical term at all.** A global search-and-replace would corrupt these, and the migration needs them counted as their own answer |
| **`ground truth`** | 13 | An imported idiom: the held label set (S2) standing in for the world (S1). The idiom exists *because* the two are conflated, so assigning either would erase what it is |
| **`missing ground`** | 11 | Spans S1 and S3 irreducibly: **a relevant condition (S1) inadequately represented at the act (S3)**. It is the gap *between* two senses and cannot be one of them. The proposal's own table maps it to "basis gap", which concedes the same point |

**`missing ground` is the row the migration will be hardest on**, and it is hard for a structural
reason rather than a linguistic one: it names a *relation between two of the senses*, so it survives
the split only if the split gives it somewhere to live. The proposal saw this and answered it; the
audit confirms the answer is required, not optional.

**The ordinary-English cluster is the one nobody costed.** It is the reason the proposal's own
implementation step 7 — *"treat an unqualified use of ground as a drafting warning, except in
quotations or historical notes"* — needs a third exception it does not have: **and except where it
is not the technical term.**

---

## 6. What is asked at this gate

1. **Rule the method's honesty**: 64% deterministic, 36% sampled at n=100 with intervals shown. The
   alternative is a second pass hand-reading all 1,022, which the session can do and estimates at
   roughly the length of this gate. **The session's view is that it is not needed for D-3** — S2's
   lead is far outside every interval — but it is Emil's call whether the audit should be exact.
2. **Note §1.1**, which reframes D-3's first question: canon is bilingual S1/S3; the software is 92%
   S2. Whichever sense keeps the word, one side of the programme migrates nearly everything.
3. **Note §3.1** — the apparatus defines `ground` as the read-only surface an actor inspects and
   cites `core/00` for it, while `core/00` defines it as what determinations are made against.
   That is a live miscitation across the seam and may deserve its own repair irrespective of the
   migration.
4. **Confirm the unassignable clusters** at §5, particularly that ordinary-English use is counted as
   its own answer rather than folded into a sense.
