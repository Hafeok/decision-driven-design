# Specification Demand Is Verdict Entropy

### Conservation as the Chain Rule

*Emil — Context&. Formal note.*

*This note is a projection of `actor-indexed-determination` at `v5.3.0` and `decision-driven-design`
at `v0.4.0`; bracketed claim identifiers resolve against these refs.*

---

## Abstract

A companion argument holds that the demand for determination in a task is conserved: every governing
decision gets made, and design choices relocate the demand between stores rather than removing it. That
argument has carried a standing debt. Without a counting procedure shown invariant across two
architectures of one task, conservation is an accounting discipline rather than a measured quantity.

This note pays the debt on a bounded region. For a task whose acceptance predicate closes, we identify
specification demand with the Shannon entropy of the **verdict** — the correct output the predicate
assigns over the distribution of ground the task faces. Conservation is then the chain rule of entropy:
conditioning on any variable `X` splits the total into what `X` encoded, `I(V;X)`, and what remains,
`H(V|X)`. Three claims previously stated separately — seam demand under decomposition, store allocation
across actors, and the encode/verify split in retrieval-augmented generation — are this one identity
under three choices of `X`. Two further instances — the identity iterated across a two-level
decomposition, and a ground-distribution sweep — extend the worked coverage without adding a fourth
claim.

**The theorem is Shannon's.** What is claimed here is the identification, which is a modelling claim and
is falsifiable in a way arithmetic is not. We are explicit about what our computations do and do not
establish: they show the identification is computable and non-degenerate, not that it is true. The
correspondence that would make it a measured result — that `I(V;S)` predicts the engineering cost of an
interface — is stated as a protocol and not run.

The measure has a sharp boundary. Entropy of a verdict requires a verdict function, and an open
acceptance predicate is one that lacks it. So the measure exists exactly where the predicate closes and
vanishes exactly at the floor. We argue this coincidence is the strongest evidence the identification is
the right one.

---

## 1. Why demand resisted counting

The obvious way to measure demand is to count decisions. It fails, and the way it fails points at the
right answer.

Counting is representation-dependent. One architectural decision, ten component decisions, and a
thousand control-flow decisions may describe the same task at different resolutions, and nothing in the
count says which resolution is correct. Worse, the count is not stable under the operations the
framework most wants to reason about. **Decomposition creates decisions.** Split a task in two and an
interface now exists that did not exist before, carrying decisions nobody had to make in the monolith.
A quantity that grows when you cut the task cannot be the conserved one.

The deeper failure is that cardinality is the wrong kind of quantity. A decision that discriminates
between two thousand cases carries more demand than one that discriminates between two, and counting
treats them alike. Demand is extensive; a count is not.

So demand is not a count. It is a measure, and it needs a unit.

Ashby had one. Requisite variety is stated in bits, and the framework's central claim — that a fixed
quantity of determination must be supplied from somewhere — is Ashby's shape without Ashby's unit. This
note supplies it for the region where it exists.

---

## 2. The definition

> **Definition.** For a task with an acceptance predicate that closes, let the **verdict** `V` be the
> correct output the predicate assigns to each point of the input space, and let `P` be the distribution
> over inputs the task actually faces — the **ground distribution**. The **specification demand** of the
> task is the Shannon entropy of the verdict:
>
> **`D = H(V)`**, in bits.

Demand is the information required to specify the correct answer over the ground the task faces. Not how
many decisions — **how much distinction**.

Three properties follow immediately, and each answers something the counting approach could not.

**It is representation-independent.** `H(V)` is a property of the verdict function and the ground
distribution. Describing the task at a different granularity does not change it.

**It never mentions the actor.** This is the exact form of the framework's claim that demand is fixed by
the task and never by the system. Whatever resolves the task faces the same `H(V)`.

**It is deployment-relative, which is a correction rather than a concession.** `H(V)` depends on `P`. The
same validator faces different demand in an environment where inputs are nearly always valid than in one
where they are adversarial. That is an added parameter and it is the honest one: *fixed by the task* is
properly *fixed by the task, the tolerance, and the ground distribution*.

---

## 3. Conservation is the chain rule

Let `X` be any variable the verdict can be conditioned on. The chain rule of entropy gives, with no
approximation:

