# The Tier–Specification Inverse Law

> Insertion block for `core/03-the-polanyi-floor`. Derives, rather than asserts, why withholding encoded specification forces required actor tier upward — and why past a point that demand can be met only by selection, not training.
>
> **Depends on:** the floor decomposition `floor = intrinsic + transfer` (this file), the Law's four stores and last wind (`core/01-the-law`), and the success decomposition `1 − success = esc_escape + esc_wind` (`core/01-the-law`, action/levers block).
>
> **Establishes:** the inverse law asserted in the action/levers block, with its mechanism, its scope condition (recurrence structure of the environment), and its two failure modes.

---

## 1. What must be derived

The action/levers block asserts:

> Required actor tier rises as encoded specification falls, because withheld specification relocates demand onto the actor's judgment store; past the transfer floor, that demand can be met only by a lower intrinsic floor — selected, not trained.

Three links in that chain are not yet derived, only stated:

- **(L1)** that *withheld encoded specification* lands on the *actor's judgment store* rather than escaping or vanishing;
- **(L2)** that the resulting demand, once it exceeds the transfer floor, falls on the *intrinsic* component specifically;
- **(L3)** that the intrinsic component is reachable by *selection* but not by *training*.

This block derives each from the conservation identity and the floor decomposition already in canon. Nothing new is postulated; the law is a consequence.

---

## 2. Setup: demand conservation on a fixed action

Fix an action `t` at assurance level `α`. By the Law, the governing decision set `D(t,α)` has fixed cardinality (fixed by the task, per the finite-index lemma) and is allocated across four stores with no silent residual:

```
|D|  =  enc  +  mech  +  jud  +  esc                      (conservation, Principle 1)
```

Encoded specification is the portion carried by `enc` (constraint form) and `mech` (criterion form) — the two extra-actor stores. Write the **encoded mass** and the **actor-borne mass**:

```
E   =  enc ∪ mech        (encoded, extra-actor)
J   =  jud               (judgment — per-run, actor-resident)
                          (esc is defect exposure; held aside, addressed in §6)
```

Because `|D|` is constant, any decision not carried by `E` and not escaped must be carried by `J`:

```
J  =  |D|  −  E  −  esc                                    (†)
```

Identity (†) is the whole mechanism. It is not a modeling choice; it is conservation rearranged.

---

## 3. L1 — withheld specification lands on judgment

Suppose the program *withholds* encoded specification: it declines to encode decisions that could be encoded, lowering `E` by ΔE. By (†), holding `esc` fixed (the program does not intend to expose defects):

```
ΔJ  =  −ΔE                                                 (withheld encoding → judgment)
```

Every decision removed from the encoded stores reappears in the judgment store. It cannot vanish — `|D|` is conserved — and it cannot silently escape without the program accepting defect exposure. So **withheld specification is not absence of demand; it is relocation of demand onto the actor.** This is L1.

This is the same mechanism as checklist-relocation, run in reverse. A checklist moves a decision `jud → enc` to relieve the load-pressured judgment store. Withholding specification moves it `enc → jud`, loading the judgment store on purpose. The direction differs; the conservation is identical.

**Why a program would do this** (not yet the derivation, but the reason the case is real): in an adversarial or non-recurring environment, encoding is *counter-productive* — a stable encoded doctrine is a fixed target an adversary optimizes against, and a non-recurring environment offers no second instance for the encoding to amortize over. There, withholding is correct, and the relocation onto `J` is the intended design, not a failure. §5 makes the recurrence condition precise.

---

## 4. L2 — the loaded judgment store draws on the intrinsic floor once transfer is exhausted

The judgment store is not free capacity. Its per-run cost is bounded below by the actor's Polanyi floor for this (task, actor, environment) triple:

```
floor(t, actor, env)  =  intrinsic(t, actor)  +  transfer(t, actor, env)
```

The floor is the measured reach of Polanyi's condition — unsharable experience yielding unsharable decisions — per (task, actor). It decomposes into an **intrinsic** part (final, actor-and-task inherent) and a **transfer** part (movable, manufactured by training; expertise and articulability opposed by mechanism).

The judgment store executes decisions the actor cannot obtain from transmitted context — it draws on the actor's own capability. As demand on `J` rises (from §3), the actor absorbs it first out of the **transfer-floor capacity**: the trainable, embodiment-manufactured competence. That capacity is finite. Once demand on `J` exceeds what the transfer floor can carry:

```
J  >  (capacity reachable by lowering transfer floor)
   ⇒  residual demand falls on the intrinsic floor
```

The residual has nowhere else to go: it is not encodable (or it would have been carried by `E`), not escapable (or the program accepts defects), and not absorbable by more training (or it would have been transfer, not intrinsic). By elimination it lands on the intrinsic component. This is L2. Formally it is the same by-elimination move as escape's definition — *decided by nobody* — applied one level up: *carriable by no store but the intrinsic floor.*

```
demand on J:  ── carried by transfer floor ──┼── carried by intrinsic floor ──▶
              low J (spec present)            │   high J (spec withheld)
                                     transfer capacity exhausted
```

---

## 5. L3 — the intrinsic floor answers to selection, not training

The transfer floor is, by its canonical definition, the part of the floor **manufactured by training** — embodiment is intra-actor encoding that amortizes without externalizing. Training's entire reach is the transfer component; that is what "transfer" names.

