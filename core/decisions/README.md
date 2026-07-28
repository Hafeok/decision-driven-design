# core/decisions/

Decision nodes: one YAML file per decision, `DDD-dec-NN.yaml`, per the ontology in
`meta/graph-tool-ontology.md` §2. A decision is **volitional** — made by a principal in
order to act — and is the framework's original primitive; a claim is **epistemic**. The
load-bearing edge is `decision --basedOn--> claim` (`basis:`).

These are the decisions settled in the graph-scaffolding session, landed rather than
re-invented (`meta/graph-tool-ontology.md` §7 recommends backfilling the research repo's
own decisions as day-one seed data). Emil is the accountable principal on all three.

**A decision is not falsifiable — it is superseded or revisited.** Each carries a
`reviewTrigger`; a basis claim changing is always one (`meta/graph-tool-ontology.md` §4,
rule 2).

**Basis status, noted for Emil.** All three rest on `DDD-tool-01` (projected), and
`DDD-dec-02`/`DDD-dec-03` also on `DDD-measure-01` / `DDD-org-02` (both projected;
`DDD-org-02` is additionally flagged session-authored). Per ontology rule 1 the status
floor scales with commitment level: these are `policy`-level commitments resting on
projected bases. That is accepted risk under a named principal (Emil), not invisible risk
— recorded here so it stays auditable, and a candidate for Emil to confirm or to raise the
required floor.

**Validate:** `python3 scripts/validate-claims.py core/decisions/ --decisions`
