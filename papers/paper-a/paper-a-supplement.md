# Supplement — *Actor-Indexed Determination*

*Companion to `paper-a.md`. Not required to follow the argument.*

---

## S1. What this supplement is, and why it is separate

An external review found the paper carrying its own filing history, pending-node discussion and
generated graph tables inside the argumentative path, and judged that an archival paper should not.
The finding was accepted. **The apparatus is not reduced; it is moved.** Everything here still runs,
still verifies, and still fails loudly.

The boundary applied is one rule:

> **A passage moves here when it is about the graph. It stays in the paper when it is about the
> world, or about how much warrant the paper has.**

So the status *vocabulary* is here and the sentence *"this claim is `projected`, its evidence field
is empty, and the study is unrun"* is not — that one is about warrant and stays where a reader meets
the claim. Filing history, minting rulings, pin mechanics and reproduced node tables are about the
graph.

---

## S2. The projection's pin, and what it is pinned to

The paper is a projection of `actor-indexed-determination` at the annotated tag **`v5.12.0`**. Every
bracketed claim, decision and term identifier in the paper resolves against that one ref. No
identifier resolves against the downstream repository, so no downstream ref is pinned.

**The pin was held deliberately, and then advanced.** The paper was merged as a projection of
`v5.9.0`, and the pin was kept there by ruling while canon moved — through `v5.10.0`, `v5.11.0` and
`v5.12.0` — so that upstream repair would not drag the projection behind it. This revision advances
it in one step. Two of the four quotations that broke at the advance are quotations of claims the
review asked the paper to stop overstating, so the repair paid a debt the paper already owed.

The companion measure note — `papers/measure-note/measure-note.md` in `decision-driven-design` — is
cited by path at commit `2b26f25`, which carries its discharge section and the vocabulary rename
described in S5. **That commit is this session's own** — Paper A pinned the note at `aa7e135`, and
W1 edited the note, so the pin had to advance to a commit this revision created. The alternative was
to keep citing a commit whose prose says `ground distribution` while this paper's says
`deployment distribution`, which would have been a citation that reads as current and is not. The note is absent from `v0.4.0` and from every earlier downstream tag, so it
resolves at a commit rather than at a tag.

---

## S3. Filing status of what the paper carries

Three passages in the paper state a distinction the graph does not carry. Each is marked
register-native at the point of use; this is where their filing status is recorded.

| Passage | Status in canon | Why |
|---|---|---|
| §2.4's five-way ground provenance (controlled, observed, inferred, institutional, missing) | **ruled ineligible for minting**, not merely deferred [DDD-dec-26] | a mint would fix a partition that an open trust question may restructure, and the institutional slot's mechanism is gated on it. §8.1 exhibits a case the partition does not adjudicate, which is the reason arriving in a worked form |
| §5.2's **constructively closed** rung | **not filed**; no claim node names it, and the word *constructive* occurs nowhere in the principle repository's core documents | `term:closure` is stated in evaluative terms alone. A dedicated node is pending on the framework's open-questions wave; until it lands the rung's basis is closure, the separation of closure from generation cost, and the measure's silence on search |
| §3's two commitment terms | **`draft`** — filed, not ratified [DDD-dec-26] | both were minted only when a downstream projection needed them as citable nodes, and a downstream document is never the proximate cause of an upstream mint: the canonical text was drawn from canon's own existing exposition |

**The paper files nothing.** A projection that mints is a projection that has stopped being one.

---

## S4. A finding this revision leaves open in canon

The paper's §7 reports that the graph carries **two counts** of accountability's elements —
`DDD-frame-08`'s five and `term:accountability`'s three — with a mapping showing that the five
refines the third element into stake and sanction path and **adds** authority linkage.

A `projected` claim that adds an element to a `settled` term is a supersession question, not an
elaboration. **The paper flags it and does not take the ruling**, which is not a projection's to
take. The finding is filed as a successor item against both nodes, naming this session as its
finder, so that the flag is delivered to canon rather than sitting in a projection nothing points
back at — a flag nothing points back at being, by this framework's own vocabulary, filed and
undelivered.

