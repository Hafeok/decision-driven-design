# Response to the external review of *Actor-Indexed Determination*

**The review:** `meta/sessions/2026-08-23-phase1a/paper-a-objective-review.md`, against the
manuscript at `40d277f` and the graph at `v5.8.0`. Recommendation: **major revision / reject and
invite resubmission.**

**This response:** the revision of 2026-08-30, session record at
`meta/sessions/2026-08-30-paper-a-revision/`. Every objection the review raises is mapped below to
**conceded**, **repaired**, or **defended — and why**. Nothing is left unanswered, including the
objections the paper lost.

**The headline, stated first because it is the honest summary.** We count **twenty-two distinct
objections** in the review. **Twenty-one are conceded, repaired, or accepted and booked as work not
yet done. One is defended** — a wording choice, and even there the finding underneath it is
conceded. §5 below lists three things we decline to give up, but those are propositions the review
*praised*, not objections it raised, and counting them as defences would flatter us.

Two of the three load-bearing findings had already forced **canon** changes before this revision
ran, so much of what the paper does here is catch up with corrections your review caused. **The
paper is longer than the one you reviewed, not shorter** — 11,708 words to 17,334, a 48% increase —
and §9 explains why we think that is the honest outcome rather than a failure to comply.

---

## 1. Two corrections to the review itself

Offered because they are useful to you, not to score points.

**1.1 The Hollnagel and Woods citation points at the wrong volume.** §8 cites
`10.1201/9781420005684` as *"Woods and Hollnagel, Joint Cognitive Systems"*. That DOI resolves to
**Woods & Hollnagel (2006), *Joint Cognitive Systems: Patterns in Cognitive Systems Engineering***.
The volume your prose is about — the joint cognitive system stated as a unit of analysis — is
**Hollnagel & Woods (2005), *Foundations of Cognitive Systems Engineering***,
`10.1201/9781420038194`. Two books, one year apart, sharing a main title, with the author order
reversed. **Both are now cited**, since both are on point, and the correction is reported rather
than made silently because a database would have propagated the error.

**1.2 A near-miss on our side, recorded for symmetry.** While drafting the survey we nearly
attributed a *"Law of Conservation of Complexity"* to *Patterns* — a claim that, if true, would
have **strengthened** our position by giving our conservation principle a named precedent in the
literature you say we ignore. It could not be corroborated in any primary source. **It is used
nowhere**, and it is recorded in our successor list so a later session does not rediscover and
believe it. We mention it because a verification rule that only ever removes inconvenient claims is
not a verification rule.

---

## 2. The three critical findings

### 2.1 The closure–measure biconditional is false (review §2) — **CONCEDED, and repaired in canon**

You are right, and the worse fact is that the contradiction was ours before it was yours. Our own
companion measure note had already rewritten its §7 into a scope condition with three separated
requirements — existence, availability, estimability — and **canon was never updated to match**. So
`DDD-measure-06` still carried the biconditional at `established`, and the paper projected it
faithfully. **The projection was stronger than the note sharing its graph.**

- `DDD-measure-06` is **retired** (`retired_from: established`), superseded by `DDD-measure-16`
  (availability to an arrangement, at `established`) and `DDD-measure-17` (the coincidence, at
  `projected` — see 2.1b).
- The paper now separates the three conditions in a table at §4.4 and carries the separation at
  five further sites. **Closure governs availability and neither of the other two.**
- Your four-condition repair (§2.5) is adopted in substance. We fold semantic determinacy and
  constructive closure differently — the first into existence, the second onto our closure ladder —
  and say so.

**2.1b One thing your finding produced that you did not ask for.** The old node bundled two
propositions under one status: *where the measure applies*, and *what the agreement between that
boundary and the floor's location is worth*. The second is an interpretive claim about two
arguments, not arithmetic, and it is now `projected` rather than `established` — with a falsifier.
Splitting them was your finding's consequence and it is a better claim than either half was.

**2.1c And a finding about our instruments, not our claims.** `DDD-measure-06` retired and **fired
no warning**: our cross-repository pin instrument only watches nodes that are pinned, and this one
was not. Both existing checkers passed all three lines where the paper called it `established`,
because none is a block quotation and none is an appendix row. We found it with a sweep written for
this revision, now shipped as a **third checker** (§7 below). The node and its successors are now
pinned.

