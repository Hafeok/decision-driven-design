# GATE 3 — the §7 / Q27 reconciliation, and a finding that blocks Gate 4

**Status: draft-pending-ruling.** Two things in this gate, and the second is the larger.

---

# Part 1 — the reconciliation. **Tested against the corpus, not assumed.**

## The candidate, restated

> The rule's normative force sits in the **acceptance relation**; the arrangement's *representation*
> of the rule is a **reading**; the **trust decision** governs whether that representation may be
> relied on without independent verification. Three objects, currently one.

**The prompt requires this to be tested and not assumed. It was tested, it survives, and the test
changes it** — in the direction that makes Q27 cheaper to file, not dearer.

## The test: every occurrence of `institutional ground`, read

The compound is matched by an **anchored** rule (`institutional[ _-]ground`), which Part 2 shows is
the reliable class. **17 rows; 2 are the rule catching a neighbouring list item** (`inferred ground`
and `missing ground` in the same taxonomy list), so **15 genuine**. The audit reported 13; the
corrected figure is 15, and its claim that **zero are in upstream canon holds exactly.**

| | Count | |
|---|---|---|
| **Meta-mentions** — naming the category, not using it | **11** | Q27's own heading, the taxonomy definition, "the slot is Q27-gated", "rung 3's least settled kind" |
| **Actual uses** | **4** | `paper-a.md:882`, `paper-a.md:909`, and two `product-cli` predicates |

**All four actual uses denote a representation supplied by an authority. Not one denotes a rule's
normative force.**

| Use | What is actually being called ground |
|---|---|
| `paper-a.md:882` | *"how the endpoint behaves on a country the **institutional ground** does not cover"* — the country-rules table the model consults. **Coverage is a property of a representation** |
| `paper-a.md:909` | *"the correct output is **computed by rule** from **institutional ground**"* — canon **already separates them in one sentence**: `by rule` is the procedure, `institutional ground` is the data it reads |
| `serialisation-contract-declared.yaml` | *"The institutional ground item… the defaults are not wrong, they are simply **owned by someone else**"* — a serialiser's defaults. A fact, not a rule |
| `deployment-secret-containment.yaml` | *"what counts as a secret is **knowledge the template author has**"* — a fact held by an authority |

