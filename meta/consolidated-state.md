# DDD — Consolidated State

**Date:** July 2026, end of the review session.
**Purpose:** a single authoritative statement of what the framework now claims, what was
retreated, and what is still owed. Several existing artifacts contradict each other after the
adversarial review; this document says which one wins.

**Read this first.** Anything in an older artifact that conflicts with this document is
**superseded.**

---

## 1. The framework, as it now stands

### 1.1 The two primitives

> **Decisions** — the things determined.
> **Ground** — what they are determined against.

Every determination reads ground to resolve a choice. There is no third thing. **The act is a
decision** — there is no floor of "pure action" beneath the decisions; what we called the act is
just the last decision in the chain.

### 1.2 The admission tests — the discipline that keeps this a law

> **A choice is a decision iff varying *the choice* moves the outcome past tolerance.**
>
> **A fact is ground iff varying *the world* moves the outcome past tolerance.**

**These must be allowed to fail things.** A rock does not decide where to land. A quark does not
determine — it has no substrate it inspects, and quantum indeterminacy is a probability amplitude,
not a choice. **If everything passes, the framework forbids nothing and is worthless.**

*This is the framework's primary defence against becoming a universal solvent, and it only works
if it is enforced against claims you would like to be true.*

### 1.3 The four stores

Given that a choice must be made, where can the thing that determines it live?

| Store | Form | Property |
|---|---|---|
| **Encoded** | constraint, before the act | extra-actor · amortises · cheap to state, **expensive to find** |
| **Mechanical** | criterion, after the act | pays the **executability tax** · cheap to trust |
| **Judgment** | per-run, by an actor reading ground | does not amortise · walks out the door |
| **Escaped** | decided by nobody | defect exposure · **the only forbidden state** |

**{rule, check, actor, nothing}** — there is no fifth source.

**Status: this is a definitional partition.** It cannot be false. It is **ergonomics, not a
discovery**, and must be claimed as such. The one genuine addition over prior art is the
**escaped** store — naming *"decided by nobody = latent defect exposure"* as first-class. Tesler
did not have it.

### 1.4 Conservation — the weak, defensible position

> **Within a fixed task decomposition, determination demand is conserved.** Reduce one store and
> the demand relocates; it does not vanish.
>
> **Choosing the decomposition is itself the highest-leverage governing decision** — and a better
> decomposition genuinely *destroys* demand (CRDTs delete conflict-resolution decisions;
> content-addressed builds delete ordering decisions).

**This is Tesler's Law of Conservation of Complexity, generalised** — denominated in decisions, with
a fourth store and an assurance-level granularity bound. **Cite Tesler. Cite Ashby** (who had a
unit — bits — which we do not). **Do not claim physical-law status.**

**Register:** "Principle," not "Law," in any technical context. If "Law" is used, it is homage in
the sense of *Tesler's Law* and *Ashby's Law* — and that must be stated.

### 1.5 The floor is in the predicate

**The framework's best original result.**

> **The intrinsic floor is a property of the acceptance predicate, not of the decision.**
>
> **Zero** wherever the predicate is decidable over digital ground — and there **path-degeneracy**
> makes it *robustly* zero: infinitely many structurally different determiners suffice, so **no
> *particular* judgment is required, only an *adequate* one.**
>
> **Non-zero** exactly where the predicate does not close — and **whether it closes is, in general,
> undecidable** (Rice).

**Bounded by:** Rice's theorem · inevitable model error (Xu et al. 2024; Kalai & Vempala — even the
strongest rebuttal reduces it to *negligible*, not zero) · Collins's **collective** tacit knowledge.

**Determinism does not rescue the strong version.** A "know every variable" premise imports the
entire physical state, which is the opposite of *"closes over **digital** ground"* — and the
objections above are about **decidability**, not predictability. They hold in a deterministic
universe.

**Retired:** *"There is no tacit knowledge in digital work."* Not defensible against Collins.

### 1.6 The encode/verify split

> **You can encode ground you control. You must mechanically verify ground you don't.**

Any uncontrolled ground is **two facts**: *your copy* (pinned, stale-able) and *the source of truth*
(remote, mutable). A lockfile pins the first and cannot pin the second.

> **You cannot amortise an observation of something you do not control.** Each act requires its own
> observation. That cost is irreducible.

