# GATE 1 — the manuscript skeleton, with bills of materials

**draft-pending-ruling.** P-1: the foundation's §12 structure, amended by everything that landed
since it was written, with per-section bills of materials and the two authored sections outlined.

**Working title:** *The Missing Parameter: Actor-Indexed Determination*
**Register:** the paper **states** the framework. Not a defence, not a survey, not the measure
note. The measure note counts; Paper A says what is being counted and why the accounting is
act-indexed.
**Pin (front matter):** *a projection of `actor-indexed-determination` at `v5.8.0`* — see the
survey §5.1 for the measure-note citation seam, held for ruling.
**Standing rule:** the paper may not introduce claims. Every load-bearing statement either cites a
graph node or is marked **register-native**.

## Reading the bills

- **Projects** — graph nodes cited in that section, with their status at `v5.8.0`. Status shown
  because the paper must never let a reader mistake a `projected` node for a finding.
- **Carries** — register-native material: prose argument, positioning, worked examples,
  reinterpretation. Nothing here asserts canon.
- **Closes** — a divergence or hedge this section resolves, one hunk each, flagged in the manifest.
- ⚠ marks a node held for ruling at this gate (survey §6, §7) and not yet in the bill.

---

## The amendments to §12, applied

| Amendment | Lands in |
|---|---|
| The determinable opens the vocabulary (`DDD-frame-13`; Johnson's noun — the foundation predates it) | **§2** |
| The outcome/verdict registers, where discharge is introduced (`DDD-frame-14`) | **§4.3** |
| The four discharge modes with the seam guard, where escape is defined (`DDD-frame-15`/`16`) | **§4.3** |
| The relational floor as `DDD-floor-02`, not the foundation's sketch | **§6** |
| The H-set carried as predictions-never-findings | **§9** *(numbering held — survey §5.2)* |
| §4.4's hedge → the conservation projection with the closing-region bound | **§4.4** |
| `term:commitment-level` / `term:residual-discretion`, minted at v5.8.0 | **§3** |

---

# The twelve sections

## §1 — Introduction: the fixed arrangement · ~850 w

**Projects**
| Node | Status |
|---|---|
| `DDD-frame-01` — determination indexed by ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩, not by the task alone | projected |
| `DDD-dec-24` — the filing provenance of the indexed-determination core | decision |

**Carries** — the motivating argument; *"a parameter that never varies is indistinguishable from a
constant"* (now canon exposition, `core/14` §1, so the paper's own sentence has a home to point at);
the list of what a governing choice may now be allocated among; the explicit refusal of the
"third species has appeared" argument; contributions; and the claim-status convention stated once,
here, so §9 does not have to re-argue it.

**Q38b** — the asymmetry thesis (software mechanised the determinable half and never the
determination half) is deliberately unfiled and out of scope. **One forward sentence permitted, no
more** (prompt). Placed at the end of §1's motivation, phrased as a question the paper does not
take up.

**Register note.** §1 must state, in its own voice, that the paper's primary claim is `projected`
and what that word means in the graph. The measure note's §7 earned its reviewer's trust by
conceding early; the equivalent move here is conceding in §1.

---

## §2 — Actors, arrangements, and ground · ~1,050 w

**Projects**
| Node | Status |
|---|---|
| `term:actor`, `term:admission-test`, `term:arrangement`, `term:act` | settled ×4 |
| `term:determinable`, `term:determinate` | **settled** (map said "new"; survey §3.2) |
| `DDD-frame-13` — determination's object is the determinable, its product a determinate; demand is a measure over unresolved determinables | projected |
| `term:composite-actor`, `term:ensemble-actor`, `term:swarm-gate` | settled ×3 |
| ⚠ `DDD-ground-05` — declaring the determinable space is constitutively prior to determination over it | projected |

**Carries** — the three-element actor test as exposition (alternatives, information-bearing
pathway, selection); the rock and the thermostat; actorhood as relative to an abstraction
boundary; scale and the market-as-one-actor-or-many; the arrangement as the unit of comparison.

**Authored §2.4 — the ground-provenance five-way.** Outlined below.

**Note on `DDD-frame-13`'s credits.** This is where Johnson, Prior, Funkhouser and Wilson enter
the bibliography; the credits field carries all four locators and the Wave 3 record marks all four
verified. The paper states which part is theirs and which is ours, in the credits' own words.

---

## §3 — Commitment resolution · ~650 w

**Projects**
| Node | Status |
|---|---|
| `DDD-frame-02` — three levels, composing, not actor species; residual discretion the remainder | projected |
| `term:commitment-level` | **draft** |
| `term:residual-discretion` | **draft** |
| `DDD-dec-26` — the mint provenance, and that the track was the trigger and not the authority | decision |

**Carries** — worked instances of each level; the composition argument; boundary-case
walkthroughs; and the discipline sentence the foundation states and canon now carries — *a
deterministic arrangement can carry substantial discretion, a randomised one can be tightly
committed, and a zero-variance arrangement can be consistently wrong.*

**Status discipline.** Both terms are `draft`, and this is the only place a draft node is
load-bearing. §3 says so in line, once, in the paper's own voice — not only in Appendix A.

---

## §4 — Resolution and assurance · ~1,400 w

The paper's densest section, and the one carrying both recorded divergences' first closure.

### §4.1 Source of resolution — **CLOSES the mode-mapping divergence**

**Projects**
| Node | Status |
|---|---|
| `DDD-frame-03` — source and assurance are separate dimensions | projected |
| `DDD-frame-15` — every completed act's demand is discharged: filed decision · judgment · arrangement default · uncontrolled draw | projected |
| ⚠ `term:store` — `{rule, check, actor, nothing}`; "there is no fifth source" | settled |

**Closes.** The foundation's §4.1 table (prior commitment / runtime actor / environmental-or-default
/ failure-or-non-resolution) is **replaced by `DDD-frame-15`'s four modes**. Canon's own words for
why, from frame-15's notes: the foundation's third source "mixes declared defaults with
uncontrolled dynamics", and its fourth "is not a discharge mode — under `DDD-frame-14` even a
failed arrangement's act lands a world-register outcome." One hunk; flagged in the manifest.