### 2.2 Raw ground collapses the allocation measure (review §3) — **CONCEDED; interim posture adopted**

Take `X = G` for a deterministic task and mutual information reports the ground as carrying the
entire verdict, while the arrangement may hold no rule for turning that ground into an answer.
`DDD-measure-15`'s admissibility condition does not exclude it. **You are right, and the previous
round's answer — a caveat that a real actor may fail to use information that is present — does not
repair a condition that fails to exclude the case.**

**What we have not done:** repaired it. The framework-native fix is that admissible `X` should be
*a representation the arrangement can decode*, which would make the residual arrangement-relative
and bring the measure into line with the paper it appears in. That is research, not filing, and it
is not in this revision.

**What we have done:** adopted your own recommended interim posture. The paper does not present
verdict entropy as an established measured region. §4.4 states the identification as a modelling
claim, `projected`, with its falsifier a correspondence that has not been run; §10.2 states the
admissibility condition's limit; and the abstract says the identification is unproven in the same
sentence that says the chain rule is certain.

### 2.3 The four discharge modes do not partition (review §4) — **CONCEDED; the claim is retired**

All three of your overlaps land. `DDD-frame-15` is **retired**, superseded by `DDD-frame-17`.

You asked for either an explicit priority rule that assigns each case exactly once, or a recast onto
orthogonal axes. **A priority rule was drafted and tested against your six cases. It ties on
declared defaults and on a timeout's when-to-stop alternative, and every ordering that breaks those
ties crosses the guard separating governance-supply from discharge.** So the disposition is the
recast, not the rule — and your framing of the choice is what produced that answer.

The successor partitions by two dichotomies and nothing else: does the standing configuration
together with the ground at the act fix the resolution (**predetermined**), and if not, is what
fixes it inside the arrangement's control (**exercised**) or outside it (**drawn**). Three
consequences, each closing one of your overlaps:

- **the unit is the outcome-relevant alternative, not the act.** Your timeout case dissolves here:
  a timeout carries a when-to-stop alternative and a what-to-return alternative and they discharge
  differently. The retired claim quantified over acts in its statement and over alternatives in its
  own test field — a second defect you did not report and we found while drafting the successor;
- **governance status is not an axis.** Your declared-default overlap was a declaredness test
  smuggled into a locus partition. Declaredness is a different partition's question;
- **no value turns on actorhood.** The retired *judgment* mode did, and thereby inherited the
  admission test's circularity you name in §6. This one does not inherit it.

Your trained-inference case is worked explicitly at §3.3: policy-committed on one axis,
predetermined on another, standing on a third, **all three true at once and none competing**. The
old list read as competition because it drew values from three axes simultaneously.

**One thing we defend.** You suggest *"ungoverned resolution"* would be clearer than *"determined
never"*. We keep the canonical phrase, because it names a state and *"ungoverned"* names an
assessment — and we accept your underlying finding: an external reader met our guard and still
reported the phrasing as conflicting, which is a finding about our exposition. §4.1 now states the
guard before the reader can trip on it rather than after.

---

## 3. The major findings

### 3.1 Residual discretion conflates different phenomena (review §5) — **CONCEDED; the term is amended**

Your cryptographic-hash example is decisive and canon now carries it. `term:residual-discretion` is
amended to quantify **at fixed ground**: the alternatives still admissible once the standing
configuration *and this act's ground* are both given. A hash varies enormously across inputs and
exercises no discretion, because at each input the commitments fix the output exactly. Under the old
wording it came out carrying enormous discretion, which was plainly wrong.

Your four phenomena are separated: variation across ground, epistemic uncertainty about a fixed
policy, stochasticity, and genuine unresolved selection. Three of the four are now excluded in the
term's own text. `DDD-frame-02`'s clause is amended in step.

**A consequence worth naming:** this repair and 2.3's turn out to be one repair made in two nodes.
An alternative with no residual discretion at fixed ground is exactly what *predetermined* means.

