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
| `REE.E1_persistent_predictive_substrate` | Deep, slow predictive substrate |
| `REE.E2_fast_forward_predictor` | Fast near-horizon predictor |
| `REE.HippocampalSystems_rollout_and_provenance` | Explicit rollout generation and provenance binding |
| `REE.RC_reality_coherence_loop` | Reality-coherence conflict lane (`S5`/`RC_conflict`) |
| `REE.control_plane_router` | Control routing over stream/loop/global planes |
| `REE.E3_trajectory_selector` | Commitment gating and trajectory selection |
| `REE.gate_cognitive_set` | Cognitive-set commit gate |
| `REE.gate_motivational` | Motivational commit gate |
| `REE.gate_motor` | Motor/action release gate |
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

### Control-plane signal classes (MECH-004/064/065)

- `signal.S1_fast`
- `signal.S1_slow`
- `signal.S3_fast`
- `signal.S3_slow`
- `signal.S5_RC_conflict`

### Predictive and gating interface channels

- `latent.prior_bundle`
- `forward_prediction_kernel`
- `rollout.candidates`
- `provenance.bindings`
- `candidate_commit`
- `verifier.approve_or_deny`
- `gate_request`
- `gate_bias`
- `trusted.POL+ID+CAPS`

### Control routing channels

- `control.Pi_ext+Pi_prop`
- `control.Pi_int+Pi_rc+Pi_noc`
- `control.K3+K4+K5+K10`
- `commit.inhibit`
- `search.widen`

### Commit-boundary learning channels (MECH-060/061/062)

- `stream.sim_error`
- `stream.realized_error`
- `commit_boundary.tokenized_update`
- `post_commit.outcome_trace`

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
2. Edge labels use loggable stream IDs (`stream.*`, `signal.*`, `payload.*`, `control.*`, `trusted.*`).
3. The same component IDs must appear in all three Mermaid views.
4. New channels are added to `stream_routing.v1.yaml` first, then diagram files are updated.
