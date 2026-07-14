# The Closure Principle

> **Core — normative topic chapter.** One determination the framework makes so often it earns its own statement: what happens when an actor reads its own prior output back in as ground. It is the [escaped store](00-determination.md#the-four-stores) at its most dangerous, because the defect wears the markings of a sound inference. Its rigorous ancestor is Kalman.

> **An actor's own prior output is not ground.**

[Ground](00-determination.md#the-two-primitives) is what a determination is made *against* — the world, the source of truth, the substrate the actor does not author. An actor's own prior output is not that. It is a determination the actor already made, and reading it back in as if it were ground closes a loop with **no corrective term.**

## Why the loop diverges

A determination made against real ground has a correction path: if the actor's model of the world is wrong, the world pushes back — the reading disagrees, the test fails, the source of truth contradicts. Consuming a cached belief as ground removes that path. The actor is now making determinations against its own model of the ground rather than the ground, and nothing in the loop can tell it the model has drifted.

Failures of this kind are **correct inferences over false premises.** The reasoning is sound; the ground was not ground. So the output is not confused or hedged — it is **confident, well-reasoned, and catastrophic**, because fluent correct-looking inference over a poisoned premise is exactly what the actor is good at. This is the [escaped store](00-determination.md#the-four-stores) surfaced as output: a decision that was made by nobody — nobody re-observed the ground — arriving dressed as a decision that was made well.

## This is estimator divergence (Kalman)

The principle is not new; it has theorems, and they belong to control theory. An estimator that trusts its own model over its measurements **diverges**: the covariance it reports can shrink toward zero — the estimate looks ever more certain — *while the actual error grows.* This is **filter divergence / observability failure**, and the remedy is the [separation principle](05-lineage-and-limits.md#16-kalman-control-theory-observability-and-estimator-divergence-1960s) made concrete: keep estimation anchored to measurement.

Cite Kalman. Filter divergence is the rigorous ancestor of this principle, and it has what the framework otherwise lacks — conditions under which divergence provably occurs. What the framework adds is only a **name and a generalisation across actor kinds**: the same divergence for a program with a stale cache, a model consuming its own summaries, a human consulting their mental model of the system rather than the system, an organisation acting on a report of the market rather than the market. One mechanism, many actors.

## The remedy is always the same

> **Go and look.**

Wherever a determination matters, re-observe the ground rather than consuming the last determination made against it. This is why an [uncontrolled ground](adversarial-ground.md#the-encodeverify-split) cannot be amortised: each act requires its own observation, because the only thing that closes the loop's corrective term is a fresh reading of the world. A cache is a bet that the ground has not moved; the closure principle is the reminder that when the bet is wrong, the actor will be the last to know.
