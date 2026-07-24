# Determination

**Destination:** `core/00-determination.md` — before `01-the-principle.md`. This is what the
principle is *about*. Everything else in `core/` is a consequence.

*Register note: this document predates the naming decision in `01-the-principle.md`. Where it says
"the law," read "the principle" — the framework's own claim is a principle, not a law (see `01`,
"Register"). The word "law" is retained below only where it refers to **Tesler's** or **Ashby's**
laws, or is used as a deliberate rhetorical foil ("a law about X").*

**Status:** the reframing is a clarification, not a new claim. It changes nothing about what the
law asserts, only about what it is understood to range over. The load-bearing claims remain
exactly as before, and remain falsifiable: **demand is conserved**, and **the four stores are
exhaustive**. Nothing in this document should be read as evidence for those.

---

## 1. The collapse

The framework has been carrying a distinction it does not need, and the distinction has been
hiding what the law is about.

We spoke of **governing decisions** as decisions *about an act* — the act was the primitive, the
decisions were the specification wrapped around it. Decide the constraints, then act.

**There is no act.**

"Which voltage to the motor, now" is a decision. "Which word next" is a decision. "Fire or hold"
is a decision. Descend as far as you like and you never reach a floor of *pure action* that
decisions merely describe. It is decisions the whole way down. What we called *the act* was the
**last decision in the chain** — the one closest to the world, whose determination is expressed
rather than passed on.

> **The law is not about building. It is about the requirements for making a determinate choice
> at all.**

It reads as a law about software engineering for the same reason thermodynamics reads as a law
about steam engines to someone standing next to one. Engineering is where we found it. It is not
what it is about.

---

## 2. Two primitives

Once the act dissolves, the framework has exactly two primitives.

> **Decisions** — the things determined.
> **Ground** — what they are determined against.

That is the whole ontology. Every act of determination — by rule, by check, or by an actor in
the moment — **reads ground in order to resolve a choice.** There is no third thing.

The apparatus holds against this without strain:

| Apparatus | A statement about |
|---|---|
| The four stores | *where the determination lives* |
| The Polanyi floor | *how much determination can be moved off an actor* |
| The seam-demand identity | *decisions created between decomposed decisions* |
| Poisoned ground | *corrupting what a determination reads against* |
| The encode/verify split | *whether you author the ground a determination reads* |
| Assurance level | *which choices count as decisions at all* |

Nothing needs a third primitive. Nothing is left over.

---

## 3. The four stores, restated

If the stores were four ways of organising engineering work, their exhaustiveness would be a
contingent claim about engineering — an empirical taxonomy, and a suspicious one.

They are not that. They answer a question with nothing to do with engineering:

> **Given that a choice must be made, where can the thing that determines it live?**

- **Encoded** — determined *in advance*, by a rule.
- **Mechanical** — determined *after*, by a check.
- **Judgment** — determined *in the moment*, by an actor reading ground.
- **Escaped** — determined by *nothing*. Which is to say: by accident.

A choice is determined by exactly one of **{rule, check, actor, nothing}**. There is no fifth
source. Conservation is then nearly tautological in the good way: **the set of choices is fixed
by the task, each is determined by exactly one source, so the only freedom is the assignment.**

---

## 4. The admission tests

This generalisation is dangerous, and the danger is precise: *"the act is a decision"* is one
step from *"everything is decisions,"* which explains nothing because it excludes nothing.

**"Makes a determinate choice against a substrate" must remain a real predicate, not a universal
solvent.**

> **A choice is a decision iff varying *the choice* moves the outcome past tolerance.**
>
> **A fact is ground iff varying *the world* moves the outcome past tolerance.**

Same tolerance, same granularity bound; two different things varied.

These tests **exclude**, and must be allowed to. A rock falling is not deciding where to land.
Describing it in choice-language is *you authoring ground, not the rock reading it* — it inspects
nothing, nothing it "reads" could vary and change what it does, and there is no substrate against
which it resolves anything. It fails both tests.

**Apply the tests or the framework becomes vacuous. A law that admits everything forbids
nothing.**

---

## 5. The name

*Full treatment: `01-the-principle.md` ("Register") and `meta/lineage-and-limits.md`.*

The reframing forces a naming question, and the answer is a **two-level structure**, not a
replacement — and, after external review, a **downgrade of register.**

**"Specification" is a domain word.** It means *the thing you write down before you build*. An
immune system has no specification; a market has no specification. Using it in the general
statement drags the reader back into the engineering frame the principle is not confined to, and
invites the misreading that the principle is about *documents* — the error behind "CMSes are going
away."

**"Conservation" and "demand" survive; "law" does not.** Conservation is the load-bearing claim.
Demand means *what must be supplied*, agnostic about who supplies it. But **there is no measured
quantity**, so the correct register is **principle**, in the sense of *Tesler's Law* and *Ashby's
Law* — homage, not physics (`01`, "Register").

