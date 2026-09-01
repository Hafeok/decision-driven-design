# GATE 2 — the twenty precedents

**Status: draft-pending-ruling. This is the session's largest ruling and the reason it exists.**
Nothing is edited by this gate: every proposed re-expression below is a proposal, executed at G3/G4
only under the ruling.

**Drawn from the 185-row bare ledger** Gate 1 ruled governing (`g1-head-ledger.json`), selected for
coverage over every distinct sentence shape in it, hardest first, with at least one S2 and one S3
that the delivery vocabulary must now name. Sites are cited by content, never by line. The target
vocabulary is Q2's, ratified at the audit's Gate 3 and reused, never minted (SR-3): **available
ground** (S2 — what the arrangement holds), **delivered ground**, act-indexed (S3 — what reaches
the act), **undelivered ground** (the failure). S1 keeps the bare word (SR-1); S3 is verbs applied
to the S1 object (SR-2), which is why most precedents below rule *no edit* — a no-edit ruling is
still a ruling, and it is the citable kind.

Each precedent: the sentence, the proposal, the pattern it establishes, and what inherits it.
**A later re-expression citing no precedent is a new ruling and stops at a gate.**

---

## P-01 — pinned text moves only behind a stated prediction

**Sites.** `DDD-frame-17` (pinned, `content_hash` present) and `DDD-agent-01` (pinned, hashed) —
the only pinned upstream nodes carrying bare rows.

**The facts that decide it.** The pin digest covers `statement`, `region` and `canonical_md`
only. `DDD-frame-17`'s *statement* already carries the settled act-indexed form — *"the ground at
the act determines the resolution"* — its bare rows sit in the **falsifier**, which reads *"the
standing configuration and the ground together determine the resolution"*. `DDD-agent-01`'s bare
row sits in the **statement** itself.

**Proposals.**
- `DDD-frame-17` falsifier: *"…whether the standing configuration and the ground together
  determine the resolution"* → *"…whether the standing configuration and **the ground at the
  act** together determine the resolution"*. Aligns the falsifier to its own statement's form.
  **Fires nothing** — the falsifier is not hashed — and is still named at the gate before it runs.
- `DDD-agent-01` statement: *"context decay, compaction, and distractors remove claim nodes from
  the agent's ground"* — **no edit.** *Remove from* is a store operation; the sentence names what
  happens to the held ground (SR-2). This also avoids an unpredicted eighth W6. The statement's
  *"Grounding the agent in a persistent external claim graph"* is the verb lexeme, not the noun —
  recorded as a reclassification candidate (S2 → U-ordinary), not silently changed.

**Pattern established.** *An edit inside hashed text is a firing, and is predicted by id and hash
before the operation (the `DDD-dec-29` pattern); an edit in unhashed fields of a pinned node fires
nothing but is still named at its gate. No edit is ever chosen, or avoided, to make a firing
prediction come true.*
**Inherits:** every G3/G4 row inside `core/claims/` and `core/graph/terms.yaml`.

## P-02 — anaphora inherits its antecedent's qualification

**Site.** `term:poisoned-ground`, settled canonical text (embedded in `core/00-primitives.md`,
quoted in `meta/reference-audit-2026-08-07.md`): *"ground that is present but false: the substrate
a determination reads has been corrupted, so a correct determiner resolves wrongly with full
authority. The logic is sound; **the ground** is the attack surface."*

**Proposal.** **No edit.** The final clause's bare *the ground* is anaphoric on a head that has
already named the state twice (*present but false*; *the substrate a determination reads*).
Qualifying the anaphor would re-say what the passage just said.

**Pattern established.** *A bare occurrence whose referent is established by a qualified
antecedent, within one passage and an unbroken referent, needs no edit. The state is named once,
at the head; anaphora inherit.* Scope bound: same passage or tightly-coupled document opening; a
new section starts a new obligation.
**Inherits:** the aphorism family — *"the attack surface of any actor is its ground, not its
logic"* (`apparatus/adversarial-ground.md`, whose opening defines the state before the aphorism)
and its `README.md`/`apparatus/README.md` echoes; `core/11`'s failure-table rows after its head.
Note: `term:poisoned-ground` still gains its one state-naming sentence at G3 (the seed's item 2) —
that is an addition beside this clause, not an edit of it.

## P-03 — role-position uses stay bare

**Sites.** `core/11-the-floor-mechanism.md`: *"the closure principle (**an actor's own prior
output is not ground**)"*, with its echoes in `meta/consolidated-state.md`,
`meta/reference-audit-2026-08-07.md`, both READMEs. Affirmative twins: *"what makes an
institution's statement **usable as ground**, and what makes it fail"* (`papers/paper-a`);
*"the verdict is new **ground** about the verdict function itself"* (`core/14-maturation.md`,
downstream); *"as if it were ground"* (`apparatus/the-skill-floor.md`).

