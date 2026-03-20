# V3-EXQ-045 — MECH-102: Energy Escalation Ladder (Ethical Policy + ttype Split)

**Status:** FAIL
**Claims:** MECH-102, ARC-024
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Training policy:** RANDOM  |  **Eval policy:** ETHICAL (argmin E3(E2(z, a)))
**Metric:** advantage_sig = mean_cf_harm − harm_actual
**alpha_world:** 0.9  (SD-008)  |  **Seed:** 0
**Complement:** EXQ-032b PASS (same claim, random policy)

## Design Rationale

EXQ-032b used random eval policy: causal_sig = harm_actual − mean_cf (positive at
contact because agent stepped into hazard). EXQ-045 tests the complementary case.

With ethical policy, harm_actual is the *minimum* over all actions.
advantage_sig = mean_cf − harm_actual = how much harm the ethical choice spared.

MECH-102 prediction: advantage_sig escalates with transition energy:
- none (safe): all actions harmless → advantage ≈ 0
- approach: action space starts to diverge (toward vs away from hazard) → advantage rises
- contact: maximum action-space gradient → advantage maximised

If PASS: ethical agency matters MOST when stakes are highest.
Both EXQ-032b (harm incurred) and EXQ-045 (harm avoided) confirm MECH-102.

## Results — Ethical Advantage Ladder

| State Energy Level | advantage_sig | n steps |
|---|---|---|
| none (safe locomotion)    | 0.066755 | 23554 |
| hazard_approach (medium)  | 0.049484 | 392 |
| contact (high — combined) | 0.044058 | 49 |

- **world_forward R²**: 0.9481

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: advantage_sig_contact > advantage_sig_none | FAIL | 0.044058 vs 0.066755 |
| C2: advantage_sig_approach > advantage_sig_none (gradient precedes contact) | FAIL | 0.049484 vs 0.066755 |
| C3: advantage_sig_contact > 0.001 (non-trivial advantage at contact) | PASS | 0.044058 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9481 |
| C5: n_contact >= 50 | FAIL | 49 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C1 FAIL: advantage_sig_contact=0.044058 <= advantage_sig_none=0.066755. Ethical choice doesn't save more harm at contact than at baseline.
- C2 FAIL: advantage_sig_approach=0.049484 <= advantage_sig_none=0.066755. No gradient before contact.
- C5 FAIL: n_contact=49 < 50
