# The Finite-Index Lemma

> When is the governing decision set of a task finite — and therefore knowable in finite terms? This lemma answers that question and no other. It does not use digitality; it is independent of the zero-floor postulate.

**Location:** `core/02-completeness/finite-index-lemma.md`
**Depends on:** `core/01-the-law` (governing decision set, assurance level, tolerance)
**Independent of:** `core/03-the-polanyi-floor` (zero-floor postulate). See §5.

---

## 1. What this lemma establishes

The Law allocates `|D(t,α)|` across four stores and forbids silent residual. That accounting presupposes `D(t,α)` is a well-defined finite set. This lemma states the condition under which that presupposition holds. It is one of the three **Knowability Claims** (KC1: finiteness); KC2 (membership decidability) and KC3 (loop termination) are proved elsewhere and rest on different premises. "KC" is used for these throughout the completeness core to avoid overloading `K`.

The claim is **not** that every task has a finite decision set. It is that finiteness is a checkable property of the task's outcome map relative to the assurance level, and it identifies exactly which property.

---

## 2. The object to quotient

Naively one might quotient the space of *candidate decisions* by τ-outcome-indistinguishability and ask for finite index. This is vacuous: candidates compose. Refining one decision into two, or fusing two into one, generates infinitely many candidates from finitely many underlying degrees of freedom. The candidate space is combinatorially infinite even for trivial tasks. It is the wrong object.

Quotient the **free-parameter space** instead.

Let the task's outcome be a map

```
O : Θ → (Y, ‖·‖)
```

where `Θ = ∏_{i∈I} Θ_i` is the space of free parameters of the action — the degrees of freedom **not** pinned by substrate (facts, which are inspected not decided) and **not** pinned by the actor's fixed value-bindings. `Y` is outcome space with a norm. `α` fixes tolerance `τ`.

A governing decision's only demand-relevant content is how it moves outcome. So the object that carries decision content is the coordinate structure of `Θ`, read through `O`.

---

## 3. τ-live coordinates

**Definition.** Coordinate `i ∈ I` is **τ-live** iff moving it alone can cross tolerance:

```
∃ θ ∈ Θ, ∃ θ_i' ∈ Θ_i :   ‖ O(θ) − O(θ[i ↦ θ_i']) ‖ > τ
```

A coordinate that is not τ-live is **τ-dead**: no admissible move along it ever changes outcome by more than τ.

This is coordinate-wise, which dissolves the composition problem. Refining or fusing candidate decisions does not change how many coordinates of `Θ` carry τ-sensitivity.

---

## 4. The lemma

> **Lemma (Finite Decision Set).**
> With `O`, `Θ`, `τ` as above, `D(t,α)` is in bijection with the set of τ-live coordinates, and
> ```
> |D(t,α)| < ∞   ⟺   the number of τ-live coordinates is finite.
> ```

**Proof.**
Each governing decision is, by the granularity membership test of `core/01-the-law`, a degree of freedom whose variation can move outcome past τ. In the `Θ` basis this is precisely a τ-live coordinate; τ-dead coordinates fail the membership test and are excluded. The correspondence decision ↔ τ-live coordinate is therefore a bijection by construction of `Θ`. Finiteness of one side is finiteness of the other. ∎

The lemma reduces "is `D` finite?" to "does `O` have finitely many τ-live coordinates?". That right-hand side is not automatic. §4.1 gives the condition under which it holds; §4.2 the failure mode.

### 4.1 Sufficient condition: τ-approximate finite dimension

> **Condition (τ-finite sensitivity).** There exists a finite `J ⊆ I` such that `O` factors through the projection `π_J : Θ → ∏_{j∈J} Θ_j` up to tolerance:
> ```
> ‖ O(θ) − O(π_J θ) ‖ ≤ τ    for all θ ∈ Θ.
> ```

Under this condition every coordinate outside `J` is τ-dead: moving it leaves `O` within τ, so it can never cross τ. Hence the τ-live set is contained in `J` and is finite; `|D(t,α)| ≤ |J| < ∞`.

