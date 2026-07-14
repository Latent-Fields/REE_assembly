# Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning

**Class surveyed:** CURRICULUM / GOAL-GENERATION | **Evidence direction:** supports | **Confidence:** 0.72

**Source:** Sebastien Forestier, Remy Portelas, Yoan Mollard et al. (2022). *Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning.* JMLR 23(152):1-41 (arXiv:1708.02190)

Forestier et al. formalise Intrinsically Motivated Goal Exploration Processes (IMGEP): the agent self-generates a space of parameterized goals and selects which to pursue by maximizing *learning progress* -- the empirical improvement in achieving goals from a region -- yielding an automatic curriculum that moves from easy/high-progress goals to harder ones as competence saturates, reusing experience across goals in a hindsight-like batch update.

This is the paper that most sharply separates the curriculum class from a plain novelty bonus. Novelty (RND/count) rewards unpredictability of state and keeps rewarding noisy or unlearnable regions -- the noisy-TV trap. Learning-progress rewards *reducible error / competence gain* and actively abandons both mastered and unlearnable regions. It is a genuinely distinct, competence-directed drive that composes with REE's existing curiosity substrate rather than duplicating it.

Buildability is the lightest of the curriculum class: the learning-progress selector is a bookkeeping layer over per-goal-region success deltas, directly implementable as a proposer policy on top of the existing agent -- no architecture add-on. Its developmental grounding (Oudeyer, Kaplan & Hafner 2007, learning-progress as intrinsic drive) also fits REE's brain-like-construction constraint.

Confidence 0.72: framework-level plus robotics evidence rather than a MiniGrid floor->competent datapoint, so it corroborates the class and the learning-progress-vs-novelty distinction more than it proves the specific number. Paired with AMIGo (which supplies the discrete-gridworld precedent) it makes the curriculum route the strongest *standalone* unsupervised competence-manufacturer.
