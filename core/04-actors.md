# Actors

**Destination:** `core/04-actors.md`

**Status.** This is the part of the framework with the least prior art and the strongest claim to
novelty. It survived external adversarial review intact — not because it was overlooked, but
because there is little to hit it with: the classical results have an **actor slot that nobody
filled in**, and this document fills it.

The load-bearing claims here are:

1. Actors differ in **pinning resolution** — how tightly their behaviour can be constrained.
2. The **intrinsic floor is a property of the acceptance predicate, not of the decision** — which
   yields *selection intensity is inversely proportional to predicate closure.*
3. Composite actors allocate **seam demand** across the same four stores, and *seam occupancy* —
   actor vs. mechanism — is a real design fork with a real price.
4. **Re-indexing the classical laws by actor changes their predictions.** This is the contribution.

---

## 1. The pinning-resolution spectrum

An **actor** is anything that determines choices against ground (`core/00`, §4 — the admission
tests gate this, and must be allowed to fail things).

Actors are not interchangeable, and the axis on which they differ is **how tightly their behaviour
can be pinned**:

| Actor | Pinned | What you get | What you *don't* get |
|---|---|---|---|
| **Classical program** | **by value** | A point. Every decision pre-made at authoring time. | Any capacity for the unanticipated. Judgment store fixed at zero. |
| **Model** | **by binding** | A *distribution*, and it genuinely holds still — freeze weights, freeze prompt. | A guarantee. A frozen distribution is not a correct one. |
| **Human** | **by classification** | A **capability envelope** — rank, certification, selection. | A distribution. The envelope is *individual*, *expiring*, and *not instance-general*. |

The spectrum runs **by value → by binding → by classification**, and it runs from *tightest* to
*loosest*.

The **last wind** is the executing actor's residual variance under the tightest available pinning.
It is what remains after you have done everything you can to constrain the actor, and it is the
irreducible cost of using that actor at all.

**Why this axis is new.** The classical results have no theory of actors. Ashby's regulator is a
black box with a variety count — he never asks *what kind of thing* is regulating, because in 1956
it did not vary. Tesler asks "user, developer, or platform" — all humans in different hats. Design
by Contract assumes the checker is a program and the contract-author is a person, and never says so,
because what else would they be.

They are not wrong. They are **under-parameterised.** Each has an actor slot nobody filled in,
because until recently there was nothing to put in it but *a person* or *a program* — and the
distinction between those two was a light switch, not a spectrum.

---

## 2. The floor is in the predicate

This is the corrected form of the zero-floor postulate, after external review. The original claim —
*"if the governing decisions and the acceptance predicate both close over digital ground, the
intrinsic floor is zero"* — was too strong. What survives is **sharper and more useful**, because it
locates the floor precisely.

> **The intrinsic floor is a property of the acceptance predicate, not of the decision.**
>
> Zero wherever the predicate is **decidable over digital ground**. There, *path-degeneracy* makes
> it robustly zero: infinitely many structurally different determiners suffice, so **no particular
> judgment is required — only an adequate one.**
>
> Non-zero exactly where the predicate does not close. **And whether it closes is, in general,
> undecidable** (Rice).

### 2.1 Why the floor moved

The bound comes from three results, and note that **none of them is about determinism** — they all
hold in a fully deterministic universe, because they concern *decidability and knowability*, not
whether the future is fixed:

- **Rice's theorem** — all non-trivial semantic properties of programs are undecidable. The
  acceptance predicate can itself be uncomputable.
- **Inevitable model error** (Xu, Jain & Kankanhalli 2024; Kalai & Vempala) — a calibrated model
  must err on rare facts, with a **non-zero lower bound**. Even the leading rebuttal reduces the
  probability to *negligible*, not zero. Both sides agree the floor is non-zero.
- **Collective tacit knowledge** (Collins) — cannot be made explicit without socialisation.

