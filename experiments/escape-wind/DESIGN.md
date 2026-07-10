# Experiment: The Escape/Wind Decomposition

Status: **projected** — this document is the design. It becomes evidence only when linked runs are cited. Do not upgrade.

## The stake

The Escape Under Pressure section claims confabulation decomposes into two classes with different owners:

- **Escape-hallucination** — decisions/facts missing from the priced stores; reducible by allocation.
- **Wind-hallucination** — actor residual variance under full allocation; *not* reducible by allocation, only by binding choice.

This yields three predictions that the existing literatures do **not** jointly make, each independently falsifiable:

**P1 (escape is allocation-sensitive).** For a fixed binding, hallucination rate falls monotonically as demand is relocated from escape into encoded + sensed stores.

**P2 (wind is allocation-insensitive).** Beyond full allocation — every governing decision encoded, every consumed fact in context and verified retrievable — the residual error rate is **stable** across further prompt improvements. Distinct full-allocation prompt variants for the same task set produce statistically indistinguishable residuals.

**P3 (the spatial incentive).** Holding semantic allocation *constant*, capacity pressure alone increases the error rate — and the increase concentrates in escape-class errors (unowned decisions falling to the prior), not wind-class errors.

**Kill conditions, stated up front:**

- If the residual keeps dropping under successive full-allocation prompt variants → the escape/wind split fails: there is no allocation-insensitive floor, "wind" was just unexhausted escape.
- If capacity pressure does not raise error rate at constant semantic allocation → the spatial-escape mechanism fails.
- If pressure raises *wind*-class errors as much as escape-class → the taxonomy's class boundary fails even if the aggregate effect holds.

Any of these outcomes is publishable against the section. That is the point.

## Why this is cheap for us

The binding is already pinned: the DGX Spark serving stack (vLLM, Qwen3.6-35B-A3B-FP8, frozen image, frozen flags) is a pinnable-by-binding actor by construction. The experiment is a completeness-exercise variant: N sampled trials against a declared acceptance predicate, per allocation tier. The whole apparatus is the framework's own sampled tier pointed at the framework's own claim.

## Design

### The task family

One task family where ground truth is mechanical and the governing decision set is enumerable: **structured fact extraction with a decision rule.** Each item is a synthetic source document (so no training-set contamination — generated, not scraped) plus a query whose correct answer requires (a) retrieving 2–4 facts from the document and (b) applying 1–2 governing decisions (a tie-break rule, a unit convention, a scope boundary).

Synthetic sources are mandatory. If the facts could live in the weights, the escape/sensed boundary is uncontrolled — the prior could answer *correctly*, contaminating the escape measurement. Facts must be inventable: fictional entities, arbitrary numeric values, generated identifiers. The prior must have no route to the right answer except the window.

~50 items per cell minimum; power notes below.

### The allocation tiers (P1, P2)

| Tier | Encoded store | Sensed store | Predicted error class present |
|------|--------------|--------------|-------------------------------|
| T0 | bare question | document absent | escape (facts + decisions unowned) |
| T1 | bare question | document present | escape (decisions unowned) |
| T2 | decision rules encoded | document present | wind only, if the split holds |
| T2′, T2″ | *same* decision set, two independently authored full-allocation phrasings | document present | wind only — **the P2 test** |

- T0→T1→T2 tests **P1**: monotone decrease.
- T2 vs T2′ vs T2″ tests **P2**: three distinct surface forms of the same complete allocation. If the split holds, their error rates are indistinguishable. If one phrasing "unlocks" a lower rate, the decision set was not actually complete under the other phrasings — which is either an authoring defect (fix and rerun) or, if it persists under audit, evidence against a stable floor.

Completeness of T2 must be *verified, not asserted*: before the main run, an audit pass confirms every fact is retrievable in isolation (single-fact probe questions, near-100% required) and every decision rule is applied correctly in isolation (single-rule probes). Items failing the audit are repaired or dropped. Without this gate, "full allocation" is a status upgrade.

### The pressure arm (P3)

Take T2 items only (allocation complete) and manufacture pressure without touching semantics:

| Condition | Manipulation |
|-----------|--------------|
| T2-near | facts placed adjacent to the query, minimal padding |
| T2-mid | same content, facts buried mid-context with semantically inert distractor documents (other items' sources, irrelevant), total length ~60–70% of window |
| T2-far | same, ~85–95% of window |

The distractors are inert by construction — they contain no facts about the query's entities, verified by generation. Semantic allocation is identical across the three conditions; only spatial pressure varies.

### Error classification — the load-bearing instrument

Every wrong answer is classified, mechanically where possible:

- **Escape-class**: the error is consistent with the prior deciding — a plausible-but-absent value, a default convention where the encoded rule said otherwise, an answer to the *unconditioned* version of the question. Operationally: the wrong answer is *not derivable from the provided facts under any reading*.
- **Wind-class**: the facts and rule were present and retrievable (audit-verified), and the error is a retrieval/application slip — a value from the *wrong provided fact*, a rule applied to the wrong operand. Operationally: the wrong answer *is composed of provided material*, misassembled.
- **Unclassifiable**: logged, reported, excluded from class-level analysis, included in aggregate.

The classifier is a script over structured answers (the schema forces extractable fields — that is the mechanical-verification store doing its job), with a hand-audit of a 10% sample to validate the classifier itself. If unclassifiable exceeds ~15%, the task family is redesigned before results are read.

### Sampling and binding

- Binding pinned and recorded: image digest, model hash, flags, temperature. Two temperature arms: T=0 (deterministic-ish reading) and T=0.7 (distribution reading, k=5 samples per item). The wind claim is about the *distribution* — the T=0.7 arm is the primary one; T=0 is the cheap smoke test.
- Seeds recorded. Every run emits a manifest: binding, tier, item set hash, raw outputs. Runs are the citable evidence; this document stays projected until they are linked.

### Power, roughly

Detecting a difference between a ~5% and ~10% error rate at α=.05, power .8 needs ≈430 trials per cell — at k=5 samples that is ~90 items per cell, or accept coarser resolution at 50 items. The P2 *equivalence* claim needs the most care: equivalence testing (TOST) with a declared margin — propose ±3 percentage points as the indistinguishability bound, declared before the run, not after. Fit the item count to the Spark's throughput; at 65k context and 4 seqs, the pressure arm is the slow one.

## Readout

| Result | Verdict |
|--------|---------|
| Monotone T0>T1>T2, and T2≈T2′≈T2″ within margin, and pressure raises escape-class but not wind-class | All three predictions stand; section upgrades to reported with runs cited |
| T2 variants differ beyond margin after authoring audit | P2 falls; escape/wind split is retired or weakened to a tendency |
| No pressure effect | P3 falls; spatial incentive retired from the section |
| Pressure raises both classes equally | Aggregate mechanism survives, taxonomy boundary falls |

Partial survival is a legitimate outcome and gets reported as such. No silent scope-narrowing after the fact.

## What this does not test

- The human arm. P1–P3 have human analogs, but the checklist literature already covers P1-human, and a human P2/P3 study is not cheap. Out of scope; the section's human claims remain projected on this experiment's completion.
- The mechanistic reading. A positive result says the allocation accounting predicts error structure; it says nothing about attention internals. The guardrail holds either way.
