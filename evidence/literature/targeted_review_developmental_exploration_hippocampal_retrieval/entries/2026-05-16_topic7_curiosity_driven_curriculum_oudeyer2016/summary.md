# How Evolution May Work Through Curiosity-Driven Developmental Process
**Oudeyer & Smith (2016) -- Topics in Cognitive Science**

## What the paper did

Pierre-Yves Oudeyer (FLOWERS team, INRIA) and Linda Smith (Indiana University developmental psychology) present a synthesis and robotic experiment. The robotic experiment allowed a learner to probabilistically select its own learning experiences based on a formalization of curiosity as expected reduction in prediction error (learning progress). The paper describes how curiosity-driven learning yields self-organized epigenesis with emergent ordered behavioral and cognitive developmental stages.

## Key findings

In the robot experiments, curiosity-driven learning (selecting for maximum learning progress) led the robot to successively discover object affordances and vocal interactions with peers -- without any pre-programmed curriculum. A learning curriculum adapted to the learner's current state formed automatically. The observed trajectories share many properties with infant development: a mixture of regularities (ordered stages) and diversities (individual variation in stage sequence and timing). The paper argues these emergent developmental structures can guide and constrain evolution, especially for language origins.

## REE translation

The core REE relevance is the demonstration that ordered developmental stages arise from prediction-error-reduction intrinsic motivation, not from an externally designed curriculum. For REE's infant substrate, this means the transition from random exploration to structured action patterns does not need to be hard-coded or externally scheduled -- it can self-organize if E1's prediction error serves as an intrinsic reward.

The specific mechanism is: the agent concentrates exploration where learning progress is highest (intermediate difficulty -- neither already mastered nor completely unpredictable). This is the "zone of proximal development" formalized computationally. Operationally, this means REE's infant substrate could implement exploration weighting based on the derivative of E1 loss -- actions in novelty regions where E1 loss is decreasing fast should be preferentially explored.

This directly addresses REE Q3: the transition from random to structured is governed by learning progress, not by a separate curriculum signal.

## Limitations and caveats

The robot experiment uses a simplified environment without harm constraints; pure curiosity-driven learning would need augmentation with harm sensitivity in REE's setting. The ordered stages observed in the robot may not emerge in REE's more complex action space. The paper conflates curiosity as an evolutionary force with curiosity as a developmental mechanism, which are distinct claims.

## Confidence reasoning

Topics in Cognitive Science invited contribution; strong author credentials (Oudeyer and Linda Smith). The robotic experiment is well-documented and the infant development parallels are well-argued. Confidence 0.77.
