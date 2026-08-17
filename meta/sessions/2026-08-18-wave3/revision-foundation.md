# The Missing Parameter: Actor-Indexed Determination

## Revision foundation and continuation draft

**Purpose.** This document replaces the vulnerable conceptual foundation of `paper-a-draft.md` while preserving its strongest contribution: determination is not a property of a task alone. It is relative to a system arrangement, the ground available to that arrangement, the relation used to judge acceptance, and the assurance level being demanded.

This is not yet a complete submission manuscript. It is a revised foundation, a set of defensible propositions, and a structure for completing the remaining sections without rebuilding the paper around a brittle program–model–human taxonomy.

---

## Revised abstract

Several influential accounts of complexity, control, and verification describe where the work of determination resides while holding the determiner largely fixed. We propose that this omission has become consequential as engineered systems increasingly combine authored procedures, learned policies, human judgment, mechanical checks, and institutional principals.

We introduce **actor-indexed determination**: the claim that unresolved determination is relative not only to a task, but to a tuple consisting of a system arrangement, accessible ground, an acceptance relation, a declared tolerance, and an assurance requirement. We distinguish three levels at which behavioural commitments may be attached—outcome, policy, and principal—and separate the source of a resolution from the mechanism used to assure it. This yields a precise account of an **escaped decision**: a consequential resolution that is neither intentionally governed nor adequately checked at the declared assurance level.

We then distinguish logical, operational, economic, and normative closure. A sound operational checker can reduce dependence on producer identity for the property it checks, but it does not imply that acceptable candidates are cheap to generate, that the acceptance region is dense, or that the predicate captures every relevant value. This separation supports a graded empirical hypothesis: as operational evaluability, feedback density, and ground accessibility increase, comparative advantage should shift toward systems able to generate candidates and exploit direct verification; as they decrease, performance and trust should depend increasingly on situated judgment and accountability-complete institutional arrangements.

The paper’s contribution is therefore not a new species taxonomy of programs, models, and humans. It is a framework for analysing where consequential choices are resolved, how commitments attach, what can be verified, who bears the residual consequence, and which parts of determination remain actor-relative.

---

## 1. The parameter hidden by a fixed arrangement

Ashby’s regulator has no species.

It is described by the variety it can absorb, not by whether that variety is supplied by a governor, a nervous system, a bureaucracy, or a program. Brooks distinguishes essential from accidental complexity. Tesler asks where complexity is allocated. Meyer specifies obligations through preconditions, postconditions, and invariants. These are not instances of one hidden formalism, and this paper does not claim that they are. They do, however, share a useful limitation: the arrangement that performs, checks, and answers for the work is usually held fixed while the allocation problem is analysed.

A parameter that never varies is indistinguishable from a constant. For much of software engineering, treating the determiner as fixed was productive. The operative arrangement was usually some combination of authored procedure, human developer, human operator, and mechanical execution. Contemporary systems make the omitted parameter harder to ignore because the same governing choice may now be allocated among:

- an explicit rule;
- a search or planning procedure;
- a learned policy;
- a human specialist;
- a model with tools;
- an automated checker;
- a human reviewer;
- an organization that authorizes and bears consequences;
- or a composition of several of these.

The important change is not that an ontologically unprecedented third species has appeared. Probabilistic programs, adaptive systems, learned components, organizations, and collectives predate contemporary generative models. The change is operational: heterogeneous arrangements now resolve consequential choices inside ordinary engineering systems at a scale that makes their differences load-bearing.

The missing parameter is therefore not simply **which actor species acts**. It is the whole arrangement through which a resolution is produced, constrained, checked, attributed, and sanctioned.

### 1.1 The primary claim

Let a determination problem be described relative to:

- a task \(T\);
- accessible ground \(G\);
- an acceptance relation \(P\);
- a declared tolerance \(\tau\);
- a system arrangement \(A\);
- an assurance requirement \(\alpha\).

The paper’s primary claim is:

> **The unresolved determination of a task is indexed by \(\langle T, G, P, \tau, A, \alpha\rangle\), not by \(T\) alone.**

Changing the arrangement can change:

