# Session prompt — the measure note: the discharge section

Repositories: `actor-indexed-determination` (upstream, head — canon at **v5.7.0**) and
`decision-driven-design` (downstream, head — the manuscript's home). Fetch both.
Session type: **interactive paper drafting.** Projection work throughout: the paper may not
introduce claims; every load-bearing statement cites a graph node or is flagged register-native.
Hold at every gate. British spelling; one idea per sentence; the theorem is Shannon's, first,
always; principle, never law; the identity is reported as arithmetic and projected as a model —
never fused.
**First act, before Gate 1:** commit this prompt and bootstrap to
`meta/sessions/2026-08-19-measure-discharge/` in `decision-driven-design`, per DDD-dec-20.

## What this session is

The measure note (`papers/measure-note/measure-note.md`, revised through the external-review
response) gains its **discharge section** — booked at Wave 3's routing as "the aggregation
mathematics files to the measure paper as a section waiting on its claims." The claims landed at
v5.7.0 (`DDD-frame-15`, `DDD-frame-16`); the wait is over. The session also takes the small
already-ruled manuscript items that accumulated while canon moved. **This is a bounded session:**
one new section, one §7 refinement, a citation-upgrade pass, and the context doc's regeneration.
The paper is otherwise done and reviewed; the failure mode is re-opening what the review already
settled.

## The work, itemised

### M-1 — the discharge section (the session's centre)

New section, placed by the session's proposal at Gate 1 (natural home: after §5's instances,
before §6's epistemics — the aggregation results are worked content, and §6's honesty table must
cover them too). Content, all projection:

- **Per-act discharge as the primitive** [DDD-frame-16]: standing inherited per act, occasioned
  produced per act; the paper's per-act constitutive Scale paragraph is the same fact in measure
  vocabulary — cite, don't restate.
- **Aggregate discharge** `N·H(V)` over N draws — *strengthening the ratified Scale repair*: the
  aggregation section must reconcile with (and cite) the Scale paragraph's "expected information
  in N independent draws" reading; the section is that reading given content, never a reopening of
  the `nH(V)` error the review caught.
- **The correlation inequality** `H(V₁…V_N) ≤ N·H(V)`, equality iff independent — the formal
  statement of why caching, memoisation, and batch decisions work: correlated verdicts mean the
  aggregate demand is less than the per-act sum, and the difference is what one resolution
  amortised across correlated acts captures.
- **The O(1)/O(N) asymmetry** — authoring paid once, discharge inherited per act: "paid once,
  inherited by every run" as a theorem about the two sides' scaling, wired to the standing/
  occasioned registers [DDD-frame-16, the cost split citations already in §2.1].
- **What the section does not claim** — the honesty discipline extended: the inequality is
  Shannon's (chain rule + subadditivity); the identification of "correlated verdicts" with
  "cacheable work" is the modelling claim, and the correspondence (do measured verdict
  correlations predict realised amortisation?) is untested — one paragraph, §6's register.
- **Q-C's exposition** (distribution-weighted discharge as the measure's `P` doing its work) —
  one paragraph, no claim, per its Wave 3 flag.
- Numbers only from scripts: if the section states worked figures (e.g. the date task's aggregate
  under correlation), a new asset in the `measure-*` pattern computes them, reproducing, landed
  beside the others upstream with the paper's Reproduction section extended. If the section can
  carry its content with the existing assets, prefer that — a new asset is licensed, not required.

### M-2 — the §7 refinement: constructive closure (Q32, filed reading)

§7 currently distinguishes existence / availability / estimability. Add the strongest rung:
**constructively closed** — the verdict computed by rule, no candidate search to price — where
`H(V)` is not merely defined and available but computed. Two sentences of consequence: the
retirement history ("closed predicates make intelligence unnecessary" was retired because
verification-closure leaves generation expensive) is not tripped by constructive closure, which
sidesteps rather than contradicts it. **Scope guard:** this files as refinement against canon's
closure vocabulary as it stands at v5.7.0 — if the session finds Q32 needs a canon node first
(the survey question: does the closure vocabulary carry the constructive/verification split
anywhere?), the refinement is drafted citing what exists and the gap is flagged for the Q-wave,
not filed here.

### M-3 — the citation-upgrade pass (already ruled, exact IDs in hand)

`measure-paper-context.md` carries these from the freight session:
- §5.3's "a dedicated claim node for the iterated form is pending canon filing" → cites
  **DDD-measure-14**.
- §3.1's pending-node flag for admissibility → cites **DDD-measure-15**.
- §2.1's demand/cost distinction → gains **DDD-cost-30**.
Plus from Wave 3: the §5.2/§5.1 encode-verify and allocation readings may now also cite
`DDD-frame-14`'s registers where the prose speaks of verdicts landing — the session proposes
each upgrade with the line it touches; nothing is rewritten, only citation markers added or
upgraded.

### M-4 — front matter and apparatus

Pin line advances to the tags the citations resolve against (upstream **v5.7.0**; downstream at
its current tag or the merge SHA per the established pattern — session verifies which resolves).
Appendix A gains the newly cited nodes' rows, statements verbatim. Word count reported without
padding; the body grew by one section and the target conversation is: report the number, Emil
rules if it matters.

### M-5 — context doc v3

`measure-paper-context.md` regenerated: canon source at v5.7.0, the discharge section recorded as
landed, the settled OPEN items struck with their rulings, M-2's outcome recorded, and the
remaining genuinely-open items carried (the correspondence campaign, the information-theorist
certification with the reviewer brief as instrument, multi-actor composition still owed).

## Walk

1. **Fetch, verify, propose.** Both repos at head; manuscript as merged; all assets re-run;
   every existing citation re-verified at v5.7.0. The M-2 survey question answered. Report:
   proposed placement and outline for M-1, the new-asset question (needed or not, with the
   figures the section wants), M-3's upgrade list line-by-line, and any drift between the
   manuscript and canon introduced since the revision merged. **GATE 1 — hold.**
2. **M-1 drafted** — the section in full, citations inline, the honesty paragraph in §6's
   register, asset built first if licensed. **GATE 2 — hold for line-level ratification.**
3. **M-2 and M-3.** The §7 refinement and the citation upgrades, as diffs. **GATE 3 — hold.**
4. **M-4 and M-5.** Front matter, Appendix A, word count; context doc v3. **GATE 4 — hold.**
5. **Close.** Validators; reference closure over the manuscript's citations; branch, PR,
   manifest. **GATE 5 — hold; Emil merges.**

## Out of scope

Paper A (next session; this session's close should note anything M-1 produced that Paper A's §
structure will want, as one line in the manifest). The correspondence campaign (protocol stands,
unrun). The escape/judgment split's content (named next result, stated and stopped — frame-15/16
do not change the paper's caveat 3, which concerns the *cleave within the residual*, a different
object; the session verifies the caveat still reads correctly against the new section and reports
rather than rewrites). Multi-actor composition (still owed; caveat stands). The carve, the
Q-wave, S-1, G-track. Any canon filing — including the Q32 node if the survey finds the gap. Do
not bundle.

## Standing note

Commit drafts before reporting at each gate, bodies marked draft-pending-ruling. The review
settled this paper's register: concede before the reader can object, state what computations do
not establish, end sections on what is taken or conceded rather than on triumph. The discharge
section enters a reviewed manuscript — it must read as if it had been through the same review,
because the next reviewer will hold it to that standard.
