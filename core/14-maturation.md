# Maturation

<!-- ddd:contract

requires: [act, occasioned-cost, escape]
establishes: [maturation, waterline, maturity]
status: settled
-->

**The dynamics of the volume layer.** `13` prices supply across acts at a fixed allocation; this
file states what moves the allocation. Same register: cost, not conserved. Everything below
requires verdicts to persist between acts, so it files here under the boundary charter (upstream
`DDD-dec-09`; adopted `DDD-dec-10`), and it files **actor-general** per R4b (`DDD-dec-11`): the
ledger method's home domain is engineering, not its boundary.

**Claims.** The propositions of this note are landed as claim nodes under `core/claims/`; canon
authority for each is its claim file, and this document is their exposition. The mapping:

| Section | Proposition | Claim | Status |
|---|---|---|---|
| §1 | The maturation schedule: density-order encoding, stepwise decline to the two-part floor | `DDD-cost-14` | projected |
| §2 | Record dependence: uncaptured verdicts mature nothing | `DDD-cost-15` | projected |
| §2 | Escape is doubly costly: escaped demand cannot be learned out of | `DDD-cost-16` | projected |
| §2 | Open predicates stall the loop | `DDD-cost-17` | projected |
| §2 | Drift is the counter-force; steady state is encoding rate = depreciation rate | `DDD-cost-18` | projected |

Where this prose and a claim disagree, the claim governs and the prose is the bug.

**Basis and figures.** The empirical basis is graded in the principle repository's assessment
(`meta/mdl-cost-manufacturing-assessment-2026-08-08.md` at the pinned ref): learning-curve data
is abundantly consistent with the generic form and was never collected to discriminate it. The
maturation-curve figure is a Context& projection, not canon; it links here after acceptance.

---

## 1. The return channel and its schedule

The act is a two-sided event. Forward, it consumes occasioned supply. Backward, it produces: the
verdict is new ground about the verdict function itself.

<!-- ddd:embed id=term:maturation -->
> **Maturation** — the return channel spanning the act in reverse: from the mechanical store
> (post-act verdicts) into the encoded store (pre-act standing supply). A maturing arrangement
> is one where that loop is closed.
<!-- /ddd:embed -->

The schedule follows from the cost layer, with no new parameter:

<!-- ddd:embed id=term:waterline -->
> The **waterline** — the descending crossover threshold: the `N*` below which a distinction is
> not yet worth standing at current volume. Cumulative acts push it down.
<!-- /ddd:embed -->

Distinctions encode in information-density order as each crosses its `N*` — `DDD-cost-07`'s
marginal condition, read over time rather than at a point. Per-act occasioned cost declines
stepwise toward a floor, and the floor decomposes in two: the **open-predicate residual** — no
verdict function, nothing to encode, ever — and the **below-waterline tail** — verdicts exist,
not worth encoding at this volume. *(Claim `DDD-cost-14`, projected.)*

| Stage | Allocation | Signature |
|---|---|---|
| Novice | All occasioned | No record; volume buys nothing |
| Recording | Occasioned + capture | Verdicts accumulate; waterline begins descending |
| Encoding | Staged build-out | Distinctions cross `N*` in density order; the learning curve |
| Equilibrium | Standing above waterline; occasioned = floor + tail | Encoding rate = drift rate |
| Sclerotic | Over-encoded | Standing exceeds optimum; drift outruns re-encoding |

<!-- ddd:embed id=term:maturity -->
> **Maturity** is the distance between an arrangement's actual allocation and the
> volume-and-drift-optimal allocation — not the fraction encoded.
<!-- /ddd:embed -->

Steady state is not full encoding. It is the equilibrium where encoding rate matches
drift-driven depreciation of encoded bits (§2, drift) — which is why the sclerotic stage is a
failure mode and not an achievement.

---

## 2. Rate bounds — each a distinct claim

- **Record dependence.** Uncaptured verdicts mature nothing. An arrangement without an
  execution record pays full occasioned cost forever, regardless of volume. The record is a
  productive asset, not only an accountability one. *(Claim `DDD-cost-15`, projected.)*
- **Escape is doubly costly.** Escaped residual never reaches the predicate, so it generates no
  verdict: ungoverned now and invisible to maturation. **Escaped demand cannot be learned out
  of.** *(Claim `DDD-cost-16`, projected.)*
- **Open predicates stall the loop.** No verdict function, no clean signal; maturation there
  runs only on proxy, delayed, or social feedback. *(Claim `DDD-cost-17`, projected.)*
- **Drift is the counter-force.** Encoded bits depreciate at the drift rate of the ground they
  encode; steady state is encoding rate matching depreciation, and over-encoding is a real
  failure mode (basis: Abernathy & Wayne 1974, the Model T — organisational evidence, not a
  cost floor; the assessment's caveat is carried, not waived). *(Claim `DDD-cost-18`,
  projected.)*
