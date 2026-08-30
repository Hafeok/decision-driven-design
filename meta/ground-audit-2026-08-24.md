# The ground audit

**Filed 2026-08-24, Phase 1b session.** Interactive audit, four gates, Emil ruling at each.
**This audit changed nothing.** No term was renamed, no claim amended, no canon file touched. The
upstream repository was read and never written; `product-cli` was cloned read-only and never
written. The whole of the session's diff is this document, its instruments, and the session record.

**Read at:** `actor-indexed-determination` `37f508e` (= `v5.10.0`) · `decision-driven-design`
`92c7b2e` · `product-cli` `d0f4297`.

> **Erratum filed against this document:** `meta/ground-audit-2026-08-24-erratum.md`, by the
> ground-migration session of 2026-08-27, on Emil's ruling at that session's GATE 1 and GATE 2.
> Three corrections — the definition layer is **17 settled terms and one draft, not fifteen** (§3.1);
> **`ground channel` occurs 10 times, not zero**, one of them inside `term:arrangement`'s settled
> canonical text (§2); and the corpus at this document's own read commits is **2,843**, because the
> instrument counted this session's index line (§1). The findings, the four rulings and the wave
> shape are untouched, and the central finding was corroborated by the completed classification.
> **This forward reference is the only change to this file.** Its text stands as filed.

**Instruments and data**, reproducible, in `meta/sessions/2026-08-24-ground-audit/`:
`count-ground.py`, `extract-occurrences.py`, `classify.py`, `classification.json` (2,845 rows),
`residual-adjudication.json`, and the four gate reports.

---

## 1. What was counted, and how far it can be trusted

> **2,845 occurrences of `ground` and its variants, across 394 files, in three repositories.**

| Repository | Occurrences | Files |
|---|---|---|
| `actor-indexed-determination` (canon) | 523 | 82 |
| `decision-driven-design` (projection) | 1,036 | 104 |
| `product-cli` (software) | 1,286 | 208 |

**The instrument was wrong three times before it was trusted**, and each correction moved the
number. `_` is a word character, so the first pattern's `\b` never fired between `parse_` and
`ground` and it discarded every snake_case identifier as a false positive. Escaped newlines inside
Rust string literals hid four occurrences of the real YAML field name `ground:`. And the audit
counted itself, because its own instrument quotes its own regex. Naive 2,932 → corrected 2,845: **+14
recovered, −101 removed.** A single number would have concealed both movements.

**Classification is 64% deterministic and 36% sampled, and the two are never mixed in a number.**
1,823 occurrences were assigned by an ordered rule table in which every rule states why its
assignment is safe and **there is no default rule**. The 1,022 that matched nothing are spread over
249 files with a long tail; 100 were drawn at random and hand-read in context.

> **The estimate is decision-grade and not execution-grade.** It suffices to take the four rulings
> below. It does not suffice to cut a single file. **Before anything is migrated, the 1,022 residual
> occurrences need full classification** — a decision can be taken on a bounded estimate; a rename
> cannot be executed on one.

---

## 2. The classification

| Sense | Rule-assigned | Residual est. | 95% CI | **Total** | Share |
|---|---|---|---|---|---|
| **S2** representations the arrangement holds | 1,004 | 634 | [536, 731] | **1,638** | **57.6%** |
| **S1** conditions in the case | 273 | 215 | [133, 296] | **488** | 17.2% |
| **S3** representations delivered at the act | 270 | 61 | [14, 109] | **331** | 11.6% |
| **U** unassignable | 172 | 72 | [20, 123] | **244** | 8.6% |
| **S5** the population | 74 | 31 | [0, 65] | **105** | 3.7% |
| **S4** institutional rules | 30 | 10 | [0, 30] | **40** | 1.4% |

**The two halves of the programme use different senses, each nearly self-consistent** (rule-assigned,
exact):

