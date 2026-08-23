# Triage — external review of Paper A

**Status:** holding. Claude-drafted assessment for Emil's ruling. Nothing filed, no manuscript edit
made. Paper A stands as merged at `40d277f`.
**Verdict on the review:** high quality, technically competent, and mostly correct. It is a
major-revision review whose three load-bearing findings **change canon before they change prose** —
which is exactly what the reviewer says in their §12.1, and they are right about the ordering.
**One finding is mine:** the closure ladder's axis mixing (§10.1) is a structure I ratified at
Paper A's Gate 1. Recorded as my error, not the session's.

---

## 1. The three findings that move canon

### F-A — `DDD-measure-06`'s biconditional (review §2)

The reviewer says Paper A claims the measure exists **iff** the predicate operationally closes, and
that the companion measure note contradicts this in both directions. **They are right, and the
worse fact is that the contradiction is ours, not theirs.**

The measure note's revision (external review, seven gates, merged) rewrote §7 into a *scope
condition* with three separated requirements — existence, availability, estimability — and conceded
that open predicates admit distributions over evaluator judgment. **Canon was never updated to
match.** `DDD-measure-06` still carries the boundary claim at `established`, and Paper A projected
the node faithfully. So the projection is *stronger* than the note that shares its graph, and the
node is the source of the defect.

Note the historical detail: the measure revision's Gate 1 found the manuscript **overstating**
`DDD-measure-06` and repaired the manuscript to comply with the node. This review finds the node
itself wrong in the other direction. Both repairs are correct; the first did not license skipping
the second.

**Recommended disposition:** a canon session re-scopes `DDD-measure-06` — most likely statement
narrowed to *availability of this construction to an arrangement*, with existence and estimability
separated as the note's §7 already does — and its status re-examined. `established` is not
defensible for a claim whose own companion projection concedes both failure directions.

### F-B — raw ground collapses the allocation reading (review §3)

For a deterministic task `V = f(G)`, take `X = G`: then `H(V|G) = 0` and `I(V;G) = H(V)`. `G` is
ground available at the act and is not the verdict, so **`DDD-measure-15`'s admissibility condition
admits it**. The reading "the residual is what the arrangement must still resolve" then says an
arrangement holding raw ground has nothing left to resolve — while it may hold no rule for turning
that ground into an answer.