> **`H(V) = I(V;X) + H(V|X)`**
>
> total demand = what `X` encoded + what remains to resolve given `X`

That is the whole formal content of this note. Everything below is a choice of `X`.

Read through the framework's vocabulary, the terms map exactly:

| Information quantity | Framework quantity |
|---|---|
| `H(V)` | total specification demand, fixed by the task |
| `I(V;X)` | demand **encoded** by `X` — paid once, inherited by every run |
| `H(V|X)` | demand **remaining** — what must still be resolved at run time |

**Conservation within a fixed structure is now forced rather than asserted.** Fix `X`, and
`I(V;X) + H(V|X)` cannot fail to equal `H(V)`. Moving work between what the structure encodes and what
the parts must resolve is a zero-sum transfer, exactly.

We are aware of how this reads, and §6 says it plainly: the fact that an identity holds is not evidence
for anything. The content of this note is the identification in §2, not the arithmetic in §3.

---

## 4. Worked example, and the correction it forced

Take a task small enough to compute exhaustively: validate a two-field date `(M, D)` with
`M ∈ {1,2,3,4}` and `D ∈ {1,…,31}`, inputs uniform. The verdict is `VALID ⟺ D ≤ days(M)`, with
`days = {Jan 31, Feb 28, Mar 31, Apr 30}`. There are `n = 124` points, of which 120 are valid.

Total demand: `H(V)·n = 25.493` bits.

Now take two decompositions — two ways of splitting the task so that sub-tasks are handled separately.

| Decomposition `S` | groups | parts `H(V\|S)·n` | seam `I(V;S)·n` | sum |
|---|---|---|---|---|
| **A** — split by month | 4 | 20.593 | 4.901 | **25.493** |
| **B** — split by day, `≤28` vs `≥29` | 2 | 11.020 | 14.474 | **25.493** |

Here `I(V;S)` is **seam demand**: what the decomposition itself absorbed. The framework had previously
asserted a seam identity, `|D_comp| = |D_single| + |S|`. It is not an assertion. It is the chain rule,
with the seam identified as the mutual information between the decomposition and the answer.

**What this computation corrected.** Decomposition B's parts are dramatically cheaper than A's — 11.0
bits against 20.6. The framework's earlier language called this *a better decomposition destroying
demand*, and treated it as the strongest counterexample to conservation.

It is not destruction. B moved more demand into the seam, from 4.9 bits to 14.5. B's split already knows
where the valid/invalid boundary lives — at day 29 — and that knowledge is not free. It is mutual
information, pre-paid into the structure.

> **A better decomposition pre-pays more demand into the seam, buying cheaper parts. The total is
> invariant.** The destruction was always an artifact of not counting the seam.

This is worth dwelling on because it is the only place in the framework's history where a computation
overturned a stated position. The counterexample had been booked as unresolved for some time. It was not
a counterexample; it was a measurement error.

**Two predictions follow that are not postdictions.** Ranging over all decompositions of a fixed task:
`H(V|S)` is minimised exactly when `I(V;S)` is maximised, so **you cannot make the parts easier without a
higher-information seam** — a quantitative tradeoff curve for any concrete task. And `H(V|S) = 0`
requires `I(V;S) = H(V)`: the only way to make the parts trivial is to put the entire answer in the
decomposition. **You cannot decompose your way out of the work.**

---

## 5. One theorem, three conditioning variables

The seam result is one instance. Choosing `X` differently recovers claims the framework had stated
separately, with no new machinery.

### 5.1 `X` = an actor's encoding → store allocation

Let `E` be what an actor can encode before acting — its capacity to compute something about the input in
advance. Then `H(V) = I(V;E) + H(V|E)` reads as: total demand = encoded by this actor + left to this
actor's judgment.

On the same date task:

| Actor | encodes | `I(V;E)` | `H(V\|E)` | sum |
|---|---|---|---|---|
| **Program** | the exact verdict | 25.493 | 0.000 | **25.493** |
| **Weak model** | `D ≤ 28` | 14.474 | 11.020 | **25.493** |
| **Mid model** | `D ≤ 28`, plus whether the month is February | 20.964 | 4.529 | **25.493** |

