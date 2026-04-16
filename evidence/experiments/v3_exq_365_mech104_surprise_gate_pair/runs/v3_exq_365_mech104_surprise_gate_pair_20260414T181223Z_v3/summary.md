# V3-EXQ-365 -- MECH-104: Surprise Gate Discriminative Pair (5-seed)

**Status:** PASS
**Claim:** MECH-104 -- unexpected harm events spike commitment uncertainty (LC-NE analog)
**Design:** Matched discriminative pair per seed (VOLATILITY_ON vs VOLATILITY_OFF ablation)
**P0:** 50 eps warmup | **P1:** 150 eps world-forward | **Eval:** 50 eps | **Seeds:** [42, 7, 13, 99, 21]

## Mechanism Under Test

Harm events cause large world-forward prediction error -> _running_variance spikes
via EMA update (alpha * error_var). Ablation: set _ema_alpha=0.0 freezes variance.
Paired comparison per step: harm transitions vs non-harm transitions.
Transition labeling: harm_prev (from action that produced z_world_curr).

## Pre-registered Thresholds

| Criterion | Threshold | Seed requirement |
|-----------|-----------|-----------------|
| C1: spike_contrast (harm-nonharm) | > 0.0 | >= 4/5 seeds |
| C2: OFF harm spike frozen | < 1e-10 | ALL 5 seeds |
| C3: pairwise_delta (ON-OFF) | > 0.0 | >= 4/5 seeds |
| C4: n_harm_steps | >= 1 | ALL 5 seeds |

## Results by Seed

| Seed | post-train rv | ON harm spike | ON nonharm spike | ON contrast | OFF harm spike | Pairwise delta | Decommits (ON) |
|------|-------------|-------------|----------------|-------------|--------------|---------------|---------------|
| 42 | 0.0000019 | 0.00000205 | -0.00000005 | 0.00000210 | 0.00e+00 | 0.00000205 | 0 |
| 7 | 0.0000010 | 0.00000184 | -0.00000004 | 0.00000188 | 0.00e+00 | 0.00000184 | 0 |
| 13 | 0.0000010 | 0.00000157 | -0.00000004 | 0.00000162 | 0.00e+00 | 0.00000157 | 0 |
| 99 | 0.0000017 | 0.00000244 | -0.00000006 | 0.00000251 | 0.00e+00 | 0.00000244 | 0 |
| 21 | 0.0000010 | 0.00000182 | -0.00000004 | 0.00000185 | 0.00e+00 | 0.00000182 | 0 |

## PASS Criteria

| Criterion | Seeds passing | Required | Result |
|-----------|------------|---------|--------|
| C1 spike_contrast > 0.0 | 5/5 | >=4 | PASS |
| C2 OFF harm spike frozen | 5/5 | ==5 | PASS |
| C3 pairwise_delta > 0.0 | 5/5 | >=4 | PASS |
| C4 n_harm_steps >= 1 | 5/5 | ==5 | PASS |

Criteria met: 4/4 -> **PASS**

