#!/usr/bin/env python3
"""Run the escape/wind experiment against an OpenAI-compatible endpoint.

Tiers:
  T0        query only (no document, no rules)
  T1        document + query (no rules)
  T2        document + rules(A) + query      — full allocation, phrasing A
  T2p       document + rules(B) + query      — same decisions, phrasing B
  T2pp      document + rules(C) + query      — same decisions, phrasing C
  T2-near / T2-mid / T2-far                  — T2 content under padding pressure

Usage:
  python run.py --base-url http://spark:8000/v1 --model Qwen/Qwen3.6-35B-A3B-FP8 \
      --items items.jsonl --tier T2 --k 5 --temperature 0.7 --out runs/
  python run.py ... --audit          # audit gate: single-fact/single-rule probes
"""
import argparse, hashlib, itertools, json, os, random, time
from pathlib import Path
import urllib.request

# --- three independently authored phrasings of the SAME decision set (P2) ---
RULE_PHRASINGS = {
    "A": lambda rules: "Rules:\n" + "\n".join(f"- {r}" for r in rules),
    "B": lambda rules: ("Before answering, apply these constraints in order. "
                        + " ".join(rules)),
    "C": lambda rules: ("CONSTRAINTS\n" + "\n".join(
        f"{i+1}. {r}" for i, r in enumerate(rules))
        + "\nAnswers violating any constraint are wrong."),
}

