# Determination Demand Is Verdict Entropy

### Conservation as the Chain Rule

*Emil — Context&. Formal note.*

*This note is a projection of `actor-indexed-determination` at `v5.3.0` and `decision-driven-design`
at `d8fd8e6`; bracketed claim identifiers and the assets named under Reproduction resolve against
these refs.*

---

## Abstract

A companion argument holds that the demand for determination in a task is conserved: every governing
decision gets made, and design choices relocate the demand between stores rather than removing it. That
argument has carried a standing debt. Without a counting procedure shown invariant across two
architectures of one task, conservation is an accounting discipline rather than a measured quantity.

This note pays the debt on a bounded region. For a task whose acceptance predicate closes, we identify
determination demand with the Shannon entropy of the **verdict** — the correct output the predicate
assigns over the distribution of ground the task faces. Conservation is then the chain rule of entropy:
conditioning on any variable `X` splits the total into the verdict information `X` carries, `I(V;X)`, and
what remains, `H(V|X)`. Three claims previously stated separately — seam demand under decomposition,
store allocation across actors, and the encode/verify split — are this one identity under three choices
of `X`. Two further instances — the identity iterated across a two-level
decomposition, and a ground-distribution sweep — extend the worked coverage without adding a fourth
claim.

**Demand is not cost.** Entropy prices what each act must resolve. Description length prices the
mechanism that supplies it. Two classifiers with identical demand can therefore differ without bound in
what supplying it costs, and the measure is silent on that difference by construction (§2.1).

**The theorem is Shannon's.** What is claimed here is the identification, which is a modelling claim and
is falsifiable in a way arithmetic is not. We are explicit about what our computations do and do not
establish: they show the identification is computable and non-degenerate, not that it is true. The
correspondence that would make it a measured result — that `I(V;S)` predicts the engineering cost of an
interface — is stated as a protocol and not run.

The measure has a sharp boundary, stated as a scope condition: the construction applies where the task
supplies an operationally usable verdict function and a ground distribution that can be estimated.
Outside that region the framework's independently derived floor becomes non-zero and the measure goes
silent, for the same reason in both cases. That coincidence is worth noticing. It is not evidence, and
the note does not use it as any.

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

So demand is not a count. It is a measure, and it needs a unit [DDD-measure-09].

Ashby had one. Requisite variety is stated in bits, and the framework's central claim — that a fixed
quantity of determination must be supplied from somewhere — is Ashby's shape without Ashby's unit. This
note supplies it for the region where it exists.

### 1.1 What demand is, independently of its measure

An identification is contestable only if the thing identified has a characterisation independent of the
thing it is identified with. Demand has one, and it is prior to this note.

The companion framework treats each **act** — the bounded episode of determination running from its
first governing decision to an expressed outcome — as governed by decisions that must each be supplied
from one of four sources: a **rule** that fixes the decision before the act, a **check** that applies a
criterion after it, an **actor** that resolves it during the act by reading ground, or nothing at all,
in which case the decision is **escaped** — determined never, by nobody [term:store; term:act;
term:escape]. There is no fifth source. **Demand is what must be supplied.**

This characterisation is count-free. It asks where each governing decision sits, not how much any of
them carries, and it is available whether or not the acceptance predicate closes [DDD-frame-11]. That is
what makes the identification below a claim rather than a definition: demand is specified here without
reference to entropy, and the proposal is that entropy measures it. What fixes the demand is the task,
the declared **tolerance**, and the distribution of ground the task faces; what resolves it is the
actor, and the measure never mentions one [term:tolerance; term:actor].

One distinction follows immediately and governs the rest of the note. Demand is what must be supplied;
it is not what supplying it costs. That distinction is §2.1's, and this note measures demand.

---

## 2. The definition

