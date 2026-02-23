Status: processed

Processed in:
- `docs/architecture/e3.md` (MECH-062 overlay re-engagement + trigger-field routing)
- `docs/architecture/control_plane.md` (MECH-063 competitive trigger-field bandwidth policy)
- `docs/architecture/sleep.md` (MECH-030 post-sleep tactic-option expansion expectation)
- `docs/claims/claims.yaml` (source lineage updates for MECH-030/057/060/062/063)
- `docs/changelog.md` (2026-02-23 thought-intake processing record)

---

THOUGHT for REE_assembly

Title: Skill drift from conscious control to post-commit automation; abstraction-level gating; surprise interrupts
Type: Hypothesis-generating phenomenology → architecture mapping
Tags: skill learning, automaticity, commitment gating, basal ganglia, striatum, cerebellum, hippocampus, noradrenaline, dopamine, abstraction-level control

0) Source phenomenology (mined, near-verbatim)
	•	“I can learn skills. When these consistently have low outcome error to hoped for outcome they can drift out of conscious manipulation to allow conscious thought think about higher level abstractions.”
	•	Sailing example: early phase = conscious tiller/weight/rope pulling; later phase = “my body sense… seemed to encompass the dinghy,” and “the thrum of water and wind… was much more than just vibrations.”
	•	Automatic phase: “It automatically guided miniscule updates.”
	•	Interrupt condition: “if something didn’t add up my conscious mind lifted the reigns again,” but conscious takeover felt “more clumsy… less smooth.”
	•	Learning vs execution: “Learning seemed concentrated on conscious processes whereas those handed over to the more automatic may have learned optimisation but not tactic improvement.”

1) Core hypothesis

H1 (skill drift / control migration): As outcome error becomes consistently low, control migrates from a conscious, higher-latency supervisory loop to fast post-commit loops that run continuous micro-updates. Conscious control re-enters primarily when a mismatch/surprise criterion is met.

H2 (commitment framing): This maps onto pre-commit vs post-commit separation:
	•	Pre-commit: path proposal, goal selection, tactical reasoning, abstraction selection.
	•	Post-commit: smooth execution of committed policy with dense sensorimotor feedback and micro-corrections.

H3 (abstraction-level gating): Basal ganglia–thalamic gating dynamically selects the latent abstraction level (or the representational stratum) used by the “trajectory selector” machinery, such that reflective control focuses where it adds value (high uncertainty / goal conflict / tactic search), and yields control when execution is stable.

2) Proposed REE (Reflective–Ethical Engine) mapping

Using the project’s E-loop language:
	•	E1 (deep predictor / world model): Supplies stable state estimates (“dinghy + wind + water” becoming a unified controllable manifold).
	•	E2 (fast predictor / transition operator; cerebellar-like): Drives the “miniscule updates” layer: rapid forward prediction + continuous correction.
	•	E3 (trajectory selector; hippocampus–prefrontal–amygdala–like):
	•	Chooses goals, evaluates valence, proposes paths and tactics.
	•	Re-engages when “something doesn’t add up.”
	•	Basal ganglia loops (commitment machinery):
	•	Gate transitions between E3-dominant deliberation and E2/E1-dominant execution.
	•	Potentially gate which abstraction layer is currently “controlling” the policy output (high-level tactics vs low-level motor primitives).

3) Error signals and neuromodulator hypotheses (as architecture knobs)

H4 (error system split):
	•	Post-commit execution has strong expectations; deviations are better captured by surprise / unexpected uncertainty signals (noradrenaline-like) that trigger interrupt + escalation to E3.
	•	Pre-commit learning and valuation rely more on dopamine-like precision / prediction error for updating action values and policy selection.

H5 (striatal subregions as functional partitions):
	•	Ventral striatum / nucleus accumbens more engaged for E3-adjacent valuation and goal-salience arbitration.
	•	Dorsal striatum more engaged for stabilized post-commit execution/habitualized skill flow.

