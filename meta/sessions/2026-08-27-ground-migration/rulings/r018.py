# downstream :: root docs, graph pins, meta (60 rows)
# 899/900 are the two rows the re-extraction could not locate: the audit's own session-index line in
# meta/sessions/README.md, written in its working tree and not committed at the read commit. They are
# the audit counting itself a third time, beyond the 101 its SELF skip removed. U-selfcount.
R = {
 523:'S2',                 # "the `ground` PRD" — the G-track PRD
 526:'S2',527:'S2',
 531:'S3',532:'S3',
 533:'S1',534:'S1',535:'S1',
 537:'S2',538:'S2',540:'S2',
 541:'S1',542:'S1',
 547:'S1',                 # "a decision was encoded whose ground still moves"
 548:'S3',                 # INV-6 prefix ordering: ground -> decisions -> task, into the context
 549:'S3',
 551:'U-ordinary',         # "how well the principle is grounded"
 552:'S1',
 556:'S3',557:'S3',
 558:'S2',                 # `ground-prd.md`
 559:'S3',
 560:'S1',                 # graph/upstream.yaml — the term:ground PIN
 565:'S3',
 632:'U-ordinary',         # "posed on IB's ground" — the idiom
 635:'U-ordinary',         # "this claim also grounds why ..." — explains, no filed edge
 637:'S3',638:'S3',
 639:'S2',
 640:'U-ordinary',641:'U-ordinary',   # "Grounded, exclusionary"; "is established ground"
 648:'S3',
 651:'S1',655:'S1',
 657:'S2',
 666:'S1',669:'S1',674:'S1',680:'S1',
 685:'S2',
 686:'S1',699:'S1',702:'S1',
 713:'U-idname',           # "the ground-01 join" — the node identifier
 885:'S2',
 886:'S3',
 887:'S2',
 889:'S1',890:'S1',891:'S1',
 894:'S2',
 895:'U-ordinary',
 896:'S2',897:'S2',898:'S2',
 899:'U-selfcount',900:'U-selfcount',
 901:'S2',
 902:'S1',
 906:'S5',
}