**The seam guard, carried in prose — the line the section exists to hold.** Two partitions over
one act, answering different questions:

- **The store partition** asks *what governance supplied*. Escape is **nothing**; there is no
  fifth source.
- **The discharge partition** asks *what the world produced*. Escape is **a supply mode** — an
  uncontrolled draw — because the world never produces nothing.

Neither reduces to the other. `DDD-frame-15`'s region field states the guard; §4.1 states it in
prose and cites the region. *This is the first of the two places the prompt expects line-level
rulings at Gate 2.*

### §4.2 Assurance mechanism

**Projects** — ⚠ `DDD-cost-25` (pre-act / at-act / post-act positions, each with a latency;
a mechanism whose latency exceeds the consequence horizon does not assure) · `DDD-cost-08`,
`DDD-cost-09` (assurance-by-actor is occasioned, assurance-by-check is standing) — all projected.

**Carries** — the mechanism list (proof, mechanical check, monitoring, review, authorization,
statistical evaluation, audit, none) and the foundation's defining sentence: the property is not
timing but independence sufficient to detect relevant failure.

### §4.3 Escaped decisions, and the two registers

**Projects**
| Node | Status |
|---|---|
| `term:escape` — determined *never*, by nobody; the only forbidden state | settled |
| `DDD-frame-04` — escaped decisions predict ungoverned failure modes | projected |
| `DDD-frame-14` — discharge produces a determinate landing in two registers: outcome and verdict | projected |
| `term:outcome` — the world renders outcomes, never verdicts; governance is the conversion | settled |
| `DDD-frame-16` — discharge is act-indexed; standing supply is inherited per act, occasioned produced per act | projected |
| ⚠ `DDD-delivery-01/02/03` — filing is not encoding; governance filed but undelivered is escape; unretrieved decision and unretrieved check are correlated failures | projected ×3 |

