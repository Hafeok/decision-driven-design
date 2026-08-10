# core/

**This repository is the software projection.** The actor-general theory layer — the numbered core
documents `00`–`12`, the canonical term graph, and the per-act reproduction assets — is **canon in
the principle repository** (`actor-indexed-determination`) and lives there, not here. This directory
holds what is local to the projection's own graph:

- `13-cost-projection.md` — the projection's numbered core documents, numbered to continue the
  upstream reading order (upstream canon ends at `core/12`). `13` is the volume layer of the cost
  register: everything that quantifies over act volume, filed here under the boundary charter
  (upstream `DDD-dec-09`; `DDD-dec-10` here) — the principle layer is synchronic, and anything
  requiring persistence between acts files with the projection.
- `claims/` — the projection-local claims (`org`, `tool`, `sim`) and the volume-denominated `cost`
  claims (`DDD-cost-04` relocated, `DDD-cost-06`/`07` split from the upstream per-act claims).
  Actor-general claims are pinned upstream in `graph/upstream.yaml`.
- `decisions/` — the program's decision nodes (`DDD-dec-01..07`, `DDD-dec-10`), including the split
  decisions. Decisions are volitional program acts; they live with the projection, not upstream.
- `graph/terms.yaml` — terms established by this repository's own documents (`act-volume`).
  Upstream terms are never duplicated here.
- `assets/` — computations backing this repository's reported claims (`measure-mdl-volume.py`);
  they must reproduce.

The principle repo's canon is consumed by pin, not by copy: `graph/upstream.yaml` names every upstream
id this repository depends on, at a version and a status, and `validate-core-order.py` checks them
against a shallow clone of the pinned ref (basis-loss detection — `DDD-agent-01` applied to repos).
Pinned upstream ids satisfy `requires`/`ref` edges in local documents: upstream precedes every local
document in the reading order, so the cross-repo edge points backward by construction.
