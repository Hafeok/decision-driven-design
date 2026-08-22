# GATE 1 — survey, dependents, and the proposed dispositions

**Status: draft-pending-ruling.** Nothing in canon is touched. This document reports what is in
the repositories, verbatim, and proposes two dispositions for Emil to rule.

Canon read at **`v5.9.0`** = `bce18fe80bf96a0f3106029a655f8749b34487d0`, which is also
`actor-indexed-determination`'s head. Downstream read at `8a4c8f5`.

---

## 0. Four findings that arrived before the survey did

These change what the session is asked to do, so they are reported ahead of the verbatim survey
rather than buried in it.

### 0.1 Neither review input arrived

The prompt names `paper-a-objective-review.md` and `paper-a-review-triage.md` as uploads. The
session's upload directory holds the prompt alone; neither file exists in either repository. This is
`DDD-dec-17`'s arrival-failure class recurring — the sixth instance, the first since `DDD-dec-20`
filed the convention — and it is recorded in `bootstrap.md` with its consequence: the prompt's own
rendering of the review is sufficient to do the commissioned work, so **no repair is blocked**, but
nothing in this session quotes the reviewer, and no drafted node cites the review as a locatable
artefact.

### 0.2 `term:residual-discretion` is already minted

The prompt says residual discretion "entered `DDD-frame-02` at Wave 3 and was deliberately not
minted as a term", and instructs "mint after the separation, never before". **That is true of
`v5.7.0` and false of canon at `v5.9.0`.** The Track 1 session minted it at **`v5.8.0`**:

```
id: term:residual-discretion
term: residual-discretion
aliases: ['residual discretion']
established_by: 14-indexed-determination.md
status: draft
```

It is ruled by `DDD-dec-26`, released in `releases/v5.8.0.yaml`, embedded in `core/14` §2, **pinned
downstream** by `DDD-dec-28` at `sha256:77284b14…` with `status_at_pin: draft`, and projected in
both Paper A (line 314, and Appendix A line 1404) and the determination track (rung 6).

**R-2's question therefore changes shape.** It is no longer *does this mint?* — it is *does the
minted term's canonical text survive the four-way separation?* The session's answer is at §4: it
does not, and the correction is a canonical-text repair to a `draft` term with a downstream pin,
not a mint. **No new mint is proposed.** Emil should know the question moved before ruling on it.

### 0.3 The measure note's "revised §7" is **§8** in the note as merged

The prompt, the review, and `papers/measure-note/response-to-review.md` all call the boundary
section **§7**, with subsections §7.1 and §7.2. In the note **as merged** it is **§8, "Where the
measure stops"**, with **§8.1** and **§8.2**. The discharge session inserted §6 ("Discharge over
many acts") and everything below it moved down one; `measure-paper-context.md` §5 confirms the
merged numbering ("The boundary — the paper's best feature, §8"), and §3 confirms that the *present*
§7 is a different section entirely ("What the computations establish, and what they do not").

The prompt's instruction is followed against the **section, not the number**. §8 is quoted in full
at §5.2 below. No renumbering is proposed here; the stale numbers live in a response document and a
context file, which is a bookkeeping item for the manifest, not a canon repair.

### 0.4 `DDD-measure-06` has no falsifier, and is a compound statement

The prompt asks for the falsifier verbatim. **There is no `falsifier:` field.** The file carries
`test:` only. That is legal — `spec/claim-format.md` §2 rule 2 requires a falsifier for *projected*,
not for *established* — but it matters to R-3, because a status proposal that moves the node to
`projected` must supply one.

Separately: the statement joins two assertions with a semicolon. Rule 1 is *"One proposition per
claim. Compound statements split. The unit of status change must be the unit of statement."* The
near-definitional half and the substantive half currently share one status field, which is the
mechanism by which this node resisted repair for as long as it did. This is reported as a
**schema-grade defect independent of the review**, and it shapes the R-3 proposal at §5.

---

## 1. `DDD-frame-15` — verbatim

```yaml
format: 1
id: DDD-frame-15
kind: conceptual
statement: |
  At every completed act in a task's scope, the act's determination demand is discharged — by a filed decision, an actor's judgment, an arrangement default, or an uncontrolled draw; escape is a supply mode of discharge, not an absence of supply — demand is never unmet, only ungoverned.
status: projected
region: |
  Completed acts within a task's declared scope. The seam this claim must not cross, stated as
  region: the four modes partition discharge — the physical production of a determinate at the
  act — not governance-supply. In the store partition (term:store) escape remains nothing and
  there is no fifth source, because the question there is what governance supplied; here the
  same act's demand is met by an uncontrolled draw, because the question is what the world
  produced, and the world never produces nothing. The two partitions answer different questions
  about the same act, and neither reduces to or replaces the other.
evidence:
  - kind: derivation
    ref: core/13-delivery.md §4
    note: derivation check run at Wave 3 GATE 2; premises by ID and steps in notes
falsifier: |
  An act exhibiting a fifth supply mode unclassifiable as the four; or an act completing with an outcome-relevant alternative resolved by nothing at all.
test: |
  Coding reliability over recorded acts: independent coders assigning every completed act's outcome-relevant alternatives to the four modes without remainder, and without collapsing the discharge coding into the store coding.
owner: none
changed: v5.7 (2026-08-18, Wave 3 session)
```

