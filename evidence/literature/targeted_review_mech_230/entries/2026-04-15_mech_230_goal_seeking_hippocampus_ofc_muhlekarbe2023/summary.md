# MECH-230 Literature Entry: Muhle-Karbe et al. 2023

**Entry ID:** 2026-04-15_mech_230_goal_seeking_hippocampus_ofc_muhlekarbe2023
**Claim:** MECH-230 -- z_goal as structured positive attractor distinct from harm avoidance
**DOI:** https://doi.org/10.1016/j.neuron.2023.08.021

---

## What the paper did

Muhle-Karbe and colleagues (2023) ask a deceptively simple question: does pursuing a goal *change* how the brain represents space, or does the brain first represent space neutrally and then evaluate locations for goal relevance separately? They had human participants navigate an agent through a grid world with four interlinked rooms, seeking two successive goal locations whose dependence was signaled by contextual cues. Using fMRI and representational similarity analysis, they examined the geometry of how hippocampus and orbitofrontal cortex encoded allocentric spatial information during goal-seeking versus non-goal-seeking movement. They also built a computational model -- a joint place code for current and prospective location -- to account for the observed distortions.

## Key findings relevant to MECH-230

The central finding is that goal-seeking *compresses* hippocampal and OFC spatial codes: locations cued as goals are coded closer together in neural state space than their physical distance would predict. This is not noise or decreased precision -- it is a systematic reorganization of the representational geometry so that the goal-relevant sub-space is internally compressed. Critically, the magnitude of this compression predicted learning success, suggesting that compression is a functional property, not an epiphenomenon. The same effect appeared in both hippocampus and OFC, with a computational model (joint encoding of current and prospective location in a single place code) accounting for the data.

## REE translation

MECH-230 requires that z_goal forms a structured sub-space in E3's latent space, distinct from z_harm and measurable as z_goal_norm > 0. Muhle-Karbe et al. provide the strongest available human neural evidence that the hippocampus and OFC do exactly what MECH-230 predicts: when a location is a goal, its neural representation is drawn toward other goal representations, forming a compressed cluster -- a positive attractor in representational geometry terms. The OFC involvement is particularly relevant to REE: E3's evaluative component (which interfaces with OFC's role in outcome valuation) is precisely where goal salience should distort the terrain map. If MECH-230 is correct, we should see exactly this pattern in REE: z_goal states clustering together in E3's latent space, with the cluster norm measurably above zero when goals are active.

The joint place code model -- encoding current and prospective location simultaneously -- maps onto REE's forward model structure: E2's rollout generates a prospective trajectory, and E3 evaluates terrain relative to goal, implying that z_goal compresses the terrain map toward the goal attractor by exactly this joint encoding mechanism.

## Limitations and caveats

The paper's task uses externally cued spatial goals with no harm or punishment condition. MECH-230 specifically requires that z_goal is *distinct* from z_harm -- not just that goal representations are structured. The compression finding is silent on whether approach-goal and avoidance-harm representations would be geometrically separated or interleaved in the same sub-space. This is a genuine gap: the paper supports goal-space structure but cannot adjudicate the approach/avoidance separation half of MECH-230.

A secondary limitation is the resolution of fMRI relative to REE's discrete sub-space. Muhle-Karbe et al. measure macroscopic BOLD signals in human cortex; whether the same compression geometry characterizes REE's learned z_goal vectors requires direct measurement, not inference by analogy.

## Confidence reasoning

Confidence is set at 0.74. Source quality is excellent (Neuron, human fMRI with computational modeling, multi-voxel geometry analysis). Mapping fidelity is good for the goal-clustering aspect but partial: the approach/harm separation is not tested. The hippocampus-OFC axis is directly relevant to REE's E3 + terrain architecture. This paper provides the most direct existing evidence that goal-directed behavior reorganizes hippocampal-OFC representational geometry into the kind of compressed attractor structure that MECH-230 requires -- and that this reorganization is functionally meaningful rather than a passive byproduct of goal proximity.