---

## S5. Vocabulary: `ground` in its population sense

This revision carries the first wave of a vocabulary migration. The word `ground` had been carrying
five senses across the corpus, and the **population sense** — the distribution of cases a task
faces — is renamed **`deployment distribution`** throughout this paper and the measure note, where
those two artefacts own the prose.

Three kinds of occurrence were deliberately **not** renamed, and each for a reason that is the same
reason: **the words are canon's, not the paper's.** A reproduced node table carries the graph's own
statements; a passage quoting a live claim verbatim must keep quoting it; and canon still reads
`ground distribution` at `v5.12.0`. Renaming any of them would forge agreement the pin does not
have, which is the same principle the pin itself exists to enforce. Those occurrences move when
canon moves.

Three further occurrences were ruled **ambiguous** between the population sense and the sense
naming the conditions in the case, and deferred whole rather than ruled in a paper session. Where a
rename is contestable, it is not this wave's.

---

## Reproduction

**This paper mints no figures and no assets.** Every number it states was produced by an existing
script in the principle repository and is cited to the projection that works it: the
date-validation totals of §4.4 and §8.6 come from `core/assets/measure-toy.py`, worked in the
companion measure note's §4 and in `core/09` §3. That script was re-run fresh while this paper was
drafted and reproduces the stated values.

**Three checkers, and each covers a surface the others cannot reach.** All three live beside the
manuscript and take the ref as an argument, so every check is reproducible against any ref rather
than against the one that happened to be current.

| Script | What it verifies | Surface |
|---|---|---|
| `check-quotations.py` | every block quotation attributed to a node is verbatim at the ref, or discloses itself partial in its own citation | block quotations |
| `check-appendix.py` | every rendered row matches the graph; nothing the paper cites is missing; nothing is invented; the hypothesis rows really do carry empty evidence | the generated tables |
| `check-status.py` | every inline citation asserting a status asserts the status the graph carries | running prose |

The third is new at this revision, and its origin is a defect rather than a design. The pin advance
retired `DDD-measure-06`, the paper called it **established** in three places, and the two existing
checkers passed all three lines — because none was a block quotation and none was an appendix row.
The unchecked surface was precisely the one that converts a citation into warrant.

**Appendix A is generated wholesale and never hand-edited** (`gen-appendix.py`), then re-read
against the graph by an independent script that shares no code with the generator
(`check-appendix.py`). Since the split, the generator reads the manuscript's citations and renders
into this file, so the two cannot drift: the supplement's tables are a function of what the paper
cites. Idempotence is checked by running the generator three times and comparing bytes.

Reproducing the whole apparatus, from the directory holding the manuscript:

```
python3 check-quotations.py paper-a.md <upstream-repo> v5.12.0
python3 check-status.py     paper-a.md <upstream-repo> v5.12.0
python3 gen-appendix.py     paper-a.md <upstream-repo> v5.12.0 paper-a-supplement.md
python3 check-appendix.py   paper-a.md <upstream-repo> v5.12.0 paper-a-supplement.md
```

**What the checkers do not do.** They verify correspondence between this paper and the graph. They
do not establish that anything in the graph is true, and a fully green run is consistent with every
claim in the paper being wrong.

---

## Appendix A. Cited claims, decisions and terms

The paper cites nodes in the framework's claim graph. Statements below are reproduced
word-for-word from the graph at the ref pinned in the front matter, so the paper can be checked
without it. **Kind** and **status** are the graph's own fields, and they answer different questions.
*Kind* is what sort of claim it is: *formal* is arithmetic or a derivation, *empirical* rests on
observation, *conceptual* fixes or uses the framework's vocabulary, *normative* says what ought to
be done. *Status* is how far it has been argued: *settled* and *established* are argued and
unchallenged **within this framework**, *reported* is exercised by a reproducing computation,
*projected* is proposed with a declared falsifier and not yet met, *draft* is filed and not yet
ratified, *retired* is superseded and kept with the correction that killed it.

