# Hippocampal Braid (Path Memory and Replay)

**Claim Type:** architectural_commitment  
**Scope:** Path memory; indexing, storage, and replay of experienced trajectories  
**Depends On:** [residue geometry](residue_geometry.md), [L-space](l_space.md), [default mode](default_mode.md)  
**Status:** stable

---

Role in REE

The hippocampal braid in the Reflective Ethical Engine (REE) is responsible for path memory:
the indexing, storage, and replay of experienced trajectories through latent space.

It does not:
	•	compute value
	•	select actions
	•	overwrite perception
	•	flatten or optimise ethical residue

Its function is orthogonal to valuation and control.
It exists to preserve identity, continuity, and reflectability over time.

⸻

Conceptual distinction: field vs path

REE distinguishes between two mathematical objects:
	•	Residue field
A persistent curvature over latent space:
\phi(z)
encoding ethical cost and moral residue
(see residue_geometry.md).
	•	Paths through the field
Time-ordered trajectories:
\gamma(t) = z(t), \quad t \in [t_0, t_1]

Ethics is encoded in the field.
Identity and autobiographical memory arise from the paths.

The hippocampal braid operates exclusively on paths.

⸻


Stored object: episodic trajectories

The hippocampal braid stores indexed trajectories, not isolated states.

A minimal episodic trace can be represented as:
\Gamma_i =
\Big\{
z(t),
a(t),
\Delta \phi,
c(t),
t
\Big\}_{t_0}^{t_1}

Where:
	•	z(t) is the latent state (typically spanning z_S and z_A)
	•	a(t) is the committed action or trajectory choice
	•	\Delta \phi reflects experienced ethical curvature
	•	c(t) captures contextual / salience annotations
	•	t preserves temporal ordering

These traces encode experienced traversal, not evaluation.

⸻

## Sparsity, segmentation, and pattern completion

The hippocampal braid operates on **sparse, segmented representations** rather than a continuous recording of experience.
This is not an implementation detail but a functional necessity.

### Event boundaries (segmentation)

Continuous trajectories \(\gamma(t)\) are segmented into **events** at points of:
- action commitment (E3 collapse)
- sharp changes in prediction error or precision
- contextual or motivational shifts

These boundaries define *episodic units* and prevent memory from becoming an undifferentiated stream.
Segmentation supports recall, replay, and narrative recomposition without requiring full fidelity replay of lived time.

### Sparsity and indexing

Only a sparse subset of latent states along a trajectory are indexed.
Indexing favours:
- decision points
- surprising transitions
- regions of high ethical curvature

This sparsity enables efficient retrieval and avoids storing exhaustive state histories.

### Pattern separation

Similar trajectories are **actively separated** at storage time.
Small differences in context, choice, or experienced curvature are amplified to prevent interference.
This allows distinct episodes to coexist even when they occupy nearby regions of latent space.

### Pattern completion and imaginative filling-in

During recall or replay, partial cues can trigger **pattern completion**, reconstructing a plausible full trajectory
from sparse indices.

This mechanism supports:
- imagination and counterfactual exploration
- daydreaming and spontaneous recombination
- the experience of "what might have happened" or "what could happen next"

Importantly, completed trajectories are *hypotheses*, not commitments:
they do not overwrite perception, policy, or residue unless subsequently enacted and committed via E3.

⸻

Inputs and outputs

Inputs
	•	Shared sensory latent z_S(t)
	•	Affordance / action latent z_A(t)
	•	Implicit curvature information via ease or difficulty of traversal
	•	Salience signals (for indexing priority, not value assignment)

Outputs
	•	Indexed episodic traces \Gamma_i
	•	Replay sequences (partial or full)
	•	Routing signals for offline reprojection

The hippocampal braid does not emit reward, penalties, or action commands.

⸻

Replay and offline reprojection

Replay samples alternative traversals over a fixed residue field.

Key properties:
	•	Replay does not erase or flatten \phi(z)
	•	Replay does not directly change policy
	•	Replay explores counterfactual paths, not counterfactual values

This supports:
	•	reflection
	•	regret
	•	narrative integration
	•	character formation

without collapsing ethical cost into optimisation.

Replay is therefore exploratory, not corrective.

⸻

Relationship to other REE components

Relation to E1 (deep recurrent predictor)
	•	E1 provides temporally coherent latent dynamics
	•	Hippocampal replay can seed E1 with alternative initial conditions
	•	No overwrite of perceptual state occurs

Relation to E2 (fast forward predictors)
	•	E2 generates candidate trajectories
	•	Hippocampal traces constrain which trajectories feel “familiar” or “self-consistent”
	•	No trajectory is privileged as optimal

Relation to E3 (trajectory selection)
	•	E3 commits to trajectories
	•	Commitments mark decision points along a path
	•	These points anchor episodic segmentation

Relation to residue \phi(z)
	•	Residue shapes traversal cost
	•	Hippocampus records traversal history
	•	Neither replaces the other

⸻

Design constraints

The hippocampal braid must satisfy:
	1.	No perceptual overwrite
It may not directly modify z_S.
	2.	No value computation
It may not compute reward, penalty, or optimisation gradients.
	3.	No residue erasure
Replay must preserve path-dependence of ethical curvature.
	4.	Temporal integrity
Stored trajectories must preserve ordering and duration.

These constraints preserve moral continuity and prevent retrospective self-editing.

⸻

Interpretation

The hippocampal braid enables the REE agent to say:

“This is how I moved through my world, given who I was then.”

Not:

“This is the optimal thing I should have done.”

Identity is therefore not a policy,
but a distribution over lived paths through ethical geometry.

⸻

Cross-references
	•	Residue geometry: architecture/residue_geometry.md
	•	Latent stack: architecture/latent_stack.md
	•	Trajectory selection: architecture/trajectory_selection.md
	•	Offline reprojection: architecture/offline_reprojection.md (planned)

⸻
