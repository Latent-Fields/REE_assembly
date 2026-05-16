# IMGEP: Intrinsically Motivated Goal Exploration Processes (Forestier et al., JMLR 2022)

## What the paper did

Forestier, Portelas, Mollard, and Oudeyer built a computational framework for autonomous developmental learning, directly modelled on how human infants create their own learning curricula through curiosity-driven exploration. IMGEP's core mechanism: the agent self-generates goals from a parameterised goal space, selects the next goal to attempt based on empirical learning progress (the rate of competence improvement on that goal over recent history), and systematically reuses experience across goals. No external curriculum is specified. The agent's internal progress tracking generates a natural curriculum: it preferentially practices goals where it is currently improving, moves away from goals where it has plateaued, and is drawn to explore new regions of the goal space when progress is zero on all familiar goals.

## Key findings

On a real humanoid robot with hundreds of continuous goal dimensions, IMGEP discovers diverse skills -- including nested tool use -- that would be unreachable by random goal exploration or objective-driven RL alone. The key empirical result is that skills learned early become stepping stones for skills learned later: the curriculum is self-organising, not externally imposed. The theoretical contribution is connecting infant developmental trajectories to the computational principle of learning progress maximisation, providing a mechanism for why infants preferentially engage with moderately difficult tasks (the Goldilocks principle in developmental psychology).

## Translation to REE

REE's V_s monostrategy problem has an IMGEP-relevant diagnosis: the agent collapses to a single mode because gradient pressure on the dominant attractor overwrites the learning signal from competing attractors before they are sufficiently explored. IMGEP's solution is to track per-goal competence and actively steer exploration toward the least-explored competence-improving goal. For REE, this means tracking per-schema or per-region wanting saturation as a proxy for competence, and modulating schema salience in the E3 score by learning progress rather than (or in addition to) current wanting level. When wanting for a region saturates (competence plateau), salience for that region should decrease and salience for under-explored regions should increase. This is a principled curriculum over the wanting landscape, not noise injection. It maps onto ARC-066 (tonic vigor: competence-state-dependent exploration modulation) and ARC-072 (hippocampal cue-indexed goal repertoire: the hippocampus stores the goal-region map that makes per-goal competence tracking possible).

## Limitations and caveats

IMGEP requires an explicit parameterised goal space. REE's goal space is implicit in the residue field, not a discrete set of labelled goals. Extracting a learning-progress signal requires either discretising the goal space (per-region wanting history) or approximating progress from E3 score variance per schema. The cold-start problem is also real: IMGEP's curriculum requires the agent to have already made some progress on some goals before the learning-progress signal is meaningful. REE's infant-stage agent may need a bootstrapping phase (analogous to motor babbling) before an IMGEP-like curriculum can operate.

## Confidence

0.77. JMLR publication with solid developmental science grounding. Transfer risk lower than other entries because REE's wanting/residue mechanism is a natural home for a learning-progress proxy. Main gap is engineering: making REE's goal space explicit enough to track per-goal progress.