**Neither field claims external validation, and the two must be read together.** *Established*
means internally argued and unchallenged, not empirically confirmed; *reported* means a computation
runs and reproduces, not that the world was consulted. The pairing is what carries the information:
every *established* claim in this graph is *formal*, so what is settled here is arithmetic, and the
modelling claims that give the arithmetic its meaning are *projected*. The canonical statement of
what each value means, and what it does not, is `spec/claim-format.md` §5 at the pinned ref; this
paragraph projects it and does not replace it.

**This appendix is generated from the graph and never hand-edited** (`gen-appendix.py`), then
re-read against the graph by an independent script (`check-appendix.py`).

### Claims

| ID | Kind | Status | Statement |
|---|---|---|---|
| `DDD-agent-01` | empirical | projected | Long-running agent drift is escaped decisions caused by basis loss: context decay, compaction, and distractors remove claim nodes from the agent's ground, so later actions are decisions with no basedOn edge to the declared claims and revert to model priors. Grounding the agent in a persistent external claim graph — basis as query, not context residue, with per-decision claim citation — reduces drift relative to context-carried instruction. |
| `DDD-cost-08` | conceptual | projected | Actor selection for an act is two-gated: capacity gates always — the actor must carry the act's residual at the declared tolerance or the excess escapes — and assurance gates exactly where the acceptance predicate does not close, where assurance must attach to the actor because no check can carry it. |
| `DDD-cost-09` | conceptual | projected | Assurance-by-actor binds assurance to a scarce carrier, supplied occasioned — at the act, at the carrier's class price. Assurance-by-check moves it into a mechanism, supplied standing — independent of the act. Closing a predicate converts a property's assurance supply from occasioned to standing. |
| `DDD-cost-11` | conceptual | projected | On an open predicate, assurance and actor class are positively coupled; closing the predicate flips the sign — the assurance gate lifts and the capacity gate softens — so the actor class the act requires falls, leaving the actor carrying generation only. |
| `DDD-cost-12` | conceptual | projected | Required actor class for an act is the maximum, over the act's capabilities, of the class needed where assurance is not mechanically discharged — per capability, not per act. |
| `DDD-cost-13` | conceptual | projected | Where assurance attaches to the actor per capability, an answer-keyed qualification instrument — an examination, an eval — evidences demonstrated class on predicates that close. Its verdict cannot evidence open-predicate carriage: the instrument's own predicate closes while the target predicate does not, so delegation to the open predicate substitutes the actor's identity for exactly the check the instrument cannot be. |
| `DDD-cost-20` | conceptual | projected | Encoding around a carrier and encoding within it differ in locus: around-encoding — context, retrieval, scaffolds — is standing supply outside the carrier, delivered through the channel at each act; within-encoding — training — converts judgment allocation to encoded allocation inside the carrier. Training buys allocation, not capacity: it does not enlarge the judgment store. |
| `DDD-cost-25` | conceptual | projected | Assurance mechanisms occupy temporal positions relative to the act — pre-act (selection, training, encoding, static checks), at-act (monitoring), post-act (review, audit, consequence) — each with a latency; a mechanism whose latency exceeds its position's budget — the episode for at-act mechanisms, the consequence horizon for post-act ones — cannot hold its position, so rising tempo, which compresses both budgets, forces assurance pre-act, into standing supply or the carrier. |
| `DDD-delivery-01` | conceptual | projected | Filing is not encoding: a decision sits in I(V;X) only to the extent the arrangement delivers it at the act, so store allocation cannot be read off artefacts, and the paid-once-inherited-by-every-run property belongs to act-triggered delivery specifically, not to standing supply generally. |
| `DDD-delivery-02` | conceptual | projected | Governance filed but not delivered is escape: no source supplied the governing decision at the act, so it was determined by nobody (term:escape, supply-general), and delivery failure is thereby a generator of escape — sufficient, never necessary — whose distinguishing feature is that the ledger shows coverage: escape that presents as governance. |
| `DDD-delivery-03` | conceptual | projected | An unretrieved decision and an unretrieved check over the same act are correlated failures — same actor, same budget, same position — so judgement-mediated delivery on both the source and assurance sides silently removes the independence a gate depends on: the failures compound rather than stack. |
| `DDD-floor-01` | formal | reported | H(V\|X) bundles judged and escaped demand; cleaving them requires an actor-capacity model, and residual demand an actor has taken up escapes where it exceeds effective capacity min(C_hold, C_resolve) AND the shed decisions carry no verifier — overflow ∩ open is the mechanism of capacity-generated escape, sufficient for escape and not necessary for it, with overflow alone producing retries, not escape. |
| `DDD-floor-02` | conceptual | projected | The judgment floor is relational: irreducibility is a property of the indexed relation ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩, not of the task alone — the portion of determination an arrangement cannot discharge through its prior commitments or adequate direct verification at the declared assurance level moves when any coordinate of the relation moves. |
| `DDD-frame-01` | conceptual | projected | Unresolved determination is indexed by the tuple ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩, not by the task alone. |
| `DDD-frame-02` | conceptual | projected | Behavioural commitments attach at three levels — outcome, policy, principal — which compose and are not actor species; residual discretion is the outcome-relevant variation those commitments leave open at the act, held at fixed ground. |
| `DDD-frame-03` | conceptual | projected | The source of a resolution and the mechanism assuring it are separate dimensions; the four-store model held the arrangement largely fixed while the allocation was analysed, and did not draw the distinction. |
| `DDD-frame-04` | empirical | projected | Escaped decisions — consequential resolutions with no adequate source-and-assurance combination — predict ungoverned failure modes and design-review findings. |
| `DDD-frame-05` | formal | projected | Under a sound terminating operational checker with complete declared ground, producer identity is not epistemically necessary for the checked property — and nothing more: not cheap generation, not normative completeness, not accountability. |
| `DDD-frame-06` | formal | established | Closure is distinct from generation cost: verification being cheap implies nothing about the density or accessibility of the acceptance region. |
| `DDD-frame-07` | empirical | projected | Operational evaluability, feedback density, and ground accessibility predict the comparative advantage of computationally assisted arrangements over unaided situated judgment, after controlling for difficulty and resources (H1–H5, filed as DDD-hyp-01 through DDD-hyp-05). |
| `DDD-frame-08` | normative | projected | Accountability is a relation (attribution, persistent principal, authority linkage, stake, sanction path), not an intrinsic capacity; an arrangement naming an executor but no principal is incomplete. |
| `DDD-frame-09` | formal | retired | RETIRED — "closed predicates make intelligence unnecessary." Does not follow from producer-independence under verification; generation may still require whatever capability the search demands. |
| `DDD-frame-10` | formal | projected | Determination demand is conserved as a scalar across arbitrary re-arrangements, actor-generally and including open predicates. |
| `DDD-frame-11` | conceptual | projected | The governance question — is every decision governing the act in a declared store, none escaped? — is well-formed on the total domain, including open predicates where the measure does not exist; the cost question — how much is in each store? — exists only where the predicate closes. The framework's governed domain is strictly wider than its measured domain. |
| `DDD-frame-13` | conceptual | projected | Determination's object is the determinable — an outcome-relevant dimension of variation at the declared tolerance — and its product is a determinate, one specific way of occupying that dimension; determination demand is thereby a measure over unresolved determinables, the verdict variable's support being the determinate-space at the declared grain where the predicate closes. |
| `DDD-frame-14` | conceptual | projected | Discharge always produces a determinate, which lands in two registers: as an outcome — the determinate as it lands in the world, produced at every completed act — and as a verdict — the determinate as assessed by a declared predicate, produced only where governance has declared one; governance is thereby the conversion of outcomes into verdicts, and every diachronic instrument runs on verdicts alone. |
| `DDD-frame-15` | conceptual | retired | RETIRED — "every completed act's determination demand is discharged by a filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw." The four modes do not partition: a declared default is both a filed decision and an arrangement default, a thermostat satisfies the judgment gloss under a rule canon times as encoded, and trained inference is policy commitment, judgment and standing encoded supply at once. Superseded by DDD-frame-17, which partitions the same object by dichotomy on determination and control. |
| `DDD-frame-16` | conceptual | projected | Discharge is act-indexed: standing supply is inherited per act and occasioned supply is produced per act, so there is no act-free discharge — governance never chooses whether demand is supplied, only by what, chosen in advance or defaulted at the act. |
| `DDD-frame-17` | conceptual | projected | At every completed act in a task's scope, each outcome-relevant alternative is discharged in exactly one of three ways: predetermined — the arrangement's standing configuration together with the ground at the act determines the resolution; exercised — it does not, and something within the arrangement's control determines it at the act; or drawn — it does not, and what determines it lies outside the arrangement's control. Demand is never unmet, only ungoverned. |
| `DDD-ground-01` | normative | projected | A governing decision must declare a resolvable applicability predicate, unless it explicitly declares universal applicability; non-evaluation must never silently become non-applicability, and where the predicate is implemented over declared ground axes, each axis is marked mechanically-evaluable or judgement-evaluable. |
| `DDD-ground-02` | conceptual | projected | Source coverage (covered · declared-empty · undeclared · unknown), resolution (resolved · deliberately-open · unknown), and assurance (adequate · inadequate · unknown) are orthogonal properties of ground relative to a filed decision set: only source coverage = undeclared is a source-coverage finding, deliberately-open is a resolution value carrying a deferred verdict, and Unknown is never a pass. |
| `DDD-ground-03` | conceptual | projected | A decision whose resolution is deliberately-open has no resolution for a timing predicate to read, so the timing vocabulary carries a fourth value — "—(open)" — alongside before, during, and after; any timing predicate without it misfiles open decisions, because every definite value it can assign erases the declaredness that makes them open. |
| `DDD-ground-05` | conceptual | projected | Declaring the determinable space is constitutively prior to determination over it — a determination selects a determinate, and determinates exist only as ways of occupying a declared determinable — with the symmetry that ground is prior within each act while decisions are prior in a registry's growth, so the priority is synchronic constitution and the bootstrap diachronic history, not a circle. |
| `DDD-hyp-01` | empirical | projected | Holding generation difficulty and resources constant, comparative advantage shifts toward high-throughput computational generators as acceptance becomes more operationally evaluable, feedback becomes faster and denser, ground becomes more accessible, checking becomes cheaper, and retries become more affordable. |
| `DDD-hyp-02` | empirical | projected | Human or institutionally situated arrangements retain greater comparative advantage as relevant ground becomes unavailable to the computational system, consequences are delayed, evaluators disagree, acceptance criteria drift over time, tacit or socially distributed knowledge is required, or normative legitimacy is part of the task. |
| `DDD-hyp-03` | empirical | projected | A generator-plus-checker arrangement — a computational generator composed with a mechanical checker or an independent reviewer — outperforms both generator-alone and judgment-alone baselines where candidate generation benefits from breadth or speed, significant parts of acceptance are operationally closed, and the remaining open residue can be escalated. |
| `DDD-hyp-04` | empirical | projected | Trust and deployment willingness are better predicted by the completeness of the accountability arrangement — attribution, persistent principal, authority linkage, stake, sanction path — than by whether the immediate executor is human or computational. |
| `DDD-hyp-05` | empirical | projected | Reliance on worker or provider selection increases as result-level evaluation becomes slower, less objective, less stationary, and less complete, holding labour supply, training cost, consequence severity, and task structure constant. |
| `DDD-measure-01` | empirical | projected | Specification demand is verdict entropy: for a task whose acceptance predicate closes, the demand engineers experience as specification burden is H(V) over the ground distribution. |
| `DDD-measure-02` | formal | established | Given the identification (DDD-measure-01), conservation on the closing region is the chain rule of entropy: H(V) = I(V;X) + H(V\|X) for any conditioning variable X. |
| `DDD-measure-03` | formal | reported | The seam of a decomposition is I(V;S); a decomposition with cheaper parts has pre-paid more demand into the seam, and H(V\|S) is minimised exactly when I(V;S) is maximised. |
| `DDD-measure-06` | formal | retired | RETIRED — "the measure exists iff the acceptance predicate operationally closes; H(V) is undefined exactly where the framework's floor result locates non-zero floor." The biconditional fails in both directions and the two limbs carry different warrants under one status. Superseded by DDD-measure-16 (availability to an arrangement, with existence and estimability separated) and DDD-measure-17 (the coincidence, at projected). |
| `DDD-measure-08` | formal | retired | RETIRED — "a better decomposition destroys demand." Cheaper parts were purchased by a higher-information seam; the destruction was an artifact of not counting I(V;S). |
| `DDD-measure-10` | formal | established | You cannot decompose your way out of the work: for a fixed closing task, H(V\|S) = 0 requires I(V;S) = H(V) — the parts become trivial only when the decomposition already encodes the entire verdict. Demand is conserved, not escapable by re-decomposition. |
| `DDD-measure-11` | conceptual | reported | The measure prices the verdict, not the search: H(verdict) is a property of the verdict function and the ground distribution and says nothing about the cost of computing a correct answer. Two tasks with identical verdict entropy can differ unboundedly in generation cost, so the measure must not be read as pricing generation. |
| `DDD-measure-15` | conceptual | projected | The engineering reading of the chain-rule identification holds only for admissible conditioning variables. A conditioning variable X is admissible where it is computable from ground available at the act and from what the arrangement has standing before it, and not from the verdict itself — computable by something that has not been handed the answer. The arithmetic holds for any X whatever; admissibility is what restricts the reading, not the identity. |
| `DDD-measure-16` | formal | established | The verdict-entropy construction is available to an arrangement exactly where the task's acceptance predicate closes for that arrangement; availability is a property of the arrangement, not of the task, and it is neither the existence of the verdict function nor the estimability of the ground distribution. |
| `DDD-measure-17` | conceptual | projected | The verdict-entropy construction's domain and the region where the framework's floor result locates non-zero floor coincide, and the coincidence is principled rather than evidential: the two arguments share the closure of the acceptance predicate as a premise, so their agreement about where the line falls is close to definitional on the measure's side and is not evidence that the identification is correct. |

