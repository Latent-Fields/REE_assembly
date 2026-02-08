Depth–Phase Coordinate System (REE Canonical Specification)

Status

Normative architectural specification
This document defines required coordinate axes and gating constraints used across all REE modules.

⸻

1. Overview

REE computations are defined over three orthogonal coordinates:
	•	Temporal depth (τ-depth) — prediction horizon
	•	Representational depth (ρ-depth) — abstraction height in the latent stack
	•	Phase (φ) — routing, binding, and commitment eligibility regime

A REE state, candidate, or path must not be considered well-formed unless it is explicitly tagged with all three.

\text{REE Token} := \langle z \mid \tau, \rho, \phi, \pi \rangle

Where:
	•	z = latent content
	•	\tau = temporal depth
	•	\rho = representational depth
	•	\phi = phase / control mode
	•	\pi = precision (confidence / gain proxy)

⸻

2. Temporal Depth (τ-depth)

Definition

Temporal depth is the effective time horizon over which a model’s predictions are integrated and expected to remain coherent.

Temporal depth determines:
	•	update rate
	•	error integration window
	•	eligibility for action coupling

Canonical τ bands

τ label	Description
γ (gamma)	Immediate transitions, sensory–motor glue
β (beta)	Action–outcome loops, affordances
θ (theta)	Episode-scale coherence, replay, sequencing
δ (delta)	Slow context, narrative drift, mode stability

Architectural invariant

Predictions, errors, and confidence must not be mixed across τ bands without an explicit projection or aggregation operator.

⸻

3. Representational Depth (ρ-depth)

Definition

Representational depth is the abstraction height within a latent hierarchy used to encode state.

ρ-depth is not time.
It reflects compression, invariance, and semantic distance from raw sensory detail.

Canonical ρ strata (conceptual)

ρ level	Characteristics
shallow	Concrete, modality-bound, detail-rich
mid	Relational, compositional, task-state
deep	Schema-like, invariant, value / identity-adjacent

Implementation may use discrete labels or indexed layers (ρ = 0…N), but projections between depths must be explicit.

Architectural invariant

Projections from deeper ρ to shallower ρ must be lossy and constrained.
Deep abstractions may not directly masquerade as high-certainty sensory states.

⸻

4. Phase (φ): Routing and Eligibility Control

Definition

Phase is a control-plane primitive that governs:
	1.	which representations may bind,
	2.	which messages may propagate,
	3.	which candidates are eligible for commitment.

Phase is not metadata.
It is a routing and gating key.

Canonical φ regimes (functional)

φ label	Functional meaning
TASK	Externally anchored, action-coupled
DMN (Default Mode Network-like)	Internal generative simulation
OFFLINE	Replay / consolidation, no action coupling

Additional φ regimes may be defined, but each must specify its eligibility rules.

Safety-critical invariant

No commitment or motor coupling may occur unless φ explicitly permits it.

⸻

5. The Depth Matrix (τ × ρ), gated by φ

Definition

For each φ regime, define an allowed region in τ × ρ space:

M_\phi \subseteq \{(\tau,\rho)\}

Tokens outside M_\phi may be computed or simulated, but are ineligible for E3 commitment.

⸻

Example eligibility regions (illustrative)

φ = TASK
	•	Commitment-eligible:
	•	(β, ρ_mid)
	•	(γ, ρ_shallow)
	•	Simulation-only:
	•	(θ, ρ_mid)
	•	Prohibited from commitment:
	•	(δ, ρ_deep)

φ = DMN
	•	Simulation-allowed:
	•	(θ, ρ_mid / ρ_deep)
	•	(δ, ρ_deep)
	•	Action coupling prohibited:
	•	(γ, ρ_shallow)
	•	(β, ρ_mid)

φ = OFFLINE
	•	Replay allowed across τ and ρ
	•	Commitment edge disabled entirely

⸻

6. Module-specific responsibilities

E1 — Persistent Predictive Substrate
	•	Primary axis: ρ-depth
	•	Maintains multiplexed latent fields across abstraction levels
	•	Phase gates which ρ bands participate downstream

E1 output tags:
\langle z \mid \rho, \phi \rangle
(optional preferred τ target)

⸻

E2 — Fast Forward Predictor
	•	Primary axis: τ-depth
	•	Evolves predictions at multiple temporal horizons
	•	Samples E1 selectively across ρ based on τ and φ

E2 output tags:
\langle z \mid \tau, \rho, \phi, \pi \rangle

E1 multiplexing = many meanings
E2 multiplexing = many futures

⸻

Hippocampal Path Generator (mapping + sequencing)

Path definition
A hippocampal path P is an ordered sequence:

P = [s_0, s_1, \dots, s_k]

Each state token:
s_i := \langle z_i \mid \tau_i, \rho_i, \phi_i, \pi_i \rangle

Interpretation
	•	Paths encode coherent traversals of τ × ρ space under φ
	•	They are viability traces, not plans

Required constraint
Paths generated under φ = DMN or φ = OFFLINE must not directly enter E3 commitment without a φ transition and re-validation against M_\phi.

⸻

E3 — Trajectory Selection
	•	Consumes only commitment-eligible tokens
	•	Selection occurs after φ-gated τ×ρ validation
	•	E3 cannot override eligibility decisions

⸻

7. Canonical Gating Function

All commitment decisions must pass through:

Eligibility = G(\tau, \rho, \phi, \pi, context)

Where:
	•	G is authoritative
	•	E3 may select among commit_ok
	•	E3 may not promote simulate_only

⸻

8. Failure Mode Interpretation (non-normative)

Many pathological states arise from illegal bindings in τ × ρ under inappropriate φ:
	•	Impulsivity: shallow ρ + short τ + TASK φ
	•	Rumination: deep ρ + short τ + unresolved φ
	•	Mania / psychosis: deep ρ + long τ + TASK φ
	•	Healthy imagination: deep ρ + long τ + DMN φ

⸻

9. Design Rationale (brief)
	•	Separating τ and ρ prevents abstraction being conflated with time
	•	Phase gating allows rich internal simulation without reckless action
	•	Explicit tagging enables auditability, safety constraints, and modular extension

⸻

10. References within REE

This specification is normative for:
	•	E1.md
	•	E2.md
	•	latent_stack.md
	•	control_plane.md
	•	E3.md

All inter-module messages must conform to this coordinate system.
