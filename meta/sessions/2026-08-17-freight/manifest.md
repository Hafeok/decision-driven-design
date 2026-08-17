# Freight session manifest — verification against head

**draft-pending-ruling.** Every manifest item checked against the three repositories at head before
any repair. Verified 2026-08-17. Bases: upstream `4f58837` (v5.5.0 + the merged addendum),
downstream `4848b9e`, `product-cli` `d506ac9`.

Disposition vocabulary: **STANDS** (defect confirmed at head, repair as booked) · **STANDS+**
(defect confirmed, but larger than its booking — resistance named) · **STRUCK** (already fixed by a
prior session; reported, not re-done) · **MOVED** (defect confirmed, but not where the manifest put
it).

---

## Batch A — prose and reference repairs

| Item | Disposition | Finding at head |
|---|---|---|
| **A-1** | **STANDS+** | `core/11` §7 names **four** instances (`05` §7, `05` §8, `06`, `10` §9), omitting `11` §6's own Missing row. `DDD-dec-15` and `DDD-floor-01` both record **five**. Two further defects found: (i) `core/11` §7 and `DDD-floor-01`'s notes both cite the unqualified declarer at **`05` §8**, but §8 is *Where this stops* — the unqualified declarer is at **`05` §6**, which is what `DDD-dec-15` says; (ii) `meta/b1-reconciliation-2026-08-14.md` §4 inherited the same wrong section number. Three sites, one fact. |
| **A-2** | **STANDS** | `core/09`:282 carries *"the intersection result `escape = overflow ∩ open`"* unqualified. `core/09`:415–416 already carries the corrected scope, so this is residue in §6.4 alone. |
| **A-3** | **STANDS** | `core/README`:23 carries *"escape = overflow ∩ open"* as the index gloss for `11`. |
| **A-4** | **MOVED** | The defect is **upstream**, at `meta/consolidated-state.md`:318–321, exactly where `DDD-dec-15` put it. The *downstream* `meta/consolidated-state.md` was reduced to the software-projection state at the split (`ae1aac4`) and carries neither defect — its judgment/escape material is gone entirely. Upstream's bullet carries both defects in one: the necessity form (*"the point at which H(verdict\|X) exceeds actor capacity is where demand escapes"*) and *"Not yet done — the natural next result"*, describing as unstarted a result `core/11` landed. |
| **A-5** | **STRUCK** | The novelty-statement correction landed at `06b0603` (*Gate 4 sweep: extend the supersession to DDD-cost-05 and the novelty statement*), tagged into v5.4.0. The register sentence at `meta/lineage-and-limits.md`:278 reads *"of **capacity-generated** escape with"*. Adjacent lines swept: §1.7's governing sentence (:124–127, scoped to *resolve-overflow error*), §1.9's *What DDD adds* (:165, scoped to *overflow escape*), the *Additional context* line (:270–271, scoped to *capacity overflow*), and the credits table (:475–478) all carry correctly scoped forms. **No residue. Nothing to repair.** |
| **A-6** | **STANDS+** | Booked at six; **thirteen** stale `core/10` references, all in the floor-mechanism sense (`core/10` is now the cost note; the mechanism is `core/11`). `apparatus/prefix-stability.md` ×2 (:6, :189), `apparatus/tool-contract.md` ×4 (:4, :123, :130, :149), `apparatus/tool-surfaces.md` ×7 (:4, :8, :27, :44, :65, :149, :164). Same repair, more lines — mechanical throughout. |
| **A-7** | **STANDS+** | Booked as `CLAUDE.md` alone; the stale `v5.0.0` pin statement appears at `CLAUDE.md`:9, `README.md`:8 and :79, `meta/way-of-working.md`:12, and `meta/consolidated-state.md`:55. Live pin is `v5.5.0` (`graph/upstream.yaml`). `migration-report.md`'s `v5.0.0` references are historical record of the migration and are **correct as they stand** — excluded. |
| **A-8** | **STANDS+** | Booked as the `v5.3.0` gap; upstream `CHANGELOG.md` stops at **v5.2.0**, so **three** versions are missing (v5.3.0, v5.4.0, v5.5.0 — tags exist for all three). Separately, `releases/` holds only `v5.5.0.yaml` (itself a retro-cut). Whether already-cut tags get retro release descriptors is a **convention question, not freight** — flagged, not taken. |
| **A-9** | **STANDS** | `DDD-cost-03`'s **`breaks:`** field (not `notes:`) reads *"The capacity/escape denomination (`DDD-cost-05`) survives"*, which carries the superseded identity reading. The corrected form already exists at `DDD-cost-08`'s `breaks:` — *"`DDD-cost-05`'s per-act denomination of the capacity model's escape term stands"* — and is the exact template. One line. |

