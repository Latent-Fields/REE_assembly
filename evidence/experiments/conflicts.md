# Evidence Conflict Report

Generated: `2026-02-21T17:40:42.838182Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-003` | directional | 3 | 4 | 0.857 | `2026-02-15T213603Z_claim-probe-arc-003_seed1001_single_error_stream_toyenv_internal_minimal` | 7 |
| `ARC-007` | directional | 8 | 4 | 0.667 | `exp_0011_20260215T213710856170Z` | 12 |
| `ARC-018` | directional | 6 | 4 | 0.8 | `exp_0012_20260215T213710917446Z` | 10 |
| `MECH-033` | directional | 7 | 4 | 0.727 | `exp_0014_20260215T213723404871Z` | 11 |
| `MECH-040` | directional | 5 | 4 | 0.889 | `exp_0008_20260215T213710679868Z` | 9 |
| `MECH-046` | directional | 5 | 4 | 0.889 | `exp_0009_20260215T213710739916Z` | 9 |
| `MECH-056` | directional, source_disagreement | 21 | 74 | 0.442 | `2026-02-21T151443Z_trajectory-integrity_seed71_trajectory_first_enabled_toyenv_internal_minimal` | 95 |
| `MECH-057` | directional | 4 | 5 | 0.889 | `2026-02-15T213702Z_claim-probe-mech-057_seed1003_trajectory_first_enabled_toyenv_internal_minimal` | 9 |
| `MECH-058` | directional, mixed_evidence | 58 | 40 | 0.816 | `2026-02-21T151442Z_jepa-anchor-ablation_seed71_ema_anchor_on_toyenv_internal_minimal` | 99 |
| `MECH-059` | directional, mixed_evidence | 42 | 11 | 0.415 | `2026-02-21T151442Z_jepa-uncertainty-channels_seed71_explicit_uncertainty_head_toyenv_internal_minimal` | 103 |
| `MECH-060` | directional, mixed_evidence | 58 | 40 | 0.816 | `2026-02-21T151442Z_commit-dual-error-channels_seed71_pre_post_split_streams_toyenv_internal_minimal` | 99 |
| `MECH-061` | directional | 4 | 4 | 1 | `exp_0005_20260215T213657425679Z` | 8 |
| `Q-001` | directional | 7 | 4 | 0.727 | `exp_0018_20260215T213711149303Z` | 12 |
| `Q-002` | directional | 7 | 4 | 0.727 | `exp_0019_20260215T213711209047Z` | 12 |
| `Q-003` | directional | 7 | 4 | 0.727 | `exp_0020_20260215T213711269582Z` | 12 |
| `Q-004` | directional | 7 | 4 | 0.727 | `exp_0021_20260215T213711331429Z` | 12 |
| `Q-005` | directional | 7 | 4 | 0.727 | `exp_0022_20260215T213711393596Z` | 12 |
| `Q-006` | directional | 7 | 4 | 0.727 | `exp_0023_20260215T213711453369Z` | 12 |
| `Q-007` | directional | 8 | 4 | 0.667 | `exp_0015_20260217T225221918220Z` | 13 |
| `Q-012` | directional | 4 | 4 | 1 | `2026-02-15T213633Z_claim-probe-q-012_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 8 |
| `Q-013` | directional | 7 | 4 | 0.727 | `exp_0016_20260215T213711036144Z` | 11 |
| `Q-014` | directional | 7 | 4 | 0.727 | `exp_0017_20260215T213711090991Z` | 11 |
| `Q-015` | directional | 5 | 4 | 0.889 | `exp_0010_20260215T213710798125Z` | 9 |
| `Q-017` | directional, mixed_evidence | 57 | 40 | 0.825 | `2026-02-21T151442Z_control-axis-ablation_seed71_full_axis_toyenv_internal_minimal` | 98 |

## Conflict Details

### ARC-003
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.657
- Recent entries:
  - `2026-02-15T18:09:24.416725Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T18:09:24.496279Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:13Z` `experimental` `claim_probe_arc_003` direction=`weakens` confidence=0.75
  - `2026-02-15T21:10:33Z` `experimental` `claim_probe_arc_003` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:03Z` `experimental` `claim_probe_arc_003` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (4)
  - `mech060:attribution_reliability_break` (4)
  - `mech060:commitment_reversal_spike` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=8, weakens=4, conflict_ratio=0.667, overall_confidence=0.682
- Recent entries:
  - `2026-02-15T20:52:57.233345Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:31Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:01Z` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:57.544367Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:37:10.856170Z` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.682
- Recent entries:
  - `2026-02-15T20:52:17Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:37Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:08Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:37Z` `experimental` `claim_probe_arc_018` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:10.917446Z` `experimental` `claim_probe_arc_018` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.7
- Recent entries:
  - `2026-02-15T21:10:38Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:09Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:38Z` `experimental` `claim_probe_mech_033` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:10.977612Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
  - `2026-02-15T21:37:23.404871Z` `experimental` `claim_probe_mech_033` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-040
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.658
- Recent entries:
  - `2026-02-15T20:52:14Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:34Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:05Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:34Z` `experimental` `claim_probe_mech_040` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:10.679868Z` `experimental` `claim_probe_mech_040` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-046
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.648
- Recent entries:
  - `2026-02-15T20:52:15Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:35Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:06Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:35Z` `experimental` `claim_probe_mech_046` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:10.739916Z` `experimental` `claim_probe_mech_046` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=21, weakens=74, conflict_ratio=0.442, overall_confidence=0.795
