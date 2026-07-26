# An Information-Theoretic Account of Specification Demand

**A formal note.** Location: `core/09-the-measure.md`. Reproduction scripts in
`core/assets/measure-*.py`. Also suitable as a standalone paper
(*"Specification Demand Is Verdict Entropy: Conservation as the Chain Rule"*).

**Status.** The central identity is a theorem (Shannon, 1948). The **claim** of this note is not
the theorem — it is the *identification* of the framework's informal quantities with exact
information-theoretic ones. That identification is a modelling claim, it is falsifiable, and on the
worked example it holds without leftover or contradiction. **Scope: the closing-predicate region
only.** The note is explicit about where the measure ceases to exist, which is exactly the floor.

**What this pays off.** The counting-procedure debt booked in `meta/lineage-and-limits.md` — *"until
a counting procedure for governing decisions exists and is shown invariant across two architectures,
conservation is an accounting identity, not a measured invariant."* This note supplies the
procedure, for closing predicates, and shows the invariance is a theorem rather than an observation.

---

## 1. The move: demand is not a count

The counting procedure kept failing because it tried to measure an extensive quantity with a
cardinality. Decisions resist counting for a concrete reason: a decision closing over a large ground
carries more demand than one over a small ground, and decomposition *creates* decisions (the seam).
Count and demand come apart.

So demand is not a count. It is a **measure**. And the measure is **Shannon information**.

> **Definition (specification demand).** For a task with a decidable acceptance predicate, let the
> **verdict** be the correct output the predicate assigns to each point of the input space, and let
> `P` be the distribution over inputs (the *ground distribution*). The **specification demand** of
> the task is the Shannon entropy of the verdict:
>
> **D = H(verdict)**, measured in **bits**.

Demand is the information required to specify the correct answer over the ground the task faces. Not
how many decisions — *how much distinction*.

---

## 2. The identity: conservation is the chain rule

Let `S` be a **decomposition** — any variable that splits the task into sub-tasks (handle each value
of `S` separately). The chain rule of entropy gives, with no approximation:

> **H(verdict) = H(verdict | S) + I(verdict ; S)**

Read through the framework's vocabulary:

| Information quantity | Framework quantity | Meaning |
|---|---|---|
| **H(verdict)** | total demand `D` | the task's distinction demand — **fixed by the task** |
| **H(verdict \| S)** | runtime demand of the parts | what the sub-actors must still resolve *given the split* |
| **I(verdict ; S)** | **seam demand `\|S\|`** | what the *decomposition choice* absorbed |

So the framework's asserted seam identity

> `|D_comp| = |D_single| + |S|`

is **derived**, not posited: it is the chain rule, with `|S| = I(verdict ; S)`. The seam demand is
the **mutual information between the decomposition and the answer.**

**This is what "conservation within a fixed decomposition" means, made exact.** Fix `S`, and
`H(verdict|S) + I(verdict;S)` is *forced* to equal `H(verdict)`. Moving work between the split and
the parts is a zero-sum transfer. Conservation is not an empirical regularity; it is an algebraic
identity — once you accept the identification in §1.

---

## 3. Worked example (fully computed)

Task: validate a two-field date `(M, D)`, `M ∈ {1,2,3,4}`, `D ∈ {1,…,31}`, uniform inputs.
Verdict: `VALID ⟺ D ≤ days(M)`, with `days = {Jan 31, Feb 28, Mar 31, Apr 30}`.
`n = 124` points; 120 valid, 4 invalid.

**Total demand:** `H(verdict) × n = 25.493 bits`.

Two decompositions, each computed exactly:

| Decomposition `S` | groups | runtime `H(V\|S)·n` | seam `I(V;S)·n` | sum |
|---|---|---|---|---|
| **A** — split by month | 4 | 20.593 | 4.901 | **25.493** |
| **B** — split by day (`≤28` vs `≥29`) | 2 | 11.020 | 14.474 | **25.493** |

Both sum to the whole, exactly. (Verified to machine precision: residual `−0.0000`.)

---

## 4. What the example corrects in the framework

Decomposition B's *parts* are much cheaper than A's (11.0 vs 20.6 bits). The earlier framework
language would call B "a better decomposition that destroys demand." **The computation shows this is
wrong.** B did not destroy demand; it moved *more* demand into the seam — `I(verdict;S)` rose from
4.9 to 14.5 bits. B's split (knowing the valid/invalid boundary lives at day 29) is a
**high-information choice**: it absorbs more, so the parts are easier. The total is invariant.

> **Correction to the canon.** "A better decomposition destroys demand" → **"A better decomposition
> pre-pays more demand into the seam, buying cheaper parts. The total is invariant."** The
> destruction was always an artifact of not counting the seam.

This also sharpens the encoded store's role (`core/01`): the seam `I(verdict;S)` is *encoded*
demand — paid once, into the decomposition, and inherited by every run. B is "better" only because
someone already knew where the boundary was. That knowledge is not free; it is the mutual
information, pre-paid.

