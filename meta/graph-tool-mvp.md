# Graph tool — MVP sketch

**Status:** parked until paper 1 ships. Scope: an afternoon. Anything that does not fit in an
afternoon belongs to the full tool (`DDD-tool-01`) and waits.

**Principle.** The MVP adds no behaviour the convention does not already have — it mechanises grep.
Claims stay markdown; manifests stay front-matter; the only executable is CI.

**Post-split note.** The `core/09` and `core/assets/measure-*.py` this sketch reproduces are canon in
the principle repository now (`actor-indexed-determination`); a reproduce-and-diff CI job for them runs
there. Here, `graph/upstream.yaml` + `validate-core-order.py` check that the pins this repo depends on
still resolve at the pinned ref.

---

## 1. Claims file

`core/claims.md` — one entry per claim node:

```markdown
## DDD-measure-01
- **status:** established (v4.5)
- **claim:** On the closing region, specification demand is verdict entropy; conservation is the chain rule.
- **evidence:** core/09; assets/measure-toy.py, measure-actor-allocation.py, measure-rag.py
- **falsifier:** reproduction failure of any listed asset → demote to reported pending fix
- **changed:** v4.5
```

Convention `DDD-<area>-<n>`. IDs never reused; retired claims keep theirs.

## 2. Projection manifest

YAML front-matter on each projection's context file:

```yaml
projection: measure-paper
source_version: v4.4
claims: [DDD-measure-01, DDD-measure-02, DDD-boundary-01]
audience: academic
status_floor: projected
rendered: 2026-07-26
```

## 3. CI job

Two checks, both trivially scriptable:

1. **Reproduce.** Run every `core/assets/measure-*.py`; diff output against the values stated in
   `core/09`. Mismatch → fail the build and print the demotion: which claim, which asset.
2. **Staleness.** For each manifest, compare `source_version` against the `changed` field of every
   listed claim. Any claim newer than the pin → warn with the projection name and the claim ID.
   Warn, not fail: staleness opens a re-render/annotate/let-stand decision for the principal; it is
   not itself an error.

Attribution: CI log records script, canon version, commit, run date. Principal for demotions: Emil.

## 4. Explicitly out of MVP scope

- Watcher-actors running falsifiers on dependency change.
- Any parsing of claim *content*; the MVP reads only metadata.
- Escalation routing, dashboards, graph visualisation.
- Non-uniform actor capabilities. All of this is `DDD-tool-01` and is parked.

## 5. First real exercise

The tool's shakedown is the arXiv feedback cycle on paper 1: if review changes any claim, the
staleness check should name every affected projection without anyone re-reading them. If it does,
`DDD-tool-01` earns its build; if manual audit is still needed, that is the falsifier firing early
and cheaply.
