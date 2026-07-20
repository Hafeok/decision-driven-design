# Lineage, Attribution, Corrections, and Retreats

**Location:** `meta/lineage-and-limits.md`. This is the honesty layer — the record of what the
framework stands on, what external adversarial review corrected, and what it still owes. The edits
it prescribes have been applied across `core/00`–`core/06`; this document is the standing account of
*why* they were made.

**Purpose.** An adversarial review (external, literature-grounded) found real flaws. This
document does three things: **credits the prior art** the framework was reinventing, **corrects**
the claims that were wrong, and **retreats** the claims that overreached — keeping only what
survives. The goal is a framework that is smaller, correctly attributed, and harder to knock
down, rather than one that is impressive and brittle.

The governing principle for this revision: **cite where we are additive, retreat where we are
not, and never claim physical-law status for a heuristic.**

---

## 1. Lineage — what we are standing on

The framework is not sui generis. It is a **synthesis and re-tooling** of at least six prior
results, and it should say so plainly. For each: what they established, and what — if anything —
DDD adds.

### 1.1 Ashby — the Law of Requisite Variety (1956)

> *"Only variety can destroy variety."* A regulator must command at least as much variety as the
> disturbance it must absorb.

This is the **rigorous ancestor of conservation**, and it is *better than our version in the one
way that matters*: it has a **unit**. Ashby counts variety in states/bits and ties it to
Shannon's Theorem 10. Our "specification demand" has no counting procedure, which is exactly why
our "law" is weaker than his.

**What DDD adds:** an *allocation* vocabulary — Ashby says the variety must exist somewhere; we
say *where* it can live (four stores) and *who pays* for each. That is a real addition, but it is
downstream of Ashby, and we must credit him as the source of the conserved-quantity intuition.

**Honesty note:** Ashby himself refused physical-law status — he called requisite variety "an
information law, an expression of what is mathematically inevitable," not a law like Newton's. If
Ashby wouldn't claim it with a measurable quantity in hand, we cannot claim it without one.

### 1.2 Tesler — the Law of Conservation of Complexity (1980s)

> *"Every application has an inherent amount of irreducible complexity. The only question is who
> deals with it — the user, the developer, or the platform."*

This is the **nearest antecedent**, and it is nearly our exact claim with three bins instead of
four. Kay Hammer & Tina Timmerman independently reached the same ("conservation of complexity,"
2007).

**What DDD adds:** the fourth bin — **Escaped** — which Tesler did not have, and the explicit
**assurance-level** parameter that sets the granularity bound. Both are genuine, both are small.

**Correction:** we must stop presenting the conservation claim as a discovery. It is **Tesler's
Law, generalized to include the escaped store and denominated in decisions rather than
complexity.** State it that way, with credit, everywhere.

### 1.3 Brooks — essential vs. accidental complexity (1986)

> Essential complexity is inherent in the problem; accidental complexity is an artifact of tools
> and can be attacked. No single technique yields an order-of-magnitude gain against the
> essential part.

Supplies the *"fixed by the task, invariant to tooling"* half of conservation. Our "demand is
fixed by the task, never by the system" **is** Brooks's essence/accident line in decision
vocabulary.

**What DDD adds:** almost nothing to this specific claim. Credit Brooks as the source of
task-fixed invariance.

### 1.4 Meyer — Design by Contract (1986–92), on Hoare logic (1969)

Preconditions and postconditions are **exactly** our Encoded and Mechanical stores, formalized
decades earlier, with an implementation (Eiffel) and a proof theory (Hoare).

**Correction:** DDD adds **nothing** to the verification content of the encoded/mechanical
distinction. Design by Contract is more precise than we are. Our contribution near this seam is
only the *pairing with the other two stores* (judgment, escape) — the recognition that a decision
not covered by a contract still gets made, by an actor or by nobody. Credit Meyer and Hoare for
the contract halves.

### 1.5 Saltzer, Reed & Clark — the End-to-End Argument (1984)

Already answers *"at what layer should a function or check live"* — a sharper, older version of
our "by whom / when" question for the checking store. Later work (Moors, 2002) showed some
functions **migrate into the substrate and vanish as separate concerns** — which is our single
most important counterexample (see §3.1).

**What DDD adds:** generalization beyond network layers to actors of different kinds. Credit them
for the placement question.

### 1.6 Kalman / control theory — observability and estimator divergence (1960s)

