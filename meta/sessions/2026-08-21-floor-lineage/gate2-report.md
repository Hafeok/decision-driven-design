# GATE 2 report — F-1 and F-2 landed

**Session** `2026-08-21-floor-lineage` · **draft-pending-ruling** · principal: Emil

Step 2 of the walk, per Emil's GATE 1 ruling. Two upstream commits on
`claude/floor-lineage-canon-repair-76sm10` in `actor-indexed-determination`. Nothing merged; the
downstream repository is untouched apart from this session record.

---

## F-1 — Option C, taken as ruled

**`core/graph/terms.yaml`.** `term:floor`'s `canonical_md` is now definition first, then the claim
sentence verbatim:

```yaml
    canonical_md: |
      The "floor" is the portion of a determination's demand that **cannot be moved off the in-the-moment
      actor** — the residue that no amount of encoding or checking can amortise, that must be paid, per
      run, in judgment.

      > **The intrinsic floor is a property of the acceptance predicate, not of the decision.**
```

**Promotion, not authoring, and checkable as such.** Both halves are lifted byte-for-byte from `03`'s
own prose at head — the definition from `03:30–32`, the claim from `03:20`. Nothing ratified is lost
and nothing is new. The sibling anomaly is the recorded warrant: `term:acceptance-predicate` and
`term:closure` both define, and `term:floor` alone asserted.

**`core/03-the-floor.md`.** The embed moves to the document's opening move, ahead of the novelty
framing, so the definition now precedes every use of it. The claim block keeps both limbs verbatim.

### The one authored sentence, flagged

Moving the claim sentence up left `## The claim` opening on a bare `>` continuation. It gains one
connective:

> The claim has two limbs.

That is **the only sentence this session wrote into `03`'s claim material**, and it is flagged rather
than buried. Two alternatives were available and rejected: leaving the claim sentence duplicated at
`## The claim` (the document would then state it three times in twenty lines, since the novelty
framing already restates it), or opening the section on the `**Zero**` limb with no lead (elliptical).
If Emil prefers either, the change is one hunk.

### Gates, upstream

| Gate | Baseline (head) | After F-1 and F-2 |
|---|---|---|
| `validate-core-order.py core/` | 0 errors, 66 warnings, **0 W4** | 0 errors, 66 warnings, **0 W4** |
| embeds | match the graph | match the graph |
| `validate-claims.py core/claims/` | 60 valid | 60 valid |
| `validate-claims.py core/decisions/ --decisions` | 8 valid | 8 valid |

Warning count is **identical** to baseline — the new section introduced no forward edge.

### The downstream consequences, verified now rather than asserted

Each of Emil's four F-1 conditions was exercised against the actual new upstream state (`0d21034`),
not predicted:

1. **W6 / the pin.** `graph/upstream.yaml:81` pins `term:floor` at
   `content_hash: sha256:daf43e07…`, which resolves against `v5.8.0` exactly. The change moves it, so
   W6 fires as designed. **The pin is deliberately not advanced in this commit** — see the ordering
   constraint below.
2. **Appendix A regeneration.** `gen-appendix.py` run against the new upstream state in a scratch
   copy. The diff is **exactly two lines**: `term:floor`'s row gains the definition, and the
   generated footer names the ref. No other row moves.
3. **The independent re-read.** `check-appendix.py` on the regenerated file: **72 nodes rendered, 72
   cited in the body, 0 discrepancies.**
4. **Both re-quotes.** `check-quotations.py`: **29 verbatim, 0 disclosed-partial, 0 failing**, both
   before and after. `reviewer-brief.md:57` is an inline italic rather than a block quote, so the
   checker does not cover it; read by hand, it remains a verbatim run.

**Downstream baseline, unchanged and green:** 67 pins resolved, 0 basis-loss, **0 content-drift**.

### The ordering constraint, and why nothing downstream is committed yet

`graph/upstream.yaml` pins a **tag, never a branch**, and the validator shallow-clones that ref.
Advancing the pin to `v5.9.0` before the tag exists would leave the downstream validator unable to
resolve any of its 67 pins. Per `CLAUDE.md`, merging the release descriptor to the default branch is
what cuts the tag. So the correct sequence is: upstream PR merges and `v5.9.0` is cut → downstream PR
advances the pin, regenerates Appendix A **against the tag**, and updates the manuscript's front
matter (`paper-a.md:7` declares the projection is at `v5.8.0`). Committing an appendix generated at a
branch sha would put a branch sha in a published manuscript, which is the thing the pin convention
exists to prevent.

The downstream decision node governing the advance is drafted at GATE 3 with the Paper A work, so
that one downstream PR carries F-1's consequences and F-4's citations together.

### One finding that needs a ruling, not a fix

Paper A `§6.1` quotes `term:floor` and cites it `[term:floor, settled]`. After this change that
quotation is **the second half of `canonical_md`, not the whole of it.**

`check-quotations.py` passes it, and the pass is genuine rather than a false one: the instrument's
own test is `contains(canon, quoted)` — *"Is `quoted` a verbatim run of `canon`?"* — so a contiguous
run verifies whether or not it is complete. Nothing is broken.

But the paper has its **own** disclosure convention for exactly this shape, and applies it elsewhere:
`[DDD-frame-15 — closing clause]`, `[DDD-floor-02 — opening clause; the claim continues, quoted in
full at §6]`. By that convention `§6.1`'s citation would become something like
`[term:floor, settled — closing clause]`. It is a citation tail, not argument, and this session
caused the condition that makes it wanted.

> **For ruling at GATE 3:** add the disclosure tail at `§6.1` (and the matching one at
> `reviewer-brief.md:57`), or leave both as they stand since the checker verifies them.

---

## F-2 — the ancestry, every locator verified or flagged in its own entry

