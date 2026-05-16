# Summary: Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning

**Entry ID:** 2026-05-16_devrobotics_imgep_curriculum_forestier2022
**Claim IDs:** INV-060, MECH-197, ARC-050, INV-058

## What the paper does

Forestier, Portelas, Mollard, and Oudeyer (JMLR 2022; preprint 2017) present the Intrinsically Motivated Goal Exploration Processes (IMGEP) framework, which achieves automatic curriculum learning by selecting learning goals based on a competence-progress metric. The key insight is that neither maximally easy nor maximally hard goal regions are selected for practice -- the system selects regions where the rate of competence change (within a sliding window) is maximal. Skills acquired at earlier stages act as stepping stones for later, more complex skills. Demonstrated on a real iCub humanoid robot acquiring multi-hundred-dimensional motor skills.

## Key findings

Competence-progress is operationally defined as the derivative of success rate over a sliding window of trials within a goal region. This is a non-Goodharted metric: it tracks where learning is happening, not where performance is already high. The automatic curriculum that emerges visits goal regions in an order that reflects their mutual dependencies -- simpler skills provide a foundation for complex ones. This self-organization matches the structure of INV-060's claim that play type progression is not optional -- competence dependencies enforce the ordering.

## REE mapping

IMGEP provides the operational metric most directly applicable to the DEV-NEED stage gates. For DEV-NEED-010 (sensorimotor play), the gate criterion should be: competence-progress for basic motor-goal regions is near zero (saturation -- the play type has exhausted its developmental contribution). For DEV-NEED-011 (constructive play), competence-progress for compositional multi-step goals should be active and E2 rollout competence should be measurably improving. The stepping-stones finding supports INV-058 and MECH-197's dependency-order claim: the stage progression is emergent from the competence structure, not just imposed by design.

The IMGEP framework answers a key implementation question for ARC-050: synthetic z_goal seeding during play episodes should be targeted at goal regions with positive competence-progress signal, not at already-saturated or not-yet-reachable regions. This makes the synthetic seeding productive rather than random.

## Limitations and caveats

IMGEP does not model play frames at all -- all exploration is treated as real-consequence intrinsic motivation. The bilateral tag mechanism (ARC-049), synthetic signal substitution (MECH-194), and strategy-calibration dissociation (MECH-195) are absent from the framework. The competence-progress metric would need to be applied specifically within play episodes to serve as a DEV-NEED gate, rather than across all exploration. The system does not produce discrete stage certificates -- transitions are continuous, not pass/fail gated.

## Confidence reasoning

Confidence 0.77: JMLR-quality empirical validation on real robots with a well-defined, operationally sound metric. Mapping fidelity is moderate because the play-frame architecture is entirely absent, requiring significant REE-specific adaptation. The core metric (competence-progress) is directly translatable.
