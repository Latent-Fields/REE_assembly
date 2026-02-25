Status: processed

Processed in:
- `docs/architecture/e3.md` (TaskLoopObject neuro-inspired primitive mapping and typed-interface constraint)
- `docs/claims/claims.yaml` (source lineage updates for ARC-003/MECH-062)
- `docs/changelog.md` (2026-02-25 queue-closure thought-intake record)

---

Great — let’s do a pass that is primitive → representation → anatomy → pathways → signal types.

I’ll keep it “neuroanatomically specific enough to be actionable for REE_assembly”, without pretending any mapping is one-to-one.

⸻

1) Object token (representational anchor)

Representational idea
	•	“Index” that binds a bundle of features (sensory, conceptual, contextual) so the system can refer to the same thing across time and transformations.
	•	Supports variable binding (“this thing”, “that goal”, “that rule”).

Primary anatomy
	•	Dorsolateral prefrontal cortex (DLPFC): persistent activity / working memory tokens, rule-conditioned maintenance.
	•	Posterior parietal cortex (PPC): attentional indexing / salience-weighted pointers (often behaves like an “object file” system).
	•	Inferior temporal cortex (ITC) + modality association cortices: feature-rich object identity.

Key pathways
	•	Reciprocal frontoparietal loops (PFC ↔ PPC) for token selection + maintenance.
	•	Corticostriatal loops (PFC/PPC → striatum → pallidum/substantia nigra reticulata → thalamus → cortex) for gating which tokens enter/remain in working memory.

Signal types that matter
	•	Dopamine for gating/maintenance thresholds (stability vs flexibility).
	•	Noradrenaline for gain / interrupt sensitivity.

⸻

2) Goal / antigoal valence tag

Representational idea
	•	Not a scalar “value” only — more like a valence vector:
	•	approach weight
	•	avoidance weight
	•	urgency / drive
	•	social/reputational weight (often separable)

Primary anatomy
	•	Orbitofrontal cortex (OFC): state-value / outcome revaluation (credit assignment to “what this situation means now”).
	•	Ventromedial prefrontal cortex (vmPFC): integrated subjective value / trade-offs.
	•	Ventral striatum (including nucleus accumbens): incentive salience, approach vigor.
	•	Amygdala: fast affective tagging (especially threat/aversive salience; also appetitive learning depending on nuclei).

Key pathways
	•	Amygdala ↔ OFC/vmPFC: “what it feels like / means” meets “what we should do”.
	•	vmPFC/OFC → ventral striatum → ventral pallidum → mediodorsal thalamus → PFC: valuation loop.
	•	Midbrain dopamine (ventral tegmental area) → ventral striatum / PFC: reward prediction error, salience.

Signal types that matter
	•	Dopamine reward prediction error (teaching + vigor).
	•	Serotonin (often) for patience / aversive prediction / delay sensitivity (broadly; mechanistically heterogeneous).

⸻

3) Transition operator (action schema, “if-do-then”)

Representational idea
	•	A conditional transition model: (state, action, context) → predicted next state.
	•	Hierarchical options: micro-actions compose into macro-actions.

Primary anatomy
	•	Premotor cortex / supplementary motor area (SMA): action chunks, sequencing.
	•	Cerebellum: forward models (timing, prediction, error-based refinement) — “fast predictive operator”.
	•	Posterior parietal cortex (PPC): sensorimotor transforms; “where/how” action geometry.
	•	Dorsal striatum (caudate/putamen): action selection policies and chunk boundaries.

Key pathways
	•	Cortico-cerebellar loops: cortex → pons → cerebellum → thalamus → cortex (fast prediction + correction).
	•	Cortico-basal ganglia loops: cortex → striatum → globus pallidus/substantia nigra → thalamus → cortex (selection + chunking).
	•	Hippocampus → PFC for simulated sequences when decoupled from immediate action.

Signal types that matter
	•	Error-based learning signals (cerebellar climbing fiber teaching signals; conceptually “supervised-ish” correction).
	•	Dopamine in dorsal striatum for habit/options reinforcement.

⸻