**Proposal.** **No edit, as a class.** These sentences quantify over admission to the role of
ground — what may serve as ground at all. A delivery qualifier would narrow them falsely:
*"own output is not **available** ground"* would licence it as delivered ground, which is exactly
what the closure principle forbids.

**Pattern established.** *Where the sentence asserts or denies that something can serve as
ground — is/is not ground, usable as ground, becomes ground — the bare word names the role and
stays. Qualification narrows a universal.*

## P-04 — the capacity entry: act-location already names delivery

**Site.** `term:capacity`, settled, **pinned, hashed — one of the seed's seven predicted W6**:
*"**hold capacity** — the bits of ground it can have **in context at once**"*; prose twin in
`core/11`: *"The substrate it **reads**."*

**Proposal.** **No edit to this clause.** *In context at once* is the act-location; it names
delivery by position. Writing *delivered ground* beside it would double-name the state.

**Pattern established.** *An act-locating phrase — in context, at the act, this act's, at
act-time — is a delivery qualifier already. Nothing is added beside it.*
**Consequence, recorded now:** if G3 finds no other clause of `term:capacity` moving, the seed's
predicted firing on it does not occur, and that divergence is **recorded, never manufactured** —
editing settled text to make a firing prediction true is the same failure Gate 1's ruling closed
for counts.
**Inherits:** *"ground available at the act"*, *"the ground at the act are both given"*, and every
row my instrument or the seed's counted bare only because the qualifier is positional.

## P-05 — the overflow entry: parallel clauses complete each other *(S3 edit)*

**Site.** `term:overflow`, settled, **unpinned**: *"**Hold-overflow** — the decision's governing
ground does not fit. **Resolve-overflow** — the ground fits and is held, but the bits that must be
jointly resolved exceed resolve capacity."*

**Proposal.** *"Hold-overflow — the decision's governing ground **exceeds hold capacity**."* The
entry's own second clause supplies the form (*exceed resolve capacity*); the repair completes the
parallel and names what *does not fit* means. The second clause's *"fits and is held"* already
qualifies and does not move. Fires nothing.

**Pattern established.** *Where a definition's sibling clause already names the state in the
entry's own vocabulary, the bare clause is completed to the parallel — reuse inside the entry
before reaching for the delivery words.*

## P-06 — negated-capability verbs already qualify

**Sites.** `papers/paper-a`: *"an act whose acceptance depends on **ground the arrangement cannot
reach** has a floor above zero"* (twice); `meta/lineage-and-limits.md` (upstream): *"ground that
an arrangement cannot reach is ground its predicate cannot evaluate over"*.

**Proposal.** **No edit.** *Cannot reach* names unavailability more precisely than *unavailable*
would — it says whose failure it is.

