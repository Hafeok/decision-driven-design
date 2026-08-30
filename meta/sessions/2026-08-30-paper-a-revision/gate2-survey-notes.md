# GATE 2 — the survey's reading record

**Status: draft-pending-ruling.** The record of what was read, how each locator was verified, and
what the reading did and did not support. Filed separately from the drafted section because the
survey's warrant is the reading, and a reader who wants to check the section should not have to
reconstruct the reading from it.

**The standard, from Emil's Gate 1 ruling and the Hayek precedent:** every locator verified
directly, or flagged unverified in its own entry with the reason. The Tesler entry is the pattern
for a source with no primary publication.

---

## 1. How each locator was verified

Two registries were used, both authoritative and both independent of the review: **Crossref**'s
DOI records (`api.crossref.org`) and **Open Library**'s ISBN records. Publisher pages
(`mitpress.mit.edu`, `direct.mit.edu`, `taylorfrancis.com`, `routledge.com`, `dl.acm.org`) refused
automated requests, so none of them is the basis of any entry.

| Work | Locator, as verified | Verified against |
|---|---|---|
| Hutchins | *Cognition in the Wild*, MIT Press 1995, ISBN 9780262082310; pb Bradford Books 1996, ISBN 9780262581462 | Open Library, both ISBNs |
| Hollnagel & Woods | *Joint Cognitive Systems: Foundations of Cognitive Systems Engineering*, CRC Press 2005, ISBN 0-8493-2821-7, doi:10.1201/9781420038194 | Crossref **and** Open Library |
| Woods & Hollnagel | *Joint Cognitive Systems: Patterns in Cognitive Systems Engineering*, CRC Press 2006, ISBN 0-8493-3933-2, doi:10.1201/9781420005684 | Crossref **and** Open Library |
| Hollnagel & Woods (1983) | *International Journal of Man-Machine Studies* 18(6):583–600; reprinted *IJHCS* 51(2):339–356, 1999, doi:10.1006/ijhc.1982.0313 | NCBI E-utilities, PMID 11543350 |
| Leveson | *Engineering a Safer World*, MIT Press 2011, ISBN 9780262016629; pb 2017, ISBN 9780262533690; open-access edition | Open Library, both ISBNs |
| Horvitz | CHI '99, pp. 159–166, doi:10.1145/302979.303030 | Crossref, **and the full text read** |
| Bovens | *European Law Journal* 13(4):447–468, 2007, doi:10.1111/j.1468-0386.2007.00378.x | Crossref, **and the full text read** |
| Matthias | *Ethics and Information Technology* 6(3):175–183, 2004, doi:10.1007/s10676-004-3422-1 | Crossref, **and the full text read** |
| Santoni de Sio & van den Hoven | *Frontiers in Robotics and AI* 5:15, 2018, doi:10.3389/frobt.2018.00015 | Crossref |

---

## 2. Two catches, and they are the reason the rule exists

### 2.1 The review's own Hollnagel-and-Woods locator is the wrong volume

The review cites `10.1201/9781420005684` and names it *"Woods and Hollnagel, Joint Cognitive
Systems"*. Crossref resolves that DOI to:

> **Woods, David D.; Hollnagel, Erik. *Joint Cognitive Systems: Patterns in Cognitive Systems
> Engineering.* CRC Press, 27 March 2006.**

The volume the review's **prose** is about — the joint cognitive system stated as a unit of
analysis — is the sibling:

> **Hollnagel, Erik; Woods, David D. *Joint Cognitive Systems: Foundations of Cognitive Systems
> Engineering.* CRC Press, 28 February 2005.** doi:10.1201/9781420038194.

Two books, one year apart, sharing a main title, with the author order reversed between them. A
citation database would have propagated the error silently, which is exactly what the Hayek
facsimile check was instituted to prevent. **Both volumes are cited in the drafted section**, since
both are on point. Per Emil's Gate 1 ruling, the error is recorded for the response-to-review
rather than quietly corrected: telling the reviewer their own citation was reversed is more useful
to them than fixing it behind their back.

### 2.2 A conservation law attributed to *Patterns* — could not be corroborated, and is not used

A search result attributed a **"Law of Conservation of Complexity"** — *"complexity is conserved
under transformation and translation"* — to Woods & Hollnagel's *Patterns*. If true it would be
directly load-bearing: it would give the framework's own conservation principle a named precedent
inside the literature the review says is unengaged, and it would change the Tesler entry as well.

**It could not be corroborated.** A curated index of the resilience-engineering literature's named
laws attributes the *law of fluency*, the *law of stretched systems*, the *law of coordinative
entropy* and the *law of the kludge* to Hoffman & Woods's *Beyond Simon's Slice*, and records no
conservation law from *Patterns* at all. No primary text was obtained.

**Nothing in the drafted section rests on it.** It is written down here so that a later session does
not rediscover the same unverified attribution and believe it the second time. If someone with the
book in hand can confirm or refute it, that is a real finding either way, and it is booked as a
successor item rather than a footnote.

---

## 3. What was read, and at what grade

The distinction matters and the section is written to respect it. **Locator verified** is not
**text read**, and a difference claim is only as good as the reading behind it.

