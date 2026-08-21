# meta/sessions/

Session arrival records. One directory per session, named `YYYY-MM-DD-<slug>/`, holding the
**prompt** and its **bootstrap** as committed *before* the session ran.

**Why this exists.** Five sessions arrived without a durable record of what they were asked to do:
the prompt lived only in the invocation, so a session's own charter could not be cited, diffed, or
checked against what the session actually did. `DDD-dec-17` records those five arrival failures.
Committing the prompt first makes the charter a repo object — quotable at every gate, and auditable
afterwards against the commits the session produced.

**The convention.** Before a session begins work:

1. `meta/sessions/YYYY-MM-DD-<slug>/prompt.md` — the session prompt, verbatim.
2. `meta/sessions/YYYY-MM-DD-<slug>/bootstrap.md` — the invocation message and the session's
   parameters (branch, base commits, gates, principal).

Both land in the session's first commit, on the session's branch, before any canon is touched.

A session's own scope is thereby fixed at arrival rather than reconstructed at close. Where a
session's later work exceeds the committed prompt, the excess is visible as excess.

**Index.**

| Session | Type |
|---|---|
| `2026-08-17-freight/` | Interactive canon curation — the accumulated small-items list (batches A–G) |
| `2026-08-18-wave3/` | Interactive canon curation — the principle-layer filings (batches W/H/Q, map P) |
| `2026-08-18-track-1-determination/` | Projection authoring — the determination learning track, ten rungs, two repositories |
| `2026-08-19-measure-discharge/` | Interactive paper drafting — the measure note's discharge section (items M-1…M-5) |
| `2026-08-20-paper-a/` | Interactive paper drafting — Paper A, the framework's statement paper (P-1…P-5) |
| `2026-08-21-floor-lineage/` | Interactive canon curation — the floor's definition placement and lineage (F-1…F-4) |
