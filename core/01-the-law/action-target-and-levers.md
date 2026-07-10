# Action, Target, and the Two Levers

> Insertion block for `core/01-the-law`. Defines what an action is, how a target success determines required specification, and how the two ways to reach a target — specification and actor — are priced against distinct residual classes.
>
> **Depends on:** the Law (governing decision set, four stores, assurance level, last wind), `core/02-completeness/finite-index-lemma` (τ-live rank, τ-effective dimension), `core/03-the-polanyi-floor` (intrinsic + transfer decomposition).

---

## A. Action and intent

A unit of work is an **action** iff it carries a **decidable acceptance predicate**

```
A : Y → {0,1}
```

over outcome space `Y`, such that for any produced outcome `y`, `A(y)` is determined in finite steps by a designated accountable actor. A unit lacking such a predicate is an **intent**, not an action.

**Decidable, not deterministic.** The word that separates action from intent is *decidable*, not *deterministic*. `A(y)` must terminate with a verdict; how `y` was produced — deterministically, stochastically, by a model under last wind — is irrelevant to whether the unit is an action. Determinism is a property of the executing actor (the last-wind axis); decidability is a property of the acceptance predicate (the specification axis). They must never be fused. A model actor with irreducible variance still executes genuine actions, because the acceptance predicate is decidable even though production is not.

*"Go gardening"* is an intent: no criterion applied after the fact yields a verdict. It decomposes into actions — *weed bed A* (predicate: no weeds > 3 cm remain, decidable by inspection), *water the tomatoes* (predicate: soil moisture > threshold, decidable by probe). The intent is the value the actions serve; the actions are the units carrying acceptance predicates. **An intent becomes actionable exactly when a decidable acceptance predicate is attached** — and that attachment is specification work.

**The acceptance predicate is the criterion form.** `A` is the mechanical-verification store made into a membership condition: the criterion form of the action's governing decisions, applied after the act. An action is precisely a unit whose demand *can* be pushed into the mechanical-verification store. "Go gardening" cannot; that is why it is not an action.

**τ sets both grains at once.** With a tolerance-parameterized predicate

```
A_τ(y) = 1   iff   ‖ y − y* ‖ ≤ τ        (y* the spec/reference outcome)
```

the same τ that cuts the sensitivity spectrum in the finite-index lemma — setting `|D(t,α)|` — also sets the acceptance predicate's grain. An action's acceptance predicate and its decision count are two readouts of one tolerance. This is why assurance level is a single knob: tightening τ simultaneously admits more governing decisions and sharpens the acceptance test.

**Actor-relativity caveat.** "Decidable by a designated accountable actor in finite steps" imports the actor. For a purely digital action under zero-floor, `A` closes over digital state and is decidable by a program — actor-independent. For a physical action (*weed bed A*), `A` is decidable only relative to an actor with the inspection capability to judge "weed" vs "seedling"; that judgment is itself a decision in the judgment store with its own floor. Decidability of the acceptance predicate is **actor-independent for zero-floor digital actions, actor-relative for physical ones** — the same KC1⊥zero-floor / KC2-needs-zero-floor split from the finite-index lemma, surfacing in the definition of action. (KC1–KC3 = the three Knowability Claims: finiteness, membership decidability, loop termination — see `core/02-completeness`.)

---

## B. Success decomposition

Success shortfall is not one quantity. It splits into two classes with different reducibility, and the split is what makes the cost metric coherent:

```
1 − success  =  esc_escape  +  esc_wind

  esc_escape   escaped decisions — nobody decided.
               Reducible by allocation (relocate decision: judgment/escaped → encoded).
               This is the class specification trades against.

  esc_wind     actor residual variance under tightest pinning (last wind).
               NOT reducible by specification. Buying more spec does not move it.
```

Only `esc_escape` responds to specification. Against `esc_wind`, "more specification → more success" is false: unbounded specification cannot close a gap that is the actor's irreducible variance. A metric that treats total shortfall as spec-purchasable demands infinite specification to close a gap specification structurally cannot reach.

---

## C. Specification–success trade

Let `s` = specification effort, measured as **decisions moved into encoded stores** (priced as τ-live rank per the finite-index lemma — decisions, not tokens or hours). Then

