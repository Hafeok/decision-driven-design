# GATE 4 — the migration plan

**Status: draft-pending-ruling. This is the plan, not the cut.** Nothing in canon is touched by this
gate. Read at `ce2c477` (= `v5.11.0`), `e81a454`, `d0f4297`, on the classification
`w0-classify.py` produces.

---

## 1. The finding that resizes the whole migration

**SR-1 gives S1 the word. SR-2 says S3 is not a rival primitive but *verbs applied to the S1
object*. Put together, those two rulings mean that prose which already names the verb is already
correct** — *"an actor **reading** ground"*, *"the ground **at the act**"*, *"**held at fixed**
ground"*, *"**available** ground", *"ground **channels**"*. Nothing in those sentences moves.

Measured over the 567 S2/S3 prose occurrences in canon and the projection, excluding immutable rows
and identifiers:

| | | |
|---|---|---|
| **already qualified** by a verb or adjective within 40 characters | **380** | **67%** — no edit |
| **bare** — the reader must infer the state from the sentence | **187** | **33%** — needs re-expression |

> **The migration is 187 prose decisions in canon and the projection, not 684.**

**This is SR-2 paying for itself.** The audit priced the migration at *"~2,357 migrating
occurrences, mostly re-expression"*. Two thirds of that re-expression turns out to be already
written, because canon's own habit is to say what is being done to the ground rather than to name a
state. **The expensive disposition Emil took with the cost in view is cheaper than the cost he
accepted.**

---

## 2. The corpus, dispositioned

| | Rows | Disposition |
|---|---|---|
| **S1** | **567** | **Keeps the word. No edit, no pin, no re-projection.** |
| **U** | **261** | Never migrated. 142 are `DDD-ground-NN` identifiers, unmigratable at any price |
| **immutable** | **260** | Session records and release descriptors: classified, never touched |
| **S2 + S3 prose, qualified** | 380 | Already correct under SR-1 + SR-2 |
| **S2 + S3 prose, bare** | **187** | **The migration's real body** |
| **S5** | 97 (87 mutable) | → *deployment distribution* |
| **S4** | 22 (20 mutable, **0 in canon**) | Dissolves into provenance attributes (SR-4) |
| **`product-cli`** | 1,203 | **W4. Priced below, not executed.** |

---

## 3. The waves, redrawn on the corrected counts

The audit's table is superseded in three places: `apparatus/` moves, S4 disappears, and W2 shrinks.

| Wave | Content | Size | Pins | Notes |
|---|---|---|---|---|
| **W1** | S5 → *deployment distribution* | 87 mutable, **29 in merged papers** | `term:verdict` **unpinned** | SR-5: rides with a paper revision, which is **out of this session's scope** |
| **W2** | the definitional repair: 11 registry entries + 11 embeds + upstream `core/` bare prose | 11 + 11 + **65** | **7 fire W6** | The most expensive to get wrong |
| **W3** | `apparatus/`, projections, applications, papers, downstream `core/` | **122** bare | 0 | **Re-booked from the audit — see §5** |
| **W4** | `product-cli` | 1,203 | — | **Not executed. §7** |
| **never** | U (261) + immutable (260) | 521 | — | |

### W2's registry work, exactly

**Seven pinned entries whose canonical text moves. Predicted firing, stated before any operation:**

> **Exactly seven `W6`, on `term:actor`, `term:arrangement`, `term:capability`, `term:capacity`,
> `term:closure`, `term:judgment`, `term:residual-discretion`. Nothing else. Zero `W5`** — no pinned
> status moves. **Zero `W7`** — no local id is added or shadowed. **Zero `W3`** — every entry keeps
> its single embed site.

All seven are instrumented (each carries a `content_hash`), so each firing is a governed advance in
the `DDD-dec-29` pattern and not undetected drift. Four further entries move and are **unpinned**:
`term:encode-verify-split`, `term:overflow`, `term:poisoned-ground`, `term:verdict`.

