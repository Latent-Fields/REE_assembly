# Two eyes for an eye: the neuroscience of force escalation
**Shergill, Bays, Frith & Wolpert (2003) — Science**
DOI: 10.1126/science.1085327 | PMID: 12855800

## What the paper did

The paper begins from a simple but profound observation: physical conflicts escalate. In tit-for-tat exchanges -- children hitting each other, disputants in bar fights -- both parties sincerely report being the victim of disproportionate force. Both are usually telling the truth about their perceptual experience. Shergill et al. designed a controlled experiment to quantify this asymmetry. A torque motor applied a constant force to a subject's left index finger. The subject was then asked to reproduce that force -- either by pressing with their right index finger directly on the left (direct action), or by using a joystick to control the torque motor (indirect action, where prediction is not possible). The critical comparison was how much force subjects applied versus how much they had received.

## Key findings

When reproducing force via direct action, subjects consistently applied substantially more force than they had received -- they needed to apply roughly two-thirds more to perceive equivalence. When using the joystick (novel mapping, no efference copy possible), they could faithfully reproduce the force. The interpretation is tight: direct action generates an efference copy prediction that attenuates the sensory consequences of the self-produced force, making it feel weaker. The subject must therefore apply more force to match the subjective magnitude of the originally experienced (externally-produced) force. The force escalation in real-world conflicts is a natural consequence: each retaliatory act is under-perceived by the actor, so each perceives the other as escalating.

## REE translation -- link to MECH-071

MECH-071 makes a two-part claim: E2 harm prediction is better calibrated for agent-caused transitions, and E3 learns a graded approach gradient. Shergill et al. deliver the most direct behavioral evidence for the first part.

The mechanism is this: E2 as a forward model (MECH-070) predicts the harm consequences of agent-initiated actions before they arrive. When the prediction is accurate, the arriving harm signal is largely cancelled by the prediction -- it generates a small residual error, not a full surprise. This is what "better calibrated" means in MECH-071 language: smaller, more precise prediction errors for agent-caused harm. When the environment causes harm with no agent action as causal root, E2 has no advance prediction. The harm signal arrives unattenuated, generating a large surprise. The agent therefore systematically underestimates harm they cause (because they predicted it and it was attenuated) and overestimates harm they receive from the environment (because it arrives as a full surprise). This is the Shergill effect at the level of latent harm evaluation.

There is also a striking moral-intuition implication: this same asymmetry would explain why agents tend to discount the harm they cause and amplify the harm they suffer -- not through motivated reasoning but through the basic architecture of predictive processing. MECH-071 operationalizes this as a measurable calibration asymmetry in E2's harm prediction residuals.

## Limitations and caveats

The paper studies force/tactile perception, not harm evaluation. The step from "force attenuation" to "harm calibration asymmetry" requires that the efference-copy mechanism extends into harm-relevant latent representations. This is architecturally argued (MECH-070, SD-011) but not demonstrated here. There is also a temporal structure question: Shergill's paradigm involves immediate force matching; MECH-071's approach-gradient claim requires prospective harm encoding over extended trajectories, which is a different computational problem.

A further consideration: the attenuation effect disappeared when the action-sensation mapping was novel (joystick). If E2's learned latent dynamics are sufficiently novel relative to the harm-generation process, the attenuation might not emerge without explicit architectural support. This is a risk for implementations where E2 is trained from scratch on harm-rich environments -- the prediction-attenuation asymmetry may need to be seeded by architecture, not just emerge from training.

## Confidence reasoning

Science 2003, tight experimental design, robust behavioral effect, frequently replicated, consistent with the broader efference copy literature. Mapping to MECH-071 is the most direct of the four papers reviewed here. Confidence 0.82, reduced from its natural floor by the domain gap (force/tactile to harm) and the latent-model transfer uncertainty.
