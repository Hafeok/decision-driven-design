# Manifest — the primer session

*draft-pending-ruling (Gate 4)*

Interactive drafting session, four gates, all held for Emil's ruling. Nothing merged; nothing
filed in canon.

## Deliverables

| Artefact | Where | State |
|---|---|---|
| The declaration | `meta/the-declaration.md` | Filed verbatim as supplied, §D's four open items included (`b009fba`); byte-identical to the source Emil provided |
| The primer | `projections/primer/primer.md` | Drafted at Gate 3, line-level ratified; draft marker removed at Gate 4 |
| The generator | `projections/primer/generate.py` | Thirteen generated regions from pin `v5.12.0`; stamp (pin + digest); `--check` fails on missing or stale |
| Session records | `meta/sessions/2026-09-01-primer/` | prompt, bootstrap, gate1-filter, gate2-outline, g4-quote-check.py, this manifest |

## The gates

| Gate | Held on | Ruling |
|---|---|---|
| 1 | The filter (89 claims: 4 established all formal, 11 reported all assets reproducing, 70 projected, 4 retired) and the survivor set against the predicted ten | Accepted; graph governs over the prediction; §§2/3/5 source from terms and normative decisions; §4 takes the reported floor mechanism; both status findings recorded, not repaired; pin `v5.12.0` |
| 2 | The outline; the absent declaration; `term:delivery` at *draft*; the example set | All four approved; declaration supplied and filed; §5.1's coordinate-system recording promoted from caution to procedure |
| 3 | The draft (419 lines, 3,630 words, ~2,700 hand-written) | Ratified as drafted, cuts and length accepted |
| 4 | This close | Held |

## Instruments run at the close

- `generate.py --check` — green: stamp present, pin `v5.12.0`, all thirteen regions current.
- `g4-quote-check.py` (this directory) — an independent extraction path, deliberately not the
  generator checking itself: ten term regions verbatim against `terms.yaml` at `v5.12.0`; the
  declaration region carries §A and §B-3 byte-for-byte; **zero quoted blocks exist outside
  generated regions**, so the check is exhaustive over every quoted node.
- Declaration source diff — `meta/the-declaration.md` byte-identical to the file Emil supplied.
- Reference closure — all 35 ids cited in the primer resolve: terms and upstream ids at
  `v5.12.0`, downstream ids at head; none unresolved.
- Validators, both repos, fresh runs — all green at the ruled baseline (upstream 32 warnings +
  66 core-order warnings, zero W4; downstream 6 warnings; decisions clean in both).

## Recorded for the freight list

**One item: `DDD-measure-11` and `DDD-measure-13`.** Both sit at `reported` on
derivation-only evidence, where `spec/claim-format.md` §5 requires an evidence entry whose
asset reproduces; measure-13's falsifier pattern ("none — arithmetic given the chain rule")
matches two `established` claims, making it the sharper case. The five projected-with-assets
claims were the control: their notes withhold `reported` deliberately, so the defect is real,
not an artefact of the check. The primer reads both conservatively as `projected`; the repair
is a canon session's act, not this one's.

## Arrival failure number seven

**The declaration.** The session prompt referenced `meta/the-declaration.md` as committed
("it is committed at `meta/the-declaration.md`") when it existed in neither repository: it
had a commit prompt written and was referenced as landed without confirmation. Surfaced by
the Gate 2 search; supplied by Emil at the Gate 2 ruling; filed verbatim at Gate 3 entry
(`b009fba`). This is the same failure class as DDD-dec-17's five and the vocabulary session's
sixth — a delivered governing artefact that did not arrive — caught this time by the
convention the earlier failures bought: verifying the referenced object against the repo
before building on it.

## Strengthening over the ruled outline

**Every quoted node became a generated region.** The outline planned the declaration as
hand-carried prose under a Gate 4 verbatim check; the draft instead generates it from
`meta/the-declaration.md`, alongside the ten term boxes generated from the registry at the
pin. Combined with the stamp and an independent close-out check, drift in any quoted node is
mechanically impossible rather than checked-for. **This is the pattern the next projection
should inherit**: quote nothing by hand; generate every quotation from its source, stamp the
generation with pin plus digest, fail the close on missing or stale, and verify once more
through a second code path.

## Noted, not repaired

§2.4 teaches `DDD-ground-04`'s two retro-filing fields without naming the id inline, where
§2.2 names `DDD-ground-01`. The text is ratified; the asymmetry is recorded here for Emil to
rule on (a one-clause insertion) or leave.

## Out of scope, untouched

No status repair filed. No pin advance. The transfer (item 7) not assumed. Q40–Q46, the
accountability arity successor item, W4's local items, the `verdict` and `projection`
collisions, Paper A and the measure note — none touched. No canon edit in either repository;
the upstream repo carries no change from this session.

## The pin, at close

The primer describes canon at `v5.12.0`, the version `graph/upstream.yaml` pins. The ground
migration's changes reach it at the next pin advance — a governed decision, recorded when it
happens, with `generate.py` re-run against the new tag as part of that act.
