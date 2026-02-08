# Temporal Dynamics and Phase Gating

**Claim Type:** architectural_commitment  
**Scope:** Temporal depth, representational depth, and phase-gated eligibility for commitment  
**Depends On:** INV-002 (coherence includes temporal binding), [L-space](l_space.md), [control plane](control_plane.md), [E3](e3.md)  
**Status:** provisional  
**Claim ID:** ARC-008
<a id="arc-008"></a>

---

## Overview

REE computations are defined over three orthogonal coordinates:
- Temporal depth (tau-depth): prediction horizon
- Representational depth (rho-depth): abstraction height in the latent stack
- Phase (phi): routing, binding, and commitment eligibility regime

A REE state, candidate, or path is well-formed only when tagged with all three:

\[
\text{REE Token} := \langle z \mid \tau, \rho, \phi, \pi \rangle
\]

Where:
- \(z\) = latent content
- \(\tau\) = temporal depth
- \(\rho\) = representational depth
- \(\phi\) = phase / control mode
- \(\pi\) = precision (confidence / gain proxy)

---

<a id="mech-021"></a>
## Fast/Slow Prediction and the Construction of “Now” (MECH-021)

Fast and slow predictive systems mirror cortical–cerebellar dynamics rather than hippocampal ones. Fast systems outrun the present and generate cheap, speculative predictions; slower systems stabilise the authoritative present.

Subjective “now” is not the current sensory timestamp. It is the control surface where predictions across multiple temporal scales are rendered actionable. Some learning signals are technically about the future, but they are felt as present because affordances across horizons re-centre on the same control window.

This allows:
- anticipatory learning,
- restraint before harm,
- and responsibility before consequence.

Learning eligibility can therefore be future-shifted while phenomenology remains grounded in the present.

Source: `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`

---

## Temporal depth (tau-depth)

Temporal depth is the effective time horizon over which a model's predictions are integrated and expected to remain coherent.
It determines update rate, error integration window, and eligibility for action coupling.

Canonical tau bands:
- \(\gamma\) (gamma): immediate transitions, sensory-motor glue
- \(\beta\) (beta): action-outcome loops, affordances
- \(\theta\) (theta): episode-scale coherence, replay, sequencing
- \(\delta\) (delta): slow context, narrative drift, mode stability

Architectural invariant: predictions, errors, and confidence must not be mixed across tau bands without an explicit
projection or aggregation operator.

---

## Representational depth (rho-depth)

Representational depth is the abstraction height within a latent hierarchy used to encode state.
It reflects compression, invariance, and semantic distance from raw sensory detail.

Canonical rho strata (conceptual):
- shallow: concrete, modality-bound, detail-rich
- mid: relational, compositional, task-state
- deep: schema-like, invariant, value / identity-adjacent

Architectural invariant: projections from deeper rho to shallower rho must be lossy and constrained.
Deep abstractions may not directly masquerade as high-certainty sensory states.

---

## Phase (phi): routing and eligibility control

Phase is a control-plane primitive that governs which representations may bind, which messages may propagate, and which
candidates are eligible for commitment. Phase is a routing and gating key.

Canonical phi regimes (functional):
- TASK: externally anchored, action-coupled
- DMN (Default Mode Network-like): internal generative simulation
- OFFLINE: replay / consolidation, no action coupling

Safety-critical invariant: no commitment or motor coupling may occur unless phi explicitly permits it.

---

## The depth matrix (tau x rho), gated by phi

For each phi regime, define an allowed region in tau x rho space:

\[
M_\phi \subseteq \{(\tau,\rho)\}
\]

Tokens outside \(M_\phi\) may be computed or simulated, but are ineligible for E3 commitment.

Example eligibility regions (illustrative):
- phi = TASK: commitment-eligible (beta, rho_mid) and (gamma, rho_shallow). Simulation-only (theta, rho_mid). Prohibited from commitment (delta, rho_deep).
- phi = DMN: simulation-allowed (theta, rho_mid / rho_deep) and (delta, rho_deep). Action coupling prohibited (gamma, rho_shallow) and (beta, rho_mid).
- phi = OFFLINE: replay allowed across tau and rho. Commitment edge disabled entirely.

---

## Module-specific responsibilities

E1 (Persistent Predictive Substrate): primary axis rho-depth. Maintains multiplexed latent fields across abstraction
levels. Phase gates which rho bands participate downstream.

E2 (Fast Forward Predictor): primary axis tau-depth. Evolves predictions at multiple temporal horizons. Samples E1
selectively across rho based on tau and phi.

Hippocampal path generator: paths encode coherent traversals of tau x rho space under phi. Paths generated under
phi = DMN or phi = OFFLINE must not directly enter E3 commitment without a phi transition and re-validation.

E3 (Trajectory Selection): consumes only commitment-eligible tokens. Selection occurs after phi-gated tau x rho
validation. E3 cannot override eligibility decisions.

---

## Canonical gating function

All commitment decisions must pass through:

\[
\text{Eligibility} = G(\tau, \rho, \phi, \pi, \text{context})
\]

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-008
- ARC-003
- ARC-004
- ARC-005
- INV-002
- MECH-021

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/depth_phase_spec.md`
- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
