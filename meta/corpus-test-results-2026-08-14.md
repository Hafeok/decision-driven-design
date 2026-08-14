# Corpus test — results document (DRAFT, exercise session 2026-08-14)

**Status: DRAFT pending GATE 1 ruling. Nothing here is canon. Nothing here files.**

Session prompt: the corpus test, v2 (rulings baked in), SR-1–SR-10 standing. Interactive
exercise; every gate holds for Emil's ruling. This document is the session's only deliverable
channel; it grows gate by gate.

## 1. Fetch and ref verification (walk step 1)

| Repo | Required ref | State found | Verdict |
|---|---|---|---|
| `actor-indexed-determination` | v5.4.0 | tag v5.4.0 = `a49cab4`, present and an ancestor of the working branch head `6ce7012` | ✔ pinned canon readable at tag |
| `decision-driven-design` | head | branch head `87b28b0` = `origin/main` head | ✔ |
| `product-cli` | head (read-only except this document's channel) | branch head `d506ac9` = `origin/main` head | ✔ |

The downstream pin agrees: `graph/upstream.yaml` pins the upstream at `ref: v5.4.0`, advance
recorded as DDD-dec-16 (downstream) on DDD-dec-15 (upstream). The upstream working branch is
8 commits ahead of v5.4.0 (the measure-paper related-work session); this session reads upstream
canon **at the tag**, not at branch head.

## 2. SR-9 — document identity check: **BLOCKED, holding**

The ground-axes holding note (the 1,375-line / 13,622-word copy) **was not uploaded and exists
nowhere in the three repos**. The session's upload directory contains exactly one file:

| File | Lines | Words | sha256 |
|---|---|---|---|
| `d7ab51bf-promptcorpustest.md` (the session prompt itself) | 127 | 1,210 | `7b6578afbd2d59f6dc946fa1b7405888640601acfecd789f1008f3c0f0f93ef4` |

Searched for any in-repo copy: no file in any of the three repositories matches
`ground-axes` / `ground ax` in name or content. `assessment-ground-axes-rev5.md` (the advisory
assessment) is likewise absent. The only holding notes present in
`decision-driven-design/meta/` are `holding-note-act-cost-2026-08-08.md` and
`measure-note-related-work-2026-08-10.md` — neither contains a §13, §13.10/§13.11, or Q1–Q24.

SR-9's own instruction applies a fortiori: the check was written for a divergent copy; an
absent copy is the limiting case. **Held. Nothing beyond step-1 verification has been run.**

Consequence: Test A's expression vocabulary (the §13 axes, the binary timing predicate's exact
wording), the sample labels U-06 / D-05 / D-11, and the Test B act-site labels A-01 / A-02 /
A-03 are all defined only in the missing note (and/or the missing assessment). They are not
recoverable from the repositories.

## 3. SR-2 — sample resolution at head (partial)

| Sample member | Resolves? | Where / note |
|---|---|---|
| DDD-dec-15 (the supersession) | ✔ | upstream `core/decisions/DDD-dec-15.yaml`, present at tag v5.4.0; escape-mechanism re-scope, ruled 2026-08-13 |
| DDD-dec-14 (the open decision) | ✔ | downstream `core/decisions/DDD-dec-14.yaml`; identity-unit question, filed OPEN, owner Emil |
| F-batch representative | ◐ candidate-resolvable | The F-batch (F-1..F-6 falsifier repairs) is real: referenced in `product-cli/docs/ddd-m8-report.md`, `docs/audits/provenance-2026-08.md`, and ledger change-sets (e.g. `01KZX70S86…`, the revisit_if ruling; `01KZTGHF4B…`, the watched-edge decision). Double coverage exists: the `.ddd` register's decisions are mirrored as `dec:hafeok.ddd/…` in the ledger. **Which representative was previously approved is stated only in the missing inputs.** |
| U-06 (multi-line probe) | ✘ | label absent from all three repos |
| D-05, D-11 (contestable store assignment) | ✘ | labels absent from all three repos |
| one plainly judgement-mediated delivery | ◐ | selectable from the registers once the vocabulary is in hand; no blocker beyond the note |

Registers available at head, for scale: downstream `core/decisions/` 12 decisions; upstream
`core/decisions/` 4 (DDD-dec-08, -09, -12, -15); `product-cli/.ddd/decisions/` 46;
`product-cli/.decisions/` ledger 93 declared decisions across 186 change-set files. The 8–12
row sample is comfortably drawable — but not confirmable — without the note.

No substitution is proposed. SR-2 forbids substituting because a decision expresses badly;
these members fail to *resolve*, which is a different failure, and the remedy (Emil re-supplies
the note, or names the members directly) is Emil's to choose, not mine.

## 4. SR-3 — Test B act-sites: **not confirmable**

A-01 / A-02 / A-03 appear nowhere in the three repositories. If they name canon sessions
(candidates visible in the history: the escape reconciliation session behind v5.4.0, the Wave 2
curation session behind v5.3.0, the measure-paper related-work session on the upstream branch —
each with gates, rulings, and PR trails that would support a delivered-set versus emitted-proxy
reconstruction), the mapping is a guess, and the standing rule is flag, don't guess. Per-gate
selections for A-02/A-03 are therefore not argued yet. Held for the note or for Emil's naming.

## 5. SR-6 — axis registries as they exist today: **none** (expected: none — confirmed)

Searched all three repositories for `axis registry` / `axis-registr` / `axes registr` in names
and content: zero files. The upstream term registry (`core/graph/terms.yaml`) contains zero
occurrences of "axis". The `.ddd` store has no axis artefact; the ledger has none; no
`meta/` document carries one. After fourteen months of practice there is no axis registry
anywhere — SR-6's premise holds at head, verbatim. Every axis Test A uses will be invented in
this session's table, and the invention cost is the adoption cost.

## 6. SR-7 — acceptance status: **head has moved past the ruling's numbers**

