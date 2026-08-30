# GATE 5 — §6 executed

**The migration deferred whole. These are the repairs that surfaced during it.**

**The boundary held.** Nothing in this gate re-expressed a bare S2/S3 occurrence. **No occurrence of
`ground` changed sense or wording anywhere in either repository.** Repair what contradicts itself;
never resolve what is merely unqualified.

---

## Predicted before operating, and verified after

> **Prediction: zero `W5`, zero `W6`, zero `W7` in this session** — the downstream pin resolves
> against `ref: v5.9.0`, and this session neither advances the pin nor cuts a tag, so nothing here
> is visible to it.

**Verified:** `upstream 67 pins resolved against the pinned ref, 0 basis-loss, 0 content-drift,
1 shadowed id(s)` — the shadowed id being `term:maturation`'s governed `DDD-dec-21` shadow,
unchanged.

**A correction to GATE 4's prediction, and it is a real one.** GATE 4 stated *"exactly seven W6"*.
That prediction attaches to the **pin advance**, which is a separate operation this session does not
perform. **The seven belong to the deferred migration, not to §6.**

**The deferred firing §6 itself creates, stated now so the successor inherits it rather than
discovering it:**

> **When the pin is next advanced past these commits, exactly three `W6` fire and no more:**
> **`term:delivery`**, **`DDD-cost-09`** and **`DDD-delivery-01`** — the three pinned objects whose
> `statement` or `canonical_md` moved.

**What does not fire, and why**, since the digest covers `statement`, `region` and `canonical_md`
only: `DDD-delivery-01`'s **notes** moved and notes are not hashed; `DDD-delivery-03` moved and is
**unpinned**; the three Grade A entries moved and **none is pinned**; `term:verdict` moved and is
**unpinned**.

---

## What landed

### 1 · Sweep 1 Grade A — three terms that never defined themselves

Each definition **promoted byte-for-byte from its own establishing document**, never authored. Each
entry is now definition-then-claim, which is `term:floor`'s repaired shape.

| Term | Promoted from |
|---|---|
| `term:seam` | `06` §"The seam-demand identity": *"splitting a task or an actor manufactures new governing decisions — the ones about how the parts coordinate — that did not exist when the thing was whole"* |
| `term:composite-actor` | `06` §"Composition at one act": *"from outside the declared boundary, the composite is **one actor**: one capability envelope, one verdict owed"* |
| `term:projection` | `08` §"The one line": *"the same compound — pay once, inherit thereafter — drawn on two axes"* |

All three embeds re-projected. **All three unpinned; nothing fires.** `term:projection`'s sharper
definition also helps the deferred `projection` collision: a reader can now tell which object is
meant without the rename.

### 2 · `mechanical` → `act-triggered`, on the delivery value only

**The store keeps its word.** `term:mechanical` is untouched, and `term:compound`'s *"a mechanical
**check**"* is correctly retained — it is the store.

