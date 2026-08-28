# GATE 1 — the survey, the I-1 proposals, the I-2 counts, and the W1 recommendation

**DRAFT — PENDING RULING.** Nothing in this document has been ratified. It reports what the graph
says, proposes where a proposal was asked for, and holds.

Counts are counted. Every number below is produced by `survey.py` in this directory; the
classification behind §3 is `i1a-classification.yaml`, filed as data so a disagreement can be
located at a claim rather than at a total.

---

## 0. Fetch and verification

| Repository | Head | Tag |
|---|---|---|
| `actor-indexed-determination` | `403dede40416c5f90ec51f7e2b2226ba7fadf6f3` | `v5.10.0` = `37f508e92645c169312095b4274223ba03c89e51` |
| `decision-driven-design` | `efb46682251c74d8396ecf90518a38d1c711eab7` | — |

**The tag is found and it is not head.** `v5.10.0` resolves to `37f508e`, the Phase 1a merge (PR
#18). Upstream head is three commits further on — `8948db0`, `b1c1c0e`, `403dede` — and `git diff
v5.10.0..HEAD` touches exactly one file, `README.md`, +515/−57.

So the prompt's assertion holds on the substance: **canon at head is canon at `v5.10.0`**, and every
count in this document is a count of `v5.10.0` canon. It does not hold on the letter: head and tag
coincided at Phase 1b's arrival and no longer do. Reported rather than smoothed over, because the
next release descriptor's `commit` handling depends on which is true.

---

## 1. The kind × status table, verified at head

**Upstream — 63 claims.**

| kind | projected | reported | established | retired | total |
|---|---|---|---|---|---|
| conceptual | 29 | 3 | 0 | 1 | **33** |
| empirical | 11 | 1 | 0 | 0 | **12** |
| formal | 2 | 6 | 4 | 3 | **15** |
| normative | 3 | 0 | 0 | 0 | **3** |
| **total** | **45** | **10** | **4** | **4** | **63** |

**Downstream — 26 claims.**

| kind | projected | reported | established | retired | total |
|---|---|---|---|---|---|
| conceptual | 12 | 0 | 0 | 0 | **12** |
| empirical | 13 | 0 | 0 | 0 | **13** |
| formal | 0 | 1 | 0 | 0 | **1** |
| **total** | **25** | **1** | **0** | **0** | **26** |

**Combined — 89 claims, ten populated kind × status combinations.**

The scope correction is confirmed against the graph, not against the triage. `kind` is present and
legal on all 89 claims; there is no unpopulated field, no default, and no claim needing one.
The ten combinations are the upstream ten — downstream populates three of them, all already
upstream-populated, so the combined table adds no eleventh cell.

**`established` is four claims, all `formal`:** `DDD-frame-06`, `DDD-measure-02`, `DDD-measure-10`,
`DDD-measure-16`. This is the number I-4 writes to.

---

## 2. What the survey found before any proposal

Three facts that were not in the prompt and that bear on more than one item.

**(i) The largest cell is not the conceptual/projected cell.** It is, at 29 — but 45 of 89 claims
are `projected` and 41 of those 45 are `conceptual` or `empirical`. The corpus is young, and the
maturity field is doing most of its work at one value.

**(ii) `test` and `falsifier` are not alternatives in practice; they are strata.** Of the 29,
fifteen carry both, ten carry `falsifier` only, and four carry `test` only. **All four test-only
claims are definitions** under §3's criterion, and no mixed or substantive claim is test-only. The
field already separates a definitional subset — with perfect precision and poor recall (4 of 16).

**(iii) The rule-1 detector's first version was wrong, and the way it was wrong matters.** A
semicolon detector fires on `I(V;X)`. Six claims — `DDD-measure-02`, `DDD-measure-05`,
`DDD-measure-10`, `DDD-measure-13`, `DDD-delivery-01`, `DDD-cost-06` — are false positives from
mutual-information notation alone, and two of them are `established`. The masked detector is used
throughout §5; the unmasked count is reported alongside it so the size of the correction is visible.

---

## 3. I-1(a) — the 29 conceptual/projected claims, classified

The criterion, applied uniformly: a **definition** fails by non-application, no extension, or a
wrong joint; a **substantive** claim fails by a describable state of affairs; a claim is **mixed**
when its statement carries a separable stipulative limb *and* a separable assertoric limb.

| Class | n | Claims |
|---|---|---|
| **Definition** | **16** | `cost-05` `cost-30` `delivery-01` `delivery-02` `floor-02` `frame-01` `frame-02` `frame-03` `frame-12` `frame-13` `frame-16` `ground-02` `ground-03` `ground-05` `measure-15` `measure-17` |
| **Mixed** | **8** | `cost-01` `cost-09` `cost-12` `cost-20` `cost-25` `frame-11` `frame-14` `frame-17` |
| **Substantive** | **5** | `cost-08` `cost-11` `cost-13` `cost-22` `delivery-03` |

Per-claim reasons are in `i1a-classification.yaml`.

### The answer, and it is not the one the item anticipated

**`conceptual` is not coherent — 16 of 29 are definitions, and the reviewer's observation was
right.** But the split cannot be filed, because **the boundary does not run between claims. It runs
through eight of them.**

A `definitional` value would have to code `DDD-frame-17` — the predetermined/exercised/drawn
partition — as one thing or the other. It is a stipulated taxonomy *and* an exhaustiveness claim
*and* a carried-over compact form. Whichever value it takes, the other job it does is miscoded, and
the miscoding is now in a field an outside reader reads as authoritative. That is worse than the
present state, where `conceptual` is at least honestly vague.

`DDD-frame-11` is the sharpest instance and it makes the point without argument: **its `falsifier`
field already has two limbs of different type** — an audit question that cannot be posed without the
measure (definitional failure) and a demand reduction at fixed task and tolerance (empirical
failure). The claim is telling us it is two claims.

### The proposal, therefore, is a sequence and not a field

**Proposed: the split is real, is not filed in this session, and is filed after rule 1 is
enforced — because rule 1 is what makes it fileable.**

1. **Now (this session):** file nothing in `kind`. Record the finding and the dependency.
2. **After I-2's rule-1 pass:** the eight mixed claims split into a definitional limb and an
   assertoric limb, each with its own status — which is rule 1's own stated purpose, *"the unit of
   status change must be the unit of statement"*.
3. **Then, and only then:** `conceptual` → `definitional` + `conceptual` becomes a mechanical
   recode of claims that each do one job.

**This is the worked precedent running forwards.** `DDD-measure-16`/`-17` was exactly this
operation done by hand for one node: the arithmetic limb went `formal`/`established`, the modelling
limb went `conceptual`/`projected`. It could be done *because the split came first*. Phase 1a did
not add a kind value; it split a statement, and the kinds then fell out. Eight nodes are waiting for
the same treatment, and adding a value before splitting them inverts the order that worked.

**Alternative, if Emil prefers a filing now:** the counter-argument is that 16 of 29 is a majority
and waiting leaves the appendix (I-3) rendering `conceptual` for definitions for at least another
session. If that weighs more, the minimal version is to file the *finding* as a claim or decision
without touching `kind` — the recode then has a basis to cite. This is drafted, not recommended.

### The interaction I-2 was told to carry: what is a definition's falsifier?

**Answer, and it is already canon's answer.** `spec/claim-format.md` §1 gives `test` for
conceptual/normative kinds and names its three forms — counterexamples, coding reliability,
explanatory utility. Those are exactly the definitional failure modes: *carves the wrong joint*,
*cannot be applied consistently*, *earns nothing*. The schema anticipated this and the corpus
confirms it — all four test-only claims are definitions.

**So a definition's falsifier is its `test`, and the enforcement rule follows: a definition must
carry a `test`; an assertoric claim must carry a `falsifier`; a mixed claim must carry both, which
is a smell rather than a virtue.** Note what this does *not* license: it does not make `test` a
general escape from `falsifier`. Emil's Phase 1a ruling — *"every claim carries one"*, no
near-definitional exception — is what §5's A2 costs out.

---

## 4. I-1(b) — the four retired claims, and what history actually holds

The four, with prior status recovered as far as it is recoverable:

| Claim | kind | `changed` | Prior status | Recoverable from the graph? | Recoverable from git? |
|---|---|---|---|---|---|
| `DDD-measure-06` | formal | v5.10 | **`established`** | **Yes — but only as prose inside `notes:`** | Yes (`f9c1534`, repo genesis) |
| `DDD-frame-15` | conceptual | v5.10 | **`projected`** | **No** | Yes (`dba00c5`, 2026-08-17) |
| `DDD-frame-09` | formal | v4.5 | **Unrecoverable** | No | **No** |
| `DDD-measure-08` | formal | v4.5 | **Unrecoverable** | No | **No** |

### The finding is worse than the item states, and this is the argument

The item says the field no longer distinguishes a once-established claim from a young one. True. But
the fallback the item implicitly relies on — recover it from history — **fails for half the corpus
of retired claims.**

`DDD-frame-09` and `DDD-measure-08` were already `retired` in the repository's first commit
(`f9c1534`, `v5.0.0`, 2026-08-05), carrying `changed: v4.5`. Their status transitions happened
before this repository existed. They are not in git here, not in `meta/seed/claims-seed.yaml`
downstream (which also carries them at `retired`), and not in `CHANGELOG.md`, which records what the
retirement *corrected* and never what the node *was*. Both were searched.

And the one case that does read from the graph reads only by accident of authorship.
`DDD-measure-06`'s prior status survives because the Phase 1a session chose to preserve the whole
pre-retirement field block verbatim in `notes:`, under the heading *"THE FIELDS AS THEY STOOD FROM
v4.5 TO v5.9"*. That was good practice and it is not a mechanism. `DDD-frame-15`, retired in the
same session by the same hand, preserves its **statement** verbatim and **not its status** — so two
claims retired on the same day, three commits apart, differ in whether the loss occurred.

**The test question, answered:** *can a reader see, from the graph alone, that `DDD-measure-06` was
once `established`?* **Today: yes for that one claim, by reading prose; no for the other three; and
no as a property of the format.** One in four, by luck, is the honest summary.

### Options, drafted and tested — not picked

**O1 — keep `retired` as terminal maturity; record the prior value in `notes:`.**
Cost: zero schema change. Verdict against the test: **weak pass, and it is the status quo that
already failed three times out of four.** It is unenforceable by the validator (prose), unqueryable
(no field), and it is precisely what produced the `measure-06`/`frame-15` asymmetry above. Drafted
for completeness; the evidence is against it.

**O2 — add a lifecycle field orthogonal to maturity (`lifecycle: active | retired`).**
`status` then keeps the maturity the claim actually held: `DDD-measure-06` reads
`status: established, lifecycle: retired`. Verdict against the test: **clean pass, and it is the
conceptually correct placement** — the item's own diagnosis is that a lifecycle state is sitting in
a maturity field, and this is the option that removes it from there.
Costs, all real: a format change (format 2, additively — absent `lifecycle` defaults to `active`, so
the other 85 claims need no edit); **`status: retired` stops existing**, which changes what every
consumer of the field reads, including `gen-appendix.py` (I-3) and the I-4 gloss; four claim files
migrate; `DDD-frame-09` and `DDD-measure-08` have no maturity to restore, so they need an honest
`status: unknown` or a stated convention for pre-repository nodes. The last cost is the one to
weigh: O2 *forces* the unrecoverable cases into the open, where O1 and O3 let them stay quiet.

**O3 — add `retired_from:` to the node.**
`DDD-measure-06` gains `retired_from: established`. Verdict against the test: **clean pass.**
Costs: a format change (format 2, additively), but the field is optional and fires only on retired
claims — **zero backfill for the 85 live claims**, four files touched, and `status` keeps its
current meaning so no consumer changes. `DDD-frame-09` and `DDD-measure-08` take
`retired_from: unknown`, with a `notes` line saying the transition predates the repository — which
is a true record rather than a silence.
The objection: it leaves a lifecycle value in the maturity field and adds a second field to
compensate, so it treats the symptom. It is the cheaper option and the less honest one.

**O4 — derive it from version history. Ruled out by evidence, and recorded so it is not
re-proposed.** It fails on `DDD-frame-09` and `DDD-measure-08`, and a mechanism that works for
claims retired after 2026-08-05 and not before is not a mechanism.

**A note the ruling should have in view.** Whichever of O2/O3 is taken, **it is a format-2 change**,
and `spec/claim-format-2-addendum.md` already exists as the precedent for additive fields that leave
all format-1 claims valid. The path is open and has been walked once.

---

## 5. I-2 — both checks run against the corpus, with hit lists

Both were run as reports. Neither is proposed as enforcing in this document.

### Check A — falsifier presence

Retired claims are exempt in every variant: a retired node's statement is its epitaph
(`RETIRED — "…"`), and an epitaph has no falsifier. Four claims are exempt on that ground.

| Variant | Rule | Hits |
|---|---|---|
| **A1 lenient** | `falsifier`, or `test` for conceptual/normative; retired exempt | **0** |
| **A2 strict** | `falsifier` on every live claim, `test` no substitute | **7** |

**A1 fires on nothing.** It is mergeable as an **error** today with no migration at all. It is not
nothing: rule 2 currently requires a falsifier only for `projected`, so A1 newly binds `reported`
and `established` — the exact gap `DDD-measure-06` fell through, sitting at `established` from v4.5
to v5.9 with no stated observation that would fire against it. **A1 closes the case that produced
the item, at zero corpus cost.**

**A2's seven, in full:**

| Claim | kind | status | has `test` |
|---|---|---|---|
| `DDD-measure-09` | conceptual | reported | yes |
| `DDD-measure-12` | conceptual | reported | yes |
| `DDD-cost-05` | conceptual | projected | yes |
| `DDD-frame-01` | conceptual | projected | yes |
| `DDD-frame-02` | conceptual | projected | yes |
| `DDD-frame-03` | conceptual | projected | yes |
| `DDD-frame-08` | normative | projected | yes |

All seven are upstream; all seven carry a `test`. **A2 is a tractable migration — seven falsifiers
to write — but it is canon authoring, not a schema edit**, and each one needs a ruling. It also
collides with §3's answer: `DDD-frame-01`, `-02`, `-03` and `cost-05` are four of the sixteen
definitions, and A2 says a definition must carry a falsifier anyway. Emil's Phase 1a ruling says
exactly that and it is his to reaffirm or narrow with the seven now visible.

**Recommendation, offered because the count licenses it:** A1 as **error** now; A2 as **warning**
now and error once the seven are written. This is the shape that merges something real this session
without booking seven unwritten falsifiers as a debt inside an error-class gate.

### Check B — rule 1, single-limb statements

**There is no mechanical test for "one proposition".** What can be counted is clause-joining
punctuation, and the gap between the two is the finding.

| Variant | Rule | Hits (of 89) |
|---|---|---|
| B0 | semicolon anywhere | 40 |
| **B1** | semicolon outside mathematical notation | **34** |
| B2 | B1, or `, and ` | 53 |

**B1's exposure on ratified claims — six**, and this is the number the item asked for:
`DDD-cost-02`, `DDD-floor-01`, `DDD-measure-03`, `DDD-measure-04`, `DDD-measure-14` (reported) and
`DDD-measure-16` (established).

**All six were read.** The detector is right about four and wrong about two:

- **Genuine multi-limb:** `DDD-cost-02` (a degeneracy result *and* what pricing requires),
  `DDD-floor-01` (bundling, a cleaving requirement, *and* the overflow ∩ open mechanism),
  `DDD-measure-03` (a definition *and* two results), `DDD-measure-14` (iteration *and* invariance).
- **False positives at the semantic level:** `DDD-measure-04`, where the semicolon follows a colon
  and separates two glosses of one proposition; and — the one that matters —
  **`DDD-measure-16`**, whose second clause scopes the first rather than asserting beside it.

**`DDD-measure-16` is the reason B cannot be an error.** It is the claim Phase 1a *built* to cure
`DDD-measure-06`'s compoundness. A rule-1 check that fires on the repair is a check that would have
blocked the fix.

**Recommendation:** **B1 as a warning only, and labelled as what it is** — a drafting prompt that
locates candidates for human adjudication, not an enforcement of rule 1. Rule 1 proper is a semantic
property and its enforcement is an audit with rulings, not a validator pass. If Emil wants rule 1
genuinely enforced, the instrument is a one-off adjudication of B1's 34, and this session can carry
the hit list into it — but **splitting any of them edits statements, which this session's own rule
forbids**, so the adjudication lands in a successor.

**On the twenty-claim threshold the prompt set:** B1 fires on 34 and B2 on 53. Both are past it.
**A1 fires on 0 and A2 on 7. Both are under it.** The four checks separate cleanly into "merge now"
and "needs a plan", and the line falls between A and B rather than inside either.

---

## 6. W1 — recommendation: **do not take it in this session**

The audit's Q4 is Ruled (`ground distribution` → **deployment distribution**), and W1 is genuinely
independent of I-1 to I-4. The recommendation is against taking it here anyway, on three grounds,
the first of which is decisive on its own.

**One — W1 edits claim statements, and this session's rule forbids that.** The literal phrase
`ground distribution` appears in the `statement:` field of four upstream claims:

| Claim | kind / status | where |
|---|---|---|
| `DDD-measure-01` | empirical / projected | statement — *"H(V) over the ground distribution"* |
| `DDD-measure-11` | conceptual / reported | statement |
| `DDD-measure-12` | conceptual / reported | statement |
| `DDD-measure-16` | formal / **established** | statement |

A W1 that skipped them would rename the concept everywhere except in the four claims that define it
— a partial rename, which is worse than none. A W1 that included them breaks *"nothing in this
session edits a claim statement"* on an `established` claim.

**Two — the ordering rationale this session was given points the same way.** This session goes
before the migration because it touches claim *headers* and the migration touches statements, so
schema-final-first means the migration never re-touches what it just edited. Taking a
statement-touching wave here defeats the reason for the ordering.

**Three — the audit's own placement.** W1 *"rides with a paper revision rather than replacing
one"*: 29 of its 74 rule-assigned occurrences sit in the merged papers, and Paper A's revision is
explicitly out of scope here. Counted at head, the literal phrase appears 4 times in `paper-a.md`
and 12 times in `measure-note.md`.

**A count correction, reported not smoothed.** The prompt gives W1 as 105 occurrences. The literal
string `ground distribution` occurs **24 times upstream and 39 times downstream** — 63 across the
two attached repositories. The audit's 105 counts occurrences *assigned to sense 5*, which includes
bare `ground` used in the population sense, so the two numbers measure different things and neither
is wrong. `product-cli` is not attached to this session and its single occurrence was not verified
here.

**If Emil takes W1 anyway**, the only coherent version is the full one including the four
statements, as its own commit and its own gate, with the "no statement edits" rule explicitly
suspended for it at the ruling. Half a rename is the one option to refuse.

---

## 7. What is held at GATE 1

| # | Held for ruling |
|---|---|
| **R1** | I-1(a): file nothing in `kind` now; record the finding; the split follows rule 1's pass. Or file the finding as a node now. |
| **R2** | I-1(a) interaction: a definition's falsifier is its `test`; definitions require `test`, assertoric claims require `falsifier`. |
| **R3** | I-1(b): O1, O2, or O3 — and, if O2 or O3, what `DDD-frame-09` and `DDD-measure-08` carry where the prior status is unrecoverable. |
| **R4** | I-2 Check A: A1 as error now; A2 as warning now and error when the seven are written. |
| **R5** | I-2 Check B: B1 as warning only, labelled a drafting prompt; rule 1's real enforcement deferred to an adjudication session. |
| **R6** | W1: not taken here. If taken, taken whole, with the statement rule suspended by ruling. |
| **R7** | The tag/head divergence upstream — recorded, and whether the release descriptor at close should say anything about it. |
