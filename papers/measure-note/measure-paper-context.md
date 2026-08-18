# Project context — The Measure Paper (v3)

**Purpose.** Canonical context for work on the measure note. Settled canon unless marked OPEN.
Where this file and older material disagree, this file wins. **Supersedes v2 entirely**, which in
turn superseded v4.4 — no session should work from either.

**Canon source.** The note is a projection of `actor-indexed-determination` at **`v5.7.0`**
(principally `core/09-the-measure.md`, `core/06-composition.md`, `core/13-delivery.md`, the
`DDD-measure-*`, `DDD-frame-*` and per-act `DDD-cost-*` claims, and `core/assets/measure-*.py`)
and `decision-driven-design` at **`v0.4.0`** (the volume cost claims `DDD-cost-06/07` and the
ratified related-work source). **The repo is ground truth; fetch both before producing file
changes.** Canon authority lives in the claim files and the term registry, not in prose —
including this file.

**The manuscript's home is this directory:** `papers/measure-note/measure-note.md`. Papers are
projections; projections live in the repo. There is no authoritative uploaded copy of anything,
anywhere.

---

## 1. The paper

**Title:** *Determination Demand Is Verdict Entropy: Conservation as the Chain Rule*
**Author:** Emil (Context&), sole author
**Venue:** arXiv first. A formal note; the register differs from Paper A's throughout.

**Length: 9,122 words**, body through Reproduction, tables excluded (9,662 including tables), as
measured at the discharge session's Gate 4. **State the method with the number** — v2 recorded
"4,657 words at Gate 4" against a target band of 5,000–7,000, and both were stale: the figure
predates the external-review revision. §1–§5 alone now measure 4,631 by this method, which is
suggestively close to the recorded 4,657 — but the method behind that figure was never written
down, so the resemblance is an observation and not an explanation. Hence the rule: state the
method with the number.

