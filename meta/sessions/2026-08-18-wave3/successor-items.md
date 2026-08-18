# Wave 3 successor items

Booked at the close, none begun, per the do-not-bundle rule.

1. **The `term:training` supersession question.** The revision foundation's §8 commentary —
   "closure does not make training available or unavailable as a hard gate" — contradicts the
   settled term's letter ("closure decides whether training is *available*"). `DDD-hyp-05` was
   drafted to need no ruling on it. Whether "decides availability" softens to a gradient is a
   supersession against a settled term, to be examined with the sign-flip (`DDD-cost-11`) and
   rent-vs-own material it touches. Flagged at the GATE 4 ruling for the freight successor list.
2. **Ref-staleness instrumentation.** `DDD-dec-25` records that W6 cannot see a missed pin
   advance (it resolves against the pinned ref). Whether ref staleness deserves its own
   instrument — e.g. a check against the upstream repo's latest tag — is a design question,
   deliberately not resolved in the recording decision.

   **Second motivating case — Track 1 session, 2026-08-18** (appended by that session at Emil's
   instruction; the item stays Wave 3's, unscoped, and is not begun here).

   The gap, stated as a property of the instruments rather than of the incident: **W5 and W6
   check that the pin is internally *consistent*; neither checks that it is *current*.** Both
   resolve against the ref the pin names, so a pin left at a superseded tag resolves cleanly —
   every id exists at that ref, every status matches, every content hash verifies — and reports
   green. A missed advance is invisible to both by construction, not by oversight.

   **The asymmetry this session surfaced, which the Wave 3 record does not yet carry.** The
   failure is one-directional. A *premature* bump — naming a ref that does not exist yet — fails
   loudly: the shallow clone cannot resolve the ref and E12 fires. A *missed* bump — naming a ref
   that exists but has been superseded — is silent. The instruments are therefore already
   sensitive to one error and blind to its mirror image, and only the silent one has occurred
   (Wave 3, `DDD-dec-25`) or been risked (this session: a bump was instructed on the premise that
   an upstream PR had merged; it had not, and nothing in the repository would have reported the
   pin as stale had the tag existed and the advance been skipped).

   **Input class, named and not scoped.** Detecting a missed advance requires an input no
   validator currently reads: **the upstream repository's tag list** — that is, knowledge of refs
   *other than* the one pinned. Every existing check (E12, E13, W5, W6, W7) operates inside the
   pinned ref's contents. This is a different input class, not a stronger predicate over the same
   input, which is why it cannot be reached by extending an existing warning. Whether it belongs
   in `validate-core-order.py`, in CI, or in neither is a design question and stays open. Nothing
   about the instrument's shape, trigger, severity, or home is decided here.
2a. **Unchecked assertion under `ddd:ref`.** Booked by the Track 1 session (2026-08-18) at
   Emil's instruction; stated, not scoped, and not begun.

   `E13` enforces byte-match between an embedded block and upstream `canonical_md` — for
   `ddd:embed` only. **For `ddd:ref` no instrument checks anything about the text near the
   marker.** But a quoted block placed under a ref marker *asserts to a reader that the words are
   canon's*. That assertion is unchecked, and it is the assertion a projection most wants to be
   able to trust.

   **Evidence, from one document.** Track 1 compared all nine marker-plus-quote blocks in
   `projections/tracks/01-determination.md` against upstream at `v5.8.0`. Three diverged, and no
   validator could have reported any of them:

   - **a genuine truncation** — `term:commitment-level`'s quote dropped canon's final clause
     ("the question is never which of three kinds an actor is, but at which levels the
     arrangement has committed"). Caught by hand, at the moment a prose citation was converted to
     a marker, because converting is when the claim changes. Now corrected.
   - **a disclosed partial quote** — `term:admission-test`'s quote carries only the first of
     canon's two halves, deliberately, with the rung's prose saying so and rung 3 supplying the
     second. Legitimate, and indistinguishable from the truncation by any byte comparison.
   - **an upstream formatting quirk** — `term:closure`'s `canonical_md` is the one registry entry
     not written as a blockquote, so a quoting projection either reproduces the inconsistency or
     silently normalises it. Words identical.

   **Same shape as item 2, on a different axis: the instrument set is tight on one construct and
   silent on its neighbour.** Ref-staleness is pin-currency; this is quote-fidelity. Both are
   places where a check exists for the strict form and nothing exists for the loose one beside it.

   **The open question, stated rather than answered.** Whether `ref` should be checked *at all* is
   genuinely undecided. A ref is a **pointer**, not a transclusion, and a quote under it may
   legitimately be partial — rung 2's disclosed half-quote is the proof that a strict byte-match
   rule would be wrong. Any instrument here would need to distinguish *disclosed partial* from
   *silent truncation*, which is a question about what a projection may declare, not only about
   what a validator may compute. **Shape, severity, and home are all open**, including whether the
   answer is an instrument at all rather than a convention.

3. **The luck-ruling step upgrade.** `DDD-frame-15`'s derivation step 3 restates the rev18
   correction-1 ruling with provenance because the note is unratified; when the ground-axes
   note's corrections ratify, the step becomes citable by reference and the notes can shrink.
4. **Docs 00–07's `outcome` pointers.** Seven accepted W1 advisories; each document gains its
   forward pointers when next touched, never in a sweep (GATE 2 ruling).
5. **Paper A session.** Starts from `batch-p-projection-readiness.md`; front matter pins
   *projection of actor-indexed-determination at v5.7.0*; H set carried as predictions with
   unrun falsifiers, never findings; Q38b and Q36 pull material available as positioning prose,
   deliberately unfiled.
6. **The measure paper's discharge section.** Q33-B/C's aggregation results (N·H(V), the
   correlation inequality, the standing/occasioned bit asymmetry) file there as projections of
   `DDD-frame-16`, per the rev18 routing — next session's material, not this one's.
7. **Upstream cosmetic, noted not opened.** `term:closure` is the only entry in
   `core/graph/terms.yaml` whose `canonical_md` is not written as a markdown blockquote, so it
   reads differently from every other term wherever it is quoted. A one-line tidy for a later
   wave that is already touching the registry. Not opened here: it changes a settled term's
   canonical bytes, which would move its content hash and fire `W6` on every downstream pin —
   cheap to do, not free, and not this session's.

8. **Standing, inherited:** the open-conjunct actor-indexing on `term:escape-mechanism`
   (flagged at DDD-dec-15, carried); the empty-option-set generator (open, unexamined); the
   ground-provenance taxonomy's institutional slot (Q27-gated); Q36's ranking instrument
   (corpus-gated with Q9); Q37 and S-1 (post-Q27 wave); the carve (seeded, waiting); the
   repo-name question (charter-level, Emil-only).
