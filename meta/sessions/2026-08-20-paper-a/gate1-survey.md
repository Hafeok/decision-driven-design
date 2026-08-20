# GATE 1 survey — Paper A: the readiness map re-verified

**draft-pending-ruling.** Step 1 of the walk: repos at head, session record committed, the Wave 3
projection-readiness map re-verified against canon **at the tag actually found**. Everything the
map asserts that head now contradicts is reported below rather than carried.

---

## 1. The tag, verified

Emil reported **v5.8.0**. The fetch confirms it.

| | |
|---|---|
| Newest tag in `actor-indexed-determination` | **`v5.8.0`**, dated 2026-08-18 |
| Tag message | *"v5.8.0 — Track 1: the two deferred mints, discharged on use"* |
| Commit | `9e92099f503a180e7205df224d625b1f0d2fa96f` |
| Upstream head | `33b6d28a4f4d3528371a53dd4af76b809f07cbd5` |
| head − tag | **one file**: `core/assets/measure-aggregate-discharge.py` (+160), the measure note's sixth asset. No claim, term, decision or document differs. |
| Full tag list | v5.0.0, v5.2.0, v5.3.0, v5.4.0, v5.5.0, v5.6.0, v5.7.0, **v5.8.0** |
| Downstream head | `aa7e1352bc6484c7bb5f467bd5b66a849692cbc9` (PR #25, the measure note's discharge section) |
| Downstream newest tag | **`v0.4.0`** → `5455fcf` |

**Consequence for the pin.** Wave 3's successor item 5 and the readiness map both anticipated
*"projection of `actor-indexed-determination` at v5.7.0"*, because v5.7.0 was the expected
acceptance tag when they were written. One release has landed since. **The paper pins v5.8.0**,
and every citation below was verified against v5.8.0 rather than against head or against the
map's word.

---

## 2. The map re-verified, ID by ID

Every claim, decision and term identifier the readiness map names **resolves at `v5.8.0`**.
Thirty-five claim/decision IDs checked, twenty term IDs checked, **zero missing**.

Statuses the map asserts, re-read from the graph:

| Map's assertion | At v5.8.0 | |
|---|---|---|
| `DDD-frame-06` established | `established` | ✓ |
| `DDD-floor-01` *reported*, region-bounded per `DDD-dec-15` | `reported`; dec-15 present and re-scoping | ✓ |
| `DDD-frame-09` retired | `retired` | ✓ |
| `DDD-measure-08` retired | `retired` | ✓ |
| `DDD-floor-02` new, the relational floor, core/14 §3 | `projected`; core/14 §3 present | ✓ |
| `DDD-measure-11` verdict-not-search | `reported` | ✓ |
| `DDD-frame-11` governed domain wider than measured | `projected` | ✓ |
| `DDD-measure-15` admissibility | `projected` | ✓ |
| H-set `DDD-hyp-01`–`05` + `DDD-frame-07` umbrella | all `projected`, all `evidence: []`, all `owner: paper-4` | ✓ |
| `DDD-frame-13`'s credits carry the determinable literature | present, four locators | ✓ |
| `term:closure` — operational closure is canon's closure, decidable the special case | `settled`, exactly so | ✓ |
| `term:escape-mechanism`'s scope note | `settled`, carries "sufficient for escape, never necessary" | ✓ |
| `DDD-dec-24` for the filing provenance | present | ✓ |
| core/09 §3's computed example | present (`## 3. Worked example (fully computed)`) | ✓ |
| core/00 §4a the determinable | present | ✓ |

**Validator baseline at this commit** (recorded so any later movement is attributable):

| Gate | Result |
|---|---|
| upstream `validate-core-order.py core/` | exit 0, **0 errors**, 66 warnings — 59 W1 + 7 W2, **0 W4** |
| upstream `validate-claims.py core/claims/` | 60 claims valid |
| upstream `validate-claims.py core/decisions/ --decisions` | 8 decisions valid |
| upstream `validate-releases.py releases/` | 4 descriptors valid |
| downstream `validate-core-order.py core/` | 0 errors, 0 warnings |
| downstream claims / decisions | 26 claims, 20 decisions valid |

---

## 3. What head now contradicts, or adds, that the map could not carry

The map was written at Wave 3 against v5.7.0. Six items have moved. None invalidates the map;
four are gains, one is a name change, one is a residue worth a reader's attention.

### 3.1 §3 gains two citable nodes — both `draft` (gain)

`v5.8.0` minted **`term:commitment-level`** and **`term:residual-discretion`**, both established
by `core/14-indexed-determination.md` §2 — the exposition home `DDD-frame-02` already had. The map's
§3 row lists `DDD-frame-02` alone and no terms, because at Wave 3 the mint was deferred
("minting waits on use"; `DDD-frame-02` notes). The use arrived with the Track 1 determination
track, and `DDD-dec-26` records the mint.

**Both carry `status: draft`**, matching their establishing document. Paper A may cite them and
must show the status, exactly as it shows `projected` for the H-set. This is the only place in
the paper where a *draft* node is load-bearing.

### 3.2 `term:determinable` / `term:determinate` are now `settled` (name change)

The map calls them "new"; `DDD-frame-13`'s notes call them "status draft pending ratification".
At v5.8.0 both are **`settled`**. §2's determinable material is therefore firmer than the map
promises, not weaker.

### 3.3 `DDD-dec-26` rules directly on the ground-provenance taxonomy (gain — and a constraint)

The map's §2 row says the five-way "is **not** canon — institutional ground's mechanism is
Q27-gated (rev18); project as manuscript analysis or wait for the post-Q27 wave." `DDD-dec-26`
(new at v5.8.0) goes further and **rules the taxonomy ineligible for minting**, with the reason
stated:

> Minting a four-way variant would fix a partition Q27 may restructure, so no term is minted. The
> track carries the canon half — *a fact belongs to ground when information about it can change
> the resolution or its acceptance status beyond the declared tolerance* — as the definition …
> and carries the five-way taxonomy as track-native expository scaffolding, marked non-canon in
> line at the point of use, with the institutional slot flagged Q27-gated where it appears.

This is a **precedent Paper A's second authored section should follow**, and it is stronger than
"flag it": the ruling says *mark non-canon in line at the point of use*, not only in a closing
flag. It also supplies the canon half the section builds on — the ground definition itself.

### 3.4 `core/14` is `status: draft` (worth a reader's attention, not a blocker)

The exposition home for the paper's §1, §3 and §6 material is `core/14-indexed-determination.md`,
whose contract reads `status: draft, pending ratification`. The **claims** it exposits
(`DDD-frame-01`, `DDD-frame-02`, `DDD-floor-02`) are `projected` and they govern; the paper cites
claims, never the document, so nothing is blocked. Recorded because a paper that pins a tag should
know which of its exposition homes are not yet ratified.

### 3.5 `DDD-dec-26` still carries its `[PROPOSED]` banner inside a cut tag (residue)

`DDD-dec-26`'s `resolution` opens *"[PROPOSED — Emil ratifies at Gate 1; nothing below is settled
until he does.]"* and its `notes` open *"[PROPOSED] … Nothing in this file is ratified"*. Yet the
same file's body records the Gate 1 ruling as **made** ("now ruled (Gate 1, Emil)"), records a
Gate 3 ruling in its notes, and `DDD-frame-02`'s notes likewise say "now ruled (Gate 1, Emil)".
The file merged and was tagged at v5.8.0 with the banners unstruck.

