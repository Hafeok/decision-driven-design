# W0-bis :: reading-ground (99) — 83 right, 16 wrong. The BEST of the eight prose rules.
# The rule is `\b(read|reads|reading|...)\b[ _-]ground|ground\b[^.]{0,30}\bat the act\b`, and its
# adjacent alternative is sound: 'an actor reading ground' and 'ground available at the act' are S3
# every time. All 16 errors are one shape — the token is a SECOND `ground` in a sentence whose
# FIRST one triggered the rule: term:actor's 'reading ground: variation in declared ground',
# term:act's 'resolved against ground', term:residual-discretion's 'not variation across ground'.
# Those second occurrences are S1, and canon deliberately opposes them to the first in one breath.
R = {
 31:'S3', 33:'S3', 39:'S3', 40:'S3', 41:'S3', 113:'S3', 143:'S3', 145:'S3', 157:'S3', 170:'S3', 180:'S3', 188:'S3', 206:'S3', 209:'S3', 210:'S3', 213:'S3', 278:'S3', 295:'S3', 296:'S3', 300:'S3', 315:'S3', 316:'S3', 322:'S3', 327:'S3', 335:'S3', 346:'S3', 355:'S3', 356:'S3', 382:'S3', 385:'S3', 443:'S3', 450:'S3', 453:'S3', 454:'S3', 458:'S3', 515:'S3', 545:'S3', 598:'S3', 605:'S3', 667:'S3', 764:'S3', 905:'S3', 950:'S3', 953:'S3', 972:'S3', 981:'S3', 1067:'S3', 1072:'S3', 1073:'S3', 1076:'S3', 1077:'S3', 1080:'S3', 1081:'S3', 1086:'S3', 1087:'S3', 1088:'S3', 1089:'S3', 1092:'S3', 1093:'S3', 1102:'S3', 1106:'S3', 1107:'S3', 1108:'S3', 1120:'S3', 1125:'S3', 1128:'S3', 1129:'S3', 1175:'S3', 1181:'S3', 1183:'S3', 1206:'S3', 1229:'S3', 1232:'S3', 1246:'S3', 1253:'S3', 1267:'S3', 1281:'S3', 1283:'S3', 1294:'S3', 1299:'S3', 1301:'S3', 1497:'S3', 1498:'S3',
 142:'S1', 177:'S1', 189:'S1', 317:'S1', 336:'S1', 338:'S1', 357:'S1', 457:'S1', 599:'S1', 1074:'S1', 1091:'S1', 1103:'S1', 1233:'S1', 1282:'S1', 1284:'S1',
 1101:'S2',
}
WAS = {i:'S3' for i in R}
