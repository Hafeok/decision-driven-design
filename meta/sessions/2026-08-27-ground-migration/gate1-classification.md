# GATE 1 — W0, the completed classification

**Status: draft-pending-ruling.** Nothing in canon is touched. This gate changed no term, no claim,
no prose; the whole of its diff is this document, its instruments, and its data.

**Read at:** `actor-indexed-determination` `ce2c477` (= annotated tag `v5.11.0`, verified: head and
tag are the same commit) · `decision-driven-design` `e81a454` · `product-cli` `d0f4297`.

**Instruments**, reproducible from this directory: `w0-classify.py`, `rulings/r001.py`…`r021.py`
(one ruling per occurrence, with the reason), `w0-full.json` (2,845 rows), `w0-residual.json` (the
1,022 this gate ruled), `w0-extract-head.py` (the head delta).

---

## 1. The classification is complete

> **All 2,845 occurrences now carry a sense or a recorded reason for carrying none. The residual is
> zero by construction** — `w0-classify.py` asserts that the rulings cover the residual exactly, and
> fails if one occurrence is unruled or twice-ruled.

| Sense | Rule-assigned (audit) | **Ruled here** | **Total** | Share |
|---|---|---|---|---|
| **S2** representations the arrangement holds | 1,004 | 532 | **1,536** | **54.0%** |
| **S1** conditions in the case | 273 | 247 | **520** | 18.3% |
| **S3** representations delivered at the act | 270 | 147 | **417** | 14.7% |
| **U** unassignable | 172 | 66 | **238** | 8.4% |
| **S5** the population | 74 | 27 | **101** | 3.6% |
| **S4** institutional rules | 30 | 3 | **33** | 1.2% |

**Method.** The audit's committed extract was taken unaltered, so the rule-assigned half is inherited
exactly and only the residual moved. Each of the 1,022 was read **in its own file**, not in the
240-character extract window. After the first file a decision rule was fixed and applied to every
one after it: **read the predicate applied to the word, never the compound** — world predicates
(*varies, moves, is uncontrolled, is a dimension*) are S1; store predicates (*held, available,
assembled, filed, cited, pinned, stale*) are S2; act predicates (*read at, delivered, consulted,
present, in context, bound at the as-of*) are S3; rule predicates S4; population predicates S5.
The rule is stated at the head of `rulings/r005.py`, where it was fixed.

---

## 2. Two sense boundaries moved. **Findings, held, not errors.**

The audit's sampled estimate carried 95% confidence intervals. Two senses landed outside theirs.

| Sense | Sampled est. | 95% CI | **Counted** | |
|---|---|---|---|---|
| **S3** | 61 | [14, 109] | **147** | **+38 above the upper bound** |
| **S2** | 634 | [536, 731] | **532** | **−4 below the lower bound** |
| S1 | 215 | [133, 296] | 247 | in CI |
| U | 72 | [20, 123] | 66 | in CI |
| S5 | 31 | [0, 65] | 27 | in CI |
| S4 | 10 | [0, 30] | 3 | in CI |

**S3 is the one that matters, and it is not marginal.** Full-corpus S3 goes from the audit's 331 to
**417, up 26%.** The 100-occurrence sample drew six S3 rows; the true rate was fourteen in a hundred.

**Where the extra S3 came from** — and it is not scattered:

| | S3 rows added |
|---|---|
| `apparatus/` (tool-surfaces, tool-contract, encode-verify, the-skill-floor, prefix-stability) | 38 |
| upstream `core/` documents | 28 |
| holding notes, both repositories | 26 |
| session records (immutable) | 10 |
| claim, decision and registry files | 18 |

**Why the sample missed it.** The rule table's S3 rules keyed on *delivery* and on *reading*.
The apparatus does neither: it says **exports**, **bounds**, **consumes**, **sits on**, **fires
against**, **is in the prefix**. `tool-surfaces.md` alone contributes nine — a *ground exporter*
"returns content the actor must interpret", and *Roots* "bounds the ground". Those are act
predicates in every case, and no rule was looking for them.

