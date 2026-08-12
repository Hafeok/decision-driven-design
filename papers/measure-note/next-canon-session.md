# Next canon session — items raised by the measure note's external review

**Status:** input for a canon session, not canon. Nothing here is filed. The revision session that
produced this list filed nothing in `actor-indexed-determination` by instruction; every item below
needs a canon session with its own gates.

**Provenance.** All five items were surfaced by the external review of the measure note and the
revision that answered it (branch `claude/measure-note-revision-75wr59`, this repository). Two of them
are inconsistencies *inside* the term registry that the review found indirectly — it objected to the
paper, and the paper was faithfully projecting canon.

---

## 1. Registry seam — `term:closure` against `term:verdict` on decidability

`term:closure` reserves *decidable* for the formal special case:

> A predicate is **closed for an arrangement** when the relevant ground is observable and adequacy can
> be evaluated within declared resource, latency, and confidence bounds. **Decidable** is reserved for
> the formal special case.

`term:verdict` opens with a different criterion:

> **Definition (determination demand).** … For a task with a **decidable** acceptance predicate, let
> the **verdict** be …

`core/09-the-measure.md` §7 carries the same slip in prose — it rules that formal decidability is the
wrong criterion and then says the note "proves the part that was already inside the **decidable**
region."

**Why it matters.** The review's objection that entropy can exist without decidability lands on this
seam, not only on the paper. The two readings are not equivalent: a predicate can be decidable and not
operationally closed, and vice versa.

**What the paper now does.** §7 separates existence, availability, and estimability, and uses
operational closure throughout; the stray "decidable region" phrasing is gone from the manuscript. The
canon-side wording is untouched.

**Candidate repair.** Bring `term:verdict`'s opening clause into line with `term:closure` — "a task
whose acceptance predicate closes" — and correct the `core/09` §7 sentence. Both are wording changes to
settled terms, so both need ratification rather than a patch.

---

## 2. Registry seam — `term:acceptance-predicate` against `term:verdict` on what the predicate does

`term:acceptance-predicate`:

> The **acceptance predicate** is the criterion that settles whether an outcome is acceptable at the
> declared tolerance.

That is a predicate over outcomes — a relation `A(x, y)`. `term:verdict` then treats the same object as
a function from inputs to outputs:

> let the **verdict** be the correct output the predicate assigns to each point of the input space

**Why it matters.** These come apart exactly where the framework most wants to reason: verification
tasks, and tasks with several acceptable outputs. A predicate that evaluates pairs does not, in
general, name a unique correct output, so `H(verdict)` is not defined for a relation task without a
further declared choice.

**What the paper now does.** §2.2 declares four task classes — decision, function, relation,
verification — states what `V` is in each, restricts the note's worked instances to decision and
function tasks, and states that the entropy of a verification verdict is not the entropy of the
generation task (`DDD-frame-06`, `DDD-measure-11`). It narrows what the note argues; it does not touch
what canon claims.

**Candidate repair.** Either restrict `term:verdict` to the task classes where the function reading
holds, or add the relation case explicitly with the selection rule as a declared parameter. This is
the largest of the five items and may want its own claim node.

---

## 3. `core/assets/measure-rag.py` — replicate band not printed

The asset estimates `H(A)` and `H(A|R)` by plug-in from 40,000 samples per row and computes
`I(A;R) = H(A) − H(A|R)`. Two consequences the asset does not surface:

- the printed `sum` column is exact by construction and is not a check on anything;
- the row-to-row variation in the totals is sampling error on a re-estimated `H(A)`, whose population
  value is 2.6126 bits.

The revision measured the estimator's behaviour and states it in the note's §5.2 — mean 2.6117,
standard deviation 0.0049, central 95% range [2.601, 2.621], bias −0.0008, and recovery of the analytic
conditional entropy to within 0.002 bits in mean over 200 replicates. **Those figures are not printed by
the asset**, and the session was instructed not to fork a canon asset, so the note states the parameters
needed to regenerate them instead.

**Candidate repair.** Extend `measure-rag.py` to print the analytic joint alongside the estimates and to
run the replicate study, so the numbers the note quotes come out of the asset that backs
`DDD-measure-05`. Worth doing before the note ships externally.

**Related, and already flagged in canon:** `DDD-measure-05`'s `notes:` carries an unresolved FLAGGED
tension against `core/09` §6.3's "conservation … measured on a deployed system pattern rather than a
toy." The revision did not touch it. It should be resolved in the same session.

---

## 4. Two claim candidates

Both were named by the review triage. Neither overturns a ratified claim; both look like
strengthenings.

### 4a. The demand/cost distinction

Canon carries the sentence in prose at `core/10-cost.md` §1 — "Demand says what must be supplied; cost
says what supplying it that way is worth" — and carries adjacent content in `DDD-cost-01`
(locus-of-supply asymmetry) and `DDD-cost-03` (the rate split). **No node states the distinction
itself.**

It is the framework's answer to the review's central objection, so it is doing load-bearing work
without a node. The note cites `DDD-cost-01` and `DDD-cost-03` and carries a pending-node flag.

### 4b. The admissibility condition on conditioning variables

The note states it in §3.1, derived from `term:encoded` and `term:act`:

> A conditioning variable `X` is **admissible** if it is a function of ground available at the act, and
> of what the arrangement has standing before it, and not of the verdict itself.

It excludes `X = V`, which is what restores `DDD-measure-10` from near-tautology. It does **not**
exclude a mechanism that computes the verdict from ground — `core/09`'s program encoding does exactly
that and must stay legitimate. Any filing must carry that distinction; a condition written as "cannot
determine the verdict" would break the actor-allocation instance.

The note carries a pending-node flag for this too.

---

## 5. The iterated-form node — `DDD-measure-14`

Already recorded in `papers/measure-note/measure-paper-context.md` §10 and flagged in the manuscript at
§5.3. The chained-seam form

> `H(V) = I(V;S₁) + I(V;S₂|S₁) + H(V|S₁,S₂)`

has no node; the note cites the chain rule and the seam identification instead. Filing it takes the next
free `DDD-measure-*` id, at which point §5.3's pending-node sentence upgrades to the ID.

The same session should promote `measure-chained-seams.py` and `measure-nonuniform-ground.py` from this
repository's `papers/measure-note/assets/` to upstream `core/assets/`, per the context file. The
chained-seams asset is the worked instance `core/06-composition.md` names as owed, and the filing should
cite it.

---

## Not on this list

A notation observation rather than a canon defect, recorded so it is not lost: `core/10-cost.md` §3
writes the degeneracy as `ΔI = −ΔR`, where `R` is the residual. The measure note uses `R` for the
retrieval variable, so the shorthand collides on projection. The note avoids it by writing the two terms
out. If canon wants the shorthand to survive projection unchanged, it needs a different letter.
