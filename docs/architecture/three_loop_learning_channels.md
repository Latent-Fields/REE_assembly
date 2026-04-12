---
nav_exclude: true
---

# Three-Loop Learning Channel Separation

**Source thought:** `docs/thoughts/2026-03-14_three_bg_systems_error_signals.md`

---

<a id="arc-021"></a>
## Three BG-like cortico-striatal loops require distinct learning channels (ARC-021)

**Claim Type:** architectural_commitment
**Subject:** basal_ganglia.three_loop_learning_channel_separation
**Status:** candidate
**Claim ID:** ARC-021

The REE architecture is organised around three functionally distinct cortico-striatal-like learning loops, each defined by a different error signal and a different level of representational abstraction. These are:

1. **Sensorium loop** — learns from sensory prediction error: the mismatch between predicted and observed sensory latent state. Corresponds to E1 in REE. Continuous; not gated by action. Maintains the "perceived present" — what the system expects to sense given current context.

2. **Action-enacting loop** — learns from motor-sensory error on the *conceptual sensorium*: the mismatch between predicted and actual effect of an action on the unified latent space `z_gamma` (where coherent sensory objects form). Corresponds to E2 in REE. Gated by action; operates at the level of objects, not raw sensory features.

3. **Planning-gates loop** — learns from harm and goal errors: realized harm vs. expected harm, goal achievement vs. goal deviation. Corresponds to E3 and HippocampalModule in REE. Outcome-level; gated by trajectory commitment; the residue field accumulates harm signal across trajectories.

These three loops are the structural substrate of the three-gate BG architecture (Q-019 model B). ARC-021 is the claim that this separation is *required* — not optional optimization — because the error signals are incommensurable (MECH-069).

---

<a id="mech-069"></a>
## Sensory prediction error, motor-sensory error, and harm/goal error are incommensurable (MECH-069)

**Claim Type:** mechanism_hypothesis
**Subject:** latent_stack.three_loop_error_signal_incommensurability
**Status:** candidate
**Claim ID:** MECH-069

The three error signals that drive learning in the REE architecture are incommensurable: no one of them can be derived from or collapsed into another without loss of the information each carries.

- **Sensory prediction error** (E1): "I failed to predict the sensory world correctly." This error carries no information about which action caused the mismatch, or whether the mismatch was harmful. It indexes world-model fidelity.

- **Motor-sensory error** (E2): "My action had a different effect on latent sensory objects than I expected." This error requires knowing *what action was taken* — it is action-conditioned. It indexes motor-model fidelity. It does not carry information about whether the effect was harmful or goal-relevant.

- **Harm/goal error** (E3 + residue): "This trajectory caused harm / failed to achieve the goal." This error requires knowing the outcome of a committed trajectory. It indexes ethical and purposive fidelity. It does not carry information about sensory prediction quality or motor prediction quality.

**Implication:** collapsing these signals into a single scalar prediction error — as a naive world-model architecture would — misattributes credit across all three. A sensory mismatch would incorrectly update motor weights; a harmful outcome would incorrectly update sensory weights. The separation is not for efficiency; it is for correct credit assignment.

**Relationship to MECH-058:** timescale separation between E1 and E2 (MECH-058) is a *consequence* of incommensurability. Different error signals have different natural timescales — sensory prediction error is frequent and small; motor-sensory error is sparser (only at action steps); harm/goal error is slowest (only at trajectory completion). The timescale separation follows from the error signal separation, not the reverse.

**Relationship to SD-003:** the gap `E2(z_t, a_actual) − E2(z_t, a_cf)` is the agent's causal signature on the object world. When this gap is near zero for all counterfactual actions, the latent transition was environment-caused; when the gap is large, the agent's action was causally responsible. This E2-derived causal signature is the correct substrate for self-attribution precisely because E2's error signal is action-conditioned and operates at the level of coherent objects — not raw sensory streams, not harm outcomes.

---

<a id="mech-070"></a>
## E2 is a conceptual-sensorium motor model with planning horizon exceeding E1 (MECH-070)

**Claim Type:** mechanism_hypothesis
**Subject:** latent_stack.e2_conceptual_sensorium_motor_model
**Status:** candidate
**Claim ID:** MECH-070

E2 is NOT a raw sensory predictor. It is a motor model of the *conceptual sensorium* — the unified latent space `z_gamma` where all sensory modalities have been bound into coherent objects by the LatentStack.

**E2 specifics:**
- Input: `(z_gamma_t, action_t)` — latent object-world state plus action
- Output: `z_gamma_{t+1}` — predicted next object-world state
- Error signal: MSE(`E2(z_t, a_t)`, `actual z_gamma_{t+1}`) — motor-sensory mismatch at the object level
- Training: supervised on `(z_t, action, z_{t+1})` transition tuples recorded from actual execution

**Why E2's planning horizon must exceed E1's:**

E1 predicts the "perceived present" by projecting the sensory latent stream a short distance forward without action conditioning — it estimates what the system will sense if it continues in its current context. E2 predicts the causal chain of a motor act on the object world, which unfolds over a longer interval. For E2 to be useful for trajectory planning, it must be able to simulate further ahead than E1's associative horizon:

- E1 `prediction_horizon`: default 20 steps — how far ahead E1 simulates sensory context
- E2 `rollout_horizon`: default 30 steps — how far ahead E2 simulates motor consequences

The planning horizon ordering E2 > E1 is architecturally required: if E2 only predicted as far as E1's perceived present, trajectory planning would offer no planning advantage over simply following the sensory stream.

**HippocampalModule chaining:**

HippocampalModule chains E2 rollout kernels into even longer plans (hippocampal planning horizon >> E2's rollout horizon). E2 provides the motor-sensory kernels; the hippocampus chains them into multi-step trajectories navigated under residue-field terrain (ARC-018, MECH-033). The kernel metaphor in MECH-033 refers to E2's single-transition outputs being *composed* into longer rollouts — not to E2's individual planning horizon being short.

**Connection to ARC-021:** E2 is the "action-enacting loop" of the three-loop architecture. Its error signal (motor-sensory mismatch on z_gamma) is incommensurable with E1's sensory prediction error and E3's harm/goal error (MECH-069). This grounds why E2 must be trained separately from E1, with its own optimizer and its own transition buffer recording `(z_t, action, z_{t+1})` tuples.
