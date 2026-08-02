#!/usr/bin/env python3
"""Validate claim files against the claim format spec (spec/claim-format.md).

Usage:
    validate-claims.py meta/seed/claims-seed.yaml     # single seed file with a claims: list
    validate-claims.py core/claims/                    # directory of per-claim YAML files
    validate-claims.py core/decisions/ --decisions     # directory of decision files (minimal checks)

Exit code 0 = valid; 1 = violations printed to stderr.
Implements format version 1. New format versions extend SUPPORTED_FORMATS
with their own rule set; claims validate against their declared version.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

SUPPORTED_FORMATS = {1}
STATUSES = {"projected", "reported", "established", "retired"}
KINDS = {"formal", "empirical", "conceptual", "normative"}
ID_RE = re.compile(r"^DDD-[a-z]+-\d{2}$")

errors = []


def err(where, msg):
    errors.append(f"  {where}: {msg}")


def check_claim(c, where, default_format=None):
    fmt = c.get("format", default_format)
    if fmt not in SUPPORTED_FORMATS:
        err(where, f"format missing or unsupported: {fmt!r}")
        return
    cid = c.get("id", "<no id>")
    where = cid
    if not ID_RE.match(cid):
        err(where, f"id does not match DDD-<area>-<nn>: {cid!r}")
    if c.get("kind") not in KINDS:
        err(where, f"kind missing or illegal: {c.get('kind')!r}")
    status = c.get("status")
    if status not in STATUSES:
        err(where, f"status missing or illegal: {status!r}")
        return
    if not c.get("statement"):
        err(where, "statement missing")
    if not c.get("region"):
        err(where, "region missing (rule 5: 'everywhere' must be written to be claimed)")
    if not c.get("changed"):
        err(where, "changed missing (staleness pin)")

    evidence = c.get("evidence") or []
    # Rule 2: status entry conditions
    if status in ("reported", "established") and not evidence:
        err(where, f"status '{status}' requires at least one evidence entry")
    if status == "established" and not any(
        e.get("kind") in ("derivation",) for e in evidence if isinstance(e, dict)
    ):
        err(where, "status 'established' requires a derivation evidence entry "
                   "(credits filled if the theorem is borrowed)")
    if status == "projected":
        if c.get("kind") in ("conceptual", "normative"):
            if not (c.get("test") or c.get("falsifier")):
                err(where, "projected conceptual/normative claim requires test (or falsifier)")
        elif not c.get("falsifier"):
            err(where, "projected claim requires falsifier")
    if status == "retired" and not (c.get("supersedes") or c.get("notes")):
        err(where, "retired claim requires supersedes or a notes entry naming what killed it")


def check_decision(d, where):
    """Minimal decision checks per ontology rule 1: no escaped decisions."""
    did = d.get("id", where)
    if not d.get("principal"):
        err(did, "decision has no accountable principal (escaped decision)")
    basis = d.get("basis") or d.get("basedOn") or []
    if not basis:
        err(did, "decision has no basedOn edges (escaped decision)")
    if not d.get("resolution"):
        err(did, "decision has no resolution")
    if not d.get("made"):
        err(did, "decision has no made timestamp/context")


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_decisions = "--decisions" in sys.argv
    if not args:
        sys.exit(__doc__)
    target = Path(args[0])

    items, default_format = [], None
    if target.is_dir():
        for p in sorted(target.glob("*.yaml")):
            data = load(p)
            items.append((data, str(p)))
    else:
        data = load(target)
        if isinstance(data, dict) and "claims" in data:
            default_format = data.get("format")
            items = [(c, target.name) for c in data["claims"]]
        elif isinstance(data, dict) and "decisions" in data:
            items = [(d, target.name) for d in data["decisions"]]
            as_decisions = True
        else:
            items = [(data, target.name)]

    ids = []
    for item, where in items:
        if as_decisions:
            check_decision(item, where)
        else:
            check_claim(item, where, default_format)
        if isinstance(item, dict) and item.get("id"):
            ids.append(item["id"])

    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        err("global", f"duplicate ids: {sorted(dupes)}")

    kind = "decisions" if as_decisions else "claims"
    if errors:
        print(f"INVALID — {len(errors)} violation(s) across {len(items)} {kind}:",
              file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"valid: {len(items)} {kind}, ids unique, format rules satisfied")


if __name__ == "__main__":
    main()
