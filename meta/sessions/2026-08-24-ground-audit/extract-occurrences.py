#!/usr/bin/env python3
"""Extract every occurrence of `ground` with its context, for classification.

One row per occurrence: repository, path, line number, artefact class, whether
the occurrence sits in an identifier or in prose, the matched token, and 120
characters of context either side. The classifier at classify.py reads this file
and nothing else, so the classification is reproducible from a fixed extract.
"""
import os, re, json, sys

TOKEN   = re.compile(r'(?i)(?<![A-Za-z0-9])ground[A-Za-z0-9_]*')
UNESC   = re.compile(r'\\[ntr]')
SKIP    = {'.git','target','node_modules','.venv','__pycache__','dist'}
TEXT    = {'.md','.yaml','.yml','.py','.rs','.toml','.json','.txt','.ttl','.sh',
           '.jsx','.js','.ts','.tsx','.css','.html','.sql',''}
SELF    = os.path.join('meta','sessions','2026-08-24-ground-audit')

# An occurrence is an IDENTIFIER when it is part of a claim ID, a path, a code
# symbol, a YAML key, or a crate name — things a rename must migrate as data
# rather than rewrite as prose.
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
    # product-cli
    if rel.startswith('.ddd'):                     return 'C7 .ddd ledger (serialised)'
    if rel.startswith('.decisions'):               return 'C8 .decisions ledger'
    if rel.startswith('docs' + os.sep + 'g-track'):return 'C9 docs/g-track'
    if rel.startswith('docs'):                     return 'C3 docs other'
    if rel.endswith('.rs'):                        return 'C1 Rust source'
    if rel.endswith(('.yaml','.yml')):             return 'C2 YAML'
    if rel.endswith(('.json','.ttl')):             return 'C4 schema'
    if rel.endswith('.toml'):                      return 'C5 manifests'
    return 'C6 other'

# Immutable by this repository's own rules: never migrated, only classified.
IMMUTABLE = {'A9 release descriptors', 'B13 session records'}

def run(roots):
    rows = []
    for root, repo in roots:
        for dp, dn, fns in os.walk(root):
            dn[:] = [d for d in dn if d not in SKIP]
            for fn in fns:
                if os.path.splitext(fn)[1].lower() not in TEXT:
                    continue
                p = os.path.join(dp, fn)
                rel = os.path.relpath(p, root)
                if rel.startswith(SELF):
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
                    })
    return rows

if __name__ == '__main__':
    rows = run([('/home/user/actor-indexed-determination','upstream'),
                ('/home/user/decision-driven-design','downstream'),
                ('/home/user/hafeok/product-cli','product-cli')])
    json.dump(rows, open(sys.argv[1],'w'))
    print(f"{len(rows)} occurrences extracted")