**Pattern established.** *A capability verb under negation — cannot reach, does not control, do
not own, never controlled — is a full qualifier. This is also the instrument's known false-bare
class (precision 9/12), recorded at Gate 1; rows bare only by lexicon gap cite this precedent and
close with no edit.*
**Inherits:** the control/ownership family across `apparatus/` (*"ground you do not control"*,
*"ground the author did not control"*, *"ground you do not own"*, *"the price of the ground being
someone else's"*).

## P-07 — consumption verbs already qualify

**Sites.** `core/09-the-measure.md`: *"a mechanism that **computes** the verdict **from
admissible ground**"*; `DDD-measure-15` (unpinned) same form; `papers/measure-note` twin without
the adjective: *"a mechanism that computes the verdict from ground"*.

**Proposal.** **No edit, including the twin.** *Computes from* names consumption; *admissible*
names the filter where present, and its absence in the note's compressed restatement does not
leave the state open — the verb carries it.

**Pattern established.** *Verbs of consumption and production — computes from, derives from,
reads, re-derives, replays over, consults — qualify their object. The sentence already says what
is done to the ground; SR-2 verbatim.*

## P-08 — index positions stay bare

**Sites.** `core/10-cost.md`: *"the admission test (`00` §4), applied **per ground type**"* (and
its `core/15`, asset and holding-note echoes); `projections/tracks/01-determination.md`: *"no
axis, **no ground**, no principal, and total commitment"*.

**Proposal.** **No edit.** *Per ground type* indexes over kinds of the S1 object; the tuple
enumeration cites the coordinate by name. Neither predicates a state.

**Pattern established.** *Type-indexing and coordinate citation range over the S1 object and keep
the bare word — the same reason the ⟨task, ground, …⟩ tuple keeps it.*

## P-09 — comparative endowments name availability; per-act reach names delivery *(S2 edit)*

**Site.** `projections/tracks/01-determination.md`, the arrangement comparison: *"The program's
has the **narrowest ground** and a perfect record."* … *"**the program's arrangement is the most
tightly bounded and has the least ground**, while **the engineer's has the most ground and the
least record**"*. (The passage's neighbours already qualify: *"richest ground channels"*,
*"inherits its ground from whatever the pipeline retrieved"*, *"you can give the program more
ground"*.)

**Proposal.** Name the state once per sentence, at the head of each comparison:
*"The program's has the narrowest ground **available to it** and a perfect record"*; *"…has the
least ground **available to it**, while the engineer's has the most ground available and the
least record"*. The *give/feed/inherits/retrieved* sentences do not move (P-07).

**Pattern established.** *Arrangement-level comparisons of endowment take **available** (what the
arrangement holds); per-act statements take **delivered**. These rows are S3-classified but
availability-named — the boundary call is made here, once, for the ruling: classification answers
"which sense", the vocabulary answers "which state the sentence asserts", and a comparative
asserts holding, not arrival.*

## P-10 — existence denials of evidence name availability *(S2 edit)*

**Site.** `projections/tracks/01-determination.md`, the ground-cited table row: *"support's
argument that older transcripts resolve repeat cases: **asserted, never measured — no ground
exists for it**"*.

**Proposal.** *"asserted, never measured — **no ground is available for it**"*. *Exists* reads as
a world-denial (S1) and is false as one — the facts exist, unmeasured; what is missing is held
evidence.

**Pattern established.** *Where prose denies the existence of ground and means the arrangement
holds none, the denial is re-said with **available** — the one case where bare wording does not
merely omit the state but asserts the wrong sense.*

## P-11 — relational compounds keep the word

**Sites.** `apparatus/tool-contract.md`: *"Capability without **ground relation** is motion
without traction"*, *"**Ground relation** — per response, not per tool"*; `papers/paper-a` and
`reviewer-brief`: *"**ground access**"* in the H1 bundle.

**Proposal.** **No edit.** The compound's head names the relation (*relation*, *access*); the
modifier slot cites the object.

**Pattern established.** *A compound whose head noun names a relation or operation over ground is
verb-shaped in SR-2's sense; the modifier stays bare.*

## P-12 — headings and table heads inherit their body

**Sites.** *"**H2 — ground and judgment dependence**"* (`core/14-indexed-determination.md`,
`README.md`, cited in `DDD-frame-07`) — the body's first predication is *"as ground becomes
unavailable"*; `core/11`'s failure table: header *"| Cause | The ground is… |"* with cells
*false · missing · stale*.

**Proposal.** **No edit.** A heading is a handle; the obligation to name the state belongs to the
first predicating sentence under it, which here already discharges it. The table head is the same
shape rotated: the cells carry the predicates.

**Pattern established.** *Headings, hypothesis titles and table heads stay bare where the body's
first predication names the state; the heading cites its body as its antecedent (P-02 at
document scale). A heading over a body that never names the state is bare prose and falls back to
the edit precedents.*
**Inherits:** *"### Ground exporters"*, *"## 1. Ground first"*, *"### 2.4 Ground provenance"*.

## P-13 — filed decisions and recorded rulings are history

**Sites.** `DDD-dec-26` (upstream): *"## Ground provenance — ruled ineligible, not deferred by
preference"*; `DDD-dec-27` twins; `DDD-cost-05` **notes**, which record freight item F-2's
proposal *as formed*: *"context is simultaneously the ground, the retrieved governance and the
working space"*.

**Proposal.** **No edit, ever, in this class.** A decision file records what was ruled in the
words it was ruled in; a notes field that says *"recorded here so the successor session inherits
it formed"* is a record embedded in a claim. Supersession, never rewriting — the predecessor's
retired-mode ruling at its GATE 2 is the model, and Gate 1's ruling on the 134 meta additions is
the same principle one layer up.

**Pattern established.** *Bare rows inside filed decisions, and inside notes that record a ruling
or a proposal as-made, are historical record: never re-expressed. If the recorded wording later
misleads, the remedy is a new sentence beside it, not a changed one.*

## P-14 — provenance adjectives are the attribute vocabulary, not rivals

**Sites.** `applications/sdlc/production-as-ground.md`: *"practices that convert **substitute
ground** into **real ground** should outperform…"* (and its three siblings);
`meta/holding-note-ground-axes-rev18.md` (G5 surface): *"a CV is **unsupported ground**; a
licence is **trusted ground** with a printed date"*.

**Proposal.** **No edit.** *Substitute/real*, *trusted/unsupported*, *yours/someone else's* are
provenance attributes doing exactly what SR-4 says provenance does — independent attributes, not
an enumeration and not a fifth sense. They compose with the delivery words; they do not compete
with them.

**Pattern established.** *An adjective naming provenance or ownership is a qualifier in good
standing. Re-expression never replaces it with a delivery word, and never stacks one on top
without a reason the sentence states.*

## P-15 — proposed-term citations are mentions

**Site.** `meta/holding-note-ground-axes-rev18.md` (G5 surface), Q30: *"**Proposed canon term:
ground registry**, with the software layer as one consumer"* and its echoes.

**Proposal.** **No edit.** The occurrence cites a proposal by its proposed name. Renaming it in
the filing would mint vocabulary (SR-3) inside a record (P-13). If the proposal is ever taken up,
the naming happens there, against the registry, with the collision check.

**Pattern established.** *A proposed or foreign term cited by name is a mention, whatever the
classifier says; mentions are never re-expressed.*

## P-16 — code surfaces follow prose rules; identifiers never move

**Sites.** `core/assets/recon-cadence-demo.py` (downstream): *"# ground corruption rate per day
(drift / adversarial)"*; `core/assets/measure-routing-example.py`: *"ground type
"code-synthesis""*, *"# visual ground -> excluded"*.

**Proposal.** **No edit.** The comments name their object beside the computation that defines it;
the strings are data. Identifier renames are SR-6's and W4's territory, not a prose wave's.

**Pattern established.** *A comment is prose and takes the prose precedents; a string or
identifier is data and takes none. An asset edit that changes no computation must leave the
asset's output byte-identical — verified by re-run, per the repo's executable-evidence rule.*

## P-17 — verb-headed compounds are SR-2 verbatim

**Sites.** `apparatus/tool-surfaces.md`: *"### Ground exporters — return unstructured or
unbounded content…"*, *"**Bounds the ground.**"*, *"a **ground-scoping** primitive"*;
`downstream:CHANGELOG.md`'s *"ground-first tool contract"*.

**Proposal.** **No edit.** *Exporter, scoping, bounding, -first*: each head names an operation on
the object. This is the compound form of P-07 and the reason `poisoned ground` costs one sentence
rather than sixty-six edits.

**Pattern established.** *A compound headed by an operation word is already verb-shaped; the
migration leaves it and, where the compound is load-bearing enough to be a term, the registry
names its state once (the `term:poisoned-ground` model).*

## P-18 — bare apposition takes the delivery word *(S3 edit)*

**Site.** `apparatus/prefix-stability.md`: *"In a typical prefix, stable content **is** long
(**ground**, a large corpus of settled decisions) and volatile content is short (the task)."*

**Proposal.** *"(**delivered ground**, a large corpus of settled decisions)"*. The parenthesis
has no verb to lean on and the passage is precisely about what reaches the actor's context — the
delivery word is the cheapest honest qualifier. The companion ordering notation *"(ground →
decisions → task)"* is notation and does not move (P-16).

