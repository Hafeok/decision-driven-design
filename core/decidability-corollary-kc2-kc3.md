# The Decidability Corollary: Zero-Floor ⇒ KC2 + KC3

<!-- Naming: KC = Knowability Claim. KC1 finiteness, KC2 membership decidability,
     KC3 loop termination. "KC" is used throughout the DDD completeness core to avoid
     collision with field-K, completeness constants, and Knaster–Tarski. Spell
     "Knowability Claim" in full on first use in any external paper. -->

> Insertion block for `core/02-completeness`. Discharges the remaining two knowability claims — membership decidability (KC2) and encode–exercise loop termination (KC3) — for purely digital actions, as a corollary of the zero-floor postulate. Unlike the finite-index lemma, this block introduces **no new content**: it reads existing canon (zero-floor postulate, its proof program, the descent measure) into the knowability frame.
>
> **Depends on:** `core/03-the-polanyi-floor` (zero-floor postulate, intrinsic/transfer floor, proof program = termination of encode–exercise iteration, descent measure = unencoded demand mass); `core/02-completeness/finite-index-lemma` (KC1, τ-live membership test); `core/01-the-law` (four stores, acceptance predicate, last wind).

---

## 1. The three claims, and what remains

"The governing decision set of a software action can be known" is three claims, not one. Call them the three **Knowability Claims (KC1–KC3)** — "KC" throughout, to avoid overloading `K`:

```
KC1  finiteness              |D(t,α)| < ∞                         — finite-index lemma
KC2  membership decidability  d ∈ D(t,α) is decidable             — this block
KC3  loop termination         encode–exercise converges; esc→esc_wind is reachable
                             and detectable                       — this block
```

KC1 was proved independently of digitality (`KC1 ⊥ zero-floor`). KC2 and KC3 are the two that *require* the zero-floor condition, and they fall out of canon already present in `core/03`. This block does the reading; it postulates nothing.

**The zero-floor condition (restated from `core/03`).** An action has intrinsic floor zero iff its governing decision set **and** its acceptance predicate both close over digital state. For such an action, the experience of the action is itself serializable data — Polanyi's precondition (unsharable experience → unsharable decisions) never obtains, so no decision is intrinsically actor-locked.

---

## 2. KC2 — membership decidability

**Claim.** For a zero-floor action, membership `d ∈ D(t,α)` is decidable.

**From canon.** The finite-index lemma already gives the membership test:

```
d ∈ D(t,α)   iff   ∃ v, v' ∈ dom(d):  ‖ outcome(v) − outcome(v') ‖ > τ
```

This test is *decidable* precisely when two objects are effectively computable/searchable:

- `outcome(·)` — the outcome map must be a computable function.
- `dom(d)` — the decision's domain must be effectively enumerable/searchable.

The zero-floor condition supplies exactly these two, and nothing else is needed:

- **Governing decision set closes over digital state ⇒ `dom(d)` is a typed digital space** — finite or effectively enumerable, hence searchable. A decision over digital state has a domain that is itself digital state.
- **Acceptance predicate closes over digital state ⇒ `outcome(·)` composed with `A` is a program** — `outcome(v)` is producible and `‖ outcome(v) − outcome(v') ‖ > τ` is evaluable, because outcome space and the τ-comparison both live in serializable state.

So the membership test reduces to a (possibly expensive) decidable search over a digital domain with a computable predicate. **KC2 holds.**

**KC2 is the zero-floor postulate wearing a second hat.** The postulate says: digital closure ⇒ Polanyi's precondition never obtains ⇒ no decision is unsharable ⇒ every governing decision is in principle inspectable. "In principle inspectable" *is* membership decidability. The two statements are the same fact — one phrased about tacit knowledge, one phrased about a decision procedure. This block adds no premise; it renames one.

**Scope, stated honestly.** Decidable ≠ tractable. The search over `dom(d)` may be astronomically large; KC2 asserts a decision procedure exists and terminates, not that it is cheap. Cost is a separate axis (the token/capacity projection), not a knowability claim. And for a *non*-zero-floor (physical) action, `outcome(·)` is not a program and `A` is actor-relative — the test is no longer decidable in general. KC2 is bounded exactly to the zero-floor condition; outside it, membership is at best actor-relatively decidable, matching the actor-relativity caveat in the action definition.

---

## 3. KC3 — loop termination

**Claim.** For a zero-floor action, the encode–exercise loop terminates: `esc` is driven to `esc_wind`, that limit is reachable, and reaching it is detectable. Under zero-floor, `esc_wind → 0`, so the loop terminates at complete knowledge.

**From canon.** `core/03` already states the proof program and the descent measure:

```
proof program           = termination of the encode–exercise iteration
candidate descent measure = unencoded demand mass  (the law itself as termination measure)
```

Read as a well-foundedness argument, this is KC3 directly.

**The loop.** One cycle: exercise the action → observe escaped decisions (residual surfacing as output, per the escape-under-pressure canon) → encode them (relocate `esc → enc/mech`) → re-exercise. Define the loop variant:

```
Φ(n)  =  unencoded demand mass after cycle n
       =  |D|  −  E(n)                    (E = enc ∪ mech, encoded mass after cycle n)
```

