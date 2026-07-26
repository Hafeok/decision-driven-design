# The Floor

**The framework's best original result.** It corrects an earlier, over-strong claim (a "zero-floor
postulate" that survived external review only in narrowed form) and replaces it with something
sharper and more useful: **the irreducible floor is a property of the acceptance predicate, not of
the decision.**

---

## The claim

> **The intrinsic floor is a property of the acceptance predicate, not of the decision.**
>
> **Zero** wherever the predicate is **closed for the arrangement over ground it can inspect** — and
> there, *path-degeneracy* makes it *robustly* zero: infinitely many structurally different
> determiners suffice, so **no *particular* judgment is required, only an *adequate* one.**
>
> **Non-zero** exactly where the predicate does not close — and **whether it closes is, in general,
> undecidable** (Rice's theorem).

The "floor" is the portion of a determination's demand that **cannot be moved off the in-the-moment
actor** — the residue that no amount of encoding or checking can amortise, that must be paid, per
run, in judgment.

The result relocates that floor. It is not a property of *how hard the decision is*. It is a
property of **whether you can check the answer.**

**Effective closure, defined.** A predicate is **closed for an arrangement** when the relevant
ground is observable and adequacy can be evaluated within declared resource, latency, and confidence
bounds. **Decidable** is reserved for the formal special case. Formal decidability is the wrong
instrument in both directions: any bounded finite domain is decidable by exhaustive lookup — making
practically open predicates formally closed — while a decidable checker may require infeasible time,
memory, observation or precision. Where precision is needed, decompose — logical decidability,
observational closure, computational feasibility, economic feasibility, assurance sufficiency — and
operational closure is the conjunction of whichever are relevant to the arrangement. This is a
strengthening, not a retreat: the framework has been using closure as an engineering property
throughout, and this makes the usage honest.

---

## Why the floor is in the predicate

Consider what each store requires:

- **Encoding** requires that you can state the constraint in advance.
- **Mechanical checking** requires that you can *decide*, after the act, whether the criterion is
  met — i.e. it requires the **acceptance predicate to be computable.**
- **Judgment** is what carries whatever the first two cannot.

If the acceptance predicate is **closed for the arrangement over ground it can inspect**, then the
mechanical store is available: you can check the answer. And if you can check the answer, you do not need the *right*
determiner — you need only an *adequate* one, because you can verify adequacy directly. The floor is
zero: no particular judgment is load-bearing.

If the acceptance predicate **does not close** — if there is no computable check for "is this
right?" — then the mechanical store is *structurally unavailable*, the demand cannot be verified out,
and it falls to judgment. The floor is non-zero, **for that reason and no other.**

> **The floor is non-zero exactly when, and because, you cannot check the work.**

---

## Path-degeneracy: why "zero" means robustly zero

Where the predicate closes, the floor is not merely zero in principle — it is **robustly** zero, and
the mechanism is **degeneracy** (Edelman & Gally, *PNAS* 2001: structurally different elements
yielding the same function).

Infinitely many distinct decision paths converge on an adequate act. You do not need the path that a
particular expert would take; you need *any* path that lands inside the acceptance region, and you
can tell when you've landed there because the predicate closes.

This is why machines reach superhuman performance on closing-predicate tasks without anything worth
calling understanding: **no particular determiner is required where adequacy is checkable.** What
closure removes is the demand for a *specific* judgment — not the cost of producing an adequate one.
Those are separate quantities, and the floor result governs only the first (`core/04` §2.2). (The
consequences for the intelligence debate are drawn out in `07-determination-and-intelligence.md`.)

---

## The three limits — and why determinism does not lift them

The floor is bounded below, away from zero, wherever the predicate is open. Three independent results
establish this, and it is worth being explicit that **none of them is about determinism** — they hold
in a fully deterministic universe, because they concern *decidability and knowability*, not whether
the future is fixed:

**Rice's theorem.** All non-trivial semantic properties of programs are undecidable. So the
acceptance predicate can itself be *uncomputable*, and deciding whether a given predicate "closes over
digital ground" can require solving the halting problem. This is a theorem; physics does not touch it.

**Inevitable model error** (Xu, Jain & Kankanhalli 2024; Kalai & Vempala). A calibrated model must
err on facts that appear rarely in its training, with a **non-zero lower bound.** Even the strongest
rebuttal (Suzuki et al. 2025) reduces the probability to *negligible*, **not zero.** Both sides agree
the floor is non-zero.

**Collective tacit knowledge** (Collins). The genuinely irreducible kind of tacit knowledge is
embedded in society and cannot be made explicit without socialisation. Denying it in digital work is
exactly the assertion Collins's program contradicts.

### The determinism objection, addressed directly

A strong-determinism premise — *"if every variable of the universe is known, the future is fixed"* —
does **not** rescue a zero floor on open predicates, for two reasons:

1. **It imports the entire physical state**, which is the *opposite* of "closed for the arrangement
   over ground it can **inspect**." The whole content of the zero-floor case is that the relevant
   ground is **small and closed.** Universal determinism makes it **maximal and open** — it changes
   the subject.
2. **The objections are about decidability, not predictability.** Rice's theorem and inevitable model
   error are true whether or not the universe is deterministic. Determinism is simply the wrong tool
   against them.

Determinism buys nothing here. The floor is where it is because of what can be *decided*, not because
of what is *fixed*.

---

## What survives, and why the retreat is a sharpening

The earlier claim — *"if the governing decisions and the acceptance predicate both close over digital
ground, the intrinsic floor is zero"* — was too strong: it treated "closes over digital ground" as
something you could establish, when in general you cannot (Rice).

What survives is **better**, because it *locates* the floor precisely instead of asserting its
absence:

> The floor lives in the **acceptance predicate.** Closed predicate → zero, robustly. Open
> predicate → non-zero, necessarily. Whether a given predicate is decidable → itself undecidable in
> general.

This is more useful than the original, because it tells you *where to look*: to lower a task's floor,
you do not train harder — **you find or construct a closing predicate.** That is the move that
actually works, and it is the move the whole `apparatus/` layer operationalises (contracts, checks,
the encode/verify split).

**Retired:** the slogan *"there is no tacit knowledge in digital work."* Not defensible against
Collins's collective tacit knowledge, and not needed — the predicate-located version is both correct
and more actionable.

---

## Consequence: this is what makes the actor model predictive

The floor result is the hinge between the principle and the actor model (`04-actors.md`). Because the
floor is a property of the ⟨actor, predicate⟩ pair:

- **Selection intensity is inversely proportional to predicate closure.** Where you can check the
  work, you train; where you cannot, you must select — you check the worker instead.
- **Models outperform humans exactly where the predicate closes**, and underperform where it does
  not — the gap tracks *closure*, not *difficulty*.

Both fall out of this document. Neither is available without it.

---

## The one line

> **The irreducible floor is not a property of the problem. It is a property of whether you can check
> the answer — and whether you can check the answer is, in general, something you cannot decide.**
