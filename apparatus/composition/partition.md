# Actor Composition: Partition for Reach

> How multiple actors compose into one, and what capability that does and does not buy. This block treats the **partition** case: covering a larger decision set than any single actor can reach. Reach is the only capability axis composition adds; this block states the exact gain, the exact cost (seam demand), and the success/failure conditions.
>
> **Location:** `apparatus/composition/partition.md`.
> **Depends on:** `core/01-the-law` (governing decision set, four stores, conservation, acceptance predicate, last wind; **seam-demand identity** `|D_comp| = |D_single| + |S|`); `core/02-completeness/finite-index-lemma` (τ-live subspace, τ-effective rank/basis); the capability decomposition (reach / resolution). Cross-refs the Build-seam / Reification-Contract apparatus (interface contracts).

---

## 1. When is a composite an actor at all

The action/intent definition applies to composites unchanged. A collection of actors is itself **an actor** iff the joint action carries a **decidable acceptance predicate** — a verdict on the composite output, determinable in finite steps. A collection with no joint acceptance predicate is not a more-capable actor; it is an **intent with an unfinished decomposition**. First gate, before any capability question: does the composite have a verdict? If not, there is nothing to compose — there is only work not yet specified.

---

## 2. Capability is not one scalar

"Gain enough capability" hides the trap. From the capability decomposition, an actor's capability is at least two independent axes:

```
reach       breadth of the decision space the actor can address
resolution  per-decision work the actor can bring to a single decision
```

Composition acts on these two oppositely, and conflating them is the characteristic error:

```
reach       COMPOSES      — disjoint coverage unions; the composite reaches ⋃ of parts
resolution  DOES NOT       — per-decision resolution is bounded by the BEST single actor
                            on that decision; actors below a decision's demand do not sum
                            to an actor above it. Averaging can worsen it (committee mean).
```

> **Composition buys reach, not resolution.** A reach-bound action (large decision set, each decision individually within some actor's resolution) is closed by composition. A resolution-bound action (some decision exceeds every available actor's resolution) is **not** — no count of actors closes it; only a higher-resolution single actor on that decision does.

This is the escape/wind split in team clothes: composition reduces escape-class residual (decisions nobody had the *reach* to cover) and does nothing for wind-class residual on any individual decision. This block is the reach case; it assumes the action is reach-bound and every `dᵢ` sits within some actor's resolution.

---

## 3. Partition, exactly

Partition the τ-live subspace (finite-index lemma) into regions, one actor per region:

```
D  =  D₁ ⊔ D₂ ⊔ … ⊔ Dₙ ⊔ S
       └── actor i owns Dᵢ ──┘   └─ S = seam decisions ─┘
```

Two conservation facts make this exact.

### 3.1 Reach is the union — the genuine gain

If each actor's reach covers its assigned `Dᵢ`, the composite covers `⋃ Dᵢ` by construction. When `⋃ Dᵢ` exceeds any single actor's reach, the composite has strictly more reach than its parts. This is the only capability axis composition adds, and it is real.

### 3.2 The partition manufactures S — the strict cost

`S` did not exist for a single actor. It is created **by the act of partitioning** — the interface decisions at every boundary between `Dᵢ` and `Dⱼ`: what is passed, in what form, who owns the interface. These are governing decisions in `D(t,α)` that a single actor never had to encode because it held both sides in one head.

This is the actor-composition instance of the **seam-demand identity** (`core/01-the-law`, *Seam Demand Under Decomposition*): decomposition into separately-discharged parts is not demand-neutral; it manufactures seam demand. For a partition across actors, that identity reads:

```
|D_composite|  =  |D_single|  +  |S(partition)|
```

> **Decomposition is not demand-neutral.** It strictly increases total governing-decision demand by the seam `|S|`. The single actor paid `|D|`; the team pays `|D| + |S|`. This is the non-obvious conservation consequence of composition, and it is the whole reason composition is a trade rather than free capability. The identity itself is core; this file instantiates it for partition across actors.

---

## 4. The seam must be encoded, or it escapes

`S` is demand. By the Law it is carried by some store or it escapes. For a composite there is only one honest place to carry it: the **encoded store, as an interface contract**.

```
S encoded    →  interface contract (producer authors the seam; Build seam / Reification Contract)
S unencoded  →  boundary escape (integration defect)
```

**Boundary escape is the characteristic multi-actor failure mode:** every actor's piece is individually correct, the composite fails, and the failed decision lived in the seam where no actor owned it. Each side assumed the other decided it.

