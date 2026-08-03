# migration/ — repo split execution bundle

Everything the kickoff prompt requires, landed on the execution branch. Contents:

| File | Role |
|---|---|
| `core-contracts.md` | The core reorder: per-doc ddd:contract blocks, reorder map, "what old 00 loses" ledger |
| `validate-core-order.py` | Ordering + transclusion checker. Reads `core/graph/*.yaml` registries AND per-claim `core/claims/*.yaml` files carrying `canonical_md` (format 2) |
| `graph/terms.yaml` | Seed term registry — extend to every `establishes` entry during step 4 |
| `spec-addendum-claim-format-2.md` | Additive claim-format bump enabling claims as embed sources; all format-1 claims valid unchanged |
| `decisions/DDD-dec-04..06.yaml` | The split decisions, drafted in the live decision format with real basis ids. **Filing them is Emil's act** — land into `core/decisions/` only on his explicit authorisation |

Gates before execution (both verified by the agent, neither performable by it):
1. DDD-dec-04..06 present in `core/decisions/`
2. Measure note shipped, recorded in CHANGELOG or consolidated-state (per DDD-dec-06)

Corrections vs the v1 package: pin examples now use live ids (`DDD-floor-01`,
`DDD-measure-01`, `term:closure`); decision YAML uses the repo's actual schema
(question/resolution/commitmentLevel/basis/assurance/principal/made/reviewTrigger);
claims embed from `core/claims/` per-claim files, not a parallel registry.
The placement table and pinning semantics (E12/E13/W5) in `repo-split-package.md` §2–3
stand, with ids read as corrected here.