The `notes:` field is long; the load-bearing paragraph for this session is **derivation step 4**,
quoted whole because the whole disposition turns on it:

> 4. Exhaustiveness by cases on where the resolving variation lives: authored in advance and
>    delivered (a filed decision); produced at the act by an actor reading ground (judgment);
>    carried by the arrangement's standing configuration without a fresh resolution (a
>    default); or in nothing the arrangement controls (the draw, non-empty by steps 2-3). A
>    fifth mode would need a completed act whose alternative resolves in none of these loci —
>    the falsifier's first limb. **Note the modes classify the producer of the resolution, not
>    its governance status: a default may be declared and governed or incidental and not; the
>    governance question is the store partition's, per the region.**

(Emphasis added. The rest of `notes:` — the Wave 3 provenance, the luck ruling as a restated step,
the foundation §4.1 divergence, the compact-form booking — is unchanged by anything proposed here
and is not reproduced.)

## 2. `DDD-frame-02` — verbatim

```yaml
format: 1
id: DDD-frame-02
kind: conceptual
statement: |
  Behavioural commitments attach at three levels — outcome, policy, principal — which compose and are not actor species; residual discretion is the outcome-relevant variation that remains after the arrangement's declared commitments are applied.
status: projected
region: engineered arrangements
test: >-
  boundary-case coverage; an arrangement whose commitments resist the three-level coding, or
  whose remaining outcome-relevant variation resists description as residual discretion
owner: none
changed: v5.7 (2026-08-18, Wave 3 session — residual-discretion clause added, exposition home gained, flag cleared)
```

No `falsifier`, no `evidence`, no `breaks`. `kind: conceptual`, so `test:` is the appropriate field
per the schema. The `notes:` carry the Wave 3 amendment record, the prior v4.4 statement, and the
`[PROPOSED]` Track 1 mint record — **including the duplicated word "One / One consequence" already
booked by the Paper A session as a freight item**, still present at `v5.9.0`.

## 3. `DDD-cost-20` — verbatim

```yaml
format: 1
id: DDD-cost-20
kind: conceptual
statement: |
  Encoding around a carrier and encoding within it differ in locus: around-encoding — context, retrieval, scaffolds — is standing supply outside the carrier, delivered through the channel at each act; within-encoding — training — converts judgment allocation to encoded allocation inside the carrier. Training buys allocation, not capacity: it does not enlarge the judgment store.
status: projected
region: |
  Per-act, synchronic: the locus distinction and what training buys are properties of the carrier at the act. The crossover between the two paths quantifies over act volume and files with the projection.
evidence: []
falsifier: |
  A training intervention demonstrated to enlarge a carrier's capacity — hold or resolve — rather than reallocate supply between its stores, at fixed architecture; or around-encoding shown to alter the carrier's internal allocation without the channel.
breaks: |
  The rent-and-encode versus own-and-train fork loses its locus premise; 10 §8's precision points revert to vendor framing.
owner: none
changed: v5.3 (2026-08-10, Wave 2 curation session)
```

**Why the review reaches this node.** It is the third limb of the trained-inference overlap: training
"converts judgment allocation to encoded allocation **inside the carrier**". So canon already holds
that a trained carrier's supply is *encoded*, and `term:encoded` times encoding **before the act**.
That is what makes trained inference read as standing supply at the same time as it reads as
judgment.

## 4. `term:store` and the timing terms — verbatim

All five are `status: settled`, established by `core/01-the-principle.md`.

**`term:store`**

> **{rule, check, actor, nothing}.** There is no fifth source.

**`term:encoded`** — the *before* term

> **Encoded** — a constraint, fixed *before* the act, by a rule. It amortises: cheap to
> state, **expensive to find**.

**`term:mechanical`** — the *after* term

> **Mechanical** — a criterion, applied *after* the act, by a check. It pays the
> **executability tax** and is cheap to trust.

**`term:judgment`** — the *during* term

> **Judgment** — determined *during* the act, by an actor reading ground, **with an
> accountable party named**. It does not amortise; it walks out the door.
>
> **A judgment allocation naming no accountable party is not an allocation. It is Escaped
> with an executor attached.**

**`term:escape`**

> **Escaped** — determined *never*, by nobody: decided-by-nobody as a first-class category.
> Latent defect exposure. **The only forbidden state.**

Two further terms the dispositions rest on:

**`term:commitment-level`** (draft, `core/14` §2)

> A **commitment level** is a level at which an arrangement fixes behaviour in advance:
> **outcome-level** — permitted resolutions fixed directly; **policy-level** — the
> generating procedure fixed; **principal-level** — a determiner selected by qualification
> and case-level resolution delegated. The three compose, and they are levels of
> commitment, not species of actor: the question is never which of three kinds an actor
> is, but at which levels the arrangement has committed.

**`term:residual-discretion`** (draft, `core/14` §2) — the R-2 target

> **Residual discretion** is the outcome-relevant variation remaining at the act after the
> arrangement's declared commitments are applied. It is not randomness: a deterministic
> arrangement can carry substantial discretion across unfamiliar cases, a randomised one
> can be tightly committed, and a zero-variance arrangement can be consistently wrong.

## 5. `DDD-measure-06`, and the measure note's boundary section

### 5.1 `DDD-measure-06` — verbatim, in full

