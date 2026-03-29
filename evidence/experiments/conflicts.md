# Evidence Conflict Report

Generated: `2026-03-29T12:23:52.494031Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional, source_disagreement, mixed_evidence | 8 | 6 | 0.857 | `2026-03-29_arc_007_theta_sequences_goals_wikenheiser2015` | 16 |
| `ARC-016` | directional, source_disagreement, mixed_evidence | 13 | 13 | 1 | `2026-03-28_arc_016_threshold_striatum_presma_forstmann2008` | 30 |
| `ARC-018` | directional | 7 | 1 | 0.25 | `2026-03-29_arc_018_prioritized_replay_mattar2018` | 8 |
| `ARC-024` | directional, mixed_evidence | 13 | 9 | 0.818 | `2026-03-28_arc_024_threat_proximity_gradient_mobbs2007` | 33 |
| `MECH-033` | directional, mixed_evidence | 7 | 1 | 0.25 | `2026-03-29_mech_033_preplay_prospective_olafsdottir2015` | 9 |
| `MECH-071` | directional, mixed_evidence | 18 | 11 | 0.759 | `2026-03-29_mech_071_threat_imminence_gradient_mobbs2007` | 53 |
| `MECH-089` | directional, mixed_evidence | 9 | 4 | 0.615 | `v3_exq_122_mech089_theta_integration_pair_20260328T200134Z_v3` | 17 |
| `MECH-090` | directional, mixed_evidence | 8 | 4 | 0.667 | `v3_exq_119_mech090_beta_gate_pair_20260328T213307Z_v3` | 22 |
| `MECH-093` | directional, source_disagreement, mixed_evidence | 4 | 5 | 0.889 | `v3_exq_116_mech093_heartbeat_multiseed_20260328T211756Z_v3` | 11 |
| `MECH-095` | directional, source_disagreement, mixed_evidence | 5 | 2 | 0.571 | `v3_exq_121_mech095_agency_attribution_pair_20260328T195503Z_v3` | 12 |
| `MECH-098` | directional, source_disagreement, mixed_evidence | 9 | 12 | 0.857 | `v3_exq_110_c1fail_20260328T161637Z_v3` | 27 |
| `MECH-099` | directional, source_disagreement, mixed_evidence | 3 | 4 | 0.857 | `v3_exq_098b_mech099_agency_attribution_20260327T155605Z_v3` | 9 |
| `MECH-102` | directional, source_disagreement, mixed_evidence | 5 | 10 | 0.667 | `2026-03-29_mech_102_just_war_last_resort_aloyo2015` | 27 |
| `MECH-104` | directional, mixed_evidence | 7 | 1 | 0.25 | `2026-03-29_mech_104_unexpected_uncertainty_ne_yudayan2005` | 10 |
| `MECH-135` | directional, mixed_evidence | 7 | 2 | 0.444 | `2026-03-29_mech_135_mosaic_parallel_forward_models_wolpert1998` | 15 |
| `Q-020` | directional | 1 | 2 | 0.667 | `2026-03-29_q020_value_free_map_duvelle2019` | 3 |
| `SD-003` | directional, source_disagreement, mixed_evidence | 17 | 23 | 0.85 | `v3_exq_115_sd003_zharms_counterfactual_20260328T204836Z_v3` | 78 |
| `SD-004` | directional, source_disagreement | 7 | 5 | 0.833 | `2026-03-29_sd_004_theta_sequences_goals_wikenheiser2015` | 12 |
| `SD-005` | directional, source_disagreement, mixed_evidence | 10 | 14 | 0.833 | `v3_exq_113_sd005_double_dissociation_20260328T162148Z_v3` | 33 |
| `SD-007` | directional, source_disagreement, mixed_evidence | 12 | 9 | 0.857 | `v3_exq_118_c1fail_20260328T212454Z_v3` | 25 |
| `SD-011` | directional, source_disagreement, mixed_evidence | 6 | 3 | 0.667 | `2026-03-29_sd_011_spinothalamic_ascending_pathways_willis1997` | 17 |

## Conflict Details

### ARC-007
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=8, weakens=6, conflict_ratio=0.857, overall_confidence=0.8
- Recent entries:
  - `2026-03-28T20:48:15Z` `experimental` `v3_exq_114_arc007_path_memory_probe` direction=`supports` confidence=0.75
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_arc_007` direction=`mixed` confidence=0.6
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_arc_007` direction=`supports` confidence=0.82
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_arc_007` direction=`supports` confidence=0.74
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_arc_007` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
  - `The paper does not provide evidence that harm or causal attribution specifically is used as an organising axis for hippocampal maps — the non-spatial examples are relational/semantic, not harm-weighted.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-016
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=13, weakens=13, conflict_ratio=1, overall_confidence=0.802
- Recent entries:
  - `2026-03-27T17:21:37Z` `experimental` `v3_exq_100_z_harm_a_integration` direction=`mixed` confidence=0.5
  - `2026-03-27T17:42:57Z` `experimental` `v3_exq_100b_affective_harm_diagnostic` direction=`weakens` confidence=0.75
  - `2026-03-27T17:58:43Z` `experimental` `v3_exq_101_harm_obs_a_normfix` direction=`weakens` confidence=0.75
  - `2026-03-28T23:55:00Z` `literature` `targeted_review_connectome_arc_016` direction=`supports` confidence=0.76
  - `2026-03-28T23:55:00Z` `literature` `targeted_review_connectome_arc_016` direction=`supports` confidence=0.74
