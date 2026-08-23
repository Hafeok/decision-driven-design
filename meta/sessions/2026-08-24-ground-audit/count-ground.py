#!/usr/bin/env python3
"""Enumerate every occurrence of `ground` and its morphological variants.

Counting method, stated so the count is checkable rather than trusted:

  * The pattern is  (?i)\bground\w*  — a word boundary before "ground", then any
    word characters after it. The leading \b is what excludes "background",
    "underground", "foreground" and "playground": in those the preceding
    character is a word character, so no boundary exists and no match fires.
    Those exclusions are counted separately and reported, so the exclusion is
    auditable rather than asserted.
  * Hyphenated compounds DO match — "adversarial-ground", "ground-cli",
    "ground-axes" — because a hyphen is a word boundary. That is deliberate:
    a crate directory named ground-cli is an occurrence the migration pays for.
  * Every match is bucketed by the exact token matched, so "ground", "grounds",
    "grounded" and "grounding" are never silently merged.
  * Binary files and .git are skipped. Nothing is sampled; every text file in
    every named artefact class is read whole.
"""
import os, re, sys, json, collections

# Corrected pattern. The first version used \bground\w*, and its own exclusion
# report showed the defect: `parse_ground`, `ground_provenance` inside a longer
# identifier, and a dozen snake_case Rust test names were being thrown away as
# "false positives". They are not false positives. In regex, `_` is a WORD
# character, so \b does not fire between `parse_` and `ground` — the pattern
# silently under-counted every snake_case identifier, which is most of the
# software surface. The boundary is therefore stated explicitly as "not a letter
# and not a digit", which makes `_` a boundary while still excluding
# "background", "underground", "foreground" and "playground".
TOKEN = re.compile(r'(?i)(?<![A-Za-z0-9])ground[A-Za-z0-9_]*')
EXCLUDED = re.compile(r'(?i)[A-Za-z0-9]+ground[A-Za-z0-9_]*')

# Escaped newlines inside source string literals hide occurrences: a Rust test
# holding embedded YAML as "tolerance_floor: T1\\nground: characterised" puts an
# `n` immediately before `ground`, so no boundary fires. Unescaping \n, \t and \r
# to whitespace before matching recovers them; four such occurrences exist in
# product-cli's ledger-core, all of them the real YAML field name `ground:`.
UNESCAPE = re.compile(r'\\[ntr]')

# The audit's own output is excluded from the counts it produces. Its instrument
# quotes the regex `\bground\w*` in its own docstring, and counting that would
# mean the audit inflating its own subject.
SELF = os.path.join('meta', 'sessions', '2026-08-24-ground-audit')

SKIP_DIRS = {'.git', 'target', 'node_modules', '.venv', '__pycache__', 'dist'}
TEXT_EXT = {'.md','.yaml','.yml','.py','.rs','.toml','.json','.txt','.ttl','.sh',
            '.jsx','.js','.ts','.tsx','.css','.html','.sql','.cfg','.ini',''}

def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext and ext not in TEXT_EXT:
                continue
            yield os.path.join(dirpath, fn)

def count(root, label):
    per_file = {}
    tokens = collections.Counter()
    excluded = collections.Counter()
    path_hits = []
    for p in walk(root):
        rel = os.path.relpath(p, root)
        if rel.startswith(SELF):
            continue
        # the path itself is an occurrence if a path component matches
        for comp in rel.split(os.sep):
            if TOKEN.search(comp):
                path_hits.append(rel)
                break
        try:
            text = open(p, encoding='utf-8', errors='strict').read()
        except (UnicodeDecodeError, OSError):
            continue
        text = UNESCAPE.sub(' ', text)
        ms = TOKEN.findall(text)
        for m in EXCLUDED.findall(text):
            excluded[m.lower()] += 1
        if ms:
            per_file[rel] = len(ms)
            for m in ms:
                tokens[m.lower()] += 1
    return {'label': label, 'root': root, 'per_file': per_file, 'tokens': dict(tokens),
            'total': sum(per_file.values()), 'files': len(per_file),
            'excluded': dict(excluded), 'path_hits': sorted(set(path_hits))}

if __name__ == '__main__':
    out = {}
    for root, label in [(sys.argv[i], sys.argv[i+1]) for i in range(1, len(sys.argv), 2)]:
        out[label] = count(root, label)
    print(json.dumps(out, indent=1, sort_keys=True))
