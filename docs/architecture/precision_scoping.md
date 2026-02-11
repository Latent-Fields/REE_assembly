# Precision Scoping

**Claim Type:** mechanism_hypothesis  
**Scope:** Tau-scoped precision separation and update rules  
**Depends On:** INV-008, ARC-004  
**Status:** candidate  
**Claim ID:** MECH-003
<a id="mech-003"></a>

---

Source: `docs/processed/legacy_tree/architecture/precision_scoping.md`

τ-Scoped Precision: Update Rules and Separation

Overview

REE treats precision and confidence as the same control variable operating at different temporal depths (τ).
To prevent pathological coupling, precision MUST be τ-scoped, with explicit, lossy projections between τ bands.

There is no global precision scalar in REE.

⸻

Definitions

Let:
	•	\tau \in \{\gamma, \beta, \theta, \delta\} be temporal depth
	•	\varepsilon_\tau be prediction error at depth τ
	•	\pi_\tau be precision (gain / confidence weight) at depth τ
	•	z_\tau be the state estimate at depth τ

A τ-scoped state token is:

\langle z \mid \tau, \rho, \phi, \pi_\tau \rangle

⸻

Core Rule (Normative)

Precision values at different τ depths MUST be stored, updated, and applied independently.

Formally:

\pi_\gamma \neq \pi_\beta \neq \pi_\theta \neq \pi_\delta

No module may:
	•	directly overwrite another τ’s precision
	•	aggregate precisions without a projection operator
	•	treat precision as τ-agnostic metadata

⸻

Local Precision Update (Phasic-like)

At each τ depth, precision updates locally from error statistics:

\pi_\tau(t+1) = (1 - \alpha_\tau)\,\pi_\tau(t) + \alpha_\tau\,f(|\varepsilon_\tau(t)|, context)

Where:
	•	\alpha_\tau is τ-specific (γ ≫ β ≫ θ ≫ δ)
	•	f is bounded and saturating
	•	update is event-locked at γ/β and slowly integrated at θ/δ

Interpretation:
	•	γ / β precision behaves phasically (fast, sharp)
	•	θ / δ precision behaves tonically (slow, stabilising)

⸻

Precision Application

Precision modulates influence, not truth.

At each τ depth:

\Delta z_\tau \propto \pi_\tau \cdot \varepsilon_\tau

Crucially:
	•	γ precision weights sensory/motor corrections
	•	β precision weights action–outcome learning
	•	θ precision weights trajectory relevance
	•	δ precision weights model persistence and narrative stability

⸻

Cross-τ Projection (Explicit and Lossy)

Cross-τ influence MUST pass through a projection operator:

\pi_{\tau_j} \leftarrow \mathcal{P}_{\tau_i \rightarrow \tau_j}(\pi_{\tau_i}, history, context)

Properties of \mathcal{P}:
	•	Slow (many samples required)
	•	Directional (usually short → long τ only)
	•	Lossy (cannot preserve sharp spikes)
	•	Context-gated (φ-dependent)

Examples:
	•	repeated β-scale precision → gradual θ-scale confidence
	•	sustained θ-scale confidence → very slow δ-scale belief stability
	•	γ-scale precision never projects directly to δ

⸻

Prohibited Operations (Hard Constraints)

The following are architectural violations:
	•	using γ-scale surprise to directly raise δ-scale certainty
	•	collapsing πγ…πδ into a single “attention” scalar
	•	letting E3 read untyped precision
	•	allowing precision to bypass φ gating

These violations correspond to known failure modes:
	•	impulsivity
	•	delusional certainty
	•	manic over-commitment
	•	reward hacking

⸻

Biological Correspondence (Non-normative note)

This separation mirrors:
	•	phasic dopamine → πγ / πβ
	•	tonic dopamine → πθ / πδ
	•	anatomical separation enforcing τ isolation

REE encodes this by design, not by accident.

Expected vs unexpected uncertainty should be treated as **separate control inputs** (ACh‑like vs NE‑like), rather than
collapsed into a single precision signal.

⸻

Summary (for quick reference)
	•	Precision is one variable, many τ-scoped registers
	•	Phasic vs tonic = short-τ vs long-τ integration
	•	Cross-τ effects require explicit, slow projection
	•	Precision modulates influence, not truth
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-003

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/precision_scoping.md`
