# Terminology Proposal: Retire “Ground”

**Context:** Decision-Driven Design, Paper A  
**Status:** Recommended terminology revision  
**Purpose:** Replace the overloaded term *ground* with a vocabulary that distinguishes the state of a case from the information available to a decision arrangement.

## Executive recommendation

Retire **ground** as a standalone technical primitive.

The term currently covers several different things: relevant facts in the world, representations of those facts, information available to an arrangement, information actually delivered during a decision act, institutional rules, and sometimes the distribution of cases. Those are not interchangeable. Treating them as one object obscures important failure modes and makes several claims harder to state precisely.

Use the following terms instead:

- **Relevant state** or **relevant conditions** for the features of the case that can affect which resolutions are acceptable.
- **Decision basis** for the observations, records, claims, and representations an arrangement can use.
- **Act basis** or **delivered basis** for the information actually present and usable during a particular decision act.
- **Basis gap** for a relevant condition that is not adequately represented in the act basis.
- **Corrupted basis** for information that is present but false, stale, misleading, or otherwise unreliable.
- **Basis provenance** for how a basis item was produced or introduced.
- **Deployment distribution** or **case distribution** for the population of situations over which performance is evaluated.

The recommended canonical term is **decision basis**, shortened to **basis** after its first definition. This preserves the framework’s existing language—such as `basedOn`, basis pins, and basis loss—while giving it a clearer conceptual role.

## Why “ground” is not doing enough work

“Ground” is evocative, but its breadth is a liability in a formal framework. In ordinary use it can mean evidence, justification, circumstances, background conditions, reasons, or the subject matter itself. The paper inherits this ambiguity.

At least four distinct objects can currently appear under the label:

1. **Conditions in the case:** what is actually true or normatively relevant.
2. **Representations available to the arrangement:** records, observations, reports, measurements, or inferred features.
3. **Representations delivered at the act:** the subset that reaches the actor or mechanism at the moment of resolution.
4. **Rules and commitments:** institutional policies, acceptance standards, or constraints that determine how a case should be judged.

The fourth category is especially important. A rule that determines acceptability is not merely another piece of case information. It often belongs in the **acceptance relation** or among the arrangement’s **standing commitments**. Calling both the rule and the case record “ground” collapses the criterion of judgment into the material judged.

The ambiguity creates practical problems:

- A missing fact and a missing record of that fact become hard to distinguish.
- The framework cannot cleanly separate an unknown condition from a false representation.
- A delivery failure can look like an absence in the world rather than an absence at the interface.
- Evaluation over a population of cases can be confused with the information supplied in one case.
- Institutional standards can be mistaken for evidence rather than part of the definition of acceptability.

The problem therefore cannot be solved by replacing every occurrence of *ground* with one new word. The concept should be split.

## Proposed ontology

### 1. Relevant state

The **relevant state** is the collection of case conditions whose variation can change the acceptable resolution beyond the declared tolerance.

> A relevant condition is a feature of the case whose counterfactual variation can change the acceptable resolution beyond declared tolerance.

This is the world-facing side of the distinction. It may include physical circumstances, prior events, legal status, preferences, resource constraints, or other conditions, depending on the decision domain.

The relevant state need not be fully observable. It describes what matters, not what the arrangement knows.

### 2. Decision basis

The **decision basis** is the set of observations, claims, records, and representations available to an arrangement for resolving or evaluating a decision.

> The decision basis may be incomplete, stale, false, inferred, or internally inconsistent. Availability does not imply truth.

This is the representation-facing side of the distinction. A medical test result, a filed form, a sensor reading, a witness statement, a database record, and a model-generated feature can all be basis items.

**Knowledge** should not be used as a synonym. Knowledge conventionally implies truth or warrant, while a decision arrangement can act on information that is wrong.

### 3. Act basis

The **act basis**—also called the **delivered basis**—is the portion of the decision basis actually delivered and usable during a particular decision act.

This makes delivery an explicit part of the framework. A record can exist in the arrangement without appearing in the interface, arriving on time, being legible, or being available to the component that resolves the case.

The distinction supports precise statements such as:

- “The supporting record existed, but it was absent from the act basis.”
- “The arrangement had the information, but the delivery channel failed.”
- “The actor resolved the case from an incomplete basis.”

