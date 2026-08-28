# The Missing Parameter: Actor-Indexed Determination

### Where consequential choices are resolved, what assures them, and who answers

*Emil — Context&. Statement paper.*

*This paper is a projection of `actor-indexed-determination` at `v5.9.0`. Every bracketed claim,
decision and term identifier resolves against that one ref, and Appendix A reproduces each of them
from it, so the paper can be checked without the repository. No identifier here resolves against the
downstream repository, so no downstream ref is pinned. The companion measure note —
`papers/measure-note/measure-note.md` in `decision-driven-design` — is cited by path at commit
`aa7e135`, which carries its discharge section; the note is absent from `v0.4.0` and from every
earlier downstream tag, so it resolves at that commit rather than at a tag.*

---

## Abstract

Several influential accounts of complexity, control and verification describe where the work of
determination resides while holding the determiner largely fixed. That omission has become
consequential, because engineered systems now combine authored procedures, learned policies, human
judgment, mechanical checks and institutional principals inside one arrangement.

We state **actor-indexed determination**: unresolved determination is relative not to a task alone
but to a tuple of task, accessible ground, acceptance relation, declared tolerance, system
arrangement and assurance requirement. Three levels at which behavioural commitments attach —
outcome, policy and principal — are distinguished, and the *source* of a resolution is separated
from the *mechanism* that assures it. This yields a precise account of an **escaped decision**: a
consequential resolution that no adequate source-and-assurance combination governs, and whose
unacceptable outcomes are not reliably detected.

Two results give the framework its shape. Every completed act's determination demand is discharged
— by a filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw — so
**demand is never unmet, only ungoverned**; and discharge is act-indexed, so governance never
chooses whether demand is supplied, only by what. On the region where the acceptance predicate
closes, that demand is measurable, and its conservation is the chain rule of entropy. Off that
region the measure does not exist and the governance question still does.

The contribution is not a new species taxonomy of programs, models and humans. It is a framework
for analysing where consequential choices are resolved, how commitments attach, what can be
verified, who bears the residual consequence, and which choices have been left to accident.

---

## Note on claim status

This paper is a **projection**. Every load-bearing statement below either cites a node in the
framework's claim graph or is marked as the paper's own analysis. The graph's status vocabulary is
used throughout and is not this paper's to redefine:

- **settled** / **established** — argued and unchallenged in the graph.
- **reported** — exercised by a reproducing computation.
- **projected** — proposed with a declared falsifier, not yet met.
- **draft** — filed, not yet ratified.
- **retired** — superseded, retained with the correction that killed it.

The paper's primary claim is `projected` [DDD-frame-01]. So is most of what follows. Where a
statement is the paper's own analysis rather than the graph's, it is marked **(analysis)** and
carries no claim status at all, because it is not a claim. Appendix A reproduces every cited node
word-for-word from the graph, with its status, so the paper can be checked without it.

---

## 1. The parameter hidden by a fixed arrangement

Ashby's regulator has no species.

It is described by the variety it can absorb, not by whether that variety is supplied by a governor,
a nervous system, a bureaucracy or a program. Brooks, Tesler and Meyer each analyse the allocation
of work differently (§11), and they share one limitation: the arrangement that performs, checks and
answers for the work is usually held fixed while the allocation problem is analysed.

**A parameter that never varies is indistinguishable from a constant.** For much of software
engineering, treating the determiner as fixed was productive, because the operative arrangement was
reliably some combination of authored procedure, human developer, human operator and mechanical
execution. Contemporary systems make the omitted parameter harder to ignore, because the same
governing choice may now be allocated among an explicit rule, a learned policy, a human specialist,
a model with tools, an automated checker, a reviewer, an organisation that authorises and bears
consequences — or a composition of several of these.

The important change is not that an unprecedented third species has appeared — probabilistic
programs, adaptive systems, learned components, organisations and collectives all predate
contemporary generative models. The change is operational: heterogeneous arrangements now resolve
consequential choices inside ordinary engineering systems, at a scale that makes their differences
load-bearing. **(analysis)**

### 1.1 The primary claim

Let a determination problem be described relative to a task `T`, accessible ground `G`, an
acceptance relation `P`, a declared tolerance `τ`, a system arrangement `A`, and an assurance
requirement `α`. The paper's primary claim is the framework's:

> **Unresolved determination is indexed by the tuple ⟨task, ground, acceptance relation, tolerance,
> arrangement, assurance⟩, not by the task alone.** [DDD-frame-01, projected]

The framework built those coordinates severally before stating them as one relation: tolerance and
assurance separated first, the arrangement established as the unit of comparison, ground and the
acceptance predicate defined as primitives. The index is those coordinates read as a single
relation, and the filing that gave it a canonical home records exactly that provenance
[DDD-dec-24].

Move any coordinate and the determination problem moves with it: which distinctions are committed
in advance, which choices remain for the act, which outputs can be checked, whose identity must be
trusted, who answers, and which residual risks stay accepted — or escape.

### 1.2 What the paper claims, and what it does not

The paper claims a framework and a vocabulary, together with a set of graded predictions that are
not yet tested. It does not claim an empirical result. It does not claim a boundary between human
and computational work. It does not claim that determination demand is a measured invariant in
general — only on the region where the acceptance predicate closes, where the measure exists and
the conservation statement is arithmetic (§4.4).

One question sits adjacent to this paper and is deliberately not taken up: software mechanised the
half of engineering that names what varies, and never mechanised the half that resolves it — an
asymmetry with its own literature and its own burden of survey, which belongs to a different paper.

---

## 2. Actors, arrangements and ground

### 2.1 The actor admission test

An **actor** is a system whose output is selected through an internal state transition that is
causally sensitive to information obtained from declared ground [term:actor, settled]. Three
elements are required, and the framework's admission test is what checks them
[term:admission-test, settled].

1. **Alternatives.** At the declared abstraction and tolerance, more than one outcome-relevant
   resolution is possible.
2. **Information-bearing pathway.** Variation in declared ground can alter the resolution through
   an identifiable sensing, communication, representation or state-transition pathway *inside* the
   candidate actor.
3. **Selection.** That pathway participates in selecting among the alternatives, rather than merely
   perturbing an external physical trajectory.

A falling rock fails the second condition. Wind and terrain alter its trajectory directly; nothing
inside the rock represents those conditions and uses them to select among declared alternatives. A
thermostat passes: sensed temperature changes an internal control state, and that state selects
fire or hold. Neither verdict depends on intelligence, and that is the point of stating the test
this way.

Actorhood is relative to an abstraction boundary. A market is one actor when its aggregate
price-forming process is the relevant selector, and many actors when individual bids and
institutions are being analysed. An organisation is one actor for an authorisation decision and
several for the workflow that produces it. The framework carries this scale relativity in its
composite vocabulary: a **composite actor** is an arrangement treated as one determiner
[term:composite-actor, settled]; an **ensemble actor** is a population treated as one
[term:ensemble-actor, settled]; and a **swarm gate** is the condition under which the ensemble
reading is admissible at all [term:swarm-gate, settled].

### 2.2 What the alternatives are

The framework names the object determination resolves, and it borrows the noun rather than coining
one. A **determinable** is an outcome-relevant dimension of variation at the declared tolerance —
the dimension of comparability an axis names [term:determinable, settled]. A **determinate** is one
specific way of occupying that dimension: what discharge produces [term:determinate, settled].
Determinates under one determinable are constitutively exclusive at their grain, and
determinateness comes in orders — red, then scarlet, then this shade — with the declared tolerance
naming the order at which the framework stops distinguishing.

This is not decoration. It fixes what determination *is about*:

> **Determination's object is the determinable — an outcome-relevant dimension of variation at the
> declared tolerance — and its product is a determinate, one specific way of occupying that
> dimension; determination demand is thereby a measure over unresolved determinables, the verdict
> variable's support being the determinate-space at the declared grain where the predicate closes.**
> [DDD-frame-13, projected]

The relation runs the other way as well. Declaring the determinable space is constitutively prior
to determining over it, because a determinate exists only as a way of occupying a declared
determinable [DDD-ground-05, projected]. An arrangement that has not declared what varies has not
yet posed a determination problem; it has only an outcome.

The determinable/determinate relation, its non-genus-species structure, its constitutive
exclusivity and its orders of determinateness are W. E. Johnson's, developed by Prior, Funkhouser
and Wilson (§11). The identification of the determinable as demand's object, and of the verdict
variable's support as the determinate-space at the declared grain, is the framework's
[DDD-frame-13, credits].

### 2.3 Decision and ground

A **decision** is a declared, outcome-relevant alternative whose resolution is subject to
governance at a chosen abstraction and assurance level. The admission test is what makes it one: a
choice is a decision exactly when varying it moves the outcome past the declared tolerance
[term:admission-test].

**A fact belongs to ground when information about it can change the resolution or its acceptance
status beyond the declared tolerance** [DDD-dec-26]. This definition deliberately declines the
claim that every physical transition is a decision. The framework begins where a designer, analyst
or institution declares an outcome-relevant alternative and asks how its resolution is governed.