**Carries** — that "escaped" does not mean "determined by nothing"; the luck reading (escape is
tested on the arrangement, not on what landed); and the standing/occasioned distinction, for which
the measure note's §6 supplies a **worked projection with a reproducing asset** — cited, not
restated. `DDD-frame-16`'s region routes that content there deliberately, so the citation direction
is canon's own.

### §4.4 Conservation — **CLOSES the hedge, the ruled substitution**

**Projects**
| Node | Status |
|---|---|
| `term:conservation` — for a task at a declared assurance level, within a fixed decomposition, demand is conserved; reduce it in one store and it relocates | settled |
| `DDD-measure-01` — specification demand is verdict entropy, where the predicate closes | projected |
| `DDD-measure-02` — conservation on the closing region **is** the chain rule: H(V) = I(V;X) + H(V\|X) | **established** |
| `DDD-measure-06` — the measure exists **iff** the predicate operationally closes | **established** |
| `DDD-measure-10` — you cannot decompose your way out of the work | **established** |
| `DDD-frame-10` — demand conserved as a scalar across arbitrary re-arrangements, actor-generally | projected |
| `DDD-frame-11` — the governance question is well-formed on the total domain; the cost question only where the predicate closes | projected |
| `term:seam`, `DDD-measure-03` — the seam is I(V;S) | settled / reported |

**Closes.** The foundation wrote: *"The paper should therefore avoid saying that an exact total is
invariant until an independently motivated measure exists."* **It exists.** The hedged allocation
principle comes out; the conservation projection goes in **with the closing-region bound stated,
not implied** — `DDD-measure-06` is the bound and `DDD-frame-11` is what survives outside it. One
hunk; flagged in the manifest.

**The discipline sentence, non-negotiable.** `DDD-measure-02` is *arithmetic* — the chain rule of
entropy, Shannon's, holding for every joint distribution. `DDD-measure-01` is the *modelling
claim*, and it is what is falsifiable. The paper never presents the identity's holding as evidence
for the framework. The measure note's §7 is cited for the full statement; §4.4 states the
separation in one paragraph and does not re-derive.

**Numbers.** None minted. Where §4.4 wants a worked figure it cites `core/09` §3 or the measure
note's assets.

---

## §5 — Closure and evaluability · ~1,300 w

**Projects**
| Node | Status |
|---|---|
| `term:closure` — closed **for an arrangement**: ground observable, adequacy evaluable within declared resource, latency and confidence bounds; *decidable* reserved for the formal special case | settled |
| `DDD-frame-06` — closure is distinct from generation cost | **established** |
| `DDD-frame-05` — producer identity not epistemically necessary for the checked property, **and nothing more** | projected |
| `DDD-frame-09` — RETIRED: "closed predicates make intelligence unnecessary" | **retired** |
| `DDD-measure-11` — the measure prices the verdict, not the search | reported |
| `DDD-frame-11` — governed domain strictly wider than measured | projected |
| `DDD-cost-08/09/11` — the two gates; closing a predicate flips the sign of the assurance/actor-class coupling | projected ×3 |
| `DDD-measure-06` — measurement and closure have the same domain | **established** |

**Carries** — the kinds framing (logical / operational / economic / normative), foundation-native,
which the readiness map licenses as manuscript analysis; acceptance-region accessibility (density,
topology, search-space size, gradients, retry cost, adversarial pressure); `DDD-frame-05`'s six
non-implications stated as a list; open-predicate dependence and its residual.

**Authored §5.x — the closure taxonomy.** Outlined below. *This is the second of the two places the
prompt expects line-level rulings — it is where the retirement sits.*

---

## §6 — Actor-indexed irreducibility · ~800 w

