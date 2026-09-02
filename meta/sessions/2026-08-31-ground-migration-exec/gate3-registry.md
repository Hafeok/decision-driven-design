# GATE 3 — the registry wave, executed and verified

**Status: draft-pending-ruling.** The prediction was committed first (`gate3-prediction.md`,
downstream `a8d5fa5`), the edits after (upstream `0aa55e2`, branch
`claude/ground-migration-exec-teb4gc`). Nothing merged; no tag; the downstream pin untouched.

## Predicted, then observed

| Prediction | Observed |
|---|---|
| zero of the seed's seven W6 fire | **zero — no pinned entry's text moved** |
| exactly two W6 deferred to the next pin advance: `DDD-measure-01` → `sha256:d78274d2…`, `DDD-measure-16` → `sha256:6828d066…` | **both digests landed on the predicted values, character-exact; a sweep over all 71 pins shows exactly these two moved** |
| three entries move, all unpinned; three embeds re-project | **three and three** (`term:overflow`, `term:poisoned-ground`, `term:verdict`; `core/11`, `core/00`, `core/09`) |
| zero W5, zero W7, zero E12/E13; downstream validation unchanged | **0 errors, 0 warnings downstream; 26 claims, 6 warnings** |
| upstream validators at baseline | **0 errors, 66 warnings — identical by content** (line numbers under the grown embed shift by one, which is the third method rule observed in the wild); 63 claims / 32 warnings; 12 decisions |
| asset outputs byte-identical | **verified by run, before and after** (`measure-nonuniform-ground.py`, `measure-aggregate-discharge.py`) |

**Divergences recorded, none reconciled:**
1. **Seven predicted W6 → zero.** The definitional layer is already correct under the ratified
   precedents — the seven pinned entries' texts are the exemplars the precedents were drawn from
   (`reading`, `declared`, `observable`, `in context at once`, `channels`, `held at fixed`, `at
   the act`). The seed's prediction stands as written and did not verify; accepted in advance at
   Gate 2 (P-04's consequence).
2. **Eleven predicted embed re-projections → three.** Same cause.
3. **SR-5's "W1 fires no pins" superseded by `DDD-dec-34`**, which pinned two S5 claims after the
   seed was written. W1 now carries exactly two W6, predicted here by id and hash before the edit.
4. **Four unpinned entries predicted moving → three.** `term:encode-verify-split` needs nothing:
   *"pre-resolving ground into the encoded store"* is P-07's shape.

## What moved

**Registry (`core/graph/terms.yaml`), three entries, unpinned, nothing fires:**
- `term:overflow`: *"the decision's governing ground **exceeds hold capacity**"* — P-05, the
  entry's own parallel completed. Prose twin in `core/11` aligned.
- `term:poisoned-ground`: one sentence added — *"The state it names: **ground that reached the
  act false** — what arrived is wrong, not missing."* The settled clauses do not move (P-02).
  **A defect was caught by the validator and repaired before commit**: the first draft said *"in
  the delivery vocabulary: delivered ground…"*, and `delivery` is established by `13-delivery.md`
  — a forward edge from `00`, flagged as a new W1 warning. Re-worded to the act-locating form,
  which P-04 rules is the delivery qualifier; the warning set returned to baseline. The reading
  order is the dependency order, and the vocabulary's own name cannot be used upstream of where
  it is established.
- `term:verdict`: *"(the \*deployment distribution\*)"* — SR-5, the S5 body's registry site.

**W1 upstream, 30 tokens across 14 files** (`ground distribution` → `deployment distribution`,
plus *"non-uniform ground"* → *"non-uniform deployment distribution"* and *"under varied ground"*
→ *"under varied deployment distributions"* where the compressed forms carried the same sense):
`core/09` (10), `core/06`, `core/13`, `README.md` (the row Gate 1 booked), `DDD-measure-01`,
`-11`, `-12`, `-16`, `meta/lineage-and-limits.md`, `meta/measure-paper-context.md` (2),
`meta/repo-topology.md`, and comments/docstrings in three assets.

**Left, each with its precedent:**
- `releases/*.yaml` — immutable (A9).
- `meta/measure-paper-context-staleness-2026-08-14.md` — a dated finding; P-13.
- Three printed strings inside `measure-nonuniform-ground.py` (lines that end up in the asset's
  output) — left so the output stays byte-identical, per the committed prediction. **For the
  ruling:** if Emil prefers the printed labels moved too, the numbers are unchanged and the
  re-verified output becomes the new recorded evidence; that is a one-line follow-up, not taken
  unilaterally against a stated prediction.
- Every filename (`measure-nonuniform-ground.py` above all) — U-idname, SR-6; the measure note's
  §5.4 *"named before the vocabulary moved"* clause stays true.
- The sixteen deferred manuscript occurrences — they quote canon at the pinned `v5.12.0` tag,
  which no branch edit touches; they regenerate when the pin next advances. The supplement's
  *"canon still reads `ground distribution` at `v5.12.0`"* remains literally true.
- `ground channel`, all 10 occurrences — P-11/P-17, recorded at the prediction.

## What this gate asks

1. The registry wave as executed — three entries, three embeds, and the zero-of-seven finding.
2. The two predicted W6 riding with W1 (`DDD-measure-01`, `DDD-measure-16`) — they fire at the
   next pin advance, which is G6's proposal, not this gate's act.
3. The poisoned-ground sentence as re-worded, with the forward-edge repair disclosed.
4. The three printed asset strings: leave (as predicted) or move with re-verified output.

**Nothing merged. Holding at GATE 3.**
