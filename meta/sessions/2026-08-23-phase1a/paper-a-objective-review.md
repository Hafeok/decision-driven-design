# Objective Review: *The Missing Parameter — Actor-Indexed Determination*

**Manuscript:** [`papers/paper-a/paper-a.md`](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md)  
**Reviewed state:** `decision-driven-design` `main` at commit [`40d277f`](https://github.com/Hafeok/decision-driven-design/commit/40d277f53e93f87818ece4236c2fef9a45fa71be), merged 20 August 2026  
**Companion material checked:** the measure note at commit [`aa7e135`](https://github.com/Hafeok/decision-driven-design/blob/aa7e1352bc6484c7bb5f467bd5b66a849692cbc9/papers/measure-note/measure-note.md), the cited `actor-indexed-determination` graph at `v5.8.0`, and Paper A's reproduction scripts  
**Review recommendation:** **Major revision / reject and invite resubmission**

---

## Executive assessment

This manuscript is substantially stronger than the earlier draft. It now has a coherent central object—the **arrangement**—and it develops several useful distinctions around that object: resolution versus assurance, outcome versus verdict, filing versus delivery, and executor versus principal.

As an internal statement of the Decision-Driven Design framework, it is strong. As an archival academic paper, it is not yet publication-ready. The principal obstacle is not the absence of empirical evidence; the manuscript discloses that absence clearly. The obstacle is that one formal claim is directly contradicted by the companion measure note, the proposed discharge partition is not mutually exclusive under the paper's own examples, and the claimed scholarly novelty has not been established against the relevant literature.

The manuscript contains a real and potentially valuable paper. Its strongest contribution is not the entropy identity and not a new taxonomy of actors. It is the proposition that consequential resolution should be analysed at the level of a sociotechnical arrangement, with resolution source, delivery, assurance, and accountable principal represented separately.

## Scorecard

| Dimension | Assessment |
|---|---|
| Core idea | Strong and practically useful |
| Originality | Plausibly original synthesis; novelty not yet demonstrated |
| Conceptual consistency | Several load-bearing conflicts remain |
| Formal correctness | Critical boundary error in the entropy section |
| Empirical support | None, correctly disclosed |
| Internal traceability | Excellent |
| Related work | Far below publication standard |
| Writing | Strong sentence-level prose, but overlong and over-defensive |
| Overall recommendation | Major revision / reject-and-resubmit |

---

## 1. What the current revision genuinely fixes

Several criticisms applicable to the earlier draft are no longer fair.

### 1.1 The arrangement is now the correct unit of analysis

The manuscript no longer presents a crude human–program–model taxonomy. It correctly observes that a model with retrieval, tools, tests, review, records, and escalation is a different determiner from the same model in isolation. The corresponding move from isolated actor to arrangement is conceptually sound and practically important.

### 1.2 Resolution and assurance are separated

This is one of the strongest improvements. A mechanism that produces a resolution is not necessarily the mechanism that establishes its acceptability. The distinction gives the framework a useful way to analyse generator–checker systems, human review, monitoring, audit, and accountable authorisation without collapsing them into one store.

### 1.3 Closure has been disaggregated

Logical, operational, economic, and normative closure are now explicitly distinguished. This removes a major ambiguity in the earlier argument and prevents formal decidability from being mistaken for practical usability or normative adequacy.

### 1.4 The predictions are graded and arrangement-relative

The five hypotheses no longer propose a binary human/model frontier. They permit hybrid systems and predict shifts in comparative advantage as evaluability, feedback, ground accessibility, cost, and accountability change. That is a much more credible empirical posture.

### 1.5 Accountability has been narrowed structurally

Accountability is now treated as a relation within an arrangement rather than an intrinsic capacity of an executor. Separating executor and principal is useful, especially for systems in which the immediate producer of a resolution cannot itself answer, bear consequences, authorise action, or provide remediation.

### 1.6 Filing versus delivery is a strong engineering contribution

The observation that a correct, filed decision can still escape because it was not delivered at the act is sharp and practically valuable. “Escape that presents as governance” describes a real class of repository, retrieval, review, and operational failures.

### 1.7 The status and reproduction apparatus is unusually disciplined

The paper exposes projected status, empty evidence fields, retired claims, and pinned source versions rather than hiding them. The [quotation checker](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/check-quotations.py) and [appendix checker](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/check-appendix.py) genuinely verify correspondence with the pinned graph. They do not establish the truth of the claims, but they provide excellent internal traceability.

---

## 2. Critical finding: the closure–measure biconditional is false

Paper A says that the measure exists **if and only if** the acceptance predicate operationally closes, and that `H(V)` is undefined otherwise. It then says that at the verification-closed rung, “the measure exists.” See [§4.4](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md#L500-L535) and [§5.2](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md#L600-L615).

The pinned companion note explicitly distinguishes conditions that make this biconditional fail in both directions.

### 2.1 Closure is not sufficient for an output-valued verdict variable

A relation task can have a completely decidable acceptance predicate while allowing several acceptable outputs. In that case, no unique output-valued `V` exists until the task supplies a tie-breaker, a canonical form, or a declared selection distribution.

The measure note states this directly in its [task-class analysis](https://github.com/Hafeok/decision-driven-design/blob/aa7e1352bc6484c7bb5f467bd5b66a849692cbc9/papers/measure-note/measure-note.md#L183-L210). It also warns that the binary entropy of a verification result is not the entropy of the generation task.

Therefore, verification closure is not sufficient for the verdict variable used by Paper A.

### 2.2 Operational closure is not necessary for mathematical existence

A unique verdict function can exist mathematically while being computationally unavailable to a particular arrangement. The companion note explicitly says that `H(V)` can exist mathematically even when the procedure cannot run within available ground, resource, latency, or confidence bounds. See its [scope conditions](https://github.com/Hafeok/decision-driven-design/blob/aa7e1352bc6484c7bb5f467bd5b66a849692cbc9/papers/measure-note/measure-note.md#L712-L733).

Operational closure therefore governs availability to an arrangement, not mathematical existence.

### 2.3 Closure is not sufficient for estimation

Even when a verdict function exists and is operationally usable, `H(V)` also depends on the ground distribution. If that distribution is unknown, unstable, or only partly observable, the entropy may be well-defined but not estimable.

### 2.4 Consequence for the graph

[`DDD-measure-06`](https://github.com/Hafeok/actor-indexed-determination/blob/v5.8.0/core/claims/DDD-measure-06.yaml) should not retain `established` status in its present form. Its own counterexample—an open predicate with a defensible verdict function—is effectively supplied by the companion note.

The chain-rule identity remains correct. The problem is the domain and the engineering interpretation placed around it.

### 2.5 Required repair

The paper should distinguish at least four conditions:

1. **Semantic determinacy:** Does the task supply a unique target, tie-breaker, or declared selection distribution?
2. **Verification closure:** Can a candidate be evaluated for acceptability?
3. **Constructive closure:** Can a target candidate be produced by rule?
4. **Estimability:** Is the deployment distribution known well enough to estimate the quantity?

Only semantic determinacy plus a specified distribution makes the output-valued `H(V)` mathematically defined. Operational closure governs usability, not existence.

---

## 3. Critical finding: raw ground collapses the allocation measure

The admissibility rule allows `X` to be computed from ground available at the act. But the paper defines the verdict as an assignment induced by the ground, so for deterministic tasks:

\[
V=f(G).
\]

Choose `X = G`. Then:

\[
H(V\mid G)=0, \qquad I(V;G)=H(V).
\]

Raw input ground therefore appears to carry the entire verdict and leave no residual demand—even if the arrangement has no rule for turning that ground into the correct answer.

The date pair `(month, day)` does not itself encode the validity rule. Nevertheless, observational mutual information treats it as carrying the full verdict because an ideal observer knows the joint distribution.

The current admissibility condition in [`DDD-measure-15`](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md#L1358) does not prevent this collapse.

This exposes the central construct-validity problem:

- `I(V;X)` establishes statistical dependence.
- It does not establish that an arrangement possesses a usable representation, decoder, or decision rule.
- It therefore cannot yet be interpreted as “encoded demand” or “pre-paid work.”

The engineering quantity must be actor-, decoder-, or mechanism-relative, or it must employ a concept of usable/value-bearing information rather than ordinary mutual information. Until that is repaired, Paper A should present verdict entropy as a candidate quantitative extension, not as an established measured region of the framework.

---

## 4. Critical finding: the four discharge modes do not form a partition

The paper classifies resolutions as:

1. filed decision;
2. judgment;
3. arrangement default;
4. uncontrolled draw.

Under the paper's own definitions, these classes overlap.

### 4.1 Declared defaults overlap filed decisions

A filed decision is authored in advance and delivered at the act. The paper also says a default can be declared and governed. A declared default is therefore both a filed decision and an arrangement default.

### 4.2 Deterministic rules overlap judgment

Judgment is defined as variation produced at the act by an actor reading ground. A thermostat, lookup table, or deterministic controller can be a framework actor and read ground at the act, even though its response is already fixed by a standing rule.

### 4.3 Trained inference receives incompatible classifications

Training is called policy-level commitment in [§3.3](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md#L329-L340). Judgment is produced at the act by an actor reading ground in [§4.1](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md#L360-L375). A learned deterministic rule is then said to move demand from occasioned to standing supply in [§10.3](https://github.com/Hafeok/decision-driven-design/blob/40d277f53e93f87818ece4236c2fef9a45fa71be/papers/paper-a/paper-a.md#L1083-L1088), while `DDD-cost-20` says training converts judgment allocation into encoded allocation inside the carrier.

The trained model is consequently policy, standing encoding, and act-level judgment at once.

### 4.4 Why this is load-bearing

The categories mix several different dimensions:

- causal producer;
- provenance;
- time of resolution;
- governance status;
- control;
- and delivery.

This breaks the proposed exhaustiveness and coding-reliability claim. The framework should replace the four modes with orthogonal axes, or supply an explicit priority rule that assigns each case exactly once and survives trained inference, lookup tables, declared defaults, randomised search with checking, abstention, and timeout.

The two-register distinction is insightful, but it does not fully repair the canonical phrase “determined never, by nobody” while the paper also says the escaped choice is determined by a default or draw. “Ungoverned resolution” would be clearer than “determined never.”

---

## 5. Major finding: residual discretion conflates different phenomena

Residual discretion is said not to be randomness, and a deterministic arrangement is said to retain substantial discretion over unfamiliar cases. But if a declared deterministic policy and ground uniquely fix the output, there is no remaining act-level choice conditional on them.

What remains may instead be:

- variation across inputs;
- designer ignorance about consequences;
- inability to predict a fixed policy;
- unspecified acceptance criteria;
- delegated choice;
- or stochastic variation.

These are not interchangeable. A cryptographic hash varies enormously across inputs but exercises no discretion. Conflating these categories also drives the trained-model contradiction.

The framework needs separate terms for:

1. outcome variation across ground;
2. epistemic uncertainty about a fixed policy;
3. stochasticity;
4. genuine unresolved or delegated selection.

---

## 6. Major finding: the actor admission test remains partly circular

The revised admission test is better than the earlier draft because it requires alternatives, an information-bearing internal pathway, and selection. However, it distinguishes selection from “mere perturbation” by asserting that one is selection.

A sufficiently complex physical mechanism—a fracture threshold, mechanical governor, or chemical regulator—can satisfy the causal-pathway test. Whether it counts as an actor depends on a functional or governance interpretation that has not yet been stated independently.

The categorical claim that the rock fails is therefore not yet produced by an operational test. It is produced by the intended meaning of “selection.”

There is a related ground problem. The tuple uses **accessible ground**, while §2.4 includes relevant-but-unavailable facts as **missing ground**. These should be represented separately:

\[
G^*=\text{relevant world facts}, \qquad G_A=\text{ground accessible and delivered to arrangement }A.
\]

That separation would materially strengthen the ground-access and floor hypotheses.

---

## 7. Major finding: graph status is being used as epistemic status

The paper's transparency is good, but its status vocabulary still creates epistemic ambiguity.

- `settled` and `established` mean internally argued and unchallenged, not externally established;
- `reported` means exercised by a computation, not empirically supported;
- `analysis` is said to carry no status because it is not a claim, even though the analysis sections contain contestable propositions about institutions, accountability, Goodhart effects, and provenance.

Calling something analysis does not make it non-claiming. A more accurate label would be **authorial synthesis—not represented in the graph**.

The paper also combines several kinds of propositions under the single `projected` status:

- definitions, assessed for coherence and coding reliability;
- formal claims, assessed by proof or counterexample;
- empirical hypotheses, assessed by prediction;
- normative prescriptions, assessed by argument and stakeholder commitments.

These require different forms of warrant. A single maturity status cannot substitute for an epistemic classification.

The primary claim's current falsifier is also weak. A case whose floor does not move across arrangements does not refute the general claim that arrangement variables matter in other cases. The empirical test must compare the predictive performance of an arrangement-indexed model against a task-only alternative on held-out cases.

---

## 8. Major finding: novelty is not established by the related-work section

The manuscript contains only ten references while positioning itself across cybernetics, software complexity, mixed-initiative systems, formal verification, principal–agent theory, distributed work, and algorithmic accountability. Most named neighbourhoods contain no direct citations.

More importantly, the arrangement as a unit of analysis is already central to distributed cognition and joint cognitive systems: [Hutchins](https://pages.ucsd.edu/~ehutchins/citw.html), [Woods and Hollnagel](https://www.taylorfrancis.com/books/mono/10.1201/9781420005684/joint-cognitive-systems-david-woods-erik-hollnagel). Sociotechnical safety theory already analyses failure through system-level constraints and organisational structures: [Leveson's STAMP](https://direct.mit.edu/books/oa-monograph/2908/chapter/78968/STAMP-An-Accident-Model-Based-On-Systems-Theory). Mixed-initiative allocation also has a substantial lineage: [Horvitz](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/).

The accountability section needs direct comparison with existing structural accounts such as [Bovens's accountability framework](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0386.2007.00378.x), [Matthias's responsibility gap](https://link.springer.com/article/10.1007/s10676-004-3422-1), and the tracking/tracing account of [meaningful human control](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00015/full).

This does not make Paper A unoriginal. It changes the defensible novelty claim:

> The contribution is a specific, auditable synthesis of resolution, assurance, delivery, and accountability—not the discovery that sociotechnical arrangements matter.

Accordingly, “The Missing Parameter” is too universal. “A missing parameter in selected complexity-allocation accounts” would be more defensible.

---

## 9. Hypotheses and study design

The predictions are much better framed than before, but they are not yet study-ready.

- H1 bundles evaluability, feedback speed, feedback density, ground access, checker cost, and retry cost.
- H2 bundles several distinct mechanisms, including delayed consequences, disagreement, drift, tacit knowledge, and legitimacy.
- Difficulty and resources are invoked as controls without operational definitions.
- Escaped-decision counts found by a review using the framework risk criterion circularity.
- H4's deployment-willingness outcome has major regulatory, reputational, recourse, and risk confounders.
- Failure of the umbrella prediction would not by itself falsify the conceptual ontology.

Each hypothesis should be treated as a research program containing smaller preregistered studies. The first empirical requirement is not a comparative-performance experiment. It is demonstrating inter-rater reliability and predictive validity for the framework's coding scheme.

---

## 10. Additional internal inconsistencies

### 10.1 The closure ladder violates the paper's own orthogonality claim

Section 5.1 says logical, operational, economic, and normative closure are independent. Section 5.2 then places formal decidability on a ladder of operational strength. Formal decidability is not a stronger operational rung: a formally decidable procedure can be operationally infeasible, while constructive availability is arrangement-relative. Decidability belongs on the logical axis, not at the end of the operational ladder.

### 10.2 Accountability has competing element counts

The projected accountability claim uses attribution, persistent principal, authority linkage, stake, and sanction path. The canonical accountability term in Appendix A uses attribution, persistent answerable party, and borne consequence. These may be reconcilable, but the manuscript does not supply the mapping or explain whether the five-element version refines or replaces the three-element one.

### 10.3 The worked example does not consistently apply its provenance taxonomy

The repository conventions are treated as controlled while the current schema is treated as observed from a store. If the arrangement maintains both, the categories overlap. The business/residence status is called inferred without explaining why it could not be declared or observed. The two claimed escapes may also be discoverable through code search, tests, telemetry, or stakeholder inquiry rather than genuinely missing.

The example remains useful, but the classifications should be presented as hypotheses to be investigated rather than facts supplied by the scenario.

---

## 11. Presentation and structure

The prose is often excellent. “Filing is not delivering” and “escape that presents as governance” are memorable and useful formulations. The manuscript is nevertheless too repository-native for an external scholarly audience.

The reviewed Markdown contains approximately:

- 11,600 words before Appendix A;
- 14,900 words in total;
- 63 body headings.

Too much space is spent explaining filing history, pending nodes, canon status, and what the paper does not mint. The generated graph appendix and most projection mechanics should move to supplementary material. The main paper should focus on the argument, counterexamples, external positioning, and empirical implications.

The abstract and conclusion should also avoid calling projected propositions “results” or the “strongest result.” The status labels are present, but the surrounding rhetoric still communicates greater warrant than the graph provides.

---

## 12. Recommended revision sequence

The order matters because several prose changes depend on corrections to the framework graph.

1. **Correct the graph first.** Retire or rewrite `DDD-measure-06`; distinguish existence, closure, construction, and estimability.
2. **Resolve the raw-ground collapse.** Do not interpret ordinary mutual information as usable encoded determination.
3. **Replace or formalise the four discharge modes.** Reconcile deterministic rules, defaults, and trained inference.
4. **Separate discretion, input-conditioned variation, epistemic uncertainty, and stochasticity.**
5. **Split relevant ground from accessible and delivered ground.** Finish the actor admission criterion without relying on an undefined notion of selection.
6. **Recast graph status as internal governance metadata rather than external epistemic standing.**
7. **Rewrite related work around direct comparison tables.** Show which concepts are inherited and what the paper genuinely adds.
8. **Move entropy to a bounded candidate quantitative extension unless the measure note is repaired first.**
9. **Reduce the main paper and move the generated graph material to a supplement.**
10. **Only then operationalise H1–H5 as separate empirical studies.**

---

## 13. Publication judgment by intended use

| Intended use | Judgment |
|---|---|
| Canonical repository statement | Strong, with targeted corrections |
| Workshop or position paper | Promising after major revision |
| Archival conceptual/theory paper | Reject and invite resubmission |
| Empirical contribution | Not yet; correctly presented as future work |

The reject-and-resubmit recommendation is not a rejection of the framework. It reflects the fact that repairing the measure boundary and discharge partition will change load-bearing claims rather than merely improve exposition.

## Final assessment

There is a serious paper inside the current manuscript. Its durable core is:

> Consequential resolution should be analysed at the level of an arrangement, with resolution source, delivery, assurance, and accountable principal represented separately.

That proposition is useful, defensible, and capable of supporting empirical work.

The manuscript currently overreaches when it presents the measure boundary as established, the four discharge modes as a partition, and the arrangement parameter as broadly absent from prior work. Correct those three points, narrow the novelty claim, and move the graph machinery out of the argumentative path. The resulting paper could become a strong framework or position paper without losing what makes the project distinctive.
