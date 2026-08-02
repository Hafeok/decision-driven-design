# core/claims/

The claim graph as files: one YAML file per claim node, `DDD-<area>-<nn>.yaml`, each declaring
`format: 1` per `spec/claim-format.md`. Until the graph tool exists these files **are** the graph
and grep is the query engine (`meta/way-of-working.md` §2).

Canon authority for a converted claim lives here, not in the prose it was extracted from. Where a
`core/` document and its claim disagree, the disagreement is a bug in the prose — flagged in the
claim's `notes:`, not silently harmonised (`meta/conversion-protocol.md`).

**Provenance.** These claims were split from `meta/seed/claims-seed.yaml`, which was drafted from
projections pinned at v4.4/v4.5 and then verified against live canon in this branch. The
verification outcomes — verified, restatused, struck, or flagged — are recorded per claim in
`notes:` and in the branch commit history.

**Areas:** `measure`, `frame` (actor-indexed determination), `floor`, `tool`, `org`, `agent`,
`sim`. New areas are cheap; renumbering is forbidden; retired claims keep their IDs.

**Flags awaiting Emil review.** Claims whose `notes:` carry `UNVERIFIED` could not be confirmed
from repo contents — either Paper A / foundation-revision material not yet in `core/`
(`frame-01`, `frame-02`, `frame-07`) or session-authored predictions in the parked areas
(`org-*`, `agent-01`, `sim-*`). They are flagged, never struck, and never presented as canon.

**Validate:** `python3 scripts/validate-claims.py core/claims/`
