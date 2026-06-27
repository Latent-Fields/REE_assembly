# Tonic dopamine, opportunity costs, and response vigour (Niv, Daw, Joel & Dayan, 2007)

**Claim under test:** MECH-451 — the intermediate channel-granularity falsifier. Specifically, the grounding of the "vigour/dopaminergic" channel as one of the finer separately-learnable control dimensions.

## What the paper did

Niv and colleagues built an average-reward reinforcement-learning model in which the agent chooses not only *which* action to take but also the *latency / vigour* with which to take it. In that formulation the long-run average reward rate acts as an opportunity cost: acting slowly forgoes reward at the prevailing rate, so the optimal vigour rises when the environment is rich. The authors argue this average-reward quantity is plausibly reported by **tonic** dopamine — computationally distinct from the **phasic** dopamine signal that carries reward-prediction error and drives discrete action selection.

## Key finding relevant to the claim

The paper's value for MECH-451 is its normative separation of two roles dopamine plays: a tonic signal that sets *how vigorously* to respond, and a phasic signal that shapes *which* response to select. That is precisely the kind of functional dissociation MECH-451 leans on — vigour as a separable control channel with its own computational job, not a redundant copy of the motor-value signal. If REE's gating layer is to learn that "different control functions matter in different states," vigour-as-opportunity-cost is a clean worked example of one such function.

## Mapping to REE

This is the closest of the four MECH-451 sources to REE's own substrate, because it *is* a reinforcement-learning formalism rather than a neural measurement — so the conceptual transfer risk is low (0.4). It grounds the vigour channel as a distinct controllable quantity. What it does **not** do is show that adding a separate vigour channel to a learned gating layer *improves* the conversion of non-motor influence into committed action; the improves-conversion question is simply out of scope for a normative-optimality result.

## Caveats and confidence

There is a genuine tension worth flagging for the record. The model collapses vigour into a *single global scalar* (the average reward rate). So at the vigour level it actually argues *for* compression — one scalar is normatively optimal, and that scalar is global rather than state-specific. If MECH-451 expected vigour itself to need fine sub-channels, this paper pushes back. The mapping is therefore "vigour is a separable channel" (supports) but "vigour needs finer granularity" (mildly weakens). I have logged it **supports** with mapping_fidelity 0.6 and confidence 0.6, with the single-scalar-sufficiency point recorded as a failure signature.