### 3.2 The actor admission test remains partly circular (review §6) — **CONCEDED, and left open**

You are right that "selection" is not independently defined, and that the rock's failure is produced
by the intended meaning of the word rather than by a test. **We have not repaired it and we do not
claim to have.** It is flagged as open rather than patched, because a patch that redefined selection
without an independent criterion would move the circularity rather than remove it.

What we can report is that the discharge partition **no longer depends on it** — its three values
turn on determination and control, and are answerable without deciding whether a producer is an
actor (2.3). The circularity is contained rather than cured.

### 3.3 Split relevant ground from accessible ground (review §6) — **ACCEPTED, not yet executed**

`G*` (relevant world facts) versus `G_A` (ground accessible and delivered to arrangement `A`) is
correct and strengthening, and it is the delivery distinction applied to ground. It is **canon work
we have not done**: the tuple's `ground` coordinate is a settled term, and a projection may not
redefine one. The paper carries the distinction informally where it bears — §8.1 now says that
ground missing to one arrangement is available to another that can run the search, and that the
floor moves with it — and the split is booked.

### 3.4 Graph status is being used as epistemic status (review §7) — **CONCEDED; partly repaired**

This is the objection with the widest consequence and we treat it as such.

**Repaired in the paper.** The note on claim status now says explicitly that `settled` and
`established` mean argued and unchallenged *inside this framework* and **not externally validated**;
that `reported` means a computation reproduces, not that the world was consulted. The conclusion
states that **every `established` claim in this graph is `formal`** — so what is settled here is
arithmetic — and that **nothing in either list has been checked against the world**. Your phrase for
the analysis sections, *authorial synthesis not represented in the graph*, is adopted in substance:
`(analysis)` now says it carries no status *"which does not make it uncontestable, only unattributed
to the graph."*

**Repaired in the instruments.** A third checker verifies that every inline status assertion asserts
the status the graph carries (§7 below).

**Not repaired: the kind/maturity split.** You are right that `projected` bundles definitions,
formal claims, empirical hypotheses and normative prescriptions under one maturity label. The graph
carries a `kind` field, which the paper's tables now render — but the split you actually ask for
runs *through* several claims rather than between them, and a session that examined it ruled that
assigning a finer value before those claims are split would miscode whichever job it did not name.
**It is sequenced, not dismissed**, and it is the change we most want to land before these
repositories become public.

**Your point about the primary claim's falsifier is conceded** and §9.5 now says it: failure of the
umbrella prediction would not falsify the ontology, because the framework's descriptive and
predictive claims are separately falsifiable.

### 3.5 Novelty is not established (review §8) — **CONCEDED; the claim and the title are withdrawn**

The largest single piece of work in this revision.

- **The title is withdrawn.** *The Missing Parameter* asserted an absence we had not surveyed. The
  paper is now *Actor-Indexed Determination*, and §1.2 says why the old title went.
- **The narrowed claim is adopted in your words**: a specific, auditable synthesis of resolution,
  assurance, delivery and accountability — not the discovery that sociotechnical arrangements
  matter.
- **All seven works are engaged**, each with what the framework takes and where it differs, with a
  comparison table. Every locator is verified against Crossref, Open Library or NCBI.

**Three entries record where a neighbour is stronger than the framework**, because a survey that
only found advantages would not have been a survey:

- **Horvitz supplies a decision-theoretic criterion for allocation and we supply none** off the
  closing region;
- **Leveson's control structure carries authority structurally** and we do not improve on it;
- **four of `DDD-frame-08`'s five accountability elements are already Bovens's.** What remains is
  authority linkage and a change of tense from retrospective assessment to design-time constitution.
  One element and a tense, not a new theory.

**One difference claim was withdrawn by the reading itself.** Our survey plan had said Matthias's
responsibility gap reads as an arrangement naming an executor and no principal — *"fixable rather
than novel"*. The primary text does not support *fixable*: the gap rests on a **control condition on
just ascription**, not on a missing name. The paper now says structural completeness does not close
it, and that whether it is morally sufficient is a normative question our claim is `projected` about.

