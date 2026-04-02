# V3-EXQ-187a -- MECH-153 Supervised Context-Labeling Validation

**Status:** FAIL
**Claims:** MECH-153, ARC-042
**Seeds:** [42, 7, 11]
**Baseline:** EXQ-181b (cosine_sim=0.9999 without supervised training)

## Context

EXQ-181b demonstrated that E1 ContextMemory trained only via the world-model
prediction objective does NOT produce differentiated cue representations
(cosine_sim=0.9999 between hazard-proximate and hazard-distal contexts, 0/3 seeds).
MECH-153 claims a supervised context-labeling objective is required. This experiment
adds terrain_loss (supervised hazard-field label, lambda=0.1) to E1
training and re-runs the EXQ-181b diagnostic on extract_cue_context() outputs.

## Design

**Phase 0 (warmup):** 150 episodes x 200 steps. REEAgent training
with sd016_enabled=True: E1 prediction loss + E2 loss + lambda_terrain * terrain_loss.
terrain_loss = MSE(terrain_weight, targets) where targets derived from
hazard_field_view.max() (proxy-field-aware thresholds: >0.5 -> w_harm=0.8, else 0.2;
<0.35 -> w_goal=0.8, else 0.3).

**Phase 1 (collection):** 100 episodes x 200 steps. Random actions.
Collect extract_cue_context() outputs in Context A (max > 0.7) and Context B (< 0.33).

**Phase 2 (metrics):** C1 = cosine_sim of cue_context < 0.85. C2 = w_harm accuracy > 0.70.
C3 = ridge R^2 of cue_context -> harm > 0.3.

## Key Results

| Metric | Value | Threshold | EXQ-181b baseline |
|---|---|---|---|
| cosine_sim(cue_A, cue_B) | 1.0000 | < 0.85 | 0.9999 |
| w_harm accuracy | 0.4056 | > 0.70 | N/A |
| harm_r2 (cue -> harm) | -0.0182 | > 0.3 | 0.23 |
| n_context_A steps (total) | 2082 | -- | -- |
| n_context_B steps (total) | 1422 | -- | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: cosine_sim < 0.85 | FAIL | 0/3 |
| C2: w_harm accuracy > 0.70 | FAIL | 0/3 |
| C3: harm_r2 > 0.3 | FAIL | 0/3 |

PASS rule: all three criteria pass in >= 2/3 seeds -> PASS. 1-2 criteria -> MIXED. 0 -> FAIL. **FAIL**

## Interpretation

C1 FAIL: cosine_sim=1.0000 >= 0.85 (passed 0/3 seeds). Supervised training did NOT produce sufficient differentiation. ContextMemory may need architectural changes or stronger training signal.

C2 FAIL: w_harm_accuracy=0.4056 <= 0.70 (passed 0/3 seeds). terrain_weight does NOT reliably distinguish context types.

C3 FAIL: harm_r2=-0.0182 <= 0.3 (passed 0/3 seeds). Cue context does NOT reliably encode harm information.

## Per-Seed Results

  seed=42: n_A=678 n_B=441 cos_sim=1.0 w_harm_acc=0.3941 harm_r2=-0.0200 C1=FAIL C2=FAIL C3=FAIL
  seed=7: n_A=710 n_B=488 cos_sim=1.0 w_harm_acc=0.4073 harm_r2=-0.0228 C1=FAIL C2=FAIL C3=FAIL
  seed=11: n_A=694 n_B=493 cos_sim=1.0 w_harm_acc=0.4153 harm_r2=-0.0117 C1=FAIL C2=FAIL C3=FAIL
