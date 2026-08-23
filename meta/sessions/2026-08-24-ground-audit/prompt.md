# Session prompt — Phase 1b: the ground audit

Repositories: `actor-indexed-determination` (upstream, head) and `decision-driven-design`
(downstream, head). `product-cli` is surveyed read-only for occurrence counts. Fetch all three.
Inputs Emil uploads: `ground-terminology-recommendation.md` (the external proposal) and
`ground-terminology-assessment.md` (Claude's assessment — ruled where this prompt says so).
Session type: **interactive audit.** Hold at every gate. British spelling; one idea per sentence.
**First act, before Gate 1:** commit this prompt and bootstrap to
`meta/sessions/2026-08-24-ground-audit/` in `decision-driven-design`, per DDD-dec-20.

## What this session is and is not

**It is an audit. It changes nothing.** No term is renamed, no claim is amended, no file outside
`meta/sessions/` is edited. The deliverable is a classification, a cost table, and the design
rulings that the migration (item 5) cannot proceed without.

The C-1 precedent governs: that carve deferred whole not because the file count was frightening but
because unruled design decisions sat inside it. The same is true here. **Plan before cutting, and
the plan is the product.**

## Standing rulings this session inherits

**SR-1 — the split is ruled real, the rename is not ruled.** Three independent arrivals converge on
`ground` carrying several objects: the delivery work (v5.5.0, filed versus delivered on the decision
side), the Paper A review §6 (`G*` relevant world facts versus `G_A` accessible and delivered), and
the terminology proposal. The audit takes the split as established and prices it.

**SR-2 — `basis` is excluded as a candidate name.** `basedOn`, basis pins, and basis loss already
denote graph provenance among governance objects — which claims a node rests on. Overloading it with
"the facts an arrangement holds" recreates the ambiguity the migration exists to repair, on a word
that is already load-bearing. Do not propose it; do not propose `decision basis`.

**SR-3 — one sense keeps the word.** Full retirement is not the working assumption. The audit
reports which sense *should* keep it, with the argument, and Emil rules.

**SR-4 — the §7/Q27 interaction is out of scope here.** The proposal's §7 relocates institutional
rules out of ground; Q27 (unfiled) gives institutional ground a mechanism *as* ground. The audit
**reports the collision with both texts quoted** and does not resolve it — that ruling belongs to
the migration session, before Q27 files.

## The senses to classify against

Every occurrence is assigned exactly one, or flagged as unassignable with the reason:

1. **Conditions in the case** whose variation moves the outcome past τ — the world-facing sense.
2. **Representations the arrangement holds** — records, observations, retrieved material.
3. **Representations delivered at the act** — what actually reaches the resolver.
4. **Institutional rules and standards** — acceptance criteria, policies, constraints.
5. **The population** over which demand is measured — the measure's `P`.

An occurrence that will not sit in exactly one sense is the most valuable row in the table; it is
what the migration will be hardest on. Do not force assignments.

## Deliverables

### D-1 — the classification
Every occurrence of `ground` and its compounds (`declared ground`, `accessible ground`, `missing
ground`, `poisoned ground`, `ground provenance`, `ground channel`, `ground coverage`, `ground
distribution`, `institutional ground`, `ground registry`, and any others found) across: the term
registry; every core document; every claim and decision statement, region, falsifier and notes; the
apparatus documents; both papers; the axis registry; the G-track PRD; `product-cli`. Per row:
location, sense, and whether the occurrence is in canonical text (expensive to move) or prose
(cheap).

### D-2 — the cost table
Per sense: occurrence count, how many are canonical text, how many sit inside cut tags, how many
appear in merged papers, how many would fire W6/W7 on migration, and how many embeds would need
re-projection. **Counted, not estimated.**

### D-3 — the design rulings, stated as questions with the evidence attached
At minimum:
- **Which sense keeps `ground`?** The assessment recommends the world-facing sense — the registry
  declares dimensions of variation, `DDD-ground-05` says declaring them precedes determining over
  them, and Johnson's determinable (v5.7.0) already gives that sense its formal structure. Report
  whether the occurrence counts support that or contradict it.
- **How do senses 2 and 3 name themselves against the existing delivery vocabulary** (`term:delivery`,
  `term:undelivered`, `term:presumed-discharge`, v5.5.0)? Reuse rather than mint beside it.
- **Is provenance an enumeration or several independent attributes?** The proposal argues the latter
  (a controlled variable may also be observed; an institutional record may contain an inference).
  Report against `DDD-dec-26`'s ruled partition, which made the taxonomy ineligible for minting.
- **Does sense 5 simply leave?** `P` as *deployment distribution* looks separable at near-zero cost;
  confirm or refute from the counts.

### D-4 — the migration's own shape
Whether it is one session or a wave; what would have to defer; and whether any part can land early
at low cost (sense 5 is the candidate). **A recommendation, not a decision.**

## Walk

1. **Fetch, inaugurate, enumerate.** All three repos; session record committed. Raw occurrence
   counts per artefact before any classification, so the classification's coverage is checkable.
   **GATE 1 — hold on the enumeration and the sense definitions as the session will apply them.**
2. **D-1 and D-2.** Classification and costs, committed as the table grows. **GATE 2 — hold on the
   complete table with unassignable rows flagged.**
3. **D-3 and D-4.** The design rulings with evidence; the §7/Q27 collision reported with both texts.
   **GATE 3 — hold.**
4. **Close.** The audit document filed in `meta/` beside the holding notes; branch, PR, manifest.
   **No canon file is touched. GATE 4 — hold.**

## Out of scope

The migration itself. Renaming anything. Amending any claim, term, or document outside
`meta/sessions/` and the audit's own output. Resolving the §7/Q27 collision. Phase 1a's repairs. The
status/kind separation. The decoder repair. The Q-wave, the primer, Paper A's revision. Do not
bundle.

## Standing note

Commit drafts before reporting at each gate, bodies marked draft-pending-ruling. This session's
whole value is that it is cheap and changes nothing: it converts a terminology argument into a
counted table and four answerable questions. If the counts show the migration is larger than the
proposal assumes, that is the finding, and it is worth more than a partial rename.
