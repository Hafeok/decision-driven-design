# Session prompt — the freight session

Repositories: `actor-indexed-determination` (upstream, head — canon at **v5.5.0** plus the merged
addendum commit), `decision-driven-design` (downstream, head), and `product-cli` (**one item only**,
G-7 below; otherwise untouched). Fetch all three.
Session type: **interactive canon curation.** Hold at every gate. Supersession, never rewriting
(precedent: DDD-dec-09/10/15). British spelling; one idea per sentence.

## What this session is

The accumulated small-items list — every deferred repair, seam, annotation, and ruled-but-unfiled
item recorded across the escape, corpus, and vocabulary sessions. Many items, mostly small, several
touching ratified text. **Nothing here is new design work**: every item below was found and recorded
in a prior session (source named per item); this session executes and closes them. Where an item
turns out larger than its booking, flag and defer rather than expand — the one exception is Batch C,
which is known-large and gated accordingly.

**First act, before Gate 1:** create `meta/sessions/` in `decision-driven-design` and commit this
prompt and its bootstrap into `meta/sessions/2026-08-17-freight/`. That inaugurates the convention
this session files at Batch E — the session's own prompt is the convention's first instance.

## The manifest, batched by repair family

### Batch A — prose and reference repairs (upstream unless noted)
| Item | Source |
|---|---|
| A-1 `core/11` §7 prose says **four** instances; `DDD-dec-15` records **five**. Align prose to the claim file | ground-axes note rev 9 (its follow-up F4) |
| A-2 `core/09` §6 carries the identity form "escape = overflow ∩ open"; correct to the capacity-generated scope | escape session Gate 4 |
| A-3 `core/README:23` same identity form in the index line | escape session Gate 4 |
| A-4 `meta/consolidated-state.md` — two defects: identity form, and describes the escape/judgment split as unstarted | escape session Gate 4 |
| A-5 `meta/lineage-and-limits.md` — verify the novelty statement correction landed at v5.4.0; repair if the escape session's edit missed any adjacent line | escape session Gate 4 (partially done) |
| A-6 Six stale `core/10` references in downstream apparatus docs (tool-contract ×2, tool-surfaces ×3, prefix-stability) — mechanism lives in `core/11` | escape session Gate 1, discrepancy 3 |
| A-7 Downstream `CLAUDE.md` names canon pin at v5.0.0; live pin is v5.5.0 | escape session Gate 1, discrepancy 3 |
| A-8 `v5.3.0` changelog gap upstream | escape session close |
| A-9 `DDD-cost-03` notes cite cost-05's old denomination — one-line transitive repair | escape session Gate 4 |

### Batch B — registry seams and term repairs (upstream)
| Item | Source |
|---|---|
| B-1 `term:closure` vs `term:verdict`: verdict's canonical text still reads "decidable acceptance predicate" where closure reserves *decidable* for the formal special case. Align verdict's text to operational closure | measure revision session, D-2 |
| B-2 `term:acceptance-predicate` (evaluates an outcome) vs `term:verdict` (assigns the correct output per input point) — two objects in one registry. Reconcile: predicate evaluates pairs; verdict is the induced assignment where the task class supplies one; cite the paper's §2.2 task classes as the settled account | measure revision session, Gate 5 |
| B-3 `term:exhaustiveness` ("exactly one of") vs `core/02:78` defence-in-depth licence ("a constraint before and a criterion after"). Reconcile: exhaustiveness quantifies over the determination; defence-in-depth over carriers of it. One clarifying clause, either site | corpus test, Gate 2 |
| B-4 General rule: establishing a term ID that collides with the pinned upstream registry requires an explicit decision reference; silent shadowing becomes a validator **warning class**, suppressible only by citing the governing decision | term:maturation ruling (2026-08-10) |

### Batch C — the diachronic carve (upstream; the session's one large item)
| Item | Source |
|---|---|
| C-1 Carve the un-carved diachronic material in `core/06` (compound section) and `core/08` per R4, supersession pattern (Wave-1 precedent). Scope **explicitly includes** `core/08`'s establishment of `term:maturation` ("the compound over repetition"), which retires or re-words without the term; downstream's establishment ("the return channel") becomes sole. Record the shadow's resolution per the 2026-08-10 ruling: deliberate in destination, escaped in mechanism, known-and-temporary — now closed | Wave-2 close flag + term:maturation ruling |
| **Gate rule for C:** propose the carve plan (what moves, what re-words, every embed re-projection) before cutting anything; if the plan exceeds a session-day's remaining budget, Emil rules defer-whole — no partial carve | — |

