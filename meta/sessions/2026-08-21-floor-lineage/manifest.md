# Manifest — the floor: definition placement and lineage

**Session** `2026-08-21-floor-lineage` · principal: Emil · four gates, all held · **nothing merged**

Every change this session made, in both repositories, against what it was chartered to do. The
charter is `prompt.md` in this directory, committed before any repository was read for repair.

---

## 1. Disposition of the four booked items

| Item | Booked as | Ruled | Landed |
|---|---|---|---|
| **F-1** definition placement + `term:floor` registry | move the definition; report and hold on minting | **Option C** — promote the definition into `canonical_md`, cost accepted | done, upstream + downstream consequences staged |
| **F-2** the phenomenon has no named ancestor | register entries + a contrast paragraph | proceed, candidate set confirmed, three drafting rulings | done |
| **F-3** two competing novelty claims | report before repairing; defer if it needs a design decision | **defer whole**, session's reasoning adopted as the ruling | deferred, record filed, routed |
| **F-4** Paper A projects `03` without `03`'s sources | verify; repair only if citation-only | **citation-only**, two sources, `§6.1` alone | done |

**Minting:** none. `term:floor` already existed (`core/graph/terms.yaml`, `established_by:
03-the-floor.md`, settled), so the prompt's minting-needs-a-ruling case never arose.

---

## 2. Upstream — `actor-indexed-determination`

Branch `claude/floor-lineage-canon-repair-76sm10`, base `33b6d28`, canon pinned at `v5.8.0`.

| Commit | Contents |
|---|---|
| `3ec2e26` | F-1 — `core/graph/terms.yaml`, `core/03-the-floor.md` |
| `0d21034` | F-2 — `meta/lineage-and-limits.md` §1.3 and §1.16, `core/03`'s contrast paragraph |
| *(this commit)* | `releases/v5.9.0.yaml` |

**Files touched: three, plus the descriptor.** `core/graph/terms.yaml`, `core/03-the-floor.md`,
`meta/lineage-and-limits.md`, `releases/v5.9.0.yaml`.

### The one authored sentence in claim material

Recorded here at Emil's GATE 2 ruling, which is the right level of accounting for one sentence:

> The claim has two limbs.

`core/03-the-floor.md`, opening `## The claim`. It replaces the lead sentence that F-1 moved to the
document's opening. Everything else this session wrote is register prose, the contrast paragraph,
or session record — no other sentence entered claim material, and no claim statement moved.

### What did not move

- **No claim statement, region, status, falsifier, test, evidence or basis field** — swept over all
  **68** claim and decision files, base → HEAD. Zero changes, zero new files.
- **The registry, apart from one field.** 70 terms before and after; none added, none removed; the
  only difference anywhere is `term:floor.canonical_md`.
- **`DDD-floor-01` and `DDD-floor-02`** — untouched, as the charter required.
- **`core/03:18`'s novelty paragraph** — untouched through F-1's restructure, which moved the embed
  *above* it. F-3's deferral therefore left canon exactly as it found it.

---

## 3. Downstream — `decision-driven-design`

Branch `claude/floor-lineage-canon-repair-76sm10`, base `40d277f`.

| Commit | Contents |
|---|---|
| `113d60e` | the arrival record — `prompt.md`, `bootstrap.md`, the sessions index (**first act**, per `DDD-dec-20`) |
| `9bc73d7` | GATE 1 survey |
| `d9bded0` | GATE 2 report |
| `e41c3fe` | F-3's deferral record, F-4's citations, `DDD-dec-29`, the merge checklist, successor items, freight notes |
| *(this commit)* | GATE 4 — the two GATE 3 amendments, this manifest |

**Canon touched:** `core/decisions/DDD-dec-29.yaml` (new — the pin advance, `[PROPOSED]`).
**Manuscript touched:** `papers/paper-a/paper-a.md` — two bibliography entries, one attribution
paragraph, one disclosure tail, one locator alignment. **No argument rewritten.**

---

## 4. The three tag-dependent steps — taken, 2026-08-22

Upstream PR #17 merged as `bce18fe`; the descriptor cut **`v5.9.0`** at that commit. All three then
ran, in order, and every expected result was met.

**The prediction test was run so it could fail.** `ref` was advanced to `v5.9.0` **first**, with
`term:floor`'s `content_hash` left at its old value, and the checker run against that intermediate
state. That produced the observation `DDD-dec-29` was written to be tested against:

> 67 pins resolved, **1 content-drift**, 1 shadowed id — `W6 pinned content moved: 'term:floor' is
> pinned at content_hash sha256:daf43e07… but resolves to sha256:917f7e4d… at the ref`

