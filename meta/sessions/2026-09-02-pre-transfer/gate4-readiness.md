# GATE 4 — the publication readiness sweep (I-4)

**Status: draft-pending-ruling. A report, not a repair pass.** Emil rules what files now and what
carries to the transfer. Led, as ruled, with the invocation defect — which leads as an erratum.

---

## 0. ERRATUM first: the invocation defect retracts, and so does half of a second finding

**The GATE 3 instrument note was wrong, and the defect was this session's, not the checkers'.**

Tested directly, with exit codes captured with no pipe in between, every bad invocation of all
three Paper A checkers exits non-zero:

| Invocation | check-quotations | check-appendix | check-status |
|---|---|---|---|
| no arguments | 1 | 1 | 1 |
| unrecognised flag (`--bogus`) | 1 | 1 | 1 |
| two arguments (`--upstream <path>` — the session's own mistake) | 1 | 1 | 1 |
| swapped argument order | — | 1 | — |

`gen-appendix.py` (1), `generate.py` (2), `validate-claims.py` (1) and `validate-core-order.py`
(1) also exit non-zero on bad invocations. **Emil's exit-code rule is already satisfied by every
instrument tested.**

What actually happened: the session measured exit codes as `script | tail -N; echo $?` — which
reports **`tail`'s** exit status, always 0. The "docstring + exit 0" observation was an artefact
of the session's own measurement harness. The finding is retracted; the GATE 3 record carries an
erratum note pointing here rather than a silent edit.

**Half of the unpinned-embeds finding retracts with it.** The three ids embedded in downstream
`core/14-maturation.md` and `core/16-calibration-ledger.md` (`term:waterline`, `term:maturity`,
`term:calibration-ledger`) are **not** unwatched: they live in the downstream repository's own
registry (`core/graph/terms.yaml`, 5 terms) and the canonical invocation
(`validate-core-order.py core/`) validates their embeds (4 embedded, 0 errors). What remains true
and reportable: **run from the repository root (`validate-core-order.py .`), the tool
misclassifies the downstream-registry ids as unpinned upstream ids and FAILS with 4 spurious E13s
on a tree the canonical invocation passes.** A stranger cloning the public repo and running the
validator the obvious way sees a failing canon gate. That is a mode inconsistency in the
instrument, not an unwatched surface.

**The unwatched-surface class, recounted honestly:** three prior instances stand (the
column-count guard, the zero-citation render, the abstract past three green checkers). The fourth
and fifth named at GATE 3 correct to: a validator mode inconsistency, and — the genuine new
instance — **this session's own rc-through-pipe measurement**: a harness reporting success where
it did not look, exactly the class's shape, found only because the retraction check re-ran
everything without the pipe. The class finding stands, with the newest instance being the
session's, and the lesson sharpened: the checkers were sound; the checking of the checkers was
not.

## 1. Statuses that overstate their evidence (charter item)

`spec/claim-format.md` §5: `reported` claims "at least one evidence entry whose asset reproduces."

- **`DDD-measure-11`** — conceptual, `reported`, evidence: one `derivation` entry
  (`core/09-the-measure.md` §7, §9 caveat 1). No asset.
- **`DDD-measure-13`** — formal, `reported`, evidence: one `derivation` entry (`core/09` §5, third
  bullet). No asset.

Both are exactly the defect the charter names. Facts that price the ruling: **neither is pinned
downstream**, so a demotion fires nothing; **the primer already reads both conservatively as
`projected`** (its §6 says so in terms); the primer session's filter already found them, so this
is the second session to look and decline to leave them. Dispositions for the ruling: (a) demote
both to `projected` now — cheap, honest, aligns canon with how its own projection already reads
them; the derivation evidence stays recorded; (b) write the missing assets — out of this session's
scope; (c) record why they wait. The primer's §6 warning would need no change under (a).

No third instance: the primer's filter swept all eleven `reported` claims and found exactly these
two derivation-only; that sweep is cited rather than redone.

## 2. Anything asserting external validation: clean

Both repositories swept, world-facing surfaces (`core/`, READMEs, `spec/`, `apparatus/`,
`applications/`, `projections/`, `papers/`), two pattern families (strict: "external validation",
"empirically confirmed/validated", "validated against", "field-tested", "proven in practice";
soft: "has been shown", "we show that", "demonstrates that", "confirmed by", "verified in
practice", "real-world evidence/results"). **Every hit is a denial or the §5 definition** ("not
presented as external validation"; "Neither field claims external validation"; the DORA doc's
"was *not* validated against"). Zero assertions found. The I-2 repairs removed the nearest
approaches ("tested against", "explains", "results").

## 3. Claim/term disagreements beyond I-1

- **NEW, front page: the closure bounds count.** `term:closure` (settled), `core/03` §, and
  `DDD-measure-16`'s quotation all say closure is evaluable "within declared **resource, latency,
  and confidence** bounds" — three. Upstream `README.md:117` says "within the declared resource,
  latency, confidence, **and assurance** bounds" — four. The same defect family as the arity, on
  the front page of the settled term's own repository. (The likely source: `DDD-floor-02`'s
  relation tuple carries `assurance` as a separate coordinate; the README merged the enumerations.)
  **Not repaired — the repair direction is a ruling:** either the README drops "assurance" and
  conforms to the settled term (one word, I-2 family), or the term is wrong at settled grade,
  which is a supersession question nobody has raised. The cheap reading is the first.
