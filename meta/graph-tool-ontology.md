# Graph tool — ontology sketch

**Status.** The architecture is settled: a sibling on `product-core` with its own ontology, not an
extension of `product-cli`'s What/How vocabulary. The entity split below is settled in principle;
everything past §3 is projected design — **flag-additions applies throughout; strike what is wrong.**

---

## 1. Two entities, not one

The tool models **claims** and **decisions** as distinct node kinds. The distinction: claims are
epistemic, decisions are volitional.

| | **Claim** | **Decision** |
|---|---|---|
| What it is | A truth-apt proposition about the world, the product, or the framework | A resolution of declared alternatives, made in order to act |
| Lifecycle | Status transitions — projected → reported → established, or → retired — driven by evidence | An event: made by a principal at a time; later superseded or revisited, never falsified |
| How it fails | Its falsifier fires; it demotes | Its basis erodes, or a better resolution supersedes it |
| Verb | *Tested* | *Made* |
| Framework mapping | Governed ground — the statused, curated portion of what decisions consume | The framework's original primitive: a declared outcome-relevant alternative under governance |

Claims are foundations; decisions rest on them and produce action. Bundling them — the ADR habit of
mixing "we believe X" with "therefore we chose Y" in one prose block — is what makes decision
records rot silently: the belief goes stale and nothing points back at the choice.

## 2. Node schemas

**Claim**

- `id` — stable, never reused (`DDD-<area>-<n>`)
- `statement`
- `status` — projected | reported | established | retired
- `evidence` — links to assets, computations, papers, observations
- `falsifier` — what fires it, and what breaks with it
- `changed` — version of last status change

**Decision**

- `id`
- `question` — the alternatives as declared
- `resolution` — what was chosen
- `commitmentLevel` — outcome | policy | principal
- `basis` — `basedOn` edges to claims
- `assurance` — mechanism by which acceptability is established
- `principal` — the accountable owner; required
- `made` — timestamp and context
- `reviewTrigger` — conditions that reopen it (a basis claim changing is always one)
- `supersedes` — optional edge to a prior decision

## 3. Edges

- `decision --basedOn--> claim` — the load-bearing edge
- `decision --supersedes--> decision`
- `claim --evidencedBy--> asset`
- `claim --refines / --contradicts--> claim`
- `projection --includes--> claim | decision` — manifests, unchanged from the way of working
- `actor --tests--> claim` and `principal --owns--> decision`

## 4. Rules (SHACL shapes, on product-core's validation machinery)

1. **No escaped decisions.** Every decision has ≥1 `basedOn` edge to a claim at or above the
   context's declared status floor, and exactly one accountable principal. Violation = the
   framework's central pathology, surfaced as a validation error. **The floor scales with
   commitment level** (Stable Dependency Principle, statused — `DDD-org-02`): outcome-level,
   cheaply reversed decisions may rest on projected claims; principal-level commitments require
   established or reported bases, or an explicit risk-acceptance flag naming the principal who
   accepts it. Accepted risk is legal; invisible risk is the violation.
2. **Demotion propagates.** When a claim's `changed` advances or its status drops, every decision
   with a `basedOn` edge to it is flagged for review; every projection including it is flagged
   stale. One SPARQL query each.
3. **Status floors per projection.** A projection's manifest declares its floor; including a claim
   below the floor without an explicit flag fails validation.
4. **Reproduction gates status.** A claim whose evidence includes executable assets cannot hold
   *reported* or above while any asset fails to reproduce.

## 5. Actors

Assignment follows the closure boundary, as settled in the way of working:

- **Checker-actors** where the acceptance predicate closes — run evidence assets, diff against
  stated values, demote on failure. Attributed: script, canon version, run.
- **Watcher-actors** — on dependency change, re-run affected falsifiers and staleness queries.
- **Escalation** where predicates are open — normative claims, correspondence claims, and every
  decision review route to the named principal. The tool never fakes a check it cannot make.

The MCP surface product-core already provides is the actor interface; agents author and test the
graph through it, exactly as `product-cli` agents author the What.

## 6. What this unlocks beyond the research repo

The claim/decision split is what carries the tool from research bookkeeping into operational work —
the org-design projection:

- An organisation's thesis is a claim subgraph; its strategy and product choices are decisions
  `basedOn` it.
- "Manifest discipline predicts pivot cost" becomes testable: the tool *shows* which decisions a
  changed thesis-claim invalidates, so re-deciding is deliberate rather than incident-driven.
- ADRs are the ancestor artifact: a decision record with its basis implicit. This ontology makes
  the basis explicit, statused, and queryable.

That projection stays parked per the way of working — but the ontology is designed so it costs
nothing extra when its time comes.

## 7. OPEN

- Whether `reviewTrigger` conditions beyond basis-change are worth modelling in v1, or noted as
  prose on the decision node.
- Namespace and vocabulary naming for the sibling ontology (working assumption: `ddd:` prefix,
  spec'd in Turtle beside the schemas).
- Whether decisions in the research repo itself (e.g. "sibling on product-core", "papers before
  tool") get backfilled as decision nodes on day one — recommendation: yes, they are the natural
  seed data and this conversation already contains their bases.
