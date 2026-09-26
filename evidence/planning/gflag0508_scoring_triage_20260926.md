# GFLAG-0508 per-run triage (read-only audit, 2026-09-26)

Source of scoring status: REE_assembly/evidence/experiments/claim_evidence.v1.json (generated 2026-09-26T12:46:58Z). "Scoring" = experimental entry with scoring_excluded unset and evidence_direction not superseded/non_contributory. Fired-determination: telemetry keys in the flat JSON + runs/ manifest + metrics.json (pag_n_commits, *_freeze_fires, freeze_commit_count, freeze_active_steps, pag_freeze_frac, n_fresh_orienting_ticks, *_frozen_frac), then script inspection, then autopsy statements.

## A. Currently SCORING runs (11 queue ids, 13 claim edges)

| queue id | claim (direction, status) | run_id | gate fired? | basis | recommended disposition |
|---|---|---|---|---|---|
| V3-EXQ-228b | ARC-032 (weakens, FAIL) | v3_exq_228b_arc032_theta_bypass_onboarded_20260809T030541Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-228c | ARC-032 (weakens, FAIL) | v3_exq_228c_arc032_theta_bypass_readout_20260809T110214Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-228d | ARC-032 (weakens, FAIL) | v3_exq_228d_arc032_theta_phase_weighted_readout_20260811T234236Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-466e | SD-034 (supports, PASS) | v3_exq_466e_sd034_satisficing_residue_discharge_behavioural_20260625T030205Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-514m | MECH-230 (supports, FAIL) | v3_exq_514m_sd049_phase2_behavioural_curriculum_built_20260611T131105Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-514o | MECH-229 (supports, PASS) | v3_exq_514o_sd049_phase2_mech229_object_bound_wanting_liking_20260615T022311Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-514u | MECH-436 (supports, PASS) | v3_exq_514u_sd049_phase2_mech436_drive_coupling_continuous_amplitude_20260620T223024Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-603q | MECH-358 (supports, PASS) | v3_exq_603q_sd059_mech358_escape_affordance_bridge_evidence_20260617T042830Z_v3 | FIRED | base_pag_freeze_frac=1, pag_freeze_frac=1, pag_n_commits=189 | Adjudicate (autopsy): freeze fired on every seed (150-190 commits/seed); DV = Stage-H survival under escape bridge, so UP-walking is directly in the DV path. Presumptive supersede-candidate. |
| V3-EXQ-603q | SD-059 (supports, PASS) | v3_exq_603q_sd059_mech358_escape_affordance_bridge_evidence_20260617T042830Z_v3 | FIRED | base_pag_freeze_frac=1, pag_freeze_frac=1, pag_n_commits=189 | Adjudicate (autopsy): freeze fired on every seed (150-190 commits/seed); DV = Stage-H survival under escape bridge, so UP-walking is directly in the DV path. Presumptive supersede-candidate. |
| V3-EXQ-717 | MECH-445 (weakens, FAIL) | v3_exq_717_mech445_commit_intent_regime_scoped_falsifier_20260707T105300Z_v3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 post-fix) | Adjudicate: same 603/866a Stage-H harness (theta 0.8, trained harm) as 603q, which logged freeze on 100% of seeds; no telemetry recorded here. Presumptive affected; needs autopsy of whether the DV phase ran through select_action with freeze on. |
| V3-EXQ-776 | MECH-279 (supports, PASS) | v3_exq_776_mech279_pag_freeze_gate_functional_signature_20260717T153724Z_v3 | INERT (structural) | no env / no training: drives agent.pag_freeze_gate.tick() directly; executed action never produced (docstring L89) | KEEP scoring. Structurally unaffected: no env, freeze no-op never executed. Remove from GFLAG-0508 scope; the GOV count-first audit edge "GFLAG-0508: MECH-279 x V3-EXQ-776" is a token match, not an affected edge. |
| V3-EXQ-962 | MECH-219 (supports, PASS) | v3_exq_962_mech219_sd019b_behavioural_temporal_controllability_20260829T185419Z_v3 | INERT (structural) | driver never calls select_action(); env.step(4) fixed stay throughout (diagnostics.pag_mech091_redirect_enabled_non_gating) | KEEP scoring. select_action() never called; fixed env.step(4). Remove from scope. |
| V3-EXQ-962 | SD-019b (supports, PASS) | v3_exq_962_mech219_sd019b_behavioural_temporal_controllability_20260829T185419Z_v3 | INERT (structural) | driver never calls select_action(); env.step(4) fixed stay throughout (diagnostics.pag_mech091_redirect_enabled_non_gating) | KEEP scoring. select_action() never called; fixed env.step(4). Remove from scope. |

## B. Non-scoring listed runs (107 of 118) -- no score change needed; recorded for completeness

Exclusion reason counts (per queue id, an id can carry several): 
non_contributory=38, unlinked (no claim_ids; not in claim_evidence entries)=30, diagnostic_probe=19, superseded=11, degenerate=8, stale_substrate=3

