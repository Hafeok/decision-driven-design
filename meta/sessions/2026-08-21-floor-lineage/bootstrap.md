# Bootstrap — the floor: definition placement and lineage (2026-08-21)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any canon edit, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/floor-lineage-canon-repair-76sm10` (both repositories)
- **Base commits:**
  - `actor-indexed-determination` — head `33b6d28a4f4d3528371a53dd4af76b809f07cbd5`; **canon pinned
    at tag `v5.8.0` = `9e92099f503a180e7205df224d625b1f0d2fa96f`**
  - `decision-driven-design` — head `40d277f53e93f87818ece4236c2fef9a45fa71be` (the Paper A merge,
    PR #26)
  - `product-cli` — untouched
- **Gates:** 4 (survey and the four dispositions · F-1 and F-2 · F-3 and F-4 · close)
- **Principal:** Emil
- **Session type:** interactive canon curation — hold at every gate, merge nothing
- **Prompt identity:** `prompt.md`, 112 lines, sha256
  `0a298d5da23167dd8f1f4e366456ee36e49e2ca23653672a83aed833e9712a3d`

## Tag verification, at fetch

Emil reported canon at **v5.8.0**. Fetched and verified: `v5.8.0` is the newest tag in
`actor-indexed-determination`, an annotated tag dated 2026-08-18, message *"v5.8.0 — Track 1: the
two deferred mints, discharged on use"*, pointing at commit `9e92099`. Head is **three commits
ahead of the tag**: `c13b29b` (merge of main into the measure-discharge branch), `5c9c8ca`
(`assets: measure-aggregate-discharge.py`), and `33b6d28` (the PR #16 merge). Those three carry
canon changes that **no release descriptor covers** — `releases/` holds `v5.5.0` … `v5.8.0` and
nothing later. The session works at head, which is where its edits land, and reports the unreleased
delta at GATE 4 with its version-bump proposal.

## Scope, as committed

Four items against `core/03-the-floor.md` and its lineage register, all prose, registry, and
lineage work:

- **F-1** — the definition arrives after its own use; move it ahead of the claim block. The
  `term:floor` registry question is answered **first** and, if the term does not exist, minting is
  a filing that **holds for Emil's ruling** — never minted on the session's own motion.
- **F-2** — the floor phenomenon has no named ancestor while `03` opens on a novelty claim.
  Ancestry entries in `meta/lineage-and-limits.md`, every locator **verified or flagged in its own
  entry**; a short contrast paragraph in `03` drafted to strengthen the claim, not to apologise for
  it.
- **F-3** — two novelty claims compete in one repository. **Report before repairing**; defers whole
  if reconciling requires deciding what the framework's primary contribution is.
- **F-4** — Paper A may project `03` without carrying `03`'s own sources. **Verify first**; repairs
  only if the fix is citation-only, and no manuscript argument is rewritten here.

**No claim statement moves.** `DDD-floor-01` and `DDD-floor-02` are untouched in statement, region,
and falsifier. Supersession, never rewriting (precedent: `DDD-dec-09`/`10`/`15`).

---

Read prompt-floor-lineage.md in its entirety — this session follows it exactly, including every
gate.

This is a small, bounded canon repair to core/03-the-floor.md and its lineage register. Four items:
the definition arrives after its own use (move it, and settle the term:floor registry question);
the floor phenomenon has no named ancestor while the document opens on a novelty claim (lineage
entries in meta/lineage-and-limits.md, a short contrast paragraph in 03); two novelty claims compete
in one repository (report before repairing, defer whole if reconciling requires deciding what the
framework's primary contribution is); and Paper A may project 03 without carrying 03's own sources
(verify, repair only if citation-only).

No claim statement moves. DDD-floor-01 and DDD-floor-02 are untouched in statement, region, and
falsifier.

First act, before anything else: commit this prompt and bootstrap to
meta/sessions/2026-08-21-floor-lineage/ in decision-driven-design, per DDD-dec-20.

Fetch both repos at head — actor-indexed-determination at v5.8.0, decision-driven-design at head.

Rules that override anything you might infer:

- Interactive curation. Stop at every gate for Emil's ruling. Merge nothing.
- Minting term:floor is a filing and needs a ruling — report and hold, never mint on your own
  motion.
- Every lineage locator is verified or flagged in its own entry. Nothing asserted from memory; the
  Paper A Tesler entry is the pattern for a source with no primary publication.
- The contrast paragraph in 03 is drafted to strengthen the claim, not to apologise for it: the
  ancestors located irreducibility elsewhere, and the original move is its location in the
  checkability of the acceptance predicate, arrangement-indexed.
- F-3 defers whole if reconciliation turns out to require a design decision.
- F-4 repairs only if the fix is citation-only; no manuscript argument is rewritten.
- Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

Begin with step 1 and end your first report at GATE 1: the term:floor registry answer with node
IDs, both novelty statements verbatim, the Paper A bibliography gap stated exactly, and the lineage
candidates with a verification plan.
