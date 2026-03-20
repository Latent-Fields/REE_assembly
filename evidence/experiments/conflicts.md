# Evidence Conflict Report

Generated: `2026-03-20T18:19:23.954393Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional | 2 | 1 | 0.667 | `20260319T090529Z_v3_exq_042_hippocampal_terrain_training_v3` | 3 |
| `ARC-016` | directional, mixed_evidence | 4 | 5 | 0.889 | `20260320T172009Z_v3_exq_018_arc016_dynamic_precision_v3` | 10 |
| `ARC-018` | directional | 1 | 1 | 1 | `20260320T073809Z_v3_exq_053_arc018_rollout_viability_v3` | 2 |
| `ARC-024` | directional, mixed_evidence | 2 | 3 | 0.8 | `20260319T201636Z_v3_exq_045_mech102_ethical_ttype_v3` | 11 |
| `MECH-033` | directional | 1 | 1 | 1 | `20260320T094747Z_v3_exq_055_mech033_kernel_chaining_v3` | 2 |
| `MECH-071` | directional, mixed_evidence | 4 | 1 | 0.4 | `20260319T075521Z_v3_exq_041_full_pipeline_smoke_test_v3` | 12 |
| `MECH-090` | directional, source_disagreement | 1 | 1 | 1 | `20260320T051926Z_v3_exq_049_mech090_beta_gate_v3` | 2 |
| `MECH-093` | directional, source_disagreement | 1 | 1 | 1 | `20260319T061623Z_v3_exq_038_arc016_precision_sweep_v3` | 2 |
| `MECH-098` | directional, source_disagreement, mixed_evidence | 5 | 5 | 1 | `20260320T171130Z_v3_exq_022_combined_contrastive_lstsq_v3` | 12 |
| `MECH-099` | directional, source_disagreement, mixed_evidence | 3 | 1 | 0.5 | `20260317T232006Z_v3_exq_017_combined_lateral_reafference_v3` | 5 |
| `MECH-102` | directional, mixed_evidence | 1 | 4 | 0.4 | `20260320T155429Z_v3_exq_059_sd010_mech102_advantage_v3` | 8 |
| `SD-003` | directional, mixed_evidence | 5 | 10 | 0.667 | `20260320T171130Z_v3_exq_022_combined_contrastive_lstsq_v3` | 35 |
| `SD-005` | directional, mixed_evidence | 3 | 1 | 0.5 | `20260319T213410Z_v3_exq_047_unified_vs_split_latent_v3` | 7 |
| `SD-007` | directional, mixed_evidence | 3 | 4 | 0.857 | `20260320T171130Z_v3_exq_022_combined_contrastive_lstsq_v3` | 9 |
| `SD-008` | directional | 1 | 3 | 0.5 | `20260319T070357Z_v3_exq_040_z_separation_alpha09_v3` | 4 |

## Conflict Details

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.688
- Recent entries:
  - `2026-03-08T11:46:44.792784+00:00` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-03-16T06:19:08.594368+00:00` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-03-19T09:05:29Z` `experimental` `claim_probe_sd_004` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-016
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=4, weakens=5, conflict_ratio=0.889, overall_confidence=0.724
- Recent entries:
  - `2026-03-18T20:17:24Z` `experimental` `claim_probe_arc_016` direction=`supports` confidence=0.75
  - `2026-03-18T20:18:53Z` `experimental` `claim_probe_arc_016` direction=`supports` confidence=0.75
  - `2026-03-19T06:16:23Z` `experimental` `claim_probe_arc_016` direction=`weakens` confidence=0.75
  - `2026-03-19T07:55:21Z` `experimental` `claim_probe_mech_089` direction=`supports` confidence=0.75
  - `2026-03-20T17:20:09Z` `experimental` `claim_probe_arc_016` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `v2_verdict_fail:precision_regime_probe` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.68
- Recent entries:
  - `2026-03-15T12:58:44.288398+00:00` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-03-20T07:38:09Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:rollout_viability_mapping` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-024
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=2, weakens=3, conflict_ratio=0.8, overall_confidence=0.599
- Recent entries:
  - `2026-03-19T05:49:52Z` `experimental` `claim_probe_mech_102` direction=`supports` confidence=0.75
  - `2026-03-19T05:50:00Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-19T06:06:18Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:07:20Z` `experimental` `claim_probe_mech_071` direction=`mixed` confidence=0.5
  - `2026-03-19T20:16:36Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.695
- Recent entries:
  - `2026-03-15T16:59:27.955457+00:00` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-03-20T09:47:47Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:kernel_chaining_interface` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-071
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.777
- Recent entries:
  - `2026-03-18T20:25:55Z` `experimental` `claim_probe_arc_025` direction=`supports` confidence=0.75
  - `2026-03-19T05:49:38Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:06:18Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T06:07:20Z` `experimental` `claim_probe_mech_071` direction=`mixed` confidence=0.5
  - `2026-03-19T07:55:21Z` `experimental` `claim_probe_mech_089` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:causal_attribution_calibration` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-090
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.756
- Recent entries:
  - `2026-03-16T12:00:00Z` `literature` `targeted_review_connectome_mech_090` direction=`supports` confidence=0.78
  - `2026-03-20T05:19:26Z` `experimental` `claim_probe_mech_090` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-093
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.74
- Recent entries:
  - `2026-03-16T12:00:00Z` `literature` `targeted_review_connectome_mech_093` direction=`supports` confidence=0.72
  - `2026-03-19T06:16:23Z` `experimental` `claim_probe_arc_016` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-098
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=5, weakens=5, conflict_ratio=1, overall_confidence=0.789
- Recent entries:
  - `2026-03-18T02:59:09Z` `experimental` `claim_probe_sd_007` direction=`mixed` confidence=0.5
  - `2026-03-18T18:03:01Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-18T18:03:16Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T20:17:02Z` `experimental` `claim_probe_sd_007` direction=`supports` confidence=0.75
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-099
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.848
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
- Evidence breakdown: supports=1, weakens=4, conflict_ratio=0.4, overall_confidence=0.785
- Recent entries:
  - `2026-03-19T10:43:27Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-19T20:16:06Z` `experimental` `claim_probe_sd_003` direction=`weakens` confidence=0.75
  - `2026-03-19T20:16:36Z` `experimental` `claim_probe_mech_102` direction=`weakens` confidence=0.75
  - `2026-03-20T06:23:30Z` `experimental` `claim_probe_mech_102` direction=`mixed` confidence=0.5
  - `2026-03-20T15:54:29Z` `experimental` `claim_probe_mech_102` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-003
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=5, weakens=10, conflict_ratio=0.667, overall_confidence=0.661
- Recent entries:
  - `2026-03-19T20:16:06Z` `experimental` `claim_probe_sd_003` direction=`weakens` confidence=0.75
  - `2026-03-20T06:22:50Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-20T15:53:54Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-20T16:51:49Z` `experimental` `claim_probe_mech_100` direction=`mixed` confidence=0.5
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-005
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.737
- Recent entries:
  - `2026-03-17T20:41:44Z` `experimental` `claim_probe_mech_095` direction=`mixed` confidence=0.5
  - `2026-03-17T22:51:09Z` `experimental` `claim_probe_sd_005` direction=`weakens` confidence=0.75
  - `2026-03-18T17:34:29Z` `experimental` `claim_probe_mech_071` direction=`supports` confidence=0.75
  - `2026-03-19T07:03:57Z` `experimental` `claim_probe_sd_005` direction=`supports` confidence=0.75
  - `2026-03-19T21:34:10Z` `experimental` `claim_probe_sd_005` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-007
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.584
- Recent entries:
  - `2026-03-18T18:03:01Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
  - `2026-03-18T18:03:16Z` `experimental` `claim_probe_sd_003` direction=`mixed` confidence=0.5
  - `2026-03-18T20:17:40Z` `experimental` `claim_probe_sd_003` direction=`supports` confidence=0.75
  - `2026-03-19T20:17:02Z` `experimental` `claim_probe_sd_007` direction=`supports` confidence=0.75
  - `2026-03-20T17:11:30Z` `experimental` `claim_probe_mech_100` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-008
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=3, conflict_ratio=0.5, overall_confidence=0.697
- Recent entries:
  - `2026-03-18T02:58:20Z` `experimental` `claim_probe_sd_008` direction=`weakens` confidence=0.75
  - `2026-03-18T03:16:43Z` `experimental` `claim_probe_sd_003` direction=`weakens` confidence=0.75
  - `2026-03-18T03:17:37Z` `experimental` `claim_probe_sd_003` direction=`weakens` confidence=0.75
  - `2026-03-19T07:03:57Z` `experimental` `claim_probe_sd_005` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