**What survived the survey**, and it is what we now claim: no work surveyed carries
filing-versus-delivery as a standing category, and none separates a resolution's source from its
assurance mechanism as orthogonal dimensions. The paper adds, in its own words, that **a distinction
being unoccupied is not a distinction being correct.**

### 3.6 Hypotheses are not study-ready (review §9) — **CONCEDED; coding reliability comes first**

§9.5 now names **Study 0**: inter-rater reliability and predictive validity of the framework's
coding scheme, **before any comparative work**, with agreement reported *per dimension rather than
pooled* — since a scheme can be reliable on closure and unreliable on discharge, and a pooled figure
would hide exactly that.

Two admissions follow, both yours:

- **the escaped-decision count is circular** until the instrument holds. A count produced by the
  framework's own criterion cannot also be evidence for it, and it is usable only as an inter-rater
  quantity until an independent criterion exists — which we do not have;
- **H1 and H2 bundle variables**, difficulty and resources are invoked as controls without
  operational definitions, and each hypothesis is a research programme rather than a study. The
  paper says so.

---

## 4. The smaller findings

| Review | Disposition |
|---|---|
| **§10.1** the closure ladder mixes axes; decidability is logical, not a stronger operational rung | **Conceded and repaired.** The ladder is now **three rungs, all operational**, ending at constructively closed. Decidability is stated as the logical axis's answer, with both directions of non-implication given: a decidable predicate need not be operationally closed, and an operationally closed one need not be decidable. The defect was in our framing, not in canon, which always reserved *decidable* for the formal special case |
| **§10.2** accountability's competing element counts | **Conceded and mapped.** §7 supplies the table: the five-element version *refines* the third element into stake and sanction path and **adds** authority linkage. It refines-and-adds; it does not replace. **And a `projected` claim that adds an element to a `settled` term is a supersession question**, which the paper reports and does not rule — a projection may not rule on canon. It is filed as a successor item so the flag reaches canon rather than sitting where nothing points back at it |
| **§10.3** the worked example's provenance classifications | **Conceded and restated.** Every assignment in §8.1 is now a hypothesis with *what would overturn it*. Your schema challenge is the instructive one: an arrangement that both maintains a schema and reads it from a store holds it under **two provenances at once**, and our five-way partition does not adjudicate. That is stated as a limit |
| **§10.3** the two claimed escapes may be discoverable | **Conceded.** They are now **candidate** escapes, and our own vocabulary supplies the objection: an escape is a property of an arrangement, so a walk that did not look everywhere has not established one. Code search, contract tests, telemetry and asking the consuming teams all reach the question the walk assumed missing |
| **§11** length, repository-nativeness, graph machinery in the argumentative path | **Conceded and executed.** The generated tables, the pin mechanics, the filing history and the reproduction instructions are in a separate supplement. The boundary rule: *a passage moves when it is about the graph; it stays when it is about the world, or about how much warrant the paper has* |
| **§11** the rhetoric overruns the status labels | **Conceded and repaired.** "Two results give the framework its shape" is now "two proposals with declared falsifiers rather than findings"; "its strongest result" is "its most load-bearing proposal — and a proposal"; the conclusion no longer asserts the framework's value but states its aim, and names the open question |

---

## 5. What we decline to give up

**These are not defences against objections.** All three are propositions the review identifies as
worth keeping, and we list them because a revision that conceded this much needs to say what it did
*not* trade away under pressure.

**5.0 The one actual defence** is smaller than any of them, and it is in 2.3: we keep the canonical
phrase *"determined never, by nobody"* rather than replacing it with *"ungoverned resolution"*,
because the first names a state and the second names an assessment. Your finding underneath the
suggestion — that a reader met our guard and was still confused — is conceded, and §4.1 is
restructured because of it.

**5.1 The arrangement as the unit of analysis.** You call it the durable core and we agree — but we
defend *keeping* it while conceding the priority. The novelty narrows to the synthesis; the object
stays.

**5.2 Filing versus delivery.** You called it a strong engineering contribution unprompted, and the
survey supports it: **no work we read carries it as a standing category.** Leveson's causal-scenario
step can reach the case, and meaningful human control's tracing condition is adjacent to it — an
arrangement can satisfy tracing completely, with a named and answerable designer, and still fail at
the act because the decision that designer authored was never retrieved. **A tracing audit passes
that.** The category is the contribution and we keep it.