```
success(s)  =  1 − esc_escape(s) − esc_wind

  esc_escape(s) ↓ 0   as s → full coverage of the τ-live subspace
  esc_wind      = const   for a fixed (task, actor, env) triple      ← the floor
```

The reachable ceiling is **not** 1:

```
success_max  =  1 − esc_wind  =  1 − floor
```

This is the maturation asymptote of the canon read on the success axis. Coherence check: if a cost metric asymptotes anywhere other than `1 − floor`, it is wrong.

**The trade is marginal.** "How much spec for how much success" is a derivative, and it is the diagnostic from the escape law:

```
d(esc_escape)/ds < 0                    →  spec is buying success; keep spending  (escape-class)
d(esc_escape)/ds ≈ 0,  esc still > 0    →  wind floor reached; remaining shortfall is esc_wind;
                                           further spec is wasted — STOP
```

The second condition is the **kill signal for specification effort**, pre-declarable. You stop not at a target success but when the derivative flattens with residual shortfall — a flat derivative over nonzero residual *is* the operational detection of the floor. The floor is not assumed; it is read off the point where money stops moving success.

**Cost as a decision.** With `c(s)` the rising cost of specification and `V(p)` the value of success level `p`:

```
s* = argmax_s [ V(success(s)) − c(s) ]

interior optimum:  V'(success) · (−d esc_escape/ds)  =  c'(s)
```

Two corner solutions force a stop instead of an interior optimum:

1. `d esc_escape/ds → 0` — wind floor reached; no success left to buy at any price. *Specification-side stop.*
2. `V(1 − floor) < c(s)` at the required `s` — the best reachable success is not worth what it costs to specify toward it. *Value-side stop:* the task is **under-worth-specifying**, its wind floor caps success below the level that would justify the cost. The framework should say this out loud.

---

## D. `plan(p*)` — what do I need to hit a target

Given a fixed (task, actor, env) triple and target success `p*`:

```
plan(p*):
  1. FEASIBILITY GATE
     if p* > 1 − esc_wind:
        return INFEASIBLE(actor)        # no s reaches p*; the shortfall is wind, not escape
                                        # → actor lever required (Section E)
  2. SOLVE
     s* = the s such that esc_escape(s) = 1 − esc_wind − p*
     return FEASIBLE(s*)                # required specification, as a decision count
```

Three properties:

- **The gate can reject.** If `p* > 1 − esc_wind` there is no `s`; the procedure returns *infeasible with this actor*, not a large `s*`. The honest reading of "can I calculate what I need?" is: first check the target is below the actor's ceiling; only then does a required-specification number exist.
- **The numbers are measured, not derived.** The equation's form is theory-fixed (projected). `esc_wind` and the shape of `esc_escape(s)` come from exercise — attributed residual and the convergence cycle. `s*` is **reported** only after those two curves are pinned. Until then you hold the relationship, not the value.
- **`s*` is a decision count, basis-relative.** Turning `s*` decisions into a work/cost estimate `c(s*)` is a second, encoding-basis-dependent mapping. "What I need" splits into *how many decisions to encode* (theory-determined given the two measured curves) and *what they cost to encode* (basis- and actor-relative).

---

## E. The two levers

`plan(p*)` has exactly two outcomes, and they are the two levers of any high-assurance execution program:

```
FEASIBLE(s*)        →  SPECIFICATION LEVER   (escape-dominated residual)
                        relocate decisions into encoding; actor fixed; lower esc_escape

INFEASIBLE(actor)   →  ACTOR LEVER           (wind-dominated residual)
                        change the actor to lower esc_wind (Section F)
```

**The domain does not pick the lever; the action does.** Which lever an action demands is set by where its residual sits — escape or wind — measured by the derivative test, not by domain tradition.

```
                    SPECIFICATION LEVER          ACTOR LEVER
                    (lower esc_escape)           (lower esc_wind)
  ───────────────────────────────────────────────────────────────────
  medical           clinical research            surgical specialist
                    protocol, pre-registration   fellowship, embodiment
  military          intelligence analysis        special forces
                    doctrine, SAT, ACH           selection + training
```

Both domains use both levers. Pre-registration and structured analytic techniques are constraint-form encoding that kills escape-class residual (the forking-paths problem is escaped decisions surfacing as false positives). Fellowship and selection lower the wind floor of an embodied actor.

