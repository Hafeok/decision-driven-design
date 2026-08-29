# Bootstrap — item 5: the ground migration (2026-08-27)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any repository is read for the work, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/ground-migration-item-5-jpa9tc` (all three repositories; the branch name was
  fixed by the invocation harness and is mirrored across the three so the set is one name)
- **Base commits:**
  - `actor-indexed-determination` — head `ce2c477540d7aeeba294a0aaaa470a1d353ba110`. Annotated tag
    `v5.11.0` resolves to **the same commit**; head and tag coincide, and canon at head is canon at
    `v5.11.0` exactly as the prompt asserts. Tag message: *"v5.11.0 — Retirement provenance, the
    validator, and what a status means"*, tagged by Emil Klein 2026-08-28.
  - `decision-driven-design` — head `e81a454aeab60522124ad032561bfb80e3a46dbd` (the item-4 merge,
    PR #30)
  - `product-cli` — head `d0f429741fd06e6d09d25937efcb61f440b94472`. **Read-only in this session.**
    W4 is assessed and reported at Gate 4; it is never executed here.
- **Gates:** 6 (G1 classification · G2 collision sweep · G3 §7/Q27 · G4 plan · G5 execution ·
  G6 close)
- **Principal:** Emil
- **Session type:** interactive canon curation, with an execution phase — hold at every gate, merge
  nothing
- **Input identity:**

  | File | Lines | sha256 |
  |---|---|---|
  | `prompt.md` | 169 | `7a7b34d96cba1addef2f4ad3f13e1e96627747991df51cd4f3b53b10141d1bde` |
  | package `README.md` | 52 | `89f1fef496e1064f62a70e842d8e80dcb9576eaee3aa61bf1776ac700cc31270` |
  | package `ground-terminology-recommendation.md` | 260 | `d8c43b1ebcdb41d7bad27ae3ca943b9047a95351504e4f7299de5481dd64316e` |
  | package `ground-terminology-assessment.md` | 171 | `1668b529cb2aaf61d44bbdb290010b7cc04753a12b5093e29e0a11998b94cc44` |
  | package `q44-act-and-verdict-ontology.md` | 212 | `4d49ded8c34ac0a48b096040932ca478eae5140ad5aa26f16302f2171a740af8` |
  | package `q45-routes-and-compositional-coverage.md` | 114 | `c5925b25656a53279f858b742f3cecd84acd2052ea7d2ead9ccfd5f0a52c051b` |
  | package `q46-encoding-price.md` | 127 | `699c39c0ec3b969beef837038bb89121ba29d02c06c46d6128153970c2a6aa81` |
  | package `act-and-verdict-ontology-explainer.md` | 222 | `644eabd6a70c74894ae195c3ddda72728932562786e974479041b329b5fe59b5` |

## Arrival — clean

The prompt arrived with the invocation, inside `item5-package.zip`, and is filed here with its
identity in this session's first commit. No supplementary input was named and none is missing.

Two package files duplicate artefacts already committed by the ground-audit session at
`meta/sessions/2026-08-24-ground-audit/` — the recommendation and the assessment. Both are
**byte-identical** to the committed copies (`d8c43b1e…` and `1668b529…` respectively, verified), so
they are not re-filed; the ground-audit copies are the ones cited throughout.

The remaining five package files exist in no repository, so they are filed under `inputs/` to make
this session's charter reconstructible, which is the whole of `DDD-dec-20`'s mechanism. **Filing
them here is not filing them as canon.** Q44, Q45 and Q46 are unfiled downstream demand and remain
so; the prompt puts their filing out of scope and this session rules *with their existence known*,
which is only possible if they are quotable at the gates.

## The invocation message, verbatim

Unzip the package and read README.md, then read prompt-ground-migration.md in its entirety — this
session follows that prompt exactly, including every gate and all seven standing rulings.

This is item 5: the ground migration. The audit is already done and its four design rulings are
made — this session executes them and stops where they run out. The finding that makes it necessary:
the remedy is definitional, not a prose repair. Fifteen settled terms carry four senses of one word
between them, including the term defining what an actor is.

First act, before anything else: commit this prompt and bootstrap to
meta/sessions/2026-08-27-ground-migration/ in decision-driven-design, per DDD-dec-20.

Fetch all three repos — actor-indexed-determination at v5.11.0 (verify and report the tag found),
decision-driven-design at head, product-cli (W4 assessment only, never executed here).

The standing rulings you inherit and do not re-litigate: S1 keeps the word; S3 is not a rival
primitive but verbs applied to the S1 object; reuse the v5.5.0 delivery vocabulary and mint nothing
beside it, with `basis` excluded as a candidate name; provenance is independent attributes, not an
enumeration; S5 leaves as deployment distribution and rides with a paper revision; node identifiers
never move — the migration renames the concept, not the identifiers; and counts are counted, never
estimated.

Other rules that override anything you might infer:
- Interactive curation with an execution phase. Stop at every gate for Emil's ruling. Merge nothing.
- G1 (completing the 1,022-occurrence classification) blocks everything. A sense boundary that moves
  against the sampled estimate is a finding, not an error — report and hold.
- G2's collision sweep reports with costs and repairs nothing. Two known collisions to confirm and
  price: `mechanical` (a store and a delivery type) and `judgment` (term versus DDD-frame-17's mode).
- G3's §7/Q27 reconciliation must settle here or Q27 files onto a dissolving category.
- G4 is the plan, not the cut. If the plan exceeds the session's budget, Emil rules defer-whole — a
  half-renamed concept is worse than an un-renamed one.
- W4 (product-cli's serialised `ground:` field, 660 occurrences) is a data migration and is NOT
  executed here. Report cost and options at Gate 4.
- Every candidate name is checked against the full registry before it is proposed, and the check is
  reported whether or not it fires. Two prior naming attempts died on exactly this check.
- State predicted W6/W7 results before any pin operation.
- Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

Begin with G1 and end your first report at GATE 1: the completed classification of all 2,845
occurrences, every unassignable case with its reason, and any sense boundary that moved.
