# Determination

> **Core §0 — normative.** The foundation the rest of the framework stands on: the two primitives, the admission tests that keep them honest, and the four stores where a determination can live. [The Law](01-the-law.md) conserves the demand these primitives generate; everything after measures, bounds, or indexes it. **Start here.**

Decision-Driven Design has two primitives and one discipline. Name them first, because every later claim is machinery for keeping them.

## The two primitives

> **Decisions** — the things determined.
> **Ground** — what they are determined against.

Every determination reads ground to resolve a choice. There is no third thing. A decision consumes ground as input and contributes constraint as output; ground is the substrate a decision is made *against* — the target's distance, the wind reading, the repo's state, the source of truth.

**The act is a decision.** There is no floor of "pure action" beneath the decisions — no privileged layer where something happens that is not itself a determination. What we are tempted to call *the act* is just the last decision in the chain, the one whose output is an effect on the world rather than an input to a further decision. This matters because it is what lets the framework quantify over everything uniformly: firing the rifle, emitting the token, committing the write are all decisions, differing only in where they sit in the chain and what ground they read.

An **actor** is anything that makes decisions against ground. The framework quantifies over all actors and hard-codes none — a human forecasting from knowledge in the head, a model forecasting from knowledge in its context, a classical program replaying decisions its author pre-made, an ensemble whose choice lives in the seam between its members ([Actors](04-actors.md)). What kind of thing is deciding never enters the primitives; it enters only when we ask *where the determination can live* and *what it costs to move it*.

## The admission tests — the discipline that keeps this a law

A framework that explains everything forbids nothing and is worthless. The two primitives earn their keep only because there is a sharp test for membership in each, and **the tests are allowed to fail things.**

> **A choice is a decision iff varying *the choice* moves the outcome past tolerance.**
>
> **A fact is ground iff varying *the world* moves the outcome past tolerance.**

Both tests are relative to a declared assurance tolerance — that is what makes them decidable rather than rhetorical, and it is the same parameter the [law](01-the-law.md#the-demand-is-denominated-in-decisions) uses to bound the governing decision set.

**These must be allowed to fail things.** A rock does not decide where to land — vary its "choice" and nothing varies; it has no choice to vary. A quark does not determine — it inspects no substrate, and quantum indeterminacy is a probability amplitude, not a choice read against ground. A muscle-fiber recruitment is not a governing decision at any assurance a shooter declares, because varying it inside the trained envelope does not move the outcome past tolerance. **If everything passes, the framework forbids nothing.**

*This is the framework's primary defence against becoming a universal solvent, and it only works if it is enforced against claims you would like to be true.* The temptation is always to admit a resemblance — a quark "deciding," a market "determining" — because the resemblance is real. The resemblance is [degeneracy](05-lineage-and-limits.md#6-required-citations): many-to-one maps recur across mathematics and nature, and a shared shape is not shared mechanism. The admission tests are how the framework refuses the flattering over-extension.

## The four stores

Given that a choice is a decision — it passes the first test — where can the thing that determines it live? There are exactly four answers, and they exhaust the space because they are the four answers to *who made this decision.*

| Store | Form | Property |
|---|---|---|
| **Encoded** | constraint, before the act | extra-actor · amortises · cheap to state, **expensive to find** |
| **Mechanical** | criterion, after the act | pays the **executability tax** · cheap to trust |
| **Judgment** | per-run, by an actor reading ground | does not amortise · walks out the door |
| **Escaped** | decided by nobody | defect exposure · **the only forbidden state** |

- **Encoded** — the decision is pre-made upstream, frozen, transmitted in the act's input in a form the executing actor consumes. Paid once, amortised over every run. Cheap to *state* once found; the cost is in the *finding*.
- **Mechanical** — the decision is delegated to the executor, but its outcome is gated by an encoded acceptance criterion applied after the act, evaluable without any actor's discretion. It pays an executability tax (the criterion must be made to run) and is cheap to trust (it needs no actor's word).
- **Judgment** — the decision is made per run, by a designated accountable actor reading ground, from knowledge that is not encoded. It does not amortise — it is paid in attention every run — and it walks out the door with the actor.
- **Escaped** — the decision is made by nobody: it falls to a prior, a default, chance, or physics, and is thereby transferred to the user as defect exposure. **It is the only forbidden state.**

**{rule, check, actor, nothing} — there is no fifth source.** A decision is covered by a rule (encoded), a check (mechanical), an actor (judgment), or nothing (escaped). That is the partition [the law](01-the-law.md) conserves demand across.

**Status: this is a definitional partition. It cannot be false.** It is **ergonomics, not a discovery**, and must be claimed as such — the value is that it turns a vague quality conversation into an allocation audit, not that it reveals a hidden truth. The one genuine addition over prior art is the **escaped** store: naming *"decided by nobody = latent defect exposure"* as first-class. Tesler's Law of Conservation of Complexity has the other three (user, developer, platform → judgment, encoded, mechanical); it does not have the bin where nobody decides. Full attribution and the corrections that produced this framing are in [Lineage and Limits](05-lineage-and-limits.md).

## The register: Principle, not physical Law

The framework's central claim ([the law](01-the-law.md)) is that determination demand is conserved across these four stores. The word "Law" for it is used the way *Tesler's Law* and *Ashby's Law* use it — engineering homage, not a claim of physical-law status. A physical conservation law names a quantity invariant under a symmetry and measurable in principle; we have named no such quantity and derived no invariance, so the honest register is **Principle**. Stated in full it is **the Conservation Principle of Determination Demand** — Tesler's Law generalised, denominated in decisions, extended with the escaped store, and parameterised on assurance level. The lineage (Ashby, Tesler, Brooks, Meyer, Kalman) and the falsification debt this register still owes are set out in [Lineage and Limits](05-lineage-and-limits.md).

## What the rest of core does

- [**The Law**](01-the-law.md) conserves the demand these primitives generate: for a task at an assurance level, determination demand is constant and allocated fully across the four stores. It adds the environment clause (why software is *closable*) and the two design principles that guard the input and output boundaries.
- [**Completeness**](02-completeness.md) is the instrument that reads the allocation — everything not encoded, priced.
- [**The Polanyi Floor**](03-the-polanyi-floor.md) bounds it: the boundary below which a determination cannot move from judgment to encoded. Its sharpened form — *the floor is in the acceptance predicate* — lives in [Actors §2](04-actors.md#2-the-floor-is-in-the-predicate).
- [**Actors**](04-actors.md) supplies the parameter the primitives leave open: the pinning-resolution spectrum, the floor's true location, selection versus training, and how composite actors carry seam demand.
- [**Lineage and Limits**](05-lineage-and-limits.md) is the ledger — what the framework stands on, where it was corrected, where it retreated, what it owes.
- [**Determination and Intelligence**](06-determination-and-intelligence.md) draws the boundary the primitives imply: a thermostat determines and is not intelligent, so determination is necessary and nowhere near sufficient — and the framework is orthogonal to intelligence by construction.

Two determinations recur often enough to earn their own chapters: [**an actor's own prior output is not ground**](closure-principle.md) (the closure principle), and [**ground is an attack surface**](adversarial-ground.md) (adversarial ground).
