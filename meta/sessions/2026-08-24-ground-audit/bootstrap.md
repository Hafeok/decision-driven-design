# Bootstrap — Phase 1b: the ground audit (2026-08-24)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any repository is read for the audit, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/ground-audit-phase-1b` (`decision-driven-design`; the only repository this
  session writes to)
- **Base commits:**
  - `actor-indexed-determination` — head `37f508e92645c169312095b4274223ba03c89e51`, **which is
    also tag `v5.10.0`**, cut by Phase 1a's release descriptor landing on the default branch. Head
    and tag coincide again, as they did at Phase 1a's arrival.
  - `decision-driven-design` — head `92c7b2e1e7abda871bf9ff409dd15c6319203a33` (the Phase 1a merge,
    PR #28)
  - `product-cli` — `d0f429741fd06e6d09d25937efcb61f440b94472`, **read-only**, surveyed for
    occurrence counts and never written
- **Gates:** 4 (enumeration and sense definitions · D-1 and D-2 · D-3 and D-4 · close)
- **Principal:** Emil
- **Session type:** interactive audit — hold at every gate, merge nothing, **change nothing**
- **Input identity:**
  | File | Lines | sha256 |
  |---|---|---|
  | `prompt.md` | 112 | `c64281bd58d080f41003745d7fddbdc4d8eda86b5d103974a3b9c8e275639a9e` |
  | `ground-terminology-recommendation.md` | 260 | `d8c43b1ebcdb41d7bad27ae3ca943b9047a95351504e4f7299de5481dd64316e` |
  | `ground-terminology-assessment.md` | 171 | `1668b529cb2aaf61d44bbdb290010b7cc04753a12b5093e29e0a11998b94cc44` |

## Arrival — clean, and the contrast is worth recording

**All three inputs arrived with the prompt**, in the same message, and are filed here with their
identity in this session's first commit.

Phase 1a's inputs did not: its bootstrap recorded the failure at arrival, the sixth instance of
`DDD-dec-17`'s class and the first since `DDD-dec-20` filed the convention against it. Recording a
clean arrival is not ceremony — the convention's value is that it distinguishes the two cases at the
moment they differ, rather than reconstructing which happened at close.

## What this session is, and is not

**It is an audit. It changes nothing.** No term is renamed, no claim is amended, and no file outside
`meta/sessions/` and the audit's own output is edited. `product-cli` is read and never written.

The deliverable is a classification of every occurrence of `ground` by sense, a counted cost table,
and the four design rulings the migration cannot proceed without. **The C-1 precedent governs**:
that carve deferred whole not because the file count was frightening but because unruled design
decisions sat inside it. Plan before cutting, and the plan is the product.

## Standing rulings inherited, not to be re-litigated

- **SR-1 — the split is ruled real; the rename is not ruled.** Three independent arrivals converge:
  the delivery work at `v5.5.0` (filed versus delivered, on the decision side), the Paper A review
  §6 (`G*` relevant world facts versus `G_A` accessible and delivered), and the terminology
  proposal. The audit takes the split as established and prices it.
- **SR-2 — `basis` is excluded as a candidate name.** `basedOn`, basis pins and basis loss already
  denote graph provenance among governance objects. Overloading the word recreates the defect the
  migration exists to repair. Neither `basis` nor `decision basis` is proposed.
- **SR-3 — one sense keeps the word.** Full retirement is not the working assumption. The audit
  reports which sense *should* keep it, with the argument; Emil rules.
- **SR-4 — the §7/Q27 collision is reported, not resolved.** Both texts are quoted. That ruling
  belongs to the migration session, before Q27 files.

## The five senses, as this session will apply them

Every occurrence is assigned exactly one, or flagged **unassignable** with its reason:

1. **Conditions in the case** whose variation moves the outcome past τ — the world-facing sense.
2. **Representations the arrangement holds** — records, observations, retrieved material.
3. **Representations delivered at the act** — what actually reaches the resolver.
4. **Institutional rules and standards** — acceptance criteria, policies, constraints.
5. **The population** over which demand is measured — the measure's `P`.

**An occurrence that will not sit in exactly one sense is the most valuable row in the table.**
Assignments are not forced.

**Counts are counted, not estimated.**

## Out of scope

The migration itself. Renaming anything. Amending any claim, term or document outside
`meta/sessions/` and the audit's own output. Resolving the §7/Q27 collision. Phase 1a's repairs. The
status/kind separation. The decoder repair. The Q-wave, the primer, Paper A's revision. Not bundled.

---

Read prompt-phase1b.md in its entirety — this session follows it exactly, including every gate.

This is the ground audit. It is an audit: it changes nothing. No term is renamed, no claim amended,
no file outside meta/sessions/ and the audit's own output is edited. The deliverable is a
classification of every occurrence of "ground" by sense, a counted cost table, and the four design
rulings the migration cannot proceed without.

First act, before anything else: commit this prompt and bootstrap to
meta/sessions/2026-08-24-ground-audit/ in decision-driven-design, per DDD-dec-20.

Fetch all three repos — actor-indexed-determination and decision-driven-design at head, product-cli
read-only for occurrence counts.

Standing rulings you inherit, not to be re-litigated:
- The split is ruled real (three independent arrivals: the delivery work at v5.5.0, the Paper A
  review §6's G*/G_A, and the terminology proposal). The rename is NOT ruled.
- "basis" is excluded as a candidate name — basedOn, basis pins and basis loss already denote graph
  provenance among governance objects, and overloading it recreates the defect the migration exists
  to repair. Do not propose basis or decision basis.
- One sense keeps the word; full retirement is not the working assumption. Report which sense should
  keep it, with the argument.
- The proposal's §7 versus Q27 collision is reported with both texts quoted and NOT resolved here.

Other rules:
- Interactive audit. Stop at every gate for Emil's ruling. Merge nothing.
- Classify each occurrence into exactly one of five senses — conditions in the case, representations
  the arrangement holds, representations delivered at the act, institutional rules, the population.
  An occurrence that will not sit in one sense is the most valuable row in the table. Do not force
  assignments.
- Counts are counted, not estimated.
- Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

Begin with step 1 and end your first report at GATE 1: raw occurrence counts per artefact before any
classification, and the sense definitions as you will apply them.