- Recurring failure signatures:
  - `v2_verdict_fail:precision_regime_probe` (2)
  - `The model addresses tonic dopamine modulation of global precision rather than the local, phasic variance computation REE proposes (E3-derived variance from a specific predictive model).` (1)
  - `The affordance/action-selection framing is specific to motor hierarchy; the REE BetaGate operates at a cognitive control level that is not directly modelled.` (1)
  - `Simulated Parkinson's-like deficits are presented as validation, but this requires the transfer from pathological to healthy-optimal to REE agent which is speculative.` (1)
  - `The threshold manipulation is externally imposed (speed-accuracy cues) not internally derived from prediction uncertainty, unlike ARC-016's E3-derived variance mechanism.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=7, weakens=1, conflict_ratio=0.25, overall_confidence=0.772
- Recent entries:
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_arc_018` direction=`supports` confidence=0.78
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_arc_018` direction=`supports` confidence=0.85
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_arc_018` direction=`supports` confidence=0.68
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_arc_018` direction=`supports` confidence=0.72
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_arc_018` direction=`supports` confidence=0.8
- Recurring failure signatures:
  - `v2_verdict_fail:rollout_viability_mapping` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### ARC-024
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=13, weakens=9, conflict_ratio=0.818, overall_confidence=0.788
- Recent entries:
  - `2026-03-28T18:12:25Z` `experimental` `v3_exq_071d_rollout_batched_attribution` direction=`supports` confidence=0.55
  - `2026-03-28T21:24:50Z` `experimental` `v3_exq_117_arc024_harm_benefit_gradient_pair` direction=`weakens` confidence=0.75
  - `2026-03-28T23:45:00Z` `literature` `targeted_review_arc_024` direction=`supports` confidence=0.78
  - `2026-03-28T23:45:00Z` `literature` `targeted_review_arc_024` direction=`supports` confidence=0.7
  - `2026-03-28T23:45:00Z` `literature` `targeted_review_arc_024` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `PIC theory describes three discrete modes rather than a fully continuous gradient; the transitions between modes are threshold-like, which could be interpreted as arguing for partial discreteness rather than pure continuous gradient structure.` (1)
  - `Primarily rodent literature; human PIC research (including Mobbs 2007) is referenced but not the primary evidence base of this review.` (1)
  - `The review's focus is on sustained threat and BST/hippocampal circuits rather than the gradient structure per se; the gradient argument must be inferred from the broader PIC framework.` (1)
  - `Temporal prediction gradients (cue1 -> cue2 -> pain) are structurally analogous to but not identical with spatial proximity gradients (distance to hazard).` (1)
  - `Ventral striatum/insula activity reflects reward-prediction-error signals, not the harm gradient field directly; the mapping to CausalGridWorldV2's hazard_field requires additional theoretical steps.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=1, conflict_ratio=0.25, overall_confidence=0.841
- Recent entries:
  - `2026-03-20T19:13:45Z` `experimental` `v3_exq_055_mech033_kernel_chaining` direction=`supports` confidence=0.75
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_033` direction=`supports` confidence=0.75
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_033` direction=`supports` confidence=0.78
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_033` direction=`supports` confidence=0.72
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_033` direction=`mixed` confidence=0.58
- Recurring failure signatures:
  - `v2_verdict_fail:kernel_chaining_interface` (1)
  - `Preplay sequences are statistically indistinguishable from random population activity in some analyses, raising the possibility that apparent 'preplay' reflects post-hoc alignment rather than genuine prospective computation -- which would undercut the rollout-seeding interpretation.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-071
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=18, weakens=11, conflict_ratio=0.759, overall_confidence=0.831
- Recent entries:
  - `2026-03-28T18:12:25Z` `experimental` `v3_exq_071d_rollout_batched_attribution` direction=`supports` confidence=0.55
  - `2026-03-29T12:15:00Z` `literature` `targeted_review_connectome_mech_071` direction=`supports` confidence=0.72
  - `2026-03-29T12:15:00Z` `literature` `targeted_review_connectome_mech_071` direction=`supports` confidence=0.8
  - `2026-03-29T12:15:00Z` `literature` `targeted_review_connectome_mech_071` direction=`supports` confidence=0.82
  - `2026-03-29T12:15:00Z` `literature` `targeted_review_connectome_mech_071` direction=`supports` confidence=0.77
