#!/usr/bin/env python3
"""G4 — the citation map: every wave-body bare row cites exactly one precedent.

Per the Gate 2 ruling: the map is COUNTED, never estimated; the P-18 fallback
count is reported; a row citing no precedent stops at the gate. Rows are keyed
by content (a distinctive substring of the row's anchor), never by position.

Actions:
  no-edit          — the cited precedent rules the sentence already correct
  edit             — re-expression executed this gate, wording in NEW
  edited-at-G3     — the row moved with the registry wave
  held-for-ruling  — P-01: the edit sits in hashed text; predicted, not taken
  P13-record       — filed decisions, dated notes, recorded rulings: never
  pin-quote-defers — quotes pinned canon verbatim; regenerates at the advance
"""

# (path fragment, anchor fragment, precedent, action)  — order matters only
# where two rows in one file share a fragment; fragments are chosen unique.
M = [
# ---- W2: upstream core/ (36) ----
('core/11', 'own prior output is not ground', 'P-03', 'no-edit'),
('core/11', '*Hold capacity `C_hold`**', 'P-04', 'no-edit'),
('core/11', 'in > context at once', 'P-04', 'no-edit'),
('core/11', 'does not fit. **Resolve-overflow** — >', 'P-05', 'edited-at-G3'),
('core/11', 'does not fit; the actor decides', 'P-05', 'edited-at-G3'),
('core/11', 'The ground is…', 'P-12', 'no-edit'),
('core/11', '**add** ground (retrieval)', 'P-07', 'no-edit'),
('core/11', 'can fail to constrain', 'P-06', 'no-edit'),
('core/11', 'statement is *output decouples', 'P-07', 'no-edit'),
('core/11', 'ground-failures*; the intuition', 'P-17', 'no-edit'),
('terms.yaml', 'attack surface. - id', 'P-02', 'no-edit'),
('terms.yaml', 'it can have in > context at once', 'P-04', 'no-edit'),
('terms.yaml', 'does not fit. **Resolve-overflow**', 'P-05', 'edited-at-G3'),
('core/00', 'establishes: [determination, decision, ground', 'P-08', 'no-edit'),
('core/00', 'the ground is the attack surface', 'P-02', 'no-edit'),
('core/08', 're-derive the same ground repeatedly', 'P-07', 'no-edit'),
('core/08', 're-derives the same ground at each level', 'P-07', 'no-edit'),
('core/09', 'from admissible ground', 'P-07', 'no-edit'),
('core/09', 'Replay over recorded ground', 'P-07', 'no-edit'),
('core/12', 'single-point authorship of ground', 'P-14', 'no-edit'),
('core/12', 'destruction of legitimate ground', 'P-14', 'no-edit'),
('core/03', 'dispersion of ground', 'P-19', 'no-edit'),
('core/10', 'applied per ground type', 'P-08', 'no-edit'),
('core/13', 'configuration and the ground, the resolution is determined', 'P-01', 'edit'),
('core/14', 'ground and judgment dependence', 'P-12', 'no-edit'),
('DDD-agent-01', "from the agent's ground", 'P-01', 'no-edit'),
('DDD-agent-01', 'Grounding the agent', 'P-01', 'no-edit'),
('DDD-agent-01', 'graph-grounded agents', 'P-01', 'no-edit'),
('DDD-frame-17', 'the ground together determine', 'P-01', 'edit'),
('DDD-frame-17', 'the ground jointly determine', 'P-01', 'held-for-ruling'),
('DDD-frame-17', 'determined by configuration and ground', 'P-13', 'P13-record'),
('DDD-frame-07', 'ground and judgment dependence', 'P-12', 'no-edit'),
('DDD-measure-15', 'from admissible ground', 'P-07', 'no-edit'),
('DDD-cost-05', 'simultaneously the ground', 'P-13', 'P13-record'),
('DDD-dec-26', 'Ground provenance — ruled ineligible', 'P-13', 'P13-record'),
('DDD-dec-30', 'configuration and ground together', 'P-13', 'P13-record'),

# ---- W3: apparatus/ (46) ----
('adversarial-ground', 'attack surface of any actor is its ground', 'P-02', 'no-edit'),
('adversarial-ground', "attacks the enemy's **ground**", 'P-07', 'no-edit'),
('adversarial-ground', 'behaves as benign ground', 'P-03', 'no-edit'),
('adversarial-ground', 'authorship of your ground.** You do not verify', 'P-14', 'no-edit'),
('adversarial-ground', 'attack surface of an actor is its ground. Hardening', 'P-02', 'no-edit'),
('adversarial-ground', 'deny single-point authorship of your ground', 'P-14', 'no-edit'),
('adversarial-ground', 'ground you do not control may be authored', 'P-06', 'no-edit'),
('adversarial-ground', 'genuinely uncontrolled *and* adversa', 'P-06', 'no-edit'),
('adversarial-ground', 'actor whose ground is immutable', 'P-06', 'no-edit'),
('adversarial-ground', 'the ground is not uncontrolled', 'P-06', 'no-edit'),
('tool-contract', 'the same ground-relation requirement', 'P-11', 'no-edit'),
('tool-contract', '## 1. Ground first', 'P-12', 'no-edit'),
('tool-contract', 'Tools act on ground', 'P-07', 'no-edit'),
('tool-contract', 'specify **ground** not at all', 'P-07', 'no-edit'),
('tool-contract', 'Capability without ground relation', 'P-11', 'no-edit'),
('tool-contract', 'Ground relation — per response', 'P-11', 'no-edit'),
('tool-contract', 'It *is* the ground', 'P-03', 'no-edit'),
('tool-contract', 'touch different ground under one name', 'P-07', 'no-edit'),
('tool-contract', 'the ground-exporter signature', 'P-17', 'no-edit'),
('tool-contract', 'whether that ground is > controlled', 'P-06', 'no-edit'),
('encode-verify', 'some ground is yours and some is not', 'P-14', 'no-edit'),
('encode-verify', 'price of the ground > being someone else', 'P-14', 'no-edit'),
('encode-verify', 'ground you corrupted by caching', 'P-06', 'no-edit'),
('the-skill-floor', 'input against *this* ground. In the store vocabulary', 'P-04', 'no-edit'),
('the-skill-floor', 'against *this* ground, and can **fail closed', 'P-04', 'no-edit'),
('the-skill-floor', 'as if it were ground', 'P-03', 'no-edit'),
('the-skill-floor', 'ground the author did not control', 'P-06', 'no-edit'),
('the-skill-floor', 'tool `ground` (`applications/sdlc`', 'P-15', 'no-edit'),
('the-skill-floor', 'failing closed on unreachable ground', 'P-06', 'no-edit'),
('tool-surfaces', '### Ground exporters', 'P-17', 'no-edit'),
('tool-surfaces', 'exports enormous ground', 'P-07', 'no-edit'),
('tool-surfaces', 'is a ground exporter, and its', 'P-17', 'no-edit'),
('tool-surfaces', '**Exports ground.**', 'P-07', 'no-edit'),
('tool-surfaces', '**Bounds the ground.**', 'P-07', 'no-edit'),
('tool-surfaces', 'a ground-scoping primitive', 'P-17', 'no-edit'),
('closure-principle', 'says what ground is **for**', 'P-03', 'no-edit'),
('closure-principle', 'where ground may **come from**', 'P-14', 'no-edit'),
('closure-principle', 'genuinely immutable *and* wholly con', 'P-06', 'no-edit'),
('closure-principle', 'satisfies the definition of ground completely', 'P-03', 'no-edit'),
('closure-principle', "the ground being someone else's", 'P-14', 'no-edit'),
('closure-principle', 'ground you do not > own', 'P-06', 'no-edit'),
('apparatus/README', 'own output is not ground', 'P-03', 'no-edit'),
('apparatus/README', 'attack surface of an actor is its ground', 'P-02', 'no-edit'),
('apparatus/README', 'ground first — a tool declares', 'P-12', 'no-edit'),
('prefix-stability', '(ground, a large corpus of settled decisions)', 'P-18', 'edit'),
('prefix-stability', '(ground → decisions → task)', 'P-16', 'no-edit'),

# ---- W3: downstream core/ (8) ----
('measure-routing-example', 'per ground type', 'P-16', 'no-edit'),
('measure-routing-example', 'ground type "code-synthesis"', 'P-16', 'no-edit'),
('measure-routing-example', '# visual ground', 'P-16', 'no-edit'),
('recon-cadence-demo', 'ground corruption rate', 'P-16', 'no-edit'),
('core/14-maturation', 'the verdict is new ground about', 'P-03', 'no-edit'),
('core/15', 'admission test applied per ground type', 'P-08', 'no-edit'),
('DDD-dec-27', 'Ground provenance — the ruling applied', 'P-13', 'P13-record'),
('DDD-dec-27', 'ground-provenance ineligibility ruling', 'P-13', 'P13-record'),

# ---- W3: papers (22) ----
('paper-a.md', '### 2.4 Ground provenance', 'P-12', 'no-edit'),
('paper-a.md', 'ed]. An act whose acceptance depends on', 'P-06', 'no-edit'),
('paper-a.md', 'ing: an act whose acceptance depends on', 'P-06', 'no-edit'),
('paper-a.md', 'relocate a ground property onto the actor', 'P-11', 'no-edit'),
('paper-a.md', 'usable as ground', 'P-03', 'no-edit'),
('paper-a.md', "this act's ground are given", 'P-04', 'no-edit'),
('paper-a.md', 'executed with the ground, time, memory', 'P-08', 'no-edit'),
('paper-a.md', 'ground no arrangement has', 'P-06', 'no-edit'),
('paper-a.md', 'ground the walk assumed missing', 'P-06', 'no-edit'),
('paper-a.md', 'ground and judgment dependence', 'P-12', 'no-edit'),
('paper-a.md', 'ground access, checker cost', 'P-11', 'no-edit'),
('paper-a.md', 'its ground by provenance', 'P-14', 'no-edit'),
('paper-a.md', "ground provenance (§2.4, this paper's", 'P-14', 'no-edit'),
('paper-a.md', 'ground decays over its own run', 'P-07', 'no-edit'),
('paper-a.md', 'soundness, ground completeness', 'P-11', 'no-edit'),
('paper-a.md', 'generation cost, ground access', 'P-11', 'no-edit'),
('paper-a-supplement', "claim nodes from the agent's ground", 'P-01', 'no-edit'),
('paper-a-supplement', 'Grounding the agent', 'P-01', 'no-edit'),
('response-to-review', "this act's ground* are both given", 'P-04', 'no-edit'),
('measure-note.md', 'computes* the verdict from ground', 'P-07', 'no-edit'),
('next-canon-session', 'computes the verdict from ground', 'P-07', 'no-edit'),
('reviewer-brief', 'ground access, feedback and accountability', 'P-11', 'no-edit'),

# ---- W3: projections (14) ----
('01-determination', 'answerable to has never been asse', 'P-07', 'no-edit'),
('01-determination', 'narrowest ground and a perfect record', 'P-09', 'edit'),
('01-determination', 'inherits its ground from whatever the pipeline', 'P-07', 'no-edit'),
('01-determination', 'has the least ground**, while', 'P-09', 'edit'),
('01-determination', 'the most ground and the least record', 'P-09', 'edit'),
('01-determination', 'give the program more ground', 'P-07', 'no-edit'),
('01-determination', 'Ground | observable — a stubbed handler', 'P-12', 'no-edit'),
('01-determination', 'none consulted — not the rate limit', 'P-12', 'no-edit'),
('01-determination', 'principal against stated ground', 'P-06', 'no-edit'),
('01-determination', 'no axis, no ground, no principal', 'P-08', 'no-edit'),
('01-determination', 'no ground exists for it', 'P-10', 'edit'),
('01-determination', 'the ground line says which', 'P-11', 'no-edit'),
('01-determination', 'has ground behind it and which does not', 'P-11', 'no-edit'),
('01-determination', 'ground is stated including the part', 'P-06', 'no-edit'),

# ---- W3: applications (5) ----
('production-as-ground', 'close over *substitute* ground', 'P-14', 'no-edit'),
('production-as-ground', 'tests against substitute ground', 'P-14', 'no-edit'),
('production-as-ground', 'make substitute ground adequate', 'P-14', 'no-edit'),
('production-as-ground', 'convert substitute ground into', 'P-14', 'no-edit'),
('applications/sdlc/README', 'close over substitute ground', 'P-14', 'no-edit'),
]

