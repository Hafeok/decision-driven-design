# Holding note — ground axes, decision regions, delivery, and the exploration/incident cycle

**Status of this document.** Unratified in its entirety. No item below has canon status. Produced from a
conversational session; Emil originating, Claude developing consequences. Emil is sole ratifier.

**Date.** 2026-08-15. Revision 18.

**Queue position.** Behind the measure note. Nothing here displaces the MDL/related-work section or any
open claim-status task. Two items (§11, §12) belong inside the queued escape reconciliation rather than
beside it.

**Layer.** Positions and regions are synchronic (Layer 1). The sweep, the incident construct, the map,
the direction, delivery, and as-of decay all require persistence and are Layer 2. See §8.

**Revision note.** Revision 1 was dated 2026-08-12, written from context rather than from a clock the
arrangement could read. The axis existed, was readable, and no decision governed its use — an instance
of the uncovered-undeclared state defined in Q3, occurring inside a document defining it. Recorded
rather than silently fixed.

---

## 1. Originating move, and the limit that bounds everything after it

### 1.1 Originating move

Emil's opening statement, restated:

> By applying dimensions to the ground of a decision, we can back-track when a given decision is
> relevant.

This inverts the quantifier in the existing ground definition. The upstream definition fixes a decision
and asks which facts are ground for it. The proposed move fixes a ground dimension and asks over which
coordinates the decision is live. Same tolerance test, opposite direction.

The consequence that makes it load-bearing: a decision becomes a **region** in a factored ground space,
and retrieval of the governing set for an act becomes a position lookup rather than a hand-maintained
applicability field.

The session's later turns supply the motivation the opening move lacked. Position-indexed retrieval is
not a convenience over hand-maintained applicability fields. It is the only form a **reading actor** can
use, because retrieval happens mid-act, precision matters more than recall at that moment, and a
governing set carrying noise is discarded wholesale. An imprecise index is worse than none. See §7.

### 1.2 The declared-space limit

Stated once, here, because it applies to every instrument in this note and was previously scattered as
four separate caveats. Emil's formulation: *unknown unknowns will produce incidents.*

> Every instrument in this construction evaluates **against the declared coordinate system**. None can
> see outside it.

| Instrument | Blind to |
|---|---|
| Coverage sweep (Q8) | gaps *in* the declared space, as against gaps *within* it |
| As-of decay (Q11) | drift on axes nobody declared |
| Delivery check (Q16–Q18) | axes misdefined but correctly extracted |
| Extraction verification (Q20) | the same |

This is not a defect of any one instrument. It is a property of the construction, and it is why the
cycle in §8 is not self-starting and why tier 1 incidents remain the only channel that widens geometry.

**Two findings, two addressees.** The limit produces two distinguishable states and the vocabulary
should not merge them, because one has a queue and the other has only a channel.

| | Detectability | Route |
|---|---|---|
| Known unknown — an extraction predicate that fails to close | The tool knows which axis and why | Report and escalate; a human or model determines why and files a decision |
| Unknown unknown — an axis misdefined, correctly extracted | Nothing fails; every check passes | Surfaces only as an incident, after an act goes wrong |

**Consequence for tool output, and it should be built in rather than documented.** Any coverage figure
over declared axes is a completeness claim *relative to the coordinate system*, and reporting it
unqualified will be read as absolute. This is the standard coverage-metric failure — MC-DC at 100%
means the code, not the requirements. The qualifier belongs in the output.

---

## 2. Ratification queue — ground axes and regions

Each item is a candidate for canon entry. None is filed. Falsifiers in §5.

### Q1 — Axis-naming as a filing gate

> A decision file requires at least one named ground axis.

Proposed as structurally symmetric to the existing falsifier-requires-claim rule: both refuse entry to
something unfalsifiable in its own register. Claims must state what would break them; decisions must
state where they apply.

Diagnostic reading: if no axis can be named, no outcome-relevant alternative has been declared over any
ground, so the artifact fails the decision admission test. It is a stated intention, not a decision.
Distinguish from the case where an axis is nameable but not evaluable — that is closure failure, a
legitimate filing that routes through the assurance gate.

**Second argument for the gate, added revision 2.** Naming the axis at authoring is prior commitment
purchased against retrieval cost. The precision has to be paid for somewhere; naming it at authoring is
affordable because the author is not mid-act. This makes Q1 an instance of the allocation principle
rather than only a hygiene rule. See §7.

### Q2 — Region-based retrieval

Decisions as regions over declared axes; the governing set for an act is those regions containing the
act's position.

### Q3 — Four-state typing of ground

| State | Meaning |
|---|---|
| governed | a filed decision covers this region |
| inert | declared: no outcome-relevant alternative here |
| open | declared: alternative here, deliberately unresolved, under observation |
| uncovered-undeclared | none of the above |

Only the fourth is a finding. The point of the typing is that a retrieval miss resolves to a named state
rather than an ambiguity between *nothing applies*, *nobody filed*, and *we are deliberately watching*.
This is what makes the sweep mechanisable rather than advisory.

Whether *inert* and *open* are one construct with two values is an open ruling (§6).

### Q4 — Incident definition

> An incident is a dated observation that an act occurred which no filed decision governed at the
> declared assurance level — or which was so governed and the assurance proved inadequate.

Properties:

- Outcome does not enter the criterion. An act in ungoverned ground is an incident whether or not the
  verdict was acceptable.
- Accepted risk realising is **not** an incident. A decision filed, assured, with residual risk
  explicitly accepted, that then goes badly, is the arrangement working. Counting it would make the
  detector fire on correct governance and train against filing risk acceptances. Guard this carve
  hardest.
- A sweep finding is not an incident. The sweep reads declared geometry; incidents arrive from outside
  it.

### Q5 — Incident tiering by yield

| Tier | Yield | Effect |
|---|---|---|
| 1 | a ground axis not previously declared | geometry widens; sweep re-runs, may surface untriggered siblings |
| 2 | an uncovered region on an existing axis | filing gap; no geometry change |
| 3 | closure failure on a governed region | assurance gate, not ground space |

### Q6 — Exploration/incident carve by authored basis

Deliberate exploration is ungoverned at the decision level — that is what makes it informative. What
separates it from an incident is not governance of the act but that the region was **declared in
advance as the object of the act**.

An act whose basis is `experiment` over a named region is exploration; an act with no basis over that
region is an incident. Same ledger, one field apart. The declaration must precede the act, or every
escape becomes retrospectively into learning and the detector goes silent.

### Q7 — Bound-exceedance default (Emil's ruling, session 1)

> Exceeding a declared experiment bound is an incident by default. An experiment declaration may state
> at authoring time that out-of-bound acts are within scope — that discovering the bound's location is
> the object of the experiment. Where it does so, out-of-bound acts are amendments rather than
> incidents. Absent that statement, the default holds.

The exception is authored, so hindsight cannot reach it. The default is the safe direction: an escape
misfiled as an incident costs a review; an incident absorbed as an amendment costs a lost axis.

### Q8 — Coverage sweep, scoped

Take the complement of filed regions over declared axes; uncovered regions are candidate escapes.

Three stated limits, all of which must ship with the construct:

1. **Source half only.** Uncovered implies a candidate escape; covered implies nothing, because a routed
   decision may still have an inadequate gate. Covered-but-unassured is a separate detector, out of
   scope (recommendation accepted, session 1).
2. **Blind to undeclared axes.** The sweep finds gaps *within* the declared ground space, never gaps
   *in* it. Strongest against oversight, weakest against blind spots proper.
3. **Blind to undelivered governance.** Added revision 2. A decision filed, adequate, and never reached
   by the act presents to the sweep as covered. See Q12.

### Q9 — Demand-weighted ranking of coverage gaps

Rank candidate gaps by demand carried, not by count. Cardinality treats a rarely-occurring uncovered
region and a high-traffic one alike — the same objection §1 of the measure draft makes to counting
decisions.

Constraint: `H(V)` requires a closing predicate, which uncovered ground often lacks. The map is dense
where it is least needed and sparse where the finding would matter most. This caps the method and the
cap should be stated at filing.

### Q10 — Positional view over governed regions

`I(V;X)` against `H(V|X)` per region, with the residual labelled **unallocated**, not *judgement*.

Scope note that must travel with it: this instrument is honest in *governed* ground, which inverts the
motivation the thread started from. The sweep and the map are different instruments over the same
coordinates. A note presenting the map as answering the escape question would misread its own scope.

---

## 3. Ratification queue — time, decay, and revisitation

### Q11 — As-of on every ground reading

The originating observation was that time should be a primary ground axis. It resolves into two claims
of different strength.

**Weaker, and task-specific.** Time as a **coordinate**: deadlines, business hours, an age threshold.
Declared like any other axis, primary in some tasks and absent in others.

**Stronger, and universal.** Time as a **validity index** on every ground reading:

> Every ground reading carries an as-of, and therefore every statement of position is a claim that
> decays.

The type argument for the split: if time were a coordinate you would add one and be done. But each other
coordinate was read at its own moment — repository state minutes ago, dependency versions yesterday,
architectural convention whenever someone last looked. One clock per axis is not a coordinate. It is a
property attaching to each of them.

Consequence for Q2: region membership becomes a claim with an age rather than a boolean, and a retrieval
answer inherits the age of its **worst-aged coordinate**. That is computable and more useful than
per-item freshness.

This is already implicit upstream, which says a stored statement about uncontrolled ground is not
equivalent to a current observation, with revalidation cadence set by drift rate, consequence,
consistency guarantee, and assurance level. What was missing was the name and the detector.

**Amendment (revision 13): the reading is a three-tuple.** Alongside as-of and provenance (Q12), each
reading carries **the assurance at which it was made** — instrument, method, or the trust decision
behind it (Q27). Emil's ice: "looks good enough" is an eyeball at low assurance; a truck needs a gauge
at high assurance; using the first for the second is the fault. The act's α is a requirement, the
reading's assurance is a property, and **the mismatch is the fault class** — not a comparison of trust
scores. This is why "how trusted is the ground" is *not* a parameter on ground: closure is
per-arrangement and per-predicate, so the same reading is trusted-enough for one act and not another,
and a scalar stamp would have to be recomputed per act anyway. The self-assessment case (§7.4)
resolves without a rule about who is competent: it is a low-assurance reading, fine for low-α acts,
a fault when it feeds high-α ones — the framework says which acts may stand on it, not whether the
questionnaire is good.

Guard: three things stay distinct — the source's trust status (a filed ceiling, Q27), the reading's
assurance (per reading), and the act's requirement (per act). A scalar would have collapsed them.

### Q12 — Ground not as expected at act time (Emil's ruling, session 2)

> Stale ground is the same mechanism as poisoned ground. It is not escape. It is ground not as expected
> at act time.

The class separates from escape on remedy, which is the test it should pass:

| | Governance | Ground | Remedy |
|---|---|---|---|
| Escape | absent or inadequate | as expected | file a decision, close the gate |
| Ground not as expected | present and adequate | not as assumed | revalidation cadence |

Two refinements offered and unratified:

- **The rate parameter is provenance, not elapsed time alone.** Controlled ground may not drift at all;
  observed and inferred ground drift at their source's rate. Risk is elapsed time *scaled by* drift
  rate, and the existing provenance typing already supplies the scaling.
- **Poisoning breaks the time monotonicity, and only that.** Decay is drift-like and monotone in elapsed
  time; an adversary can poison the instant after a reading. Same class, two generators, one rate
  structure each. Cadence bounds the decay generator and does nothing against poisoning.

Detector-wise this needs its own instrument. The coverage sweep is blind here by construction, since
governance is present and the region is covered.

### Q13 — Only one interval survives (Emil's ruling, session 2)

Claude proposed two intervals: decision-to-act and reading-to-act. Emil ruled the first out:

> A decision made a year ago on ground that has since moved was a decision that needed making again on
> current ground. That is supersession, a decision-level event with its own act, not a ground-freshness
> property.

So **reading-to-act is the only real interval**, and the decision ladder already handles the other case.

### Q14 — Reading-triggered revisitation

Emil's question, and the more valuable direction:

> Does reading ground in order to act determine when a given decision should be revisited?

Proposed mechanism: a reading that diverges from what a decision assumed is evidence the decision needs
remaking. Divergence within tolerance is the normal case — that is what tolerance is for. Divergence
beyond the tolerance the decision declared is a trigger, observable at act time by whoever is already
reading the ground.

Why it beats scheduled review: calendar cadence is a proxy for drift and a poor one, firing on untouched
regions and missing fast-moving ones. Reading-triggered revisitation fires proportional to actual
traffic and actual movement, and the reading was going to happen anyway for the act, so the detector is
nearly free.

**Precondition.** A decision must record what it **assumed about ground**, not only which region it
covers. Region membership answers *does this apply here*; the assumption answers *does the ground still
look like what I was authored against*. Two fields, and only the first is in the Q1 gate.

**Possible resolution of an outstanding item.** This may answer the `watched:` / `revisit_if` edge-type
ontology — `revisit_if` as a declared tolerance on a ground assumption, evaluated at read time, rather
than as an edge type. Whether it collapses into that or stays distinct is Emil's.

*Flagged:* this makes ground-reading an act with governance consequences, which may pull readings
themselves into the ledger. Cost not assessed.

### Q21 — Ground pinning as the second remedy

Q12 named cadence as the remedy for ground not as expected. Pinning is the other one, and where
available it is stronger, because it removes the decay rather than bounding it.

Emil's two examples are **not the same mechanism**, and the distinction should survive into the
vocabulary, since *pinned* reads like the second and gets used for both.

| | Mechanism | Fails by |
|---|---|---|
| Oven holding 180° | **Regulation** — closed-loop sensing and correction | drifting out of band undetected; sensor failure is silent |
| CI build | **Constraint** — lockfile, digest, hermetic environment; deviation refused at entry | the pin not covering everything: transitive dependencies, ambient environment, clock, network |

Regulation holds ground within tolerance by acting on it; pinning holds it by refusing to proceed if it
differs. Ashby's regulator against an outcome-level commitment.

**Three connections into the rest of the note.**

- **Pinning collapses as-of decay.** A pinned coordinate does not age relative to the act, so Q11's
  worst-aged-coordinate calculation skips it. This identifies which axes need the decay machinery at
  all.
- **Pinning makes axes mechanically evaluable.** Extraction over a pinned value closes trivially, so
  pinning is a route to Q19's mechanical delivery rather than merely adjacent to it.
- **Drift moves rather than disappearing, and this is the one to watch.** A pinned value stops ageing
  relative to the act and starts ageing relative to the world — pinned dependencies become insecure
  precisely because they do not move. Pinning converts decay-of-reading into decay-of-relevance, which
  surfaces as **supersession** (Q13) rather than as ground-not-as-expected (Q12). Different class,
  different detector, and it is what makes lockfiles dangerous rather than merely stale.

**Typing.** Pinning is a commitment about ground, so it is neither source nor assurance — it acts on the
provenance axis, converting observed or inferred ground to controlled. The *check that the pin holds* is
the assurance gate. Two objects, and they should not be filed as one.

### Q22 — Interval as drift exposure: the PR case (Emil)

> A PR should not live more than a day or two, because you pay the drift penalty of main shifting.