Ground carries orthogonal properties relative to a filed decision, and the framework keeps them
apart because collapsing them is a common failure: source coverage (covered, declared-empty,
undeclared, unknown), resolution (resolved, deliberately-open, unknown), and assurance (adequate,
inadequate, unknown) vary independently [DDD-ground-02, projected]. A decision whose resolution is
deliberately open has no resolution for a timing predicate to read, which is why the framework's
timing vocabulary carries a fourth value alongside before, during and after [DDD-ground-03,
projected]. And a governing decision must declare a resolvable applicability predicate unless it
declares universal applicability, so that **non-evaluation never silently becomes
non-applicability** [DDD-ground-01, projected].

### 2.4 Ground provenance

**(analysis)** Ground is not homogeneous, and the differences between kinds of ground drive
engineering decisions that the single word conceals. The canon half is the definition already given
in §2.3: **a fact belongs to ground when information about it can change the resolution or its
acceptance status beyond the declared tolerance** [DDD-dec-26]. Everything below is this paper's
sorting of what that definition admits, and it is offered as analysis rather than as canon.

| Provenance | The ground is | Finer distinctions where they matter |
|---|---|---|
| **Controlled** | maintained by the arrangement and enforceable through commitments | — |
| **Observed** | read from an external or independently changing system | **sensory** — read at the act, current by construction; **recorded** — read from a store, current only as of its write |
| **Inferred** | estimated from data or a model | **derived** — computed from ground already held; **predicted** — estimated about a state not yet observed |
| **Institutional** | supplied through rules, conventions, authority or social practice | — |
| **Missing** | relevant and unavailable to the executing arrangement | — |

**Why the observed/inferred sub-distinctions earn their place.** *A stored statement about
uncontrolled ground is not equivalent to a current observation of that ground.* That sentence is the
whole practical yield of the taxonomy, and it is a claim about the sensory/recorded boundary rather
than about observation in general. Revalidation cadence should depend on drift rate, consequence,
consistency guarantees and the declared assurance level, rather than on a universal "read every
time" rule — and an arrangement cannot reason about cadence at all until it knows which of its
observed ground is sensed and which is recalled. The derived/predicted boundary does the same work
on the inferred slot: a derived value fails when its inputs are wrong, a predicted one fails when
the world moves, and the two want different checks.

**Missing ground is a slot, not an omission.** It is what makes an arrangement's limits a property
of *ground* rather than of the executor, which is why the first variable in the framework's
situated-advantage hypothesis is relevant ground being unavailable to the computational system
[DDD-hyp-02, projected]. An act whose acceptance depends on ground the arrangement cannot reach has
a floor, whatever the executor's capability (§6.1). Dropping this slot would relocate a ground
property onto the actor, which is precisely the collapse the index exists to prevent.

**Institutional provenance, and the mechanism this paper does not state.** Institutional ground is
supplied by rules, conventions, authority and social practice, and it is the slot §7's
accountability material leans on: an authority that supplies ground is usually also a party that can
answer for it. *How* that supply works — what makes an institution's statement usable as ground, and
what makes it fail — is **a question the framework has open and has not answered.** The trust
material that would settle it is unfiled, and this paper does not anticipate it. Institutional
provenance is named here and its mechanism is stated as pending that filing, cited as an open
question rather than smuggled in early.

*This five-way partition is not canon. The framework has ruled it ineligible for minting rather than
merely deferred — a mint would fix a partition that the open trust question may restructure —
so it is carried here as this paper's analysis, marked non-canon at the point of use, with the
institutional slot's mechanism flagged as pending on that same question [DDD-dec-26]. This paper
flags the gap and files nothing.*

### 2.5 The arrangement, not the isolated actor

An actor rarely determines alone. The **system arrangement** is the composition of producer or
executor, prior commitments, available ground channels, tools and memory, verification mechanisms,
reviewers or authorisers, execution record, accountable principal, and remediation and sanction
paths [term:arrangement, settled].

The same model, program or person behaves differently across arrangements. A language model without
repository access is not the same determiner as the same model with retrieval, tests, a compiler
and a human reviewer. A person acting privately is not the same accountable arrangement as the same
person acting through a licensed organisation with records, insurance, review and appeal.

**The unit of comparison is therefore the arrangement, not the isolated actor** [term:arrangement].
Almost every empirical question in this paper inherits that unit, and §9's hypotheses are stated
over arrangements for exactly this reason.

---

## 3. Commitment resolution

How does an arrangement fix behaviour in advance? The framework's answer is three levels, and the
levels compose.

> **Behavioural commitments attach at three levels — outcome, policy, principal — which compose and
> are not actor species; residual discretion is the outcome-relevant variation that remains after
> the arrangement's declared commitments are applied.** [DDD-frame-02, projected]

Two terms name the halves of that claim. Both were minted only when a downstream projection needed
them as citable nodes, and **both carry `draft` status** — they are filed and not yet ratified, and
this paper shows the status rather than quietly promoting it [DDD-dec-26].

### 3.1 The three levels

> A **commitment level** is a level at which an arrangement fixes behaviour in advance:
> **outcome-level** — permitted resolutions fixed directly; **policy-level** — the generating
> procedure fixed; **principal-level** — a determiner selected by qualification and case-level
> resolution delegated. [term:commitment-level, **draft**]

**Outcome-level** commitment fixes the answers. A validation table, an enumerated set of permitted
states, a hard-coded threshold: the arrangement has decided in advance what may come out, and the
act has nothing left to resolve along that dimension.

**Policy-level** commitment fixes the procedure that generates the answers. A retry policy, a
routing rule, a trained model deployed under a fixed decision procedure: the arrangement has not
decided what will come out, but it has decided how the answer will be produced.

**Principal-level** commitment fixes neither. It selects a determiner by qualification and delegates
the case-level resolution — a licensed engineer signs off, a reviewer with named authority accepts,
a specialist decides. Assurance here attaches to the actor rather than to a mechanism, which is the
expensive case and is priced as such [DDD-cost-09, projected].

The three compose, and the question is never which of three kinds an actor is, but at which levels
the arrangement has committed [term:commitment-level]. A single deployed system routinely carries
outcome-level commitments on its input validation, policy-level commitments on its retry behaviour,
and principal-level commitments on its exception path. Reading those as three species of actor is
the error the level vocabulary exists to prevent.

### 3.2 Residual discretion

> **Residual discretion** is the outcome-relevant variation remaining at the act after the
> arrangement's declared commitments are applied. It is not randomness: a deterministic arrangement
> can carry substantial discretion across unfamiliar cases, a randomised one can be tightly
> committed, and a zero-variance arrangement can be consistently wrong.
> [term:residual-discretion, **draft**]

Those three clauses each block a different mistake. Determinism is not commitment: a program that
always does the same wrong thing on an unfamiliar input has enormous outcome-relevant variation
across the input space, all of it unresolved by any declared commitment. Randomisation is not
discretion: a sampler drawing from a tightly bounded distribution the arrangement declared and
accepted has been committed at policy level. And low variance is not correctness: an arrangement
can be consistent and consistently unacceptable, which is why variance is never the measure of
commitment.

### 3.3 Boundary cases

**(analysis)** Three cases test the vocabulary, and each resolves inside it.

*A configuration file.* Its values look like outcome-level commitments and often are. Where a value
is edited per deployment by whoever is on call, the commitment is nominal: the file records a
resolution that is in fact taken at the act by an actor, and the arrangement should read as
principal-level with a written default. The test is not where the value is stored but whether
varying it at the act is possible and consequential.

*A trained model.* Training is policy-level commitment — the generating procedure is fixed and the
answers are not — with the important qualification that what training buys is *allocation* and not
*capacity* [DDD-cost-20, projected]. Deploying the same weights behind a stricter acceptance check
changes the arrangement's commitments without changing the model at all, which is §2.5's point
arriving in a concrete form.

*An escalation path.* An arrangement that commits at outcome level for familiar cases and delegates
unfamiliar ones to a named principal has committed at two levels simultaneously. This is the
ordinary case in deployed systems, and the composition clause is what lets the framework describe
it without inventing a fourth level.

---

## 4. Resolution and assurance

The framework's earlier four-store model mixed two dimensions. A cleaner model separates *where a
resolution comes from* from *how its acceptability is established*.

> **The source of a resolution and the mechanism assuring it are separate dimensions;** the
> four-store model held the arrangement largely fixed while the allocation was analysed, and did not
> draw the distinction. [DDD-frame-03, projected]

That separation is the section's spine. Section 4.1 takes the source side, §4.2 the assurance side,
§4.3 what happens when neither is adequate, and §4.4 what is conserved across every rearrangement
of the two.

### 4.1 Source of resolution: the four discharge modes

A completed act's determination demand is not sometimes supplied and sometimes not. It is always
supplied, and the only question is by what.

> **At every completed act in a task's scope, the act's determination demand is discharged — by a
> filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw; escape is a
> supply mode of discharge, not an absence of supply — demand is never unmet, only ungoverned.**
> [DDD-frame-15, projected]

The four modes classify **the producer of the resolution**, not its governance status. A *filed
decision* is variation authored in advance and delivered at the act. *Judgment* is variation
produced at the act by an actor reading ground. A *default* is variation carried by the
arrangement's standing configuration without a fresh resolution — and a default may be declared and
governed, or incidental and not. A *draw* is variation living in nothing the arrangement controls.

