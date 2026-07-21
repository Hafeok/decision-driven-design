# Decision-Driven Design

**A theory of where determinations come from, what they cost, and which actor should make each one.**

Version 4.0. This release adds the theoretical layer beneath the framework — and, following an
external adversarial review, corrects and downgrades several claims that the earlier versions
overstated. It is deliberately **smaller and better-attributed** than v3, and harder to knock down.

---

## Start here: the one idea

Four classical results govern how work is allocated in engineered systems — Brooks's essential
complexity, Tesler's conservation of complexity, Ashby's requisite variety, Meyer's contracts. Each
quantifies over an **actor**: the thing that makes a determination against some ground. **None of them
makes that actor explicit.** They had no reason to — for the whole history of these results there
were two kinds of determiner, a person or a program, and the gap between them was a light switch, not
a spectrum.

A third kind now exists: **non-deterministic, yet with a distribution that can be frozen by binding.**
Decision-Driven Design is what you get when you **fill in the actor slot** those results left empty —
and discover that supplying the missing parameter *changes their predictions.*

Two consequences follow, and they are the framework's core contribution:

1. **The irreducible floor of a task is a property of its *acceptance predicate*, not of the task.**
   Zero where you can check the answer; non-zero where you cannot; and *whether you can* is, in
   general, undecidable. → [`core/03-the-floor.md`](core/03-the-floor.md)

2. **Selection intensity is inversely proportional to acceptance-predicate closure.** *Training* is
   what you do when you can check the work. *Selection* is what you do when you cannot — you check the
   worker instead. This is falsifiable across professions.
   → [`core/04-actors.md`](core/04-actors.md)

And, new in 4.1: for tasks whose acceptance predicate closes, **specification demand is measurable** —
it is the Shannon entropy of the verdict, and conservation is the chain rule of entropy
([`core/08`](core/08-the-measure.md)). The measure exists exactly where the predicate closes, and
vanishes precisely at the floor.

And a prediction: **model actors outperform human actors exactly where the acceptance predicate
closes, and underperform exactly where it does not — the gap tracks *closure*, not *difficulty*.**

---

## What this is, and is not

**It is** a two-primitive theory (decisions, and the ground they are determined against), an
allocation lens (four stores: encoded, mechanically checked, judged, escaped), and an actor model
(pinning resolution, the floor-in-the-predicate, seam composition).

**It is not** a new physical law. The conservation claim is **Tesler's Law of Conservation of
Complexity, generalised** — denominated in decisions, with a fourth store (the *escaped* one Tesler
lacked) and an assurance-level bound. It has **no measurable unit**, so it is a **principle**, not a
law, and the repository says so throughout. See [`core/01-the-principle.md`](core/01-the-principle.md)
and, for the full record of what was corrected and why,
[`meta/lineage-and-limits.md`](meta/lineage-and-limits.md).

We publish the review and the retreats as first-class documents. A framework that states what it
cannot support is worth more than one that overclaims.

---

## Reading order

### Core — the theory

The claim, from primitives to consequences. Read in order if you are new.

| | Document | What it establishes |
|---|---|---|
| 00 | [`core/00-determination.md`](core/00-determination.md) | The two primitives; the admission tests; *the act is a decision* |
| 01 | [`core/01-the-principle.md`](core/01-the-principle.md) | The conservation principle; the four stores; the register question |
| 02 | [`core/02-completeness.md`](core/02-completeness.md) | Why the stores are exhaustive — and why that is worth less than it looks |
| 03 | [`core/03-the-floor.md`](core/03-the-floor.md) | **The floor is in the acceptance predicate** — the best original result |
| 04 | [`core/04-actors.md`](core/04-actors.md) | **The missing parameter.** Pinning; selection vs. training; seams; the compound |
| 05 | [`core/05-composition.md`](core/05-composition.md) | The seam-demand identity; orchestrator vs. swarm; the channel is the platform |
| 06 | [`core/06-determination-and-intelligence.md`](core/06-determination-and-intelligence.md) | Determination ≠ intelligence; why the LLM debate is structurally undecidable |
| 07 | [`core/07-projections.md`](core/07-projections.md) | The funnel & maturation as **judgment-demand** projections (not count); why the model's feedback loops appeared |
| 08 | [`core/08-the-measure.md`](core/08-the-measure.md) | **Demand is Shannon entropy of the verdict; conservation is the chain rule.** The counting-procedure debt, paid for closing predicates |

