# Accountability

**Destination:** `core/05-accountability.md` — immediately after `04-actors.md`, which it extends.
This seats accountability with the actor model and shifts former `05`–`09` to `06`–`10` (see the
canon patch register, P3.1). Actor-general, denominated in determinations. Depends on `00` (admission tests), `01` (the four stores), `03` (the
floor lives in the acceptance predicate) and `04` (pinning-resolution spectrum). Forward-references
`09` (the measure) and `10` (escape = overflow ∩ open), both of which now sit later in the read
order; the dependency is citational, not definitional.

**Status: projected.** Derived, unexercised. Falsifiers stated per claim. Nothing here is reported.

This document **introduces** two things core does not currently contain: an accountability condition
on actors (§§1–6) and the **assurance tower** (§7). Neither is cited from elsewhere in the repo, so
there are no dangling forward-references — but §7 is a substantive addition in its own right, and if
the tower is held back for a later release, §§1–6 stand without it and §7 lifts out cleanly. One
edit to `01`'s store table ships alongside (register P3.3).

---

## 1. The gap

`01` gives the four stores as **{rule, check, actor, nothing}**. Judgment's source is *an actor
reading ground*; Escaped's source is *nobody*.

The partition therefore turns on a distinction it never draws: **the difference between an actor
having produced a determination and there being somebody the determination is by.** A classical
program reads ground and determines choices — it satisfies `00`'s admission tests, and `04` lists it
as an actor. It cannot be answerable for anything. If actorhood alone were sufficient for the
Judgment store, a program-executed determination would be Judgment rather than Escaped, and the
forbidden state would be unreachable by construction.

It is not sufficient. Something else is required, and core does not currently say what.

> **Claim.** The Judgment store requires a second actor property that `04`'s spectrum does not
> supply, and the principle's one forbidden state is not well-defined without it.

---

## 2. Accountability capacity is a second axis, independent of pinning resolution

`04` ranks actors by **pinning resolution** — by value → by binding → by classification, tightest to
loosest. That axis answers *how reliably will this actor determine what was determined for it.* It
does not answer *can this actor be bound to the determination afterwards.*

The second question is not recoverable from the first, and the ordering is not the same. The
classical program is the **tightest**-pinned actor and has **zero** accountability capacity. The
human is the loosest-pinned and is the only current instance with full capacity. On this axis the
spectrum runs the other way.

> **Accountability capacity is a second axis of the actor model — independent of pinning resolution,
> in the sense that it is not recoverable from it — and the scarcer of the two.**

*Independent, not orthogonal.* The axes are not unrelated: §7 shows they are linked through
revocability. What holds is the weaker and more useful claim — knowing how tightly an actor can be
pinned tells you nothing about whether it can be bound to a determination afterwards.

**The conditions are not imported.** They follow from the pricing structure of the escaped store,
which `01` already states: escape costs nothing at the moment of the decision, and the bill arrives
later.

Escape is forbidden because it is **unpriced**. A price borne by nothing is not a price, so something
must bear it: **stake**. The bill arrives after the act — that is the whole of escape's cost
structure — so the bearer must still exist when it arrives: **persistence**. And the bill must be
deliverable: **sanctionability**.

All three fall out of the one state the principle forbids, which is why accountability is a
structural concern of the framework rather than an ethical annexe to it.

- **Persistence** — the actor continues to exist beyond the act.
- **Stake** — something of the actor's can be taken.
- **Sanctionability** — the actor has standing such that a sanction can be applied and can land.

**Persistence is the root, not one condition among three.** Stake requires something surviving to be
taken; sanctionability requires a target existing at sanction time. The other two stand on it.

| Actor | Pinning resolution | Accountability capacity |
|---|---|---|
| **Classical program** | tightest (by value) | **none** — no persistence as a deciding thing, no stake, nothing to sanction |
| **Model** | middle (by binding) | **none currently** — see §7; the incapacity is contingent |
| **Human** | loosest (by classification) | **full** — persists, holds stake, is sanctionable |

*Falsifier:* an actor bearing consequence without persistence — a sanction landing on something that
no longer exists in any sense that affects it.

---

## 3. Persistence of the actor, not of the artifact

Persistence must be persistence of the *determining actor*, not of an artifact associated with it.

Weights surviving for years are a persistent **artifact**. If every run is a fresh context with no
continuity linking act to consequence, nothing both determined and later exists to be sanctioned.
Artifact persistence with zero actor persistence does not satisfy §2.

