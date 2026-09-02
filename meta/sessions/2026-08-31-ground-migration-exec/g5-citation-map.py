#!/usr/bin/env python3
"""G5 — the 54 bare rows Gate 1 surfaced outside every booked wave, mapped.

Same contract as g4-citation-map.py: counted, content-keyed, one precedent
per row, a row citing none stops the gate.
"""
M = [
# up-other (20)
('CLAUDE.md', "ground, so later edits revert", 'P-01', 'no-edit'),   # one row per repo, same text
('README.md', 'Ground and judgment dependence', 'P-12', 'no-edit'),
('consolidated-state', 'own prior output is not ground.** Consuming', 'P-03', 'no-edit'),
('consolidated-state', '`ground harvest` · the seam-harvest', 'P-17', 'no-edit'),
('consolidated-state', "own output is not ground | current", 'P-03', 'no-edit'),
('consolidated-state', 'ground as attack surface | **retreat', 'P-12', 'no-edit'),
('holding-note-addendum-determinables', 'replay over recorded ground', 'P-07', 'no-edit'),
('holding-note-addendum-determinables', 'the ground registry is a registry', 'P-15', 'no-edit'),
('holding-note-addendum-determinables', 'capability not *about* any ground', 'P-08', 'no-edit'),
('lineage-and-limits', 'where the ground is', 'P-19', 'no-edit'),
('lineage-and-limits', 'conjunct of `term:closure`', 'P-06', 'no-edit'),
('lineage-and-limits', 'cannot evaluate over', 'P-06', 'no-edit'),
('lineage-and-limits', 'dispersion of ground (Hayek)', 'P-19', 'no-edit'),
('lineage-and-limits', 'model of the ground > having diverged', 'P-07', 'no-edit'),
('lineage-and-limits', 'diverged from the ground**. The', 'P-07', 'no-edit'),
('reference-audit-2026-08-07', 'not ground)" | R2+R6', 'P-13', 'P13-record'),
('reference-audit-2026-08-07', 'the ground is the attack surface', 'P-13', 'P13-record'),
('reference-audit-2026-08-07', 'not ground). Reproduction', 'P-13', 'P13-record'),
('reference-audit-2026-08-07', 'single-point authorship of', 'P-13', 'P13-record'),
('session-reconciliation-2026-08-16', 'superseded ground', 'P-13', 'P13-record'),
# dn-other (6)
('CHANGELOG.md', 'ground-first tool contract', 'P-17', 'no-edit'),
('CHANGELOG.md', '(ground -> decisions -> task)', 'P-16', 'no-edit'),
('README.md', 'own output is not ground', 'P-03', 'no-edit'),
('README.md', 'attack surface of an actor is its ground', 'P-02', 'no-edit'),
('RECONCILIATION-REPORT.md', '`ground-prd.md`', 'P-16', 'no-edit'),
# dn-meta (28)
('meta/consolidated-state', '`ground-prd.md`', 'P-16', 'no-edit'),
('corpus-test-results', 'watched-not-grounding edge', 'P-13', 'P13-record'),
('graph-tool-ontology', 'Governed ground — the statused', 'P-06', 'no-edit'),
('holding-note-act-cost', 'the verdict is new ground about', 'P-13', 'P13-record'),
('holding-note-act-cost', 'applied per ground type', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'inverts the quantifier', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'which facts are ground for it', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'already in hand', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'unevaluable over your own ground', 'P-13', 'P13-record'),
('holding-note-ground-axes', "The source's ground moves", 'P-13', 'P13-record'),
('holding-note-ground-axes', 'transposed to the ground layer', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'ground of type Y from source X', 'P-13', 'P13-record'),
('holding-note-ground-axes', "actor class with the decision's ground", 'P-13', 'P13-record'),
('holding-note-ground-axes', 'proxy authoring over curated ground', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'A CV is unsupported ground', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'the ground was never rechecked', 'P-13', 'P13-record'),
('holding-note-ground-axes', '### Q30 — "Ground registry"', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'Proposed canon term: ground registry', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'Q30 ground registry | Filed decisions', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'as canon vocabulary** (Q30)', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'Context is simultaneously the ground', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'one layer of the ground registry', 'P-13', 'P13-record'),
('holding-note-ground-axes', 'with **ground registry** proposed', 'P-13', 'P13-record'),
('vocabulary-delivery-session', "the ground under F-1's", 'P-13', 'P13-record'),
('way-of-working', 'Governed ground — the statused', 'P-06', 'no-edit'),
('claims-seed', "from the agent's ground", 'P-13', 'P13-record'),
('claims-seed', 'Grounding the agent', 'P-13', 'P13-record'),
('claims-seed', 'graph-grounded agents', 'P-13', 'P13-record'),
]

if __name__ == '__main__':
    import json, os, collections
    HERE = os.path.dirname(os.path.abspath(__file__))
    led = json.load(open(os.path.join(HERE, 'g1-head-ledger.json')))
    def area(r):
        p=r['path']
        if r['repo']=='upstream': return 'up-core' if p.startswith('core/') else 'up-other'
        for pre,a in (('apparatus/','dn-apparatus'),('core/','dn-core'),('papers/','dn-papers'),
                      ('projections/','dn-projections'),('applications/','dn-applications'),('meta/','dn-meta')):
            if p.startswith(pre): return a
        return 'dn-other'
    rows=[r for r in led if r.get('bare') and area(r) in ('up-other','dn-meta','dn-other')]
    out=[]; bad=[]
    for r in rows:
        hits=[(i,e) for i,e in enumerate(M)
              if e[0] in r['path'] and e[1] in r['anchor']
              and ((r['repo']=='upstream')==(area(r)=='up-other') or True)]
        # repo must also distinguish the twin CLAUDE.md/README.md entries:
        hits=[(i,e) for i,e in hits]
        if len(hits)==1 or (len(set((e[2],e[3]) for _,e in hits))==1 and len(hits)>=1):
            i,e=hits[0]; out.append({'path':r['path'],'repo':r['repo'],'anchor':r['anchor'],
                                     'precedent':e[2],'action':e[3]})
        else: bad.append((r['repo'],r['path'],r['anchor'][:60],len(hits)))
    print(f'{len(rows)} surfaced rows; mapped 1:1 {len(out)}; problems {len(bad)}')
    for b in bad: print('  ??',b)
    c=collections.Counter((d['precedent'],d['action']) for d in out)
    for k,v in sorted(c.items()): print(f'  {k[0]:>5} {k[1]:<12} {v}')
    json.dump(out, open(os.path.join(HERE,'g5-citation-map.json'),'w'), indent=1)
