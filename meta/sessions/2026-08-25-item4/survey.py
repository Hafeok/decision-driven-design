#!/usr/bin/env python3
"""Item-4 survey: the kind x status table, and the two candidate I-2 checks.

Every count in gate1-survey.md is produced here. Run it to reproduce them.

    survey.py <upstream-repo> <downstream-repo>

The two candidate checks are run as *reports*, not as gates: nothing here exits
non-zero. Proposing a check as enforcing before its hit list is known is the
failure this script exists to prevent.
"""
import collections
import re
import sys
from pathlib import Path

import yaml

STATUSES = ["projected", "reported", "established", "retired"]
KINDS = ["conceptual", "empirical", "formal", "normative"]

# Mutual-information notation carries a semicolon -- I(V;X) -- and every such
# semicolon is a false positive for a clause-joining detector. Parentheticals are
# stripped before any limb counting; the difference the stripping makes is reported
# rather than hidden, because a detector's false-positive rate is the whole question.
PAREN = re.compile(r"\([^()]*\)")


def mask(s):
    s = " ".join(str(s).split())
    prev = None
    while prev != s:
        prev, s = s, PAREN.sub(" ", s)
    return re.sub(r"^RETIRED — ", "", s)


def load(repo, label):
    out = []
    for p in sorted((Path(repo) / "core/claims").glob("*.yaml")):
        c = yaml.safe_load(open(p))
        c["_repo"] = label
        out.append(c)
    return out


def table(claims, label):
    t = collections.Counter((c.get("kind"), c.get("status")) for c in claims)
    print(f"=== {label}: {len(claims)} claims ===")
    print(f"{'kind':<12}" + "".join(f"{s:>14}" for s in STATUSES) + f"{'total':>9}")
    for k in KINDS:
        row = [t.get((k, s), 0) for s in STATUSES]
        if not sum(row):
            continue
        print(f"{k:<12}" + "".join(f"{v:>14}" for v in row) + f"{sum(row):>9}")
    print(f"{'total':<12}"
          + "".join(f"{sum(t.get((k, s), 0) for k in KINDS):>14}" for s in STATUSES)
          + f"{len(claims):>9}")
    print(f"populated kind x status combinations: {len([1 for v in t.values() if v])}\n")


def check_a(claims):
    """Falsifier presence, at three strictnesses. Retired claims are exempt in all
    three: a retired node's statement is the epitaph, and an epitaph has no falsifier."""
    live = [c for c in claims if c.get("status") != "retired"]
    a1 = [c for c in live if not c.get("falsifier")
          and not (c.get("kind") in ("conceptual", "normative") and c.get("test"))]
    a2 = [c for c in live if not c.get("falsifier")]
    a0 = [c for c in claims if c.get("status") == "retired" and not c.get("falsifier")]
    print("########## CHECK A -- falsifier presence ##########")
    print(f"A1 lenient  (falsifier, or test for conceptual/normative; retired exempt): {len(a1)}")
    print(f"A2 strict   (falsifier on every live claim, test no substitute)         : {len(a2)}")
    print(f"   (retired claims lacking a falsifier, exempt under both               : {len(a0)})\n")
    print("A2 hit list:")
    for c in sorted(a2, key=lambda c: (c.get("status"), c["id"])):
        print(f"    {c['_repo']:<5}{c['id']:<18}{c.get('kind'):<11}{c.get('status'):<13}"
              f"test={'yes' if c.get('test') else 'NO'}")
    if a1:
        print("A1 hit list:")
        for c in a1:
            print(f"    {c['_repo']:<5}{c['id']:<18}{c.get('kind'):<11}{c.get('status')}")
    print()


def check_b(claims):
    """Rule 1 -- one proposition per claim. There is no mechanical test for 'one
    proposition'; what is counted here is clause-joining punctuation, which is a
    proxy and is reported as one."""
    rows = []
    for c in claims:
        raw = " ".join(str(c.get("statement", "")).split())
        m = mask(raw)
        rows.append((c, raw.count(";"), m.count(";"), len(re.findall(r",\s+and\s+", m))))
    b_raw = [r for r in rows if r[1] > 0]
    b1 = [r for r in rows if r[2] > 0]
    b2 = [r for r in rows if r[2] > 0 or r[3] > 0]
    print("########## CHECK B -- rule 1, single-limb statements ##########")
    print(f"B0 unmasked  semicolon anywhere                : {len(b_raw)}")
    print(f"B1 masked    semicolon outside math notation   : {len(b1)}")
    print(f"B2 masked    B1 or ', and '                    : {len(b2)}")
    fp = [r[0]["id"] for r in rows if r[1] > 0 and r[2] == 0]
    print(f"   false positives removed by masking ({len(fp)}): {', '.join(fp)}\n")
    print("B1 hit list:")
    for c, _, ms, _ in sorted(b1, key=lambda r: (STATUSES.index(r[0].get('status')), r[0]['id'])):
        print(f"    {c['_repo']:<5}{c['id']:<18}{c.get('kind'):<11}{c.get('status'):<13}"
              f"limbs~{ms + 1}")
    rat = [r for r in b1 if r[0].get("status") in ("reported", "established")]
    print(f"\nB1 fires on {len(rat)} reported/established claims:"
          f" {', '.join(r[0]['id'] for r in rat)}")
    print(f"B2 adds over B1: {len(b2) - len(b1)} further claims\n")


def main(up, down):
    u, d = load(up, "up"), load(down, "down")
    table(u, "upstream (actor-indexed-determination)")
    table(d, "downstream (decision-driven-design)")
    table(u + d, "combined corpus")
    print("upstream established claims: "
          + ", ".join(f"{c['id']} ({c['kind']})" for c in u if c.get("status") == "established")
          + "\n")
    check_a(u + d)
    check_b(u + d)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
