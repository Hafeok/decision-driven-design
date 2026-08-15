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
