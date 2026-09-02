# GATE 3, step 1 — the registry wave, predicted before anything moves

**Status: committed before any edit, in the `DDD-dec-29` pattern.** Every prediction below is
stated by id, and where a hash exists, by hash — old and new, the new computed from the drafted
edit before the file moves. A divergence found at verification is recorded, never reconciled.

## 1. The finding that resizes the wave

**Applying the ratified precedents to the eleven entries, none of the seven pinned entries'
canonical texts needs to move.**

| Entry | Pinned | Its ground occurrence | Precedent | Ruling |
|---|---|---|---|---|
| `term:actor` | yes | *"by **reading** ground: variation in **declared** ground"* | P-07, P-20 | no edit |
| `term:arrangement` | yes | *"**ground channels**"* | P-11/P-17 | no edit |
| `term:capability` | yes | *"the class of ground a pathway **can read**"* | P-07 | no edit |
| `term:capacity` | yes | *"the bits of ground it can have **in context at once**"* | P-04 | no edit |
| `term:closure` | yes | *"the relevant ground is **observable**"* | P-07 | no edit |
| `term:judgment` | yes | *"an actor **reading** ground"* | P-20 | no edit |
| `term:residual-discretion` | yes | *"**held at fixed** ground … **at the act** … variation across ground (S1)"* | P-04, SR-1 | no edit |
| `term:encode-verify-split` | no | *"**pre-resolving** ground **into the encoded store**"* | P-07 | no edit |
| `term:overflow` | no | *"the decision's governing ground **does not fit**"* | **P-05** | **edit** |
| `term:poisoned-ground` | no | anaphor ruled at P-02 | **seed item 2** | **one sentence added** |
| `term:verdict` | no | *"(the **ground distribution**)"* — S5 | **SR-5 / W1** | **edit** |

The definitional layer is already correct under the ratified vocabulary — the registry's own
texts are the exemplars the precedents were drawn from. **The seed's predicted seven W6 therefore
do not fire: zero of seven.** That divergence was accepted in advance at Gate 2 (P-04's
consequence): the prediction stands as written and is recorded as not verifying, exactly as
380/187 was at Gate 1. **Eleven predicted embed re-projections become three** — only entries
whose text moves re-project.

## 2. W1's upstream body rides with `term:verdict`, and it brings two W6 of its own

`term:verdict`'s edit makes `core/09` internally inconsistent unless the surrounding prose moves
with it, and `core/09` cites the measure claims, which carry the same phrase in their statements.
The papers already moved (15 W1 moves, merged; the measure note's pin advanced so both agree);
canon still reads `ground distribution` at `v5.12.0`. **The upstream S5 body is therefore
executed here**, and its firing consequences are:

- **`DDD-dec-34` pinned two of the S5 claims after the seed was written.** SR-5's *"W1 fires no
  pins"* was true against the seed's pin set and is superseded by that advance — recorded as a
  post-seed fact, not a seed error.

> **Prediction: when the downstream pin next advances past these commits, exactly two W6 fire
> and no more, both from W1:**
>
> | id | occurrences in hashed fields | pinned hash (= live, verified) | predicted hash after edit |
> |---|---|---|---|
> | `DDD-measure-01` | 1 (statement) | `sha256:66b01ede631c0173d86696dca945ade53c9ffe37462bbe290a6df6b6de4b41ea` | `sha256:d78274d2350cb867c9ec3497aaf13caeafb4792f9e20c20697ba54114a58c198` |
> | `DDD-measure-16` | 2 (statement) | `sha256:2d763d1adf9e1c68c88d1f5c3e30550a5079e274d84e688c31f5f5bb51f1d94e` | `sha256:6828d06649045bfdf374f985a7984d337d01fdb42be29ef8f051a185411fe674` |
>
> **Zero W5** (no status moves), **zero W7** (no id added or shadowed), **zero E12/E13.**
> Of the 71 pins, exactly these two digests move; the other 69 are verified unchanged after the
> edits. The edit is the phrase `ground distribution` → `deployment distribution`, verbatim,
> nothing else in any hashed field.

**In-session observables: nothing fires at all.** The downstream pin resolves against the `v5.12.0`
tag, which no branch edit touches; downstream `validate-core-order.py` reports the same 71 pins,
0 basis-loss, 0 content-drift, 1 governed shadow before and after. Upstream validators stay at
their documented baselines (0 errors / zero W4; 63 claims valid, 32 warnings; 12 decisions).

## 3. The exact upstream edit set

**Registry (`core/graph/terms.yaml`), three entries, all unpinned, nothing fires:**
1. `term:overflow`: *"the decision's governing ground does not fit."* → *"the decision's
   governing ground **exceeds hold capacity**."* (P-05 as ratified.)
2. `term:poisoned-ground`: one sentence **added** after the settled text, naming the state in the
   delivery vocabulary (the seed's item 2 — one sentence, not 66 edits). The existing clauses do
   not move (P-02).
3. `term:verdict`: *"(the \*ground distribution\*)"* → *"(the \*deployment distribution\*)"*.

**Embeds re-projected, three sites:** `core/00-primitives.md` (poisoned-ground),
`core/11-the-floor-mechanism.md` (overflow), `core/09-the-measure.md` (verdict). The other eight
embed sites do not move; `term:capacity`'s embed in `core/11` in particular stays byte-identical.

**W1 upstream prose and claims** (`ground distribution` → `deployment distribution`, verbatim):
`core/09-the-measure.md`; `DDD-measure-01`, `DDD-measure-11`, `DDD-measure-12`,
`DDD-measure-16`; `README.md` (the row Gate 1 booked); `meta/lineage-and-limits.md`,
`meta/measure-paper-context.md`, `meta/repo-topology.md`. Each remaining upstream S5 ledger row
is dispositioned in the gate report with its precedent.

**W1 upstream assets** — comments and docstrings only, P-16's condition enforced:
`core/assets/measure-nonuniform-ground.py` and `core/assets/measure-aggregate-discharge.py` are
run before and after; **outputs must be byte-identical**, and every filename keeps its name
(`measure-nonuniform-ground.py` is cited by name in the measure note's §5.4 divergence clause,
which stays true).

**Explicitly not edited:** `releases/*.yaml` (immutable, A9); dated records under P-13
(`meta/measure-paper-context-staleness-2026-08-14.md` if its occurrence proves to be a dated
finding); the sixteen deferred manuscript occurrences (ruled at the Paper A session's Gate 1 —
they quote canon at the pinned ref and regenerate when the pin next advances); `product-cli`
(W4, never here).

## 4. Also recorded at this gate

- **`ground channel`, all 10 occurrences: no edit**, under P-11/P-17 — the compound's head names
  the delivery path. The seed's item 3 wanted the surface known, not moved; it is known and it
  stands.
- The downstream W1 remainder (downstream meta, applications, assets, and the papers' 16
  deferrals) is G4's, under the same precedents.

*Verification section follows in the gate report, after execution.*