### Decisions

| ID | Statement |
|---|---|
| `DDD-dec-15` | The escape mechanism's scope correction: overflow ∩ open is the mechanism of capacity-generated escape — sufficient for escape, never necessary for it. Escape as such stays as term:escape defines it, supplied by nobody for any reason, and term:escape-mechanism and DDD-floor-01 are re-scoped by supersession of their universal quantifier. |
| `DDD-dec-24` | Wave 3 files the principle layer's central material: the indexed-determination core given its canon home (core/14, with the flag clearances that home licenses), the discharge chain (the determinable, the determinate's two registers, supply-mode exhaustiveness, act-indexed discharge, constitutive priority of ground), and the hypothesis set as a new claim area — six derivation-grade claims, five statement-grade hypotheses, three settled terms, one new core document, filed by supersession-and-amendment with every divergence from source material reported rather than harmonised. |
| `DDD-dec-26` | The Track 1 session mints two terms and no more — term:commitment-level and term:residual-discretion, both established by core/14-indexed-determination.md §2 — discharging the mint DDD-frame-02 deferred pending use; three anticipated deltas (axis, arrangement, escaped decision) are ruled non-deltas because canon already carries each, and the five-way ground-provenance taxonomy is ruled ineligible for minting because its institutional slot is Q27-gated. |