New: **`meta/lineage-and-limits.md` §1.16, "The floor's own ancestry — irreducibility before this
framework"**, with a lead stating why it exists, four entries, a closing contrast, and one
deliberate non-filing.

Emil's three drafting rulings, applied:

- **Polanyi's placement corrected as found** — the dangling lineage was `core/03` citing Collins
  without him, not the register lacking him. §1.7 already carries both, and is left alone. Fixed at
  `03`.
- **Dreyfus and Suchman as one joint entry** (embodiment and situated action). They make one move,
  and the register carries the fuller treatment the paragraph cannot.
- **Both locators, never a pick**, on every source where two circulate.

### Verification outcomes, per entry

**Hayek — verified against the article itself, and the check earned its keep.** The AER original was
read as a scanned facsimile, text extracted directly. Its masthead reads *"VOLUME XXXV · SEPTEMBER,
1945 · NUMBER FOUR"*, and the quoted sentence stands in **§I, on p. 519** — the article's first page.

Two errors were caught that a citation database would not have surfaced, and both are now recorded
in the entry:

| | Web reproductions (e.g. Econlib) | The facsimile |
|---|---|---|
| comma after *"integrated form"* | **absent** | **present** |
| section | §III | **§I** |

The entry quotes the facsimile, and warns the next re-checker to expect the discrepancy. The draft
had also quoted the sentence from its midpoint without an ellipsis; it now carries the full sentence
from *"The peculiar character…"*.

**Bainbridge — verified, both forms.** *Automatica* **19(6):775–779**, 1983,
doi:10.1016/0005-1098(83)90046-8, first presented at the IFAC/IFIP/IFORS/IEA Conference on Analysis,
Design and Evaluation of Man–Machine Systems, Baden-Baden, **September 1982**.

**Dreyfus and Suchman — verified.** Harper & Row **1972**, revised MIT Press **1992**, ISBN
0-262-54067-3; Cambridge University Press **1987**, ISBN 978-0-521-33739-7, 203 pp. The 1972 edition
is given because subtitle variants circulate across printings and the two are routinely conflated.

**Wittgenstein — verified with its reservation stated in full, in its own body.** This is the entry
that could not be closed cleanly, and it is the Paper A Tesler pattern applied:

- §201 is a remark number and is stable across editions;
- the wording is the **Anscombe rendering** as reproduced in the *Stanford Encyclopedia of
  Philosophy*'s Wittgenstein entry §3.5, whose bibliography lists **both** Anscombe (Blackwell, 1953)
  **and** the revised fourth edition (Hacker & Schulte, eds. and trans., Wiley-Blackwell, 2009) and
  **does not attribute the quotation to either**;
- the same wording is what Kripke quotes at the opening of *Wittgenstein on Rules and Private
  Language* (1982);
- **not checked against a printed copy of either edition, and the fourth edition's revision of
  Anscombe's wording has not been compared.**

The entry says all of that in its body and names the debt for a session with the printed text. It is
not asserted as settled.

**Brooks — the adjacent discrepancy resolved, as ruled.** §1.3's heading is now *(1986; 1987)* and the
entry states both forms: *Proceedings of the IFIP 10th World Computer Congress*, North-Holland,
**1986**; reprinted *IEEE Computer* **20(4):10–19, April 1987**, doi:10.1109/MC.1987.1663532. The
register and Paper A no longer disagree.

### What §1.16 deliberately does not do

**No row is added to §6's required-citations table.** §6 is a standing duty on *every artifact that
uses the corresponding claim*; six new rows would obligate Paper A and every future projection at
once, which is a filing with consequences far outside this booking. The ancestry is recorded and the
citation duty is not extended. The non-filing is stated in §1.16 itself, so it reads as a decision
rather than an omission.

### `core/03` — the contrast paragraph

New section **"What is not new here"**, placed after the determinism subsection and before "What
survives, and why the retreat is a sharpening" — so the reading order is *the limits* → *the
tradition they sit in* → *what survives*. Four sentences, and `03`'s **first pointer at
`meta/lineage-and-limits.md`**, which it had never carried:

> An irreducible residue is not this framework's discovery, and the claim is stronger for saying so.
> Polanyi located that residue in the knower and Collins in the society; Wittgenstein located it in
> the fact that no rule contains its own application, Hayek in the dispersion of ground, Bainbridge
> in what automation leaves to the operator, and Dreyfus and Suchman in the actor's embodied
> situation. The register is `meta/lineage-and-limits.md` §1.7 and §1.16, which states for each what
> it contributes and where it differs. **None of them locates irreducibility in the checkability of
> the acceptance predicate, arrangement-indexed** — and that is the whole of the original move here:
> an ancestor's floor is a standing feature of knowers, societies or situations, while this one is a
> property of a relation, and it goes to zero wherever the predicate closes.

Drafted to strengthen by contrast. The last clause is the load-bearing one: the ancestors' floors do
not go to zero, and this one does, which is what makes it a result rather than an observation.

---

## Basis-impact check, run early

**No claim statement moved.** `DDD-floor-01` and `DDD-floor-02` are untouched in statement, region,
status and falsifier — verified by diff, not asserted. The full sweep runs at GATE 4.

## Held for GATE 2 ruling

1. **F-1's one authored sentence** — *"The claim has two limbs."* Accept, or take one of the two
   alternatives above.
2. **`§6.1`'s disclosure tail** — rule now or at GATE 3.
3. **§1.16's non-filing of §6 rows** — confirm the ancestry is recorded without extending the
   citation duty.
4. **The Wittgenstein entry** — confirm that "verified with the reservation stated in the entry" is
   the right disposition, rather than dropping the candidate.

**Nothing merged. The downstream repository carries only this session record.**