- Recurring failure signatures:
  - `v2_verdict_fail:causal_attribution_calibration` (1)
  - `If E2/E3 harm prediction errors are not differentially routed based on causal attribution (agent-caused vs environment-caused), the dorsal/ventral striatum dissociation predicted by this paper would not appear in REE's architecture.` (1)
  - `If the insula-to-striatum gating of causal beliefs is absent in harm-specific circuits, MECH-071's calibration asymmetry would need a different implementation route.` (1)
  - `If E2 cannot distinguish self-generated from environment-generated harm events at the latent level, this cerebellar forward-model architecture would predict identical somatosensory responses -- the opposite of what the paper shows.` (1)
  - `If E2 harm prediction shows no agent/environment differential in calibration quality under identical physical harm magnitudes, the sensory attenuation mechanism this paper establishes would be disconfirmed as a route to MECH-071.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-089
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=9, weakens=4, conflict_ratio=0.615, overall_confidence=0.817
- Recent entries:
  - `2026-03-22T12:00:00Z` `literature` `targeted_review_connectome_mech_089` direction=`supports` confidence=0.84
  - `2026-03-23T10:10:09Z` `experimental` `v3_exq_066_mech089_theta_batching` direction=`mixed` confidence=0.5
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
  - `2026-03-28T20:01:34Z` `experimental` `v3_exq_122_mech089_theta_integration_pair` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-090
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=8, weakens=4, conflict_ratio=0.667, overall_confidence=0.741
- Recent entries:
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
  - `2026-03-26T16:35:11.933414Z` `experimental` `v3_exq_059_arc016_beta_gate_fixed_threshold` direction=`weakens` confidence=0.75
  - `2026-03-26T16:35:11.936466Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-26T16:35:11.936824Z` `experimental` `v3_exq_060_arc016_beta_gate_fixed_threshold` direction=`supports` confidence=0.75
  - `2026-03-28T21:33:07Z` `experimental` `v3_exq_119_mech090_beta_gate_pair` direction=`mixed` confidence=0.5
- Recurring failure signatures:
  - `beta_as_idle_not_commitment` (1)
  - `sensorimotor_beta_desynchronizes_during_action` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-093
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=4, weakens=5, conflict_ratio=0.889, overall_confidence=0.694
- Recent entries:
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
  - `2026-03-26T21:42:12Z` `experimental` `v3_exq_097_mech093_heartbeat_rate` direction=`weakens` confidence=0.75
  - `2026-03-27T14:53:29Z` `experimental` `v3_exq_097b_mech093_heartbeat_rate` direction=`supports` confidence=0.75
  - `2026-03-28T21:17:56Z` `experimental` `v3_exq_116_mech093_heartbeat_multiseed` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-095
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=5, weakens=2, conflict_ratio=0.571, overall_confidence=0.783
- Recent entries:
  - `2026-03-24T20:23:13Z` `experimental` `v3_exq_047j_tpj_routing_ce` direction=`mixed` confidence=0.5
  - `2026-03-25T02:15:58Z` `experimental` `v3_exq_047k_tpj_routing_larger_n` direction=`supports` confidence=0.75
  - `2026-03-27T15:53:04Z` `experimental` `v3_exq_098b_mech099_agency_attribution` direction=`weakens` confidence=0.75
  - `2026-03-27T15:56:05Z` `experimental` `v3_exq_098b_mech099_agency_attribution` direction=`mixed` confidence=0.5
  - `2026-03-28T19:55:03Z` `experimental` `v3_exq_121_mech095_agency_attribution_pair` direction=`mixed` confidence=0.5
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-098
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=9, weakens=12, conflict_ratio=0.857, overall_confidence=0.774
- Recent entries:
  - `2026-03-26T22:31:51Z` `experimental` `v3_exq_099a_mech098_reafference_upgrade` direction=`supports` confidence=0.75
  - `2026-03-26T22:33:06Z` `experimental` `v3_exq_099a_mech098_reafference_upgrade` direction=`weakens` confidence=0.75
  - `2026-03-28T20:51:48.344843Z` `experimental` `v3_exq_110_mech098_reafference_pair` direction=`weakens` confidence=0.75
  - `2026-03-28T20:51:48.345582Z` `experimental` `v3_exq_110_mech098_reafference_pair` direction=`weakens` confidence=0.75
  - `2026-03-28T20:51:48.346204Z` `experimental` `v3_exq_110_mech098_reafference_pair` direction=`weakens` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-099
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=3, weakens=4, conflict_ratio=0.857, overall_confidence=0.692
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
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=5, weakens=10, conflict_ratio=0.667, overall_confidence=0.713
- Recent entries:
  - `2026-03-23T13:16:25Z` `experimental` `v3_exq_080_mech102_depletion_ordering` direction=`mixed` confidence=0.5
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_mech_102` direction=`supports` confidence=0.67
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_mech_102` direction=`supports` confidence=0.7
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_mech_102` direction=`mixed` confidence=0.62
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_mech_102` direction=`mixed` confidence=0.58
- Recurring failure signatures:
  - `The GAM does not require prior exhaustion of non-violent coordination alternatives before aggression is triggered -- it can be activated by hostile attribution bias, provocation cues, or script activation without pathway closure.` (1)
  - `Aloyo argues that all accounts of last resort either generate wrong policy recommendations or reduce to proportionality, suggesting the 'sequential exhaustion' framing of MECH-102 may face analogous philosophical problems at the institutional level.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-104
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=1, conflict_ratio=0.25, overall_confidence=0.876
- Recent entries:
  - `2026-03-28T20:30:37Z` `experimental` `v3_exq_126_mech104_surprise_gate_pair` direction=`weakens` confidence=0.75
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_104` direction=`supports` confidence=0.82
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_104` direction=`supports` confidence=0.78
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_104` direction=`supports` confidence=0.8
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_mech_104` direction=`supports` confidence=0.79
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-135
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=7, weakens=2, conflict_ratio=0.444, overall_confidence=0.83
- Recent entries:
  - `2026-03-28T19:53:41Z` `experimental` `v3_exq_108_mech135_discriminative_pair` direction=`superseded` confidence=0.55
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_mech_135` direction=`supports` confidence=0.68
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_mech_135` direction=`supports` confidence=0.74
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_mech_135` direction=`mixed` confidence=0.55
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_mech_135` direction=`supports` confidence=0.72
- Recurring failure signatures:
  - `Ito's framework does not specify whether cerebellar internal models run simultaneously with cortical state updates or whether they run in an interleaved/sequential fashion. The co-evolution timing claim in MECH-135 is not directly addressed.` (1)
  - `The paper's evidence for Kalman-filter-style parallel computation is primarily in the motor domain; the extension to cognitive/planning functions is speculative and not demonstrated.` (1)
  - `The separate MF projection finding is morphological and compatible with sequential gating architectures as well as parallel ones -- it is a necessary but not sufficient condition for parallel co-evolution.` (1)
  - `GRASP uses a single world model with parallelized state optimization across time -- it does not involve two separate models (fast/cerebellar and slow/cortical) co-evolving. The dual-model structure of MECH-135 is not tested.` (1)
  - `The 'lifted states' formulation with soft dynamics constraints is a gradient-based optimization technique, not a biological parallel computation -- the mapping to cerebellar-cortical co-evolution requires significant additional bridging.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-020
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=2, conflict_ratio=0.667, overall_confidence=0.675
- Recent entries:
  - `2026-03-29T15:00:00Z` `literature` `targeted_review_q_020` direction=`weakens` confidence=0.78
  - `2026-03-29T15:00:00Z` `literature` `targeted_review_q_020` direction=`weakens` confidence=0.72
  - `2026-03-29T15:00:00Z` `literature` `targeted_review_q_020` direction=`supports` confidence=0.65
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-003
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=17, weakens=23, conflict_ratio=0.85, overall_confidence=0.765
- Recent entries:
  - `2026-03-28T00:00:00Z` `literature` `targeted_review_sd_003` direction=`supports` confidence=0.76
  - `2026-03-28T00:00:00Z` `literature` `targeted_review_sd_003` direction=`supports` confidence=0.68
  - `2026-03-28T16:16:34Z` `experimental` `v3_exq_109_sd003_harm_counterfactual` direction=`weakens` confidence=0.75
  - `2026-03-28T18:12:25Z` `experimental` `v3_exq_071d_rollout_batched_attribution` direction=`weakens` confidence=0.75
  - `2026-03-28T20:48:36Z` `experimental` `v3_exq_115_sd003_zharms_counterfactual` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `Patients with delusions of control report that their own actions feel alien or externally caused -- the forward model comparator is failing to match predicted to actual sensory consequence, so self-generated movements are misclassified as externally produced. This is the SD-003 failure mode: if E2 is miscalibrated, causal_sig will systematically misattribute the agent's own causal footprint.` (1)
  - `Patients with anosognosia experience illusory awareness of movement despite sensory loss, driven by motor command streams alone -- suggesting the forward model can generate self-attribution independently of sensory feedback, which has implications for SD-003 in low-feedback environments.` (1)
  - `The paper identifies parietal cortex as housing predicted and current state representations, and prefrontal/premotor as housing intended action representations -- disruption at either site produces distinct misattribution patterns, suggesting that the single forward model SD-003 implements may need to be decomposed in V4.` (1)
  - `Scholkopf et al. warn that most learned representations do not support interventional reasoning because they encode correlational structure rather than causal structure. If E2_harm_s is trained with a standard regression objective (minimising next-state prediction error), it may learn to encode correlational regularities between actions and harm outcomes rather than the underlying causal mechanism. In this case, E2(z_t, a_cf) would not correctly represent the interventional distribution P(z_harm_s | do(a_cf)), and causal_sig would be a biased estimate of the true causal contribution.` (1)
  - `The paper argues that causal representation learning requires some form of interventional or multi-environment data to break the symmetry between observationally equivalent but causally distinct models. If SD-003's E2_harm_s is trained only on observational trajectories without explicit counterfactual perturbations, it may not learn a representation that supports the interventional computation causal_sig requires.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-004
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=7, weakens=5, conflict_ratio=0.833, overall_confidence=0.787
- Recent entries:
  - `2026-03-23T16:23:27Z` `experimental` `v3_exq_046_arc007_path_memory_ablation` direction=`weakens` confidence=0.75
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_sd_004` direction=`supports` confidence=0.8
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_sd_004` direction=`supports` confidence=0.85
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_sd_004` direction=`supports` confidence=0.78
  - `2026-03-29T13:30:00Z` `literature` `targeted_review_connectome_sd_004` direction=`supports` confidence=0.72
