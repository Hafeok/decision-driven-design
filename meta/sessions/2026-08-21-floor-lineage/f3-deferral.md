# F-3 — the competing novelty claims: deferral record

**Session** `2026-08-21-floor-lineage` · ruled **defer whole** by Emil at GATE 1, confirmed at GATE 2
· principal: Emil

**Locators below are as at this session's upstream head**, which includes F-1's restructure of
`core/03` and F-2's new `meta/lineage-and-limits.md` §1.16 — both shift line numbers in the files
this record cites.

This is F-3's deliverable. The item was booked as *report before repairing*, and the honest finding
was that reconciling the statements requires deciding what the framework's primary contribution is —
a design question. Emil ruled the deferral and adopted the session's reasoning as the ruling. Nothing
was repaired. This file exists so the tension is a repo object rather than a session residue, and so
the session that inherits it does not have to rediscover it.

---

## 1. What was found

The prompt booked **two** competing novelty claims. There are **three**.

### Statement one — the floor. `core/03-the-floor.md:18`

> **The framework's best original result.** It corrects an earlier, over-strong claim (a "zero-floor
> postulate" that survived external review only in narrowed form) and replaces it with something
> sharper and more useful: **the irreducible floor is a property of the acceptance predicate, not of
> the decision.**

Carried at three sites, consistently, all about the floor:

| Site | Text |
|---|---|
| `core/03-the-floor.md:18` | "**The framework's best original result.**" |
| `core/README.md:15` | "**03 — the floor** · the intrinsic floor lives in the *acceptance predicate* — the framework's best original result" |
| `meta/consolidated-state.md:78` | "**The framework's best original result.**" |

### Statement two — the register sentence. `meta/lineage-and-limits.md:403–409`

Corrected at **v5.4.0**, commit `06b0603`, *"Gate 4 sweep: extend the supersession to DDD-cost-05 and
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

### Statement three — the Escaped store. `meta/lineage-and-limits.md:572–574`

Found by this session's survey and not booked. §5, *"What survives, and is genuinely ours"*, item 2:

> 2. **The Escaped store.** Naming *"decided by nobody = latent defect exposure"* as a first-class
>    category is the framework's clearest original contribution. Tesler didn't have it; it makes
>    implicit risk nameable.

The same numbered list ranks the floor **third**:

> 3. **The floor-is-in-the-predicate sharpening** (§2.2). Locating the intrinsic floor in the
>    *decidability of the acceptance predicate* rather than in the decision is a genuine and useful
>    result, and it is *ours* even though it is built from Rice + Collins + degeneracy.

---

## 2. Which of them actually compete

**Two and three compete. One and two do not.**

**Statement two is scoped and does not compete.** Its paragraph opens *"`core/09` and `core/11` are
applied information theory"*, and its heading is *"The register sentence, for every future
write-up"*. It is a citation-register sentence for the measure layer, not a ranking of the
framework's contributions. Its "What this framework contributes" is additive-part language about
*that layer*.

**One qualification, and it cuts the other way.** `core/decisions/DDD-dec-15.yaml:81` names it
**"the framework's own novelty statement"** — definite article, unqualified — and rules its
correction in scope on the ground that:

> A false originality claim is the most expensive kind, which is why this one file outside core/ is
> in scope.

So a ratified decision treats the register sentence as *the* novelty statement while the sentence's
own paragraph scopes it to two documents. That inconsistency lives in a decision node, not in prose,
and it is part of what the inheriting session must settle.

**Statements one and three are genuinely in tension.** *"Best original result"* and *"clearest
original contribution"* are both superlatives over the same domain, awarded to different objects,
neither scoped, both ratified. §5's numbering makes the ranking explicit and opposite to `03`'s.

---

## 3. The minimal reconciliation, stated and not taken

It is available, and the session states it so the inheriting session does not have to re-derive it:
scope each superlative to what it ranks — *"best original result"* meaning the strongest **result**
(a claim carrying a falsifier), *"clearest original contribution"* meaning the most legible
**category** (a naming that makes risk visible). One clause each, at four sites.

**It was not taken, and the reason is the resistance.**

> Two ratified, unscoped superlatives over one domain cannot both stand, and which one yields is a
> ranking of the framework's contributions, not a prose repair.

Choosing which reading survives *is* deciding whether the framework's primary contribution is the
floor result or the Escaped store. §5's numbered list already contains a ranking, so any repair must
either ratify or overturn it. The prompt's own test applies exactly: *"If the honest finding is that
reconciling them requires deciding what the framework's primary contribution is, that is a design
question and defers whole."*

**The cost of deferring, stated as a cost.** The tension stays in canon. A reader meeting `core/03`
and `meta/lineage-and-limits.md` §5 in the same sitting meets two superlatives and no rule for
ranking them. That is a real defect and it is being carried deliberately, not overlooked.

---

## 4. Routing, per Emil's GATE 2 ruling

> Route it explicitly: to whichever session next states what the framework's primary contribution is
> — the Paper A revision or the method paper, since a paper cannot avoid the question a repo can
> defer.

**Inherited by:** the next session that states the framework's primary contribution. On current
plans that is **the Paper A revision** or **the method paper**, whichever comes first.

**Why a paper and not a canon session.** A repository can carry two superlatives indefinitely,
because nothing forces the two sentences into one paragraph. A paper cannot: its abstract, its
introduction and its conclusion each have to say what the contribution *is*, in one voice, and the
question resolves itself the moment that sentence is written. The right place to settle a ranking is
where the ranking is unavoidable.

**What the inheriting session receives, complete:** the three statements verbatim with locators; the
scoping analysis above; `DDD-dec-15`'s conflicting characterisation; the minimal reconciliation
already drafted; and the four sites a repair would touch — `core/03-the-floor.md:18`,
`core/README.md:15`, `meta/consolidated-state.md:78`, `meta/lineage-and-limits.md:573`.

**What it must not do:** treat this as a wording fix. The deferral is on record precisely because it
is not one.

---

## 5. What this session changed about F-3

**Nothing.** No superlative was edited, scoped, or moved, in either repository. `core/03:10` stands
verbatim, including through F-1's restructure, which moved the embed **above** that paragraph and
left the paragraph itself untouched.