**What it does to SR-1 and SR-2: nothing, and it strengthens SR-2.** S1 keeping the word was ruled
on canon's authority against the counts, so a count moving cannot disturb it. And every one of the
86 new S3 occurrences is a *verb applied to the S1 object* — exported, bounded, consumed, held in a
prefix — which is exactly SR-2's "one object in three conditions, not three objects". **The sense
that grew is the sense SR-2 says is not a rival primitive.** The delivery vocabulary now has 26%
more work to do than the audit priced, and no more kinds of work.

**The one caution.** S3 at 417 is now larger than the *whole* of what W2 was scoped to touch. Its
distribution is the reason the W2/W3 boundary needs re-drawing at Gate 4: 38 of the new rows are
`apparatus/`, which the audit put in W3 as "rides with revisions already owed", and `apparatus/`
turns out to be where the delivered sense actually lives.

---

## 3. The definition layer is larger than recorded: **17 settled terms, not 15**

The audit's §3.1 table, the finding the whole migration rests on, is **wrong in both directions** —
and correcting it makes the finding stronger.

> **18 registry entries use the word at `v5.11.0`: 17 settled and one draft. They carry four senses.**

| Sense | Entries | |
|---|---|---|
| **S1** (7) | `term:ground` · `term:admission-test` · `term:determination` · `term:act` · **`term:tolerance`** · **`term:answerability`** · **`term:swarm-gate`** | |
| **S3** (7) | `term:actor` · `term:judgment` · `term:poisoned-ground` · `term:capacity` · `term:overflow` · `term:capability` · **`term:residual-discretion`** *(draft)* | |
| **S2** (3) | `term:closure` · `term:encode-verify-split` · **`term:arrangement`** | |
| **S5** (1) | `term:verdict` | |

**The audit named two terms that do not use the word at all** — `term:attribution` and
`term:accountability`, zero occurrences each. The "ground channels" it credited to
`term:accountability` is in **`term:arrangement`**. **And it omitted six that do**: `term:tolerance`,
`term:arrangement`, `term:answerability`, `term:capability`, `term:swarm-gate`, and the draft
`term:residual-discretion`.

**The count moved from 15 to 17 settled and the sense split stayed four.** The prompt's own
statement of the finding — *"fifteen settled terms carry four senses of one word between them,
including the term defining what an actor is"* — is right in substance and wrong in its number, and
the corrected number is worse: **`term:tolerance` is S1 and `term:arrangement` is S2, and both sit
in `00-primitives.md`, the first document a reader meets.** The multi-sense defect is not merely in
the registry; it is on one page of it.

**Also corrected: S1 and S3 are tied at seven each.** The audit reported the registry as using S3
twice as often as S1 (12 against 6) and concluded "there is no clean origin to have drifted from".
The corrected figures are 7 and 7 by entry, 9 and 16 by occurrence. The conclusion survives; the
asymmetry that supported it does not.

---

## 4. What the full pass found that no sample could

### 4.1 A sixth object, and a seventh — both in `product-cli`, both invisible to a rule table

**`ground term` — the RDF/logic term of art (11 occurrences).** In
`product-core/tests/graph_capability_tests.rs`, `let ground = |store| … .filter(|q| !matches!(q.object,
Term::BlankNode(_)))` — a *ground term* is one containing no variables or blank nodes. Related to
none of S1–S5. Eleven occurrences in a local closure name and its assertion messages.

**`ground` as a CSS surface colour (6 occurrences).** *"the two surface **grounds** the page and its
cards sit on"*, *"the card **ground** one step above `--surface`"*, *"the page's **ground** colour"*
— in `.ddd/render.html`, a design-token decision, and two `seam-web-token-*` files. Background
against foreground, ordinary design vocabulary.

**Both matter to the drafting-warning instrument, and to G2.** The audit already ruled that the
warning needs a third exception for ordinary English. These are two more classes it must not fire
on, and the second is a name collision inside the repository that carries the serialised field.

### 4.2 `ground channel` occurs **10 times**, not zero

