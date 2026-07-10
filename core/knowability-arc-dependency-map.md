# Knowability Arc — Dependency Map

> Integration reference for the four insertion blocks. Lists every cross-reference each file makes, the `core/` target path it assumes, the anchors/concepts it pulls, and a mechanical checklist to verify against the live repo tree before landing. Also records the dependency DAG and confirms it is acyclic.

---

## 1. The four files and their intended homes

| File (output) | Intended repo path | Role |
|---|---|---|
| `finite-index-lemma.md` | `core/02-completeness/finite-index-lemma.md` | KC1 — new content (τ-finite sensitivity) |
| `decidability-corollary-kc2-kc3.md` | `core/02-completeness/decidability-corollary.md` | KC2 + KC3 — corollary of zero-floor |
| `action-target-and-levers.md` | `core/01-the-law/` (block, or `action-and-levers.md`) | action def, plan(p*), two levers |
| `tier-specification-inverse-law.md` | `core/03-the-polanyi-floor/` (block, or `tier-inverse-law.md`) | derives tier–spec inverse law |

> Note: two files are written as *insertion blocks* for existing core files (`action-*` → `01-the-law`; `tier-*` → `03-the-polanyi-floor`). Decide at integration whether they land as new sibling files under those dirs or as appended sections. The map treats each as a node regardless.

---

## 2. Outbound dependencies (what each file references)

Legend for concept pulls — verify each target actually defines the named concept at the cited path.

### finite-index-lemma.md  → depends on
```
core/01-the-law            : governing decision set, assurance level, tolerance, granularity membership test
core/03-the-polanyi-floor  : zero-floor postulate    [INDEPENDENT-OF, not depends-on — see §5 of file]
```
Self-declared location: `core/02-completeness/finite-index-lemma.md`.
Note: the reference to `03` is an explicit **non-dependency** (KC1 ⊥ zero-floor). It must not become a build/dependency edge; it is an anti-edge asserting independence.

### decidability-corollary-kc2-kc3.md  → depends on
```
core/03-the-polanyi-floor            : zero-floor postulate; intrinsic/transfer floor;
                                       proof program (= termination of encode–exercise iteration);
                                       descent measure (= unencoded demand mass)
core/02-completeness/finite-index-lemma : KC1; τ-live membership test
core/01-the-law                      : four stores; acceptance predicate; last wind
```
Self-declared home: `core/02-completeness`.

### action-target-and-levers.md  → depends on
```
core/01-the-law (the Law)               : governing decision set, four stores, assurance level, last wind
core/02-completeness/finite-index-lemma : τ-live rank, τ-effective dimension
core/03-the-polanyi-floor               : intrinsic + transfer decomposition
```
Also cites (soft, cross-file concept, not a path): the maturation asymptote `(1 − floor)`; the escape-under-pressure / two-class residual taxonomy. Verify these live in `01-the-law` or wherever maturation/escape are canonically defined.

### tier-specification-inverse-law.md  → depends on
```
core/03-the-polanyi-floor (this file)   : floor = intrinsic + transfer  [SAME-FILE / self]
core/01-the-law                         : four stores, last wind;
                                          success decomposition 1 − success = esc_escape + esc_wind
                                          (the latter lives in the action/levers block)
```
Cross-block dependency: pulls the **success decomposition** from the action/levers block. If that block lands under `01-the-law`, this edge is `03 → 01`. If it lands as its own file, update the citation to that path.

---

## 3. Dependency DAG

Nodes abbreviated: `LAW`=01-the-law, `FIL`=finite-index-lemma, `COR`=decidability-corollary, `ACT`=action-target-and-levers, `TIER`=tier-inverse-law, `PF`=03-the-polanyi-floor.

```
        LAW ────────────────┐
         ▲   ▲   ▲          │
         │   │   │          │
   FIL ──┘   │   │          │   (FIL → LAW)
             │   │          │
   ACT ──────┘   │          │   (ACT → LAW, ACT → FIL, ACT → PF)
    │            │          │
    ├───→ FIL    │          │
    └───→ PF     │          │
                 │          │
   COR ──────────┘          │   (COR → LAW, COR → FIL, COR → PF)
    ├───→ FIL               │
    └───→ PF                │
                            │
   TIER ────────────────────┘   (TIER → LAW, TIER → PF, TIER → ACT-block)
    ├───→ PF (self/same-dir)
    └───→ ACT (success decomposition)

   Anti-edge (assert, do NOT wire):  FIL ⊥ PF   (independence, §5 of FIL)
```

