# DDD Applied: The Autonomy Ladder

> **Apparatus §4 — informative.** How the apparatus maps to the standard 0–5 autonomy ladder, why per-role autonomy is the unit, and why the ceiling of any role is the measured [Polanyi floor](../core/03-the-polanyi-floor.md) of its task type, never an assertion. Not required for conformance; supplied for readers already thinking in autonomy levels.
>
> Borrowed terms (DAG, DMN, RDF, MCP, OCI, …) — see [Glossary](glossary.md).

How the architecture maps to the standard autonomy framework, what each level looks like in DDD terms, and why DDD is the structure that makes Levels 4 and 5 actually achievable rather than aspirational.

## The framework

The five-level autonomy framework, descended from SAE J3016 and adapted to AI:

- **Level 0.** No AI. All work is human.
- **Level 1.** Assistance. AI suggests; humans decide and act.
- **Level 2.** Partial automation. AI handles specific bounded tasks; humans supervise and own most of the work.
- **Level 3.** Conditional automation. AI handles most work; humans intervene at defined checkpoints or on escalation.
- **Level 4.** Autonomous. AI handles all work within a defined operating domain; humans intervene only by exception, on signals the AI itself surfaces.
- **Level 5.** Fully autonomous. AI handles all work across all operating domains, including the meta-work of defining and improving the domains themselves.

The framework is useful as a destination grammar — it gives organizations a way to talk about where they are and where they want to be. It is less useful as a how-to. Knowing you want to reach Level 4 doesn't tell you what infrastructure makes Level 4 possible.

DDD is the answer to the how. The mapping reveals that the framework's discipline is exactly what's needed to traverse the levels cleanly.

## The fundamental shift: autonomy is per-role, not per-system

The standard framing treats autonomy as a property of "the AI system." A self-driving car is at Level 3 or Level 4 as a whole. A customer support bot is fully autonomous or it isn't.

DDD reframes this. The unit of autonomy is the role, not the system. A single process can have some roles at Level 4 (fully autonomous), some at Level 3 (human-checkpointed), and some at Level 2 (AI-assisted, human-owned). The whole-system level is the floor, not a uniform setting.

This matches how organizations actually work. An organization doesn't need to make its architect role autonomous before it can make its implementer role autonomous. Different decisions have different stakes, different feedback loops, different fit profiles. Treating autonomy as per-role lets each role graduate when its measurement evidence supports it, independent of other roles in the same process.

The architecture supports this naturally. The role catalog declares each role; the orchestration system's policy declarations bind each role to a model or a human. Promoting a role from human-filled to AI-filled is a one-line policy change with a measurement audit trail. Demoting it back, when evidence supports the move, is symmetric.

The system's autonomy level at any moment is determined by its highest-level role's floor — if any role still requires human input, the system is at most at the level the most-supervised role allows. But the path to higher levels is per-role progress, accumulated over time.

## Level-by-level mapping

### Level 0: Manual

No AI involvement. No DDD needed. Humans fill every role; coordination happens through whatever the organization's existing practices are. The framework is overkill here because the discipline DDD enforces — typed artifacts, measured sessions, audited handoffs — is mostly invisible value to humans coordinating informally.

This is most organizations' starting point. DDD's value proposition begins to appear when even one role is considered for automation.

### Level 1: Assistance

AI suggests; humans decide and act. An IDE autocomplete. A drafting assistant. A research summarizer. The AI is a tool the human uses while filling their role; it doesn't fill the role itself.

DDD is largely invisible at this level. The artifacts the human produces are the same artifacts they would produce without the AI assistance. No role assignments change, no measurements accumulate at the role-fit level, no policy decisions about model selection. The single-interface principle is trivially satisfied because there's only one population (humans) filling roles.

The one place DDD provides value at Level 1: if the organization is building toward higher levels, structuring the work as decision-graphs-with-artifacts now means later promotion is mechanical. An organization at Level 1 with no structure has to build the structure before promoting. An organization at Level 1 with DDD discipline already has the structure; promotion is a policy change.