```yaml
format: 1
id: DDD-measure-06
kind: formal
statement: |
  The measure exists iff the acceptance predicate operationally closes; H(V) is undefined exactly where the framework's floor result locates non-zero floor.
status: established
region: everywhere — this claim is about the boundary itself
evidence:
- kind: derivation
  ref: core/09-the-measure.md
  note: >-
    near-definitional on the measure side; the force of the claim is the coincidence with
    core/03's independently derived floor. Claim the boundary as principled, not as convergent
    evidence.
test: >-
  a task with an open predicate for which a defensible verdict function exists anyway
owner: paper-1
changed: v4.5
```

That is the entire file. **Fields absent: `falsifier`, `breaks`, `credits`, `supersedes`, `notes`.**

Read against the schema, three things are true of it before any reviewer is consulted:

1. **The statement is compound** (rule 1). Limb (a) — *the measure exists iff the predicate
   operationally closes* — is what the evidence note itself calls "near-definitional on the measure
   side". Limb (b) — *`H(V)` is undefined exactly where the floor result locates non-zero floor* — is
   the coincidence with `core/03`, derived on independent grounds. One status governs both.
2. **The evidence note contains its own warning and canon did not act on it**: *"Claim the boundary
   as principled, not as convergent evidence."* The node then carries `established` on a statement
   whose second limb is exactly the convergence.
3. **`region: everywhere`** is written, so it is claimed (rule 5). Nothing scopes this node to an
   arrangement, which is precisely what the note's revision went on to do.

### 5.2 The measure note's boundary section, **as merged**, verbatim

`papers/measure-note/measure-note.md` lines 708–802. Quoted in full because the proposal is that
canon adopt it.

> ## 8. Where the measure stops
>
> The boundary is a scope condition, and it is best stated as one.
>
> > **The construction applies where the task supplies an operationally usable verdict function and a
> > ground distribution that can be estimated.**
>
> Three requirements sit inside that sentence, and they fail in different ways. Collapsing them is the
> error the section is written to avoid.
>
> **Existence.** `H(V)` requires a verdict function. Where the acceptance predicate assigns no correct
> output to a point of the input space, there is no ground truth to have entropy about, `H(V)` is
> undefined, and there is nothing to measure.
>
> **Availability.** A verdict function can exist without being usable. A predicate that assigns a definite
> verdict to every input, but whose acceptance procedure cannot be executed over available ground within
> declared resource, latency, and confidence bounds, does not close [term:closure] — and `H(V)` then
> exists mathematically while being unavailable in practice. These are two failures, not one. The second
> says nothing about existence. Formal decidability is the wrong criterion for either: any bounded finite
> domain is decidable by lookup, and a decidable checker may require infeasible resources.
>
> **Estimability.** Closure is not sufficient. `H(V)` is taken with respect to `P` (§2), so `P` must be
> known well enough to estimate. Where the deployment distribution is unknown, unstable, non-stationary,
> or only partly observable, the demand is well defined and cannot be computed [DDD-measure-12]. A
> verdict function alone does not deliver a number.

(The section continues with the constructive-closure rung and its retirement note, which is R-4
material and is quoted at §7 below.)

> ### 8.1 What the boundary does not claim
>
> **An open predicate does not abolish measurement.** Where evaluators disagree there are distributions
> over their judgments; where preferences are elicited there are distributions over preferences; where
> outputs are scored there are distributions over scores. Those are measurable, and some are informative.
> What is unavailable outside the scope condition is *this construction* — a deterministic verdict
> function to take the entropy of — and not measurement as such. […]

> ### 8.2 The coincidence, and what it is worth
>
> […] **Measurement and closure have the same domain** [DDD-measure-06].
>
> That is worth noticing and it is not evidence. The two arguments share a premise — the closure of the
> acceptance predicate — so their agreement about where the line falls is close to definitional on the
> measure's side. What is not definitional is that the line was drawn twice, from different materials,
> with neither drawing fitted to the other. That makes the boundary **principled rather than arbitrary**.
> It does not make the identification true, and the note does not argue that it does.

### 5.3 The contradiction, stated exactly

`DDD-measure-06` says **iff**. §8 concedes both directions, and it is worth being precise about which
sentence does which, because the two failures are not symmetric.

| Direction | What `DDD-measure-06` asserts | What §8 concedes | Sentence |
|---|---|---|---|
| **closes ⇒ measure exists** | closure is sufficient | it is not: *"A verdict function can exist without being usable"* — and conversely, `term:verdict` requires the **task class** to supply one correct output per input, which closure does not deliver. A predicate can close while the class supplies no such assignment. | §8 Existence / Availability |
| **closes ⇒ computable** | not asserted, but read in by *"the measure exists"* | *"the demand is well defined and cannot be computed"* — estimability is a third, independent failure | §8 Estimability |
| **¬closes ⇒ `H(V)` undefined** | the region outside is measurement-free | *"An open predicate does not abolish measurement… What is unavailable outside the scope condition is* this construction *… and not measurement as such"* | §8.1 |
| **the floor coincidence** | asserted at `established` | *"That is worth noticing and it is not evidence… close to definitional on the measure's side"* | §8.2 |

The last row is the one that bites hardest on **status**. `established` requires a derivation or
theorem (rule 2). The node's own evidence note says the derivation covers limb (a) and that limb (b)
is a coincidence to be claimed as *principled, not convergent* — and the companion projection, written
later and merged, says the coincidence *is not evidence*. **A claim at `established` whose only
evidence entry disclaims the half that carries the content is not defensible on this repository's own
rules**, independently of any external reviewer.