**Mis-lever is the characteristic high-stakes failure — the framework's falsifiable prediction:**

- Specifying against a wind-dominated action → infinite protocol, checklists that do not help, "we wrote a procedure and it still failed" — the residual was never escape. (A checklist for surgical intuition would not work; aviation checklists work *because* those decisions were escape-class.)
- Training/selecting against an escape-dominated action → heroic actors compensating for an unspecified system; brittle, non-scalable, escape resurfaces the moment the hero is absent. Much "we just need better people" is a mis-diagnosed escape problem.

**Levers compose per residual class.** Real programs run both. Special forces carry heavy doctrine (spec atop a selected actor); surgeons follow the WHO surgical checklist (spec against the escape-class residual even a specialist leaves — glove counts, site marking — while embodiment handles the wind class). An action's residual is layered: an escape portion the spec lever clears and a wind portion only the actor lever reaches. `plan(p*)` returns the *mix*, not a side.

---

## F. Inside the actor lever: train, then select

The actor lever is not one operation. The Polanyi floor decomposes, and the two components take different tools:

```
floor  =  intrinsic (final, unmovable)  +  transfer (movable, manufactured by training)

  training  manufactures transfer-floor reduction (embodiment: intra-actor encoding
            that amortizes without externalizing — executed, not articulable).
  selection measures the intrinsic floor and rejects actors whose intrinsic floor
            is too high for the demand placed on them.
```

Apply in order: **train down the transfer floor; when demand still exceeds the reachable floor, select for a lower intrinsic floor.** How far training gets before selection takes over is set by the environment's recurrence structure.

**Two inverted floor structures:**

```
                  transfer-dominated            intrinsic-dominated
                  (heart surgeon)               (Delta operator, CQB)
  ──────────────────────────────────────────────────────────────────────
  action          recurring, stable             non-recurring, adversarial
  spec withheld?  no — specification maximized   yes — specification withheld by design
  floor reach     low, reachable by training     high, not reachable past intrinsic bound
  dominant lever  TRAIN                          SELECT
  attrition       aptitude threshold             brutal — searching for a rare
                                                 pre-existing low intrinsic floor
```

The surgeon's floor is *transfer-dominated*: the operation recurs enough for embodiment to amortize, so training moves the floor down to a small residual intrinsic component. The fellowship exists because training works.

CQB is *intrinsic-dominated* — **and by design**. The assignment ships with specification deliberately reduced ("we have some knowledge; you do the rest yourself") because the environment is adversarial and non-recurring: an adversary optimizes against any doctrine you would encode, and no two rooms repeat. Withheld specification relocates demand onto the actor's judgment store; past the transfer floor that demand can be met only by a lower *intrinsic* floor, which training cannot manufacture. Selection is the only remaining lever. Selection attrition is brutal because it is a search for a pre-existing low intrinsic floor; training attrition is not, because it amortizes a transfer floor every apt actor shares.

**The tier–specification inverse law.**

> Required actor tier rises as encoded specification falls. Withheld specification relocates demand onto the actor's judgment store; past the transfer floor, that demand can be met only by a lower intrinsic floor — which is **selected, not trained**.

This is why special-operations tiers climb precisely where doctrine thins.

**Correction to a common conflation.** "Movable floor" and "existing floor" are opposite properties. Both surgeon and operator have intrinsic floor > 0 (both are physical, embodied — zero-floor never obtains). The difference is not *surgeon has a floor, operator does not*; it is *which component dominates*. The surgeon's floor is low and reachable because it is transfer-dominated; the operator's is high and unreachable-by-training because it is intrinsic-dominated. Stating it as "movable vs not" would lose that both are partly unmovable — the surgeon simply carries less of the unmovable part relative to the demand placed on them.

---

## G. Summary of the arc

```
action        = unit with a decidable acceptance predicate A (criterion form; τ-grained)
shortfall     = esc_escape + esc_wind                       (two classes, different reducibility)
success(s)    = 1 − esc_escape(s) − esc_wind,  ceiling 1 − floor
plan(p*)      = feasibility gate → { FEASIBLE(s*) | INFEASIBLE(actor) }
levers        = specification (lower esc_escape) ⊕ actor (lower esc_wind), composed per class
actor lever   = train (transfer floor) then select (intrinsic floor)
tier law      = actor tier rises as encoded specification falls
```
