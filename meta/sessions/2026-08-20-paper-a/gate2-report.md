# GATE 2 report — the ten projected sections

**draft-pending-ruling.** Step 2 of the walk. The manuscript is at
`papers/paper-a/paper-a.md`. Every Gate 1 ruling is applied; the two authored sections stand as
marked placeholders for Gate 3.

---

## 1. What is drafted

Twelve sections exist. **The ten projected ones are complete.** The two sections the readiness map
named as containing absences — §2 and §5 — have their projectable material drafted and their
authored subsections held:

| | Section | State |
|---|---|---|
| §1 | The parameter hidden by a fixed arrangement | complete |
| §2 | Actors, arrangements and ground | projectable material complete; **§2.4 held** |
| §3 | Commitment resolution | complete |
| §4 | Resolution and assurance | complete — carries two of the three closures |
| §5 | Closure and evaluability | projectable material complete; **§5.2 held** |
| §6 | Actor-indexed irreducibility | complete |
| §7 | Accountability completeness | complete |
| §8 | Worked example: code generation | complete |
| §9 | Predictions and study design | complete — carries the third closure |
| §10 | Limits and boundary cases | complete |
| §11 | Related work (incl. §11.1, Q36) | complete |
| §12 | Conclusion | complete |

§2 and §5 were drafted rather than deferred whole because Gate 3 is for **the two authored
sections**, not for two whole sections; their projectable rows in the bill of materials are Gate 2's
work. Both placeholders are one line, naming the gate they are owed at.

## 2. The three closures, landed

| Closure | Where | Form |
|---|---|---|
| **§4.1's mode mapping** | §4.1 | The foundation's four-source table is replaced by `DDD-frame-15`'s four modes. The replacement is stated explicitly in the body, with canon's own reason quoted: the foundation's third source "mixed declared defaults with uncontrolled dynamics", and its fourth was not a discharge mode at all. |
| **§4.4's hedge** | §4.4 | The hedge is gone. `term:conservation` is stated, the identification `DDD-measure-01` is named as **the modelling claim**, `DDD-measure-02` as **arithmetic**, and the closing-region bound is stated with `DDD-measure-06` rather than implied. `DDD-frame-11` carries what survives outside the bound. |
| **§8's training gradient** | §9.3 | `term:training` is quoted in its settled form. The foundation's softening is named as available, declined in one sentence, and routed to the supersession question as the framework's successor item — **manuscript-absent**, per the charter. |

Each is one hunk. All three are flagged for the manifest.

## 3. The two places you expected line-level rulings

**§4.1's seam guard** is a table plus three paragraphs under the heading *"The seam this section must
not cross"*. It sets the store partition (`{rule, check, actor, nothing}` — escape is *nothing*)
against the discharge partition (four modes — escape is *a supply mode*), states that both are
correct and neither reduces to the other, and closes on the sentence that does the work: **the world
never produces nothing.** The paragraph naming the failure mode — a reader importing one partition's
"nothing" into the other's four modes and concluding the framework contradicts itself — is the one
most worth your line-level read.