Use **act basis** when emphasizing the act-indexed object. Use **delivered basis** when emphasizing the delivery mechanism. The framework should choose one as canonical and retain the other as an explanatory alias; **act basis** is the slightly cleaner primitive.

### 4. Basis gap

A **basis gap** exists when a relevant condition lacks an adequate representation in the act basis.

This term connects the world-facing and representation-facing objects without conflating them. It also permits different kinds of gaps:

- **Absence:** no representation is present.
- **Insufficient resolution:** a representation exists but is too coarse for the decision.
- **Staleness:** the representation no longer tracks the current condition.
- **Inaccessibility:** the representation exists but is not usable at the act.
- **Uncertainty:** the available representation does not resolve the relevant variation.

A basis gap may create a judgment floor: no improvement in the resolution mechanism can recover a distinction that the act basis does not adequately represent.

### 5. Corrupted basis

A **corrupted basis** contains information that is present but materially false, stale, distorted, adversarially manipulated, or attached to the wrong case.

This is distinct from a basis gap. Missing information and misleading information can have different causes, detection methods, and remedies. The framework should preserve that distinction.

### 6. Basis provenance

**Basis provenance** records how a basis item was produced, transformed, or introduced. Possible categories include observed, reported, inferred, retrieved, generated, and institutionally supplied.

Existing categories such as *controlled*, *observed*, *inferred*, and *institutional* should be reviewed before being made exclusive. For example, a controlled variable may also be observed, and an institutional record may contain an inference. Provenance may work better as several independent attributes than as a single enumeration.

### 7. Acceptance standards and standing commitments

Institutional rules should be classified by function:

- A rule that determines which resolutions are acceptable belongs in the **acceptance relation** or **acceptance standard**.
- A policy that constrains how an arrangement acts belongs among its **standing commitments** or constraints.
- A record communicating a rule to a particular actor may appear in the **decision basis**, but the record is not identical to the rule’s normative role.

This prevents “institutional ground” from becoming a catch-all category.

## Formal model

Let:

- \(T\) be the decision target,
- \(S\) be the relevant case state,
- \(P(c,S)\) state whether candidate resolution \(c\) is acceptable in state \(S\),
- \(\tau\) be the declared tolerance,
- \(A\) be the decision arrangement,
- \(a\) be a decision act, and
- \(\alpha\) be the resulting resolution.

The arrangement delivers an act basis through a delivery or representation function:

\[
B_{A,a}=\delta_{A,a}(S)
\]

The arrangement then resolves from that basis:

\[
\alpha=A(B_{A,a})
\]

The primary decision index can therefore remain compact:

\[
\langle T,S,P,\tau,A,\alpha\rangle
\]

with \(B_{A,a}\) treated as an act-indexed object derived through the arrangement. If basis properties must be first-class in a particular analysis, the expanded form is:

\[
\langle T,S,B_{A,a},P,\tau,A,\alpha\rangle
\]

The compact form is preferable as the core model because the delivered basis depends on both the arrangement and the act. Treating one fixed \(B\) as an independent case property would hide that dependency.

The conceptual division is:

- The **relevant state** helps determine what is acceptable.
- The **arrangement** determines what representation is delivered.
- The **act basis** is what the resolver can actually use.
- The **acceptance relation** evaluates the resulting candidate against the relevant state.

## Recommended language migration

The migration should be semantic, not a global search-and-replace.

| Current expression | Recommended replacement | Use when |
|---|---|---|
| ground | relevant state / decision basis / acceptance standard | Classify by the role played in the sentence |
| accessible ground | available decision basis | Information is accessible somewhere in the arrangement |
| ground at the act | act basis | Information is delivered and usable during one act |
| declared ground | declared relevant conditions | The declaration identifies what conditions matter |
| declared ground | declared basis | The declaration identifies what information may be used |
| missing ground | basis gap | A relevant condition is inadequately represented |
| poisoned ground | corrupted basis | Present information is false, stale, or manipulated |
| ground provenance | basis provenance | Describing the production history of information |
| ground channel | basis-delivery channel | Describing how representations reach the act |
| ground coverage | basis coverage | Measuring representation of relevant conditions |
| institutional ground | acceptance standard / standing commitment / institutional basis | Classify the institution’s rule, constraint, or record by function |
| ground distribution | deployment distribution / case distribution | Describing the population over which the arrangement operates |
| ground accessibility | basis availability | Describing whether information can be reached or used |