**Items added by the verification pass, swept in on Emil's GATE 1 ruling:**

| Item | Disposition | Finding |
|---|---|---|
| **A-2b** | **DONE** | `core/05`:12 (upstream) — the document header's forward-reference gloss carried the identity form. Corrected to the capacity-generated scope. |
| **A-3b** | **DONE** | Downstream `README.md`:84 — *"escape is overflow ∩ open"* in the load-bearing-results sentence. Same correction. |
| **A-6b** | **DONE** | Found while repairing A-6: `apparatus/tool-contract.md`:149 carried the identity form too (*"the escape set (`core/10`: overflow ∩ open)"*). Both defects in one line — the stale document number **and** the superseded quantifier. Repaired for both. |
| **A-6c** | **DONE** | Found in the same sweep: downstream `README.md`:78 described upstream canon as *"`00` primitives through `11` the licensing instance"*. The licensing instance is `12`; `13` is delivery. Same renumbering-residue family as A-6, one line, corrected to *"`00` primitives through `13` delivery"*. |

---

## Batch B — registry seams and term repairs

| Item | Disposition | Finding at head |
|---|---|---|
| **B-1** | **STANDS** | `term:verdict`'s `canonical_md` reads *"For a task with a **decidable** acceptance predicate"*. `term:closure` reserves *decidable* for the formal special case and defines operational closure instead. One embed site (`core/09`). |
| **B-2** | **STANDS** | `term:acceptance-predicate` = *"the criterion that settles whether an outcome is acceptable at the declared tolerance"* (evaluates an outcome); `term:verdict` = *"the correct output the predicate assigns to each point of the input space"* (an assignment over the input space). Two objects, unreconciled. The settled account exists already in the paper's §2.2 (`papers/measure-note/measure-note.md`:181) — the reconciliation is a citation, not new work. |
| **B-3** | **STANDS** | `term:exhaustiveness` = *"determined by exactly one of"*; `core/02`:78 licenses *"a constraint before **and** a criterion after"* as defence in depth. Confirmed live at both sites; the corpus test found three rows (5, 6, 7) sitting in the licensed configuration, which is why it surfaced. |
| **B-4** | **STANDS**, with a **sequencing argument** (below) | Downstream `validate-core-order.py` has no shadow check. `check_upstream` compares pinned **status** only; nothing compares local term IDs against the upstream registry. `term:maturation` is live in *both* registries today and the validator is silent — 0 errors, 0 warnings, 28 pins resolved. Note the check must range over the **whole** upstream registry, not the pin list: `term:maturation` is not pinned, so a pin-scoped check would miss the one instance that motivated the rule. |

---

## Batch C — the diachronic carve

