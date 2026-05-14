# Pinneri et al. 2021 - Sample-efficient Cross-Entropy Method for Real-time Planning

[PMLR](https://proceedings.mlr.press/v155/pinneri21a.html) - Proceedings of the 2020 Conference on Robot Learning, PMLR 155:1049-1065.

## What the paper did

Pinneri and colleagues study CEM as a trajectory optimizer for model-predictive control. Their iCEM variant keeps the basic CEM pattern but adds proposal-side improvements such as temporally correlated action sequences and memory. The emphasis is practical: make CEM fast enough for real-time planning while preserving the advantages of sampling-based trajectory optimization.

## Why this matters for ARC-065

The relevant lesson for V3-EXQ-563b is the locality of the repair. When CEM is the live proposal boundary, the right first repair is a measured change to candidate generation, not a new high-level drive. iCEM supports conservative proposal-side interventions: keep normal CEM candidates, instrument the refit loop, preserve useful proposal structure, and avoid confusing downstream selection with an unevaluated mean action.

For REE, this argues for two implementation constraints. First, scaffold candidates should remain diagnostic and should be recorded separately. Second, support-preserving CEM should be an experimental flag that minimally guards first-action support while leaving the CEM scoring path observable.

## Limitations and confidence

iCEM does not address REE's exact failure: categorical first-action classes disappearing from the final candidate set. It works in continuous control and focuses on sample efficiency. Still, its proposal-side repair style is a close engineering analogue. Confidence is 0.70: strong for CEM/MPC design discipline, moderate for the categorical action-support translation.
