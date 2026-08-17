# GATE 1 survey — Wave 3 (draft-pending-ruling)

**Status: draft-pending-ruling.** Nothing below is filed. Every entry names its node IDs; every
verification was run against the live repos at the session's base commits (upstream `01db788` =
`v5.6.0`; downstream `0452a40`). Validators pass in both repos at base: upstream
`validate-core-order.py` exit 0 / 0 errors, 49 claims valid, 6 decisions valid; downstream 25
claims valid, 17 decisions valid, 32 pins resolved with 0 basis-loss and 0 content-drift.

---

## 0. Arrival failures and holds

**The Paper A revision foundation is absent.** It is in neither repository (searched by name and
by content: no file, no `papers/` entry beyond the measure note) and was not uploaded with the
session. The prompt's instruction applies: hold rather than work from summary. Consequences:

- **Batch W drafting is blocked** — the prompt drafts W against the foundation's §1.1, §3, §4,
  §5. The *survey* below is unaffected: it runs against canon at head, using the prompt's own
  statement cores.
- **Batch H drafting is blocked** — H1–H5's statements and their §9 study designs live in the
  foundation. The *overlap check* below is unaffected.
- **Batch P is blocked** at its map step — the map is indexed by the foundation's §12 manuscript
  structure.
- **Batch Q is not blocked.** Q-A's derivation cites foundation §4.3 as one of three premises;
  the other two (`term:escape`, the luck ruling) are in-repo, and the addendum states the
  derivation independently. Recommendation: draft Q with the §4.3 citation marked pending, to be
  confirmed against the document when it arrives. Alternative, if Emil prefers: hold Q-A too.

**Observation, not a hold:** downstream `graph/upstream.yaml` pins upstream at `ref: v5.5.0`
while upstream head is tagged `v5.6.0`. The freight session's upstream PR was accepted (v5.6.0
exists, downstream head merged) but no pin advance to v5.6.0 is recorded in `core/decisions/`.
The prompt expects "downstream pin advances" at this session's close (to v5.7.0); whether that
advance goes v5.5.0 → v5.7.0 in one recorded decision, or the v5.6.0 advance is a separate
missed step, is Emil's call at Gate 5. W6 at the advance runs against whatever pins exist then.

---

## 1. Batch W survey — carried / partially carried / absent

The failure mode named by the prompt is refiling what exists. Finding: **all four W items
already have substantial presence upstream; none needs a wholly new claim except possibly W-4.**
Three of the four existing nodes carry `UNVERIFIED — Emil review` flags saying exactly what
Wave 3 was chartered to fix: the claim exists, its canon exposition does not.

### W-1 — the six-tuple index. **Carried as claim, absent as canon exposition.**

- **Node:** `DDD-frame-01` (conceptual, projected, changed v4.4): "Unresolved determination is
  indexed by the tuple ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩,
  not by the task alone." Verbatim the W-1 statement core (modulo "Unresolved determination" vs
  the prompt's "Determination" — see Q-A/Q-E seam note below).
- **The gap, per the node's own notes:** "The six-tuple index … is Paper A / foundation-revision
  material and is NOT stated in any core/ document. Canon carries the components severally
  (tolerance and assurance separated in core/01 §'declared assurance level'; arrangement in
  core/05 §2; ground and acceptance predicate in core/00, core/03) but never as this named
  tuple. Cannot verify the tuple as a canon claim; flagged for Emil, not struck."
- **Wave 3 work:** not a new claim — give `DDD-frame-01` its canon home (exposition in a core
  document, drafted from foundation §1.1 — blocked on arrival) and clear the flag by ruling.
  Overlap verified: `term:granularity-bound` and `term:arrangement` carry components, not the
  tuple; the closure vocabulary (`term:closure`) indexes closure by arrangement, consistent
  with and not duplicating the tuple.

### W-2 — commitment levels + residual discretion. **Partially carried.**

- **Node:** `DDD-frame-02` (conceptual, projected, v4.4): "Behavioural commitments attach at
  three levels — outcome, policy, principal — which compose and are not actor species." Also
  flagged `UNVERIFIED`: the levels appear only in pre-split scaffolding that did not migrate;
  no core/ document states them.
- **The absent part:** "residual discretion is what remains after declared commitments" — no
  hit for "discretion" anywhere in upstream `core/`. This clause is genuinely new content.
