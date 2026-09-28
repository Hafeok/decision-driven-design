# GATE 1 — survey (act address landing)

**Status.** Report only. Nothing is filed. Every recommendation is `[PROPOSED]` until Emil rules.
Surveyed 2026-09-28 against upstream `361e88f` (v5.14.1) and downstream `1c81da0` (`cba63ef` plus
the arrival commit).

## Weakest point, named first

**`DDD-ground-06` may be narrower than the predicates it anchors.** The draft says decisions are
anchored to acts by `DDD-ground-01`'s applicability predicates evaluated over the address. But
`DDD-ground-01`'s region refuses to make axes the ontology: "the predicate abstraction is wider
than coordinate geometry: categorical or interval constraints, graph queries, temporal
conditions, and compositions all serve; factored axes are one implementation … not the ontology
of every region." Its corpus evidence puts the beyond-region cases at about 27–36% of rows.

The address is a position on declared axes plus a layer path. The layer path can plausibly
carry graph predicates. Temporal predicates are a different matter. The time index is kept out of
the address (`DDD-address-01`, criterion K5) and files downstream. So a decision with a temporal
applicability condition seems to need more than "its address and the decisions' applicability
predicates" to compute its governing set. That is `DDD-ground-06`'s own first falsifier limb.

This does not show the claim is wrong. It may mean the falsifier limb needs "address and time
index", or that the region needs to exclude temporal predicates explicitly. Either repair touches
the synchronic/diachronic split that places the claim upstream. `UNVERIFIED — Emil review.`

## 1. Drift since the drafts were written

| Object | Change since `361e88f` / `cba63ef` |
|---|---|
| Both `main` branches | None. The drafts' bases are the current heads. |
| `DDD-ground-01`, `DDD-frame-01`, `DDD-floor-02`, `term:act`, `core/04` | None on `main`. The last change to any of them predates v5.14.0. |
| Unmerged branches (all `origin/*`, both repositories) | No branch carries a commit beyond `main` that touches the basis. `claude/act-primitive-lm1s03` is fully merged. |
| Open PRs | Upstream #3 (`claude/primitives-reader-clean`, last updated 2026-08-06) rewrites `core/00` prose about "the act". It does not touch the `term:act` embed. It is stale against the split and changes nothing now, but if it merged later it would reword the doc that establishes `term:act`. |
| Ground-axes holding note rev 18 | Not in either repository (held by Emil; cited as unratified in `DDD-frame-17` and the ground claims). No drift can be checked. |

Two findings came out of checking the basis rather than from drift.

- **Citation precision.** `DDD-ground-06`'s region and finding F-2 cite "`DDD-ground-01`'s
  declared-space limit". `DDD-ground-01` states axis marking over declared axes. It does not state
  a limit on undeclared space. The limit as stated lives in `DDD-ground-05` (the determinable space
  is prior) and `DDD-ground-02` (`undeclared` as a source-coverage value). `[PROPOSED]` cite
  `DDD-ground-05` (with `DDD-ground-02`) at filing.