The audit reported *"two compounds the proposal named — `ground channel` and `ground coverage` —
occur **zero times anywhere**"*. Half of that is wrong. `ground coverage` is indeed zero.
**`ground channel` occurs 10 times, and one of them is inside settled canonical text** —
`term:arrangement`: *"executor, prior commitments, **ground channels**, checks, reviewers, record,
and accountable principal"*. The others are `core/00-primitives.md:129`, three in
`projections/tracks/01-determination.md`, three in `papers/paper-a/paper-a.md`, one holding note,
one session record. All S2.

**This is a migration surface the audit told the plan it did not have**, and it is in the registry.

### 4.3 The multi-sense defect has been **translated**

`i18n/ordliste-dansk.md:17` glosses `grund` as **both senses in one entry**: *"Det, en beslutning
afgøres **imod**"* — what a decision is determined against, S1 — *"— det læsbare underlag, aktøren
inspicerer"* — the readable substrate the actor inspects, S3. The Danish glossary is not drifting
from the registry either; it is faithfully translating a definition layer that was never
single-sensed. **The migration owes i18n a pass, and the audit did not budget one.**

### 4.4 The audit counted itself once more than it caught

Re-running the audit's extractor at its own read commits yields **2,843, not 2,845.** The two extra
rows are `meta/sessions/README.md:34` — the audit's own session-index line, *"`2026-08-24-ground-audit/`
| Interactive audit — Phase 1b: the ground audit"* — written in its working tree and outside the
directory its `SELF` skip excluded. Its §1 reports catching 101 self-occurrences; there were 103.

**Nothing moves.** Both rows are immutable-class and both are U. **The corpus proper at the audit's
commits is 2,843**, and this gate classifies the committed 2,845-row extract in full so the two are
visible rather than quietly dropped. This session's own directory is excluded from every count it
takes, which is the same lesson applied a third time.

---

## 5. Every occurrence that will not sit in exactly one sense

**238 of 2,845 (8.4%).** The audit projected 244; it was right to within six.

| Count | Cluster | Why it will not sit in one sense |
|---|---|---|
| **116** | `DDD-ground-01`…`05` identifiers | A node identifier, not a use of the word. The five claims split across senses. **`CLAUDE.md` forbids renumbering: unmigratable at any price** |
| **59** | ordinary English | *"new ground"*, *"on the grounds that"*, *"common ground"*, *"the claim it grounds"*, *"groundwork"*, *"literature-grounded"*, *"cost the paper ground"*. A global replace corrupts every one |
| **13** | `ground truth` | The imported machine-learning idiom: the held label set standing in for the world. **The idiom exists because the two are conflated** |
| **13** | `missing ground` / *"ground is missing"* | **Spans S1 and S3 irreducibly** — a relevant condition inadequately represented at the act. The gap *between* two senses |
| **11** | the RDF `ground term` | §4.1. A sixth object, from logic |
| **10** | bare name citations | *"the ground area"*, *"the ground audit"*, *"the ground PRD"*, `"ground"` as a token in a checker's `SKIP` set. **No predication to read a sense from** |
| **6** | the CSS design token | §4.1. A seventh object, from design |
| **5** | names two senses at once | The provenance table's subject in Paper A and its two ancestors; the Danish gloss; the Paper A review's *"`G*` (relevant) vs `G_A` (accessible and delivered)"* |
| **3** | bare node-identifier citations | *"the ground-01 join"*, *"D-3/ground-04"* |
| **2** | the audit's own index line | §4.4 |

**The five-sense partition would lose the relational cases silently**, which the audit's design
requirement already predicted. There are now **18** of them, not 11: `missing ground` (13) plus the
five that name two senses in one phrase. Q2's `undelivered ground` is relational by construction and
covers the first cluster. **It does not cover the second.** A provenance table whose subject is
*"The ground is"* and whose four values are S1, S2, S2 and S4 has no home in a partition, and SR-4
is what dissolves it — the table becomes independent attributes on a record, and the subject stops
having to be one sense. **Recorded for Gate 4: SR-4 is not only a ruling about provenance, it is the
repair for five occurrences that no naming scheme could fix.**

---

## 6. Cost columns, now exact over all 2,845

The audit's were exact over the 1,823 rule-assigned only. Three moved.

