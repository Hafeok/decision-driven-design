# Manifest — item-4 session (2026-08-25)

Everything this session changed, in both repositories, with the ruling each change lands under.
**No claim statement, status or region moved.** Verified mechanically against `v5.10.0`: four claim
files changed, statements moved: none.

---

## `actor-indexed-determination` (upstream) — branch `claude/prompt-item4-status-kind-vaquwe`

| File | Change | Ruling |
|---|---|---|
| `core/decisions/DDD-dec-31.yaml` | **new** — `conceptual` does not split now; the sequence; a definition's falsifier is its `test` | R1, R2 |
| `core/decisions/DDD-dec-32.yaml` | **new** — `retired_from` filed, `lifecycle` booked as format 2 | R3 |
| `core/decisions/DDD-dec-33.yaml` | **new** — the four validator checks and the rule assigning their classes | R11–R15 |
| `core/claims/DDD-measure-06.yaml` | `retired_from: established`, provenance in `notes` | R3 |
| `core/claims/DDD-frame-15.yaml` | `retired_from: projected`, provenance in `notes` | R3 |
| `core/claims/DDD-frame-09.yaml` | `retired_from: unrecoverable`, search recorded in `notes` | R3 |
| `core/claims/DDD-measure-08.yaml` | `retired_from: unrecoverable`, search recorded in `notes` | R3 |
| `spec/claim-format-2-addendum.md` | reclassified from *proposed format 2* to *additive extensions in force*; `retired_from`; the falsifier condition at every live status | R3, R15 |
| `spec/claim-format.md` | §4 — the two report classes and the rule that governs them; **§5 — what the statuses mean and what they do not** (new); old §5 renumbered §6 | R11, I-4 |
| `scripts/validate-claims.py` | warning channel; `CHECK_CLASS`; four checks | R11–R14 |
| `CLAUDE.md` | reference closure — the addendum's contents, §5, and what the warning counts mean | close |
| `releases/v5.11.0.yaml` | **new** — the release descriptor | close |

## `decision-driven-design` (downstream) — same branch name

| File | Change | Ruling |
|---|---|---|
| `meta/sessions/2026-08-25-item4/` | prompt, bootstrap, gate records, `survey.py`, `i1a-classification.yaml`, this manifest | DDD-dec-20 |
| `meta/successor-items-item4.md` | **new** — four successor items | R1, R3, R5, R10 |
| `meta/sessions/README.md` | index row | DDD-dec-20 |
| `scripts/validate-claims.py` | identical copy of the upstream change | R11–R14 |
| `spec/claim-format.md` | identical §4 and §5 additions | R11, I-4 |
| `papers/paper-a/gen-appendix.py` | **`kind` column**; preamble rewritten and pointed at `spec/claim-format.md` §5; defect history | I-3 |
| `papers/paper-a/check-appendix.py` | checks `kind`; status re-anchored so a new column cannot silence it; defect history | I-3, P5 |
| `papers/paper-a/paper-a.md` | Appendix A regenerated wholesale against `v5.9.0` | I-3 |

**`scripts/validate-claims.py` and `spec/claim-format.md` are byte-identical across the two
repositories except for `claim-format.md`'s upstream-only §6, which is the drift that existed before
this session and is filed as successor item 4.**

---

## Predictions against outcomes

All six predictions were committed at `64818d8` before any of the operations they predict ran.

| | Predicted | Observed |
|---|---|---|
| **P1** W6 pinned content movement | unchanged, no new W6 | **0 content-drift** across 67 pins ✓ |
| **P2** W7 shadowed ids | unchanged, no new W7 | **0 W7 warnings**; `terms.yaml` untouched in both repos ✓ |
| **P3** W5 basis loss | unchanged | **0 basis-loss** ✓ |
| **P4** `check-quotations.py` at the pin | passes; the four known failures are against `v5.10.0`, not `v5.9.0` | **29 verbatim, 0 failing** ✓ |
| **P5** `check-appendix.py` silently weakens | **fails silently** unless updated in the same commit | **confirmed by experiment** — see below ✓ |
| **P6** regeneration idempotent | identical bytes over three runs | identical ✓ |

### P5, demonstrated rather than asserted

The prediction was that adding a column would switch off the status check while the run still
reported success, because the check was guarded on `len(cols) == 2`.

A copy of the regenerated appendix was corrupted in two cells — `DDD-cost-08`'s status
`projected` → `established`, and `DDD-cost-09`'s kind `conceptual` → `formal` — and both checkers
were run against it:

```
OLD checker:  72 nodes rendered, 72 cited in the body, 0 discrepancies    exit 0
NEW checker:  72 nodes rendered, 72 cited in the body, 2 discrepancies    exit 1
                DDD-cost-08: status differs from the graph
                DDD-cost-09: kind differs from the graph
```

**The pre-session checker passes an appendix carrying a falsified status and a falsified kind.**
Metadata columns are now counted from the left and named individually, and the hazard is recorded
in the checker's own defect history: *never guard a check on a total column count*.

---

## Gates, at close

| Gate | upstream | downstream |
|---|---|---|
| `validate-core-order.py core/` | 0 errors, 66 warnings (59 W1 · 7 W2), **zero W4** | 0 errors, 0 warnings; 67 pins resolved, 0 basis-loss, 0 content-drift |
| `validate-claims.py core/claims/` | valid: 63, 0 errors, 32 warnings | valid: 26, 0 errors, 6 warnings |
| `validate-claims.py core/decisions/ --decisions` | valid: 12 | valid: 21 |
| `validate-releases.py releases/` | valid: 7 | n/a |
| `core/assets/` reproduction | **9 of 9 reproduce** | n/a |
| `check-appendix.py` @ `v5.9.0` | n/a | 72 nodes, 0 discrepancies |
| `check-quotations.py` @ `v5.9.0` | n/a | 29 verbatim, 0 failing |

---

## Version proposal — `v5.11.0`

**Minor.** Descriptor filed at `releases/v5.11.0.yaml`.

**Not a patch.** The schema gains a field (`retired_from`) and a rule (the falsifier condition at
every live status); three decisions are filed; and `spec/claim-format.md` gains a section that
changes what an outside reader is told the registry means. A patch is for corrections that leave the
shape alone, and this changes the shape.

**Not a major.** **Every format-1 claim remains valid unchanged**, the corpus migration is empty
(both error-class checks fire on 0 of 89), no consumer of any existing field changes, and no
statement, status or region moves. The one change that would break an unchanged reader — the
`lifecycle` field — is deliberately deferred, and format 2 is reserved for it.

**The pin is not advanced.** Paper A stays at `v5.9.0` by standing ruling; its four known-failing
quotations against `v5.10.0` are Phase 1a's held state and are untouched here.

**A note the descriptor carries and this manifest repeats**, because the next release will meet it:
head diverged from the tag at this session's arrival — `v5.10.0` is `37f508e` and head was
`403dede`, three README-only commits further on. The descriptor omits `commit`, so it cuts wherever
it lands, which is the correct handling and is now on the record as having been handled.