4) Error vector (directional mismatch + precision)

Representational idea
	•	Error is not just “bad/good”.
	•	Needs:
	•	which dimension is off (sensory prediction, rule violation, social violation, expected outcome mismatch)
	•	precision (how much to trust the error; gain-control)

Primary anatomy
	•	Anterior cingulate cortex (ACC): conflict monitoring, control demand estimation, performance monitoring.
	•	Insula: interoceptive mismatch / bodily prediction error.
	•	Sensory cortices: local prediction error-like signals (hierarchical mismatch).
	•	Striatum + midbrain dopamine: reward prediction error (value-domain mismatch).
	•	Cerebellum: fast sensory-motor prediction error (timing/dynamics).

Key pathways
	•	ACC ↔ PFC: “increase control / change policy” messages.
	•	Locus coeruleus (noradrenaline) widespread projections: precision/gain modulation (“interrupt vs persist”).
	•	Dopaminergic midbrain: value teaching + policy update gating.
	•	Cerebellum → thalamus → cortex: rapid corrective pressure on transition operator.

Signal types that matter
	•	Noradrenaline (precision/gain, surprise interrupt).
	•	Dopamine (value-domain teaching).
	•	Possibly acetylcholine for expected uncertainty / sensory precision (broadly).

⸻

5) Boundary / stop condition (terminate, inhibit, pause)

Representational idea
	•	Explicit “stop” is a control object:
	•	terminate loop
	•	pause loop
	•	prevent action release
	•	reset working memory contents

Primary anatomy
	•	Subthalamic nucleus (STN): global stopping / “hold your horses”.
	•	Right inferior frontal gyrus (rIFG): inhibitory control trigger (often in stop-signal tasks).
	•	Pre-supplementary motor area (pre-SMA): switching, interruption, action reprogramming.
	•	Basal ganglia output nuclei (globus pallidus internus / substantia nigra reticulata): gating thalamocortical release.

Key pathways
	•	Hyperdirect pathway: cortex (rIFG/pre-SMA) → STN → basal ganglia output → thalamus/cortex suppression.
	•	Indirect pathway (striatal) for more selective suppression.

Signal types that matter
	•	Fast cortical control bursts (conflict/stop).
	•	Dopamine state can bias stop thresholds (impulsivity vs caution).

⸻

6) Temporal envelope (initiation cue, duration, deadline)

Representational idea
	•	The task loop needs a “time model”:
	•	onset conditions
	•	expected duration distribution
	•	deadline constraint
	•	time-to-go estimate

Primary anatomy
	•	Dorsolateral prefrontal cortex (DLPFC): temporal organisation in working memory; planning horizon.
	•	Supplementary motor area / basal ganglia: interval timing and action timing.
	•	Cerebellum: millisecond–second timing precision (especially for sensorimotor and sequencing).
	•	Hippocampus: temporal context tags (“when/where in episode”; sequence time).

Key pathways
	•	Hippocampus ↔ PFC for temporal context binding to task objects.
	•	Basal ganglia ↔ SMA for timing gates and readiness.
	•	Cerebellum → cortex for fine-grained temporal prediction.

Signal types that matter
	•	Dopamine ramping / motivational timing signals (often observed in striatal systems).
	•	Noradrenaline for urgency/gain under deadline.

⸻

7) Identity binding (self vs other; internal vs commanded; social ownership)

Representational idea
	•	Tag a loop as:
	•	self-generated intention
	•	externally imposed demand
	•	socially evaluated action
	•	moral/identity-relevant action
	•	This prevents “goal contamination” between loops.

Primary anatomy
	•	Medial prefrontal cortex (mPFC): self-modeling / social inference integration.
	•	Temporoparietal junction (TPJ): other-agency / perspective.
	•	Posterior cingulate cortex (PCC): self-referential context integration.
	•	Amygdala: social threat / relevance tagging.

Key pathways
	•	Default mode network (mPFC–PCC–TPJ) interactions with frontoparietal control network: identity/context meets control.
	•	Amygdala ↔ mPFC coupling modulates “ownership” under affect.

