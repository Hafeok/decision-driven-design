# W0-bis :: ground-coverage-assurance (31) — 18 right, 13 wrong
# TWO mechanisms, not one. Ten of the thirteen errors are `DDD-ground-0N` IDENTIFIERS captured by
# this rule before `ddd-ground-id` could reach them, because the audit's table is ordered, first
# match wins, and the identifier rule sits LAST. That is a rule-ORDERING defect, distinct from the
# window-crossing defect, and it also reaches the anchored class. See b009.
R = {
 190:'S2', 337:'S2',
 422:'U-idname',
 423:'S2', 440:'S2',
 591:'U-idname',
 600:'S2', 601:'S2', 602:'S2',
 603:'S3',                    # "the narrowest ground" — the per-actor readable table
 644:'S2',
 694:'S1',                    # "the ground-applicability holding note"
 708:'U-idname',
 816:'S3',                    # "Ground channels — axes readable AT ACT TIME"
 991:'U-idname',
 1204:'S2', 1221:'S2', 1236:'S2', 1307:'S2', 1309:'S2', 1312:'S2', 1316:'S2', 1332:'S2', 1337:'S2',
 1220:'U-idname',
 1340:'S1',                   # "ground-incident rates"
 1341:'S2',
 2606:'U-idname', 2617:'U-idname', 2660:'U-idname', 2676:'U-idname',
}
WAS = {i:'S2' for i in R}
