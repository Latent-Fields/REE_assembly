# Shergill, Bays, Frith & Wolpert (2003) — Summary for SD-003

**Source**: Shergill, S.S., Bays, P.M., Frith, C.D., & Wolpert, D.M. (2003). Two eyes for an eye: the neuroscience of force escalation. *Science*, 301(5630), 187. DOI: [10.1126/science.1085327](https://doi.org/10.1126/science.1085327)

## What the Paper Did

This is a tightly controlled behavioral experiment from the Wolpert-Frith group demonstrating that people systematically underestimate the force of their own actions relative to externally applied force of identical magnitude. The paradigm is elegant: participants press on each other's fingers in turn, each instructed to match the force they just received. Despite these instructions, applied force escalates in a positive feedback cycle -- each participant perceives the force they themselves apply as lighter than the force they received, and therefore applies slightly more to match, which the partner then also underestimates, and so on. The paper interprets this through the forward model framework: self-generated force activates the forward model, which predicts the sensory consequence of the action and partially cancels it at the level of tactile perception, making self-applied force feel lighter. Externally applied force has no such cancellation, so it feels heavier.

## Key Findings Relevant to SD-003

The paper provides the cleanest behavioral evidence that the forward model output is not merely theoretical -- it is subtracted from sensory perception before a causal or magnitude judgment is formed. This is the behavioral signature of the mechanism SD-003 proposes: the agent's forward model (E2) is evaluated for the actual action, and its output is what gets compared against baseline to produce the causal attribution signal. In this experiment, that comparison reduces perceived force magnitude for self-produced stimuli. The forward model difference IS the self-attribution computation.

The force escalation failure mode is a particularly vivid empirical illustration of what happens when an agent cannot complete a counterfactual comparison. Each participant's forward model correctly cancels their own force in perception, but they have no counterfactual model of the partner's force -- no way to compare 'what force would have arrived if my partner had acted differently?' Without this counterfactual, the asymmetry in perceived magnitude is unavoidable, and escalation is structurally inevitable.

## Translation to REE / SD-003

The experiment demonstrates, in a behavioral laboratory setting, the exact failure mode SD-003 is designed to prevent. An REE agent without a calibrated E2 counterfactual would face an analogous asymmetry in the harm-stream: self-caused harm events would be (if anything) predicted and therefore partially discounted in the agent's internal representation, while externally caused harm events would arrive unpredicted and feel larger. Without the explicit counterfactual comparison -- causal_sig = E2(z_t, a_actual) - E2(z_t, a_cf) -- the agent would systematically misattribute its own harm footprint as smaller than it actually is.

The force escalation dynamic is also relevant to MECH-102 (violence as terminal error-correction). Shergill 2003 provides the mechanistic substrate for one route to escalating harm cycles: forward model miscalibration that makes self-caused harm appear smaller than other-caused harm, creating a persistent grievance asymmetry that drives escalation even among agents who intend to match, not exceed.

## Limitations and Caveats

The paper demonstrates the single-pass forward model cancellation (E2(a_actual) subtracted from perception), not SD-003's two-pass counterfactual difference. The modality is tactile/force perception rather than harm-stream latents. The specific-counterfactual SD-003 requires (choosing a_cf and evaluating E2(z_t, a_cf)) goes beyond what this paper evidences. The experiment is also a symmetric reciprocal paradigm between two agents, whereas SD-003 concerns a single agent attributing its own causal footprint in an environment.

## Confidence Reasoning

Confidence 0.68. Very high source quality (Science, canonical finding) and the behavioral demonstration is directly relevant. The moderate confidence reflects the single-pass vs. two-pass gap, the modality transfer (tactile force vs. harm-stream latent), and the task context difference (symmetric reciprocal paradigm vs. single-agent environment).
