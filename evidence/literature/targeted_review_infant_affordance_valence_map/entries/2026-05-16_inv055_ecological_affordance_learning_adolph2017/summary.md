# Ecological Affordance Learning in Development -- Adolph (2019)

## What the paper does

Karen Adolph's theoretical synthesis, "An Ecological Approach to Learning In (Not And) Development," argues that learning and development are not separable processes. The paper reviews decades of research from the NYU Infant Action Lab on how infants acquire locomotor and object-manipulation affordances. Core claims: behavioral flexibility requires varied, error-laden experience; learning is posture-specific; infants do not perceive affordances when first acquiring a skill; and the real developmental outcome is "learning to learn" -- flexible processes for perceiving body-environment relations rather than memorized facts.

## Key findings relevant to REE

The empirical base is substantial. Novice crawlers repeatedly fail at steep slopes that experienced crawlers perceive as dangerous. Experienced crawlers transfer almost nothing to walking: they become novices again with their first steps. Walking infants average 2,400 steps per hour across varied surfaces and fall 17 times per hour -- this error-rich varied experience is the raw material from which affordance calibration is built.

Three points are directly relevant to REE. First, the exploration epoch must precede reinforcement narrowing: applying goal-directed reinforcement before the exploration epoch is complete locks in a narrow option library. Second, environmental variation is necessary: an impoverished training substrate with few surface types and uniform topology restricts the affordance map regardless of training duration. Third, posture-specificity means the exploration epoch must span the agent's full action repertoire.

## How this maps to REE

INV-073 posits any model-building agent must undergo a dedicated motor-sensory exploration epoch before RL narrows the option library. Adolph's framework is probably the strongest empirical grounding for this claim in the developmental literature. INV-055 requires the infant stage to produce a behavioral repertoire and harm/benefit geography -- the behavioral repertoire component is directly addressed. ARC-072 identifies a gap in REE: insufficient diversity-bootstrapping before RL narrowing is the upstream cause of monostrategy. Adolph's work implies the substrate must include diverse action-environment encounters from the start of training.

## Limitations and caveats

The paper does not address valence map formation, reward sensitivity, or the benefit/harm side of INV-055. The full requirement of INV-055 -- populating a harm/benefit geography and valence map -- requires additional literature. Transfer from human infant locomotion to a grid-world agent is approximate: infants physically fail in ways that make harm feedback natural and salient; REE needs engineered harm salience signals in a discrete environment.

## Confidence reasoning

Confidence 0.78 reflects strong source quality (Adolph is the leading researcher in this domain), good mapping to the behavioral repertoire component of INV-055 and INV-073, and low transfer risk for the core principle. Capped below 0.80 because the valence/reward component is not addressed.
