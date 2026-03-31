# V3-EXQ-181b -- E1 Prior Context Discrimination (Context-B Fix)

**Status:** FAIL
**Claims:** MECH-150, ARC-041
**Supersedes:** V3-EXQ-181
**Seeds:** [42, 7, 11]

## Context

EXQ-181 failed because Context B sampling (hazard_field_view.max() < 0.1) never fired with num_hazards=4: the hazard field is ambient everywhere in a 10x10 grid with 4 sources. Fix: num_hazards=1 produces genuine spatial context separation -- cells near the single hazard (Context A) vs far from it (Context B).

## Design

**Phase 0 (warmup):** 100 episodes x 200 steps. Standard REEAgent training (E1 + E2 losses, Adam lr=1e-3, alpha_world=0.9).

**Phase 1 (collection):** 100 episodes x 200 steps. Random actions. Context A: hazard_field_view.max() > 0.7. Context B: < 0.33. (Thresholds revised from EXQ-181 0.3/0.1 for proxy-field normalised range.)

**Phase 2 (metrics):** C1 = cosine_sim(mean_prior_A, mean_prior_B) < 0.85. C2 = ridge R^2 of prior -> harm_scalar > 0.3.

## Key Results

| Metric | Value | Threshold |
|---|---|---|
| cosine_sim(mean_A, mean_B) | 0.9999 | < 0.85 |
| harm_r2 (prior -> harm) | 0.2289 | > 0.3 |
| n_context_A steps (total) | 2157 | -- |
| n_context_B steps (total) | 1356 | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: cosine_sim < 0.85 | FAIL | 0/3 |
| C2: harm_r2 > 0.3 | FAIL | 1/3 |

PASS rule: both criteria pass in >= 2/3 seeds -> **FAIL**

## Interpretation

C1 FAIL: cosine_sim=0.9999 >= 0.85 (passed 0/3 seeds). E1 priors do NOT differ between hazard-proximate and hazard-distal contexts. SD-016 cue-indexed retrieval will require supervised ContextMemory training.

C2 FAIL: harm_r2=0.2289 <= 0.3 (passed 1/3 seeds). E1 prior does NOT reliably predict harm gradient. SD-016 extract_cue_context() will need terrain_loss supervision to calibrate.

## Per-Seed Results

  seed=42: n_A=728 n_B=500 cos_sim=0.9998042583465576 harm_r2=0.2295 C1=FAIL C2=FAIL
  seed=7: n_A=575 n_B=466 cos_sim=0.9999731183052063 harm_r2=0.1211 C1=FAIL C2=FAIL
  seed=11: n_A=854 n_B=390 cos_sim=0.9999409317970276 harm_r2=0.3360 C1=FAIL C2=PASS