So the two-level structure is:

> ### The Conservation Principle of Determination Demand
> *(`core/` — actor-general. Ranges over anything that determines choices against ground.)*
>
> ### Conservation of Specification Demand
> *(the **engineering projection** — the same principle, denominated in the vocabulary of a domain
> where determinations are called specifications; see `applications/sdlc`.)*

The funnel and maturation are *projections* of the principle, not restatements. **Specification is
what determination demand is called when the actor is building software.**

*A note on delivery.* "I have found a law governing immune systems, markets, and your codebase"
earns the skepticism it will receive. "Here is a conservation *principle* in software engineering —
which turns out to be the projection of something more general, and which I am careful not to call
a law, because I have no unit" is the same claim in the order, and the register, that earns belief.

---

## 6. Ensemble actors

The immune system forces an addition, and it is **not a fifth store**. It is a *strategy for
populating the judgment store when no single actor can carry the demand.*

### 6.1 The organism cannot encode the determinations

The antigen space is larger than the genome and shifts within a lifetime, so the determinations
**cannot be pre-encoded.** State precisely what that does and does not establish.

It closes the **encoded** store. Capacity overflow alone would not produce a floor: a determination
that cannot be encoded can still be verified out, and where a check exists adequacy stays cheap
(`core/03`).

**The floor is there because the predicate does not close.** The organism cannot check, before or
after, whether a response to a novel antigen was correct. There is no verdict function over the
antigen space; autoimmunity is precisely the uncaught error, and it arrives as damage rather than as
a verdict. Encoding is unavailable by capacity and verification is unavailable by openness, so the
determination falls to the in-the-moment actor on every encounter. **That is the floor, in the
framework's exact sense.**

So what does the organism encode instead?

> **It encodes a process for generating determiners, rather than the determinations themselves.**

V(D)J recombination is a **dedicated, encoded randomiser** that shuffles gene segments to produce
~10¹¹ distinct receptors. State this precisely, because the intuitive account is wrong: **the
diversity is not evolutionary drift or copy noise.** The organism spends real metabolic cost to
build a diversity engine *on purpose*. The genome does not encode the receptors — **it encodes the
machine that manufactures them.**

### 6.2 The population is the actor. The cell is not.

No individual lymphocyte is adaptive, or intelligent, or capable of recognising a novel pathogen.
Each is a dumb detector with one fixed receptor: it binds, or it does not. Closer to a
**degenerate actor** — all decisions pre-made at recombination time.

The determination — *this is non-self, respond* — is made by the **population**, through
selection: clones whose receptors happen to bind are amplified; the rest are not.

> **The choice is a property of the ensemble, and it exists nowhere in any member.**

Run the admission tests on the ensemble and it passes cleanly. Vary the collective response →
outcome moves past tolerance. Vary the ground (which antigen is present) → outcome moves. **The
population is an actor in the framework's exact sense.** The cell mostly is not.

### 6.3 The result

> **Diversity in a population is how you carry judgment demand that exceeds any single actor's
> capacity.**

When demand exceeds an actor's floor there are three options: encode more (impossible if the space
is too large), accept escape (fatal), or **distribute across a diverse population whose union
covers what no member could.**

### 6.4 Diversity is not redundancy

The distinction with teeth. Conflating the two is a real error.

> **Redundancy buys reliability. Diversity buys coverage.**
>
> **They are different goods.**

A population of *identical* actors does not carry more judgment than one actor — it carries the
same judgment redundantly. Ten thousand identical lymphocytes recognise exactly one antigen. Ten
thousand *different* ones recognise ten thousand.

**The variance is not a defect tolerated for robustness. The variance is the capability.**

And this is the same structure as denying single-point authorship of ground (`The Adversarial
Ground`). Redundant *uncorrelated* channels defeat an adversary who can author only one. Diverse
*uncorrelated* detectors cover a space no single detector can. In both, the value lies in the
actors being **decorrelated** — and in both, **correlation is the failure mode.**

A monoculture is a population that has lost its coverage. It is why crop monocultures,
immunocompromised populations, and homogeneous detection stacks fail identically: **one thing gets
through everything, because everything is the same thing.**

### 6.5 The price

The framework must charge for this, and it does.

Selection over a diverse population is **slow** (the adaptive response takes days), **metabolically
expensive**, and it **requires the mechanical store to police it** — thymic negative selection
exists precisely because a randomiser will inevitably manufacture self-reactive actors, and they
must be checked and destroyed before licensing.

> **Diversity is not free judgment. It is judgment bought with time, energy, and an obligatory
> verification apparatus.**

That is the price of covering a floor you cannot encode away — and it is exactly the price the law
says must be paid somewhere.

### 6.6 The gate on swarms

