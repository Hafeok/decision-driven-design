# Prefix Stability

**Location:** `apparatus/prefix-stability.md`. Connects the caching invariant already shipped in the
reference tooling (`ground` PRD, INV-6) to the theory that now explains it. Depends on the
encode/verify split (`apparatus/encode-verify.md`), the measure (`core/08`), and the floor mechanism
(`core/09`). Verification: `assets/prefix-stability-check.py` (brute-forces all orderings and
confirms the rule in §3, including the case that falsifies the naive version).

**Standing on:** **Robert C. Martin, the Stable Dependencies Principle** (*Agile Software
Development*, 2002; and the package-design papers of the mid-1990s) — *depend in the direction of
stability.* The ordering rule below is SDP; what this note adds is a substitute instability metric
that fits a prefix, a derivation that the ordering is optimal, and the observation that the cache
turns SDP violations into a **detector** for mislocated encoding.

---

## 1. A prefix is a dependency graph

Causal attention makes every token after position `k` depend, structurally, on every token before it.
A cached prefix is therefore a **totally ordered dependency chain** — not by convention, but by
mechanism.

Martin's rule applies directly: **depend in the direction of stability.** Volatile content placed
early means stable content depends on it, and every change to the volatile part invalidates
everything downstream.

This is why the reference tooling emits **ground → settled decisions → task** (INV-6), and it is not
an arbitrary convention. It is descending stability:

| Segment | Stability | Changes when |
|---|---|---|
| **Ground** | most stable | the world moves — slowly, and not because of you |
| **Settled decisions** | stable | a harvest re-encodes them |
| **The task** | most volatile | every run |

Dependencies point from volatile toward stable. Never the reverse.

---

## 2. Instability, redefined for a prefix

Martin's metric is `I = Ce / (Ca + Ce)` — efferent coupling over total. It does not transfer: in a
prefix there is no afferent/efferent distinction, because *everything* depends on everything before
it.

The framework already supplies the right quantity. Stability is inverse to how often the content's
governing decisions are re-made:

> **Instability = expected re-derivation rate.**

Which is measurable, in the framework's own vocabulary:

- **Ground you do not control** has a re-verification cadence (`apparatus/encode-verify.md`: verify on
  a schedule, because their truth moves on their clock). Its rate is the drift rate of the source of
  truth.
- **Encoded decisions** change only when harvested. Their rate is the harvest cadence.
- **The task** changes every run. Rate = 1.

And SDP becomes: **order the prefix by ascending re-derivation rate per token** (§3 — the per-token
normalisation is required; ascending rate alone is not optimal).

---

## 3. The optimal ordering (and a correction)

Placing content at position `k` in a prefix of length `n` means that when that content changes,
everything after it is invalidated — `n − k` tokens of prefill, re-paid. So the expected waste
contributed by a segment is:

> **waste(segment) = (re-derivation rate) × (tokens after it)**

**A first guess, and why it is wrong.** The intuitive rule — *sort by ascending re-derivation rate* —
is **not** optimal, and it fails on a case that matters. Brute-force search over orderings shows it
losing badly whenever a **volatile segment is long**: a 5000-token task placed last means every change
to the short, stable segments ahead of it invalidates all 5000 tokens behind them. Ascending-rate
gives waste 551 where the true optimum is 151.

**The correct rule** follows from an exchange argument. Compare adjacent segments A and B:

- `A then B` costs `rate_A × len_B` more than `B then A` costs `rate_B × len_A`
- so **A belongs before B iff `rate_A / len_A < rate_B / len_B`**

> ### **Order the prefix by ascending (re-derivation rate ÷ length).**

This is **Smith's rule** (weighted shortest processing time) from scheduling theory, and it is
provably optimal for this objective. Verified against brute force on four cases, including two
adversarial ones:

| Case | ascending *rate* | ascending *rate/length* |
|---|---|---|
| typical (stable content long, volatile short) | optimal ✓ | optimal ✓ |
| **stress: volatile segment is huge** | **551 (fails)** | **151 ✓** |
| random mix | 1312 (fails) | 557 ✓ |
| realistic prefix | optimal ✓ | optimal ✓ |

**Why the simple rule usually works anyway.** In a typical prefix, stable content *is* long (ground,
a large corpus of settled decisions) and volatile content *is* short (the task). Rate and rate/length
then agree, which is why ascending-rate looks right in practice and why the shipped INV-6 ordering
(ground → decisions → task) is correct. **But the rule that holds in general is Smith's**, and any
tool that automates the ordering must use it — precisely because the case where they diverge (a long
volatile segment, e.g. a big per-run document) is a case a tool will actually meet.

