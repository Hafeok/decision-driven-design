# Response to review — *Determination Demand Is Verdict Entropy*

**Part 1** is the reply to the reviewer and is written to be sent. **Part 2** is an internal record of
what the revision found, and is not part of the reply.

---

# Part 1 — Response to the reviewer

Thank you. This was a major-revision review and the manuscript has had one. Almost everything you
identified was right, two of your objections cost the paper ground it should not have been holding, and
one of your observations turned out to be an instance of the framework's own position rather than a
counterexample to it. All three outcomes are recorded below without smoothing.

The revision also changed the paper's title. You wrote that "specification demand" risks misleading a
reader, because in engineering usage a specification is the mechanism description — precisely what
entropy does not measure. The companion framework's own term for the quantity is **determination
demand**; "specification demand" was its denomination for the engineering projection. The projection
name failed in the domain it was chosen for, which is the sort of thing only a reader from that domain
finds. The paper is now *Determination Demand Is Verdict Entropy*, and the engineering name is
introduced once, at the definition, as the same quantity under another denomination.

## On length

The body grew from 4,832 to 8,259 words, roughly seventy per cent. Nearly all of it is attributable to
four things you asked for: a task-class declaration (§2.2, +373), an admissibility condition on
conditioning variables (§3.1, +439), a fully specified simulation (§5.2, +417 net), and a correspondence
protocol with controls and a predicted direction (§6, +262). The remaining large additions are the
independent characterisation of demand (§1.1, +259) and the demand/cost section (§2.1, +524) that your
central objection made necessary. The caveats section is shorter, not longer. The length is the review's
doing, and we would rather say so than pad or trim.

## Disposition, objection by objection

| Your objection | Disposition | Where |
|---|---|---|
| Entropy is not specification complexity | **Observation accepted, conclusion resisted** | §2.1 |
| `I(V;X)` is symmetric and observational, not "encoded" or "pre-paid" | **Conceded** | §3.1, §4 |
| Decomposition needs a formal admissibility condition | **Conceded; condition supplied** | §3.1 |
| The closure boundary is overstated | **Conceded** | §7, §7.1, §7.2 |
| An acceptance predicate does not assign the task's output | **Conceded** | §2.2 |
| `nH(V)` as "the demand of a single pass" overclaims | **Conceded** | §2, *Scale* |
| The RAG example is under-specified | **Conceded, and further** | §5.2 |
| A bare correlation would be confounded | **Adopted in full** | §6 |
| Related work: Ashby, Brooks, MDL, rate–distortion | **Conceded on all four** | §8 |
| No conventional bibliography; claim IDs unusable externally | **Conceded** | References, Appendix A |
| Corrupted symbols | **Checked; partly real** | throughout |
| Caveats repeated, rhetoric overheated | **Conceded** | §9 and throughout |

### The central objection — where we agree and where we do not

Your two classifiers with equal `H(V)` and wildly unequal specification cost are correct, and the
manuscript had no visible answer. It does now, and the answer is the framework's, not a repair invented
for this review: **demand is what must be supplied; cost is what supplying it that way is worth.**
Entropy prices the occasioned side — what each act must resolve. Description length prices the standing
side — the mechanism that supplies it. The two classifiers face the same demand per act and differ in
the price of one way of meeting it.

So your counterexample is now the paper's worked illustration of the distinction (§2.1), which is where
it belongs and where it does more good than anything the manuscript previously had. Your recommendation
7 asked for a case where verdict entropy and specification complexity diverge; §2.1 supplies two, held
deliberately apart — divergence in what a mechanism costs to *describe*, and divergence in what an
answer costs to *compute* (a lookup table against a satisfiability instance). The manuscript had been
conflating them.

What we do not accept is the conclusion that the identification is therefore underdetermined. It is
narrow, and it is now stated as narrow. The measure is silent on two axes by construction, both
silences are declared, and neither is a defect in a measure of demand.

The related consequence, which your recommendation 8 pressed and we accept: the MDL relationship is a
tension and not a tidy division of labour. §8 now closes on it — description length reaches an aspect of
specification that entropy cannot reach at all, any account wanting both must carry two registers, and
this note carries one.

### Admissibility, and what your condition needed

Your bullets are adopted essentially as written. An admissible conditioning variable is a function of
ground available at the act, and of what the arrangement has standing before it, and not of the verdict
itself. `X = V` is excluded, and with it your charge that "you cannot decompose your way out of the
work" was close to tautological — which was fair against the unrestricted construction.

One clarification the condition needed, and now carries: it must **not** exclude a mechanism that
*computes* the verdict from the input. The paper's program encoding does exactly that, reaches zero
residual legitimately, and pays for it in standing cost. The distinction is between building the answer
and being handed it. With it, the result recovers its content rather than losing it: the residual
reaches zero only when some admissible mechanism determines the whole verdict, and §2.1 prices what that
mechanism costs. The work is not escaped; it is relocated to the standing side and paid there.