| | S1 | S2 | S3 | S4 | S5 | U |
|---|---|---|---|---|---|---|
| canon | **101** | 24 | **110** | 3 | 31 | 49 |
| projection | **165** | 116 | **134** | 22 | 42 | 86 |
| software | 7 | **864** | 26 | 5 | 1 | 37 |

Canon is bilingual in S1 and S3 with S2 barely present. `product-cli` is **92% S2**.

### Cost columns, exact over rule-assigned occurrences

| Column | Count | What it means |
|---|---|---|
| **identifiers** | 820 | Claim IDs, crate and binary names, module paths, YAML field names, code symbols. A data migration or an ID change, never an edit |
| **immutable** | 260 | Session records (239) and release descriptors (21). **Classified and flagged, never migrated** — counting them as work would overstate the downstream total by about a quarter |
| **merged papers** | 164 | Paper A and the measure note, both already owed revisions |
| **canonical text** | 240 | Term registry, claim and decision files, both repositories |
| **embeds** | 26 | Require re-projection rather than editing |
| **pinned objects** | 4 | The only occurrences that fire W6 directly |

### The compounds cluster, 90–100%

`ground-cli`, `ground registry`, `grounding edge`, `ground table` — **100% S2**. `reading ground`
96% S3. `ground axes`, `uncontrolled ground`, `relevant ground`, `raw ground` — 90–95% S1.
**That is a result and not an artefact**: the classifier was forbidden to assume sense from a
compound, so purity had to be earned occurrence by occurrence.

**The volume was where nobody looked.** Five compounds nobody named carry **236 occurrences**; four
compounds the proposal named carry **68**. Two compounds the proposal named — `ground channel` and
`ground coverage` — occur **zero times anywhere**.

### The unassignable rows

| Cluster | Why it will not sit in one sense |
|---|---|
| `DDD-ground-*` identifiers | A node identifier, not a use of the word — and the five claims split across senses (`-02` is S2, `-05` is S1) |
| **ordinary English** | *"new ground"*, *"common ground"*, *"the claim it grounds"*. **Not the technical term.** A global replace would corrupt them |
| `ground truth` | An imported idiom: the held label set standing in for the world. The idiom exists *because* the two are conflated |
| `missing ground` | **Spans S1 and S3 irreducibly** — a relevant condition inadequately represented at the act. It is the gap *between* two senses |

---

## 3. Three findings from canon itself

### 3.1 The definition layer is multi-sense — which decides what kind of repair this is

Every use of the word in `core/graph/terms.yaml`, the settled layer:

| Sense | Settled terms |
|---|---|
| **S1** | `term:ground` (*"what they are determined against"*) · `term:admission-test` (*"varying **the world**"*) · `term:act` · `term:determination` · `term:attribution` |
| **S3** | `term:actor` (*"resolves decisions by **reading ground**"*) · `term:judgment` · `term:poisoned-ground` (*"**present** but false: the substrate a determination **reads**"*) · `term:capacity` (*"the bits of ground it can have **in context**"*) · `term:overflow` · `term:residual-discretion` |
| **S2** | `term:closure` (*"the relevant ground is **observable**"*) · `term:encode-verify-split` · `term:accountability` (*"**ground channels**"*) |
| **S5** | `term:verdict` (*"the ***ground distribution***"*) |

> **Fifteen settled terms. Four senses. One registry.**

**This forecloses the prose-repair remedy.** Prose cannot be repaired to comply with `term:ground`
while ten other *settled* terms — including the one defining what an actor **is** — use the word
otherwise. The prose is not drifting from the definition; it is faithfully following a definition
layer that was never single-sensed. **The remedy is definitional.**

The registry alone uses S3 twice as often as S1 (12 against 6), so there is no clean origin to have
drifted from.

### 3.2 The apparatus cites canon for a definition canon does not give

`apparatus/encode-verify.md:21`:

> Ground is the read-only surface an actor inspects in order to act (`core/00`).