Discharge is also indexed to the act, on both sides of the supply split:

> **Discharge is act-indexed: standing supply is inherited per act and occasioned supply is
> produced per act, so there is no act-free discharge — governance never chooses whether demand is
> supplied, only by what, chosen in advance or defaulted at the act.** [DDD-frame-16, projected]

"Paid once, inherited by every run" is therefore a statement about *inheritance*, not about
authoring: even fully pre-resolved demand is consumed per act, at the moment the act inherits it
[DDD-delivery-01, projected]. The measure note works that arithmetic over `N` acts, with an asset
behind it; this paper cites the worked projection rather than restating it (measure note §6).

#### The seam this section must not cross

The framework carries **two partitions over the same act**, and they answer different questions.
Collapsing them is the error most available to a careful reader, so the distinction is stated here
rather than left to be inferred.

| | The store partition | The discharge partition |
|---|---|---|
| Asks | what **governance supplied** | what **the world produced** |
| Values | `{rule, check, actor, nothing}` [term:store] | filed decision · judgment · default · draw [DDD-frame-15] |
| Escape is | **nothing** — "there is no fifth source" | **a supply mode** — the uncontrolled draw |

Both are correct, and neither reduces to the other [DDD-frame-15, region]. In the store partition
escape is nothing, because the question is what governance supplied and the answer is that nothing
did. In the discharge partition the same act's demand is met by an uncontrolled draw, because the
question is what the world produced, and **the world never produces nothing**. A reader who reads
one partition's "nothing" into the other's four modes will conclude the framework contradicts
itself; it does not, and the two questions are simply distinct.

*This paper's §4.1 replaces the source enumeration its own foundation document used —* prior
commitment, runtime actor, environmental-or-default, failure-or-non-resolution. That enumeration
mixed declared defaults with uncontrolled dynamics in its third source, and its fourth was not a
discharge mode at all, since even a failed arrangement's act lands an outcome in the world register
[DDD-frame-15, notes]. Canon governs, and the paper carries canon's form.

### 4.2 Assurance mechanism

A resolution may be assured by proof or static constraint, by mechanical checking, by runtime
monitoring, by independent human review, by accountable authorisation, by statistical evaluation,
by post-deployment audit or consequence — or by no adequate mechanism at all.

Checks occur before, during or after execution, and the framework denominates those positions
rather than leaving them informal: assurance mechanisms occupy **pre-act** positions (selection,
training, encoding, static checks), **at-act** positions (monitoring), and **post-act** positions
(review, audit, consequence), each with a latency, and **a mechanism whose latency exceeds the
consequence horizon does not assure** [DDD-cost-25, projected]. Timing is therefore not the
defining property. The defining property is whether acceptability is evaluated through a criterion
independent enough to detect relevant failure.

Where assurance attaches matters economically, and the framework prices it. Assurance-by-actor
binds assurance to a scarce carrier and is supplied **occasioned** — at the act, at the carrier's
class price. Assurance-by-check moves it into a mechanism and is supplied **standing** —
independent of the act [DDD-cost-09, projected]. Actor selection for an act is consequently
two-gated: capacity gates always, since the actor must carry the act's residual at the declared
tolerance or the excess escapes; assurance gates exactly where the acceptance predicate does not
close [DDD-cost-08, projected].

### 4.3 Escaped decisions

> **Escaped** — determined *never*, by nobody: decided-by-nobody as a first-class category. Latent
> defect exposure. **The only forbidden state.** [term:escape, settled]

An escaped decision is a consequential resolution that no adequate source-and-assurance combination
intentionally governs, and whose unacceptable outcomes are not reliably detected. The framework
predicts consequences from it:

> **Escaped decisions — consequential resolutions with no adequate source-and-assurance combination
> — predict ungoverned failure modes and design-review findings.** [DDD-frame-04, projected]

**"Escaped" does not mean "determined by nothing."** Defaults, physical behaviour, legacy code,
incentives and accidental interaction still determine an outcome. Escape means the outcome is not
deliberately governed and assured — which is exactly the seam guard of §4.1 read from the escape
side.

It follows that **escape is tested on the arrangement, not on the outcome**. Ask whether any
adequate source-and-assurance combination governed the act. If none did, the act escaped whether or
not what landed happened to be acceptable, because what landed was drawn from a distribution the
arrangement did not control [DDD-frame-15, derivation].

#### Filing is not delivering

An escape generator that ordinary practice systematically underweights: a decision can be filed,
correct, and still absent at the act.

> **Governance filed but not delivered is escape: no source supplied the governing decision at the
> act, so it was determined by nobody (`term:escape`, supply-general), and delivery failure is
> thereby a generator of escape — sufficient, never necessary — whose distinguishing feature is that
> the ledger shows coverage: escape that presents as governance.** [DDD-delivery-02, projected]

A decision sits in the arrangement's encoded store only to the extent the arrangement delivers it
at the act, so store allocation cannot be read off artefacts [DDD-delivery-01]. Worse, the failures
correlate: an unretrieved decision and an unretrieved check over the same act share an actor, a
budget and a position, so judgment-mediated delivery on both the source and the assurance side
silently removes the independence the assurance argument assumed [DDD-delivery-03, projected].

#### The two registers of what discharge produces

Every discharge produces a determinate, and it lands in two registers:

> **Discharge always produces a determinate, which lands in two registers: as an outcome — the
> determinate as it lands in the world, produced at every completed act — and as a verdict — the
> determinate as assessed by a declared predicate, produced only where governance has declared one;
> governance is thereby the conversion of outcomes into verdicts, and every diachronic instrument
> runs on verdicts alone.** [DDD-frame-14, projected]

**The world renders outcomes, never verdicts** [term:outcome, settled]. This is why §4.1's fourth
mode is a draw rather than a failure: the act lands something regardless. It is also why every
diachronic instrument the framework describes — audit, review, learning from consequence — runs on
verdicts alone, and therefore only reaches the region where a predicate has been declared.

### 4.4 What is conserved

The framework holds a conservation statement:

> **For a task at a declared assurance level, and within a fixed decomposition of that task,
> determination demand is conserved.** Every governing decision gets made. The only choice is **by
> whom, when, and at what price.** Reduce the demand in one store and it **relocates**; it does not
> vanish. [term:conservation, settled]

This paper states that as a principle of the framework, and it states the one region where the
principle is more than a discipline — with the boundary made explicit, because the boundary is
where honesty about it lives.

**The identification, and what kind of claim it is.** For a task whose acceptance predicate closes,
the demand engineers experience as specification burden is identified with the Shannon entropy of
the **verdict** — the correct output the predicate assigns over the distribution of ground the task
faces [DDD-measure-01, projected; term:verdict, settled]. **This identification is a modelling
claim.** It is falsifiable, it is `projected`, and its declared falsifier is a correspondence that
has not been run.

**The conservation statement on that region, and what kind of claim it is.** Given the
identification, conservation is the chain rule of entropy:

> **H(V) = I(V;X) + H(V|X)** for any conditioning variable `X`. [DDD-measure-02, **established**]

**This is arithmetic.** It is Shannon's, it holds for every joint distribution, and its holding is
not evidence for anything the framework claims. The two must never be fused: the arithmetic is
certain and empty on its own, the identification is contentful and unproven, and the framework's
strength on this region is exactly the strength of the identification and no more. The companion
measure note states that separation at length and this paper does not re-derive it (measure note
§7).

Three consequences are worth carrying into a statement paper.

**You cannot decompose your way out of the work.** For a fixed closing task, `H(V|S) = 0` requires
`I(V;S) = H(V)`: the parts become trivial only when the decomposition already encodes the entire
verdict [DDD-measure-10, **established**]. The seam of a decomposition is `I(V;S)`, and a
decomposition with cheaper parts has pre-paid more demand into the seam [DDD-measure-03, reported;
term:seam, settled]. The measure note's worked date-validation task computes both halves exactly
for two decompositions of one task: totals of 25.493 bits either way, split 20.593 / 4.901 by one
decomposition and 11.020 / 14.474 by the other (measure note §4; `core/09` §3). Demand is conserved
across the two, not escaped by either.

**The bound, stated and not implied.** The measure exists **if and only if** the acceptance
predicate operationally closes, and `H(V)` is undefined exactly where the framework locates a
non-zero floor [DDD-measure-06, **established**]. Off the closing region there is no verdict
function to have entropy about, and conservation is what it was before the measure existed: an
accounting discipline, a principle rather than a measured invariant.

**Governance outruns measurement.** The governance question — is every decision governing the act
in a declared store, none escaped? — is well-formed on the total domain, including open predicates
where the measure does not exist; the cost question exists only where the predicate closes
[DDD-frame-11, projected]. **The framework's governed domain is strictly wider than its measured
domain**, and nothing about the measure's silence licenses a claim that determination is
unaccountable where the measure stops.

The framework also carries the stronger, unmeasured form — demand conserved as a scalar across
arbitrary rearrangements, actor-generally and including open predicates [DDD-frame-10, projected].
That claim is `projected` and this paper does not argue it. It is named so that a reader can see
which half of the conservation material has a measure behind it and which does not.

