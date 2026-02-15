# Sensory-to-Commit Information Flow Trace

Date: 2026-02-15
Scope: End-to-end REE information flow starting from tagged sensory streams through commitment and post-commit attribution.

## 1) Primary sensory ingress (tagged streams)

Input stream set (ARC-017):
- `WORLD`
- `HOMEOSTASIS`
- `HARM`
- `SELF_SENSORY`

Interpretation rule:
- Streams are privileged only for prediction and prediction-comparison operations.
- Tag identity determines downstream routing semantics (for example, harm spikes vs reafference mismatch).

Primary anchors:
- `docs/architecture/sensory_stream_tags.md#arc-017`

## 2) Shared sensory latent binding in L-space

The tagged streams are fused into shared sensory latent state at fast depth (`z_gamma` -> `z_S`).

Outputs at this stage:
- current bound sensory state
- precision-weighted residuals per stream

Primary anchors:
- `docs/architecture/l_space.md#arc-004`
- `docs/architecture/sensory_stream_tags.md#arc-017`

## 3) Fast forward prediction and affordance expansion (E2)

E2 consumes `z_S` + precision profile + optional E1 priors and emits:
- near-horizon predictions
- action-conditioned predictions
- affordance manifold (`z_beta` -> `z_A`)
- fast mismatch/error signals

Important boundary:
- E2 emits forward prediction kernels; explicit multi-step rollouts are not E2-native.

Primary anchors:
- `docs/architecture/e2.md#arc-002`
- `docs/architecture/hippocampal_systems.md#mech-033`

## 4) Slow contextual priors and long-horizon constraints (E1)

E1 maintains deeper regime/context priors (`z_theta`, `z_delta`) and conditions E2/E3 without direct sensory overwrite.

Outputs at this stage:
- long-horizon constraints
- identity/regime continuity priors
- stability context for trajectory evaluation

Primary anchors:
- `docs/architecture/e1.md#arc-001`
- `docs/architecture/l_space.md#arc-004`

## 5) Control-plane integration and channel modulation

Control plane consumes multi-source control signals and sets operating knobs:
- precision/gain routing
- commitment thresholds
- arousal/readiness/veto channels
- exploration/replay scheduling

With current extension pressure (MECH-063), modulation should be handled as orthogonal axes with tonic/phasic components.

Primary anchors:
- `docs/architecture/control_plane.md#arc-005`
- `docs/architecture/control_plane.md#mech-039`
- `docs/architecture/control_plane.md#mech-040`
- `docs/architecture/control_plane.md#mech-063`

## 6) Explicit trajectory construction (hippocampal systems)

Hippocampal systems chain E2 kernels under E1 constraints to produce explicit candidate trajectories.

Outputs at this stage:
- candidate rollout set for selection
- viability/path structure for comparison

Primary anchors:
- `docs/architecture/hippocampal_systems.md#arc-018`
- `docs/architecture/hippocampal_systems.md#mech-033`

## 7) Pre-commit evaluation and tri-loop gate arbitration (E3)

E3 receives candidate trajectories, control-plane state, and residue/constraint signals.

Gate family (MECH-062):
- motor gate
- cognitive-set gate
- motivational gate

Pre-commit error class (MECH-060):
- counterfactual/simulation mismatch
- conflict/effort/coherence penalties
- anticipated value and viability divergence

Primary anchors:
- `docs/architecture/e3.md#arc-003`
- `docs/architecture/e3.md#mech-062`
- `docs/architecture/agency_responsibility_flow.md#mech-060`

## 8) Commit boundary emission

At threshold crossing, E3 emits commit-boundary token (MECH-061).

Function of the token:
- marks the transition from hypothetical to attributable intervention
- binds downstream errors to `commit_id` for responsibility routing
- gates which signals count as post-commit learning evidence

Primary anchors:
- `docs/architecture/e3.md#mech-061`
- `docs/architecture/e3.md#q-015`

## 9) Action release and post-commit sensing loop

After commitment:
- `ACTION` is emitted
- new `SELF_SENSORY` and other stream observations return
- predicted vs observed consequences are compared

Post-commit error class (MECH-060):
- reafference mismatch
- realized outcome deviation
- cross-timescale attribution/credit signals

Primary anchors:
- `docs/architecture/sensory_stream_tags.md#arc-017`
- `docs/architecture/agency_responsibility_flow.md#mech-060`

## 10) Responsibility and durable update routing

Post-commit errors are routed into:
- E2 fast adaptation
- E1 slower model adjustment
- residue/constraint updates
- attribution and responsibility flow updates

Key separation:
- pre-commit error informs search/gating
- post-commit error informs ownership and durable adaptation

Primary anchors:
- `docs/architecture/agency_responsibility_flow.md#arc-015`
- `docs/architecture/agency_responsibility_flow.md#mech-057`
- `docs/architecture/e3.md#mech-061`

## 11) Replay and consolidation cycle

Committed trajectories and attribution outcomes feed replay/consolidation scheduling.

Outputs:
- updated rollout priors
- updated control-plane baselines
- updated commitment stability under new evidence

Primary anchors:
- `docs/architecture/hippocampal_systems.md#arc-007`
- `docs/architecture/sleep.md#arc-011`
- `docs/architecture/control_plane.md#arc-005`

## 12) Condensed routing summary

1. Tagged sensory streams -> shared sensory latent (`z_S`).
2. E2 expands near-horizon affordances (`z_A`) and fast residuals.
3. E1 supplies long-horizon priors and regime constraints.
4. Control plane sets precision/gating regime (including tonic/phasic axis state).
5. Hippocampal systems produce explicit trajectory candidates.
6. E3 tri-loop gates arbitrate and evaluate pre-commit errors.
7. Commit boundary token emitted at threshold crossing.
8. Action emitted; post-commit observations return.
9. Post-commit errors routed for attribution and durable updates.
10. Replay/consolidation integrates outcomes into future priors.

## 13) Dependency-retune implications

The trace implies the following dependency pressure is now central (already partly encoded):
- `MECH-061` should remain downstream of `MECH-060` and upstream of responsibility attribution interfaces.
- `MECH-062` should remain downstream of `ARC-003` and `ARC-005`, with explicit tie to arbitration policy (`Q-016`).
- `MECH-063` should stay tied to control-plane channel separation claims (`MECH-039/040/055`) and inform mode/regime wiring.

Open retune targets to inspect next:
- whether `ARC-015` should explicitly depend on `MECH-061` in claim registry,
- whether `MECH-057` should include `MECH-061` as a dependency when discussing attribution stability,
- whether `IMPL-023` dependency text should mention `MECH-061/062/063` for v2/v3 transition hooks.
