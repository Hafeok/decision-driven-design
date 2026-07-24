# Canon patch register — v4.3 → v4.4

> **Filing note.** Archived verbatim as the authoritative statement of what v4.4 owed, so the
> corrections stay auditable after merge. Its `core/NN` citations are stated against **v4.3**
> numbering, before the P3.1 renumbering it prescribes: read `core/08` as `core/09` (the measure)
> and `core/09` as `core/10` (the floor mechanism). The register is not rewritten to post-shift
> numbering, because it is the record of the shift.

**Scope.** Every correction the repo currently owes, from two sources: (a) internal inconsistencies
found while drafting Paper A, and (b) material authored in the paper that canon does not yet carry.

**Two patches were delivered separately and are not restated here.** They remain outstanding and are
part of this release:

- `core-04-pinning-attachment-patch.md` — pinning resolution defined by *where a constraint attaches*;
  new §1.1 closing the temperature-zero objection; last wind and pinning mode declared independent.
- `canon-patch-closure-condition.md` — *"decidable over digital ground"* → *"decidable over ground the
  actor can inspect"*, nine live substitutions, three explicit do-not-touch quotations of the retired
  postulate.

**Direction of dependency throughout:** authored in Paper A, owed to the repo. Paper A is drafted
against the patched forms. If a patch is rejected the corresponding paper passage reverts with it.

---

## P1 — Re-decomposition relocates demand; it does not destroy it

**Severity: highest. The repo currently contradicts itself, and the contradiction is load-bearing.**

`core/08` §4 states the correction explicitly:

> "A better decomposition destroys demand" → **"A better decomposition pre-pays more demand into the
> seam, buying cheaper parts. The total is invariant."** The destruction was always an artifact of not
> counting the seam.

Two meta files still carry the superseded concession, and both cite the same two examples.

### P1.1 — `meta/lineage-and-limits.md` §3.1

**Old (§3.1 heading and body):**

> ### 3.1 Architecture can *destroy* demand, not just relocate it
>
> - Idempotent / content-addressed designs (Nix-style builds) delete ordering and rebuild decisions.
> - CRDTs delete conflict-resolution and reconciliation decisions.

**New:**

> ### 3.1 Architecture relocates demand into the seam — the counterexample, resolved
>
> This was booked as the strongest counterexample to conservation, and `core/08` §4 resolves it. The
> examples are real; the destruction reading was an artifact of counting the parts and not the seam.
>
> - **Content-addressed designs** (Nix-style builds) do not delete ordering decisions. They make the
>   determination once, in deciding **what constitutes identity of a build input** — whether timestamps,
>   build paths, or compiler versions are inside the hash. That is where the difficulty of such systems
>   is known to concentrate.
> - **CRDTs** do not delete conflict-resolution decisions. They make the determination once, in the
>   choice between add-wins, remove-wins, and last-writer-wins semantics. That is where the difficulty
>   of CRDT design is known to concentrate.
> - **Declarative substrates** absorb application concerns into the substrate's own interface contract,
>   which is the seam under another name.
>
> In each case the determination moved into the **seam**: the interface contract the decomposition
> brings into existence. Count the seam and the total is invariant. The parts are cheaper because
> somebody pre-paid.
>
> **The resolution is no longer a choice between a weak and a strong position.** For any conditioning
> variable, `H(V) = I(V;X) + H(V|X)`; a decomposition is such a variable; the total is therefore
> invariant by the chain rule, not by concession (`core/08` §4). What genuinely changes the total is
> changing the task or the declared tolerance — not re-drawing boundaries within one.

**Retain the register conclusion.** The reason we do not claim physical-law status is unaffected: the
measure exists only on closing predicates, so the invariance is a theorem on that region and an
accounting identity off it. Nothing here promotes *principle* to *law*.

### P1.2 — `meta/consolidated-state.md` §1.4

**Old:**

> **Choosing the decomposition is itself the highest-leverage governing decision** — and a better
> decomposition genuinely *destroys* demand (CRDTs delete conflict-resolution decisions;
> content-addressed builds delete ordering decisions).