**Pattern established.** *A bare occurrence in apposition or parenthesis — no verb, no adjective,
no antecedent in reach — is the residual class that takes the Q2 word outright: available for
holdings, delivered for what reaches the act. This is the default when no other precedent
applies, and it is deliberately last-resort: the corpus prefers verbs.*

## P-19 — locational predication stays bare

**Sites.** `core/03-the-floor.md`: *"Polanyi in tacit application, **Hayek in the dispersion of
ground**, Bainbridge in what automation leaves"*; `meta/lineage-and-limits.md` (upstream): *"the
task's irreducibility is about **where the ground is**, not about whether an answer can be
stated"*.

**Proposal.** **No edit.** These sentences predicate location and dispersion of the object across
the world and across actors — the fact at issue *is* the position. A delivery word would collapse
the point into one arrangement's viewpoint.

**Pattern established.** *Predications about where ground sits — dispersion, location,
concentration — are about the S1 object's situation and stay bare, whatever store sense the
classifier assigned the row.*

## P-20 — the judgment gloss is the shape's named instance *(Emil's Gate 1 directive)*

**Site.** `README.md` (upstream), the delivery table's judgment row: *"**Judgment** — an actor
reading ground, **with an accountable party named** — during the act — paid per run"*. The
delivered/judgment/default trio that carried this shape in Paper A was cut, not moved, by the
revision; this is the shape's clearest surviving instance, selected deliberately so the shape
does not go unruled.