> **Definition (determination demand).** *(In the engineering projection this same quantity is
> denominated in the vocabulary of the domain and called* **specification demand** *; the measure below
> is identical either way.)* For a task with an acceptance predicate that closes, let the **verdict** `V`
> be the correct output the predicate assigns to each point of the input space, and let `P` be the
> distribution over inputs the task actually faces — the **ground distribution**. The **determination
> demand** of the task is the Shannon entropy of the verdict:
>
> **`D = H(V)`**, in bits.

[term:verdict] Demand is the information required to specify the correct answer over the ground the task
faces. Not how many decisions — **how much distinction**. And the correct *answer*, not the mapping from
inputs to answers: the mapping is a mechanism, mechanisms are priced by description length, and §2.1
separates the two. The definition's phrase *the correct output the predicate assigns* holds for some
task classes and not others; §2.2 says which, and what `V` is in the rest.

**Notation.** `H(·)` denotes Shannon entropy in bits, `H(V) = −Σᵥ P(v) log₂ P(v)`; `H(·|·)`
conditional entropy; `I(·;·)` mutual information. All are taken with respect to the ground
distribution `P`.

**Scale.** `D = H(V)` is demand per act: one input drawn from `P`, one verdict rendered. The worked
tables report `H(V)·n`, the demand of a single pass over an input space of `n` points, which keeps
the figures in whole bits; because `n` multiplies every term, the identity of §3 holds in either
scale.

Three properties follow immediately, and each answers something the counting approach could not.

**It is representation-independent.** `H(V)` is a property of the verdict function and the ground
distribution. Describing the task at a different granularity does not change it.

**It never mentions the actor.** This is the exact form of the framework's claim that demand is fixed by
the task and never by the system. Whatever resolves the task faces the same `H(V)`.

**It is deployment-relative, which is a correction rather than a concession.** `H(V)` depends on `P`. The
same validator faces different demand in an environment where inputs are nearly always valid than in one
where they are adversarial. That is an added parameter and it is the honest one: *fixed by the task* is
properly *fixed by the task, the tolerance, and the ground distribution*.

### 2.1 Demand is not cost

The definition invites one misreading above all others, and the framework's answer to it is prior to
this note. **Demand says what must be supplied; cost says what supplying it that way is worth**
[DDD-cost-01].

The two sides of the identity below denominate in the same unit — bits of one act's verdict — and differ
in **locus of supply**. What a mechanism fixes before any act is supplied by a *standing artifact*,
built once and present at each act. What is left is supplied by a *contemporaneous event*: an actor's
judgment, spent at the act and again at the next. A **cost register** prices that difference, and the
demand register cannot see it — **standing cost** for the price of building and holding the artifact,
**occasioned cost** for the price of the per-act event [term:cost-register; term:standing-cost;
term:occasioned-cost].

The two sides are not priced in the same currency, and the identity is why. Pricing the standing side by
what the mechanism captures — `I(V;E)`, for `E` the encoding a mechanism fixes before the act (§5.1) —
is degenerate: conservation forces `ΔI(V;E) = −ΔH(V|E)` exactly, so every distinction removes precisely
as many occasioned bits as it adds standing ones, and no distinction can be priced ahead of another
[DDD-cost-02]. Pricing distinctions apart therefore requires the standing
side priced as the **description length** of the mechanism, which is not a conserved quantity, with
entropy pricing only the occasioned side — MDL's `L(model)` and `L(data|model)`, read as per-act rates
[DDD-cost-03]. That correspondence is a modelling claim and is projected, not measured; §8 places it
against the literature.

**The consequence is a divergence, and it is worth stating as one.** Take two binary classifiers over
the same input space of `n` points, both returning `0` and `1` equally often under `P`. The first
returns the first input bit. The second reads an incompressible lookup table. Both face `H(V) = 1` bit
per act — that is arithmetic, and the measure cannot tell them apart. Their mechanisms differ by
everything: a sentence against `n` bits of table. **Same demand, standing costs differing by a factor of
`n`.** The measure is not failing here. It is measuring demand, and the two classifiers do not differ in
demand; they differ in the price of one way of supplying it, which is the other register's business.

