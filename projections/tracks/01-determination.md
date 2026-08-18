# Track 1 — Determination

**A single ordered path through the determination vocabulary, taught against one decision that
does not change.** Ten rungs. For software engineers; C#/.NET fluency assumed, framework
vocabulary assumed absent.

> **[PROPOSED] — rungs 1–5 drafted, Gate 2, 2026-08-18.** Nothing here is ratified. Emil merges
> and ratifies; this document proposes. Rungs 6–10 land at Gate 3.

---

## Manifest

| Field | Value |
|---|---|
| **Source canon** | `actor-indexed-determination` at **`v5.7.0`**, pinned in `graph/upstream.yaml` |
| **Audience** | software engineers — C#/.NET fluency assumed, no framework vocabulary assumed |
| **Register** | engineering |
| **Rendered** | 2026-08-18 |
| **Filter** | the determination vocabulary: what a decision is, what resolves it, what it is resolved against, and how an arrangement commits in advance |
| **Status floor** | none — every projected or draft node is flagged **at the point of use**, not only here |
| **Governing decision** | `DDD-dec-27` (rung order, filing, and the ground-provenance ruling) |
| **Track claim** | `DDD-track-01` — **files at Gate 3**; carries the track's pre-registered falsifier and its `Q27` revision dependency |

**Nodes cited, and their status at the pinned version.** A `ddd:ref` marker appears at each
node's first substantive use; the marker is what makes a stale citation mechanically detectable
rather than a matter of someone remembering.

| Node | Status at `v5.7.0` | First cited |
|---|---|---|
| `term:determinable` | settled | rung 1 |
| `term:determinate` | settled | rung 1 |
| `term:tolerance` | settled | rung 1 |
| `DDD-frame-13` | **projected** | rung 1 |
| `DDD-ground-05` | **projected** | rung 1 |
| `term:decision` | settled | rung 2 |
| `term:admission-test` | settled | rung 2 |
| `term:governing-decision` | settled | rung 2 |
| `term:ground` | settled | rung 3 |
| `DDD-ground-02` | **projected** | rung 3 |
| `term:actor` | settled | rung 4 |
| `term:arrangement` | settled | rung 4 |
| `term:judgment` | settled | rung 4 |
| `term:act` | settled | rung 4 |
| `DDD-frame-01` | **projected** | rung 5 |
| `DDD-frame-02` | **projected** | rung 5 |
| `term:commitment-level` | **draft — not in `v5.7.0`** | rung 5 |
| `term:capability` | settled | rung 5 |

> **Two nodes are pinned at a version that does not exist yet.** `term:commitment-level` and
> `term:residual-discretion` are proposed upstream in this same session and are **not present at
> `v5.7.0`**. They carry no `ddd:ref` marker and no pin until the upstream proposal is accepted
> and the pin advances to `v5.8.0`. Rungs 5 and 6 cite them in prose and say so where they do.
> This is the honest state, not an oversight: pinning an id that does not exist at the pinned ref
> would fail the cross-repo check outright.

---

## Before you start

**What this track gives you is capability, not competence.**

Rungs 1 through 9 teach you to see things you cannot currently see, and to say things you cannot
currently say. In the framework's own vocabulary that is **capability** — a typing over what
ground you can read and what distinctions you can resolve against it
<!-- ddd:ref id=term:capability --> — and capability is the entry fee. It is what lets you
attempt the work. It is not evidence that you did it, and it is not a qualification.

Nothing you own changes until rung 10, where you record one real decision from your own system
and put your name on it. Nine rungs of vocabulary with no rung 10 is a glossary you have read.

Read the rungs in order. Each one moves the same decision one step, and no rung needs a word a
later rung introduces.

## The decision

One decision, unchanged across all ten rungs. It is deliberately unglamorous.

```csharp
services.AddHttpClient<PaymentGatewayClient>()
    .AddPolicyHandler(HttpPolicyExtensions
        .HandleTransientHttpError()
        .WaitAndRetryAsync(3, attempt =>
            TimeSpan.FromSeconds(Math.Pow(2, attempt))));
```

**How many times do we retry a failed outbound call?** Here: three.

Three actors will appear at every rung, and they never merge:

| Actor | In this system |
|---|---|
| **the program** | the retry policy above — a `WaitAndRetryAsync` that runs the same way every time |
| **the LLM** | a model in the delivery pipeline that proposes the retry count when scaffolding a new client |
| **the on-call engineer** | the person who, at 03:00 with the gateway degraded, changes it |

