# DDD — Consolidated State (software projection)

**Scope.** This is the **software-projection** repository's consolidated state. The shared,
actor-general framework claims — the two primitives, the four stores, conservation, the floor, the
actor model, the measure, determination-vs-intelligence — are **canon in the principle repository**
and are **not restated here**. For their authoritative status read the principle repo's
`meta/consolidated-state.md`; this repository pins the specific claims it depends on in
`graph/upstream.yaml`. Where a shared claim and this document ever disagree, the principle repo
wins.

This document records only what is **local to the software projection**: the outreach corrections,
the product backlog, and the organisation-design projection (a directory per `DDD-dec-05`).

---

## 1. Organisation design (projection)

Four projected, session-authored claims, held as a directory (`applications/organizations/`), not a
repository. Statements and falsifiers are in `applications/organizations/README.md` and the claim
files `core/claims/DDD-org-01..04`. All rest on principle-layer discipline pinned upstream. Promotion
to a repository requires core-like documents and an identified external checker (`DDD-dec-05`).

---

## 2. Corrections to the LinkedIn plan

The eight-post sequence stands, with three edits:

- **Post 4** (*spec ops earned the tier, your consultancy didn't*) — keep, but the mechanism is now
  **predicate closure**, not "adversarial ground." *Spec ops carries judgment because the acceptance
  predicate does not close; consulting carried judgment because nobody wrote the check.* Sharper, and
  it is now the same claim as §1.8.
- **Post 6** (*Every decision gets made*) — **do not present conservation as a discovery.** Present it
  as *"Tesler said this in the 80s about complexity. Here it is in decisions, with a fourth bin he
  didn't have — the one where nobody decides."* **The escaped store is the post.** Leading with a
  law you can't measure invites the exact rebuttal a sharp reader will reach for.
- **New post 9** (*Training vs. selection*) — **the strongest post in the set, and it was not there.**
  *"You can train a surgeon. You cannot train an elite soldier — you must select one. The difference
  is not difficulty. It is whether you can check the work."* Recognisable, counterintuitive, testable,
  and it introduces the actor model without vocabulary.

---

---

## 3. Product — what is still owed

**Product (see `ground-prd.md`):** rebuild Bicep on **compile-then-evaluate** (P0 — the current regex

---

## 4. The split

Executed per `DDD-dec-04..07`. The actor-general canon moved to the principle repository
(`actor-indexed-determination`) at tag `v5.0.0`; this repository became its software projection and
kept the name. No claim's status changed in the split. Cross-repo dependencies are pinned and
status-checked in `graph/upstream.yaml` (basis-loss detection, `DDD-agent-01` applied to repos).
