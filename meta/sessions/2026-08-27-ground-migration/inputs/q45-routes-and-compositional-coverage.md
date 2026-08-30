# Holding note entry — Q45: closing an open verdict, and compositional coverage

**Status:** holding. Claude-drafted from the 2026-08-26 working conversation (Emil's material: the
proxy/method-supply disjunction, and the product company closing the loop through a closed
architecture). Extends the 2026-08-26 addendum and Q44. Nothing filed.
**Blocked by:** the ground migration, as with Q40–Q44.

---

## Q45 — Three routes, and what makes the second one scale

### (a) The trichotomy

**Proposed.** An open verdict — one whose acceptance relation cannot be stated — has exactly three
dispositions, and canon currently names only the third clearly:

| Route | What it does | Supply | Position |
|---|---|---|---|
| **1 — Write a proxy** | Keeps the determination at the verdict; substitutes a checkable criterion for the uncheckable one | assurance by check | after the act |
| **2 — Supply the act ontology** | Relocates the determination out of the verdict into the method; the open question is never posed | encoded | before the act |
| **3 — Carry it by the actor** | Leaves it open and trusts a qualified resolver | occasioned, carrier-borne | at the act |

Route 3 is the status quo and the only one that never amortises. Routes 1 and 2 are both conversions
of occasioned assurance to standing, at different loci — which makes this the same shape as
*build the check or train the worker*, now applied to the verdict rather than to the assurance.

**Falsifier:** an arrangement disposing of an open verdict by a mechanism that is none of the three
— neither a substituted criterion, nor a specified method, nor a trusted resolver.

### (b) They fail differently, and the second failure is less discussed

**Route 1 fails by divergence.** Both crescents of the proxy result: good work the check rejects,
and work that passes without being what was wanted. Optimising against the proxy widens the second.

**Route 2 fails by foreclosure.** You get exactly what the method produces, *including where the
method is wrong for this instance* — the carpenter cutting the specified joint on wood that needed a
different one. Nothing rejects it; the specification was followed.

**The trade, stated:** route 1 exchanges fidelity for checkability. Route 2 exchanges adaptivity for
determinacy. Neither is free, and an arrangement that has taken route 2 everywhere has bought
predictability by removing its own ability to notice a novel case.

### (c) Route 2's precondition

**Proposed.** Route 2 requires that the act ontology **actually determine** the verdict in that
domain — same method, same outcome. Where it does, specification works and has for centuries:
surgical checklists, GMP, building codes, traditional craft.

Where the same method yields varying outcomes — diagnosis, negotiation, design — no amount of
specification closes the verdict, and attempting it produces confident wrong work rather than
refusal.

**Falsifier:** a domain with demonstrably variable outcomes under fixed method where full method
specification nonetheless closes the verdict.

### (d) Compositional coverage — the property that makes route 2 scale

**Proposed, and this is the entry's centre.**

Route 2 appears expensive: specifying the method for a large verdict space looks like specifying
everything. It is not, when the act ontology has **compositional coverage** — a *small closed* set
of primitives whose *compositions* span a large verdict space.

The test is what happens when a new requirement arrives:

- **Without compositional coverage:** a new requirement is a new architectural decision. The act
  ontology grows with the verdict space, and route 2 costs what it appeared to cost.
- **With compositional coverage:** a new requirement is a new *composition* of existing primitives.
  The act ontology stays closed while the verdict space it reaches keeps expanding.

**This is what makes an act ontology a standing asset rather than a growing liability**, and it is
the property being selected for when an arrangement commits to one architecture across engagements.

**Falsifier:** an act ontology committed to across many engagements whose size grows in proportion to
the verdict space it serves — compositions failing to absorb new requirements.

**Two limits, both necessary.** Compositional coverage is **domain-relative**: a primitive set spans
some domains superbly and others badly, so the claim is about the fit between primitives and domain,
never about primitives being good in themselves. And the closed set still forecloses per (b) — where
composition reaches a requirement awkwardly, the requirement is met *badly* rather than refused,
which is the failure mode that looks like success.

### (e) The refusal asymmetry — why route 1 closes for a product company

**Proposed, downstream.** The proxy result assumes the target is fixed and external. A party that
owns **both** the what and the how does not face a fixed target: it can decline the requirements its
architecture expresses badly. The proxy then stops standing in for something outside it and
approaches a definition — which is why route 1 can close for a product company and cannot for a
practice taking the *what* as given.

**Consequence for a consultancy:** the loop closes only where the closed set composes to reach what
was asked. Where it does not, the choice is to break the architecture or renegotiate the
requirement, and **that boundary is where amortisation stops.**

**Recorded interaction:** a sector-scoped verdict ontology (Q44(c)) buys partial refusal — *that is
not how this sector does it* is a defensible decline in a way *our architecture cannot* is not. So
sector specialisation and compositional coverage are complements: one supplies partial refusal, the
other supplies reach.

---

## Routing

| Piece | Destination |
|---|---|
| (a) the trichotomy | Q-wave, upstream — it enumerates dispositions of an open verdict |
| (b) the two failure modes | With (a); (b)'s foreclosure half is new and belongs upstream |
| (c) route 2's precondition | With (a) |
| (d) compositional coverage | Downstream economics — it is an amortisation property |
| (e) the refusal asymmetry | Downstream; and the consultancy half is business record, not canon |

**Not canon, per the 08-26 addendum's section D:** which architecture a practice commits to, and
whether to own the *what*. Both are commercial decisions that *use* (d) and (e); neither is a claim
about determination.
