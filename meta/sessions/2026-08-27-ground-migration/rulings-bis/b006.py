# W0-bis :: delivered (41) — 3 right, 38 wrong. The worst rule in the table.
# `ground\b[^.]{0,50}\bdeliver\w*` matches the word "delivery" anywhere within 50 characters, and the
# v5.5.0 release descriptor, the CHANGELOG entry and core/13-delivery.md all name the `ground` area
# and the `delivery` area in the same breath — so thirteen `DDD-ground-0N` identifiers and the area
# name itself became S3, the delivered sense.
R = {
 4:'U-mention',
 5:'S1', 26:'S1',             # "the **ground** area names what a determination stands on"
 21:'U-mention',
 22:'U-idname', 23:'U-idname', 24:'U-idname', 25:'U-idname',
 52:'U-ordinary',             # "what was refused, and on what ground"
 53:'U-idname',
 132:'S1',                    # "determination records are indexed by ground (position, as-of, …)"
 168:'U-idname', 169:'U-idname',
 480:'U-mention',
 546:'S1',                    # "ground-dependent technical" — closes only over real ground
 677:'U-idiom', 678:'U-idiom',
 679:'S1',                    # the predicted-ground note
 695:'U-mention', 696:'U-mention',
 697:'U-idname',
 730:'S1',                    # "Holding note — ground axes, decision regions, …"
 1096:'S3',                   # "the standing rule not fix the output given the ground"
 1114:'S3',                   # G_A — "accessible and delivered to arrangement A"
 1115:'S2',                   # "the ground-access hypotheses"
 1118:'S1',                   # "relevant ground", the G* half
 1119:'S3',                   # "accessible and delivered ground"
 1133:'S1',                   # "the delivery distinction applied to ground" — SR-2's object exactly
 1134:'S2',
 1198:'U-idname', 1199:'U-idname',
 1358:'S1', 1359:'S1',        # ground-indexed determination
 1549:'S1',                   # "verification against real ground"
 1556:'S1',
 2494:'U-idiom',
 2564:'U-idname', 2587:'U-idname', 2628:'U-idname',
 2671:'S1',                   # "ground-not-as-expected"
 2681:'S2',                   # prd-ground-as-ontology.md
}
WAS = {i:'S3' for i in R}
