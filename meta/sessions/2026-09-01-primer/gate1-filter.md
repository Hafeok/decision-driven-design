# Gate 1 — the filter and the survivor set

*draft-pending-ruling*

## Arrival

- `actor-indexed-determination`: tag `v5.13.0` found and verified — it points at `5c7fe46`,
  which is exactly the head of the default branch. Nothing has landed past the tag.
- `decision-driven-design`: head at `fc4a81b` (the ground-migration-exec merge).
- Validators, fresh runs: `validate-core-order.py core/` exits 0 with zero W4 (66 warnings, all
  W1/W2-class); upstream `validate-claims.py` exits 0 with 32 warnings; downstream with 6; both
  decision runs clean. The warning counts equal the `v5.11.0` baseline recorded in CLAUDE.md —
  nothing new, nothing silently cleared.
- Every asset cited by a claim at `reported` reproduces on a fresh run: `measure-mdl-demo`,
  `floor-mechanism`, `perr-rate-distortion`, `measure-toy`, `measure-actor-allocation`,
  `measure-nonuniform-ground`, `measure-chained-seams`, `measure-rag` (upstream) and
  `measure-mdl-volume` (downstream). No demotion is triggered by reproduction failure.

## The filter

89 claims across both repos: 4 `established`, 11 `reported`, 70 `projected`, 4 `retired`.

### `established` — four claims, all `formal` (the anchor holds)

| id | kind | statement (gist) |
|---|---|---|
| DDD-frame-06 | formal | closure is distinct from generation cost |
| DDD-measure-02 | formal | conservation on the closing region is the chain rule: H(V) = I(V;X) + H(V|X) |
| DDD-measure-10 | formal | H(V|S) = 0 requires I(V;S) = H(V) — no decomposing out of the work |
| DDD-measure-16 | formal | the construction is available exactly where the predicate closes for the arrangement |

Exactly the four `spec/claim-format.md` §5 names. Nothing empirical, conceptual or normative has
reached `established`; nothing downstream has reached it at all.

### `reported` — eleven claims

| id | repo | kind | evidence shape |
|---|---|---|---|
| DDD-cost-02 | up | formal | asset (mdl-demo) |
| DDD-floor-01 | up | formal | derivation + two assets |
| DDD-measure-03 | up | formal | asset (toy) |
| DDD-measure-04 | up | formal | asset (actor-allocation) |
| DDD-measure-05 | up | empirical | asset (rag, 40k samples) |
| DDD-measure-09 | up | conceptual | asset (toy) |
| DDD-measure-11 | up | conceptual | **derivation only — no asset** |
| DDD-measure-12 | up | conceptual | derivation + asset (nonuniform-ground) |
| DDD-measure-13 | up | formal | **derivation only — no asset** |
| DDD-measure-14 | up | formal | derivation + asset (chained-seams) |
| DDD-cost-06 | down | formal | asset (mdl-volume) |

### `retired` — four, provenance filed

frame-09 (`retired_from: unrecoverable`), frame-15 (`projected`), measure-06 (`established`),
measure-08 (`unrecoverable`). All four carry the correction that killed them; none deleted.

## The survivor set against the prediction

The prediction was ten mechanics. The graph's answer, mechanic by mechanic:

1. **The two primitives.** Canonical terms (`term:determinable`, `term:determinate`, established
   by `00-primitives.md`). Claim-side: DDD-frame-13, DDD-ground-05 — conceptual, `projected`.
2. **The act as unit of account, one verdict at a declared boundary.** Terms (`term:act`,
   `term:act-individuation`, `term:verdict`). Claim-side: DDD-frame-12, DDD-frame-16,
   DDD-cost-01 — all `projected`.
3. **The four stores and their timing.** `term:store`; the model itself (DDD-frame-03) and the
   timing vocabulary (DDD-ground-03) are `projected`. One facet survives higher: DDD-measure-04
   (`reported`, formal) — store allocation is actor-relative while total demand is invariant.
4. **The admission test with tolerance.** `term:admission-test`, `term:tolerance`
   (`00-primitives.md`); the applicability gate is DDD-ground-01 — normative, `projected`. No
   claim at `established` or `reported` carries it.
