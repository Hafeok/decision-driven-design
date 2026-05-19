# Decision-Driven Design

A framework for building systems with LLMs.

## Premise: LLMs as forecasters

An LLM is a knowledge forecaster: given a context, it predicts what comes next. Humans work the same way. We reach decisions by forecasting from the knowledge we hold and the context we're operating in.

## Implication for work

A human work process is a chain of context-conditioned decisions. Roles (UXer, designer, PM, developer) are labels for context bundles plus authority to act on them. The decision is a forecast over the bundle.

## What organizations actually do

Organizations exist to perform value actions — the things that create value: shipping a product, closing a deal, treating a patient, publishing a paper. Every value action is preceded by a chain of decisions that determines whether, when, and how it happens. So the work to model is not the org chart and not the process flow, but the decision graph upstream of each value action. Map value-backwards: start from what the organization actually produces, and trace back through the decisions that had to occur for it to happen.

## The shift this enables

Most of the hard problems in knowledge work aren't automation problems — they're decision problems. Automation works when you already know what to build and just need to execute reliably. But the work of figuring out *what* to build, what's good, what's worth doing, who needs to weigh in — that's decisions, all the way down. Treating LLMs as forecasters lets us tackle that layer directly.

This is also why LLMs feel categorically different from prior automation. Industrial automation was good at the value action itself — the assembly, the transaction, the routing — and the upstream decisions were a human bottleneck the factory couldn't touch. In knowledge work the action and the decision often collapse into the same step ("send this email" is both), and the chain of decisions upstream is most of the work. Factory automation can't help with that because it can't decide. LLMs can.

## Contrast with the factory metaphor

The dominant AI-factory framing reaches for assembly lines and workstations: discrete tasks, deterministic flow, machines that execute. That metaphor fits when the answer is known and the goal is throughput. It fits poorly when the goal is to *decide*, because decisions are shaped by which context arrives and in what form — not by repeatable mechanical steps. The factory isn't wrong; it's just answering a different question.

## The alternative: a digital twin of the process

Map the real process — the roles, the decisions each role makes, and the artifacts that flow between them (briefs, specs, designs, reviews, tickets, decision records). Artifacts are not incidental; they are the medium by which context transfers between roles. Once the process and its artifacts are mapped, we have a digital twin: a structure we can simulate, with LLMs filling roles and producing the same artifacts a competent human would.

## The unit of work and the unit of composition

The unit of work is the decision. The unit of composition is the artifact. Decisions are private to a role — they're what the role does, internally, by forecasting over its context. Artifacts are how decisions cross role boundaries: a decision becomes an artifact (a spec, an ADR, a ticket, a review) the moment it needs to inform someone else's decision. Across boundaries, artifacts are the only thing that flows.

This makes the system composable. Stable artifact schemas — form, required fields, provenance, the model or human that produced it — are the interface contracts that let any role consume the output of any other, regardless of how that output was produced. Swap the reviewer's model; the spec it produces still slots into the same downstream graph. This is the same property that makes Unix pipes and microservice APIs work: composition follows interface stability.

The composition is a graph, not a pipeline. Multiple artifacts feed a single decision (an architect reads a spec, a constraint doc, and three prior ADRs); one decision spawns multiple artifacts (a design produces a mockup, a spec, and a list of open questions). Pipelines are the factory's geometry. DAGs are this system's.

Two disciplines keep the graph honest:

**Granularity.** You can trace decisions backwards forever, since every action presupposes a context that was itself decided. The natural stopping point is where decisions either become trivial (routine execution within an established frame) or get absorbed into a single role's standing authority. Below that line is execution; above it is the graph you're modeling.

**Value anchoring.** Every subgraph must terminate in a value action. That's what keeps the system from sprawling, and it's a useful audit: if you can't trace a decision back to a value action it eventually serves, either the map is wrong or the decision shouldn't exist.

## Context has a form

Written context — briefs, specs, decision logs, code, tickets — is LLMs' native medium and moves into them at near-zero loss. Visual context — sketches, mockups, layouts, the felt sense of a design — used to be a hard wall. Modern frontier multimodal models (Claude Opus 4.7 and peers) read images and design files with enough fidelity to participate in visually-driven roles. Smaller, cheaper models often don't, or do so poorly.

So form-of-context becomes a model-selection constraint per role: a role mediated by text-only artifacts has a wide menu of models; a role mediated by visual artifacts needs a frontier multimodal model, with the cost and latency tradeoffs that implies. Some visual artifacts (Figma component trees, prototype interactions, motion) carry meaning that a screenshot still misses, so even capable models may need a translation layer — annotated specs, structured tokens, design rationale.

When mapping the process, classify each artifact by its form. The form tells you which model can fill that role and how much engineering the handoff needs.

## Model selection is per-role

Form of context is one dimension; there are others. Some roles need deep reasoning over ambiguous, multi-source context (architectural calls, prioritization, design critiques); others make narrow, high-frequency judgments (classifying a ticket, drafting a routine reply, sanity-checking output). Some need vision, others don't. Some sit on a critical path with strict latency requirements; others run in batch and can spend more compute. Some are cost-sensitive at scale; others are rare and high-stakes.

The role-as-context-bundle framing extends naturally: the bundle dictates the model. A digital twin of a real process will typically use a mix — a frontier multimodal model for the design lead, a strong reasoning model for the architect, a fast cheap model for the triage step, perhaps a code-specialized model for the developer. Picking one model for the whole twin is the equivalent of staffing every role with the same person regardless of skill, seniority, or specialty. It works, but it leaves capability on the table and burns cost where it doesn't need to.

Treat model selection as a per-role design decision, not a deployment detail.

## Design principle

1. **Identify the value actions.** What does the organization actually produce that creates value.
2. **Trace backwards.** For each value action, what decisions had to happen for it to occur, and in what order.
3. **Map the roles and artifacts.** Each decision belongs to a role; each role consumes and produces artifacts. Artifacts are the interface.
4. **Classify artifact form.** Text, visual, structured, mixed — this constrains which models can fill the role.
5. **Choose a model per role** whose capabilities match the context shape and decision profile.
6. **Wire them up.** Feed each role its context, and let the artifacts flow.

## Why this works

- Existing processes already encode hard-won judgments about which context belongs where. We inherit that for free.
- Artifacts make context transfer concrete and inspectable. If a step fails, you can read what it had to work with — and what it didn't.
- Stable artifact schemas make the system composable. Roles can be swapped, models upgraded, branches added, without rewriting the graph.
- Value anchoring prevents sprawl. Every chain has to pay out in something the organization actually values.
- It gives an honest failure criterion. When an LLM step underperforms, the first question is "did it have the context a competent human in this role would have?" — not "is the model good enough?" Most of the time, the gap is contextual, and that's where the engineering is.
- It's honest about the problem. We're not building a faster assembly line. We're building a system that can decide.
