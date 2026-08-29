# Act ontology and verdict ontology

**Status:** working explainer, drafted 2026-08-26. Not canon, not filed. Written to be handed to a
session or a reader with no memory of the conversation that produced it.
**Formal entry:** the claim-shaped version with falsifiers is `Q44`. This document explains; that one
files.
**Blocked by:** the ground migration — *ontology*, *carving* and *determinables* are all in the
vocabulary under review, so the names below may move even where the distinction survives.

---

## 1. The distinction

Every act's governing decisions draw their distinctions from somewhere. The claim is that they draw
from **two different places**, and the framework has had one word for both.

**The act ontology** is the set of distinctions that govern **how the work is done**. Which tool, in
what sequence, by what technique.

**The verdict ontology** is the set of distinctions that govern **what the output must be**. What the
thing is, what makes it good, what makes it acceptable.

### The carpenter

Asked to build a chair, a carpenter holds two bodies of knowledge that do not overlap.

The first is about saws, planes, grain direction, which joint carries which load, what order to cut
in, how long glue takes. None of it is about chairs. It would be the same for a table.

The second is about chairs: what height, what a seat has to do to a body over three hours, what
counts as beautiful in this room, who is going to sit in it.

A brilliant carpenter with no idea what a chair is for builds something well-made and wrong. Someone
with excellent taste and no craft describes a chair nobody can build.

**Both are ontologies in the same sense** — declared sets of distinctions at a grain. What differs is
what they govern and, crucially, who else holds them.

### In software

- **Act ontology:** how a service is structured, how errors propagate, when to use a queue, what a
  handler may do. Shared with everyone doing this craft on this stack.
- **Verdict ontology:** what a valid referral is, when a claim may be paid, what makes a patient
  record complete. Shared with the customer's sector.

---

## 2. Why the distinction earns its place

Three things follow that neither half explains alone.

### 2.1 Method decisions can be unverifiable even when output is verifiable

A chair passes every inspection at handover and fails in two years because a joint was cut across the
grain.

The *output* predicate closed — you could check the chair. The *method* decision that determined its
life did not, and not because no criterion exists. The criterion exists; **its consequence arrives
after the verdict's horizon.**

So *can this be checked?* is **two questions**, not one — can the outcome be assessed, and can the
method be assessed — and they have different answers in the same act.

This explains, without appealing to culture or tradition:

- why craft traditions inspect the *worker* (apprenticeship, licensure) even where the product is
  inspectable;
- why code review exists at all — you cannot tell from a running program whether its error handling
  was right, and the consequence arrives later than any verdict rendered at merge.

### 2.2 The two ontologies are shared with different populations

This is what makes one a standing asset and the other an engagement:

| Layer | Shared with | Amortises over |
|---|---|---|
| How determination works at all | everyone | every arrangement |
| **Act ontology** | everyone practising that craft on that stack | every engagement the practice runs |
| **Verdict ontology** | everyone in the sector | every customer in that sector |
| **Tolerances and choices** | nobody | this customer, this engagement |

Put in the framework's own terms: **within a sector the determinables are largely shared** — which
dimensions matter is set by the sector. What is customer-specific is the **grain and the choice**:
how tight the tolerance, and which alternative was taken. Same axes, different declarations.

### 2.3 Sectors share because they share institutional ground

Not a coincidence of similar businesses. A sector has a common regulator, common standards bodies,
common certification, common professional norms — and those write the distinctions **once, for
everyone in it.**

Which predicts a gradient: the more institutionally governed a sector, the larger the shareable
fraction of its verdict ontology. Healthcare, aviation, finance high. Unregulated commercial software
low.

---

## 3. What divergence between them shows

Where the two ontologies do not line up, three distinct conditions arise:

| Divergence | Condition | What it looks like |
|---|---|---|
| Act has a distinction the verdict lacks | **Invisible craft** | The customer has no word for it, so cannot want it. Quality goes unpriced; two suppliers who differ are bought as identical; a cost cut here is undetectable at handover |
| Verdict has a distinction the act lacks | **Unbuildable requirement** | A stated want with no technique that reaches it. The honest form of "we cannot do that" |
| Both carve, differently | **False agreement** | Same word, two distinctions. Agreement is reached, work proceeds, the verdict later disagrees |

