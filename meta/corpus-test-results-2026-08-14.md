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

— end of Gate 1 draft —