---

## 6. Every dependent node

Sites are grouped by what a repair would actually do to them. Session records (`meta/sessions/`) are
history and are listed only where they carry a live instruction.

### 6.1 Dependents of `DDD-frame-15`

| Site | Kind of dependency | What a repair touches |
|---|---|---|
| `core/13-delivery.md` §4 | **Exposition home.** Restates the claim and the seam guard in prose (lines 79–90) | Prose must move with any statement change; the seam-guard paragraph is untouched by both dispositions |
| `core/13-delivery.md` §5 line 106 | "adds no store — `DDD-frame-15` partitions discharge rather than supply" | Unaffected; this *is* the guard |
| `core/claims/DDD-frame-16.yaml` | **Derivation premise**, step 3: "every completed act's demand is discharged by one of four modes" | **Live basis edge.** Step 3 says "one of four modes" — literal mode count enters frame-16's derivation |
| `core/decisions/DDD-dec-24.yaml` | Wave 3 ruling record; §67 records the foundation-table divergence, §75 the luck-ruling provenance, §96 the compact form | Historical; a supersession is recorded against it, never in it |
| `releases/v5.7.0.yaml` | Release descriptor, immutable | **Never edited.** Any change ships in a new descriptor |
| `graph/upstream.yaml` (downstream) | **Pinned**, `status_at_pin: projected`, `content_hash: sha256:6d14509d…` | **W6 content-drift on any statement or notes change.** Prediction stated at §8 |
| `projections/tracks/01-determination.md` rung 9 (lines 61, 785, 790) | Projection, cites as **projected** | Re-read required; a mode-name change rewrites rung 9 |
| `papers/paper-a/paper-a.md` line 368 | **Block quotation** of the statement, verified by `check-quotations.py` | **Any statement change fails the quotation checker** until the paper is revised — and Paper A's revision is out of scope |
| `papers/paper-a/paper-a.md` line 396 | Table row: "filed decision · judgment · default · draw" | Same |
| `papers/paper-a/paper-a.md` Appendix A | Rendered statement row, verified by `check-appendix.py` | Regenerated, never hand-edited |

### 6.2 Dependents of `DDD-frame-02` / `term:residual-discretion`

| Site | Kind of dependency | What a repair touches |
|---|---|---|
| `core/14-indexed-determination.md` §2 | **Exposition home and `establishes` contract**; carries both terms as `ddd:embed` blocks | Canonical text is edited **here** — in `terms.yaml` — and re-projected into §2 |
| `core/graph/terms.yaml` | The registry entry itself | The R-2 repair site |
| `core/decisions/DDD-dec-26.yaml` | The mint ruling; `[PROPOSED]` banners still standing | Historical. **Its `[PROPOSED]` banners are a standing freight item, not this session's** |
| `core/decisions/DDD-dec-27.yaml`, `DDD-dec-28.yaml` | The deliberate non-pinning, then the pin at `v5.8.0` | Historical |
| `graph/upstream.yaml` (downstream) | **Pinned**: `DDD-frame-02` at `sha256:f45492ee…` (projected); `term:residual-discretion` at `sha256:77284b14…` (draft); `term:commitment-level` at `sha256:7714da9e…` (draft) | **W6 on each node actually changed.** Prediction at §8 |
| `projections/tracks/01-determination.md` rungs 5 and 6 (lines 47, 51, 463, 528, 534) | Projection | Rung 6 embeds the term's canonical text |
| `papers/paper-a/paper-a.md` lines 276, 314, 884, 1199 | Two **block quotations** (`DDD-frame-02` statement; `term:residual-discretion` canonical text) plus two prose citations | **Quotation checker fails on any text change** |
| `papers/paper-a/paper-a.md` Appendix A lines 1342, 1404 | Rendered rows | Regenerated |

### 6.3 Dependents of `DDD-measure-06`

| Site | Kind of dependency | What a repair touches |
|---|---|---|
| `core/09-the-measure.md` line 28 | Claim-map row: "§7 \| The measure exists iff the predicate closes; vanishes at the floor" | Row rewrites with the successor |
| `core/decisions/DDD-dec-08.yaml`, `DDD-dec-19.yaml` | `basedOn` edges | **Live basis edges into a node proposed for retirement.** Both must be checked: a retired node may be *based on* but a decision resting on a retired claim needs a note |
| `meta/measure-paper-context.md` line 111 | Upstream context table listing it `established` | Editorial |
| `papers/measure-note/measure-note.md` line 782 | Cited in §8.2 for "Measurement and closure have the same domain" | The successor for the coincidence limb goes here |
| `papers/measure-note/measure-note.md` Appendix A line 1006 | Rendered row, `established` | Regenerated |
| `papers/measure-note/measure-paper-context.md` line 123 | Context | Editorial |
| `papers/paper-a/paper-a.md` lines 532, 605, 756, 911 | **Four prose citations, three of them carrying the bolded `established` status inline** | Every one is a status-bearing citation; a demotion makes all four wrong |
| `papers/paper-a/paper-a.md` line 756 | Near-verbatim restatement of the second limb | Check against the quotation checker |
| `papers/paper-a/paper-a.md` Appendix A line 1368 | Rendered row | Regenerated |
| `papers/paper-a/reviewer-brief.md` line 61 | Quotes the claim to the reviewer | Editorial |
| **Not pinned** in `graph/upstream.yaml` | — | **No W6 fires for R-3.** The exposure is the quotation and appendix checkers, not the pin checker |

