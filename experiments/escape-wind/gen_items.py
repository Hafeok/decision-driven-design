#!/usr/bin/env python3
"""Generate synthetic task items for the escape/wind experiment.

Every fact is invented (fictional entities, arbitrary values) so the prior
has no route to a correct answer except the window. Emits items.jsonl with,
per item: source document, decision rules, query, ground truth, and the
single-fact / single-rule audit probes.
"""
import argparse, hashlib, json, random, string

FIRST = ["Veylin", "Ostrek", "Maruni", "Teldova", "Quorast", "Brenniv",
         "Ashkell", "Doriveth", "Lunmark", "Serquin", "Havrelli", "Tovask"]
KIND = ["relay", "conduit", "manifold", "gantry", "lattice", "sluice"]
SITE = ["Kettle Ridge", "Fenwick Hollow", "Darrow Flats", "Ilsbeck",
        "Norrow Point", "Vantry Cross", "Millhaven East", "Ostwick Verge"]

RULES = {
    "tiebreak_low_id": "If two units share the same reading, report the one with the lower unit ID.",
    "unit_mw": "Report power in megawatts (MW). Source values are in kilowatts (kW); divide by 1000.",
    "scope_active": "Only units with status ACTIVE are in scope. Ignore all others.",
}

def mk_unit(rng):
    return {
        "id": f"U-{rng.randint(100,999)}",
        "name": f"{rng.choice(FIRST)} {rng.choice(KIND)}",
        "site": rng.choice(SITE),
        "status": rng.choice(["ACTIVE", "ACTIVE", "STANDBY", "FAULT"]),
        "reading_kw": rng.choice(range(1200, 9800, 100)),
    }

def render_doc(units, rng):
    lines = ["FIELD REPORT — distribution grid, cycle %d" % rng.randint(40, 90), ""]
    for u in rng.sample(units, len(units)):
        lines.append(f"Unit {u['id']} ({u['name']}) at {u['site']}: "
                     f"status {u['status']}, output reading {u['reading_kw']} kW.")
    return "\n".join(lines)

def mk_item(rng, idx):
    while True:
        units = [mk_unit(rng) for _ in range(rng.randint(5, 7))]
        ids = {u["id"] for u in units}
        if len(ids) == len(units):
            break
    active = [u for u in units if u["status"] == "ACTIVE"]
    if len(active) < 2:
        active_fix = rng.sample(units, 2)
        for u in active_fix:
            u["status"] = "ACTIVE"
        active = [u for u in units if u["status"] == "ACTIVE"]
    # force a tie among ACTIVE units on the max reading
    top = max(u["reading_kw"] for u in active)
    tied = rng.sample(active, 2)
    for u in tied:
        u["reading_kw"] = top
    winner = min(tied, key=lambda u: u["id"])
    truth_mw = round(top / 1000, 3)

    doc = render_doc(units, rng)
    query = ("Which in-scope unit has the highest output, and what is that "
             "output? Answer as JSON: {\"unit_id\": str, \"output_mw\": number}.")
    rules = [RULES["scope_active"], RULES["tiebreak_low_id"], RULES["unit_mw"]]

    audit_probes = {
        "facts": [
            {"q": f"What is the output reading in kW of unit {u['id']}? "
                  f"Answer as JSON: {{\"reading_kw\": number}}.",
             "truth": {"reading_kw": u["reading_kw"]}} for u in tied
        ] + [
            {"q": f"What is the status of unit {tied[0]['id']}? "
                  f"Answer as JSON: {{\"status\": str}}.",
             "truth": {"status": tied[0]["status"]}}
        ],
        "rules": [
            {"q": "Two ACTIVE units U-201 and U-105 both read 4000 kW. "
                  "Per the rules, which unit is reported? "
                  "Answer as JSON: {\"unit_id\": str}.",
             "truth": {"unit_id": "U-105"}},
            {"q": "A reading of 4500 kW is what value in MW? "
                  "Answer as JSON: {\"output_mw\": number}.",
             "truth": {"output_mw": 4.5}},
        ],
    }
    item = {
        "item_id": f"item-{idx:04d}",
        "document": doc,
        "rules": rules,
        "query": query,
        "truth": {"unit_id": winner["id"], "output_mw": truth_mw},
        "audit_probes": audit_probes,
        # material lists for the error classifier:
        "provided_values": sorted({u["reading_kw"] for u in units}),
        "provided_ids": sorted(ids),
    }
    item["item_hash"] = hashlib.sha256(
        json.dumps(item, sort_keys=True).encode()).hexdigest()[:16]
    return item

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=90)
    ap.add_argument("--seed", type=int, default=20260708)
    ap.add_argument("--out", default="items.jsonl")
    args = ap.parse_args()
    rng = random.Random(args.seed)
    with open(args.out, "w") as f:
        for i in range(args.n):
            f.write(json.dumps(mk_item(rng, i)) + "\n")
    print(f"wrote {args.n} items to {args.out} (seed={args.seed})")

if __name__ == "__main__":
    main()
