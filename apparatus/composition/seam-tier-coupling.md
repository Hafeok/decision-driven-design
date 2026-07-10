# Seam × Tier Coupling

> Where the composition laws meet the tier–specification inverse law. Unencoded seam relocates onto per-run judgment (seam-demand identity); relocated judgment past the transfer floor lands on the intrinsic floor (tier law); the intrinsic floor answers only to selection. The consequence: **composition raises required actor tier at the boundary, and the interface contract is the one-time specification that buys it back.** This is also the point where the two accounting ledgers — demand (decisions/tier) and capacity (tokens/context) — meet on the same object.
>
> **Location:** `apparatus/composition/seam-tier-coupling.md`. Closes the open slot named in `partition.md` §9 and `seam-allocation.md` §8.
> **Depends on:** `core/01-the-law` (seam-demand identity `|D_comp| = |D_single| + |S|`; four stores; judgment store); `core/03-the-polanyi-floor` (floor = intrinsic + transfer; tier–specification inverse law L1–L3); `apparatus/composition/partition.md` and `seam-allocation.md` (the four seam kinds); the MCP token/decision ledger (capacity accounting).

---

## 1. The coupling, mechanically

Both laws are already proved; the coupling is their composition. The seam-demand identity supplies a `ΔJ`; the tier law consumes it.

```
[seam-demand identity §3]   seam not encoded  →  it relocates onto per-run judgment:
                            ΔJ_boundary = +|S_unencoded|

[tier law L2]               judgment demand past the transfer floor lands on the intrinsic floor:
                            if J_boundary > transfer-floor capacity → residual on intrinsic floor

[tier law L3]               the intrinsic floor answers only to selection, not training:
                            required tier AT THE BOUNDARY rises; met only by a selected actor
```

Chained:

> **Seam–Tier Coupling.** Unencoded seam demand relocates onto boundary judgment; where it exceeds the transfer floor, it lands on the intrinsic floor and raises the actor tier required *at the seam*, meetable only by selection. Encoding the seam reverses the chain: it moves `S` back to the encoded store, drops boundary judgment below the transfer floor, and lowers the tier the seam requires.

That is the whole mechanism. The three sections that follow are the consequences neither law shows alone.

---

## 2. Tier pressure is local to the seam, not global to the action

The tier law as stated in `core/03` treats one action, one actor, one floor. Composition breaks the action into parts, and the seam identity locates the manufactured demand `S` **at the boundaries** between parts. So the relocated judgment — and therefore the tier pressure — is **spatially concentrated at the seams**, not spread over the action.

```
interior of each Dᵢ :  reach demand only; can be owned by a LOW-tier actor
the boundaries (S)   :  relocated judgment (if unencoded); demands tier AT THE SEAM
```

**Consequence.** A composition's tier profile is non-uniform. The actors doing the interior of each part can be junior; whoever owns the *boundary* — integration, handoff, arbitration — needs the tier the unencoded seam demands.

> This derives why integration roles, interface owners, and system-integration leads are senior even when component work is junior: the unencoded seam relocates its judgment onto the boundary owner's intrinsic floor. The framework predicts the seniority sits *at the seams*, and predicts *which* seams (the unencoded, high-coupling ones), not uniformly across the team.

Each of the four seam kinds concentrates tier at its own location:
```
reach seam (interface)      → tier at the integration boundary
speed seam (cut-assumption)  → tier at the cut point (who owns the assumption's validity)
assurance seam (aggregation) → tier at the aggregator (who adjudicates disagreement)
failover seam (arbitration)  → tier at the handover (who owns first-success + contamination check)
```

---

## 3. The non-additivity: composition can raise total tier while lowering per-actor reach

This is the trap neither law shows alone, and the sharpest result of the coupling.

Partitioning an action is motivated by **reducing reach demand per actor** — each owns a smaller `Dᵢ` (that is the reach allocation, `partition.md`). But the partition **manufactures `|S|`** (seam identity), and unencoded `S` **raises tier demand at the boundary** (§1). These act on different axes and different actors:

```
partition's two opposite effects:
   reach demand per actor :  ↓   (smaller Dᵢ — the intended gain, on interior actors)
   tier demand at the seam:  ↑   (unencoded S → boundary intrinsic floor — the hidden cost)
```

They do not net, because they are different currencies (reach vs tier) landing on different actors (interior vs boundary). Therefore:

> **A decomposition that makes every piece individually easier can require a *more expert* actor than the undivided action did** — because the undivided action had no seam, and the divided one relocated seam demand onto an intrinsic floor at a boundary that nobody had to staff before.

This is "no free decomposition" restated in **tier currency**. The partition block stated it in decision currency (`|D_comp| = |D_single| + |S|`); the coupling states its consequence: the extra `|S|`, if unencoded, is not just more decisions — it is *higher-tier* decisions, concentrated at boundaries, meetable only by selection. A team can be cheaper per-head and more expensive in total tier than a single broader actor. When it is, the decomposition was a false economy.

**Design reading.** Decompose only when either (a) the action is genuinely reach-bound and no single actor can hold it, or (b) you will *encode* the seam (§4) so it never reaches the boundary intrinsic floor. Decomposing a reach-feasible action and leaving its seam unencoded is the characteristic false economy: you paid interface `|S|` in raised boundary tier for a split you did not need.

---

## 4. The interface contract: one-time specification that buys down boundary tier

