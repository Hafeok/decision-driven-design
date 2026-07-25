# Lineage, Attribution, Corrections, and Retreats

**Location:** `meta/lineage-and-limits.md`. This is the honesty layer — the record of what the
framework stands on, what external adversarial review corrected, and what it still owes. The edits
it prescribes have been applied across `core/00`–`core/07`; this document is the standing account of
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
functions **migrate into the substrate**, appearing there as part of its interface contract rather
than as separate application concerns — which was booked as our single most important
counterexample, and is resolved as relocation into the seam (see §3.1).

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

**Why §1.8–§1.11 exist.** v4.1 (`core/09-the-measure.md`) and v4.2 (`core/10-the-floor-mechanism.md`) rest
almost entirely on information theory. Prior to this addendum, **Shannon appeared exactly once in the
repository** — as a passing mention inside the Ashby section. That is an attribution failure of the
same kind the framework corrected in v4.0, and it is corrected here on the same principle: **cite
where we are additive, retreat where we are not.**

The governing sentence for both new results:

> **The mathematics is Shannon's. The claim is the *identification* — that specification demand *is*
> verdict entropy, seam demand *is* mutual information, and resolve-overflow error *is* the
> rate-distortion bound. Those identifications are modelling claims, they are falsifiable, and they
> were tested. They are not mathematical discoveries.**

### 1.8 Shannon — information theory (1948)

**"A Mathematical Theory of Communication," *Bell System Technical Journal* 27.**

This is the foundation of everything in `core/09` and `core/10`. Specifically:

- **Entropy `H(X)`** — the measure of information in a random variable. `core/09` identifies
  *specification demand* with `H(verdict)`. The unit (bits) is Shannon's; the quantity is Shannon's;
  the identification with demand is ours.
- **Conditional entropy `H(X|Y)` and mutual information `I(X;Y)`** — `core/09` identifies *runtime
  demand of the parts* with `H(verdict|S)` and *seam demand* with `I(verdict;S)`.
- **The chain rule**, `H(X) = H(X|Y) + I(X;Y)` — **this is what the framework calls "conservation."**
  Conservation of specification demand, in the closing-predicate case, **is the chain rule of
  entropy.** It is a theorem of 1948, not a discovery of this framework.

**What DDD adds:** the identification, and the observation that three of the framework's separately
stated claims (the seam identity, actor-relative store allocation, and the encode/verify split) are
the same chain rule under three different conditioning variables. That mapping could have failed. It
did not. **That is the contribution, and it is not the theorem.**

**Correction to earlier framing:** any presentation of `core/09` that leads with "conservation is a
theorem" without immediately naming Shannon is misleading. Lead with: *"conservation, on the
closing-predicate region, is Shannon's chain rule — here is why that identification holds."*

### 1.9 Shannon — rate-distortion theory (1948, 1959)

**"Coding Theorems for a Discrete Source with a Fidelity Criterion," IRE Nat. Conv. Rec. (1959).**

`core/10` §4.1 derives the per-decision error rate under resolve-overflow as

> `p_err = H_b⁻¹(1 − r)`, `r = C_resolve / n`

This is the **inverse of the binary rate-distortion function** `R(D) = 1 − H_b(D)` for a Bernoulli(½)
source under Hamming distortion. It is Shannon's result. It gives the *information-theoretic lower
bound* on achievable error at a given rate — no actor can do better.

**What DDD adds:** the identification of *actor resolve capacity* with a channel rate, and therefore
of *overflow escape* with forced rate-distortion. Also the observation that the hard-capacity model
(chance error on shed decisions) is the `r → 0` limit of the same bound — the two regimes are one
model.

**What DDD must not claim:** that it derived a bound on error under capacity limits. It applied one.

### 1.10 Cover & Thomas — the standard treatment

**"Elements of Information Theory" (1991, 2nd ed. 2006).**

The canonical reference for the chain rule, conditional entropy, mutual information, and
rate-distortion as used throughout `core/09` and `core/10`. Any formal write-up should cite this for
the machinery rather than re-deriving it, and any reviewer will expect it.