This is the **rigorous ancestor of poisoned ground**, and it has what we lack: theorems. Filter
divergence is the precise, quantified statement of "an estimator that trusts its own model over
its measurements diverges" — the covariance can shrink to zero *while the actual error grows*.
The separation principle governs when estimation and control can be treated independently.

**Correction:** "poisoned ground" is **observability failure / estimator divergence**, applied to
software and organizations. Cite it. It gains us predictive content (divergence has *conditions*)
and it sheds the false unifications (§4).

### 1.7 Polanyi (1966) and Collins (2010) — tacit knowledge

Polanyi gave us "we know more than we can tell" — the floor. **Collins gave the taxonomy we must
respect:** relational tacit knowledge (contingently tacit, explicable in principle), somatic (body
/brain-limited, often machine-reproducible), and **collective** (embedded in society, which
Collins argues is the *only* genuinely irreducible kind and cannot be made explicit without
socialization).

**Correction:** our floor decomposition (intrinsic + transfer) maps onto *relational and somatic*
TK but **denies collective TK**, which Collins's whole program says exists. See §2.2.

---

## 2. Corrections — where the framework was wrong

### 2.1 "Law" → "Principle." No physical-law status without a measured quantity.

A conservation law names a quantity invariant under a symmetry (Noether) and measurable in
principle. We have named no such quantity and derived no invariance. Until a **counting procedure
for governing decisions** exists and is shown invariant across two genuinely different
architectures solving the same task, the correct word is **Principle** or **Heuristic**.

**Action:** rename to **The Conservation Principle of Determination Demand**, presented as
"Tesler's Law, generalized." Keep "Law" only in the informal engineering register, the way "Tesler's
Law" and "Ashby's Law" use it — as homage, not as a claim of physical status. Flag this explicitly
so no reader mistakes the register.

**The falsification debt, stated openly.** For the principle to be more than a vocabulary, it must
forbid one pre-registered observation. The candidate: *count the governing decisions for a fixed
task at a fixed assurance level under two different architectures; the principle predicts the
counts are equal.* Until that experiment is run, we concede the principle is an **organizing
vocabulary, not an empirical theory** — a respectable and still-useful status, and we say so.

### 2.2 The zero-floor postulate: retreat to the acceptance predicate

The original claim — *"if the governing decisions and the acceptance predicate both close over
digital ground, the intrinsic floor is zero"* — is the most-attacked and least-defensible as
stated. It survives only in a **narrowed** form, and the narrowing is itself the useful result.

Three limits, all real, and note that **none of them is about determinism** — they hold in a fully
deterministic universe, because they are about *decidability and knowability*, not about whether
the future is fixed:

- **Rice's theorem.** All non-trivial semantic properties of programs are undecidable, so the
  acceptance predicate can itself be uncomputable, and deciding whether it "closes" can require
  solving the halting problem. This is a theorem, true regardless of physics.
- **Inevitable model error** (Xu, Jain & Kankanhalli 2024; Kalai & Vempala). A calibrated model
  must err on rare facts, with a non-zero lower bound. Even the leading rebuttal (Suzuki et al.
  2025) reduces the probability to *negligible*, not zero. Both sides agree the floor is non-zero.
- **Collective tacit knowledge** (Collins). Cannot be rendered explicit without socialization;
  denying it in digital work is exactly the assertion Collins's program contradicts.

**On determinism specifically (the Nielsen argument).** A strong-determinism premise — *know every
variable and the future is fixed* — does **not** rescue zero-floor, for two reasons. First, it
imports the entire physical state, which is the opposite of "closes over *digital* ground": the
whole content of zero-floor is that the relevant ground is *small and closed*, and universal
determinism makes it *maximal and open*. Second, the objections above are about **decidability, not
predictability** — Rice's theorem and inevitable model error are true in a deterministic universe,
so determinism does not touch them. Determinism is the wrong tool against these objections.

**What survives, and it is worth keeping — the retreat is a sharpening.** The zero-floor property
is real, but it lives in the **acceptance predicate**, not the decision:

> **The intrinsic floor is zero for any decision whose *acceptance predicate is itself decidable
> over digital ground.* For those, path-degeneracy makes it robustly zero — infinitely many
> distinct determiners suffice, so no *particular* judgment is required. The floor is non-zero
> exactly when the acceptance predicate does not close — and whether it closes is, in general,
> undecidable.**

