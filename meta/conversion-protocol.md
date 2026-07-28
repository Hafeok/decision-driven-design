# Conversion protocol — core/ to claims

**Status.** Process document, versioned with the way of working — not with the claim format
(`spec`) and not with claim content. Changing how conversion is done edits this file only.

The full conversion must run against the live repo — the seed file in this project is extracted
from projections at v4.4 and **every entry requires verification against canon before landing**.

Per core document, in a session with the repo checked out (Claude Code is the natural venue; the
skills pattern from product-cli applies — this protocol is a candidate for the DDD repo's first
`.claude/skills/` skill):

1. Read the document; list every assertion that is a proposition rather than exposition.
2. Split compounds per the format's one-proposition rule; assign IDs in reading order within the
   area.
3. Status each per the format's entry conditions — the document's own hedging language usually
   encodes the status ("we observe" → reported; "should" → projected; "it follows" → check for a
   derivation).
4. Anything asserted without evidence or falsifier gets statused *projected* and flagged — the
   conversion will surface claims the prose was carrying on confidence, and finding them is half
   the point.
5. The document itself becomes exposition that *cites* claim IDs; canon authority moves to the
   claim files. Prose that contradicts its claims is a bug in the prose.
6. Commit per area, not per claim; `changed` set to the conversion version for all.

Expected yield from step 4: a handful of load-bearing assertions in `core/` that turn out to have
neither evidence nor falsifier. Those are the graph's first escalations to the principal.