---

## 5. Closure and evaluability

The acceptance relation is central to everything above, and the word "closure" has to be divided
before it can carry weight. Let `P(c, G)` denote whether candidate `c` is acceptable relative to
declared ground `G`.

The framework's own closure is operational:

> **Effective closure, defined.** A predicate is **closed for an arrangement** when the relevant
> ground is observable and adequacy can be evaluated within declared resource, latency, and
> confidence bounds. **Decidable** is reserved for the formal special case. [term:closure, settled]

### 5.1 Four kinds of closure

**(analysis)** Four questions travel under the one word, and they are independent. This
quadruple is the paper's own framing, not a canon taxonomy; the framework files operational closure
as its closure, prices economic closure in its cost register, and does not currently name normative
closure at all.

**Logical closure.** An acceptance procedure exists and terminates for every candidate in the
declared domain. This is formal decidability, and it says nothing by itself about practical cost.

**Operational closure.** The acceptance procedure can be executed with the ground, time, memory,
tools, permissions and reliability available to the arrangement. This is the relevant concept for
deployed systems, and it is what [term:closure] names.

**Economic closure.** Generation and verification can be performed at an acceptable cost relative
to the value, latency, consequence and assurance requirement of the task. A procedure can be
logically and operationally available and still economically useless.

**Normative closure.** The acceptance relation adequately represents the values, rights, trade-offs
and stakeholders the arrangement is meant to serve. A mechanically executable predicate may be
normatively incomplete, contested or gameable.

**A second axis follows, and it is orthogonal to this one.** These four name *which* closure
question is being asked. The next section asks *how strong* the answer is once the question is
fixed as operational. A predicate has a position on both axes at once, and neither reading
constrains the other — so nothing in §5.2 competes with the four kinds, and a reader meeting both
should not look for a contradiction between them.

### 5.2 How strong is the closure?

**(analysis)** Section 5.1 sorted the questions. This section orders the answers to one of them.
Fix the question as operational closure — the framework's own [term:closure] — and predicates still
differ in *degree*, along a gradient the framework's material already implies and has not yet
assembled in one place. Four rungs, weakest first.

| Rung | What holds | Where the framework says so |
|---|---|---|
| **Open** | No acceptance procedure over accessible ground at the declared assurance level. | [term:closure], by negation |
| **Verification-closed** | Adequacy can be *evaluated* within declared resource, latency and confidence bounds. | [term:closure] |
| **Constructively closed** | The verdict is *computed by rule* from ground available at the act. | measure note §8 |
| **Formally decidable** | An acceptance procedure exists and terminates over the declared domain. | [term:closure]'s reservation |

**Open.** No procedure decides acceptability, so there is no verdict function to have entropy about
and the measure does not exist [DDD-measure-06, **established**]. Governance is untouched by this:
the question of whether every decision governing the act sits in a declared store, none escaped, is
well-formed on the total domain [DDD-frame-11]. The measure's silence here is a fact about the
measure.

**Verification-closed.** The rung canon means by *closure*: the relevant ground is observable and
adequacy can be evaluated within declared bounds [term:closure]. Two things become available at
once. The measure exists, so specification demand is `H(V)` [DDD-measure-01]. And producer identity
stops being epistemically necessary — for the checked property, and nothing more [DDD-frame-05].

**Constructively closed.** A predicate can be more than checkable. Call it **constructively closed**
when the verdict is not merely evaluable but computed by rule from ground available at the act: a
procedure returns the correct output directly, and there is no candidate search to price. Closure
asks whether adequacy can be *evaluated*; constructive closure asks whether the verdict can be
*produced*. The distinction is the measure note's, and the worked date task of §8.6 is its example —
its entropies are exact and exhaustive rather than sampled precisely because the verdict there is
computed rather than searched for (measure note §8).

**Formally decidable.** Placed last and deliberately not at the top. Canon reserves *decidable* for
the formal special case rather than making it the requirement [term:closure], and the reservation is
load-bearing in both directions: any bounded finite domain is decidable by lookup, and a decidable
checker may demand resources no arrangement has. Decidability is therefore a special case of the
ladder rather than its summit, and the rungs that govern deployed arrangements are the middle two.

#### The retirement this ladder walks past

The third rung approaches a claim the framework killed, and the approach has to be stated carefully
because the resemblance is real.

> **RETIRED — "closed predicates make intelligence unnecessary."** Does not follow from
> producer-independence under verification; generation may still require whatever capability the
> search demands. [DDD-frame-09, **retired**]

The retirement turns on a premise: that a search remains, and that verification-closure bounds
nothing about how expensive it is [DDD-frame-06, **established**; DDD-measure-11, reported].
Constructive closure does not contradict that finding. It **sidesteps** it — where the verdict is
computed by rule, there is no search left to be expensive, so the premise the retirement turns on is
**absent rather than denied**.

The difference matters, because the two readings license different things. Denying the retirement
would license inferring cheap generation from closure, which is exactly what was retired.
Sidestepping it licenses nothing beyond the case at hand: a predicate whose verdict is computed has
no generation cost to bound, and predicates whose verdicts are merely checkable are untouched. The
scoped survivor of the retirement — that producer identity is not necessary *for the checked
property and nothing more* — holds either way [DDD-frame-05].

*Canon's closure vocabulary does not carry the constructive/verification distinction. `term:closure`
is stated in evaluative terms alone, no claim node names the stronger rung, and the word*
constructive *occurs nowhere in the principle repository's core documents. The rung above is stated
register-native, as this paper's analysis and not as canon; a dedicated node is pending filing on
the framework's open-questions wave, and until it lands the citation basis is closure, the
separation of closure from generation cost, and the measure's silence on search, as cited above.
This paper flags the gap and files nothing.*

### 5.3 Closure is not generation cost

The single most load-bearing separation in this section:

> **Closure is distinct from generation cost: verification being cheap implies nothing about the
> density or accessibility of the acceptance region.** [DDD-frame-06, **established**]

A proof may be easy to check and extremely hard to discover. A cryptographic preimage is trivially
verifiable and infeasible to find. A predicate may accept exactly one candidate out of an enormous
space. None of these contradicts closure. What they refute is the inference *from* closure *to*
cheap adequacy, and that inference is the one the framework retired a claim over (§10).

The measure register says the same thing from its own side: **the measure prices the verdict, not
the search.** `H(verdict)` is a property of the verdict function and the ground distribution, and
two tasks with identical verdict entropy can differ without bound in what it costs to compute a
correct answer [DDD-measure-11, reported].

The variables that govern how hard it is to *produce* an acceptable candidate are separate from
closure and worth naming: density of acceptable outputs, topology of the acceptance region, search
space size, availability of gradients or incremental feedback, cost of retries, generator
capability, access to relevant ground, and adversarial pressure. **(analysis)**

### 5.4 Producer independence, and nothing more

The strongest defensible result about closure is narrow, and the framework states its limits inside
the claim rather than in a footnote:

> **Under a sound terminating operational checker with complete declared ground, producer identity
> is not epistemically necessary for the checked property — and nothing more: not cheap generation,
> not normative completeness, not accountability.** [DDD-frame-05, projected]

The five things it does not imply are worth enumerating, because each has been inferred from it in
practice: that the candidate was cheap to generate; that the predicate captures every relevant
value; that the checker is legitimate or correctly implemented; that the candidate is safe outside
the declared ground; and that accountability disappears (§7).

### 5.5 The two gates, and what closing a predicate does

Closure changes what an arrangement must buy, and the framework prices the change rather than
asserting a boundary.

> **On an open predicate, assurance and actor class are positively coupled; closing the predicate
> flips the sign — the assurance gate lifts and the capacity gate softens — so the actor class the
> act requires falls, leaving the actor carrying generation only.** [DDD-cost-11, projected]

Required actor class is computed **per capability, not per act**: it is the maximum, over the act's
capabilities, of the class needed where assurance is not mechanically discharged [DDD-cost-12,
projected]. This matters for how the framework's predictions are read. It does not say models win
where predicates close and people win where they do not. It says the *price* of the assurance an
act needs moves with closure, per capability, and that arrangements respond to prices.

### 5.6 Where no adequate procedure exists

Where no adequate acceptance procedure is available over accessible ground at the declared
assurance level, acceptance cannot be fully discharged through direct mechanical verification. The
residual may depend on situated judgment, social convention, institutional authority, delayed
observation, trust, negotiation, or explicit risk acceptance. **(analysis)**

This does not establish that a person can necessarily find a correct answer. Some tasks are
under-specified, contested, unknowable or impossible rather than merely judgment-dependent, and the
framework's hypotheses are written to respect that difference (§9) [DDD-hyp-02, region].

---

## 6. Actor-indexed irreducibility

Brooks's essential/accidental distinction becomes more precise when it is indexed. The framework's
statement of that precision is its strongest result, and it is relational:

> **The judgment floor is relational: irreducibility is a property of the indexed relation ⟨task,
> ground, acceptance relation, tolerance, arrangement, assurance⟩, not of the task alone — the
> portion of determination an arrangement cannot discharge through its prior commitments or adequate
> direct verification at the declared assurance level moves when any coordinate of the relation
> moves.** [DDD-floor-02, projected]

