#!/usr/bin/env python3
"""Generate (or check) the primer's generated regions.

The primer is a projection: generated where it can be, pinned always, never hand-maintained
beside canon. This script fills the regions marked

    <!-- primer:generated id=NAME -->
    ...
    <!-- /primer:generated -->

in primer.md from the upstream tag that graph/upstream.yaml pins, plus this repository's own
claim register and meta/the-declaration.md, and writes a generation stamp as the file's last
line:

    <!-- primer:stamp pin=vX.Y.Z sha256=... -->

Two-stage verification, applied to this artefact's own tooling: `--check` FAILS when the stamp
is missing, when the stamp's pin differs from the pinned ref, or when any region's content
differs from a fresh generation. A primer whose generated blocks were never generated is
thereby distinguishable from one whose blocks pass.

Usage:
    python3 projections/primer/generate.py            # rewrite regions + stamp
    python3 projections/primer/generate.py --check    # verify, exit 1 on missing/stale
    python3 projections/primer/generate.py --upstream PATH   # local clone of the principle repo
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PRIMER = Path(__file__).resolve().parent / "primer.md"

# The terms the primer embeds, in the order their boxes may appear.
EMBED_TERMS = [
    "term:admission-test", "term:tolerance", "term:store",
    "term:act", "term:delivery",
    "term:floor", "term:closure",
    "term:escape", "term:escape-mechanism", "term:undelivered",
]

# §6's named research material: the claims whose content backs the primer's procedures or
# whose constructs a practitioner will meet elsewhere, listed with live status. Upstream ids
# are read at the pin; downstream ids at this repository's head.
NAMED_CLAIMS_UP = [
    "DDD-measure-01", "DDD-delivery-01", "DDD-delivery-02", "DDD-delivery-03",
    "DDD-ground-02", "DDD-ground-03", "DDD-floor-02", "DDD-measure-11", "DDD-measure-13",
]
NAMED_CLAIMS_DOWN = ["DDD-delivery-04", "DDD-cost-14", "DDD-cost-24"]


def pinned_ref() -> str:
    doc = yaml.safe_load((ROOT / "graph" / "upstream.yaml").read_text())
    return doc["upstream"]["ref"]


def git_show(upstream: Path, ref: str, path: str) -> str:
    return subprocess.run(
        ["git", "-C", str(upstream), "show", f"{ref}:{path}"],
        capture_output=True, text=True, check=True,
    ).stdout


def git_ls(upstream: Path, ref: str, path: str) -> list:
    out = subprocess.run(
        ["git", "-C", str(upstream), "ls-tree", "--name-only", ref, path + "/"],
        capture_output=True, text=True, check=True,
    ).stdout
    return [line for line in out.splitlines() if line.endswith(".yaml")]


def load_terms(upstream: Path, ref: str) -> dict:
    doc = yaml.safe_load(git_show(upstream, ref, "core/graph/terms.yaml"))
    terms = doc.get("terms", doc)
    return {(t.get("id") or t.get("term")): t for t in terms}


def load_claims_at_pin(upstream: Path, ref: str) -> list:
    claims = []
    for path in git_ls(upstream, ref, "core/claims"):
        claims.append(yaml.safe_load(git_show(upstream, ref, path)))
    return claims


def load_claims_local() -> list:
    claims = []
    for path in sorted((ROOT / "core" / "claims").glob("*.yaml")):
        if path.name == "README.md":
            continue
        claims.append(yaml.safe_load(path.read_text()))
    return claims


def term_box(terms: dict, tid: str, ref: str) -> str:
    t = terms[tid]
    body = t["canonical_md"].strip()
    caption = (f"— `{tid}` (registry status *{t.get('status', '?')}*, established by "
               f"`{t.get('established_by', '?')}`, at `{ref}`)")
    return f"{body}\n>\n> {caption}"


def declaration_region() -> str:
    """§A verbatim, then the §B-3 paragraph verbatim, from meta/the-declaration.md."""
    text = (ROOT / "meta" / "the-declaration.md").read_text()

    def blockquote_after(heading: str) -> str:
        idx = text.index(heading)
        lines, started = [], False
        for line in text[idx:].splitlines()[1:]:
            if line.startswith(">"):
                started = True
                lines.append(line)
            elif started:
                break
        return "\n".join(lines)

    a = blockquote_after("## A. The canonical text")
    b3 = blockquote_after("### B-3")
    return (f"{a}\n\n{b3}\n\n"
            f"*Carried verbatim from `meta/the-declaration.md` (§A and the §B-3 paragraph); "
            f"that file is the source and this block is generated from it.*")


def roster_region(up_claims: list, down_claims: list, ref: str) -> str:
    def counts(claims):
        table = {}
        for c in claims:
            area = c["id"].split("-")[1]
            table.setdefault(area, {})
            table[area][c["status"]] = table[area].get(c["status"], 0) + 1
        return table

    statuses = ["established", "reported", "projected", "retired"]
    lines = ["| Area | " + " | ".join(statuses) + " |",
             "|---|" + "---|" * len(statuses)]
    merged = {}
    for label, claims in (("up", up_claims), ("down", down_claims)):
        for area, ct in counts(claims).items():
            key = f"{area} ({'principle' if label == 'up' else 'projection'})"
            merged[key] = ct
    for key in sorted(merged):
        ct = merged[key]
        lines.append("| " + key + " | " +
                     " | ".join(str(ct.get(s, 0)) for s in statuses) + " |")
    total = len(up_claims) + len(down_claims)
    est = [c["id"] for c in up_claims + down_claims if c["status"] == "established"]
    head = (f"{total} claims at `{ref}` (principle) and this repository's head (projection). "
            f"`established` is {len(est)} claims, all `formal`: " +
            ", ".join(f"`{i}`" for i in sorted(est)) +
            ". A status is not a confidence score and does not aggregate.")

    by_id = {c["id"]: c for c in up_claims}
    by_id_down = {c["id"]: c for c in down_claims}
    named = ["", "The claims this primer's procedures lean on without asserting, by id:", "",
             "| Claim | Kind | Status |", "|---|---|---|"]
    for cid in NAMED_CLAIMS_UP:
        c = by_id[cid]
        named.append(f"| `{cid}` | {c['kind']} | `{c['status']}` |")
    for cid in NAMED_CLAIMS_DOWN:
        c = by_id_down[cid]
        named.append(f"| `{cid}` (projection) | {c['kind']} | `{c['status']}` |")
    return head + "\n\n" + "\n".join(lines) + "\n" + "\n".join(named)


def build_regions(upstream: Path, ref: str) -> dict:
    terms = load_terms(upstream, ref)
    up_claims = load_claims_at_pin(upstream, ref)
    down_claims = load_claims_local()
    regions = {
        "pin": (f"This primer describes canon at **`actor-indexed-determination {ref}`** — the "
                f"version `graph/upstream.yaml` pins. Generated blocks are drawn from that tag; "
                f"hand-written sections say so and carry the same pin in their own text."),
        "declaration": declaration_region(),
        "roster": roster_region(up_claims, down_claims, ref),
    }
    for tid in EMBED_TERMS:
        regions[tid] = term_box(terms, tid, ref)
    return regions


REGION_RE = re.compile(
    r"(<!-- primer:generated id=(?P<id>[^ ]+) -->\n)(?P<body>.*?)(<!-- /primer:generated -->)",
    re.DOTALL,
)
STAMP_RE = re.compile(r"<!-- primer:stamp pin=(?P<pin>[^ ]+) sha256=(?P<digest>[0-9a-f]{64}) -->\s*$")


def digest_of(regions: dict, ref: str) -> str:
    h = hashlib.sha256()
    h.update(ref.encode())
    for k in sorted(regions):
        h.update(k.encode())
        h.update(regions[k].encode())
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--upstream", type=Path,
                    default=ROOT.parent / "actor-indexed-determination")
    args = ap.parse_args()

    ref = pinned_ref()
    if not ref:
        print("FAIL: no pinned ref found in graph/upstream.yaml")
        return 1
    regions = build_regions(args.upstream, ref)
    text = PRIMER.read_text()

    used = set()

    def fill(m):
        rid = m.group("id")
        used.add(rid)
        if rid not in regions:
            raise SystemExit(f"FAIL: primer.md marks region '{rid}' the generator does not know")
        return m.group(1) + regions[rid] + "\n" + m.group(4)

    new_text = REGION_RE.sub(fill, text)
    missing = set(regions) - used
    if missing:
        print(f"FAIL: generator regions never placed in primer.md: {sorted(missing)}")
        return 1

    stamp = f"<!-- primer:stamp pin={ref} sha256={digest_of(regions, ref)} -->"
    stamped = STAMP_RE.sub("", new_text).rstrip() + "\n\n" + stamp + "\n"

    if args.check:
        m = STAMP_RE.search(text)
        if m is None:
            print("FAIL: no generation stamp — the primer's generated blocks were never "
                  "generated (a pass state must be distinguishable from a never-run state).")
            return 1
        if m.group("pin") != ref:
            print(f"FAIL: stamp pin {m.group('pin')} != pinned ref {ref}")
            return 1
        if m.group("digest") != digest_of(regions, ref):
            print("FAIL: stamp digest is stale — regenerate (a source the regions draw from "
                  "has changed).")
            return 1
        if new_text != text:
            print("FAIL: a generated region's content differs from a fresh generation.")
            return 1
        print(f"OK: stamp present, pin {ref}, all regions current.")
        return 0

    PRIMER.write_text(stamped)
    print(f"generated: {len(used)} regions at pin {ref}; stamp written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