**Projects**
| Node | Status |
|---|---|
| `DDD-floor-02` — the judgment floor is **relational**: irreducibility is a property of the indexed relation, not of the task alone | projected |
| `term:floor` — the intrinsic floor is a property of the acceptance predicate, not of the decision | settled |
| `DDD-floor-01` — the capacity mechanism, region-bounded | **reported** |
| `term:escape-mechanism` — overflow ∩ open; **sufficient for escape, never necessary** | settled |
| `DDD-dec-15` — the scope correction that bounds both | decision |
| `DDD-measure-06` — the measure vanishes exactly where the floor is non-zero | **established** |

**Carries** — the Brooks reinterpretation (essential/accidental becomes precise when indexed);
Ashby, Tesler, Meyer. **`DDD-floor-02` replaces the foundation's sketch**, which is why §6 states
the relation rather than arguing toward it.

**Discipline.** The floor's coincidence with the measure's boundary is *worth noticing and is not
evidence* — the two arguments share the closure premise. The measure note's §8.2 states this
exactly; §6 cites it and does not re-argue it. `DDD-floor-01` and `term:escape-mechanism` are
cited **only** in their `DDD-dec-15` scoping: sufficient, never necessary. The universal
quantifier is superseded and the paper must not restore it.

---

## §7 — Accountability completeness · ~600 w

**Projects**
| Node | Status |
|---|---|
| `DDD-frame-08` — accountability is a **relation** (attribution, persistent principal, authority linkage, stake, sanction path), not an intrinsic capacity; an arrangement naming an executor but no principal is incomplete | projected |
| `term:accountability`, `term:attribution`, `term:answerability`, `term:liability` | settled ×4 |
| `DDD-hyp-04` — carried here as the prediction the relation generates | projected |

**Carries** — executor versus principal; the ledger-limits argument (what provenance records
cannot supply: authority, stake, a sanction path); `core/05`-consistent exposition.

**Closes** — the foundation's §14 "replace completely" item *accountability as an intrinsic actor
capacity*. `DDD-frame-08` is the replacement.

---

## §8 — Worked example: code generation · ~900 w

**Projects** — canon **corroboration** only: `core/09` §3's fully computed example; the corpus
results for register practice. No claim is stated here that is not stated elsewhere.

**Carries** — the example itself, manuscript-native by design, carried through every construct:
task and tolerance → ground and its provenance → the three commitment levels → resolution source
per choice → closure analysis per predicate → the escaped decisions the walk exposes → the
prediction.

**Numbers — the rule.** The example is **structural, not numerical**. Where it wants a figure it
cites the measure note's assets or `core/09` §3. **No asset is minted this session.** If a figure
turns out to be wanted that nothing existing supplies, the figure is dropped, not computed.

---

## §9 — Predictions and study design · ~900 w · *(numbering held, survey §5.2)*

**Projects**
| Node | Status | Evidence | Owner |
|---|---|---|---|
| `DDD-hyp-01` operational evaluability | projected | `[]` | paper-4 |
| `DDD-hyp-02` ground and judgment dependence | projected | `[]` | paper-4 |
| `DDD-hyp-03` generator/checker composition | projected | `[]` | paper-4 |
| `DDD-hyp-04` accountability completeness | projected | `[]` | paper-4 |
| `DDD-hyp-05` selection versus training | projected | `[]` | paper-4 |
| `DDD-frame-07` — the umbrella over H1–H5 | projected | `[]` | paper-4 |

**Predictions, never findings — the verbatim requirement.** All six are `projected` with `evidence:
[]` and `owner: paper-4`. §9 says so **in the body**, not only in the appendix: these are
predictions with unrun falsifiers, the evidence fields are empty by discipline, and the study that
would pay the debt is paper-4's and is unrun. Appendix A shows `projected` and the empty evidence
column so no reader can mistake the set for results.