**The asymmetry is the diagnostic.** The first two produce *silence* — something unsaid, or something
refused. The third produces **confident agreement that is wrong**, and nothing in a normal engagement
checks it. Disputes over delivered work are disproportionately the third kind.

### The inspectable diff

The third condition used to be undetectable: both carvings private, the only evidence a dispute after
the fact.

When both are **declared**, it becomes a diff — the same term, two definitions, side by side, before
the work starts.

Two conditions on that, and they are what keep it real:
- both sides must declare, which a practice can supply for its own act ontology but must **elicit**
  for the customer's verdict ontology;
- a matching term *name* is not a matching distinction. The diff finds candidates; adjudicating them
  is judgement, with an owner.

### "We're special"

A customer saying this is reporting a **divergence from their sector's verdict ontology** — the only
part of their carving they can see, because nobody states what everyone shares.

It is therefore the most useful thing they say, and the productive response is neither agreement nor
scepticism but: **which decision does this change?**

- attaches to no decision → ceremonial;
- attaches to many → the engagement's scope.

And the ceiling runs the other way: the divergences they *cannot* name are the dangerous ones,
because those are the assumptions deep enough to read as facts. Their list is where elicitation
starts, not where it finishes.

---

## 4. Why this matters for delegation

A model has a **strong ambient act ontology** for software — it read the corpus of how software is
built — and **no verdict ontology** for a specific customer's domain.

So the supply pattern falls out:

- **inherit** the ambient act ontology;
- **state only the divergences** from it — where this practice does something the field would not;
- **supply the verdict ontology explicitly**, because nothing ambient carries it.

And one structural fact behind why the tooling works: **the act ontology is positional.** It attaches
to code structure — this method, this project, this type — which is what makes it deliverable
mechanically at the moment of the work. The verdict ontology is not positional and cannot be
delivered the same way.

That may be the reason a language-server-shaped delivery mechanism works on the act side and no
equivalent exists on the verdict side.

---

## 5. Assessing method, and why craft learns slowly

Assessing an act *against the act ontology* — was this the right technique, in the right order — is
itself an act of judgement, with its determinations drawn from the act ontology. No new machinery is
needed; the same rules that stop the regress elsewhere apply.

What is worth separating is **assessment from learning**. A method assessment yields a verdict about
*this act*. Learning is verdicts accumulating into what is encoded — and method verdicts update the
**act ontology itself** rather than any particular rule.

By 2.1 that signal arrives late, sparsely, and is frequently attributed to the wrong cause. Which
gives a mechanism for why craft improves more slowly than outcome-driven work, without appealing to
temperament or tradition.

---

## 6. The boundary case — architecture straddles

Some decisions govern both. *Should this be a service* is a method decision and an output property at
once.

**This is stated as a limit, not resolved.** A clean two-way distinction that quietly excludes its
hardest cases is exactly the defect that got a claim retired earlier this month, and the same
discipline applies here: the straddle files *with* the distinction, or the distinction does not file.

---

## 7. What is not claimed

Recorded so a later session does not inherit more than the argument supports.

- **Not that the two ontologies partition all decisions cleanly.** §6 is a live boundary case.
- **Not that the act ontology is complete or completable in general.** The claim about completeness
  is narrower: complete *for a given act*, because an act needs only the distinctions its governing
  decisions turn on.
- **Not that a declared ontology is correct.** It is *stated* and therefore inspectable. It remains a
  stand-in for the domain, and can be complied with perfectly while missing what was wanted.
- **Not a claim about which architecture, sector, or stack a practice should choose.** Those are
  commercial decisions that use this material; they are not part of it.

---

## 8. To carry into the next session

**Open questions:**
1. Whether *ontology* is the right word at all, given the framework already has determinables at a
   grain — and given the term is heavily loaded elsewhere. A naming ruling, best made against the
   registry after the migration rather than against intuition.
2. Whether the act/verdict split is orthogonal to the existing timing and supply partitions, or
   interacts with them. Untested.
3. Whether §3's three divergence conditions discriminate — the falsifier is whether competent
   readers can classify real disputes into them at better than chance.

**Where the formal version lives:** `Q44`, with falsifiers per part and routing per piece. `Q45`
extends it with the three routes to an open verdict and compositional coverage.

**And the standing constraint:** nothing here files before the ground migration settles the
vocabulary. The material is not lost by waiting; it is written down, with its falsifiers, and the
migration will tell it which words to use.