**Proposal.** **No edit** — and the row is *named*: **the canonical instance of the
verb-qualified S3 shape**. *An actor reading ground* is what SR-2 means; the accountable-party
clause is `term:judgment`'s settled condition riding with it.

**Pattern established.** *The qualified population (416 rows) has a standing citation: a row
whose verb names the act in this shape needs no edit and cites P-20. If the trio's sentence is
ever restored to a paper, it is authored against this row and `term:judgment`, not reconstructed
from memory.*

---

## The set, summarised

| | Ruling | Class |
|---|---|---|
| P-01 | predict-then-edit; falsifier aligned, statement untouched | pin governance |
| P-02 | no edit — anaphora inherit | scope |
| P-03 | no edit — role-position | semantics |
| P-04 | no edit — act-location names delivery; firing divergence recorded if it comes | registry |
| P-05 | **edit** — parallel completion, `exceeds hold capacity` | registry, S3 |
| P-06 | no edit — negated capability verbs | instrument false-bare |
| P-07 | no edit — consumption verbs | SR-2 |
| P-08 | no edit — index positions | semantics |
| P-09 | **edit** — `available to it` on comparatives | S2, boundary call |
| P-10 | **edit** — `no ground is available for it` | S2, wrong-sense repair |
| P-11 | no edit — relational compounds | SR-2 |
| P-12 | no edit — headings inherit body | scope |
| P-13 | no edit ever — decisions and recorded rulings | history |
| P-14 | no edit — provenance adjectives | SR-4 |
| P-15 | no edit — proposed-term mentions | SR-3 |
| P-16 | no edit — code comments and data | SR-6 / W4 seam |
| P-17 | no edit — verb-headed compounds | SR-2 |
| P-18 | **edit** — apposition takes the delivery word; the last-resort default | S3 |
| P-19 | no edit — locational predication | semantics |
| P-20 | no edit — the named instance of the qualified shape | the trio's replacement |

**Five edits, fifteen no-edit rulings.** That ratio is SR-2 measured a third way: the audit
predicted it, Gate 4 of the predecessor priced it, and ruling the twenty hardest instances
confirms it — canon's habit really is to name what is done to the ground, and the migration's
body shrinks again once anaphora (P-02), headings (P-12) and the instrument's false-bare class
(P-06) are citable.

**What G4 does with this.** Every one of the remaining bare rows cites exactly one precedent, in
a committed citation map; a row no precedent fits stops at a gate as a new ruling. The map is
counted at G4's midpoint hold, per SR-7 — no inheritance estimates are offered here, deliberately.

**What this gate asks.**
1. The twenty, individually — each is a ruling, and P-09's available/delivered boundary call and
   P-13's notes-are-history extension are the two most consequential.
2. P-01's governance: falsifier aligned without a firing; `DDD-agent-01` untouched. If Emil
   prefers the agent-01 statement edited, it is an **eighth W6, predicted by id and hash before
   the operation** — the precedent covers both outcomes; the draft recommends no edit.
3. P-04's recorded consequence: a predicted firing that G3 may find unearned is a divergence to
   record, not to manufacture.
4. Whether P-18's last-resort default is ratified as the fallback for rows no other precedent
   fits, or whether such rows must each stop at a gate regardless.

**Nothing edited. Nothing merged. Holding at GATE 2.**