**The total is actor-invariant; the allocation is actor-relative.** This distinction is the point, and it
rules out a tempting misreading. Demand is **not** constant *by* actor — that would mean each actor has
its own conserved quantity, which is difficulty under another name and says nothing. Demand is constant
*across* actors and allocated *by* actor. The same `H(V)` faces all three; the actor determines only how
it splits.

### 5.2 `X` = a retrieval policy → the encode/verify split

Retrieval-augmented generation is the same structure in deployment: retrieval converts ground into
encoded specification, leaving the model to carry the residual as judgment. With `A` the answer —
this task's verdict variable — and `R` the retrieval:

| retrieval (hit / distractor) | `I(A;R)` | `H(A\|R)` | sum |
|---|---|---|---|
| 0.00 / 0.00 | 0.000 | 2.609 | **2.609** |
| 0.30 / 0.20 | 0.458 | 2.154 | **2.612** |
| 0.50 / 0.30 | 0.791 | 1.812 | **2.602** |
| 0.70 / 0.20 | 1.365 | 1.251 | **2.616** |
| 0.90 / 0.05 | 2.136 | 0.474 | **2.610** |
| 1.00 / 0.00 | 2.612 | 0.000 | **2.612** |

Quantities estimated from 40,000 samples through a simulated retrieval process with imperfect hit rate
and plausible distractors. Better retrieval moves demand from judgment into encoded; distractors push it
back.

**What this instance is for, precisely.** It is not a measurement of conservation — §6. It shows the
identification survives an *estimated* channel rather than an exactly computed one, which is the
condition any deployed system presents. That is a claim about tractability, not about truth.

### 5.3 `X` applied twice → chained seams

Decompositions chain. Split the date task by month, and each month's sub-task can be split again by
day-band. Conditioning iterates, and the chain rule iterates with it, still without approximation
[DDD-measure-02]:

> **`H(V) = I(V;S₁) + I(V;S₂|S₁) + H(V|S₁,S₂)`**

The conditional term is an **internal seam**: the demand the second-level split absorbs, given what
the first level already absorbed [DDD-measure-03]. On the date task, chaining the two decompositions
of §4 — in both orders — gives:

| Chain | level-1 seam | internal seam | parts | sum |
|---|---|---|---|---|
| **month, then day-band** | `I(V;M)` = 4.901 | `I(V;D\|M)` = 17.838 | 2.755 | **25.493** |
| **day-band, then month** | `I(V;D)` = 14.474 | `I(V;M\|D)` = 8.265 | 2.755 | **25.493** |

Three things are exact here, and none is an assumption. The level-1 seams are §4's seams, unchanged —
the same split absorbs the same demand whether or not it is later refined. Both chains end at the
same parts residual, 2.755 bits: the order of the chain does not change what remains, only how the
seam divides between levels. And the two seam terms sum to the joint seam, 22.739 bits, in either
order. **Chaining re-splits the seam; it cannot create or destroy demand.**

This is the same iterated identity the framework's composition formalism names for a composed
arrangement's internal seams — there the conditioning variables are actor encodings rather than
sub-decompositions; the arithmetic is identical, the instance distinct, and the multi-actor case
remains unworked here [term:seam-identity]. Iteration is arithmetic — the theorem is still
Shannon's, applied twice. *A dedicated claim node for the iterated form is pending canon filing;
until it lands, the citation basis is the chain rule and the seam identification, as above.*

### 5.4 `P` varied → non-uniform ground

The worked example uses a uniform ground distribution. `P` is a parameter of the definition (§2),
not a convenience of the example, and the identity owes a demonstration under a skewed one
[DDD-measure-12]. Re-running the task under two skewed deployments — benign, where valid inputs
arrive nine times as often as invalid, and adversarial, the reverse — with both decompositions of §4:

| Deployment | `H(V)·n` | A parts | A seam | B parts | B seam |
|---|---|---|---|---|---|
| **benign** (valid 9× invalid) | **4.357** | 3.781 | 0.576 | 2.586 | 1.771 |
| **uniform** (the worked example) | **25.493** | 20.593 | 4.901 | 11.020 | 14.474 |
| **adversarial** (invalid 9× valid) | **96.639** | 67.867 | 28.772 | 23.924 | 72.716 |

