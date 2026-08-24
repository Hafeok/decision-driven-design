# GATE 3 — D-3 the design rulings, D-4 the migration's shape

**Status: ratified at its gate (Emil).** Nothing outside this directory has been touched.

Per the GATE 2 ruling: **volume is a cost, not a vote.** Every argument below is made from canon's
definition and canon's usage. The three repositories' counts enter only where cost is priced, and
are marked as cost when they do.

---

## 0. The question changed shape, and the audit is the first artefact that could tell

Emil asked at GATE 2 whether canon's prose is **drifting from its own settled term**, or whether the
**settled term is too narrow** for what canon needs the word to do. Opposite remedies: a prose repair
against a definitional one.

**The audit answers it, and the answer is neither drift nor narrowness alone — the definition layer
is itself multi-sense.** Here is every occurrence in `core/graph/terms.yaml`, the settled layer,
grouped by the sense it carries:

| Settled term | The words | Sense |
|---|---|---|
| `term:ground` | *"what they are determined against"* | **S1** |
| `term:admission-test` | *"a fact is ground iff varying **the world** moves the outcome past tolerance"* | **S1** |
| `term:act` | *"an act is decisions **resolved against** ground"* | **S1** |
| `term:determination` | *"the resolving of a decision **against** ground"* | **S1** |
| `term:attribution` | *"which determinations were made, by whom, **against what ground**"* | **S1** |
| `term:actor` | *"resolves decisions by **reading ground**"* | **S3** |
| `term:judgment` | *"determined during the act, by an actor **reading ground**"* | **S3** |
| `term:poisoned-ground` | *"ground that is **present** but false: the substrate a determination **reads**"* | **S3** |
| `term:capacity` | *"hold capacity — the bits of ground it can have **in context** at once"* | **S3** |
| `term:overflow` | *"the decision's governing ground **does not fit**… the ground **fits and is held**"* | **S3** |
| `term:residual-discretion` | *"held at **fixed ground**… the ground **at the act**"* | **S3** |
| `term:closure` | *"the relevant ground is **observable**"* | **S2** |
| `term:encode-verify-split` | *"**pre-resolving ground into the encoded store** before the act"* | **S2** |
| `term:accountability` | *"executor, prior commitments, **ground channels**, checks, reviewers, record"* | **S2** |
| `term:verdict` | *"let `P` be the distribution over inputs (the ***ground distribution***)"* | **S5** |

> **Fifteen settled terms. Four senses. One registry.**

**This forecloses the prose-repair remedy.** You cannot repair prose to comply with `term:ground`
when ten other *settled* terms in the same registry — including the one that defines what an actor
*is* — use the word otherwise. The prose is not drifting from the definition; **it is faithfully
following the definition layer, which is not single-sensed.**

**And it forecloses the simple narrowness remedy too.** `term:ground` is not too narrow for canon's
*prose*; it is too narrow for canon's **own registry**. That is a stronger claim and it is the one
the counts support.

Corroboration from usage, canon only, rule-assigned and exact:

| | S1 | S2 | S3 | S4 | S5 | U |
|---|---|---|---|---|---|---|
| canonical text (registry + claims + decisions) | **38** | 15 | 22 | 1 | 10 | 26 |
| canon prose (`core/*.md`) | 28 | 4 | **32** | 2 | 11 | 5 |
| **the registry alone** | 6 | 1 | **12** | 0 | 1 | 0 |

**The registry — the settled layer, the authority within the authority — uses S3 twice as often as
S1.** Claim and decision statements lean S1; prose and the registry lean S3. A drift story requires a
clean origin to drift *from*, and there is none.

---

## D-3 · Question 1 — which sense keeps `ground`?

### The recommendation, and it is not the assessment's

> **S1 keeps the word — the conditions in the case whose variation moves the outcome past
> tolerance — and the recommendation is made on canon's authority, not on the counts.**

