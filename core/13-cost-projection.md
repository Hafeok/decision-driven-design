# Cost, priced across acts

<!-- ddd:contract

requires: [act, cost-register, standing-cost, occasioned-cost]
establishes: [act-volume|act volume]
status: settled
-->

**A projection note.** This file is the volume layer of the cost register: everything in it
quantifies over **act volume** — what persists between acts — which is exactly what the principle
layer's synchronic charter excludes (upstream `DDD-dec-09`; adopted here by `DDD-dec-10`). The
per-act register it prices is upstream canon, pinned in `graph/upstream.yaml`. Numbered `13` to
continue the upstream reading order, which ends at `core/12`; the cross-repo edge points backward
by construction.

**Upstream basis.** The per-act layer this file prices, pinned at a version and a status:

<!-- ddd:ref id=term:act -->
<!-- ddd:ref id=DDD-cost-01 -->
<!-- ddd:ref id=DDD-cost-02 -->
<!-- ddd:ref id=DDD-cost-03 -->

**Claims.** The propositions of this note are landed as claim nodes under `core/claims/`
(`DDD-cost-*`); canon authority for each is its claim file, and this document is their exposition.
The mapping:

| Section | Proposition | Claim | Status |
|---|---|---|---|
| §2 | Volume corollary: all information-priced crossovers at `N* = n·(α/β)` | `DDD-cost-06` | reported (arithmetic) |
| §3 | MDL optimisation: cost = `L(mechanism)` + N·`H(V\|E)`; marginal condition `N* = n·ΔL/ΔR` | `DDD-cost-07` | projected |
| §4 | The `09` §6.2 actor rows are the optimal encodings at three act-volume regimes | `DDD-cost-04` | projected (relocated) |

Where this prose and a claim disagree, the claim governs and the prose is the bug.

**Reproduction script** in `core/assets/measure-mdl-volume.py`. Empirical basis filed in the
principle repository (`meta/mdl-cost-manufacturing-assessment-2026-08-08.md` at the pinned ref).

---

## 1. Act volume and the two-part total

Write **act volume** `N` for the number of acts the arrangement will face — a quantity no demand
identity mentions and the upstream cost register never carries. The upstream register prices one
act: standing cost and occasioned cost are rates at the act (`DDD-cost-01`, pinned). Across `N`
acts the total is

> **C(E, N) = α · standing + β · N · occasioned**

with the demand identity fixing, for every candidate encoding `E`, how much of the verdict each
side must supply per act. Demand says what must be supplied; the per-act register says what each
side's supply is worth at one act; this file says what supplying it that way is worth across `N`
acts. The asymmetry that makes `N` bite is upstream: the standing artifact is paid for once and
present for every act thereafter, the occasioned event is paid at each act, amortising never.

---

## 2. The volume corollary of the degeneracy

Upstream `DDD-cost-02` (pinned): priced in captured information, every distinction has density
exactly 1 — conservation forces ΔI = −ΔR, and the tradeoff is flat. Across acts the flatness
becomes a corollary about crossovers: every crossover sits at the same volume,

> **N\* = n · (α/β)**, identically, for every step of the frontier,

and the whole frontier flips at once — below `N*` supply nothing standing, above it supply
everything. **A graded build-out over volume therefore requires standing cost priced as mechanism
description length.** An identity consequence, *reported as arithmetic*, exercised end to end by
`measure-mdl-volume.py` (all crossovers at N\* = 124 on the date task). *(Claim `DDD-cost-06`,
citing `DDD-cost-02` as basis.)*

---

## 3. The MDL optimisation

The non-degenerate total prices the standing side as description length and the occasioned side by
entropy per act, accumulated over volume:

> **cost = L(mechanism) + N · H(verdict|E)** — MDL's `L(model) + L(data|model)`, with the model
> the mechanism the arrangement stands up, and the data the residual verdicts its actor must
> supply per act.

The rate-split itself — description length prices the standing side, entropy the occasioned side —
is upstream canon (`DDD-cost-03`, pinned), where its per-act occasioned-floor falsifier also
files. What files here is the optimisation over volume and its discriminating prediction, the
**marginal condition**: distinctions flip from occasioned to standing at computable crossover
volumes `N* = n · ΔL/ΔR`, ordered by information density — residual removed per unit of mechanism
description. Falsifier: within-task cost-vs-volume data whose crossover-curve shape contradicts
the marginal condition. *(Claim `DDD-cost-07`.)*

---

## 4. The actor table as optimal encodings

The upstream measure's actor table (`09` §6.2 at the pinned ref — program, weak model, mid model,
one invariant total, three allocations) re-reads under the cost model as **the optimal encodings
at three act-volume regimes**: the encoding worth standing up depends on `N`, and the rows are the
frontier points a cost-minimising arrangement selects as volume grows. Projected; falsifier: an
optimal build-out ordering that contradicts observed actor orderings. *(Claim `DDD-cost-04`,
relocated whole per `DDD-dec-09`/`DDD-dec-10` — ID intact.)*

---

## 5. Reproduce

One self-contained script regenerates every figure in this note:

- `core/assets/measure-mdl-volume.py` — optimal encoding vs volume under both cost models, the
  crossover table (every model-1 crossover at N\* = 124), and the graded build-out under
  description-length pricing, on the upstream `09` §3 date task.

Coefficients are stipulated, not measured. The script exercises the projected optimisation; it
does not and cannot confirm the correspondence.
