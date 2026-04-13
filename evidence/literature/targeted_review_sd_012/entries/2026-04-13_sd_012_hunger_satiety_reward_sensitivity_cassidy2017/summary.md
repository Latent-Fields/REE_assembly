# Hunger and Satiety Gauge Reward Sensitivity

**Entry:** 2026-04-13_sd_012_hunger_satiety_reward_sensitivity_cassidy2017
**Claim tested:** SD-012 (homeostatic drive modulation of z_goal seeding)
**Evidence direction:** supports
**Confidence:** 0.72

---

## What the paper does

Cassidy and Tong (2017) is a systematic review synthesising how the neurochemical systems governing hunger and satiety modulate mesolimbic dopaminergic reward circuits. Rather than presenting new empirical data, it organises a large body of rodent pharmacology, optogenetics, and some primate and human neuroimaging into a coherent framework: hunger signals amplify dopaminergic reward sensitivity while satiety signals suppress it, through anatomically distinct but interacting pathways.

The hunger-promoting side involves AgRP/NPY neurons of the arcuate nucleus (which disinhibit dopaminergic regions upon food cue detection), lateral hypothalamic neurons and their orexin projections to VTA, and ghrelin acting directly on VTA GHS-R1a receptors and indirectly through AgRP/orexin intermediaries. The satiety-promoting side involves GLP-1 neurons of the nucleus tractus solitarius (which reduce long-term potentiation in dopaminergic synapses and increase dopamine clearance), POMC neurons producing balanced synaptic changes that constrain continued feeding, and leptin broadly suppressing mesolimbic reward system activity.

## Key findings

The central result is that drive state is not a passive backdrop for reward processing -- it is an active gain-control parameter on the dopaminergic system. Hunger mediators amplify the dopaminergic response to food-predictive cues, specifically the phasic release triggered by conditioned stimuli, while satiety mediators attenuate baseline and cue-evoked dopamine. The modulation is graded and reversible: as energy reserves recover, gain returns toward a default level. The review also documents that satiety suppression is not absolute silencing -- it reduces, rather than eliminates, reward-circuit sensitivity, so that sated animals can still respond to strong rewards.

A practical corollary is that highly palatable (superstimulus) foods can bypass satiety-mediated suppression, driving continued approach even in the presence of GLP-1 and leptin. This asymmetry -- easier to amplify than to suppress -- has direct implications for any drive-scaling architecture.

## REE translation

SD-012 formalises drive-state modulation as effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level), where drive_level = 1.0 - agent_energy. The Cassidy/Tong synthesis is the biological grounding for this formulation. When the agent is energy-depleted (drive_level near 1.0), AgRP/ghrelin-equivalent processes amplify dopaminergic gain on benefit signals -- this is the drive_weight * drive_level term. When sated (drive_level near 0.0), effective_benefit collapses toward raw benefit_exposure -- matching leptin/GLP-1-mediated suppression back to default. The bidirectionality and graded nature of the modulation justify the linear multiplicative formulation in SD-012 rather than a binary switch.

The insular cortex integrative role (which receives both drive-state signals and gustatory/reward value signals) is consistent with the REE architecture where z_goal seeding requires convergence of drive state and benefit exposure -- neither alone is sufficient.

## Limitations and caveats

The review is rodent-centred and does not resolve the precise mathematical form of the drive-gain relationship. Whether the scaling is linear (as SD-012 assumes), sigmoidal, or logarithmic with drive level is not empirically determined. The review also pertains specifically to food-related goal-seeking; extension to generalised goal-directed behaviour in non-food domains requires inference. The biological circuits operate on timescales of minutes to hours (neuroendocrine), whereas SD-012 operates at the per-step level (energy_decay = 0.01/step). The architectural mapping is valid in spirit but quantitative gain calibration needs care.

## Confidence reasoning

Source quality is high for a peer-reviewed systematic review (Frontiers in Endocrinology). Mapping fidelity is good: the bidirectional, graded drive-scaled dopaminergic gain maps cleanly onto SD-012's functional restatement. Transfer risk is moderate: biological circuits vs. discrete architectural parameter. Confidence 0.72.