- Recurring failure signatures:
  - `Paper remains largely descriptive of biological findings; the abstraction to action-object space is inferred from the logic of generalisation, not demonstrated experimentally in a non-spatial task with action-object structure` (1)
  - `The authors note that direct neural evidence for non-spatial cognitive maps is still emerging; the strongest evidence remains spatial` (1)
  - `SR is policy-dependent -- the predictive map changes when behavior changes, implying the map backbone is not a stable action-object library but a policy-contingent weighting` (1)
  - `SR as originally formulated does not compress multi-step action sequences into objects; it represents individual states weighted by future occupancy` (1)
  - `SR is defined over primitive states; Dayan does not consider action-object compression -- the extension to action-consequence chunks requires additional theoretical work (temporal abstraction, options framework)` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-005
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=10, weakens=14, conflict_ratio=0.833, overall_confidence=0.752
- Recent entries:
  - `2026-03-24T20:23:13Z` `experimental` `v3_exq_047j_tpj_routing_ce` direction=`mixed` confidence=0.5
  - `2026-03-25T02:15:58Z` `experimental` `v3_exq_047k_tpj_routing_larger_n` direction=`supports` confidence=0.75
  - `2026-03-25T05:05:29Z` `experimental` `v3_exq_096_full_integration_benchmark` direction=`superseded` confidence=0.55
  - `2026-03-25T05:54:16Z` `experimental` `v3_exq_096a_full_integration_benchmark` direction=`supports` confidence=0.75
  - `2026-03-28T16:21:48Z` `experimental` `v3_exq_113_sd005_double_dissociation` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `shared_self_world_representation` (1)
  - `partial_overlap_in_z_self_z_world_substrates` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-007
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=12, weakens=9, conflict_ratio=0.857, overall_confidence=0.808
- Recent entries:
  - `2026-03-28T00:00:00Z` `literature` `targeted_review_sd_007` direction=`supports` confidence=0.8
  - `2026-03-28T00:00:00Z` `literature` `targeted_review_sd_007` direction=`supports` confidence=0.7
  - `2026-03-28T00:00:00Z` `literature` `targeted_review_sd_007` direction=`supports` confidence=0.77
  - `2026-03-28T20:51:48.277586Z` `experimental` `discriminative_pair_sd007_reafference_gate` direction=`weakens` confidence=0.75
  - `2026-03-28T21:40:19.449255Z` `experimental` `discriminative_pair_sd007_reafference_multiseed` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `The cancellation is shown to be specific to self-produced stimuli with predictable sensory consequences — externally produced stimuli of identical physical parameters are perceived as significantly more intense. This implies the predictor must be trained on the specific statistical relationship between actions and sensory outcomes; an untrained or poorly calibrated predictor would fail to cancel.` (1)
  - `The cerebellum shows less activation during the movement that generates the tactile stimulus than during a movement that does not — suggesting the cancellation signal is computed in relation to the predicted sensory consequence of the specific action, not movement in general.` (1)
  - `The review notes important differences across sensory systems: visual reafference cancellation operates at higher cortical stages than vestibular/somatosensory suppression, implying that the REE architecture's single latent-level subtraction is an abstraction of a multi-stage biological process.` (1)
  - `The review emphasises that the brain continuously calibrates the relationship between motor signals and sensory feedback — a static predictor without ongoing calibration would diverge, a failure mode not directly addressed in SD-007's current implementation.` (1)
  - `Attenuation is graded by temporal delay: increasing delay between action and sensory outcome reduces attenuation, suggesting temporal correspondence is a prerequisite. A ReafferencePredictor operating on a stale prior state (large effective delay) would lose its cancellation effectiveness.` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### SD-011
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=6, weakens=3, conflict_ratio=0.667, overall_confidence=0.779
- Recent entries:
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_sd_011` direction=`supports` confidence=0.87
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_sd_011` direction=`supports` confidence=0.82
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_sd_011` direction=`supports` confidence=0.88
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_sd_011` direction=`supports` confidence=0.92
  - `2026-03-29T11:05:00Z` `literature` `targeted_review_connectome_sd_011` direction=`supports` confidence=0.84
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
