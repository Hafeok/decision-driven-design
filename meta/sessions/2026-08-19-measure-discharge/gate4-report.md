# GATE 4 — M-4 and M-5

**draft-pending-ruling.** Commits `502a499` (M-4) and `46ba44f` (M-5).

**Batching judgment:** M-5 rides with M-4. Context v3 is derived from everything M-1–M-4 settled,
so one ratification pass covers the whole record, and Gate 5 stays clean for validators, reference
closure, the branch and the manifest.

---

## 1. The pin — and the one thing it cannot cover

Advanced to **`v5.7.0` / `v0.4.0`**. No stale ref survives anywhere in the manuscript (`v5.3.0`,
`d8fd8e6`, `v5.6.0` all return zero hits).

**But the sixth asset does not resolve at the pin, and this is a real seam rather than a
formality.** Verified path by path:

| Asset | At `v5.7.0`? |
|---|---|
| `measure-toy.py`, `measure-actor-allocation.py`, `measure-rag.py`, `measure-chained-seams.py`, `measure-nonuniform-ground.py` | **yes**, all five |
| `measure-aggregate-discharge.py` | **no** — created this session, lives on the upstream session branch |

The old front matter said *"bracketed claim identifiers **and the assets named under
Reproduction** resolve against these refs."* Left as written with the pin advanced, that sentence
would have been **false**. Two changes fix it honestly:

- Front matter now pins **claim identifiers** and defers the assets: *"…the assets named under
  Reproduction resolve as stated there."*
- Reproduction states the split: five at `v5.7.0`; `measure-aggregate-discharge.py` *"is new with
  this note and lands upstream alongside it, so it resolves at the next tag rather than at the
  pin."*

**The alternative, raised and not taken:** an upstream release descriptor cutting a tag that
carries the sixth asset would let the front matter pin uniformly. That is a release, the prompt
puts releases outside this session, and *do not bundle* is explicit. **Your call — carried as an
open item in context v3.**

## 2. Appendix A — regenerated, not edited

I regenerated both tables **wholesale from the graph** rather than hand-adding nine rows and
hand-fixing three. Every row is then verbatim *by construction*, and the three Gate 1 drifts are
corrected by the same mechanism that adds the new rows rather than as a separate error-prone pass.

**20 → 27 claims, 15 → 17 terms.** An independent second script re-read the finished appendix
against the graph: **all 44 rows match, statement-for-statement and status-for-status.**

New rows: `DDD-cost-30`, `DDD-frame-05`, `DDD-frame-09`, `DDD-frame-14`, `DDD-frame-16`,
`DDD-measure-14`, `DDD-measure-15`, `term:act-individuation`, `term:outcome`.
Refreshed: `term:verdict`, `DDD-cost-05`, `DDD-floor-01`.

`DDD-frame-09` lands as the first **retired** citation. Appendix A's preamble already defined the
status; no apparatus was added.

## 3. `N` into §2's Notation

> *"Two counts appear and are never interchangeable: `n` is the number of points in the input
> space, used below as a display scale, and `N` is a number of acts (§6, §9)."*

Stated once, in the paragraph that states notation once. §6.2's in-place definition stands as the
working introduction, as ruled.

## 4. The final count

| | Words |
|---|---|
| Body through Reproduction, **tables excluded** | **9,122** |
| Including tables | 9,662 |
| §1–§5, untouched by this session | 4,631 |
| §6, this session's new section | 1,229 |

Method recorded in context v3 so future counts are comparable: prose lines only — table rows,
rules and headings dropped, inline code spans counted as one token each.

Movement across the session: 7,443 → 8,738 (§6) → 9,057 (§8 refinement) → **9,122** (M-4's
notation sentence, the Reproduction pin sentence, and Appendix A prose). Every increment is booked
content.

## 5. Context doc v3

Rewritten, superseding v2. Beyond the mechanical updates, three things v3 carries that v2 could
not:

**The two identifications, tabled together**, with the second recorded as layered on the first and
not implied by it — so no future session can pick up the aggregate reading believing §2's
identification carries it.

**Caveat 3 recorded as verified and unchanged**, with the reason attached: `DDD-frame-15`/`16`
partition *discharge*, the caveat cleaves *within the residual*. A future session that meets
frame-15 and reaches for caveat 3 will find the check already done.

**The Ashby hazard written into the working conventions** — `§N/M` forms are Ashby's, and any
mechanical renumber must exclude `§N` followed by `/`. It nearly went wrong at Gate 2 and the next
renumber will not have this session's context.

**The length band is replaced by your rule**, not by a new number. v2's 4,657 is recorded as stale
with an honest note: §1–§5 measure 4,631 by the new method, which is suggestively close, but the
old method was never written down — so the resemblance is reported as an observation and
explicitly not as an explanation.

## 6. Verification at this gate

- Reference closure: **27 claim IDs, 17 term IDs, all resolve** at `v5.7.0` / `v0.4.0`.
- **Appendix A verbatim against the graph: 44/44.**
- Section references: **zero dangling**.
- Stale pin refs: **none**.
- Reproduction paths: **five verified at the pin, the sixth stated as resolving at the next tag**.

## 7. Gate 5 preview

Validators both repos; reference closure re-run over the final text; branch and PR; the manifest —
carrying the renumber correction, the Ashby catch, the two open items (Q32 node, the sixth asset's
pin), and the Paper A note that §6's `O(1)`/`O(N)` material is available as a worked projection.