**The H-set** is §9, and §9.1 is written to be read before any hypothesis is. It states, before H1
appears, that all five are `projected`, all carry declared falsifiers, **all have empty evidence
fields**, and all are owned by an unrun study — and that the emptiness is discipline rather than
oversight. Each hypothesis then carries its own region qualification inline (H2's "does not claim a
situated arrangement can necessarily find a correct answer"; H3's "outside that region the
hypothesis predicts nothing"). §9.5 closes on *what would make this paper wrong*, stated as a
pattern the study can produce.

## 4. Verification at this gate

| Check | Result |
|---|---|
| Cited claim/decision IDs resolving at `v5.8.0` | **48 / 48** |
| Cited term IDs resolving at `v5.8.0` | **24 / 24** |
| Status labels asserted in the body vs the graph | **0 mismatches** |
| Block quotations verbatim against the graph | **26 / 26** after repair (see §5) |
| Disclosed partial quotations | 2, both marked in the citation itself |
| Dangling `§N.M` cross-references | **none** (54 headings, every reference resolves) |
| External `§` references (measure note, `core/09`) | 4, excluded from the internal check by construction |
| British spelling / house forms | clean — no Americanised forms found |
| Figures minted by this paper | **none** |
| Figures cited, re-verified against a fresh asset run | **5 / 5** |

**The figures.** `core/assets/measure-toy.py` was re-run fresh at head rather than trusted from the
manifest. It reproduces `25.493` total, `20.593` / `4.901` for the first decomposition and `11.020`
/ `14.474` for the second, exactly as §4.4 and §8.6 cite them. §8.6 states in the manuscript that no
figure in this paper was produced by this paper.

## 5. Finding: nine quotations were partial or divergent, and every one was repaired

Worth reporting because it is **Wave 3 successor item 2a arriving live** — the unchecked-assertion
hazard under a citation marker, where a quoted block asserts to a reader that the words are canon's
and nothing verifies it.

A first draft of the ten sections produced **nine** block quotations that were not verbatim:

- **three divergent** — `DDD-frame-13` abridged mid-statement; `DDD-delivery-02` with its
  parenthetical and its whole closing clause dropped; `DDD-floor-02` in §12 **paraphrased inside
  quotation formatting**, which is the worst of the three.
- **five silently truncated** — `DDD-frame-03`, `DDD-frame-14`, `DDD-cost-11`, `DDD-floor-01`,
  `DDD-floor-02` in §6, each quoting a genuine prefix and stopping without saying so.
- **one composed** — §12's compact form, which is the conjunction of `DDD-frame-15` and
  `DDD-frame-16`, formatted as though it were one node's words.

Each was caught by a script that extracts every block quote, reads its trailing citation, and
compares the quoted text against that node's `statement` or `canonical_md` at `v5.8.0`. **None would
have been caught by any existing validator**, exactly as successor item 2a predicts.

**How each was repaired.** Seven now quote in full. Two remain deliberately partial and **say so in
the citation itself** — §12's `[DDD-floor-02 — opening clause; the claim continues, quoted in full
at §6]` and `[DDD-frame-15 — closing clause]`, both with an explicit `…`. §12's compact form is now
canon's sentence as a quotation, followed by prose stating that the compact form is the
**conjunction** of two claims rather than either alone, per the rev18 booking.

**The truncation of `DDD-floor-01` was the one that mattered most.** The dropped tail was the
`DDD-dec-15` scope clause — *sufficient for escape and not necessary for it* — whose loss would have
restored the superseded universal quantifier inside a quotation attributed to canon. §6.2's prose
already carried the correction, so the paper would have contradicted itself between its quote and
its gloss. It now quotes the whole statement.

**Carried for the manifest:** a projection that quotes canon should verify its quotations
mechanically, and the check is cheap. The script is small and general.

## 6. Length, reported honestly

Method: **prose words, tables excluded** — the measure note's method, so the two are comparable.

| § | Words | Est. | Δ |
|---|---|---|---|
| front matter | 84 | — | — |
| Abstract | 264 | 250 | +14 |
| Note on claim status | 157 | — | (unbudgeted; see below) |
| 1 | 548 | 850 | −302 |
| 2 | 902 | 1,050 | −148 |
| 3 | 702 | 650 | +52 |
| 4 | **1,876** | 1,400 | **+476** |
| 5 | 856 | 1,300 | −444 |
| 6 | 760 | 800 | −40 |
| 7 | 461 | 600 | −139 |
| 8 | 775 | 900 | −125 |
| 9 | 929 | 900 | +29 |
| 10 | 628 | 700 | −72 |
| 11 | 730 | 1,050 | −320 |
| 12 | 540 | 450 | +90 |
| **Total** | **10,212** | 10,900 | −688 |

§5's and §2's deficits are the two authored subsections, not yet written. **Projected body at Gate 3
close: ≈ 11,362** — about **360 over the 11,000 ceiling**, before References and Appendix A.

### Where the overage is, and what bought it

**§4 is +476, and every word of it is a Gate 1 ruling.** The budget was written before you approved
the six extra nodes. §4 absorbed four of them — `DDD-delivery-01/02/03` (the *Filing is not
delivering* subsection, ~180 words), `DDD-cost-25` (§4.2's latency material), and `term:store` (the
seam-guard table, which cannot be stated in prose with one partition). The *two registers*
subsection under §4.3 is `DDD-frame-14`'s amendment, also unbudgeted. So the overage is booked
content, not sprawl — but it is real, and it lands the body over the band.

**The unbudgeted 157-word status note** is the §1 material the skeleton described as "the
claim-status convention stated once, here". It grew into its own heading because §9 and Appendix A
both lean on it.

### Three ways to land inside the band, for your ruling

1. **Do nothing.** Report ≈11,360 at Gate 5 with the method and this table. The measure note's rule
   governs — *as long as its booked content, reported honestly* — and by that rule the paper is the
   right length. The 8,000–11,000 target then reads as an estimate the content overran, which is
   what it was.
2. **Trim ~400 from the softest prose** *(recommended if the band is a real ceiling)*. The
   candidates, in order of least loss: §6.3's classical-accounts paragraph (~150, register-native
   and partly restated in §11); §10.3's boundary-case list (~120, seven cases where five would
   carry the argument); §8.2/§8.3's example commentary (~100, the tables do most of the work);
   §1's second paragraph (~60, overlaps §1.1). None touches a citation or a closure.
3. **Cut §11.1 (Q36, 260 words).** Lands the paper at ≈11,100 in one hunk. **Not recommended** — you
   ruled it in at Gate 1 for a stated reason, and it is the only place the framework's motivating
   force is named.

I have not trimmed anything. The overage is a length judgment and it is yours.

## 7. Two things I flagged rather than resolved

**§8.4 forward-references §5.2**, the authored ladder, for the phrase *constructively closed*. That
is a real dependency: if Gate 3's ladder changes the term or drops the rung, §8.4 changes with it.
Noted so the two are read together at Gate 3.

**§5.1 is marked `(analysis)` and says so twice** — once in the heading paragraph and once inside
it, stating that the framework files operational closure as its closure, prices economic closure in
the cost register, and does not name normative closure at all. Your Gate 1 ruling asked for the
orthogonality sentence; it opens §5.2's placeholder position and will be written into §5.2 proper at
Gate 3, where the ladder is there to be orthogonal *to*. If you would rather it sit in §5.1 so the
kinds framing carries it, that is a one-sentence move.

## 8. Not done, and owed

- §2.4 and §5.2 — Gate 3.
- Front-matter pin line is **drafted** and carries the ruled option A sentence; References, Appendix
  A and the reviewer brief are Gate 4 and Gate 5.
- No claim, term, decision or release descriptor was filed in either repository. Nothing merged.