The assessment recommended the same sense; the audit reaches it by a different route and with one
correction to the assessment's reasoning, which matters because the correction is what makes the
recommendation survive the counts.

**The argument, from canon and in this order:**

1. **`term:ground` and `term:admission-test` are both `settled`, and both state S1.** The admission
   test is not a gloss — it is the *test by which a fact is admitted as ground at all*, and it
   quantifies over **the world**, not over any record. No other candidate sense has an admission
   test in canon.
2. **The primitive is defined as the object determination runs against, and three further settled
   terms repeat that construction** — `term:act`, `term:determination`, `term:attribution`, each
   using *"against"*. That is the framework's most-repeated formula for the word.
3. **`DDD-ground-05` makes S1 constitutively prior**: *"Declaring the determinable space is
   constitutively prior to determination over it."* Ground-as-declared-determinables is the sense
   that has a **claim** behind it, and `term:determinable` (settled, `v5.7.0`) already supplies that
   sense's formal structure — Johnson's determinable/determinate.
4. **No other sense has that spine.** S2 has no admission test and no claim defining it; it is
   carried by compounds (`accessible ground`, `ground registry`). S3 is carried entirely by *verbs*
   — *reading*, *held*, *present*, *in context*, *fits* — which is exactly what one would expect of
   a sense that is a **relation to** the primitive rather than the primitive.

**That last point is the audit's own contribution and it is the load-bearing one.** S3 is not a
rival primitive competing with S1 for the noun. It is *what happens to S1 at an act*. Canon's
S3 occurrences almost all read as **verbs applied to ground**, not as a different thing called
ground:

- upstream S3 by rule: `reading-ground` 44, `poisoned-ground` 46, `delivered` 14, `reads-different-ground` 6.
- **Every one of those is a predicate over the S1 object.** *Reading* ground, ground being *present*,
  ground *held in context*, ground *delivered*.

**So the split is not five peers.** S1 is the primitive; S2 and S3 are **states of S1 relative to an
arrangement and to an act** — which is precisely the shape `term:delivery` already gives the decision
side. The proposal treats `relevant state`, `decision basis` and `act basis` as three objects. The
audit's reading of canon is that there is **one object in three conditions**, and that is why the
delivery vocabulary fits (Question 2) rather than needing a parallel invention.

### What the counts say, entered as cost and not as vote

| Disposition | Migrating occurrences | The expensive part |
|---|---|---|
| **S1 keeps the word** (recommended) | ~2,357 of 2,845 | **`product-cli`'s 864 S2 occurrences**, including a crate, a binary, a module tree, and `ground:` as a serialised ledger field |
| S2 keeps the word | ~1,207 | canon's own S1 and S3 — the registry, the admission test, five settled terms' canonical text, and both merged papers |

**The recommended disposition is the more expensive one, by roughly two to one, and the audit
recommends it anyway.** Canon is the authority and the projection follows; the software repository's
volume prices the choice and does not make it. **But the price is real and it is Emil's to accept**:
S1 keeping the word means the software repository migrates a serialised field name, which is a data
migration, not a rewrite. Question 4's answer and D-4's shape are both built around softening that.

---

## D-3 · Question 2 — how do S2 and S3 name themselves against the delivery vocabulary?

### The recommendation

> **Reuse, do not mint beside.** The delivery vocabulary already models exactly this relation on the
> decision side; S2 and S3 are the same relation on the ground side, and canon should say so rather
> than build a parallel set of nouns.

`term:delivery` (draft, `v5.5.0`):

> **Delivery** is how authored governance reaches an act: **mechanical** … or **judgment-mediated**
> … Delivery is a property of a decision **at an act-site**, never of the decision alone.

**Read that with "ground" substituted for "a decision" and it is S2 versus S3 exactly.** The
structural claim — *a property at an act-site, never of the object alone* — is the whole content of
the held/delivered distinction, already ratified, already act-indexed.

**Concretely, three reuses and no new primitives:**

