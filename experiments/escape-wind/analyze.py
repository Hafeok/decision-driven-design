#!/usr/bin/env python3
"""Read run logs and issue per-prediction verdicts.

  python analyze.py runs/ --margin 0.03

P1: error(T0) > error(T1) > error(T2), each step significant (two-prop z).
P2: T2 ≈ T2p ≈ T2pp by TOST within ±margin (declared before the run).
P3: escape-class rate rises T2-near → T2-mid → T2-far; wind-class rate does not.
"""
import argparse, glob, json, math
from collections import Counter, defaultdict

def load(runs_dir):
    tiers = defaultdict(list)
    for path in glob.glob(f"{runs_dir}/run-*.jsonl"):
        lines = [json.loads(l) for l in open(path)]
        man = lines[0]["manifest"]
        if man.get("audit"):
            continue
        tiers[man["tier"]].extend(lines[1:])
    return tiers

def rate(recs, pred):
    n = len(recs)
    k = sum(1 for r in recs if pred(r))
    return k, n, (k / n if n else float("nan"))

def two_prop_z(k1, n1, k2, n2):
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return 0.0, 1.0
    z = (k1 / n1 - k2 / n2) / se
    pval = math.erfc(abs(z) / math.sqrt(2))
    return z, pval

def tost(k1, n1, k2, n2, margin):
    """Two one-sided tests for equivalence of proportions within ±margin."""
    p1, p2 = k1 / n1, k2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2) or 1e-9
    d = p1 - p2
    z_low = (d + margin) / se     # H0: d <= -margin
    z_high = (d - margin) / se    # H0: d >= +margin
    p_low = math.erfc(z_low / math.sqrt(2)) / 2 if z_low > 0 else 1.0
    p_high = math.erfc(-z_high / math.sqrt(2)) / 2 if z_high < 0 else 1.0
    return d, max(p_low, p_high)  # equivalence if this p < .05

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs_dir")
    ap.add_argument("--margin", type=float, default=0.03,
                    help="P2 equivalence margin (declared pre-run)")
    args = ap.parse_args()
    tiers = load(args.runs_dir)

    err = lambda r: r["class"] in ("escape", "wind")
    esc = lambda r: r["class"] == "escape"
    wnd = lambda r: r["class"] == "wind"

    print("== rates ==")
    for t in sorted(tiers):
        k, n, p = rate(tiers[t], err)
        ke, _, pe = rate(tiers[t], esc)
        kw, _, pw = rate(tiers[t], wnd)
        u = sum(1 for r in tiers[t] if r["class"] == "unclassifiable")
        print(f"  {t:8s} err {p:6.1%} (escape {pe:5.1%} wind {pw:5.1%}) "
              f"n={n} unclassifiable={u} ({u/n:.1%})")
        if n and u / n > 0.15:
            print(f"    !! unclassifiable > 15% — redesign gate tripped for {t}")

    print("\n== P1: monotone decrease T0 > T1 > T2 ==")
    ok = True
    for a, b in [("T0", "T1"), ("T1", "T2")]:
        if a in tiers and b in tiers:
            ka, na, pa = rate(tiers[a], err)
            kb, nb, pb = rate(tiers[b], err)
            z, pv = two_prop_z(ka, na, kb, nb)
            step = pa > pb and pv < 0.05
            ok &= step
            print(f"  {a}->{b}: {pa:.1%} -> {pb:.1%}  z={z:.2f} p={pv:.4f} "
                  f"{'PASS' if step else 'FAIL'}")
    print(f"  P1 verdict: {'STANDS' if ok else 'FALLS'}")

    print(f"\n== P2: full-allocation equivalence (TOST ±{args.margin:.0%}) ==")
    ok = True
    for a, b in [("T2", "T2p"), ("T2", "T2pp"), ("T2p", "T2pp")]:
        if a in tiers and b in tiers:
            ka, na, _ = rate(tiers[a], err)
            kb, nb, _ = rate(tiers[b], err)
            d, pv = tost(ka, na, kb, nb, args.margin)
            eq = pv < 0.05
            ok &= eq
            print(f"  {a} vs {b}: diff={d:+.1%}  p_tost={pv:.4f} "
                  f"{'EQUIVALENT' if eq else 'NOT SHOWN EQUIVALENT'}")
    print(f"  P2 verdict: {'STANDS' if ok else 'FALLS (or underpowered — check n)'}")

    print("\n== P3: pressure raises escape-class, not wind-class ==")
    pres = [t for t in ("T2-near", "T2-mid", "T2-far") if t in tiers]
    if len(pres) >= 2:
        a, b = pres[0], pres[-1]
        for name, pred in (("escape", esc), ("wind", wnd)):
            ka, na, pa = rate(tiers[a], pred)
            kb, nb, pb = rate(tiers[b], pred)
            z, pv = two_prop_z(ka, na, kb, nb)
            rose = pb > pa and pv < 0.05
            print(f"  {name}: {a} {pa:.1%} -> {b} {pb:.1%}  z={z:.2f} p={pv:.4f} "
                  f"{'ROSE' if rose else 'no significant rise'}")
        print("  P3 stands iff escape ROSE and wind did not.")
    else:
        print("  (pressure tiers not yet run)")

if __name__ == "__main__":
    main()