### 6.4 Dependents of `DDD-cost-20`

| Site | What a repair touches |
|---|---|
| `core/10-cost.md` line 30 (claim map), line 265 (exposition) | Untouched — no change to `DDD-cost-20` is proposed |
| `core/claims/DDD-hyp-05.yaml` line 27 | Basis edge; untouched |
| `core/claims/DDD-cost-21.yaml` (downstream) line 8 | "rests on the upstream locus claim (`DDD-cost-20`, pinned)" |
| `core/14-maturation.md` (downstream) lines 124, 138 | Exposition |
| `graph/upstream.yaml` | Pinned at `sha256:f15de6f5…` (projected) |
| `papers/paper-a/paper-a.md` lines 336, 1001, 1334 | Two prose citations and the Appendix row |

**`DDD-cost-20` is surveyed, not repaired.** It enters R-1 only as the third limb of the
trained-inference overlap — it is what makes a trained carrier's supply *encoded* and therefore
timed *before the act*. Neither disposition changes it.

---

## 7. R-1 — the discharge partition

### 7.1 Diagnosis: three overlaps, and they are not the same kind of defect

The prompt reports three. Testing each against canon at `v5.9.0` separates them:

**(i) Declared default vs filed decision.** A declared, governed default is both. **This is a real
axis mixing, and canon half-knows it.** Step 4's own note says the modes classify *the producer*,
not governance status — yet the two modes it fails to separate are separated by nothing else. Read
step 4's glosses side by side:

- *filed decision* = "authored in advance and **delivered**"
- *arrangement default* = "carried by the arrangement's standing configuration **without a fresh
  resolution**"

A lookup table is authored in advance, delivered, carried by standing configuration, and involves no
fresh resolution. It satisfies both glosses completely. The only feature that would separate them is
**whether the fixed thing was authored as a decision about this class of case** — which is
*provenance*, a dimension the claim never names — or **whether it is governed**, which the region
field forbids this claim from using. **Neither mode can be reached from the other by a locus test,
because they do not differ in locus.**

**(ii) The thermostat.** A thermostat reads ground at the act and produces output by a rule fixed
beforehand. Canon times a rule as `term:encoded` — *before* the act. The gloss for the judgment mode
reads "produced at the act by an actor reading ground", which describes the thermostat exactly.
**This is a name collision, not an axis mixing**, and it is sharper than a reader's confusion:

> `term:judgment` — "determined *during* the act, **by an actor reading ground, with an accountable
> party named**… A judgment allocation naming no accountable party is not an allocation. It is
> Escaped with an executor attached."

The minted term carries an **accountability clause**. `DDD-frame-15`'s judgment *mode* cannot carry
it — an ungoverned actor's variation still discharges the act, and saying otherwise would collapse
the discharge partition into the store partition, which is precisely what the seam guard forbids.
**So `DDD-frame-15`'s "judgment" and `term:judgment` are two different objects sharing one word,
inside canon, today.** That is a defect the reviewer found from outside and canon can confirm from
inside.

**(iii) Trained inference.** Policy-level commitment, judgment, and standing supply at once. **This
is neither a name collision nor a two-way axis mixing — it is the flat list failing to represent a
composition.** Canon already has the vocabulary that represents it, in a claim the review also
touches: `term:commitment-level` says an arrangement commits at outcome, policy, or principal level,
and *"the three compose"*. A trained carrier is **committed at policy level and open at outcome
level**. `DDD-cost-20` adds the third limb: training converts judgment allocation to *encoded*
allocation, and `term:encoded` times encoding before the act. Three true descriptions, one flat list
with room for one.

### 7.2 The unit of classification, which the statement never states

`DDD-frame-15`'s `test:` field quantifies over **"every completed act's outcome-relevant
alternatives"**. The `statement:` quantifies over acts and says the *act's* demand is discharged by
one of four modes. **Those are different claims**, and several reported overlaps dissolve the moment
the unit is fixed at the alternative rather than the act — a timeout act has a *when-to-stop*
alternative and a *what-to-return* alternative, and they discharge differently. Both dispositions
below fix the unit explicitly. This is a repair the review did not ask for and the six-case test
forces.

### 7.3 The six cases, tested against **both** dispositions before either is proposed

The rule under test for **(a)** is the strongest priority ordering the session could construct
without inventing criteria. Applied to each outcome-relevant alternative, first match wins:

1. Is the resolving variation in nothing the arrangement controls? → **uncontrolled draw**
2. Else, is it produced at the act by an actor reading ground? → **judgment**
3. Else, was it authored in advance and delivered to this act? → **filed decision**
4. Else → **arrangement default**

The axes under test for **(b)** — three, of which two are already canon:

- **Axis 1 — producer of the resolving variation.** `artefact` · `actor` · `uncontrolled`.
  Three values, mutually exclusive, exhaustive by step 4's case split once *filed decision* and
  *arrangement default* are merged (they do not differ in locus — §7.1(i)). **Deliberately renamed
  off the store vocabulary.**
- **Axis 2 — level at which the arrangement committed** (`term:commitment-level`, canon at
  `v5.8.0`). `outcome` · `policy` · `principal` · `none reached this alternative`.