### Level 2: Partial automation

AI fills specific bounded roles under human supervision. Triage classification. Routine drafting. Standardized handoffs. The roles are narrow, well-framed, and low-stakes; AI output is consumed by humans who can readily catch issues.

DDD starts paying off here. The framework's value at Level 2:

**Role typing makes the boundary explicit.** "AI fills the triager role; humans fill everything else" is a declaration in the role catalog, not a fuzzy practice. When AI output is bad, the failure mode is locatable: triager session N produced this output from this bundle.

**The single interface is now load-bearing.** Humans downstream of AI-filled roles consume the same artifacts they would consume from human-filled roles. No translation. No parallel paths. The human reviewing a triager's classification reads the same artifact format the triager produced.

**Measurement starts.** Sessions accumulate measurements from the first AI-filled role. The first "is this binding correct" evaluations become meaningful.

Most current "AI in workflow" deployments live here. The risk at this level is sprawling AI surface area without the structure to keep it auditable. DDD provides the structure.

### Level 3: Conditional automation

AI fills most roles; humans intervene at defined checkpoints. The architect produces ADRs but a human reviews and approves before they're accepted. The test designer produces test plans but a human verifies coverage. The gatekeeper produces verdicts but a human signs off on high-risk releases.

This is DDD's natural operating point. Every architectural choice in the design supports it:

**The checkpoint mechanism is first-class.** Roles configured with `requires_human_approval` route to humans via the same dispatch path that routes to models. The bundle the human consumes is identical. The verdict artifact they produce is identical. The orchestration system doesn't know whether a model or a human filled the role; it just sees the role completed.

**Measurement evaluates fit per role at this level specifically.** The question "is this AI-filled role ready to lose its human checkpoint" is the central question at Level 3, and the measurement infrastructure exists to answer it empirically. Trend analysis on quality, downstream rejection, amendment rate — these tell you when a checkpointed role's AI output is good enough to advance to autonomous.

**The action-interpretation pattern protects against runaway actions.** Every action session pairs with an interpretation session, often human-checkpointed. The system can't barrel ahead with bad actions because the interpretation gate is structural, not policy.

**Feedback flows let humans surface AI failures structurally.** When a human checkpoint catches a bad AI output, they produce a feedback artifact. That feedback routes to the appropriate upstream system, becomes input to policy decisions, drives binding changes. Human supervision at Level 3 isn't just gatekeeping — it's a feedback signal that drives the architecture's improvement.

Most organizations should aim to live here for an extended period before considering higher levels. Level 3 captures most of the productivity gains while keeping the audit and improvement loops human-anchored.

### Level 4: Autonomous in defined domain

AI fills all roles within a bounded process; humans intervene only on signals the AI surfaces. The orchestration system's escalation policies define the boundary: this set of conditions warrants human attention; everything else proceeds without.

DDD's full architecture is what makes Level 4 reachable. The pieces that matter:

**The orchestration system makes the boundary explicit.** "Autonomous in defined domain" requires the domain to be defined. The orchestration system's policy declarations — role-to-filler bindings, escalation triggers, capacity limits — are the explicit definition. Outside the declared boundary, the orchestration system escalates rather than acting.

**Measurement-driven binding decisions replace human checkpoints with confident bindings.** A role that has run thousands of sessions with consistent quality, low downstream rejection, and stable performance graduates from human-checkpointed to autonomously bound. The graduation is evidence-based and reversible.

**Self-surfacing failure modes.** Audit infrastructure (preflight, gap, drift) and measurement infrastructure (fitness functions, action-interpretation agreement) generate escalation signals automatically. When the system is operating outside its competence, the audits surface it before downstream consequences accumulate. Human attention is allocated to the moments the system itself flags as warranted.

**The feedback loop closes.** Operations feeds back to Engineering; Validation feeds back to Engineering and Discovery; rejected artifacts route back to producers. The architecture's behavior at Level 4 isn't "AI does everything statically" — it's "AI does everything and the architecture improves itself from operational experience."