Edge list (directed, "A → B" = A depends on B):
```
FIL  → LAW
COR  → LAW,  COR → FIL,  COR → PF
ACT  → LAW,  ACT → FIL,  ACT → PF
TIER → LAW,  TIER → PF,  TIER → ACT
```

**Acyclicity check.** Topological order exists:
```
LAW  <  FIL  <  { ACT, PF }  <  { COR, TIER }
```
- LAW has no outbound edges (root of the arc; it is prior canon).
- FIL depends only on LAW.
- PF is prior canon (zero-floor lives there); within this arc it is depended-upon, and its only new addition (TIER) depends outward on LAW/ACT, not back into COR/FIL — no cycle.
- ACT depends on LAW, FIL, PF — all earlier.
- COR depends on LAW, FIL, PF — all earlier.
- TIER depends on LAW, PF, ACT — all earlier.

No back-edges. **DAG confirmed acyclic.** The one relation that *could* look like a cycle — FIL and PF — is explicitly an anti-edge (independence), not a dependency, so it introduces no edge at all.

---

## 4. Pre-landing verification checklist (mechanical)

Run against the live repo tree. Each row: confirm the **path exists** and the **named concept is actually defined there**.

```
[ ] core/01-the-law                         exists
    [ ] defines: governing decision set
    [ ] defines: four stores (encoded/mech/judgment/escaped)
    [ ] defines: assurance level, tolerance τ
    [ ] defines: granularity membership test
    [ ] defines: last wind
    [ ] defines: acceptance predicate            (NEW — arrives via ACT block; if ACT lands elsewhere, fix FIL/COR/ACT anchors)
    [ ] defines: success decomposition 1−success = esc_escape + esc_wind  (NEW — via ACT block)
    [ ] defines / hosts: maturation asymptote (1−floor)   (verify canonical location)
    [ ] defines / hosts: escape-under-pressure two-class taxonomy  (verify canonical location)

[ ] core/02-completeness                     exists
    [ ] core/02-completeness/finite-index-lemma.md   (FIL lands here)
    [ ] core/02-completeness/decidability-corollary.md  (COR lands here; rename from kc2-kc3 filename if desired)
    [ ] defines: KC1, KC2, KC3 naming (Knowability Claims)   — canonical def site is COR §1

[ ] core/03-the-polanyi-floor                exists
    [ ] defines: zero-floor postulate
    [ ] defines: floor = intrinsic + transfer decomposition
    [ ] defines: proof program (= termination of encode–exercise iteration)
    [ ] defines: descent measure (= unencoded demand mass)
    [ ] hosts: tier–specification inverse law   (TIER lands here)
```

**Anchor-fragility flags** (the edges most likely to break on integration):
```
!  acceptance predicate + success decomposition are declared as living in 01-the-law
   via the ACT block. THREE files cite them (FIL soft, COR, TIER). If ACT lands as a
   separate file instead of inside 01-the-law, update the cited path in COR and TIER.

!  maturation asymptote and escape two-class taxonomy are cited by ACT and COR but their
   canonical home was not written by this arc. Confirm where they live and point at it.

!  FIL ⊥ PF independence must be preserved as prose, never wired as a dependency. If a
   docs build auto-links "core/03-the-polanyi-floor" mentions, exempt FIL's §5 reference.
```

---

## 5. Naming convention (record)

```
KC   = Knowability Claim
KC1  = finiteness              |D(t,α)| < ∞                    (finite-index lemma)
KC2  = membership decidability  d ∈ D(t,α) decidable           (decidability corollary)
KC3  = loop termination         encode–exercise converges,     (decidability corollary)
                                detectably, to esc = esc_wind
```
Canonical definition site: `decidability-corollary` §1. Full phrase "Knowability Claim(s)" on first use in any external paper (Paper B). "KC" chosen to avoid collision with field-`K`, completeness constants, Knaster–Tarski.

---

## 6. Suggested integration order

Land in topological order so every dependency exists before its dependents cite it:
```
1. (verify prior canon LAW, PF in place)
2. FIL   → core/02-completeness/finite-index-lemma.md
3. ACT   → core/01-the-law/  (this publishes acceptance predicate + success decomposition)
4. COR   → core/02-completeness/decidability-corollary.md
5. TIER  → core/03-the-polanyi-floor/
6. (optional) assemble the Knowability Theorem as core/02-completeness/knowability.md,
   citing FIL (KC1) and COR (KC2/KC3) — single citable result for Paper B.
```
Step 3 before 4 and 5 matters: both COR and TIER cite concepts ACT introduces.