Parts and seam sum to the row's whole, exactly, for both decompositions in every deployment. The
identity is indifferent to
the skew; the demand is not. The same validator, unchanged, faces roughly four times the uniform
demand when invalid inputs dominate and about a sixth of it when they are rare. Where the demand
sits moves too: the share decomposition B pre-pays into its seam is 41% of the whole on the benign
ground, 57% on the uniform, and 75% on the adversarial. A decomposition's seam economics are a
property of the task *and its deployment*. *Fixed by the task* is fixed by the task, the tolerance,
and the ground distribution — now worked, not merely stated.

### 5.5 What is unified

Three claims that read as independent — the seam identity, the actor-relative store allocation, and the
encode/verify split — are one identity under three choices of `X`. That a single conditioning argument
recovers all three, with no additional assumptions, is the note's main structural result.

The two further instances add no fourth claim. Chaining exercises the same identity iterated;
the skewed ground exercises it with `P` varied. What they add is coverage: the identity has now been
worked on five instances — the three conditioning variables, a two-level chain, and a
ground-distribution sweep across three deployments — on two tasks.

**One caveat carried forward, and it is where the next work is.** In all three, *escape* is folded into
`H(V|X)` together with *judgment*. The identity cleaves what was encoded from everything else; it does
not cleave what an actor resolves from what it sheds. Separating those requires a model of actor
**capacity** — the point at which `H(V|X)` exceeds what an actor can carry is where demand begins to
escape. The floor lives in that split, and it is not done here.

---

## 6. What the computations establish, and what they do not

An identity cannot be confirmed by computation, and this note's computations do not confirm one. It is
better to say so directly than to let a reader discover it.

`I(V;X) + H(V|X) = H(V)` holds for every joint distribution. Computing it on a date validator and
finding it holds establishes nothing about the framework. Estimating it from 40,000 samples and finding
it holds within a hundredth of a bit establishes that the estimator works. Neither is evidence that
specification demand *is* verdict entropy.

| What the computations do establish | What they do not |
|---|---|
| The identification is **computable** — the framework's quantities can be evaluated for concrete tasks rather than merely defined | That conservation is empirically true. The identity needs no testing |
| It is **non-degenerate** — values are non-trivial, neither zero nor everything, and they move as the framework says they should | That the identification is the *correct* one |
| The framework's qualitative claims appear with the **right signs and magnitudes** — a higher-information split really does buy cheaper parts; distractors really do push demand back to judgment | That information-theoretic demand predicts any **engineering** quantity |
| No contradiction appears across five worked instances on two tasks — three conditioning variables, an iterated chain, and a three-deployment ground sweep | Anything whatsoever about open predicates |

**So where does falsifiable content live?** In the identification, which is a modelling claim, and
modelling claims fail by failure of correspondence rather than by arithmetic. The correspondence that
matters:

> **`I(V;S)` should predict the engineering cost of an interface** — the specification effort it takes
> to agree the contract, the defect rate at the boundary, or the time to stabilise it. Likewise `I(V;E)`
> should predict which decisions an actor gets right unaided.

If a decomposition with high `I(V;S)` reliably has a *cheap* interface, or an actor with high `I(V;E)`
performs no better without help, then the identification is wrong — and Shannon is untouched, because
none of it was ever in question.

**That correspondence has not been tested here.** A protocol is straightforward: take a task with
several genuine decompositions in production, compute `I(V;S)` for each against the observed input
distribution, and correlate against interface specification effort and boundary defect density. It is a
different paper and it is the one that would make this a measured result rather than a well-founded one.

**What this note claims, then, is narrower than it first appears and firmer than an assertion.** A
measure exists, it is exact, it is computable, its boundary is principled, and it unifies three prior
claims. Whether it is the *right* measure of the thing engineers experience as specification burden is
open, stated, and testable.

A final consequence belongs in this section, because it governs how the note is to be used. **The
measure's job is to exist, not to be computed.** Its existence on the closing region is what makes
conservation a theorem rather than a maxim, and proxy pricing an approximation to something exact
rather than to nothing (§8). Practice runs count-free on the audit — where does each decision sit,
not how many bits does it carry — and proxy-priced on the optimisation, in money, hours, or tokens,
never on live entropy. Necessary for the warrant, unnecessary for the operation [DDD-frame-11].

---

## 7. Where the measure stops