A second divergence runs on a different axis and must not be fused with the first. Two tasks with
identical verdict entropy can differ unboundedly in the cost of *computing* an answer — a lookup table
and a satisfiability instance over the same input space carry the same `H(V)`, and one is answered by
indexing while the other is NP-hard to solve [DDD-measure-11; DDD-frame-06]. The measure prices the
verdict, not the search.

So the measure is silent on two things by construction: what a mechanism costs to describe, and what an
answer costs to compute. Both silences are stated in the framework's own canon rather than conceded
here, and neither is a defect in the identification. They are why demand needs a register of its own.

### 2.2 What `V` is, and for which tasks

An acceptance predicate evaluates an outcome: it settles whether a candidate is acceptable at the
declared tolerance [term:acceptance-predicate]. Written out, it is a relation `A(x, y) ∈ {0,1}` over an
input `x` and a candidate `y` — not, in general, a function from `x` to a unique `y`. Four task classes
follow, and `V` is a different object in each.

| Task class | What the predicate supplies | `V` for this construction |
|---|---|---|
| **Decision** — accept or reject an input | one bit per input | the accept/reject bit; `H(V) ≤ 1` per act |
| **Function** — one correct output per input | a unique `y` for each `x` | that output; the definition applies as written |
| **Relation** — several acceptable outputs per input | an acceptance set `{y : A(x,y)}` | not determined without a further choice |
| **Verification** — judge a candidate already in hand | one bit per pair `(x, y)` | the accept/reject bit, over the distribution of pairs |

**This note's worked instances are decision and function tasks.** The date validator of §4 is a decision
task, one bit per input. §5.2's simulation yields one answer per act, which is the function shape.
Nothing here is worked on a relation task.

**Relations have no verdict function, and the construction does not quietly supply one.** Where several
outputs are acceptable, `H(V)` is undefined until something selects among them — a tie-break, a
canonical form, or a declared distribution over the acceptance set — and each is a modelling choice
that changes the number. Declaring which is in force is part of declaring the task. Leaving it
undeclared and computing anyway is an error this construction will not detect.

**The entropy of a verification verdict is not the entropy of the generation task.** A verification
verdict is one bit; the answer it accepts may carry many, and the two must never be substituted for one
another. The framework separates them deliberately: closure is distinct from generation cost, and
verification being cheap implies nothing about the density or accessibility of the acceptance region
[DDD-frame-06]. The measure prices the verdict, not the search (§2.1) [DDD-measure-11].

---

## 3. Conservation is the chain rule

Let `X` be any variable the verdict can be conditioned on. The chain rule of entropy gives, with no
approximation:

> **`H(V) = I(V;X) + H(V|X)`**
>
> total demand = the verdict information `X` carries + what remains to resolve given `X`

That is the whole formal content of this note. Everything below is a choice of `X`.

Read through the framework's vocabulary, the terms map across. The left column is arithmetic; the right
column is the reading proposed in §2, and the two must not be confused:

| Information quantity (arithmetic) | Framework reading (under the identification) |
|---|---|
| `H(V)` | total determination demand, fixed by the task |
| `I(V;X)` | verdict information carried by `X` — **encoded demand** |
| `H(V\|X)` | verdict uncertainty remaining given `X` — **residual demand** |

**Conservation within a fixed structure is now forced rather than asserted.** Fix `X`, and
`I(V;X) + H(V|X)` cannot fail to equal `H(V)`. Moving work between what the structure encodes and what
the parts must resolve is a zero-sum transfer, exactly.

We are aware of how this reads, and §6 says it plainly: the fact that an identity holds is not evidence
for anything. The content of this note is the identification in §2, not the arithmetic in §3.

### 3.1 Which variables the reading applies to

The arithmetic above holds for any `X` whatever. The engineering reading does not, and the note owes a
condition saying which variables carry it.

