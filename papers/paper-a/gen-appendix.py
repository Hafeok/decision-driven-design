#!/usr/bin/env python3
"""Generate Appendix A for Paper A, wholesale, from the claim graph.

Appendix A is generated and never hand-edited. Regenerating both tables from
`core/claims/`, `core/decisions/` and `core/graph/terms.yaml` makes every row verbatim by
construction, and corrects drifted rows in the same pass that adds new ones. The rendered
result is then re-read against the graph by a separate script, `check-appendix.py`, so the
check is independent of the generator that produced it.

Usage:  gen-appendix.py <manuscript.md> <upstream-repo> <ref>
Rewrites everything from the `## Appendix A` heading to end of file.

Defect history, kept with the instrument:

  * First version was not idempotent: it appended a horizontal rule to a body that already
    ended with the rule preceding the appendix, so a second run added a second rule. A
    convention that says "regenerate wholesale" must survive being run twice, and this one
    did not. Fixed by stripping trailing rules from the body first; idempotence is now
    checked by running three times and comparing bytes.

  * The claims table rendered `id | status | statement` and no kind, for five minor versions.
    `kind` has been populated on every claim since format 1, so this was never a schema gap --
    an external reader inferred one from the appendix and reported the registry as missing a
    field it has always had. A projection defect reads as a schema defect when the projection
    is the only view a reader has. Adding the column changes the table's shape, so
    `check-appendix.py` was updated in the same commit; see its own defect history for why
    that could not wait.
"""
import re
import subprocess
import sys

import yaml

HEADING = '## Appendix A. Cited claims, decisions and terms'

PREAMBLE = """
The paper cites nodes in the framework's claim graph. Statements below are reproduced
word-for-word from the graph at the ref pinned in the front matter, so the paper can be checked
without it. **Kind** and **status** are the graph's own fields, and they answer different questions.
*Kind* is what sort of claim it is: *formal* is arithmetic or a derivation, *empirical* rests on
observation, *conceptual* fixes or uses the framework's vocabulary, *normative* says what ought to
be done. *Status* is how far it has been argued: *settled* and *established* are argued and
unchallenged **within this framework**, *reported* is exercised by a reproducing computation,
*projected* is proposed with a declared falsifier and not yet met, *draft* is filed and not yet
ratified, *retired* is superseded and kept with the correction that killed it.

**Neither field claims external validation, and the two must be read together.** *Established*
means internally argued and unchallenged, not empirically confirmed; *reported* means a computation
runs and reproduces, not that the world was consulted. The pairing is what carries the information:
every *established* claim in this graph is *formal*, so what is settled here is arithmetic, and the
modelling claims that give the arithmetic its meaning are *projected*. The canonical statement of
what each value means, and what it does not, is `spec/claim-format.md` §5 at the pinned ref; this
paragraph projects it and does not replace it.

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

    # Kind and status are rendered together because either alone misleads. A reader who
    # sees `established` and not `formal` reads a claim about the world as confirmed; the
    # pair says it is arithmetic. The column is the graph's own field, populated since
    # format 1 -- what was missing was the rendering, not the data.
    out = [HEADING, PREAMBLE, '### Claims', '',
           '| ID | Kind | Status | Statement |', '|---|---|---|---|']
    for c in [c for c in cited_c if c in claims]:
        y = claims[c]
        out.append(f"| `{c}` | {y.get('kind')} | {y.get('status')} | {cell(y.get('statement'))} |")

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
    # The body already ends with the rule that preceded the appendix. Appending another would
    # make the generator non-idempotent -- a second run would add a second rule, and a convention
    # that says "regenerate wholesale" must survive being run twice.
    body = body.rstrip('\n')
    while body.endswith('---'):
        body = body[:-3].rstrip('\n')
    open(path, 'w').write(body + '\n\n---\n\n' + '\n'.join(out))
    print(f'Appendix A generated: {len([c for c in cited_c if c in claims])} claims, '
          f'{len([c for c in cited_c if c in decisions])} decisions, {len(cited_t)} terms, '
          f'{len(hset)} hypothesis-set rows')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