**Well-foundedness.** Each cycle that discovers and encodes at least one escaped decision strictly decreases Φ:

```
E(n+1) > E(n)   ⇒   Φ(n+1) < Φ(n)
```

Φ is bounded below. Its lower bound is **not** zero in general — it is the wind floor:

```
Φ  ≥  esc_wind   =  intrinsic floor mass
```

A strictly decreasing sequence over a well-founded order with a floor terminates. **The loop terminates at `Φ = esc_wind`.** For an arbitrary actor/task this is termination *at the floor*, not at zero — which is the correct, general statement (KC3 does not claim zero-escape; it claims a reachable, detectable limit).

**Zero-floor collapses the limit to zero.** The zero-floor condition asserts intrinsic floor = 0. Then:

```
esc_wind  =  intrinsic floor mass  =  0        (zero-floor)
⇒  Φ terminates at 0
⇒  the loop reaches complete encoding: every governing decision encoded, esc = 0
```

So under zero-floor the loop terminates at **complete knowledge of `D`**, not merely at a floor. This is what makes the maturation asymptote `(1 − floor) = 1` for purely digital task types — the same fact, read on the recurrence projection. **KC3 holds, and its zero-floor specialization is exactly the maturation asymptote already in canon.**

**Detectability.** Termination must be *detectable*, or "we can know we're done" fails even when the loop converges. Detection is a fixed point of the loop, not a guess:

```
a cycle exercises the action and discovers no new escaped decision   ⇒   Φ unchanged   ⇒   fixed point
```

Under zero-floor, a fixed point with `esc = 0` is decidable *because* `esc = 0` is itself checkable — escaped decisions surface as output, and "no escape surfaced under exercise that covers the τ-live subspace" is a decidable condition when outcome and acceptance close over digital state (KC2 again). So detection reduces to KC2 applied to the loop's stopping test. **Detectability inherits from KC2** — the two claims are not independent; KC3's detectability *is* KC2 applied to the termination predicate.

For a non-zero-floor action, the fixed point sits at `esc_wind > 0`, and detecting it is the flat-derivative signal (`Δesc/Δencode ≈ 0` with residual) from the cost metric — reported, actor-relative, not a clean digital check. Again KC3's strength tracks the zero-floor condition exactly.

---

## 4. The knowability theorem, assembled

KC1 (finite-index lemma) + KC2 + KC3 (this block) compose:

> **Knowability Theorem (software).** For an action `t` whose governing decision set and acceptance predicate close over digital state (zero-floor condition), and whose outcome map is τ-finitely-sensitive at assurance level α (finite-index condition), the decision set `D(t,α)` is:
> - **(KC1)** finite — `|D(t,α)| < ∞`;
> - **(KC2)** membership-decidable — `d ∈ D(t,α)` is decidable by a computable search;
> - **(KC3)** the encode–exercise loop terminates at `esc = esc_wind = 0`, detectably.
>
> Hence `D(t,α)` is effectively knowable, and complete encoding (`esc = 0`) is reachable and detectable.

**Two named premises, cleanly separated:**

```
finite-index condition  (τ-finite sensitivity of outcome)   →  KC1        [⊥ zero-floor]
zero-floor condition    (digital closure of decisions + A)  →  KC2, KC3
```

Neither premise is smuggled; both are falsifiable properties of the action, not assumptions about the framework. KC1's premise is about the outcome map's sensitivity spectrum; KC2/KC3's premise is about digital closure. They are independent — a task can satisfy one and fail the other:

- τ-finite but not digitally closed (a physical action with finite outcome-sensitivity): finite `D`, but membership only actor-relatively decidable, loop terminates at `esc_wind > 0`. Knowable *in count*, not *completely encodable*.
- digitally closed but not τ-finite (a bit-exact-against-unbounded-stream digital task at tight τ): decidable membership and zero-floor termination *per decision*, but infinitely many decisions — `|D|` unbounded. Every decision knowable, the *set* not finite.

Complete effective knowability needs **both** premises. That is the honest boundary of the claim, and it is exactly the two-lemma structure the canon has been building toward.

---

## 5. What this block did and did not do

- **Did:** read the zero-floor postulate, its proof program, and its descent measure — all already in `core/03` — into the KC2/KC3 slots, and showed KC3's detectability is KC2 applied to the stopping test.
- **Did not:** introduce any new postulate. The only genuinely new mathematical content in the knowability arc remains the finite-index lemma's τ-finite-sensitivity condition (KC1). KC2 and KC3 are corollaries; the zero-floor postulate is the single premise doing the work, and it was already load-bearing in the floor file.
- **Open, inherited from `core/03`:** the zero-floor postulate is itself *projected, falsifiable, below the current evidence line*. This block's KC2/KC3 are therefore as sound as the postulate — no more, no less. If the postulate falls (a digital action found with irreducible non-serializable decision content), KC2/KC3 fall with it, and the knowability theorem retreats to "finite and floor-terminating" without the `esc = 0` conclusion. The dependency is stated so nothing here claims more certainty than the postulate it rests on.
