# Gate 2 — the outline, against the ruled survivor set

*draft-pending-ruling*

Sourcing rule as ruled at Gate 1: §§2, 3 and 5 cite terms and normative decisions; §4 asserts
the reported floor mechanism; every justification that lives in a `projected` claim is named in
§6 and nowhere else. The primer treats DDD-measure-11 and DDD-measure-13 as `projected`.

## Where the primer lives, and the pin

- **Location**: `projections/primer/primer.md` in `decision-driven-design`, beside
  `projections/tracks/` (the precedent DDD-dec-27 set: projections are this repo's artefacts).
- **Pin**: `v5.12.0` throughout — the version `graph/upstream.yaml` actually pins. Every quote
  and every generated block is drawn from the `v5.12.0` tag, not from head. §6 states plainly:
  the primer describes canon at `v5.12.0`; the ground migration's changes reach it at the next
  pin advance. (Checked: the pin-gap diff touching cited docs is two wording touches and one
  term annotation — nothing the outline below quotes changes sense across the gap.)
- **Generated where it can be**: a generator script `projections/primer/generate.py` fills
  marked regions (`<!-- primer:generated ... -->`) from the pinned tag — the term boxes (from
  `core/graph/terms.yaml` `canonical_md`, the format-2 embed mechanism), the §6 status roster
  (from both repos' `core/claims/`), the pin line, and the status counts. Everything else is
  hand-written-against-the-pin, and each hand-written section carries "written against
  `actor-indexed-determination v5.12.0`" in its own text.
- **Two-stage verification, applied to the primer's own tooling**: the generator writes a
  generation stamp (pin + digest of the generated regions); the Gate 4 check *fails on a
  missing or stale stamp*. A primer whose generated blocks were never generated is thereby
  distinguishable from one whose blocks pass — the pattern the month taught, applied first to
  the instrument that will police the primer itself.

## The sections

### §1 — What this is for (one page; hand-written; declaration embedded verbatim)

The job: governing decisions must be supplied from somewhere; the practitioner's work is
placement and escape-prevention. Cites `term:governing-decision` and `term:escape` (settled;
"determined never, by nobody… the only forbidden state").

**Finding, for ruling: `meta/the-declaration.md` exists in neither repository at head.** I
searched both repos by name and content ("declaration", "register-native", "§B-3"); the freight
manifest's B-3 is the unrelated exhaustiveness item. There is nothing to carry verbatim, and I
will not paraphrase or invent it. Proposed handling: the outline reserves a marked slot in §1
(`<!-- the-declaration.md §B-3, verbatim; blocked: source absent at head -->`); drafting
proceeds around it; the Gate 4 verbatim check binds the moment the file lands. Alternatives are
yours to rule: (a) you commit the declaration and the slot fills at Gate 3; (b) §1 ships with
the slot visibly empty; (c) the declaration is elsewhere and I fetch it from where you name.

### §2 — Filing a decision (hand-written; term boxes generated)

Procedure, in filing order:

1. **The admission test** — `term:admission-test` (settled, canonical): a choice is a decision
   iff varying the choice moves the outcome past tolerance; a fact is ground iff varying the
   world does. With `term:tolerance` and `term:decision`.
2. **The applicability gate** — DDD-ground-01 (normative): a resolvable applicability
   predicate, or declared universality; non-evaluation must never silently become
   non-applicability.
3. **The axis-type field** — provenance as attributes, the settled vocabulary; the three-axis
   reading (coverage / resolution / assurance) is taught as filing vocabulary, its claim
   (DDD-ground-02) named in §6.
4. **Store assignment and timing** — `term:store` (settled); timing values including
   "—(open)" for a deliberately-open resolution, taught as vocabulary with DDD-ground-03 named
   in §6.
5. **What a well-formed record contains**, including retro-filing — DDD-ground-04 (normative):
   the two fields, when the gap was uncovered distinct from when the act occurred, and that it
   was retro-filed.

Worked examples (all real, all filed): `DDD-dec-14` (the open decision — filing
deliberately-open without faking a resolution; corpus row 4); the no-unwrap decision from
`product-cli`'s `.ddd` register (corpus row 7 — filed as claim, reads as constraint: the store
question on data; pseudonymised); the pending risk-acceptance row (corpus row 8 — "exposure
accepted until review": what accepting a risk looks like as a filed decision; pseudonymised).

### §3 — Reading an act (hand-written; term box generated)

What governed it, what was delivered, what the verdict was. Cites `term:act`,
`term:act-individuation`, `term:verdict` (settled) and `term:delivery` — **registry status
`draft` at v5.12.0**, proposed handling: teach the act-triggered / judgement-mediated
vocabulary (it is the settled delivery vocabulary of the migration), with the registry status
named in §6 alongside the projected delivery claims.

- **Delivery type per act-site**: the same decision can be act-triggered at one act-site and
  judgement-mediated at another; a path is act-triggered only if every edge on it is.
- **"Filing is not encoding", stated as a check**: for each decision governing this act, name
  the channel that delivered it at this act-site; a decision with no channel here was not
  standing supply here, whatever the register says. The justifying claim (DDD-delivery-01) is
  named in §6, not here.
- **The two-stage verification pattern**, taught where the section teaches reading checks: a
  check whose pass state is indistinguishable from its never-run state is not a check.
  Exemplar: the pin advance filed as DDD-dec-34 — firing predicted in a committed file before
  the pin was touched, verified after, with the predicting instrument committed beside it.

Worked examples: `DDD-dec-02` (papers-before-tool — plainly judgement-mediated: no mechanical
carrier exists, it reaches an act only if a session recalls it; corpus row 3); the no-unwrap
decision again (mechanically delivered per act, check running *after* the act — the mechanical
store's defining position; corpus row 7); the ledger tolerance-floor decision (delivery by
construction — a below-floor state unconstructible rather than policed; corpus row 11,
pseudonymised).

### §4 — The floor, operationally (the exception: asserts the reported mechanism)

`term:floor` defines before it asserts, and the section follows it: the floor is the portion of
demand that cannot be moved off the in-the-moment actor — a property of the acceptance
predicate, not of the decision. Then `term:closure` (settled): closed for an arrangement when
the relevant ground is observable and adequacy evaluable within declared resource, latency and
confidence bounds.

The operational question: **does the predicate close for *this* arrangement, over material it
can inspect?** The consequence: check the work, or check the worker.

What §4 may assert, by status: DDD-frame-06 and DDD-measure-16 (`established` — closure is
distinct from generation cost; the construction is available exactly where the predicate
closes); DDD-floor-01 (`reported` — capacity-generated escape = overflow ∩ open, both
necessary), carried **with the v5.4.0 scope correction** (DDD-dec-15): overflow ∩ open is one
generator of escape, sufficient and not necessary — never the definition. Overflow alone,
closing predicate: retries, recoverable, not floor. Open alone, within capacity: carried by
judgement where an accountable supplier is named. The relational reading of the floor
(DDD-floor-02) is `projected` and goes to §6.

Worked example: the pin advance pair (corpus row 5 / DDD-dec-16): the standing pin is
mechanically checked (the predicate closes — check the work), the advance itself is a governed
judgement act (it does not — check the worker); one decision, both halves of the consequence.

### §5 — Finding escape (hand-written)

Escape is supply-general — determined by nobody, whatever the failure route. The generators, each
with what it looks like in a real register:

1. **Capacity-generated** — overflow ∩ open (`term:escape-mechanism`, settled; the DDD-dec-15
   scope carried as in §4).
2. **Delivery failure** — filed but undelivered: §3's channel check, run register-wide; the
   claim that this is escape (DDD-delivery-02) is named in §6.
3. **Silent non-applicability** — the ground-01 gate violated: a predicate that was never
   evaluated read as "did not apply".
4. **The unfiled decision** — visible only retroactively; DDD-ground-04's two fields are what
   make the retro-filed node honest.

The sweep's honest limit, stated as the section's closing discipline: **a coverage figure is
completeness relative to the declared coordinate system, so silence is not evidence of
coverage.** The two-stage pattern recurs here: a sweep records what it swept — its coordinate
system and its date — or a clean sweep is indistinguishable from no sweep. The empty-option-set
generator is named as open and unexamined, in §6.

Worked examples: the canon programme's own arrival failures — five delivered governing
artefacts that did not arrive, filed as evidence in DDD-dec-17/DDD-dec-20, and the corpus
test's Test B reconstruction floor (delivered governing sets recoverable only from residue);
the watched-edge `revisit_if` decision (corpus row 10, pseudonymised — a decision whose content
is its own revisitation trigger, i.e. escape-prevention filed as a field).

### §6 — What this does not do (roster generated; prose hand-written)

- **The pin, plainly**: this primer describes canon at `v5.12.0`, the version the projection
  repository pins; the ground migration's changes reach it at the next advance.
- **The research material, named with status** (generated roster from both repos' claims): the
  measure's empirical identification (DDD-measure-01, projected); maturation and the cost layer
  (cost family, projected); the calibration ledger (cost-24, dec-13, dec-14 OPEN); the org, sim,
  hyp and track families (projected, empirical); the delivery claims behind §3's and §5's
  procedures (delivery-01…-04, projected; term:delivery registry status draft); the relational
  floor (floor-02, projected); ground-02/-03 behind §2's vocabulary; measure-11 and measure-13
  read conservatively as projected. A practitioner meeting maturation or calibration elsewhere
  now knows what it is.
- **The instruments' own limit**: all three checkers verify correspondence against the graph —
  which is what makes them trustworthy and what bounds them. Prose *about* a document inherits
  no citation's protection: Paper A's abstract carried a retired claim (DDD-measure-06,
  `retired_from: established`) past three green checkers. Know that before trusting a green run.
- **Open and unexamined**: the empty-option-set generator.
- **What the statuses mean and do not** — one generated paragraph from spec §5: four
  established, all formal; a status is not a confidence score and does not aggregate.

## Length

Reported at Gate 3, no band. The shape above prices at roughly: §1 one page; §§2–5 two to three
pages each, procedures and one to two examples per section; §6 two pages of which half is
generated roster. Subtraction applies from the first draft.

## For ruling at this gate

1. **The declaration**: absent at head — handling (a)/(b)/(c) above.
2. **Location and tooling**: `projections/primer/` with `generate.py` and the stamped
   generation record as described.
3. **term:delivery at `draft`**: teach the delivery vocabulary in §3 with the registry status
   named in §6, as proposed — or hold §3's vocabulary some other way.
4. **The worked-example set**: the eight named above (dec-14, dec-02, dec-16/dec-15 pair,
   dec-17/dec-20 arrival evidence, dec-34, and corpus rows 7, 8, 10, 11 from `product-cli`,
   pseudonymised). Any row you strike, I replace only from the same three real sources.
