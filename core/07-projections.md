# Projections

**Location:** `core/07-projections.md`. Depends on the principle (`01`), the floor (`03`), and the
compound loop in composition (`05`). Patch addition to the shipped 4.0 core.

**Status:** the correction in this document (funnel as *cost*, not *count*) resolves a modelling
error that produced spurious feedback loops in the reference model. That diagnostic history is
reported, not projected — see §5. This revision also makes "cost" precise (§"What cost is"): it is
**judgment demand**, denominated in decisions, and it inherits — does not escape — the
counting-procedure debt already booked for conservation.

> **Figure:** `assets/projections.svg` (static) · `assets/projections.html` (interactive — toggle
> "encode the harvest" to see the funnel form or fail). Both plot *judgment demand* descending while
> *count* stays flat — the correction, made visible.

---

## The two projections

The principle has two projections. They are not two mechanisms. **They are the same mechanism — the
encoded store amortising a cost paid once — viewed on two different axes.**

> **Maturation** is the compound over **repetition**: pay once, and every future *run* is cheaper.
>
> **The funnel** is the compound over **depth**: pay once at the top, and every decision *below*
> inherits the resolved ground cheaply.

Maturation runs along the time axis (run N+1 is cheaper than run N). The funnel runs along the
depth axis within a single run (decision K+1 inherits what decision K resolved). Same encoded-store
amortisation, two axes of the same space.

This is why they always read as siblings. They are the principle seen from two directions — the same
relationship RDF and event sourcing have (one opens the shape axis, the other the time axis, and
neither community noticed they were describing one thing).

---

## What "cost" is

"Cost" cannot stay a vibe with axes, or it is exactly the unpinned quantity the review caught in
"demand." So, precisely:

**Cost is not tokens, dollars, or wall-clock time.** Those are *substrate-specific prices* — they
vary by actor (a human-hour versus a GPU-second), so they cannot be the quantity the projection is
about, which is actor-general. If cost were dollars, the funnel would be a claim about a cloud bill.

**Cost is the price of resolving a governing decision, paid in the store that resolves it** — and
that price is not one currency but **one quantity denominated differently per store**, because the
four stores are four different ways to pay:

| Store | What "cost" means there | When paid | Amortises |
|---|---|---|---|
| **Judgment** | actor capacity spent resolving the decision this run | per run | no |
| **Encoded** | *authoring* (cheap) + **search** for the correct constraint (expensive) | once | yes |
| **Mechanical** | the executability tax — building the checker | once | yes (near-zero per run after) |
| **Escaped** | expected damage: defect probability × severity, discounted by when it surfaces | later | — |

So cost is **a vector with four components, each in its own natural unit.** You cannot naively add
across stores (see the caveat in §6). The funnel and maturation are claims about **one specific
component**, projected along an axis.

### The funnel measures judgment demand

> **In the funnel, "cost" is *judgment demand*: the quantity of governing decisions that must be
> resolved per run by an actor reading ground, rather than inherited from the encoded store.**
>
> **Unit: decisions-resolved-in-judgment.** The same unit the whole framework is denominated in —
> not tokens, not dollars. *Decisions.*

And now the descent has an exact cause rather than a shape:

> Each decision resolved and **encoded** at depth *k* removes ground that decision *k+1* would
> otherwise have had to resolve in judgment. The judgment demand at *k+1* falls by exactly the amount
> converted to encoded at *k*.

That is **conservation doing the accounting.** The judgment demand does not vanish — it **moved to
the encoded store one level up.** The funnel is the judgment-demand curve *precisely because* the
encoded cost was paid once at the top. The two are the same conserved quantity crossing a store
boundary.

**Cost is judgment demand, watched over an axis.** The orange curve in the diagram is judgment
demand per decision; the floor is not "where cost bottoms out" but **the residual judgment demand
that cannot be converted to encoded because the acceptance predicate does not close** (`03`) — which
is exactly why the curve asymptotes there and not at zero.

---

## The correction: the funnel is a judgment-demand projection, never a count projection

This is the load-bearing correction, and it fixes an error that was previously invisible.

**The old reading: the funnel narrows because there are fewer decisions as you descend.** This is
**wrong**, and it is wrong for the most fundamental reason available — it contradicts the principle.
The number of governing decisions is **fixed by the task** (`01`). Demand does not shrink. Any
picture in which the funnel narrows because decisions are *eliminated* is fighting conservation.

**The correct reading: the same decisions, less judgment demand each level.** Nothing narrows in
*count*. What narrows is **judgment demand per decision**, because a decision once encoded is not
re-derived in judgment — it is inherited. The funnel shape is the **judgment-demand curve**, not the
decision count.

> **The funnel is not decisions being eliminated. It is the judgment-demand-per-governing-decision
> curve descending as encoded ground accumulates within a run — the judgment demand converting to
> encoded, one level up, and the total conserved.**

The bigger actor at the top of the funnel is not there to make *more* decisions. It is there to
**pay the expensive first pass** — to spend the judgment that resolves ground which is then encoded
and inherited cheaply below. That is why you reach for the capable actor early and can drop to a
cheaper one deeper: not because there are fewer decisions down there, but because the top of the
funnel already converted their ground from judgment to encoded.

---

## The condition: it only funnels if you encode as you descend

The funnel is **conditional**. It forms only if the resolved ground is actually encoded on the way
down. Skip the encoding and there is no funnel — you pay full price at every level, and you
re-derive the same ground repeatedly.