- which distinctions are committed in advance;
- which choices remain for runtime resolution;
- which outputs can be checked directly;
- which failures can be detected;
- whose identity must be trusted;
- who can be held answerable;
- and which residual risks remain accepted or escaped.

This claim is intentionally weaker than a conservation law. The paper does not yet establish a decomposition-invariant scalar quantity of determination demand. It establishes an allocation problem: reductions in runtime discretion are ordinarily purchased through additional commitment, observation, verification, coordination, or accepted risk elsewhere.

### 1.2 Relationship to the classical accounts

The paper uses Brooks, Tesler, Ashby, and Meyer as comparative lenses, not as four formally equivalent antecedents.

- **Ashby** makes the regulator’s required variety explicit while abstracting over the constitution of the regulator.
- **Brooks** asks which complexity is intrinsic to the software problem, but the practical experience of that complexity still depends on the capabilities, representations, and checks available to the arrangement.
- **Tesler** treats complexity as allocated among roles, which anticipates the present concern but does not distinguish the constitutional or assurance properties of the mechanisms occupying those roles.
- **Meyer** gives a powerful account of mechanically checkable obligations, but the significance of a contract changes when candidate production, checking, authorization, and accountability are distributed across heterogeneous components.

The proposed extension is not that the classical accounts are wrong. It is that varying the arrangement makes some of their apparent constants behave like parameters.

---

## 2. Actors, arrangements, and ground

### 2.1 Actor definition

An **actor** is a system whose output is selected through an internal state transition that is causally sensitive to information obtained from declared ground.

Three elements are required:

1. **Alternatives.** At the declared abstraction and tolerance, more than one outcome-relevant resolution is possible.
2. **Information-bearing pathway.** Variation in declared ground can alter the resolution through an identifiable sensing, communication, representation, or state-transition pathway internal to the candidate actor.
3. **Selection.** The pathway participates in selecting among the alternatives rather than merely perturbing an external physical trajectory.

Actorhood is relative to an abstraction boundary. A market may be treated as one actor when its aggregate price-forming process is the relevant selector, or as many actors when individual bids and institutions are being analysed. An organization may likewise be one actor for an authorization decision and several actors for the workflow that produces it.

A falling rock is excluded because changes in wind or terrain alter its trajectory directly; there is no information-bearing pathway inside the rock that represents or uses those conditions to select among declared alternatives. A thermostat qualifies because sensed temperature changes an internal control state that selects fire or hold. Neither conclusion depends on intelligence.

### 2.2 Decision and ground

A **decision** is a declared, outcome-relevant alternative whose resolution is subject to governance at a chosen abstraction and assurance level.

A fact belongs to **ground** when information about that fact can change the resolution or its acceptance status beyond the declared tolerance.

These definitions deliberately avoid the claim that every physical transition is literally a decision. The framework begins where a designer, analyst, or institution declares an outcome-relevant alternative and asks how its resolution is governed.

Ground should be described by provenance:

- **controlled ground:** maintained by the arrangement and enforceable through commitments;
- **observed ground:** read from an external or independently changing system;
- **inferred ground:** estimated from data or a model;
- **institutional ground:** supplied through rules, conventions, authority, or social practice;
- **missing ground:** relevant information unavailable to the executing arrangement.

This distinction matters because a stored statement about uncontrolled ground is not equivalent to a current observation of that ground. Revalidation cadence should depend on drift rate, consequence, consistency guarantees, and the declared assurance level rather than on a universal “read every time” rule.

### 2.3 The arrangement, not the isolated actor

An actor rarely determines alone. Define the **system arrangement** as the composition of:

- producer or executor;
- prior commitments;
- available ground channels;
- tools and memory;
- verification mechanisms;
- reviewers or authorizers;
- execution record;
- accountable principal;
- remediation and sanction paths.

The same model, program, or human can behave differently across arrangements. A language model without repository access is not the same determiner as the same model with retrieval, tests, a compiler, and a human reviewer. A person acting privately is not the same accountable arrangement as the same person acting through a licensed organization with records, insurance, review, and appeal.

The unit of comparison should therefore usually be the arrangement, not an isolated biological or computational component.

---

## 3. Commitment resolution

