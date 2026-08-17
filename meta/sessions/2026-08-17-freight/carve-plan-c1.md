# C-1 — the diachronic carve of `core/06` and `core/08`: plan and size estimate

**draft-pending-ruling.** Filed at GATE 1 per the manifest's gate rule for Batch C: *propose the
carve plan — what moves, what re-words, every embed re-projection — before cutting anything.*
Nothing has been cut. **Recommendation at the end: defer-whole.**

Governing rule: **R4, the boundary charter** (`DDD-dec-09`) — *the principle layer is synchronic and
stateless; any statement requiring anything to persist between acts files with the projection.*
Pattern: **supersession, not rewriting** (Wave-1 precedent, `DDD-dec-09`/`DDD-dec-10`; the escape
precedent, `DDD-dec-15`).

---

## 1. What is actually un-carved

### 1.1 `core/06-composition.md` — two sections

**§"The compound: harvesting the seam"** (:107–142). Diachronic by inspection: the five-step loop is
*over runs* (*"each cycle the seam gets cheaper per run"*), and `term:compound`'s canonical text says
so outright — *"the loop that harvests recurring seam-judgment into the encoded store over a
write-back channel … so that each cycle shrinks per-run judgment toward the floor."* Recurrence,
harvest, and cycle all require something to persist between acts.

*Except* the **matched-pair invariant** (:129–142). Read as a constraint on one arrangement at one
act — *an encoded seam with no check on it escapes what an actor at the seam was absorbing* — it is
synchronic and belongs upstream. Read as it is written — *"you may not **move** seam demand from
judgment to encoded without simultaneously allocating a mechanical check"* — it quantifies over a
change between arrangements, which is diachronic framing of a synchronic fact. **This needs a
ruling, not a decision procedure**: which of the two the invariant is, is a charter judgement on
ratified text.

**§"The channel is the platform"** (:145–161). Diachronic throughout: a write-back path *from
judgment into encoding* and an inheritance path *to the next run*; the three worked cases
(vertebrate immunity, CRISPR, vaccines) are all across-generation. Relocates whole.

`core/06`'s closing one-line (:190–194) names the compound and re-words with it.

### 1.2 `core/08-projections.md` — the organising thesis, not a section

This is the hard half, and it is why the item is booked as known-large.

`core/08`'s content **is** the pairing: *"They are not two mechanisms. They are the same mechanism —
the compound — viewed on two different axes."* The funnel is the depth axis, *within a single run*
(synchronic, stays). Maturation is the time axis, *across runs* (diachronic, goes). Removing one axis
is not an excision — it removes the document's thesis. The maturation half runs through seven of the
nine sections:

| Section | Lines | Maturation content |
|---|---|---|
| Header + `ddd:contract` | :1–25 | `establishes: [projection, funnel, maturation]`; *"the compound loop in composition (`06`)"* |
| §"The two projections" | :27–60 | The whole section. Three embeds; *"Maturation runs along the time axis (run N+1 is cheaper than run N)"* |
| §"The condition" | :138–158 | *"the same condition maturation carries, on the other axis"* + the joint statement of the two conditions |
| §"The diagnostic" | :160–192 | *"the runs where the compound was not happening"* |
| §"The two projections, stated for the record" | :196–215 | An entire **Maturation** subsection; *"Both are the compound"*; *"The funnel bottoms out at the floor; maturation converges to the floor"* |
| §"What stays unpinned" | :217–242 | *"the funnel and maturation each track one component"* |
| §"The one line" | :244–250 | The whole line is the pairing |

### 1.3 The `term:maturation` shadow

Live in **both** registries at head:

- upstream `core/graph/terms.yaml`:334 — *"the compound over **repetition**: pay once, and every
  future run is cheaper"*, `established_by: 08-projections.md`;
- downstream `core/graph/terms.yaml`:18 — *"the return channel spanning the act in reverse: from the
  mechanical store (post-act verdicts) into the encoded store (pre-act standing supply)"*,
  `established_by: 14-maturation.md`.