Mutual information is symmetric and observational: `I(V;X) = I(X;V)`. It establishes that `X` and the
verdict are statistically dependent. On its own it does not establish that anyone constructed `X`, that
information flows causally from `X` to the verdict, that an engineering cost was paid, or that `X` is
even available when the act happens. Two of those the framework supplies elsewhere; two it does not
claim at all.

**Availability is supplied by a condition on `X`.** The encoded store is by definition what is fixed
*before* the act, by a rule [term:encoded; term:act]. Read as a restriction on conditioning variables:

> **Admissibility.** A conditioning variable `X` is **admissible** if it is a function of ground
> available at the act, and of what the arrangement has standing before it, and not of the verdict
> itself. It must be computable by something that has not been handed the answer.

**Cost is supplied by a different register**, and deliberately not by `I(V;X)`: what a mechanism costs
to build and hold is standing cost, priced by description length (§2.1). Whether `I(V;X)` predicts it
is the open correspondence of §6 [DDD-measure-07].

**Deliberate construction and causal flow are not claimed at all.** `I(V;X)` is verdict information
carried by `X`. Where this note calls that quantity *encoded* or *pre-paid*, the word is its name under
the identification of §2, never a property of mutual information.

The condition does real work. Choosing `X = V` gives `I(V;X) = H(V)` and `H(V|X) = 0` — the whole of
the demand in the conditioning variable, obtained tautologically. Without a restriction, §4's *you
cannot decompose your way out of the work* would be close to tautological with it. `X = V` is
inadmissible: the verdict is not ground available before the verdict.

What admissibility does **not** exclude is a mechanism that *computes* the verdict from ground. §5.1's
program does exactly that and reaches `H(V|E) = 0` legitimately. The difference is between building the
answer and being handed it. So §4's result survives with its content restored rather than lost: the
residual reaches zero only when some admissible mechanism determines the whole verdict, and §2.1 prices
what standing up that mechanism costs. The work is not escaped. It is relocated to the standing side
and paid there.

*A dedicated claim node for the admissibility condition is pending canon filing; until it lands, the
citation basis is the encoded store's definition and the act, as above.*

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

Both decompositions here are admissible (§3.1): each is a function of the input, computable before the
verdict is known. `I(V;S)` is the **verdict information carried by the decomposition**; under the
identification its name is **seam demand** [term:seam-information]. The framework had previously
asserted a seam identity, `|D_comp| = |D_single| + |S|` [term:seam-identity]. It is not an assertion. It
is the chain rule, with the seam identified as the mutual information between the decomposition and the
answer.

**What this computation corrected.** Decomposition B's parts are dramatically cheaper than A's — 11.0
bits against 20.6. The framework's earlier language called this *a better decomposition destroying
demand*, and treated it as the strongest counterexample to conservation.

It is not destruction. B moved more demand into the seam, from 4.9 bits to 14.5. B's split already knows
where the valid/invalid boundary lives — at day 29. That knowledge is verdict information carried by the
decomposition, and under the identification we call it demand pre-paid into the structure
[DDD-measure-03].

> **A better decomposition pre-pays more demand into the seam, buying cheaper parts. The total is
> invariant.** The destruction was always an artifact of not counting the seam.

**What that does not say.** A higher-information seam is not thereby a more expensive one. `I(V;S)`
is symmetric and observational (§3.1): it measures how much the split says about the answer, and
nothing about what discovering, agreeing, implementing, or maintaining the split costs. Those are
standing costs (§2.1). Whether the two track each other is the untested correspondence of §6
[DDD-measure-07], and it is where this reading would fail: a split with high `I(V;S)` may be obvious
and cheap, and if that is reliably so, the identification is wrong.

This is worth dwelling on because it is the only place in the framework's history where a computation
overturned a stated position. The counterexample had been booked as unresolved for some time. It was not
a counterexample; it was a measurement error.

