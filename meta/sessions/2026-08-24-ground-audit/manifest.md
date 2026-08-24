# Session manifest — Phase 1b: the ground audit (2026-08-24)

**Session type:** interactive audit, four gates, Emil ruling at each. **Nothing merged.**
**Branch:** `claude/ground-audit-phase-1b` (`decision-driven-design` only).
**Read at:** upstream `37f508e` (= `v5.10.0`, head and tag coincident) · downstream `92c7b2e` ·
`product-cli` `d0f4297`, read-only.

---

## 1. The audit changed nothing, and that is checkable

| Repository | State at close |
|---|---|
| `actor-indexed-determination` | **No branch created, no commit, clean tree, still on `main` at `37f508e`.** Read only |
| `product-cli` | **Clean tree.** Cloned read-only, never written |
| `decision-driven-design` | 6 commits on the session branch, **every changed path inside `meta/`** |

`git diff --name-only main...HEAD` outside `meta/sessions/2026-08-24-ground-audit/` returns exactly
one path: `meta/sessions/README.md`, the index row `DDD-dec-20` requires. The deliverables added at
GATE 4 are `meta/ground-audit-2026-08-24.md` and `meta/successor-items-ground-audit.md`.

**No canon file, no claim, no term, no document outside `meta/` was edited in any repository.**

---

## 2. What the session produced

| Deliverable | Where |
|---|---|
| **D-1** the classification | `meta/ground-audit-2026-08-24.md` §2; `classification.json`, 2,845 rows |
| **D-2** the cost table | `meta/ground-audit-2026-08-24.md` §2; `gate2-classification.md` §2 |
| **D-3** the four design rulings | `meta/ground-audit-2026-08-24.md` §4; `gate3-rulings.md` |
| **D-4** the migration's shape | `meta/ground-audit-2026-08-24.md` §6 |
| the §7/Q27 collision, both texts | `gate3-rulings.md`; summarised at `§5` of the audit |
| successor items | `meta/successor-items-ground-audit.md` |
| instruments | `count-ground.py`, `extract-occurrences.py`, `classify.py`, `residual-adjudication.json` |

---

## 3. The four things worth carrying forward

### 3.1 The definition layer was never single-sensed, which decided what kind of repair this is

Emil's GATE 2 question — is canon's prose drifting from its settled term, or is the settled term too
narrow — had a third answer the audit was the first artefact in a position to give. **Fifteen settled
terms in `core/graph/terms.yaml` carry four senses of the word between them.**

**That forecloses the prose-repair remedy.** Prose cannot be repaired to comply with `term:ground`
while ten other *settled* terms — including the one defining what an actor **is** — use the word
otherwise. The prose is not drifting; it is following a definition layer that was already split.
**The remedy is definitional**, and knowing that before cutting is most of what the audit bought.

### 3.2 The overload has already cost something

`apparatus/encode-verify.md` defines `ground` as the read-only surface an actor inspects **and cites
`core/00` for it**, where `core/00` defines it as what determinations are made against.

SR-1 ruled the split real on three *observations*. **This is a consequence** — a false citation
across the repository seam, in a document written to state a principle correctly. Both the proposal
and the assessment missed it, because both reasoned about the word and neither put the two
definitions side by side. **The split's first realised cost, not its fourth prediction.**

### 3.3 One object in three conditions, not three objects

The audit's own contribution to the ruling. Canon's sense-3 occurrences are **verbs applied to the
sense-1 object** — *reading*, *held*, *present*, *delivered*. Sense 3 is not a rival primitive
competing for the noun; it is what happens to sense 1 at an act.

Two consequences followed immediately. The **delivery vocabulary fits** rather than needing a
parallel invention — `term:delivery`, `term:undelivered` and `term:presumed-discharge` already model
this relation on the decision side. And the migration is mostly **re-expression rather than
re-conception**, which is what made the expensive disposition affordable.

### 3.4 Volume is a cost, not a vote

Ruled at GATE 2 and load-bearing at GATE 3. `product-cli` carries 45% of all occurrences and is 92%
one sense — the sense that does *not* keep the word. The recommendation was made from canon's
definition and canon's usage, with counts entering only where cost is priced, and **the more
expensive disposition was recommended and taken**.

---

## 4. Where the audit corrected its own inputs

| Input claim | What the count showed |
|---|---|
| The assessment prices the migration as the registry, core documents, claim statements, the axis registry, the G-track PRD, the primer and two papers | **`product-cli` is absent from that list and carries 1,286 occurrences — 45% of the total, more than either canon repository** |
| The assessment names the G-track PRD as migration surface | It is `product-cli/docs/g-track/prd-ground-as-ontology.md` — **in the repository the assessment does not price** |
| The proposal's migration table has rows for `ground channel` and `ground coverage` | **Both occur zero times in any repository** |
| The proposal and the assessment enumerate named compounds | **Five unnamed compounds carry 236 occurrences; four named ones carry 68** |
| SR-1 records three independent arrivals | **Q27 is a fourth**, reaching the held/delivered distinction from the assurance side |
| `DDD-dec-26` read as ruling the provenance taxonomy exclusive | It ruled it ineligible for **minting**, with a stated reason. **The gate was on the value, not the axis** |

---

## 5. The instrument's defect history

Recorded with the instrument, per the convention Phase 1a established.

| Defect | Effect | Fix |
|---|---|---|
| `_` is a word character, so `\bground` never fires after `parse_` | Discarded **every snake_case identifier** as a false positive — most of the software surface | Boundary restated as "not a letter and not a digit" |
| Escaped newlines in Rust string literals put `n` before `ground` | Hid four occurrences of the real YAML field name `ground:` | `\n`, `\t`, `\r` unescaped before matching |
| The instrument quoted its own regex in its own docstring | The audit counted itself | Audit directory excluded |

Naive 2,932 → corrected **2,845**: **+14 recovered, −101 removed.** The net is small and the gross is
not; a single number would have concealed both.

**And the honest coverage was reported rather than manufactured.** The rule table has **no default
rule**, because a default is the single thing that could have made the classification lie. 1,022
occurrences matched nothing and are reported as sampled, not as assigned.

---

## 6. Deliberately not done

| Item | Why |
|---|---|
| **The migration itself** | The audit is the plan; the plan is the product. C-1 precedent |
| **Renaming anything** | Out of scope by charter, in every repository |
| **Repairing the apparatus miscitation** | Found by the audit; **recorded and routed as freight**, per the GATE 2 ruling. The session changes nothing and that held even for a defect it found |
| **Resolving the §7/Q27 collision** | SR-4. Reported with both texts quoted; the migration session rules it before Q27 files |
| **`poisoned ground`'s sense change** | Flagged as must-touch; it is a `settled` term, so a supersession and not a migration edit |
| **The decoder repair** | Research. The split makes the defect easier to state and does not fix it |
| **Full classification of the 1,022** | **W0, and it blocks the migration** — but it is the migration's first session, not a prerequisite to planning it |
| **`product-cli`'s field-name disposition** | Surfaced without recommendation. It is the only edit in the migration that can break something already running |

---

## 7. Pull request

One, `decision-driven-design` only, because only one repository was written.

**Nothing upstream to open**, and that is the manifest's closing check rather than an omission: the
canon repository has no branch, no commit and a clean tree at the session's end.
