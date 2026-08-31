# Manifest — Paper A's revision, carrying W1 (2026-08-30)

**Session type:** interactive paper revision, projection work. Five gates, held at every one.
**Principal:** Emil. **Branch:** `claude/paper-a-w1-revision-b8sx45`, both repositories.
**Base:** `actor-indexed-determination` `81f6929` (= `v5.12.0`, verified) · `decision-driven-design`
`54f00eb`.

**Nothing merged. No claim, term or decision was filed, amended or retired in either repository by
this session**, except the pin-advance decision this repository owes for its own pin. Q44, Q45 and
the ontology explainer were read and cited nowhere.

---

## 1. What the session produced

| Item | Result |
|---|---|
| **R-1** the related-work survey | seven works engaged, every locator verified against Crossref, Open Library or NCBI; three entries record a neighbour being stronger than the framework |
| **R-2** narrowed claim, retitle, rhetoric | *The Missing Parameter* → *Actor-Indexed Determination*; the claim narrowed in the review's own words; five warrant-overrunning formulations repaired |
| **R-3** pin advance and quotations | `v5.9.0` → `v5.12.0`, predicted before it ran and verified after; four quotations repaired, and a fifth repair no checker could see |
| **R-4** the supplement split | `paper-a-supplement.md`; the apparatus moved, not reduced, and still running |
| **R-5** W1 | 15 moved, 16 deferred, of 31 in the two manuscripts |
| **R-6** the review's small items | §7's arity mapped, §8.1's provenance made hypotheses, §8.5's escapes made candidates, §9.5's Study 0 added, and — flagged rather than assumed — the closure ladder repaired |

## 2. The close checks

| Gate | Result |
|---|---|
| `check-quotations.py` @ `v5.12.0` | **30 verbatim, 0 disclosed-partial, 0 failing** |
| `check-status.py` @ `v5.12.0` | **96 inline status assertions, 0 wrong** |
| `check-appendix.py` @ `v5.12.0` | **75 nodes rendered, 75 cited, 0 discrepancies** |
| `gen-appendix.py` idempotence | byte-identical across three runs, in split mode, manuscript unwritten |
| `validate-core-order.py core/` | **0 errors, 0 warnings**; 71 pins, 0 basis-loss, 0 content-drift, 1 standing shadow |
| `validate-claims.py core/claims/` | valid, 26 claims, **6 warnings** — the six `CLAUDE.md` records at `v5.11.0` |
| `validate-claims.py core/decisions/ --decisions` | valid, 22 decisions |
| reference closure | 22 entries; **0 cited-but-absent, 0 absent-but-cited** |
| internal cross-references | 58 headings, **0 `§` references matching no heading**; 0 references to material that moved to the supplement |

## 3. Word count, with the method stated and the growth attributed

**Method:** regex word tokens over the Markdown source, `[A-Za-z0-9][A-Za-z0-9'’\-–—/.]*`. It
reproduces the external review's own figures — *"approximately 11,600 words before Appendix A;
14,900 in total"* — to within 1%, which is why it is the method used rather than a better one.

| | Arrival (`40d277f`) | Close |
|---|---|---|
| Argumentative body | **11,708** | **17,334** |
| Supplement | — | **5,232** |
| Together | 15,250 | 22,566 |
| Body headings | 63 | 70 |

**The paper grew 48%, and the attribution is the defence.** The review asked for narrower claims, a
survey it did not have, and less machinery in the argumentative path. All three were done. The
machinery left — 5,232 words of it. What replaced it is qualification: a narrower claim needs the
hedging a broad one does not; a survey of seven works is longer than an assertion about them; three
of its entries record a neighbour being stronger, and each costs a paragraph; and a status
discussion that says what `established` does *not* mean is longer than one that says what it does.

**No argument was cut** (Emil, GATE 3). The failure mode this session was written to avoid is a
shorter paper that sounds more certain because it has less to qualify, and buying brevity out of
argument would have been that failure with extra steps.

## 4. The pin advance, predicted and verified

Committed at `7c9e2fa` **before** `graph/upstream.yaml` was touched, with the instrument that
computed it beside it. Advanced in two stages — ref first, hashes second — so the firing could be
observed rather than assumed.

| | Predicted | Observed |
|---|---|---|
| `E12` | 0 | **0** |
| `W5` | exactly 1 — `DDD-frame-15`, projected → retired | **1, that one** |
| `W6` | exactly 6, named by id, field and both hashes | **6, every id and every hash as written** |
| `W7` | 1, unchanged | **1** |

After re-instrumentation: 71 pins, 0 basis-loss, 0 content-drift, 1 shadow. Filed as `DDD-dec-34`.
The migration seed's own three-W6 prediction for this advance appeared exactly; none of its seven
W1 W6 fired, correctly, since W1 renames nothing upstream in this session.

## 5. Three findings that are not repairs

**5.1 A node forcing the largest repair in the revision fired nothing.** `DDD-measure-06` retires at
`v5.12.0` from `established`. `W5` sees only pinned ids and it was not pinned; both existing
checkers passed all three prose lines calling it `established`, because none is a block quotation
and none is an appendix row. Found by a sweep written at GATE 1, now shipped as
`papers/paper-a/check-status.py`. Four nodes pinned in consequence.

**5.2 Two checks fired against claims that would have helped us, and that is the pattern worth
keeping.** The first is the corroboration check. A search result
attributed a *"Law of Conservation of Complexity"* to Woods & Hollnagel's *Patterns*. Had it held it
would have given the framework's own conservation principle a named precedent inside the literature
the review says we ignore. **It could not be corroborated in any primary source and is used
nowhere.** A verification rule that only ever removes inconvenient claims is not a verification
rule; this is the case worth having on record.