---

## 5. What it predicts (not just postdicts)

The identity is not merely descriptive. For a fixed task, ranging over all decompositions `S`:

- **A hard frontier.** `H(verdict|S)` is minimised exactly when `I(verdict;S)` is maximised, and
  the sum is constant. **You cannot make the parts easier without a higher-information seam.** This
  is a quantitative tradeoff curve, testable against any concrete task.
- **You cannot decompose your way out of the work.** `H(verdict|S) = 0` requires
  `I(verdict;S) = H(verdict)` — the decomposition already contains the *entire* answer. The only way
  to make the parts trivial is to put all the demand in the seam. This is the exact, quantitative
  form of the framework's claim that demand is conserved, not escapable.
- **The maturation/funnel asymptote** (`core/08`) is `H(verdict) − I(verdict;S_encoded)`: as you
  harvest more of the answer into the encoded decomposition, runtime demand falls toward the
  residual the encoding hasn't captured — never below what the *open* part of the predicate leaves
  undetermined.

---

## 6. One theorem, three conditioning variables

The decomposition result (§2) is one instance of something more general. The chain rule holds for
**any** variable `X` you condition the verdict on:

> **H(verdict) = I(verdict ; X) + H(verdict | X)**
>
> total demand = what `X` encoded + what is left to resolve given `X`

The framework's separately-stated claims turn out to be this one identity with three different
choices of `X`. Each was verified computationally.

### 6.1 X = a decomposition → seam demand

Covered in §2–§3. `I(verdict; S)` is the seam; `H(verdict|S)` is the runtime demand of the parts.
This *derives* the asserted `|D_comp| = |D_single| + |S|`.

### 6.2 X = an actor's encoding → store allocation (the actor model, unified)

Let `E` be **what an actor can encode before acting** — the actor's pinning resolution made concrete
as a variable it can compute about the input. Then:

> **H(verdict) = I(verdict ; E) + H(verdict | E)**
> total demand = **encoded by this actor** + **left to this actor's judgment**

Computed on the date task (`H(verdict) = 25.493` bits), for three actors of increasing encode
capacity:

| Actor | what it can encode | encoded `I(V;E)` | judged `H(V\|E)` | sum |
|---|---|---|---|---|
| **Program** (pins by value) | the exact verdict | 25.493 | 0.000 | **25.493** |
| **Weak model** | coarse proxy (`D ≤ 28`) | 14.474 | 11.020 | **25.493** |
| **Mid model** | `D ≤ 28` + "is it February?" | 20.964 | 4.529 | **25.493** |

**The total is actor-invariant; the allocation is actor-relative.** This is the precise, provable
form of the unification of conservation with the actor model — and it corrects a tempting overclaim:

> **Demand is NOT "constant *by* actor" (each actor with its own conserved quantity — that would be
> mere relabelled difficulty). Demand is "constant *across* actors, *allocated by* actor."** The same
> `H(verdict)` faces every actor; the actor sets only how it splits between encoded and judgment.

`H(verdict)` never mentions the actor. It is a property of the verdict function and the ground
distribution — the task. That is exactly why it is "fixed by the task, never by the system."

### 6.3 X = retrieval → RAG, and conservation measured on a real pattern

RAG is the encode/verify split (`apparatus/encode-verify.md`) running in production: it converts
**ground** (the corpus) into **encoded** specification (retrieved context), leaving the model to
carry the residual as judgment. With `R` = retrieval:

> **H(answer) = I(answer ; R) + H(answer | R)**
> total demand = **encoded by retrieval** + **left to the model's judgment**

This was tested not with a clean formula but with a **messy simulated retrieval process** — imperfect
hit rate, plausible distractor documents — with the information quantities *estimated empirically from
40,000 samples*. If the identity were an artifact of a tidy channel, this would break it. It does not:

| retrieval (hit / distractor) | encoded `I(A;R)` | judged `H(A\|R)` | sum |
|---|---|---|---|
| 0.00 / 0.00 | 0.000 | 2.609 | **2.61** |
| 0.30 / 0.20 | 0.458 | 2.154 | **2.61** |
| 0.50 / 0.30 | 0.791 | 1.812 | **2.60** |
| 0.70 / 0.20 | 1.365 | 1.251 | **2.62** |
| 0.90 / 0.05 | 2.136 | 0.474 | **2.61** |
| 1.00 / 0.00 | 2.612 | 0.000 | **2.61** |

`H(answer) ≈ 2.61` bits throughout. **Better retrieval moves demand from judgment to encoded;
distractors push it back; the total never moves.** Conservation of specification demand, measured on
a deployed system pattern rather than a toy — and the same theorem as the seam and the actor
allocation.

### 6.4 What this unifies

Three of the framework's claims that read as independent —

- the **seam identity** (`core/06`),
- the **actor-relative store allocation** (`core/04`),
- the **encode/verify split** (`apparatus/encode-verify.md`),

