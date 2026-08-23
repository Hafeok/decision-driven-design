# Session manifest — Phase 1a: the discharge partition and `DDD-measure-06` (2026-08-23)

**Session type:** interactive canon curation, four gates, Emil ruling at each. **Nothing merged.**
**Branch:** `claude/phase-1a-claim-repairs-i6ilkv`, both repositories.
**Canon read at:** `v5.9.0` = `bce18fe`, which was also head — head and tag coincided for the
session's whole run, so canon-at-head and canon-at-tag were one object.

---

## 1. What the session did

| Item | Booked as | Done |
|---|---|---|
| **R-1** | the discharge partition | `DDD-frame-15` **retired**; `DDD-frame-17` filed |
| **R-2** | residual discretion, four phenomena | `DDD-frame-02` clause **amended**; `term:residual-discretion` canonical text corrected. **Nothing minted** |
| **R-3** | `DDD-measure-06` | **retired**; `DDD-measure-16` and `DDD-measure-17` filed |
| **R-4** | the closure ladder's axis error | **recorded**, not repaired — a constraint on Q32's filing |

**Two nodes retired, three filed, one amended, one registry entry corrected, one ruling record
(`DDD-dec-30`), four notes-only amendments (`DDD-frame-16`, `DDD-dec-08`, `DDD-dec-19`,
`DDD-dec-24`), three documents re-projected (`core/09`, `core/13`, `core/14`), one release
descriptor proposed (`v5.10.0`).**

---

## 2. The three things worth carrying forward

### 2.1 A dichotomy is not a list, and the difference is the whole repair

`DDD-frame-15` enumerated four loci and asserted there was no fifth. **That is a list, and a list
can be counterexampled** — which is what an external reader did, three times, in one section.
`DDD-frame-17` asks two questions instead: is the resolution determined by standing configuration
and ground together, and if not, is what determines it inside the arrangement's control?
**Exhaustiveness is now provable.**

The consequence is where the claim's *content* now lives. It is no longer in the enumeration, where
it was false. It is in the answerability of the fixing test — and that is where the falsifier points.

### 2.2 A guard that a reader may skip is not a guard

The seam guard was correctly ratified, correctly worded, and **an external reader met it and still
reported the conflict it was written to prevent.** That is a finding about the guard's audience, not
its content — and the repair was not to reword it. Under `DDD-frame-17`, **governance status is not
an axis of the claim at all**. The guard moved from a paragraph to an exclusion the schema enforces.

The naming half is the same lesson: `DDD-frame-15`'s judgment mode and `term:judgment` were **two
objects under one word inside canon**, because the minted term carries an accountability clause a
discharge mode cannot carry. Shared vocabulary across a seam is a standing invitation to cross it.

### 2.3 A compound statement makes a node undemotable

`DDD-measure-06`'s two limbs carried different warrants under one `status` field. **Demoting the
node would have demoted the sound limb, so nobody demoted it** — for five minor versions, in a
repository that reviews its own canon. The defect was not that nobody saw it; it was that the only
available correction was worse than the defect.

`spec/claim-format.md` §2 rule 1 exists to prevent exactly this, and **a rule that is stated but not
checked prevents nothing.** That is the rationale for the freight instrument item, and it is the
most reusable thing the session produced.

---

## 3. Principles ruled, for reuse

| Principle | Ruled at | Where it lives |
|---|---|---|
| **Retire when the statement is wrong; amend when a clause is wrong.** `DDD-frame-15`'s enumeration did not partition, so the statement died. `DDD-frame-02`'s statement stands and its clause did not | GATE 2 | `DDD-dec-30` notes |
| **A basis edge records what a decision was made on. Repointing one at a successor falsifies the record.** Retired nodes keep their inbound basis edges; a note explains, the edge does not move | GATE 3 | `DDD-dec-08`, `DDD-dec-19`, `DDD-dec-24` notes |
| **Canon is not shaped around a projection's convenience.** Where a correct retirement breaks a downstream quotation, the pin waits and the retirement does not | GATE 2 | `DDD-dec-30`, and §5 below |
| **Editing a file is not a licence to close unrelated items in it.** Two `DDD-frame-02` freight items stayed unreleased while the file was open, so the freight session rules them on their own evidence | GATE 3 | this manifest |

---

## 4. Instruments — predictions stated before operations, results after

Predictions were written down before any command ran, per the convention.

