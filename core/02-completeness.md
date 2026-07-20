# Completeness

**What this document claims:** that the four stores are exhaustive — every governing decision lands
in exactly one — and, just as importantly, **what that claim is worth.** It is worth less than it
first appears, and saying so is the point.

---

## The exhaustiveness claim

> Every governing decision is determined by exactly one of: a **rule** (encoded), a **check**
> (mechanical), an **actor** (judgment), or **nothing** (escaped).

The argument is a case split on two binary questions:

1. **Is the determination made by something, or by nothing?**
   - Nothing → **Escaped.**
   - Something → continue.
2. **When is it made, relative to the act?**
   - Before, as a constraint → **Encoded.**
   - After, as a criterion → **Mechanical.**
   - During, by an actor reading ground → **Judgment.**

Every governing decision has answers to both questions, so every governing decision lands in exactly
one store. **The partition is complete by construction.**

---

## Why "complete by construction" is a warning, not a boast

A partition that cannot fail to be complete **carries no empirical content.** It cannot be refuted,
which means it predicts nothing — it *organises*, it does not *discover*.

This is the honest status of the four stores, and the framework states it plainly rather than
letting a reviewer discover it:

> **The four stores are ergonomics, not physics.** They are a lens for allocating and auditing
> determinations, not a claim about the world that could turn out false.

A useful lens is worth having. Much of engineering practice runs on definitional frameworks that
organise attention well (the OSI layers, the CAP triad, the essential/accidental split). But a
definitional framework must not be dressed as a discovery, and the "conservation" language is
exactly the dress that invites the mistake. See `01-the-principle.md` on the register question.

---

## The genuine content is at the edges

The partition itself is empty. Three things *around* it are not, and these are where the framework
earns its place:

### 1. The escaped store exists and is usually invisible

Prior allocations (Tesler: user / developer / platform) have **no bin for "nobody."** They assume
every decision is made by *someone* and ask only whom. The escaped store's contribution is the claim
that **"decided by nobody" is a real, common, and the most expensive** allocation — and that it is
invisible precisely because nothing occupies it. Naming it is what makes it auditable.

### 2. The stores have asymmetric costs

The partition says nothing about cost; the framework does (`01`, §"cost asymmetry" and §"escape is
free"). Encoded is cheap-to-state / expensive-to-find; mechanical pays the executability tax;
judgment doesn't amortise; **escape is the only store free at the moment of decision** — which is why
demand drifts into it. These are claims *about* the partition, not the partition itself, and they are
not definitional.

### 3. Redundancy is permitted; only uncovered-and-unpriced is forbidden

A single governing decision may be held in more than one store — a constraint before *and* a
criterion after. This is not double-counting; it is defence in depth, and the principle permits it.
What the principle forbids is a governing decision that is **in no store at all** — uncovered, and
with its cost unpaid. That is the escaped state, and it is the only forbidden one.

---

## The boundary of a "governing decision"

Completeness is only meaningful relative to what counts as a governing decision, and that is set by
the **assurance level** (`00`, admission tests):

> A choice is a **governing decision** iff varying it moves the outcome **past tolerance**.

Below tolerance, a choice is not a governing decision and is not in the accounting at all — it is
*substrate*, inspected in order to act, not demand to be allocated. This is what keeps the store
count finite (see the finiteness argument in `03-the-floor.md`, which depends on it): raise the
assurance level and more choices cross into the governing set; lower it and fewer do. The partition
is complete *at a declared tolerance*, and undefined without one.

---

## What this does not establish

- It does **not** establish that demand is conserved. Completeness says every decision has a store;
  conservation says the *total* is fixed within a decomposition. Different claims; conservation is
  the weaker-supported one (`01`, and `meta/lineage-and-limits.md`).
- It does **not** establish that the stores are the *right* four rather than some other complete
  partition. A different pair of binary questions would yield a different complete partition. We
  claim these four are *useful*, not that they are *forced*.

---

## The one line

> **Every governing decision has a store — trivially, by construction. The content is not the
> partition but its edges: that one store is "nobody," that the stores cost asymmetrically, and that
> the free one is where everything drifts.**
