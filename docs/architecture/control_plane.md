# Control Plane (Precision, Gain, and Mode Regulation)

**Claim Type:** architectural_commitment  
**Scope:** Precision routing, gain modulation, operating modes, and commitment gating  
**Depends On:** INV-008 (precision is routed and depth-specific), INV-009 (attention via precision modulation), INV-014 (separation of representation and regulation), [L-space](l_space.md), [E3](e3.md)  
**Status:** stable  
**Claim ID:** ARC-005
<a id="arc-005"></a>

---

## Role in REE

The control plane in the Reflective Ethical Engine (REE) governs **how the system operates**, not *what it represents*.
It modulates precision, gain, exploration, replay, and commitment thresholds across the architecture.

**Subsystem abstract (core claims):** ARC‑005 is the control-plane commitment itself, and MECH‑019/MECH‑039/MECH‑040
specify how modes emerge from channel space and how safety baseline vs volatility shapes arousal/readiness. MECH‑005
grounds fast interruptibility, and MECH‑002 anchors precision‑control analogues. Supporting mechanisms include MECH‑001,
MECH‑003, MECH‑004, MECH‑006, MECH‑007, and MECH‑008.

The control plane does **not**:
- overwrite representational content,
- select actions directly, or
- compute reward or value.

Its function is to tune information flow so that prediction, imagination, commitment, and learning occur in the appropriate regime.

---

<a id="mech-019"></a>
## Control Plane and Modes of Cognition (MECH-019)

The control plane should not be understood as a discrete chooser or decision module. Instead, it modulates modes of cognition by tuning gain, horizon, learning eligibility, and constraint enforcement across predictive systems.

Different cognitive modes (reactive, deliberative, habitual, reflective) emerge from how the control plane biases:
- which prediction horizons dominate,
- which errors are allowed to matter,
- which bindings become rigid or remain fluid,
- and which trajectories are allowed to accumulate learning.

From the outside, this can look like “choice.”
From the inside, it is better understood as continuous shaping of a landscape in which some paths stabilise and others decay.

Source: `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`

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
3. adjusts **exploration horizon and branching** in candidate rollouts (hippocampal, seeded by E2),
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
\alpha_S,\; g_S,\; \alpha_A,\; \kappa_{\text{commit}},\; \tau_{E2},\; H,\; N,\; \eta_{E1},\; \eta_{E2},\; g_{\text{replay}},\; b_{\text{completion}},\; m,\; a_{\text{base}},\; a_{\Delta},\; r_{\text{ready}},\; v_{\text{veto}}
\}
\]

Where (illustrative, not exhaustive):
- \(\alpha_S\): sensory prediction-error precision
- \(g_S\): sensory gain (attention-like modulation)
- \(\alpha_A\): action/policy precision
- \(\kappa_{\text{commit}}\): commitment threshold (E3)
- \(\tau_{E2}\): rollout temperature (hippocampal generator, seeded by E2)
- \(H\): rollout horizon
- \(N\): number of candidate futures
- \(\eta_{E1}, \eta_{E2}\): learning-rate rigidity/plasticity
- \(g_{\text{replay}}\): replay rate (hippocampal braid)
- \(b_{\text{completion}}\): pattern-completion bias
- \(m\): operating mode flag
- \(a_{\text{base}}\): arousal baseline (tonic availability)
- \(a_{\Delta}\): arousal volatility sensitivity (phasic change tracking)
- \(r_{\text{ready}}\): action readiness / motor gating bias
- \(v_{\text{veto}}\): hard interrupt threshold

The control plane updates \(\theta_{\text{tune}}\) continuously based on context, urgency, residue curvature, and predicted risk or harm.

Rollout temperature and horizon parameters refer to **hippocampal candidate generation** seeded by E2, not an independent
E2 rollout generator. E2 is a forward-prediction module; hippocampus chains those kernels into explicit rollouts.

Optional social coupling parameters (multi-agent):
- `lambda_empathy`: other-to-self coupling strength for harm/viability pruning.
- `g_social`: social attention gain for `OTHER_SELFLIKE` agents.
- `alpha_other`: precision assigned to inferred other-states.
- `v_other_veto`: whether other-harm can veto vs only affect ranking.

---

