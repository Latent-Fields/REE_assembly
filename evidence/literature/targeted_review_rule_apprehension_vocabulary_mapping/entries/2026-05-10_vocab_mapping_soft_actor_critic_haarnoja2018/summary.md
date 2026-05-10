# Haarnoja et al. 2018 -- Soft Actor-Critic: Maximum-Entropy Reinforcement Learning

## What the paper did

Haarnoja, Zhou, Abbeel and Levine introduced Soft Actor-Critic (SAC), an off-policy actor-critic algorithm based on the maximum-entropy reinforcement-learning framework. The MaxEnt objective replaces the standard expected-reward maximisation with a sum of expected reward AND policy entropy: the agent simultaneously maximises return and stays as stochastic as possible while doing so. Empirically, SAC achieves state-of-the-art sample efficiency and stability on continuous-control benchmarks (Hopper, Walker2d, HalfCheetah, Ant, Humanoid). Theoretically, the MaxEnt framework has formal soft-Q-learning convergence guarantees and a clean variational interpretation of the entropy term.

## Key findings relevant to the rule-apprehension vocabulary question

For Pull 4, this paper anchors the ML home of REE's MECH-313 (stochastic-noise-floor). The MaxEnt-RL framework explicitly maximises policy entropy; the entropy term is exactly what MECH-313 is supposed to do at the substrate level. Direct vocabulary mapping:

- *MECH-313 (stochastic-noise-floor, LC-NE-tonic-analog)* = *MaxEnt-RL policy-entropy term*.
- *ARC-065 (behavioural-diversity-generation pathway)* = *MaxEnt-RL with non-zero entropy temperature alpha*.
- *MECH-313's "non-zero softmax temperature on E3" implementation note* = *SAC's temperature parameter alpha*.

This is one of the cleanest single-paper inheritances in this pull. SAC gives REE off-the-shelf convergence guarantees, an extensive hyperparameter-tuning literature (especially around alpha auto-tuning), and a benchmark suite for comparing the noise-floor-on vs noise-floor-off conditions. Inheritance is at the *algorithm* level, not just the *concept* level.

## How the findings translate to REE

Three direct implications:

1. **R2 inheritable result**: SAC is the canonical implementation candidate for MECH-313. The MaxEnt-RL formal framework gives REE a normative justification for non-zero entropy regularisation (it is part of the optimisation objective, not an ad-hoc addition).

2. **R4 renaming candidate**: MECH-313 could be renamed "max-entropy policy regularisation" (or kept REE-specific but explicitly cross-referenced to MaxEnt-RL canon). The biological/substrate reading (LC-NE tonic) and the algorithmic reading (MaxEnt-RL) line up cleanly.

3. **R5 sequencing impact**: V3-EXQ-543b should test the noise-floor arm (ARM_1) using SAC-style entropy regularisation rather than ad-hoc softmax temperature -- the MaxEnt formulation gives a principled training-time objective rather than an inference-time temperature.

## Limitations and caveats

SAC's entropy term is a hyperparameter chosen by the engineer (or auto-tuned via a target-entropy constraint, but still ultimately externally controlled). In REE's biological reading, the noise floor is supposed to be substrate-emergent (LC-NE tonic firing, per Pull 1's Aston-Jones 2005 entry). Adopting MaxEnt-RL vocabulary at the algorithm level commits REE to engineer-chosen alpha; whether this matches the biological dynamics is an open empirical question.

The other caveat: SAC's empirical demonstrations are on simulated robotics, not biological agents. Transfer to REE's continuous-state grid-world substrate is plausible (and standard) but not zero-shot.

A subtler issue: SAC's entropy term encourages *immediate* stochasticity in the policy. The biological MECH-313 substrate may also encourage *behavioural-trajectory* stochasticity (different episodes look different) which is more like a mutual-information / DIAYN-style objective than a per-step entropy. Whether the MaxEnt-RL per-step formulation suffices for what MECH-313 is supposed to do is implementation work.

## Confidence reasoning

Scored 0.80. Source quality is at-ceiling (ICML 2018, 10000+ citations, code released and extensively replicated). Mapping_fidelity is high (0.82) because MaxEnt-RL is the canonical home for stochastic-noise-floor claims. Transfer_risk is low-moderate (0.30); the algorithm transfers cleanly, the biological-substrate claim is where translation work is needed. The paper feeds R2 (clean MaxEnt-RL inheritance for MECH-313), R4 (RENAME-TO-EXISTING candidate: MECH-313 -> "max-entropy policy regularisation" or a hybrid with explicit cross-reference), and R5 (use SAC-style training-time entropy regularisation in V3-EXQ-543b ARM_1).
