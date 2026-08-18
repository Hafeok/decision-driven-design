#!/usr/bin/env python3
"""Self-containment check: does any rung's prose USE a term a later rung introduces?

This is the weaker, document-level reading of the constraint — the one stated in
projections/tracks/README.md ("no rung may need a term a later rung introduces").
It is checked against the track text itself, not against canon's contracts.
"""
import re, sys
from pathlib import Path

INTRO = {
    "determinable":1,"determinate":1,"tolerance":1,
    "decision":2,"admission test":2,"governing decision":2,
    "ground":3,
    "actor":4,"arrangement":4,"act":4,"judgment":4,
    "commitment level":5,"capability":5,
    "residual discretion":6,
    "acceptance predicate":7,"closure":7,
    "assurance":8,"encoded":8,"mechanical":8,
    "escape":9,
    "accountability":10,"attribution":10,"answerability":10,"liability":10,
}
# words too common in ordinary English to test as vocabulary uses
SKIP = {"decision","ground","act","actor","tolerance","closure","mechanical","encoded"}

# Declared forward pointers, listed in the track's manifest. Canon's own W1 is a WARNING,
# not an error, and canon carries 59 of them at v5.7.0 under the same discipline: a forward
# use is a defect only when it is undeclared. Each entry here passes the deletion test —
# removing the word would misquote canon (rungs 3, 5) or blunt the rung (rung 8).
DECLARED = {(3, "assurance"), (5, "assurance"), (8, "escape")}

text = Path(sys.argv[1]).read_text(encoding="utf-8")
# split into rungs
parts = re.split(r"\n## Rung (\d+)", text)
rungs = {}
for i in range(1, len(parts), 2):
    rungs[int(parts[i])] = parts[i+1]

hits = declared = 0
for r in sorted(rungs):
    body = rungs[r]
    for term, ri in INTRO.items():
        if ri <= r or term in SKIP: continue
        pat = re.compile(r"\b" + term.replace(" ", r"[-\s]") + r"(?:e?s)?\b", re.I)
        for m in pat.finditer(body):
            ctx = body[max(0,m.start()-60):m.end()+40].replace("\n"," ")
            if (r, term) in DECLARED:
                declared += 1
                print(f"  declared  rung {r} uses '{m.group(0)}' (introduced rung {ri})")
            else:
                hits += 1
                print(f"  UNDECLARED  rung {r} uses '{m.group(0)}' (introduced rung {ri})  …{ctx}…")
print(f"\nrungs scanned: {len(rungs)}   declared forward pointers: {declared}   "
      f"undeclared forward uses: {hits}")
print("(terms too common in ordinary English are excluded: " + ", ".join(sorted(SKIP)) + ")")
if hits:
    print("\nFAIL — an undeclared forward use is an escaped edge; declare it or remove it.")
    sys.exit(1)
print("PASS — every forward use is declared in the track's manifest.")
