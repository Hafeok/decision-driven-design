# Successor items — Paper A's revision (2026-08-30)

Items raised at the Paper A revision and deliberately **not** taken there. Each names the node or
document it lands against and the reason it was not done in-session. **Nothing here is filed canon.**

The session was projection work: the paper may not introduce claims, so every finding it made about
canon has to leave as an item rather than as an edit. That is the whole reason this file exists.

---

## 1. `term:accountability` and `DDD-frame-08` disagree about the relation's arity

**DISCHARGED — pre-transfer session, GATE 1 ruling C (Emil, 2026-09-03).** The two are different
objects: the settled term defines the relation; the claim asserts what a complete instance requires
at design time. `DDD-frame-08`'s statement re-scoped by supersession; the term untouched; the
distinction and its test stated in `core/05` §2 beside the embed; the Bovens lineage filed in the
claim's notes. Record: `meta/sessions/2026-09-02-pre-transfer/gate1-arity.md`.

**Ruled at GATE 3 (Emil): the paper flags, and a canon session gets the issue — both, not either.**

The graph carries two counts of accountability's elements.

- `term:accountability`, **settled**: *"attribution of the determination, a persistent answerable
  party, and a borne consequence"* — three.
- `DDD-frame-08`, **projected**: *"attribution, persistent principal, authority linkage, stake,
  sanction path"* — five.

The mapping, worked in the paper's §7 and reproduced here so the item stands alone:

| `term:accountability` (three, settled) | `DDD-frame-08` (five, projected) | Relation |
|---|---|---|
| attribution of the determination | attribution | same element |
| a persistent answerable party | persistent principal | same element |
| a borne consequence | **stake** and **sanction path** | the five-element version *splits* one into exposure and the mechanism that imposes it |
| — | **authority linkage** | the five-element version *adds* an element the term does not carry |

**The split is defensible; the addition is the question.** Exposure to consequence and a body able
to impose one are separable, and an arrangement can have the first without the second. But a
`projected` claim that adds a fourth kind of thing to a `settled` term is a **supersession question
rather than an elaboration**, and it has been carried as an elaboration since both were filed.

**Why it was not taken here.** A projection may not rule on canon, and this one did not. The paper
reports the disagreement, gives the mapping, and says explicitly that reading the five-element
version as settled because the three-element version is settled would be the status confusion the
review named.

**What a canon session owes.** Either amend `term:accountability` to carry authority linkage — in
which case a settled term moves and every projection pinning it fires W6 — or scope `DDD-frame-08`'s
fifth element as an addition the term deliberately does not make, with the reason stated. **Not
both, and not neither.** The cheap moment is before the repositories are public, because the term is
`settled` and an outside reader will read the count as canonical.

**Bearing on the external review.** Its §10.2 asked for exactly this mapping and asked whether the
five refines or replaces the three. The paper now answers *refines-and-adds*. It does not answer
whether the addition is licensed, and that is this item.

---

## 2. W1's remaining surface, and the counts the charter got wrong

**Reported at GATE 1, corrected in the migration seed on Emil's ruling.**

The session's charter said 88% of W1 lives in the two papers. Against the committed classification:
**88 is the corpus-wide mutable total, and the two manuscripts hold 31 of it — 35%.** The migration
seed is corrected. **W1's remaining surface after this session is 73 of 88**, and it is not in the
papers.

Sixteen of the 31 were deferred here, in three classes, and each class is a rule rather than a
judgement call:

- **generated or hand-carried node tables** (8) — the words are canon's; renaming them forges
  agreement the pin does not have;
- **passages quoting a live claim verbatim** (4) — `DDD-measure-12` and `term:verdict` still read
  `ground distribution` at `v5.12.0`, so a rename would make the note misquote a live node;
- **one filename** (`measure-nonuniform-ground.py`, upstream) and **three occurrences ruled
  ambiguous** between the population sense and the sense naming conditions in the case.

**The pattern worth carrying:** a wave cannot move text it does not own. The three classes above are
all one rule — *the words are canon's* — and a wave's real scope is the prose its own artefacts
author.

---

## 3. `measure-nonuniform-ground.py` and the section it computes now read under two words

The measure note's §5.4 is renamed to *"`P` varied → a non-uniform deployment distribution"*. Its
reproducing asset is `core/assets/measure-nonuniform-ground.py`, upstream and out of a downstream
session's reach. The divergence is flagged in the note itself, in one clause, rather than hidden.

