# GATE 1 — the classification reconciled against head

**Status: RULED (Emil, 2026-09-01).** Nothing in canon is touched by this gate.

> **The ruling, recorded verbatim in substance:** (1) reconciliation and removal attributions
> accepted as read. (3) **The frozen instrument's ledger governs**; 380/187 is recorded as a
> prediction that did not verify; the nine-row divergence is a finding with a name — *a figure
> whose instrument was not committed is not reproducible* — filed as the **fourth method
> mechanism** in the seed. The 185≈187 coincidence stays flagged as coincidence: two independent
> instruments landing two apart is not agreement. (2) The 80 proposed senses accepted; both
> boundary cases and the two-row README divergence recorded rather than resolved — `ground by
> provenance` is SR-4's territory and is not settled by a sense assignment. (4) Wave sizes
> accepted, including W1's +1 — a row found by reconciliation is the reconciliation working;
> booked. (5) **The 54 bare unbooked rows go to G5. The 134 unruled meta additions are out of
> scope by name** — they are programme meta, and a migration that rewrites its own audit trail is
> editing history; any of the 134 that is a live surface rather than a record is named
> individually at G5 or stays as written. Carried into G2: the delivered/judgment/default trio was
> cut rather than moved, so its shape survives in the corpus without its clearest instance —
> **a replacement instance for that shape is selected deliberately at G2**.

**Read at:** `actor-indexed-determination` `81f6929` (= annotated tag **`v5.12.0`**, verified — tag
and branch head are the same commit) · `decision-driven-design` `d89ed55` plus this session's
arrival commit · `product-cli` `d0f4297` — **the same commit the predecessor read.** That repository
has not moved.

The arrival record was committed first, per `DDD-dec-20`
(`meta/sessions/2026-08-31-ground-migration-exec/`, prompt and bootstrap verbatim).

---

## 1. Method