Reaching Level 4 with DDD looks like the end-state of the implementation plan: all five process plug-ins running, orchestration handling routing, measurement driving binding decisions, humans intervening only on flagged escalations. The "defined domain" is the bounded set of work the plug-ins cover — software development from request to production deployment, end-to-end, with the architecture's discipline making it auditable.

### Level 5: Fully autonomous

AI fills all roles across all operating domains, including the meta-work of defining and improving the domains. Level 5 in DDD terms isn't "no humans anywhere" — humans can remain as a population that fills certain roles for reasons unrelated to capability (governance, accountability, choice). Level 5 is the architecture handling all process work autonomously, including the work of evolving the process itself.

The DDD constructs that enable this:

**The policy owner role becomes AI-filled.** At Level 4, policy decisions (which model for which role, what thresholds, what escalation triggers) are typically human-owned because they shape the system's behavior. At Level 5, the policy owner role is itself filled by AI, consuming measurement evidence and producing policy update artifacts. The orchestration system uses its own audits to validate policy changes.

**Cross-process composition becomes autonomous.** New processes can be added — a new plug-in registers, the orchestration system integrates it into the routing graph, the platform begins driving it — without human intervention. The plug-in itself is built by humans (or eventually by other AI systems), but its integration is automatic.

**The framework refines itself through measurement.** Aggregate patterns across all systems reveal structural issues — feedback class incidences suggest role catalog gaps, bundle size distributions suggest decomposition threshold changes, model performance drift suggests rebindings. At Level 5, these patterns trigger architectural changes autonomously rather than requiring human decisions.

This is the framework applied recursively to itself: decisions about the framework's operation are decisions, with their own audit, measurement, and improvement loops.

Reaching Level 5 requires Level 4 first. The path from 4 to 5 is not a phase in the implementation plan; it is the natural evolution that happens as Level 4 operation accumulates measurement evidence and the architecture demonstrates that its own meta-decisions can be trusted to AI fills. Some organizations may never reach Level 5 by choice — keeping humans in the policy-owner role can be a deliberate governance decision, not a capability gap.

## How the implementation phases map

The phases from the build plan correspond to levels in a non-uniform way.

**Phase 0 (infrastructure).** No autonomy level. The infrastructure exists; nothing runs through it yet.

**Phase 1 (Engineering plug-in).** Level 2 for software development. Some Engineering roles can be AI-filled with human supervision. Validation is external; humans fill validation roles. The system is partially automated within a narrow scope.

**Phase 2 (Validation plug-in).** Level 3 for the dev+validation chain. Most roles are AI-fillable with explicit human checkpoints at architectural reviews and ship verdicts. The first complete cross-system flow runs under conditional automation.

**Phase 3 (Operations plug-in).** Still Level 3, but now with feedback loops. The system can learn from production behavior even though humans are still gatekeeping high-stakes decisions.

**Phase 4 (Discovery plug-in).** Approaching Level 4. With Discovery, the full upstream exists. Many Discovery roles are still human-heavy at this phase, but the architecture supports promoting them as measurement evidence accumulates.

**Phase 5 (Release plug-in).** Level 4 achievable end-to-end. Release decisions can be human-checkpointed (Level 3) or autonomous-with-escalation (Level 4) depending on stakes. The full architecture exists; the level achieved is a policy choice per role.

**Beyond Phase 5.** Level 5 evolution. Measurement-driven binding changes graduate roles from human-checkpointed to autonomous. The policy owner role itself can graduate. Cross-process plug-ins can be added autonomously. The architecture's discipline applies to itself.

The implementation plan reaches Level 4 capability. Reaching Level 5 is not more building; it is using what was built, accumulating evidence, and graduating roles based on that evidence.

## Why DDD is the structure for Levels 4 and 5

