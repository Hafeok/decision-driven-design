#!/usr/bin/env python3
"""G1 — proposed senses for the live rows the corpus gained since the
classification was fixed. PROPOSED, draft-pending-ruling: these enter the
working ledger only on Emil's Gate 1 ruling.

Keyed by content, never by position (the seed's third method mechanism): each
key is a distinctive substring of the occurrence's context, unique within its
file at head. The decision rule is the audit's — read the predicate applied
to the word, never the compound. Each entry: (repo, path, anchor) -> (sense,
reason). Rows in audit output, session records and release descriptors are
not ruled here — they are counted, never migrated.
"""

R = {
# ---- upstream README.md (19 rows; the predecessor ruled the file into the
# migration at its GATE 1; its per-row senses were reported only in aggregate
# — S1x8 S2x4 S3x4 S5x1 U-x1 — so these are re-derived and the two
# aggregate divergences are flagged in the gate report) ----
('upstream','README.md','determines choices against ground: programs'): ('S1','world predicate: determined against; the ident flag on this row is a false positive of the ground:-colon rule'),
('upstream','README.md','What ground does the determination depend on?'): ('S1','world predicate: depended on by the determination'),
('upstream','README.md','**Ground** — what they are determined against'): ('S1','the definition itself'),
('upstream','README.md','resolving of a decision against ground'): ('S1','determined against'),
('upstream','README.md','prior commitments, ground channels, checks'): ('S3','channel: the delivery path; verb-shaped under SR-2'),
('upstream','README.md','⟨task, ground, acceptance relation'): ('S1','the index tuple names the case coordinate'),
('upstream','README.md','an actor reading ground, **with an accountable party named**'): ('S3','act predicate: reading'),
('upstream','README.md','relevant ground is observable and adequacy'): ('S2','store predicate: observable within declared bounds (term:closure)'),
('upstream','README.md','left open at the act, holding ground fixed'): ('S2','held fixed for the quantification'),
('upstream','README.md','verdict induced by the task over the ground distribution'): ('S5','population predicate: distribution over cases'),
('upstream','README.md','verdict function with the required ground truth'): ('U-ordinary','"ground truth" is ordinary English of measurement, none of the five'),
('upstream','README.md','how much governing ground it can have available at once'): ('S2','store predicate: available at once (hold capacity)'),
('upstream','README.md','output decoupled from correct ground because'): ('S3','act predicate: absent/false/present at the act'),
('upstream','README.md','because that ground is absent, false, or present'): ('S3','same predication, second token'),
('upstream','README.md','Actorhood means resolving choices against ground'): ('S1','determined against'),
('upstream','README.md','**Ground and judgment dependence** Situated'): ('S2','H2 heading; the predication is availability, made explicit in the next sentence'),
('upstream','README.md','advantage as ground becomes unavailable'): ('S2','store predicate: unavailable'),
('upstream','README.md','|decisions, ground, determination, actor'): ('U-mention','doc-map row citing the primitive by name'),
('upstream','README.md','ask what must be determined, what ground it depends on'): ('S1','depended on'),

# ---- papers/paper-a/paper-a.md (25 rows added by the revision) ----
('downstream','papers/paper-a/paper-a.md','leave open at the act, held at fixed ground.** [DDD-frame-02'): ('S2','held fixed'),
('downstream','papers/paper-a/paper-a.md','leave open at the act, **held at fixed ground**: the alternatives'): ('S2','held fixed'),
('downstream','papers/paper-a/paper-a.md','configuration and the ground at the act are both given'): ('S3','at the act'),
('downstream','papers/paper-a/paper-a.md','It is not variation > across ground — a cryptographic hash'): ('S1','world predicate: variation across the case'),
('downstream','papers/paper-a/paper-a.md','The held-at-fixed-ground clause is a repair'): ('U-mention','names the clause, not the object'),
('downstream','papers/paper-a/paper-a.md','conflating four phenomena: outcome variation across ground'): ('S1','variation across'),
('downstream','papers/paper-a/paper-a.md','Quantifying at *fixed ground* is what excludes it'): ('S2','fixed'),
('downstream','papers/paper-a/paper-a.md','**Variation across ground is not discretion**'): ('S1','variation across'),
('downstream','papers/paper-a/paper-a.md','standing configuration and this act\'s ground are given'): ('S3','this act\'s, given at the act'),
('downstream','papers/paper-a/paper-a.md','no residual discretion at fixed ground is *predetermined*'): ('S2','fixed'),
('downstream','papers/paper-a/paper-a.md','standing configuration and the ground jointly fix the output'): ('S1','the case jointly fixing the outcome'),
('downstream','papers/paper-a/paper-a.md','together with > the ground at the act determines the resolution'): ('S3','at the act'),
('downstream','papers/paper-a/paper-a.md','configuration and the ground at the act, together, fix the resolution'): ('S3','at the act'),
('downstream','papers/paper-a/paper-a.md','asks whether standing configuration and ground jointly determine'): ('S1','jointly determine'),
('downstream','papers/paper-a/paper-a.md','whether standing configuration and ground determine the resolution [DDD-frame-17, falsifier]'): ('S1','determine'),
('downstream','papers/paper-a/paper-a.md','decides acceptability over accessible ground within declared bounds'): ('S3','accessible'),
('downstream','papers/paper-a/paper-a.md','demand time, memory, permissions or ground no arrangement has'): ('S2','store predicate: has/holds; bare of a delivery verb'),
('downstream','papers/paper-a/paper-a.md','| Ground | Assignment | What would overturn it |'): ('U-mention','column header naming the coordinate'),
('downstream','papers/paper-a/paper-a.md','ground missing to one arrangement is available to another'): ('S3','missing/available to an arrangement'),
('downstream','papers/paper-a/paper-a.md','does any of those has ground the walk assumed missing'): ('S3','missing/has at the act'),
('downstream','papers/paper-a/paper-a.md','feedback density, ground access, checker cost'): ('S3','access'),
('downstream','papers/paper-a/paper-a.md','its ground by provenance, its predicates by closure rung'): ('S2','coded by provenance — SR-4 attribute on the held object; boundary case, flagged'),
('downstream','papers/paper-a/paper-a.md','ground provenance (§2.4, this paper\'s analysis and not canon)'): ('S2','provenance attribute; boundary case, flagged'),
('downstream','papers/paper-a/paper-a.md','The gap is grounded in a **control condition'): ('U-ordinary','"grounded in" — a different word'),
('downstream','papers/paper-a/paper-a.md','the gap, grounded in a control condition'): ('U-ordinary','"grounded in"'),

# ---- papers/paper-a/paper-a-supplement.md (15 rows; the appendix rows are
# generated from the pinned upstream — they carry canon's words and move when
# canon moves, never as wave work) ----
('downstream','papers/paper-a/paper-a-supplement.md','keep citing a commit whose prose says `ground distribution`'): ('U-mention','quotes the phrase as vocabulary'),
('downstream','papers/paper-a/paper-a-supplement.md','five-way ground provenance (controlled, observed'): ('U-mention','cites the passage by its name'),
('downstream','papers/paper-a/paper-a-supplement.md','## S5. Vocabulary: `ground` in its population sense'): ('U-mention','word-as-word'),
('downstream','papers/paper-a/paper-a-supplement.md','The word `ground` had been carrying five senses'): ('U-mention','word-as-word'),
('downstream','papers/paper-a/paper-a-supplement.md','canon still reads `ground distribution` at `v5.12.0`'): ('U-mention','quotes canon\'s current wording'),
('downstream','papers/paper-a/paper-a-supplement.md','commitments leave open at the act, held at fixed ground. | | `DDD-frame-03`'): ('S2','generated appendix row quoting DDD-frame-02; moves when canon moves'),
('downstream','papers/paper-a/paper-a-supplement.md','together with the ground at the act determines the resolution; exercised'): ('S3','generated appendix row quoting DDD-frame-17; moves when canon moves'),
('downstream','papers/paper-a/paper-a-supplement.md','| `DDD-ground-01` | normative | projected'): ('U-idname','node identifier; SR-6'),
('downstream','papers/paper-a/paper-a-supplement.md','| `DDD-ground-02` | conceptual | projected'): ('U-idname','node identifier; SR-6'),
('downstream','papers/paper-a/paper-a-supplement.md','| `DDD-ground-03` | conceptual | projected'): ('U-idname','node identifier; SR-6'),
('downstream','papers/paper-a/paper-a-supplement.md','| `DDD-ground-05` | conceptual | projected'): ('U-idname','node identifier; SR-6'),
('downstream','papers/paper-a/paper-a-supplement.md','nor the estimability of the ground distribution. | | `DDD-measure-17`'): ('S5','generated appendix row quoting DDD-measure-16; W1-bound with the claim, moves when canon moves'),
('downstream','papers/paper-a/paper-a-supplement.md','commitments leave open at the act, **held at fixed ground**: the alternatives'): ('S2','quotes the amended term:residual-discretion draft'),
('downstream','papers/paper-a/paper-a-supplement.md','admissible once the standing configuration and the ground at the act are both given. It is not variation'): ('S3','same quotation, at-the-act clause'),
('downstream','papers/paper-a/paper-a-supplement.md','are both given. It is not variation across ground — a cryptographic hash'): ('S1','same quotation, variation-across clause'),

# ---- papers/paper-a/response-to-review.md (15 rows; the response is the
# paper's record of what it conceded — quotes the review and the repairs) ----
('downstream','papers/paper-a/response-to-review.md','### 2.2 Raw ground collapses the allocation measure'): ('S1','the review\'s object: world facts fed raw to the measure'),
('downstream','papers/paper-a/response-to-review.md','mutual information reports the ground as carrying the entire verdict'): ('S1','world facts carrying the verdict'),
('downstream','papers/paper-a/response-to-review.md','no rule for turning that ground into an answer'): ('S1','same object, next clause'),
('downstream','papers/paper-a/response-to-review.md','together with the ground at the act fix the resolution'): ('S3','at the act'),
('downstream','papers/paper-a/response-to-review.md','amended to quantify **at fixed ground**: the alternatives'): ('S2','fixed'),
('downstream','papers/paper-a/response-to-review.md','configuration *and this act\'s ground* are both given'): ('S3','this act\'s'),
('downstream','papers/paper-a/response-to-review.md','phenomena are separated: variation across ground, epistemic uncertainty'): ('S1','variation across'),
('downstream','papers/paper-a/response-to-review.md','no residual discretion at fixed ground is exactly what'): ('S2','fixed'),
('downstream','papers/paper-a/response-to-review.md','### 3.3 Split relevant ground from accessible ground'): ('S1','relevant: the world-facts half of the review\'s split'),
('downstream','papers/paper-a/response-to-review.md','Split relevant ground from accessible ground (review §6)'): ('S3','accessible: the delivered half'),
('downstream','papers/paper-a/response-to-review.md','versus `G_A` (ground accessible and delivered to arrangement'): ('S3','accessible and delivered'),
('downstream','papers/paper-a/response-to-review.md','the delivery distinction applied to ground. It is **canon work'): ('S1','the undivided object the distinction applies to'),
('downstream','papers/paper-a/response-to-review.md','the tuple\'s `ground` coordinate is a settled term'): ('U-mention','names the coordinate as a term'),
('downstream','papers/paper-a/response-to-review.md','§8.1 now says that ground missing to one arrangement is available'): ('S3','missing/available'),
('downstream','papers/paper-a/response-to-review.md','on the explicit ground that those sentences are about warrant'): ('U-ordinary','"on the ground that" — ordinary English of reasons'),

# ---- the rest of the live additions ----
('downstream','papers/measure-note/measure-note.md','Worked by `measure-nonuniform-ground.py`, named before the vocabulary moved'): ('U-idname','asset filename; the note itself says why it keeps the name'),
('downstream','core/decisions/DDD-dec-34.yaml','meta/migration-plan-ground.md predicted three W6'): ('U-idname','file path'),
('downstream','core/decisions/DDD-dec-34.yaml','repairs and are not ground-migration work'): ('U-mention','names the programme'),
('upstream','core/decisions/DDD-dec-31.yaml','DDD-ground-0'): ('U-idname','node identifiers; SR-6 (three rows, one anchor: all three tokens sit in DDD-ground-0N ids)'),
}

if __name__ == '__main__':
    import collections
    print(f'{len(R)} proposed rulings')
    print(dict(collections.Counter(v[0].split("-")[0] for v in R.values())))
