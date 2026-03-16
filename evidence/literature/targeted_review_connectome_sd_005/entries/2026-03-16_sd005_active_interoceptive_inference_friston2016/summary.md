# Literature Summary: 2026-03-16_sd005_active_interoceptive_inference_friston2016

## Claims Tested

- `MECH-069`
- `MECH-070`

## Source

- Friston KJ, FitzGerald T, Rigoli F, Schwartenbeck P, Pezzulo G (2017). *Active interoceptive inference and the emotional brain*. Philosophical Transactions of the Royal Society B.
- DOI: `10.1098/rstb.2016.0007`
- URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC5062097/`

## Source Wording

The brain maintains distinct generative models for interoceptive (internal body state: visceral, homeostatic) and exteroceptive (external world: visual, auditory, tactile) signals. These generate structurally separate prediction error streams — interoceptive prediction errors are minimized by autonomic reflexes and allostatic behaviour, while exteroceptive prediction errors are minimized by perception and action. Emotion arises from interoceptive inference contextualized by exteroceptive cues. The two streams converge but are not identical: collapsing them would confuse body-state regulation with world-model updating.

## REE Translation

**SD-005 (self/world latent split)**: z_self (proprioceptive/interoceptive, E2 domain) and z_world (exteroceptive, E3 domain) correspond directly to the interoceptive vs exteroceptive generative model split. The biological architecture validates the V3 decision to separate these as distinct encoder heads — they serve structurally different functions (body regulation vs world modeling) and generate incommensurable error signals.

**MECH-069 (incommensurable error signals)**: Interoceptive and exteroceptive prediction errors are not reducible to each other; minimizing one does not minimize the other. In REE terms: E1 sensory prediction error, E2 motor-sensory error (z_self), and E3 harm/goal error (z_world) correspond to distinct prediction error streams with distinct targets. Collapsing them into a shared z_gamma (as in V1/V2) produces the credit misattribution problem that motivates SD-005.

**MECH-070 (E2 as conceptual-sensorium motor model with extended horizon)**: The exteroceptive generative model (z_world) must accommodate longer prediction horizons than the motor/proprioceptive model (z_self) — world-state consequences of actions extend beyond immediate motor consequences. This supports E2's rollout_horizon > E1's prediction_horizon architectural decision.

## Caveat

Friston's active inference framework is a normative model. The specific architectural instantiation (separate encoder heads, z_self vs z_world dimensions) is a REE design choice, not directly stated in the source. The claim that these streams correspond to distinct thalamic circuits (relevant to ARC-023) requires additional literature support.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.75`