**The length rule, which replaces the band** (ruled at the discharge session's Gate 2): *the body
is as long as its booked content, reported honestly, with ceiling questions taken explicitly.* No
padding, and no trimming of reviewed content to pay for booked additions. When a figure lands past
what was last accepted, raise it as a question rather than let it drift.

**Relationship to Paper A.** Paper A (*The Missing Parameter: Actor-Indexed Determination*) states
the actor-general principle and cites this result rather than deriving it. This note cites A for
the framework and does not restate it.

**Why this paper exists.** It pays the counting-procedure debt booked in the principle repo's
`meta/lineage-and-limits.md`: it supplies the procedure for closing predicates and shows the
invariance is a theorem.

---

## 2. The result

> **For a task whose acceptance predicate closes, determination demand is the Shannon entropy of
> the verdict over the ground the task faces.** `D = H(V)`, in bits. Conditioning on any variable
> `X` splits it by the chain rule into what `X` encoded, `I(V;X)`, and what remains, `H(V|X)`.
> Three of the framework's separately-stated claims are this one identity: `X` a **decomposition**
> gives the seam; `X` an **actor's encoding** gives the store allocation; `X` a **retrieval
> policy** gives RAG. Two further instances extend the worked coverage without adding a fourth
> claim: the identity **iterated** across a two-level chain, and a **ground-distribution sweep**
> across three deployments.

**Naming.** Inside the engineering projection, **specification demand**; the actor-general term is
*determination demand*. It is a **principle**, never a law. **Register, load-bearing:** on the
closing region conservation is a theorem, and saying so is not a promotion — the theorem is
Shannon's. **Say "the theorem is Shannon's" first, always, and never write "law" as a
self-reference.**

**Projection discipline, held for the whole manuscript:** the paper may not introduce claims.
Every load-bearing statement cites a graph node (`[DDD-…]`, `[term:…]`) or is register-native.
Where a needed node does not exist, the statement carries a flagged pending-node note and the
filing is a canon-session item — never a paper session's act.

---

## 3. The critical framing — carried into the note as §7

What the computations establish: the identification is **computable**, **non-degenerate**,
qualitatively **right-signed**, consistent across five worked instances on two tasks, and — since
the discharge session — **exact in the aggregate**. What they do not: that conservation is
empirically true, that either identification is the right one, that information-theoretic demand
predicts any engineering quantity, or anything about open predicates.

**There are now two identifications and two open correspondences, and §7's table carries both.**

| | Identification | Correspondence, untested |
|---|---|---|
| §2 | determination demand **is** verdict entropy | `I(V;S)` predicts interface cost; `I(V;E)` predicts unaided performance [`DDD-measure-07`] |
| §6 | the aggregate gap **is** cacheable work | measured verdict correlations predict realised amortisation |

The second is **layered on the first and not implied by it** — the first can hold while the second
fails. §6.6 states this explicitly, and it is the thing the next reviewer will test first.

§7 also carries the ratified measure-role addendum: **the measure's job is to exist, not to be
computed; necessary for the warrant, unnecessary for the operation** [`DDD-frame-11`].

---

## 4. The six assets (all reproduce; verified at the discharge session)

| § | Instance | Asset | Resolves at |
|---|---|---|---|
| §4 | Decomposition seam (both splits sum to 25.493) | `measure-toy.py` | upstream `v5.7.0` |
| §5.1 | Actor store allocation (three sums = 25.493) | `measure-actor-allocation.py` | upstream `v5.7.0` |
| §5.2 | Retrieval / encode-verify (`H(A)` ≈ 2.61 invariant) | `measure-rag.py` | upstream `v5.7.0` |
| §5.3 | Chained seams (iterated chain rule, both orders) | `measure-chained-seams.py` | upstream `v5.7.0` |
| §5.4 | Non-uniform ground (three deployments) | `measure-nonuniform-ground.py` | upstream `v5.7.0` |
| §6 | Aggregate discharge over `N` acts | `measure-aggregate-discharge.py` | **next upstream tag** — new with the discharge session |

**The sixth asset does not resolve at the pin, and the note says so** in Reproduction rather than
papering over it. Closing that seam needs an upstream tag carrying the asset; that is a release
descriptor's job and was deliberately not bundled into the paper session. **Carried as an open
item — see §10.**

Numbers appear in prose only from the scripts; every stated value re-runs. §5.2 is presented as a
demonstration that the identification survives an estimated channel, never as conservation
measured in the wild (`DDD-measure-05`; ruling R-a, settled).

---

## 5. The boundary — the paper's best feature, §8

The measure exists iff the acceptance predicate **operationally** closes; it vanishes exactly at
the floor, where the framework's independent floor result predicts measurement must fail
(`DDD-measure-06`). Presented as a boundary correctly drawn, not buried as a limitation.

**Since the discharge session §8 carries a fourth rung above the three requirements:
constructively closed** — the verdict computed by rule from ground available at the act, no
candidate search to price. It is a strengthening, not a fourth failure mode. It **sidesteps rather
than contradicts** the retirement of "closed predicates make intelligence unnecessary": where the
verdict is computed by rule there is no search left to be expensive, so the premise that retirement
turns on is absent rather than denied. See §9 for the open canon item this creates.

---

## 6. Caveats as merged (§10)

1. The theorem is Shannon's; the claim is the mapping. **Now: the mappings**, plural — §6 adds a
   second.
2. Demand is relative to the ground distribution — worked at §5.4 (`DDD-measure-12`).
3. Escape is not separated from judgment. **Verified against `DDD-frame-15`/`16` and unchanged:**
   those claims partition *discharge*, while this caveat cleaves *within the residual* — a
   different object, and `DDD-frame-15`'s own region field guards the seam.
4. **Five instances is credibility, not certification.** Multi-actor composition remains unworked.
   Information-theorist certification outstanding. **The aggregate is not a sixth instance** — the
   five are choices of `X` in the chain rule, and the aggregate is a statement about repeated acts.
5. The correspondences to engineering quantities are untested — the most important, and there are
   now two of them.

---

## 7. Structure as merged

§1 counting problem · §2 definition · §3 chain rule · §4 worked example and the correction ·
§5 five instances · **§6 discharge over many acts** · §7 what the computations establish +
measure-role addendum · §8 where the measure stops · §9 related work · §10 caveats · §11 one line ·
Reproduction · Appendix A.

§6 sits between the instances and the epistemics because its content is worked and §7's honesty
table must cover it. §7 sits before §8 by design — concession before boundary reads as argument,
not apology.

---

## 8. Working conventions

- British spelling; one idea per sentence; tables for structures, prose for arguments.
- The identity is reported as arithmetic and projected as a model; never fused.
- Notation stated once and used exactly. Operators: `H(·)`, `H(·|·)`, `I(·;·)`, all w.r.t. `P`.
  Variables: `V` verdict, `A` the answer (§5.2's verdict variable), `X` conditioning, `S`
  decomposition, `E` actor encoding, `R` retrieval, `P` ground, `M` the month (§5.3's chain, §6's shared latent).
  **Two counts, never interchangeable: `n` points in the input space (the display scale), `N`
  acts.** Both are now declared in §2's Notation paragraph.
- Worked tables report the `H(V)·n` scale, marked `·n` in every header; §5.2's RAG table and §6's
  aggregate table are in bits and carry no `·n`.
- **`§N/M` forms are Ashby's section numbers, not this paper's** (`§7/7`, `§11/7`, `§11/9`). Any
  mechanical renumbering must exclude `§N` followed by `/`. This was nearly a silent corruption at
  the discharge session's Gate 2.
- A future revision may unify `A` with `V` and must then rename §4's and §5.4's decomposition
  labels **A**/**B**, which collide with `A` the answer. Ruled not-now, twice.
- Fetch the live repos before producing file changes; hold at every gate; flag additions Emil did
  not confirm.
- Commits citing canon carry a `Basis:` line naming the claim and term IDs they rest on.

---

## 9. Related work

**Replaced by the merged section.** §9 of the manuscript is the ratified related-work section
(line-level, 2026-08-10); its source of record is `meta/measure-note-related-work-2026-08-10.md`.
The section exists; edits to it are line-level ratification matters.

---

## 10. OPEN log

### Settled at the discharge session (2026-08-19)

- ~~The aggregation mathematics, booked at Wave 3 as "a section waiting on its claims".~~
  **Landed as §6.** `DDD-frame-15`/`16` arrived at `v5.7.0` and `DDD-frame-16`'s region field
  routes the aggregate formal content to this projection explicitly.
- ~~Does the aggregate count as a sixth worked instance?~~ **Settled (R-1): no.** Reviewed §5 text
  stands unchanged.
- ~~§5.3 and §3.1 pending-node sentences.~~ **Settled:** upgraded to `DDD-measure-14` and
  `DDD-measure-15`; the sentences are gone.
- ~~§2.1's demand/cost sentence riding `DDD-cost-01`.~~ **Settled:** now cites `DDD-cost-30`, the
  node filed because of that sentence.
- ~~`DDD-frame-14`'s registers in the manuscript.~~ **Settled:** cited at §5.2 and §8.1, each with
  a clause rather than a bare marker. A third proposed site was **dropped** — a citation that only
  decorates a sentence is noise.
- ~~Three canon drifts from `v5.6.0`.~~ **Settled:** `term:verdict`, `DDD-cost-05` and
  `DDD-floor-01` refreshed verbatim in Appendix A, and `DDD-cost-05`'s superseded clause repaired
  at its two body sites per `DDD-dec-15`.
- ~~The length band.~~ **Settled:** replaced by the length rule in §1 above.

### Settled earlier, carried for the record

RAG-as-demonstration (R-a) · chained seams and non-uniform ground worked (R-b) · correspondence
proposed as protocol, not run · escape/judgment split named and stopped · related-work positioning
merged as §9.

### Open

- **The constructive-closure node (Q32).** The discharge session's survey found canon at `v5.7.0`
  carries **no** constructive/verification split: the word *constructive* occurs nowhere in
  `core/`, and `term:closure` is stated in evaluative terms alone. §8's refinement is drafted
  against `term:closure`, `DDD-frame-06`, `DDD-frame-09` and `DDD-frame-05` with a pending-node
  flag. **For the Q-wave, not for a paper session.** This is the manuscript's only remaining
  pending-node flag.
- **The sixth asset's pin.** `measure-aggregate-discharge.py` resolves at the next upstream tag,
  not at `v5.7.0`. A release descriptor cutting a tag that carries it would let the front matter
  pin uniformly. **Emil's call; deliberately not bundled.**
- **The second correspondence.** Do measured verdict correlations predict realised amortisation?
  Untested, stated in §6.6 with its falsifier. Joins the first correspondence as an open debt.
- **The correspondence campaign** (the first correspondence). Protocol stands in §7, unrun.
  Running it is a different paper.
- **Information-theorist certification** — a collaboration, not a research task. The outreach
  instrument is `papers/measure-note/reviewer-brief.md`, and it now has more surface to certify:
  the aggregate section's inequality and its bound.
- **Multi-actor composition** — the one instance still owed (caveat 4).
- The `term:maturation` collision items and the 06/08 carve, per the ruling of 2026-08-10.

### For Paper A's session

§6's `O(1)`/`O(N)` material is the measure-register form of *paid once, inherited by every run*.
Paper A's structure will want it where it treats standing versus occasioned supply, and it can now
cite a worked projection rather than restate the arithmetic.
