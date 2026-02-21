# REE Architecture Streams and IDs (v1)

This file defines the canonical identifiers shared by:

- `architecture_static.mmd`
- `architecture_typed_dataflow.mmd`
- `episode_sequence.mmd`
- `stream_routing.v1.yaml`

## Canonical component identifiers

| ID | Role |
| --- | --- |
| `ENV.world_state` | External world state and consequences |
| `EXT.external_inputs` | External inputs from user/tool/sensor channels |
| `BOUNDARY.typed_payload_boundary` | Runtime typed ingress (`OBS`/`INS`) |
| `REE.shared_latent_substrate` | Shared JEPA-like latent substrate used by fast/slow regime adapters |
| `REE.E1_persistent_predictive_substrate` | Slow/deep regime adapter over shared substrate |
| `REE.E2_fast_forward_predictor` | Fast/near-horizon regime adapter over shared substrate |
| `REE.HippocampalSystems_rollout_and_provenance` | Explicit rollout generation and provenance binding |
| `REE.RC_reality_coherence_loop` | Reality-coherence conflict lane (`S5`/`RC_conflict`) |
| `REE.error_channel_router` | Tagged error bus with sink/write-locus gating |
| `REE.control_plane_router` | Control routing over stream/loop/global planes |
| `REE.thalamic_precision_relay` | Precision/delay relay from control plane into E1/E2/E3 |
| `REE.neuromodulatory_state_estimator` | Neuromodulatory state estimate (precision/gain regime input) |
| `REE.connectome_constraint_model` | Connectome/effective-connectivity constraint feedback for routing |
| `REE.E3_trajectory_selector` | Commitment gating and trajectory selection |
| `REE.associative_meta_calibration` | Outcome-vs-decision calibration for control-plane retuning |
| `REE.filter_context_anchor` | Pre-commit contextual/provenance eligibility filter |
| `REE.filter_body_feasible` | Pre-commit homeostasis/feasibility eligibility filter |
| `REE.filter_motivation_ok` | Pre-commit motivational sufficiency eligibility filter |
| `REE.filter_hard_veto` | Pre-commit hard-veto eligibility filter |
| `REE.gate_cognitive_set` | Cognitive-set commit gate |
| `REE.gate_motivational` | Motivational commit gate |
| `REE.gate_motor` | Motor/action release gate |
| `REE.gate_probe_sweep` | Rapid disinhibitory cross-check sweep before release |
| `REE.action_executor` | Action execution surface |
| `REE.post_commit_learning` | Post-commit attribution and durable update router |
| `REE.verifier` | Verifier for privileged commitment paths |
| `REE.trusted_stores_POL_ID_CAPS` | Trusted authority stores |

## Stream and signal identifiers

### Payload boundary types

- `payload.OBS`
- `payload.INS`
- `trusted.POL`
- `trusted.ID`
- `trusted.CAPS`

### Core stream tags (ARC-017)

- `stream.WORLD`
- `stream.HOMEOSTASIS`
- `stream.HARM`
- `stream.SELF_SENSORY`
- `stream.PRECISION`
- `stream.TEMPORAL_COHERENCE`
- `stream.REALITY_COHERENCE`
- `stream.VALENCE`
- `stream.ACTION`
- `stream.SELF_IMPACT`
- `stream.sim_error`
- `stream.realized_error`

### Shared-substrate predictive interface channels

- `latent.shared_state`
- `latent.slow_update_proposal`
- `latent.fast_update_proposal`
- `latent.prior_bundle`
- `forward_prediction_kernel`
- `rollout.candidates`
- `provenance.bindings`

### Tagged error-router channels

- `error.sensory_prediction`
- `error.action_prediction`
- `error.precommit_sim`
- `error.postcommit_outcome`
- `error.precommit_sim+error.action_prediction+error.sensory_prediction`
- `error.postcommit_outcome_replay`

### Control-plane signal and routing channels (MECH-004/064/065)

- `signal.S1_fast`
- `signal.S1_slow`
- `signal.S3_fast`
- `signal.S3_slow`
- `signal.S5_RC_conflict`
- `control.modulator_state`
- `route.candidate_profile`
- `route.constraint_feedback`
- `control.precision_bias_bundle`
- `control.precision_thal`
- `control.delay_bias_thal`
- `control.Pi_ext+Pi_prop`
- `control.Pi_int+Pi_rc+Pi_noc`
- `control.K3+K4+K5+K10`
- `control.P_cognitive`
- `control.meta_recalibration`
- `commit.inhibit`
- `search.widen`

### Predictive and gating interface channels

- `candidate_commit`
- `verifier.approve_or_deny`
- `gate_request`
- `gate_bias`
- `gate_probe.request`
- `gate_probe.policy`
- `gate_probe.inject`
- `gate_probe.response`
- `gate_probe.summary`
- `trusted.POL+ID+CAPS`
- `filter.context_anchor`
- `filter.motivation_ok`
- `eligibility.pass_or_fail`
- `eligibility.veto_state`

### Commit-boundary learning channels (MECH-060/061/062)

- `commit_boundary.tokenized_update`
- `post_commit.outcome_trace`
- `packet.decision_snapshot`
- `packet.outcome_snapshot`

## Logging event envelope (recommended)

```json
{
  "event_id": "evt_000001",
  "ts": "2026-02-21T00:00:00Z",
  "from": "REE.E2_fast_forward_predictor",
  "to": "REE.control_plane_router",
  "type": "signal.S1_fast",
  "phase": "pre_commit",
  "commit_id": null,
  "trace_id": "trace_abc123"
}
```

## Naming rules

1. Components use dotted identifiers with stable prefixes (`ENV`, `EXT`, `BOUNDARY`, `REE`).
2. Edge labels use loggable stream IDs (`stream.*`, `signal.*`, `payload.*`, `control.*`, `trusted.*`, `error.*`, `route.*`, `gate_probe.*`).
3. The same component IDs must appear in all three Mermaid views.
4. New channels are added to `stream_routing.v1.yaml` first, then diagram files are updated.
