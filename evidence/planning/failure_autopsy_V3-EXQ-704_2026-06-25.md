# Failure Autopsy -- V3-EXQ-704 (MECH-451 finer-channel-granularity falsifier)

- generated_utc: 2026-06-25T18:53:00Z
- run_id: v3_exq_704_mech451_finer_channel_granularity_falsifier_20260625T174413Z_v3
- queue_id: V3-EXQ-704
- claim: MECH-451 (intermediate channel-granularity falsifier; candidate / substrate_conditional / v3)
- status: FAIL / evidence_direction non_contributory (self-routed `substrate_not_ready_requeue`)
- adjudication: CONFIRMED (interactive gate, user-approved)

## 1. Scope

Single-target autopsy. Considered as a possible cluster with V3-EXQ-705b (both FAIL/non_contributory,
both on the same GAP-A reef-bipartite foraging substrate + landed arithmetic envelope, both with a
committed-action-class-entropy primary DV, both attacking the MECH-439 F-dominance conversion ceiling
from different angles). **NOT a cluster:** opposite failure shapes -- 704 is an invalid-precondition
control-calibration artifact (the test could not run fairly), whereas 705b is a *fair* test that
revealed a real ceiling. Different claims (MECH-451 vs MECH-314), different routing. Adjudicated
separately.

## 2. Facts (no interpretation)

The experiment is the EXP-0391 validation falsifier for the MECH-451 finer-channel substrate built
2026-06-24. 4 arms x 6 seeds, settling W_lat OFF on all arms (isolates channel granularity), landed
arithmetic envelope (demotion + 689e adaptive floor + 689g go_nogo + 569i top-k) as a matched constant:

- A0_ENVELOPE_ONLY
- A1_GLOBAL_WCHAN (the ARC-108 single global weight; the collapse-to-blend ablation, sits in the C1 bar)
- A2_FINER_CHANNELS (`use_finer_channel_gating`; the MECH-451 finer per-named-channel weights)
- ARM_NOISE (same-layer finer-gating null: frozen magnitude-matched random `w_chan_finer`, eta=0)

Pre-registered load-bearing criterion C1 = A2 strict-above A0 AND A1 AND ARM_NOISE on committed-class entropy.

**Observed:** C1 failed; C2 (lift grows over training) failed. **But the decisive fact is a readiness
precondition failure.** Of the 7 preconditions, 6 met; one failed:

| precondition | measured | threshold | met |
|---|---|---|---|
| enough_divergent_seeds | 3.0 | 3.0 | yes |
| finer_channels_dissociable (A2 w_chan_finer range) | 0.00148 | 0.0001 | yes (barely, ~15x floor) |
| delta_t_carries_variance | 0.00050 | 0.0001 | yes (barely) |
| learned_weights_moved_from_init | 0.00135 | 0.0001 | yes (barely) |
| matched_noise_control_verified_lifting | 2.0 | 2.0 | yes |
| **fcg_noise_magnitude_matched (ratio ARM_NOISE range / A2 learned range)** | **176.9** | **[0.25, 4.0]** | **NO** |
| candidate_pool_divergent_focus_arms | 0.0343 | 0.05 | (per-seed divergence gate passed via enough_divergent_seeds) |

`criteria_non_degenerate.preconditions_met = false` (driven by `fcg_noise_magnitude_matched`).
`metrics.json` is empty (`values: {}`); the `interpretation` block is the source of truth.

## 3. Claim-layer mapping

MECH-451 asks whether the MECH-439 F-dominance conversion ceiling is *representational compression*
(finer channels convert non-motor influence to committed action) rather than a need for full per-loop
competition (ARC-110). Its `what_would_answer` explicitly routes: SUPPORTS if A2 lifts beyond A1;
WEAKENED / route-to-ARC-110 if finer channels move weights but produce no lift; **NON-DEGENERACY:** the
finer channels must carry dissociable variance and the pool must be divergent, else
`substrate_not_ready_requeue`.

**The claim was not tested under conditions where it could express itself.** The C1 bar requires "A2
strict-above ARM_NOISE", but ARM_NOISE's frozen-random `w_chan_finer` came in ~177x larger than the
A2 *learned* range. A null 177x out of band makes the strict-above-noise comparison meaningless (and a
177x-magnitude perturbation at the gating layer is not a "null" -- it dominates behaviour). The "A2
weights-move-but-no-lift -> ARC-110" disposition is equally unreachable: a broken noise control cannot
establish that finer channels move-without-lifting. **MECH-451 is unweakened either way.**