| # | Prediction | Result | Held? |
|---|---|---|---|
| P1 | downstream pins unchanged: 67 resolved, 0 basis-loss, **0 content-drift**, 1 shadowed id | exactly that | **yes** |
| P2 | `check-quotations` @ `v5.9.0`: 29 verbatim, 0 failing | exactly that | **yes** |
| P3 | `check-appendix` @ `v5.9.0`: 72 rendered, 72 cited, 0 discrepancies | exactly that | **yes** |
| P4 | `check-quotations` @ **session branch**: **exactly 3 failing** | **4 failing**, 25 verbatim | **no — see below** |
| P5 | `check-appendix` @ session branch: non-zero, at least 4 changed rows | **6 discrepancies** across those 4 nodes (statement *and* status for the two retired) | yes, undercounted granularity |
| P6 | regenerate Appendix A @ `v5.9.0`: zero-line diff | zero-line diff | **yes** |

**P4 failed, and it is the most useful result in the table.** GATE 2 predicted three failing
quotations from a manual scan of block-quote runs. **The checker found four.** The extra is Paper A
line 1208 — the compact form quoted alone, disclosed-partial: *"… demand is never unmet, only
ungoverned." [DDD-frame-15 — closing clause]*.

Two things follow. First, the manual scan was wrong and the run was right, which is the whole
argument for running rather than reasoning. Second, **the missed quotation is the cheapest of the
four to repair, for the reason that makes it interesting: the compact form is the one sentence
`DDD-frame-17` preserves verbatim.** The citation moves and no prose does — the sentence that was
worth preserving was preserved.

**Ruled at GATE 4: this is a finding, not a miss, and it is filed with the instrument** rather than
left in a session record. The fourth quotation is one sentence quoted inline with a disclosure
tail, which is exactly the shape a human scanning for block-quote runs does not see. Manual
enumeration and instrumented enumeration disagreed and the instrument was right — **the opposite
direction from the two defects the paper checkers already carry in their docstrings**, where the
human caught the script both times. Recording only those would misstate the instrument's record in
the direction that gets it retired.

It is also the clearest case for the prediction convention itself. **A prediction that holds tells
you the operation went as expected; a prediction that fails tells you your model of the artefact
was wrong** — which is worth more, and which you learn only if the prediction was written down
first.

Upstream validators, at every gate and at close: `validate-core-order.py` **exit 0, 66 warnings —
59 W1, 7 W2, zero W4**, identical to arrival. 63 claims, 9 decisions, 6 release descriptors valid.

**One warning was introduced and removed rather than tolerated.** At GATE 2, `core/13` §4 cited
`term:commitment-level`, which `core/14` establishes — a genuine forward edge, an escaped seam by
this repository's own rule. The composition now states itself in `core/14` §2, where the term is
established. Warning count back to 66, not 67.

---

## 5. The pin, held deliberately

**`graph/upstream.yaml` stays at `v5.9.0`.** No pin operation ran this session, which is why P1
predicted zero content-drift and got it.

Retiring `DDD-frame-15` rewrites its statement, per canon's retirement convention. Paper A quotes
it — and `DDD-frame-02`'s statement, and `term:residual-discretion`'s canonical text, and the
compact form. **Paper A's revision advances the pin, having first rewritten those four
quotations**, two of which are the very claims the review asks the paper to stop overstating. The
revision pays a debt it owed anyway.

The precedent is `DDD-dec-27`'s: nodes deliberately left unpinned rather than pinned to something
not yet true.

---

## 6. Arrival, and its failure

**Neither review input arrived with the prompt.** Recorded at the bootstrap *before* work, per
`DDD-dec-20` — the sixth instance of `DDD-dec-17`'s class and the first since the convention was
filed to make it visible. Both files arrived after GATE 1 and are filed here with their identity
(349 lines / `1d291a5f…`; 179 lines / `e9650358…`).

**The consequence was carried and then discharged.** Between arrival and GATE 2 the session worked
from the prompt's rendering of the review, cited nothing to the reviewer, and put no review
reference in any claim field. After the inputs landed, every draft was re-read against them. **Two
drafts changed as a result**, both recorded at GATE 2.

**The prompt's own charter was stale in two places**, and the convention is what made that visible
rather than invisible: `term:residual-discretion` was described as unminted (minted at `v5.8.0`),
and the measure note's boundary section was cited as §7 (it is §8 as merged). Emil recorded the
first as his staleness at the GATE 1 ruling.

---

## 7. Errors, recorded on both sides

**The GATE 1 axis error.** The session proposed an `artefact · actor · uncontrolled` split without
checking `term:actor`, which states in terms that *"a thermostat qualifies"* — so the split was
unavailable on canon's own terms and would have classified the review's two hardest cases by fiat.
Emil ratified the disposition without checking the term either. **Recorded on both sides at GATE 2.**

