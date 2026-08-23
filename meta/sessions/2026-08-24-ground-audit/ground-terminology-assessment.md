# Assessment — the ground terminology proposal

**Status:** holding. Claude-drafted for Emil's ruling. Nothing filed.
**Summary:** the **diagnosis is right and overdue**; the **ontology split should be taken**; the
**rename to "basis" should not be taken as proposed**, because `basis` already denotes something
else in this framework and the collision recreates the ambiguity the proposal exists to cure.
**One interaction the proposal cannot know:** its §7 relocates institutional ground out of ground
entirely, and Q27 (unfiled) was drafted to give institutional ground a mechanism *as* ground. Those
cannot both stand.

---

## 1. The diagnosis is correct, and this is the third independent arrival

`ground` carries at least five objects in current canon:

| Sense | Where it appears |
|---|---|
| Conditions in the case that matter | `DDD-ground-05` (constitutive priority), the axis registry, "declared ground" |
| Representations the arrangement holds | "accessible ground", the ledger, `DDD-agent-01`'s basis loss |
| Representations delivered at the act | "ground standing at that tick", "reading ground", the streaming result |
| Institutional rules and standards | "institutional ground", Q27's trust material |
| The population over which demand is measured | the measure's `P`, "ground distribution" |

The last is the least defensible: `P` is a *population*, not a case's material, and the measure note
already treats it as a separate parameter in everything but its name.

**Three independent arrivals now converge on the split:**

1. **The delivery work (v5.5.0)** — filing is not encoding; a decision can exist and not reach the
   act. That is the available/delivered distinction, already ratified, expressed on the *decision*
   side and never on the ground side.
2. **The Paper A review §6** — `G*` (relevant world facts) versus `G_A` (accessible and delivered),
   proposed as a strengthening of the floor and ground-access hypotheses.
3. **This proposal**, from the terminology side.

That is the escape-reconciliation pattern repeating: three routes, one finding. The framework's own
convergence rule says the split is real.

**And the split has framework-native force**, not merely stylistic force: a basis gap and a missing
world-fact have different remedies (deliver it versus discover it); a corrupted basis and an absent
one have different detection methods; a delivery failure at the interface reads as an absence in the
world if the vocabulary cannot separate them. Those are the failure modes the framework exists to
distinguish, and the current word blurs them.

---

## 2. Why "basis" is the wrong replacement word

The proposal's strongest argument for `basis` is that it aligns with the existing `basedOn`
relation. **That alignment is the objection, not the support.**

`basedOn` in this framework denotes **which claims and decisions a node rests on** — graph
provenance among governance objects. "Basis pins" pin *claims*. "Basis loss" is `DDD-agent-01`'s
name for a node's supporting claims becoming unreachable. None of that is about a case's facts.

Adopting `decision basis` for the representational object would mean:

- `basis` denotes both *the claims a decision rests on* and *the facts an arrangement holds*;
- "basis loss" would mean either an agent losing its supporting decisions or an arrangement losing
  its case information;
- `basedOn:` fields and "basis gap" would sit in the same registry meaning unrelated things.

That is precisely the failure the proposal diagnoses in `ground`, moved onto a word that is already
load-bearing. **A migration that creates the defect it repairs is not worth its cost.**

Secondary: `basis` also has an established mathematical meaning, and the framework is already
carrying an information-theoretic register.

---

## 3. What to do instead

**Take the split. Choose different names. Keep `ground` for exactly one sense.**

Recommended assignment, for Emil's ruling — the reasoning is that `ground`'s strongest and most
canonical uses are world-facing (the registry declares dimensions of variation; `DDD-ground-05` says
declaring them precedes determining over them):

| Object | Recommended name | Note |
|---|---|---|
| Conditions in the case whose variation moves the outcome past τ | **ground** (retained) | The registry is a registry of *determinables* (Johnson, v5.7.0) — the framework already has the formal word for this sense's structure |
| What the arrangement holds | **the record** / held representations | Deliberately not `basis` |
| What reaches the act | **the act's reading** / delivered representations | Delivery vocabulary already exists (v5.5.0) — reuse it rather than mint beside it |
| A relevant condition inadequately represented at the act | **reading gap** | Distinguishes cleanly from a world-fact nobody could have |
| Present but false, stale, or manipulated | **corrupted reading** | "Poisoned ground" survives as the adversarial special case |
| The population | **deployment distribution** | Adopt as proposed; the measure's `P` is already this |
| Institutional rules | see §4 | Not a naming question |