### Terms

| ID | Term | Canonical wording |
|---|---|---|
| `term:accountability` | accountability | **Accountability** is a property of the arrangement, not of the executor: attribution of the determination, a persistent answerable party, and a borne consequence. An arrangement missing any of the three has not allocated the decision's consequence. |
| `term:actor` | actor | An **actor** is a system that resolves decisions by reading ground: variation in declared ground can alter the resolution through an internal pathway that selects among alternatives. A thermostat qualifies; a falling rock does not. Actorhood does not require intelligence. |
| `term:admission-test` | admission-test | **A choice is a decision iff varying *the choice* moves the outcome past tolerance.** **A fact is ground iff varying *the world* moves the outcome past tolerance.** |
| `term:answerability` | answerability | **Answerability** — the obligation to produce the chain: which determinations were made, by whom, against what ground. |
| `term:arrangement` | arrangement | The **arrangement** is the composition through which a resolution is produced and governed: executor, prior commitments, ground channels, checks, reviewers, record, and accountable principal. The unit of comparison is the arrangement, not the isolated actor. |
| `term:attribution` | attribution | **Attribution** — provenance-shaped, and therefore checkable: the record connecting the determination to the execution that produced it. |
| `term:closure` | closure | **Effective closure, defined.** A predicate is **closed for an arrangement** when the relevant ground is observable and adequacy can be evaluated within declared resource, latency, and confidence bounds. **Decidable** is reserved for the formal special case. |
| `term:commitment-level` | commitment-level | A **commitment level** is a level at which an arrangement fixes behaviour in advance: **outcome-level** — permitted resolutions fixed directly; **policy-level** — the generating procedure fixed; **principal-level** — a determiner selected by qualification and case-level resolution delegated. The three compose, and they are levels of commitment, not species of actor: the question is never which of three kinds an actor is, but at which levels the arrangement has committed. |
| `term:composite-actor` | composite-actor | A **composite actor** — several actors read as one at a declared boundary: from outside it the composite is **one actor**, with one capability envelope and one verdict owed. **A composite actor carries its members' demand, plus the seam demand between them.** |
| `term:conservation` | conservation | **For a task at a declared assurance level, and within a fixed decomposition of that task, determination demand is conserved.** Every governing decision gets made. The only choice is **by whom, when, and at what price.** Reduce the demand in one store and it **relocates**; it does not vanish. |
| `term:determinable` | determinable | The **determinable** — an outcome-relevant dimension of variation at the declared tolerance: the object determination resolves, and the dimension of comparability an axis names. Determinateness comes in orders — red → scarlet → this shade — and the declared tolerance names the order at which the framework stops distinguishing. |
| `term:determinate` | determinate | The **determinate** — one specific way of occupying a determinable: what discharge produces. A determinate is a way of being, not the determinable plus a differentia, and determinates under one determinable are constitutively exclusive at their grain. |
| `term:ensemble-actor` | ensemble-actor | **The choice is a property of the ensemble, and it exists nowhere in any member.** |
| `term:escape` | escape | **Escaped** — determined *never*, by nobody: decided-by-nobody as a first-class category. Latent defect exposure. **The only forbidden state.** |
| `term:escape-mechanism` | escape-mechanism | **Capacity-generated escape — the escape an actor produces from residual it has taken up — requires two conditions, both necessary:** **(1) Overflow** — demand exceeds resolve capacity. **(2) Open** — no verifier the actor holds. Overflow alone (closing predicate) → **retries, not escape.** Recoverable. Not floor. Open alone (within capacity) → **carried by judgment**, where an accountable supplier is named. Not floor. Where none is named, it is escape by another route (`05` §7) — outside this mechanism, not excluded by it. **Overflow AND open** → **escape. This is the floor.** **Sufficient for escape, never necessary.** A governing decision that never entered an actor's residual escapes without overflowing anything: escape is supplied-by-nobody (`term:escape`), and capacity shortfall is one generator of it. |
| `term:floor` | floor | The "floor" is the portion of a determination's demand that **cannot be moved off the in-the-moment actor** — the residue that no amount of encoding or checking can amortise, that must be paid, per run, in judgment. **The intrinsic floor is a property of the acceptance predicate, not of the decision.** |
| `term:liability` | liability | **Liability** — bearing the consequence. |
| `term:outcome` | outcome | The **outcome** — the determinate as it lands in the world, produced at every completed act. The **verdict** is the same determinate as assessed by a declared predicate, produced only where governance has declared one. The world renders outcomes, never verdicts; governance is the conversion of outcomes into verdicts. |
| `term:residual-discretion` | residual-discretion | **Residual discretion** is the outcome-relevant variation the arrangement's commitments leave open at the act, **held at fixed ground**: the alternatives still admissible once the standing configuration and the ground at the act are both given. It is not variation across ground — a cryptographic hash varies enormously with its input and exercises no discretion, because at each input the commitments fix the output exactly. It is not an observer's inability to predict a fixed policy, which is a fact about the observer and not about the arrangement. And it is not randomness: a deterministic arrangement can carry substantial discretion across unfamiliar cases, a randomised one can be tightly committed, and a zero-variance arrangement can be consistently wrong. |
| `term:seam` | seam | The **seam** — the coordination boundary decomposition creates between the parts: splitting a task or an actor manufactures new governing decisions, the ones about how the parts coordinate, that did not exist when the thing was whole. A composite carries the demand of its parts, **plus** the seam demand `S` created *between* them. |
| `term:store` | store | **{rule, check, actor, nothing}.** There is no fifth source. |
| `term:swarm-gate` | swarm-gate | **A swarm is an actor only if it genuinely determines choices against ground.** The admission tests (`00` §4) still gate, and they must. |
| `term:training` | training | **Closure decides whether training is *available*. Cost decides the *ratio* when it is.** Training requires a **reliable error signal** — you must be able to tell, and tell soon, whether the output was right. |
| `term:verdict` | verdict | **Definition (determination demand).** For a task whose acceptance predicate **closes** for the arrangement (`term:closure`; *decidable* is the formal special case, not the requirement), the predicate evaluates outcomes, and the **task class** supplies one correct output per input point. The **verdict** is that induced assignment — the correct output over each point of the input space. Let `P` be the distribution over inputs (the *ground distribution*). The **determination demand** of the task is the Shannon entropy of the verdict: **D = H(verdict)**, measured in **bits**. Where the task class supplies no such assignment, the predicate still evaluates outcomes and there is no verdict to have entropy about — which is the boundary `09` §7 draws. |

### The hypothesis set, as the graph holds it

The hypothesis set is broken out because its discipline is the easiest thing in the paper for a
reader to mistake. Every row is `projected`, every row declares a falsifier, **every evidence field
is empty**, and every row is owned by a study that has not been run. The columns below are the
graph's own fields, not the paper's summary of them.

| ID | Status | Evidence | Owner | Falsifier declared |
|---|---|---|---|---|
| `DDD-frame-07` | projected | `[]` (empty) | paper-4 | yes |
| `DDD-hyp-01` | projected | `[]` (empty) | paper-4 | yes |
| `DDD-hyp-02` | projected | `[]` (empty) | paper-4 | yes |
| `DDD-hyp-03` | projected | `[]` (empty) | paper-4 | yes |
| `DDD-hyp-04` | projected | `[]` (empty) | paper-4 | yes |
| `DDD-hyp-05` | projected | `[]` (empty) | paper-4 | yes |

*Generated from the graph at `v5.12.0`. 48 claims, 3 decisions, 24 terms.*
