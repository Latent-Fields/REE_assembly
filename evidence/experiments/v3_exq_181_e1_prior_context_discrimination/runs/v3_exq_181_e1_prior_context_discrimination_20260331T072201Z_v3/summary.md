# V3-EXQ-181 -- E1 Prior Context Discrimination Diagnostic

**Status:** MIXED
**Claims:** MECH-150, ARC-041
**Seeds:** [42, 7, 11]

## Context

SD-016 specifies a frontal cue-indexed integration circuit using E1's ContextMemory to produce context-specific priors feeding E2 (action bias) and E3 (terrain precision). This diagnostic tests whether the EXISTING generate_prior() interface already discriminates hazard-proximate from hazard-distal z_world contexts, before implementing the SD-016 extract_cue_context() extension.

## Design

**Phase 0 (warmup):** 100 episodes x 200 steps. Standard REEAgent training (E1 + E2 losses, Adam lr=0.001, alpha_world=0.9).

**Phase 1 (collection):** 100 episodes x 200 steps. Random actions. Each step: call agent.e1.generate_prior([z_self, z_world]) to get prior [1, world_dim]. Classify step as Context A (hazard_field_view.max() > 0.3), Context B (hazard_field_view.max() < 0.1), or ambiguous (skip).

**Phase 2 (metrics):** C1 = cosine_sim(mean_prior_A, mean_prior_B) < 0.85. C2 = ridge R^2 of prior -> harm_scalar > 0.3.

## Key Results

| Metric | Value | Threshold |
|---|---|---|
| cosine_sim(mean_A, mean_B) | N/A | < 0.85 |
| harm_r2 (prior -> harm) | 0.5292 | > 0.3 |
| n_context_A steps (total) | 4622 | -- |
| n_context_B steps (total) | 0 | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: cosine_sim < 0.85 | FAIL | 0/3 |
| C2: harm_r2 > 0.3 | PASS | 3/3 |

PASS rule: both criteria pass in >= 2/3 seeds -> **MIXED**

## Interpretation

C1 FAIL: cosine_sim=nan >= 0.85 (passed 0/3 seeds). E1 priors do NOT differ between hazard-proximate and hazard-distal contexts. SD-016 cue-indexed retrieval will require explicit training of ContextMemory.

C2 PASS: harm_r2=0.5292 > 0.3 in 3/3 seeds. E1 prior predicts harm gradient linearly -- cue context carries harm information.

## Per-Seed Results

  seed=42: n_A=1519 n_B=0 cos_sim=N/A harm_r2=0.5318 C1=FAIL C2=PASS
  seed=7: n_A=1587 n_B=0 cos_sim=N/A harm_r2=0.5615 C1=FAIL C2=PASS
  seed=11: n_A=1516 n_B=0 cos_sim=N/A harm_r2=0.4944 C1=FAIL C2=PASS
