# Bootstrap — the freight session (2026-08-17)

The invocation message that accompanied `prompt.md`, recorded verbatim as the session's arrival
record. Committed **before** the session ran, per the convention this session files at Batch E
(`E-2`). This directory is that convention's first instance.

---

Read prompt-freight-session.md in its entirety — this session follows it exactly, including every
gate and the batch structure.

This is the freight session: the accumulated small-items list from the escape, corpus, and vocabulary
sessions, batched by repair family (A prose/references, B registry seams, C the diachronic carve,
D measure-region filings, E instrumentation/conventions, F capacity residue rulings, G cross-repo
one-liners). Nothing here is new design work — every item was found and recorded in a prior session,
and the prompt names each item's source. The session's virtue is closing items at their booked size;
where an item resists its booking, defer with the resistance named rather than expanding.

First act, before anything else: create meta/sessions/ in decision-driven-design and commit this
prompt and bootstrap into meta/sessions/2026-08-17-freight/ — the session inaugurates the convention
it files at Batch E.

Fetch all three repos — actor-indexed-determination at head (v5.5.0 plus the merged addendum),
decision-driven-design at head, product-cli (one item, G-7, otherwise untouched). Verify every
manifest item against head first: anything a prior session already fixed en passant is reported and
struck, not re-done.

Rules that override anything you might infer:

* Interactive canon curation. Stop at every gate for Emil's ruling. Merge nothing.
* Supersession, never rewriting, for ratified text (precedent: DDD-dec-09, DDD-dec-10, DDD-dec-15).
* Batch C (the diachronic carve) is the one known-large item: plan before cutting, and if the plan
  exceeds the session's remaining budget, Emil rules defer-whole — no partial carve.
* Batch F is rulings-first: present the evidence both ways, draft both readings, file only what the
  ruling licenses.
* D-3's admissibility wording is load-bearing: computable-from-ground-without-being-handed-the-
  verdict, never "cannot determine the verdict" — the second form breaks the actor-allocation
  instance.
* Commit drafts to feature branches before reporting at each gate, bodies marked
  draft-pending-ruling.

Begin with step 1 and end your first report at GATE 1: manifest items verified against head with
already-fixed items struck, the batch order confirmed or re-argued, and the C-1 carve plan's size
estimate.

---

## Session parameters

| Field | Value |
|---|---|
| Date | 2026-08-17 |
| Type | Interactive canon curation (freight) |
| Branch (all three repos) | `claude/freight-batch-closure-41w96f` |
| Upstream base | `actor-indexed-determination` @ `4f58837` (v5.5.0 + merged addendum) |
| Downstream base | `decision-driven-design` @ `4848b9e` |
| product-cli base | `d506ac9` (G-7 only) |
| Gates | 6 |
| Principal | Emil |
