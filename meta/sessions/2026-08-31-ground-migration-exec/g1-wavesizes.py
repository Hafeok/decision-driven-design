#!/usr/bin/env python3
"""G1 — the corrected wave sizes, computed at head.

Builds the head working ledger: every head row carries either the sense the
execution-grade classification gave its baseline counterpart (matched by
content), a proposed sense from g1-added-rulings.py (draft-pending-ruling),
or an explicit UNRULED bucket (audit output, session records, release
descriptors, downstream meta gained since the classification — counted,
listed, not ruled here). Then counts, per SR-7: counted, never estimated.
"""
import os, sys, json, collections, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-','_'),
                                                  os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m
g1 = load('g1-reconcile')
gb = load('g1-bare')
added = load('g1-added-rulings').R

base = json.load(open(os.path.join(HERE,'..','2026-08-24-ground-audit','classification.json')))
senses = json.load(open(os.path.join(HERE,'..','2026-08-27-ground-migration','w0-full-v2.json')))
for i, r in enumerate(base): r['sense'] = senses[str(i)]
head = json.load(open(os.path.join(HERE,'g1-head-extract.json')))

b2h, rem_b, add_h = g1.match(base, head)
pair = {('downstream','papers/paper-a/paper-a.md'),
        ('downstream','papers/paper-a/paper-a-supplement.md')}
moved = {}
for width in (240, 80, 32):
    anchors = collections.defaultdict(list)
    for j in add_h:
        r = head[j]
        if (r['repo'], r['path']) in pair:
            anchors[(r['token'], g1.window(r, width))].append(j)
    still = []
    for i in rem_b:
        r = base[i]
        if (r['repo'], r['path']) in pair and i not in moved:
            a = (r['token'], g1.window(r, width))
            if anchors[a]:
                j = anchors[a].pop(0); moved[i] = j; add_h.remove(j); continue
        still.append(i)
    rem_b = still

for i, j in b2h.items(): head[j]['sense'] = base[i]['sense']
for i, j in moved.items(): head[j]['sense'] = base[i]['sense']

unruled = collections.Counter(); misses = []
for j in add_h:
    r = head[j]
    # Among the anchors this context contains, take the one lying closest to
    # the token itself — neighbouring occurrences share 240-char contexts, so
    # containment alone can hand a row its neighbour's ruling.
    hit, best = None, 10**9
    for (repo, path, anchor), (sense, why) in added.items():
        if r['repo'] == repo and r['path'] == path:
            at = r['ctx'].find(anchor)
            if at >= 0:
                dist = abs((at + len(anchor)//2) - r['tok_off'])
                if dist < best:
                    hit, best = sense, dist
    if hit:
        r['sense'] = hit; r['proposed'] = True
    else:
        r['sense'] = None
        if r['immutable']:                       unruled['immutable (A9/B13)'] += 1
        elif r['path'].startswith('meta/'):      unruled[f"{r['repo']} meta, unruled"] += 1
        else:
            unruled['live, missing a proposed ruling'] += 1
            misses.append((r['repo'], r['path'], r['line']))

top = lambda s: s.split('-')[0] if s else 'unruled'
print('=== head totals (2,845-row classification carried by content + proposed rulings)')
for k, v in sorted(collections.Counter(top(r['sense']) for r in head).items()):
    print(f'  {k:>8} {v:>5}')
print('  unruled buckets:', dict(unruled))
if misses: print('  MISSING RULINGS:', misses[:10])

live = [r for r in head if r['sense']]
mut = [r for r in live if not r['immutable']]
print('\n=== W1 (S5 -> deployment distribution)')
s5 = [r for r in mut if top(r['sense']) == 'S5']
s5x = [r for r in s5 if r['repo'] != 'product-cli']
gen = [r for r in s5x if 'appendix row' in dict(added).get((r['repo'],r['path'],''),('',''))[1]]
per = collections.Counter((r['repo'], r['path']) for r in s5x)
print(f'  mutable S5 excl product-cli: {len(s5x)} (corpus-wide mutable {len(s5)})')
for k, n in per.most_common(): print(f'    {n:>3}  {k[0]}:{k[1]}')

print('\n=== S2/S3 prose population at head (canon+projection, mutable, non-ident)')
pop = [r for r in live if top(r['sense']) in ('S2','S3') and r['repo'] != 'product-cli'
       and not r['immutable'] and not r['ident']]
q = [r for r in pop if gb.qualified(r)]
b = [r for r in pop if not gb.qualified(r)]
print(f'  population {len(pop)} = qualified {len(q)} + bare {len(b)}  (frozen instrument)')
per = collections.Counter(gb.area(r) for r in b)
print('  bare per area:', dict(sorted(per.items())))
print('  bare, wave bodies: up-core (W2) =', per['up-core'],
      '; W3 body (apparatus+core+papers+projections+applications) =',
      sum(per[a] for a in ('dn-apparatus','dn-core','dn-papers','dn-projections','dn-applications')))
print('  bare, outside the booked waves: up-other =', per['up-other'],
      ', dn-meta =', per['dn-meta'], ', dn-other =', per['dn-other'])

print('\n=== W4 (product-cli, assessed at Gate 6, never executed here)')
pc = [r for r in head if r['repo'] == 'product-cli']
pcm = [r for r in pc if not r['immutable']]
print(f'  occurrences {len(pc)}, mutable {len(pcm)}')
gfield = sum(1 for r in pc if r['path'].startswith('.ddd'))
print(f'  rows in .ddd/ (serialised ledger): {gfield} in',
      len({r["path"] for r in pc if r["path"].startswith(".ddd")}), 'files')

json.dump([{k: r.get(k) for k in ('repo','path','sense','ident','immutable')} |
           {'anchor': gb.WS.sub(' ', r['ctx'][max(0,r['tok_off']-40):r['tok_off']+len(r['token'])+40]).strip(),
            'bare': (r in b) if r in pop else None,
            'proposed': r.get('proposed', False)}
          for r in head],
          open(os.path.join(HERE, 'g1-head-ledger.json'), 'w'))
print('\nhead ledger written: g1-head-ledger.json')
