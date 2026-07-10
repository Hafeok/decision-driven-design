# Task-Shape Taxonomy and Seed Exercise Corpus

> apparatus note — campaign instrument. Defines the two task shapes the escape-split
> campaign attributes against, the tagging discipline that keeps a decision assignable to
> exactly one shape, and a seed set of exercise decisions tagged by shape. Feeds E2–E3
> (and F1–F4, which overlap). Not a claim; an instrument for producing evidence.

---

## Why shape is the binding variable

The escape-split prediction says reach-bound escape and resolution-bound escape separate
along the active/total axis. That prediction is only measurable if each exercise decision
loads *one* of the two capacities and not the other — otherwise an escape can't be
attributed to reach vs resolution, because both were under load at once.

So the corpus is not "hard tasks." It is tasks engineered to be **capacity-selective**: a
breadth-shape decision must exhaust reach while leaving resolution slack; a depth-shape
decision must exhaust resolution while leaving reach slack. A decision that loads both is
not usable for attribution — it goes in the discard bin, and its existence is itself a
finding about the taxonomy's sharpness.

This mirrors the SPMC axis-isolation discipline (E4): you cannot attribute a residual to an
axis you did not hold the others fixed against. Shape isolation is axis isolation applied to
the two capacity bounds.

---

## The two shapes

### Breadth shape — reach-selective

A breadth-shape decision requires the actor to *retrieve and combine knowledge spanning
many domains or entities*, where each retrieval is shallow — no multi-step derivation, just
recall and assembly. The governing decision is settled the moment the right facts are in
hand; there is little decision *work* once they are.

Diagnostic properties:
- The decision references entities, APIs, conventions, or facts from **many distinct
  domains** (the wider the span, the more total-parameter reach it demands).
- Each sub-fact is **individually shallow** — a single lookup, not a chain.
- **Encoding the missing knowledge into context closes it.** If you can hand the actor the
  fact and the decision resolves, it was reach-bound.
- Per-step reasoning depth is **low**: one forward pass has ample room; the constraint is
  what the pass can *reach*, not what it can *compute*.

Escape signature under load: the actor confabulates a plausible-but-wrong fact for a domain
it could not reach — the classic recall hallucination. Reducible by reach (total params) or
by transmitting the fact.

### Depth shape — resolution-selective

A depth-shape decision requires *multi-step derivation within a narrow, fully-reachable
domain*, where no single step needs exotic knowledge but the chain is long enough that one
forward pass cannot hold the whole derivation. The facts are all present or trivially
reachable; the decision *work* is the constraint.

Diagnostic properties:
- The decision stays **within one domain** the actor demonstrably knows (verify by
  confirming the actor answers each isolated sub-step correctly).
- It requires a **chain of dependent steps** — each step consumes the last, no step is
  skippable, and the chain length exceeds what one pass resolves.
- **Decomposing the action into smaller per-pass steps closes it.** If splitting the
  decision so each sub-step is its own action resolves it, it was resolution-bound.
- Reach demand is **low**: all needed knowledge is present; adding more context does *not*
  help and may hurt by crowding the working room.

Escape signature under load: the actor drops or transposes a middle step — arithmetic slips,
skipped constraints, a conclusion that doesn't follow from its own stated premises. Reducible
by resolution (active params) or by decomposition.

---

## The reducibility test (the attribution primitive)

Every escaped decision is classified by *which intervention closes it*, run as an actual
A/B, not a judgment call:

| Intervention | If it closes the escape | Classification |
|---|---|---|
| Add the missing fact(s) to transmitted context, nothing else | escape closes | **reach-bound** |
| Decompose the action into smaller per-pass steps, same total knowledge | escape closes | **resolution-bound** |
| Neither closes it across repeated runs | escape persists | **wind-class** (irreducible residual) |
| Both independently close it | escape closes either way | **discard** — decision loaded both capacities; not shape-clean |

The discard row is load-bearing for honesty. A decision that both interventions close was
not capacity-selective, so it cannot testify about the split. Counting discards is part of
the no-silent-residual discipline: every escape lands in exactly one of
{reach-bound, resolution-bound, wind-class, discard}, and a high discard rate is a signal
the corpus needs sharpening, not a result to bury.

---

## Seed exercise corpus

Twelve seed decisions, six per shape, phrased as product-cli exercise decisions (a governing
decision an actor must make against a bundle). Each is tagged with its shape, the reach span
or chain depth that makes it selective, and the pre-declared closing intervention. These are
seeds — the campaign expands each into a family by varying difficulty until the escape rate
lands in a measurable band (neither floor nor ceiling).

### Breadth-shape seeds (reach-selective)