Nothing substantive is open — the rulings are recorded. But **a reader of canon at v5.8.0 cannot
tell from the file's own words whether dec-26 is ratified**, and Paper A cites dec-26 for §3's
mint provenance. Reported, not repaired: striking a banner is a canon edit and this session files
nothing. It belongs on the next canon wave's list.

`DDD-frame-02`'s notes also carry a duplicated word at the hunk boundary — *"One / One consequence
was raised for ruling"*. Same disposition: reported, not repaired.

### 3.6 The measure note has never been in a downstream tag (a real pin seam — see §5)

---

## 4. Referenced sources: present, and one absent

The prompt's arrival discipline: *if any referenced source is absent at head, hold and report.*

| Source | State |
|---|---|
| The revision foundation | **present** — `meta/sessions/2026-08-18-wave3/revision-foundation.md`, 742 lines, committed at Wave 3 |
| The readiness map | **present** — `meta/sessions/2026-08-18-wave3/batch-p-projection-readiness.md` |
| Wave 3 successor items | **present** |
| The measure note (complete, with §6 discharge) | **present** at downstream head |
| The measure note's reviewer brief (P-5's pattern) | **present**, 986 words |
| The bibliographic verification record | **present** — Wave 3 `gate1-survey.md` lines 173–176, all four locators marked verified ✓ |
| Upstream assets (six) | **present** in `core/assets/` |
| **`paper-a-draft.md`** | **ABSENT — from both repositories, in full history** |

### The absent source, and why it does not stop the walk

The foundation's Purpose says it *"replaces the vulnerable conceptual foundation of
`paper-a-draft.md`"*, and its §14 is headed *"Immediate editing instructions for
`paper-a-draft.md`"*. That file **has never existed in either repository** — checked against the
full (unshallowed) history of both, not just head.

This is reported rather than treated as a blocker, on three grounds, and Emil should confirm the
reading:

1. The prompt states the position directly: *"the revision foundation is already in-repo …
   **nothing else is needed**."*