`H(V)` requires a verdict function. An acceptance predicate that does not close is precisely one that
lacks a verdict function — there is no ground truth to have entropy about. So `H(V)` is undefined, and
the measure does not exist.

> **The measure exists if and only if the acceptance predicate closes. It vanishes exactly at the
> floor.**

*Closes* here means **operationally**: the acceptance procedure can be executed over available ground
within declared resource, latency, and confidence bounds. Formal decidability is the wrong criterion in
both directions — any bounded finite domain is decidable by lookup, and a decidable checker may require
infeasible resources.

**This coincidence is the note's strongest argument and it should not be read as a limitation.** The
companion framework locates the irreducible floor of a task in its acceptance predicate: the floor is
non-zero exactly where the predicate does not close, because verification is then structurally
unavailable and the demand falls to whoever is present. That result was derived independently, on
entirely different grounds, before this measure existed.

The measure goes silent in exactly that region.

A measure that stopped at an arbitrary boundary would invite suspicion that the boundary was chosen. This
one stops where an independently derived result says measurement must fail, and it stops there for the
same reason: no verdict function. **Measurement and closure have the same domain.** That two arguments
built from different materials draw the same line is the best available evidence that the identification
is tracking something real.

The consequence for the framework is a bounded claim, which is the correct kind. **Conservation of
specification demand is a theorem for closing predicates.** Off that region it remains what it was — an
accounting discipline, a principle rather than a measured invariant — and this note does not extend its
reach. It proves the part that was already inside the decidable region and marks the edge sharply.

---

## 8. Related work

Each neighbour below is taken in turn, and each entry closes on what this note takes from that
literature or concedes to it. The epistemics — what the computations establish, and where the
falsifiable content lives — are §6's, and are not reargued here.

**Shannon (1948).** The theorem is Shannon's, and so is every formal object in this note: entropy,
mutual information, and the chain rule that carries conservation are used exactly as 1948 states
them. What the note contributes is the identification alone — specification demand as verdict
entropy (§2) — and that is a modelling claim, with its failure mode stated in §6. Nothing here
strengthens, extends, or tests Shannon's result. The dependence runs one way: where the
identification fails, the theorem is untouched; where it holds, every formal property the note
uses is inherited, not proved.

**Ashby.** Requisite variety (1956) is the rigorous ancestor, and the nearest one. Ashby stated
the regulator's burden in bits — the unit this framework lacked, as §1 records — and the
framework's conservation claim is Ashby's shape: a fixed quantity of disturbance that must be met
with variety from somewhere (§1). This note is the framework arriving where Ashby already stood,
and it arrives on a restricted region: the measure exists exactly where the acceptance predicate
closes (§7). What is added to Ashby is therefore not a stronger claim but a narrower one — an
exact domain on which the variety accounting is a theorem rather than a maxim. Off that domain,
the note concedes Ashby's own caution: he had the unit in hand and still declined to claim more
than a principle, and this note does the same.

**Kolmogorov complexity and MDL.** The nearest objection arrives from here: why entropy rather
than description length? The framework's answer is that the two are not rivals — they price
different sides of the act. What must be resolved at the act, over the ground the act faces, is
occasioned, and entropy prices it; the mechanism built once, before any act, is standing, and
description length prices it [DDD-cost-01; DDD-cost-03]. On this reading MDL's two-part form,
`L(model) + L(data|model)`, is not a competing measure of demand. Read as per-act rates it is the
cost decomposition laid over the same conserved identity [DDD-cost-03], and over `N` acts it
becomes `L(mechanism) + N·H(V|E)`, with computable crossover volumes at which a distinction flips
from occasioned to standing [DDD-cost-07]. The identity itself forces this division of labour:
pricing the standing side in captured information, `I(V;E)`, is degenerate, because conservation
makes the tradeoff exactly flat — every distinction buys precisely what it costs, and no
distinction can be priced ahead of another — so a graded build-out over volume requires the
standing side priced as description length, which is not a conserved quantity
[DDD-cost-02; DDD-cost-06]. Where the framework has looked for this structure in production data,
the evidence is consistent with the two-part form but cannot yet select the MDL form, and is filed
as basis rather than confirmation [DDD-cost-03; mdl-cost-manufacturing-assessment-2026-08-08].
Within this note's own region a second, older
answer stands: entropy is relative to a declared ground distribution and computable from it
[DDD-measure-12], and Kolmogorov complexity is neither — which is what makes demand
deployment-relative. The note therefore concedes the standing side to description length entirely:
entropy cannot price the mechanism, and the cost layer built on this identity is MDL's.

