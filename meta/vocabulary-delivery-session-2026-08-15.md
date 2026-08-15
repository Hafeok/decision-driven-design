# Vocabulary-and-delivery session — the earned canon session (2026-08-15)

**Status: GATE 1 closed (Emil); holding at GATE 2. Drafts on the feature branches; nothing
merged; every filing pends its gate's ruling.**

Session prompt: `prompt-vocabulary-delivery.md` (four filings, five gates). Interactive canon
curation; every gate holds for Emil's ruling; merge nothing. Evidence base:
`meta/corpus-test-results-2026-08-14.md` at head (merged as PR #20), read in full. This document
is the session's report channel; drafts land as claim/term files on the feature branches and are
recorded here gate by gate.

## 1. Fetch and verification (walk step 1)

| Check | Expected | Found | Verdict |
|---|---|---|---|
| `actor-indexed-determination` | canon read at tag v5.4.0 | tag v5.4.0 = `3bf739e`, ancestor of branch head `6ce7012` (branch head carries the measure-paper session's work — not read as canon) | ✔ |
| `decision-driven-design` | head | feature branch = `origin/main` head `886035b` (the PR #20 merge) | ✔ |
| Holding note identity (SR-9 discipline) | 1,375 lines / 13,622 words / sha256 `5d8aede1…` | 1,375 / 13,622 / `5d8aede1b97941b38d5eac5966c5b1fe1add3f9a55a08971e01da34fa8e398cb` | ✔ exact match |
| `assessment-ground-axes-rev5.md` | received, advisory | received; read in full; advisory only | ✔ |
| Corpus results at head | evidence base | present, 1,261 lines, all five gates closed, earning ruling recorded | ✔ |

Working branches: `claude/earned-canon-vocab-delivery-k4ngl4` in both repositories, per the
session's branch requirement. `product-cli` is not touched.

## 2. The node map — everything the four filings touch or cite

### 2.1 Upstream (`actor-indexed-determination`, read at v5.4.0)

**Terms (in `core/graph/terms.yaml`) — cited, none amended:**

| Node | Status at tag | How the filings touch it |
|---|---|---|
| `term:escape` | settled | F-3's escape generator files *under* it: undelivered governance is escape as `term:escape` already defines it — supplied by nobody, for any reason. Cited, never widened; DDD-dec-15's "no new claim is minted" holding is the model. |
| `term:store` | settled | SR-1's boundary. F-3's filing-is-not-encoding is a correctness condition on *reading* allocation, not a fifth store. Cited as the boundary every delivery claim must state. |
| `term:exhaustiveness` | settled | The "exactly one of" wording. Not touched — the exhaustiveness/defence-in-depth seam stays on the freight list. Cited so the drafts avoid colliding with it. |
| `term:encoded` / `term:mechanical` / `term:judgment` | settled | The three positions (before / after / during) that F-2's `—(open)` extends. The extension is additive — a fourth value for decisions with no resolution to time — and amends none of the three. |
| `term:escape-mechanism` | settled (re-scoped by DDD-dec-15) | Context for F-3: capacity-generated escape is one generator; delivery failure is another route to the same supplied-by-nobody condition. Cited. |
| `term:admission-test` | settled | Q1's diagnostic reading — an artefact naming no axis fails the decision admission test. Cited by F-1. |
| `term:tolerance`, `term:granularity-bound` | settled | Membership in the governing set is fixed by tolerance and the world, not by evaluation — the ground under F-1's "non-evaluation must never silently become non-applicability". Cited. |
| `term:assurance` | settled | F-3's compounding claim cuts across source and assurance identically (Q17). Cited. |
| `term:maturation` | settled | R-2 exposure check target (with core/08's harvest-channel condition, lines 147–155 at tag: "the channel must exist"). Reported on at GATE 3, not amended. |

**Claims — cited or checked, none amended without ruling:**

| Node | Status at tag | How the filings touch it |
|---|---|---|
| `DDD-cost-09` | projected | R-2 exposure check. Its "supplied standing — independent of the act" is exactly the phrasing Q15 qualifies: the paid-once-inherited-by-every-run property belongs to mechanical *delivery*, not to standing supply generally. Candidate weakening — reported at GATE 3, amended only on ruling. |
| `DDD-cost-08` | projected | R-2 exposure check. Two-gate routing; the assurance gate's worth rests on gate independence, which F-3's compounding names the failure of. Its `breaks:` field was already amended by DDD-dec-15. Reported at GATE 3. |
| `DDD-frame-05` | (at tag) | Checked-property independence — credited by DDD-cost-08; F-3's compounding is about the *removal* of independence by shared judgement-mediated delivery. Cited. |
| `DDD-measure-13` | reported | The maturation/funnel asymptote — the formal node nearest the maturation return channel. R-2 exposure check context. |
| `DDD-frame-12` | (at tag) | The return channel at the claim layer ("act-layer machinery — individuation, the two gates, escape, the return channel — applying at the claim layer"). R-2 exposure check context. |
| `DDD-floor-01` | reported | Context only (re-scoped by DDD-dec-15); not touched. |

**Decisions:**

| Node | How the filings touch it |
|---|---|
| `DDD-dec-15` (upstream) | Cited three ways: precedent for supersession-never-rewriting; the recorded escape-generator instances F-3's undelivered generator joins; and the boundary the drafts must respect — its UNVERIFIED block holds the empty-option-set generator (generator 2) open, and nothing this session files may close or crowd that slot. |
| `DDD-dec-09` (upstream) | R4, the boundary charter — the sorting test for every destination below (synchronic upstream; anything persisting between acts downstream). Also F-1 evidence context: the corpus's low-information-region finding on charter decisions. |
| `DDD-dec-12` (upstream) | Not touched (Wave 2 upstream ruling; no filing cites it). |

**Structure:** `spec/claim-format.md` (+ format-2 addendum) — the schema the new claim files
validate under. `core/graph/terms.yaml` — receives any new terms; carries a structural question
flagged in §3.5 below.

### 2.2 Downstream (`decision-driven-design`, at head)

| Node | How the filings touch it |
|---|---|
| `meta/corpus-test-results-2026-08-14.md` | The evidence base. Every filing wires evidence into basis/evidence fields by section reference to this document. |
| `DDD-dec-16` | Evidence for F-3: its resolution records the presumed-discharge instance verbatim (E12/E13/W5 silent while the pinned statement moved — "would have carried this repository forward against a superseded statement without a word"). Cited, not amended. |
| `DDD-dec-14` | Evidence for F-2: the first `—(open)` row; corpus row 4. Cited, not amended. |
| `DDD-dec-02` | Evidence for F-1's axis-type field: the `reviewTrigger` half of the matched pair (nameable → resolvable). Cited, not amended. Date conflict reported in §4.1. |
| `DDD-dec-10` | Process precedent for GATE 5: upstream-first, pin staged against branch head, bumped on acceptance. Also named in the supersession-precedent triple (dec-09/10/15). |
| `graph/upstream.yaml` | GATE 5: any new upstream node a downstream claim rests on gets pinned; pin staged against the upstream branch, bumped on acceptance, per the DDD-dec-16 pattern. |
| `scripts/validate-claims.py` | F-4 finding (§3.4): the only executable statement of the decision-record format, byte-identical in both repositories. Not modified — no tooling this session. |
| `meta/graph-tool-ontology.md`, `meta/way-of-working.md` | The ontology (decision --basedOn--> claim) and status vocabulary the new claims must respect. Cited. |

## 3. Proposed IDs and destinations, per filing

New areas are cheap; renumbering is forbidden; every ID below is a proposal for ruling. Two new
areas are proposed: **`ground`** (the applicability/typing vocabulary — F-1, F-2, F-4) and
**`delivery`** (F-3). Precedent for one area spanning both repositories: `cost`, split per-act
upstream / volume downstream under DDD-dec-09 — `delivery` uses the same licence.

### F-1 — the applicability gate (GATE 2)

| Object | Proposed ID | Destination | Notes |
|---|---|---|---|
| The gate | `DDD-ground-01`, kind normative, status projected | upstream `core/claims/` | Resolvable applicability predicate over declared axes, or explicit universal declaration; non-evaluation never silently becomes non-applicability. Region states the evidenced bound: binds where acts are mediated by extractable artefacts; semantic-content decisions may carry nameable axes with the weaker standing named. Includes the Q19 axis-type field (mechanically-evaluable / judgement-evaluable) as a **maturity state**, per the Gate 4 consequence ruling, with the matched pair as evidence. |
| Evidence wiring | — | — | Corpus: axis registry (22 axes, 20 resolvable one partial, 2 nameable, both semantic canon-register rows); Gate 4 synthesis §2 (91%); §4 Q2 (the matched pair) — with the date correction of §4.1 below. |

### F-2 — the four-state typing with the timing value (GATE 2)

| Object | Proposed ID | Destination | Notes |
|---|---|---|---|
| Four-state typing | `DDD-ground-02`, kind conceptual, projected | upstream `core/claims/` | governed / declared-empty / open / uncovered-undeclared; `open` as a resolution value carrying a deferred verdict. Scoped as evidenced: the corpus exercised `open` twice and `declared-empty` zero times — the declared-empty limb is flagged in the draft, and whether it files now or waits is Emil's GATE 2 ruling (the corpus did not exercise it; its wording sources to the applicability note — see §4.3). |
| `—(open)` timing value | `DDD-ground-03`, kind conceptual, projected | upstream `core/claims/` | An open decision has no resolution for the timing predicate to read; three-way timing plus the fourth value is total over the corpus where the binary was not (binary lost on 3 of 11). Alternative: merge into DDD-ground-02 as one claim — Emil's call; drafted separate so each carries its own falsifier. |
| Evidence wiring | — | — | Corpus rows 4 and 8; summary table failure column; SR-5 hybrid verdict (Gate 2 closure); Gate 4 criterion-1 ruling (11/11 under the fourth value governs; 9/11-plus-one-nameable-class without). |

### F-3 — delivery (GATE 3; the largest filing)

| Object | Proposed ID | Destination | Notes |
|---|---|---|---|
| The vocabulary | `term:delivery`, `term:undelivered`, `term:presumed-discharge` | upstream `core/graph/terms.yaml` | `delivery` as the axis; mechanical / judgement-mediated as values **per act-site** (the edge-colouring — a path is only as mechanical as its weakest edge); `undelivered` as the failure; `presumed discharge` as the record property (a gate's pass meaning never-reached), argued on mechanisability. Structural flag in §3.5. |
| Filing is not encoding | `DDD-delivery-01`, kind conceptual, projected | upstream `core/claims/` | A correctness condition on reading: `I(V;X)` counts what the arrangement supplies at the act; store allocation cannot be read off artefacts. Not a fifth store, not a new axis — SR-1's boundary stated in the claim's own region. Falsifier from the note: ledger-counted and delivery-counted allocation agree across a corpus. |
| Undelivered as escape generator | `DDD-delivery-02`, kind conceptual, projected | upstream `core/claims/` | Governance filed but not delivered = no source supplied the governing decision at the act = escape under `term:escape` (supply-general), citing DDD-dec-15 and joining the recorded generator instances. Distinguishing feature named: the ledger shows coverage — escape that presents as governance. Must leave DDD-dec-15's generator-2 slot untouched. |
| Compounding | `DDD-delivery-03`, kind conceptual, projected | upstream `core/claims/` | Unretrieved decision + unretrieved check over the same act are correlated failures (same actor, same budget, same position), removing the independence a gate depends on. The note's prediction files as the falsifier: mechanise-checks-keep-retrieval-judgement outperforms the reverse, content constant. |
| Maturation retrieval-dependence | `DDD-delivery-04`, kind conceptual, projected | **downstream** `core/claims/` | The diachronic consequence: maturation's paid-once-inherited property holds only where the harvest channel *delivers* at future acts — judgement-mediated standing supply does not amortise reliably. Downstream under R4 (quantifies over persistence between acts). Cites `term:maturation` and the corpus's delivery-failure rows via pin. Alternative ID: `DDD-cost-30` — Emil's call. |
| R-2 exposure check | report only | GATE 3 report | Whether `DDD-cost-09`, `DDD-cost-08`, and the maturation return channel want a named delivery condition. Reported, not amended, unless Emil rules. |

Evidence wiring: delivery type determinable 7 of 7 gates (Test B tally); the A-01 Gate 1
centrepiece with the reflexive chain (Gate 4 synthesis §5); rows 1 and 5's verbatim
presumed-discharge instances; the four-kind improvisation typology with un-annotated
follow-through at 1-in-7.

### F-4 — retro-filing's two fields (GATE 4)

**Finding on where decision-record format lives (reported as the prompt requires):** nowhere as
spec. Upstream `spec/` holds the claim format only; the decision record is defined operationally —
`scripts/validate-claims.py --decisions` (byte-identical in both repositories: principal, basis,
resolution, made) plus register practice, with the ontology in downstream
`meta/graph-tool-ontology.md`. There is no `spec/decision-format.md` in either repository.

| Object | Proposed ID | Destination | Notes |
|---|---|---|---|
| The two fields | `DDD-ground-04`, kind normative, projected | upstream `core/claims/` | A retro-filed decision carries when the gap was uncovered (distinct from when the act occurred) and that it was retro-filed; without them retro-filing launders escape into coverage and the sweep reports clean. Actor-general and register-general, so statable upstream without referencing dependents. Evidence is indirect — no retro-filed row was sampled — flagged in the draft; the filing is cheap and the laundering risk is the argument. Validator/spec enforcement is deliberately **not** done this session (no tooling). |
| Registry seed | artefact file, not canon | downstream `graph/axis-registry.yaml` (alternative: `meta/axis-registry-seed-2026-08-14.md`) | The corpus's 22-axis table seeded as the axis registry's first instance, headed clearly as an artefact seeded from the corpus test, not canon. Location is Emil's GATE 4 call. |

### 3.5 Structural flag — terms without an establishing document

Every existing term in `core/graph/terms.yaml` carries `established_by: <core doc>`. The three
delivery terms have no establishing document — this session files vocabulary, not prose. Registry
precedent exists for terms without canonical_md (five registry-only terms), but not for terms
without an establishing doc. Options for the GATE 3 ruling: (a) registry entries with
`established_by` pointing at the claim that establishes them (a format extension); (b) terms wait
for a future doc projection and the claims carry the vocabulary meanwhile; (c) something Emil
prefers. Flagged now so the GATE 2 drafts can follow the same pattern if F-1/F-2 want terms.

## 4. Conflicts between the prompt's evidence citations and the corpus/repos at head

**4.1 The matched-pair date (real conflict; repo is ground truth).** The prompt (F-1) dates
`reviewTrigger`'s "wide margin" at **2026-07-08**. The repository says `DDD-dec-02` was made
**2026-07-28** (file landed that day in the graph scaffolding session; git history shows no
earlier version). The corpus document itself says "five weeks apart" (Gate 4 Q2) and "five weeks
from nameable to resolvable" (the earning ruling) — but 2026-07-28 to the revisit_if ruling's
batch acceptance (2026-08-13) is roughly two and a half weeks, and to the `reported@2026-08-06`
pin under two weeks. The prompt's date looks back-derived from the corpus's "five weeks". The
evidence itself — the same revisitation slot moving from nameable to resolvable as formats
matured — stands untouched; only the interval is wrong. Proposed handling: the F-1 draft cites
repo dates (2026-07-28 → 2026-08-13) and does not carry "five weeks"; the corpus document is not
amended (it is a ratified record; its error is noted here). **Held for Emil's ruling.**

**4.2 "Eleven ratified decisions" (minor framing conflict).** The bootstrap and prompt describe
the corpus as pricing against eleven *ratified* decisions. The corpus populations are 5
canon-ratified, 3 batch-accepted, 1 pre-batch-accepted, 2 **pending**. Drafts will say "eleven
decisions (five canon-ratified, four accepted, two pending)" where the sample is cited.

**4.3 F-1/F-2 elements sourced from a document this session does not hold (gap, not conflict).**
Four elements of the prompt's F-1/F-2 wording do not appear in the corpus document at head or in
the ground-axes holding note: the exact revised-Q1 statement ("resolvable applicability predicate
… explicit declaration of universal applicability; non-evaluation must never silently become
non-applicability"); **`declared-empty`** as a name and "the applicability note's ruling-2
answer"; the **`Unknown`-is-never-a-pass rule**; and "source coverage, resolution, and assurance
as orthogonal properties". Their source is evidently the ground-applicability holding note
(2026-08-12, unratified — the note DDD-dec-15 cites), which is absent from the package and from
all repositories; the corpus cites it only for the resolvable/nameable definitions ("the
applicability note's revised gate"). Per flag-don't-guess these elements will be drafted exactly
as the prompt states them and **marked in the drafts as resting on the prompt's authority, not on
a document this session verified** — unless Emil supplies the applicability note or dictates
wording at GATE 2.

**4.4 Everything else checks.** 20/22 resolvable (one partial) ✔; every product-cli axis
resolvable ✔; two nameable axes are semantic canon-register rows ✔; binary lost on 3 of 11, with
no-unwrap timing resolution-authoring instead of determination-supply ✔; the two `—(open)` rows
are DDD-dec-14 and the What-boundaries acceptance ✔; delivery determinable 7 of 7 ✔; the A-01
Gate 1 centrepiece and the reflexive chain ✔; four-kind typology with un-annotated follow-through
at 1-in-7 ✔; 11/11 under the fourth value as the governing reading ✔; cost at the bar with
marginal cost falling ✔.

## 5. GATE 1 — holding

For Emil's ruling:

1. The node map (§2) and the proposed IDs and destinations (§3) — including the two new areas
   (`ground`, `delivery`), the F-2 one-claim-or-two question, DDD-delivery-04's repo and ID, and
   the registry seed's location.
2. §3.5 — how terms without an establishing document enter the registry.
3. §4.1 — the matched-pair date conflict and the proposed handling (repo dates in the draft; the
   corpus record left unamended, error noted here).
4. §4.3 — the four elements sourced from the absent applicability note: supply the note, dictate
   wording, or approve drafting on the prompt's authority with the marking stated.

Nothing has been drafted into `core/` in either repository. Drafting begins at the GATE 2 step on
the Gate 1 ruling.

---

# Gate 1 closed (Emil, 2026-08-15) — rulings recorded

1. Node map and both new areas approved; `ground` and `delivery` minted; `delivery` spans repos
   on the `cost` precedent.
2. F-2 stays two claims (DDD-ground-02, DDD-ground-03), each with its own falsifier — typing and
   the timing value fail independently; one claim would weld them.
3. DDD-delivery-04 downstream under that ID, not DDD-cost-30 — area coherence beats
   registry-local numbering; the claim is delivery's consequence for maturation, not cost's.
4. Registry seed: `graph/axis-registry.yaml`, headed artefact-not-canon; machine-read files live
   in `graph/`; `meta/` would misfile it as evidence. Header states validators do not yet check
   it. No validator work this session.
5. Terms establish in a **new minimal upstream core document** at the next free number —
   delivery is an axis of the same rank as timing; registry-only terms would break the
   `established_by` convention. The doc hosts the three delivery terms and the prose homes of
   DDD-delivery-01/02/03; number, title, and skeleton proposed at GATE 3. Minimal — the corpus
   evidence carries the weight; the doc establishes and points.
6. Date conflict handled as proposed: drafts cite repo dates (DDD-dec-02 made 2026-07-28,
   interval ~2.5 weeks); "five weeks" dropped everywhere; the ratified corpus record stays
   unamended. **Erratum, recorded here:** the corpus document's "five weeks apart" (§4 Q2) and
   "five weeks from nameable to resolvable" (the earning ruling), and the session prompt's
   2026-07-08 date, do not match the repository; the interval is roughly two and a half weeks.
   The evidence — nameable maturing to resolvable — stands on the dates that are true.
7. Populations stated wherever drafts cite the corpus: 5 ratified, 4 accepted-not-ratified,
   2 pending.
8. The four applicability-note-sourced elements: the note supplied (announced 362 lines / 2,494
   words, sha256 `4afe380c…`); identity to verify on receipt; the note's wording then governs,
   superseding the prompt's paraphrase; provenance marked in each draft.
9. The generator-2 slot stays untouched.

# Gate 2 — F-1 and F-2 drafts (holding)

## Identity check on the supplied applicability note: **FAILED — ABSENT. Holding.**

The Gate 1 ruling announced the ground-applicability note as supplied now (362 lines / 2,494
words, sha256 `4afe380c…`). It did not arrive. The session's upload directory contains exactly
one file — the original session package zip (`9417eba2-vocabdeliverypackage.zip`, sha256
`b360527a…`, four files, note not among them). Searched: uploads, scratchpad, both repositories,
by name (`*applicab*`), by line count (362), and by hash fragment (`4afe380c`) — the only
occurrence of the hash anywhere is the ruling text itself. An absent copy is the identity
check's limiting case; nothing is reconstructed.

This is the third instance of the reflexive chain the corpus test recorded: the same failure
mode (a governing input announced, not arrived) at A-01's Gate 1, at the corpus session's Gate 1,
and now here — caught each time by an identity check refusing to substitute. Recorded as session
data adjacent to F-3's evidence; nothing files from it.

**Consequence, per flag-don't-guess:** the four note-sourced elements are drafted as the
prompt's paraphrase and carry a `PENDING — Emil review` mark naming the non-arrival; the note's
wording governs on receipt, per the ruling. Everything not resting on the note is drafted in
full.

## Drafts committed (upstream feature branch, commit `83af130`)

**`DDD-ground-01`** (normative, projected) — the applicability gate. Statement: files with a
resolvable applicability predicate over declared axes or an explicit universal declaration; each
axis marked mechanically-evaluable or judgement-evaluable; non-evaluation never silently becomes
non-applicability. Region carries the evidenced bound (binds fully where acts are mediated by
extractable artefacts; semantic-content decisions may carry nameable axes with the weaker
standing named). Evidence: the 22-axis registry (20 resolvable, one partial, 2 nameable, 91%)
and the matched pair at repo dates, with the erratum cross-referenced. Falsifier from the note's
Q1 row; test names the counterexample hunt. The axis-type field files as a maturity state per
the Gate 4 consequence ruling. PENDING mark: the statement's first sentence sources to the
absent note.

**`DDD-ground-02`** (conceptual, projected) — the four-state typing: governed / declared-empty /
open / uncovered-undeclared; only the fourth is a finding; typing classifies ground per region,
not decisions. Evidence: open exercised twice with its distinctive features doing real work
(rows 4, 8; §4 Q1), and the criterion-1 gap (11/11 with, 9/11-plus-class without). Falsifier:
a miss assignable to no single state, or open's features doing no discriminating work.
**FLAGGED for this gate's ruling: whether the declared-empty limb files now or waits** — the
corpus exercised it zero times, and its wording ("ruling-2") sources to the absent note. The
orthogonal-properties framing and the Unknown-is-never-a-pass rule are deliberately kept OUT of
the statement and held in notes pending the note.

**`DDD-ground-03`** (conceptual, projected) — the `—(open)` timing value. Statement: an open
decision has no resolution for a timing predicate to read; the timing vocabulary carries the
fourth value alongside before/during/after; any predicate without it misfiles open decisions.
Additive — none of term:encoded / term:mechanical / term:judgment is amended. Evidence: the two
no-honest-value rows and totality over the corpus; the SR-5 verdict (binary loses 3 of 11,
including no-unwrap's after-position erasure). Breaks: criterion-1's governing reading reverts
to 9/11-plus-class.

## Validation

Upstream, all three validators pass at the draft commit: `validate-claims.py core/claims/`
(42 claims valid), `validate-claims.py core/decisions/ --decisions` (4 valid),
`validate-core-order.py core/` — 0 errors, zero W4, warning profile **identical to baseline:
52 W1, 7 W2** (checked with and without the new files).

## GATE 2 — holding

For Emil's ruling:

1. **The applicability note's non-arrival** — re-supply it (identity re-checked on receipt, its
   wording then governs the four marked elements), or rule the paraphrase sufficient.
2. **F-1 (DDD-ground-01)** as drafted — statement, region bound, maturity-state field, evidence
   at repo dates.
3. **F-2 (DDD-ground-02/03)** as drafted — including the flagged ruling: does `declared-empty`
   file now (per the applicability note's ruling-2 answer) or wait? The corpus did not exercise
   it.

## Applicability note received — identity check PASSED; drafts rebuilt (commit `dd500c3` upstream)

The note arrived after the first Gate 2 report: 362 lines / 2,494 words / sha256
`4afe380ceab252aa29b7579a57fdad94e32792f690e096c2d02a4e74dd34500d` — exact match to the ruling's
announcement. Per the Gate 1 ruling its wording governs the four note-sourced elements; the
prompt's paraphrase is superseded, PENDING marks replaced with provenance marks in all three
drafts ("sourced from the 2026-08-12 applicability note, unratified, filed here on corpus
evidence").

**What the note changed in the drafts:**

- **DDD-ground-01** — statement rebuilt on the note's Q1: "a governing decision must declare a
  resolvable applicability predicate, unless it explicitly declares universal applicability";
  the note's Q1 falsifier adopted (ceremonial universal predicates). The note states the
  predicate abstraction as wider than factored axes, and the corpus's beyond-region tally
  (§4 Q5, ~27–36% needing graph or temporal predicates) is added as evidence for exactly that
  framing. The axis-marking clause (mechanically-evaluable / judgement-evaluable) joins from
  ground-axes Q19 — the note's Q1 does not mention axes — and the join is named in the draft as
  this filing's, required by the prompt's F-1 and evidenced by the corpus.
- **DDD-ground-02** — restated as the note's Q3 **orthogonal typing**: source coverage
  (covered · declared-empty · undeclared · unknown), resolution (resolved · deliberately-open ·
  unknown), assurance (adequate · inadequate · unknown); only `undeclared` a finding;
  `deliberately-open` a resolution value carrying a deferred verdict; `Unknown` never a pass.
  The corpus's four-state exercise maps in the draft's notes (governed ↔ covered ∧ resolved;
  inert ↔ declared-empty; open ↔ deliberately-open; uncovered-undeclared ↔ undeclared) with the
  honest limit stated: orthogonality itself is only partially exercised (rows 4 and 8 vary
  resolution independently of coverage; assurance was not varied).
- **DDD-ground-03** — subject updated to "resolution is deliberately-open"; otherwise as
  drafted.

**Two new findings for this gate's ruling:**

- **The two notes conflict on Q3's shape, and the later-dated note carries the superseded
  form.** The applicability note (2026-08-12) replaces the first draft's four states with the
  orthogonal axes; the ground-axes note as packaged (revision 8, 2026-08-13 — the corpus
  session's source) still carries the four states. The prompt and the Gate 1 ruling follow the
  applicability note; recorded in DDD-ground-02's notes, not harmonised. A structural
  observation is recorded alongside, not asserted: the orthogonal split answers the ground-axes
  note's inert/open collapse question by construction — they sit on different axes.
- **"Ruling-2" has no answer to point at.** The prompt's declared-empty flag reads "per the
  applicability note's ruling-2 answer", but the note's ruling 2 is an **open question** — "is
  declared-empty a decision kind, a resolution value, or a conventional applicability record?"
  So the Gate 2 ruling on declared-empty is now two-part: does it file now or wait (corpus
  exercised it zero times), and if now, in which of the three shapes?

Validators re-run at the redraft commit: 42 claims valid; core-order 0 errors, zero W4, warning
profile identical to baseline (52 W1, 7 W2).

**Still holding at GATE 2** for: F-1 as redrafted; F-2 as redrafted; the declared-empty two-part
ruling; and the ground-01 join (note's gate + Q19's axis marking in one statement) — approve or
split.

---

# Gate 2 closed (Emil, 2026-08-15) — rulings recorded

1. **F-1 approved, join kept**, for Q19's reason: an axis nobody can extract at act time cannot
   support mechanical delivery, and the corpus evidenced both halves at once. Conditions met:
   the join named as this filing's own; the region carries the corpus's bound (binds where acts
   are mediated by extractable artefacts; semantic-content decisions carry nameable axes at the
   weaker standing named).
2. **F-2 approved as restructured** — orthogonal typing governing, four-state mapping recorded
   as the corpus's exercise of it, honest limit stated. One sentence added to the evidence
   field: rows 4 and 8 varied resolution independently of coverage — the one orthogonality the
   corpus did test, and it held.
3. **The structural observation promoted to stated**: declared-empty is a coverage value,
   deliberately-open a resolution value; the inert/open collapse question dissolves by
   construction — the ground-axes note's open ruling 2, answered, findable from the claim.
4. **Declared-empty: files now**, as the coverage value it already is — omitting one of four
   values from a filed enumeration because the corpus did not draw it would leave the
   enumeration incomplete on ratification; zero corpus draws recorded as its evidence status.
   **Shape: it is a claim** — declared-empty asserts no choice in the region moves the outcome
   past tolerance, an admission-test assertion, attributable and falsifiable by one act; a claim
   with a claimant, subject to claimant calibration. Not a decision kind, not a bare record.
   Recorded as answering the applicability note's ruling 2, note as source, this session the
   ruling site. (Emil's ruling names the calibration instrument; carried upstream as "claimant
   calibration" under the Stable Dependency Principle — the instrument's term is filed with this
   projection. Noted in the claim.)
5. **Beyond-region evidence entry on DDD-ground-01 approved.**

Rulings applied in upstream commit `f8f57ca`.

# Gate 3 — F-3: delivery (holding)

## Drafts committed (upstream `d3674ce`; downstream this commit)

**The establishing document — number, title, skeleton proposed.** `core/18-delivery.md`,
title "Delivery", contract `requires: [store, mechanical, judgment, escape, assurance, act,
maturation]`, `establishes: [delivery, undelivered, presumed-discharge]`, status **draft**.
Number reasoning: the split's document sequence is continuous — this projection carries 13–17
(cost-projection, maturation, routing-example, calibration-ledger, time-and-assurance) — so the
next free number globally is 18; if Emil means upstream-local numbering, 13 is the alternative
and the file renames on ruling. Skeleton, deliberately minimal (establishes and points): §1 the
axis (term:delivery embedded; supply-versus-arrival; the trigger test), §2 the failure
(term:undelivered embedded; adds no condition to escape), §3 the record property
(term:presumed-discharge embedded; the source/assurance record asymmetry), §4 what the document
does not do (no store, no maturation amendment, no generator closed).

**Terms** (registry, `established_by: 18-delivery.md`, status **draft**, canonical_md matching
the doc's embeds byte-for-byte — E6 green):

- `term:delivery` — mechanical (act triggers retrieval) / judgment-mediated (only if an actor
  recalls it); a property of a decision **at an act-site**, never of the decision alone; a path
  is only as mechanical as its weakest edge.
- `term:undelivered` — filed, adequate, never reached the act; determined by nobody: escape,
  with the ledger showing coverage.
- `term:presumed-discharge` — a gate's pass meaning never-reached; a property of the record, so
  it stays mechanisable.

Canonical texts use canon's "judgment" spelling (matching `term:judgment` and the document
register); claim prose keeps the corpus's "judgement". Flagged, not hidden.

**Claims upstream:**

- **`DDD-delivery-01`** (conceptual, projected) — filing is not encoding: a decision sits in
  I(V;X) only to the extent the arrangement delivers it at the act; store allocation cannot be
  read off artefacts; paid-once-inherited belongs to mechanical delivery specifically. Region
  states the SR-1 boundary in terms: not a fifth store, not a new axis; an undelivered
  decision's store assignment is nothing — escape — exactly as the partition already reads it.
  Evidence: rows 1/5 (the pin channel silent while the statement moved), row 6 (per-site
  divergence), 7-of-7 determinability, the 1-in-7 un-annotated base rate. Falsifier: the note's
  Q15 row (ledger-counted and delivery-counted allocation agree across a corpus).
- **`DDD-delivery-02`** (conceptual, projected) — undelivered as escape generator: sufficient,
  never necessary, joining DDD-dec-15's recorded generators (capacity shortfall,
  no-applicable-filed-source); distinguishing feature in the statement — the ledger shows
  coverage, escape that presents as governance. Region draws the 10 §9 boundary (inadequate
  assurance on a filed source is governed, not escaped). Evidence: the A-01 Gate 1 centrepiece
  with the reflexive chain — including this session's own third instance (the applicability
  note arriving only after the identity check reported it absent) — and DDD-dec-16's verbatim
  presumed-discharge record. The generator-2 slot untouched, stated in the claim's notes.
- **`DDD-delivery-03`** (conceptual, projected) — compounding: unretrieved decision plus
  unretrieved check over the same act are correlated failures (same actor, same budget, same
  position), removing gate independence. **Flagged in the draft as the thinnest-evidenced
  filing**: no sampled act exhibited the correlated double miss; the corpus supplies the
  condition that makes the check worth having (1-in-7, low and nonzero), and the note's
  prediction files as the falsifier (mechanise-checks-vs-mechanise-retrieval, content
  constant). DDD-frame-05 explicitly untouched in breaks.

**Claim downstream:**

- **`DDD-delivery-04`** (conceptual, projected) — maturation retrieval-dependence: the
  paid-once-inherited property holds only where the harvest channel delivers at the consuming
  act; the channel condition includes delivery at each future run's act-sites, not only receipt
  of the harvest into the encoded store. Diachronic, hence downstream (R4); this ID per the
  Gate 1 ruling. Evidence: rows 1/5, row 6, row 3 (DDD-dec-02 — standing, no carrier,
  inheriting nothing per run by itself). Pin dependency stated in the claim's notes: rests on
  upstream `term:delivery` and `DDD-delivery-01`, which do not exist at the pinned v5.4.0 —
  `graph/upstream.yaml` is staged at GATE 5 per the DDD-dec-10/16 pattern and bumped on
  acceptance; until then the claim declares its upstream basis explicitly not yet pinned.

## R-2 exposure check — reported, nothing amended

Carried from the prior delivery prompt: do `DDD-cost-09`, `DDD-cost-08`, and the maturation
return channel want a named delivery condition?

1. **`DDD-cost-09` — yes, mildly; reported, not amended.** Its "assurance-by-check ... supplied
   standing — independent of the act" holds **per act-site, not per decision**: the corpus's
   no-unwrap row carries the same criterion act-triggered in CI and actor-triggered locally —
   judgement-mediated under the trigger test — so a closed predicate is amortised assurance
   only at act-sites where the check's delivery is mechanical. Candidate amendment if Emil
   rules it: a region or notes qualifier "at act-sites where the check is act-triggered";
   DDD-delivery-01 states the general condition without touching cost-09.
2. **`DDD-cost-08` — exposure named, no amendment wanted on its own terms.** The claim governs
   selection economics and survives as stated; what delivery conditions is its *benefit*
   arithmetic — the assurance gate adds independent protection only where the gate's delivery
   is not correlated with the decision's (DDD-delivery-03's case: both judgement-mediated,
   same actor, same budget). Its breaks field already carries DDD-dec-15's correction.
   Candidate on acceptance: a notes cross-reference to DDD-delivery-03; nothing stronger.
3. **The maturation return channel — yes, and the condition is filed rather than reported
   loose.** Core/08's "the channel must exist" is authoring-side (harvest received into the
   encoded store); the corpus showed the consuming side failing while the authoring side held
   (rows 1/5; row 6 per-site). The named delivery condition is DDD-delivery-04, downstream,
   with upstream prose unamended (R4 — the consequence is diachronic).

## Validation

Upstream: 45 claims valid, 4 decisions valid; core-order 0 errors, zero W4; warning delta from
baseline exactly **+1 W1** — `00-primitives.md:207`, "*A note on delivery.*", a rhetorical use
of the word predating the term, now read as a forward pointer. False positive; reported, not
repaired (candidate one-word rewording for a canon session if Emil wants the profile clean).
Downstream: 25 claims valid, 12 decisions valid; core-order 0 errors, 0 warnings; 26 pins
resolve against v5.4.0.

## GATE 3 — holding

For Emil's ruling:

1. The establishing document: number (18 proposed; 13 the repo-local alternative), title,
   skeleton, and its draft status.
2. The three terms as drafted (values, canonical texts, draft status; the judgment/judgement
   spelling split flagged above).
3. DDD-delivery-01/02/03 as drafted — including delivery-03's thin-evidence flag.
4. DDD-delivery-04 as drafted downstream, with the pin staging deferred to GATE 5.
5. The R-2 exposure check outcomes — in particular whether cost-09 takes the per-act-site
   qualifier now or on acceptance, and whether cost-08 takes the notes cross-reference.
6. The +1 W1 false positive — leave reported, or queue the one-word rewording.

---

# Gate 3 closed (Emil, 2026-08-15) — rulings recorded

1. **Number: `core/13-delivery.md`, upstream-local.** The projection's 13–17 is a downstream
   sequence; a global sequence across two repos would couple numbering across the charter
   boundary the split exists to keep separate. Renamed on the ruling. Title, skeleton, draft
   status approved.
2. **Terms approved as drafted**, including the spelling split — canonical texts take canon's
   "judgment" (matching term:judgment); claim prose keeps the corpus's "judgement". Recorded
   for the manifest as deliberate.
3. **DDD-delivery-01/02/03 approved.** Delivery-03's thin-evidence flag stands — the claim
   files on its falsifier's strength, the correct standing for a claim whose test is a
   prediction. Delivery-02's evidence field now states the third arrival-failure instance was
   minted during the filing.
4. **DDD-delivery-04 approved**; pin staging at Gate 5 per the dec-10/16 pattern.
5. **R-2: both amendments taken now** — deferring would leave a ratified claim knowingly
   slightly wrong across the merge. DDD-cost-09's region gains the per-act-site qualifier;
   DDD-cost-08's notes gain the compounding cross-reference; both `changed` fields bumped,
   statements untouched; both recorded as scope extensions in the session's decision node
   **DDD-dec-17** (upstream, drafted at GATE 3, grows to close — the DDD-cost-05 pattern).
   Maturation condition as DDD-delivery-04, upstream prose unamended: confirmed correct under
   R4.
6. **The +1 W1: reworded.** 00-primitives' closing aside "A note on delivery" → "A note on
   **presentation**" (the session's word; the registry does not own it). Recorded for the
   manifest as a term-collision repair, not a content edit — the term:maturation divergence
   pattern caught before it became one. Warning profile back to exact baseline (52 W1, 7 W2).

Applied in upstream commits `e3832bf` (rulings) and `cc5e8f9` (F-4 draft, below).

# Gate 4 — F-4 and the registry seed (holding)

## F-4 — `DDD-ground-04` (upstream, normative, projected; commit `cc5e8f9`)

A retro-filed decision carries **when the gap was uncovered** (distinct from when the act
occurred) and **that it was retro-filed**; without both, retro-filing launders escape into
coverage and a sweep reading the register reports clean. Region: binds at filing, register- and
actor-general. **The session's thinnest evidence base, flagged in the draft as ruled at Gate 1:
the corpus sampled no retro-filed row, the evidence field is empty, and the claim files
projected on its falsifier's strength** — the laundering risk is the argument, urgent because
the escape correction and the undelivered generator make retro-filing more attractive (it is
the only mechanism converting a silent completion into a visible node) and nothing currently
marks it. Notes carry: the §13.5 pinning-versus-resolution distinction (a retro-filed test pins
but did not constrain — the mark keeps a register from conflating them); the symmetry with
DDD-delivery-02 (ledger-shows-coverage is the same presentation failure in space that unmarked
retro-filing is in time); the decision-format finding restated (format lives in the validator
and practice; enforcement deliberately not built this session); and the note's unresolved flag,
left for Emil — whether retro-filing is the discharge mechanism for the escape generators, and
whether the retro-filing act is itself a claim-layer act as declared-empty was ruled to be.

## The registry seed — `graph/axis-registry.yaml` (downstream, this commit)

Seeded per the Gate 1 ruling: machine-read YAML in `graph/`, headed **ARTEFACT, NOT CANON**,
with the header stating that validators do not yet check it and that no tooling accompanied the
seeding. Contents: the corpus table's 22 axes verbatim — axis, forcing row, reuse, quality
(resolvable / resolvable-partial / nameable), extractor sketch, and the recorded granularity
defect on `artifact-class`; totals as ratified (20 resolvable, one partial; 2 nameable). The
header carries the SR-6 provenance (no axis registry existed anywhere before the corpus test;
invention cost is adoption cost) and points the quality mark at DDD-ground-01's maturity-state
evidence. Parses clean (22 axes); downstream validators unaffected (0 errors, 0 warnings).

## Validation at this gate

Upstream: 46 claims, 5 decisions valid; core-order 0 errors, zero W4; warning profile at exact
baseline (52 W1, 7 W2). Downstream: 25 claims, 12 decisions valid; core-order clean; registry
seed parses.

## GATE 4 — holding

For Emil's ruling:

1. **DDD-ground-04 as drafted** — including the empty evidence field with the flag, and the
   two sub-questions left open in its notes (discharge-mechanism; retro-filing as claim-layer
   act).
2. **The registry seed as drafted** — header, format (`axis-registry/v1`), and content
   fidelity to the corpus table.
3. Anything Emil wants carried differently into DDD-dec-17 before Gate 5 extends it.

---

# Gate 4 closed (Emil, 2026-08-15; ruling re-issued — the original did not arrive) — recorded

1. **DDD-ground-04 approved as drafted**, empty evidence field and all. Both sub-questions
   ruled and recorded in the claim's notes and DDD-dec-17: retro-filing is the ledger-side
   discharge mechanism for the escape generators, discharging only with both fields present —
   the fields turn retro-filing from concealment into remedy; and the retro-filing act is a
   claim-layer act, the sibling ruling to Gate 2's declared-empty ruling.
2. **Registry seed approved** with the promotion-path header line added: canon on (1) a
   validator reading it plus (2) a ratification act; until both, artefact.
3. **DDD-dec-17 extended** with the sub-question rulings, the meta/sessions working convention
   recommended to the freight session (evidence: five arrival failures — manuscript, review,
   predicted-ground note, the applicability note at this session's Gate 1, and this ruling's
   own non-arrival; cost: the Test B reconstruction floor), and the reflexive chain stated
   once in full, this gate's instance included (a ruling is a delivered governing artefact;
   its non-arrival is the phenomenon — judged the same failure class).
4. **Source identity recorded** for the manifest: this session filed from ground-axes rev 8
   (1,375 / 13,622 / `5d8aede1…`) and the applicability note (362 / 2,494 / `4afe380c…`); a
   rev-14 successor exists (1,869 lines, `ac47441f…`, adding Q25–Q30), assessed separately,
   touching nothing in the four filings.

Applied in upstream commit `acf284b`.

# Gate 5 — close (holding)

## Basis-impact sweep — weakenings reported, not repaired

Touched nodes: DDD-cost-09 (region qualifier), DDD-cost-08 (notes cross-reference),
00-primitives (word swap), plus the eight new claims, three new terms, one new document, and
two decisions. Every citing node re-checked:

| Citing node | Reads | Impact |
|---|---|---|
| DDD-cost-11 (upstream) | "adjacent, not identical, to DDD-cost-09" | none — relationship statement only |
| core/10-cost.md §6 + summary row | "supplied standing — independent of the act" | prose is exposition and now reads unqualified against the qualified region; candidate one-line annotation for a later canon session; claim statement itself unchanged |
| DDD-cost-12/13/22, DDD-dec-15 (cite cost-08) | gate structure, contrapositive | none — cost-08's statement and region unchanged; notes-only cross-reference |
| **DDD-cost-10 (downstream)** + core/13-cost-projection.md:111 | "standing, independent of the act", amortisation corollary | **mild genuine weakening, reported**: the corollary inherits the per-act-site condition — cost divides over act volume at act-sites where the check is act-triggered; unamended; nothing demotes (no statement moved, no computation fails) |
| core/15-routing-example.md | exercises DDD-cost-08's two gates | benefit arithmetic now conditioned by DDD-delivery-03 (correlated-delivery case); reported |
| "A note on delivery" (00-primitives) | — | no citing node; swap is collision repair only |

Recorded in DDD-dec-18's resolution as the adopting repo's record.

## Reference closure

Every claim ID, decision ID, term ID, file path, and cited section in the changed files of both
repositories resolves against the union of the two registries, checked mechanically. One
deliberate exception, reported: DDD-delivery-04's notes mention `DDD-cost-30` as the
**rejected alternative ID** from the Gate 1 ruling — a never-minted ID documenting a ruling,
not a citation.

## Validators — final state

Upstream: 46 claims, 5 decisions valid; core-order 14 documents, 65 terms, 0 errors, zero W4;
warning profile at exact baseline (52 W1, 7 W2). Downstream: 25 claims, 13 decisions valid;
core-order 0 errors, 0 warnings; **28 pins resolve against the staged ref, 0 basis-loss
warnings**.

## Pin staging — DDD-dec-18

`graph/upstream.yaml` ref advanced v5.4.0 → the staged upstream branch (checks resolve during
staging, the DDD-dec-16 pattern); bumps to tag v5.5.0 on Emil's acceptance of the upstream PR,
before the downstream PR is accepted, per the Gate 4 ruling. Pins added: `term:delivery`
(status_at_pin: draft — flips to settled on ratification, which W5 will then instrument) and
`DDD-delivery-01` (projected). The advance is governed, not mechanical, for the recorded
reason: DDD-cost-09's region moved while its status stayed projected — the
statement-moved-silently case for the second time, and itself an instance of the session's own
presumed-discharge vocabulary. DDD-dec-18 records the advance, the added pins, and the sweep's
weakenings.

## The manifest

**Filed (upstream, area `ground`):** DDD-ground-01 (applicability gate + axis-type field as
maturity state); DDD-ground-02 (orthogonal coverage/resolution/assurance typing;
declared-empty ruled in as a coverage value whose filing is a claim-layer act); DDD-ground-03
(the —(open) timing value); DDD-ground-04 (retro-filing's two fields, with both Gate 4
rulings).
**Filed (upstream, area `delivery`):** core/13-delivery.md (draft, minimal — establishes and
points); term:delivery, term:undelivered, term:presumed-discharge (status draft);
DDD-delivery-01 (filing is not encoding); DDD-delivery-02 (undelivered as escape generator);
DDD-delivery-03 (compounding). Scope extensions by Gate 3 ruling, recorded in DDD-dec-17:
DDD-cost-09 region qualifier; DDD-cost-08 notes cross-reference. Term-collision repair:
00-primitives "delivery" → "presentation". Session decision: DDD-dec-17.
**Filed (downstream):** DDD-delivery-04 (maturation retrieval-dependence); the axis-registry
seed (graph/axis-registry.yaml, artefact-not-canon, promotion path stated); the staged pin
advance and DDD-dec-18; this session document.

**Flagged beyond evidence (in the drafts themselves, per scoped-as-evidenced):**
DDD-delivery-03 — no sampled act exhibited the correlated double miss; files on falsifier
strength (ruled the correct standing at Gate 3). DDD-ground-04 — no retro-filed row sampled;
evidence field empty; files on falsifier strength with the laundering risk as argument.
DDD-ground-02 — declared-empty at zero corpus draws (ruled in regardless, enumeration
completeness); orthogonality only partially exercised (assurance never varied — rows 4 and 8
tested the coverage/resolution orthogonality, which held).

**Stayed out (per the prompt's out-of-scope list and rulings):** the store re-derivation
(SR-1 stands; the counterexample channel closed empty); any amendment to term:escape or the
escape mechanism; the empty-option-set generator (open and unexamined, exactly as DDD-dec-15
holds it); everything on the freight list including the exhaustiveness/defence-in-depth seam;
all instrument and tooling work (no validator reads the axis registry; no delivery evaluator;
no retro-filing enforcement); capacity material (the scoping session consumes the corpus's
question-3 evidence next); Generator 2; Wave 3; Paper A.

**Deliberate register notes:** canonical term texts take canon's "judgment" (matching
term:judgment); claim prose keeps the corpus's "judgement" — ruled deliberate at Gate 3, not
drift. The corpus record's "five weeks" erratum stands recorded at Gate 1; drafts carry repo
dates. Source identity: filed from ground-axes rev 8 (`5d8aede1…`) and the applicability note
(`4afe380c…`); rev-14 (`ac47441f…`, Q25–Q30) exists, assessed separately, touches nothing
filed here.

## PRs — upstream-first

Opened at this gate, merge on Emil's acceptance only (sequence per the Gate 4 ruling: upstream
accepted → Emil tags v5.5.0 → pin bumps to the tag → downstream accepted). Links recorded in
the Gate 5 report.

**GATE 5 — holding** for Emil's acceptance of the upstream PR, the v5.5.0 tag, the pin bump,
and the downstream acceptance.