This is the ideal-observer objection from the first review, escalated correctly: it was answered
there with *caveats* (§5.1's "a real actor may fail to use information that is present"), and the
reviewer's point is that a caveat does not repair a condition that fails to exclude the case.
**The building-versus-being-handed distinction does not separate `G` from a program** — both build,
and only one is decodable by the arrangement.

**The repair is framework-native, and that is the interesting part.** The framework's own central
thesis is that determination is arrangement-indexed; the measure currently is not. Admissible `X`
should be **a representation the arrangement can decode** — which makes the residual
arrangement-relative and brings the measure into line with the paper it appears in. The literature
the reviewer gestures at exists and is citable: usable/predictive **V-information** (Xu et al.),
computational entropy, Blackwell sufficiency. This is a real technical gap with a real repair, not
a fatal objection.

**Interim honesty, if the repair is not immediate:** the reviewer's own recommendation — present
verdict entropy as a *bounded candidate quantitative extension* rather than an established measured
region — is the correct interim posture for Paper A.

### F-C — the four discharge modes do not partition (review §4)

`DDD-frame-15` filed three days ago at v5.7.0. The reviewer's three overlaps:

- **declared default vs filed decision** — a declared, governed default is both. *Cheap fix:* the
  mode means **undeclared** default; the definition says so.
- **deterministic rule vs judgment** — a thermostat reads ground at the act and produces output by
  a rule fixed beforehand. Canon's timing answer is *encoded*, but the paper's gloss of judgment
  ("variation produced at the act by an actor reading ground") reads as covering it. *Fix:* judgment
  requires that the standing rule **not** fix the output given the ground — genuine
  underdetermination at the act.
- **trained inference** — policy-level commitment (§3.3), judgment (§4.1), and standing supply
  (§10.3, `DDD-cost-20`) at once. This one is not cosmetic; it needs a priority rule.

**The seam guard does not save this.** The guard separates governance-supply from discharge — a
different distinction, correctly ratified, and orthogonal to the overlaps above. Worth recording
that an external reader met the guard and still reported the "determined never, by nobody" phrasing
as conflicting: the guard is doing its job for a reader who already holds the framework, and not
for one who does not.

**Recommended disposition:** either an explicit priority rule that assigns each case exactly once
(and survives the reviewer's six test cases — trained inference, lookup tables, declared defaults,
randomised search with checking, abstention, timeout), or the modes are recast as orthogonal axes.
Both are canon work on a claim three days old, which is the cheapest moment it will ever be.

---

## 2. The meta-finding, and it matters most for the NGO plan

**Review §7: graph status is being read as epistemic status.** `established` means internally
argued and unchallenged; `reported` means exercised by a computation; `projected` bundles
definitions, formal claims, empirical hypotheses, and normative prescriptions — four kinds of
proposition with four different forms of warrant — under one maturity label.

The reviewer is right, and the timing is consequential: the primer session's status audit was
designed to *filter on this field*, and the repositories are about to become public under a
foundation. **A public status field that outsiders read as epistemic warrant, while it encodes
internal maturity, is the single largest trust exposure in the transfer.**

**Recommended disposition — and this may be the most valuable thing the review produces:** separate
the two axes. Maturity (`projected` → `reported` → `established`) stays as internal governance
metadata; a second field carries **kind** (definitional · formal · empirical · normative), because
each kind has a different warrant and a different falsifier shape. The reviewer's phrase for the
analysis sections — *authorial synthesis, not represented in the graph* — is more honest than
"analysis carries no status" and should be adopted.

This is a registry change with a wide blast radius. It is also exactly the sort of thing that gets
much more expensive after publication.

---

## 3. What I ratified wrongly

**Review §10.1 — the closure ladder mixes axes.** At Paper A's Gate 1 I ruled that §5.1 carries the
kinds framing (logical / operational / economic / normative) and §5.2 carries the strength ladder
(open → verification-closed → constructively-closed → formally-decidable), with an orthogonality
sentence in §5.1. The reviewer points out that **formal decidability is a logical property, not the
top rung of an operational ladder** — a decidable procedure can be operationally infeasible, and
constructive availability is arrangement-relative.

They are right, and the defect is in my Gate 1 ruling rather than in the session's execution. The
ladder should end at constructively-closed; decidability belongs on the logical axis, with the
relation between them stated rather than implied.

---

## 4. Correct, cheap, and not load-bearing

| Review item | Assessment |
|---|---|
| §5 residual discretion conflates four phenomena | **Correct.** Separate outcome variation across ground · epistemic uncertainty about a fixed policy · stochasticity · genuine unresolved or delegated selection. The cryptographic-hash example is decisive. Note `residual discretion` was added to `DDD-frame-02` at Wave 3 and deliberately not minted as a term — mint it *after* this separation, not before |
| §6 admission test's "selection" is not independently defined | **Correct.** The rock's failure is produced by the intended meaning of selection, not by a test. Genuinely hard; flag as open rather than patch |
| §6 ground separation `G*` (relevant) vs `G_A` (accessible and delivered) | **Correct and strengthening** — it is the delivery distinction applied to ground, and it makes the floor and ground-access hypotheses sharper. Cheap to adopt |
| §8 novelty not established | **Correct.** Hutchins, Hollnagel & Woods, Leveson, Horvitz, Bovens, Matthias, meaningful human control are all directly on point and absent. The narrowed novelty claim they offer — *a specific, auditable synthesis of resolution, assurance, delivery, and accountability* — is defensible and should be adopted |
| §8 title too universal | **Accept.** "The Missing Parameter" claims absence from prior work the paper has not surveyed |
| §9 hypotheses bundle variables; coding reliability first | **Correct.** Inter-rater reliability on the coding scheme genuinely is the first study, before any comparative-performance work |
| §10.2 accountability element counts (five vs three) | **Correct** — supply the mapping or reconcile |
| §10.3 worked example's provenance classifications | **Fair.** Present as hypotheses to investigate, not facts supplied by the scenario |
| §11 length, repository-nativeness, graph machinery in the argumentative path | **Correct.** Move Appendix A and the projection mechanics to supplementary material; the filing history and pending-node discussion do not belong in an archival paper |
| §11 rhetoric still communicates more warrant than the graph provides | **Correct**, and the same defect the measure note's review caught. The status labels are present; the surrounding sentences overrun them |

---

## 5. What not to concede

- **The arrangement as unit of analysis.** The reviewer calls it the durable core and they are right;
  the novelty narrows to the synthesis, not the object.
- **Filing versus delivery.** They call it a strong engineering contribution unprompted. It stands.
- **Resolution versus assurance.** Same.
- **The traceability apparatus.** They verified the checkers work and say so. Keep it — but move it
  out of the argumentative path per §11.
- **The disclosure discipline.** The absence of evidence is correctly disclosed and the reviewer says
  so twice. Do not let the revision make the paper more confident to compensate for being shorter.

---

## 6. Sequencing — and it changes the board

The reviewer's §12 ordering is right: **the graph moves first, then the paper.** Concretely:

1. **A canon session** taking F-A (`DDD-measure-06`), F-C (the discharge partition, three days old),
   §5's discretion separation, and §6's `G*`/`G_A` split. All four are claim-level.
2. **The status/kind separation** (§2 above) — its own session, and it should land **before** the
   repositories go public, because it is a registry change and the field is about to become a public
   commitment.
3. **The primer session, re-scoped.** The audit was to filter on status; the status field is now
   itself under repair. The primer either waits for the kind field, or filters on *derivation
   grade* — which is what the survivor list actually tracks and what a practitioner needs.
4. **F-B's measure repair** — arrangement-indexed admissibility, or the interim posture. This one is
   research, not filing; it should not block the others.
5. **Paper A's revision**, last, against a repaired graph — with the related-work survey (the
   reviewer named seven works; the survey is a week of reading, not a session), the narrowed novelty
   claim, the retitle, the supplement split, and the ladder repair.

**Nothing here needs to reach the running primer session mid-flight.** But the audit's premise has
moved, and Gate 1 is where that should be told.
