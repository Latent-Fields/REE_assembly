# Precision Control

**Claim Type:** mechanism_hypothesis  
**Scope:** Precision control analogues and cognitive regimes  
**Depends On:** ARC-005, INV-008, ARC-004  
**Status:** provisional  
**Claim ID:** MECH-002
<a id="mech-002"></a>

---

Source: `docs/processed/legacy_tree/architecture/precision_control.md`

# Precision control (monoamine analogue)

REE uses depth-indexed precision gains \(\alpha_k\) to control how strongly errors at different depths shape belief and action.

## Minimal knobs

For each depth \(k\):

- `alpha_k` multiplies the prediction error term in training / inference.
- Optionally, `alpha_k` modulates sampling temperature (higher precision → lower entropy).

## Functional roles (analogue)

Precision control does not merely tune learning rates. It induces **qualitatively distinct cognitive regimes** by reshaping how and where temporal collapse, commitment, and exploration occur.

### Functional regimes (analogue)

- Dopamine-like (commitment / trajectory locking):
	Increases precision at action and policy depths.
	Promotes temporal collapse of a selected trajectory.
	Phenomenology: confidence, motivation, goal-directed flow.
	Pathology when excessive: over-commitment, mania, compulsivity.

- Noradrenaline-like (unexpected uncertainty / interrupt):
	Transiently increases gain on surprising inputs and resets prior expectations.
	Breaks existing phase-locks and suspends temporal collapse.
	Phenomenology: alarm, vigilance, attentional narrowing.
	Pathology when excessive: panic, hypervigilance, fragmentation.

- Acetylcholine-like (expected uncertainty / sensory precision):
	Increases precision at sensory depths (\(\alpha_\gamma\)) under expected noise.
	Forces perceptual updating against top-down prediction.
	Phenomenology: clarity, vividness, perceptual anchoring.
	Pathology when excessive: sensory overload, derealisation.

- Serotonin-like (anti-collapse / horizon widening):
	Reduces premature commitment by limiting precision escalation.
	Stabilises exploratory hippocampal rollouts across longer horizons.
	Phenomenology: patience, emotional buffering, tolerance of ambiguity.
	Pathology when excessive: apathy, blunted affect, indecision.

Design constraint: expected uncertainty (ACh-like) must be separated from unexpected uncertainty (NE-like); they are
distinct control channels, not a single precision scalar.

<a id="mech-043"></a>
## Dopamine Precision‑Weighting (MECH-043)

**Claim Type:** mechanism_hypothesis  
**Scope:** Dopamine-like modulation of precision-weighting for unsigned prediction errors  
**Depends On:** ARC-005, INV-008, MECH-003  
**Status:** provisional  
**Claim ID:** MECH-043

Dopamine‑like signals should modulate the **precision weighting** of unsigned prediction errors, shaping learning and
commitment without becoming a scalar reward objective. Misallocation of this precision is a plausible mechanism for
hallucination‑like failures.

⸻

Precision as a controller of temporal experience

Precision allocation determines whether temporally displaced predictions are:
- Collapsed into a lived present (high action-depth precision),
- Held in exploratory suspension (balanced precision),
- Or fragmented into competing, incoherent trajectories (misallocated precision).

Thus, shifts in precision do not merely alter accuracy or learning speed.
They alter:
- Whether a unitary “now” is constructed,
- How tightly perception is bound to action,
- How emotion and value predictions bias trajectory selection,
- And whether experience feels continuous, urgent, fragmented, or unreal.

---

## Signed Harm/Benefit PE Precision (Implementation Sketch)

This section operationalizes **MECH‑054** (see `control_plane.md`) in precision‑control terms.
It treats harm‑related and benefit‑related prediction errors as **distinct channels** with separate precision weights.

Let:
- \(e_H\) = harm‑related prediction error (from `HARM` / `HOMEOSTASIS` streams),
- \(e_B\) = benefit‑related prediction error (from `VALENCE` / reward‑proxy streams),
- \(\pi_H, \pi_B\) = precision weights for harm vs benefit channels.

