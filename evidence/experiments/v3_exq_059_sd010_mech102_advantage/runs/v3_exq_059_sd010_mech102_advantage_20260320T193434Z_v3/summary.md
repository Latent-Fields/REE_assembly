# V3-EXQ-059 — SD-010: MECH-102 Advantage Signal

**Status:** FAIL
**Claims:** MECH-102, SD-010
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Retests:** EXQ-045 (advantage_sig threshold 0.001)
**Training policy:** RANDOM  |  **Eval policy:** ETHICAL (argmin harm_eval_z_harm(harm_enc(harm_bridge(E2(z,a)))))
**alpha_world:** 0.9  (SD-008)  |  **Seed:** 0

## Context

EXQ-045 FAILED: advantage_sig not meaningful at hazard contact. Root cause: z_world
harm_eval was contaminated by world-model correlates — ethical policy was optimising
against noise rather than true hazard proximity.

SD-010 fix: ethical policy now uses a clean harm signal. Pipeline:
  1. E2.world_forward(z_world, a) → z_world_cf
  2. harm_bridge(z_world_cf) → harm_obs_approx
  3. harm_enc(harm_obs_approx) → z_harm_cf
  4. harm_eval_z_harm(z_harm_cf) → harm scalar

MECH-102 prediction: advantage_sig escalates with proximity energy.
advantage_sig = mean_cf_harm - harm_actual = how much harm the ethical agent spared.

## Results — Ethical Advantage Ladder (SD-010)

| State Energy Level | advantage_sig | n steps |
|---|---|---|
| none (safe locomotion)    | 0.015947 | 28421 |
| hazard_approach (medium)  | 0.010781 | 380 |
| contact (high — combined) | 0.010547 | 27 |

- **world_forward R²**: 0.9470

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: advantage_sig_contact > advantage_sig_none | FAIL | 0.010547 vs 0.015947 |
| C2: advantage_sig_contact > 0.001 | PASS | 0.010547 |
| C3: world_forward_r2 > 0.05 | PASS | 0.9470 |
| C4: n_contact >= 50 | FAIL | 27 |

Criteria met: 2/4 → **FAIL**

## Failure Notes

- C1 FAIL: advantage_sig_contact=0.010547 <= advantage_sig_none=0.015947. Ethical z_harm policy not advantageous near hazards vs safe regions.
- C4 FAIL: n_contact=27 < 50