### 1.7 The closure principle

> **An actor's own prior output is not ground.**

Consuming a cached belief as ground closes a loop with **no corrective term**. Failures are *correct
inferences over false premises* — **confident, well-reasoned, catastrophic.**

**This is estimator divergence / observability failure (Kalman). Cite it.** It is the rigorous
ancestor and it has theorems; we add a name and a generalisation across actor kinds.

**Retreated:** the cross-domain *unification*. TOCTOU (concurrency), molecular mimicry (a false
*negative*), and autoimmunity (a false *positive*) are **not one mechanism** — grouping opposite
error directions was the apophenia the review correctly flagged. They remain *instances of* "the
actor's model of the ground diverged from the ground," but the mechanisms differ and must not be
conflated.

### 1.8 Actors

**The strongest part of the framework, and the part with the least prior art.**

**Pinning-resolution spectrum:** by **value** (program — a point) → by **binding** (model — a
distribution that genuinely holds still) → by **classification** (human — a capability *envelope*,
individual, expiring, not instance-general).

**Selection vs. training** — the falsifiable claim:

> **Training is what you do when the acceptance predicate closes.**
> **Selection is what you do when it does not.**
>
> **Selection intensity is inversely proportional to predicate closure.**

You cannot check the work, so **you check the worker.** Selection is verification relocated from the
act onto the actor's identity.

*It is a **gradient**, not a dichotomy. Surgeons are also selected; soldiers are also trained. The
ratio tracks closure.*

**The model prediction:**

> **Models outperform humans exactly where the acceptance predicate closes, and underperform exactly
> where it does not — and the gap tracks *closure*, not *difficulty*.**

### 1.9 Composite actors and the seam

`|D_comp| = |D_single| + |S|` applied to **actors**, not tasks. **Seam demand allocates across the
same four stores** — seam occupancy is a design fork:

| Seam store | Occupant | Author cost | Run cost | Novelty | Poisonable centre |
|---|---|---|---|---|---|
| **Judgment** | an **actor** (orchestrator) | cheap — just say "coordinate" | **expensive, every run** | **yes** | **yes** |
| **Encoded** | a **mechanism** (selection, stigmergy) | **expensive — *search*** | nearly free | no | no |
| **Mechanical** | a **check** (the thymus) | executability tax | cheap | no | no |
| **Escaped** | nobody | zero | zero | — | — |

**Swarms are not free.** Encoded seams are *cheap to state and expensive to find* — evolution paid
for bind-and-proliferate in deep time. That is **search cost**, and the framework charges for it.

**Matched-pair invariant:**

> **You may not move seam demand from judgment to encoded without simultaneously allocating a
> mechanical check on the seam.**

The orchestrator was silently absorbing the exceptions. Encode the rule, remove the orchestrator, and
**nobody catches them** — they escape. *This is what the thymus is.*

### 1.10 The channel is the platform

> Having a judgment store and an encoded store **is not enough.** Two stores with no channel between
> them means the expensive discoveries evaporate.

- **Vertebrate immunity:** judgment discovers, germline would benefit, **no channel** (Weismann
  barrier). Memory compounds *within one lifetime* and dies with the individual. **A cache, not a
  platform.**
- **CRISPR:** judgment (survive a phage) → **harvested into encoding** (spacer filed in an
  inheritable array) → **inherited**. Instrument, channel, sink, inheritance. **This is the compound
  platform**, and its mechanism is exactly as advertised.
- **A vaccine** is the harvest channel **built externally**, because the germline would not carry it.
  Inherited encoding, delivered by syringe. *Original antigenic sin is poisoned ground, literally.*
- **FDE + platform · `ground harvest` · the seam-harvest loop:** the same four parts.

### 1.11 Determination is not intelligence

*Full treatment: `core/06-determination-and-intelligence.md`.*

**The framework is orthogonal to intelligence, and this is a feature.**

A thermostat determines — reads ground, resolves a choice, passes both admission tests. Nobody thinks
it is intelligent. **Determination is necessary and nowhere near sufficient.**

**Do not require intelligence for actorhood.** The moment you do, you lose the program, the ensemble,
the market — and the actor-general claim that makes the framework work.

**The negative result:**

