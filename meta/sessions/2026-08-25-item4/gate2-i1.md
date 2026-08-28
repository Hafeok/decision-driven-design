# GATE 2 — I-1 as ruled

**DRAFT — PENDING RULING.** Filed for the Gate 2 ruling. Nothing is merged.

Both repositories' gates are green after these edits. **No claim statement is touched**, and no
live claim is touched at all — the four files that change are the four retired ones, and the change
is a header field plus a notes paragraph each.

---

## R1 — `conceptual` does not split now; the split is sequenced after rule 1

**Filed upstream as `DDD-dec-31`** (`core/decisions/DDD-dec-31.yaml`), and as item 1 of
`meta/successor-items-item4.md` here.

Emil's stronger form of the argument is carried as the decision's own reason rather than as the
session's: **a kind value is cheap to add and expensive to undo.** Once `definitional` exists and
sixteen claims carry it, the later split adjudication is constrained by what has already been filed;
splitting first leaves the assignment free. The cost is asymmetric, so the order is not a preference.

**Filed as a decision and a successor item, not as a claim node** — per the ruling. The distinction
is recorded in the decision's *deliberately not done*, because it is worth keeping sharp: this is a
finding about canon's metadata, not a claim about the world, and the claim graph is not the place to
record facts about the claim graph's fields.

**`DDD-frame-17` is named the first target, with the reason stated plainly** in both the decision's
notes and the successor item: it was filed this month, at `v5.10.0`, as the successor built to cure
`DDD-frame-15`'s compoundness, and it is already known-compound at three limbs. **A repair authored
under a rule the validator does not check reproduces the defect it repairs.** That is evidence for
the sequencing rather than against the claim, and it is the same argument the freight item makes
about `DDD-measure-06` — which is why the two items sit on one surface.

The eight are named in full in both places so the successor adjudication starts from a list rather
than a re-survey. The sixteen definitions and five assertoric claims are named in the decision's
notes; the per-claim criterion and reason stay with the session record, so a disagreement lands on a
claim rather than on a total.

## R2 — a definition's falsifier is its `test`

**Filed in the same decision**, because rule 1's enforcement cannot be drafted without it and
splitting the ruling across two nodes would separate a rule from its own precondition.

The recorded form is the one that makes it a finding rather than an interpretation: the schema
anticipated the distinction it was said to be missing — §1's three test forms are the three
definitional failure modes — and **the corpus confirms it, all four test-only claims being
definitions and no mixed or assertoric claim being test-only**. What it does not license is stated
in the same paragraph: `test` is not a general escape from `falsifier`, and the ruling that every
claim carries one stands, costed separately at I-2.

---

## R3 — `retired_from` filed; `lifecycle` booked

**Filed upstream as `DDD-dec-32`**, with the field in `spec/claim-format-2-addendum.md` and the four
values on the four claims.

### The schema

`spec/claim-format-2-addendum.md` gains a third additive field beside `canonical_home` and
`canonical_md`, under its own heading (the existing two gained one in the same edit, since the file
now carries two independent additions):

```yaml
status: retired
retired_from: established | reported | projected | unrecoverable
```

Legal only where `status` is `retired`; optional; **all format-1 claims valid unchanged**.

**The deferral is recorded with its reasoning**, per the ruling, in both the addendum and the
decision. The load-bearing sentence: `retired_from` is additive, so every existing claim and every
existing consumer stays correct, whereas `lifecycle` removes a value from `status`'s range and
thereby **changes what an unchanged claim file means to an unchanged consumer** — a format version's
work, not an addendum's. The successor item adds what a format-2 session must then decide and this
one did not: under `lifecycle` the unrecoverable cases land in `status` itself, which is mandatory,
so they need either a `status: unknown` value or a stated convention. **`lifecycle` forces them into
the open where `retired_from` lets them stay quiet, and that is an argument in its favour.**

### The four values

| Claim | `retired_from` | Provenance recorded in `notes` |
|---|---|---|
| `DDD-measure-06` | `established` | its own preserved field block, **confirmed independently against git** at `f9c1534` |
| `DDD-frame-15` | `projected` | git: filed at `projected` at `dba00c5`, held to the Phase 1a retirement at `c73c463` |
| `DDD-frame-09` | `unrecoverable` | search recorded — see below |
| `DDD-measure-08` | `unrecoverable` | search recorded — see below |

**The search, recorded verbatim on both unrecoverable claims:** already `retired` in this
repository's first commit (`f9c1534`, `v5.0.0`, 2026-08-05) carrying `changed: v4.5`, so the status
transition predates the repository; git history searched (each claim's whole history is one commit,
at `retired`); the downstream seed `meta/seed/claims-seed.yaml` searched, and also carries them at
`retired`; `CHANGELOG.md` searched, and records what each retirement *corrected* and never what the
node *was*.

**Nothing is inferred, including from the v4.5 changelog entries.** The decision says so in its
*deliberately not done*, in the ruling's own terms: a recorded loss is a fact, and a guessed status
would then read as authoritative — the graph would assert something nobody knows, in a field an
outside reader trusts precisely because the rest of it is checked.

**The field's first test passes.** Can a reader see, from the graph alone, that `DDD-measure-06` was
once `established`? With `retired_from: established` in the header: yes — as a field, queryable, and
without depending on a notes block written by a session that happened to be thorough.

### One thing deliberately left for Gate 3

**Whether `retired_from` becomes mandatory on `retired` claims is validator work**, and it is not
ruled here. Rule 2 currently requires `supersedes` or a `notes` entry on a retired claim and is
untouched. The decision records the deferral rather than assuming it; the proposal goes to Gate 3
beside A1, A2 and B1, where it belongs with the other enforcement questions.

---

## Found in passing, not touched

**`spec/claim-format.md` exists in both repositories and the copies have drifted.** The upstream file
carries a §5 interpretation note that the downstream copy does not; nothing else differs, and nothing
states which governs when they disagree. Filed as successor item 4. The `retired_from` field does not
widen it — `spec/claim-format-2-addendum.md` is upstream-only, so the field sits in a file the
downstream copy never had.

---

## Gates, both repositories

| | upstream | downstream |
|---|---|---|
| `validate-core-order.py core/` | 0 errors, 66 warnings (59 W1, 7 W2), **zero W4** | 0 errors, 0 warnings |
| `validate-claims.py core/claims/` | valid: 63 | valid: 26 |
| `validate-claims.py core/decisions/ --decisions` | **valid: 11** (was 9) | valid: 21 |

Warning counts are unchanged from Gate 1 in both repositories.

---

## Held at GATE 2

| # | Held for ruling |
|---|---|
| **R8** | `DDD-dec-31` and `DDD-dec-32` as drafted — two decisions rather than one, R2 folded into the I-1(a) decision because it is that rule's precondition. |
| **R9** | The `retired_from` value set — `established · reported · projected · unrecoverable`. `reported` is legal and currently unused; retained so the set matches `status`'s live range rather than only what the four claims need. |
| **R10** | Successor item 4 (the drifted spec copies) — filed as found, or ruled out of the programme's interest. |
