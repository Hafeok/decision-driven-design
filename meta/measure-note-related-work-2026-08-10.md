# Measure note — related-work section (session yield, 2026-08-10)

Ratified at Gate 3 line-level, 2026-08-10. Placement per Gate 1 ruling: inserted between the
draft's §7 (Where the measure stops) and the caveats, which renumber to §9; the one-line result
renumbers to §10. Citations: `[DDD-…]` markers resolve against the principle repository at
v5.3.0 (`DDD-cost-01/02/03`, `DDD-cost-05`, `DDD-measure-02/11/12`) and this repository at head
(`DDD-cost-06/07`). Everything uncited is register-native (positioning prose or historical
attribution), per the session's standing rules. The integration diff against the uploaded
`measure-paper-draft.md` is `meta/measure-note-related-work-2026-08-10.patch`. Emil places the
section himself.

---

## 8. Related work

Each neighbour below is taken in turn, and each entry closes on what this note takes from that
literature or concedes to it. The epistemics — what the computations establish, and where the
falsifiable content lives — are §6's, and are not reargued here.

**Shannon (1948).** The theorem is Shannon's, and so is every formal object in this note: entropy,
mutual information, and the chain rule that carries conservation are used exactly as 1948 states
them. What the note contributes is the identification alone — specification demand as verdict
entropy (§2) — and that is a modelling claim, with its failure mode stated in §6. Nothing here
strengthens, extends, or tests Shannon's result. The dependence runs one way: where the
identification fails, the theorem is untouched; where it holds, every formal property the note
uses is inherited, not proved.

**Ashby.** Requisite variety (1956) is the rigorous ancestor, and the nearest one. Ashby stated
the regulator's burden in bits — the unit this framework lacked, as §1 records — and the
framework's conservation claim is Ashby's shape: a fixed quantity of disturbance that must be met
with variety from somewhere (§1). This note is the framework arriving where Ashby already stood,
and it arrives on a restricted region: the measure exists exactly where the acceptance predicate
closes (§7). What is added to Ashby is therefore not a stronger claim but a narrower one — an
exact domain on which the variety accounting is a theorem rather than a maxim. Off that domain,
the note concedes Ashby's own caution: he had the unit in hand and still declined to claim more
than a principle, and this note does the same.

**Kolmogorov complexity and MDL.** The nearest objection arrives from here: why entropy rather
than description length? The framework's answer is that the two are not rivals — they price
different sides of the act. What must be resolved at the act, over the ground the act faces, is
occasioned, and entropy prices it; the mechanism built once, before any act, is standing, and
description length prices it [DDD-cost-01; DDD-cost-03]. On this reading MDL's two-part form,
`L(model) + L(data|model)`, is not a competing measure of demand. Read as per-act rates it is the
cost decomposition laid over the same conserved identity [DDD-cost-03], and over `N` acts it
becomes `L(mechanism) + N·H(V|E)`, with computable crossover volumes at which a distinction flips
from occasioned to standing [DDD-cost-07]. The identity itself forces this division of labour:
pricing the standing side in captured information, `I(V;E)`, is degenerate, because conservation
makes the tradeoff exactly flat — every distinction buys precisely what it costs, and no
distinction can be priced ahead of another — so a graded build-out over volume requires the
standing side priced as description length, which is not a conserved quantity
[DDD-cost-02; DDD-cost-06]. Where the framework has looked for this structure in production data,
the evidence is consistent with the two-part form but cannot yet select the MDL form, and is filed
as basis rather than confirmation [DDD-cost-03]. Within this note's own region a second, older
answer stands: entropy is relative to a declared ground distribution and computable from it
[DDD-measure-12], and Kolmogorov complexity is neither — which is what makes demand
deployment-relative. The note therefore concedes the standing side to description length entirely:
entropy cannot price the mechanism, and the cost layer built on this identity is MDL's.

**Information bottleneck.** Tishby, Pereira and Bialek's bottleneck (1999) is the closest formal
machinery: `I(V;X)` set against `H(V|X)` is structurally a bottleneck functional. The difference
is what is done with it. IB optimises: it seeks the representation that best trades compression
against relevance, under a tradeoff parameter. This note optimises nothing. The chain rule split
is an identity, and no optimisation appears anywhere in it (§3) [DDD-measure-02]; the measure
prices the verdict, not the search for it, and says nothing about what a good representation costs
to find [DDD-measure-11]. Where the framework does optimise — which distinctions to encode
standing, and at what volume — is the cost layer downstream of this note
[DDD-cost-06; DDD-cost-07], and that is where IB is genuinely adjacent. Same functional, different
question: IB asks which representation to keep; this note asks what any representation, kept for
whatever reason, must sum to. When the framework poses the keeping question, it is posed on IB's
ground.

**Rate–distortion.** The note's stated next result (§5.3, §9) is the split of `H(V|X)` into judged
and escaped demand, which requires a model of actor capacity — the bits an actor can supply per
act, with escape the residual exceeding them [DDD-cost-05]. Rate–distortion theory is the natural
home for that split: what a channel must lose when the required rate exceeds the available one is
rate–distortion's founding question. The note states the result and defers to it; nothing of its
content is anticipated here.

**Brooks.** Brooks drew the line between essential and accidental complexity, and held that the
essential part is fixed by the task, invariant to tooling. That line receives an exact form here:
`H(V)` never mentions the actor (§2). It also receives a correction, already carried in §2 and §9:
*fixed by the task* is properly *fixed by the task, the tolerance, and the ground distribution*.
The exchange is even. The note gives Brooks's line the unit it lacked, and accepts from the
identity the parameter Brooks did not have to name — the deployment the task actually faces. The
distinction is inherited, not replaced.