**B1 — Cross-library API reconciliation.** Given a task touching four unrelated libraries
(e.g. an RDF store, an HTTP client, a date library, a CLI parser from four ecosystems),
decide the correct call signature for each. *Selective because:* span = 4 domains, each call
shallow. *Closes by:* transmitting the four signatures.

**B2 — Multi-jurisdiction convention lookup.** Decide the correct date/number/currency
formatting for a record spanning several locales. *Selective because:* wide locale span, each
rule shallow. *Closes by:* transmitting the locale rules.

**B3 — Cross-domain entity disambiguation.** Given a term that names different things in
five distinct fields, decide which sense applies from surrounding context. *Selective
because:* the reach is knowing all five senses. *Closes by:* transmitting the sense
inventory.

**B4 — Dependency-version compatibility recall.** Decide whether a set of package versions
from different ecosystems are mutually compatible. *Selective because:* breadth of ecosystem
knowledge; each check shallow. *Closes by:* transmitting the compatibility facts.

**B5 — Standard-conformance field mapping.** Map fields from three unfamiliar provider
schemas onto one canonical model (the calendar-flow provider-neutrality problem, generalized).
*Selective because:* three foreign schemas, shallow per-field. *Closes by:* transmitting the
schema definitions.

**B6 — Idiom-across-languages translation.** Decide the idiomatic equivalent of one
construct across several programming languages. *Selective because:* wide language span,
shallow per-language. *Closes by:* transmitting the per-language idioms.

### Depth-shape seeds (resolution-selective)

**D1 — Constraint-chain scheduling.** Within the calendar domain the actor knows, decide a
valid slot satisfying a chain of ~8 interdependent constraints (ordering, buffers,
timezone-relative windows) where each constraint consumes the last. *Selective because:*
single domain, long dependent chain. *Closes by:* decomposing into per-constraint sub-steps.

**D2 — Multi-hop graph derivation.** Given a small RDF graph fully in the bundle, decide the
answer to a query requiring ~6 chained SPARQL-style hops. *Selective because:* all facts
present, depth is the hop chain. *Closes by:* decomposing into per-hop sub-queries.

**D3 — Nested arithmetic reconciliation.** Reconcile a figure requiring a long chain of
dependent arithmetic (allocations, percentages, carries) — the specification-demand ledger
math itself is a natural instance. *Selective because:* trivial per-op, long dependent chain.
*Closes by:* decomposing into per-operation steps.

**D4 — Recursive spec derivation.** Given a How element, derive the full SPMC bundle by
walking the derivation contract through several dependent levels. *Selective because:* one
framework, deep derivation chain. *Closes by:* decomposing per derivation level.

**D5 — State-machine trace.** Trace a deterministic state machine (fully specified in the
bundle) through ~10 transitions to decide the final state. *Selective because:* all rules
present, depth is the trace length. *Closes by:* decomposing per transition.

**D6 — Conditional-logic resolution.** Resolve a decision governed by deeply nested
conditionals (fully stated) to decide which branch fires. *Selective because:* all conditions
present, depth is the nesting. *Closes by:* decomposing per nesting level.

---

## Wiring into the campaign

- **E2 (attributed residual):** run each seed family against both falsification-test bindings
  (Qwen3-4B dense, Qwen3-30B-A3B) and both in-stack bindings (35B-A3B, 27B-dense). Every
  escape gets the reducibility A/B; tabulate reach-bound / resolution-bound / wind / discard
  per binding per shape.
- **E3 (convergence cycle):** the closing interventions *are* the convergence moves — a
  reach-bound escape is closed by encoding (context), a resolution-bound escape by
  decomposition (the funnel). The campaign therefore measures the two projections directly:
  encoding closes reach escapes, funnel decomposition closes resolution escapes.
- **F-overlap (Paper B):** the depth-shape seeds are the digital, fully-reachable decisions
  the zero-floor postulate speaks to — every depth escape must close by decomposition (no
  residual tacit step), or the postulate takes damage. Depth-shape discards and wind-class
  depth escapes are the postulate's stress points and must be reported, not smoothed.

**Kill condition inherited:** if the reach/resolution escape ratio does not separate by
architecture (TOST inside the pre-declared equivalence margin, per the capacity note), the
decomposition is retracted regardless of how clean the corpus is. A sharp corpus that
produces no separation falsifies the prediction more strongly, not less.

---

## Status

**Projected instrument.** The taxonomy and reducibility test are derived; the seed corpus is
authored but unexercised. Promotes to **reported** only when the seeds have been run, escape
rates land in measurable bands, and the discard rate is low enough that attribution is
trustworthy. First exercise run against product-cli is the gate.
