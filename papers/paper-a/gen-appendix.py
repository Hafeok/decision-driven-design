#!/usr/bin/env python3
"""Generate Appendix A for Paper A, wholesale, from the claim graph.

Appendix A is generated and never hand-edited. Regenerating both tables from
`core/claims/`, `core/decisions/` and `core/graph/terms.yaml` makes every row verbatim by
construction, and corrects drifted rows in the same pass that adds new ones. The rendered
result is then re-read against the graph by a separate script, `check-appendix.py`, so the
check is independent of the generator that produced it.

Usage:  gen-appendix.py <manuscript.md> <upstream-repo> <ref>
Rewrites everything from the `## Appendix A` heading to end of file.
"""
import re
import subprocess
import sys

import yaml

HEADING = '## Appendix A. Cited claims, decisions and terms'

PREAMBLE = """
The paper cites nodes in the framework's claim graph. Statements below are reproduced
word-for-word from the graph at the ref pinned in the front matter, so the paper can be checked
without it. **Status** is the graph's own: *settled* and *established* are argued and unchallenged,
*reported* is exercised by a reproducing computation, *projected* is proposed with a declared
falsifier and not yet met, *draft* is filed and not yet ratified, *retired* is superseded and kept
with the correction that killed it.

**This appendix is generated from the graph and never hand-edited** (`gen-appendix.py`), then
re-read against the graph by an independent script (`check-appendix.py`).
"""

HSET_PREAMBLE = """
The hypothesis set is broken out because its discipline is the easiest thing in the paper for a
reader to mistake. Every row is `projected`, every row declares a falsifier, **every evidence field
is empty**, and every row is owned by a study that has not been run. The columns below are the
graph's own fields, not the paper's summary of them.
"""


def show(repo, ref, path):
    r = subprocess.run(['git', '-C', repo, 'show', f'{ref}:{path}'],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'cannot read {path} at {ref}: {r.stderr.strip()}')
    return r.stdout


def load(repo, ref):
    claims, decisions = {}, {}
    for d, into in (('core/claims/', claims), ('core/decisions/', decisions)):
        listing = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', ref, d],
                                 capture_output=True, text=True).stdout.split()
        for f in listing:
            if f.endswith('.yaml'):
                y = yaml.safe_load(show(repo, ref, f))
                into[y['id']] = y
    terms = {t['id']: t for t in yaml.safe_load(show(repo, ref, 'core/graph/terms.yaml'))['terms']}
    return claims, decisions, terms


def cell(s):
    """One graph field as one table cell: collapsed to a line, pipes escaped."""
    return ' '.join(str(s).split()).replace('|', r'\|')


def canonical(term):
    """A term's canonical wording, with blockquote markers stripped.

    `term:closure` is the one registry entry not written as a blockquote, so stripping is
    conditional per line rather than assumed for the whole block.
    """
    md = term.get('canonical_md')
    if not md:
        return '— registry entry; no canonical wording pinned'
    lines = [re.sub(r'^> ?', '', ln) for ln in str(md).split('\n')]
    return cell(' '.join(lines))


def main(path, repo, ref):
    claims, decisions, terms = load(repo, ref)
    text = open(path).read()
    body = text.split(HEADING)[0].split('## Appendix A')[0]

    cited_c = sorted(set(re.findall(r'DDD-[a-z]+-\d+', body)))
    cited_t = sorted(set(re.findall(r'term:[a-z-]+', body)))
    miss = [c for c in cited_c if c not in claims and c not in decisions]
    miss += [t for t in cited_t if t not in terms]
    if miss:
        sys.exit(f'cited but not in the graph at {ref}: {miss}')

    out = [HEADING, PREAMBLE, '### Claims', '',
           '| ID | Status | Statement |', '|---|---|---|']
    for c in [c for c in cited_c if c in claims]:
        y = claims[c]
        out.append(f"| `{c}` | {y.get('status')} | {cell(y.get('statement'))} |")

    out += ['', '### Decisions', '', '| ID | Statement |', '|---|---|']
    for c in [c for c in cited_c if c in decisions]:
        out.append(f"| `{c}` | {cell(decisions[c].get('statement'))} |")

    out += ['', '### Terms', '', '| ID | Term | Canonical wording |', '|---|---|---|']
    for t in cited_t:
        y = terms[t]
        out.append(f"| `{t}` | {y.get('term', t.split(':', 1)[1])} | {canonical(y)} |")

    hset = [c for c in cited_c if c in claims and (c.startswith('DDD-hyp-')
                                                   or c == 'DDD-frame-07')]
    if hset:
        out += ['', '### The hypothesis set, as the graph holds it', HSET_PREAMBLE,
                '| ID | Status | Evidence | Owner | Falsifier declared |', '|---|---|---|---|---|']
        for c in hset:
            y = claims[c]
            ev = y.get('evidence')
            out.append(f"| `{c}` | {y.get('status')} | "
                       f"{'`[]` (empty)' if ev in ([], None) else cell(ev)} | "
                       f"{y.get('owner')} | {'yes' if y.get('falsifier') else '**no**'} |")

    out += ['', f'*Generated from the graph at `{ref}`. '
                f'{len([c for c in cited_c if c in claims])} claims, '
                f'{len([c for c in cited_c if c in decisions])} decisions, '
                f'{len(cited_t)} terms.*', '']
    open(path, 'w').write(body.rstrip('\n') + '\n\n---\n\n' + '\n'.join(out))
    print(f'Appendix A generated: {len([c for c in cited_c if c in claims])} claims, '
          f'{len([c for c in cited_c if c in decisions])} decisions, {len(cited_t)} terms, '
          f'{len(hset)} hypothesis-set rows')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
