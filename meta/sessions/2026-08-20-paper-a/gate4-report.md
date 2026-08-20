# GATE 4 report — the closures recorded, and the apparatus

**draft-pending-ruling.** Step 4 of the walk: P-3's closures confirmed and written up for the
manifest, and P-4's apparatus inherited wholesale from the measure note.

---

## 1. P-3's closures — all three in place, manifest-ready

Each is one hunk, each replaces something the foundation carried, and each states in the body that
it is doing so. Nothing further was owed at this gate; the record below is what the manifest will
carry at GATE 5.

| | Foundation carried | Canon governs, and the paper carries | Where |
|---|---|---|---|
| **C-1** | §4.1's four-source table: prior commitment / runtime actor / environmental-or-default / failure-or-non-resolution | `DDD-frame-15`'s four discharge modes, with the store/discharge seam guard in prose | §4.1, line 406 |
| **C-2** | §4.4's hedged allocation principle, avoiding conservation "until an independently motivated measure exists" | `term:conservation` with `DDD-measure-01` named as the modelling claim, `DDD-measure-02` as arithmetic, and the closing-region bound stated via `DDD-measure-06`; `DDD-frame-11` for what survives outside it | §4.4, line 512 |
| **C-3** | §8's H5 commentary: "closure does not make training available or unavailable as a hard gate" | `term:training` in its settled form; the softening named, declined in one sentence, routed to the supersession question as a successor item | §9.3, line 999 |

**C-1's reason is canon's own words, not the paper's judgment.** `DDD-frame-15`'s notes record that
the foundation's third source "mixed declared defaults with uncontrolled dynamics" and its fourth
"is not a discharge mode" — the paper quotes that rather than arguing the replacement itself.

**C-3 is a decline, not a rebuttal.** The paper does not argue that the softening is wrong. It
states that the question is a supersession against a settled term, that it is queued, and that it is
not this paper's to take. The gradient reading is manuscript-absent, as ruled.

---

## 2. The apparatus

### 2.1 Front matter — and a correction to the option-A pin

The option-A pin I drafted at GATE 2 carried an inherited clause Paper A does not earn. It read
*"a projection of `actor-indexed-determination` at `v5.8.0` and of `decision-driven-design` at
`v0.4.0`; bracketed claim and term identifiers resolve against those refs."*

**Tested rather than assumed: the paper cites no downstream node at all.** All 48 claim and decision
identifiers and all 24 term identifiers resolve upstream at `v5.8.0`; the intersection between the
cited set and the downstream repository's own claims and decisions is **empty**. The measure note
needs its downstream half because it cites downstream cost claims. Paper A does not, so the clause
asserted by implication that identifiers resolve against a ref against which none of them resolve.

The pin now names one ref for identifiers, says explicitly that no downstream ref is pinned, and
states the measure-note split in the note's own idiom — *absent from `v0.4.0` and from every earlier
downstream tag, so it resolves at that commit rather than at a tag.* Option A is unchanged as a
ruling; this is the ruling applied accurately.

No stale ref survives anywhere in the manuscript: the single remaining mention of `v0.4.0` is the
pin's own statement that the note is **absent** there.

### 2.2 Bibliography — ten entries, nine verified, one flagged

Every locator was checked rather than carried on the strength of a record.