SR-7 describes ~79 `product-cli` ledger rows pending Emil's manual `ledger accept`. At head
that population has collapsed: **91 of 93 decisions carry an acceptance** (signed
`emk@delegate.dk`); exactly **2 remain pending**:

1. `dec:hafeok.ledger/01KZXJX693…` — "ledger accept --group|--set batches the act, never the
   signature …" (the group-acceptance semantics decision)
2. `dec:hafeok.ddd/01KZTGGX5A…` — "The 24 undeclared What boundaries stay undeclared; exposure
   accepted until review"

The branch head is itself the merge of the `ledger-accept-group` PR (#42) — the batch accept
SR-7 was written in anticipation of has landed. The accepted/pending column will still be
carried on every row, but the "pending rows evidence authoring habits" population is now two
rows, and any synthesis over it will be reported as such rather than as a population. Flagged
for the Gate 1 ruling: SR-7's separate-populations reading survives, but its evidential weight
does not, unless Emil wants the pre-accept state read from history instead (the ledger's
append-only log makes the pre-#42 state reconstructable at a chosen ref — a possible amended
instruction, not taken without ruling).

## 7. Gate 1 holds — questions for Emil

1. **The ground-axes holding note and `assessment-ground-axes-rev5.md` are absent.** Re-upload
   the note (SR-9 runs on receipt, before anything else), or rule an alternative.
2. **U-06, D-05, D-11, and act-sites A-01/A-02/A-03** resolve only through the note — confirm
   they arrive with it, or name them directly.
3. **SR-7 population collapse** (2 pending, not ~79): read the two populations as found at
   head, or reconstruct the pre-accept state from the append-only log at a ref Emil names?

---

# Gate 1 re-report (after Emil's ruling, 2026-08-14)

Emil's Gate 1 ruling: inputs re-supplied; the planning-pass labels (U-06, D-05, D-11,
A-01/A-02/A-03 as previously used) **voided, not reconstructed**; act-sites named directly;
the Test A sample to be proposed by the session under SR-2's constraints; SR-7 read as found
at head with acceptance dates recorded; upstream read at the v5.4.0 tag approved.

## 8. SR-9 identity check — **PASSED**

| Criterion | Expected | Found |
|---|---|---|
| Line count | 1,375 | 1,375 |
| Word count | 13,622 | 13,622 |
| sha256 | `5d8aede1…` | `5d8aede1b97941b38d5eac5966c5b1fe1add3f9a55a08971e01da34fa8e398cb` |
| §13.10 present | yes | yes (`### 13.10 The per-act proxy predicate`, line 1243) |
| §13.11 present | yes | yes (`### 13.11 Proposed sequence`, line 1320) |
| Q1–Q24 present | all | all 24 resolve (Q1–Q24, no gaps) |

Upload: `d744c219-holdingnotegroundaxesrev5copy.md`. The note self-identifies as revision 8,
dated 2026-08-13 — consistent with SR-9's warning that revision labels diverge across copies
while content identity does not; identity is recorded by content, above.
`assessment-ground-axes-rev5.md` also received (advisory except where a standing ruling adopts
it). Both read in full before this re-report.

## 9. Test B act-sites — as ruled, with per-gate selections

| Act-site | Session | Record | Depth |
|---|---|---|---|
| A-01 | escape reconciliation (v5.4.0) | upstream PR #8 (merge `3bf739e`, tagged v5.4.0), downstream PR #19 (merge `87b28b0`); DDD-dec-15/16 | every gate (deep case) |
| A-02 | Wave 2 canon curation (v5.3.0) | upstream PR #7 (merge `1db6772`, tagged v5.3.0), downstream PR #15 (merge `bab62f3`); DDD-dec-11/13/14 here, DDD-dec-12 upstream | one gate |
| A-03 | measure-note revision | downstream PR #17 — **flag below** | one gate |

