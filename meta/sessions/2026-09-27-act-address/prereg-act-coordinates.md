# Pre-registration — the act address ruling

**Revision 3, 2026-09-27.** Revision 3 supersedes revision 2 with rulings R-4 to R-6 and the reuse finding in §3.3. Revision 1's correction record is carried unchanged in §1.

**Status.** Fixed 2026-09-27. This document is the discipline boundary. Results go in a separate document and never edit this one. Nothing here is filed. Emil is sole ratifier.

**Code name.** Phoenix is the first customer engagement (six weeks from October 2026). It is referred to by code name only.

**Layer.** Actor-general. The ruling belongs upstream in `actor-indexed-determination`.

**Basis read.** Both repos, cloned 2026-09-27: `DDD-frame-01`, `DDD-floor-02`, `DDD-ground-01` (projected), `core/04` (settled), `core/06`, `core/14`, corpus test results 2026-08-14, ground-axes holding note rev 18 (unratified).

---

## 0. Rulings recorded (Emil, 2026-09-27)

| # | Ruling |
|---|---|
| R-1 | Correction record accepted. |
| R-2 | The candidate under test is D. A and C are retired from the run, and their predictions stay on record in §5. |
| R-3 | T2 is to be supplied by Emil. |
| R-4 | Time is accepted as a second, causal index beside the address (§3.1). |
| R-5 | The layer path is accepted as part of the address (§3.2). |
| R-7 | Coincidence is defined on the ground-position component. Behaviour is read at two grains: full address within one parent, and ground position across parents (§3.3). |
| R-8 | T2 is split into T2a (retry-count, dry run) and T2b (first Phoenix slice, independent test). |
| R-6 | Every act occurrence is unique, and occurrences may coincide on the same address. Reusing one piece of code for several acts is an implementation optimisation, not the truth about the acts. The act map is therefore a tree of occurrences, and reuse lives in the derivation layer, not in the address space. |

## 1. Correction record (carried from revision 1)

| # | What was proposed | What the repo says | Consequence |
|---|---|---|---|
| C-1 | Pinning resolution and behavioural-sameness resolution may both be τ | `core/04` (settled) defines pinning resolution as an actor-side property. τ is task-side. | Withdrawn. Moved to `[OPEN]` in §7. |
| C-2 | Candidate C, the tuple minus the arrangement | The tuple indexes a determination problem, not an act. `DDD-ground-01` anchors decisions to acts through applicability predicates. | C fails one-address-per-act. D was added. |

Cause: Claude reasoned from the project projection before fetching the repo.

## 2. Criteria

| # | Criterion |
|---|---|
| K1 | Each act occurrence has exactly one address |
| K2 | The address excludes the occupant, so behaviour is comparable across actors |
| K3 | The address is the act's ground address, and acts are retrieved by it |
| K4 | No contradiction with `DDD-frame-01` or `DDD-ground-01` |
| K5 | Behaviour stays definable: recurrence must be possible at a fixed address |

K5 is new in this revision. It is added because of the weakest point of the time extension (§3.1).

## 3. D and its two extensions

**D (ruled into the test).** An act's address is its position on declared ground axes, extracted at the act-site. Decisions anchor through applicability predicates. Actors anchor as occupants.

### 3.1 Time — Emil's extension, `[PROPOSED]`

> The address plus the distance in time makes a real map. Two acts sharing an address will have two different time addresses if they are dependent.

**Weakest point.** If time enters the address itself, every act occurrence gets a unique address. Then nothing recurs at a fixed address, and behaviour, which is defined as recurrence at the same address, disappears. That violates K5.

**Proposed resolution** (Claude, flagged): time is a second index beside the address, not a component of it. The address says *where*. Time says *when, and after what*. Behaviour is read along the time index at a fixed address. This keeps K5 and gives exactly the map Emil describes.

**Proposed form of the time index** (Claude, flagged): the time index should be causal position, not wall-clock. Dependent acts are ordered by dependency. Independent acts at the same address are concurrent and may share a time position. This is a partial order, which is what an event stream already records. Wall-clock distance is derived from it, not the other way round.

**Relation to the holding note.** Rev 18 argues that time is weak as a coordinate, because each ground axis ages on its own clock. That argument is about the age of the *ground*. The extension is about the *act's* position in dependency order. These are different objects. `(UNVERIFIED — Emil review: that the two do not conflict.)`

**What it buys in the method.**
- Invalidation fan-out becomes a query: the acts after a superseded decision in causal order, at addresses its predicate matches.
- As-of decay has an anchor: the distance from the act to the reading of each ground axis.

### 3.2 Layering — Emil's extension, `[PROPOSED]`

> By using the composite nature of the model we can use the layering of acts to add a dimension to the address.

**Proposed form** (Claude, flagged): the address becomes ⟨layer path, ground position⟩. The layer path records the chain of composite acts that the act sits inside. Unlike time, layering is spatial, so recurrence survives: the same sub-act under the same parent recurs at one address. K5 holds.

**What it buys.** `core/06` holds that decomposition manufactures seam decisions about how the parts coordinate. Without a layer, a seam decision has no act of its own to anchor to, so under D it would be flagged as a candidate escape. With a layer, it anchors at the parent act. The measure paper's seam, `I(V;S)`, then has an address.

