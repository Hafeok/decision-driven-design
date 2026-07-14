# Lineage and Limits

> **Core §5 — normative.** What the framework is standing on, where it was wrong and has been corrected, where it overreached and has retreated, and what it still owes. An external, literature-grounded adversarial review found real flaws; this chapter credits the prior art the framework was reinventing, records the corrections applied to the other chapters, and books the falsification debts openly. The governing principle: **cite where we are additive, retreat where we are not, and never claim physical-law status for a heuristic.**

**Read this as the ledger for the framework's own claims.** Where it conflicts with an older phrasing elsewhere in the repository, this chapter and the chapters it corrects ([the law](01-the-law.md), [the floor](03-the-polanyi-floor.md), [actors](04-actors.md), [escape under pressure](escape-under-pressure.md)) win.

---

## 1. Lineage — what we are standing on

The framework is not sui generis. It is a **synthesis and re-tooling** of at least six prior results, and it should say so plainly. For each: what they established, and what — if anything — DDD adds. The single contribution that is genuinely ours is the **actor parameter** ([§4](04-actors.md)) and the two results that follow only from supplying it; everything else below is prior art we index, not prior art we replace.

### 1.1 Ashby — the Law of Requisite Variety (1956)

> *"Only variety can destroy variety."* A regulator must command at least as much variety as the disturbance it must absorb.

This is the **rigorous ancestor of conservation**, and it is *better than our version in the one way that matters*: it has a **unit**. Ashby counts variety in states/bits and ties it to Shannon's Theorem 10. Our "determination demand" has no counting procedure, which is exactly why our "law" is weaker than his.

**What DDD adds:** an *allocation* vocabulary — Ashby says the variety must exist somewhere; we say *where* it can live (four stores) and *who pays* for each. Real, but downstream of Ashby.

**Honesty note:** Ashby himself refused physical-law status — he called requisite variety "an information law, an expression of what is mathematically inevitable," not a law like Newton's. If Ashby wouldn't claim it with a measurable quantity in hand, we cannot claim it without one.

### 1.2 Tesler — the Law of Conservation of Complexity (1980s)

> *"Every application has an inherent amount of irreducible complexity. The only question is who deals with it — the user, the developer, or the platform."*

The **nearest antecedent** — nearly our exact claim with three bins instead of four (Kay Hammer & Tina Timmerman reached the same independently, 2007).

**What DDD adds:** the fourth bin — **Escaped** — which Tesler did not have, and the explicit **assurance-level** parameter that sets the granularity bound. Both are genuine, both are small.

**Correction:** stop presenting the conservation claim as a discovery. It is **Tesler's Law, generalized to include the escaped store and denominated in decisions rather than complexity.** State it that way, with credit, everywhere. This is the register correction now folded into [the law](01-the-law.md#register-and-lineage) and the [README](../README.md).

### 1.3 Brooks — essential vs. accidental complexity (1986)

Essential complexity is inherent in the problem; accidental complexity is an artifact of tools. Supplies the *"fixed by the task, invariant to tooling"* half of conservation. Our "demand is fixed by the task, never by the system" **is** Brooks's essence/accident line in decision vocabulary. **What DDD adds:** almost nothing to this specific claim. Credit Brooks as the source of task-fixed invariance.

### 1.4 Meyer — Design by Contract (1986–92), on Hoare logic (1969)

Preconditions and postconditions are **exactly** our Encoded and Mechanical stores, formalized decades earlier, with an implementation (Eiffel) and a proof theory (Hoare). **Correction:** DDD adds **nothing** to the verification content of the encoded/mechanical distinction — Design by Contract is more precise than we are. Our contribution near this seam is only the *pairing with the other two stores* (judgment, escape): the recognition that a decision not covered by a contract still gets made, by an actor or by nobody.

### 1.5 Saltzer, Reed & Clark — the End-to-End Argument (1984)

Already answers *"at what layer should a function or check live"* — a sharper, older version of our "by whom / when" question for the checking store. Later work (Moors, 2002) showed some functions **migrate into the substrate and vanish as separate concerns** — our single most important counterexample (see §3). **What DDD adds:** generalization beyond network layers to actors of different kinds.