This is §1's tuple applied to the hardest question the framework asks. What cannot be reduced is
not a residue sitting inside the task, waiting to be discovered by a sufficiently capable actor. It
is what *this* arrangement, with *this* ground, against *this* acceptance relation, at *this*
tolerance and assurance level, cannot discharge mechanically.

### 6.1 The floor lives in the predicate

> **… The intrinsic floor is a property of the acceptance predicate, not of the decision.**
> [term:floor, settled — closing clause; the canonical text opens with the floor's definition]

Where the predicate does not close, verification is structurally unavailable, and the demand falls
to whoever is present. That is the mechanism, and it is why the floor is not a statement about
difficulty. A task can be enormously difficult with a fully closing predicate — the search is
expensive and the check is cheap — and carry no floor at all (§5.3).

**Attribution.** The phenomenon this claim relocates — an irreducible residue in determination — is
Polanyi's and Collins's, and this paper cites them for the phenomenon only, taking no result from
either (Polanyi 1966; Collins 2010). What is the framework's, and not theirs, is the residue's
*location*: in the checkability of the acceptance predicate, arrangement-indexed.

The measure's boundary coincides with the floor's location: **the measure exists if and only if the
acceptance predicate operationally closes, and `H(V)` is undefined exactly where the framework
locates non-zero floor** [DDD-measure-06, **established**].

**That coincidence is worth noticing and it is not evidence.** The two arguments share a premise —
the closure of the acceptance predicate — so their agreement about where the line falls is close to
definitional on the measure's side. What is not definitional is that the line was drawn twice, from
different materials, with neither drawing fitted to the other. That makes the boundary principled
rather than arbitrary. It does not make the identification true, and this paper does not argue that
it does (measure note §8.2).

### 6.2 The capacity mechanism, and its scope

A second and narrower result describes one *generator* of floor rather than the floor itself.

> **H(V|X) bundles judged and escaped demand; cleaving them requires an actor-capacity model, and
> residual demand an actor has taken up escapes where it exceeds effective capacity `min(C_hold,
> C_resolve)` AND the shed decisions carry no verifier — overflow ∩ open is the mechanism of
> capacity-generated escape, sufficient for escape and not necessary for it, with overflow alone
> producing retries, not escape.** [DDD-floor-01, **reported**]

The condition has two limbs and both are necessary: **overflow** — demand exceeding resolve
capacity — and **open** — no verifier the actor holds [term:escape-mechanism, settled]. Overflow
alone, on a closing predicate, produces **retries, not escape**; it is recoverable and it is not
floor. Open alone, within capacity, is **carried by judgment** where an accountable supplier is
named, and that too is not floor. Only overflow **and** open together produce escape by this route.

**The scope correction matters and the paper carries it.** This mechanism is **sufficient for
escape and never necessary for it**. A governing decision that never entered any actor's residual
escapes without overflowing anything, because escape is supplied-by-nobody for any reason, and
capacity shortfall is one generator among others [DDD-dec-15]. Both `DDD-floor-01` and
[term:escape-mechanism] had a universal quantifier superseded to say so, and restoring it would
reintroduce the error the correction removed.

### 6.3 Reading the classical accounts through the index

**(analysis)** Brooks's essential complexity, read through [DDD-floor-02], is not a property of the
problem but of the problem-against-an-arrangement — which is why essential complexity is observed to
move when tooling, ground access or acceptance criteria change. That single relocation is what the
index buys, and §11 places the other classical accounts against it.

---

## 7. Accountability completeness

An arrangement can produce resolutions it cannot answer for. The framework treats that as a
structural property rather than a moral one, and it locates the property in a relation:

> **Accountability is a relation (attribution, persistent principal, authority linkage, stake,
> sanction path), not an intrinsic capacity; an arrangement naming an executor but no principal is
> incomplete.** [DDD-frame-08, projected]

The framework separates four terms that ordinary usage runs together. **Attribution** is the
determination of who acted [term:attribution, settled]. **Answerability** is the standing obligation
to explain [term:answerability, settled]. **Liability** is exposure to consequence [term:liability,
settled]. **Accountability** is the relation that requires all of them together with a persistent
principal, authority linkage and a sanction path [term:accountability, settled].

### 7.1 Executor and principal

The executor produces the resolution. The principal answers for it. These are routinely the same
party and are never the same *role*, and an arrangement is accountability-incomplete exactly when
it names the first and not the second.

**(analysis)** This is where the framework's refusal to treat accountability as an actor property
does work. A capable executor with no persistent identity, no authority linkage and no sanction
path is not partially accountable; the relation is simply absent, and no increase in the executor's
capability supplies it. Conversely an arrangement with a named principal, records, review, appeal
and insurance is accountability-complete whether the immediate executor is a person, a program or a
model, because the relation does not read the executor's kind.

### 7.2 What a ledger cannot supply

**(analysis)** Provenance records are necessary and not sufficient, and the gap is easy to
underestimate because records are the visible part.

A ledger supplies attribution: it can say what happened, when, and on whose credential. It can
supply the raw material for answerability, if someone is obliged to read it. It cannot supply
**authority linkage** — that the acting party was entitled to act — because entitlement is a fact
about the institution, not about the log. It cannot supply **stake**, because exposure to
consequence is an arrangement of interests. And it cannot supply a **sanction path**, because a
sanction requires a body able to impose one. An arrangement that responds to an accountability
question by improving its logging has answered a different question.

### 7.3 The prediction the relation generates

The framework's accountability material yields a testable prediction, carried in §9 with the rest
of the hypothesis set:

> **Trust and deployment willingness are better predicted by the completeness of the accountability
> arrangement — attribution, persistent principal, authority linkage, stake, sanction path — than
> by whether the immediate executor is human or computational.** [DDD-hyp-04, projected]

It is `projected`, its evidence field is empty, and the study that would fill it is unrun (§9).

---

## 8. Worked example: code generation

**(analysis)** One example, carried through every construct above. It is deliberately structural
rather than numerical: where a figure is wanted, this paper cites a computed one rather than
minting a new one, and where nothing computed exists, the figure is omitted rather than estimated.

**Task.** A service must gain an endpoint that accepts a customer address, validates it, normalises
it to a canonical form, and stores it. A model with repository access, a test suite, a type checker
and a human reviewer is available.

### 8.1 Ground and its provenance

The relevant ground is heterogeneous, and §2.4's provenance vocabulary sorts it. The repository's
conventions are **controlled**. Each country's address-format rules are **institutional**, supplied
by postal authorities rather than derived. The current schema is **observed**, and observed *from a
store*, so it is current only as of its last write. Whether a customer record is a business or a
residence is **inferred**. And whether downstream consumers depend on the existing un-normalised
form is, in most real repositories, **missing**.

The missing slot is not a defect in the taxonomy. It is the finding: an act whose acceptance depends
on ground the arrangement cannot reach has a floor, whatever the executor's capability (§6.1).

### 8.2 Commitments, by level

*Outcome-level:* the schema fixes field types and lengths, the linter fixes formatting — these
resolve their determinables directly. *Policy-level:* "new endpoints follow the existing controller
pattern" fixes the generating procedure without fixing the output, as does the coverage requirement.
*Principal-level:* "a reviewer with commit rights accepts the change" selects a determiner by
qualification and delegates the case-level resolution.

*Residual discretion* is what survives all three: which normalisation the canonical form uses, how
the endpoint behaves on a country the institutional ground does not cover, and whether the
un-normalised form is preserved. The model is deterministic given its inputs, and that changes
nothing about the size of that residual [term:residual-discretion].

### 8.3 Resolution source, per choice

| Choice | Discharge mode | Governed? |
|---|---|---|
| Field types | filed decision (schema) | yes |
| Controller structure | filed decision (policy, delivered by retrieval) | yes, **if delivered** |
| Canonical normalisation form | judgment (model, then reviewer) | yes |
| Behaviour on an uncovered country | **default** — whatever the library does | usually not |
| Preservation of the un-normalised form | **draw** — whichever the generated code happens to do | no |

The last two rows are the section's point. Both acts complete and both land outcomes in the world;
one is governed by an arrangement default nobody declared, and one is not governed at all. Under
[DDD-frame-15] both are discharged — demand is never unmet, only ungoverned — and under [term:store]
the last row's source is *nothing*, which is an escape. The second row carries the qualification: if
the model's context does not deliver that filed decision at the act, no source supplied it, and it
escapes too [DDD-delivery-02].

### 8.4 Closure, per predicate

Type-correctness is **verification-closed** and cheaply so: the checker runs, terminates, and
decides. Test-suite conformance is verification-closed relative to the tests, which is a
substantially weaker statement than conformance to intent. Canonical-form correctness is
**constructively closed** for the countries whose rules are encoded — the correct output is
computed by rule from institutional ground, and there is no search to price (§5.2). Behaviour on an
uncovered country is **open**: no procedure over accessible ground decides acceptability, and there
is nothing for `H(V)` to be about [DDD-measure-06].

Closure varies *within a single act*, per capability, which is precisely why required actor class is
computed per capability rather than per act [DDD-cost-12].

### 8.5 What the walk exposes, and what it predicts

Two escapes, both invisible to the arrangement's own instruments: the library default on uncovered
countries, and the un-normalised-form question that nothing in the arrangement asks. Both are
consequential, neither is governed, and the framework predicts that both surface as ungoverned
failure modes and as design-review findings [DDD-frame-04].

The remedy the framework recommends is not more capability. It is declaring the determinables — the
uncovered-country behaviour and the preservation question become decisions once the arrangement
names them, and a named decision can be filed, delivered and checked [DDD-ground-05,
DDD-ground-01].

### 8.6 A note on figures

Where a worked number is wanted for the conservation material, this paper cites the computed
date-validation task rather than computing a new one: total demand 25.493 bits, split 20.593 /
4.901 by one decomposition and 11.020 / 14.474 by another, both summing to the same total (measure
note §4; `core/09` §3, with the reproducing asset named there). No figure in this paper was
produced by this paper.

---

## 9. Predictions and study design

### 9.1 What these are, stated before they are stated

The five hypotheses below are **predictions, not findings**. Every one is `projected` in the claim
graph, every one carries a declared falsifier, **every one's evidence field is empty**, and every
one is owned by a study that has not been run. The emptiness is discipline, not oversight: the
framework files a hypothesis at the strength its falsifier gives it and does not backfill evidence
from the corpus that suggested it. Appendix A shows the status and the empty evidence column for
all six nodes so that no reader has to take this paragraph's word for it.

They replace binary human-versus-model predictions with graded predictions about **arrangements**
(§2.5). Each names a gradient, not a boundary.

The set is summarised by one umbrella claim: **operational evaluability, feedback density and
ground accessibility predict the comparative advantage of computationally assisted arrangements
over unaided situated judgment, after controlling for difficulty and resources** [DDD-frame-07,
projected].

### 9.2 The five hypotheses

**H1 — operational evaluability.** *Holding generation difficulty and resources constant,
comparative advantage shifts toward high-throughput computational generators as acceptance becomes
more operationally evaluable, feedback becomes faster and denser, ground becomes more accessible,
checking becomes cheaper, and retries become affordable.* [DDD-hyp-01, projected] The hypothesis
predicts a gradient of advantage, not a boundary, and the unit of comparison is the arrangement.

**H2 — ground and judgment dependence.** *Human or institutionally situated arrangements retain
greater comparative advantage as relevant ground becomes unavailable to the computational system,
consequences are delayed, evaluators disagree, acceptance criteria drift over time, tacit or
socially distributed knowledge is required, and normative legitimacy is part of the task.*
[DDD-hyp-02, projected] It names the situated-advantage variables. It does **not** claim a situated
arrangement can necessarily find a correct answer; some tasks are under-specified, contested or
unknowable rather than judgment-dependent [DDD-hyp-02, region].

**H3 — generator/checker composition.** *A generator-plus-checker arrangement outperforms both
generator-alone and judgment-alone baselines where candidate generation benefits from breadth or
speed, significant parts of acceptance are operationally closed, and the remaining open residue can
be escalated.* [DDD-hyp-03, projected] Outside that three-condition region the hypothesis predicts
nothing, and says so.

**H4 — accountability completeness.** *Trust and deployment willingness are better predicted by the
completeness of the accountability arrangement than by whether the immediate executor is human or
computational.* [DDD-hyp-04, projected] The comparison holds claimant-identity persistence constant
across executor kinds.

**H5 — selection versus training.** *Reliance on worker or provider selection increases as
result-level evaluation becomes slower, less objective, less stationary and less complete, holding
labour supply, training cost, consequence severity and task structure constant.* [DDD-hyp-05,
projected]

### 9.3 H5's mechanism, and one thing it does not soften

H5's gradient reads the framework's training condition as a quality gradient over the error signal
the condition requires. The condition itself is settled and this paper carries it in its settled
form:

> **Closure decides whether training is *available*. Cost decides the *ratio* when it is.** Training
> requires a **reliable error signal** — you must be able to tell, and tell soon, whether the output
> was right. [term:training, settled]

Evaluation speed, objectivity, stationarity and completeness are the quality dimensions of that
signal, which is why H5's gradient and the settled condition are compatible rather than competing.
Separately, what training buys is bounded: it changes *allocation*, not capacity [DDD-cost-20],
which is why selection does not vanish even where training is available.

**A softer reading is available in this paper's source material and is deliberately not carried.**
Whether "closure decides availability" should become a gradient rather than a gate is a supersession
question against a settled term. It is queued in the framework's successor list, it is not this
paper's to take, and the paper states [term:training] as settled canon states it.

### 9.4 H5's validity qualification

Selection reaches open-predicate carriage only through records attached to claimant identities that
outlive their verdict horizons. An answer-keyed qualification instrument — an examination, an eval —
evidences demonstrated class on predicates that **close**, and its verdict cannot evidence
open-predicate carriage [DDD-cost-13, projected]. Provider selection across model-version
succession is therefore partial at best and per-capability, and H5's gradient must be read with
identity persistence held constant [DDD-hyp-05, notes].

### 9.5 Study design

**(analysis)** The design below is the paper's proposal; the preregistration artefact belongs to
the study that owns the hypothesis set, and is referenced here rather than asserted.

*Unit of analysis.* The arrangement-task pair, never the actor. An arrangement is specified by its
executor, its commitments by level, its ground channels, its verification mechanisms, its reviewers
and its accountable principal (§2.5).

*Independent variables.* Operational evaluability of the acceptance predicate; feedback latency and
density; ground accessibility; retry cost; and accountability completeness, coded against
[DDD-frame-08]'s five elements.

*Dependent variables.* Acceptance rate at declared tolerance; time and cost to acceptance; escaped-
decision count found by structured design review [DDD-frame-04]; and, for H4, elicited deployment
willingness.

*Falsifiers.* Each hypothesis carries one in the graph, and they are not decorative. H1 fails if
comparative advantage does not track evaluability at matched difficulty and resources. H3 fails if
composition does not beat both baselines inside its declared region. H5 fails if selection reliance
does not track evaluation speed, objectivity, stationarity and completeness at matched labour
supply, training cost, consequence and task structure [DDD-hyp-05, falsifier].

*What would make this paper wrong.* Not a single failed condition — these are graded predictions —
but a pattern in which arrangement-level variables carry no more predictive weight than executor
kind. That is a result the design can produce, and the framework would owe the retirement.

---

## 10. Limits and boundary cases

### 10.1 Two claims this framework retired

The framework has killed two of its own claims on the record, and both are retained in the graph
with the correction that killed them. IDs are never reused and retired claims are never deleted.

> **RETIRED — "closed predicates make intelligence unnecessary."** Does not follow from
> producer-independence under verification; generation may still require whatever capability the
> search demands. [DDD-frame-09, **retired**]

What survives is the scoped result of §5.4: producer identity is not necessary *for the checked
property and nothing more* [DDD-frame-05]. The retirement is the difference between those two
statements, and the difference is the whole of §5.3.

> **RETIRED — "a better decomposition destroys demand."** Cheaper parts were purchased by a
> higher-information seam; the destruction was an artifact of not counting `I(V;S)`.
> [DDD-measure-08, **retired**]

This one was retired by a computation, not by an argument: the worked task of §8.6 shows the
"destroyed" demand sitting in the seam, to the bit.

**(analysis)** A statement paper that shows its own retirements is making a methodological claim,
and the claim is checkable: the corrections are attached to the killed nodes, the survivors are
scoped in the graph rather than in prose, and a reader can verify both without this paper's help.

### 10.2 Where the framework's own instruments stop

*The measure's admissibility condition.* The engineering reading of the chain-rule identity holds
only for **admissible** conditioning variables — computable from ground available at the act
[DDD-measure-15, projected]. A conditioning variable that already knows the verdict produces an
arithmetically valid split with no engineering meaning, and the condition is what excludes it.

*The escape mechanism's scope.* Overflow ∩ open is sufficient for escape and never necessary for
it (§6.2) [DDD-dec-15].

*The measure's silence.* Off the closing region the measure does not exist, and its absence licenses
no claim about governance, which is well-formed there [DDD-frame-11].

### 10.3 Boundary cases

**(analysis)** *Learned and adaptive systems.* Randomisation is not discretion (§3.2): an adaptive
program whose adaptation rule is declared and bounded is policy-level committed, while one whose
adaptation is unbounded carries the discretion that bound would have removed. A system that learns a
rule and then applies it deterministically has moved demand from occasioned to standing supply
[DDD-frame-16], and that the rule was learned rather than authored changes nothing in the
accounting.

*Hybrid arrangements.* The ordinary case, and the reason the arrangement is the unit (§2.5): a
hybrid is not a fraction of a person plus a fraction of a model, but an arrangement with its own
commitments, checks and principal.

*Distributed actors.* The composite and ensemble vocabulary handles these (§2.1), with one caution:
a composite carries the demand of its parts **plus** the seam demand created between them
[term:seam, settled].

*Incomplete and gameable predicates.* Normative closure can fail while operational closure holds
(§5.1), and a predicate optimised against has had its acceptance region searched adversarially.

*Long-running agents.* An arrangement whose ground decays over its own run instances the escape
account directly: context decay removes filed claim nodes from the agent's ground, so later actions
become decisions with no link back to the declared claims — escape by delivery failure, at scale
[DDD-agent-01, projected; DDD-delivery-02].


---

## 11. Related work

Each neighbourhood below is taken in turn, and each entry closes on what this paper takes from it
and what it does not.

**The determinable literature.** The determinable/determinate relation is W. E. Johnson's (*Logic*
Part I, ch. XI, 1921), developed by Prior (*Mind* 58, 1949, in two parts) and Funkhouser (*The
Logical Structure of Kinds*, OUP, 2014), and surveyed by Wilson (*SEP*, rev. 2023). Four structural
gifts are taken directly: that the relation is not genus-and-species; that determinates under one
determinable are constitutively exclusive; that determinateness comes in orders; and that the
determinable is a dimension of comparability. **What is the framework's, and not theirs**, is the
identification of the determinable as determination demand's object and of the verdict variable's
support as the determinate-space at the declared grain [DDD-frame-13, credits].

