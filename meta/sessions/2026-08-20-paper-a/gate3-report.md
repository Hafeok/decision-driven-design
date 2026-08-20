# GATE 3 report — the two authored sections

**draft-pending-ruling.** Step 3 of the walk, plus the four GATE 2 rulings applied. These two
sections are the paper's only original prose.

---

## 1. The GATE 2 rulings, applied first

| Ruling | State |
|---|---|
| Quotation checker ratified as a standing requirement | **Committed** as `papers/paper-a/check-quotations.py`; filed as freight item 1 in `successor-items.md` with the near-miss recorded in full; carried into the manifest at GATE 5 |
| Length: option (2), trim ~400 from the named sites | **Applied — −300 achieved, not 400.** Reported honestly in §4 below |
| §11.1 stays (option 3 rejected) | Untouched, 261 words |
| Orthogonality sentence → §5.1 | **Moved.** §5.1 now closes on it, announcing the second axis before §5.2 opens |
| §4.1's seam guard ratified | Unchanged |
| §9.1's H-set framing ratified | Unchanged |
| §8.4 / §5.2 terminology dependency | **Held.** §5.2 names the rung *constructively closed*; §8.4 already used that exact phrase, so no hunk was needed. Verified mechanically, not by eye |

---

## 2. §2.4 — Ground provenance · 479 words

**Shape.** The canon half first and cited; the five-way as a table with the sub-distinctions inside
their slots; one paragraph on why the sub-distinctions earn their place; one on missing ground; one
on institutional provenance and the mechanism the paper does not state; the closing flag.

**What it asserts as canon.** Exactly one thing — the ground definition, cited to `DDD-dec-26`.
Everything else is marked `(analysis)` at the head of the section and again in the closing flag.

**The sub-distinctions, placed as you ruled.** *Sensory* and *recorded* refine **observed**;
*derived* and *predicted* refine **inferred**. The section argues for them rather than asserting
them: the sensory/recorded boundary is what makes *a stored statement about uncontrolled ground is
not equivalent to a current observation of that ground* a usable sentence rather than a slogan,
because an arrangement cannot reason about revalidation cadence until it knows which of its observed
ground is sensed and which is recalled. The derived/predicted boundary earns its place by the same
test: a derived value fails when its inputs are wrong, a predicted one when the world moves, and the
two want different checks.

**Missing ground carries the paragraph you predicted it would.** It is stated as a slot rather than
an omission, and the reason is `DDD-hyp-02`'s first variable — dropping the slot would relocate a
*ground* property onto the actor, which is the collapse the index exists to prevent.

**The Q27 flag, at the point of use.** Institutional provenance is named, its mechanism is stated as
pending the trust filing, and the closing italic paragraph records that the framework ruled the
partition **ineligible for minting rather than merely deferred**, with dec-26's reason. It ends
*"This paper flags the gap and files nothing."*

**A deliberate omission worth your eye.** The section never names Q27 by its question number, and
never names the trust decision's content. It says only that the mechanism is pending a filing the
framework has open. A paper that named the unfiled question's expected answer would be anticipating
it, which is the failure mode dec-26's ruling exists to block.

---

## 3. §5.2 — How strong is the closure? · 642 words

**Shape.** The orthogonality is already handled in §5.1, so §5.2 opens directly on its question. A
four-row table gives each rung and the node it rests on; four paragraphs take the rungs in order;
then the retirement subsection; then the flag.

**The ladder, weakest first.** Open → verification-closed → constructively closed → formally
decidable, with each rung's basis named in the table's third column so a reader can check the
assembly rather than trust it.

**Decidability is last and is argued to be a special case, not a summit.** Canon reserves *decidable*
for the formal case rather than making it the requirement, and the section reads that reservation
in both directions: any bounded finite domain is decidable by lookup, and a decidable checker may
demand resources no arrangement has. The rungs that govern deployed arrangements are the middle two,
and the section says so.

### The retirement paragraph — the closest read in the section

The subsection quotes `DDD-frame-09` in full, states the premise the retirement turns on
(`DDD-frame-06`, `DDD-measure-11` — a search remains, and verification-closure bounds nothing about
its cost), and then draws the distinction the whole section stands on:

> Constructive closure does not contradict that finding. It **sidesteps** it — where the verdict is
> computed by rule, there is no search left to be expensive, so the premise the retirement turns on
> is **absent rather than denied**.

**One paragraph beyond the measure note's version, and it is the one to read hardest.** The note
states the sidestep; Paper A adds *why the difference between denying and sidestepping matters*,
because that is where a reviewer will push. Denying the retirement would license inferring cheap
generation from closure — precisely what was retired. Sidestepping licenses nothing beyond the case
at hand: a predicate whose verdict is computed has no generation cost to bound, and predicates whose
verdicts are merely checkable are untouched. The scoped survivor holds either way [`DDD-frame-05`].

