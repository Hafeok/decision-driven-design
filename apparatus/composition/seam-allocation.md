# The Seam-Allocation Law: Reach, Speed, Assurance, and Failover

> Composition has four motives — cover a bigger decision set (reach), finish sooner (speed), complete more reliably by agreement (assurance), complete more reliably by backup (failover). This block shows they are **one conservation account**: each manufactures seam demand and differs only in *where* the seam sits and *which residual class* it moves. Speed and serial assurance/failover are antagonistic; hedged failover is the one variant that escapes the antagonism, by moving reliability's cost from wall-clock to compute. The assurance and failover motives carry a mandatory diagnostic, because both help only against wind-class failure and are futile (assurance: actively false) against floor-class failure.
>
> **Location:** `apparatus/composition/seam-allocation.md`. Companion to `apparatus/composition/partition.md`.
> **Depends on:** `core/01-the-law` (conservation, four stores, ground, last wind; **seam-demand identity** `|D_comp| = |D_single| + |S|`, which this file's four allocations all spend); `core/02-completeness/finite-index-lemma` (τ-live subspace); `apparatus/composition/partition.md` (the reach allocation, `S` as interface seam); success decomposition `1 − success = esc_escape + esc_wind`; the wind/floor split of `core/03-the-polanyi-floor`.

---

## 1. One account, four allocations

The **seam-demand identity** of `core/01-the-law` is the master fact: decomposition manufactures seam demand `S`, and `|D_composite| = |D_single| + |S|` (instantiated for actor partition in `apparatus/composition/partition.md`). The four composition motives are four ways to *spend* that seam.

```
motive      what the partition does           seam is spent on           residual class moved
──────────────────────────────────────────────────────────────────────────────────────────────
reach       union disjoint decision regions   coverage interfaces        escape (coverage gaps)
speed       parallelize the critical path      dependency cuts            escape (boundary, from cuts)
assurance   overlap on same decisions, agree   redundant cross-check      wind — ONLY IF wind-dominated
failover    overlap on same decisions, backup  arbitration + cancellation wind-failure — ONLY IF independent
```

Assurance and failover are **siblings**: both overlap actors on the same decision, both need failure independence, both are futile against correlated floor-failure. They differ only in the aggregation operator — assurance takes the **mean** (agreement/vote), failover takes the **max** (first success). That single difference (§4a) makes failover monotone-safe on correctness where assurance is not.

All three obey the same conservation: seam is demand, carried by the encoded store (a contract, an assumption, a cross-check protocol) or escaped (boundary defect, stale assumption, ratified error). **There is no free composition.** The motives are not different mechanisms; they are different seam allocations of one mechanism.

---

## 2. Reach — seam as coverage interface (recap)

Covered fully in `apparatus/composition/partition.md`. Partition the τ-live subspace into disjoint regions `D = ⊔ Dᵢ ⊔ S`; the composite reaches `⋃ Dᵢ`; seam `S` is the interfaces between regions; unencoded `S` → boundary escape (Conway). Reach composes; resolution does not. Included here only as the first of the four allocations. The remaining three add structure *on top of* a reach partition.

---

## 3. Speed — seam as dependency cut

Speed is not coverage. It is **parallelism across the critical path**. Decisions carry a dependency order: a decision that consumes another's output as *ground* cannot run until that output exists. So wall-clock time is bounded not by actor count but by dependency depth:

```
t_wall  ≥  critical path  =  longest chain of dependent decisions in D
```

**Amdahl, derived through the decision graph.** Adding actors past one-per-parallelizable-region buys zero speed; the critical path is unmoved. Speed is available only to the width of the graph, never below its depth.

**The seam cost of speed.** To run regions concurrently you must **cut dependency edges**. Cutting an edge means the downstream actor cannot wait for the real upstream output — it must proceed on an *encoded assumption* standing in for that output. Each cut manufactures a seam decision of a specific kind:

```
dependency cut  →  seam decision = "the assumed value of the not-yet-available upstream output"
                   encoded   → an assumption contract (precondition the upstream must satisfy)
                   unencoded → stale-assumption escape (downstream ran on a guess that was wrong)
```

So **speed strictly increases `|S|`**, and it does so by forcing cuts through decision-coupling a serial actor would have left intact — precisely the dense-coupling regions that `apparatus/composition/partition.md` §6 said to *avoid* cutting. Speed spends seam by cutting where reach-partition would not.

```
more parallelism  →  more dependency cuts  →  larger |S|  →  higher boundary-escape risk
```

The assumption-seam is the load-bearing object: a fast composite is a bet that its cut-point assumptions hold. Encoding them (preconditions, contracts) prices the bet; leaving them implicit is stale-assumption escape.

---

## 4. Assurance — seam as redundant overlap, with a mandatory diagnostic

Assurance is the opposite geometry from reach. Reach makes decisions **disjoint** (each owned once); assurance makes them **overlapping** (each owned `n` times):

```
reach:      D = D₁ ⊔ D₂ ⊔ …        each decision owned once
assurance:  every actor sees the same d, results aggregated   each decision owned n times
```

Redundancy on a decision aggregates `n` actors' verdicts. Whether this buys success depends entirely on **which residual class dominates the decision's shortfall** — and that is exactly what was declared unknown, so the law must *diagnose before it spends*.

### 4.1 The two classes behave oppositely under redundancy

```
wind-class residual   (independent execution variance, last wind)
    → redundancy AVERAGES IT DOWN.  n actors, independent errors → aggregate error falls (~1/√n).
    → redundancy WORKS. This is the case that buys success.

floor-class residual  (intrinsic floor — correlated across actors sharing the limitation)
    → redundancy RATIFIES IT.  If the decision exceeds every actor's floor, they fail together;
      the vote returns their shared wrong answer with HIGHER confidence.
    → redundancy gives FALSE ASSURANCE. Worse than one actor, because it launders correlated
      error as agreement.
```

> Redundancy buys success against the wind component of shortfall and manufactures false confidence against the floor component. Applied blind, it cannot tell which it is doing.

### 4.2 The diagnostic — separate the classes before spending redundancy

Since the residual class is unknown, run the separation *first*. The signature that distinguishes them is **correlation of error across independent actors**:

```
DIAGNOSTIC (pre-redundancy):
  put n actors that do NOT share training/doctrine/ground on the same decision.
  measure error correlation ρ across them.

    ρ ≈ 0   (errors independent)      → wind-dominated  → redundancy will work; spend it
    ρ ≈ 1   (errors agree when wrong)  → floor-dominated → redundancy is false assurance; DO NOT spend
                                          the residual is intrinsic → actor lever (train/select), not overlap
```

The diagnostic requires **actor diversity** to be valid: `n` actors sharing the same blind spot always show `ρ ≈ 1` on that spot regardless of the true class, so a homogeneous ensemble cannot distinguish wind from floor — it will report floor-like correlation even for wind, or hide floor behind shared confidence. **Diversity of actors is the precondition for the diagnostic, and independence of error is the thing redundancy needs anyway.** A redundant ensemble of identical actors is the degenerate case: it neither diagnoses nor helps.

### 4.3 Cost

Redundancy's seam is a **cross-check protocol** (how verdicts are aggregated, tie-breaking, what counts as agreement) plus the `n×` execution cost on each redundant decision. Encoded → an aggregation contract. Unencoded → the aggregation rule is itself a per-run judgment, relocating seam onto judgment (and, if the aggregator is one of the actors, correlating the very errors redundancy was meant to decorrelate).

---

## 4a. Failover — seam as backup, the max operator

Failover is assurance's sibling: overlap `n` actors on the same decision, but instead of aggregating their verdicts (mean), **take the first that passes the acceptance predicate** (max). You do not combine answers; you retry until one succeeds.

**Failover presupposes a decidable acceptance predicate** — you must *detect* the failure to know to fail over. This is the action/intent gate doing load-bearing work: no verdict, no failover, because you could not tell the first actor failed. Failover is only defined for actions that are actions.

### 4a.1 The success arithmetic and its trap

Composite fails only if *all* actors fail:

```
P(composite fails)  =  ∏ᵢ pᵢ         ← ONLY IF failures are independent
                    =  pⁿ             (identical independent actors)
```

`pⁿ` is the seductive number — it collapses fast, and it is why "just add executors" feels like free reliability. It is the failover form of the wind/floor trap:

```
independent (wind) failure   → failover WORKS.   P(all fail) = pⁿ falls fast.
                                the backup draws fresh; likely succeeds where the first stumbled.
correlated (floor) failure    → failover FUTILE.  P ≈ p regardless of n.
                                every actor fails on the SAME input; retrying a decision that
                                exceeds every actor's floor just fails again.
```

> Failover buys reliability against wind-class failure and **nothing** against floor-class failure. The `pⁿ` curve is real for independent stumbles and a fantasy for correlated floor-limits.

This is the **same diagnostic** as assurance (§4.2): measure failure correlation `ρ` across diverse actors. `ρ ≈ 0` → wind → `pⁿ` real → failover works. `ρ ≈ 1` → floor → `pⁿ` collapses to `p` → futile → switch to the actor lever. Same instrument; shared with the assurance motive.

### 4a.2 The mean/max asymmetry — failover is monotone-safe on correctness

Assurance (mean) and failover (max) differ in a way that matters:

```
assurance (mean)  CAN be worse than one actor — a committee ratifies correlated error,
                  laundering a shared wrong answer as agreement (higher confidence, same error).
failover  (max)   is NEVER worse than one actor on success probability — worst case is
                  "all fail," identical to one actor failing. A backup cannot make you
                  less likely to succeed.
```

So failover's downside is **cost, not correctness**. This is why backup *feels* safer than voting, and here it is genuinely true — on the success axis. The two catches are (1) the `pⁿ` gain is real only for independent failure, and (2) the handover can secretly re-correlate independent actors (below). Get those right and failover is the one composition motive monotone-safe on correctness.

### 4a.3 Hedged (parallel) failover — the variant that escapes the speed antagonism

Serial failover pays for reliability in **time**: retries stack on the critical path (`t = tₐ + t_b + …`), making it antagonistic to speed exactly like redundancy. **Hedged failover fires all `n` concurrently and takes the first success:**

```
serial:  t = Σ tᵢ over attempts   reliability↑, LATENCY↑, cost = actual attempts
hedged:  t = min(t₁,…,tₙ)          reliability↑, LATENCY↓, cost = n× (all fired)
```

Hedging does not stack on the critical path — `min` of concurrent draws is *faster* than a single expected draw, not slower. So hedging is the one reliability motive **aligned** with speed rather than antagonistic. It does not beat conservation; it **moves reliability's payment from the wall-clock store to the compute store.** You pay in `n×` executors what serial failover paid in `n×` time.

> Hedging is the escape hatch from the speed⊥assurance antagonism (§5) — along the resource axis only. Reliability is not free; it is made parallel.

**Two separable payoffs.** Hedging buys two things that come apart:

```
reliability:   P(all fail) = ∏pᵢ    — needs failure independence (the ρ diagnostic)
tail-latency:  E[min tᵢ] < E[tₐ]     — needs latency variance; helps EVEN WHEN p = 0
```

The tail-latency payoff is often the real reason to hedge: `min` clips the slow tail even if nobody fails. So hedging can be worth it at `p → 0` purely to cut completion-time variance — a benefit the `pⁿ` reliability story does not capture.

### 4a.4 The idempotency gate — hedging's hard precondition

Concurrent execution has a seam serial failover does not: **all `n` actually run.** Its seam decisions:

```
• cancellation predicate — when one succeeds, KILL the others. Unencoded → they run to completion,
  wasting resource AND possibly producing side effects. This is the characteristic hedging defect:
  DUPLICATE SIDE EFFECTS (two actors both commit the write, both send the email).
• idempotency of the action — hedging is safe ONLY for actions whose concurrent/repeated
  execution is idempotent OR cleanly cancellable.
• first-success arbitration — who declares the winner; is that arbiter a single point of failure
  that re-correlates the independence you paid for.
```

The idempotency requirement is a **hard gate, not a caveat**:

> Hedging trades cost for latency only for idempotent-or-cancellable actions. Fired at an action with irreversible side effects (charge the card, launch the missile, send the wire), hedging manufactures `n×` the side effect, not `n×` the reliability. For irreversible actions, hedging is not a reliability technique — it is a way to do the irreversible thing `n` times.

Serial failover largely avoids this gate (one runs at a time), which is the cost it pays for its worse latency. The choice between serial and hedged failover is therefore: **serial pays in latency and is side-effect-safe; hedged pays in resource and demands idempotency.**

### 4a.5 The handover re-correlation trap (both variants)

Whatever the variant, if a backup inherits the failed actor's partial work as ground, and the failure *corrupted* that work, the backup inherits the corruption — **re-correlating draws designed to be independent.** You engineered independence (fresh actor) and destroyed it (shared poisoned state). Clean failover requires the backup to draw fresh over the decision, not over the first actor's contaminated intermediate state. This is the failover-specific form of boundary escape: the handover secretly couples the executors you added to be independent.

---

## 5. The antagonism: speed and reliability spend against each other

Speed and assurance are the same knob turned opposite ways:

```
speed      CUTS dependency edges      → fewer cross-checks, more assumptions   → raises boundary escape → LOWERS assurance
assurance  ADDS redundant checks       → each check is a dependency the fast path wanted to cut → SERIALIZES → LOWERS speed
```

A cross-check is a dependency edge (the checked decision must complete before the check resolves). Speed's whole method is *removing* dependency edges; assurance's whole method is *adding* them. The speed-optimal partition of an action (maximal cuts, minimal overlap) and the assurance-optimal partition (maximal overlap, minimal cuts) are **different partitions of the same action**. No single partition is optimal for both —

**except on slack.** The one reconciliation:

```
if the critical path has SLACK (parallel width the longest chain does not use):
    spend the idle parallel capacity on redundancy that rides ALONGSIDE the critical path,
    not on it.  Redundant checks on off-critical-path decisions cost no wall-clock time.
    → speed and assurance stop competing exactly to the extent of the slack.
```

So the design target is: **partition so redundancy rides on slack.** Cross-check the decisions that are *not* on the critical path (free assurance); accept that cross-checking a critical-path decision trades directly against speed and must be paid for in wall-clock. Slack is the only place the two motives are not antagonistic.

**Serial vs hedged reliability changes which axis pays.** The antagonism above is specifically speed vs *serial* reliability (redundancy, serial failover) — both stack dependency edges on the wall-clock. **Hedged failover breaks it** (§4a.3): firing `n` concurrently pays for reliability in *compute*, not wall-clock, so it is aligned with speed rather than antagonistic. The full picture:

```
                        pays for reliability in    vs speed
  ───────────────────────────────────────────────────────────────
  redundancy (mean)      wall-clock (serial checks)  ANTAGONISTIC (except on slack)
  serial failover (max)  wall-clock (serial retries) ANTAGONISTIC (except on slack)
  hedged failover (max)  compute (n× concurrent)     ALIGNED (gated on idempotency)
```

So there are two escape hatches from the speed/reliability antagonism, not one: **spend reliability on slack** (works for any variant, limited by available slack) or **spend reliability on compute via hedging** (works without slack, limited by idempotency and resource budget). A design with neither slack nor idempotency nor spare compute genuinely cannot have both speed and reliability — the antagonism is real and binding there.

---

## 6. The unified law

```
SEAM-ALLOCATION LAW

Every composition manufactures seam demand S (|D_composite| = |D_single| + |S|).
The four motives are four allocations of S:

  reach      → coverage interfaces        moves escape-class residual (coverage)
  speed      → dependency-cut assumptions  moves escape-class residual (boundary), bounded by critical path
  assurance  → redundant cross-checks      moves WIND-class residual (mean); ratifies FLOOR-class residual
  failover   → arbitration + cancellation  moves WIND-class FAILURE (max); futile on FLOOR-class failure

All S is demand: encoded (contract / precondition / aggregation / cancellation protocol) or escaped
(boundary defect / stale assumption / laundered correlated error / duplicate side effect).

Constraints:
  • resolution never composes (reach guardrail)
  • speed is bounded below by critical-path depth (Amdahl via the decision graph)
  • assurance & failover require the wind/floor diagnostic BEFORE spending; need actor diversity to be valid
  • assurance (mean) can be worse than one actor (ratifies correlated error);
    failover (max) is monotone-safe on correctness (never worse than one actor)
  • hedged failover is gated on idempotency-or-cancellability; else it multiplies side effects
  • speed ⊥ serial reliability except on slack; hedged failover is speed-aligned, paying in compute
```

> **Statement.** A composition's motive determines only *where* its seam is spent and *which residual class* it moves; it cannot escape manufacturing seam, cannot compose resolution, cannot beat the critical path, and cannot convert floor-class residual/failure into success by overlap. Reach and speed move escape-class residual. Assurance (mean) and failover (max) move wind-class failure only: assurance misapplied to floor-class residual manufactures false confidence, failover misapplied to floor-class failure is merely futile. Speed and serial reliability are antagonistic except on critical-path slack; hedged failover escapes the antagonism by paying in compute, at the price of an idempotency precondition.

---

## 7. Diagnostic decision procedure (operational)

```
plan_composition(action, motive):

  reach wanted?
    partition τ-live subspace on sparse cuts (min |S|); encode interfaces; check coverage complete.

  speed wanted?
    build the decision dependency graph; t_wall floor = critical path depth.
    add actors only up to graph width. For each dependency cut, encode the assumption
    as a precondition contract. |S| rises with cut count — stop when reach gain of a
    further cut < its assumption-seam risk.

  assurance wanted?  (agreement — mean)
    DIAGNOSE FIRST: diverse actors on sample decisions, measure error correlation ρ.
      ρ ≈ 0 → wind-dominated → redundancy valid → place redundant checks, preferably on
              off-critical-path (slack) decisions; encode the aggregation protocol.
      ρ ≈ 1 → floor-dominated → redundancy is false assurance → switch to the ACTOR LEVER
              (train/select for a lower floor); do not spend redundancy.
      ρ unknown & actors homogeneous → diagnostic invalid → diversify actors or treat as floor
              (conservative: assume redundancy won't help until independence is shown).

  failover wanted?  (backup — max)
    SAME DIAGNOSTIC FIRST: measure failure correlation ρ across diverse actors.
      ρ ≈ 1 → floor → failover futile (P ≈ p, not pⁿ) → actor lever, not backup.
      ρ ≈ 0 → wind → failover valid (P(all fail) = ∏pᵢ). Then choose variant:
        action idempotent-or-cancellable AND spare compute?  → HEDGE (fire n concurrent,
            cancel losers, take first success). Speed-aligned; also clips tail latency.
            ENCODE the cancellation predicate or risk duplicate side effects.
        action has irreversible side effects?  → SERIAL failover only (one at a time).
            Pays in latency; never hedge an irreversible action.
      handover: backup draws FRESH over the decision; never inherit the failed actor's
        contaminated partial state (re-correlates the independence you paid for).

  all four?
    reach-partition first (coverage) → schedule for critical path (speed) →
    place diagnosed-wind redundancy on the resulting slack (assurance) →
    add failover for wind-class failure: hedge where idempotent+compute-rich,
    serial where irreversible.
    Order matters: coverage defines the graph, the graph defines the critical path,
    the critical path defines the slack, the slack is where free (serial) reliability goes;
    hedging spends compute instead of slack when slack runs out.
```

---

## 8. Open slots

- **Slack measurement.** "Critical-path slack" is asserted schedulable. Turning it into a number needs the decision dependency graph with per-decision cost estimates — the same graph the speed motive needs. Projected until the graph is instrumented.
- **ρ estimator and diversity metric.** The wind/floor diagnostic (shared by assurance and failover) rests on measuring error/failure correlation across actors and on a notion of actor diversity (non-shared training/doctrine/ground). Neither estimator is specified here; both must be declared before any reported assurance or failover reliability claim. This is the composition-side image of the escape-vs-wind classifier already designed for the hallucination harness — likely the same instrument, now doing triple duty (hallucination class, assurance validity, failover validity).
- **Assumption-seam vs interface-seam vs handover-seam accounting.** Reach's interface-seams, speed's assumption-seams, and failover's handover/cancellation-seams are all `S` but have different failure signatures (unowned boundary / stale assumption / duplicate side effect / re-correlated state). Whether they share one `|S|` ledger or several is unresolved; the `|S|` estimator (open in the partition block) must decide this.
- **Idempotency as an action property.** Hedged failover is gated on idempotency-or-cancellability, but nothing in the framework yet *classifies* an action as idempotent. This is an action-level property (does concurrent/repeated execution preserve the acceptance predicate?) that should be defined alongside the acceptance predicate in `core/01-the-law`, not left implicit in the composition layer. Flagged for the action definition.
- **Tail-latency as a distinct payoff.** Hedging's latency benefit (`E[min tᵢ] < E[tₐ]`) is separable from its reliability benefit and survives at `p → 0`. The framework accounts for reliability (success axis) but has no first-class treatment of latency-variance as a quantity; hedging exposes the gap. Open.
- **Coupling to the tier–specification inverse law.** Unencoded seam of any of the four kinds relocates onto per-run actor judgment, raising required tier at the seam. Speed raises it at cut points, assurance at aggregation points, reach at interfaces, failover at arbitration/handover points. The composition laws and the tier law meet at the seam; still not developed.
