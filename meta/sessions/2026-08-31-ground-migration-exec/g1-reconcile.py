#!/usr/bin/env python3
"""G1 — reconcile the execution-grade classification against head.

The baseline is the audit's committed extract (2,845 rows) carrying the senses
w0-classify.py assembled into w0-full-v2.json. The corpus has moved: the
predecessor's own §6 landed upstream as v5.12.0, and the Paper A revision
merged downstream as PR #32. This instrument re-extracts at head with the same
extraction logic as w0-extract-head.py, then matches baseline rows to head rows
BY CONTENT, never by line number (the seed's third method mechanism).

Matching: per (repo, path), greedy multiset matching in three passes of
decreasing anchor width — full normalised context, an 80-character window
centred on the token, a 32-character window. A baseline row with no head match
is REMOVED; a head row with no baseline match is ADDED. A fourth pass matches
removed-against-added across the paper-a.md / paper-a-supplement.md pair, since
the revision moved material between those two files without rewording it.

Exclusions, stated because they are rulings and not defaults:
  - meta/sessions/2026-08-24-ground-audit and 2026-08-27-ground-migration are
    excluded exactly as the committed extractor excludes them (a session must
    not count itself; the audit's own artefacts quote the corpus wholesale).
  - meta/sessions/2026-08-31-ground-migration-exec (this session) is excluded
    for the same reason.
  - meta/sessions/2026-08-30-paper-a-revision is INCLUDED, as the committed
    extractor would include it: it is another session's record, class B13,
    immutable — classified, never migrated. Its rows are counted separately in
    the report so the immutable growth is visible rather than mixed in.
"""
import os, re, json, sys, collections

HERE   = os.path.dirname(os.path.abspath(__file__))
SESS27 = os.path.join(HERE, '..', '2026-08-27-ground-migration')
AUDIT  = os.path.join(HERE, '..', '2026-08-24-ground-audit', 'classification.json')

# ---- extraction, byte-for-byte the logic of w0-extract-head.py ----
TOKEN   = re.compile(r'(?i)(?<![A-Za-z0-9])ground[A-Za-z0-9_]*')
UNESC   = re.compile(r'\\[ntr]')
SKIP    = {'.git','target','node_modules','.venv','__pycache__','dist'}
TEXT    = {'.md','.yaml','.yml','.py','.rs','.toml','.json','.txt','.ttl','.sh',
           '.jsx','.js','.ts','.tsx','.css','.html','.sql',''}
SELF    = os.path.join('meta','sessions','2026-08-24-ground-audit')
SELF2   = os.path.join('meta','sessions','2026-08-27-ground-migration')
SELF3   = os.path.join('meta','sessions','2026-08-31-ground-migration-exec')
IDENT = re.compile(r'(?i)(DDD-ground-\d+|ground-cli|ground_[a-z_]+|[a-z]+_ground\b'
                   r'|ground/|/ground|ground\.rs|ground:\s|ground\s*:\s*\S|`ground`)')

