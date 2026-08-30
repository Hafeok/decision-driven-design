# Holding note entry — Q46: determination, execution, and the price of encoding

**Status:** holding. Claude-drafted from the 2026-08-26 working conversation (Emil's observation: the
closer a decision sits to an act, the clearer its verdict). Extends the 2026-08-26 addendum, Q44 and
Q45. Nothing filed.
**Blocked by:** the ground migration, as with Q40–Q45.

---

## Q46 — What encoding costs

### (a) The distinction that already exists, restated so it is not re-litigated

Canon settles act versus decision, and the settlement is **not** about latency: an act is the unit of
account, individuated by one verdict at a declared boundary; decisions are what the act is composed
of.

**Recorded because a natural-seeming alternative fails.** Defining a decision as *a determination
whose verdict is deferred* would make it a synonym for a claim — canon already holds that a claim is
an act with a deferred verdict — and would cost the individuation that makes acts countable. The
distinction below is therefore **a dimension over decisions**, not a redefinition of either term.

### (b) The mechanism: encoding separates determination from execution

**Proposed.**

- **Judgment fuses them.** An actor resolving at the act determines and executes in one motion.
- **Encoding separates them.** A filed rule determines once and executes later, at many acts.

That separation is the whole of what encoding is, seen from the time axis rather than from the
store partition — and it is what generates everything below.

**Falsifier:** an encoded determination whose execution cannot be separated from its determination —
a rule that can only be applied at the moment it is decided.

### (c) The observable: verdict distance

**Proposed.** The further a determination sits from the act it governs, the more its verdict is
**delayed, diffuse, and misattributed**:

- **Delayed** — it can only be assessed through acts that have not happened yet.
- **Diffuse** — its consequence is spread across every act it governs, rather than landing on one.
- **Misattributed** — the acts have their own resolvers and their own failures, and an encoded
  decision's contribution is the hardest term to isolate.

This is what Emil's observation names: a decision made at the act has a verdict you can see; a
decision made at architecture time has one you may never cleanly attribute.

**Note this is not a new axis.** It is the timing already in the store partition, read for its
evidential consequence rather than for its supply consequence.

**Falsifier:** encoded determinations whose verdicts are recovered as promptly and as cleanly as
those resolved at the act, at matched stake and matched act volume.

### (d) The price: ground for reuse

**Proposed, and this is the entry's centre.**

Canon prices encoding as **amortisation** — determine once, inherit at every act. It does not state
what is paid for that.

**Deciding earlier means deciding on less ground.** A determination made at architecture time is made
against *predicted* ground; the same determination made at the act has the actual material in front
of it. So:

> **Encoding trades ground for reuse.**

The trade is favourable where the ground is stable — the prediction holds across the acts governed —
and unfavourable where it moves, which is the same stability question the revalidation material
already asks about stored checks, now asked about stored *decisions*.

**This makes the encode/judge boundary an economic question with two terms rather than one.** The
benefit is act volume; the cost is ground fidelity at the moment of determination. An arrangement
encoding everything is not maximally governed — it is maximally committed to predictions.

**Falsifier:** encoded determinations over unstable ground performing as well as act-time resolution
at matched volume — the trade having no cost.

### (e) Why encoded decisions drift undetected

**Proposed, and it supplies a mechanism to something previously observed.**

(c) and (d) compose. A decision made on predicted ground can go stale when the ground moves — and by
(c), its verdict signal is delayed, diffuse and misattributed, so **nothing reports the staleness.**
The rule keeps being followed; the acts keep producing outcomes; the drift is invisible in exactly
the register that would show it.

This is the ontology-drift observation with a mechanism instead of a description: rules are not
abandoned because practitioners are undisciplined, and not only because the carving moved — but
because the feedback that would have caught the movement is structurally the weakest feedback in the
system.

**Falsifier:** arrangements where encoded-decision staleness is detected at rates comparable to
act-time error, without a dedicated instrument.

---

## Interactions

- **With the maturation material.** The descent is priced as pure gain: encode, and per-act cost
  falls. (d) says the descent has a cost that grows with ground instability, which suggests the
  curve has a floor set by prediction quality and not only by what is encodable.
- **With the predicted-ground material.** That note reached the same trade from the other side —
  determination on ground that does not yet exist. (d) is its standing-supply case: the encoded
  decision is a prediction, and everything true of predicted ground applies to it.
- **With Q40(a).** Ontology drift said *the carving moved*. (e) says *and the movement is
  undetectable*, which is why the recorded-ignore instrument is the right remedy: it manufactures the
  signal the structure suppresses.
- **With Q44(b).** Method decisions' consequences fall outside the verdict horizon; (c) says encoded
  decisions' consequences are diffuse across acts. Both are verdict-distance problems and may be one
  claim seen from two sides — worth testing whether the falsifiers are the same test.

---

## Routing

| Piece | Destination |
|---|---|
| (a) the restatement | Notes only — it exists to stop a re-litigation, not to file |
| (b) determination/execution separation | Upstream; it is a synchronic property of encoding |
| (c) verdict distance | Upstream, with (b) |
| (d) ground for reuse | **Upstream, and the highest-value piece here** — it adds a term to a claim canon already carries |
| (e) undetected drift | Downstream; it is diachronic and needs the ledger |

**One filing caution.** (d) modifies how canon prices encoding. It should be drafted as an *addition*
to the amortisation account rather than a correction of it — the benefit claim is not wrong, it is
one-sided. Filing it as a correction would misdescribe what moved.
