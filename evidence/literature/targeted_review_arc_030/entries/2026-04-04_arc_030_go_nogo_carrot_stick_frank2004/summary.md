# By carrot or by stick: cognitive reinforcement learning in parkinsonism

**Frank, Seeberger & O'Reilly (2004). Science, 306(5703), 1940-1943.**
**DOI:** 10.1126/science.1102941 | **PMID:** 15528409

---

## What the paper did

Frank, Seeberger and O'Reilly tested Parkinson's disease patients both on and off dopaminergic medication on a probabilistic reinforcement learning task requiring discrimination between stimulus pairs with different reward and punishment frequencies. The key manipulation was dopamine level -- on-medication patients had elevated tonic dopamine, while off-medication patients had chronically depleted dopamine. The study coupled this behavioral paradigm with a neurocomputational model of the cortico-basal ganglia-thalamo-cortical circuit that instantiated distinct Go (direct, D1-MSN) and NoGo (indirect, D2-MSN) pathways with opponent dopamine modulation.

## Key findings

The dissociation was striking and predicted by the model: patients on medication were better at learning from positive outcomes and worse at learning from negative outcomes, while patients off medication showed the reverse. The model explains this through opponent dopamine effects. Phasic dopamine bursts (positive reward prediction errors) potentiate D1-MSN synapses in the direct Go pathway, reinforcing actions that led to reward. Phasic dopamine dips (negative prediction errors) potentiate D2-MSN synapses in the indirect NoGo pathway, inhibiting actions that led to punishment. Elevating tonic dopamine with medication boosts Go pathway activity while blunting NoGo pathway signaling via D2 receptor saturation -- the result is an approach-dominant agent who learns poorly from punishment. Depleting dopamine reverses this: Go pathway is suppressed, NoGo is released from inhibition, and the agent learns preferentially from punishment.

## Mapping to ARC-030

This paper is the canonical computational and empirical grounding for ARC-030's symmetry requirement. ARC-030 claims that each BG-like loop in REE requires symmetric Go (approach, goal attractor MECH-112) and NoGo (avoidance, harm stream SD-010) sub-channels, and that removing either direction produces systematic behavioral bias rather than balanced motivation. Frank et al. demonstrate exactly this: the biological system requires both pathways operating in balance, and disrupting either direction -- toward over-approach or over-avoidance -- is measurably pathological. The commit threshold mechanism (ARC-016, MECH-106) that ARC-030 proposes as the competition balance point maps directly onto the model's action selection gate, where the net Go-minus-NoGo evaluation determines whether a candidate action crosses the selection threshold.

The architectural implication ARC-030 draws from this lineage -- that an REE agent trained only on harm avoidance signals would correspond to a dopamine-depleted state -- finds direct empirical grounding here. The off-medication patients represent a pure-avoidance learning state: they acquire avoidance efficiently but fail to build approach-oriented policies, and their overall behavior becomes dominated by avoidance. This is the clinical instantiation of Q-021's prediction.

## Limitations and caveats

The task is a 2-choice probabilistic RL paradigm, not a multi-step trajectory planning problem. Extending the Go/NoGo balance principle to REE's E3-level deliberation requires assuming that the same opponent-pathway architecture scales to longer-horizon evaluation -- a reasonable assumption given the anatomical homology of the three BG-like loops (ARC-021), but one that requires separate validation. The Parkinson's disease population introduces multiple confounders beyond dopamine levels (motor impairment, duration of illness, age-related changes), and the causal attribution to Go/NoGo imbalance specifically relies on the computational model fit rather than direct pathway measurement.

## Confidence reasoning

Confidence 0.82. Source quality is exceptional -- Science publication, canonical in the field, the Frank Go/NoGo model has been replicated and extended across dozens of follow-up studies spanning human, primate, rodent, and computational work. Mapping fidelity is high because the opponent Go/NoGo pathway architecture is the direct biological inspiration for ARC-030's symmetric sub-channel design. Transfer risk is relatively low: the functional principle that behavioral balance requires both approach and avoidance pathways to be active is substrate-independent and well-established. The main gap is scale -- from 2-choice RL to multi-step trajectory planning -- which reduces confidence from the source quality ceiling.
