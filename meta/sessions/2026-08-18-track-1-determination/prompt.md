# Session: Track 1 — Determination, for software engineers

*The session prompt, verbatim as received. Committed before Gate 1 per `meta/sessions/README.md`.*

---

## Scope
Draft the first learning track: a single ordered path of ten rungs teaching the
determination vocabulary through one worked decision. Nothing else. Reject
bundling — no path generator, no ActorClass axis, no Diátaxis restructuring, no
website work. Those are separate sessions.

## Ground state — fetch before proposing anything
Read, do not assume:
- upstream `Hafeok/actor-indexed-determination`: `core/`, `graph/terms.yaml`,
  `graph/axis-registry.yaml`
- downstream `Hafeok/decision-driven-design`: `core/13-delivery.md`, the DAD
  way-of-working document, `docs/g-track/` for filing conventions
- both validators: `validate-core-order.py`, `validate-claims.py`

Report the current tags of both repos at Gate 0 before writing.

## Split
- **Upstream** — any new or amended term needed by rungs 1–9 (determinable /
  determinate, axis, ground provenance, arrangement, commitment level, residual
  discretion, escaped decision). Amend existing canon by supersession only;
  never rewrite ratified text.
- **Downstream** — the track document itself and rung 10 (ledger discharge).
- One branch per repo. Upstream PR first; downstream pin bumped on acceptance.

## The content
Worked decision, unchanged across all ten rungs: **how many times do we retry a
failed outbound call?**

Ten rungs, in this order:
1. Determinable / determinate — `3` is not a decision; `retry-count` is the axis
2. What makes it a decision — declared, outcome-relevant, governed at a chosen
   abstraction and tolerance
3. Ground and its provenance — controlled, observed, inferred, institutional,
   missing
4. Actor and arrangement — same axis, three resolvers; the unit of comparison is
   the arrangement, not the component
5. Commitment level — program/outcome, LLM/policy, engineer/principal
6. Residual discretion — and why zero variance is not correctness
7. Acceptance and closure — operationally closed against a test suite, open
   against peak-load behaviour
8. Assurance is not source — identical escape risk if neither is checked
9. Escaped decision — `3` was the HTTP client's default; no axis, no ground, no
   principal, governs production anyway
10. Discharge — the learner records one real act: axis, value, ground, α,
    principal

Three actors run throughout: a program, an LLM, an on-call engineer. Primary
audience is software engineers; assume C#/.NET fluency and no framework
vocabulary.

## Prohibitions
- **Do not cite `H(V)`, entropy, or the measure anywhere in this track.** "Learn
  DDD" has no verdict function; the predicate does not close and the measure is
  silent there. Rung 5→9 teaches conservation as felt, not measured. A citation
  here would be the exact overreach the measure paper's §6 exists to prevent.
- Do not present rungs 1–9 as establishing competence. They supply capability
  only; capability is the entry fee. Stake starts at rung 10.
- Do not derive pedagogical order from canon dependency order. It is a declared,
  judgement-mediated decision with an owner. Deriving it is presumed discharge.

## Constraints to satisfy
- Rung order must be a linear extension of the canon dependency partial order.
  State the check; propose a validator instrument only if it costs nothing.
- Rung 10 must name a principal and a declared α, or it is not a discharge.
- Every substantive claim carries a pre-registered falsifier. Track-level
  falsifier to draft: *if learners completing rungs 1–9 without owning the rung
  10 act perform equivalently on later judgement-mediated acts, the pairing is
  decoration.*

## Discipline
- All additions marked `[PROPOSED]`. Emil merges and ratifies; this session
  proposes.
- Substantive changes stop at a gate for ratification. Editorial changes proceed.
- British spelling. Sentences carry one idea. Tables for structures, prose for
  arguments.
- No customer-identifying material. Examples stay structural.
- Commit this prompt to `meta/sessions/` before Gate 1.
- Commit drafts to the feature branches before reporting at each gate.

## Gates
- **Gate 0** — repo state, tags, and the proposed file paths for both repos.
- **Gate 1** — upstream term deltas only. Stop.
- **Gate 2** — rungs 1–5 drafted. Stop.
- **Gate 3** — rungs 6–10, the falsifier, and the linear-extension check. Stop.
- **Gate 4** — validators run clean, PRs opened upstream-first.

## Open, flag do not resolve
- Whether the retry example survives contact with the juniors, or whether a
  business-line domain example is stronger. Emil is gathering feedback.
- Whether rung 7 (closure) belongs before rung 5 (commitment level), since
  closure arguably conditions which commitment levels are available at all.