Exactly one W6, on `term:floor`, both hashes as written down before the operation, no W5, no E12.
**The prediction held in every limb.** Advancing ref and hash in one edit would have shown 0 drift
throughout and left nothing to check the prediction against — the pass and the skip producing
identical output, which is presumed discharge in its exact form.

The hash was then re-instrumented (**0 content-drift**, baseline restored), Appendix A regenerated
against the tag (**exactly the two-line diff predicted at GATE 2**; the independent re-read moved
from 1 expected discrepancy to **0**), and the manuscript's declared ref advanced at
`paper-a.md:7` — the only `v5.8.0` mention in either Paper A artefact, checked rather than assumed.

`DDD-dec-29`'s `[PROPOSED]` banner is struck, at the bump and not at the merge. It therefore does
**not** become a second instance of Paper A freight item 4; it is that item's remedy demonstrated,
and the item's note is corrected to say so.

### What was deliberately not taken, and why (kept as the record)

`downstream-merge-checklist.md` carries them with each expected result pre-verified: advance the pin
and re-instrument `term:floor`'s hash; regenerate Appendix A against the tag (**a two-line diff**);
advance the manuscript's declared ref. They wait because `graph/upstream.yaml` pins *a tag, never a
branch*, and because two of them write the ref into a published manuscript.

`DDD-dec-10`'s staged-branch alternative was available and **declined**, with the reason recorded:
that precedent moved a repository-internal pin file only.

---

## 5. Gate results, at close

### Upstream

| Gate | Result |
|---|---|
| `validate-core-order.py core/` | **exit 0** — 15 documents, 70 terms, 70 graph objects, 62 embedded, **0 errors**, 66 warnings, **0 W4** |
| warning count vs. pre-session baseline | **identical, 66** — no forward edge introduced |
| `validate-claims.py core/claims/` | 60 valid |
| `validate-claims.py core/decisions/ --decisions` | 8 valid |
| `validate-releases.py releases/` | 5 valid |
| `core/assets/` reproduction | **9 of 9 re-run and reproduce** |

### Downstream

| Gate | Result |
|---|---|
| `validate-core-order.py core/` | **exit 0** — 0 errors, 0 warnings; upstream: 67 pins resolved, 0 basis-loss, **0 content-drift**, 1 shadowed id (the standing W7) |
| `validate-claims.py core/claims/` | 26 valid |
| `validate-claims.py core/decisions/ --decisions` | 21 valid |
| `check-quotations.py … ` | **29 verbatim, 0 disclosed-partial, 0 failing** |
| `check-appendix.py … ` | 72 rendered, 72 cited, **1 discrepancy — `term:floor`, expected**, cleared by the checklist's step 2 |

### Reference closure

Every `core/…`, `meta/…`, `papers/…`, `graph/…` path reference in the ten files this session wrote
or edited resolves in one of the two repositories. The single dangling reference at the time of
checking was `releases/v5.9.0.yaml`, written in this commit.

---

## 6. The version proposal, and the descriptor question answered

**`v5.9.0` — minor, not patch.** The session opened expecting a patch, because F-1 was booked as a
prose move. Option C changed that: `term:floor`'s canonical text moves, a downstream pin moves with
it, and a registry change is a minor by the repository's own convention.

**The three commits above `v5.8.0`.** The question was raised at GATE 1 and is answered here rather
than left. The entire delta between `v5.8.0` and this session's base is **one new file** —
`core/assets/measure-aggregate-discharge.py`, 160 lines, added by the measure-discharge session and
covered by no descriptor. **No claim, term, document or evidence field moved with it, and no claim
cites it yet.** It reproduces.

It therefore needs no descriptor of its own and no separate release: it is carried by `v5.9.0`, and
`v5.9.0`'s summary **names it under "Carried, not introduced"** rather than letting it ride silently.
A release descriptor that omits canon the tag will carry is a false record of what was cut, and that
is the whole reason the descriptor is the reviewable object.

---

## 7. What leaves this session open

Four successor items, **none begun** (`successor-items.md`): F-3's routing to the next session that
states the framework's primary contribution; whether a *contrast*-ancestor should generate a §6
required-citation row at all; a **sweep of the whole registry** for canonical text that asserts
without defining, widened from a spot-check at Emil's GATE 3 ruling; and the Wittgenstein print
check, a named debt dischargeable by one reading.

Two findings added to existing freight items rather than booked new: *verbatim is not complete* (a
partial-quote disclosure rule is a second predicate over `check-quotations.py`'s input), and
*prediction before the operation* filed as a convention on the evidence of three independent
instances — `DDD-dec-25`, `-28`, `-29`.

One thing reported and deliberately not repaired: `core/graph/terms.yaml`'s header comment says five
terms are registry-only; there are **eight**. A one-line fix in a file this session already edits,
left alone because the charter forbids bundling.
