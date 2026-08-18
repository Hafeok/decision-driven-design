# GATE 1 — fetch, verify, propose

**draft-pending-ruling.** Nothing in this report is filed, and no manuscript line has been
changed. Everything below is a proposal awaiting Emil's ruling.

Session: the measure note's discharge section (M-1…M-5). Base commits as recorded in
`bootstrap.md` — `actor-indexed-determination` at `4d0d177` (= tag `v5.7.0`),
`decision-driven-design` at `8e348ce` (head).

---

## 0. Verification record

**Both repositories fetched at head.** Upstream head is exactly `v5.7.0`: the annotated tag
`v5.7.0` resolves to commit `4d0d177`, which is `origin/main`. Downstream head is `8e348ce`
(Wave 3 merge, PR #23).

**All five assets re-run upstream, all reproduce, no drift.**

| Asset | Figures checked | Result |
|---|---|---|
| `measure-toy.py` | `H(V)·n = 25.493`; A parts 20.593 / seam 4.901; B parts 11.020 / seam 14.474 | reproduces exactly |
| `measure-actor-allocation.py` | three sums = 25.493; 25.493/0.000, 14.474/11.020, 20.964/4.529 | reproduces exactly |
| `measure-rag.py` | all six rows, `H(A)` ≈ 2.609–2.616, sums as tabled | reproduces exactly |
| `measure-chained-seams.py` | 4.901 + 17.838 + 2.755 and 14.474 + 8.265 + 2.755; joint seam 22.739 | reproduces exactly |
| `measure-nonuniform-ground.py` | benign 4.357, uniform 25.493, adversarial 96.639, all six part/seam pairs | reproduces exactly |

Every figure printed in §4, §5.1, §5.2, §5.3 and §5.4 of the manuscript matches its asset's
fresh output character for character. No demotion is triggered.

**Reference closure over the manuscript's citations, at `v5.7.0`.** 20 distinct claim IDs and
15 term IDs are cited. All resolve: 18 claims upstream, 2 (`DDD-cost-06`, `DDD-cost-07`)
downstream, which is correct — they are the volume layer and the note says so. All 15 terms
resolve in `core/graph/terms.yaml`. **Zero dangling citations.**

**Validators green at both heads.** Upstream: `validate-core-order.py` — 0 errors, **0 W4**
(59 W1, 7 W2, all pre-existing); `validate-claims.py` — 60 claims valid. Downstream:
0 errors, 0 warnings; 25 claims valid.

---

## 1. M-1 — proposed placement and outline

### Placement

**A new top-level section between §5 and §6**, i.e. the aggregation content becomes **§6** and
§6…§10 shift to §7…§11. That is the prompt's natural home and I think it is right: the content
is worked, so it belongs with the worked material and not after the epistemics; and §6's honesty
table has to cover it, which it cannot do if the content follows it.

**The cost, priced honestly: 19 cross-references need renumbering** — `§6`×10, `§7`×5, `§8`×2,
`§9`×2. All are greppable and mechanical, and the diff will be reviewable line by line. I do not
think this is a reason to prefer the alternative.

**The alternative I considered and reject.** Putting the content at §5.6 avoids all renumbering,
but §5 is titled *One theorem, three conditioning variables* and closes at §5.5 with *What is
unified*. The aggregate is not a fourth conditioning variable — it is a statement about repeated
acts — so §5.6 would both fight the section title and sit after the section's closer. The
renumbering is the cheaper cost.

**Proposed title:** *§6. Discharge over many acts*. Register-native; names the object without
promoting anything.

### Outline

**§6.0 — opening.** The identity so far is per-act, and §2's Scale paragraph already said so.
This section asks the next question and only the next question: what happens over `N` acts.
Two sentences, no promises.

**§6.1 — Per-act discharge as the primitive** [`DDD-frame-16`]. Standing supply inherited per
act; occasioned supply produced per act; no act-free discharge. The paper's per-act constitutive
Scale paragraph in §2 is the same fact in measure vocabulary — **cited, not restated**, per the
prompt. One paragraph. Also cites `term:act` and `term:act-individuation` (see §5 below: the
latter is new since the pin and is directly load-bearing here).

**§6.2 — Aggregate discharge over `N` acts.** `N·H(V)` is the demand of `N` **independent**
draws. This paragraph opens by citing §2's Scale paragraph explicitly and adopting its reading
verbatim — *the expected information in `N` independent draws* — and states that what follows
gives that reading content by asking what happens when the draws are **not** independent. It is
written so that a reader who remembers the `nH(V)` correction sees the correction being *used*,
not revisited.

**§6.3 — The correlation inequality.** `H(V₁…V_N) ≤ N·H(V)`, with equality iff the draws are
independent. **Shannon's, first and plainly** — it is subadditivity of joint entropy, and the
sentence naming it as Shannon's comes before the sentence saying what it is for. Then the
reading: correlated verdicts mean aggregate demand is strictly less than the per-act sum, and
the gap `N·H(V) − H(V₁…V_N)` is exactly what one resolution amortised across correlated acts
can capture. Worked figures here — see §2 below.

**§6.4 — The O(1)/O(N) asymmetry** [`DDD-frame-16`; the §2.1 cost-split citations]. Authoring is
paid once; discharge is inherited per act. Under the batch model of §6.3 this is *numerical*
rather than rhetorical: the shared latent is paid once, `O(1)`, and the residual is paid `N`
times, `O(N)` — and the per-act aggregate falls to the conditional entropy as `N` grows. This is
where `paid once, inherited by every run` gets its arithmetic, wired to the standing/occasioned
registers. **Guard:** stays in the demand register. Where it touches pricing it points at
§2.1 and at `DDD-cost-06/07`'s volume layer and stops; it does not re-derive a crossover.

**§6.5 — Distribution-weighted discharge** (Q-C's exposition). One paragraph, **no claim, no
node**, marked as exposition — the measure's `P` doing its work: demand comes due where acts
concentrate, at the rate `P` supplies them. Canon carries this in exactly the same posture
(`core/13` §4, *"an exposition note, deliberately not a claim"*), and the paragraph will say so.

**§6.6 — What this section does not claim.** The honesty paragraph, written to §6's (→§7's)
register and cross-referenced from it. Three sentences of content:
1. The inequality is Shannon's — chain rule and subadditivity. Nothing here strengthens or
   tests it.
2. The identification of *correlated verdicts* with *cacheable work* is the modelling claim,
   and it is a **second** identification, layered on §2's and not implied by it.
3. The correspondence — do measured verdict correlations predict realised amortisation? — is
   **untested**, on the same footing as `DDD-measure-07`'s correspondence and with the same
   falsifier shape: if realised cache hit-rates are reliably uncorrelated with the measured
   gap, the second identification is wrong and Shannon is untouched.

**Section closes on the concession**, per the standing note — the last sentence is what is
conceded, not what is taken.

### The claim-availability position, stated plainly

`DDD-frame-16`'s own `region` field routes this content **out** of the claim and to the paper:

> *"The aggregate formal content — N·H(V) accounting over repeated acts, the correlation
> inequality, the standing/occasioned bit asymmetry — is measure-register material and lies
> outside this claim, routed to the projection that carries it."*

So the section is licensed by canon to carry the aggregate arithmetic, and the arithmetic itself
needs no node — it is Shannon's, and the note cites Shannon for it exactly as §3 cites Shannon
for the chain rule. **What canon does not carry is the second identification** (correlated
verdicts ↔ cacheable work). Per the session rule, §6.6 states it as register-native modelling
content with its falsifier, and the gap is flagged for a canon session. **Nothing is filed.**
This is flagged as item R-2 below because it is the one place the section says something canon
does not.

---

## 2. The new-asset question — answered: **licensed, and I recommend taking the licence**

**Do the existing assets carry it?** No. None of the five computes a joint entropy over repeated
acts; the aggregate `H(V₁…V_N)` is not a quantity any of them forms. If §6.3 and §6.4 state
worked figures, they need a new script.

**Should the section state worked figures?** I recommend yes, for three reasons. The paper's
method throughout is *exact arithmetic on a concrete task*, and a §6 that argued the inequality
abstractly would be the only section that did not. The gap `N·H(V) − H(V₁…V_N)` is the section's
whole point, and its size is the interesting fact. And the Reproduction section is a standing
promise that every stated figure re-runs — meeting it costs one script.

### Proposed asset: `core/assets/measure-aggregate-discharge.py`

On **the same date task** — no new task is introduced, and the numbers connect to §4's already-
ratified figures.

**The correlation model, stated so it is a model and not a fudge.** A batch of `N` acts shares a
**month**, drawn once; days are drawn uniformly within it. The verdicts are then conditionally
independent given `M`, so the joint entropy is exact and cheap: the probability of a verdict
sequence depends only on its count of `VALID`s, and `H(V₁…V_N)` sums in closed form over
`k = 0…N`. Canon licenses the framing directly — `term:act-individuation`: *"batch boundaries
are verdict boundaries."*

**The figures the section wants**, all from this script:

1. **Per-act baselines**, from §4's already-published totals divided by `n = 124`:
   `H(V) = 0.205593` bits/act, `H(V|M) = 0.166070`, `I(V;M) = 0.039523`. Multiplied back by
   `n` these give **25.493 / 20.593 / 4.901** — §4's decomposition A exactly. **Not new
   numbers**, which is the point.
2. **The independent sum** `N·H(V)` against **the correlated joint** `H(V₁…V_N)`, tabled at
   `N = 1, 10, 100, 1000`.
3. **The gap** `N·H(V) − H(V₁…V_N)` at each `N` — the amortisable quantity.
4. **The equality limb, demonstrated numerically**: re-run with the month redrawn i.i.d. per act
   and the joint equals `N·H(V)` to floating-point exactness. Equality iff independent, shown
   rather than asserted.
5. **The `O(1)`/`O(N)` split**: the gap grows at `I(V;M)` per act less a one-off of at most
   `H(M) = 2` bits — algebraically `gap = N·I(V;M) − I(V₁…V_N;M)`, with the subtracted term
   bounded by 2 bits for every `N`. The shared latent is paid once; the residual is paid `N`
   times. This is §4's seam, harvested.

**Verified ahead of the gate.** I ran the computation to check the section can actually carry
what the outline promises before proposing it. The figures below are from that check; if the
asset is licensed, the landed script is the number of record and the section quotes it, not
this table.

| `N` | `N·H(V)` | `H(V₁…V_N)` | gap | gap per act | i.i.d. control |
|---|---|---|---|---|---|
| 1 | 0.2056 | 0.2056 | **0.0000** | 0.00000 | `= N·H(V)` exactly |
| 10 | 2.0559 | 2.0009 | 0.0550 | 0.00550 | `= N·H(V)` exactly |
| 100 | 20.5593 | 17.8871 | 2.6722 | 0.02672 | `= N·H(V)` exactly |
| 1000 | 205.5925 | 167.5696 | **38.0229** | 0.03802 | `= N·H(V)` exactly |

Three things fall out, and each is a sentence §6 wants. The gap is **exactly zero at `N = 1`** —
a batch of one is not correlated, and the inequality's equality limb is visible at the top of the
table before it is stated. The i.i.d. control column returns `N·H(V)` **to floating-point
exactness** at every `N`: equality iff independent, demonstrated. And the per-act gap climbs
toward `I(V;M) = 0.039523` from below — `0.0055 → 0.0267 → 0.0380` — which is the `O(1)`/`O(N)`
asymmetry in numbers: the shared month costs `H(M) = 2` bits **once**, and every further act
harvests the seam again. The identity `gap = N·I(V;M) − I(V₁…V_N;M)` holds at every row with the
subtracted term bounded by 2 bits, as it must be.

**What this connects.** The seam that decomposition A pre-pays in §4 is the same object the
batch amortises in §6. That is coverage of the existing identity, not a new claim — and it is
why I think the section reads as belonging to this paper rather than bolted onto it.

**A consequence I want ruled rather than assumed** — item R-1 below: whether this counts as a
**sixth worked instance**. My recommendation is **no**. The five instances are five choices of
`X` in the chain rule; the aggregate is about repeated acts and is a different object. Keeping
*"five worked instances on two tasks"* intact in §5.5, §6's table, §9's caveat 4 and the
abstract leaves reviewed text untouched, which is the session's stated failure mode to avoid.
The honesty table still gains a row — for the second identification, not for an instance count.

---

## 3. M-2 — the survey question, answered: **the gap is real. Canon lacks the split.**

**Question:** does canon's closure vocabulary, at `v5.7.0`, carry the constructive/verification
split anywhere?

**Answer: no.** The word *constructive* does not occur anywhere in `core/` — not in
`terms.yaml`, not in any claim, not in any document. `term:closure` is settled and purely
**evaluative**:

> *"A predicate is **closed for an arrangement** when the relevant ground is observable and
> **adequacy can be evaluated** within declared resource, latency, and confidence bounds.
> **Decidable** is reserved for the formal special case."*

That is verification-closure and only verification-closure. Nothing in the registry or the claim
graph distinguishes *the verdict can be checked* from *the verdict can be computed by rule*.

**What canon does carry nearby** — the material the refinement can cite:

| Node | What it gives §7 |
|---|---|
| `term:closure` | the definition being refined; the rung the new one sits above |
| `DDD-frame-06` (established) | closure is distinct from generation cost — the seam the new rung sits on |
| `DDD-frame-09` (**retired**) | *"closed predicates make intelligence unnecessary"* — retired because verification-closure leaves generation expensive. **This is the retirement history the refinement must not trip.** |
| `DDD-frame-05` | producer-independence is for trust only — the scoped survivor of that retirement |
| `DDD-measure-11` (reported) | the measure prices the verdict, not the search |
| `core/07` §4.2 | the cheap-generation / hard-generation split — the closest canon comes, and it is about generation *cost*, not about resolution *by rule* |

**Why constructive closure does not trip the retirement, stated as the refinement will state
it.** `DDD-frame-09` was retired because verification-closure does not bound generation:
checking is cheap, search may be NP-hard, so closure alone licenses no claim about the
determiner. Constructive closure does not contradict that — it **sidesteps** it. Where the
verdict is computed by rule there is no candidate search to price, so the premise the retirement
turns on is absent rather than denied. `DDD-frame-06`'s seam is untouched: closure still does
not imply cheap generation; constructive closure is the stronger condition under which the
question does not arise.

**Therefore M-2's scope guard fires.** Per the prompt, the refinement is **drafted citing what
exists** — `term:closure`, `DDD-frame-06`, `DDD-frame-09`'s retirement, `DDD-measure-11` — with
a flagged note that no dedicated node carries the constructive rung, in the same posture §3.1
and §5.3 used before their nodes landed. **The gap is flagged for the Q-wave. Nothing is filed
this session.** Item R-3 below.

---

## 4. M-3 — the citation-upgrade pass, line by line

Nothing is rewritten. Markers are added or upgraded, and where a pending-node sentence is
replaced the replacement is the citation the sentence was waiting for.

### The three already-ruled upgrades

| # | Line | Current text | Proposed | Verified |
|---|---|---|---|---|
| **U-1** | **459–460**, §5.3 | *"A dedicated claim node for the iterated form is pending canon filing; until it lands, the citation basis is the chain rule and the seam identification, as above."* | Delete the pending-node sentence; the paragraph's closing sentence gains `[DDD-measure-14]`. | `DDD-measure-14` exists, status **reported**, and its `notes` name this exact marker as what it was filed on. Its asset is `measure-chained-seams.py` — §5.3's own asset. |
| **U-2** | **277–278**, §3.1 | *"A dedicated claim node for the admissibility condition is pending canon filing; until it lands, the citation basis is the encoded store's definition and the act, as above."* | Delete the pending-node sentence; the **Admissibility** block-quote at **253–255** gains `[DDD-measure-15]`. | `DDD-measure-15` exists, status **projected**. Its statement is the paper's condition almost verbatim, and its `notes` record the GATE 7 wording ruling the paper's phrasing already honours — *computable from*, never *cannot determine the verdict*. The paper's wording passes that test as it stands. |
| **U-3** | **143**, §2.1 | *"**Demand says what must be supplied; cost says what supplying it that way is worth** [DDD-cost-01]."* | Becomes `[DDD-cost-30; DDD-cost-01]`. | `DDD-cost-30` exists, status **projected**, and its `notes` say it was filed **because this exact sentence** *"was doing claim work while riding DDD-cost-01's citation, which is a different claim."* The paper is the instance the node names. Keeping `DDD-cost-01` alongside is correct — the sentence's second half still rests on the locus-of-supply asymmetry. |

**A note on U-2 that is a gain, not a change.** `core/09` now carries admissibility as its own
§2.1. The paper's §3.1 no longer carries the condition alone; the citation is to canon. No
prose change is needed for this — the sentence already reads correctly.

### The Wave 3 `DDD-frame-14` proposals — one strong, one weak, one the ruling did not name

I am reporting these as I actually find them rather than as three equal upgrades.

| # | Line | Site | Assessment |
|---|---|---|---|
| **U-4** | **381**, §5.2 | *"With `A` the answer, this instance's verdict variable, and `R` what is supplied:"* | **Strong fit; recommend.** This is the line where the paper declares that `A` is playing the verdict role. `DDD-frame-14` is exactly what licenses that: the verdict is the determinate as assessed by a declared predicate. Add `[DDD-frame-14]`. |
| **U-5** | **344**, §5.1 | *"`E` is admissible by construction (§3.1): it is fixed before the act."* | **Weak fit; recommend against.** §5.1 is about allocation, and nothing on this line speaks of a verdict landing. Citing `DDD-frame-14` here would be a marker without work to do. If a §5.1 marker is wanted, the honest site is **363–365** — *"Zero residual is not demand destroyed; it is demand supplied entirely by a mechanism"* — but that sentence is **discharge**, so its node is `DDD-frame-16`, and §6.1 will carry it. My recommendation is to let §6 carry it and leave §5.1 alone. |
| **U-6** | **603–607**, §7.1 | *"Where evaluators disagree there are distributions over their judgments…"* and the paragraph following | **Strong fit the ruling did not name.** This is the paper's one passage about outcomes that no declared predicate assesses — which is precisely `DDD-frame-14`'s register split, and `term:outcome` is new canon since the pin. Flagging it rather than proposing it, since it is outside M-3's ruled scope. **Emil's call** — item R-4. |

---

## 5. Drift between the manuscript and canon

**Every drift below landed at `v5.6.0` (the freight session), after the revision merged.** None
was introduced by Wave 3. All three are supersessions the paper has not yet caught up with.

### D-1 — `term:verdict`'s canonical wording (Appendix A). **Material; must be fixed.**

Appendix A promises statements *"reproduced word-for-word from the graph at the refs pinned in
the front matter."* The `term:verdict` row still reads *"For a task with a **decidable**
acceptance predicate"*. Canon at `v5.7.0` reads:

> *"For a task whose acceptance predicate **closes** for the arrangement (`term:closure`;
> *decidable* is the formal special case, not the requirement), the predicate evaluates
> outcomes, and the **task class** supplies one correct output per input point…"*

