# Composition

**Read `04-actors.md` first.** This document extracts and states, on its own terms, the composition
result that the actor model implies: **what happens to determination demand when you decompose one
actor into several, or one task into several.**

---

## The seam-demand identity

> **|D_comp| = |D_single| + |S|**
>
> A composite carries the demand of its parts, **plus** the seam demand `S` created *between* them.

Decomposition is **not demand-neutral.** Splitting a task or an actor manufactures new governing
decisions — the ones about how the parts coordinate — that did not exist when the thing was whole.
The interface contract is the one-time specification that pays `S` down; skip it and `S` does not
disappear, it escapes.

This is the composition-level statement of conservation (`01`): you cannot lower total demand by
decomposing. You can only *relocate* it, and decomposition *adds* the seam term. The one move that
genuinely lowers the total is choosing a *different* decomposition whose seam is cheaper — which is
why the decomposition is the highest-leverage decision.

---

## Seam demand allocates across the same four stores

`S` is demand, so it obeys the principle: it lands in encoded, mechanical, judgment, or escaped. The
allocation is a real design fork, and its name is **seam occupancy** — *who or what sits at the
seam.*

| Seam store | Occupant | Author cost | Run cost | Handles novelty | Poisonable centre |
|---|---|---|---|---|---|
| **Judgment** | an **actor** (an orchestrator) | cheap — just say "coordinate" | **expensive, every run** | **yes** | **yes** |
| **Encoded** | a **mechanism** (selection dynamics, stigmergy, price-clearing) | **expensive — search** | nearly free | no | no |
| **Mechanical** | a **check** on what the seam produces | executability tax | cheap | no | no |
| **Escaped** | nobody coordinates | zero | zero | — | — |

Note the last row. **A composite with no seam allocation is not a system, it is a mess** — a
badly-decomposed distributed architecture is exactly seam demand left in the escaped store. The
difference between an ant colony and a crowd is whether `S` is carried at all.

---

## Actor at the seam vs. mechanism at the seam

The central trade, and it has teeth:

**An actor at the seam** (an orchestrator) can carry *judgment* — it handles novelty in the
coordination itself, decides which sub-actor to trust when they conflict, notices when the
decomposition is wrong. But it is a **bottleneck** (all `S` flows through one actor's capacity), a
**single point of authorship** (poison its ground and you poison the composite — prompt injection
into an orchestrator is exactly this), and it **does not scale.**

**A mechanism at the seam** (clonal selection, a pheromone field, a market's price) cannot handle
novelty — the rule is fixed, and a situation outside what the rule anticipates escapes. But it
**scales without bound**, has **no bottleneck**, and crucially has **no poisonable centre**: you
cannot corrupt the immune system's seam by corrupting one lymphocyte, because the seam *is the
dynamics*, not any member.

> **Actor-at-seam buys adaptivity and pays with a bottleneck and a poisonable centre.**
> **Mechanism-at-seam buys scale and robustness and pays with rigidity.**

### The cost that is easy to miss

Encoded seams look free at runtime, and are not. **They are cheap to *state* and expensive to
*find*.** "Bind-and-proliferate" is three words; what was expensive was *finding a local rule whose
emergent behaviour is the coordination you wanted* — evolution paid for that in deep time. That is
**search cost over the space of encodings**, a cost distinct from the executability tax, and the
framework charges for it explicitly. **Swarms are not free.** They are cheap-per-run and enormously
expensive to author, which is the encoded store's usual bargain.

An actor at the seam is the opposite: expensive per run, cheap to specify — you delegate `S` to
judgment, and judgment need not be articulated. **You are buying your way out of a search problem
with per-run judgment cost.** Which is exactly why multi-agent systems overwhelmingly use
orchestrators: not because orchestrators are better, but because *nobody knows how to find the
seam-encoding.*

---

## The compound: harvesting the seam

The seam is where the compound effect lives (full treatment in `04-actors.md`, §5). The orchestrator,
running, is *performing the search* — and you are paying for it anyway. So harvest it:

1. **Orchestrator at the seam** — expensive per run, but searching.
2. **Observe which coordination decisions recur** — recurrence is the signal an encoding will
   amortise.
3. **Harvest the recurring ones into the encoded seam** — and **simultaneously add a mechanical
   check on the seam** (the matched-pair rule, below).
4. **The orchestrator's judgment shrinks to the residual** — the genuinely novel coordination.
5. Repeat. Each cycle the seam gets cheaper per run and the residual smaller and more valuable.

The asymptote is the floor (`03`): coordination decisions whose acceptance predicate does not close,
where an actor must stay at the seam permanently — which is the correct place for judgment.

### The matched-pair invariant

> **You may not move seam demand from judgment to encoded without simultaneously allocating a
> mechanical check on the seam.**

The orchestrator's judgment was *silently absorbing the exceptions*. Encode the rule, remove the
orchestrator, and nobody catches them — they escape. This is not a safety nicety; it is the principle:
the demand the orchestrator was carrying has to land somewhere, and if it doesn't land on a check, it
lands in escape.

**This is what the thymus is.** The immune system's encoded seam (bind-and-proliferate) is dangerously
general, so a dedicated mechanical check (negative selection) polices what the rule produces. The
encoded seam and its check are a matched pair.

---

## The channel is the platform

Having a judgment store and an encoded store **is not enough.** Two stores with no channel between
them means the expensive discoveries evaporate. The compound requires a **write-back path** from
judgment into encoding, and an **inheritance path** from encoding to the next run.

- **Vertebrate immunity** has judgment and encoding and **no channel** (the Weismann barrier); its
  memory is a *cache*, dying with the individual.
- **CRISPR** has all four parts — judgment (survive a phage) → harvest (spacer filed in an
  inheritable array) → inheritance → cheaper next encounter, across the population. **The compound
  platform.**
- **A vaccine** is that channel *built externally*, because the germline would not carry it.

> **The channel is the platform.** Not the graph, not the ledger, not the orchestrator — the
> write-back path from judgment to encoding, and the inheritance path from encoding to the next run.

---

## The one line

> **Decomposition manufactures demand at the seam; the seam allocates across the same four stores;
> and the compound is what you get when you build the channel that harvests seam-judgment into
> seam-encoding — with a check, always, on what you harvested.**