- Recent entries:
  - `2026-02-21T15:12:23Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_056` direction=`weakens` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_056` direction=`weakens` confidence=0.75
  - `2026-02-21T15:14:43Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-21T15:14:43Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (70)
  - `domination_lock_in` (48)
  - `stop:ledger_edit_detected_count>0` (47)
  - `explanation_policy_divergence` (36)
  - `stop:domination_lock_in_events>0` (34)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-057
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=5, conflict_ratio=0.889, overall_confidence=0.705
- Recent entries:
  - `2026-02-15T20:52:30Z` `experimental` `claim_probe_mech_057` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:50Z` `experimental` `claim_probe_mech_057` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:21Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:50Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:02Z` `experimental` `claim_probe_mech_057` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=58, weakens=40, conflict_ratio=0.816, overall_confidence=0.72
- Recent entries:
  - `2026-02-21T15:12:23Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_058` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_058` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (36)
  - `mech058:ema_drift_under_shift` (10)
  - `threshold:latent_prediction_error_mean` (2)
  - `threshold:latent_prediction_error_p95` (2)
  - `threshold:latent_rollout_consistency_rate` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=42, weakens=11, conflict_ratio=0.415, overall_confidence=0.773
- Recent entries:
  - `2026-02-21T15:12:23Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_059` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_059` direction=`weakens` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (44)
  - `mech059:abstention_reliability_collapse` (36)
  - `threshold:latent_prediction_error_mean` (2)
  - `threshold:latent_uncertainty_calibration_error` (2)
  - `threshold:precision_input_completeness_rate` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=58, weakens=40, conflict_ratio=0.816, overall_confidence=0.709
- Recent entries:
  - `2026-02-21T15:12:23Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_060` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_mech_060` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (36)
  - `mech060:attribution_reliability_break` (36)
  - `mech060:commitment_reversal_spike` (36)
  - `threshold:pre_commit_error_signal_to_noise` (2)
  - `threshold:post_commit_error_attribution_gain` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-061
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.608
- Recent entries:
  - `2026-02-15T18:09:24.601905Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:15Z` `experimental` `claim_probe_mech_061` direction=`weakens` confidence=0.75
  - `2026-02-15T21:10:36Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:06Z` `experimental` `claim_probe_mech_061` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:57.425679Z` `experimental` `claim_probe_mech_061` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (4)
  - `mech060:attribution_reliability_break` (4)
  - `mech060:commitment_reversal_spike` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-001
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.591
- Recent entries:
  - `2026-02-15T20:52:21Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:42Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:13Z` `experimental` `claim_probe_q_001` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:41Z` `experimental` `claim_probe_q_001` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.149303Z` `experimental` `claim_probe_q_001` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-002
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.591
- Recent entries:
  - `2026-02-15T20:52:22Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:43Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:13Z` `experimental` `claim_probe_q_002` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:42Z` `experimental` `claim_probe_q_002` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.209047Z` `experimental` `claim_probe_q_002` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-003
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.591
- Recent entries:
  - `2026-02-15T20:52:23Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:43Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:14Z` `experimental` `claim_probe_q_003` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:43Z` `experimental` `claim_probe_q_003` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.269582Z` `experimental` `claim_probe_q_003` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-004
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.591
- Recent entries:
  - `2026-02-15T20:52:24Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:44Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:15Z` `experimental` `claim_probe_q_004` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:44Z` `experimental` `claim_probe_q_004` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.331429Z` `experimental` `claim_probe_q_004` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-005
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.591
- Recent entries:
  - `2026-02-15T20:52:25Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:45Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:16Z` `experimental` `claim_probe_q_005` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:45Z` `experimental` `claim_probe_q_005` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.393596Z` `experimental` `claim_probe_q_005` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-006
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.591
- Recent entries:
  - `2026-02-15T20:52:26Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:46Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:17Z` `experimental` `claim_probe_q_006` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:45Z` `experimental` `claim_probe_q_006` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.453369Z` `experimental` `claim_probe_q_006` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-007
- Conflict types: directional
- Evidence breakdown: supports=8, weakens=4, conflict_ratio=0.667, overall_confidence=0.615
- Recent entries:
  - `2026-02-15T21:10:47Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:18Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:46Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.511831Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-17T22:52:21.918220Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-012
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.652
- Recent entries:
  - `2026-02-15T18:05:24Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
  - `2026-02-15T20:52:12Z` `experimental` `claim_probe_q_012` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:32Z` `experimental` `claim_probe_q_012` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:02Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:33Z` `experimental` `claim_probe_q_012` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-013
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.645
- Recent entries:
  - `2026-02-15T20:52:20Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:39Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:10Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:39Z` `experimental` `claim_probe_q_013` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.036144Z` `experimental` `claim_probe_q_013` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-014
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.645
- Recent entries:
  - `2026-02-15T20:52:21Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:41Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:12Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:40Z` `experimental` `claim_probe_q_014` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.090991Z` `experimental` `claim_probe_q_014` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-015
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.638
- Recent entries:
  - `2026-02-15T20:52:16Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:36Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:07Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:36Z` `experimental` `claim_probe_q_015` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:10.798125Z` `experimental` `claim_probe_q_015` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-017
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=57, weakens=40, conflict_ratio=0.825, overall_confidence=0.729
- Recent entries:
  - `2026-02-21T15:06:50Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_q_017` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `claim_probe_q_017` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-21T15:14:42Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (36)
  - `q017:control_axis_entropy_collapse` (36)
  - `q017:control_axis_policy_loss_spike` (26)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