- **Axis 3 — occasion** (`DDD-frame-16`, canon at `v5.7.0`). `inherited` · `occasioned`.
- **Axis 0 — governance status is not an axis of this claim.** `term:store` answers it. This is the
  seam guard restated as an exclusion rather than as a paragraph, and it is what keeps the guard
  untouched.

| # | Case | Alternative(s) | **(a) priority rule** | **(b) axes** |
|---|---|---|---|---|
| 1 | **Trained inference** | what to output | rule 2 fires → **judgment**. Once. But the policy-level commitment and the encoded standing supply are *discarded*, not resolved — the classification is total because it throws away two of the three true things | Axis 1 `actor` · Axis 2 `policy` committed, outcome open · Axis 3 `occasioned` (output) over `inherited` (weights). **Once, and all three limbs survive** |
| 2 | **Lookup table** | which output for this key | rules 1–2 miss; rule 3 fires → **filed decision**. Once — but only because rule 3 is tried before rule 4; the table satisfies both glosses and the ordering, not the world, breaks the tie | Axis 1 `artefact` · Axis 2 `outcome` · Axis 3 `inherited`. Once |
| 3 | **Declared defaults** | which value when the trigger fires | rules 1–2 miss. **Rules 3 and 4 both fire.** Separating them needs *declared* — governance status — which the region field assigns to the store partition. **The tie cannot be broken without crossing the seam guard** | Axis 1 `artefact` · Axis 2 `outcome`, conditional on a trigger · Axis 3 `inherited`. Once. Declaredness never enters — it is Axis 0, off this claim | 
| 4 | **Randomised search with checking** | (α) which candidate is drawn; (β) which candidates are admissible | α → rule 1 → **draw**. β → rule 3 → **filed decision**. Once each, and correctly: the check is an assurance position, not a discharge mode | α: Axis 1 `uncontrolled` · Axis 2 `none` · Axis 3 `occasioned`. β: Axis 1 `artefact` · Axis 2 `outcome`-as-constraint-set · Axis 3 `inherited`. Once each |
| 5 | **Abstention** | whether to resolve; and, if abstention is expressed, what lands | If the abstention is **expressed as an outcome**: rule 2 → **judgment**. Once. If it is **not expressed**, the act does not complete and falls outside the claim's region — also a single, correct disposition | Expressed: Axis 1 `actor` · Axis 2 `policy` if the abstain rule is authored (*"abstain below θ"*), `none` if the actor simply declined · Axis 3 `occasioned`. Unexpressed: out of region. Once |
| 6 | **Timeout** | (α) when to stop; (β) what to return at the cut | α: rules 3 and 4 **both fire** on the deadline — an authored artefact that is also standing configuration. **Same tie as case 3.** β → rule 1 → draw | α: Axis 1 `artefact` · Axis 2 `outcome` (the deadline) · Axis 3 `inherited`. β: Axis 1 `uncontrolled` · Axis 2 `none` · Axis 3 `occasioned`. Once each |

**Result, by the prompt's own criterion.**

- **(a) fails.** It classifies four of six cleanly and **ties on cases 3 and 6α**, and both ties are
  the same tie: *filed decision* against *arrangement default*. Every ordering that breaks it must
  appeal to **declaredness — governance status — which the region field reserves to the store
  partition.** A priority rule that classifies all six exactly once therefore does so **by crossing
  the seam guard**, which this session is instructed to leave untouched and which is correctly
  ratified. Case 1 is a second, softer failure: (a) is total there only because it discards the
  policy-level and standing-supply limbs the review reports.
- **(b) passes.** All six classify exactly once on Axis 1, with Axes 2 and 3 carrying what the flat
  list destroyed. Governance status never enters, so **the seam guard is untouched — and is
  strengthened**, moving from a paragraph a reader may skip to an axis the schema excludes.

### 7.4 The naming question the review does not ask

**Does the confusion come partly from the shared words? Yes — and it is worse than confusion; it is
a live collision inside canon.** But **renaming carries roughly one of the three overlaps, and the
axis recast carries all three.** Scored against the reported defects:

| Overlap | Distinct names alone would fix it? | Axis recast alone would fix it? |
|---|---|---|
| (ii) thermostat / judgment | **Yes.** The collision *is* the word: `term:judgment` carries an accountability clause the mode cannot carry | Yes — Axis 1's value is `actor`, and accountability is Axis 0 |
| (i) declared default / filed decision | **No.** Renaming two modes that do not differ in locus leaves two names for one thing | **Yes.** They merge into `artefact` and re-separate on Axis 2 |
| (iii) trained inference | **No.** Any flat list of four has room for one answer where three are true | **Yes.** That is what axes are for |

**Recommendation: do both, and the naming is the cheaper half of one disposition, not an
alternative to it.** Disposition (b) already requires new value names for Axis 1, and the session
proposes `artefact` · `actor` · `uncontrolled` precisely because none of the three is a store name.
*filed decision*, *judgment* and *default* all retire as discharge vocabulary; `term:judgment`,
`term:store` and `term:delivery` keep their words unshared.

### 7.5 Proposed disposition for R-1

> **(b) — the modes recast as orthogonal axes**, with Axis 1 renamed off the store vocabulary, the
> unit fixed at the outcome-relevant alternative, and governance status excluded by construction.

**Shape of the repair, per the supersession rule** (`DDD-dec-09`/`10`/`15`) — drafted at Gate 2, not
now:

- `DDD-frame-15` is **superseded, not rewritten**. It stays in the graph with the correction that
  killed it, per `DDD-measure-08`.
