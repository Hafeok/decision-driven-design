# The ground migration — plan, deferred whole, filed as the successor's seed

**Filed 2026-08-27 by the ground-migration session**
(`meta/sessions/2026-08-27-ground-migration/`), on Emil's GATE 4 ruling. **Nothing was migrated.**
The plan is complete, the classification is execution-grade, and **a successor starts at execution.**

Filed here rather than only in the session directory because a successor must be able to find it
beside the audit it descends from: `meta/ground-audit-2026-08-24.md` and its erratum.

---

## What the successor does not have to redo

| | |
|---|---|
| **The vocabulary is settled** | SR-1…SR-7, plus `act-triggered` (filed), plus `denominations:` (filed) |
| **The classification is execution-grade** | 2,845 rows, residual zero by construction, reproducible: `meta/sessions/2026-08-27-ground-migration/w0-classify.py` |
| **The plan is written** | `gate4-plan.md` — every pin, every embed, every firing named |
| **The design rulings are answered** | six gates of them, in `gate1`…`gate5` |
| **The surprises are spent** | two senses nobody had, a compound the audit called absent, a translated defect, a definition layer 17 terms wide, an instrument with three named failure mechanisms |

---

## The migration, in one table

**SR-1 gives S1 the word; SR-2 says S3 is verbs applied to the S1 object. Prose that already names
the verb is already correct.** Measured over the 567 S2/S3 prose occurrences in canon and the
projection: **380 (67%) need no edit; 187 are bare and need re-expression.**

| Wave | Content | Size | Pins |
|---|---|---|---|
| **W1** | S5 → *deployment distribution* | 87 mutable, 29 in merged papers | `term:verdict` unpinned |
| **W2** | 11 registry entries + 11 embeds + upstream `core/` bare prose + **`apparatus/`** | 11 + 11 + 65 | **7 fire W6** |
| **W3** | projections, applications, papers, downstream `core/` | 122 bare | 0 |
| **W4** | `product-cli` | 1,203 | ruled separately |
| **never** | U (261, of which **142 identifiers**) + immutable (260) | 521 | — |

**Corrected counts, after W0 and W0-bis:** S2 1,529 · S1 **567** · S3 369 · U 261 · S5 97 · S4 **22**.
Canon is **S1-led** (182 S1 : 154 S3) and **canon's S4 is mechanically zero.**

### The seven W6, predicted and unfired

`term:actor` · `term:arrangement` · `term:capability` · `term:capacity` · `term:closure` ·
`term:judgment` · `term:residual-discretion`. **Zero W5, zero W7, zero W3.** All seven carry a
`content_hash`, so each advance is governed in the `DDD-dec-29` pattern.

**Add three that this session created and did not fire**, because the pin stays at `v5.9.0`:
`term:delivery`, `DDD-cost-09`, `DDD-delivery-01`. **Ten in total when the pin next advances past
both.**

### The seven S1 entries are not touched at all

`term:ground` · `term:admission-test` · `term:determination` · `term:act` · `term:tolerance` ·
`term:answerability` · `term:swarm-gate`.

---

## Four things the successor must not re-decide

1. **`apparatus/` is W2's, not W3's.** The audit booked it as *"rides with revisions already owed"*;
   it is where the delivered sense concentrates, and `encode-verify.md:21` carries the miscitation —
   *"Ground is the read-only surface an actor inspects in order to act (`core/00`)"*, an S2
   definition attributed to an S1 source. **W2 repairs that line or nothing does.**
2. **`poisoned ground` needs one sentence, not 66 edits.** SR-2 makes the compound already
   verb-shaped; what it needs is `term:poisoned-ground` saying which state it names.
3. **`ground channel` exists**, 10 occurrences, one inside `term:arrangement`'s settled text. The
   audit reported zero; the erratum records the correction.
4. **W1 is bound and has been found unavailable twice** — `v5.11.0` recorded `ground distribution` in
   four claim statements, one `established`; SR-5 additionally ties W1 to a paper revision. It is a
   real constraint, not an oversight.

---

## What §6 already landed, so the successor does not repeat it

Filed at `v5.12.0` (proposed): three Grade A definitions promoted; `mechanical` → `act-triggered` on
the delivery value with the store untouched; `denominations:` as an additive field with
`term:verdict`'s parenthetical moved in; the `README.md` judgment row and closure paraphrase; the
Danish double gloss. **None of it moved a `ground` occurrence.**

**Still open from §6's neighbours:** sweep 1's Grades B and C (7 entries, with their grading);
the `projection` and `verdict` collisions (both unpinned, `09`'s contract already disambiguates
`verdict|verdict function`); the drafting-warning instrument, which now needs **five** exceptions —
quotations, historical notes, ordinary English, the RDF `ground term`, the CSS surface colour.

---

## The method rule, for whoever writes the next instrument

> **A classification rule whose match window can cross a clause boundary is not an anchored rule, and
> the two classes cannot share an acceptance standard.**

Three mechanisms, all found by reading rows the instrument had already scored:

1. **Clause-crossing windows.** Rules written `ground\b[^.]{0,N}\bKEYWORD\b` assume `[^.]` stops at a
   sentence boundary. **It does not** — not at a comma, semicolon, dash, list item, `§`-ref, version
   number or decimal — so a 50–70 character window routinely spans two clauses and often two list
   entries. *"outcome variation across ground · epistemic uncertainty about a fixed **policy**"* is
   one list; the rule read it as one sentence.
2. **Rule ordering.** In an ordered first-match-wins table, any rule that can match an identifier
   steals rows from the identifier rule unless the identifier rule is **first**. The audit's was
   **last**: 15 steals and, symmetrically, 13 inverse steals. **Put identifier and immutability rules
   first.**
3. **Size and quality are uncorrelated.** A 60-row sample across a mixed table reported 29% correct
   where the truth was 72%, because two rules of 22 rows carried a tenth of the sample. **Report
   per-rule precision, never one figure for a table. A windowed rule earns a sample of its own.**

**This closes two mechanisms, not the possibility of a rare third.**