**Shared sub-acts — ruled (R-6).** The act map stays a tree of unique occurrences. Where two occurrences look like "the same act", that sameness is coincidence on an address, or reuse in the code. Neither makes them one act.

**Second weak point.** The layer path depends on the decomposition, which is itself a decision (`S`). The same work decomposed two ways gets two sets of addresses. Proposed handling: the addresses are relative to a ruled decomposition, and re-decomposition proceeds by supersession.

### 3.3 Reuse as a mechanism — consequence of R-6

**Emil's observation.** One act often demands a change to a single function, and that change incurs sudden changes in hundreds of other places. The mechanism is exactly the reuse that R-6 moves out of the address space.

**Development** (Claude, flagged). Derivation runs forward: acts declare ground requirements, which pull components. Reuse is many occurrences pulling one component. That component is a seam spanning every occurrence that pulled it. By the ruled seam result, such a seam decays at the conjunction of k persistence probabilities. A function shared by a hundred acts is therefore a very fragile seam, and the theory already predicts that.

When one act's decision changes the shared component, the decision is anchored at that one act's address. Its effect lands at every other occurrence that pulled the component. No applicability predicate covers those other occurrences, so the effect is an escaped decision crossing act addresses. That is the channel `theory.md` says behaviour change detects.

**What it buys in the method.**
- The fan-out of a component change becomes a forward query: the occurrences that pulled the component. It is no longer discovered in production.
- The query result can be shown to the person changing the component before they change it.
- Reuse becomes a priced design choice. It amortises demand but concentrates seam risk, and the map shows both.

**The grain question.** R-5 puts the layer path in the address. So two occurrences under different parents have different full addresses, even when their ground positions are equal. "Coincide on the same address" then needs a grain.

`[PROPOSED]` (Claude): coincidence is defined on the ground-position component. Behaviour can then be read at two grains:
- At full address, within one parent, which shows how an act behaves in its composite.
- At ground position, across parents, which is where the hundreds-of-changes effect appears as simultaneous behaviour change.

`[OPEN]` for ruling.

## 4. Cases

| Case | Content |
|---|---|
| T1 | Date validator, `(M,D)` over `M ∈ {1..4}`, `D ∈ {1..31}`, three occupants, and decompositions A (by month) and B (by day) |
| T2a | `[PROPOSED]` The retry-count worked example in `projections/tracks/01-determination.md`: a retry policy reused across clients, with a model proposing the count when scaffolding. It can be run now as a dry run. Its weakness is that it was written inside the framework, so it may fit by construction. |
| T2b | The first slice of Phoenix, pseudonymised. It does not exist yet, and its act map is itself produced by method step 1. Its predictions are fixed here before the slice exists. That makes it the independent test. |
| T3 | Architecture sign-off for the T2 slice: an open-predicate act |

## 5. Predictions

Each prediction is marked either analytic (follows from the definition) or empirical (can surprise).

**D with both extensions:**

| | T1 | T2 | T3 |
|---|---|---|---|
| Address | One address at the parent layer, with three occupants. *Analytic.* | Every act occurrence gets exactly one address. *Empirical.* | The address is declarable but low-information. *Empirical.* |
| Layer | The day-29 split in decomposition B anchors at the parent layer. It would be an unanchored escape without the layer. *Analytic.* | At least one seam decision would be unanchored under plain D and is anchored by the layer. At least one component is pulled by two or more occurrences, and its fan-out is computable forward from the derivation record. *Empirical.* | Sign-off sits at the slice's parent layer, above the acts it approves. *Empirical.* |
| Time | Not exercised. | At least two dependent acts share an address and are separated only by time. *Empirical.* | Successive sign-offs share one address and are distinguished by time. A ground shift appears as a behaviour change along time only if readings are recorded. *Empirical.* |

**Retired candidates, on record:**
- A: fails K2 by construction.
- C: fails K1 on T2 wherever an act resolves two or more decisions.

## 6. Falsifiers

| Falsifier | What it breaks |
|---|---|
| An act whose governing set cannot be computed from its address plus the decision predicates, without verdict content | The address/readings split |
| Two occupants at one address that must declare different ground axes | K2 |
| The same act landing on two addresses through mapping choice alone, within one ruled decomposition | K1 |
| Two dependent acts whose order cannot be recovered from the record | The time index as causal position |
| A seam decision that anchors at no layer even with the layer path | The layering extension |
| A component change whose affected occurrences cannot be computed forward from the derivation record | §3.3; reuse would not be recoverable from the map |
| Two occurrences at the same ground position whose behaviour is incomparable across parents | The ground-position grain in §3.3 |

## 7. Open, not tested here

- The relation between pinning resolution (actor-side) and τ (task-side) in fixing the grain of behaviour.
- The term for the address. `[PROPOSED]` "act address", with "time index" and "layer path" for the two extensions. Registry entries are needed.
- The declared-space limit of `DDD-ground-01`, which is carried forward.

## 8. Rulings needed before the run

None. T2's predictions in §5 apply to both T2a and T2b.