> **A closing predicate makes intelligence unnecessary.** Path-degeneracy means adequacy is cheap
> where adequacy is checkable. Every domain that fell to machines fell because someone found a
> closing predicate — **not because someone built a mind.**
>
> Which suggests, without proving: **intelligence, whatever it is, is only load-bearing where you
> cannot check the work.**

**The LLM-intelligence debate is structurally undecidable — and the framework says why.**

The invalid inference, which must be **refused explicitly**: *"LLMs decide on open predicates ∴ LLMs
are intelligent"* affirms the consequent, and worse — it treats **unverifiability as evidence for the
capacity that unverifiability makes unmeasurable.** A Magic 8-Ball also emits determinations on open
predicates. *Emitting is not the criterion.*

The real result:

> **You cannot benchmark your way across an open predicate — because a benchmark *is* a closing
> predicate.** Construct one and you have *closed* the predicate, moving the question into the region
> where degeneracy says intelligence is unnecessary.
>
> **Every measurable success is in the region where intelligence is unnecessary. Every claim of
> intelligence is in the region that is unmeasurable.** The evidence and the claim **never occupy the
> same territory** — and cannot, by construction.

It cuts **both** camps: the skeptics' dismissal is as unfalsifiable as the claim they dismiss (their
evidence would be failures on open predicates, equally ungradeable); and the believers' every
benchmark is *structurally evidence against its own relevance* — the better the score, the more
certainly it was reachable without the thing being demonstrated.

**Falsifiable:** exhibit an open predicate whose performance can nonetheless be reliably assessed (it
was not open), **or** show path-degeneracy fails on some closing predicate (adequacy is *not* cheap
there). Either kills it. Neither has been done.

**The framework declines the verdict.** *"Our theory proves LLMs are intelligent"* would travel
further than anything else in this repository. It is also false, and claiming it would forfeit the
framework's standing on everything else — which is the universal-solvent failure the admission tests
exist to prevent.

---

## 2. Superseded — do not cite these

| Claim | Status |
|---|---|
| *"Law of Conservation of Specification Demand"* as a physical-law claim | **Superseded** → "Principle," Tesler-derived, weak position only (§1.4) |
| *"There is no tacit knowledge in digital work"* | **Retired** → not defensible against Collins's collective TK |
| **The immune system as the *licensing instance*** for the general name | **Retired.** Immunologically wrong in two of four cells: negative selection is **leaky** (not a mechanical check); innate/adaptive is a **continuum** (not rules-vs-judgment). Use **CRISPR** instead. |
| *"Diversity buys coverage, redundancy buys reliability"* | **Superseded** → the named concept is **degeneracy** (Edelman & Gally 2001): *structurally different elements, same function* — which delivers **both** |
| The poisoned-ground **cross-domain unification** | **Retreated** → a *family*, not one mechanism. Opposite error directions must not be conflated. |
| Escape- vs. wind-hallucination as novel | **Cite the prior taxonomy** (Ji et al.; Huang et al.) — ours is a gloss |
| Quarks / quantum resonance | **Do not write it.** Fails both admission tests. The resemblance is **degeneracy** — a fact about many-to-one maps in mathematics, not evidence of determination. |

**Artifacts needing revision:** `determination.md` (§7 immune licensing — cut), `adversarial-ground.md`
(the unification — retreat to a family), `linkedin-plan.md` (post 4 and post 6 both lean on retreated
claims — see §4).

**Current `core/` set:**

| File | Contains | Status |
|---|---|---|
| `00-determination.md` | two primitives · admission tests · the four stores restated · the naming resolution · ensemble actors | **current**, except §7 (immune licensing) — **cut it** |
| `01-the-principle.md` | the conservation principle, weak position | needs the Tesler/Ashby attribution folded in |
| `03-the-floor.md` | the floor | **superseded** by the floor-in-the-predicate result (`core/04` §2) |
| `04-actors.md` | pinning spectrum · floor-in-predicate · selection vs. training · composite actors & seams · the compound loop · **re-indexing the classical results** | **current — the contribution** |
| `05-lineage-and-limits.md` | attribution · corrections · retreats · the falsification debts | **current** (= `ddd-revision.md`) |
| `06-determination-and-intelligence.md` | determination ≠ intelligence · the invalid inference refused · **the debate is structurally undecidable** | **current** |
| `closure-principle.md` | an actor's own output is not ground | current; cite **Kalman** |
| `adversarial-ground.md` | ground as attack surface | **retreat the unification** to "a family, not one mechanism" |

