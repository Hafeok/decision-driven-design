# core/

**This repository is the software projection.** The actor-general theory layer — the numbered core
documents `00`–`11`, the canonical term graph, and the reproduction assets — is **canon in the
principle repository** (`actor-indexed-determination`) and lives there, not here. This directory holds
only what is local to the projection's own graph:

- `claims/` — the projection-local claims (`org`, `tool`, `sim`). Actor-general claims are pinned
  upstream in `graph/upstream.yaml`.
- `decisions/` — the program's decision nodes (`DDD-dec-01..07`), including the split decisions.
  Decisions are volitional program acts; they live with the projection, not upstream.

The principle repo's canon is consumed by pin, not by copy: `graph/upstream.yaml` names every upstream
id this repository depends on, at a version and a status, and `validate-core-order.py` checks them
against a shallow clone of the pinned ref (basis-loss detection — `DDD-agent-01` applied to repos).
