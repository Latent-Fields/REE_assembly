Status: processed

Processed in:
- `docs/architecture/developmental_curriculum.md` (IMPL-019, ARC-019)
- `docs/claims/claims.yaml` (IMPL-019)
- `docs/claims/claim_index.md` (IMPL-019)

---

DEV-ROADMAP: Self-First, Social-Later Developmental Ordering Hypothesis

Layer: Architectural Governance / Developmental Heuristic

⸻

1. Motivation

There is a structural concern that attempting to instantiate and test social systems within REE before stabilising basic self-viability mechanisms may introduce interpretability problems and architectural instability.

Hypothesis: Social modelling presupposes a sufficiently stable self-model and viability-regulation loop. Without this, social cost integration may mask more fundamental architectural deficiencies.

This document proposes a staged developmental testing order informed by:
	•	Ontogeny constraint (developmental ordering of capacities)
	•	Phylogeny analogy (earlier evolutionary regulators tend to be simpler and more conserved)

This is not an architectural commitment. It is a testing and governance heuristic.

⸻

2. Developmental Hypothesis

Core Claim (Provisional)

Social regulation requires:
	•	Stable self-viability learning
	•	Stable control-plane regime management
	•	Reliable predictive rollouts

Therefore:

Testing and instantiation should proceed in the order:
	0.	Harness and observability
	1.	Self-harm learning loop
	2.	Control-plane stabilisation
	3.	Predictive rollout maturity
	4.	Social coupling and other-modelling

This ordering may increase interpretability and reduce architectural thrash.

⸻

3. Evolutionary Analogy (Heuristic Only)

Early biological regulators tend to be:
	•	Broad projection systems
	•	Low-dimensional control
	•	Highly conserved across species

Later biological regulators tend to be:
	•	Context-sensitive
	•	More stateful
	•	More specialised and less universally conserved

Engineering analogy:
	•	Early REE mechanisms (precision routing, harm-response, commitment gating) should be simple, global, and robust.
	•	Later mechanisms (social weighting, care persistence, coupling parameters) should be layered on top of a stable substrate.

This is not a biological claim about literal equivalence. It is a complexity-ordering heuristic.

⸻

4. Proposed Staged Roadmap

Stage 0 — Harness and Observability

Goal: Make experimental results reproducible and interpretable.

Required:
	•	Deterministic seeds
	•	Explicit mechanism flags
	•	Invariant checks
	•	Structured metrics logging

Failure mode: Results are not trustworthy or comparable.

⸻

Stage 1 — Self-Viability Loop

Goal: Agent reliably reduces self-harm over episodes.

Mechanisms under test:
	•	Harm sensing
	•	Residue accumulation
	•	Commitment gating
	•	Basic reality constraint

Metrics:
	•	Harm per episode
	•	Survival duration
	•	Residue growth curve
	•	Recovery latency after first harm exposure

Failure modes:
	•	Repeated self-harm
	•	Dithering without commitment
	•	Residue runaway freeze

⸻

Stage 2 — Control Plane Stabilisation

Goal: Stable internal regimes without oscillatory thrash.

Mechanisms under test:
	•	Precision update dynamics
	•	Commitment thresholds
	•	Mode switching logic
	•	Offline integration cadence

Metrics:
	•	Action volatility
	•	Mode-switch frequency
	•	Long-horizon stability
	•	Calibration (confidence vs prediction error)

Failure modes:
	•	Mode thrashing
	•	Regime lock-in
	•	Catastrophic forgetting

⸻

Stage 3 — Predictive Rollout Maturity

Goal: Counterfactual reasoning becomes reliable.

Mechanisms under test:
	•	E1/E2 conditioning
	•	Rollout diversity vs feasibility
	•	Reality filtering

Metrics:
	•	Plan feasibility rate
	•	Prediction error alignment
	•	Regret signatures

Failure modes:
	•	Confabulated plans
	•	Overly narrow exploration
	•	Planning paralysis

⸻

Stage 4 — Social Extension

Goal: Introduce other-modelling without destabilising self-viability.

Incremental approach:
	1.	Passive other-state tracking
	2.	Mirror harm prediction (logging only)
	3.	Hard veto mechanisms
	4.	Graded coupling parameters

Metrics:
	•	Other-harm incidents
	•	False veto rate
	•	Self–other tradeoff stability

Failure modes:
	•	Social override of self-viability
	•	Excessive veto conservatism
	•	Instability introduced by coupling

⸻

5. Interaction with “No Explicit Ethical Cost” Direction

Current V1 runner includes explicit ethical term M(\zeta).

Canonical direction in REE_assembly: E3 selection does not require explicit ethical cost term.

Implication of staged roadmap:
	•	Validate self-viability and control-plane stability first.
	•	Then remove explicit M and observe the failure signature.
	•	Introduce constraint-based or residue-based alternatives incrementally.

This isolates causal effects rather than conflating multiple transitions.

⸻

6. Testable Predictions
	1.	Removing social modules during early stages should not impair self-survival metrics.
	2.	Introducing social coupling before control-plane stabilisation should increase instability.
	3.	Precision regulation should have measurable effects before social weighting does.
	4.	Residue geometry alone may produce proto-social avoidance patterns.

⸻

7. Open Questions
	•	Are there environments where social modelling improves early self-viability?
	•	Does residue generalisation produce unintended conservatism?
	•	What invariants must hold before social modules can be considered safe to enable?

⸻

8. Governance Note

This document is a developmental heuristic.

It does not currently modify ARC, MECH, or INV claims.

Promotion to formal architectural commitment requires:
	•	Empirical validation in experiment harness
	•	Conflict review against existing claims
	•	Clear invariant formulation