**Cybernetics and requisite variety.** Ashby supplies the move this paper generalises — describing
a regulator by what it must absorb rather than by what it is. What the framework adds is that the
absorbing arrangement is itself a variable, and that its coordinates can be enumerated (§1).

**Complexity allocation.** Brooks and Tesler ask where complexity resides and where it is moved.
The framework indexes both questions (§6.3) and, on the closing region, measures the second one
(§4.4). It does not claim their results as instances of its own.

**Formal verification and proof-carrying systems.** The producer-independence result (§5.4) is the
framework's statement of what a sound check buys, deliberately narrowed to the checked property.
The literature's own scope conditions — soundness, ground completeness, checker legitimacy — are
carried inside the claim rather than assumed away.

**Design by contract.** Meyer's preconditions, postconditions and invariants are outcome-level and
policy-level commitments written at an interface (§3.1). The framework contributes the level
vocabulary and the observation that contracts do not reach principal-level commitment at all.

**Mixed-initiative and human-in-the-loop systems.** This literature studies arrangements directly
and is the framework's closest empirical neighbour. What the framework adds is a vocabulary for
*why* a given mix works — which commitments attach where, which predicates close, who answers —
rather than a catalogue of mixes that do.

**Bounded rationality and principal–agent theory.** The accountability relation (§7) is adjacent to
principal–agent analysis and is not reducible to it: authority linkage and sanction path are
institutional facts, not incentive parameters, and an arrangement can be incentive-aligned and
accountability-incomplete.

