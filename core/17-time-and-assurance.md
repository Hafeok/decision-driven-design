# Time as a factor of assurance

<!-- ddd:contract

requires: [act, capability, calibration-ledger, maturation]
establishes: []
status: settled
-->

**The time register.** The act gives assurance a time axis: before, during, and after exist only
relative to a bounded episode. The synchronic member of this set — tempo pruning assurance
positions — is upstream canon (`DDD-cost-25`, pinned); everything below persists between acts and
files here under the boundary charter (upstream `DDD-dec-09`; `DDD-dec-10`/`DDD-dec-11` here).
Four mechanisms, kept apart deliberately.

<!-- ddd:ref id=DDD-cost-25 -->

**Claims.**

| Section | Proposition | Claim | Status |
|---|---|---|---|
| §1 | The verdict gap is carrier-bridged: a late-closing predicate is open at act time | `DDD-cost-26` | projected |
| §2 | Mechanical assurance decays at the drift rate of the ground it read | `DDD-cost-27` | projected |
| §3 | Carrier assurance accrues at verdict speed; the turnover bound | `DDD-cost-28` | projected |
| §4 | Ground assurance has three suppliers; detection class and recon cadence are substitutes | `DDD-cost-29` | projected |

Where this prose and a claim disagree, the claim governs and the prose is the bug.

**Reproduction script** in `core/assets/recon-cadence-demo.py` (§4).

---

## 1. The verdict gap is carrier-bridged

Operational closure already includes latency bounds (upstream canon, v4.5) — this section reads
that time index at the act. **A late-closing predicate is open at act time: the check exists but
has not happened, so assurance across the verdict gap can only be carried — every declared
verdict horizon is a declared span of carrier-borne assurance.** *(Claim `DDD-cost-26`,
projected; partially held by existing canon, noted.)*

---

## 2. Mechanical assurance decays

**Mechanical assurance decays at the drift rate of the ground it read: a passing check is a
stored statement about uncontrolled ground, so assurance is assurance-at-time; re-verification
cadence is the standing cost of holding assurance above the declared level.** *(Claim
`DDD-cost-27`, projected; the revalidation-cadence half is held by existing canon, noted.)*

Expiring certifications and rotting test suites are one phenomenon at two layers. The sclerotic
branch of maturation (`14` §2) is this decay outrunning re-supply.

---

## 3. Carrier assurance accrues at verdict speed

**The calibration ledger (`16`) builds only from matured verdicts, so an open-class instrument
has a minimum build time set by verdict latency and required sample count — parallel claims
compress the count term, never the latency floor — and when claimant turnover outpaces verdict
latency, carrier assurance cannot accumulate.** *(Claim `DDD-cost-28`, projected.)*

This is the mechanism behind `DDD-cost-24`'s validity condition: open-class actors are slow to
produce for a second reason — the assurance evidence itself arrives at verdict speed. Model
versions churn faster than open-claim verdict horizons, so the ledger certifies only claimant
identities that outlive their horizons; cross-identity transfer is partial at best and
per-capability (`DDD-dec-14`, the identity-unit question, open).

---

## 4. Ground assurance and the recon cadence

A check verifies the resolution against declared ground, so a valid verdict on poisoned ground
is wrong with full authority (upstream canon). Ground assurance is therefore a distinct
requirement with its own three suppliers, and a substitution law between two of them:

> **Ground assurance has three suppliers — encoded (validators, freshness constraints), carried
> (the actor's anomaly-detection capability), and occasioned (recon: fresh observation at a
> cadence) — and carrier detection class and recon cadence are substitutes: weaker actors
> require more frequent ground checks, the cadence computable from the decay machinery (§2):
> exposure per act ≈ λ·t·(1−d)·(1−c) held under the assurance-implied bound, with λ the drift
> or adversary rate, d detection class, c encoded coverage.**

*(Claim `DDD-cost-29`, projected.)* Degenerate actors have zero detection class — which is why
classical practice obsesses over input validation: predicted, not assumed. Adversary tempo
compresses all cadences and makes detection class dominant, since the attacker sets λ.

**The prompt-injection instance.** Prompt injection is poisoned ground meeting insufficient
detection class at zero recon cadence — agent defence is a ground-assurance budget across the
three suppliers, not a prompt trick.

**Reproduce.** `core/assets/recon-cadence-demo.py` — stipulated coefficients; ~35× recon-interval
spread across actor classes (1.2 days for a degenerate rule-executor to 41.7 days for a
specialist with cross-checks), adversary tempo compressing all cadences tenfold. The script
exercises the substitution law; it does not test the correspondence.
