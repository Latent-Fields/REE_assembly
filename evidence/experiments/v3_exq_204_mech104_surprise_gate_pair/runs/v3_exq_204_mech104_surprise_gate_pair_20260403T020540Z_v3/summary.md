# V3-EXQ-204 -- MECH-104: Volatility Interrupt Discriminative Pair

**Status:** PASS
**Claim:** MECH-104 -- unexpected harm events spike commitment uncertainty (LC-NE analog)
**Design:** Matched discriminative pair per seed (VOLATILITY_ON vs VOLATILITY_OFF ablation)
**Warmup:** 200 eps | **Eval:** 50 eps | **Seeds:** [0, 1, 2]

## Mechanism Under Test

Harm events cause large world-forward prediction error -> _running_variance spikes
via EMA update (alpha * error_var). Ablation: set _ema_alpha=0.0 freezes variance.
Paired comparison per step: harm transitions vs non-harm transitions.
Transition labeling: harm_prev (from action that produced z_world_curr).

## Pre-registered Thresholds

| Criterion | Threshold | Seed requirement |
|-----------|-----------|-----------------|
| C1: spike_contrast (harm-nonharm) | > 0.0 | >= 2/3 seeds |
| C2: OFF harm spike frozen | < 1e-10 | ALL 3 seeds |
| C3: pairwise_delta (ON-OFF) | > 0.0 | >= 2/3 seeds |
| C4: n_harm_steps | >= 1 | ALL 3 seeds |

## Results by Seed

| Seed | post-train rv | ON harm spike | ON nonharm spike | ON contrast | OFF harm spike | Pairwise delta | Decommits (ON) |
|------|-------------|-------------|----------------|-------------|--------------|---------------|---------------|
| 0 | 0.0000017 | 0.00000194 | -0.00000005 | 0.00000198 | 0.00e+00 | 0.00000194 | 0 |
| 1 | 0.0000012 | 0.00000140 | -0.00000003 | 0.00000144 | 0.00e+00 | 0.00000140 | 0 |
| 2 | 0.0000011 | 0.00000160 | -0.00000004 | 0.00000164 | 0.00e+00 | 0.00000160 | 0 |


## PASS Criteria

| Criterion | Seeds passing | Required | Result |
|-----------|------------|---------|--------|
| C1 spike_contrast > 0.0 | 3/3 | >=2 | PASS |
| C2 OFF harm spike frozen | 3/3 | ==3 | PASS |
| C3 pairwise_delta > 0.0 | 3/3 | >=2 | PASS |
| C4 n_harm_steps >= 1 | 3/3 | ==3 | PASS |

Criteria met: 4/4 -> **PASS**

