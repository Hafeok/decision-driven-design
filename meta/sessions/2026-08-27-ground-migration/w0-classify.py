#!/usr/bin/env python3
"""W0 — complete the ground audit's classification. Every occurrence, one sense or U-with-reason.

METHOD, stated so the result is checkable rather than trusted.

The audit (meta/ground-audit-2026-08-24.md) assigned 1,823 of 2,845 occurrences by an ordered rule
table with no default rule, and sampled 100 of the 1,022 the table did not match. This completes the
1,022 by hand, reading each occurrence in its own file rather than in the 240-character extract
window, and records one ruling per row with the reason it was taken.

INPUT is the audit's own committed extract, meta/sessions/2026-08-24-ground-audit/classification.json,
unaltered — so the rule-assigned half is inherited exactly and only the residual moves.

THE DECISION RULE, fixed after the first file and applied to every one after it: read the PREDICATE
APPLIED TO THE WORD, never the compound.
    world predicates   (obtains, varies, moves, is uncontrolled, is a dimension or region)  -> S1
    store predicates   (held, available, assembled, filed, cited, pinned, stale, complete)  -> S2
    act predicates     (read at, delivered, consulted, present, in context, bound at as-of)  -> S3
    rule predicates    (is a standard, determines acceptability, is the regulation)          -> S4
    population preds   (distribution over, evaluated over, per deployment)                   -> S5
An occurrence that will not sit in exactly one sense is U, with the reason recorded, never a default.

OUTPUT: w0-full-v2.json, sense per row over all 2,845; w0-residual.json, W0's 1,022; w0bis-rulings.json,
W0-bis's 456.

Per-file rulings and their reasons are in rulings/r0NN.py, which this script merges. Nothing here
re-derives a sense: the rulings ARE the classification, and this file only assembles and checks them.
"""
import json, glob, importlib.util, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIT = os.path.join(HERE, '..', '2026-08-24-ground-audit', 'classification.json')

def load_rulings(pattern='rulings/r0*.py'):
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, *pattern.split('/')))):
        n = os.path.basename(f)[:-3]
        s = importlib.util.spec_from_file_location(n, f)
        m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
        dup = set(out) & set(m.R)
        assert not dup, f'{n} re-rules rows already ruled: {sorted(dup)[:8]}'
        out.update(m.R)
    return out

def main(src, outdir):
    rows = json.load(open(src))
    residual = {i for i, r in enumerate(rows) if r['rule'] == 'residual-no-rule-matched'}
    R = load_rulings('rulings/r0*.py')
    assert set(R) == residual, (
        f'rulings cover {len(R)} rows, residual is {len(residual)}; '
        f'unruled={sorted(residual - set(R))[:8]} over-ruled={sorted(set(R) - residual)[:8]}')
    # W0-bis: the 427 prose-context rows plus the 29 anchored-class ordering corrections.
    B = load_rulings('rulings-bis/b0*.py')
    assert not (set(B) & residual), 'W0-bis must not overlap W0 — the residual was already read'
    full = {i: (R[i] if i in R else r['sense']) for i, r in enumerate(rows)}
    full.update(B)
    json.dump({str(k): v for k, v in R.items()}, open(os.path.join(outdir, 'w0-residual.json'), 'w'))
    json.dump({str(k): v for k, v in B.items()}, open(os.path.join(outdir, 'w0bis-rulings.json'), 'w'))
    json.dump({str(k): v for k, v in full.items()}, open(os.path.join(outdir, 'w0-full-v2.json'), 'w'))
    top = lambda s: s.split('-')[0]
    print(f'{len(full)} classified; 0 unassigned by construction (the assert above)')
    for k, v in sorted(collections.Counter(top(v) for v in full.values()).items()):
        print(f'  {k}  {v:>5}  {100*v/len(full):5.1f}%')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else AUDIT, sys.argv[2] if len(sys.argv) > 2 else HERE)