- **Checked and clean: `term:floor` vs `DDD-floor-02`.** The same shape as the arity — a settled
  term locating the floor in the predicate, a projected claim relocating it to the six-coordinate
  relation — but the claim's own `region` already states the reconciliation: "Consistent with, not
  competing against, term:floor — the acceptance predicate is a coordinate of the relation." This
  is disposition C avant la lettre, and evidence the I-1 ruling generalises.
- **Checked and clean:** `term:store`, `term:commitment-level`, `term:arrangement` against their
  README and claim carriages — counts agree everywhere.
- The `core/05` four-element sentence was the arity's third count — repaired at I-1.

## 4. Dangling references to artefacts that do not exist (mechanical pass, both repos)

Method: every markdown link and backticked repo path in every `.md`, resolved against the
referencing file's directory and the repo root. Raw total ≈ 250; ~215 are in dated records,
CHANGELOGs and session files — **correct as history, no repair proposed**. The live findings:

**4a. The worst artefact finding of the sweep: `applications/sdlc/` does not contain the v3
framework the front page says it contains.** The downstream README (twice) and
`applications/sdlc/README.md` present the four v3 design documents — `01-foundations.md`,
`02-entity-reference.md`, `03-autonomy-levels.md`, `04-implementation.md` — as "retained" and the
framework as "**intact** — it now lives in `applications/sdlc/`". None of the four files exists
anywhere in the tree; the directory holds only the README and `production-as-ground.md`. History:
the docs lived under `docs/` and were deleted at commit `219ad6c` ("rewrite"); they were never
landed at the advertised path. A stranger clicks four dead links under an existence claim. This is
simultaneously a dangling-reference finding and an I-2-class front-page over-claim ("That
framework is intact"). Dispositions for the ruling: restore the four docs from `219ad6c^` (content
landing — a projection nobody in this session ruled); or repair the claims to match the tree (the
links point at history, the "intact" sentence weakens to what is true: retained in history,
`production-as-ground.md` and the reference implementation carry the projection today). The second
is this session's shape; the first is real work someone must own.

