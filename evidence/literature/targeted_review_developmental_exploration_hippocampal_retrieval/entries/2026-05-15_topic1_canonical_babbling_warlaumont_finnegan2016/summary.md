# Learning to Produce Syllabic Speech Sounds via Reward-Modulated Neural Plasticity
**Warlaumont & Finnegan (2016), PLoS ONE** | DOI: 10.1371/journal.pone.0145096

## What the paper did

Computational model combining a spiking neural network, reinforcement-modulated STDP, and a human-like vocal tract to simulate the acquisition of canonical babbling. The model is rewarded when it produces auditorily salient sounds, consistent with caregiver contingent response data.

## Key findings

Canonical babbling frequency increases gradually as dopamine-modulated STDP in motor cortex learns to harness natural oscillatory dynamics for syllabic production. Critically, simulations of deafness and tracheostomy (blocking own-voice feedback) arrest development at pre-canonical babbling -- the agent gets stuck at a single low-diversity attractor. The reward signal required is self-referential (auditory salience of own output), not externally imposed.

## REE translation

This is the computational proof-of-concept for ARC-065's developmental bootstrapping claim. Motor exploration does not converge to a diverse repertoire by chance; it requires reward-shaping from the start. When the reward signal is absent (deafness) or blocked (tracheostomy), the system collapses to monostrategy. The mapping to REE is direct: action diversity generation requires an intrinsic reward signal to prevent repertoire collapse -- precisely the problem the monostrategy experiments (EXQ-561 cluster) reveal in the V3 substrate.

## Limitations

Simulation only; limited validation against longitudinal diversity trajectories in actual infant babbling. External reward (caregiver response) may not be the primary driver in low-CDS cultural contexts.

## Confidence reasoning

PLoS ONE computational; conceptually close to REE repertoire bootstrapping logic. Source quality moderate; mapping fidelity high. 0.70.
