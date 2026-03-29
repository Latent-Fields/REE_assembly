# Targeted Literature Review: MECH-071
## E2/E3 Harm Evaluation Calibration and Approach Gradient

**Claim ID:** MECH-071
**Claim subject:** e3.harm_eval_calibration_gradient_asymmetry
**Claim statement:** E2 harm prediction is better calibrated for agent-caused vs environment-caused transitions; E3 learns a graded danger model from z_world (approach gradient, not just contact).
**Date created:** 2026-03-29
**Number of entries:** 4
**Status:** provisional, implementation_phase: v3
**Depends on:** MECH-070 (conceptual sensorium motor model), ARC-024 (harm gradients)

---

## Entries

| entry_id | paper | year | evidence_direction | confidence |
|----------|-------|------|--------------------|------------|
| 2026-03-29_mech_071_efference_selfproduced_blakemore1998 | Central cancellation of self-produced tickle sensation | 1998 | supports | 0.80 |
| 2026-03-29_mech_071_force_calibration_shergill2003 | Two eyes for an eye: the neuroscience of force escalation | 2003 | supports | 0.82 |
| 2026-03-29_mech_071_causal_inference_corticostriatal_dorfman2021 | Causal Inference Gates Corticostriatal Learning | 2021 | supports | 0.72 |
| 2026-03-29_mech_071_threat_imminence_gradient_mobbs2007 | When fear is near: threat imminence elicits prefrontal-periaqueductal gray shifts | 2007 | supports | 0.77 |

---

## Rationale for source selection

MECH-071 makes two separable claims that required different literature threads.

**Claim 1 -- E2 calibration asymmetry (agent-caused vs environment-caused harm):** This is the efference-copy/reafference thread. The key papers are Blakemore et al. (1998), which establishes the cerebellar forward-model mechanism for self/other sensory asymmetry (fMRI evidence), and Shergill et al. (2003), which demonstrates the behavioral consequence of this asymmetry in force calibration. Together they show that self-generated sensory events are systematically attenuated relative to externally-generated identical events -- and that this difference disappears when action-outcome prediction is not possible. Dorfman et al. (2021) adds the complementary circuit: causal beliefs gate learning in dorsal striatum, providing a neural implementation of how the brain routes prediction errors differently based on whether the agent caused the outcome.

**Claim 2 -- E3 graded danger model (approach gradient):** This is the threat imminence thread. Mobbs et al. (2007) is the definitive human fMRI paper showing graded proximity-danger encoding: vmPFC for distal threat, PAG for proximal, with a continuous gradient as a function of approach. This directly supports the claim that E3's harm model should produce graded z_harm_s activation during trajectory approach, not only at contact.

The Blakemore/Shergill papers were targeted directly from prior knowledge as foundational in this literature. Dorfman et al. was found via PubMed search on action-outcome causal attribution. Mobbs et al. was found via WebSearch on threat imminence continuum.

---

## Overall assessment

The literature strongly supports both sub-claims of MECH-071. The agent/environment calibration asymmetry is well-grounded in the efference copy literature (40+ years of evidence) and has a specific behavioral quantification in Shergill 2003. The approach-gradient claim is supported by the threat imminence framework with human neural evidence. No papers in this set weaken the claim. The principal uncertainty is the domain gap: all papers use benign (force/touch) or virtual (maze avoidance) contexts, and the extension to harm evaluation in a latent architecture is an inference that MECH-071 itself must ultimately be validated with REE experiments (EXQ series).