**New:**

> **Choosing the decomposition is itself the highest-leverage governing decision** — not because a
> better decomposition destroys demand, but because it **pre-pays demand into the seam**, where it is
> encoded once and inherited by every run rather than resolved per run. CRDTs and content-addressed
> builds are the standard examples and both are relocation, not destruction (`core/08` §4).

### P1.3 — sweep

Any other passage asserting destruction-by-re-decomposition. Grep `destroy` across `meta/` and
`applications/` before closing this patch.

---

## P2 — The immune floor is closure, not capacity

**`core/00` §6.1.** The section argues the floor from the antigen space exceeding the genome — the
determinations cannot be *pre-encoded*. That is an **encoding-capacity** argument, and on `core/03`'s
derivation capacity alone does not produce a floor.

The floor is demand that cannot move off the in-the-moment actor. Capacity overflow closes the
**encoded** store. It says nothing about the **mechanical** store, and where a check exists the demand
is verified out rather than stranded — adequacy stays cheap, and there is no floor. `core/09` already
keeps the two mechanisms apart deliberately (escape = overflow ∩ open). §6.1 fuses them.

**This is not a small imprecision.** The immune system is the licensing instance for the general name,
and Paper A cannot use it as a floor exhibit while the mechanism is misattributed.

**Old:**

> The antigen space is larger than the genome and shifts within a lifetime. The determinations
> *cannot* be pre-encoded — an irreducible floor, in the framework's exact sense: determination
> that cannot be moved off the in-the-moment actor no matter how much evolutionary training is
> applied. The genome is finite; the antigen space is not; **the gap is the floor.**

**New:**

> The antigen space is larger than the genome and shifts within a lifetime, so the determinations
> **cannot be pre-encoded.** State precisely what that does and does not establish.
>
> It closes the **encoded** store. Capacity overflow alone would not produce a floor: a determination
> that cannot be encoded can still be verified out, and where a check exists adequacy stays cheap
> (`core/03`).
>
> **The floor is there because the predicate does not close.** The organism cannot check, before or
> after, whether a response to a novel antigen was correct. There is no verdict function over the
> antigen space; autoimmunity is precisely the uncaught error, and it arrives as damage rather than as
> a verdict. Encoding is unavailable by capacity and verification is unavailable by openness, so the
> determination falls to the in-the-moment actor on every encounter. **That is the floor, in the
> framework's exact sense.**

**Consequence.** Add a one-line cross-reference in `core/09` noting that the immune case is the worked
instance of overflow ∩ open with both conjuncts satisfied for different reasons.

---

## P3 — Accountability chapter: placement and dangling dependencies

The chapter was drafted against a tree it could not read. Three corrections before merge.

**P3.1 — Numbering collision.** `core/05` is **Composition**. The chapter's own dependency argument is
correct — it extends the actor model and belongs immediately after `04-actors` — so:

| New | Was |
|---|---|
| `core/05-accountability.md` | *(new)* |
| `core/06-composition.md` | `core/05` |
| `core/07-determination-and-intelligence.md` | `core/06` |
| `core/08-projections.md` | `core/07` |
| `core/09-the-measure.md` | `core/08` |
| `core/10-the-floor-mechanism.md` | `core/09` |

**Sweep every cross-reference in the repo.** `core/NN` citations appear throughout `core/`, `meta/`,
`apparatus/`, and `applications/`. This is the recurring failure mode; do it mechanically, not by eye.

**P3.2 — Dangling references.** The chapter cites the **assurance tower** and **KC1 (finiteness)** as
results that depend on it. Neither exists anywhere in the repo at v4.3, nor does the term *Knowability
Claims*. Either they ship in v4.4 alongside, or §1's motivation and §7's base case are rebuilt on
foundations that exist. **Do not merge with dangling forward-references** — the honesty layer is the
asset being protected.

**P3.3 — The judgment-store amendment must land in `core/01`.** The chapter amends a definition
(*"per-run determination by a designated accountable actor"*) that `core/01` does not currently carry.
The live table row reads *during the act · an actor reading ground*. Patch the row and add the split
below the table:

**Old row:**

> | **Judgment** | — | during the act | an actor reading ground | does not amortise · walks out the door |

**New row:**

> | **Judgment** | — | during the act | an actor reading ground, **with an accountable party named** | does not amortise · walks out the door |

**New paragraph, after the `{rule, check, actor, nothing}` line:**

> **Two roles, not one.** The judgment store names an **executor** — the actor that determines this run
> — and an **accountable party** that bears the determination. For human actors these coincide, which
> is why the earlier statement could fuse them without visible error. For model actors they must be
> split: the model holds the judgment, a named accountability-bearing actor holds the consequence
> (`core/05` §6). **A judgment allocation naming no accountable party is not an allocation. It is
> Escaped with an executor attached.**

---

## P4 — Accountability chapter: two internal corrections

Authored in Paper A §4 and owed back.

**P4.1 — Derive the three conditions rather than list them.** As written, persistence, stake, and
sanctionability arrive as a list, which invites the charge that they were imported from responsibility
theory and given framework vocabulary. They follow from what the canon already says about escape.

**Insert before the three conditions in §2:**

> The conditions are not imported. They follow from the pricing structure of the escaped store.
>
> Escape is forbidden because it is **unpriced**. A price borne by nothing is not a price, so something
> must bear it: **stake**. The bill arrives after the act — that is the whole of escape's cost
> structure, free at the moment of decision and expensive later — so the bearer must still exist when
> it arrives: **persistence**. And the bill must be deliverable: **sanctionability**.
>
> All three fall out of the one state the principle forbids, which is why accountability is a structural
> concern of the framework rather than an ethical annexe to it.

**P4.2 — "Orthogonal" is the wrong word.** §2 claims orthogonality; §7 then argues the axes are linked
through revocability. Both cannot stand. What §2 needs is non-recoverability, which is weaker and true.

- **§2:** *"orthogonal to pinning resolution"* → **"independent of pinning resolution — not recoverable
  from it."**
- **§7:** promote the revocability link from caveat to result. The property that makes classification
  pinning loosest — that it *expires* — is the mechanism of revocation, revocation is the mechanism of
  sanction, and sanction is the substrate of accountability. **The property that makes an actor hardest
  to constrain is the property that makes it able to answer.** State it as a finding.

---

## P5 — CHANGELOG entry

Suggested, matching the existing format.

```
## 4.4 — Accountability, and the second actor axis

### Added
- core/05-accountability.md — accountability capacity as a second actor axis, independent of
  pinning resolution. Conditions (persistence, stake, sanctionability) derived from the pricing
  structure of the escaped store. Answerability and liability separated.

### Corrected
- Re-decomposition RELOCATES demand into the seam; it does not destroy it. meta/lineage §3.1 and
  meta/consolidated-state §1.4 retired to core/08 §4's position. The counterexample booked as
  strongest against conservation is resolved, not conceded.
- core/00 §6.1 — the immune floor is predicate-closure, not encoding-capacity. Capacity closes the
  encoded store only; the floor is there because the organism cannot check a novel response.
- core/01 — judgment store splits executor from accountable party.
- Closure condition generalised: "digital ground" -> "ground the actor can inspect". The floor is a
  property of the <actor, predicate> pair, which the substrate phrasing could not support.
- core/04 §1 — pinning resolution defined by where a constraint attaches. Closes the
  temperature-zero objection. Last wind and pinning mode are independent quantities.

### Renumbered
- core/05..09 shift to core/06..10 to seat accountability after the actor model.
```

---

## Ordering

P3.1 first — the renumbering touches every other patch's line references, and doing it last means
doing it twice. Then P3.2 (or the tower work lands), P1, P2, P4, the two delivered patches, P5.

## Not patched, still open

- Whether accountability capacity is **binary or graded**. The chapter leaves it open; Paper A does not
  depend on the answer.
- Whether the **assurance tower** exists. P3.2 blocks on this and it is the only item that can stall
  the release.