**Two predictions follow that are not postdictions.** Ranging over all admissible decompositions of a
fixed task: `H(V|S)` is minimised exactly when `I(V;S)` is maximised, so **you cannot make the parts
easier without a higher-information seam** — a quantitative tradeoff curve for any concrete task. And
`H(V|S) = 0` requires `I(V;S) = H(V)`: the parts become trivial only when the decomposition determines
the entire verdict, which §2.1 prices and §3.1 shows is not an escape [DDD-measure-10]. **You cannot
decompose your way out of the work.**

---

## 5. One theorem, three conditioning variables

The seam result is one instance. Choosing `X` differently recovers claims the framework had stated
separately, with no new machinery.

### 5.1 `X` = an actor's encoding → store allocation

Let `E` be what an actor encodes before acting — what it has computed about the input in advance of the
verdict. `E` is admissible by construction (§3.1): it is fixed before the act. Then
`H(V) = I(V;E) + H(V|E)` reads as: total demand = carried by this actor's encoding + left to this actor
at the act.

On the same date task:

| Actor | encodes | `I(V;E)·n` | `H(V\|E)·n` | sum |
|---|---|---|---|---|
| **Program** | the exact verdict | 25.493 | 0.000 | **25.493** |
| **Weak model** | `D ≤ 28` | 14.474 | 11.020 | **25.493** |
| **Mid model** | `D ≤ 28`, plus whether the month is February | 20.964 | 4.529 | **25.493** |

**The total is actor-invariant; the allocation is actor-relative** [DDD-measure-04]. This distinction is
the point, and it
rules out a tempting misreading. Demand is **not** constant *by* actor — that would mean each actor has
its own conserved quantity, which is difficulty under another name and says nothing. Demand is constant
*across* actors and allocated *by* actor. The same `H(V)` faces all three; the actor determines only how
it splits.

The program's row is worth reading against §3.1. It reaches `H(V|E) = 0` by computing the verdict from
the input, which is admissible, and it pays for that in standing cost (§2.1). Zero residual is not
demand destroyed; it is demand supplied entirely by a mechanism.

**`H(V|E)` is the ideal-observer residual, not the actor's burden.** Conditional entropy assumes
something that can exploit every statistical relationship `E` carries. A real actor may fail to use
information that is present, and it then faces more than `H(V|E)`, never less. The gap is capacity, and
capacity sits outside the identity: the bits an actor can supply per act, with escape the residual
exceeding them, is a named next result and is not worked here [DDD-cost-05; DDD-floor-01]. So the
allocation above is the split an ideal user of `E` would face — a lower bound on what the actor must
resolve, not a measurement of what it will.

### 5.2 `X` = what is supplied before the act → the encode/verify split

Retrieval-augmented generation motivates this instance; it is not what is simulated, and the section is
named for what is. The structure is the framework's **encode/verify split** [term:encode-verify-split]:
part of what an act needs is supplied to it in advance, and the rest is left to whatever acts. As
conditioning that is the identity again, with `X` the material supplied before the answer — admissible
by construction (§3.1). With `A` the answer, this instance's verdict variable, and `R` what is supplied:

| retrieval (hit / distractor) | `I(A;R)` | `H(A\|R)` | sum |
|---|---|---|---|
| 0.00 / 0.00 | 0.000 | 2.609 | **2.609** |
| 0.30 / 0.20 | 0.458 | 2.154 | **2.612** |
| 0.50 / 0.30 | 0.791 | 1.812 | **2.602** |
| 0.70 / 0.20 | 1.365 | 1.251 | **2.616** |
| 0.90 / 0.05 | 2.136 | 0.474 | **2.610** |
| 1.00 / 0.00 | 2.612 | 0.000 | **2.612** |

Better supply moves demand from the residual into what `R` carries; distractors push it back.

**The generating model, in full.** It is stipulated rather than learned, and it contains neither
documents nor a model.

- `A` is drawn independently at each act from a fixed eight-outcome prior
  `w = (0.30, 0.22, 0.16, 0.12, 0.09, 0.06, 0.03, 0.02)`. Its population entropy is exactly
  `H(A) = 2.6126` bits.
