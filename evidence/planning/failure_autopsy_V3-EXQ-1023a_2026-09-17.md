# Failure autopsy -- V3-EXQ-1023a (SD-106)

Status: confirmed (user gate 2026-09-17)
Generated: 2026-09-17T17:57:22Z
Run: `v3_exq_1023a_sd106_preservation_parity_epochs40_20260917T144824Z_v3`
Purpose: diagnostic | Outcome: FAIL | Direction: weakens (recommended; manifest carries none)
supersedes: V3-EXQ-1023 | bears_on: `zworld_actor_adequacy_locus`

## 0. Headline

The budget branch of the partition left open by `failure_autopsy_V3-EXQ-1023_2026-09-14` and
`failure_autopsy_V3-EXQ-1041_2026-09-16` is **closed** -- but not for the reason this
autopsy's first draft gave. The objective is **NON-TRANSFERRING, not exhausted**.

## 1. Facts

Dry-run gate: CLEAN. Recording: `validate_recording.py` OK, 0 always-core gaps.
substrate_hash `56a0a0dd...`, machine `ree-worker-3`, 3 seeds [42,43,44], elapsed 67360 s.
All 6 preconditions met; `gate_green` = 1.

Driver manipulation vs V3-EXQ-1023: **P0a epochs 12 -> 40 on the SD-106 track alone**
(1320/1320/1160 optimiser steps against a shipped reference of 396/396/348, ~3.3x).
The OFF arm stays at 12 by design.

| criterion | load-bearing | threshold | measured | result |
|---|---|---|---|---|
| C1 SD-106 consumer agreement >= 0.85 | YES | 2 of 3 seeds | **0 of 3** | FAIL |
| C2 preservation head used / not used | no | 2 | 2 | PASS (cannot vary) |
| C3 P0a step floor | no | 1000 | 1160 | PASS (dominated -- see 4) |

Consumer `oracle_action_agreement` at `zworld_sd106__mlp128`: 0.7542 / 0.7356 / 0.6921,
mean **0.7273**, against the 0.85 bar. The task-agnostic PCA-32 anchor clears the SAME bar at
the SAME width on **3 of 3** seeds (0.8771 / 0.8578 / 0.8702) -- the bar is demonstrably
achievable.

**Which criterion failed:** the absolute acceptance criterion, C1 -- and C1 is the only
informative one.

## 2. The budget branch -- corrected argument

The first draft said "more budget did NOT move the DV up". **That is false and is withdrawn.**
Recomputed from both manifests:

| seed | 1023 (12 ep) | 1023a (40 ep) | delta |
|---|---|---|---|
| 42 | 0.7398 | 0.7542 | **+0.0144** |
| 43 | 0.7191 | 0.7356 | **+0.0165** |
| 44 | 0.6987 | 0.6921 | -0.0066 |
| **mean** | 0.7192 | 0.7273 | **+0.0081** |

The mean ROSE and 2 of 3 seeds rose. Only the minimum fell, by -0.0066 -- which is **smaller
than the measured null wobble** (section 3) and must not be reported as a direction at all.

**The closure argument is a TRANSFER RATE, not no-movement.** 3.3x the optimiser steps bought
+0.0081 of consumer agreement against a 0.1227 mean shortfall to the bar -- about **6.6% of the
gap per 3.3x steps**. Closing it by budget alone is implausible by roughly two orders of
magnitude of compute.

## 3. The mechanism: trained hard, did not transfer

Recomputed on the upstream objective, same arm, same seeds:

| seed | `sd106_preservation_holdout_r2` 1023 | 1023a | delta |
|---|---|---|---|
| 42 | 0.7490 | 0.8601 | +0.1111 |
| 43 | 0.7464 | 0.8540 | +0.1076 |
| 44 | 0.6999 | 0.8363 | +0.1365 |
| **mean** | 0.7318 | 0.8501 | **+0.1184** |

The budget knob moved the **objective by +0.1184 R^2** and the **consumer DV by +0.0081** --
an observed transfer slope of **0.068 agreement per unit R^2** against V3-EXQ-1041's
PCA-anchored interpolation of **3.4655**: a **~50x shortfall**.

And the head has **not saturated**: 1041 recorded `sgd_head_r2` medians 0.746 / 0.806 / 0.854
at 12 / 20 / 40 epochs and states explicitly it is "still rising". 1023a confirms that from a
different instrument.

**So "the budget lever is exhausted" is false. The lever is not spent; it is not connected.**
Those are different findings with different successors, and only the second is supported.

### Cross-run confound, bounded by the run's own cells

The DRIVER manipulation is budget-only; the CROSS-RUN contrast is not. It additionally crosses
substrate `fe63dd68` -> `72befccd` (1851 insertions across 9 files incl. `ree_core/agent.py`,
`causal_grid_world.py`, `hippocampal/module.py`) and machine `ree-cloud-2` -> `ree-worker-3`.

It is near-inert, and the cells bound it: `zworld_off__*` max |delta| over all 15 cells is
**0.000000** and `rawfield_ceiling` is bit-identical -- rollouts, labels, the decoder ladder and
the OFF z_world path are demonstrably unaffected.

**And it supplies the noise floor the draft said was missing:** the PCA-32 anchor (untouchable
by an epochs knob by construction) moved on **9 of 15 cells, max |delta| 0.0098**. That exceeds
the -0.0066 seed-44 drop. Likely locus: the PCA eigendecomposition under a different host's
BLAS, not a substrate semantic change.

## 4. Instrument notes

- **C3 is BIT-IDENTICALLY DOMINATED by precondition 6.** Both are computed from the same local
  variable `budget_engaged` in one function (`driver:485`, `:510`; P6 at `:511-519`, C3 at
  `:555-568`) -- identical measured 1160, identical threshold 1000, identical boolean. C3
  carries **zero** independent information.
