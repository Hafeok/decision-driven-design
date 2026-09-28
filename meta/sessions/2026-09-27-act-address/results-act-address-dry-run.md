# Results — act address dry run (T1, T2a)

**Pre-registration.** `prereg-act-coordinates.md`, revision 3, fixed 2026-09-27.
The file was hashed immediately after fixing, and this run is scored against that hashed version.
SHA-256: `ef34e3bc14ab793800edd8c096e82adf0652ef8bc284d54d52efd20f8bf5f5eb`.

**Status.** Dry run. Unratified. The act maps below were built by Claude alone. Nothing is filed, and Emil rules.

**Scope.** This is a dry run: T1 is analytic, and T2a was written inside the framework. It tests the instrument, not the claim. T2b (Phoenix) is the independent test.

**Weakest point of this run.** The T2a result depends on which ground axes Claude declared, gateway state in particular. A different mapper could produce a different address set. The act map in §2 is therefore the first thing to check.

---

## 1. T1 — date validator

| Prediction | Verdict | Note |
|---|---|---|
| One address at the parent layer, three occupants | **Holds** | Analytic |
| Day-29 split in B anchors at the parent layer; unanchored without the layer | **Holds, with a correction to the prediction** | See E-1 |
| Time | Not exercised | As pre-registered |

**E-1 — error in the pre-registration, attributed to Claude.** The prediction said that under plain D the seam decision would be *unanchored*. It is not unanchored.

Under plain D, the parent act (validate the date) and the child acts (the `D ≤ 28` part and the `D ≥ 29` part) sit on overlapping positions. So the split decision's predicate matches the children as well as the parent. The decision is therefore **ambiguously anchored**: it lands in the governing set of acts that did not make it. The layer path removes that ambiguity by anchoring it at the parent only.

The extension is still needed. The failure mode it prevents is ambiguity, not absence. The pre-registration is not edited; this record stands instead.

## 2. T2a — retry-count

**Act map** (Claude, for review). Ground axes declared: act-kind, target client, gateway state, calling context.

| Occurrence | Occupant | Layer path | Ground position |
|---|---|---|---|
| a1 | LLM | delivery pipeline / scaffold client / configure resilience | configure-retry, payment client, gateway state not read |
| a2 | on-call engineer | operations / incident / reconfigure resilience | configure-retry, payment client, gateway degraded |
| a3.n | program | runtime / checkout request / outbound call / retry attempt *n* | execute-retry, payment client, transient error |

| Prediction | Verdict | Note |
|---|---|---|
| Every act occurrence gets exactly one address | **Holds** | Five occurrences (a1, a2, and three attempts), five addresses |
| A seam decision anchored by the layer, not by plain D | **Holds, same correction as E-1** | See F-2 |
| A component pulled by two or more occurrences, fan-out computable forward | **Indeterminate** | See F-3 |
| Dependent acts sharing an address, separated only by time | **Holds** | Retry attempts 1 to 3 of one call share an address. Each depends on the previous one failing. |
| T3 | Not exercised | T2a has no sign-off act |

No falsifier in §6 of the pre-registration fired.

## 3. Findings, all flagged `(UNVERIFIED — Emil review)`

**F-1 — One decision, three addresses.** The track says that all three actors resolve the same axis. Under D, they resolve the same *decision* at three different *addresses*, because they act on different ground: at scaffold time, during an incident, and at runtime.

Candidate C would have merged these into one coordinate with three occupants. It would then have compared the behaviour of acts that do not share ground. D compares behaviour across actors only where occupants actually swap at one address, for example if the LLM took over incident reconfiguration.

This is the first case where D and C disagree on real material. D's answer is the one consistent with K3.

**F-2 — The layer carries inherited tolerance.** The seam decision is how the retry policy fits the checkout latency budget. Three retries hold a request for roughly fourteen seconds against a budget of 800 ms. The same retry act under a batch-job parent would face a different tolerance. The layer path is what distinguishes the two.

Plain D can emulate this with a declared calling-context axis, and this run did declare one. The difference is that the layer is derived from composition, while the axis must be remembered and declared. An undeclared context axis falls under `DDD-ground-01`'s declared-space limit. The layer does not.

**F-3 — Two kinds of fan-out.** There are two, and T2a shows both:
- **Component fan-out.** `HandleTransientHttpError` is a library component pulled by every client occurrence. A version change reclassifies transient errors for all of them. Its fan-out is computable only from a derivation record, which T2a lacks, so the prediction is indeterminate here.
- **Decision fan-out.** The LLM *copies* the retry policy into each new client rather than sharing it. When the retry-count decision changes, the affected set is every occurrence its applicability predicate matches, not a component's pullers. This fan-out is computable today from predicates alone.

Replication and reuse are duals. Reuse concentrates seam risk in a component. Replication spreads one decision across many occurrences. The method should query both.

## 4. Rulings requested

1. Accept E-1 as a correction record.
2. Review the T2a act map, specifically the axis declarations behind F-1.
3. Rule F-1 to F-3: accept as findings, `[PROPOSED]`, or strike.