### 1.6 Kalman / control theory — observability and estimator divergence (1960s)

The **rigorous ancestor of the escaped store's poisoned-ground failure**, and it has what we lack: theorems. Filter divergence is the precise, quantified statement of "an estimator that trusts its own model over its measurements diverges" — the covariance can shrink to zero *while the actual error grows*. The separation principle governs when estimation and control can be treated independently. **Correction:** what [escape under pressure](escape-under-pressure.md) calls a decision falling to the prior, when the prior is the actor's own stale model of the ground, **is** observability failure / estimator divergence. Cite it. It gains us predictive content (divergence has *conditions*).

### 1.7 Polanyi (1966) and Collins (2010) — tacit knowledge

Polanyi gave us "we know more than we can tell" — the [floor](03-the-polanyi-floor.md). **Collins gave the taxonomy we must respect:** relational tacit knowledge (contingently tacit, explicable in principle), somatic (body/brain-limited, often machine-reproducible), and **collective** (embedded in society, which Collins argues is the *only* genuinely irreducible kind and cannot be made explicit without socialization). **Correction:** our floor decomposition (intrinsic + transfer) maps onto *relational and somatic* TK but must not **deny collective TK**, which Collins's whole program says exists. See §2.2.

---

## 2. Corrections — where the framework was wrong

### 2.1 "Law" → "Principle." No physical-law status without a measured quantity.

A conservation law names a quantity invariant under a symmetry (Noether) and measurable in principle. We have named no such quantity and derived no invariance. Until a **counting procedure for governing decisions** exists and is shown invariant across two genuinely different architectures solving the same task, the correct word is **Principle** or **Heuristic**.

