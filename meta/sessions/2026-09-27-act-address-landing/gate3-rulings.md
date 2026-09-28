# GATE 3 — rulings (act address landing)

Principal: Emil. Given 2026-09-28, in two messages, after PR #24 had merged at `e484ca5` and
`v5.15.0` had been cut without the GATE 2 fix `cc0abf8`.

| # | Subject | Ruling |
|---|---|---|
| 1 | GATE 3 | Accepted. |
| 2 | The missed fix | Open v5.15.1 from a fresh branch. Cherry-pick `cc0abf8`. Write a descriptor recording the miss on the v5.14.1 precedent. Stop at the PR. |
| 3 | GATE 4 | After v5.15.1 is tagged, run GATE 4 against v5.15.1: bump the ref, verify limb by limb, record the change of target from the prediction as a deviation with its cause, re-instrument `DDD-frame-08`, and write the manifest. |
| 4 | Successor items | Add a release-head guard: the descriptor records the ratified head, and CI fails if the head moves. **Priority.** Add decision pinning for `basedOn` references. **Low priority.** |
| 5 | PR #37 | Watch it on the same terms as #24. |
| 6 | Danish notes (second message) | Strike. Replace both notes with "Se core/14." and keep the two rows. Add the commit to PR #25 and report the new head. "I ratify that head, not 1986110." |
| 7 | Successor item (second message) | A glossary pass for act, act occurrence, act-site and ground axis. "handling" for act is implicitly ruled by `handlingsadresse` and needs its own ruling. |

**Note on ruling 6.** The first GATE 3 message carried the Danish-notes ruling as an unfilled
"[keep / strike]". The session applied nothing and flagged it. The second message filled it.

## How the rulings landed

| Ruling | Where |
|---|---|
| 2 | Upstream branch `claude/act-address-landing-bla6io-v5.15.1`: `7cfc828` (cherry-pick of `cc0abf8`), `1986110` (descriptor) |
| 6 | Upstream `7266306` (glossary notes, descriptor updated). PR #25 merged at `1cb3819` with exactly that head; tagged `v5.15.1` |
| 3 | Downstream `4b94593` (deviation, before the bump), `662f8b2` (ref alone), `50e90ca` (re-instrumentation) |
| 4, 7 | `successor-items.md` |