On the naming (your recommendation 5): the substance is conceded and stated at first use — `I(V;S)` is
**verdict information carried by the decomposition**, and "seam demand" is its name *under the
identification*, not a property of mutual information. The term itself is retained because it is a
settled node in the companion framework's registry, and diverging from it in the paper would put the
projection out of step with its source. §4 also now states plainly what a high-information seam does
*not* imply about interface cost, and identifies that as where the reading would fail.

### The boundary — the expensive concession, and an admission

You are right on all three sub-objections, and the correction runs deeper than the review could have
known. The companion framework's own claim node for the boundary carries an explicit instruction:
*claim the boundary as principled, not as convergent evidence.* The manuscript claimed convergent
evidence anyway — "the strongest evidence the identification is the right one." **The overclaim was not
a position we were defending; it was a manuscript out of compliance with its own governing claim.** Your
objection returned it to compliance.

§7 now separates three requirements the manuscript had collapsed into one: **existence** (no verdict
function, nothing to measure), **availability** (a verdict function can exist while its predicate does
not operationally close, in which case `H(V)` is defined and unavailable), and **estimability** (`P`
must be known well enough to estimate; a verdict function alone does not deliver a number). §7.1 states
that open predicates admit distributions over evaluator judgment, disagreement, preference, and scores;
what is unavailable there is this construction, not measurement. The framework already held that from
the other side — its governance question is well-formed on open predicates exactly where the measure is
not, and its governed domain is strictly wider than its measured domain. The manuscript had let the
measure's silence read as the framework's.

The coincidence with the floor is kept and demoted (§7.2). The two arguments share the closure premise,
so their agreement is close to definitional on the measure's side. What is not definitional is that the
line was drawn twice, from different materials, with neither fitted to the other. That makes the
boundary principled rather than arbitrary. It does not make the identification true, and the paper no
longer suggests it does.

One thing we did not adopt: your proposed reformulation, in which the paper would investigate "when
these quantities serve as useful proxies." The companion framework carries the identification as a
*projected* claim with a stated falsifier, and the paper presents it at that strength — neither more nor
less. The revision narrows what the paper **argues**; it does not restate what the framework **claims**
more weakly than the framework holds it. §7.2 says so explicitly so the distinction is visible rather
than implied.

### The simulation

Specified in full, and further than you asked. `A` is drawn from a stipulated eight-outcome prior with
population entropy 2.6126 bits exactly. `R` is a single categorical symbol carrying no document
identity, no content, and no hit flag. Distractors are independent draws from the same prior. **The
supplying process depends on the answer by construction**, maximally so on a hit — which is why the run
is a simulated channel and not a measurement of a retrieval system, and the companion claim's region
line already said so.

Two things you did not reach, which the revision found and states:

- **The sum column was not a check.** `I(A;R)` is computed as `H(A) − H(A|R)`, so the totals sum to
  `H(A)` by construction. The manuscript had presented that as evidence the identity survives
  estimation. It is not, and §5.2 now says it is not — which is the same error the paper's own §6 exists
  to prevent.
- **The real result is better.** What the run does establish is that a plug-in estimator recovers the
  analytic conditional entropy of a channel it is not given in closed form: within 0.002 bits in mean
  over 200 replicates, with up to 0.010 bits of single-run deviation.

Your question about why the totals vary around 2.61 has an exact answer: each row re-estimates `H(A)`
from its own fresh 40,000-sample draw, and plug-in entropy at that sample size has a standard deviation
of 0.0049 bits and a central 95% range of [2.601, 2.621]. Every printed total lies inside it. The
section is also renamed, because you were right that the engineering interpretation was unclear: it
simulates an encode/verify channel, retrieval-augmented generation motivates it, and it is now named for
what it is.

Your sharpest point here we have extended beyond where you raised it. `H(A|R)` assumes an ideal observer,
so it is not the actor's burden — and that applies just as much to the paper's **actor-allocation**
instance, which you did not challenge. Both sections now state that a real actor which cannot exploit
everything the conditioning variable carries faces *more* than the tabulated residual, never less, and
that capacity sits outside the identity.

### The empirical protocol

Adopted in full. §6 now fixes three things in advance: the **direction** (higher `I(V;S)` predicts
higher specification effort, higher boundary defect density, longer time to stabilise — monotone, and a
reliable inverse association falsifies the identification while leaving Shannon untouched); the
**controls**, all nine of yours, with verdict imbalance singled out as structural rather than incidental
because a skewed input distribution lowers `H(V)` and every seam term in one stroke; and the
**baselines**, all six.

On the sixth — MDL of the routing rule — the framework commits before the data. `L(routing rule)` is the
standing side, priced in description length; `I(V;S)` is the demand the seam carries. **The prediction
is that both load and neither subsumes the other.** If `I(V;S)` adds nothing after `L(routing rule)` is
controlled, the demand register is idle where it matters most and the distinction the paper is built on
buys nothing. That is a second falsifier, and it is sharper than the first.

We should record that you arrived independently at the framework's own filed falsifier. Your sentence —
mutual information may be high because a partition aligns neatly with a simple rule, making the
interface cheaper — is, near enough word for word, the falsification condition already recorded against
the identification's claim node. Independent arrival at a filed falsifier is the most useful signal in
the review.

