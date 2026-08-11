# Project context — The Measure Paper (v2)

**Purpose.** Canonical context for work on the measure note. Settled canon unless marked OPEN.
Where this file and older material disagree, this file wins. **Supersedes v4.4 entirely** — no
session should work from v4.4 guidance.

**Canon source.** The note is a projection of `actor-indexed-determination` at `v5.3.0`
(principally `core/09-the-measure.md`, `core/06-composition.md`, the `DDD-measure-*` and per-act
`DDD-cost-*` claims, and `core/assets/measure-*.py`) and `decision-driven-design` at `v0.4.0`
(the volume cost claims `DDD-cost-06/07` and the ratified related-work source). **The repo is
ground truth; fetch both before producing file changes.** Canon authority lives in the claim
files, not in prose — including this file.

**The manuscript's home is this directory:** `papers/measure-note/measure-note.md`, with its two
downstream assets in `assets/`. Papers are projections; projections live in the repo. The
chat-artefact era ended with the Gate 1 ruling of 2026-08-11 — there is no authoritative uploaded
copy of anything, anywhere.

---

## 1. The paper

**Title:** *Specification Demand Is Verdict Entropy: Conservation as the Chain Rule*
**Author:** Emil (Context&), sole author
**Venue:** arXiv first. A formal note; the register differs from Paper A's throughout.
**Length:** 4,657 words at Gate 4 (target 5,000–7,000; ruled: no trim list, and explicitly no
padding — the floor is not a target).

**Relationship to Paper A.** Paper A (*The Missing Parameter: Actor-Indexed Determination*)
states the actor-general principle and cites this result rather than deriving it. This note cites
A for the framework and does not restate it.

**Why this paper exists.** It pays the counting-procedure debt booked in the principle repo's
`meta/lineage-and-limits.md`: it supplies the procedure for closing predicates and shows the
invariance is a theorem.

---

## 2. The result

> **For a task whose acceptance predicate closes, specification demand is the Shannon entropy of
> the verdict over the ground the task faces.** `D = H(V)`, in bits. Conditioning on any variable
> `X` splits it by the chain rule into what `X` encoded, `I(V;X)`, and what remains, `H(V|X)`.
> Three of the framework's separately-stated claims are this one identity: `X` a **decomposition**
> gives the seam; `X` an **actor's encoding** gives the store allocation; `X` a **retrieval
> policy** gives RAG. Two further instances extend the worked coverage without adding a fourth
> claim: the identity **iterated** across a two-level chain (internal seams as conditional
> mutual-information terms), and a **ground-distribution sweep** across three deployments.

**Naming.** Inside the engineering projection, **specification demand**; the actor-general term
is *determination demand*, used only when referring up to Paper A. It is a **principle**, never a
law. **Register, load-bearing:** on the closing region conservation is a theorem, and saying so
is not a promotion — the theorem is Shannon's. **Say "the theorem is Shannon's" first, always,
and never write "law" as a self-reference.**

**Projection discipline, held for the whole manuscript:** the paper may not introduce claims.
Every load-bearing statement cites a graph node (`[DDD-…]`, `[term:…]`) or is register-native
(positioning prose or historical attribution). Where a needed node does not exist, the statement
carries a flagged pending-node note, and the filing is a canon-session item — never this
session's act.

---

## 3. The critical framing — carried into the note as §6

The identity holding is not evidence; the note says so before a reviewer can. What the
computations establish: the identification is **computable**, **non-degenerate**, qualitatively
**right-signed**, and consistent across five worked instances on two tasks. What they do not:
that conservation is empirically true, that the identification is the right one, that
information-theoretic demand predicts any engineering quantity, or anything about open
predicates. The falsifiable content lives in the correspondence (`I(V;S)` predicts interface
cost; `I(V;E)` predicts unaided performance — `DDD-measure-07`), stated in §6 as a protocol and
**not run** (settled position; see OPEN log). The note's §6 also carries the ratified
measure-role addendum: **the measure's job is to exist, not to be computed; necessary for the
warrant, unnecessary for the operation** [`DDD-frame-11`].

---

## 4. The five instances (all reproduce; verified this session)

| § | Instance | Asset | Resolves at |
|---|---|---|---|
| §4 | Decomposition seam (both splits sum to 25.493) | `measure-toy.py` | upstream `v5.3.0` |
| §5.1 | Actor store allocation (three sums = 25.493) | `measure-actor-allocation.py` | upstream `v5.3.0` |
| §5.2 | Retrieval / encode-verify (`H(A)` ≈ 2.61 invariant) | `measure-rag.py` | upstream `v5.3.0` |
| §5.3 | Chained seams (iterated chain rule, both orders) | `measure-chained-seams.py` | `assets/` here |
| §5.4 | Non-uniform ground (three deployments) | `measure-nonuniform-ground.py` | `assets/` here |