| Work | Grade of reading |
|---|---|
| Horvitz 1999 | **primary, in full** — all twelve critical factors read verbatim from the author's own copy of the paper |
| Bovens 2007 | **primary, in full** — the definition, the three stages, the forum typology and the problem of many hands read verbatim |
| Matthias 2004 | **primary, in full** — the gap's statement and the control condition it rests on read verbatim |
| Santoni de Sio & van den Hoven 2018 | **primary** — the tracking and tracing conditions read in the published full text |
| Hollnagel & Woods 1983 | **primary abstract** — the definition of a cognitive system, from the authors' own abstract via NCBI's record |
| Hutchins 1995 | **author's own summary plus secondary** — the unit-of-analysis and emergent-properties formulations from the author's page for the book |
| Hollnagel & Woods 2005 / Woods & Hollnagel 2006 | **secondary only** — the books themselves were not obtained |
| Leveson 2011 | **secondary, but authored by Leveson** — the STPA Handbook's statement of the control structure, process models and the four types of unsafe control action, read in full |

**The two weakest readings are on the closest neighbour**, which is uncomfortable and is stated
rather than hidden. The Hollnagel-and-Woods entry is therefore written to claim only what the
primary 1983 abstract and multiple independent secondary characterisations agree on, and it credits
the priority rather than arguing a difference the reading has not earned.

---

## 4. Substance, per work, with the differentiating node

Every difference below cites a node **already filed and already cited elsewhere in the manuscript**,
so the drafted section adds no node to Appendix A and no pin to `graph/upstream.yaml`. Q44 and Q45
sharpened the reading; nothing here depends on them and neither is cited.

**Hutchins.** Takes: the unit of cognitive analysis is a collection of people and artefacts in a
work practice, and *"groups must have cognitive properties that are not predictable from a knowledge
of the properties of the individuals in the group"*. Differs: descriptive, not governing — no
acceptance relation, no assurance mechanism, no accountable principal. `term:arrangement`,
`DDD-frame-03`.

**Hollnagel & Woods.** Takes: **the priority for the arrangement as the unit is theirs, not the
framework's.** CSE *"introduces the concept of a cognitive system: an adaptive system which
functions using knowledge about itself and the environment in the planning and modification of
actions"* (1983 abstract, verbatim), and the joint cognitive system treats people and machines as
one such system. Differs: the JCS is characterised by what it does; it does not separate where a
resolution comes from from what establishes its acceptability, nor standing supply from occasioned.
`DDD-frame-03`, `DDD-cost-09`.

**Leveson.** Takes: a hierarchical control structure whose vertical axis *"indicates control and
authority"*, controllers with process models, and four provably complete types of unsafe control
action — not providing, providing, wrong timing or order, wrong duration. Differs: the four types
quantify over control actions **provided**, and a constraint that is authored and absent at the act
is modelled as a process-model or control-algorithm flaw. STPA's causal-scenario step can reach the
case; what is absent is a standing category that separates a decision's being **filed** from its
being **delivered at an act-site**. `DDD-delivery-01`, `DDD-delivery-02`.

**Horvitz.** Takes: initiative as an allocation decided per interaction under uncertainty about the
user's goal, with the twelve factors including *"inferring ideal action in light of costs, benefits,
and uncertainties"* and *"minimizing the cost of poor guesses about action and timing"*. Differs:
the factors govern **when the automated service should act**, not what the arrangement has committed
in advance; commitment levels are what the allocation is of. `term:commitment-level`. **And it
differs in the framework's disfavour**: Horvitz supplies a decision-theoretic criterion for the
allocation, and the framework supplies none outside the closing region. That is said in the entry.

**Bovens.** Takes: accountability as *"a relationship between an actor and a forum"*, with three
stages — the actor obliged to inform, the forum able to interrogate (*"hence the close semantic
connection between 'accountability' and 'answerability'"*), and the forum able to pass judgement and
impose sanctions. Also the **problem of many hands**, which is §7's difficulty stated twenty years
earlier. Differs: **four of `DDD-frame-08`'s five elements are already Bovens's** — the entry says
so. The fifth, authority linkage, is not; and Bovens's relation is assessed retrospectively over
conduct where the framework's is a design-time property of an engineering arrangement.
`DDD-frame-08`, `term:accountability`.

**Matthias.** Takes: the gap arises because *"nobody has enough control over the machine's actions
to be able to assume the responsibility for them"* — a control condition on just ascription, not a
missing name. Differs, **and less than the Gate 1 plan claimed**: the plan said the gap reads as
*"an arrangement naming an executor and no principal — fixable rather than novel"*. The reading does
not support *fixable*. `DDD-frame-08` holds that accountability does not read the executor's kind,
so an arrangement can be made complete without its principal predicting the executor; **whether that
completeness is morally sufficient to answer Matthias is a normative question the claim is
`projected` about and the paper does not settle.** This correction is the survey doing its job.

**Meaningful human control.** Takes: two separable conditions — **tracking**, that the system *"be
responsive to the human moral reasons relevant in the circumstances"*, and **tracing**, that its
actions *"be traceable to a proper moral understanding on the part of one or more relevant human
persons"*. Differs: tracing is satisfied by a person who understands and is answerable; the
framework's delivery question is whether the governing decision **reached the act**, and a tracing
condition satisfied in the record while failing at the act is escape that presents as governance.
`DDD-delivery-02`. The two are adjacent and not the same, and the entry says which is which.
