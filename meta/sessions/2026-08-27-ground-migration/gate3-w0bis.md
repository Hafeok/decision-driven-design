# GATE 3, re-opened — W0-bis

**Status: draft-pending-ruling.** The classification is whole. Reproducible:
`python3 w0-classify.py` merges `rulings/r001…r021.py` (W0's 1,022) and `rulings-bis/b001…b009.py`
(W0-bis's 456) and asserts that neither set overlaps the other and that nothing is unruled.

---

## First: a correction to what I reported at GATE 3, in the direction that mattered

> **I told you the prose-context class was 29% correct, from a 21-row sample.
> Measured over all 427, it is 71.7% correct. My estimate over-stated the error rate by 2.5×.**

Two causes, both mine:

1. **The sample drew disproportionately from the small bad rules.** Of 21 prose rows it drew 1 each
   from `rule-standard-context` (15% correct) and `distribution-context` (56%), which are 13 and 9
   rows in a 427-row class — so two of the worst rules carried a tenth of the sample.
2. **I mis-ruled four rows in the sample itself.** I marked `ground-provenance` occurrences wrong
   when the audit had them right. Naming the provenance *axis* is S2; only a subject *characterised
   by* the enumeration spans senses and is U-multi. That rule is now fixed and stated at the head of
   `rulings-bis/b008.py`, and it was applied to the whole pass.

**Emil ruled option A on that number.** The ruling still holds on the corrected one — **146 sense
changes across 2,845 rows is material, and Gate 4 could not have been planned on top of them** — but
the number I gave was wrong and the ruling deserved the right one.

---

## What W0-bis measured

**427 prose-context rows, each read in its own file. Not sampled — counted.**

| Rows | Rule | Wrong | Correct |
|---|---|---|---|
| 191 | `accessible-available` | 17 | **91.1%** |
| 99 | `reading-ground` | 16 | **83.8%** |
| 41 | `delivered` | **38** | **7.3%** |
| 32 | `ordinary-english` | 20 | 37.5% |
| 31 | `ground-coverage-assurance` | 13 | 58.1% |
| 13 | `rule-standard-context` | 11 | 15.4% |
| 11 | `missing-ground` | 2 | 81.8% |
| 9 | `distribution-context` | 4 | 55.6% |
| **427** | **total** | **121** | **71.7%** |

**The class is not uniformly bad — two rules are.** `delivered` and `rule-standard-context` supply
49 of the 121 errors from 54 rows. The two largest rules, which carry 68% of the class, are 91% and
84% correct. **"Prose-context rules are unreliable" was the wrong generalisation; "these two rules
are broken" is the right one.**

**Why `delivered` fails at 7%.** Its pattern is `ground\b[^.]{0,50}\bdeliver\w*`, and the v5.5.0
release descriptor, the CHANGELOG entry and `core/13-delivery.md` all name **the `ground` area and
the `delivery` area in the same breath**. Thirteen `DDD-ground-0N` identifiers and the area name
itself became S3, the delivered sense. The rule is not reading prose; it is reading a table of
contents.

**Two sub-clusters came back clean**, which is why `accessible-available` survives at 91%:
`ground registry` / `ground table` / `ground item` — 69 rows, 3 wrong; and `ground provenance` /
`observed ground` / `inferred ground` — **60 rows, 0 wrong.**

---

## The anchored-class reopening — it happened, and it **closes**

Per the ruling: an anchored-class error reopens the question rather than being absorbed. One turned
up. It reopened, and it closes, because **the mechanism is decidable rather than a sampling matter.**

> **It is rule ORDERING, not window width.** `ddd-ground-id` is the **last** rule in the audit's
> ordered table, and first match wins.

| | |
|---|---|
| **15 rows** whose token **is** a `DDD-ground-0N` identifier were taken by an **earlier anchored rule** and given a sense — `declared-ground-axes` 11, `reads-different-ground` 2, `relevant-conditions` 1, `software-module` 1. An identifier inherits no sense |
| **13 rows** whose token is **not** the identifier were taken **by** `ddd-ground-id`, because an identifier sits elsewhere in the 240-character window. **The inverse steal** |

**Both sets were enumerated mechanically over the whole corpus, not sampled.** The family is
therefore closed by construction, not bounded by a confidence interval.

> **The true count of `DDD-ground-NN` identifier rows is 142, not the 116 the audit reported — and
> all 142 now classify U.** Verified mechanically: every row whose token sits inside the identifier.

**One further anchored error is not mechanically findable**, and it came from a second seeded sample:
`reads-different-ground` on *"edges … are never read as ground"*, where the sense is the ledger's
basis (S2) and not what an actor reads at an act.

**The second anchored sample, for the confidence you asked for.** 35 rows, seeded, drawn outside
W0-bis's scope and outside the first sample: **33 correct, 2 wrong** — and both errors are the two
mechanisms already named. Combined with the first sample: **72 of 74 anchored rows correct (97%)**,
with every identified failure belonging to an enumerable family. That is the honest bound, and it is
finite: it does not exclude a rare third mechanism, only the two now closed.

---

## The corrected classification

| | audit estimate | GATE 1 | **W0-bis** | net vs audit |
|---|---|---|---|---|
| **S2** | 1,638 | 1,536 | **1,529** | −109 (−7%) |
| **S1** | 488 | 520 | **567** | **+79 (+16%)** |
| **S3** | 331 | 417 | **369** | +38 (+11%) |
| **U** | 244 | 238 | **261** | +17 (+7%) |
| **S5** | 105 | 101 | **97** | −8 (−8%) |
| **S4** | 40 | 33 | **22** | **−18 (−45%)** |

**146 rows changed sense; 171 changed label.**

### Does a sense boundary move a second time? **Yes — S3, and it moves back.**

> **At GATE 1 I reported S3 up 26% on the audit, and called it corroboration of SR-2. S3 gives back
> 48 of those 86 occurrences. It lands at +11%, not +26%.**

The inflation came from the two broken rules: `delivered` labelled thirteen identifiers and the area
name S3, and `reading-ground` labelled sixteen S1 occurrences S3 — the second `ground` in sentences
like `term:actor`'s *"reading ground: variation in **declared ground**"*, where canon deliberately
opposes the two in one breath.

**The finding survives; its magnitude does not.** S3 is still materially larger than the audit
estimated, and every genuinely-added occurrence is still a verb applied to the S1 object — the
apparatus's *exports*, *bounds*, *consumes*, *sits on*. **SR-2 is unaffected either way**, since it
was ruled on canon's authority and not on a count. But the Gate 4 consequence I drew from the
26% — that `apparatus/` is where the delivered sense concentrates — needs restating at the corrected
size, and it does survive: `apparatus/` is still the largest single contributor of added S3.

### The boundary that moved most is **S1**, and nobody predicted it

**+79 over the audit, +47 over GATE 1.** S1 is now **567 (19.9%)**, and upstream canon is
**182 S1 against 154 S3** — reversing the ordering I reported at Gate 1, where S3 led.

**This strengthens SR-1 rather than disturbing it.** S1 keeps the word, and the sense that keeps the
word turns out to be canon's largest — which the audit's own ruling reached on authority, against
what the counts then showed. **The counts have now come to it.**

### S4 falls to 22, and **canon's S4 is exactly zero**

| | S1 | S2 | S3 | S4 | S5 | U | total |
|---|---|---|---|---|---|---|---|
| upstream | **182** | 81 | 154 | **0** | 42 | 64 | 523 |
| downstream | 362 | 267 | 196 | 20 | 54 | 137 | 1,036 |
| `product-cli` | 23 | **1,181** | 19 | 2 | 1 | 60 | 1,286 |

**GATE 3 Part 1 said the corpus contains no use of `ground` for a rule's normative force in canon.
The corrected classification says it mechanically: upstream S4 = 0.** The reconciliation and the
count were derived independently and agree.

### Independent corroboration: compound purity improved

Re-measured after W0-bis, the compounds are **cleaner**, which is what a correct correction looks
like: `reading ground` **96% → 100% S3** · `accessible ground` **85% → 100% S2** ·
`poisoned ground` 100% S3 · `ground-cli` 100% S2 · `ground distribution` 100% S5 ·
`institutional ground` 100% S4 · `uniform ground` 100% S5 · `ground registry` 100% S2.
`ground-state` remains the one impure compound (S2 7 · S1 4 · U 2).

---

## The method rule, for the manifest

> **A classification rule whose match window can cross a clause boundary is not an anchored rule, and
> the two classes cannot share an acceptance standard.**

**The mechanism, recorded precisely because the next instrument will make the same mistake in a
different regex:**

- The audit's context rules are written `ground\b[^.]{0,N}\bKEYWORD\b`. **`[^.]` is intended to stop
  at a sentence boundary and does not.** It fails on abbreviations, decimals, version numbers,
  file extensions, ellipses and `§`-refs, and it never stops at a comma, semicolon, dash or list
  item — so a 50-to-70-character window routinely spans two clauses and often two list entries.
  *"outcome variation across ground · epistemic uncertainty about a fixed **policy**"* is one list;
  the rule read it as one sentence.
- **An anchored rule matches at or beside the token** — `poisoned[ _-]ground`, `ground[ _-]registry`,
  `src/ground`. Its warrant is the compound, and the compound is present at the token or it is not.
  **A windowed rule's warrant is proximity, which is not a fact about the occurrence.**
- **Ordering is a third mechanism, independent of both.** In an ordered first-match-wins table, a
  rule that can match an identifier steals rows from the identifier rule unless the identifier rule
  is **first**. The audit's is last. That produced 15 steals and, symmetrically, 13 inverse steals.

**Three corollaries for any successor instrument:**

1. **Report per-rule precision, never a single figure for the table.** The audit reported its
   rule-assigned half as *"exact"* against the sampled half's confidence intervals. The distinction
   ran the wrong way: the sampled half was the better-measured one.
2. **Put identifier and immutability rules first**, because they are decidable and cannot be stolen
   from without loss.
3. **A rule with a window earns a sample of its own.** A 60-row sample across a mixed table told me
   29% when the truth was 72%, because rule size and rule quality are uncorrelated.

---

## What this gate asks

1. **The correction to my GATE 3 estimate** — 29% reported, 71.7% measured, and the two reasons.
2. **The completed classification** — 146 sense changes, residual zero by construction.
3. **S3 moving a second time, and back** — my GATE 1 finding was inflated; the finding survives at
   +11% rather than +26%, and SR-2 is untouched.
4. **S1 as the largest movement (+16%), and canon now S1-led** — unpredicted, and it strengthens SR-1.
5. **The anchored-class reopening, closed** — one mechanism, two directions, 28 rows enumerated
   mechanically; 97% on 74 sampled rows as the residual bound.
6. **The method rule for the manifest.**

**Gate 4 is now unblocked.** Nothing repaired. Nothing merged.
