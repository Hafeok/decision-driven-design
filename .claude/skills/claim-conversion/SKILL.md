---
name: claim-conversion
description: Convert a core/ document of the decision-driven-design repo into claim files under core/claims/. Use whenever asked to convert, extract, verify, or land claims from canon prose — including verifying seed claims against the live repo. Triggers: "convert core/NN", "extract claims", "verify the seed", "land claims".
---

# Claim conversion

You are converting canon prose into claim files. Authority: `meta/way-of-working.md`.
Format: `spec/claim-format.md` (format version 1). The repo is ground truth — never land a
claim whose statement, status, or evidence you have not verified against the live document
and, where evidence is executable, against a fresh run of the asset.

## Protocol (per core document)

1. Read the document; list every assertion that is a proposition rather than exposition.
2. Split compounds — one proposition per claim. If "and" joins two testable assertions,
   split them. Assign IDs `DDD-<area>-<nn>` in reading order within the area; continue
   existing numbering, never reuse an ID.
3. Status each per the format's entry conditions. The document's own hedging usually
   encodes it: "we observe" → reported (verify the asset reproduces); "should" → projected
   (write the falsifier); "it follows" → check for an actual derivation before writing
   established. The arithmetic/model split is enforced: an identity that holds is a
   separate `formal` claim from the identification that gives it meaning.
4. Anything asserted without evidence or falsifier: status projected, and flag in `notes:`
   — "UNVERIFIED — carried on confidence in prose; Emil review". Surfacing these is half
   the point of converting.
5. The document becomes exposition that cites claim IDs; canon authority moves to the
   claim files. Prose that contradicts its claims is a bug in the prose — flag, do not
   silently harmonise.
6. Run `scripts/validate-claims.py core/claims/` — must pass before commit.
7. Commit per area, not per claim; set `changed` to the conversion version for all landed
   claims. Commit message lists: landed / struck / restatused / flagged.

## Hard rules

- Never present an identity holding as evidence for the framework.
- British spelling. Region is mandatory on every claim.
- Reasoning Emil has not confirmed gets flagged, not asserted.
- When verifying seed claims drafted outside the repo: strike or restatus freely — the
  seed's own header instructs it. A struck claim is a success of the pass, not a failure.