**Eleven embed re-projections, all in upstream `core/`**, one site each: `00-primitives.md` ×3,
`11-the-floor-mechanism.md` ×2, `01-the-principle.md`, `03-the-floor.md`, `09-the-measure.md`,
`10-cost.md`, `14-indexed-determination.md`.

**The seven S1 entries are not touched at all**: `term:ground`, `term:admission-test`,
`term:determination`, `term:act`, `term:tolerance`, `term:answerability`, `term:swarm-gate`.

### `poisoned ground` — a decision, not 66 edits

The audit put it on the must-touch list because **its sense changes without its text changing**: an
S3 compound of an S1 head word, 66 occurrences at 100% S3 purity. Under SR-2 the compound is
*already* a verb-shaped construction (*"ground that is **present but false**: the substrate a
determination **reads**"*), so the text stands. **What it needs is one sentence in `term:poisoned-ground`
saying which state it names** — one entry, unpinned, one embed. Not sixty-six edits.

---

## 4. Order of operations

1. **The separately-ruled items** (§6) — they do not depend on the rename and three are already ruled.
2. **W2's registry**, one entry at a time, each with its predicted firing stated first, then the
   embed re-projected, then `validate-core-order.py` re-run.
3. **W2's upstream `core/` prose** — 65 bare occurrences, after the registry, because the registry
   is what the prose must agree with.
4. **The pin advance**, as one decision node citing all seven W6 firings, in the `DDD-dec-29` pattern.
5. **W3**, downstream, after the pin advance lands.
6. **W1** only when a paper revision carries it (SR-5), which is out of scope here.
7. **W4** never in this session.

**The seam that must not be crossed:** upstream lands and is accepted before downstream advances its
pin. Every prior session in this programme has followed that order and `graph/upstream.yaml`'s own
header requires it.

---

## 5. `apparatus/` — the re-booking Emil ordered at GATE 1

The audit booked `apparatus/` into **W3**, *"rides with revisions already owed"*. W0 found it is
where the delivered sense concentrates; W0-bis corrected the size but not the direction.

**Re-booked: `apparatus/` moves to W2's tail, not W3's.** Its five documents —
`tool-surfaces.md`, `tool-contract.md`, `encode-verify.md`, `the-skill-floor.md`,
`prefix-stability.md` — carry the vocabulary the definitional repair is *about*, and
`encode-verify.md:21` carries the miscitation the audit found (*"Ground is the read-only surface an
actor inspects in order to act (`core/00`)"* — an S2 definition attributed to an S1 source). **That
line is repaired by W2 or it is not repaired at all**, because W3 rides with revisions that are
themselves out of scope.

---

## 6. The separately-ruled items — independent of the rename

**Each was ruled on its own merits. None depends on the concept moving.**

| | Work | Pins |
|---|---|---|
| **Sweep 1 Grade A** *(ruled in)* | `term:seam`, `term:composite-actor`, `term:projection` — promote a definition into each | **0** — all three unpinned, one embed each |
| **`mechanical` → `act-triggered`** *(ruled in)* | `term:delivery`'s canonical text and alias list; ~49 occurrences across three repos | **1 W6**, on `term:delivery`. `term:mechanical` is **not touched** — the store keeps its word |
| **`denominations:` field** *(ruled in)* | `spec/claim-format` addendum; move `term:verdict`'s inline parenthetical into the field; validator check | **0** — `term:verdict` unpinned |
| **The erratum pointer** *(filed)* | done at GATE 3 | 0 |
| **README.md** *(ruled in, C5)* | 19 occurrences, **five senses on one public page** — S1×8, S2×4, S3×4, S5×1, U×1 | 0 — outside `core/` |
| **i18n** *(C4, book or defer by name)* | `ordliste-dansk.md:17` glosses both senses in one entry; 2 occurrences | 0 |

**`denominations:` has a second consumer beyond the primer**, and it is the cheapest repair of the
`projection` collision: moving `term:verdict`'s *"(in the engineering **projection** …)"* out of
canonical text stops the word doing denomination duty inside a settled entry.

---

## 7. W4 — priced, not executed

**1,203 mutable occurrences in `product-cli`, 1,181 of them S2 (98%).** The repository is
essentially monolingual, which is what makes the option below real.

| | |
|---|---|
| **The field** | `ground:` in `.ddd/` predicates and `.decisions/` sets — **the audit's 660 occurrences across 70 files**, a serialised key, not prose |
| **Code** | `product-core/src/ground/` (a module path), `ground-cli` (a **published binary name**), `Ground`/`Ground::Characterised` (Rust types), `crate::ground::*` (57 import paths) |
| **The risk** | **the only edit in this programme that can break something already running** |

**Three options, unchanged in shape by the corrected counts:**

- **A — full data migration.** Rename the field, the module, the binary and the types; write a
  reader that accepts both keys for one release. Correct, and the largest single body of work in the
  programme.
- **B — the field stays, the concept is renamed**, at the price of a **documented divergence**. The
  audit surfaced this without recommending it. **The corrected counts strengthen it**: `product-cli`
  is 98% one sense, so the field name is unambiguous *inside* that repository, and the divergence is
  a seam note rather than a live confusion.
- **C — defer W4 entirely** and revisit when the ledger next changes format.

**Two findings W4 must carry**, both from this session: `floor` collides inside `product-cli`
(`tolerance_floor` §4.2.1 against the Polanyi floor §3.5, **168 files**), and two further objects sit
under `ground` there — the RDF `ground term` (11) and the CSS surface colour (6). **Option B does not
dispose of those**; they are local collisions and are ruled with W4 or not at all.

---

## 8. The head delta, classified — C7 discharged

**+133 across 11 files. 106 are immutable or the audit's own output. 27 are live, in 4 files.**

| | |
|---|---|
| `upstream/README.md` **+17** (2 → 19) | **The migration surface that did not exist when the audit was taken.** Five senses on one page, and it embeds two registry definitions: `term:closure`'s *"relevant ground is observable"* (S2) beside line 7's *"determines choices against ground"* (S1). **Ruled into this migration at GATE 1 — it is the transfer's front door** |
| `upstream/core/decisions/DDD-dec-31.yaml` **+3** | All three are `DDD-ground-0N` identifiers. **U. No work** |
| `downstream/meta/successor-items-*.md` **+25** | Downstream meta prose; migrates with W3 |
| `downstream/meta/ground-audit-2026-08-24.md` **+61** | The merged artefact. **Not edited** — its erratum is filed and now carries a forward reference |

---

## 9. The size, honestly, against the C-1 precedent

**What the plan is:**

| | |
|---|---|
| 187 | bare prose re-expressions, canon + projection — **each a judgment about how to re-say a sentence**, not a replacement |
| 11 | registry entries superseded, of which **7 are ratified canon under a live pin** |
| 11 | embed re-projections |
| 7 | `W6` firings, needing one decision node in the `DDD-dec-29` pattern |
| 87 | S5 occurrences that cannot land without a paper revision **that is out of scope** |
| ~49 | the `mechanical` repair, with its own pin |
| 3 + 1 + 19 + 2 | Grade A · `denominations:` · README · i18n |

**Against the precedent.** `DDD-dec-29` records what **one** pinned registry entry cost: a decision
node, an Appendix A regeneration, a manuscript re-quote, and a predicted-then-verified firing.
**This plan has seven of those, plus 187 prose rulings in ratified canon and merged papers.**

**My assessment, for the ruling and not in place of it: the migration proper exceeds what this
session can execute at the standard it has held.** The reasons are specific rather than general:

- **Every one of the 187 is a ruling, not an edit.** SR-2 means the question at each site is *does
  this sentence need a qualifier, and which one* — and the vocabulary Q2 settled (`available`,
  `delivered`, `undelivered`) has never been applied to a single canon sentence. The first twenty
  would set precedents the remaining 167 would inherit, unreviewed.
- **W1 cannot land at all** without bundling a paper revision the prompt puts out of scope, so S5 —
  the cheapest wave, and the one the audit said could go early and alone — is unavailable here.
- **The half-renamed risk is real and asymmetric.** A registry that says *delivered ground* while
  `apparatus/` still says bare *ground* is worse than one where neither does, and `apparatus/` is
  exactly the body the re-booking just moved into W2.

**The recommendation is therefore: defer the migration whole, and land §6.** The separately-ruled
items are not the migration: each was ruled on its own evidence, none moves the concept, and three of
them (Grade A, `mechanical`, `denominations:`) Emil ruled *into* this session explicitly. **Whether
"defer whole" reaches them is Emil's to say, and it is the one question this gate cannot answer for
itself.**

**What a successor session inherits if it defers.** This is the argument that the deferral is cheap:

- **the vocabulary is settled** — SR-1 through SR-7, plus `act-triggered`, plus `denominations:`;
- **the classification is execution-grade** — 2,845 rows, residual zero by construction, reproducible;
- **the plan is written** — this document, with every pin, every embed and every firing named;
- **the surprises are spent** — two senses that nobody had (RDF, CSS), a compound the audit reported
  as absent, a translated defect, a definition layer 17 terms wide, and a classification instrument
  with three named failure mechanisms.

**A successor starts at execution.** The audit said an audit was worth running *even if the migration
then defers*, because it makes the design rulings answerable. The same holds one level up: this
session made them answerable **and answered them**.

---

## 10. The twenty-three carried items, dispositioned

| | Item | Disposition |
|---|---|---|
| C1 | `apparatus/` re-booked | **Done — §5.** W2's tail, not W3 |
| C2 | why S3's estimate was low | Recorded; superseded in size by C19 |
| C3 | `ground channel`, 10 occurrences | **In W2** — `term:arrangement` is one of the seven pinned entries |
| C4 | the i18n gloss | **Booked in §6.** Two occurrences, no pin |
| C5 | `README.md` | **In §6 and §8.** Five senses, one public page |
| C6 | SR-4's warrant | Recorded; the five two-sense occurrences dissolve with S4 |
| C7 | the head delta | **Discharged — §8** |
| C8 | sweep 1's grades | Grade A in §6; B and C to freight with their grading |
| C9 | `mechanical` → `act-triggered` | **In §6.** 1 W6, on `term:delivery` |
| C10 | `projection`, `verdict` | To freight — and `denominations:` repairs `projection`'s half cheaply |
| C11 | `judgment` closed | No work |
| C12 | five exceptions | Rides with the drafting-warning instrument, which is W2's |
| C13 | `floor` in `product-cli` | **In §7** — W4's assessment |
| C14 | Q-1, Q-2 | Q-1 **filed**; Q-2 **in §6** |
| C15 | the reconciliation | Q27 cleared to file; strike `rules` from the supply list — one word, in W2 |
| C16 | S4 dissolves | **Four senses plus attributes.** §2, §3 |
| C17 | W0-bis blocking | **Discharged** |
| C18–C23 | W0-bis's findings and the method rule | **In the manifest**, §11 below |

---

## 11. What this gate asks

1. **The plan**, §3–§8, on the corrected counts.
2. **The re-sizing at §1** — 187, not 684, because SR-2 already did two thirds of the work.
3. **The size ruling.** My assessment is that the migration proper exceeds this session.
   **Execute, or defer whole?**
4. **If defer-whole: does it reach §6?** The four separately-ruled items were ruled on their own
   merits and Emil ruled three of them into this migration. **They can land without the rename.**
5. **W4: option A, B or C** — priced, not executed, with the two local collisions named.

**Nothing repaired. Nothing merged.**