In words: **outcome depends, up to tolerance, on only finitely many coordinates.** This is a modulus-of-continuity statement about `O` — a τ-approximate finite-dimensionality of the outcome map. It is the honest hypothesis the lemma runs on.

### 4.2 Failure mode

The condition can fail, and the failure is real, not pathological. An outcome map that aggregates contributions from infinitely many coordinates — each individually sub-τ, but with no finite `J` capturing the aggregate to within τ — has infinitely many τ-live coordinates and no finite decision set at that α.

The canonical example: an outcome required bit-exact against an unbounded reference stream. At τ below one bit's contribution, infinitely many coordinates are live. Raise τ above the tail mass and the count collapses to finite. **τ does the work.** Tightening α (lowering τ) can flip a coordinate from dead to live. Finiteness is a statement about where τ sits in `O`'s sensitivity spectrum, not an absolute property of the task.

Quotable form:

> `D(t,α)` is finite **iff** the outcome map has finite τ-effective dimension. A task is knowable in finite terms exactly to the depth τ reaches into `O`'s sensitivity spectrum.

---

## 5. Independence from the zero-floor postulate

Nothing above uses digitality. `O` may be physical, analog, or digital. Finiteness is purely a relation between the sensitivity spectrum of the outcome map and τ. Therefore:

```
KC1 (finiteness)  ⊥  zero-floor postulate.
```

Zero-floor supplies KC2 (membership decidability) and KC3 (loop termination) for purely digital tasks. It does **not** supply KC1. A purely digital task can still have unbounded outcome-sensitivity and hence no finite decision set. Fusing the two would be a vocabulary collision: keep them as separate lemmas with separate premises.

---

## 6. Corollaries

**C1 — The granularity bound is a spectral cut.**
"Assurance level = granularity bound" becomes precise: α selects τ, τ selects a cutoff in `O`'s sensitivity spectrum, and `|D(t,α)|` is the number of modes above the cut. Raising assurance lowers the cut and admits more decisions. This is the mathematical content of *determination demand is fixed by the task*: the spectrum belongs to the task, the cut belongs to the assurance level, and `|D|` is determined by both — by no one's discretion, and never by the system.

**C2 — The invariant is τ-effective rank, not coordinate count.**
The lemma fixed a basis `Θ = ∏ Θ_i`. The τ-live *count* is basis-dependent: a rotation can spread one live coordinate across many. What is basis-invariant is the **τ-effective dimension** — the rank of `O`'s sensitivity above τ, not the coordinate count. The rigorous invariant is therefore

```
|D(t,α)|  :=  τ-effective rank of O.
```

Any encoding basis realizes this rank as a concrete decision count. Two correct specifications with different decision counts price the same demand: they are different bases of the same τ-live subspace.

**C3 — Coverage and redundancy get a formal reading.**
Coverage of demand = spanning the τ-live subspace. Redundancy = basis over-completeness (more encoded forms than the rank requires). This is the formal reason for *redundancy permitted, only uncovered-and-unpriced forbidden*: an over-complete basis still spans (permitted); a basis that fails to span leaves a τ-live mode unpriced (forbidden). Constraint form and criterion form of one decision are two basis elements aligned on the same mode — redundant, single-priced, non-double-counted.

---

## 7. Scope and what remains open

- The proof is at modulus-of-continuity level. Making the "sensitivity spectrum" fully precise (a metric-measure structure on `Θ` yielding a spectral decomposition of `O`) is deferred; it is not needed for the finiteness result.
- The τ-finite-sensitivity condition (§4.1) is stated as sufficient. Whether a natural necessary-and-sufficient condition exists in general is open; §4 already gives an exact iff at the level of τ-live coordinate count, which is what the accounting requires.
- τ-effective rank (C2) is asserted as basis-invariant at the modulus-of-continuity level. A full proof of invariance belongs with the deferred metric-measure treatment.
