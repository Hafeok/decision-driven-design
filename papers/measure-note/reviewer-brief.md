# Reviewer brief — *Specification Demand Is Verdict Entropy*

*Prepared for information-theorist outreach. Two pages. The full note is ~4,700 words;
this brief states what it claims, what it does not, and the specific certification being
asked for.*

---

## The result

Software engineering has an informal conservation principle: the demand a task places on
determination — every governing decision that must be made for an acceptable output — is fixed
by the task, and design choices relocate that demand rather than remove it. The principle
lacked a unit, and attempts to count decisions failed: counts are representation-dependent,
and decomposition *creates* decisions (the interface), so the counted quantity grows under
exactly the operations it should be invariant to.

The note supplies the measure, on a bounded region. For a task whose acceptance predicate
closes — the accept/reject procedure can actually be executed over the ground the task faces,
within declared resource bounds — let `V` be the verdict, the correct output the predicate
assigns over the input distribution `P`. The identification:

> **Specification demand is `H(V)`, in bits.** Conditioning on any variable `X` splits it, by
> the chain rule and exactly: `H(V) = I(V;X) + H(V|X)` — what `X` encoded, and what remains.

Three claims the framework had stated separately are this identity under three choices of `X`:
a decomposition (the interface's "seam demand" is `I(V;S)`), an actor's encoding (what a
component can pre-compute versus what is left to its judgment), and a retrieval policy (the
encode/verify structure of retrieval-augmented generation). Two further worked instances
iterate the conditioning (a two-level decomposition, with internal seams as conditional
mutual-information terms) and vary `P` (a three-deployment sweep).

## The separation the note lives on

**The theorem is Shannon's — 1948, used exactly as stated, first and always.** Entropy, mutual
information, and the chain rule are inherited, not proved, and nothing in the note strengthens,
extends, or tests them. What the note contributes is the **identification** alone: that the
quantity engineers experience as specification burden *is* verdict entropy. That is a modelling
claim. It is falsifiable in a way arithmetic is not, and the two never mix: where the
identification fails, the theorem is untouched; where it holds, every formal property is
inherited. The note polices this line in its own voice — conservation on the closing region is
"a theorem plus an identification", never a discovery, and never a "law".

## What the computations do and do not establish

The note computes the identity on a small exhaustive task (a date validator, two decompositions,
three actor encodings, chained splits, three deployment distributions) and estimates it through a
simulated retrieval channel (40,000 samples). It then states, before a reviewer can:
**an identity holding is not evidence.** `I(V;X) + H(V|X) = H(V)` holds for every joint
distribution; computing it and finding it holds establishes nothing about the framework, and
estimating it and finding it holds verifies the estimator.

What the computations *do* establish: the identification is **computable** for real task
descriptions; it is **non-degenerate** (values are neither zero nor everything, and they move
with structure); the framework's qualitative claims appear with the **right signs** (a
higher-information split really does buy cheaper parts; distractors really do push demand back
to judgment); and no contradiction appears across five worked instances on two tasks. What they
do not: that conservation is empirically true, that this is the *right* identification, that
`H(V)` predicts any engineering quantity, or anything about open predicates.

The falsifiable content is a correspondence claim, stated as a protocol and not run: `I(V;S)`
should predict the engineering cost of an interface (specification effort, boundary defect
rate, time to stabilise), and `I(V;E)` should predict which decisions an actor gets right
unaided. A decomposition with high `I(V;S)` and a reliably cheap interface contract would
falsify the identification with Shannon untouched.

## The boundary argument

`H(V)` requires a verdict function. An acceptance predicate that does not close is precisely
one that lacks a verdict function, so the measure does not exist there — not "is hard to
estimate"; does not exist. The framework independently locates the irreducible floor of a task
where its predicate fails to close, on grounds derived before this measure existed. The measure
goes silent in exactly that region. The note argues this coincidence — measurement and closure
having the same domain, with the line drawn by two arguments from different materials — is the
strongest available evidence that the identification tracks something real, and it bounds the
claim accordingly: conservation of specification demand is a theorem *for closing predicates*;
off that region the framework keeps only an accounting discipline.

A second boundary inside the first: the measure prices the **verdict**, not the search. A
lookup table and a SAT instance over the same input space carry the same `H(V)` with unboundedly
different generation costs (Cook–Levin). The note states this and never reads the measure as
pricing generation.

## The certification being asked for

This is a request for collaboration, not a courtesy read. Specifically, certification — or
correction — on four points:

1. **Standard usage.** The note's information theory is textbook-exact: no novel quantity, no
   extension, no result claimed beyond the chain rule applied to declared joint distributions.
2. **The framing.** The identity/identification separation is maintained everywhere — no
   passage presents arithmetic as evidence, and the estimated-channel instance is presented as
   a tractability demonstration, not as measurement of conservation.
3. **The failure semantics.** The identification's falsifier is correctly formed: the stated
   correspondence failures would refute the modelling claim while leaving the mathematics
   untouched, and nothing in the note would survive equivocally.
4. **The estimation caveat.** The note's closing caution — the theorem is exact; identifying
   the right conditioning variable for a deployed system is estimation, with error bars — is
   the right shape for the transition from worked examples to practice.

Anything that fails certification gets corrected, credited, and re-issued — the note's own
correction loop treats a certified objection as its most valuable input. Attribution per the
reviewer's preference, from acknowledgement to co-authorship of the correction.
