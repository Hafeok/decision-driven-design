# The Conservation Principle of Determination Demand

**Read `00-determination.md` first.** It establishes the two primitives (decisions and ground)
and the admission tests. This document states the principle those primitives obey.

---

## Register: this is a principle, not a law

A conservation *law*, in the sense physics uses the word, names a quantity that is invariant under
a symmetry and **measurable in principle**. We have no such measure. "Determination demand" has no
unit — unlike Ashby's variety, which is counted in bits.

So this is a **principle**, in the sense of *Tesler's Law of Conservation of Complexity* and
*Ashby's Law of Requisite Variety* — both of which use "law" as homage, and the more careful of the
two (Ashby) explicitly refused physical-law status even with a unit in hand.

> **We do not claim more than Ashby claimed with more than Ashby had. This is a principle. Where the
> word "law" appears in this repository, it is homage, and it is flagged.**

This matters because the framework's honesty about its own status is load-bearing (see
`meta/lineage-and-limits.md`). A principle that admits what it cannot prove is worth more than a
law that overclaims.

---

## The statement

> **For a task at a declared assurance level, and within a fixed decomposition of that task,
> determination demand is conserved.**
>
> Every governing decision gets made. The only choice is **by whom, when, and at what price.**
> Reduce the demand in one store and it **relocates**; it does not vanish.

Two qualifiers carry the whole weight, and both are concessions the review forced:

**"At a declared assurance level."** Two distinct variables live under this qualifier and must not
be fused: **tolerance** — which outcome deviations are acceptable — and **assurance** — the strength
of evidence that tolerance is met. The granularity bound is **tolerance-indexed**: a choice is a
governing decision iff varying it moves the outcome past *tolerance* (`00`, admission tests). Change
the tolerance and you change the set. Assurance then governs how much evidence the allocation must
carry — which is what `core/05` §7's tower is built on: **the tower is a tower of assurance
declarations, and the thing each declares is a tolerance.** Two systems can share a tolerance and
differ in required assurance. Without a declared tolerance the decision set is not even well-formed.

**"Within a fixed decomposition."** This is the important one. **Conservation holds within a chosen
task decomposition — not across decompositions.** Re-drawing the task boundary *relocates* demand
into the **seam** — the interface contract the decomposition brings into existence — where it is
pre-paid once and inherited by every run, rather than resolved per run (`core/09` §4). The total is
invariant under re-decomposition; what genuinely changes it is changing the task or the declared
tolerance, not re-drawing boundaries within one. So the principle is an accounting identity
*relative to a decomposition*, and **choosing the decomposition is itself the highest-leverage
governing decision** — not because it lowers the total, but because it sets how much demand is
pre-paid into the seam versus resolved, per run, in every part.

---

## The four stores

Every governing decision is determined by exactly one of four sources (`00`, §3):

| Store | Form | When | By whom | Property |
|---|---|---|---|---|
| **Encoded** | constraint | before the act | a rule | amortises · cheap to state, **expensive to find** |
| **Mechanical** | criterion | after the act | a check | pays the **executability tax** · cheap to trust |
| **Judgment** | — | during the act | an actor reading ground, **with an accountable party named** | does not amortise · walks out the door |
| **Escaped** | — | never | nobody | defect exposure · **the only forbidden state** |

**{rule, check, actor, nothing}.** There is no fifth source.

**Two roles, not one.** The judgment store names an **executor** — the actor that determines this
run — and an **accountable party** that bears the determination. For human actors these coincide,
which is why the earlier statement could fuse them without visible error. For model actors they
must be split: the model holds the judgment, a named accountability-bearing actor holds the
consequence (`core/05` §6). **A judgment allocation naming no accountable party is not an
allocation. It is Escaped with an executor attached.**

### This partition is definitional — and we say so

The four stores partition "who decides, and when" by construction: before / after / during / never,
crossed with someone / no-one. **It cannot be false.** It is therefore **ergonomics, not a
discovery** — a lens for design review, not an empirical claim.

The one genuine addition over the prior art (Tesler had three bins: user, developer, platform) is
the **escaped** store: naming *"decided by nobody = latent defect exposure"* as a first-class
category. That, and the assurance-level parameter, are the whole of what this partition adds. We
claim no more.

### The cost asymmetry between encoded and mechanical

These two stores are *not* interchangeable, and the difference is the reason both exist:

- **Encoded is cheap to author, expensive to trust.** Writing "prefer the smaller diff" is a
  sentence. Whether it is *correct* is unverifiable until something checks it.
- **Mechanical is expensive to author, cheap to trust.** A criterion must be *executable by a
  machine* — total, decidable, correct. You have to **build the thing that decides.** That is the
  **executability tax.** But once built, it fires, and you can trust it.

Every governing decision admits both forms — a constraint before, a criterion after. Redundancy is
permitted. Only **uncovered-and-unpriced** — escaped — is forbidden.

---

## Escape is the only store with no window cost

The four stores are not symmetric in one crucial way: **three of them cost something to occupy, and
one is free.**

Encoding costs authoring effort. Mechanical checking costs the executability tax. Judgment costs an
actor's capacity, per run. **Escape costs nothing at the moment of the decision** — you simply don't
make it. The bill arrives later, as a defect, when it is most expensive.

> **This asymmetry is why everything drifts toward escape.** A capacity-bound actor under pressure
> sheds decisions into the only store with no immediate cost. Humans do it under cognitive load
> (decisions collapse to habit); models do it under context pressure (decisions surface as
> hallucination); organisations do it under deadline (the decision "is our belief still true?" goes
> unmade).

The framework's central practical claim follows directly: **the job is not to reduce demand — you
cannot — but to make the allocation visible, and specifically to find the demand sitting in
escape.**

---

## What conservation buys, and what it does not

**It buys** a discipline: for every governing decision, ask which store holds it, and whether that
is the cheapest correct home at this assurance level. It makes *implicit risk nameable* — the
escaped store turns "we didn't think about that" into a category with a location.

**It does not buy** a measurement. There is no number. Until a counting procedure for governing
decisions exists and is shown invariant across two genuinely different architectures for one task,
conservation is an **accounting identity within a decomposition**, not a measured invariant. This is
booked as an open debt in `meta/lineage-and-limits.md`, and it is the single most important thing
the framework still owes.

---

## Lineage

This principle is a synthesis, not a discovery. Its ancestors, with what each supplied:

- **Tesler**, Conservation of Complexity — the nearest antecedent; "who deals with it" with three
  bins. We add the escaped store and the assurance parameter.
- **Ashby**, Requisite Variety — the *measurable* ancestor (variety in bits); the conserved-quantity
  intuition, done rigorously, which we do not match on measurement.
- **Brooks**, essential vs. accidental complexity — "fixed by the task, invariant to tooling."
- **Meyer**, Design by Contract; **Hoare** logic — the encoded + mechanical stores, formalised
  decades earlier and more precisely than here.

Full attribution and the corresponding retreats: `meta/lineage-and-limits.md`.

---

## The one line

> **Every governing decision gets made. The only forbidden outcome is the one made by nobody. The
> total is fixed by the task within a decomposition — so the decomposition is the decision that
> matters most.**
