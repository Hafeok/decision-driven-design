# GATE 3 — M-2 and M-3, as diffs

**draft-pending-ruling.** Commit `fa98148`. Nine hunks in one file; no other file touched;
nothing filed in either repository.

---

## M-2 — the §8 refinement

Placed **after** Estimability and **before** §8.1, as a rung *above* the three requirements
rather than a fourth failure mode. The three are conditions for the measure to exist and be
computable at all; this one is a strengthening some tasks meet.

```diff
+**A rung above closure, and the note should name it.** ... Call a predicate **constructively
+closed** when the verdict is not merely checkable but **computed by rule** from ground available
+at the act — a procedure returns the correct output directly, and there is no candidate search to
+price. Closure asks whether adequacy can be *evaluated* within declared bounds [term:closure];
+constructive closure asks whether the verdict can be *produced*. The date task of §4 is
+constructively closed, and that is why its entropies are exact and exhaustive rather than sampled:
+there `H(V)` is not merely defined and available but **computed**.
+
+**This does not trip the retirement it appears to approach.** ... [DDD-frame-09, retired;
+DDD-frame-06; DDD-measure-11]. Constructive closure does not contradict that finding; it
+**sidesteps** it. Where the verdict is computed by rule there is no search left to be expensive,
+so the premise the retirement turns on is absent rather than denied — and the scoped survivor of
+that retirement ... is untouched either way [DDD-frame-05].
+
+*Canon's closure vocabulary does not currently carry the constructive/verification distinction ...
+a dedicated claim node is pending canon filing; until it lands, the citation basis is closure, the
+separation of closure from generation cost, and the measure's silence on search, as above.*
```

**Three things about this draft worth ratifying explicitly.**

The rung earns its place from the paper's own material rather than from assertion: **the date task
is constructively closed, and that is why §4's entropies are exact and exhaustive.** The
distinction does visible work in the manuscript before it is proposed to canon.

The retirement sentence is the load-bearing one and it is stated as *sidesteps, not contradicts* —
the premise is **absent rather than denied**. `DDD-frame-09` is cited **marked retired**, so a
reader is never misled about its status, and `DDD-frame-05`'s scoped survivor is named as
untouched in either direction.

**The scope guard held and nothing was filed.** The flag uses the same idiom §3.1 and §5.3 carried
before their nodes landed — which is the idiom this same gate is *removing* from those two
sections. That symmetry is deliberate: the device now marks only the genuinely open item, and the
manuscript carries exactly one pending-node flag.

---

## M-3 — five upgrades

| # | § | Before → After |
|---|---|---|
| **U-1** | §5.3 | pending-node sentence **deleted**; `[term:seam-identity]` → `[term:seam-identity; DDD-measure-14]` |
| **U-2** | §3.1 | pending-node sentence **deleted**; the Admissibility block-quote gains `[DDD-measure-15]` inline at its last clause |
| **U-3** | §2.1 | `[DDD-cost-01]` → `[DDD-cost-30; DDD-cost-01]` |
| **U-4** | §5.2 | *"With `A` the answer, this instance's verdict variable, and `R`…"* → *"…verdict variable — a determinate assessed by a declared predicate, which is what makes it a verdict rather than merely an outcome [DDD-frame-14] — and `R`…"* |
| **U-6** | §8.1 | gains a sentence: *"The framework names the same boundary in register terms: every completed act lands an **outcome**, and a **verdict** exists only where governance has declared a predicate to assess it [DDD-frame-14; term:outcome]."* |
| ~~U-5~~ | ~~§5.1~~ | **dropped per ruling** — a marker with no work to do |

U-1 and U-2 are the two the freight session left deliberately: each deletes the sentence that was
waiting and cites the node it was waiting for. U-3 cites the node that exists *because* of that
sentence. U-4 and U-6 are the two `DDD-frame-14` sites, and both add a clause rather than only a
bracket — the register split is worth a reader's sentence, not just a marker.

---

## R-5 — the two repairs, minimal

Both sites reproduced the clause `DDD-dec-15` corrected: capacity shortfall stated as *the
definition* of escape rather than as *one generator* of it.

```diff
 §5.1  capacity sits outside the identity: the bits an actor can supply per act,
-      with escape the residual exceeding them, is a named next result
+      with capacity shortfall one generator of escape, is a named next result

 §9    ... requires a model of actor capacity — the bits an actor can supply per act,
-      with escape the residual exceeding them [DDD-cost-05].
+      with residual an actor has taken up escaping where it exceeds them [DDD-cost-05].
```

The two repairs are worded differently on purpose. §5.1's sentence is about **capacity**, so it
takes the generator reading. §9's is about **rate–distortion's split**, so it takes
`DDD-floor-01`'s re-scoped region wording — *residual an actor has taken up* — which is the limb
that claim now quantifies over. Both remove the identity reading; neither adds a claim.

**Caveat 3 was left alone**, as reported and accepted at Gate 1: its wording never carried the
defective clause.

---

## Verification at this gate

- **Reference closure over the whole manuscript: 27 claim IDs, 17 term IDs, all resolve.** Three
  claims are newly cited by M-2 (`DDD-frame-05`, `DDD-frame-09`, `DDD-measure-11` — the last was
  already cited elsewhere), and `term:outcome` enters with U-6.
- **Every `§`-reference resolves to a heading that exists.** Zero dangling.
- **Exactly one pending-node flag remains** in the manuscript, and it is M-2's.
- **Diff scope: one file, nine hunks, +41/−13.**

## Length

9,057 prose words, up **319** on the 8,738 you ratified at Gate 2. The growth is the booked M-2
refinement and nothing else — the five upgrades and two repairs are net **−4** words between them.
Reported under the principle you set: the body is as long as its booked content.

## Carried to M-4 (Gate 4)

**Appendix A owes nine rows**, all to be copied verbatim at the new pin:

| Claims | Terms |
|---|---|
| `DDD-cost-30`, `DDD-frame-05`, `DDD-frame-09`, `DDD-frame-14`, `DDD-frame-16`, `DDD-measure-14`, `DDD-measure-15` | `term:act-individuation`, `term:outcome` |

Plus the three **verbatim refreshes** ruled at Gate 1 (`term:verdict`, `DDD-cost-05`,
`DDD-floor-01`), the pin advance to **v5.7.0 / v0.4.0**, `N` joining §2's Notation list, and the
word count.

**One thing to note about `DDD-frame-09`'s row:** it is the manuscript's first *retired* citation.
Appendix A's preamble already defines the status — *"retired is superseded"* — so the row needs no
new apparatus, but it is the first time that definition does any work.
