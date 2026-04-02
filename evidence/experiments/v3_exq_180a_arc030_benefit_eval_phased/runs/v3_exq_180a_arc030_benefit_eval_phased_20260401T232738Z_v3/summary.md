# V3-EXQ-180a -- Resource Proximity benefit_eval_head with Phased Training

**Status:** FAIL
**Claims:** ARC-030
**Seeds:** [42, 7, 11]
**Supersedes:** V3-EXQ-180

## Context

EXQ-180 showed probe_r2=0.619 (z_world DOES encode resource proximity, C1 PASS) but benefit_ratio=0.29x (C3 FAIL). Root cause: joint training -- benefit_eval_head chased moving z_world during E1 convergence. Fix: phased training.

## Design (Phased Training Protocol)

**Phase 0 (200 eps):** E1+E2 warmup ONLY. No benefit_eval training. Let z_world converge.

**Phase 1 (100 eps):** Freeze E1+E2. Train benefit_eval_head on z_world.detach() with MSE on resource_field_view.max() (continuous proximity). Also fit linear probe for R^2 diagnostic.

**Phase 2 (200 eps):** Eval with benefit_eval_enabled=True in E3 trajectory scoring. BENEFIT_EVAL_ON vs BENEFIT_EVAL_OFF (random).

**Config:** alpha_world=0.9, benefit_weight=1.0, num_hazards=4, num_resources=3, use_proxy_fields=True

## Key Results

| Metric | Value | Threshold |
|---|---|---|
| probe_r2 (linear) | 0.4467 | > 0.3 |
| benefit_head_r (eval) | -0.1026 | > 0.3 |
| head_r_p1 (training) | -0.0937 | -- (diagnostic) |
| benefit_ratio | 0.37x | > 1.0 |
| benefit_on | 0.160 | -- |
| benefit_off | 0.433 | -- |
| final_benefit_loss | 0.117820 | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: probe_r2 > 0.3 | PASS | 3/3 |
| C2: benefit_head_r > 0.3 | FAIL | 0/3 |
| C3: benefit_ratio > 1.0 | FAIL | 0/3 |

PASS rule: all three criteria pass in >= 2/3 seeds -> **FAIL**

## Interpretation

C1 PASS: probe_r2=0.4467 (> 0.3) (3/3 seeds). z_world DOES encode resource proximity.

C2 FAIL: benefit_head_r=-0.1026 (<= 0.3) (0/3 seeds). Signal exists in z_world but head did not learn it. Check lr, n_p1_samples, or head capacity.

C3 FAIL: benefit_ratio=0.37x (<= 1.0) (0/3 seeds). Expected -- head not tracking proximity.

## Per-Seed Results

  seed=42: probe_r2=0.4861 head_r=-0.1598 head_r_p1=-0.0941 on=0.165 off=0.515 ratio=0.32x loss=0.093947 C1=PASS C2=FAIL C3=FAIL
  seed=7: probe_r2=0.3356 head_r=-0.0551 head_r_p1=-0.0876 on=0.165 off=0.335 ratio=0.49x loss=0.150999 C1=PASS C2=FAIL C3=FAIL
  seed=11: probe_r2=0.5184 head_r=-0.0930 head_r_p1=-0.0993 on=0.150 off=0.450 ratio=0.33x loss=0.108516 C1=PASS C2=FAIL C3=FAIL
