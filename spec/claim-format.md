# Claim format specification

**Format version: 1.** This file is the versioned schema artifact for claim nodes — shape and
validation rules only. It contains no process (see `meta/conversion-protocol.md`, versioned with
the way of working) and no content (see `core/claims/`, versioned per claim via `changed`). The
three change independently:

| Artifact | Changes when | Version field |
|---|---|---|
| **This spec** | The shape of a claim changes — a field added, a rule altered | Format version, top of this file |
| **Process** | How the work is done changes | Way-of-working revision |
| **Content** | A claim's status or statement changes | `changed` on the claim; the spec is untouched |

**Versioning rules.** A format change bumps the format version and ships a migration note in this
file stating how existing claims move (or that they are valid unchanged). Claims declare the format
they conform to; validation is always against the declared version, so old claims never break when
the spec advances — they migrate deliberately or stay valid under their version. A content change
never requires touching this file; if it seems to, the change was a format change in disguise.

Storage: one YAML file per claim under `core/claims/`; Turtle export handled by the tool when it
exists. Until then these files are the graph and grep is the query engine.

---

## 1. Schema

```yaml
format: 1                    # spec version this claim conforms to; mandatory
id: DDD-<area>-<n>          # stable, never reused; retired claims keep theirs
kind: formal | empirical | conceptual | normative
statement: >                 # one proposition; one idea; if "and" joins two testable
                             # assertions, split the claim
status: projected | reported | established | retired
region: >                    # where the claim holds; "closing predicates only" is a
                             # region, and boundedness is stated here, never implied
evidence:                    # empty list is legal for projected, mandatory content for
  - kind: asset | derivation | computation | paper | observation
    ref: core/assets/measure-toy.py        # repo path, citation, or DOI
    note: reproduces §4 values exactly     # reported and above
falsifier: >                 # what observation fires it, in one sentence
breaks: >                    # what else falls if it fires ("nothing in core/" is legal)
test: >                      # for conceptual/normative kinds: the appropriate test
                             # (counterexamples, coding reliability, explanatory utility)
credits: >                   # borrowed theorems named here — "the theorem is Shannon's"
                             # lives in the claim, not just the paper
owner: paper-1 | paper-2 | ... | none      # which projection pays this claim's debt
changed: v4.5                # canon version of last status change
supersedes: DDD-...-n        # optional; corrections reference what they replaced
notes: >                     # anything else, including flagged unconfirmed reasoning
```

## 2. Rules

1. **One proposition per claim.** Compound statements split. The unit of status change must be the
   unit of statement.
2. **Statuses have entry conditions.** *Reported* requires at least one evidence entry whose asset
   reproduces. *Established* requires a derivation or theorem, with `credits` filled if borrowed.
   *Projected* requires `falsifier` (or `test` for conceptual/normative kinds). *Retired* requires
   `supersedes` on the correcting claim or a `notes` entry naming what killed it.
3. **Retired claims stay in the tree.** They are evidence the loop works; `DDD-measure-08` is the
   exemplar.
4. **The arithmetic/model split is enforced in `kind`.** An identity that holds is `formal` and can
   be established; the identification that gives it meaning is a separate claim, `empirical` or
   `conceptual`, and starts projected. Never fuse them in one file.
5. **Region is mandatory.** "Everywhere" must be written to be claimed.
6. **`changed` pins staleness.** Any projection manifest listing this claim with an older
   `source_version` is stale by definition.

## 3. Areas

`measure`, `frame` (actor-indexed determination), `floor`, `tool`, `org`. New areas are cheap;
renumbering is forbidden.

## 4. Validation

A claim file is valid iff: it declares `format`; validation runs against the declared version's
rules (§2 for format 1); mandatory fields for its `status` and `kind` are present. Everything else
— how claims are authored, converted, or reviewed — is process and lives outside this spec.

`scripts/validate-claims.py` reports at two classes, and the difference is a ruling rather than a
taste:

| Class | Meaning | Exit |
|---|---|---|
| **error** | The claim is invalid. | 1 |
| **warning** | A rule with a known backlog, or a heuristic that locates candidates for a human rather than deciding. | 0 |

**A check becomes error class only when its hit list against the existing corpus is empty or already
migrated.** A check that fires on ratified claims needs a migration plan, not a merge — so the hit
list is produced before the class is chosen, never after. The checker's `CHECK_CLASS` table is the
whole of that policy, one line per check, so promoting a check is a one-word reviewable change.

**Rule 1 is not mechanically decidable and is never error class.** "One proposition" is a semantic
property; what a checker can count is clause-joining punctuation. The best available proxy fires on
sound claims — including `DDD-measure-16`, the claim built to cure `DDD-measure-06`'s compoundness —
so it ships as a drafting prompt that flags candidates for adjudication. **A rule that is stated but
not checked prevents nothing; a rule checked by a proxy that overreaches prevents the wrong things.**
Rule 1's real enforcement is an adjudication with rulings.

Rules added since format 1 — the falsifier condition at every live status, and `retired_from` on
retired claims — are stated in `spec/claim-format-2-addendum.md` with their migration notes. Both
are enforced now and both have empty hit lists.
