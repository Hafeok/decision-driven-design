# Encoding a Domain: Context, Bundle, Phases, Types

> **Apparatus §3 — informative.** The [core](../core/) law says the way to make a decision well is to move its knowledge into the encoded store. This document is the *how*: the concrete machinery by which a domain's knowledge is packaged, transmitted, sequenced, and — as it recurs — frozen into reusable structure. If [§1](01-decisions-and-artifacts.md) established that artifacts are what flows and [§2](02-entities.md) named every entity, this is where the two meet the practical question: **what does the encoded store actually look like when you build it?**

The encoded store is not an abstraction in a running system — it is files, schemas, and queries. This document walks the four things a builder actually assembles: the **context** a decision sees, the **bundle** that delivers it, the **phases** that sequence the graph, and the **task types** that let recurring work descend the [maturation curve](../core/04-projections.md#maturation-allocation-over-recurrence). Together they are the encoding apparatus — the concrete form the law's "encoded" store takes.

## Context: what a decision sees

**Context is the set of artifacts that condition a specific decision.** It is what the role sees when it forecasts. Same role, different decisions, different contexts — the architect approving a design reads a different context than the architect retiring a deprecated module.

Context is not free-form. It is a *deterministic assembly* of artifacts, following the graph: "context for feature X" means "X plus its linked decisions plus their tests plus relevant dependencies." It is reproducible because the graph is reproducible — the same graph, the same focal artifact, and the same assembly query produce the same context every time.

This determinism is what makes the [conservation law](../core/01-the-law.md) auditable in practice. If context were assembled by hand or by a model's discretion, you could never say what the encoded store *contained* for a given run. Because it is a query over a graph, you can — and the [completeness exercise](../core/02-completeness.md) can walk it.

### Frozen vs. sensed context

The [environment clause](../core/01-the-law.md#the-environment-clause-when-the-demand-is-finitely-encodable) splits context by binding time, and the apparatus makes the split concrete:

- **Frozen context** binds when the spec is authored — pinned repo state, prior decisions, schemas, house conventions. It is hashed into the bundle and is stable for the life of the binding.
- **Sensed context** binds when the action fires — a live reading of external state that could not be known at authoring time.

A domain's exposure to wind is measured by how much of its context is necessarily sensed. Code authoring over a frozen repo is nearly all frozen; a flow over live external state carries irreducibly sensed context. This is why the same apparatus produces a Level-4-reachable software system and a judgment-bounded live-flow system: the ratio of frozen to sensed context differs.

### Knowledge from outside the graph

Some decisions need knowledge that is neither in the graph nor in the model — current platform specifics, a specialist's read. The rule: **such knowledge enters only through the bundle, never through a live call inside the session that consumes it.** A live retrieval mid-session would make the output depend on something the bundle does not capture, breaking session replayability. It enters in one of two frozen forms, chosen by whether producing it is itself a judgment:

- When producing it *is* a decision ("does this architecture hold up against the platform's guidance?"), it is the output of a subject-matter-expert **role**, captured as a Domain Knowledge artifact with snapshot provenance (source, query, time, content hash).
- When it is a fact lookup with a single correct answer, the **bundle assembler** retrieves it at assembly time and freezes it in, hashed with everything else.

The deciding test is decision-content first: if a call is being made, it owes an artifact; if any two lookups would agree, it belongs in bundle assembly.

## The bundle: context made deliverable

**The bundle is the packaged, deliverable form of context** — an artifact in its own right, assembled from other artifacts. Where context is the abstract concept, the bundle is the concrete thing: the markdown document, the JSON blob, the file that goes into the role's input.

Bundles are **deterministically assembled** (same graph, same arguments, same bundle), have their own format and ordering rules, and are **measurable**: dimensions, size, density, token estimate, form profile. The bundle is the operationalized interface between the graph and the role — the actual, hashable object the [completeness exercise](../core/02-completeness.md) exercises against a pinned binding.

The unit of the exercise *is* the bundle: one prompt, one artifact type, assembled in dependency order, with its own model binding. One bundle, one binding, one completeness verdict. This is the point where the abstract "encoded store" of the law becomes a single, addressable, cacheable thing.

## SPMC: the four axes a bundle's quality rides on

A worker session's output quality depends on four independently-versioned axes, stamped on every session record so a quality drop can be triaged to the one axis that changed (see [SPMC](02-entities.md#spmc-schema-prompt-model-context)):

- **Schema** — what a good artifact *is*, owned by the role. A schema change moves the target, so it resets the quality baseline.
- **Prompt** — the *how*, the versioned execution guidance, one per `(role, artifact type)` cell.
- **Model** — the concrete, capability-tagged model behind the worker.
- **Context** — the deterministically-assembled, hashable bundle.

Hold three fixed, vary one, and any change in output quality is attributable to the axis that moved. This is what turns a model migration into a *measured swap* and a prompt revision into a *clean experiment*. SPMC is the encoded store, itemized into the four things you can actually version and pin.

## Phases: sequencing the graph

**A phase is a stage in the process with exit criteria** — a coarse-grained sequencing mechanism. Phases let the graph express "X must complete before Y" at a coarser grain than individual artifact dependencies. Each phase has artifacts (typically a set of features or their equivalent), exit criteria (artifacts that must pass), and a gate state (open/locked). The system enforces phase gates by refusing to surface phase-N+1 work while phase-N exit criteria are failing.

Phase exit criteria are a coarse-grained instance of the [ready predicate](02-entities.md#convergence-state): phase N cannot surface its successor's work until its focal artifacts are *done* and its phase-level artifacts are *ready*.

> A note on phases and the DAG. Phases are the pragmatic, human-legible sequencing layer. In the purest form of the graph, ordering is *derived* — a node runs once the artifacts it depends on are present and accepted — and the two convergence gates (ready, done) replace explicit phases entirely. Phases earn their keep where a team needs a coarse, nameable ordering to plan against; treat them as a convenience over the artifact-state machinery, not a separate primitive. The [notation](method/02-notation.md) deliberately omits a phase glyph for this reason.

## Task types: freezing recurring work into the catalog

The most consequential part of the encoding apparatus is the one that makes a system get *cheaper* over time rather than just bigger. It is the concrete form of [maturation](../core/04-projections.md#maturation-allocation-over-recurrence).

A unit of delivered work decomposes into three composition levels, forming a stability stack — dependencies point *down* the gradient, never up:

- **Cell** — one prompt, one artifact type, one model binding. The most stable layer; a prompt changes least. Depends on nothing above it.
- **Task** — a coherent sub-unit producing a *cluster* of related artifacts. Defined purely by its cell cluster and their ordering; composes cells but never reaches up into the delivered unit.
- **Delivered unit** — the value-anchored whole (a feature, a closed deal, a case). Composes tasks but never reaches down past a task into its cells.

This lets each layer's catalog stabilize without thrashing the layer beneath it.

**A TaskType is the registered, versioned definition of how a recurring task decomposes** — a catalog entry carrying:

- **The cell cluster** — which artifact types this task decomposes into.
- **The dependency order** — the edges among the cells (what must precede what, what runs in parallel). This is the task's own internal decision graph, declared once.
- **The prompt binding per cell** — which `(role, artifact type)` prompt fills each cell. Because one prompt is one decision kind, the cell cluster is also a set of decision kinds.
- **The coherence audit** — the cross-cell consistency the task requires (the cluster's artifacts must agree where they overlap).
- **A recognition signature** — what marks incoming work as being of this type, so a classifier can match it.

A TaskType is **born** through a frozen boundary, like all domain knowledge: typifying an exploratory build is a judgment call, so it is produced by an architect-as-SME role generalizing from the originating session into a TaskType artifact with provenance — never auto-derived from one example. It is **reused** mechanically: a classifier matches incoming work to a type, and dispatch instantiates the cluster, assembles bundles in order, binds the prompts, and runs the coherence audit. It is **evolved** on the meta-loop: a coherence audit that keeps failing means the decomposition is wrong, and the architect revises the type as a normal versioned change.

The known-type fraction — the share of incoming work that decomposes entirely into existing types — is the operational measure of architectural maturity. It climbs as the catalog fills and drops on entry to a new domain. That is the maturation curve, made into a dashboard number.

## How it fits together

The encoding apparatus is one pipeline from domain to dispatched work:

1. A domain's decisions are mapped ([the method](method/01-applying.md)) and each `(role, artifact type)` cell gets a **schema** (what) and a **prompt** (how).
2. Recurring cell clusters are frozen into **task types**, moving their generation decisions from live reasoning into the catalog.
3. For a given piece of work, **context** is assembled deterministically from the graph and packaged as a hashable **bundle**.
4. The bundle is exercised for [completeness](../core/02-completeness.md) against its pinned binding; a non-empty residual is a work order back onto the encoding.
5. **Phases** and the ready/done gates sequence the whole, and the [orchestration system](02-entities.md#system) dispatches each cell to a worker whose SPMC binding fits.

Every step is a place the encoded store grows and the judgment store shrinks — which is the [law](../core/01-the-law.md), running.

Next: [autonomy](04-autonomy.md) covers how a role graduates from human-checkpointed to autonomous as its measurement evidence accrues, and [conformance](05-conformance.md) covers the substrate capabilities all of the above requires.
