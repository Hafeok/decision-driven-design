# Bootstrap — Paper A's revision, carrying W1 (2026-08-30)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** any repository is read for the work, per `DDD-dec-20`.

## Parameters

- **Branch:** `claude/paper-a-w1-revision-b8sx45` (both repositories; the branch name was fixed by
  the invocation harness and is mirrored across the two so the set is one name)
- **Base commits:**
  - `actor-indexed-determination` — head `81f6929d7525bcb1f2d07b5ce5bf3c6ed6d4275d`. Annotated tag
    `v5.12.0` resolves to **the same commit** (`git rev-parse 'v5.12.0^{}'` →
    `81f6929d7525bcb1f2d07b5ce5bf3c6ed6d4275d`); head and tag coincide, and canon at head is canon
    at `v5.12.0` exactly as the prompt asserts. Tag message: *"v5.12.0 — Definitions that were
    never in the registry, and a collision the store won"*. This is the tag the pin advances to;
    the projection's pin at arrival is `v5.9.0`.
  - `decision-driven-design` — head `54f00eb775edf75fe37649b9a99e8443a014ee8f` (the item-5 merge,
    PR #31)
- **Gates:** 5 (G1 survey plan, retitle, supplement boundary, W1's counts · G2 the related-work
  section · G3 the narrowed claim, the rhetoric pass, the small items · G4 pin advance,
  quotations, Appendix A, supplement split, W1 · G5 close)
- **Principal:** Emil
- **Session type:** interactive paper revision — projection work; hold at every gate, merge nothing
- **Input identity:**

  | File | Lines | sha256 |
  |---|---|---|
  | `prompt.md` | 130 | `6a0ca35825259ac09c4357d2561be069f3b5dcc89fbd71399c0c9d24239e975c` |
  | package `README.md` | 45 | `8808bebae00354acfa37adca92b0860a804b9fe16244af467c4137052e1c2588` |
  | package `paper-a-objective-review.md` | 349 | `1d291a5fcc605ae6ade4c82922802b1be2d132d33b470110946d95b272205707` |
  | package `paper-a-review-triage.md` | 179 | `e9650358e5f6120905d4d7cfc4f4769c407d6f10d4804be9fe09bada8e3f741a` |
  | package `q44-act-and-verdict-ontology.md` | 212 | `4d49ded8c34ac0a48b096040932ca478eae5140ad5aa26f16302f2171a740af8` |
  | package `q45-routes-and-compositional-coverage.md` | 114 | `c5925b25656a53279f858b742f3cecd84acd2052ea7d2ead9ccfd5f0a52c051b` |
  | package `act-and-verdict-ontology-explainer.md` | 222 | `644eabd6a70c74894ae195c3ddda72728932562786e974479041b329b5fe59b5` |

## Arrival — clean

The prompt arrived with the invocation, inside `papera-package.zip`, and is filed here with its
identity in this session's first commit. No supplementary input was named and none is missing.

**Five of the seven package files are already committed, byte-identically, and are not re-filed.**
Each was hashed against its committed copy before the decision:

| Package file | Committed at | Identical |
|---|---|---|
| `paper-a-objective-review.md` | `meta/sessions/2026-08-23-phase1a/paper-a-objective-review.md` | yes |
| `paper-a-review-triage.md` | `meta/sessions/2026-08-23-phase1a/paper-a-review-triage.md` | yes |
| `q44-act-and-verdict-ontology.md` | `meta/sessions/2026-08-27-ground-migration/inputs/q44-act-and-verdict-ontology.md` | yes |
| `q45-routes-and-compositional-coverage.md` | `meta/sessions/2026-08-27-ground-migration/inputs/q45-routes-and-compositional-coverage.md` | yes |
| `act-and-verdict-ontology-explainer.md` | `meta/sessions/2026-08-27-ground-migration/inputs/act-and-verdict-ontology-explainer.md` | yes |

Those five paths are the ones cited throughout this session. The identity check is the point, not
the courtesy: the ground-migration session's arrival caught a wrong artefact offered at a gate by
hashing it, and an unhashed "already committed" would be the same presumed discharge in a quieter
form.

The two files with no committed copy are `prompt.md` (this session's charter) and the package
`README.md`, filed under `inputs/` so the charter is reconstructible.

**Filing Q44 and Q45 anywhere is not filing them as canon.** They are unfiled downstream demand and
the prompt keeps them unfiled. This session rules *with their existence known* — which is only
possible if they are quotable at the gates — and the paper may not cite them. Where the paper wants
a distinction they carry, it is register-native prose or it waits.

## The invocation message, verbatim

Unzip papera-package.zip and read papera-package/README.md, then read prompt-paper-a-revision.md in
its entirety — this session follows that prompt exactly, including every gate.

This is Paper A's revision: it answers its external review, advances its pin from v5.9.0 to v5.12.0,
and carries W1 — the ground migration's cheapest wave, 88% of which lives inside this paper and the
measure note.

First act, before anything else: commit this prompt and bootstrap to
meta/sessions/2026-08-30-paper-a-revision/ in decision-driven-design, per DDD-dec-20.

Fetch both repos at head — actor-indexed-determination at v5.12.0 (verify and report the tag found)
and decision-driven-design at head. The manuscript at papers/paper-a/paper-a.md is the working text.

Rules that override anything you might infer:
- Interactive revision. Stop at every gate for Emil's ruling. Merge nothing.
- Projection work: the paper may not introduce claims. Q44, Q45 and the ontology explainer are
  supplied as context and are UNFILED — never cite them as canon. Where the paper wants a
  distinction they carry, it is register-native prose or it waits.
- The related-work survey is reading before it is drafting. Verify every locator or flag it
  unverified in its own entry; the Hayek facsimile check and the Tesler no-primary-publication entry
  are the two patterns.
- W1 renames the population sense ONLY. Any occurrence ambiguous between it and another sense defers
  to the migration rather than being ruled here. Report moved and deferred counts.
- State predicted W6/W7 results before the pin advance, and verify after.
- Appendix A is regenerated wholesale from the graph, never hand-edited, with the independent
  re-read. Hand-editing it would forge agreement the pin does not have.
- Commit drafts before reporting at each gate, bodies marked draft-pending-ruling.

The failure mode to avoid: the revision makes the paper shorter, better sourced and narrower, and a
shorter paper can end up sounding more certain because it has less to qualify. Where a claim is
projected, the sentence around it says so.

Begin with step 1 and end your first report at GATE 1: citations re-verified at v5.12.0, the four
failing quotations confirmed, W1's occurrences enumerated with ambiguous cases separated, the survey
plan, retitle candidates, and the supplement split's proposed boundary.