> **SDP is not borrowed here. For a prefix it is the optimal ordering, derived — with the correct
> instability measure being rate *per token*, and the cache making the cost of violating it a measured
> quantity rather than a design smell.**

This is the one place where Martin's principle sharpens in translation. In package design, an SDP
violation is a maintenance cost felt *eventually*. In a prefix it has an immediate, countable price:
the length of everything after the mislocated content.

---

## 4. The cache is a detector

The result that makes this worth building into a product.

An SDP violation in a prefix is **simultaneously a cache defect and a specification defect**, for one
reason:

> If stable content depends on volatile content, then something you claimed was **settled** actually
> depends on something that **is not**.

That is not a performance problem. It means **a decision was encoded whose ground still moves** —
precisely the encode/verify violation (`apparatus/encode-verify.md`: you can encode ground you
control; you must *verify* ground you do not). The cache invalidation is the **symptom**; the
mislocated decision is the **disease**.

Which gives a diagnostic the framework did not previously have:

> **A prefix segment that keeps invalidating is telling you that something in your encoded store is
> sitting on unstable ground and should not be encoded at all — it should be verified per run.**

Cache-hit-rate telemetry, read this way, is **automated detection of mislocated encoding.** You do not
need to audit the encoded store by hand; the invalidation pattern points at the entries that are
lying about their own stability.

### 4.1 The necessary caveat — the detector only fires on the prefix

Content can be volatile for entirely legitimate reasons that are *not* specification defects: a
timestamp, a session identifier, genuinely per-run task context. These invalidate nothing they
shouldn't, because they belong in the **suffix**, where volatility is the point.

> **Volatility in content that *claims to be encoded* is a defect.**
> **Volatility in content honestly labelled per-run is the suffix doing its job.**

The diagnostic therefore applies **only to the prefix**, and only to segments asserted as settled. A
volatile suffix is not a signal; a volatile *prefix* is.

---

## 5. Product consequences

Three things this licenses building, in rough order of effort:

**Order by measured rate, not by intuition.** Instrument re-derivation per segment (how often each
piece of ground or each encoded decision actually changes) and sort by **Smith's rule** — ascending
rate ÷ length (§3). This is a concrete, automatable optimisation with a provably optimal target, not a
heuristic. **Use the per-token form, not raw rate**: the two diverge exactly when a volatile segment is
long, which is a case any real tool will meet.

**Ship invalidation telemetry as a specification audit.** Report, per prefix segment: re-derivation
rate, position, and resulting wasted prefill. High-rate segments early in the prefix are ranked
defects — each one is an encoded decision whose ground is not stable enough to encode. This is §4,
operationalised.

**Enforce the boundary.** A segment asserted as encoded that exceeds a re-derivation threshold should
**fail a check**, not merely warn — the matched-pair discipline (`core/05`) applied to the prefix
itself. Encoding something unstable is exactly how demand escapes later, when the stale encoding is
consumed as ground (`apparatus/closure-principle.md`).

---

## 6. Relation to the rest of the framework

**The cacheable boundary and the store boundary are the same boundary.** `core/08` splits demand into
`I(verdict;X)` (encoded — does not vary per run) and `H(verdict|X)` (residual — varies per run). The
stable prefix *is* the encoded part; the volatile suffix *is* the residual. Prefix caching does not
merely resemble the encoded/judgment split — **it is that split, serialised in the order the cache can
exploit.**

**And cost and quality stop being a trade-off.** `core/09` shows the lever on escape is the **encode
fraction**, not context size. Encoded content is exactly the cacheable content. Therefore:

> **Maximising cache hit rate and minimising escape are the same optimisation.** Raising the encode
> fraction lowers the bill *and* lowers escape, at once, because both are governed by the same
> quantity.

This is worth stating plainly because the intuition runs the other way: people expect caching to be a
cost optimisation traded against quality. It is not. In this framework the two move together, and the
reason is that both are functions of how much of the task's demand has been pre-resolved into the
encoded store.

---

## 7. The one line

> **A prefix is a dependency chain, so Martin's Stable Dependencies Principle governs it: order by
> ascending re-derivation rate **per token** (Smith's rule), which is provably the minimum-waste
> ordering. And because the stable
> prefix is exactly the encoded store, a segment that keeps invalidating is not a cache problem — it
> is an encoded decision sitting on ground that still moves.**
