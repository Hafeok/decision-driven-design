# upstream :: everything outside core/ (60 rows) — root docs, meta, releases, i18n
# FINDING at 520: the Danish glossary glosses `grund` as BOTH senses in one entry — "Det, en
# beslutning afgøres *imod*" (what a decision is determined against, S1) "— det læsbare underlag,
# aktøren inspicerer" (the readable substrate the actor inspects, S3). The definition layer's
# multi-sense defect has been translated, so the migration owes i18n a pass it did not budget for.
R = {
 3:'S2',
 9:'U-mention',            # "the ground area's exposition" — the claim-area name, no predication
 11:'S1',13:'S1',
 20:'S2',32:'S3',34:'S2',35:'S5',36:'S5',      # release descriptors — IMMUTABLE, classified only
 44:'S5',
 46:'S3',
 54:'S2',
 56:'U-ordinary',          # "literature-grounded"
 59:'S3',60:'S3',61:'S3',
 62:'S1',63:'S1',          # production-as-ground.md, cited by name
 64:'S2',65:'S2',66:'S2',67:'S2',68:'S2',      # the Hayek dispersion material
 82:'S1',                  # "decidable over digital ground"
 90:'S2',91:'S2',
 92:'S3',93:'S3',
 102:'S3',105:'S2',106:'S2',
 111:'S1',112:'S1',
 114:'S2',
 115:'S3',116:'S3',117:'S3',119:'S3',
 122:'S1',
 131:'S1',133:'S1',134:'S1',135:'S1',137:'S1',138:'S1',139:'S1',140:'S1',141:'S1',
 147:'S1',
 151:'S2',152:'S2',
 153:'S1',154:'S1',        # "the actor's model of the ground diverged from the ground"
 159:'S3',160:'S2',161:'S3',162:'S3',
 167:'S5',
 520:'U-multi',            # the Danish glossary: S1 and S3 in one gloss
 521:'S1',
}
