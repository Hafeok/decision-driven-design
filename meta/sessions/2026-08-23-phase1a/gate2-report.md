# GATE 2 — R-1 and R-2, drafted together

**Status: draft-pending-ruling.** Every body committed upstream carries a `[PROPOSED]` banner.
Nothing is ratified. Nothing is merged. The banners are struck at the ruling, per `DDD-dec-29`.

Upstream commit `c73c463` on `claude/phase-1a-claim-repairs-i6ilkv`.

---

## 0. The two review inputs arrived, and are filed

Both landed after GATE 1 and are committed to this directory with their identity, per the
`holding-note-ground-axes-rev18` precedent in `DDD-dec-20`'s notes:

| File | Lines | sha256 |
|---|---|---|
| `paper-a-objective-review.md` | 349 | `1d291a5fcc605ae6ade4c82922802b1be2d132d33b470110946d95b272205707` |
| `paper-a-review-triage.md` | 179 | `e9650358e5f6120905d4d7cfc4f4769c407d6f10d4804be9fe09bada8e3f741a` |

**The GATE 1 drafts were re-read against them.** The arrival failure recorded at the bootstrap
stands as recorded — it happened — and its consequence is now discharged rather than carried.
Four deltas came out of that re-read and are reported at §4. **None of them changes a ruling
already made**; two of them change what was drafted.

---

## 1. What was committed upstream

| File | Change | Shape |
|---|---|---|
| `core/claims/DDD-frame-17.yaml` | **New.** The discharge partition successor | `supersedes: DDD-frame-15` |
| `core/claims/DDD-frame-15.yaml` | **Retired.** Statement rewritten to a retirement record; ratified statement preserved verbatim in `notes`; Wave 3 derivation retained beneath | Supersession |
| `core/claims/DDD-frame-16.yaml` | **Notes only.** Derivation step 3's mode count, and the deferred abstention tension | Amendment |
| `core/claims/DDD-frame-02.yaml` | **Statement amended**, residual-discretion clause only; prior statement verbatim in `notes` | Amendment, per this node's own Wave 3 precedent |
| `core/graph/terms.yaml` | `term:residual-discretion` canonical text corrected | Text correction to a `draft` term |
| `core/14-indexed-determination.md` | §2 embed re-projected; the held-at-fixed-ground exposition and the convergence with `DDD-frame-17` | Exposition |
| `core/13-delivery.md` | §4 rewritten to the three values; §5 and the header reference re-pointed | Exposition |
| `core/decisions/DDD-dec-30.yaml` | **New.** The GATE 2 ruling record | `[PROPOSED]` |

**Validators green, baseline exactly restored:** `validate-core-order.py` exit 0, 15 documents,
70 terms, 0 errors, **66 warnings — 59 W1, 7 W2, zero W4**, identical to arrival.
`validate-claims.py` 61 claims valid, 9 decisions valid, 5 release descriptors valid.

One new W1 was introduced and removed rather than tolerated: `core/13` §4 cited
`term:commitment-level`, which `core/14` establishes — a genuine forward edge, an escaped seam by
this repository's own rule. The composition is now stated in `core/14` §2, where the term is
established, and `core/13` points forward to `14` without naming the term. **The warning count is
back to 66, not 67.**

---

## 2. R-1 — the recast as drafted

### 2.1 `DDD-frame-17`'s statement

> At every completed act in a task's scope, each outcome-relevant alternative is discharged in
> exactly one of three ways: **fixed** — the arrangement's standing configuration together with
> the ground at the act determines the resolution; **resolved** — it does not, and something
> within the arrangement's control determines it at the act; or **drawn** — it does not, and what
> determines it lies outside the arrangement's control. Demand is never unmet, only ungoverned.

Three things about that sentence are deliberate.

**Exhaustiveness is provable, not enumerated.** Given the configuration and the ground, the
resolution is determined or it is not — exhaustive and exclusive by construction. If it is not,
what determines it is inside the arrangement's control or outside — exhaustive and exclusive by
the meaning of control. Two dichotomies, three values, no remainder. `DDD-frame-15`'s
exhaustiveness was an enumeration over four loci that were not disjoint. **This moves the claim's
content out of the enumeration, where it was false, and into the answerability of the fixing test,
where the falsifier now sits.**

**The unit is the outcome-relevant alternative.** `DDD-frame-15`'s `test:` field already quantified
that way; its `statement:` quantified over acts. Those were different claims. A timeout carries a
*when-to-stop* alternative and a *what-to-return* alternative, and they discharge differently.

**The compact form survives verbatim**, and so does the seam guard — carried into `region:` word
for word, because it was correctly ratified and is orthogonal to the overlaps that killed the mode
list.

### 2.2 Governance status as Axis 0, which is the ruling's payoff

`region:` now states it as an exclusion:

> Governance status is not an axis of this claim. Whether a resolution is declared, governed,
> filed, or escaped is `term:store`'s question and is answered there. This claim's three values
> turn on determination and control alone, never on declaredness.