- **Overlap verified:** `term:store` partitions supply sources, not commitment levels — no
  conflict; the commitment material in core/03 is the acceptance predicate's, not attachment
  levels. **Wave 3 work:** canon exposition for the three levels (foundation §3 — blocked on
  arrival) + the residual-discretion clause, either as an amendment to `DDD-frame-02`'s
  statement under ruling or as one small companion claim. Recommendation: amendment — the
  clause completes the same thought, and the node is projected, not ratified.

### W-3 — source/assurance as separate dimensions. **Carried. Cite, do not refile.**

- **Node:** `DDD-frame-03` (conceptual, projected, v4.5), verified against canon per its own
  notes: core/05 §§1–2 makes accountability a second axis independent of pinning resolution;
  core/01 separates tolerance from assurance. `DDD-cost-09` (occasioned vs standing assurance)
  and `DDD-ground-02` (source coverage · resolution · assurance orthogonal) carry the split
  onward.
- **One standing flag to rule, not this session's to invent:** the notes flag the historical
  clause "the four-store model conflated them" as the seed's gloss — canon says the model
  "never draws" the distinction, which is weaker than active conflation. Emil may rule the
  clause softened or kept; either way W-3 files nothing new.

### W-4 — the relational judgment floor. **Partially carried; the one candidate gap.**

