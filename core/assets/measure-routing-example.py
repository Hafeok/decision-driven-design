#!/usr/bin/env python3
"""
measure-routing-example.py — Worked example: routing one act by capability.

Exercises, in one arrangement: the act (one verdict), capability typing via the
admission test, per-capability residual and mechanical coverage, assurance
attachment (mechanism vs carrier), the max-over-vector class rule, the sign
flip (coverage investment lowering required class), retry economics, the
crossover volume N*, and the escape check (unchecked-property degradation).

STATUS: every quantity is STIPULATED. The example establishes that the routing
model is computable and non-degenerate and reproduces observed market behaviour
qualitatively (coding pinned to frontier; pin released by coverage, not model
progress). It establishes no correspondence to any measured arrangement.

The act: "implement a validated repository change from a filed ticket."
One act = one verdict of the merge acceptance predicate.
"""

# ---------------------------------------------------------------- the act
# Capability requirement derives from the admission test per ground type:
# required iff the verdict varies with ground accessible only through that
# pathway. Vision is included to show the test excluding.
# residual: bits/act the capability must resolve (stipulated)
# coverage: fraction of assurance alpha mechanically discharged on it
ACT = {
    #  capability        residual  coverage(today)   ground type
    "code-synthesis":   dict(r=12.0, cov=0.95),  # compiler + type system
    "tool-use":         dict(r=3.0,  cov=0.90),  # build/test runs self-verify
    "navigation":       dict(r=4.0,  cov=0.70),  # retrieval checks, link CI
    "architecture":     dict(r=8.0,  cov=0.15),  # conventions/intent: open
    "vision":           dict(r=0.0,  cov=1.00),  # verdict does not vary with
                                                 # visual ground -> excluded
}

# Class thresholds: uncovered assurance demand u = r*(1-cov) maps to the
# minimum actor class that may carry it where alpha attaches to the carrier.
def req_class(u):
    if u < 0.5:  return 0      # any actor
    if u < 2.0:  return 1      # small
    if u < 5.0:  return 2      # mid / specialised
    return 3                   # frontier or qualified human

CLASS_NAME = {0: "any", 1: "small", 2: "mid", 3: "frontier/qualified"}

# ------------------------------------------------------------- actor menu
# Per-capability class vector, per-act price, and per-try acceptance
# probability when operating at its capacity margin (for retry economics).
ACTORS = {
    "S  small":        dict(cls=dict(zip(ACT, [2,2,2,1,0])), price=4,   p=0.55),
    "M  code-mid":     dict(cls=dict(zip(ACT, [3,2,2,2,0])), price=20,  p=0.75),
    "F  frontier":     dict(cls=dict(zip(ACT, [3,3,3,3,2])), price=100, p=0.90),
}

def profile(coverage_overrides=None):
    ov = coverage_overrides or {}
    out = {}
    for cap, d in ACT.items():
        cov = ov.get(cap, d["cov"])
        u = d["r"] * (1 - cov)
        out[cap] = dict(r=d["r"], cov=cov, u=u, cls=req_class(u))
    return out

def binding(prof):
    req = {c: d["cls"] for c, d in prof.items() if d["r"] > 0}
    cap = max(req, key=req.get)
    return cap, req[cap], req

def route(prof):
    cap, cls, req = binding(prof)
    fits = {n: a for n, a in ACTORS.items()
            if all(a["cls"][c] >= k for c, k in req.items())}
    if not fits:
        return cap, cls, None, None
    name = min(fits, key=lambda n: fits[n]["price"] / fits[n]["p"])
    a = fits[name]
    return cap, cls, name, a["price"] / a["p"]   # expected cost incl. retries

def show(title, prof):
    print(f"\n=== {title} ===")
    print(f"{'capability':<16}{'residual':>9}{'coverage':>9}{'uncovered α':>12}{'min class':>22}")
    for c, d in prof.items():
        excl = "  (excluded by admission test)" if d["r"] == 0 else ""
        print(f"{c:<16}{d['r']:>9.1f}{d['cov']:>9.2f}{d['u']:>12.2f}"
              f"{CLASS_NAME[d['cls']]:>22}{excl}")
    cap, cls, name, cost = route(prof)
    print(f"binding capability: {cap} at class {cls} ({CLASS_NAME[cls]})")
    if name:
        print(f"route: {name} — expected cost {cost:.1f}/act (price/p, retries included)")
    else:
        print("route: no listed actor qualifies")
    return cost

# ---------------------------------------------------------------- states
print("Act: implement a validated repository change. One act = one verdict.")
cost_A = show("STATE A — today's coverage", profile())

cost_B = show("STATE B — architectural fitness functions raise arch coverage to 0.85",
              profile({"architecture": 0.85}))

show("STATE C — partial coverage investment (arch 0.50)",
     profile({"architecture": 0.50}))

# ------------------------------------------------- crossover for state B
L_COVERAGE = 3000.0   # standing cost of encoding the architectural checks
saving = cost_A - cost_B
n_star = L_COVERAGE / saving
print(f"\nCrossover: coverage investment L = {L_COVERAGE:.0f} against per-act "
      f"saving {saving:.1f}\n  N* = {n_star:.0f} acts — beyond this volume the "
      "coverage pays for the class drop.")

# ----------------------------------------------------- escape check
print("\nESCAPE CHECK — route S small in State A anyway:")
pA = profile()
s = ACTORS["S  small"]
for c, d in pA.items():
    if d["r"] > 0 and s["cls"][c] < d["cls"]:
        print(f"  {c}: uncovered α {d['u']:.1f} bits/act needs class {d['cls']}, "
              f"S carries class {s['cls'][c]} — the difference degrades WITHOUT "
              "SIGNAL (no check reaches it). Escape, not saving.")

# ----------------------------------------------------- rejection payloads
print("\nREJECTION-PAYLOAD LEVER (State B, actor S):")
for label, p in [("pass/fail verdict only", 0.35), ("rich rejection payload", 0.55)]:
    print(f"  {label:<26} p={p:.2f}  E[tries]={1/p:4.1f}  expected cost "
          f"{ACTORS['S  small']['price']/p:6.1f}/act")

print("\nStatus: all quantities stipulated. Computable and non-degenerate; "
      "reproduces the\nfrontier-pin on coding qualitatively. No correspondence "
      "to a measured arrangement is claimed.")