What is required is a continuity binding act to consequence:

> **The thing sanctioned later must be identifiably the thing that determined earlier.**

This makes the condition **provenance-shaped, and therefore checkable**. Attribution over a
determination record is not documentation *of* accountability; it is the substrate that makes
accountability capacity computable rather than assumed.

---

## 4. The chain is attributable and tamper-evident, not internally held

A tempting formulation: an actor can be accountable only if it knows why it determined as it did.

**This is false, and it fails on the only actor with full capacity.** Humans routinely produce
fluent, confident, incorrect accounts of their own reasons. This is what `03` and `04` §3 together
predict: training buys cheap execution by *not* storing reasons — articulability is traded away by
the mechanism that manufactures the transfer floor. If self-held knowledge of *why* were the
criterion, the most trained actors would be the least accountable, which inverts observed practice.

**Corrected condition.** The chain must be:

- **Attributable** — binds a determination to an actor;
- **Tamper-evident** — cannot be rewritten after the consequence appears;
- **Persistent** — survives to sanction time.

Where the chain is stored is immaterial, and that it is external is the norm rather than a defect.
Decision records, contracts, signatures, stamped calculation packages, flight recorders and audit
logs exist *because* internal chains are unreliable — not as supplements to reliable ones.
Retrospective narrative repair is the failure mode these instruments are built against.

**Consequence (inversion).** On the provenance condition alone, an actor with an externalised
immutable record can *outperform* a human: every determination attributed, every input recorded, no
confabulation, no post-hoc repair. **The barrier to model accountability was never the chain.**
Models can win on the chain. The barrier is stake and sanctionability.

*Falsifier:* a domain where accountability is successfully assigned on an actor's self-report with
no attributable external record, and survives contest.

---

## 5. Answerability and liability are separable

Accountability decomposes into two obligations that come apart in practice and must not be fused:

- **Answerability** — the obligation to produce the chain: which determinations were made, by whom,
  against what ground.
- **Liability** — bearing the consequence.

They are separated deliberately in real practice:

- *Strict liability*: consequence borne, no account required.
- *Blameless postmortem*: full account required, liability suspended.

The postmortem norm is not a softening of accountability; it is a **purchase**. Liability is
suspended precisely to protect answerability, because when the two are fused, actors stop producing
chains — which is the same escape gradient `01` describes, one level up: producing a chain has an
immediate cost, and suppressing it does not.

> **Escalation routes a determination to an accountability-bearing actor — not merely to a more
> capable one.** Capability and accountability capacity are the two axes of §2; escalation moves
> along the second.

---

## 6. The two roles in the Judgment store

`01` gives Judgment's source as *an actor reading ground*. That is correct and stays. It elides one
distinction that matters as soon as the executing actor is not a human — and the elision is patched
directly into `01`'s store table alongside this chapter (canon patch register, P3.3):

- **Executor** — the actor making the determination this run.
- **Accountable party** — the actor bound to it afterwards.

For a human they are the same actor, which is why the elision was invisible: for every actor that had
ever occupied the Judgment store, the two coincided.

> **Refined reading.** *Judgment: per-run determination by a designated executor, with the
> consequence held by a named accountability-bearing actor. Where the executor lacks accountability
> capacity (§2), the two are recorded separately.*

> **A judgment allocation naming no accountable party is not an allocation. It is Escaped with an
> executor attached.**

This is `10`'s escape condition at the allocation layer rather than the run layer: the question *who
answers for this* is **open** — no closing predicate is available for it — and under load it is
resolved by nobody. Overflow ∩ open.

Note what this does **not** claim: that model-executed determinations are always escape. A model
executing under a named accountable human is a well-formed Judgment allocation. What is forbidden is
the allocation that names no one.

---

## 7. The assurance tower

`01`'s statement carries two qualifiers: *at a declared assurance level*, and *within a fixed
decomposition*. `01` already concedes that the second is itself a governing decision — **choosing the
decomposition is the highest-leverage governing decision there is.** The first has not been given the
same treatment. This section gives it.

**The declaration is internal.** The assurance level fixes which choices are governing decisions at
all (`00`, admission tests; `01`, granularity bound). Vary it and the set resizes. It therefore
passes `00`'s own admission test: varying it moves the outcome past tolerance. It is a governing
decision. If it were exogenous — outside every store — it would be a governing decision determined by
nobody, which is Escaped. **The framework would require its own forbidden state as a precondition.**

