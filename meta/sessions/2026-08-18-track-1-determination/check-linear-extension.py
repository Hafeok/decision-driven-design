#!/usr/bin/env python3
"""Gate 3 linear-extension check for the determination track.

Constraint: no rung may require vocabulary a LATER rung introduces.

Method. Each upstream core doc declares a ddd:contract with `requires` and
`establishes`. That induces a dependency partial order over terms: term X
depends on term Y iff X's establishing doc requires Y, transitively closed.
The track introduces terms at rungs. The rung order is a linear extension of
that partial order iff, for every dependency X -> Y where BOTH are taught by
the track, Y's rung <= X's rung.

Claims are covered through the terms they are stated in: a claim cited at rung
n is checked as though it introduced nothing, since it mints no vocabulary.
"""
import re, sys, yaml
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/up-v570")

# --- the track's introductions, in rung order ------------------------------
INTRO = {
    "determinable": 1, "determinate": 1, "tolerance": 1,
    "decision": 2, "admission-test": 2, "governing-decision": 2,
    "ground": 3,
    "actor": 4, "arrangement": 4, "act": 4, "judgment": 4,
    "commitment-level": 5, "capability": 5,
    "residual-discretion": 6,
    "acceptance-predicate": 7, "closure": 7,
    "assurance": 8, "encoded": 8, "mechanical": 8,
    "escape": 9,
    "accountability": 10, "attribution": 10, "answerability": 10, "liability": 10,
}

CONTRACT = re.compile(r"<!--\s*ddd:contract\s*(.*?)-->", re.DOTALL)
FIELD = re.compile(r"^(requires|establishes)\s*:\s*(.*)$")

def key(t): return t.split("|")[0].strip().lower()

# --- read the contracts ----------------------------------------------------
establishes, requires_of_doc = {}, {}
docs = sorted((UP / "core").glob("[0-9][0-9]-*.md"))
for p in docs:
    m = CONTRACT.search(p.read_text(encoding="utf-8"))
    if not m: continue
    f = {"requires": [], "establishes": []}
    for line in m.group(1).splitlines():
        fm = FIELD.match(line.strip())
        if fm: f[fm.group(1)] = [key(t) for t in fm.group(2).strip("[]").split(",") if t.strip()]
    requires_of_doc[p.name] = f["requires"]
    for t in f["establishes"]: establishes[t] = p.name

# the two Track 1 mints are proposed upstream, established by core/14
for t in ("commitment-level", "residual-discretion"):
    establishes.setdefault(t, "14-indexed-determination.md")

# --- direct dependency: X depends on everything X's home doc requires -------
def deps(t):
    home = establishes.get(t)
    return set(requires_of_doc.get(home, [])) if home else set()

# transitive closure over all terms
closure = {t: set(deps(t)) for t in establishes}
changed = True
while changed:
    changed = False
    for t in closure:
        add = set()
        for d in closure[t]: add |= closure.get(d, set())
        if not add <= closure[t]:
            closure[t] |= add; changed = True

# --- the check -------------------------------------------------------------
violations, checked = [], 0
for x, rx in sorted(INTRO.items(), key=lambda kv: kv[1]):
    for y in sorted(closure.get(x, set())):
        if y not in INTRO: continue          # not taught by the track
        if y == x: continue
        checked += 1
        if INTRO[y] > rx:
            violations.append((x, rx, y, INTRO[y]))

print(f"terms introduced by the track : {len(INTRO)}")
print(f"core docs read                : {len(docs)}")
print(f"dependency pairs both-taught  : {checked}")
print()
for x, rx, y, ry in violations:
    print(f"  VIOLATION rung {rx} '{x}' depends on '{y}', introduced later at rung {ry}")
if violations:
    print(f"\nFAIL — {len(violations)} forward edge(s); the rung order is NOT a linear extension")
    sys.exit(1)
print("PASS — every dependency between track-taught terms points backward.")
print("The rung order is a linear extension of the canon dependency partial order.")

# --- how much freedom the constraint leaves --------------------------------
constrained = {(x, y) for x in INTRO for y in closure.get(x, set()) if y in INTRO and y != x}
print(f"\nThe constraint binds {len(constrained)} of the "
      f"{len(INTRO)*(len(INTRO)-1)//2} possible term pairs "
      f"({100*len(constrained)/(len(INTRO)*(len(INTRO)-1)//2):.0f}%). "
      "The rest of the order is free, which is why it is a decision.")