This matters beyond bookkeeping: the paper's §7 argues at length that *"formal decidability is
the wrong criterion for either"*, and its own appendix currently reproduces a wording that says
decidable. **The body is right and the appendix is stale.** Refresh the row verbatim under M-4.

### D-2 — `DDD-cost-05` re-scoped (`DDD-dec-15`). **Appendix A row plus two body sites.**

Canon changed *"escape is the residual exceeding capacity"* → *"within core/11's capacity model
the escape term is the residual exceeding capacity."* The correction's point: capacity shortfall
is **one generator** of escape, not its definition.

- Appendix A row **821** — stale statement; refresh verbatim.
- **Body site, §5.1, line 370–371** — *"the bits an actor can supply per act, **with escape the
  residual exceeding them**, is a named next result"*. This reproduces the superseded clause.
- **Body site, §8 rate–distortion, line 706–707** — the same clause again.

### D-3 — `DDD-floor-01` re-scoped (same decision). **Appendix A row.**

Canon changed *"demand escapes where residual demand exceeds effective capacity…"* →
*"**residual demand an actor has taken up** escapes where it exceeds… — overflow ∩ open is the
mechanism of capacity-generated escape, **sufficient for escape and not necessary for it**."*
Escape where no supplier took the decision up at all is now explicitly outside the claim's
region. Appendix A row **824** — refresh verbatim.