**W2 closes it** when the migration reaches `core/assets/`. Until then the note names the asset by
its real name, which is the only option that keeps the reproduction instruction true.

---

## 4. The measure note has no checkers

Paper A has three — `check-quotations.py`, `check-appendix.py`, and now `check-status.py`. The
measure note has none, and its node table is hand-carried at `v5.7.0` while the paper's is generated
at `v5.12.0`.

**The consequence is live, not theoretical.** This session's sixteen W1 deferrals in that note are
protected by one session's reading and by nothing else, and a later session renaming
`ground distribution` inside its `DDD-measure-12` quotations would break nothing any instrument
would notice. The note is also three releases behind on its own pin.

The three scripts are already ref-parameterised and manuscript-parameterised, so pointing them at
the note is a small session rather than a new instrument.

**Ruled at GATE 4 (Emil): the checkers point at the note before the note's pin next advances**, and
the reason is a rule rather than a preference for this note:

> **An advance without instruments is unobservable, and an unobservable advance is presumed
> discharge at the pin layer.**

That is the same shape as `term:presumed-discharge` one layer up: the artefact recording a verified
advance is identical to the artefact recording an unverified one, because a green run and no run
produce the same file. The two-stage verification this session used — advance the ref, observe the
firing, then re-instrument — requires instruments to observe with. Without them the note's next pin
advance is a bump, and a bump is what the pin discipline exists to prevent.

---

## 5. `README.md`'s "missing parameter" over-claims, and the README is the transfer's front door

**Ruled at GATE 3 (Emil): goes to the freight list, repaired before publication rather than
whenever.**

`README.md:32` reads: *"Decision-Driven Design is what you get when you fill in the actor slot those
results left empty — and discover that supplying the missing parameter changes their predictions."*

That asserts an absence on the same grounds the paper's title asserted one, and the survey does not
support it: the arrangement as a unit of analysis is central to distributed cognition, joint
cognitive systems and systems-theoretic safety. The paper withdrew the claim and the title; the
README still makes it, in the first thing an outside reader sees.

`CHANGELOG.md:303` uses the phrase too and is **deliberately left alone** — a changelog is a
historical record and is not edited retrospectively.

---

## 6. An unverifiable attribution, recorded so it is not rediscovered and believed

While drafting §11, a search result attributed a **"Law of Conservation of Complexity"** —
*"complexity is conserved under transformation and translation"* — to Woods & Hollnagel's *Joint
Cognitive Systems: Patterns* (2006).

**If true it would be load-bearing.** It would give the framework's own conservation principle a
named precedent inside the literature the review says is unengaged, and it would change the Tesler
entry as well.

**It could not be corroborated.** A curated index of the resilience-engineering literature's named
laws attributes the laws of fluency, stretched systems, coordinative entropy and the kludge to
Hoffman & Woods's *Beyond Simon's Slice*, and records no conservation law from *Patterns*. The
volume itself could not be obtained. **Nothing in the paper rests on it.**

Anyone with the book in hand can settle it in a minute, and it is a real finding either way.

---

## 7. The abstract is an uninstrumented surface, and the finding generalises

**Recorded at GATE 5 (Emil): note the general form, because it will recur.**

At this session's close — three checkers green, every validator clean — the abstract still carried
the four-mode enumeration retired at `v5.10`, after §4.1 had been repaired to carry its successor.
Nothing caught it but reading the paper from the top.

> **Instruments cover the surfaces someone thought to instrument.** The abstract is the surface
> nobody thinks to instrument, because it is *prose about the paper* rather than a citation *in* it
> — so it inherits no citation's protection while carrying more of the reader's warrant than any
> single citation does.

**What this item is not.** It is not a proposal for a fourth checker. An instrument that parsed an
abstract for claims it does not cite would be guessing at meaning rather than checking
correspondence — a different kind of tool, and a worse one, since its false negatives would be
indistinguishable from a clean run. The three checkers all verify correspondence against the graph;
that is what makes them trustworthy and it is also what bounds them.

**What it is.** A standing instruction for any session that repairs a projection against a moved
graph: **the abstract and the conclusion are repaired last and read whole**, because they restate
claims without citing them, and a restatement inherits nothing from the citation it paraphrases.
The full manifest entry is at `meta/sessions/2026-08-30-paper-a-revision/manifest.md` §5.3, with the
sibling finding — an unpinned node moving silently — at §5.1.

Whether this belongs in `meta/way-of-working.md` as a projection rule rather than sitting in a
session's successor list is a question for whoever next touches that document. It is not filed here.
