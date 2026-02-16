# Evidence Conflict Report

Generated: `2026-02-16T15:09:35.081467Z`
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
| `MECH-056` | directional, source_disagreement | 11 | 22 | 0.667 | `exp_0004_20260215T211117389757Z` | 33 |
| `MECH-057` | directional | 4 | 5 | 0.889 | `2026-02-15T213702Z_claim-probe-mech-057_seed1003_trajectory_first_enabled_toyenv_internal_minimal` | 9 |
| `MECH-058` | directional, mixed_evidence | 22 | 14 | 0.778 | `2026-02-15_mech058_connectome_byol_asymmetry_analysis_2022` | 37 |
| `MECH-059` | directional, mixed_evidence | 14 | 1 | 0.133 | `2026-02-15T213803Z_claim-probe-mech-059_seed1008_deterministic_plus_dispersion_toyenv_internal_minimal` | 41 |
| `MECH-060` | directional, mixed_evidence | 22 | 14 | 0.778 | `2026-02-15_mech060_connectome_vjepa2_dual_loss_channels_arxiv2025` | 37 |
| `MECH-061` | directional | 4 | 4 | 1 | `exp_0005_20260215T213657425679Z` | 8 |
| `Q-001` | directional | 7 | 4 | 0.727 | `exp_0018_20260215T213711149303Z` | 12 |
| `Q-002` | directional | 7 | 4 | 0.727 | `exp_0019_20260215T213711209047Z` | 12 |
| `Q-003` | directional | 7 | 4 | 0.727 | `exp_0020_20260215T213711269582Z` | 12 |
| `Q-004` | directional | 7 | 4 | 0.727 | `exp_0021_20260215T213711331429Z` | 12 |
| `Q-005` | directional | 7 | 4 | 0.727 | `exp_0022_20260215T213711393596Z` | 12 |
| `Q-006` | directional | 7 | 4 | 0.727 | `exp_0023_20260215T213711453369Z` | 12 |
| `Q-007` | directional | 7 | 4 | 0.727 | `exp_0024_20260215T213711511831Z` | 12 |
| `Q-008` | directional | 7 | 5 | 0.833 | `exp_0015_20260216T150514802604Z` | 13 |
| `Q-009` | directional | 7 | 4 | 0.727 | `exp_0026_20260215T213711626687Z` | 12 |
| `Q-010` | directional | 7 | 4 | 0.727 | `exp_0027_20260215T213711687120Z` | 12 |
| `Q-012` | directional | 4 | 4 | 1 | `2026-02-15T213633Z_claim-probe-q-012_seed1002_trajectory_first_enabled_toyenv_internal_minimal` | 8 |
| `Q-013` | directional | 7 | 4 | 0.727 | `exp_0016_20260215T213711036144Z` | 11 |
| `Q-014` | directional | 7 | 4 | 0.727 | `exp_0017_20260215T213711090991Z` | 11 |
| `Q-015` | directional | 5 | 4 | 0.889 | `exp_0010_20260215T213710798125Z` | 9 |
| `Q-017` | directional, mixed_evidence | 23 | 16 | 0.821 | `exp_0006_20260215T213657486711Z` | 40 |

## Conflict Details

