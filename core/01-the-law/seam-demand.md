# Seam Demand Under Decomposition

> Insertion block for `core/01-the-law`. States, actor-neutrally, the conservation consequence of decomposing a governing decision set: decomposition is not demand-neutral — it manufactures **seam demand**. This is the core conservation fact that the composition apparatus (`apparatus/composition/`) consumes; it is stated here so the law owns it and apparatus never redefines it.
>
> **Depends on:** the Law (governing decision set, four stores, conservation / no silent residual), `core/02-completeness/finite-index-lemma` (the decision set as a τ-live subspace with a basis).
> **Consumed by:** `apparatus/composition/partition.md`, `apparatus/composition/seam-allocation.md`.

---

## 1. The identity

Let a governing decision set `D(t,α)` be decomposed — partitioned into parts to be discharged separately (by distinct actors, distinct stages, distinct times; the identity is neutral to what the parts are).

A decomposition into parts `{Dᵢ}` induces a set of **seam decisions** `S`: the decisions that exist *only because the set was split* — the decisions at the boundaries between parts (what crosses each boundary, in what form, under what precondition, who owns the interface). These are governing decisions in the same sense as any other: varying them can move outcome past tolerance. They were not separate demand items for the undecomposed set, because a single undivided discharge held all boundaries internally.

**Seam-demand identity.**

```
|D_decomposed|  =  |D_undecomposed|  +  |S(decomposition)|
```

Equivalently: total governing-decision demand is **not invariant** under decomposition. It is invariant under *re-allocation across stores* (the base conservation law) but *strictly increases* under *decomposition into separately-discharged parts*, by the seam `|S|`.

---

## 2. Why this is a conservation statement, not an apparatus detail

The base law says demand is fixed by the task and only relocates across the four stores — encoded, mechanical, judgment, escaped. That invariance is over *how one discharge is priced*. The seam-demand identity is over *how many discharges there are*. These are different operations:

```
re-allocation  (base law):   |D| constant; the four-store partition of a FIXED D changes.
decomposition  (this block):  D itself is split into parts; the split MANUFACTURES new
                              boundary decisions S, so total demand rises to |D| + |S|.
```

The identity is therefore a genuine extension of the conservation law's content — it tells you what conservation does under an operation the base law did not cover. It is actor-neutral (nothing here mentions who discharges the parts), so it belongs in core. The *reasons one would decompose* (to spread reach across actors, to parallelize, to add redundancy or backup) and the *machinery of spending `S`* are actor-structural and belong in `apparatus/composition/`.

---

## 3. Seam demand is still demand

`S` obeys the base law without exception. Every seam decision is carried by a store or it escapes:

```
S encoded   →  the boundary is specified (an interface / precondition / protocol)
S judged    →  the boundary is decided per-run by an accountable actor at discharge time
S escaped   →  the boundary is decided by nobody → boundary defect
```

There is no store in which a seam decision costs nothing. In particular, **`S` cannot be made to vanish by choosing a clever decomposition** — only *minimized*. A decomposition that cuts along sparsely-coupled boundaries manufactures small `|S|`; one that cuts through dense coupling manufactures large `|S|`. `|S| = 0` requires no decomposition at all (the undivided set). This is the conservation root of modularity: a good boundary is one where `|S|` is locally minimal.

---

## 4. Consequences (stated in core, developed in apparatus)

The identity has consequences that core states and apparatus develops:

- **Decomposition is a trade, never free.** Whatever a decomposition buys (reach, speed, reliability) is paid for in `|S|`. The trade is favorable only when the gain exceeds the manufactured seam. Developed per-motive in `apparatus/composition/seam-allocation.md`.
- **Unencoded seam relocates onto judgment or escape.** By §3, seam not carried by encoding is carried by per-run actor judgment (raising the actor cost / required tier at the boundary) or escapes as boundary defect. The tier consequence couples to the tier–specification inverse law (`core/03-the-polanyi-floor`); the coupling is developed in `apparatus/composition/`.
- **The defect structure of a decomposed discharge mirrors its boundaries.** Because `S` lives at the boundaries and unencoded `S` escapes there, boundary defects concentrate at decomposition seams. This is the conservation derivation of Conway's law; stated here, instantiated for actor composition in apparatus.

---

## 5. Scope

- The identity counts seam decisions; the `|S|` **estimator** (how to count boundary decisions from a given decomposition of the τ-live basis) is not fixed here and is declared where used. Projected until an estimator is declared.
- "Decomposition" here is the abstract operation of splitting a decision set into separately-discharged parts. Its actor-structural instances — partition across actors, pipeline across stages, overlap across redundant/backup actors — are `apparatus/composition/`. The identity holds for all of them because it is neutral to which instance is chosen.