## 4. Biological-reference triage

Closest reference: parallel, segregated cortico-basal-ganglia channels (Alexander/DeLong/Strick) and the
distinct control functions MECH-451 names (OFC devaluation, dACC conflict, lateral-PFC rule evidence,
vigour, liking). These are an existence proof for the *class* (separable control channels exist in real
brains). So a fair re-test is warranted; there is no biological basis to read this FAIL as a
falsification. Biological reference: **clear**. This run says nothing about the biology -- it is a
measurement/control-calibration artifact.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | not tested under expressible conditions (broken null) |
| Biological reference | clear | segregated channels are an existence proof for the class |
| Dependency / prerequisites | present | ARC-108 learner present; substrate built 2026-06-24 |
| Implementation completeness | complete | finer-channel substrate built + 12 contracts |
| Environment adequacy | adequate | GAP-A reef-bipartite foraging, divergent seeds met (3/3) |
| Measurement / control adequacy | **mis-calibrated** | ARM_NOISE magnitude 176.9x the learned range -> null is not a null |
| Integration adequacy | n/a | single-substrate slice |
| Scale / capacity | weak signal | A2 dissociation only ~15x floor (see Step 7 flag) |

**Dominant diagnosis:** invalid-precondition control-calibration artifact -- the V3-EXQ-642
invalid-precondition family. The manifest's own precondition names the remedy: re-tune `FCG_NOISE_SCALE`
("the legitimate ONE-time re-tune knob ... at the correct layer").

**Root cause of the blow-up:** A2's learned finer channels barely dissociated (range 0.00148, ~15x the
0.0001 floor). `FCG_NOISE_SCALE` was sized to a *presumed* learned magnitude that never materialised, so
a fixed-scale null overwhelmed the tiny real structure by 177x.

## 6. Learning extracted

1. Magnitude-matched null scales that are set as a fixed absolute (or to a presumed learned range) are
   fragile when the learned structure comes in much smaller than the design anticipated. The match should
   be computed *relative to the realised* A2 learned range per (arm, seed), not a presumed one.
2. The A2 finer-channel dissociation is **weak** (range 0.00148, delta_t std 0.00050, w_chan moved
   0.00135 -- all barely clearing floors). Even with a re-tuned null, the finer channels are close to
   "the compressed blend re-labelled" (the exact near-vacuity the dissociability gate warns about). 704b
   must watch for *substantive* dissociable variance, not just floor-clearing, or MECH-451's compression
   hypothesis faces a near-vacuous test.

## 7. Routing (user-confirmed)

- **/queue-experiment V3-EXQ-704b** (LETTER iteration; scientific question unchanged, implementation
  control was mis-calibrated): re-tune `FCG_NOISE_SCALE` so ARM_NOISE's frozen-random `w_chan_finer`
  range lands within `[0.25, 4.0]x` the realised A2 learned range (compute the match against the measured
  per-(arm,seed) learned range, not a presumed magnitude). Config-only; substrate already built.
- **recommended_substrate_queue_entry: action=none** (substrate built 2026-06-24; no gap).
- **Re-derive brake: NOT fired** -- this is the *first* failure-autopsy on MECH-451.
- Secondary instruction for 704b: strengthen / watch the dissociability readiness so a near-vacuous
  finer-channel decomposition self-routes rather than producing a misleading no-lift.

## 8. Recommended governance writes (autopsy does NOT apply these)

- evidence_direction: `non_contributory` (already self-routed; SOUND -- no correction).
- `non_degenerate_per_claim` / preconditions_met: false (already in manifest; correct).
- MECH-451: no status change; stays candidate / substrate_conditional / v3.
- Draft `evidence_quality_note` (governance to write):
  "V3-EXQ-704 (EXP-0391 MECH-451 validation falsifier) self-routed substrate_not_ready_requeue /
  non_contributory: the ARM_NOISE same-layer null was 176.9x the A2 learned w_chan_finer range
  (precondition fcg_noise_magnitude_matched [0.25,4.0] FAILED), so the C1 strict-above-noise bar was
  meaningless and MECH-451 could not be tested in either direction. V3-EXQ-642 invalid-precondition
  family (control-calibration artifact), NOT a ceiling and NOT a falsification. MECH-451 unweakened.
  Re-derive brake not fired (1st MECH-451 autopsy). Route: V3-EXQ-704b re-tuning FCG_NOISE_SCALE relative
  to the realised learned range; watch the (weak, ~15x-floor) finer-channel dissociation for near-vacuity."
