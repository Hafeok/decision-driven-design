# W0-bis :: the ANCHORED-CLASS reopening (29 rows). Emil's GATE 3 ruling: an anchored-class
# error reopens the question rather than being absorbed. It did, and the reopening CLOSES,
# because the mechanism is decidable rather than a sampling matter.
#
# ONE mechanism, in two directions, and it is rule ORDERING, not window width:
#   `ddd-ground-id` is the LAST rule in the audit's ordered table and first match wins.
#   * 15 rows whose token IS a `DDD-ground-0N` identifier were taken by an earlier anchored
#     rule (declared-ground-axes 11, reads-different-ground 2, relevant-conditions 1,
#     software-module 1) and given a sense. An identifier inherits no sense.
#   * 13 rows whose token is NOT the identifier were taken BY `ddd-ground-id`, because the
#     identifier sits elsewhere in the 240-character window. The inverse steal.
# Both sets were found MECHANICALLY over the whole corpus, not sampled, so the class is closed.
#
# Plus one row from the second anchored sample that is not mechanically findable:
#   1581 — `reads-different-ground` on 'never read as ground', where the sense is the ledger's
#   basis (S2), not what an actor reads at an act.
R = {48: 'U-idname', 128: 'U-idname', 434: 'U-idname', 435: 'U-idname', 484: 'U-idname', 622: 'U-idname', 931: 'U-idname', 945: 'U-idname', 1013: 'U-idname', 1016: 'U-idname', 1150: 'U-idname', 1223: 'U-idname', 1377: 'U-idname', 1378: 'U-idname', 2592: 'U-idname', 7: 'U-mention', 18: 'S1', 19: 'S1', 28: 'U-mention', 495: 'S1', 496: 'S1', 569: 'S1', 722: 'U-mention', 1000: 'U-idname', 1009: 'S1', 2618: 'S1', 2627: 'S2', 2666: 'S2', 1581: 'S2'}