| Object | Name | Why this and not a mint |
|---|---|---|
| S2 — what the arrangement holds | **available ground** | `term:closure` already says *"the relevant ground is **observable**"*; availability is the word canon uses for the same idea in `DDD-measure-16`'s region. `accessible ground` (13 occurrences) is the existing usage and can be promoted rather than replaced |
| S3 — what reaches the act | **delivered ground**, act-indexed | Direct reuse of `term:delivery`. The compound already reads correctly in canon's own sentences: *"the ground at the act"* |
| the failure mode | **undelivered ground** | `term:undelivered` is already minted for exactly this shape on the decision side: *"filed, adequate, and never reached the act… escape, with a distinguishing feature — **the ledger shows coverage**"* |

**`term:undelivered` is the strongest evidence for reuse in the whole audit.** Its canonical text
describes, word for word, what the proposal calls a `basis gap` of the *inaccessibility* kind — and
it already names the failure that makes it dangerous: **escape that presents as governance.** Minting
`basis gap` beside it would give canon two names for one mechanism, on opposite sides of a seam that
the same session is trying to close.

**And `term:presumed-discharge` supplies the instrument** the ground side would otherwise need to
invent: *"a gate's pass meaning never-reached: the artefact recording the skip is identical to the
artefact recording the pass."* Q27's holding note reaches the same conclusion independently —
*"Presumed discharge (Q18) transposed to the ground layer"* — which is a fourth arrival on SR-1's
list that SR-1 does not count.

**One thing this reuse does not solve, stated rather than hidden:** the proposal's `corrupted basis`
has an existing canon home — `term:poisoned-ground`, settled — but that term is currently **S3 by its
own words** while its head word would become S1. Under the recommendation, `poisoned ground`
**changes sense without changing text**, which is the single largest hidden cost in Question 1's
disposition and is flagged for D-4 rather than solved here.

---

## D-3 · Question 3 — is provenance an enumeration or several independent attributes?

### The recommendation

> **Several independent attributes. The proposal is right, canon already half-says so, and
> `DDD-dec-26`'s ruling is not an obstacle — it is a different question that has been read as this
> one.**

**What `DDD-dec-26` actually ruled**, verbatim:

> the five-way ground-provenance taxonomy is ruled **ineligible for minting** because its
> institutional slot is **Q27-gated**.

That is a ruling about **minting**, with a stated reason: one of the five values had no mechanism
behind it. It is not a ruling that the five values are mutually exclusive, and it does not survive
being cited as one.

**Canon already carries the orthogonality claim.** `DDD-ground-02`, `projected`:

> Source coverage (covered · declared-empty · undeclared · unknown), resolution (resolved ·
> deliberately-open · unknown), and assurance (adequate · inadequate · unknown) are **orthogonal
> properties of ground relative to a filed decision**.

**Three independent axes over ground, filed, using the word "orthogonal".** The proposal's argument —
*"a controlled variable may also be observed, and an institutional record may contain an inference…
Provenance may work better as several independent attributes than as a single enumeration"* — is the
same move applied to the provenance axis, and `DDD-ground-02` is the precedent for making it.

**The audit's evidence for it, from the counts:** `ground provenance` occurs 44 times and classifies
**S2 at 95%** — it is consistently about held material. But the *values* it takes span senses:
`observed` and `inferred` are properties of **how a representation was produced** (S2); `controlled`
is a property of **the world** (S1); `institutional` is a property of **a rule** (S4). **A single
enumeration whose values live in three different senses is not an enumeration; it is three attributes
that have been flattened.** That is the audit's independent confirmation, and it is why the answer
does not depend on the proposal being persuasive.

**What this unblocks and what it does not.** Splitting provenance into independent attributes
resolves `DDD-dec-26`'s stated obstacle without waiting for Q27: the institutional *value* was
Q27-gated, but an institutional *attribute* — "this representation communicates a rule" — is not the
same object as the rule's normative force, which is Question 4's territory. **The gate was on the
value, not on the axis.**

