# GATE 1 — citations at `v5.12.0`, W1's occurrences, and three plans

**Status: draft-pending-ruling.** Nothing in the manuscript is touched. This gate changed no claim,
no term and no prose; the whole of its diff is this document and the session's arrival record.

**Read at:** `actor-indexed-determination` `81f6929` · `decision-driven-design` `54f00eb`
(both repositories fetched at head on the session's branch, `claude/paper-a-w1-revision-b8sx45`).

**The tag, verified rather than assumed.** `git rev-parse 'v5.12.0^{}'` →
`81f6929d7525bcb1f2d07b5ce5bf3c6ed6d4275d`, which is `origin/main`'s head. Head and tag are the
**same commit**, so canon at head is canon at `v5.12.0` exactly as the prompt asserts. Tag message:
*"v5.12.0 — Definitions that were never in the registry, and a collision the store won"*. The
projection's pin at arrival is `v5.9.0` (`graph/upstream.yaml`), held there by ruling.

---

## 1. Every citation re-verified at `v5.12.0`

Run against the manuscript unchanged, at both refs, with the instruments that live beside it.

| Instrument | at `v5.9.0` (the pin) | at `v5.12.0` (the target) |
|---|---|---|
| `check-quotations.py` | 29 verbatim, 0 disclosed-partial, **0 failing** | 25 verbatim, **4 failing** |
| `check-appendix.py` | 72 nodes, **0 discrepancies** | 72 nodes, **10 discrepancies** across 8 nodes |
| id resolution | 72/72 resolve | **72/72 resolve** — no E12-class loss |

**Nothing the paper cites has disappeared.** Every one of the 72 nodes still exists at `v5.12.0`;
what has moved is content and status, which is the governed case rather than the broken one.

### 1.1 The four failing quotations — confirmed, and each named

The prompt predicted four. The checker reports exactly four, and they are the four predicted.

| # | Site | Node | What happened upstream | Cost |
|---|---|---|---|---|
| 1 | §4.1, L366–368 | `DDD-frame-15` statement | **Retired** at `v5.10`, superseded by `DDD-frame-17` | the block is rewritten and the surrounding four modes go |
| 2 | §3, L274–276 | `DDD-frame-02` statement | **Amended** at `v5.10` — the residual-discretion clause only; first clause untouched | one clause of the block |
| 3 | §3.2, L310–314 | `term:residual-discretion` | **Amended** at `v5.10` — the separation the review asked for | the block is replaced by canon's longer text |
| 4 | §12, L1208 | `DDD-frame-15` compact form | the compact form **survives verbatim** in `DDD-frame-17`'s closing clause | **the citation moves; no prose does** |

Item 4 is confirmed as the prompt describes it. `DDD-frame-15`'s own retirement notes say so in
canon's words: *"The compact form — demand is never unmet, only ungoverned — is unchanged and is
carried by DDD-frame-17's closing clause."* The disclosure marker `— closing clause` stays valid;
only the id changes.

### 1.2 A fifth repair the checkers cannot see

**`DDD-measure-06` is retired at `v5.12.0`** (`retired_from: established`), superseded by
`DDD-measure-16` (availability to an arrangement) and `DDD-measure-17` (the coincidence, at
`projected`). That is the review's §2 — finding F-A — **already repaired in canon**.

The quotation checker does not catch it, because the paper never blockquotes `DDD-measure-06`. It
asserts the node inline, with a status label, in prose. A sweep written for this gate finds four
inline status assertions that are wrong at `v5.12.0`:

| Site | As the paper has it | at `v5.9.0` | at `v5.12.0` |
|---|---|---|---|
| §4.1 L368 | `[DDD-frame-15, projected]` | projected | **retired** |
| §4.4 L532 | `[DDD-measure-06, **established**]` | established | **retired** |
| §5.2 L605 | `[DDD-measure-06, **established**]` | established | **retired** |
| §6.1 L756 | `[DDD-measure-06, **established**]` | established | **retired** |

Two further sites cite `DDD-measure-06` without a status label (§1.2 L111, §8.4 L911), and the
conclusion's *"What is established"* list at L1220–1223 names *"that the measure exists exactly
where the acceptance predicate closes"* among the established four. **That sentence is the single
most exposed line in the paper**, and at `v5.12.0` it is false in the graph's own terms.

*The instruments are sound and this is not a defect in them.* `check-quotations.py` closes the gap
its docstring claims — block quotations — and says so. What has no instrument is the **inline
status assertion**, which is the more common form in the manuscript and the one that carries the
warrant a reader takes away. Proposed at Gate 4: the sweep above becomes a third checker beside
the other two, `check-status.py`, so the next pin advance cannot leave a retired node labelled
`established` in prose. **Flagged for ruling, not built yet.**

### 1.3 Appendix A's ten discrepancies

All ten are content movement on nodes that still resolve; none is a missing id. They are listed so
the regeneration at Gate 4 can be checked against a prediction rather than accepted on trust.

| Node | What moved |
|---|---|
| `DDD-frame-15` | statement **and** status (retired) |
| `DDD-measure-06` | statement **and** status (retired) |
| `DDD-frame-02` | statement — the residual-discretion clause |
| `DDD-delivery-01` | statement — `mechanical delivery` → `act-triggered delivery` |
| `term:residual-discretion` | canonical wording — the four-way separation |
| `term:verdict` | canonical wording — the `specification demand` parenthetical moved to a new `denominations:` field |
| `term:composite-actor` | canonical wording — a definition promoted above the existing line |
| `term:seam` | canonical wording — same |

Appendix A is regenerated wholesale at Gate 4 and never hand-edited. Two rows will also **appear**
that are not in the table above, because the body will newly cite `DDD-frame-17` and
`DDD-measure-16`/`DDD-measure-17`.

### 1.4 The validators, at head, before anything moves

| Gate | Result |
|---|---|
| `python3 validate-core-order.py core/` | **OK** — 5 documents, 5 terms, 4 embedded, 0 errors, 0 warnings; 67 pins resolved, 0 basis-loss, 0 content-drift |
| `python3 scripts/validate-claims.py core/claims/` | **valid** — 26 claims, **6 warnings**, exactly the six `CLAUDE.md` records for `v5.11.0` |
| `python3 scripts/validate-claims.py core/decisions/ --decisions` | **valid** — 21 decisions |

One note, reported because it is a surprise rather than a failure: running the ordering validator
over the **repository root** rather than `core/` raises four `E13` errors on `core/14-maturation.md`
and `core/16-calibration-ledger.md` (embeds of four unpinned upstream ids). CI runs it on `core/`,
which is the documented gate and is green, so this is **not a regression and not this session's**.
It is recorded here because it is the shape of an escaped decision about the instrument — a check
that passes because of where it is pointed — and it belongs on a successor list, not in this
session's scope.

---

## 2. W1 — the occurrences, enumerated, with the ambiguous cases separated

### 2.1 What W1 is, and the one rule that governs it

W1 renames the **population sense** of *ground* — sense **S5** in the ground migration's
classification, *the population the task faces* — to **deployment distribution**. It touches no S1
(conditions in the case), no S2 (representations the arrangement holds) and no S3 (representations
delivered at the act). **Any occurrence ambiguous between S5 and another sense defers to the
migration rather than being ruled here.**

The classification is not re-derived. It is the ground-migration session's, execution-grade and
committed at `meta/sessions/2026-08-27-ground-migration/`, read here through
`w0-full-v2.json` against the audit's own extract.

### 2.2 A count in the charter that does not reconcile — reported, not worked around

The package `README.md` says *"88 of its 88 mutable occurrences sit in the two papers"*; the
invocation says *"88% of which lives inside this paper and the measure note"*; the prompt's R-5
says *"88 occurrences of W1 sit in these two artefacts."* Against the committed classification:

| Quantity | Count |
|---|---|
| S5 occurrences, whole corpus | 97 |
| of which immutable (session records, a cut release descriptor) | 9 |
| **S5 mutable, whole corpus** | **88** |
| S5 mutable excluding `product-cli` (W4, ruled separately) | 87 |
| **S5 mutable in the two manuscripts** | **31** (measure note 26, Paper A 5) |
| S5 mutable anywhere under `papers/` | 39 |

**88 is the corpus-wide mutable total, not the count in the two papers.** The two manuscripts hold
**31 of 88 — 35%, not 88%.** The migration plan's own W1 row is closer and still not exact: it
records *"87 mutable, 29 in merged papers"* where the extract gives 31.

This does not change what the session should do; W1 is still separable and still worth carrying
here. It changes what the session may **claim** to have done. The close report will say
*31 of 88*, and the migration's remaining W1 surface is **57 occurrences, not zero.**

### 2.3 The enumeration, with dispositions

Thirty-one occurrences, each read in its own file at head. **Not every S5 occurrence is W1's to
move**, and the exclusions are the substance of this section.

**Paper A — 5 occurrences**

| Line | Text | Disposition |
|---|---|---|
| 502 | §4.4 *"over the distribution of ground the task faces"* | **move** — flagged, §2.4 |
| 672 | §5.3 *"the verdict function and the ground distribution"* | **move** |
| 1376 | Appendix A, `DDD-measure-01` row | **defer** — generated |
| 1382 | Appendix A, `DDD-measure-11` row | **defer** — generated |
| 1420 | Appendix A, `term:verdict` row | **defer** — generated |

**Measure note — 26 occurrences**

*Move (16):* L27, L41, L114, L129, L466, L482, L493, L495, L601, L651, L713, L842, L899 —
thirteen straightforward — plus L22 and L88 (flagged, §2.4) and L464 (flagged, §2.5).

*Defer (10):*

| Line(s) | Why |
|---|---|
| 138, 484, 879 | each reproduces `DDD-measure-12`'s statement verbatim — *"fixed by the task, the tolerance, and the ground distribution"* — as an italicised quotation. The node still says `ground distribution` at `v5.12.0`. Renaming would make the note misquote a live claim |
| 102 | inside a blockquote restating `term:verdict`'s definition. The registry still reads `ground distribution` at `v5.12.0` |
| 923 | `measure-nonuniform-ground.py` — a **filename** for an asset in the principle repository's `core/assets/`. The audit's extract does not flag it as an identifier; this session does |
| 1001, 1010, 1011 ×2, 1035 | the note's own node table — canon's words |

**Totals: 18 proposed moved, 13 deferred, of 31.**

Reproducible: `w1-enumerate.py` in this directory prints the table and asserts that every S5
occurrence the classification names in the two manuscripts carries exactly one disposition. It
fails loudly if the manuscript has moved under the enumeration — which it has, once, and the
next paragraph is that finding.

**The classification's line numbers for Paper A are stale, and the staleness is instructive.**
The audit's extract was taken on 2026-08-24; the item-4 session regenerated Appendix A the next
day with a `kind` column, moving every appendix row down by eleven lines. So three of Paper A's
five S5 rows point at the wrong lines — `1365`, `1371`, `1409` in the extract against `1376`,
`1382`, `1420` at head. Nothing is lost, because the sense assignment travels with the
occurrence rather than the line, but a migration executed by line number would have edited three
wrong rows. The enumerator carries both numbers and reconciles neither silently. **The measure
note has not moved since the extract, and Paper A itself is unchanged since the review's
`40d277f` in every respect but that regeneration.**

### 2.4 The ambiguous set, separated as the rule requires

**The `ground the task faces` pair.** The classification splits a three-word difference across two
senses: *"the **distribution of** ground the task faces"* is S5 (Paper A L502; measure note L22,
L88), while *"over **the** ground the task faces"* is S1 (measure note L107, L911). Both readings
are defensible and the boundary is invisible to a reader.

Renaming the S5 half and leaving the S1 half produces, inside one document, *"the deployment
distribution the task faces"* three lines from *"the ground the task faces"*. That is either the
migration doing exactly its job — disambiguating a word that carried two senses — or it is a
migration artefact that will read as an inconsistency to a reviewer who does not hold the sense
table. **This is a ruling, and it is Emil's.** The session's recommendation is to **move** the three
S5 members and leave the two S1 members untouched, because leaving them is what "renames the
population sense only" means; but the three are flagged rather than moved silently.

**Two occurrences that are S5 by the audit and read as elliptical.** Measure note L482 (*"41% of
the whole on the benign ground, 57% on the uniform"*) and L493 (*"the skewed ground exercises it
with `P` varied"*) drop the noun the distribution qualifies. They are S5 — the three deployments
are the population — and they are listed as moves, but each needs a rewrite rather than a token
swap: *"on the benign deployment distribution"*, *"the skewed distribution"*.

### 2.5 One coupling W1 creates, and it is not cosmetic

Measure note §5.4's heading is *"`P` varied → non-uniform ground"*. Its reproducing asset is
`core/assets/measure-nonuniform-ground.py`, **upstream and out of this session's reach**. Renaming
the heading while the asset keeps its name puts a section and the script that computes it under two
different words. Three dispositions, and the session recommends the second:

1. rename the heading and leave the asset — a visible divergence, honest, resolved by W2;
2. rename the heading and **say so in one clause** — *"worked by `measure-nonuniform-ground.py`,
   named before the vocabulary moved"*;
3. defer the heading to W2, so section and asset move together.

### 2.6 Two consequences of touching the measure note at all

**Paper A pins the measure note by commit.** Its front matter cites the note *"by path at commit
`aa7e135`"*. The note is unchanged since `aa7e135` — verified. The moment W1 edits it, Paper A
either keeps citing a commit whose prose says `ground distribution` while Paper A's own says
`deployment distribution`, or advances the citation to a commit this session creates. **Ruling
needed at Gate 4;** the recommendation is to advance it, in the same commit, with the reason stated
in the front matter.

**The measure note has no checkers.** Paper A has `check-quotations.py` and `check-appendix.py`;
the note has neither, and its node table is hand-carried at `v5.7.0`. So the ten deferrals in §2.3
are protected by this session's reading and by nothing else. That is a finding about the note, and
it is why the deferral list is enumerated line by line above rather than summarised.

---

## 3. R-1 — the survey plan

**The survey is reading before it is drafting.** This section is the plan; the section itself is
Gate 2's, and no differentiation is claimed here that the reading has not yet earned.

### 3.1 Locators can be verified in this session

Confirmed: outbound HTTPS resolves and publisher pages, DOIs and repository records are reachable.
So the Hayek precedent's standard applies in full — **every locator verified directly, or flagged
unverified in its own entry with the reason.** The Tesler entry stays as the pattern for a source
with no primary publication.

### 3.2 A first catch, before the survey starts

The review's own locator for Hollnagel and Woods is
`10.1201/9781420005684`, given as *"Woods and Hollnagel, Joint Cognitive Systems"*. That DOI
resolves to **Woods & Hollnagel (2006), *Joint Cognitive Systems: Patterns in Cognitive Systems
Engineering***, CRC Press — **not** Hollnagel & Woods (2005), *Joint Cognitive Systems: Foundations
of Cognitive Systems Engineering*, CRC Press, ISBN 0-8493-2821-7, which is the volume that states
the joint cognitive system as a unit of analysis and is the one the review's prose is about.

Two books, reversed author order, one year apart, sharing a main title. **This is the Hayek
facsimile check earning its keep on the first entry**, and it is the reason the plan below names an
edition for each work rather than a name.

### 3.3 The seven entries, with candidate locators and the axis each is differentiated on

Every axis below rests on **filed canon**. Q44 and Q45 sharpened the session's reading of where the
differences lie; they are unfiled, they are cited nowhere, and no distinction in the drafted section
will depend on them. Where a distinction needs them, it is written register-native as the paper's
own analysis or it waits.

| Work | Candidate locator (to verify at Gate 2) | What the framework **takes** | Where it **differs**, and on which filed node |
|---|---|---|---|
| **Hutchins**, distributed cognition | *Cognition in the Wild*, MIT Press 1995, ISBN 9780262082310 (pb 9780262581462) | the arrangement, not the individual, as the cognitive unit — and the priority is Hutchins's, not the framework's | descriptive rather than governing: no assurance axis, no accountable principal. `term:arrangement`, `DDD-frame-03` |
| **Hollnagel & Woods**, joint cognitive systems | *Foundations*, CRC Press 2005, ISBN 0-8493-2821-7; and *Patterns*, Woods & Hollnagel 2006, doi:10.1201/9781420005684 | **the closest neighbour, and the one that most narrows the novelty claim** — the human–machine ensemble as one control process | the **supply partition**: where a resolution comes from versus what assures it, and standing versus occasioned supply. `DDD-frame-03`, `DDD-cost-09` |
| **Leveson**, STAMP | *Engineering a Safer World*, MIT Press 2011, ISBN 9780262016629; OA edition, ch. 4 | safety as a control-structure property, and inadequate control as the failure unit | **filing versus delivery**: STAMP's constraint can be authored and absent at the act, and the model has no place to record that. `DDD-delivery-01`, `DDD-delivery-02` |
| **Horvitz**, mixed-initiative | CHI '99, pp. 159–166, doi:10.1145/302979.303030 | initiative as an allocation decision per interaction, not a fixed assignment | **commitment levels** — outcome, policy, principal — as what the allocation is *of*. `term:commitment-level` |
| **Bovens**, accountability | *European Law Journal* 13(4):447–468, 2007, doi:10.1111/j.1468-0386.2007.00378.x | accountability as a **relation** to a forum, not a virtue of the actor — the framework's `DDD-frame-08` is the same move | the relation as a **design-time checkable property of an engineering arrangement**, with a named incompleteness. `DDD-frame-08`, `term:accountability` |
| **Matthias**, responsibility gap | *Ethics and Information Technology* 6(3):175–183, 2004, doi:10.1007/s10676-004-3422-1 | the gap as a real structural consequence of learning systems | the gap read as **an arrangement naming an executor and no principal** — fixable rather than novel. `DDD-frame-08` |
| **Meaningful human control** | Santoni de Sio & van den Hoven, *Frontiers in Robotics and AI* 5:15, 2018, doi:10.3389/frobt.2018.00015 | tracking and tracing as two separable conditions | **delivery**: a tracing condition satisfied in the record and failed at the act is *escape that presents as governance*. `DDD-delivery-02` |

### 3.4 The standard each entry meets, and the shape of the section

The measure note's §8 set the standard and it is the one to meet: **what the framework takes, and
where it differs** — not a citation list. Each entry closes on both, in that order, with the taking
first, because the review's finding is that the paper claimed absence it had not surveyed.

Proposed shape, for ruling: the existing §11's ten short neighbourhood paragraphs are **kept and
compressed**, and the seven works above are added as a **comparison table plus one paragraph each**
— the reviewer's own recommendation in their §12.7. Estimated addition: **1,200–1,600 words**.

### 3.5 What the survey may conclude, and what it may not

The framework's genuine difference is more statable now than when the review was written. It is
still a difference the survey has to earn. **No entry will be drafted before its source is read**,
and where the reading does not support a difference, the entry will say the framework takes and
adds nothing — which is a finding, not a failure.

---

## 4. R-2 — retitle candidates

*The Missing Parameter* claims absence from prior work the paper has not surveyed. The triage
accepts the retitle. Four candidates, with what each costs.

| # | Title | What it does | Cost |
|---|---|---|---|
| **1** | **Actor-Indexed Determination: where consequential choices are resolved, what assures them, and who answers** | makes **no absence claim at all**; promotes the paper's existing subtitle, which already describes the contribution accurately | loses the memorable phrase; the paper becomes eponymous with the repository |
| **2** | Indexing Determination to the Arrangement: a synthesis of resolution, assurance, delivery and accountability | states the **narrowed claim** in the title, in the reviewer's own terms | "synthesis" in a title is a hostage; it invites the question the survey must answer |
| **3** | A Missing Parameter in Complexity-Allocation Accounts: actor-indexed determination | closest to the reviewer's own proposal; **concedes visibly**, which has been this paper's credibility mechanism | keeps an absence claim, narrowed to a named literature the survey must then actually cover |
| **4** | Resolution, Assurance, Delivery, Accountability: an auditable framework for actor-indexed determination | leads with the four separated coordinates the reviewer called the durable core | reads as a list; buries the index |

**Recommendation: 1, with 3 as the alternative.** Candidate 1 is the only one that cannot be
falsified by the survey it precedes. Candidate 3 keeps continuity with the merged version and
concedes in the title, which is a real virtue — but it makes a scoped absence claim, and the scope
("complexity-allocation accounts") is exactly the neighbourhood where Brooks, Tesler and Meyer sit
and where the claim is most nearly defensible. **Either is defensible; 2 and 4 are not
recommended.**

---

## 5. R-4 — the supplement split's proposed boundary

### 5.1 The boundary rule, stated so it can be applied rather than argued case by case

> **A passage moves to the supplement when it is about the graph. It stays when it is about the
> world, or about how much warrant the paper has.**

Filing history, minting decisions, pin mechanics, node tables and instrument descriptions are about
the graph. *"This claim is `projected`, its evidence field is empty, and the study is unrun"* is
about warrant, and it **stays** — the review praised the disclosure discipline twice and the triage
says explicitly not to trade it for brevity.

### 5.2 What moves, and what it costs

Into `papers/paper-a/paper-a-supplement.md`, with the generator retargeted at it:

| Passage | Words |
|---|---|
| **Appendix A** in full — claims, decisions, terms, hypothesis-set tables | 3,542 |
| **Reproduction** — the three scripts and their invocation | 138 |
| The front matter's **pin apparatus** (one sentence stays in the body) | ~115 |
| **Note on claim status** — the five-value vocabulary list; a compressed honest paragraph stays | ~144 |
| §2.4's *"ruled ineligible for minting"* filing rationale | 52 |
| §3's *"both were minted only when a downstream projection needed them"* | 45 |
| §5.2's *"a dedicated node is pending filing on the open-questions wave"* | 116 |
| §11.1's *"it is not filed, and it is not filed for a stated reason"* | 70 |

### 5.3 The arithmetic, stated before it is a surprise at Gate 4

Measured at head, by the same method the review used — regex word tokens over the Markdown source,
which reproduces the review's own figures to within 1%:

| | Words | Body headings |
|---|---|---|
| Whole file | **15,250** (review: ~14,900) | — |
| Body, before Appendix A | **11,708** (review: ~11,600) | **63** (review: 63) |
| Appendix A | 3,542 | — |

Removing everything in §5.2 takes the body to roughly **11,030**. **R-1 then adds 1,200–1,600.**

**The supplement split does not by itself make the main paper shorter.** It lands at roughly
**12,200–12,600 words** — longer than it is now. Saying so at Gate 1 is cheaper than discovering it
at Gate 4.

If a shorter main paper is the objective, the reduction has to come from argument, and the four
honest candidates are: §5.2's closure ladder (which is being repaired anyway — the triage records
the axis-mixing as Emil's own Gate 1 ruling, and the ladder should end at constructively-closed);
§8's worked example (six subsections, structural rather than numerical); §9.5's study design; and
§10.3's boundary cases. **This is a ruling and the session does not take it.**

### 5.4 One thing the split must not do

The apparatus **stays** — it moves. `check-quotations.py`, `check-appendix.py` and `gen-appendix.py`
keep running, against the supplement instead of the body, and the close report says so. A
supplement that the checkers no longer read would convert a verified apparatus into a claim about
one, which is the exact failure the review credited the paper for avoiding.

---

## 6. What this gate did not do

Nothing in `papers/` is touched. No claim, term or decision is filed, amended or retired in either
repository. The pin stays at `v5.9.0` until Gate 4, where the advance is made with the predicted
W6/W7 results **stated before the operation** and verified after. Q44, Q45 and the ontology
explainer are read and cited nowhere.
