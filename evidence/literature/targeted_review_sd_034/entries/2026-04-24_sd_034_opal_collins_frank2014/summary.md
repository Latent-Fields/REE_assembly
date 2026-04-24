# Collins & Frank 2014 -- Opponent Actor Learning (OpAL)

## Source
Collins AGE, Frank MJ. Opponent actor learning (OpAL): modeling interactive effects of striatal dopamine on reinforcement learning and choice incentive. Psychological Review 121(3):337-366. DOI: 10.1037/a0037015

## Finding
OpAL formalises a dual-actor striatal architecture: a Go population (D1-expressing direct pathway) learns predominantly from positive prediction errors, a NoGo population (D2-expressing indirect pathway) learns predominantly from negative prediction errors. Dopamine state modulates the balance between them, and this single architecture accounts for dopaminergic effects on learning, choice incentive, exploration-exploitation balance, and task-set (dis)engagement across a wide range of published datasets including probabilistic RL, effort-based choice, and motor skill learning.

## Why it maps to SD-034
SD-034 requires two outputs from the closure operator on successful rule-state satisfaction:
1. release of the bistable commitment latch (MECH-090 BetaGate)
2. a temporary No-Go bias on re-entry to the just-completed rule / action class (MECH-260)

OpAL's D2/NoGo population is the canonical biological substrate for (2). The paper explicitly discusses task-set disengagement as one of the functions the architecture supports, which is SD-034's target phenomenon. The mapping is at the architectural-prerequisite level: OpAL shows the substrate on which SD-034's No-Go output is implementable, not the closure-detector itself.

## Confidence: 0.55 (mixed)
- source_quality 0.85 (Psych Rev, canonical model, >1000 citations)
- mapping_fidelity 0.50 (substrate only; closure-detection step outside model scope)
- transfer_risk 0.55 (REE's MECH-260 is at a different level of abstraction than D1/D2 opponency)

## Key limitations
- OpAL is a computational model, not direct neural recording. Accepting OpAL's architecture is accepting a model assumption.
- The closure operator per se (the detector that fires on rule satisfaction and emits a release signal) is not in OpAL. OpAL describes what happens to the value representations after a choice / outcome; it does not describe when to stop evaluating.
- REE implements action-class suppression at the DACCAdaptiveControl level (action_history FIFO), not at a D1/D2 striatal level. If the critical biology is striatal dopamine dynamics, REE may be at the wrong abstraction level.

## Failure signatures
- If closure-release is implemented through a top-down cortical mechanism that bypasses D1/D2, OpAL is the wrong substrate.
- If the biological implementation of action-class No-Go depends on D2 LTD timescales that REE does not model, the REE-OpAL mapping fails at the dynamics level.
- OpAL's disengagement dynamics are smooth gradient effects; if closure is a discrete event ("done" token), the mapping is at best a coarse approximation.
