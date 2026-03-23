# Evidence Conflict Report

Generated: `2026-03-23T10:53:35.434482Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional | 3 | 3 | 1 | `v3_exq_042_hippocampal_terrain_training_20260319T090529Z_v3` | 6 |
| `ARC-016` | directional, mixed_evidence | 10 | 9 | 0.947 | `20260321T131836Z_v3_exq_060_arc016_beta_gate_fixed_threshold_v3` | 21 |
| `ARC-018` | directional | 2 | 1 | 0.667 | `v3_exq_053_arc018_rollout_viability_20260320T073809Z_v3` | 3 |
| `ARC-024` | directional, mixed_evidence | 6 | 7 | 0.923 | `v3_exq_045_mech102_ethical_ttype_20260319T201636Z_v3` | 25 |
| `MECH-033` | directional | 4 | 1 | 0.4 | `v3_exq_055_mech033_kernel_chaining_20260320T191345Z_v3` | 5 |
| `MECH-071` | directional, mixed_evidence | 11 | 9 | 0.9 | `20260320T200725Z_v3_exq_058_arc027_harm_stream_calibration_v3` | 36 |
| `MECH-089` | directional, mixed_evidence | 8 | 3 | 0.545 | `2026-03-22_mech089_canolty_knight_cfc_2010` | 13 |
| `MECH-090` | directional, mixed_evidence | 7 | 4 | 0.727 | `v3_exq_062b_mech104_surprise_gate_spike_selectivity_20260322T220307Z_v3` | 19 |
| `MECH-093` | directional, source_disagreement, mixed_evidence | 1 | 4 | 0.4 | `v3_exq_038_arc016_precision_sweep_20260322T020909Z_v3` | 6 |
| `MECH-098` | directional, source_disagreement, mixed_evidence | 7 | 7 | 1 | `20260320T171130Z_v3_exq_022_combined_contrastive_lstsq_v3` | 18 |
| `MECH-099` | directional, source_disagreement, mixed_evidence | 3 | 1 | 0.5 | `20260317T232006Z_v3_exq_017_combined_lateral_reafference_v3` | 5 |
| `MECH-102` | directional, mixed_evidence | 3 | 9 | 0.5 | `v3_exq_059c_sd010_mech102_advantage_fixed_20260321T084609Z_v3` | 19 |
| `SD-003` | directional, mixed_evidence | 13 | 20 | 0.788 | `v3_exq_058c_sd010_sd003_attribution_fixed_20260320T212335Z_v3` | 67 |
| `SD-004` | directional | 3 | 2 | 0.8 | `v3_exq_042_hippocampal_terrain_training_20260319T090529Z_v3` | 5 |
| `SD-005` | directional, source_disagreement, mixed_evidence | 6 | 7 | 0.923 | `v3_exq_047d_sd005_info_probe_v2_20260322T134050Z_v3` | 20 |
| `SD-007` | directional, mixed_evidence | 7 | 7 | 1 | `v3_exq_057_sd010_reafference_isolation_20260322T014230Z_v3` | 18 |

## Conflict Details

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=3, conflict_ratio=1, overall_confidence=0.777
- Recent entries:
  - `2026-03-16T06:19:08.594368+00:00` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-03-19T07:00:48Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`weakens` confidence=0.75
  - `2026-03-19T07:02:43Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`weakens` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `claim_probe_sd_004` direction=`supports` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-016
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=10, weakens=9, conflict_ratio=0.947, overall_confidence=0.816
- Recent entries:
  - `2026-03-22T02:08:22Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`mixed` confidence=0.5
  - `2026-03-22T02:09:09Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
  - `2026-03-22T14:56:26.967166Z` `experimental` `v3_exq_059_arc016_beta_gate_fixed_threshold` direction=`weakens` confidence=0.75
  - `2026-03-22T14:56:26.969118Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-22T14:56:26.971046Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:precision_regime_probe` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.787
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
- Evidence breakdown: supports=6, weakens=7, conflict_ratio=0.923, overall_confidence=0.713
- Recent entries:
  - `2026-03-19T06:06:18Z` `experimental` `v3_exq_036_sd003_multistep_attribution` direction=`mixed` confidence=0.5
  - `2026-03-19T06:07:20Z` `experimental` `claim_probe_mech_071` direction=`mixed` confidence=0.5
  - `2026-03-19T06:07:20Z` `experimental` `v3_exq_039_training_progression` direction=`mixed` confidence=0.5
  - `2026-03-19T20:16:36Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T20:16:36Z` `experimental` `v3_exq_045_mech102_ethical_ttype` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.804
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
- Evidence breakdown: supports=11, weakens=9, conflict_ratio=0.9, overall_confidence=0.756
- Recent entries:
  - `2026-03-19T06:07:20Z` `experimental` `v3_exq_039_training_progression` direction=`mixed` confidence=0.5
  - `2026-03-19T07:00:39Z` `experimental` `v3_exq_041_full_pipeline_smoke_test` direction=`weakens` confidence=0.75
  - `2026-03-19T07:55:21Z` `experimental` `claim_probe_mech_089` direction=`supports` confidence=0.75
  - `2026-03-19T07:55:21Z` `experimental` `v3_exq_041_full_pipeline_smoke_test` direction=`supports` confidence=0.75
  - `2026-03-20T21:45:33.169911Z` `experimental` `v3_exq_058_arc027_harm_stream_calibration` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:causal_attribution_calibration` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-089
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=8, weakens=3, conflict_ratio=0.545, overall_confidence=0.821
- Recent entries:
  - `2026-03-19T09:05:29Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`supports` confidence=0.75
  - `2026-03-20T04:26:36Z` `experimental` `claim_probe_sd_006` direction=`mixed` confidence=0.5
  - `2026-03-20T04:26:36Z` `experimental` `v3_exq_052_sd006_multirate_validation` direction=`mixed` confidence=0.5
  - `2026-03-21T00:31:17Z` `experimental` `v3_exq_052b_sd006_multirate_fixed` direction=`supports` confidence=0.75
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_mech_089` direction=`supports` confidence=0.84
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-090
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.732
- Recent entries:
  - `2026-03-22T13:40:08Z` `experimental` `v3_exq_062a_mech104_surprise_gate_committed_only` direction=`mixed` confidence=0.5
  - `2026-03-22T14:56:26.967166Z` `experimental` `v3_exq_059_arc016_beta_gate_fixed_threshold` direction=`weakens` confidence=0.75
  - `2026-03-22T14:56:26.969118Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-22T14:56:26.971046Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-22T22:03:07Z` `experimental` `v3_exq_062b_mech104_surprise_gate_spike_selectivity` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `beta_as_idle_not_commitment` (1)
  - `sensorimotor_beta_desynchronizes_during_action` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-093
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=1, weakens=4, conflict_ratio=0.4, overall_confidence=0.565
- Recent entries:
  - `2026-03-19T06:13:50Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
  - `2026-03-19T06:16:23Z` `experimental` `claim_probe_arc_016` direction=`weakens` confidence=0.75
  - `2026-03-19T06:16:23Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
  - `2026-03-22T02:08:22Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`mixed` confidence=0.5
  - `2026-03-22T02:09:09Z` `experimental` `v3_exq_038_arc016_precision_sweep` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-098
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.77
- Recent entries:
  - `2026-03-18T18:03:16Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-18T18:03:16Z` `experimental` `v3_exq_027_sd003_v3_reafference` direction=`mixed` confidence=0.5
  - `2026-03-19T20:17:02Z` `experimental` `claim_probe_sd_007` direction=`supports` confidence=0.75
  - `2026-03-19T20:17:02Z` `experimental` `v3_exq_027b_sd007_reafference_diagnostic` direction=`supports` confidence=0.75
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-099
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.665
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
- Evidence breakdown: supports=3, weakens=9, conflict_ratio=0.5, overall_confidence=0.624
- Recent entries:
  - `2026-03-20T06:23:30Z` `experimental` `v3_exq_059_sd010_mech102_advantage` direction=`mixed` confidence=0.5
  - `2026-03-20T15:54:29Z` `experimental` `claim_probe_mech_102` direction=`mixed` confidence=0.5
  - `2026-03-20T15:54:29Z` `experimental` `v3_exq_059_sd010_mech102_advantage` direction=`mixed` confidence=0.5
  - `2026-03-20T19:34:34Z` `experimental` `v3_exq_059_sd010_mech102_advantage` direction=`mixed` confidence=0.5
  - `2026-03-21T08:46:09Z` `experimental` `v3_exq_059c_sd010_mech102_advantage_fixed` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-003
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=13, weakens=20, conflict_ratio=0.788, overall_confidence=0.684
- Recent entries:
  - `2026-03-20T16:51:49Z` `experimental` `claim_probe_mech_100` direction=`mixed` confidence=0.5
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-20T19:26:44Z` `experimental` `v3_exq_058c_sd010_sd003_attribution_fixed` direction=`mixed` confidence=0.5
  - `2026-03-20T19:33:55Z` `experimental` `v3_exq_058_sd010_sd003_attribution` direction=`mixed` confidence=0.5
  - `2026-03-20T21:23:35Z` `experimental` `v3_exq_058c_sd010_sd003_attribution_fixed` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-004
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=2, conflict_ratio=0.8, overall_confidence=0.786
- Recent entries:
  - `2026-03-16T21:45:54Z` `experimental` `claim_probe_sd_004` direction=`supports` confidence=0.75
  - `2026-03-19T07:00:48Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`weakens` confidence=0.75
  - `2026-03-19T07:02:43Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`weakens` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `claim_probe_sd_004` direction=`supports` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `v3_exq_042_hippocampal_terrain_training` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-005
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=6, weakens=7, conflict_ratio=0.923, overall_confidence=0.752
- Recent entries:
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_sd_005` direction=`mixed` confidence=0.68
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_sd_005` direction=`supports` confidence=0.8
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_sd_005` direction=`supports` confidence=0.77
  - `2026-03-22T13:21:06Z` `experimental` `v3_exq_047d_sd005_info_probe_v2` direction=`weakens` confidence=0.75
  - `2026-03-22T13:40:50Z` `experimental` `v3_exq_047d_sd005_info_probe_v2` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `shared_self_world_representation` (1)
  - `partial_overlap_in_z_self_z_world_substrates` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-007
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=7, conflict_ratio=1, overall_confidence=0.741
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