**CLOSES the training divergence.** The foundation's §8 H5 commentary — *"closure does not make
training available or unavailable as a hard gate"* — contradicts settled `term:training`
(*"closure decides whether training is available; cost decides the ratio when it is"*).
`DDD-hyp-05`'s notes record the divergence and the disposition. **Canon governs: the paper carries
`term:training`'s settled form and the gradient reading stays manuscript-absent.** The supersession
question is Wave 3 successor item 1 — queued, named in one sentence, not taken. One hunk; flagged.

`DDD-hyp-05`'s validity qualification is carried with it: the gradient must be read with claimant-
identity persistence held constant, because an answer-keyed instrument cannot evidence open-
predicate carriage (`DDD-cost-13`).

**Carries** — the study design: unit of analysis, independent and dependent variables, the
preregistered model, the falsifiers. The preregistration artifact is **paper-4's**, referenced and
not asserted.

---

## §10 — Limits and boundary cases · ~700 w

**Projects**
| Node | Status |
|---|---|
| `DDD-frame-09` — retired, with its scoped survivor `DDD-frame-05` | **retired** |
| `DDD-measure-08` — retired: "a better decomposition destroys demand"; the destruction was an artifact of not counting I(V;S) | **retired** |
| `term:escape-mechanism` — the scope note | settled |
| `DDD-measure-15` — admissibility: the engineering reading holds only for conditioning variables computable from ground available at the act | projected |
| `DDD-frame-11` — the measure's silence licenses no claim of unaccountability | projected |
| ⚠ `DDD-frame-12`, ⚠ `DDD-agent-01` | projected ×2 |

**Carries** — randomised and adaptive programs; learned symbolic systems; hybrid arrangements;
distributed actors; incomplete and gameable predicates; expensive decidable checks; contested
normative ground.

**The section's argument.** The retirements are **evidence the loop works**: the framework killed
two of its own claims on the record, kept the correction attached, and never reused the IDs. A
statement paper that shows its own retirements is making a methodological claim it can back.

---

## §11 — Related work · ~800 w

**Projects** — `DDD-frame-13`'s credits, which carry the determinable lineage and the ours/theirs
line: *"The identification of the determinable as demand's object, and of the verdict variable's
support as the determinate-space at grain tau, is ours."*

**Bibliography entering here** (all four verified, Wave 3 `gate1-survey.md` ll. 173–176):
Johnson 1921 · Prior 1949 (both parts) · Funkhouser 2014 · Wilson SEP rev. 2023.

**Carries** — the eight neighbourhoods of §12's list: mixed-initiative systems; human-in-the-loop
and sociotechnical systems; formal verification and proof-carrying systems; bounded rationality
and principal–agent theory; algorithmic accountability and responsibility gaps; cybernetics and
requisite variety; tacit knowledge and expertise; probabilistic programming and adaptive control.
Each entry closes on what the paper takes and what it does not — the measure note's §9 pattern.

**Held** — Q36's pull material (world-pull / ledger-pull; Goodhart as ledger-pull mis-aimed) is
available as positioning prose and deliberately unfiled. **Ruling item 7.**

---

## §12 — Conclusion · ~450 w

**Projects**
| Node | Status |
|---|---|
| `DDD-floor-02` — the relational statement | projected |
| `DDD-frame-15` + `DDD-frame-16` — the compact form: **demand is never unmet, only ungoverned** | projected ×2 |
| `DDD-frame-14` — the two registers | projected |

**Carries** — what is established and what is projected, separated explicitly; Decision-Driven
Design as the engineering corpus the research program was abstracted from.

**The central sentence.** The compact form is the conjunction of `DDD-frame-15` and `DDD-frame-16`
per the rev18 booking — it is not either claim alone, and the paper attributes it to both.

---

# The two authored sections

Both author **prose, not claims**. Where either wants a canon node, the paper states the material
register-native and flags the pending filing **at the point of use** — the measure note's §8
pattern, and `DDD-dec-26`'s stronger instruction to mark non-canon in line. Nothing is filed. The
ideal ending state is the measure note's: **one pending-node flag, and it is the genuinely open
one.**