Emil's ruling of **2026-08-10** (recorded verbatim at
`meta/measure-note-related-work-2026-08-10.md`:96–126) fixes the disposition: the shadow is
**deliberate in destination** (`DDD-dec-11` governed the model's filing correctly) and **escaped in
mechanism** (no ruling governed ID reuse; the validator default resolved it), recorded as **known and
temporary**, with resolution **bound to this carve** — at which the upstream establishment *"retires
or re-words without the term"* and downstream's becomes sole.

That session's read-only sense check is on the record and still holds at head: every downstream
occurrence intends the local return-channel sense; **the upstream compound-over-repetition sense
appears nowhere downstream.** So the two establishments are genuinely different objects sharing an
ID — which is the cleanest case a carve can get, and it does not make the carve small.

---

## 2. The plan, if executed

### Upstream (`actor-indexed-determination`)

1. `core/06-composition.md` — relocate the harvest loop and the channel section; retain (or relocate)
   the matched-pair invariant per ruling; re-word the closing one-line; amend the `establishes:`
   contract line.
2. `core/08-projections.md` — the funnel survives; the document's frame does not. Seven sections in
   play, ~120 of 250 lines.
3. `core/graph/terms.yaml` — four entries: `term:compound` (relocates or retires), `term:maturation`
   (retires upstream per the 2026-08-10 ruling), `term:projection` (re-words — its canonical text is
   *"the same mechanism — the compound — run along two different axes"*, and both the compound and
   one axis leave), `term:funnel` (re-words — *"the compound over depth"* rests on a term that is
   going).
4. `core/README.md` — index lines :19 (`06`) and :20 (`08`).
5. `core/claims/DDD-measure-13.yaml` — *"The maturation/funnel asymptote is H(verdict) −
   I(verdict;S_encoded)"*. One claim, two projections, one of which relocates: re-scope, or split
   with the diachronic half filing downstream citing this ID as basis (the `DDD-cost-02`/`-03`
   precedent from `DDD-dec-09`).
6. `core/decisions/DDD-dec-19.yaml` (new) — the carve, R4 applied to `06`/`08` by supersession,
   recording the relocation and the shadow's closure.
7. `CHANGELOG.md` / `releases/v5.6.0.yaml`.

### Downstream (`decision-driven-design`)

8. A home for the relocated material — `core/14-maturation.md` extended, or a new numbered document.
   `core/14` already establishes maturation in the return-channel sense, so the upstream
   compound-over-repetition material has to be **reconciled with it, not appended to it**. That is
   the second design decision in this item.
9. `core/graph/terms.yaml` — `term:compound` established locally (ID moved, per `DDD-cost-04`'s
   precedent: *claims relocate, never renumber*), `term:maturation`'s local establishment becomes
   sole.
10. `graph/upstream.yaml` — pin set changes; ref advances to the new upstream tag.
11. `core/decisions/DDD-dec-20.yaml` (new) — adoption, the pin advance, and the shadow's closure.
12. `core/README.md`, `core/17-time-and-assurance.md` — cross-references.
13. `papers/measure-note/measure-paper-context.md`:179 — names the carve as pending; updates on close.

### Embed re-projections

Four, all upstream: `term:compound` (`core/06`:109), `term:projection` (`core/08`:32),
`term:maturation` (`core/08`:37), `term:funnel` (`core/08`:42). Downstream's `core/14`:43 embed of
its own `term:maturation` is **unaffected** — it embeds the local establishment. Both validators
re-run; upstream's W1 baseline (currently 59 warnings) re-baselines.

---

## 3. Size estimate

| Dimension | Estimate |
|---|---|
| Files touched | **13–15** across two repositories |
| Canon documents substantially re-worked | **2** (`core/06` partially, `core/08` structurally) |
| Term entries re-worded or relocated | **4** |
| Embeds re-projected | **4** |
| Claims re-scoped or split | **1** (`DDD-measure-13`) |
| Decision nodes filed | **2** (one per repository) |
| Release artefacts | upstream tag + downstream pin advance |
| Comparable prior work | `DDD-dec-09`'s cost carve — **which was its own session**, and moved a smaller surface (one document, no thesis loss) |

**The estimate is not the problem.** The problem is that three of the steps are **design rulings, not
freight**:

1. **What the matched-pair invariant is** — synchronic constraint or diachronic transition rule
   (§1.1). A charter judgement on ratified text.
2. **What `core/08` is after maturation leaves** — a document named *Projections* with one projection
   in it, a merge into `core/06`, or a re-titled funnel document. This is the thesis of a settled
   canon document, and no prior ruling reaches it.
3. **How the relocated compound reconciles with downstream's existing return-channel maturation** —
   two established senses meeting in one repository, where the destination already has a settled
   term, three settled sibling terms, and seven claims resting on them.

None of the three is answered by any recorded ruling. Each would be resolved in-session by an agent
inventing an answer — which is precisely the failure the session's own standing note names: *a
freight session that grows a design session inside itself has failed at its own job.*

---

## 4. Recommendation

**Defer-whole**, per the gate rule. Reasons, in order of weight:

1. **It is design, not freight.** Three unruled design decisions sit inside it. The manifest's own
   framing — *"nothing here is new design work"* — is false of C-1 alone, and C-1 is the one item the
   prompt marks as gated for exactly this reason.
2. **It consumes the session.** Batches A, B, D, E, F and G are 27 items, most of them small and all
   of them closable at their booked size. Executing C-1 first, or at all, puts them at risk for one
   item.
3. **Deferring costs almost nothing, and the plan is now filed.** The carve has been pending since
   the Wave-2 close flag and has cost nothing while pending; what it *was* missing — a scoped plan —
   this file supplies. A successor session starts from §1–§3 rather than from a flag.

**But one piece should not defer with it.** The 2026-08-10 ruling's **item 1** — the decision
*recording* the shadow as known-and-temporary, deliberate-in-destination and escaped-in-mechanism —
is a record, not a carve. It is one node, it is already fully specified by the ruling text, and B-4
needs it: B-4's new warning class is *"suppressible only by citing the governing decision ID"*, and
if C-1 defers whole with no such decision filed, B-4 either fires an unsuppressible warning on
`term:maturation` or ships with nothing to cite.

**Proposed split, for Emil's ruling:**

- **Defer:** the carve itself (§1.1, §1.2), all four term movements, both relocations, `DDD-measure-13`.
- **Take now, with B-4:** the shadow-record decision (downstream, one node), stating the disposition
  in the ruling's own terms and recording that resolution *remains* bound to the deferred carve.

This keeps the deferral clean, gives B-4 its citable ground, and files nothing the carve would have
to unpick.
