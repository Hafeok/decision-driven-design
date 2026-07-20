# The Adversarial Ground

**Destination:** `core/` — as the adversarial reading of the closure principle
(`core/01-the-principle.md`, ground) and the seam-demand identity.

**Status:** projected, with unusually strong corroboration. The derivation is clean. The
empirical claim — that three independent fields discovered this mechanism, named it in their
own vocabularies, and converged on the same defence — is *reported from those fields' own
literatures*, not run as a campaign. That convergence is the evidence, and it is the strongest
kind a projected claim can have: three witnesses who never spoke to each other.

---

## The claim

> **The attack surface of any actor is its ground, not its logic.**

An adversary who attacks reasoning must defeat a capable actor at the thing it is best at. An
adversary who attacks **ground** lets the actor's own competence carry the payload. The second
is cheaper, more reliable, and nearly invisible — because the actor's reasoning remains sound
throughout. It is drawing correct conclusions from premises the adversary authored.

This is the closure principle (`an actor's own prior output is not ground`) read from the other
side. There, the actor poisoned its own ground by carelessness. Here, **someone poisons it on
purpose** — and every property of the failure class becomes an operational weapon.

---

## Why the adversary prefers ground

Recall the signature of poisoned ground: *the system is confident, the logic is sound, and the
outcome is catastrophic.* For an attacker, each clause is a feature.

**Confident** — the actor commits fully. No hesitation to exploit around; the authority is
already delegated.

**Sound logic** — nothing in the reasoning trips an alarm, because there is nothing wrong with
the reasoning. Defences aimed at the logic never fire.

**Catastrophic** — the actor's own authority is the blast radius. The attacker supplies a
premise; the victim supplies the force.

And the decisive economic fact, straight from the principle: **escape is the only store with no
window cost.** So an actor under pressure sheds decisions into it. The adversary's real move is
therefore not "make them believe X" — that is the goal, not the method. The method is:

> **Manufacture the pressure. Make independent verification expensive, slow, or unavailable,
> so the target relies on the channel you control.**

The attack is on **condition (3)** — the mandatory re-verification step. Defeat that, and the
poison flows through a substrate the victim trusts.

---

## Three fields, one mechanism

The strength of this claim is that it was found three times, independently, by people who were
not looking for a conservation principle.

### Intelligence: counterintelligence and deception

Military deception does not attack the enemy's analysis. It attacks the enemy's **ground**, and
lets first-rate analysts reason their way to the wrong place. The analyst who concludes the
landing is at Pas-de-Calais is not incompetent — they are reasoning impeccably over facts
someone else manufactured.

The tradecraft is entirely about condition (3): feed the channel the target trusts, corroborate
across channels you also control, and make independent verification costly enough to skip. The
target's certainty is not a bug to be induced; it is the *delivery mechanism*.

**Named in its own vocabulary:** "deception," "the trusted channel," "corroboration." The field
has understood for centuries that the substrate is the target and the reasoning is the vector.

### Cybersecurity: malware and evasion

Malware is a **purer** instance, because the whole contest happens at the moment of inspection,
before any act. The art is: *look like a fact until you are read as a fact, then stop being
one.*

- **Masquerade** (signed binaries, trusted names, `svchost` impersonation) — a false fact that
  passes inspection. The scanner reasons correctly (*signed, therefore trusted*) over a premise
  the attacker authored.
- **Time-bombs / logic bombs** — the ground is genuinely benign *when observed* and malicious
  *when acted upon*. This attacks the gap between inspection and act directly. It is the exact
  operational form of **"you cannot amortize an observation of something you do not control"**:
  the scan was true when it ran, and a belief with an expiry date by the time you execute.
- **Sandbox-aware malware** — behaves as benign ground *while watched*. The attacker reasons
  about your verification step and defeats it specifically. The cyber form of "feed the channel
  they are watching": it knows you refresh, so it stays clean during refresh.
- **TOCTOU (time-of-check to time-of-use)** — poisoned ground with the mechanism *written into
  the name*. Verify the file, use the file, swap it in between. The security literature isolated
  this bug class decades ago and named it precisely — independent discovery of the closure
  principle's condition-(3) failure.

### Infrastructure: state-based tooling

The canonical accidental instance, covered in the closure principle. The state file is a cached
belief consumed as ground; `plan = f(config, state)`, not `f(config, reality)`; the destructive
plan is a *correct inference over a false premise*. `refresh` is condition (3), correctly
implemented — and `-refresh=false` is the ecosystem making verification optional on exactly the
check that keeps the ground clean.

The difference from the other two fields is only intent: no adversary authored the state
divergence. But the *mechanism is identical*, which is the point. An accidental closed loop and
a weaponised one fail the same way, because the failure is structural, not motivational.

---

## The refinement: fact versus relation

One class of attack forces a genuine extension to the principle, and it belongs in core because
it changes what "verify the ground" can mean.