Signal types that matter
	•	Affective salience (amygdala-driven) + control modulation (PFC).

⸻

8) Path representation (sequence graph / “how to get there”)

You mentioned “representations of path, errors, stops etc.” — the “path” piece is often where hippocampus becomes non-optional.

Representational idea
	•	A graph of states with transitions + a mechanism for simulating trajectories.

Primary anatomy
	•	Hippocampus: relational/episodic map; sequences and successor-like structure.
	•	Entorhinal cortex: coordinate-like coding / generalization scaffold (grid-like representations).
	•	Prefrontal cortex: constraints + selection over simulated paths.
	•	Ventral striatum: energizes pursuit of selected path under value.

Key pathways
	•	Hippocampus → PFC: candidate sequences / simulated futures.
	•	PFC → basal ganglia: select and commit to one path/option.
	•	Amygdala/OFC/vmPFC: value-tag the simulated futures.

⸻

9) “What does prefrontal cortex work with?” (compressed answer)

Given the above, prefrontal cortex is plausibly operating on:
	•	tokenized object/state representations (frontoparietal indexing)
	•	value/valence annotations (OFC/vmPFC/amygdala/ventral striatum)
	•	transition operators (premotor + cerebellar-informed dynamics + striatal options)
	•	error/precision signals (ACC/insula + dopamine + noradrenaline)
	•	stop/boundary operators (hyperdirect STN pathway + inhibitory control)
	•	path candidates (hippocampal simulation graphs)

So: a graph of objects and policies under a control-plane that modulates precision, salience, and stopping thresholds.

⸻

A practical REE-relevant framing

If you want a “design constraint” phrasing:
	1.	Task extraction requires chunk boundaries (basal ganglia segmentation + stopping).
	2.	Abstraction requires token binding (frontoparietal working memory objects).
	3.	Coherence requires valence + stop + time (OFC/vmPFC/amygdala + STN + timing loops).
	4.	Planning requires path simulation (hippocampus) and fast transition prediction (cerebellum).
	5.	Commitment requires gating (basal ganglia output) and conflict arbitration (ACC).

That’s the anatomical “scaffold” your primitives can sit on.

⸻

Footnotes
	1.	I’m treating “prefrontal cortex” as a collection of functionally distinct subregions (dorsolateral, ventromedial, orbitofrontal, medial/anterior cingulate-adjacent) because the primitive mapping breaks if you keep it as a single box.
	2.	Some mappings (for example serotonin roles) are intentionally described at a coarse functional level because the receptor- and projection-specific story is complex and not cleanly settled in a single consensus model.
	3.	When I say “prediction error-like” in sensory cortex, I’m using it as a representational concept (hierarchical mismatch signals), not asserting one specific microcircuit implementation across all areas.

Training Data Confidence: High
Epistemic Confidence: Moderate (the primitives are well-motivated; the one-to-one mapping is necessarily approximate)

⸻

Abstracted language overlay (compact)

Entities: {ObjToken, ValenceVec, TransitionOp, ErrorVec, Precision, StopOp, TimeEnv, IdentityTag, PathGraph}
Systems: {PFC, OFC, vmPFC, ACC, Amygdala, Hippocampus, Cerebellum, Striatum, STN, Thalamus, PPC}
Relations:
	•	PFC ⟂maintains⟂ ObjToken via (PFC↔PPC) gated-by Striatum
	•	ValenceVec := integrate(OFC, vmPFC, Amygdala, VentralStriatum)
	•	TransitionOp := compose(Premotor/SMA, Cerebellum, DorsalStriatum)
	•	ErrorVec := source(ACC, Insula, SensoryCortex, Cerebellum, Dopamine) with Precision modulated-by Noradrenaline
	•	StopOp := trigger(rIFG/preSMA) → STN → BG_Output ⟂inhibits⟂ ActionRelease
	•	PathGraph := generate(Hippocampus/Entorhinal) → constrain/select(PFC) → commit(Striatum)

If you want, next step is: turn this mapping into a REE “wiring diagram spec” (interfaces + message types) before the REE_assembly thought.