def call(base_url, model, prompt, temperature, seed, max_tokens=300):
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "seed": seed,
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(
        f"{base_url}/chat/completions", data=body,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        out = json.load(r)
    return out["choices"][0]["message"]["content"]

def build_prompt(item, tier, all_items, window_tokens, rng):
    doc, rules, query = item["document"], item["rules"], item["query"]
    if tier == "T0":
        return query
    if tier == "T1":
        return f"{doc}\n\n{query}"
    if tier in ("T2", "T2p", "T2pp"):
        ph = {"T2": "A", "T2p": "B", "T2pp": "C"}[tier]
        return f"{doc}\n\n{RULE_PHRASINGS[ph](rules)}\n\n{query}"
    if tier.startswith("T2-"):
        # pressure: inert distractors = other items' documents (no shared entities
        # by construction of the generator's random naming; verified in audit).
        fill_frac = {"T2-near": 0.05, "T2-mid": 0.65, "T2-far": 0.90}[tier]
        target_chars = int(window_tokens * 3.5 * fill_frac)  # ~3.5 chars/token
        others = [i["document"] for i in all_items if i["item_id"] != item["item_id"]]
        rng.shuffle(others)
        pad, size = [], 0
        for d in itertools.cycle(others):
            if size >= target_chars:
                break
            pad.append(d)
            size += len(d)
        block = "\n\n---\n\n".join(pad)
        if tier == "T2-near":
            return f"{block}\n\n---\n\n{doc}\n\n{RULE_PHRASINGS['A'](rules)}\n\n{query}"
        # mid/far: bury the target document in the middle of the padding
        half = len(pad) // 2
        head = "\n\n---\n\n".join(pad[:half])
        tail = "\n\n---\n\n".join(pad[half:])
        return (f"{head}\n\n---\n\n{doc}\n\n---\n\n{tail}\n\n"
                f"{RULE_PHRASINGS['A'](rules)}\n\n{query}")
    raise ValueError(tier)

def parse_json_answer(text):
    # tolerate fenced or embedded JSON; take the last {...} block
    depth, start, spans = 0, None, []
    for i, c in enumerate(text):
        if c == "{":
            if depth == 0:
                start = i
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0 and start is not None:
                spans.append(text[start:i + 1])
    for s in reversed(spans):
        try:
            return json.loads(s)
        except Exception:
            continue
    return None

def classify(ans, item):
    """escape | wind | correct | unclassifiable — per DESIGN.md."""
    truth = item["truth"]
    if ans is None:
        return "unclassifiable"
    uid, mw = ans.get("unit_id"), ans.get("output_mw")
    if uid == truth["unit_id"] and isinstance(mw, (int, float)) \
            and abs(mw - truth["output_mw"]) < 1e-6:
        return "correct"
    provided_ids = set(item["provided_ids"])
    provided_mw = ({round(v / 1000, 3) for v in item["provided_values"]}
                   | {float(v) for v in item["provided_values"]})  # kW-as-MW slip = wind
    id_provided = uid in provided_ids
    mw_provided = isinstance(mw, (int, float)) and any(
        abs(mw - p) < 1e-6 for p in provided_mw)
    if id_provided and mw_provided:
        return "wind"        # misassembled from provided material
    return "escape"          # material not derivable from the window: prior decided

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--items", default="items.jsonl")
    ap.add_argument("--tier", required=True)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--window-tokens", type=int, default=65536)
    ap.add_argument("--seed", type=int, default=20260708)
    ap.add_argument("--out", default="runs")
    ap.add_argument("--audit", action="store_true",
                    help="run single-fact/single-rule probes instead of the main task")
    args = ap.parse_args()

    items = [json.loads(l) for l in open(args.items)]
    rng = random.Random(args.seed)
    Path(args.out).mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%dT%H%M%S")
    tag = "audit" if args.audit else args.tier
    run_path = Path(args.out) / f"run-{tag}-{stamp}.jsonl"
    manifest = {
        "base_url": args.base_url, "model": args.model, "tier": args.tier,
        "k": args.k, "temperature": args.temperature, "seed": args.seed,
        "window_tokens": args.window_tokens, "audit": args.audit,
        "items_hash": hashlib.sha256(open(args.items, "rb").read()).hexdigest()[:16],
        "started": stamp,
    }

    records = []
    with open(run_path, "w") as f:
        f.write(json.dumps({"manifest": manifest}) + "\n")
        if args.audit:
            for item in items:
                for kind in ("facts", "rules"):
                    for p in item["audit_probes"][kind]:
                        ctx = item["document"] if kind == "facts" else \
                              RULE_PHRASINGS["A"](item["rules"])
                        raw = call(args.base_url, args.model,
                                   f"{ctx}\n\n{p['q']}", 0.0, args.seed)
                        ans = parse_json_answer(raw)
                        ok = ans == p["truth"] or (
                            ans and all(
                                abs(ans.get(k2, 1e9) - v) < 1e-6
                                if isinstance(v, (int, float)) else ans.get(k2) == v
                                for k2, v in p["truth"].items()))
                        rec = {"item_id": item["item_id"], "probe_kind": kind,
                               "ok": bool(ok), "raw": raw}
                        records.append(rec)
                        f.write(json.dumps(rec) + "\n")
            fails = [r for r in records if not r["ok"]]
            print(f"AUDIT: {len(records)-len(fails)}/{len(records)} probes pass. "
                  f"{len({r['item_id'] for r in fails})} items need repair/drop.")
            return

        for item in items:
            prompt = build_prompt(item, args.tier, items,
                                  args.window_tokens, rng)
            for s in range(args.k):
                raw = call(args.base_url, args.model, prompt,
                           args.temperature, args.seed + s)
                ans = parse_json_answer(raw)
                cls = classify(ans, item)
                rec = {"item_id": item["item_id"], "sample": s,
                       "class": cls, "answer": ans, "raw": raw}
                records.append(rec)
                f.write(json.dumps(rec) + "\n")

    from collections import Counter
    c = Counter(r["class"] for r in records)
    n = len(records)
    print(f"tier={args.tier}  n={n}")
    for k2 in ("correct", "escape", "wind", "unclassifiable"):
        print(f"  {k2:15s} {c[k2]:5d}  ({c[k2]/n:.1%})")
    print(f"raw log: {run_path}")

if __name__ == "__main__":
    main()
