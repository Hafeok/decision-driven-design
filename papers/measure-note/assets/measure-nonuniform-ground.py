"""
Non-uniform ground for "Specification Demand Is Verdict Entropy."
Re-runs the date task under skewed input distributions and verifies the identity

    H(V) = I(V;S) + H(V|S)

per deployment: same task, same code, same decompositions — demand moved by the
ground distribution alone. Exercises DDD-measure-12 (demand is relative to the
ground distribution) as a worked instance rather than a stated caveat.
Task and denomination (bits x n) as in measure-toy.py; entropies are exact
(weighted, exhaustive), nothing is sampled.

Run: python3 measure-nonuniform-ground.py
"""
from math import log2

# Task: validate (M, D). VALID iff D <= days_in_month(M).
days = {1: 31, 2: 28, 3: 31, 4: 30}
points = [(m, d) for m in days for d in range(1, 32)]
verdict = {(m, d): (d <= days[m]) for (m, d) in points}
n = len(points)

def H(pairs):
    """Shannon entropy (bits) of the verdict under weights [(weight, bool)]."""
    tot = sum(w for w, _ in pairs)
    p = sum(w for w, v in pairs if v) / tot
    if p == 0.0 or p == 1.0:
        return 0.0
    return -(p * log2(p) + (1 - p) * log2(1 - p))

def analyze(split, weight):
    """(parts, seam, whole) in bits x n under the weighted ground distribution."""
    all_pairs = [(weight(p), verdict[p]) for p in points]
    tot = sum(w for w, _ in all_pairs)
    Hv = H(all_pairs)
    groups = {}
    for p in points:
        groups.setdefault(split(p), []).append(p)
    Hc = 0.0
    for g in groups.values():
        pairs = [(weight(p), verdict[p]) for p in g]
        Hc += (sum(w for w, _ in pairs) / tot) * H(pairs)
    return n * Hc, n * (Hv - Hc), n * Hv

# Deployments: the ground distribution the task faces, nothing else varied.
deployments = [
    ("benign      (valid 9x invalid)", lambda p: 9.0 if verdict[p] else 1.0),
    ("uniform     (the worked example)", lambda p: 1.0),
    ("adversarial (invalid 9x valid)", lambda p: 1.0 if verdict[p] else 9.0),
]
splits = [("A: by month", lambda p: p[0]),
          ("B: by day<=28|>=29", lambda p: p[1] <= 28)]

print(f"n={n}  valid={sum(verdict.values())}  — demand under three ground distributions\n")
print(f"{'deployment':34s} {'H(V)':>8s}   {'decomposition':20s} "
      f"{'parts':>8s} {'seam':>8s} {'sum':>8s}")
for dname, w in deployments:
    for sname, s in splits:
        parts, seam, whole = analyze(s, w)
        assert abs(parts + seam - whole) < 1e-9
        print(f"{dname:34s} {whole:8.3f}   {sname:20s} "
              f"{parts:8.3f} {seam:8.3f} {parts+seam:8.3f}")
    print()

print("""The identity holds exactly in every deployment; what changes is the demand itself,
and where it sits. The same validator faces ~4x the uniform demand when invalid
inputs dominate and ~1/6 of it when they are rare, and the share a fixed
decomposition pre-pays into its seam moves with the deployment: B's seam carries
41% of the whole on the benign ground, 57% on the uniform, 75% on the adversarial.
'Fixed by the task' is fixed by the task, the tolerance, and the ground distribution.""")