## Preferred usage examples

- “The acceptance relation is evaluated against the relevant case state.”
- “The actor resolves from the act basis.”
- “A supporting record existed, but it was not delivered in the act basis.”
- “The missing representation created a basis gap.”
- “The basis was corrupted by a stale identity record.”
- “Performance is evaluated over the deployment distribution.”
- “The policy is part of the acceptance standard, while the filed policy notice is a basis item.”

These sentences remain understandable outside the paper while preserving a precise technical distinction inside it.

## Why “decision basis” is the strongest replacement

**Decision basis** is the best name for the representational object because it:

- aligns naturally with the existing `basedOn` relation;
- accommodates observations, testimony, records, measurements, and inferences;
- does not imply that the information is true;
- works for human, automated, and hybrid arrangements;
- supports compounds such as basis gap, basis provenance, basis delivery, and basis loss; and
- is readable in both formal and institutional prose.

The word *basis* has a mathematical meaning, but the compound *decision basis* is sufficiently specific. Define the full term once, then use *basis* where the context is unambiguous.

## Alternatives considered

| Candidate | Assessment |
|---|---|
| context | Too broad and at least as overloaded as *ground* |
| evidence | Too closely associated with proof, warrant, and assurance; not every input is evidence |
| input | Too computational and does not distinguish what is available from what is delivered |
| knowledge | Incorrectly implies truth or epistemic warrant |
| world state | Useful for actual conditions, but too narrow for records, rules, and representations |
| information state | Technically plausible, but less natural in institutional prose and can blur availability with delivery |
| substrate | Distinctive but opaque and unnecessarily metaphorical |
| grounds | Retains the original ambiguity between reasons, evidence, and circumstances |

No single candidate should replace every sense of *ground*. The ontology split is more important than the individual label.

## Effect on the information-theoretic account

The terminology change clarifies the objects in the model, but it does not by itself solve the paper’s information-theoretic problem.

If the delivered basis contains the full relevant state, \(B=S\), ordinary mutual information can make the conditional uncertainty of a value appear to vanish:

\[
H(V\mid B)=0
\]

That result does not establish that the arrangement has a usable decoder, interpretation rule, or mechanism for recovering \(V\). Renaming *ground* as *basis* exposes the distinction more clearly, but the measure still needs to be mechanism- or decoder-relative if it is intended to represent usable decision information.

Likewise, the population over which the measure is evaluated should be named separately as the **deployment distribution** or **case distribution**. It is not part of an individual act’s basis.

## Implementation plan

1. **Audit every occurrence of “ground.”** Classify each use as relevant state, decision basis, act basis, acceptance standard, standing commitment, or deployment distribution.
2. **Add canonical definitions.** Define relevant condition, decision basis, act basis, basis gap, corrupted basis, and basis provenance in the terminology section.
3. **Revise the formal primitives.** Use \(S\) for relevant state and \(B_{A,a}\) for the act-indexed basis delivered by arrangement \(A\).
4. **Update the graph vocabulary.** Preserve `basedOn`; align basis pins, basis loss, provenance, and delivery relations with the new definitions.
5. **Separate rules from records.** Move normative rules into the acceptance relation or standing commitments; keep their representations in the basis where appropriate.
6. **Revise measurement language independently.** Replace *ground distribution* with deployment or case distribution, and address the decoder-relative issue directly.
7. **Add a terminology check.** Treat an unqualified use of *ground* as a drafting warning, except in quotations or historical notes.

## Final recommendation

Adopt **relevant state**, **decision basis**, and **act basis** as three distinct concepts, with **basis gap** and **corrupted basis** naming their principal failure modes. Reserve institutional rules for the acceptance relation or standing commitments, and use **deployment distribution** for the population over which performance is measured.

This is more than a naming improvement. It gives Decision-Driven Design a clearer ontology:

- the world contains conditions that matter;
- the arrangement represents only some of them;
- the act receives only some of those representations; and
- acceptability is judged against the relevant conditions, not against whatever happened to be delivered.

That distinction is foundational enough to justify retiring *ground* as a primitive rather than searching for a single synonym.
