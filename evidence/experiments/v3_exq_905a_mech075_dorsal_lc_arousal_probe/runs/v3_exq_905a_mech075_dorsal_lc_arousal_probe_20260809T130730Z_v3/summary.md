# V3-EXQ-905a -- MECH-075 DORSAL LEG: LC-Arousal Attractor-Basin Probe

**Supersedes:** v3_exq_905_mech075_dorsal_lc_arousal_probe_20260808T232406Z_v3 (LC_GAIN recalibration -- 905's C2 was underpowered at LC_GAIN=2.0; see 2026-08-09 autopsy)
**Status:** FAIL  **Label:** dorsal_lc_arousal_no_attractor_widening
**Claim:** MECH-075 (dorsal leg only; ventral/VTA leg is a sibling script)
**Seeds:** [42, 7, 123]
**Conditions:** LC_AROUSAL_GATED vs LC_AROUSAL_ABLATED
**Warmup:** 150 eps x 200 steps  **Eval:** 50 eps x 200 steps
**LC gain (905a re-derived):** 80.0  **LC EMA alpha:** 0.1

## P0 Readiness Gate

| Check | Measured | Floor | Met |
|---|---|---|---|
| lc_arousal_signal_magnitude_supra_floor | 0.00429916 | 0.001 | True |

P0 raw mean novelty (pre-EMA, reduction=sum): 0.00849969

## Per-Seed Results

| Seed | GATED arousal_ema | GATED cem_scale | GATED basin_width | ABLATED basin_width | gap | C1 | C2 |
|---|---|---|---|---|---|---|---|
| 42 | 0.003014 | 1.2411 | 0.013300 | 0.013300 | -0.000000 | PASS | FAIL |
| 7 | 0.003081 | 1.2464 | 0.015131 | 0.015131 | +0.000000 | PASS | FAIL |
| 123 | 0.002852 | 1.2282 | 0.014570 | 0.014545 | +0.000026 | PASS | FAIL |

## PASS Criteria

| Criterion | Threshold | Result |
|---|---|---|
| C1: mean_arousal_ema_gated > 0.001 (>= 2/3 seeds) | manipulation check | PASS |
| C2 (load-bearing): basin_width_gap >= 15% relative (>= 2/3 seeds) | behavioral | FAIL |

## Interpretation

MECH-075 DORSAL LEG FALSIFIED: signal cleared the detection floor and was correctly LC-targeted (P0+C1 met) but produced no measurable widening of dorsal attractor dynamics. This is the FIRST result actually falsifying the dorsal leg -- all three prior FAILs (EXQ-192a/209/230) failed on the precondition itself and were uninformative about the mechanism.

## Failure Notes

- C2 FAIL: per-seed basin_width gap [-0.0, 0.0, 2.6e-05] does not clear 15% relative floor in >= 2/3 seeds -- LC-arousal signal is active and correctly targeted (P0+C1 met) but does not widen hippocampal attractor basin width. This IS the first result actually falsifying the dorsal leg (all three prior FAILs failed on the precondition itself).