5. **Acceptance predicate and operational closure.** Survives at the top: DDD-frame-06 and
   DDD-measure-16, both `established`.
6. **The floor located in the predicate.** Split. The formal mechanism — escape = overflow ∩
   open, p_err from rate-distortion — is DDD-floor-01, `reported`, assets reproducing. The
   relational reading (floor as property of the indexed tuple, not the task) is DDD-floor-02,
   conceptual, `projected`; so is DDD-measure-17 (domain coincidence).
7. **Escape as supply-general with its generators.** `projected` throughout: DDD-delivery-02
   (filed-but-undelivered is escape, supply-general), DDD-frame-04 (escape predicts ungoverned
   failure), DDD-cost-16 (escape is doubly costly). Only floor-01's formal intersection is
   `reported`.
8. **Standing versus occasioned supply.** The distinction itself (DDD-cost-01, conceptual) is
   `projected`; its formal consequences are `reported` — DDD-cost-02 (degeneracy) and
   DDD-cost-06 (volume corollary, the one downstream survivor).
9. **Delivery, and that filing is not encoding.** Entirely `projected`: DDD-delivery-01 (filing
   is not encoding), -02, -03 upstream, DDD-delivery-04 downstream — all conceptual.
10. **Demand as verdict entropy where the predicate closes.** The richest survivor, with a
    load-bearing shape: the identification itself (DDD-measure-01, empirical) is `projected`;
    what is `established` is the conditional arithmetic (measure-02, -10) and the availability
    condition (measure-16); `reported` carries the seam identity, actor-invariance, the
    estimated-channel run, and the scope claims (measure-03/-04/-05/-09/-11/-12/-13/-14).

**Where the graph disagrees with the prediction.** Roughly half the predicted list survives at
`established`/`reported`, and only in its formal aspect: closure, the measure's arithmetic and
scope, the floor's mechanism, store-allocation invariance, the cost degeneracy. The other half —
the primitives, the act, the admission test, escape's generators, delivery and
filing-is-not-encoding — is carried either as canonical vocabulary (terms have no status to
survive with) or as claims at `projected`. The practitioner-central mechanics of §2, §3 and §5
(filing, delivery, escape-finding) rest on `projected` conceptual claims, which under the
standing note do not enter the procedures as claims. The consistent pattern: **every mechanic's
formal skeleton outranks its modelling reading** — which is §5's own kind/status separation
doing its job, and it will shape how the primer may teach (definition and procedure from the
terms and the normative decisions; assertion only where the status carries it).

## Statuses that look wrong on their own evidence

Reported, not fixed; any repair is a canon session's act.

1. **DDD-measure-11** (conceptual, `reported`). §5 defines `reported` as "at least one evidence
   entry whose asset reproduces". Its two evidence entries are both derivations; it cites no
   asset. On its own evidence it is `projected` (falsifier declared, unmet) — or it needs the
   asset its status presupposes.
2. **DDD-measure-13** (formal, `reported`). Same defect — derivation evidence only, no asset —
   plus the sharper edge: its falsifier line reads "none — arithmetic given the chain rule;
   fires with DDD-measure-01", the exact pattern of measure-02 and measure-10, which sit at
   `established`. Its own evidence matches `established` (unchallenged derivation) or
   `projected`; it matches `reported` least of the three.

Checked and found principled, not wrong: the five `projected` claims that carry reproducing
assets (cost-03, cost-04, cost-07, cost-29, measure-15) — each asset note states it exercises
the computation and "does not and cannot confirm the correspondence", so withholding `reported`
is deliberate. The falsifier-strict warnings on measure-09 and measure-12 are inside the ruled
baseline and both carry reproducing assets; nothing to add.

## One pin observation, for Gate 2

`graph/upstream.yaml` pins the downstream repo at `v5.12.0`; this session reads canon at
`v5.13.0`. The primer must carry a pin in its own text. Whether it pins the repo's `v5.12.0` or
the session's `v5.13.0` — and whether a pin-advance decision precedes it — is a question for the
outline gate, not for this filter. Advancing the pin is a governed decision and out of this
session's scope to file.
