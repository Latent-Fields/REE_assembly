---
closure_plan:
  id: commitment_closure
  title: "Commitment / Closure / Mode-Governance"
  registered: 2026-05-08
  last_updated: 2026-08-22
  scope_claims: [SD-033a, SD-033b, SD-033c, SD-033d, SD-033e, SD-034, MECH-090, MECH-091, MECH-260, MECH-262, MECH-263, MECH-266, MECH-267, MECH-268]
  sibling_plans: [sd033_governance]
  nodes:
    - id: "commitment_closure:GAP-1"
      title: "SD-033a bias head untrained (Go-side mechanically silent)"
      status: done
      severity: load-bearing
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-033a, MECH-262, SD-034]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      cross_plan_link:
        - "arc_062_rule_apprehension:GAP-A"
        - "arc_062_rule_apprehension:GAP-B"
        - "arc_062_rule_apprehension:GAP-C"
        - "arc_062_rule_apprehension:GAP-D"
      blocking_external: []
      last_updated: 2026-05-29
      completion_note: "V3-EXQ-598b ran 20260527T120345Z and confirmed C1 frozen_silent PASS (bias=0 when head frozen) + C2 trainable_nonzero PASS (head learned mean abs 0.05-0.10 when trainable). Bias head is no longer mechanically silent. SD-033a recorded as supports (substrate fires as specified). The downstream C3 trainable_not_monomodal FAIL (P2 reef-visit fractions remained equivalent across frozen and trainable arms) is a separate substrate_ceiling: MECH-262 reclassified weakens -> non_contributory + epistemic_category=substrate_ceiling + pending_retest_after_substrate=true on the rule-creator/discriminator substrate (the next layer that would populate DIFFERENTIATED rule_state inputs). That work is tracked under arc_062_rule_apprehension:GAP-B (re-blocked 2026-05-29 on rule-creator substrate) and via the MECH-262 retest flag, not under this gap. GAP-1's narrow scope (head is untrained) is RESOLVED."
      resume_condition: "GAP-1 closes on V3-EXQ-598b PASS (2-arm ablation). Per failure_autopsy_V3-EXQ-543l_2026-05-27 sections 7+9, V3-EXQ-598b is the DISCRIMINATOR between substrate-enrichment (predicted PASS -- GAP-C/D routing consumer rescues differentiation) and test-design-ceiling (predicted FAIL -- REINFORCE on shared return structurally insufficient regardless of consumer) readings. 543l FAIL/mixed (2026-05-26) does NOT block 598b; the autopsy explicitly routes substrate-enrichment-first. 598b carries a PERMISSIVE startup gate (manifest exists + outcome in {PASS, FAIL}); contributory PASS on 543l is NOT required."
      substrate_note: "GAP-C + GAP-D substrate implemented 2026-05-17 (discriminator_proj + train_rule_bias_head + bias_head_parameters). V3-EXQ-598b queued 2026-05-27 (ree-v3 main 94db78d; supersedes V3-EXQ-598a; gates_on_exq=V3-EXQ-543l with permissive semantic per autopsy routing; priority 240): frozen vs trainable bias head on ARC-062+SD-054 stack (SP-CEM main-path defaults, differential heads, mode_separation_floor=0.25, P1_W_DEVIATION_AUX_WEIGHT=0.1). claim_ids=[SD-033a, MECH-262] with evidence_direction_per_claim (SD-034 dropped: closure_operator not exercised by 2-arm ablation). Dry-run smoke: ARM_0 frozen PASS bias=0; ARM_1 trainable FAIL on tiny 3+4+2 ep schedule (documented insufficient-budget signature). Per autopsy section 9 retest sequence on full-run completion: contributory PASS -> close GAP-1 + ARC-062 weak-reading governance-stamped viable; FAIL/weakens -> ARC-063 V4 lit-pull + design session; non_contributory -> /diagnose-errors."
    - id: "commitment_closure:GAP-2"
      title: "EXP-0157 (V3-EXQ-461) delayed-reward persistence PASS"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-033a, MECH-090, SD-034]
      depends_on: []
      completion_note: "V3-EXQ-461 substrate-readiness runner PASS reviewed 2026-05-12; full behavioural delayed-reward arm remains blocked on GAP-3 env extensions."
      last_updated: 2026-05-12
    - id: "commitment_closure:GAP-3"
      title: "CausalGridWorldV2 env extensions (tolerance/counter-evidence/dual-cue)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-034, MECH-266, MECH-268]
      depends_on: []
      blocking_external: []
      last_updated: 2026-05-17
      completion_note: "Primitives 1-3 IMPLEMENTED 2026-05-17 in ree-v3/ree_core/environment/causal_grid_world.py (env-only constructor kwargs; NO config.py/REEConfig/queue -- concurrency-safe vs the active goal_pipeline:GAP-3 session). Validated by ree-v3/tests/contracts/test_env_extensions_gap3.py 14/14 (C1 bit-identical OFF + frac=0.0 dynamics-identical; C2 tolerance band/graded_exp; C3 counter-evidence persistent-only + monotone validity->floor + context-invariant; C4 dual-cue SD-049 fail-fast + accounting; C5 spec-section-5 integration smoke) and full ree-v3 contract regression 434/434. NO claim-validation EXQ (spec section 5: env infrastructure; concurrency forbade queue) -- a spec-sanctioned deviation from the implement-substrate skill Step 8. Scope deviation: completion_tolerance_targets='waypoint+resource' is reserved/fail-fast (primitive 1 ships waypoint-only per Q-1a; no EXP arm needs the resource half). GAP-3 (= the tolerance/counter-evidence/dual-cue env primitives) is DONE; this unblocks GAP-8 (depends_on GAP-3). NOTE: the SD-034/MECH-266/MECH-268 *behavioural* arms still require deliverable 4 (phased rule_state training curriculum -- the V3-EXQ-321/261 blocker), which was deliberately split into its own separate design pass (spec section 6) and is NOT part of GAP-3. Spec: causalgridworldv2_env_extensions_spec.md (Status: IMPLEMENTED 2026-05-17)."
    - id: "commitment_closure:GAP-4"
      title: "OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction"
      status: in-progress
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-034, MECH-266, MECH-267, MECH-268, MECH-090, MECH-342]
      depends_on: ["commitment_closure:GAP-2"]
      cross_plan_link: ["sd033_governance:CHK-EXP_PROPOSALS", "conversion_ceiling_campaign:P2-rootC"]
      last_updated: 2026-08-18
      governance_2026_08_16: "Stale-since-review acknowledgement + routing update (no status change; /governance cycle cranky-driscoll-126a36). Flagged by check_closure_drift.py's date-aware section: confirmed failure_autopsy_V3-EXQ-934_2026-08-16 reclassified MECH-266, which is in this node's unblocks set, after the 2026-08-12 last_updated. TWO substantive movements this cycle, both on this node's claims. (1) MECH-266: V3-EXQ-934 is adjudicated non_contributory and explicitly PERIPHERAL -- its manipulation arm (ARM_ASYM_STICKY_TASK sticky exit rail) sat at fraction_in_external_task 1.0 with n_switches 0 in ALL 15 cells (3 seeds x 5 caps), and the load-bearing criterion was evaluated on the SYMMETRIC arm, which contains no MECH-266 mechanism. So NO substrate_ceiling attribution accrues to MECH-266 from this run and its brake count is UNCHANGED at 6. The run establishes a measurement precondition for a future MECH-266 test and weighs nothing either way. Its sibling SD-032a takes the cycle's only supports (narrow, diagnostic): genuine discrete alternation where the argmax crossing sits (seed 42 @ cap 0.75, 19 switches; seed 43 @ cap 1.75, 18 switches) -- the FIRST alternating occupancy in this lineage, which previously read 0.0 or 1.0 everywhere. READ NARROWLY: the passing criterion is an EXISTENTIAL over a 5-point cap grid evaluated per seed, the two passing seeds sit at OPPOSITE ENDS, no single cap grades on more than 1 of 3 seeds, so winning_cap_band is the min/max of two disjoint singletons and NO common operating point was demonstrated; H2 (structurally bang-bang) is NOT eliminated. Successor V3-EXQ-935 (claimed 2026-08-16T13:01Z) already tests the common-operating-point question via a margin-normalised cap rule on 5 seeds. (2) MECH-267: confirmed failure_autopsy_927-928-mech267-cluster_2026-08-16 localises the mode-content wash-out to CEM REFIT BREADTH -- H3 (mode_partitioned_cem) - OFF = +0.0167 paired, t=+4.34, 24/30 seeds positive, while H2 (mode_value_weight) is a CLEAN NULL at +0.0015, t=+0.48. That RESOLVES the H2/H3 fork this node's governance_2026_08_12 note recorded as 'TWO live loci, NEITHER built': the answer is H3. substrate_queue SD-MECH267-CEM-SELECTION-FIX amended accordingly. Both facets still default OFF, so MECH-267 mode-conditioning remains washed out in production until the default flips, and its pending_retest is now gated on that DEFAULT FLIP rather than on a build. V3-EXQ-927 was additionally marked superseded as a burned-id duplicate of 928 (bit-identical numerics, no ree_core change) so it stops double-counting in MECH-267 population statistics. GAP-4 stays in-progress; the live: head already re-projected via Step 3c pre-heal, so only last_updated is bumped here. PROMOTES/DEMOTES NOTHING beyond the evidence_quality_notes applied in claims.yaml this cycle."
      governance_2026_08_12: "Stale-since-review acknowledgement + routing update (no status change; /governance cycle sd-016-h3-algorithm-3370cd). Flagged by check_closure_drift.py date-aware section: confirmed failure_autopsy_V3-EXQ-923_2026-08-12 reclassified MECH-267, which is in this node unblocks set, after the 2026-08-10 last_updated. Substance: 923 ELIMINATES H1 (iteration-count) of the GOV-FANOUT-1 portfolio opened by failure_autopsy_V3-EXQ-869a_2026-08-03 -- production-settings content wash-out is not iteration-count dependent (gaps flat by iters=2, unchanged at iters=3). non_contributory, consistent with the long-standing pattern this node history records for MECH-090/MECH-267 legs (eliminate a rival rather than falsify). What IS new since 2026-08-10: the portfolio is down to TWO live loci, H2 (mode-dependent term in the CEM elite-selection value function) and H3 (hard-partitioned per-mode candidate pools), NEITHER built, and substrate_queue entry SD-MECH267-CEM-SELECTION-FIX was created this cycle to own them -- deliberately unscoped between H2/H3 per the 2026-08-12 user decision (neither costed). GAP-4 stays in-progress; the live: head already re-projected to the 923 autopsy via Step 3c pre-heal, so only last_updated is bumped here. PROMOTES/DEMOTES NOTHING beyond the MECH-267 evidence_quality_note applied in claims.yaml this cycle."
      governance_2026_08_10: "Stale-since-review acknowledgement only (no status change; /governance cycle queue-depth-low-ops-aac785). Flagged by check_closure_drift.py's date-aware section for 4 confirmed autopsies landing after the 2026-06-25 last_updated, touching this node's scope_claims: failure_autopsy_V3-EXQ-871_2026-08-02 (MECH-090, non_contributory/measurement_test_design_defect, routing=queue-experiment), failure_autopsy_V3-EXQ-869_2026-08-02 (MECH-267, non_contributory/competence_implementation_gap, routing=implement-substrate), failure_autopsy_V3-EXQ-869a_2026-08-03 (MECH-267, non_contributory/competence_implementation_gap, routing=queue-experiment), plus one further reclassification the drift report's summary truncated. All three checked directly are non_contributory (no weakens/supports) -- consistent with the long-standing pattern in this node's history where MECH-090/MECH-267 legs repeatedly self-route substrate_not_ready_requeue rather than falsify. None changes GAP-4's load-bearing status. GAP-4 stays in-progress; last_updated bumped to acknowledge."
      governance_2026_06_25: "Stale-since-review acknowledgement only (no status change; session governance-cycle-20260625T0420Z). Flagged because failure_autopsy_V3-EXQ-466d_2026-06-24 (applied by governance-cycle-20260624T2249Z) reclassified SD-034 -> non_contributory, and SD-034 is in this node's unblocks set. That reclassification is the residue-DISCHARGE leg (part c of the SD-034 done-token), which the 466d autopsy itself called structurally DISTINCT from the MECH-445/446 latch/beta de-commit lineage the 460e..460l autopsies (this node's owner_exq) test -- and it was already reconciled last cycle onto the SIBLING child node commitment_closure:GAP-4-battery (owner repointed 466d -> V3-EXQ-466e). THIS node (GAP-4) tracks the (b) de-commit-conversion lineage per governance_2026_06_23b, which the 466d/SD-034 discharge result does not touch. GAP-4 stays in-progress on the f_dominance_conversion_ceiling amend. last_updated bumped to acknowledge."
      governance_2026_06_23b: "SPLIT (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). This node's title bundles TWO sub-questions whose work has diverged: (a) OCD-BATTERY COMPLETENESS (the 460b/461/463b/464b/466b/467b/468b *b behavioural cohort for SD-034/MECH-266/267/268 + MECH-342 ecological) and (b) the MECH-090/445/446 COMMIT-ENTRY / DE-COMMIT CONVERSION lineage (the 460h..460l F-dominance lineage, now cross-linked to conversion_ceiling_campaign:P2-rootC). The ~600-word owner_exq is entirely the (b) lineage; (a) is owed-but-unqueued and invisible. Surfaced (a) as a child node commitment_closure:GAP-4-battery so the owed battery arms are visible; THIS node (GAP-4) now tracks the (b) de-commit-conversion lineage. No status change to GAP-4 (in-progress, gated on the f_dominance_conversion_ceiling amend the re-derive brake routed -- under active build by 2 concurrent /implement-substrate sessions)."
      governance_2026_06_23: "460k RAN + 460l (its JOB-2 successor) RAN + AUTOPSIED (session failure-autopsy-460l-20260623T0401Z, this autopsy). Both terminal FAIL/non_contributory. 460k (the rung-6 duration-lever retest) was adjudicated by the concurrent failure-autopsy-460k session (confirmed substrate_ceiling/non_contributory). V3-EXQ-460l -- the ARC-108 JOB-2 control-plane L0/L1/L2 falsifier (rho_t maintenance ramp + habenula negative-delta_t de-commit DRIVER pair, ree-v3 main c5614ab, the biologically-faithful B6 successor to the rung-6 lever) -- RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z (ree-cloud-4; manifest v3_exq_460l_job2_control_plane_ramp_habenula_falsifier_20260622T221756Z_v3). VERDICT (confirmed failure_autopsy_V3-EXQ-460l_2026-06-23, interactive gate 'Confirm as recommended'): clean substrate_not_ready_requeue at readiness gate 3 (closure_exclusive_eval_did_not_arm_hold) -- ncl_hold_closure_armed_total=0 AND ncl_hold_reassert_total=0 on EVERY arm/seed; L0 fails to monopolise (mean per-commit hold ~1.2 vs floor 5.0); rho_peak_max=0. INDEPENDENTLY CONFIRMS the 460k diagnosis from a clean foraging eval (no contract-harness injection): the closure_exclusive_decommit_eval arm source _closure_commit_active is structurally gated on the F-driven e3._committed_trajectory, so the closure-coupled latch-hold does not arm in a real run and the JOB-2 DRIVER pair is UNEXERCISABLE. Narrow positive: gate 6 (delta_t negative variance) PASSED -- the JOB-1 signed-RPE delta_t the habenula reuses is live (n_neg_delta_ticks 834-1117, delta_t_min -0.42); the habenula INPUT works, only the hold it would abort is absent. NOT a falsification of any tagged claim (none exercised). Re-derive brake FIRED (MECH-445/446 5th lineage autopsy 460h..460l, threshold 2): routing /implement-substrate AMEND f_dominance_conversion_ceiling (decouple closure-coupled hold-arming from the F-driven e3._committed_trajectory so a hold arms+sustains independently of the F-dominated natural commit), REFUSE a V3-EXQ-460m same-claim re-queue. LOAD-BEARING REFRAME: on the foraging substrate no sustained monolithic hold forms at all, so the maintenance-RELEASE face is not even the exercisable constraint -- the binding constraint is upstream at commit-ENTRY / sustained-occupancy formation, i.e. the F-dominance selection face (MECH-439). NO claims.yaml status change -- MECH-090/MECH-342/MECH-445/MECH-446 stay candidate (MECH-445/446 v3_pending/pending_retest_after_substrate); ARC-108 stays substrate_conditional (no demotion, brake fresh: 0 prior autopsies). 460l manifest evidence_direction_note appended; 460l marked reviewed (reviewed_run_ids + discussed_experiment_dirs). GAP-4 stays in-progress. PROMOTES NOTHING. (session failure-autopsy-460l-20260623T0401Z)"
      governance_2026_06_22: "OWNER FRONTIER ADVANCED 460j -> 460k (session igb-gap4-reconcile-460k-owner-20260622T1530Z, /inter-governance-brief Step 1 plan-doc drift reconcile). The owner_exq lead prose still said 460j was 'now CLAIMED/running -- the LIVE owner', but governance_2026_06_21c already records 460j RAN terminal FAIL/non_contributory 2026-06-21 (clean substrate_not_ready_requeue, route_reason=off_baseline_not_sustained) and the rung-6 natural-commit-occupancy-release lever was PARKED (failure_autopsy_V3-EXQ-460j_2026-06-21): the latch-hold yields-to-closure-de-commit BY DESIGN and the active SD-034 closure control plane de-commits ~every tick on the foraging substrate, so no sustained occupancy ever forms for the rung-6 release to shorten. The named dissociable substrate -- a closure-exclusive de-commit eval mode (closure_exclusive_decommit_eval) where beta elevates only via _closure_commit_active so natural-commit occupancy is dissociable from closure-de-commit -- was then BUILT (ree-v3 main e52158d; substrate_queue f_dominance_conversion_ceiling fallback_ladder rung-6 PARKED->BUILT, build_record_460j). The 460-lineage successor V3-EXQ-460k was queued + ingested 2026-06-22 (ree-v3 main 979a943; experiments/v3_exq_460k_natural_commit_occupancy_release_decommit_falsifier.py; coordinator /queue/active confirmed via git reconcile): it ports 460j with closure_exclusive_decommit_eval=True on every arm and adds gate 2.5 (closure_exclusive_eval_armed) that self-routes substrate_not_ready_requeue if the eval mode does not arm the closure-coupled hold -- never a false MECH-445/446 weakening. owner_exq lead repointed 460j -> 460k with the 460j record preserved as [HISTORICAL]; resume_condition repointed to the 460k acceptance shape; last_updated bumped. NO claims.yaml status change -- SD-034 / MECH-445 / MECH-446 / MECH-090 / MECH-342 stay candidate (460k PROMOTES NOTHING until it scores; governance applies after the run). GAP-4 stays in-progress. (session igb-gap4-reconcile-460k-owner-20260622T1530Z)"
      governance_2026_06_21c: "V3-EXQ-460j RAN terminal FAIL/non_contributory 2026-06-21T11:55Z (manifest v3_exq_460j_natural_commit_occupancy_release_decommit_falsifier_20260621T115511Z_v3), AUTOPSIED + APPLIED this /governance cycle (governance-cycle-20260621T1215Z; confirmed failure_autopsy_V3-EXQ-460j_2026-06-21). The owner_exq 'now claimed/running' prose in governance_2026_06_21b is SUPERSEDED -- 460j has run. VERDICT (confirmed): clean substrate_not_ready_requeue self-route, route_reason=off_baseline_not_sustained -- the gate-3 sustained-hold redesign + the no-op-default natural_commit_latch_hold lever were BOTH armed in all arms (contact_non_vacuity 3/3, rule_bias_trained 2/3, closure_trigger_available 3/3) but the OFF (lever-disabled) baseline still does NOT sustain a natural-commit beta-latch occupancy (sustained_hold 0/3) -> the rung-6 release has nothing to shorten (lever_shortened_occupancy 0/3) and the de-commit DV never ran (coupling_nonvacuity 0/3, co_occurrence 0/3). ROOT CAUSE: the latch-hold yields-to-closure-de-commit BY DESIGN, and the active SD-034 closure control plane de-commits ~every tick on the foraging substrate (the 460i fragmentation), so the hold never establishes a sustained occupancy. NOT a weakens -- MECH-445/446 stay candidate / v3_pending / pending_retest_after_substrate (PROMOTES NOTHING). 8th iteration (460d->j); 3 consecutive autopsies (460h/i/j) with an EVOLVING shape -> granularity-debt / design-rethink flagged at the human gate (is the rung-6 natural-commit-occupancy-release lever testable on a closure-de-commit-active substrate?). NEXT substrate step (implement-substrate): narrow the latch-hold yield clause so it yields ONLY to a genuine closure fire, not the per-tick re-toggle, OR test on a regime where the closure de-commit is quieter. substrate_queue f_dominance_conversion_ceiling rung-6 amended with the 460j failure record. 460j marked reviewed. GAP-4 stays in-progress. (session governance-cycle-20260621T1215Z)"
      governance_2026_06_21b: "OWNER FRONTIER ADVANCED 460i -> 460j (session inter-governance-brief-20260621T074124Z, /inter-governance-brief Step 1 plan-doc drift reconcile). The 06:48Z /governance cycle (governance-cycle-20260621T0639Z) consumed confirmed failure_autopsy_V3-EXQ-460i_2026-06-21: V3-EXQ-460i RAN terminal FAIL/non_contributory (self-routed substrate_not_ready_requeue at readiness gate 3 -- the rung-6 lever was correctly armed but the 460h sustained ~2400-step monolithic natural-commit hold did NOT reproduce; the active SD-034 de-commit control-plane fragmented the beta latch to ~1-tick blips EVEN WITH THE LEVER OFF, so there was no sustained occupancy to shorten and the CO_OCCURRENCE DV never scored; non_degenerate=false). SUPERSEDED BY V3-EXQ-460j (NEW letter; gate-3 redesigned to a SUSTAINED-HOLD proxy + a no-op-default natural_commit_latch_hold substrate lever that re-asserts the beta latch each tick so the ARM_LEVER_OFF baseline sustains BY CONSTRUCTION; ree-v3 main f425f89, REE_assembly master bfaff24589; queued + ingested to the coordinator DB, machine_affinity ree-cloud-3, now claimed/running). owner_exq lead repointed 460i -> 460j with the 460i record preserved as [HISTORICAL]; last_updated bumped; resume_condition carries a revise-TODO marker for the session that scores 460j. NO claims.yaml status change -- SD-034 / MECH-445 / MECH-446 / MECH-090 / MECH-342 stay candidate (460j PROMOTES NOTHING until it scores; governance applies after the run). GAP-4 stays in-progress. (session inter-governance-brief-20260621T074124Z)"
      governance_2026_06_20b: "OWNER RECONCILE: 460i is now QUEUED + INGESTED (drop the stale 'GATED, not yet queued' framing). Session igb-gap4-reconcile-460i-queued-20260620T2032Z via /inter-governance-brief Step 1. V3-EXQ-460i -- the 460h-successor de-commit falsifier on the rung-6 graded natural-commit-occupancy-release lever -- was queued + ingested 2026-06-20 (ree-v3 main 21903a5; coordinator DB row pending + /queue/active confirmed; machine_affinity ree-cloud-3; the rung-6 lever NaturalCommitUrgencyRelease was BUILT ree-v3 main ab2c1a9 by the parallel implement-substrate-commit-duration-latch session, PARALLEL to the selection-face MECH-448 build). owner_exq opening clause + resume_condition updated to reflect 460i as the LIVE in-flight falsifier (advances/closes on its RESULT) with the pre-registered co-occurrence acceptance shape (MECH-445 commit-intent + MECH-446 within-arm post-closure occupancy drop on the SAME ARM_GAP_SCALED seed, >= 2/3 guard seeds, after all six readiness gates incl the new lever-shortened-occupancy non-vacuity gate); last_updated bumped. Snapshot/drift regenerated (derive-only). NO claims.yaml status change -- SD-034 / MECH-445 / MECH-446 / MECH-090 / MECH-342 stay candidate (460i PROMOTES NOTHING until it scores; governance applies after the run). GAP-4 stays in-progress. Parallel reconcile-arc107-689d (19:38Z) handled behavioral_diversity_isolation:GAP-I/GAP-J + biology_grounding_convergence_v4:BG-2 but did NOT touch this node; this closes that residual. (session igb-gap4-reconcile-460i-queued-20260620T2032Z)"
      governance_2026_06_19b: "OWNER REPOINTED 460g -> 460h after the granularity-debt decomposition + substrate amend landed (session gap4-repoint-460h-20260619T2130Z). The 7th-autopsy granularity-debt trigger recorded in governance_2026_06_19 has discharged in two steps. (1) DECOMPOSITION: /claim-synthesis (2026-06-19, applied REE_assembly master 6a35087fd6) split the coarse 'SD-034 ClosureOperator has behavioural de-commit authority over the MECH-090 beta latch' claim into a narrowed SD-034 umbrella + MECH-445 (closure->beta coupling ENGAGEMENT) + MECH-446 (de-commit-authority MAGNITUDE), both candidate / v3_pending / pending_retest_after_substrate -- the double dissociation (460f coupling-without-magnitude / 460g magnitude-without-measurable-coupling) is the separability proof. (2) SUBSTRATE AMEND: /implement-substrate landed the de-commit-authority deliverable (ree-v3 main 167b3b7; recorded in substrate_queue commitment-closure-control-plane implementation_log + docs/architecture/sd_034_governance_closure_operator.md): BetaGate.note_closure_commit_intent + sd034_n_closure_commit_intent -- a REFRACTORY-INDEPENDENT closure-coupling commit-intent counter that decouples the MECH-446 magnitude lever from the MECH-445 coupling-engagement non-vacuity metric, directly resolving the 460g S5 self-defeat where the committed-run-scaled refractory pinned at the 60-tick cap and suppressed sd034_n_closure_coupled_elevations 36->0. V3-EXQ-460h QUEUED (ree-v3 main b46c777, supersedes 460g, ingested in the coordinator DB): same magnitude lever + within-arm around-closure C2 occupancy-delta DV, non-vacuity gated on sd034_n_closure_commit_intent>0; claim_ids=[MECH-446 scored, MECH-445 precondition]. owner_exq advanced 460g -> 460h; resume_condition repointed to the 460h PASS criterion. NO claims.yaml status change (governance applies after the 460h run; SD-034 / MECH-445 / MECH-446 / MECH-260 / MECH-261 unchanged). 468f still separately owed. GAP-4 stays in-progress. (session gap4-repoint-460h-20260619T2130Z)"
      governance_2026_06_19: "V3-EXQ-460g RAN terminal FAIL/non_contributory 2026-06-19T18:57Z (supersedes 460f; manifest v3_exq_460g_sd034_closure_control_plane_decommit_magnitude_20260619T185744Z_v3), AUTOPSIED + APPLIED this /governance cycle (consumed confirmed failure_autopsy_V3-EXQ-460g_2026-06-19, the parallel autopsy session wrote the artifact; governance applied its recommendations). 460g implemented the 460f-autopsy-prescribed de-commit MAGNITUDE lever (committed-run-scaled Leg-B refractory, ree-v3 main 2cd0aa2) + a PAIRED within-ON-arm around-closure C2 occupancy-delta DV. VERDICT (confirmed): the magnitude lever + the 460f-prescribed tightened coupling non-vacuity gate are SELF-DEFEATING -- the scaled refractory pins at the 60-tick cap on ~530-560-step runs and BetaGate.elevate() is a no-op while the refractory is active, so the closure-coupled re-elevations the gate counts can never fire (sd034_n_closure_coupled_elevations 36->0 seed42, 0/3; closure_coupling_nonvacuous 0/3, within_arm_window_nonvacuous 1/3). The de-commit refractory HAS authority (seed-42 within-arm occupancy 0.333->0.0, C2 PASS) but suppresses its own coupling certifier -> the self-route substrate_not_ready_requeue is correct + conservative (NO false weakens). APPLIED: SD-034 -> non_contributory + pending_retest; MECH-261 -> non_contributory (closures all hook-driven, n_automatic_fires=0, mode-conditioning bypassed -- protect the stable claim); MECH-260 -> supports (No-Go nogo_installed>=1 3/3, narrow non-promoting positive); claims.yaml notes appended; substrate_queue commitment-closure-control-plane failure_record += 460g; 460f -> superseded; 460g marked reviewed. 7th SD-034-lineage autopsy; the 460f granularity-debt WATCH ITEM trigger FIRED -> route /claim-synthesis (primary) + a 460h re-queue with a refractory-independent commit-intent coupling counter (secondary). owner_exq advanced 460f->460g; 468f still owed. GAP-4 stays in-progress. (session governance-cycle-20260619T2013Z)"
      governance_2026_06_12: "LIVE BLOCKER LIFTED + *c COHORT QUEUED. The scaffolded_sd054_onboarding readiness gate (the 2026-06-10 LIVE BLOCKER) PASSED 2026-06-11 (V3-EXQ-603n; substrate_queue.scaffolded_sd054_onboarding.ready flipped true: corrected G0 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the ecological 0.4, all four legs >=2/3 seeds, non-vacuity met). The full Phase 4/5 OCD behavioural cohort was REWIRED + QUEUED 2026-06-12 via /queue-experiment at priority 230 (ree-v3 main 605fa29 [468c] + 1eed1d3 [460c/461c/464c/466c/467c] + de9c564 [629b]; umbrella 5e392ba): 468c (SD-034/MECH-268/MECH-090 commitment-vs-contradiction; PILOT, claimed/running ree-cloud-3), 460c (SD-034/MECH-260/MECH-261 verified-but-not-released), 461c (MECH-090/SD-033a/SD-034 delayed-reward persistence), 464c (MECH-266/SD-032a competing goals), 466c (SD-034/MECH-094 satisficing residue discharge), 467c (MECH-266/SD-032a mode stickiness dose-response), 629b (MECH-342 ecological maintenance-release). 463b EXCLUDED (lone PASS, measured directly not closure-gated). Each rewires the TRAINING harness from committed_mode_curriculum (trains commitment but NOT foraging competence -> the *b cohort self-scored n_closures/n_windows/n_switches/contradictions=0) to the FULL scaffolded_sd054_onboarding curriculum at the 603n config (the 514n pattern), the substrate the readiness flip made ready. KEY FINDING (pilot-surfaced, recorded for the audit trail): the *b cohort's contradictions=0/n_switches=0 was PARTLY A WIRING GAP, not only the foraging-competence ceiling -- 468b never set subgoal_mode=True, so BOTH GAP-3 waypoint-completion paths AND the counter_evidence injection gate (causal_grid_world 1664/1740/2067 hard-require subgoal_mode) were INERT; the *c env builders set it. The MECH-266 arms (464c/467c) use the GAP-3 dual_cue primitive + SalienceCoordinator hysteresis rails with use_closure_operator OFF (closure injects a confounding closure_event mode-switch signal). 629b ADDITIONALLY needed the failure_autopsy_V3-EXQ-629_2026-06-03 score_margin_floor recalibration on top of the curriculum: a 629b probe measured ecological per-candidate score margins mean ~0.006 / max ~0.02 / frac>=0.05==0 (the same NO_NATURAL_COMMITMENT precondition 629 hit -- the legacy 0.05 MECH-090 admission floor rejected every elevation), so the admission + MR score-margin floors were recalibrated to 0.001 (beta now elevates) AND the inert degradation driver was wired via the env mech090_readiness_outcome source (scheduled_limb_damage -> 1-mean(limb_damage) -> nav EMA below MR_NAV_FLOOR; reduced degraded-window hazards so the limb-impaired agent survives to be released); seed-44 probe showed the full discriminating signal (ARM_1 betaocc 0.30/fires 1/decommit 4 vs ARM_0 betaocc 1.00/fires 0). EVERY *c member + 629b carries TWO non-vacuity gates (603n contact guard + a mechanism-specific gate: commitment/completion/Hold-window/mode-switching engaged) that self-route substrate_not_ready_requeue (non_contributory) below floor -- NEVER a false weakens (the V3-EXQ-643/514n same-precondition lesson). NO claims.yaml change this cycle: SD-034/MECH-266/MECH-267/MECH-268/MECH-090/MECH-342 stay as-is; the cohort has NOT run yet (governance applies supports/weakens when the manifests land). GAP-4 stays in-progress; closes when the *c cohort + 629b PASS (subject to the MECH-342 v3_pending gate). (session governance-gap4-node-refresh-20260612T0547Z)"
      governance_2026_06_12b: "*c COHORT WALKED (PM /governance cycle 2026-06-12T22:16Z). The cohort ran. TWO members adjudicated this cycle via confirmed failure_autopsy_SD-034-closure-cluster_2026-06-12 (user-confirmed 'Apply as recommended'): V3-EXQ-460c (n_closures=0 on 3/3 seeds -- env sequence_complete not routed into ClosureOperator.emit_closure(); rule_bias_head untrained) + V3-EXQ-468c (closure-coupled release fires MORE near contradiction, C1 PASS, but no de-commitment hold -> committed_frac DV cap-pinned) reclassified non_contributory + substrate_ceiling + pending_retest; manifests + claims.yaml (SD-034/MECH-260) noted; reviewed. The substrate_not_ready branch of the 06-12 resume_condition fired -- NOT a false weakens. The other FIVE members (461c MECH-090/SD-033a/SD-034; 464c+467c MECH-266/SD-032a; 466c SD-034/MECH-094; 629b MECH-342) LANDED and self-route residual_*_open/weakens (629b non_contributory) but were FLAGGED for a /failure-autopsy CLUSTER EXTENSION and LEFT PENDING (no inline evidence stamp, not reviewed) -- the cohort siblings the SD-034 cluster autopsy named to fold in as they arrived. SD-034 + MECH-266 provisional->candidate demotions HELD this cycle (conflict ratios inflated by the pending cohort, not falsifications). New substrate task 'commitment-closure-control-plane' created in substrate_queue (route env sequence_complete -> emit_closure + de-commit hold + train rule_bias_head; both *c failure records). GAP-4 stays in-progress: closes when the rewired behavioural arm (post-/implement-substrate) returns a contributory PASS. (session governance-cycle-20260612T2216Z)"
      governance_2026_06_10: "AUDIT RECONCILE (read-only audit confirmed node accurate; two frontmatter-drift fixes applied, no experiment action). (1) The 629 leg never got folded into GAP-4 gating after it FAILed: governance_2026_06_02b asserted GAP-4 is gated on '629 PASS', but V3-EXQ-629 (MECH-342 ecological) RAN 2026-06-02T22:58Z and FAILed non_contributory, epistemic_category=measurement_test_design_defect (NO_NATURAL_COMMITMENT: mean_score_margin ~0.00074, ~70x below the MECH-090 admission floor 0.05, so R-c admission AND never fires and there is no beta latch for MECH-342 to release; degradation driver also inert). NOT a MECH-342 falsification -- claim_ids=[], zero claim weight; MECH-342 stays candidate/v3_pending, ecological validation BLOCKED. failure_autopsy_V3-EXQ-629_2026-06-03.{md,json} routes a 629b redesign (recalibrate score_margin_floor to the ecological decisiveness distribution OR commitment-inducing curriculum + wire the inert degradation driver). 629b is OWED but NOT YET QUEUED and is NOT substrate-ready -- it shares the SAME no-natural-commitment precondition as the *b cohort (the scaffolded_sd054 / E3 score-margin-decisiveness ceiling; cross-link MECH-341 E3 score-diversity watch item). (2) Audit re-confirmed the full *b cohort: all 7 members RAN; 6/7 non_contributory/substrate_ceiling/pending_retest (substrate-not-engaged: n_closures/n_switches/n_windows=0), 463b is the lone PASS/supports (MECH-268 dACC saturation, measured directly not closure-gated). MECH-090 behavioural commit-entry conjunction (461b+468b) is therefore still owed -- both landed non_contributory because beta never releases. GAP-4 remains in-progress; both the *b re-runs AND 629b are gated on the same live scaffolded_sd054_onboarding goal-completion ceiling, still FAILING as of 2026-06-10 (V3-EXQ-603m FAIL 2026-06-10T13:38Z; 603n in-flight). (session gap4-frontmatter-reconcile-20260610T1702Z)"
      governance_2026_06_04: "Phase 4/5 OCD behavioural *b cohort (460b/461b/464b/466b/467b/468b) ALL RAN and were ALL reclassified non_contributory + substrate_ceiling + pending_retest_after_substrate by /governance 2026-06-04 (confirmed failure_autopsy_V3-EXQ-460b-461b-464b-466b_2026-06-04, extended to fold in 467b/468b). ONE substrate-not-engaged cluster: in the live committed_mode_curriculum loop the agent commits (beta latch engages) but never tolerance-completes a waypoint / never switches mode / never hits a contradiction, so n_closures=0 / beta_release=0 / n_switches=0 / n_windows=0 / contradictions=0 in EVERY arm including the forced-RV positive controls. The cohort did NOT close GAP-4 (they cannot, until goal completions occur). GAP-4 does NOT close on this cohort; it now blocks on the SAME goal-achievement/foraging-competence ceiling as the 603e/626a/634/634b cluster -- scaffolded_sd054_onboarding (V3-EXQ-634c seeding-calibration validation pending; ready=false). All 6 failure_records + 8 unblocks_claims added to that substrate_queue entry. RESUME: re-queue the *b cohort once scaffolded_sd054_onboarding delivers runtime goal completions. EXCEPTION: the contemporaneous V3-EXQ-463b (dACC saturation, measured directly not closure-gated) PASSED and genuinely supports MECH-268."
      governance_2026_06_02: "SUBSTRATE SIDE OF GAP-4 RESOLVED via the V3-EXQ-592d->592e->592f->592g chain (disposition LANDED REE_assembly master 01144f9bf6, 2026-06-02T17:57Z). Chain: (1) 592e (C1-baseline fix attempt, force-uncommitted P2 entry) FAILed does_not_support 2026-06-01T18:09Z. (2) 592f (controlled state-machine probe, supersedes 592e; forced score_margin=0.01 < floor 0.05 + nav_readiness=0.0 < floor 0.3 while beta forced elevated + E3 committed pointer forced present) produced ZERO state-occupancy suppression and ZERO decommit transitions -- tag FAIL_NO_RELEASE_AUTHORITY. Combined with the B3b release-path audit (all 4 candidate release pathways = NO; commits e00c8e0f96 + b20ea959b8), this surfaced the real finding: MECH-090 governs commit ENTRY soundly but carries NO release/decommit authority -- that capability was simply absent from the substrate. (3) The gap spawned MECH-342 (maintenance-time release substrate). (4) 592g (MECH-342 maintenance-release validation probe) PASSED all six criteria 2026-06-02T16:35Z: with MECH-342 ENABLED, degraded execution readiness under elevated beta now yields >=1 decommit transition per fail stage (the quantity 592f measured as zero), suppression 0.4-0.6, mech342_fires 1/stage, C4 conjunction strictly-positive 0.6 (592f passed C4 only vacuously at 0), no false abort in A/E. Governance outcome: MECH-090 unchanged (active); its pending_retest_after_substrate cleared (reach gap closed) -- the release capability now lives on MECH-342. MECH-342 registered candidate/v3_pending (592g is a diagnostic state-machine probe, NOT ecological evidence; the V3-pending gate forbids promotion). 592f re-tagged does_not_support -> non_contributory (epistemic_category substrate_ceiling). substrate_queue MECH-342 -> implemented_validated_v3_exq_592g. REMAINING GAP-4 WORK (status stays in-progress): (a) MECH-342 ecological/behavioural evidence to clear v3_pending -- LANDED as V3-EXQ-629 (queued 2026-06-02T18:08Z, ree-v3 e9a0b87; see governance_2026_06_02b). NOTE: the next-wave session's pre-allocated V3-EXQ-631 is a PHANTOM -- NEVER MINTED, and specifically NOT deferred work owed to this node: no queue entry current or historical, no script, no manifest (established by governance_2026_07_21 below; re-verified 2026-08-15). It was a duplicate id for the experiment that actually ran as V3-EXQ-629. Do NOT queue it and do NOT read it as an owed successor -- the 629/629b lineage is the actual ecological evidence run; (b) the Phase 4/5 OCD behavioural *b cohort (460b, 461 full, 463b, 464b, 466b, 467b, 468b) is STILL UNQUEUED -- next action is /queue-experiment for that cohort on env extensions (GAP-3) + committed_mode_curriculum (GAP-11), both already done. GAP-4 closes when the *b cohort PASSes."
      governance_2026_06_02b: "MECH-342 ecological evidence run LANDED: V3-EXQ-629 (v3_exq_629_mech342_ecological_maintenance_release_evidence) queued via /queue-experiment 2026-06-02T18:08Z (ree-v3 main e9a0b87, pushed origin/main; umbrella 0fae1c1). This is the ecological evidence-grade complement the 2026-06-02 disposition required -- 592g is experiment_purpose=diagnostic (stubs E3.select, forces committed state); 629 uses a REAL REEAgent in a REAL CausalGridWorldV2 with natural commitment (E3.select not stubbed, R-c-gated entry via committed_mode_curriculum P0 warmup) and natural mid-commitment readiness degradation (SD-047 multi_source_dynamics raises E2 world-forward error -> running_variance -> nav_competence proxy drop + score-margin compression). Arm axis = use_maintenance_release ON vs OFF (commit-entry gating identical). Two P2 windows: HEALTHY (no false abort) + DEGRADED (decommit + mech342 fires + occupancy < OFF, which reproduces the 592f gap). Acceptance C1 baseline-commits / C2 degradation-occurred (INVALID_HARNESS->non_contributory guard, NOT a FAIL) / C3 release-authority / C4 no-false-abort / C5 distinct-from (use_harm_stream=False => MECH-091 inert; V_s release OFF; ghost-goal OFF; ARC-028 completion-release shared across arms cannot explain ON-vs-OFF delta). Predecessor V3-EXQ-592g, NOT supersedes. owner_exq advanced 592g -> 629. CORRECTION: the governance_2026_06_02 note above named V3-EXQ-631 as the ecological follow-on; that id is a PHANTOM -- NEVER MINTED (no queue entry current or historical, no script, no manifest), not deferred work owed to this node, and not to be queued. The concurrent next-wave session held it pending IGW-024 + this governance flag and then never minted it; 629 is the actual run. See governance_2026_07_21 for the full provenance check. priority=270, machine_affinity=any, seeds=3, conditions=2, est 240min. ID bumped from 628 (a concurrent MECH-319 session committed b7fae0a on 628 mid-flight). GAP-4 stays in-progress: still gated on (a) 629 PASS (clears MECH-342 v3_pending evidence side, subject to the V3-pending gate) AND (b) the unqueued Phase 4/5 OCD behavioural *b cohort. (session plan-gap4-drift-629-update-20260602T181126Z)"
      governance_2026_06_03: "Phase 4/5 OCD behavioural *b cohort QUEUED via /queue-experiment (ree-v3 main a5afed7, pushed origin/main 2026-06-03T~20:24Z). Seven entries: V3-EXQ-460b (SD-034 verified-but-not-released), 461b (MECH-090+SD-033a+SD-034 delayed-reward persistence, FULL behavioural -- newly authored; new letter because bare 461 was a substrate-readiness diagnostic superseded by the GAP-11 pilot V3-EXQ-592), 463b (MECH-268 dACC conflict saturation, 500-step), 464b (MECH-266 competing goals / switch-cost asymmetry -- newly authored; bare 464 already ran), 466b (SD-034 satisficing/residue discharge), 467b (MECH-266 mode stickiness dose-response), 468b (SD-034+MECH-268+MECH-090 commitment vs contradiction). 460b/463b/466b/467b/468b were staged-not-queued (authored by a prior session, never queued/run -- confirmed absent from runner_status); 461b/464b authored this session on the 460b/467b behavioural templates. All seven run on the GAP-3 CausalGridWorldV2 env extensions (tolerance-band completion; dual-cue for 464b/467b via SD-049) + the GAP-11 committed_mode_curriculum (P0 warmup -> P1 consolidation -> P2 eval) with the O-2 forced-rv mandatory contrast. All smoke-tested (exit 0, wiring confirmed) + pass the emit_outcome AST contract + ASCII-clean. priority=290, machine_affinity=any, seeds=3. Substrate prereqs confirmed resolved before queuing: MECH-090 active, MECH-342 validated by 592g, GAP-3 env + GAP-11 curriculum landed. Queue-write serialized behind concurrent claims gap7-l1-626b (626b) + gap8-sd033b-485bc (485b/c) per user direction; 626b preserved in the same queue commit. GAP-4 stays in-progress: closes when the *b cohort PASSes (plus 629 PASS clears MECH-342 v3_pending evidence side). (session gap4-ocd-behavioural-cohort-20260603T175250Z)"
      governance_2026_06_13: "*c COHORT + *d VALIDATION WALKED (AM /governance 2026-06-13T08:58Z). (1) The 5 remaining *c cohort siblings (461c MECH-090/SD-033a/SD-034; 466c SD-034/MECH-094; 464c+467c MECH-266/SD-032a; 629b MECH-342) -- the PM-cycle pending set -- were ADJUDICATED via confirmed failure_autopsy_SD-034-closure-cluster-ext_2026-06-12 (user 'Apply but discuss mode-gov entry'): ALL non_contributory, NONE falsify. Splits 3 ways: A closure-plane (461c/466c, amend commitment-closure-control-plane), B mode-governance (464c/467c -> NEW substrate_queue entry mode-governance-engagement, priority 1 per user; external_task occupancy never driven, n_switches==n_episodes vacuous gate), C readiness (629b, amend scaffolded_sd054_onboarding; MECH-342 FIRED on the 1 competent seed = narrow_supports). Manifests weakens->non_contributory + pending_retest; reviewed. (2) The closure-control-plane substrate that LANDED 2026-06-12 was validated by V3-EXQ-460d (supersedes 460c) + V3-EXQ-468d (supersedes 468c). 460d: C1_n_closures PASS -- closure NOW FIRES on the env-completion hook (the *c n_closures=0 gap is CLOSED; MECH-260 supports), but C2_beta_release/C4 FAIL (de-commit behavioural authority residual; Leg C trained rule_bias_head still experiment-side). 468d: precondition_unmet (contradiction injection 1/3 seeds). BOTH routed to /failure-autopsy this cycle (no evidence_direction, LEFT PENDING). (3) SD-034 + MECH-266 provisional->candidate demotions HELD again (user 'Hold both'; ratios inflated by the now-excluded cohort FAILs). owner_exq advanced 468c/460c -> 460d/468d frontier. GAP-4 STAYS in-progress (Case 3): closes when the residual de-commit leg (460d C2/C4) is resolved (autopsy -> /implement-substrate Leg C: train rule_bias_head + non-cap-pinned DV) and a contributory PASS lands. (session governance-cycle-20260613T0858Z)"
      governance_2026_06_16: "LEG C BUILT + V3-EXQ-460e QUEUED (session implement-substrate-leg-c-gap4-20260616T1940Z). The confirmed failure_autopsy_SD-034-closure-control-plane-d_2026-06-13 route discharged: the 460d residual was the LITERAL 'Leg C not built' -- both 460d/468d set lateral_pfc_train_rule_bias_head=True but NEVER added the head to any optimizer (grep optim|Adam|.backward = ZERO matches), so the rule_state carried no task-shaped magnitude and the closure-coupled de-commit had no net authority over the MECH-090 latch (460d C2_beta_release/C4 FAIL: ON occupancy >= OFF on seeds 43/44). /implement-substrate landed Leg C as a scaffold-harness training leg: scaffold_train_rule_bias_head trains agent.lateral_pfc.bias_head_parameters() during scaffolded_sd054_onboarding P1 via the V3-EXQ-598b outcome-coupled E3-gradient REINFORCE pattern (mirrors scaffold_train_harm_pathway; no-op default, bit-identical OFF; ree_core untouched). ree-v3 3ccc48a (script+contracts+CLAUDE.md); REE_assembly 2f360c270a (sd_034 design-doc Leg C amend + claims.yaml SD-034 implementation_note_2026_06_16 [substrate-only, NO status flip] + substrate_queue commitment-closure-control-plane implementation_log + substrate_dependencies landing mechanism_changing=false). 109/109 scaffolded contracts (102 prior + 7 new C17, incl the REINFORCE-gradient-reaches-the-head load-bearing contract) + 7/7 preflight; smoke: head trains max|dW| 0.0015>0 + mean |bias| 0.039 ON / dW=0 exactly OFF. V3-EXQ-460e QUEUED via /queue-experiment (ree-v3 main f0fbbf6, coordinator DB /queue/active CONFIRMED present; supersedes 460d; priority 325, machine any, 3 seeds, est 190min): enables scaffold_train_rule_bias_head + reads de-commit on a NON-CAP-PINNED ON<OFF beta-latch-occupancy drop (replaces 460d count-C2 + cap-pinned C4); FOUR readiness gates self-route substrate_not_ready_requeue (contact / rule_bias-head-trained [mean |bias| > floor -- the direct anti-460d-bug gate] / beta-engagement-both-arms [the 468d commit-without-beta guard] / closure-trigger), NEVER a false weakens. NO claims.yaml status flip: SD-034 stays provisional / pending_retest_after_substrate; MECH-260/MECH-261/MECH-090/MECH-268 unchanged. GAP-4 STAYS in-progress: closes when 460e returns a contributory PASS (ON<OFF de-commit on the non-cap-pinned DV >=2/3 seeds with all readiness gates met). 468e (MECH-090 commit-entry conjunction, the 468d successor) is OWED but not yet queued -- its prerequisite (the trained head) is now built; separate session. GAP-4 is independent of the GAP-A choke. (session implement-substrate-leg-c-gap4-20260616T1940Z)"
      governance_2026_06_17: "V3-EXQ-460e RAN + AUTOPSIED (session failure-autopsy-460e-apply-20260617T1457Z; analysis committed fb9fc52bc4 by a parallel autopsy instance, ADOPTED after independent code-verification of the central claim). 460e ran terminal FAIL/non_contributory on ree-cloud-1 (manifest v3_exq_460e_..._20260617T085103Z_v3; coordinator DB completed). VERDICT (confirmed failure_autopsy_V3-EXQ-460e_2026-06-17): Leg C WORKS -- rule_bias_head_trained 1.0 3/3 + closure_trigger_available 5-7 closures 3/3 (the two 460d-failing gates now PASS); self-routed substrate_not_ready_requeue on the THIRD readiness gate beta_engagement_both_arms (1/3 < 2/3) BEFORE the load-bearing C2 de-commit DV ran. CODE-CONFIRMED commit-without-beta dissociation: 460e config sets ONLY beta_gate_bistable=True (both MECH-090 R-c gates OFF), so the bistable latch elevates iff E3 result.committed (running_variance < commit_threshold; agent.py:5843-5859) -- a decisive natural commit-entry firing on 1/3 seeds; the closure control-plane sets committed_trajectory + fires closures independently (seeds 42/43 committed_steps 2415/2019 but total_beta_elevated 0). The trained head biases per-candidate SCORING not commit-entry decisiveness -> cannot rescue engagement (inverse tell: seeds 42/43 saturated rule_bias at the 0.10 clamp rail yet beta failed; seed 44 at 0.020 engaged). Seed 44 = positive existence proof: beta engaged both arms, C2 PASSED (ON mean_beta_elevated 11.73 < OFF 14.87, non-cap-pinned) -> the de-commit DV is SOUND; the gap is engagement, not measurement. NOT a falsification (claims never exercised -- do not weaken); NOT granularity debt (signatures advance link-by-link Leg-A -> Leg-C-unbuilt -> beta-engagement, pre-registered by failure_autopsy_SD-034-closure-control-plane-d_2026-06-13 line 90 -> no /claim-synthesis). APPLIED THIS SESSION: substrate_queue commitment-closure-control-plane amended (5th failure_record + beta-engagement deliverable mechanisms a/b appended; ready stays false, status amend_implemented_pending_validation); claims.yaml SD-034/MECH-260/MECH-261 evidence_quality_note + pending_retest_after_substrate=true (NO status/confidence change -- user-confirmed); 460e marked reviewed. 460f + 468e HELD until the beta-engagement amend lands (re-queuing now re-derives the precondition miss -- 654d/654e anti-pattern; user-confirmed). GAP-4 STAYS in-progress. (session failure-autopsy-460e-apply-20260617T1457Z)"
      governance_2026_06_18: "V3-EXQ-460f RAN + AUTOPSIED (session plan-reconcile-gap4-460f-20260618T0611Z adopting the failure-autopsy-460f-20260618T0549Z artifact; confirmed failure_autopsy_V3-EXQ-460f_2026-06-18, user-confirmed interactive gate). The beta-engagement amend WORKED -- all four readiness gates cleared (the 460e blocker beta_engagement_both_arms now 1.0), so the load-bearing C2 de-commit occupancy-drop DV RAN for the first time: PASS 1/3 (seed 42 ON 23.73 < OFF 35.67 -33.5%), FAIL 43/44. VERDICT: substrate/measurement gap, NOT a falsification. The amend's coupling diagnostic sd034_n_closure_coupled_elevations fired 36/52 on seed 42 but 0/0 on seeds 43/44 -- on strong-natural-commit seeds result.committed always co-occurred with the closure-plane commit so the coupling was inert and the DV reduced to the bare Leg-B 5-tick refractory, whose magnitude (~20-35 tick-blocks) is swamped by ~530-560 natural-commit elevated steps; the between-arm unpaired DV is underpowered. Seed 42 + 460e seed 44 (ON 11.73 < OFF 14.87) are existence proofs of the correct sign -> residual gap = de-commit-authority MAGNITUDE + DV POWER. claim_ids FIX: the self-stamped MECH-261 weakens is MIS-ATTRIBUTED -- all closures hook-driven (n_automatic_fires=0), the Leg-A env-completion hook bypassed the MECH-261 mode-conditioning predicate (run does not exercise it; protect the stable claim, exp_conf 0.724). USER-CONFIRMED disposition (governance APPLIES; NOT applied here): SD-034 -> non_contributory; MECH-261 -> non_contributory; MECH-260 -> supports (No-Go nogo_installed >= 1 on 3/3, narrow positive); all three pending_retest_after_substrate; epistemic_category substrate_ceiling. Recurrence: link-by-link (Leg-A hook -> Leg-C trained head -> beta-engagement -> de-commit magnitude), NOT granularity debt (consistent with the 460e autopsy) -- but 460g FLAGGED as the tip-point. owner_exq advanced 460e -> 460f. NEXT: /implement-substrate amend commitment-closure-control-plane (de-commit-authority-magnitude lever + within-arm around-closure C2 DV) -> re-issue 460g; 468e separately owed. The stale gap8-sd033b-485g claim holding this plan doc (~15h, claimed 2026-06-17T14:59Z) was cleared (user-confirmed). Artifacts failure_autopsy_V3-EXQ-460f_2026-06-18.{md,json} (REE_assembly master 003d634f54). NO claims.yaml / substrate_queue change this session (analysis + handoff). GAP-4 STAYS in-progress. (session plan-reconcile-gap4-460f-20260618T0611Z)"
      governance_2026_06_18b: "V3-EXQ-468e RAN + AUTOPSIED (session failure-autopsy-468e-20260618T1445Z; confirmed failure_autopsy_V3-EXQ-468e_2026-06-18, user agreed with all four findings + requested this node repoint). 468e is the PERSEVERATION-SIDE sibling owed by the 460e autopsy (the other owed successor, 460f, was autopsied earlier 2026-06-18). It ran terminal FAIL/non_contributory (supersedes 468d; manifest v3_exq_468e_..._20260618T060133Z_v3; coordinator DB completed 06:01:37Z). VERDICT: the beta-engagement amend ENGAGED THE SUBSTRATE FAIRLY -- both non-vacuity gates cleared (foraging-contact 1.0; commitment-non-vacuity 1.0 -- ON arm committed AND a contradiction fired 3/3), so C1/C2 drove a verdict. C1 (beta_release_near_contradiction) PASSED 3/3 with ON>OFF (43/16/58 vs 14/10/0) -- the MECH-268 dACC-saturation -> beta-release pathway works PROXIMALLY. C2 (committed_frac_post_absolute ON < OFF) FAILED 3/3 because the ON-arm post-contradiction committed fraction is PINNED AT THE 1.0 CEILING on every seed: the agent stays fully committed through the whole post-contradiction window despite the release (seed-44 ON=1.0 vs OFF=0.0 is a non-commit artifact, NOT de-commit). SAME STRUCTURAL PROPERTY AS 460f via an independent DV: the de-commit/release fires with correct sign but SUB-THRESHOLD AUTHORITY MAGNITUDE; and the absolute committed-fraction DV RE-PINNED at the ceiling (the 468c->468e cap-pin escape moved 0.85->1.0 but did not lift). claim_ids FIX: the self-stamped MECH-090 weakens is MIS-ATTRIBUTED -- script line 857 ties MECH-090 to the C2-gated overall PASS, but the run tests MECH-090's latch RELEASE via C1, which PASSED 3/3; MECH-090 is ACTIVE -- do not weaken on a downstream-authority fail (mirror of the 460f MECH-261 correction; EXQ-048/MECH-057b class). USER-CONFIRMED disposition (governance APPLIES; NOT applied here): SD-034 -> non_contributory; MECH-090 -> non_contributory (C1 release recorded as a narrow non-scoring positive); MECH-268 -> supports (C1 3/3, narrow positive); SD-034 + MECH-090 pending_retest_after_substrate; epistemic_category substrate_ceiling. Recurrence: 468e CONFIRMS the 460f structural property via a second independent DV -- NOT a structurally-new signature, NOT granularity debt (consistent with the 460e/460f autopsies) -- but the tip-point HARDENS: two DVs now fail at the same authority gap; if the post-amend retests 460g/468f still fail with a structurally-different signature, route the SD-034 closure cluster to /claim-synthesis. NEXT: /implement-substrate amend commitment-closure-control-plane (shared de-commit-authority-magnitude lever + a GRADED within-arm post-contradiction de-commit DV replacing the 1.0-saturated committed_frac_post_absolute) -> re-issue 468f alongside 460g. Artifacts failure_autopsy_V3-EXQ-468e_2026-06-18.{md,json}. NO claims.yaml / substrate_queue change this session (analysis + handoff). owner_exq advanced to record both 460f + 468e run+adjudicated. GAP-4 STAYS in-progress. (session failure-autopsy-468e-20260618T1445Z)"
      resume_condition: "Advances/closes on the V3-EXQ-460k RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943, coordinator /queue/active via git reconcile, machine_affinity any; supersedes V3-EXQ-460j, which RAN terminal FAIL/non_contributory 2026-06-21 self-routing substrate_not_ready_requeue route_reason=off_baseline_not_sustained, then PARKED + the named dissociable substrate BUILT) NOW RETESTED ON THE BUILT closure-exclusive de-commit eval substrate (closure_exclusive_decommit_eval=True on every arm, ree-v3 main e52158d -- beta elevates only via _closure_commit_active so the natural-commit latch occupancy is dissociable from the SD-034 closure de-commit, dissolving the 460j off_baseline_not_sustained root cause), with a NEW gate 2.5 (closure_exclusive_eval_armed: ncl_hold_closure_armed_total>0 AND ncl_hold_reassert_total>0 on ARM_LEVER_OFF >= 2/3) that self-routes substrate_not_ready_requeue if the eval mode does not arm the closure-coupled hold -- NEVER a false MECH-445/446 weakening. The rung-6 COMMIT/RELEASE-DURATION lever = the graded natural-commit-occupancy release (NaturalCommitUrgencyRelease, ree_core/policy/natural_commit_urgency.py, BUILT ree-v3 main ab2c1a9 2026-06-20), NOT a re-queue on the current selector. The rung-6 lever shortens the F-driven natural-commit latch occupancy (~2400-2600 steps on strong seeds) so weak-natural-commit becomes the norm ACROSS seeds, dissolving the 460h disjoint-certifier problem (the selection-face levers conflict-graded-k + gap-scaled commit-T; MECH-439, do NOT shorten latch occupancy -- this is the duration FACE of the F-dominance conversion ceiling, root C reclassified from open/orthogonal 2026-06-20; conversion_ceiling_phase0_synthesis_2026-06-18 + GAP-I). PRE-REGISTERED ACCEPTANCE (verbatim shape in the v3_exq_460i docstring + substrate_queue f_dominance_conversion_ceiling rung-6 implementation_log.falsifier_next; MECH-446 scored, MECH-445 precondition): on ARM_GAP_SCALED, per guard seed, sd034_n_closure_commit_intent>0 (MECH-445 commit-intent) AND the within-arm around-closure occupancy DROP (mean post-closure occupancy < mean pre-closure with a >= DECOMMIT_MIN_DROP_FRAC relative drop over >= C2_MIN_WINDOW_EVENTS windows; MECH-446) BOTH hold on the SAME seed -> overall PASS = co-occurrence on >= 2/3 guard seeds, scored ONLY after all SIX readiness/non-vacuity gates clear (incl the rung-6 lever-shortened-occupancy gate: ARM_GAP_SCALED ncur_n_releases_total>0 AND mean beta-latch occupancy dropped vs ARM_LEVER_OFF). On the post-run 460k manifest /governance walk: (PASS -- co-occurrence on >= 2/3 guard seeds, after gate 2.5 closure_exclusive_eval_armed clears) -> apply supports to MECH-445 + MECH-446, clear pending_retest, close GAP-4 (subject to 468f); (readiness met but a fairly-tested no-drop -- occupancy drop unmet on coupling-certified seeds) -> GENUINE weakens on MECH-446, route /failure-autopsy; (non-vacuity unmet, incl gate 2.5 closure-coupled hold not armed) -> substrate_not_ready_requeue, NEVER a false weakens. 460h (predecessor, RAN terminal FAIL/non_contributory 2026-06-20, confirmed failure_autopsy_V3-EXQ-460h_2026-06-20, applied by autopsy-apply-460h-20260620T0843Z; supersedes 460g): the refractory-independent commit-intent fix WORKED (seed-44 sd034_n_closure_commit_intent=375 where 460g collapsed 36->0, closing the S5 self-defeat) but the MECH-445 (commit-intent; fires where the F-driven natural commit is WEAK -- seed 44, OFF committed_steps=0) and MECH-446 (within-arm window; measurable where STRONG -- seed 42) non-vacuity certifiers fired on DISJOINT seeds, empty intersection, so C2 was never scorable on a coupling-certified seed. Existence proofs BOTH children (MECH-445 seed-44 375 commit-intent / OFF beta=0; MECH-446 seed-42 within-arm 0.333->0.0 C2 PASS), recorded as narrow non-scoring positives (claims.yaml evidence_quality_note). NOT a falsification, NOT a substrate ceiling. SD-034 narrowed umbrella + MECH-445 + MECH-446 stay candidate / v3_pending / pending_retest_after_substrate (460k PROMOTES NOTHING until it scores). 468f (perseveration side) separately owed. Do NOT re-author 460d/468d/460e/460f/460g/460h/460i/460j (superseded/run). --- HISTORICAL prior 460h-PASS-criterion routing retained in governance_2026_06_19b + governance_2026_06_20. Cross-link IGW-20260531-021."
      governance_2026_06_20: "V3-EXQ-460h RAN + AUTOPSIED + APPLIED (session autopsy-apply-460h-20260620T0843Z, consuming confirmed failure_autopsy_V3-EXQ-460h_2026-06-20; interactive gate). 460h is the FIRST evidence for the re-grained children MECH-445 (closure->beta coupling engagement) + MECH-446 (de-commit-authority magnitude). VERDICT: non_contributory both, NO weakens, pending_retest_after_substrate. The refractory-independent commit-intent certifier (ree-v3 main 167b3b7) is CONFIRMED WORKING -- seed-44 sd034_n_closure_commit_intent=375 where 460g's coupled-elevation counter collapsed 36->0 under the de-commit-magnitude lever; the S5 self-defeat is CLOSED. The run still self-routes substrate_not_ready_requeue because the two non-vacuity certifiers fire on DISJOINT seeds (commit-intent on the WEAK-natural-commit seed 44, OFF committed_steps=0; within-arm window on the STRONG-natural-commit seed 42) -- empty intersection, C2 (MECH-446) never scorable on a MECH-445-coupling-certified seed; precondition_unmet, not a fair C2 FAIL. Existence proofs both children (seed-44 / seed-42 0.333->0.0). LOAD-BEARING REFRAME (user-directed cluster lens): the SD-034 de-commit is the COMMIT/RELEASE-DURATION FACE of the F-dominance conversion ceiling (root C reclassified from open/orthogonal -- contradicts the standing conversion_ceiling_phase0_synthesis_2026-06-18 classification, now updated): the ~2400-2600-step natural-commit latch occupancy that swamps the de-commit IS the F-driven E3 commitment (running_variance<commit_threshold <- F-dominated score; V3-EXQ-571 88-89%), so the closure-coupled de-commit is a modulatory channel subdominant to the same F-driven commit that monopolises the candidate argmax (root B). APPLIED: 460h manifest evidence_quality_note + narrow_supports + pending_retest (already non_contributory per-claim); 460g manifest -> superseded; 460h marked reviewed; index rebuilt. claims.yaml MECH-445/446 evidence_quality_note existence proofs + MECH-445 what_would_answer REGIME-SCOPED to weak-natural-commit seeds (the 2/3 commit-intent=0 seeds 42/43 are strong-natural-commit redundancy, not inert coupling; user-confirmed) -- NO status change (both stay candidate/v3_pending/pending_retest). conversion_ceiling_phase0_synthesis root C reclassified; substrate_queue f_dominance_conversion_ceiling amended (NEW commit-entry-decisiveness / latch-occupancy rung + 460h failure_record + 514t/625e cluster members + MECH-445/446 unblocks); GAP-I looped in. owner_exq advanced 460h -> 460i (gated, not yet queued). GAP-4 STAYS in-progress. (session autopsy-apply-460h-20260620T0843Z)"
      governance_2026_07_21: "V3-EXQ-631 CONFIRMED PHANTOM (doc-only correction, no experiment/claims action; session loving-banach-31d3c4). V3-EXQ-631 does not exist and never did: no entry in ree-v3/experiment_queue.json current or historical (`git log -S\"631\" --all -- experiment_queue.json` returns only two unrelated numeric-substring hits, de92762 + bbd7ea6), no script under ree-v3/experiments/, no manifest and no runs/ pack under evidence/experiments/. The only commit naming it is the REE_assembly planning commit 386629042a that proposed it. It was a DUPLICATE ID: the same experiment was queued the same day (2026-06-02) by a concurrent session as V3-EXQ-629 (v3_exq_629_mech342_ecological_maintenance_release_evidence, recorded in governance_2026_06_02b above) -- both plan sections were evidently written without knowledge of the other, so 631 is a phantom sibling of 629, not deferred work owed. WHAT ACTUALLY RAN: 629 (manifest ..._20260602T225839Z_v3.json) FAIL / non_contributory / claim_ids []; 629b (manifest ..._20260612T155004Z_v3.json) FAIL / non_contributory / claim_ids [MECH-342]. Per governance_note_2026_06_13 on MECH-342 in claims.yaml, 629b's failure is UPSTREAM foraging incompetence (nav-competence not transferring to the ecological harness), NOT a MECH-342 defect -- the contact-guard held on only 1/3 seeds, and on the one competent seed (43) MECH-342 maintenance-release FIRED correctly (decommit_transitions=34, mech342_fires=1, beta occupancy 1.0->0.217 in the degraded window vs 1.0 OFF), a narrow single-seed positive. Not a falsification. MECH-342 TODAY: candidate / v3_pending true / pending_retest_after_substrate true, live_status as_of 2026-07-11 verdict non_contributory-precondition_unmet from failure_autopsy_V3-EXQ-732; nothing for it in the queue. The ecological retest is UNQUEUED and gated on the scaffolded_sd054_onboarding nav-competence leg clearing >=2/3 seeds in the ecological harness; no new EXQ id is minted here (separate chipped work). Three stale rows repointed at the 629/629b lineage: the Full-GAP-4-closure line, the Other-relevant-EXQs table row, and the 2026-06-02 disposition Effect-on-GAP-4 paragraph. Future readers: do not go looking for 631 evidence."
      governance_2026_06_01: "V3-EXQ-592d disposition LANDED via failure_autopsy artifact (2026-06-01T05:57Z) + /governance cycle 0607Z (2026-06-01T06:17Z): measurement defect on C1 baseline, NOT substrate falsification. Substrate sound. 592d reclassified non_contributory on flat + runs manifests; MECH-090 claims.yaml evidence_quality_note appended; pending_retest_after_substrate=false; substrate_queue action=none. GAP-4 status remains in-progress pending V3-EXQ-592e successor (routed to /queue-experiment). Case 3 in closure-drift terms: node now suppressed via manifest_evidence_direction=non_contributory rule (alongside case_3_self_tag pathway). owner_exq stays V3-EXQ-592d in the field until 592e is queued; once queued, update owner_exq to V3-EXQ-592e and last_updated."
      completion_note: "Phase 2 DONE 2026-05-21 reconcile: V3-EXQ-460..468 scripts in ree-v3/experiments/; substrate-readiness PASS on all nine (460/466 x2, 461 reviewed 2026-05-12, 462/465 executed 2026-04-21, 463/464/467/468 authored+PASS 2026-04-21). Queue slots consumed post-run (not re-queued). 2026-05-21 V3-EXQ-592 surfaced rv-only commit-entry pathology (seed 42 rv=2.7e-5 with nav_competence=0.0). 2026-05-28 lit-pull synthesis (REE_assembly/evidence/literature/targeted_review_connectome_mech_090/synthesis.md commit 9e68c5ca8a) dispositioned R-a NOT defensible / R-b conservative / R-c strongest. 2026-05-28 implement-substrate landed the within-tick decisiveness axis of R-c (per-candidate score_margin gate at BetaGate.should_admit_elevation; floor 0.05). 2026-05-29 implement-substrate landed the across-tick motor-program readiness axis of R-c (CommitReadiness EMA module + nav_competence harness-push seam + conjunction AND-composed with score_margin gate at both elevate sites; floor 0.3). Both axes are R-c readings; both can be enabled/disabled independently. 2026-05-29 V3-EXQ-592b (2-arm, score_margin-axis-only) FAILed DLAPTOP-4 (manifest silent-drop pre-runner-pipeline-fix 41c3411). 2026-05-30 V3-EXQ-592c (2-arm, score_margin-axis-only re-run post-fix) FAILed ree-cloud-3. 2026-05-31 V3-EXQ-592d queued (expanded to 4-arm, FIRST-EVER nav_competence axis validation; supersedes 592c). Phase 4/5 behavioural arms still blocked on V3-EXQ-592d PASS."
      governance_2026_08_18: "ACKNOWLEDGED, no status change (/governance cycle 2026-08-18, session governance-paused-bb6e76). Flagged by check_closure_drift.py under 'Stale since last update' because confirmed failure_autopsy_V3-EXQ-935_2026-08-18 reclassified MECH-266 -- one of this node's unblocks_claims -- after the node's then-current last_updated of 2026-08-16. Governance reviewed it and the new evidence does NOT change the node: the 935 disposition is non_contributory/standard and PERIPHERAL to MECH-266 (935 sweeps a single symmetric affinity_input_cap and contains no asymmetric-threshold arm, so MECH-266's Schmitt trigger was never instantiated -- it is a calibration step UPSTREAM of any MECH-266 test, not a test of it). The node therefore stays in-progress with its named successor V3-EXQ-935a, and last_updated is bumped purely to record the acknowledgement so the node clears the report rather than re-flagging every cycle."
    - id: "commitment_closure:GAP-4-battery"
      title: "OCD-battery completeness: the *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) for SD-034/MECH-266/267/268 + MECH-342 ecological -- split out of GAP-4"
      status: in_progress
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-034, MECH-266, MECH-267, MECH-268, MECH-342]
      depends_on: ["commitment_closure:GAP-4", "commitment_closure:GAP-3", "commitment_closure:GAP-11"]
      cross_plan_link: ["sd033_governance:CHK-SD034"]
      last_updated: 2026-08-21
      governance_2026_08_21: "Closure-drift stale-since-review ACKNOWLEDGE (governance cycle 2026-08-21, gov-20260821-0203). Flagged because confirmed failure_autopsy_V3-EXQ-935_2026-08-18 reclassified MECH-266 after last_updated. This cycle did not re-adjudicate 935; live: block was already current (as_of 2026-08-18). Does NOT change this node. Status stays in_progress; last_updated bumped to acknowledge."
      governance_2026_08_16: "Stale-since-review acknowledgement only (no status change; /governance cycle cranky-driscoll-126a36). Same trigger as the sibling GAP-4 note: confirmed failure_autopsy_V3-EXQ-934_2026-08-16 reclassified MECH-266 after this node's 2026-08-12 last_updated. This node tracks the *b BEHAVIOURAL cohort (460b/461/463b/464b/466b/467b/468b). V3-EXQ-934 is a cap-sweep MEASUREMENT-PRECONDITION probe on the mode-occupancy register, not a behavioural-cohort arm, so it does not advance or retire any *b leg. It is, however, mildly CONFIRMATORY of this node's standing block rather than neutral: 934's MECH-266 arm could not be exercised at all (fraction_in_external_task 1.0, n_switches 0 in all 15 cells), which is the same could-not-engage signature the *b cohort recorded, and it is TWICE NON-PRODUCTION (salience_affinity_input_cap defaults None, use_external_task_drive defaults False) -- so it reinforces, from a fresh angle, the don't-queue-commitment-dependent-behavioural deferral this node's resume_condition already names. No change to the owed work. Stays in_progress; last_updated bumped. PROMOTES/DEMOTES NOTHING."
      governance_2026_08_12: "Stale-since-review acknowledgement only (no status change; /governance cycle sd-016-h3-algorithm-3370cd). Same trigger as the sibling GAP-4 note: confirmed failure_autopsy_V3-EXQ-923_2026-08-12 reclassified MECH-267 after this node 2026-08-10 last_updated. This node tracks the *b BEHAVIOURAL cohort (460b/461/463b/464b/466b/467b/468b); 923 is a MECHANISM-locus discrimination leg on the CEM elite-refit, not a behavioural-cohort result, so it does not advance or retire any *b leg and changes nothing about this node owed work. Recorded so the acknowledgement is explicit rather than inferred from the sibling. Stays in_progress; last_updated bumped. PROMOTES/DEMOTES NOTHING."
      governance_2026_08_10: "Stale-since-review acknowledgement only (no status change; /governance cycle queue-depth-low-ops-aac785). Flagged for failure_autopsy_V3-EXQ-869_2026-08-02 and failure_autopsy_V3-EXQ-869a_2026-08-03 (both MECH-267, non_contributory/competence_implementation_gap). MECH-267 is one of the commitment-DEPENDENT arms this node's resume_condition already names as deferred-blocked on the incomplete BG commitment layer -- a non_contributory result there is consistent with, not new information against, the existing block. Node stays in_progress as battery-incomplete; last_updated bumped to acknowledge."
      resume_condition: "466e RAN + PASSED (governance-cycle-20260625T0420Z). The SD-034 residue-discharge battery arm is DONE; the residual node openness is the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342), which the standing don't-queue-commitment-dependent-behavioural rule defers until the BG commitment layer is complete (blocked-on-upstream). Node stays in_progress as battery-incomplete, NOT as discharge-arm-pending."
      governance_2026_06_25: "OWNER 466e RAN terminal PASS/supports 2026-06-25T03:02Z (manifest v3_exq_466e_satisficing_residue_discharge_behavioural_20260625T030205Z_v3; supersedes V3-EXQ-466d). The 466d harness gap is FIXED: sd034_satisficing_discharge_confirmed -- all three load-bearing criteria PASS and non_degenerate (C1_n_closures, C2_discharge_events, C3_off_no_closure_no_discharge), and the new residue-field-populated non-vacuity gate (ON residue_active_peak >= 1 on >= 2/3 seeds) is MET, so C2 now fires genuinely rather than from the 466d empty active_mask. SD-034 records a clean supports for the residue-discharge leg (part c of the done-token). APPLIED (user-approved 'Apply supports + supersede 466d'): SD-034 evidence supports (auto-scored); 466d manifest -> evidence_direction:superseded (whole run scoring-excluded); SD-034 STAYS provisional + pending_retest_after_substrate=True (the de-commit-authority lineage GAP-4/460h..460l still owes its retest -- a single discharge-leg PASS does not clear the claim's broader retest debt). 466e marked reviewed. Node STAYS in_progress: the SD-034 discharge arm is delivered, but the MECH-266/267/268/342 commitment-dependent arms remain deferred-blocked on the incomplete BG commitment layer (don't-queue rule). This is Case 3 in closure-drift terms -- the owner_exq 466e reached terminal PASS, but the node is legitimately non-terminal pending those deferred successor arms (blocked-on-upstream BG commitment layer), NOT drifted. (session governance-cycle-20260625T0420Z)"
      result_note: "2026-06-24 (failure-autopsy-466d-20260624T2200Z): AUTOPSIED + CONFIRMED non_contributory (interactive gate). owner V3-EXQ-466d FAILed C2_discharge_events 0/3 while C1_n_closures PASSED -- closures now FORM (466c Leg-A hook fixed) but the discharge does NOT follow because the residue field is EMPTY for the whole run: ResidueField.discharge_domain is implemented + correctly wired (closure_operator.residue=residue_field, agent.py:1577) and fires every closure, but neither the scaffold curriculum nor the 466d eval ever calls agent.update_residue() (the sole add_residue path), so discharge_domain returns 0 from an empty active_mask (field.py:671) regardless of closure behaviour. C2 is DEGENERATE (pinned by test construction) -- the V3-EXQ-642 invalid-precondition pattern, NOT a falsification and NOT a substrate ceiling (the discharge mechanism needs no enrichment; the manifest's criteria_non_degenerate C2=true is wrong). SD-034 -> non_contributory + pending_retest; MECH-094 -> non_contributory (waking-only, not exercised) + DROPPED from scored tags. Re-derive brake NOT fired (642 exemption: harness gap; SD-034's 9 priors are the separate MECH-445/446 latch lineage). Route /queue-experiment V3-EXQ-466e: wire update_residue into scaffold P1/P2 + eval, add a residue-field-populated non-vacuity gate, claim_ids=[SD-034]. substrate_queue action=none. See failure_autopsy_V3-EXQ-466d_2026-06-24.{md,json}. Node STAYS in_progress -- the 466e harness-fix re-queue is the owed next step (chip). Governance applies the evidence_direction at its next walk."
      registered_note: "Registered 2026-06-23 (session closure-map-enhance-20260623T043407Z) to surface the OCD-battery-completeness half of GAP-4, whose work has diverged from the de-commit-conversion lineage GAP-4 now tracks. The *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) is substrate-UNBLOCKED (curriculum + env primitives both DONE since 2026-06-02) but was never queued; the sd033_governance CHK-SD034/MECH266/267/268 nodes are `done` only at substrate-readiness, so SD-034/MECH-266/267/268 remain candidate awaiting these behavioural arms. CAUTION (per the standing don't-queue-commitment-dependent-behavioural rule): any arm whose DV needs sustained action-commitment would re-derive the F-dominance conversion ceiling while the BG layer is incomplete -- gate against that; the commitment-FREE arms (e.g. 466b residue-discharge / satisficing reads) are the safer first queue. Author via /queue-experiment. NOT queued here (experiment_queue.json held by concurrent sessions). NO claims.yaml change."
    - id: "commitment_closure:GAP-5"
      title: "MECH-090 V_s commit-release pathway (V3-EXQ-481 FAIL)"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [MECH-090]
      depends_on: []
      last_updated: 2026-05-17
      completion_note: "Root causes audited (2026-05-17): (1) natural variance gate never crossed in short runs -> beta never elevated -> _committed_anchor_keys never set; (2) empty-snapshot secondary: set().issubset(any)=True -> predicate vacuously False. Fixes: (1) V3-EXQ-481b uses forced commitment (beta_gate.elevate() + manual snapshot) per EXQ-461 pattern; (2) lazy re-population added to agent.py select_action() -- if snapshot is non-None but empty and current_keys is non-empty while beta elevated, re-populate; release runs on next tick. 477/477 contracts pass. Dry-run: UC1 (ON fires) + UC2 (OFF silent) + UC3 (empty-snapshot re-pop) all PASS. Queued 2026-05-17."
    - id: "commitment_closure:GAP-6"
      title: "MECH-260 vs SD-034 No-Go pulse boundary unclear (V4 flag)"
      status: deferred
      severity: low
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [MECH-260, SD-034, SD-033a]
      depends_on: ["commitment_closure:GAP-4"]
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-7"
      title: "MECH-091 salient-event trigger wiring (2 of 3 triggers unwired; phase_reset itself is built)"
      status: done
      severity: low
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [MECH-091]
      depends_on: []
      blocking_external: []   # cleared 2026-09-01: MECH091-SALIENT-EVENT-TRIGGER-WIRING landed ree-v3 6293b2395248 on 2026-08-17
      last_updated: 2026-09-01
      governance_2026_09_01: "FLIPPED blocked -> done (GFLAG-0067, session govdesk-20260901). Both halves are now discharged and the 2026-08-22 acknowledgement above is superseded. THE WIRING LANDED: ree-v3 6293b2395248, 2026-08-17, wiring the two previously-unwired salient-event triggers into phase_reset() at 4 call sites in agent.py. THE VALIDATION RAN AND PASSED: V3-EXQ-944b, 2026-08-25, PASS/supports, non_degenerate, claim_ids [MECH-091]; reviewed and applied to the claim by the 2026-08-28 governance cycle; indexer scores MECH-091 exp_conf 0.76, quadrant confirmed_established, latest_run_id 944b. CAVEAT THAT TRAVELS WITH THIS FLIP: the PASS rests on FIVE OF SIX SEEDS -- seed 7 is red on episode_admits_cycle_contrast / rate_match_holds and is unscored, not refuting. Do not cite a bare PASS. NOTE the node was stale by a full governance cycle: its live: block still named the 944 autopsy and routed to queue-experiment, an action already performed and reviewed. GFLAG-0067 asked for pending_review to be walked for 944b; that was already done on 2026-08-28, so only this node flip remained."
      governance_2026_08_22: "ACKNOWLEDGED, no status change (Step 5b case 3). The V3-EXQ-944 autopsy confirmed 2026-08-22 reclassified MECH-091 non_contributory / epistemic_category standard, which is why the staleness detector flagged this node -- but it does NOT move the node. 944 is an instrument/test-design result (readiness precondition P3 read 0.914 on seed 42 because the RATE_MATCHED control degenerated into NO_RESET; all four acceptance criteria PASSED and were non-degenerate), not evidence about whether the two unwired salient-event triggers exist. The node stays blocked on substrate_queue MECH091-SALIENT-EVENT-TRIGGER-WIRING exactly as the 2026-08-16 generation decision left it, and MECH-091 stays candidate in the V3 denominator. last_updated bumped to record the acknowledgement. The autopsy additionally routes a /queue-experiment successor (three mis-specified guards to fix: P1 floors the wrong denominator, P3 is a self-cancelling ratio, P2 measures a near-constant; the due=min(due,72) clamp is inert) -- that successor is downstream of the wiring build, not a substitute for it. Governance cycle bold-chaum-7e245c."
      governance_2026_08_16: "GENERATION DECIDED -- the decision GFLAG-0037 said had never been made is now made, and this node stops being an orphan. /governance cycle cranky-driscoll-126a36, user-adopted, on the DECISION-READY brief evidence/planning/sd006_phase2_generation_brief.md (chip-20260815-sd006-phase2-generation-brief). DECISION: SPLIT, rather than the V3-or-V4 pick the flag posed -- BOTH branches as posed inherit a FALSE PREMISE. (a) MECH-091 -> V3 as a small buildable. (b) SD-006 phase 2 TRUE CONCURRENCY -> V4. WHY THE POSED QUESTION WAS WRONG: MECH-091's phase_reset() is BUILT (ree_core/heartbeat/clock.py:182), WIRED (agent.py:9903) and was MEASURED on 2026-08-01 as the DOMINANT driver of E3 tick cadence in a real 53,063-step rollout (diagnostic_arc071_e3_reselection_probe_2026-08-01.md) -- so the 2026-05-08 deferral rationale ('there is no oscillatory clock phase to reset, the mechanism under test is absent') is contradicted by direct measurement four months later, and nobody connected the two. Further, 'phase 2' is NOT ONE THING: control_plane_heartbeat.md:201-209 offers three options and RECOMMENDS HTA (option 3), whose defining mechanism (MECH-089 ThetaBuffer) IS ALREADY BUILT, while clock.py:32 fuses that recommended-and-built option with the spec-DISFAVOURED threading option (option 1, GIL caveat) into a single deferral -- and every downstream 'blocked on phase 2' inherited the fused definition. What genuinely remains unbuilt is option 1, true concurrency, which is a poor fit for a torch substrate and a reasonable V4 item. THE REAL MECH-091 GAP is small and buildable: of the three salient events the claim names (task completion, unexpected harm, commitment-boundary crossing), only harm_signal < 0 calls phase_reset(); completion and commitment-boundary crossing are unwired, and both events already exist in the substrate (hippocampal completion drives BetaGate release; commitment entry/exit IS the MECH-090 beta-gate boundary). Registered this cycle as substrate_queue MECH091-SALIENT-EVENT-TRIGGER-WIRING (priority 2, degrading, node_class 'complicated (buildable)'), which is what blocking_external now points at instead of the fused phase-2 string. THIS NODE THEREFORE MOVES deferred -> blocked, entering the V3 denominator: MEASURED closure effect, by A/B regeneration of scripts/generate_closure_snapshot.py on an isolated detached worktree at base 4089301534 with the A arm reproducing the 71.9%/94 baseline exactly, is 71.9% across 94 non-deferred -> 71.3% across 95; remaining 32 -> 33; deferred 13 -> 12; blocked 11 -> 12; done UNCHANGED at 62. WHAT STAYS PHASE-2-GATED and is NOT unblocked by this: ARC-023, MECH-092's consolidation half, MECH-291-quiescent, MECH-057a, and the three downstream claims (MECH-165, MECH-209, MECH-122) -- ARC-023's non-degeneracy precondition is specifically that rate separation survive REAL asynchronous load, which no phase-1 test can supply, so it is honestly V4 and its implementation_phase is corrected v3 -> v4 in claims.yaml this cycle. ONE CHEAP PUZZLE-GRADE CHECK IS OWED BEFORE BUILDING, carried on the substrate entry rather than gating this node: confirm MECH-091's what_would_answer DV ('no partial-integration artefacts straddling a salient event') is observable on phase 1 and not itself absorbed by the EXQ-131 E3-output-freeze staleness artifact -- one reading of the E3 integration path, not an experiment. That is the honest counter-argument the brief states against its own recommendation; if it fails, the brief's V4 branch is the fallback and nothing is wasted. needs_review CLEARED (it had been true since the D-002 detector flagged 'newest_forward_predates_later_decision_event(s)' and nothing acted for over three months). Recorded in decision_log.v1.jsonl for MECH-091 and ARC-023."
      governance_2026_08_15: "ADJUDICATED (session orphan-v3-claims-adjudicate-6f88bd, chip-20260815-orphan-v3-claims-adjudicate; D-002 orphan-V3-claim finding, severity P2/weak, confidence 0.45). NOTE ONLY -- NO status change applied (outside this session's authority). VERDICT, and this is the one of the four D-002 cases that does NOT resolve cleanly: the `deferred` status is UNJUSTIFIED AS RECORDED, but `blocked` is NOT established either, because the fact that would decide it does not exist anywhere. This is a `puzzle (known rules)` -- the missing fact is the GENERATION OF SD-006 PHASE 2 -- not a `complicated (buildable)` fix. Do not resolve it by picking a status. FIVE artefacts consulted: (1) claims.yaml MECH-091 line 11117 -- implementation_phase v3, status candidate, live_status reading candidate, verdict hold_candidate_resolve_conflict/applied; NOTE it carries NO v3_pending KEY AT ALL, which is why D-002 graded this weak, and the grading is right: implementation_phase alone is the weakest possible V3 assertion and claims.yaml itself records elsewhere that 'the implementation_phase field is a prediction, not a permission gate'; (2) claims.yaml MECH-091 what_would_answer -- 'SUBSTRATE PRECONDITION: requires SD-006 phase 2 (async multi-rate loop execution) to be built', with BOTH EXQ-133 runs (2026-03-28 and the 2026-04-21 rerun) reclassified non_contributory for exactly that reason, twice, 'NOT a falsification'; (3) claims.yaml SD-006 -- status `implemented`, but the status_note scopes that to 'phase 1: time-multiplexed'. So SD-006 reads implemented while the specific thing MECH-091 needs, phase 2 async, is NOT built; (4) substrate_queue.json -- SD-006 has ZERO entries. Phase 2 is not queued, not scoped, not prioritised, and carries no generation label anywhere in the repo. There is no artefact that says phase 2 is V3 and none that says it is V4; (5) this node -- deferred, severity low, last_updated 2026-05-08, i.e. never revisited in over three months. MECHANISM (why the inconsistency arose): a DEFERRAL KEYED TO AN EXTERNAL SUBSTRATE THAT WAS NEVER SCOPED. GAP-7 was registered 2026-05-08 with blocking_external 'SD-006 phase 2 async heartbeat' and deferred on that basis. That is a reasonable thing to do ONLY if something else then carries SD-006 phase 2 -- and nothing does: it never reached substrate_queue.json, so no scoping pass, no IGW discovery and no /implement-substrate route can ever see it. The deferral therefore became permanent by omission rather than by decision, and MECH-091 fell out of the V3 denominator as a side effect. Two independent signals on the node now contradict its own status: its live block (as_of 2026-08-13, from failure_autopsy_mech266-464e-467e-cluster) carries next 'routing=implement-substrate' -- i.e. the most recent autopsy says the next step is to BUILD something, which is not what `deferred` means -- and it is the ONLY node in this D-002 batch carrying needs_review TRUE, with needs_review_reasons ['newest_forward_predates_later_decision_event(s)'], i.e. the repo's own staleness machinery had already flagged this node and nothing acted on the flag. PROPOSED FIX (route: /governance), IN ORDER -- the first step is a decision, not an edit: (a) DECIDE the generation of SD-006 phase 2 async multi-rate execution, and record it. If V3 -> add an SD-006-phase-2 entry to substrate_queue.json and set this node `blocked` (weight 0.1, +1 to the V3 denominator). If V4 -> keep this node `deferred` and CORRECT claims.yaml MECH-091 implementation_phase v3 -> v4, which is the claims.yaml half of this and is PROPOSED, NOT APPLIED, per this session's authority. Either way the orphan closes; what is not acceptable is the current state, where neither is recorded and the claim is invisible to both the V3 denominator and the substrate queue. (b) Clear needs_review on this node once (a) lands. CLOSURE EFFECT, MEASURED not estimated, by A/B regeneration of scripts/generate_closure_snapshot.py in an isolated worktree at the same base (REE_assembly HEAD 2026-08-15), this node plus arc_062_rule_apprehension:GAP-I-absorption and behavioral_diversity_isolation:GAP-G all moved deferred -> blocked: 71.9% across 94 non-deferred nodes -> 70.0% across 97, remaining 32 -> 35, done UNCHANGED at 62, deferred 13 -> 10. Per-node attribution was not separated -- the three were measured as one A/B. The B arm is the 'SD-006 phase 2 is V3' branch of (a); if governance decides V4 instead, this node contributes nothing and the delta is smaller."
    - id: "commitment_closure:GAP-8"
      title: "SD-033b behavioural validation (devaluation + perceptual discrimination)"
      status: assembling
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      assembly_status: built
      unblocks_claims: [SD-033b, MECH-263]
      depends_on: ["commitment_closure:GAP-3"]
      cross_plan_link: ["conversion_ceiling_campaign:P3-ofc", "conversion_ceiling_campaign:FULLSTACK"]
      last_updated: 2026-06-23
      governance_2026_06_23: "ASSEMBLY-FRONTIER MIGRATION + EDGE RECONCILE (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). status in-progress -> assembling per the assembly-vs-closure keystone (this node is the named first migration candidate, REE_assembly/CLAUDE.md). Justification: 485m's CONFIRMED autopsy FACE-VALIDATED the OFC valuation face and folded it into conversion_ceiling_campaign:FULLSTACK (use_ofc_devaluation_head ON); the re-derive brake REFUSES an isolated 485n, so this node's real resolution path is the campaign's full-stack arm, not another isolated behavioural letter -- i.e. it is 'substrate being assembled', not a stalled in-progress gap. awaiting=conversion_ceiling_campaign:FULLSTACK, assembly_status=built (the decoupled devaluation_bias_head is built, ree-v3 758956f). Added cross_plan_link to conversion_ceiling_campaign:P3-ofc (the campaign node that owns the folded OFC face) + :FULLSTACK -- previously prose-only, now drawn. SD-033b/MECH-263 UNWEAKENED (candidate / substrate_conditional / pending_retest_after_substrate). REOPEN/advance on the FULLSTACK run. PROMOTES NOTHING."
      governance_2026_06_21c: "OWNER FRONTIER ADVANCED 485j -> 485k (governance-cycle-20260621T1919Z, closure-drift stale-since-review reconcile). V3-EXQ-485k RAN FAIL 2026-06-21T19:25Z (during this governance cycle) and self-routed substrate_not_ready_requeue (manifest non_contributory / non_degenerate:false -> already scoring_excluded, no governance weight). NEW SIGNATURE: unlike 485e-j, ALL FOUR readiness/non-vacuity preconditions MET (high-threat range 0.423, FIX-2 devalued-state range 0.107 >= 0.05, head-delta 5.64, MECH-448 excluded_count=5 > 0 -- envelope fired) yet BOTH load-bearing DVs vacuous (C1 + C2 non_degenerate=false; C2 a REGRESSION from the 485j conversion). Readiness-met / DVs-vacuous: the self-route label is questionable, so this was FLAGGED for /failure-autopsy (user-confirmed) and LEFT PENDING this cycle -- diagnose the DV vacuity + the 485j C2 regression from FIX-1's re-ranking driver, flag the 485e->k /claim-synthesis recurrence. The 485j manifest's self-stamped weakens was ALSO overturned -> non_contributory both claims this cycle (confirmed failure_autopsy_V3-EXQ-485j; index rebuilt, SD-033b/MECH-263 genuine_exp weakens 1->0; the SD-033b hold_candidate_resolve_conflict pending_user item cleared). owner_exq lead repointed 485j -> 485k (485j/485i/485h/485g preserved as [HISTORY]). NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate. GAP-8 STAYS in-progress (485k self-routed, did not close the gap; awaiting the autopsy + a re-ranking-DV successor)."
      governance_2026_06_21b: "OWNER FRONTIER ADVANCED 485i -> 485j (focused plan-doc reconcile under TASK_CLAIMS; check_closure_links/governance derive regen). V3-EXQ-485i RAN FAIL 2026-06-21T12:42Z and self-routed substrate_not_ready_requeue (manifest v3_exq_485i_sd033b_demotion_enabled_behavioural_20260621T124253Z_v3; non_contributory / non_degenerate:false -> already scoring_excluded, no governance weight). failure_autopsy_V3-EXQ-485i_2026-06-21 (status=confirmed) verdict: the self-route is CORRECT and the test was genuinely vacuous -- the MECH-448 F->eligibility demotion lever silently did not engage (f_eligibility_excluded_count==0 on all seeds; the 0.30 absolute merit-share floor admitted all 8 candidates because the OFC-isolated SD-054 behavioural bank's SPREAD F leaves the best candidate below the 30% share floor), so the demotion-ON test arm reduced to the demotion-OFF F-dominance-ceiling arm (ARM_2==ARM_1) and the C1/C2 behavioural DVs never ran through a genuinely-demoted selector. The adjudicated routing was implement-substrate-style harness calibration + re-queue (NOT a MECH-439 F-variance rebalance, NOT /claim-synthesis). V3-EXQ-485j (NEW letter, supersedes 485i) was authored + queued + ingested 2026-06-21 (ree-v3 main 4680c0d; coordinator DB row pending; verified present in experiment_queue.json). 485j ports the 485i 3-arm behavioural harness and CALIBRATES the absolute f_eligibility_envelope_floor per-(arm,seed) to the bank's measured merit-share distribution so the MECH-448 envelope genuinely excludes the F-best top-k in [2,4] at the largest share-gap, while KEEPING precond-3 (excluded_count>0 on >=2/3 seeds) a hard readiness gate before C1/C2 -- a flat F bank fails calibration -> all-admit -> self-route, never a false weakens. owner_exq lead repointed 485i -> 485j (485i preserved as [HISTORY]); last_updated bumped. NO claims.yaml status change -- SD-033b / MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate (485j PROMOTES NOTHING until it scores; governance applies after the run). GAP-8 STAYS in-progress (a queued/pending successor does not close the gap)."
      governance_2026_06_21: "OWNER FRONTIER ADVANCED 485h -> 485i (session inter-governance-brief-20260621T074124Z, /inter-governance-brief Step 1 plan-doc drift reconcile). The deferred retest anticipated in governance_2026_06_19b ('Deferred retest V3-EXQ-485i routes the OFC bias through the proven 569i top-k channel after the MECH-439 F-rebalance') is now QUEUED: V3-EXQ-485i (NEW letter, supersedes 485h which RAN FAIL/non_contributory 2026-06-19 = the MECH-439 F-dominance conversion-ceiling signature) was authored + ingested 2026-06-21 (ree-v3 main d7a5040; coordinator DB row pending/ree-cloud-2; /queue/active confirmed). It ports the 485h trained-OFC-head harness verbatim and RE-TARGETS the primary DVs (C1 devaluation_selection_shift, C2 between-context TV) from 485h's isolated OFC softmax to the COMMITTED selection through the real E3.select() on the MECH-448/ARC-107 rank-preserving F->eligibility demotion-enabled selector -- the ceiling MECH-448 provisionally lifted at the 06:48Z governance cycle. 3-arm dissociation (ARM_0_frozen_demotion_on silence / ARM_1_trained_demotion_off = the 485h F-dominance regime / ARM_2_trained_demotion_on the test) attributes any conversion to the trained-head AND demotion conjunction; readiness + MECH-448 non-degeneracy gates self-route substrate_not_ready_requeue, never a false weakens. owner_exq lead repointed 485h -> 485i with the 485h/485g records preserved; last_updated bumped. NO claims.yaml status change -- SD-033b / MECH-263 stay candidate / pending_retest_after_substrate (485i PROMOTES NOTHING until it scores; governance applies after the run). GAP-8 stays in-progress. (session inter-governance-brief-20260621T074124Z)"
      governance_2026_06_19b: "V3-EXQ-485h RAN FAIL 2026-06-19T19:27Z (supersedes 485g; manifest v3_exq_485h_sd033b_trained_ofc_head_behavioural_20260619T192735Z_v3), AUTOPSIED + APPLIED this /governance cycle (consumed confirmed failure_autopsy_V3-EXQ-485h_2026-06-19; the parallel autopsy session wrote the artifact + marked 485h reviewed but left the manifest weakens + applied no claims.yaml/substrate_queue -- governance completed the apply). 485h is the 485g-designed T-vs-F disambiguator + the TERMINUS of the 485 behavioural lineage: readiness MET 3/3 (bias range 0.50 high-threat; head delta 5.63), C3 silence-control PASS 3/3, but C1 1/3 + C2 0/3. DISAMBIGUATION RESOLVED: (T) threat-invariant-bias REFUTED (range collapses at the devalued state, ratio 0.12, 3/3 -- the head IS genuinely outcome-value-conditioned; MECH-263 devaluation positively shown at the REPRESENTATION level); (F) MECH-439 F-dominance conversion ceiling IMPLICATED (OFC bias reaches E3 authority range 0.50 with ZERO committed conversion; proven 569i top-k F-bypass absent from this loop). Only behavioural conversion fails, at the shared F-dominated selector. non_contributory (NOT a weakens/demotion). APPLIED: manifest evidence_direction weakens -> non_contributory (flat + nested pack) + per-claim non_contributory; index rebuilt (SD-033b/MECH-263 weakens stays 0, exp_conf 0.0 -- corrected the latent false-weakens the un-rebuilt index would have activated); 485g -> superseded; substrate_queue SD-033b failure_record += 485h; claims.yaml SD-033b/MECH-263 notes appended (epistemic_category substrate_ceiling + pending_retest UNCHANGED). owner_exq advanced 485g -> 485h. Deferred retest V3-EXQ-485i routes the OFC bias through the proven 569i top-k channel after the MECH-439 F-rebalance (569i / GAP-B 654g / 689a / 625e). SD-033b/MECH-263 stay candidate; no claims.yaml status change. (session governance-cycle-20260619T2013Z)"
      governance_2026_06_19: "V3-EXQ-485g RAN FAIL 2026-06-19. The 485f readiness-floor + driver fix WORKED -- readiness MET (bias range 0.171 >= 0.05 DV floor; head trained, delta 6.32), so the behavioural DVs scored for the first time in this lineage. RESULT: C1 devaluation 0/3 + C2 discrimination 0/3 (zero behavioural conversion) despite genuine cross-candidate bias range in the head -- the conversion-ceiling signature, NOT obviously a representational weakness. The script self-stamped this readiness-met-DVs-fail as 'weakens' (its honest-weakens path), and it is the SOLE genuine experimental entry for both SD-033b and MECH-263 (lit 0.896/0.899). Letting one substrate-limited FAIL define exp_conf for two strongly-lit claims is the illusory-conflict case on the live MECH-439 F-dominance root. USER-CONFIRMED disposition (governance-20260619T1455Z AskUserQuestion): flag for /failure-autopsy, apply NO evidence_direction this cycle. Manifest evidence_direction weakens -> non_contributory + per-claim non_contributory + pending_retest_after_substrate; index rebuilt (SD-033b/MECH-263 genuine_exp weakens 1->0, exp_conf 0.325->0.0); 485f -> superseded; 485g NOT marked reviewed (stays pending). GAP-8 STAYS in-progress (Case 3): adjudicate genuine-weakens vs conversion-ceiling, then either route to the F-dominance conversion fix (MECH-439 V3-EXQ-689 / 569i top-k shortlist -- the OFC bias drowns at the F-dominated E3 argmax) and re-issue a 485h on the converting substrate, OR accept a genuine representational weakens if the autopsy rules out the ceiling. SD-033b/MECH-263 stay candidate / pending_retest_after_substrate; no claims.yaml status change. NEXT: /failure-autopsy V3-EXQ-485g."
      governance_2026_06_17: "V3-EXQ-485g AUTHORED + AST-validated + dry-run smoke PASS (self-routes substrate_not_ready_requeue correctly at dry scale; trainable-arm head_delta=0.124 vs frozen 0.0 -> the new driver trains the head; C3 frozen-silence 1/1). owner_exq STAYS V3-EXQ-485f (already advanced by the 2026-06-12 cycle; 485f reviewed FAIL/non_contributory). DECISION = Branch-1 (bank-spread IS live): VERIFIED from the 485f manifest that the candidate-bank z_world spread is NOT the binding constraint -- 485f max_trained_bank_zworld_spread=0.043 (per-arm 0.017-0.043; SD-056 e2_action_contrastive operative; V3-EXQ-617 multistep substrate-readiness PASS all gates, NaN-fraction 0.0). The OFC-head READOUT was the wall (max_trained_bias_range=0.00898 compressed from a 0.043-distinguishable input; never approached the raised ofc_bias_scale=0.5 clamp). So GAP-8 is NOT blocked on SD-056 (which stays candidate/v3_pending but is empirically operative at behavioural runtime); it was blocked on (i) a vacuous readiness floor (485f cleared 0.00898 > 1e-3 but ~50x below the 0.05 DV floor) and (ii) 485f's under-driving shared-return selected-index REINFORCE (the 543l-collapse form). V3-EXQ-485g (supersedes 485f) fixes BOTH: (a) BIAS_RANGE_FLOOR 1e-3 -> 0.05 (== DEVAL_SHIFT_MARGIN) so 'ready' cannot certify a vacuous DV; (b) an outcome-coupled, threat-conditioned, PER-CANDIDATE REINFORCE-over-candidates driver (adv = gain*threat*(mean_harm - per-candidate harm_eval) over ALL K candidates -- the SD-033a/V3-EXQ-598b pattern sharpened to the OFC MECH-263 devaluation function), LR_OFC_BIAS 5e-4 -> 2e-3, P1 60 -> 120 ep. NON-CIRCULAR: the low-threat gradient is zero (not anti-range), so the driver gives the head the OPPORTUNITY to learn threat-conditioned range without injecting the devaluation shift; readiness-met-but-DVs-fail is then an honest weakens, below-0.05-range is substrate_not_ready_requeue (NEVER a false weakens). External touchstone: Daw 2005 dual-system + Wilson/Schoenbaum 2014 (fix the representation [done -- bank live] before re-running the readout [485g]). QUEUE APPEND + PUSH PENDING: held per /queue-experiment Step-5 working-tree-vs-HEAD audit guard -- the shared ree-v3 checkout is under active concurrent write (uncommitted ree_core/agent.py + experiment_queue.json edits from other sessions, main diverged 1/1, V3-EXQ-514s/654f scripts untracked); appending now would sweep foreign uncommitted edits into the commit. Script authored at ree-v3/experiments/v3_exq_485g_sd033b_trained_ofc_head_behavioural.py, ready to append once the tree settles. SD-033b/MECH-263 stay candidate; no claims.yaml status change."
      governance_2026_06_12: "Closure-drift stale-since-review acknowledgement (governance cycle 2026-06-12). Flagged because owner_exq pinned V3-EXQ-485e but the routing successor V3-EXQ-485f has since RUN and been reviewed (FAIL/non_contributory; readiness-gate miscalibration, cleared 0.00898 but ~50x below the 0.05 DV floor; reclassified by the batch9 cycle, NOT a weakens). owner_exq advanced 485e -> 485f. GAP-8 STAYS in-progress (Case 3): the SD-033b/MECH-263 behavioural validation is still owed -- V3-EXQ-485g (readiness floor aligned to the 0.05 DV floor) is the next successor, not yet queued. SD-033b/MECH-263 stay candidate; no claims.yaml status change."
      governance_2026_06_11b: "AUTOPSY CONFIRMED + APPLIED (governance cycle #4). failure_autopsy_V3-EXQ-485e_2026-06-11 (status=confirmed, user-adjudicated) consumed: the 485e self-route substrate_not_ready_requeue is adjudicated CONFIRMED -> non_contributory for BOTH SD-033b and MECH-263 (NOT a weakens). Root cause = cross-candidate bias RANGE collapse (1/3 seeds clear the floor) via TWO gaps: (1) OFC compute_bias clamp-saturation at the +/-ofc_bias_scale=0.1 rail on 2/3 seeds (the GAP-8 landing's pre-registered calibration risk), (2) candidate-bank z_world collapse (reconstruction-trained e2.world_forward world_states[1]; ARC-065 GAP-A / SD-056) -- even the one unsaturated+READY seed gave a vacuous deval_shift (8e-05 vs 0.05) + a degenerate C2 ratio (criteria_non_degenerate.C2=false). APPLIED: manifests (flat+nested) carry evidence_direction non_contributory + per-claim epistemic_category substrate_ceiling + failure_autopsy_ref; claims.yaml SD-033b + MECH-263 each got pending_retest_after_substrate=true + the autopsy quality note; substrate_queue AMENDED -- 485e failure record appended to the modulatory-bias-selection-authority (ARC-065 GAP-A) entry (priority 2; no new substrate). SD-033b/MECH-263 stay candidate. GAP-8 STAYS in-progress (Case 3): the routing successor V3-EXQ-485f (raise ofc_bias_scale / pre-clamp signal + enable SD-056 e2_action_contrastive in P0 + absolute floor on between_context_tv) is OWED via /queue-experiment, not yet queued. NEXT: /queue-experiment V3-EXQ-485f."
      governance_2026_06_11: "STAGE (evidence-grade behavioural arm) RAN, did NOT close GAP-8 -- owner_exq advanced V3-EXQ-485d -> V3-EXQ-485e (governance cycle #3). V3-EXQ-485e (the deferred evidence-grade trained-OFC-head devaluation/discrimination arm, claim_ids=[SD-033b, MECH-263], experiment_purpose=evidence) self-routed substrate_not_ready_requeue / non_contributory EXACTLY as the resume_condition anticipated: the trained-OFC-head bias CROSS-CANDIDATE RANGE at the high-threat positive-control state did NOT clear the pre-registered non-vacuity floor, so the devaluation DV (C1) scored 0 seeds (C2 discrimination separated on 2 seeds, C3 frozen-head silence control held 3/3). Per its design this NEVER weakens SD-033b/MECH-263 (the same-statistic bias-range non-vacuity gate). User FLAGGED 485e for /failure-autopsy (gov cycle #3): diagnose WHY the trained head did not produce sufficient cross-candidate bias range (training budget / gradient path / signal) before routing a successor. 485e LEFT PENDING (no review_tracker entry, no inline evidence stamp). GAP-8 STAYS in-progress (Case 3): on confirmed failure_autopsy_V3-EXQ-485e, apply its routing (larger-P1 / stronger-head-training successor vs substrate amend) then re-issue the trained-head behavioural arm via /queue-experiment. No claims.yaml status change -- SD-033b/MECH-263 stay candidate."
      resume_condition: "OWNER FRONTIER = V3-EXQ-485j (QUEUED 2026-06-21, pending; supersedes 485i). 485j re-runs the trained-OFC-head C1 devaluation_selection_shift + C2 between-context-TV behavioural DVs through the real E3.select() on the MECH-448 demotion-enabled selector, with the absolute f_eligibility_envelope_floor CALIBRATED per-(arm,seed) to the OFC behavioural bank's measured merit-share spread (keeps the F-best top-k in [2,4] excluded at the largest share-gap) so the MECH-448 envelope genuinely engages -- the fix for the 485i excluded_count==0 all-admit no-op where the demotion-ON arm collapsed to demotion-OFF (ARM_2==ARM_1). precond-3 (f_eligibility_excluded_count>0 on >=2/3 seeds) stays a HARD readiness gate before C1/C2: a flat-F bank fails calibration -> all-admit -> self-route substrate_not_ready_requeue, never a false weakens. RESUME: review 485j when the runner lands it. (a) On readiness MET + C1/C2 PASS -> the trained-head behavioural conversion is shown through a genuinely-demoted selector; route the SD-033b/MECH-263 candidate->provisional promotion through /governance (the governance-weighting follow-on). (b) On readiness MET + C1/C2 FAIL with the envelope genuinely excluding -> a genuine behavioural weakens (adjudicate against the MECH-439 F-dominance conversion ceiling via /failure-autopsy before applying). (c) On self-route substrate_not_ready_requeue (calibration could not seat a non-degenerate envelope) -> re-queue under a new letter with a revised calibration / converting substrate. SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate until 485j scores; PROMOTES NOTHING in the interim."
      governance_2026_06_09: "Trained-OFC-head pathway landed via /implement-substrate (commitment_closure:GAP-8, the SD-033b analogue of the now-DONE SD-033a GAP-1/GAP-D). Substrate ree-v3 382db2c (OFCConfig.train_state_bias_head + REEConfig.ofc_train_state_bias_head + OFCAnalog.bias_head_parameters(); default False bit-identical OFF; 976/977 contracts PASS, the 1 fail the documented control_vector C4 baseline flake; preflight 7/7). Docs: sd_033b_ofc_analog.md + ree-v3/CLAUDE.md GAP-8 entry; claims.yaml SD-033b evidence_quality_note c8546ae0ff (no flag/confidence change -- status stays candidate). Validation EXQ V3-EXQ-485d queued (ree-v3 8839724). GAP-8 stays in-progress pending the 485d runner result + the subsequent evidence-grade behavioural arm. owner_exq advanced 485b/485c -> 485d."
      governance_2026_06_04: "Both validation runs LANDED PASS and were reviewed by /governance 2026-06-04: V3-EXQ-485b (devaluation sensitivity, supports 3/3, post-onset divergence 0.105) + V3-EXQ-485c (task-role discrimination, supports, separation_ratio ~297, z_world match 1.0). Both are diagnostic representation-level MECH-263 functional-signature tests; SD-033b + MECH-263 stay candidate (supports recorded). GAP-8 lands PARTIAL as predicted: FULL SD-033b candidate->provisional promotion still needs the deferred trained-OFC-head behavioural arm (frozen-zeroed bias head -> behaviour-change not yet measurable; parallel to SD-033a GAP-1). status stays in-progress pending that arm. This is Case 3 in closure-drift terms (legitimately non-terminal pending the deferred trained-OFC-head behavioural arm; the 485b/485c diagnostic-validation half is done)."
      governance_2026_06_03: "Blocker GAP-3 (env extensions) DONE 2026-05-17 -> GAP-8 unblocked. Audit found V3-EXQ-485b/485c were NEVER queued (no manifests / no runner_status rows / no git history / no coordinator-DB rows) -- the prior 'queued 485b/c' note was aspirational. Authored + smoke-PASSED + queued both as REPRESENTATION-LEVEL MECH-263 functional-signature diagnostics (ree-v3 main 9f45b0f). SUBSTRATE FINDING: the OFC reads only z_world + z_harm (no appetitive value/drive input), so SD-049 satiety AND the GAP-3 counter-evidence primitive are invisible to the state_code; 485b uses an AVERSIVE outcome devaluation, 485c uses same-z_world/different-task-stage. status->in-progress (awaiting runner). NOTE: FULL SD-033b candidate->provisional promotion still needs the deferred trained-OFC-head behavioural arm (frozen-zeroed bias head -> behaviour-change not measurable; parallel to SD-033a GAP-1) -- so GAP-8 will land 'partial' on 485b/c PASS, not fully done."
    - id: "commitment_closure:GAP-9"
      title: "SD-033c/d/e graph-consolidation incomplete"
      status: done
      severity: low
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-033c, SD-033d, SD-033e]
      depends_on: []
      last_updated: 2026-06-09
      completion_note: "GAP-9 graph/registration finishing CLOSED 2026-06-09 (V3-scope, no experiment, no substrate). Three deliverables landed in one pass on REE_assembly master: (1) SD-033c (vmPFC value integration) consolidation step TAKEN -- the subsumption of ARC-035 / MECH-151 / MECH-152 / MECH-235 is now an explicit closed bidirectional edge: SD-033c gains a subsumes list + consolidation_status=complete; each of the four sources already carried instantiates: SD-033c. No new implementation, no status change. (2) SD-033d (premotor/SMA) design_doc was null -> wrote docs/architecture/sd_033d_premotor_sma_analog.md mapping the EXISTING E3 sequence-selection machinery (propose_trajectories / action_object = PMd; E3TrajectorySelector.select = pre-SMA; MECH-090 _committed_step_idx + bistable BetaGate = SMA execution; ARC-028/MECH-105 completion = sequence-end release) onto the Tanji & Hoshi 2008 gradient; linked via a design_doc field on the claim; no new substrate (records the SD-033d-i/ii/iii split trigger). (3) SD-033e (frontopolar) V3/V4 boundary made EXPLICIT via a structured v3_v4_boundary field + notes addendum: formally DEFER the substrate, implementation_phase STAYS v4 (no genuine v3 dependency to reclassify; reverse-deps MECH-264/265 are v4). V3-scope = the forward-compat hook only (reserved parallel_goal_deliberation mode + keyed-dict MECH-261 gate + no-op frontopolar_analog.py stub), which is present + complete. Also reconciled a stale doc drift: sd_033_pfc_subdivision_architecture.md had retained the old deliberative_branching placeholder in 2 places -> now parallel_goal_deliberation matching the claim + ree-v3 code. No claim promotion/demotion (registration completeness only)."
    - id: "commitment_closure:GAP-10"
      title: "StepHarness audit of governance write paths"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: []
      depends_on: []
      cross_plan_link: ["sleep_substrate:GAP-6"]
      last_updated: 2026-05-17
      completion_note: "Audit complete 2026-05-17. All 6 write sub-sites documented in sd_034_governance_closure_operator.md under 'StepHarness write-path audit (GAP-10)'. All sites are within-select_action() architectural exceptions (steps 1+4 prerequisites met before step 7 runs) or experiment-only unit tests (dacc.record_outcome). Zero sites require StepHarness re-routing. dacc.record_outcome() canonical wiring deferred to GAP-3 env extension landing (no routing error; intentional deferral)."
    - id: "commitment_closure:GAP-11"
      title: "Phased rule_state training curriculum (GAP-3 deliverable 4 -- committed-mode elicitation)"
      status: done
      severity: load-bearing
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V3-EXQ-968-871b_2026-09-02#V3-EXQ-871b"
        verdict: "non_contributory/standard"
        next: "routing=queue-experiment"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["SD-033a", "SD-033b", "SD-033c", "SD-033d", "SD-033e", "SD-034", "MECH-090", "MECH-091", "MECH-260", "MECH-262", "MECH-263", "MECH-266", "MECH-267", "MECH-268"]
      unblocks_claims: [SD-034, MECH-266, MECH-268, MECH-090, SD-021]
      depends_on: ["commitment_closure:GAP-3"]
      last_updated: 2026-05-17
      completion_note: "IMPLEMENTED 2026-05-17: experiments/committed_mode_curriculum.py -- 3-phase harness helper (NOT a ree_core substrate scheduler, O-1). API: run_p0_warmup() (E1+E2 training on easy env, mid-probe abort at 60% budget for R1 escalation), run_p1_consolidation() (target env, exits when committed_steps/ep >= 100), run_p2_eval() (frozen-policy eval, measures committed_steps/hold_rate/rule_state_norm), clone_trained_agent() (load_state_dict + rv copy for O-2 forced-rv control arm). O-2 mandatory emergent-vs-forced contrast enforced by API design. O-3 single threshold_relaxation param. Generalises EXQ-321b run_training + EXQ-543b P0/P1 scaffolding. Smoke tests PASS (P0 convergence, P0 abort gate, P1 emergence, P2 forced-rv, clone bistable). Backward compat: no ree_core changes. NEXT STEP: /queue-experiment for EXP-0157 / V3-EXQ-461 pilot (delayed-reward persistence -- simplest committed-hold test, O-5). All Phase 4/5 behavioural arms now unblocked (V3-EXQ-460b/461/463b/464b/466b/467b/468b). ree-v3/CLAUDE.md updated."
