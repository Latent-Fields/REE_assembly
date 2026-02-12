TRAJECTORY-LEVEL RESIDUE VS REPRESENTATIONAL DISTORTION

Status: Thought Intake (Not Promoted)
Layer: Architectural Mechanism Placement / Safety Geometry

Related: ARC-013 (Residue Geometry), ARC-018 (Hippocampal Rollouts), ARC-003 (E3 Commitment), ARC-004 (L-Space)

⸻

1. Motivation

REE separates:
	•	E1/E2 — predictive representation (latent generative structure)
	•	Hippocampal rollout system — trajectory indexing and feasibility mapping
	•	E3 — trajectory commitment under control-plane precision gating

This separation allows asymmetric encoding of danger:

Dangerous states may remain richly represented in E1/E2
While trajectories leading to those states become increasingly inaccessible.

This raises a design question:

Where should residue primarily accumulate?
	1.	In latent representational geometry (E1/E2 distortion)?
	2.	In trajectory-space gating (hippocampal/E3 suppression)?
	3.	Hybrid?

This document proposes that trajectory-level accumulation may preserve epistemic richness while constraining behaviour.

⸻

2. Core Hypothesis

Knowledge and affordance should be separable.

It may be desirable that:
	•	The system can model dangerous states in detail.
	•	But cannot easily enact trajectories that lead to them.

Therefore:

Residue should preferentially operate at the level of:
	•	Trajectory feasibility
	•	Commitment thresholds
	•	Path authority gating

Rather than primarily distorting representational latent space.

⸻

3. Architectural Framing

E1 / E2 (Predictive Substrate)

Responsibilities:
	•	Detailed generative modelling
	•	Counterfactual simulation
	•	Coherence maintenance

If residue strongly distorts this layer:
	•	Predictive accuracy may degrade
	•	Generalisation may suffer
	•	Epistemic blind spots may emerge

⸻

Hippocampal Rollouts (ARC-018)

Responsibilities:
	•	Path indexing
	•	Contextual feasibility mapping
	•	Episodic trajectory filtering

Residue accumulation here could:
	•	Increase cost of specific path manifolds
	•	Reduce sampling probability of harmful trajectories
	•	Leave representational modelling intact

⸻

E3 (ARC-003)

Responsibilities:
	•	Commitment gating
	•	Precision thresholding
	•	Converting hypothetical futures into enacted plans

Residue at this layer could:
	•	Raise commitment thresholds for harmful trajectories
	•	Trigger veto or hard constraint mechanisms

⸻

4. Design Options

Option A — Latent Distortion

Residue modifies L-space geometry directly.

Consequences:
	•	Harmful states become geometrically “repelled”
	•	Representation shifts over time
	•	Risk of predictive degradation

Failure modes:
	•	Over-generalisation of avoidance
	•	Loss of modelling fidelity
	•	Catastrophic blind spots

⸻

Option B — Trajectory-Level Residue

Residue modifies:
	•	Hippocampal trajectory cost
	•	E3 selection scoring
	•	Commitment thresholds

Consequences:
	•	Detailed knowledge preserved
	•	Behaviour selectively constrained
	•	Clean separation of epistemics and enactment

Failure modes:
	•	Possible insufficient generalisation
	•	Risk of loophole trajectories

⸻

Option C — Hybrid
	•	Mild latent bias
	•	Strong trajectory gating

Consequences:
	•	Balance between epistemic fidelity and behavioural constraint

⸻

5. Developmental Implication

Under the Self-First developmental roadmap:
	•	Early stages (self-viability learning) should prefer trajectory-level residue.
	•	Representational distortion should be avoided until predictive stability is demonstrated.
	•	Social residue (later stages) may operate similarly: suppress enactment without degrading world-model fidelity.

⸻

6. Testable Experimental Plan

Design ablation experiments in ree-v1-minimal:

Conditions:
	1.	Residue applied only in E3 scoring.
	2.	Residue applied to latent state update.
	3.	Hybrid implementation.

Metrics:
	•	Predictive error stability
	•	Survival duration
	•	Harm recurrence rate
	•	Generalisation to new contexts
	•	Representation drift magnitude

Predictions:
	•	Pure latent distortion will degrade predictive coherence more rapidly.
	•	Pure trajectory gating will preserve modelling accuracy while reducing harmful enactment.
	•	Hybrid may optimise trade-off.

⸻

7. Safety Implication

A safety-aligned architecture may prefer:

“Know everything; enact selectively.”

Over:

“Avoid knowing dangerous things.”

Suppressing representation risks epistemic brittleness.

Suppressing trajectories preserves modelling while constraining behaviour.

⸻

8. Open Questions
	•	Does pure trajectory gating generalise sufficiently without representational bias?
	•	Under what conditions does latent distortion become necessary?
	•	How does residue placement interact with precision regulation?
	•	Can trajectory-level suppression create hidden attractors?

⸻

9. Governance Note

This document proposes a mechanism placement hypothesis.

It does not alter:
	•	ARC-013 (Residue Geometry)
	•	ARC-018 (Hippocampal Rollouts)

Promotion would require:
	•	Experimental comparison across residue placement strategies
	•	Demonstration of preserved predictive coherence
	•	Clear invariant specification for residue persistence and non-erasure

⸻

Abstracted Layer (Optional Appendix)

⟦Separation⟧
E1/E2 = RepresentationalRichness
HPC/E3 = TrajectoryAuthority

⟦Principle⟧
DangerDetailed ∧ PathInaccessible

⟦Preference⟧
Residue(TrajectorySpace) > Residue(RepresentationDistortion)

Status: ThoughtIntake (NotPromoted)