### 1.11 Hallucination taxonomies — prior art for `core/10` §6

`core/10` decomposes hallucination into three causes (missing / poisoned / overflowed ground). The
existing literature already partitions hallucination, and must be credited:

- **Ji et al. (2023), "Survey of Hallucination in Natural Language Generation," *ACM Computing
  Surveys*** — the intrinsic/extrinsic and faithfulness/factuality distinctions.
- **Huang et al. (2023), "A Survey on Hallucination in Large Language Models"** — the extended
  taxonomy.
- **Xu, Jain & Kankanhalli (2024), "Hallucination is Inevitable"** and **Kalai & Vempala** — the
  non-zero lower bound on model error, already cited in `core/03`, and the reason `core/10`'s escape
  cannot be driven to zero by capacity alone.

**What DDD adds — and the honest limit of the claim.** The three-cause decomposition is *causal and
derived from the store model* (a decision is made without correct ground iff the ground is absent,
false, or unresolved), and it attaches a **different remedy to each cause** — add / re-verify /
encode. That actionable split is the contribution. It is **not** a claim to have discovered that
hallucinations have kinds; the surveys above already established that. Where DDD's categories overlap
theirs, cite theirs.

*Note also the standing correction from v4.0: the earlier "escape-hallucination vs.
wind-hallucination" split was a relabelling of the existing taxonomy and was retreated. The
three-cause version supersedes it and is defensible **because** it is derived rather than observed —
but it still cites the surveys.*

### 1.12 Martin — the Stable Dependencies Principle (1990s; Agile Software Development, 2002)

"Depend in the direction of stability." A package should depend only on packages more stable
than itself; instability I = Ce/(Ca+Ce).

apparatus/prefix-stability.md applies this to cached prefixes, which are totally-ordered
dependency chains by mechanism (causal attention).

What DDD adds: (a) a substitute instability metric that fits a prefix, since Martin's
afferent/efferent coupling ratio does not transfer — instability = expected RE-DERIVATION RATE;
(b) the observation that the cache makes SDP violations MEASURABLE rather than a design smell,
with an immediate cost equal to the length of everything after the mislocated content; and
(c) the diagnostic that an SDP violation in a prefix is simultaneously a cache defect and a
SPECIFICATION defect.

What DDD must not claim: the ordering principle. That is Martin's.

### 1.13 Smith — the weighted shortest processing time rule (1956)

W. E. Smith, "Various optimizers for single-stage production," Naval Research Logistics
Quarterly 3.

The optimal prefix ordering in apparatus/prefix-stability.md §3 is Smith's rule: sort by
ascending (weight / processing time) — here, ascending (re-derivation rate / length).

NOTE A CORRECTION: an earlier formulation of this result claimed ascending RE-DERIVATION RATE
was optimal. That is false, and brute-force search falsifies it whenever a volatile segment is
long. The correct rule is the per-token normalisation, which is Smith's, established in 1956.
The framework applied a known scheduling result; it did not derive a new one.

### 1.14 DORA / Forsgren, Humble & Kim — the DevOps research programme

Accelerate (2018) and the annual State of DevOps reports.

applications/sdlc/production-as-ground.md reads DORA's four key metrics as instrumentation of the
encode/verify gap, and treats DORA's findings as external corroboration.

What DDD adds: an explanation of WHY the metrics work (§2-3), and one derived prediction DORA has
not tested (§7). What DDD explicitly does NOT add: the batch-size result, which predates both and
belongs to Reinertsen and Lean queueing theory (§5). The framework offers a redescription there,
not an explanation DORA lacks, and says so.

The DORA correspondence is retrodiction against PUBLISHED findings. DORA's response-level data is
not public; no statistical validation was performed and none is claimed.

### 1.15 Reinertsen — product development flow / queueing theory

The batch-size and feedback-latency results. Cited so that production-as-ground does not appear to
claim them.

### Additional context worth acknowledging

Two adjacent literatures that a reviewer will raise, and which the framework should acknowledge
rather than be caught by:

- **Minimum description length / Kolmogorov complexity** (Solomonoff, Kolmogorov, Rissanen) — an
  alternative formalisation of "how much specification does this task require." `core/09` uses
  Shannon entropy over a ground distribution instead, which is *weaker but computable*. Worth a
  sentence in any paper explaining the choice: MDL would give a distribution-free measure but is
  uncomputable; entropy is distribution-relative but calculable, which is what let us actually
  compute the worked examples.
- **Bounded rationality** (Simon, 1955) and **rational inattention** (Sims, 2003) — the economics
  literature on agents with limited information-processing capacity, where Sims in particular models
  attention as a Shannon channel with finite capacity. This is close prior art for `core/10`'s
  capacity model and should be cited: **the move of treating a decision-maker's capacity as an
  information channel is Sims's, not ours.** DDD's addition is the *verifier* condition — that
  capacity overflow only produces escape where no check catches the shed decision.

### The register sentence, for every future write-up

> **`core/09` and `core/10` are applied information theory. Shannon supplied the entropy, the chain
> rule, and the rate-distortion bound; Sims supplied the channel model of a capacity-limited
> decision-maker. What this framework contributes is the identification of specification demand with
> verdict entropy, of seam demand with mutual information, and of escape with the intersection of
> rate-distortion-forced error and absent verification — together with the demonstration that those
> identifications hold without leftover on worked examples. The mathematics is not ours. The mapping
> is, and the mapping is what is falsifiable.**

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

## 3. The strongest counterexample, resolved

### 3.1 Architecture relocates demand into the seam — the counterexample, resolved

This was booked as the strongest counterexample to conservation, and `core/09` §4 resolves it. The
examples are real; the destruction reading was an artifact of counting the parts and not the seam.

- **Content-addressed designs** (Nix-style builds) do not delete ordering decisions. They make the
  determination once, in deciding **what constitutes identity of a build input** — whether timestamps,
  build paths, or compiler versions are inside the hash. That is where the difficulty of such systems
  is known to concentrate.
- **CRDTs** do not delete conflict-resolution decisions. They make the determination once, in the
  choice between add-wins, remove-wins, and last-writer-wins semantics. That is where the difficulty
  of CRDT design is known to concentrate.
- **Declarative substrates** absorb application concerns into the substrate's own interface contract,
  which is the seam under another name.

In each case the determination moved into the **seam**: the interface contract the decomposition
brings into existence. Count the seam and the total is invariant. The parts are cheaper because
somebody pre-paid.

**The resolution is no longer a choice between a weak and a strong position.** For any conditioning
variable, `H(V) = I(V;X) + H(V|X)`; a decomposition is such a variable; the total is therefore
invariant by the chain rule, not by concession (`core/09` §4). What genuinely changes the total is
changing the task or the declared tolerance — not re-drawing boundaries within one.

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
| Demand = verdict entropy; the unit (bits) | **Shannon 1948** | the measure is his; the identification is ours |
| Conservation = chain rule; seam = mutual information | **Shannon 1948**; **Cover & Thomas** | *the theorem is Shannon's* — say so first |
| `p_err` under resolve-overflow | **Shannon 1959** (rate-distortion) | we applied a bound, did not derive one |
| Capacity as an information channel | **Sims 2003** (rational inattention); **Simon 1955** | the channel model of a decision-maker is Sims's |
| Hallucination has kinds | **Ji et al. 2023**; **Huang et al. 2023** | our contribution is the *causal* split + distinct remedies |
| Error cannot be driven to zero | **Xu et al. 2024**; **Kalai & Vempala** | already cited in `core/03`; also bounds `core/10` |
| Alternative demand formalisation | **Kolmogorov / MDL** | acknowledge the road not taken, and why |
| Prefix ordering by stability | Martin (SDP) | the ordering principle is his |
| The optimal ordering is rate/length | Smith 1956 (WSPT) | a known scheduling result, applied |
| DORA metrics read as demand | Forsgren/Humble/Kim, DORA reports | corroboration; the explanation is ours, the findings are theirs |
| Batch size, feedback latency | Reinertsen; Lean | NOT our contribution — redescription only |

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