| Entry | State |
|---|---|
| Johnson 1921, *Logic* Part I ch. XI | verified (Wave 3 record; carried in `DDD-frame-13`'s credits) |
| Prior 1949, *Mind* 58(229):1–20 and 58(230):178–194 | **re-verified directly** — both parts, pagination confirmed |
| Funkhouser 2014, OUP, ISBN 9780198713302 | verified (Wave 3 record) |
| Wilson, SEP | **re-verified directly** — first published 7 Feb 2017, substantive revision 18 Jan 2023, exactly as the record has it |
| Ashby 1956, with §7/7, §11/7, §11/9 | verified (measure note, external review) |
| Brooks 1987, *IEEE Computer* 20(4):10–19 | verified (measure note) |
| Shannon 1948, *BSTJ* 27(3) and 27(4) | verified (measure note) |
| **Meyer 1992**, Applying "Design by Contract", *IEEE Computer* 25(10):40–51 | **newly verified** |
| **Goodhart 1975**, in *Papers in Monetary Economics* Vol. I, Reserve Bank of Australia | **newly verified**, with the 1984 Macmillan reprint noted |
| **Tesler, ca. 1984** | **UNVERIFIED — flagged in the entry itself** |

**The Tesler entry, and why it is flagged rather than fixed.** There is no primary publication. The
law is attributed to Tesler from Xerox PARC and was communicated through talks and interviews; the
earliest substantial published discussion is an interview in Saffer (2006), *Designing for
Interaction*. The entry says all of this in the bibliography rather than in a footnote, and adds the
line that limits the exposure: **this paper cites Tesler for the allocation question only, and takes
no result from him.** Inventing a locator would have been the alternative and is the thing the
discipline exists to prevent.

The References section opens by stating the convention, so a reader meets it before the entries.

### 2.3 Appendix A — generated, then independently re-read

Two scripts, deliberately not sharing code, both committed beside the manuscript and both taking the
ref as an argument.

- **`gen-appendix.py`** reads the body for cited identifiers, pulls `statement` (claims, decisions)
  and `canonical_md` (terms) from the graph, and rewrites the whole appendix. Every row is verbatim
  by construction. It handles `term:closure` — the one registry entry not written as a blockquote —
  by stripping quote markers per line rather than assuming the block has them.
- **`check-appendix.py`** takes the *rendered markdown* as input, parses the tables back out, and
  compares each cell to the graph. It checks four different failures: a row that misquotes; a cited
  node with no row; a row for a node the body never cites; and a hypothesis-set row misreporting its
  evidence field.

**Result: 72 nodes rendered, 72 cited in the body, 0 discrepancies** — 45 claims, 3 decisions, 24
terms.

**The re-read earned its keep immediately.** On its first run it reported four discrepancies —
`DDD-floor-01`, `DDD-measure-02`, `DDD-measure-03`, `DDD-measure-10`. All four statements contain a
literal pipe (`H(V|X)`, `H(V|S)`), which the generator correctly escapes as `\|` in a table cell and
which the checker's parser was splitting on, breaking those cells in two. **The appendix was right
and the checker was wrong** — which is itself the argument for having a second script: a
discrepancy report is a claim about two artefacts, and finding the fault in the checker is a real
outcome, not a nuisance. The parser now splits on unescaped pipes only, and the hazard is commented
at the split.

**Six negative controls, all failing as they should:** a single reworded word in a rendered
statement; a cited row deleted; a status silently upgraded from `projected` to `established`; a
hypothesis-set evidence cell claiming evidence the graph does not hold; a term's canonical wording
reworded; and an invented row for a node the body never cites. Two earlier control attempts were
mis-aimed — one edited body prose the appendix checker correctly ignores, one matched no text at all
— and were re-run properly rather than counted as passes.

### 2.4 The H-set, with `projected` visible

The appendix carries a **separate generated table** for the hypothesis set, because burying the
discipline in a 45-row claims table would defeat it. Its columns are the graph's own fields:

| ID | Status | Evidence | Owner | Falsifier declared |
|---|---|---|---|---|
| `DDD-frame-07` … `DDD-hyp-05` (6 rows) | `projected` ×6 | `` `[]` (empty) `` ×6 | `paper-4` ×6 | yes ×6 |

`check-appendix.py` verifies the evidence column against the graph and **fails if a row in this
table has non-empty evidence** — so the predictions-never-findings discipline is machine-checked
rather than promised. §9.1 states the same thing in the body, before H1 appears.

### 2.5 Reproduction

A short section, in the measure note's idiom: **this paper mints no figures and no assets.** The
only numbers it states are the date-validation totals, produced by `core/assets/measure-toy.py`,
re-run fresh during drafting. The section also names all three checking scripts and notes that each
takes the ref as an argument, so the checks are reproducible against any ref rather than the one
that happened to be current.

---

## 3. Length — a correction that bears on your GATE 3 ruling

You raised the ceiling to accommodate **11,075**. Measured with the parts separated, that figure
included the front matter:

| Part | Words (tables excluded) |
|---|---|
| Front matter (title, subtitle, pin) | 121 |
| **Body — Abstract through §12** | **10,992** |
| Apparatus — Reproduction, References, Appendix A | 630 |

**The manuscript body is 10,992 — inside 11,000.** The 11,075 I reported at GATE 3 was the file's
prose total at that point, front matter included; the body proper was 10,992 then too, and the
pin correction since has added 38 words of front matter rather than argument.

So the ceiling raise may not be needed. Three readings are available and the choice is yours:

1. **The body is what the band governs** → 10,992, inside, no raise required. This is the reading I
   would take: a word target for a statement paper is about how much argument a reader must get
   through, and a pin line is not argument.
2. **Front matter counts** → 11,113, and the raise you granted covers it.
3. **Everything counts, apparatus included** → 11,745, which no reading of the band was ever meant
   to cover, since Appendix A is generated and References are locators.

Whichever you take, the GATE 5 count will state the method and give all three numbers, so the figure
is never a single number without its decomposition. The trim's own record is unchanged: −300, not
−400, stopped where cuts became argument.

---

## 4. Verification at this gate

| Check | Result |
|---|---|
| `check-quotations.py` at `v5.8.0` | **29 verbatim, 0 failing** |
| `check-appendix.py` at `v5.8.0` | **72 rendered / 72 cited, 0 discrepancies** |
| Appendix negative controls | **6 / 6 fail as they should** |
| Cited claim + decision IDs resolving at `v5.8.0` | 48 / 48 |
| Cited term IDs resolving at `v5.8.0` | 24 / 24 |
| Status labels vs the graph | **0 mismatches** |
| Downstream nodes cited | **none** — the pin's downstream half was removed as unearned |
| Stale ref references | **none** (the one `v0.4.0` mention asserts absence) |
| Bibliographic locators | 9 verified, **1 flagged unverified in its own entry** |
| Figures minted by this paper | **none** |
| Pending-node flags | 2, unchanged |

## 5. Not done, and owed at GATE 5

Assembly and full read; the reviewer brief (P-5); word count with method stated; all validators in
both repositories; reference closure; Appendix regeneration and re-read at the final commit; the
`meta/sessions/README.md` index row; branch, PR, manifest.

No claim, term, decision or release descriptor was filed in either repository. Nothing merged.