| Column | Audit | **Exact** | |
|---|---|---|---|
| identifiers | 820 | **820** | unchanged — every identifier was rule-assigned |
| immutable | 260 | **260** | unchanged. By sense: S1 70 · S2 69 · S3 56 · U 42 · S4 12 · S5 11 |
| merged papers | 164 | **164** | unchanged (Paper A 100, measure note 64) |
| canonical text | 240 | **222** | −18: the audit's figure double-counted across the two repositories' claim directories |
| embeds | 26 | **26** | unchanged |
| pinned objects | 4 | **4** | unchanged. `term:ground`'s pin in `graph/upstream.yaml` is one |

**Never touched — immutable or U: 456. Remainder: 2,389.**

---

## 7. The corpus at head, because execution happens there and not at the audit's commits

**2,976 at head, against 2,843 at the audit's read commits: +133 across 11 files, +0 in `product-cli`.**
This session's own directory is excluded.

| Movement | | |
|---|---|---|
| +85 | the ground audit's own output (`meta/ground-audit-2026-08-24.md` 61, `successor-items-ground-audit.md` 24) | a document about the word |
| +19 | item-4 session records | **immutable** |
| +17 | `actor-indexed-determination/README.md` | **the one that needs attention** |
| +6 | `meta/sessions/README.md` | index rows |
| +3 | `DDD-dec-31` | new canon |
| +2 | `releases/v5.11.0.yaml` | **immutable** |
| +1 | `successor-items-item4.md` | |

**Upstream's `README.md` was rewritten in three commits after `v5.10.0`** (+515 lines), and 17 of its
lines now use the word — up from 2. It is outside `core/`, so it is not canon, **but it embeds
canonical definitions**: line 115 carries `term:closure`'s *"relevant ground is observable"* and
line 58 carries `term:arrangement`'s *"ground channels"*. A public-facing README reproducing two
registry definitions in two different senses is a migration surface, and it did not exist when the
audit was taken.

**Recommended, for the ruling:** classify the head delta at Gate 4 rather than now. 106 of the 133
are immutable or are the audit's own output; the 27 that are not sit in three files and can be read
in one pass alongside the plan.

---

## 8. What did not move

- **The compounds are still pure**, and now measured over the whole corpus rather than half:
  `poisoned ground` 100% S3 (66) · `ground-cli` 100% S2 (120) · `ground distribution` 100% S5 (58) ·
  `institutional ground` 100% S4 (13) · `ground channel` 100% S2 (10) · `ground axes` 97% S1 (77) ·
  `reading ground` 96% S3 (49) · `uncontrolled ground` 95% S1 (22).
  **One is not**: `ground state`, 13 occurrences, S2 7 / S1 4 / U 2. It is the only impure compound
  found, and it is the one `product-cli` puts in a status line.
- **`uniform ground` / `non-uniform ground` is S5**, 25 occurrences, 100% — a compound nobody named,
  in `core/09`, three canon assets and the measure note. S5 was 74 rule-assigned and is now 101.
- **The two halves are still bilingual**, and canon more sharply than reported: upstream is now
  S3 171 · S1 167 · S2 85, so the delivered sense is canon's *most frequent*, not its second.
  `product-cli` is 91% S2 (1,173 of 1,286), essentially unmoved from the audit's 92%.
- **`ground coverage` really is zero.**

---

## 9. What this gate asks

1. **The completed classification**, §1 — accept as the execution-grade basis W0 was to supply.
2. **The two moved boundaries**, §2 — S3 +26%, held as a finding. Nothing in SR-1 or SR-2 turns on
   it, and the redistribution is an input to the W2/W3 boundary at Gate 4, not a re-opening here.
3. **The definition layer at 17 settled terms, not 15**, §3 — a correction to the finding the
   migration rests on, in the direction that makes it worse.
4. **The four things the audit could not have seen**, §4 — two further objects under the word, a
   compound reported as absent that is in the registry, a translated defect, and a self-count.
5. **Whether the head delta is classified now or at Gate 4**, §7 — recommendation: Gate 4.

**Nothing here is repaired.** G2's sweeps are next and repair nothing either.