2. The foundation *replaces* the draft's conceptual foundation; it is the blueprint, and §12's
   structure is self-contained.
3. §14's two lists — *replace completely*, *preserve and adapt* — were **already discharged
   against canon by the readiness map**, which reports every "replace" item as having its
   replacement in canon and every "preserve" item as surviving with a canon cite. The work §14
   describes is therefore done in the map, and the draft is not needed to do it again.

What is genuinely lost with the draft is only its *prose*: §14's "preserve and adapt" list names
sentences (the thermostat example, "where you cannot check the work, you check the worker",
"last wind") whose original wording is unavailable. Each has a canon or foundation home for its
*content*, so the paper re-authors the prose rather than preserving it. **Flagged, not guessed.**

---

## 5. Two seams that need a ruling before drafting

### 5.1 The measure-note citation has no tag to resolve against

Paper A cites the measure note repeatedly by charter: §4.4's substitution ("cite the measure note
and `DDD-measure-02/03/06` through its front-matter pin rather than re-deriving"), the closure
taxonomy's §8 rung, and §4's standing/occasioned material (the discharge session's manifest
routes its `O(1)`/`O(N)` projection to Paper A explicitly).

**The measure note is not in any downstream tag.** `papers/measure-note/measure-note.md` was added
at `43f0f30` and is absent at v0.1.0, v0.2.0, v0.3.0 and v0.4.0 alike. The note's own front matter
pins *`decision-driven-design` at `v0.4.0`* — that pin governs the **downstream claim identifiers
the note cites**, not the note's own location.

So Paper A's pin line cannot say "the measure note at v0.4.0" — that would be false. The options,
for ruling:

| | Option | Cost |
|---|---|---|
| **A** *(recommended)* | Pin claim identifiers to `v5.8.0` / `v0.4.0`; cite the measure note **by path plus the commit that carries the discharge section** (`aa7e135`), and say so in one Reproduction-style sentence. | One honest sentence; mirrors exactly how the measure note handled its own sixth asset ("resolves at the next tag rather than at the pin"). |
| **B** | Ask for a downstream tag cutting the completed measure note before Paper A's pin is written. | Out of this session's scope to cut; blocks the pin line until Emil acts. |
| **C** | Cite only material present at v0.4.0. | **Loses the §8 constructive-closure rung and the whole discharge section** — i.e. loses the substance the charter sends the paper there for. Not recommended. |