**And the three hard cases outside the compound resolve the same way.** *"The ground is
institutional — a statute, a contract"* (`01-determination.md:984`, `DDD-dec-27:243`) and *"a discard
decision with the regulation as its ground"* (rev18:1029) look like rules-as-ground. Read in place,
they are not: the determination track's own record field reads **"ground cited: the statutory
minimum for the records class (institutional, verified against the regulation's…)"** — what is cited
is **a value read from the statute**, with a provenance and a date. `DDD-dec-27`'s *authority
disagreement* is a disagreement about **which value the authority licenses**. Both are
representations.

> **Result: the corpus contains no use of `ground` for a rule's normative force. Zero.**

## What the collision actually is — one mis-listed word

§7 and Q27 do not compete for the same occurrences, because §7's object never occupied any. The
appearance of collision lives entirely in **the canon slot's own wording**, which all three
definitional occurrences reproduce verbatim:

> *institutional ground — supplied through **rules**, conventions, authority, or social practice*

**That list mixes a content kind with three supply channels.** `conventions`, `authority` and
`social practice` answer *how the material arrived*. `rules` answers *what kind of thing it is*.
One word, in one list, in the foundation document — and it is the whole of the §7/Q27 conflict.

## The reconciliation, as the corpus supports it

**Three objects, and the word only ever named one of them.**

| Object | Where it belongs | Status |
|---|---|---|
| The **rule's normative force** — what makes a resolution acceptable | the **acceptance relation**, or **standing commitments** | §7 is right, and **it was never ground.** §7 repairs a defect the corpus does not have |
| The arrangement's **representation** of a rule or of an authority's fact | **delivered ground**, carrying an **institutional provenance attribute** (SR-4) | **Q27's object. All four actual uses.** Reuse `term:delivery`'s vocabulary; mint nothing |
| The **trust decision** — may this be relied on without independent verification | a **filed governing decision**, Q27's mechanism, backing the provenance attribute | Q27's mechanism, unchanged |

**The repair is to strike one word**, not to relocate a category: remove `rules` from the supply list
so the slot reads *"supplied through conventions, authority, or social practice"*. What is supplied is
a representation, always. A rule's normative force is then visibly not on that list, which is §7's
whole point, achieved without moving anything.

**SR-4 completes it and makes the slot unnecessary.** With provenance as independent attributes rather
than a five-way enumeration, `institutional` becomes an attribute a record carries — alongside
`observed`, alongside `inferred`, as the proposal's own §6 already argued (*"an institutional record
may contain an inference"*) — and the trust decision backs that attribute. **There is no enumeration
slot left to dissolve.**

## The question G3 was asked

> **Q27 does not file onto a dissolving category.** It files onto the only category that was ever
> occupied, narrowed to exactly what its mechanism is about. **Filing it is safe, and it is safe
> before the migration cuts.**

**Consequence for the sense partition: S4 does not survive as a sense.** Its four real occurrences
are S2/S3 material carrying a provenance attribute; its eleven meta-mentions name a category. The
partition is **four senses plus attributes**, not five — which is SR-4 reaching the partition itself,
and it removes the smallest and least defensible sense without a single rename.

**One thing the reconciliation does not fix, stated so nobody expects it to.** Q27's own hardest
limit stands untouched: *"triangulation raises assurance within closure and never closes an open
predicate"*, and *"it yields assurance without a principal — six people saying the ice held is
evidence, and none bears your consequences."* Assurance and accountability remain separate axes.
The vocabulary makes the limit easier to state; it does not move it.

---

# Part 2 — **a finding that blocks Gate 4.** Reported and held.

## What happened

G3 required reading the S4 occurrences, because a reconciliation cannot settle on a category whose
membership is unknown. Reading them showed the S4 set was wrong. Tracing why showed something larger.

**GATE 1's acceptance rested on the residual being complete, which it is.** The 1,022 were read one
by one, in their own files, and every ruling is enumerated. **What Gate 1 did not examine was the
1,823 rows the audit assigned by rule, which it inherited exactly and by design.** Examining them for
G3 broke them.

## The measurement

A seeded sample of **60 rows drawn from the 1,823 rule-assigned**, hand-read in place.
**15 are wrong — 75% correct overall.** The errors are **not uniform**, and the split is the finding:

| Rule class | Sampled | Wrong | Correct | Rows in corpus |
|---|---|---|---|---|
| **Anchored** — the pattern matches at or beside the token: `software-module`, `ddd-ground-id`, `ground-distribution`, `characterised`, `watched-not-grounding`, `yaml-field`, `poisoned-ground`, `admission-test`, `relevant-conditions`, `declared-ground-axes`, `institutional-ground`, … | 39 | **0** | **100%** | **1,396** |
| **Prose-context** — the pattern matches a keyword up to 70 characters away, across clause boundaries `[^.]` does not stop: `accessible-available` (191), `reading-ground` (99), `delivered` (41), `ordinary-english` (32), `ground-coverage-assurance` (31), `rule-standard-context` (13), `missing-ground` (11), `distribution-context` (9) | 21 | **15** | **29%** | **427** |

> **The identifier- and compound-anchored rules are perfect. The prose-context rules are wrong about
> seven times in ten, and there are 427 of them — roughly 305 suspect rows.**

**Two of the eight were adjudicated in full, not sampled**, and both confirm the rate:
`rule-standard-context` — **11 of 13 wrong** (it matches `policy` within 70 characters, so *"outcome
variation across ground … a fixed **policy**"* and *"no ground **truth** … the **standard** varies by
rater"* both became S4). `distribution-context` — **4 of 9 wrong** (it matches `deployment` and
`distribution`, so *"relative to a task **distribution**, accessible ground"* became S5 when it is S2).

Typical misassignments, all from the sample: *"a determination against some **ground**"* filed as
ordinary English because the rule lists `some ground`; *"variation in **declared ground**"* inside
`term:actor` filed S3 because *"reading ground"* sits earlier in the same sentence; the release
descriptor's basis line `DDD-**ground**-03` filed S3 because `deliver` appears nearby; *"**Ground**
channels — axes readable **at act time**"* filed S2 when the predicate is an act predicate.

## Why this is a finding and not an error to fix quietly

**The audit was explicit about its own standard**, and it holds: *"every rule states why its
assignment is safe … there is no default rule."* The rules do state their warrant. **What no rule
states is its precision**, and the audit's §2 reported the rule-assigned half as *"exact"* against
the sampled half's confidence intervals — a distinction that turns out to run the wrong way. The
sampled half is now the better-measured one.

**It does not touch anything ruled so far:**

- **G1's residual work stands.** 1,022 rows, read individually, unaffected.
- **G2 stands.** Both sweeps read the registry directly and never consulted the classification.
- **G3 Part 1 stands.** `institutional-ground` is an anchored rule, 15 genuine rows, all read here.
- **SR-1 and SR-2 stand.** Both were ruled on canon's authority against the counts.

**What it does touch is Gate 4.** A migration plan is a per-file, per-occurrence instrument. The
wave table, the cost columns, and every "what moves and what re-words" line are computed off the
classification, and ~305 of its rows are suspect — concentrated in `accessible-available` and
`reading-ground`, which are precisely the S2/S3 boundary the delivery vocabulary is being reused to
name.

## What it would cost to close

**W0-bis: re-adjudicate the 427 prose-context rows.** Same method as W0 — read each in its own file,
one ruling per row with its reason, residual zero by construction. The anchored 1,396 stay inherited,
now with a measured warrant rather than an assumed one.

**427 rows is 42% of W0's 1,022, and W0 ran within this session.** No new instrument is needed:
`w0-classify.py` already merges per-row rulings and asserts coverage; the rulings files extend by one
range.

## The three options, priced

| | | |
|---|---|---|
| **A — run W0-bis now**, then Gate 4 | Gate 4 plans on a classification with a measured error rate throughout. Costs roughly 40% of W0 | **Recommended** |
| **B — defer W0-bis and plan Gate 4 anyway** | The plan's file lists and wave sizes carry ~305 suspect rows, unmarked. **This is the C-1 precedent's failure mode**, arriving one gate early: a plan that looks executable and is not |
| **C — defer the whole migration now**, W0-bis with it | Available, and cheaper than B. But G1–G3 have already produced the design rulings the audit said were the point, and none of them depends on the suspect rows |

**Recommended: A.** The finding is bounded, measured, and its remedy is the method that already
worked once in this session.

---

## What this gate asks

1. **The reconciliation** — three objects, the word only ever named one, the repair is to strike
   `rules` from the supply list, and **Q27 is safe to file.**
2. **S4 does not survive as a sense** — four senses plus provenance attributes, which is SR-4
   reaching the partition.
3. **The W0-bis finding** — 427 prose-context rows, ~305 suspect, Gate 4 blocked until they are read.
4. **Option A, B or C.**

**Nothing repaired. Nothing merged.**
