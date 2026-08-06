# The Closure Principle

**Location:** `apparatus/closure-principle.md`. Builds on the definition of ground in
`core/00-determination.md` and the four stores in `core/01-the-principle.md`.

**Status:** projected. The derivation is clean; the empirical claim (that observed
catastrophic failures in state-based tooling are instances of this) is reported, not
exercised.

---

**Upstream basis.** This document is part of the software projection; it builds on the
principle repo's canon (`actor-indexed-determination`). The `core/NN` references below resolve
there, pinned at a version and a status in `graph/upstream.yaml`:

<!-- ddd:ref id=term:determination -->
<!-- ddd:ref id=term:conservation -->

## The gap this closes

The current treatment defines **ground** as *the read-only surface actors inspect in order to
act*, and `fact` as one element of it. That is a definition by *role* — it says what ground is
**for**.

It does not say where ground may **come from**. And that omission admits a construction which
satisfies every word of the definition and destroys the principle's guarantees.

---

## The construction

An actor writes an artifact. On a later run, an actor inspects that artifact in order to act.

The artifact is read-only at the moment of inspection. It is a surface. It is inspected in
order to act. **It satisfies the definition of ground completely.**

But it is not a fact about the world. It is a **belief about the world, authored by an actor,
and now being consumed as if it were the world.**

---

## The principle

> ## An actor's own prior output is not ground.
>
> Ground is what you inspect *in order to* discover the state of the world. The moment an
> actor inspects its own belief instead of the world, it has closed a loop with **no
> corrective term** — and every error in the belief propagates into the act, carrying the
> actor's full authority.

Call this a **closed loop**, and the ground it produces **poisoned**.

---

## Why this is a *correctness* claim, not a hygiene one

The principle says every governing decision lands in one of four stores, and that `Escaped` — decided
by nobody — is the only forbidden state.

A closed loop manufactures escape *silently*, and worse: it manufactures escape that
**presents as coverage**.

Consider a decision D that depends on a fact F.

- **Open loop:** the actor reads F from the world. If F is unreadable, the actor knows it, and
  D is visibly unresolved. Escape is *detectable*.
- **Closed loop:** the actor reads F from its own cached belief B(F). If B(F) is stale or
  wrong, the actor **does not know it**. D is decided — confidently, mechanically, correctly
  *given the premise* — and the error is invisible until it is collected.

The decision was made. It was made *well*. It was made against a fact nobody verified.

**That is escape wearing the costume of encoding.** And it is the most dangerous form, because
every visible indicator says the decision is covered.

---

## The diagnostic

A closed loop exists wherever:

1. an actor **writes** an artifact describing the world, **and**
2. a later run **reads** that artifact **in place of** the world, **and**
3. there is **no mandatory re-verification** against the world.

All three are required. (1) and (2) alone are merely a cache — legitimate, and safe *iff* (3)
is absent, i.e. iff re-verification is mandatory and unskippable. **The poison is (3).**

---

## The canonical instance

Infrastructure-as-code tooling of the state-file kind reads three things:

| | What it is |
|---|---|
| **the configuration** | *your copy* — encoded, controlled, yours |
| **the live infrastructure** | *the source of truth* — uncontrolled, mutable, not yours |
| **the state file** | **neither** |

The state file is a cached belief about the source of truth — an artifact the tool wrote to
itself and reads back as fact. Which means the plan is computed as:

> **plan = f(config, state)** — not **f(config, reality)**

The diff is derived against a *belief*. When the belief is wrong — a change made out-of-band,
a bad import, a restored backup, a lost lock — the tool derives a **correct plan from a false
premise** and executes it with full authority.

The resulting destruction is not a defect in the diff engine. **The diff engine is working
perfectly, over poisoned ground.**

The decisive evidence is what the ecosystem did next. A `refresh` step exists precisely to
re-verify state against reality — condition (3), correctly implemented. It is slow. So a flag
was added to skip it, and skipping it became routine.

> **Verification was made optional on exactly the check that keeps the ground clean.**

That is not an implementation accident. It is the predicted consequence: **escape is the only
store with no window cost**, so a capacity-bound system under time pressure sheds decisions
into it. Here the pressure was latency, the actor was an organisation, and the decision shed
was *"is our belief still true?"*

---