4) Concrete predictions (useful for falsification + instrumentation)

P1 (interrupt signature): When execution is smooth, E3 compute is low; when mismatch rises, a discrete “interrupt” occurs: increased deliberative sampling + reduced smoothness (higher variance, slower corrections).
P2 (two-stage learning): Early learning improves “tactic” (strategy selection) under E3; later consolidation improves “optimization/smoothness” under post-commit loops, with limited tactic gains unless E3 is re-invoked during exploration.
P3 (abstraction gating): Under stable contexts, control policy uses low-level representations; under novelty/uncertainty, the system shifts to higher abstraction representations (and vice versa after stabilization).
P4 (sleep refactor): Offline phases selectively compress / refactor successful post-commit policies to avoid combinatorial explosion of online exploration.

5) Implementation hooks for REE_assembly
	•	Add an explicit Interrupt Channel: surprise_signal -> elevate_control(E3) with hysteresis to avoid thrashing.
	•	Add Abstraction Router: selects representation layer (object-level, relational, tactic-level) based on uncertainty + goal conflict.
	•	Add Two-Lane Learning:
	•	Lane A: E3 policy improvement (tactics, path proposals).
	•	Lane B: post-commit optimization (smoothness, micro-corrections, motor primitives).
	•	Add Skill Drift Criterion: sustained low outcome error + low surprise → migrate control weight from E3 to post-commit executor.

⸻

Gaps to fill (explicit prompts, not invented)
	1.	Trigger condition details: What exactly counts as “something didn’t add up” for you—sensory mismatch, goal mismatch, timing mismatch, affect/valence shift, or social/environmental hazard cue?
	2.	Granularity: Does re-engagement of conscious control happen as a full takeover, or as a temporary “audit” layer while the post-commit loop continues underneath?
	3.	Tactic vs optimization: Can you name one example where tactic improved only when consciously engaged, and one where optimization improved only after “hand-off”?
	4.	Phenomenology of self-boundary: When the dinghy became “part of self,” did it feel like expanded proprioception, expanded agency, reduced verbal thought, or something else?

⸻

Confidence measures
	•	Training Data Confidence: High (this pattern matches common skill-learning/automaticity motifs in neuroscience and cognitive models).
	•	Epistemic Confidence: Moderate (the architectural mapping is coherent; specific neuromodulator ↔ subsystem assignments are plausible but should be treated as testable hypotheses).

⸻

Abstracted language overlay (compact)

Let:
	•	E3 := {goal_select, path_propose, tactic_reason, valence_eval}
	•	POST := {execute_policy, micro_correct, smooth_optimize}
	•	INT := surprise_interrupt
	•	GATE := basal_ganglia_commit
	•	ABS := abstraction_level_router

Assertions:
	1.	low(outcome_error) ∧ stable(context) -> weight(POST)↑ ∧ weight(E3)↓
	2.	mismatch_or_surprise -> INT -> weight(E3)↑ ∧ weight(POST)↓(partial)
	3.	ABS := f(uncertainty, goal_conflict, novelty)
	4.	learning := {Δtactic via E3, Δsmoothness via POST}
	5.	neuromod: NA_like ≈ INT ; DA_like ≈ value/precision update in E3

⸻

Footnotes
	1.	“Pre-commit / post-commit” is being used here as an architectural control distinction (selection vs execution), not as a claim that biology implements a single binary gate; the point is a functional separation you can instrument in REE_assembly.
	2.	“Surprise / noradrenaline-like” is shorthand for an interrupt-style unexpected-uncertainty signal (locus coeruleus in biology); in REE terms it’s a fast, global “stop trusting current policy” modulator rather than a value-learning error.
	3.	“Dopamine-like” is shorthand for value/precision learning signals used in selecting and reinforcing actions (ventral/dorsal striatal loops in biology); in REE terms it’s a policy-selection update and confidence-weighting signal, not “pleasure.”