- A successor node carries Axis 1 as the discharge partition proper — three values, `artefact` ·
  `actor` · `uncontrolled` — quantified over outcome-relevant alternatives, with the compact form
  (*demand is never unmet, only ungoverned*) intact and the seam guard carried into `region:`
  verbatim.
- Axes 2 and 3 are **not new claims**: they are `term:commitment-level` and `DDD-frame-16`, already
  canon, and the successor's `notes:` records that the three axes compose. **Nothing is minted for
  R-1.**
- `DDD-frame-16`'s derivation step 3 reads "one of four modes" and needs a **notes-only** amendment
  to track the successor. Flagged now; it is the one live basis edge that carries the mode count.

**One resistance, named rather than resolved** (the C-1 precedent). Case 5's unexpressed abstention
turns on whether an abstained-from episode is a **completed act** — `term:act` runs "to an expressed
outcome", so the session's reading is that it is not, and the case falls outside the region. That
reading is **stated, not decided**: it touches `term:act-individuation`, and if Emil judges it a
decision the framework has not made, the successor node's region says so and the case defers.

---

## 8. R-3 — proposed disposition for `DDD-measure-06`

The prompt asks for the statement, region, evidence note, falsifier and status verbatim alongside
§8; §5 above delivers all of it, including the finding that **there is no falsifier**.

### 8.1 Proposed shape

> **Supersede `DDD-measure-06` with two nodes, splitting on the rule-1 fault line the node already
> carries, and demote only the limb that needs demoting.**

- **`DDD-measure-06` → `retired`**, kept in the graph with the correction that killed it, per rule 3
  and the `DDD-measure-08` exemplar. `notes:` records the correction in the repository's own words:
  the node's evidence field said *"Claim the boundary as principled, not as convergent evidence"*,
  and the node did the opposite.
- **`DDD-measure-16` (new, `formal`)** — the **availability** limb, narrowed as the prompt directs:
  *this construction is available to an arrangement only where the task's acceptance predicate
  closes for that arrangement.* **Existence and estimability are separated as §8 already separates
  them**, and they belong in `region:`, which is where boundedness is stated and never implied
  (rule 5): existence is a condition on the task class supplying a verdict function, availability is
  closure for the arrangement, estimability is a condition on `P`, and the three fail differently.
  `supersedes: DDD-measure-06`.
- **`DDD-measure-17` (new, `conceptual`)** — the **coincidence** limb, carrying what §8.2 actually
  supports: the construction's domain and the non-zero-floor region coincide, the coincidence is
  **principled rather than evidential** because the two arguments share the closure premise, and the
  agreement is not evidence for the identification. `supersedes: DDD-measure-06`.

**Why two successors and not one.** `DDD-measure-06` is cited at nine live sites across two
projections, five of them for the coincidence specifically (`paper-a.md` 532, 605, 756, 911;
`measure-note.md` 782). Retiring without a successor for that limb orphans five citations in
documents this session is forbidden to revise. Two successors keep every citation re-pointable by a
one-token edit.

### 8.2 The status proposal, and its warrant — **Emil's to rule**

> **`DDD-measure-16`: `established`. `DDD-measure-17`: `projected`.**

The demotion lands **on the coincidence, not on the boundary**. The warrant is the repository's own
rules, in this order:

1. **The evidence note is the warrant against itself.** *"near-definitional on the measure side; the
   force of the claim is the coincidence… Claim the boundary as principled, not as convergent
   evidence."* Near-definitional content is establishable — rule 4 says an identity that holds is
   `formal` and can be established. The coincidence is not that, and the note says so.
2. **The companion projection concedes it.** §8.2: *"That is worth noticing and it is not
   evidence."* A claim at `established` whose own companion projection says its content is not
   evidence fails `established`'s entry condition (rule 2: a derivation or theorem).
3. **`CLAUDE.md`'s standing instrument.** *"Never present an identity holding as evidence for the
   framework. State which is arithmetic and which is a modelling claim, always."* The split into
   `formal`/`established` and `conceptual`/`projected` is that instrument applied to a node that
   fused the two — which rule 4 forbids in terms: *"Never fuse them in one file."*

**`projected` requires a falsifier** (rule 2), and `DDD-measure-06` has none to inherit. One is
drafted at Gate 3 rather than asserted here. The shape it must take: an arrangement for which the
construction's domain and the non-zero-floor region **come apart** — a task whose predicate does not
close for the arrangement and whose floor is nevertheless zero, or a closing predicate with non-zero
floor. `DDD-measure-06`'s existing `test:` — *"a task with an open predicate for which a defensible
verdict function exists anyway"* — is the second half of that and carries forward.

**Three alternatives the session considered and is not proposing**, so the ruling is made against
real options:

- **Amend `DDD-measure-06` in place.** Rejected: it is `established` and ratified, and this session
  supersedes rather than rewrites.
- **Retire outright with no successor.** Rejected: orphans nine citation sites in two projections
  this session cannot revise.
- **Four successors, one per §8 requirement plus the coincidence.** Rejected as above booked size —
  existence and estimability are *conditions on the same construction*, and `region:` is the field
  the schema provides for exactly that.

### 8.3 What R-3 does **not** touch