So level *n*'s assurance declaration is a governing decision at level *n+1*, with its own declared
assurance level, and so on. The regress must be shown to terminate.

**Termination requires two conditions, not one.**

1. **Descent.** Determining a tolerance governs a strictly smaller set than determining everything
   the tolerance governs. The chain is finite.
2. **Well-formedness.** The chain reaches an actor with accountability capacity (§2).

> **Finite is not terminated.** A chain descending to an actor incapable of bearing consequence does
> not bottom out — it **runs out**. Running out is escape at the top of the tower, and its signature
> is distinctive: not a defect but an **unfalsifiable ledger**, in which every coverage claim below is
> true by vacuity because the bound was declared by nobody who can answer for it.

Detectable by inspection one level down: a tolerance with no accountable declarer is escaped on its
face.

**On the descent measure — booked honestly.** `09` defines demand as `H(verdict)` and states that the
measure exists **only where the acceptance predicate closes**. A tolerance declaration generally has
no closing predicate — *"was this the right assurance level?"* is the open question par excellence. So
`H(verdict)` is undefined up the tower, and the descent argument above rests on **governing-set
cardinality**, which `09` §1 explicitly demotes as a measure of demand. The descent claim is
therefore weaker than it looks: an argument about set inclusion, not about bits. It must not be read
as licensed by `09`.

*Falsifiers:* a task whose tolerance decision does not govern a strictly smaller set than the task
itself (breaks descent); a well-formed practice whose tower terminates at an actor satisfying none of
§2's conditions (breaks well-formedness).

### 7.1 Result: revocability is why the loosest-pinned actor is the one that can answer

`04` records the human capability envelope as *individual, expiring, and not instance-general* — read
until now purely as the weakness of classification pinning, the price of using an actor you cannot
pin tighter.

It is not only a weakness. **Expiry is the mechanism of revocation, revocation is the mechanism of
sanction, and sanction is the substrate of accountability (§2).** An envelope that could not be
withdrawn could not be a stake.

> **The property that makes an actor hardest to constrain is the property that makes it able to
> answer.**

This is the link between the two axes of §2, and it explains the inversion noted there: the
tightest-pinned actor has no accountability capacity, and the loosest-pinned has full capacity. The
ordering is not a coincidence. Pinning by value leaves nothing to revoke.

**On model actors.** Present incapacity is **contingent, not necessary**. It rests on persistence,
stake and sanctionability — all currently absent, none logically impossible. Model deprecation and
version retirement are structurally decertification: expiry, exercised. What is missing is not the
mechanism but its attachment — it is wielded by an operator for operational reasons, not by a
certifying body in response to a specific act. **Today's towers terminate at the operator, not at the
model.** Making a model accountable would relocate the base case, not create one. Corporate
personhood is the existence proof that accountability-bearing actors can be **manufactured** when a
domain requires one.

---

## 8. Where this stops

The framework determines **who must answer, and for which determinations.** That is structure, and it
follows from the principle.

It does **not** determine **what the consequence should be.** Proportionality is set by impact on
affected parties and is exogenous — the same status `09` §7 gives the region where the measure ceases
to exist, and the same status ground-characterisation has throughout: required as input, not
producible by the framework.

This limit is declared, not conceded. The framework does speak to **irreversibility**, which is
structural: where the reversibility window is zero, no criterion can arrive in time and the governing
determinations must be pre-made. That is a statement about allocation, not about desert.

The legal-personhood question is bracketed, but the framework explains why it is difficult without
taking a position: legal personhood *is* the manufacture of an accountability-bearing actor, which is
why corporate personhood is the governing precedent and why the debate turns on persistence, stake
and sanctionability rather than on capability.

---

## 9. The result, in one line

> **Judgment requires an actor that can be bound to a determination after the fact — one that
> persists, holds stake, can be sanctioned, and is tied to the determination by a record nobody can
> rewrite. Actorhood is not enough: a store naming an executor but no accountable party is escape
> wearing a name.**

---

## 10. Open

- Whether accountability capacity is **graded** or **binary**. Binary is assumed above; institutional
  actors suggest gradation.
- Whether answerability and liability need distinct notation, or one accountable-party field with a
  liability-suspended flag suffices.
- Whether escape at the top of the tower warrants its own term or is simply Escaped at level *n+1*,
  with the level index carrying the distinction. Preference: no new term.
- Whether a measure-theoretic descent argument can be recovered for the tower at all given `09`'s
  closure restriction, or whether the cardinality argument is the best available and should be
  labelled as such permanently.
