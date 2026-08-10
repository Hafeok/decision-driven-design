# Worked example — routing one act by capability

<!-- ddd:contract

requires: [act, capability]
establishes: []
status: settled
-->

**An evidence note.** This file is the routing model's worked instance — the upstream claims it
exercises are canon in the principle repository, pinned in `graph/upstream.yaml`:

<!-- ddd:ref id=term:capability -->
<!-- ddd:ref id=DDD-cost-08 -->
<!-- ddd:ref id=DDD-cost-11 -->
<!-- ddd:ref id=DDD-cost-12 -->

All quantities are **stipulated**; the structure, not the values, is the example. Reproduction:
`core/assets/measure-routing-example.py` (naming per Wave 1's R1 — the `measure-*` convention).
Notation: `α` in the tables below denotes *uncovered assurance* (bits/act), the holding-note
notation — distinct from `13` §1's price coefficient `α`.

**The act.** Implement a validated repository change from a filed ticket. One act = one verdict
of the merge acceptance predicate. This is Paper A's worked task, carried into the routing model.

---

## 1. Typing the act

Capability requirement derives from the admission test applied per ground type (`DDD-cost-12`'s
derivation at the pinned ref): a capability is required iff the verdict varies with ground
accessible only through that pathway. Vision is listed to show the test excluding.

| Capability | Ground type read | Residual (bits/act) | Mechanical coverage today | Uncovered α | Min class |
|---|---|---|---|---|---|
| code-synthesis | source, type system | 12.0 | 0.95 — compiler, types | 0.60 | small |
| tool-use | build/test toolchain | 3.0 | 0.90 — runs self-verify | 0.30 | any |
| navigation | repository structure | 4.0 | 0.70 — retrieval checks | 1.20 | small |
| architecture | conventions, intent | 8.0 | 0.15 — largely open | 6.80 | **frontier/qualified** |
| vision | visual | 0.0 | — | 0.00 | excluded by admission test |

---

## 2. State A — today: the frontier pin

Required class = max over capabilities of the class needed where assurance is not mechanically
discharged (`DDD-cost-12`). The maximum is architecture: 6.8 uncovered bits/act, class
frontier/qualified. One capability pins the act. Route: frontier, expected cost **111.1/act**
(price over per-try acceptance; retries included).

Note what is being paid for: synthesis, tool-use, and navigation are over-served by two classes.
The frontier price buys the whole vector to carry one component — which is the observed market
behaviour on coding acts, reproduced rather than assumed.

**The escape check.** Route the small actor anyway and the arrangement does not get cheap; it
gets ungoverned: architecture's 6.8 uncovered bits/act need class 3 and the small actor carries
class 1 — the difference degrades **without signal**, because no check reaches it. Escape, not
saving. This is `DDD-cost-11`'s safety bound made arithmetic.

---

## 3. State B — the sign flip: coverage releases the pin

Encode the architectural conventions into mechanical checks — fitness functions, structural
lint, dependency rules — raising architecture coverage from 0.15 to 0.85. Uncovered assurance
falls to 1.20; required class falls to small. **The binding capability moves**: code-synthesis
is now binding, at class small. Route: small actor, expected cost **7.3/act** — a fifteen-fold
drop, purchased entirely by coverage. No model improved. (`DDD-cost-11`, the sign flip;
`DDD-cost-12`, coverage-not-actor-progress.)

> **The pin releases when coverage improves, not when models do.** High assurance, on a closing
> predicate, is a reason to build checks, not to hire up.

The crossover is the familiar one. Stipulating the coverage investment at L = 3000, the per-act
saving of 103.8 gives **N\* = 29 acts** (`DDD-cost-07`'s marginal condition) — beyond that
volume the standing investment in checks pays for the class drop. The routing decision and the
encoding decision are the same calculation.

Partial investment interpolates: at architecture coverage 0.50, uncovered assurance is 4.0,
class mid, route code-mid at 26.7/act. The class falls exactly as far as coverage reaches, and
no further.

---

## 4. The rejection-payload lever

The small actor operates at its capacity margin, so retry economics enter (`DDD-cost-11`'s
second bound). The checker's rejection payload sets the per-try acceptance probability:

| Checker behaviour | p(accept)/try | E[tries] | Expected cost/act |
|---|---|---|---|
| pass/fail verdict only | 0.35 | 2.9 | 11.4 |
| rich rejection payload | 0.55 | 1.8 | 7.3 |

A checker that explains its rejection raises the weak actor's effective capacity — each retry
becomes a guided step. The shape of a rejection payload is a lever on achievable actor class,
not an API detail. (Basis cross-reference for the pending M3/M4 principal decision: queue item
2.13.)

---

## 5. What the example establishes, and what it does not

| Establishes | Does not establish |
|---|---|
| The routing model is computable: act profile in, route and cost out | That real acts decompose into these capabilities at these residuals |
| It is non-degenerate: the three coverage states produce three different routes at order-of-magnitude cost separation | That the class thresholds correspond to any measured actor property |
| It reproduces observed behaviour qualitatively: coding pinned to frontier by uncovered architectural assurance; capability-specialised actors beating general ones at matched acts | That coverage investment at these prices exists; L and all prices are stipulated |
| The constructs compose: admission-test typing, two gates, sign flip, N\*, escape, and retry economics in one arrangement with no conflict | Any correspondence to engineering cost — the same untested correspondence as the measure note §6, one layer up |

The correspondence that would make this measured rather than well-founded: audited capability
coverage of a real arrangement's checks should predict which actor class its acts actually
require, and coverage investments should produce class drops at computable N\*. That is a
protocol, stated and not run.

---

## 6. Reproduce

`core/assets/measure-routing-example.py` regenerates every figure above. Single file, no
dependencies, same convention as the other `measure-*` scripts.
