# Paper A successor items

Booked as the session runs, none begun, per the do-not-bundle rule. Item 1 is a **freight item for
the next canon session**, filed at Emil's GATE 2 ruling.

---

## 1. Quotation fidelity as a standing requirement *(freight — next canon session)*

**The rule, as ruled.** Every block quotation attributed to a graph node must **verify verbatim
against the graph**, or **declare itself partial in its own citation**. Same class as Appendix A's
generated-not-edited convention: the fix is mechanical verification, because papers are where
canon's text gets silently rewritten if nobody checks.

**Why it is a rule and not a habit — the instance that justifies it.** Paper A's first drafting pass
produced **nine** block quotations that were not verbatim. Three were divergent, five were silently
truncated, one composed two claims and formatted them as one. **No existing instrument could have
caught any of them**: `E13` enforces byte-match for `ddd:embed` only, `W5`/`W6` resolve inside the
pinned ref's contents, and a prose citation carries no marker at all. This is Wave 3 successor item
2a — unchecked assertion under a citation — arriving in a paper rather than a track.

**The specific near-miss, recorded because it is the rule's justification.**

- **What was dropped.** `DDD-floor-01` was quoted as far as *"…AND the shed decisions carry no
  verifier"* and stopped there. The dropped tail is the `DDD-dec-15` scope clause: *"— overflow ∩
  open is the mechanism of capacity-generated escape, **sufficient for escape and not necessary for
  it**, with overflow alone producing retries, not escape."*
- **What the truncation would have asserted.** Exactly the universal quantifier `DDD-dec-15`
  superseded. A reader would have taken canon to say that capacity overflow on an open predicate is
  *the* mechanism of escape, rather than *one generator* of it — which is the error the scope
  correction was filed to remove.
- **That the paper's own gloss would have contradicted it.** §6.2's prose already carried the
  correction, in its own voice, two paragraphs below the quotation: *"This mechanism is sufficient
  for escape and never necessary for it."* The paper would therefore have quoted canon as saying one
  thing and immediately glossed it as saying the opposite — a contradiction internal to a single
  subsection, introduced entirely by an undisclosed truncation.

**The instrument.** `papers/paper-a/check-quotations.py`, committed with this session and run at
every gate from GATE 3 onward. It extracts each `> ` run, reads its trailing citation, and compares
against `statement` (claims, decisions) or `canonical_md` (terms) at a pinned ref. It accepts a
quotation that begins mid-sentence with an author's capital, and it accepts a disclosed partial —
a citation carrying *"closing clause"*, *"opening clause; the claim continues"* or similar, with an
explicit `…`. Everything else fails. Verified against two negative controls: the near-miss above,
and a single reworded word in an otherwise-correct quotation. Both fail the check.