- **C2 cannot vary** under a correctly-configured substrate: ON arms are `preservation_weight=200`,
  OFF arms `0.0`, so `measured` can only be 2.
- **C1 is NOT dominated by any precondition** -- no precondition measures the consumer DV or any
  monotone function of it. P2 measures the ANCHOR track against the same bar and is logically
  independent. So the failure stands on the one criterion that carries information.
- Count the informative criteria before reading "2 of 3 passed" as corroboration.

## 5. Pre-registered discrimination -- the run's largest yield

The manifest carries a `discrimination` block staged by the driver explicitly "so
/failure-autopsy can read the outcome as a discrimination", routing nothing itself:

| leg | predicted | observed 0.7273 is | verdict |
|---|---|---|---|
| H-transfer-amplification | 0.806 | 0.0787 away | **FALSIFIED** |
| H-which-directions | 0.719 | **0.0083 away** | **SURVIVES** |
| H-under-budgeted-p0a | "toward or past 0.85" | -- | **FALSIFIED** |

Pre-registered separation 0.087; observed is **9.5x closer** to H-which-directions. Both are
EXISTING legs on the EXISTING question `zworld_actor_adequacy_locus` -- this run opens no leg.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | tested fairly at 3.3x budget; own acceptance bar not reached |
| Biological reference | **absent** | no lit entry for generic-vs-task-relevant compression |
| Prerequisites | present | 6/6 |
| Implementation | complete AND training well | +0.1184 R^2, still climbing |
| Environment | adequate | -- |
| Measurement | adequate on C1 | C3 dominated, C2 cannot vary |
| Integration | **partially coupled -- DOMINANT LAYER** | objective trains, gain does not arrive downstream |
| Scale | 3 seeds | measured null wobble up to 0.0098 |

**Failure-location summary (GOV-FAILLOC-1): MIXED (MECHANISM + integration).** Measurement is
adequate on the load-bearing criterion and environment is adequate, but the biological reference
is ABSENT and integration is only partially coupled, so REE FAILED is unavailable.

## 7. Recording notes -- NOT gaps

- The flat manifest has no `evidence_direction`. **Neither driver ever sets it**; the run pack
  carries the writer default `unknown`. This is the standard writer path, not a defect of this
  run -- the predecessor's `mixed` was applied post-hoc by governance-20260915.
- The run's absence from `claim_evidence.v1.json` is a **TIMING artifact**: that snapshot was
  generated 2026-09-17T13:34:42Z, **1h13m before** the manifest's 14:48:24Z stamp. Not an
  indexing gap; must not be routed as one.

## 8. Two claim-record defects governance must fix

1. **SD-106's `evidence_quality_note` still OPENS with "NO EXPERIMENTAL EVIDENCE YET"** while
   its own body now carries the V3-EXQ-1023 and V3-EXQ-1041 results. The lead sentence is false.
   GOV-APPLY-1 has been flagging the unapplied V3-EXQ-1023 disposition on this claim.
2. **`live_status.evidence.from` is stamped `failure_autopsy_V3-EXQ-1043_2026-09-17`** -- an
   artifact whose `claim_ids` are `["MECH-537"]` and which does not adjudicate SD-106 at all
   (it names SD-106 only in `bears_on`, as a known limitation).

## 9. Re-derive brake

**Does not fire.** SD-106 literal count 0 (2 prior targets, neither a counting ceiling read);
direction `weakens` + category `standard` fail the first gate independently.

Recorded for a future count: routing is `lit-pull` primary with the substrate amend as
bookkeeping only, so this target does **not** owe a build and plainly does not count. Routing
`implement-substrate` as primary would have made the R3 clause-2/clause-3 release something
that had to be argued -- a second-order cost of the drafted routing that the draft did not
notice.

## 10. Step 7b / 7c

- **7b:** 0 fires. C5 `inapplicable`.
- **7c: CONTESTED.** Model `claude-opus-5` -- the SESSION model, **not** cross-model
  (`claude-fable-5-1` returned HTTP 429 monthly spend limit; re-spawned once per Step 7c).
  Same-model pass: shares the drafter's priors. Four findings, all accepted and independently
  re-verified: D1 the no-movement claim was false (section 2); D2 the run pair is not budget-only
  and the anchor supplies a noise floor (section 3); D3 the pre-registered discrimination was
  omitted (section 5); D4 the routing was wrong (section 11). The draft's precondition-dominance,
  recording/timing and claims.yaml findings were attacked and **held**.

## 11. Routing

**PRIMARY: `lit-pull`** on generic vs task-relevant / behaviourally-conditioned selective
compression, **reconciled against the EXISTING open chip `chip-20260916-sd106-compression-litpull`
-- do NOT spawn a second** (1041's own instruction).

`failure_autopsy_V3-EXQ-1041_2026-09-16` is CONFIRMED (user gate 2026-09-16T13:06:22Z) and
conditions any redesign verbatim: *"a different-mechanism redesign under a new sd_id and a new
EXQ number, once the lit-pull has grounded it."* This run's result lands on H-which-directions
-- precisely what that lit-pull was commissioned to ground.

**SECONDARY:** the SD-106 `substrate_queue` amend, severity unchanged at `degrading`,
**bookkeeping only, no build**.

`implement-substrate` as primary was drafted and **WITHDRAWN at the Step 8 gate** (user
decision 2026-09-17): its stated ground was falsified by this run's own +0.1184 R^2 and by
1041's non-saturation finding, and it would have skipped the predecessor's stated precondition.

Per-claim disposition and the `-> stamp this artifact` citation change are in the companion
`.json`. `/governance` applies them.
