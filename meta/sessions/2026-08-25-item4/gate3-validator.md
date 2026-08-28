# GATE 3 — the validator checks

**DRAFT — PENDING RULING.** The four checks are implemented and running in both repositories.
`validate-claims.py` is byte-identical in the two repos and stays so.

**Zero errors in canon, both repositories.** Both error-class checks fire on nothing, which is why
they are error class.

---

## 1. What shipped

`scripts/validate-claims.py` gains a warning channel alongside its errors, and a `CHECK_CLASS`
table that is the whole of the class policy — one line per check, so promoting a check is a
one-word reviewable change and never a silent one.

| Check | Class | Hits in canon | What it does |
|---|---|---|---|
| **`falsifier-presence`** (A1) | **error** | **0 of 89** | Rule 2's falsifier condition held at every live status, not `projected` alone. `test` substitutes for `conceptual`/`normative` only. |
| **`falsifier-strict`** (A2) | warning | 7 of 89 | Every live claim carries a `falsifier`, `test` no substitute. |
| **`single-limb`** (B1) | warning | 31 of 89 | Rule 1's proxy — clause-joining punctuation outside mathematical notation. Labelled *candidate for adjudication, not a verdict*. |
| **`retired-from`** | **error** | **0 of 89** | A retired claim records the maturity it held; the field is legal only on retired claims; `unrecoverable` requires a `notes` entry. |

Current output, unchanged in substance from Gate 1's predictions: upstream **32 warnings, 0 errors**
across 63 claims; downstream **6 warnings, 0 errors** across 26.

### A1 — why the class is free and the rule is not trivial

A1 fires on nothing today, so it merges without a migration. It is not thereby empty. Rule 2
required a falsifier for `projected` and said nothing for `reported` or `established`, so **the
strongest status canon offers carried the weakest evidential requirement** — and that is the gap
`DDD-measure-06` sat in from v4.5 to v5.9. The rule now binds where the defect was.

### A2 — warning, and what promotes it

The seven, unchanged from Gate 1: `DDD-measure-09`, `DDD-measure-12` (reported); `DDD-cost-05`,
`DDD-frame-01`, `DDD-frame-02`, `DDD-frame-03`, `DDD-frame-08` (projected). All carry a `test`; four
are among the sixteen definitions. **The ruling that lands the last of the seven is the one that
promotes the check**, and the code says so where the class is set.

### B1 — a drafting prompt, and one correction made at this gate

**Retired claims are exempt, and the exemption is not a convenience.** The first implementation
fired on `DDD-frame-09`, `DDD-measure-06` and `DDD-measure-08`. A retired claim's `statement` is a
retirement record, not a proposition — canon rewrites it as `RETIRED — "<the dead claim>"`.
`DDD-measure-06`'s epitaph **quotes verbatim the compound statement that killed it**, so flagging it
for rule 1 flags the record of the defect as though it were the defect. Rule 1 governs propositions,
and an epitaph is not one. Hit list 34 → **31**.

The check names itself in every line and calls its findings candidates. It is never to be promoted
without an adjudication: it fires on `DDD-measure-16`, the claim built to cure `DDD-measure-06`.

---

## 2. `retired_from` mandatory — argued on its own terms, as ruled

**Proposed: error class.** The argument does not lean on the field having just been filed.

**The hit list is 0 of 89** — the four retired claims carry the field, so nothing migrates.

**The rule can never be unsatisfiable, which is the load-bearing property.** `unrecoverable` is
always available and always honest. A mandatory field that can be discharged by an honest "not
found" imposes no pressure to fabricate; a mandatory field with no such value would create exactly
the incentive `DDD-dec-32` forbids. **The rule is safe to make mandatory because the escape hatch is
truthful rather than because it is rare.**

**Optional is the disposition that fails.** The defect `retired_from` repairs is not that the prior
maturity is hard to record — it is that **two claims retired on the same day by the same hand
recorded it differently**, `DDD-measure-06` preserving its field block and `DDD-frame-15` not.
Optional reproduces exactly that: the field gets filled by sessions that are thorough and skipped by
sessions that are busy, and the reader cannot tell a claim with no recorded prior status from a
claim whose prior status was never looked for. **An optional provenance field records diligence, not
provenance.**

