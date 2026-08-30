# GATE 2 — the collision sweep

**Status: draft-pending-ruling.** **This gate repairs nothing.** It reports two sweeps over the same
registry read, with costs, so the repairs can be ruled in batches or declined.

**Scope:** all **62** entries in `core/graph/terms.yaml` carrying canonical text (the remaining 8 are
registry-only and out of sweep 1, since nothing pins their wording), plus the downstream registry's 5.
Read at `ce2c477` (= `v5.11.0`), `e81a454`, `d0f4297`. Instrument: `sweep2.py`.

---

## Sweep 1 — canonical text that asserts without defining

**The pattern**, from `DDD-dec-29`'s warrant: `term:floor` carried the *claim about* the floor and
never a definition of it, while both sibling terms established by the same document defined. Such an
entry is useful prose but cannot serve as an embedded definition — **the reader meets a claim about a
thing before learning what the thing is.**

**All 62 read. Three buckets.**

| Bucket | Count |
|---|---|
| **Defines** — the canonical text says what the subject is | **41** |
| **Mixed** — defines, then asserts. This is `term:floor`'s *repaired* shape and is correct | **11** |
| **Asserts** — the F-1 defect, in three grades below | **10** |

**Mixed (11), for the record:** `tolerance` · `arrangement` · `act` · `poisoned-ground` · `encoded` ·
`mechanical` · `judgment` · `escape` · `acceptance-predicate` · `floor` · `accountability`.

### The ten, graded by how far the definition is from the reader

**Grade A — no definition anywhere, in the registry or in the establishing document. Worse than F-1.**

| Term | Canonical text | What is missing |
|---|---|---|
| **`term:seam`** | *"A composite carries the demand of its parts, plus the seam demand `S` created between them."* | The entry is named `seam` and defines **seam demand** in passing. **A seam is never defined.** 41 uses of the bare word in `06`, none definitional |
| **`term:composite-actor`** | *"A composite actor carries its members' demand, plus the seam demand between them."* | Near-duplicate of `term:seam`'s text. *"Composite actor"* appears twice in `06`, both the embed |
| **`term:projection`** | *"The principle has two projections. They are not two mechanisms. They are the same mechanism — the compound — run along two different axes."* | Says there are two and what they share. Never says what **a projection is** |

**Grade B — the exact F-1 shape: an ungoverned definition sits in the establishing document.**

| Term | The ungoverned definition, already in the document |
|---|---|
| **`term:training`** | `04` §3: *"Selection and training are two ways to **acquire an actor whose capability envelope covers the residual**."* |
| **`term:ensemble-actor`** | `12` §1: *"It is a **strategy for populating the judgment store when no single actor** …"* |

**Grade C — the definition is present but grammatically subordinate to the assertion.**

`term:path-degeneracy` (*"…infinitely many structurally different candidates satisfy the predicate"*,
inside a consequence clause) · `term:pinning-resolution` (an appositive under *"Actors differ in…"*) ·
`term:orchestrator` (a parenthetical: *"An actor at the seam (an orchestrator) carries judgment"*) ·
`term:p-err` (*"the error rate rises smoothly with load"*, after the derivation claim) ·
`term:redundancy` (defined only by contrast with diversity).

### Cost — and it is the finding

> **30 of the 62 entries are pinned downstream. Not one of the ten is.**

| | |
|---|---|
| pin advances (W5/W6) | **0** |
| decision nodes of the `DDD-dec-29` kind | **0** |
| embed sites | **1 each**, all upstream `core/` |
| Paper A exposure | **4** — `training`, `seam`, `composite-actor`, `ensemble-actor`: appendix regeneration and a quotation re-check, no pin |

**F-1 cost a decision node, an Appendix A regeneration and a manuscript re-quote *because
`term:floor` is pinned*.** These ten are the cheap tail of the same defect. **Grade A is three
entries, unpinned, one embed each** — the cheapest canon repair available anywhere in this programme.

**Not repaired here**, per the booking. Recommended at Gate 4 as a batch of three (Grade A) with
B and C ruled separately, because B has a definition to promote byte-for-byte and C only needs a
sentence reordered.

---

## Sweep 2 — names used in canon for a second object

**Five collisions confirmed live, one confirmed and already retired, one already governed.**
Plus the two Gate 1 added by ruling.

### C-A · `mechanical` — **CONFIRMED, live, and the registry itself carries both**

| | |
|---|---|
| **Object 1** | `term:mechanical` (**settled**, `01-the-principle.md`) — *"a criterion, applied **after the act**, by a check"*. A **store** |
| **Object 2** | `term:delivery` (**draft**, `13-delivery.md`, v5.5.0) — *"**mechanical** — the act triggers retrieval, without judgment"*. A **delivery mode** |

