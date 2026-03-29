# targeted_review_connectome_sd_004

**Claim:** SD-004 — Action objects as hippocampal map backbone
**Subject:** hippocampal_module.action_object_map_backbone
**Date created:** 2026-03-29
**Number of entries:** 4

## Claim summary

SD-004 states that in REE V3, the HippocampalModule navigates action-object space O rather than raw z_world latent space. Action objects are compressed action-consequence representations produced by E2; each action object encodes a structured multi-step consequence chunk. By organising the hippocampal map around action objects rather than raw states, the agent can plan over far longer effective horizons than E1's 20-step sensory prediction window allows. SD-004 co-depends on SD-005 (self/world latent split): action objects require z_world (the world-directed causal latent) as their substrate.

## Entries

| Entry ID | Paper | Evidence direction | Confidence |
|----------|-------|-------------------|------------|
| 2026-03-29_sd_004_predictive_map_stachenfeld2017 | Stachenfeld et al. (2017), Nature Neuroscience — The hippocampus as a predictive map | supports | 0.85 |
| 2026-03-29_sd_004_cognitive_map_review_behrens2018 | Behrens et al. (2018), Neuron — What Is a Cognitive Map? | supports | 0.80 |
| 2026-03-29_sd_004_theta_sequences_goals_wikenheiser2015 | Wikenheiser & Redish (2015), Nature Neuroscience — Hippocampal theta sequences reflect current goals | supports | 0.72 |
| 2026-03-29_sd_004_successor_representation_dayan1993 | Dayan (1993), Neural Computation — Improving Generalization for TD Learning: The Successor Representation | supports | 0.78 |

## Rationale for source selection

The four papers were selected to cover three distinct levels of the SD-004 claim:

1. **Theoretical foundation (Dayan 1993):** The SR is the computational principle underlying the entire SD-004 design. Understanding what the SR is, why it is efficient, and what its limitations are is prerequisite to evaluating whether the action-object extension is sound.

2. **Biological grounding (Stachenfeld et al. 2017):** The strongest direct evidence that the biological hippocampal map is organised by SR structure rather than geometric space. This is the primary paper linking computational SR theory to place/grid cell physiology, and is the most direct biological precedent for SD-004's map backbone design.

3. **Generalisation licence (Behrens et al. 2018):** The key review paper arguing that the cognitive map is not spatial but relational and domain-general. This licenses SD-004's proposal to organise the map around action-object structure rather than spatial positions.

4. **Goal-directed dynamics (Wikenheiser & Redish 2015):** Direct electrophysiological evidence that hippocampal sequential activity is prospective, goal-directed, and goal-scaled in its look-ahead distance. This grounds SD-004's requirement that HippocampalModule traversal of action-object space be goal-modulated with a dynamic planning horizon.
