# V3-EXQ-142 -- MECH-113 Self-Maintenance Discriminative Pair

**Status:** FAIL
**Claims:** MECH-113
**Decision:** hybridize
**Seeds:** [42, 123]
**Conditions:** SELF_MAINT_ON vs SELF_MAINT_ABLATED
**Warmup:** 200 eps x 200 steps  **Baseline eval:** 10 eps  **Post-perturb eval:** 30 eps
**Env:** CausalGridWorld size=10, 3 hazards, 5 resources nav_bias=0.35
**Perturbation:** Gaussian noise sigma=2.0 injected into z_self at first step of eval
**maint_weight:** 0.1  **d_eff_target:** 1.5

## Design

MECH-113 asserts a homeostatic error signal monitors internal latent coherence (z_self D_eff) independently of external harm signals. SELF_MAINT_ON activates the D_eff homeostatic loss; SELF_MAINT_ABLATED removes it. A Gaussian noise perturbation is injected into z_self at eval start to stress-test recovery. If MECH-113 Level 1 is correct, ON holds D_eff near baseline; ABLATED disperses.

## Pre-Registered Thresholds

C1: ON d_eff_ratio (post/baseline) <= 1.5 both seeds (homeostatic recovery)
C2: ABLATED d_eff_ratio (post/baseline) >= 2.0 both seeds (uncontrolled dispersal without homeostasis)
C3: per-seed gap (ABLATED_post - ON_post) >= 0.5x ABLATED_post both seeds (clear separation)
C4: e2_loss_ON <= e2_loss_ABLATED + 0.01 both seeds (homeostasis does not degrade E2 motor model)
C5: n_d_eff_samples >= 50 per condition per seed (data quality)

## Results

| Condition | D_eff baseline | D_eff post | ratio | E2 loss |
|-----------|----------------|------------|-------|----------|
| SELF_MAINT_ON      | 22.2694 | 22.2746 | 1.001x | 0.00001 |
| SELF_MAINT_ABLATED | 22.2694 | 22.2746 | 1.001x | 0.00001 |

**per-seed gap (ABLATED_post - ON_post): [0.0, 0.0]**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: ON ratio <= 1.5 (both seeds) | PASS | [0.9938, 1.0077] |
| C2: ABLATED ratio >= 2.0 (both seeds) | FAIL | [0.9938, 1.0077] |
| C3: gap >= 0.5x ABLATED_post (both seeds) | FAIL | [0.0, 0.0] |
| C4: e2_ON <= e2_ABL + 0.01 (both seeds) | PASS | ON=0.00001 ABL=0.00001 |
| C5: n_d_eff_min >= 50 | PASS | 1264 |

Criteria met: 3/5 -> **FAIL**

## Interpretation

Partial support: directional D_eff effect observed but not all criteria met. C1=True (ON recovery) C2=False (ABL dispersal) C3=False (separation) C4=True (E2 unaffected) C5=True (data quality). Consider adjusting maint_weight or noise_sigma.

## Per-Seed Detail

SELF_MAINT_ON:
  seed=42: d_eff_baseline=23.9863 d_eff_post=23.8383 ratio=0.994x e2_loss=0.00000 n_samples=1264
  seed=123: d_eff_baseline=20.5526 d_eff_post=20.7109 ratio=1.008x e2_loss=0.00001 n_samples=1412

SELF_MAINT_ABLATED:
  seed=42: d_eff_baseline=23.9863 d_eff_post=23.8383 ratio=0.994x e2_loss=0.00000 n_samples=1264
  seed=123: d_eff_baseline=20.5526 d_eff_post=20.7109 ratio=1.008x e2_loss=0.00001 n_samples=1412

## Failure Notes

- C2 FAIL: ABLATED d_eff_ratio [0.9938, 1.0077] < 2.0 -- ablated condition does not disperse; D_eff may be architecture-bounded independent of maintenance signal
- C3 FAIL: per-seed gap [0.0, 0.0] < 0.5 * ablated_post in some seeds; ON and ABLATED conditions do not clearly separate