**5.3 The disclosure discipline.** You note twice that the absence of evidence is correctly
disclosed. We have not traded it for brevity: **every projected-and-empty sentence stayed in the
main paper** when the apparatus moved to the supplement, on the explicit ground that those sentences
are about warrant rather than about the graph.

---

## 6. Where the revision leaves the paper by your own scorecard

| Dimension | Your assessment | What changed |
|---|---|---|
| Formal correctness | *critical boundary error* | the node is retired; three conditions separated; the successor's coincidence claim demoted to `projected` |
| Conceptual consistency | *several load-bearing conflicts* | the discharge partition recast; residual discretion amended; the closure ladder repaired; the accountability counts mapped |
| Related work | *far below publication standard* | seven works engaged, locators verified, three of them recording where the neighbour is stronger |
| Originality | *novelty not yet demonstrated* | the claim is narrowed to your formulation and the title withdrawn |
| Empirical support | *none, correctly disclosed* | unchanged, and Study 0 now precedes the comparative design |
| Writing | *overlong and over-defensive* | **the paper is longer.** See §12 |
| Internal traceability | *excellent* | a third checker added, covering the surface the other two structurally cannot reach |

---

## 7. One thing the review caused that is not in the paper

Your §7 is about status being read as warrant. Acting on it exposed a gap in our instruments rather
than in our prose.

We had two checkers: one verifying block quotations against the graph, one re-reading the generated
tables. Neither reads the manuscript's **most common** citation form — the inline citation asserting
a status in running prose. When `DDD-measure-06` retired, the paper called it `established` in three
places and **both checkers passed all three lines.**

`check-status.py` now verifies that surface, and it ships with its origin recorded as its warrant:
it was not designed against a specification, it was generalised from a sweep that found something,
**so its coverage is that sweep's and no wider.** That the one unchecked surface was exactly the one
converting a citation into warrant is not a coincidence we wanted to leave unfixed.

---

## 8. What is still owed

Stated because a response listing only what it fixed is not a response.

1. **The measure's decoder repair.** `I(V;X)` is not usable-information and we have not made it one.
   The interim posture is adopted; the repair is research.
2. **`G*` versus `G_A`.** Accepted, canon work, booked.
3. **The kind/maturity split.** Sequenced behind a claim-splitting question it depends on.
4. **The actor admission test's circularity.** Open, and flagged as open.
5. **The accountability arity.** Reported by the paper, filed as a successor item, unruled.
6. **Inter-rater reliability itself.** Study 0 is designed and unrun. Every hypothesis's evidence
   field is still empty, and the paper still says so on every page it needs to.

---

## 9. Recommendation, in your own terms

Your §13 judged the manuscript strong as a canonical repository statement, promising for a workshop
after major revision, and reject-and-resubmit as an archival conceptual paper. We think the revision
moves the third of those and do not claim it clears it — **the measure's construct-validity problem
is not repaired, and you were right that it is load-bearing.** What the paper now does is state that
limit where a reader meets the measure, rather than in a footnote.

**The one thing we would ask you to weigh again** is the relationship between length and
compliance. You asked for narrower claims, better sourcing, and less machinery in the argumentative
path. We did all three, and the argumentative body grew from **11,708 words to 17,334 — 48%**
(counted by the same method that reproduces your own figures of ~11,600 and ~14,900 to within 1%:
regex word tokens over the Markdown source).

The machinery did leave: 5,232 words of it are now in a supplement. **What replaced it is
qualification.** A narrower claim needs the hedging a broad one does not. A survey of seven works is
longer than an assertion about them. Three of its entries record a neighbour being stronger than we
are, and each of those costs a paragraph. The status discussion now says what `established` does not
mean, which is longer than saying what it does.

**We would rather defend the length than the certainty that buying brevity would have cost.** The
failure mode we were most worried about entering this revision was a shorter paper that sounds more
confident because it has less to qualify. If the length is now the objection, that is a better
objection to have.