| queue id | manifest claim_ids | exclusion | gate fired? | basis |
|---|---|---|---|---|
| V3-EXQ-324d | SD-020 | non_contributoryx1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-460c | MECH-260, MECH-261, SD-034 | non_contributoryx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460d | MECH-260, MECH-261, SD-034 | diagnostic_probex3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460e | MECH-260, MECH-261, SD-034 | non_contributoryx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460f | MECH-260, MECH-261, SD-034 | supersededx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460g | MECH-260, MECH-261, SD-034 | supersededx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460h | MECH-445, MECH-446 | stale_substratex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460i | MECH-445, MECH-446 | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460j | MECH-445, MECH-446 | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460k | MECH-445, MECH-446 | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460l | ARC-108, MECH-090, MECH-342, MECH-445, MECH-446 | non_contributoryx5 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460m | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460n | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460o | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-460p | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-461c | MECH-090, SD-033a, SD-034 | non_contributoryx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-464c | MECH-266, SD-032a | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-464d | MECH-266, SD-032a | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-464e | MECH-266, SD-032a | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-466c | MECH-094, SD-034 | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-466d | MECH-094, SD-034 | supersededx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-467c | MECH-266, SD-032a | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-467d | MECH-266, SD-032a | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-467e | MECH-266, SD-032a | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-468c | MECH-090, MECH-268, SD-034 | non_contributoryx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-468d | MECH-090, MECH-268, SD-034 | diagnostic_probex3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-468e | MECH-090, MECH-268, SD-034 | diagnostic_probex3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-468f | MECH-090, MECH-268, SD-034 | non_contributoryx3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-475 | MECH-279, SD-036 | diagnostic_probex2 | FIRED | seed0_freeze_active_steps=1000, seed0_freeze_commit_count=20, seed0_pag_n_commits=71 |
| V3-EXQ-475b | Q-040 | non_contributoryx1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-483 | MECH-280, MECH-281, SD-037 | supersededx3 | FIRED | arm_OFF_OFF_mean_freeze_active_steps=1000, arm_OFF_OFF_mean_freeze_commit=20, arm_OFF_ON_mean_freeze_active_steps=1000 |
| V3-EXQ-483a | MECH-280, MECH-281, SD-037 | supersededx3 | FIRED | arm_OFF_OFF_mean_freeze_active_steps=1000, arm_OFF_OFF_mean_freeze_commit=28.3333, arm_OFF_ON_mean_freeze_active_steps=1000 |
| V3-EXQ-483b | MECH-280, MECH-281, SD-037 | supersededx3, diagnostic_probex3 | FIRED | arm_OFF_OFF_mean_freeze_active_steps=1000, arm_OFF_OFF_mean_freeze_commit=29, arm_OFF_ON_mean_freeze_active_steps=1000 |
| V3-EXQ-483c | MECH-280, MECH-281, SD-037 | supersededx3 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-483d | MECH-280, MECH-281, SD-037 | non_contributoryx3 | UNKNOWN (483d autopsy: pag_release_count==0, read as never fired; but 490-series shows release=0 with 20 commits/1000 active steps, so release=0 does not prove not-fired) | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-483e | MECH-280, MECH-281, SD-037 | non_contributoryx3 | UNKNOWN (as 483d; pag_release_count_end=0 only) | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-490 | MECH-269b, Q-040 | diagnostic_probex4 | FIRED | freeze_active_steps=1000, freeze_commit_count=20 |
| V3-EXQ-490b | Q-040 | supersededx1 | FIRED | freeze_active_steps=1000, freeze_commit_count=20 |
| V3-EXQ-490c | Q-040 | supersededx1 | FIRED | freeze_active_steps=1000, freeze_commit_count=20 |
| V3-EXQ-490e | Q-040 | non_contributoryx1 | FIRED | freeze_active_steps=1000, freeze_commit_count=20 |
| V3-EXQ-490f | Q-040 | supersededx1, non_contributoryx1 | FIRED | freeze_active_steps=1000, freeze_commit_count=55 |
| V3-EXQ-514n | MECH-229 | non_contributoryx1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-514p | MECH-229 | non_contributoryx1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-514q | MECH-229 | non_contributoryx1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-514r | MECH-436 | non_contributoryx1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-514s | MECH-436 | supersededx1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-514t | MECH-436 | stale_substratex1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-600a | MECH-282, SD-037 | diagnostic_probex2 | FIRED | pag_freeze_commits=8 |
| V3-EXQ-601 | MECH-269b | diagnostic_probex2 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-603h | - | unlinked | FIRED | pag_freeze_frac=1, pag_n_commits=444 |
| V3-EXQ-603i | - | unlinked | FIRED | base_pag_freeze_frac=1, pag_freeze_frac=1, pag_n_commits=462 |
| V3-EXQ-603k | - | unlinked | UNKNOWN | no telemetry; theta=0.8 harm_trained=False orient=False |
| V3-EXQ-603l | MECH-358, SD-059 | non_contributoryx2 | FIRED | base_pag_freeze_frac=1, pag_freeze_frac=1, pag_n_commits=187 |
| V3-EXQ-603m | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-603n | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-603o | MECH-358, SD-059 | non_contributoryx2 | FIRED | base_pag_freeze_frac=1, pag_freeze_frac=1, pag_n_commits=193 |
| V3-EXQ-603p | - | unlinked | FIRED | pag_freeze_frac=1, pag_n_commits=195 |
| V3-EXQ-603r | MECH-357 | non_contributoryx1 | FIRED | pag_freeze_frac=1, pag_n_commits=191 |
| V3-EXQ-603s | MECH-357 | non_contributoryx1 | FIRED | pag_freeze_frac=1, pag_n_commits=189 |
| V3-EXQ-603t | MECH-357 | non_contributoryx1 | FIRED | pag_freeze_frac=1, pag_n_commits=191 |
| V3-EXQ-603u | MECH-357 | non_contributoryx1 | FIRED | pag_freeze_frac=1, pag_n_commits=198 |
| V3-EXQ-620 | - | unlinked | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-620b | - | unlinked | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-625 | - | unlinked | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-625b | - | unlinked | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-625c | - | unlinked | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-625d | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-625e | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-629b | MECH-342 | stale_substratex1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-629c | MECH-342 | degeneratex1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-664 | - | unlinked | FIRED | seed0_freeze_fires=11, seed1_freeze_fires=20, seed2_freeze_fires=13 |
| V3-EXQ-665 | - | unlinked | NOT FIRED | total_freeze_fires=0 |
| V3-EXQ-687 | MECH-260, MECH-313, Q-045 | degeneratex3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-687a | MECH-260, MECH-313, Q-045 | degeneratex3 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-693 | SD-015, SD-049 | non_contributoryx2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-693a | SD-015, SD-049 | degeneratex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-715 | MECH-445, MECH-446 | degeneratex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-715a | MECH-445, MECH-446 | degeneratex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-721 | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-733a | MECH-456 | non_contributoryx2 | FIRED | mean_reacq_latency_frozen=20, stale_rate_frozen=0.997633 |
| V3-EXQ-793 | SD-049 | diagnostic_probex1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-793a | SD-049 | diagnostic_probex1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-797 | MECH-266, SD-032a | diagnostic_probex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-812 | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-812a | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-862 | Q-040 | non_contributoryx1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-862a | Q-040 | non_contributoryx1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-862b | Q-040 | non_contributoryx1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=False |
| V3-EXQ-866a | INV-034, Q-021 | degeneratex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-866b | MECH-358, SD-059 | diagnostic_probex2 | FIRED | pag_n_commits=188 |
| V3-EXQ-866c | INV-034, Q-021 | degeneratex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-899 | - | unlinked | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-906 | - | unlinked | NOT FIRED | total_freeze_fires=0 |
| V3-EXQ-906a | - | unlinked | NOT FIRED | total_freeze_fires=0 |
| V3-EXQ-906b | - | unlinked | NOT FIRED | total_freeze_fires=0 |
| V3-EXQ-910 | MECH-489 | diagnostic_probex1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=True |
| V3-EXQ-910a | MECH-489 | diagnostic_probex1 | UNKNOWN | no telemetry; theta=default2.0 harm_trained=False orient=True |
| V3-EXQ-910b | MECH-489 | diagnostic_probex1 | FIRED | n_fresh_orienting_ticks=11025, n_fresh_orienting_ticks=5303 |
| V3-EXQ-916 | - | unlinked | FIRED | seed0_freeze_fires=79, seed1_freeze_fires=31, seed2_freeze_fires=66 |
| V3-EXQ-916a | - | unlinked | FIRED | seed0_freeze_fires=79, seed1_freeze_fires=31, seed2_freeze_fires=66 |
| V3-EXQ-932 | - | unlinked | FIRED | seed0_freeze_fires=79, seed1_freeze_fires=31, seed2_freeze_fires=66 |
| V3-EXQ-932a | - | unlinked | FIRED | freeze_fires=83, total_freeze_fires=124, total_freeze_fires=150 |
| V3-EXQ-934 | MECH-266, SD-032a | diagnostic_probex2 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-935 | MECH-266, SD-032a | diagnostic_probex2 | LIKELY FIRED (1107 autopsy names 935/935a harness) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-935a | MECH-266, SD-032a | diagnostic_probex2 | FIRED (autopsy V3-EXQ-1107: same settings lock from tick 1 post-fix; pre-fix lock masked by UP-walking) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-951 | MECH-320 | non_contributoryx1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-951c | MECH-320 | diagnostic_probex1 | LIKELY FIRED (inferred) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-1067 | MECH-266, SD-032a | diagnostic_probex2 | LIKELY FIRED (autopsy: contact guard "may reflect UP-walking") | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |
| V3-EXQ-1090 | MECH-449 | diagnostic_probex1 | FIRED (autopsy 2026-09-26: executed_action=0 on 3000/3000 ARM_HARM_ON rows) | no telemetry; 603-lineage harness theta=0.8 + trained harm pathway (siblings 603h-u/866b log 130-460 commits/seed; 1107 autopsy: same config locks from tick 1 p |

## C. Determination totals (all 120 incl. straddlers)

LIKELY FIRED=67, FIRED=30, UNKNOWN=17, NOT FIRED=4, INERT=2
