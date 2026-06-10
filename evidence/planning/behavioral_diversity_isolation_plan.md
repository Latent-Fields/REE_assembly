---
closure_plan:
  id: behavioral_diversity_isolation
  title: "Behavioural Diversity Isolation"
  registered: 2026-05-25
  last_updated: 2026-06-08
  scope_claims: [ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076]
  sibling_plans: [arc_062_rule_apprehension, commitment_closure, sleep_substrate, sd033_governance, goal_pipeline, self_attribution]
  nodes:
    - id: "behavioral_diversity_isolation:GAP-A"
      title: "Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)"
      phase: "substrate validated ready -> FP-2 falsifier work resumes"
      status: in-progress
      severity: medium
      owner_exq: "V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30; V3-EXQ-569f QUEUED 2026-06-09 (R1.b FP-2 matched-entropy action-contrastive behavioural falsifier on the 649-validated candidate_summary_source=e2_world_forward stack; supersedes 569d; ree-v3 db812e6)"
      unblocks_claims: [ARC-065]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-H", "arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-06-09
      governance_2026_06_07_pm: "GAP-A VALIDATED READY -- the documented resume condition is MET. V3-EXQ-649 (arc065_gapa_shared_candidate_summary_source) PASSed 2026-06-07T13:14Z: load-bearing C2 (e2_world_forward lifts consumed cand_world_summaries spread over the proposer source) PASS with ARM_1 consumed-summary spread 0.090 >= the 0.05 floor; the precondition_unmet adjudication flag was an indexer upper-bound false-positive (fixed on origin 4cad6af514/639e9e0a59). Confirmed by failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07 (status=confirmed; applied this /governance cycle). Status advanced blocked_pending_substrate -> in-progress. R1.a/R1.b matched-entropy work can now resume (queue V3-EXQ-569a successor) AND the cluster's downstream retests are unblocked: V3-EXQ-604c (MECH-314-family, supersedes the pre-fix non_contributory 604b), the MECH-341 committed-class diversity re-test (within-class-REPRESENTATIVE-diversity readout per autopsy Learning #2, GAP-B node), and the ARC-062/063 GAP-B falsifier. Companion curiosity-channel probe V3-EXQ-648a also confirmed load-bearing-ready (C2 PASS). ARC-065 substrate_queue entry amended (gapA_status=ready_validated; 604b + 649 failure_records appended)."
      substrate_landed_2026_06_07: "SHARED-CHANNEL E2-world-forward per-candidate signal preservation LANDED 2026-06-07 via /implement-substrate (session implement-substrate-arc065-gapa-e2wf-candidate-pool-20260607T0803Z), routed by failure_autopsy_V3-EXQ-614e_2026-06-07. The 614e autopsy relocated the committed-class-diversity bottleneck from the authority gate (GAP-B, resolved by V3-EXQ-643a) to this node (GAP-A candidate-pool class collapse; cand_world_pairwise_dist=0.0000). Fix: ree-v3 REEConfig.candidate_summary_source (proposer|e2_world_forward, default proposer/bit-identical) re-sources the SHARED cand_world_summaries consumed by lateral_pfc/ofc/mech295/gated_policy/tonic_vigor from the SD-056-trained e2.world_forward(z0,a_i) -- the shared-channel sibling of the curiosity-only MECH-314a Phase-2 fix (648a) and the generalisation of the GatedPolicy-only ARC-062 GAP-B first-action-onehot fix to ALL E3-side bias channels. agent.py _candidate_world_summaries helper consulted at all 5 cand_world_summaries fresh-build sites; 889 contracts + 7 preflight PASS (bit-identical OFF); 6 new contracts test_arc065_gapa_candidate_summary_source.py; 614e --dry-run unchanged. Status STAYS blocked_pending_substrate until the substrate-readiness validation V3-EXQ-649 (claim_ids=[]; candidate_summary_source=e2_world_forward + cand_world_pairwise_dist readiness precondition + shared-bias-channel per-candidate range readout) PASSes. On 649 PASS the node's R1.a/R1.b matched-entropy work can resume AND the MECH-341 committed-class diversity re-test (within-class-REPRESENTATIVE-diversity readout, NOT committed-class entropy per autopsy Learning #2) unblocks. Detector depends on a trained e2.world_forward (SD-056); the 649 readiness precondition guards vacuity (substrate_not_ready_requeue on an under-trained e2)."
      governance_2026_05_29: "Drift report freshness bump only; status remains in_progress / blocked_pending_substrate. The /implement-substrate work on the E2-world-forward per-candidate signal preservation (SD-056 contrastive next-state landed 2026-05-29 in ree-v3 main 041a974; substrate-readiness validation queued as V3-EXQ-613 by the sibling implement-substrate session) is now in flight. Next-step V3-EXQ-569a matched-entropy FP-2 falsifier will be queued post-V3-EXQ-613 PASS via /queue-experiment. IGW-20260528-008 remains stale pending V3-EXQ-613 outcome."
      resume_condition: "IN FLIGHT 2026-06-09 on V3-EXQ-569f (queued via /queue-experiment; supersedes V3-EXQ-569d). The substrate seam HAS landed and is 649-validated, so the FP-2 falsifier has resumed -- do NOT queue the dead V3-EXQ-569a (the 569a/b/c/d/e lineage all already ran; 569e is the frontier). HISTORY: V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path). V3-EXQ-569 matched-entropy sweep ran 2026-05-16 and was reclassified non_contributory at governance review: all 6 arms produced identical entropy (~0.496) because bias_fraction=0 for all diversity components -- the structured-vs-random comparison was never activated. V3-EXQ-571 PASS diagnostic confirmed F (forward model) dominates 88-89% of E3 score variance and ALL bias_fractions are machine-epsilon. V3-EXQ-573 10-arm bias-scale sweep (1x/5x/10x) reproduced the identical-arms collapse at 10x scale -> reclassified non_contributory; bias channel does not propagate at scale. V3-EXQ-609 per-candidate spread decomp (methodology fork from 571) surfaced curiosity emitting zero per-candidate vector. Root cause documented 2026-05-25 in evidence/planning/v3_exq_571_root_cause_2026-05-25.md: score_bias plumbing is correct, but the per-candidate signal is STRUCTURALLY ZERO -- all K candidates produce identical z_world after one E2 world-forward step (cand_world_pairwise_dist=0.0000) despite differing first actions. Same root cause as the 2026-05-17 ARC-062 GAP-B autopsy; that fix was scoped only to GatedPolicy. R1.a/R1.b cannot fire while the bias channel structurally carries no per-candidate variance. The /implement-substrate fix landed 2026-06-07 (SHARED-channel candidate_summary_source=e2_world_forward, re-sourcing cand_world_summaries from the SD-056-trained e2.world_forward) and V3-EXQ-649 PASS validated readiness (consumed-summary spread 0.090>=0.05). NEXT STEP DONE 2026-06-09: V3-EXQ-569f queued (ree-v3 db812e6) as the matched-entropy FP-2 falsifier successor on the 649 stack -- 3-arm single-variable design toggling candidate_summary_source (ARM_0 proposer / ARM_1 e2_world_forward / ARM_2 matched-noise T=2.5), claim_ids=[ARC-065], PRIMARY DV selected_action_class_entropy; R1.b PASS = ARM_1 strictly above BOTH matched-noise and proposer per matched seed (>=2/3) with readiness + e2-divergence floors met (supports); readiness/C1 unmet -> non_contributory (substrate_not_ready_requeue); readiness met + no lift -> weakens (R1.a entropy-only-artefact). On 569f landing: governance applies R1.a/R1.b to ARC-065. IGW-20260528-008 (this node's owning IGW item) advances from substrate-blocked to falsifier-in-flight."
    - id: "behavioral_diversity_isolation:GAP-B"
      title: "Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)"
      phase: "660 landed PASS/supports -> temperature-graded confirmation + governance ratification owed"
      status: partial
      severity: load-bearing
      next_owner_exq: "OWED (not yet queued): a temperature-graded MECH-341 within-class confirmation -- 660 showed the within-class-representative lever is load-bearing (legacy-vs-any-sweep lift) but BYTE-IDENTICAL across T=0.5/1.0/2.0 (4.861916), so a graded/ratifiable response is not yet demonstrated; that + governance ratification gates v3_pending clearance. ARC-062 (in unblocks_claims) still untouched by this owner."
      owner_exq: "V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e). Governance folded into claims.yaml 2026-06-10 (MECH-341 supports, v3_pending HELD). Predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS"
      unblocks_claims: [MECH-341, ARC-062, ARC-065]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-06-10
      governance_2026_06_10: "V3-EXQ-660 LANDED 2026-06-10T04:41Z PASS / supports (manifest v3_exq_660_mech341_within_class_representative_diversity_20260610T044109Z_v3; evidence_direction_per_claim[MECH-341]=supports; reviewed). The owed GAP-B action is DONE at the run level and folded into claims.yaml the same day: the [2026-06-10 governance: V3-EXQ-660 supports, v3_pending HELD] note on MECH-341 records C1 substrate-operative + within-class branch active + multi-rep available (majority); C2 within-class-REPRESENTATIVE-diversity lift PASS (swept 4.862 vs legacy 4.781 nats); committed-CLASS (across-class) entropy flat = EXPECTED negative control (secondary, not a gate). This is the corrected-readout retest the 614e autopsy Learning #2 required (H(rep_signature | committed_class), NOT committed-class entropy). The resume_condition's C1+C2 branch fired -- but governance HELD v3_pending rather than clearing it, on two caveats: (1) the lift margin is THIN (~0.08 nats vs 0.05 threshold); (2) the three temperature arms T=0.5/1.0/2.0 produce BYTE-IDENTICAL within-class entropy (4.861916; 196/1105/255 samples) -- the lever fires but is INSENSITIVE to temperature magnitude (only legacy-vs-any-sweep differs). So 660 confirms the within-class sub-axis is LOAD-BEARING but does not yet show a graded, ratifiable response. DISPOSITION: MECH-341 stays candidate / v3_pending=true (no promotion, no auto-flip of the within-class default); 660 supersedes 614e (already non_contributory). Node STAYS partial: the run is absorbed (not pending, not lost), but v3_pending is not cleared and ARC-062 in unblocks_claims is untouched. Plan-doc reconcile only -- claims.yaml + manifest + review_tracker already current; no claims/scoring edits this session. last_updated bumped 2026-06-09 -> 2026-06-10."
      governance_2026_06_09_pm: "V3-EXQ-660 QUEUED via /queue-experiment 2026-06-09T21:33Z (session queue-mech341-gapb-within-class-rep-diversity-20260609T2117Z) -- the owed GAP-B action, unblocked by V3-EXQ-649 GAP-A readiness PASS + the 614e autopsy Learning #2. Forked from 614e with the CORRECTED matched readout: PRIMARY DV C2 = within_class_rep_cond_entropy = H(rep_signature | committed_class), where rep_signature is the post-first-action argmax signature of agent.e3._last_selected_trajectory (which within-class representative is selected inside the committed class), expected to RISE with the swept within-class temperature {None=legacy argmin,0.5,1.0,2.0}. Committed-class (across-class) entropy is now only a SECONDARY negative-control (expected flat per 614e; NOT a gate). All 4 arms arm GAP-A (candidate_summary_source=e2_world_forward), authority (use_modulatory_selection_authority=True gain=0.5), SP-CEM, MECH-341, SD-056. C1 non-vacuity gate (within-class branch fires AND committed class offers >=2 distinct representatives, majority swept-arm seeds) asserts the SAME within-class-representative axis C2 routes on; C1 FALSE self-routes substrate_not_ready_requeue -> non_contributory (protects MECH-341 from a false weakens). Evidence-direction: C1-fail->non_contributory / C1+C2->supports / C1 + C2-fail->weakens. ree-v3 main bf06d8a; ingested into coordinator /queue/active. NO claims.yaml/governance edit; MECH-341 stays candidate / v3_pending. Node stays partial pending the run + a later /governance fold-in. last_updated bumped."
      governance_2026_06_09: "Closure-drift stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-654_2026-06-09 (confirmed, applied this cycle) touches ARC-062, which is in this node's unblocks_claims. That autopsy adjudicates the arc_062 GAP-B *rule-apprehension* falsifier (V3-EXQ-654) as non_contributory / substrate_ceiling (CandidateRuleField per-episode cold-start; C1c readiness FAIL gated out the DV) and does NOT reclassify ARC-062's status (stays candidate / substrate_ceiling / v3_pending) -- so it does not change this node's disposition. This node's real outstanding work is the distinct MECH-341 within-class-representative-diversity retest on the GAP-A-ready substrate (still owed, not queued). Node stays partial; last_updated bumped to acknowledge."
      governance_2026_06_08: "Plan-drift reconcile. The prior 2026-06-08 freshness note for V3-EXQ-610f remains true but incomplete. The V3-EXQ-542a overlap is also a false-positive for this node (ARC-062 substrate-readiness lineage, not the 614-lineage MECH-341 question). V3-EXQ-614e has now been autopsied and applied: non_contributory substrate_ceiling, MECH-341 not weakened, and the bottleneck moved upstream to GAP-A. GAP-A readiness is now validated by V3-EXQ-649 PASS, so this node stays partial with the next real action being a MECH-341 GAP-A-ready retest using the within-class-representative-diversity readout."
      governance_2026_06_07: "Lineage advance: V3-EXQ-614e (manifest v3_exq_614e_mech341_within_class_temperature_authority_on_20260607T070701Z_v3) landed 2026-06-07T07:07Z and supersedes 614d -- the FIRST within-class-temperature behavioural test on the now-VALIDATED modulatory-bias-selection-authority substrate (V3-EXQ-643a PASS, float32 catastrophic-cancellation fix). Unlike 614d (lever ACTIVE but ZERO committed-action authority), 614e ran with use_modulatory_selection_authority=True+gain=0.5 so the lever is OPERATIVE: C1 substrate-operative=True (within-class branch + Site-2 authority normalization fire; ARM_0 committed entropy non-degenerate) AND C3 readiness=True, yet C2 (committed_class_entropy rises with within-class temperature) STILL =False across all arms. So even with operative committed-action authority, within-class temperature produces NO committed-class diversity lift -- the fourth convergent committed-action-authority/no-lift instance on this node. Script self-emitted evidence_direction=weakens on MECH-341; /governance 2026-06-07 DEFERRED it weakens->non_contributory (manifest + runpack edited, index rebuilt: MECH-341 reverts to 2 supports:0 weakens, exp_conf 0.809) and ROUTED 614e to /failure-autopsy (user directive) to adjudicate clean-falsifier-of-MECH-341 vs monostrategy/GAP-B substrate-ceiling (no class diversity for E3 scoring to preserve). 614e NOT marked reviewed -- stays pending as the autopsy work-list. MECH-341 stays candidate / v3_pending=true; no confidence move. Node stays partial. last_updated bumped."
      governance_2026_06_06: "Closure-drift stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-608-611c_2026-06-06 (confirmed) reclassified MECH-341 in this node's unblocks set. That autopsy adjudicates the 611c substrate-readiness PASS as vacuous-pass-class (gate carried by a temperature-invariant C2 + near-vacuous C3; fires != preserves) and the 608/611 self-route epsilon as a measurement-design defect; routing=governance-record-only, recommended_substrate_queue_entry.action=none (the modulatory-bias-selection-authority gate already lists MECH-341 in unblocks_claims and gates the efficacy re-test). MECH-341 stays candidate / v3_pending=true; no confidence move. This is the SAME committed-action-authority finding already captured in governance_2026_06_03 (614d third convergent instance) -- node disposition unchanged, stays partial owed to the newly-implemented authority substrate. last_updated bumped to acknowledge."
      governance_2026_06_03: "614c lineage RESOLVED -- this row no longer waits on 614c. (1) V3-EXQ-614c ran 2026-06-01T12:45Z FAIL (manifest v3_exq_614c_mech341_stratified_within_class_temperature_sweep_20260601T124509Z_v3), reclassified evidence_direction=non_contributory per failure_autopsy_V3-EXQ-614c_2026-06-01 (status=confirmed): both failing criteria are test-design defects -- C2 vacuous score-layer-argmin metric is temperature-invariant; C1 mis-specified per-seed band vs cross-seed mean; C3 substrate-readiness PASS 3/3 (instrumentation_defect, NOT substrate_ceiling). Already in review_tracker reviewed_run_ids + discussed_experiment_dirs; pending_retest gated on the corrected harness. (2) Corrected-harness successor V3-EXQ-614d (supersedes 614c) ran 2026-06-03T12:01Z and was reviewed same day (session review-614d-mech341-20260603T144832Z): interpretation_label PASS_C1_C3_only_within_class_active_no_committed_class_lift; evidence_direction=mixed; experiment_purpose=diagnostic (scoring-excluded). C1 (cross-seed mean vs 614b ALL_ON 0.80 band) PASS; C3 (within-class branch fires 3/3 seeds, 159-1030 samples) PASS; C2 (committed-class temperature lift) FAIL -- committed-class entropy byte-identical 1.056572 at T=0.5/1.0/2.0 (legacy 1.057734), 0/3 paired-lift seeds per arm. FINDING: the within-class temperature lever is ACTIVE but has ZERO committed-action authority -- the THIRD convergent instance of the modulatory-bias-selection-authority gap (604a curiosity, 624a vigor, 614d within-class temperature; scoring-layer signals do not reach the committed argmax). This retroactively corrects the governance_2026_06_01 hope that the SD-056 amend would transitively unblock the cross-plan beneficiaries: the amend stabilised the substrate but the within-class lever alone does not deliver committed diversity. DISPOSITION (user-approved): MECH-341 stays candidate / v3_pending=true -- do NOT clear; dated note added to MECH-341. SUBSTRATE: the modulatory-bias-selection-authority gate CLEARED 2026-06-03; that substrate was IMPLEMENTED 2026-06-03T15:20Z via /implement-substrate (session implement-substrate-modulatory-bias-selection-authority-20260603T145832Z; approach b gap-relative scaling: E3Config.use_modulatory_selection_authority + modulatory_authority_gain=0.5 + min_range_floor=1e-6; e3_selector.select additive-chain + MECH-341 bonus rescaled to gain*raw_score_range; e3_score_diversity.stratified_select across-class unit-range normalization = the 614d C2 fix; primary scores unmodified; 734/734 contracts + 7/7 preflight PASS flag-OFF bit-identical) -- substrate_queue entry modulatory-bias-selection-authority now status=implemented_pending_validation (ready=false), MECH-341 added to its unblocks_claims, 614d added as 3rd failure_record, implementation_hint unified across MECH-314 curiosity / MECH-320 vigor / MECH-341 within-class temperature (one shared committed-action-authority bottleneck, build the arbitration channel once). NEXT STEP: queue the modulatory-bias-selection-authority substrate-readiness validation EXQ via /queue-experiment (priority-1 substrate_queue lane) -- NOT a re-spec'd 4-arm within-class sweep on the current substrate (614d already proved the within-class lever has no committed authority pre-authority-substrate). After that validation passes, queue the MECH-341 committed-class diversity re-test. Status stays partial: 614c/614d fully absorbed (NOT pending, NOT lost) but MECH-341 not cleared and the committed-action authority is owed to the newly-implemented substrate; do NOT promote to done. Plan-doc reconcile only -- no claims.yaml/manifest/scoring edits this session (MECH-341 dispositions + substrate_queue edits already landed under the 614d review + /implement-substrate sessions)."
      governance_2026_06_01: "V3-EXQ-614b FAIL (manifest v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended_20260531T182040Z_v3) confirmed C1 structurally degenerate (B_only Rung-1 majority=False; per-seed frac_pre_ge2=0.0 -- CEM proposer collapses to single-class candidate pools without SP-CEM Layer A) AND C2 necessity_delta 0.087 just below pre-amend 0.1 threshold. C3 ALL_ON Rung-1 PASSed at 0.800 nats (highest of any 614-lineage run -- positive substrate-readiness for SD-056 amend at behavioural-runtime horizon). Failure-autopsy V3-EXQ-616 Sections 7 + 10 named the contingent path: stratified_temperature default + A-vs-B partial-redundancy probe; this path activated by 614b FAIL_C1. MECH-341 amend landed 2026-06-01 via /implement-substrate (session implement-substrate-mech-341-amend-stratified-temp-ab-probe-20260601T063226Z): (a) E3ScoreDiversity gains stratified_within_class_temperature: Optional[float] = None lever -- within each first-action class, when set, sample representative via softmax(-class_scores / T); legacy argmin when None (bit-identical OFF). Decoupled from existing across-class stratified_temperature (default 1.0; unchanged). (b) A-vs-B partial-redundancy probe lever satisfied by the existing independent flags use_support_preserving_cem (Layer A) and use_e3_score_diversity (Layer B) -- compose to A_only / B_only / BOTH / NEITHER. No new code flag added (would be redundant); the lever IS the existing flag composition. NO flip of use_differentiable_cem default (SD-055 safety note preserved). 655/655 contracts + 7/7 preflight PASS post-amend with master OFF and amend OFF. Validation: V3-EXQ-614c queued 2026-06-01 (4-arm within-class temperature sweep {None=legacy, 0.5, 1.0, 2.0} on SD-056-amended baseline). Cross-plan: amend transitively unblocks arc_062_rule_apprehension:GAP-B (V3-EXQ-543l successor cohort) under shared SD-056-amended substrate. Status remains partial pending 614c outcome; do NOT promote to done."
      governance_2026_05_31: "V3-EXQ-614a landed 2026-05-30T19:32Z PASS (manifest v3_exq_614a_mech341_p3_behavioural_falsifier_3arm_20260530T193245Z_v3) with interpretation_label PASS_C2_C3_only_mech341_load_bearing_in_stack_only per behavioral_diversity_isolation_plan R2.c rule. Routing under the script's 4-row interpretation grid: 'PASS via C2+C3 only -> /governance MECH-341 supports load-bearing + Q-054 entropy_bias_scale sweep'. Governance cycle 2026-05-31 applied evidence_direction_per_claim[MECH-341]=supports + evidence_direction_per_claim[ARC-065]=supports to claims.yaml. Companion PASSes in same cycle: V3-EXQ-569d (floor-recal FP-2 falsifier supersedes 569c) and V3-EXQ-615 (Rung-1 matched-entropy on rescued substrate). ARC-065 v3_pending + pending_retest_after_substrate cleared. MECH-341 stays candidate / v3_pending=true pending V3-EXQ-569e mechanism-dissociation autopsy interpretation (569e was a Pathway A vs B diagnostic FAIL flagged for /failure-autopsy). NEXT STEP per interpretation grid: queue Q-054 entropy_bias_scale sweep via /queue-experiment (Q-054 sweep across entropy_bias_scale magnitudes to determine the load-bearing scale range of mech341). GAP-B status flipped 'blocked' -> 'partial' 2026-05-31T11:08Z after closure-drift walk with operator: load-bearing evidence collected on MECH-341 (supports) + ARC-065 (supports, v3_pending cleared) -- 1-of-3 unblocks_claims closed + partial-PASS on the principal claim is more accurately 'partial' (CLOSURE_STATUS_WEIGHTS=0.5) than 'blocked' (0.1). Remaining work (Q-054 sweep V3-EXQ-616 queued same session + Phase P4 11-arm matrix + V3-EXQ-569e autopsy on MECH-341) is forward-progress, not re-block. Still NOT 'done': MECH-341 stays candidate / v3_pending=true pending 569e autopsy + Q-054 magnitude-load result; ARC-062 not yet addressed by this owner. Drift script tightened in the same session to read manifest evidence_direction so the GAP-1 / GAP-2 false positives stop firing."
      governance_2026_05_31_midday: "Case 3 in closure-drift terms: legitimately non-terminal partial. Midday governance applied V3-EXQ-569e autopsy verbatim (verdict=INSTRUMENTATION_FAILURE; diagnostic, non-weighting; evidence_direction_per_claim[ARC-065]=mixed, [MECH-341]=mixed; SD-056 multistep amend landed at 11:25Z with V3-EXQ-617 substrate-readiness PASS at 11:31Z); MECH-341 v3_pending=true preserved pending the SD-056 amend-and-re-run cycle on the corrected substrate. V3-EXQ-616 Q-054 entropy_bias_scale sweep also queued same morning is the second outstanding forward-progress item. GAP-B partial status remains correct; do NOT promote to done."
      governance_2026_05_31_afternoon: "V3-EXQ-614b queued 2026-05-31T12:32Z via /queue-experiment as the amend-and-re-run leg of the SD-056 amend-and-re-run cycle flagged in the midday note. Re-runs the 614a 3-arm behavioural falsifier (ARM_0 B_only / ARM_1 ablate_B / ARM_2 ALL_ON) on the SD-056-amended substrate. User-confirmed via AskUserQuestion 2026-05-31T12:31Z: BOTH SD-056 amend levers ON in all 3 arms (Lever (a) multi-step contrastive h=5 + Lever (b) per-step output norm clamp ratio=2.0; t=1 contrastive also ON), held constant across the diversity-axis comparison so R2.c interpretation is not confounded by amend on/off being correlated with A/B/C/D axis state. Acceptance criteria UNCHANGED (C1/C2/C3 + PASS = C1 OR (C2 AND C3)); 4-row interpretation grid UNCHANGED with header note clarifying that under the amended substrate PASS via C1 (R2.c MECH-341 isolation) is now the load-bearing target since 614a established PASS via C2+C3. Cross-plan: same Layer-B substrate stabilisation unblocks arc_062_rule_apprehension:GAP-B (V3-EXQ-543l successor cohort) under shared SD-056-amended substrate -- note flagged in queue entry rationale. Sibling concurrent /queue-experiment session for V3-EXQ-569a (ARC-065 GAP-A) holds disjoint script path; coordinated via user-approved re-read-before-write protocol. Status remains partial pending 614b outcome + 569e autopsy claim-narrowing + Q-054 magnitude-load result."
      resume_condition: "PARTIAL 2026-06-10. V3-EXQ-660 has LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-queue it; its C1+C2 branch fired and governance is folded into claims.yaml. The within-class-representative sub-axis is now load-bearing-CONFIRMED but v3_pending is HELD (not cleared) on two caveats: thin lift margin (~0.08 nats vs 0.05) and byte-identical entropy across T=0.5/1.0/2.0 (lever fires but is temperature-INSENSITIVE). RESUME path to clear MECH-341 v3_pending: (a) a temperature-GRADED within-class confirmation showing a monotonic/ratifiable response to within-class temperature (the 660 design proved load-bearing-ness but not gradedness), AND (b) governance ratification. Until then MECH-341 stays candidate / v3_pending=true. Separately, ARC-062 (in unblocks_claims) remains unaddressed by this owner. Ignore V3-EXQ-542a/610f overlap flags for this node; they do not change the 614-lineage question."
    - id: "behavioral_diversity_isolation:GAP-C"
      title: "Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)"
      phase: "P1"
      status: in-progress
      severity: medium
      owner_exq: "V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling"
      unblocks_claims: [MECH-313, MECH-260, Q-045]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-H"]
      last_updated: 2026-06-10
      governance_2026_06_10_pm: "Closure-drift acknowledge (session governance-20260610T1600Z). Both gates GAP-C waits on have now LANDED but neither is CLEARED, so the node stays in-progress: (1) the 4-arm bridge re-test V3-EXQ-603l landed FAIL/weakens (SD-059/MECH-358) but the weakens rests on a survivability ceiling (BASE G_H already 1.0; bridge credits + clears G_H 2/3 non-vacuously, preconditions all MET) -- user FLAGGED for /failure-autopsy this cycle (possible discrimination-ceiling artifact vs genuine weakens), so the bridge verdict is NOT yet settled and the ready-flip is NOT taken; (2) the full scaffolded G1/G2/G3 gate V3-EXQ-603m landed FAIL at G0 only (Stage-0 nursery z_goal>0.4 held 1/3; G1 survival 3/3, G2 contact 3/3, G3 ecological z_goal 2/3 all PASS; non-vacuity MET) -- confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10 ruled G0 a measurement/developmental-sequencing artifact and routed the corrected-G0 re-run V3-EXQ-603n (queued this cycle). NOTE the closure-drift lineage-advanced flag pins 603m as a 'later sibling' of owner_exq 603k: 603m/603n is the scaffolded-curriculum readiness lineage (owned at goal_pipeline:GAP-2), distinct from 603k's Stage-H harm-pathway leg; owner_exq stays 603k. Q-045/MECH-313/MECH-260 retest stays gated on the 603l autopsy verdict + the 603n corrected-G0 scaffolded gate clearing. No claims.yaml / manifest edits."
      governance_2026_06_10: "Substrate-reconcile WP-A (session substrate-reconcile-603jk-WP-A-20260610T0631Z): both 603j/603k PASS manifests re-verified directly and the substrate_queue entries reconciled to match -- escape-affordance-bridge status pending_implementation -> IMPLEMENTED/safety-half-validated (ready stays false; behavioural validation V3-EXQ-603l in flight owns the ready flip), scaffolded_sd054_onboarding status updated to harm-pathway-survival-leg VALIDATED (ready stays false; residual = foraging/benefit-contact P2 leg + Stage-0 z_goal>0.4 holds on only 1/3 seeds). GAP-C unchanged: stays in-progress + non-governance-weighting, Q-045/MECH-313/MECH-260 retest still gated on the full 4-arm 603l bridge re-test landing AND on the full scaffolded G1/G2/G3 gate. No claims.yaml / manifest edits."
      governance_2026_06_09_pm: "V3-EXQ-603k LANDED PASS 2026-06-09T18:14Z (Stage-H harm-pathway readiness; claim_ids=[], non_contributory; reviewed). The PRIMARY nav/survival-competence ceiling is now resolved at the harm-pathway level: harm pathway trained 6242 steps, ARM_HARM_OFF_NAV nav-control still dies (G_H 0.0), harm_eval(z_world) range lifted to 0.133 (vs 603i flat ~0.002), load-bearing G_H clears 2/3, criteria_non_degenerate all true. With 603j (safety-half) this makes BOTH escape-affordance-bridge readiness prereqs green; the full 4-arm SD-059/MECH-358 bridge behavioural re-test is queued via chip. GAP-C stays in-progress + non-governance-weighting: the Q-045/MECH-313/MECH-260 behavioural retest stays gated on that full bridge re-test landing (and on the full scaffolded G1/G2/G3 gate, which 603k's narrow harm-pathway probe does not by itself satisfy). last_updated current."
      governance_2026_06_09: "Closure-drift stale-since-review reconcile. owner_exq repointed off the in-flight V3-EXQ-603i to absorb its terminal outcome + the later sibling 603j. 603i FAILed non_contributory/substrate_ceiling (escape-affordance bridge validation, claim_ids=[]; autopsy applied prior cycle) -- two co-equal substrate gaps, neither a bridge verdict. The SECONDARY gap (safety-half starvation) is now closed at the readiness layer: V3-EXQ-603j (escape_bridge_safety_half_readiness) PASSed 2026-06-09 (trained MECH-303/304 safety_signal 0.89 >= 0.5 floor + under-threat gate 0.58 >= 0.1; claim_ids=[], non_contributory, reviewed this cycle) -- the SD-059 safety half can now credit non-vacuously. The PRIMARY nav/survival-competence ceiling is being addressed by V3-EXQ-603k (Stage-H harm-pathway training). GAP-C stays in-progress and non-governance-weighting; the Q-045/MECH-313/MECH-260 behavioural retest stays gated on the full 4-arm escape-affordance bridge re-test, which is gated on the 603k nav-competence leg landing. last_updated bumped."
      governance_2026_06_08: "Plan-drift reconcile. The old prereq (2)/(3) resume list is obsolete. The scaffolded_sd054_onboarding survival/hazard leg has progressed through the Stage-H and escape-affordance-bridge amendments; the current active validation is V3-EXQ-603i, claimed on ree-cloud-1 at 2026-06-08T13:57:39Z, diagnostic claim_ids=[]. Status moves blocked_pending_substrate -> in-progress. GAP-C remains non-governance-weighting until 603i returns; only a PASS/non-vacuous readiness result unblocks the Q-045/MECH-313/MECH-260 behavioural retest."
      substrate_landed_2026_05_31: "Prereq (3) substrate change landed via /implement-substrate-infant-curriculum-h-pos-recal-20260531T123353Z (cross-link IGW-20260531-009). InfantCurriculumScheduler.H_POS_FRAC_OF_MAX recalibrated 0.70 -> 0.20 in ree-v3/experiments/infant_curriculum.py (Path (a) per failure_autopsy_V3-EXQ-591_2026-05-27 section 7). 0.20 * ln(144) ~= 0.99 sits inside the observed rolling-mean H_pos band 0.03-1.08 with ~9% margin above observed max. Path (b) alternative-gate (z_goal-norm / residue-coverage) NOT taken: z_goal collapses to ~1e-7 across 591 arms (blocked on prereq (2) goal_pipeline:GAP-4) and residue_coverage saturates trivially per autopsy. 3 contract tests added (test_infant_curriculum_gap9.py C11 trio: default-within-band, synthetic-P0-trajectory-advances, marginal-clearance). infant_substrate_expansion.md Section 6.1 (Phase 0 exit condition) updated. Status remains blocked_pending_substrate because prereq (2) z_goal-collapse blocker on goal_pipeline:GAP-4 / V3-EXQ-490g cohort is still load-bearing. When (2) clears, V3-EXQ-603d / 591b can queue immediately -- (3) is no longer the gate."
      resume_condition: "IN FLIGHT 2026-06-08 on V3-EXQ-603i. Do not queue the Q-045/MECH-313/MECH-260 retest until 603i lands. On 603i PASS/non-vacuous readiness, queue the GAP-C successor retest; on FAIL or substrate_not_ready_requeue, route to failure-autopsy/implement-substrate. 603i is diagnostic with claim_ids=[] and should not move claim confidence by itself."
    - id: "behavioral_diversity_isolation:GAP-D"
      title: "Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)"
      phase: "P1"
      status: done
      severity: medium
      owner_exq: "V3-EXQ-550 FAIL/supports MECH-269 (2026-05-11T20:18Z, diagnostic-probe; scoring_excluded); V3-EXQ-601 PASS/supports MECH-269b (2026-05-21T12:02Z, diagnostic-probe; scoring_excluded); R4.b stamped 2026-05-29; Q-040b behavioural sufficiency continues under goal_pipeline:GAP-4"
      unblocks_claims: [MECH-269, MECH-269b, Q-040]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-29
      governance_2026_05_29: "R4.b stamped this session per user authorisation (options i+ii+iii: plan-doc close + MECH-269/269b evidence_quality_note + drift-script extension). The supporting runs (V3-EXQ-550 + V3-EXQ-601) sit in claim_evidence.v1.json with evidence_direction=supports but flagged scoring_excluded=diagnostic_probe (both manifests carry experiment_purpose=diagnostic), so the standard /governance pipeline cannot auto-promote MECH-269 / MECH-269b off the hold_pending_v3_substrate recommendation -- the stamp is a governance-level recognition of the R4.b reading on the diagnostic evidence, not an experimental_confidence move. MECH-269 / MECH-269b remain v3_pending=true. The non-diagnostic behavioural sufficiency test (Q-040b) is owned by goal_pipeline:GAP-4 / V3-EXQ-490g Tier-1 retest cohort and is the path to lifting v3_pending. Drift-script extended to flag pending_governance_stamp on future plan-nodes so this manual-stamp loop closes automatically next time."
      resume_condition: "CLOSED 2026-05-29. R4.b stamped on V3-EXQ-550 + V3-EXQ-601 diagnostic evidence per behavioral_diversity_isolation_plan.md decision-rules (Theory 4 promoted; V_s pathology confirmed). Theory 4 contribution to the isolation matrix is now established at the diagnostic-probe level. Follow-up sufficiency work continues under goal_pipeline:GAP-4 (V3-EXQ-490g cohort); do NOT re-open GAP-D for that work -- it has its own closure node. Reopen GAP-D only if (a) the supports-MECH-269 per-claim direction on the V3-EXQ-550 manifest is later revised, or (b) a non-diagnostic falsifier at Layer D produces a contributory result that directly contradicts R4.b."
    - id: "behavioral_diversity_isolation:GAP-E"
      title: "Theory 5 (deferred): proposal-distribution bias (re-enters candidate set on R_X.c)"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["behavioral_diversity_isolation:GAP-A", "behavioral_diversity_isolation:GAP-B", "behavioral_diversity_isolation:GAP-C", "behavioral_diversity_isolation:GAP-D"]
      last_updated: 2026-05-25
      resume_condition: "Re-enters candidate set only if R_X.c fires -- i.e. the full 4-substrate stack (Layers A+B+C+D ON) still fails Rung 1 at ALL_ON. Until then, retained as secondary candidate but no falsifier is owed."
    - id: "behavioral_diversity_isolation:GAP-F"
      title: "Theory 6 (deferred): MECH-260 anti-recency contribution to behavioural diversity"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-260]
      depends_on: ["behavioral_diversity_isolation:GAP-C"]
      last_updated: 2026-05-25
      resume_condition: "Partially covered by Q-045 4-arm ablation (MECH-313 OFF / 313 only / 260 only / both ON) under GAP-C's V3-EXQ-603c retest. Promote to non-deferred only if the 4-arm result needs a dedicated MECH-260-vs-MECH-313 redundancy follow-up per R_X.b."
    - id: "behavioral_diversity_isolation:GAP-G"
      title: "Theory 7 (deferred): MECH-314 curiosity weight (Goldilocks calibration)"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-314, MECH-314a]
      depends_on: ["behavioral_diversity_isolation:GAP-B"]
      last_updated: 2026-05-25
      resume_condition: "V3-EXQ-590a annotated pending_retest_after_substrate (MECH-111 broadcast novelty was scalar EMA -> argmax-invariant null on selection). Re-queue as V3-EXQ-590b is gated on MECH-314a per-candidate RBF novelty implementation AND behavioural diversity landing (i.e. resolution of GAP-B). Until both gates clear, theory 7 stays deferred and its falsifier is not queued."
    - id: "behavioral_diversity_isolation:GAP-H"
      title: "Theory 8 (deferred): z_goal config-default confound"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["behavioral_diversity_isolation:GAP-D"]
      last_updated: 2026-05-25
      resume_condition: "Confound check on V3-EXQ-550 (Theory 4). If GAP-D's R4-rule application surfaces an ARM_ON >> ARM_OFF asymmetry that maps to z_goal config-default rather than V_s substrate pathology (R4.a), this node becomes the dedicated re-run with z_goal matched across arms. Until GAP-D's R4 disposition lands in governance, theory 8 stays deferred."
