# Changelog

## 4.1 — The measure

The measure — specification demand is verdict entropy, conservation is the chain rule
(closing-predicate case); funnel/maturation corrected to judgment-demand projections; Danish
glossary.

### Added
- **`core/07-projections.md`** — the funnel and maturation, corrected: both are **judgment-demand** (cost) projections, never *count* projections; explains the reference model's spurious feedback loops. Figures: `core/assets/projections.svg` (static), `core/assets/projections.html` (interactive).
- **`core/08-the-measure.md`** — **the formal result**: for tasks whose acceptance predicate closes, specification demand is the Shannon entropy of the verdict, and conservation is the chain rule of entropy. One identity, three conditioning variables (decomposition → seam, actor → allocation, retrieval → RAG). Reproduction scripts (stdlib-only): `core/assets/measure-toy.py`, `core/assets/measure-actor-allocation.py`, `core/assets/measure-rag.py`.
- **`i18n/ordliste-dansk.md`** — Danish glossary of the framework vocabulary.

### Changed
- **The counting-procedure debt moves from open to partially discharged.** For closing predicates, demand is measured (verdict entropy) and conservation is the chain rule — a *measured* invariant on the closing-predicate region. It remains open for open predicates, where the verdict function does not exist — the same boundary as the floor. See `meta/consolidated-state.md` §5.
- The register is unchanged: still a **principle**, not a law. `core/08` strengthens how well the principle is grounded on the closing-predicate region, but the measure exists only where the predicate closes, so the general claim remains a principle.

### Corrected
- *"A better decomposition destroys demand"* — a better decomposition *pre-pays* more demand into the seam, buying cheaper parts; the total is invariant. Nothing is destroyed; it relocates. See `core/08` §4.
- The funnel as a *count* projection — it is a *judgment-demand* (cost) projection; count is fixed by the task. See `core/07`.

### Open debts (booked, not hidden)
- The judgment/escape split: `core/08` folds escape into judgment; separating them needs an actor-capacity model — the natural next result.

## 4.0 — The theory layer, and the register correction

### Added
- **`core/`** — the actor-general theory beneath the framework:
  - `00-determination` — two primitives (decisions, ground); the admission tests; *the act is a decision*
  - `01-the-principle` — conservation of determination demand; the four stores; the principle-not-law register
  - `02-completeness` — exhaustiveness of the stores, and its definitional (non-empirical) status
  - `03-the-floor` — **the floor is in the acceptance predicate** (best original result)
  - `04-actors` — **the missing parameter**: pinning, selection-vs-training, seams, the compound
  - `05-composition` — seam-demand identity; orchestrator vs. swarm; the channel is the platform
  - `06-determination-and-intelligence` — determination ≠ intelligence; the debate is structurally undecidable
- **`apparatus/`** — encode/verify, the closure principle (poisoned ground), adversarial ground
- **`meta/`** — lineage-and-limits and consolidated-state: attribution, corrections, retreats, open debts
- Full attribution to Tesler, Ashby, Brooks, Meyer/Hoare, Saltzer/Reed/Clark, Kalman, Polanyi/Collins, Rice, Edelman & Gally

### Changed
- **The v3 framework is now the SDLC projection.** The four design docs move to `applications/sdlc/` as the *engineering projection* of the general principle. Not deprecated — repositioned.
- **"Law" → "Principle."** No physical-law status is claimed; there is no measurable unit. "Law" appears only as homage (Tesler's, Ashby's), flagged as such.
- **Conservation** restated in its defensible form: an accounting identity *within a fixed decomposition*. Re-decomposition can destroy demand, so the decomposition is the highest-leverage decision.

### Corrected (following external adversarial review)
- **Zero-floor postulate** retreated to **the floor-in-the-predicate** — bounded by Rice's theorem, inevitable model error (Xu et al.; Kalai & Vempala), and Collins's collective tacit knowledge. Determinism does not lift these (they are about decidability, not predictability).
- **The immune system** demoted from "licensing instance" to suggestive parallel with known disanalogies (negative selection is leaky, not a mechanical check; innate/adaptive is a continuum). **CRISPR** is the accurate compound-platform instance.
- **"Diversity vs. redundancy"** → **degeneracy** (Edelman & Gally 2001).
- **Poisoned-ground cross-domain unification** retreated to *a family, not one mechanism* — opposite error directions (autoimmunity vs. mimicry vs. TOCTOU) must not be conflated.
- **"There is no tacit knowledge in digital work"** retired as indefensible against Collins.

### Retired / refused
- The quantum/quark extension (fails the admission tests — the resemblance is degeneracy, a fact about many-to-one maps, not determination).
- The claim that the framework proves LLMs are (or are not) intelligent. It proves the question, as posed, is **undecidable**, and maps where a verdict could come from.

### Open debts (booked, not hidden)
- A counting procedure for governing decisions, shown invariant across two architectures — the thing that would make "conservation" measurable rather than asserted.
- An operational measure of predicate closure (proposed proxies: time-to-feedback, objectivity, stationarity).
- The selection/training ratio tested across professions (falsifiable from existing literature).