**Three sub-checks, all at 0:** presence on retired claims; legality (the field only on retired
claims); and a `notes` entry required where the value is `unrecoverable`. The last is deliberately
weak and says so in its own message — *that* the notes record a search is not mechanically
checkable, only that notes exist. That is the B1 lesson applied honestly rather than a check
pretending to more than it does.

---

## 3. Two findings from implementation

### (a) The seed fails the new checks, and that is the checks working

`meta/seed/claims-seed.yaml` is the frozen 27-claim pre-conversion snapshot. Run against it, the new
checks exit 1 with **three violations**:

```
DDD-measure-06: [falsifier-presence] status 'established' requires falsifier
DDD-measure-08: [retired-from] retired claim requires retired_from
DDD-frame-09:   [retired-from] retired claim requires retired_from
```

**The first is `DDD-measure-06`, caught on the first run, in the v4.5 snapshot.** The node was found
in canon by an external reader working through the argument, five minor versions later. This is the
instrument's first independent confirmation and it is worth stating plainly: **the repository could
have found it by reading the file.**

**The seed is not repaired.** It is history, and supersession-never-rewriting applies to it as much
as to a retired claim — a snapshot edited to pass today's checks would stop being a record of what
v4.5 was. Its exit 1 is a true report. CI validates `core/claims/` and `core/decisions/` only and is
unaffected; the checker's docstring now says all of this, because the usage line invites exactly
that run.

**Held:** the seed stays red, or the seed is exempted. Recommendation: stays red.

### (b) The versioning question these checks raise, and it is not rhetorical

`spec/claim-format.md`'s own versioning rule says a format change is *"a field added, a rule
altered"*. This session has done both: `retired_from` is a field added, and the falsifier condition
at every live status is **rule 2 altered**. Both are filed in `spec/claim-format-2-addendum.md` with
migration notes, and both are enforced now — against claims that all declare `format: 1`.

That is in tension with the spec's own discipline, which says validation *"runs against the declared
version's rules (§2 for format 1)"*.

**The tension predates this session and this session did not create it.** The addendum calls itself
*proposed format 2* while its existing fields — `canonical_home`, `canonical_md` — are already read
and enforced by `validate-core-order.py` against format-1 claims, on 62 embedded blocks. **No claim
in either repository declares `format: 2`.** The addendum is in force in practice and proposed in
its title.

**Two dispositions, both real work, neither taken here:**

1. **Bump.** The addendum stops calling itself proposed, `SUPPORTED_FORMATS` gains 2, and every
   claim's `format:` moves to 2 — 89 files, mechanical, and a genuine migration note.
2. **Reclassify.** The additions are recorded as format-1 strengthenings with empty hit lists, the
   addendum's scope is narrowed to say which of its contents are format-2 material and which are
   format-1 rules, and the bump is booked for when a change actually breaks a format-1 claim.

**Recommendation: (2) now, (1) booked with the `lifecycle` field**, which is the first change that
genuinely cannot be additive and therefore genuinely needs the bump. Doing (1) now would spend a
format version on changes that break nothing.

---

## 4. Gates

| | upstream | downstream |
|---|---|---|
| `validate-core-order.py core/` | 0 errors, 66 warnings (59 W1 · 7 W2), **zero W4** | 0 errors, 0 warnings |
| `validate-claims.py core/claims/` | valid: 63, **0 errors**, 32 warnings | valid: 26, **0 errors**, 6 warnings |
| `validate-claims.py core/decisions/ --decisions` | valid: 11 | valid: 21 |

`validate-claims.py` byte-identical across the two repositories.

---

## Held at GATE 3

| # | Held for ruling |
|---|---|
| **R11** | The four checks and their classes as implemented. |
| **R12** | `retired-from` mandatory at **error** class, on the argument in §2 — the rule is safe to make mandatory because `unrecoverable` is truthful, and optional records diligence rather than provenance. |
| **R13** | B1's exemption of retired claims — an epitaph is not a proposition. |
| **R14** | The seed stays red, or is exempted. Recommendation: stays red. |
| **R15** | The versioning question — reclassify now, bump booked with `lifecycle`. Or bump now. |
