# GATE 1 — the accountability arity (I-1)

**Status: draft-pending-ruling.** Ruled at Paper A's Gate 3 as both-not-either; the paper flagged,
this is the canon session that owes the ruling. Discharges item 1 of
`meta/successor-items-paper-a-revision.md`.

Base verified: upstream `actor-indexed-determination` at `5c7fe46`, tag `v5.13.0` pointing exactly
at the head of the default branch. Downstream `decision-driven-design` at `46d581a` (the primer
merged).

---

## 1. Both texts, verbatim

`DDD-frame-08` (`core/claims/DDD-frame-08.yaml`, upstream, **projected**, kind normative, owner
paper-4, changed v4.5) — the statement field:

> Accountability is a relation (attribution, persistent principal, authority linkage, stake,
> sanction path), not an intrinsic capacity; an arrangement naming an executor but no principal is
> incomplete.

`term:accountability` (`core/graph/terms.yaml`, upstream, **settled**, established by
`05-accountability.md`) — the canonical_md field:

> **Accountability** is a property of the arrangement, not of the executor: attribution of
> the determination, a persistent answerable party, and a borne consequence. An arrangement
> missing any of the three has not allocated the decision's consequence.

**A third enumeration exists in canon prose**, and the gate should see it. `core/05-accountability.md`
§2, the bolded sentence immediately above the term's embed — the sentence `DDD-frame-08`'s own
notes cite as its verification:

> **Accountability completeness is a property of an arrangement, not a capacity of an actor. An
> execution is accountability-complete when it is linked to a persistent responsible principal, an
> attributable record, a defined stake, and an enforceable consequence path.**

Four elements: it already carries the split (stake and consequence path separate) and does not
carry authority linkage. Canon therefore counts the relation three ways — three (term, settled),
four (core/05 §2 prose, exposition), five (claim, projected). Authority linkage's only canonical
carriage is `DDD-frame-08` and the statement of `DDD-hyp-04`; the nearest prose support is core/05
§2's "sanctionability depends on an authority with enforceable jurisdiction — all properties of a
relationship among executor, principal, record, and sanctioning authority".

## 2. Every node depending on either

### Upstream (`actor-indexed-determination`, v5.13.0)

| Node | Dependency |
|---|---|
| `core/claims/DDD-frame-08.yaml` | the claim itself |
| `core/graph/terms.yaml` → `term:accountability` | the term itself |
| `core/claims/DDD-hyp-04.yaml` | its **statement** enumerates all five elements ("attribution, persistent principal, authority linkage, stake, sanction path"); its notes cite frame-08 as conceptual basis per a GATE 1 ruling — the prediction is "frame-08's test made graded and preregistered" |
| `core/05-accountability.md` | establishes and embeds `term:accountability` (`ddd:embed`, E6 byte-match enforced); §2 carries the four-element bold sentence frame-08's notes cite |

No other upstream claim or decision references either id. `DDD-dec-27` (recorded downstream in the
pin comment) is provenance for frame-08's pin addition, not a live dependent.

### Downstream (`decision-driven-design`, head)

| Node | Dependency |
|---|---|
| `graph/upstream.yaml` | pins both: `DDD-frame-08` (projected, `content_hash sha256:cf73b307…`) and `term:accountability` (settled, `sha256:a986dc63…`). Hash covers statement + region + canonical_md (`validate-core-order.py`), so **any change to either text fires the pin** |
| `projections/tracks/01-determination.md` | rung 4 (line ~397): prose enumerates the five elements with `ddd:ref id=DDD-frame-08`; rung 10 (lines ~913–920): quotes the term's canonical text in full and frame-08's statement in paraphrase; status table rows at lines 50 and 64 |
| `papers/paper-a/paper-a.md` | §7 quotes frame-08's statement verbatim and reproduces the term's three-element enumeration; carries the mapping table (refines-and-adds); further uses at lines ~1263, 1292, 1430, 1515–1537, 1566–1567 (related-work table: "four of five accountability elements" Bovens's; "authority linkage; the relation as a design-time property" the framework's), 1629 |
| `papers/paper-a/paper-a-supplement.md` | line ~66 (the mapping, five vs three); line ~189 (frame-08's statement verbatim, appendix table); line ~230 (the term's canonical_md verbatim, appendix table) |
| `meta/successor-items-paper-a-revision.md` item 1 | the ruling this gate owes; discharges here |
| `meta/seed/claims-seed.yaml` | historical seed copy of frame-08 (record, not live) |
| session records (`2026-08-18-wave3`, `2026-08-20-paper-a`, `2026-08-25-item4`, `2026-08-30-paper-a-revision`), ground-audit files | historical mentions; records do not move |

### The survey constraint that binds every disposition

Paper A's related-work survey (gate2-survey-notes, carried into the paper's related-work table):
**four of `DDD-frame-08`'s five elements are already Bovens's** (the actor–forum relation: inform,
interrogate, judge-and-sanction; the problem of many hands). What is not Bovens's is **authority
linkage**, plus the change of tense — retrospective assessment of conduct → design-time
constitution of an arrangement. Whatever files at this gate must not claim more than that, and
currently `DDD-frame-08`'s notes say nothing about lineage at all.