Structurally this is Q13's reading-to-act interval with the branch point as the reading. The PR is
authored against main-at-branch-time and merged against main-at-merge-time.

**It is the cleanest instance in the note, because both the interval and the drift rate are directly
measurable.** The rate parameter takes an observable form: exposure is not days but
**commits-to-touched-paths since branch**. A week-old PR in a quiet region carries less exposure than a
day-old one across a busy interface.

Two features the oven and CI cases do not have:

- **Merge conflict is the detected fraction; the undetected fraction is the interesting one.** Textual
  conflict is a mechanical check with a closing predicate, so that portion has a gate. Semantic drift —
  main changed a contract the PR still satisfies textually — passes cleanly. Green means *no textual
  conflict* and is read as *no drift*, which is presumed discharge in Q18's sense.
- **Rebase is revalidation, the cadence remedy applied per-PR.** It re-reads the ground and so bounds
  decay, but it detects the semantic fraction no better than the merge does.

**This case cuts against Q21.** A PR pinned to its branch point ages worse, not better. The practice is
short-interval *because* the ground is uncontrolled and must not be pinned. Pinning and short-interval
are therefore alternative remedies selected by whether the ground is yours to control — and main is not.

**Differential prediction, which is where the content is.** The practice supplies a heuristic ("a day or
two"); the model supplies a rate. It predicts that safe interval varies by region and should be
measurable rather than conventional. That is the part that can be wrong.

*Flagged:* trunk-based development and continuous-integration literature argue this empirically —
batch size, integration frequency, DORA metrics. Unchecked. If the correspondence campaign wants a
domain where interface cost and drift are already instrumented, this is the strongest candidate in the
note.

### 3.1 Postdiction caution

Recorded because it applies to Q22 and to three other results in this note.

The thread has now explained four practices that were already known and independently derived: rebase
frequency, writing things down, the cost of multitasking, and PR age. Each read as confirmation while
being written. **None is evidence.** Trunk-based development would be just as correct if the
ground-decay account were false.

What the account buys in each case is a **rate or ranking parameter where the practice has a
heuristic**, and the claim lives entirely where the two come apart — commits-to-touched-paths against
elapsed days (Q22), verdict entropy against usage mass (Q9), named-axis retrievability against recall
effort (§7.1). A model that only reproduces known practice is a frame. A model that says the convention
is wrong in specific identifiable cases is a claim.

The honest current status: the model is **coherent across cases**, which is a precondition for being
right and not evidence of it.

---

## 4. Ratification queue — delivery

The session's largest addition, and Emil's assessment: an important distinction needing its own
vocabulary, whether it projects existing machinery or is new.

### Q15 — Filing is not encoding

> A decision sits in `I(V;X)` only to the extent the arrangement actually delivers it at act time.

A ledger entry that judgement fails to retrieve was never in the encoding. It looked like it was, because
someone paid the authoring cost. Store allocation can therefore be read wrongly by counting the ledger
rather than the delivery. The paid-once-inherited-by-every-run property belongs to **mechanical
delivery** specifically, not to standing supply generally.

### Q16 — Three delivery mechanisms

| Mechanism | Authored | Delivered | Failure mode |
|---|---|---|---|
| Standing, mechanical | once | per act, without judgement | gate wrong or absent |
| Standing, judgement-mediated | once | per act, by judgement | not retrieved, or **misapplied** |
| Occasioned | — | at act | resolved wrongly |

**Misapplication is unique to the middle row.** A fresh decision can be wrong; a retrieved one can be
correct and applied to a position it does not govern.

**Sharpening of "most uncertain."** Emil's formulation was that retrieving standing decisions at
judgement time is the most uncertain way to apply them. Whether the failure *rate* is highest is
empirical and actor-dependent. What is structural is worse: this mechanism **fails while presenting as
compliance**. Occasioned resolution that goes badly is attributable to the act; an unretrieved standing
decision leaves the ledger looking exactly as it does when things work.

### Q17 — The split applies identically to assurance (Emil's extension)

Source and assurance are separate dimensions upstream. The delivery split cuts across both identically,
which is a mark in favour of it being real rather than an artefact of the source side.

A judgement-retrieved check has the same three failure modes: not retrieved, retrieved and misapplied,
retrieved and applied correctly. Two things the assurance side adds:

**Failures compound rather than stack.** An unretrieved decision plus an unretrieved check over the same
act is a second failure correlated with the first — same actor, same budget, same position, missed both.
Independence is what makes a gate worth anything, and judgement-mediated delivery on both sides silently
removes it.

**Retrieval failure is invisible to the check's own record.** A gate reports *passed* meaning
applied-and-satisfied or meaning never-reached, and nothing in the artefact distinguishes them. On the
source side the act's outcome is at least available to argue from. Here the evidence is the check saying
it is fine.

**Testable design consequence.** Mechanical delivery matters more on the assurance side than the source
side, because the assurance side has no independent signal that delivery happened. This predicts that
arrangements mechanising checks while leaving decision retrieval to judgement should outperform the
reverse, holding the content of both constant.

### Q18 — Proposed vocabulary

Candidates for the slots. The slot inventory is likelier to be right than the names.

| Slot | What it names | Candidate |
|---|---|---|
| The axis | how authored governance reaches an act | **delivery** |
| Value 1 | reaches the act without judgement | mechanical delivery |
| Value 2 | reaches the act only if an actor recalls it | judgement-mediated delivery |
| The failure | filed, adequate, never reached | **undelivered** |
| The record property | a gate's *pass* meaning never-reached | **presumed discharge** |

*Delivery* sits next to supply rather than replacing it: standing supply says when the demand was paid,
delivery says whether the payment arrives. They come apart, which is the whole finding.

*Presumed discharge* is the term to argue hardest for, because it names what makes this dangerous rather
than merely inefficient: the artefact recording the skip is identical to the artefact recording the
pass. Naming the record state rather than the actor's omission keeps it mechanisable — one can ask a
discharge ref whether it distinguishes the two senses.

*Judgement-mediated* is preferred over *retrieved* because retrieval is only half of it; misapplication
is delivery to the wrong position, which *retrieved* does not cover. Uglier and more accurate.

**Open, and it points two ways.** Undelivered governance means the act was not in fact governed at the
declared assurance level, which reads as escape by delivery failure. It presents as covered, which is
why it needs a distinct name — but if it is a **generator** of escape rather than a sibling, the
vocabulary should show that. Note this sits opposite the Q12 ruling, which put ground-not-as-expected
outside escape on the grounds that governance was present and adequate. Here it was not. Both rulings
look right and they point in opposite directions. This belongs inside the queued escape reconciliation.

*Flagged:* discharge refs may already record what would distinguish the two senses of *passed*, in which
case Q17–Q18 project existing machinery rather than requiring new. Not checked.

### Q19 — Mechanical retrieval

The index is not the hard part. The trigger is.

> Mechanical delivery means the **act** triggers retrieval, not the actor. If someone must decide to
> look, delivery is judgement-mediated again and Q16's failure modes return.

So position must be **derivable from the act itself**, without the actor stating it. That constrains
what may serve as an axis, and forces a second field on the Q1 gate:

| Axis type | Evaluable at act time by | Delivery available |
|---|---|---|
| Mechanically evaluable | an extractor reading the act | mechanical |
| Judgement evaluable | the actor only | judgement-mediated, with Q16 failure modes |

A decision all of whose axes are mechanically evaluable can be delivered mechanically. One with any
judgement-evaluable axis cannot. That is computable per decision and reportable — capability typing
applied to axes rather than to actors.

**Minimal mechanism, three parts.**

1. **Region predicates as data** — evaluable expressions over named axes, stored on the decision.
2. **A position extractor per act-site** — reads coordinates from the act and stamps each with an as-of
   (Q11).
3. **An evaluator** — takes a position, returns the governing set.

At current ledger scale the evaluator is a linear scan over predicates. Indexing is premature; the
interval-tree and policy-decision-point machinery exists if scale ever demands it.

**Two properties to design in.** The evaluator is **shared with the sweep** — retrieval evaluates at a
point, the sweep evaluates the complement over the space, same predicates. And the output should carry
**unevaluated axes** alongside the governing set, so partial delivery is legible rather than returning a
confident wrong answer.

**Act-sites.** Commit hook, CI, and SARIF ingestion already exist. For an LLM actor the act-site is the
tool call, so the governing set can be injected at call time.

**Primary case (Emil).** The most-used site will be decisions governing code-writing acts. This is also
where judgement-mediated retrieval demonstrably fails, and it matches the worked example the upstream
foundation document already carries.

*Flagged:* "transcriping" in the session; read as code-writing acts generally, covering both generation
and modification. Correct if a narrower sense was meant.

### Q20 — Extraction verified by the actor model (Emil's ruling)

> Apply the actor model to the extraction act itself. Ensure its predicate closes, so mechanical
> verification runs on every retrieval.

This terminates the regress rather than deferring it. The extractor's task is small and its acceptance
predicate closes: does the extracted coordinate match the axis's declared type and range, and does the
act sit there.

**Why it bottoms out at depth one.** The checker is a fixed artefact governing a bounded task, so it
needs no extractor of its own — the position for verifying an extraction *is* the extraction.
Self-supplied ground, no further reading required.

Three consequences:

- **Closure becomes a filing constraint on axes, not a discovered property.** Declaring an axis
  mechanically evaluable is a commitment that its extractor's predicate closes, assertable at authoring
  and checkable in CI. This gives Q19's second field a test rather than a claim.
- **Per-retrieval verification is affordable here, unusually.** Per-act checking is normally the
  expensive option; extraction checks are cheap because the predicate is small and the ground is already
  in hand. Note in the PRD that this does not generalise to other gates.
- **Failure to close is a legitimate outcome, not an error.** It means the axis is judgement-evaluable
  and delivery is judgement-mediated for that decision. The tool reports and escalates; a human or model
  determines why and files a decision. See §1.2.

**What this buys and what it does not.** Mechanical delivery is guaranteed against *extraction failure*
and not against *axis misdefinition* — an extractor that correctly reads a field the axis was never
meant to designate passes every check. That is not a regress but a definitional error, caught by
incidents rather than verification. The PRD must state which of the two it is buying.

### Q23 — The evaluator's output contract (Emil's ruling: natural output)

Q19's evaluator returns, per act:

1. **The governing set** — regions containing the act's position.
2. **Unevaluated axes** — where partial delivery must be legible (per Q19).
3. **The exposure profile** — per governing decision, the drift exposure of the axes connecting it to
   this act, the delivery type of the path, and the age of the readings (Q11).

The argument for (3) being in the contract rather than a separate instrument: the evaluator walks those
paths anyway. The profile is a byproduct of retrieval, not a second computation — refusing to return it
discards information already in hand.

**What the profile supports, and its limit.** It shows where the unresolved share concentrates per
act-site. It cannot show whether that share is being *carried* — high residual means judgement or
escape, and the profile cannot distinguish them (B1, same bundled-residual discipline as Q10: the label
is **unallocated burden**, not capability gap).

**Remedy routing without B1.** What it can distinguish is remedy type, on properties the evaluator
already reads:

| Signal at an act-site | Indicated investment |
|---|---|
| High residual; axes mechanically evaluable; decisions filed | **Delivery** — mechanise retrieval (Q19); governance exists and is not arriving |
| High residual; decisions absent; predicate would close | **Filing** — author the decisions; nothing to deliver yet |
| High residual; predicate does not close | **Capability or selection** — the H3/§5.7 boundary; the only row where training the actor is the answer |

Capability is the *last* resort in the table. This inverts the instinct a burden map feeds — such maps
read naturally as "train people here," and two of three rows say the fix is structural.

**§1.2 applies.** Profiles are computed over declared axes at filed decisions. The worst concentrations
may sit on axes nobody named, and those appear as suspiciously quiet regions. Quiet on this map is
ambiguous between governed-and-boring and invisible.


### Q24 — Predicates as first-class graph citizens (Emil)

The open ones are the important half. A closing predicate could almost stay implicit — executable, its
identity nearly exhausted by its extension. An open predicate cannot be run, so unreified it exists
nowhere: it is the framework's dark matter — the §5.7 residue, the floor, the H3 escalation target, and
the third row of Q23's remedy table are all defined by reference to predicates with no representation in
the graph. Demand cannot be routed to judgement if the thing judgement judges against has no node.

**The node type:**

| Field | Motivated by |
|---|---|
| Closure status — a **map from ground regions to closure status, per arrangement** | closure is relative to arrangement *and* region; a scalar would repeat the store mistake |
| Specification, separate from executability | demonstration transfers spec without closure (§13.8); an open predicate can still be *stated*, which is what makes escalation possible |
| Ground axes the predicate reads | its region of evaluability; extraction requirements (Q19–Q20) |
| What discharges it | checker artefact, named reviewer, accountable principal — the assurance side gets an address |

**Identity and evaluation separated (Emil's car case, corrected in session).** Driving the same road
daily under shifting conditions is one predicate — "safe progress along this road" — evaluated against
different ground per act. Identity lives in the specification; an evaluation is predicate + ground + an
as-of. If shifting conditions made each evaluation a unique predicate, automation would be impossible;
it is possible because the predicate is one and the ground varies. Shared predicate node, evaluations
as dated events. This buys both aggregations: fifty decisions waiting on one open predicate (the
escalation queue's question) and one checker discharging a thousand acts.

**Closure is regional.** The self-driving car closes "safe progress" on dry daylight highways and not in
snow — same predicate, one specification, operationally closed on part of its ground and open on the
rest. The industrial precedent is the **operational design domain**, with its documented failure mode:
acts drifting out of the closure region while the checker keeps returning verdicts. Presumed discharge
(Q18) in its most expensive known form.

**Closure transitions are graph history.** A predicate moving from open to closed — checker written,
drill completed, verifier landed — becomes a dated transition. This is Q3's direction made observable
per-predicate; the maturity-state reading of open ruling 12 practically requires this node type.

**Layer boundary.** Predicates are Layer 1 objects synchronically; closure *transitions* are ledger
history, Layer 2. Same split as position/movement (§9).

**Residual, open:** identity of *informal* predicates — when two judgement criteria are the same
predicate — is settled by the car case for specified predicates only. Unspecified criteria remain hard.


### Q25 — Intent as a filed object (Emil's question)

Q1's diagnostic named the failure case of decisionhood — an artifact with no nameable axis "is a stated
intention, not a decision" — without asking whether the failure case is itself an object. It is, and
it types something every detector in this note has been emitting without a name.

**The gap.** The sweep, the completeness check, failed-to-close extraction, and Q14's revisitation
triggers all end the same way: *report and escalate; a human or model determines why and makes a
decision.* Four instruments emit findings; nothing names what a finding becomes once acknowledged. The
escalation queue has no entry type.

> **An intent is a decision acknowledged as owed and not yet made.**

**Where it buys the most: canon's open remainder.** Capacity-generated escape is closed; the remainder
is the decision *no supplier took up*, diagnosed on five instances and detectable only post-hoc. An
intent with an owner is a supplier assignment filed before the decision exists. No-supplier escape
converts from diagnosis to trackable debt: an act in a region whose intent sits unfilled past its
condition is a *known* failure, attributable before anything breaks. Intent is the governance object
for the half of escape the capacity model does not reach.

**Position in the funnel.** Extends Q3's direction backward one stage:
`uncovered-undeclared → intent (owed; direction stated; possibly pre-axis) → open (region named,
deliberately unresolved) → governed → closed`. Distinct from its neighbours: *open* requires a named
region, intent need not have axes yet; the held-out *goal* construct (§13.6) is claim-side — a value
acts serve — where intent is decision-side, an obligation to resolve; an experiment declaration (Q6)
is an intent whose fulfilment method is observation.

**Three guards, or it is a liability:**

- **Intents never govern.** No resolution, so nothing to retrieve — excluded from governing sets by
  type, visible only in the escalation and exposure channels. An LLM treating a filed intent as
  licence is proxy-authoring failure (§13.10) with paperwork attached.
- **Precedence discipline.** A retro-filed intent — "we always meant to decide that" — launders
  no-supplier escape into managed debt. Same rule as experiments: it counts only if it preceded the
  act.
- **Admission gate.** Minimally an owner and a completion condition (decided, or declared inert, by
  some trigger). The falsifier-and-axis admission pattern a third time: each artifact type admitted
  only with the thing that lets it fail.

Prior art: issue trackers and ADR *proposed* status are intent registers in the wild; the framework's
move is connecting them to decision provenance, which no current tooling does.

*Flagged:* node type versus status on the decision node ("owed") is a real design fork — status is
cheaper; a node carries pre-axis intents the decision schema cannot hold. Belongs in the escape
reconciliation, whose scope now carries retro-filing, undelivered, and intent — see B4.

### Q26 — Ground axes as ontology (Emil)

The axis registry is an ontology, and the tooling already runs one: `product-cli` validates the graph
with SHACL and SPARQL. What Emil noticed is that the machinery adopted for validation is the machinery
the axes want. **This is ground, not claims** — a vocabulary for what a decision is made *on*, not for
what is asserted.

| Coordinate framing | RDF framing |
|---|---|
| axis | property with a range (`governs:domainEntity`, `governs:effectiveFrom`) |
| region | class expression over properties |
| position lookup (Q2, Q19) | SPARQL query over an act's asserted properties |
| linear scan of region predicates | existing engine |

**Subsumption is what the coordinate framing could not say.** Regions over numeric axes are intervals,
but domain axes have hierarchy — a decision on Order governs OrderLine acts, and that inheritance is
what position-lookup missed. Under `subClassOf` the coordinate system carries specificity for free:
"the region containing my position" becomes *which class expressions subsume this act's asserted
type.* Emil's "concepts bound into more specific concepts" is the class hierarchy plus property
restrictions. This is also how the registry is **domain-generic and dives inward**: start at the widest
concept, specialise by restriction, software breaks into regions and regions into regions.

**§1.2 has a name.** The declared-space limit — everything evaluates against the declared coordinate
system, nothing sees outside it — is the **open-world assumption**. An RDF graph never entails what it
does not state; the sweep's blindness to undeclared axes is OWA behaviour. And "close the world where
you sweep" has a decades-old operationalisation: **SHACL** is closed-world validation over an
open-world graph. Declare the shape; completeness is checked *relative to that shape* — the exact
qualifier the sweep's output was told to carry. Q3's inert/open declarations are shape assertions; the
coverage sweep is arguably a SHACL shape run against acts. One is already running.

**Two guards.** RDF/OWL are strong on subsumption and weak on time — validity intervals for triples
are a known gap and Q11's as-of/decay needs it (options: reification, named graphs, RDF-star; none
first-class). And the claim graph is currently a validation target; making it a live retrieval index
brings acts and their properties into it, converting a canon artifact into an operational store — a
scale and layer question, since acts are numerous and Layer 2.

*Flagged:* whether the axis registry *is* the existing product-cli ontology extended with act
properties, or a separate vocabulary that references it, is the design fork the escape
reconciliation, the intent construct, and the retrieval PRD now all wait behind.

### Q27 — Trusted sources: institutional ground given a mechanism (Emil)

Canon has carried this slot empty since the foundation document: *institutional ground — supplied
through rules, conventions, authority, or social practice.* Nothing stood under it. Emil's crocodile
supplies the mechanism.

> Many sources say a crocodile eats meat; we say it is a carnivore, citing the trusted ground the
> decision stood on, without verifying it ourselves.

**It is a supply-form claim.** Verifying "crocodiles eat meat" yourself is occasioned supply.
Accepting it because eight zoology sources agree is standing supply — someone else paid the demand
once and you inherit it. **Trust converts occasioned assurance into standing assurance.** The
accountability-completeness apparatus (upstream §7) applies verbatim: a trusted source is a
*persistent principal* with *stake* and a *record*, and the demand you are not paying was paid by
them. "Trusted" is therefore a governance status, not a belief state — an accountability structure
standing behind ground you did not verify.

**Trust closes predicates you could not otherwise close.** "Is this a carnivore?" is unevaluable over
your own ground; you have never watched a crocodile eat. It is *closed* over trusted ground: the
acceptance procedure is source-consultation, and it terminates. This is operational closure as canon
defines it, with source-consultation admitted as an execution path. It is also why Q26's registry can
be generic and dive inward: the generic layers *are* consensus regions — carnivore, entity,
transaction — where trust is broad and cheap; specificity is bought by narrower, costlier sources.
Wide trust wide, narrow trust narrow. SDP again, seen from the source side.

**Trusted ground drifts at the source's rate, three ways.** Q12 said provenance sets the drift
scaling. Trusted ground has three generators and only one is the source's own:

| Generator | Example | Note |
|---|---|---|
| The source's ground moves | taxonomy revised | ordinary drift |
| The source's *trust status* moves | source discredited | one event invalidates every inference standing on it |
| Inference propagation | a derived decision inherits the source's as-of, not the derivation's | `derived_at` is not `valid_as_of` — the trap |

The third generalises Q11: every inference carries the *oldest as-of of its sources* — the
worst-aged-coordinate rule, now with a source dimension.

**Trust is a decision and must be filed.** Otherwise it is escape with extra steps — a governing
decision (*rely on X for Y*) nobody wrote down. Assurance-side anatomy: an inference over trusted
ground has **no gate of its own**; its assurance is entirely inherited from the trust decision. So a
trust decision that is undelivered or superseded silently invalidates every inference standing on it,
and nothing fires — the source keeps looking authoritative in the artefact. Presumed discharge (Q18)
transposed to the ground layer. It is exactly why the human version fails as it does: we know the
crocodile is a carnivore; we do not know we stand on eight sources unchecked since school.

**Filing shape.** `institutional` becomes a first-class provenance value with a *trust decision* as
its required backing — a decision node whose region is "ground of type Y from source X," and whose
Q1 axis-naming is precisely the specification of what is trusted for what. The admission-gate pattern
a fourth time.

**Prior art, one line each.** PROV-O is this — `wasDerivedFrom`, `wasAttributedTo`, agent, entity —
RDF-native, W3C-recommended, and it plugs into the SHACL/SPARQL stack already in use. Named graphs
carry per-source provenance without polluting the assertions.

**Amendment (revision 13): triangulation and independence.** Many sources, one reading — the crocodile
proper. It buys assurance **only to the extent the sources are independent**, and independence is
itself a claim about the sources' provenance graph. Eight citations of one Victorian naturalist are one
source *presenting as eight*; that is Q17's correlated failure on the assurance side, and it is the
escape channel that survives triangulation. Payoff: PROV-O answers "do these derive from a common
root" as a graph query, so "how many sources agree" converts to "how many independent roots agree" —
the second is what raises assurance, and it is read off `wasDerivedFrom` chains rather than asserted.
Two limits: triangulation raises assurance *within closure* and never closes an open predicate (eight
sources agreeing an architecture is good do not make maintainability evaluable); and it yields
assurance without a principal — six people saying the ice held is evidence, and none bears your
consequences. Assurance and accountability stay separate axes. *Independence* becomes a required field
on triangulated readings.

*Flagged:* "how the human mind works" is the register caution — the mechanism claim is
arrangement-general and files as such; the cognitive reading (testimony, epistemic dependence, source
monitoring) is a large literature the framework does not need to enter. Independence-checking over
provenance graphs has treatments in evidence synthesis and source criticism, unchecked.


### Q28 — Projections typed by function and by receiving arrangement (Emil)

Papers, the primer, the generated website, and now the evaluator's output have all been "projections"
without distinction. Emil's split names two functions and a second axis, and Event Modeling's read
model is the specimen that makes it click.

**Function axis.**

| Type | Function | Consumer | Shape | Fidelity criterion |
|---|---|---|---|---|
| **Ground projection** | expose which decisions govern a region | an actor orienting — deciding what to decide | wide; region-scoped; slow to change | completeness relative to the region |
| **Act projection** | deliver the governing set to a specific act | an actor mid-act | narrow; position-scoped; per act; disposable | precision — §7.1's retrieval-under-act-conditions criterion |

Different fidelity criteria are the strongest sign these are two objects and not a spectrum. So is
node admission: an intent (Q25) or an open predicate (Q24) belongs in a ground projection so an actor
knows what is owed, and must be **excluded** from an act projection because it never governs.

Q19's evaluator output *is* an act projection — the delivery mechanism has been building them all
week without the name. Position and as-of decide the type: ground projections tolerate hours of
staleness; an act projection's as-of is the act's. Mechanisable check: a projection whose consumers
are all mid-act but whose scope is a whole region is the wrong type for its use — the policy document
handed to someone mid-task.

**"Never a separate content source" sharpens.** Both types generate from the graph; neither authors.
But ground projections generate ahead of time from region (the CI/website case, which is what the
standing position was stated for) and act projections generate at act time from position (runtime,
never CI). The principle was stated for one of two cases.

**Receiving-arrangement axis (Emil: actor class with the decision's ground has an impact on the
projection).** Q16 typed delivery by mechanism only. Delivery also has a **form**, and the form is
determined by the arrangement receiving it: the same governing set reaches a person as prose, a bound
model as prompt content, a compiler as a schema. Three shapes, one graph. The graph is source and
**every consumer-facing form is derived, and derivation is parameterised by the arrangement.**

Actor arrangement is projection-relevant exactly to the extent that capability differs — the content
delivered is the same across arrangements (demand is fixed by the task); what changes is what the
arrangement can absorb from a given form, which is `I(V;E)`. Blueprint density calibrated for "a
competent developer" is projection form tuned to one arrangement's `E`; the agent-density question was
never a hunch about model quality but a projection-form problem. Fidelity per arrangement is
measurable in principle — comprehension under act conditions for a person, proxy fidelity (§13.10)
for a bound model, exact evaluability for a checker — and the bound-model case is runnable today.

**Fourth delivery-failure mode.** Beside not-retrieved, misapplied, and undelivered: **delivered in a
form the arrangement cannot absorb** — arrived, not absorbed. A schema to a person; a policy PDF to a
compiler. Not retrieval failure; presents as compliance.

*Guard:* projection form is a function of *the arrangement's encoding*, not of an actor class.
Class labels are shorthand until two arrangements of one class absorb differently — which the agent
case produces immediately, since two models with different tool access are two arrangements.
Reintroducing "human/model/program" here would be the species framing §2.3 removed.

**Adversarial instance — sales, and Emil's ruling that trust plus poisoned ground covers it.** A
seller emits ground projections into a buyer's ground, tuned to the buyer's arrangement, so that the
buyer's proxy predicate returns *buy*. That is Q27's trust mechanism with the direction of interest
reversed — engineered standing supply of the seller's claims without paying the verification demand
displaced — combined with Q12's poisoning generator run by a legitimate participant, feeding §13.10's
proxy authoring over curated ground. Segmentation is form-tuning by receiving arrangement, discovered
empirically before this note named it; content authored for a bound model's retrieval is the fourth
failure mode weaponised. The framework's line between legitimate and manufactured is precise and
non-moral: **whether the accountability structure behind the ground is complete** — a seller bearing
stake and sanction is a trusted source; one who does not is manufacturing ground the buyer treats as
trusted with no node behind it. Presumed discharge on the source side. **Ruled: no new vocabulary.**
Coverage without a new term is the finding; the rest is inferable from Q27 and Q12.

**Documentation is the indexed case (Emil).** Documentation has always been actor-specific ground
projection; what the two axes add is an **index**. The set of decisions in scope, crossed with the
arrangements that will act on them, yields the projection matrix — which cells are needed, and which
are missing. Documentation coverage becomes computable the same way decision coverage did: the sweep,
one layer up, run over projections instead of regions.

This reframes documentation debt precisely. It was never "not enough written"; it is *an arrangement
acting on decisions with no projection in a form it can absorb* — the fourth failure mode as a
coverage gap. And it explains why documentation always felt like the wrong artifact type: it was
authored as a separate content source, aged independently of the decisions it described, and could
not be indexed because nothing declared what it projected or for whom. Under this reading
documentation is a **generated cell, not a written thing.**

Two guards, both already earned: the matrix's receiving axis is arrangement, not class (a wrong
granularity is now a diagnosis rather than a hunch); and a cell can be **present and stale** — a
filled cell whose source decisions have moved is presumed discharge in documentation form, which is
the failure everyone experiences with documentation, and why derivation-not-hand-refresh is what makes
the matrix trustworthy.

*Flagged:* the projection matrix may be the demand map §9 was hunting for, arrived at from the
consumer side — projections needed per arrangement per decision set. First time in this note the map
has fallen out of a construction rather than been reached for. Whether it is the map wanted is a
ruling.

Prior art: Event Modeling's read-model discipline — one per act-site, generated, never hand-authored
— is the strongest available precedent for act projections specifically.


### Q29 — Describing an arrangement for projection derivation (Emil's question, redirected)

Emil asked what parameters make up an actor. The picture was unclear because the object was wrong:
the foundation document removed the actor as the unit of comparison (§2.3 — the same model, program,
or human behaves differently across arrangements). A parameter list *for an actor* is the species
framing arriving as a schema, and it is the third time this week the instinct surfaced (capacity,
capability, projection class). Ask **what parameters of an arrangement are projection-relevant** and
it gets clear fast — and the set is small, because only what changes how a governing set should be
shaped for delivery matters.

| Parameter | Determines about the projection | Already in the note as |
|---|---|---|
| **Encoding** — carried before the act | what can be omitted; density | `I(V;E)`; capability §13.7 |
| **Absorbable forms** — channels governance can arrive through | which form to emit; whether mechanical delivery is available | Q28 fourth failure mode |
| **Ground channels** — axes readable at act time | which coordinates it resolves vs. needs pre-resolved | Q19 evaluability |
| **Capacity** — resolve budget per act | how much residual can be handed over | `C_resolve` (core/11, ratified) |
| **Assurance available** — which outputs are gated | which decisions need criterion vs. constraint form | source/assurance split |
| **Trust posture** — sources accepted as standing | how much ground can be supplied by citation | Q27 |
| **Accountable principal** | whether it can receive delegated judgement at all | upstream §7 |

Six of seven are ratified or near-ratified. The schema was mostly written; it was not collected.

**Shape (Emil's ruling pending):** a *profile* record, or a *class hierarchy* in the Q26 ontology —
"bound model with repo access" as a subclass of "bound model," inheriting most fields, overriding two.
The hierarchy fits the dive-inward instinct, keeps class labels as legitimate coarse nodes rather than
a rival framing, and makes "two arrangements of one class that absorb differently" a subclass split
instead of a contradiction.

**Encoding is estimated behaviourally for every arrangement, and humans make that unavoidable.** The
schema field for a human arrangement is not *encoding* but **encoding-proxy, with the proxy named** —
credentials, role, tenure, track record. That is §3.3's principal-level commitment (constraint through
selection and qualification), and canon's "where you cannot check the work, check the worker" applied
to `I(V;E)`. The model-side proxy is a benchmark score or capability envelope — **benchmarks-as-
licences (Wave 2) is this observation from the model side**; the mechanism existed and was not unified
with the human case.

Three things about proxies, all already booked:

- **They decay both ways.** A credential ages against its holder; the task's demand moves under a
  stable proxy — Q21's decay-of-relevance under a pin. Human-arrangement descriptions have a drift
  rate, so Q28's projection matrix goes stale on the arrangement axis too.
- **They are ground, so poisoning applies.** Credentials can be manufactured; self-report is Q12's
  poisoning generator with the actor as poisoner. This is why proxies for humans are institutionally
  issued: the accountability structure behind a licence is what makes it a *trusted source* about
  encoding in Q27's sense. A CV is unsupported ground; a licence is trusted ground with a principal.
- **The proxy is for the derivation, not the audit.** It shapes projection form ahead of time. Once
  acts flow, §13.10's emitted-proxy-versus-delivered-set comparison measures actual absorption per
  act, for any arrangement. **The encoding-proxy is a prior; the act stream is the update.** Human
  arrangements start with credentials and converge on measured behaviour, exactly as a bound model
  does — same object, and calibration closes the gap.

**Self-assessment questionnaires (Emil).** An encoding-proxy sourced from the arrangement being
described. Two problems, separable: it is uninstrumented self-report from a source with the strongest
reason to shape the answer *and* no inspectable access to its own encoding (§13.7's opacity holds for
the person filling in the form); and it is a proxy **never checked against acts** — no calibration
loop, no stake, no update. Presumed discharge in HR form: the form exists, the answers look
authoritative, the ground was never rechecked. The fix is not a better questionnaire; it is treating
the questionnaire as the prior and the act stream as the update — the calibration ledger with human
arrangements as a customer. Under the Q11 amendment it needs no verdict about competence: it is a
low-assurance reading, fine for low-α acts, a fault feeding high-α ones.

**Register guard, stated plainly because it will be misread.** The schema describes *arrangements*; a
person is one component; the estimate attaches to the arrangement. It estimates what an arrangement
carries before an act, for the purpose of shaping what is handed to it. Read as a rating of a person,
it has been repurposed into something the framework did not build and does not stand behind.

*Flagged:* the calibration ledger and the parked actor-capacity model now share this customer — the
overlap between them recorded as an open question elsewhere. The human-arrangement case may be what
forces that overlap to resolve. And the calibration ledger, queued behind capacity scoping, has gained
a second customer.


### Q30 — "Ground registry" as the term, and projection-as-source as the diagnostic (Emil, from the G-track PRD)

Two rulings from PRD work, both the same shape at different scales, recorded here because the second
is a term proposed for canon and the shape is a diagnostic worth carrying.

**A codebase is a projection of the domain, not its authority.** The domain is the decisions that came
before — most unfiled, some escaped. Extraction recovers *evidence* of those decisions from a
projection; it does not recover the decisions. Asking which repo is authoritative is asking which
shadow is the object. Consequence in the PRD: a shared-domain ontology recovered from several
codebases is the **retro-filed decision set** the extractions are evidence for (§13.4 fields apply),
with `wasAttributedTo` on the ratification, not the extraction; and a divergent fourth codebase raises
a delivery question, not an authority question.

**"Domain" is a lacking term.** It arrived from Evans and names the business-problem vocabulary a piece
of software addresses. What the ontology reaches for is the organisation's **ground registry**: the
full set of declared axes across all §13.9 layers — domain, technical, organisational, regulatory —
plus the decisions that region them and the trust decisions (Q27) that let ground be supplied by
citation. Software's domain is one ground projection of the registry; it stood in for the whole only
because it is the layer extractable from code. **Proposed canon term: ground registry**, with the
software layer as the first populated. Register guard, because the word will travel: the defensible
claim is not reach but structure — *the registry is regioned by decisions*, which is what enterprise
knowledge graphs lacked; they modelled entities without modelling who decided anything about them.
Lead with the graph.

**The diagnostic.** Both errors were a projection standing in for its source — repo for domain, domain
for registry — and both were caught by Q28's typing, which names what a thing is a projection *of*.
This joins "is this attaching to the wrong object" (revision 13 note) as the note's most reliable
detector, and it is the "never a separate content source" principle applied to the framework's own
tooling. Any artifact proposed as a source should be asked what it projects; if there is an answer,
it is not the source.

**Extractor limit named as §1.2.** A code extractor bootstraps exactly one layer of the registry and is
silent about every layer that has no projection in code. Decisions that never reached software are not
*unfiled*; they are invisible to that instrument. Stated in the PRD so a G0 result is not read as
populating "the domain."


### Q31 — Event sourcing as the data-layer instance of authority/projection (Emil)

**The observation.** SQL migration was always painful for a structural reason, not an operational one:
a state store's current state is a projection whose source was discarded. Ask what the state projects
(Q30's diagnostic): the history of writes. The writes were folded into state and thrown away, so the
projection was forced to serve as authority, and every migration since has been hand-patching a
projection with nothing to re-derive from — a hand-patched projection is one whose source ref is a
lie, compounded per migration, lossy wherever old-schema → new-schema is not information-preserving.
The loss is silent: presumed discharge (Q18) in data form. The migration ran green; what the store can
no longer answer is invisible.

**Event sourcing is the split done correctly for data.** Events are the acts (the EM reading: events
are the reason ground at t₁ differs from t₀); state is a fold; "migration" dissolves into
**re-projection** — write a new projector, replay the ledger. Putting old data into current ground has
a mechanism because the events were recorded at their as-of under the ground of their time, and a new
projection re-reads them under current ground. Without the events that re-reading is impossible *in
principle*, not merely inconvenient.

**Convergence noted.** The framework independently arrived at this discipline everywhere it stores
anything: supersession-never-rewriting is event sourcing for canon; the registry repo is append-only
history with rebuildable endpoints; the act log is an event stream; the L-track ledger is
content-hashed decisions. One principle: **anything that cannot be rebuilt from retained acts is a
projection whose authority was destroyed.**

**Raw events are the ledger; mapped events are proxies frozen into storage.** The old raw-versus-mapped
argument was miscast as cost when it was type. A mapped event is someone's per-act proxy (§13.10) —
which fields mattered, that day's schema, that day's idea of relevance — baked in, its omissions
invisible because dropped fields leave no gap. Raw events carry information nobody had yet decided was
relevant: the only hedge against future ground that exists. Precisions: **raw means at the trust
boundary, as received** — raw relative to the arrangement; upstream there is always another mapping.
And the winning position is not "don't map" but **map freely; maps are rebuildable projections, cheap
precisely because the raw ledger makes them disposable.** Keeping only the mapped version does not
even save the mapping cost — it makes the first mapping permanent and every later one impossible.

**Discard, corrected (Emil, against Claude's "discard never").** An unconditional rule was the wrong
type — the framework indexes retention like everything else:

> **Discard is a governed act, permitted where the mapping decisions' drift for a specific ground
> version is within τ at α.**

Mechanics: eligibility runs per ground-version cohort (events mapped under G_v become candidates when
G_v is closed — superseded, frozen, no longer subject to reinterpretation demands inside declared α);
retention policy becomes filed decisions with regions rather than blanket durations, which gives
GDPR-driven deletion a principled home (a discard decision with the regulation as its ground); and
**discard carries the highest α in the arrangement, because it is the one irreversible act** — every
other act is re-derivable from retained sources; discard destroys re-derivability itself. Low-α
eyeball assessments of "we'll never need that" are exactly the readings this act may not stand on.
Under Q4's carve, a question arriving after a properly filed discard is **accepted risk realising —
the arrangement working, not an incident.**

**Falsifiers.** For the ledger claim: a case where re-projection from retained raw events failed to
answer a question the mapped store could. For the discard rule: a discard filed within declared τ/α
followed by a question *inside the declared region* the mapped store cannot answer — which falsifies
the drift-assessment method, not the rule.

### Q32 — Constructive versus verification closure (from the G-track PRD)

Canon retired "closed predicates make intelligence unnecessary" because verification-closure does not
make generation cheap. The G-track extraction work surfaced a class that sidesteps the retirement
rather than trips it:

> A predicate is **constructively closed** when the verdict is *computed* by rule — there is no
> candidate-generation step to price. It is **verification closed** when acceptance is mechanically
> checkable but candidates must be searched for.

The distinction is the crisp answer to "when is a model needed at all": never for constructively
closed work (extraction, ETL transforms, entailment — rule-derived, rung zero); for verification-closed
work, only as the generator (the loop's code edits: checked mechanically, searched generatively). It
also names why Rust-class languages fit constructively closed pipelines — representational predicates
close at compile time — while generation-heavy work is indifferent to them.

*Flagged:* this may be a refinement of Q24's closure map (a third value on closure status) rather than
a standalone construct, and it bears on the measure paper's boundary vocabulary — where the predicate
is constructively closed, H(V) is not only defined but *computed*, which is a stronger state than the
paper currently distinguishes. Filing location is Emil's.


### Q33 — Demand discharge: the movement filed as core (Emil's ruling: some of this is canon)

**Emil's originating move.** Demand is a pull: software projects toward decisions because decisions
have demand; projection is placing decisions on the ground and then supplying the demand. Company
artefacts are the same shape one layer up — a product is a projection of a demand claim, exercising
acts supply verdicts, and status records verdicts priced.

**What is canon-grade, and why the path differs from Q1–Q24.** The core statements are **derivable
from ratified canon**, not new observations: they need a derivation check, not a corpus. That is a
higher-grade basis than the vocabulary additions carried, and the right epistemics for core
material.

Three candidate upstream filings, drafted:

| # | Statement | Derivation | Falsifier |
|---|---|---|---|
| A | **Supply-mode exhaustiveness.** At every act within a task's scope, the act's determination demand is discharged — by a filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw. Escape is a supply mode, not an absence of supply. | `term:escape` ("decided by nobody — something still happens") + the luck ruling (a verdict drawn from a distribution the arrangement does not control is still a drawn verdict) | An act exhibiting a fifth supply mode unclassifiable as the four; or an act completing with an outcome-relevant alternative resolved by nothing at all |
| B | **Discharge is act-indexed.** Standing supply is inherited per act; occasioned supply is produced per act; there is no act-free discharge. Governance never chooses *whether* demand is supplied — only *by what*, chosen in advance or defaulted at the act. | The act as unit of account (founding premise) + the standing/occasioned split | Demand shown to be consumed absent any act |
| C | **Discharge is distribution-weighted.** Demand comes due where acts concentrate, at the rate the ground distribution supplies them. | The measure's `P` | *Flagged as possibly a projection of the measure rather than a new claim* — if so it files as exposition, not as a claim, and the flag is the finding |

**What stays prose, deliberately.** The force metaphor (motivation, not filing — §3.1 discipline);
firefighting as ungoverned discharge observed (practitioner material; also the best pitch Q23's
exposure map has — *a forecast of where the pull will drag people*); and the company recursion —
products as demand claims, MVPs as cheapest exercising projections, pivots as supersession,
**status inflation** as the named failure mode (a demand claim filed at *projected* and spent
against as if *ratified*, with no exercising act — the retro-filing laundering at the business
layer). Status inflation joins Goodhart in the projection layer's failure modes. The one-question
instrument: *what would convince you the demand is not there?* Silence is the finding.

**Routing (amended at revision 18 — Emil: demand × act is measure-paper material; the routing
splits).** NOT into the earned vocabulary-and-delivery session — core-ness is not priced-ness, and
the earning discipline holds only if scope stays equal to evidence.

- **Statement A** (supply-mode exhaustiveness) is principle-layer: Wave 3 upstream, projected into
  **Paper A**, where "demand is never unmet, only ungoverned" is arguably the central sentence.
- **Statements B and C, plus the aggregation results**, are **measure-paper material** — they have
  formal content the principle layer cannot hold: aggregate discharge `N·H(V)` over N acts; the
  correlation inequality `H(V₁…V_N) ≤ N·H(V)` (equality iff acts independent — the formal statement
  of why caching, memoisation, and batch decisions work: inter-act redundancy exploitation); and
  the bit-accounting asymmetry that gives "paid once, inherited per run" its theorem — standing
  supply discharges `N·I(V;X)` bits from one authored artifact where occasioned supply produces
  `N·H(V|X)` fresh determinations. O(1) authoring against O(N) discharge, stated loss-blind, inside
  the paper's own register. The economic crossover (the N* where authoring pays for itself) needs
  prices and is **projection-layer** — consulting material, kept out of the paper by the paper's
  own discipline.
- **Sequencing:** papers project canon, so the discharge section cannot be written until its
  claims exist in the graph. Order: the earned vocabulary session (unchanged), then B/C filed
  upstream with Wave 3, then a paper session adding the discharge section as a projection. The
  paper does not move in the queue; it gains a **booked section waiting on its claims** — and it
  is the second honest filler to appear against the paper's ~700-word gap (the first was the
  chained-seams worked example), this one new formal content rather than more of the same kind.
- **The bridge note:** core/11's soft-capacity bound already relates demand rate to `C_resolve`;
  the discharge section is the currently-missing prose bridge between the measure and the capacity
  result.

Upstream's constitutional rarity (four decisions in fourteen months) is the bar working;
derivation-based claims are what clears it.

**Sharpenings recorded from the session.** *Demand is never unmet, only ungoverned* is the compact
form of A+B and the fileable sentence. *Status is not the verdict — status is the record of
verdicts priced* keeps the market's per-act verdicts apart from the ratifier's status acts. The
corpus test was itself this machinery run reflexively: the vocabulary was a demand claim at
projected, the test was the exercising act, the Gate 4 ruling moved status.

---

## 5. Falsifiers

| Item | What would falsify it |
|---|---|
| Q1 axis gate | A meaningful fraction of existing ratified decision files cannot name a ground axis, *and* reading them shows no defect. |
| Q2 region retrieval | Governing-set selection by position diverges materially from expert hand-selection on a corpus of acts. |
| Q8 sweep | It cannot recover findings a decision-table or policy completeness checker produces on the same input. |
| Q9 demand weighting | Entropy-ranked gaps and usage-mass-ranked gaps produce the same ordering across cases. Then the weighting adds nothing. |
| Q4 incident definition | Applied retrospectively to an incident log, it classifies accepted-risk realisations as incidents. |
| Q6 exploration carve | Experiment declarations are routinely filed post-hoc in practice. Then the constraint is unenforceable. |
| Q11 as-of | Worst-aged-coordinate age fails to correlate with any observed act-time failure across a corpus. |
| Q14 reading-triggered revisitation | Ground-assumption divergence at read time fires no more precisely than calendar cadence. |
| Q15 filing-is-not-encoding | Ledger-counted and delivery-counted store allocation agree across a corpus. Then the distinction has no extension. |
| Q17 assurance asymmetry | Mechanising checks while leaving retrieval to judgement does *not* outperform the reverse, content held constant. |
| Q19 mechanical retrieval | Position derived by extractor diverges from position an expert assigns to the same act, across a corpus of act-sites. |
| Q20 extraction verification | Extraction predicates that pass verification are found, on audit, to place acts in the wrong region at a rate comparable to unverified extraction. |
| Q21 pinning | Pinned axes show as-of-related failures at a rate comparable to unpinned ones. Then pinning is not removing the decay. |
| Q22 interval as exposure | Commits-to-touched-paths since branch predicts post-merge defect rate no better than elapsed days. Then the rate parameter adds nothing over the heuristic. |
| Q23 exposure profile | Remedy routing by the three-row table misdirects investment on audited cases — e.g. mechanising delivery where the actual gap was filing. |
| §13.9 SDP-as-drift | Declared layerings and measured co-drift orderings agree everywhere checked. Then the differential is empty and the translation adds nothing over doctrine. |
| Q24 predicate nodes | Aggregation queries (decisions waiting on one open predicate; one checker discharging many acts) turn out unanswerable under identity-by-specification on real ledger data. |
| §13.10 proxy pipeline | Emitted proxies from LLM act-sites honour undelivered constraints as often as delivered ones. Then delivery does not bound proxy fidelity and the ceiling claim is wrong. |
| Q25 intent | Filed intents with owners and conditions show no better no-supplier-escape detection than an unfiled backlog on audited cases. Then intent is bookkeeping, not governance. |
| Q26 ontology | Region-as-class-expression retrieval fails to return governing sets that hand-selection returns, on the corpus — or subsumption returns governing decisions an expert rejects as not applying. |
| Q27 trusted sources | Inferences over filed trust decisions decay at the derivation's as-of rather than the source's, on audit — or trust-status revocation fails to propagate to standing inferences. Then the mechanism does not track what it claims. |
| Q28 projection types | An existing projection is found genuinely mixed — region-scoped and consumed mid-act with no fidelity penalty — or the same governing set in two forms shows no absorption difference across arrangements with different `I(V;E)`. Then function or form is not a real axis. |
| Q29 arrangement schema | Projection forms derived from the seven-parameter profile absorb no better than a single generic form, measured by proxy fidelity across arrangements. Then the parameters are not projection-relevant. |
| Q11 amendment (assurance-on-reading) | Acts whose reading-assurance is below their α show no elevated failure rate versus matched acts. Then the mismatch is not a fault class. |
| Q27 amendment (independence) | Readings triangulated from provenance-independent roots show no higher accuracy than readings from correlated roots at equal source count. Then independence is not what raises assurance. |
| Q30 ground registry | Filed decisions found regioning ground that no declared layer holds — then the layer set is incomplete and "registry" is claiming a scope it does not have; or the software layer, once populated, is found to be the *whole* registry in practice, in which case "domain" was sufficient and the term adds nothing. |
| Q31 raw ledger / discard | Ledger claim: re-projection from retained raw events fails to answer a question the mapped store answers. Discard rule: a filed discard within declared bounds is followed by an in-region question the mapped store cannot answer — falsifying the drift assessment, not the rule. |
| Q32 constructive closure | A constructively closed task is found whose rule set's authoring cost behaves like search — i.e. the generation step was relocated into rule-writing rather than removed. Then the class is verification closure with the search paid earlier, and the distinction collapses. |
| Q10 positional view | Was booked unfalsifiable pending B1; the capacity model is ratified, so the falsifier is now statable: on acts where the actor-indexed conjunct is defined, regions labelled *unallocated* that core/11's machinery classifies as carried-judgement at a rate indistinguishable from chance would show the label is hiding available information. |

---

## 6. Open rulings — Emil's

None should be settled by Claude.

1. **Do tier 2 incidents survive as a category**, or fold into the sweep as "uncovered region, observed
   traffic"?
2. **Do *inert* and *open* collapse** into one construct with two values? *(Corpus evidence,
    2026-08-14: `open` was exercised twice and its distinctive features did real work — horizon,
    owner, observation; `inert` appeared zero times in 11 rows. One half of the pair does all the
    observed work; the collapse is unsettled by this corpus.)*
3. **Is "axis" one term or two?** The coordinate named at authoring, and the thing a tier 1 incident
   yields, may not be the same object. Emil: might differ, not determinable yet. Parked deliberately.
4. **Is a bound-finding experiment its own object**, or is "amendable" doing double duty in Q7?
5. **Are the four states ordinal**, or is `I(V;X)/H(V)` the only real ordering? Emil: a feedback loop
   with backward jumps, so direction survives as a gradient rather than a sequence.
6. **Is "high demand, low coverage" a new claim or a projection** of the existing escape definition with
   a measure attached?
7. **Does the maturation correspondence** (§9) help the upstream diachronic carve or contaminate it?
8. **Does `revisit_if` collapse into a declared tolerance on a ground assumption** (Q14), or remain an
   edge type?
9. **Is *undelivered* a generator of escape or a sibling class?** (Q18.) Points opposite to the Q12
   ruling. Belongs in the escape reconciliation.
10. **Do discharge refs already distinguish the two senses of *passed*?** Determines whether Q17–Q18
    project or introduce.
11. **Does the mechanically-evaluable flag belong on the axis or on the decision?** An axis may be
    extractable at one act-site and not another, in which case delivery type is a property of the pair
    rather than of either.
12. **Is a judgement-evaluable axis a permanent type or a maturity state?** If extractors can be
    written later, the flag is a position on the Q3 direction rather than a fixed classification.
    *(Corpus evidence: the register contains a matched pair five weeks apart — DDD-dec-02's
    `reviewTrigger` with a judgement-read tolerance, and no-unwrap's hash-pinned mechanically
    evaluable `revisit_if` in the same slot. An axis made the transition, with dates. Points to
    maturity state.)*
13. **Do extractors require their own decision files?** Q20 makes extraction an act; whether it is a
    governed act with a filed decision or a fixed artefact outside the ledger is unsettled.
14. **Do regulation and constraint need separate terms** (Q21), or is one a special case of the other
    with a sensing loop attached?
15. **Is decay-of-relevance under pinning a third class**, or does it fold cleanly into supersession as
    Q21 currently assumes?
16. **Are the three B1-reducing constructs one account or three?** Shared budget (§7.3), capability
    membership (§13.7), and the disposition framing (§13.1) each arrived independently and each felt
    like progress. **Reframed at revision 9:** canon has partially ruled — capacity-generated escape
    and the no-supplier remainder come apart on five diagnosed instances (DDD-floor-01), so a
    capacity-shaped account and a membership-shaped account are already separated in canon. The
    corpus question is now narrower: do the specimens agree with that separation, and does the
    disposition framing add anything over the two canon accounts? Two standing disciplines from the
    B1 note bind the corpus session: where the actor-indexed conjunct ("no verifier the actor
    holds") is undefined because no actor was assigned, record *undefined* as a datum rather than
    forcing a classification; and specimens resembling an empty option set flag against the
    UNVERIFIED empty-option-set generator rather than being assigned to the nearer account.
    *(Corpus outcome, 2026-08-14: across 11 expressions and 7 gates, no classification invoked a
    magnitude — presence/arrival objects carried everything. The membership-style account sufficed;
    the budget was never needed. Ruled consequence: the capacity scoping session regenerates
    smaller, citing the table.)*
17. **Is `I(V;E)` the internalised store?** If the actor's encoding in the measure has been the
    internal location all along, external standing supply is a different conditioning variable, and
    §13.7 is a clarification of existing machinery rather than a construct. Step 1 should show it.
    *(Corpus evidence: thin, honestly. The split surfaced operationally as delivery-failure-mode
    present versus absent — row 11's nothing-to-deliver against rows 1–10's artefacts. Whether
    `I(V;E)` is the formal home did not arise in expression work.)*
18. **Does the goal construct stay out?** §13.6 holds it out pending the corpus test; if existing
    decisions do not express without it, that position reverses.
19. **Are registries-by-drift a construct or the N*-split machinery applied to axis authoring?**
20. **Three drift rates need names** (§13.9 flag) — ground-value, axis-registry, referent-under-pin.
    Whether they are three terms or one term with a qualifier is a vocabulary ruling.
21. **Is the predicate node shared with identity-by-specification** (Q24, answered for specified
    predicates by the car case), and what settles identity for informal, unspecified criteria?
22. **Does surfacing authored proxies become a standing obligation on LLM actors** in the arrangement
    (§13.10)? Plausibly the most practically consequential ruling this note has produced.
    *(Corpus evidence, both directions: A-01 Gate 1 is the fidelity ceiling live — an undelivered
    governing input, not improvised from its summary, surfaced and held open. A-01 Gate 5 is the
    over-honouring caution — session-authored criteria the principal never delivered, safe by
    delivery-and-ruling, not by absence. Un-annotated follow-through base rate: 1 in 7 gates, the
    mildest form — the nonzero-but-low condition under which the delivered-vs-emitted check earns
    its keep.)*
23. **Is the per-act proxy the fifth construct** (§13.10), or is it the delivery machinery viewed from
    the act side? The corpus test should distinguish. *(Corpus evidence: authored proxies were
    observed in the wild at real gates — over-honouring criteria, improvised content converted to
    governed objects at a minting gate. The construct has referents; whether it is a fifth construct
    or delivery-from-the-act-side remains Emil's.)*
24. **Intent: node type or status?** (Q25.) Status is cheaper; a node carries pre-axis intents.
25. **Is the axis registry the product-cli ontology extended, or a separate vocabulary referencing
    it?** (Q26.) The fork the reconciliation, intent, and the retrieval PRD wait behind.
26. **Does the escape reconciliation split before it is attempted?** Its scope now carries
    retro-filing, undelivered, intent, and the trust-decision backing. One session may not hold it.
27. **How is trust status itself assured?** (Q27.) A trust decision is filed with a region; what
    gates its supersession when a source is discredited, and who owns the propagation, is unstated.
28. **Two projection types or a spectrum** with region-scoping as the parameter? (Q28.) The
    fidelity-criterion and node-admission differences argue two; the corpus test can ask whether any
    existing projection is genuinely mixed.
29. **Arrangement description: profile record or class hierarchy in the Q26 ontology?** (Q29.)
30. **Is the projection matrix (Q28) the §9 map**, or a different instrument?
31. **Does the calibration ledger absorb the actor-capacity overlap** now that human arrangements are
    a shared customer (Q29)?
32. **"Ground registry" as canon vocabulary** (Q30) — and whether "domain" is retained in Evans's
    sense for the software layer or retired. Freight-list item.
33. **Does Q32 file as a third closure value on Q24's map** or as a standalone construct — and does
    the measure paper's boundary vocabulary gain the computed/checkable distinction?
34. **Where does Q31 file?**
35. **Q33 routing** — *amended at revision 18, per Emil:* the routing splits — A to Paper A via
    Wave 3; B/C plus the aggregation results to the **measure paper** as a booked discharge
    section, claims filed upstream first. Remaining open: whether C is a claim or an exposition of
    the measure, and whether the correlation inequality files as a claim or rides as derivation
    inside the section. It is data-layer vocabulary with an EM bridge (events as acts) and a
    canon convergence (supersession as event sourcing); candidate homes are the downstream repo's
    engineering vocabulary or the EM projection document. The D-track material it surfaced through is
    parked and separate.

---

## 7. Retrieval, capacity, and what was retired

### 7.1 Retrieval under act conditions

Retrieval happens mid-act. Precision matters more than recall there, because a governing set carrying
irrelevance is discarded wholesale rather than filtered. This is what makes Q1 and Q2 load-bearing
rather than convenient.

**On writing things down.** Externalising does not fix this by itself — an unindexed record has the same
precision problem and arguably a worse one, since a large record returns more irrelevance than a small
memory. What externalisation buys is that the **index can be authored separately from the recall**, at a
moment when attention is available to spend on it. This is Q1 from the other end.

**On multitasking.** Held to the narrow version: two acts at different positions need two governing
sets, and retrieval serving one returns noise for the other. The cost is not switching tasks; it is that
position is the retrieval key and only one can be occupied. Predicts that interleaving within a region
is markedly cheaper than across regions, scaling with distance between positions rather than task count.

**On the actor-general failure.** That both humans and models retrieve unreliably is a *derivation*, not
an observation — determination is indexed by arrangement and never by actor species, so difficulty
living in the index predicts shared failure. Scoped: this accounts for one class only, where a decision
was recorded, was relevant, and still was not retrieved. It does not cover unfiled decisions, axes named
but not evaluable at act time, or plain capacity limits. Something explaining all retrieval failure in
both actor types is a frame, not a claim.

*Flagged:* there is a substantial cognitive literature on task-switching cost and external memory in
expert practice, unchecked, plausibly bearing on this directly. The framework-side version — an unnamed
axis makes a filed decision unretrievable — is testable against the ledger without touching cognition.
That is the version to file. The cognitive reading is motivation.

### 7.2 Attention — retired as a term

Claude used *attention* as an actor-general capacity. Withdrawn as equivocation: in a transformer it
names a weighting over a context window with no depletion and no serial bottleneck, which would make the
multitasking argument inapplicable to that arrangement entirely.

Replaced by the weaker and stateable version: **retrieval competes with the act for a finite budget**,
so precision is paid beforehand or not at all. Whether a given arrangement's budget is shared between
holding ground and finding governance is an empirical question about that arrangement, not a definition.
Attention is then the human instantiation, not the general term.

### 7.3 Execution capacity — extends a blocked model

Emil's formulation: execution capacity per actor is what pays for doing, retrieving, or making
decisions.

**Consequence for the blocked work.** The actor-capacity model was booked as needed to cleave judgement
from escape in `H(V|X)` — the point where the residual exceeds what an actor can carry. If retrieval and
authoring draw on the same budget, capacity is consumed by finding governance and by deciding at all,
not only by resolving. Escape can then occur with residual well inside what the actor could have
resolved, because the budget went to retrieval. *(Revision 9: the model is ratified, not blocked — see
B1 as re-booked. This paragraph's claim survives the re-booking but changes status: it is now a
proposed **extension to a landed model** — whether `C_resolve` accounting should include retrieval and
authoring draws — which is a canon amendment question for after the corpus test, not pre-work for a
pending model.)*

Two constraints held:

- **Commensurability is unestablished.** One budget assumes a common unit, and the framework has a unit
  for one draw only — `H(V)`, on closing predicates. Retrieval cost is search over an index; authoring
  cost is prior commitment. One budget versus three trading at a rate is a modelling claim with the same
  status as the demand identification, and should be marked so rather than adopted as structure.
- **Per arrangement, not per actor.** The same model with retrieval and tests is a different capacity
  from the same model without. *Execution capacity per actor* should read *per arrangement*, or it
  reintroduces the species framing removed upstream.

### 7.4 Parked by Emil

The LLM-specific capacity question. Recorded because it bears on 7.3 if resumed:

- Context is simultaneously the ground, the retrieved governance, and the working space for resolving —
  three competing draws sharing one store with no accounting separating them. For this arrangement type
  the three uses are literally one budget, a cleaner case than can be made for a human.
- Context window and network size are separable capacity parameters, correlated in released models
  because both scale with investment, not by mechanism.
- Retrieval quality degrades within the window before it fills, so effective capacity is below nominal
  and position-dependent. A capacity model reading the nominal number would overstate the arrangement.
- Weights and forward pass are stateless, which is why the upstream layer is synchronic. The
  *arrangement* generally is not — this session had memory, tools, and a file. Same weights, different
  capacity.

---

## 8. The cycle, and where it is not closed

Axes make decisions into regions. Regions make retrieval a position lookup. The complement is the
uncovered set. Uncovered ground is entered either declared (exploration) or undeclared (incident). Both
yield axes. New axes widen the space and sharpen retrieval.

Two qualifications on "two ways to the same result":

- **Reachable sets differ.** Exploration bounds its region using axes already held, so it widens
  geometry from the inside. Incidents can arrive from regions the coordinate system has no name for.
- **The cycle is closed but not self-starting.** Tier 1 incidents widen geometry, and by construction
  the sweep cannot detect them. They arrive through a channel outside the mechanism, permanently, not
  just at bootstrap.

---

## 9. Wardley correspondence

Emil's test, adopted: a map requires at least two axes **and a direction**. Ground space has axes and no
direction, so by that bar it was a space, not a map.

**Direction supplied by the sign flip.** Demand converting from occasioned to standing supply applies to
regions, not only components. A region moves `uncovered-undeclared → open → governed → closed predicate`,
relocating demand from per-act resolution to pre-paid. Monotone in intent; regressions named (dependency
drift can stop a predicate closing). Emil: a feedback loop whose deviations are always backward, so
direction survives as a gradient rather than a sequence.

**Two correspondences.** Wardley's evolution axis and the demand-relocation story describe the same
movement — genesis is exploration, commodity is a closed predicate. His practical advice reads as *do
not pay occasioned supply for demand somebody has already converted to standing supply*. Separately, his
value chain is a decomposition and therefore has a seam, making a Wardley chain a candidate object for
the correspondence campaign rather than only an analogy.

**One non-correspondence, load-bearing.** Wardley has exactly two axes, fixed for every map. Ground
space has as many as the task declares, and the exploration/incident cycle exists to discover new ones.
His coordinate system is never widened by observation. A Wardley map sits *inside* this construction as
a two-axis projection chosen for executive legibility, and cannot host the mechanism. The framework can
render a Wardley map; Wardley cannot render the framework.

**Caution on borrowing.** The evolution axis is not measured — position is assigned by practitioner
judgement against cheat-sheet characteristics. One reading: it is a proxy for demand converted from
occasioned to standing supply, in which case the framework has the measure and Wardley has the
intuition.

**Layer consequence.** Direction is diachronic. Position is Layer 1; movement requires the ledger and is
Layer 2. A map, under Emil's definition, cannot be a Layer 1 object, and "map" is ledger vocabulary.

---

## 10. Corrections made during the session

Recorded rather than silently absorbed.

| # | Correction | Origin |
|---|---|---|
| 1 | The luck clause struck from Q4; the test is on the arrangement, not the outcome | Emil |
| 2 | "Incident output is an axis" holds for tier 1 only | Claude |
| 3 | Demand anomaly as a defect signal rejected; the finding is the join of high demand and low coverage | Claude |
| 4 | "The funnel narrows demand" corrected — `H(V)` is fixed, `H(V\|X)` narrows | Claude |
| 5 | Verification is not a third store; it is a gate over one | Claude |
| 6 | Exploration is not governed action; the carve is by authored basis | Claude |
| 7 | Stale ground is not escape; it is ground not as expected at act time | Emil |
| 8 | Decision-to-act is not an interval; that case is supersession | Emil |
| 9 | *Attention* withdrawn as equivocation; replaced by shared finite budget | Claude, prompted by Emil |
| 10 | Revision 1 dated from context rather than from a readable clock | Claude |
| 11 | The blind spot was flagged four times as an instrument caveat; it is one structural property and now sits in §1.2 | Emil |
| 12 | Failure-to-close on extraction is a reportable finding requiring escalation, not a tool error | Emil |
| 13 | Oven and CI build are not one mechanism; regulation and constraint separated | Claude |
| 14 | Four explained practices recorded as coherence, not evidence (§3.1) | Claude |
| 15 | Judgement is not a store; it is a residual, and the object is a graph not a partition | Emil |
| 16 | "No new decisions" replaced by "last decision precedes the act"; the first is not abstraction-stable | Claude |
| 17 | The LLM novelty is a failure surface (silent completion), not a new capability | Claude |
| 18 | Actor count is not two; every link has a filler and fillers vary across the graph | Emil |
| 19 | The map's lens colours edges, not nodes; delivery type is per decision-and-act-site | Claude |
| 20 | Watching does not close the predicate; it transfers the specification, and closure takes calibration | Claude |
| 21 | Supervised learning is not demonstration; it is correction without specification | Claude |
| 22 | The checker-arrival asymmetry is an arrangement property, not a platform property | Claude |
| 23 | "Describe everything" struck; bearer-hood is per-region and the domain-model decision has no bearer | Claude |
| 24 | Act-direction is not SDP's dependency direction; per-act exposure separated from global layering | Claude |
| 25 | Drift-revisitation correlation is plumbing, not theory; the residual is the finding | Claude |
| 26 | Unique-predicate-per-conditions inverted: identity in the specification, ground varies per evaluation | Claude |
| 27 | Satisfaction is not closure; the junction is a closed predicate polling volatile ground | Claude |
| 28 | Authoring does not close a predicate; evaluability is its design constraint | Claude |
| 29 | "Fit the verdict we need" struck as rationalisation; the target is tracking the acceptable region | Claude |
| 30 | "As close to the one we know to be right" corrected: the retrieved context is the specification being approximated | Claude |
| 31 | B1's booking ("unratified, blocked behind §11a–e") was stale-projection drift, not a live blocker; re-booked at revision 9 against verified live canon | canon (DDD-floor-01 notes), via the gate-pass session |
| 32 | Institutional ground carried as an empty provenance slot since the foundation document; mechanism supplied at Q27 | Emil |
| 33 | The escalation queue had no entry type across four detectors; typed at Q25 | Emil, prompted |
| 34 | "Projection" carried two functions and no receiving-arrangement axis; typed at Q28. "Never a separate content source" was stated for one of two cases | Emil |
| 35 | Adversarial ground manufacture proposed as needing vocabulary; ruled covered by Q27 + Q12 | Emil (rejecting Claude's flag) |
| 36 | "Parameters of an actor" redirected to parameters of an arrangement — third occurrence of the species instinct this week | Claude |
| 37 | "How trusted is the ground" as a scalar parameter rejected; assurance-on-reading with per-act mismatch instead | Claude |
| 38 | "Three assurance sources" corrected: one property, one requirement, one ceiling — no third supplier; triangulation proper is many-sources-one-reading and hinges on independence | Claude |
| 39 | PRD asked which repo is authoritative for the domain; a repo is a projection and cannot be | Emil |
| 40 | "Domain" used for what the ontology reaches for; it is one layer of the ground registry | Emil |
| 41 | "Discard never" corrected to a governed act within τ at α per ground-version cohort — an unconditional rule where the framework indexes | Emil |
| 42 | §13.2's binary timing predicate corrected by corpus data: no honest value for open decisions, and it erases the mechanical store's after-position (times resolution-authoring where the store question is determination-supply). Canon's three-way timing is primary; the binary is derived. SR-5 probe, fired on the row selected in advance to fire it | corpus test, Gate 2 ruling |

**On correction 1.** The original clause read "or would have been but for luck." Emil: *luck does not
exist; statistics and probability exist.* The clause tested the wrong object. Correct test: was any
adequate source-and-assurance combination governing this act? If not, the act escaped, whether or not
the verdict was acceptable — the verdict was drawn from a distribution the arrangement did not control.
Two improvements followed. The evidence class widens past failure, so every observed act reports rather
than only the ones that went badly, removing the survivorship structure from the detector. And the
hindsight problem disappears, because the judgement moves from imagining a counterfactual severity to a
ledger lookup.

---

## 11. Blockers

**B1 — judgement/escape split. RE-BOOKED at revision 9; the blocker as originally stated has
cleared.** The original booking — "the actor-capacity model, unratified and blocked behind the §11a–e
upstream collision" — was written against a stale projection. Live canon (verified 2026-08-14, B1
reconciliation note, `meta/b1-reconciliation-2026-08-14.md`) has the capacity model **ratified**:
`term:capacity`, `term:overflow`, `term:escape-mechanism`, `term:p-err` all settled, established by
core/11; DDD-floor-01 at *reported*, changed v5.4; both assets reproduce.

What canon supplies: **capacity-generated escape is closed** — and the mechanism is *sufficient for
escape, not necessary for it* (core/11 §7, DDD-dec-15 scope correction). The escape that overflows
nothing — a governing decision no supplier took up — is diagnosed on **five** instances of ratified
canon (the claim file's count; core/11 §7's prose says four and is the bug, filed as follow-up F4).

B1's residual is three items with three different dispositions, none of which is "unratified" and
none of which is "blocked behind":

| Residual item | Disposition |
|---|---|
| Real-actor calibration | a rig problem, not a ruling |
| Formal write-up | owned by paper-3 |
| Non-capacity remainder | **outside the model by DDD-dec-15** — a scope boundary, not a dependency |

Consequences for this note: where the residual falls inside the capacity model's scope and the
actor-indexed conjunct is defined, the judgement/escape split is *available*, not pending. Q10 and
Q23's **unallocated** label remains correct where the conjunct is undefined (no actor assigned) and
where acts sit in the non-capacity remainder — the label's justification has narrowed from "the model
does not exist" to "the model's scope does not reach here", which is a different and better reason.
The bundled-residual discipline stays; its ground has changed.

**B2 — queue head.** *(Revision 16: discharged twice over. The measure note's related-work debt
shipped 2026-08-14; the corpus test ran the same day and **the additions earned their canon
session** — all four SR-10 criteria met, 11/11 under the fourth value, 91% resolvable axes, median
at the cost bar, 7/7 gates yielding. The queue as ruled at the corpus Gate 4: (1) the
vocabulary-and-delivery canon session — scope **as evidenced, not as dreamed**: Q1 gate, Q3
four-state typing with the —(open) timing value, position/region vocabulary with the 22-axis
registry draft as seed, delivery vocabulary (Q15/Q17/Q18/presumed discharge) absorbing the queued
delivery filings; (2) capacity scoping, regenerated smaller on the question-3 evidence; (3)
freight, now carrying the exhaustiveness/defence-in-depth wording seam; (4) Wave 3. **Q25–Q32
were not priced** — the tested note was the revision-8 copy — and the canon session must not
absorb them by momentum; they wait for their own pricing or ride the reconciliation.)*

**B3 — `term:maturation` escaped seam.** The Wardley/maturation correspondence in §9 touches a term
divergent across both registries pending the upstream diachronic carve. Nothing in §9 files before that
carve resolves.

**B4 — escape reconciliation.** Q12 and Q18 both bear directly on it and point in opposite directions.
They belong inside that session rather than beside it, and it is already ahead of this note in the
queue. *(Revision 10: the session's scope has grown to carry retro-filing (§13.4), undelivered (Q18),
intent (Q25), and the trust-decision backing (Q27). Open ruling 26 asks whether it splits before it is
attempted. Canon's own five-instance diagnosis of no-supplier escape is its opening evidence.)*

---

## 12. Prior art — asserted, not verified

The sweep is not novel. Mature components exist:

| Component | Nearest prior art |
|---|---|
| Name axes, partition each | Category-partition method (Ostrand & Balcer, 1988); input-space partitioning |
| Regions over a factored input space | Equivalence partitioning; combinatorial testing, covering arrays |
| Sweep for uncovered regions | SCR tabular requirements — mechanised completeness and disjointness checks |
| Rules as regions; gaps and shadowing | Firewall rule anomaly detection; DMN decision-table completeness; XACML policy analysis |
| Governance coverage over code | MC-DC and decision coverage under DO-178C |
| Ranking by usage | Musa operational profile |
| Staleness and revalidation | Cache invalidation; TTL and staleness bounds in distributed systems |
| Intent registers | Issue trackers; ADR *proposed* status |
| Axis registry as ontology | RDF/OWL class hierarchies and property restrictions; SHACL as closed-world validation over OWA graphs; SPARQL for position lookup |
| Trusted-source provenance | W3C PROV-O (`wasDerivedFrom`, `wasAttributedTo`); named graphs |
| Act projections | Event Modeling read models — per act-site, generated, never hand-authored |
| Encoding proxies | Credentialing and licensure (human); benchmarks and system cards (model) — unified as benchmarks-as-licences |
| Independence over provenance | Evidence synthesis; source criticism — unchecked for a formal treatment |

Firewall rule analysis is the closest mechanical analogue: rules are hyperrectangles over header
dimensions and gaps are found by taking the complement. The sweep is that, with decisions for rules and
declared ground for header fields.

**Where novelty may sit.** The weighting. Existing methods rank by count, structural coverage, or usage
mass. Verdict entropy comes apart from usage mass in a way that matters: a region can carry most of the
traffic and near-zero demand, because the verdict never varies there. Operational profiling says test
where users go; verdict entropy says govern where the answer moves.

**Confidence.** The classical prior art above is asserted from knowledge with reasonable confidence and
is not searched. Whether information-theoretic weighting of specification coverage gaps has been
published recently is **not** checked, and that is where novelty would live. Emil has not ruled on
running the check. The delivery construct (§4) has not been checked against prior art at all.

**Consequence for related work.** If any of this reaches a paper, the survey burden is against testing
and policy-analysis literature, not information theory — a different survey from the measure note's.

**Implementation path.** Coverage and policy tools emit findings the `ddd` CLI could ingest through
SARIF. Not designed; noted as available.

---

## 13. Synthesis — the model as it now stands

Not a queue item. This section states where the session arrived and what it costs to act on, and it is
the part most likely to be wrong, because it was assembled last and quickly.

### 13.1 What broke

**Judgement was never a store.** `H(V|X)` is defined as a residual — what remains after conditioning.
Naming a remainder as though it were a location produced three stores and a leftover, and the strain
became visible the moment a second question was asked of it, which is what decision retrieval did
(Emil's diagnosis).

**The type was wrong, not the cell.** Stores partition a quantity: no order, no position. Everything
this session produced needs position — retrieval happens at a point, as-of decay measures distance,
delivery is whether an earlier resolution reaches a later act. None of that is expressible over a
partition. The object was a graph being described as a partition.

**Consequence for judgement and escape.** They are not two stores sharing a bucket. They are two
dispositions of unencoded demand, separated by actor capability. *(Revision 9: this was written when
B1 was booked as blocked; the capacity model is in fact ratified in live canon. The disposition
framing is therefore not an anticipation of a pending model but a redescription of a landed one, and
must be read against core/11's actual machinery — where it adds nothing over `term:capacity` and
`term:escape-mechanism`, it is redundant. Ruling 16 as reframed carries the question.)*

### 13.2 What replaces it

| Construct | What it is | Status |
|---|---|---|
| **Graph** | the existing claim/decision graph | unchanged; not a new object |
| **Position** | ground axes make a decision a region; an act has coordinates | Q1, Q2 |
| **Timing** | per decision, relative to an act: is the resolution complete *before* the act, or completed *by* it | new |
| **Delivery** | whether a pre-act resolution reaches the act; mechanical or judgement-mediated | Q15–Q20 |

Allocation stops being a partition of a quantity and becomes a property read off the graph relative to a
given act.

**Timing stated as a predicate, not a category:** *is this decision's resolution complete before the act
begins, or does the act complete it?* Binary, observable, and stable under abstraction change — unlike
"no new decisions occur," which is true of program execution at one abstraction and false at a finer
one. A runtime branch is a resolution whose last decision precedes the act.

**The measure is untouched.** `H(V) = I(V;X) + H(V|X)` was never defined in terms of stores; `X` as an
actor's encoding gives the split directly. Store vocabulary was a projection of the measure, not a
foundation for it. What needs re-deriving is engineering vocabulary. **The measure note ships
unaffected**, which is the load-bearing reassurance here.

### 13.3 Filling, and what is actually new

Links in the graph are filled or empty relative to an act, and empty comes in two kinds: **deliberately
open** (Q3's `open` state — a filled link whose content is *resolve this later*) and **never noticed**.
Identical at act time, different provenance, and only the second is a finding.

**On the LLM claim, narrower than stated in session.** Deferring resolution to act time is ancient —
every operator does it, every runtime branch does it. What is new is that an actor with broad enough
coverage can fill a link *that was never authored*, at act time, without the gap being noticed. Earlier
act-time fillers were either narrow (a branch resolves exactly what it was written to resolve) or
accountable (a person who knows they are deciding). Silent completion is a new **failure surface**, not
a new capability, and it is the source-side twin of presumed discharge.

**Number of actors is not fixed.** Author, extractor, checker, reviewer, and acting party can each fill
different links. What is actor-general is that every link has a filler and fillers vary across the
graph. Fixing the count at two would reintroduce the species framing removed upstream.

**Capability is not filling.** A link's status has at least three values — filled and delivered, filled
and undelivered, empty — and capability speaks to none of them directly. This is the delivery finding
restated at the graph level.

### 13.4 Retro-filing

Adding an escaped decision to the graph once uncovered is the only mechanism that converts a silent
completion into a visible node. Two fields it must carry:

- **When it was uncovered**, distinct from when the act occurred. The gap measures how long the graph
  was wrong.
- **That it was retro-filed.** A node added after the fact has different evidential status from one
  authored before. Without this, retro-filing launders escape into coverage and the sweep begins
  reporting clean.

*Flagged:* retro-filing may be the discharge mechanism for the escape generators rather than a separate
operation. This belongs in the escape reconciliation (B4).

### 13.5 Test-driven development as the timing discipline (Emil)

Written before the code, a test is a resolution complete before the act: the answer exists in the
repository and the act is constrained to satisfy it. Written after, it records a resolution the act
already made. Same artefact, opposite side of the act. TDD's entire discipline is a rule about timing.

This explains why test-after feels different despite producing the same suite. It is not laziness; the
tests cannot constrain what was already decided. It is retro-filing.

Two refinements:

- **Tests are a special case, not the mechanism.** A test states the verdict and verifies it — a fusion
  of source and assurance, which is part of why TDD feels powerful, but it restricts coverage to
  decisions expressible as a checkable assertion over an act's output. Architectural fit, dependency
  choice, and interface shape are resolved before the act and are not testable. TDD is the pre-act
  mechanism **where the predicate closes**; the general case is broader.
- **Retro-filed tests are not worthless.** A test written after passing code pins behaviour against
  future drift though it constrained nothing at the time. That is Q21 pinning, not resolution. If the
  graph marks retro-filed nodes as §13.4 requires, it distinguishes these automatically rather than by
  convention.

**Prediction, and the testable part:** the value of test-first should track how *unresolved* the
decision was, not how complex the code is. Test-first over well-understood behaviour is pinning with
extra steps; over genuinely open behaviour it is the resolution mechanism. This predicts TDD's uneven
empirical record. That literature exists and is unchecked here.

### 13.6 The map, resolved (Emil)

The Wardley hunt (§9) is retired rather than satisfied. The direction was never a coordinate to be
found; it is the edges. The claim/decision graph with declared ground, expressed as a directed graph
toward acts, has direction built in — acts are sinks, and the funnel is the in-degree structure. What
narrows toward the sink is the unresolved share, not the total (correction 4 holds).

**The lens is an edge-colouring, not a node-colouring.** Delivery type is a property of a decision *at
an act-site* (this settles the direction of open ruling 11 toward the pair reading). The same decision
can be mechanically delivered at one sink and judgement-mediated at another; colouring nodes would hide
exactly that. Consequence, computable over the DAG:

> A path from a decision to an act is only as mechanical as its weakest edge.

**The map is the evaluator's own structure rendered**, not a separate artefact — same object the Q19
evaluator walks. This files it under the standing position on the claim-graph website: generated
downstream of the graph by CI, never a separate content source.

**Rendering constraint.** Acts are numerous and mostly uninteresting; a global DAG is unreadable.
Useful views are per-act-site or per-region. The filter is principled rather than aesthetic: surface
nodes by unresolved share and delivery type, not structural importance. **Uninteresting is what
governed-and-closed looks like from outside** — a helper function is a resolution complete before the
act, mechanically delivered, `H(V|X)` near zero. Vital-and-boring is the target state. Boringness is an
observable proxy for capability coverage, available from the actor's own report without measurement;
effortful regions are uncovered regions.

**Call graphs are the all-mechanical restriction.** A call graph's edges are control transfer —
mechanical by construction, no failed delivery possible. That is why compilers can do so much with them
and why none of this note's failure modes appear there. Caution: the properties that make call-graph
machinery tractable are precisely the ones this graph lacks; borrow selectively.

**Goals: no new construct until the corpus test runs.** Many acts serving a value is plausibly a claim
the acts ground, not a new node type. Adding a goal object now risks duplicating the claim side.
Aggregation to a goal is a decomposition, so it has a seam and `I(V;S)` applies — if goals are ever
needed, that is where the measure meets them.

### 13.7 Capability, and the two locations of standing supply

Emil's definition, adopted as the working one:

> **A capability is a set of trained decisions ready for fast retrieval when acting.** Capabilities are
> the basis for the fundamental boring acts.

This is a better-behaved object than capacity-as-budget: it has extension (you can ask which decisions
are in it), it is typed, and it maps onto the graph rather than sitting beside it. It is part of why B1
kept resisting — the budget was a scalar where the object is a set.

**Two locations for a pre-act resolution** (from the ROE/CQB split, Emil):

| | Resolution lives | Delivery | Inspectable | Superseded by |
|---|---|---|---|---|
| Standing, **external** | in an artefact — ROE card, filed decision, lockfile | retrieved at act | directly | filing an amendment |
| Standing, **internal** | in the actor — weights, trained response | none; the actor *is* the resolution | behaviourally only | retraining |

Internalised resolutions have **no delivery failure mode** — nothing to deliver — which is why they are
the strong mechanism and the dangerous one. They cannot be audited, only tested (statistical, not
exhaustive); and they cannot be superseded by filing — amend the doctrine and actors carrying the old
resolution keep carrying it until retrained. Design rule the doctrine already encodes: **resolutions
that must change fast stay external; resolutions that must be fast stay internal.** The split lands
where the predicate closes (battle drills against judgement-under-uncertainty).

**Consequence for the B1 split.** An unfilled link facing an actor whose capability contains a matching
resolution is *judged*; facing one whose capability does not, it *escapes*. Membership, not magnitude —
checkable in principle where the budget was not. Both may be needed (a capable actor can still be
overloaded), but membership is the operable one. *(Revision 9: canon partially confirms the pairing —
capacity-generated escape is closed as sufficient-not-necessary, and the five diagnosed
counter-instances are no-supplier cases, which is the membership shape. The corpus session reads
specimens against that separation rather than treating this as an open conjecture.)*

**Frameworks and languages are externalised, transferable capability stores** (Emil): resolutions
somebody internalised, worked loose into an artefact, made installable. The GC is a filed resolution of
memory-reclamation decisions. The artefact sits on both sides depending on the indexing actor —
internal-to-the-program (constitution, not consultation), external-to-the-adopter (auditable,
versioned, supersedable) — and that dual position *is* the transfer mechanism, not a wrinkle. It
connects §9 (commodity is this transfer at scale) and inverts the supersession asymmetry (dependency
upgrade is retraining you can pin, diff, roll back; its decay mode is Q21's — pinned, ageing against
the world). Cost stated in the same breath: adoption is accepting thousands of resolutions unread —
coverage without inspection, escape's precondition arriving through the supply chain.

Constraints held: capability extension is knowable only behaviourally, putting it in the same epistemic
position as `H(V)` estimated from samples; and capability is **per arrangement**, not per actor — the
resolutions may live in the tooling rather than the weights.

*Flagged, structural:* this is the **third** construct this session that reduces B1 (shared budget,
§7.3; membership, here; and the disposition framing, §13.1). Each felt like progress. The corpus test
must check whether these are one account or three; if three, the model carries unnoticed redundancy.

### 13.8 Transfer, closure, and training

The chain of correspondences, each adopted with a correction:

**Demonstration transfers a specification, not a resolution.** "Watch me do this" delivers the verdict;
"this is how your stance should be" hands over the acceptance predicate. A framework transfers the
resolution itself — exact, identical per adopter, working on day one. Demonstration transfers what
right looks like; internalising it still costs the observer's own practice. The valuable half is the
**checker installed by watching**: verification transfers by observation, generation only by practice —
the generator/checker asymmetry in human form, and teaching exploits the gap in that order.

**Watching does not close the predicate** (correction to Emil's formulation, accepted in session).
Closure is operational — the student's evaluation of their own stance must *run reliably in the
student's arrangement*, and early practice is full of "it felt right" that the instructor rejects. The
sequence has three stages: **specification** (transferred by watching) → **calibration** (corrected
reps; the instructor is the operational closure the student lacks) → **drill** (generation trained
against the now-closed predicate). The instructor's exit between stages two and three is observable:
"check your stance" replaces "let me check your stance."

**Drill is H3 inside a single actor.** Training against a closed predicate is the generator/checker
composition running internally: cheap verification, expensive generation, retries. Drill works for the
same structural reason RLVR works — dense mechanical verdicts per attempt. The H3 boundary carries
over: what is trainable this way is what the predicate reaches. Demonstration-based teaching fails not
when the student cannot perceive the demonstration but when the predicate cannot be specified
perceptibly at all — then nothing closes, and the residue routes to selection, apprenticeship, delayed
feedback (§5.7 upstream, on a shooting range).

**Supervised learning is stage two without stage one.** Labelled data is verdicts — corrected reps with
the demonstration stage absent. The model never extracts a specification from watching; it guesses and
is graded. In the analogy: a student never shown the stance, only told hit or miss. It works at scale,
and its rep count is the price of correction without specification. The cleaner mapping: *specification
→ calibration → drill* corresponds to *pretraining → supervised fine-tuning → RLVR*, with few-shot
prompting as demonstration installed without gradient.

**The checker-arrival asymmetry — an arrangement property, not a platform one.** In drill, the student
acquires the predicate; the instructor's exit is closure transferring. In gradient training the checker
stays outside the model permanently — loss computed *on* it, never *by* it. What internalises is
capability shaped by the predicate, not the predicate as executable resolution. Hence models that
generate what they cannot verify: generation transferred without the checker, the inverse order from
demonstration-led human training. **Restated at the right level:** the order in which H3's halves
arrive is a property of the *training arrangement* — outcome-graded humans also get generation first
(the natural athlete who cannot coach), and verifier-model setups are attempts at checker-first digital
arrangements. Predicts self-verification lagging generation in models trained with external loss — an
observable, much-discussed property.

**The platform discipline** (from Emil's "two separate platforms," scoped): platform constrains the
**arrangement menu** — no weight inspection for humans, no few-shot install of motor skills — without
appearing in the constructs. Every divergence must be pushed down to the arrangement that produces it.
"It's a platform difference" is almost always one level too high; if a divergence genuinely cannot be
pushed down, *that* would be framework-relevant, because it would mean a species clause is load-bearing
somewhere. None has appeared this session.

*Flagged:* §13.8 models human skill acquisition and ML training in the same breath. Deliberate
practice, apprenticeship, and tacit-knowledge literatures on one side; ML curriculum and
self-verification literatures on the other. Both unchecked. The framework-side claims are the filable
ones; the pedagogy and the training lore are motivation.

### 13.9 Domain, layers, and per-act exposure

**Entity-attachment is the one-axis special case** (Emil). A decision pinned on a domain entity is a
region specified on the domain axis and open on the rest. The bearer view and the position view are one
object read from the node side or the space side. The physics analogy carries further than it claims:
in physics the object is not given — carving the world into objects is the modelling act. Carried over:
**domain modelling is axis authoring.** The domain model is the axis registry other decisions file
against.

Name collision acknowledged rather than avoided: Evans's Domain-Driven Design holds this machinery under
other names — bounded context as region, ubiquitous language as per-context axis registry, aggregate
design as seam minimisation. **Relations between entities are seams**: a decision attached to a relation
lives at a decomposition boundary and should carry `I(V;S)`. "High cohesion, low coupling" is the
chain-rule trade-off stated qualitatively. *(Asserted from general knowledge, unchecked against Evans's
text; the corpus test could exercise the relations-as-seams projection cheaply — aggregate boundaries in
the client codebase are a live specimen.)*

**Why domain axes behave well, and the trap.** Entities are controlled ground — versioned, drift-free by
construction; domain-model change is supersession, visible and diffable. The best-behaved axis type in
the provenance table. The trap: the entity "Customer" is controlled; the customer is not. The pin holds
the representation still while the referent moves — Q21's decay-of-relevance arriving through the domain
model.

**One overreach struck before filing:** "describe everything" cannot hold on the framework's own
grounds. The domain-model decision attaches to no entity — it creates them. Cross-cutting decisions span
entities. Bearer-hood is per-region, not universal.

**Layers, and SDP as a drift rule** (Emil). Multiple axis registries — domain, technical,
organisational, regulatory — each an authored coordinate system, ordered by dependency. SDP translated:
*depend in the direction of stability* means **pin your regions on the axes with the lowest drift
rate**; a registry depending on a fast-moving one inherits its decay, and every decision filed against
it ages at the upstream rate. SDP minimises the supersession cascade. "The domain is the stable core"
becomes measurable rather than doctrinal: registry drift rates are observable in version control.

**Declared stability is a prediction, not a property.** A wrong estimate inverts a dependency and the
cascade runs backward through everything filed against it. The upstream/downstream repo topology is this
applied once already, and the §11a–e collision is what a stability-prediction miss looks like from
inside.

Consequences: **layer boundaries are seams between registries** (anti-corruption layers are seam
artefacts — seam demand paid explicitly rather than smeared), and **cross-cutting decisions get an
address** — filed against a different registry whose axes span the domain layer; cross-cutting was only
ever relative to one coordinate system.

**The structuring metric, corrected** (from Emil's drift proposal). Two corrections held:

- Drift and revisitation are not independent — Q14 fires on drift by construction, so the correlation
  validates the plumbing, not the theory. **The residual is the finding**: revisitation firing where
  measured drift is low means a mis-layered axis, a wrong tolerance, or an unnamed axis moving
  underneath (§1.2 arriving through the revisitation channel).
- Drift alone under-determines the structure. Entities and their invariants co-move; coupling belongs
  within a layer, rate differences between layers. The rule is **cluster axes by co-drift, order
  clusters by rate.** Two quantities.

What drift-as-metric buys at its real strength: **SDP becomes falsifiable per codebase.** Declared
layering implies a predicted drift ordering; version control contains the actual one; mismatches are
mis-layered axes, findable mechanically. Another §3.1 case — the claimable content lives in the
differential, where measured co-drift says the conventional layering is wrong.

**Per-act exposure** (Emil). The act is an origin point that orders the graph: from an act's position,
every governing decision sits at some distance in drift exposure, delivery type, and reading age.
Multiple acts, same graph, different orderings. This is **not** multiple SDP structures — dependency
direction runs between registries and does not run toward acts; both layers are upstream of every act.
It is **per-act stability relative to position**: the layering stays global, the exposure profile is
per-act. Kept separate, they check each other: many acts' profiles ranking a "stable" layer as their
dominant drift source means the global layering is wrong *as measured from where the work happens* —
SDP validation weighted by act traffic, the Q9 move applied to structure instead of coverage.

The profile is the evaluator's natural output (Q23, Emil's ruling).

*Flagged:* "drift" now carries three distinct rates — ground-value drift (Q12), axis-registry drift
(here), and referent drift under a pinned representation (the Customer trap). The structuring metric is
the second. They need separate names before any of this files, or the construct leaks across them.

### 13.10 The per-act proxy predicate

The session's last construct, and the one where the others converge.

**Guarded acts: satisfaction is not closure** (correction to Emil's junction case, accepted). Waiting to
pull out, the predicate — gap sufficient — is operationally closed the whole time; every glance
evaluates it reliably. What changes while waiting is the *verdict*: false, false, true. Letting "closes"
name verdict-true would leak the framework's most load-bearing term. The junction is a closed predicate
polling volatile ground.

**The evaluation is the last event before the act; the last decision happened earlier.** The threshold
("pull out when the gap is sufficient") is a standing resolution, authored by training before the
junction was ever reached. Verdict-true is discharge, not decision — which is why it is fast,
repeatable, and boring for the experienced driver (§13.6's diagnostic). Anatomy of a guarded act:

| Part | When | What it is |
|---|---|---|
| Threshold | pre-act, standing | the decision — what counts as sufficient |
| Polling loop | act-approach | repeated ground reads, as-of refreshed per glance (Q11) |
| Verdict-true | act trigger | evaluation — discharge of the standing resolution |

Pinning collapses the polling loop (Q21), which is the software case: CI acts without waiting.

**Act-time authoring: where a decision actually occurs at act time.** When no threshold is standing —
unfamiliar junction, snow, a novice — the actor authors the acceptance criterion under act conditions.
Two corrections held from session:

- Authoring does not *close* anything; evaluability is the **design constraint** of the authored
  predicate, not an accomplishment. The actor writes a predicate evaluable by them, here.
- "To fit the verdict we need" struck: a predicate authored to output the wanted verdict is
  rationalisation — the checker built to pass. The target is a predicate whose verdict *tracks the
  acceptable region*, authored without full access to the true acceptance relation. That gap is where
  act-time authoring goes wrong.

**The capability, named:** decomposing an unevaluable acceptance relation into an evaluable proxy over
available ground. Both actor types demonstrably have it — the human at the snowy junction; an LLM told
"make the code good" that decides to check compiles, tests pass, interfaces unchanged. Arguably the most
consequential thing LLMs do that programs never did: a program evaluates the predicates it shipped
with; an LLM writes new ones mid-act. The danger case is §13.3's silent completion in predicate form —
a proxy authored and not surfaced, so the act looks governed by a filed criterion while governed by an
improvised one.

**Quality dimension: proxy fidelity** — how well the authored predicate's verdict tracks the true
acceptance relation over ground actually encountered. Goodhart's territory. A drilled evaluation is
right or wrong per act; an authored proxy can be systematically wrong in a region and self-confirming,
because the actor's only check on the proxy is the proxy.

**The pipeline (Emil's assembly).** Per act: retrieval delivers the governing set → capacity conditions
how well → the actor authors a proxy from the delivered specification plus drilled parts, binding
current ground at current as-ofs → the act discharges against the proxy. Every construct in this note
feeds the authoring step, and the pipeline is only as good as its worst stage:

- Undelivered decisions → proxies authored without constraints that exist.
- Stale readings → proxies fit to ground that has moved.
- Capacity spent on retrieval → capacity unavailable for authoring.

**One correction to the assembly:** not "as close to the one we know to be right" — if the true
predicate were known, the actor would evaluate it. Authoring happens precisely where the acceptance
relation is not fully stateable. The retrieved context is not input to an approximation of a known
target; **it is the specification being approximated.** Two consequences:

- **Proxy fidelity is bounded by delivery before skill enters.** An actor cannot honour a constraint
  that never arrived. Mechanical delivery raises the fidelity ceiling for every act at a site,
  regardless of actor quality — Q19's value restated at its sharpest.
- **The proxy is where everything converges.** Position selects the governing decisions; delivery
  determines which arrive; as-of determines what ground binds; capability supplies the drilled parts;
  the residual is filled by the actor or escapes. Plausibly what `H(V|X)` has been counting: the demand
  the delivered encoding leaves for the proxy to carry.

**Model consequence.** §13.2 is one construct short: graph, position, timing, delivery are structure;
the per-act authored proxy is the **event** where structure meets an act. Fifth construct, pending the
corpus test like the rest.

**Mechanisable check, rare for anything touching judgement:** delivered governing set versus emitted
proxy is a comparison a tool can run — did the proxy honour what arrived, and what did it improvise
beyond it?

### 13.11 Proposed sequence

The pull to re-derive the store vocabulary while this is fresh is exactly what canon-first discipline
exists to resist. A store re-derivation touches ratified material across both registries.

| # | Step | Why here |
|---|---|---|
| 0 | **Measure note / MDL related-work** | Queue head, unaffected by any of this (§13.2) |
| 1 | **Corpus test** — re-express a handful of ratified decisions in graph + timing + delivery terms | Cheap falsifier. Clean expression earns the model a session; a class that will not express is learned for the cost of an afternoon, with nothing entering canon |
| 2 | **Escape reconciliation** | Already queued; now absorbs retro-filing (§13.4) and *undelivered* (Q18) rather than these being separate rulings |
| 3 | **Store re-derivation** | Own gated session, only if step 1 passes |
| 4 | **PRD for retrieval and delivery** | Q19–Q20; engineering, and ranks below all of the above |

**Open rulings that step 1 would settle cheaply:** whether *inert* and *open* collapse (ruling 2),
whether judgement-evaluable is a type or a maturity state (ruling 12) — §13.7's trainability argument
pushes toward maturity-state, the strongest evidence in the note for that reading — whether the
chain/graph is the composition object or the seam machinery restated, whether the three B1 reductions
are one account (ruling 16), and whether `I(V;E)` is the internalised store (ruling 17).

---

## 14. Provenance

Conversational sessions on 2026-08-12 and 2026-08-13. Originating claims from Emil. Formal consequences,
corrections, and prior-art assertions developed by Claude and marked where unconfirmed.

Emil ruled explicitly on: the luck clause, bound-exceedance default, the map definition requiring axes
plus direction, the four states as a feedback loop with backward jumps, the store framing in Q10, stale
ground as ground-not-as-expected rather than escape, supersession over decision-to-act decay, execution
capacity as the shared budget, parking the LLM capacity question, that the delivery distinction needs its
own vocabulary, applying the actor model to the extraction act with a closing predicate (Q20),
failure-to-close as an escalated finding, consolidating the declared-space limit as one structural result
(§1.2), code-writing acts as the primary act-site, ground pinning as a tolerance mechanism (Q21), and PR
lifetime as drift exposure (Q22), judgement as residual rather than store, the graph as the object,
retro-filing of uncovered escapes, TDD as the timing discipline (§13.5), the directed graph toward acts
as the map with delivery type as the lens (§13.6), capability as a set of trained decisions and the
basis of boring acts (§13.7), the ROE/CQB split between external and internal standing supply,
frameworks and languages as program-actor capability, demonstration as the human transfer mechanism,
transfer as predicate closure (corrected in session to specification-then-calibration), the
supervised-learning correspondence, platform divergence as acceptable (scoped in session to the
arrangement menu), domain entities as decision bearers with the physics-object parallel, ground-axis
layers structured by SDP, drift as the calculable basis for SDP with revisitation as its correlate
(corrected in session: residual over correlation, co-drift clustering added), the act as per-act origin
point over the shared graph, and the exposure profile as the evaluator's natural output (Q23), predicates as first-class graph citizens
with open predicates as the motivating half (Q24), predicate identity under shifting ground (corrected
in session: identity in specification, closure regional), the junction case as polling (corrected in
session: satisfaction is not closure; the last decision precedes the act), act-time predicate authoring
as a capability of both actor types (corrected in session: evaluability as design constraint, not
closure achieved), and the per-act proxy pipeline (corrected in session: retrieved context as the
specification being approximated). All other content is projected and unexercised.

**Section 13 carries lower confidence than the rest.** It was assembled at the end of a long session and
has had no settling time. The corpus test in §13.11 exists to price it before anything is acted on.

**Revision 9 (2026-08-14).** B1 re-booked against verified live canon following the related-work
gate-pass session: the capacity model is ratified (core/11; DDD-floor-01 at *reported*), capacity-
generated escape closed as sufficient-not-necessary, five no-supplier counter-instances diagnosed in
ratified canon, residual re-stated as three items with three dispositions. Ruling 16 reframed;
revision-9 annotations added at §13.1, §13.7, §7.3; Q10's falsifier stated. The original B1 booking is
itself the third recorded instance of the stale-projection failure mode this note's Q11/Q12 describe —
a forward-looking phrase outliving the work it waited on — and is recorded as correction 31 rather
than silently repaired. Sections other than those named are unrevised and may still carry phrasing
written under the old booking; the corpus session reads the B1 reconciliation note as authoritative
where they conflict.

**Revision 10 (2026-08-14).** Three additions from Emil's questions: intent as a filed object (Q25),
ground axes as ontology with the OWA/SHACL reading of §1.2 (Q26), and trusted sources as the mechanism
under institutional ground (Q27). Emil ruled explicitly that Q26 concerns ground and not claims, that
the registry should start generic and dive inward, and that trust must cite the ground it stood on.
Corrections 32–33 recorded; rulings 24–27 opened; B4 annotated as grown.

**Revision 11 (2026-08-14).** Q28: projections typed by function (ground/act) and by receiving
arrangement, with the fourth delivery-failure mode and the sales specimen as adversarial instance.
Emil ruled that trust and poisoned ground cover the adversarial case without new vocabulary
(correction 35). Ruling 28 opened.

**Revision 12 (2026-08-14).** Q28 extended with documentation as the indexed case — the projection
matrix as decision-set × receiving-arrangement — per Emil. Flagged as a candidate for the §9 map.

**Revision 13 (2026-08-14).** Q29 (arrangement description for projection derivation, redirected from
Emil's actor question; encoding-proxies for humans; self-assessment as prior); Q11 amended
(assurance-on-reading, the ice); Q27 amended (triangulation hinges on provenance-independence).
Corrections 36–38; rulings 29–31. Emil ruled: humans need proxies for encoding parameters, and
questionnaires are that proxy; the ice case; that "three sources" was worth asking about
triangulation. Claude redirected the actor question to arrangement, rejected trust-as-scalar, and
corrected the three-sources framing — all recorded.

**Revision 14 (2026-08-14).** Q30 from G-track PRD work: repo as projection not authority; "domain"
as lacking term with **ground registry** proposed for canon; projection-as-source recorded as a
diagnostic alongside wrong-object attachment. Corrections 39–40 (both Emil's, both the same shape);
ruling 32 opened as a freight-list item.

**Revision 18 (2026-08-15).** Q33's routing amended per Emil: demand × act is measure-paper
material. B/C plus aggregation (N·H(V), the correlation inequality, the bit-accounting amortisation
asymmetry) route to a booked measure-paper discharge section, claims filed upstream with Wave 3
first; A stays Paper A. The economic crossover N* is held at projection layer by the paper's own
loss-blind discipline. Noted: second honest filler against the paper's word-floor gap, and the
missing prose bridge to core/11's soft-capacity bound.

**Revision 17 (2026-08-15).** Q33: demand discharge as core, per Emil's ruling that the demand
movement belongs in canon. Three upstream filings drafted with derivations and falsifiers
(supply-mode exhaustiveness; act-indexed discharge; distribution-weighted discharge, flagged as
possibly expository); the force metaphor, firefighting, and the company recursion deliberately held
as prose; status inflation named as a projection-layer failure mode beside Goodhart. Routing
recommended to Wave 3 + Paper A, explicitly not into the earned session, protecting
scope-equals-evidence. Ruling 35 opened.

**Revision 16 (2026-08-14).** The corpus test ran and closed at five gates
(`meta/corpus-test-results-2026-08-14.md`, downstream repo — the authoritative record; this note
defers to it on every count). Outcomes folded: correction 42 (the binary timing predicate loses —
three-way primary, —(open) as the fourth value); evidence appended to rulings 2, 12, 16, 17, 22, 23;
B2 rewritten as discharged-and-earned with the ruled queue. The registers' own history corroborated
the vocabulary before it existed (proto-`revisit_if`, the granularity paragraph, the named
exposure) — additions that describe what practice already does under improvised names. The earned
canon session's scope is fixed by the Gate 4 ruling and excludes Q25–Q32, which were never priced.

**Revision 15 (2026-08-14).** Q31 (event sourcing as the data-layer instance of authority/projection;
raw-at-the-boundary as the ledger; discard as a governed highest-α act, correcting Claude's "discard
never" — correction 41) and Q32 (constructive versus verification closure, from G-track extraction).
Rulings 33–34 opened. The Databricks/Spetlr D-track question is **parked by Emil's ruling** — it does
not fit product-cli — with its 2026-08-14 verification results banked in the conversation record:
Delta Kernel Rust as the strategic library, UC credential vending GA, managed-table external writes in
Beta, and the extract-decisions-before-porting-code migration discipline. A future D-1 re-verifies;
the Beta status is the kind of fact that moves.

No repository access was available in any session producing this note. Nothing here has been
committed. The standing commit-before-reporting rule cannot be discharged from here and remains
outstanding for this artifact.
