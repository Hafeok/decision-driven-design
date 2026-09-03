#!/usr/bin/env python3
"""Gate 4 independent quotation check for the primer.

Deliberately NOT generate.py: a separate extraction path, so a defect shared between the
generator's write and check modes cannot vouch for itself. Verifies:

  1. every `primer:generated id=term:*` region quotes its term's canonical_md at the pinned
     tag verbatim (the caption line is the region's own addition and is excluded);
  2. the declaration region carries meta/the-declaration.md's §A blockquote and §B-3
     paragraph byte-for-byte (the provenance line is the region's own addition);
  3. no blockquote line exists in primer.md OUTSIDE a generated region — i.e. every quoted
     node in the primer is generated, which is what makes 1 and 2 exhaustive.

Usage: g4-quote-check.py <primer.md> <upstream-repo> <ref> <declaration.md>
"""
import re, subprocess, sys, yaml

primer, repo, ref, decl = sys.argv[1:5]
text = open(primer).read()
fail = 0

regions = dict(re.findall(
    r"<!-- primer:generated id=([^ ]+) -->\n(.*?)<!-- /primer:generated -->", text, re.S))

# 1. term regions vs terms.yaml at the tag
terms = yaml.safe_load(subprocess.run(
    ["git", "-C", repo, "show", f"{ref}:core/graph/terms.yaml"],
    capture_output=True, text=True, check=True).stdout)["terms"]
canon = {t["id"]: str(t.get("canonical_md", "")).strip() for t in terms}
nterm = 0
for rid, body in regions.items():
    if not rid.startswith("term:"):
        continue
    nterm += 1
    quoted = body.split("\n>\n> —")[0].strip()
    if quoted != canon.get(rid):
        print(f"FAIL: {rid} region is not the canonical_md at {ref}")
        fail = 1
print(f"term regions checked: {nterm} (verbatim against {ref} unless FAIL above)")

# 2. declaration region vs the file
dtext = open(decl).read()
def blockquote_after(heading):
    idx = dtext.index(heading)
    lines, started = [], False
    for line in dtext[idx:].splitlines()[1:]:
        if line.startswith(">"):
            started = True; lines.append(line)
        elif started:
            break
    return "\n".join(lines)
want_a = blockquote_after("## A. The canonical text")
want_b3 = blockquote_after("### B-3")
body = regions["declaration"]
if want_a not in body or want_b3 not in body:
    print("FAIL: declaration region does not carry §A and §B-3 byte-for-byte"); fail = 1
else:
    print("declaration region: §A and §B-3 carried byte-for-byte")

# 3. no blockquote outside generated regions
outside = re.sub(r"<!-- primer:generated id=[^ ]+ -->\n.*?<!-- /primer:generated -->", "",
                 text, flags=re.S)
stray = [l for l in outside.splitlines() if l.startswith(">")]
if stray:
    print(f"FAIL: {len(stray)} blockquote line(s) outside generated regions:"); fail = 1
    for l in stray[:5]: print("   ", l[:100])
else:
    print("no quoted block outside a generated region — coverage is exhaustive")

sys.exit(fail)
