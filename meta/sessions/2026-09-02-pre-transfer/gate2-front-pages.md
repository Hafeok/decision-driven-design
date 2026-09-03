# GATE 2 — the front pages read as a stranger would (I-2)

**Status: draft-pending-ruling. Findings only; nothing repaired.**

Method: both READMEs read in full against the graph at `v5.13.0` (upstream) and head (downstream);
every sentence tested against the primer §6 register — *a front page may say what the framework is
for; it may not say what it has shown unless a status carries it* — and against Paper A's
related-work survey. Line numbers are against the current files.

The status facts the findings rest on, fetched fresh:

| Assertion on a front page | Nearest carrying node | Kind | Status |
|---|---|---|---|
| the floor is in the acceptance predicate | `DDD-floor-02` | conceptual | **projected** |
| selection intensity tracks predicate closure | `DDD-hyp-05` | empirical | **projected** |
| demand is the Shannon entropy of the verdict (the identification) | `DDD-measure-01` | empirical | **projected** |
| conservation is the chain rule (the arithmetic) | `DDD-measure-02` | formal | established |
| overflow ∩ open is the mechanism of capacity-generated escape | `DDD-floor-01` | formal | reported (toy actors) |
| the hallucination account | none — exposition in `core/11` only | — | — |
| the immune-system instance | none — no claim carries it | — | — |
| the classical results' predictions change | none | — | — |

`spec/claim-format.md` §5: `established` is four claims, all `formal`; nothing empirical,
conceptual or normative has ever reached it; external validation exists nowhere.

---

## Downstream README (`decision-driven-design/README.md`)

**D1 — lines 30–32, the named over-claim, confirmed and wider than one line.**

> A third kind now exists: **non-deterministic, yet with a distribution that can be frozen by
> binding.** Decision-Driven Design is what you get when you **fill in the actor slot** those
> results left empty — and discover that supplying the missing parameter *changes their
> predictions.*

Two defects in one sentence. (a) "the actor slot those results left empty" and "the missing
parameter" are the absence claim the paper's retitle withdrew — *The Missing Parameter* was dropped
because it "claims absence from prior work the paper has not surveyed", and the survey then found
the neighbours (Hollnagel & Woods hold the arrangement-as-unit priority; Horvitz supplies an
allocation criterion the framework lacks). The paper's ruled formulation is "holding the determiner
**largely** fixed", with the contribution "stated against them rather than against their absence"
(abstract; §1 "usually held fixed"). (b) "changes their predictions" — no claim at any status
states that Brooks's, Tesler's, Ashby's or Meyer's predictions change; §11 says the opposite
discipline: "It does not claim their results as instances of its own."

**D2 — lines 25–26, the absolute absence claim.**

> **None of them makes that actor explicit.**

Scoped to the four named results, so it is the nearly-defensible form the retitle analysis
identified — but it is stated absolutely where the paper's ruled wording is "largely fixed" /
"usually held fixed". The survey supports the weaker form.

**D3 — lines 34–43, projected claims presented as consequences that follow.**

> Two consequences follow, and they are the framework's core contribution:
> 1. **The irreducible floor of a task is a property of its *acceptance predicate*, not of the
>    task.** Zero where you can check the answer; non-zero where you cannot; and *whether you can*
>    is, in general, undecidable.
> 2. **Selection intensity is inversely proportional to acceptance-predicate closure.** […] This is
>    falsifiable across professions.

Consequence 1 is `DDD-floor-02`, conceptual, **projected**. Consequence 2 is `DDD-hyp-05`,
empirical, **projected**. "Falsifiable across professions" is honest; "consequences follow" with no
status mark is not — a stranger reads two shown results.

**D4 — lines 45–48, the projected identification asserted flat.**

> for tasks whose acceptance predicate closes, **specification demand is measurable** — it is the
> Shannon entropy of the verdict, and conservation is the chain rule of entropy

The chain rule is `DDD-measure-02` (formal, established — arithmetic). The identification of the
framework's demand with verdict entropy is `DDD-measure-01` — empirical, **projected**. The
sentence asserts the identification as fact and leans it on the arithmetic: the identity-as-evidence
move canon forbids, on the front page.

**D5 — lines 14–17, "proven" and "harder to knock down".**

> It remains deliberately **smaller and better-attributed** than v3, and harder to knock down — and
> says exactly which of its claims are proven, exercised, or still projected.

"Proven" is not in the status vocabulary and describes nothing in the graph — §5 says `established`
is internal warrant, four formal claims, no external validation. "Harder to knock down" asserts
robustness no status carries. This is the sentence most likely to be quoted against the framework
verbatim.

**D6 — lines 84–86, "results" over four claims of which three are projected.**

> The load-bearing, falsifiable results — the floor is in the acceptance predicate, selection
> intensity tracks predicate closure, demand is the Shannon entropy of the verdict, overflow ∩ open
> is the mechanism of capacity-generated escape — all live upstream.

`projected`, `projected`, `projected`, `reported` (toy actors). "Falsifiable" is right; "results"
is not carried.