**Unrelated objects.** One says where a determination was resolved; the other says how governance
reached the act. *"Encoded and mechanically delivered"* reads as incoherent because the reader parses
`mechanical` as the store.

**Three aggravations the sweep found:**

1. **The registry registers the collision as an alias.** `term:delivery` carries
   `aliases: [mechanical delivery, judgment-mediated delivery, …]`. The overloaded compound is a
   *first-class registry entry*.
2. **One document does both.** `13-delivery.md`'s own contract reads
   `requires: [store, **mechanical**, judgment, escape, …]` — it declares a dependency on the store
   sense and then establishes the delivery sense in the same file.
3. **Canon already has the discipline, and it postdates the collision.** `DDD-dec-30` (v5.10.0)
   records choosing `predetermined`/`exercised`/`drawn` because they *"share no word with
   `term:store`, with the timing terms (`term:encoded`, `term:mechanical`, `term:judgment`), or with
   `term:escape` … the shared word would have read the discharge axis back into the store partition —
   the one thing this decision exists to prevent."* **`term:delivery` is the case that rule was
   written for, five versions too late.**

**Cost, both directions. Both terms are pinned, so either repair fires a pin advance and needs a
`DDD-dec-29`-class decision. The volumes are not close.**

| Repair | Occurrences | Status of the term repaired |
|---|---|---|
| rename the **delivery value** | **≈49** (34 *"mechanical delivery"*, 9 *"mechanical channel/path/edge"*, 4 *"delivered mechanically"*, 2 *"delivery is mechanical"*) | **draft**, filed v5.5.0 |
| rename the **store** | **≈340** of 389 bare `mechanical` + 159 `mechanically` | **settled**, filed at `01`, the framework's second document |

> **Recommended: repair the newer, smaller, draft-status object.** The store keeps the word.
> That is `DDD-dec-30`'s own discipline applied — the new value gives back the word the store
> vocabulary owns — and it is roughly a seventh of the work.

**Consequence for `posterior`: it is not needed.** It was a candidate to replace the **store**, which
is the expensive side. If the repair goes to the delivery side, **nothing replaces `mechanical` and
no name is minted for the store at all.** The check on it is reported below regardless, because the
prompt requires it and because it fires.

### C-B · `judgment` — **CONFIRMED, and already retired. Cost: zero.**

The brief names *"`term:judgment` versus `DDD-frame-17`'s judgment mode"*. **The mode was
`DDD-frame-15`'s, not `DDD-frame-17`'s**, and `DDD-frame-17` is the claim that *removed* it.

- `DDD-frame-15` — **`status: retired`**, `retired_from: projected`. Its four modes were *filed
  decision, judgment, arrangement default, uncontrolled draw*.
- `DDD-frame-17` — the three values are **`predetermined` · `exercised` · `drawn`**. None is
  `judgment`.
- **Canon records the collision in its own words.** `DDD-dec-30`: *"`DDD-frame-15`'s judgment mode
  and `term:judgment` were therefore two distinct objects sharing one word inside canon, **not a
  reader's confusion**."* And `13-delivery.md` §4: *"The retired mode list borrowed *filed decision*
  and *judgment* from the store vocabulary while partitioning a different object — and
  `term:judgment` carries an accountability clause…"*

**So the collision was real, was recorded at Phase 1a as open, and was closed at v5.10.0 by the node
it was recorded against.** The residue is ~7 historical mentions in the retired claim,
`DDD-frame-17`'s *"what was wrong"*, `DDD-dec-30` and `13-delivery.md` §4. **All are correct as
history and must not be migrated.** The item to carry is that the brief inherited it as open.

### C-C · `projection` — **NEW, live, and it sits inside `term:verdict`**

| | |
|---|---|
| **Object 1** | `term:projection` (settled, `08`) — one of the two axes the compound runs along: the funnel and maturation |
| **Object 2** | the **projection layer / the engineering projection** — a repository and an audience denomination |

Object 2 in canon: `core/README.md` *"Its software **projection** lives in a separate repository"* ·
`core/10-cost.md` ×2 *"files with the **projection** layer"* · `core/13-delivery.md` *"files with the
**projection** that carries diachronic claims"* · `core/00-primitives.md` *"the **engineering
projection** — the same principle, denominated in the vocabulary of a domain"* · and —

> **inside `term:verdict`'s settled canonical text**: *"(In the engineering **projection** this same
> quantity is denominated in the vocabulary of the domain and called **specification demand**.)"*

**The collision sits on the one term that already carries an audience denomination**, which is item 3
of the queued downstream demand. See §4.