The intrinsic floor is, by the same decomposition, the part training does **not** reach — final, inherent to the (task, actor) pair. Two consequences follow directly:

- **Training cannot lower it.** Applying more training to an intrinsic-dominated residual moves nothing: `d(intrinsic)/d(training) = 0` by definition of the split. This is the flat-derivative floor signal from the cost metric, now located on the actor axis: training spend with no floor movement means the residual is intrinsic.
- **Selection can find a lower one.** Intrinsic floor is a property of the *(task, actor)* pair — it varies across actors. A different actor may have a lower intrinsic floor for the same task. Selection is exactly the operation that measures the intrinsic floor (qualification testing = Tier-3 sampled exercise on the actor) and rejects actors whose intrinsic floor exceeds the demand. Selection does not *manufacture* a lower floor; it *finds a pre-existing* one.

So the only lever for intrinsic-dominated residual is selection. This is L3. Training and selection are not interchangeable tools for the same job — they act on different components of the floor, and the decomposition dictates which acts on which.

---

## 6. The law, derived

Chaining L1→L2→L3:

```
E ↓  (specification withheld)
  →  J ↑            by (†), conservation                          [L1]
  →  once J exceeds transfer capacity, residual falls on intrinsic floor  [L2]
  →  intrinsic floor answers to selection, not training           [L3]
  ∴  required actor tier ↑  as encoded specification ↓
```

> **Tier–Specification Inverse Law (derived).**
> For a fixed action at fixed assurance, lowering the encoded specification mass `E` raises the judgment mass `J` by exactly `−ΔE` (conservation). While the increase is absorbed by trainable transfer-floor capacity, the required actor is met by **training**. Once `J` exceeds that capacity, the residual falls on the intrinsic floor, which **training cannot lower and only selection can reduce**, by finding an actor whose intrinsic floor is lower. Hence required actor tier rises monotonically as encoded specification falls, and the lever crosses from training to selection at the point where judgment demand exhausts the transfer floor.

The crossover point is not a constant — it is set by how much of the floor is transfer vs intrinsic for this triple, which §7 ties to the environment.

---

## 7. Scope condition: recurrence sets the transfer floor

Transfer floor is manufactured by training, and training amortizes embodiment over repetition. So the size of the transfer floor — how far training gets before selection takes over — is set by the **recurrence structure of the environment**:

```
recurring, stable environment      →  large transfer floor
                                       (embodiment amortizes; training reaches far)
                                       →  training-dominated; low tier suffices at high spec

non-recurring, adversarial env      →  small transfer floor
                                       (no repetition to amortize; adversary defeats
                                        stable encoding, so spec is withheld by design)
                                       →  intrinsic-dominated; selection-dominated; tier climbs
```

This closes the two inverted cases from the action/levers block without re-asserting them:

- **Heart surgeon** — recurring, stable action; specification *maximized* (protocol, fellowship curriculum); large transfer floor; training reaches the reachable floor; tier is an aptitude threshold, not a rare-actor search.
- **Delta operator, CQB** — non-recurring, adversarial; specification *withheld by design* (encoding is a defeatable fixed target, no repetition to amortize); small transfer floor; residual intrinsic-dominated; selection-dominated; tier climbs precisely where doctrine thins.

The inverse law is therefore not a claim about military vs medical work. It is a claim about **recurrence**: adversarial non-recurrence shrinks the transfer floor, which forces demand onto the intrinsic component, which forces the selection lever, which raises the required tier. Medicine could produce the same structure (a novel, non-recurring, high-variance intervention would); special operations could produce the surgeon's structure (a recurring, encodable sub-task trains rather than selects).

---

## 8. Two failure modes the derivation predicts

Because the law is derived from conservation, its violations are diagnosable:

- **Withholding specification while forbidding escape and lacking actor capacity.** By (†), if `E` is lowered, `esc` is held at zero, and `J` exceeds both transfer and intrinsic capacity, the identity cannot balance — the excess *must* escape. The program believed it was withholding to load a capable actor; it was in fact manufacturing defect exposure. Detection: escape-class output appears despite a nominally competent actor. The cure is to restore `E` (encode) or lower the intrinsic floor (select up), not to train.
- **Training against an intrinsic-dominated residual.** By L3, training spend with no floor movement (`d floor/d training ≈ 0` with residual > 0) means the residual is intrinsic. Continuing to train is wasted spend; the lever is misapplied. This is the actor-axis image of the specification-side kill signal — flat derivative over nonzero residual — and its cure is selection, not more training hours.

Both are the mis-lever failure of the action/levers block, now shown to be conservation violations rather than merely empirical observations.

---

## 9. Caveat: the crossover is per-triple, not universal

The derivation gives a *monotone* relationship (tier rises as spec falls) and a *crossover* (training → selection at transfer exhaustion). It does **not** give a universal crossover point. Where training stops reaching depends on the transfer/intrinsic split for the specific (task, actor, environment) triple, and that split is *measured* — attributed to the intrinsic vs transfer components by exercise (qualification testing for the intrinsic floor; training-response measurement for the transfer floor), not derived. The law's form is projected; its crossover point is reported only after the split is measured for the triple in hand. Stating a universal tier threshold would fuse the derived form with an unmeasured number — the same projected/reported discipline the rest of the canon holds.
