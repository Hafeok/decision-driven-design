# Session prompt — item 4: status, kind, and the validator

Repositories: `actor-indexed-determination` (upstream, head — canon at **v5.10.0**; verify) and
`decision-driven-design` (downstream, head). Fetch both.
Session type: **interactive canon curation.** Hold at every gate. Supersession, never rewriting.
British spelling; one idea per sentence.
**First act, before Gate 1:** commit this prompt and bootstrap to
`meta/sessions/2026-08-25-item4/` in `decision-driven-design`, per DDD-dec-20.

## Scope correction — read before anything else

An earlier triage claimed the registry needed a second field carrying **kind**, separate from
maturity. **That was wrong, and checked wrong.** `kind` has existed since format 1
(`spec/claim-format.md`), is populated on all 63 upstream claims and on every downstream claim, and
spans ten kind×status combinations. The reviewer's observation was about **Paper A's appendix**,
which renders `id | status | statement` with no kind column; the triage escalated a projection
defect into a schema defect without asking the graph.

The session inherits the corrected scope below. **Do not re-derive the schema change; there isn't
one.** Where this prompt and the triage conflict, this prompt governs, and the triage's §2 carries a
correction note when its file is next touched.

## What this session is

Four items on one surface — the claim schema, its validator, and how both are read from outside.

### I-1 — the two rulings that are the real work

**(a) Does `conceptual` split?** The reviewer's four kinds were *definitional · formal · empirical ·
normative*; canon's are *conceptual · formal · empirical · normative*. If `conceptual` is carrying
both definitions and substantive conceptual claims, the largest cell in the table
(29 conceptual/projected) is doing two jobs. **Survey before proposing:** read all 29 and report how
many are definitions in the reviewer's sense. If the split is real, propose it; if `conceptual` is
coherent, say so and file nothing.

**Interaction the session must carry into I-2:** if some conceptual claims are definitions, then
falsifier-presence enforcement has to say what a definition's falsifier looks like — a definition
fails by being unusable or by carving the wrong joint, not by an observation. Answer this before
proposing any enforcement rule.

**(b) `retired` is a lifecycle state sitting in a maturity field.** Four claims are retired
(formal ×3, conceptual ×1), two of them created last session. **The information loss is the
argument:** `DDD-measure-06` was `established` and `DDD-frame-15` was `projected`; both now read
`retired`, and the field no longer distinguishes a once-established claim that fell from a young one
that was replaced. For a public registry that is a real loss — an external reader cannot see that a
claim reached `established` and did not survive.

Options to draft, not to pick: keep `retired` as a terminal maturity value and record the prior
value elsewhere; add a lifecycle field (`active` / `retired`) orthogonal to maturity; or a
`retired_from:` field on the node. **Test whichever against:** can a reader see, from the graph
alone, that `DDD-measure-06` was once `established`?

### I-2 — the validator gap (Phase 1a's freight item, folded in deliberately)

`validate-claims.py` enforces neither **falsifier presence** nor **`spec/claim-format.md` rule 1**
(single-limb statements). This is the same registry-and-validator surface as I-1, and
`DDD-measure-06` is the worked example for both defects: its compound statement is why rule 1 needs
enforcing, and its missing falsifier is how it escaped scrutiny for five minor versions. **One
instrument, one session — this is not bundling.**

Both checks must be run against the existing corpus **before** being proposed as enforcing, and the
hit list reported. A check that would fire on twenty ratified claims needs a migration plan, not a
merge. Warning class or error class is Emil's ruling, informed by the count.

### I-3 — the appendix renders `kind`

The projection-side gap, and it is one column plus a regeneration. `gen-appendix.py` gains a `kind`
column; the appendix regenerates wholesale (never hand-edited); the independent re-read verifies it;
`check-quotations.py` unaffected. **Constraint:** the pin is held at v5.9.0 by a standing ruling, so
Paper A's appendix regenerates against the pinned ref and its four known-failing quotations stay
failing — that is Phase 1a's predicted state, not a defect introduced here.

### I-4 — status semantics for external readers

Documentation, not schema. A short section — in `spec/claim-format.md` or `meta/`, the session
proposes which — stating plainly what each maturity value means and, more importantly, **what it
does not mean**: `established` means internally argued and unchallenged, not externally validated;
`reported` means exercised by a computation, not empirically supported.

**The exposure is narrower than feared and the number should anchor the writing: `established` is
four claims, all `formal`.** Write to that fact rather than to a worry.

## The worked precedent

Phase 1a already performed this session's move by hand, once, because the schema had no field doing
the work: `DDD-measure-16` (formal/established) split from `DDD-measure-17` (conceptual/projected)
along the arithmetic-versus-modelling line. Reason from it — it is the shape of what a populated
`kind` column is supposed to make visible without a session having to do it node by node.

## Optional warm-up — W1

The ground audit's W1 (the population sense leaving for **deployment distribution**) is independent
of everything here: 105 occurrences, zero identifiers, zero pins, one in `product-cli`, and 29 in
merged papers so it rides with a paper revision rather than replacing one. It may be taken in this
session **as its own commit and its own gate**, or left. Emil rules at Gate 1; if taken, it does not
mix with I-1 to I-4 in any commit.

## Walk

1. **Fetch, inaugurate, survey.** Both repos; session record committed. The kind×status table
   verified at head; all 29 conceptual/projected read and classified for I-1(a); the four retired
   claims with their prior statuses recovered from git history for I-1(b); both I-2 checks run
   against the corpus with hit lists. **GATE 1 — hold on the survey, the I-1 proposals, the I-2
   counts, and the W1 ruling.**
2. **I-1** as ruled. **GATE 2 — hold.**
3. **I-2** — the two checks, with migration plan if the hit lists warrant one. **GATE 3 — hold.**
4. **I-3 and I-4.** **GATE 4 — hold.**
5. **Close.** Basis-impact sweep; instruments with predictions stated before operations; validators
   both repos; reference closure; appendix regenerated with independent re-read; branch per repo;
   PRs upstream-first; manifest. Version proposal with reasoning. **GATE 5 — hold.**

## Out of scope

The ground migration (item 5) and its W0 classification grind. Paper A's revision, including the pin
advance and the four failing quotations. The measure decoder repair. The Q-wave. The primer. The
carve. The NGO transfer. Do not bundle.

## Standing note

Commit drafts before reporting at each gate, bodies marked draft-pending-ruling. This session goes
before the migration for a mechanical reason: it touches every claim file's **header**, and the
migration touches statements, regions and notes in the same files. Schema final first means the
migration never re-touches what it just edited. Keep it that way — nothing here should edit a
statement.
