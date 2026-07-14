# Adversarial Ground

> **Core — normative topic chapter.** [Ground](00-determination.md#the-two-primitives) is what a determination reads to resolve a choice — which makes it an attack surface, and a maintenance liability, whenever the actor does not control it. This chapter states the encode/verify split that governs uncontrolled ground, and then retreats — deliberately — from a unification the framework once claimed and should not.

## The encode/verify split

> **You can encode ground you control. You must mechanically verify ground you don't.**

The [encoded store](00-determination.md#the-four-stores) works by freezing a determination upstream. That only holds if the ground the determination was made against holds still. For ground the actor controls — its own schema, its own invariants — freezing is sound: you authored it, and it changes only when you change it. For ground the actor does *not* control, freezing is a bet.

Any uncontrolled ground is really **two facts**, and they must not be conflated:

- **Your copy** — pinned, local, inspectable, and **stale-able.** It is what you froze at authoring time.
- **The source of truth** — remote, mutable, authored by someone else, and free to move after you froze your copy.

A lockfile pins the first and **cannot pin the second.** A pinned dependency version, a cached API response, a snapshot of a config store — each is your copy, and each can silently disagree with the source of truth the moment the source moves. So uncontrolled ground cannot be discharged into the encoded store and forgotten; its share of the determination must be **mechanically verified against the source at the time it matters** — a contract test re-run against a moving source of truth.

> **You cannot amortise an observation of something you do not control.** Each act requires its own observation. That cost is irreducible.

This is the [closure principle](closure-principle.md) seen from the ground side: consuming your pinned copy as if it were the source of truth is consuming a prior determination as ground, and the loop has no corrective term until you go and look. The [end-to-end argument](05-lineage-and-limits.md#15-saltzer-reed-clark-the-end-to-end-argument-1984) says the same thing about where the check belongs: the verification has to sit at the boundary where the uncontrolled ground actually enters, not at some convenient upstream layer that froze a copy of it.

## Ground as attack surface

If a determination reads ground, then whoever controls that ground controls the determination. This is not a metaphor. **Prompt injection is exactly this:** an attacker who can write into the ground a model reads — a retrieved document, a tool result, a summarised history — is authoring the model's determination, because the model cannot distinguish ground it was given from ground that is true. An orchestrator whose coordination ground can be poisoned is a [single point of authorship](04-actors.md#43-the-orchestrator-is-the-poisoned-ground-target), which is why a mechanism-at-the-seam has no such centre and an actor-at-the-seam does.

The defence is the same encode/verify discipline, applied adversarially: ground you control (and can therefore trust) is encoded; ground you do not control (and therefore an adversary might) is verified before it is allowed to steer a determination. The question *"who authored this ground?"* is a security question, and the framework makes it a first-class one.

## The retreat: a family, not one mechanism

The framework once claimed a **cross-domain unification** of poisoned ground — that time-of-check/time-of-use races, molecular mimicry, autoimmunity, estimator divergence, and prompt injection were *one mechanism*. That claim is **retreated**, and the retreat is the honest move.

They are not one mechanism. The error directions alone are opposite:

- **TOCTOU** (concurrency) — the ground was valid when checked and invalid when used; the failure is *atomicity*, a gap in time.
- **Molecular mimicry** (immunology) — a **false negative**: foreign material read as self, and admitted.
- **Autoimmunity** — a **false positive**: self read as foreign, and attacked.

Grouping opposite error directions under one label was **apophenia** — the [universal-solvent failure mode](00-determination.md#the-admission-tests-the-discipline-that-keeps-this-a-law) the admission tests exist to prevent, arriving as a satisfying pattern. A false negative and a false positive are not the same defect because they both involve "ground," any more than a shared shape is a shared cause. The resemblance is real; the mechanism is not shared.

What survives is a **family**, and only a family:

> Poisoned ground is a *family* of failures unified only by **the actor's model of the ground having diverged from the ground.** The *direction* and *mechanism* of divergence differ by domain and must not be conflated.

Each remains a genuine instance of *"verification and use are separated, and the substrate is not what the actor believes it is."* But the instrument that catches a TOCTOU race (atomicity, locking) is not the instrument that catches molecular mimicry (a tighter negative-selection threshold) is not the instrument that catches prompt injection (provenance and verification of read ground). Keep them as separate instances; stop claiming they are the same thing. The correction is recorded in full in [Lineage and Limits §4](05-lineage-and-limits.md#24-a-note-on-retreats-carried-by-other-forks).
