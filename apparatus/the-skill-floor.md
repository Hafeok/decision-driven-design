# The Skill Floor

**Location:** `apparatus/the-skill-floor.md`. A direct consequence of the floor result applied to
*skills* — any invokable capability that says what it does. Depends on the matched-pair invariant
and the encode/verify split (`apparatus/encode-verify.md`).

Upstream basis (pinned in `graph/upstream.yaml`; the floor result and its canonical term live in
the principle repo, not here):

<!-- ddd:ref id=DDD-floor-01 -->
<!-- ddd:ref id=term:floor -->
<!-- ddd:ref id=term:seam-identity -->
<!-- ddd:ref id=term:conservation -->

**Status:** the mechanism is derived and demonstrated (hard-capacity toy). The practical claim —
that unverified skills are the systematic locus of silent failure under load — is reported from
field use (a C# generation task that "passed validation but not inspection"), consistent with the
proof.

---

## The claim

> **A skill specified without a per-invocation verifier is floor-exposed. Its reliability in
> practice is not a property of how well it was authored — it is `1 − (overflow × openness)`, and
> it degrades exactly when the invoking context is loaded.**

Put plainly: *a skill without a verifier is not a capability. It is a specification you are hoping
holds.*

---

## Why a skill is specification without verification

A skill declares **what** it does. It almost never ships a **criterion-form check** that fires, per
invocation, confirming it did that thing on *this* input against *this* ground. In the store
vocabulary (`core/01`): a skill is an **encoded** constraint with no **mechanical** partner. It is
exactly the case the matched-pair invariant (`core/06`) forbids — encoding moved into place without a
check on the seam.

The floor result (`core/03`, hard-capacity proof) says what that means precisely. Escape requires
two conditions, both necessary:

1. **Overflow** — the task pushes past the actor's resolve capacity.
2. **Open** — the decision has no verifier the actor holds.

A skill without a per-invocation check satisfies condition (2) *by construction*. So the moment
condition (1) is also met — a loaded context, a large task, deep nesting — the skill's behaviour is
in the escape intersection, and it escapes **silently.** Nothing catches it, because catching it is
exactly the thing the skill omitted.

---

## Why authoring-time testing does not save it

The natural objection: *"but the skill was tested — it works."*

It was tested **once, at authoring time, on the author's cases.** That is a verification that
happened then and got compressed into the belief *"this skill works,"* which is now carried into
every future invocation as if it were ground.

This is the encode/verify split (`apparatus/encode-verify.md`) and the closure principle
(`apparatus/closure-principle.md`), together:

- The skill's future inputs are **ground the author did not control.** Each invocation is a new act
  against new ground.
- *"This skill works"* is therefore **an observation of uncontrolled ground, encoded as if it were a
  fact** — a cached belief consumed as ground on every subsequent run. Poisoned-ground-shaped.
- And **you cannot amortise an observation of something you do not control.** The one-time authoring
  check cannot cover invocations it never saw. Each act requires its own observation.

So *"it works"* is not a property the skill has. It is a claim that was true on the cases checked and
is **unverified on the case at hand.** The trust placed in it is **judgment** — per-invocation,
carried by whoever invokes it, non-amortising — wearing the costume of the encoded store.

> **A skill looks like the encoded store (write once, reuse) but behaves like the judgment store
> (must be re-checked every time). The gap between how it looks and how it behaves is exactly where
> the escape hides.**

---

## Why the intuition "we can't trust it works" is the correct verdict

It is not caution. It is the theorem. An unverified skill escapes its overflow, by the floor result.
The only open questions are quantitative:

- **How much overflow** — how far past resolve capacity the invoking task pushes. A trivial skill on
  a light task has near-zero overflow and near-zero escape; it is fine *in practice*, and the theory
  says why (the intersection is nearly empty).
- **How open** — how much of the skill's behaviour has no per-invocation check.

The reliability estimate follows directly from the hard-capacity formula:

> **P(skill behaves as intended) ≈ 1 − (overflow_fraction × open_fraction)**

A complex skill, invoked deep in a loaded context, with most of its behaviour unchecked, sits at high
overflow × high openness — which is precisely the C# generation task that compiled (the closing part
was caught) but violated conventions and size constraints (the open part escaped). *Passed
validation, failed inspection* is this formula, observed.

---

## What a trustworthy skill actually requires

The theorem is explicit, and it is not "author more carefully." Careful authoring raises the quality
of the *specification*; it does nothing to condition (2). The floor is removed only by attaching a
verifier.

> **A skill is trustworthy to exactly the degree it ships its own per-invocation verifier** — a
> check that fires on *this* run, against *this* ground, and can **fail closed.**

Not *"we tested it."* A criterion, in criterion form, executed at invocation. That is the matched
pair (`core/06`) applied to skills: the encoded capability and its mechanical check, shipped
together, or not trusted. Test 3 of the hard-capacity proof is the guarantee — when every decision is
verified, overflow produces *retries, not escape*, at any capacity. Verification converts silent
floor-escape into visible, recoverable cost. That conversion is the whole value.

And the fix is the one already observed in the field (Test 4): **convert open behaviour into verified
behaviour.** Encoding a convention as an explicit rule *with a check* moves it out of the escaping
class. Escape falls in proportion to how much you convert. This is not adding capacity — it is moving
decisions out of the floor.

---

## `ground` is the deliberate inverse

The reference tool `ground` (`applications/sdlc`, `ground-prd`) is the anti-skill, and now it is
clear this was never a matter of taste.

A skill is **all specification, no verification.** `ground` is **all verification, no
specification** — it refuses to say what should be true and only checks what *is* true, failing
closed on unreachable ground (INV-3). It is, precisely, the missing half of the matched pair, built
as a standalone product.

That a verification-only tool had to be built separately is itself evidence for the skill floor: the
specification half ships everywhere, unverified, so the scarce, valuable, deliberately-constructed
thing is the **check.** `ground` exists because skills systematically omit the one store that would
make them trustworthy.

---

## The one line

> **A skill is an encoded capability with no check — specification without verification — which the
> floor result identifies as exactly the class of decision that escapes under load. Its
> trustworthiness is not authored in; it is the fraction of its behaviour that ships a
> fail-closed, per-invocation verifier. Everything else is a specification you are hoping holds.**