That is the consequence you named at the ruling, filed as the claim's own text rather than as
commentary on it.

### 2.3 The six cases, re-run against the drafted axis

Every case classifies exactly once. Two of them split into more than one alternative, which is the
unit repair doing its work rather than a failure to classify.

| Case | Alternative | Value | `term:commitment-level` |
|---|---|---|---|
| Trained inference, greedy decode | what to output | **fixed** | policy committed, outcome open |
| Trained inference, sampled decode | what to output | **resolved**, or **drawn** if the sampling source is uncontrolled | policy |
| Lookup table | which output for this key | **fixed** | outcome |
| Declared default | which value when the trigger fires | **fixed** | outcome, conditional on the trigger |
| Randomised search with checking | which candidate is drawn | **resolved** if the generator is arrangement-controlled, **drawn** if not | none reaches this alternative |
| Randomised search with checking | which candidates are admissible | **fixed** | outcome, as a constraint set |
| Abstention, expressed, rule-governed | whether to resolve | **fixed** | policy |
| Abstention, expressed, actor-declined | whether to resolve | **resolved** | principal, or none |
| Abstention, unexpressed | — | **out of region**; deferred | — |
| Timeout | when to stop | **fixed** | outcome |
| Timeout | what to return at the cut | **drawn**, or **resolved** where the arrangement fixes the partial-state policy | none reaches this alternative |

---

## 3. R-2 — the separation, and the convergence

### 3.1 The four phenomena, separated before any text moved

| Phenomenon | Discretion? | Why |
|---|---|---|
| outcome variation across ground | **no** | the commitments fix the output at each ground point; the variation is the ground's. **The hash.** |
| epistemic uncertainty about a fixed policy | **no** | a fact about an observer, not about the arrangement. An unread lookup table exercises none |
| stochasticity | **no** | already excluded by the clause's surviving sentence — the one thing Wave 3's text got right |
| genuine unresolved or delegated selection | **yes** | this alone |

### 3.2 The corrected canonical text

> **Residual discretion** is the outcome-relevant variation the arrangement's commitments leave
> open at the act, **held at fixed ground**: the alternatives still admissible once the standing
> configuration and the ground at the act are both given. It is not variation across ground — a
> cryptographic hash varies enormously with its input and exercises no discretion, because at each
> input the commitments fix the output exactly. It is not an observer's inability to predict a
> fixed policy, which is a fact about the observer and not about the arrangement. And it is not
> randomness: a deterministic arrangement can carry substantial discretion across unfamiliar
> cases, a randomised one can be tightly committed, and a zero-variance arrangement can be
> consistently wrong.

**The ratified last sentence is verbatim.** What is added excludes two phenomena it did not
exclude; nothing it said is withdrawn.

`DDD-frame-02`'s clause changes correspondingly — *"the outcome-relevant variation those
commitments leave open at the act, held at fixed ground"* — and the first clause, the three levels,
is untouched.

**Why "declared" is struck.** Declaredness is governance status. Making discretion depend on it
would import into `DDD-frame-02` the exact seam that `DDD-frame-17` spends its budget excluding.
Undeclared commitments constrain an act precisely as declared ones do; that is what makes an
incidental default a default.

### 3.3 The convergence — why the charter was right to put both in one gate

**Residual discretion is exactly `DDD-frame-17`'s `resolved` value.** The commitments leave the
alternative open, and something within the arrangement's control settles it at the act. Where it is
settled outside that control it is `drawn`, which is stochasticity, which the clause already said
is not discretion. The four-way separation and the discharge partition are one distinction seen
from two sides.

---

## 4. Four deltas from re-reading the drafts against the arrived inputs

### 4.1 `term:actor` says "a thermostat qualifies" — GATE 1's axis was wrong, and the repair is better

Review §4.2 does not merely say a thermostat reads ground; it says *"A thermostat, lookup table, or
deterministic controller **can be a framework actor***." Canon agrees in terms:

> An **actor** is a system that resolves decisions by reading ground… **A thermostat qualifies**; a
> falling rock does not.

**GATE 1's proposed Axis 1 was `artefact · actor · uncontrolled`. That split is not available** —
the very case the review raises is a canonical actor, so a lookup table is an actor too, and the
axis would have classified cases 1 and 2 by fiat. **That is an error in my GATE 1 draft, caught by
drafting against canon.**

The axis was rebuilt on the fixing test — *does the standing configuration together with the ground
determine the resolution?* — and the rebuild is strictly better in two ways. It resolves the
thermostat by asking the question that actually discriminates, rather than adjudicating actorhood.
And it means **no value on this axis turns on actorhood at all**, so `DDD-frame-17` does not
inherit the actor admission test's open circularity — which review §6 reports and the triage rules
*"flag as open rather than patch"*. **`DDD-frame-15`'s judgment mode did inherit it.** That is an
unlooked-for payoff of the ruling.