This is the same seam the discharge session reported one gate-set ago ("the pin could not be made
uniformly true"), arriving from the other side.

### 5.2 Manuscript §-numbering: which "§8" carries the H-set?

The prompt says *"the H-set as §8 carrying predictions-never-findings"*. Every other §-reference in
the prompt (§4.1, §4.4, §5, "the §8/`term:training` gradient") is numbered against the **foundation
document**, where §8 *is* "Empirical hypotheses". But the manuscript blueprint is the foundation's
**§12 structure**, where §8 is "Worked example" and the H-set is §9.

**Recommendation: keep §12's order** — §8 Worked example, §9 Predictions and study design, with the
H-set in §9 — and read the prompt's "§8" as the foundation-document numbering it uses everywhere
else. The readiness map is indexed to §12's numbering and would otherwise need re-indexing.
Flagged rather than assumed; the skeleton is written on the recommendation and re-numbers in one
pass if Emil rules the other way.

---

## 6. The two authored sections: the partitions do not match their sources

**This is the largest item at this gate.** In both authored sections the prompt names a partition
that differs from the one the foundation and the readiness map carry. Both are reported; neither
is silently resolved.

### 6.1 The closure taxonomy — two different four-ways

| | Partition | Source |
|---|---|---|
| **The prompt's** | open / verification-closed / constructively-closed / formally-decidable | assembled from `term:closure`, `DDD-frame-06`, retired `DDD-frame-09` + `DDD-frame-05`, `DDD-measure-11`, the measure note's §8 rung |
| **The map's / foundation's** | logical / operational / economic / normative | foundation §5.1–5.4; the map calls this quadruple "not canon … present as manuscript analysis" |

These are not rival versions of one taxonomy. **The prompt's is a strength ladder** — how *much*
closure a predicate has, ordered, with the measure note's constructive rung slotted between
verification-closure and decidability. **The map's is a kinds taxonomy** — *which question*
closure is being asked about, four independent axes, no ordering. The prompt's five named sources
support the ladder precisely and say nothing about economic or normative closure; conversely the
foundation's §5.1–5.4 *is* the structure of manuscript §5, so the kinds taxonomy has to be handled
whatever happens to the ladder.

**Recommendation: carry both, with only one of them authored as the new section.** §5 opens on the
kinds taxonomy as foundation-native exposition (which is what the map already licenses — "present
as manuscript analysis"), and the **authored** section is the prompt's ladder, which is the piece
that genuinely needs new prose and that the measure note's §8 rung feeds. Outlined that way in the
skeleton. If Emil wants the section to be the kinds quadruple instead, or wants the ladder only, it
re-outlines at this gate rather than at Gate 3.

### 6.2 The ground-provenance five-way — a different five

| | Partition |
|---|---|
| **The prompt's** | sensory / recorded / derived / predicted / institutional |
| **The foundation's §2.2, the map's, and `DDD-dec-26`'s** | controlled / observed / inferred / institutional / missing |

Only *institutional* is common to both. The prompt attributes its five-way to "the foundation's §5
material"; the foundation's §5 is **Closure and evaluability**, and its ground provenance is at
**§2.2**. So the bullet carries two slips — the section number, and four of five slot names — or it
is a deliberately new partition.

It matters more than a naming quibble, for two reasons:

1. **`DDD-dec-26` ruled on the *specific* partition.** Its ineligibility ruling names
   controlled/observed/inferred/institutional/missing, and its stated reason — Q27 may restructure
   the partition — attaches to that partition's shape. A different five-way is not covered by that
   ruling and would be the paper proposing a partition of its own, which is closer to introducing
   a claim than the charter allows.
2. **The prompt's five-way loses `missing` ground**, which is load-bearing elsewhere: missing
   ground is what makes `DDD-hyp-02`'s first variable ("relevant ground unavailable to the
   computational system") a *ground* property, and the foundation's §2.2 stores the
   stored-statement-versus-current-observation argument in the controlled/observed split, which
   *sensory*/*recorded* re-cuts differently.

**Recommendation: author the section on the canon-adjacent five-way** —
controlled / observed / inferred / institutional / missing — because it is the one the foundation
states, the map names, and dec-26 ruled on; and carry the prompt's four fresh names, where they
earn their place, as *sub-distinctions inside* it (sensory and recorded both refine *observed*;
derived and predicted both refine *inferred*). That keeps every slot inside a ruled partition while
losing none of the resolution the prompt's names were reaching for. Outlined that way, with the
alternative preserved so Emil can rule it either way.

---

## 7. Additions beyond the map, proposed not taken

Six nodes are strong fits for sections the map lists without them. Each is **proposed here and
cited nowhere until ruled**, because carrying a node the bill of materials does not name is scope
growth, however apt.

| Node | Status | Proposed home | Why |
|---|---|---|---|
| `DDD-delivery-01/02/03` | projected ×3 | §4, with escape | Delivery failure *generates* escape — "filing is not encoding". The map's §4 row has escape and seams but no delivery; the paper's escape section is materially weaker without it. |
| `DDD-cost-25` | projected | §4.2 assurance | Pre-act / at-act / post-act positions with latency — canon's form of the foundation's "before, during, or after" sentence, which §4.2 carries verbatim otherwise. |
| `DDD-ground-05` | projected | §2 | Declaring the determinable space is constitutively prior to determination over it — the ground/determinable symmetry §2 is otherwise stating register-native. |
| `term:store` | settled | §4, the seam guard | The other half of the guard: `{rule, check, actor, nothing}`, "there is no fifth source", against frame-15's four modes. The guard cannot be stated in prose without both partitions. |
| `DDD-frame-12` | projected | §9 or §10 | A claim is an act with a deferred verdict — relevant to how the H-set's falsifiers are in flight. Weakest of the six; easily dropped. |
| `DDD-agent-01` | projected | §10 or omit | Long-running agent drift as escaped decisions from basis loss. A vivid boundary case; also the furthest from the map. Proposed with least confidence. |

`term:store` and `DDD-delivery-02` are the two the drafting will most feel the lack of.

---

## 8. Held for ruling at this gate

1. **The pin seam** (§5.1) — option A, B or C for citing the measure note.
2. **Manuscript numbering** (§5.2) — §12's order kept, or the H-set moved to §8.
3. **The closure taxonomy's partition** (§6.1) — both, ladder only, or kinds only.
4. **The ground-provenance partition** (§6.2) — canon-adjacent five with the prompt's names as
   sub-distinctions, or the prompt's five as given.
5. **The absent `paper-a-draft.md`** (§4) — confirm it is not needed, as the prompt states.
6. **The six proposed additions** (§7) — which, if any, enter the bills of materials.
7. **Q36's pull material** — the map has it "available as positioning prose, deliberately
   unfiled" for §11. The prompt's out-of-scope list names Q38b's asymmetry material (one forward
   sentence permitted) but is silent on Q36. Does §11 carry it, and at what length?
8. **The word target** — 8,000–11,000 with the measure note's rule governing ("as long as its
   booked content, reported honestly"). The skeleton's per-section estimates total ~10,650; the
   estimate is reported with the count method stated so the two are comparable at Gate 5.
