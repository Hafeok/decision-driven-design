# Floor-lineage successor items

Booked as the session ran, **none begun**, per the do-not-bundle rule.

---

## 1. The competing novelty claims *(deferred whole — routed to a paper session)*

Full record: **`f3-deferral.md`**, in this directory. Three novelty statements, two of which
genuinely compete; the minimal reconciliation drafted and deliberately not taken, because choosing
between them is a ranking of the framework's contributions rather than a prose repair.

**Inherited by** the next session that states what the framework's primary contribution *is* — the
Paper A revision or the method paper, whichever comes first. A paper cannot avoid the question a
repository can defer.

---

## 2. Should the floor's ancestry be a required citation, or only a register entry? *(governance)*

**The question.** `meta/lineage-and-limits.md` §6 is headed *"Required citations (add to every
artifact that uses the corresponding claim)"*. It carries the row **"The floor | Polanyi; Collins"**,
and that row is what warranted F-4's repair to Paper A this session. §1.16 now adds five more
ancestors for the same phenomenon — Wittgenstein, Hayek, Bainbridge, Dreyfus, Suchman — and **no row
was added for any of them.**

**Why the non-filing was correct here, and why it is still open.** Adding six rows would obligate
Paper A and every future projection **retroactively**, at once, with no examination of what the
obligation costs or where it stops. That is a governance change wearing a bibliography's clothes,
and it needs its own ruling with the obligation's scope examined — Emil's words at GATE 2. The
ancestry is recorded; the citation duty is not extended.

**What the inheriting session must decide.** Not "should we cite our ancestors" — the register
already does. The question is narrower and harder: **what makes a lineage entry rise to a §6 row?**
§6's existing rows are all sources a claim *rests on* — Tesler for conservation, Rice for the
zero-floor limits, Shannon for the measure. The §1.16 ancestors are sources the framework
*differs from*. Whether a contrast-ancestor generates a standing citation duty is the actual
question, and answering it may need §6 split into two registers rather than extended.

**Do not** resolve this by adding the rows quietly. The non-filing is stated inside §1.16 as a
decision, and reversing a decision is a ruling.

---

## 3. `term:floor`'s promotion — the pattern, not the instance *(observation, unscoped)*

F-1 found that `term:floor`'s `canonical_md` carried the *claim about* the floor and never a
definition of it, while both sibling terms established in the same document define. That instance is
fixed. **Whether it is the only one is not known** — no sweep was run, and running one was outside
this session's booking.

The check is cheap and mechanical: for each term in `core/graph/terms.yaml` with a `canonical_md`,
does the text define the term, or assert something about it? A registry whose entries assert are
still useful, but they cannot be embedded as a definition, and a document that embeds one will
reproduce F-1's defect. `term:path-degeneracy` is the obvious next candidate to look at — *"Where the
floor is zero, path-degeneracy makes it robustly zero…"* is a claim, not a definition.

Unscoped deliberately: whether this is a validator rule, a one-off audit, or nothing at all is open.

---

## 4. Wittgenstein §201 — the print check *(a named debt, discharged by one reading)*

`meta/lineage-and-limits.md` §1.16's Wittgenstein entry is **flagged-verified** and says so in its own
body: the wording is the Anscombe rendering as reproduced in the *SEP* Wittgenstein entry §3.5, whose
bibliography lists both Anscombe (Blackwell, 1953) and the revised fourth edition (Hacker & Schulte,
Wiley-Blackwell, 2009) and attributes the quotation to neither; Kripke (1982) quotes the same
wording; **no printed copy of either edition was consulted, and the fourth edition's revision of
Anscombe's wording has not been compared.**

**Discharged by:** anyone with either printed edition to hand. Confirm the wording, name the
translation, and if the fourth edition differs, record both renderings. The entry is already written
to receive the answer.

---

## 5. Freight, added to an existing item rather than booked here

Not a new item — recorded so the trail is complete. Paper A successor item 1 (*"Quotation fidelity as
a standing requirement"*, freight) gained one finding from this session at Emil's GATE 2 ruling:
**verbatim is not complete.** `check-quotations.py`'s test is `contains(canon, quoted)`, so it
verifies faithfulness and not disclosure; a partial-quote disclosure rule is a separate predicate
over the same input. The instance was created by this session — F-1 lengthened `term:floor`'s
canonical text, which turned Paper A `§6.1`'s quotation into an untagged partial overnight, with the
checker still passing it and correctly so. Paper A successor item 4 likewise gained `DDD-dec-29` as a
second instance of a `[PROPOSED]` banner filed before the merge it records.
