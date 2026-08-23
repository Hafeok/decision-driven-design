# Successor items — Phase 1a session (2026-08-23)

Items raised at the Phase 1a session and deliberately **not** taken there. Each names the node or
document it lands against and the reason it was not done in-session. Nothing here is filed canon.

---

## 1. Freight — `validate-claims.py` enforces neither falsifier presence nor rule 1

**Ruled at GATE 1 (Emil): file the finding with its two instances as evidence.**

`spec/claim-format.md` §2 states two rules the validator does not check:

- **Rule 1 — one proposition per claim.** *"Compound statements split. The unit of status change
  must be the unit of statement."* Nothing checks that a `statement` carries one limb.
- **Falsifier presence.** Rule 2 requires `falsifier` for `projected` (or `test` for
  conceptual/normative kinds) and says nothing for `established`, so an `established` claim may
  carry no falsifier at all and no field records that it does not.

**Both defects in `DDD-measure-06` were visible from the schema alone, without a reviewer.** That
is what makes this the most reusable finding of the session: the external review found the node by
reading the argument, and the repository could have found it by reading the file.

**Instance 1 — the missing falsifier.** `DDD-measure-06` at `v5.9.0` carries
`format · id · kind · statement · status · region · evidence · test · owner · changed` and no
`falsifier`, `breaks`, `credits`, `supersedes`, or `notes`. It sat at `established` for five minor
versions with no stated observation that would fire against it.

