#!/usr/bin/env python3
"""Verify every block quotation in a projection against the claim graph.

A quoted block placed under a citation asserts to the reader that the words are canon's.
No existing validator checks that assertion: E13 enforces byte-match for `ddd:embed` only,
and a prose citation carries no marker at all. This script closes that gap for a paper.

For each run of `> ` lines ending in a `[<id>...]` citation, the quoted text is compared
against that node's `statement` (claims and decisions) or `canonical_md` (terms) at a
pinned ref. A quotation must either match verbatim or declare itself partial in its own
citation — the trailing bracket carrying a disclosure such as "closing clause" or
"opening clause; the claim continues" — and a leading or trailing `…`.

Usage:  check-quotations.py <manuscript.md> <upstream-repo> <ref>
Exit 0 when every quotation verifies or is disclosed; 1 otherwise.

Defect history, kept with the instrument:

  * First version folded case at the first character only, and failed a legitimate quotation of
    DDD-measure-02 that begins mid-sentence at "H(V)". Fixed by trying the quotation as written
    and with either casing of its first letter -- and only those, so an internal rewording
    still fails.
"""
import re
import subprocess
import sys

import yaml

DISCLOSURE = re.compile(r'(closing clause|opening clause|first clause|the claim continues|abridged|partial)', re.I)


def show(repo, ref, path):
    r = subprocess.run(['git', '-C', repo, 'show', f'{ref}:{path}'],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'cannot read {path} at {ref}: {r.stderr.strip()}')
    return r.stdout


def load_graph(repo, ref):
    nodes = {}
    for d in ('core/claims/', 'core/decisions/'):
        listing = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', ref, d],
                                 capture_output=True, text=True).stdout.split()
        for f in listing:
            if f.endswith('.yaml'):
                y = yaml.safe_load(show(repo, ref, f))
                nodes[y['id']] = str(y.get('statement', ''))
    for t in yaml.safe_load(show(repo, ref, 'core/graph/terms.yaml'))['terms']:
        nodes[t['id']] = str(t.get('canonical_md', ''))
    return nodes


def normalise(s):
    """Strip markdown emphasis and quote marks, collapse whitespace, fold typography."""
    s = re.sub(r'[*`>]', '', s)
    s = re.sub(r'\s+', ' ', s)
    for a, b in (('\u2014', '-'), ('\u2018', "'"), ('\u2019', "'"),
                 ('\u201c', '"'), ('\u201d', '"'), ('\u2026', '')):
        s = s.replace(a, b)
    return s.strip()


def contains(canon, quoted):
    """Is `quoted` a verbatim run of `canon`?

    A quotation may legitimately begin mid-sentence, in which case the author
    capitalises its first letter, or begin at a sentence canon capitalises. Both
    readings are tried, and only those two -- an internal rewording still fails.
    """
    if not quoted:
        return False
    variants = {quoted, quoted[:1].lower() + quoted[1:], quoted[:1].upper() + quoted[1:]}
    return any(v in canon for v in variants)


def main(path, repo, ref):
    nodes = load_graph(repo, ref)
    text = open(path).read()
    ok = disclosed = 0
    failures = []

    for block in re.findall(r'((?:^> .*\n)+)', text, re.M):
        body = normalise(block)
        cite = re.search(r'\[([A-Za-z][A-Za-z:\-0-9]*)([^\]]*)\]\s*$', body)
        if not cite:
            failures.append(('UNCITED', '', body[:110]))
            continue
        node_id, tail = cite.group(1), cite.group(2)
        quoted = normalise(body[:cite.start()])
        if node_id not in nodes:
            failures.append(('UNKNOWN NODE', node_id, ''))
            continue
        canon = normalise(nodes[node_id])
        if contains(canon, quoted):
            ok += 1
        elif DISCLOSURE.search(tail) and contains(canon, quoted.rstrip('.')):
            disclosed += 1
        else:
            failures.append(('NOT VERBATIM', node_id, quoted[:110]))

    print(f'{ok} verbatim, {disclosed} disclosed-partial, {len(failures)} failing '
          f'({path} against {ref})')
    for kind, node_id, detail in failures:
        print(f'  {kind}: {node_id} {detail}')
    return 1 if failures else 0


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