## A. The closure taxonomy — §5.x · ~650 w

*Outlined on the survey §6.1 recommendation: §5 opens on the kinds framing as foundation-native
exposition, and the **authored** section is the strength ladder. Re-outlines at this gate if Emil
rules otherwise.*

**The question it answers.** §5's kinds framing asks *which* closure question is being posed.
The ladder asks a different one: **given that we mean operational closure, how much closure does
this predicate have?** The framework's own material already orders the rungs; nothing has assembled
them.

**The four rungs, and the node each rests on**

| Rung | Statement | Rests on |
|---|---|---|
| **Open** | No acceptance procedure over accessible ground at the declared assurance level. The measure does not exist here — there is no verdict function to take the entropy of. Governance still applies: the governance question is well-formed on the total domain. | `term:closure` (by negation) · `DDD-measure-06` · `DDD-frame-11` |
| **Verification-closed** | Adequacy can be *evaluated* within declared resource, latency and confidence bounds. **This is canon's closure.** The measure exists. Producer identity stops being necessary — for the checked property and nothing more. | `term:closure` · `DDD-frame-05` · `DDD-measure-01` |
| **Constructively closed** | The verdict is not merely checkable but **computed by rule** from ground available at the act: a procedure returns the correct output directly and there is no candidate search to price. | **the measure note §8's rung — cited, not restated** |
| **Formally decidable** | The formal special case, reserved by canon and **deliberately last**: it is neither the top of the ladder nor a requirement. Any bounded finite domain is decidable by lookup, and a decidable checker may need infeasible resources. | `term:closure`'s reservation · measure note §8's Availability paragraph |

**Why the order is not a strength ordering in the obvious direction, and why that is the point.**
Decidability sits at the end as a *special case*, not a summit. The rungs that matter for deployed
arrangements are the middle two, and canon says so by reserving *decidable* for the formal case
while defining closure operationally.

**The retirement the ladder walks past — the paragraph that gets the closest read.** `DDD-frame-09`
is retired: closed predicates do **not** make intelligence unnecessary, because verification-closure
bounds nothing about generation (`DDD-frame-06`; `DDD-measure-11` — the measure prices the verdict,
not the search). Constructive closure looks like it re-approaches the retired claim and does not:
where the verdict is computed by rule there is no search left to be expensive, so the premise the
retirement turns on is **absent rather than denied**. The scoped survivor — `DDD-frame-05`'s
producer-independence *for the checked property and nothing more* — is untouched either way. The
measure note argues exactly this; §5.x cites it and states the distinction in one paragraph.

**The pending-node flag, at the point of use.** Canon's closure vocabulary carries no
constructive/verification split: `term:closure` is stated in evaluative terms alone, no claim node
names the stronger rung, and the word *constructive* occurs nowhere in `core/`. The rung is stated
**register-native**, the flag sits with it, and the filing is the **Q-wave's item (Q32)**, already
booked by the discharge session. **This paper files nothing.** Until it lands, the citation basis
is closure, the separation of closure from generation cost, and the measure's silence on search.

**What the section must not do** — it must not present the ladder as canon's taxonomy, must not
imply the framework holds four named closure classes, and must not let *decidable* read as the
strongest thing a predicate can be.

## B. The ground-provenance five-way — §2.4 · ~500 w

*Outlined on the survey §6.2 recommendation: the canon-adjacent five-way, with the prompt's four
fresh names carried as sub-distinctions inside it. Re-outlines at this gate if Emil rules for the
prompt's partition as given.*

**The canon half it builds on**, stated first and cited: *a fact belongs to ground when
information about it can change the resolution or its acceptance status beyond the declared
tolerance.* This is the definition `DDD-dec-26` names as canon's contribution, and it is the
section's only load-bearing claim.

**The five slots**