The original draft’s “pinning resolution” becomes more defensible when it is treated as a property of commitments in an arrangement rather than as an intrinsic species taxonomy.

A behavioural commitment may attach at three levels.

### 3.1 Outcome-level commitment

The arrangement fixes permitted resolutions directly.

Examples:

- a lookup table;
- a hard-coded mapping;
- a schema constraint;
- a fixed threshold;
- an allow-list;
- an invariant that permits only one acceptable outcome for a class of cases.

Outcome-level commitment offers the strongest local predictability, but it may require extensive prior specification and may fail outside the cases represented by the commitment.

### 3.2 Policy-level commitment

The arrangement fixes a procedure, policy, distribution, objective, or parameterized mapping that produces resolutions.

Examples:

- a sorting or planning algorithm;
- a probabilistic program;
- a trained model with fixed weights and decoding configuration;
- a search procedure;
- an optimization objective;
- a human operating procedure;
- a controller.

Policy-level commitment does not require enumerating every input-output pair. It fixes how resolutions are generated, although the mapping may be difficult to interpret, predict, or verify locally.

### 3.3 Principal-level commitment

The arrangement selects a determiner or institution by qualification and delegates case-level resolution.

Examples:

- a licensed engineer;
- a court;
- a medical specialist;
- an incident commander;
- a certified supplier;
- an organizational review board.

Principal-level commitment constrains behaviour through selection, authority, professional norms, history, and sanction rather than through a complete output or policy specification.

### 3.4 Commitments compose

These levels are not mutually exclusive and are not actor species.

A deployment may:

- select a qualified human principal;
- require the principal to follow an explicit policy;
- use a model to generate candidate resolutions;
- enforce outcome-level constraints;
- and mechanically reject non-compliant results.

The analytical question is not “which of three kinds is this actor?” It is:

> At which levels has the arrangement made commitments, and what unresolved discretion remains after those commitments are applied?

### 3.5 Residual discretion

Replace “last wind” as a technical primitive with **residual discretion**:

> Residual discretion is the outcome-relevant variation remaining after the arrangement’s declared commitments are applied, relative to a task distribution, accessible ground, tolerance, and time horizon.

Residual discretion is not identical to randomness.

- A deterministic model can have zero run-to-run variance and still have substantial epistemic uncertainty across unfamiliar cases.
- A randomized program can have non-zero variance while remaining tightly specified.
- A human can have low observed variance on a rehearsed procedure.
- A zero-variance arrangement can be consistently wrong.

For assurance, residual discretion must be analysed together with bias, correlated failure, expected loss, and tail risk.

---

## 4. Resolution source and assurance mechanism

The earlier four-store model mixed two dimensions. A cleaner model separates where a resolution comes from from how its acceptability is established.

### 4.1 Source of resolution

A governing choice may be resolved by:

1. **Prior commitment**  
   An encoded rule, constraint, policy, procedure, or prior design choice.

2. **Runtime actor resolution**  
   A program, model, human, team, market, or hybrid arrangement selects among alternatives using available ground.

3. **Environmental or default resolution**  
   Library behaviour, timing, infrastructure defaults, uncontrolled dynamics, or other incidental mechanisms settle the outcome.

4. **Failure or non-resolution**  
   The arrangement does not produce a usable resolution.

### 4.2 Assurance mechanism

The resolution may be assured through:

- proof or static constraint;
- mechanical checking;
- runtime monitoring;
- independent human review;
- accountable authorization;
- statistical evaluation;
- post-deployment audit or consequence;
- or no adequate mechanism.

Checks may occur before, during, or after execution. Their defining property is not timing but whether acceptability is evaluated through a criterion sufficiently independent to detect relevant failure.

### 4.3 Escaped decision

An **escaped decision** is:

> A consequential resolution that is not intentionally governed by an adequate source-and-assurance combination at the declared assurance level, and whose unacceptable outcomes are not reliably detected.

“Escaped” does not mean “determined by nothing.” Defaults, physical behaviour, legacy code, incentives, or accidental interaction will still determine an outcome. Escape means the outcome is not deliberately governed and assured.

### 4.4 Allocation principle

The paper should state an allocation principle rather than an unproven conservation theorem:

> At a fixed task, tolerance, representation, and assurance level, reducing unresolved runtime discretion ordinarily requires additional prior commitment, observation, verification, coordination, or explicit risk acceptance elsewhere in the arrangement.

This proposition is falsifiable as an engineering tendency and does not require a representation-independent unit of “decision count.”

Decomposition can:

- expose hidden choices;
- merge equivalent choices;
- compress repeated distinctions into a general rule;
- amortize a decision across many cases;
- relocate choices into interfaces;
- or alter which distinctions matter at the selected abstraction.

The paper should therefore avoid saying that an exact total is invariant until an independently motivated measure exists.

---

## 5. Closure and evaluability

The acceptance relation is central, but “closure” must be divided into distinct questions.

Let \(P(c, G)\) denote whether candidate \(c\) is acceptable relative to declared ground \(G\).

### 5.1 Logical closure

An acceptance procedure exists and terminates for every candidate in the declared domain.

Logical closure is a property of formal decidability. It says nothing by itself about practical cost.

### 5.2 Operational closure

The acceptance procedure can be executed with the ground, time, memory, tools, permissions, and reliability available to the arrangement.

Operational closure is the relevant concept for deployed engineering systems.

### 5.3 Economic closure

Candidate generation and verification can be performed at an acceptable cost relative to the value, latency, consequence, and assurance requirement of the task.

A procedure can be logically and operationally available yet economically useless.

### 5.4 Normative closure

The acceptance relation adequately represents the values, rights, trade-offs, and stakeholders that the arrangement is meant to serve.

A mechanically executable predicate may be normatively incomplete, contested, or gameable.

### 5.5 Acceptance-region accessibility

Closure must be separated from the difficulty of producing an acceptable candidate.

Relevant variables include:

- density of acceptable outputs;
- topology or connectivity of the acceptance region;
- search-space size;
- availability of gradients or incremental feedback;
- cost of retries;
- generator capability;
- access to relevant ground;
- adversarial pressure.

A proof may be easy to check and extremely hard to discover. A cryptographic preimage may be easy to verify and infeasible to find. A predicate may accept exactly one candidate. None of these contradicts closure; they refute the inference from closure to cheap adequacy.

### 5.6 Producer independence under successful verification

The strongest defensible result is narrower:

> Given a declared acceptance relation, complete access to the ground required by it, a sound and terminating operational checker, and a candidate that passes, producer identity is not epistemically necessary for establishing the checked property.

This does **not** imply:

- that the candidate was cheap to generate;
- that the predicate captures every relevant value;
- that the checker is legitimate or correctly implemented;
- that the candidate is safe outside the declared ground;
- that accountability disappears;
- or that intelligence was unnecessary to produce the candidate.

### 5.7 Open-predicate dependence

Where no adequate acceptance procedure is available over accessible ground at the declared assurance level, acceptance cannot be fully discharged through direct mechanical verification.

The residual may depend on:

- situated judgment;
- social convention;
- institutional authority;
- delayed observation;
- trust;
- negotiation;
- or explicit risk acceptance.

This does not establish that a human individual can necessarily find a correct answer. Some tasks are under-specified, contested, unknowable, or impossible rather than merely judgment-dependent.

---

## 6. Actor-indexed irreducibility

Brooks’s essential/accidental distinction becomes more precise when indexed by arrangement.

Define the **judgment floor** as:

> The portion of outcome-relevant determination that cannot be discharged through the arrangement’s prior commitments or adequate direct verification at the declared assurance level.

The judgment floor is not a property of the task alone. It depends on:

- what the arrangement can observe;
- what it can compute;
- which commitments already exist;
- what counts as acceptable;
- what resources are available;
- what level of assurance is required;
- and which risks may be accepted.

The relational claim is therefore:

> **Irreducibility is a property of the relation among task, arrangement, ground, acceptance relation, tolerance, and assurance level.**

This explains why the same nominal task may be routine for one arrangement and judgment-heavy for another. It also explains why better tools, representations, contracts, sensors, tests, and institutions can move the boundary without making the original task “intrinsically” simpler in every sense.

---

## 7. Accountability completeness

The capacity to produce a resolution does not imply the capacity to bear its consequence.

