#!/usr/bin/env python3
"""Classify every extracted occurrence into exactly one sense, or U.

METHOD, stated so the result is checkable rather than trusted.

Rules are ordered; the first that matches wins; each rule carries the reason it
is safe. The rules were written by reading real context, not invented — every
one was drawn from occurrences sampled out of the extract, and the residual
(nothing matched) is reported rather than absorbed into a default. A default
would be the single thing that could make this table lie, so there is none:
unmatched occurrences are U-residual and are counted as such.

Per GATE 1 rule 2, ratified: sense is read from the sentence, not from the
compound. Where a rule keys on a compound it is because reading the occurrences
showed that compound to be consistently one sense — that is a result, and each
such rule says so.

SENSES
  S1  conditions in the case whose variation moves the outcome past tolerance
  S2  representations the arrangement holds
  S3  representations delivered at the act
  S4  institutional rules and standards
  S5  the population over which demand is measured
  U   will not sit in exactly one sense, with the reason recorded
"""
import json, re, sys, collections

def rx(p):
    return re.compile(p, re.I)

# (sense, name, pattern, why-this-is-safe)
RULES = [
 # ---- S5: the population. Narrow and unambiguous. ----
 ('S5','ground-distribution', rx(r'(?<![A-Za-z0-9])ground[ _-]distribution'),
  'the compound denotes P, the distribution over inputs, in every occurrence read'),
 ('S5','distribution-context', rx(r'ground\b[^.]{0,60}\b(distribution|population|deployment)\b|\b(distribution|population)\b[^.]{0,40}\bground\b'),
  'the sentence quantifies over cases rather than describing one case'),

 # ---- S4: institutional rules and standards. ----
 ('S4','institutional-ground', rx(r'institutional[ _-]ground'),
  'canon and the software both use this compound for rules and standards, never for case facts'),
 ('S4','rule-standard-context', rx(r'ground\b[^.]{0,70}\b(statute|regulation|policy|standard|acceptance criteri|institutional rule)\b'),
  'the occurrence is a criterion of judgement, not material judged'),

 # ---- S3: delivered at the act. ----
 ('S3','reading-ground', rx(r'\b(read|reads|reading|resolves against|resolved against)\b[ _-]ground|ground\b[^.]{0,30}\bat the act\b|ground standing at'),
  'the act is named in the occurrence; what is at issue is what reached the resolver'),
 ('S3','poisoned-ground', rx(r'poisoned[ _-]ground|corrupt\w*[^.]{0,30}ground'),
  'term:poisoned-ground is "ground that is present but false: the substrate a determination reads" '
  '— present-and-read is the delivered object, not the world'),
 ('S3','delivered', rx(r'ground\b[^.]{0,50}\bdeliver\w*|deliver\w*[^.]{0,40}\bground\b'),
  'delivery is act-site indexed by term:delivery'),

 # ---- S2: representations the arrangement holds. ----
 ('S2','accessible-available', rx(r'(accessible|available|held|retrieved|observed|inferred|recorded)[ _-]ground|ground[ _-](accessibility|availability|provenance|item|items|registry|record|records|facts?|extraction|table|rows?)'),
  'the occurrence is about material the arrangement has, not about the world or the act'),
 ('S2','software-module', rx(r'src/ground|ground/|ground-cli|ground_[a-z]|ground\.rs|ground-registry'),
  'product-core/src/ground is documented as "code extraction into ground" — a store of extracted facts'),
 ('S2','characterised', rx(r'(un)?characterised|ground:\s*(un)?characterised'),
  "ledger-core's Ground enum is about whether facts are available for inspection"),
 ('S2','ground-coverage-assurance', rx(r'ground[ _-](coverage|assurance|channels?)|source coverage'),
  'DDD-ground-02 makes coverage and assurance properties of ground relative to a filed decision'),

 # ---- S1: conditions in the case. ----
 ('S1','admission-test', rx(r'varying[^.]{0,30}world|fact is ground|determined against|what they are determined against'),
  "term:admission-test and term:ground state the world-facing sense in these exact words"),
 ('S1','declared-ground-axes', rx(r'declared[ _-]ground|ground[ _-]ax[ei]s|determinable|dimension of variation'),
  'the registry declares dimensions of variation; DDD-ground-05 ties declaration to the determinable'),
 ('S1','relevant-conditions', rx(r'(relevant|raw|base|predicted|uncontrolled|digital)[ _-]ground|conditions in the case|state of the (world|case)'),
  'these compounds read as conditions obtaining, not as records of them'),

 ('S2','yaml-field', rx(r'ground:\s*\[|ground:\s*$|ground:\s*\n|-\s*ground:|\bground:\s*[a-z-]+\s'),
  'a serialised field name in the ledger and predicate formats: the value is the filed facts a '
  'decision was taken against, which is material the arrangement holds'),
 ('S2','filed-as-ground', rx(r'(fil\w+|ratif\w+|manufactur\w+|merg\w+|propos\w+|new|accepted|settled|existing)\s+(as\s+)?ground\b|\bground\b\s+(edge|edges|bundle|slice|sidecar)'),
  "the software's ledger sense: ground is a filed artefact a reviewer ratifies, which is held "
  'material and never the world itself'),
 ('S2','decisions-ground', rx(r"(decision|claim|node|set|predicate)('s|s')?\s+ground\b|ground\s+(for|of)\s+(the\s+)?(decision|claim|set)"),
  'ground relative to a filed decision, which DDD-ground-02 makes a property of held material'),
 ('S2','watched-not-grounding', rx(r'watched-not-[ _-]?grounding|grounding\s+edge'),
  'an edge kind in the ledger vocabulary, naming held provenance between filed objects'),

 ('S3','reads-different-ground', rx(r'\b(read|reads|reading)\b[^.]{0,40}\bground\b|\bground\b[^.]{0,25}\b(a determination|the resolver|the actor) reads'),
  'what reaches a particular resolver at a particular act, which is the delivered object'),

 ('S1','ground-the-task-faces', rx(r'ground (the|a) (task|case|act|arrangement) (faces|meets|encounters)|over the ground|against (the )?ground\b|ground (a|the) determination'),
  'the conditions determination runs against, stated world-facing'),

 ('U','ordinary-english', rx(r'\b(new|common|shaky|solid|firm|higher|lower|middle|conceptual|theoretical|philosophical|much|no|some|any|covered|breaking|break|broke|gained|lost|stands? on|shifts?|shifted|changed)\s+ground\b|ground\s+(has changed|shifts|is shifting)|on the ground\b|from the ground up'),
  'ORDINARY ENGLISH, not the technical term — "new ground", "common ground", "its ground has '
  'changed". These need no rename and a global search-and-replace would corrupt them, which is '
  'why they are counted as their own answer rather than folded into a sense'),
 # ---- U: named ambiguity, adjudicated once and applied. ----
 ('U','missing-ground', rx(r'missing[ _-]ground'),
  'spans S1 and S3 irreducibly: a relevant condition (S1) inadequately represented at the act (S3). '
  'This is the gap BETWEEN two senses and cannot be one of them'),
 ('U','ground-truth', rx(r'ground[ _-]truth'),
  'imported machine-learning idiom: the label set (S2, held) standing in for the world (S1). '
  'The idiom exists precisely because the two are conflated'),
 ('U','ddd-ground-id', rx(r'DDD-ground-\d'),
  'a node identifier, not a use of the word: the five claims it names are themselves split across '
  'senses (DDD-ground-02 is S2, DDD-ground-05 is S1), so the ID inherits no single sense'),
]

def classify(rows):
    out = []
    hits = collections.Counter()
    for r in rows:
        c = r['ctx']
        for sense, name, pat, why in RULES:
            if pat.search(c):
                r2 = dict(r); r2['sense'] = sense; r2['rule'] = name
                out.append(r2); hits[(sense,name)] += 1
                break
        else:
            r2 = dict(r); r2['sense'] = 'U'; r2['rule'] = 'residual-no-rule-matched'
            out.append(r2); hits[('U','residual-no-rule-matched')] += 1
    return out, hits

if __name__ == '__main__':
    rows = json.load(open(sys.argv[1]))
    out, hits = classify(rows)
    json.dump(out, open(sys.argv[2],'w'))
    print(f"{len(out)} classified")
    for (s,n),v in sorted(hits.items()):
        print(f"  {s}  {n:<28} {v:>5}")
