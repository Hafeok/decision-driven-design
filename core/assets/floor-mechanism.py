"""
Reproduction script for core/10 — The Floor Mechanism.
Two regimes: hard capacity (the intersection result) and soft capacity (the encode-fraction law).
stdlib only. Run: python3 floor_mechanism.py
"""
import random, math
random.seed(3)

# ---------------------------------------------------------------------------
# HARD CAPACITY: escape requires BOTH overflow AND open (no verifier).
# ---------------------------------------------------------------------------
def hard(n_A, n_B, C, trials=4000):
    """n_A verified (closing), n_B unverified (open). C = bits resolved cleanly/run."""
    total = n_A + n_B
    esc_B = retries = 0
    for _ in range(trials):
        overflow = max(0, total - C)
        idx = list(range(total)); random.shuffle(idx)
        shed = set(idx[:overflow])
        for i in range(total):
            if i in shed and random.random() < 0.5:      # shed -> coin flip -> wrong
                if i < n_A: retries += 1                  # verified: caught -> retry
                else:       esc_B += 1                    # open: survives -> escape
    return esc_B/trials, retries/trials

print("HARD CAPACITY — escape only at the intersection (overflow AND open)")
print(f"{'C':>4} {'overflow':>9} {'escape(open)':>13} {'retries(closing)':>17}")
for C in [40,30,24,16,0]:
    eB,rt = hard(20,20,C); ov=max(0,40-C)
    print(f"{C:>4} {ov:>9} {eB:>13.3f} {rt:>17.3f}")
print("  all-verified (n_B=0): escape is 0 at every C -> overflow alone = retries, not floor")
eB,_ = hard(40,0,0); print(f"    check: all-verified at C=0 -> escape={eB:.3f}\n")

# ---------------------------------------------------------------------------
# SOFT CAPACITY: escape = open_residual * p_err(load). Raw ground harms; encoding helps.
# ---------------------------------------------------------------------------
C_resolve=30.0; T=40
def p_err(load):
    return 0.5/(1.0+math.exp(-(load-C_resolve)/(0.25*C_resolve)))

print("SOFT CAPACITY — escape = open_residual * p_err(total load)")
print(" (1) adding RAW ground (no encoding): monotonic harm")
print(f"     {'rawR':>5} {'load':>6} {'p_err':>7} {'escape':>7}")
for R in [0,20,40,60]:
    load=R+T; print(f"     {R:>5} {load:>6.0f} {p_err(load):>7.3f} {T*p_err(load):>7.2f}")
print(" (2) fixed budget=50, shift raw->encoded: escape -> 0 (the product-cli fix)")
print(f"     {'encoded':>7} {'residual':>9} {'load':>6} {'escape':>7}")
for D in [0,10,20,30,40]:
    R=50-D; res=T-D; load=R+D+res
    print(f"     {D:>7} {res:>9} {load:>6.0f} {res*p_err(load):>7.2f}")
print("\n  Lever is ENCODE FRACTION, not context size. Raw ground past capacity is pure harm.")
