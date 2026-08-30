#!/usr/bin/env python3
"""W1's occurrences in the two manuscripts, enumerated with their dispositions.

W1 renames the POPULATION sense of `ground` -- sense S5, "the population the task faces" -- to
`deployment distribution`. It touches no S1, S2 or S3 occurrence, and an occurrence ambiguous
between S5 and any other sense DEFERS to the migration rather than being ruled in a paper session.

The classification is NOT re-derived here. It is the ground-migration session's, execution-grade
and committed, read through w0-full-v2.json against the ground audit's own extract. What this
script adds is the disposition: not every S5 occurrence is W1's to move, and the exclusions are
the substance.

Four exclusions, each a reason a rename would assert something the session cannot:

  generated  a row in a table `gen-appendix.py` regenerates from the graph. Renaming it is
             hand-editing the appendix, which forges agreement the pin does not have.
  quotes     the passage reproduces a live claim's statement or a registry entry verbatim. Canon
             still says `ground distribution` at v5.12.0; renaming would make the paper misquote.
  identifier a filename. `measure-nonuniform-ground.py` is an asset in the principle repository
             and out of this session's reach. The audit's extract does not flag it; this does.
  ambiguous  S5 by the classification and three words from an S1 reading of the same phrase.

Usage:  w1-enumerate.py [<repo-root>]
Prints the enumeration and the counts the close report must use.
"""
import collections
import json
import os
import sys

TWO = ('papers/paper-a/paper-a.md', 'papers/measure-note/measure-note.md')

# Dispositions, keyed by (path, line). Every line the classification calls S5 in the two
# manuscripts appears exactly once; the script asserts that, so a drifted manuscript fails
# loudly rather than silently dropping an occurrence.
# Lines are the AUDIT EXTRACT's, and for paper-a.md three of them are stale by design rather
# than by error: the extract was taken at the ground audit (2026-08-24), and the item-4 session
# regenerated Appendix A the next day with a `kind` column, moving every appendix row down. The
# head line is carried beside the extract line so a reader can find the occurrence in the file,
# and the divergence is recorded rather than silently reconciled -- an enumeration that quietly
# renumbers is an enumeration whose input cannot be checked. measure-note.md did not move.
DISPOSITION = {
    ('papers/paper-a/paper-a.md', 502):  ('move-flagged', 502,  'ambiguous: "distribution of ground the task faces" (S5) vs "the ground the task faces" (S1)'),
    ('papers/paper-a/paper-a.md', 672):  ('move',         672,  ''),
    ('papers/paper-a/paper-a.md', 1365): ('defer',        1376, 'generated: Appendix A, DDD-measure-01'),
    ('papers/paper-a/paper-a.md', 1371): ('defer',        1382, 'generated: Appendix A, DDD-measure-11'),
    ('papers/paper-a/paper-a.md', 1409): ('defer',        1420, 'generated: Appendix A, term:verdict'),
}
_MN = 'papers/measure-note/measure-note.md'
for ln in (27, 41, 114, 129, 466, 493, 495, 601, 651, 713, 842, 899):
    DISPOSITION[(_MN, ln)] = ('move', ln, '')
DISPOSITION[(_MN, 482)] = ('move', 482, 'elliptical: rewrite, not a token swap')
DISPOSITION[(_MN, 22)] = ('move-flagged', 22, 'ambiguous: the "ground the task faces" pair')
DISPOSITION[(_MN, 88)] = ('move-flagged', 88, 'ambiguous: the "ground the task faces" pair')
DISPOSITION[(_MN, 464)] = ('move-flagged', 464, 'heading couples to upstream asset measure-nonuniform-ground.py')
for ln in (138, 484, 879):
    DISPOSITION[(_MN, ln)] = ('defer', ln, 'quotes: DDD-measure-12 statement, verbatim')
DISPOSITION[(_MN, 102)] = ('defer', 102, 'quotes: term:verdict definition, blockquoted')
DISPOSITION[(_MN, 923)] = ('defer', 923, 'identifier: measure-nonuniform-ground.py')
for ln in (1001, 1010, 1011, 1035):
    DISPOSITION[(_MN, ln)] = ('defer', ln, "quotes: the note's own node table")


def main(root='.'):
    ses = os.path.join(root, 'meta', 'sessions')
    rows = json.load(open(os.path.join(ses, '2026-08-24-ground-audit', 'classification.json')))
    sense = json.load(open(os.path.join(ses, '2026-08-27-ground-migration', 'w0-full-v2.json')))
    for i, r in enumerate(rows):
        r['s'] = sense[str(i)]

    s5 = [r for r in rows if r['s'] == 'S5']
    mutable = [r for r in s5 if not r['immutable']]
    print(f'S5 corpus-wide: {len(s5)}  immutable {len(s5) - len(mutable)}  '
          f'MUTABLE {len(mutable)}  mutable excl. product-cli '
          f'{sum(1 for r in mutable if r["repo"] != "product-cli")}')

    here = [r for r in mutable if r['repo'] == 'downstream' and r['path'] in TWO]
    print(f'in the two manuscripts: {len(here)} '
          f'{dict(collections.Counter(r["path"] for r in here))}')
    print(f'anywhere under papers/: '
          f'{sum(1 for r in mutable if r["repo"] == "downstream" and r["path"].startswith("papers/"))}')

    # L1011 carries two occurrences on one line; count rows, key dispositions by line.
    counts = collections.Counter()
    print()
    for r in sorted(here, key=lambda r: (r['path'], r['line'])):
        key = (r['path'], r['line'])
        if key not in DISPOSITION:
            sys.exit(f'UNRULED S5 occurrence {key} -- the manuscript moved under the enumeration')
        verdict, head_line, why = DISPOSITION[key]
        counts[verdict.split('-')[0]] += 1
        moved_line = '' if head_line == r['line'] else f' (head L{head_line})'
        print(f'  {verdict:13s} {r["path"].split("/")[-1]:16s} '
              f'L{r["line"]:<5d}{moved_line:<12s} {why}')

    print(f'\nMOVED {counts["move"]}   DEFERRED {counts["defer"]}   '
          f'of {sum(counts.values())} in the two manuscripts, of {len(mutable)} corpus-wide')
    print('The corpus-wide mutable total is 88. The two manuscripts hold '
          f'{len(here)} of it, which is {100 * len(here) // len(mutable)}% -- not 88%.')


if __name__ == '__main__':
    main(*sys.argv[1:])