# The edits, by content anchor -> replacement (executed with Edit, recorded here)
NEW = {
 'configuration and the ground, the resolution is determined':
   'core/13: "given the standing configuration and the ground at the act, the resolution is determined or it is not" (P-01 alignment to DDD-frame-17\'s statement form)',
 'the ground together determine':
   'DDD-frame-17 falsifier: "whether the standing configuration and the ground at the act together determine the resolution" (P-01; unhashed field, fires nothing)',
 '(ground, a large corpus of settled decisions)':
   'prefix-stability: "(delivered ground, a large corpus of settled decisions)" (P-18)',
 'narrowest ground and a perfect record':
   '01-determination: "the narrowest ground available to it and a perfect record" (P-09)',
 'has the least ground**, while':
   '01-determination: "has the least ground available to it**, while" (P-09)',
 'the most ground and the least record':
   '01-determination: "the most ground available and the least record" (P-09)',
 'no ground exists for it':
   '01-determination: "asserted, never measured — no ground is available for it" (P-10)',
}

if __name__ == '__main__':
    import json, os, collections
    HERE = os.path.dirname(os.path.abspath(__file__))
    led = json.load(open(os.path.join(HERE, 'g1-head-ledger.json')))
    AREAS = {'up-core','dn-apparatus','dn-core','dn-papers','dn-projections','dn-applications'}
    def area(r):
        p=r['path']
        if r['repo']=='upstream': return 'up-core' if p.startswith('core/') else 'up-other'
        for pre,a in (('apparatus/','dn-apparatus'),('core/','dn-core'),('papers/','dn-papers'),
                      ('projections/','dn-projections'),('applications/','dn-applications'),
                      ('meta/','dn-meta')):
            if p.startswith(pre): return a
        return 'dn-other'
    body=[r for r in led if r.get('bare') and area(r) in AREAS]
    used=[0]*len(M); out=[]; orphans=[]
    for r in body:
        hits=[i for i,(pf,af,prec,act) in enumerate(M)
              if pf in r['path'] and af in r['anchor']]
        if len(hits)==1:
            i=hits[0]; used[i]+=1
            out.append({'path':r['path'],'anchor':r['anchor'],'precedent':M[i][2],'action':M[i][3]})
        else:
            orphans.append((r['path'], r['anchor'], len(hits)))
    print(f'wave-body bare rows: {len(body)}; mapped 1:1: {len(out)}; orphans/ambiguous: {len(orphans)}')
    for o in orphans: print('  ??', o)
    unused=[(M[i][0],M[i][1]) for i,u in enumerate(used) if u==0]
    multi=[(M[i][0],M[i][1],u) for i,u in enumerate(used) if u>1]
    if unused: print('unused entries:', unused)
    if multi: print('multi-matched entries:', multi)
    c=collections.Counter((d['precedent'],d['action']) for d in out)
    print('\nper-precedent counts:')
    for k,v in sorted(c.items()): print(f'  {k[0]:>5} {k[1]:<16} {v}')
    print('P-18 fallback count:', sum(v for (p,a),v in c.items() if p=='P-18'))
    json.dump(out, open(os.path.join(HERE,'g4-citation-map.json'),'w'), indent=1)