`core/00-primitives.md`, `term:ground`, **settled**:

> **Ground** — what they are determined against.

The first is S2; the second is S1, tested by varying the world. **Two apparatus files attribute an S2
definition to a source that gives an S1 one, by name, with a citation.** Recorded and routed as
freight; not repaired here.

**This is stronger evidence for the split than the three arrivals it was ruled real on**, because
those are *observations* that the word carries several objects and this is a *consequence* — the
overload has already produced a false citation across the repository seam, in a document whose
purpose is to state a principle correctly. **The split's first realised cost, not its fourth
prediction.**

### 3.3 The permanent identifiers do not name one sense

`DDD-ground-01`…`05` carry the word in their **identifiers**, cited **142 times**. `CLAUDE.md`
forbids renumbering, so **those occurrences cannot be migrated at any price** — the migration renames
the concept, never the node names. And the five claims do not share a sense: `DDD-ground-02` is about
*"orthogonal properties of ground relative to a filed decision"* (S2); `DDD-ground-05` is about
*"declaring the determinable space"* (S1).

---

## 4. The rulings (Emil, GATE 3)

### Q1 — **S1 keeps the word.** Ruled.

The conditions in the case whose variation moves the outcome past tolerance. On canon's authority:
it is the only sense with an **admission test**; three further settled terms repeat the same
*"against"* construction; `DDD-ground-05` makes it constitutively prior and `term:determinable`
supplies its formal structure.

**S3 is not a rival primitive.** Canon's S3 occurrences are verbs applied to the S1 object —
*reading*, *held*, *present*, *delivered*. **One object in three conditions, not three objects
competing for one name.** That is why the delivery vocabulary fits rather than needing a parallel
invention, and it is what makes the ~2,357 migrating occurrences mostly **re-expression rather than
re-conception**.

**The expensive option was taken with the cost in view**: S1 keeping the word migrates roughly twice
what the alternative would, because it puts `product-cli`'s 864 S2 occurrences on the migrating side,
including a serialised ledger field. Canon is the authority and the projection follows; volume prices
a disposition and does not choose one.

### Q2 — **Reuse the delivery vocabulary; do not mint beside it.** Ruled.

| Object | Name | Reuse |
|---|---|---|
| S2 — what the arrangement holds | **available ground** | `term:closure`'s *"observable"*; the existing `accessible ground` promoted |
| S3 — what reaches the act | **delivered ground**, act-indexed | `term:delivery` — *"a property of a decision **at an act-site**, never of the decision alone"* |
| the failure mode | **undelivered ground** | `term:undelivered` |

**`term:undelivered` is decisive**: *"filed, adequate, and never reached the act… escape, with a
distinguishing feature — **the ledger shows coverage**."* That is the proposal's `basis gap` of the
inaccessibility kind, already minted, already naming its own danger. Minting beside it would put two
canon names on one mechanism across the exact seam being closed.

**Q27 independently arrives at *"presumed discharge (Q18) transposed to the ground layer"*, which is
a fourth convergence. SR-1 undercounted at three.**

**`poisoned ground` changes sense without changing text** under this ruling — an S3 compound of an S1
head word. **It goes on the migration's must-touch list.** A term whose meaning moves silently is
worse than one whose text moves; it is the defect `term:floor` carried, and that one was found only
because a reader tripped over it.

### Q3 — **Provenance is several independent attributes.** Ruled.

`DDD-dec-26` ruled the five-way taxonomy *"ineligible for **minting** because its institutional slot
is Q27-gated"* — a ruling about minting, with a stated reason. **The gate was on the value, not on
the axis.** `DDD-ground-02` is the precedent: three *"orthogonal properties of ground relative to a
filed decision"*, already filed.

The evidence closes it: the enumeration's values live in **three different senses** — `controlled` is
S1, `observed` and `inferred` are S2, `institutional` is S4. **Three attributes flattened, not a
taxonomy.**

