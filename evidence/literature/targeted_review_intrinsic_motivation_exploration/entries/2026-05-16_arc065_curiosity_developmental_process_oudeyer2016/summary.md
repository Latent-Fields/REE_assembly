# Summary: How Evolution May Work Through Curiosity-Driven Developmental Process (Oudeyer & Smith, Topics Cog Sci 2016)

**Entry:** 2026-05-16_arc065_curiosity_developmental_process_oudeyer2016
**Claims:** ARC-065, MECH-314, MECH-314c
**Direction:** supports | **Confidence:** 0.76

---

## What the paper did

Oudeyer and Smith reviewed computational models of curiosity-driven learning in developmental robotics (particularly the IADM -- Intelligent Adaptive Curiosity -- architecture), connecting them to empirical data from infant development. The central experiment described is a robot learner that selects experiences based on their predicted learning-progress (rate of prediction improvement, not novelty per se). The robot discovers object affordances and eventually vocal interaction patterns as an emergent consequence of this drive, without any pre-programmed developmental schedule.

## Key findings relevant to the claim

The central finding is that learning-progress curiosity -- not pure novelty curiosity -- produces emergent ordered developmental stages that parallel infant development. When a robot selects experiences that maximise its current learning rate, it naturally progresses from simple to complex tasks because easy tasks become boring quickly (learning rate drops to zero once mastered) and genuinely novel but too-hard tasks are also uninformative (learning rate stays near zero because the task exceeds current capacity). The system gravitates toward the zone of proximal development.

A key comparison in the paper is between novelty-based curiosity (visit novel states) and learning-progress curiosity: novelty curiosity produces equal coverage without developmental staging; learning-progress curiosity produces staged development because it naturally dwells at the frontier of competence. This is directly relevant to MECH-314c vs. MECH-314a in REE: if the goal is to produce a natural developmental curriculum during infant-stage training, MECH-314c is the more appropriate signal.

The environment richness condition is made explicit: the staged development only emerged when the environment contained a natural difficulty gradient -- objects with varying affordance complexity, vocal partners with hierarchically structured interactions. In a featureless environment, no developmental staging emerged even with learning-progress curiosity, because the learning rate was flat everywhere.

## REE translation -- the central question

This paper is the strongest available evidence for the specific user question about environment structure. The finding is unambiguous: a novelty_bonus_weight at maximum (MECH-314a analog) does not produce developmental staging. Learning-progress curiosity (MECH-314c) does -- but only when the environment has a natural difficulty gradient.

For REE's infant-stage design, this translates to: if the CausalGridWorld environment in the infant stage is a flat gridworld where all regions are equally hard (or all equally easy), neither high novelty_bonus_weight nor MECH-314c will produce meaningful developmental sequencing. The environment needs contextually distinct regions that can be learned in sequence -- simpler patterns that the agent can master early, more complex patterns that become accessible once the simple ones are consolidated.

The emergent curriculum finding also has implications for the REE infant-stage duration: with an appropriate environment, the agent may naturally complete the infant stage when it has mastered the available affordance structures, without requiring a pre-defined curriculum gate.

## Limitations and caveats

The robotic experiments used multi-modal environments that are substantially richer than REE's current gridworld -- the environment richness condition that produced staged development may exceed what a CausalGridWorld can provide even with modifications. The theoretical framework (IAC) predates the deep learning era; whether modern deep RL agents show the same emergent developmental staging with learning-progress curiosity is an open empirical question not fully settled by this paper. This is why the confidence is moderate (0.76) despite a clear finding: the transfer from developmental robotics to deep RL on a gridworld involves untested assumptions.

## Confidence reasoning

Topics in Cognitive Science 2016, Oudeyer is the primary architect of the learning-progress curiosity tradition. Source quality is good, not top-tier (this journal is not Nature-level for neuroscience). Mapping fidelity is moderate -- the key insight transfers clearly but the specific environmental conditions required for the finding may not be met in REE's current gridworld. Transfer risk is above average because of the computational substrate difference.