> **Encode as you descend → judgment demand descends → clean funnel.**
> **Descend without encoding → judgment demand stays flat or spikes → no funnel, only re-derivation.**

This is the same condition maturation carries, on the other axis. Maturation forms only if the
harvest channel exists to carry the encoding from one run to the next (`05`, "the channel is the
platform"). The funnel forms only if the encoding is carried from one *level* to the next within a
run.

> **The funnel's condition ("encode as you descend") and maturation's condition ("the channel must
> exist") are the same condition on different axes: the encoded store has to actually receive the
> harvest, or neither projection forms.**

One failure mode. Two symptoms.

---

## Why this produced feedback loops in the model (the diagnostic)

The correction is not cosmetic. Under the old *count* reading, the reference model exhibited feedback
loops "at odd times" — and those loops were an artifact of measuring the wrong quantity.

Here is the mechanism. Under the count model, decisions were expected to decrease monotonically as
the run descended. But real runs do not behave that way: a decision deep in the funnel *surfaces new
governing decisions* — the seam demand `|D_comp| = |D_single| + |S|` (`05`), appearing whenever a
decision decomposes. Under the count model, that looks like the funnel **widening back out at the
wrong moment**: the count went *up* where the model said it should go *down*, and a feedback loop
appeared to fire for no reason.

Under the **judgment-demand** model, there is no loop. You hit a decision whose ground was not yet
converted to encoded, the judgment demand spikes locally, the ground gets encoded, and the demand
drops. The apparent "loop" was a judgment-demand spike that a count-based model had no way to
represent — so it surfaced as a spurious cycle.

> **The model was plotting count and seeing judgment demand. The odd-timed feedback loops were
> judgment-demand spikes the count representation could not express.**

And the diagnostic goes further, because it distinguishes two regimes the old model collapsed:

- **A run that encodes as it descends** shows judgment demand descending — a clean funnel, no loops.
- **A run that does not encode** shows judgment demand flat or spiking, and re-derives the same
  ground at each level — **genuine** loops.

So the feedback loops were not a bug in the model. **They were the model correctly showing the runs
where the compound was not happening** — where the funnel failed to form because the encoding was
skipped. The vocabulary to read them that way did not exist yet: they looked like "the funnel
behaving weirdly" rather than "the funnel failing to form."

This is the strongest kind of correction: it is retrodictive. It explains an anomaly that was
already observed and previously unexplained.

---

## The two projections, stated for the record

**Funnel — the positional / depth projection.**
Within a single run, judgment demand per governing decision descends as encoded ground accumulates —
*conditional on encoding as you descend*. The capable actor at the top pays the expensive first pass;
lower levels inherit resolved ground and can be handled by cheaper actors. The count of governing
decisions does not fall (and may locally rise as seams open); the **judgment demand** falls.

**Maturation — the recurrence / time projection.**
Across runs, judgment demand per run descends as encoded ground accumulates in the platform —
*conditional on the harvest channel existing* (`05`). Run N+1 inherits what run N encoded. Again the
count is fixed by the task; the **judgment demand** falls.

Both are the compound. Both are conditional on the encoded store actually receiving the harvest. The
asymptote of each is the floor (`03`): the decisions whose acceptance predicate does not close,
which never convert to encoded, and must be paid in judgment on every run and at every level. **The
funnel bottoms out at the floor; maturation converges to the floor.** Same limit, two axes — and now
the limit has a unit: the **residual judgment demand** whose predicate does not close.

---

## What stays unpinned (booked, not hidden)

Making cost precise exposes two debts. They must be stated, or this section becomes the thing the
next review catches.

**1. "Per decision" assumes decisions are countable and unit-comparable.** Judgment demand is a
quantity; "per governing decision" normalises it by a *count*, which assumes resolving decision A and
resolving decision B are one unit each. They are not obviously equal — a decision closing over a
large ground may carry more judgment demand than one over a small ground. So the honest unit is
**judgment demand**, and "per decision" is a normalisation that inherits the **same
counting-procedure debt already booked for conservation** (`meta/lineage-and-limits.md`). The funnel
does not create a new debt; it does not escape the existing one either.

**2. Cross-store addition is not defined.** You can watch judgment demand descend and encoded demand
rise, and — within that one transfer — call the total conserved. You **cannot** yet write
*total cost = a·judgment + b·encoded + c·mechanical + d·escaped*, because the exchange rates
(a, b, c, d) are not derived, and escaped "cost" is in different units entirely (expected damage, not
decisions). So **"total cost is conserved" is clean only within the judgment ↔ encoded transfer the
funnel shows.** Full four-store cost conservation remains **projected, not proven.**

What *is* pinned, and is enough for the projections: the funnel and maturation each track **one
component** — judgment demand — in **one unit** — decisions-resolved-in-judgment — and that component
descends because it converts to encoded, one boundary crossing, conserved. That claim stands on its
own without the cross-store exchange rates.

---

## The one line

> **Both projections are the same compound — pay once, inherit thereafter — drawn on two axes: depth
> within a run (the funnel) and repetition across runs (maturation). Both measure *judgment demand*
> — decisions that must be resolved by an actor rather than inherited from encoding — never *count*;
> the count is fixed by the task. Both form only if the encoding is actually harvested. And both
> descend only to the floor: the residual judgment demand whose predicate does not close.**