- **`term:act` and `core/09` (the draft's flagged relation).** `core/09` §1 already says "acts
  nest as actors nest": an inner check with its own verdict individuates an inner act, and the
  outer boundary's verdict individuates the outer act. That supports the layer path, and it
  supports reading individuation and address as orthogonal. `core/09` also says retry economics
  "stays synchronic as an expectation over the outer act". T2a's attempts a3.1–a3.3 are separate
  occurrences only if each attempt carries its own verdict. `[PROPOSED]` narrow the
  `UNVERIFIED` flag to the retry case; the layer relation itself is consistent with canon.

The **pin advance spans three releases**, not one. Downstream pins `v5.13.0`, so the advance
crosses v5.14.0 and v5.14.1 as well as the release that carries this landing. `DDD-frame-08` is
pinned and its statement moved at v5.14.0. That is at least one predicted W6 before this session's
own content. The full prediction belongs to GATE 3.

## 2. ID collisions

| ID | Free? | Checked |
|---|---|---|
| `DDD-ground-06` | Yes | Upstream holds `DDD-ground-01…05`. No ref on any branch of either repository names `-06`. |
| `DDD-dec-37`, `DDD-dec-38` | Yes | Decision numbers are shared across the two repositories; `01…36` are all in use, and `37`/`38` appear on no branch. |
| `term:act-address` | Yes | Not in the registry and on no branch. `term:act` and `term:act-individuation` exist and are distinct. |
| `DDD-address` area | Yes | No `DDD-address-*` file on any branch. New areas are cheap (`spec/claim-format.md` §3). |

No replacements are needed, so no cross-references are rewritten.

**A related scope finding.** Upstream `CLAUDE.md` says this repository carries no reference to its
dependents, "the software projection, its apparatus, or its applications", anywhere under
`core/`. The upstream drafts reference the dependent in two ways:

| Reference | In | Precedent |
|---|---|---|
| Evidence `ref` to "decision-driven-design meta/sessions/2026-09-27-act-address/…" | `DDD-ground-06` | Precedented: `DDD-frame-02`, `DDD-frame-15`, `DDD-dec-30`, `DDD-dec-33` and `DDD-dec-36` cite session records "in the projection repository". |
| "the Phoenix engagement", "the first Phoenix slice" | `DDD-ground-06` `test`; `DDD-dec-37` statement and resolution | No precedent. Phoenix is an application of the software projection. |

`[PROPOSED]` upstream wording: "the pre-registered independent case (T2b), fixed before the case
exists; its identity and predictions are held in the projection repository's session record".
Phoenix is then named only downstream. Emil to rule.

## 3. Validation

The drafts were copied into scratch trees of each repository and run.

| Validator | Errors | Warnings |
|---|---|---|
| Upstream `validate-claims.py core/claims/` | 0 | 32; baseline 32, none on `DDD-ground-06` |
| Upstream `validate-claims.py core/decisions/ --decisions` | 0 | 0 |
| Downstream `validate-claims.py core/claims/` | 0 | 6; baseline 6, none on `DDD-address-01…05` |
| Downstream `validate-claims.py core/decisions/ --decisions` | 0 | 0 |
| Upstream `validate-core-order.py core/`, term as drafted | **1: E10** "term:act-address has no establishing doc contract" | 67 (+1: W3, `canonical_md` embedded nowhere) |
| Same, with the term established by `core/14` and the bare `address` alias dropped | 0 | 66; baseline 66, and W4 = 0 |

The validators do not check the `changed: SESSION-SETS-AT-…` placeholders. They are set at
GATE 2 and GATE 3.

## 4. Rule 1 candidates

The mechanical proxy flags none of the six drafts. These are semantic candidates for
adjudication.

| Claim | Joined limbs | `[PROPOSED]` |
|---|---|---|
| `DDD-ground-06` (pre-flagged) | (a) the address is position plus layer path, read at the act-site; (b) the occupant is not a component. The two falsifier limbs map one-to-one onto (a) and (b). | **Keep joined.** Without (b), (a) does not define an address, as the draft's notes argue. Alternative: split (b) as `DDD-ground-07`. |
| `DDD-address-01` (pre-flagged) | (a) a time index sits beside the address; (b) it is causal order, not wall-clock; (c) the "so that" consequence. | **Keep joined.** (c) is a consequence clause, and (a)+(b) define one object. Alternative: split (b) as `DDD-address-06`. |
| `DDD-address-02` | (a) every occurrence is its own act; (b) reuse is a derivation relation, never act identity. | Keep joined: (b) is what (a) excludes. |
| `DDD-address-05` | Two grains | Keep: one proposition about the reading grain. |
| `DDD-address-03`, `-04` | — | No candidate. |

## 5. The Gate 0 behaviour bundle

**It has not been filed anywhere.** There is no `term:behaviour`/`behavior` in the registry, and
nothing on any branch of either repository or in any open PR. `DDD-address-05`'s central noun has
no registered definition. Its region carries a working definition, "recurring acts at one address
under the same relative ground", and "relative ground" is also unregistered.

| Option | Cost |
|---|---|
| **File with the dependency named** `[PROPOSED]` | The claim stands on a working definition. The later behaviour term must be checked against it, which is a successor item. `DDD-address-04`'s `breaks` stays resolvable. |
| Hold | `DDD-address-04`'s `breaks` and `DDD-dec-38`'s statement ("the two behaviour grains … 01 to 05") must be rewritten to 01–04. The claim waits for a bundle with no date. |

The recommendation is to file with the dependency named. The falsifier ("a grain that adds no
detection over the other") can be evaluated under the working definition.

## 6. Seam-decay result

**No canonical home exists.** No claim, term, core document or meta note in either repository
states that a seam spanning k occurrences decays at the conjunction of k persistence
probabilities. The nearest canon is not it:

| Nearest | What it says |
|---|---|
| `DDD-cost-27` (downstream, projected) | Mechanical assurance decays at the drift rate of the ground it read |
| `DDD-measure-03`, `DDD-measure-14` (upstream, reported) | Seam arithmetic, with no persistence or decay |

`DDD-address-03`'s statement does not depend on the result; its notes and one limb of its
`breaks` ("the pricing of reuse as seam risk") do. `[PROPOSED]` file `DDD-address-03` with its
note restated ("no canonical home at v5.14.1; nearest `DDD-cost-27`"), keep the `UNVERIFIED`
flag, and carry the seam-decay result as a successor item.

## 7. Unruled items, presented for ruling and not filed

| Item | What it says | Observation from this survey | `[PROPOSED]` |
|---|---|---|---|
| **E-1** | The pre-registration mis-stated plain D's failure. Without the layer, the seam decision is ambiguously anchored (it matches parent and children), not unanchored. | Consistent with `core/09` §1: parent and child acts nest, so overlapping positions are expected. The pre-registration stays unedited. | Accept as a correction record. |
| **F-1** | One decision (retry count), three addresses: scaffold, incident, runtime. C would have merged them. | a3 differs from a1/a2 on act-kind alone. a1 and a2 differ only on gateway state, and a1's value is "not read". Under `DDD-ground-02`, "not read" looks like a coverage state (`unknown`), not a position. If so, a1 and a2 may not be separable on ground. `UNVERIFIED — Emil review.` | Hold until the act map is reviewed. |
| **F-2** | The layer carries inherited tolerance; an axis can emulate it but must be remembered. | "Roughly fourteen seconds against 800 ms" cannot be checked: the run records no backoff parameters. The "declared-space limit" citation should be `DDD-ground-05`/`-02` (§1). | Accept with the arithmetic flagged and the citation corrected. |
| **F-3** | Reuse (component fan-out) and replication (decision fan-out) are duals. | Only the component case is claimed (`DDD-address-03`). The decision case is computable from predicates today. | Accept as a finding; decision fan-out as a successor candidate claim. |
| **T2a act map** | Axes: act-kind, target client, gateway state, calling context. Five occurrences. | Two checks: whether "gateway state not read" is a position (F-1), and whether each retry attempt carries its own verdict, which `core/09` requires before the attempts are inner acts (§1). | Emil reviews. |

## 8. Registry fit

**`established_by: DDD-ground-06` does not fit.** All 70 registry entries name a `core/` document.
The drift validator enforces this: it reports E10 when no document's `ddd:contract` establishes
the term.

| Option | Cost |
|---|---|
| **Establish it in `core/14-indexed-determination.md`** `[PROPOSED]` | A short section embedding the `canonical_md`, `act-address` added to the contract's `establishes`, and the intro's "two terms and no more" amended. This is precedented: `core/14` already establishes two `draft` terms, and it comes after every term the definition uses. Tested in scratch: 0 errors, warnings unchanged. It is a prose change to a core document, beyond the prompt's "claim, term, decision". |
| Establish it in another doc | `core/06` (composition) or `core/09` (individuation) would read naturally. Both are earlier in the reading order, so each needs its own backward-edge check. Not tested. |
| Hold the term | File `DDD-ground-06` alone. The address then has no canonical text to embed downstream, and downstream prose must cite the claim. |

Either way, **drop the bare `address` alias**. It matches ordinary English ("addresses", `core/04`
line 505) and raises a W1 forward-use warning. Keep `act address`.

## Rulings requested

1. The weakest point: repair `DDD-ground-06`'s falsifier or region for temporal predicates before
   filing, or file as drafted with the tension recorded in notes.
2. Phoenix out of upstream `core/`: adopt the proposed wording, or rule otherwise.
3. The `DDD-ground-05`/`-02` citation correction in `DDD-ground-06` (and F-2).
4. Rule 1: keep `DDD-ground-06` and `DDD-address-01` joined, or split.
5. `DDD-address-05`: file with the dependency named, or hold.
6. `DDD-address-03`: file with the seam-decay reliance as a successor item.
7. E-1, F-1, F-2, F-3 and the T2a act map.
8. The term's home: `core/14`, another doc, or hold. The alias drop.
9. The Danish glossary rows (`handlingsadresse`, `lagsti`): rule the terms, or leave them out of
   GATE 2.