- `R` is a single categorical symbol in `{0,…,7, NULL}`. It carries no document identity, no document
  content, and no hit flag.
- With probability `p_hit`, `R` is the answer. With probability `p_dist`, `R` is a **distractor**: an
  independent draw from the same prior `w`, so a plausible wrong answer rather than an arbitrary one.
  Otherwise `R` is `NULL`.
- **The supplying process therefore depends on the answer by construction**, maximally so on a hit.
  That is what makes this a simulated channel and not a measurement of a retrieval system
  [DDD-measure-05].
- Estimation is plug-in — entropies from empirical counts over 40,000 sampled acts per row, no bias
  correction.

**What the table tests, and what it cannot.** `I(A;R)` is computed as `H(A) − H(A|R)`, so the sum
column is exact by construction and tests nothing. Presenting it as a check would be the
arithmetic-as-evidence error §6 exists to prevent. What the run does test is whether a plug-in
estimator recovers the conditional entropy of a channel it is not given in closed form. It does:
against the analytic joint, the mean estimate over 200 replicates is within 0.002 bits at every
setting, and a single 40,000-sample run carries a standard deviation of 0.005 to 0.010 bits.

**Why the totals move.** Each row re-estimates `H(A)` from its own fresh sample, so the totals differ by
estimator noise and nothing else. Over 200 independent replicates at `N = 40,000`, plug-in `H(A)` has
mean 2.6117 bits, standard deviation 0.0049, and a central 95% range of `[2.601, 2.621]`, with a bias of
−0.0008. Every total in the table falls inside that range, and the population value they scatter about
is 2.6126.

**What this instance is for, precisely.** It is not a measurement of conservation — §6. It shows the
quantities are estimable from samples at a useful accuracy, which is the condition any deployed system
presents. That is a claim about tractability, not about truth. And `H(A|R)` remains the ideal-observer
residual, on the same reading as §5.1: something that cannot exploit everything `R` carries faces more
than the table shows, never less [DDD-cost-05].

### 5.3 `X` applied twice → chained seams

Decompositions chain. Split the date task by month, and each month's sub-task can be split again by
day-band. Conditioning iterates, and the chain rule iterates with it, still without approximation
[DDD-measure-02]:

> **`H(V) = I(V;S₁) + I(V;S₂|S₁) + H(V|S₁,S₂)`**

The conditional term is an **internal seam**: the demand the second-level split carries, given what
the first level already carries [DDD-measure-03]. On the date task, chaining the two decompositions
of §4 — in both orders — gives:

| Chain | level-1 seam `·n` | internal seam `·n` | parts `·n` | sum |
|---|---|---|---|---|
| **month, then day-band** | `I(V;M)` = 4.901 | `I(V;D\|M)` = 17.838 | 2.755 | **25.493** |
| **day-band, then month** | `I(V;D)` = 14.474 | `I(V;M\|D)` = 8.265 | 2.755 | **25.493** |

Three things are exact here, and none is an assumption. The level-1 seams are §4's seams, unchanged —
the same split carries the same demand whether or not it is later refined. Both chains end at the
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

| Deployment | `H(V)·n` | A parts `·n` | A seam `·n` | B parts `·n` | B seam `·n` |
|---|---|---|---|---|---|
| **benign** (valid 9× invalid) | **4.357** | 3.781 | 0.576 | 2.586 | 1.771 |
| **uniform** (the worked example) | **25.493** | 20.593 | 4.901 | 11.020 | 14.474 |
| **adversarial** (invalid 9× valid) | **96.639** | 67.867 | 28.772 | 23.924 | 72.716 |

Parts and seam sum to the row's whole, exactly, for both decompositions in every deployment. The
identity is indifferent to
the skew; the demand is not. The same validator, unchanged, faces roughly four times the uniform
demand when invalid inputs dominate and about a sixth of it when they are rare. Where the demand
sits moves too: the share decomposition B carries in its seam is 41% of the whole on the benign
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
`H(V|X)` together with *judgment*. The identity cleaves what `X` carries from everything else; it does
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
determination demand *is* verdict entropy.

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

