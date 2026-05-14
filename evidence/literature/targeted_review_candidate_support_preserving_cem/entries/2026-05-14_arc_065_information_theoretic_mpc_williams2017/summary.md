# Williams et al. 2017 - Information theoretic MPC for model-based reinforcement learning

[DOI](https://doi.org/10.1109/ICRA.2017.7989202) - 2017 IEEE International Conference on Robotics and Automation, pp. 1714-1721.

## What the paper did

Williams and colleagues develop an information-theoretic model-predictive control algorithm for model-based reinforcement learning. The paper sits next to CEM in the sampling-based MPC family, but its framing emphasizes trajectory distributions, weighted samples, stochastic optimal control, and information-theoretic structure rather than a pure hard-elite refit loop.

## Why this matters for ARC-065

This is useful for REE as a design analogy, not as a planner replacement. V3-EXQ-563a showed that E3 can use a score bias once candidate support exists. The next question is whether the proposer supplies a support surface and whether the bias magnitude is commensurate with the E3 score range. Information-theoretic MPC makes that coupling explicit: the optimizer is not only about the single best trajectory; the distribution and weighting structure are part of the control mechanism.

Therefore V3-EXQ-563b should measure candidate entropy, support counts, score ranges, score_bias ranges, and selected rank before and after bias. A support surface without score-scale calibration is still not enough for naturalistic goal, curiosity, or vigor mechanisms to move behaviour.

## Limitations and confidence

The paper is not a CEM-support-preservation recipe. It does not argue that REE should replace CEM with MPPI, and it says nothing about hippocampal action-object decoding. Confidence is 0.66 because the mapping is conceptual and diagnostic: entropy and scale need instrumentation before behavioural evidence is interpretable.