By tier-law L3, once seam demand sits on the intrinsic floor, training cannot lower it — you are paying for **selection** (a senior boundary owner) on **every run**. The seam identity §3 gives the alternative lever: **encode the seam.**

```
two ways to meet the tier a seam demands:
  (a) SELECT a senior actor to own the unencoded seam   — recurring cost, per boundary, per run
  (b) ENCODE the seam once (interface contract /          — one-time specification cost,
      precondition / aggregation / cancellation protocol)   amortized over all runs
```

Encoding moves `S` from judgment back to the encoded store → boundary judgment drops below the transfer floor → the tier the seam requires falls to what training (or a junior actor) can meet.

> **The interface contract is a one-time specification cost that permanently lowers the tier required at a boundary**, substituting encoded specification for a recurring per-run selection cost.

This is the economic derivation of **producer-owns-the-seam** (RFC 0001): the producer encodes the boundary not as a courtesy but because encoding it once is cheaper than every downstream consumer fielding a selected senior actor to decide it per-run. Authorship is directional (producer writes the contract) precisely because the producer is the party positioned to move `S` into encoding before it ever reaches a consumer's boundary judgment.

It is also the tier-currency reading of the tier–specification inverse law itself: **withholding seam encoding is withholding specification, and by the inverse law that raises the required tier — here, at the boundary.** The seam is just the location where composition makes the inverse law bite locally.

---

## 5. Where the two ledgers meet: the seam is one object on both

The coupling is also the junction of the two accounting systems. Every seam is **simultaneously** a demand-side and a capacity-side object:

```
one seam, two ledgers:
  DEMAND side   : |S| governing decisions, priced in TIER (who must own the boundary — §1–4)
  CAPACITY side : the tokens that cross the boundary — the ground transmitted into the next
                  actor's context window so it can act (MCP token/decision ledger)
```

For a model actor this is literal: the seam *is* what crosses the context window at the handoff. So the seam is exactly where demand accounting and capacity accounting meet on the same physical object.

**Unencoded seam is expensive on both ledgers at once:**
```
demand side   : boundary tier ↑ (relocated judgment on intrinsic floor)
capacity side : tokens ↑ (the ambiguous boundary state must be carried in full into the
                downstream actor's window so it can make the relocated judgment)
```

**Encoding the seam pays down both ledgers with one artifact:**
```
demand side   : tier ↓  (the boundary decision is pre-made — encoded store)
capacity side : tokens ↓ (the contract is a compressed schema, not raw boundary state —
                fewer tokens cross the seam to convey the same governing content)
```

> **The interface contract is the single artifact that reduces both the demand ledger (boundary tier) and the capacity ledger (transmitted tokens).** It is where "encode the seam" is simultaneously a tier-reduction and a context-compression. The MCP token/decision ledger is the instrument that measures both effects on the same seam: decisions relocated (demand) and tokens saved (capacity) per contract.

**Coupling law (ledger form).**
```
for a seam s:
   unencoded:  cost(s) = tier_premium(boundary owner) · runs   +   tokens(raw boundary state) · runs
   encoded:    cost(s) = spec_cost(contract) [once]            +   tokens(schema) · runs
   encode s  iff  spec_cost(contract)  <  (tier_premium · runs) + (tokens_raw − tokens_schema) · runs
```
The contract pays off when its one-time specification cost is less than the recurring dual-ledger cost of leaving the seam open — a threshold that falls (contract more likely worth it) as run count rises. High-traffic seams should always be encoded; one-shot seams may not clear the threshold. This is the instrumentable decision the MCP ledger exists to make.

---

## 6. Summary

```
seam–tier coupling  =  seam-demand identity (ΔJ at boundary) ∘ tier inverse law (J → intrinsic → selection)

consequences beyond either law alone:
  §2  tier pressure is LOCAL to the seam (integration roles senior; interior junior)
  §3  NON-ADDITIVITY: decomposition can raise total tier while lowering per-actor reach
      (no free decomposition, in tier currency)
  §4  interface contract = one-time spec that buys down recurring boundary-selection cost
      (economic derivation of producer-owns-the-seam)
  §5  the seam is ONE object on TWO ledgers; the contract pays down both
      (demand: boundary tier; capacity: transmitted tokens) — the MCP-instrumentable junction
```

---

## 7. Open slots

- **`tier_premium` and `spec_cost` estimators.** The ledger-form coupling law (§5) prices selection premium and contract specification cost; neither estimator is given. Both must be declared before any reported encode/don't-encode verdict. Projected. The `tier_premium` estimator couples to the intrinsic-floor measurement (qualification testing) already open in the tier law.
- **Run-count dependence.** §5's threshold falls with run count; this makes seam-encoding decisions *traffic-dependent*, which the static `|S|` ledger does not capture. Whether the demand ledger should carry a run-count weight is unresolved and interacts with the maturation/recurrence projection.
- **Token/decision exchange rate.** §5 sums a tier premium (demand currency) and a token cost (capacity currency) in one inequality, implying a conversion between them. The exchange rate (what a boundary-tier premium is worth in tokens, or both in a common cost unit) is not defined; the MCP ledger must fix a common denomination or keep the two ledgers separate and decide lexicographically. Load-bearing open question for the ledger design.
- **Multi-hop seams.** A pipeline (speed allocation) has seams in series; relocated judgment may compound along the chain (each stage's unencoded seam raising the next stage's boundary tier). Whether tier pressure is additive, max, or compounding along a multi-hop seam is not derived here.