This gives Conway's law a derivation rather than an analogy: the composite's defect structure mirrors its partition boundaries because that is where `S` lives, and unencoded `S` surfaces exactly there. The framework's addition is the mechanism — **seam demand is conserved, so it is paid in encoding (interface contract) or in escape (integration bug), never in nothing.** The entire discipline of interface contracts *is* the pricing of seam demand into the encoded store.

---

## 5. Success and failure conditions

```
PARTITION WINS  iff
  (a) reach-bound       — |D| large; each dᵢ within some actor's resolution
  (b) complete coverage — ⋃ Dᵢ ⊇ τ-live subspace; no region unassigned
  (c) seam encoded      — every decision in S carried by an interface contract
  (d) net positive      — reach unlocked  >  |S| cost
```

Each failed condition names a distinct real failure:

```
¬(a)  resolution-bound action → composition cannot close it; wrong lever (need higher-res actor)
¬(b)  coverage gap → a τ-live region owned by nobody → escape in the interior, not the seam
¬(c)  unencoded seam → boundary escape → integration defect (the Conway failure)
¬(d)  seam cost exceeds reach gain → the team is net negative; a single broader actor is cheaper
```

Condition (b)'s failure is worth distinguishing from (c)'s: (b) is an **unassigned region** (nobody was given those decisions); (c) is an **unencoded boundary** (the decisions between regions were nobody's). Both are escape, at different locations — interior vs seam.

---

## 6. Partition granularity: the seam–reach tradeoff

`|S|` depends on *where* you cut. Finer partition (more actors, smaller `Dᵢ`) means more boundaries → larger `|S|`. Coarser partition means more reach demanded per actor. The optimal partition minimizes seam subject to the reach constraint:

```
minimize   |S(partition)|
subject to each Dᵢ within its actor's reach
```

The minimizer cuts along the **natural low-coupling seams of the τ-live subspace** — boundaries where decisions on either side are most nearly independent, so the interface carries the fewest decisions. This gives modularity a conservation meaning:

> A good module boundary is one where `|S|` is locally minimal — the cut passes through sparse decision-coupling. A bad partition cuts through dense coupling and pays enormous seam cost.

So *how* a team is split matters as much as *that* it is split, and it is measurable in principle (seam decision count), not merely aesthetic. Two partitions of the same action into the same number of actors can have very different `|S|`; the better one found the sparse cut.

---

## 7. What composition does not do (guardrails, from the other cases)

Stated so this block is not misread as "composition = capability":

- **Does not add resolution** (§2). Held here by the reach-bound assumption; a resolution-bound decision inside some `Dᵢ` breaks the composite regardless of how many actors surround it.
- **Does not reduce a shared floor.** Adding actors who share a blind spot (same training, same doctrine, same missing capability) does not cover the region none of them reach — `⋃ Dᵢ` still excludes it. Reach gain is real only across *complementary* actors; redundant actors union to no more than one of them.
- **Redundancy (same decision, multiple actors) is a different composition** — it touches wind-class residual, not reach, and only when residuals are independent. Out of scope here; see the redundancy/ensemble treatment.

---

## 8. Theorem

> **Composition-by-Partition Theorem.** A composite of actors is an actor iff the joint action has a decidable acceptance predicate. Partitioning the τ-live subspace into disjoint regions gives the composite reach `⋃ Dᵢ`, which may strictly exceed any single actor's reach, at the cost of seam demand `|S|` — governing decisions manufactured at the boundaries, satisfying `|D_composite| = |D_single| + |S|`. The seam must be carried by an encoded interface contract or it escapes as boundary (integration) defect. Composition closes a reach-bound action iff coverage is complete, the seam is encoded, and reach unlocked exceeds `|S|`. Composition does not add resolution and cannot close a resolution-bound action.

---

## 9. Open slots

- **`|S|` estimator.** Seam decision count is asserted as measurable-in-principle. A concrete estimator (counting interface decisions from a partition of the τ-live basis) is not given here; declare it before any reported `|S|`. Projected until then.
- **Optimal-cut existence.** §6 assumes a sparse cut exists. Some τ-live subspaces are densely coupled everywhere (no low-`|S|` partition) — for these, partition is dominated by a single broader actor. A criterion separating partitionable from irreducibly-dense subspaces is open, and is the composition-side analogue of the finite-index sensitivity spectrum.
- **Interaction with the tier–specification inverse law.** Seam encoding is itself specification; a partition that withholds seam encoding relocates seam demand onto the actors' judgment (each actor deciding the interface per-run) — raising required actor tier at the boundary. The composition and tier laws couple here; not yet developed.