Keep all three in view. Most of what the vocabulary buys you is the ability to say something
precise about *how they differ*, and the usual words — "automated", "manual", "human in the
loop" — cannot say it.

---

## Rung 1 — `3` is not a decision

**What you cannot do yet.** You can read that code and say "the retry count is three". You cannot
yet say what kind of thing "three" is, so you cannot say what would have to be true for a
different number to be *wrong* rather than merely different.

### The move

Two things are in that line and they are not the same thing.

<!-- ddd:ref id=term:determinable -->
The first is **retry-count**: a dimension along which the system could vary, where the variation
matters. That is a **determinable** — an outcome-relevant dimension of variation at the declared
tolerance. It is the axis. *(Canon uses the word "determinable"; engineers say "axis". They name
the same node — `term:determinable` reads, in canon, "the dimension of comparability an axis
names". This track uses "axis" in running prose and "determinable" where precision is needed.)*

<!-- ddd:ref id=term:determinate -->
The second is **3**: one specific way of occupying that axis. That is a **determinate** — what
resolving the decision produces. Not the axis plus a modifier; a way of being at the axis.

The asymmetry that makes this worth a rung:

| | Axis (determinable) | Value (determinate) |
|---|---|---|
| retry-count | the thing that can be governed | `3` |
| exists | before anyone chooses | only as an occupation of the axis |
| can be | declared, argued, owned, revisited | right or wrong, at a stated tolerance |
| answer to | "what varies here that matters?" | "and how did it land?" |

<!-- ddd:ref id=DDD-ground-05 -->
The order matters and is not stylistic. Declaring the axis is **constitutively prior** to
choosing a value on it: a value is only ever *a way of occupying* a declared axis, so a value
with no axis behind it is not a resolution of anything. *(`DDD-ground-05`, **projected** — a
clean derivation, unexercised. Flagged because you are reading a practice document: this is
canon's position, not a measured finding.)*

<!-- ddd:ref id=DDD-frame-13 -->
And "how fine-grained" is itself declared, not discovered. Determinateness comes in orders — red,
then scarlet, then this exact shade — and the **declared tolerance** names the order at which you
stop distinguishing <!-- ddd:ref id=term:tolerance -->. Whether `3` and `4` are different values
on your axis, or the same value at your grain, is something you say, not something the world
says. *(`DDD-frame-13`, **projected**.)*

### On the decision

`3` is not a decision. `3` is what a decision produced, or what happened where a decision was not
made — rung 9 is entirely about telling those two apart, and you cannot yet.

`retry-count` is the axis. Write it down as a name. The moment it has a name, three questions
become askable that were not askable before: *what values are permitted on it, who says, and
against what.*

Notice what the three actors share. The program, the LLM, and the on-call engineer all resolve
**the same axis**. They are not doing different jobs. This is the observation rung 4 is built on,
and it is invisible until the axis has a name.

### What you can now do

Name the axis under a literal. Not "why is it 3?" — **"what is the 3 a value of?"** Try it on the
last four constants you merged.

---

## Rung 2 — what makes it a decision

**What you cannot do yet.** You can name axes. You cannot yet tell which ones are worth
governing, so you will either govern everything and drown, or govern what is salient and miss
what matters.

### The move

Not every axis is a decision. There is a test, and it is a counterfactual, not a feeling.

<!-- ddd:ref id=term:admission-test -->
> **A choice is a decision iff varying *the choice* moves the outcome past tolerance.**
>
> **A fact is ground iff varying *the world* moves the outcome past tolerance.**

Read the first half now; the second is rung 3, and the fact that they are one test with two
directions is the point.

Three conditions have to hold together, and each one does real work:

| Condition | What it rules out | On retry-count |
|---|---|---|
| **declared** | an axis nobody has named — you cannot govern what has no name (rung 1) | somebody wrote `retry-count` down |
| **outcome-relevant** | axes whose variation stays inside tolerance | 3 vs 30 changes gateway load and customer-visible latency; 3 vs 4, at some tolerances, does not |
| **governed at a chosen abstraction and tolerance** | the pretence that "correct" is absolute | "the retry policy", not "this `Math.Pow` call"; and "p99 checkout latency under 800 ms", not "fast" |

<!-- ddd:ref id=term:tolerance -->
**Tolerance indexes everything.** It is the declared boundary of acceptable outcome deviation,
and without one the decision set is not well-formed — not "hard to evaluate", *not well-formed*.
Whether retry-count is a decision at all depends on a number you have to declare before the
question means anything.

This is the sentence engineers resist, so here it is concretely. At tolerance "the call
eventually succeeds", retry-count is barely a decision — 3, 5, 10, all fine. At tolerance "p99
checkout latency under 800 ms with the gateway degraded", retry-count is one of the two or three
things that decide whether you meet it. **Same axis, same code, same system.** The axis became a
decision when somebody declared a tolerance, and if nobody has declared one, the honest statement
is not "it's fine" — it is "we cannot say".

<!-- ddd:ref id=term:governing-decision -->
An axis that passes the test and has been resolved by something you can point at is a **governing
decision**. Rungs 4 and 5 are about what that something can be.

### On the decision

Run the test properly.

1. **Declared?** Yes, as of rung 1.
2. **Outcome-relevant?** Pick the tolerance first. Under "p99 checkout latency under 800 ms while
   the gateway is degraded": a failing call with three retries at exponential backoff holds a
   request open for roughly fourteen seconds before it gives up. That is not near the boundary.
   That is seventeen times past it. **Yes.**
3. **At what abstraction?** "The outbound retry policy for the payment gateway." Not the
   `Math.Pow` expression, which is an implementation of it. Not "resilience", which is a mood.

Retry-count is a decision. It was a decision before anyone decided it, which is exactly why rung
9 is possible.

### What you can now do

State the tolerance before arguing about the value. When the tolerance turns out not to exist,
you have found something more useful than the answer you were looking for.

---

## Rung 3 — ground, and where it comes from

**What you cannot do yet.** You can say retry-count is a decision. You cannot yet say what it
should be *resolved against*, so every discussion about the value collapses into whoever is most
confident.

### The move

<!-- ddd:ref id=term:ground -->
**Ground** is what a decision is determined against. It is the other half of rung 2's test, run
in the other direction: a fact is ground iff varying *the world* moves the outcome past tolerance.

**That definition is the whole of this rung's canon.** Note what it does not say. It does not say
ground is data, or telemetry, or documentation. Ground is defined by a counterfactual on the
world, so whether a fact is ground is a property of the decision and the tolerance — never of the
fact's format or where it is stored.

For retry-count, ground includes: the gateway's published rate limits, its actual behaviour under
load, whether its endpoints are idempotent, the checkout latency budget, and what the contract
with the payment provider obliges. Vary any of those and the right retry count moves.

#### Five kinds, and what they cost you — track-native, **not canon**

> ⚠️ **The five-way split below is expository scaffolding invented for teaching. It is not
> canon.** It is not a claim, and it is not a partition — the categories are not proven exclusive
> or exhaustive, and nothing in the framework rests on them. It appears here because engineers
> reliably conflate "we have a number for it" with "we know it", and naming the kinds breaks that
> conflation fast. The canon content of this rung is the definition above; if the scaffolding and
> the definition ever disagree, the definition wins.
>
> ⚠️ **`institutional` is additionally gated.** The mechanism by which authority, convention, and
> social practice supply ground is an open upstream question (`Q27`, trusted sources). Treat that
> row as the least settled of the five. `DDD-track-01` records this dependency: **if `Q27` lands,
> this section must be revised**, because a resolved `Q27` may restructure the split rather than
> confirm it.

| Kind | Where it comes from | On retry-count | What it costs you |
|---|---|---|---|
| **controlled** | maintained by your arrangement, enforceable by your own commitments | your latency budget; your circuit-breaker settings | cheap to read, and you can change it — but you can also change it *by accident* |
| **observed** | read from an external or independently changing system | the gateway's measured p99 and error rate last Tuesday | true when read, decaying afterwards at a rate nobody has stated |
| **inferred** | estimated from data or a model | "transient failures usually clear within two seconds" | carries the estimator's error, which does not appear in the number |
| **institutional** ⚠️ | rules, conventions, authority, social practice | "three is what our services do"; the provider's fair-use clause | often the real reason, almost never written down |
| **missing** | relevant, and unavailable to the arrangement executing | whether *this* failure is a blip or an outage starting | the dangerous one — see below |

**A stored statement about uncontrolled ground is not a current observation of it.** This is the
sentence to carry out of the rung. The gateway's p99 in your runbook is not the gateway's p99. It
is a claim about the gateway's p99, made on a date, by someone, and decaying since. How fast it
decays depends on drift rate, consequence, and your declared assurance level — not on a universal
"read it every time" rule, which is unaffordable, and not on "read it once", which is how
runbooks become fiction.

**Missing ground is the one to sit with.** It is not the absence of a fact. It is a fact that is
relevant — it passes the ground test — and unavailable to the actor doing the resolving. It will
matter twice: at rung 4, because the three actors have *different* ground missing, and at rung 9,
where a decision made against no ground at all still governs production.

<!-- ddd:ref id=DDD-ground-02 -->
Canon does carry an instrument here, and it is worth having early. Source coverage
(covered · declared-empty · undeclared · unknown), resolution (resolved · deliberately-open ·
unknown), and assurance (adequate · inadequate · unknown) are **orthogonal** — and the rule that
bites is that **Unknown is never a pass**. "We didn't check" and "we checked and there's nothing"
are different states, and only one of them is safe. *(`DDD-ground-02`, **projected**.)*

### On the decision

What is retry-count = 3 resolved against?

Ask the question out loud in your own system and observe how quickly the answer becomes "we'd
have to go and look". That reaction is the finding. The value has been in production for months;
the ground it is answerable to has never been assembled.

Now split it by actor, because they do not have the same ground available:

| Actor | Ground it can actually read |
|---|---|
| **the program** | its own configuration, the response status, elapsed time. Not the gateway's rate limits. Not the latency budget. |
| **the LLM** | the repository, the prompt, whatever was retrieved for it. Not last Tuesday's p99 unless something put it there. |
| **the on-call engineer** | the dashboard, the incident channel, the fact the gateway sounded odd yesterday — and eight years of pattern-matching that nobody has written down |

Same axis. Same tolerance. **Three different sets of missing ground.** This is the observation the
next rung is built on.

### What you can now do

Ask "against what?" and refuse the answer "against experience" without asking whose, and whether
anything the executing arrangement can read carries it.

---

## Rung 4 — actor and arrangement

**What you cannot do yet.** You can see that the three actors read different ground. You will
still, by reflex, compare them as *things* — "is the model as good as the engineer?" — and that
question has no answer, because it is not well-formed.

### The move

<!-- ddd:ref id=term:actor -->
An **actor** is a system that resolves decisions by reading ground: variation in declared ground
can alter the resolution through an internal pathway that selects among alternatives. A
thermostat qualifies. A falling rock does not. **Actorhood does not require intelligence**, and
the framework's use of "actor" is not a compliment.

<!-- ddd:ref id=term:act -->
All three of ours qualify, and they resolve the same axis at an **act** — the occasion on which a
determination is actually made.

Which raises the question you were reaching for at rung 3, and which the framework refuses in the
form you want to ask it.

<!-- ddd:ref id=term:arrangement -->
> The **arrangement** is the composition through which a resolution is produced and governed:
> executor, prior commitments, ground channels, checks, reviewers, record, and accountable
> principal. The unit of comparison is the arrangement, not the isolated actor.

Read the list. The executor is **one of eight items**. "Is the model as good as the engineer?"
varies one item and holds the other seven fixed by accident, then attributes the whole result to
the item that varied. It is the wrong unit, in the way that comparing two engines by their
pistons is the wrong unit.

Here are the three, written as arrangements:

| | **the program** | **the LLM** | **the on-call engineer** |
|---|---|---|---|
| executor | `WaitAndRetryAsync` | the model | the person |
| prior commitments | the compiled policy | the prompt, the house style, the scaffold | the runbook, the incident process |
| ground channels | response status, elapsed time | repository, retrieval, prompt | dashboards, the incident channel, colleagues, memory |
| checks | the integration suite | code review, the same suite | the deploy pipeline, or nothing at 03:00 |
| reviewers | whoever approved the PR | whoever approved the PR | possibly nobody until morning |
| record | git history | git history, if the tool is logged | a chat message, if they remember |
| accountable principal | the service owner | **the service owner — never the model** | the engineer, or the service owner, and this is usually unstated |

Now the differences are legible, and almost none of them are about the executor. The engineer's
arrangement has the richest ground channels and the weakest record. The program's has the
narrowest ground and a perfect record. The LLM's inherits its ground from whatever the pipeline
retrieved, which is a design choice somebody made and probably did not write down.

<!-- ddd:ref id=term:judgment -->
One line in that table needs its own definition, because it is where the framework is strictest.
**Judgment** is determination *during* the act, by an actor reading ground, **with an accountable
party named**. The last clause is not decoration:

> **A judgment allocation naming no accountable party is not an allocation. It is Escaped with an
> executor attached.**

"The on-call engineer will handle it" is not an allocation of the decision to judgment. It names
an executor. If no principal is named — if nobody's answer is required when it goes wrong — then
what you have is the forbidden state with somebody's name on the pager, which is worse than an
obvious gap because it looks handled.

### On the decision

Compare arrangements, not components.

The interesting result is that **the program's arrangement is the most tightly bounded and has
the least ground**, while **the engineer's has the most ground and the least record**. Neither is
better. They fail differently, and they fail differently *because of the seven items that are not
the executor*.

And most of those seven are changeable. You can give the program more ground — feed it the
gateway's published rate limits at startup instead of hard-coding around them. You can give the
engineer a record — a two-line entry that survives the incident. Neither change touches the
executor. Both change the arrangement, which is the unit that was under comparison all along.

### What you can now do

Fill in the seven non-executor rows before comparing two ways of resolving anything. When a row
is blank, that is the finding — most usefully the last row.

---

## Rung 5 — commitment level

**What you cannot do yet.** You can describe an arrangement. You cannot yet say *what it has
already settled* versus *what it leaves to the moment*, so you cannot say what changes when you
swap one actor for another.

### The move

The three actors are not three kinds of thing. They are three **levels at which an arrangement
commits behaviour in advance**.

> **[PROPOSED — not in `v5.7.0`.]** `term:commitment-level` is proposed upstream in this same
> session and does not exist at the pinned version, so it carries no `ddd:ref` marker yet. Its
> content is `DDD-frame-02`, which is pinned and cited below. The marker and pin land when the
> pin advances to `v5.8.0`.

> A **commitment level** is a level at which an arrangement fixes behaviour in advance:
> **outcome-level** — permitted resolutions fixed directly; **policy-level** — the generating
> procedure fixed; **principal-level** — a determiner selected by qualification and case-level
> resolution delegated. The three compose, and they are levels of commitment, not species of
> actor.

<!-- ddd:ref id=DDD-frame-02 -->
*(`DDD-frame-02`, **projected** — behavioural commitments attach at three levels which compose
and are not actor species.)*

Mapped onto the decision:

| Level | What is fixed in advance | Our instance | What is left at the act |
|---|---|---|---|
| **outcome** | the permitted resolutions themselves | `WaitAndRetryAsync(3, ...)` — the value is *in* the artefact | nothing about the count |
| **policy** | the procedure that generates a resolution | the LLM's scaffolding step: given a client of this shape, propose a retry count | which count, this time |
| **principal** | who resolves, chosen by qualification, the case delegated | the on-call engineer, trusted because of who they are and what they know | essentially all of it |

**"Not actor species" is the load-bearing phrase.** The program is not *inherently* outcome-level.
It is outcome-level **in this arrangement**, because somebody hard-coded a literal. Write the
count into configuration read at startup and the same executor becomes policy-level on that axis.
Have the model select from an enumerated set of three approved counts and it becomes
outcome-level. **The level is a property of the arrangement, not of the thing executing.** This
is why the vocabulary is worth learning: it moves the question from "what is it?" — unanswerable
— to "what has been committed?" — checkable.

**And they compose.** Your real system is likely all three at once: a principal is selected (the
service owner, who owns the payment integration), bound to a policy (the house resilience
standard), enforced by outcome constraints (a lint rule capping retries at five). That is one
axis governed at three levels simultaneously, which the "human vs. automated" framing cannot
represent at all.

<!-- ddd:ref id=DDD-frame-01 -->
Sitting under this is the reason the framework exists. Unresolved determination is indexed by
⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩ — **not by the task
alone** *(`DDD-frame-01`, **projected**)*. Change the arrangement and the determination problem
changes, even though the task — "pick a retry count" — is written the same way. A parameter that
never varies is indistinguishable from a constant, which is why holding the arrangement fixed
made the determiner look like one.

### On the decision

Ask, of the retry count in your own system: **at which levels has anything been committed?**

The usual answer is one level, by accident. A literal in a source file is an outcome-level
commitment made without anyone deciding to make one — nobody chose to fix the permitted
resolutions; somebody typed a number. That is a real commitment with no decision behind it, which
is rung 9's subject, and you now have three of the four words needed to say what is wrong with it.

### What you can now do

State an arrangement's commitment level per axis, and notice that changing the level is usually
cheaper than changing the executor. That is a design move you did not have before.

**What you still cannot do.** You cannot yet say what is left *unfixed* after the commitments are
applied, or why an arrangement that always produces the same answer is not thereby a correct one.
That is rung 6.

---

*Rungs 6–10 land at Gate 3.*
