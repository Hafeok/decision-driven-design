"""
Find the CORRECT ordering rule. This is a classic scheduling problem.
waste = sum_i rate_i * (sum of lengths AFTER i)
Exchange argument: compare adjacent pair (A then B) vs (B then A).
  A then B: A contributes rate_A * (len_B + rest), B contributes rate_B * rest
  B then A: B contributes rate_B * (len_A + rest), A contributes rate_A * rest
  Difference (AthenB - BthenA) = rate_A*len_B - rate_B*len_A
  So A before B iff rate_A*len_B < rate_B*len_A  iff  rate_A/len_A < rate_B/len_B
=> SORT BY ASCENDING (rate / length).  Not ascending rate.
This is Smith's rule / the weighted-shortest-processing-time ordering.
"""
from itertools import permutations
def waste(order):
    return sum(rate*sum(s[1] for s in order[i+1:]) for i,(n,ln,rate) in enumerate(order))

def check(segs, label):
    res = sorted(((waste(p),[s[0] for s in p]) for p in permutations(segs)))
    by_rate  = sorted(segs, key=lambda s: s[2])
    by_ratio = sorted(segs, key=lambda s: s[2]/s[1])   # rate / length
    print(f"\n{label}")
    print(f"  brute-force optimum : {' -> '.join(res[0][1])}   waste={res[0][0]:.2f}")
    print(f"  ascending rate      : {' -> '.join(s[0] for s in by_rate)}   waste={waste(by_rate):.2f}  match={res[0][1]==[s[0] for s in by_rate]}")
    print(f"  ascending rate/len  : {' -> '.join(s[0] for s in by_ratio)}   waste={waste(by_ratio):.2f}  match={res[0][1]==[s[0] for s in by_ratio]}")

check([("ground",1000,0.01),("decisions",400,0.10),("examples",300,0.30),("task",100,1.00)],
      "CASE 1 — typical (stable content is long, volatile is short)")
check([("ground",100,0.01),("decisions",100,0.10),("task",5000,1.00)],
      "CASE 2 — stress (volatile segment is huge)")
check([("a",50,0.5),("b",500,0.6),("c",20,0.05),("d",900,0.9)],
      "CASE 3 — random mix")
check([("g",2000,0.001),("d",300,0.05),("ex",800,0.4),("t",150,1.0)],
      "CASE 4 — realistic prefix")