---

# Behavioural Diversity Isolation Plan (REE-v3)

**Created:** 2026-05-25T11:46:33Z
**Author session:** diversity-isolation-plan-20260525T114633Z
**Status:** draft (plan-of-record)
**Sibling to:** [`behavioral_diversity_acceptance_criteria.md`](behavioral_diversity_acceptance_criteria.md)
**Related claims:** ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a/b/c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076

---

## Purpose

The acceptance-criteria doc (sibling) defines **what counts as success** for behavioural
diversity in REE-v3. This document defines **how we isolate which of the candidate failure
mechanisms is load-bearing** when diversity fails. The two are complementary:

| Doc | Question answered |
|-----|-------------------|
| `behavioral_diversity_acceptance_criteria.md` | When can we say diversity is real and useful? |
| `behavioral_diversity_isolation_plan.md` (this) | When diversity is absent, which substrate layer is responsible? |

The isolation plan is needed because **diversity failure is multi-causal**: ARC-065 already
commits the architecture to a distributed pathway (LC-NE tonic + frontopolar curiosity +
striatal novelty + hippocampal trajectory sampling), and multiple layers can independently
suppress the observed action-class entropy. Without an isolation matrix, a Rung-1 FAIL is
under-determined: we don't know which substrate to fix next.

---