**Verbatim is not complete — a second predicate over the same input** *(added by the floor-lineage
session, 2026-08-21, at Emil's GATE 2 ruling).* The checker's test is `contains(canon, quoted)` —
*"Is `quoted` a verbatim run of `canon`?"* — so it verifies **faithfulness, not disclosure**, and a
contiguous partial passes untagged. The instance: upstream item F-1 lengthened `term:floor`'s
`canonical_md`, which turned Paper A `§6.1`'s quotation into a partial overnight, with the checker
still reporting it verbatim and correctly so. A partial-quote disclosure rule is a **separate
predicate over the same input**, and whoever implements this item should carry both rather than
assume the first covers the second.

**Open, and deliberately not decided here.** Whether this belongs in `validate-core-order.py`, in
CI, in a projection-side linter, or stays a per-paper script is a design question — the same
question Wave 3's item 2 left open for ref-staleness, and for the same reason: it reads an input
(the manuscript) that no current validator reads. Shape, severity and home are all open. What is
settled is the requirement, not its implementation.

*A found bug, recorded because it bears on trusting the instrument.* The checker's first version
folded case at the first character only, and failed a legitimate quotation of `DDD-measure-02` that
begins mid-sentence at `H(V)`. Corrected to try the quotation as written and with either casing of
its first letter, and only those — an internal rewording still fails, as control 2 confirms. The
defect is recorded in the script's own docstring, not only here.

---

## 1a. Appendix generation, re-read independently *(freight — rides with item 1)*

**The rule.** An appendix reproducing graph text is **generated, never hand-edited**, and then
**re-read against the graph by a second script that shares no code with the generator** and takes
the *rendered* artefact as its input. Generated-not-edited was already the standing convention from
the discharge session; what this session adds is that the re-read must be **independent**, and why.

**Why independence, and not merely a re-read.** `check-appendix.py`'s first run reported four
discrepancies — `DDD-floor-01`, `DDD-measure-02`, `DDD-measure-03`, `DDD-measure-10`. **All four
were the checker's fault, not the appendix's.** Each of those statements carries a literal pipe —
`H(V|X)`, `H(V|S)` — which the generator correctly escapes as `\|` inside a table cell, and which
the checker's parser was splitting on, breaking the cell in two. The appendix was correct
throughout.

That is the argument, and it is stronger than the usual one. A checker that can be wrong about a
**correct** artefact is a checker that could have been wrong about an **incorrect** one, and only
independence surfaces which of the two artefacts is at fault. Had generator and checker shared a
parser, the four discrepancies would never have appeared — and neither would a real one of the same
shape. The defect is recorded in the script's own docstring.

**Machine-checked predictions-never-findings.** The same script fails if any row in a hypothesis-set
table shows evidence the graph does not hold. Ruled at GATE 4 as an upgrade from discipline to
instrument, and generalised here: **any projection carrying hypothesis nodes fails if a rendered row
reports evidence the graph does not carry.** The H-set has been carried as
predictions-never-findings by convention since Wave 3's GATE 4; this makes the convention
executable.

**A second defect, found at the close, and the rule it adds.** The generator was **not
idempotent**: it appended a horizontal rule to a body that already ended with the rule preceding the
appendix, so a second run added a second one. A convention that says *regenerate wholesale* is a
convention that will be run more than once, and an instrument serving it must survive that. Fixed,
and idempotence is now demonstrated by running the generator three times and comparing bytes. **The
rule this adds: a generated section's generator must be idempotent, and the check is running it
twice, not reading it.** Recorded in the script's own docstring.

**Open, as with item 1.** Whether generator and checker belong in a shared projection toolkit, in
CI, or per-paper is undecided. What is settled is the requirement: generated, re-read, re-read
*independently*, and idempotent.

---

## 2. The constructive-closure node (Q32) — carried, not created

Paper A's §5.2 states the constructive-closure rung register-native and flags the pending filing at
the point of use, as the measure note's §8 already does. **This session adds no new claim on the
item**; it is recorded here only so the Q-wave sees a second projection now depending on it. Canon
still carries no constructive/verification split, and the word *constructive* still occurs nowhere
in `core/`.

## 3. The institutional-provenance mechanism (Q27) — carried, not created

Paper A's §2.4 names institutional provenance and states its mechanism as **pending the trust
filing**, per `DDD-dec-26`'s ruling that the five-way partition is ineligible for minting rather
than merely deferred. A Q27 landing that restructures the partition forces a §2.4 revision, exactly
as it forces a revision of the determination track. Recorded so the dependency is visible from the
Q-wave's side.

## 4. `DDD-dec-26`'s `[PROPOSED]` banners inside a cut tag *(freight — next canon session)*

*Second instance, 2026-08-21:* `DDD-dec-29` (the floor-lineage pin advance) carries the same banner
for the same reason — it is filed before the merge it records. It inherits this item rather than
resolving it.

Reported at GATE 1, ruled reported-not-repaired: a paper session does not reach into canon to tidy
banners. `DDD-dec-26`'s `resolution` and `notes` both open with `[PROPOSED … nothing is ratified]`
while the same file's body records the GATE 1 and GATE 3 rulings as made, and `DDD-frame-02`'s notes
say the same. The file merged and was tagged at `v5.8.0` with the banners unstruck, so a reader of
canon at the tag cannot tell from the file's own words whether it is ratified. `DDD-frame-02`'s
notes additionally carry a duplicated word at a hunk boundary — *"One / One consequence was raised
for ruling"*. Both are one-line repairs for a session that is already touching those files.

## 5. `paper-a-draft.md` — closed, not outstanding

Recorded so no later session re-opens it. The file the revision foundation names as its predecessor
**has never existed in either repository**, checked against full unshallowed history. The foundation
replaces it, the readiness map already discharged its §14 editing instructions against canon, and
its prose was re-authored rather than preserved. Emil confirmed the reading at GATE 1. **Closed.**

## 6. The measure note has no downstream tag

Paper A cites the note by path plus commit `aa7e135`, per the GATE 1 option-A ruling, because the
note is absent from `v0.1.0` through `v0.4.0`. This is not a defect in the paper and it is a
standing awkwardness for any future projection citing the note. Whether a downstream tag should be
cut that carries it is Emil's, unbundled — the same shape as the measure session's own
sixth-asset pin item, arriving from the other side.
