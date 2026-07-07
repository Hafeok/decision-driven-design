# Applications

> **Non-normative examples.** Worked applications of the specification to concrete domains. Examples illustrate the framework but do not extend it; new general claims discovered through application are promoted into the spec (see "The promotion rule" below).

Worked applications of Decision-Driven Design to concrete domains.

The framework documents in [`core/`](../core) and [`apparatus/`](../apparatus) define DDD in the abstract. This section does the opposite: it takes a real, messy practice and shows DDD applied to it — what the framework's abstractions become in that domain, what the application buys, and what it costs. The README's standing claim is that the strongest pressure on the framework has come from applying it past its origin; this is where that pressure is written down.

## What an application is

Each application takes one domain and traces DDD through it end to end: the processes and their value actions, the roles and artifacts, the task decomposition, the points where the domain pushes back on the framework. An application is *use*, not *theory*.

## The promotion rule

An application applies the existing framework. If applying it to a domain forces *new* framework — a new entity, a new invariant, a new general claim — that material does not stay in the application. It is promoted into `core/` and `apparatus/` (where it is stated in the abstract, for every domain), and the application references it.

This keeps the two honest and separate. `core/` and `apparatus/` is the framework; `/applications` is evidence the framework carries weight. A reader should be able to tell, from where a thing lives, whether it is a general claim or a domain illustration. When an application leans on something general, it links to the spec rather than restating it.

## Status discipline

Applications are marked for what they are. A *projected* application is a clean derivation not yet exercised by a running system — valuable as a design, but conjecture. A *reported* application describes something a real system has actually run. The distinction is stated up front in each doc, because a framework in love with its own generality is a failure mode, and the cheapest guard against it is to never let a projection read as a result.

## Applications

- [**The software development lifecycle**](sdlc.md) — *projected.* Code generation under DDD: the steered coding agent dissolving into typed task clusters, the classify-and-dispatch gate, the broad worker as explorer-and-typifier, and the maturation toward a standard-task catalog. The first application, and the one the reference implementation (product-cli) is being built against.

Planned, as they get pressure-tested: non-engineering work management (the household/family stress test), robotics sensing (strategic layer only), game AI (decision layer only).