**Information bottleneck.** Tishby, Pereira and Bialek's bottleneck (1999) is the closest formal
machinery: `I(V;X)` set against `H(V|X)` is structurally a bottleneck functional. The difference
is what is done with it. IB optimises: it seeks the representation that best trades compression
against relevance, under a tradeoff parameter. This note optimises nothing. The chain rule split
is an identity, and no optimisation appears anywhere in it (§3) [DDD-measure-02]; the measure
prices the verdict, not the search for it, and says nothing about what a good representation costs
to find [DDD-measure-11]. Where the framework does optimise — which distinctions to encode
standing, and at what volume — is the cost layer downstream of this note
[DDD-cost-06; DDD-cost-07], and that is where IB is genuinely adjacent. Same functional, different
question: IB asks which representation to keep; this note asks what any representation, kept for
whatever reason, must sum to. When the framework poses the keeping question, it is posed on IB's
ground.

**Rate–distortion.** The note's stated next result (§5.5, §9) is the split of `H(V|X)` into judged
and escaped demand, which requires a model of actor capacity — the bits an actor can supply per
act, with escape the residual exceeding them [DDD-cost-05]. Rate–distortion theory is the natural
home for that split: what a channel must lose when the required rate exceeds the available one is
rate–distortion's founding question. The note states the result and defers to it; nothing of its
content is anticipated here.

**Brooks.** Brooks drew the line between essential and accidental complexity, and held that the
essential part is fixed by the task, invariant to tooling. That line receives an exact form here:
`H(V)` never mentions the actor (§2). It also receives a correction, already carried in §2 and §9:
*fixed by the task* is properly *fixed by the task, the tolerance, and the ground distribution*.
The exchange is even. The note gives Brooks's line the unit it lacked, and accepts from the
identity the parameter Brooks did not have to name — the deployment the task actually faces. The
distinction is inherited, not replaced.

---

## 9. Caveats

**The theorem is Shannon's.** The chain rule is 1948. What is asserted here is the identification of
demand with verdict entropy, seam with mutual information, and decomposition with conditioning. That is
a modelling result and is never to be presented as a mathematical one.

**Demand is relative to the ground distribution.** The worked example uses a uniform `P`. Real
deployments do not, and the same task carries different demand under different input distributions. This
is no longer only stated: §5.4 works the sweep, and the demand moves while the identity holds. It
remains a genuine added parameter.

**Escape is not separated from judgment.** `H(V|X)` bundles both. The split requires an actor-capacity
model and is the natural next result.

**Five instances is credibility, not certification.** The identity is general because it is the chain
rule, and it has now been exercised on three conditioning variables, an iterated chain, and a
three-deployment ground sweep, across two tasks. Of the cases previously owed, chained seams and
non-uniform ground are worked (§5.3, §5.4); multi-actor composition remains. The framing should be
certified by an information theorist. The theorem is exact; identifying the right conditioning
variable for a deployed system is estimation, with error bars.

**The correspondence to engineering quantities is untested** — §6, and the most important of these.

---

## 10. The result in one line

> **For a task whose acceptance predicate closes, specification demand is the Shannon entropy of the
> verdict over the ground the task faces. Conditioning on any variable `X` splits it by the chain
> rule into what `X` encoded and what remains, which always sum to the whole. `X` a decomposition gives the seam; `X` an actor's encoding
> gives the store allocation, total actor-invariant and split actor-relative; `X` a retrieval policy
> gives the encode/verify split. Conservation of specification demand is the chain rule of entropy —
> where the predicate closes, and only there.**

---

## Reproduction

Five self-contained scripts regenerate every figure above: `measure-toy.py` for §4,
`measure-actor-allocation.py` for §5.1, `measure-rag.py` for §5.2, `measure-chained-seams.py` for
§5.3, and `measure-nonuniform-ground.py` for §5.4 — the last two in `assets/` beside this note. All
five were re-run against this draft and reproduce the stated values.
