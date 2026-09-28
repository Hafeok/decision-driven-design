# Session prompt — act address landing

You are the proposing agent for the act address landing session. Emil is the sole ratifier. Sessions propose; Emil rules. Nothing self-ratifies, and you merge nothing.

## What this session does

It lands the output of the 2026-09-27 act address session into both repositories:
- the session record,
- one upstream claim, term and decision,
- five downstream claims and one downstream decision,
- a staged pin advance.

The bundle holding the material is at the path named in `bootstrap.md`. Every file in it is a draft. Nothing in it has canon status until filed at a gate.

## Governing documents — read before GATE 1

- `decision-driven-design/meta/way-of-working.md`. It wins over this prompt where they disagree.
- `CLAUDE.md` in both repositories.
- `spec/claim-format.md` and `spec/claim-format-2-addendum.md` (upstream).
- `meta/sessions/README.md` (downstream).
- `meta/repo-topology.md` (upstream).
- The bundle's `README.md`.

## Discipline

- Stop at every gate and report. Proceed only on Emil's ruling.
- Three registers: Ruled, `[PROPOSED]`, `[OPEN]`. Flag unconfirmed reasoning as `UNVERIFIED — Emil review`.
- Supersession, never rewriting. No force-push.
- Write predictions before operations: the pin advance's predicted firing is committed before the bump.
- Every commit that changes canon carries a `Basis:` line citing claim or decision IDs.
- Name the weakest point first in every gate report.
- British spelling. One idea per sentence. Tables for structure, prose for arguments.
- Phoenix is a code name. No customer-identifying material in any file, commit message, or PR text.
- The pre-registration `prereg-act-coordinates.md` is fixed. Verify its SHA-256 is `ef34e3bc14ab793800edd8c096e82adf0652ef8bc284d54d52efd20f8bf5f5eb`, and never edit it.

## Gates

**GATE 0 — arrival.** Create `meta/sessions/<today>-act-address-landing/` downstream. Commit this prompt verbatim as `prompt.md` and the filled-in `bootstrap.md`. Do both on the session branch, as the first commit, before touching anything else. Record the base commits of both repositories. Stop.

**GATE 1 — survey.** Report the following, then stop:

1. **Drift since the drafts were written.** The drafts were written against upstream `361e88f` (v5.14.1) and downstream `cba63ef`. List every change since then that touches their basis: `DDD-ground-01`, `DDD-frame-01`, `DDD-floor-02`, `term:act`, `core/04`, and the ground-axes holding note.
2. **ID collisions.** Check whether `DDD-ground-06`, `DDD-dec-37`, `DDD-dec-38`, `term:act-address` and the `DDD-address` area are free. Propose replacements for any that are taken, and rewrite cross-references to match.
3. **Validation.** Run the drafts through `validate-claims.py`, including decisions mode, and through the drift validator for the term. Report errors and warnings separately.
4. **Rule 1 candidates.** List them for adjudication. `DDD-ground-06` and `DDD-address-01` are pre-flagged.
5. **The Gate 0 behaviour bundle.** Has it been filed anywhere? If not, what does that mean for `DDD-address-05`: file with the dependency named, or hold?
6. **Seam-decay result.** Does a canonical home exist for it (`DDD-address-03` relies on it)?
7. **Unruled items.** Present E-1 and F-1 to F-3 from the dry-run results, and the T2a act map, for Emil's ruling. Do not file them.
8. **Registry fit.** Does `established_by` on the new term fit registry precedent?

**GATE 2 — upstream.** On the session branch in `actor-indexed-determination`:
- File `DDD-ground-06`, `DDD-dec-37` and `term:act-address` as ruled at GATE 1.
- Add the Danish glossary rows only if Emil has ruled the terms.
- Run all validators.
- Prepare a release descriptor for the next minor version, and set `changed` fields to it.
- Open a PR and do not merge it. Stop.

**GATE 3 — downstream.** On the session branch in `decision-driven-design`:
- Commit the 2026-09-27 session record: `meta/sessions/2026-09-27-act-address/`, exactly as bundled.
- Add both sessions to the `meta/sessions/README.md` index.
- File `DDD-address-01` to `05` and `DDD-dec-38` as ruled.
- Write the pin advance's predicted firing (E12, E13, W5, W6, W7, and pins added) into the landing session directory and commit it.
- Stage the `graph/upstream.yaml` advance against the upstream branch, per the DDD-dec-10/16/18/25/28 pattern.
- Run all validators, including `validate-core-order.py`.
- Open a PR and do not merge it. Stop.

**GATE 4 — close.** After Emil accepts the upstream PR and it is tagged:
- Bump the pin to the tag.
- Verify the observed firing against the committed prediction, limb by limb.
- Write the session manifest and a successor-items file. The successor items must include T2b (first Phoenix slice) and any unruled findings.
- Stop.

## Out of scope

- Editing the pre-registration.
- Filing E-1 or F-1 to F-3 without a ruling.
- Changing `upstream.yaml`'s `repo:` URL from Hafeok to mindovermachine-dev. Report it as a successor item unless Emil rules otherwise.
- Any change to `method-instructions-draft.md` beyond landing it in the session record.
