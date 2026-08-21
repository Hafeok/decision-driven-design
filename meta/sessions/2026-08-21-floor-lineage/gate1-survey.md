# GATE 1 survey — the floor: definition placement and lineage

**Session** `2026-08-21-floor-lineage` · **draft-pending-ruling** · principal: Emil

Fetch, inaugurate, survey, per the prompt's step 1. Four dispositions are put to Emil below. Nothing
in `core/` has been touched; this file and the arrival record are the session's only commits.

---

## 0. Fetch and baseline

**`actor-indexed-determination`.** Head `33b6d28`. `v5.8.0` verified as the newest tag — annotated,
2026-08-18, message *"v5.8.0 — Track 1: the two deferred mints, discharged on use"*, pointing at
commit `9e92099`.

**Head is three commits ahead of the tag**, and this matters at GATE 4. `c13b29b`, `5c9c8ca`
(`core/assets/measure-aggregate-discharge.py`) and `33b6d28` (the PR #16 measure-discharge merge)
carry canon changes that **no release descriptor covers** — `releases/` holds `v5.5.0` … `v5.8.0`
and nothing later. This session's version proposal must say whether it is bumping over its own
change alone or over that delta too.

**`decision-driven-design`.** Head `40d277f`, the Paper A merge (PR #26). Its
`graph/upstream.yaml` pins `ref: v5.8.0`.

**Baseline gates, all green at head, before any edit:**

| Gate | Result |
|---|---|
| `python3 validate-core-order.py core/` | exit 0 — 15 documents, 70 terms, 70 graph objects, 62 embedded, **0 errors**, 66 warnings, **0 W4** |
| `python3 scripts/validate-claims.py core/claims/` | valid: 60 claims |
| `python3 scripts/validate-claims.py core/decisions/ --decisions` | valid: 8 decisions |
| `python3 scripts/validate-releases.py releases/` | valid: 4 descriptors |

---

## F-1 — the registry answer

### The answer, with node IDs

**`term:floor` exists.** `core/graph/terms.yaml:216`:

```yaml
  - id: term:floor
    term: floor
    aliases: [intrinsic floor]
    established_by: 03-the-floor.md
    status: settled
    canonical_md: |
      > **The intrinsic floor is a property of the acceptance predicate, not of the decision.**
```

`established_by: 03-the-floor.md`. This is the prompt's **first case** — exists, established by `03`
— and **minting does not arise.** The session mints nothing and proposes nothing minted.

`03` already embeds it, at `core/03-the-floor.md:19–21`, inside the claim block. The embed is
byte-exact: `validate-core-order.py` reports `core: OK — edges point backward, embeds match the
graph`, so E6 is clean today.

The doc's three sibling terms are all likewise `established_by: 03-the-floor.md` and all likewise
embedded in it: `term:acceptance-predicate` (`terms.yaml:198`, embedded at `03:50–54`),
`term:closure` (`terms.yaml:207`, embedded at `03:37–41`), `term:path-degeneracy`
(`terms.yaml:223`, embedded at `03:90–94`).

### The anomaly the answer exposes

The registry question resolves cleanly, and in resolving it exposes something the prompt's three
cases did not anticipate.

**`term:floor`'s canonical text is not a definition of the floor. It is the claim about the floor.**
"The intrinsic floor is a property of the acceptance predicate, not of the decision" says what the
floor is a property *of*; it never says what a floor *is*.

The definition — the thing F-1 wants moved — is **unregistered prose**, at `03:30–32`:

> The "floor" is the portion of a determination's demand that **cannot be moved off the in-the-moment
> actor** — the residue that no amount of encoding or checking can amortise, that must be paid, per
> run, in judgment.

So `03` embeds, for the term "floor", a sentence that presupposes the reader already knows what a
floor is; and the sentence that tells them lives outside the graph, ungoverned, three lines below
the claim that uses it. That is F-1's defect stated exactly: **the definition arrives after its own
use because the definition was never the canonical text in the first place.**

The two adjacent terms establish the contrasting pattern. `term:acceptance-predicate` opens *"The
**acceptance predicate** is the criterion that settles whether…"*; `term:closure` opens *"A predicate
is **closed for an arrangement** when…"*. Both define. `term:floor` alone asserts.

### Three repairs, with their costs

**Option A — prose-only.** Move `03:30–32` above the claim block. The registry is untouched;
`term:floor`'s embed stays byte-exact inside the claim block; the definition remains ungoverned
prose, but now precedes its use.

- *Cost:* none downstream. Suggests a **patch** bump.
- *What it does not fix:* the registry still has no definition of "floor", and any downstream doc
  embedding `term:floor` still gets the claim without the definition.

**Option B — the definition replaces the claim as `canonical_md`.** `term:floor` comes to say what a
floor is; the relocation claim stays in `03` as unembedded claim prose.

- *Cost:* loses the embed on the framework's most-quoted sentence. **Not recommended.**

**Option C — `canonical_md` carries both, definition first.** One embed block, at the document's
opening move: the definition, then the relocation claim. The registry entry for "floor" comes to
define the floor and then state the result about it.

- *Cost, verified, not estimated:*
  - upstream: a change to ratified canonical text — a supersession, and a **minor** bump;
  - downstream `graph/upstream.yaml:81` pins `term:floor` at
    `content_hash: sha256:daf43e07…`. That digest is **live-verified against `v5.8.0` and currently
    matches exactly.** Changing `canonical_md` fires **W6 "pinned content moved"**, and
    `graph/upstream.yaml`'s own header states the rule: *"Advancing a pin is a decision … record the
    advance as a decision under `core/decisions/` before bumping."* So Option C costs a downstream
    **decision node**, not a mechanical bump;
  - `papers/paper-a/paper-a.md:1387` reproduces `term:floor`'s canonical text verbatim in Appendix A,
    which is generated from the graph and never hand-edited — it would need regeneration;
  - `papers/paper-a/paper-a.md:742` quotes it in §6.1, and `papers/paper-a/reviewer-brief.md:57`
    quotes it again;
  - five `ddd:ref` sites (`apparatus/encode-verify.md:13`, `apparatus/tool-surfaces.md:17`,
    `apparatus/the-skill-floor.md:11`, `applications/sdlc/README.md:17`,
    `applications/sdlc/production-as-ground.md:19`) reference but do not embed, so they are unaffected.

### What the session proposes, and holds for

**Recommended: Option A**, and the anomaly filed rather than repaired.

The reasoning: F-1 was booked as a placement defect, and Option A closes it at booked size. Option C
is the better *canon*, and this is the session's honest view — a registry entry for "floor" that
never says what a floor is will keep generating this defect downstream — but it is a supersession of
ratified canonical text plus a downstream decision node, which is a filing, and the session does not
take filings on its own motion. Option C at booked size would be growing a design session inside
this one, which is exactly the failure the prompt's freight precedent names.

**Placement, under Option A.** The prompt says *"as the document's opening move"*, which the session
reads literally: the definition becomes the first prose after the `ddd:contract`, ahead of the
novelty framing at `03:10–13`. Reading order becomes *what a floor is* → *why this document matters*
→ *the claim*. The alternative placement — immediately under the `## The claim` heading, before the
claim block — is available if Emil prefers the novelty framing to keep the opening.

**Note the F-3 coupling:** the novelty framing paragraph at `03:10–13` is exactly F-3's contested
sentence. If F-3 defers, that paragraph stands unchanged and Option A's placement is unaffected
either way.

> **DISPOSITION F-1, for ruling.** (a) Option A, definition moved as the document's opening move,
> registry untouched, anomaly filed for a later session. (b) Option A with the alternative placement
> under `## The claim`. (c) Option C, accepting the supersession, the minor bump, and the downstream
> pin-advance decision.

---

## F-2 — the ancestry gap

### The gap, verified

`03` attributes its limits and its mechanism carefully, and names **no ancestor for the floor
itself**:

- Rice's theorem — `03:111–113`
- inevitable model error — Xu, Jain & Kankanhalli 2024; Kalai & Vempala; Suzuki et al. 2025 as the
  rebuttal — `03:115–118`
- collective tacit knowledge — Collins — `03:120–122`
- degeneracy — Edelman & Gally, *PNAS* 2001 — `03:83–84`

**`03` also carries no pointer to `meta/lineage-and-limits.md` at all.** `01`, `02`, `08` and `09`
each point at the register; `03` does not. Verified by grep across `core/`. So the convention the
prompt names — lineage lives in the register, core documents point at it — is not merely thin at
`03`; it is absent.

### One candidate needs correcting before the plan

**Polanyi is already in the register.** `meta/lineage-and-limits.md:105`, §1.7 *"Polanyi (1966) and
Collins (2010) — tacit knowledge"*, opens *"Polanyi gave us 'we know more than we can tell' — the
floor."* And §6's required-citations table (`:461`) carries the row **"The floor | Polanyi; Collins
(relational/somatic/collective TK) | we must respect collective TK"**.

So the dangling lineage the prompt predicts is **real but one level down from where it was
predicted**: the register has Polanyi; **`core/03` cites Collins without him.** That reframes F-2's
register work — it is an extension of §1.7's neighbourhood, not a fresh Polanyi entry — and it makes
`03`'s contrast paragraph the load-bearing half of the repair.

**§6's table is stronger than a convention.** Its heading reads *"Required citations (**add to every
artifact that uses the corresponding claim**)"*. That is a standing duty, and it governs F-4 below.

### Candidate status, verified against the repository

| Candidate | In the repo? | Where |
|---|---|---|
| Polanyi (1966) | **yes** | `lineage:105` §1.7; `lineage:461` §6 table row "The floor" |
| Collins (2010) | **yes** | `lineage:105` §1.7; `03:120–122` |
| Brooks | **yes** | `lineage:59` §1.3; §6 table; Paper A bibliography |
| Wittgenstein, *PI* §201 | **no** | absent from `core/` and `meta/` entirely |
| Hayek (1945) | **no** | absent |
| Bainbridge (1983) | **no** | absent |
| Dreyfus | **no** | absent |
| Suchman (1987) | **no** | absent |

**An adjacent discrepancy, reported not repaired.** `lineage:59` dates Brooks **1986**; Paper A's
bibliography dates the same work **1987** (*IEEE Computer* 20(4):10–19). Both are defensible — the
IFIP Congress paper is 1986, the *IEEE Computer* version 1987 — but the repository states two dates
for one source. Out of F-2's booking; flagged here so it is not lost.

### Verification plan

Every locator is verified or flagged **in its own entry**, per the prompt, with the Paper A Tesler
entry as the pattern for a source with no primary publication. No locator is asserted from memory.

For each candidate carried forward:

1. **Establish the primary publication** — title, year, publisher or journal, and the internal
   locator (section, chapter, or aphorism number) that carries the claim the entry attributes.
2. **Check the locator directly** against the source text where reachable, not against a secondary
   description of it. An entry marked *(verified)* means the cited passage was read at the cited
   locator.
3. **Where it cannot be checked, the entry says so in its own body**, with the reason and with what
   the entry does and does not take from the source — the Tesler pattern verbatim:
   *"**(unverified — no primary publication.)** … This paper cites X for Y only, and takes no result
   from him."*
4. **Two locators need care and are called out now.** Wittgenstein *PI* §201 is a remark number,
   stable across editions but with a translation question (Anscombe vs Hacker–Schulte) that the entry
   must name. Bainbridge's *Ironies of Automation* has two locators in circulation — the 1982 IFAC
   Analysis, Design and Evaluation of Man–Machine Systems proceedings and the 1983 *Automatica*
   19(6):775–779 version; the entry states which it cites.
5. **A candidate that cannot be verified and cannot be honestly flagged is dropped**, with the drop
   recorded at GATE 2 rather than left silent.

Each surviving entry states, per the register's own §1 form: what it established, and what — if
anything — the framework adds or where it differs.

### The contrast paragraph

Drafted at GATE 2 to strengthen, not to apologise. Its load-bearing sentence is the difference, and
the session will draft it around: *the ancestors located irreducibility in the knower (Polanyi), in
the society (Collins), in the rule's application (Wittgenstein), in the dispersion of knowledge
(Hayek), in the problem (Brooks), and in what automation leaves behind (Bainbridge) — none of them
locates it in the checkability of the acceptance predicate, arrangement-indexed.* Three or four
sentences, naming the tradition, pointing at `meta/lineage-and-limits.md`, ending on the contrast.

> **DISPOSITION F-2, for ruling.** Proceed as booked: register entries at GATE 2 with the
> verification discipline above, plus `03`'s contrast paragraph and its first pointer at the
> register. Confirm the candidate set — the session proposes carrying **Wittgenstein, Hayek,
> Bainbridge, Dreyfus and Suchman** as new entries, and **extending §1.7** rather than duplicating
> Polanyi and Collins.

---

## F-3 — the two novelty claims, verbatim

### Statement one — `core/03-the-floor.md:10`

> **The framework's best original result.** It corrects an earlier, over-strong claim (a "zero-floor
> postulate" that survived external review only in narrowed form) and replaces it with something
> sharper and more useful: **the irreducible floor is a property of the acceptance predicate, not of
> the decision.**

It is **not confined to `03`.** The same words appear at `core/README.md:15` — *"**03 — the floor** ·
the intrinsic floor lives in the *acceptance predicate* — the framework's best original result"* —
and at `meta/consolidated-state.md:78`, *"**The framework's best original result.**"* Three sites,
one claim, consistently about the floor.

### Statement two — `meta/lineage-and-limits.md:275–281`, the register sentence

Corrected at v5.4.0, in commit `06b0603` *"Gate 4 sweep: extend the supersession to DDD-cost-05 and
the novelty statement"* (2026-08-13). Verbatim at head:

> **`core/09` and `core/11` are applied information theory. Shannon supplied the entropy, the chain
> rule, and the rate-distortion bound; Sims supplied the channel model of a capacity-limited
> decision-maker. What this framework contributes is the identification of specification demand with
> verdict entropy, of seam demand with mutual information, and of **capacity-generated** escape with
> the intersection of rate-distortion-forced error and absent verification — together with the demonstration that those
> identifications hold without leftover on worked examples. The mathematics is not ours. The mapping
> is, and the mapping is what is falsifiable.**

The v5.4.0 diff, verified: `of escape with the intersection` → `of **capacity-generated** escape with
the intersection`.

### A third the survey found, and the session must report

The prompt books F-3 as two claims. There are **three**. `meta/lineage-and-limits.md:444–446`, §5
*"What survives, and is genuinely ours"*, item 2:

> 2. **The Escaped store.** Naming *"decided by nobody = latent defect exposure"* as a first-class
>    category is the framework's clearest original contribution. Tesler didn't have it; it makes
>    implicit risk nameable.

And in the same list, item 3 ranks the floor **below** it:

> 3. **The floor-is-in-the-predicate sharpening** (§2.2). Locating the intrinsic floor in the
>    *decidability of the acceptance predicate* rather than in the decision is a genuine and useful
>    result, and it is *ours* even though it is built from Rice + Collins + degeneracy.

So the repository carries two competing superlatives — the floor is *"the framework's best original
result"*, the Escaped store *"the framework's clearest original contribution"* — in a numbered list
that places the floor third and the Escaped store second.

### Genuinely in tension, or scoped differently?

**Statement two is scoped and does not compete.** Its own paragraph opens *"`core/09` and `core/11`
are applied information theory"*, and its heading is *"The register sentence, for every future
write-up"* — a citation-register sentence for the measure layer, not a ranking of the framework's
contributions. Its "What this framework contributes" is a locution about *that* layer's additive
part. Read in place, it is **scoped differently**, not in tension.

One qualification, and it cuts the other way. `core/decisions/DDD-dec-15.yaml:81` names it
**"the framework's own novelty statement"** — definite article, unqualified — and rules its
correction in scope on the ground that *"A false originality claim is the most expensive kind, which
is why this one file outside `core/` is in scope."* So a ratified decision treats the register
sentence as *the* novelty statement while its own paragraph scopes it to two documents. That is a
real inconsistency, and it is in a decision node, not in prose.

**Statements one and three are genuinely in tension.** *"Best original result"* and *"clearest
original contribution"* are both superlatives over the same domain, awarded to different objects, in
one repository, both ratified. Neither is scoped. §5's own numbering makes the ranking explicit and
opposite to `03`'s.

### What the session finds, and why it recommends deferring

The minimal reconciliation is available and the session can state it: scope each superlative to what
it ranks — *"best original result"* meaning the strongest **result** (a claim with a falsifier), and
*"clearest original contribution"* meaning the most legible **category** (a naming that makes risk
visible) — which is close to what the two sentences already mean, and would need one clause each.

**But the session does not think that is honest.** Choosing which reading survives *is* deciding
whether the framework's primary contribution is the floor result or the Escaped store, and §5's
numbered list already contains a ranking that a reconciliation would have to either ratify or
overturn. That is a design question about what the framework is for. The prompt's own test is exact:
*"If the honest finding is that reconciling them requires deciding what the framework's primary
contribution is, that is a design question and defers whole."*

**The resistance, named:** two ratified, unscoped superlatives over one domain cannot both stand, and
which one yields is a ranking of the framework's contributions, not a prose repair. Deferring leaves
the tension in canon, which is a real cost and is stated as one.

> **DISPOSITION F-3, for ruling.** The session recommends **defer whole**, with the resistance named
> above and the third statement recorded — the finding is that there are three novelty statements,
> not two, and that a decision node calls one of them *the* novelty statement while its own paragraph
> scopes it to `core/09` and `core/11`. If Emil rules the minimal reconciliation instead, the session
> will draft it at GATE 3 as one clause each at `03:10`, `core/README.md:15`,
> `meta/consolidated-state.md:78` and `lineage:445`.

---

## F-4 — the Paper A bibliography gap, stated exactly

### The bibliography, as it stands

`papers/paper-a/paper-a.md:1256`, §References. **Ten entries**, exactly as the prompt anticipated:
Ashby (1956), Brooks (1987), Funkhouser (2014), Goodhart (1975), Johnson (1921), Meyer (1992), Prior
(1949), Shannon (1948), Tesler (ca. 1984, **unverified — no primary publication**), Wilson (2023).

### The gap

**Total.** A grep across the whole 1,413-line manuscript for `rice`, `undecidab`, `halting`,
`collins`, `tacit`, `degenerac`, `edelman`, `kalai`, `vempala`, `suzuki`, `polanyi`, `xu et al`,
`kankanhalli` returns, from the paper's own prose, **nothing**.

- **No Rice, and no undecidability anywhere** — zero hits on `undecidab` and `halting` in the file.
- **No Collins, no Polanyi.**
- **No Edelman & Gally, and no degeneracy** — the word does not occur.
- **No Xu, Jain & Kankanhalli; no Kalai & Vempala; no Suzuki et al.**

The only occurrences of `tacit` in the file are inside `DDD-hyp-02`'s **own statement**, reproduced
from the graph at `:962` and `:1347` — *"…tacit or socially distributed knowledge is required…"* —
which is canon's text carried verbatim, not the paper's argument.

### What the paper does project from `03`

`§6.1` (`:739`) quotes `term:floor` — *"The intrinsic floor is a property of the acceptance predicate,
not of the decision." [term:floor, settled]* — and glosses it: *"Where the predicate does not close,
verification is structurally unavailable, and the demand falls to whoever is present."* `§6` opens on
`DDD-floor-02`; `§6.2` carries `DDD-floor-01`.

### The finding, stated precisely

**The paper projects `03`'s positive result and does not state `03`'s limits at all.** It never claims
that closure is undecidable, never claims a non-zero lower bound on model error, never claims
collective tacit knowledge exists, and never invokes degeneracy for the robustly-zero half. The
prompt's framing — *"projects the floor result"* without its warrant — is confirmed for the result;
the limits are not projected-without-warrant, they are **absent**.

That distinction decides F-4's disposition, and it cuts both ways:

**Reading one — nothing to cite; defers.** A citation attaches to a claim. Since the paper states none
of the limits, adding Rice or Edelman & Gally to the bibliography would produce entries cited
nowhere, which is worse than absence. Giving them a citation point means **writing the limits into the
manuscript** — new argumentative prose, and §11's neighbourhood entries are argument, each stating
what the paper takes and what it does not. That is a Paper A revision, and it defers.

**Reading two — a standing duty is unmet; a citation-only fix exists.** `meta/lineage-and-limits.md`
§6 is headed *"Required citations (**add to every artifact that uses the corresponding claim**)"* and
carries the row **"The floor | Polanyi; Collins"**. Paper A **uses** that claim — it quotes
`term:floor` at §6.1. By canon's own standing rule the paper already owes Polanyi and Collins, and
discharging that debt is a bibliography entry plus an attribution at §6.1 — no limit is asserted, no
argument is added. The `Zero-floor limits` row (*Rice; Xu et al.; Kalai & Vempala*) is **not**
triggered, because the paper does not use that claim.

The session's reading is that **reading two is correct and strictly narrower**: two entries, one
attribution point, no argument. Rice, Edelman & Gally, Xu et al., Kalai & Vempala and Suzuki et al.
are **not** repaired here under either reading — they defer with the finding recorded.

One thing the session will not do without a ruling: §5.6 (`:710`) is authored analysis whose residual
*"may depend on situated judgment, social convention, institutional authority…"* is Collins's
territory, and it is the natural second attribution point. Attaching a citation there is closer to
argument than §6.1's is, and the session proposes §6.1 alone.

> **DISPOSITION F-4, for ruling.** (a) Citation-only repair, downstream PR: **Polanyi and Collins**
> added to §References with locators verified per F-2's plan, and one attribution at §6.1 discharging
> `lineage` §6's standing row; the remaining five sources recorded as a finding and deferred to a
> Paper A revision session. (b) Defer F-4 whole, recording the gap. (c) (a) plus the §5.6 attribution.

---

## The four dispositions, together

| | Item | Session recommends |
|---|---|---|
| **F-1** | definition placement; `term:floor` registry | **Option A** — prose-only move as the document's opening move; `term:floor` exists (`terms.yaml:216`, `established_by: 03-the-floor.md`), so **no mint arises**; the canonical-text anomaly filed, not repaired |
| **F-2** | the floor's ancestry | **proceed as booked** — extend §1.7 rather than duplicate Polanyi/Collins; new entries for Wittgenstein, Hayek, Bainbridge, Dreyfus, Suchman, each verified or flagged in its own body; `03` gains the contrast paragraph and its first pointer at the register |
| **F-3** | two — in fact **three** — novelty claims | **defer whole**, resistance named |
| **F-4** | Paper A's bibliography | **(a) citation-only** — Polanyi and Collins only, discharging `lineage` §6's standing row at §6.1; five sources deferred with the finding recorded |

**Version bump, provisionally.** Under the recommended set the upstream change is prose-only —
`core/03` and `meta/lineage-and-limits.md`, no registry edit, no claim statement moved — which
suggests a **patch**. That proposal is provisional and is made properly at GATE 4, where the
unreleased three-commit delta above head's last descriptor must also be settled.

**Nothing is merged. Nothing in `core/` is edited. Held for Emil's ruling on all four.**
