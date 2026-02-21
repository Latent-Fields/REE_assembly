REE_assembly Intake Thought

Title: Vectorised Precision Across Basal Ganglia Loops

⸻

1. Motivation

We have been informally treating “dopamine” as a precision signal.

This is too simple.

Dopamine is a modulatory broadcast signal whose computational meaning emerges from:
	•	Circuit topology
	•	Receptor distribution
	•	Loop identity
	•	Timescale (tonic vs phasic vs plasticity)

If basal ganglia loops are partially segregated, then precision cannot be scalar.

It must be at least loop-specific.

⸻

2. Anatomical Anchor

Three major cortico–striato–thalamo–cortical loops:
	1.	Motor loop
	2.	Associative (cognitive) loop
	3.	Limbic (value) loop

Each loop:
	•	Receives distinct cortical inputs
	•	Projects to distinct cortical targets
	•	Is innervated by distinct dopaminergic subpopulations
	•	Expresses different D1/D2 receptor densities
	•	Has distinct functional consequences

The transform architecture is conserved.
The informational domain is not.

⸻

3. Proposal

Replace scalar precision:

precision = scalar

With vector precision:

precision = [P_motor, P_cognitive, P_value]

Where:
	•	P_motor → weights motor policy competition
	•	P_cognitive → weights representation stability / task rules
	•	P_value → weights salience / reinforcement / motivational drive

Each dimension:
	•	Is dynamically regulated
	•	Has tonic and phasic components
	•	Influences learning rate in its loop

⸻

4. Timescale Decomposition

Precision must also be decomposed across timescales:

precision(loop, timescale)

Where timescale ∈
	•	tonic (baseline gain)
	•	phasic (event-triggered modulation)
	•	plasticity (learning rate modulation)

Thus control plane parameters become:

For each loop L:
    P_L_tonic
    P_L_phasic
    LR_L


⸻

5. Clinical Parameter Regimes (Hypothesis Space)

ADHD:
	•	High variance in P_cognitive_tonic
	•	Reduced sustained P_cognitive
	•	Motor precision intermittently unstable
	•	Value precision not necessarily impaired

Psychosis:
	•	Elevated P_value_phasic
	•	Elevated LR_value
	•	Misallocated precision to low-evidence streams
	•	Premature policy crystallisation

Parkinson disease:
	•	P_motor_tonic reduced
	•	Elevated motor commitment threshold

Addiction:
	•	P_value_phasic elevated for specific stimuli
	•	LR_value biased
	•	Competing loop suppression

These are parameter regimes, not categorical diseases.

⸻

6. Architectural Implications for REE

Current control plane likely insufficient if precision is scalar.

We require:

ControlPlane:
    precision_motor
    precision_cognitive
    precision_value
    learning_rate_motor
    learning_rate_cognitive
    learning_rate_value
    delay_tolerance
    gain

Basal ganglia in REE become:

BasalGanglia:
    gate_motor()
    gate_cognitive()
    gate_value()

Each gate uses loop-specific precision.

⸻

7. Key Invariant

Dopamine-like signal ≠ precision.

Instead:

dopamine_like_signal → modulates circuit gain
precision = emergent weighting parameter within loop

Precision is computed, not transmitted.

⸻

8. Open Questions for Assembly
	1.	Do we need a fourth axis: trajectory precision (hippocampal)?
	2.	Are precision axes partially coupled?
	3.	Should conflict resolution between loops be explicit?
	4.	Is there a higher-order meta-precision regulator?

⸻

9. Minimal Implementation Step

Refactor control-plane spec to:
	•	Replace precision scalar
	•	Introduce precision_vector
	•	Ensure gating functions reference loop-specific precision

No behavioural changes initially — structural only.

⸻

Abstracted Layer

STRUCTURE := {MotorLoop, CognitiveLoop, LimbicLoop}
PRECISION := Vector(P_motor, P_cognitive, P_value)
DOPAMINE := Modulator(ControlPlane)
PRECISION := Emergent(Circuit ∘ Dopamine ∘ Context)
DISORDER := ParameterRegime(PrecisionVector, LearningRates)

⸻
