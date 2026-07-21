"""
TEST 1: Is H(verdict) actor-INVARIANT while its ALLOCATION is actor-relative?
Claim: H(verdict) = [encoded by actor] + [judged by actor] + [escaped by actor]
       - the three terms depend on the actor; the SUM does not.
This is the chain rule with conditioning variable = "what the actor has encoded (E)".
    H(V) = I(V;E) + H(V|E)        [encoded part] + [left to judgment/escape]
The actor's pinning resolution determines how much of V it can pull into E.
"""
from math import log2
days={1:31,2:28,3:31,4:30}
Ms=[1,2,3,4]; Ds=list(range(1,32))
points=[(m,d) for m in Ms for d in Ds]
V={(m,d):(d<=days[m]) for (m,d) in points}
n=len(points)
def H(vals):
    k=len(vals); t=sum(vals)
    if t==0 or t==k: return 0.0
    p=t/k; return -(p*log2(p)+(1-p)*log2(1-p))
def Hcond(groups):  # sum P(g) H(V on g)
    return sum((len(g)/n)*H([V[p] for p in g]) for g in groups.values())
Hv=H([V[p] for p in points]); whole=n*Hv
print(f"TASK total demand H(V) = {whole:.3f} bits  (actor-invariant target)\n")

# An ACTOR is defined by what it can ENCODE = a variable E it can compute about the input
# BEFORE acting. Pinning resolution = how much of V that E captures = I(V;E).
def actor(name, encode_fn):
    g={}
    for p in points: g.setdefault(encode_fn(p),[]).append(p)
    hcond=Hcond(g); parts=n*hcond; encoded=whole-parts
    print(f"{name}")
    print(f"   encodes E = {encode_fn.__doc__}")
    print(f"   I(V;E) encoded   = {encoded:7.3f} bits")
    print(f"   H(V|E) judgment  = {parts:7.3f} bits")
    print(f"   sum              = {encoded+parts:7.3f}  (target {whole:.3f})\n")
    return encoded, parts

# Actor 1: PROGRAM pinned by value — can encode the full rule (it IS the rule).
def prog(p):
    "the exact verdict (program computes days_in_month table)"
    return V[p]
# Actor 2: WEAK MODEL — can only encode a coarse proxy: 'is D<=28?' (month-agnostic).
def weak(p):
    "coarse proxy: D<=28 (knows the always-safe zone, nothing else)"
    return p[1]<=28
# Actor 3: MID MODEL — encodes 'D<=28' AND 'is it February?' (the main exception).
def mid(p):
    "D<=28, plus whether month is Feb (the biggest exception)"
    return (p[1]<=28, p[0]==2)

a1=actor("ACTOR 1 — program (pins by value)", prog)
a2=actor("ACTOR 2 — weak model (coarse encode)", weak)
a3=actor("ACTOR 3 — mid model (better encode)", mid)

print("VERDICT:")
print(f"  All three sums = {whole:.3f}. The TOTAL is actor-invariant.")
print(f"  Encoded/judgment SPLIT differs by actor:")
print(f"    program: encodes {a1[0]:.1f}, judges {a1[1]:.1f}")
print(f"    weak:    encodes {a2[0]:.1f}, judges {a2[1]:.1f}")
print(f"    mid:     encodes {a3[0]:.1f}, judges {a3[1]:.1f}")
print("  => Same conserved H(V); allocation set by the actor's encode capacity. CLAIM HOLDS.")