### Apparatus — the mechanisms

Operational results that fall out of the core. Read as needed.

| Document | What it gives you |
|---|---|
| [`apparatus/encode-verify.md`](apparatus/encode-verify.md) | *Encode ground you control; verify ground you don't* — and verify on a schedule |
| [`apparatus/closure-principle.md`](apparatus/closure-principle.md) | *An actor's own output is not ground* — poisoned ground, and why Terraform can delete your database |
| [`apparatus/adversarial-ground.md`](apparatus/adversarial-ground.md) | The attack surface of an actor is its ground, not its logic — across three fields |

### Applications — the projections

The framework, denominated in a domain.

| Document | Domain |
|---|---|
| [`applications/sdlc/`](applications/sdlc/) | Software delivery — the agentic/DAG design framework (formerly the whole of v3) |

### Meta — the honesty layer

| Document | What it is |
|---|---|
| [`meta/lineage-and-limits.md`](meta/lineage-and-limits.md) | Full attribution, corrections, retreats, and the open falsification debts |
| [`meta/consolidated-state.md`](meta/consolidated-state.md) | Single authoritative status: what stands, what is superseded, what is owed |

Danish glossary: [`i18n/ordliste-dansk.md`](i18n/ordliste-dansk.md).

---

## What changed from v3

v3 was the agentic-design framework: decisions as the unit of work, a DAG of roles, artifacts with
schemas, backed by [`product-cli`](https://github.com/Hafeok/product-cli). **That framework is
intact** — it now lives in [`applications/sdlc/`](applications/sdlc/) as the **engineering
projection** of the general principle, which is exactly what it always was. What v4 adds is the layer
*beneath* it: the theory that explains why the DAG design works, and the actor model that says which
node each determination belongs to.

The register also changed. Following external review:

- **"Law" → "Principle."** No physical-law status without a measurable quantity (which we do not have;
  Ashby did, and even he refused the term).
- **Conservation** holds as an accounting identity *within a fixed decomposition* — re-decomposing can
  *destroy* demand, so the decomposition is the highest-leverage decision.
- **The immune-system "licensing" argument** is demoted to a suggestive parallel with known
  disanalogies; **CRISPR** is the accurate compound-platform instance.
- **The zero-floor postulate** is retreated to **the floor-in-the-predicate** result, which is
  sharper and survives the theoretical limits (Rice, inevitable model error, collective tacit
  knowledge).

Full record: [`meta/lineage-and-limits.md`](meta/lineage-and-limits.md).

---

## Status

This is a working specification under active revision. The strongest claims — the floor-in-the-
predicate, and *selection intensity tracks predicate closure* — are **falsifiable**, and the
conditions are stated in the documents. The framework books its open debts openly
([`meta/`](meta/)); the most important is a counting procedure for governing decisions that would let
"conservation" be measured rather than merely asserted.

Reference implementation: [`product-cli`](https://github.com/Hafeok/product-cli) (the authoring layer
for the SDLC projection).

## Standing on

Tesler (conservation of complexity) · Ashby (requisite variety) · Brooks (essential complexity) ·
Meyer & Hoare (contracts) · Saltzer, Reed & Clark (end-to-end) · Kalman (observability) · Polanyi &
Collins (tacit knowledge) · Rice (undecidability) · Edelman & Gally (degeneracy). Full attribution in
[`meta/lineage-and-limits.md`](meta/lineage-and-limits.md).

## License

Spec text: **CC BY 4.0**. Any code and schemas: **Apache-2.0**.