def artefact_class(repo, rel):
    if repo == 'upstream':
        if rel == 'core/graph/terms.yaml':        return 'A1 term registry'
        if rel.startswith('core/graph/'):          return 'A2 upstream graph'
        if rel.startswith('core/claims/'):         return 'A3 claim files'
        if rel.startswith('core/decisions/'):      return 'A4 decision files'
        if rel.startswith('core/assets/'):         return 'A5 assets'
        if rel.startswith('core/'):                return 'A6 core documents'
        if rel.startswith('meta/'):                return 'A7 meta / holding notes'
        if rel.startswith('spec/'):                return 'A8 spec'
        if rel.startswith('releases/'):            return 'A9 release descriptors'
        if rel.startswith('i18n/'):                return 'A10 i18n'
        return 'A12 root docs'
    if repo == 'downstream':
        if rel.startswith('graph/axis-registry'):  return 'B1 axis registry'
        if rel.startswith('graph/'):               return 'B2 pins'
        if rel.startswith('core/claims/'):         return 'B3 claim files'
        if rel.startswith('core/decisions/'):      return 'B4 decision files'
        if rel.startswith('core/assets/'):         return 'B5 assets'
        if rel.startswith('core/'):                return 'B6 core documents'
        if rel.startswith('apparatus/'):           return 'B7 apparatus'
        if rel.startswith('papers/paper-a'):       return 'B8 Paper A (merged)'
        if rel.startswith('papers/measure-note'):  return 'B9 measure note (merged)'
        if rel.startswith('papers/'):              return 'B10 papers other'
        if rel.startswith('projections/'):         return 'B11 projections'
        if rel.startswith('applications/'):        return 'B12 applications'
        if rel.startswith('meta/sessions/'):       return 'B13 session records'
        if rel.startswith('meta/'):                return 'B14 meta / holding notes'
        if rel.startswith('migration'):            return 'B15 migration'
        if rel.startswith('spec/'):                return 'B16 spec'
        return 'B18 root docs'
    if rel.startswith('.ddd'):                     return 'C7 .ddd ledger (serialised)'
    if rel.startswith('.decisions'):               return 'C8 .decisions ledger'
    if rel.startswith('docs' + os.sep + 'g-track'):return 'C9 docs/g-track'
    if rel.startswith('docs'):                     return 'C3 docs other'
    if rel.endswith('.rs'):                        return 'C1 Rust source'
    if rel.endswith(('.yaml','.yml')):             return 'C2 YAML'
    if rel.endswith(('.json','.ttl')):             return 'C4 schema'
    if rel.endswith('.toml'):                      return 'C5 manifests'
    return 'C6 other'

IMMUTABLE = {'A9 release descriptors', 'B13 session records'}

def extract(roots):
    rows = []
    for root, repo in roots:
        for dp, dn, fns in os.walk(root):
            dn[:] = [d for d in dn if d not in SKIP]
            for fn in sorted(fns):
                if os.path.splitext(fn)[1].lower() not in TEXT:
                    continue
                p = os.path.join(dp, fn)
                rel = os.path.relpath(p, root)
                if rel.startswith((SELF, SELF2, SELF3)):
                    continue
                try:
                    raw = open(p, encoding='utf-8').read()
                except Exception:
                    continue
                text = UNESC.sub(' ', raw)
                lines = text.split('\n')
                offs, o = [], 0
                for ln in lines:
                    offs.append(o); o += len(ln) + 1
                for m in TOKEN.finditer(text):
                    lo = 0
                    while lo + 1 < len(offs) and offs[lo+1] <= m.start():
                        lo += 1
                    a, b = max(0, m.start()-120), min(len(text), m.end()+120)
                    ctx = text[a:b].replace('\n', ' ')
                    cls = artefact_class(repo, rel)
                    rows.append({
                        'repo': repo, 'path': rel, 'line': lo+1, 'class': cls,
                        'token': m.group(0).lower(),
                        'ident': bool(IDENT.search(text[max(0,m.start()-14):m.end()+3])),
                        'immutable': cls in IMMUTABLE,
                        'ctx': ctx,
                        'tok_off': m.start()-a,   # token offset inside ctx (content anchor aid)
                    })
    return rows

# ---- content anchors ----
WS = re.compile(r'\s+')
def norm(s): return WS.sub(' ', s).strip()

