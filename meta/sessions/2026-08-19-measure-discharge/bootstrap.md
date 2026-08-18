# Bootstrap — the measure note: the discharge section (2026-08-19)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any manuscript edit, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/measure-discharge-section-o0y0f7` (both repositories)
- **Base commits:**
  - `actor-indexed-determination` — `4d0d177d0c9b7d317c000018a83bd94a6e1c1d09` (= tag `v5.7.0`)
  - `decision-driven-design` — `8e348ceb201afb42c85d8a089e44f8e083f575b0` (head; Wave 3 merge, PR #23)
  - `product-cli` — untouched
- **Gates:** 5 (fetch/verify/propose · M-1 drafted · M-2 and M-3 · M-4 and M-5 · close)
- **Principal:** Emil
- **Session type:** interactive paper drafting — hold at every gate, merge nothing
- **Prompt identity:** `prompt.md`, 128 lines, sha256
  `bd30d4e80f5455b23c9daa8904b9c5361b58b418248ced72027a1c8495a40b02`

## Scope, as committed

One new section (M-1, the discharge section), one §7 refinement (M-2, constructive closure), a
citation-upgrade pass (M-3), front matter and Appendix A (M-4), and the context doc's
regeneration (M-5). **Projection work throughout: the paper may not introduce claims.** Where the
section wants a claim canon lacks, the section is drafted citing what exists and the gap is
flagged — nothing is filed.

---

Read prompt-measure-discharge.md in its entirety — this session follows it exactly, including
every gate.

This is a bounded paper session: the measure note gains its discharge section (booked at Wave 3,
its claims landed at v5.7.0 as DDD-frame-15/16), the §7 constructive-closure refinement, the
already-ruled citation upgrades (DDD-measure-14, DDD-measure-15, DDD-cost-30 — exact lines in
measure-paper-context.md), front-matter and Appendix A updates, and context doc v3. The paper is
otherwise done and reviewed; the failure mode is re-opening what the review settled.

First act, before anything else: commit this prompt and bootstrap to
meta/sessions/2026-08-19-measure-discharge/ in decision-driven-design, per DDD-dec-20.

Fetch both repos at head — actor-indexed-determination at v5.7.0, decision-driven-design at head;
the manuscript at papers/measure-note/measure-note.md is the working text. Re-run all assets and
re-verify every citation before proposing anything.

Rules that override anything you might infer:
- Interactive drafting. Stop at every gate for Emil's ruling. Merge nothing.
- Projection work: the paper may not introduce claims. Where the section wants a claim canon
  lacks (the M-2 survey question), draft citing what exists and flag the gap — file nothing.
- The theorem is Shannon's, first, always. The correlation inequality is Shannon's; the
  identification of correlated verdicts with cacheable work is the modelling claim, and its
  untested correspondence is stated in §6's register.
- The aggregation content strengthens the ratified Scale repair and cites it — it never reopens
  the nH(V) error the review caught.
- Numbers only from scripts: a new asset is licensed if the section states worked figures, not
  required if existing assets carry it.
- Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

Begin with step 1 and end your first report at GATE 1: proposed placement and outline for the
discharge section, the new-asset question answered with the figures the section wants, the M-2
survey result, the citation-upgrade list line-by-line, and any manuscript-canon drift since the
revision merged.