**A swarm is an actor only if it genuinely determines choices against ground.** The admission
tests (§4) still gate, and they must.

A flock turning together is mostly **not** making a determination — local rules producing global
pattern, with no choice resolved against a substrate. Ant colony foraging is closer, because the
pheromone field is genuine ground, read and written.

**The immune system passes. Not everything swarm-shaped will.** Without the gate, "swarms are
intelligent actors" becomes exactly the vacuous generalisation §4 exists to prevent.

---

## 7. The immune system as the licensing instance

The immune system is not an illustration. It is the **test that licenses the general name**, and it
is the strongest available, for one reason:

> **The immune system had no engineer.**

Nobody wrote its specification. And yet:

| Store | Instance |
|---|---|
| **Encoded** | innate immunity — germline pattern-recognition receptors, fixed across evolutionary time, free at runtime, cannot adapt within a lifetime |
| **Mechanical** | thymic negative selection — T-cells tested against self *after* manufacture and *before* licensing. A validator at a boundary, with a dedicated organ. |
| **Judgment** | adaptive immunity — per-encounter determination against novel antigen; slow, costly, and it dies with the individual |
| **Escaped** | a pathogen no receptor fires on and no response has caught. The decision is made by nobody, so it is made by default — *do not attack* — and collected later, as damage. |

All four stores, physically instantiated, with the correct cost structures. Conservation is visible
in the forced split: innate is fast and cannot handle novelty; adaptive handles novelty and is
slow. **The organism runs both because neither store can carry the whole demand** — the law forcing
a split, not an engineering preference.

**And both poisoned-ground attacks, with no metaphor in between:**

**Autoimmune disease is poisoned ground.** The machinery works *perfectly* — sound logic — over a
substrate corrupted so that self reads as non-self. It then does what correct reasoning over a
false premise always does: attacks with full authority. *Confident, well-reasoned, catastrophic.*
The signature, in a body.

**Molecular mimicry is masquerade.** A pathogen evolves surface proteins resembling host tissue —
*it looks like normal ground*, so the determination reads it as self and does not fire. The
benign-looking binary, exactly. And the sequel is worse: when a response is finally mounted against
the mimic, it **cross-reacts with the host tissue that resembled it**. Rheumatic fever is a
streptococcal surface that mimicked heart tissue closely enough that the eventual immune response
attacked the heart.

That is a masquerade attack **inducing collateral destruction of legitimate ground** — the same
structure as an intrusion so entangled with real system processes that remediation damages the
host.

Three domains — cybersecurity, counterintelligence, immunology — running the *same* attack:
**author the ground so that a correct determiner reads it wrong.** The immune system runs it in
protein instead of packets or intel.

**This is what licenses the general name.** Here is a system with all four stores, a dedicated
mechanical-verification organ, a genuine Polanyi floor, an ensemble actor, and both poisoned-ground
attacks — that **evolved**, with no specifier anywhere.

If the law were about engineering, it could not be here.

It is here. So it is not.

---

## 8. Why it was not written down

*This section explains. It does not argue. A good story about why nobody found your idea is exactly
the kind of thing that feels like evidence and is not. Do not cite it as though it were.*

The obvious account — *we only had humans in the choice-making category* — is close, and not quite
right.

**Classical programs were always actors**, degenerate ones, every decision pre-made at authoring
time. And that is *why* the law stayed invisible. A program **cannot take** an unallocated
decision; its judgment store is fixed at zero. So the allocation question had two answers: encode
it, or a human carries it. Not a spectrum. **A light switch.**

Nobody writes a conservation law for a light switch.

What appeared is narrower and sharper than "a second actor." It is the **first actor pinnable by
binding** — non-deterministic, but with a distribution that can be frozen. For the first time, the
judgment store has a **carrier that is neither a person nor zero.**

The allocation became **continuous**. Demand can now sit anywhere on the spectrum, placement is a
real choice with real prices, and — decisively — **it can be got wrong in ways that look right.**

> **The law was always true. It was unobservable, because the demand had nowhere to go.**
>
> **A conserved quantity is invisible until something moves.**

The same shape as the CMS correction: build cost collapsed and revealed that *specification* had
been load-bearing all along. Here, the actor spectrum opened and revealed that *allocation* had
been load-bearing all along. Nothing became true. Something became **visible**, because a cost that
had pinned everything in place stopped.

Which accounts for the surrounding fields holding the pieces without assembling them. Polanyi had
the floor without the stores. Software engineering had specification without conservation.
Counterintelligence had poisoned ground without knowing it generalised. Immunology had all four
stores and no reason to call them that. Each field found the fragment its own domain made visible —
and **assembly requires seeing the quantity move**, which nothing could, until a binding-pinned
actor existed to move it.

---

## 9. The one line

> **The law does not describe how to build things. It describes what is required to determine
> anything at all — and what necessarily happens to a determination nobody makes.**
