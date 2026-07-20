# Determination Is Not Intelligence

**Destination:** `core/06-determination-and-intelligence.md`

**Status.** The positive claim (*determination ≠ intelligence*) is a **consequence** of the
admission tests and is not optional — the framework collapses without it. The negative result
(*the LLM-intelligence debate is structurally undecidable*) is a **derivation** from the
floor-in-the-predicate result, and it is falsifiable in a specific way stated in §5.

**What this document does NOT do.** It does not claim LLMs are intelligent. It does not claim they
are not. It claims that **the question as currently posed cannot be answered**, and it says exactly
why.

---

## 1. Determination is not intelligence

A thermostat determines. It reads ground (temperature), resolves a choice (heat or don't), against
a predicate (below setpoint). It passes **both admission tests** cleanly: vary the choice, the
outcome moves; vary the world, the outcome moves.

**It is an actor in the framework's exact sense. Nobody thinks it is intelligent.**

> **Determination is necessary and nowhere near sufficient for intelligence.**

This is not a concession. It is **load-bearing**, and the framework does not work without it.

The apparatus quantifies over *where a determination's source lives*, *how tightly an actor can be
pinned*, and *whether the acceptance predicate closes*. **None of these mentions intelligence.** A
program pinned by value determines; a model pinned by binding determines; a human pinned by
classification determines; a bacterial CRISPR array determines. The framework treats them
identically **because for its purposes they are identical** — they all resolve choices against
ground, and the principle is about *the resolution*, not *the resolver*.

**Require intelligence for actorhood and the framework dies on the spot.** You lose the program,
the ensemble, the market — and with them the actor-general claim that makes the whole thing work.

**The framework is orthogonal to intelligence, and that orthogonality is a feature.**

---

## 2. But the negative result is not empty

The framework *does* say something about intelligence. It is **negative**, and it is more
interesting than a positive claim would be.

Recall the floor result (`core/04`, §2):

> The intrinsic floor is a property of the **acceptance predicate**. Where the predicate closes,
> **path-degeneracy** makes it *robustly* zero — infinitely many structurally different determiners
> suffice, so **no *particular* judgment is required, only an *adequate* one.**

Read that again with intelligence in mind. It says:

> ## **A closing predicate makes intelligence unnecessary.**
>
> **Adequacy is cheap where adequacy is checkable.**

You do not need to *understand* chess to play it superhumanly — you need a search and an evaluation
function. You do not need to understand a codebase to make its tests pass. **Every domain that fell
to machines fell because someone found a closing predicate — not because someone built a mind.**

Which inverts the usual question. The interesting one is not *"does determination prove
intelligence?"* It is:

> **Intelligence, whatever it is, is only load-bearing where you cannot check the work.**

*Stated carefully: this is not a definition of intelligence and not a proof of anything. It is what
the framework's own results imply about where intelligence could possibly be doing work.*

---

## 3. The invalid argument — and why it must be refused

There is a tempting inference here, and it is **wrong**. It must be stated and killed explicitly,
because it is the first thing a reader will reach for:

> 1. Intelligence is (perhaps) required to decide where the predicate does not close.
> 2. LLMs decide where the predicate does not close.
> 3. ∴ **LLMs are intelligent.**

This is **affirming the consequent** — but the deeper problem is that **premise 2 is ambiguous and
is doing all the work.**

LLMs *emit determinations* on open predicates. They will tell you which architecture to choose.
**What is unestablished is whether the determinations are any good** — and you cannot check,
*because the predicate does not close.* **That is what "does not close" means.**

So the argument reduces to:

> *"We cannot verify its output, therefore it must be doing the thing we cannot verify it is
> doing."*

**Unverifiability is being treated as evidence for the very capacity that unverifiability makes
unmeasurable.** A random number generator also emits determinations on open predicates. So does a
Magic 8-Ball. **Emitting is not the criterion.**

**And the framework explicitly predicts this failure.** From `core/04`, §3.2: where the predicate
does not close, binding buys you a **frozen distribution over a space where you cannot tell right
from wrong** — *precision without accuracy*. The framework's own prediction is that models
**underperform** there. **You cannot then use performance in that region as evidence of
intelligence, when the theory says performance in that region is unmeasurable.**

---

## 4. The real result: the debate is structurally undecidable

Here is what the framework actually delivers to the LLM-intelligence argument.

> ## **The debate is unresolvable in the region where it is being fought — and the framework
> explains why.**

Both camps are arguing about performance on **open predicates**: reasoning, understanding, judgment,
"real" comprehension. And an open predicate is **by definition** one where you cannot check the work.

**So there is no experiment either side can run that settles it.**

This is not a temporary state of ignorance pending better benchmarks. It is **structural**:

> **You cannot benchmark your way across an open predicate — because a benchmark *is* a closing
> predicate.**
>
> The moment you construct one, **you have closed the predicate** — and you have moved the question
> into the region where degeneracy says *adequacy is cheap and intelligence is unnecessary*.

The measuring instrument destroys the thing it was built to measure. Not metaphorically —
**definitionally.**

### 4.1 It cuts the skeptics

> *"It's just next-token prediction. There is no real understanding."*

**You cannot demonstrate that.** Your evidence would have to be *failures on open predicates* — and
you cannot grade those either. The same unverifiability that blocks the believers blocks you.

**Your dismissal is exactly as unfalsifiable as the claim you are dismissing.**

### 4.2 It cuts the believers

> *"Look how well it reasons about X."*

**Every benchmark you cite is a closed predicate** — that is what makes it a benchmark. And on closed
predicates, **the framework says intelligence is not required**: path-degeneracy, adequacy is cheap
where adequacy is checkable.

**Your evidence is drawn entirely from the region where your conclusion does not follow.**

Worse: **every impressive benchmark result is, structurally, evidence *against* the relevance of the
benchmark.** The better the score, the more certainly it was obtainable without the thing you are
trying to demonstrate.

### 4.3 The shape of the deadlock

> **Every measurable success is in the region where intelligence is unnecessary.**
> **Every claim of intelligence is in the region that is unmeasurable.**
>
> **The evidence and the claim never occupy the same territory — and the framework says they
> cannot, by construction.**

This explains why the debate is so stuck, and it is **not** because the participants are foolish. The
disagreement is **structurally undecidable given the evidence anyone is able to produce.**

> **Anyone who believes they have settled it has smuggled a closing predicate into a region that
> does not have one.**

---

## 5. What would actually change the answer

The result is not a counsel of despair. It tells you precisely what a resolution would require, and
this is where the claim becomes **falsifiable**:

**Either** exhibit an open predicate on which performance can nonetheless be reliably assessed — which
would mean the predicate was not open, and the framework's classification of it was wrong;

**or** show that path-degeneracy fails somewhere — that on some class of *closing* predicates, adequacy
is **not** cheap, and only a narrow band of determiners can reach it. That would mean intelligence is
load-bearing on some closed predicates after all, and the framework's central claim about degeneracy
is false.

**Either would falsify this document.** Neither has been done.

Until one is, the honest position is:

> **The framework does not tell you whether LLMs are intelligent. It tells you that the question, as
> currently posed, cannot be answered — and it identifies exactly why.**

---

## 6. The consequence for the framework's own scope

This is a **boundary**, and it is the second one the framework has drawn against itself (the first
being the admission tests refusing the rock and the quark).

Drawing it costs something real: the framework must **decline** the most attention-getting claim
available to it. *"Our theory proves LLMs are intelligent"* would travel further than anything else in
this repository.

It is also **false**, and claiming it would destroy the framework's standing on everything else it
says — which is the price of every universal-solvent move, and exactly the failure the admission tests
exist to prevent.

> **A framework that will not say what it cannot support is worth more than one that will.**

The framework's contribution to this debate is **not a verdict.** It is the demonstration that **there
is no verdict available** — and, more usefully, **the map of where a verdict could ever come from.**
