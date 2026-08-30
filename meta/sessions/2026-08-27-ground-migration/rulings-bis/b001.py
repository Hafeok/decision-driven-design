# W0-bis :: rule-standard-context (13) — adjudicated in full at GATE 3, recorded here
# The rule matches `policy|standard|statute|regulation` within 70 characters of the token, and
# `[^.]` does not stop at a clause boundary, so "outcome variation across ground ... a fixed POLICY"
# and "no ground TRUTH ... the STANDARD varies by rater" both became S4.
R = {203:'U-idiom', 321:'S1', 519:'S1', 627:'S4', 1121:'S3', 1122:'S1', 1131:'S1', 1137:'S3',
     1375:'S4', 1546:'U-idiom', 1694:'S2', 2506:'S2', 2532:'S2'}
WAS = {i:'S4' for i in R}
