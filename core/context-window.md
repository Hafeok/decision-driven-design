# The Actor's Capacity: Context Length as Allocation Budget

Core §N — normative. A property of the law read against one actor type. The Conservation of Specification law quantifies over all actors and hard-codes none; this section works out what the law's four stores cost *physically* when the actor is a language model. The result is that context length is not a performance parameter but the size of the actor's total allocation capacity for a single action — and from that, both the model-size choice and the maximum action size follow as theorems rather than heuristics.

## The stores have a location

The law says demand allocates across four stores: encoded, mechanical verification, judgment, escaped. It says where each store lives *logically* — encoded is in the input, judgment is in a designated head, and so on. It does not say what those stores cost as physical resource, because for most actors the question is uninteresting: the stores occupy separate media that do not compete.

For a human, the encoded store lives on paper or screen, the sensed facts live in the environment being inspected, and judgment happens in the head. These are three different physical places. Loading more onto the checklist does not shrink the room available for thinking; reading more of the environment does not consume the checklist. The human's stores are spatially independent.

The model actor is peculiar, and the peculiarity is the whole subject of this section: **for a language model, three of the four stores occupy the same finite resource — the context window.** The encoded specification transmitted to it, the facts it senses at fire time, and the working room in which its per-run judgment actually happens are all resident in one space, and they compete for it.

This is what context length measures. Not speed, not quality — **capacity**. The context window is the model-actor's total allocation budget for a single action: every store's share, for that action, must fit inside it at fire time, because that is where the stores physically are.

## Two consequences, both derivable

Once context length is named as the allocation budget, two things that looked like operational lore become theorems.

### Why explore mode wants a long context

Explore mode runs a high judgment share by construction — the exploring actor makes governing decisions per run, against an intent, rather than replaying decisions pre-made upstream. For a model, judgment *is* computation over what is in the window: the width to sense facts, hold intermediate decisions, and steer toward the intent all consumes window space as the exploration proceeds.

So explore mode is judgment-store-hungry, and context length is exactly the budget for that store. A long context buys explore-width. A short context forces the opposite trade: with no room to carry judgment live, the specification must be pre-paid — the flow engineered, the decisions frozen up front — because there is nowhere to make them at fire time.

This reframes the model-size choice precisely. You do not reach for a large model in explore mode because it is *smarter*. You reach for it because **explore mode's allocation is judgment-heavy, and judgment is window-resident.** The large model's contribution is capacity for the judgment store, not raw capability. Where the demand permits the specification to be pre-paid, a small model suffices — not because the task got easier, but because the allocation moved out of the window and into frozen encoding.

### Why context length bounds action size

This is the load-bearing result. The law fixes the demand by task and assurance level. For a model actor, the *entire* demand — every window-resident store's share — must fit in the context at fire time, because that is where those stores live. Therefore:

> An action is executable by a model actor only if its total window-resident specification demand fits the model's context.

Context length is the maximum action size the actor can take. This is not a soft limit that degrades gracefully; it is the physical boundary of what one action can demand of one model.

This gives the funnel a physical reading, not merely a conceptual one. As work pushes toward the value action, constraint density rises monotonically — and the encoded share of a single action's demand can exceed the window even while the decision count stays finite. Decomposing the funnel into smaller actions is therefore not only cleaner design; it is **the mechanism for keeping each action's demand under the actor's context bound.** The funnel is how a finite-capacity actor takes an action whose full-fidelity specification would not fit in one window: split it until each sub-action's demand fits.

The window is a single budget, but it resolves into two independently-bound stores once the actor's architecture is pinned: reach (total parameters) and resolution (active parameters). See [Model-Actor Capacity](../apparatus/model-actor-capacity.md) for the decomposition and its escape-split prediction.

## Conservation, spatialized

These two results connect into something the law had not previously exhibited. Engineered mode and explore mode make *opposite trades against the same window*:

- **Engineered mode** spends window on encoded specification and leaves little judgment room. Small judgment share — so small models suffice — but the specification was paid up front and occupies the window as encoding.
- **Explore mode** leaves the window empty of encoding and spends it on judgment. Needs the large window — but the specification was deferred, not paid.

Same finite resource, allocated to opposite stores. This is the Conservation of Specification showing up as a *spatial* constraint inside a single actor at a single moment. Everywhere else in the framework the conservation is temporal (maturation — allocation over recurrence) or positional (the funnel — allocation over position in a chain). Here it is neither: it is conservation across the physical capacity of one actor, at fire time. The two established projections are joined by this third reading — the law measured not over time or position but over the actor's own capacity.

## The escape valve is spatial, and so is the trap

One store costs no window: **escaped.** An unowned decision — one that falls to a prior, a default, chance, or physics — consumes no context, because no store holds it. This is quietly grim. Under context pressure, escape is the *cheapest store spatially*, so a model near its context bound will structurally tend to escape decisions rather than encode or judge them, unless something forbids it.

This is a mechanism, derivable straight from the law, for *why* under-specification happens under context pressure. It is not carelessness; it is the actor's stores competing for a resource and the only free store being the one that ships defects to the user. The completeness gate (Principle 2) is what forbids the cheap path: it refuses to let an effect commit through a specification with unpriced escape, regardless of how tight the window is. The gate is, among other things, a defense against the spatial incentive to escape.

## The open seam: is mechanical verification window-resident?

Three stores compete for the window. The fourth priced store — mechanical verification — may not, and resolving this changes a design consequence.

The claim to test: the mechanical-verification acceptance predicate is evaluated *outside* the window. It runs on the output, after the act, as a separate check — not in the actor's context. If so, mechanical verification is the model's **escape valve *from* the context bound that is not escape itself**: the way to push demand out of the window without pushing it into the escaped store.

That would be a real and specific design consequence. Under context pressure, the correct move is to relocate demand to mechanical verification — not to judgment (which costs window) and not to encoding (which costs window) and not to escape (which costs the user). Mechanical verification would be the only store that both relieves the window *and* stays on the ledger. It converts a spatial problem into a post-hoc check, which is exactly what you want when the actor is capacity-bound.

The seam to resolve before this sets: whether any part of the predicate is necessarily window-resident. A predicate the actor must *consult while acting* (as opposed to one applied to its finished output) would compete for the window after all, and the escape-valve reading would hold only for the strictly post-hoc portion. The likely resolution: mechanical verification splits by binding time exactly as context does — a post-hoc predicate is out-of-window and relieves the bound; any in-flight check the actor consults is window-resident and does not. This mirrors the frozen-context / sensed-context split and would keep the account uniform.

---

## Placement note

This section belongs after the four stores are established and after the environment clause (which introduces binding time and the frozen/sensed split), because it reuses both: the window-resident/out-of-window distinction is a binding-time distinction on physical space. It belongs before or alongside the funnel projection, since it supplies the funnel's physical necessity (decomposition as capacity management). It is core, not apparatus: it is a property of the law under one actor type, not a mechanism for running the law against a domain.