Most attempts at autonomous AI jump straight to Level 5 ambitions — "an agent that does everything" — and fail because they lack the structure to make autonomy bounded, auditable, and improvable. The failure modes are predictable: opaque decision-making, ungovernable behavior, no way to localize failures, no mechanism for graduating capability.

DDD addresses each failure mode structurally.

**Bounded autonomy.** The orchestration system's policy declarations make the boundary of "defined domain" explicit. Outside the boundary, escalation. Inside, autonomous operation. Level 4 requires this boundary; DDD provides it.

**Auditable autonomy.** Every session is recorded. Every artifact has provenance. Every routing decision is itself an artifact. When autonomous operation produces a bad outcome, the audit trail explains what happened and why. Level 4 requires this auditability; DDD provides it.

**Improvable autonomy.** Measurement infrastructure makes role-model fit empirically evaluable. Policy decisions consume measurement evidence. The system improves through structured feedback rather than ad-hoc tweaking. Level 4 sustainability requires this; Level 5 requires this loop to apply recursively to policy itself. DDD provides both.

**Localized failure.** When the autonomous system fails, the failure is locatable to a specific role, in a specific system, with a specific session record showing the bundle and the output. Recovery is bounded: route the failure to a human, route around the bad role, retrain or rebind. Without the structural localization, failure modes are systemic and unrecoverable.

These are not accidents. The framework was designed for this — decisions as the unit, artifacts as the composition, value actions as the terminus. The same discipline that makes individual decisions auditable makes autonomous operation governable.

## What this clarifies about DDD's positioning

Three things this mapping makes precise.

**DDD is the substrate for autonomy, not autonomy itself.** The framework does not "make AI autonomous." It provides the structural conditions under which autonomy is achievable and governable. An organization deploying DDD doesn't automatically operate at Level 4; they have the infrastructure to reach Level 4 if their measurement evidence supports it for the roles in question.

**The traversal through levels is gradient, not stepped.** Per-role autonomy means a system can be at Level 3 overall while specific roles operate at Level 4 and others at Level 2. The level is the floor, not a uniform setting. Organizations move through the levels by graduating roles, not by flipping switches.

**Level 4 is the realistic destination for most organizations.** Level 5 is an end-state that some processes may reach but that requires organizational tolerance for fully-autonomous policy decisions. Many high-stakes domains (finance, healthcare, regulated industries) will deliberately stay at Level 4 with human policy ownership — not because Level 5 is technically infeasible but because governance considerations argue for keeping certain checkpoints human-anchored.

The framework supports this nuance. DDD doesn't push toward Level 5; it supports each organization's chosen operating point and provides the infrastructure to operate cleanly at whichever level they target.

## Summary

The five autonomy levels map cleanly to DDD constructs:

- Level 0-1 don't require DDD (humans own all decisions or AI is merely advisory).
- Level 2 begins to benefit from DDD's role typing and single interface as AI fills bounded roles.
- Level 3 is DDD's natural operating point — most roles AI-filled with explicit human checkpoints, measurement evaluating per-role fit, feedback loops driving improvement.
- Level 4 is the destination the implementation plan reaches — bounded autonomy with escalation-based human involvement, the full architecture operating.
- Level 5 is evolution beyond the plan — measurement-driven policy decisions, recursive application of the framework's discipline to its own operation.

The unit of autonomy is the role. The level of the system is the floor. Graduating roles based on measurement evidence is how organizations move up the levels deliberately and reversibly.

DDD is what makes Levels 4 and 5 actually achievable rather than aspirational. Without the framework's discipline, "autonomous AI" tends to mean opaque, unbounded, unauditable agent loops that fail in ways no one can diagnose. With DDD, autonomous operation is structurally constrained, continuously measured, and improvable through the same mechanisms that produced it.

The framework's design choices — decisions as the unit, artifacts as the composition, value actions as the terminus, single interface for humans and LLMs, system bounded by process, per-role model selection, audit at multiple layers, feedback as a flow class — all converge on this property. DDD is the autonomy substrate. The levels are the destinations it supports.