### Batch D — measure-region filings and annotations (upstream unless noted)
| Item | Source |
|---|---|
| D-1 `DDD-measure-14` — the iterated chain-rule form as a claim node; §5.3's flag-upgrade path in the paper then cites the ID | measure completion session |
| D-2 Demand/cost distinction as a claim (G-1): the `core/10` §1 sentence promoted to a node; the paper's §2.1 then has its citation | revision session, Gate 1 |
| D-3 Admissibility as a claim (G-2), **with the Gate-7 warning honoured**: the condition must read *computable from ground available at the act without being handed the verdict* — a form that excludes S=V while keeping the Program row legitimate (building vs being-handed). A "cannot determine the verdict" form is wrong and breaks the actor-allocation instance | revision session Gates 3/7 |
| D-4 `measure-rag.py` replicate-band amendment: the 200-replicate band (sd ≤0.010, population 2.6126) into the asset's evidence note | revision session, next-canon list |
| D-5 `DDD-measure-05` FLAGGED tension vs `core/09` §6.3 ("measured on a deployed system pattern") — resolve: the revision retitled the instance encode/verify and demoted the sum claim; §6.3's phrase re-words to match | revision session, R-3 |
| D-6 `DDD-cost-10` + `13-cost-projection.md:111` (downstream): the one-line annotations inheriting cost-09's per-act-site qualifier | vocabulary session, DDD-dec-18 |
| D-7 Asset promotions: `measure-chained-seams.py`, `measure-nonuniform-ground.py` from `papers/measure-note/assets/` to upstream `core/assets/`, reproduction verified post-move, paper's Reproduction section re-pointed | measure completion, R-b |

### Batch E — instrumentation and conventions
| Item | Source |
|---|---|
| E-1 E13/W5 extension: instrument pinned **statements and regions**, not only status — dec-18's silent-region-move is the evidence, twice observed. Scope: validator change downstream + a decision recording the rule; keep the implementation minimal (hash the pinned fields; warn on divergence) | DDD-dec-16/18 |
| E-2 The `meta/sessions/` convention filed as a working-convention decision (downstream): prompts and bootstraps committed before sessions run; five arrival failures as basis (recorded in DDD-dec-17). This session's own first act is the first instance — cite it | DDD-dec-17 |

### Batch F — capacity residue (rulings, then minimal filing)
| Item | Source |
|---|---|
| F-1 Ruling 16's residue: are shared-budget (§7.3) and membership (§13.7) one account or two? Evidence before Emil: corpus question-3 (no magnitude invoked in 11 rows/7 gates; membership and arrival carried everything), the b1-reconciliation note, the delivery claims. Session presents the evidence and drafts both readings; **Emil rules; filing is whatever the ruling licenses and no more** | cancelled scoping session |
| F-2 Does `C_resolve` accounting extend to retrieval and authoring draws? Same treatment: canon-amendment question on `DDD-cost-05`'s region, presented with the two constraints (commensurability unestablished; per-arrangement not per-actor) | ground-axes §7.3 |
| F-3 The actor-indexed `open` conjunct ("no verifier the actor holds") is ill-defined where no actor was assigned — file the scope note on `term:escape-mechanism` recorded at DDD-dec-15 | escape session Gate 2 |

### Batch G — cross-repo one-liners
| Item | Source |
|---|---|
| G-7 The 2.13 cross-reference into `product-cli`'s decision register, citing `DDD-cost-11` — the one-line entry deferred since Wave 2 ("next session that touches that repo": this is it) | Wave 2 close |
| G-8 `DDD-dec-14` annotation (downstream, notes only): Q37 reframes the identity unit as the join key for one capability profile; the resolving session takes Q29 and Q37 together | rev18 assessment |

## Walk

1. **Fetch, inaugurate, verify.** All three repos; `meta/sessions/` first act done; every manifest
   item verified against head — items already fixed en passant by prior sessions are reported and
   struck, not re-done. Report batch order (default A→G; argue any resequencing) and the C-1 carve
   plan's size estimate. **GATE 1 — hold.**
2. **Batches A + B** (mechanical repairs and seam reconciliations). **GATE 2 — hold on the diffs.**
3. **Batch C** — the carve plan first, then execution only on Emil's plan approval per the gate rule.
   **GATE 3 — two holds: plan, then cut.**
4. **Batch D** (filings and annotations; D-3's wording gets line-level scrutiny). **GATE 4 — hold.**
5. **Batches E + F** (instrumentation decision + validator change; the two capacity rulings with
   evidence presented both ways; F-3's scope note). **GATE 5 — hold; F is rulings-first.**
6. **Batch G, sweep, close.** Cross-repo one-liners; full basis-impact sweep over everything touched;
   validators all repos; reference closure; branch per repo; PRs upstream-first (product-cli's is
   one line and independent); manifest recording every item's disposition — done, deferred, or
   struck-as-already-fixed. **GATE 6 — hold.**

On Emil's acceptance of the upstream PR: tag **v5.6.0** (term repairs + carve + new claims — minor),
downstream pin bumps to the tag, downstream PR stands, product-cli's merges independently.

## Out of scope

Wave 3 and everything routed to it (Q33-A/B, Q34, Q35, Q38a, 3.1–3.4, H1–H5). The measure paper
itself (D-items touch canon and assets, never the manuscript — the paper's citations update in its
own next session). The Q25/Q27/Q30/Q31 wave. Q37's inference machinery. G-track beyond G-7's one
line. The sweep/map/ranking tooling. Generator 2 (still a retrieval problem, not a work item). The
repo-name question (charter-level, Emil-only, own session if ever). Do not bundle.

## Standing note

Commit drafts to feature branches before reporting at each gate, bodies marked draft-pending-ruling.
This session's virtue is closing items at their booked size: where an item resists its booking,
the finding files as a deferral with the resistance named — a freight session that grows a design
session inside itself has failed at its own job.