**A-03 flag (flag, don't guess).** Downstream PR #17's branch is
`claude/measure-note-completion-ve5i1c`; PR #18's branch is
`claude/measure-note-revision-75wr59`. Emil's ruling reads "the measure-note revision session
(PR #17)" — the number points at #17, the descriptor at #18. Provisional reading: the number
governs (#17), held for one-word confirmation at the Gate 1 hold.

**Gate selection for A-02, proposed: the gate at which DDD-dec-14 was filed open (GATE F per
its `made:` field).** Argument: it is a *minting* gate — a decision entered the register there,
open, in-session — so the delivered-governing-set versus emitted-proxy comparison lands on a
decision that is also a Test A sample row, letting the two tests cross-check at one site; and
gates that mint decisions are where improvisation beyond the delivered set would be most
consequential if it occurred.

**Gate selection for A-03, proposed: the session's closing gate (the final ruling/gate-pass).**
Argument: A-01 covers every gate and A-02 covers a mid-session minting gate, so the remaining
probe buys most variance at a *closing* gate, where an emitted proxy has had the whole session
to drift from the delivered set — the best single site to observe accumulated improvisation.
Together the three sites sample opening-to-close without expanding the act count (SR-3).

## 10. SR-7 as found at head, acceptance dates recorded

Acceptance-date histogram over all 93 ledger decisions: **12 accepted 2026-08-11** (the
long-standing population), **79 accepted 2026-08-13** (the batch — PR #42, `ledger accept
--group`), **2 pending**. The batch date keeps the original ruling's authoring-habits signal
legible without archaeology: every sampled row below carries its acceptance date, and the
three populations (pre-batch / batch / pending) are read separately in synthesis. The
population collapse itself (79 pending → accepted between the ruling's drafting and this
session) is recorded here as a finding about the corpus's own cadence.

## 11. Proposed Test A sample (for ruling at the Gate 1 hold)

Eleven rows — within SR-2's 8–12. Registers: upstream 2, downstream 3, product-cli 6 (of
which the F-batch representative and the no-unwrap gate are dual-register: `.ddd` file plus
ledger row). Constraint coverage stated per pick.

| # | Decision | Register | Status / date | Why this pick |
|---|---|---|---|---|
| 1 | `DDD-dec-15` | upstream (at v5.4.0) | ratified canon | **Ruled in (SR-2): the supersession.** Re-scopes a term and a claim by superseding a universal quantifier — the hardest position/timing case in canon. |
| 2 | `DDD-dec-09` | upstream (at v5.4.0) | ratified canon | The boundary charter (R4). A definitional charter whose region is plausibly *universal* — probes whether region vocabulary degenerates on charter decisions or a universal region is expressible. **Contestable store assignment (pick 1):** a filing rule enforced partly by validators, partly by judgement in session. |
| 3 | `DDD-dec-02` | downstream | ratified canon | **Plainly judgement-mediated delivery (ruled in):** papers-before-tool sequencing. No mechanical carrier exists — it reaches an act only if a session recalls the queue. The clean middle-row (Q16) specimen. |
| 4 | `DDD-dec-14` | downstream | ratified canon, OPEN | **Ruled in (SR-2): the open decision.** Deliberately unresolved with a conditional transfer note — probes Q3's `open` state and question 1 (inert/open collapse). |
| 5 | `DDD-dec-16` | downstream | ratified canon | The pin advance. Its standing effect is a mechanically-checked pin (`upstream.yaml`, E12/E13/W5) while the advance itself was a governed judgement act. **Contestable store assignment (pick 2):** rule or judgement depends on which act you index from — Q21 (pinning) made flesh. |
| 6 | `dec/ddd/rust-class-enforced-here` = `dec:hafeok.ddd/…PV4CM246FBEPP9V7RN5` | `.ddd` + ledger | accepted 2026-08-13 (batch) | **F-batch representative.** One-line argument: it is the register's only *experiment*-typed decision (F-7f in the basis-quality audit), so it exercises Q6's authored-basis carve — exploration versus incident — which no other candidate touches; and it carries the ruled double coverage (`.ddd` file + ledger row). |
| 7 | `dec/rust/no-unwrap` = `dec:hafeok.ddd/…GTKM7T8Y6GY78TGJRNB8` | `.ddd` + ledger | accepted 2026-08-13 (batch) | The cleanest mechanically-delivered standing decision: `clippy -D unwrap_used`, delivered per act with no judgement — and the check runs **after** the act, the mechanical store's defining position. **The direct SR-5 probe**: if the binary predicate misclassifies this row, that is SR-1's point on data. **Contestable store assignment (pick 3):** filed as claim, reads as constraint (F-7b). |
| 8 | `dec:hafeok.ddd/…GGX5ABSQ2PVTQ32NPKVNE` | ledger | **PENDING** | "The 24 undeclared What boundaries stay undeclared; exposure accepted until review." Risk-acceptance — probes Q4's hardest carve (accepted risk realising is not an incident) and the pending population. |
| 9 | `dec:hafeok.ledger/…XJX693301CZSY4XNP643XY` | ledger | **PENDING** | "accept --group batches the act, never the signature." Governs the acceptance mechanics themselves; mechanically enforced inside `ledger-cli`'s own gate — self-referential delivery, and the second pending row. |
| 10 | `dec:hafeok.ddd/…GHF4B718YCRCKCGVM7XWA` | ledger | accepted 2026-08-13 (batch) | The watched-edge / `revisit_if` decision. Its content *is* a revisitation trigger — the direct probe of Q14 and open ruling 8 (does `revisit_if` collapse into a declared tolerance on a ground assumption?), and a likely consumer of graph/temporal predicates (question 5). |
| 11 | `dec:hafeok.ledger/…NF77DK5F2FA25EVYR60TD3` | ledger | accepted **2026-08-11** (pre-batch) | "A set's tolerance is a floor … a below-floor state is unconstructible rather than policed." Delivery *by construction* — refusal at entry, Q21's constraint mechanism in its strongest form — and the sample's one pre-batch acceptance, so all three acceptance populations are represented. |

Ledger-primary rows: #8, #9, #10, #11 — four, per the ruling's "3–4"; #6 and #7 sit in the
`.ddd` register with ledger mirrors and fill the F-batch and mechanical-delivery slots.
Nothing here was selected for expressing well; #2, #5, #7 are expected to resist, and that
expectation is why they are in.

**Held at the re-opened GATE 1 for Emil's ruling on: the sample (11 rows), the A-02/A-03 gate
selections, and the A-03 PR number flag.**

— end of Gate 1 re-report —

---

# Gate 1 closed (Emil, 2026-08-14): A-03 = PR #17 (the number governs; descriptor recorded as
wrong); both gate selections approved; the eleven-row sample approved without substitution;
SR-7 populations confirmed 12 / 79 / 2. Recorded per the ruling: upstream contributes only 2
of 11 rows because upstream decisions are constitutionally rare — that asymmetry is itself
weak evidence about where decision volume lives, and Gate 4 must say so rather than let the
ratio pass unremarked.

# Test A — the expression table (working draft, grows row by row)

## Vocabulary used, fixed before the first row

- **Store** (canon, `term:store` at v5.4.0): `{rule, check, actor, nothing}`. Positions from
  `core/02`: encoded/rule = *before*, as a constraint; mechanical/check = *after*, as a
  criterion; judgment/actor = *during*, by an actor reading ground. `core/02` line 78
  explicitly permits one decision held in more than one store — "a constraint before *and* a
  criterion after… defence in depth" — which bears on the counterexample channel and is
  recorded here before any row is classified.
- **Timing** (SR-5, primary): the store's supply position — *before* / *by-the-act* / *after*.
  Where a decision is held in two stores, both positions are recorded, dominant first.
- **Binary (derived column)**: the note's §13.2 predicate — *is the resolution complete before
  the act, or does the act complete it?* Recorded per row; losses against the three-way are
  the SR-5 finding.
- **Region**: named axes plus a region predicate. Every axis is invented (SR-6); each is
  logged in the axis registry (§ below) with the SR-4 quality mark: **resolvable** (an
  extractor's predicate closes over it at act time) or **nameable** (statable, not
  mechanically evaluable).
- **Delivery** (Q16/Q18): mechanical / judgement-mediated, **per act-site** (edge colouring,
  §13.6). Presumed-discharge sites named where observed.
- **Time**: active working time to express the row (analysis, verification against source,
  writing). Caveat declared now for the Gate 4 cost note: this is agent working time in an
  environment with the repos in hand, not human hand time; the two are not interchangeable
  and the cost criterion will be read with that stated.

## Row 1 — `DDD-dec-15` (upstream, ratified at v5.4.0; the supersession)

**Acts governed.** Canon edits and citations touching escape vocabulary from 2026-08-13
onward: any act writing or citing `term:escape-mechanism`, `DDD-floor-01`, `DDD-cost-05`,
`DDD-cost-08`, or the corrected prose sites (11 §3/§6/§7/§8, 05 §6/§7, 10 §5), upstream and —
via the pin — downstream.

**Store.** `rule` — the corrected scope is encoded in `terms.yaml` and the claim files;
canonical text governs, prose is exposition. Fits exactly one cell.

**Region.** Axes: `artefact-path` (resolvable — diff paths against the enumerated corrected
sites), `term-reference` (resolvable — canonical term IDs are grep-able tokens in any diff or
citation). Predicate: *act touches a listed artefact-path ∨ act's content references
term:escape-mechanism / DDD-floor-01 / the overflow∩open form*. An extractor closes over
both axes today.

**Timing.** before (rule). **Binary:** before — no loss on this row.

**Delivery, per act-site.** Upstream canon sessions: judgement-mediated (the agent must fetch
the claim; `Basis:` commit lines are the protocol; the validators check structure, not the
corrected semantics — misapplication per Q16 remains possible). Downstream: the pin's
mechanical channel (E12/E13/W5) demonstrably did **not** deliver this correction — the pin
instruments status, not statement, and DDD-dec-16's resolution says in terms the checks
"would have carried this repository forward against a superseded statement without a word".
That is **presumed discharge** (Q18) observed verbatim in ratified canon: the artefact
recording the pass is identical to the artefact recording the skip. Delivery of the
correction downstream was judgement-mediated (a governed advance).

**Expresses fully?** Yes. The row needed no invention beyond the two axes; the delivery
vocabulary did real work (the presumed-discharge reading of W5's silence is *more* precise
than the prose it summarises). **Time:** ~14 min.

## Row 2 — `DDD-dec-09` (upstream, ratified at v5.4.0; the boundary charter — expected to resist)

**Acts governed.** Filing acts in both canon registers: creating, relocating, or re-scoping a
claim or term — the act of deciding *where* a statement lives.

**Store.** `rule` — the sorting test is encoded ("does the statement require anything to
persist between acts?"). Fits one cell.

**Region.** Axes: `act-kind` (resolvable — the act creates/moves a file under `core/claims/`
or `core/graph/` in either repo), `canon-registry` (resolvable — which repo). Predicate:
*act-kind = claim/term filing ∧ canon-registry ∈ {upstream, downstream}*.

**The resistance, materialised as predicted — but not where expected.** The region expresses
and an extractor closes over it; what the region does *not* carry is the decision's content.
The charter's discriminating input — is the statement synchronic or diachronic? — is not a
coordinate of the act; it is the input to the decision's own verdict, and it is
judgement-evaluable (no extractor reads "quantifies over persistence" off a diff). Logged in
the registry as `statement-temporality`, **nameable**, with the finding: **charter decisions
have low-information regions; their content lives in the predicate, and the region vocabulary
was never designed to carry it.** This is a nameable class, not a diffuse failure: expression
succeeds, but the expressive payload sits in Q24's predicate node, not in Q2's region. The
proposed vocabulary survives only because the note carries both.

**Timing.** before. **Binary:** before.

**Delivery.** Judgement-mediated at every site — no validator evaluates temporality; the
charter reaches a filing act only if the session recalls it. Misapplication is live (Q16
middle row): DDD-dec-09's own notes record a *correctly governed pre-charter* basis to
distinguish it from misapplication, which is the kind of distinction only judgement carries.

**Expresses fully?** Yes, with the low-information-region finding recorded. **Time:** ~18 min.

## Row 3 — `DDD-dec-02` (downstream, ratified; the plainly judgement-mediated delivery)

**Acts governed.** Work-selection acts in the programme, 2026-07-28 → paper-1-ships: tool
building beyond the markdown scaffolding and the validator is deferred.

**Store.** `rule` (a filed policy). Fits one cell.

**Region.** Axes: `work-target` (resolvable — an extractor classifies a session's diff by
path/artefact class: graph-tool implementation vs paper vs scaffolding), `milestone-phase`
(resolvable — paper-1-shipped is readable from the repo, exactly as DDD-dec-06 later used a
CHANGELOG/consolidated-state entry as its execution verification). Predicate: *work-target =
tool-implementation ∧ milestone-phase = before-paper-1-shipped* → defer.

**Timing.** before. **Binary:** before.

**Delivery.** Judgement-mediated at every act-site, with no mechanical carrier even possible
at the time: no hook, no CI, nothing intercepts a session that starts building the tool. The
decision reaches an act only through prompt text or recall. This is the clean Q16 middle-row
specimen the sample needed, and its failure mode is the note's: an act violating it would
leave the register looking exactly as it does when things work.

**One further observation, recorded for the table not for a verdict.** The `reviewTrigger`
field ("Paper 1 stalls past its estimated week by a wide margin") is a proto-`revisit_if`: a
declared ground assumption (the estimate) with a tolerance — but the tolerance ("wide
margin") is nameable, not resolvable. The register was already reaching for Q14's mechanism
in July, without the vocabulary.

**Expresses fully?** Yes. **Time:** ~11 min.

## Row 4 — `DDD-dec-14` (downstream, ratified, OPEN)

**Acts governed.** Any product-cli or L-track act bearing on the claimant-identity unit: the
act must cite DDD-dec-14 and must not resolve the question.

**Store — two levels, and the vocabulary keeps them apart.** The *second-order* decision
(hold the question open; cite, don't resolve; transfer on a named condition) is `rule`,
filed, fits one cell. The *first-order* question (which identity unit?) has **no store
assignment because it has no resolution** — and that is not escape: it is Q3's `open` state,
declared, deliberately unresolved, under observation, owner named. Without the four-state
typing this row is unclassifiable except as a spurious `nothing`; with it, the row expresses.

**Region.** Axes: `track` (partially resolvable — ledger crates and `.decisions/` paths
classify most acts), `question-topic` (**nameable only** — "does this act bear on the
identity unit?" closes for no extractor; the first genuinely judgement-evaluable axis in the
table). Predicate: *track ∈ {product-cli L-track, calibration-ledger work} ∧ question-topic =
identity-unit* → cite, do not resolve.

**Beyond-region machinery required (question 5 will cite this row).** The transfer note —
"transfers when a Decision Ledger PRD exists in a repo Emil designates" — is not a region
over axes; it is a **conditional home**: an event-triggered predicate over future repo state.
Simple axis regions do not express it; Q24's predicate node (specification separate from
executability) does.

**Timing.** Second-order rule: before. First-order question: **the timing predicate is
undefined — there is no resolution to time.** The three-way column reads `—(open)`; the
binary column can only say *not-before*, which would file the row with occasioned resolution
and escape and thereby erase exactly the declaredness that makes it open. **This is a real
SR-5 loss, on the sample's first open row: the binary predicate has no value for `open` that
does not misread it.**

**Delivery.** Judgement-mediated; nothing intercepts an edit that quietly resolves the
identity unit.

**Expresses fully?** Partial — expressible only with Q3's state vocabulary and Q24's
predicate machinery alongside region/timing/delivery; timing is undefined at the first-order
level. The failure is a **nameable class: open decisions have no resolution to time.**
**Time:** ~20 min.

## Row 5 — `DDD-dec-16` (downstream, ratified; the pin advance — expected to resist)

**Acts governed.** Standing: every downstream act consuming upstream escape vocabulary, and
every validator run resolving the pin. Occasioning act (past): the advance itself, governed
by `upstream.yaml`'s header rule ("advancing a pin is a decision").

**Store — the contest, and its resolution.** The standing pin is `rule` (encoded, literal
data in `upstream.yaml`); the validator (E12/E13/W5) is `check` — after, as a criterion. Two
carriers. Canon resolves the contest before it starts: `core/02` line 78 permits a decision
held as "a constraint before *and* a criterion after" as defence in depth, and Q21
independently requires the same split (the pin is the commitment; the check that the pin
holds is the assurance gate; "two objects, and they should not be filed as one"). Assignment:
**rule, with a check-after gate over part of its surface** — recorded as canon-licensed
dual holding, *not* as a two-cell counterexample. The counterexample channel stays empty on
this row, with the note that SR-1's "fits two" wording and canon's defence-in-depth clause
need reconciling at Gate 4.

**Region.** Axes: `canon-registry` (resolvable), `artefact-path` (resolvable — apparatus
docs, claims citing escape), `pinned-id` (resolvable — the pin list is literal). Predicate:
*registry = downstream ∧ (act touches a pinned id ∨ act cites escape vocabulary)*.

**The named exposure is region vocabulary already in use.** The four apparatus documents
building on the mechanism with no pin are, in Q3 terms, a **declared uncovered region under
observation** — filed in the decision's own notes, deliberately unbundled. The register was
again reaching for the note's vocabulary before it existed.

**Timing.** before (rule); the gate's position is after. **Binary:** before — and here the
derived column starts to blur: it reads identically for the pin (whose mechanical check runs
after) and for row 3 (which has no mechanical carrier at all). The three-way plus delivery
columns keep those apart; the binary alone cannot.

**Delivery.** Split across the decision's own surface, per path: mechanical for the
instrumented half (id existence, embed divergence, status movement — CI-run, after), and
judgement-mediated for the statement-moved half, where the decision itself documents the
mechanical channel's presumed discharge (see row 1). One decision, one region, two delivery
types by path — §13.6's edge-colouring claim ("a path is only as mechanical as its weakest
edge") instantiated in ratified canon.

**Expresses fully?** Yes — and the row that was expected to resist instead produced the
table's richest expression, *because* the vocabulary's two-object splits (Q21, store-vs-gate;
delivery-per-path) are exactly what the decision's own prose spends paragraphs doing by hand.
**Time:** ~19 min.

## Row 6 — `dec/ddd/rust-class-enforced-here` (F-batch representative; experiment; accepted 2026-08-13, batch)

**Acts governed.** From the Rust adapter's fixture acceptance onward: contract-surface edits
to this workspace's Rust sources, via the MCP write path — rejected until a seam declaration
covers them. Simultaneously an experiment: the acts it governs are the first live reading of
the friction falsifier.

**Store.** `rule` (the `intercept_by_class.code: enforce` config) with a `check` gate (the
write-interceptor evaluates the applied edit and restores on an undeclared boundary) —
canon's defence-in-depth holding again; assigned rule-with-gate, one decision.

**Region.** Axes: `repo` (resolvable), `artifact-class` (resolvable — declared by the
adapter), `edit-kind` (resolvable — the contract-surface classifier is *implemented*, in
`ddd-core/src/surface.rs`; the extractor is running code, not a sketch), `milestone-phase`
(resolvable — adapter shipped). Predicate: *repo = product-cli ∧ artifact-class = code ∧
edit-kind = contract-surface ∧ phase ≥ adapter-accepted* → reject unless a seam declaration
covers the boundary.

**The region carries a recorded granularity defect, in the decision's own words.** The
available axis is `artifact-class`, the intended region was `language = Rust`; both adapters
declare class `code`, so C# is swept in unintentionally — harmless here, priced not paid.
The decision's "granularity limit" paragraph *is* an axis-granularity statement: the register
documented a region/axis mismatch two days before the note named the machinery.

**The Q6 carve expresses.** Basis type `experiment` with the declaration preceding the acts
("adopted to find out", ref `docs/ddd-m6-experiment.md`) — the authored-basis carve between
exploration and incident holds on a real row: acts in this region are exploration, and the
same acts without the declaration would be incident material. The sample's only experiment
row does the work it was picked for.

**Timing.** before (rule); the interceptor's position is after-the-edit within the act
envelope (evaluate, then restore). **Binary:** before.

**Delivery — per act-site, the repo says it itself.** Mechanical at the MCP write path;
**not delivered at the CLI act-site** (`product domain new` is not intercepted; `ddd what
--strict` is the gate there, which is actor-triggered and therefore judgement-mediated under
Q19's trigger test). One decision, two act-sites, two delivery types — the edge-colouring
again, and this time the variance is documented in the consuming repo's own CLAUDE.md.

**Expresses fully?** Yes. **Time:** ~16 min.

## Row 7 — `dec/rust/no-unwrap` (mechanical, after; the SR-5 probe; accepted 2026-08-13, batch)

**Acts governed.** Every Rust code-writing act in the workspace outside the fixture globs: no
`unwrap`.

**Store — the contested assignment, landed.** Filed as a claim, re-typed to constraint
(F-7b); held in **two stores by canon's own licence**: `rule` before (the
`[workspace.lints.clippy]` manifest entry — encoded constraint, and the decision's rationale
says "enforced twice by arrangement") and `check` after (the CI clippy gate). Canon
`core/02:78` names this exact configuration defence in depth. Assignment recorded as
rule+check dual holding; **dominant carrier: check** — the criterion is what actually stops
a violating act, the manifest entry alone stops nothing.

**Timing — where the SR-5 probe fires.** Three-way: **after** (the dominant carrier is a
criterion applied after the act; the rule half sits before). Binary derived column: the
resolution (the criterion's content) was complete *before* any governed act — so the binary
reads **before**. **The derived column here classifies a mechanically-supplied, after-position
row identically with rows 1–3 and 5, erasing the mechanical store's defining position. That
is SR-1's point demonstrated on data, on exactly the row selected in advance to probe it.**
The two predicates attach timing to different events — resolution-authoring versus
determination-supply — and only the three-way carries the second.

**Region.** Axes: `language` (resolvable), `path-scope` (resolvable — workspace members
minus the ignore globs, literal data). Predicate: *language = Rust ∧ path ∈ workspace \
fixtures*.

**Delivery.** Mechanical at the CI act-site (act-triggered, per Q19). At the local
developer/agent act-site the same check is **actor-triggered** (`cargo clippy` must be
invoked), which under Q19's trigger test makes local delivery judgement-mediated even though
the criterion itself is mechanical — the delivery type belongs to the pair, not the check
(open ruling 11's pair reading, holding on data).

**The `revisit_if` edge is Q14 made literal.** DDD-gates-01 pinned at
`reported@2026-08-06` with a content sha256: a declared tolerance on a ground assumption,
mechanically evaluable (status or content movement fires a reopen finding). The register
already implements reading-triggered revisitation for this row.

**Expresses fully?** Yes. **Time:** ~17 min.

## Row 8 — `dec:hafeok.ddd/…PKVNE` — the What-boundaries risk acceptance (**PENDING**)

**Statement.** "The 24 undeclared What boundaries stay undeclared; exposure accepted until
review."

**Acts governed.** None operationally — that is the point. It is a decision *not* to govern:
the 24 boundary contracts remain undeclared, the exposure accepted, a review horizon set.
(Its accepted predecessor `…TCA7` priced the same exposure; this row extends the acceptance.)

**Store — two levels again, resolving cleanly.** The acceptance itself is `rule` (filed, one
cell). The 24 boundary determinations underneath are **not escaped and not governed**: they
are Q3 `open` — declared, deliberately unresolved, under observation with a horizon. Q4's
hardest carve then does its work: if accepted exposure realises at one of these boundaries,
that is *the arrangement working*, not an incident — a distinction the store partition alone
cannot state and the four-state typing states in one word.

**Region.** Axes: `boundary-id` (resolvable — the 24 are enumerated by `ddd what`),
`review-horizon` (resolvable — a date; Q11's weak, task-specific time-as-coordinate).
Predicate: *boundary ∈ {the 24} ∧ now < review-horizon* → exposure accepted.

**Timing.** Acceptance: before. The underlying determinations: `—(open)` — the second open
row, same nameable class as row 4, same binary-column failure (*not-before* misfiles a
declared acceptance with escape).

**Delivery.** Judgement-mediated (a calendar horizon, Q14's weak form; nothing fires it
mechanically).

**Population note (SR-7).** A pending row: authored, gate-clean, awaiting the principal's
signature. What it evidences is authoring habit — the register's authors reach for
risk-acceptance-with-horizon as a native shape.

**Expresses fully?** Yes, given Q3+Q4; without them, no. **Time:** ~12 min.

## Row 9 — `dec:hafeok.ledger/…643XY` — accept-group semantics (**PENDING**)

**Statement (head).** "`ledger accept --group|--set` batches the act, never the signature" —
one invocation, N acceptance records, each signing its own version hash; six rulings make it
safe (enumerated-and-pinned selection, manifest-hash confirm, per-member gate, held members
stop the run by name, …).

**Acts governed.** Batch-acceptance invocations, and code changes to the verb.

**Store.** `rule` before (the six rulings, encoded in the verb) with `check` gates at entry
(manifest hash presented back; per-member gate; refusal on a held member). Much of it is
Q21-constraint style: the unsafe states are refused at entry rather than policed after.

**Region.** Axes: `command` (resolvable — argv, the most literal extractor in the table),
`actor-identity` (resolvable — git-config email, mechanically corroborated; L009 binds
committer to acceptor). Predicate: *command = ledger accept --group|--set* → the six rulings
bind.

**Timing.** before; gates at entry. **Binary:** before.

**Delivery.** Mechanical at the CLI act-site — the verb is the act-site, so delivery is
act-triggered by construction.

**Self-reference, recorded for question 5's evidence later.** This decision's own acceptance
act — it is pending — will be governed by the verb it specifies. The region contains the act
that ratifies it. Expressible, but only because the region predicate ranges over ledger
state, not over a static coordinate.

**Expresses fully?** Yes. **Time:** ~13 min.

## Row 10 — `dec:hafeok.ddd/…M7XWA` — the watched-edge / `revisit_if` ruling (accepted 2026-08-13, batch)

**Statement (two versions — a supersession inside the ledger).** V1 filed the open question
(distinct edge kind, or retire at the F-batch; `watched:` markers meanwhile, never read as
ground). V2 records Emil's ruling: a watched-not-grounding edge **is** a distinct edge type,
`revisit_if` — this claim's death reopens the decision; never inside `based_on`; a status
movement produces a reopen finding, never a basis-loss one.

**Acts governed.** Ontology acts: filing decisions that track a claim without resting on it,
in the `.ddd` register (format 7) and the ledger (spec v1.5 / format 4).

**Store.** `rule` (the edge vocabulary is encoded in the formats; the gate validates the
schema). One cell, with the schema check as its after-gate.

**Region.** Axes: `artefact-kind` (resolvable — `.ddd` decision files, ledger change-sets),
`edge-kind` (resolvable — the syntax distinguishes `revisit_if` from `based_on`),
`format-version` (resolvable). Predicate: *artefact-kind ∈ {ddd-decision, ledger-change-set}
∧ edge-kind = watched-not-grounding* → file as `revisit_if`, never as ground.

**The content is Q14, ratified.** "This claim's death reopens the decision" is an
event-triggered predicate over graph state — a declared tolerance on a ground assumption,
evaluated at read time, pinned with status and content hash (row 7 carries a live instance).
The row is simultaneously *expressible in* the note's vocabulary and *about* that
vocabulary's Q14/open-ruling-8 machinery: the register ruled the mechanism into its ontology
the day the note was finishing. Recorded as table data; the question-2/question-5 readings
wait for synthesis (SR-8).

**Timing.** before. **Binary:** before. The trigger it defines is a *future-conditional* —
"on this claim's death" — which no static region expresses; second beyond-region case after
row 4's conditional home.

**Delivery.** Mechanical at gate/reindex act-sites (the schema and graph stages);
judgement-mediated at authoring sites.

**Expresses fully?** Yes, with the beyond-region trigger noted. **Time:** ~15 min.

## Row 11 — `dec:hafeok.ledger/…60TD3` — tolerance floors unconstructible (accepted **2026-08-11**, pre-batch)

**Statement.** A set's tolerance is a floor; a version may override only upward; a
below-floor state is **unconstructible rather than policed**; effective tier is hashed
content via the floor pinned at version creation; raising a floor strands every member below
it until re-accepted.

**Acts governed.** Version and set construction in the ledger; floor raises.

**Store.** `rule` — in its strongest form: the option space itself lacks the violating
state. No check ever needs to run because no act can produce the state a check would catch.
Fits one cell, and it is the table's purest single-store row.

**Region.** Axes: `artefact-kind` (resolvable — sets, versions), `operation` (resolvable —
create-version, raise-floor). Predicate: *artefact-kind ∈ {set, version} ∧ operation ∈
{create, raise-floor}*.

**Timing.** before — and the row completes the table's timing spread deliberately: row 11 is
before+mechanical (constraint at entry), row 7 is after+mechanical (criterion), row 3 is
before+judgement-mediated. Q21's regulation/constraint split lands here as data: this is
constraint (refusal at entry), and clippy is a criterion after — different mechanisms the
binary column reads identically. **Binary:** before.

**Delivery.** Mechanical by construction at every act-site that goes through the format;
no act-triggered retrieval is even needed, because there is nothing to retrieve — the
resolution is structural. (Nearest thing in the table to §13.7's *internal* standing supply:
no delivery failure mode because there is nothing to deliver.)

**The stranding clause is a graph consequence.** "Raising a floor strands every member below
it until re-accepted" quantifies over membership and acceptance state — a consequence rule
over ledger graph state, the third beyond-region case.

**Expresses fully?** Yes. **Time:** ~12 min.

## The axis registry — first draft (F-1; SR-4, SR-6)

Every axis below was invented in this session; none existed anywhere before it (SR-6,
verified at Gate 1). The invention cost of this registry **is** the adoption cost, carried
to Gate 4. Quality per the applicability note's revised gate: **resolvable** = an extractor's
predicate closes at act time; **nameable** = statable, not mechanically evaluable.

| # | Axis | Forced by (first) | Also used by | Quality | Extractor sketch |
|---|---|---|---|---|---|
| 1 | `artefact-path` | Row 1 (DDD-dec-15) | 5 | resolvable | diff paths vs an enumerated site list |
| 2 | `term-reference` | Row 1 | 5 | resolvable | canonical term IDs grep-able in diff/citation |
| 3 | `act-kind` | Row 2 (DDD-dec-09) | — | resolvable | operation class from the tool/command performing the act |
| 4 | `canon-registry` (repo) | Row 2 | 5, 6 | resolvable | which repository the act writes |
| 5 | `statement-temporality` | Row 2 | — | **nameable** | none closes — judgement reads "quantifies over persistence"; content-in-predicate finding |
| 6 | `work-target` | Row 3 (DDD-dec-02) | — | resolvable | diff paths → artefact class |
| 7 | `milestone-phase` | Row 3 | 6 | resolvable | repo-state milestone markers (CHANGELOG entry, adapter shipped) |
| 8 | `track` | Row 4 (DDD-dec-14) | — | resolvable (partial) | path classification; boundary cases leak |
| 9 | `question-topic` | Row 4 | — | **nameable** | none closes — semantic bearing on the identity-unit question |
| 10 | `pinned-id` | Row 5 (DDD-dec-16) | — | resolvable | literal pin list |
| 11 | `artifact-class` | Row 6 (rust-class…) | — | resolvable | adapter declaration; **recorded granularity defect: class ⊋ language** |
| 12 | `edit-kind` (contract-surface) | Row 6 | — | resolvable | classifier implemented in `ddd-core/src/surface.rs` |
| 13 | `language` | Row 6 | 7 | resolvable | file extension / adapter |
| 14 | `path-scope` | Row 7 (no-unwrap) | — | resolvable | workspace members minus ignore globs, literal |
| 15 | `boundary-id` | Row 8 (…PKVNE) | — | resolvable | the 24 enumerated by `ddd what` |
| 16 | `review-horizon` | Row 8 | — | resolvable | a date; Q11's weak time-as-coordinate |
| 17 | `command` (argv) | Row 9 (…643XY) | — | resolvable | argv — the most literal extractor in the table |
| 18 | `actor-identity` | Row 9 | — | resolvable | git-config email, mechanically corroborated (L009) |
| 19 | `artefact-kind` | Row 10 (…M7XWA) | 11 | resolvable | file/record type |
| 20 | `edge-kind` | Row 10 | — | resolvable | `revisit_if` vs `based_on` syntax |
| 21 | `format-version` | Row 10 | — | resolvable | format field, literal |
| 22 | `operation` | Row 11 (…60TD3) | — | resolvable | verb performed on the artefact |

**Registry totals: 22 axes, 20 resolvable (one partial), 2 nameable.** Both nameable axes
come from canon-register rows whose content is semantic (charter temporality, question
bearing); every product-cli axis resolves, which is unsurprising — the corpus source is a
toolchain whose acts are already mediated by extractable artefacts.

**Beyond-region machinery, tallied for question 5 (evidence drafting deferred per SR-8):**
three cases — row 4's conditional home (event-triggered transfer), row 10's future-conditional
trigger (claim-death reopen), row 11's stranding clause (quantification over membership and
acceptance state). Row 9's self-referential region (predicate over ledger state) is a fourth,
softer case.

## Summary table

| Row | Decision | Register | Status / date | Store (canon) | Timing (3-way) | Binary (derived) | Delivery (dominant site) | Expresses? | Time |
|---|---|---|---|---|---|---|---|---|---|
| 1 | DDD-dec-15 | upstream | ratified | rule | before | before | judgement (canon sessions); presumed-discharge case named | full | 14m |
| 2 | DDD-dec-09 | upstream | ratified | rule | before | before | judgement | full (low-information region) | 18m |
| 3 | DDD-dec-02 | downstream | ratified | rule | before | before | judgement (no mechanical carrier possible) | full | 11m |
| 4 | DDD-dec-14 | downstream | ratified, OPEN | rule (2nd-order); —(open) 1st-order | before / **—(open)** | **no honest value** | judgement | **partial — nameable class: open has no resolution to time** | 20m |
| 5 | DDD-dec-16 | downstream | ratified | rule (+check gate, canon-licensed) | before (+after gate) | before | split by path: mechanical + judgement | full | 19m |
| 6 | rust-class-enforced-here | .ddd + ledger | accepted 08-13 (batch) | rule (+check gate) | before (+after gate) | before | mechanical (MCP) / **absent at CLI site** | full | 16m |
| 7 | no-unwrap | .ddd + ledger | accepted 08-13 (batch) | **rule+check dual (canon-licensed); dominant check** | **after** | before ← **SR-5 loss fires** | mechanical (CI) / judgement-triggered locally | full | 17m |
| 8 | …PKVNE What-boundaries | ledger | **pending** | rule (acceptance); open underneath | before / —(open) | no honest value | judgement (calendar horizon) | full given Q3+Q4 | 12m |
| 9 | …643XY accept-group | ledger | **pending** | rule (+entry gates) | before | before | mechanical (verb = act-site) | full | 13m |
| 10 | …M7XWA revisit_if | ledger | accepted 08-13 (batch) | rule (+schema gate) | before | before | mechanical (gate/reindex) / judgement (authoring) | full | 15m |
| 11 | …60TD3 floors | ledger | accepted **08-11** (pre-batch) | rule (purest single-store row) | before | before | mechanical by construction | full | 12m |

**Failure column, populated:** 11 of 11 rows express; 2 of 11 (rows 4, 8) express only
partially/conditionally, and both failures are the **same nameable class — open decisions
(and open sub-regions) have no resolution for the timing predicate to read.** No diffuse
scatter. The binary derived column loses information on three rows (4, 8: no honest value;
7: after-position erased) and survives on eight.

**Counterexample channel (question 6, status only per SR-8):** empty. No row fits zero
cells. Rows 5, 6, 7 are held in two stores *in canon's own defence-in-depth sense*
(`core/02:78`) — recorded for Gate 4 as a wording reconciliation between SR-1's "fits two"
and canon's licence, not as a counterexample.

**Time: median 15 min/decision** (range 11–20; total ≈ 2h47m of active expression work
across 11 rows), with the declared caveat that this is agent working time.

**Suspicious-speed check (standing note), run.** The expressions averaged ~15 minutes, not
seconds, and the check is passed structurally: every region predicate above names its
extractor or is marked nameable — 20 of 22 axes carry an extractor sketch an implementer
could act on, and the two that do not are marked as exactly that. The predicates are
resolvable in the note's sense, not prose in predicate syntax.

**GATE 2 — holding on the complete table.** SR-8 satisfied: all rows classified, failure and
invented-axis columns populated, timing recorded three-way with the derived binary. No
question evidence drafted yet.
