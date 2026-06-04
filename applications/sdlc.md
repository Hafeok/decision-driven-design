# Application: the software development lifecycle

> **Status: projected.** This is a clean derivation of DDD applied to code generation, not yet a reported result from a running system. The reference implementation (product-cli) is being built against it. Read it as a design, and weight the open questions accordingly.
>
> Relies on framework concepts defined in the spec: [Task and TaskType](../docs/02-entity-reference.md#task), [the maturation curve](../docs/01-foundations.md#the-funnel-over-time-maturation), [the funnel](../docs/01-foundations.md#the-funnel-model-capability-tracks-constraint-density), [Decision and the two graphs](../docs/01-foundations.md#two-graphs-artifacts-and-decisions), and [SPMC](../docs/02-entity-reference.md#spmc-schema-prompt-model-context). This doc applies them; it does not re-derive them.

---

## The practice this replaces

The standard shape of LLM code generation is a harness — Claude Code or similar — handed a feature and a tool belt and steered toward a goal. One worker, broad authority, a long agentic loop, and human steering when it drifts. It is good at what it is good at: holding a whole problem in one context and adapting on the fly.

In DDD terms that harness is *one role making many kinds of decision in one session* — infrastructure, API shape, test strategy, error-handling, naming, all fused. That is the fusion the one-prompt-one-artifact-type rule forbids: the session's decision graph is a black box, and when the output is wrong you cannot tell whether the infrastructure reasoning or the test strategy was at fault, because they were never separated. It is a muddied decision graph hiding inside a single worker.

DDD says code is an artifact like any other — schema, producing session, subject-matter decisions, a place in both graphs. Once code is an artifact, a unit of implementation is not one artifact but a cluster of typed artifacts, each its own `(role, artifact type)` cell with its own prompt, generation decisions, and model binding. The single steered agent decomposes into a small graph of single-purpose generators.

## The three levels, in this domain

The framework's [composition levels](../docs/02-entity-reference.md#task) land in the SDLC as:

- **Feature** — the value-anchored unit; the terminal value action is `shipped feature`.
- **Task** — the typed unit. SDLC task types: *add-an-entity*, *expose-a-CRUD-API*, *add-an-auth-rule*, *wire-a-migration*. Each owns a cell cluster.
- **Cell** — one prompt, one artifact: the bicep, the API contract, the handler, the test cases.

A CRUD-API task decomposes into a cluster like {contract, handler, integration tests, IaC route}; an add-entity task into {model class, migration, unit tests}; a pure refactor into {impl, tests} with no contract or IaC. The cluster is a property of the task type, declared once.

The [Stable Dependency stack](../docs/02-entity-reference.md#task) is concrete here: the handler prompt (cell) changes least; the CRUD-API task type composes cells and never reaches up into a feature; the feature composes task types and never reaches into a cell. Standardizing the CRUD-API task type cannot break the handler prompt beneath it.

## Where the cell boundaries fall

The only hard design question is where to split, and the framework's crossing test answers it: **a boundary exists where a sub-artifact crosses to inform a different downstream decision.**

- **API contract** → a cell. The test generator, the handler generator, and any client consumer all read it.
- **Test cases** → a cell. The gate/verifier consumes them independently of the code.
- **IaC** → a cell. Deployment consumes it; it has its own domain decisions (regions, sizing, tagging).
- **Variable naming inside one function** → not a cell. It crosses nothing; it is absorbed into the handler generator's standing authority. This is the granularity floor.

Over-split and you pay coordination cost for no gain; under-split and the black box returns. "Implementation" as a single role dissolves into a value-action cluster of roles — contract designer, handler implementer, test author, IaC author — all serving one terminal value action, so they are modules within the Engineering system, not new systems. product-cli already owns feature/ADR/TC/dep artifacts; this says the *code* it produces is similarly typed, not monolithic.

## The funnel, inside one feature

The cells sit at different points on the [funnel](../docs/01-foundations.md#the-funnel-model-capability-tracks-constraint-density). The API contract is upstream — it sets constraints, the hard problem-domain calls concentrate there, it may want a strong reasoning model. The handler is downstream of it — the contract pinned the hard calls, so a small code-specialized model translates a well-specified problem into a known idiom. The IaC is further down still. Model binding follows the funnel inside the implementation, and the funnel discipline applies as a forcing function: if the handler cell needs a frontier model, the first question is not "is the model good enough" but "did the contract pin the calls it should have." Under-specification surfaces as model-size escalation in a named cell.

## Classify and dispatch, at the task level

The cluster path works only when a task's type is recognized, so classification sits at the task level. A feature is processed by decomposing it into tasks first, then routing each:

- **Known task type** → dispatch its cell cluster: instantiate the cells, assemble bundles in the declared `derived_from` order, bind the prompts, run the coherence audit. Mechanical, cheap, walkable.
- **Unknown task type** → a broad worker, with a specific job: one-shot the task, or explore it and emit a new TaskType for the catalog.

A feature is almost never wholly unknown — it is mostly known tasks plus maybe one novel one. The known tasks dispatch their clusters; the novel task goes to the broad worker; if its breakdown generalizes it is folded back as a new task type. The mixed feature is the normal case, not an edge case.

```
   feature --> decompose into tasks -->  task1   task2   task3 ...
                                           |       |       |
                            +--------------+--+    |    +--+---------------+
                            v                 |    v    |                  v
                   classify: known type?   (known) (known)      classify: known type?
                       known | unknown                              known | unknown
                  +----------+---------+                       ... mostly known ...
                  v                    v
        +--------------------+  +---------------------------+
        | dispatch cluster:  |  | broad worker              |
        | contract->handler->|  | - one-shot the task, OR   |
        | tests, IaC ||      |  | - explore + mint a NEW    |
        | (walkable)         |  |   TaskType                |
        +---------^----------+  +-------------+-------------+
                  +----- new TaskType registered <---------+
```

**The broad path feeds the typed path.** The broad worker is the explorer-and-typifier; when it builds something genuinely new, its most valuable output is not the code but the discovery of a task type that can be dispatched cheaply forever after. This is the principled standing of the broad-authority coding agent (opencode/aider as a node, not rejected like the orchestration frameworks): it owns the unknown. The classifier needs a "not confident → broad worker" escape hatch, which means the broad path is also the low-confidence path, not only the unknown-type path.

## Maturation toward standard tasks

This domain is the clearest instance of the [maturation curve](../docs/01-foundations.md#the-funnel-over-time-maturation). Early on, few task types exist; most tasks are unknown and go to a broad worker or human; each run mints types. As the catalog fills, features increasingly decompose into known tasks and the broad worker retires from the common ones. At maturity, "the architecture supports 80% of new features" means 80% of incoming features decompose entirely into known task types — and that 80% is exactly the [type-decomposability fitness function](../docs/02-entity-reference.md#fitness-function).

"The set of standard tasks we do every time" is the SDLC's name for the task-type catalog reaching a fixpoint. A standard task is a task type with high eligibility, high autonomy, a stable cluster, and a coherence audit that hasn't fired in a long time. The descent to small models tracks this: early work is big-model/human-heavy, mature work runs the 80% on small code-specialized models because the constraint now lives in the catalog, not the model's reasoning.

![Maturation curve](../docs/assets/maturation.svg)

## The costs this decomposition introduces

Real, and worth designing for rather than discovering.

1. **Ordering is explicit — and it's just `derived_from`.** Contract before handler before tests; IaC parallel. Declared once in the TaskType; the orchestration system assembles bundles in that order instead of an agent steering a loop.

2. **Cross-cell consistency becomes an explicit audit.** One agent's shared context made the endpoint, the route, and the test path agree for free. Split across cells they can drift. The fix is the shared upstream artifact (the contract) plus a named coherence audit owned by the task type. **This is the load-bearing audit of the whole pattern — worth prototyping first.** If it is weaker than what a single context gave for free, the decomposition is worse than the monolith.

3. **Emergent decisions cost a round-trip.** The handler surfaces a problem the contract didn't anticipate. The monolith fixes it inline; here it is `gap`/`unimplementable` feedback flowing up to the contract cell, which re-opens and re-converges. Better for auditability, slower than inline. Right for a high-autonomy ready→done chain; maybe wrong for spike work — the standing argument for keeping the broad worker available as one node.

## Open questions specific to this application

- **Recognition is the soft spot, at two levels** — matching a task to a TaskType, and a feature to a feature-type-shaped decomposition. Signature by schema shape, embedding similarity, or an explicit field the requester sets? Misclassification dispatches a confidently-wrong cluster, so the escape hatch matters.
- **Task-type granularity.** Too many narrow types and recognition is hopeless; too few and clusters are vague. Likely coarse, parameterized types (CRUD-API with/without auth, with/without async) over proliferation.
- **Decomposition quality is its own measurement.** A feature→task breakdown can be wrong independently of the tasks being right — correct tasks that don't compose into the intended feature. The decomposer role needs measurement separate from cell-level quality.
- **The coherence audit's teeth** are the thing to validate before trusting any decomposition. Prototype it first.
