#!/usr/bin/env python3
"""Verify every inline status assertion in a projection against the claim graph at a ref.

The gap this closes, and it is a third gap rather than a variation on the other two.
`check-quotations.py` verifies BLOCK quotations and says so honestly in its own docstring;
`check-appendix.py` re-reads the generated node tables. Neither reads the manuscript's MORE COMMON
form: the inline citation that asserts a status in running prose -- `[DDD-measure-06,
**established**]`. At the v5.9.0 -> v5.12.0 advance that gap hid a retirement. DDD-measure-06 is
retired at v5.12.0; the paper called it **established** in three places; both existing checkers
passed all three lines, because none of the three is a block quotation and none is an appendix row.

**A status label is the part of a citation a reader converts into warrant.** It is therefore the
part most worth checking, and it was the part with no check. That the review's central criticism was
that the paper communicates more warrant than the graph provides, and that the one unchecked
surface was exactly the warrant labels, is not a coincidence worth leaving unfixed.

The script also reports every cited node whose status MOVED between two refs, label or not, when a
baseline ref is given. A status can move under a citation that never named one while the prose
around it still asserts the old reading -- which is what happened at §8.4 and in the conclusion's
"what is established" list, neither of which carried a label.

Usage:  check-status.py <manuscript.md> <upstream-repo> <ref> [<baseline-ref>]
Exit 0 when every inline status assertion matches the graph at <ref>; 1 otherwise.
Appendix A is excluded, wherever it lives: it is generated wholesale and re-read by
check-appendix.py, and checking it here would report one defect twice.

Defect history, kept with the instrument:

  * Written as a one-off sweep at this revision's GATE 1 to answer a question -- does the pin
    advance break anything the two checkers cannot see -- and it did, four times. It was kept as
    a session artefact for one gate before being ruled an instrument. Recording that here because
    the instrument's origin is its warrant: it was not designed against a specification, it was
    generalised from a sweep that found something, and its coverage is therefore exactly the
    coverage of that sweep and no wider.

  * The citation regex accepts a status after a comma or an em dash, matching both forms the
    manuscript uses -- `[id, projected]` and `[id -- closing clause]`. A citation carrying NO
    status word is skipped rather than flagged: a projection may cite without asserting, and
    treating a bare citation as a defect would make the honest form the expensive one. The cost
    is that a bare citation whose surrounding PROSE asserts a status is invisible here, and the
    baseline-ref comparison is the mitigation rather than a cure.
"""
import re
import subprocess
import sys

import yaml

STATUSES = r'(settled|established|projected|reported|draft|retired)'


def show(repo, ref, path):
    r = subprocess.run(['git', '-C', repo, 'show', f'{ref}:{path}'],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'cannot read {path} at {ref}: {r.stderr.strip()}')
    return r.stdout


def statuses(repo, ref):
    out = {}
    for d in ('core/claims/', 'core/decisions/'):
        listing = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', ref, d],
                                 capture_output=True, text=True).stdout.split()
        for f in listing:
            if f.endswith('.yaml'):
                y = yaml.safe_load(show(repo, ref, f))
                out[y['id']] = y.get('status')
    for t in yaml.safe_load(show(repo, ref, 'core/graph/terms.yaml'))['terms']:
        out[t['id']] = t.get('status')
    return out


def main(path, repo, ref, baseline=None):
    now = statuses(repo, ref)
    was = statuses(repo, baseline) if baseline else {}
    body = open(path).read().split('## Appendix A')[0]

    checked = 0
    failures = []
    for i, line in enumerate(body.split('\n'), 1):
        for m in re.finditer(r'\[([A-Za-z][A-Za-z:\-0-9]*)((?:,|\s\u2014)[^\]]*)\]', line):
            node_id, tail = m.group(1), m.group(2)
            s = re.search(r'\*{0,2}' + STATUSES + r'\*{0,2}', tail)
            if not s:
                continue
            checked += 1
            claimed, actual = s.group(1), now.get(node_id)
            if actual is None:
                failures.append((i, node_id, claimed, 'ABSENT at ref'))
            elif actual != claimed:
                prior = f' (was {was[node_id]} at {baseline})' if node_id in was else ''
                failures.append((i, node_id, claimed, f'{actual}{prior}'))

    # Nodes cited anywhere in the body whose status moved between the two refs, label or not:
    # a status can move under a citation that never named one, and the prose around it still
    # asserts the old reading.
    moved = []
    if baseline:
        cited = set(re.findall(r'DDD-[a-z]+-\d+', body)) | set(re.findall(r'term:[a-z-]+', body))
        moved = sorted((c, was.get(c), now.get(c)) for c in cited if was.get(c) != now.get(c))

    print(f'{checked} inline status assertions checked, {len(failures)} wrong '
          f'({path} against {ref})')
    for line, node_id, claimed, actual in failures:
        print(f'  L{line}: [{node_id}, {claimed}] -- graph says {actual}')
    if baseline:
        print(f'{len(moved)} cited node(s) whose status moved {baseline} -> {ref}:')
        for c, o, n in moved:
            print(f'  {c}: {o} -> {n}')
    return 1 if failures else 0


if __name__ == '__main__':
    if not 4 <= len(sys.argv) <= 5:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
