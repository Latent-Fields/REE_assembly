# Path Authority And Interrupts

**Claim Type:** mechanism_hypothesis  
**Scope:** Path authority, interruptibility, and commitment pressure  
**Depends On:** ARC-005, ARC-003, ARC-008  
**Status:** provisional  
**Claim ID:** MECH-005
<a id="mech-005"></a>

---

Source: `docs/processed/legacy_tree/architecture/path_authority_and_interrupts.md`


Norepinephrine: Path Authority, Interruptibility, and Commitment Pressure

(Proposed file: path_authority_and_interrupts.md)

⸻

Overview

In REE, all temporal depths (τ bands) operate continuously and coherently.
There is no switching on or off of τ bands.

Instead, a norepinephrine-like control signal (ν) modulates:
	•	which predictions and paths are allowed to influence commitment,
	•	how interruptible the current trajectory is, and
	•	how strongly post-commit errors drive learning and reorganisation.

ν is therefore a path-authority and commitment-pressure signal, not a clock selector and not a learning signal.

⸻

Core Claim (Normative)

Norepinephrine does not select temporal depth.
It modulates the authority, interruptibility, and commitment pressure of paths derived from nested τ-scale predictions.

All τ bands run; ν controls what must now matter.

⸻

The Imperative to Commit

REE assumes an irreversible temporal arrow:
	•	Time advances.
	•	The system must act or continue acting.
	•	Inaction is itself a commitment to trajectory persistence.

Therefore:
	•	Commitment is unavoidable.
	•	The question is not whether to commit, but how tightly the system is bound to its current path, and how costly deviation is allowed to be.

ν exists to regulate this pressure.

⸻

Functional Definition

Let:
	•	P_{current} = currently committed trajectory
	•	\{P_i\} = candidate future extensions (θ-scale paths)
	•	\nu = norepinephrine-like signal
	•	\phi = control mode
	•	\tau bands = nested predictors producing constraints and errors

ν modulates path authority, not prediction generation.

⸻

What ν Does (Precisely)

1. Path Authority Weighting

ν controls how strongly the system privileges:
	•	continuation of the current path,
	•	recently validated past paths,
	•	newly generated alternative paths.

High ν:
	•	recent path endings dominate
	•	deviation is costly
	•	commitment becomes “sticky”

Low ν:
	•	alternative paths gain voice
	•	branching is tolerated
	•	commitment is more exploratory

Formally (conceptual):

Authority(P_i) \propto A(P_i) \cdot g(\nu, context)

Where A(P_i) is coherence-based viability, not reward.

⸻

2. Interruptibility and Reorientation

ν controls whether local prediction errors (γ/β) are allowed to:
	•	remain local updates, or
	•	trigger θ-scale path reevaluation.

High ν:
	•	small mismatches can force reorientation
	•	rapid abandonment of failing paths

Low ν:
	•	local errors are absorbed
	•	the system “stays the course”

This is not learning; it is allocation of attention and urgency.

⸻

3. Commitment Pressure and Post-Commit Error Salience

Once a commitment is made:
	•	prediction errors after commitment carry special status
	•	these errors are uniquely informative about:
	•	model adequacy
	•	action viability
	•	environmental volatility

ν modulates how much post-commit error propagates upward:
	•	High ν → post-commit errors strongly drive θ-level restructuring
	•	Low ν → post-commit errors are damped, treated as noise

This captures a crucial biological asymmetry:

Errors after action matter more than errors before action.

⸻

What ν Explicitly Does Not Do

Architectural prohibitions:
	•	ν does not update precision registers (πτ)
	•	ν does not encode prediction error
	•	ν does not select τ bands
	•	ν does not determine value or reward

Any architecture where stress or surprise directly rewrites confidence is already collapsed.

⸻

Interaction with Phase (φ)

ν is permitted to influence φ transitions.

Examples:
	•	sustained high ν → φ forced into TASK / ALERT
	•	sustained low ν → φ permits DMN-like simulation
	•	extreme ν → φ may force abort / reset

φ changes alter which τ×ρ combinations are eligible for commitment, but τ bands themselves continue running.

⸻

Relationship to Nested τ Bands (Clarified)

Key invariant:

γ, β, θ, and δ predictions coexist continuously.

ν does not:
	•	enable or disable these predictors.

ν does:
	•	weight their influence on:
	•	path extension,
	•	commitment persistence,
	•	escalation of error.

γ always updates perception.
β always updates affordances.
θ always generates candidate paths.
δ always constrains identity and narrative.

ν decides how hard the system must care, right now.

⸻

Failure Modes (Interpretive)
	•	Hypervigilance: ν chronically high → constant reorientation, no stability
	•	Perseveration: ν chronically low → failure to abandon incoherent paths
	•	Burnout: ν flattened → weak post-commit learning
	•	Chaotic switching: ν incorrectly coupled to precision

⸻

Design Rationale

Fragmenting:
	•	precision (dopamine-like, τ-scoped)
	•	path authority (norepinephrine-like, urgency-scoped)

allows REE to:
	•	act decisively without freezing,
	•	learn from consequences without panic,
	•	imagine freely without compulsive enactment.

This is a control architecture, not an optimisation trick.

⸻

Summary
	•	τ bands are nested and always active
	•	Commitment is inevitable as time advances
	•	ν modulates urgency, interruptibility, and path authority
	•	Post-commit errors are privileged learning signals
	•	ν never directly rewrites confidence or belief
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-005

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/path_authority_and_interrupts.md`
