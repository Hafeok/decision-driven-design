#!/usr/bin/env python3
"""G1 — the two merged sessions' movement, isolated.

Point A is the predecessor's read state: actor-indexed-determination at
ce2c477 (= v5.11.0), decision-driven-design at e81a454, product-cli at
d0f4297. Everything from the classification's extract up to point A was
discharged by the predecessor (gate4-plan.md §8); the A->head delta is
therefore exactly what the two merged sessions moved — the ground-migration
session's own merge (upstream v5.12.0 + the downstream record and seed) and
the Paper A revision (PR #32).

Usage: check the two repositories out at point A in worktrees, then
    python3 g1-pointA.py <upstream-A-root> <downstream-A-root> <product-cli-root>
Writes g1-delta-A-head.json. product-cli's head IS d0f4297 — verified
unchanged since the predecessor read it.
"""
import os, sys, json, collections, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('g1', os.path.join(HERE, 'g1-reconcile.py'))
g1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(g1)

A = g1.extract([(sys.argv[1], 'upstream'), (sys.argv[2], 'downstream'),
                (sys.argv[3], 'product-cli')])
H = json.load(open(os.path.join(HERE, 'g1-head-extract.json')))
print(f'point A rows: {len(A)}  head rows: {len(H)}')

b2h, remA, addH = g1.match(A, H)
pair = {('downstream','papers/paper-a/paper-a.md'),
        ('downstream','papers/paper-a/paper-a-supplement.md')}
moved = {}
for width in (240, 80, 32):
    anchors = collections.defaultdict(list)
    for j in addH:
        r = H[j]
        if (r['repo'], r['path']) in pair:
            anchors[(r['token'], g1.window(r, width))].append(j)
    still = []
    for i in remA:
        r = A[i]
        if (r['repo'], r['path']) in pair and i not in moved:
            a = (r['token'], g1.window(r, width))
            if anchors[a]:
                j = anchors[a].pop(0); moved[i] = j; addH.remove(j); continue
        still.append(i)
    remA = still

print(f'A->head: matched {len(b2h)+len(moved)} (moved-to-supplement {len(moved)}), '
      f'removed {len(remA)}, added {len(addH)}')
for name, idxs, rows in (('removed', remA, A), ('added', addH, H)):
    pf = collections.Counter((rows[i]['repo'], rows[i]['path']) for i in idxs)
    print(f'\n{name} A->head per file:')
    for (repo, path), n in pf.most_common():
        print(f'  {n:>3}  {repo}:{path}')
json.dump({'removed': [dict(A[i], pointA_index=i) for i in remA],
           'added':   [H[j] for j in addH],
           'moved':   len(moved)},
          open(os.path.join(HERE, 'g1-delta-A-head.json'), 'w'), indent=1)
