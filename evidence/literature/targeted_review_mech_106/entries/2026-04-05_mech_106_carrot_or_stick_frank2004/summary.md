# Frank, Seeberger & O'Reilly 2004 -- By Carrot or By Stick: MECH-106 Mapping

**Source:** Frank, M.J., Seeberger, L.C., & O'Reilly, R.C. (2004). By carrot or by stick: cognitive reinforcement learning in parkinsonism. *Science*, 306(5703), 1940-1943. DOI: [10.1126/science.1102941](https://doi.org/10.1126/science.1102941)

---

## What the Paper Does

This Science paper provides the critical behavioural evidence for the D1/D2 Go/NoGo asymmetry that Frank 2005 models computationally. The logic is elegant: if D1 pathway activity (driven by phasic DA bursts) supports Go/approach learning, and D2 pathway activity (modulated by DA dips) supports NoGo/avoidance learning, then Parkinson's patients -- who have reduced striatal dopamine -- should show a selective deficit. But the deficit should depend on medication state. Off medication, tonic DA is reduced, impairing phasic DA bursts but leaving DA dip signalling relatively more intact. On medication, tonic DA is raised by levodopa, restoring burst capacity but paradoxically blunting the DA dip signal (because there is more DA to dip from).

The paper tests this by having patients perform two probabilistic reinforcement learning tasks. The result is a clean double dissociation: off-medication patients are better at learning to avoid negative outcomes (NoGo learning intact, Go impaired); on-medication patients are better at learning to approach positive outcomes (Go learning enhanced, NoGo suppressed). The control group shows normal asymmetric learning in the reward direction, as predicted by baseline dopamine dynamics.

## Key Findings

The double dissociation is the central result. It establishes at the behavioural level what Frank 2005 predicts at the computational level: reward-driven and punishment-driven learning are not simply two ends of a single scale -- they are mediated by anatomically distinct pathways that can be selectively impaired or enhanced by the same pharmacological manipulation. This is not what a unidimensional dopamine-as-value-signal account would predict.

The medication effect is particularly informative: levodopa does not simply restore normal function but creates a specific performance profile (better Go, worse NoGo) that can only be understood if D1 and D2 pathways are being differentially affected. The patients serve as a natural pharmacological dissection of a system that is otherwise difficult to probe non-invasively in humans.

A secondary finding relevant to MECH-106 is that the asymmetry is context-dependent: it depends on the current DA state of the system, not just the valence of the outcome in isolation. A positive outcome in an already high-DA state (on medication) has different effects than the same outcome in a low-DA state. This is consistent with MECH-106's hysteresis account -- the commit threshold change is not just a function of the outcome valence but of the current D1/D2 balance at the time the outcome is received.

## REE Mapping to MECH-106

MECH-106 claims the commit threshold is raised by negative outcomes (via D2 pathway activation) and lowered by positive outcomes (via D1 pathway potentiation). Frank 2004 establishes that these two directions of modulation are empirically dissociable in humans, dopamine-dependent, and selectively disrupted by Parkinson's disease and its treatment. The mapping to commitment entry/exit dynamics is direct at the level of mechanism: the same pathway asymmetry that produces Go/NoGo learning asymmetry in discrete choice tasks should produce commit/de-commit threshold asymmetry in ongoing action sequence management.

The extension MECH-106 requires -- from discrete trial-level asymmetry to commitment mode persistence -- remains inferential. What Frank 2004 directly supports is the foundational premise: that D1 and D2 pathways respond differently to positive and negative outcomes, and that this produces asymmetric action propensity changes. MECH-106 is essentially applying this principle to a different level of action organisation (mode entry/exit rather than single-choice selection).

## Limitations and Confidence Reasoning

The Parkinson's patient methodology is an indirect probe. Dopaminergic medications are not selective for striatal D1 or D2 receptors and have peripheral effects and effects on other brain regions. The dissociation is predicted by the BG model, but the causal story depends on accepting the computational interpretation. There is also a question of task validity: the probabilistic learning task measures what action to take next, not whether to sustain or exit an ongoing commitment -- the latter is a different computational problem that may engage similar but not identical circuits.

That said, this paper is one of the most convincing pieces of human evidence for the D1/D2 asymmetry in reinforcement learning, and it supports the core mechanism MECH-106 invokes. The Science venue and citation record reflect its standing in the field. Confidence: 0.80.

*Based on article retrieved from PubMed (PMID: 15528409, DOI: [10.1126/science.1102941](https://doi.org/10.1126/science.1102941)).*