---
# Commitment / Closure / Mode-Governance Plan

**Registered:** 2026-05-08
**Status:** active
**Scope:** close the SD-034 closure-operator + MECH-090/091 commitment + MECH-260
recency-suppression + MECH-266/267/268 mode-governance + SD-033a/SD-033b
bias-pathway substrate gaps that together govern when REE *commits*, when it
*holds*, when it *releases*, and when it *disengages* -- and the OCD test
battery (EXP-0156 .. EXP-0164 reserved at V3-EXQ-460..468) that falsifies
them. Sibling plan: [sd033_governance_plan.md](./sd033_governance_plan.md)
remains the OCD-specific test-battery sub-plan (linked from
[Test cohort](#test-cohort) below).

This plan is the durable resume-point for commitment / closure /
mode-governance work across sessions. When work pauses to handle adjacent
paths (sleep substrate; V_s anchor reset; MECH-307 conjunction architecture),
the deviation is logged in the [Decision log](#decision-log) with a resume
condition.

---

## One-line framing

> The Hold latch, the No-Go suppressor, the asymmetric mode register, the
> mode-conditioned proposer, the conflict-saturation cap, and the closure
> operator have all landed. The Go-side bias pathway is still untrained
> (GAP-1). CausalGridWorldV2 env extensions and the committed-mode curriculum
> harness are landed (GAP-3, GAP-11). The OCD substrate-readiness battery
> (V3-EXQ-460..468) is complete. The MECH-090 commit-entry conjunction
> validation chain (V3-EXQ-592d->g) resolved 2026-06-02: it surfaced that
> MECH-090 governs commit *entry* but had no *release* authority -- now
> supplied by the new MECH-342 maintenance-release substrate (validated by
> V3-EXQ-592g, candidate/v3_pending). The Phase 4/5 OCD behavioural *b cohort
> is the remaining GAP-4 work and is still unqueued.

The control-plane substrate matured fast between 2026-04-10 and 2026-04-21:
MECH-090 bistable BetaGate (2026-04-10), MECH-260 FIFO action-class
suppression (2026-04-19), SD-033a LateralPFCAnalog with zeroed bias head
(2026-04-20), SD-034 ClosureOperator (2026-04-20), MECH-267 CEM-noise
mode conditioning (2026-04-20), MECH-268 dACC FIFO PE saturation (2026-04-20),
MECH-266 Schmitt-trigger asymmetric hysteresis (2026-04-21). Substrate-
readiness diagnostics PASSed across the cluster (V3-EXQ-460 / 462 / 463 /
464 / 465 / 466 / 467 / 468 sub-tests). SD-034, MECH-266, MECH-267,
MECH-268 promoted candidate -> provisional 2026-04-28.

The gap is not "more substrate"; the gap is (a) training the SD-033a bias
head so the Go side actually moves, (b) extending CausalGridWorld with the
behavioural primitives the OCD battery needs (tolerance-band completion,
counter-evidence injection, dual simultaneously-active resource cue), and
(c) authoring + queueing the rest of the battery.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| [sd033_governance_plan.md](./sd033_governance_plan.md) | Sibling plan: 2026-04-20 GAP MEMO + OCD test battery; serves as OCD-specific test-battery sub-plan under this plan |
| [docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md](../../docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md) | GAP MEMO: "REE-V3 is not missing cognition. It is missing governance." |
| [docs/thoughts/2026-04-20_modes.md](../../docs/thoughts/2026-04-20_modes.md) | Six-step mode-binding implementation sketch |
| [docs/thoughts/2026-04-20_ocd1.md](../../docs/thoughts/2026-04-20_ocd1.md) | Four constraints on closure (terminate, bind, domain-scope, dACC saturation) |
| [docs/thoughts/2026-04-20_ocd3.md](../../docs/thoughts/2026-04-20_ocd3.md) | Eight OCD subtypes mapped to control-plane failures (test-battery source) |
| [docs/thoughts/2026-04-20_ocd4.md](../../docs/thoughts/2026-04-20_ocd4.md) | SD-033 Go/Hold/No-Go gating substrate; explicit test matrix |
| [docs/architecture/control_plane_heartbeat.md](../../docs/architecture/control_plane_heartbeat.md) | MECH-090 / MECH-091 + heartbeat architecture |
| [docs/architecture/sd_033_pfc_subdivision_architecture.md](../../docs/architecture/sd_033_pfc_subdivision_architecture.md) | PFC subdivision cluster, SD-033 / SD-033a / SD-033b / SD-033c / SD-033d / SD-033e |
| [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) | SD-033a bias-pathway design, untrained head |
| [docs/architecture/sd_034_governance_closure_operator.md](../../docs/architecture/sd_034_governance_closure_operator.md) | SD-034 closure operator design (backfilled 2026-04-27) |
| evidence/literature/targeted_review_sd_034 / _connectome_mech_266 / _267 / _268 | 2026-04-27 lit-pulls for the cluster |
| substrate_queue.json SD-034, MECH-266, SD-033a entries | Implementation status anchors |

---

## Existing substrate (do not duplicate)

Lifted from [sd033_governance_plan.md "Existing substrate (not to be
duplicated)"](./sd033_governance_plan.md#existing-substrate-not-to-be-duplicated)
and extended with the post-2026-04-21 landings.

| Function | Component | Location | Status |
|---|---|---|---|
| Hold (bistable commitment latch) | MECH-090 BetaGate (bistable) | `ree-v3/ree_core/heartbeat/beta_gate.py`, `ree_core/agent.py` | active; bistable latch landed 2026-04-10; V3-EXQ-049e PASS, V3-EXQ-049a PASS, V3-EXQ-062b PASS, V3-EXQ-321b PASS |
| Urgency interrupt (hyperdirect analog) | MECH-091 z_harm_a-triggered beta release | `ree-v3/ree_core/agent.py` | implemented; phase-reset arm held on SD-006 phase 2 async |
| No-Go (recency-bias suppression) | MECH-260 `DACCAdaptiveControl._action_history` FIFO | `ree-v3/ree_core/cingulate/dacc.py` | candidate; implemented 2026-04-19; V3-EXQ-445h supports |
| Mode register with hysteresis | SD-032a SalienceCoordinator + MECH-266 Schmitt rails | `ree-v3/ree_core/cingulate/salience_coordinator.py` | provisional; MECH-266 landed 2026-04-21; V3-EXQ-464 + V3-EXQ-467 sub-tests PASS |
| Mode-conditioned write gating | MECH-261 dict-keyed registry | same | stable; promoted 2026-04-25 |
| Mode-conditioned hippocampal proposals | MECH-267 CEM-noise scale on `propose_trajectories` | `ree-v3/ree_core/hippocampal/module.py` | provisional; landed 2026-04-20; V3-EXQ-462 + V3-EXQ-465 sub-tests PASS |
| dACC PE saturation | MECH-268 FIFO outcome-history `f_sat = 1/(1 + s * max(0, n_rec - g))` | `ree-v3/ree_core/cingulate/dacc.py` | provisional; landed 2026-04-20; V3-EXQ-463 + V3-EXQ-468 sub-tests PASS |
| Closure operator (5-part "done" token) | SD-034 ClosureOperator | `ree-v3/ree_core/governance/closure_operator.py` | provisional; landed 2026-04-20; V3-EXQ-460 + V3-EXQ-466 sub-tests PASS x2 |
| Lateral-PFC-analog (rule/goal substrate) | SD-033a LateralPFCAnalog (gate-modulated EMA + frozen-zeroed bias head) | `ree-v3/ree_core/pfc/lateral_pfc_analog.py` | candidate; substrate landed 2026-04-20; **bias head untrained** (frozen-random, last Linear zeroed -> initial bias=0) |
| OFC-analog (state-space / oracle path) | SD-033b OFCAnalog + outcome oracle | `ree-v3/ree_core/pfc_analogs/ofc_analog.py` | candidate; substrate landed 2026-04-25; oracle 2026-05-04; V3-EXQ-485 PASS, V3-EXQ-485a queued |
| AIC-analog descending modulation | SD-032c AICAnalog harm_s_gain | `ree-v3/ree_core/cingulate/aic_analog.py` | candidate (independent of this plan) |
| dACC-analog conflict / pe substrate | SD-032b DACCAdaptiveControl | same | candidate (SD-032b dACC bundle) |
| Hypothesis-tag categorical write gate | MECH-094 (generalised by MECH-261) | distributed | candidate; load-bearing for sleep + replay safety -- shared with [sleep_substrate_plan.md](./sleep_substrate_plan.md) |

---

## Gap inventory

Ten gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | SD-033a bias head untrained: frozen-random with last Linear zeroed -> initial bias = 0; Go-side pathway is mechanically silent until a training protocol lands | load-bearing | MECH-262 rule-selective persistence; SD-034 mode-conditioning gate firing from a real rule_state; full-loop OCD-battery interpretability |
| **GAP-2** | V3-EXQ-461 (EXP-0157 delayed-reward persistence / Hold-axis falsifier) substrate-readiness PASS reviewed; full behavioural successor remains GAP-3 env-infra work | high | OCD battery completeness; SD-033a + MECH-090 + SD-034 Hold-axis evidence |
| **GAP-3** | CausalGridWorldV2 env extensions not built: tolerance-band completion, counter-evidence injection, dual simultaneously-active resource cue, phased rule_state training curriculum | high | SD-034 + MECH-266 + MECH-268 behavioural arms (currently smoke / sub-test only); EXP-0156/0157/0160/0162/0163/0164 full-loop runs |
| **GAP-4** | OCD battery Phase 2 DONE (460..468 substrate-readiness PASS); substrate side of MECH-090 commit-entry/release RESOLVED 2026-06-02 (592d->g chain -> MECH-342 release substrate validated by 592g); Phase 4/5 behavioural *b cohort QUEUED 2026-06-03 (460b/461b/463b/464b/466b/467b/468b; ree-v3 a5afed7) -- now awaiting runner execution | high | First end-to-end behavioural battery on env extensions + committed_mode_curriculum; SD-034 / MECH-266 / MECH-267 / MECH-268 promotion path; MECH-342 ecological evidence (V3-EXQ-629) |
| **GAP-5** | MECH-090 V_s -> commit-release pathway substrate-readiness FAIL: V3-EXQ-481 vs_commit_release_count=0 in BOTH ON and OFF arms; release predicate never matches; anchor resets fire (63/31 per seed) but release threshold never met | medium | MECH-090 release-via-V_s pathway empirical validation; tighter coupling between hippocampal anchor invalidation (MECH-269 / MECH-284) and BG beta release |
| **GAP-6** | MECH-260 vs SD-034 No-Go pulse boundary unclear: lit-pull 2026-04-27 recommended routing post-completion negative bias through SD-033a per-candidate bias projection rather than only via MECH-260 action-class FIFO; current implementation does both, with overlapping function | medium (V4 flag) | Cleaner mode-governance separation in V4; not urgent for V3 |
| **GAP-7** | MECH-091 salient-event phase-reset held on SD-006 phase 2 async heartbeat (V3-EXQ-133 reclassified non_contributory 2026-04-22) | low (V4 deferred) | MECH-091 empirical validation; deferred to V4 unless SD-006 phase 2 lands earlier |
| **GAP-8** | SD-033b behavioural validation deferred: substrate-readiness PASS (UC1-UC5) and oracle round-trip PASS (V3-EXQ-485a sub-tests); devaluation sensitivity + perceptually-identical / task-distinct discrimination need env extensions (env blocker GAP-3 landed 2026-05-17; the two representation-level diagnostics V3-EXQ-485b/485c then RAN PASS 2026-06-03 — see the node record and Status table) | medium | SD-033b promotion candidate -> provisional via behavioural evidence (currently lit-only at lit_conf 0.863) |
| **GAP-9** | SD-033c / SD-033d / SD-033e graph-consolidation **DONE 2026-06-09**: SD-033c consolidation step taken (subsumes ↔ instantiates closed; consolidation_status complete); SD-033d design_doc written + linked (sd_033d_premotor_sma_analog.md, E3/MECH-090 → premotor/SMA mapping, no new substrate); SD-033e V3/V4 boundary made explicit (substrate deferred, stays v4; forward-compat hook present) | low | Claim-graph completeness; V3-scope finishing (not V4-deferred); not gating any V3 evidence path |
| **GAP-10** | StepHarness audit of governance write paths: SD-034 closure pulse, MECH-260 inject_nogo, MECH-268 outcome buffer, SD-033a bias write should all flow through the canonical `sense / update_z_goal / update_residue` sequence enforced by StepHarness landed 2026-05-08 | medium | bit-aligned governance writes; shared concern with [sleep_substrate_plan.md GAP-6](./sleep_substrate_plan.md#gap-inventory) |

---

## Sequenced plan

Eight phases. Each phase is small, verifiable, and unblocks at least one
downstream item. Phases ordered by leverage. Where work depends on adjacent
non-governance paths (sleep substrate; SD-006 async; V_s anchor reset),
that is called out as a deviation in the [Decision log](#decision-log).

### Phase 1: SD-033a bias-head training (GAP-1) -- REFRAMED 2026-05-09

**Status:** blocked on the rule-apprehension cluster's Phase 1 + Phase 2.
The ARC-062 / MECH-309 cluster registered 2026-05-08 reframes this gap:
SD-033a's bias head needs a non-oracle rule signal to train against, and
that signal lives upstream of SD-033a in the apprehension layer. See
[arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md)
for the parent plan; this Phase 1 closes when that plan's Phase 3
(GAP-C + GAP-D) lands.

The original Phase 1 deliverable list proposed a phased pre-training-on-
rule-cue-curriculum approach. That approach presupposed an oracle
`rule_cue_id` label that, per MECH-309's logical-necessity claim, cannot
exist honestly in REE — trainers weight rules they do not invent. Pre-
training the bias head on oracle labels would produce a substrate that
learns supervised mappings in a lab but has no honest signal source in
deployment. The reframe drops the oracle-curriculum approach in favour
of joint training through ARC-062's discriminator-driven gradient path.

Reframed deliverables (all gated on arc_062_rule_apprehension Phase 1 +
Phase 2 PASS):

1. ARC-062 discriminator output wired into `LateralPFCAnalog.update()`
   source vector as a third projection alongside `delta_proj(z_delta)`
   and `world_pool_weight * world_proj(z_world)`. Owned by
   arc_062_rule_apprehension GAP-C / Phase 3.
2. Bias head's `requires_grad_(True)` and added to E3 optimiser; gradient
   flows from existing E3 path through `score_bias` back to head weights
   — no separate loss term. Owned by arc_062_rule_apprehension GAP-D /
   Phase 3.
3. Master flag `use_lateral_pfc_analog` defaults flipped to True for
   experiments that *also* enable `use_gated_policy` (the ARC-062 flag);
   remains False elsewhere. Replaces the original "rule-cue-tagged
   experiments" condition.
4. Validation EXQ: 2-arm ablation (head trainable vs frozen-zero) on the
   ARC-062 + SD-054 stack. Acceptance: trainable arm shows non-zero
   `score_bias` after N episodes AND non-trivial reef/forage strategy
   split (cross-link to ARC-062's monomodal-collapse falsifier in
   arc_062_rule_apprehension GAP-B / Phase 2).

Contract test: `lateral_pfc_analog.score_bias` non-zero on at least one
candidate after training, zero before.

Original Q1 ("phased vs joint vs frozen-trigger training protocol") is
RETIRED -- joint-with-E3 via gradient-through-score_bias is the only
architecturally honest option once the rule signal is non-oracle. See
[Decision log](#decision-log) 2026-05-09 entry for the full reframing
rationale.

### Phase 2: V3-EXQ-461 EXP-0157 authoring (GAP-2)

The Hold-axis falsifier. Ten-line scope: copy V3-EXQ-462 structure
(rule-binding) and substitute the delayed-reward persistence env hook.
Reserve queue slot V3-EXQ-461 (already in the sd033_governance_plan
reservation table). Author script via `/queue-experiment` skill.

2026-05-12 update: substrate-readiness script authored, queued, executed,
and reviewed as `v3_exq_461_mech090_sd033a_delayed_reward_persistence.py`.
Runner PASSed at 2026-05-12T18:04:25Z with six deterministic sub-tests:
baseline Hold, weakened passthrough, SD-033a/MECH-261 replay-gated
persistence, strengthened Hold, mode-gate table values, and SD-034 terminal
closure. GAP-2 is closed at substrate-readiness level. The full behavioural
delayed-reward task remains Phase 3 env-infra work.

Deliverables:

1. Reserve V3-EXQ-461 in `ree-v3/experiment_queue.json`. **Done 2026-05-12;
   runner PASS reviewed.**
2. Author `v3_exq_461_mech090_sd033a_delayed_reward_persistence.py`
   with the OCD ocd4 row's substrate-readiness acceptance criteria.
   **Done 2026-05-12; dry-run and runner PASS.**
3. Update `manual_proposals.v1.json`: EXP-0157 status `queued` ->
   `executed`; reserved_queue_id `null` -> `V3-EXQ-461`.
   `experiment_proposals.v1.json` is regenerated from the manual source by
   the governance/index pipeline.

Acceptance: substrate-readiness sub-tests PASS (no env extension required
for sub-test version; full behavioural arm depends on Phase 3).

### Phase 3: CausalGridWorldV2 env extensions (GAP-3)

The behavioural-validation gate. The OCD battery is mostly substrate-
readiness diagnostics today. Promoting from provisional -> stable on
SD-034 / MECH-266 / MECH-268 needs env primitives that don't yet exist.

Deliverables:

1. Tolerance-band completion: rule_state completion fires when the agent
   reaches a state within tolerance T of the goal, not exact-match.
   Required by EXP-0156 / EXP-0157 / EXP-0162 behavioural arms.
2. Counter-evidence injection hook: env can introduce a contradicting
   outcome stream against a persistent rule_state. Required by
   EXP-0164 (SD-034 + MECH-268 commitment vs contradiction) full-loop.
3. Dual simultaneously-active resource cue: two competing goal cues
   active in the same episode. Required by EXP-0160 (MECH-266 competing
   goals) and EXP-0163 (MECH-266 mode stickiness) behavioural arms.
4. Phased rule_state training curriculum: a curriculum schedule that
   reliably elicits committed-mode sequences (the same blocker that
   stops V3-EXQ-321 / V3-EXQ-261; see substrate_queue SD-021 / SD-022
   notes).

Acceptance: a single integration smoke run with all four primitives
exercised in one episode produces non-zero committed_steps, non-zero
counter-evidence injection events, and dual cues active for >=10 ticks.

This phase has no claim-validation EXQ; it is env infrastructure.

### Phase 4: SD-034 + closure-coupled behavioural validation (GAP-4 partial)

Once Phase 3 env extensions land, re-queue the substrate-readiness EXQs
under behavioural conditions and add the previously-deferred behavioural
arms.

Deliverables:

1. V3-EXQ-460b (EXP-0156 verified-but-not-released, behavioural):
   tolerance-band completion event triggers closure pulse; agent
   disengages within bounded window. Acceptance: bounded re-evaluation
   count after completion.
2. V3-EXQ-461 (EXP-0157 delayed-reward persistence, full): rule_state /
   goal field persists across delay window; closure fires at delayed
   resolution. Acceptance: rule_state present at delay end +
   closure-pulse signature within 2 ticks of resolution.
3. V3-EXQ-466b (EXP-0162 satisficing): sufficient-but-not-optimal action
   produces correct residue discharge. Acceptance: residue_field
   discharge within domain on satisficing completion;
   not-yet-satisficed arm preserves residue.
4. V3-EXQ-468b (EXP-0164 commitment vs contradiction, full 4-arm
   behavioural): A/B/C/D interaction with counter-evidence injection.
   Acceptance: under sustained counter-evidence, MECH-268 PE caps and
   the SD-034 closure operator does NOT fire on weak local outcomes;
   under genuine completion, both fire together.

These re-runs should also serve as substrate co-validation -- a SD-034
behavioural PASS without any MECH-266/267/268 confound is the cleanest
governance signal.

### Phase 5: MECH-266 + MECH-268 behavioural validation (GAP-4 partial)

Adjacent to Phase 4 but tests the mode-register and dACC layers
specifically.

Deliverables:

1. V3-EXQ-464b (EXP-0160 competing goals, behavioural): with dual
   simultaneously-active resource cue; symmetric vs asymmetric mode
   thresholds. Acceptance: switch-cost asymmetry detectable; symmetric
   baseline matches MECH-259 legacy.
2. V3-EXQ-467b (EXP-0163 mode stickiness, behavioural): 5-arm
   parametric sweep of exit_threshold ratio under sustained mode
   pressure. Acceptance: dose-response curve along the OCD <->
   depression axis (over-binding at exit~0; under-binding at low
   enter_threshold).
3. V3-EXQ-463b (EXP-0159 dACC saturation, 500+ step sustained outcome):
   pe plateau signature across a long identical-outcome stream.
   Acceptance: pe trajectory bounded; saturation factor f_sat falls
   below 0.5 within saturation_window ticks.

### Phase 6: MECH-090 V_s -> commit-release reactivation (GAP-5)

V3-EXQ-481 substrate-readiness FAIL identified that the
`use_vs_commit_release` hook is wired but the release predicate never
matches. Anchor resets fire 63/31 per seed but the release path is inert.

Deliverables:

1. Audit `_committed_anchor_keys` capture in REEAgent: when does a
   commit-entry record an anchor key, and is the key still present in
   `HippocampalRouter` at the moment MECH-269 anchor-reset fires?
2. Either widen the BoundaryEvent rate at commit entry or relax the
   release predicate to require *any* anchor in the committed set to
   mark inactive, not all.
3. V3-EXQ-481b 2-arm ablation (V_s release ON vs OFF) on the same
   curriculum. Acceptance: vs_commit_release_count > 0 in ON arm,
   release fires within bounded window after anchor invalidation.

This phase shares concerns with [sleep_substrate_plan.md GAP-1
(MECH-204)](./sleep_substrate_plan.md#gap-inventory) -- both
involve a captured signal that no consumer reads. Cross-link maintained.

### Phase 7: SD-033b behavioural validation (GAP-8)

After Phase 3 env extensions land, run the deferred behavioural arms.

Deliverables:

1. V3-EXQ-485b devaluation sensitivity (Q-036-style): outcome is
   devalued mid-episode; OFC oracle path's predicted-outcome signal
   updates within bounded ticks.
2. V3-EXQ-485c task-distinct discrimination: perceptually identical
   states with different task roles produce distinct OFC representations.

Acceptance criteria from MECH-263 functional signatures (devaluation
sensitivity, task-role discrimination).

### Phase 8: low-priority V3 finishing + V4 deferrals

V3-scope completion items (do when other phases idle):

* GAP-9 SD-033c / SD-033d / SD-033e graph-consolidation -- **DONE 2026-06-09**
  (registration-finishing under the SD-033 cluster; V3-scope, no experiment,
  no substrate). SD-033c subsumption of existing ARC-035 / MECH-151 / MECH-152
  / MECH-235 is now an explicit closed bidirectional edge (`subsumes:` on
  SD-033c + `instantiates: SD-033c` on each source; `consolidation_status:
  complete`). SD-033d design_doc written + linked
  (docs/architecture/sd_033d_premotor_sma_analog.md) mapping the existing E3
  sequence-selection machinery + MECH-090 commitment loop onto premotor / SMA
  biology -- no new substrate. SD-033e V3/V4 boundary made explicit (structured
  `v3_v4_boundary:` field): substrate formally DEFERRED, implementation_phase
  stays v4; the V3-scope forward-compat hook (reserved parallel_goal_deliberation
  mode + keyed-dict MECH-261 gate + no-op frontopolar_analog.py stub) is present
  + complete. Stale `deliberative_branching` doc drift reconciled to
  `parallel_goal_deliberation`. Did not gate any other V3 evidence path.
* GAP-10 StepHarness audit of governance writes: walk SD-034 / MECH-260
  / MECH-268 / SD-033a write sites against canonical sequence after
  Phase 4 / 5 / 6 land. Sibling concern with sleep plan GAP-6;
  efficient to combine the audit pass.

V4 deferrals (genuinely out of V3 scope):

* GAP-6 MECH-260 vs SD-034 No-Go-pulse routing reconciliation: V4
  reconsideration -- route post-completion negative bias through
  SD-033a per-candidate bias projection (lit-pull 2026-04-27
  recommendation). Not blocking V3 work.
* GAP-7 MECH-091 phase-reset: gated on SD-006 phase 2 async heartbeat;
  deferred until SD-006 phase 2 lands or V4 substrate redesign occurs.

---

## Status table

The resume primitive. Updated every session that touches commitment /
closure / mode-governance work. See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | done | (none) | **ROW RECONCILED 2026-07-31 (docs-only): status was `in-progress`, node record has been `done` since 2026-05-29.** V3-EXQ-598b ran 2026-05-27 and confirmed C1 frozen_silent PASS + C2 trainable_nonzero PASS -- the bias head is no longer mechanically silent; SD-033a recorded as supports. The downstream C3 trainable_not_monomodal FAIL is a separate substrate_ceiling tracked under `arc_062_rule_apprehension:GAP-B`, not this gap. GAP-1's narrow scope (head untrained) is RESOLVED. See node `completion_note`. | V3-EXQ-598b | 2026-07-31 (row reconcile; node record 2026-05-29) |
| GAP-2 | 2 | done | none for substrate-readiness; behavioural successor blocked on GAP-3 | Use Phase 3 env extensions for the full behavioural delayed-reward arm | V3-EXQ-461 | 2026-05-12 |
| GAP-3 | 3 | done | (none) | DONE 2026-05-17: env extensions primitives 1-3 IMPLEMENTED; 14/14 contract tests PASS + 434/434 regression. Deliverable 4 (phased curriculum) is GAP-11 (separate). Unblocks GAP-8. | env infra (no EXQ) | 2026-05-17 |
| GAP-4 | 2, 4, 5 | in-progress | **DATE RECONCILED 2026-07-31 (docs-only, no status change): row was frozen at 2026-06-03; node record (`last_updated`) has since advanced to 2026-06-25 across the 460c..460l de-commit-conversion lineage autopsies -- see the node's `governance_2026_06_25`/`resume_condition` for the live frontier.** Phase 4/5 OCD behavioural *b cohort QUEUED 2026-06-03 (awaiting runner) + MECH-342 ecological evidence (V3-EXQ-629 queued) | Phase 4/5 *b cohort (460b/461b/463b/464b/466b/467b/468b) authored+smoke-tested+queued via /queue-experiment (ree-v3 a5afed7, priority 290, seeds 3). 461b (delayed-reward persistence FULL) + 464b (competing goals) newly authored; 460b/463b/466b/467b/468b were staged-not-queued. Runs on GAP-3 env extensions + GAP-11 committed_mode_curriculum. Substrate side already RESOLVED 2026-06-02 (592d->g -> MECH-342 validated by 592g). GAP-4 now tracks the MECH-090/445/446 de-commit-conversion lineage (split 2026-06-23; OCD-battery completeness moved to child node `commitment_closure:GAP-4-battery`, new row below). GAP-4 closes on a contributory PASS of the live owner_exq (see node `resume_condition`). | V3-EXQ-460b..468b (superseded; see node resume_condition for the live 460-lineage frontier) | 2026-08-18 (row reconcile; node record 2026-08-18) |
| GAP-4-battery | 2, 4, 5 | in_progress | commitment_closure:GAP-4, GAP-3, GAP-11 (all satisfied); the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342) are deferred until the BG commitment layer is complete, per the standing don't-queue-commitment-dependent-behavioural rule | **NEW ROW 2026-07-31 -- this child node has existed in the frontmatter since the 2026-06-23 split (surfacing the OCD-battery-completeness half of GAP-4) but was never added to this table.** V3-EXQ-466e RAN PASS/supports 2026-06-25 (satisficing/residue-discharge leg; supersedes 466d) -- SD-034 records a clean supports for that leg. Node stays `in_progress` as battery-incomplete (the commitment-dependent MECH-266/267/268/342 arms remain blocked-on-upstream), NOT as discharge-arm-pending. owner_exq: V3-EXQ-629c queued 2026-07-21 (MECH-342 ecological maintenance-release retest, supersedes 629b; gate-cleared per its own queue note). | V3-EXQ-466e (PASS, reviewed) / V3-EXQ-629c (queued) | 2026-08-18 (row reconcile; node record 2026-08-16) |
| GAP-5 | 6 | done | (none) | Two root causes fixed: (1) forced commitment pattern for 481b; (2) empty-snapshot re-population in agent.py. V3-EXQ-481b queued 2026-05-17; dry-run UC1/UC2/UC3 PASS. | V3-EXQ-481b | 2026-05-17 |
| GAP-6 | 8 | deferred V4 | post Phase-4 PASS; lit-pull 2026-04-27 V4 reconsideration | none in V3 | n/a | 2026-05-08 |
| GAP-7 | 8 | blocked | substrate_queue MECH091-SALIENT-EVENT-TRIGGER-WIRING (V3, buildable now) | **ROW RECONCILED 2026-08-18 (docs-only): status was `deferred V4` (frozen since 2026-05-08); the node's 2026-08-16 /governance cycle (GFLAG-0037, session cranky-driscoll-126a36) decided the generation question this row's own "SD-006 phase 2 async heartbeat" blocker begged, and SPLIT it -- MECH-091 -> V3 as a small buildable (this node, now `blocked`, entering the V3 denominator), true concurrency (SD-006 phase 2 proper) -> V4 (not tracked by this node). MECH-091's phase_reset() is already built + wired; only 2 of the 3 salient-event triggers (task completion, commitment-boundary crossing) remain unwired -- registered as substrate_queue MECH091-SALIENT-EVENT-TRIGGER-WIRING, priority 2. See the node's `governance_2026_08_16` note for the full decision rationale and the measured closure delta.** **Prior row text (2026-05-08, retained for reconstruction):** none in V3 unless SD-006 phase 2 lands. | MECH091-SALIENT-EVENT-TRIGGER-WIRING (substrate_queue, not yet run) | 2026-08-18 (row reconcile; node record 2026-08-16) |
| GAP-8 | 7 | assembling | nothing on 485b/485c (both RAN PASS 2026-06-03, reviewed). Node awaiting `conversion_ceiling_campaign:FULLSTACK` (assembly_status=built; the decoupled devaluation_bias_head is built, ree-v3 758956f) | **ROW RECONCILED 2026-07-29 (docs-only) — this row had been frozen at 2026-06-03 while the node record advanced eight times.** Current node state (frontmatter `governance_2026_06_23`): status `assembling`; the owner frontier ran 485b/485c -> 485d -> 485e -> ... -> 485k, all superseded/non_contributory, and 485m's CONFIRMED autopsy face-validated the OFC valuation face and FOLDED it into `conversion_ceiling_campaign:FULLSTACK` (use_ofc_devaluation_head ON); the re-derive brake REFUSES an isolated 485n, so this node's resolution path is the campaign's full-stack arm, not another isolated behavioural letter. SD-033b / MECH-263 UNWEAKENED (candidate / substrate_conditional / pending_retest_after_substrate). REOPEN on the FULLSTACK run. **Superseded row text (2026-06-03, retained for reconstruction):** "Awaiting runner for 485b/485c. DONE 2026-06-03: audited 485b/485c = NEVER ran (no manifest/runner_status/git/coordinator rows; prior "queued" note was aspirational). Authored+smoke+queued both as representation-level MECH-263 functional-signature diagnostics (ree-v3 main 9f45b0f; 485b 3/3 + 485c 4/4 PASS at smoke). OFC reads only z_world+z_harm -> appetitive SD-049 satiety + GAP-3 counter-evidence invisible to state_code; 485b uses aversive devaluation, 485c same-z_world/diff-task-stage. On PASS -> GAP-8 PARTIAL (full done still needs trained-OFC-head behavioural arm, parallel SD-033a GAP-1)." — that PASS duly arrived (485b supports 3/3, post-onset divergence 0.105; 485c supports, separation_ratio ~297; both reviewed), which is what makes the "NEVER ran" wording read backwards today. | V3-EXQ-485k (frontier; 485b/485c/485d-j preserved as [HISTORY]); awaits `conversion_ceiling_campaign:FULLSTACK` | 2026-07-29 (row reconcile; node record 2026-06-23) |
| GAP-9 | 8 | done | low-priority graph completeness | none in V3 | n/a | 2026-06-09 |
| GAP-10 | 8 | done | (none) | Audit complete: 6 write sub-sites documented in sd_034_governance_closure_operator.md; all are within-select_action() architectural exceptions; zero require StepHarness re-routing | substrate audit (no EXQ) | 2026-05-17 |
| GAP-11 | 4 | done | (none) | DONE 2026-05-17: committed_mode_curriculum.py harness helper IMPLEMENTED; P0/P1/P2/clone_trained_agent API; smoke PASS. Pilot EXQ V3-EXQ-592 queued (3 arms: EMERGENT/FORCED_RV/STARVED). | V3-EXQ-592 | 2026-05-17 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `partial`,
`done`, `deferred`. A `paused` row carries a resume condition in the
[Decision log](#decision-log).

---

## Test cohort

The OCD test battery from [sd033_governance_plan.md SD-033 test
battery](./sd033_governance_plan.md#sd-033-test-battery-ocd4-table) is the
primary falsification cohort for this plan. Sub-plan: that document
remains the canonical OCD-axis breakdown. This plan tracks battery
completeness as a status concern.

### Battery state (2026-05-21)

| Reserved EXQ | Proposal | Subject | Status (proposal) | Status (script / evidence) |
|---|---|---|---|---|
| V3-EXQ-460 | EXP-0156 | SD-034 verified-but-not-released | executed (sd033 CHK-SD034) | script + PASS x2 (2026-04-21); queue consumed |
| V3-EXQ-461 | EXP-0157 | MECH-090 + SD-033a + SD-034 delayed-reward persistence | executed | script + PASS reviewed 2026-05-12; queue consumed |
| V3-EXQ-462 | EXP-0158 | MECH-267 rule binding | executed | script + PASS (2026-04-21); queue consumed |
| V3-EXQ-463 | EXP-0159 | MECH-268 dACC conflict saturation | executed (substrate landing) | script + PASS (2026-04-21); queue consumed |
| V3-EXQ-464 | EXP-0160 | MECH-266 competing goals | executed (substrate landing) | script + PASS (2026-04-21); queue consumed |
| V3-EXQ-465 | EXP-0161 | MECH-267 intrusive simulation filtering | executed | script + PASS (2026-04-21); queue consumed |
| V3-EXQ-466 | EXP-0162 | SD-034 satisficing / residue discharge | executed (substrate landing) | script + PASS x2 (2026-04-21); queue consumed |
| V3-EXQ-467 | EXP-0163 | MECH-266 mode stickiness | executed (substrate landing) | script + PASS (2026-04-21); queue consumed |
| V3-EXQ-468 | EXP-0164 | SD-034 + MECH-268 commitment vs contradiction | executed (substrate landing) | script + PASS (2026-04-21); queue consumed |

**Phase 2 acceptance (substrate battery):** met 2026-05-21 -- all nine scripts
authored; all latest manifests `result: PASS` at substrate-readiness level.

**Phase 4/5 gate (UPDATED 2026-06-02):** The substrate prerequisite is now
satisfied. The MECH-090 commit-entry conjunction validation chain
(V3-EXQ-592 -> 592b -> 592c -> 592d -> 592e -> 592f -> 592g) resolved
2026-06-02: 592f (FAIL_NO_RELEASE_AUTHORITY) + the B3b release-path audit
surfaced that MECH-090 had no decommit authority; the new MECH-342
maintenance-release substrate supplies it and 592g PASSed all six criteria
validating it. The Phase 4/5 behavioural arms (460b, 461 full, 463b, 464b,
466b, 467b, 468b -- require GAP-3 env primitives + `committed_mode_curriculum.py`,
both DONE) are now UNBLOCKED on the substrate side and are the immediate
next /queue-experiment action.

**Full GAP-4 closure:** Phase 2 (done) + commit-entry/release substrate
validated (done 2026-06-02 via 592g + MECH-342) + Phase 4/5 behavioural *b
cohort PASS on env extensions (UNQUEUED) + MECH-342 ecological evidence to
clear v3_pending (**UNQUEUED** -- the 629/629b lineage both RAN and both
FAILed `non_contributory`; the retest is gated on the
`scaffolded_sd054_onboarding` nav-competence leg clearing >=2/3 seeds in the
ecological harness. V3-EXQ-631 was a phantom duplicate ID for 629 and has no
evidence -- see `governance_2026_07_21`).

### Other relevant EXQs

| EXQ | Subject | Status | Plan reference |
|---|---|---|---|
| V3-EXQ-049a / 049e / 062b / 321b | MECH-090 BetaGate bistable validation | PASS | foundational; not part of OCD battery |
| V3-EXQ-445h | SD-032b dACC reef + MECH-258/260 supports | PASS (per-claim) | MECH-260 first clean supporting evidence |
| V3-EXQ-481 | MECH-090 V_s -> commit-release substrate-readiness | FAIL (inconclusive) | GAP-5 / Phase 6 |
| V3-EXQ-485 / 485a | SD-033b OFC substrate readiness + oracle round-trip | PASS / queued | GAP-8 / Phase 7 |
| V3-EXQ-485b / 485c | SD-033b OFC MECH-263 functional signatures (devaluation sensitivity / task-role discrimination; representation-level) | **PASS / supports both** (ran 2026-06-03T20:10Z; 485b post-onset divergence 0.105 supports 3/3, 485c separation_ratio ~297 + z_world match 1.0; both reviewed 2026-06-04) | GAP-8 / Phase 7 |
| V3-EXQ-456 | SD-033a substrate-landing diagnostic | (per substrate_queue) | GAP-1 / Phase 1 baseline |
| V3-EXQ-592 / 592b / 592c / 592d | MECH-090 commit-entry conjunction (curriculum pilot -> 4-arm validation) | FAIL/superseded chain (592d non_contributory, measurement defect) | GAP-4 / Phase 2,4,5 |
| V3-EXQ-592e | MECH-090 conjunction, C1-baseline fix attempt | FAIL does_not_support (2026-06-01) | GAP-4; superseded by 592f |
| V3-EXQ-592f | MECH-090 commitment-state transition probe (controlled state-machine) | FAIL non_contributory (substrate_ceiling); FAIL_NO_RELEASE_AUTHORITY -> spawned MECH-342 | GAP-4 |
| V3-EXQ-592g | MECH-342 maintenance-release validation probe | PASS supports (6/6 criteria, 2026-06-02) | GAP-4; MECH-342 candidate/v3_pending |
| V3-EXQ-629 | MECH-342 maintenance-release ecological evidence | FAIL non_contributory (2026-06-02; claim_ids []) | GAP-4; would clear MECH-342 v3_pending |
| V3-EXQ-629b | MECH-342 maintenance-release ecological evidence (retry) | FAIL non_contributory (2026-06-12; MECH-342). Upstream foraging incompetence, NOT a MECH-342 defect -- contact-guard held on 1/3 seeds; on the competent seed 43 MECH-342 FIRED correctly | GAP-4; retest UNQUEUED, gated on `scaffolded_sd054_onboarding` nav-competence >=2/3 seeds |
| ~~V3-EXQ-631~~ | (phantom) MECH-342 maintenance-release ecological follow-on | **NEVER EXISTED** -- duplicate ID minted 2026-06-02 by a parallel session for the same experiment as 629; no queue entry, no script, no manifest | see `governance_2026_07_21` |

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 | SD-033a (priority=2, implemented) | SD-033a, MECH-262 | docs/architecture/sd_033a_lateral_pfc_analog.md |
| GAP-2 / Phase 2 | (no separate entry; OCD battery sub-plan) | MECH-090, SD-033a, SD-034 | sd033_governance_plan.md |
| GAP-3 / Phase 3 | (env infra, no claim) | n/a | docs/architecture/causal_gridworld_v2.md (to be authored) |
| GAP-4 / Phase 2, 4, 5 | SD-034, MECH-266, MECH-267, MECH-268 (all priority=2, implemented) | SD-034, MECH-266, MECH-267, MECH-268 | sd033_governance_plan.md |
| GAP-5 / Phase 6 | (no separate entry; cross-link to MECH-269 / MECH-284 / MECH-287 V_s cluster) | MECH-090, MECH-269, MECH-284 | docs/architecture/control_plane_heartbeat.md, docs/architecture/v_s_invalidation_runtime.md |
| GAP-6 / Phase 8 | (V4 flag, no entry yet) | MECH-260, SD-034, SD-033a | sd033_governance_plan.md (V4 reconsideration note) |
| GAP-7 / Phase 8 | (held on SD-006 phase 2) | MECH-091 | docs/architecture/control_plane_heartbeat.md |
| GAP-8 / Phase 7 | SD-033b (priority=2, implemented) | SD-033b, MECH-263 | docs/architecture/sd_033_pfc_subdivision_architecture.md |
| GAP-9 / Phase 8 | SD-033c, SD-033d, SD-033e | SD-033c, SD-033d, SD-033e | docs/architecture/sd_033_pfc_subdivision_architecture.md |
| GAP-10 / Phase 8 | (no entry; audit) | (audit, no claim) | shared with sleep_substrate_plan.md GAP-6 |

The substrate_queue.json edits to update `design_doc` fields for SD-034,
MECH-266, MECH-267, and MECH-268 to point at this plan are made in the same
session as plan registration (see [Decision log](#decision-log)).

---

## Cross-link with sleep plan

[sleep_substrate_plan.md](./sleep_substrate_plan.md) and this plan share
two load-bearing claims:

1. **MECH-094 hypothesis-tag generalisation by MECH-261 mode-conditioned
   write-gate registry.** Sleep plan's GAP-3 (Phase B-E flags default-False)
   and GAP-6 (StepHarness audit) both ride on MECH-094 / MECH-261 staying
   the canonical write-gate primitive across waking and offline phases.
   This plan inherits the same primitive as the closure operator's mode-
   conditioning gate (SD-034 closure blocked in `internal_replay` /
   `offline_consolidation` modes).

2. **Captured-but-unread signal pattern.** Sleep plan GAP-1: MECH-204
   `precision_at_rem_entry` captured at REM entry, never read by any
   consumer. This plan GAP-5: MECH-090 `_committed_anchor_keys` captured
   at commit entry; V_s release predicate never matches. Same architectural
   smell, different substrate.

3. **StepHarness audit (GAP-10 here, GAP-6 in sleep plan).** Combine into
   one audit pass when either plan reaches Phase 5 / Phase 8 -- governance
   write sites and sleep-period write sites both want the same canonical
   `sense / update_z_goal / update_residue` discipline.

Sessions that touch *both* plans (e.g. closure-during-sleep questions, or
V_s read-path work) should update the [Status table](#status-table) on
both this plan and the sleep plan.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-07-29 - GAP-8 reconcile: the row still said 485b/485c "NEVER ran"; they had run and PASSED, and the frontier has since moved eight letters on

**Docs-only. No experiments queued, no claims.yaml edit, no manifest touched.**

The GAP-8 Status-table row was frozen at 2026-06-03, when an audit had correctly
found that V3-EXQ-485b/485c were never queued (the prior "queued 485b/c" note
having been aspirational) and had authored + smoke-tested + queued both. The row
recorded that audit finding -- "audited 485b/485c = NEVER ran" -- and then never
recorded the sequel. **They ran the same day** (2026-06-03T20:10Z) and both
PASSED: 485b devaluation sensitivity, supports 3/3, post-onset divergence 0.105;
485c task-role discrimination, supports, separation_ratio ~297, z_world match
1.0. Both were reviewed 2026-06-04. Read cold today, the row asserts the exact
opposite of what happened.

The node record, by contrast, is current and has advanced eight times since
(485d -> 485e -> ... -> 485k, plus the 485m autopsy). Per
`governance_2026_06_23` the node is now `assembling`, not `in-progress`: 485m's
confirmed autopsy face-validated the OFC valuation face and folded it into
`conversion_ceiling_campaign:FULLSTACK` (`use_ofc_devaluation_head` ON), and the
re-derive brake REFUSES an isolated 485n -- so the resolution path is the
campaign's full-stack arm, not another isolated behavioural letter. The row was
brought into line with that, with the 2026-06-03 text retained verbatim for
reconstruction. SD-033b / MECH-263 are unweakened and unchanged (candidate /
substrate_conditional / pending_retest_after_substrate).

Also corrected: the gap-description table said GAP-8 had "no behavioural EXQ
queued" (its env blocker GAP-3 landed 2026-05-17), and the experiment table
listed 485b/485c as "queued 2026-06-03 (smoke PASS)" rather than as the PASSes
they became.

### 2026-06-03 - GAP-4: Phase 4/5 OCD behavioural *b cohort authored + queued (460b/461b/463b/464b/466b/467b/468b)

The substrate side of GAP-4 was resolved 2026-06-02 (MECH-090 commit-entry +
the new MECH-342 maintenance-release substrate, validated by V3-EXQ-592g). The
remaining owed work was the Phase 4/5 OCD behavioural `*b` cohort. This session
queued it.

**Cohort re-derivation (the plan's candidate IDs were corrected).** The plan
named `460b, 461 (full), 463b, 464b, 466b, 467b, 468b`. Investigation showed:
five `*b` scripts (460b/463b/466b/467b/468b) already existed but were committed
`staged, not yet queued` and had never run (confirmed absent from every
`runner_status/*.json`); and `461 full` / `464b` did not exist. Because bare
`461` was a substrate-readiness diagnostic (superseded by the GAP-11 pilot
V3-EXQ-592) and bare `464` had already run, the full behavioural versions take
new letters: **461b** and **464b**, both newly authored this session.

- **461b** (MECH-090 + SD-033a + SD-034, delayed-reward persistence, full
  behavioural): in a live committed_mode_curriculum loop, measures that the
  SD-033a rule_state PERSISTS across the MECH-090 Hold window and that SD-034
  closure fires within 2 ticks of the delayed RESOLUTION (beta release), with a
  no-Hold (bistable-OFF) contrast. Modeled on 460b.
- **464b** (MECH-266, competing goals): dual-cue env (SD-049) + symmetric
  (legacy MECH-259) vs asymmetric per-mode exit rails; measures switch-cost
  asymmetry (sticky exit rail raises external_task occupancy + suppresses
  switches). Modeled on 467b.

All seven: smoke-tested (exit 0; wiring confirmed -- smoke PASS/FAIL is
meaningless at the 3-episode dry-run budget), pass the `emit_outcome` AST
contract, ASCII-clean, correct `_v3`/epoch/outcome/`evidence_direction_per_claim`
fields. Queued at priority 290, machine_affinity any, seeds 3, on the GAP-3
CausalGridWorldV2 env extensions + GAP-11 committed_mode_curriculum (O-2
forced-rv mandatory contrast included).

**Concurrency deviation (pause/resume).** Three sessions held active claims on
`ree-v3/experiment_queue.json` simultaneously (gap7-l1-626b with `V3-EXQ-626b`
uncommitted in the shared working tree; gap8-sd033b-485bc; and this GAP-4
session). Per the CLAUDE.md no-silent-overwrite rule the conflict was surfaced
to the user, who chose to pause the queue write and serialize. Once gap7
committed 626b (working tree clean), the cohort was appended on top (preserving
626b) and landed: ree-v3 `a5afed7`, pushed origin/main. The 461b/464b scripts
were committed atomically with their queue entries via a pathspec-limited
commit; the foreign untracked scripts (598c/610e) and modified 626a were left
untouched.

**Status:** GAP-4 stays `in-progress`; it closes when the `*b` cohort PASSes
(plus V3-EXQ-629 PASS clears the MECH-342 v3_pending evidence side).

### 2026-06-03 - GAP-8: SD-033b behavioural validation un-stuck; 485b/485c authored+queued as representation-level MECH-263 signatures (aversive-devaluation + task-stage instruments)

GAP-8 was carried as `blocked` with next-action "After Phase 3 PASS, queue
485b/c" and owner `V3-EXQ-485b, 485c`. The blocker (GAP-3 env extensions) had
in fact landed 2026-05-17, so GAP-8 was already unblocked. An audit of 485b/485c
found they were **never queued and never ran**: no manifests in
`evidence/experiments/` (only 485 + 485a exist), no `runner_status` rows on any
host, no git history of the IDs in `ree-v3/experiment_queue.json`, and no
`experiments`/`results` rows in the coordinator DB. The "queued 485b/c" language
was aspirational, not a record of a run -- so this is NOT a manifest silent-drop
(no completion row + zero results); it is case (c) never-claimed, and the IDs
were reusable.

**Substrate finding that reshaped the instruments.** `OFCAnalog.update(z_world,
z_harm, gate)` reads only `z_world` and (when `harm_dim>0`) `z_harm` -- it has
**no appetitive value / drive / benefit input**. The originally-imagined SD-049
sensory-specific-satiety instrument (and the GAP-3 counter-evidence primitive,
which mutates only committed-target reward-validity and leaves observations
invariant) are therefore **invisible to the OFC state_code**. The faithful
realizations given the OFC's actual inputs:

- **V3-EXQ-485b** (MECH-263 sig a, devaluation sensitivity): an AVERSIVE outcome
  devaluation -- `z_harm` dropped (threat removed) at a fixed `z_world` state,
  matched DEVALUE-vs-CONTROL arms, measure state_code divergence onset within
  bounded EMA ticks. Smoke: 3/3 seeds PASS (ticks_to_div 9-18 < 20).
- **V3-EXQ-485c** (MECH-263 sig b, same-sensory / different-task-role): two
  distinct task-context `z_world` histories converging on a byte-identical
  matched final input; state_code separability vs within-context jitter. NOT the
  GAP-3 dual-cue primitive (its cues are perceptually DISTINCT). Smoke: 4/4 reps
  PASS (separation ratio 67-297 >> 3).

Both are **representation-level** (`experiment_purpose=diagnostic`, claim_ids
`[SD-033b, MECH-263]`), in the same direct-drive style as the PASSed 485/485a.
The OFC **bias head is frozen-random with last layer zeroed (untrained)**, so
behaviour-change is not measurable here -- FULL SD-033b candidate->provisional
promotion still needs the deferred trained-OFC-head behavioural arm (the
phased-training protocol, parallel to SD-033a GAP-1). On 485b/c PASS, GAP-8
advances to **partial**, not fully done. Landed ree-v3 main 9f45b0f.

### 2026-06-02 - GAP-4: MECH-090 commit-entry/release validation chain RESOLVED; MECH-342 release substrate registered + validated (592d->g)

The 4-arm conjunction validator V3-EXQ-592d FAILed 2026-05-31 and was
diagnosed (2026-06-01) as a C1-baseline measurement defect, not substrate
falsification. The redesign chain that followed produced a more important
finding than the original test was after:

- **592e** (C1-baseline fix, force-uncommitted P2 entry) FAILed
  `does_not_support` 2026-06-01T18:09Z.
- **592f** (controlled state-machine probe, supersedes 592e) forced
  `score_margin=0.01` (< floor 0.05) and `nav_readiness=0.0` (< floor 0.3)
  while beta was forced elevated and the E3 committed pointer forced present.
  It produced **zero state-occupancy suppression and zero decommit
  transitions** -- tag `FAIL_NO_RELEASE_AUTHORITY`. Together with the B3b
  release-path audit (all four candidate release pathways = NO; commits
  `e00c8e0f96` + `b20ea959b8`) this established that **MECH-090 governs
  commit ENTRY soundly but carries NO release/decommit authority** -- the
  capability was simply absent from the substrate, not mis-measured.
- That gap spawned **MECH-342** (maintenance-time release substrate).
- **592g** (MECH-342 maintenance-release validation probe) PASSed all six
  criteria 2026-06-02T16:35Z: with MECH-342 enabled, degraded execution
  readiness under elevated beta now yields >=1 decommit transition per fail
  stage (the quantity 592f measured as zero), suppression 0.4-0.6,
  `mech342_fires` 1/stage, C4 conjunction strictly-positive at 0.6 (592f had
  passed C4 only vacuously at 0), no false abort in A/E.

Governance disposition (REE_assembly master `01144f9bf6`, 2026-06-02T17:57Z):
MECH-090 stays `active`, unchanged; its `pending_retest_after_substrate`
cleared ("reach gap closed") since the release capability now lives on
MECH-342. MECH-342 registered **candidate / v3_pending** -- 592g is a
diagnostic state-machine probe, not ecological evidence, and the V3-pending
gate forbids promotion. 592f re-tagged `does_not_support -> non_contributory`
(epistemic_category `substrate_ceiling`). `substrate_queue` MECH-342 ->
`implemented_validated_v3_exq_592g`.

**Effect on GAP-4:** the commit-entry/release *substrate* side is now
resolved. GAP-4 stays `in-progress`; the remaining work is (a) MECH-342
ecological evidence to clear v3_pending -- as of 2026-07-21 still **UNQUEUED**:
the V3-EXQ-629 -> 629b maintenance-release runs both executed and both FAILed
`non_contributory` (629b's failure is upstream foraging incompetence, not a
MECH-342 defect), and the retest is gated on the `scaffolded_sd054_onboarding`
nav-competence leg clearing >=2/3 seeds in the ecological harness. (This
paragraph originally named V3-EXQ-631 as a queued follow-on; 631 was a phantom
duplicate ID for 629 and never existed -- see `governance_2026_07_21`.);
(b) the Phase 4/5 OCD
behavioural *b cohort (460b, 461 full, 463b, 464b, 466b, 467b, 468b), still
UNQUEUED -- the immediate next /queue-experiment action, on the already-done
GAP-3 env primitives + GAP-11 committed_mode_curriculum. owner_exq advanced
V3-EXQ-592d -> V3-EXQ-592g; status-table, gap-inventory, one-line framing,
and Phase 4/5 gate rows updated to match.

### 2026-05-28 - GAP-4: MECH-090 R-c commit-entry readiness conjunction substrate LANDED; V3-EXQ-592b queued (IGW-20260528-013)

V3-EXQ-592 seed 42 surfaced the rv-only commit-entry pathology
(`running_variance=2.7e-5` with `nav_competence=0.0` -- agent satisfied the
predicate by becoming trivially predictable in a degenerate near-fixed-point
basin, not by becoming competent). Predecessor lit-pull session
`lit-pull-commit-predicate-mech090-sd034-20260528T170025Z` wrote the synthesis
at [synthesis.md](../literature/targeted_review_connectome_mech_090/synthesis.md)
(commit `9e68c5ca8a`), dispositioning the three live readings:

- R-a (rv-only correct; V3-EXQ-592 is curriculum problem) -- NOT defensible
  against the post-pass corpus.
- R-b (rv-only entry + separate downstream propagation gate; Tandetnik 2021) --
  conservative; retained as fallback if validation fails.
- R-c (single-gate conjunction rv_low AND readiness>=floor; Cisek-Kalaska 2010
  + Hanes-Schall 1996 + Roesch-Calu-Schoenbaum 2007) -- strongest reading.

User selected R-c + per-candidate first-action score-margin readiness signal
+ new mech_090_commit_entry_predicate.md design doc + V3-EXQ-592b 2-arm
falsifier-grade validation via AskUserQuestion at the implement-substrate
design-plan step.

Substrate landed:

- `ree-v3/ree_core/heartbeat/beta_gate.py` -- `BetaGate.should_admit_elevation(
  score_margin, n_candidates)` predicate; new `__init__` kwargs
  `use_commit_readiness_gate` / `commit_readiness_floor` /
  `commit_readiness_strict_single_candidate`; `get_state` + `reset` extended
  with `mech090_n_elevation_admitted` / `_blocked` / `_single_candidate` /
  `_last_readiness_score_margin` diagnostics.
- `ree-v3/ree_core/agent.py` -- `REEAgent.__init__` forwards the three knobs
  via `getattr` fallback (default False). Both `beta_gate.elevate()` call
  sites in `select_action` (bistable branch; legacy branch) compute
  `_readiness_margin = sorted(scores)[1] - sorted(scores)[0]` once and
  guard with `should_admit_elevation`.
- `ree-v3/ree_core/utils/config.py` -- 3 new no-op fields on `HeartbeatConfig`.
- NOT modified: `ree-v3/ree_core/predictors/e3_selector.py` (rv-only
  `committed` signal stays as-is; gate layered on top). This was the
  load-bearing concurrency-safety choice -- the MECH-341 retune session
  (`implement-substrate-mech-341-retune-20260528T165000Z`) holds
  `e3_selector.py` with a 6-arm sweep + `stratified_select` call-site
  expansion under way.

Backward-compat: 506/506 contracts PASS with master OFF (regression-clean
2026-05-28). 7 BetaGate primitive unit tests PASS (default no-op, gate
admit / block, single-candidate permissive / strict, reset clears,
backward-compat elevate/propagate/release).

Validation experiment V3-EXQ-592b queued as 2-arm falsifier:

- **ARM_0 GATED:** `use_commit_readiness_gate=True`, `floor=0.05`, same env
  + seed 42 as V3-EXQ-592. Acceptance: `total_committed_steps == 0` AND
  `mech090_n_elevation_blocked >= 1` AND `running_variance <
  commitment_threshold` at some point during the run.
- **ARM_1 GATED_FORCED_READY:** Same gate config; experiment script
  artificially injects `score_bias` to ensure margin >= 0.10. Acceptance:
  `total_committed_steps > 0` AND `mech090_n_elevation_admitted >= 1`.

Joint PASS = GAP-4 substrate side resolved; remaining work is Phase 4/5
behavioural arms (*b cohort 460b/461/463b/464b/466b/467b/468b). Status
flipped `partial` -> `in-progress` pending V3-EXQ-592b PASS; on joint PASS
flip to `done` once Phase 4/5 cohort completes.

Design doc: [mech_090_commit_entry_predicate.md](../../docs/architecture/mech_090_commit_entry_predicate.md).
`claims.yaml` MECH-090 `implementation_note` extended with R-c amendment
section + `evidence_quality_note` extended with V3-EXQ-592 motivating
finding. Out-of-scope follow-on surfaced: V3-EXQ-612 has a colliding ERROR
completion record blocking `test_queue_schema_valid` -- spawned as a
separate chip task.

### 2026-05-21 - V3-EXQ-592 re-queued after accidental dequeue (IGW-20260521-008)

Audit: `V3-EXQ-592` was appended 2026-05-17 (`717d1c3`) then removed by cloud
`queue: remove completed/failed items` (`916d0ef`, 2026-05-21) with **no**
`runner_status.json` entry and **no** manifest under
`evidence/experiments/v3_exq_592_gap11_pilot_committed_mode_curriculum/`. Script
and `validate_experiments` contract OK; dry-run smoke exit 0 (2026-05-21).

Re-queued on `ree-v3/main` with `priority: 3`, `machine_affinity:
DLAPTOP-4.local` (per battery gate). Phase 2 substrate battery unchanged
(V3-EXQ-460..468 latest manifests PASS). GAP-4 remains `partial` until 592
runner PASS + Phase 4/5 *b cohort `/queue-experiment`.

### 2026-05-21 - GAP-4 Phase 2 DONE: OCD substrate battery reconciled (IGW-20260521-008)

Plan-of-record reconcile against repo state (not runner queue -- completed EXQs
are removed from `experiment_queue.json` per queue-completion policy):

- **Scripts:** all nine `ree-v3/experiments/v3_exq_46{0..8}_*.py` present.
- **Evidence:** latest manifest per type `result: PASS` (460/466 diagnostic;
  461 supports MECH-090/SD-033a/SD-034 reviewed 2026-05-12; 462..468
  substrate-landing diagnostics 2026-04-21).
- **Queue:** no V3-EXQ-460..468 entries remain (expected after PASS + auto-sync).
- **Owner:** GAP-4 `owner_exq` -> V3-EXQ-592 (GAP-11 pilot); status stays
  `partial` until 592 PASS and Phase 4/5 *b behavioural cohort is queued.

Staleness corrected: gap inventory still said "unqueued / 461 unauthored";
battery table frozen at 2026-05-12. Phase 2 substrate completeness is now
explicit in YAML `completion_note`, status table, and battery state table.

Next action: monitor V3-EXQ-592 on DLAPTOP-4.local; on PASS, run
`/queue-experiment` for Phase 4/5 behavioural arms (460b, 461 full, 463b,
464b, 466b, 467b, 468b).

### 2026-05-20 - GAP-1 validation EXQ V3-EXQ-598 queued; plan reconciled to 543k gate

Status table was stale (still referenced V3-EXQ-543g as live falsifier). Reconciled:
arc_062 GAP-B owner is V3-EXQ-543k (mode_separation_floor post-543i autopsy); GAP-1
validation is V3-EXQ-598 (2-arm `lateral_pfc_train_rule_bias_head` OFF vs ON on the
ARC-062 + SD-054 bipartite stack with SP-CEM + differential heads). Queue priority 4
(runs after 543k at 5). `depends_on` arc_062:GAP-B added to GAP-1 YAML node.
Interpretation gate: treat 598 as closure evidence only after 543k contributory PASS.
Dry-run smoke: frozen bias silent (C1 PASS); trainable bias moves (C2 PASS); reef
split criterion not met on 3+4+2 ep schedule (C3 FAIL -- full run required).

### 2026-05-17 - GAP-10 DONE: StepHarness write-path audit complete

All 6 governance write sub-sites audited against the StepHarness canonical sequence
(`sense → update_z_goal → select_action → env.step → update_residue`). Full findings in
`sd_034_governance_closure_operator.md` under "StepHarness write-path audit (GAP-10)".

Summary: every site is either a within-`select_action()` architectural exception (SD-034 closure
pulse, MECH-260 `record_action` + `inject_nogo`, MECH-268 `reset_outcome_history` +
`reset_episode_pe`, SD-033a `lateral_pfc.update()`) or an experiment-only unit test on a
standalone `DACCAdaptiveControl` object (MECH-268 `record_outcome()` in EXQ-463/EXQ-468). All
prerequisite latent and gate states (`_current_latent` from step 1, `write_gate("sd_033a")` from
step 4) are established before step 7 runs -- no ordering hazard.

One pending item: `dacc.record_outcome()` has no agent-level call site yet. The canonical home
(StepHarness step 10, after `update_residue()`) requires env-level outcome class tagging that
awaits the GAP-3 env extension. Not a routing error; intentional deferral.

Mirrors `sleep_substrate:GAP-6` result (2026-05-15): both clusters find their write sites are
architectural exceptions that cannot and should not call the harness.

### 2026-05-17 - GAP-5 DONE: MECH-090 V_s commit-release audited, fixed, V3-EXQ-481b queued

Root-cause audit of V3-EXQ-481 (vs_commit_release_count=0 in BOTH arms):

**Root cause 1 (primary)**: The 6-episode x 200-step run never crossed the
commitment threshold. `running_variance` (init 0.5) requires a converged E2
world-forward model to fall below `commitment_threshold=0.40`; untrained short
runs don't achieve this. So `beta_gate` was never elevated, `_committed_anchor_keys`
was never set, and the release check block in `select_action()` was never entered.

**Root cause 2 (secondary, empty-snapshot)**: Even if commitment fires naturally
before any BoundaryEvent installs an anchor, `_committed_anchor_keys = set()`
(empty). `set().issubset(anything)` is vacuously True -> `not True = False` ->
predicate never fires. Affects the natural case as well as any race between
commit entry and the first BoundaryEvent.

**Fix 1**: V3-EXQ-481b uses forced commitment (`agent.beta_gate.elevate()` +
manual `_committed_anchor_keys` snapshot from the current active anchor set),
following the EXQ-461 substrate-readiness pattern. The variance-gate blocker
belongs to GAP-11 (phased curriculum), which is separate.

**Fix 2**: Lazy re-population added to `ree_core/agent.py` `select_action()`
(lines 2508-2531 region). If `_committed_anchor_keys` is non-None but empty and
`current_keys` is non-empty while beta is elevated, the snapshot is re-populated.
The release check then runs on the NEXT tick when any of those keys become
inactive. 477/477 contracts PASS.

**V3-EXQ-481b**: Three UCs -- UC1 (ON arm: release fires after anchor
invalidated by hysteresis), UC2 (OFF arm: release silent), UC3 (empty-snapshot
re-population path). Dry-run: all three PASS. Queued 2026-05-17, priority=2,
any machine.

GAP-5 status: open -> done. MECH-090 release-via-V_s pathway is now validated
at substrate-readiness level. Governance evidence requires the full committed-
mode curriculum (GAP-11) to run the behavioural arms.

### 2026-05-17 - GAP-11 design questions O-1..O-5 RESOLVED (user); implementation concurrency-blocked

User resolved all five open design questions; design doc Section 8 is
now the frozen implementation contract:

- O-1 = experiment-harness helper (`experiments/_lib/
  committed_mode_curriculum.py`), NOT a ree_core substrate scheduler.
- O-2 = emergent + forced-`_running_variance` control arm per
  behavioural arm (the contrast is mandatory; ~2x compute accepted).
- O-3 = at most ONE `commitment_threshold` step 0.40->0.45 on the
  easiest env, then ESCALATE as a substrate mis-calibration finding
  (R1). No variance-gate hyperparameter sweep (the R3 hazard).
- O-4 = contract/integration validation per the GAP-3 spec-section-5
  precedent; queued governance EXQ deferred regardless until
  goal_pipeline:GAP-3 releases experiments/ + queue.
- O-5 = pilot arm EXP-0157 / V3-EXQ-461 (delayed-reward persistence).

GAP-11 stays `design_complete`. The next step -- build the harness
helper + run the EXP-0157 pilot -- is deliberately NOT started: it is
concurrency-blocked on the active goal_pipeline:GAP-3 session (holds
`experiments/` + `experiment_queue.json`). Implementation resumes when
that claim clears or via explicit coordination. No code, no substrate
change, claims.yaml untouched this pass.

### 2026-05-17 - GAP-3 deliverable 4 DESIGN PASS COMPLETE: phased rule_state training curriculum (GAP-11 registered)

Design doc + risk analysis written:
docs/architecture/phased_rule_state_training_curriculum.md (Status:
DESIGN -- PENDING IMPLEMENTATION). Registered as plan node GAP-11
(status design_complete, depends_on GAP-3, load-bearing).

Root-cause finding (verified in source): committed mode is gated solely
by `running_variance < commitment_threshold` in e3_selector.py:806
(precision_init 0.5 vs commitment_threshold 0.40, config.py:309-311);
running_variance only crosses under a converged E2 world-forward model,
which the short generic training loops in the OCD-battery experiments
never achieve -> `total_committed_steps = 0` across all seeds/arms
(EXQ-321/261/325). The lone "PASS" (EXQ-321b) scripted the state; not
emergent. Env-side `_sequence_in_progress` adds a navigation-competence
floor on top.

Design: a 3-phase experiment-harness training protocol (NOT a ree_core
substrate scheduler, NOT an oracle rule-cue curriculum -- the retired Q1
trap). P0 world-model + navigation warmup until the variance gate is
crossed on an easy env; P1 staged-difficulty consolidation keyed on the
SD-049 _global_step pattern with a mid-curriculum abort probe (ARC-062
behavioural-divergence-probe precedent); P2 frozen eval. Emergent arm +
forced-commitment control arm (EXQ-125a/321b primitive) to convert the
scripted-only MECH-090 evidence into a controlled contrast. GAP-3
primitive 1 (adaptive tolerance) is the competence-ramp lever;
primitives 2/3 enter only at end-P1/P2.

Existential risk R1: the commit gate may be mis-calibrated vs the
world-model accuracy actually achievable on CausalGridWorldV2 -- in
which case this is a substrate finding, not a curriculum-tuning problem.
The design front-loads the cheap R1 test (easiest-env P0 + ~60%-budget
abort probe) so the >=7 expensive behavioural arms are never launched
until R1 is retired.

Acceptance bar (pre-stated, from substrate_queue SD-021): total_
committed_steps > 100 per eval episode, emergent (no scripted variance /
forced rv), MECH-090 latch holding on the same curriculum, stable
SD-033a ||rule_state|| > 0 satisfying the SD-034 stability predicate.

5 open design questions O-1..O-5 (architecture home; emergent-only vs
emergent+forced; R1 escalation trigger; validation route incl. the
concurrency note that experiments/+queue are held by goal_pipeline:GAP-3;
pilot arm) are surfaced for user decision BEFORE any implementation.
This remains deliberately off the critical path until O-1..O-5 resolve.

### 2026-05-17 - GAP-3 DONE: CausalGridWorldV2 env extensions primitives 1-3 IMPLEMENTED

Implemented via /implement-substrate (plan confirmed by user) in
`ree-v3/ree_core/environment/causal_grid_world.py` as env-only
constructor kwargs -- NO config.py / REEConfig / queue / experiments
touched (the concurrency-safe path; the goal_pipeline:GAP-3 session held
those files, and the spec was deliberately designed env-only to avoid
them).

- Primitive 1 (adaptive tolerance-band completion): 7
  `completion_tolerance_*` kwargs; Chebyshev/Manhattan; hard /
  graded_exp `exp(-d/lambda)`; OFF and frac=0.0 both dynamics
  bit-identical (lockstep-verified). `waypoint+resource` reserved /
  fail-fast (Q-1a default is waypoint-only; no EXP-0156/0157/0162 arm
  needs the resource half -- fail-fast preferred over a silent partial).
- Primitive 2 (counter-evidence = graded contingency degradation):
  6 `counter_evidence_*` kwargs + `_inject_counter_evidence()` cloned
  structurally from the SD-029 injector. Validity decremented toward
  floor while the rule is persistent; committed-target reward scaled by
  validity; context provably untouched (method-level invariant test).
- Primitive 3 (dual-cue): 4 `dual_cue_*` kwargs; rides SD-049; hard
  ValueError if SD-049 off (Q-3a fail-fast); replace_on_early_consume
  default False (invalidate-episode, Q-3b).

Validated by `tests/contracts/test_env_extensions_gap3.py` 14/14 (C1-C5
incl. spec-section-5 integration smoke) + full ree-v3 contract
regression 434/434 (bit-identical OFF confirmed suite-wide). **Deviation
from implement-substrate Step 8 (queue a validation EXQ): NONE queued --
spec section 5 states Phase 3 is env infrastructure with no
claim-validation EXQ, and the concurrency constraint forbade touching
the queue. Validation is the contract test + integration smoke, as the
user explicitly directed.**

GAP-3 status open -> done. This unblocks GAP-8 (`depends_on: GAP-3`).
**Important scoping note:** GAP-3 == the tolerance/counter-evidence/
dual-cue env primitives only. The SD-034 / MECH-266 / MECH-268
*behavioural* arms still need deliverable 4 (phased rule_state training
curriculum -- the V3-EXQ-321/261 committed-mode-elicitation blocker),
which the 2026-05-16 user decision deliberately split into its own
separate design pass (spec section 6). GAP-3 done does NOT by itself
enable the behavioural promotions; it removes the env-primitive blocker.

### 2026-05-16 - GAP-3 env-extension spec sub-questions RESOLVED (lit-pull + engineering)

All six open sub-questions in causalgridworldv2_env_extensions_spec.md
resolved. Biology-grounded via a literature pull
(literature_synthesis_2026-05-16_counter_evidence_generalization_competing_goals.md;
2 new MECH-268 lit entries):

- **Q-2a (load-bearing)**: counter-evidence = **graded contingency
  degradation** (context held constant, dose+duration sweepable), NOT a
  signed perturbation or identity-flip/reversal. Basis: Piquet 2023
  Curr Biol (contingency degradation = action-validity detection,
  vHPC->mPFC) + Dutech 2011 J Physiol Paris (weak/strong
  contradiction-detection asymmetry; sustained regime is the
  discriminating one). Spec section 3 rewritten; this directly shapes
  EXP-0164 (SD-034 vs MECH-268 dACC pe-saturation).
- **Q-1b**: Chebyshev confirmed (grid x/y integral -> Shepard isotropic
  metric; Manhattan rejected) + optional graded_exp kernel added
  (generalization is concave-graded). Basis: Shepard 1987, Marjieh 2024.
- **Q-3b**: invalidate-episode (replace_on_early_consume default flipped
  True->False) -- mid-episode replacement is a reactive-measurement
  confound for MECH-266 mode stickiness.
- **Q-1a/Q-2b/Q-3a** (engineering): waypoint-only tolerance default;
  independent counter-evidence scheduler (not shared with SD-029);
  hard precondition error for dual_cue without SD-049 (fail-fast).

Spec is now decision-complete for primitives 1-3; next step is
/implement-substrate review. Deliverable 4 (phased curriculum) remains a
separate design pass. The MECH-309 falsifier re-issue (V3-EXQ-543e) on
the SP-CEM substrate is independently running (arc_062:GAP-B
in-progress, runner DLAPTOP-4.local).

### 2026-05-16 - Q2 RESOLVED: GAP-3 tolerance-band = ADAPTIVE (user decision); spec primitives 1-3, curriculum split

User decision (surfaced after the closure-map reconciliation same day):

- **Q2 tolerance-band completion default = ADAPTIVE (scaled to env
  size)**, overriding the plan's proposed fixed-window default. The
  SD-034 / MECH-266 / MECH-268 behavioural arms (EXP-0156/0157/0162)
  will be specced against an adaptive `T`. Concrete scaling function +
  per-experiment override in causalgridworldv2_env_extensions_spec.md.
- **Approach = spec primitives 1-3 now** (adaptive tolerance-band /
  counter-evidence injection hook / dual simultaneously-active resource
  cue); **deliverable 4 (phased rule_state training curriculum) split
  into its own design pass** -- it is the V3-EXQ-321 / V3-EXQ-261
  committed-mode-elicitation blocker (substrate_queue SD-021 / SD-022)
  and is the highest-risk piece, kept off the GAP-3 critical path.

GAP-3 `blocking_external` cleared (no longer waiting on a scoping
decision). Status stays `open`: next is spec review then env-infra
implementation of primitives 1-3 (no claim-validation EXQ; env
infrastructure). GAP-3 closure unblocks GAP-8 (SD-033b behavioural
validation, depends_on GAP-3) and the full behavioural arms of
GAP-2 / GAP-4. Q2 open-question entry struck through + marked resolved;
GAP-3 YAML node + status-table row reconciled.

### 2026-05-16 - Closure-map reconciliation: GAP-1 upstream gate (arc_062:GAP-B) cleared by ARC-065 SP-CEM

Staleness pass (status tables 5-8 days behind runner, now V3-EXQ-581).

GAP-1 (SD-033a bias head untrained, load-bearing) is gated through
cross_plan_link arc_062:GAP-A/B/C/D. The load-bearing upstream node
arc_062:GAP-B (CEM-candidate-distinguishability) was reconciled
blocked -> open today: V3-EXQ-567 PASS (supports ARC-065) provides the
support-preserving CEM that lifts candidate support 1.007 -> 2.810 and
natural action entropy 0.012 -> 0.497, satisfying the 2026-05-11
substrate-readiness gate. V3-EXQ-563a / 563c independently confirmed the
E3 rule_bias actuator is wired and live (bias-norm wiring confirmed).

GAP-1 itself stays `blocked`: the bias head is still untrained until the
re-issued MECH-309 falsifier lands on SP-CEM, then GAP-C (route
discriminator to LateralPFCAnalog.update source) and GAP-D (add
rule_bias_head.parameters() to the E3 optimiser) close. But the path is
now substrate-unblocked end-to-end -- GAP-1 is no longer waiting on an
unresolved root cause, only on the sequenced GAP-B -> C -> D execution.
GAP-2 remains done (2026-05-12); its dependant GAP-4 dependency is
therefore satisfied (GAP-4 still needs the OCD-battery EXQ scoping).

### 2026-05-12 - GAP-2 V3-EXQ-461 substrate-readiness PASS reviewed

GAP-2 moved `open -> done` at substrate-readiness level. New script:
`ree-v3/experiments/v3_exq_461_mech090_sd033a_delayed_reward_persistence.py`.
Queue entry: `V3-EXQ-461` (priority 2, machine_affinity any, 5 min) was
auto-picked by DLAPTOP-4.local and PASSed in 2.1s. Manual proposal EXP-0157
updated to `executed` with `reserved_queue_id=V3-EXQ-461`.

Scope decision: this is deliberately the substrate-readiness version of the
ocd4 delayed-reward-persistence row, not the full behavioural delayed-reward
task. It validates the contract that the behavioural successor will need:
MECH-090 delay-window Hold, a weakened/no-Hold passthrough contrast,
SD-033a rule_state persistence under the MECH-261 replay gate, a strengthened
Hold threshold contrast, the sd_033a mode-gate table, and SD-034 terminal
closure release. Dry-run and runner execution both PASSed all six sub-tests
on 2026-05-12. Full delay-to-reward behaviour remains blocked on GAP-3
CausalGridWorldV2 env extensions (delay-to-benefit, tolerance-band
completion, counter-evidence, dual-cue primitives).

Resume condition: none for GAP-2 substrate-readiness. Next work is GAP-3 if
the goal is the full behavioural delayed-reward arm.

### 2026-05-09 - GAP-1 reframed as ARC-062-dependent

Phase 1 deliverable 1 (Q1 training protocol) and deliverable 4 (rule-cue
gridworld) both presupposed an oracle `rule_cue_id` label that the
architecture says doesn't exist (MECH-309: trainers weight rules they do
not invent). Per the rule-apprehension cluster registered 2026-05-08
(MECH-309 / ARC-062 / ARC-063), the rule-creating substrate is ARC-062
(V3 weak reading) / ARC-063 (V4 strong reading), not the env. SD-033a
sits *downstream* of that layer in the apprehension → commitment
pipeline.

GAP-1 reclassified `open → blocked` on `arc_062_rule_apprehension:GAP-A/B`
(parent plan-of-record [arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md)
registered same session). The Phase 1 deliverable list is rewritten so
the bias head is trained jointly with E3 via the existing score-aggregation
gradient path, with the rule signal arriving from ARC-062's discriminator
rather than from an oracle label.

Two preceding lit-pulls 2026-05-09 grounded the architectural decisions:
- Pull A (`targeted_review_arc_062_rule_apprehension/` 8 entries) resolved
  R1 (multi-stream discriminator input), R2 (N=2 heads at Phase 1, V4 caveat
  on continuous mixed-selectivity), R3 (Phase-1 default = score_bias level).
- Pull B (`targeted_review_arc_062_refuge_forage_ecology/` 6 entries)
  resolved R4 (multi-signature tolerance window, PASS rule = at least
  2 of 4 acceptance criteria hold across seeds).

Q1 in [Open questions](#open-questions) is retired by the reframe; joint-
with-E3 via gradient-through-score_bias is the only architecturally honest
option once the rule signal is non-oracle. The plan-doc-default phased-
pre-training option is dropped.

Cross-plan link to `arc_062_rule_apprehension_plan.md` GAP-A / B / C / D
established. Sessions that touch *both* plans should update the
[Status table](#status-table) on both.

### 2026-05-08 - Plan registered

Plan-of-record commitment_closure_plan.md registered. Ten gaps surfaced and
sequenced into eight phases. Sibling sd033_governance_plan.md retained as
the OCD-specific test-battery sub-plan rather than merged: scope overlap
exists but sd033_governance_plan covers (a) the 2026-04-20 GAP MEMO
provenance, (b) lit-pull backlog, (c) the ocd4 test-matrix axis decomposition.
Merging would lose those entry points. Cross-link maintained via [Test
cohort](#test-cohort) and [Source artefacts](#source-artefacts).

substrate_queue.json edits this session: SD-034 + MECH-266 design_doc
redirected from sd033_governance_plan.md to commitment_closure_plan.md.
SD-033b design_doc null -> commitment_closure_plan.md (in scope under
GAP-8 / Phase 7). SD-033c/d/e design_docs null ->
docs/architecture/sd_033_pfc_subdivision_architecture.md -- the
architecture doc IS the substrate spec, which is what design_doc should
point to whether the work is V3-scope or not (correcting an earlier
session draft that used "out of V3 scope" as the rationale; SD-033c/d/e
ARE V3 graph-consolidation work, just lower priority than the active
phases). MECH-267 + MECH-268 lack substrate_queue entries entirely --
flagged in WORKSPACE_STATE for next queue-completeness session.
MECH-204 design_doc retained at sleep_substrate_plan.md. SD-033a
design_doc retained at docs/architecture/sd_033a_lateral_pfc_analog.md.

### 2026-04-21 - MECH-266 asymmetric hysteresis implemented (substrate-prior)

Schmitt-trigger extension to SD-032a SalienceCoordinator. Per-mode
enter/exit threshold dicts; empty -> legacy MECH-259 symmetric. Validation
PASSed: V3-EXQ-464 (EXP-0160) and V3-EXQ-467 (EXP-0163) sub-tests + 5-arm
parametric sweep r in [0.10 .. 2.00].

### 2026-04-20 - SD-034 closure operator implemented (substrate-prior)

ClosureOperator coordinating five sub-signals at rule_state completion:
beta release + targeted No-Go + residue discharge + mode relaxation + PE
reset. Master flag `use_closure_operator` (default False, bit-identical OFF).
Mode-conditioning generalises MECH-094 hypothesis-tag: closure blocked in
internal_replay / offline_consolidation. Validation PASSed: V3-EXQ-460
(EXP-0156) + V3-EXQ-466 (EXP-0162) + V3-EXQ-468 (EXP-0164, coupled with
MECH-268). Lit-pull recommendation 2026-04-27 flagged V4 reconsideration:
route post-completion negative bias through SD-033a per-candidate bias
projection rather than only via MECH-260 action-class FIFO -- captured as
GAP-6 / Phase 8 here.

### 2026-04-20 - MECH-267 mode-conditioned proposals implemented (substrate-prior)

CEM-noise scale on `propose_trajectories` per operating_mode. V3
implementation is mode-conditional exploration *breadth* (CEM std multiplier);
the lit-pull 2026-04-27 recommended additionally modulating look-ahead
*horizon* -- captured as a V4 elaboration. V3-EXQ-462 + V3-EXQ-465
sub-tests PASS.

### 2026-04-20 - MECH-268 dACC PE saturation implemented (substrate-prior)

FIFO outcome-history `f_sat = 1 / (1 + s * max(0, n_rec - g))` (graded
learning-rate adapter, NOT binary cap). Coupling to SD-034: closure.tick()
calls `dacc.reset_episode_pe()`. Validation PASSed: V3-EXQ-463 (EXP-0159) +
V3-EXQ-468 (EXP-0164). Behavioural arms (500+ step sustained outcome /
counter-evidence injection) deferred -- captured as GAP-3 / Phase 3 + Phase 5.

### 2026-04-20 - SD-033a substrate landed; bias head untrained

LateralPFCAnalog with frozen-random last-Linear-zeroed bias head. Initial
score_bias = 0 by construction. Three design alternatives documented (A1
per-candidate vs uniform; A2 frozen-random vs trained; A3 EMA vs recurrent /
synaptic-hold). V3 commits to per-candidate (A1.a). Training protocol
deferred -- the gap that becomes GAP-1 / Phase 1 in this plan.

### 2026-04-19 - MECH-260 dACC FIFO action-class suppression implemented

`DACCAdaptiveControl._action_history` length 8; suppression weight applied
as positive bias (lower-is-better convention -> discourages repeats).
V3-EXQ-445h supports (3/3 seeds). Lit-pull 2026-04-27 V4 reconsideration:
overlap with SD-034 No-Go pulse -- captured as GAP-6.

### 2026-04-10 - MECH-090 BetaGate bistable latch implemented

Gate elevates only on entry to committed state; hippocampal completion
signal triggers release. V3-EXQ-049a / 049e / 062b / 321b PASS. 2026-04-25
V3-EXQ-481 substrate-readiness FAIL on V_s -> commit release pathway --
captured as GAP-5 / Phase 6.

---

## Open questions

Numbered for reference from future sessions.

- **Q1**: ~~SD-033a bias-head training protocol -- joint with E3 vs phased
  pre-training vs frozen until task-conditional trigger?~~ **RETIRED
  2026-05-09.** Resolved by the ARC-062 / MECH-309 cluster reframe: joint-
  with-E3 via gradient-through-score_bias is the only architecturally
  honest option once the rule signal is non-oracle. The phased-pre-
  training-on-rule-cue-curriculum default presupposed an oracle
  `rule_cue_id` label that MECH-309 says cannot exist honestly in REE.
  See [arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md)
  Open Question R1 / R2 / R3 / R4 for the resolved-default values
  (biology-anchored from Pull A + Pull B lit-pulls 2026-05-09).
- **Q2**: ~~Phase 3 tolerance-band completion default -- fixed window
  (T_default ~ 1 step / 1 grid cell) vs adaptive (scaled to env size)?
  Default proposed: fixed window per env config, configurable per
  experiment.~~ **RESOLVED 2026-05-16 (user decision): ADAPTIVE
  (scaled to env size)**, overriding the proposed fixed-window default.
  Rationale: robustness across env sizes; the SD-034 / MECH-266 /
  MECH-268 behavioural arms (EXP-0156/0157/0162) are to be specced
  against an adaptive `T` rather than a hard 1-cell window. Concrete
  scaling function + per-experiment override surface specified in
  [causalgridworldv2_env_extensions_spec.md](./causalgridworldv2_env_extensions_spec.md).
  Approach decision (same session): spec primitives 1-3 now; deliverable
  4 (phased rule_state training curriculum) treated as a separate design
  pass (it is the V3-EXQ-321 / V3-EXQ-261 committed-mode-elicitation
  blocker; substrate_queue SD-021 / SD-022).
- **Q3**: Multi-rule SD-034 -- when multiple rule_states are committed
  simultaneously (e.g. nested goals), is the per-rule closure pulse
  sufficient or does the architecture need a chained / hierarchical
  closure operator? Default proposed: per-rule pulse for V3; chained
  closure deferred to V4 unless behavioural evidence requires it.
- **Q4**: EXP-0157 (Hold-axis) -- delayed-reward window scaling vs
  distractor density: which dimension to vary first? Default proposed:
  scale window first (cleaner falsifier; distractor density couples to
  Phase 5 dual-cue work).
- **Q5**: MECH-260 FIFO recency suppression vs SD-034 targeted No-Go pulse
  -- functional overlap? Lit-pull 2026-04-27 recommended routing post-
  completion negative bias through SD-033a per-candidate bias projection
  rather than only via MECH-260. V3 retains both; V4 reconsideration
  deferred (GAP-6 / Phase 8).
- **Q6**: V_s release predicate (Phase 6) -- relax to "any anchor in the
  committed set inactive" vs "all inactive" vs "anchor-reset rate above
  threshold"? Default proposed: any-inactive; tighten if it produces
  false-release chatter.

---

## Resume ritual

When picking up commitment / closure / mode-governance work after a
deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that was
   `paused` or `in-progress`.
3. If `paused`, find its entry in the [Decision log](#decision-log) and
   confirm the resume condition has fired.
4. If `in-progress`, find the most recent decision-log entry for that
   phase and continue from the last concrete action.
5. Update the row's `Last updated` field and `Status` if it changes.
6. Append a new decision-log entry for any architectural choice made
   during the resumed session.
7. If the work touches the [sleep plan](./sleep_substrate_plan.md) cross-
   link concerns (MECH-094 / MECH-261, captured-but-unread signal,
   StepHarness audit), update both plans' status tables.

Sessions that do NOT touch governance / closure / mode-governance work do
not need to read this document. Sessions that DO touch this work read
this document before any code or experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite
entries die with the session; WORKSPACE_STATE.md is recent-work, not
strategic; substrate_queue.json is granular but does not capture phase
ordering or decision rationale; sd033_governance_plan.md is the OCD-
specific test-battery sub-plan, not the strategic envelope. This document
is the strategic envelope.

---

## See also

- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) -- OCD-specific test-battery sub-plan (sibling)
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) -- sleep substrate plan (cross-link via MECH-094 / MECH-261 + captured-but-unread pattern)
- [evidence/planning/substrate_queue.json](./substrate_queue.json) -- SD-034, MECH-266, MECH-267, MECH-268, SD-033a, SD-033b queue entries
- [docs/architecture/control_plane_heartbeat.md](../../docs/architecture/control_plane_heartbeat.md) -- MECH-090, MECH-091, heartbeat architecture
- [docs/architecture/sd_033_pfc_subdivision_architecture.md](../../docs/architecture/sd_033_pfc_subdivision_architecture.md) -- SD-033 cluster
- [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) -- SD-033a substrate spec
- [docs/architecture/sd_034_governance_closure_operator.md](../../docs/architecture/sd_034_governance_closure_operator.md) -- SD-034 design (backfilled 2026-04-27)
- [docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md](../../docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md) -- GAP MEMO
- [docs/thoughts/2026-04-20_ocd1.md](../../docs/thoughts/2026-04-20_ocd1.md) .. [ocd4.md](../../docs/thoughts/2026-04-20_ocd4.md) -- OCD source thoughts
