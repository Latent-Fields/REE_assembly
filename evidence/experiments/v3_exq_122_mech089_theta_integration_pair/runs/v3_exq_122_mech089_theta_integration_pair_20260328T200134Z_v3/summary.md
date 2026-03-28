# V3-EXQ-122 -- MECH-089 Theta-Gamma Integration Discriminative Pair

**Status:** FAIL
**Claim:** MECH-089
**Proposal:** EXP-0020 / EVB-0016
**Seeds:** [42]
**theta_k:** 2  (E3 ticks every 2 steps; same rate in both conditions)
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 50 eps
**env_drift_prob:** 0.3  **env_drift_interval:** 3

## Design

THETA_INTEGRATION_ON: E3 receives ThetaBuffer.summary() = mean of last 2 z_world frames at each E3 tick.
THETA_INTEGRATION_ABLATED: E3 receives raw most-recent z_world frame at each E3 tick. Same E3 update rate (every 2 steps). Only the content differs.

Redesign rationale (vs EXQ-066): theta_k=4 degraded E3 performance (batched error 2.28x worse than raw). Redesign uses theta_k=2 (shorter window) and measures harm AUC rather than prediction error variance for a cleaner discriminative outcome.

## Pre-Registered Thresholds

C1: harm_auc_ON - harm_auc_ABLATED >= 0.05  (relative advantage)
C2: harm_auc_ON >= 0.6  (absolute harm prediction learning)
C3: harm_auc_ON > harm_auc_ABLATED for ALL seeds  (consistency)
C4: min_harm_steps >= 20  (data quality)
C5 (diagnostic): mean_within_batch_var >= 1e-05  (buffer non-trivial)

## Aggregate Results

| Metric | THETA_ON | THETA_ABLATED | Delta | Pass |
|--------|----------|---------------|-------|------|
| harm_AUC (C1 delta) | 0.4896 | 0.6250 | -0.1354 | NO |
| harm_AUC >= 0.6 (C2) | 0.4896 | -- | -- | NO |
| seed consistency (C3) | [False] | -- | -- | NO |
| min_harm_steps (C4) | 32 | -- | -- | YES |
| mean_batch_var (C5 diag) | 0.000034 | -- | -- | YES |

## Interpretation

MECH-089 NOT SUPPORTED at theta_k=2 operationalisation. harm_auc_ON=0.4896, harm_auc_ABLATED=0.6250, delta=-0.1354. Theta-cycle averaging of E1 z_world output did not improve E3 harm prediction AUC over raw same-rate z_world delivery. Consistent with EXQ-066 backwards result (k=4 degraded performance): the environment may change meaningfully every step, making any averaging (even at k=2) destroy temporal resolution E3 relies on.

## Per-Seed (THETA_INTEGRATION_ON)

  seed=42: harm_auc=0.4896 harm_rate=0.7111 harm_steps_eval=32 n_e3_ticks=22 mean_batch_var=0.000034 train_harm_steps=34

## Per-Seed (THETA_INTEGRATION_ABLATED)

  seed=42: harm_auc=0.6250 harm_rate=0.7111 harm_steps_eval=32 n_e3_ticks=22 train_harm_steps=34

## Failure Notes

- C1 FAIL: harm_auc_ON=0.4896 vs harm_auc_ABLATED=0.6250 (delta=-0.1354, needs >=0.05). Theta-averaging (k=2) did not improve harm AUC over raw same-rate sampling. Possible causes: (1) theta_k=2 still too coarse for CausalGridWorldV2 dynamics, (2) harm_buf training signal too sparse at this hazard density, (3) E3 harm_eval learns equally well from raw or averaged z_world at world_dim=32.
- C2 FAIL: harm_auc_ON=0.4896 (needs >=0.6). ON condition did not achieve reliable harm prediction. Check harm_buf_pos_final -- insufficient positive samples.
- C3 FAIL: per_seed direction inconsistent ([False]). ON did not consistently beat ABLATED across seeds.