**Cost:** `term:projection` is **not pinned**; one embed site (`08`). Object 2's occurrences are prose
across `core/README`, `00`, `10`, `13` and both repositories' structural vocabulary.

### C-D · `verdict` — **NEW, live, and it is between three settled registry entries**

| | |
|---|---|
| **Object 1** | `term:verdict` — *"that induced assignment — the correct output over **each point of the input space**"*. A **function**. `D = H(verdict)` is its entropy |
| **Object 2** | `term:act-individuation` — *"one act = **one verdict** of the acceptance predicate at the declared boundary; batch boundaries are verdict boundaries"*. A **value at one act** |
| | `term:outcome` — *"The **verdict** is the same determinate as assessed by a declared predicate, produced only where governance has declared one"*. Also the per-act value |

**A function and a value of that function are not the same object**, and `H(verdict)` is only
well-formed on the first reading while *"one act, one verdict"* is only well-formed on the second.
All three terms are settled and all three are established by `09-the-measure.md`.

**Canon half-knows.** `09`'s contract already disambiguates —
`establishes: [**verdict|verdict function**, …]` — and `term:verdict` carries
`aliases: [verdict function]`. **The `term:` field itself is the bare word**, and §7a is titled
*"Outcome and verdict: the determinate's two registers"* while naming the two registers of
*determinate*, not of *verdict*.

**Cost:** `term:verdict`, `term:outcome` and `term:act-individuation` are **all unpinned**. The
cheapest available repair is to promote the existing alias — make `verdict function` the term and
`verdict` the alias — which touches the registry and `09`'s prose and fires no pin.

### C-E · `maturation` — **already governed. Reported as the pricing precedent.**

Upstream `term:maturation` (*the compound over repetition*, `08`) and downstream `term:maturation`
(*the return channel from the mechanical store to the encoded store*, `14-maturation.md`) are two
objects under **one id**, declared by `shadows_upstream: DDD-dec-21` and reported by the validator as
*"1 shadowed id"*.

`DDD-dec-21`'s framing is the model for the four above: **"deliberate in destination, escaped in
mechanism, known and temporary"** — the escape being that *"no ruling governed id reuse across the two
registries; the validator's default resolved it silently, by having no opinion, which is a governing
decision determined by nobody."* Resolution bound to the deferred 06/08 carve.

**`mechanical`, `projection` and `verdict` are the same escape inside one registry**, where no
validator reports them at all.

### C-F · `floor` in `product-cli` — **CONFIRMED, live, cross-repo**

`tolerance_floor` — a decision set's minimum tier, `§4.2.1`, *"an override is valid only above the
floor"* — against the **Polanyi floor** (`§3.5`), which is `term:floor`. **168 files touch
`tolerance_floor`**, and both senses appear in the same documents. A serialised field name, so W4's
class.

### C-G · `ground` — the two Gate 1 added by ruling, both in `product-cli`

- **the RDF/logic `ground term`** — 11 occurrences, `product-core/tests/graph_capability_tests.rs`;
  a term containing no variables or blank nodes.
- **`ground` as a CSS surface colour** — 6 occurrences; *"the two surface **grounds** the page and
  its cards sit on"*.

Both are local to one repository, neither touches canon, and neither is migrated. **They belong on the
drafting-warning instrument's exception list**, which already needs a third exception for ordinary
English and now needs five.

### Checked and clear

`store` · `closure` (aliases `closes/closed/closing` already registered) · `capacity` · `selection` ·
`training` · `demand` · `outcome` · `escape` · `encoded` · `act` · `decision` · `actor` ·
`arrangement` · `tolerance` · `assurance` · `compound` · `funnel` · `attribution` · `capability` ·
`overflow` · `conservation` · `exhaustiveness` · `diversity` · `redundancy` · `liability` ·
`accountability` · `answerability` and the remaining registry names: **one object each in canon.**

**One near-miss, reported as drafting and not as collision:** `floor` is used twice in
`core/00-primitives.md` in ordinary English — *"you never reach a **floor** of pure action"*, *"the
collapse removes the act as a **floor**"*. Same class as the `ground` ordinary-English cluster;
a matter for the drafting-warning instrument's exceptions, not for a rename.

---

## The required registry check on `posterior` — **it fires**

**Reported whether or not it fires, per the standing note. It fires.**

**Name check: clear.** No term or alias in either registry is called `posterior`. Prose occurrences
across all three repositories: **3, and all three are this session's own committed prompt and
inputs.** Zero pre-existing.

**Content check: fires.** The objection is the one that killed `basis` — *"the framework is already
carrying an information-theoretic register"* — and it is **stronger here, because the framework does
not merely carry the register, it uses the pair's other half.**