This is *better* than the original claim, because it locates the floor precisely: **the floor is a
property of the predicate, not of the decision.** "Does it compile," "is this valid JSON," "do the
tests pass" — decidable predicates, floor zero, and there path-degeneracy means the model needs no
particular judgment, only an adequate one. "Is this the right architecture," "is this secure
against an adversary who hasn't attacked yet" — the predicate does not close, and the floor is
non-zero *for that reason*.

This also **explains the immune-system correction below**: negative selection is *leaky* precisely
because "is this self?" is an acceptance predicate that does not cleanly close, so no mechanical
check can be exact, so a probabilistic actor plus peripheral tolerance must carry the residual. The
floor is non-zero there for exactly the reason the narrowed postulate predicts.

**Retire** "there is no tacit knowledge in digital work" as a slogan. Replace with: "the relational
and somatic tacit component can approach zero on decidable-predicate tasks; a floor remains from
undecidable predicates, inevitable model error, and collective tacit knowledge."

### 2.3 The immune system: rebuild on degeneracy, or retire

The mapping is inaccurate in two of four cells and must be fixed or dropped.

- **Negative selection is not mechanical verification.** It is a leaky, probabilistic,
  affinity-threshold process; self-reactive clones routinely escape (Klein/Kyewski/Allen/Hogquist,
  *Nat Rev Immunol* 2014). It behaves like a **thresholded probabilistic actor**, not a check.
  Autoimmunity is standing proof of the leak. *(This is now consistent with §2.2: the predicate
  doesn't close, so the check can't be exact.)*
- **Innate/adaptive is not rules-vs-judgment.** Trained immunity (Netea et al.) shows innate cells
  carry epigenetic memory; the field treats innate/adaptive as a continuum.
- **"Diversity buys coverage, redundancy buys reliability" is the wrong frame.** The correct,
  named concept is **degeneracy** (Edelman & Gally, *PNAS* 2001): *structurally different elements
  performing the same function*, which delivers coverage **and** reliability at once — dissolving
  the neat two-way split. Redundancy is *identical* elements (Tononi/Sporns/Edelman 1999).
- **V(D)J** is largely right as "encode the generator, not the determinations," but the dominant
  diversity source (junctional / N-nucleotide addition) is **non-templated and random** — the
  germline encodes the *machinery*, not the receptor.

**Action:** demote the immune system from "licensing instance" to "**suggestive parallel, with
known disanalogies.**" It does *not* license the general name; where checkable, it is distorted. If
retained at all, rebuild on **degeneracy + leaky selection**, and only keep a mapping that a
trained immunologist would endorse. The claim "a system with no engineer instantiates the stores"
is rhetorically attractive and **evidentially weak** — drop it as support.

### 2.4 Escape-hallucination vs. wind-hallucination: cite the existing taxonomy

This split re-labels the established **intrinsic/extrinsic** and **faithfulness/factuality**
distinctions (Ji et al.; Huang et al.). Keep our terms only if they add predictive content;
otherwise cite the existing taxonomy and note ours as a gloss. It is not demonstrably more
predictive, so **credit the prior taxonomy.**

---

## 3. The strongest counterexample, admitted

### 3.1 Architecture can *destroy* demand, not just relocate it

Conservation says demand is fixed by the task and can only move between stores. But **re-conceiving
the task boundary can eliminate whole classes of governing decisions:**

- Idempotent / content-addressed designs (Nix-style builds) delete ordering and rebuild decisions.
- CRDTs delete conflict-resolution and reconciliation decisions.
- Declarative substrates absorb functions that were application concerns (Moors 2002, on end-to-end).

If demand can be **destroyed** by re-drawing the task boundary, then "fixed by the task, invariant
to the system" is false — *unless* "task" is redefined post hoc to absorb the change, which is the
tautology trap.

**Resolution, stated honestly.** We concede one of two positions and must pick openly:

1. **Weak (defensible):** demand is conserved *for a fixed task decomposition*. Changing the
   decomposition changes the demand. This is true, useful, and no longer a "law" — it is an
   accounting identity within a chosen boundary.
2. **Strong (indefensible):** demand is fixed by "the task itself" independent of decomposition.
   This is false, per the counterexamples, unless rescued by tautology.

**We take position 1.** Conservation holds *within a decomposition*; choosing the decomposition is
itself a governing decision (the highest-leverage one), and a better decomposition genuinely
lowers total demand. This is consistent with Brooks (you cannot remove *essential* complexity, but
the boundary of "essential" moves when you re-conceive the problem) and it is the correct
engineering advice anyway: **the decomposition is the decision that matters most.**

