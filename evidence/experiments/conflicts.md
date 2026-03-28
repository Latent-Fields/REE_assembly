# Evidence Conflict Report

Generated: `2026-03-28T11:20:38.158172Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional | 4 | 6 | 0.8 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 11 |
| `ARC-016` | directional, mixed_evidence | 11 | 13 | 0.917 | `v3_exq_101_harm_obs_a_normfix_20260327T175843Z_v3` | 28 |
| `ARC-018` | directional | 2 | 1 | 0.667 | `v3_exq_053_arc018_rollout_viability_20260320T073809Z_v3` | 3 |
| `ARC-024` | directional, mixed_evidence | 7 | 7 | 1 | `v3_exq_071_rollout_batched_attribution_20260323T143350Z_v3` | 27 |
| `MECH-033` | directional | 4 | 1 | 0.4 | `v3_exq_055_mech033_kernel_chaining_20260320T191345Z_v3` | 5 |
| `MECH-071` | directional, mixed_evidence | 11 | 10 | 0.952 | `v3_exq_085f_mech071_goal_wired_navigation_20260327T172024Z_v3` | 47 |
| `MECH-089` | directional, mixed_evidence | 9 | 3 | 0.5 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 16 |
| `MECH-090` | directional, mixed_evidence | 8 | 4 | 0.667 | `20260321T131836Z_v3_exq_060_arc016_beta_gate_fixed_threshold_v3` | 21 |
| `MECH-093` | directional, source_disagreement, mixed_evidence | 3 | 5 | 0.75 | `v3_exq_097b_mech093_heartbeat_rate_20260327T145329Z_v3` | 10 |
| `MECH-095` | directional, source_disagreement, mixed_evidence | 5 | 2 | 0.571 | `v3_exq_098b_mech099_agency_attribution_20260327T155605Z_v3` | 11 |
| `MECH-098` | directional, source_disagreement, mixed_evidence | 9 | 9 | 1 | `v3_exq_099a_mech098_reafference_upgrade_20260326T223306Z_v3` | 24 |
| `MECH-099` | directional, source_disagreement, mixed_evidence | 3 | 4 | 0.857 | `v3_exq_098b_mech099_agency_attribution_20260327T155605Z_v3` | 9 |
| `MECH-102` | directional, mixed_evidence | 3 | 10 | 0.462 | `v3_exq_080_mech102_depletion_ordering_20260323T131625Z_v3` | 23 |
| `MECH-135` | directional | 2 | 2 | 1 | `v3_exq_103_e2_training_horizon_ablation_20260328T100444Z_v3` | 4 |
| `SD-003` | directional, mixed_evidence | 13 | 20 | 0.788 | `v3_exq_095_harm_forward_model_sd003_20260325T021349Z_v3` | 71 |
| `SD-004` | directional | 3 | 5 | 0.75 | `v3_exq_046_arc007_path_memory_ablation_20260323T162327Z_v3` | 8 |
| `SD-005` | directional, source_disagreement, mixed_evidence | 10 | 13 | 0.87 | `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 32 |
| `SD-007` | directional, mixed_evidence | 7 | 7 | 1 | `v3_exq_057_sd010_reafference_isolation_20260322T014230Z_v3` | 18 |

