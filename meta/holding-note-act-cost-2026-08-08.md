# Holding note — act, cost, maturation, and pricing (session 2026-08-08)

<!-- ddd:contract
requires: [act (pending this session's canon edit), encode-verify-split, tolerance, actor, arrangement]
establishes: []   # deliberately nothing — this file fixes no terms and promotes no claims
status: closed — historical record (2026-08-10). Curated into canon by the Wave 2 session,
gated A–H with Emil ruling at every gate; the closure manifest in §14 maps every item to its
claim/term/decision ID. Canon authority is those files, never this note.
-->

**Provenance.** Drafted by Claude from the 2026-08-08 project session, at Emil's request, so
the reasoning survives outside a chat transcript. Items marked *affirmed* were agreed
conversationally in session; *proposed* items are Claude's reasoning Emil has not confirmed.
Nothing here is ratified canon. Session artifacts referenced: `measure-mdl-demo.py`, the
empirical assessment ("Two-Part MDL Cost Structure in Manufacturing"), `act-four-stores.svg`,
`maturation-curve.svg`, `price-the-act.html`, `prompt-act-primitive-canon.md`.

---

## 1. The maturation model *(affirmed in session; construal of funnel/inverted funnel confirmed)*

The act is a two-sided event. Forward, it consumes occasioned supply. Backward, it produces:
the verdict is new ground about the verdict function itself. Maturation is the return channel
spanning the act in reverse — from the mechanical store (post-act verdicts) into the encoded
store (pre-act standing supply). A maturing arrangement is one where that loop is closed.

The schedule follows from the cost layer. The crossover condition N* = mechanism cost /
per-act saving defines a waterline; cumulative acts push it down; distinctions encode in
information-density order as each crosses its N*. Per-act occasioned cost declines stepwise
toward a floor. The floor decomposes into the open-predicate residual (no verdict function —
nothing to encode, ever) and the below-waterline tail (verdicts exist, not worth encoding at
this volume).

**Maturity is the distance between an arrangement's actual allocation and the
volume-and-drift-optimal allocation — not the fraction encoded.** Steady state is an
equilibrium where encoding rate matches drift-driven depreciation of encoded bits.

| Stage | Allocation | Signature |
|---|---|---|
| Novice | All occasioned | No record; volume buys nothing |
| Recording | Occasioned + capture | Verdicts accumulate; waterline begins descending |
| Encoding | Staged build-out | Distinctions cross N* in density order; learning curve |
| Equilibrium | Standing above waterline; occasioned = floor + tail | Encoding rate = drift rate |
| Sclerotic | Over-encoded | Standing exceeds optimum; drift outruns re-encoding |

Rate bounds *(each a distinct claim)*:
- **Record dependence.** Uncaptured verdicts mature nothing. An arrangement without an
  execution record pays full occasioned cost forever, regardless of volume. The record is a
  productive asset, not only an accountability one. *Falsifier:* arrangements with equal
  volume but no verdict capture show declining occasioned cost anyway.
- **Escape is doubly costly.** Escaped residual never reaches the predicate, so it generates
  no verdict: ungoverned now and invisible to maturation. **Escaped demand cannot be learned
  out of.** *Falsifier:* demonstrated maturation on distinctions whose resolutions were never
  checked.
- **Open predicates stall the loop.** No verdict function, no clean signal; maturation runs
  only on proxy, delayed, or social feedback — the region Paper A's H5 assigns to
  selection-over-training.
- **Drift is the counter-force.** Over-encoding is a real failure mode (basis: Abernathy &
  Wayne 1974, the Model T — organisational, not a cost floor; see the empirical assessment's
  caveat). *Falsifier:* high-drift domains showing encoded fractions equal to low-drift
  domains at equal volume.

All projected. Files in the cost file's orbit (dynamics of the optimised layer, same
register: not conserved).

## 2. The channel-memory claim *(proposed)*

> **A rented arrangement pays standing supply at occasioned rates, because the rented channel
> has no memory.**

Act-side encoding — context, retrieval, instructions, scaffolds — is standing supply by
nature: pay once, inherit every act. The rented channel re-transmits those bits on every act
and meters them as occasioned. Consequences: renting the act without own-side encoding
produces spend linear-or-worse in act volume (the Novice flat at industrial scale); no
descent of the maturation curve is possible through the channel alone; vendor prompt-caching
is partial amortisation retrofitted onto a meter that denies it *(proposed reading, flagged)*.
This claim also grounds why the rent-vs-own crossover (§4) exists at all.

## 3. The token as the machine's hour *(affirmed in session)*

The token meters the rented actor's channel traffic — compute consumed, context
re-transmitted, internal search — which is the supplier's quantity. It does not meter demand
resolved, the buyer's quantity. A ten-token act can carry more `H(V)` than a thousand-token
act. Structurally the same denomination error as the billable hour: pricing one store's
throughput and calling it value. Files under Context& projections (pricing), with §2 as its
mechanism.

## 4. Rent-versus-own *(affirmed in session, with two canon-precision corrections applied)*

A rented actor improves only by encoding *around* it (context, retrieval, scaffolds — per
act, bounded by the channel). An owned actor improves by training — which **converts judgment
to encoded inside the carrier**; it does not enlarge the judgment store. Precision points:
training buys allocation, not capacity; ownership does not create a principal, but adds the
control linkage of Paper A §7 (weights, training data, change record governed).

Two maturation curves follow: rent-and-encode (low `L`, per-act context tax, capped descent)
and own-and-train (large `L` in training cost, deeper floor, surplus captured in the
carrier). Ownership crosses over at sufficient act volume *and* sufficient closure — training
needs signal, signal needs verdicts, verdicts need the predicate to close. This derives
Paper A's H5 axis from the rental structure rather than positing it. Fine-tuning-as-a-service
is the mixed store: rented carrier, trainable allocation, no control of base ground.
*Proposed corollary:* locating a client's crossover is an N*-type calculation and a sellable
service.

## 5. Actor selection — right-sizing the actor to the act *(affirmed in session, incl. the assurance gate; formulations proposed)*

Acts differ in residual demand `H(V|E)`; actors differ in capacity, price, and assurance
class. Current rented practice binds one frontier actor to every act, so the rent price
collapses to tokens × a constant tier — structurally unable to correlate with per-act
demand. **Paying frontier capacity for every residual is paying peak price for mostly
trivial acts.**

The routing rule is two-gated, and the gates cover different regions of the act:

- **Capacity gates always.** The actor must carry the act's residual at the declared
  tolerance, or the excess escapes.
- **Assurance gates where the predicate does not close.** There, α cannot attach to a check,
  so it must attach to the actor — qualification, track record, certification, class. This is
  the contrapositive of Paper A §5.6: producer independence holds for checked properties, so
  for every unchecked property, producer identity is load-bearing. *Actor assurance is what
  fills the space mechanical verification vacates* ("check the worker where you cannot check
  the work"). Where the predicate closes, α discharges through the checker and actor choice
  is free above the capacity bar — which is what legitimises cheapest-sufficient routing
  there, and only there. Mixed acts split: check what closes, select for the rest.

The soldier case is the tendency in pure form: no mid-act verification is possible, so
assurance is pre-paid entirely into selection, and the class of soldier is the assurance
mechanism. Selection additionally carries **tail-risk assurance** — low variance under
conditions no output-check would have exercised; a checker vouches for the acts it sees, a
selected actor is vouched for on the acts nobody foresaw. This is part of what the higher
class buys and why selection persists even where predicates mostly close.

*Proposed cost-layer claim:* **a closed predicate is amortised assurance.**
Assurance-by-actor binds α to a scarce carrier priced per act; assurance-by-check moves α
into a mechanism paid once. Closing a predicate converts assurance from the arrangement's
most expensive supply into standing supply — the sharpest economic argument for predicate
discipline in the set, and the explanation of selection-pipeline economics (enormous
standing investment because the per-act assurance it enables cannot be bought otherwise).

**The sign flip** *(affirmed in session; formulation proposed).* On open predicates,
assurance and actor class are positively coupled: more α, higher class. Closure flips the
sign: high α becomes a reason to encode into the mechanical store, and the actor class
falls — the actor is left carrying generation only. Two mechanisms do the lowering, and
they are distinct: (i) the assurance gate lifts — α discharges through the check, producer
independence applies; (ii) the capacity gate softens — a checker permits generate-and-test,
so weak actor + retries + verification composes into effective capacity exceeding the
actor's; verification converts capacity shortfall into retry cost. This derives Paper A H3
rather than positing it, and is the formal licence for small-model routing on closed
predicates.

Bounds on the sign flip:
- **Acceptance-region accessibility still gates generation** (Paper A §5.5): a checker
  cannot make a weak actor find a sparse candidate; the move works where the region is
  dense and retries cheap.
- **Retry economics enter the routing**: weak actor × expected retries × per-act price vs
  strong actor × one shot, a computable crossover. Rich rejection payloads shift it — a
  checker that explains its rejection turns each retry into a guided step, raising the weak
  actor's effective capacity. *Consequence for open decisions:* the M3/M4 apply_edit
  rejection-payload shape is a lever on achievable actor class, not an API detail; that
  decision now has a framework-level basis.
- **Safety condition — unchecked-property degradation.** Frontier actors silently supply
  assurance on properties nobody declared; downgrade the class and everything outside the
  predicate's coverage degrades without a signal. Class may fall only as far as the
  predicate's coverage of α actually extends. Skipped, the small-model move is an
  escape-mode generator, not an optimisation.

*Falsifiers for the sign flip:* closed-predicate deployments where declared-equal assurance
is not met by weak-actor+checker arrangements at any retry budget in dense regions; or
actor class failing to fall with checker investment where coverage is complete.

### 5a. Capabilities — typing the capacity vector *(affirmed in session; formulations proposed)*

Capacity is not a scalar. A **capability** is a typing over an actor's pathways: the class
of ground a pathway can read (visual, repository, physical, tool-mediated) and the class of
distinctions it can resolve against it. **Not a third primitive** — it classifies the two
primitives' traffic. The requirement side derives from the admission test applied per
ground type: *an act requires capability X iff its verdict varies with ground accessible
only through X-type pathways.* Grounded, exclusionary, no free parameter.

The routing rule sharpens to a max over the vector:

> **Required actor class = max over the act's capabilities of the class needed where α is
> not mechanically discharged — per capability, not per act.**

One uncovered high-class capability pins the act to frontier even when everything else is
trivial. This explains the coding case: mechanical coverage of the coding capability is
partial (tests cover a slice; architecture, intent, unstated operational properties stay
open), so the α residual attaches to the coding capability specifically and the sign flip
has not occurred for that component. Frontier coding class is being rented as assurance on
everything the tests do not reach. Close that coverage and the pin releases — the
small-model saving for coding is gated on coverage of the coding capability, not on model
progress.

Consequences:
- **Bundled pricing buys the vector.** Frontier is high class across many capabilities; an
  act with one binding capability pays for all. Capability-specialised small models are the
  market unbundling this — evidence for the typed view, since scalar capacity cannot
  explain narrow-high beating general-mid on matched acts.
- **Benchmarks are licences** *(proposed)*: where assurance attaches to a rented actor's
  capability, the per-capability eval is the assurance instrument — selection by
  qualification (Paper A, principal-level commitment) applied to models. Eval scores
  function as class certificates for actors nobody can interview.

Confound, carried honestly: capability levels within an actor correlate strongly (a general
factor), which is why "frontier" works as a single label. The typed claim earns its keep at
the margins where profiles diverge. *Falsifiers:* scalar capacity predicting routing
outcomes as well as the vector on divergent-profile actors; assurance transferring freely
across capabilities within an actor at no loss.

Routing requires per-act demand *and* per-act assurance need to be declared — which the
acceptance predicate and triage already provide in a governed arrangement — so actor
selection is downstream of predicate discipline, not a separate practice. Structural echo:
measure note §5.1 (actors as volume regimes) and Paper A H5 (selection rises as evaluation
weakens) both fall out of the same two gates. *Falsifiers:* demand-routed arrangements
failing to beat single-frontier arrangements on cost at equal acceptance rates; arrangements
achieving declared assurance on open predicates with unselected actors at no loss.

## 6. The Context& pricing projection *(affirmed in session)*

The hour is denominated in occasioned supply — it priced one store and called it value; the
proxy held only while judgment had one carrier. Both stores are now rentable (`00` §6: the
first actor pinnable by binding). Hourly billing additionally punishes maturation: every
encoded distinction shrinks the invoice, so the pricing model decides who captures the
descent. The honest model segments by closure: closed portions priced fixed per accepted
act (product); open residual on retainer as access to an accountable principal (floor +
accountability-completeness, never hours); undeclared scope is escape risk — scope creep is
escaped demand under a fixed price. When the act is a commodity, **the arrangement is the
product**: declared predicate, entitled acceptance, principal who answers.

Honesty boundary: the conclusion (leave the billable hour) is established ground
(value-pricing literature, Baker et al.); the framework contributes the mechanism only.
Files under Context& projections; traceability line to Paper A §7 wanted when the website
surface is built.

## 8. Labour-market stratification *(proposed throughout; social-science claims — higher flagging bar)*

The α–capability coupling runs through closure: where checks are strong, α discharges
mechanically and class stays low regardless of stakes. Where they are weak, α lands on the
carrier — and on an open predicate it cannot attach to one capability cleanly, because
nothing verifies where one capability's contribution ends. **Verification separates
capabilities; its absence bundles them.** High-assurance open work demands the full vector
at high class because unverifiable work cannot be decomposed into checkable, routable
slices.

Three regimes, with distinct fates under the new actor:
1. **Single-capability, covered, mid-class** — abundant, cheaply trained, and the rented
   actor's first target: coverage is what makes an act routable, and routable acts route to
   the cheapest sufficient carrier. This names the mechanism behind routine-biased
   technological change (Autor–Levy–Murnane, basis): *routine* was a proxy for
   *mechanically coverable*.
2. **Single-capability, high-class, uncovered** — the specialist. Moat = the openness of
   their predicate; every coverage investment in their capability is a pending class drop.
3. **Multi-capability, high-class, open-α** — the vector roles. Protected by
   un-decomposability on the demand side (and see the separated scarcity claim below).
   Where accountability concentrates: un-checkable acts need principals.

**The prediction:** the wage premium migrates from capability level to predicate openness.
Equal-class workers on coverable vs open capabilities should diverge as coverage
accumulates; premia should decline in occupations with demonstrably improved verification
tooling, at a lag tracking coverage investment. *Test bed:* task-content data (O\*NET
lineage) — codes routine-ness, not coverage; adjacent, not identical, same gap as the
floor-free meta-analyses. Credentials price class; the rent accrues to positions in the
coverage structure. Corollary: examination systems are coverage infrastructure, so
professions whose examinations closed most should show the earliest routing pressure.

**Separated claim, filed to fail alone** *(per Emil, 2026-08-08)*: multiplicative scarcity —
if class-3 in one capability is 1-in-10, class-3 across k quasi-independent capabilities is
rarer than any single tail, explaining vector-role scarcity. Shakiest link: the general
factor substantially rescues real populations from independence. Its failure would not
touch the regime structure above. *Falsifier:* vector-role supply predicted by the general
factor alone, with no residual multiplicative penalty.

## 9. The openness axis of actor class *(affirmed in session via the spec-ops gradient; formulations proposed)*

Actor class has two axes: capability class, and **what the actor is certified to carry — a
declared predicate or an open one.** Different assurance products, separately priced:
- **Declared-predicate execution class**: tight tolerance, scoped act, checkable outcome,
  extreme α; the predicate pre-exists the act; selection optimises low-variance execution.
  (Session shorthand: the SEAL case.)
- **Open-predicate determination class**: the mission statement is open; the actor supplies
  the predicate itself — declares, executes, accepts in-theatre, within intent. A delegated
  principal-level function, not more of the same demand. (The Delta case.)

Canon correspondence: this is the commitment ladder (Paper A §3) as a military doctrine
history — detailed orders = outcome-level; doctrine/ROE = policy-level; mission command
(Auftragstaktik) = principal-level, with commander's intent as tolerance declaration. As
mission statements open, the arrangement climbs the ladder.

**The selection instrument mirrors the deployment predicate** *(proposed)*: open-class
assessment removes the checker (unannounced standards, no feedback) because the only valid
test for open-predicate carriage is sustained determination without external verification —
the condition of deployment. Declared-class selection may use checkable drills; open-class
selection must test in the check's absence. Pipeline economics follow §5's amortised-
assurance logic: the pipeline is the standing investment that produces carriers of
open-predicate assurance, brutal because act-by-act verification of the product is
unavailable.

**The model-market gap** *(proposed; safety-relevant)*: every benchmark has an answer key,
so every benchmark is a declared-predicate instrument. **No licensing instrument exists for
open-predicate delegation of models** — yet the market delegates open missions ("improve
the codebase") on execution-class certificates. Bounds the benchmarks-are-licences claim
(§5a): licences exist for the first class only. *Falsifier for the axis:* declared-class
certification predicting open-mission performance at no loss — if execution scores fully
predict open-delegation outcomes, the second axis is redundant.

## 10. Claims as acts — the claim layer *(affirmed in session; construal noted, formulations proposed)*

*Construal (confirm or strike):* "use system actor capabilities to prove claims" is read as
attaching claim assurance to the arrangement's actors by capability class where the claim's
predicate will not close mechanically; the alternate reading — system instrumentation
closing claim predicates — is the other gate of the same rule, and both are filed.

**The inversion.** The feature layer is the most covered territory in software (compilers,
types, tests, CI — decades of coverage investment); the claim layer is the most escaped.
Every feature embodies a claim — *this behaviour serves that goal* — shipped undeclared,
unfalsified, verdict never collected. Product organisations run large escaped-claim
inventories; OKR/KPI machinery is proxy closure on those open predicates (existing Goodhart
canon). The demand did not leave the claim layer; it escaped there, because verification
tooling points at the layer below.

**The formal move (canon already holds it): a claim is an act with a deferred verdict.**
One claim = one act; verdict arrives at `closesAt`; `pending-verdict` is the act in flight;
closure is the verdict event. Act individuation extends with no new rule, so the session's
machinery applies natively: claim capabilities (product, technical, market judgment),
two-gate routing, escape, maturation.

The two gates at the claim layer:
- **Instrument toward closure** where the horizon permits: declared falsifier, metric,
  `closesAt`. Coverage investment on claims, same N\* economics — worth building for
  claim-classes made repeatedly. (A product strategy, in this vocabulary: a standing bet
  amortised over many claim-acts.)
- **Carrier assurance** where it does not: α attaches to the claimant by demonstrated
  class. **The calibration ledger** (per-claimant accuracy across matured predicates) is
  the licence instrument §9 found missing: open-predicate carriage cannot be tested with an
  answer key, but a claimant's record across claims whose predicates *later closed* is a
  matured-verdict certificate. Works identically for model actors — a model's delegated
  claims tracked against later verdicts is the open-class licence the benchmark regime
  cannot provide. **The calibration ledger closes the model-market gap (§9)**; status
  change: from parked construct to load-bearing, pending Emil's ratification.

*Falsifiers:* claimant calibration failing to predict subsequent claim outcomes better
than seniority or confidence; instrumented claim-closure showing no reduction in
escaped-claim incident classes relative to proxy-governed (OKR) baselines.

## 11. Time as a factor of assurance *(proposed throughout; items (a),(b) partially held by existing canon)*

The act gives assurance a time axis: before/during/after exist only relative to a bounded
episode. Four distinct mechanisms, kept apart:

**(a) Closure is time-indexed; the verdict gap is carrier-bridged.** Operational closure
already includes latency bounds (canon, v4.5). Consequence: a late-closing predicate is
open *at act time* — the check exists but has not happened — so assurance across the gap
can only be carried. Every `closesAt` horizon is a declared span of carrier-borne
assurance. *Falsifier:* arrangements sustaining declared α across long verdict gaps with
no identifiable carrier and no loss.

**(b) Mechanical assurance decays at the drift rate of the ground it read.** α is α(t): a
passing check is a stored statement about uncontrolled ground (canon: revalidation
cadence). Re-verification cadence is the standing cost of holding α above the declared
level; the sclerotic branch (§1) is this decay outrunning re-supply. Expiring
certifications and rotting test suites are one phenomenon at two layers.

**(c) Carrier assurance accrues at verdict speed.** The calibration ledger builds from
matured verdicts, so an open-class licence has a minimum build time: verdict latency ×
sample count. Open-class actors are slow to produce for this second reason — the assurance
evidence itself arrives at `closesAt` speed. **Turnover bound: when actor turnover
outpaces verdict latency, carrier assurance cannot accumulate.** Model versions churn
faster than open-claim verdict horizons, so the ledger (§10) closes the model-market gap
(§9) only for actors whose identity outlives their verdicts; cross-version transfer is
partial at best and per-capability. *Falsifiers:* fast-minted open-class certification
performing at par; full assurance transfer across version bumps at no loss.

**(d) Tempo prunes assurance positions.** Mechanisms have temporal positions — pre-act
(selection, training, encoding, static checks), at-act (monitoring), post-act (review,
audit, consequence) — each with latency. Rising act tempo pushes post- and at-act
mechanisms outside the budget, forcing assurance pre-act into standing supply or the
carrier. Names the mechanism in the soldier case: no review fits inside the act, so all
assurance is pre-paid. Slots into conservation-into-tempo.

**(e) Ground assurance and the recon cadence** *(affirmed in session; formulation
proposed)*. A check verifies the resolution against declared ground, so a valid verdict on
poisoned ground is wrong with full authority (existing canon) — ground assurance is a
distinct requirement with its own three suppliers: **encoded** (validators, freshness
constraints — standing), **carried** (the actor's anomaly-detection capability; degenerate
actors have zero detection class, which is why classical practice obsesses over input
validation — predicted, not assumed), and **occasioned** (recon: fresh observation at a
cadence). **Substitution law: carrier detection class and recon cadence are substitutes**
— weaker actors require more frequent ground checks. Cadence is computable from §11(b)'s
decay machinery: exposure per act ≈ λ·t·(1−d)·(1−c) held under the α-implied bound, with λ
the drift *or adversary* rate, d detection class, c encoded coverage; demonstration in
`recon-cadence-demo.py` (stipulated; ~35× interval spread across classes; adversary tempo
compresses all cadences and makes detection class dominant, since the attacker sets λ).
Security corollary: **prompt injection is poisoned ground meeting insufficient detection
class at zero recon cadence** — agent defence is a ground-assurance budget across the
three suppliers, not a prompt trick. *Falsifier:* recon frequency and actor class failing
to trade off in ground-incident rates at matched α.

## 12. The boundary charter — actor principle vs DDD *(affirmed in session 2026-08-09; sharpening proposed)*

**Emil's charter:** the actor principle describes one actor performing one act — where
determination demand sits and what supplies it. Its whole content: every decision affecting
the act is supplied from one of the four stores, gated by tolerance, assurance, capability.
It says nothing about claims. **DDD is named for what it adds: the decisions/claims
graph/ledger layered on top.**

**Sharpened test (proposed):** does the statement require anything to persist between
acts? No → actor principle (synchronic, stateless). Yes → DDD (diachronic, the graph is
the persistence). This supersedes the "military unit" sorting test as the primary
boundary; generality remains a secondary check.

What the charter re-derives *(evidence it is the right cut)*:
- **Channel-memory becomes a corollary:** a rented arrangement executes Layer 1 only — it
  performs acts and cannot hold the graph. Final form of the pricing argument: **the
  ledger is the arrangement's memory; renting the actor never rents the memory; DDD is
  the ownable layer.** "The arrangement is the product" resolves to: Layer 2 is the
  product.
- **Maturation is a Layer 2 phenomenon by its own claims:** record dependence is the
  statement that maturation does not exist without the ledger. Likewise calibration,
  `closesAt`, pending-verdict, and all N/k/horizon quantities.
- **R2 resolves along the act boundary:** per-act supply identity and gates → actor
  principle; volume optimisation, crossover, amortisation → ledger layer. The cost-file
  fork was the boundary showing itself.

**Re-sort consequences (supersedes parts of the queue's destination table — see R4):**
maturation general statement, calibration construct, §11(a)–(c) → DDD; §11(d) (tempo,
within-episode) → actor principle; claims-as-acts is the **bridge definition** — stated in
act vocabulary, operable only with the ledger.

**Open tension for ruling (R4b):** ledgers exist outside engineering (after-action
reviews, service records = calibration). Either (a) DDD is the actor-general name of the
ledger method, engineering merely its home domain — Emil's sentence reads as (a) — or
(b) a thin general Layer 2 statement lives upstream with DDD as its full engineering
instrument. *Falsifier for the charter:* a load-bearing actor-principle claim that cannot
be stated without inter-act persistence, or a ledger-layer claim fully expressible
per-act.

**Reflexive corollary — the framework describes its own repo topology** *(affirmed in
session 2026-08-09; formulation proposed)*: a repo split is a decomposition, so it has a
seam; `upstream.yaml` is the seam contract and E12/E13/W5 its mechanical verification.
The charter cut was a high-information seam: heavy pre-payment into the boundary (the
persistence test, the pin discipline) buying two simpler parts — decomposition B's
pattern, applied to the repository itself. Consequences for future splits: **SDP orders
them, the cost layer times them** — a package earns separation when its stability
diverges from its neighbours and consumers want to pin it independently, an N\*-type
decision; do not split ahead of the crossover. The seam itself splits across the
boundary: its arithmetic (the chain-rule identity, declared ground distribution) is
Layer 1; its life (choosing `S`, the interface contract, the `I(V;S)`↔interface-cost
correspondence with its `closesAt`, amortisation over N) is Layer 2. First future split
candidate: the claim-format specification — the interface between canon and all tooling,
the most SDP-stable object in the system.

**Composition is Layer 1** *(affirmed in session 2026-08-09; formulations proposed)*: a
composed arrangement executing one act is Layer 1 twice over — from outside the declared
boundary it is one actor (capability vector, capacity); inside, the wiring is declared
structure, like the ground distribution and the decomposition. Layer 1 is not timeless:
sequence exists within the episode (tempo, §11d); the test is only that nothing survives
past the verdict. **The arrangement is Layer 1; the arrangement's history is Layer 2**
(member selection, composition decisions, calibration-keyed escalation, standing teams
amortised). Two consequences: (i) **nesting addendum to individuation** — acts nest as
actors nest; one act = one verdict of the declared predicate *at the declared boundary*;
inner checker verdicts individuate inner acts; retry economics stays synchronic as an
expectation over the outer act; learning from rejections across acts is Layer 2. (ii)
**Composition is Layer 1's named unfinished mathematics** (measure caveat 4): the chain
rule iterates — `H(V) = I(V;E₁) + I(V;E₂|E₁) + H(V|E₁,E₂)` — the conditional terms are
the composition's internal seams; composition is to the supply side what decomposition
is to the task side, under the same identity.

## 12a. The operational one-line, and the domain distinction *(Emil's crystallisation, 2026-08-09; sharpening proposed)*

**Emil's statement:** for an act, every decision governing it must be supplied from one of
the four stores. We do not care how many; we care that each is in one of the three and not
escaped.

Sharpened into its two questions:
- **The governance question** — *is every governing decision in a declared store, none
  escaped?* Binary per decision, count-free, **total domain**: well-formed on open
  predicates, where the measure does not exist. Three suppliers, one sink; the goal is a
  dry sink.
- **The cost question** — *how much is in each store?* Measured in bits, **partial
  domain**: exists only where the predicate closes (`08`).

Consequence: DDD's governance layer ranges strictly wider than the measure — the reason
the framework is not merely applied information theory, and the reason it governs product
claims, mission statements, and architecture where `H(V)` is undefined.

Corollary retiring a practice class: conservation makes reduction impossible, so
"simplify away the decisions" is not a goal — **the only games are placement and
escape-prevention.**

**Addendum — the measure's role** *(Emil, 2026-08-09; sharpening proposed)*: measuring
demand is valuable in software and **not necessary** for the method. Sharpened: **the
measure's job is to exist, not to be computed.** Its existence on the closing region is
what makes conservation a theorem, escape a defined category, and the cost proxies honest
— practice runs count-free on the audit and proxy-priced (money, hours, tokens) on the
optimisation, never on live entropy. Position: *necessary for the warrant, unnecessary
for the operation.* Consequence for the measure paper: state this in its framing (near
§6) — it pre-answers the practicality objection and strengthens the paper's modesty.

## 12b. Papers as projections *(Emil's crystallisation, 2026-08-09; consequences proposed)*

**Paper A is a projection of `actor-indexed-determination`, as the measure note is a
projection of `08`** (whose context file already states it: "the repo is ground truth").
Papers do not hold content; canon holds content, papers hold registers.

Consequences:
- **Wave 3 re-scoped** (corrects the queue's earlier framing): openness axis, labour
  stratification, commitment-ladder material, model-market gap, and H1–H5 file as
  upstream claims with statuses and falsifiers *first*; the paper projects them. A paper
  may not introduce claims, by the same rule that prompts may not introduce design. Only
  register-native material (related-work positioning, prose argument) is authored in the
  paper directly.
- **Writing Paper A becomes auditing**: the revision foundation runs as a two-way gap
  checklist — draft-says-what-canon-lacks → file or cut; canon-holds-what-draft-lacks →
  projection incomplete.
- **Mechanical fidelity**: a future `validate-paper` diffs manuscript claims against the
  graph (E6–E9 discipline applied to the manuscript); front matter pins the projection —
  "projection of `actor-indexed-determination` at vX.Y" — making the arXiv artefact
  reproducible against a repo tag.
- **One source, two registers**: Paper A and the generated website project the same claim
  graph — reviewers and checkers read different renderings of identical content.

Candidate use: operational counterpart to `00` §7's one-line; website front-page
statement. *Falsifier for the domain claim:* a governance audit question that cannot be
posed without the measure, or a demand reduction (not relocation) demonstrated at fixed
task, tolerance, and ground.

## 13. Filing guidance

| Item | Files where | Status |
|---|---|---|
| Maturation model (§1) | Cost file orbit — dynamics section or successor file | Projected, unratified |
| Channel-memory claim (§2) | Cost file orbit | Proposed |
| Token/hour symmetry (§3) | Context& projections | Affirmed, unfiled |
| Rent-vs-own + crossover (§4) | Cost file orbit; related-work hook to Paper A H5 | Affirmed, unfiled |
| Actor selection (§5) | Cost file orbit; echoes measure note §5.1 | Affirmed, formulation proposed |
| Pricing projection (§6) | Context& projections | Affirmed, unfiled |
| Labour-market stratification (§8) | Paper A orbit — H2/H5 labour side; ALM as basis | Proposed |
| Multiplicative scarcity (§8, separated) | Same, filed to fail alone | Proposed, weakest link |
| Openness axis of actor class (§9) | Paper A orbit — commitment ladder, selection/H5; model-market gap safety-relevant | Affirmed via gradient; formulations proposed |
| Claims as acts + calibration ledger (§10) | Spans all three: canon (claim=act extension), cost file (claim-layer gates), Decision Ledger PRD (the ledger's role); resolves §9's gap | Affirmed; ledger promotion pending ratification |
| Time as a factor of assurance (§11) | Cost file (decay, tempo); ledger construct (accrual, turnover bound qualifies §10's resolution of §9) | Proposed |

Nothing above enters canon through this note. Each item requires its own decision and, where
claims are made, filing with falsifiers via the standard workflow. Queue position unchanged:
the measure note's related-work section remains ahead of all of it.

---

## 14. Closure — the Wave 2 filing manifest (2026-08-10)

**This note is now a historical record pointing at canon.** Every item below entered canon (or
was explicitly deferred) through the Wave 2 curation session, gated A–H, with Emil ruling at
every gate. Canon authority is the claim, term, and decision files named here — where this
note and canon disagree, canon governs. Branches: `claude/wave2-canon-curation-r3v571`
(actor-indexed-determination, harness-designated) and `session-yield-2026-08-08`
(decision-driven-design), per the branch ruling at GATE A.

| Item | Destination | Status | IDs |
|---|---|---|---|
| R4b ruling — DDD is the actor-general name of the ledger method (a) | downstream decisions | ruled, recorded | `DDD-dec-11` |
| R3 ruling — synchronic single-domain generals upstream at projected, flagged | upstream decisions | ruled, recorded | `DDD-dec-12` |
| §12 composition addendum (Layer 1) | upstream `core/06` "Composition at one act" | affirmed, filed as prose | — |
| §12 individuation boundary clause | upstream `terms.yaml` + `09` §1 re-projection | settled term amended | `term:act-individuation` |
| §12 reflexive corollary (repo topology) | upstream `meta/repo-topology.md` | affirmed, filed (meta) | — |
| §12a operational one-line, domain distinction, measure role | upstream `09` §7 "The operational form" | projected; one-line flagged candidate for `00` §7; measure role flagged to the measure paper's framing | `DDD-frame-11` |
| 2.1 capability term + admission-test derivation | upstream `terms.yaml` + `10` §7 | settled term; derivation prose | `term:capability` |
| 2.2 two-gate routing rule | upstream `10` §6 | projected | `DDD-cost-08` |
| 2.3 assurance-locus conversion / amortised assurance (GATE B carve) | upstream `10` §6 + downstream `13` §5 | projected, both | `DDD-cost-09`, `DDD-cost-10` |
| 2.4 sign flip, three bounds as region | upstream `10` §6 | projected | `DDD-cost-11` |
| 2.5 max-over-vector, frontier pin, coverage-not-actor-progress | upstream `10` §7 | projected, R3-flagged | `DDD-cost-12` |
| 2.6 selection instrument and its bound (GATE C carve) | upstream `10` §7; downstream stub in `core/README.md` | projected; instance pending evidence | `DDD-cost-13` |
| 2.7 routing worked example + script | downstream `core/15` + `core/assets/measure-routing-example.py` | evidence note; asset reproduces | — |
| 2.8 maturation model | downstream `core/14` §§1–2 | projected ×5; terms settled | `DDD-cost-14`–`18`; `term:maturation`, `term:waterline`, `term:maturity` |
| 2.9 channel-memory (GATE D, mechanistic form) | downstream `14` §3 | projected | `DDD-cost-19` |
| 2.10 around/within + crossover (pre-Gate-E carve) | upstream `10` §8 + downstream `14` §4 | projected, both | `DDD-cost-20`, `DDD-cost-21` |
| 2.11 claims-as-acts (GATE E, construal confirmed) | upstream `09` §1 + `10` §9 + `spec/claim-format.md` §5; downstream `13` §6 | projected | `DDD-frame-12`, `DDD-cost-22`, `DDD-cost-23` |
| 2.12 calibration-ledger promotion (GATE F) | downstream `core/16` + decisions | projected; promotion recorded; identity unit OPEN | `DDD-cost-24`, `DDD-dec-13`, `DDD-dec-14`, `term:calibration-ledger` |
| §11(d) tempo prunes assurance positions (GATE G) | upstream `10` §6 | projected | `DDD-cost-25` |
| §11(a)–(c), (e) time register (GATE G) | downstream `core/17` + `core/assets/recon-cadence-demo.py` | projected ×4; asset reproduces | `DDD-cost-26`–`29` |
| 2.13 rejection-payload basis for M3/M4 | **pending transfer** — `product-cli` outside session scope; basis carried at `DDD-cost-11` notes and `15` §4 | awaiting mechanics ruling (GATE H) | — |
| Wave 3 (openness axis, model-market gap — qualified by `DDD-cost-24`'s validity condition — labour stratification, multiplicative scarcity; H1–H5) | upstream claim filings, then Paper A projection | pending paper work | — |
| Wave 4 Context& traceability (price-the-act.html, both figures) | projections index | pending, after merges | — |

**Unchanged, as chartered:** the measure note's related-work section remains queue head for
paper work; the M3/M4 principal decisions remain open and Emil's; `00`:158 and other carried
items remain separate; the MDL correspondence remains projected pending its falsifiers.

**Open at GATE H:** the Wave-2-proposed falsifier/test lines on `DDD-frame-12` and
`DDD-cost-22` (flagged in their notes, awaiting strike-or-amend); the `core/06` compound
section observed as un-carved diachronic material upstream (flagged at GATE B, no ruling
sought — future charter application); pins staged at 26 against the upstream branch head, to
be bumped to the merge SHA/tag on acceptance, upstream-first.