Accountability should be modelled as a relation among executor, principal, record, authority, stakeholder, and sanctioning institution rather than as an intrinsic capacity of a model, program, or human.

An execution is **accountability-complete** when the arrangement provides:

1. **Attribution**  
   A record connecting the resolution to the relevant execution, inputs, tools, configuration, and authorizing context.

2. **Persistent principal**  
   A person or institution that remains available after execution and is recognized as responsible for the deployment or authorization.

3. **Authority or control linkage**  
   A defensible relation between the principal and the conditions under which the execution occurred.

4. **Stake**  
   Something the principal can lose or must expend when the arrangement causes unacceptable consequences.

5. **Sanction or remediation path**  
   A mechanism through which correction, compensation, restriction, appeal, or penalty can be applied.

A tamper-evident execution record may outperform unaided human recollection on provenance, but provenance is only one component. A ledger cannot supply institutional authority, legitimate liability, stake, or remediation by itself.

The design rule is:

> A runtime judgment allocation that names an executor but no accountable principal is incomplete. Where the residual consequence matters, the arrangement must also identify who authorizes, answers, and bears the remediation path.

---

## 8. Empirical hypotheses

The paper should replace binary human-versus-model predictions with graded hypotheses about arrangements.

### H1 — Operational evaluability

Holding generation difficulty and resources constant, comparative advantage should shift toward high-throughput computational generators as:

- acceptance becomes more operationally evaluable;
- feedback becomes faster and denser;
- ground becomes more accessible;
- checking becomes cheaper;
- retries become affordable.

### H2 — Ground and judgment dependence

Human or institutionally situated arrangements should retain greater comparative advantage as:

- relevant ground is unavailable to the computational system;
- consequences are delayed;
- evaluators disagree;
- acceptance criteria change over time;
- tacit or socially distributed knowledge is required;
- normative legitimacy is part of the task.

### H3 — Generator/checker composition

A model-plus-checker or model-plus-reviewer arrangement should often outperform both model-alone and human-alone baselines where:

- candidate generation benefits from breadth or speed;
- significant parts of acceptance are operationally closed;
- and the remaining open residue can be escalated.

### H4 — Accountability completeness

Trust and deployment willingness should be better predicted by the completeness of the accountability arrangement than by whether the immediate executor is human or computational.

### H5 — Selection versus training

Reliance on worker or provider selection should increase as result-level evaluation becomes slower, less objective, less stationary, and less complete, holding labor supply, training cost, consequence, and task structure constant.

Closure does not make training available or unavailable as a hard gate. Open-predicate domains still support apprenticeship, imitation, critique, socialization, delayed feedback, and proxy objectives. Closed domains may still use selection because training is costly and variance matters.

---

## 9. Proposed study design

### 9.1 Unit of analysis

Compare **system arrangements**, not only isolated actor labels.

Candidate conditions:

1. human alone;
2. model alone;
3. conventional program or solver;
4. model plus mechanical checker;
5. model plus human reviewer;
6. human plus automated checker;
7. model plus retrieval and tools;
8. human-model team with accountable authorization.

### 9.2 Independent variables

Measure separately:

- operational evaluability;
- verification cost;
- feedback latency;
- feedback density;
- ground accessibility;
- acceptance-region accessibility;
- nominal task difficulty;
- consequence severity;
- normative disagreement;
- task stationarity.

Do not use “decidability” as the empirical label unless formal decidability is actually measured. The professional-data study should use **operational evaluability**.

### 9.3 Dependent variables

Possible outcomes:

- acceptance rate;
- time to acceptable result;
- total generation-plus-checking cost;
- severe-error rate;
- calibration;
- tail loss;
- reviewer disagreement;
- remediation cost;
- trust or deployment willingness;
- accountability attribution accuracy.

### 9.4 Core preregistered model

A defensible preregistered prediction is:

> After controlling for nominal difficulty and resources, operational evaluability will explain additional variance in the comparative performance of computationally assisted arrangements relative to unaided human arrangements.

A stronger interaction hypothesis is:

> The advantage of model-plus-checker arrangements over model-alone arrangements will increase with operational evaluability and decrease with missing ground and normative disagreement.

### 9.5 Falsifiers

The theory is weakened if:

- operational evaluability adds no predictive value after task difficulty and resources are controlled;
- highly evaluable tasks systematically favor unaided situated judgment despite equivalent ground and checking access;
- accountability completeness does not affect trust, adoption, or remediation outcomes;
- commitment-locus analysis fails to identify allocation differences not already captured by ordinary workflow descriptions;
- escaped-decision analysis does not predict failure modes or design-review findings.

---

## 10. Worked example: code generation

Use one example throughout the final paper.

### Task

Generate a repository change satisfying a declared request.

### Ground

- repository contents;
- API definitions;
- language semantics;
- tests;
- dependency versions;
- architectural conventions;
- performance requirements;
- operational context.

### Commitments

- outcome-level: code must compile, preserve public interfaces, and satisfy declared invariants;
- policy-level: coding standards, generation procedure, tool configuration, and model or solver policy;
- principal-level: a maintainer or organization authorizes the merge.

### Resolution sources

- model generates a patch;
- static tooling resolves formatting and type constraints;
- tests check selected behaviour;
- a reviewer resolves architectural fit;
- deployment monitoring observes effects not captured before release.

### Closure analysis

- parsing and compilation may be operationally closed;
- test-suite compliance may be operationally closed relative to the suite;
- formal correctness may be logically closed but economically expensive;
- maintainability may be partially evaluable;
- long-horizon architectural fitness may remain open;
- organizational acceptability may be normatively contested.

### Escaped decisions

Examples include:

- an undocumented API behaviour changes because no test or reviewer covers it;
- dependency drift invalidates a cached assumption;
- generated code passes tests but violates an unstated operational constraint;
- no named principal owns the risk of deploying the change;
- model output is accepted because it appears plausible rather than because the relevant property was checked.

### Prediction

Model advantage should increase as more of the acceptance relation becomes operationally evaluable and feedback becomes immediate. Human or institutional judgment should remain load-bearing where ground is missing, values conflict, consequences are delayed, or architecture cannot be adequately represented by the checker.

---

## 11. Claim-status table

| Claim | Status | Basis | Appropriate test |
|---|---|---|---|
| Determination is indexed by \(T,G,P,\tau,A,\alpha\) | Primary conceptual claim | Definition and comparative analysis | Explanatory utility and counterexamples |
| Outcome-, policy-, and principal-level commitments | Analytical taxonomy | Construction | Boundary-case coverage and utility |
| Source and assurance are separate dimensions | Analytical distinction | System-design analysis | Case-study coding reliability |
| Escaped decisions predict ungoverned failure | Engineering hypothesis | Repository practice and examples | Design-review and incident studies |
| Operational verification reduces producer dependence for the checked property | Conditional proposition | Verification argument | Controlled comparisons |
| Closure is distinct from generation cost | Derived distinction | Counterexamples from search and verification | Task experiments |
| Operational evaluability predicts arrangement advantage | Empirical hypothesis | Proposed mechanism | Preregistered multi-condition study |
| Accountability is relational | Normative/institutional model | Responsibility analysis | Case studies and stakeholder experiments |
| Determination demand is conserved as a scalar | **Not established** | No stable measure yet | Formalization required |
| Verdict entropy measures determination demand | **Research hypothesis only** | Conditional information model | Construct-validation studies |
| Rate-distortion universally bounds actor reasoning | **Not established** | Requires restrictive source/channel assumptions | Empirical model validation |
| Closed predicates make intelligence unnecessary | **Retire** | Does not follow from verification | — |

---

## 12. Revised manuscript structure

1. **Introduction: the fixed arrangement**
   - motivate the missing parameter;
   - state the indexed tuple;
   - state contributions and claim status.

2. **Actors, arrangements, and ground**
   - actor admission test;
   - information-bearing pathway;
   - scale and composite actors;
   - ground provenance.

3. **Commitment resolution**
   - outcome-, policy-, and principal-level commitment;
   - residual discretion;
   - boundary cases.

4. **Resolution and assurance**
   - two-axis model;
   - escaped decisions;
   - allocation principle;
   - seams and decomposition.

5. **Closure and evaluability**
   - logical, operational, economic, normative;
   - accessibility and generation cost;
   - producer-independence proposition.