## Conflict Details

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=6, conflict_ratio=0.8, overall_confidence=0.707
- Recent entries:
  - `2026-03-23T12:16:55Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-23T14:33:03Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-23T16:23:27Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-016
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=11, weakens=13, conflict_ratio=0.917, overall_confidence=0.799
- Recent entries:
  - `2026-03-26T16:35:11.936466Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-26T16:35:11.936824Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-27T17:21:37Z` `experimental` `v3_exq_100_z_harm_a_integration` direction=`mixed` confidence=0.5
  - `2026-03-27T17:42:57Z` `experimental` `v3_exq_100b_affective_harm_diagnostic` direction=`weakens` confidence=0.75
  - `2026-03-27T17:58:43Z` `experimental` `v3_exq_101_harm_obs_a_normfix` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:precision_regime_probe` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.75
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
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.727
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
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.828
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
- Evidence breakdown: supports=11, weakens=10, conflict_ratio=0.952, overall_confidence=0.757
- Recent entries:
  - `2026-03-24T20:22:10Z` `experimental` `v3_exq_085d_mech071_goal_persist` direction=`unknown` confidence=0.45
  - `2026-03-26T16:35:11.928901Z` `experimental` `v3_exq_058_arc027_harm_stream_calibration` direction=`supports` confidence=0.75
  - `2026-03-26T18:09:34Z` `experimental` `v3_exq_085e_mech071_drive_modulated_goal` direction=`mixed` confidence=0.5
  - `2026-03-27T17:09:48Z` `experimental` `v3_exq_085f_mech071_goal_wired_navigation` direction=`superseded` confidence=0.55
  - `2026-03-27T17:20:24Z` `experimental` `v3_exq_085f_mech071_goal_wired_navigation` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `v2_verdict_fail:causal_attribution_calibration` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-089
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=9, weakens=3, conflict_ratio=0.5, overall_confidence=0.829
- Recent entries:
  - `2026-03-21T00:31:17Z` `experimental` `v3_exq_052b_sd006_multirate_fixed` direction=`supports` confidence=0.75
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_mech_089` direction=`supports` confidence=0.84
  - `2026-03-23T10:10:09Z` `experimental` `v3_exq_066_mech089_theta_batching` direction=`mixed` confidence=0.5
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-090
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=8, weakens=4, conflict_ratio=0.667, overall_confidence=0.741
- Recent entries:
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
  - `2026-03-26T16:35:11.933414Z` `experimental` `v3_exq_059_arc016_beta_gate_fixed_threshold` direction=`weakens` confidence=0.75
  - `2026-03-26T16:35:11.936466Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-26T16:35:11.936824Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `beta_as_idle_not_commitment` (1)
  - `sensorimotor_beta_desynchronizes_during_action` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-093
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=5, conflict_ratio=0.75, overall_confidence=0.663
- Recent entries:
  - `2026-03-22T02:09:09Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
  - `2026-03-26T21:42:12Z` `experimental` `v3_exq_097_mech093_heartbeat_rate` direction=`weakens` confidence=0.75
  - `2026-03-27T14:53:29Z` `experimental` `v3_exq_097b_mech093_heartbeat_rate` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-095
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=5, weakens=2, conflict_ratio=0.571, overall_confidence=0.783
- Recent entries:
  - `2026-03-24T01:27:20Z` `experimental` `v3_exq_047i_tpj_routing_poc` direction=`weakens` confidence=0.75
  - `2026-03-24T20:23:13Z` `experimental` `v3_exq_047j_tpj_routing_ce` direction=`mixed` confidence=0.5
  - `2026-03-25T02:15:58Z` `experimental` `v3_exq_047k_tpj_routing_larger_n` direction=`supports` confidence=0.75
  - `2026-03-27T15:53:04Z` `experimental` `v3_exq_098b_mech099_agency_attribution` direction=`weakens` confidence=0.75
  - `2026-03-27T15:56:05Z` `experimental` `v3_exq_098b_mech099_agency_attribution` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-098
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=9, weakens=9, conflict_ratio=1, overall_confidence=0.792
- Recent entries:
  - `2026-03-23T13:17:11Z` `experimental` `v3_exq_082_mech098_reafference_harm_pair` direction=`mixed` confidence=0.5
  - `2026-03-26T22:05:24Z` `experimental` `v3_exq_099_mech098_reafference_upgrade` direction=`supports` confidence=0.75
  - `2026-03-26T22:05:44Z` `experimental` `v3_exq_099_mech098_reafference_upgrade` direction=`weakens` confidence=0.75
  - `2026-03-26T22:31:51Z` `experimental` `v3_exq_099a_mech098_reafference_upgrade` direction=`supports` confidence=0.75
  - `2026-03-26T22:33:06Z` `experimental` `v3_exq_099a_mech098_reafference_upgrade` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-099
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.695
- Recent entries:
  - `2026-03-17T23:20:06Z` `experimental` `claim_probe_mech_099` direction=`weakens` confidence=0.75
  - `2026-03-26T21:47:50Z` `experimental` `v3_exq_098_mech099_three_stream` direction=`weakens` confidence=0.75
  - `2026-03-26T21:49:28Z` `experimental` `v3_exq_098_mech099_three_stream` direction=`weakens` confidence=0.75
  - `2026-03-27T15:53:04Z` `experimental` `v3_exq_098b_mech099_agency_attribution` direction=`weakens` confidence=0.75
  - `2026-03-27T15:56:05Z` `experimental` `v3_exq_098b_mech099_agency_attribution` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-102
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=10, conflict_ratio=0.462, overall_confidence=0.607
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

### MECH-135
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=2, conflict_ratio=1, overall_confidence=0.7
- Recent entries:
  - `2026-03-28T09:54:13Z` `experimental` `v3_exq_103_e2_training_horizon_ablation` direction=`supports` confidence=0.75
  - `2026-03-28T09:54:19Z` `experimental` `v3_exq_104_e1_parallel_rollout` direction=`weakens` confidence=0.75
  - `2026-03-28T09:54:25Z` `experimental` `v3_exq_105_rollout_horizon_sweep` direction=`weakens` confidence=0.75
  - `2026-03-28T10:04:44Z` `experimental` `v3_exq_103_e2_training_horizon_ablation` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-003
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=13, weakens=20, conflict_ratio=0.788, overall_confidence=0.681
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
- Evidence breakdown: supports=3, weakens=5, conflict_ratio=0.75, overall_confidence=0.683
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
- Evidence breakdown: supports=10, weakens=13, conflict_ratio=0.87, overall_confidence=0.753
- Recent entries:
  - `2026-03-24T01:27:20Z` `experimental` `v3_exq_047i_tpj_routing_poc` direction=`weakens` confidence=0.75
  - `2026-03-24T20:23:13Z` `experimental` `v3_exq_047j_tpj_routing_ce` direction=`mixed` confidence=0.5
  - `2026-03-25T02:15:58Z` `experimental` `v3_exq_047k_tpj_routing_larger_n` direction=`supports` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
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
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.747
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
