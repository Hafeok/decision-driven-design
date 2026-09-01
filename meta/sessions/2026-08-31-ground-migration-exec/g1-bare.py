#!/usr/bin/env python3
"""G1 — rebuild the qualified/bare split over the S2/S3 prose population.

GATE 4 of the predecessor session measured: of the 567 S2/S3 prose occurrences
in canon and the projection (mutable, non-identifier), 380 are already
qualified by a verb or adjective within 40 characters and 187 are bare. The
instrument that measured it was NOT committed — the figure is in
gate4-plan.md §1 and the seed, the row list is nowhere. This rebuilds it.

Anchoring, per the seed's first method mechanism: the 40-character window is
clipped at clause boundaries (sentence stops, semicolons, dashes, list
separators, markdown table pipes) so the rule cannot read a qualifier out of
the next clause. A comma does NOT clip: "the ground, as delivered," is one
predication. The qualifier lexicon is drawn from the audit's own predicate
lists (classify.py: store predicates, act predicates) plus the four
already-correct shapes gate4-plan.md §1 itself quotes.

Output: per-row determination (g1-bare.json) keyed by content anchor, and the
per-area counts the wave sizes rest on. The 380/187 figure is a PREDICTION in
the seed's sense: this instrument's result is verified against it and any
divergence is recorded, never reconciled by tuning.
"""
import json, re, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))

# What counts as the occurrence already naming what is done to (or held of)
# the ground. Word-boundary, case-insensitive, matched inside the clipped
# window around the token.
QUAL = re.compile(r'''(?ix)\b(
    read|reads|reading|re-?read(s|ing)?           # the act predicates
  | deliver(s|ed|y|ing|able)?|undelivered
  | consult(s|ed|ing)?
  | inspect(s|ed|ing|able)?
  | observ(e|es|ed|ing|able)
  | present|absent
  | bound|binds?|binding|as-of
  | held|holds?|holding
  | availab(le|ility)|unavailable
  | assembl(e|es|ed|ing|y)
  | fil(e|es|ed|ing)
  | cit(e|es|ed|ing)
  | pinn?(ed|ing)?\b
  | stale|fresh
  | complete|incomplete|partial
  | fixed|fix(es|ed|ing)?
  | channel(s|led)?
  | poison(ed|ing)?
  | adversarial
  | supplied|supply|supplies
  | declared?|declar(es|ing)
  | stored?|caches?d?
  | snapshot(s|ted)?
  | provided?|provision(ed)?
  | carri(es|ed)|carry(ing)?
  | fetch(es|ed|ing)?
  | at\ the\ act                                   # gate4-plan's own example
  # Revision 1 — each word warranted by a sampled row the first lexicon
  # mis-scored as bare (recorded in gate1-reconciliation.md; the additions
  # repair found defects, they do not tune toward the seed's figure):
  | check(s|ed|ing)?                               # "more frequent ground checks"
  | consum(e|es|ed|ing)                            # "consuming it as ground"
  | emit(s|ted|ting)?                              # "emits ground projections"
  | (pre-?)?resolv(e|es|ed|ing)                    # "pre-resolve some ground"
  | accessib(le|ility)                             # "ground accessibility"
  | assur(ance|ed)                                 # "ground assurance"
  # Revision 2 — same warrant discipline, second fresh sample; the
  # instrument is FROZEN after this revision whatever figure it yields:
  | encod(e|es|ed|ing|able)                        # "you can encode ground you control"
  | (un)?verif(y|ies|ied|iable|ication)            # "competence on unverifiable ground"
  | (un)?trust(ed|worthy)?                         # "trusted ground has three generators"
  | at\ act[ -]time                                # "ground not as expected at act time"
)\b''')

# Clause boundaries that CLIP the window (the seed's mechanism 1: [^.] does
# not stop at these, so this instrument must).
CLIP = re.compile(r'[.;!?]|—|--|·|\||\s#\s|\n')

TOKEN = re.compile(r'(?i)(?<![A-Za-z0-9])ground[A-Za-z0-9_]*')
WS = re.compile(r'\s+')

def tok_off(row):
    if 'tok_off' in row: return row['tok_off']
    cands = [m.start() for m in TOKEN.finditer(row['ctx'])
             if m.group(0).lower() == row['token']]
    return min(cands, key=lambda i: abs(i - 120)) if cands else len(row['ctx'])//2

def clipped_window(ctx, off, tlen, w=40):
    left = ctx[max(0, off-w):off]
    m = None
    for m in CLIP.finditer(left): pass
    if m: left = left[m.end():]
    right = ctx[off+tlen : off+tlen+w]
    m = CLIP.search(right)
    if m: right = right[:m.start()]
    return left, right

def qualified(row, w=40):
    ctx = row['ctx']; off = tok_off(row); tlen = len(row['token'])
    left, right = clipped_window(ctx, off, tlen, w)
    return bool(QUAL.search(left) or QUAL.search(right))

def population(rows, senses=None):
    top = lambda s: s.split('-')[0]
    out = []
    for i, r in enumerate(rows):
        s = senses[str(i)] if senses else r['sense']
        if top(s) in ('S2','S3') and r['repo'] != 'product-cli' \
           and not r['immutable'] and not r['ident']:
            out.append((dict(r, sense=s)))
    return out

def area(r):
    if r['repo'] == 'upstream':
        return 'up-core' if r['path'].startswith('core/') else 'up-other'
    p = r['path']
    if p.startswith('apparatus/'):    return 'dn-apparatus'
    if p.startswith('core/'):         return 'dn-core'
    if p.startswith('papers/'):       return 'dn-papers'
    if p.startswith('projections/'):  return 'dn-projections'
    if p.startswith('applications/'): return 'dn-applications'
    if p.startswith('meta/'):         return 'dn-meta'
    return 'dn-other'

def report(pop, label):
    q = [r for r in pop if qualified(r)]
    b = [r for r in pop if not qualified(r)]
    print(f'{label}: population {len(pop)} = qualified {len(q)} + bare {len(b)}')
    per = collections.Counter((area(r)) for r in b)
    print('  bare per area:', dict(sorted(per.items())))
    return q, b

if __name__ == '__main__':
    base = json.load(open(os.path.join(HERE,'..','2026-08-24-ground-audit','classification.json')))
    senses = json.load(open(os.path.join(HERE,'..','2026-08-27-ground-migration','w0-full-v2.json')))
    pop = population(base, senses)
    q, b = report(pop, 'baseline (seed predicted 380/187)')
    json.dump([{'repo':r['repo'],'path':r['path'],'sense':r['sense'],
                'anchor': WS.sub(' ', r['ctx'][max(0,tok_off(r)-40):tok_off(r)+len(r['token'])+40]).strip(),
                'bare': not qualified(r)} for r in pop],
              open(os.path.join(HERE,'g1-bare.json'),'w'), indent=1)