**The Q32 flag, at the point of use.** The closing italic paragraph records that `term:closure` is
stated in evaluative terms alone, that no claim node names the stronger rung, and that the word
*constructive* occurs nowhere in the principle repository's core documents. The rung is stated
register-native, the node is named as pending on the open-questions wave, and the citation basis
until it lands is closure, the closure/generation-cost separation, and the measure's silence on
search. It ends *"This paper flags the gap and files nothing."*

**Attribution discipline.** The constructive rung is the measure note's refinement, and the table's
third column says `measure note §8` rather than naming a canon node — the one row in the table not
resting on the graph, visibly so.

---

## 4. Length, reported honestly — the ruling I owe you

**Method:** prose words, tables excluded (the measure note's method).

| Stage | Words |
|---|---|
| At GATE 2 | 10,212 |
| After the ruled trims | **9,912** (**−300**) |
| Plus §2.4 (479) and §5.2 (642) | **11,075** |

**The trim came to −300, not −400, and here is why.** The four named sites held ~895 words between
them at GATE 2. Taking 400 would have removed **45%** of them, and past about 300 the cuts stopped
removing padding and started removing argument. What went: §6.3 lost its Ashby/Tesler/Meyer
walk-through entirely (all three are treated in §11, so the loss is duplication, not content) and
kept only the Brooks relocation, which is the subsection's actual claim; §10.3 went from eight
boundary cases to **five** as ruled, with the two thinnest folded away and the remainder tightened;
§1 lost its roll-call sentence; §8.1–§8.3 lost their restatement of what the tables already carry.
**No citation and no closure was touched** — verified mechanically: the cited-node census is
identical before and after at 48 claims and 24 terms.

**So the body stands at 11,075 — about 75 over.** You pre-authorised this outcome: *"if the authored
sections push past ~11,000 anyway, say so and I'll take the ceiling explicitly rather than by
drift."* Saying so.

**One thing the arithmetic settles.** The authored sections came in at **1,121** against a 1,150
outline — *under* estimate. They did not cause the overage. §4 did, and §4's overage is the six
nodes you approved at GATE 1. The paper is 75 words over because of content you ruled in, and I have
not quietly clawed it back from elsewhere.

**Available if you want it inside the band.** About 85 words of genuine slack remain in the two
authored sections' softer joints — not in the rung definitions, the retirement argument, or either
flag. I have **not** taken it, because you asked to read these two closest and prose squeezed for
arithmetic is not what you should be reading. One word from you and it goes.

---

## 5. Verification at this gate

| Check | Result |
|---|---|
| `check-quotations.py` against `v5.8.0` | **29 verbatim, 0 failing, exit 0** |
| Negative control — the `DDD-floor-01` near-miss reintroduced | **fails**, exit 1 ✓ |
| Negative control — one reworded word in `DDD-frame-06` | **fails**, exit 1 ✓ |
| Cited claim/decision IDs resolving at `v5.8.0` | 48 / 48 |
| Cited term IDs resolving at `v5.8.0` | 24 / 24 |
| Status labels vs the graph | **0 mismatches** |
| Dangling `§N.M` cross-references | **none** |
| Pending-node flags in the manuscript | **exactly 2** — §2.4's and §5.2's, both at the point of use |
| New nodes cited by the authored sections | **none** — the census is unchanged at 48/24 |

**The last row is the one I would point at.** Both authored sections were written without reaching
for a single node the paper was not already leaning on. That is the signature register-native prose
should have: if authoring a section had required new citations, it would have been authoring claims.

**The checker found a bug in itself.** Its first version folded case at the first character only and
failed a legitimate mid-sentence quotation of `DDD-measure-02` beginning at `H(V)`. Corrected to try
the quotation as written and with either casing of its first letter — and only those, so an internal
rewording still fails, which control 2 confirms. Recorded in the freight item, because an instrument
ratified as a standing requirement should carry its own defect history.

## 6. Not done, and owed

- **GATE 4:** P-3's closure flags into the manifest, and P-4's apparatus — front matter (pin line
  drafted), References with every locator verified or flagged, **Appendix A generated from the
  graph** with the independent re-read, the H-set's `projected` status and empty evidence visible.
- **GATE 5:** assembly, the reviewer brief, full read, word count with method, validators, reference
  closure, Appendix regeneration + re-read, branch, PR, manifest.
- No claim, term, decision or release descriptor was filed in either repository. Nothing merged.