- **Components carried:** `term:floor` ("a property of the acceptance predicate, not of the
  decision"); `term:closure` ("closed **for an arrangement**"); core/03 "Consequence" section:
  "the floor is a property of the ⟨actor, predicate⟩ pair"; core/03's one line: "not a property
  of the problem … a property of whether you can check the answer". `DDD-floor-01`
  (post-correction, reported) is the capacity mechanism only — its region explicitly excludes
  the general thesis. `DDD-frame-11` is the governed/measured domain split — adjacent, not this.
- **The gap:** no claim node states the relational thesis as such — that irreducibility is a
  property of the indexed relation (the `DDD-frame-01` tuple), not of the task. Canon's prose
  carries three *partial* indexings (predicate; ⟨actor, predicate⟩; arrangement) that the
  relational claim would unify without contradicting `term:floor` (the predicate is *in* the
  relation; closure supplies the arrangement index).
- **Wave 3 work:** one new claim, proposed `DDD-floor-02`, derivation-grade against
  `term:floor` + `term:closure` + `DDD-frame-01`, drafted against foundation §5 (blocked on
  arrival for the exposition; the derivation itself is canon-internal and could draft now if
  Emil prefers).

**Net W-batch:** zero-to-one new claims (W-4), one statement amendment (W-2), two
flag-clearings with canon exposition (W-1, W-2), one pure citation (W-3). The batch shrinks
exactly as the prompt anticipated.

---

## 2. Batch H overlap check

**The umbrella exists:** `DDD-frame-07` (empirical, projected, owner paper-4) — "Operational
evaluability, feedback density, and ground accessibility predict the comparative advantage of
computationally assisted arrangements over unaided situated judgment, after controlling for
difficulty and resources **(H1–H5)**." Its notes: the hypotheses themselves are "Paper A /
foundation-revision material, not stated in any core/ document" — flagged `UNVERIFIED`.
So the H-set files *under* an existing umbrella; the relation (five nodes superseding
frame-07, or five nodes + frame-07 annotated as the set's summary) is a Gate 4 ruling.
Recommendation: keep `DDD-frame-07` as the set's summary claim, annotate it to point at the
five nodes; supersession would lose its already-filed falsifier for nothing.

**H4 (accountability completeness):**
- `DDD-frame-08` (normative, projected) already claims the relation-not-capacity thesis, with a
  *test* that is itself a prediction ("completeness of the relation predicting trust and
  remediation outcomes better than executor identity"). H4 must either be that prediction
  stated as a graded hypothesis (then it files citing frame-08, no duplication) or differ from
  it visibly.
- `DDD-cost-24` (downstream): the Wave 2 close ruled its validity condition (the
  model-market-gap qualification — the instrument exists only for claimant identities that
  outlive their verdict horizons; cross-identity transfer partial, per-capability) carried on
  H4/H5. **Consequence found: `DDD-cost-24` cannot be cited by ID from upstream** — the
  principle repo carries no reference to its dependents. The qualification must be *restated*
  in the upstream claim bodies (it is two sentences), with `DDD-cost-13` (upstream, citable)
  as the instrument-bound premise; the `DDD-cost-24` cross-link files downstream as an
  annotation, not upstream. Same pattern as the freight session's citation-scope convention.

**H5 (selection versus training):**
- Carried components upstream: `term:selection` ("verification relocated from the act onto the
  actor's identity"), `term:training` (closure decides availability; reliable error signal),
  `DDD-cost-20` (training buys allocation, not capacity), `DDD-cost-13` (the instrument bound),
  core/03's consequence section ("where you can check the work, you train; where you cannot,
  you must select"). H5 as a *graded hypothesis* (prediction over task markets) is absent —
  files citing these, with the cost-24 qualification restated as above.

**H1–H3** (operational evaluability; ground and judgment dependence; generator/checker
composition): no per-hypothesis overlap beyond frame-07's umbrella and the conceptual ground
(`DDD-frame-05`, `DDD-frame-06`, `DDD-cost-08`/`09`). No existing node states any of them as a
separate graded hypothesis. Clean to file — statements blocked on the foundation's §8.

---

## 3. Batch Q — every cited premise, verified at head

| Premise | Where | Status at head | Note |
|---|---|---|---|
| `term:escape` | upstream terms.yaml | settled ✓ | "decided-by-nobody as a first-class category" |
| `term:store` | upstream terms.yaml | settled ✓ | "{rule, check, actor, nothing}. There is no fifth source." — Q-A's seam-guard counterparty |
| the luck ruling | downstream rev18 note, correction 1 | **recorded ruling, not a canon node** | "luck does not exist; statistics and probability exist … the verdict was drawn from a distribution the arrangement did not control." Emil-ruled, held in an unratified note. Nothing upstream carries it; grep for luck/uncontrolled-draw is empty. **Q-A's derivation must restate its content as a stated step, not cite it** — an upstream claim cannot cite a downstream holding note (citation-scope convention), and an unratified note is not ground either |
| foundation §4.3 | absent | **hold** | see §0; draft with citation-pending or hold Q-A per ruling |
| `term:act` (unit of account) | upstream | settled ✓ | "the unit demand is counted in" — Q-B premise |
| `term:standing-cost` / `term:occasioned-cost` | upstream | settled ✓ (registry-only) | Q-B's split; `DDD-cost-01` (upstream, projected) carries the locus-of-supply form |
| `term:verdict` | upstream | settled ✓ | Q-D/Q-E premise; support = determinate-space at grain τ reading is consistent with its text |
| `DDD-cost-16` | **downstream** | projected ✓ | **cannot be cited from upstream.** Resolution proposed: the upstream Q-D claim derives from `term:verdict` + `term:maturation`/`term:compound` (maturation harvests verdicts — upstream, settled) and states the mechanism; `DDD-cost-16` gains a downstream annotation naming the new upstream claim as its named mechanism. The addendum's "this is DDD-cost-16's mechanism named" lands downstream, exactly as routed |
| `DDD-frame-12` | upstream | projected ✓ | claim = act with deferred verdict; Q-D's verdict-pending state |
| `DDD-ground-04` | upstream | projected ✓ | retro-filing's two fields; Q-D's retro-conversion honesty condition |
| `term:act-individuation` | upstream | settled ✓ | the individuation boundary clause the addendum cites |
| `term:admission-test` | upstream | settled ✓ | Q-E's grain-picker |
| `term:granularity-bound` | upstream | settled ✓ | Q-E premise |
| `DDD-ground-01` | upstream | projected ✓ | Q-F's mechanical gate ("F-1's gate") |
| Johnson 1921 | verified ✓ | — | *Logic* Part I, ch. XI "The Determinable", Cambridge University Press, 1921 (chapter title confirmed via SEP) |
| Prior 1949 | verified ✓ | — | "Determinables, Determinates and Determinants", *Mind* 58, two parts: 58(229): 1–20 and 58(230): 178–194 |
| Funkhouser 2014 | verified ✓ | — | *The Logical Structure of Kinds*, Oxford University Press, ISBN 9780198713302; his "determination dimensions" match Q35's dimension-of-variation reading |
| Wilson (SEP) | verified ✓ | — | Jessica Wilson, "Determinables and Determinates", *Stanford Encyclopedia of Philosophy*, first published 2017-02-07, substantive revision 2023-01-18 |

**Absence checks (the other half of premise verification):** upstream carries no `term:outcome`,
no `term:determinable`/`term:determinate`, no "supply mode" vocabulary, and no luck/uncontrolled-
draw language — the Q filings introduce genuinely new nodes, nothing collides.

**Seam-guard groundwork (Q-A), for line-level scrutiny at Gate 2:** the four discharge modes
(filed decision · actor judgment · arrangement default · uncontrolled draw) are **not** the four
stores {rule, check, actor, nothing} under new names — `check` is an assurance position, not a
discharge mode, and `nothing` in the store partition is *absence of governance-supply* where
`uncontrolled draw` is a *positive physical event*. One partition is over governance-supply
(where escape is nothing); the other is over discharge (where escape is an uncontrolled draw).
The mandatory sentence will state this disjointness explicitly.

---

## 4. Proposed IDs, destinations, document homes

All filings upstream (`actor-indexed-determination`); downstream consequences named per item.
IDs continue the shared cross-repo sequences (claims per family; decisions: next is
`DDD-dec-24`).

| Item | Proposed ID | Kind / grade | Proposed home | Downstream consequence |
|---|---|---|---|---|
| Q-E determinable/determinate | `DDD-frame-13` + `term:determinable`, `term:determinate` | conceptual, derivation-grade | `core/00-primitives.md`, new section beside the admission tests (§4-adjacent) — the determinable is what the admission test picks the grain of | none |
| Q-D outcome/verdict registers | `DDD-frame-14` + `term:outcome` | conceptual, derivation-grade | `core/09-the-measure.md` §7-adjacent (verdict's home; the boundary section already draws governed-only) — alternative: `core/13-delivery.md`. 02 is excluded: citing `term:verdict` from 02 is a forward edge | `DDD-cost-16` annotated: mechanism named by `DDD-frame-14` |
| Q-A supply-mode exhaustiveness | `DDD-frame-15` | conceptual, derivation-grade | `core/13-delivery.md`, new discharge section (post-09, so verdict/outcome citable; delivery is already the how-governance-reaches-an-act doc) — alternative: a new `core/14-discharge.md` | rev18 Q33-A retires into it |
| Q-B act-indexed discharge | `DDD-frame-16` | conceptual, derivation-grade | with Q-A | B's formal content (N·H(V) etc.) stays measure-paper, per rev18 routing |
| Q-C distribution-weighted | **no claim** | exposition | one paragraph beside Q-A/Q-B citing the measure's `P` | — |
| Q-F constitutive priority | `DDD-ground-05` | conceptual, derivation-grade | `core/00-primitives.md`, corollary in Q-E's section (ground-01's gate cited as the mechanical form) | none |
| W-1 tuple | no new claim — exposition home for `DDD-frame-01` + flag cleared | — | **the open question the prompt names:** new core doc vs existing. Recommendation: a short new `core/14-indexed-determination.md` carrying the tuple statement, the commitment levels (W-2), and the relational floor (W-4) as one document — the foundation's §1.1/§3/§5 cluster is one idea (the index), and 00 is already 260 lines with a settled shape. Alternative: tuple into 00 §3 (actor/arrangement section), levels into 05, floor into 03 — three small additions, no new doc | pin advance picks up changed nodes |
| W-2 levels + residual discretion | `DDD-frame-02` amended (or one companion claim) + exposition | statement-grade | with W-1's home | — |
| W-3 | nothing files | — | — | — |
| W-4 relational floor | `DDD-floor-02` (if ruled a gap) | conceptual, derivation-grade | with W-1's home, or `core/03` consequence section | — |
| H1–H5 | `DDD-hyp-01`…`DDD-hyp-05` (new family; alternative: `DDD-frame-17`–`21`) | empirical, statement-grade, shared preregistration-shaped falsifier discipline | one document section: recommendation `core/14`'s closing section (hypotheses the index generates) if the new doc is ruled; else a new section in `core/07` or `08` — held for the same ruling | cost-24 cross-link annotated downstream; frame-07 annotated as umbrella |

**Ordering inside Q (per prompt):** Q-E → Q-D → Q-A → Q-B → Q-F (Q-F last as Q-E's corollary;
Q-B rides Q-A's section).

**Terms entering the registry:** `term:determinable`, `term:determinate` (Q-E, together),
`term:outcome` (Q-D, beside the existing `term:verdict`). All additive; no settled term moves.
W7 shadow check: none of the three collides with a pinned downstream id.

---

## 5. What Gate 1 asks of Emil

1. **The foundation document** — upload, or rule which batches proceed without it (Q can, W/H/P
   cannot).
2. **The document-home ruling** — new `core/14-indexed-determination.md` (recommendation) vs
   additions to 00/03/05/07/09/13; and whether the H-set rides the same doc.
3. **The H-family ID** — `DDD-hyp-*` vs `DDD-frame-17+`.
4. **W-2's residual-discretion clause** — amendment to `DDD-frame-02` vs companion claim.
5. **Q-A under the foundation hold** — draft now with §4.3 citation-pending (recommendation),
   or hold the whole Q batch for the upload.
6. **The pin observation** (§0) — noted for Gate 5, no action asked now.
