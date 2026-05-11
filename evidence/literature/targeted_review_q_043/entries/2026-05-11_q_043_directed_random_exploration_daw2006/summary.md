# Daw et al. 2006 — Cortical substrates for exploratory decisions in humans

**Citation.** Daw ND, O'Doherty JP, Dayan P, Seymour B, Dolan RJ. (2006). Cortical substrates for exploratory decisions in humans. *Nature* 441(7095):876-9. [DOI](https://doi.org/10.1038/nature04766). PMID 16778890.

## What the paper did

Fourteen healthy adults played a four-armed bandit gambling task during fMRI. Reward distributions on each arm drifted slowly across trials, so a rational player had to balance exploiting the currently best-looking arm against occasionally exploring the less-sampled arms in case one had drifted upward. The authors fit a softmax reinforcement-learning model with a Kalman-filter belief over each arm's payoff to each subject's choice sequence, classified every trial as exploitative or exploratory on the basis of whether the chosen arm was the model's argmax, and looked for BOLD signal that tracked the classification.

Two systems showed the cleanest dissociation. Frontopolar cortex and intraparietal sulcus were preferentially active during exploratory decisions; striatum and ventromedial prefrontal cortex tracked value and were preferentially active during exploitative decisions. The model fit was good enough to support a strong claim: human four-armed-bandit choice is consistent with a soft-action-selection policy modulated by a separable exploration system.

## Relevance to Q-043

Q-043 asks about the relative weighting of MECH-313 (state-independent stochasticity, LC-NE tonic analog) and MECH-314 (state-dependent uncertainty-driven curiosity bonus, frontopolar analog) in the V3 substrate. Both presuppose that an exploration system exists separately from the exploit system — that the policy is not purely greedy value-maximisation with arbitrary tie-breaking noise. Daw 2006 is the canonical neuroimaging evidence for this presupposition: the frontopolar locus is mechanistically distinct from the value-tracking striatum, and the dissociation is robust to the specific model formulation. Without this evidence the question of "how to weight" the two exploration mechanisms would not even be well-posed; one might collapse exploration into a single decision-noise parameter.

The mapping that REE is committed to — MECH-314 ≈ frontopolar uncertainty-driven bonus per the ARC-065 family doc — gets its primary anchor here.

## Caveats and what this paper does NOT establish

Daw 2006's RL model uses a softmax policy with a temperature parameter; exploration in the model is driven by both the temperature and the Kalman variance over each arm. The paper does not directly separate state-independent decision noise from state-dependent uncertainty-driven information seeking. Their classification of trials as exploratory vs exploitative pools over both, so the frontopolar BOLD effect could be driven by either mechanism, or both. The within-exploration decomposition that Q-043 actually asks about — calibrating the relative contribution of a noise-floor mechanism against an uncertainty-bonus mechanism — is left for later work. Wilson 2014, Zajkowski 2017, Warren 2017, and Gershman 2018 (see sibling entries) made that distinction empirically.

I am also conscious that the cohort is small (n=14), the task is one-shot (not life-long REE agent training), and the reward distributions are stationary in their drift rate (REE's SD-054 reef substrate is not). Each of these is a transfer caveat rather than a fatal flaw.

## Confidence reasoning

I assign 0.78 because the paper is canonical and methodologically strong (source_quality 0.92), but its mapping onto Q-043's specific calibration question is moderate (0.55) — it anchors the existence of the two systems rather than their relative weights. The transfer risk is modest (0.25) because the human-RL setting maps onto the REE substrate at the relevant level of abstraction. Daw 2006 is load-bearing for the EXISTENCE premise of Q-043, not for the CALIBRATION verdict — that distinction is captured in the failure_signatures field.