The second fired on this session's own writing. A draft of `response-to-review.md` opened
*"nineteen conceded or repaired, three defended"* — a count reached by treating three propositions
the review **praised** as objections we had defended. It would have flattered us. Corrected during
drafting to twenty-one conceded and **one** defended, with §5 renamed *What we decline to give up*
and told plainly that those are not defences. **Twice in one session a check fired against something
that would have helped**, which is the only evidence that the checks are not decorative.

**5.3 The abstract carried a retired claim past three green checkers, and this is the argument for
the full read.** At GATE 5, with `check-quotations.py`, `check-status.py` and `check-appendix.py`
all reporting zero and every repository validator clean, the abstract still read *"discharged — by a
filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw"*. That
enumeration was retired at `v5.10` and §4.1 had already been repaired to carry its successor. **The
paper's most-read paragraph was projecting a claim the graph had killed**, and nothing caught it but
reading the paper from the top.

*Why no instrument saw it.* The abstract is not a block quotation, so the quotation checker does not
read it. It carries no citation, so the status checker has nothing to compare. It is not an appendix
row. **Three instruments, three surfaces, and the sentence most readers will actually read sits
outside all of them.**

**The general form, stated because it will recur:**

> **Instruments cover the surfaces someone thought to instrument.** The abstract is the surface
> nobody thinks to instrument, because it is *prose about the paper* rather than a citation *in* it
> — so it inherits no citation's protection while carrying more of the reader's warrant than any
> single citation does.

This is the **second** unwatched-surface finding of this session and it is the same shape as the
first. §5.1's was an unpinned node moving silently; this one is unciting prose asserting silently.
Both were found by a human-scale pass rather than by a checker, and both were found only because
someone went looking at a layer the instruments do not describe. A third checker was the answer to
the first. **A fourth is not obviously the answer to this one** — an instrument that parsed the
abstract for claims it does not cite would be guessing at meaning rather than checking
correspondence, which is a different kind of tool and a worse one. The honest remedy is the full
read, and its cost is now known.

**5.4 A count in the session's own charter did not reconcile.** The charter said 88% of W1 lives in
the two papers. Against the committed classification, **88 is the corpus-wide mutable total and the
two manuscripts hold 31 of it — 35%.** The migration seed is corrected, and W1's remaining surface
is **73 of 88, not zero.**

## 6. Rulings taken at the gates

| Gate | Ruling |
|---|---|
| 1 | `status-sweep.py` becomes a third checker · retitle candidate 1 · survey plan approved, the DOI error to go to the response · supplement boundary as stated · no argument cut · **all five ambiguous occurrences defer, including the three reading as S5** · stale line numbers to the migration seed's method rule |
| 2 | §11 ratified, including the three where-a-neighbour-is-stronger entries and the Bovens finding at its true size · reading grades in reference entries become standing practice · length accepted with attribution · the conservation-law near-miss to the manifest as a finding |
| 3 | ladder repair ratified rather than reverted · §7's arity: the paper flags **and** a canon session gets the issue · rhetoric pass not over-corrected · `README.md:32` to the freight list |
| 4 | the measure note's pin follows the note · the checkers point at the note **before** its pin next advances, because *an advance without instruments is unobservable, and an unobservable advance is presumed discharge at the pin layer* · §5.4's heading renames with the divergence clause |

## 7. Files

**`decision-driven-design`**

| Path | Change |
|---|---|
| `papers/paper-a/paper-a.md` | retitled; §4.1, §3.2, §3.3, §4.4, §5.1, §5.2, §6.1, §7, §8.1, §8.5, §9.5, §11, §12 revised; the appendix, the pin apparatus and the reproduction notes removed to the supplement |
| `papers/paper-a/paper-a-supplement.md` | **new** — the reproduced nodes, the pin, the filing statuses, the arity finding, the W1 record, Reproduction |
| `papers/paper-a/check-status.py` | **new** — the third checker |
| `papers/paper-a/gen-appendix.py`, `check-appendix.py` | a fourth argument: citations read from the manuscript, rendered into the supplement; new defect history in both |
| `papers/paper-a/response-to-review.md` | **new** — every objection mapped |
| `papers/paper-a/reviewer-brief.md` | retitled |
| `papers/measure-note/measure-note.md` | W1: 14 moves, 16 deferrals; §5.4's asset-divergence clause |
| `papers/measure-note/measure-paper-context.md` | Paper A's title, with the reason |
| `graph/upstream.yaml` | ref `v5.9.0` → `v5.12.0`; six pins re-instrumented; four added |
| `core/decisions/DDD-dec-34.yaml` | **new** — the pin advance |
| `meta/migration-plan-ground.md` | the third method mechanism; W1's counts corrected |
| `meta/successor-items-paper-a-revision.md` | **new** — six items |
| `meta/way-of-working.md` | Paper A's title |
| `meta/sessions/2026-08-30-paper-a-revision/` | prompt, bootstrap, four gate documents, three instruments, package README |

**`actor-indexed-determination`** — **untouched.** The principle repository carries no reference to
its dependents, and this session had no reason to write to it. Its branch exists and is empty of
changes, which is the correct state for a projection session.

## 8. What is owed after this

Six successor items at `meta/successor-items-paper-a-revision.md`: the accountability arity, W1's
remaining 73 occurrences, the `measure-nonuniform-ground.py` divergence, the measure note's missing
checkers, `README.md:32`'s over-claim on the freight list, and the unverifiable conservation-law
attribution. The response-to-review's §8 lists what the *paper* still owes, which is a different and
longer list, and the first item on it is the measure's decoder repair.