<a id="mech-039"></a>
## Channels vs Modes (MECH-039)

The control plane exposes **continuous control channels**. Modes are **stable regions in that channel space**, not
additional modules. Switching is a trajectory through channel space, sometimes forced by a high‑priority interrupt.

Examples of channels:
- Arousal baseline and volatility sensitivity
- Action readiness / motor gating bias
- Precision and gain routing
- Commitment threshold and interruptibility
- Replay/learning scheduling
- Hard veto / interrupt threshold

Examples of modes:
- Task‑engaged (high readiness, elevated sensory precision)
- Default‑Mode‑like (low readiness, high replay, low sensory precision)
- Emergency (high arousal, high readiness, high veto)

Hard veto is a **fast interrupt channel**, not a mode. It can force a transition even when the rest of the control
state still reflects a prior regime.

---

<a id="mech-040"></a>
## Safety Baseline vs Volatility (MECH-040)

Safety assessment is split into two control channels:
- **Baseline safety** (tonic): whether core viability remains within bounds.
- **Safety volatility** (phasic): how rapidly safety is changing.

Arousal should rise when baseline safety is low **or** volatility is high. Action readiness then depends on arousal
*and* predicted action value, while veto triggers when harm predictions cross a catastrophic threshold.

This keeps a stable safe state calm, but still reacts to sudden drops in safety or abrupt hazard signals.

---

## Relationship to E3

E3 instantiates the **decision logic** of the control plane.

- The **commitment gate** selects and stabilises a future trajectory.
- The **control plane** determines whether commitment is permitted, deferred, or suppressed, and how strongly prediction errors should influence learning.

E3 therefore acts as the *epistemic liability gate* of the system: it decides when outcomes become attributable and belief-updating.

---

## Operating modes

The control plane supports distinct operating regimes through coordinated tuning of parameters.
Modes are labels over stable regions of the control‑channel landscape, not additional control modules.

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

### Emotion as composite control regime (clarification)

“Emotion” in REE is not a primitive signal. It is a **phenomenological label** for a **composite control‑plane regime**
assembled from multiple channels (arousal baseline/volatility, readiness, veto thresholds, precision/gain, valence
weighting, and social coupling). Universal‑looking expressions likely reflect **stable, reusable channel configurations**
rather than single‑axis signals. Specific mappings (e.g., particular expressions ↔ specific neuromodulator levels) should
be treated as hypotheses and constrained by evidence, not as architectural primitives (see `serotonin.md`).

---

<a id="mech-042"></a>
## Telemetry Exposure Channels (MECH-042)

**Claim Type:** mechanism_hypothesis  
**Scope:** Low‑bandwidth exposure of internal control state for diagnostics and early training  
**Depends On:** ARC-005, MECH-039, MECH-040  
**Status:** candidate  
**Claim ID:** MECH-042

REE should expose **diagnostic telemetry channels** that report internal control‑plane state (precision profile,
arousal baseline/volatility, readiness, veto thresholds, mode regime). These channels are read‑only and do not
participate in selection. They exist to support early training, calibration, and safety diagnostics without
introducing new decision pathways or symbolic overrides.

This supports **developmental safety**: problems can be detected, addressed, and later reflected upon without
requiring severe destabilization or trauma to surface the underlying issue.

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
- Path memory and replay: `hippocampal_systems.md`
- Default Mode (internal generative mode): `default_mode.md`
- Ethical residue geometry: `residue_geometry.md`

---

## Open Questions

<a id="q-007"></a>
**Q-007 — Universal emotion/expression ↔ control‑channel mapping**  
Do universal‑looking expressions (e.g., victory/pride displays) correspond to **stable multi‑channel control regimes**
in REE, and if so which combinations of arousal, readiness, precision, valence, and social coupling best align with
observed universals? This remains an evidence‑constrained hypothesis, not an architectural primitive.

## Related Claims (IDs)

- ARC-005
- ARC-003
- ARC-004
- INV-008
- INV-009
- INV-014
- MECH-001
- MECH-019
- MECH-039
- MECH-040
- MECH-042
- Q-007

## References / Source Fragments

- `docs/processed/legacy_tree/docs/architecture/control_plane.md`
- `docs/processed/legacy_tree/architecture/control_plane.md`
- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
