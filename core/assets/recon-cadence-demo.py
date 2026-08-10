#!/usr/bin/env python3
"""Recon cadence vs actor class — ground assurance substitution (all stipulated).
Exposure per act ~ lam*t*(1-d)*(1-c) <= eps  ->  t_max = eps/(lam*(1-d)*(1-c))"""
lam_drift, lam_adv = 0.002, 0.02      # ground corruption rate per day (drift / adversary)
c = 0.6                                # encoded ground-check coverage
eps = 0.001                            # alpha-implied per-act exposure bound
classes = {"rule (degenerate)": 0.0, "small": 0.3, "mid": 0.6, "frontier": 0.9, "specialist+cross-check": 0.97}
print(f"{'actor class':<26}{'d':>6}{'recon interval, drift':>24}{'under adversary':>18}")
for name, d in classes.items():
    t1 = eps/(lam_drift*(1-d)*(1-c)); t2 = eps/(lam_adv*(1-d)*(1-c))
    print(f"{name:<26}{d:>6.2f}{t1:>20.1f} d{t2:>16.2f} d")