## Layer model: where diversity can collapse

Diversity must survive all four layers between candidate generation and observable action.
Failure at any one layer reproduces the monostrategy phenotype downstream.

```
                  ARC-065 distributed diversity-generation pathway
                                    |
                                    v
   [ Layer A: PROPOSAL ]  hippocampal trajectory sampling, CEM candidate pool
                                    |
                                    v
   [ Layer B: SCORING ]    E3 score aggregation across trajectory classes
                                    |
                                    v
   [ Layer C: ACTION-SELECT ]  softmax / argmax over E3-ranked candidates
                                    |
                                    v
   [ Layer D: REPRESENTATION ] V_s anchor sets / regional verisimilitude
                                    | (feeds back into Layer A on next tick)
                                    v
                              observable action stream
```

**Layer D feedback note.** Layer D is not strictly downstream of A-C in a single tick --
state representation in tick t+1 depends on what was committed in tick t. Stale V_s
representations therefore amplify monostrategy across episodes even when Layers A-C are
behaving correctly within any one tick. This is why MECH-269 reads as "monostrategy"
upstream of the action-selection stack despite acting on representations.

---

## The 4 theories (top of the candidate field)

Drawn from the 8-mechanism survey 2026-05-25 (see prior conversation / governance log).
Theories 5-8 (proposal-distribution bias, MECH-260 anti-recency, curiosity weight, z_goal
config-default confound) are retained as secondary candidates but not the focus of this
plan.

