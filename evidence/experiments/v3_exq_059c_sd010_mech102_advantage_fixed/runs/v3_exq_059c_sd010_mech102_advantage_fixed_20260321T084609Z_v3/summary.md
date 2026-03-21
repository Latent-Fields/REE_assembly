# V3-EXQ-059c — SD-010: MECH-102 Advantage Fixed

**Status:** PASS
**Claims:** MECH-102, SD-010
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Retests:** EXQ-059a (three fixes + redesigned C1)
**Training policy:** RANDOM  |  **Eval:** ethical vs random (episode-level contact rate)
**alpha_world:** 0.9  (SD-008)  |  **Seed:** 0

## Fixes vs EXQ-059a

1. **Label normalization**: harm_obs[12] for all harm_eval training.
2. **Sigmoid removed**: harm_eval_z_harm_head is a linear regression head.
3. **Stratified training buffer**: Equal sampling from none/approach/contact.
4. **CF contamination removed**: Median-labeled CF samples removed from training.
5. **C1 redesigned**: Episode-level contact rate (ethical < random) replaces step-level
   advantage_sig_contact > advantage_sig_none. Step-level advantage is highest in "none"
   states (early redirection) not contact — the old C1 was testing the wrong time slice.

## Results — Episode-Level Contact Rate

| Policy | Contact steps | Total steps | Contact rate |
|---|---|---|---|
| Ethical | 95 | 19697 | 0.0048 |
| Random  | 62  | 1354  | 0.0458  |
| Reduction | — | — | 0.0410 |

- **Approach advantage** (harm spread at approach): 0.015880
- **world_forward R²**: 0.9540

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contact_rate_ethical < contact_rate_random | PASS | 0.0048 < 0.0458 |
| C2: approach_adv > 0.001 (harm spread at approach) | PASS | 0.015880 |
| C3: world_forward_r2 > 0.05 | PASS | 0.9540 |
| C4: n_contact_ethical >= 10 | PASS | 95 |

Criteria met: 4/4 → **PASS**