`prior` is live in the **Bayesian** sense, in four places, one of them ratified canon:

| Where | |
|---|---|
| `core/claims/DDD-measure-05.yaml` | **ratified canon** — *"200 samples from the **prior** and channel the asset stipulates"* |
| `meta/holding-note-addendum-determinables.md` (upstream) | *"encoding-proxy as **prior**, act stream as **update**, calibration ledger as **estimator**"* |
| `meta/holding-note-ground-axes-rev18.md` (downstream, ×2) | *"**The encoding-proxy is a prior; the act stream is the update.**"* |
| `ledger-cli` fixture | *"parks demand on a **prior** while reading as allocated"* |

**And the collision would land next door to its own pair.** `term:calibration-ledger` is
*"a claimant's record across claims whose predicates later closed: a matured-verdict certificate"* —
the **estimator** in that very prior→update→estimator pipeline, and an object about verdicts arriving
after the act. A *"posterior store"* beside a calibration ledger whose machinery is explicitly
prior-and-update would read as the updated belief, which is not what the mechanical store is.

> **Third naming attempt, third registry check.** `fixed` died against `term:encoded`; `resolved`
> died against `term:determination`; **`posterior` dies against the live Bayesian register, one
> instance of which is in ratified canon.**

**And it is moot under the recommendation.** If C-A is repaired on the delivery side, the store keeps
`mechanical` and no candidate is needed. `posterior` is reported as checked and declined, not as
rejected in favour of something else.

**If Emil rules the store side anyway**, the candidates that pass both checks are `ex-post` (0
occurrences anywhere) and `act-supplied` (0). **`automatic` is clear on the registry but fires on
Emil's own stated criterion** — it carries the automation implication `posterior` was liked for
avoiding. **`standing` fires**: 626 occurrences, and *"standing supply"* is live framework vocabulary
that `13-delivery.md` explicitly sets delivery beside.

## The delivery value's replacement, if C-A is repaired as recommended

**Checked before proposing.** `act-triggered` — **registry check clear**, and **already canon's own
gloss of the value**: `DDD-cost-09` reads *"at act-sites where the check is **act-triggered**
(`term:delivery`, mechanical)"*, and `term:delivery`'s own text is *"the act triggers retrieval,
without judgment"*. 18 occurrences across upstream and downstream, all in this sense.

**This is reuse, not minting.** It pairs cleanly with the existing `judgment-mediated`, and the pair
`act-triggered` / `judgment-mediated` names the mechanism on both sides by what triggers it.

Also checked and clear on the registry, reported for completeness: `retrieved` (26, but the word is
load-bearing in `product-cli`'s ledger), `unprompted` (2), `pulled` (17, 15 of them `product-cli`
code), `ambient` (18, 13 of them `product-cli`).

---

## Two questions this gate raises, for ruling at whichever gate Emil prefers

**Q-1 — the erratum has no pointer from the artefact it corrects.**
`meta/ground-audit-2026-08-24-erratum.md` is filed. Adding a line to the audit pointing at it would
edit a merged artefact, which the GATE 1 ruling forbids. Leaving it means a reader of the audit meets
the fifteen-term count with nothing to warn them. **That is a delivery failure of exactly
`term:undelivered`'s shape — filed, adequate, and never reaching the act.** Options: leave as filed;
add a one-line pointer and treat a pointer as not-a-history-edit; or list errata in
`meta/README.md`. **Not decided here.**

**Q-2 — a `denominations:` field would repair C-C more cheaply than a rename.**
C-C exists because `term:verdict`'s canonical text carries an audience denomination *inline*, and the
word it uses for that is `projection`. If denominations moved to a registry field —
`denominations: [{audience: engineering, name: specification demand}]` — the parenthetical leaves
canonical text, `projection` stops doing denomination duty inside a settled entry, and the practice
canon already has in one place becomes a rule. **The queued primer is the first projection that needs
it at scale, and C-C is the first place it would pay for itself.** Costed at Gate 4 if Emil wants it.

---

## What this gate asks

1. **Sweep 1's ten**, with the finding that **none is pinned** — batch, split, or decline.
2. **C-A `mechanical`**, confirmed live, with the recommendation to **repair the delivery side**
   (~49 occurrences, draft) rather than the store (~340, settled).
3. **C-B `judgment`**, confirmed and **already retired** — the brief named the wrong node; cost zero.
4. **C-C `projection`** and **C-D `verdict`**, both new, both live, **both unpinned**.
5. **`posterior`: checked, fires, declined** — and moot under the C-A recommendation.
6. **Q-1** and **Q-2**, at Emil's convenience.

**Nothing repaired. Nothing merged.**