The decoder repair — arrangement-relative admissibility, review item 8 — is **not attempted**, per
the prompt. Note for the record that `DDD-measure-16`'s narrowing to *availability **to an
arrangement*** is adjacent to it and stops short: it relativises the *construction's availability*
to an arrangement, which `term:closure` already does (*"closed for an arrangement"*), and asserts
nothing about which conditioning variables are admissible.

---

## 9. R-4 — recorded, not repaired

The closure ladder is `papers/paper-a/paper-a.md` §5.2, lines 598–627. Its fourth rung:

> | **Formally decidable** | An acceptance procedure exists and terminates over the declared domain. | [term:closure]'s reservation |

and its prose:

> **Formally decidable.** Placed last and deliberately not at the top. Canon reserves *decidable* for
> the formal special case rather than making it the requirement [term:closure] […] Decidability is
> therefore a special case of the ladder rather than its summit, and the rungs that govern deployed
> arrangements are the middle two.

**The paper already saw half of it and stopped half-way.** It knows decidability is not the summit;
it still places it *on the ladder*. The review's point is stronger: the other three rungs are
**arrangement-indexed operational properties** — can *this* arrangement evaluate, can *this*
arrangement produce, within *declared* bounds — and formal decidability is a **logical property of
the predicate**, true or false with no arrangement in the index at all. It is not a higher rung or a
lower one. **It is not on that axis.**

This is Paper A prose and repairs at the paper's revision, which is out of scope. **It is recorded
here as a constraint on Q32's eventual filing**, drafted at Gate 4 into the successor-items record:

> **Constraint on the Q32 constructive-closure node.** The node must be filed on a single axis —
> arrangement-indexed operational closure, with `verification-closed` and `constructively closed` as
> its rungs. **Formal decidability is not a rung and must not be filed as one.** It is a logical
> property of the predicate, not an operational property of an arrangement, and `term:closure`
> already carries it correctly as a *reservation* rather than a position: *"**Decidable** is
> reserved for the formal special case."* A Q32 node that admits decidability as a fourth rung
> reproduces Paper A §5.2's axis error in canon, where it is far more expensive to remove.

---

## 10. Instruments — predictions recorded before any operation

Per the convention, stated **now**, before anything runs.

**Baselines at arrival, all green.** Upstream: `validate-core-order.py` exit 0, 15 documents,
70 terms, 0 errors, **66 warnings, zero W4**; `validate-claims.py` 60 claims valid; decisions 8
valid; `validate-releases.py` 5 descriptors valid. Downstream: `validate-core-order.py` exit 0,
5 documents, 0 errors, 0 warnings, **67 pins resolved, 0 basis-loss, 0 content-drift, 1 shadowed
id** (the standing W7, unchanged since `v5.8.0`). `check-quotations.py` **29 verbatim, 0
disclosed-partial, 0 failing** against `v5.9.0`. `check-appendix.py` **72 rendered, 72 cited, 0
discrepancies** against `v5.9.0`.

**Predicted content-drift, if Emil rules both dispositions as proposed.** No pin operation happens
before Gate 4; this is the prediction it will be checked against.

| Node | Pinned at | Changed by | Predicted |
|---|---|---|---|
| `DDD-frame-15` | `sha256:6d14509d…`, projected | superseded → `retired`, `notes` gains the correction | **W6 content-drift** |
| `DDD-frame-02` | `sha256:f45492ee…`, projected | R-2 amendment | **W6 content-drift** |
| `term:residual-discretion` | `sha256:77284b14…`, draft | canonical text corrected | **W6 content-drift** |
| `term:commitment-level` | `sha256:7714da9e…`, draft | **not changed** | **no W6** |
| `DDD-cost-20` | `sha256:f15de6f5…`, projected | **not changed** | **no W6** |
| `term:judgment`, `term:closure` | settled | **not changed** | **no W6** |
| `DDD-measure-06` | **not pinned** | retired | **no W6 — the exposure is the quotation and appendix checkers, not the pin checker** |
| new successors | — | do not exist at `v5.9.0` | **unpinnable until the tag** — the `DDD-dec-27`/`DDD-dec-28` pattern applies again |

**One prediction that is not about pins and matters more.** `check-quotations.py` verifies **block
quotations of claim statements** against the pinned ref. Paper A block-quotes `DDD-frame-15`'s
statement (line 368), `DDD-frame-02`'s statement (line 276), and `term:residual-discretion`'s
canonical text (line 314). **If those statements change and Paper A is not revised — and Paper A's
revision is explicitly out of scope — the quotation checker fails on three quotations.** The
successors are new IDs, so the old quotations still resolve against the *retired* nodes and may
survive; that is a prediction the session cannot make confidently from reading the script's
docstring, and it will be **run rather than assumed** at Gate 4, before any pin advance. Flagged
now because it may constrain the shape Emil rules.

---

## 11. What is asked at this gate

1. **R-1 — rule (a) or (b).** The session proposes **(b)**, with the naming carried inside it, and
   reports that **(a) cannot classify all six cases exactly once without crossing the seam guard**.
2. **R-3 — rule the shape and the status.** The session proposes supersession into two nodes, with
   **`established` retained for the availability limb and `projected` for the coincidence**.
3. **Two findings that may change the instructions themselves**: `term:residual-discretion` **is
   already minted** (§0.2), so R-2's question is a canonical-text correction and not a mint; and
   **neither review input arrived** (§0.1).
4. **One reading stated rather than decided**: whether an unexpressed abstention is a completed act
   (§7.5).