**Instance 2 — the compound statement.** *"The measure exists iff the acceptance predicate
operationally closes; H(V) is undefined exactly where the framework's floor result locates non-zero
floor."* Two limbs joined by a semicolon, carrying different warrants — the first near-definitional
(the node's own evidence note says so), the second a coincidence with an independently derived
result. **One `status` field governed both**, which is exactly the failure rule 1 exists to prevent,
and it is the mechanism by which the node resisted repair: demoting it would have demoted the
sound limb, so nobody demoted it.

**Why rule 1 needs enforcing rather than merely stating — the durable half of this finding**
(Emil, GATE 3 ruling). A compound statement does not merely offend tidiness. It makes the node
*undemotable*: `DDD-measure-06`'s two limbs carried different warrants under one `status` field, so
demoting the node would have demoted the sound limb along with the unsound one. **That is how a
defect survives five minor versions in a repository that reviews its own canon** — not because
nobody saw it, but because the only available correction was worse than the defect. Rule 1 exists
to prevent exactly that, and a rule that is stated but not checked prevents nothing. **This is the
reason the instrument is worth building, and it should be the first line of its rationale.**

**What a checker could catch, and what it could not.** Falsifier presence is mechanical. Rule 1 is
not fully mechanical — but a heuristic flagging semicolon- and "and"-joined statements for human
review would have surfaced this node, and the false-positive rate is the design question rather
than an objection. **Deliberately not designed here**; the finding is filed, the instrument is the
freight session's.

**Not to be bundled with the status/kind separation** (review §7, triage §2). That is a registry
change with a wide blast radius and its own session. This is a validator gap in the *existing*
schema, and it is cheap.

---

## 2. `term:escape` — the reviewer's re-wording proposal

Review §4, closing paragraph: *"The two-register distinction is insightful, but it does not fully
repair the canonical phrase 'determined never, by nobody' while the paper also says the escaped
choice is determined by a default or draw. **'Ungoverned resolution' would be clearer than
'determined never.'**"*

**Not acted on.** `term:escape` is `settled`, established by `core/01`, and re-wording it is outside
this session's booked scope. The proposal is recorded because it is concrete and because the
finding attached to it is worth more than the proposal:

> **An external reader met the seam guard and still reported "determined never, by nobody" as
> conflicting.** The guard is doing its job for a reader who already holds the framework and not
> for one who does not. That is a finding about the guard's **audience**, not about its content,
> and it argues for the guard's exposition rather than against the guard.

The successor session should note that `DDD-frame-17` narrows the problem without solving it: the
retired mode list said escape was discharged by a *default or draw*, two of four; the successor
says **drawn**, one of three, and `drawn` is a control word rather than a governance word. The
collision between *determined never* and *the world always produces something* survives that
narrowing.

---

## 3. The unexpressed abstention — deferred, naming two nodes

**Ruled at GATE 1 (Emil): defer, and widen the successor's scope to name both nodes.**

An abstention that is never expressed sits outside `DDD-frame-17`'s region on the reading that
`term:act` runs an act *"to an expressed outcome"*. The reading follows `term:act` correctly and it
is **stated, not ruled**.

The tension it creates is why it defers. If an unexpressed abstention is not an act, **while the
determinable is nevertheless determined**, then determination happened with no act to index it —
which is **act-free discharge**, and `DDD-frame-16` denies exactly that. Three exits, and the
framework has not chosen:

1. The `term:act` reading is wrong, and an unexpressed abstention completes an act.
2. An unexpressed abstention determines nothing, and the determinable is simply still open.
3. `DDD-frame-16` needs a boundary it does not currently state.

**Nodes it lands against:** `DDD-frame-16`, `term:act-individuation`, `term:act`. Design question,
not a repair; the C-1 precedent.

---

## 4. Constraint on Q32's eventual filing — the closure ladder's axis error

**R-4, recorded and not repaired.** See `gate4-report.md` for the full record; restated here so the
Q-wave finds it with the other successor items.

Paper A §5.2's ladder runs open → verification-closed → constructively closed → **formally
decidable**. The paper already knows decidability is not the summit and still places it *on the
ladder*.

> **Constraint.** The Q32 constructive-closure node must be filed on a **single axis** —
> arrangement-indexed operational closure, with `verification-closed` and `constructively closed`
> as its rungs. **Formal decidability is not a rung and must not be filed as one.** It is a logical
> property of the predicate, true or false with no arrangement in the index; the other rungs are
> operational properties of an arrangement. `term:closure` already carries it correctly as a
> *reservation* — *"**Decidable** is reserved for the formal special case"* — rather than as a
> position. A Q32 node admitting decidability as a fourth rung reproduces Paper A §5.2's axis error
> in canon, where it is far more expensive to remove.

The error is in the Paper A Gate 1 ruling that set the ladder's structure, recorded as such in the
triage (§3), not in that session's execution.

---

## 5. Paper A's **four** block quotations, and the pin

**Not this session's work, and named so the revision session does not discover it late.**

Paper A block-quotes **four** passages this session changes, established by running the checker
against the session branch rather than by reading the manuscript:

| Line | Node | What it quotes | Repair cost at the revision |
|---|---|---|---|
| 365 | `DDD-frame-15` | the full statement | rewrite to `DDD-frame-17`'s three values |
| 274 | `DDD-frame-02` | the full statement | one clause |
| 310 | `term:residual-discretion` | the canonical text | replace with the corrected text |
| **1208** | `DDD-frame-15` | **the compact form alone**, disclosed-partial: *"… demand is never unmet, only ungoverned." [DDD-frame-15 — closing clause]* | **a one-token citation change** |

The fourth was missed at GATE 2, where a manual scan of block-quote runs found three. **The
checker found four.** The extra is Paper A §12's central sentence, and it is the cheapest of the
four to repair for the reason that makes it interesting: **the compact form is the one sentence
`DDD-frame-17` preserves verbatim**, so the citation moves and no prose does —
`[DDD-frame-15 — closing clause]` becomes `[DDD-frame-17 — closing clause]`.

`DDD-frame-15`'s retirement rewrites its statement per canon's retirement convention, so the first
and fourth quotations cannot survive as written.

The pin is therefore **held at `v5.9.0`** by this session. Paper A's revision session advances it,
having first rewritten those three quotations — which it must do anyway, since two of the three are
the very claims the review asks the paper to stop overstating.

---

## 6. Stale section numbers in the measure note's apparatus

`papers/measure-note/response-to-review.md` and `papers/measure-note/measure-paper-context.md`
refer to the boundary section as **§7 / §7.1 / §7.2**. In the note as merged it is **§8 / §8.1 /
§8.2** — the discharge session inserted §6 and everything below moved down one.

Bookkeeping in projection apparatus, not canon. Cheap, and it misled this session's own charter,
which is the argument for doing it.