| Slot | Statement | The prompt's names, carried as sub-distinctions |
|---|---|---|
| **Controlled** | Maintained by the arrangement and enforceable through commitments. | — |
| **Observed** | Read from an external or independently changing system. | **sensory** — read at the act, current by construction; **recorded** — read from a store, current only as of its write. |
| **Inferred** | Estimated from data or a model. | **derived** — computed from other ground already held; **predicted** — estimated about a state not yet observed. |
| **Institutional** | Supplied through rules, conventions, authority, or social practice. | — |
| **Missing** | Relevant information unavailable to the executing arrangement. | — |

**Why the partition matters, and the argument that pays for the section.** A **stored statement
about uncontrolled ground is not equivalent to a current observation of that ground.** Revalidation
cadence should follow drift rate, consequence, consistency guarantee and declared assurance level —
never a universal "read every time" rule. The sensory/recorded sub-distinction is what makes that
argument sharp, which is why the prompt's names earn a place *inside* observed rather than
replacing the slot.

**Where the taxonomy connects to the rest of the paper** — *missing* ground is what makes
`DDD-hyp-02`'s first variable ("relevant ground unavailable to the computational system") a
property of ground rather than of the actor; and *institutional* is the slot §7's accountability
material leans on.

**The pending-node flag, at the point of use.** `DDD-dec-26` rules this taxonomy **ineligible for
minting** — not deferred by preference — because Q27 may restructure the partition and a mint
would fix what Q27 may move. The section is therefore **register-native throughout**, marked
non-canon **in line at the point of use** per dec-26's instruction, with **the institutional slot's
mechanism flagged Q27-gated where it appears** and cited as the Q-wave's item. Institutional
provenance states its mechanism as *pending the trust-decision filing* and does not smuggle it in
early. **This paper files nothing.**

**What the section must not do** — it must not present the five-way as canon, must not state the
institutional mechanism, and must not let the sub-distinctions read as a nine-way partition.

---

# Apparatus (P-4), booked for Gate 4

| Item | Source | Note |
|---|---|---|
| Front-matter pin line | measure note's | *projection of `actor-indexed-determination` at `v5.8.0`*; downstream ref for downstream claim IDs; **measure-note citation held for ruling** (survey §5.1) |
| Bibliography | conventional, every locator verified or flagged | Johnson, Prior, Funkhouser, Wilson enter at §11 (all four verified) |
| **Appendix A** | **generated from the graph, never hand-edited** | wholesale regeneration + **independent re-read by a second script**; verbatim by construction |
| H-set in Appendix A | `projected` status and empty evidence **visible** | so no reader mistakes predictions for findings |
| Numbers | scripts only | this paper should need almost none; cite the measure note's assets, mint nothing |
| Reviewer brief (P-5) | measure note's brief pattern, one page | audience: the framework's natural critic |

---

# Word budget

Estimates, with the count method stated so the Gate 5 figure is comparable: **prose words,
tables excluded**, the measure note's method.

| § | Section | Est. |
|---|---|---|
| — | Abstract | 250 |
| 1 | Introduction: the fixed arrangement | 850 |
| 2 | Actors, arrangements, and ground *(incl. authored §2.4, 500)* | 1,050 |
| 3 | Commitment resolution | 650 |
| 4 | Resolution and assurance | 1,400 |
| 5 | Closure and evaluability *(incl. authored §5.x, 650)* | 1,300 |
| 6 | Actor-indexed irreducibility | 800 |
| 7 | Accountability completeness | 600 |
| 8 | Worked example: code generation | 900 |
| 9 | Predictions and study design | 900 |
| 10 | Limits and boundary cases | 700 |
| 11 | Related work | 800 |
| 12 | Conclusion | 450 |
| | **Total** | **10,650** |

Inside the 8,000–11,000 target. The governing rule is the measure note's, not the band: **as long
as its booked content, reported honestly.** If a section comes in materially over, the overage is
reported at its gate with what bought it.
