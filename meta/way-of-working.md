# Way of working — Decision-Driven Design

**Purpose.** Canonical description of how work on the framework is structured, where it lives, and how
it flows. This file governs the repo and every project that projects from it. Settled unless marked
OPEN. Where this file and older material disagree, this file wins.

**Intended location.** `meta/way-of-working.md` in the `decision-driven-design` repo. A copy serves as
the base context file for any working project.

**Post-split note (`DDD-dec-04`).** The **framework** layer — the `core/` documents, the term graph,
and `core/assets/` — is now canon in the principle repository (`actor-indexed-determination`, split
at tag `v5.0.0`; the live pin is in `graph/upstream.yaml`). Every `core/NN` and `core/assets/…`
reference below is descriptive of that upstream layer, not a local path in this repository; this repo holds the **program** and the **projections**, and
consumes the framework by pin (`graph/upstream.yaml`). `meta/lineage-and-limits.md` also lives
upstream now.

---

## 1. The model

The work is a graph, not a set of documents. Files are a storage format; the graph is the object.

Three layers:

| Layer | What it is | Where it lives |
|---|---|---|
| **Framework** | The claim graph — every claim the framework makes, with status, evidence, falsifiers, and version | `core/` |
| **Program** | The interrogation of the framework — which claims need what kind of test, which debts are booked, which paper pays which | `meta/` |
| **Projections** | Rendered views of the graph for an audience — papers, engineering guides, org-design notes, product material | `projections/` |

The core thesis is worked out through the flow between them:

> **repo → program** (audit: what does each claim need) **→ projection** (establish or falsify)
> **→ repo** (canon revision) **→ re-render stale projections.**

This loop has already run once. The date-validation computation, done inside a projection effort,
overturned the canon claim that a better decomposition "destroys demand." The canon updated; the
language retired. The loop is now first-class rather than accidental.

---

## 2. Claims

A claim is a node. Every node carries:

- **an identifier**, stable across versions;
- **a status** — see vocabulary below;
- **evidence**, or the absence of it, stated;
- **a falsifier** — what observation would break it, and what breaks with it;
- **the version** at which it last changed.

Edges are derivation, dependency, and correction-flow. At current scale the graph is markdown with
consistent claim IDs and a disciplined convention, not tooling. Build tooling only when grep stops
being a sufficient query engine.

**Status vocabulary**, applied uniformly:

| Status | Meaning |
|---|---|
| **established** | Proven or theorem-backed on a stated region (e.g. conservation on closing predicates — the theorem is Shannon's, the identification is ours) |
| **reported** | Exercised with evidence; computations reproduce |
| **projected** | Clean derivation, unexercised; ships with a falsifier |
| **retired** | Overturned or shown not to follow; kept in the graph with the correction that killed it |

Retired claims are not deleted. The correction history is part of the framework's evidence that the
loop works.

---

## 3. Projections

A projection is a filtered, re-registered view of the graph, pinned to a canon version. The
measure-paper context file is the type specimen: *"Projection of `decision-driven-design` at v4.4,
principally `core/08`."*

**Two axes define a projection:**

1. **Filter** — which region of the graph, and which **status floor**. Academic projections may
   include projected claims, because papers exist to test them. Practice-facing projections
   (engineering, organisational, product) filter to established and reported, or flag projected
   claims loudly. Nobody makes a working decision on an unproven hypothesis without knowing it.

2. **Register** — the same node renders differently per audience. One node, three renderings:
   - *Formal:* conservation is the chain rule on the closing region.
   - *Engineering:* you cannot decompose your way out of the work; a cleaner split moves cost into
     the interface contract, so budget for the seam.
   - *Organisational:* when you split a team, the coordination knowledge moves into whoever owns the
     boundary — make that a named role.

**Every projection carries a manifest:**

- source canon version;
- the claim IDs it includes;
- audience and register;
- date rendered.

The manifest is what makes staleness mechanically detectable: a projection is stale when any included
claim has changed since the pinned version. Which projections cite claim X, and which predate its
last change, is a grep.

**Projections are never edited in place.** When a claim changes, each stale projection gets one of
three treatments:

| Treatment | When |
|---|---|
| **Re-render** | The projection is live and the change matters to its audience (arXiv v2, updated guide) |
| **Annotate** | The artifact must stand but readers need the correction (erratum note) |
| **Let stand** | The projection is a timestamped historical claim — published papers are allowed to say what was true at v4.4 |

The one forbidden move: changing a projection without touching the canon. That makes the projection a
second source of truth, which is the failure mode this whole structure exists to prevent.

**Corrections flow upward.** Work done inside a projection that changes a claim lands in `core/`
first, then re-projects. The repo is ground truth, always.

---

## 4. The program

`meta/` holds the program layer: the generalisation of `lineage-and-limits.md` from one booked debt
to all of them. For each claim that is not established: what kind of test it needs, which projection
owns it, and what it would cost.

**The paper roadmap, in dependency order:**

| # | Paper | Establishes | Status |
|---|---|---|---|
| 1 | **The measure note** — *Specification Demand Is Verdict Entropy* | Conservation as a theorem on the closing region; the boundary as principled | Draft complete; finish list below |
| 2 | **The correspondence study** | Whether `I(V;S)` predicts interface cost and `I(V;E)` predicts unaided performance — converts the measure from well-founded to measured | Protocol specified in paper 1; not run |
| 3 | **The escape/judgment split** | The actor-capacity model cleaving `H(V\|X)` into resolved and escaped; the floor mechanism. Likely home of the rate–distortion material (`core/10`) | Named as next formal result; not started |
| 4 | **The arrangement study** | H1–H5 — operational evaluability predicting comparative advantage across system arrangements | Furthest out; needs collaborators and data |

**The graph tool** sits beside the papers, not among them — it is infrastructure that is itself a
projection of the framework:

| Stage | What | Status |
|---|---|---|
| **MVP** | Claims file with IDs and statuses; YAML-front-matter manifests on projections; CI job running `core/assets/measure-*.py` (fail → demote) and grepping for stale manifests | Sketched in `meta/graph-tool-mvp.md`; an afternoon; **after paper 1 ships**. May be absorbed by the full tool given the foundation below |
| **Full tool** | Actor-assigned claim testing: checker-actors where predicates close, watcher-actors running falsifiers on dependency change, escalation to a named principal where predicates are open; staleness actor opening re-render decisions | **Projected — claim `DDD-tool-01` below.** Foundation inventory done: `product-cli` covers graph store (YAML/Turtle), rule enforcement (SHACL + SPARQL), actor surface (MCP + agent sessions), live views. Remaining work is a schema-and-rules layer, not an engine |

**Settled — architecture.** The tool is built **as a sibling on `product-core`**, with its own
ontology; it does not extend `product-cli`'s What/How vocabulary. Claims and decisions have a
different lifecycle from commands and events, and coupling the framework graph to the product tool
would tie two release cadences together. We need our own.

**Settled — the ontology has two operational entities, not one:**

| | **Claim** | **Decision** |
|---|---|---|
| Nature | Epistemic — truth-apt | Volitional — made in order to act |
| Lifecycle | Status transitions: projected → reported → established, or → retired | Event: made by a principal at a time; later superseded or revisited, never falsified |
| Verb | Tested | Made |
| Carries | Status, evidence, falsifier, changed-version | Alternatives, resolution, commitment level (outcome/policy/principal), basis, assurance mechanism, accountable principal |
| Framework mapping | Governed ground — the statused portion of what decisions consume | The framework's original primitive |

The load-bearing edge is `decision --basedOn--> claim`. Consequences:

1. **Escaped decisions become SHACL-detectable** — a decision lacking a basis at the required
   status floor, or lacking a principal, fails validation. The framework's central pathology as a
   machine check.
2. **Claim demotion propagates into operations** — a staleness query returns every decision resting
   on a changed claim; the operational analogue of stale projections, and the mechanism the
   org-design thesis needs to be testable.
3. **ADR lineage** — an ADR is a decision record with the basis implicit; this ontology makes the
   basis explicit and statused.

Detail in `meta/graph-tool-ontology.md`.

The tool instantiates the framework's own closure boundary: mechanical actors exactly where
acceptance closes, human escalation exactly where it does not. Its accountability must be complete —
every automated verdict attributed (script, canon version, run) and owned by a principal — or the
tool becomes a source of escaped decisions about the framework itself.

Claim node, stated with its falsifier per convention:

> **`DDD-tool-01`** *(projected)* — An actor-assigned claim graph reduces the cost of exercising the
> framework: canon changes propagate to affected projections without manual tracking, and claim
> demotions are detected mechanically rather than by re-reading. **Falsifier:** after one full
> canon-revision cycle with the tool, staleness detection or demotion still requires manual audit,
> or tool maintenance exceeds the audit cost it replaces. **What breaks:** nothing in `core/` — the
> tool is a projection; if it fails, the discipline reverts to convention and grep.

**Paper A** (*Actor-Indexed Determination*) is not a paper on this roadmap. It
is the program's conceptual material. The foundation-revision document is quarried, not completed:
its claim-status table and hypothesis structure move into `meta/`; its manuscript prose waits. A
synthesis paper may exist eventually — written last, organising results rather than proposing
vocabulary, and only if papers 1–3 give it results to organise.

---

## 5. Repo structure

```
decision-driven-design/
  core/           the claim graph — canon, versioned
    09-the-measure.md
    assets/measure-*.py        computations are canon assets; they reproduce or the claim demotes
  meta/           the program
    lineage-and-limits.md      booked debts (the original)
    way-of-working.md          this file
    research-program.md        claim audit: status, owner-paper, cost   [to create, from the Paper A material]
  projections/    rendered views, each with a manifest
    measure-paper/             paper 1: draft, context file, manifest
    ...                        future: guides, org notes, product material
```

**Projects** (working sessions, wherever they run) are scoped to one projection or one canon change.
A project's context file is the projection manifest plus working conventions. Fetch the live repo
before producing file changes; the repo is ground truth and the project copy is not.

---

## 6. Working conventions

Carried over from the measure-paper project; now repo-wide.

- **Derivations over assertions.** Every projected claim ships with a specific falsifier and a note
  on what breaks with it.
- **Arithmetic and model are never fused.** An identity holding is reported as arithmetic; the
  identification is projected as a model. State which, always.
- **Credit first.** Borrowed theorems are named before the claim that uses them. The theorem is
  Shannon's; the identification is ours. "Principle," never "law," as self-reference.
- British spelling. One idea per sentence. Tables for structures, prose for arguments.
- Notation stated once and used exactly.
- **Flag additions** — reasoning Emil has not confirmed is marked so it can be struck.
- Computations that back a reported claim live in `core/assets/` and must reproduce; a claim whose
  computation fails to reproduce demotes until fixed.

---

## 7. Current state and immediate work

**Paper 1 finish list** (the only work gating anything):

1. Related-work section + references — the one real gap. Must answer the Kolmogorov/MDL objection
   (why entropy: distribution-relative and computable) and position against the information
   bottleneck. Credit Shannon first; Ashby as the ancestor with the unit.
2. Soften §7: claim a *principled* boundary, not "strongest available evidence" — the measure
   vanishing on open predicates is near-definitional, and the honest claim is that the boundary is
   not arbitrary.
3. Optional but cheap: one chained-seam instance on the date task, to blunt the "three instances,
   two tasks" objection.
4. Reproduction pass: re-run all three scripts against the submission text.
5. Post to arXiv; solicit the information-theorist review with the preprint. arXiv is revisable —
   certification is a v2 improvement, not a gate.

**Then:** extract `meta/research-program.md` from the Paper A material (an hour of restructuring,
not writing), file the foundation-revision document as quarry, and the program is fully in the shape
this file describes.

---

## 8. OPEN

- Whether the chained-seam instance goes into paper 1 before first posting or into v2.
- Claim-ID convention: adopt one before writing `research-program.md` (proposal: `DDD-<area>-<n>`,
  e.g. `DDD-measure-01`; cheap to change now, expensive later).
- Whether `projections/` holds rendered artifacts or manifests-plus-pointers when the artifact lives
  elsewhere (arXiv, a published guide). Position: manifest always in repo; artifact wherever it must
  live, with the manifest recording where.