Numbers appear in prose only from the scripts; every stated value re-runs. §5.2 is presented as
a demonstration that the identification survives an estimated channel — never as conservation
measured in the wild (`DDD-measure-05`, region line; ruling R-a, settled).

---

## 5. The boundary — the paper's best feature

The measure exists iff the acceptance predicate **operationally** closes; it vanishes exactly at
the floor, where the framework's independent floor result predicts measurement must fail
(`DDD-measure-06`). Presented as a boundary correctly drawn, §7, not buried as a limitation.

---

## 6. Caveats as merged (§9)

1. The theorem is Shannon's; the claim is the mapping.
2. Demand is relative to the ground distribution — **now worked** (§5.4), remains a genuine
   added parameter (`DDD-measure-12`).
3. Escape is not separated from judgment; actor-capacity model is the named next result
   (`DDD-cost-05`). The note states it and stops.
4. **Five instances is credibility, not certification.** Chained seams and non-uniform ground
   worked; **multi-actor composition remains**. Information-theorist certification outstanding.
5. The correspondence to engineering quantities is untested — the most important.

---

## 7. Structure as merged

§1 counting problem · §2 definition · §3 chain rule · §4 worked example and the correction ·
§5 five instances (5.1 actor, 5.2 retrieval, 5.3 chained seams, 5.4 non-uniform ground, 5.5 what
is unified) · §6 what the computations establish + measure-role addendum · §7 where the measure
stops · §8 related work · §9 caveats · §10 one line · Reproduction. §6 sits before §7 by design —
concession before boundary reads as argument, not apology.

---

## 8. Working conventions

- British spelling; one idea per sentence; tables for structures, prose for arguments.
- The identity is reported as arithmetic and projected as a model; never fused.
- Notation stated once and used exactly — operators: `H(·)` Shannon entropy in bits, `H(·|·)`
  conditional entropy, `I(·;·)` mutual information, all with respect to `P`; variables: `V`
  verdict, `A` the answer (§5.2's verdict variable), `X` conditioning variable, `S`
  decomposition, `E` actor encoding, `R` retrieval, `P` ground distribution, `n` points. Worked
  tables report the `H(V)·n` scale, marked `·n` in every header; §5.2's RAG table is per-act
  bits and carries no `·n`. (A future revision may unify `A` with `V`; ruled not-now at Gate 4.
  That same pass must rename the decomposition labels **A**/**B** of §4 and §5.4, which collide
  with `A` the answer.)
- Fetch the live repos before producing file changes; hold at every gate; flag additions Emil
  did not confirm.
- Commits citing canon carry a `Basis:` line naming the claim and term IDs they rest on.

---

## 9. Related work

**Replaced by the merged section.** §8 of the manuscript is the ratified related-work section
(line-level, 2026-08-10); its source of record is `meta/measure-note-related-work-2026-08-10.md`.
Do not re-derive positioning guidance from v4.4 — the section exists; edits to it are line-level
ratification matters.

---

## 10. OPEN log

**Settled (2026-08-10 / 2026-08-11 rulings):**

- ~~RAG instance as evidence?~~ **Settled (R-a):** demonstration that the identification
  survives an estimated channel; never measurement. §5.2 as merged is the canon reading.
- ~~Work chained seams / non-uniform ground before submission?~~ **Settled (R-b):** both worked
  (§5.3, §5.4); multi-actor composition remains and is named honestly in caveat 4.
- ~~Correspondence campaign in this paper?~~ **Settled:** proposed as a protocol in §6, not run.
  Running it is a different paper.
- ~~Escape/judgment split here or in the floor-mechanism paper?~~ **Settled:** named next
  result; this note states it and stops.
- ~~Related-work positioning.~~ **Settled:** merged as §8 (see §9 above).

**Open:**

- **Information-theorist certification** — a collaboration, not a research task. The outreach
  instrument is `papers/measure-note/reviewer-brief.md`.
- **Multi-actor composition** — the one instance still owed (caveat 4).

**Recorded for the next canon session (not this project's to execute):**

- Promote `measure-chained-seams.py` and `measure-nonuniform-ground.py` to upstream
  `core/assets/`; file the iterated-form claim node (next free `DDD-measure-14`), at which point
  §5.3's pending-node flag upgrades to the ID. The chained-seams asset is the worked instance
  `06-composition.md` names as owed; cite it in the filing.
- The `term:maturation` collision items and the 06/08 carve, per the recorded ruling of
  2026-08-10 (see `meta/measure-note-related-work-2026-08-10.md`, closing addendum).

**Emil, out of band:** cut `v0.4.0` on `decision-driven-design` at `5455fcf` before the PR
merges — the front-matter pin resolves against it.
