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

**Subsystem abstract (core claims):** ARC‑007 anchors path memory and replay, ARC‑018 makes the hippocampus the sole
explicit rollout and viability‑mapping engine, MECH‑022 defines hippocampal hypothesis injection and control‑plane
gating, and MECH‑033 specifies the E2‑kernel → hippocampal rollout interface. Supporting context includes ARC‑003
(commitment), ARC‑004 (L‑space), INV‑006 (residue persistence), and MECH‑037 (provenance gating).

---

<a id="arc-018"></a>
## Hippocampal Rollouts and Viability Mapping (ARC-018)

**Claim Type:** architectural_commitment  
**Scope:** Explicit multi-step rollouts and post-commitment viability mapping  
**Depends On:** ARC-007, ARC-003, ARC-002, ARC-001  
**Status:** provisional  
**Claim ID:** ARC-018

The hippocampal system performs **counterfactual trajectory construction** and **post-commitment viability mapping**.
It is the only place explicit multi-step rollouts exist; E1/E2 supply constraints and short-horizon predictions.

---

## Two hippocampal functions (rollout vs viability mapping)

1. **Counterfactual rollout (imagination)**  
   - Constructs branching trajectories from the current latent state.  
   - Uses constraints from E1 and short-horizon predictions from E2.  
   - Produces candidate futures without ranking or commitment.

2. **Viability path mapping (commitment learning)**  
   - Triggered after an action is executed.  
   - Uses predicted vs observed `SELF_SENSORY` mismatch plus resulting WORLD/HOMEOSTASIS/HARM changes.  
   - Updates a viability map of action-space under commitment: which sequences are stable, fragile, or path-closing.  
   - This is not reward learning; it is learned affordance geometry under real execution.

---

<a id="mech-033"></a>
## E2 Kernel → Hippocampal Rollout Interface (MECH-033)

**Claim Type:** mechanism_hypothesis  
**Scope:** How E2 forward-prediction kernels seed hippocampal rollouts  
**Depends On:** ARC-018, ARC-002, ARC-001, ARC-005  
**Status:** candidate  
**Claim ID:** MECH-033

E2 supplies short-horizon forward-prediction kernels (local conditional transitions) rather than multi-step trajectories.
Hippocampal systems chain these kernels into explicit rollouts, constrained by E1 priors and modulated by control-plane
parameters (horizon, branching, temperature). This keeps “kernel” and “rollout” distinct while preserving a clean
handoff from fast prediction to explicit trajectory construction.

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
- Predicted vs observed `SELF_SENSORY` mismatch for post-commitment viability mapping

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
- Residue integration and curvature updates occur separately (see `residue_geometry.md` and `sleep.md`).

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

Relation to E2 (fast forward predictors): E2 supplies fast predictions and reafference signals. Hippocampal traces
constrain which trajectories feel familiar or self-consistent, while hippocampal systems generate explicit trajectories
and update viability maps.

Provenance gating for E1-generated content may be implemented via a Papez-like loop (see `papez_circuit.md`).

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
- ARC-018
- ARC-003
- ARC-004
- INV-006
- MECH-022
- MECH-033

## References / Source Fragments

- `docs/processed/legacy_tree/docs/architecture/hippocampal_braid.md`
- `docs/processed/legacy_tree/architecture/Hippocampal_braid.md`
- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
- `docs/thoughts/2026-02-09_starting_with_sensory_streams.md`
- `docs/thoughts/2026-02-09_e2_hpc_interface.md`
