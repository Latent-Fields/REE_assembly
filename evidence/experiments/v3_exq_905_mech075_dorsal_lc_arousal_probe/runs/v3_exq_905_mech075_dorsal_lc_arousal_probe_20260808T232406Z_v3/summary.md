# V3-EXQ-905 -- MECH-075 DORSAL LEG: LC-Arousal Attractor-Basin Probe

**Status:** FAIL  **Label:** dorsal_lc_arousal_no_attractor_widening
**Claim:** MECH-075 (dorsal leg only; ventral/VTA leg is a sibling script)
**Seeds:** [42, 7, 123]
**Conditions:** LC_AROUSAL_GATED vs LC_AROUSAL_ABLATED
**Warmup:** 150 eps x 200 steps  **Eval:** 50 eps x 200 steps
**LC gain:** 2.0  **LC EMA alpha:** 0.1

## P0 Readiness Gate

| Check | Measured | Floor | Met |
|---|---|---|---|
| lc_arousal_signal_magnitude_supra_floor | 0.00428212 | 0.001 | True |

P0 raw mean novelty (pre-EMA, reduction=sum): 0.00848684

## Per-Seed Results

| Seed | GATED arousal_ema | GATED basin_width | ABLATED basin_width | gap | C1 | C2 |
|---|---|---|---|---|---|---|
| 42 | 0.002196 | 0.013385 | 0.013385 | -0.000000 | PASS | FAIL |
| 7 | 0.002726 | 0.015191 | 0.015191 | +0.000000 | PASS | FAIL |
| 123 | 0.002851 | 0.014451 | 0.014450 | +0.000000 | PASS | FAIL |

## PASS Criteria

| Criterion | Threshold | Result |
|---|---|---|
| C1: mean_arousal_ema_gated > 0.001 (>= 2/3 seeds) | manipulation check | PASS |
| C2 (load-bearing): basin_width_gap >= 15% relative (>= 2/3 seeds) | behavioral | FAIL |

## Interpretation

MECH-075 DORSAL LEG FALSIFIED: signal cleared the detection floor and was correctly LC-targeted (P0+C1 met) but produced no measurable widening of dorsal attractor dynamics. This is the FIRST result actually falsifying the dorsal leg -- all three prior FAILs (EXQ-192a/209/230) failed on the precondition itself and were uninformative about the mechanism.

## Failure Notes

- C2 FAIL: per-seed basin_width gap [-0.0, 0.0, 0.0] does not clear 15% relative floor in >= 2/3 seeds -- LC-arousal signal is active and correctly targeted (P0+C1 met) but does not widen hippocampal attractor basin width. This IS the first result actually falsifying the dorsal leg (all three prior FAILs failed on the precondition itself).