---

## 3. Attribution — required in every artifact

| Claim | Cite |
|---|---|
| Conservation of demand | **Tesler**, Conservation of Complexity; **Ashby**, Requisite Variety (the *measurable* ancestor) |
| Fixed by the task | **Brooks**, essential/accidental complexity |
| Encoded + Mechanical stores | **Meyer**, Design by Contract; **Hoare** logic *(more precise than we are)* |
| Where a check should live | **Saltzer, Reed & Clark**, End-to-End Argument |
| Poisoned ground | **Kalman** filter divergence; observability; the separation principle |
| The floor | **Polanyi**; **Collins** (relational / somatic / **collective**) |
| Zero-floor limits | **Rice's theorem**; **Xu et al. 2024**; **Kalai & Vempala** |
| Degeneracy | **Edelman & Gally**, *PNAS* 2001 |
| Immune tolerance is leaky | **Klein / Kyewski / Allen / Hogquist**, *Nat Rev Immunol* 2014 |
| Trained immunity (innate/adaptive is a continuum) | **Netea et al.** |

---

## 4. Corrections to the LinkedIn plan

The eight-post sequence stands, with three edits:

- **Post 4** (*spec ops earned the tier, your consultancy didn't*) — keep, but the mechanism is now
  **predicate closure**, not "adversarial ground." *Spec ops carries judgment because the acceptance
  predicate does not close; consulting carried judgment because nobody wrote the check.* Sharper, and
  it is now the same claim as §1.8.
- **Post 6** (*Every decision gets made*) — **do not present conservation as a discovery.** Present it
  as *"Tesler said this in the 80s about complexity. Here it is in decisions, with a fourth bin he
  didn't have — the one where nobody decides."* **The escaped store is the post.** Leading with a
  law you can't measure invites the exact rebuttal a sharp reader will reach for.
- **New post 9** (*Training vs. selection*) — **the strongest post in the set, and it was not there.**
  *"You can train a surgeon. You cannot train an elite soldier — you must select one. The difference
  is not difficulty. It is whether you can check the work."* Recognisable, counterintuitive, testable,
  and it introduces the actor model without vocabulary.

---

## 5. What is still owed

**The falsification debt, booked openly:**

1. **A counting procedure for governing decisions.** Until one exists and is shown invariant across
   two architectures for one task at one assurance level, "conservation" is an accounting identity,
   not a law. *The framework must say so in print.*
2. **Operationalise predicate closure.** §1.8's falsifiable claim needs an independent measure.
   Proposed proxies — **time-to-feedback**, **objectivity of the standard**, **stationarity of the
   standard** — are proxies, and must be conceded as such.
3. **The selection/training ratio, tested across professions.** This is *falsifiable from existing
   literature* — which **unblocks Paper A §6**, previously gated on evidence campaigns E1–E4.

**Product (see `ground-prd.md`):** rebuild Bicep on **compile-then-evaluate** (P0 — the current regex
parser violates the never-re-derive rule) · close the **`binds` join** · **live verification** of Key
Vault / App Config · **scheduled** verify · the **model-actor harvester**.

---

## 6. The one-line claim, final

> **The Conservation Principle of Determination Demand** — a generalisation of **Tesler's** Law of
> Conservation of Complexity, denominated in decisions, extended with a fourth allocation (the
> **escaped** store) and an assurance-level granularity bound. It holds as an accounting identity
> **within a fixed task decomposition**; the decomposition is itself the highest-leverage governing
> decision.
>
> Its rigorous ancestors are **Ashby** (requisite variety), **Brooks** (essential complexity),
> **Meyer** (contracts), and **Kalman** (observability).
>
> **Its contribution is the missing actor parameter** — and the two results that follow only from
> supplying it: **the intrinsic floor lives in the acceptance predicate** (so *selection intensity is
> inversely proportional to predicate closure*), and **seam demand allocates across the same four
> stores** (so *the compound requires a channel from judgment back into encoding*).
>
> **Its principal limit:** the floor is zero only where the acceptance predicate is decidable over
> digital ground — and whether it is, is in general undecidable.

Smaller. Correctly attributed. Harder to knock down. **More useful.**