**4b. The cross-repo reference class (the split's residue), world-facing members:**

| Referencing file (downstream) | Dangles to | Note |
|---|---|---|
| `README.md` (front page, as **links**) | `core/01`, `core/03`, `core/04`, `core/09`, `meta/lineage-and-limits.md` | 404 on the public site; the objects live upstream. The reading-order section *says* the theory lives upstream, then links it repo-relatively |
| `CONTRIBUTING.md`, `LICENSE.md`, `meta/way-of-working.md`, `meta/the-declaration.md` | `meta/lineage-and-limits.md` | lives upstream only; the declaration is embedded in the primer, so the primer inherits the reference textually |
| `spec/claim-format.md` | `spec/claim-format-2-addendum.md` | the downstream spec names an addendum "in force" that exists only upstream — a reader of the public downstream repo cannot find the rules the spec says bind it |
| `apparatus/closure-principle.md` | `core/00-determination.md` | doubly stale: cross-repo AND the pre-renumber document name that no longer exists upstream either |
| `apparatus/adversarial-ground.md`, `papers/measure-note/*` (4 files), `paper-a-supplement.md` | various `core/*`, `core/assets/*` | same class |
| `core/13-cost-projection.md`, `core/14-maturation.md` | `meta/mdl-cost-manufacturing-assessment-2026-08-08.md` | the record exists upstream only |

One repair shape covers the class: cross-repo references become explicit upstream URLs (or a
stated "upstream:" prefix convention), starting with the front page's five links. The full-corpus
rewrite is a session of its own; the front-page links are publication-critical now.

**4c. Upstream, world-facing:** `spec/claim-format.md` → `meta/conversion-protocol.md` — the file
lives downstream; the upstream spec references its dependent layer's process file, which is both
dangling and against the spirit of the no-references-to-dependents rule (the letter covers
`core/`). One sentence to scope ("the projection repository's conversion protocol") or drop.

**4d. Resolved during the pass (no action):** upstream CHANGELOG's `DDD-cost-04.yaml` — relocated
whole downstream under `DDD-dec-09`/`DDD-dec-10`, governed, the history is correct.
`meta/research-program.md` — `way-of-working` marks it "[to create]", a declared debt rather than
a dangling reference.

**4e. Housekeeping found at arrival:** `meta/sessions/README.md` lacks index rows for
`2026-08-31-ground-migration-exec` and `2026-09-01-primer`.

## 5. The known collisions, reported with costs, not repaired

- **`verdict`** (C10, ground-migration): `term:verdict` names the induced assignment (the function
  whose entropy is `D`); `term:act-individuation` and `term:outcome` use the per-act verdict (a
  value of that function) — a function against its value across three settled entries established
  by one document. `core/09`'s contract already disambiguates (`verdict|verdict function`) and the
  registry carries the alias; only the bare `term:` display field collides. Cost to repair: a
  settled registry entry's display field moves (the id `term:verdict` — the pin key — need not),
  with a supersession record; embeds unaffected (canonical_md untouched). Cost to carry: an
  outside reader meets one word naming two objects, with the disambiguation one contract away.
- **`projection`** (C10): `term:projection` (the compound's two axes) against "the engineering
  projection" / the projection layer — and the colliding sense appears **inside `term:verdict`'s
  settled canonical text**. The `denominations:` field repaired half at v5.12.0. Cost to repair
  the rest: prose-sense disambiguation in a settled canonical_md → canonical text moves → pin
  fires, embed re-projects. Cost to carry: same as above, and the collision sits inside a settled
  definition a paper quotes.
- **Publication test, honestly applied:** both are documented, disambiguated-by-contract, and
  quotable only as untidiness, not as error. They read as *untidy waits* unless Emil weighs the
  settled-text location of `projection`'s collision as quotable-against-us.

## 6. Also carried to the close

- `DDD-frame-08`'s `changed: v5.14` awaits the close's version proposal (flagged at GATE 1).
- The four `check-appendix` discrepancies at v5.13.0 stand recorded for the next manuscript
  session (GATE 3 ruling).
- The supplement's one failing quotation (the boundary rule, UNCITED, ref-independent) — the
  supplement quotes a session artefact, not canon; either the quotation declares its source or the
  checker's scope statement names the supplement out. One line either way; a ruling picks which.
- Out of scope, untouched, as chartered: W4's local items, Q40–Q46, the measure note's missing
  checkers, the delivery layer, the G-track, the licence split and `meta/lineage-and-limits.md`
  as public register (the transfer session's).

## 7. Proposed dispositions, for the ruling (the session proposes; Emil disposes)

**Files now (unfixable-or-expensive-once-public):**
1. `DDD-measure-11`/`-13` demote to `projected` (1a) — two claims move upstream, nothing fires.
2. The closure-bounds word on the upstream front page (§3) — one word, pending the direction
   ruling.
3. The sdlc front-page existence claim and the four dead links (4a) — the repair-to-match-tree
   variant; restoring v3 content is its own ruled session.
4. The downstream front page's five cross-repo links become upstream URLs (4b, first row).
5. The `spec/claim-format-2-addendum.md` reference gains its upstream location (4b) and the
   upstream spec's `conversion-protocol` sentence is scoped (4c).
6. The two index rows (4e).

**Carries to the transfer or later:** the collisions (§5); the full cross-repo reference rewrite
beyond the front pages; the v3 content restoration question; the validator's root-mode
inconsistency (§0) — an instrument fix with its own tests, wrong to rush inside a canon session;
the supplement-quotation scope line (§6).

**HOLD at GATE 4 — awaiting Emil's ruling on the dispositions.**
