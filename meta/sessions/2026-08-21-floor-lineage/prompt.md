# Session prompt — the floor: definition placement and lineage

Repositories: `actor-indexed-determination` (upstream, head — canon at **v5.8.0**) and
`decision-driven-design` (downstream, head — Paper A merged). Fetch both.
Session type: **interactive canon curation.** Hold at every gate. Supersession, never rewriting
(precedent: DDD-dec-09/10/15). British spelling; one idea per sentence.
**First act, before Gate 1:** commit this prompt and bootstrap to
`meta/sessions/2026-08-21-floor-lineage/` in `decision-driven-design`, per DDD-dec-20.

## What this session is

A small, bounded repair to `core/03-the-floor.md` and its lineage register. Four items, found by
reading the document at head. **No claim statement moves**: `DDD-floor-01` and `DDD-floor-02` are
untouched in statement, region, and falsifier. This is prose, registry, and lineage work.

**The session's virtue is closing items at booked size** (the freight precedent). If an item
resists its booking — particularly F-3's novelty reconciliation — it defers with the resistance
named rather than growing a design session inside this one.

## The four items

### F-1 — the definition arrives after its own use

`03` states the floor's definition (the portion of a determination's demand that cannot be moved
off the in-the-moment actor; the residue no encoding or checking can amortise, paid per run in
judgment) **after** the claim block, so the reader meets the claim about the floor before learning
what a floor is. Move the definition ahead of the claim, as the document's opening move.

**Registry question the session must answer first:** does `term:floor` exist in the upstream
registry, and what is its `established_by`? Three cases, each with a different repair:
- exists and is established by `03` → the definition becomes the document's embed, byte-exact, and
  the embed checker verifies it;
- exists and is established elsewhere → `03` embeds or cites it per the registry's convention;
- does not exist → **minting is a filing and needs Emil's ruling** — the session reports and holds
  rather than minting on its own motion.

### F-2 — the phenomenon has no named ancestor

`03` attributes its three limits carefully (Rice; inevitable model error — Xu, Jain & Kankanhalli
and Kalai & Vempala, with Suzuki et al. as the rebuttal; Collins on collective tacit knowledge) and
its degeneracy mechanism (Edelman & Gally 2001). It names **no ancestor for the floor itself** —
the phenomenon of an irreducible residue — while opening on a novelty claim.

Repair, in two places per canon's own convention (lineage lives in `meta/lineage-and-limits.md`;
core documents point at it):
- **`meta/lineage-and-limits.md`** gains the ancestry entries, each with what it contributes and
  where it differs. Candidates, all to be **verified or flagged, never asserted from memory**
  (the freight A-8 / Paper A Tesler discipline): Polanyi (1966) — irreducibility in the knower, and
  Collins's direct antecedent, so citing Collins without him is a dangling lineage; Wittgenstein,
  *Philosophical Investigations* §201 — no rule contains its own application; Hayek (1945) —
  irreducibility by dispersion; Brooks (1987) — essential complexity, already in the register;
  Bainbridge (1983), *Ironies of Automation* — the operational form, automation leaving the residue
  to the human; Dreyfus and Suchman (1987) — embodiment and plans underdetermining situated action.
  The session may add or drop candidates on the evidence; each entry states the contribution and
  the difference.
- **`core/03`** gains a short "what is not new here" paragraph — three or four sentences naming the
  tradition, pointing at `meta/lineage-and-limits.md` for the register, and stating the contrast
  that makes the original move legible: **none of the ancestors locates irreducibility in the
  checkability of the acceptance predicate, arrangement-indexed.** The ancestry strengthens the
  claim by contrast; draft it that way, not apologetically.

### F-3 — two novelty claims in one repository

`03` opens by calling itself the framework's best original result. `meta/lineage-and-limits.md`'s
novelty statement was corrected at v5.4.0 to concern capacity-generated escape. Both are ratified
prose and they compete.

**Report before repairing.** The session states both verbatim, says whether they are genuinely in
tension or scoped differently (one may be "best result", the other "the novel identification"), and
proposes the minimal reconciliation. Emil rules. If the honest finding is that reconciling them
requires deciding what the framework's primary contribution *is*, that is a design question and
**defers whole** with the resistance named.

### F-4 — Paper A may project `03` without `03`'s warrant

Paper A's bibliography (ten entries at its Gate 4: Johnson, Prior, Funkhouser, Wilson, Shannon,
Ashby, Brooks, Meyer, Goodhart, Tesler-flagged) appears to carry **none** of `03`'s own sources —
no Rice, no Collins, no Edelman & Gally — while the paper projects the floor result.

**Verify first, repair only if mechanical.** If the gap is real and the fix is citation-only
(bibliography entries plus in-text citations at the points where the paper projects `03`'s limits),
it rides this session as a second, downstream PR. If it would require argumentative prose — if the
paper *states* the limits rather than citing them — it defers to a Paper A revision session with
the finding recorded. No manuscript argument is rewritten here.

## Walk

1. **Fetch, inaugurate, survey.** Both repos at head; session record committed. Answer F-1's
   registry question with node IDs; quote both novelty statements verbatim for F-3; run the
   bibliography check for F-4 and report the exact gap; list the lineage candidates with a
   verification plan. **GATE 1 — hold on all four dispositions.**
2. **F-1 and F-2.** Definition moved (and embedded per Gate 1's ruling); lineage entries with every
   locator verified or flagged in its own entry; `03`'s contrast paragraph. **GATE 2 — hold.**
3. **F-3 and F-4** per their Gate 1 rulings. **GATE 3 — hold.**
4. **Close.** Basis-impact sweep (no claim statement should have moved — verify and report);
   quotation checker over any block quotes added; validators both repos; reference closure; branch
   per repo; PRs upstream-first; manifest. The session proposes the version bump with reasoning —
   prose-only suggests a patch, a registry change suggests a minor. **GATE 4 — hold.**

## Out of scope

Any change to `DDD-floor-01` or `DDD-floor-02`'s statement, region, or falsifier. The Q-wave and
both of Paper A's pending flags. The carve. The training-gate supersession. S-1, Q37, G-track. The
three instrument freight items. Minting `term:floor` without a ruling. Rewriting Paper A's
argument. Do not bundle.

## Standing note

Commit drafts before reporting at each gate, bodies marked draft-pending-ruling. `03` is ratified
canon and its result stands — this session makes the document say what it already means, and gives
its claim the ancestry that makes its novelty checkable. A novelty claim whose prior art is
unstated is not a stronger claim; it is an unbounded one.