**That correspondence has not been tested here, and a bare correlation would not test it.** Take a task
with several genuine decompositions in production and compute `I(V;S)` for each against the observed
input distribution. Three things must then be fixed in advance.

**The direction.** Across admissible decompositions of one task, higher `I(V;S)` predicts *higher*
interface specification effort, *higher* boundary defect density, and *longer* time to stabilise. The
prediction is monotone and it is the identification's, not a hedge. A reliable inverse association —
high-information seams that are cheap to agree and stable in production — falsifies the identification
and leaves Shannon untouched [DDD-measure-01; DDD-measure-07].

**The controls.** Interface size, domain complexity, team experience, coupling and change frequency,
tooling, decomposition discoverability, traffic volume, and organisational boundaries all move
interface cost independently of `I(V;S)`; a study that does not hold them is measuring the organisation
rather than the seam. Imbalance in the verdict distribution is the sharpest of them, and structural
rather than incidental: a skewed `P` lowers `H(V)` and every seam term in the same stroke
[DDD-measure-12], so it enters as a covariate and never as noise.

**The baselines.** `I(V;S)` must be set against number of interface states, schema or contract
description length, cyclomatic or logical complexity, interface surface area, input/output
dimensionality, and the description length of the routing rule. The last is not a rival measure, and
the framework says which it is before the data arrives: `L(routing rule)` is the standing side of §2.1,
priced in description length, while `I(V;S)` is the demand the seam carries [DDD-cost-03]. **The
prediction is that both load and neither subsumes the other** — that `I(V;S)` retains association after
`L(routing rule)` is controlled. If it does not, the demand register is idle where it matters most and
the distinction this note is built on buys nothing.

It is a different paper and it is the one that would make this a measured result rather than a
well-founded one.

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

The boundary is a scope condition, and it is best stated as one.

> **The construction applies where the task supplies an operationally usable verdict function and a
> ground distribution that can be estimated.**

Three requirements sit inside that sentence, and they fail in different ways. Collapsing them is the
error the section is written to avoid.

**Existence.** `H(V)` requires a verdict function. Where the acceptance predicate assigns no correct
output to a point of the input space, there is no ground truth to have entropy about, `H(V)` is
undefined, and there is nothing to measure.

**Availability.** A verdict function can exist without being usable. A predicate that assigns a definite
verdict to every input, but whose acceptance procedure cannot be executed over available ground within
declared resource, latency, and confidence bounds, does not close [term:closure] — and `H(V)` then
exists mathematically while being unavailable in practice. These are two failures, not one. The second
says nothing about existence. Formal decidability is the wrong criterion for either: any bounded finite
domain is decidable by lookup, and a decidable checker may require infeasible resources.

**Estimability.** Closure is not sufficient. `H(V)` is taken with respect to `P` (§2), so `P` must be
known well enough to estimate. Where the deployment distribution is unknown, unstable, non-stationary,
or only partly observable, the demand is well defined and cannot be computed [DDD-measure-12]. A
verdict function alone does not deliver a number.

### 7.1 What the boundary does not claim

**An open predicate does not abolish measurement.** Where evaluators disagree there are distributions
over their judgments; where preferences are elicited there are distributions over preferences; where
outputs are scored there are distributions over scores. Those are measurable, and some are informative.
What is unavailable outside the scope condition is *this construction* — a deterministic verdict
function to take the entropy of — and not measurement as such. The note claims the domain of its own
construction and nothing wider.

The framework holds the same thing from the other side. Its governance question — is every governing
decision in a declared store, none escaped? — is well-formed on open predicates exactly where the
measure is not, and its domain is strictly wider than the measure's [DDD-frame-11]. Nothing about the
measure's silence licenses a claim that determination is unaccountable where the measure stops.