The rebuild on the fixing test is better, and for a reason neither anticipated: **no value on the
axis turns on actorhood**, so `DDD-frame-17` does not inherit the actor admission test's open
circularity that review §6 reports. `DDD-frame-15`'s judgment mode did inherit it. *A repair that
sheds an inherited defect it was not aimed at is evidence the shape is right.*

**The GATE 2 quotation count.** Three predicted from a manual scan; four found by the checker. See
§4.

---

## 8. The review, assessed

The review was correct on both repairs, and the session's own discipline said so independently:
`DDD-measure-06`'s companion projection conceded what the node asserted, and `DDD-frame-15`'s modes
failed their own exhaustiveness on six cases.

**It paid for itself twice more inside one session.**

- **A mechanism the note states less sharply.** §2.1: a fully decidable acceptance predicate can
  admit several acceptable outputs, so no unique output-valued `V` exists until the task supplies a
  tie-breaker, a canonical form, or a declared selection distribution. **This changed a draft** —
  `DDD-measure-16`'s existence condition names the **task class** as supplier rather than the
  predicate because of it.
- **Independent convergence on one boundary from two sections.** §2.1 states the existence
  condition directly; §5 lists *"unspecified acceptance criteria"* among candidate species of
  residual discretion, where it is not discretion at all but an open acceptance predicate — the
  same boundary, reached from the other end, unnoticed. **Booked for the reviewer response**, where
  it is worth more than agreement on a conclusion.

**Where the session declined.** The triage's two "cheap fixes" for R-1 were both answered rather
than adopted: reading the default mode as *undeclared* is the seam-guard crossing, so it is the
expensive option; and requiring that the standing rule not fix the output given the ground is
correct, and is what the recast delivers structurally — **the triage found the right discriminator
and attached it to the wrong shape.**

---

## 9. Deliberately not done

| Item | Why |
|---|---|
| **The decoder repair** (arrangement-relative admissibility, review §3) | Research, not filing. Explicitly out of scope. `DDD-measure-16`'s boundary is recorded in its notes so the research session finds it already drawn |
| **The status/kind separation** (review §7) | A registry change with a wide blast radius and its own session. **Not bundled with the validator gap**, which is a hole in the *existing* schema and is cheap |
| **`term:escape`'s wording** | The reviewer proposes *"ungoverned resolution"*. Settled term, outside booked scope, **booked** with the audience finding attached |
| **The closure ladder** | Paper A prose. **Recorded** as a constraint on Q32's filing so the axis error is not baked into canon |
| **`DDD-frame-02`'s two freight items** | The `[PROPOSED]` Track 1 banner and the duplicated *"One / One"*. The file was open and they stayed shut, on Emil's ruling |
| **The unexpressed abstention** | Deferred with the resistance named on **both** nodes it bears on — `term:act-individuation` and `DDD-frame-16`. If it is not an act while the determinable is determined, that is act-free discharge, which `DDD-frame-16` denies |
| **The pin advance** | §5 |
| **Paper A's four quotations** | Its revision's work, booked |
| **The ground audit, the Q-wave, the primer, the carve, the freight list** | Out of scope, not bundled |

---

## 10. Version proposal — `v5.10.0`, minor

`releases/v5.10.0.yaml` is in the upstream pull request, per `spec/release-format.md`: merging it to
the default branch is what cuts the tag.

**Minor, not patch**, and the reasoning is the repository's own rules rather than a feeling about
size:

- **Two claim statements die and one is amended.** `changed:` moved on `DDD-frame-15`,
  `DDD-frame-02` and `DDD-measure-06`; three nodes are new. A patch does not retire canon.
- **A registry entry's canonical text moves.** `term:residual-discretion` is `draft` and **pinned
  downstream**, so the correction is a content-drift event — the same test the `v5.9.0` bump was
  ruled a minor on, where `term:floor`'s canonical text moving was named as what made it minor.
- **`region` boundaries change on a claim at `established`.** `DDD-measure-16` narrows what
  `DDD-measure-06` claimed *everywhere*.

**Not major.** No spec version changes; `spec/claim-format.md` and `spec/release-format.md` are
untouched. Format 1 descriptors and format 1 claims remain valid unchanged, and every node filed
here conforms to the schema as it stands. The framework's central claims — conservation, the floor,
the store partition — are untouched; what moved is one partition's shape and one boundary's scope.

**`basis` cites nine nodes** including the two retired ones, because a release pins what it retires
as much as what it files.

---

## 11. Pull requests

**Upstream first**, per the session's charter: canon lands before the record that describes it.

1. `Hafeok/actor-indexed-determination` — the canon repairs and `releases/v5.10.0.yaml`.
2. `Hafeok/decision-driven-design` — the session record, the four gate reports, the two filed review
   inputs, and the successor items.

**Neither is merged by the session.**