**These names are proposals, not recommendations I would defend to the death.** The load-bearing
recommendations are: (a) split; (b) do not use `basis`; (c) whichever sense keeps `ground`, say so
once and enforce it.

**One cheap instrument the proposal supplies and should be kept verbatim:** an unqualified use of
the retained word becomes a drafting warning, except in quotations and historical notes. That is the
`term:maturation` shadow lesson applied to prose.

---

## 4. The interaction the proposal cannot see: §7 versus Q27

The proposal's §7 says institutional rules belong in the **acceptance relation** or among
**standing commitments**, and that calling both the rule and the case record "ground" collapses the
criterion into the material judged. That is a sharp and probably correct observation.

**But Q27 (trust, drafted, unfiled) does the opposite:** it fills institutional ground's empty
provenance slot by treating a trusted source's output *as ground*, with trust as a filed decision
converting occasioned assurance into standing assurance. Under the proposal, most of what Q27 calls
institutional ground would be reclassified out of ground entirely.

Both can be partially right, and the reconciliation is probably: **the rule's normative force is in
the acceptance relation; the arrangement's representation of the rule is a reading; the trust
decision governs whether that representation may be relied on without independent verification.**
Three objects, currently one.

**This must be settled before Q27 files.** Filing Q27's mechanism onto a category the terminology
work is about to dissolve would mean filing twice.

---

## 5. What the split does not fix — and the proposal says so

The proposal is honest that renaming does not repair the decoder problem: even with a clean
vocabulary, `H(V | delivered representations) = 0` when the representation contains the state,
without the arrangement possessing any rule to recover `V`. That is the Paper A review's F-B, and
the repair is arrangement-relative admissibility — **research, not terminology**.

Worth stating plainly so no one expects the migration to close it: the split makes the defect
*easier to state*, which is real progress and not a fix.

---

## 6. Cost, and the C-1 precedent

A retained-word split is much cheaper than a full retirement, but it is still large: the term
registry, every core document, claim statements citing ground, the axis registry, the G-track PRD
(titled *ground as ontology*), the primer's planned §4, and two merged papers.

**The C-1 carve precedent applies directly.** That was deferred whole not because the file count was
frightening but because three design rulings sat inside it. The same is true here — at minimum:
which sense keeps the word; how the held/delivered pair names itself against the existing delivery
vocabulary; whether provenance is an enumeration or several independent attributes (the proposal
argues the latter and is probably right).

**So: plan before cutting, and the plan is a deliverable.** A session that produces the audit —
every occurrence of `ground` classified by sense, with counts per sense and per artefact — is worth
running *even if the migration then defers*, because the audit is what makes the design rulings
answerable.

---

## 7. Sequencing, against everything else pending

Four registry-or-vocabulary changes are now queued at once. Ordered by dependency and by the
publication gate:

| # | Change | Why here |
|---|---|---|
| 1 | **Discharge partition repair** (Paper A review F-C) | `DDD-frame-15` is days old; smallest and cheapest now |
| 2 | **`DDD-measure-06` re-scope** (F-A) | One node; canon is currently contradicted by its own projection |
| 3 | **Ground audit** (this proposal) | Produces the design rulings; cheap; blocks nothing |
| 4 | **Status/kind separation** (Paper A review §7) | Registry-wide; **must precede publication** |
| 5 | **Ground migration**, on the audit's rulings | **Must precede publication and the primer** — renaming a primitive after either is far worse |
| 6 | **Primer** | Written once, in the settled vocabulary |
| 7 | Q27 wave, with §4's reconciliation ruled | After the vocabulary settles |
| 8 | Paper A revision; the measure's decoder repair | Research and prose, unblocked by the above |

**The primer moves behind the migration.** Writing it in the current vocabulary and then migrating
would mean writing it twice, and the primer is the artefact most likely to be read by people who
will never read canon — so it should be the first thing written in the settled words, not the last
thing converted to them.
