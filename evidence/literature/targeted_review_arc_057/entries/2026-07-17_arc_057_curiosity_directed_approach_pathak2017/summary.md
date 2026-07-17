# Pathak, Agrawal, Efros & Darrell (2017) -- Curiosity-driven Exploration by Self-supervised Prediction

**Claim tested:** ARC-057 (approach emerges from DA-mediated representational expansion x a curiosity drive; no explicit approach gradient required).
**Direction:** supports | **Confidence:** 0.60

## What the paper did

Pathak et al. give an agent a single intrinsic reward: the error of a forward model trying to predict the next state, computed in a feature space that a self-supervised inverse-dynamics model learns (so the features encode what the agent can control, filtering out uncontrollable noise). With no extrinsic reward at all, curiosity-only agents learn purposeful behaviour: they systematically traverse Super Mario Bros levels and navigate room-to-room through VizDoom mazes. The learned exploration transfers to unseen maps, and when sparse extrinsic reward is later introduced it is reached far faster. This is the ICML 2017 paper (arXiv:1705.05363).

## Why it bears on ARC-057

ARC-057 asserts that directed approach is an *emergent* consequence of an information-seeking drive rather than a commanded gradient -- the agent "does the same thing everywhere (explores available structure)," and an observer only infers an attractive gradient. Pathak et al. are the cleanest computational proof-of-concept of the first half of that claim: an intrinsic curiosity drive, and nothing else, yields coherent, directed, goal-approaching navigation. The agent has no value function pointing it anywhere; the directedness is a by-product of chasing prediction error through the reachable structure of the world. REE's SD-025 curiosity drive is meant to play exactly this functional role. Where ARC-057 goes further -- and where this paper cannot follow -- is the claim that the *space itself* has been asymmetrically shaped by dopaminergic representational expansion (MECH-232 / SD-024), so that a uniform drive produces approach aimed specifically at reward locations. Pathak et al. supply the "uniform drive produces directed approach" half; the DA-asymmetry half is REE's own contribution.

## Limitations and caveats

The curiosity computations differ in a way worth stating plainly. ICM curiosity is *surprise* -- prediction error, seeking the unpredictable. SD-025 curiosity is *density-following* -- novelty defined as representational density times (1 - familiarity), seeking the representationally rich but not-yet-familiar. The shared label "curiosity" spans two genuinely different drives, and one known failure mode makes the difference concrete: prediction-error curiosity falls into the "noisy-TV" trap (a stochastic transition looks perpetually novel and captures the agent), a pathology the density-following formulation does not share. So a naive reading that "curiosity reliably yields adaptive approach" would over-claim. And, again, there is no DA representational-expansion component here -- the environment is fixed and explored uniformly.

## Confidence reasoning

Source quality is high (canonical, heavily cited ICML result with public code and many replications). Mapping fidelity is moderate: strong on ARC-057's emergence principle (intrinsic drive -> directed approach, no explicit reward gradient), weaker because the drive is prediction-error rather than density-following and there is no DA-expansion partner. Transfer risk is moderate-to-high: a deep-RL pixel agent in video games maps onto REE's abstract hippocampal CEM only by functional analogy. Net 0.60: a solid support for the "emergence from a curiosity drive" leg, discounted for the mechanism differences and for evidencing only half of the two-component interaction.