*A note on the determinism objection.* A strong-determinism premise ("know every variable and the
future is fixed") does **not** rescue the original zero-floor claim. It imports the entire physical
state, which is the opposite of *"closes over **digital** ground"* — the whole content of zero-floor
is that the relevant ground is **small and closed**, and universal determinism makes it **maximal
and open**. And the objections above are about decidability, which determinism does not touch.

### 2.2 Path-degeneracy is what makes the surviving claim robust

Where the predicate *does* close, the floor is not merely zero — it is **robustly** zero, and the
mechanism is **degeneracy** (Edelman & Gally, *PNAS* 2001: structurally different elements yielding
the same function).

Infinitely many distinct decision paths converge on an adequate act. The determination does not
require the *right* path, only *a sufficient* one. This is why models can be superhuman at tasks
with closing predicates despite having no "understanding" in any demanding sense — **adequacy is
cheap when adequacy is checkable.**

---

## 3. Selection and training

The sharpest consequence of §2, and a prediction none of the classical results can make.

> ## **Training is what you do when the acceptance predicate closes.**
> ## **Selection is what you do when it does not.**

**Why.** Training requires a *reliable error signal* — you must be able to tell, and tell soon,
whether the actor's output was right. That is the mechanical-verification store applied to the
**actor's development**. If the predicate closes, the check is available, the loop runs, and **you
can manufacture the actor.**

If the predicate does *not* close, the mechanical store is **structurally unavailable** for actor
development. There is no reliable feedback to train against. So the verification demand — which is
conserved, and does not vanish — **relocates from the act to the actor.**

> **You cannot check the work, so you check the worker.**
>
> **Selection is verification relocated from the act onto the actor's identity.**

This is why selection is brutal and high-attrition: you are measuring a property you **cannot
manufacture.**

### 3.1 The honest version — it is a gradient, not a dichotomy

The tempting statement — *"surgeons are trained, elite soldiers are selected"* — **is false as
stated, and must not be used.** Surgeons are heavily selected (admissions, the match, residency
attrition). Soldiers are heavily trained, for years, after selection.

> **Both are selected and trained. What differs is the *ratio*, and the ratio tracks predicate
> closure.**
>
> **Selection intensity is inversely proportional to acceptance-predicate closure.**

| Profession | Predicate closure | Ratio |
|---|---|---|
| Airline pilot | high — sim checks, recurrent evaluation, immediate objective failure | heavy training, moderate selection |
| Cardiac surgeon | mostly closes — graft patency, survival, M&M review; checkable, and checkable *soon* | heavy training, real but slower selection |
| Intelligence analyst | poor — "was that the right call" may never be checkable | heavy selection, notoriously weak training |
| Special operations | poor **and adversarial** — the standard moves because an opponent is moving it | extreme selection |

**This is the falsifiable form of the claim**, and it is testable across professions: measure
predicate closure independently (time-to-feedback, objectivity of the standard, stationarity of the
standard) and predict the selection/training ratio.

### 3.2 What this predicts about models

The model actor is pinnable **by binding** — *more* pinnable than a human. But binding delivers a
**distribution**, not a **guarantee**, and whether that suffices depends entirely on predicate
closure:

- **Predicate closes** → put the model in the judgment store cheaply. The mechanical store catches
  its variance. Path-degeneracy means adequacy is all you need, and adequacy is checkable.
- **Predicate does not close** → binding buys you almost nothing. You have a frozen distribution
  over a space where you *cannot tell right from wrong*: **precision without accuracy.** Arguably
  worse than a human, whose classification envelope at least encodes *selected-for* competence on
  unverifiable ground.

> **Models should outperform humans exactly where the acceptance predicate closes, and underperform
> exactly where it does not — and the gap should track predicate closure, not task difficulty.**

This explains the otherwise-strange observation that models are superhuman at competitive
programming (closing predicate) and unreliable at architecture decisions (open predicate) **despite
the latter being "easier."** Difficulty is the wrong axis. Closure is the right one.

---

## 4. Composite actors

An actor may be composed of actors. This is not an extra assumption — it is the **seam-demand
identity** (`|D_comp| = |D_single| + |S|`) applied one level down, to actors rather than tasks.

> **A composite actor carries its members' demand, plus the seam demand between them.**

Which immediately explains ensemble actors. A swarm is not intelligent because its members are.
**It is an actor because the seam carries the determination.** The members are near-degenerate; the
choice is resolved in `S`. That is why "the choice exists nowhere in any member" — of course it
does not. It lives in the seam.

### 4.1 Seam occupancy: the four stores again

The seam demand `S` is itself **allocated across the four stores.** Recursion, exactly as predicted.

| Seam store | Who sits at the seam | Instance |
|---|---|---|
| **Judgment** | an **actor** — concentrated determination | an LLM orchestrator over subagents |
| **Encoded** | a **mechanism** — distributed determination, no determiner in it | clonal selection; stigmergy; price-clearing |
| **Mechanical** | a **check** on what the seam produces | thymic negative selection (a filter on the population, not a determiner in it) |
| **Escaped** | nobody coordinates | a badly-decomposed distributed system |

Note the last row: **a swarm with no seam allocation is not a swarm, it is a mess.** The difference
between an ant colony and a crowd is whether the seam demand is carried at all.

### 4.2 The seam trade — and the cost that is easy to miss

| Seam store | **Author** cost | **Run** cost | Handles novelty | Poisonable centre |
|---|---|---|---|---|
| **Judgment** (actor) | **cheap** — you just say "coordinate" | **expensive**, every run | **yes** | **yes** |
| **Encoded** (mechanism) | **expensive — *search*** | nearly free | no | no |
| **Mechanical** (check) | expensive — the *executability tax* | cheap | no | no |
| **Escaped** | zero | zero | — | — |

**The cost that gets missed.** Encoded seams are **cheap to state and expensive to find.**
"Bind-and-proliferate" is three words. What was expensive was *finding a rule whose emergent
behaviour is the coordination you wanted* — evolution paid that in deep time. That is not the
executability tax; it is **search cost over the space of possible encodings**, and the framework
must charge for it. **Swarms are not free.**

Conversely an actor at the seam is **cheap to specify and expensive to run**: you delegate the seam
demand to judgment, and judgment does not need to be articulated. You are **buying your way out of a
search problem with per-run judgment cost.**

Which explains why multi-agent systems overwhelmingly use orchestrators: not because orchestrators
are better — they are bottlenecked and poisonable — but because **nobody knows how to find the
seam-encoding**, and an actor at the seam lets you skip the search. It is a rational trade. It is
also the *same* trade the senior-dependent consultancy made, with the *same* failure mode: **it does
not amortise, and it does not scale.**

### 4.3 The orchestrator is the poisoned-ground target

A concrete, and I think important, security consequence.

**An actor at the seam is a single point of authorship.** Corrupt the orchestrator's ground and you
corrupt the composite determination — which is exactly what prompt injection into an orchestrator
*is*. A mechanism at the seam has no such centre: you cannot poison clonal selection by corrupting
one lymphocyte, because the seam is the *dynamics*, not any member.

This is the same decorrelation result as `The Adversarial Ground`: **redundancy buys reliability;
degeneracy buys coverage; and neither buys anything if the actors are correlated.** An orchestrator
is maximally correlated — it *is* the correlation.

---

## 5. The compound: harvesting the seam

The seam is where the compound effect lives, and the loop is the FDE argument one level down.

**Judgment at the seam is expensive per-run and does not amortise. Encoded seams are nearly free
per-run and expensive to find.** But the orchestrator, running, **is performing the search** — and
you are paying for it anyway. So:

1. **Orchestrator at the seam.** Expensive per-run — but it is *searching*, and the bill is already
   being paid.
2. **Observe which coordination decisions recur.** *Recurrence*, not stability, is the signal that
   an encoding will amortise (the maturation projection).
3. **Harvest the recurring ones into the encoded seam** — and **simultaneously allocate a mechanical
   check on the seam** (§5.1, non-negotiable).
4. **The orchestrator's judgment shrinks to the residual** — the genuinely novel coordination
   decisions the encoding does not cover.
5. **Repeat.** Each cycle the seam gets cheaper per-run and the residual gets **smaller and more
   valuable.**

The asymptote is the floor: coordination decisions whose acceptance predicate does not close, where
an actor must remain at the seam **permanently**. That is correct, and now you are paying for
judgment *only there*.

**The platform requirement.** This only works if the seam is an **encoding-accepting surface** — not
"configurable" (a fixed aperture) but a surface where a *newly discovered* coordination decision can
be admitted post-hoc, without rebuilding the orchestrator, and made available to **every** subsequent
run. An orchestrator with hardcoded coordination logic **cannot compound by construction**: it
performs the search on every run and discards the answer on every run.

### 5.1 The matched-pair rule (hard invariant)

> **You may not move seam demand from judgment to encoded without simultaneously allocating a
> mechanical check on the seam.**

**Why.** Evolution paid millions of years for its seam-encoding because the rule must hold **across
every case the organism will ever meet, without an actor there to catch the exceptions.** You are
proposing to shortcut that search by observing an orchestrator over finitely many runs. **You will
harvest an encoding that is correct on the cases you saw and wrong on the ones you did not.**

The orchestrator's judgment was silently absorbing those exceptions. Encode the rule, remove the
orchestrator, and **nobody catches them at all** — they escape.

This is exactly what the thymus is. The immune system's encoded seam (bind-and-proliferate) is
*dangerously general*, so a dedicated mechanical check polices what the rule produces. **The encoded
seam and its mechanical check are a matched pair.** Not a safety nicety — **the conservation principle.**
The demand the orchestrator was absorbing has to land somewhere.

### 5.2 The immune system is *not* the compound platform — and what is

Worth stating, because the near-miss is instructive.

Vertebrate immunity has a judgment store that **discovers** things, an encoded store (the germline)
that would benefit enormously from those discoveries, and **no channel between them.** The Weismann
barrier holds; the soma cannot write to the germline. Immunological memory compounds **within one
lifetime** and dies with the individual — that is a **cache, not a platform.**

> **The immune system has a sink and an instrument, and no channel between them.**

**CRISPR is the compound platform.** Judgment (encounter a phage, survive) → **harvested into
encoding** (a spacer excised and filed in an inheritable array) → **inherited** (descendants read the
array *before* acting) → the Nth encounter is cheaper than the first, **across the population,
permanently.** Instrument, harvest channel, sink, inheritance. All four. Bacteria have the channel
vertebrates lack.

**And a vaccine is the harvest channel built externally.** The immune system cannot write judgment
back into encoding — so we built the channel *outside the organism*: someone encounters the pathogen
(judgment, expensive, sometimes fatal), we **harvest** what worked, and **inject that encoding into
every subsequent actor**, skipping the discovery entirely. The organism receives memory it never paid
for.

**A vaccine is inherited encoding, delivered by syringe because the germline would not carry it.** It
is the prefix. And the failure modes follow exactly: influenza requires **annual re-harvest** because
the encoding goes stale (*you can encode ground you control; you must re-verify ground you do not* —
the virus is ground you do not control, so the flu vaccine is a **contract test re-run against a
moving source of truth**). And **original antigenic sin is poisoned ground**, literally: a cached
prior belief consumed as ground, biasing the response toward an expired epitope and degrading a
correct determination. Confident, well-reasoned, worse than nothing.

**The lesson for the platform:** having a judgment store and an encoded store **is not enough.** Two
stores with no channel between them means the expensive discoveries evaporate.

> **The channel is the platform.**

Not the graph, not the ledger, not the orchestrator — **the write-back path from judgment to
encoding, and the inheritance path from encoding to the next run.**

---

## 6. Re-indexing the classical results

**This section is the contribution.** Everything above is machinery; this is what the machinery
*buys*.

The classical laws are correct. They are stated for an **unexamined actor**. Supplying the actor
parameter does not replace them — it **indexes** them, and **the indexed versions make predictions the
originals cannot.**

That test — *does filling the slot change the prediction?* — is what separates a real contribution
from a re-labelling. It does.

### Tesler — Conservation of Complexity

**Original:** complexity is irreducible; the only question is *who deals with it* — user, developer,
or platform.

**Indexed:** those are three humans in different hats. Fill the slot and *who* becomes a variable
with **structure**: the **price** of each destination differs by **pinning resolution**, so optimal
allocation is not a matter of taste but of the actor spectrum — **and the optimum moved when a
binding-pinned actor arrived.**

> **Tesler's law cannot tell you that LLMs change where the complexity should sit. The indexed
> version can, and does.**

### Ashby — Requisite Variety

**Original:** only variety can destroy variety; the regulator must command at least as much variety
as the disturbance. *(And Ashby has what we lack: a unit — bits.)*

**Indexed:** variety is **cheap for a program** (encoded, amortising), **expensive for a human**
(judgment, per-run, non-amortising), and **newly purchasable from a model** at a price between the
two.

> **Ashby's law is silent on the market for variety. The indexed version has a price list.**

### Brooks — essential vs. accidental complexity

**Original:** essential complexity is inherent in the problem and irreducible; accidental complexity
is an artifact of tools.

**Indexed:** essential **to whom**? The corrected floor result (§2) answers it: irreducibility is a
property of the **acceptance predicate**, not of the problem.

> **This is why Brooks's line always felt slippery and nobody could say why — he was measuring a
> two-place relation with a one-place instrument.**

### Meyer — Design by Contract

**Original:** preconditions and postconditions. *(More precise than we are on the verification
content; we add nothing there.)*

**Indexed:** a contract presupposes an actor that can be *held* to it. **Pinning resolution tells
you which actors can be contracted at all** — by value (trivially), by binding (probabilistically),
by classification (only via an envelope, which is *not* a distribution).

> **DbC assumes the contracted party is a program. The indexed version says what a contract even
> *means* for a model or a human — and why the guarantee weakens as pinning loosens.**

### Kalman — observability and estimator divergence

**Original:** an estimator that trusts its own model over its measurements diverges. *(The rigorous
ancestor of poisoned ground.)*

**Indexed:** the same divergence, **for any actor** — a program with a stale cache, a model consuming
its own summaries, a human consulting their model of the system rather than the system, an immune
system in original antigenic sin.

> **Kalman formalised it for one class of estimator. The indexed version says it is a property of
> determination as such, and the remedy is the same in every case: go and look.**

### Polanyi / Collins — tacit knowledge

**Original:** we know more than we can tell; and (Collins) the tacit divides into relational, somatic,
and **collective** — the last being genuinely irreducible.

**Indexed:** the floor is not a property of the *knower*. It is a property of the
**actor–predicate pair.** Which is what produces §3: *selection intensity is inversely proportional
to predicate closure* — a result about **how you obtain actors**, which neither Polanyi nor Collins
addresses.

---

## 7. The honest statement of the contribution

Not *"I have reframed Tesler, Ashby, Brooks, Meyer, and Kalman."* That is true, and it will read as
grandiose, and it will be dismissed for the reasons the adversarial review already gave.

The defensible framing is smaller and lands harder:

> **There is a parameter missing from the classical results. It did not matter until now, because
> there was only ever one kind of actor to put in it. Here it is — and here is what changes when
> you supply it.**

The actor slot was always there. **A new kind of actor is simply what made the omission visible.**

And the two results that are *ours*, that follow only from filling the slot, and that no classical
law can produce:

1. **The floor lives in the acceptance predicate** — so *selection intensity is inversely
   proportional to predicate closure*, and *models outperform humans exactly where the predicate
   closes.*
2. **Seam demand allocates across the same four stores** — so *actor-at-seam buys adaptivity and pays
   with a bottleneck and a poisonable centre; mechanism-at-seam buys scale and pays with an expensive
   search* — and *the compound requires a channel from judgment back into encoding.*
