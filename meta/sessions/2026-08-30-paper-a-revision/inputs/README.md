# Paper A's revision — package

Upload to a Claude Code session with both canon repositories available, and paste `bootstrap.md` as
the opening message.

## Contents

| File | Role |
|---|---|
| `prompt-paper-a-revision.md` | The session prompt. Five gates, six work items |
| `bootstrap.md` | Paste as the opening message |
| `paper-a-objective-review.md` | The external review — the session's brief |
| `paper-a-review-triage.md` | Emil's ruled triage: concede, defend, repair |
| `q44-act-and-verdict-ontology.md` | **Unfiled.** Context for differentiating in the survey |
| `q45-routes-and-compositional-coverage.md` | **Unfiled.** Same |
| `act-and-verdict-ontology-explainer.md` | **Unfiled.** Standalone explanation of both |

**Not in the package, because the repositories are authoritative:** the manuscript
(`papers/paper-a/paper-a.md`), Appendix A's generator and checkers, `measure-paper-context.md`, and
the migration seed (`meta/migration-plan-ground.md`).

## Why this runs before the migration

W1 is not a dependency of the revision — it is nearly the same work. 88 of its 88 mutable
occurrences sit in the two papers; 11 more ride other waves trivially. And W1 is separable by
construction: it renames a sense that touches no other sense and fires no pins, so carrying it here
is not a partial migration.

The write-twice cost of doing the papers first is 13 occurrences of the migration's 187 — and zero
if W1 rides, which it does.

## What Emil rules

| Gate | Ruling |
|---|---|
| 1 | Survey plan, retitle candidates, supplement boundary, W1's counts |
| 2 | The related-work section — the session's largest ruling |
| 3 | The narrowed novelty claim, the rhetoric pass, the review's small items |
| 4 | Pin advance, the four quotations, Appendix A, the supplement split, W1 |
| 5 | Close, PR, the response-to-review document |

## After this

The ground migration executes from its seed — now 88 occurrences smaller. Then the primer, then the
transfer.