Local updates (illustrative):

\[
\pi_H(t+1) = (1-\alpha_H)\pi_H(t) + \alpha_H f(|e_H(t)|, context)
\]
\[
\pi_B(t+1) = (1-\alpha_B)\pi_B(t) + \alpha_B f(|e_B(t)|, context)
\]

Where \(f\) is bounded and saturating, and \(\alpha_H, \alpha_B\) may differ by mode.

Usage:
- **Learning:** \( \Delta z \propto \pi_H e_H + \pi_B e_B \) (applied per channel, not collapsed into a scalar).
- **Commitment gating:** if \( \pi_H |e_H| \) exceeds a threshold, feed the aversive gate (MECH‑053) to suppress or
  delay commitment.
- **Unsigned precision:** dopamine‑like gain (MECH‑043) can scale the *overall* learning rate, while signed precision
  determines **which** errors dominate.

This keeps **hedonic tone** (μ/κ overlays), **valence vectors** (MECH‑035), and **signed PE precision** conceptually
distinct. See MECH‑055 in `control_plane.md` for the separation rule.

### Operational control state (LC/astrocyte aware)

To make control effects observable and calibratable, REE should expose explicit state variables:

- \(A_t\): tonic arousal baseline (maps to control-plane baseline channel, K7-like).
- \(N_t\): phasic volatility/imminence signal (maps to interrupt pressure, K8-like).
- \(R_t\): action readiness bias (maps to motor gating readiness, K9-like).
- \(C_t\): slow regulatory context integrator (astrocyte-like modulation field, tied to MECH-001).

Illustrative updates:
\[
K2_t = k2_0 + w_A A_t + w_N N_t + w_C C_t
\]
\[
K2_{H,t} = K2_t + \Delta_H,\qquad K2_{B,t} = K2_t + \Delta_B
\]
\[
K1_t = k1_0 + u_C C_t - u_O overload_t
\]
\[
K10_t = k10_0 - v_N N_t + v_S safety\_margin_t
\]

Interpretation:
- \(N_t\uparrow\) lowers the effective veto threshold (\(K10_t\downarrow\)) and increases interrupt propensity.
- \(C_t\) modulates slower plasticity/precision drift, capturing regulatory inertia rather than instant switching.
- \(K2_H\) and \(K2_B\) are channel-specific precision weights; they should not collapse back to a single valence scalar.

Telemetry requirement (MECH-042-aligned):
- Log \(A_t,N_t,R_t,C_t,K1_t,K2_t,K2_{H,t},K2_{B,t},K10_t\) per episode window.
- Log commitment breaks/interrupts with triggering channels and thresholds.
- Distinguish tonic drift from phasic spikes in diagnostics.

**Calibration note:** Quantitative tuning rules are intentionally deferred until the signal‑map wiring (MECH‑004) and
regulatory‑stack framing (MECH‑001) are clarified. The current separation rules are **invariant‑compatible scaffolding**,
not a final calibration protocol.

## Astrocyte-aware regulatory stack

**Note:** The above framing treats monoamines as direct control knobs. A more neuroscience-informed perspective reinterprets monoamines as **broadcast meta-regulatory signals** that bias a slower astrocytic regulatory substrate, which then modulates precision/gain/plasticity with spatial and temporal lags.

See `docs/astrocyte_aware_regulatory_stack/` for:

- Why monoamines are not direct knobs (astrocytes mediate their effects).
- How to model the slow regulatory field \(R(x,t)\) that produces \(\alpha_k(x,t)\).
- Implications for care budget, inertia, and sleep recalibration.

For REE-v0, the direct-knob model (above) is a valid simplification. Future implementations should account for the layered regulatory architecture documented in the astrocyte-aware module.
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-002
- MECH-043
- MECH-054
- MECH-035
- MECH-055

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/precision_control.md`
- `docs/thoughts/2026-02-11_habenula_signed_pe.md`