def window(row, w):
    """A w-character window centred on the token, whitespace-normalised.

    The audit's extractor and w0-extract-head.py share one geometry:
    ctx = text[max(0, start-120) : end+120], so the token sits at offset
    min(120, start). Head rows carry the exact offset; for baseline rows the
    token is recovered as the token-boundary match closest to offset 120.
    """
    ctx = row['ctx']
    off = row.get('tok_off')
    if off is None:
        cands = [m.start() for m in TOKEN.finditer(ctx)
                 if m.group(0).lower() == row['token']]
        off = min(cands, key=lambda i: abs(i - 120)) if cands else len(ctx)//2
    a = max(0, off - w//2); b = min(len(ctx), off + len(row['token']) + w//2)
    return norm(ctx[a:b]).lower()

def match(base, head, key=lambda r: (r['repo'], r['path'])):
    """Greedy multiset matching per key, three anchor widths, then leftovers."""
    bykey_b = collections.defaultdict(list)
    bykey_h = collections.defaultdict(list)
    for i, r in enumerate(base): bykey_b[key(r)].append(i)
    for j, r in enumerate(head): bykey_h[key(r)].append(j)
    b2h = {}
    for k in bykey_b:
        bs, hs = bykey_b[k], list(bykey_h.get(k, []))
        # pass 0: full-context equality, independent of anchor centring —
        # catches rows whose token the baseline anchor recovery mis-centres
        anchors = collections.defaultdict(list)
        for j in hs: anchors[(head[j]['token'], norm(head[j]['ctx']).lower())].append(j)
        rest = []
        for i in bs:
            a = (base[i]['token'], norm(base[i]['ctx']).lower())
            if anchors[a]:
                j = anchors[a].pop(0); b2h[i] = j; hs.remove(j)
            else:
                rest.append(i)
        bs = rest
        for width in (240, 80, 32):
            anchors = collections.defaultdict(list)
            for j in hs: anchors[(head[j]['token'], window(head[j], width))].append(j)
            rest = []
            for i in bs:
                if i in b2h: continue
                a = (base[i]['token'], window(base[i], width))
                if anchors[a]:
                    j = anchors[a].pop(0)
                    b2h[i] = j
                    hs.remove(j)
                else:
                    rest.append(i)
            bs = rest
    unmatched_b = [i for i in range(len(base)) if i not in b2h]
    matched_h = set(b2h.values())
    unmatched_h = [j for j in range(len(head)) if j not in matched_h]
    return b2h, unmatched_b, unmatched_h

def main():
    roots = [(sys.argv[1] if len(sys.argv) > 1 else '/home/user/actor-indexed-determination', 'upstream'),
             (sys.argv[2] if len(sys.argv) > 2 else '/home/user/decision-driven-design', 'downstream'),
             (sys.argv[3] if len(sys.argv) > 3 else '/home/user/hafeok/product-cli', 'product-cli')]
    base = json.load(open(AUDIT))
    senses = json.load(open(os.path.join(SESS27, 'w0-full-v2.json')))
    for i, r in enumerate(base): r['sense'] = senses[str(i)]
    head = extract(roots)
    print(f'baseline {len(base)} rows; head {len(head)} rows')

    b2h, rem_b, add_h = match(base, head)
    # fourth pass: the supplement split — content moved between two named files
    pair = {('downstream','papers/paper-a/paper-a.md'),
            ('downstream','papers/paper-a/paper-a-supplement.md')}
    moved = {}
    for width in (240, 80, 32):
        anchors = collections.defaultdict(list)
        for j in add_h:
            r = head[j]
            if (r['repo'], r['path']) in pair:
                anchors[(r['token'], window(r, width))].append(j)
        still = []
        for i in rem_b:
            r = base[i]
            if (r['repo'], r['path']) in pair and i not in moved:
                a = (r['token'], window(r, width))
                if anchors[a]:
                    j = anchors[a].pop(0); moved[i] = j
                    add_h.remove(j); continue
            still.append(i)
        rem_b = still

    out = {
        'removed': [dict(base[i], baseline_index=i) for i in rem_b],
        'added':   [head[j] for j in add_h],
        'moved_supplement': [{'from': dict(base[i], baseline_index=i),
                              'to': head[j]} for i, j in sorted(moved.items())],
        'matched': len(b2h) + len(moved),
    }
    json.dump(head, open(os.path.join(HERE, 'g1-head-extract.json'), 'w'))
    json.dump(out, open(os.path.join(HERE, 'g1-delta.json'), 'w'), indent=1)

    print(f'matched {out["matched"]} (of which {len(moved)} moved into the supplement); '
          f'removed {len(rem_b)}; added {len(add_h)}')
    pf = collections.Counter((base[i]['repo'], base[i]['path']) for i in rem_b)
    print('\nremoved, per file (with baseline senses):')
    for (repo, path), n in pf.most_common():
        cs = collections.Counter(base[i]['sense'] for i in rem_b
                                 if (base[i]['repo'], base[i]['path']) == (repo, path))
        print(f'  {n:>3}  {repo}:{path}  {dict(cs)}')
    pf = collections.Counter((head[j]['repo'], head[j]['path']) for j in add_h)
    print('\nadded, per file:')
    for (repo, path), n in pf.most_common():
        print(f'  {n:>3}  {repo}:{path}')

if __name__ == '__main__':
    main()