| # | Theory | Layer | Primary claim | Falsifier EXQ | Status |
|---|--------|-------|---------------|---------------|--------|
| 1 | CEM elite-pool collapse to one action class | A | ARC-065 (SP-CEM child) | V3-EXQ-567 / V3-EXQ-569 | landed 2026-05-17 (main-path); matched-entropy control pending |
| 2 | **E3 scoring collapses diverse candidates to one** | **B** | **MECH-341 (new)** | **TBD (this plan, design below)** | **unclaimed gap until 2026-05-25** |
| 3 | Missing tonic noise floor (LC-NE analog) | C | MECH-313 | V3-EXQ-543b ARM_MECH313_only | substrate landed, matched-entropy gate pending |
| 4 | V_s regional verisimilitude staleness | D | MECH-269 / 269b | V3-EXQ-550 (live falsifier) | falsifier in flight |

**Headline gap.** Theory #2 (E3 scoring) is the highest residual leverage because the other
three either have landed substrate (#1, #3) or have an active falsifier (#4). MECH-341
registered in this pass closes the claim-side of the gap; the experiment design (Section 5)
closes the test-side.

---

## Isolation matrix

Each row is an experiment arm; each column is a substrate ON/OFF. A run produces the row
of outcomes; comparison across rows pins the contribution of each substrate. The matrix is
designed so that *any single substrate ablation against the all-ON baseline gives a
single-substrate contribution estimate*; the all-OFF arm is the Rung-0 substrate-naive
baseline that anchors ARC-065's architectural commitment.

| Arm | SP-CEM (A) | E3 score-diversity (B) | Noise floor MECH-313 (C) | V_s active MECH-269 (D) | Use |
|-----|:----------:|:---------------------:|:------------------------:|:----------------------:|-----|
| BASE_OFF | off | off | off | off | Rung 0 baseline / ARC-065 architectural-necessity check |
| ALL_ON | **on** | **on** | **on** | **on** | Rung 1 target (matched-entropy controlled) |
| A_only | on | off | off | off | Theory 1 contribution (SP-CEM proposal lift in isolation) |
| B_only | off | **on** | off | off | Theory 2 contribution (E3 scoring lift in isolation) |
| C_only | off | off | **on** | off | Theory 3 contribution (noise floor in isolation) |
| D_only | off | off | off | **on** | Theory 4 contribution (V_s in isolation) |
| ablate_A | off | on | on | on | Marginal cost of removing SP-CEM |
| ablate_B | on | off | on | on | Marginal cost of removing E3 diversity preservation |
| ablate_C | on | on | off | on | Marginal cost of removing noise floor |
| ablate_D | on | on | on | off | Marginal cost of removing V_s |
| MATCHED_NOISE | off | off | T=2.5 uniform | off | FP-2 control: structured-vs-noise comparison for acceptance doc Rung 1 |

**Pragmatic note.** The full 11-arm matrix is not required in a single run. Sequencing
(Section 6) reduces this to a phased programme of 3-arm and 4-arm experiments that each
answer one question.

**Layer-B substrate gap.** "E3 score-diversity ON" requires MECH-341 substrate to exist;
until it lands, B columns are vacuously OFF and theories 1/3/4 are the only testable axes.
MECH-341 substrate work is a prerequisite for the full matrix.

---

## Decision rules

Each rule has the form `if (observation) -> (decision)`. Rules are applied in order; the
first matching rule wins.

### Theory 1 (CEM elite-pool collapse)

- **R1.a** If V3-EXQ-569 matched-entropy control shows SP-CEM entropy = noise-matched entropy on
  all diversity metrics (entropy, coverage, trajectory_class_count): theory 1 is **not
  load-bearing on its own**. ARC-065 SP-CEM child substrate marked `non_contributory` for
  diversity (separate from its non-collapse role). Promote attention to theories 2-4.
- **R1.b** If V3-EXQ-569 shows SP-CEM strictly > matched noise on trajectory_class_count
  (FP-2 cleared): theory 1 confirmed as a real contributor; advance to Rung 2 testing.

### Theory 2 (E3 scoring collapse) -- this plan's primary new test

- **R2.a** If pre-MECH-341 trajectory_class_count >= 2 in CEM candidates but post-E3-scoring
  selected class count = 1 for >= 80% of timesteps (measured on SP-CEM-ON, MECH-269-ON
  baseline): theory 2 is confirmed as a real diversity-collapse site. MECH-341 substrate
  becomes priority.
- **R2.b** If post-E3 selected class count tracks pre-E3 candidate class count within +/- 1
  on average: theory 2 is **not load-bearing**. E3 is preserving the diversity it receives;
  the collapse must be at A or C or D. MECH-341 retains as architectural commitment but no
  substrate work is triggered.
- **R2.c** If theory 2 confirmed AND MECH-341 substrate lands AND `B_only` arm produces
  trajectory_class_count >= 2 with first_action_entropy > 0.3: MECH-341 provisional
  promotion candidate.

### Theory 3 (noise floor)

- **R3.a** If MECH-313 ON alone (`C_only` arm) produces matched-entropy-distinguishable lift
  on trajectory_class_count but not on coverage: theory 3 contributes to per-tick entropy
  but not to strategic diversity. Retain MECH-313 as Layer-C substrate but escalate
  attention to theories 2/4.
- **R3.b** If ablate_C arm (drop MECH-313 from ALL_ON) drops trajectory_class_count below 2
  while Rung 1 metrics for ALL_ON pass: MECH-313 is necessary-and-sufficient at Layer C;
  promote on Rung 2 PASS.
- **R3.c** If ablate_C arm leaves Rung 1 metrics unchanged from ALL_ON: MECH-313 is
  redundant under combined substrate -- candidate for de-prioritisation pending broader
  ablation matrix.

### Theory 4 (V_s representation staleness)

- **R4.a** If V3-EXQ-550 ARM_ON >> ARM_OFF on relevant diversity metrics: confounded by
  z_goal config default; V_s pathology not confirmed; theory 4 demoted. Re-run with z_goal
  matched across arms before re-evaluating.
- **R4.b** If V3-EXQ-550 ARM_ON ≈ ARM_OFF: V_s substrate pathology confirmed; theory 4
  promoted; MECH-269 follow-up substrate work prioritised.
- **R4.c** If V3-EXQ-550 ARM_ON crashes: separate substrate bug surfaces; classify as
  failure_autopsy candidate; theory 4 status unchanged until autopsy resolves.

### Cross-theory escalation rules

- **R_X.a** If ALL_ON arm produces Rung 1 PASS but `A_only`, `B_only`, `C_only`, `D_only`
  all individually FAIL Rung 1: diversity is **emergent across substrates** (INV-074
  plasticity-crystallization invariant fires); no single Layer is load-bearing. Promote
  ARC-065 on multi-arm evidence.
- **R_X.b** If two single-substrate arms (e.g., `A_only` and `C_only`) each PASS Rung 1
  independently: substrates are **partially redundant**; revisit Q-045 (MECH-313 vs
  MECH-260 independence) and propose new Q-claim on A-vs-C redundancy.
- **R_X.c** If ALL_ON FAILS Rung 1: the four-substrate stack as currently specified is
  insufficient; **expand candidate set** to theories 5-8 (proposal-distribution bias,
  MECH-260 anti-recency, MECH-314 curiosity weight, z_goal config-default) before further
  Layer-A/B/C/D refinement.

---

## Experiment sequencing

Layer-B (MECH-341) substrate does not yet exist, so the full isolation matrix cannot run
in one pass. Phased approach:

### Phase P1 -- Pre-existing-substrate isolation (executable now)

**Arms:** BASE_OFF, A_only, C_only, D_only, ALL_ON (excluding Layer-B). MATCHED_NOISE
arm for FP-2 control. **6 arms.**

**Target:** Pin which of theories 1, 3, 4 is load-bearing under the current main-path
substrate. Apply R1, R3, R4 decision rules.

**Falsifiers reused:** V3-EXQ-567 (A_only effect already measured), V3-EXQ-569 (matched
noise, queued), V3-EXQ-550 (D_only effect, in flight).

**Required new EXQ:** A 6-arm P1 isolation run combining all three substrates on a single
SD-054 episode set, so the cross-substrate comparison is on matched data. Recommend
queueing as **V3-EXQ-TBD (P1 layer isolation, 6 arms)** -- queue via `/queue-experiment`
skill, not directly.

### Phase P2 -- E3 scoring diagnostic (executable now; no substrate needed)

**Arms:** ALL_ON_now (A+C+D, no MECH-341), instrumented to log:
- per-tick: pre-E3 CEM candidate trajectory_class_count
- per-tick: post-E3 selected trajectory_class_count
- per-tick: E3 score distribution across distinct classes (mean, std, top-2 gap)

**Target:** Apply R2.a / R2.b. **No substrate change**, just instrumentation. If R2.a
fires: MECH-341 substrate work is justified and prioritised. If R2.b fires: MECH-341 stays
architectural-only.

**Required new EXQ:** **V3-EXQ-TBD (P2 E3 score-collapse diagnostic, instrumentation only)**.
Same SD-054 episode set as P1; can be a single-arm probe.

### Phase P3 -- MECH-341 substrate build + B-axis test

**Trigger:** P2 confirms R2.a.

**Substrate work:** Implement MECH-341 (one of: entropy bonus over candidate classes at
E3 aggregation; class-stratified argmax with proportional sampling within class; jittered
tie-breaking when top-K E3 scores are within epsilon). Specific design open -- see
"Substrate design options" below.

**Arms (post-build):** B_only, ablate_B, ALL_ON (now including B). **3 arms.**

**Target:** Apply R2.c. Promote MECH-341 if `B_only` produces Rung 1-comparable diversity
in isolation OR if ablate_B drops Rung 1 metrics significantly.

### Phase P4 -- Full matrix (post-MECH-341 landing)

Run the 11-arm matrix on a downstream env (CausalGridWorld or a new substrate) for
replication and to apply R_X rules.

**Design doc staged 2026-05-31:** [`v3_exq_p4_11arm_isolation_design_2026-05-31.md`](v3_exq_p4_11arm_isolation_design_2026-05-31.md)
fully specifies the 11 arms, R_X.a/b/c acceptance grid, data plan, V3 substrate
tagging requirements, and Python skeleton (forked from
`ree-v3/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py`).
Reserved queue ID: **V3-EXQ-618** (priority 90, one rung below V3-EXQ-616).

**Gating EXQ:** P4 fires AFTER **V3-EXQ-614b** PASSes (the MECH-341 amend-and-re-run
cycle on the SD-056-amended substrate, queued 2026-05-31T12:32Z @ priority 250).
Informed by V3-EXQ-616 (Q-054 entropy_bias_scale sweep -- sets
`MECH341_ENTROPY_BIAS_SCALE`) and V3-EXQ-569a (GAP-A R1.b matched-entropy FP-2 --
sets A_only expectation). Plan-doc's original blocker text ("Blocked on Rung 2
SD-054 clearance + MECH-341 landed") is now satisfied at the diagnostic-probe level
(GAP-B partial-PASS via R2.c on V3-EXQ-614a establishes the Rung-2 reading;
MECH-341 substrate landed 2026-05-27 + amend landed 2026-05-31). The remaining
gate is the behavioural confirmation that 614b PASSes on the amended substrate.

Submission protocol in design-doc Section 11. Design doc stays `status: STAGED`
until 614b PASSes; submission session updates to `status: SUBMITTED` with
queue-time decisions recorded.

---

## Substrate design options for MECH-341 (when P3 triggers)

The claim asserts that E3 must preserve trajectory-class diversity across its scoring step.
There are at least three plausible implementations:

1. **Entropy bonus over candidate classes.** E3 score = harm_score + lambda * H(class | candidates).
   Penalises homogenisation of the candidate pool at scoring time. Risk: lambda is another
   tuning knob; matched-noise control needed.
2. **Class-stratified argmax with within-class proportional sampling.** Stratify candidates
   by first-action class; pick best within each class; sample across classes proportional
   to their best-in-class scores. Preserves all surviving classes; biases toward best
   representative of each. **Amend 2026-06-01:** within-class step gains an
   optional temperature `stratified_within_class_temperature` (`None` = legacy
   argmin bit-identical; positive `T` = sample within each class via
   `softmax(-class_scores / T)`). Decoupled from the existing across-class
   `stratified_temperature` so the A-vs-B partial-redundancy probe can
   dissociate within-class and across-class layers in V3-EXQ-614c.
3. **Jittered tie-breaking near top.** Standard argmax, but when top-K scores are within
   epsilon, sample uniformly across them. Cheapest implementation; only affects diversity
   when E3 scores are nearly tied (which is precisely when diversity is being lost).

These three options are not mutually exclusive (could combine 1+3). Pre-implementation
governance: which to try first should be decided after P2 results, since P2's per-tick E3
score distribution data will tell us whether the collapse is happening at near-ties
(option 3 sufficient) or at large score gaps (option 1 or 2 required).

---

## Status table (resume primitive)

| Theory | Layer | Claim | Substrate status | Falsifier | Result | Decision |
|--------|-------|-------|------------------|-----------|--------|----------|
| 1 CEM collapse | A | ARC-065 (SP-CEM child) | landed 2026-05-17 main-path; **E2-world-forward per-candidate signal collapse identified 2026-05-25 (root cause doc)** | V3-EXQ-567 / V3-EXQ-569 / V3-EXQ-571 / V3-EXQ-573 / V3-EXQ-609 | 567 PASS (entropy 0.012->0.497); 569 + 573 non_contributory (bias channel structurally zero); 570/571/609 diagnostics landed | **R1 falsifier blocked**: per-candidate bias signal structurally zero (all K cands -> identical z_world after one E2 step). Awaiting E2-world-forward substrate fix; V3-EXQ-569a queued after substrate lands |
| 2 E3 scoring | B | **MECH-341** (registered 2026-05-25) | **IMPLEMENTED 2026-05-27 (options 1+2 togglable); RETUNE 2026-05-28 (stratified_select on both branches + lambda/scale defaults); AMEND 2026-06-01 (stratified_within_class_temperature lever + A-vs-B probe naming)** | V3-EXQ-608 P2 (PASS R2a 2026-05-26); V3-EXQ-611c PASS 2026-05-29; V3-EXQ-614a PASS_C2_C3_only 2026-05-30; V3-EXQ-614b FAIL_no_criterion 2026-05-31 (per-claim non_contributory MECH-341 + ARC-065 via /governance); V3-EXQ-616 FAIL_no_floor_under_max_swept_scale 2026-05-31 (per-claim non_contributory Q-054 + MECH-341 via /governance); V3-EXQ-614c queued 2026-06-01 | 608 R2a fired; substrate + retune validated; 614b structural ARM_0 degeneracy without SP-CEM Layer A; 616 mathematically rules out scale-axis isolation of MECH-341 under SP-CEM-OFF; amend landed adding within-class proportional sampling lever | await V3-EXQ-614c manifest -- C1 regression-guard + C2 within-class lift or C3 substrate-readiness; PASS clears MECH-341 v3_pending |
| 3 noise floor | C | MECH-313 | landed | V3-EXQ-543b ARM_MECH313 (pending Q-045 retest) | autopsy 603b: substrate operative but design-blocked | retest via 603c (training-phase fix) |
| 4 V_s stale | D | MECH-269 / 269b | substrate-ready (IGW-021); MECH-269b staleness wiring landed | V3-EXQ-550 (z_goal probe); V3-EXQ-601 (MECH-269b staleness gate) | 550 FAIL/supports MECH-269 2026-05-11T20:18Z; 601 PASS/supports MECH-269b 2026-05-21T12:02Z; both reviewed; both diagnostic-probe (scoring_excluded) | **R4.b STAMPED 2026-05-29** (V_s pathology supported on diagnostic evidence; theory 4 promoted). Closure node done. MECH-269 / MECH-269b stay v3_pending=true; Q-040b behavioural sufficiency continues under goal_pipeline:GAP-4 (V3-EXQ-490g cohort) |

**Update cadence:** every time a P-phase experiment lands, update this table in-place with
the result and the decision-rule outcome. This is the resume primitive across sessions.

### 2026-05-29 GAP-D R4.b stamp (CLOSED)

R4.b stamped this session per user authorisation (options i+ii+iii: plan-doc close +
MECH-269 / MECH-269b evidence_quality_note in claims.yaml + drift-script extension).

**Why the manual stamp.** The supporting runs (V3-EXQ-550 + V3-EXQ-601) sit in
`claim_evidence.v1.json` with `evidence_direction=supports` but flagged
`scoring_excluded=diagnostic_probe` (both manifests carry `experiment_purpose=diagnostic`).
The indexer correctly excludes diagnostic-probe runs from `experimental_confidence`, so
MECH-269 / MECH-269b show `exp_conf=0.0` and the standard `/governance` pipeline can only
recommend `hold_pending_v3_substrate` (applied). Auto-promotion via the experimental
gate is therefore architecturally unavailable for diagnostic-probe evidence.

R4.b is a **governance-level recognition** of the V_s-pathology reading on the diagnostic
evidence -- a different kind of stamp than a confidence-driven promotion. It promotes the
theory within the isolation-plan reasoning (Theory 4 contribution to the isolation matrix
is established) without claiming the v3_pending substrate gate has cleared.

**What did NOT change.** MECH-269 / MECH-269b remain `v3_pending: true` in claims.yaml.
The non-diagnostic behavioural sufficiency test (Q-040b) is owned by
`goal_pipeline:GAP-4` / V3-EXQ-490g Tier-1 retest cohort, and is the path to lifting
v3_pending. Promotion off `hold_pending_v3_substrate` waits on a non-diagnostic experimental
result.

**What did change.**
- This node: `status: pending_governance_stamp` -> `done`; `last_updated: 2026-05-29`.
- claims.yaml: `evidence_quality_note` added to MECH-269 + appended to MECH-269b citing
  the R4.b stamp on the diagnostic-probe supports-direction.
- scripts/check_closure_drift.py: `NON_TERMINAL_STATUSES` extended to include
  `pending_governance_stamp`, so future plan-nodes parked at this status get flagged
  automatically on the next /governance cycle (closes the manual-stamp loop).

**Prior disposition (2026-05-28, by igw-011-gapd-doc-sync).** R4.b reading was applied to
the status table by that session under `pending_governance_stamp`. The 2026-05-29 stamp
above completes that disposition; the prior R4.a/R4.b/R4.c decision-rule walk is preserved
in the manifest interpretation grid and in the V3-EXQ-550 manifest `evidence_direction_note`.

---

---

## New claims registered with this plan (2026-05-25)

| Claim | Title (abbreviated) | Type | Status |
|-------|---------------------|------|--------|
| MECH-341 | e3_scoring_preserves_trajectory_class_diversity | mechanistic_implementation | candidate, v3_pending |
| Q-054 | minimum trajectory-class diversity floor for ARC-062 (was proposed as Q-046) | open_question | open |
| Q-055 | sleep consolidation: diversity-preserving vs eroding (was proposed as Q-047) | open_question | open |
| INV-076 | behavioural diversity as structural prerequisite for ethical counterfactual evaluation (was proposed as INV-074 -- ID taken 2026-05-17 by plasticity-crystallization invariant) | invariant (universal) | candidate |

Q-054, Q-055, INV-076 supersede the 2026-05-15 "proposed new claims" in the
acceptance-criteria doc (Q-046, Q-047, INV-074); their original IDs were never registered
and INV-074 was subsequently taken by a different, broader claim about plasticity
crystallization. The new IDs preserve the original scientific intent under the next
available IDs in their respective ranges.

---

## What this plan does NOT do

- **Does not redefine acceptance criteria.** The Rung 0-4 framework in the sibling
  acceptance-criteria doc is authoritative. This plan layers an isolation analysis on top of
  it.
- ~~**Does not commit to a MECH-341 implementation.** P2 diagnostic results determine which
  of the three design options (Section "Substrate design options") to build.~~ Superseded
  2026-05-27: V3-EXQ-608 P2 majority `R2a_e3_collapse_confirmed_large_gap` (large-gap,
  ruling out option 3 jittered tie-breaking) routed the substrate-design phase to options
  1 + 2. Both landed as togglable sub-flavours under one master in
  `ree-v3/ree_core/predictors/e3_score_diversity.py`. Design doc:
  `REE_assembly/docs/architecture/mech_341_e3_score_diversity_preservation.md`.
- **Does not address theories 5-8.** Those remain candidate mechanisms and re-enter the
  candidate set only if R_X.c fires (full 4-substrate stack insufficient).
- **Does not queue experiments directly.** All EXQ entries flagged here go through
  `/queue-experiment` for code-review + smoke-test discipline.

---

*This document is the plan-of-record for behavioural diversity ISOLATION (which substrate*
*layer is responsible when diversity fails). For acceptance criteria, see the sibling*
*`behavioral_diversity_acceptance_criteria.md`.*
