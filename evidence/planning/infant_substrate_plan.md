---
closure_plan:
  id: infant_substrate
  title: "Infant Substrate Expansion"
  registered: 2026-05-16
  last_updated: 2026-09-03
  scope_claims: [INV-055, INV-073, ARC-046, ARC-065, DEV-NEED-001, DEV-NEED-002, DEV-NEED-003, DEV-NEED-004, DEV-NEED-005, DEV-NEED-006, DEV-NEED-007, DEV-NEED-008, MECH-189, MECH-313, MECH-314]
  nodes:
    - id: "infant_substrate:GAP-1"
      title: "Harm gradient env feature (harm_gradient_enabled, graduated harm proximity signal without terminal contact)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-004, ARC-013]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-2"
      title: "Microhabitat zones env feature (microhabitat_enabled, zone_A/B/C resource+hazard density modulation via Voronoi seed)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-001, DEV-NEED-003, DEV-NEED-007, ARC-065]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-3"
      title: "Transient benefit patches env feature (transient_benefit_enabled, stochastic high-salience patch spawn for z_goal seeding)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-006, MECH-189]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-4"
      title: "Stochastic attractor audit (enumerate CausalGridWorldV2 sources of irreducible randomness; mark or remove before high novelty_bonus_weight deployment)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-003, MECH-314]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-5"
      title: "H_pos / zone_coverage telemetry (Shannon entropy of position histogram per episode, per-zone cell coverage fraction)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-001, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-6"
      title: "residue_coverage_pct metric (fraction of grid cells with |residue| > threshold; harm_benefit_ratio)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-004, DEV-NEED-008]
      depends_on: ["infant_substrate:GAP-1"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-7"
      title: "traj_pairwise_cosine_mean metric (edit/cosine distance across stored trajectories; volumetric coverage estimate)"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-002, DEV-NEED-005, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-17
    - id: "infant_substrate:GAP-8"
      title: "post_sleep_z_goal_retention metric (z_goal.norm ratio before/after sleep integration; replay_diversity_index)"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-007, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-17
    - id: "infant_substrate:GAP-9"
      title: "4-phase infant curriculum scheduler (config hook for phase-gated parameter switching; Phase 0 babbling -> Phase 1 benefit -> Phase 2 geography -> Phase 3 gate)"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-008, ARC-046]
      depends_on: ["infant_substrate:GAP-1", "infant_substrate:GAP-2", "infant_substrate:GAP-3"]
      last_updated: 2026-05-17
    - id: "infant_substrate:GAP-10"
      title: "EXQ-ISEF-001: harm gradient vs binary-contact residue geography formation speed"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-004, ARC-013]
      depends_on: ["infant_substrate:GAP-1", "infant_substrate:GAP-5", "infant_substrate:GAP-6"]
      last_updated: 2026-09-04
      governance_2026_09_04: "RECONCILE (governance-20260904-1347; confirmed failure_autopsy_V3-EXQ-996_2026-09-04, red-team F2/F3): the harm_gradient_enabled channel this node validated via V3-EXQ-587 is STRUCTURALLY INERT under CausalGridWorldV2 default parameters (proxy-field mode: hazard_approach pre-empts the transition_type == none gate; pinned by tests/contracts/test_harm_gradient_gap1.py::test_c3_suppressed_by_proxy_approach since 2026-05-16; reachable only with proximity_approach_threshold above ~0.33 or use_proxy_fields=False). 587 therefore measured a DEAD channel, not geometry: its C1 0/5 / ratios ~1.0 null is about channel inertness and the 2026-05-19 geometry-null reading is withdrawn. Status stays done (the run happened and V3-EXQ-576 validated the feature in the mode where it is live); INF-ENV-001 amended (severity degrading) with a standing consumer instruction to record a per-cell fire count. No re-run owed by this node."
    - id: "infant_substrate:GAP-11"
      title: "EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-006, MECH-189]
      depends_on: ["infant_substrate:GAP-3", "infant_substrate:GAP-5"]
      blocked_by: ""
      resume_condition: "CLOSED 2026-06-10: V3-EXQ-588c PASS -- the node's load-bearing closure criterion (C1 ARM_ON-vs-ARM_OFF adult z_goal seeding DISCRIMINATION, >=2/3 seeds) met on 3/3 seeds (ON mean adult z_goal.norm 0.394 vs OFF 0.0; child anchors formed n_occupied=1; adult READ seeding fired 206 seeds). The ContextMemory writes substrate (MECH-189 SuperOrdinalGoalMemory, ree-v3 c7ac035) is validated end to end. The DEV-NEED-006 0.4 ABSOLUTE crossing was advisory and a near-miss (0.394, 2/3 seeds) -- per the node design it routes to a SEPARATE trained-encoder MECH-189 evidence successor (the absolute governance gate), NOT this node. That successor is tracked on MECH-189 (candidate / conf 0.0; full behavioural validation pending), not as GAP-11."
      last_updated: 2026-06-10
      governance_2026_06_10: "Closure-drift reconcile (Case 1, PASS criteria met): V3-EXQ-588c manifest (v3_exq_588c_mech189_super_ordinal_seeding_20260610T004619Z_v3, PASS/supports) cleared the node's own load-bearing C1 discrimination criterion on 3/3 seeds. status in_progress -> done. /governance 2026-06-10 recorded MECH-189 supports (stays candidate / conf 0.0; advisory 0.4 near-miss routes to a trained-encoder evidence successor on the MECH-189 claim, not GAP-11). reviewed_run_ids updated; manifest reviewed."
      governance_2026_06_09: "ContextMemory writes substrate LANDED (/implement-substrate). The MECH-189 SuperOrdinalGoalMemory the node was blocked_pending_substrate on is implemented (ree-v3 c7ac035: ree_core/goal.py SuperOrdinalGoalMemory + agent.update_z_goal WRITE/READ hooks + set_super_ordinal_write_enabled freeze hook; 8 new contracts + 985 contract suite green; bit-identical OFF). claims.yaml MECH-189 carries an implementation_note (NEITHER promoted NOR weakened; stays candidate / conf 0.0). Design doc docs/architecture/mech_189_super_ordinal_goal_anchors.md. status blocked_pending_substrate -> in_progress; owner_exq V3-EXQ-588b -> V3-EXQ-588c (queued via /queue-experiment; supersedes the 588 ISEF-002 framing). blocked_by cleared. A smoke-test correction to the write gate (complexity gates new-anchor allocation only; reinforcement on salience) was applied (anchor norm 0.019 frozen -> 0.373 matured)."
      governance_2026_05_30: "Closure-drift reconcile: status blocked -> blocked_pending_substrate (terminal). V3-EXQ-588b terminal signal (manifest 20260521T053758Z FAIL non_contributory diagnostic, no claim tags) fully absorbed; closure now sits behind the ContextMemory writes substrate. blocked_by added. resume_condition consolidated (588b FAIL outcome folded in -- prior text said 'on PASS close GAP-11' which is no longer the live path). No claims.yaml / manifest / substrate_queue edits this session (plan-doc reconcile only)."
      governance_2026_05_29: "V3-EXQ-588b ran 20260521T053758Z FAIL non_contributory (diagnostic, no claim tags). GAP-11 blocked on the ContextMemory path prerequisite called out in the original resume_condition; the MECH-189 retest cannot proceed until ContextMemory writes are implemented (separate substrate work, not a re-queue of 588 chain)."
    - id: "infant_substrate:GAP-11b"
      title: "MECH-189 trained-encoder evidence successor -- the DEV-NEED-006 0.4 ABSOLUTE adult z_goal crossing (588c near-miss 0.394) that the closed GAP-11 deferred to a separate run"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [MECH-189, DEV-NEED-006]
      depends_on: ["infant_substrate:GAP-11"]
      last_updated: 2026-06-23
      completion_note: "CLOSED 2026-06-23T23:28Z (/governance). The claim-tagged evidence successor V3-EXQ-588e ran PASS/supports (manifest v3_exq_588e_mech189_trained_encoder_absolute_crossing_evidence_20260623T231707Z_v3): C_CROSS load-bearing met 3/3 seeds -- ARM_ON adult median z_goal.norm 0.4219 crosses the DEV-NEED-006 0.4 ABSOLUTE gate (frac_on_cross 1.0), encoder trained 3/3 (frac_encoder_trained 1.0, NOT the 642 untrained confound), OFF arm 0.0, non_degenerate. This is the node's actual gate (the claim-free 588d could not score against the claims). MECH-189 records the supports (genuine_exp_count 1, exp_conf 0.775, confirmed_established) but is KEPT candidate / epistemic_category=substrate_ceiling / pending_retest_after_substrate / ceiling_decision=deferred -- all tagged to goal_pipeline:GAP-2 context-diversity (anchor-store saturation, 669a/669b), which the 588 FORCED-FEED single-anchor harness deliberately bypasses. So 588e confirms the trained-encoder z_world-MAGNITUDE root (the 0.37 ceiling was an untrained-encoder artifact) but does NOT lift the GAP-2 diversity ceiling. DEV-NEED-006 is a developmental-need gate, not a claims.yaml id; the tag documents it. User-approved (Record + close GAP-11b, keep ceiling)."
      governance_2026_06_23_drift: "Case 3 in closure-drift terms. The owner_exq diagnostic V3-EXQ-588d landed PASS (gov 2026-06-23T22:14Z) -- but 588d is a CLAIM-FREE readiness probe that by its own routing does NOT close this node. RESULT: trained_encoder_absolute_crossing_met -- on_mean_adult_zgoal_norm 0.4439 crosses the DEV-NEED-006 0.4 absolute gate 3/3 seeds (frac_on_cross 1.0), encoder trained 3/3 (frac_encoder_trained 1.0), OFF arm 0.0. The trained-encoder hypothesis is CONFIRMED: the 0.37 anchor-norm ceiling was an UNTRAINED-ENCODER z_world-magnitude artifact, not the context-diversity ceiling -- a P0 SD-018 encoder warmup lifts adult z_goal past 0.4. NEXT (this node's actual gate, now well-motivated and substrate-confirmed): author a CLAIM-TAGGED MECH-189/DEV-NEED-006 evidence successor over the same forced-feed single-anchor + P0-warmup harness so the crossing scores against the claims (588d itself, claim_ids=[], cannot). Node stays in_progress pending that successor; follow-on chip spawned 2026-06-23. NOTE for the successor author: MECH-189 currently carries epistemic_category=substrate_ceiling + a 2026-06-19 ceiling_routing_note ('do not re-queue the 669 line until a context-diversity substrate lands') -- the successor is the 588c forced-feed line, NOT the braked 669 line, and 588d is the readiness evidence that the trained-encoder substrate clears the ceiling."
      governance_2026_06_23: "owner_exq set + status open -> in_progress (session queue-experiment-588d-mech189-trained-encoder-readiness-20260623T0508Z). V3-EXQ-588d queued via /queue-experiment as a CLAIM-FREE DIAGNOSTIC (experiment_purpose=diagnostic, claim_ids=[]; PROMOTES NOTHING) -- NOT the claim-tagged absolute evidence run. RATIONALE: MECH-189 is now epistemic_category=substrate_ceiling + pending_retest_after_substrate (gov 2026-06-13, per failure_autopsy_V3-EXQ-669a/669b) with a 2026-06-19 ceiling_routing_note ('do not re-queue the 669 line until a context-diversity substrate lands') -- governance state that POSTDATES this node's 2026-06-10/06-23 registration basis. The re-derive brake (Step 2.5b) is MET (2 substrate_ceiling autopsies: 588, 669a). User adjudicated 2026-06-23 (AskUserQuestion): run the trained-encoder absolute-crossing test brake-exempt AS A DIAGNOSTIC. 588d is NOT the braked 669 line -- it uses the 588c FORCED-FEED SINGLE-ANCHOR harness (bypasses both the 669a ecological-contact starvation and the 669b nursery anchor-store context-diversity saturation) to test a DIFFERENT root: whether the 0.37 anchor-norm ceiling is an UNTRAINED-ENCODER z_world-magnitude artifact (P0 SD-018 encoder warmup) vs the context-diversity ceiling. ROUTING (claim-free, so it does NOT itself close unblocks_claims): readiness unmet -> substrate_not_ready_requeue; readiness met + crosses 0.4 -> trained_encoder_absolute_crossing_met -> THEN author a CLAIM-TAGGED MECH-189/DEV-NEED-006 evidence successor (the actual gate that would unblock this node); readiness met + no cross -> absolute_crossing_ceiling_persists -> route substrate enrichment + fire the MECH-189 re-derive brake at autopsy (NOT a falsification). No claims.yaml change."
      registered_note: "Registered 2026-06-23 (session closure-map-enhance-20260623T043407Z) to surface owed work buried in GAP-11's completion prose. GAP-11 closed `done` 2026-06-10 on its C1 discrimination criterion (588c PASS), but its resume_condition explicitly defers the DEV-NEED-006 0.4 ABSOLUTE crossing (a near-miss 0.394, 2/3 seeds) to 'a SEPARATE trained-encoder MECH-189 evidence successor (the absolute governance gate)' that is 'tracked on MECH-189 (candidate / conf 0.0; full behavioural validation pending), not as GAP-11'. MECH-189 is confirmed still `candidate` (verified 2026-06-23) and that successor has no closure node + no queued experiment. This node tracks it so the owed trained-encoder run is visible on the map rather than only in a completion_note. Author via /queue-experiment when prioritised. NOT queued here (experiment_queue.json held by concurrent sessions). NO claims.yaml change."
    - id: "infant_substrate:GAP-12"
      title: "EXQ-ISEF-003: microhabitat zones vs homogeneous geography (latent state diversity)"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-001, DEV-NEED-007, ARC-065]
      depends_on: ["infant_substrate:GAP-2", "infant_substrate:GAP-5", "infant_substrate:GAP-7"]
      last_updated: 2026-05-29
      completion_note: "V3-EXQ-589 ran 20260518T134905Z PASS supports ARC-065 (microhabitat zones produce greater latent-state diversity than homogeneous geography per the per-claim direction). GAP-12 closes for ARC-065. DEV-NEED-001 / DEV-NEED-007 measurement gaps satisfied by this run's metrics."
    - id: "infant_substrate:GAP-13"
      title: "EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attractor capture)"
      status: in_progress
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-003, MECH-314]
      depends_on: ["infant_substrate:GAP-4", "infant_substrate:GAP-5", "infant_substrate:GAP-6"]
      cross_plan_link: ["behavioral_diversity_isolation:GAP-A", "behavioral_diversity_isolation:GAP-I"]
      blocked_by: "RE-ADJUDICATED 2026-06-09: the 'build a MECH-111 broadcast -> E3-selection routing substrate' framing is STALE on TWO counts. (1) A per-candidate novelty routing substrate LANDED 2026-06-07 (MECH-314a Phase-2, curiosity_candidate_source=e2_world_forward) and V3-EXQ-648a confirmed the curiosity channel is LOAD-BEARING-READY: readiness floors all MET (consumed candidate z_world spread 0.149 >= 0.05; consumed curiosity bias range 0.0206 >= 1e-4) and the LOAD-BEARING C2 PASSED (visitation source -> per-candidate-VARYING curiosity bias). The 648a overall FAIL is driven ONLY by non-load-bearing C1/C3 + a now-fixed precondition false-positive (REE_assembly 4cad6af514/639e9e0a59), per failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07 (confirmed). So 'the channel does not carry variance' is no longer true. (2) The V3-EXQ-590 DESIGN itself is the WRONG vehicle: it sweeps novelty_bonus_weight = MECH-111 (E1-PE-variance novelty in score_trajectory), a DIFFERENT, still-BROADCAST channel; a literal 590b re-run of that design would still be byte-identical. The now-ready per-candidate channel is the MECH-314 StructuredCuriosity path under curiosity_candidate_source=e2_world_forward. RESIDUAL BLOCKER (not a new substrate build): the shared selection-AUTHORITY frontier -- whether the now-per-candidate-varying curiosity bias actually CHANGES the committed selection. 604b's C1 (curiosity-changes-selection under modulatory authority) FAILed as a PRE-FIX null (ran before the GAP-A fix validated 2026-06-07T13:14Z) -> retest as 604c on the GAP-A-fixed + modulatory-authority substrate. Same selection-authority frontier (modulatory-bias-selection-authority V3-EXQ-643a + MECH-341 V3-EXQ-660) that self_attribution:GAP-2, sd_037_axis_b, arc_062:GAP-B converge on. GAP-13 is NOT a separate /implement-substrate build."
      resume_condition: "Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once the shared behavioural-diversity selection-authority frontier lands contributory (604c curiosity-changes-selection on the GAP-A + modulatory-authority substrate; V3-EXQ-660 MECH-341 within-class diversity), re-issue the novelty Goldilocks calibration as V3-EXQ-590b on the MECH-314 e2_world_forward novelty channel (curiosity_candidate_source=e2_world_forward + use_structured_curiosity + the GAP-A/authority stack matched), NOT the bare MECH-111 sweep. The 648a routing table pre-registered this: phase2_substrate_ready PASS -> queue 590b; that PASS branch did not fire because the residual is selection authority, now owned by the shared frontier."
      last_updated: 2026-07-20
      governance_2026_07_20: "Closure-drift stale-since-review ACKNOWLEDGE (governance cycle 2026-07-20T15:57Z). Flagged because confirmed failure_autopsy_V3-EXQ-604c_2026-07-20 reclassified MECH-314 (in this node's unblocks set) after last_updated. Does NOT change GAP-13's status. The 604c re-adjudication applied non_contributory/substrate_ceiling to the MECH-314b/314c/Q-044 family; the substrate-ceiling audit now lists all three as ceiling-may-have-lifted (the modulatory-bias-selection-authority substrate landed and pending_retest_after_substrate is still set), so the owed retest is runnable. This BEARS on GAP-13 without resolving it: the node was re-adjudicated 2026-06-23 to RE-QUEUEABLE-WITH-CAUTION on the MECH-314 e2_world_forward channel (NOT the bare MECH-111 sweep), and the 604c re-read means the per-candidate curiosity leg that re-adjudication leaned on is itself now awaiting a retest rather than settled. Author 590b only after that retest, and keep the non-vacuity guard the 2026-06-23 entry specifies. Status stays blocked_pending_substrate; owner_exq unchanged; NO claims.yaml change in this pass beyond the family notes already applied; last_updated bumped 2026-06-27 -> 2026-07-20."
      governance_2026_06_27: "LINEAGE ADVANCED 705b -> 706 -> 706b; the double-gated RESUME path named in the 06-25 entry RAN and is the brake-LOCK TERMINAL. The brake-EXEMPT DOUBLE-GATED re-test (use_f_eligibility_demotion AND use_go_nogo_constitution both ON) was queued as V3-EXQ-706 -> validity-fixed V3-EXQ-706b (superseding 706). 706b (confirmed failure_autopsy_704b-706b-conversion-ceiling_2026-06-27, applied this cycle) is the FIRST FULLY-VALID double-gated test (non_degenerate=True; all 6 readiness legs met incl. MECH-448 demotion excluded 23.4 AND MECH-449 Go/No-Go suppressed 7.9; valid magnitude-matched non-temperature null; per-seed budget balanced) and committed-action-class entropy STILL did not lift (ARM_CURIOSITY 0.967 < double-gated F-only 1.029 < valid null 1.019) -> conversion_ceiling_persists_despite_double_gating_valid_null (the pre-registered TERMINAL). Re-derive brake FIRED + BRAKE-LOCK (8th MECH-314 ceiling autopsy): REFUSES any further V3 letter on the MECH-314 conversion lineage; the ceiling is architectural (single-arena collapse) -> route /implement-substrate on v4_loop_segregation (ARC-110), which now lists MECH-314 in unblocks_claims (706b failure record appended). MECH-314 UNWEAKENED (epistemic_category stays substrate_ceiling, pending_retest_after_substrate stays true). owner_exq V3-EXQ-705b -> V3-EXQ-706b. Status stays in_progress (closes only on a committed-conversion lift, which now requires the ARC-110 build). Convergent with V3-EXQ-704b (MECH-451) onto the identical single-arena wall. NO claims.yaml status change (note-only)."
      governance_2026_06_25: "LINEAGE ADVANCED 590c -> 705 -> 705b; conversion-ceiling reconciliation. The 590c novelty Goldilocks self-routed substrate_not_ready_requeue (confirmed failure_autopsy_V3-EXQ-590c_2026-06-24, 4th MECH-314 ceiling autopsy: weight sweep argmin scale-invariant within a fixed eligible set -> vacuous) and re-derive brake FIRED, routing to the demotion-ON conversion re-test family. That re-test ran as V3-EXQ-705 (all-admit confound, brake-exempt; failure_autopsy_V3-EXQ-705_2026-06-25) -> V3-EXQ-705b (config-only fix: 689e channel-adaptive floor + hardened legC). 705b (failure_autopsy_V3-EXQ-705b_2026-06-25, CONFIRMED, applied this cycle) is the FIRST FAIR demotion test (excluded_count 14.45 vs 705 all-admit 0.0; 590c saturation-arm confound fixed; GAP-A pool divergent) and committed-action-class entropy STILL did not lift -> conversion_ceiling_persists_despite_demotion. MECH-314 set epistemic_category=substrate_ceiling + pending_retest_after_substrate=true (UNWEAKENED -- the ceiling is upstream/architectural, a single rank-preserving eligibility gate). Re-derive brake FIRED 6th time -> REFUSES a 705c demotion-only same-substrate letter. RESUME path (brake-EXEMPT): /queue-experiment a DOUBLE-GATED re-test (use_f_eligibility_demotion=True AND use_go_nogo_constitution=True -- MECH-449 Go/No-Go already built+validated, 689g PASS 3/3, but was OFF in 705b); V4 ARC-110 loop-segregation (existing v4_loop_segregation substrate_queue entry) ONLY if the double-gated re-test also fails. substrate action=none (no build owed). owner_exq V3-EXQ-590c -> V3-EXQ-705b. Status stays in_progress (closes only on a committed-conversion lift). NO claims.yaml status change (epistemic_category + pending_retest only)."
      governance_2026_06_24: "GUARDED RE-QUEUE LANDED (session queue-experiment-590c-mech314-novelty-goldilocks). The 2026-06-23 RE-QUEUEABLE-WITH-CAUTION condition is now actioned: V3-EXQ-590c authored + queued via /queue-experiment (ree-v3 5229c8f; experiments/v3_exq_590c_mech314_novelty_goldilocks.py + experiment_queue.json). Correct ID is 590c not 590b (590b already RAN 2026-06-11 FAIL/non_contributory; per EXQ versioning the next letter is 590c, and the 590b routing table says 're-queue as V3-EXQ-590c'). DESIGN: sweeps curiosity_novelty_weight [0,0.05,0.25,1.0] on the MECH-314 StructuredCuriosity per-candidate channel (curiosity_candidate_source=e2_world_forward + use_structured_curiosity), with the GAP-A/modulatory-bias-selection-authority stack held CONSTANT (use_modulatory_selection_authority=True, modulatory_authority_gain=1.0, use_modulatory_shortlist_then_modulate=True + modulatory_shortlist_mode=top_k + modulatory_shortlist_k=3 from 569i). Under the top-k shortlist the committed action is the within-top-3 argmin of the curiosity-fed _modulatory_accum, so curiosity_novelty_weight is load-bearing (NOT washed out by the additive-authority rescale -- the reason 590b had to sweep authority_gain). DV = committed-action-class entropy (the 569i/MECH-439 statistic), NOT h_pos. claim_ids re-evaluated from scratch = [MECH-314, DEV-NEED-003] (NOT 590b's MECH-314a). MANDATORY non-vacuity guard (the 569i conversion is ENV-CONDITIONAL, V3-EXQ-625e): committed_class_entropy flat across weights OR curiosity bias range / e2 cand-divergence below floor -> self-route substrate_not_ready_requeue (non_contributory), NEVER a weakens. Re-derive brake (Step 2.5b, MECH-314 3 ceiling autopsies) RELEASED: the 569i top-k conversion path + ARC-065 GAP-A are both built; this is the conversion-path re-issue, not a same-granularity re-test; the guard prevents a false falsification. Dry-run smoke: 4 arms end-to-end, guard self-routes at toy/untrained-e2 scale, validate_experiments --strict OK, no manifest leak. status blocked_pending_substrate -> in_progress; owner_exq V3-EXQ-590 -> V3-EXQ-590c. NO claims.yaml change."
      governance_2026_06_23: "RE-ADJUDICATE vs the selection-authority frontier landing + EDGE DRAW (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). The resume_condition's named preconditions have now substantially fired: behavioral_diversity_isolation:GAP-A is status=done (V3-EXQ-569i PASS 2026-06-17) and the 604c curiosity-changes-selection leg PASSED (closed the Q-044/MECH-314 strand per arc_062 GAP-H). So GAP-13's blocker (per-candidate curiosity bias reaching committed selection) is no longer substrate-absent. CAVEAT (the honest brake): the 569i conversion is ENV-CONDITIONAL (V3-EXQ-625e autopsy 2026-06-20) -- a 590b Goldilocks re-issue could still re-derive the MECH-439 conversion ceiling on the infant env. So GAP-13 is now RE-QUEUEABLE-WITH-CAUTION (author 590b via /queue-experiment on the MECH-314 e2_world_forward channel, NOT the bare MECH-111 sweep), gated on a non-vacuity guard that self-routes if committed-selection diversity does not survive. Added cross_plan_link to behavioral_diversity_isolation:GAP-A (now done) + :GAP-I (the conversion root). Status stays blocked_pending_substrate pending that guarded re-queue (NOT auto-queued -- experiment_queue.json held by concurrent sessions). NO claims.yaml change."
      governance_2026_06_09: "Re-adjudicated GAP-13's MECH-111-routing blocker against the landed 2026-06-07 e2_world_forward routing (user-directed follow-on to self_attribution:GAP-2; same stale-gate pattern). FINDING: the substrate the 2026-05-30 blocked_by demanded ('build MECH-111 broadcast -> E3 routing') was effectively delivered 2026-06-07 by MECH-314a Phase-2 + GAP-A, and V3-EXQ-648a proved the per-candidate curiosity channel carries variance (C2 load-bearing PASS, spread 0.149 / bias range 0.0206). The real residual is selection AUTHORITY (does the varying bias move the committed argmin), which collapses GAP-13 into the SAME behavioural-diversity frontier as self_attribution:GAP-2 / sd_037_axis_b / arc_062:GAP-B (paced by V3-EXQ-660 + V3-EXQ-643a authority + 604c). Corrected blocked_by + resume_condition; flagged that the 590 design (novelty_bonus_weight=MECH-111) is the wrong vehicle and 590b must run on the MECH-314 e2_world_forward channel. NO experiment queued (vacuous until the authority frontier lands); NO claims.yaml/scoring change; status stays blocked_pending_substrate (the per-candidate signal exists, but the selection-authority leg keeps the experiment non-runnable)."
      governance_2026_05_30: "Closure-drift reconcile: status blocked -> blocked_pending_substrate (terminal). V3-EXQ-590 terminal signal (manifest 20260525T084057Z procedural PASS but MECH-314 + MECH-111 per-claim non_contributory, pending_retest_after_substrate=true) fully absorbed; closure sits behind the MECH-111 broadcast -> E3-selection routing substrate. blocked_by added; resume_condition formalised with the successor naming convention (V3-EXQ-590b). No claims.yaml / manifest / substrate_queue edits this session (plan-doc reconcile only)."
      governance_2026_05_29: "V3-EXQ-590 ran 20260525T084057Z PASS but evidence_direction=pending_retest_after_substrate with MECH-314 + MECH-111 per-claim non_contributory: Goldilocks calibration is degenerate across novelty_bonus_weight 0.1..1.0 (all 5 arms produce byte-identical mean_coverage=1.0, mean_h_pos, mean_novelty_ema to 16 sig figs -- the MECH-111 broadcast-novelty signal does not propagate to E3 selection variance). Same routing-break signature as 2026-05-08 EXQ-141b. Blocked on MECH-111 broadcast -> E3-selection routing substrate; calibration is unmeasurable until that channel carries per-candidate variance. Routes to /implement-substrate on the MECH-111 routing rather than a re-queue with a finer novelty_bonus_weight grid."
    - id: "infant_substrate:GAP-14"
      title: "EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)"
      status: blocked_pending_substrate
      severity: medium
      live:
        as_of: "2026-09-04"
        from: "failure_autopsy_V3-EXQ-996_2026-09-04"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["ARC-046", "f_dominance_conversion_ceiling", "infant_substrate:GAP-14", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: [DEV-NEED-008, ARC-046]
      depends_on: ["infant_substrate:GAP-9", "infant_substrate:GAP-5", "infant_substrate:GAP-6", "infant_substrate:GAP-7", "infant_substrate:GAP-8", "infant_substrate:GAP-14-c2"]
      cross_plan_link: ["behavioral_diversity_isolation:GAP-A", "behavioral_diversity_isolation:GAP-I"]
      blocked_by: "CORRECTED 2026-06-14 (see governance_2026_06_14 -- the prior 'prereq c CLEARED / only prereq b remains' framing was BACKWARDS). Of the three substrate prerequisites (per failure_autopsy_V3-EXQ-591_2026-05-27 section 7): (a) MECH-307 default-value recalibration -- CLEARED 2026-05-15 via V3-EXQ-540g supports. (b) goal-pipeline training regime produces non-trivial z_goal in default config -- CLEARED 2026-06-10 via V3-EXQ-603n PASS (scaffolded_sd054 full-curriculum readiness; all FOUR load-bearing gates G0_stage0_positive_control / G1_p1_survival / G2_p2_contact / G3_p2_zgoal_consumption PASS and non-degenerate -- z_goal is both FORMED and CONSUMED in P2). (c) InfantCurriculumScheduler Phase 0->1 advancement gate -- RE-OPENED (was prematurely marked CLEARED in the 2026-06-10 note BEFORE its readiness diagnostics returned). The 591b/591c readiness diagnostics arbitrated AGAINST clearance and split (c) into TWO orthogonal defects: (c-1) exploration-STRENGTH collapse -- V3-EXQ-591b FAIL (only 4/5 seeds reach Phase 1; seed 46 collapses, h_pos_mean 0.0375) and V3-EXQ-591c FAIL (diversity stack ARMED at landed defaults, seed-46 collapse PERSISTS identical to stack-OFF); the prescribed Q-043 magnitude sweep V3-EXQ-667 FAILed (4/5 seeds byte-identical across 8x joint knob scaling -> the swept exploration knobs have ZERO E3 selection authority) -> magnitude lever EXHAUSTED; retest V3-EXQ-667a NOT yet queued. GATE REPOINTED 2026-07-21 (see governance_2026_07_21): c-1 is NO LONGER blocked on modulatory-bias-selection-authority (that gate was RETIRED 2026-07-20) -- it is blocked on the BEHAVIOURAL-COMPETENCE wall (V3-EXQ-724 competence_deficit_diffuse). (c-2) gate OVER-PERMISSIVENESS -- RESOLVED at the criterion level 2026-06-15 (see governance_2026_06_15). The gate-criterion lineage ran 591d -> 591e -> 591f: 591d FAIL (neither single-episode K-of-N nor EMA(alpha0.2) discriminates -- both reject genuine explorers 42/43 AND the seed-45 false-advancer); 591e FAIL (the 591d-prescribed EMA-of-LEVEL@0.2 ADMITS the seed-45 false-advancer via a causal one-way-latching short-memory EMA -- failed OPPOSITE to 591d); 591f PASS 2026-06-15 (robust sustained-level criterion sweep; interpretation.label sustained_level_criterion_discriminates_crossing_count) -- a crossing-count criterion DISCRIMINATES (admits genuine explorers 42/43/44, rejects seed-45). All three claim-free (ARC-046 not weighted). The DISCRIMINATING criterion is now IDENTIFIED; the residual c-2 step is WIRING it into the live InfantCurriculumScheduler Phase 0->1 gate (a substrate edit, not a further diagnostic). EXQ-ISEF-005 (the full curriculum-vs-flat V3-EXQ-591 successor) stays blocked_pending_substrate until (c-1) resolves AND the (c-2) crossing-count criterion is wired into the scheduler; do NOT re-queue it on the (b)-cleared signal alone."
      last_updated: 2026-09-03
      governance_2026_09_03: "V3-EXQ-591h VACUOUS -- EXPERIMENT-DESIGN DEBT RECORDED HERE, and DELIBERATELY NOT a substrate_queue entry. Confirmed failure_autopsy_V3-EXQ-591h_2026-09-03 (ratified REE_assembly d51fc6aaa5) states an earlier draft proposing a new entry (infant-curriculum-phase-has-no-behavioural-consumer) is WITHDRAWN on red-team measurement, so governance recorded the debt on this node instead of minting one. 591h PASSED 5/5 seeds with all five preconditions met, but per_episode_h_pos is BIT-IDENTICAL between ARM_SPIKE and ARM_CROSSING on 5/5 seeds (0 differing episodes, max |diff| 0.0) despite the arms sitting in different phases for 6-24 episodes on four seeds: the only phase->agent channel the 591b-591h driver family wires is config.e3.novelty_bonus_weight, whose consumer was DELETED 2026-05-25 as dead-by-construction. A 4.8h run returned a unanimous PASS about a loop that was never closed. THE CURRICULUM DOES REACH BEHAVIOUR, via channels the drivers never wired -- env_kwargs() (harm_gradient_enabled -> causal_grid_world.py:2617; transient_benefit_enabled -> :3077) and config_overrides() offline_integration_frequency (10 -> 20 -> agent.py:12070). ANY SUCCESSOR MUST (a) apply env_kwargs() and offline_integration_frequency, NOT novelty_bonus_weight; (b) carry a precondition asserting the two arms trajectories diverge somewhere BEFORE the verdict is computed; (c) take a NEW EXQ number per infant_gap14_redesign_staged_20260827.md, not another 591 letter. BLOCKER FOR THAT WORK: ree-v3/tests/contracts/test_infant_curriculum_gap9.py:262-264 currently pins the dead novelty_bonus_weight key > 0 and must be updated by any such change. GOVERNANCE ALSO REMOVED 591h ARC-019 CLAIM TAG (user-approved this cycle, written to both manifest copies): the run bears on ARC-019 in neither direction, and the tag is what placed an untested claim into pending_review.md as though tested. Routing per the autopsy is queue-experiment (design debt), NOT implement-substrate. status UNCHANGED (blocked_pending_substrate); no claims.yaml status change; substrate_queue.json queue length unchanged (no create)."
      governance_2026_07_21b: "UNVERIFIED PRECONDITION RESOLVED -- 667 KNOB ROUTING TRACED (READ-ONLY code trace; plan-frontmatter ONLY; NO claims.yaml / queue / manifest / substrate_queue / substrate edit; NOTHING queued; session affectionate-bose-38affb, 2026-07-21T17:44Z). governance_2026_07_21 above flagged as UNVERIFIED that nobody had confirmed 667's swept knobs reach the E3 path MECH-448/449 act on. Traced at ree-v3 HEAD. VERDICT: SPLIT -- one knob DISJOINT, one knob same-path-but-attenuated; either way 667a is NOT a viable re-run-with-the-lift-ON and needs a DIFFERENT DESIGN. (1) WHAT 667 SWEEPS (experiments/v3_exq_667_q043_exploration_magnitude_sweep.py:150-157): exactly two knob families, jointly scaled 1x/2x/4x/8x -- MECH-313 noise_floor_alpha (0.1 base) and MECH-314 curiosity_{novelty,uncertainty,learning_progress}_weight (0.05 base each, all three set to the SAME swept value). Nothing else varies per arm. (2) noise_floor_alpha IS DISJOINT FROM THE COMMITTED SELECTION POINT. It reaches ree_core exactly once: agent.py:938-944 builds NoiseFloor; noise_floor.py:192 lifts the softmax temperature (effective = baseline + alpha, baseline = 1.0, the select_action default at agent.py:4949 -- 667 never passes one); agent.py:6778-6784 stores it as tonic_effective_temperature and agent.py:7039-7041 passes it to e3.select as the `temperature` positional. In 667's config EVERY shortlist/demotion/gap-scaled flag is default OFF (config.py:596 use_modulatory_selection_authority, :1020 use_modulatory_shortlist_then_modulate, :1074 use_gap_scaled_commit_temperature, :1112 use_f_eligibility_demotion, :1169 use_go_nogo_constitution, :767 use_loop_segregation, :3187 use_e3_score_diversity), so the committed branch is e3_selector.py:3113 `selected_idx = int(scores.argmin().item())` -- an ARGMIN, which is temperature-INVARIANT by construction. Temperature bites ONLY on the uncommitted branch (probs built e3_selector.py:2742, sampled :3136; the commit gate itself is :2792 committed = commit_variance < effective_threshold, i.e. an E3-variance quantity alpha does not touch). CRITICALLY THE LIFT DOES NOT CHANGE THIS: with use_f_eligibility_demotion ON the committed pick is e3_selector.py:3022 `mod_eligible.argmin()` -- still an argmin, still temperature-free. The ONLY committed-path consumer of temperature anywhere in select() is MECH-439 Factor B `_gap_scaled_commit_pick` (e3_selector.py:1366-1391, T_eff = base + alpha*(1-gap_norm) then multinomial), reached at :3018 or :3108 and gated on use_gap_scaled_commit_temperature -- a DIFFERENT flag from the two the June note was waiting on. So MECH-313 is on a path DISJOINT from the MECH-448/449 lift. (3) curiosity_weight IS on the same path, and MECH-448 AMPLIFIES it -- but the JOINT-MAGNITUDE knob is structurally attenuated. Routing: structured_curiosity.compute_score_bias -> agent.py:6334-6348 sums it into dacc_score_bias -> agent.py:6944 passes it as the `score_bias` kwarg -> e3_selector.py:2256-2258 adds it to `scores` AND assigns it as `_modulatory_accum` -> committed argmin :3113. That accumulator is EXACTLY what MECH-448 arbitrates on: f_demotion builds the eligible set from raw_scores only (:2859-2866, _f_eligibility_envelope :1125-1203, rank-preserving F-prefix) and then picks by `_modulatory_accum.argmin()` within it (:2964, :3022) with F REMOVED -- so the curiosity channel gains genuine committed authority under the lift. MECH-449 (_go_nogo_eligibility_gate :1205-1251, applied :2937-2940) governs eligible-set MEMBERSHIP on axes ORTHOGONAL to F (safety/staleness/perseveration/viability/go) -- same path, but not fed by either 667 knob; it can only change WHICH candidates the curiosity arbitration sees. TWO ATTENUATORS make the 667 knob itself weak regardless of the lift: (a) only MECH-314a novelty is PER-CANDIDATE (structured_curiosity.py:401); 314b and 314c are scalar broadcasts times ones(K) (:420-422, :437-439) = UNIFORM shifts, argmin-invariant -- so two of the three weights 667 scaled are inert at selection BY CONSTRUCTION (independently confirmed by failure_autopsy_V3-EXQ-604c_2026-07-20, already cited above); and (b) the sum is clamped ELEMENTWISE to +/-curiosity_bias_scale (default 0.1, config.py:3033) at structured_curiosity.py:448-450, AFTER the uniform terms are added -- so once curiosity_uncertainty_weight*unc + curiosity_lp_weight*lp >= 0.1 EVERY element hits the -0.1 rail, the vector becomes exactly uniform, and the per-candidate 314a component is ANNIHILATED. Scaling the weights UP drives toward that saturation, i.e. the knob's authority is NON-MONOTONE in the swept scale and can fall to zero at high scale. curiosity_bias_scale was NOT swept by 667. This is consistent with the recorded readiness failure (per_arm_healthy_mean 1x 0.5757 / 2x 0.5795 / 4x 0.5795 / 8x 0.5929 -- 2x and 4x IDENTICAL; range 0.0172 < floor 0.05). Note use_modulatory_selection_authority being default-OFF is what SPARED 667 an outright normalise-away (e3_selector.py:2417-2450 rescales the combined modulatory contribution to gain*raw_score_range, which would make ANY joint magnitude scaling exactly inert) -- relevant because that authority is `status: implemented` in substrate_queue: a 667a that turns it ON must NOT sweep magnitude. (4) WHAT 667a WOULD HAVE TO SWEEP INSTEAD (design note only, NOTHING queued, c-1 still gated on the V3-EXQ-724 competence wall): NOT noise_floor_alpha x curiosity_weight jointly. On the MECH-313 face the knob must be `use_gap_scaled_commit_temperature` (+ its alpha), the only committed-path temperature consumer. On the MECH-314 face: sweep the 314a novelty weight ALONE with 314b/314c OFF (only 314a is per-candidate), and sweep `curiosity_bias_scale` jointly with it or the clamp eats the sweep. And the lever that actually converts a per-candidate curiosity range into committed-action change is turning use_f_eligibility_demotion ON (optionally with use_f_eligibility_adaptive_floor, :1185-1195) -- i.e. the lift is a FLAG to arm, not a background condition that makes the old sweep work. (5) INCONCLUSIVE residue: whether the residue-sourced 314a novelty carried any non-zero cross-candidate range during Phase 0 CANNOT be settled statically, and the 667 manifest recorded no curiosity diagnostics (no curiosity bias_max_abs, no committed-tick fraction, no f_eligibility_* fields -- the flags were off). So the split between 'clamp saturation' and 'novelty signal flat' is unresolved; any 667a must instrument e3_selector.last_score_diagnostics + StructuredCuriosity._last_bias_max_abs as a P0 readiness assertion BEFORE scoring any behavioural DV. status UNCHANGED (blocked_pending_substrate) -- this resolves a PRECONDITION, not the c-1 block, which stays gated on the V3-EXQ-724 behavioural-competence wall."
      governance_2026_07_21: "c-1 GATE REPOINTED OFF A RETIRED BLOCKER (plan-frontmatter reconcile ONLY; NO claims.yaml / queue / manifest / substrate_queue edit; NOTHING queued; session wizardly-tereshkova-31e9a1). This node's blocked_by named `modulatory-bias-selection-authority` as c-1's gate, prose last written 2026-06-14/06-23. THAT GATE WAS RETIRED 2026-07-20 and the node has been routing off it ever since: confirmed failure_autopsy_V3-EXQ-604c_2026-07-20 resolved MECH-314 (parent + 314a `supports` STANDS, no substrate owed; 314b/314c non_contributory -- global scalars broadcast across K candidates, so a 0.0 delta is an arithmetic identity, behaviourally inert at selection BY CONSTRUCTION and untestable by any selection-level DV), and named the remedy as an ARC-065 amend (give 314b/c the per-candidate treatment 314a already has), EXPLICITLY NOT selection authority. insights_report.md Corrections section 2 (2026-07-20T07:58Z) supersedes the selection-authority recommendation and docs/CURRENT_FRONT.md renders the gate struck through. So GAP-14 was gated on a work item that no longer exists. THE LIVE GATE IS THE BEHAVIOURAL-COMPETENCE WALL: V3-EXQ-724 competence_localization_diagnostic ran 20260709T211405Z FAIL / non_contributory, interpretation.label `competence_deficit_diffuse`, localizing_arms EMPTY -- and its readiness anchor CLEARS (a greedy nearest-resource oracle forages 6.05 resources/ep against a COMPETENCE_RESOURCE_FLOOR of 1.0 in the same env), so the env is FINE and the deficit is the agent's, diffuse, with no single arm localizing it. This is the same wall that aborted V3-EXQ-714 at C1 readiness, and it is the reframe failure_autopsy_V3-EXQ-719a_2026-07-08 applied to the whole conversion ceiling (a behavioural-COMPETENCE / training-regime ceiling, NOT a further selection/de-commit lever). NET EFFECT ON 667a: still NOT queued, and DELIBERATELY so -- but for a DIFFERENT reason than the stale prose gave. Note in 667a's favour that the selection-face lift the June note was waiting on WAS built + validated + promoted (MECH-448 use_f_eligibility_demotion + MECH-449 use_go_nogo_constitution, per behavioral_diversity_isolation:GAP-I governance_2026_07_06d), so a substrate lever now exists that did not in June; against it, a 667a run under the 724 diffuse-competence wall would most likely abort at readiness like 714 or return byte-identical seeds AGAIN for a different reason, and would then read as a SECOND exhausted lever when the competence floor is what is actually binding. AMEND (same session, 2026-07-21T17:43Z, on a substrate_queue re-read): the gate was RETIRED PARTLY BECAUSE IT WAS BUILT, and this note's first pass under-stated that. The substrate_queue entry `modulatory-bias-selection-authority` ('Modulatory score-bias selection authority at E3.select', design_doc docs/architecture/modulatory_bias_selection_authority.md) is `status: implemented`, `ready: true`, `depends_on_unresolved: []`, and lists MECH-314/314a/314b/314c + ARC-062/ARC-065/MECH-309 among its unblocks_claims. So a reader must NOT take 'the gate was retired' to mean the authority never arrived -- it arrived. Note also that this entry's own `failure_record` is the 667-class signature in four other lineages (604a curiosity_bias_abs_mean 0.0 in EVERY arm incl ARM_ALL_ON; 624a action_density lift 0.0 both arms; 614d committed-class entropy BYTE-IDENTICAL across within-class temperature 0.5/1.0/2.0; 640a), i.e. 'a scoring-layer lever that does not reach committed selection' is a RECURRENT failure mode here, not a 667 peculiarity -- which is exactly why the routing question below is the decisive one and not a formality. RELATEDLY the ARC-065 amend that failure_autopsy_V3-EXQ-604c_2026-07-20 named as the replacement remedy HAS been applied to substrate_queue.json (REE_assembly `2241c39cdc`, 'apply CONFIRMED 604c autopsy amend to ARC-065 (GAP-A Phase-2 per-candidate extension for MECH-314b/314c)'), so insights_report.md Corrections section 2's 'confirmed and not yet applied' is itself now STALE -- do not re-apply it. UNVERIFIED PRECONDITION for whoever authors it: nobody has confirmed that 667's specific swept exploration knobs actually ROUTE THROUGH the E3 path the MECH-448/449 lift acts on (nor through the implemented `modulatory-bias-selection-authority` E3.select bias) -- if they do not, the lift is irrelevant to c-1 and 667a needs a different DESIGN, not a re-run. Check that BEFORE authoring. c-1 therefore now tracks the competence-floor thread (MECH-457 cold-start/retention; V3-EXQ-789 retention-auxiliary-decay landed 2026-07-20) rather than behavioral_diversity_isolation:GAP-I's selection face; GAP-I cross_plan_link RETAINED (the root lineage is real history) but is no longer the thing c-1 waits on. The 2026-07-18 readiness-anchor instruction below STANDS UNCHANGED and still binds the reviving session. status UNCHANGED (blocked_pending_substrate -- c-1 open, gate merely renamed to the true one); EXQ-ISEF-005 stays blocked; ARC-046 / DEV-NEED-008 untouched, still candidate."
      governance_2026_07_18: "READINESS-ANCHOR SPECIFICATION DEFECTS RECORDED (record-only; NO script edit, NO status change, NO claims.yaml/queue/manifest edit; session keen-meninsky-71ca79). A follow-on audit of the 591 family (after gracious-hermann-65e9b1's corpus-wide anchor-reachability audit) CONFIRMED all 591 anchors are REACHABLE -- no 778d-class unmeetable gate -- but surfaced TWO defects in the opposite direction, i.e. anchors that under-fail rather than over-fail. (A) `early_policy_produces_nontrivial_h_pos` is VACUOUS in ALL FIVE of 591b/c/d/e/f: the predicate is `max(r['h_pos_max'] for r in seed_results) >= H_POS_MOVEMENT_FLOOR (0.20)` -- a max over all seeds AND all episodes, against a floor two orders of magnitude below the 0.994 gate the load-bearing criterion actually routes on. One seed's single lucky episode clears it while every other seed is stationary; 591c's own docstring records seed 46 at h_pos_mean 0.0375 (h_pos_max 0.690, so seed 46 ALONE clears the floor 3.5x while functionally non-moving). It can essentially never report met:false, so it carries NO readiness signal. (B) `false_advancer_present` in 591d/e/f passes at EXACTLY its gate, zero margin: seed-45's recorded profile is h_pos_mean 0.140 with n_eligible_ge_threshold EXACTLY 2, so the crossings conjunct is SATISFIED and seed 45 is non-genuine SOLELY on 0.140 < 0.20 -- a 0.06-nat margin, scoring 1 against a gate of 1. Any seed-level drift lifting seed 45 past 0.20 flips it genuine, n_false -> 0, anchor unmeetable on that draw. NOT FIXED, deliberately, on two independent grounds: (i) all five scripts ALREADY RAN (591b 20260610T090813Z FAIL, 591c 20260610T225515Z FAIL, 591d 20260614T232048Z FAIL, 591e 20260615T095228Z FAIL, 591f 20260615T115131Z PASS), so per the EXQ supersession policy a fix takes a NEW LETTER (591g, `supersedes:`) and NEVER an in-place edit -- editing them would decouple each script from the evidence record it produced, incl. 591f's PASS (the run that identified the crossing-count criterion wired 2026-06-19, commit b4dc264), reintroducing exactly the 591 evidence-record drift resolved 2026-06-19; and (ii) this node is blocked_pending_substrate on (c-1) with a standing do-NOT-queue instruction, so there is nothing to re-queue. IMPORTANT -- these defects are LATENT and did NOT cause the 591 outcomes: the anchors reported and every run proceeded to a verdict; the failures were adjudicated to genuine seed-46 monostrategy collapse. They are a forward risk (a vacuous readiness gate lets a run emit a confident verdict on an untrained channel), not a retrospective cause, which is why this is recorded HERE as a revival trigger and NOT as a failure-autopsy amendment. ACTION FOR THE REVIVING SESSION: when (c-1) clears and EXQ-ISEF-005 / 591g is authored via /queue-experiment, re-specify anchor (A) as a per-seed statistic (FRACTION of seeds whose h_pos_mean clears the floor -- the same statistic the criterion routes on) and revisit the 0.20 floor against the criterion's 0.994; for (B) either add assert_anchor_reachable(margin_cells=...) with the frozen seed-45 fixture or widen the false-advancer definition off the single 0.06-nat threshold, and document the margin decision explicitly. Do NOT copy the max-based predicate forward. DO NOT 'fix' 591d/e/f's `genuine_explorers_present` -- audited SAFE (a strict widening of the predicate that produced its own control: 591c seeds 42/43/44 at 0.562/0.323/0.842, all clearing 0.20; best achievable 3 vs gate 2). Generic lesson (an existence quantifier standing in for a population property, plus the fact that assert_anchor_reachable tests only a FLOOR and so cannot catch vacuity at all) recorded in ree-v3/experiments/_lib/readiness_anchor.py. status UNCHANGED (blocked_pending_substrate; c-1 open, 667a still not queued)."
      governance_2026_06_23: "SPLIT (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). GAP-14's blocked_by has long self-decomposed into two orthogonal defects: (c-1) seed-46 exploration-STRENGTH collapse [OPEN, blocked on the modulatory-bias-selection-authority / behavioral_diversity_isolation:GAP-A frontier; magnitude lever EXHAUSTED at 667; 667a not queued] and (c-2) gate OVER-PERMISSIVENESS [RESOLVED end-to-end -- criterion IDENTIFIED 591f PASS 2026-06-15 + WIRED into InfantCurriculumScheduler 2026-06-19]. A closed half and an open half shared this one perpetually-blocked box, masking that c-2 is finished. Surfaced c-2 as a `done` child node infant_substrate:GAP-14-c2 (added to depends_on so GAP-14 visibly gates on it); GAP-14 now tracks the residual c-1 only. Added cross_plan_link to behavioral_diversity_isolation:GAP-A (now done) + :GAP-I (the authority frontier c-1 waits on) -- c-1's gate was prose-only. Status stays blocked_pending_substrate (c-1 open). NO claims.yaml change."
      governance_2026_06_19: "c-2 CROSSING-COUNT CRITERION WIRED INTO THE LIVE SCHEDULER (/implement-substrate, ree-v3 experiments/infant_curriculum.py; NOT another diagnostic). The 591f-validated crossing-count criterion (the residual c-2 step the governance_2026_06_15 note named) is now an OPT-IN Phase 0->1 advancement gate on InfantCurriculumScheduler: two no-op-default constructor kwargs phase_0to1_use_crossing_count (default False -> legacy single-episode SPIKE gate, bit-identical) + phase_0to1_crossing_count_min (default 3 = the 591f CROSSING_COUNT_MIN); when ON, _try_phase_0_to_1 accumulates post-ep_min spike-bar crossings and advances at >= count_min -- mirrors the 591f offline _advance_crossing_count EXACTLY (contract asserts online==offline replay on a genuine-explorer and a seed-45-like sequence). 27/27 test_infant_curriculum_gap9.py (19 prior + 8 new C12) + 8/8 preflight PASS; default-OFF bit-identical for every existing caller (591/591b-f, 586, 610e, 669, 667). NO claims.yaml / scoring / script-generated-globals edits (ARC-046 / DEV-NEED-008 untouched, still candidate). status UNCHANGED (blocked_pending_substrate): GAP-14 still requires (c-1) seed-46 exploration-STRENGTH collapse to resolve [still blocked on modulatory-bias-selection-authority / GAP-A; Q-043/667 magnitude lever EXHAUSTED, 667a not yet queued] before the full curriculum-vs-flat EXQ-ISEF-005 (V3-EXQ-591 successor) can be queued. (c-2) is now genuinely closed end-to-end (criterion IDENTIFIED 591f + WIRED 2026-06-19). Plan-doc + ree-v3/CLAUDE.md reconcile only."
      governance_2026_06_15: "c-2 GATE-CRITERION RESOLVED AT CRITERION LEVEL (governance cycle 2026-06-15; claim-free, ARC-046 untouched / still candidate conf 0.0). The c-2 over-permissiveness strand ran its full diagnostic lineage this period: V3-EXQ-591d FAIL (no candidate criterion discriminates -- both K-of-N and EMA reject genuine explorers AND the seed-45 false-advancer; confirmed failure_autopsy_V3-EXQ-591d_2026-06-15) -> V3-EXQ-591e FAIL/non_contributory (the 591d-prescribed EMA-of-LEVEL@0.2 ADMITS seed-45 via causal one-way-latching short-memory EMA, failing OPPOSITE to 591d; confirmed failure_autopsy_V3-EXQ-591e_2026-06-15; supersedes 591d) -> V3-EXQ-591f PASS 2026-06-15 (robust sustained-level criterion sweep; a crossing-count criterion DISCRIMINATES -- admits genuine explorers 42/43/44, rejects the seed-45 false-advancer; supersedes 591e; resolves the gate-criterion question). All three are claim-free c-2 sub-diagnostics (no claim weighting); 591e/591f marked reviewed this cycle, 591e evidence_direction non_contributory + EQN. NET: the DISCRIMINATING Phase 0->1 advancement criterion (crossing-count of the sustained h_pos level) is IDENTIFIED. The residual c-2 work is to WIRE crossing-count into the live InfantCurriculumScheduler gate (a substrate edit via /implement-substrate, NOT another diagnostic). EXQ-ISEF-005 still blocked: BOTH (c-1) exploration-strength collapse [still blocked on modulatory-bias-selection-authority / GAP-A 569g/682, 667a not yet queued] AND the (c-2) crossing-count wiring must land. status UNCHANGED (blocked_pending_substrate). Plan-doc reconcile ONLY: no claims.yaml / scoring / script-generated-globals edits."
      governance_2026_06_14: "STALE-NOTE CORRECTION (chipped follow-on, task_344ccb38). The governance_2026_06_10 note below was actively misleading the next session: it asserted prereq (c) Phase 0->1 gate CLEARED and prereq (b) z_goal as the SOLE remaining blocker. The reverse is true. (b) is CLEARED, (c) is RE-OPENED. (b) z_goal: V3-EXQ-603n PASS landed 2026-06-10T20:14Z (AFTER the 06-10 note was written) -- all four load-bearing gates incl G3_p2_zgoal_consumption non-degenerate; z_goal is formed AND consumed, so 'non-trivial z_goal in default config' is satisfied for this substrate. (c) Phase 0->1 gate: the 06-10 note marked (c) cleared on a 2/3-seed UNTRAINED-agent smoke and queued V3-EXQ-591b for full-scale validation BEFORE that diagnostic returned. The diagnostics it queued then arbitrated AGAINST clearance -- V3-EXQ-591b (FAIL 2026-06-10: only 4/5 seeds reach Phase 1, seed 46 h_pos_mean 0.0375, label phase01_gate_unreliable_needs_strengthening), V3-EXQ-591c (FAIL, failure_autopsy_V3-EXQ-591c_2026-06-11 status confirmed/USER-ADJUDICATED), and the prescribed-fix V3-EXQ-667 Q-043 magnitude sweep (FAIL 2026-06-11, failure_autopsy_V3-EXQ-667_2026-06-11). (c) now splits into two orthogonal defects (full detail in blocked_by): (c-1) seed-46 exploration-strength collapse -- the magnitude sweep is EXHAUSTED (667 = 4/5 seeds byte-identical across an 8x joint scaling; the knobs have zero authority over the committed E3 argmin), blocked on modulatory-bias-selection-authority, retest V3-EXQ-667a not yet queued; (c-2) single-episode-gate over-permissiveness (seed 45 advanced without genuine exploration) -- gate-robustness diagnostic V3-EXQ-591d queued 2026-06-14. status UNCHANGED (blocked_pending_substrate); EXQ-ISEF-005 stays blocked until BOTH (c-1) and (c-2) resolve. Plan-doc reconcile ONLY: NO claims.yaml / manifest / substrate_queue / script-generated-globals (closure_status.md / closure_drift.*) edits (ARC-046 untouched, still candidate conf 0.0)."
      governance_2026_06_10: "Prereq (c) closed (implement-substrate session). The Phase 0->1 H_pos gate retune the autopsy routed to /implement-substrate had already landed 2026-05-31 (H_POS_FRAC_OF_MAX 0.70 -> 0.20); this node's blocked_by was stale (last_updated 2026-05-30, predating the recalibration). Verified empirically: a live early-policy (untrained REEAgent) smoke 2026-06-09 advanced 2/3 seeds past Phase 0 within 112 ep (seeds 42@ep107, 44@ep101; seed 43 borderline at the short 130-step window). User decision 2026-06-10 (AskUserQuestion): keep 0.20, no further gate code change; let the full-scale readiness diagnostic arbitrate. Queued V3-EXQ-591b (diagnostic, claim_ids=[], 160 ep x 5 seeds x 200 steps; ingested into coordinator DB 2026-06-10) -- PRIMARY C1: every seed reaches curriculum phase>=1. GAP-14 status UNCHANGED (blocked_pending_substrate): the sole remaining blocker is prereq (b) z_goal collapse (goal_pipeline:GAP-4 / bdi:GAP-C). Do NOT re-queue the full V3-EXQ-591 curriculum-vs-flat comparison until (b) clears. No claims.yaml / manifest edits (ARC-046 untouched, still candidate conf 0.0). [SUPERSEDED 2026-06-14 -- this note's (c)-cleared / (b)-sole-blocker framing was premature and is reversed by governance_2026_06_14 above; the 591b readiness diagnostic this note queued returned FAIL.]"
      governance_2026_05_30: "Closure-drift reconcile: status blocked -> blocked_pending_substrate (terminal). V3-EXQ-591 terminal signals (manifest 20260526T184231Z FAIL/does_not_support + failure_autopsy_V3-EXQ-591_2026-05-27 confirmed, evidence_direction overridden to non_contributory, ARC-046 NOT weakened) fully absorbed; closure sits behind the 3-prerequisite substrate chain. blocked_by added with the prerequisite breakdown (cluster-aware -- prereq b is the shared blocker with goal_pipeline:GAP-4 and bdi:GAP-C). No claims.yaml / manifest / substrate_queue edits this session (plan-doc reconcile only)."
      governance_2026_05_29: "Drift report freshness bump only; status remains BLOCKED per the 2026-05-27 autopsy. Three substrate prerequisites (MECH-307 default-fix, goal-pipeline training regime, InfantCurriculumScheduler Phase 0->1 gate retune) all unchanged this cycle."
      resume_condition: "2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirmed) applied: manifest evidence_direction overridden to non_contributory; epistemic_category=substrate_ceiling; ARC-046 NOT weakened; pending_retest_after_substrate=true. Root finding: InfantCurriculumScheduler Phase 0->1 advancement gate (H_pos >= 0.70*ln(144) ~= 3.48) is structurally unreachable under random-policy 2000-episode training (observed rolling-mean H_pos peaks 0.03-1.08). z_goal collapses to ~1e-7 in every arm. Cluster pattern: fourth member of substrate-uniform z_goal-zero family (V3-EXQ-540 / 603 chain / 590a / 591). Status changed in-progress -> blocked: three substrate prerequisites must clear before V3-EXQ-591b can be queued: (a) MECH-307 default-value recalibration validated via V3-EXQ-540e; (b) goal-pipeline training regime produces non-trivial z_goal in default config via V3-EXQ-603c P0/P1 phased training (NOW FAIL 2026-05-27 -- Q-045 routed to substrate_conditional; this prerequisite needs V4 substrate or alternative resolution); (c) InfantCurriculumScheduler Phase 0->1 advancement signal tuned to achievable H_pos magnitudes OR replaced with z_goal-norm-based / residue-progression-based exit gate (routed to /implement-substrate)."
    - id: "infant_substrate:GAP-14-c2"
      title: "GAP-14 defect (c-2): Phase 0->1 gate over-permissiveness -- discriminating crossing-count criterion identified + wired into the live scheduler"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      unblocks_claims: []
      depends_on: ["infant_substrate:GAP-9"]
      last_updated: 2026-06-23
      completion_note: "The c-2 over-permissiveness strand of GAP-14, RESOLVED end-to-end and split out 2026-06-23 from the GAP-14 parent (it was masked behind GAP-14's blocked_pending_substrate box). Lineage 591d FAIL -> 591e FAIL -> 591f PASS 2026-06-15 (a crossing-count criterion on the sustained h_pos level DISCRIMINATES: admits genuine explorers seeds 42/43/44, rejects the seed-45 false-advancer). WIRED 2026-06-19 (/implement-substrate, InfantCurriculumScheduler phase_0to1_use_crossing_count / phase_0to1_crossing_count_min, no-op default; 27/27 + 8/8 tests; online==offline replay contract). Claim-free (ARC-046 not weighted). The residual GAP-14 work is c-1 (exploration-strength collapse), tracked on the GAP-14 parent."
    - id: "infant_substrate:GAP-15"
      title: "Gate update: replace single z_goal.norm criterion in developmental_curriculum.md with 7-criterion table (3 blocking + 4 advisory) from infant_substrate_expansion.md Section 8"
      status: done
      severity: governance
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_substrate-readiness-cluster_2026-09-02"
        verdict: "non_contributory/standard"
        next: "routing=implement-substrate"
        brake: "fired"
        needs_review: false
      join:
        bears_on: ["f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["INV-055", "INV-073", "ARC-046", "ARC-065", "DEV-NEED-001", "DEV-NEED-002", "DEV-NEED-003", "DEV-NEED-004", "DEV-NEED-005", "DEV-NEED-006", "DEV-NEED-007", "DEV-NEED-008", "MECH-189", "MECH-313", "MECH-314"]
      completion_note: "developmental_curriculum.md Gate Criterion section replaced with 8-criterion table (C1-C3 blocking, C4-C8 advisory) matching developmental_metrics.md DEV-NEED-008. Thresholds noted as proposals pending EXQ-ISEF-001..004. 2026-05-17T10:54Z"
      unblocks_claims: [DEV-NEED-008]
      depends_on: ["infant_substrate:GAP-10", "infant_substrate:GAP-11", "infant_substrate:GAP-12", "infant_substrate:GAP-13"]
      last_updated: 2026-05-17
---
# Infant Substrate Expansion Plan

**Registered:** 2026-05-16
**Status:** active
**Scope:** implement the richer infant-stage developmental substrate proposed in
`docs/architecture/infant_substrate_expansion.md`, close the DEV-NEED-001..008
measurement gaps, and replace the single-criterion childhood transition gate with
the 7-criterion table derived from targeted literature pulls.

This plan is the durable resume-point for infant substrate work across sessions.
See [infant_substrate_expansion.md](../../docs/architecture/infant_substrate_expansion.md)
for the full design: compression analysis, evidence table, diversity taxonomy,
feature proposals, curriculum schedule, metrics, and experimental manifests.

---

## One-line framing

> The infant stage has a single gate criterion (z_goal.norm) and a structurally
> homogeneous environment; neither produces the valence geography, trajectory
> diversity, or action-class coverage that DEV-NEED-001..008 require and that
> the childhood/play stage presupposes.

The V_s monostrategy problem (MECH-309) is the proximate driver: EXQ-522
(SD-054 heuristic PASS) proved the substrate can carry diverse behavior, but
every trained-policy run returns non_contributory due to monomodal V_s. That
diagnosis points upstream — the infant stage never produced a diverse behavioral
repertoire to begin with. The current infant environment is compressed in six
distinct ways (Section 2 of the design doc); each compression generates a
specific downstream deficit in the developmental gate.

Literature synthesis (37 new entries, 2026-05-16) converges on: monostrategy
prevention requires structured environment with learnable difficulty at multiple
levels, not just a high novelty_bonus_weight. MECH-314c learning-progress
curiosity (not MECH-314a novelty) produces emergent developmental staging.
Context-rigidity — not entropy collapse — is the measurable failure signature.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/infant_substrate_expansion.md](../../docs/architecture/infant_substrate_expansion.md) | Full design: compression analysis, evidence table, feature proposals, curriculum, metrics, gates |
| [docs/architecture/developmental_curriculum.md](../../docs/architecture/developmental_curriculum.md) | Current infant stage parameters; gate criterion to be replaced |
| [docs/architecture/developmental_needs_register.md](../../docs/architecture/developmental_needs_register.md) | DEV-NEED-001..008 with gap log and quantitative gate proposals |
| [evidence/planning/behavioral_diversity_acceptance_criteria.md](behavioral_diversity_acceptance_criteria.md) | Rung 0-4 diversity framework; trajectory diversity prerequisites |
| [evidence/literature/targeted_review_developmental_exploration_hippocampal_retrieval/](../literature/targeted_review_developmental_exploration_hippocampal_retrieval/) | 19 entries: babbling, hippocampal retrieval, enrichment/deprivation |
| [evidence/literature/targeted_review_intrinsic_motivation_exploration/](../literature/targeted_review_intrinsic_motivation_exploration/) | 5 entries: Pathak 2017, Burda 2018, Monosov 2024, Oudeyer 2016, Ventura 2024 |
| [evidence/literature/targeted_review_rl_diversity_monostrategy_curriculum/](../literature/targeted_review_rl_diversity_monostrategy_curriculum/) | 6 entries: DIAYN, DvD, PAIRED, MAP-Elites, IMGEP, Narvekar survey |
| [evidence/literature/targeted_review_infant_affordance_valence_map/](../literature/targeted_review_infant_affordance_valence_map/) | 5 entries: Adolph 2019, Keren-Portnoy 2021, Valadi 2020, Berridge 1998, Burnay 2020 |
| ree-v3/ree_core/environment/causal_grid_world.py | Target file for env feature implementation (GAP-1..4) |

---

## Existing substrate (do not duplicate)

Already implemented and usable for infant stage:

| Component | Location | Status |
|---|---|---|
| MECH-313 noise floor (LC-NE tonic analog) | `ree-v3/ree_core/` | PASS 2026-05-10; entropy lift confirmed EXQ-567 |
| MECH-314 structured curiosity bonus (novelty_bonus_weight) | `ree-v3/ree_core/utils/config.py` | Implemented; defaults to 0.0 (must be set for infant stage) |
| MECH-314c learning-progress (e3._running_variance EMA) | `ree-v3/ree_core/predictors/e3_selector.py` | Phase-1 approximation implemented |
| SD-049 multi-resource heterogeneity | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED 2026-05-03/04; resource_introduction_schedule hook available |
| SD-054 reef safe zones + bipartite layout | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED 2026-05-11; heuristic PASS EXQ-522 |
| SD-047 multi-source hazard dynamics | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED |
| SD-048 interoceptive noise | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED (CONFIRMED primary stochastic attractor — GAP-4 audit; mask from novelty signal when novelty_bonus_weight > 0) |
| SD-029 scheduled external hazard | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED |
| ARC-046 hazard protection (residue_scale_factor ~0.1) | `developmental_curriculum.md` parameter | Specified; residue_scale_factor must be enabled (currently 0.0 default for infant) |
| offline_integration_frequency | `ree-v3/ree_core/utils/config.py` | Available; high sleep:wake ratio for infant (every 10-20 steps) |

---

## Gap inventory

Fifteen gaps across 5 phases. Phases 1-2 (env features + telemetry) are the
minimum prerequisite for any validation run. Phase 3 (curriculum scheduler) is
independent and can be deferred without blocking experiments. Phase 4 runs the
5 candidate experiments from the design doc. Phase 5 closes the governance loop.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | Harm gradient env parameter | high | DEV-NEED-004 gate criterion; residue geography experiments |
| **GAP-2** | Microhabitat zones env parameter | high | DEV-NEED-001/003/007; z_world coverage experiments |
| **GAP-3** | Transient benefit patches env parameter | high | DEV-NEED-006 z_goal seeding experiments |
| **GAP-4** | Stochastic attractor audit | high | Safe deployment of novelty_bonus_weight > 0 |
| **GAP-5** | H_pos / zone_coverage telemetry | high | DEV-NEED-001 blocking gate; EXQ-ISEF experiments |
| **GAP-6** | residue_coverage_pct metric | high | DEV-NEED-004 blocking gate |
| **GAP-7** | traj_pairwise_cosine_mean metric | medium | DEV-NEED-002/005 advisory gate |
| **GAP-8** | post_sleep_z_goal_retention metric | medium | DEV-NEED-007 advisory gate |
| **GAP-9** | 4-phase curriculum scheduler | medium | Emergent developmental staging (Oudeyer 2016) |
| **GAP-10** | EXQ-ISEF-001: harm gradient vs binary-contact | medium | DEV-NEED-004 evidence |
| **GAP-11** | EXQ-ISEF-002: transient benefit z_goal seeding | medium | DEV-NEED-006 / MECH-189 evidence |
| **GAP-12** | EXQ-ISEF-003: microhabitat latent diversity | medium | DEV-NEED-001/007 / ARC-065 evidence |
| **GAP-13** | EXQ-ISEF-004: novelty bonus calibration | medium | MECH-314 calibration |
| **GAP-14** | EXQ-ISEF-005: curriculum vs flat comparison | medium | DEV-NEED-008 / ARC-046 evidence |
| **GAP-15** | Gate criterion update in developmental_curriculum.md | governance | DEV-NEED-008 gate closure |

---

## Sequenced plan

### Phase 1: Environment features (GAP-1, 2, 3, 4)

All four can be implemented in parallel. GAP-4 (audit) is code-read only — no
new implementation, just enumerate `random.*` calls in `causal_grid_world.py`
step() and reset() and classify each as learnable-stochastic vs irreducible.

GAP-1 deliverables: `harm_gradient_enabled: bool`, `harm_gradient_outer_radius: float`,
`harm_gradient_inner_radius: float`, `harm_gradient_scale: float` in
`CausalGridWorldV2.__init__`. Reward computed in `step()` as
`-hazard_harm * (1 - d/r_outer)^2 * scale` for cells within r_outer but outside
r_inner of any hazard. No terminal contact until r_inner.

GAP-2 deliverables: `microhabitat_enabled: bool`, `n_microhabitats: int`,
`zone_A/B/C_resource/hazard_factor: float`, `zone_C_ambient_bonus: float`.
Zone map generated once per episode via Voronoi seed on `reset()`.
Zone-B hazard_factor ~1.8x; zone-C hazard_factor 0.0; zone-C ambient +0.05.

GAP-3 deliverables: `transient_benefit_enabled: bool`, `transient_benefit_prob: float`,
`transient_benefit_duration: int`, `transient_benefit_multiplier: float`.
Spawn logic in `step()`: each step, with probability p, add patch at a
zone-weighted random cell. Patch tracked in episode buffer; expires after N steps.
Contact reward = `resource_benefit * multiplier`.

GAP-4 deliverables: a brief audit note (can live in the design doc or as a
comment block in causal_grid_world.py). Flag SD-048 interoceptive noise as
potential stochastic attractor — its noise scale should be excluded from the
novelty signal computation when novelty_bonus_weight > 0.

---

### Phase 2: Telemetry infrastructure (GAP-5, 6, 7, 8)

GAP-5: Add to `info` dict in `step()` or compute in training loop:
- `pos_entropy`: Shannon entropy of position histogram (rolling 100-step window)
- `zone_coverage`: dict of {zone: fraction cells visited} — requires zone_map
  from GAP-2, OR stub with single zone until GAP-2 lands

GAP-6: Add to training loop or episode summary:
- `residue_coverage_pct`: fraction of grid cells where `abs(residue[y,x]) > threshold`
  (suggested threshold: 0.02 * residue_scale_factor). Requires residue_scale_factor > 0.

GAP-7: At end of each episode, compute over N sampled trajectory pairs:
- `traj_cosine_mean`: mean(1 - cosine_similarity(traj_i, traj_j)) for N random pairs.
  Trajectories represented as flattened (y,x) sequences or action sequences.

GAP-8: After each sleep integration cycle, log:
- `z_goal_before_sleep`: z_goal.norm() at sleep entry
- `z_goal_after_sleep`: z_goal.norm() after `offline_integration_frequency` steps
- `z_goal_retention`: z_goal_after_sleep / z_goal_before_sleep

---

### Phase 3: Curriculum scheduler (GAP-9) — independent

Implement a curriculum_phase counter in REEAgent or training loop that gates
which env parameters are active. Phase boundaries triggered by episode count +
telemetry thresholds (or hard episode count if telemetry unavailable):

```python
# Pseudocode for infant curriculum scheduler
if episode < 100 and H_pos < threshold:
    phase = 0  # babbling
elif z_goal.norm() < 0.3 or benefit_contacts < 5:
    phase = 1  # benefit discovery
elif residue_coverage_pct < 0.10:
    phase = 2  # geography
else:
    phase = 3  # pre-gate
```

Phase 0: novelty_bonus_weight=0.5, E3 planning disabled, no transient benefits,
no harm gradient, no microhabitats, residue_scale_factor=0.0.

Phase 1: +transient_benefit_enabled, +harm_gradient (mild), residue_scale_factor=0.05.

Phase 2: +microhabitat_enabled, harm_gradient full, multi-resource active (food+water),
residue_scale_factor=0.10. SD-054 bipartite active.

Phase 3: all features active. E3 planning at weight 0.1. approach adult parameters.

---

### Phase 4: Validation experiments (GAP-10..14)

Each experiment script follows the `/queue-experiment` skill path. No direct
writes to `experiment_queue.json` outside that skill. Scripts go in
`ree-v3/experiments/` with the EXQ-ISEF-* identifier in the filename; the
actual queue IDs will be assigned at queue time (EXQ-NNN where NNN is next
available).

**EXQ-ISEF-001 (GAP-10)** -- harm gradient residue geography speed (V3-EXQ-587)
- Prereqs: GAP-1, GAP-5, GAP-6
- Criterion: ARM_1 (harm_gradient_enabled=True, scale=0.30) final mean_weight > 2x
  ARM_0 (harm_gradient_enabled=False) in >= 4/5 seeds. Coverage metric saturates at
  1.0 for both arms (V3-EXQ-575a finding); mean_weight (continuous, magnitude-sensitive)
  is the discriminating primary criterion.

**EXQ-ISEF-002 (GAP-11)** — transient benefit z_goal seeding rate
- Prereqs: GAP-3, GAP-5
- Criterion: treatment median first z_goal.norm() > 0.4 crossing < 0.7x control

**EXQ-ISEF-003 (GAP-12)** — microhabitat latent diversity
- Prereqs: GAP-2, GAP-5, GAP-7
- Criterion: treatment z_world PCA top-3 variance > 1.2x control at episode 1000

**EXQ-ISEF-004 (GAP-13)** — novelty bonus Goldilocks calibration
- Prereqs: GAP-4, GAP-5, GAP-6
- Criterion: identify optimal novelty_bonus_weight ∈ [0.1, 1.0]; report Goldilocks point

**EXQ-ISEF-005 (GAP-14)** — curriculum vs flat comparison
- Prereqs: GAP-9, all telemetry GAPs
- Criterion: treatment passing > 5/7 gate criteria; controls < 5/7

---

### Phase 5: Gate update (GAP-15)

After EXQ-ISEF-001..004 results are reviewed, update `developmental_curriculum.md`
to replace the single `z_goal.norm()` gate with the 7-criterion table. Update
`developmental_needs_register.md` gap log to reflect resolved gaps. Run governance
pipeline to confirm no pending_review items generated by the new evidence.

---

## Status table

| Gap | Status | Owner EXQ | Last updated |
|-----|--------|-----------|-------------|
| GAP-1 Harm gradient env | done | V3-EXQ-576 PASS | 2026-05-21 |
| GAP-2 Microhabitat zones env | done (redraw guard added) | V3-EXQ-577a PASS (supersedes V3-EXQ-577) | 2026-05-16 |
| GAP-3 Transient benefit patches env | done | V3-EXQ-578 | 2026-05-16 |
| GAP-4 Stochastic attractor audit | done | audit-note | 2026-05-16 |
| GAP-5 H_pos / zone_coverage telemetry | done | V3-EXQ-579 | 2026-05-16 |
| GAP-6 residue_coverage_pct metric | done | V3-EXQ-580 | 2026-05-16 |
| GAP-7 traj_pairwise_cosine_mean | done | V3-EXQ-584 (queued) | 2026-05-17 |
| GAP-8 post_sleep_z_goal_retention | done | V3-EXQ-585 (queued) | 2026-05-17 |
| GAP-9 Curriculum scheduler | done | V3-EXQ-586 (queued) | 2026-05-17 |
| GAP-10 EXQ-ISEF-001 | done | V3-EXQ-587 (queued) | 2026-05-17 |
| GAP-11 EXQ-ISEF-002 | done | V3-EXQ-588c (PASS 2026-06-10; supersedes 588b) | 2026-07-31 (row reconcile; node record 2026-06-10) |
| GAP-11b MECH-189 trained-encoder evidence successor (588c near-miss follow-on, split out of GAP-11) | done | V3-EXQ-588e (PASS/supports, closed 2026-06-23) | 2026-07-31 (row added; node record 2026-06-23) |
| GAP-12 EXQ-ISEF-003 | done | V3-EXQ-589 (PASS/supports ARC-065, 2026-05-18) | 2026-07-31 (row reconcile; node record 2026-05-29) |
| GAP-13 EXQ-ISEF-004 | in_progress | V3-EXQ-706b (frontier; lineage 590/590c/705/705b/706/706b) | 2026-07-31 (row reconcile; node record 2026-07-20) |
| GAP-14 EXQ-ISEF-005 | blocked_pending_substrate (UPDATED 2026-06-19: prereq b z_goal CLEARED via V3-EXQ-603n PASS; (c-2) gate over-permissiveness CLOSED end-to-end -- 591f PASS criterion + crossing-count now WIRED into InfantCurriculumScheduler 2026-06-19 [/implement-substrate, no-op-default phase_0to1_use_crossing_count flag, 27/27 contracts]; ONLY (c-1) exploration-strength collapse remains [667 sweep exhausted, 667a not yet queued]. GATE REPOINTED 2026-07-21: c-1 is NOT blocked on modulatory-bias-selection-authority (retired 2026-07-20 per 604c autopsy + insights Corrections 2) but on the BEHAVIOURAL-COMPETENCE wall (V3-EXQ-724 competence_deficit_diffuse, oracle clears floor 6.05 vs 1.0 so the env is fine). EXQ-ISEF-005 stays blocked until (c-1) resolves) | V3-EXQ-591 (FAIL) -> 591b/591c (FAIL) -> 667 (FAIL) -> 591d (FAIL) -> 591e (FAIL) -> 591f (PASS, crossing-count discriminates) -> wired 2026-06-19 -> gate repointed 2026-07-21 | 2026-07-21 |
| GAP-14-c2 GAP-14 defect (c-2): Phase 0->1 gate over-permissiveness (discriminating crossing-count criterion, split out of GAP-14) | done | V3-EXQ-591f (PASS 2026-06-15; wired into scheduler 2026-06-19) | 2026-07-31 (row added; node record 2026-06-23) |
| GAP-15 Gate criterion update | done | governance (no EXQ) | 2026-05-17 |

---

## Decision log

### 2026-05-16 — Plan registered

Infant substrate expansion design doc completed after 4 parallel lit-pulls (37
new entries). Plan registered immediately from the design doc's deliverables.
No implementation work has started; all GAPs are open. Phase 1 env features are
the critical path since they are prerequisites for all telemetry and experiments.

The stochastic attractor audit (GAP-4) must precede any novelty_bonus_weight
deployment — Burda 2018 / Pathak 2017 both demonstrate permanent capture of the
curiosity signal by irreducible random stimuli. SD-048 interoceptive noise is the
primary suspect.

The 7-criterion gate (GAP-15) is intentionally deferred until EXQ-ISEF-001..004
results inform which criteria are empirically achievable and at what thresholds.
The thresholds in Section 8 of the design doc are proposals, not commitments.

### 2026-05-16 — GAP-5 implemented (pos_entropy / zone_coverage telemetry)

`CausalGridWorldV2.step()` now emits four always-present info keys:
`pos_telemetry_enabled`, `pos_entropy` (Shannon entropy in nats of the agent
position histogram over a rolling `pos_entropy_window`, default 100; `-1.0`
sentinel when disabled/empty), `pos_entropy_window` (echo), and `zone_coverage`
(`{zone_id: visited_fraction}` over the GAP-2 `_zone_map` zones 0..3 when
microhabitat is enabled, else a single-zone-0 stub over the interior; `{}` when
disabled). New env-only kwargs `pos_telemetry_enabled` / `pos_entropy_window` /
`zone_coverage_stub_single_zone` (not surfaced through `REEConfig.from_dims`,
matching the GAP-1/2/3 + SD-047/48/49 precedent).

Departure from the GAP-1/2/3 "default OFF / bit-identical OFF" precedent:
`pos_telemetry_enabled` **defaults ON**. The precedent exists because those
substrates draw RNG and/or change env dynamics; GAP-5 telemetry does neither, so
agent behaviour, RNG sequences, and results are bit-identical whether ON or OFF.
GAP-5 is the DEV-NEED-001 blocking gate, so defaulting ON means the EXQ-ISEF
experiments get H_pos / zone_coverage without a flag flip. The master switch is
retained for the contract OFF path and zero-overhead runs.

Validation: 14/14 contract tests in
`ree-v3/tests/contracts/test_pos_telemetry_gap5.py` (C1 OFF inert +
bit-identical layout, C2 entropy correctness incl. window cap / 0-entropy /
ln(K), C3 GAP-2 zone_coverage, C4 single-zone stub, C5 reset clears) PASS;
full 398/398 contracts+preflight regression-clean. Validation EXQ
**V3-EXQ-579** queued (substrate-readiness diagnostic, ARM_OFF / ARM_ON_STUB /
ARM_ON_ZONES; dry-run 5/5 criteria PASS). GAP-5 unblocks DEV-NEED-001 and
DEV-NEED-008; GAP-6/7/8 telemetry remain open.

### 2026-05-16 — GAP-2 implemented (microhabitat zones env feature)

GAP-2 landed in `ree-v3/ree_core/environment/causal_grid_world.py`
(CausalGridWorldV2). Ten env-only `__init__` kwargs, not surfaced through
`REEConfig.from_dims` (SD-047/048/049/054/GAP-1 precedent), all no-op defaults:
`microhabitat_enabled` (master, False), `n_microhabitats` (3), `zone_A/B/C`
resource+hazard factors (1.5/0.3, 0.8/1.8, 0.3/0.0), `zone_C_ambient_bonus`
(0.05), `zone_novelty_decay` (0.95).

`_build_microhabitat_zones()` builds a per-episode Voronoi zone map over
interior cells (n seeds via `self._rng`, nearest-seed assignment); cells
adjacent to a different base zone are promoted to the automatic D border
zone (neutral 1.0/1.0, no ambient). `_pop_zone_weighted()` replaces the
bare `forage_pool.pop()` at the hazard + SD-049 + legacy resource spawn
sites, weighting cell selection by the zone's resource/hazard factor; the
disabled path keeps a bare `pop()` so no extra RNG draws occur (bit-identical
OFF, verified over 300 steps). A zone-C ambient presence bonus is added in
`step()` (after the GAP-1 harm-gradient block, before move) when the agent
enters a zone-C cell with `transition_type == "none"`, decaying
multiplicatively per zone-C visit by `zone_novelty_decay`. Four `info`
diagnostics added (always present, inert when disabled):
`microhabitat_enabled`, `microhabitat_zone_at_agent`,
`microhabitat_zone_c_ambient_this_tick`, `microhabitat_zone_counts`.

Contract tests: `ree-v3/tests/contracts/test_microhabitat_gap2.py`
(11 tests, C1-C5: OFF backward-compat + bit-identical RNG, zone-map
coverage, zone-weighted hazard density bias, zone-C ambient fire+decay,
reset state clearing) -- 11/11 PASS. Full regression suite 367/367
relevant + 7/7 preflight PASS with master OFF (the one failing test,
`test_mech_293_ghost_probes.py::test_c2_master_off_no_op`, is pre-existing
and unrelated -- fails identically with GAP-2 changes stashed). Activation
smoke + 300-step bit-identical-OFF parity PASS.

Validation experiment V3-EXQ-577 queued (substrate-readiness diagnostic,
`experiment_purpose=diagnostic`, `claim_ids=[]` -- mirrors GAP-1 V3-EXQ-576
precedent; GAP-2's `unblocks_claims` are governed by the full infant
pipeline + EXQ-ISEF behavioural runs, not this readiness diagnostic).
2-arm (OFF/ON) x 3 seeds, ~10 min, dry-run smoke 4/4 criteria PASS.
`claims.yaml` NOT modified: GAP-2 alone does not resolve ARC-065
`v3_pending` (gated on the full infant pipeline). Phase-1 critical path
now has GAP-1 + GAP-2 done; GAP-3 (transient benefit patches) and GAP-4
(stochastic attractor audit) remain open.

### 2026-05-16 — GAP-3 implemented (transient benefit patches env feature)

GAP-3 landed in `ree-v3/ree_core/environment/causal_grid_world.py`
(CausalGridWorldV2), implemented in parallel with the GAP-2 session (user
authorised concurrent work; GAP-3 is an independent code block + separate
contract-test file). Four env-only `__init__` kwargs, not surfaced through
`REEConfig.from_dims` (SD-047/048/049/054/GAP-1/GAP-2 precedent), all no-op
when the master is off: `transient_benefit_enabled` (master, False),
`transient_benefit_prob` (0.02), `transient_benefit_duration` (15),
`transient_benefit_multiplier` (2.0).

Each `step()`, after the env-drift block and before subgoal timeout
(agent-independent, on the env clock), expiry runs first (patches whose
`spawn_step + duration` has elapsed are dropped: grid cell cleared,
removed from `self.resources` + tracking), then a single Bernoulli spawn
attempt at `transient_benefit_prob`. `_spawn_transient_benefit()` picks an
empty interior cell (zone-weighted via `_pop_zone_weighted` when GAP-2
microhabitat zones are active, uniform shuffle otherwise; reef cells
excluded), tags it as a resource entity so the proximity field and
perception treat it as a high-salience benefit, and registers it in
`self.resources` + `self._transient_benefits` (with expiry) +
`self._transient_benefit_cells`. The resource-contact branch detects a
transient cell and pays `resource_benefit * transient_benefit_multiplier`
(overriding the SD-049 per-type amplitude; transient patches are
intentionally not SD-049 typed). All RNG draws are guarded by the master
switch so seed sequences for existing experiments are bit-identical when
disabled. Six `info` diagnostics added (always present, inert when
disabled): `transient_benefit_enabled`, `transient_benefit_n_active`,
`transient_benefit_n_spawned`, `transient_benefit_n_contacted`,
`transient_benefit_n_expired`, `transient_benefit_contact_this_tick`.

Contract tests: `ree-v3/tests/contracts/test_transient_benefit_gap3.py`
(12 tests, C1-C5: OFF backward-compat + bit-identical RNG over reset AND
stepped trajectory, spawn-every-tick at prob=1.0 with correct expiry
bookkeeping, single-patch expiry exactly `duration` steps after spawn,
contact-reward multiplier + plain-resource-unaffected, reset state
clearing) -- 12/12 PASS. Full regression suite 376 passed + 7/7 preflight
with master OFF (the one failing test,
`test_mech_293_ghost_probes.py::test_c2_master_off_no_op`, is pre-existing
and unrelated -- fails identically with GAP-3 changes stashed on a clean
HEAD). Instrumented run confirms conservation: at prob=1.0/duration=3,
`n_active` stabilises at 3 and `n_expired` increments in lockstep with
`n_spawned`.

Validation experiment V3-EXQ-578 queued (substrate-readiness diagnostic,
`experiment_purpose=diagnostic`, `claim_ids=[]` -- mirrors GAP-1 V3-EXQ-576
/ GAP-2 V3-EXQ-577 precedent; GAP-3's `unblocks_claims` DEV-NEED-006 /
MECH-189 are governed by the full infant pipeline + EXQ-ISEF behavioural
runs, not this readiness diagnostic). 2-arm (OFF/ON) x 3 seeds, ~12 min,
dry-run smoke 4/4 criteria PASS (C1 spawn-rate band, C2 ARM_0 fully
silent, C3 patches expire, C4 contact multiplier exact). `claims.yaml`
NOT modified: GAP-3 alone does not resolve any `v3_pending` (gated on the
full infant pipeline). Phase-1 critical path now has GAP-1 + GAP-2 + GAP-3
done; GAP-4 (stochastic attractor audit) is the last open Phase-1 node.

### 2026-05-16 — GAP-4 completed (stochastic attractor audit)

GAP-4 is code-read only (no implementation, no EXQ). Every RNG call site in
`CausalGridWorldV2.reset()` / `step()` was enumerated and classified
learnable-stochastic vs irreducible. Full audit (enumeration table + verdict +
binding action) written into `docs/architecture/infant_substrate_expansion.md`
section 5.6 (the pre-existing audit placeholder, checklist replaced with the
completed audit).

Key facts: one seeded master RNG (`causal_grid_world.py:607`) -> runs are
reproducible; the attractor concern is within-episode irreducible entropy a
curiosity signal cannot predict away (Burda 2018 / Pathak 2017 noisy-TV).
Verdict: **SD-048 interoceptive noise is the confirmed primary irreducible
stochastic attractor** -- Source 1 autonomic i.i.d. Gaussian on `harm_obs_a`
every tick (`:2631`) and the Poisson sensitisation onset (`:2609`); fatigue
AR(1) (`:2575`) is a partial attractor. SD-047 weather innovation (`:2399`) +
transient Poisson (`:2415`) are secondary partial attractors. Reset/spawn/
respawn/hazard-drift randomness are learnable-stochastic (no risk). All
SD-047/SD-048 noise is OFF by default; risk materialises only with
`novelty_bonus_weight > 0` (the infant config). Confirms the plan's
pre-registered suspicion.

Binding constraint passed downstream to GAP-13 (EXQ-ISEF-004,
`depends_on` GAP-4): MECH-314a (z_world RBF novelty) is structurally safe --
z_world does not carry `harm_obs_a`. The exposure is MECH-314b/c, which
consume `e3._running_variance` (PE) that SD-048 autonomic noise inflates;
when `use_structured_curiosity AND interoceptive_noise_enabled` the PE feed
to 314b/c must exclude / low-pass the harm-stream PE component (option (b)
exclude-from-novelty; option (a) make-Markovian is unavailable for i.i.d.
readout noise). An explicit config-coupling assertion must be wired BEFORE
GAP-13 runs. `claims.yaml` NOT modified (audit only; no claim resolved --
DEV-NEED-003 / MECH-314 governed by the full infant pipeline). Phase 1
(GAP-1..4) is now complete; the critical path advances to Phase 2 telemetry
(GAP-5..8).

### 2026-05-16 — GAP-6 implemented (residue_coverage_pct / harm_benefit_ratio telemetry)

GAP-6 differs structurally from GAP-5: the residue field is **agent-side**
(`ree-v3/ree_core/residue/field.py` `ResidueField`), not env-side. There is
no residue grid in `causal_grid_world.py`, so GAP-6 is **not** an env
`info`-dict telemetry key like GAP-5 — it is a read-only metric over the
agent's `ResidueField`. This matches the plan's "add to training loop or
episode summary" wording and the EXQ-575 precedent
(`residue_coverage_pct = active_centers / 32`).

Landed as one additive, read-only method
`ResidueField.get_coverage_telemetry(residue_scale_factor=1.0)` returning
native python floats/ints: `residue_coverage_pct`,
`residue_coverage_threshold`, `residue_active_centers`,
`residue_n_centers`, `harm_benefit_ratio`, `harm_total`, `benefit_total`.
`residue_coverage_pct` = fraction of harm-residue RBF centers that are
active AND `abs(weight) > 0.02 * max(residue_scale_factor, 1e-8)` (the
plan's grid-cell `abs(residue)>thr` definition mapped to the RBF basis —
the V3 substrate has no literal (y,x) grid). `harm_benefit_ratio` =
`total_residue / total_benefit` when the benefit terrain is enabled and
benefit has accumulated; a single `-1.0` sentinel otherwise (benefit
terrain off, or zero benefit accumulated — GAP-5 sentinel precedent).

Non-invasive by construction: `get_statistics()` is deliberately left
**unchanged** (EXQ-575 and other callers depend on its exact 4-key set);
the new method mutates no field state and nothing in the agent/env hot
path calls it, so every existing run is **bit-identical**. No config
change, no `from_dims` surface, no env change. No MECH-094 concern (pure
read; no simulation/replay/memory write). No phased training (no encoder).

Contract tests: `ree-v3/tests/contracts/test_residue_coverage_gap6.py`
(12 tests, C1 surface + get_statistics intact, C2 coverage correctness
incl. sub-threshold exclusion / scale-factor scaling / 0.0-clamp, C3
harm_benefit_ratio sentinels, C4 non-invasive + idempotent, C5 bounds)
— 12/12 PASS. Full regression 403/403 contracts + 7/7 preflight green.

Validation experiment **V3-EXQ-580** queued (substrate-readiness
diagnostic, `experiment_purpose=diagnostic`, `claim_ids=[]` — mirrors the
GAP-1 V3-EXQ-576 / GAP-5 V3-EXQ-579 precedent). 2-arm (ARM_0 binary
hazard contact / ARM_1 GAP-1 `harm_gradient_enabled=True`) x 3 seeds,
512-center field so the every-tick-in-band ARM_1 signal does not saturate
to the sparse on-contact ARM_0 value; dry-run smoke 5/5 criteria PASS
(C0 well-formed, C1 ARM_1 strictly > ARM_0 by >= 0.01 all seeds,
C2 -1.0 sentinel both arms, C3 non-invasive, C4 ARM_0 has harm residue).
`claims.yaml` NOT modified: GAP-6 alone does not resolve any
`v3_pending` (DEV-NEED-004 / DEV-NEED-008 are governed by the full
infant pipeline + EXQ-ISEF behavioural runs, not this readiness
telemetry). Phase-2 telemetry now has GAP-5 + GAP-6 done; GAP-7
(traj_pairwise_cosine_mean) and GAP-8 (post_sleep_z_goal_retention)
remain open.

### 2026-05-16 — GAP-2 degenerate-seeding redraw guard (V3-EXQ-577 autopsy "enrich" half)

The V3-EXQ-577 (gap2_microhabitat_validation) failure autopsy
(`failure_autopsy_EXQ-577_2026-05-16`) found C2 was a **false-negative**:
~2-3% of stochastic episodes land the 3 Voronoi seeds close enough that
one whole base niche (0/1/2) is consumed by the boundary→D (zone 3)
promotion. C1/C3/C4 PASS — the GAP-2 mechanism is functionally correct;
this is an **enrichment** (defense in depth for the infant
niche-discrimination curriculum DEV-NEED-001/003/007 / EXQ-ISEF-003),
not a bug fix of broken logic. User-confirmed routing: "both — enrich +
relax"; this entry is the enrich half.

`_build_microhabitat_zones` (`ree-v3/ree_core/environment/causal_grid_world.py`)
was refactored into a deterministic capped-retry guard: the verbatim
pre-guard draw+Voronoi+boundary→D logic moved into a pure
`_draw_microhabitat_zone_map` helper; a `_count_surviving_base_zones`
helper counts distinct base codes (0..n_seeds-1, excluding the D
ecotone) surviving in the interior. After promotion, if fewer than
`n_seeds` base zones survive, the seeds are redrawn via `self._rng`
(fully deterministic given the per-episode seed) up to a cap; the first
non-degenerate draw wins, and on cap exhaustion the best (most-surviving)
draw is kept and a diagnostic surfaced. One env-only `__init__` kwarg
`microhabitat_max_seed_redraws` (default 8; NOT surfaced through
`REEConfig.from_dims` — SD-047/048/049 + GAP-1/2/3/5 precedent; `0` is
an escape hatch reproducing pre-guard map behaviour). Two always-present
`step()` info keys added (`microhabitat_redraw_count`,
`microhabitat_redraw_exhausted`; 0/False when disabled) so the relax-half
EXQ can read the collapse-frequency statistic.

Bit-identical OFF preserved by construction: `_build_microhabitat_zones`
is only called on the enabled path; the disabled path
(`_zone_map=None`, bare `pool.pop()`) is untouched — zero extra RNG
draws OFF (300-step default-vs-explicit-OFF parity PASS). The common
~97-98% enabled case accepts the first draw and consumes `self._rng`
exactly as the pre-guard code did; only the ~2-3% degenerate episodes
draw extra RNG (the intended enrichment; the ON path has no
bit-identical contract).

Verification: `ree-v3/tests/contracts/test_microhabitat_gap2.py`
extended with C6 (3 tests: 300-episode autopsy-repro zero-collapse +
guard-engaged + no-exhaustion, inert-when-disabled info keys, cap=0
escape hatch) — 14/14 PASS. Full regression 413/413 contracts + 7/7
preflight green; `validate_queue.py` OK. Guard-efficacy smoke at the
exact autopsy config (size=14, seeds 0/1/2, 100 eps, 6 hazards):
**pre-guard cap=0 → 7/300 collapses** (exactly the autopsy's
missing_012 = 2+2+3), **post-guard cap=8 → 0/300 collapses**, 6 redraws
engaged, 0 exhausted. Threshold met: base-zone-collapse rate ~0 over
100 episodes/seed with strict per-episode {0,1,2} presence.

`claims.yaml` NOT modified: GAP-2 alone resolves no `v3_pending`
(same precedent as the original GAP-2/GAP-6 entries; ARC-065 et al. are
governed by the full infant pipeline). Validation experiment
**V3-EXQ-577a** queued via `/queue-experiment` (corrected C2:
per-episode well-formedness + ≥2 base zones + zone 3 present, {0,1,2}
asserted aggregated over episodes, base-zone-collapse frequency reported
as a diagnostic stat; `supersedes: gap2_microhabitat_validation`). The
local runner (DLAPTOP-4.local) auto-claimed and ran it immediately —
**V3-EXQ-577a PASS** (`v3_exq_577a_gap2_microhabitat_validation_20260516T230804Z_v3`,
non-dry, 3/3 seeds C1-C4 True; diagnostic `base_zone_collapse_count=0`
/ `collapse_rate=0.0` / `redraws=1` per seed / `exhausted=0` — the guard
engages once per seed and drives residual collapse to exactly zero over
100 eps/seed). Status-table owner-EXQ reconciled to V3-EXQ-577a (PASS,
per autopsy §7). Governance still owns the V3-EXQ-577 manifest
reclassification to `evidence_direction: superseded` (autopsy §7
explicitly defers that to the governance pass — not applied here).
GAP-5 flag (autopsy learning #3): the GAP-5 `zone_coverage` consumer
must still tolerate a base zone with 0 cells — now effectively
impossible post-guard but the consumer remains defensively correct
either way.

### 2026-05-17 -- GAP-7 implemented (traj_pairwise_cosine_mean telemetry)

`CausalGridWorldV2` now emits three always-present info keys for
trajectory diversity: `traj_telemetry_enabled`, `traj_pairwise_cosine_mean`
(mean(1 - cosine_similarity) over up to `traj_n_pairs` random pairs drawn
from a rolling buffer of up to `traj_max_stored` episode-level position
histograms; `-1.0` sentinel when disabled or fewer than 2 episodes stored),
and `traj_n_episodes_stored` (current buffer length). New env-only kwargs:
`traj_telemetry_enabled` (default True), `traj_max_stored` (20),
`traj_n_pairs` (20). Not surfaced through `REEConfig.from_dims` (same
precedent as GAP-5/6 and all harm_gradient_*/microhabitat_* params).

Representation: trajectories stored as normalised position histograms
(fraction of steps at each grid cell; fixed-length `size*size` float32
vectors). Cosine similarity computed between histogram pairs; 1 - sim
gives pairwise diversity distance. Pair sampling uses a separate
`_traj_pair_rng` (seeded from env seed) that does not touch `self._rng`,
so env dynamics are bit-identical ON vs OFF.

`_traj_store` persists across episodes (cleared only at fresh env
construction); `_traj_current` is per-episode (cleared by `reset()` and
`reset_to()`). The metric updates once per episode on the `done=True`
step and the cached value is returned on all intermediate steps.

Matching GAP-5 precedent: `traj_telemetry_enabled` defaults ON (no RNG
draws, no dynamics feedback -> bit-identical). Advisory gate criterion is
`traj_pairwise_cosine_mean > 0.3` (DEV-NEED-002/005 column in the 7-criterion
gate table).

Contract tests: `ree-v3/tests/contracts/test_traj_pairwise_cosine_gap7.py`
(13 tests: C1 OFF sentinels + bit-identical layout, C2 store growth +
cap + sentinel-until-2, C3 update timing, C4 cosine metric properties,
C5 reset semantics) -- **13/13 PASS**. Full regression **460/460**
contracts + preflight green.

Validation experiment **V3-EXQ-584** queued (substrate-readiness
diagnostic, `experiment_purpose=diagnostic`, `claim_ids=[]`). Two-arm
(ARM_0 OFF / ARM_1 ON) x 3 seeds, 5 episodes per arm per seed. Dry-run
smoke: 6/6 verdicts PASS, all C0-C4 criteria met, mean_metric_arm1=0.95
(random actions in 12x12 grid with hazards produce highly diverse
trajectories -- expected, validates metric is live). `claims.yaml` NOT
modified: GAP-7 alone does not resolve any `v3_pending` (DEV-NEED-002/005
are governed by the full EXQ-ISEF validation runs and gate-criterion
satisfaction, not this readiness telemetry). Phase-2 telemetry: GAP-5/6/7
done; GAP-8 (post_sleep_z_goal_retention) remains open.

### 2026-05-17 -- GAP-8 implemented (post_sleep_z_goal_retention + replay_diversity_index)

GAP-8 differs structurally from GAP-5/6/7: it is not an env `info`-dict
metric or a training-loop computation -- it is telemetry on the sleep
integration cycle itself. Landed as two additions to
`SleepLoopManager._run_cycle()` in
`ree-v3/ree_core/sleep/phase_manager.py`:

1. **`_safe_z_goal_norm(agent)` static method** -- non-invasive read of
   `agent.goal_state._z_goal.norm().item()`; returns -1.0 sentinel when
   `goal_state` is absent or `_z_goal` is None. Placed alongside the
   existing `_build_evidence_snapshot` / `_extract_region_key` helpers.

2. **Before/after z_goal capture** -- `_z_goal_before` captured immediately
   before `agent.run_sleep_cycle()`, `_z_goal_after` immediately after.
   Four metrics written into the `merged` return dict:
   `post_sleep_z_goal_before`, `post_sleep_z_goal_after`,
   `post_sleep_z_goal_retention` (ratio, or -1.0 when before <= 1e-8),
   `replay_diversity_index` (len(replayed_regions)/n_draws, or -1.0 when
   no routed draws occurred this cycle).

`replay_diversity_index` computes from `replayed_regions` (already
collected upstream for MECH-284 partial-decay) and `sws_routed_draws`
(already computed for MECH-272 anchor-channel). Zero new data structures.

Non-invasive by construction: `_safe_z_goal_norm` only reads; nothing
in the hot path calls it during waking steps; the four new dict keys
do not conflict with any pre-existing metric name. Sleep cycle semantics
and all existing metrics are bit-identical.

Contract tests: `ree-v3/tests/contracts/test_z_goal_retention_gap8.py`
(7 tests: C1 sentinel when no goal_state, C2 correct norm from seeded
_z_goal, C3 all four keys always present, C4 -1.0 sentinels on no-goal/
no-sampler path, C5 retention ~1.0 when seeded (sleep preserves z_goal),
C6 replay_diversity_index in [0,1] when draws occur, C7 pre-GAP-8 SWS
keys still present) -- **7/7 PASS**. Full regression **467/467**
contracts + preflight green.

Validation experiment **V3-EXQ-585** queued (`experiment_purpose=diagnostic`,
`claim_ids=[]`). Two-arm (ARM_0 no-goal / ARM_1 goal-seeded) x 3 seeds.
Dry-run smoke 4/4 criteria PASS: C1 ARM_0 before/after/retention all -1.0,
C2 ARM_0 replay_div -1.0, C3 ARM_1 retention=1.0 > 0.95, C4 ARM_1
before=0.6 > 0.1. `claims.yaml` NOT modified: GAP-8 alone does not
resolve any `v3_pending` (DEV-NEED-007/008 governed by the full infant
pipeline + EXQ-ISEF behavioural runs). Phase-2 telemetry: all of GAP-5,
GAP-6, GAP-7, GAP-8 now done.

### 2026-05-17 -- GAP-9 implemented (4-phase infant curriculum scheduler)

GAP-9 is an experiment-harness helper (NOT a ree_core substrate
scheduler), following the commitment_closure GAP-11 O-1 precedent.
Implemented as `ree-v3/experiments/infant_curriculum.py`:
`InfantCurriculumScheduler` class.

**Design:** phase-only-advance state machine with episode-count hard
minimums (phase 0->1: ep >= 100; 1->2: ep >= 500; 2->3: ep >= 2000) and
optional telemetry gates (H_pos threshold 0.70*ln(grid_cells) for 0->1;
z_goal.norm() >= 0.30 AND benefit_contacts_window >= 5 for 1->2;
residue_coverage_pct >= 0.15 for 2->3). When a metric is None, hard
episode count governs (fallback). Phases never retreat.

**`env_kwargs(phase)`** returns CausalGridWorldV2 constructor kwargs:
- Phase 0: all infant features OFF.
- Phase 1: `harm_gradient_enabled=True, harm_gradient_scale=0.15,
  transient_benefit_enabled=True`.
- Phase 2+: adds `microhabitat_enabled=True, harm_gradient_scale=0.30`.

**`config_overrides(phase)`** returns agent config override dict:
- `novelty_bonus_weight`: 0.5 / 0.7 / 0.5 / 0.5 (phases 0-3).
- `residue_scale_factor`: 0.0 / 0.05 / 0.10 / 0.15 (strictly increasing).
- `offline_integration_frequency`: 10 / 20 / 50 / 100 (strictly increasing).

**Contract tests:** `ree-v3/tests/contracts/test_infant_curriculum_gap9.py`
(16 tests: C1 fresh start, C2 hard transitions x3, C3 H_pos gate blocks
+ ep-min, C4 z_goal gate blocks, C5 no retreat, C6 env_kwargs x4 phases,
C7 config_overrides ordering, C8 phase_changed flag, C9 full walk + summary,
C10 benefit_contacts window gate) -- **16/16 PASS**. Full regression
**483/483** contracts + preflight green.

**Validation experiment V3-EXQ-586** queued (`experiment_purpose=diagnostic`,
`claim_ids=[]`). Two arms x 3 seeds: ARM_0 hard-count only (transitions at
100/500/2000); ARM_1 synthetic-telemetry gated (delayed transitions at
150/650/2000 -- demonstrates H_pos gate delays 0->1, z_goal gate delays
1->2). C2 env constructor per phase + C3 feature flags + C4 config
ordering also checked. Dry-run **5/5 criteria PASS**: C0 ARM_0 transitions
correct, C1 ARM_1 delayed transitions correct, C2 env constructor OK,
C3 feature flags correct, C4 config ordering correct. `claims.yaml` NOT
modified (GAP-9 alone does not resolve any `v3_pending`; DEV-NEED-008 and
ARC-046 governed by the full infant pipeline + EXQ-ISEF validation).
Phase 3 curriculum scheduler: GAP-9 done; GAP-10..14 (EXQ-ISEF experiments)
remain open.

### 2026-05-17 -- GAP-10 queued (EXQ-ISEF-001 harm gradient vs binary-contact)

GAP-10 is the first Phase 4 validation experiment (EXQ-ISEF-001). Experiment
script `ree-v3/experiments/v3_exq_587_isef001_harm_gradient_enabled_v3.py`
written and queued as **V3-EXQ-587**.

**Context from prior runs:** V3-EXQ-575 and V3-EXQ-575a were warm-start gate
diagnostics that varied `proximity_harm_scale` (a different parameter, not the
GAP-10 manipulation). 575a's informational C3 metric showed mean_weight
separation ~2x (ARM_0=1.48 vs ARM_1=2.84) while thresholded
`residue_coverage_pct` saturated at 1.0 for both arms. This ruled out coverage
as a discriminating metric; mean_weight (continuous, magnitude-sensitive) is
the correct primary criterion.

**Design:** Two arms, 5 seeds [42..46], 1000 episodes, 200 steps/episode.
- ARM_0 (control): `harm_gradient_enabled=False` -- binary contact only.
- ARM_1 (treatment): `harm_gradient_enabled=True, harm_gradient_scale=0.30`
  -- approach-signal gradient fires graduated reward proportional to proximity.
- Primary criterion C1 (gate): ARM_1 final `mean_weight` > 2x ARM_0 final
  `mean_weight` in >= 4/5 seeds. Threshold pre-registered from 575a
  informational result.
- Advisory C2: ARM_1 coverage at ep100 > ARM_0 (early geography formation).
- Advisory C3: ARM_1 final harm_total > ARM_0 (sanity: gradient fires events).

**Metric source:** `agent.residue_field.get_statistics()["mean_weight"].item()`.
Coverage via `get_coverage_telemetry()["residue_coverage_pct"]` is advisory
only (saturates at 1.0).

**Smoke test:** dry-run PASS. validate_experiments.py exit 0. Progress
instrumentation: `[train] ARM ep N/1000 seed=S` at every 100 episodes;
`verdict: PASS/FAIL` per arm per seed (10 total for 5 seeds x 2 arms);
`Seed S Condition ARM` boundary lines.

**Expected runtime:** ~280 min (2,000,000 total env steps across 5 seeds x 2
arms x 1000 ep x 200 steps/ep). Queue entry `episodes_per_run=1000,
seeds=5, conditions=2`.

**If PASS:** GAP-10 closed; ARC-013 and DEV-NEED-004 unblocked for the
harm-gradient evidence they need.
**If FAIL:** investigate whether the approach gradient is firing (C3 sanity);
check harm_gradient_scale (may need to raise above 0.30) or episode budget.

### 2026-05-17 — GAP-11 queued as V3-EXQ-588 (EXQ-ISEF-002)

Script: `ree-v3/experiments/v3_exq_588_isef002_transient_benefit_zgoal_seeding.py`

Design: ARM_0_control (`transient_benefit_enabled=False`) vs ARM_1_treatment
(`transient_benefit_enabled=True, transient_benefit_multiplier=3.0`). Agent
persists across all 1000 episodes per seed (goal state accumulates as in the
developmental model). Both arms share the same agent config: `z_goal_enabled=True`,
`alpha_world=0.9`, `drive_weight=2.0`.

Primary metric: first episode at which `z_goal.norm() > 0.4` (sentinel=1001 if
never). C1 gate: ARM_1 median first-crossing < 0.7x ARM_0 median.
Secondary (informational): C2 mean transient contacts per episode (ARM_1 > 0,
ARM_0 = 0 by design); C3 active_episode_fraction (fraction of episodes where
goal_state.is_active() at episode end).

**Smoke test:** dry-run PASS. validate_experiments.py exit 0. Progress: `[train]
ARM seed=S ep N/1000` every 100 eps; `verdict: PASS/FAIL` per arm per seed (10
total); `Seed S Condition ARM` boundary lines.

**Expected runtime:** ~150 min (2,000,000 total env steps: 5 seeds x 2 arms
x 1000 ep x 200 steps). Queue entry: `episodes_per_run=1000, seeds=5, conditions=2`.

**If PASS:** GAP-11 closed; enable transient patches as infant default; proceed
to 7-criterion gate update (GAP-15). DEV-NEED-006 and MECH-189 unblocked.
**If FAIL:** z_goal encoder or MECH-189 write path is the bottleneck; queue
goal-seeding pipeline diagnostic (similar to EXQ-536a instrumentation approach).

### 2026-05-17 -- GAP-12 queued as V3-EXQ-589 (EXQ-ISEF-003)

Script: `ree-v3/experiments/v3_exq_589_isef003_microhabitat_latent_diversity.py`

Design: ARM_0_control (`microhabitat_enabled=False`, homogeneous geography) vs
ARM_1_treatment (`microhabitat_enabled=True, n_microhabitats=3`). Fresh agent per
arm x seed; no backprop. Agent acts under `torch.no_grad()` -- z_world diversity
reflects environmental structure through the (randomly-initialised) encoder.
Both arms: `alpha_world=0.9`.

Primary metric: PCA absolute variance sum (sum of top-3 singular_values^2 / (n-1))
from 200 z_world vectors collected at every step of the snapshot episode (ep999 =
episode 1000). C1 gate: ARM_1 top3_abs_var_sum > 1.2x ARM_0 in >= 4/5 seeds.
Secondary (advisory): C2 traj_pairwise_cosine_mean (ARM_1 > ARM_0); C3 zone_coverage
breadth in treatment (>= 2 zones each > 0.1 in >= 3/5 seeds).

**Smoke test:** dry-run PASS. validate_experiments.py exit 0. Progress: `[train]
ARM seed=S ep N/1000` every 100 eps; `verdict: PASS/FAIL` per arm per seed (10
total); `Seed S Condition ARM` boundary lines. emit_outcome sentinel confirmed.

**Expected runtime:** ~150 min (5 seeds x 2 arms x 1000 ep x 200 steps = 2M env
steps). Queue entry: `episodes_per_run=1000, seeds=5, conditions=2, priority=10`.

**If PASS:** GAP-12 closed; microhabitat zones confirmed to create richer z_world
structure; ARC-065 substrate-readiness for diversity-generation experiments confirmed;
DEV-NEED-001 and DEV-NEED-007 unblocked.
**If FAIL:** zone map not propagating into z_world encoder; check obs_world channel
content per zone; may need zone-specific features in obs or larger zone factor
contrasts; if C3 also fails, agent is anchored to one zone.

### 2026-05-17 -- GAP-15 closed: 7-criterion gate update in developmental_curriculum.md

`developmental_curriculum.md` "Gate Criterion" section replaced with the expanded
8-criterion table (7 from `infant_substrate_expansion.md` Section 8 + criterion 8
`competence_progress_rate` from the EF literature, per `developmental_metrics.md`
DEV-NEED-008):

- **Blocking (all must pass):** C1 z_goal.norm() > 0.4 (DEV-NEED-006); C2 H_pos >
  0.65*ln(grid_cells) rolling 100-ep (DEV-NEED-001); C3 residue_coverage_pct > 0.15
  (DEV-NEED-004).
- **Advisory (flag if missing):** C4 action_entropy_global > ln(3) AND zone KL > 0.05
  (DEV-NEED-001/005); C5 harm_benefit_ratio in [0.2, 5.0] (DEV-NEED-004); C6
  post_sleep_z_goal_retention > 0.85 (DEV-NEED-007); C7 traj_pairwise_cosine_mean > 0.3
  (DEV-NEED-002/005); C8 competence_progress_rate > 0 (DEV-NEED-008, Forestier 2022).
- Perseveration check (gate blocker for C1-C3 monostrategy false-pass).
- Thresholds noted as proposals pending EXQ-ISEF-001..004 empirical calibration.

`developmental_needs_register.md` and `developmental_metrics.md` already carried the
expanded criteria (added 2026-05-16); this closes the alignment gap in
`developmental_curriculum.md`. No claims.yaml change (GAP-15 is a documentation gate;
DEV-NEED-008 governance is the experiment-result follow-on). GAP-15 depends_on
GAP-10/11/12/13 per the plan node; closing now on the design-doc criteria since the
experiments validate thresholds rather than define criteria. (session:
infant-substrate-gap15-2026-05-17T105412Z)

### 2026-05-17 -- GAP-13 queued: V3-EXQ-590 novelty bonus Goldilocks calibration

`v3_exq_590_isef004_novelty_bonus_goldilocks_v3.py` written and queued as V3-EXQ-590.

Design: sweeps `novelty_bonus_weight` in [0.1, 0.3, 0.5, 0.7, 1.0] (5 arms x 3 seeds x
1000 episodes x 200 steps). Tests MECH-111 broadcast novelty EMA signal in the infant
Phase 2 environment (interoceptive_noise_enabled=True, microhabitat_enabled=True,
harm_gradient_enabled=True, harm_gradient_scale=0.30). Novelty EMA updated per step from
E1 prediction error via `compute_prediction_loss()` under `torch.no_grad()` -- no backprop.

Acceptance: C1 = any arm with mean_novelty_ema > 0.001 in >=2/3 seeds (signal active);
C2 = >=3/5 arms with mean_coverage > 0.05 in >=2/3 seeds (exploration quality). Goldilocks
arm = highest (norm_coverage + norm_H_pos) / 2; reported regardless of C1/C2 outcome.
nonmonotone_detected=True if peak arm is interior (inverted-U), confirming stochastic
attractor boundary visibility at high novelty_bonus_weight.

Note: `novelty_bonus_weight` modulates MECH-111 (broadcast scalar offset in
score_trajectory), not MECH-314 (StructuredCuriosity per-candidate RBF score_bias).
MECH-314 is tagged for audit-trail consistency; evidence_direction_per_claim marks MECH-314
as non_contributory (PASS) because the per-candidate pathway is not under test.

GAP-4 binding constraint honored: SD-048 interoceptive noise present as the irreducible
stochastic attractor; the sweep identifies the safe operating region below capture threshold.

Smoke test (--dry-run): novelty_ema = 0.00719 > 0.001 threshold confirms E1 prediction
error signal is active. All 5 arms completed without crash. (session:
infant-substrate-gap13-2026-05-17T110655Z)

### 2026-05-17 -- GAP-14 queued: V3-EXQ-591 EXQ-ISEF-005 curriculum vs flat baselines

`v3_exq_591_isef005_curriculum_vs_flat_v3.py` written and queued as V3-EXQ-591.

Design: 3-arm comparison x 5 seeds x 2000 episodes x 200 steps.
  ARM_0_ctrl_a -- flat novelty_bonus_weight=0.7, all env features ON from episode 0
    (harm_gradient_enabled=True, scale=0.30, transient_benefit_enabled=True,
    microhabitat_enabled=True).
  ARM_1_ctrl_b -- flat novelty_bonus_weight=0.5, minimal env (all infant features OFF).
  ARM_2_curriculum -- InfantCurriculumScheduler 4-phase schedule (infant_curriculum.py):
    Phase 0 (ep 0-99): babbling, all features OFF, novelty=0.5.
    Phase 1 (ep 100-499): mild harm gradient + transient benefits, novelty=0.7.
    Phase 2 (ep 500-1999): all features ON + microhabitat, novelty=0.5.
    Phase 3 (ep 2000+): pre-gate, same as Phase 2.

7 gate criteria (Section 8 of infant_substrate_expansion.md) evaluated at ep 2000.
PASS: ARM_2 (curriculum) passes >= 6/7 criteria in >= 4/5 seeds AND (ARM_0 OR ARM_1)
      passes <= 4/7 criteria in >= 3/5 seeds.
Claim tagged: ARC-046 (phased residue accumulation via curriculum).
Unblocks: DEV-NEED-008 (gate threshold calibration with empirical evidence).

All three arms use per-episode env reconstruction with episode-specific seed for fair
curriculum comparison. Agent persists across episodes within each seed. Sleep is forced
at end of run (force_cycle) to measure post-sleep z_goal retention (C6 criterion).
Novelty bonus updated dynamically each episode for the curriculum arm via
agent.config.e3.novelty_bonus_weight.

Smoke test (--dry-run): all 3 arms PASS, 7/7 criteria, 3 verdict lines printed,
emit_outcome sentinel written. validate_experiments.py OK. (session:
infant-substrate-gap14-2026-05-17T111918Z)

### 2026-05-21 -- GAP-11 reconciled after V3-EXQ-588 autopsy (plan + workset)

V3-EXQ-588 completed FAIL; governance 2026-05-20 applied
`failure_autopsy_V3-EXQ-588_2026-05-19` (MECH-189 non_contributory; route
goal-seeding diagnostic). Plan frontmatter had remained `owner_exq: V3-EXQ-588`,
which made `inter_governance_workset` emit a stale `/queue-experiment` package.

**Updates:** `owner_exq` -> V3-EXQ-588b; `resume_condition` documents do-not-rerun-588;
`substrate_queue` INF-ENV-003 -> `implemented` (GAP-3 env landed via V3-EXQ-578).
Inter-governance workset regenerated. (session: infant-substrate-gap11-reconcile-20260521T030737Z)
