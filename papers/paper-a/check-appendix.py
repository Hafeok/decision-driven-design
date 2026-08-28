#!/usr/bin/env python3
"""Re-read a rendered Appendix A against the claim graph, independently of the generator.

Verbatim-by-construction is only half a verification: a generator can be wrong in a way its
own output cannot reveal. This script takes the *rendered markdown* as its input — not the
graph objects the generator held — parses the tables back out, and compares every cell against
the graph. It shares no code with `gen-appendix.py` by design.

Four things are checked, and they are different failures:
  1. every rendered row matches the graph word-for-word;
  2. every node the body cites has a row (nothing dropped);
  3. every row corresponds to a node the body cites (nothing invented);
  4. the hypothesis-set rows really do carry empty evidence.

Usage:  check-appendix.py <manuscript.md> <upstream-repo> <ref>
Exit 0 when the appendix matches the graph; 1 otherwise.

Defect history, kept with the instrument because a check that can be wrong about a correct
artefact could have been wrong about an incorrect one:

  * First run reported four discrepancies -- DDD-floor-01, DDD-measure-02, DDD-measure-03,
    DDD-measure-10 -- and all four were this script's fault. Their statements carry literal
    pipes, H(V|X) and H(V|S), which the generator correctly escapes as \| in a table cell;
    the parser split rows on a bare '|' and broke those cells in two. The appendix was right.
    Fixed by splitting on unescaped pipes only; the hazard is commented at the split.

  * The status check was guarded on `len(cols) == 2`. When the claims table gained a `kind`
    column the guard stopped matching, so the status column silently stopped being checked
    while the statement column carried on and the run reported success -- a verification
    quietly weaker than the one before it, with nothing to see. This was predicted from
    reading the code before the column was added, and fixed in the same commit. Metadata
    columns are now counted from the LEFT and named individually, so a future column cannot
    switch an existing check off. **Never guard a check on a total column count.**
"""
import re
import subprocess
import sys

import yaml


def show(repo, ref, path):
    r = subprocess.run(['git', '-C', repo, 'show', f'{ref}:{path}'],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'cannot read {path} at {ref}: {r.stderr.strip()}')
    return r.stdout


def graph(repo, ref):
    nodes = {}
    for d in ('core/claims/', 'core/decisions/'):
        for f in subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', ref, d],
                                capture_output=True, text=True).stdout.split():
            if f.endswith('.yaml'):
                y = yaml.safe_load(show(repo, ref, f))
                nodes[y['id']] = y
    for t in yaml.safe_load(show(repo, ref, 'core/graph/terms.yaml'))['terms']:
        nodes[t['id']] = t
    return nodes


def flat(s):
    return ' '.join(str(s).split())


def unescape(cell_text):
    return flat(cell_text).replace(r'\|', '|')


def strip_quote(md):
    return flat(' '.join(re.sub(r'^> ?', '', ln) for ln in str(md).split('\n')))


def main(path, repo, ref):
    nodes = graph(repo, ref)
    # Which ids are claims, so a decisions row (id | statement) is not mistaken for a claims
    # row that lost its metadata columns.
    claim_ids = {i for i, n in nodes.items() if 'status' in n and not i.startswith('term:')}
    text = open(path).read()
    head, _, appendix = text.partition('## Appendix A')
    if not appendix:
        sys.exit('no Appendix A found')

    body_cited = set(re.findall(r'DDD-[a-z]+-\d+', head)) | set(re.findall(r'term:[a-z-]+', head))
    rendered, bad = set(), []

    # Statements carry literal pipes -- H(V|X), H(V|S) -- escaped as \| in a cell. Splitting on
    # a bare '|' would break those cells in two and report four false discrepancies.
    for row in re.findall(r'^\| `([^`]+)` \|(.*)\|\s*$', appendix, re.M):
        node_id, rest = row[0], row[1]
        cols = [c.strip() for c in re.split(r'(?<!\\)\|', rest)]
        if node_id in rendered and not node_id.startswith('DDD-hyp') and node_id != 'DDD-frame-07':
            bad.append(f'{node_id}: duplicate row')
        rendered.add(node_id)
        node = nodes.get(node_id)
        if node is None:
            bad.append(f'{node_id}: row for a node absent from the graph at {ref}')
            continue
        if node_id.startswith('term:'):
            if unescape(cols[-1]) != strip_quote(node.get('canonical_md') or
                                                 '— registry entry; no canonical wording pinned'):
                bad.append(f'{node_id}: canonical wording differs from the graph')
            if cols[0] != node.get('term', node_id.split(':', 1)[1]):
                bad.append(f'{node_id}: term name differs from the graph')
        elif len(cols) == 4:
            # The hypothesis-set table: id | status | evidence | owner | falsifier. Four
            # columns after the id is unambiguous -- a claims row has three and a decisions
            # row has one -- but that is a fact about the current tables, so if a fifth column
            # is ever added anywhere, this discrimination is the thing to revisit first.
            status, evidence, owner, falsifier = cols
            if status != str(node.get('status')):
                bad.append(f'{node_id}: status differs from the graph')
            empty = node.get('evidence') in ([], None)
            if empty != evidence.startswith('`[]`'):
                bad.append(f'{node_id}: evidence column misreports the graph')
            if not empty:
                bad.append(f'{node_id}: rendered in the hypothesis table with NON-EMPTY evidence')
            if owner != str(node.get('owner')):
                bad.append(f'{node_id}: owner differs from the graph')
            if (falsifier == 'yes') != bool(node.get('falsifier')):
                bad.append(f'{node_id}: falsifier column misreports the graph')
        else:
            # Claims and decisions. The claims table is id | kind | status | statement and the
            # decisions table is id | statement, so the metadata columns are counted from the
            # LEFT and the statement is read from the right. Guarding a column's check on the
            # total column count -- as this did while the claims table had two columns -- means
            # that adding a column silently switches the check off while the run still reports
            # success. That is the failure mode this instrument exists to prevent, so it must
            # not be the instrument's own.
            if unescape(cols[-1]) != flat(node.get('statement')):
                bad.append(f'{node_id}: statement differs from the graph')
            meta = cols[:-1]
            if len(meta) == 2:                                 # claims: kind, then status
                if meta[0] != str(node.get('kind')):
                    bad.append(f'{node_id}: kind differs from the graph')
                if meta[1] != str(node.get('status')):
                    bad.append(f'{node_id}: status differs from the graph')
            elif len(meta) == 1:                               # a claims row with no kind column
                bad.append(f'{node_id}: claims row carries no kind column '
                           '(regenerate with gen-appendix.py)')
            elif node_id in claim_ids:
                bad.append(f'{node_id}: claims row has {len(cols)} columns, expected 4')

    dropped = sorted(body_cited - rendered)
    invented = sorted(rendered - body_cited)
    for d in dropped:
        bad.append(f'{d}: cited in the body, absent from the appendix')
    for i in invented:
        bad.append(f'{i}: in the appendix, cited nowhere in the body')

    print(f'{len(rendered)} nodes rendered, {len(body_cited)} cited in the body, '
          f'{len(bad)} discrepancies ({path} against {ref})')
    for b in bad:
        print(f'  {b}')
    return 1 if bad else 0


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
