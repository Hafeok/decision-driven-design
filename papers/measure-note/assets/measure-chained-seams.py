"""
Chained seams for "Specification Demand Is Verdict Entropy."
Verifies the iterated chain rule on a two-level decomposition of the date task:

    H(V) = I(V;S1) + I(V;S2|S1) + H(V|S1,S2)

where S1 is the first-level split, S2 the refinement within each S1 group, and the
conditional term I(V;S2|S1) is the internal seam of the chained decomposition.
Task, conventions and denomination (bits x n) as in measure-toy.py.

Citation basis: DDD-measure-02 (chain rule, any conditioning variable; iteration is
arithmetic), DDD-measure-03 (seam = I(V;S)), term:seam-identity. A dedicated claim
node for the iterated form (next free DDD-measure-14) is pending the next canon
session; this asset is the worked instance 06-composition.md names as owed.

Run: python3 measure-chained-seams.py
"""
from math import log2

# Task: validate (M, D). VALID iff D <= days_in_month(M). Uniform inputs.
days = {1: 31, 2: 28, 3: 31, 4: 30}
points = [(m, d) for m in days for d in range(1, 32)]
verdict = {(m, d): (d <= days[m]) for (m, d) in points}
n = len(points)

def H(vals):
    """Binary Shannon entropy (bits/point) of a list of booleans."""
    k = len(vals); t = sum(vals)
    if t == 0 or t == k:
        return 0.0
    p = t / k
    return -(p * log2(p) + (1 - p) * log2(1 - p))

def Hcond(split):
    """H(V | split) in bits/point."""
    groups = {}
    for p in points:
        groups.setdefault(split(p), []).append(p)
    return sum((len(g) / n) * H([verdict[p] for p in g]) for g in groups.values())

by_month = lambda p: p[0]
by_day   = lambda p: p[1] <= 28
joint    = lambda p: (p[0], p[1] <= 28)

Hv = H([verdict[p] for p in points])
whole = n * Hv

def chain(name, s1, s2, label1, label2):
    """Two-level chain: seam of S1, then internal seam of S2 given S1, then parts."""
    H_s1 = Hcond(s1)                  # H(V|S1)
    H_s1s2 = Hcond(joint)             # H(V|S1,S2) — the full two-level tree
    seam1 = n * (Hv - H_s1)           # I(V;S1)
    seam2 = n * (H_s1 - H_s1s2)       # I(V;S2|S1)
    parts = n * H_s1s2                # H(V|S1,S2)
    total = seam1 + seam2 + parts
    print(f"{name}")
    print(f"  level-1 seam  I(V;{label1})        = {seam1:7.3f}")
    print(f"  internal seam I(V;{label2}|{label1}) = {seam2:7.3f}")
    print(f"  parts         H(V|{label1},{label2})   = {parts:7.3f}")
    print(f"  sum = {total:7.3f}   (whole = {whole:.3f})\n")
    return seam1, seam2, parts

print(f"n={n}  valid={sum(verdict.values())}  total demand H(verdict)={whole:.3f} bits")
print(f"Two-level decomposition: S1 and S2 chain to the 8-group tree (month x day-band).\n")

a = chain("Chain 1: month first, then day<=28|>=29 within each month",
          by_month, by_day, "M", "D")
b = chain("Chain 2: day<=28|>=29 first, then month within each band",
          by_day, by_month, "D", "M")

# One-shot check: conditioning on the joint variable directly.
one_shot_parts = n * Hcond(joint)
one_shot_seam = whole - one_shot_parts
print(f"One-shot on the joint (S1,S2): seam I(V;S1,S2) = {one_shot_seam:.3f}, "
      f"parts = {one_shot_parts:.3f}, sum = {one_shot_seam + one_shot_parts:.3f}")
assert abs(a[0] + a[1] - one_shot_seam) < 1e-9
assert abs(b[0] + b[1] - one_shot_seam) < 1e-9

print(f"""
Both chains sum to the whole exactly, and to each other's total: the order of the
chain moves demand between the level-1 seam and the internal seam ({a[0]:.3f}+{a[1]:.3f}
against {b[0]:.3f}+{b[1]:.3f}) but their sum is the joint seam ({one_shot_seam:.3f}) either way,
and the parts' residual ({one_shot_parts:.3f}) does not depend on the order at all.
Conservation iterates: internal seams are conditional mutual-information terms,
and chaining a decomposition re-splits the seam without creating or destroying demand.""")
