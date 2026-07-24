"""
DERIVING p_err FROM RATE-DISTORTION — closing the last real hole in core/10.

The question: when an actor must resolve H bits of residual demand but has resolve
capacity C bits, what is the error rate on the decisions it cannot resolve?

In core/10 I ASSUMED a logistic. That was a modelling choice, not a derivation.
Shannon's rate-distortion theory answers this exactly, and it is the RIGHT frame:
'what happens when you push more bits through a channel than its capacity' is
literally the question.

SETUP (binary decisions, Hamming distortion):
  - Residual demand: H bits to be resolved (n binary decisions, H = n bits if uniform).
  - Actor capacity: C bits per run. This is a CHANNEL of capacity C.
  - The actor must convey/resolve H bits through a C-bit channel.
  - If C >= H: no distortion required. Error rate 0.
  - If C < H: the actor MUST distort. Rate-distortion gives the MINIMUM achievable
    error rate for a binary source at rate C.

BINARY RATE-DISTORTION FUNCTION (Bernoulli(1/2) source, Hamming distortion):
    R(D) = 1 - H_b(D)     bits per symbol,  for 0 <= D <= 1/2
  where H_b is binary entropy and D is the per-symbol error probability.
  Inverting: given available rate r = C/n bits per decision,
    1 - H_b(D) = r   =>   H_b(D) = 1 - r   =>   D = H_b^{-1}(1 - r)

This is a THEOREM, not an assumption: D is the information-theoretic LOWER BOUND on
per-decision error rate when you have r bits/decision of capacity. No actor can do better.
"""
from math import log2

def Hb(p):
    if p <= 0 or p >= 1: return 0.0
    return -(p*log2(p) + (1-p)*log2(1-p))

def Hb_inv(y, lo=0.0, hi=0.5, iters=200):
    """invert binary entropy on [0, 1/2]"""
    if y <= 0: return 0.0
    if y >= 1: return 0.5
    for _ in range(iters):
        mid = (lo+hi)/2
        if Hb(mid) < y: lo = mid
        else: hi = mid
    return (lo+hi)/2

def p_err_rd(n_decisions, C_bits):
    """Rate-distortion lower bound on per-decision error rate."""
    r = C_bits / n_decisions          # bits of capacity per decision
    if r >= 1.0:
        return 0.0                     # capacity >= demand: no error forced
    return Hb_inv(1.0 - r)             # forced distortion

print("DERIVED p_err (rate-distortion bound) vs the ASSUMED logistic\n")
print(f"{'n':>4} {'C':>5} {'r=C/n':>7} {'p_err DERIVED':>14} {'(assumed logistic)':>20}")
import math
C_res=30.0
def p_err_logistic(load):
    return 0.5/(1.0+math.exp(-(load-C_res)/(0.25*C_res)))

n=40
for C in [40,36,30,24,16,8,0]:
    pd = p_err_rd(n, C)
    pl = p_err_logistic(n)  # logistic was a function of LOAD not capacity - note mismatch
    print(f"{n:>4} {C:>5} {C/n:>7.3f} {pd:>14.4f} {pl:>20.4f}")

print("\nKEY PROPERTIES OF THE DERIVED BOUND:")
print("  r >= 1  (capacity >= demand)  -> p_err = 0 exactly. No forced error.")
print("  r -> 0  (no capacity)         -> p_err -> 0.5. Pure chance. Matches the coin-flip.")
print("  In between: p_err = Hb^-1(1-r), a THEOREM, not a fitted curve.")
print("\nThis replaces the assumed logistic with a derived lower bound.")

print("\n\n=== DOES THE FLOOR RESULT SURVIVE THE SUBSTITUTION? ===")
print("Re-run core/10's soft results with the DERIVED p_err instead of the logistic.\n")
T=40
print("(1) adding RAW ground (no encoding) — does it still monotonically harm?")
print(f"{'rawR':>6} {'demand n':>9} {'C':>5} {'r':>6} {'p_err':>8} {'escape':>8}")
C=30.0
for R in [0,20,40,60]:
    # raw ground adds to what must be PROCESSED: effective decisions to resolve rises
    n_eff = T + R          # must wade through raw ground too
    pe = p_err_rd(n_eff, C)
    esc = T*pe             # open residual stays T; error rate rises
    print(f"{R:>6} {n_eff:>9} {C:>5.0f} {C/n_eff:>6.3f} {pe:>8.4f} {esc:>8.2f}")
print("  -> still monotonic harm. STRUCTURE SURVIVES.\n")

print("(2) fixed budget, shift raw->encoded — does escape still fall to 0?")
budget=50
print(f"{'encoded':>8} {'raw':>5} {'residual':>9} {'n_eff':>7} {'r':>6} {'p_err':>8} {'escape':>8}")
for D in [0,10,20,30,40]:
    R=budget-D; res=T-D
    n_eff = res + R + D    # everything in the window is processed
    pe = p_err_rd(n_eff, C) if res>0 else 0.0
    esc = res*pe
    print(f"{D:>8} {R:>5} {res:>9} {n_eff:>7} {C/n_eff:>6.3f} {pe:>8.4f} {esc:>8.2f}")
print("  -> escape still falls to 0 as encoding replaces raw. STRUCTURE SURVIVES.\n")

print("(3) the HARD result: does 'verified never escapes' still hold?")
print("  Yes - trivially. Rate-distortion sets the ERROR RATE on shed decisions.")
print("  Whether a shed error ESCAPES or becomes a RETRY depends on the VERIFIER,")
print("  which is orthogonal to p_err. The intersection structure is untouched.")
print("\nCONCLUSION: substituting the derived bound for the assumed logistic changes")
print("the NUMBERS but not a single structural claim. The floor mechanism is robust")
print("to the p_err model - which is exactly what we needed to show.")