---

## D-3 · Question 4 — does sense 5 simply leave?

### The recommendation

> **Yes. `ground distribution` → `deployment distribution`, and it is the cheapest thing in the
> audit. Confirmed from the counts, not assumed.**

| Evidence | Value |
|---|---|
| S5 occurrences, projected total | **105** (3.7%) |
| of which in **identifiers** | **0** |
| of which **immutable** | 5 |
| of which in `product-cli` | **1** |
| `ground distribution` compound, occurrences | 51 |
| pinned graph objects affected | **0** |

**S5 is the only sense with zero identifier occurrences.** Nothing named for it, no field, no crate,
no claim ID. It is prose and one asset filename (`measure-nonuniform-ground.py`).

**And canon already treats it as a separate parameter in everything but its name.** `term:verdict`,
settled: *"Let `P` be the distribution over inputs (the *ground distribution*)"* — the definition
introduces `P` first and names it second, which is what a separable parameter looks like.
`DDD-measure-16`'s region, filed at `v5.10.0` two days ago, calls it *"the ground distribution"* while
defining estimability entirely in terms of `P`.

**One correction to "simply leaves".** 29 of the 74 rule-assigned S5 occurrences are in the **merged
papers** — the largest per-sense concentration of paper occurrences in the audit. So S5 is cheap in
canon and **not free in the projections**, and it lands with a paper revision rather than instead of
one. Both papers are already owed revisions; this rides with them.

---

## The §7 / Q27 collision — reported, not resolved (SR-4)

Both texts, quoted whole enough to be ruled on.

**The proposal, §7 — "Acceptance standards and standing commitments":**

> Institutional rules should be classified by function:
>
> - A rule that determines which resolutions are acceptable belongs in the **acceptance relation** or
>   **acceptance standard**.
> - A policy that constrains how an arrangement acts belongs among its **standing commitments** or
>   constraints.
> - A record communicating a rule to a particular actor may appear in the **decision basis**, but the
>   record is not identical to the rule's normative role.
>
> This prevents "institutional ground" from becoming a catch-all category.

**Q27, holding note revision 18 §Q27 — "Trusted sources: institutional ground given a mechanism":**

> Canon has carried this slot empty since the foundation document: *institutional ground — supplied
> through rules, conventions, authority, or social practice.* Nothing stood under it. Emil's
> crocodile supplies the mechanism.
>
> **It is a supply-form claim.** … **Trust converts occasioned assurance into standing assurance.**
> … "Trusted" is therefore a governance status, not a belief state — an accountability structure
> standing behind ground you did not verify.
>
> **Trust closes predicates you could not otherwise close.** "Is this a carnivore?" is unevaluable
> over your own ground; it is *closed* over trusted ground: the acceptance procedure is
> source-consultation, and it terminates.
>
> **Filing shape.** `institutional` becomes a first-class provenance value with a *trust decision* as
> its mechanism.

**The collision, stated precisely.** §7 **removes** institutional rules from ground and distributes
them to the acceptance relation and to standing commitments. Q27 **fills institutional ground's empty
provenance slot** by making a trusted source's output *count as ground*, with trust as a filed
decision. Under §7, most of what Q27 calls institutional ground is reclassified out of ground
entirely; under Q27, `institutional` becomes a first-class provenance **value** — which Question 3
has just recommended splitting into attributes.

**What the audit adds, having been asked not to resolve it.** Three facts the migration session
should have when it rules:

1. **The category is small.** `institutional ground` occurs **13 times** (11 downstream, 2
   `product-cli`, **0 upstream**). S4 is the smallest sense at a projected 40 occurrences, 1.4%.
   **Whatever is ruled, it is cheap to execute** — the ruling is expensive, the edit is not.