**Action, applied:** [the law](01-the-law.md#register-and-lineage) now presents conservation as **the Conservation Principle of Determination Demand — Tesler's Law, generalized** — and keeps "Law" only in the informal engineering register, the way "Tesler's Law" and "Ashby's Law" use it: as homage, not as a claim of physical status, flagged so no reader mistakes the register.

**The falsification debt, stated openly.** For the principle to be more than a vocabulary it must forbid one pre-registered observation. The candidate: *count the governing decisions for a fixed task at a fixed assurance level under two different architectures; the principle predicts the counts are equal.* Until that experiment is run, we concede the principle is an **organizing vocabulary, not an empirical theory** — a respectable and still-useful status, and we say so. See §5.

### 2.2 The zero-floor postulate: retreat to the acceptance predicate

The original claim — *"if the governing decisions and the acceptance predicate both close over digital ground, the intrinsic floor is zero"* — was the most-attacked and least-defensible as stated. It survives only in a **narrowed** form, and the narrowing is itself the useful result.

Three limits, all real, and **none of them is about determinism** — they hold in a fully deterministic universe, because they are about *decidability and knowability*, not about whether the future is fixed:

- **Rice's theorem.** All non-trivial semantic properties of programs are undecidable, so the acceptance predicate can itself be uncomputable, and deciding whether it "closes" can require solving the halting problem.
- **Inevitable model error** (Xu, Jain & Kankanhalli 2024; Kalai & Vempala). A calibrated model must err on rare facts, with a non-zero lower bound. Even the leading rebuttal (Suzuki et al. 2025) reduces the probability to *negligible*, not zero.
- **Collective tacit knowledge** (Collins). Cannot be rendered explicit without socialization; denying it in digital work is exactly the assertion Collins's program contradicts.

**On determinism specifically.** A strong-determinism premise — *know every variable and the future is fixed* — does **not** rescue zero-floor. First, it imports the entire physical state, the opposite of "closes over *digital* ground": the whole content of zero-floor is that the relevant ground is *small and closed*, and universal determinism makes it *maximal and open*. Second, the objections above are about **decidability, not predictability** — they are true in a deterministic universe, so determinism does not touch them.

**What survives, and it is worth keeping — the retreat is a sharpening.** The zero-floor property is real, but it lives in the **acceptance predicate**, not the decision:

> **The intrinsic floor is zero for any decision whose *acceptance predicate is itself decidable over digital ground.* For those, path-degeneracy makes it robustly zero — infinitely many distinct determiners suffice, so no *particular* judgment is required. The floor is non-zero exactly when the acceptance predicate does not close — and whether it closes is, in general, undecidable.**

This is *better* than the original claim, because it locates the floor precisely. "Does it compile," "is this valid JSON," "do the tests pass" — decidable predicates, floor zero, and there path-degeneracy means the model needs no particular judgment, only an adequate one. "Is this the right architecture," "is this secure against an adversary who hasn't attacked yet" — the predicate does not close, and the floor is non-zero *for that reason*. **Action, applied:** [the floor chapter](03-the-polanyi-floor.md#the-zero-floor-postulate-the-floor-is-in-the-predicate) now carries the narrowed postulate; [actors §2](04-actors.md#2-the-floor-is-in-the-predicate) draws the selection/training consequence from it.

**Retire** "there is no tacit knowledge in digital work" as a slogan. Replace with: "the relational and somatic tacit component can approach zero on decidable-predicate tasks; a floor remains from undecidable predicates, inevitable model error, and collective tacit knowledge."

### 2.3 The escape/wind taxonomy: cite the existing taxonomy

The [escape / wind split](escape-under-pressure.md#the-taxonomy-escape-versus-wind) re-labels the established **intrinsic/extrinsic** and **faithfulness/factuality** hallucination distinctions (Ji et al.; Huang et al.). Our terms are kept only because they add *allocation-predictive* content — escape-class is reducible by re-allocating stores, wind-class is not — but the taxonomy itself is prior art and must be cited as such. Ours is a gloss with a predictive rider, not a discovery.

### 2.4 A note on retreats carried by other forks

Some corrections the review prescribes have **no target in this repository** and are recorded here only so the ledger is complete. The framework in other forks carried an *immune-system licensing* claim (that a system with no engineer instantiates the four stores), a *"diversity buys coverage, redundancy buys reliability"* slogan, and a *cross-domain unification* of poisoned ground (TOCTOU, molecular mimicry, autoimmunity as one mechanism). **All three are retreated.** This repo never made them: [`apparatus/composition/seam-allocation.md`](../apparatus/composition/seam-allocation.md) already uses the correct wind/floor **correlation** treatment (redundancy averages down independent error, ratifies correlated error), and [`apparatus/biology-contrast.md`](../apparatus/biology-contrast.md) is about drives, not immune licensing. The correct named concept, where any of this is discussed, is **degeneracy** (Edelman & Gally, *PNAS* 2001: structurally different elements, same function — which delivers coverage *and* reliability at once), and poisoned ground is a **family** of failures unified only by *the actor's model of the ground having diverged from the ground* — the *direction* and *mechanism* of divergence differ by domain and must not be conflated.

---

## 3. The strongest counterexample, admitted

**Architecture can *destroy* demand, not just relocate it.** Conservation says demand is fixed by the task and can only move between stores. But re-conceiving the task boundary can eliminate whole classes of governing decisions: idempotent / content-addressed designs (Nix-style builds) delete ordering and rebuild decisions; CRDTs delete conflict-resolution decisions; declarative substrates absorb functions that were application concerns (Moors 2002). If demand can be **destroyed** by re-drawing the task boundary, then "fixed by the task, invariant to the system" is false — *unless* "task" is redefined post hoc, which is the tautology trap.

**Resolution, taken openly.** We take the **weak, defensible position**: demand is conserved *for a fixed task decomposition*. Changing the decomposition changes the demand; a better decomposition genuinely *lowers* total demand. This is no longer a "law" — it is an accounting identity within a chosen boundary. **Choosing the decomposition is itself a governing decision — the highest-leverage one.** Consistent with Brooks (you cannot remove *essential* complexity, but the boundary of "essential" moves when you re-conceive the problem), and it is the correct engineering advice anyway. **Action, applied:** [the law](01-the-law.md#the-decomposition-is-the-highest-leverage-decision) now states the fixed-decomposition scope explicitly.

---

## 4. What survives, and is genuinely ours

Stated without inflation. After the corrections, the defensible contributions:

1. **The four-store allocation lens as a design-review instrument.** For each governing decision: encoded, checked, judged, or escaped — and is that the cheapest correct home at this assurance level? Good ergonomics even though the partition is definitional, not a discovery.
2. **The Escaped store.** Naming *"decided by nobody = latent defect exposure"* as a first-class category is the framework's clearest original contribution over Tesler.
3. **The actor parameter** ([§4](04-actors.md)) — and the two results that follow only from it: **the floor lives in the acceptance predicate** (so *selection intensity is inversely proportional to predicate closure*), and **seam demand allocates across the same four stores** (so *the compound requires a channel from judgment back into encoding*). This is the part with the least prior art.
4. **The encode-vs-verify discipline for uncontrolled ground.** *You can encode ground you control; you must mechanically verify ground you do not.* The end-to-end argument plus estimator-divergence, made concrete: any uncontrolled ground is two facts — your pinned copy and the mutable source of truth — and a lockfile pins the first, never the second.

Everything else is either prior art we cite (conservation, contracts, requisite variety, observability) or overreach retreated (physical-law status, the immune licensing claim, the cross-domain unification).

---

## 5. What is still owed

The falsification debt, booked openly:

1. **A counting procedure for governing decisions.** Until one exists and is shown invariant across two architectures for one task at one assurance level, "conservation" is an accounting identity, not a law. The framework says so in print (§2.1).
2. **Operationalise predicate closure.** [Actors §3](04-actors.md#3-selection-and-training)'s falsifiable claim needs an independent measure. Proposed proxies — **time-to-feedback**, **objectivity of the standard**, **stationarity of the standard** — are proxies, and are conceded as such.
3. **The selection/training ratio, tested across professions.** This is *falsifiable from existing literature* — the cheapest debt to discharge, and the one that most directly tests the actor contribution.

---

## 6. Required citations

Add to every artifact that uses the corresponding claim.

| Claim in DDD | Cite | Register |
|---|---|---|
| Conservation of demand | **Tesler**, Conservation of Complexity; **Ashby**, Requisite Variety | generalizing Tesler; the measurable ancestor is Ashby |
| Fixed by the task | **Brooks**, essential/accidental complexity | direct antecedent |
| Encoded + Mechanical stores | **Meyer**, Design by Contract; **Hoare** logic | DbC is more precise; we add only the pairing |
| Where a check should live | **Saltzer, Reed & Clark**, End-to-End Argument | older, sharper form of the placement question |
| Poisoned ground / escaped-store prior | **Kalman** filter divergence; observability; separation principle | the rigorous ancestor; we add a name and actor-generality |
| The floor | **Polanyi**; **Collins** (relational / somatic / **collective** TK) | we must respect collective TK |
| Zero-floor limits | **Rice's theorem**; **Xu et al. 2024**; **Kalai & Vempala** | these bound the postulate |
| Path-degeneracy / degeneracy | **Edelman & Gally**, *PNAS* 2001 | structurally different elements, same function |
| Hallucination taxonomy | **Ji et al.**; **Huang et al.** | our escape/wind terms are a gloss on theirs |

---

## 7. The one-line claim, final

> **The Conservation Principle of Determination Demand** — a generalization of **Tesler's** Law of Conservation of Complexity, denominated in decisions rather than complexity, extended with a fourth allocation (the **escaped** store) and an assurance-level granularity bound. It holds as an accounting identity **within a fixed task decomposition**; the decomposition is itself the highest-leverage governing decision.
>
> Its rigorous ancestors are **Ashby** (requisite variety), **Brooks** (essential complexity), **Meyer** (contracts), and **Kalman** (observability). **Its contribution is the missing actor parameter** — and the two results that follow only from supplying it: **the intrinsic floor lives in the acceptance predicate** (so *selection intensity is inversely proportional to predicate closure*), and **seam demand allocates across the same four stores** (so *the compound requires a channel from judgment back into encoding*).
>
> **Its principal limit:** the floor is zero only where the acceptance predicate is decidable over digital ground — and whether it is, is in general undecidable.

Smaller. Correctly attributed. Harder to knock down. More useful.