### Q4 — **Sense 5 leaves.** Ruled.

`ground distribution` → **deployment distribution**. The only sense with **zero identifier
occurrences**, zero pins, one `product-cli` occurrence. `term:verdict` already introduces `P` first
and names it second, which is what a separable parameter looks like.

**It rides with a paper revision rather than replacing one**: 29 of its 74 rule-assigned occurrences
are in the merged papers, the largest per-sense paper concentration in the audit.

---

## 5. The §7 / Q27 collision — reported, not resolved

The proposal's **§7** removes institutional rules from ground, distributing them to the acceptance
relation and to standing commitments. **Q27** fills institutional ground's empty provenance slot by
making a trusted source's output count *as* ground, with trust as a filed decision — *"trust converts
occasioned assurance into standing assurance"*. Under §7, most of what Q27 calls institutional ground
is reclassified out of ground entirely.

**Both texts are quoted in full in `gate3-rulings.md`.** The ruling belongs to the migration session,
before Q27 files. Three facts for it:

1. **`institutional ground` occurs 13 times, and zero times in canon.** Nothing in canon has to be
   unpicked either way. S4 is the smallest sense at 1.4% — the ruling is expensive, the edit is not.
2. **Q3's answer partially dissolves the conflict.** With provenance as independent attributes, §7's
   third bullet and Q27's mechanism are not in competition: the *record* carries an institutional
   provenance attribute with its trust decision, while the rule's *normative force* sits in the
   acceptance relation.
3. That is the assessment's own proposed reconciliation, and **Q3 supplies the mechanism that makes
   it available** rather than merely plausible.

---

## 6. The migration's shape — a recommendation, not a decision

**W0 blocks everything**: complete the classification of the 1,022 residual occurrences. §1.

The wave splits by **cost class**, not by repository, because the classes have different risk:

| Wave | Content | ~Occurrences | Why it separates |
|---|---|---|---|
| **W0** | complete the classification | 1,022 | Decision-grade is not execution-grade |
| **W1** | sense 5 leaves | 105 | Zero identifiers, zero pins. **Can land early and alone** |
| **W2** | canon's definitional repair; the S2/S3 states named by reuse; the registry's fifteen terms made consistent | ~250 | Small, and the most expensive to get wrong |
| **W3** | apparatus, projections, applications, both papers | ~450 | Rides with revisions already owed |
| **W4** | `product-cli` | 1,286 | **A data migration, not a rewrite** |
| **never** | session records, release descriptors, `DDD-ground-*` IDs, ordinary English | ~536 | Immutable, or not the technical term |

**W4 has an option canon does not**, surfaced without recommendation: because the software is 92% one
sense, **the serialised field `ground:` could stay while the concept is renamed**, at the price of a
documented divergence. It is the only edit in the migration that can break something that already
runs, and that trade-off is Emil's to make with the running system in view.

### Design requirement — relational concepts must have somewhere to live

> `missing ground` names a **relation** between S1 and S3 — a relevant condition inadequately
> represented at the act. **A five-sense partition with no place for relations would lose it, and
> lose it silently**, because each half classifies cleanly into a different sense.

Q2's ruling satisfies the requirement: `undelivered ground` is relational **by construction**,
because delivery is *"a property at an act-site, never of the object alone"*. That is why reuse beats
minting here on more than economy.

### The drafting-warning instrument needs a third exception

The proposal's step 7 treats an unqualified `ground` as a drafting warning *"except in quotations or
historical notes"*. **It needs a third exception: and except where the word is not being used as the
technical term.** The ordinary-English cluster is a projected 244 occurrences. A warning that fires
on *"the claim it grounds"* trains every author to ignore it — **the W6 scope lesson repeating**.

### What defers

`poisoned ground`'s silent sense change (§4, Q2) · the §7/Q27 reconciliation (§5) · the decoder
repair, which is research and which the split makes *easier to state* rather than fixes.
