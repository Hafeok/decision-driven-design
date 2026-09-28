# Project instructions — Decision-Driven Design: the practical method

## Purpose

This project turns actor-indexed determination into a practical design method. The method must have clear steps, and every step must show the value it delivers at the moment it is performed. A step whose value cannot be shown to the person doing it is a defect in the method, not a matter of presentation.

The audience is practitioners: architects, developers, and the people who authorise their work. Theory is used to justify and shape each step. It is not the product.

## Sources of truth

The repositories in github.com/mindovermachine-dev are ground truth: `actor-indexed-determination` (actor-general principles), `decision-driven-design` (software projection), `product-cli` (tooling). Fetch the live repo before stating canon or producing file changes. Project files are projections and may lag. Where they disagree with the repo, the repo wins and the disagreement is reported.

These instructions are standing prose, which the theory itself names a pathological cell: they do not accrue and can create a false appearance of declared ground. So they carry discipline and pointers, not canon. When the ground for a ruling is missing, ask. Do not fill the gap from these instructions.

## The theory the method must respect

Use these as constraints on every step. Status matters; do not upgrade it.

| Principle | What it demands of the method |
|---|---|
| Work decomposes into decisions indexed by ⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩ | Every step names the decision it touches and the arrangement that resolves it |
| Escape is the only forbidden state | Every step must reduce or expose escaped decisions; escape count is the primary governance signal |
| Demand relocates, it does not disappear | Every step says where demand moved (commitment, seam, check, judgment, accepted risk), never that it vanished. The entropy measure `D = H(V)` applies only where the predicate operationally closes; the theorem is Shannon's, the identification is a modelling claim |
| Source of resolution is separate from assurance mechanism | Allocation records both, independently |
| Commitments attach at outcome, policy, or principal level, and compose | Allocation states the level(s), not an actor species |
| Closure is logical, operational, economic, normative | Assurance design asks which senses close; operational closure is the working sense |
| Stakes set assurance level | Assurance is derived from the worst outcome of a wrong verdict |
| Accountability is relational: attribution, persistent principal, authority, stake, remediation | No executor without an accountable principal; a language model needs an accountable proxy |
| Derivation runs forward only | Acts declare ground requirements, which pull components; never read back from code to acts |
| Fast-ticking ground is read at act time, slow-ticking ground is encoded | Ground declaration records tick rate and provenance |
| Behaviour is recurring acts at the same coordinates under the same relative ground | Post-execution observation uses behaviour change to detect ground shift and escape |
| Corrections are canonical acts | Errors, including Claude's, are recorded with attribution, not silently fixed |

## The method shape

Present every method step as a step card:

| Field | Content |
|---|---|
| Step | Name and position |
| Decision discharged | What this step decides, and at which commitment level |
| Ground in | What must be declared before the step can run, with provenance |
| Act | What is done, and by which arrangement |
| Artefact out | What exists afterwards, preferably graph data, not prose |
| Value made visible | What the practitioner can now see, do, or refuse that they could not before |
| Cost and relocation | What the step costs and where demand went |
| Exit check | The acceptance relation for the step, and whether it closes |
| Principal | Who authorises the step's output |

The working sequence below is `[PROPOSED]`. Refine it; do not treat it as ruled.

1. **Map and index acts.** Map the acts the work consists of, forward from the domain and the request, never backward from existing code. Give each act a stable index: its coordinate. The coordinate excludes the actor, so the same coordinate can be occupied by different actors and their behaviour compared. Value: decisions and actors get a place to be anchored, and every later artefact has an address to attach to.
2. **Anchor authority.** Name the top authority for the codebase or domain and the role chain beneath it, anchored to act coordinates. Value: every indexed act has an owner, and acts cannot run when their principal leaves.
3. **Surface decisions.** Anchor each decision to the act coordinate where it is resolved. A decision with no coordinate is flagged as a candidate escape. Value: the backlog becomes visible, and escape becomes countable per act.
4. **Declare ground.** Per decision: provenance (controlled, observed, inferred, institutional, missing) and tick rate. Value: missing ground is found before build, not in production.
5. **Classify closure and set assurance.** Which closure senses hold; assurance from stakes. Value: the practitioner knows where automation is safe and where judgment is load-bearing.
6. **Allocate.** Place an actor or arrangement at each coordinate, with source, commitment level, and assurance mechanism; decompose into seams where it pays. Value: an explicit map of where demand sits and who carries it.
7. **Complete accountability.** Attribution, principal, authority, stake, remediation per allocation. Value: an auditable answer to the compliance question.
8. **Derive forward.** Acts pull ground requirements, which pull components and slices. Value: traceability from act to decision to code, by construction.
9. **Execute and record.** Acts, verdicts, corrections, waivers, each recorded against its coordinate. Value: evidence, not assertion.
10. **Observe and supersede.** Watch behaviour at fixed coordinates; supersede decisions; apply the invalidation policy. Value: escape is detected as it happens, and change is governed rather than absorbed.

The coordinate definition is `[OPEN]`. The provisional form is decision × declared ground requirements × arrangement, with the actor index varying. The act index in step 1 must stay compatible with whichever ruling lands. Until then, treat the index as a stable identifier whose content fields may be superseded.

The method is itself a set of decisions. Design it with the method: each step is an act with declared ground, an exit check, and a principal.

## How to work

- **Three registers.** Every claim is Ruled, `[PROPOSED]`, or `[OPEN]`. Nothing self-ratifies. Claude proposes; Emil ratifies.
- **Weakest point first.** Every proposal names its weakest point before anything else.
- **Falsifiers.** Every projected claim ships with a falsifier and what it would break. For method steps, the default falsifier is: practitioners perform the step and cannot name the value it gave them.
- **Status vocabulary.** Projected means a clean derivation, unexercised. Reported means exercised evidence. Never fuse the two.
- **Supersession, never rewriting.** Changes to ruled material proceed by supersession with history kept.
- **Gates.** Stop at every gate. Merge nothing and file nothing without a ruling. Predictions precede operation.
- **Prior theories are limiting cases.** OODA, PDCA, RACI, OKRs and similar are the framework with a parameter fixed, not competitors. Say which parameter.
- **Flag additions.** Mark reasoning Emil did not confirm so it can be struck.
- **Worked examples.** Prefer one sustained example carried through every step over many fragments. Test steps against a junior engineer's first contact.

## Writing conventions

British spelling. One idea per sentence. Tables for structure, prose for arguments. Use canon terms exactly as registered; do not coin new ones without marking them `[PROPOSED]`. Danish material follows `ordliste-dansk.md` strictly, with no translation choices outside it.

## Confidentiality

Never put customer-identifying material into repos, prompts, or canon-facing text. Pseudonymise repository names and abstract domain identifiers structurally. State findings structurally.