6. **Actor-indexed irreducibility**
   - judgment floor;
   - reinterpretation of Brooks;
   - relation to Ashby, Tesler, and Meyer.

7. **Accountability completeness**
   - executor versus principal;
   - records, authority, stake, sanction, remediation.

8. **Worked example**
   - code generation carried through all constructs.

9. **Predictions and study design**
   - graded hypotheses;
   - conditions and baselines;
   - preregistration and falsifiers.

10. **Limits and boundary cases**
    - randomized and adaptive programs;
    - learned symbolic systems;
    - hybrid arrangements;
    - distributed actors;
    - incomplete and gameable predicates;
    - expensive decidable checks;
    - contested normative ground.

11. **Related work**
    - mixed-initiative systems;
    - human-in-the-loop and sociotechnical systems;
    - formal verification and proof-carrying systems;
    - bounded rationality and principal-agent theory;
    - algorithmic accountability and responsibility gaps;
    - cybernetics and requisite variety;
    - tacit knowledge and expertise;
    - probabilistic programming and adaptive control.

12. **Conclusion**
    - restate the indexed relation;
    - distinguish what is established from what is projected;
    - position Decision-Driven Design as the engineering corpus from which the research program was abstracted.

---

## 13. Replacement conclusion

Complexity does not arrive at an engineering arrangement already labelled essential or accidental. A consequential choice becomes easy, hard, checkable, delegable, or judgment-heavy only relative to what the arrangement can observe, what commitments it already contains, what acceptance relation it must satisfy, and what assurance is required.

That is the missing parameter. It is not a new species name for the determiner. It is the arrangement through which determination is produced and governed.

Once the arrangement is made explicit, several distinctions sharpen. A commitment may attach to an outcome, a policy, or a principal. A resolution source is not the same thing as its assurance mechanism. A checker can remove the need to trust a producer for a declared property without making the candidate cheap to generate or the property normatively complete. An executor can produce a resolution without being able to answer for its consequence. And a choice can escape: the system produces an outcome even though no adequate commitment, check, or accountable authorization governs it.

The strongest result is therefore relational:

> Irreducibility is not a property of a task alone. It is a property of the relation among task, arrangement, accessible ground, acceptance relation, tolerance, and assurance level.

The empirical question is not whether models replace humans wherever a predicate closes. It is how comparative advantage shifts as operational evaluability, generation cost, ground access, feedback, and accountability change. That question admits mixed arrangements, graded predictions, and falsification. It also matches engineering practice, where the practical winner is rarely an isolated actor and usually a composition of commitments, generators, checks, reviewers, and principals.

Decision-Driven Design supplies the engineering corpus from which this research program was abstracted. Its value is not that it already proves a universal conservation law or an exact human–model boundary. Its value is that it makes consequential choices auditable: where they are resolved, what they are resolved against, how they are checked, who answers for them, and which ones have been left to accident.

---

## 14. Immediate editing instructions for `paper-a-draft.md`

### Replace completely

- Abstract.
- §1.1’s historical “third actor appeared” argument.
- §2.2’s program/model/human table.
- §2.3 “last wind” as an actor-species construct.
- Exact conservation language in §3.2.
- Accountability as an intrinsic actor capacity.
- “Closed predicate makes adequacy cheap.”
- “Closed predicate makes intelligence unnecessary.”
- Exact “models win where closed, humans win where open” prediction.

### Preserve and adapt

- “A parameter that never varies is indistinguishable from a constant.”
- Actorhood need not imply intelligence.
- The thermostat example, after adding the information-pathway condition.
- Escaped decisions.
- Seam ownership and prepayment/amortization intuition.
- “Where you cannot check the work, you check the worker,” reframed as a tendency rather than a law.
- Executor/accountable-principal separation.
- “Irreducibility is not a property of the problem,” expanded to the full indexed tuple.
- The strong rhetorical voice, while reserving exact language for conditional propositions.

### Add before submission

- The missing later sections promised by the abstract.
- One sustained worked example.
- A claim-status table.
- A full related-work section.
- A references section.
- Explicit falsifiers and preregistered hypotheses.
- A limitations section covering hybrid and boundary-case systems.