### 4.2 The triage's two "cheap fixes" for R-1 — one is unavailable, one is what (b) delivers

Triage §1 F-C offers them, and both deserve an answer:

- *"the mode means **undeclared** default; the definition says so."* **Not available.** That is
  precisely the seam-guard crossing GATE 1 identified: it separates the two modes by declaredness,
  which the region field assigns to the store partition. Recorded because the triage proposed it as
  cheap, and it is not cheap — it is the expensive one.
- *"judgment requires that the standing rule **not** fix the output given the ground — genuine
  underdetermination at the act."* **Correct, and it is exactly the fixing test.** Disposition (b)
  delivers it structurally, as the axis's first dichotomy, rather than as a definitional patch to
  one mode of four. The triage found the right discriminator and attached it to the wrong shape.

### 4.3 Review §5 names six phenomena in prose and four in its recommendation

The prose list is: variation across inputs · designer ignorance about consequences · inability to
predict a fixed policy · unspecified acceptance criteria · delegated choice · stochastic variation.
The recommendation asks for four terms. The two extras are reported rather than dropped:

- **designer ignorance about consequences** — a variant of epistemic uncertainty aimed at
  downstream effects rather than at outputs. Likewise not discretion.
- **unspecified acceptance criteria** — **not a species of discretion at all.** It is an open
  acceptance predicate, and it is the *existence* condition R-3's `DDD-measure-16` carries. **The
  review reached the same boundary from two sections and did not notice.** Recorded in
  `DDD-frame-02`'s notes.

### 4.4 The reviewer proposes re-wording `term:escape`, which is settled

Review §4's closing paragraph: *"'Ungoverned resolution' would be clearer than 'determined
never.'"* That touches a `settled` term, is outside this session's booked scope, and is **booked as
a successor item, not acted on** — carried with the manifest finding that an external reader met
the seam guard and still reported the phrasing as conflicting, which is a finding about the guard's
**audience**, not its content.

---

## 5. One consequence that changes GATE 4's shape, and needs your ruling now

**Retiring `DDD-frame-15` rewrites its statement.** Canon's retirement convention makes a retired
statement into a retirement record — `DDD-frame-09` and `DDD-measure-08` are the exemplars, and
`DDD-frame-09`'s live text is *"RETIRED — 'closed predicates make intelligence unnecessary.'…"*.

I ran `check-quotations.py` rather than reasoning about it. **Paper A block-quotes three of the
nodes this gate changes:**

| Paper A line | Node | Quotation of |
|---|---|---|
| 365 | `DDD-frame-15` | the statement that is being retired |
| 274 | `DDD-frame-02` | the statement whose clause is corrected |
| 310 | `term:residual-discretion` | the canonical text being corrected |

`DDD-measure-06` is cited in **prose only** (lines 532, 605, 756, 911) — the checker reads `> `
block runs, so **R-3 carries no quotation exposure at all.** Only R-1 and R-2 do.

**These fail only when the pin advances**, because both checkers resolve against the pinned ref,
which is `v5.9.0`. Nothing is failing today; the baseline is 29 verbatim / 0 failing.

**Proposal: do not advance the pin this session.** Land the canon repairs upstream, leave
`graph/upstream.yaml` at `v5.9.0`, and book the pin advance with Paper A's revision — which is out
of scope here, is already scheduled, and is the session that must rewrite those three quotations
anyway. The precedent is `DDD-dec-27`'s: nodes deliberately not pinned when pinning would assert
something not yet true.

The alternative — advancing the pin and disclosing three failing quotations — buys nothing this
session needs and leaves the downstream repository red.

**Canon is not shaped around a projection's convenience.** The retirement stands as drafted; it is
the *pin* that waits.

---

## 6. The freight finding you asked for at GATE 1

Filed at `meta/successor-items-phase1a.md` (drafted, committed with this report): **`validate-claims.py`
enforces neither falsifier presence nor `spec/claim-format.md` §2 rule 1.** Both of
`DDD-measure-06`'s defects were visible from the schema alone, without a reviewer, and the
validator saw neither. Two instances carried as evidence: the missing `falsifier` field, and the
semicolon-joined compound statement whose two limbs carry different warrants under one status.

---

## 7. What is asked at this gate

1. **Ratify or amend `DDD-frame-17`** as drafted — statement, the three value names, region
   including the Axis 0 exclusion, and the falsifier.
2. **Ratify the asymmetry**: `DDD-frame-15` retired and superseded, `DDD-frame-02` amended in place
   per its own Wave 3 precedent. Flagged rather than assumed, because the two repairs take
   different shapes and that should be deliberate.
3. **Ratify `term:residual-discretion`'s corrected canonical text**, and `DDD-frame-02`'s
   corresponding clause.
4. **Rule the pin**: hold at `v5.9.0` this session (proposed), or advance and disclose.
5. **Note §4.1** — GATE 1's axis was wrong on canon's own terms, and the corrected axis is better
   for a reason the ruling did not anticipate.