### Caveat 3, verified as the prompt asks — **it still reads correctly. No rewrite proposed.**

Caveat 3 (line 733–736) says `H(V|X)` bundles judged and escaped demand and that cleaving them
needs an actor-capacity model. `DDD-frame-15` partitions **discharge** — and its `region` field
guards precisely this seam, insisting the four modes do **not** partition governance-supply. The
caveat concerns the cleave **within the residual**, a different object, exactly as the prompt
states. Caveat 3's own wording is safe as written.

**The exposure is at D-2's two body sites, not at caveat 3.** Those two sentences state the
capacity–escape relation as an identity, which is the form `DDD-dec-15` corrected. I am
**reporting, not rewriting** — a minimal repair exists (*"with escape the residual exceeding
them"* → *"with capacity shortfall one generator of escape"*), but it touches reviewed prose and
is Emil's to rule. Item R-5.

### D-4 — new canon since the pin that the paper may want, none of it obligatory

`term:act-individuation` (settled): *"one act = one verdict of the acceptance predicate at the
declared boundary… batch boundaries are verdict boundaries."* Directly load-bearing for §6 — it
is what licenses the batch framing — and proposed as a §6 citation. `term:outcome` (settled)
underpins U-6. `core/09` §1's **unit of account** paragraph now states canon-side that *"volume
is a parameter demand never sees; it prices supply, not the task"* — which is the Scale
paragraph's position, now carried upstream. §6.2 should cite it: it is the strongest available
guard against the section being read as reopening `nH(V)`.

### D-5 — the context doc's word count is stale. **Reportable now, ruled at M-4.**

`measure-paper-context.md` records *"4,657 words at Gate 4 (target 5,000–7,000)."* The
manuscript as merged is **≈7,440 prose words** (tables excluded; ≈8,040 including tables), body
through Reproduction. The figure predates the external-review revision, which grew the paper
substantially.

**So the paper is already at the top of its target band before §6 is written.** §6 as outlined
adds roughly 700–900 words. The prompt anticipated *report the number, Emil rules if it matters*
— it matters somewhat more than that framing assumed, and I would rather say so at Gate 1 than
at Gate 4. Item R-6. I am **not** proposing a trim: the review settled this register, and
padding-free length is what it settled on.

---

## 6. What I need ruled

| # | Item | My recommendation |
|---|---|---|
| **R-1** | Does the aggregate computation count as a **sixth worked instance**? | **No.** Keep *"five worked instances on two tasks"* in §5.5, §6's table, caveat 4 and the abstract. The five are choices of `X`; the aggregate is a different object. Leaves reviewed text untouched. |
| **R-2** | The **second identification** (correlated verdicts ↔ cacheable work) has no canon node. | Draft it register-native in §6.6 with its falsifier, flag the gap, **file nothing**. Per the session rule. |
| **R-3** | M-2's gap is confirmed. | Draft the §7 refinement citing `term:closure`, `DDD-frame-06`, `DDD-frame-09`, `DDD-measure-11`, with a flagged pending-node note. **File nothing.** Gap goes to the Q-wave. |
| **R-4** | `DDD-frame-14` at **§7.1** (U-6) — outside M-3's ruled scope. | Take it; it is the paper's best register-split site. But it is Emil's call. |
| **R-5** | D-2's two **body** sites reproduce a superseded clause of `DDD-cost-05`. | Repair both with the minimal edit. Reporting, not rewriting, until ruled. |
| **R-6** | Length: ≈7,440 words before §6; §6 adds ≈700–900. | Add the section, report the final number at Gate 4, no trim. |
| **R-7** | Placement: new **§6**, renumbering §6→§7 … §10→§11, 19 cross-references. | Proceed. Mechanical and reviewable. |
| **R-8** | Front-matter downstream pin. | **`v0.4.0`.** Verified: the annotated tag resolves to `5455fcf` — the commit Emil named out of band — and carries `DDD-cost-06`/`DDD-cost-07` **identical to head**. The current pin `d8fd8e6` resolves but is not a tag. Upstream advances `v5.3.0` → **`v5.7.0`**. |