### ARC-003
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.665
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
- Evidence breakdown: supports=8, weakens=4, conflict_ratio=0.667, overall_confidence=0.691
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
- Evidence breakdown: supports=6, weakens=4, conflict_ratio=0.8, overall_confidence=0.689
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.706
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
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.666
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
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.656
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
- Evidence breakdown: supports=11, weakens=22, conflict_ratio=0.667, overall_confidence=0.749
- Recent entries:
  - `2026-02-15T18:07:10.784771Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T18:07:10.843991Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:57.289360Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T20:52:57.348626Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-15T21:11:17.389757Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (20)
  - `stop:ledger_edit_detected_count>0` (20)
  - `domination_lock_in` (16)
  - `stop:domination_lock_in_events>0` (16)
  - `explanation_policy_divergence` (12)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-057
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=5, conflict_ratio=0.889, overall_confidence=0.711
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
- Evidence breakdown: supports=22, weakens=14, conflict_ratio=0.778, overall_confidence=0.709
- Recent entries:
  - `2026-02-15T21:11:17.270833Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T21:28:00Z` `literature` `targeted_review_connectome_mech_058` direction=`supports` confidence=0.78
  - `2026-02-15T21:29:00Z` `literature` `targeted_review_connectome_mech_058` direction=`supports` confidence=0.75
  - `2026-02-15T21:30:00Z` `literature` `targeted_review_connectome_mech_058` direction=`mixed` confidence=0.69
  - `2026-02-15T21:31:00Z` `literature` `targeted_review_connectome_mech_058` direction=`supports` confidence=0.71
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (12)
  - `mech058:ema_drift_under_shift` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=14, weakens=1, conflict_ratio=0.133, overall_confidence=0.765
- Recent entries:
  - `2026-02-15T21:37:16Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:37:28Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:37:39Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:37:51Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
  - `2026-02-15T21:38:03Z` `experimental` `claim_probe_mech_059` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (18)
  - `mech059:abstention_reliability_collapse` (18)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=22, weakens=14, conflict_ratio=0.778, overall_confidence=0.698
- Recent entries:
  - `2026-02-15T21:11:17.331544Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T21:24:00Z` `literature` `targeted_review_connectome_mech_060` direction=`supports` confidence=0.73
  - `2026-02-15T21:25:00Z` `literature` `targeted_review_connectome_mech_060` direction=`supports` confidence=0.79
  - `2026-02-15T21:26:00Z` `literature` `targeted_review_connectome_mech_060` direction=`supports` confidence=0.76
  - `2026-02-15T21:27:00Z` `literature` `targeted_review_connectome_mech_060` direction=`mixed` confidence=0.64
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (12)
  - `mech060:attribution_reliability_break` (12)
  - `mech060:commitment_reversal_spike` (12)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-061
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.615
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
- Recent entries:
  - `2026-02-15T20:52:26Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:47Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:18Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:46Z` `experimental` `claim_probe_q_007` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.511831Z` `experimental` `claim_probe_q_007` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-008
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=5, conflict_ratio=0.833, overall_confidence=0.565
- Recent entries:
  - `2026-02-15T21:10:48Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:18Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:47Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.570483Z` `experimental` `claim_probe_q_008` direction=`supports` confidence=0.75
  - `2026-02-16T15:05:14.802604Z` `experimental` `claim_probe_q_008` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-009
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
- Recent entries:
  - `2026-02-15T20:52:28Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:48Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:19Z` `experimental` `claim_probe_q_009` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:48Z` `experimental` `claim_probe_q_009` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.626687Z` `experimental` `claim_probe_q_009` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-010
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.6
- Recent entries:
  - `2026-02-15T20:52:29Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T21:10:49Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
  - `2026-02-15T21:36:20Z` `experimental` `claim_probe_q_010` direction=`weakens` confidence=0.75
  - `2026-02-15T21:36:49Z` `experimental` `claim_probe_q_010` direction=`weakens` confidence=0.75
  - `2026-02-15T21:37:11.687120Z` `experimental` `claim_probe_q_010` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (4)
  - `domination_lock_in` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-012
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.658
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.652
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
- Evidence breakdown: supports=7, weakens=4, conflict_ratio=0.727, overall_confidence=0.652
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
- Evidence breakdown: supports=5, weakens=4, conflict_ratio=0.889, overall_confidence=0.645
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
- Evidence breakdown: supports=23, weakens=16, conflict_ratio=0.821, overall_confidence=0.713
- Recent entries:
  - `2026-02-15T21:20:00Z` `literature` `targeted_review_connectome_q_017` direction=`supports` confidence=0.78
  - `2026-02-15T21:21:00Z` `literature` `targeted_review_connectome_q_017` direction=`supports` confidence=0.8
  - `2026-02-15T21:22:00Z` `literature` `targeted_review_connectome_q_017` direction=`supports` confidence=0.74
  - `2026-02-15T21:23:00Z` `literature` `targeted_review_connectome_q_017` direction=`mixed` confidence=0.72
  - `2026-02-15T21:36:57.486711Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (12)
  - `q017:control_axis_entropy_collapse` (12)
  - `q017:control_axis_policy_loss_spike` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
