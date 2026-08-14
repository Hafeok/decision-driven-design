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
