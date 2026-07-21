"""
Worked example for "An Information-Theoretic Account of Specification Demand."
Verifies: H(verdict) = H(verdict|S) + I(verdict;S) for two decompositions of a
date-validation task. Conservation of specification demand = the chain rule of entropy.
Run: python3 measure-toy.py
"""
from math import log2

# Task: validate (M, D). VALID iff D <= days_in_month(M). Uniform inputs.
days = {1: 31, 2: 28, 3: 31, 4: 30}
Ms = [1, 2, 3, 4]
Ds = list(range(1, 32))
points = [(m, d) for m in Ms for d in Ds]
verdict = {(m, d): (d <= days[m]) for (m, d) in points}
n = len(points)

def H(vals):
    """Binary Shannon entropy (bits/point) of a list of booleans."""
    k = len(vals); t = sum(vals)
    if t == 0 or t == k:
        return 0.0
    p = t / k
    return -(p * log2(p) + (1 - p) * log2(1 - p))

Hv = H([verdict[p] for p in points])          # bits per point
whole = n * Hv                                  # total demand, bits

def analyze(name, split):
    groups = {}
    for p in points:
        groups.setdefault(split(p), []).append(p)
    Hcond = sum((len(g) / n) * H([verdict[p] for p in g]) for g in groups.values())
    I = Hv - Hcond
    parts, seam = n * Hcond, n * I
    print(f"{name:28s} groups={len(groups)}  "
          f"parts H(V|S)={parts:7.3f}  seam I(V;S)={seam:7.3f}  "
          f"sum={parts+seam:7.3f}  (whole={whole:.3f})")

print(f"n={n}  valid={sum(verdict.values())}  total demand H(verdict)={whole:.3f} bits\n")
analyze("A: split by month",       lambda p: p[0])
analyze("B: split by day<=28|>=29", lambda p: p[1] <= 28)
print("\nBoth sum to the whole exactly: conservation is the chain rule of entropy.")