---

## 4. Poisoned ground: keep the mechanism, drop the unification

The core — *"consuming your own prior output as ground creates uncorrectable error"* — is correct
and is **estimator divergence / observability failure**. Cite Kalman.

**Drop the cross-domain unification** as stated. TOCTOU (concurrency/atomicity), molecular mimicry
(a *false negative* — foreign read as self), and autoimmunity (a *false positive* — self attacked
as foreign) are **not one mechanism**; grouping opposite error directions under one label is the
universal-solvent failure mode. Keep each as a separate instance of "verification and use are
separated in time / the substrate is not what the actor believes," but stop claiming they are the
same thing. The honest statement:

> Poisoned ground is a *family* of failures unified only by **the actor's model of the ground
> having diverged from the ground**. The *direction* and *mechanism* of divergence differ by
> domain and must not be conflated.

---

## 5. What survives, and is genuinely ours

Stated without inflation. After the corrections, the defensible contributions are:

1. **The four-store allocation lens as a design-review instrument.** For each governing decision:
   encoded, checked, judged, or escaped — and is that the cheapest correct home at this assurance
   level? This is good ergonomics even though the partition is definitional.
2. **The Escaped store.** Naming *"decided by nobody = latent defect exposure"* as a first-class
   category is the framework's clearest original contribution. Tesler didn't have it; it makes
   implicit risk nameable.
3. **The floor-is-in-the-predicate sharpening** (§2.2). Locating the intrinsic floor in the
   *decidability of the acceptance predicate* rather than in the decision is a genuine and useful
   result, and it is *ours* even though it is built from Rice + Collins + degeneracy.
4. **The encode-vs-verify discipline for uncontrolled ground**, operationalized in the `ground`
   tool. This is the end-to-end argument plus estimator-divergence, made concrete and shippable.
5. **Prompt-caching architecture** (stable prefix / volatile suffix). Correct, material,
   well-supported.

Everything else is either prior art we should cite (conservation, contracts, requisite variety,
observability) or overreach we should retreat (physical-law status, the immune licensing claim,
the cross-domain unification, universal "act is a decision" as anything more than a framing).

---

## 6. Required citations (add to every artifact that uses the corresponding claim)

| Claim in DDD | Cite | Register |
|---|---|---|
| Conservation of demand | **Tesler**, Law of Conservation of Complexity; **Ashby**, Requisite Variety | "generalizing Tesler; the measurable ancestor is Ashby" |
| Fixed by the task | **Brooks**, essential/accidental complexity | direct antecedent |
| Encoded + Mechanical stores | **Meyer**, Design by Contract; **Hoare** logic | DbC is more precise; we add only the pairing |
| Where a check should live | **Saltzer, Reed & Clark**, End-to-End Argument | older, sharper form of the placement question |
| Poisoned ground | **Kalman** filter divergence; observability; separation principle | the rigorous ancestor; we add a name |
| The floor | **Polanyi**; **Collins** (relational/somatic/collective TK) | we must respect collective TK |
| Zero-floor limits | **Rice's theorem**; **Xu et al. 2024**; **Kalai & Vempala** | these bound the postulate |
| Immune degeneracy | **Edelman & Gally**, *PNAS* 2001; **Tononi/Sporns/Edelman** 1999 | replaces diversity/redundancy |
| Immune tolerance is leaky | **Klein/Kyewski/Allen/Hogquist**, *Nat Rev Immunol* 2014 | corrects the "mechanical check" cell |
| Hallucination taxonomy | **Ji et al.**; **Huang et al.** | our terms are a gloss on theirs |

---

## 7. The revised one-line claim

Before:

> *The Law of Conservation of Specification Demand.*

After:

> **The Conservation Principle of Determination Demand** — a generalization of Tesler's Law of
> Conservation of Complexity, denominated in decisions rather than complexity, extended with a
> fourth allocation (the *escaped* store) and an assurance-level granularity bound. It holds as an
> accounting identity *within a fixed task decomposition*; the decomposition is itself the
> highest-leverage governing decision. Its rigorous ancestors are Ashby (requisite variety),
> Brooks (essential complexity), Meyer (contracts), and Kalman (observability). Its principal
> limit: the intrinsic floor is zero only where the acceptance predicate is decidable over digital
> ground — and whether it is, is in general undecidable.

Smaller. Correctly attributed. Harder to knock down. More useful.
