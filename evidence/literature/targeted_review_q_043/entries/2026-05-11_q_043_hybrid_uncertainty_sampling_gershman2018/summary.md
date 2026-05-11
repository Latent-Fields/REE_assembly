# Gershman 2018 — Deconstructing the human algorithms for exploration

**Citation.** Gershman SJ. (2018). Deconstructing the human algorithms for exploration. *Cognition* 173:34-42. [DOI](https://doi.org/10.1016/j.cognition.2017.12.014). PMID 29289795.

## What the paper did

Gershman set out to adjudicate between two algorithmic families for human exploration. The first family, uncertainty bonuses, includes Upper Confidence Bound (UCB) and the related "directed exploration" framework: the policy gets an additive bonus on options it is uncertain about, biasing the choice toward information. The second family, sampling, includes Thompson sampling and softmax-with-decision-noise: the policy is stochastic, with the stochasticity scaling with some quantity related to uncertainty.

He showed analytically that the two families make different predictions about the shape of the psychometric function. Uncertainty bonuses shift the BIAS of the response curve (the indifference point moves as uncertainty changes) without changing its slope. Sampling shifts the SLOPE (the curve becomes shallower) without changing the bias. The two signatures are orthogonal in principle and can be co-estimated from behavioural data.

In two experiments with human subjects, Gershman found evidence for BOTH shifts. The bias change was present, the slope change was present, and a hybrid model combining an uncertainty bonus with a sampling mechanism fit better than either single-mechanism model on AIC and BIC. The conclusion is that human exploration uses both an uncertainty-driven information-seeking signal AND a randomisation signal, and both are needed for a good quantitative fit.

## Relevance to Q-043

Of all the anchors in this lit-pull, Gershman 2018 is the most directly on-topic. Q-043's PASS-as-question-resolution outcome is "Pareto frontier exists with a consistent (w_313, w_314) regime across seeds" — i.e., the empirical answer is that BOTH mechanisms contribute and neither extreme calibration suffices. Gershman 2018 already gives that answer at the human-behavioural level: humans use both, and the hybrid model is the best account of their data.

The bias-vs-slope diagnostic is also methodologically useful for the V3 sweep. If REE runs a MECH-313-OFF arm and the policy shows a BIAS shift relative to baseline (rather than a slope shift), that would indicate MECH-314 was carrying the calibration load that should have been a slope-mechanism effect — a sign that one mechanism is compensating for the other in a way that the calibration sweep should detect and report.

## Caveats

Gershman's experiments are two-armed bandits with explicit uncertainty manipulations; SD-054 reef is multi-rule, dynamic, and the "uncertainty" the policy faces is over which rule applies, not over an arm's payoff. The translation is at the algorithmic-family level, not the implementation level. REE's MECH-313 is implemented as an action-selection-layer noise floor rather than as a Thompson sample over value estimates; MECH-314 is implemented via a StructuredCuriosity module that computes uncertainty bonuses per state, not over arms. The algorithmic correspondence is genuine but loose.

The hybrid-best-fit result depends on BIC-style model selection, which can be sensitive to parameter count and to which alternative models are compared. A sufficiently flexible single-mechanism model — for example, one that lets the sampling temperature vary with uncertainty — could in principle approximate the hybrid fit. Gershman is aware of this and addresses it in the discussion, but the result is not as airtight as a positive double dissociation.

For Q-043's specific concern — finding a Pareto frontier between behavioural diversity and task reward — Gershman 2018 does not directly speak to the trade-off, because his task does not have a complex task-reward structure where excessive exploration would meaningfully hurt performance. The empirical finding maps onto Q-043's prediction at the level of "both mechanisms contribute" but not at the level of "the optimal weighting is (x, y)."

## Confidence reasoning

I assign 0.88, the highest in the Q-043 set. Source quality (0.85) is strong (Cognition, model recovery, two experiments). Mapping fidelity (0.90) is the highest because the algorithmic families Gershman compares correspond more cleanly to MECH-313 and MECH-314 than any other paper in this lit-pull. Transfer risk (0.25) is low because the algorithmic-class match is solid. The 0.12 deficit from a hypothetical 1.0 reflects (a) task simplicity vs SD-054, (b) BIC-based model selection rather than a positive dissociation, and (c) lack of trade-off data against task reward.