## 3. The three dispositions, with costs

### A — the term supersedes to carry five

`term:accountability`'s canonical text moves to the five-element relation; the three-element text is
preserved as the superseded version with the correction recorded (supersession, never rewriting —
DDD-dec-09/10/15 pattern).

Costs:

- **A settled node carries projected content.** Authority linkage's evidence grade is a projected
  claim and an unrun hypothesis. Putting it into the settled term either over-claims — the defect
  class this session exists to prevent — or forces the term's status down, and a settled term five
  documents pin or embed is the expensive kind to demote.
- **Maximum firing surface.** canonical_md is hashed: the downstream pin fires; `core/05`'s embed
  must re-project (E6); the paper's §7 quote and the supplement's appendix table (line 230) go
  stale against a *settled* node — the worst kind of staleness for a manuscript about to be public;
  the track's rung 10 verbatim quote regenerates.
- **The Bovens constraint bites hardest here.** The three-element term is materially Bovens's own
  decomposition; a five-element settled term moves the non-Bovens element into the framework's
  canonical definition at settled grade.
- **Sequencing.** Lands after v5.13.0, so it needs the close's version proposal (v5.14.0) and a
  second downstream pin advance after I-3's — I-3's advance to v5.13.0 stays clean either way.

### B — the claim narrows to the term's three

`DDD-frame-08`'s statement supersedes to the three-element relation.

Costs:

- **Two claims move, not one.** `DDD-hyp-04`'s statement enumerates the five; narrowing frame-08
  alone relocates the disagreement rather than resolving it. Both are projected, so the status cost
  is low — this is the ordinary correction loop.
- **Canon gives up ground its own prose argues for.** The split (stake ≠ sanction path) is already
  in core/05 §2's bolded P1 sentence at four elements, and authority linkage is argued in core/05's
  exposition ("an authority with enforceable jurisdiction"). Narrowing to three discards design
  information the successor item itself called defensible.
- **Paper A's delta over Bovens halves.** The paper's stated contribution beyond Bovens is exactly
  authority linkage plus the design-time tense. Drop authority linkage from canon and half the
  stated delta has no canonical carrier — the related-work table, the mapping table, §7's quote,
  the supplement's appendix, and the track's rung 4 all rewrite. The claim's pin fires (statement
  is hashed).

### C — reconciled as different objects, the distinction stated in both

The term defines **what accountability is** — the relation that allocates a decision's consequence,
three parts at the definition's grain. The claim asserts **what a complete instance requires at
design time** — five conditions: the third part refined into stake plus sanction path (the split
core/05 §2 already carries), and authority linkage added as a completeness condition. Five is a
completeness test of the three-part relation, not a competing definition. The distinction lands in
both texts:

- **Claim side:** frame-08's statement gains the scoping words (e.g. "a **complete** accountability
  arrangement links…" / statement recast as completeness conditions of the relation the term
  defines); its notes record the ruling, the reason the term deliberately does not carry authority
  linkage, and the Bovens lineage (four of five his; authority linkage and the design-time tense
  not). The statement change fires the claim's downstream pin — a projected claim, the cheap kind.
- **Term side:** the term registry schema carries no `notes` field today (no entry uses one), so
  the term-side statement of the distinction goes in `core/05-accountability.md`'s prose beside the
  embed — exposition, which fires nothing — unless Emil prefers a schema addition (additive, like
  format 2's `canonical_home`), which is a spec question this session should not decide alone.

Costs:

- **The two counts remain visible** to an outside reader; what changes is that both texts now say
  which governs at which grain. This is the residual cost — smaller than A's or B's, but not zero:
  it requires the reader to accept a definition/completeness distinction rather than seeing one
  number.
- **The smallest firing surface.** No settled node moves; no E6 re-embed; the paper's mapping table
  stays exactly right (it already answers "refines-and-adds" — this ruling makes the addition
  licensed and states why); `DDD-hyp-04` is untouched (it already predicts on completeness).
  Frame-08's pin fires; rung 4's prose and the supplement's line-189 statement update to the new
  statement text.
- **core/05 §2's four-element bold sentence needs a disposition of its own** under any of A/B/C: it
  is exposition carrying a fourth count. Under C it reads naturally as the completeness statement
  minus authority linkage — a prose defect to flag in frame-08's `notes:` per the flag-don't-guess
  rule, or to repair in the prose as part of stating the distinction beside the embed.

## 4. What every disposition carries regardless

1. **The Bovens lineage lands in canon**, not only in the paper: frame-08's notes (and the term's
   establishing prose, under C) must state that four of the five elements are Bovens's and that the
   framework's additions are authority linkage and the design-time tense — no file may claim more.
2. **The supersession record**, whichever node moves, per DDD-dec-09/10/15: the superseded text
   stays in the graph with the correction that moved it.
3. **Sequencing with I-3:** the disposition lands upstream after v5.13.0, so it rides the close's
   version proposal; I-3's pin advance to v5.13.0 is unaffected and its two predicted W1 firings
   stay exactly as predicted.

**HOLD — awaiting Emil's ruling on A / B / C.**