**Algorithmic accountability and responsibility gaps.** The framework's contribution here is
[DDD-frame-08]'s structural reading: a responsibility gap is an arrangement naming an executor and
no principal, which is a fixable property of the arrangement rather than a novel moral category.

**Information theory.** Shannon's entropy and chain rule are used exactly as stated, and the
theorem is Shannon's, always. The identification of determination demand with verdict entropy is
the framework's modelling claim, and it is the falsifiable part (§4.4) [DDD-measure-01].

### 11.1 A force the framework names and has not filed

**(analysis)** One piece of positioning belongs here because it names the force the whole framework
is about, and it is deliberately unfiled.

Arrangements are pulled by two different things, and conflating them explains a family of failures.
**World-pull** is the pull of the outcome the arrangement exists to produce: the address is correct,
the patient recovers, the bridge stands. **Ledger-pull** is the pull of the record by which the
arrangement is assessed: the test passes, the metric moves, the review is signed. The two coincide
exactly to the extent that the ledger's predicate captures the world's acceptance relation — which
is normative closure (§5.1), and which is never total.

Read this way, Goodhart's law is not a claim that measurement corrupts. It is **ledger-pull
mis-aimed**: an arrangement optimising against a predicate that was a proxy for the world's
acceptance relation and was mistaken for it. The framework's own vocabulary predicts where this
bites hardest — where operational closure is high and normative closure is low, so the ledger is
cheap to satisfy and does not represent what acceptance requires.

The obvious next step is an instrument that ranks predicates by the gap between the two pulls. That
instrument is **not filed**, and it is not filed for a stated reason: ranking requires a corpus this
framework does not yet have, and a ranking objective proposed without one would fix a scale before
anything could calibrate it. It is named here as an open direction and cited nowhere as canon.

---

## 12. Conclusion

Complexity does not arrive at an engineering arrangement already labelled essential or accidental.
A consequential choice becomes easy, hard, checkable, delegable or judgment-heavy only relative to
what the arrangement can observe, what commitments it already contains, what acceptance relation it
must satisfy, what tolerance it declares, and what assurance is required.

That is the missing parameter. It is not a new species name for the determiner. It is the
arrangement through which determination is produced and governed [DDD-frame-01].

Once the arrangement is explicit, several distinctions sharpen. A commitment may attach to an
outcome, a policy or a principal, and the three compose [DDD-frame-02]. A resolution's source is
not its assurance mechanism [DDD-frame-03]. A checker can remove the need to trust a producer for a
declared property without making the candidate cheap to generate or the predicate normatively
complete [DDD-frame-05, DDD-frame-06]. An executor can produce a resolution without being able to
answer for it [DDD-frame-08]. And a choice can escape: the arrangement produces an outcome that no
adequate commitment, check or accountable authorisation governs [term:escape].

The framework's compact statement of what makes that possible is the conjunction of two claims:

> **… demand is never unmet, only ungoverned.** [DDD-frame-15 — closing clause]

That sentence is canon's own, and the compact statement it belongs to is the **conjunction** of two
claims rather than either alone: every completed act's demand is discharged by one of four modes
[DDD-frame-15], and discharge is act-indexed, so governance never chooses whether demand is
supplied, only by what [DDD-frame-16].

And its strongest result is relational:

> **The judgment floor is relational: irreducibility is a property of the indexed relation ⟨task,
> ground, acceptance relation, tolerance, arrangement, assurance⟩, not of the task alone …**
> [DDD-floor-02 — opening clause; the claim continues, quoted in full at §6]

**What is established, and what is projected.** Established in the graph: that closure is distinct
from generation cost; that conservation on the closing region is the chain rule; that the measure
exists exactly where the acceptance predicate closes; that the parts of a decomposition become
trivial only when the decomposition already encodes the verdict. Projected, with falsifiers and
without evidence: the index itself, the commitment levels, the discharge chain, the relational
floor, the accountability relation, and every one of the five hypotheses. This paper states a
framework whose central claims are proposals, and the honest form of that statement is this
sentence rather than a hedge distributed through the argument.

The empirical question is not whether models replace people wherever a predicate closes. It is how
comparative advantage shifts as operational evaluability, generation cost, ground access, feedback
and accountability change. That question admits mixed arrangements, graded predictions and
falsification, and it matches engineering practice, where the practical winner is rarely an
isolated actor and usually a composition of commitments, generators, checks, reviewers and
principals.

Decision-Driven Design is the engineering corpus from which this program was abstracted. Its value
is not that it proves a universal conservation principle or an exact boundary between kinds of
determiner. Its value is that it makes consequential choices auditable: where they are resolved,
what they are resolved against, how they are checked, who answers for them, and which ones have
been left to accident.

---

## Reproduction

**This paper mints no figures and no assets.** Every number it states was produced by an existing
script in the principle repository and is cited to the projection that works it: the
date-validation totals of §4.4 and §8.6 come from `core/assets/measure-toy.py`, worked in the
companion measure note's §4 and in `core/09` §3. That script was re-run fresh while this paper was
drafted and reproduces the stated values.

Every block quotation attributed to a graph node was verified verbatim against the graph at the
pinned ref by `check-quotations.py`, alongside this file. Appendix A was generated from the graph by
`gen-appendix.py` and re-read against it by `check-appendix.py`. All three scripts live beside this
manuscript and take the ref as an argument, so the checks are reproducible against any ref rather
than against the one that happened to be current.

---

## References

Locators are marked **verified** where the source was checked directly, and **unverified** where it
could not be. One entry below is unverified, and the reason is stated in the entry rather than left
for a reader to discover.

Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall, London. Variety and the bit,
§7/7; the Law of Requisite Variety in logarithmic form, §11/7, with the general statement at §11/9.
*(verified)*

Brooks, F. P. (1987). No Silver Bullet: Essence and Accidents of Software Engineering. *IEEE
Computer* 20(4):10–19, April 1987, doi:10.1109/MC.1987.1663532; reprinted from *Proceedings of the
IFIP 10th World Computer Congress*, North-Holland, 1986. Both locators are given because both
circulate. *(verified)*

Collins, H. M. (2010). *Tacit and Explicit Knowledge*. University of Chicago Press, Chicago. ISBN
978-0-226-11380-7. The three-way taxonomy the framework respects — relational, somatic and
**collective** tacit knowledge — is the book's organising distinction. *(verified)*

Funkhouser, E. (2014). *The Logical Structure of Kinds*. Oxford University Press. ISBN
9780198713302. *(verified)*

Goodhart, C. A. E. (1975). Problems of Monetary Management: The U.K. Experience. In *Papers in
Monetary Economics*, Volume I. Reserve Bank of Australia, Sydney. Reprinted in *Monetary Theory and
Practice: The U.K. Experience*, Macmillan, 1984. *(verified)*