The baseline is the audit's committed extract (2,845 rows) carrying the senses `w0-classify.py`
assembles — residual zero by construction. The corpus has moved, so every baseline row was matched
to head **by content, never by line number** (the seed's third method mechanism): per file, greedy
multiset matching on the token plus a whitespace-normalised anchor, four passes of decreasing
width (full context, 240, 80, 32 characters), then one named cross-file pass for the
`paper-a.md` → `paper-a-supplement.md` split. A baseline row with no head match is **removed**; a
head row with no baseline match is **added**. `g1-reconcile.py` is the instrument;
`g1-head-extract.json` and `g1-delta.json` are its outputs.

To isolate what the two merged sessions changed, the same extraction was run at **point A** — the
predecessor's read commits (`ce2c477` = `v5.11.0`, `e81a454`, `d0f4297`). Everything between the
audit's extract and point A was already discharged at the predecessor's GATE 4 (§8, the head
delta); the A→head delta is therefore exactly the two merged sessions' movement. `g1-pointA.py`
reproduces it.

**Two instrument defects were found while matching and fixed before any figure was read** (both
disclosed because the matcher is now part of the record): the baseline rows carry no token offset,
and recovering it naively mis-centred anchors on neighbouring tokens — fixed by taking the
token-boundary match closest to the extractor's deterministic offset of 120; and rows whose
contexts contain a neighbour's anchor could inherit the neighbour's ruling — fixed by preferring
the anchor nearest the token. The residue of the first defect, before the fix, was 53 phantom
removals; after it, every removal survives a hand read.

## 2. The reconciliation, in one table

| | rows |
|---|---|
| baseline (the audit's extract, classified) | **2,845** |
| point A (the predecessor's read commits) | 2,973 |
| **head** | **3,123** |
| matched baseline→head (of which moved into the supplement) | 2,823 (24) |
| removed baseline→head | 22 |
| added baseline→head | 300 |
| **A→head: matched / moved / removed / added** | **2,955 / 27 / 18 / 168** |

**No matched row changes sense.** Senses travel with content; every changed sentence surfaces as a
removed/added pair below, and each pair was read.

## 3. What the two merged sessions changed

### The ground-migration session's merge (upstream PR #19→`v5.12.0`; downstream record and seed)

- **Upstream: one reworded row and one immutable file.** `releases/v5.12.0.yaml` adds 13 rows
  (A9, immutable, counted never migrated). `README.md`'s judgment row is the one reworded pair —
  *"an actor reading ground"* → *"an actor reading ground, **with an accountable party named**"* —
  the §6 repair, S3 before and after. **Gate 5's claim that §6 moved no `ground` occurrence's sense
  or wording verifies**: the clause was inserted beside the word; the predication is unchanged.
- **Downstream: the programme's own artefacts.** The erratum (+23), the seed itself (+16), the
  audit's forward reference (+3), `meta/sessions/README.md` (+3). All are programme meta, in the
  unruled bucket of §6 below.

### The Paper A revision (PR #32)

- **W1's 15 moves verify by count**: 14 rows leave `measure-note.md` and 1 leaves `paper-a.md`,
  every one S5, exactly the session's recorded 15 — the occurrences now read `deployment
  distribution` and no longer contain the token.
- **One S3 sentence was cut, not moved**: *"'Judgment' is variation produced at the act by an actor
  reading ground"* — the delivered/judgment/default trio left the paper in the narrowed-claim
  revision. A qualified row, so not migration surface; noted because G2 loses that sentence as a
  precedent candidate and because the README still carries the same gloss.
- **27 rows moved wholesale into the supplement**, wording intact, matched by the cross-file pass.
- **Added**: 25 in `paper-a.md`, 15 in `response-to-review.md`, 12 net in the supplement, 1 in
  `measure-note.md`, 2 in `DDD-dec-34.yaml`, 6 in `meta/successor-items-paper-a-revision.md`, and
  48 in its own session record (B13, immutable).

### Removals older than the seed, surfacing only now

Two S1 rows died in the `README.md` rewrite the item-4 session made (the audit's extract still
carried the two-occurrence README; §8 booked the rewrite as "2 → 19"). Discharged there; listed
here so the removal count reconciles. Four U rows in `paper-a.md`'s old Appendix A
(`DDD-ground-01/02/03/05` node-table rows) match their regenerated successors in the supplement —
generated rows, which the seed's corollary says are never a wave's to move.

## 4. Proposed senses for the live added rows — draft-pending-ruling

Eighty of the 300 added rows sit on live surfaces; each has a proposed sense **keyed by content**
with a one-clause reason in `g1-added-rulings.py`, applied by the audit's own decision rule (the
predicate applied to the word, never the compound). The split: **S1 ×20 · S2 ×16 · S3 ×20 ·
S5 ×2 · U ×22.** Highlights Emil should see rather than trust:

- **`README.md` re-derived**: S1 ×7, S2 ×5, S3 ×4, S5 ×1, U ×2. The predecessor's aggregate was
  S1 ×8, S2 ×4, S3 ×4, S5 ×1, U ×1 over the same nineteen; its per-row list was never recorded, so
  the two divergences cannot be located exactly. Candidates: I read *"holding ground fixed"* (L164)
  as S2 and *"ground truth"* (L271) as U-ordinary.
- **Two boundary cases flagged, not decided**: `paper-a.md`'s *"its ground by provenance"* and
  *"ground provenance (§2.4…)"* — proposed S2 on SR-4's reading (provenance is an attribute of the
  held object), but they sit exactly on the S4-dissolution boundary.
- **The two S5 additions**: `README.md`'s *"verdict induced … over the ground distribution"*
  (mutable, and **new to W1's ledger** — see §7) and a regenerated supplement row quoting
  `DDD-measure-16` (generated; moves when canon moves, per SR-5's bound).
- The remaining 220 added rows are **counted, not ruled**: 86 immutable (release descriptors,
  session records) and 134 downstream programme meta — the audit report (+64), the erratum (+23),
  the seed (+16), three successor-items files (+31). Proposed disposition: audit output and the
  seed are frozen as record; the successor-items files are live meta prose and land with the
  dn-meta surface in §5. **G5's "whatever G1 surfaces" is the hook.**

## 5. The bare/qualified split — a finding, then a divergence, recorded

**The instrument behind the seed's 380/187 was never committed.** The figure exists in
`gate4-plan.md` §1 and the seed; the row list exists nowhere. The migration's body — *which* 187 —
was therefore not inheritable, and had to be rebuilt.

`g1-bare.py` rebuilds it, anchored per the seed's first method mechanism: a 40-character window
**clipped at clause boundaries** (a comma does not clip; a sentence stop, semicolon, dash, list
separator or table pipe does), with the qualifier lexicon drawn from the audit's own predicate
lists. Two revision rounds widened the lexicon, **each addition warranted by a sampled row read
before the resulting figure was known** (`checks`, `consume`, `emit`, `pre-resolve`,
`accessibility`, `assurance`; then `encode`, `verifiable`, `trusted`, `at act time`); the
instrument froze after the second round regardless of what it then said. Per-rule precision, per
the second method mechanism, from hand-read samples: **qualified 24/24; bare 9/12** (the three
misses are borderline qualifiers — `controlled`, `in hand`, `usable as` — left outside the frozen
lexicon).

Against the same 567-row baseline population (which reproduces exactly):

| | qualified | bare |
|---|---|---|
| the seed's figure | 380 | 187 |
| frozen instrument, baseline | 389 | 178 |

**Divergence: 9 rows, recorded, not reconciled.** The two instruments disagree row-wise more than
the totals show; since the row list behind 380/187 is unrecoverable, the frozen instrument's
ledger (`g1-bare.json`, `g1-head-ledger.json`) is proposed as the working list, with every bare
row still individually ruled in G4 under G2's precedents — the instrument sizes the waves, it
never edits.

## 6. At head, the corrected sizes

S2/S3 prose population at head (canon + projection, mutable, non-identifier): **601 = 416
qualified + 185 bare.** (That 185 sits near the seed's 187 by coincidence — different corpus
state, different lexicon; the numbers must not be conflated.)

Bare, per area: up-core **36** · dn-apparatus **46** · dn-papers 22 · dn-projections 14 ·
dn-core 8 · dn-applications 5 — and **outside every booked wave**: up-other (upstream `meta/`,
`CLAUDE.md`) 20 · dn-meta 28 · dn-other 6.

## 7. The corrected wave sizes

| Wave | Seed | **At head** | Notes |
|---|---|---|---|
| **W1** | 73 of 88 remain | **74** mutable excl `product-cli` | = the 73 the Paper A session recorded **+ 1**: `README.md`'s S5 row, in the §8 delta and never in W1's ledger — needs booking in. Of the 74, 5 are generated rows (supplement ×4, `paper-a.md` ×1) that move when canon moves, and 13 sit in `core/assets/*.py` code |
| **W2** | 11 + 11 + 65 | 11 + 11 + **36 bare** (registry and embeds re-verified at G3) | the 65→36 gap is the instrument divergence of §5: 29 rows the frozen lexicon reads as already verb-qualified |
| **W3** | 122 | **95 bare** (46 apparatus + 22 papers + 14 projections + 8 core + 5 applications) | same divergence, same direction |
| **surfaced, unbooked** | — | **54 bare** (20 up-other, 28 dn-meta, 6 dn-other) + the 134 unruled meta additions | proposed for G5, which the prompt already reserves for "whatever G1 surfaces" |
| **W4** | 1,203 | **1,203 — exact** (S2 1,181 · S3 19 · S4 2 · S5 1); `.ddd/` = **660 in 70 files, exact**; repo unmoved at `d0f4297` | assessed at Gate 6, never executed |
| **never** | U + immutable | U 280 · immutable 260 + 86 added | identifiers still 142; SR-6 holds |

Head sense totals, with proposed rulings included: S1 585 · S2 1,545 · S3 387 · S4 22 · S5 84 ·
U 280 · unruled 220. Canon remains S1-led. Canon's S4 remains zero — the 22 are downstream and
`product-cli`, unchanged.

## 8. What this gate asks

1. **The reconciliation** (§2–§3): matched senses carried by content; the 22 removals and their
   attributions as read.
2. **The 80 proposed rulings** (§4), the two flagged boundary cases, and the two-row README
   divergence against the predecessor's aggregate.
3. **The bare ledger** (§5): does the frozen instrument's row list govern G4's body, with the
   seed's 380/187 recorded as the prediction that did not verify? The alternative — treating 187
   as binding and hunting 9 rows to make it true — is exactly the reconciling the method rules
   forbid.
4. **The wave sizes** (§7), W1's +1 booking included.
5. **The 54 + 134 unbooked rows** (§6, §4): to G5, or ruled out of scope by name?
6. **G2's selection universe**: with a ruling on (3), the twenty precedents are drawn from the
   185-row bare ledger — every distinct sentence shape, hardest first, at least one S2 and one S3
   that the delivery vocabulary must name.

**Nothing repaired. Nothing merged. Holding at GATE 1.**
