# Bootstrap — item 4: status, kind, and the validator (2026-08-25)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any repository is read for the work, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/prompt-item4-status-kind-vaquwe` (both repositories; the upstream branch name
  was fixed by the invocation harness and is mirrored downstream so the pair is one name)
- **Base commits:**
  - `actor-indexed-determination` — head `403dede40416c5f90ec51f7e2b2226ba7fadf6f3`. Tag `v5.10.0`
    is `37f508e92645c169312095b4274223ba03c89e51`; head is **three commits ahead of the tag**, and
    all three touch `README.md` only. Canon at head is therefore canon at `v5.10.0`, which is what
    the prompt asserts, but head and tag no longer coincide as they did at Phase 1b's arrival.
  - `decision-driven-design` — head `efb46682251c74d8396ecf90518a38d1c711eab7` (the Phase 1b ground
    audit merge, PR #29)
- **Gates:** 5 (survey and W1 ruling · I-1 · I-2 · I-3 and I-4 · close)
- **Principal:** Emil
- **Session type:** interactive canon curation — hold at every gate, merge nothing
- **Input identity:**
  | File | Lines | sha256 |
  |---|---|---|
  | `prompt.md` | 124 | `e80f86cbb721a1528bbe95ebe32d542babde724153464f9245226ed0da3d6dd8` |

## Arrival — clean

The prompt arrived with the invocation, in the same message, and is filed here with its identity in
this session's first commit. No supplementary input was named and none is missing.

## The scope correction, restated because it is the reason this session exists in this shape

An earlier triage claimed the claim registry needed a second field carrying **kind**, separate from
maturity. That was wrong. `kind` has existed since format 1, is populated on every claim in both
repositories, and spans ten kind×status combinations. The observation that prompted the triage was
about **Paper A's appendix**, which renders `id | status | statement` and no kind column — a
projection defect escalated into a schema defect without asking the graph.

**The session does not re-derive the schema change; there isn't one.** Where the prompt and the
triage conflict, the prompt governs, and the triage's §2 carries a correction note when its file is
next touched.

## What this session is

Four items on one surface — the claim schema, its validator, and how both are read from outside.

- **I-1(a)** — does `conceptual` split, giving definitions their own value? **Survey before
  proposing:** all 29 conceptual/projected claims read and classified first. If `conceptual` is
  coherent, say so and file nothing.
- **I-1(b)** — `retired` is a lifecycle state sitting in a maturity field, and the information loss
  is the argument. Options are drafted, not picked. Every option is tested against one question:
  **can a reader see, from the graph alone, that `DDD-measure-06` was once `established`?**
- **I-2** — the validator enforces neither falsifier presence nor `spec/claim-format.md` rule 1
  (single-limb statements). Both checks run against the existing corpus **before** being proposed as
  enforcing, with hit lists reported. A check that would fire on twenty ratified claims needs a
  migration plan, not a merge.
- **I-3** — `gen-appendix.py` gains a `kind` column; the appendix regenerates wholesale.
- **I-4** — a short, honest statement of what the status values mean to an outside reader, anchored
  on the fact that `established` is four claims, all `formal`.

**Nothing in this session edits a claim statement.** Headers, schema, validator, appendix and
documentation only. The ordering is mechanical: this session touches every claim file's *header*,
and the ground migration touches statements, regions and notes in the same files. Schema final first
means the migration never re-touches what it just edited.

## Standing constraints inherited, not to be re-litigated

- **The pin stays at `v5.9.0`.** Paper A's appendix regenerates against the pinned ref, and its four
  known-failing quotations against `v5.10.0` stay failing — Phase 1a's predicted state, not a defect
  introduced here.
- **Predicted W6/W7 results are stated before any pin operation**, not after.
- **Supersession, never rewriting.** Retired claims stay in the graph with the correction that
  killed them; IDs are never reused.
- **Drafts are committed before each gate report**, bodies marked draft-pending-ruling.

## Optional warm-up — W1

The ground audit's W1 (the population sense leaving for **deployment distribution**) is independent
of I-1 to I-4: 105 occurrences, zero identifiers, zero pins, one in `product-cli`, 29 in merged
papers. Emil rules at Gate 1 whether it is taken here. If taken, it is **its own commit and its own
gate**, and mixes with no I-item commit.

## Out of scope

The ground migration (item 5) and its W0 classification grind. Paper A's revision, including the pin
advance and the four failing quotations. The measure decoder repair. The Q-wave. The primer. The
carve. The NGO transfer. Not bundled.

---

Read prompt-item4-status-kind.md in its entirety — this session follows it exactly, including every gate.
Read the scope correction first. An earlier triage claimed the registry needed a new `kind` field separate from maturity. That was wrong: `kind` has existed since format 1, is populated on every claim in both repos, and spans ten kind×status combinations. The reviewer's observation was about Paper A's appendix, which renders no kind column. Do not re-derive a schema change; there isn't one.
Four items: whether `conceptual` splits to give definitions their own value; whether `retired` — a lifecycle state sitting in a maturity field — should move, given that a retired claim's prior maturity is currently unreadable; the validator gap on falsifier presence and single-limb statements (Phase 1a's freight item, folded in deliberately because it is the same surface); the appendix rendering `kind`; and a short honest statement of what the status values mean to an outside reader.
First act, before anything else: commit this prompt and bootstrap to meta/sessions/2026-08-25-item4/ in decision-driven-design, per DDD-dec-20.
Fetch both repos at head — actor-indexed-determination at v5.10.0 (verify and report the tag found) and decision-driven-design at head.
Rules that override anything you might infer:

* Interactive canon curation. Stop at every gate for Emil's ruling. Merge nothing.
* Survey before proposing on I-1(a): read all 29 conceptual/projected claims and report how many are definitions before proposing any split. If `conceptual` is coherent, say so and file nothing.
* I-1(b) tests any option against one question: can a reader see from the graph alone that DDD-measure-06 was once `established`?
* I-2's two checks run against the existing corpus BEFORE being proposed as enforcing, with hit lists reported. A check that would fire on twenty ratified claims needs a migration plan, not a merge.
* Nothing in this session edits a claim statement. Headers, schema, validator, appendix, documentation only.
* The pin stays at v5.9.0; Paper A's four failing quotations against v5.10.0 are Phase 1a's predicted state, not a defect here.
* State predicted W6/W7 results before any pin operation.
* Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

Begin with step 1 and end your first report at GATE 1: the verified kind×status table, the 29 conceptual claims classified, the four retired claims with prior statuses recovered from history, both I-2 hit lists, and your recommendation on whether to take W1 here.
