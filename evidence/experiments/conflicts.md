# Evidence Conflict Report

Generated: `2026-03-25T06:09:15.172175Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional, mixed_evidence | 4 | 6 | 0.8 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 11 |
| `ARC-016` | directional, mixed_evidence | 11 | 11 | 1 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 25 |
| `ARC-018` | directional | 2 | 1 | 0.667 | `v3_exq_053_arc018_rollout_viability_20260320T073809Z_v3` | 3 |
| `ARC-024` | directional, mixed_evidence | 7 | 7 | 1 | `v3_exq_071_rollout_batched_attribution_20260323T143350Z_v3` | 27 |
| `MECH-033` | directional | 4 | 1 | 0.4 | `v3_exq_055_mech033_kernel_chaining_20260320T191345Z_v3` | 5 |
| `MECH-071` | directional, mixed_evidence | 11 | 10 | 0.952 | `v3_exq_085d_mech071_goal_persist_20260324T202210Z_v3` | 44 |
| `MECH-089` | directional, mixed_evidence | 9 | 3 | 0.5 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 16 |
| `MECH-090` | directional, mixed_evidence | 8 | 4 | 0.667 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 21 |
| `MECH-093` | directional, source_disagreement, mixed_evidence | 2 | 4 | 0.667 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 8 |
| `MECH-095` | directional, mixed_evidence | 5 | 1 | 0.333 | `v3_exq_047k_tpj_routing_larger_n_20260325T021558Z_v3` | 9 |
| `MECH-098` | directional, source_disagreement, mixed_evidence | 7 | 7 | 1 | `v3_exq_082_mech098_reafference_harm_pair_20260323T131711Z_v3` | 20 |
| `MECH-099` | directional, source_disagreement, mixed_evidence | 3 | 1 | 0.5 | `20260317T232006Z_v3_exq_017_combined_lateral_reafference_v3` | 5 |
| `MECH-102` | directional, mixed_evidence | 3 | 10 | 0.462 | `v3_exq_080_mech102_depletion_ordering_20260323T131625Z_v3` | 23 |
| `SD-003` | directional, mixed_evidence | 13 | 20 | 0.788 | `v3_exq_095_harm_forward_model_sd003_20260325T021349Z_v3` | 71 |
| `SD-004` | directional | 3 | 5 | 0.75 | `v3_exq_046_arc007_path_memory_ablation_20260323T162327Z_v3` | 8 |
| `SD-005` | directional, source_disagreement, mixed_evidence | 10 | 13 | 0.87 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 32 |
| `SD-007` | directional, mixed_evidence | 7 | 7 | 1 | `v3_exq_057_sd010_reafference_isolation_20260322T014230Z_v3` | 18 |

## Conflict Details

### ARC-007
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=4, weakens=6, conflict_ratio=0.8, overall_confidence=0.711
- Recent entries:
  - `2026-03-23T12:16:55Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-23T14:33:03Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-23T16:23:27Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`mixed` confidence=0.5
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-016
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=11, weakens=11, conflict_ratio=1, overall_confidence=0.81
- Recent entries:
  - `2026-03-22T14:56:26.971046Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-23T18:42:18Z` `experimental` `v3_exq_088_arc016_harm_variance_commit` direction=`weakens` confidence=0.75
  - `2026-03-24T17:25:36Z` `experimental` `v3_exq_094_arc016_rollout_e3_fix` direction=`weakens` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`mixed` confidence=0.5
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:precision_regime_probe` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.754
- Recent entries:
  - `2026-03-15T12:58:44.288398+00:00` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-03-20T07:38:09Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-03-20T07:38:09Z` `experimental` `v3_exq_053_arc018_rollout_viability` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:rollout_viability_mapping` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-024
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.734
- Recent entries:
  - `2026-03-19T06:07:20Z` `experimental` `v3_exq_039_training_progression` direction=`mixed` confidence=0.5
  - `2026-03-19T20:16:36Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T20:16:36Z` `experimental` `v3_exq_045_mech102_ethical_ttype` direction=`weakens` confidence=0.75
  - `2026-03-23T12:21:09Z` `experimental` `v3_exq_077_arc024_asymptotic_proxy_pair` direction=`supports` confidence=0.75
  - `2026-03-23T14:33:50Z` `experimental` `v3_exq_071_rollout_batched_attribution` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.832
- Recent entries:
  - `2026-03-15T16:59:27.955457+00:00` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-03-20T09:47:47Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-03-20T09:47:47Z` `experimental` `v3_exq_055_mech033_kernel_chaining` direction=`supports` confidence=0.75
  - `2026-03-20T19:13:45Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-03-20T19:13:45Z` `experimental` `v3_exq_055_mech033_kernel_chaining` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:kernel_chaining_interface` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-071
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=11, weakens=10, conflict_ratio=0.952, overall_confidence=0.759
- Recent entries:
  - `2026-03-23T14:33:50Z` `experimental` `v3_exq_071_rollout_batched_attribution` direction=`mixed` confidence=0.5
  - `2026-03-23T17:51:43Z` `experimental` `v3_exq_085_mech071_goal_directed_calibration` direction=`mixed` confidence=0.5
  - `2026-03-23T18:56:18Z` `experimental` `v3_exq_085_mech071_goal_directed_calibration` direction=`mixed` confidence=0.5
  - `2026-03-24T01:28:17Z` `experimental` `v3_exq_085c_mech071_curiosity_goal` direction=`mixed` confidence=0.5
  - `2026-03-24T20:22:10Z` `experimental` `v3_exq_085d_mech071_goal_persist` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `v2_verdict_fail:causal_attribution_calibration` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-089
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=9, weakens=3, conflict_ratio=0.5, overall_confidence=0.831
- Recent entries:
  - `2026-03-21T00:31:17Z` `experimental` `v3_exq_052b_sd006_multirate_fixed` direction=`supports` confidence=0.75
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_mech_089` direction=`supports` confidence=0.84
  - `2026-03-23T10:10:09Z` `experimental` `v3_exq_066_mech089_theta_batching` direction=`mixed` confidence=0.5
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`mixed` confidence=0.5
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-090
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=8, weakens=4, conflict_ratio=0.667, overall_confidence=0.743
- Recent entries:
  - `2026-03-22T14:56:26.969118Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-22T14:56:26.971046Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-22T22:03:07Z` `experimental` `v3_exq_062b_mech104_surprise_gate_spike_selectivity` direction=`supports` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`mixed` confidence=0.5
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `beta_as_idle_not_commitment` (1)
  - `sensorimotor_beta_desynchronizes_during_action` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-093
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=2, weakens=4, conflict_ratio=0.667, overall_confidence=0.633
- Recent entries:
  - `2026-03-19T06:16:23Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
  - `2026-03-22T02:08:22Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`mixed` confidence=0.5
  - `2026-03-22T02:09:09Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`mixed` confidence=0.5
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-095
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=5, weakens=1, conflict_ratio=0.333, overall_confidence=0.822
- Recent entries:
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.88
  - `2026-03-23T18:42:32Z` `experimental` `v3_exq_089_mech095_tpj_validation` direction=`mixed` confidence=0.5
  - `2026-03-24T01:27:20Z` `experimental` `v3_exq_047i_tpj_routing_poc` direction=`weakens` confidence=0.75
  - `2026-03-24T20:23:13Z` `experimental` `v3_exq_047j_tpj_routing_ce` direction=`mixed` confidence=0.5
  - `2026-03-25T02:15:58Z` `experimental` `v3_exq_047k_tpj_routing_larger_n` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-098
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.788
- Recent entries:
  - `2026-03-19T20:17:02Z` `experimental` `claim_probe_sd_007` direction=`supports` confidence=0.75
  - `2026-03-19T20:17:02Z` `experimental` `v3_exq_027b_sd007_reafference_diagnostic` direction=`supports` confidence=0.75
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-23T12:17:55Z` `experimental` `v3_exq_069_reafference_selectivity_pair` direction=`mixed` confidence=0.5
  - `2026-03-23T13:17:11Z` `experimental` `v3_exq_082_mech098_reafference_harm_pair` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-099
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.663
- Recent entries:
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.82
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.88
  - `2026-03-17T21:00:00Z` `literature` `targeted_review_reafference_streams` direction=`supports` confidence=0.86
  - `2026-03-17T23:17:48Z` `experimental` `claim_probe_mech_099` direction=`mixed` confidence=0.5
  - `2026-03-17T23:20:06Z` `experimental` `claim_probe_mech_099` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-102
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=10, conflict_ratio=0.462, overall_confidence=0.614
- Recent entries:
  - `2026-03-21T08:46:09Z` `experimental` `v3_exq_059c_sd010_mech102_advantage_fixed` direction=`supports` confidence=0.75
  - `2026-03-23T12:31:07Z` `experimental` `v3_exq_079_mech102_depletion_ordering` direction=`mixed` confidence=0.5
  - `2026-03-23T12:49:22Z` `experimental` `v3_exq_080_mech102_terminal_correction_pair` direction=`weakens` confidence=0.75
  - `2026-03-23T13:14:15Z` `experimental` `v3_exq_083_mech102_terminal_correction_pair` direction=`mixed` confidence=0.5
  - `2026-03-23T13:16:25Z` `experimental` `v3_exq_080_mech102_depletion_ordering` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-003
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=13, weakens=20, conflict_ratio=0.788, overall_confidence=0.688
- Recent entries:
  - `2026-03-20T21:23:35Z` `experimental` `v3_exq_058c_sd010_sd003_attribution_fixed` direction=`mixed` confidence=0.5
  - `2026-03-23T14:33:50Z` `experimental` `v3_exq_071_rollout_batched_attribution` direction=`mixed` confidence=0.5
  - `2026-03-23T18:41:50Z` `experimental` `v3_exq_087_harm_bridge_validation` direction=`mixed` confidence=0.5
  - `2026-03-24T17:25:12Z` `experimental` `v3_exq_093_harm_bridge_e3_fix` direction=`mixed` confidence=0.5
  - `2026-03-25T02:13:49Z` `experimental` `v3_exq_095_harm_forward_model_sd003` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-004
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=5, conflict_ratio=0.75, overall_confidence=0.69
- Recent entries:
  - `2026-03-19T09:05:29Z` `experimental` `claim_probe_sd_004` direction=`supports` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`supports` confidence=0.75
  - `2026-03-23T12:16:55Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-23T14:33:03Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-23T16:23:27Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-005
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=10, weakens=13, conflict_ratio=0.87, overall_confidence=0.756
- Recent entries:
  - `2026-03-24T01:27:20Z` `experimental` `v3_exq_047i_tpj_routing_poc` direction=`weakens` confidence=0.75
  - `2026-03-24T20:23:13Z` `experimental` `v3_exq_047j_tpj_routing_ce` direction=`mixed` confidence=0.5
  - `2026-03-25T02:15:58Z` `experimental` `v3_exq_047k_tpj_routing_larger_n` direction=`supports` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`mixed` confidence=0.5
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `shared_self_world_representation` (1)
  - `partial_overlap_in_z_self_z_world_substrates` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-007
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.754
- Recent entries:
  - `2026-03-18T20:17:40Z` `experimental` `v3_exq_029_sd003_proxy_gradient_world` direction=`supports` confidence=0.75
  - `2026-03-19T20:17:02Z` `experimental` `claim_probe_sd_007` direction=`supports` confidence=0.75
  - `2026-03-19T20:17:02Z` `experimental` `v3_exq_027b_sd007_reafference_diagnostic` direction=`supports` confidence=0.75
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-22T01:42:30Z` `experimental` `v3_exq_057_sd010_reafference_isolation` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