Johnson, W. E. (1921). *Logic*, Part I, chapter XI, "The Determinable". Cambridge University Press.
*(verified)*

Meyer, B. (1992). Applying "Design by Contract". *IEEE Computer* 25(10):40–51. *(verified)*

Polanyi, M. (1966). *The Tacit Dimension*. Doubleday & Company, Garden City, New York. Based on the
Terry Lectures delivered at Yale University in 1962. *(verified)*

Prior, A. N. (1949). Determinables, Determinates and Determinants. *Mind* 58(229):1–20 and
58(230):178–194, in two parts. *(verified)*

Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*
27(3):379–423 and 27(4):623–656. *(verified)*

Tesler, L. (ca. 1984). The Law of Conservation of Complexity. **(unverified — no primary
publication.)** The law is attributed to Tesler from his time at Xerox PARC and was communicated
through talks and interviews rather than a paper; the earliest substantial published discussion is
an interview with Tesler in Saffer, D. (2006), *Designing for Interaction*, New Riders. This paper
cites Tesler for the allocation question only, and takes no result from him.

Wilson, J. (2023). Determinables and Determinates. *Stanford Encyclopedia of Philosophy*, first
published 7 February 2017, substantive revision 18 January 2023. *(verified)*

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
| `DDD-delivery-01` | conceptual | projected | Filing is not encoding: a decision sits in I(V;X) only to the extent the arrangement delivers it at the act, so store allocation cannot be read off artefacts, and the paid-once-inherited-by-every-run property belongs to mechanical delivery specifically, not to standing supply generally. |
| `DDD-delivery-02` | conceptual | projected | Governance filed but not delivered is escape: no source supplied the governing decision at the act, so it was determined by nobody (term:escape, supply-general), and delivery failure is thereby a generator of escape — sufficient, never necessary — whose distinguishing feature is that the ledger shows coverage: escape that presents as governance. |
| `DDD-delivery-03` | conceptual | projected | An unretrieved decision and an unretrieved check over the same act are correlated failures — same actor, same budget, same position — so judgement-mediated delivery on both the source and assurance sides silently removes the independence a gate depends on: the failures compound rather than stack. |
| `DDD-floor-01` | formal | reported | H(V\|X) bundles judged and escaped demand; cleaving them requires an actor-capacity model, and residual demand an actor has taken up escapes where it exceeds effective capacity min(C_hold, C_resolve) AND the shed decisions carry no verifier — overflow ∩ open is the mechanism of capacity-generated escape, sufficient for escape and not necessary for it, with overflow alone producing retries, not escape. |
| `DDD-floor-02` | conceptual | projected | The judgment floor is relational: irreducibility is a property of the indexed relation ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩, not of the task alone — the portion of determination an arrangement cannot discharge through its prior commitments or adequate direct verification at the declared assurance level moves when any coordinate of the relation moves. |
| `DDD-frame-01` | conceptual | projected | Unresolved determination is indexed by the tuple ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩, not by the task alone. |
| `DDD-frame-02` | conceptual | projected | Behavioural commitments attach at three levels — outcome, policy, principal — which compose and are not actor species; residual discretion is the outcome-relevant variation that remains after the arrangement's declared commitments are applied. |
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
| `DDD-frame-15` | conceptual | projected | At every completed act in a task's scope, the act's determination demand is discharged — by a filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw; escape is a supply mode of discharge, not an absence of supply — demand is never unmet, only ungoverned. |
| `DDD-frame-16` | conceptual | projected | Discharge is act-indexed: standing supply is inherited per act and occasioned supply is produced per act, so there is no act-free discharge — governance never chooses whether demand is supplied, only by what, chosen in advance or defaulted at the act. |
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
| `DDD-measure-06` | formal | established | The measure exists iff the acceptance predicate operationally closes; H(V) is undefined exactly where the framework's floor result locates non-zero floor. |
| `DDD-measure-08` | formal | retired | RETIRED — "a better decomposition destroys demand." Cheaper parts were purchased by a higher-information seam; the destruction was an artifact of not counting I(V;S). |
| `DDD-measure-10` | formal | established | You cannot decompose your way out of the work: for a fixed closing task, H(V\|S) = 0 requires I(V;S) = H(V) — the parts become trivial only when the decomposition already encodes the entire verdict. Demand is conserved, not escapable by re-decomposition. |
| `DDD-measure-11` | conceptual | reported | The measure prices the verdict, not the search: H(verdict) is a property of the verdict function and the ground distribution and says nothing about the cost of computing a correct answer. Two tasks with identical verdict entropy can differ unboundedly in generation cost, so the measure must not be read as pricing generation. |
| `DDD-measure-15` | conceptual | projected | The engineering reading of the chain-rule identification holds only for admissible conditioning variables. A conditioning variable X is admissible where it is computable from ground available at the act and from what the arrangement has standing before it, and not from the verdict itself — computable by something that has not been handed the answer. The arithmetic holds for any X whatever; admissibility is what restricts the reading, not the identity. |

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
| `term:composite-actor` | composite-actor | **A composite actor carries its members' demand, plus the seam demand between them.** |
| `term:conservation` | conservation | **For a task at a declared assurance level, and within a fixed decomposition of that task, determination demand is conserved.** Every governing decision gets made. The only choice is **by whom, when, and at what price.** Reduce the demand in one store and it **relocates**; it does not vanish. |
| `term:determinable` | determinable | The **determinable** — an outcome-relevant dimension of variation at the declared tolerance: the object determination resolves, and the dimension of comparability an axis names. Determinateness comes in orders — red → scarlet → this shade — and the declared tolerance names the order at which the framework stops distinguishing. |
| `term:determinate` | determinate | The **determinate** — one specific way of occupying a determinable: what discharge produces. A determinate is a way of being, not the determinable plus a differentia, and determinates under one determinable are constitutively exclusive at their grain. |
| `term:ensemble-actor` | ensemble-actor | **The choice is a property of the ensemble, and it exists nowhere in any member.** |
| `term:escape` | escape | **Escaped** — determined *never*, by nobody: decided-by-nobody as a first-class category. Latent defect exposure. **The only forbidden state.** |
| `term:escape-mechanism` | escape-mechanism | **Capacity-generated escape — the escape an actor produces from residual it has taken up — requires two conditions, both necessary:** **(1) Overflow** — demand exceeds resolve capacity. **(2) Open** — no verifier the actor holds. Overflow alone (closing predicate) → **retries, not escape.** Recoverable. Not floor. Open alone (within capacity) → **carried by judgment**, where an accountable supplier is named. Not floor. Where none is named, it is escape by another route (`05` §7) — outside this mechanism, not excluded by it. **Overflow AND open** → **escape. This is the floor.** **Sufficient for escape, never necessary.** A governing decision that never entered an actor's residual escapes without overflowing anything: escape is supplied-by-nobody (`term:escape`), and capacity shortfall is one generator of it. |
| `term:floor` | floor | The "floor" is the portion of a determination's demand that **cannot be moved off the in-the-moment actor** — the residue that no amount of encoding or checking can amortise, that must be paid, per run, in judgment. **The intrinsic floor is a property of the acceptance predicate, not of the decision.** |
| `term:liability` | liability | **Liability** — bearing the consequence. |
| `term:outcome` | outcome | The **outcome** — the determinate as it lands in the world, produced at every completed act. The **verdict** is the same determinate as assessed by a declared predicate, produced only where governance has declared one. The world renders outcomes, never verdicts; governance is the conversion of outcomes into verdicts. |
| `term:residual-discretion` | residual-discretion | **Residual discretion** is the outcome-relevant variation remaining at the act after the arrangement's declared commitments are applied. It is not randomness: a deterministic arrangement can carry substantial discretion across unfamiliar cases, a randomised one can be tightly committed, and a zero-variance arrangement can be consistently wrong. |
| `term:seam` | seam | A composite carries the demand of its parts, **plus** the seam demand `S` created *between* them. |
| `term:store` | store | **{rule, check, actor, nothing}.** There is no fifth source. |
| `term:swarm-gate` | swarm-gate | **A swarm is an actor only if it genuinely determines choices against ground.** The admission tests (`00` §4) still gate, and they must. |
| `term:training` | training | **Closure decides whether training is *available*. Cost decides the *ratio* when it is.** Training requires a **reliable error signal** — you must be able to tell, and tell soon, whether the output was right. |
| `term:verdict` | verdict | **Definition (determination demand).** *(In the engineering projection this same quantity is denominated in the vocabulary of the domain and called* **specification demand** *; the measure below is identical either way.)* For a task whose acceptance predicate **closes** for the arrangement (`term:closure`; *decidable* is the formal special case, not the requirement), the predicate evaluates outcomes, and the **task class** supplies one correct output per input point. The **verdict** is that induced assignment — the correct output over each point of the input space. Let `P` be the distribution over inputs (the *ground distribution*). The **determination demand** of the task is the Shannon entropy of the verdict: **D = H(verdict)**, measured in **bits**. Where the task class supplies no such assignment, the predicate still evaluates outcomes and there is no verdict to have entropy about — which is the boundary `09` §7 draws. |

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

*Generated from the graph at `v5.9.0`. 45 claims, 3 decisions, 24 terms.*
