# The decision rule fixed here and applied from this point on, so the pass is consistent rather
# than case-by-case: read the PREDICATE APPLIED TO THE WORD.
#   world predicates   (obtains, varies, moves, is uncontrolled, is a dimension/region)  -> S1
#   store predicates   (held, available, assembled, filed, cited, pinned, stale, complete) -> S2
#   act predicates     (read at, delivered, consulted, present, in context, bound at as-of) -> S3
#   rule predicates    (is a standard, determines acceptability, is the regulation)       -> S4
#   population preds   (distribution over, evaluated over)                                -> S5
# downstream :: projections/tracks/01-determination.md (27)
R = {
 573:'S3',                 # term:capability — "what ground you can read"
 577:'S1',581:'S1',584:'S1',
 585:'S2',                 # authority/convention *supply* ground — supplied representations
 593:'S2',594:'S2',        # "never been assembled" / "the same ground available"
 595:'S3',604:'S3',606:'S3',607:'S3',608:'S3',   # the per-actor "Ground it can actually read" table
 609:'S1',
 610:'S2',611:'S2',612:'S2',613:'S2',            # term:closure and its exposition — observable
 614:'S3',                 # "none consulted"
 615:'S2',618:'S2',619:'S2',
 620:'S1',                 # term:answerability — "against what ground"
 623:'S2',625:'S2',626:'S2',628:'S2',629:'S2',
}
