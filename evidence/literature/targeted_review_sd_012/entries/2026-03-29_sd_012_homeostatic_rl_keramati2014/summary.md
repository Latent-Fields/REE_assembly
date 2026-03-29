# Keramati and Gutkin (2014) -- Homeostatic reinforcement learning for integrating reward collection and physiological stability

**Claim tested:** SD-012 (z_goal seeding requires drive-scaled benefit signals)

## What the paper did

Keramati and Gutkin set out to solve a problem that had been implicit in reinforcement learning theory but rarely formalised: how do homeostatic drives (hunger, thirst) interact with learned reward to produce adaptive motivated behavior? Standard RL treats reward as a fixed property of outcomes, but biological organisms experience the same food as more rewarding when hungry and less rewarding when sated. The paper derives a normative framework -- homeostatic reinforcement learning (HRL) -- from first principles, then validates it against a range of existing animal behavioral data including drive-modulated reward, devaluation effects, and the paradox of why intravenous nutrient injection is unrewarding even though it reduces hunger equivalently to oral food intake.

## Key findings relevant to SD-012

The core equation of HRL is: reward(outcome) = f(drive_level). More precisely, reward is proportional to the drive-reduction produced by the outcome -- the decrease in distance between current internal state and homeostatic setpoint. When drive is high (large deviation from setpoint), the same outcome produces more drive reduction and is therefore more rewarding. When drive is low (near setpoint), the same outcome produces little drive reduction and is less rewarding. This is a formal derivation, not an ad hoc assumption, arising from the normative principle that animals should optimise for homeostatic stability.

The paper also explains why oral ingestion is rewarding while intravenous nutrient injection is not: the reward signal is triggered by sensory properties of the outcome (taste, smell) that serve as a shortcut estimate of drive-reduction potential. These sensory properties are absent in intravenous injection, so the estimated drive-reduction is zero even though the actual metabolic effect is equivalent. This has direct implications for SD-012: benefit signals in REE are triggered by resource contact (sensory), not by metabolic change (internal), so they need to be scaled by current drive level to correctly represent their actual drive-reduction value.

## REE translation

SD-012's design decision is that effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level). This is a direct implementation of the HRL principle: the effective value of a benefit contact is scaled by how much the agent needs it (drive_level = 1 - energy). At high drive (hungry, energy depleted), a resource contact is amplified to approximately 2-3x its nominal value -- sufficient to push benefit_exposure above the seeding threshold. At low drive (sated), the amplification is near zero. The HRL framework provides the normative justification for this design: this is not an ad hoc fix but the architecturally correct principle for integrating homeostatic state into goal formation.

The paper also supports SD-012's resource respawn requirement: HRL predicts that goal representations require multiple drive-reduction cycles to form stable predictions (the dopamine response must transfer from primary reward to predictive cues over multiple pairings). A single encounter with a resource provides one prediction-error update; repeated encounters with resource respawn provide the iterative updates needed to build a stable z_goal representation.

## Limitations and caveats

The HRL model is a normative framework, not a mechanistic implementation. The specific formula in SD-012 (linear scaling with drive_weight=2.0) is a simplification of the full HRL criterion, which is more complex (involving the derivative of the homeostatic error function). The linear approximation is likely adequate for the current CausalGridWorld implementation but may need revision as the architecture becomes more complex. The paper also treats homeostatic drive as a single scalar variable, whereas real biological systems have multiple interacting drives (hunger, thirst, fatigue), which REE does not currently implement. Finally, the paper was validated against existing animal data rather than generating novel experimental predictions, which is a limitation of its empirical status.

## Confidence reasoning

Confidence is 0.85. This is the most directly relevant computational theory for SD-012. The HRL framework provides the normative grounding for drive-scaled benefit signals, and the mapping to SD-012's formula is structurally direct. High confidence because the claim is functional (drive must modulate reward value) and the paper provides formal derivation plus empirical validation. The main limitation -- the simplification from full HRL to linear scaling -- is acknowledged in SD-012 itself.
