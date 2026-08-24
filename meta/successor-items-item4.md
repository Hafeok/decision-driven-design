# Successor items — item-4 session (2026-08-25)

Items raised at the item-4 session and deliberately **not** taken there. Each names the node or
document it lands against and the reason it was not done in-session. Nothing here is filed canon.

---

## 1. Split the eight mixed claims, then split `conceptual`

**Ruled at GATE 1 (Emil): file nothing in `kind` now; split first. Filed as `DDD-dec-31`.**

Sixteen of the twenty-nine `conceptual`/`projected` claims are definitions in the reviewer's sense,
five are assertoric, and **eight carry both a separable stipulative limb and a separable assertoric
limb**. The split is real. It is not fileable, because the boundary runs through those eight rather
than between them, and a `kind` value assigned before they are split miscodes whichever job it does
not name — in a field an outside reader takes as authoritative.

**The order is fixed by an asymmetry, not a preference** (Emil, at the ruling): a `kind` value is
cheap to add and expensive to undo. Once `definitional` exists and sixteen claims carry it, the
later adjudication is constrained by what has already been filed. Splitting first leaves the
assignment free.

**The eight, so the successor starts from a list rather than a re-survey:**
`DDD-cost-01`, `DDD-cost-09`, `DDD-cost-12`, `DDD-cost-20`, `DDD-cost-25`, `DDD-frame-11`,
`DDD-frame-14`, `DDD-frame-17`.

**`DDD-frame-17` is the named first target, and the reason should not be softened.** It was filed
this month, at `v5.10.0`, as the successor built to cure `DDD-frame-15`'s compoundness — and it is
already known-compound, at three limbs: a stipulated taxonomy, an exhaustiveness claim, and the
compact form carried over from the claim it replaced. **A repair authored under a rule the validator
does not check reproduces the defect it repairs.** That is evidence for the sequencing rather than
against the claim, and it is the same argument the freight item makes about `DDD-measure-06` — which
is why the two items sat on one surface in this session.

`DDD-frame-11` is the second target and the clearest diagnostic in the corpus: **its `falsifier`
field already carries two limbs of different type**, one definitional and one empirical. The claim
reports that it is two claims.

**Why it was not done here.** Splitting a claim edits its statement, which this session forbids by
construction — the session precedes the ground migration precisely so that it touches headers only
and the migration never re-touches what it just edited. Each split also needs its own ruling.

**Lands against:** the eight claims upstream; then `spec/claim-format.md` §1's `kind` enumeration,
and `validate-claims.py`'s `KINDS` set in both repositories.

---

## 2. `lifecycle` as a format-2 candidate

**Ruled at GATE 1 (Emil): `retired_from` now, `lifecycle` booked. Filed as `DDD-dec-32`.**

The conceptually correct disposition, and the ruling says so: a `lifecycle: active | retired` field
orthogonal to maturity, letting `status` keep the maturity the claim actually held, so
`DDD-measure-06` reads `status: established, lifecycle: retired`. The item-4 diagnosis is that a
lifecycle state is sitting in a maturity field; `lifecycle` removes it from there, and
`retired_from` adds a second field to compensate for its still being there.

**Deferred on a difference in kind, not size.** `retired_from` is additive — optional, fires only on
`retired` claims, four files touched, no backfill, every existing consumer stays correct.
`lifecycle` removes `retired` from `status`'s range, so an unchanged claim file means something
different to an unchanged reader, and every consumer of `status` changes with it: the appendix
generator, both validators, and any external reader who learned the four values. **That is a format
version's work**, and this session's charter is one format.

**What the format-2 session must decide that this one did not:** what `status` carries for
`DDD-frame-09` and `DDD-measure-08`, whose prior maturity is `unrecoverable`. Under `retired_from`
the loss sits in an optional field; under `lifecycle` it sits in `status` itself, which is mandatory
— so `lifecycle` needs either a `status: unknown` value or a stated convention for pre-repository
nodes. **`lifecycle` forces the unrecoverable cases into the open where `retired_from` lets them
stay quiet**, and that is an argument in its favour, not against it.

**Lands against:** `spec/claim-format-2-addendum.md`, `spec/claim-format.md` §1–§2, both validators,
`gen-appendix.py`.

---

## 3. Rule 1's real enforcement — an adjudication, not a validator pass

**Ruled at GATE 1 (Emil): the B1 detector ships as a warning labelled a drafting prompt; rule 1's
enforcement is an adjudication with rulings.**

The best available mechanical detector fires on **34 of 89 claims**, and its false positives include
`DDD-measure-16` — the `established` claim Phase 1a built to cure `DDD-measure-06`'s compoundness.
A rule-1 check that fires on the repair would have blocked the fix, so the check cannot be error
class and the rule cannot be enforced by a checker alone.

**The successor is a one-off adjudication of B1's 34 hits**, each ruled split or not-split, with the
splits landing as statement edits. This session's hit list carries into it unchanged.

**Overlap with item 1 is deliberate and should not be split apart:** six of the eight mixed claims
are B1 hits, and the adjudication that splits them is the same adjudication that unblocks the `kind`
recode. One session, two outputs.

**Lands against:** the 34 claims across both repositories.

---

## 4. The two `spec/claim-format.md` copies have drifted

**Found in passing at GATE 2; not ruled, and not touched.**

`spec/claim-format.md` exists in both repositories and the copies are **no longer identical**: the
upstream file carries a §5 interpretation note ("The format as a claim-layer instance") that the
downstream copy does not. Nothing else differs.

This is a duplication with no declared authority. It is not obviously wrong — the downstream repo
validates its own claims and may want its own spec — but nothing states which file governs when they
disagree, and one has already drifted without anyone deciding that it should.

`spec/claim-format-2-addendum.md` is upstream-only, so the `retired_from` field filed this session
does not widen the divergence; it sits in a file the downstream copy never had.

**Not taken here** because it is a repository-topology decision, not a schema one, and this session
was chartered on the schema.

**Lands against:** `spec/claim-format.md` in both repositories.