### Related work, presentation, and the smaller items

Ashby is now cited precisely, from the 1956 text: variety defined as a count or its logarithm to base 2
with the bit named as its unit (§7/7), and the Law of Requisite Variety stated in that logarithmic form
(§11/7, with the general statement at §11/9). The Brooks claim is softened as you asked — the paper
offers his distinction a unit only on the region where the measure exists and only for the part of
essential complexity verdict entropy captures, "which is not all of it", with the two uncaptured axes
named. Rate–distortion is now stated cautiously: applying it needs a reproduction variable and a
distortion function, the framework has named neither, and until it does the appeal is a direction of
work rather than a result.

`n` is demoted to a display scale, with the "single pass over an input space" phrasing struck and your
reason given in the text: `nH(V)` is the entropy of `n` independent draws, not the information required
to label `n` distinct points once. Every claim in the paper is now a per-act claim, and the paper's
opening characterisation of demand makes per-act constitutive rather than a reporting convention.

Caveats are de-duplicated to one statement up front, the full treatment in §6, and three booked items at
the end. The flagged formulations — "pays the debt", "conservation is now forced", "makes conservation a
theorem", "the unit it lacked", "strongest evidence" — are all replaced. §3 now carries the load: the
split is exact, the exactness is the chain rule's, and it becomes a statement about conservation only
under the identification.

On the corrupted symbols: the source was clean UTF-8, so the breakage you saw was rendering. **Two
characters were genuinely fragile** — a modifier-letter subscript and a long double arrow, both
commonly missing from PDF fonts — and both are replaced, along with a third the revision would otherwise
have introduced. Thank you for the check; it was a false alarm that was concealing a real problem.

A conventional bibliography is added, with every locator verified against a primary or authoritative
source rather than from memory. **Appendix A** indexes all thirty-five cited graph nodes with their
statements reproduced word-for-word and each claim's status shown, so the paper is checkable without
access to the framework's repository.

## Still open

- **Multi-actor composition** remains the one worked instance the paper owes.
- **Escape is not separated from judgment.** `H(V|X)` bundles both; cleaving them needs the
  actor-capacity model, stated as the next result and not worked here.
- **The correspondence is untested.** §6 states the protocol and does not run it. This remains the most
  important open item, and it is what would make the paper a measured result rather than a well-founded
  one.
- **Certification by an information theorist** (your recommendation 12) is accepted and outstanding.

---

# Part 2 — Internal record

Not for the reviewer.

1. **The name.** Canon's `term:verdict` already marked "specification demand" as the engineering
   projection's denomination of *determination demand*. The rename restores canon's primary term rather
   than inventing one. The finding worth keeping: the projection denomination failed in the domain it
   was chosen for, and only a domain reader would have found it.

2. **The import spec was wrong and the session corrected it.** The minimum-import draft offered three
   destinations for a governing decision — encoded before the act, resolved by whoever acts, or left
   ungoverned. Canon's `term:store` is four: rule, check, actor, nothing. The draft dropped the
   **check**. The shape of that error is exactly what the review's central objection feeds on: a
   partition that nearly matches canon leaves the identification looking like it does more work than its
   materials support. The draft also used "the arrangement", which its own do-not-import list forbids.
   Both corrected before filing; §1.1 carries the four-store form.

3. **The `§4` / `§10` asymmetry is deliberate.** The §4 blockquote keeps "pre-pays more demand into the
   seam" because that is the wording of the reported claim it projects, and §10 keeps "what `X` encoded"
   because it speaks in the framework's voice after §3.1 has conditioned the vocabulary. The abstract is
   neutral for the cold reader. A reviewer comparing them will otherwise read it as inconsistency; if it
   is queried, this is the answer.

4. **Two registry seams surfaced.** `term:closure` against `term:verdict` on decidability, and
   `term:acceptance-predicate` against `term:verdict` on whether the predicate evaluates outcomes or
   assigns them. Both are recorded in `next-canon-session.md`. The reviewer found them indirectly, by
   objecting to a paper that was faithfully projecting canon, and deserves the credit.

5. **Notation, canon-side.** `core/10-cost.md` §3 writes the degeneracy as `ΔI = −ΔR`, where `R` is the
   residual; the note uses `R` for retrieval. The note now writes the two terms out and avoids the
   shorthand. If canon wants the shorthand to survive projection, it needs a different letter.

6. **Estimate corrected in flight.** The session forecast a −300 to −400 word de-duplication at Gate 6
   and delivered −82. The forecast was wrong because §9 was less redundant than assumed and because the
   escape/judgment overlap resolved in §5.5's favour rather than §5.5 being the cut. Recorded because the
   length decision was taken on the corrected number, not the forecast.

7. **Counting method.** The figures in Part 1 are whitespace tokens over the body only, the same measure
   used for the per-section attribution, so the section deltas sum to the total: 4,832 → 8,259. Plain
   `wc -w` gives 4,752 → 8,144. The growth is 71% either way. References and Appendix A are excluded
   from both, at 1,574–1,599 words depending on the measure.
