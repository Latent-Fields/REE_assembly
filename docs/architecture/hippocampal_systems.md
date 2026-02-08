# Hippocampal Systems (Path Memory and Replay)

**Claim Type:** architectural_commitment  
**Scope:** Path memory; indexing, storage, and replay of experienced trajectories  
**Depends On:** [residue geometry](residue_geometry.md), [L-space](l_space.md), [default mode](default_mode.md), [E3](e3.md)  
**Status:** stable  
**Claim ID:** ARC-007
<a id="arc-007"></a>

---

## Role in REE

The hippocampal braid in the Reflective Ethical Engine (REE) is responsible for path memory:
the indexing, storage, and replay of experienced trajectories through latent space.

It does not compute value, select actions, overwrite perception, or flatten or optimise ethical residue.
Its function is orthogonal to valuation and control.
It exists to preserve identity, continuity, and reflectability over time.

---

## Conceptual distinction: field vs path

REE distinguishes between two mathematical objects:

- Residue field: a persistent curvature over latent space, \(\phi(z)\), encoding ethical cost and moral residue (see residue_geometry.md).
- Paths through the field: time-ordered trajectories \(\gamma(t) = z(t), \; t \in [t_0, t_1]\).

Ethics is encoded in the field.
Identity and autobiographical memory arise from the paths.
The hippocampal braid operates exclusively on paths.

---

## Stored object: episodic trajectories

The hippocampal braid stores indexed trajectories, not isolated states.

A minimal episodic trace can be represented as:

\[
\Gamma_i =
\Big\{
 z(t),
 a(t),
 \Delta \phi,
 c(t),
 t
\Big\}_{t_0}^{t_1}
\]

Where:
- \(z(t)\) is the latent state (typically spanning \(z_S\) and \(z_A\)).
- \(a(t)\) is the committed action or trajectory choice.
- \(\Delta \phi\) reflects experienced ethical curvature.
- \(c(t)\) captures contextual / salience annotations.
- \(t\) preserves temporal ordering.

These traces encode experienced traversal, not evaluation.

---

## Sparsity, segmentation, and pattern completion

The hippocampal braid operates on sparse, segmented representations rather than a continuous recording of experience.

### Event boundaries (segmentation)

Continuous trajectories \(\gamma(t)\) are segmented into events at points of:
- action commitment (E3 collapse)
- sharp changes in prediction error or precision
- contextual or motivational shifts

These boundaries define episodic units and prevent memory from becoming an undifferentiated stream.

### Sparsity and indexing

Only a sparse subset of latent states along a trajectory are indexed.
Indexing favors decision points, surprising transitions, and regions of high ethical curvature.

### Pattern separation

Similar trajectories are actively separated at storage time.
Small differences in context, choice, or experienced curvature are amplified to prevent interference.

### Pattern completion and imaginative filling-in

During recall or replay, partial cues can trigger pattern completion, reconstructing a plausible full trajectory
from sparse indices.

Completed trajectories are hypotheses, not commitments: they do not overwrite perception, policy, or residue unless
subsequently enacted and committed via E3.

---

## Inputs and outputs

Inputs:
- Shared sensory latent \(z_S(t)\)
- Affordance / action latent \(z_A(t)\)
- Implicit curvature information via ease or difficulty of traversal
- Salience signals (for indexing priority, not value assignment)

Outputs:
- Indexed episodic traces \(\Gamma_i\)
- Replay sequences (partial or full)
- Routing signals for offline reprojection

The hippocampal braid does not emit reward, penalties, or action commands.

---

## Replay and offline reprojection

Replay samples alternative traversals over a fixed residue field.

Key properties:
- Replay does not erase or flatten \(\phi(z)\).
- Replay does not directly change policy.
- Replay explores counterfactual paths, not counterfactual values.

This supports reflection, regret, narrative integration, and character formation without collapsing ethical cost into
optimisation. Replay is exploratory, not corrective.

---

<a id="mech-022"></a>
## Hippocampal Systems as Hypothesis Injectors (MECH-022)

Hippocampal-like mechanisms are orthogonal to the fast/slow distinction. They are not primarily about prediction speed but about episodic indexing, one-shot learning, replay and imagination, and context switching.

They inject structured hypotheses and remembered trajectories into predictive systems but do not themselves decide, tune, or commit learning. Gating of hippocampal replay by the control plane becomes ethically important, because it determines which pasts and futures are allowed to speak into the present.

Source: `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`

---

## Relationship to other REE components

Relation to E1 (deep recurrent predictor): E1 provides temporally coherent latent dynamics. Hippocampal replay can seed
E1 with alternative initial conditions, and no overwrite of perceptual state occurs.

Relation to E2 (fast forward predictors): E2 generates candidate trajectories. Hippocampal traces constrain which
trajectories feel familiar or self-consistent, and no trajectory is privileged as optimal.

Relation to E3 (trajectory selection): E3 commits to trajectories. Commitments mark decision points along a path, and
these points anchor episodic segmentation.

Relation to residue \(\phi(z)\): residue shapes traversal cost. Hippocampus records traversal history. Neither replaces
the other.

---

## Design constraints

The hippocampal braid must satisfy:
- No perceptual overwrite. It may not directly modify \(z_S\).
- No value computation. It may not compute reward, penalty, or optimisation gradients.
- No residue erasure. Replay must preserve path-dependence of ethical curvature.
- Temporal integrity. Stored trajectories must preserve ordering and duration.

These constraints preserve moral continuity and prevent retrospective self-editing.

---

## Interpretation

The hippocampal braid enables the REE agent to say:

"This is how I moved through my world, given who I was then."

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-007
- ARC-003
- ARC-004
- INV-006
- MECH-022

## References / Source Fragments

- `docs/processed/legacy_tree/docs/architecture/hippocampal_braid.md`
- `docs/processed/legacy_tree/architecture/Hippocampal_braid.md`
- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