### 7.2 The coincidence, and what it is worth

The construction's domain was not chosen to match the framework's floor. The framework locates a task's
irreducible floor in its acceptance predicate — the floor is non-zero where the predicate does not
close, because verification is then structurally unavailable and the demand falls to whoever is present
— and that result was derived on different grounds, before this measure existed. The measure goes
silent in the same region, and for the same reason: no verdict function. **Measurement and closure have
the same domain** [DDD-measure-06].

That is worth noticing and it is not evidence. The two arguments share a premise — the closure of the
acceptance predicate — so their agreement about where the line falls is close to definitional on the
measure's side. What is not definitional is that the line was drawn twice, from different materials,
with neither drawing fitted to the other. That makes the boundary **principled rather than arbitrary**.
It does not make the identification true, and the note does not argue that it does.

**One thing this section narrows, and one it does not.** What is narrowed is what the note argues: the
scope condition above, and no claim about measurement beyond it. What is not narrowed is the
identification, which the companion framework carries as a projected claim with the correspondence of
§6 as its falsifier [DDD-measure-01]. The note presents that claim at the strength its own framework
gives it — neither more nor less — and narrowing an argument is not weakening a claim.

The consequence is a bounded result, which is the correct kind. **Conservation of determination demand
is a theorem for closing predicates.** Off that region it remains what it was — an accounting
discipline, a principle rather than a measured invariant — and this note does not extend its reach. It
proves the part inside the boundary and marks the edge.

---

## 8. Related work

Each neighbour below is taken in turn, and each entry closes on what this note takes from that
literature or concedes to it. The epistemics — what the computations establish, and where the
falsifiable content lives — are §6's, and are not reargued here.

**Shannon (1948).** The theorem is Shannon's, and so is every formal object in this note: entropy,
mutual information, and the chain rule that carries conservation are used exactly as 1948 states
them. What the note contributes is the identification alone — determination demand as verdict
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
than description length? §2.1 answers it in full — the two are not rivals, they price different
sides of the act — and what remains for this section is where that answer leaves the literature.
MDL's two-part form, `L(model) + L(data|model)`, is not a competing measure of demand. Read as
per-act rates it is the cost decomposition laid over the same conserved identity [DDD-cost-03],
and over `N` acts it becomes `L(mechanism) + N·H(V|E)`, with computable crossover volumes at which
a distinction flips from occasioned to standing — the volume layer, downstream of this note
[DDD-cost-06; DDD-cost-07]. That layer exists only because the standing side is priced as
description length: the degeneracy of §2.1 is what rules out pricing it in captured information,
and a graded build-out over acts needs a standing quantity that is not conserved [DDD-cost-02].
Where the framework has looked for this structure in production data,
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

> **For a task whose acceptance predicate closes, determination demand is the Shannon entropy of the
> verdict over the ground the task faces. Conditioning on any variable `X` splits it by the chain
> rule into what `X` encoded and what remains, which always sum to the whole. `X` a decomposition gives the seam; `X` an actor's encoding
> gives the store allocation, total actor-invariant and split actor-relative; `X` what is supplied
> before the act gives the encode/verify split. Conservation of determination demand is the chain rule of entropy —
> where the predicate closes, and only there.**

---

## Reproduction

Five self-contained scripts regenerate every figure above: `measure-toy.py` for §4,
`measure-actor-allocation.py` for §5.1, `measure-rag.py` for §5.2, `measure-chained-seams.py` for
§5.3, and `measure-nonuniform-ground.py` for §5.4 — the last two in `assets/` beside this note. All
five were re-run against this draft and reproduce the stated values.

§5.2's replicate figures — the estimator's standard deviation, central range, and bias — characterise
the estimator `measure-rag.py` uses and are not printed by it. They are reproduced by running the same
plug-in estimator over 200 independent samples of `N = 40,000` acts from the prior `w` and the channel
stated in §5.2; every parameter needed is given there.
