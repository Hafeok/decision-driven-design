# W0-bis :: ordinary-english (32) — 20 wrong, and the errors run in the DANGEROUS direction.
# Every error is a FALSE POSITIVE: a technical use labelled ordinary English, and therefore excluded
# from the migration. The rule's own word list is the mechanism — `some|any|no|conceptual` match
# "against SOME ground", "not about ANY ground", "NO ground at all", where the use is technical.
R = {
 1:'S1',                          # "a determination against some ground"
 136:'S3',                        # "capability not *about* any ground"
 248:'S3',                        # hold-overflow: "the decision's governing ground does not fit"
 249:'S2',                        # "pre-resolve some ground into the constraint"
 282:'U-idiom', 394:'U-ordinary', 399:'U-idiom', 420:'U-ordinary',
 462:'S1',                        # "the ground-applicability holding note"
 479:'U-ordinary',
 524:'S1',                        # "a determination against some ground"
 589:'U-missing',                 # "the three actors have *different* ground missing" — relabelled, class held
 590:'S1',                        # "a decision made against no ground at all"
 616:'S2',                        # the escaped-decision record's fields: "no axis, no ground, no principal"
 624:'S2',                        # "asserted, never measured — no ground exists for it"
 738:'S1',                        # "no outcome-relevant alternative declared over any ground"
 817:'S2',                        # "how much ground can be supplied by citation" (Q27)
 835:'S1',                        # "placing decisions on the ground"
 858:'U-ordinary', 903:'U-ordinary', 904:'U-ordinary',
 915:'S2', 916:'S2',              # the record's ground field
 994:'U-ordinary', 1084:'U-idiom', 1265:'U-idiom',
 1485:'S2',                       # "some ground is yours and some is not" — encode/verify
 1650:'S2', 1726:'S2', 1727:'S2', # "no ground in this repo at all" — no evidence held
 2402:'S2',                       # "a statement that mentions no ground is suspect" — the predicate field
 2423:'S2',
}
WAS = {i:'U' for i in R}
