# The SDLC Projection

**The framework, denominated in software delivery.** This is the agentic/DAG design framework that
constituted the whole of Decision-Driven Design through v3. In v4 it takes its proper place: the
**engineering projection** of the general principle — *Conservation of Specification Demand*, which is
what *Conservation of Determination Demand* is called when the actor is building software.

Nothing here is deprecated. The reframing is a promotion: what looked like the framework was always
*one projection* of it.

---

## How this relates to `core/`

| In `core/` (general) | Here (software) |
|---|---|
| Determination | a decision in the SDLC — a feature choice, an ADR, a test criterion |
| Ground | the repo, the schemas, the live environment, the source of truth |
| The four stores | encoded constraint · CI check · human/model judgment · the unhandled case |
| Actor (`04`) | a role in the DAG — human, model, or program, pinned accordingly |
| Seam demand (`05`) | the interface contract between roles; the orchestration layer |
| Encode/verify (`apparatus`) | pinning controlled ground; verifying third-party APIs and live env |
| Floor-in-the-predicate (`03`) | which decisions a model can own (closing predicate) vs. which need a human |

The design docs below predate the `core/` layer. They remain correct as *engineering guidance*; where
they reach for a foundational justification, that justification now lives in `core/`, stated more
generally and more carefully.

---

## The design documents

These are the v3 documents, retained. Read `core/` for *why*; read these for *how to build it*.

1. **[`01-foundations.md`](01-foundations.md)** — LLMs as knowledge forecasters; work as a chain of
   context-conditioned decisions; value actions as the terminus; roles and artifacts; the DAG, not the
   pipeline. *Start here for the software framing.*

2. **[`02-entity-reference.md`](02-entity-reference.md)** — the vocabulary made precise: processes,
   decisions, actions, interpretations, roles, artifacts, sessions, schemas, bundles, audits, the
   orchestration system, per-role autonomy.

3. **[`03-autonomy-levels.md`](03-autonomy-levels.md)** — the 0–5 autonomy ladder, why autonomy is
   per-role not per-system, and why this structure is what makes Levels 4–5 reachable. *Now with a
   sharper foundation: per-role autonomy is exactly the actor model's pinning resolution (`core/04`),
   and the ceiling on a role's autonomy is set by the closure of its acceptance predicate (`core/03`).*

4. **[`04-implementation.md`](04-implementation.md)** — the build architecture: Rust + Oxigraph, curated
   SPARQL for bundle assembly, the event substrate, the worker contract, emergent decisions during
   action, the meta-loop, the model catalog.

> **Note.** These four documents are carried forward from v3 and are **not yet fully reconciled** with
> the v4 register (they may still say "law" where `core/` now says "principle," and may still lean on
> the pre-review immune framing). Reconciling them is tracked in
> [`../../meta/consolidated-state.md`](../../meta/consolidated-state.md). The `core/` layer wins wherever
> they conflict.

---

## Where the projection sharpens the design

Three places where `core/` gives the SDLC framework something it did not have before:

**Which role gets which decision** is no longer a matter of taste. `core/03` says a decision can be
owned by a model iff its acceptance predicate closes over digital ground; otherwise it needs an actor
selected for competence on open predicates (a senior, a domain expert). *Autonomy is bounded by
closure.*

**The orchestration layer is a seam**, and `core/05` prices it: an orchestrator is cheap to specify
and expensive per run, a bottleneck, and the poisonable centre of the system. The compound move —
harvesting recurring coordination decisions into encoded rules, with a check on each — is how a
DDD-shaped system gets cheaper over time instead of paying full judgment cost on every run.

**Verification of third-party and environment ground** is not optional and not build-triggered.
`apparatus/encode-verify.md` says why: their truth moves on their clock, so the check must run on a
schedule, and an unreachable source is `Unknown`, never a pass.

---

## Reference implementation

**[`product-cli`](https://github.com/Hafeok/product-cli)** — the authoring layer for this projection:
owns features, ADRs, test criteria, dependencies; builds the derived graph; assembles curated bundles;
runs audits; serves the engineering graph. The companion orchestration harness is designed against the
patterns in `04-implementation.md`.