**D7 — line 80, stale front-page fact.**

> at the tag pinned in `graph/upstream.yaml` (`v5.5.0` at time of writing)

Seven releases stale (pin is v5.12.0 now; v5.13.0 after I-3). A wrong version on the front door of
a public repo, beside the file that is authoritative.

**D8 — lines 169–172, the debt declared paid on a projected identification.**

> The counting-procedure debt — a measure of governing-decision demand **shown invariant** — is
> **paid** for closing predicates by the measure (`core/09`, `DDD-measure-01`/`02`/`06`)

"Shown invariant" holds of the arithmetic (`DDD-measure-02`, established) only through the
identification (`DDD-measure-01`, projected). "Paid" asserts discharge the projected claim cannot
carry.

## Upstream README (`actor-indexed-determination/README.md`)

**U1 — lines 105–121, "the central result" is a projected claim.**

> ## The central result: check the work or check the worker
> The framework's most important result concerns the **acceptance predicate** […]
> **The floor is non-zero exactly when, and because, you cannot check the work.**

Carried at `DDD-floor-02` — conceptual, **projected**. "Result" twice, no status mark anywhere in
the section. The definitional content around it (what closure means) is the framework's own and
fine; "result" is the over-read.

**U2 — line 123, an empirical explanation asserted as succeeded.**

> This explains why organisations use licences, qualifications, grades, track records,
> certification, institutional standing, and selection.

The explanatory claim about real institutions is at best `DDD-hyp-05` (empirical, **projected**).
"Explains" reports an explanation as achieved; "would explain" or a status mark is what the graph
supports.

**U3 — line 320, a mechanical account of hallucination.**

> This also yields a mechanical account of one class of hallucination: output decoupled from
> correct ground because that ground is absent, false, or present but unresolved.

No claim carries a hallucination account at any status. The nearest node, `DDD-floor-01`, is
`reported` on toy actors and says nothing about models' hallucination. A real-world phenomenon is
presented as accounted for.

**U4 — lines 356–366, "tested", and the two front pages disagree with each other.**

> The actor-general vocabulary is tested against the vertebrate immune system.
> The mapping is not intended as metaphor: […]
> The immune system matters because no engineer specified it. If the framework's categories only
> worked for deliberately engineered systems, the actor-general claim would fail here.

No claim carries the immune-system instance at any status; "is tested" reads as a performed and
passed test, and the closing sentence frames it as a survived falsification attempt. Worse: the
**downstream README's own "What changed from v3"** records "the immune-system 'licensing' argument
is **demoted to a suggestive parallel with known disanalogies**". One front page demotes what the
other presents as a load-bearing worked instance — an outside reader can quote the two against each
other.

**B1 — borderline, reported for the ruling rather than asserted as a defect.** Upstream line 7:
"It applies to any arrangement that determines choices against ground: programs, models, humans,
organisations, markets, immune systems, and compositions of them." Read as purpose ("is for
analysing"), this is the primer-§6-legitimate kind; read as an applicability assertion, its
universality is `projected` (`DDD-frame-01`'s enumeration). The same sentence-form question governs
several purpose-adjacent lines in both files.

**What is already right, for calibration.** Upstream: "These hypotheses are **projected**, not
reported findings"; the "What this framework does not claim" list; the Register section; "toy
demonstrations are not presented as external validation". Downstream: "We publish the review and
the retreats as first-class documents." The repairs should converge on this register — it already
exists in both files.

## Proposed repair shape (for the ruling; not executed)

Per the charter: **repair over-claims, do not rewrite**. Each finding repairs in place — the
sentence keeps its position and its purpose:

- D1: replace with the paper's ruled formulation (fill in the actor slot the results "hold largely
  fixed"; drop "missing parameter" and "changes their predictions" — what is supported is that the
  framework *indexes* their questions, §11's wording).
- D2: "None of them makes that actor explicit" → the paper's "each holds it largely fixed".
- D3, D4, D6, U1, U2: add the status in place (the primer's device: assert-with-grade), and
  "results" → "claims"/"the framework's central claim" where projected.
- D5: "proven, exercised, or still projected" → the actual vocabulary; drop "harder to knock down".
- D7: repair with I-3's pin advance (one edit, the correct version, or point at the file without
  naming a version so it cannot go stale again).
- D8: "shown invariant" → the identity holds under the projected identification; "paid" → scoped to
  what measure-02 carries.
- U3: mark as the exposition it is ("suggests a mechanical reading of one class of hallucination",
  or carry `DDD-floor-01`'s status and region).
- U4: align the two front pages — either the upstream section adopts the demoted register
  ("suggestive parallel, disanalogies recorded") or Emil rules the demotion itself superseded by
  core/12; the two files must say the same thing. ("Tested" → what core/12 actually does, at its
  actual grade.)
- B1: Emil rules the sentence-form question once; the same ruling covers its instances.

**HOLD at GATE 2 — awaiting Emil's ruling on the findings and the repair shape.**