2. **Canon does not currently carry the category at all.** Zero upstream occurrences of
   `institutional ground`. The slot the assessment and Q27 both describe as "empty since the
   foundation document" is empty *in canon*, and the 13 occurrences are all in the projection layer
   and the software. **Nothing in canon has to be unpicked either way.**
3. **Question 3's answer partially dissolves it, and this is worth ruling on directly.** If
   provenance is several independent attributes rather than one enumeration, then §7's third bullet
   and Q27's mechanism are **not in competition**: the *record* communicating a rule carries an
   institutional provenance attribute (Q27's mechanism, with its trust decision), while the rule's
   *normative force* sits in the acceptance relation (§7's first bullet). That is the assessment's
   own proposed reconciliation — *"the rule's normative force is in the acceptance relation; the
   arrangement's representation of the rule is a reading; the trust decision governs whether that
   representation may be relied on"* — and **Question 3 supplies the mechanism that makes it
   available** rather than merely plausible.

**Not resolved here, per SR-4.** The audit reports that the reconciliation is *cheaper than it
looked* and that one of its two halves is already ruled.

---

## D-4 — the migration's shape

**A recommendation, not a decision.**

### D-4.1 — the estimate is decision-grade and not execution-grade

**Stated first because it is the constraint everything else sits under, per the GATE 2 ruling.**

The classification is 64% deterministic and 36% sampled at n=100. **That is sufficient to take the
four rulings above and insufficient to cut a single file.** A decision can be taken on a bounded
estimate; a rename cannot be executed on one.

> **Before anything is cut, the 1,022 residual occurrences need full classification.** Nobody should
> read "36% sampled" as migration-ready.

The residual pass is bounded work and can be quoted: 1,022 occurrences across 249 files, of which
the rule table would likely absorb a further portion once written against the residual rather than
against the whole. It is one session, and it is the migration's first session rather than a
prerequisite to planning it.

### D-4.2 — a wave, not a session, and the split is by cost class rather than by repository

The audit's cost classes do not partition by repo; they partition by **what kind of edit each
occurrence needs**, and those have genuinely different risk profiles:

| Wave | Content | Occurrences | Why it separates |
|---|---|---|---|
| **W0 — complete the classification** | the 1,022 residual | 1,022 | D-4.1. Blocks everything |
| **W1 — sense 5 leaves** | `ground distribution` → `deployment distribution` | ~105 | Zero identifiers, zero pins, one `product-cli` occurrence. **Can land early and alone** |
| **W2 — canon's definitional repair** | `term:ground`'s scope stated once; the S2/S3 states named by reuse; the registry's fifteen terms made consistent | ~250 upstream | The ruling that makes every later wave mechanical. **Small, and the most expensive to get wrong** |
| **W3 — the projection layer** | apparatus, projections, applications, both papers | ~450 | Rides with the paper revisions already owed |
| **W4 — the software** | `product-cli` | ~1,286 | **A data migration, not a rewrite.** Own session, own rules, own risk |
| **never** | session records, release descriptors, `DDD-ground-*` IDs, ordinary English | ~536 | Immutable, or not the technical term |

**W1 can land early at near-zero cost and the audit recommends it** — that was the prompt's own
candidate and the counts confirm it.

**W4 deserves its own disposition, per the GATE 1 ruling that it be reported as a distinct cost
class.** Because it is 92% one sense, `product-cli` has an option canon does not: **the field name
`ground:` can stay while the concept is renamed**, at the price of a documented divergence between
the serialised format and the vocabulary. That trade-off is real and the audit surfaces it without
recommending it: a format field is a compatibility surface with readers and writers outside this
programme, and changing it is the only edit in the whole migration that can break something that
already runs.

### D-4.3 — what would have to defer

- **`poisoned ground` changes sense without changing text** (Question 2). Under the recommendation
  it becomes an S3 compound of an S1 head word — the exact shape that produced the defect. It needs
  its own ruling and probably a supersession, and it is `settled`, so it is not a migration edit.
- **The §7/Q27 reconciliation**, per SR-4 — but D-3 Q3 has made it cheaper.
- **`missing ground` and every relational concept.** See D-4.4.
- **The decoder repair** is not in this wave at all; the split makes the defect *easier to state* and
  does not fix it, as both the proposal and the assessment say.

### D-4.4 — a design requirement, not a hard row

**Per the GATE 2 ruling, carried as a requirement on the migration's design:**

> **The split must leave somewhere for relational concepts to live.** `missing ground` names a
> relation between S1 and S3 — a relevant condition inadequately represented at the act. A five-sense
> partition with no place for relations would lose it, and it would lose it silently, because each
> half would classify cleanly into a different sense.

The audit found 11 rule-assigned occurrences of `missing ground` and expects the class to be larger
than that one compound: `ground accessibility` (11), `ground coverage` (0 — a proposal coinage for
exactly this relation), and `DDD-ground-02`'s *"source coverage"* are all relational in the same way.
**Question 2's recommendation satisfies the requirement** — `undelivered ground`, reusing
`term:undelivered`, is a relational name by construction, because delivery is *"a property at an
act-site, never of the object alone."* That is why reuse beats minting here on more than economy.

### D-4.5 — the drafting-warning instrument needs a third exception

The proposal's implementation step 7:

> **Add a terminology check.** Treat an unqualified use of *ground* as a drafting warning, except in
> quotations or historical notes.

**It needs a third exception, and the audit counted the reason:** ordinary-English use — *"new
ground"*, *"common ground"*, *"the claim it grounds"*, *"its ground has changed"* — is a projected
**244-occurrence** unassignable class of which 32 are rule-assigned as ordinary English outright.

A warning that fires on *"the claim it grounds"* trains every author to ignore it. **That is the W6
scope lesson repeating**: an instrument that cannot distinguish the case it is for from the case it
is not becomes an instrument nobody reads. The exception should be stated as *"and except where the
word is not being used as the technical term"*, with the ordinary-English cluster as its worked
examples.

---

## Found defect — recorded and routed, not repaired (GATE 2 ruling)

**Freight-class. It survives independently of whether the migration proceeds.**

`apparatus/encode-verify.md:21`:

> Ground is the read-only surface an actor inspects in order to act (`core/00`).

`apparatus/closure-principle.md:21`:

> The current treatment defines **ground** as *the read-only surface actors inspect in order to act*…

`core/00-primitives.md`, `term:ground`, **settled**:

> **Ground** — what they are determined against.

**The apparatus attributes an S2 definition to `core/00`, which gives an S1 one, by name, with a
citation.** Two files, one of them citing canon for words canon does not contain.

**Why it is stronger evidence for the split than SR-1's three arrivals**, as ruled at GATE 2: those
three are *observations* that the word carries several objects. This is a *consequence* — the
overload has already produced a false citation across the repository seam, in a document whose whole
purpose is to state a principle correctly. **It is the split's first realised cost, not its fourth
prediction.**

---

## What is asked at this gate

1. **Question 1 — rule the sense.** The audit recommends **S1**, on canon's authority, while
   reporting that this is the **more expensive** disposition by roughly two to one and that the
   price is a data migration in `product-cli`.
2. **Question 1's reframing — rule the remedy.** The audit finds the definition layer itself
   multi-sensed (fifteen settled terms, four senses), which **forecloses the prose-repair remedy**.
   The remedy is definitional.
3. **Question 2 — rule reuse over minting**, and note that `poisoned ground` changes sense without
   changing text under the recommendation.
4. **Question 3 — rule provenance as independent attributes**, and confirm that `DDD-dec-26` gated
   the institutional *value* and not the *axis*.
5. **Question 4 — confirm S5 leaves**, with the correction that 29 of its occurrences are in merged
   papers and it rides with a revision rather than replacing one.
6. **D-4 — note the shape**: W0 blocks everything; W1 can land early alone; W4 has an option canon
   does not, and the audit surfaces it without recommending it.
