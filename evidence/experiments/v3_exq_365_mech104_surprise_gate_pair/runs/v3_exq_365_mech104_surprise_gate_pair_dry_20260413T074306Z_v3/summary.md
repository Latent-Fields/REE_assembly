# V3-EXQ-365 -- MECH-104: Surprise Gate Discriminative Pair (5-seed)

**Status:** FAIL
**Claim:** MECH-104 -- unexpected harm events spike commitment uncertainty (LC-NE analog)
**Design:** Matched discriminative pair per seed (VOLATILITY_ON vs VOLATILITY_OFF ablation)
**P0:** 50 eps warmup | **P1:** 150 eps world-forward | **Eval:** 50 eps | **Seeds:** [42]

## Mechanism Under Test

Harm events cause large world-forward prediction error -> _running_variance spikes
via EMA update (alpha * error_var). Ablation: set _ema_alpha=0.0 freezes variance.
Paired comparison per step: harm transitions vs non-harm transitions.
Transition labeling: harm_prev (from action that produced z_world_curr).

## Pre-registered Thresholds

| Criterion | Threshold | Seed requirement |
|-----------|-----------|-----------------|
| C1: spike_contrast (harm-nonharm) | > 0.0 | >= 4/1 seeds |
| C2: OFF harm spike frozen | < 1e-10 | ALL 1 seeds |
| C3: pairwise_delta (ON-OFF) | > 0.0 | >= 4/1 seeds |
| C4: n_harm_steps | >= 1 | ALL 1 seeds |

## Results by Seed

| Seed | post-train rv | ON harm spike | ON nonharm spike | ON contrast | OFF harm spike | Pairwise delta | Decommits (ON) |
|------|-------------|-------------|----------------|-------------|--------------|---------------|---------------|
| 42 | 0.5000000 | -0.01864839 | -0.02291398 | 0.00426559 | 0.00e+00 | -0.01864839 | 0 |

## PASS Criteria

| Criterion | Seeds passing | Required | Result |
|-----------|------------|---------|--------|
| C1 spike_contrast > 0.0 | 1/1 | >=4 | PASS |
| C2 OFF harm spike frozen | 1/1 | ==1 | PASS |
| C3 pairwise_delta > 0.0 | 0/1 | >=4 | FAIL |
| C4 n_harm_steps >= 1 | 1/1 | ==1 | PASS |

Criteria met: 3/4 -> **FAIL**

## Failure Notes

- C3 FAIL: pairwise_delta > 0.0 in 0/1 seeds (need 4); values=['-0.0186484']
