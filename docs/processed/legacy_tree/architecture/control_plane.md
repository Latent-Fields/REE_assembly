# Control plane (precision, gain, and mode regulation)

> **📍 Canonical Location:** This content has been migrated to [`docs/architecture/control_plane.md`](../docs/architecture/control_plane.md) with formal claim typing and dependency tracking. This file is preserved for compatibility.

## Role in REE

The control plane in the Reflective Ethical Engine (REE) governs **how the system operates**, not *what it represents*.
It modulates precision, gain, exploration, replay, and commitment thresholds across the architecture.

The control plane does **not**:
- overwrite representational content,
- select actions directly, or
- compute reward or value.

Its function is to tune information flow so that prediction, imagination, commitment, and learning occur in the appropriate regime.

---

## Architectural necessity

Given REE constraints:
- perception completes at the shared sensory latent \(z_S\),
- belief update occurs only after commitment (E3),
- imagination must be possible without belief update,
- ethical residue \(\phi(z)\) must remain path dependent and non-optimisable,

there must exist a mechanism that:
1. regulates the **precision** of prediction errors at different depths,
2. controls **when commitment is possible or suppressed**,
3. adjusts **exploration horizon and branching** in fast rollouts,
4. schedules **replay and consolidation**, and
5. switches between operating modes (task-engaged, Default Mode–like, sleep/offline).

This mechanism is the control plane.

---

## Control surface


The control plane operates over a structured set of tunable parameters exposed by REE modules:

Control-plane modulation is **differential rather than global**: precision, gain, horizon, replay, and commitment parameters
may be increased in some subsystems while simultaneously decreased or stabilised in others.
There is no single global arousal or confidence variable; tuning is depth- and module-specific.

\[
\theta_{\text{tune}} = \{
\alpha_S,\; g_S,\; \alpha_A,\; \kappa_{\text{commit}},\; \tau_{E2},\; H,\; N,\; \eta_{E1},\; \eta_{E2},\; g_{\text{replay}},\; b_{\text{completion}},\; m
\}
\]

Where (illustrative, not exhaustive):
- \(\alpha_S\): sensory prediction-error precision
- \(g_S\): sensory gain (attention-like modulation)
- \(\alpha_A\): action/policy precision
- \(\kappa_{\text{commit}}\): commitment threshold (E3)
- \(\tau_{E2}\): rollout temperature
- \(H\): rollout horizon
- \(N\): number of candidate futures
- \(\eta_{E1}, \eta_{E2}\): learning-rate rigidity/plasticity
- \(g_{\text{replay}}\): replay rate (hippocampal braid)
- \(b_{\text{completion}}\): pattern-completion bias
- \(m\): operating mode flag

The control plane updates \(\theta_{\text{tune}}\) continuously based on context, urgency, residue curvature, and predicted risk or harm.

---

## Relationship to E3

E3 instantiates the **decision logic** of the control plane.

- The **commitment gate** selects and stabilises a future trajectory.
- The **control plane** determines whether commitment is permitted, deferred, or suppressed, and how strongly prediction errors should influence learning.

E3 therefore acts as the *epistemic liability gate* of the system: it decides when outcomes become attributable and belief-updating.

---

## Operating modes

The control plane supports distinct operating regimes through coordinated tuning of parameters.

### Task-engaged mode
- High sensory precision and gain
- Normal or lowered commitment threshold
- Limited replay
- Learning enabled

Used when accurate perception and timely action are required.

### Default Mode–like (internal generative) mode
- Reduced sensory precision
- Elevated replay and pattern completion
- Suppressed commitment (high \(\kappa_{\text{commit}}\))
- Learning and belief update suspended

Supports imagination, counterfactual exploration, autobiographical reflection, and planning without action.

### Sleep / offline mode
- Minimal sensory influence
- High replay scheduling
- Consolidation and structural reorganisation
- No commitment or belief update

Supports long-term integration while preserving ethical residue and perceptual corrigibility.

---

## Neuromodulatory analogy (functional, not literal)

Biological neuromodulatory systems can be understood as implementing aspects of such a control plane.
In REE, these are treated as **functional control channels**, not biological claims:

- Dopamine-like: commitment strength and policy precision
- Acetylcholine-like: sensory gain and attentional weighting
- Serotonin-like: model stability, patience, and resistance to impulsive updating
- Noradrenergic-like: urgency, interrupt, and rapid engagement
- Histamine-like: global availability and throughput (arousal)

These channels alter *how cognition runs*, not *what it represents*.

---

## Safety constraints

The control plane must satisfy:

1. **No representational overwrite**  
   Tuning alters influence and scheduling, not latent content.

2. **Commitment gating**  
   Belief update and ethical attribution occur only after E3 commitment.

3. **Residue preservation**  
   Replay and mode switching must not erase or flatten ethical curvature.

4. **Hypothesis tagging**  
   Outputs generated outside commitment are explicitly non-committal.

These constraints prevent imagination from becoming delusion and urgency from becoming compulsion.

---

## Interpretation

The control plane explains why emotion, arousal, and attention feel like changes in *how thinking works* rather than changes in belief.

It provides the mechanism by which the Self:
- remains coherent in the present,
- explores possible futures safely,
- commits under uncertainty, and
- learns responsibly from consequences.

---

## Cross-references

- Trajectory selection and commitment: `E3.md`
- Shared sensory latent and timescales: `latent_stack.md`
- Path memory and replay: `hippocampal_braid.md`
- Default Mode (internal generative mode): `default_mode.md`
- Ethical residue geometry: `residue_geometry.md`