`term:delivery`'s canonical text and aliases move: `mechanical delivery` out, `act-triggered
delivery` in. The weakest-edge clause is restated as *"a path from a decision to an act is
act-triggered only if **every** edge on it is"*, which preserves its meaning exactly rather than
carrying the old adjective into a new frame.

**Reuse, not minting**, as ruled: `DDD-cost-09` already read *"where the check is **act-triggered**"*,
and `13-delivery.md` already read *"act-triggered in CI, actor-triggered locally"*.

**Edited:** upstream `term:delivery`, `13-delivery.md`, `DDD-cost-09`, `DDD-delivery-01`,
`DDD-delivery-03`; downstream `DDD-delivery-04`, `DDD-track-01`.

**Deliberately not edited, and this is a ruling not an omission:**

- **`product-cli` (7 occurrences)** — the prompt makes that repository assessment-only. Its
  occurrences ride with W4.
- **Session records, `meta/corpus-test-results-2026-08-14.md`, `meta/vocabulary-delivery-session-2026-08-15.md`,
  and `meta/holding-note-ground-axes-rev18.md`** — these record what v5.5.0 filed, and v5.5.0 filed
  `mechanical`. **Correct as history**, exactly as `judgment`'s retired-mode mentions were ruled at
  GATE 2. The holding note additionally carries a recorded `sha256` in `DDD-dec-20`'s notes, so
  editing it would break its filed identity.
- **`papers/paper-a/paper-a.md:1347`** — Appendix A is **generated from the pinned upstream**, which
  is `v5.9.0`. It legitimately still reads `mechanical delivery` and will change when the pin
  advances and the appendix regenerates. **Hand-editing it would forge agreement the pin does not
  yet have** — which is the pin's whole purpose.

### 3 · A finding, made while making the repair

> **`core/13-delivery.md` used `mechanical` in exactly two places: its contract's `requires` list,
> and the delivery value. It never used the store at all.**

The contract declared a dependency the body did not have, **and the collision masked it** — the body
linter sees the word and cannot see which object, so `W2 required term never appears in body` never
fired. The stale requirement is removed with the rename that revealed it.

**This is the collision's cost made concrete.** G2 priced it as incoherent prose; it was also a false
edge in the dependency graph, invisible to the instrument that exists to catch false edges.

### 4 · `denominations:` — the rule canon already practised in one place

Files as an **additive terms-registry field** in `spec/claim-format-2-addendum.md`, with the rule:
**canon is the naming authority; a projection denominates for its audience; the denomination is
recorded on the term rather than invented downstream.**

`term:verdict`'s inline parenthetical moves into the field. **That is also the cheapest available
repair of the `projection` collision** — the parenthetical is precisely where `projection` did
denomination duty inside a settled entry, while `term:projection` names an axis of the compound.

**No validator check is proposed**, and the addendum says why: a denomination is right or wrong by
ruling, not by rule. The instrument is the field plus review, as with `canonical_home`.

### 5 · i18n — two definitions in one entry

`ordliste-dansk.md`'s gloss of `grund` gave canon's *"what a decision is determined against"*
**and** the apparatus's *"the readable substrate the actor inspects"* — the very definition the audit
found **miscited to `core/00`**. The second is removed, applying the file's own stated rule that the
English source wins where the two disagree.

**The Danish text's other `grund` uses are untouched** and defer with the migration.

### 6 · `README.md` — the transfer's front door

Two self-contradictions repaired; **its ground senses untouched.**

| | |
|---|---|
| **The judgment row was unpatched.** `README.md:82` read *"an actor reading ground"* with **no accountable-party clause** — the gloss `CANON-PATCH-REGISTER.md` records as corrected in `01-the-principle.md:75`, and which `term:judgment` settles with *"a judgment allocation naming no accountable party is not an allocation. It is Escaped with an executor attached."* **Restored.** It is the same gloss that made `DDD-frame-15`'s judgment mode collide with `term:judgment` — the collision G2 found already retired, still live on the public page |
| **`required` where canon says `declared`.** The closure paraphrase read *"within the **required** resource, latency, confidence, and assurance bounds"*; `term:closure` says **declared**, and *declared* is load-bearing throughout the framework. **Corrected** |

**The README's nineteen `ground` occurrences carry five senses and not one of them moved.** That page
is the clearest single argument for the deferred migration, and it is left making it.

---

## Gates, both repositories

| | |
|---|---|
| upstream `validate-core-order.py` | **0 errors, 66 warnings** — *identical to the baseline before this gate*, verified by stash |
| upstream `validate-claims.py core/claims/` | **63 claims valid, 32 warnings** — the count `CLAUDE.md` documents for `v5.11.0` |
| upstream `validate-claims.py core/decisions/ --decisions` | **12 decisions valid** |
| downstream `validate-core-order.py` | **0 errors, 0 warnings**; 67 pins resolved, **0 content-drift**, 1 governed shadow |
| downstream `validate-claims.py core/claims/` | **26 claims valid, 6 warnings** — the documented downstream count |

**No pin advanced. No tag cut. No merge.**