**Living-off-the-land.** The attacker uses *only* legitimate tools — the shell, signed system
binaries, sanctioned utilities. There is **no false fact to detect.** Every individual fact is
true. The binary is real, signed, and known-good; the command is legitimate; the network call
is to a permitted host.

Fact-level verification is defeated completely, because there is nothing false at the fact
level.

> **Poisoned ground is not always a false fact. Sometimes every fact is true, and the poison is
> in the relation.**

The malice is in the **composition** — the sequence, the timing, the *why* of legitimate
actions arranged into an unauthorised decision. And this is not a new principle; it is the
**seam-demand identity** seen adversarially:

> **|D_comp| = |D_single| + |S|**

The seam demand `S` — the decisions that exist only *between* the parts — is exactly where the
living-off-the-land attack lives. Verify every part and you have verified `D_single` for each,
and covered *none* of `S`. **You cannot verify a composition by verifying its components**, and
an adversary who works purely in the seam is invisible to any component-level check.

The industry discovered this the hard way and migrated accordingly:

| Detection era | Level | What it verifies |
|---|---|---|
| Signature-based | **fact** | is this binary known-bad? |
| Behavioural / EDR | **decision** | is this pattern of legitimate actions a decision nobody authorised? |

That migration *is* the field independently concluding that fact-level verification is
insufficient and the governing decisions must be watched directly. Which is the same reason, in
this framework, that `crossesBoundary` is a property of a **capability** and not of a **type**:
the boundary crossing is a decision about a relation, and it cannot be read off any single fact.

---

## The unified defence

Across all three fields the defence converges, and the convergence is the result.

> **Deny any single channel the authorship of your ground, and watch the decisions, not just
> the facts.**

Two components, and each answers one half of the attack.

**Against the false fact — redundancy of channel.** This reframes what redundant verification is
*for*.

> **Redundant verification is not about reliability. It is about denying any single actor the
> authorship of your ground.**

You do not verify a vendor's schema against their published spec because the spec might contain
a typo. You verify because **the spec and the running service are two channels, and if you read
only one, whoever controls it controls what you believe.** Independent, redundant,
mutually-uncorrelated channels are expensive not as insurance against error but as insurance
against *authorship* — a single channel is a single point of authorship, and an adversary needs
to own only what you actually read.

Counterintelligence calls this corroboration. Security calls it defence in depth. They are the
same move: raise the number of channels an adversary must simultaneously author from one to
many.

**Against the poisoned relation — verify at the decision level.** Where every fact is true, only
the composition can be checked, which means the governing decisions must be first-class and
observable. Behavioural detection, capability-level boundary analysis, and decision ledgers are
the same response: **watch what was decided, not merely what is present.**

---

## Consequences for the framework

**The adversarial projection has a primary mechanism now**, and it is not a footnote. The attack
surface of an actor is its ground. Hardening reasoning is nearly worthless if the substrate is
authored by the opponent — which reclassifies a scattered list of threats as one class:

- prompt injection → poisoned ground (false fact in the model's inspected context)
- supply-chain compromise → poisoned ground (false fact in a trusted dependency channel)
- disinformation → poisoned ground (false fact across corroborating channels)
- living-off-the-land → poisoned *relation* (true facts, unauthorised composition)

One class, and — modulo the fact/relation split — one defence.

**The reconnaissance cost is now fully explained.** The earlier account said adversarial ground
is expensive to read because *reading it perturbs it*. True, but incomplete. The deeper reason:
**an adversary is actively trying to author what your reconnaissance returns.** Recon is not
merely expensive; it is **contested**. Every channel you rely on is a channel someone wants to
own, which is why mutually-uncorrelated verification is worth its enormous cost — not for
reliability, but to deny single-point authorship of your ground.

**And it gives the encode/verify split its adversarial teeth.** "You must verify ground you do
not control" is, read adversarially: *you must assume the ground you do not control may be
authored against you, and a single reading of a single channel is a single point of authorship.*

---

## Falsification

The claim fails if an actor can be exhibited whose ground is genuinely uncontrolled *and*
adversarially contested, which is **nonetheless** securable by hardening its reasoning alone,
with no redundancy of channel and no decision-level observation.

No such actor is known, and the framework predicts none can exist: reasoning operates *over*
ground, so it is downstream of any poison in the substrate and cannot correct for it. The one
apparent exception — an actor whose ground is immutable and wholly controlled — is exactly the
case where the ground is not uncontrolled, the adversary has no write access, and the premise of
the claim does not obtain.

**The edge is exactly where the premise stops holding, which is the correct shape for a principle.**

---

## The one line

> **You do not defend an actor by making it think better. You defend it by controlling the
> authorship of what it believes — and where every belief is individually true, by watching the
> decisions rather than the facts.**

Three fields found this. None cited the others. That is what a real principle looks like from the
outside: the same shape, discovered independently, named three different ways.