| Item | Disposition | Finding at head |
|---|---|---|
| **C-1** | **STANDS** — plan filed at `carve-plan-c1.md`; **defer-whole recommended** | Un-carved diachronic material confirmed live in `core/06` (the compound section and the channel section) and `core/08` (the maturation axis, which is `core/08`'s organising thesis rather than a severable section). The `term:maturation` shadow is live and unresolved. Full plan, scope and estimate in the sibling file. |

---

## Batch D — measure-region filings and annotations

| Item | Disposition | Finding at head |
|---|---|---|
| **D-1** | **STANDS** | Upstream claims run `DDD-measure-01`…`13`; no `-14`. The paper's §5.3 carries the standing marker: *"A dedicated claim node for the iterated form is pending canon filing."* Form and figures ready (`H(V) = I(V;S₁) + I(V;S₂\|S₁) + H(V\|S₁,S₂)`; both chain orders sum to 25.493). |
| **D-2** | **STANDS** | The `core/10` §1 sentence — *"Demand says what must be supplied; cost says what supplying it that way is worth"* — is live and unnoded; it currently rides `DDD-cost-01`'s citation. Next free cost ID across both repos is **`DDD-cost-30`** (upstream holds 01,02,03,05,08,09,11,12,13,20,22,25; downstream 04,06,07,10,14–19,21,23,24,26–29). |
| **D-3** | **STANDS** | Unfiled. The paper's §3.1 carries the standing marker and — importantly — **already states the correct form**: *"admissible if it is a function of ground available at the act, and of what the arrangement has standing before it, and not of the verdict itself … computable by something that has not been handed the answer"*, with §5.1's Program explicitly preserved (*"the difference is between building the answer and being handed it"*). The Gate-7 warning is honoured by drafting **from this text**, not around it. |
| **D-4** | **STANDS** | `DDD-measure-05`'s asset evidence note carries *"40k samples; answer generated independently of retrieval…"* and no replicate band. The band is in the paper (§5.2, :414–424): 200 replicates, mean within 0.002 bits at every setting, single-run sd up to 0.010, plug-in `H(A)` mean 2.6117 / sd 0.0049 / central 95% `[2.601, 2.621]` / bias −0.0008, population 2.6126. |
| **D-5** | **STANDS** | `core/09` §6.3 is titled *"X = retrieval → RAG, and conservation measured on a real pattern"* and the `DDD-measure-05` FLAG is live in the claim's notes. The paper already made the corresponding move: §5.2 is retitled *"`X` = what is supplied before the act → the encode/verify split"* and states *"It is not a measurement of conservation"*. The prose is the bug; the claim governs. |
| **D-6** | **STANDS** | Neither `DDD-cost-10`'s `region:` nor `core/13-cost-projection.md`:111 carries the per-act-site qualifier that `DDD-cost-09` gained at v5.5 by scope extension. Two one-line annotations. |
| **D-7** | **STANDS** | `measure-chained-seams.py` and `measure-nonuniform-ground.py` are in `papers/measure-note/assets/`, absent from upstream `core/assets/`. **Both re-run clean at head** (chained seams: 4.901 + 17.838 = 14.474 + 8.265 = 22.739, parts 2.755, whole 25.493; non-uniform: identity exact in all four deployments). Reproduction to be re-verified *after* the move, per the booking. |

---

## Batch E — instrumentation and conventions

| Item | Disposition | Finding at head |
|---|---|---|
| **E-1** | **STANDS** | Confirmed by reading `check_upstream`: W5 fires on `status_at_pin` divergence only. Nothing hashes or compares statement or region. `DDD-dec-18`'s own resolution says so in canon's voice — *"only status is instrumented"* — and names it the second observation (the first is `DDD-dec-16`'s, on `DDD-floor-01` at v5.4). Minimal implementation available: per-pin content hash of the pinned fields, new warning class on divergence. |
| **E-2** | **STANDS — first instance already committed** | `meta/sessions/` did not exist; created, with this session's prompt and bootstrap, as the session's first act (`96d0112`, pushed before any canon was read). The convention's basis is `DDD-dec-17`'s five arrival failures, which that decision explicitly *"Recommended to the freight session, not filed here"*. The decision node itself is still to file; next free downstream decision ID is **`DDD-dec-19`**. |

---

## Batch F — capacity residue

| Item | Disposition | Finding at head |
|---|---|---|
| **F-1** | **STANDS — evidence available** | Corpus question-3 is live and readable (`meta/corpus-test-results-2026-08-14.md`:1055): across 11 expressions and 7 gates **no classification ever invoked a magnitude**; presence/arrival objects carried every reading; row 11's nothing-to-deliver is §13.7's internal location expressed as an absent delivery failure mode. The b1-reconciliation note (upstream `meta/`) is readable in full and states the two accounts explicitly (§5: capacity-shaped vs membership-shaped), together with its own instruction — *"Report the instances. Do not rule on the accounts."* The delivery claims are readable. **Evidence sufficient to present both readings.** |
| **F-2** | **STANDS — evidence INCOMPLETE, arrival failure** | The ground-axes holding note **is not in either repository** and did not arrive with this session. Its §7.3 — F-2's entire source — cannot be read. This is the same failure class `DDD-dec-17` books five times and `DDD-dec-15` still carries an `UNVERIFIED` block for; the standing discipline is to refuse to substitute a summary for a source. The two constraints as *stated in the session prompt* (commensurability unestablished; per-arrangement not per-actor) can be presented; the section they qualify cannot be checked. **Recommendation: present the question, do not draft readings from a source that did not arrive.** Emil's call. |
| **F-3** | **STANDS** | The flag is live in three places and repaired in none: `DDD-floor-01`'s notes (*"FLAGGED, not repaired here (Emil, GATE 2)"*), `DDD-dec-15`'s notes (same wording), and `meta/b1-reconciliation-2026-08-14.md`'s standing-flags list. `term:escape-mechanism`'s `canonical_md` still reads *"(2) Open — no verifier the actor holds"* with no scope note. |

---

## Batch G — cross-repo one-liners

| Item | Disposition | Finding at head |
|---|---|---|
| **G-7** | **STANDS** | `product-cli` contains **no** reference to `DDD-cost-11` or any `DDD-cost-*` id. The pending-transfer booking is at `meta/holding-note-act-cost-2026-08-08.md`:580 and its ruling at :591–593 (*"the cross-ref files into product-cli's decision register in the next session touching that repo, citing `DDD-cost-11`; no third PR"*). Content is fixed: the rejection-payload lever (`core/15` §4 — pass/fail 0.35/try vs rich payload 0.55/try; 11.4 vs 7.3 per act) as basis for the pending M3/M4 principal decisions. Register is `.ddd/decisions/`, current file format 7. |
| **G-8** | **STANDS** | `DDD-dec-14`'s notes carry nothing about Q37. Q37 is live in upstream `meta/holding-note-addendum-determinables.md`:107–137, and its own routing line says *"the dec-14 annotation immediately, one line"*. Content fixed by the source: the identity unit becomes the join key for one capability profile, cross-version transfer becomes partial per-region profile inheritance — a smaller question than the ontological one — and the resolving session takes Q29 and Q37 together. Annotation only; `DDD-dec-14` stays OPEN and is not resolved. |

---

## Summary

28 items checked.

| Disposition | Count | Items |
|---|---|---|
| **STANDS** — repair as booked | 20 | A-2, A-3, A-9, B-1, B-2, B-3, B-4, C-1, D-1…D-7, E-1, F-1, F-3, G-7, G-8 |
| **STANDS+** — confirmed, larger than booked | 4 | A-1, A-6, A-7, A-8 |
| **MOVED** — confirmed, other repository | 1 | A-4 (upstream, not downstream) |
| **STRUCK** — already fixed | 1 | A-5 |
| **Evidence incomplete** | 1 | F-2 (source did not arrive) |
| **First instance already committed** | 1 | E-2 (node still to file) |

**One item struck as already fixed: A-5.** Everything else is live at head. No item was found
already-repaired en passant beyond A-5, and no item dissolved on inspection.