## Relation to the encode/verify split

The existing rule:

> **You can encode ground you control. You must mechanically verify ground you don't.**

The closure principle is what makes that rule **non-circumventable**.

Without it, there is an apparent third option: *verify once, then encode the result, and read
the encoding thereafter.* This looks like a legitimate move — you did verify, and encoding
amortizes.

It is not. **Encoding a verification result converts a criterion into a constraint, and a
criterion over uncontrolled ground cannot be converted.** The whole content of "you do not
control it" is that it moves *after* you looked. An encoded observation of uncontrolled ground
is a belief with an expiry date and no alarm on it.

> **You cannot amortize an observation of something you do not control.**
> **Each act requires its own observation. That cost is irreducible, and it is the price of
> the ground being someone else's.**

This is the same shape as the Polanyi floor: a cost that cannot be moved, only paid. Attempting
to amortize it does not remove the cost — it converts a *known* cost into an *unknown* risk.

---

## Relation to the debugging projection

The five failure classes stand, and this **sharpens the boundary between two of them**.

**Stale encoding** — an encoded constraint no longer matches the world. Visible: the encoding
and the world can be compared, and the comparison is defined.

**Escape** — no store carries the decision.

A closed loop is neither, exactly. It is **stale encoding that has been promoted to ground**,
and thereby made *unfalsifiable within the system*. The actor cannot detect the staleness,
because detecting it would require inspecting the very thing the belief has replaced.

Propose a sixth class:

> **Poisoned ground** — the actor's substrate is its own prior belief. Failures are *correct
> inferences over false premises*. They are undetectable from inside the loop and present as
> normal operation until collected.

This class has a distinguishing signature worth recording: **the system is confident, the logic
is sound, and the outcome is catastrophic.** Stale encoding produces visible mismatches.
Escape produces visible gaps. Poisoned ground produces *confident, well-reasoned destruction.*

---

## Consequences for actors

The principle is actor-general, which is the test of whether it belongs in `core/`.

**Programs.** Any cache of uncontrolled state, read without revalidation. The state file is the
type specimen.

**Models.** A model that consumes its own prior output as context — summaries of summaries,
memory of memory, a scratchpad treated as retrieved fact — has closed a loop. Error compounds
with no corrective term, and the model's confidence does not decay to match. This is a
mechanism for a known failure mode, and it is *not* the same mechanism as escape-hallucination:
that is shedding under capacity pressure; this is **faithful reasoning over a corrupted
substrate**. The two require different remedies, and conflating them is why "just add more
context" sometimes makes things worse.

**Humans.** An expert who consults their model of the system rather than the system. The
mechanism is identical, the remedy is identical: **go and look.**

The remedy is the same in all three cases, which is what makes it a principle rather than an
observation:

> **Re-read the world. Every time. The observation is the cost of acting on ground you do not
> own.**

---

## Consequences for design

Three rules follow, and they are the operational form of the principle.

**1. Never persist an observation of uncontrolled ground as if it were a fact.**
Persist the *observation* — value, timestamp, and the fact that it was observed. Never persist
the *conclusion* with the observation discarded. The timestamp is not decoration; it is what
makes the belief falsifiable.

**2. Re-verification must be mandatory and unskippable.**
A verification step that can be turned off *will* be turned off, because escape has no window
cost and latency does. If skipping it is possible, it is not a verification step — it is a
suggestion.

**3. An actor that acts must not also cache what it acted upon.**
This is the sharpest form, and the one with real design teeth. Reporting tools may safely
observe. Acting tools must re-observe. **A tool that both acts and caches has the authority to
destroy and the memory to be wrong about why.**

---

## Falsification

The principle is falsified if a system can be exhibited that:

- consumes its own prior output as ground,
- has no mandatory re-verification,
- and is **nonetheless** immune to correct-inference-over-false-premise failure.

The only candidate is a system whose ground is genuinely immutable *and* wholly controlled — in
which case the belief cannot diverge from the world, because nothing else can write to the
world.

Note this is not a counterexample but a **boundary**: it is precisely the case where the ground
was never uncontrolled, and the encode/verify split says encoding was legitimate all along. The
principle does not apply, and it does not need to.

**Which is the correct shape for a principle: it should have an edge, and the edge should be exactly
where its premise stops holding.**