— are **one theorem seen three ways**: the chain rule of entropy, conditioned on a decomposition, an
actor's encoding, or a retrieval policy. Different `X`, same `I(verdict;X) + H(verdict|X) =
H(verdict)`.

**One caveat, now paid down.** In all three, *escape* is folded into `H(verdict|X)` together with
*judgment* — the identity separates "encoded" from "everything else," not "judged" from "escaped."
Splitting those two required a model of actor **capacity**, and `core/10-the-floor-mechanism.md`
supplies it: hold and resolve capacity in bits, effective capacity `min(C_hold, C_resolve)`, the two
overflow modes, and the intersection result `escape = overflow ∩ open` with a formula in bits, plus
a soft-capacity law derived from rate-distortion theory. The point at which `H(verdict|X)` exceeds
effective capacity is where demand begins to escape — derived and demonstrated, not conjectured
(`core/10` §§2–4).

---

## 7. Where the measure stops — and why that is the right boundary

**This account works only where the acceptance predicate closes**, and it is essential to say so.

Shannon entropy of the verdict requires the verdict function to be *defined*. Where the acceptance
predicate does not close (`core/03`), there is no verdict function — no ground truth to have entropy
about — so `H(verdict)` is **undefined** and the measure does not exist.

This is not a gap to be patched. It is the **same boundary** the floor result already draws:

> **The information-theoretic measure of demand exists if and only if the acceptance predicate is
> closed for the arrangement over ground it can inspect. It vanishes exactly at the floor.**

Which is the elegant, and honest, consequence: we have measured demand precisely on the region where
the framework says the floor is zero, and the measure *itself* goes silent precisely where the floor
becomes non-zero. Measurement and closure have the same domain. The floor remains unmeasured —
correctly, because it is where measurement fails.

So the claim is bounded: **conservation of specification demand is a theorem for closing
predicates.** For open predicates it remains what it was — a principle, an accounting discipline, not
a measured invariant. The note does not extend the framework's reach; it *proves* the part that was
already inside the decidable region, and marks the boundary sharply.

**A second silence, inside the boundary.** Even where it exists, `H(verdict)` prices the
**verdict**, not the **search**: it is the information required to *specify* the correct answer over
the ground the task faces, and it says nothing about the cost of *computing* one. Two tasks with
identical verdict entropy can differ unboundedly in generation cost — a lookup table and a SAT
instance over the same input space carry the same `H(verdict)`, and one is answered by indexing
while the other is NP-hard to solve. Closure decides whether the floor is zero and whether the
measure exists; generation cost is a second, independent variable the measure does not see
(`core/03` §2, `core/04` §2). The two quantities this release separates must not be re-fused through
the measure.

---

## 8. Caveats, booked

Three, none fatal, all required in any write-up:

1. **The theorem is Shannon's; the claim is the mapping.** The chain rule is 1948. What is asserted
   here is the *identification* of demand with verdict-entropy, seam with mutual information,
   decomposition with conditioning. That identification is falsifiable and was vindicated on the
   example — but it must be claimed as a modelling result, never as a mathematical discovery.

2. **Demand is relative to the ground distribution.** `H(verdict)` depends on `P(input)`; the
   example used uniform. So *"fixed by the task"* must be stated as *"fixed by the task, the
   tolerance, and the ground distribution."* This is arguably more correct — the same validator
   faces different demand in different deployment environments — but it is an added parameter, not a
   free lunch.

3. **Three instances is credibility, not certification.** The identity is general (it is the chain
   rule), and it has now been exercised on three conditioning variables — decomposition, actor
   encoding, and (empirically, with distractors) retrieval — all on closing-predicate tasks. That is
   real triangulation, not a single toy. But chained seams, multi-actor compositions, and non-uniform
   ground should still be worked before publication, and an information theorist should certify the
   framing. The theorem is exact; *identifying* the real conditioning variable for a deployed system
   is estimation with error bars.

---

## 9. The result, in one line

> **For a task whose acceptance predicate closes, specification demand is the Shannon entropy of the
> verdict. Conditioning on any variable `X` splits it, by the chain rule, into what `X` encoded
> (`I(verdict;X)`) and what remains (`H(verdict|X)`), which always sum to the whole. Three of the
> framework's claims are this one identity: `X` a *decomposition* gives the seam; `X` an *actor's
> encoding* gives the store allocation (total actor-invariant, split actor-relative); `X` a
> *retrieval policy* gives RAG. Conservation of specification demand is the chain rule of entropy —
> where the predicate closes, and only there.**

---

## Reproduce

Three self-contained scripts regenerate every figure in this note:

- `assets/measure-toy.py` — §3, decomposition (the seam).
- `assets/measure-actor-allocation.py` — §6.2, three actors, one invariant total.
- `assets/measure-rag.py` — §6.3, messy empirical retrieval with distractors.
