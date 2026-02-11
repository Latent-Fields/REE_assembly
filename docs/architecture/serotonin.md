# Serotonin

**Claim Type:** mechanism_hypothesis  
**Scope:** Representational collapse and exclusivity control  
**Depends On:** ARC-005, ARC-008  
**Status:** provisional  
**Claim ID:** MECH-006
<a id="mech-006"></a>

---

Source: `docs/processed/legacy_tree/architecture/serotonin.md`


Serotonin: Representational Collapse, Exclusivity, and Plasticity

⸻

Status

Normative architectural specification

This document defines the role of serotonin-like modulation within the Reflective Ethical Engine (REE), specifying its operational function, formal constraints, and interaction with temporal depth (τ), representational depth (ρ), and commitment.

⸻

1. Overview

In REE, serotonin does not encode reward, error, urgency, or precision.
Instead, it regulates how exclusive representations must be, and how rapidly the system is required to collapse competing interpretations into a single narrative.

Serotonin-like modulation therefore controls:
	•	representational exclusivity vs coexistence
	•	speed and strength of interpretative collapse
	•	permission for revision at deeper representational levels
	•	plasticity of models after consequential evidence

⸻

2. Core Claim (Normative)

Serotonin regulates the collapse pressure and mutual exclusivity of representations across representational depths (ρ), including perceptual, narrative, and identity-level models.

High serotonin permits multiple, mutually incompatible interpretations to coexist.
Low serotonin enforces rapid selection and suppression of alternatives.

⸻

3. What Serotonin Is Not

Architectural prohibitions:
	•	serotonin does not encode prediction error
	•	serotonin does not encode reward or value
	•	serotonin does not determine action commitment
	•	serotonin does not select temporal depth (τ)
	•	serotonin does not override noradrenaline-mediated urgency

Serotonin never forces action.
It only governs how tightly interpretations are required to resolve.

⸻

4. Formal Variable

Let:
	•	\sigma \in [0,1] = serotonin-like modulation parameter
	•	higher \sigma → lower collapse pressure
	•	lower \sigma → higher collapse pressure

σ is a global but slow-moving control parameter, updated on longer timescales than dopamine or noradrenaline.

⸻

5. Representational Collapse Rule

At each representational depth \rho, REE maintains a set of candidate interpretations:

\mathcal{H}_\rho = \{h_1, h_2, \dots, h_n\}

Each hypothesis has:
	•	local support (from γ/β prediction consistency)
	•	coherence (from θ continuity)
	•	compatibility with δ constraints

Collapse condition

A hypothesis h_i becomes dominant only if:

Support(h_i) - Support(h_j) > C_\rho(\sigma) \quad \forall j \neq i

Where:
	•	C_\rho(\sigma) is a collapse threshold
	•	C_\rho increases monotonically with σ

Thus:
	•	high σ → large threshold → coexistence
	•	low σ → small threshold → rapid pruning

⸻

6. Effects Across Representational Depths

Shallow ρ (Perceptual Narratives)
	•	γ-level sensory updates continue normally
	•	β-level affordance parsing remains intact
	•	but multiple perceptual parses may coexist

Phenomenology:
	•	“seeing several versions of the same thing”
	•	pattern/figure/meaning all present at once

This is not sensory noise, but delayed interpretative collapse.

⸻

Mid ρ (Situational / Episodic Models)
	•	θ-level narratives remain plural
	•	incompatible future continuations tolerated
	•	path commitment deferred

Phenomenology:
	•	rich imagination
	•	metaphorical or symbolic thinking
	•	reduced urgency to resolve ambiguity

⸻

Deep ρ (Identity / Value Models)
	•	δ-level schemas lose exclusivity
	•	identity narratives become revisable
	•	belief rigidity decreases

Phenomenology:
	•	ego softening
	•	openness to reinterpretation
	•	insight without compulsion

⸻

7. Interaction with Commitment (E3)

Serotonin does not prevent commitment — time still advances.

Instead, serotonin affects:
	•	how many interpretations reach E3
	•	how strongly a single interpretation dominates
	•	how reversible commitments feel after enactment

High σ:
	•	E3 sees many viable paths
	•	commitment feels provisional
	•	post-commit revision is permitted

Low σ:
	•	E3 sees one dominant path
	•	commitment feels definitive
	•	revision is costly

⸻

8. Interaction with Post-Commit Learning

After commitment:
	•	dopamine-like signals weight prediction error (πτ)
	•	noradrenaline-like signals weight urgency and interruption
	•	serotonin gates how deeply these errors propagate

Formally:

DepthOfRevision \propto (1 - \sigma)
	•	high σ → shallow correction only
	•	low σ → deeper θ / δ revision allowed

Thus serotonin controls learning depth, not learning rate.

⸻

9. Interaction with Other Control Signals

Signal	Primary Role	Orthogonality
Dopamine-like	Precision (πτ)	Affects influence of error
Noradrenaline-like	Commitment pressure	Affects urgency & interruptibility
Serotonin-like	Collapse & exclusivity	Affects hypothesis pruning

No two signals write to the same register.

⸻

10. Failure Modes (Interpretive)
	•	Excessively high σ:
	•	perceptual multiplicity
	•	indecision
	•	reduced action salience
	•	Excessively low σ:
	•	rigidity
	•	compulsive certainty
	•	resistance to revision
	•	Mis-coupling with NA:
	•	panic + rigidity
	•	or drift + paralysis

⸻

11. Design Rationale

REE fragments control because:
	•	perception requires fast collapse most of the time
	•	imagination requires delayed collapse sometimes
	•	identity requires rare, protected collapse

Serotonin provides a single, principled lever to regulate this trade-off without conflating:
	•	urgency,
	•	reward,
	•	learning,
	•	or action.

⸻

12. Summary
	•	Serotonin regulates representational exclusivity
	•	It weakens or strengthens collapse pressure across ρ
	•	It allows perceptual, narrative, and identity multiplicity
	•	It gates depth of post-commit revision
	•	It never forces action or value
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-006

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/serotonin.md`
