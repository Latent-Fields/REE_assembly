---
closure_plan:
  id: arc_062_rule_apprehension
  title: "Rule Apprehension"
  registered: 2026-05-09
  last_updated: 2026-09-01
  scope_claims: [MECH-309, ARC-062, ARC-063, ARC-064, ARC-065, ARC-077, MECH-337, MECH-338, MECH-312, MECH-312a, MECH-312b, MECH-312c, MECH-312d, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-316, MECH-317, MECH-318, MECH-319, Q-043, Q-044, Q-045, SD-054, SD-029, MECH-269]
  sibling_plans: [commitment_closure, sleep_substrate, sd033_governance, goal_pipeline, self_attribution, behavioral_diversity_isolation, conversion_ceiling_campaign]
  nodes:
    - id: "arc_062_rule_apprehension:GAP-A"
      title: "ARC-062 substrate implemented and readiness-validated (gated-policy heads + learned context discriminator)"
      status: done
      severity: load-bearing
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-062, MECH-309]
      depends_on: []
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-06-08
      governance_2026_06_08: "Plan-drift reconcile. V3-EXQ-542a is the canonical substrate-readiness truth for GAP-A: the gated-policy substrate exists and passed UC1-UC6 as a diagnostic/non-governance-weighting validation. Status remains done; no new experiment is owed under GAP-A."
    - id: "arc_062_rule_apprehension:GAP-B"
      title: "MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness"
      status: in-progress
      severity: load-bearing
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      governance_2026_06_19: "FALSIFIER RAN + ADJUDICATED INLINE (/governance cycle 2026-06-19T21:41Z; NO claim-scoring move). V3-EXQ-654g -- the GAP-B falsifier on the de-locked CRF + 569i top-k shortlist stack the 654f autopsy called for -- RAN FAIL/non_contributory 2026-06-19T21:31Z (ree-cloud-4) and was reviewed this cycle. THE MATURED-AND-FIRING TEST the lineage owed has now run and the prediction held: C1 FULLY MET (crf_frac_active 0.94, GAP-A divergence 0.080, propagation non-vacuous, within-arm counterfactual delta 0.0021 nonzero) yet C2 committed-class entropy lift is +0.011 nats / 0/3 seeds. CONFIRMED: it is the selection-authority CONVERSION coupling (MECH-439 F-dominance live root), not CRF maturation, that is the ceiling -- the matured+active+differentiated rule_state reaches committed action but cannot move the F-dominated committed argmax. Second behavioural channel after V3-EXQ-485h (OFC) to corroborate MECH-439. User-confirmed inline disposition (no new autopsy -- a pre-registered, non-degenerate self-route to the already-mapped MECH-439 ceiling; the 654 instrumentation lineage cleanly terminated). Applied: claims.yaml ARC-062 + MECH-309 evidence_quality_note 654g entries (no status change); 654f -> superseded (manifest + index); substrate_queue ARC-062 += 654g failure_record, crf-availability-maintenance marked complete (residual is conversion ceiling, not a CRF fault); 654g reviewed; owner_exq advanced 654f -> 654g. Route: /implement-substrate GAP-A gain/contrast amend; the conversion-ceiling chain (ARC-065 569i top-k ceiling-lifted / 689a / 625e) already carries it. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate. Status stays in-progress (GAP-B closes only on a PASS C2 lift, which requires the F-dominance rebalance). last_updated 2026-06-18 -> 2026-06-19."
      unblocks_claims: [MECH-309, ARC-062]
      depends_on: ["arc_062_rule_apprehension:GAP-A"]
      cross_plan_link: ["commitment_closure:GAP-1", "behavioral_diversity_isolation:GAP-I", "conversion_ceiling_campaign:FULLSTACK"]
      blocked_by: []
      diagnostic_recurrence_metabolized:
        date: 2026-08-14
        metabolized_hits:
          - v3_exq_906b_full_stack_observational_fishtank_20260809T163034Z_v3
          - v3_exq_906c_full_stack_observational_fishtank_20260810T014711Z_v3
          - v3_exq_911_ecology_enrichment_fishtank_20260809T201208Z_v3
        covers_tokens:
          - fishtank_906_lineage_ecology_showcase
        note: >
          GOV-DIAG-1's prescribed response was carried out IN FULL for the
          906b -> 906c -> 911 fishtank ecology-showcase chain (routed by
          /governance 2026-08-12, session sd-016-h3-algorithm-3370cd; executed by
          chip-20260812-govdiag1-repose-fishtank906). Full attribution +
          re-operationalization: evidence/planning/govdiag1_repose_fishtank906_2026-08-12.md.
          PROMOTES/DEMOTES NOTHING -- no claims.yaml edit, no experiment queued,
          no manifest evidence_direction changed; this marker and that artifact
          are the only writes. HOMED HERE, not on a node of its own: no plan node
          owns the free-form showcase token, and this node is the correct home --
          same claim (MECH-309), same substrate (SD-054 reef/shelter), same
          phenomenon (monomodal collapse vs discriminative regime switching).
          (1) ATTRIBUTED: the chain is NOT an instrumentation artifact. The two
          competing explanations were both checked against code and manifests and
          both refuted as causes. Seed shortfall: REFUTED cleanly -- queue entries
          declare "seeds": 1, manifests report n_seeds=1.0/seeds=[0], drivers
          default to [0] BY DESIGN and say so in their docstrings; declared equals
          actual, unlike V3-EXQ-912/920 which the seed-enforcement defect really
          did hit. Recording gap: PRESENT (the obs_dict-vs-info benefit_exposure
          read is live at v3_exq_906b_...py:572, pinning benefit_exposure to 0.0
          on every step) but NON-CAUSAL -- z_goal, the only gap-affected channel
          in CORE_CHANNELS, was non-degenerate in all three (chan_max_std 0.0722/
          0.0750/0.0737, writer_defect false) because it varied through
          drive_level; residue_wanting (zeroed, 906c) is EXTRA_CHANNELS only; and
          V3-EXQ-916a proved the fix is purely instrumentation (bit-identical
          sim). (2) RE-POSED: the no-verdict is DEFINITIONAL, not empirical --
          claim_ids=[] plus experiment_purpose=diagnostic fixes
          evidence_direction=non_contributory before a step runs, and every
          load-bearing criterion is a liveness gate whose FAIL branch means
          "re-run the instrument", never "hypothesis H is false". The question
          underneath is a MECH-309 discrimination (contingent shelter/forage
          control vs monomodal collapse), re-operationalized onto two
          pre-registered contingency DVs on this substrate: C1 opportunity-
          triggered exit (P(exit reef | resource sensed) - P(exit | not sensed),
          both branches updating MECH-309) and C2 threat-triggered return,
          DISTANCE-STRATIFIED to kill the absolute-distance confound the
          906b/906c/911 autopsy flagged. The liveness gates move to preconditions
          (VOID, not PASS, if unmet), plus conditioning-event floors -- the C1
          floor is the one the current reef geometry fails. (3) REFUSED: a
          same-question letter re-queue (906d / 911a / any further showcase on
          this criteria set), in the re-derive brake's spirit. (4) ROUTED, NOT
          QUEUED: successor spec `reef_contingency_discrimination` for
          /queue-experiment -- claim_ids [MECH-309], seeds >= 8 (rate contrasts,
          not one trajectory), habitat-cue geometry per
          developmental_ecology_curiosity_foraging_correction_2026-08-10.md
          (probabilistic spawn-prior shift, NOT "resources must be reef-
          perceptible"), already covered by chip-20260810-fishtank-developmental-
          ecology -- do not spawn a second chip for it. EXQ id deliberately not
          minted here. Also surfaced for /governance, not acted on: this is a
          GOV-FANOUT-1 candidate (measurement / environment / mechanism axes),
          and a factual correction to failure_autopsy_V3-EXQ-916-916a-917-920-
          fishtank-cluster_2026-08-12 -- its "use_proxy_fields left at default
          False" is wrong for this sub-lineage (CausalGridWorldV2 setdefaults it
          True at causal_grid_world.py:5187+; the operative defect is the
          wrong-dict read alone). Conclusion unchanged; mechanism as written
          would misdirect a future reader.
      governance_2026_07_07: "V3-EXQ-714 (confirmed failure_autopsy_V3-EXQ-714_2026-07-07; governance-apply) RECONFIRMS this node's ceiling: the FULLSTACK selection+valuation composite aborted at C1 readiness (GAP-A consumed-summary divergence 0.004 + OFC devalued-range 0.0007 starved at FULL P0=200; C2 never scored), non_contributory for ARC-062/MECH-309. Re-derive brake FIRED (20th ARC-062 / 19th MECH-309); fullstack re-queue REFUSED; route /implement-substrate f_dominance_conversion_ceiling GAP-A-divergence-survival face. Status stays in-progress (no change) -- acknowledgement of the 2026-07-07 evidence only."
      reconcile_2026_07_09: "COMPETENCE-WALL REFRAME ABSORBED (closure-drift stale-since reconcile; plan-frontmatter only, NO claims.yaml/queue change). failure_autopsy_V3-EXQ-719a_2026-07-08 (confirmed, governance-applied REE_assembly master 07acd6ad29; reclassified ARC-062/MECH-309) reframes this node's ceiling: the conversion-ceiling dissociation diagnostic gave the FIRST direct competence measurement of the integrated all-ON agent (forages 0.065/0.0/0.455 resources/ep, below the 1.0 floor on 0/3 seeds; MI above the shuffle null 3/3 but marginal committed entropy moderate-to-high = diffuse state-blind commitment, NOT literal monomodal collapse). This reframes the whole 654h/485i/625e/460h/460i downstream-behavioural-retest wall -- and 714's C1 readiness abort -- as ONE root: a behavioural-COMPETENCE / training-regime ceiling (thin P1 = 90-ep bias-head-only REINFORCE on a frozen encoder; all-ON mechanism interference a live alternative), NOT another selection lever (MECH-448/449 built + selection-face lifted on GAP-A). GAP-B closes only on a C2 committed-class-entropy PASS, which now requires the all-ON agent to competently commit FIRST. Live path = the brake-EXEMPT V3-EXQ-724 competence-localization diagnostic (running), then /implement-substrate on the localized competence gap. Re-derive brake FIRED (21st ARC-062 / 20th MECH-309); a same-claim behavioural re-test (654-letter, 722, 719b) is REFUSED. Status stays in-progress; ARC-062/MECH-309 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- UNWEAKENED. Acknowledgement of the 2026-07-08 evidence only."
      last_updated: 2026-09-01
      governance_2026_08_01: "Closure-drift stale-since-review acknowledgement (governance cycle 2026-08-01, session-startup-checklist-28b0bd). Flagged because confirmed failure_autopsy_V3-EXQ-851_2026-08-01 reclassified ARC-062/MECH-309. V3-EXQ-851 (GOV-FANOUT-1 Leg P-A erratum-fix retest, modulatory_channel_route_source corrected 'gated_policy' -> 'lateral_pfc') FAILed non_contributory -- MECH-448/449 flip from robustly-live (654j) to completely dead under IDENTICAL seeds, a deterministic result whose causal path is not yet identified; user explicitly declined to accept the substrate_not_ready_requeue self-route at face value. Does NOT change GAP-B: no H1 verdict was possible from this run, so the MECH-439 F-dominance conversion ceiling this node already waits on is UNCHANGED. ARC-062/MECH-309 stay candidate/substrate_ceiling/v3_pending/pending_retest_after_substrate. Routed /queue-experiment for a cheap targeted diagnostic (lateral_pfc vs none, same seeds, tracking MECH-448/449 directly) before another ~7.7-hour full run. Status stays in-progress; last_updated bumped to acknowledge."
      governance_2026_06_23: "CROSS-PLAN EDGE RECONCILE (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). GAP-B's actual closure gate -- the MECH-439 F-dominance conversion ceiling -- is named ~12x in this node's owner/governance prose ('the selection-authority CONVERSION coupling (MECH-439 F-dominance live root)', '654i PASS would also close behavioral_diversity_isolation:GAP-I') but carried ZERO map edges to where that root is tracked. Added cross_plan_link to behavioral_diversity_isolation:GAP-I (the F-dominance root-tracking parent; 654i/654j were its downstream confirmers) and conversion_ceiling_campaign:FULLSTACK (the co-armed full-stack arm that is the corrected route after the 18th/19th re-derive brake refused further GAP-B eligibility letters). behavioral_diversity_isolation + conversion_ceiling_campaign added to sibling_plans. No status/owner change -- GAP-B stays in-progress (closes on a C2 PASS, which the FULLSTACK arm now owns)."
      governance_2026_06_21_654i_repoint: "OWNER REPOINTED 654h -> 654i (plan-doc drift reconcile, session plandoc-arc062-gapb-654i-repoint-20260621T1849Z; NO claim-scoring move). V3-EXQ-654h -- the GAP-B committed-class-entropy falsifier on the MECH-448 demotion-enabled selector -- RAN FAIL/non_contributory 2026-06-21T17:57Z (ree-cloud-3) and was autopsied (failure_autopsy_V3-EXQ-654h_2026-06-21, status=confirmed). Five of six self-route gates passed but the MECH-448 non-degeneracy gate FAILED (f_eligibility_excluded_count==0): the 689d-validated absolute envelope floor (0.30) admitted every candidate on the arc_062 bank's SPREAD/non-divergent F pool -> all-admit fallback -> ARM_ON==ARM_OFF structural no-op, so the demotion lever never engaged and the C2 DV never ran through a demoted selector. Identical signature to V3-EXQ-485i (same lever, OFC bank); NOT a MECH-309/ARC-062 weakens. The re-queue gate cleared (failure_autopsy_V3-EXQ-485j: MECH-448 demotion generalises off GAP-A for 654's discrimination/committed-diversity family). V3-EXQ-654i (queued ree-v3 main; supersedes 654h) is now the live owner -- it adds 485j-style per-(arm,seed) envelope-floor calibration so the demotion lever genuinely excludes (excluded_count>0) on the spread arc_062 F pool, and scores a fired-but-non-converting outcome as a genuine weakens (not another silent no-op requeue). owner_exq lead repointed 654h -> 654i; 654h folded into [HISTORY] (654g->654h->654i lineage preserved). Status STAYS in-progress -- a queued successor does not close the gap (GAP-B closes only on a 654i PASS C2 committed-class entropy lift). PROMOTES NOTHING -- MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate; MECH-439 unchanged. last_updated stays 2026-06-21."
      governance_2026_06_20_690_ack: "ACK (no status change). failure_autopsy_V3-EXQ-690_2026-06-20 (confirmed; ARC-062 diversity-floor sweep) is the 4th channel to corroborate the MECH-439 F-dominance conversion ceiling that GAP-B already waits on -- a FOURTH inert lever (MECH-313 noise-floor selection-softmax temperature) after the CRF / OFC / dACC channels. 690's signature is BETWEEN-ARM lever-inertness (byte-identical per-seed metrics across a 0.30->2.75 temperature sweep): a selection-softmax temperature floor is architecturally incapable of moving the deterministic committed argmin over F-dominated scores (lever-target mismatch). ARC-062 stays candidate/substrate_ceiling/v3_pending/pending_retest_after_substrate, UNCHANGED; GAP-B status/owner/resume UNCHANGED (still gated on the 689a F-rebalance keystone, NOT on any 654-specific or temperature lever). Bumped last_updated to acknowledge the autopsy."
      phase0_synthesis_2026_06_18: "CROSS-REF (no status change; CORROBORATES the governance_2026_06_18_autopsy below). The conversion-ceiling Phase 0 disambiguation (evidence/planning/conversion_ceiling_phase0_synthesis_2026-06-18.md, run wf_c03ff4f4-d45) independently reached the same verdict as the 654f autopsy via a separate 5-cluster analysis: cluster D (CRF gate-lockout) is CLOSED and was causally INDEPENDENT of representation-geometry (654d armed the GAP-A de-collapse yet n_matched rose to 7-8; 654f fixed it at the CRF locus alone), and the residual flat committed-class entropy is the SHARED selection F-dominance root now formally characterized as MECH-439 (primary score = 88-89% of E3 variance, unchanged by the diversity stack -- V3-EXQ-571). Phase 0 adds the cross-cluster framing: the SAME F-dominance bottleneck swallows the modulatory (GAP-A cluster B), within-class (MECH-341 cluster E), AND CRF rule-bias (this node, cluster D-post-fix) channels -- three nominally-separate diversity mechanisms converge on one selector. The 654g route (wire the 569i top-k k=3 shortlist) is the validated PARTIAL circumvention; the open risk (MECH-439) is that its thin 2/3-seed margin may not survive the composite, in which case the target is rebalancing F's variance share directly. Recorded for discoverability; MECH-309/ARC-062 unchanged."
      governance_2026_06_18: "FALSIFIER RE-RAN (recovery re-queue; NO claim-scoring move). V3-EXQ-654f -- the verbatim recovery re-queue of the silently-stalled/phantom-completed 654e (654e crashed-before-manifest on a transient cross-checkout kwarg skew, now resolved; science unchanged) -- RAN FAIL/non_contributory 2026-06-18T00:52Z on ree-cloud-1 and was reviewed this cycle (self-route, weights nothing). The CRF-gate calibration amend (crf-availability-maintenance, ree-v3 main 42895f6) did NOT yield a contributory committed-class-entropy verdict; the manifest's interpretation block is empty (label None) so the precise blocker letter (frac_active gate vs the shared conversion/monostrategy ceiling) is not self-reported -- consistent with the lineage's standing CRF gate-lockout / monostrategy ceiling. owner_exq frontier advances 654e -> 654f (clears the lineage-advanced drift flag). A 654g successor on a de-locked substrate is owed. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. Status stays in-progress. last_updated 2026-06-17 -> 2026-06-18."
      governance_2026_06_18_autopsy: "AUTOPSY (confirmed failure_autopsy_V3-EXQ-654f_2026-06-18; /failure-autopsy session, NO claim-scoring move) -- CORRECTS the governance_2026_06_18 'interpretation block empty / blocker letter not self-reported' reading. The manifest DID self-route and DID fully populate result.interpretation (label shared_selection_authority_conversion_ceiling_route_implement_substrate); the 'empty' read is a TOP-LEVEL artifact -- the script (and the whole 654 lineage) writes interpretation/interpretation_label only nested under result, while the indexer + governance read manifest.get('interpretation') at the top level (build_experiment_indexes.py:782). NOT a self-route-before-populate, NOT a 654f regression. THE DISAMBIGUATED FINDING (reading (a)): the CRF-gate calibration amend WORKED -- C1 fully met on all five preconditions: crf_frac_active 0.869/0.968/0.828 (vs 654d 0.0) cleared the 0.30 floor, the conflict-gate lockout is GONE (crf_mean_n_matched 2.18-3.81 admitted, vs 654d's 7-8 all gated out), differentiated pool max_pairwise_dist 1.711, propagation NON-VACUOUS (ARM_ON bias != ARM_OFF, 0.0203-0.0517 > floor; the 654 seed-42 byte-identical washout did NOT recur). C2 committed-class entropy lift FALSE (0/3 seeds; ARM_ON 1.0411 ~ ARM_OFF 1.0416; committed_class_counts near byte-identical; ARM_ON lateral_pfc_bias LOWER than ARM_OFF -- bias reaches+changes the accumulator but does not move the F-dominated committed argmax). This is the FAIL_C1_holds_C2_fails branch = the SHARED selection-authority CONVERSION ceiling that behavioral_diversity_isolation:GAP-A owns (569g/569h/682), NOT a MECH-309/ARC-062 falsification. KEY: 654f armed the SUPERSEDED additive conversion lever ARM_STD_G2 (modulatory_authority_normalize_basis=std + authority_gain=2.0 + route-range), which GAP-A proved insufficient (V3-EXQ-569h FAIL, 1/3 seeds); the TOP-K shortlist conversion that GAP-A validated -- V3-EXQ-569i PASS/supports 2026-06-17, 'diversity reaches committed action', ARC-065 promoted stable -- was NOT armed (654e was queued 2026-06-17 before 569i landed). So GAP-B's residual blocker is no longer an unbuilt substrate: the fix EXISTS and is VALIDATED; only the 654g experiment wiring it is owed. ROUTE (user-confirmed at the interactive gate): /queue-experiment 654g porting the GAP-B committed-class-entropy falsifier onto the 569i-validated TOP-K shortlist conversion (use_modulatory_shortlist_then_modulate + modulatory_shortlist_mode=top_k + modulatory_shortlist_k), keeping the now-working CRF stack constant; NOT a further CRF amend (CRF done), NOT ARM_STD_G2 (superseded). Retain the C1c readiness precondition + conversion-ceiling off-ramp (NO weakens branch). ALSO: chip spawned for the manifest top-level interpretation-mirror emit fix (mirror interpretation/interpretation_label at the manifest top level; routes via /queue-experiment). RECURRENCE: 6th autopsy on the 654 target; user re-confirmed 2026-06-16 substrate-maturation NOT granularity-debt -- a single localized signature, now resolved at the CRF locus -> NO /claim-synthesis. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. NO claims.yaml/scoring/substrate_queue edits this pass (substrate_queue entry recommended action=none: top-k shortlist + crf-availability-maintenance both already landed/validated). Status stays in-progress."
      governance_2026_06_17: "CRF-GATE AMEND LANDED + 654e QUEUED (/implement-substrate + /queue-experiment session; NO claim-scoring move). Executed the user-confirmed 654d-autopsy route. VERIFY-FIRST (the load-bearing check): 569i's top-k GAP-A substrate DOES de-collapse the consumed_summary spread (0.073/0.089/0.084 > 0.05 floor, 3/3) -- but failure_autopsy_V3-EXQ-654d_2026-06-16 already proved that is the WRONG lever: 654d armed an equivalent GAP-A de-collapse and crf_frac_active stayed EXACTLY 0.0 on all 3 ARM_ON seeds, even where consumed_summary cleared the floor, because the real GAP-B blocker is the CRF conflict-gate lockout (crf_mean_n_matched 7.08/7.29/8.70 -> theta(7)=0.15+0.25*6=1.65 >> maintenance_floor 0.45 -> every matched rule gated out), INDEPENDENT of GAP-A (consumed_summary=cross-candidate E3 channel; n_matched=cross-rule CRF context-match; different vectors/loci). So NOT a blind 654e re-queue on the 569i substrate (would re-derive frac_active=0.0). /implement-substrate AMEND crf-availability-maintenance at the CRF locus, ungated from GAP-A: 3 no-op-default levers under mature_pool_dynamics (bit-identical OFF) -- mature_context_match_threshold (FAULT 1: sharpen the gate match cutoff so fewer of the clustered context_tags co-match, n_matched 7-8 -> ~2-3), tolerance_conflict_cap (FAULT 2a: cap n_competing so theta < 1.0), maintenance_couple_to_theta (FAULT 2b: floor maintained availability to max(maintenance_floor, theta(n_matched)+eps) so the maintained differentiated pool clears the gate). Landed ree-v3 main 42895f6; ree_core/policy/candidate_rule_field.py + config.py + agent.py; 24/24 CRF contracts (C20-C24 incl the 654d inversion: crowded maintained pool frac_active 0.000 legacy -> 0.98 armed, n_matched 8->3, theta 1.90->0.65) + 7/7 preflight + full suite 1064 pass (1 pre-existing control_vector C4 flake, unrelated). claims.yaml UNTOUCHED (substrate-only). THEN /queue-experiment V3-EXQ-654e (ree-v3 main 488ec03; supersedes 654d) = the 654d GAP-B falsifier ported onto the amend, ARM_ON arms 0.7/3/True, C1c crf_frac_active>=0.30 self-routing precondition retained + conversion-ceiling off-ramp + 3-branch NO-weakens routing; validate_experiments --strict OK, dry-run smoke PASS. substrate_queue crf-availability-maintenance: status string corrected (the stale 654c 'gate 654d behind GAP-A de-collapse' reading -> 654d finding + amend landed), depends_on_unresolved corrected (654e validation, NOT GAP-A), 654d failure_record + amend_log added; ready STAYS False until 654e validates the frac_active gate-firing. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened (654d was non_contributory). Status stays in-progress. The previous /governance note follows for the queue-time record."
      governance_2026_06_16: "GATE CLEARED + 654d QUEUED (Step-9.5 drift follow-on from the /queue-experiment session; NO claim-scoring move). The 654c-autopsy gate -- 'GATED ON GAP-A context DE-COLLAPSE, THEN the CRF activation amend, THEN re-queue as 654d' -- has had its load-bearing leg discharged: V3-EXQ-684a PASSED 2026-06-15 (conversion_mechanism_identified; confirmed coordinator DB + manifest non-vacuous), so the GAP-A monostrategy collapse that drove the 654c frac_active=0.0 gate-lockout is now de-collapsible via the modulatory-bias-selection-authority CONVERSION amend's ARM_STD_G2 config (std basis + authority_gain=2.0 + routed e2_world_forward channel; committed entropy 0.989 > legacy 0.775 on 3/3 seeds). ON that PASS, V3-EXQ-654d was QUEUED 2026-06-16 via /queue-experiment (ree-v3 origin/main 927fe1c) -- the GAP-B committed-class-entropy falsifier ported onto the de-collapsed substrate, arming ARM_STD_G2 as a matched-stack constant on BOTH arms (only use_candidate_rule_field swept). DESIGN NOTE on the autopsy's part-(ii) caveat: the residual CRF maintenance-theta coupling amend is NOT implemented in code (substrate_queue crf-availability-maintenance ready=False, amend owed) -- 654d deliberately tests the autopsy's PRIMARY hypothesis, that GAP-A context de-collapse alone drops n_matched enough for the EXISTING maintenance_floor 0.45 to clear the gate (autopsy mechanism: collapsed context -> >=3 co-matches -> theta>=0.65; de-collapse -> n_matched 1-2 -> theta<=0.40 < floor). The C1c precondition (crf_frac_active>=0.30, self-routing substrate_not_ready_requeue) is the GUARD: if de-collapse alone is insufficient, the run self-routes to the part-(ii) amend, NOT a falsification; 654d records crf_n_matched_last to disambiguate matched-but-gated-out (route to part ii) from never-matched. Three-branch map unchanged from the 654c framing (PASS->supports MECH-309/ARC-062; C1-holds/C2-fails->shared CONVERSION ceiling persisting under the validated lever->non_contributory+/implement-substrate, NOT a falsification; C1-fails->non_contributory/substrate_not_ready_requeue); NO weakens branch while the conversion ceiling is open. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened (awaiting the 654d run + review). NO claims.yaml/scoring/substrate_queue edits this pass. Status stays in-progress. The previous /governance note follows for the queue-time record."
      governance_2026_06_16_pm: "FALSIFIER RAN + AUTOPSIED (confirmed failure_autopsy_V3-EXQ-654d_2026-06-16; /failure-autopsy session, NO claim-scoring move). V3-EXQ-654d RAN FAIL/non_contributory 2026-06-16T15:27Z (ree-cloud-2), self-route substrate_not_ready_requeue -- the C1-fail branch the design pre-registered. C1c crf_frac_active=0.0 again (all 3 ARM_ON seeds). THE LOAD-BEARING DISAMBIGUATION: 654d (a) ARMED the GAP-A de-collapse lever ARM_STD_G2 (the 684a-validated config) on both arms and (b) finally RECORDED the discriminator crf_mean_n_matched (7.08/7.29/8.70) -- the instrument the 654c autopsy flagged as missing. The result REFUTES the 654c gating hypothesis ('GAP-A context de-collapse alone drops n_matched enough for the existing maintenance_floor 0.45 to clear the gate'): the GAP-A conversion de-collapse is the WRONG LEVER for THIS gate. ARM_STD_G2 de-collapsed the E3 SELECTION channel (consumed_summary pairwise spread cleared the 0.05 floor on 2/3 seeds) but does NOT touch the CRF rule-match context KEY -- a distinct vector/use. The 16 differentiated minted rules (crf_max_pairwise_rule_dist 1.711) match 7-8 per tick (HIGHER than 654c's >=3) and EVERY one is gated out: gate_and_select theta = 0.15 + 0.25*(n_matched-1) ~= 1.65 >> maintenance_floor 0.45. mean_prop_counterfactual_delta=0.0 (zeroing rule_state changes nothing) directly confirms the gated-out rule_state never reaches committed action. So 'matched-but-gated-out' is now MEASURED, not inferred; and the two CRF-locus faults the 654c autopsy named (context-key crowding + maintenance/conflict-gate calibration) are confirmed STILL UN-AMENDED (candidate_rule_field.py maintenance_floor 0.45 / theta calc bit-identical to 654c) and INDEPENDENT of the GAP-A selection conversion. ROUTE (user-confirmed at the interactive gate 2026-06-16): /implement-substrate AMEND crf-availability-maintenance AT THE CRF LOCUS, UNGATED FROM GAP-A -- (1) fault-2: couple maintained availability to the per-tick theta(n_matched) (maintain at max(maintenance_floor, theta(n_matched)+eps)) and/or cap n_competing and/or sharpen context_match_threshold (a PURE CRF gate calibration, the now-confirmed sole independent blocker); (2) fault-1: de-collapse the CRF mint/match context KEY so the minted rules' context_tags are separable (NOT the ARM_STD_G2/E3 lever -- 654d proved that does not reach the CRF match context); (3) keep the crf_frac_active>=0.30 readiness gate. Re-queue the GAP-B falsifier (654e) on THAT frac_active gate, NOT on GAP-A. RECURRENCE: 5th autopsy on this target (654->654a->654b->654c->654d); user RE-CONFIRMED 2026-06-16 the substrate-maturation read (NOT claim-granularity debt / NO /claim-synthesis) -- claims never tested (C1 gated every run), single localized failure signature, blocker now isolated + measured. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. NO claims.yaml/scoring/substrate_queue edits this pass (the substrate_queue crf-availability-maintenance amend + 654d failure_record is governance's to apply; entry is already ready=False). Status stays in-progress. The previous /governance note follows for the queue-time record."
      governance_2026_06_15_pm: "FALSIFIER RAN + ADJUDICATED (confirmed failure_autopsy_V3-EXQ-654c_2026-06-15; applied this /governance cycle). V3-EXQ-654c FAILed C1c readiness (crf_frac_active=0.0 < 0.30) for the 4th iteration -- but the autopsy established this is an INVERTED signature, NOT the prior churn: the 666c maintenance amend WORKED (crf_max_pairwise_rule_dist 0.0 -> 1.711, minting stabilised 12-16, pool now holds >=2 differentiated rules), yet every matched rule is gated OUT (frac_active 0.0) because the GAP-A-collapsed e2_world_forward context (consumed_summary spread 0.0089 < 0.05) makes >=3 rules co-match -> gate_and_select theta=0.15+0.25*(n_matched-1) >= 0.65 > maintenance_floor 0.45. MAINTAINED != ACTIVE -- the bottleneck moved one stage downstream (mint/maintain SOLVED by 666c; the residual is activation under a collapsed context, which is the SHARED behavioral_diversity_isolation:GAP-A monostrategy collapse). APPLIED /governance 2026-06-15: 654c evidence_direction non_contributory (per-claim MECH-309=non_contributory, ARC-062=non_contributory) + EQN; MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened; substrate_queue crf-availability-maintenance AMENDED with the 654c failure_record (de-collapse CRF context key + couple maintenance to per-tick theta + frac_ACTIVE readiness gate) and ready flipped True->False (gate-firing not yet demonstrated); 654c marked reviewed. NO 654d yet -- the CRF amend is necessary-but-not-sufficient while the GAP-A context collapse persists, so 654d is gated on GAP-A context de-collapse (569g/682 -> the in-flight modulatory-bias gain/contrast conversion amend). Status stays in-progress. NOTE: this CONFIRMS the conversion-ceiling off-ramp the morning's governance_2026_06_15 pre-registered -- C1-side maintenance cleared, the residual is the shared selection/activation-authority ceiling, same root as GAP-A 569g/682. The previous morning note follows for the queue-time record."
      governance_2026_06_15: "RESUME-CONDITION SATISFIED + FALSIFIER QUEUED (Step-9.5 drift follow-on; NO claim-scoring move). The 2026-06-14 CORRECTED RESUME PATH is now discharged on both legs: (1) V3-EXQ-666c PASSED 2026-06-15 -- the clean fraction-gated CRF-readiness re-run at the enlarged P0 (200 ep) cleared the maintained-pool gate AND all 4 non-vacuity preconditions SIMULTANEOUSLY: ARM_2 (mature+e2ctx+maintenance) mean_frac_maintained 0.854 > 0.625 floor; field mints >=2 rules/cell; e2ctx full-pool differentiation 1.598 > 0.1 captured PRE-gap on all 3 seeds; ARM_2 maintained pool count 9 + differentiation 1.701 supra-floor. substrate_queue crf-availability-maintenance flipped ready=TRUE (REE_assembly origin/master be7261d9ca, 2026-06-15; 666c is claim-free and weights nothing). (2) ON that PASS, V3-EXQ-654c was QUEUED 2026-06-15 via /queue-experiment (ree-v3 origin/main 7225065; coordinator /queue/active present) -- the GAP-B behavioural falsifier ported onto the validated substrate (666c ARM_2 levers armed on ARM_ON, enlarged P0, trained-bias-head P1). DESIGN NOTE (claim_ids re-evaluated from scratch + the standing conversion ceiling): the 654b 'weakens' branch is REPLACED by a pre-registered SHARED CONVERSION-CEILING off-ramp -- if 654c's matured+maintained+differentiated pool clears C1c AND its bias reaches committed action (C1d) but STILL does not lift committed-class entropy, that is the same shared selection-authority CONVERSION ceiling (behavioral_diversity_isolation:GAP-A; failure_autopsy_V3-EXQ-569g_2026-06-14 + V3-EXQ-682: range reaches the E3 accumulator but does not move the F-dominated committed argmax), self-routes non_contributory + /implement-substrate, NOT a MECH-309/ARC-062 falsification. So ONLY the PASS branch (C2 committed-class entropy lift >=2/3 seeds) weights the claims (as supports); both FAIL branches are non_contributory; there is NO weakens branch while the conversion ceiling is open. NOTE: a parallel session (behavioral_diversity_isolation:GAP-A 682-gated conversion amend) is concurrently /implement-substrate-ing that exact gain/contrast amend -- if 654c hits the conversion-ceiling off-ramp the remedy is already in flight. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened (awaiting the 654c run + review). Status stays in-progress."
      governance_2026_06_14: "CLOSURE-DRIFT RECONCILE (stale resume_condition; NO claim-scoring move -- the 666-series are claim-free substrate-readiness diagnostics that weight nothing). The resume_condition + the closure_status snapshot still said 'GATED ON V3-EXQ-666 PASS, then queue 654c'; that is STALE. V3-EXQ-666 has now run THREE times, all FAIL / non_contributory: (666, 2026-06-11T06:38Z) mature_dynamics_insufficient -- differentiation (e2ctx dist 1.71) and persistence (crf_frac_active) in tension; confirmed failure_autopsy_V3-EXQ-666_2026-06-11; routed -> built the crf-availability-maintenance mechanism (ARC-063 amend, ree-v3). (666a, 2026-06-11T15:40Z) the maintenance mechanism WORKS and strictly dominates -- crf_frac_maintained ARM_2 1.0/0.625/0.938 vs ARM_1 0.188/0.125/0.438 vs ARM_0 0.0, clean monotone 3/3-seed separation -- BUT the pre-registered gate used a COUNT floor (crf_n_maintained_reactivatable>=2) that differentiation-alone (ARM_1) also clears; verdict = measurement/test-design defect, NOT substrate failure (confirmed failure_autopsy_V3-EXQ-666a_2026-06-11 §7 routed -> 666b re-gated on the FRACTION statistic). (666b, 2026-06-12T00:52Z) the fraction-gate logic DISCRIMINATED correctly this time (frac_maintained_gate_discriminates_vs_arm1=true; ARM_2 0.8125 mean cleared, ARM_1 below ceiling -- both load-bearing criteria PASSED) BUT a non-vacuity precondition FAILED: e2ctx_full_pool_differentiated_supra_floor returned 0.0 (the precondition takes min crf_max_pairwise_rule_dist over the ARM_1+ARM_2 e2ctx arms measured POST the 2000-tick context-absent silence gap; ARM_1 no-maintenance erodes to an empty pool under that gap BY DESIGN, so its end-state dist=0.0 starves the precondition even though ARM_2 held 1.71) -> self-route substrate_not_ready_requeue, which routes to RE-QUEUE (not /failure-autopsy; no 666b autopsy exists or is owed -- substrate_not_ready_requeue routes to re-queue). 666b was reviewed + logged as a carried pending item in WORKSPACE_STATE; no 666c is queued anywhere yet (the queue holds only V3-EXQ-672b + V3-EXQ-680/680a). NET STATE: the crf-availability-maintenance mechanism is CONFIRMED FUNCTIONAL (666a clean monotone frac_maintained separation), but no single run has cleared the fraction gate AND all its non-vacuity preconditions SIMULTANEOUSLY. CORRECTED RESUME PATH: queue a clean fraction-gated CRF-readiness re-run V3-EXQ-666c at an adequate P0 maturation window so the e2_world_forward context differentiates the full pool supra-floor (crf_max_pairwise_rule_dist > 0.1 on the e2ctx arms) on all 3 seeds -- capturing full-pool differentiation PRE-gap so the e2ctx-differentiation precondition reflects whether the context CAN differentiate rather than ARM_1's expected post-gap erosion; ONLY on that PASS /queue-experiment the 654c GAP-B BEHAVIOURAL falsifier (committed-class entropy DV). substrate_queue crf-availability-maintenance ready stays FALSE (the 666b failure_record is already absorbed; implementation_hint/next_step refreshed to 666c this cycle). MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. Status stays in-progress."
      governance_2026_06_11: "SUBSTRATE-ENRICHMENT ROUTED STEP LANDED (stale-since-review reconcile: failure_autopsy_V3-EXQ-654b_2026-06-11 confirmed, post-dates the 2026-06-10 last_updated). The 654/654a/654b churn (crf_frac_active pinned ~0.13, crf_max_pairwise_rule_dist=0.0, pool never holds >=2 rules even at 240ep) is now diagnosed + the fix BUILT. /implement-substrate ARC-063 CandidateRuleField mature-pool amend LANDED 2026-06-11T04:42Z (ree-v3 main 7e2e0ef; REE_assembly master 2a545cfde0 design doc) -- two opt-in flags, default-OFF/bit-identical: (1) crf_mature_pool_dynamics recalibrates the conflict-gate so theta<1 for >=2 matched rules (mature_tolerance_floor 0.15 / conflict_gain 0.25 -> theta(2)=0.65 admits a 2nd co-firing rule, the latent deadlock fix) + mature_availability_decay 0.001 / mature_retire_floor 0.05 / asymmetric negative credit 0.02 / mint-youth protection 30 ticks / decoupled mint_block 0.8; (2) crf_context_from_e2_world_forward sources the CRF context from e2.world_forward (mirrors ARC-065 GAP-A). get_state emits crf_frac_active for the readiness gate. Activation smoke: legacy n_present=1/dist=0.0/READY=False (the 654b signature) -> mature n_present=2/dist=1.49/READY=True. STEP-8 readiness diagnostic queued: V3-EXQ-666 (claim-free; 3 arms ARM_0_OFF/ARM_1_MATURE/ARM_2_MATURE_E2CTX x 3 seeds on the matched 654b stack; CRF-readiness gate crf_frac_active>=0.30 AND dist>floor on ARM_1/ARM_2 >=2/3 vs the ARM_0 churn signature; dry-run confirmed discrimination ARM_0 frac 0.126/dist 0.0 vs ARM_1 frac 0.69 / ARM_2 dist 0.497). MECH-309/ARC-062 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- substrate-only amend, NO claims.yaml/scoring edits. Status stays in-progress. NEXT: V3-EXQ-666 readiness PASS gates the 654c GAP-B BEHAVIOURAL re-run (a SEPARATE /queue-experiment session, committed-class entropy DV)."
      governance_2026_06_10: "FALSIFIER RE-RAN (longer maturation) + ADJUDICATED. V3-EXQ-654b (supersedes 654a; P0+P1 maturation window widened 100->240 ep to clear the C1c floor) FAILed non_contributory, self-route substrate_not_ready_requeue -- the C1-fail branch (c) the resume_condition pre-registered. C1c arm_on_rule_field_differentiated_and_matured still UNMET: crf_frac_active=0.130 < 0.30 floor even at 240ep; C1d_within_arm_on_rule_state_counterfactual_nonzero=False; the other preconditions met (class axis exercisable 1.0, GAP-A consumed-summary divergence 0.0091>=0.005, propagation non-vacuity |bias_ON-bias_OFF|=0.0122>0.001 -- the 654 seed-42 byte-identical washout did NOT recur). So the longer window fixed the propagation washout but the CandidateRuleField pool still does not mature to a live >=0.30 active fraction. C2 committed-class lift moot (C1 gates it). APPLIED /governance 2026-06-10: 654b evidence_direction non_contributory; MECH-309/ARC-062 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened; 654a marked superseded (evidence_direction=superseded, scoring-excluded); substrate_queue modulatory-bias-selection-authority entry amended with the 654b failure_record (longer-window confirmation); 654b marked reviewed. No new autopsy required -- covered by confirmed failure_autopsy_569f-661-654a_2026-06-10 (amend modulatory-bias-selection-authority, routing implement-substrate). Status stays in-progress: the rule-apprehension substrate is still not matured; next step is substrate enrichment (pool maturation / conflict-gate relaxation), not a further re-queue at the existing maturation budget."
      governance_2026_06_09_amend_and_requeue: "BOTH ROUTED STEPS DONE. (1) PRIMARY /implement-substrate amend LANDED: ree-v3 main 9797e84 added the no-op-default crf_persist_rules_across_episode_reset flag so CandidateRuleField.reset() preserves _rules/_recurrence/_step across the per-episode agent.reset() wipe (impl target ARC-063; bit-identical OFF; 11/11 CRF contracts + 7/7 preflight). (2) SECONDARY /queue-experiment LANDED: V3-EXQ-654a queued (this session; ree-v3 experiment_queue.json + experiments/v3_exq_654a_arc062_gapb_rule_apprehension_behavioural_falsifier.py; priority 250, machine any; supersedes V3-EXQ-654; claim_ids=[MECH-309, ARC-062], experiment_purpose=evidence). 654a = the same single-variable ARM_OFF/ARM_ON falsifier with: crf_persist_rules_across_episode_reset=True (the matured pool clears the C1c crf_frac_active>=0.30 floor 654 cold-started at 0.12); a 3-phase P0(e2 warmup + field matures)/P1(frozen-encoder bias-head REINFORCE, GAP-D agent.lateral_pfc.bias_head_parameters())/P2(frozen measurement) structure; and a C1d propagation non-vacuity precondition (paired |bias_ON - bias_OFF| > 1e-3, the seed-42 byte-identical washout guard) plus a within-ARM_ON rule_state counterfactual diagnostic. PRIMARY DV stays committed-class entropy; within-class-representative entropy the secondary negative control. validate_experiments --strict + validate_queue + dry-run smoke all PASS (dry scale correctly self-routes substrate_not_ready_requeue). MECH-309/ARC-062 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened; no claims.yaml/scoring edits (awaiting the run). Status stays in-progress until 654a runs + is reviewed."
      governance_2026_06_09_pm: "FALSIFIER RAN + ADJUDICATED. V3-EXQ-654 FAILed non_contributory (self-route substrate_not_ready_requeue) -- the C1-fail branch the resume_condition pre-registered. Confirmed failure_autopsy_V3-EXQ-654_2026-06-09 (status=confirmed) applied this /governance cycle: the C2 committed-class falsifier DV never ran; the run failed the C1c readiness precondition arm_on_rule_field_differentiated (crf_frac_active 0.116/0.123/0.115 < 0.30 floor; crf_max_pairwise_rule_dist 0.0 all seeds; seed-42 ARM_ON committed-class byte-identical to ARM_OFF). Code-grounded 3-part cause: (a) agent.reset()->candidate_rule_field.reset() (agent.py:1908) wipes the rule pool every ~26-tick episode so the field never matures a live differentiated pool (cumulative n_minted 131-408 but cold-started each episode); (b) conflict gate forbids >=2-rule co-activation; (c) untrained bias head washes out the live rule_state (propagation washout). PFC/BG rule learning accumulates across experiences and is NOT reset per trial (Collins & Frank 2014; Mansouri) -> per-episode wipe is a translation failure, not a falsification; V3-EXQ-639 PASS proves the field CAN differentiate when its pool matures. APPLIED: 654 evidence_direction non_contributory (flat+runpack eq-note + source_autopsy); MECH-309/ARC-062 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate (already set) -- NOT weakened; substrate_queue ARC-062 entry amended with the 654 failure_record (n 9->10, priority 1, ready stays false); 654 marked reviewed. ROUTING: PRIMARY /implement-substrate amend = no-op-default cross-episode rule-persistence flag on candidate_rule_field.py reset() (impl target ARC-063); SECONDARY /queue-experiment 654a (gated on the amend) = trained-bias-head P1 arm + bias-non-vacuity precondition, committed-class entropy PRIMARY DV. Status stays in-progress (substrate amend -> 654a pending)."
      governance_2026_06_09: "FALSIFIER QUEUED as V3-EXQ-654 (IGW-20260609-004; ree-v3 32c5db7 on origin/main; priority 250, machine any; coordinator DB ingest confirmed). Single-variable: ARM_OFF use_candidate_rule_field=False (legacy collapsed delta/world EMA rule_state) vs ARM_ON use_candidate_rule_field=True (differentiated crf_source) -- both arms run lateral_pfc_analog (bias head un-zeroed, lateral_pfc_train_rule_bias_head=True) + gated_policy on the matched 649 GAP-A (candidate_summary_source=e2_world_forward, e2 trained online in P0) / 643a authority / SD-056 / SP-CEM / MECH-341 stack; only use_candidate_rule_field (+ auto use_candidate_rule_source) is swept. DV CORRECTION (user-confirmed 2026-06-09 via AskUserQuestion, overriding the governance_2026_06_07/08 'within-class-representative readout' prescription): code trace established the rule bias is CLASS-KEYED -- agent._candidate_world_summaries is first-action-keyed (e2.world_forward(z0, a_first)) and lateral_pfc.compute_bias broadcasts ONE rule_state across all K candidates, so within a first-action class every candidate gets an identical bias. The rule-creator therefore moves WHICH CLASS is committed (committed-class diversity), NOT within-class representative selection. The 614e Learning #2 ('use within-class-representative, not committed-class') was specific to the MECH-341 within-class TEMPERATURE lever (a within-class sampler); it does not transfer to the class-keyed rule bias. PRIMARY DV is therefore COMMITTED-CLASS entropy (paired ARM_ON>ARM_OFF lift), which the GAP-A fix makes non-vacuous; within-class-representative entropy is retained as a SECONDARY NEGATIVE CONTROL (expected ~null, confirming the class-keyed bias). experiment_purpose=evidence, claim_ids=[MECH-309, ARC-062]; C1 readiness (committed-class axis exercisable + GAP-A consumed-summary divergence real both arms + ARM_ON minted >=2 distinct rules firing a non-zero rule_state) self-routes substrate_not_ready_requeue on fail (NOT a weakens). No claims.yaml/scoring edits (awaiting the run)."
      governance_2026_06_08: "Plan-drift reconcile: the 2026-06-07 live blocker is now cleared. CandidateRuleField readiness landed via V3-EXQ-639 PASS; ARC-065 GAP-A shared candidate-summary readiness landed via V3-EXQ-649 PASS (consumed-summary spread 0.090 >= 0.05); the authority path is settled by V3-EXQ-643a PASS plus V3-EXQ-643b corrected-C2 PASS/non_contributory diagnostic; and downstream V3-EXQ-604c PASS proves the GAP-A-ready stack can express nonzero cross-candidate curiosity range. Status moves blocked_pending_substrate -> open. Next action is /queue-experiment for the GAP-B behavioural falsifier: ARM_OFF use_candidate_rule_field=False vs ARM_ON field+lateral_pfc+gated_policy on the matched GAP-A / authority / SD-056 stack, using the within-class-representative-diversity readout rather than committed-class entropy. No claims.yaml scoring move from the readiness diagnostics."
      governance_2026_06_07: "RULE-CREATOR SUBSTRATE IMPLEMENTED + READINESS-VALIDATED -- corrects the governance_2026_06_04 note below ('design is not implementation'), which was written hours BEFORE the implementation landed the same day and was never updated. ARC-063 v1 CandidateRuleField (ree_core/policy/candidate_rule_field.py) is committed 2026-06-04 (ree-v3 main 175a24f, on origin/main), fully wired (config crf_* knobs; agent.py ticks the field in select_action under a use_lateral_pfc_analog precondition; lateral_pfc_analog use_candidate_rule_source + crf_source REPLACES the legacy delta/world EMA source -- the literal 598b fix), contracts 8/8 (test_candidate_rule_field.py, re-verified PASS 2026-06-07), and READINESS-VALIDATED: V3-EXQ-639 PASS (ree-cloud-3, 20260604T154034Z, diagnostic claim_ids=[]) -- C1 differentiated rule_state norm_diff_across_contexts=0.806, C2 2 distinct mints (max pairwise 1.49), C3 conflict-sensitive gate, C4 bit-identical OFF. claims.yaml ARC-063 implementation_note already records this (the 2026-06-04 session updated claims.yaml + ree-v3/CLAUDE.md but missed THIS plan-node note). So the rule-creator/discriminator substrate this node was blocked_pending_substrate ON is DONE; the 598b C3 trainable_not_monomodal absence is structurally resolved (rule_state differentiated by construction). The 2026-06-07 'ARC-063 rule-creator chip' (filed at IGW-046 close) is REDUNDANT -- filed reading the stale 2026-06-04 note; no implementation work remains. STATUS STAYS blocked_pending_substrate because the BEHAVIOURAL GAP-B falsifier (design-doc C4: the multi-signature refuge/forage diversity criteria re-run; governance-weighting test for MECH-309/ARC-062) is now gated on a DIFFERENT, shared substrate -- ARC-065 GAP-A candidate-pool class diversity. Per the V3-EXQ-614e autopsy (2026-06-07): all K CEM candidates collapse to identical z_world after one E2 world-forward step (cand_world_pairwise_dist=0.0000), so every E3-side bias channel incl SD-033a sees a class-uniform candidate pool and the differentiated rule_state cannot differentiate committed SELECTION (behavioral_diversity_acceptance_criteria.md Rung 1 needs >=3 candidate first-action classes + selection from >=2). 4 convergent committed-action no-lift instances (604a/624a/614d/614e) -- the first AFTER the modulatory-bias-selection-authority gate was proven operative (V3-EXQ-643a C1 PASS) -- relocated the bottleneck OFF authority and onto GAP-A. The GAP-A fix (candidate_summary_source=e2_world_forward) landed 2026-06-07; its readiness validation V3-EXQ-649 is queued+claimed, NOT yet run. RESUME: when V3-EXQ-649 lands contributory (class-level candidate diversity exists) AND the V3-EXQ-643a/643b authority committed-action measurement is settled, queue the GAP-B behavioural falsifier via /queue-experiment -- using the within-class-REPRESENTATIVE-diversity readout (NOT committed-class entropy) per the 614e autopsy Learning #2 -- as ARM_OFF (use_candidate_rule_field=False, legacy collapsed rule_state) vs ARM_ON (field + lateral_pfc + gated_policy), with the GAP-A / authority / SD-056 stack matched on both arms. Only AFTER that lands contributory can MECH-312 EXP-0110 (IGW-046) be re-posed. No claims.yaml / scoring edits this pass (V3-EXQ-639 is non_contributory; substrate readiness does not weight governance). blocked_by below is now historical -- the rule-creator vehicle question it litigates is RESOLVED (own ree_core module, built); the live blocker is ARC-065 GAP-A / V3-EXQ-649."
      governance_2026_06_04: "Rule-creator substrate DESIGN landed (design-only; status UNCHANGED blocked_pending_substrate -- design is not implementation). The blocked_by rule-creator/discriminator substrate now has: (1) lit grounding -- ARC-063 A+B+C top-up pulls 2026-06-04 (targeted_review_tolerance_gated_rule_availability / _rule_level_credit_assignment / _candidate_rule_field_representation; 9 entries; ARC-063 lit 17->23, lit_conf 0.864) closed the 3 pre-design gaps (tolerance-gate mechanism / rule-level credit / field representation) at the mechanism level, residual rule-LEVEL specificity logged per-entry as REE extension; and (2) a V3-tractable design -- docs/architecture/arc_063_candidate_rule_field.md. KEY DESIGN MOVE: mint-then-weight split (MECH-309 literal answer) -- a non-Bayesian creator (bottom-up regularity-mint ARC-064 + top-down ARC-062 seed) mints distinct CandidateRule slots in a SUBSPACE-PARTITIONED field (Weber 2023 anti-monomodal geometry), so the rule_state handed to SD-033a is DIFFERENTIATED BY CONSTRUCTION -- inverting the 543l/598b collapse (598b C3 trainable_not_monomodal FAIL was the absence of exactly this). Tolerance-gated availability (Cavanagh/Frank; availability!=selection), cue-driven retrieval (MECH-338), eligibility-trace credit (Brzosko/Kovach). REVISION of the prior blocked_by note: the candidate VEHICLE is NOT scaffolded_sd054_onboarding (that is foraging-competence/z_goal, a distinct GAP-2 substrate); the rule-creator is its own ree_core module (ree_core/policy/candidate_rule_field.py) per the design doc -- scaffolded_sd054_onboarding is unrelated to rule minting. Proposed V3 child claims MECH-CRF-mint/-field/-tolerance/-credit (NOT registered). NEXT: /implement-substrate the design (V3-tractable; social in-face ARC-077/MECH-337 deferred -- needs caregiver-agent absent in V3). The substrate-enrichment-first vs test-design-ceiling fork the prior note flagged is now MOOT for design purposes: ARC-063 (the strong-reading rule-creator) is being built directly, in V3, not awaiting empirical discriminability. Off the V3-closure critical path (closure = GAP-2 foraging + V3-EXQ-638)."
      governance_2026_06_03: "Cross-plan reconcile (beneficiary of behavioral_diversity_isolation:GAP-B). The shared SD-056-amended MECH-341 within-class lever cycle has now RESOLVED and did NOT deliver the transitive unblock that behavioral_diversity_isolation:GAP-B governance_2026_06_01 anticipated for this row: V3-EXQ-614c FAIL non_contributory 2026-06-01 (instrumentation defect, superseded), and its corrected-harness successor V3-EXQ-614d (PASS C1/C3, FAIL C2; diagnostic, reviewed 2026-06-03) proved the within-class temperature lever has ZERO committed-action authority (third instance of the modulatory-bias-selection-authority gap). So the SD-056 amend stabilised the substrate but did not give the shared E3-scoring layer committed-action reach. arc_062_rule_apprehension:GAP-B status is UNCHANGED: still blocked_pending_substrate on the rule-creator/discriminator substrate (differentiated rule_state inputs to SD-033a), which is a DISTINCT blocker from the modulatory-bias-selection-authority gate -- the selection-authority substrate landed 2026-06-03 (implemented_pending_validation) but it addresses scoring-layer-to-argmax reach, not the absence of a rule-creator populating differentiated rule states. No status change, no claims.yaml/scoring edits; plan-doc cross-plan note only so the 614c/614d resolution is recorded against the beneficiary."
      governance_2026_05_30: "Closure-drift reconcile: status blocked -> blocked_pending_substrate (terminal). V3-EXQ-543l terminal signals (manifest 20260526T023059Z FAIL + failure_autopsy_V3-EXQ-543l_2026-05-27 confirmed) are fully absorbed; closure now sits behind a separate substrate-design step (rule-creator/discriminator), not a re-queue of the 543 lineage. blocked_by added pointing at the scaffolded_sd054_onboarding cluster. No claims.yaml, manifest, or substrate_queue edits this session (plan-doc reconcile only). NOTE on 598b: the 598b FAIL (C3 monomodal-rescue FAIL with C1 frozen_silent PASS + C2 trainable_nonzero PASS) is recorded under GAP-D's governance_2026_05_29 -- it confirms the trainable rule_bias_head wiring is correct but the upstream rule_state inputs collapse without a rule-creator producing differentiated rule states. GAP-B is the canonical closure for that upstream substrate gap. Prior governance_2026_05_29 note retained below verbatim."
      governance_2026_05_29: "V3-EXQ-598b (the 543l-autopsy-routed discriminator) ran 20260527T120345Z: C1 frozen_silent PASS + C2 trainable_nonzero PASS + C3 trainable_not_monomodal FAIL (ARM_0 [0.10, 0.06, 0.0] vs ARM_1 [0.10, 0.03, 0.0]). Governance applied: SD-033a=supports (substrate fires + head trains); MECH-262 reclassified weakens -> non_contributory + epistemic_category=substrate_ceiling + pending_retest_after_substrate=true. The substrate-enrichment-first path (GAP-C/D landed) does NOT escape MECH-309 monomodal collapse on the existing rule-creator-absent substrate. GAP-B now BLOCKED on rule-creator/discriminator substrate (a mechanism that populates DIFFERENTIATED rule_state inputs to SD-033a, not just trainable bias heads). Routes to /implement-substrate for rule-creator wiring rather than to a new GatedPolicy floor/aux escalation. ARC-062 remains weakens (1 contributory FAIL, narrow_supports_flag retained); MECH-309 remains supports."
      reconcile_2026_08_27: >
        STALE-OWNER CORRECTION (session f-dominance-regime-retest-ddbe10,
        debt-classification sweep; plan-frontmatter only, NO status change,
        nothing queued). The resume_condition's lead sentence "V3-EXQ-654h
        QUEUED + PENDING" is 2 months stale: 654h RAN TERMINAL
        FAIL/non_contributory 2026-06-21T17:57Z (manifest
        v3_exq_654h_arc062_gapb_rule_apprehension_behavioural_falsifier_20260621T175704Z_v3.json,
        reviewed). The live framing is the reconcile_2026_07_09
        competence-wall reframe below: GAP-B's operative wall is the
        MECH-457 competence cluster plus the MECH-439 corrected-DV
        conversion retest, per
        evidence/planning/work_graph_debt_classification_20260827.md
        (which classifies this node complex (probe-gated), absorbed into
        the competence unknown). Node stays in-progress.
      resume_condition: "V3-EXQ-654h RAN TERMINAL FAIL/non_contributory 2026-06-21T17:57Z (manifest v3_exq_654h_..._20260621T175704Z_v3; superseded V3-EXQ-654g). CORRECTED 2026-09-01 (gov-flagtriage-20260901, GFLAG-0053 + GFLAG-0061, which are the same finding on this one field). The sentence below is HISTORY from the 2026-06-21 queueing, retained for the lineage trail; the live framing is reconcile_2026_07_09 (competence-wall reading) plus reconcile_2026_08_27. Node stays in-progress: GAP-B closes only on a PASS C2 committed-class-entropy lift. The MECH-439 F-dominance conversion ceiling has been LIFTED operationally by the MECH-448 (ARC-107) rank-preserving F->eligibility demotion lever (promoted PROVISIONAL 2026-06-21 on the V3-EXQ-689d PASS), so the prior 'do NOT queue a 654h on the current selector' guidance is SUPERSEDED: 654h is the GAP-B committed-class-entropy falsifier ported onto that demotion conversion (use_f_eligibility_demotion=True armed as a matched-stack constant on BOTH arms; the f_demotion mode overrides the 569i top_k per ree-v3/ree_core/predictors/e3_selector.py; ONLY use_candidate_rule_field swept). RESUME PATH: await the 654h run + /governance review. On a 654h PASS (C2 committed-class entropy lift) -> MECH-309/ARC-062 SUPPORTS evidence + the FIRST downstream confirmation that the MECH-448 demotion lever generalises off the GAP-A foraging substrate onto the GAP-B rule-apprehension composite -> consider GAP-B closure (and it also closes behavioral_diversity_isolation:GAP-I). On C1-holds/C2-fails -> the conversion ceiling persists despite demotion (non_contributory, route /implement-substrate / MECH-449 follow-on), NOT a falsification, NOT a weakens. On C1-fails -> substrate_not_ready_requeue. PROMOTES NOTHING until 654h is adjudicated -- MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate. [HISTORY -- the 654g gate: V3-EXQ-654g RAN + ADJUDICATED 2026-06-19 (FAIL/non_contributory; C1 fully met, C2 +0.011 nats 0/3 seeds = the SHARED MECH-439 F-dominance conversion ceiling, NOT a falsification). The CRF instrumentation lineage is CLEANLY TERMINATED; GAP-B no longer waits on a 654-specific substrate. The (now-superseded) post-654g read was: GAP-B closes ONLY after the MECH-439 ceiling is lifted via the conversion-ceiling chain (behavioral_diversity_isolation:GAP-A ARC-065 569i top-k ceiling-lifted + the active 689a / 625e successors + MECH-439 F-rebalance), and do NOT queue a 654h on the then-current selector (it would re-derive the ceiling) -- that lift has since landed as MECH-448 and 654h IS that re-queue onto the demotion lever. [HISTORY -- the pre-654g gate: 654f (confirmed failure_autopsy_V3-EXQ-654f_2026-06-18) proved the CRF-gate calibration amend WORKED: C1 fully met (crf_frac_active 0.83-0.97 cleared the 0.30 floor; conflict-gate lockout gone; propagation non-vacuous) and the residual blocker is the SHARED selection-authority CONVERSION ceiling (behavioral_diversity_isolation:GAP-A; 569g/569h/682). 654f hit it on the SUPERSEDED additive lever ARM_STD_G2 (569h FAIL, 1/3); GAP-A has since SOLVED it via the TOP-K shortlist (V3-EXQ-569i PASS/supports 2026-06-17, ARC-065 promoted stable). RESUME PATH: /queue-experiment 654g = the GAP-B committed-class-entropy falsifier ported onto the 569i-validated TOP-K shortlist conversion (use_modulatory_shortlist_then_modulate + modulatory_shortlist_mode=top_k + modulatory_shortlist_k) as a matched-stack constant on BOTH arms, keeping the now-working CRF stack (mature + maintenance + persist + e2-context + trained-bias-head P1) constant; only use_candidate_rule_field swept. Retain the C1c crf_frac_active>=0.30 self-routing precondition (expected to clear now) + the conversion-ceiling off-ramp; three-branch NO-weakens map (C1+C2 -> supports; C1-holds/C2-fails -> deeper conversion ceiling, non_contributory; C1-fails -> substrate_not_ready_requeue). Do NOT re-queue on ARM_STD_G2 (superseded) or on a further CRF amend (CRF done -- C1 fully met). MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate until 654g is adjudicated. [HISTORY -- the 654d gate (now superseded by the 654e->654f runs + the 654f autopsy above): AWAITING V3-EXQ-654d RUN + REVIEW (QUEUED 2026-06-16, ree-v3 origin/main 927fe1c; coordinator /queue/active CONFIRMED present). The GAP-A-context-de-collapse gate is DISCHARGED -- V3-EXQ-684a PASSED 2026-06-15 (conversion_mechanism_identified), so the ARM_STD_G2 conversion config (modulatory_authority_normalize_basis=std + authority_gain=2.0 + routed e2_world_forward channel) de-collapses the e2 context the CRF mint/match keys off. 654d arms ARM_STD_G2 on BOTH arms + records crf_n_matched_last; it tests the autopsy's PRIMARY hypothesis that de-collapse alone drops n_matched enough for the existing maintenance_floor 0.45 to clear the gate (the part-(ii) CRF maintenance-theta coupling amend is NOT implemented -- substrate_queue crf-availability-maintenance ready=False -- and the C1c precondition is the guard that self-routes to it if de-collapse is insufficient). RESUME path on the 654d run: /governance adjudicate per the three-branch map (NO weakens branch while the conversion ceiling is open): (a) C1 readiness met (crf_frac_active>=0.30 cleared + C1d propagation non-vacuous + C1a/C1b) AND C2 committed-class lift (>=2/3 seeds) -> PASS -> MECH-309/ARC-062 SUPPORTS evidence -> consider GAP-B closure. (b) C1 met AND C2 fails -> SHARED selection-authority CONVERSION CEILING persisting under the validated ARM_STD_G2 lever -> non_contributory + route /implement-substrate (deeper conversion amend), NOT a falsification, NOT a weakens. (c) C1 fails (crf_frac_active<0.30 -- read crf_n_matched_last to disambiguate matched-but-gated-out [route to the CRF maintenance-theta part-(ii) amend] from never-matched; OR propagation vacuous; OR class axis / GAP-A divergence absent) -> non_contributory / substrate_not_ready_requeue -> re-queue / substrate enrichment; do NOT weaken. The 654d script implements exactly this three-branch map. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate until 654d is adjudicated. [HISTORY -- the 654c gate: V3-EXQ-654c RAN FAIL/non_contributory 2026-06-15 (confirmed failure_autopsy_V3-EXQ-654c): the 666c maintenance amend SOLVED mint/maintain (max_pairwise_dist 1.711, pool holds >=2 differentiated rules) but activation collapsed to frac_active 0.0 because the GAP-A-collapsed e2 context co-matched >=3 rules -> gate theta 0.65 > maintenance_floor 0.45 (MAINTAINED != ACTIVE); the autopsy gated 654d on GAP-A context de-collapse, now discharged by 684a above. The prior 'GATED ON V3-EXQ-654c RUN + REVIEW' / 'GATED ON V3-EXQ-666c PASS' gates are also DISCHARGED -- V3-EXQ-666c PASSED 2026-06-15 (the clean fraction-gated CRF-readiness re-run at the enlarged P0 cleared the maintained-pool gate AND all 4 non-vacuity preconditions simultaneously: ARM_2 mean_frac_maintained 0.854 > 0.625; field mints >=2 rules/cell; e2ctx full-pool differentiation 1.598 > 0.1 PRE-gap on all 3 seeds; ARM_2 maintained pool count 9 + differentiation 1.701 supra-floor) and substrate_queue crf-availability-maintenance flipped ready=TRUE (be7261d9ca). ON that PASS, V3-EXQ-654c was QUEUED 2026-06-15 (ree-v3 origin/main 7225065; coordinator /queue/active present) -- the committed-class-entropy GAP-B falsifier with the mature + e2ctx + maintenance flags armed on the matched GAP-A/authority/SD-056 stack + trained-bias-head P1 (GAP-D) + enlarged P0 (200 ep). RESUME path: await the 654c run, then /governance adjudicate per the CORRECTED branch map (the conversion ceiling is now confirmed open, so the prior 'C1 met & C2 fails -> weakens' branch is RETIRED): (a) C1 readiness met (crf_frac_active>=0.30 cleared + C1d propagation non-vacuous) AND C2 committed-class lift (>=2/3 seeds) -> PASS -> MECH-309/ARC-062 SUPPORTS evidence -> consider GAP-B closure. (b) C1 met AND C2 fails -> SHARED selection-authority CONVERSION CEILING (behavioral_diversity_isolation:GAP-A; failure_autopsy_V3-EXQ-569g_2026-06-14 + V3-EXQ-682: the channel range reaches the E3 accumulator but does not move the F-dominated committed argmax) -> non_contributory + route /implement-substrate (the GAP-A gain/contrast amend, already in flight via the parallel 682-gated conversion-amend session), NOT a MECH-309/ARC-062 falsification, NOT a weakens. (c) C1 fails (pool not maintained crf_frac_active<0.30, OR propagation vacuous ARM_ON bias == ARM_OFF, OR class axis / GAP-A divergence absent) -> non_contributory / substrate_not_ready_requeue -> re-queue / substrate enrichment; do NOT weaken. The 654c script implements exactly this three-branch map (NO weakens branch). Do NOT re-open the GAP-A or rule-creator blockers (both resolved); MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate until 654c is adjudicated. -- 654c is now adjudicated (FAIL/non_contributory, branch (b)/(c) hybrid: maintenance cleared, activation gated out under collapsed context); the live gate is GAP-A context de-collapse -> CRF activation amend -> 654d, per the updated lead above.]"
    - id: "arc_062_rule_apprehension:GAP-C"
      title: "ARC-062 discriminator output not routed to SD-033a LateralPFCAnalog.update() source vector"
      status: done
      severity: high
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [SD-033a, MECH-262, SD-034]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-27
      substrate_note: "Substrate DONE 2026-05-17. Validation V3-EXQ-598b queued 2026-05-27 (ree-v3 main 94db78d; supersedes V3-EXQ-598a; gates_on=V3-EXQ-543l with PERMISSIVE semantic; priority 240; claim_ids=[SD-033a, MECH-262]). Per failure_autopsy_V3-EXQ-543l_2026-05-27 sections 7+9, V3-EXQ-598b is the DISCRIMINATOR between substrate-enrichment-first (predicted contributory PASS) and test-design-ceiling (predicted FAIL/weakens) readings. 543l FAIL/mixed (2026-05-26) does NOT block 598b; contributory PASS on 543l is NOT required (the autopsy explicitly routes substrate-enrichment-first regardless of 543l's branch-e verdict). Evidence closure path: contributory PASS -> ARC-062 weak-reading governance-stamped viable + commitment_closure:GAP-1 closes; FAIL/weakens -> ARC-063 V4 lit-pull + design session."
    - id: "arc_062_rule_apprehension:GAP-D"
      title: "E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias head untrained)"
      status: done
      severity: high
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [SD-033a, MECH-262]
      depends_on: ["arc_062_rule_apprehension:GAP-C", "arc_062_rule_apprehension:GAP-B"]
      cross_plan_link: ["commitment_closure:GAP-1"]
      last_updated: 2026-05-29
      governance_2026_05_29: "V3-EXQ-598b ran 20260527T120345Z and confirmed C1 frozen_silent PASS + C2 trainable_nonzero PASS (head learned mean abs 0.05-0.10 when trainable; 0.0 when frozen). The optimiser DOES include rule_bias_head.parameters() under MECH-262's training regime -- this gap is RESOLVED at the substrate-wiring level. The downstream C3 monomodal-rescue failure is a separate substrate_ceiling (missing rule-creator/discriminator that would populate distinct rule states) tracked under GAP-B / MECH-262 pending_retest_after_substrate, not under GAP-D."
      substrate_note: "Substrate DONE 2026-05-17. Same validation EXQ as GAP-C: V3-EXQ-598b queued 2026-05-27 (ree-v3 main 94db78d). Gated on V3-EXQ-543l with PERMISSIVE semantic per failure_autopsy_V3-EXQ-543l_2026-05-27 routing -- requires only that 543l manifest exists with outcome in {PASS, FAIL} (clears against 543l's 2026-05-26 FAIL/mixed); contributory PASS on 543l NOT required (598b is the discriminator)."
    - id: "arc_062_rule_apprehension:GAP-E"
      title: "Multi-strategy scaling probe (>2 strategies) -- distinguishes ARC-062 weak from ARC-063 strong"
      status: deferred
      severity: medium
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-063]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-F"
      title: "Clinical / failure-mode tests (trauma-schema / paranoid-rule-field / depressive-rollout-constraint) -- ARC-063 falsifiable predictions (b)"
      status: deferred
      severity: low
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-063]
      depends_on: ["arc_062_rule_apprehension:GAP-E"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-G"
      title: "Sleep-vs-waking refinement asymmetry tests -- ARC-063 falsifiable predictions (c) and Pull C lit-pull placeholder"
      status: deferred
      severity: low
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-063]
      depends_on: ["arc_062_rule_apprehension:GAP-E"]
      cross_plan_link: ["sleep_substrate:GAP-1"]
      last_updated: 2026-05-09
    - id: "arc_062_rule_apprehension:GAP-H"
      title: "ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending"
      status: partial
      severity: medium
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-065, Q-043, Q-044, Q-045]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      cross_plan_link: ["behavioral_diversity_isolation:GAP-C"]
      last_updated: 2026-07-20
      governance_2026_07_20: "Closure-drift stale-since-review ACKNOWLEDGE (governance cycle 2026-07-20T15:57Z). Flagged because confirmed failure_autopsy_V3-EXQ-604c_2026-07-20 reclassified Q-044 (in this node's unblocks set). Does NOT change GAP-H, but IS substantive: the 604c re-adjudication demoted the Q-044/MECH-314b/MECH-314c family to non_contributory/substrate_ceiling, and those three claims now read candidate_substrate_landed with pending_retest_after_substrate still TRUE after the modulatory-bias-selection-authority substrate landed -- i.e. the Q-044/MECH-314-family leg this node recorded as SATISFIED (governance_2026_06_08, on the 604c PASS) has been RE-OPENED by the re-adjudication of that same run. The substrate-ceiling audit lists all three under ceiling-may-have-lifted (ACTIONABLE): the bounding substrate is in, so the owed retest is now RUNNABLE. Surfaced to the user this cycle as owed work; NOT queued here (experiment authoring goes through /queue-experiment). The remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg is unaffected and still awaits behavioral_diversity_isolation:GAP-C. Status stays partial; owner_exq unchanged; last_updated bumped 2026-07-17 -> 2026-07-20."
      rescope_note_2026_07_17: "BUILD-TARGET ROUTING (session trusting-williams-ac3b1d; metabolizes the curiosity=exploitation-amplifier reframe, registered MECH-458). PROMOTES/DEMOTES NOTHING; changes NO status/owner_exq/unblocks_claims. The H1 curiosity leg (Q-044/MECH-314, 604c PASS) is DONE for APPROACH-emergence but the reframe (V3-EXQ-767a + V3-EXQ-768a, both cloud PASS; MECH-458) shows the SD-025/MECH-314 curiosity/density-attraction drive is exploitation-dominant (rich-get-richer; 0 proactive pull toward under-represented regions; SD-025-alone-on-a-flat-map = 0) -- so it is structurally the WRONG force for strategy-diversity GENERATION. When ARC-065/MECH-314 is next built for the diversity-generation goal, route it as a PROACTIVE rarity-seeking drive (Bellemare-2016 polarity: attraction to LOW-count / under-represented strategy classes, independent of reward-shaping), NOT a novelty-MAGNITUDE sweep of the existing drive (768a: the flat-map arm reads ~0 regardless of weight; the infant_substrate:GAP-13 magnitude lever cannot help). ORDERING-GATED on INV-088 z_world differentiation (differentiate-first: a rarity term over an AUC-0.83 under-differentiated map chases the sparse corner, not diverse strategies -- matches monostrategy_representation_ceiling). The generation face this feeds is conversion_ceiling_campaign:GENERATION (added same session). Build is BLOCKED-ON-UPSTREAM INV-088; nothing queued here. See docs/architecture/sd_024_da_modulated_rbf_density.md#curiosity-exploitation-polarity-mech-458."
      governance_2026_06_23: "STALENESS FIX + SPLIT ANNOTATION (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). owner_exq said 'V3-EXQ-687 QUEUED 2026-06-17 ... AWAITING RUN+REVIEW' but 687 RAN TERMINAL FAIL/non_contributory 2026-06-18 (confirmed failure_autopsy_V3-EXQ-687_2026-06-18; reviewed; removed from queue) -- updated to the ran/autopsied record. Annotated the node's two structurally-distinct legs in owner_exq: [H1] Q-044/MECH-314 curiosity = DONE (604c PASS); [H2] Q-045/MECH-313/MECH-260 noise-floor = OPEN (687 FAIL; successor owed, blocked on behavioral_diversity_isolation:GAP-C; MECH-440 fix decision_due 2026-07-02). Kept as ONE `partial` node (status already encodes one-done/one-open; the noise-floor build leg's home is behavioral_diversity_isolation:GAP-C, now cross-linked). No status change."
      governance_2026_06_18_b_note: "Convergence + drift entries retained below."
      convergence_2026_06_18: "CONVERGENCE MECHANISM CANDIDATES REGISTERED (Convergence Demand Pipeline CDQ-002; session convergence-cdq002-noisynet-intake-20260618T0643Z). This node's Q-045/MECH-313/MECH-260 survival/noise-floor leg now has a registered candidate mechanism: MECH-440 (state_conditioned_self_annealing_noise_floor, NoisyNet analog extending MECH-313) -- learned per-parameter WEIGHT noise that PROPAGATES into the committed action (targets the V3-EXQ-687 non-propagation / r1a_entropy_only_artefact), is state-conditioned, and self-anneals; biology-anchored by lit-pull (Aston-Jones&Cohen 2005 adaptive gain + Tervo et al 2014 LC->ACC stochastic-choice gating). The Q-044/MECH-314 curiosity leg of this node is ALREADY satisfied (V3-EXQ-604c); MECH-441 (model_disagreement_directed_curiosity, RND/Plan2Explore analog extending MECH-314) does NOT reopen it -- it refines the curiosity MECHANISM (per-candidate model-disagreement that propagates, vs the V3-EXQ-590a broadcast-EMA non-propagation). Both candidate/substrate_ceiling/v3/v3_pending, each with a falsifier, MECH-440 depends_on MECH-313/MECH-260/Q-045/ARC-065 + MECH-441 depends_on MECH-314/ARC-065. OFF the V3 critical path: registered candidates only -- promotes nothing, changes NO node status/phase/owner_exq; status stays partial. Shared with behavioral_diversity_isolation:GAP-C (the noise-floor leg's home node). decide-whether-to-build is a later governance step (packet CPKT-TONIC-EXPLORATION-NOISE-20260618, decision_due 2026-07-02)."
      governance_2026_06_18: "Closure-drift stale-since-review ACKNOWLEDGE (governance cycle 2026-06-18T08:04Z). Flagged because confirmed failure_autopsy_V3-EXQ-687_2026-06-18 reclassified Q-045 (in this node's unblocks set). Does NOT change GAP-H: the 687 autopsy (handled in its own session) self-routed substrate_not_ready_requeue -> Q-045/MECH-313/MECH-260 stay candidate/substrate_ceiling/v3_pending (NOT weakened); the noise-floor leg still awaits the behavioral_diversity_isolation:GAP-C conversion stack (687-successor arming the 569i conversion). Status stays partial; owner_exq unchanged; last_updated bumped to acknowledge."
      governance_2026_06_17: "Closure-drift stale-since-review acknowledgement (governance cycle 2026-06-17). Flagged because failure_autopsy_V3-EXQ-569h_2026-06-16 (confirmed) touches ARC-065 (in this node's unblocks set). This cycle the shared GAP-A CONVERSION ceiling that the 569h autopsy diagnosed was LIFTED: V3-EXQ-569i PASS (top-k shortlist conversion) cleared C_R1B, so ARC-065 epistemic_category substrate_ceiling -> standard + pending_retest cleared. Does NOT change GAP-H: the Q-045/MECH-313/MECH-260 survival/noise-floor leg still awaits behavioral_diversity_isolation:GAP-C, and rule-apprehension closure still depends on the GAP-B successor (654e on the crf-availability-maintenance amend). Status stays partial; owner_exq unchanged; last_updated 2026-06-14 -> 2026-06-17 to acknowledge. SECOND 2026-06-17 update (later cycle, governance-20260617T1245Z): the Q-045/MECH-313/MECH-260 noise-floor/anti-recency leg now has a dedicated queued owner -- V3-EXQ-687, the registered 4-arm tonic-noise ablation (both-OFF/313-only/260-only/both-ON, ARC-062 gated-policy all arms) built on the now-survival-competent scaffolded_sd054_onboarding substrate (603q PASS 2026-06-17 cleared the survival gate the 603a-e Q-045 chain kept dying on). owner_exq repointed to name 687. Status stays partial (687 queued, not run); behavioral_diversity_isolation:GAP-C survival substrate is the shared dependency 687 builds on."
      governance_2026_06_14: "Closure-drift stale-since-review acknowledgement (governance cycle 2026-06-14). Flagged because failure_autopsy_V3-EXQ-569g_2026-06-14 (confirmed) touches ARC-065 (in this node's unblocks set). The 569g autopsy diagnoses the GAP-A channel->committed-action CONVERSION ceiling and explicitly leaves ARC-065 UNCHANGED (stays provisional / non_contributory / pending_retest_after_substrate -- no demotion). SEPARATELY this cycle promoted MECH-314a candidate_substrate_landed -> provisional (Q-044/MECH-314 family, this node's already-satisfied leg per V3-EXQ-604c) after the flat-authoritative indexer correction (074ab9401e) lifted exp_conf to 0.759. Neither changes GAP-H: the Q-045/MECH-313/MECH-260 survival/noise-floor leg still awaits behavioral_diversity_isolation:GAP-C and rule-apprehension closure still depends on the GAP-B successor. Status stays partial; owner_exq unchanged; last_updated bumped to acknowledge."
      governance_2026_06_12: "Closure-drift stale-since-review acknowledgement (governance cycle 2026-06-12). Flagged because failure_autopsy_V3-EXQ-667_2026-06-11 reclassified Q-043 (in this node's unblocks set): the 667 magnitude-sweep self-route was CONFIRMED substrate_not_ready (modulatory-bias-selection-authority bottleneck), Q-043 stays open / pending_retest with an added evidence_quality_note, no demotion. Does NOT change GAP-H: the Q-045/MECH-313/MECH-260 leg still awaits behavioral_diversity_isolation:GAP-C and rule-apprehension closure still depends on the GAP-B successor. Status stays partial; owner_exq unchanged; last_updated bumped to acknowledge."
      governance_2026_06_08: "Case 3 in closure-drift terms. Plan-drift reconcile. V3-EXQ-604c PASS on the V3-EXQ-649 GAP-A-ready stack gives contributory support to the Q-044/MECH-314 family and governance lifted their v3_pending/pending_retest_after_substrate flags. GAP-H remains partial, not done: the Q-045/MECH-313/MECH-260 leg still depends on behavioral_diversity_isolation:GAP-C / V3-EXQ-603i, and rule-apprehension cross-plan closure still depends on the newly unblocked GAP-B behavioural falsifier."
      governance_2026_06_06: "Closure-drift stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-621a_2026-06-06 (confirmed) reclassified Q-045 in this node's unblocks set. 621a is a vacuous-pass correction on the scaffolded SD-054 onboarding substrate-readiness diagnostic (appended an evidence_quality_note correction; moved NO claim confidence -- non_contributory / scoring_excluded) and is unrelated to the absent rule-creator/discriminator substrate this node tracks; GAP-H stays partial, still blocked behind arc_062_rule_apprehension:GAP-B. last_updated bumped to acknowledge."
      governance_2026_06_03: "Closure-drift stale-since-review acknowledgement only (no status change). The drift report flagged this node because confirmed autopsies post-dating last_updated reclassified ARC-065 (failure_autopsy_V3-EXQ-614b_2026-05-31, failure_autopsy_V3-EXQ-569e_2026-05-31) and Q-045 (failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03), which intersect this node's unblocks set. None change GAP-H: the MECH-318 empirical retire-vs-promote gate remains blocked behind arc_062_rule_apprehension:GAP-B (rule-creator/discriminator substrate), and the modulatory-bias-selection-authority gap that the 614/603e cluster surfaced is a DISTINCT scoring-layer-to-argmax blocker (substrate implemented_pending_validation 2026-06-03), not the absent rule-creator GAP-H/GAP-B depend on. Status stays partial; last_updated bumped to acknowledge the new evidence."
      resume_condition: "PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-603i lands, and hold rule-apprehension closure on the GAP-B successor. GAP-H closes only after those remaining legs settle."
    - id: "arc_062_rule_apprehension:GAP-I"
      title: "ARC-064 bottom-up rule-discovery cluster (MECH-318 absorption check done; MECH-316 / MECH-317 checks STILL OPEN -- see GAP-I-absorption); empirical gate pending"
      status: blocked_pending_substrate
      severity: medium
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-064, MECH-318]
      depends_on: ["arc_062_rule_apprehension:GAP-B", "arc_062_rule_apprehension:GAP-C"]
      last_updated: 2026-06-23
      governance_2026_06_23: "SPLIT + FORK ANNOTATION (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). This node bundled two radically different readiness levels: MECH-318 (has an empirical retire-vs-promote gate, gated on GAP-B) vs MECH-316/317 ('absorption checks remain doc-only -- no V3 modules', per the resume_condition). Split MECH-316/317 out to a child node arc_062_rule_apprehension:GAP-I-absorption (deferred, V4-leaning -- no V3 substrate exists for them); GAP-I now tracks the MECH-318 empirical gate only (unblocks_claims narrowed [ARC-064, MECH-316, MECH-317, MECH-318] -> [ARC-064, MECH-318]). FORK NOTE: GAP-I is the BOTTOM-UP rule-discovery path (ARC-064) opposing GAP-B's TOP-DOWN ARC-062 score_bias path -- the two canonical OR-approaches to populating differentiated rule_state, currently drawn only as a linear depends_on GAP-B chain. The dead-end 543k pin in the 606b script (GATES_ON_EXQ=V3-EXQ-543k, a FAIL/mixed terminus) must be re-gated to the GAP-B-resolving EXQ at the eventual /queue-experiment re-queue (already flagged in resume_condition). No status change (stays blocked_pending_substrate)."
      resume_condition: "BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 empirical retire-vs-promote gate (per claims.yaml MECH-318: verdict deferred to 'ARC-062 Phase 2 GAP-B PASS + Phase 3 GAP-C closure') cannot run before GAP-B resolves -- a multi-rule-context falsifier needs the cluster to produce differentiated rule_state first. MECH-318/ARC-064/MECH-316/MECH-317 are correctly held by the indexer (candidate + v3_pending/implementation_phase=v3 -> hold_pending_v3_substrate); no governance-pipeline action is stuck. STALE-PIN WARNING: the committed 606b script hardcodes GATES_ON_EXQ=V3-EXQ-543k, and 543k ran 20260522T091714Z FAIL/mixed (done, never re-runs) -- that pin is a DEAD END. Do NOT wait on a '543k successor contributory PASS' (the prior 2026-05-23 HOLD note); GAP-B was re-framed to blocked_pending_substrate on 2026-05-30 and its line moved past 543k (543l FAIL -> rule-creator substrate). 606b dry_run 20260523T223001Z FAIL/weakens (C3 PASS, C1/C2 FAIL). RESUME: when GAP-B resolves (rule-creator substrate validated via the scaffolded_sd054_onboarding cohort -- e.g. the V3-EXQ-620 / 603e / 591b line), queue a 606b-successor via /queue-experiment RE-GATED to the GAP-B-resolving EXQ (NOT 543k); the existing 606b script GATES_ON_EXQ=V3-EXQ-543k must be replaced at that time (script-logic change -> /queue-experiment, not a hand edit). DIAGNOSE-ERRORS NOTE: V3-EXQ-606a stays an unaddressed ERROR in /diagnose-errors scans (sync-lag infra error on ree-cloud-2, not a code bug; 606b is its byte-identical re-queue, parked here) until a 606b-successor actually runs -- this is expected; do not re-diagnose 606a or write a 606c. Episode-boundary multi-rule via alternating bipartite axis; MECH-318 empirical gate only. MECH-316/317 absorption checks remain doc-only (no V3 modules)."
    - id: "arc_062_rule_apprehension:GAP-I-absorption"
      title: "ARC-064 absorption checks for MECH-316 (cross-episode regularities) + MECH-317 (behavioural-pattern compression) -- doc-only, no V3 modules (split out of GAP-I)"
      status: blocked_pending_substrate
      severity: low
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [MECH-316, MECH-317]
      depends_on: ["arc_062_rule_apprehension:GAP-I"]
      last_updated: 2026-09-01
      governance_2026_09_01: "MECH-317 ABSORPTION CHECK DELIVERED -- this node's owed memo, half discharged (session mech317-absorption-20260901, user-directed). Artifact: docs/architecture/mech_317_absorption_check.md, written against the docs/architecture/mech_318_absorption_check.md template as this node's own 2026-08-18 adjudication prescribed ('the absorption-check memo needs no substrate at all, only the MECH-318 template applied to two siblings'). VERDICT (B) PARTIALLY ABSORBED, mirroring the MECH-318 sibling check's own verdict: MECH-317's compression MECHANISM (options triple, compressibility trigger, reusable-unit creation, temporally-extended selection) absorbs completely into the built ARC-071/MECH-323/MECH-324 cluster -- ChunkedPrimitive carries initiation_set + termination_condition as first-class fields at policy_chunking.py:513-514 with a docstring citing Sutton 1999 directly, and policy_chunking.py never references MECH-317/ARC-064/MECH-318, i.e. it CONVERGENTLY re-derived the mechanism under a different parent. But MECH-317's DEPENDENT VARIABLE does not absorb: its registered falsifier needs chunk boundaries detectable as action-distribution entropy troughs, and NO action-stream boundary readout exists anywhere in ree_core (entropy_trough / chunk_boundary / action_distribution_entropy / boundary_detect / boundary_readout: zero hits each). NEAR-MISS RECORDED so it is not mistaken for the instrument: first_action_entropy (hippocampal/module.py:757) measures proposal-pool diversity at ONE decision point, not entropy over the executed action stream across time. FULL SUPERSEDE IS NOT WARRANTED ON PRESENT EVIDENCE: ARC-071, the proposed absorbing survivor, has genuine_exp_count 0 / exp_conf 0.0 / plausible_unproven -- THE SAME QUADRANT as the claim it would absorb -- so the evidence-tree discriminator that decided the 2026-08-15 orphan adjudication does not separate them at parent level; and the children's separation rests on one un-autopsied scored FAIL (V3-EXQ-829) plus one PASS degenerate on its load-bearing criterion (V3-EXQ-829a: interpretation.criteria_non_degenerate.C2 False, all iso-on cells on the forced bar, rho 0.9999999999999998 -- an arithmetic identity; note its TOP-LEVEL non_degenerate reads True, so the run-level gate reports clean over a degenerate verdict criterion). Memo also records that a full supersede would ORPHAN TWO CONSUMER EDGES -- MECH-318 (rule-state abstraction) and MECH-312b (practice-maturity weighting), the latter named in no flag's claim_ids -- neither of which any ARC-071-family claim asserts anywhere (verified). And that a PRIOR ADJUDICATION already exists uncited: EXP-0263/EVB-0227, gated 2026-08-02, recommending exactly superseded_by ARC-071/MECH-323/MECH-324, 25 days before GFLAG-0066. NO DISPOSITION APPLIED -- the memo produces a verdict for governance; no claims.yaml status, epistemic_category, v3_pending or depends_on changed by this pass. NODE STAYS NON-TERMINAL: MECH-316's half of this node is untouched and out of scope for this memo, exactly as the MECH-318 check scoped out its own siblings. Status left at blocked_pending_substrate rather than moved, but flagged for the next cycle: BOTH halves of this node are doc-only by the node's own title, so 'blocked_pending_substrate' may be the wrong status for a blocker that needs no substrate -- MECH-317's half just proved that by being dischargeable at a desk. Answers GFLAG-0066 and GFLAG-0087; bears on GFLAG-0084 (which additionally bundles three separable items the memo recommends lifting out: 829's missing autopsy, the SD-083 cross-registry id collision, and 834's unmeasured growable-ceiling prediction). last_updated bumped 2026-08-18 -> 2026-09-01."
      registered_note: "Registered 2026-06-23 (session closure-map-enhance-20260623T043407Z) splitting MECH-316/MECH-317 out of GAP-I. Per GAP-I's resume_condition, 'MECH-316/317 absorption checks remain doc-only (no V3 modules)' -- they have NO empirical gate and no V3 substrate, unlike MECH-318 (which GAP-I retains). They are V4-leaning (the bottom-up rule-discovery cluster's deeper legs) and held deferred so GAP-I's MECH-318 empirical-gate readiness is not conflated with these doc-only legs. Reclassify to generation:v4 + cross-link to a V4 plan if/when a bottom-up rule-discovery substrate is scoped. NO claims.yaml change (MECH-316/317 stay candidate)."
      governance_2026_08_15: "ADJUDICATED (session orphan-v3-claims-adjudicate-6f88bd, chip-20260815-orphan-v3-claims-adjudicate; D-002 orphan-V3-claim finding, severity P0/strong, confidence 0.95). NOTE ONLY -- NO status change applied here, because changing a pre-existing node's status was outside this session's authority; the change is PROPOSED to /governance and the closure effect is MEASURED below. VERDICT: this node's `deferred` status is NOT justified and MECH-316/317 are live V3 work. FIVE artefacts consulted, FOUR say V3/open against this node alone: (1) claims.yaml MECH-316 line 51365 + MECH-317 line 51437 -- implementation_phase v3, v3_pending TRUE, status candidate, live_status reading candidate/v3_pending, verdict hold_pending_v3_substrate/applied (a HOLD pending V3 substrate is a statement that the work IS V3, not that it is V4); (2) substrate_queue.json carries sd_id MECH-316 AND MECH-317 as SEPARATE entries, status `candidate_v3_pending`, priority 3, ready false, ready_blocked_by 'Absorption-check verdict pending', depends_on_unresolved ['absorption-check memo','multi-rule-context substrate'] -- a live V3 queue entry, which is not the shape of a V4 placeholder (contrast the SD-031 precedent, where the same field read `implemented`); (3) docs/architecture/mech_318_absorption_check.md, the AUTHORITATIVE memo, says at lines 13/153/164 that the MECH-316/317 sibling absorption checks are 'still-open' and 'separately scoped tasks' -- open, explicitly NOT V4; (4) the PARENT node arc_062_rule_apprehension:GAP-I is `blocked_pending_substrate` (weight 0.1, counted) while blocked on the SAME 'multi-rule-context substrate' this node is blocked on -- same blocker, opposite denominator treatment, within one plan; (5) this node, deferred/'V4-leaning'. Evidence tree: 0 manifests for either claim, which is consistent with un-run work under either reading and therefore discriminates nothing. MECHANISM (why the inconsistency arose): a HALF-APPLIED RECLASSIFICATION, not staleness. The 2026-06-23 split acted on a V4-leaning JUDGEMENT by setting `deferred` -- which takes effect in generate_closure_snapshot.py DEFERRED_STATUSES IMMEDIATELY -- while explicitly declining the matching registry change ('NO claims.yaml change') and making the v4 reclassification CONDITIONAL on a future event ('if/when a bottom-up rule-discovery substrate is scoped') that has not occurred in the ~7.7 weeks since. So the exclusion from the V3 denominator went live while its own stated precondition never held. This is a DIFFERENT mechanism from the SD-031/GAP-5 precedent (2026-08-15), where the node was simply never revisited after a rescope; this node HAS been revisited twice (table row added 2026-07-29, live-block forward-stamp 2026-08-08) and the deferral survived both because neither pass re-opened the reclassification question. COMPOUNDING DEFECT, fixed in this same commit: GAP-I's title asserted 'MECH-316 / MECH-317 / MECH-318 absorption check done', which artefact (3) directly contradicts for 316/317 -- so the one artefact that could have retired these claims out of V3 was itself false, and would have been read as licence to leave this node deferred. PROPOSED FIX (route: /governance): set this node `blocked_pending_substrate` to match parent GAP-I, severity low, keeping unblocks_claims [MECH-316, MECH-317]. Do NOT split a new node out of it (the SD-031 template does not apply -- GAP-5 legitimately RETAINED SD-030 as genuine V4 work, whereas this node holds ONLY 316/317 and a split would leave an empty shell). NO claims.yaml change is proposed: the registry is already correct. Note one half of the blocker is `complicated (buildable)` right now -- the absorption-check memo needs no substrate at all, only the MECH-318 template applied to two siblings; only the empirical half waits on the multi-rule-context substrate. CLOSURE EFFECT, MEASURED not estimated, by A/B regeneration of scripts/generate_closure_snapshot.py in an isolated worktree at the same base (REE_assembly HEAD 2026-08-15), this node plus behavioral_diversity_isolation:GAP-G and commitment_closure:GAP-7 all moved deferred -> blocked: 71.9% across 94 non-deferred nodes -> 70.0% across 97, remaining 32 -> 35, done UNCHANGED at 62, deferred 13 -> 10. The three nodes contribute weight 0.1 each. The percentage FALLS because the correction surfaces hidden remaining work; that is the point, exactly as in the SD-031 split. Per-node attribution was not separated -- the three were measured as one A/B."
      governance_2026_08_18: "UN-DEFER APPLIED (/governance cycle 2026-08-18, session governance-paused-bb6e76, resolving GFLAG-0041). The 2026-08-15 D-002 adjudication recorded immediately above PROPOSED this change and correctly declined to apply it outside its own authority; governance has now reviewed and ACCEPTED it in full, as proposed and without revision. Applied exactly: status deferred -> blocked_pending_substrate to match parent GAP-I, severity stays low, unblocks_claims stays [MECH-316, MECH-317], NO new node split out, and NO claims.yaml change (the registry is already correct -- MECH-316/317 are candidate + implementation_phase v3 + v3_pending true, which is a statement that the work IS V3). EFFECT: these two claims re-enter the V3 progress denominator, from which the half-applied 2026-06-23 reclassification had excluded them for ~7.7 weeks while its own stated precondition ('if/when a bottom-up rule-discovery substrate is scoped') never held. Measured jointly with behavioral_diversity_isolation:GAP-G and commitment_closure:GAP-7, the three move closure from 71.9% across 94 non-deferred nodes to 70.0% across 97; the percentage FALLS because the correction surfaces hidden remaining work, which is the intended direction. Note the adjudication's own observation that one half of the blocker is 'complicated (buildable)' right now -- the absorption-check memo needs no substrate at all, only the MECH-318 template applied to the two siblings; only the empirical half waits on the multi-rule-context substrate."
    - id: "arc_062_rule_apprehension:GAP-J"
      title: "MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)"
      status: blocked
      severity: low
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [MECH-312, MECH-312a, MECH-312b, MECH-312c, MECH-312d]
      depends_on: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-17
    - id: "arc_062_rule_apprehension:GAP-K"
      title: "MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-06-02"
      status: in-progress
      severity: medium
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [MECH-319]
      depends_on: ["arc_062_rule_apprehension:GAP-B", "arc_062_rule_apprehension:GAP-H", "arc_062_rule_apprehension:GAP-I"]
      last_updated: 2026-06-19
      convergence_2026_06_19: "CONVERGENCE MECHANISM CANDIDATES REGISTERED (Convergence Demand Pipeline CDQ-005; session convergence-cdq005-muzero-reanalyze-20260619T1856Z). This node's replay-write-gating locus now has two registered candidate mechanisms that EXTEND MECH-319 (already owned, V3-EXQ-628 PASS/supports) from a BINARY block-vs-admit gate to a graded write channel: MECH-443 (priority_weighted_replay_write_selection -- WHICH/HOW-STRONGLY admitted replayed transitions write, weighted by an update-utility/surprise/value-error proxy; MuZero/EfficientZero prioritized-replay analog) + MECH-444 (staleness_gated_target_refresh_on_replay_write -- recompute the write target against the current model before it updates the rule layer, down-weighting low-drift writes; MuZero reanalyze analog, the more speculative leg). Both candidate/substrate_ceiling/generation:v3/v3_pending, each with a falsifier, depends_on MECH-319/MECH-094/MECH-312/ARC-062 (443) and MECH-319/MECH-443/MECH-094 (444); arch stub docs/architecture/prioritized_replay_write_gating.md. Biology /lit-pull BEFORE registering (SD-003/SD-010-011 discipline): evidence/literature/targeted_review_replay_prioritization_mech_319/, 5 sources, SYNTHESIS verdict SUPPORTED-with-refinement -- hippocampal SWR replay is demonstrably PRIORITIZED not uniform (Mattar & Daw 2018 gain x need; Olafsdottir 2015; Haga & Fukai 2018 write-gating; Milstein 2022 substrate availability), with the LOAD-BEARING refinement (Carey et al. 2019) that priority is update-utility, NOT reward magnitude. NON-DUPLICATIVE vs MECH-319: 319 = WHETHER the channel is open; 443/444 = WHICH writes / how FRESH. OFF the V3 critical path: registered candidates only -- promotes nothing, changes NO node status/phase/owner_exq/unblocks_claims; GAP-K stays in-progress. decide-whether-to-build is a later governance step (packet CPKT-MUZERO-REANALYZE-20260619; the actual cross-repo handoff RUN is owned by the HANDOFF-REACTIVATE pipeline node). last_updated bumped 2026-06-08 -> 2026-06-19 to record the registration."
      governance_2026_06_08: "Plan-drift reconcile. V3-EXQ-628 is already absorbed as a PASS/supports evidence-grade MECH-319 replay/caller_sim falsifier; no additional action is owed for that replay/write-gate slice. GAP-K stays in-progress because closure still waits on sibling dependencies: GAP-B is now open/ready to queue but not done, GAP-H is partial, and GAP-I remains blocked_pending_substrate."
      governance_2026_06_06: "PARTIAL ADVANCE ONLY -- node does NOT fully close. V3-EXQ-628 LANDED PASS (supports MECH-319, first evidence-grade falsifier; exp_conf 0.766, conflict 0) and is now folded into governance: MECH-319 evidence_quality_note cites it and the canonical runs/ pack was reconstructed from the cloud-2 flat manifest so build_experiment_indexes.py scores it (it had never been scored -- flat-only sync gap). This advances ONLY the MECH-319-evidence side of GAP-K. MECH-319 STAYS candidate_substrate_landed (no promotion): single contributory entry < min_experimental_entries=2, and v3_pending held. GAP-K remains in-progress because its depends_on -- GAP-B (weak-route gating, blocked, owned by V3-EXQ-543i/543j), GAP-H (diversity-generation, partial), GAP-I (multi-rule-context substrate, partial) -- are all still substrate-blocked. The deferred-AFTER-siblings condition on the falsifier is satisfied for the replay/caller_sim path, but the broader GAP-K closure waits on those sibling substrates."
      resume_condition: "IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate."
    - id: "arc_062_rule_apprehension:GAP-L"
      title: "Biology lit-pull prerequisite for the socially-scaffolded rule-population sub-cluster (ARC-077 / MECH-337 / MECH-338) -- HARD GATE before any implementation"
      status: done
      severity: load-bearing
      live:
        as_of: "2026-08-08"
        from: "failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08"
        verdict: "non_contributory/measurement_test_design_defect"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: true
        needs_review_reasons: ["newest_forward_predates_later_decision+manifest_event(s)"]
      join:
        bears_on: ["ARC-063", "f_dominance_conversion_ceiling", "ree_ai_design_critique_plan:WS-1"]
        scope_claims: ["MECH-309", "ARC-062", "ARC-063", "ARC-064", "ARC-065", "ARC-077", "MECH-337", "MECH-338", "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d", "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c", "MECH-316", "MECH-317", "MECH-318", "MECH-319", "Q-043", "Q-044", "Q-045", "SD-054", "SD-029", "MECH-269"]
      unblocks_claims: [ARC-077, MECH-337, MECH-338, ARC-063]
      depends_on: []
      last_updated: 2026-05-18
      resume_condition: "DONE 2026-05-18 (session gap-l-litpull-socially-scaffolded). The biology-before-formal-definitions lit-pull is DISCHARGED: 8 entries written + indexed in evidence/literature/targeted_review_socially_scaffolded_rule_population, tagged ARC-077/MECH-337/MECH-338, covering the full minimum-coverage set -- Csibra & Gergely 2009 natural pedagogy/ostensive cueing; Wood/Bruner/Ross 1976 scaffolding + Vygotsky ZPD; Tomasello et al. 2005 shared intentionality/joint attention/social referencing; Tulving & Thomson 1973 encoding-specificity; Godden & Baddeley 1975 context-dependent memory (with the 2021 failed-replication caveat logged); Nakazawa et al. 2002 CA3 pattern-completion substrate; plus two principled counterweights (Heyes 2016 innateness critique; Spelke & Kinzler 2007 core-knowledge / endogenous-maturational scope bound). claims.yaml lit_conf set as a PARALLEL signal: ARC-077=0.74, MECH-337=0.78, MECH-338=0.75 (indexer parallel literature_confidence 0.868/0.878/0.813). The LIT gate is now satisfied; ARC-077/MECH-337/MECH-338 REMAIN candidate -- discharging the lit-pull does NOT promote them (lit and exp evidence are not co-equal; exp_conf=0). The SECOND HARD GATE remains independently OPEN and is NOT discharged by this work: the pathway still requires a caregiver/teacher-agent substrate that DOES NOT EXIST in V3 (single-agent); scaffolded exposure needs a second agent or an ostensive-cue-delivering environment -- a required new substrate. Implementation scheduling of ARC-077 still requires that caregiver-agent substrate gate to be separately resolved. This gate is independent of the ARC-062 weak-route verdict (GAP-B remains blocked, owned by V3-EXQ-543i/543j); no ARC-062 posture change. PRIOR (BLOCKED 2026-05-18, registration session): NO implementation may begin until the caregiver-scaffolding/cued-recall lit-pull is discharged AND the caregiver-agent substrate exists; ARC-077/MECH-337/MECH-338 carried lit_conf=0."
---
# Rule Apprehension Plan (ARC-062 / MECH-309 / ARC-063)

**Registered:** 2026-05-09
**Status:** active
**Scope:** the rule-apprehension architectural slot identified by MECH-309's
logical-necessity claim. ARC-062 weak reading is the V3-tractable
instantiation; ARC-063 strong reading is the V4-deferred biology-faithful
elaboration. SD-054 reef substrate provides the substrate the falsifier runs
on; SD-029 monomodal-collapse measurement provides the dependent variable.
Sibling plans: [commitment_closure_plan.md](./commitment_closure_plan.md)
(GAP-1 SD-033a bias head training is downstream of this plan's Phase 3),
[self_attribution_plan.md](./self_attribution_plan.md), [goal_pipeline_plan.md](./goal_pipeline_plan.md),
[sleep_substrate_plan.md](./sleep_substrate_plan.md), and
[sd033_governance_plan.md](./sd033_governance_plan.md).

This plan is the durable resume-point for rule-apprehension cluster work
across sessions. When work pauses to handle adjacent paths, the deviation is
logged in the [Decision log](#decision-log) with a resume condition.

---

## One-line framing

> **MECH-309: trainers weight rules they do not invent.** Without a
> non-Bayesian rule-creator at the policy layer, gradient descent on a
> parametric policy collapses to the smoothest single regime good-enough
> across the whole state space. ARC-062 is the V3-tractable architectural
> slot for the rule-creator (gated-policy heads + learned context
> discriminator); ARC-063 is the V4-deferred biology-faithful elaboration
> (distributed CandidateRule field). The SD-054 reef substrate is the
> falsifier; the SD-029 monomodal-collapse measurement is the dependent
> variable; biology has been pulled to ground R1 / R2 / R3 / R4 with
> resolved defaults.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| MECH-309 / ARC-062 / ARC-063 entries in [docs/claims/claims.yaml](../claims/claims.yaml) | Cluster registration 2026-05-08 -- diagnostic + V3 weak + V4 strong |
| [docs/architecture/rule_apprehension_layer.md](../../docs/architecture/rule_apprehension_layer.md) | 2026-05-04 thought-intake on tolerance-gated rule apprehension |
| [evidence/literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md](../literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md) | Pull A (8 entries) -- R1 / R2 / R3 verdicts |
| [evidence/literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md](../literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md) | Pull B (6 entries) -- R4 verdict |
| [docs/architecture/sd_054_reef_enrichment_substrate.md](../../docs/architecture/sd_054_reef_enrichment_substrate.md) | SD-054 reef substrate spec (Phase 2 falsifier env) |
| [evidence/planning/commitment_closure_plan.md](./commitment_closure_plan.md) GAP-1 | Sibling plan; SD-033a bias head training is downstream of this plan's Phase 3 |
| [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) | SD-033a substrate spec (where the discriminator output gets wired) |
| substrate_queue.json ARC-062 entry (added by this plan registration) | Implementation status anchor |
| Empirical anchors: V3-EXQ-522 substrate-ceiling PASS under heuristic policy; V3-EXQ-433e/433f/523/523a/523b non_contributory under trained policy | The monomodal-collapse signature MECH-309 explains |

---

## Existing substrate (do not duplicate)

What is already in place vs what this plan adds:

| Function | Component | Location | Status |
|---|---|---|---|
| Reef + food-attracted-hazard substrate (Phase 2 falsifier env) | SD-054 reef enrichment substrate | `ree-v3/ree_core/environment/causal_grid_world.py` | implemented; V3-EXQ-521 substrate-readiness PASS 7/7 |
| Multi-arm sweep template (V3-EXQ-522 reef vs heuristic) | Existing experiment scaffolding | `ree-v3/experiments/` | available; reuse pattern |
| SD-033a LateralPFCAnalog (rule_state buffer + bias head) | downstream consumer of ARC-062 discriminator | `ree-v3/ree_core/pfc/lateral_pfc_analog.py` | implemented 2026-04-20; bias head untrained -- the closure-plan GAP-1 |
| SalienceCoordinator + MECH-261 write-gate registry | mode-conditioning the discriminator output (hypothesis_tag generalisation) | `ree-v3/ree_core/cingulate/salience_coordinator.py` | implemented; write_gate("sd_033a") consumed by SD-033a |
| E3Selector | downstream consumer of score_bias from SD-033a | `ree-v3/ree_core/predictors/e3_selector.py` | implemented; `select(score_bias=...)` parameter wired |
| MECH-269 V_s monostrategy substrate | upstream representational precondition (regions must be discriminably represented before the discriminator can route) | `ree-v3/ree_core/hippocampal/`, `ree-v3/ree_core/regulators/vs_rollout_gate.py` | Phase 1 + Phase 2 (ii / iii) + Phase 3 staleness implemented |

What this plan adds:
- New `ree_core/policy/gated_policy.py` module: two scoring heads sharing E3 encoder features + small context discriminator.
- REEConfig flag `use_gated_policy` (default False, bit-identical OFF).
- Wiring from discriminator output into SD-033a `LateralPFCAnalog.update()` source vector (Phase 3).
- Trainable bias head with E3 optimiser inclusion (Phase 3).
- Validation EXQs at Phase 1 (substrate-readiness diagnostic) and Phase 2 (monomodal-collapse falsifier).

---

## Gap inventory

Seven gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-A** | ARC-062 substrate not implemented: no gated-policy module, no learned context discriminator, no `use_gated_policy` flag | load-bearing | All downstream gaps; the entire MECH-309 falsification chain |
| **GAP-B** | MECH-309 monomodal-collapse falsifier unrun on SD-054 (ARM_0 single-head E3 vs ARM_1 gated-heads with discriminator) | load-bearing | MECH-309 promotion candidate -> provisional; ARC-062 architectural validation; SD-029 measurement gate |
| **GAP-C** | ARC-062 discriminator output not routed to SD-033a `LateralPFCAnalog.update()` source vector. Without this routing, discriminator's training signal does not reach the rule_state EMA | high | SD-033a bias-head training (commitment_closure GAP-1); MECH-262 rule-selective persistence; SD-034 closure-mode-gating from a real rule_state |
| **GAP-D** | E3 optimiser does not include `lateral_pfc_analog.rule_bias_head.parameters()`. Bias head stays at frozen-zero (Go-side mechanically silent) until parameters are added to the optimiser | high | SD-033a behavioural validation; Go-side bias pathway |
| **GAP-E** | Multi-strategy scaling probe (>2 strategies in same env) unscoped. Distinguishes ARC-062 weak-reading sufficiency from ARC-063 strong-reading necessity per the Rigotti 2013 mixed-selectivity caveat (Pull A entry) | medium (V4 flag) | ARC-063 V4 implementation gate |
| **GAP-F** | Clinical / failure-mode tests (trauma-schema / paranoid-rule-field / depressive-rollout-constraint) -- ARC-063 falsifiable predictions (b). Cannot be implemented within ARC-062 alone per the cluster claim text | low (V4 deferred) | ARC-063 V4 |
| **GAP-G** | Sleep-vs-waking refinement asymmetry tests -- ARC-063 falsifiable predictions (c). Also placeholder for the Pull C lit-pull (sleep-vs-waking refinement) deferred from the Pull A / Pull B sequence | low (V4 deferred) | ARC-063 V4; cross-link to sleep_substrate GAP-1 |

---

## Sequenced plan

Six phases. Each phase is small and verifiable. Phases 1-3 are V3 in-scope;
Phase 4 surfaces V4 as load-bearing or not; Phase 5 is V4-deferred.

### Phase 1: ARC-062 substrate landing (GAP-A)

Smallest scope, highest leverage. Without the substrate the entire
falsification chain cannot run.

Deliverables:

1. **New module** `ree-v3/ree_core/policy/gated_policy.py` with `GatedPolicy`
   class. Two scoring heads sharing E3 encoder features (depending on R3
   instantiation choice -- see Open Questions); small context discriminator
   (~16-32 hidden units; sigmoid output over 2 heads). Symmetry-broken init
   so the heads can differentiate from step 0.
2. **Discriminator inputs** = multi-stream per Pull A R1 verdict:
   `(z_world, z_self, z_harm_a)`. Concatenated, projected through a small
   MLP, scalar-sigmoid output in [0, 1]. R1-reduced single-stream variants
   reserved for Pull A R1 falsifier ARM_1a/b/c (see Phase 2).
3. **REEConfig flag** `use_gated_policy` (default False, bit-identical OFF).
   Per-knob defaults: `gated_policy_n_heads = 2`, `gated_policy_disc_hidden = 24`,
   `gated_policy_disc_init_scale = 0.1` (small enough to avoid early
   discriminator over-commitment).
4. **Contract tests** in `ree-v3/tests/contracts/test_gated_policy.py`:
   C1 default-off no-op; C2 backward-compat with all existing experiments;
   C3 discriminator output in [0, 1]; C4 head differentiation under
   symmetry-broken init; C5 simulation-mode gating per MECH-094 (ghost /
   replay paths must not advance discriminator state).
5. **Substrate-readiness diagnostic EXQ** via `/queue-experiment` skill.
   Five sub-tests: (UC1) module instantiates and forward-passes; (UC2)
   master-OFF no-op (bit-identical to baseline E3); (UC3) discriminator
   output varies with `z_world` (input sensitivity); (UC4) head
   differentiation under training pressure; (UC5) MECH-094 simulation gate.

Phase 1 PASS = 5/5 sub-tests + 244+/244+ existing preflight + contracts.

### Phase 2: MECH-309 monomodal-collapse falsifier on SD-054 (GAP-B)

The architecturally load-bearing experiment. Tests the MECH-309 logical-
necessity claim and validates ARC-062's V3 weak-reading instantiation.

Deliverables:

1. **2-arm experiment** ARM_0 (single-head E3, baseline) vs ARM_1 (gated
   heads + discriminator on multi-stream input) on SD-054 reef +
   `hazard_food_attraction` substrate. Same env config, same seeds, same
   training budget; only manipulated variable is `use_gated_policy`.
2. **Hazard-density gradient sub-arms** ARM_1_low / ARM_1_med / ARM_1_high
   to test density-tracking acceptance criterion (Pull B verdict). Density
   levels chosen so ARM_1_med matches V3-EXQ-522 baseline.
3. **R1 input-ablation sub-arms** ARM_1a (`z_world` only), ARM_1b
   (`z_world + z_self`), ARM_1c (full three-stream). Per Pull A R1 verdict:
   ARM_1c expected to clear the falsifier most cleanly; ARM_1a may collapse
   to ARM_0 baseline. Single-arm Phase 2 first; multi-arm Phase 2b if
   single-arm passes.
4. **Pre-registered acceptance criteria** per Pull B R4 verdict (multi-
   signature tolerance window, PASS rule = at least 2 of 4 criteria hold
   with no contradictory signal):

   | Criterion | Test | Source |
   |---|---|---|
   | C1 density-tracking | monotone refuge-use response across hazard density (more hazards → more refuge-use, with chronic-high-risk reduction at high end) | Lima & Bednekoff 1999 |
   | C2 state-dependence | monotone refuge-use response across `drive_level` (underfed → less refuge-use, well-fed → more refuge-use) | Balaban-Feld 2019 |
   | C3 risk-type dissociation | distinct response to feeding-risk (food-attracted hazards in forage zone) vs transit-risk (transitions between reef and forage zone) | Eccard 2020 |
   | C4 cross-seed variation | non-zero coefficient of variation in `reef_visit_fraction` across seeds | Eccard 2020 + Crowell 2016 |

   FAIL signatures (any one is unambiguous): total invariance across all
   four criteria (the unambiguous monomodal-collapse signature MECH-309
   predicts); refuge-use monotonically *increases* with chronic high-risk
   regimes (biologically inverted -- naive "always-flee-when-hazard-present"
   policy rather than relative-risk-pattern-dependent policy).

5. **Falsification routing** from Phase 2 outcome:
   - PASS at option (iii) score_bias level → unblocks Phase 3 (close
     commitment_closure GAP-1).
   - FAIL at option (iii) → route discriminator output to option (i)
     BG-side score-aggregation first (cheaper retry per Gurney/Humphries/
     Redgrave 2015 anchor); then option (ii) trajectory-proposal-level
     hippocampal preplay seeding per Pfeiffer & Foster 2013 anchor; then
     ARC-063 V4 strong reading.
   - Partial PASS (1/4 criteria) → diagnostic via Sundell 2004 partial-
     replication framing; consider Pull A Capkova/Mansouri 2025 OFC /
     PS / ACC sub-function dissociation as next-thing-to-wire.

Phase 2 PASS gates Phase 3.

### Phase 3: Wire discriminator → SD-033a (closes commitment_closure GAP-1)

Completes the architectural loop: ARC-062 generates the rule signal,
SD-033a integrates it into a committed rule_state, the bias head emits
per-candidate score_bias, E3 selects under that bias.

Deliverables:

1. **Add `discriminator_proj` to `LateralPFCAnalog.update()` source vector**
   (GAP-C). Projection from discriminator output (or its pre-softmax logits,
   depending on dimensionality choice) into `rule_dim`. Source vector
   becomes `delta_proj(z_delta) + world_pool_weight * world_proj(z_world) +
   discriminator_pool_weight * discriminator_proj(disc_output)`.
2. **Make bias head trainable** (GAP-D). Add
   `lateral_pfc_analog.rule_bias_head.parameters()` to the E3 optimiser
   (or to a separate Adam at the same learning rate). Gradient flows from
   E3 score-aggregation through `score_bias` back to head weights via the
   existing E3 loss path -- no separate loss term needed.
3. **Default-flag flip** for rule-cue-tagged experiments: when
   `use_gated_policy=True`, also set `use_lateral_pfc_analog=True` by
   default. Other experiments unchanged.
4. **Validation EXQ for GAP-1**: 2-arm ablation (head trainable vs
   frozen-zero) on the ARC-062 + SD-054 stack. Pre-registered acceptance
   per the rewritten commitment_closure GAP-1 Phase 1 deliverable list:
   trainable arm shows non-zero `score_bias` after N episodes AND
   non-trivial reef/forage strategy split (cross-link to ARC-062's
   monomodal-collapse falsifier).

Phase 3 PASS = closes commitment_closure GAP-1 (status `blocked → done`).

### Phase 4: Multi-strategy scaling probe (GAP-E)

Tests ARC-062 weak-reading sufficiency at scale. Runs after Phase 3 PASS.

Deliverables:

1. **SD-054 extension to ≥3 strategies** (e.g., reef + forage + scout, or
   reef + forage A + forage B). Env-only extension; no agent code changes.
2. **3-arm experiment** ARM_0 single-head, ARM_1 ARC-062 weak-reading
   (2 heads), ARM_2 ARC-062 weak-reading (3+ heads). Acceptance per Pull A
   R2 verdict (Rigotti 2013 mixed-selectivity caveat): ARM_1 expected to
   start failing in the 3+ strategy regime; ARM_2 (more heads) may help
   but is engineering-only and does not address the high-dimensional
   mixed-selectivity gap. ARM_2 success surfaces ARC-062 as scalable;
   ARM_2 failure surfaces ARC-063 as load-bearing.

Phase 4 outcome: either confirms ARC-062 V3-sufficient (defer ARC-063 to
genuine V4 work) or surfaces ARC-063 as the next-thing-to-implement.

### Phase 5: V4 deferrals (GAP-F + GAP-G)

Genuinely V4-bound. Flag-only for now.

- **GAP-F clinical / failure-mode tests** (trauma-schema, paranoid-rule-
  field, depressive-rollout-constraint, OCD over-generation, attachment-
  mediated approach-avoid biasing). Per ARC-063 claim text: these "cannot
  be implemented within ARC-062 alone -- they need ARC-063's named
  CandidateRule structure for residue attribution." V4 implementation gate.
- **GAP-G sleep-vs-waking refinement asymmetry** (waking does substantial
  rule-update; sleep does compression / renormalisation / counterfactual
  recombination on top). Also serves as placeholder for **Pull C
  literature pull** (sleep-vs-waking refinement biology) which was
  deferred from the Pull A / Pull B sequence. Cross-link to
  [sleep_substrate_plan.md](./sleep_substrate_plan.md) GAP-1 (the parent
  sleep substrate plan).

### Phase 6: Cross-plan audit

After Phase 3 PASS, walk the apprehension → commitment → closure pipeline
end-to-end:

ARC-062 discriminator → SD-033a `rule_state` (gate-modulated EMA) →
`compute_bias` per-candidate → score_bias added to E3 candidate scores →
E3 selects under modified scoring → committed trajectory enters BetaGate
elevation → MECH-090 latch → execution → SD-034 closure operator on rule
completion → MECH-260 No-Go injection on completed rule → MECH-268 dACC
PE reset.

Deliverable: one integration smoke test in `ree-v3/tests/contracts/`
exercising the full path. Confirms wiring + cross-plan consistency.

---

## Status table

The resume primitive. Updated every session that touches this cluster.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-A | 1 | done | nothing | Substrate landed (ree_core/policy/gated_policy.py + use_gated_policy flag + REEAgent wiring + 5 contract tests + V3-EXQ-542 substrate-readiness diagnostic 5/5 PASS) | V3-EXQ-542 | 2026-07-31 (row reconcile; node record 2026-06-08) |
| GAP-B | 2 | in-progress | V3-EXQ-543k post-543i mode_separation_floor retest (priority 5); substrate landed 2026-05-21 | **UPDATE 2026-05-20:** Live retest is **V3-EXQ-543k** (supersedes 543i; adds mode_separation_floor + basin-stability gate). V3-EXQ-598 (GAP-1 bias-head ablation) queued at priority 4 -- runs after 543k. **PRIOR 2026-05-18 (governance: confirmed failure_autopsy_V3-EXQ-543h):** The whole 543f/543g/543h MECH-309/ARC-062 falsifier cluster is non_contributory, epistemic_category=substrate_ceiling -- GatedPolicy head-differentiation does not robustly persist under outcome-coupled REINFORCE (gated arms collapse to inert intermittently). Cross-machine proof: the identical 543g config was ACTIVE on host-A only and INERT on cloud-3 + cloud-4 (bit-identical to ARM_0), so 543g _144716Z 'weakens ARC-062' is a 1/3 minority-basin artifact -> 543g overall non_contributory and its supersession voided. 543h resolved to pre-registered grid branch (c) (no repro -> substrate/seed drift, non_contributory); the 543h INV-074/MECH-334 branch-(b) per_claim 'weakens' was corrected to non_contributory. All 7 cluster manifests marked evidence_direction=superseded by **V3-EXQ-543i**. claims.yaml ARC-062 / MECH-309 / INV-074 / MECH-334 carry evidence_quality_note + epistemic_category=substrate_ceiling + pending_retest_after_substrate; narrow_supports_flag set (ARC-062 / MECH-309 have ZERO reliable contributory trained-policy evidence -- voiding the cluster is NOT conflict resolution). Substrate fix landed: GatedPolicy differential-heads robustness fix (use_differential_heads; MECH-333 implementation_note; REE_assembly b99aefbe69). V3-EXQ-543i validates it (diff_on_escape=true confirms use_differential_heads resolves head-collapse) BUT diff_off_reproduced_collapse=false, so **V3-EXQ-543i is FLAGGED FOR /failure-autopsy** and carries no evidence_direction pending that post-mortem. substrate_queue ARC-062 entry updated with the autopsy failure_record. RESUME: GAP-B stays blocked until (1) the V3-EXQ-543i /failure-autopsy explains the diff-OFF non-reproduction, then (2) a contributory post-substrate (differential-heads) GAP-B retest of the MECH-309/ARC-062 falsifier. See decision-log 2026-05-18.<br><br>**PRIOR -- UPDATE 2026-05-17 (V3-EXQ-543g FAIL -> INV-074/MECH-334 crystallization; V3-EXQ-543h 2x2x2 queued):** V3-EXQ-543g (option-2 one-hot head input + outcome-coupled REINFORCE) ran to completion and registered **FAIL / weakens ARC-062**: ARM_2_gated_only=0.444 (best), ARM_3_both=0.243 (regresses BELOW gated-only), **D2 (ARM_3-ARM_2 >= +0.10) FAILED delta=-0.200**, D3 PASS delta=+0.069. The gating is NO LONGER inert (the 543f one-hot head-input fix cleared the 543b-e inert-gating bottleneck) -- the gate expresses itself but the **dACC training signal corrupts the established gated-policy discrimination via shared-return gradient flow** (heterosynaptic-depression analog, O'Dell 2025): the gated policy is never crystallized before dACC's perturbation is introduced. This is the experimental signature of the missing **critical-period closure mechanism (MECH-334)**. The INV-074/MECH-333/MECH-334/ARC-075/Q-052 cluster (registered 2026-05-17, commit 3bd35da308) was registered for exactly this. Routing: **(1) /implement-substrate** landed the Phase-3 plasticity-injection crystallization hook -- `GatedPolicy.crystallize()` freezes head_0/head_1/discriminator and adds a zero-init plastic expansion MLP (Nikishin 2023; forward = frozen_gated(x) + expansion(x.detach())); `ResidueField.snapshot_ewc_anchor()` + `ewc_penalty()` Fisher-weighted write-protect (Kirkpatrick 2017, established-basin Fisher proxy); `InfantCurriculumScheduler(on_phase3_entry=...)` fire-once hook; all behind `REEConfig.crystallize_at_phase3` (default OFF, bit-identical; 484/484 contracts PASS; backward-compat 543g dry-run reproduced the prior signature exactly). ree-v3 f8b93e3, REE_assembly f71b6a7da0 (claims.yaml implementation_note + docs/architecture/critical_period_crystallization.md). **(2) /queue-experiment** queued **V3-EXQ-543h** (ree-v3 ab2dd30): 2x2x2 (use_gated_policy x use_dacc x crystallize_at_phase3), 8 arms x 3 seeds, `supersedes V3-EXQ-543g`. xtal-OFF arms reproduce 543g bit-identically (dry-run verified ARM_0=0.278/ARM_1=0.174/ARM_2=0.444/ARM_3=0.243); xtal-ON arms fire the closure at the P1 open-window-closes boundary (CRYSTALLIZE_P1_OPEN_FRACTION=0.5), rebuild the REINFORCE optimizer to `gated_policy.expansion_parameters()` only (frozen heads protected), add `residue.ewc_penalty()` (lambda=0.1) to the P1 loss. **F-ERROR-DEPENDENCE PRE-CHECK (Pathak 2017 ICM self-defeat; reported per task):** MECH-314b (uncertainty, reads e3._running_variance) and MECH-314c (learning-progress, EMA of |PE_t-PE_{t-K}| fed e3._running_variance) are forward-model-error-dependent -- 314c is the canonical ICM self-defeat case -- and decay to ~0 before Phase-3 crystallization fires, so they cannot establish competitive weight on the expansion layer; MECH-313 (constant temperature), MECH-314a (residue-RBF novelty, Wittmann 2008 RPE-independent), MECH-320-primary (avg-reward-rate EWMA, Niv 2007) and dACC/MECH-260 (state-dependent recency) are F-robust. **Arm adjustment:** 543h holds MECH-314 in novelty-only config (314a ON, 314b/314c OFF) on the xtal arms so the test is not diluted by a confounded null channel; dACC (the 543g corrupting signal) is NOT F-error-dependent so the crystallization hypothesis is cleanly testable. **SCHEDULER-GATE ADAPTATION:** the closure is the IDENTICAL callable the production InfantCurriculumScheduler.on_phase3_entry invokes; its hard ep-min gate (PHASE_EP_MIN[3]=2000) is incompatible with the ~108-episode falsifier, so 543h instantiates the scheduler (validates the wiring contract) but fires the same closure at the falsifier's open-window-closes boundary. PRIMARY **D2_xtal = ARM_7_both_xtal - ARM_6_gated_only_xtal >= +0.10** (crystallization rescues the 543g D2 FAIL); SECONDARY **repro = ARM_2 > ARM_3**; PASS = D2_xtal AND repro AND not xtal_harms_gated_only. Pre-registered interpretation grid (recorded in metrics.acceptance.interpretation_branch): (a) D2_xtal PASS + repro -> crystallization rescues gradient interference, Q-052 -> (B) structural, **close GAP-B + unblock GAP-C/D**; (b) D2_xtal FAIL + repro -> defect isolated to dACC's own architecture (narrower diagnostic), GAP-B stays in-progress, route to dACC-architecture review; (c) no repro -> substrate/seed drift, non_contributory; (d) xtal degrades gated-only -> plasticity injection harmful, /diagnose-errors. claim_ids [ARC-062, MECH-309, INV-074, MECH-334]; evidence_direction_per_claim emitted. **NOTE: V3-EXQ-543g still queued as 'claimed' -- NOT mutated (scope/concurrency); flagged to user for governance/runner reconciliation.** GAP-C/GAP-D substrate already pre-positioned (2026-05-17); their validation EXQs remain deferred until a contributory 543h result. See decision-log 2026-05-17.<br><br>**PRIOR -- UPDATE 2026-05-17 (V3-EXQ-543e FAIL diagnosed -> option 2):** V3-EXQ-543e ran to completion 2026-05-17T01:02Z (real run, exit ok, ~79 min) and registered **FAIL non_contributory {ARC-062: weakens, MECH-309: non_contributory}** -- same inert-gating signature as 543b/c/d (probe-gate FAIL all 3 gated-arm seeds; reef_fraction ARM_0=ARM_1=0.6918, ARM_2=ARM_3=0.5600; D1=D2=0.0, D3=-0.13). A /diagnose-errors root-cause (`failure_autopsy_EXQ-543e_2026-05-17.{md,json}`) ran a direct harness replicating 543e's exact ARM_2 P0 path and discriminated the three hypotheses: **H1 FALSE** (candidates have 4.95 unique first-action classes / entropy 1.26; `support_preserving_active=0` is the expected stratified-elites signature per V3-EXQ-567 -- SP-CEM IS engaging); **H2 FALSE** (world_states[0] pairwise L2=0.0 confirms the world_states[1] fix is in place; world_states[1] L2~0.013, ~1000x larger than 543b's 1e-5 -- probe features non-degenerate); **H3 CONFIRMED** (the ~5 first-action classes are compressed by E2 world-forward to only **0.22%** of the z_world signal magnitude before reaching the z_world-only ARC-062 head). This is the FIRST 543-lineage run with the 2026-05-11 candidate-distinguishability confound **provably absent**, so the persistent inert-gating cleanly isolates the **ARC-062 head input contract** as the bottleneck -- substrate is sound but under-fed. The `non_contributory` direction is left as-is and **NOT force-mapped**; contributory weight is captured by the autopsy + this routing. **Routing: pre-registered option 2** -- /implement-substrate to augment the GatedPolicy head input with the first-action one-hot, then re-issue as **V3-EXQ-543f** via /queue-experiment (543d 2x2 factorial + SP-CEM substrate unchanged; only the head input contract changes; supersedes V3-EXQ-543e). ARC-062 substrate-rationale retirement NOT recommended (under-fed, not redundant). GAP-C/GAP-D stay open, sequenced after a contributory falsifier PASS. See decision-log 2026-05-17. Handoff: V3-EXQ-543e is a completed FAIL now diagnosed -- flag for next governance pass to add run_id to reviewed_run_ids.<br><br>**PRIOR 2026-05-16 (falsifier re-issued on SP-CEM):** GAP-B open -> in-progress. The MECH-309 monomodal-collapse falsifier was re-issued as **V3-EXQ-543e** via /queue-experiment and is now running. 543e = the canonical 543d 2x2 factorial (ARM_0 gated/dacc OFF, ARM_1 dacc-only, ARM_2 gated-only, ARM_3 both; pre-registered D1-D4; PASS=D2 AND D3; claim_ids [ARC-062, MECH-309]; per-claim direction grid) with the ONLY change being all 4 arms now build the agent with support-preserving CEM (use_support_preserving_cem=True + support_preserving_stratified_elites=True + support_preserving_ao_std_floor=0.2 + support_preserving_min_first_action_classes=2 -- the exact config V3-EXQ-567 validated PASS for ARC-065). supersedes V3-EXQ-543d. Local smoke dry-run PASS (12 verdict lines, 36 progress lines, SP-CEM flags verified reaching config.hippocampal in all 4 arms, runner-conformance validated). The 543b/c/d evidence stays non_contributory/weakens (ran on the invalidated collapsed CEM) and is NOT force-mapped -- 543e is the FIRST contributory test of MECH-309. On completion: route per the pre-registered D-grid (PASS D2 AND D3 -> close GAP-B + unblock GAP-C/D; FAIL D1-only -> ARC-062 substrate-rationale review; FAIL all-D-null -> option 2 head-input augmentation). See decision-log 2026-05-16 (V3-EXQ-543e queued).<br><br>**PRIOR 2026-05-16 (closure-map reconciliation):** GAP-B blocked -> open. V3-EXQ-567 PASS (evidence_direction=supports, ARC-065) lifts natural selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 -- the candidate-feature variance the 2026-05-11 gate required. Next action: re-issue the MECH-309 monomodal-collapse falsifier on the SP-CEM substrate via /queue-experiment. The 543b/c/d non_contributory/superseded evidence was run under the OLD collapsed CEM and is not force-mapped. See decision-log 2026-05-16.<br><br>**UPDATE 2026-05-11 (EXQ-543c review):** V3-EXQ-543c ran 19:02Z and registered FAIL `non_contributory` for both ARC-062 + MECH-309 -- probe_gate_arm_failed on all 3 ARM_1c seeds (n_inert_gating_seeds_arm1c=3); per-seed metrics floating-point-identical between ARM_0 and ARM_1c across reef_fraction / rho / forage_hazard / transit_hazard / risk_type_ratio. 543c is a strict replication of 543b's inert-gating signature on SD-054 bipartite even with the world_states[1] Cause-1 fix applied. V3-EXQ-543d (2x2 factorial of use_gated_policy x use_dacc with MECH-260 anti-recency=0.5; supersedes 543c) is already queued and running -- its outcome supersedes 543c interpretation per its pre-registered D1-D4 grid. See decision-log 2026-05-11 (EXQ-543c) entry for the full routing logic.<br><br>**PRIOR 2026-05-11**: V3-EXQ-543b ran 2026-05-10 and registered `non_contributory` with `inert_gating_detected` on all 3 seeds; mean_tv_distance = max = min = 0.0 exact across 3 seeds x 12 windows x 32 probe states. Diagnose-errors session 2026-05-11T06:35Z--06:44Z surfaced two distinct causes: (1) script-level bug -- candidate_features = world_states[0] = initial_z_world (identical across K candidates by E2FastPredictor convention); (2) substrate-level finding -- even with the bug fixed (world_states[0] -> world_states[1]), CEM proposer at init produces 8 candidates with shared argmax-first-action, continuous-action vectors differing only ~1e-4, post-action world_states diverging only ~1e-5; ARC-062 head consumes z_world-only inputs that are structurally near-indistinguishable. Status `in-progress -> blocked` pending CEM-candidate-distinguishability substrate-readiness diagnostic that characterises first-action entropy, continuous-action L2 spread, and world_states-1 pairwise distance at init and during P0/P1 training. Three architectural options surfaced for downstream resolution (see decision-log 2026-05-11 for the full rationale): (1) land Cause-1 microscopic fix and rerun; (2) augment GatedPolicy head input with first-action (substrate change to ARC-062 contract; belongs under /implement-substrate); (3) **env-side diversification** -- design SD-054 (or successor) so the signals ARC-062 needs are structurally guaranteed-present per candidate by construction (user-direction, 2026-05-11). unblocks_claims tightened to [MECH-309, ARC-062]; SD-029 dropped per claim_ids accuracy rule (SD-054 is not SD-029's measurement substrate). | V3-EXQ-543k | 2026-08-10 (row reconcile; node record 2026-08-01) |
| GAP-C | 3 | done | V3-EXQ-543k contributory PASS (GAP-B) for evidence closure | Substrate DONE. Validation V3-EXQ-598 queued (same 2-arm ablation closes GAP-C+D and commitment_closure:GAP-1). | V3-EXQ-598 | 2026-07-31 (row reconcile; node record 2026-05-27) |
| GAP-D | 3 | done | nothing | **ROW RECONCILED 2026-07-29 (docs-only) to the node record `governance_2026_05_29`: this row said `in-progress` / "598 queued" while the node has been `done` since 2026-05-29.** RESOLVED at the substrate-wiring level: **V3-EXQ-598b ran 20260527T120345Z** and confirmed C1 frozen_silent PASS + C2 trainable_nonzero PASS (rule_bias_head learned mean abs 0.05-0.10 when trainable, 0.0 when frozen) — i.e. the E3 optimiser DOES include `lateral_pfc_analog.rule_bias_head.parameters()` under MECH-262's training regime. The predecessor **V3-EXQ-598 also ran** (FAIL / non_contributory) and is reviewed; its downstream C3 monomodal-rescue failure is a separate substrate_ceiling finding tracked under GAP-B, not a GAP-D wiring defect. | V3-EXQ-598b (resolved); V3-EXQ-598 (ran FAIL/NC, reviewed) | 2026-07-29 (row reconcile; node record 2026-05-29) |
| GAP-E | 4 | deferred | GAP-D PASS | Extend SD-054 to ≥3 strategies; 3-arm scaling experiment | n/a in V3 | 2026-05-09 |
| GAP-F | 5 | deferred V4 | GAP-E outcome | none in V3 | n/a | 2026-05-09 |
| GAP-G | 5 | deferred V4 | sleep_substrate plan progression | Pull C lit-pull (sleep-vs-waking refinement biology) when ARC-063 V4 work opens | n/a | 2026-05-09 |
| GAP-H | 2-3 | partial | the remaining Q-045 / MECH-313 / MECH-260 survival + noise-floor leg (held until V3-EXQ-603i lands) and the GAP-B successor. **NOT** on 603 — see reconcile | **ROW RECONCILED 2026-07-29 (docs-only): the "Blocking on" cell said "V3-EXQ-603 re-queued; awaiting runner", frozen at 2026-05-21. V3-EXQ-603 RAN THAT SAME DAY (FAIL / non_contributory, reviewed), and all five owner-EXQs on this row have run — 544, 545, 604, 605, 603.** Node record has advanced eight times since (latest `governance_2026_07_20`). Current state: the **Q-044 / MECH-314-family leg is SATISFIED** by V3-EXQ-604c PASS on the validated GAP-A stack (2026-06-08) — do not queue another GAP-H curiosity retest for that leg — though the confirmed `failure_autopsy_V3-EXQ-604c_2026-07-20` subsequently demoted the Q-044 / MECH-314b / MECH-314c family to non_contributory / substrate_ceiling. The node stays `partial` (not done) because the **Q-045 / MECH-313 / MECH-260 leg** is held pending `behavioral_diversity_isolation:GAP-C` / V3-EXQ-603i, and rule-apprehension closure is held on the GAP-B successor. The intervening V3-EXQ-687 (queued 2026-06-17) also RAN terminal FAIL / non_contributory 2026-06-18 and was autopsied + reviewed. **Prior row text (2026-05-21, retained for reconstruction):** ARC-065 diversity-generation cluster registered. **MECH-313 substrate landed 2026-05-10** (`ree_core/policy/noise_floor.py` + `REEConfig.use_noise_floor`/`noise_floor_alpha`/`noise_floor_min_temperature` + `select_action` e3.select call site + 11 contract tests + V3-EXQ-544 substrate-readiness diagnostic 5/5 PASS + design doc + claims.yaml status `candidate -> candidate_substrate_landed`). **MECH-314 / MECH-314a/b/c substrate landed 2026-05-10** (`ree_core/policy/structured_curiosity.py` + `StructuredCuriosity` + `StructuredCuriosityConfig` + `REEConfig.use_structured_curiosity` master + 3 independently-togglable sub-flavour switches (`use_curiosity_novelty`/`_uncertainty`/`_learning_progress`) + per-sub-flavour weights + `select_action` `dacc_score_bias` composition site between MECH-295 and MECH-313 + 13 contract tests + V3-EXQ-545 substrate-readiness diagnostic 5/5 PASS smoke + design doc + claims.yaml status `candidate -> candidate_substrate_landed` for parent + 3 children). **2026-05-21 IGW-003:** V3-EXQ-604 (Q-044) + V3-EXQ-605 (Q-043) ran FAIL `non_contributory` (all arms identical entropy ~0.24-0.31 under SP-CEM+reef -- substrate_ceiling, reviewed 2026-05-21). V3-EXQ-603 (Q-045 4-arm) pruned from queue without run; **re-queued 2026-05-21T13:36Z** (dry-run OK). GAP-H closes to `done` when 603 manifest lands. | V3-EXQ-544 + V3-EXQ-545 (ran, substrate-readiness diagnostics); V3-EXQ-604 + V3-EXQ-605 (ran FAIL/NC, reviewed); **V3-EXQ-603 (RAN 2026-05-21, FAIL/non_contributory, reviewed — the manifest this row was waiting on DID land, and it did not close the node)**; V3-EXQ-604c (PASS, Q-044 leg, later demoted by its 2026-07-20 autopsy); V3-EXQ-687 (ran FAIL/NC 2026-06-18, autopsied) | 2026-07-29 (row reconcile; node record 2026-07-20) |
| GAP-I | 2-3 | blocked_pending_substrate | `arc_062_rule_apprehension:GAP-B` (rule-creator / discriminator substrate populating DIFFERENTIATED rule_state into SD-033a; `scaffolded_sd054_onboarding` is the candidate vehicle) | **ROW RECONCILED 2026-07-29 (docs-only): status was `partial`, node record has been `blocked_pending_substrate` since 2026-06-23, and the row did not reflect the 2026-06-23 SPLIT.** The node was split — MECH-316 / MECH-317 (absorption checks that remain doc-only, no V3 modules) moved out to the child node **`arc_062_rule_apprehension:GAP-I-`** (status `deferred`; see new row below), leaving GAP-I holding only the MECH-318 empirical retire-vs-promote gate, which per claims.yaml is deferred to "ARC-062 Phase 2 GAP-B PASS + Phase 3 GAP-C closure" and so cannot run before GAP-B resolves. **Owner note:** the row's "V3-EXQ-543c-successor" descriptor is misleading read literally — that successor was minted and RAN (V3-EXQ-628, PASS/supports 2026-06-02, folded into governance; see GAP-K), but it discharged the MECH-319 replay/write-gate slice only, NOT GAP-I's multi-rule-context retire-vs-promote gate. Owner stays genuinely unassigned: no id can be allocated until GAP-B lands the substrate. **Prior row text (2026-05-10, retained for reconstruction):** ARC-064 bottom-up rule-discovery cluster registered (ARC-064 anchor + MECH-316 cross-episode regularities + MECH-317 behavioural pattern compression + MECH-318 rule-state abstraction provisional). MECH-315 absorbed into MECH-292/293 ghost-goal substrate per Pull 2 R5. **MECH-318 absorption check done 2026-05-10**: VERDICT (B) PARTIALLY ABSORBED (`REE_assembly/docs/architecture/mech_318_absorption_check.md`). Within-V3 functional weight borne by SD-033a LateralPFCAnalog rule_state + ARC-062 Phase 1 gated_policy discriminator + ARC-062 Phase 3 GAP-C planned wiring. W2 (multi-task training) + W5 (cross-episode continuity) gaps remain; W2 blocked on multi-rule-context substrate, W5 likely V4-scope. NO new V3 substrate commissioned. claims.yaml MECH-318 evidence_quality_note + notes updated; status retained `candidate` pending V3-EXQ-543c-successor empirical gate. MECH-316 / MECH-317 absorption checks separately scoped. V3 falsification path: substrate-design EXQ deferred (requires multi-rule-context substrate beyond SD-054 alone). | none assignable — gated on GAP-B substrate landing (NOT "TBD pending someone's attention"; there is no id to mint yet) | 2026-07-29 (row reconcile; node record 2026-06-23) |
| GAP-I-absorption | 2-3 | blocked_pending_substrate | `arc_062_rule_apprehension:GAP-I` | **ROW RECONCILED 2026-08-18 (docs-only): status was `deferred`; the 2026-08-18 /governance cycle (GFLAG-0041, session governance-paused-bb6e76) ACCEPTED the 2026-08-15 D-002 adjudication proposed below and flipped the node `deferred -> blocked_pending_substrate` -- this row now matches.** **NEW ROW 2026-07-29 — this child node has existed in the frontmatter since the 2026-06-23 split but was never added to this table.** ARC-064 absorption checks for MECH-316 (cross-episode regularities) + MECH-317 (behavioural-pattern compression). Split out of GAP-I because it sits at a radically different readiness level: these are **doc-only absorption checks with no V3 modules**, whereas GAP-I retains the MECH-318 empirical retire-vs-promote gate. Deferred, not blocked — nothing is waiting on a runner. **ADJUDICATED 2026-08-15 (D-002 orphan-V3-claim, P0/strong): the `deferred` status is NOT justified — 4 of 5 artefacts call MECH-316/317 live V3 (claims.yaml `v3_pending: true`; two `candidate_v3_pending` substrate_queue entries; the MECH-318 absorption memo calling the sibling checks "still-open"; parent GAP-I `blocked_pending_substrate` on the same blocker). "Doc-only" means cheap and buildable, not out-of-V3-scope — and `deferred` excludes the node from the V3 denominator entirely. Status change PROPOSED to /governance (→ `blocked_pending_substrate`); **ACCEPTED 2026-08-18** (see the node's `governance_2026_08_18` note). See the node's `governance_2026_08_15` note for the full artefact table, the half-applied-reclassification mechanism, and the measured closure delta.** | n/a (doc-only) | 2026-08-18 (row reconcile; node record 2026-08-18) |
| GAP-J | 2-3 | blocked | claims-only registration; **blocked on GAP-B** (additive-logit comparison requires non-inert gating) — status corrected 2026-07-29 from `open` to match the node record (`blocked` since 2026-05-17); the "Blocking on" text was already right | MECH-312 parent + MECH-312a/b/c/d sub-MECHs registered (uncertainty / practice-maturity / affective-stream-modulation / V_s-freshness-modulation). MECH-312e controllability/agency deferred per Pull 3 R5 (substrate not available). Multiplicative-gate combination rule registered as architectural default; additive-logit baseline needs a 543g-successor arm (V3-EXQ-543b/c listed as owner is stale -- all non_contributory due to inert-gating, not a multiplicative-vs-additive comparison). depends_on updated to [GAP-B] 2026-05-17. **Owner note (2026-07-29):** "TBD (543g-successor)" is CORRECT and should not be resolved to an id — the 543 lineage did continue (543h/543i/543j/543k/543l all ran), but none of them is the additive-logit-vs-multiplicative-gate comparison this node needs; that arm has never been authored, and it cannot be until GAP-B delivers non-inert gating. | none assignable — gated on GAP-B (the additive-logit baseline arm has never been authored) | 2026-07-29 (row reconcile; node record 2026-05-17) |
| GAP-K | 2-3 | in-progress | sibling nodes GAP-B (in-progress), GAP-H (partial) and GAP-I (blocked_pending_substrate). **NOT** the 543c-successor — that landed; see reconcile | MECH-319 simulation-mode rule-write-gating substrate registered as REE-novel substrate-level instantiation of MECH-094 at the arbitration layer. SWR machinery + reverse-replay are the substrate anchors; the categorical write-gate function is REE-novel. **MECH-319 substrate landed 2026-05-10** (`ree_core/regulators/simulation_mode_rule_gate.py` + `SimulationModeRuleGate` + `SimulationModeRuleGateConfig` + `REEConfig.use_simulation_mode_rule_gate` master + `simulation_mode_rule_gate_admit_writes` V3-EXQ-543c falsifier inverse-debug flag + `select_action` GatedPolicy + LateralPFCAnalog call-site wiring + 15 contract tests + V3-EXQ-546 substrate-readiness diagnostic 6/6 PASS smoke + design doc + claims.yaml status `candidate -> candidate_substrate_landed`). MECH-094 NOT modified per Pull 3 R1 + Pull 4 R3 KEEP-AS-IS verdicts. V3 falsification path: artificial-write-channel-routing config flag in V3-EXQ-543c-successor (paired arm: `admit_writes=False` MECH-319 normal vs `admit_writes=True` falsifier with replay-driven invocation; predicted monomodal-collapse re-emergence under the falsifier arm). **2026-06-06 governance fold: V3-EXQ-628 LANDED PASS (supports MECH-319)** -- the deferred V3-EXQ-543c-successor replay/caller_sim falsifier ran on ree-cloud-2 (2026-06-02, 3/3 seeds): BLOCK suppresses the simulation rule_state write, ADMIT (admit_writes=True) admits it (mean replay delta ~0.31), arms diverge, waking path bit-identical (C4). First evidence-grade confirmation for MECH-319; folded into claims.yaml + indexer (canonical runs/ pack reconstructed from the cloud-2 flat manifest, which never synced its pack -> the PASS had been unscored since 2026-06-02). MECH-319 STAYS candidate_substrate_landed (no promotion: 1 entry < min_experimental_entries=2; v3_pending held). **PARTIAL ADVANCE ONLY** -- GAP-K stays in-progress; its depends_on GAP-B / GAP-H / GAP-I remain substrate-blocked. **"Blocking on" cell reconciled 2026-07-29 (docs-only):** it named "V3-EXQ-543c-successor ... AFTER MECH-313 / MECH-314 / MECH-318 sibling substrates land", but that successor **is** V3-EXQ-628 and it LANDED PASS 2026-06-02 — the row's own body already recorded this and the cell was never updated to match. Per `resume_condition` (2026-06-08): 628 has satisfied the MECH-319 replay / write-gate evidence slice, **do not re-queue it**; closure now waits purely on the sibling nodes. Both owner-EXQs on this row have run (546 diagnostic, 628 evidence). | V3-EXQ-546 (ran, diagnostic, 6/6 PASS smoke) / V3-EXQ-628 (ran, evidence, PASS/supports, replay/caller_sim falsifier, 2026-06-02) | 2026-07-29 (row reconcile; node record 2026-06-19) |
| GAP-L | 3-4 | done (lit gate); substrate gate still OPEN | Gate (1) caregiver-scaffolding / cued-recall biology lit-pull = DISCHARGED 2026-05-18. Gate (2) caregiver/teacher-agent substrate STILL DOES NOT EXIST in V3 (single-agent) -- independently open, NOT discharged by this work | 2026-05-18 bring-forward: ARC-063 promoted V4 -> V3; socially-scaffolded rule-population pathway registered as structural slots (**ARC-077** parent + **MECH-337** "in" + **MECH-338** "select"); claims 645 -> 648; lit_conf=0 at registration. **2026-05-18 GAP-L lit-pull DISCHARGED** (session gap-l-litpull-socially-scaffolded): 8 entries in evidence/literature/targeted_review_socially_scaffolded_rule_population (Csibra & Gergely 2009; Wood/Bruner/Ross 1976 + Vygotsky ZPD; Tomasello et al. 2005; Tulving & Thomson 1973; Godden & Baddeley 1975 [+2021 failed-replication caveat]; Nakazawa et al. 2002 CA3 pattern-completion; counterweights Heyes 2016 + Spelke & Kinzler 2007). lit_conf set as PARALLEL signal: ARC-077=0.74 / MECH-337=0.78 / MECH-338=0.75 (indexer parallel 0.868/0.878/0.813). Claims REMAIN candidate (lit != exp; exp_conf=0). NO ARC-062 posture change (GAP-B stays blocked, owned by V3-EXQ-543i/543j). | lit-pull (GAP-L litpull session 2026-05-18) | 2026-05-18 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `partial`,
`done`, `deferred`, `registered`. `registered` = claims registered in
claims.yaml; substrate / experiments not yet built. A `paused` row
carries a resume condition in the [Decision log](#decision-log).

---

## Open questions (resolved defaults)

All four open questions sketched at plan-doc registration have biology-
anchored defaults from Pull A and Pull B. Defaults can be revisited if
Phase 1 / Phase 2 evidence motivates a change.

### R1 — Discriminator input streams

**Default: multi-stream `(z_world, z_self, z_harm_a)`.** Single-stream
`z_world`-only is the impoverished case and is reserved for the Phase 2
input-ablation sub-arm.

**Justification (Pull A SYNTHESIS verdict 1):**
- Miller & Cohen 2001 *Annu Rev Neurosci* ([DOI 10.1146/annurev.neuro.24.1.167](https://doi.org/10.1146/annurev.neuro.24.1.167)) — explicit "inputs, internal states, and outputs" framing.
- Rigotti et al. 2013 *Nature* ([DOI 10.1038/nature12160](https://doi.org/10.1038/nature12160)) — single-cell mixed selectivity to multiple task variables.
- Mitchell et al. 2016 *J Neurosci* ([DOI 10.1523/JNEUROSCI.0810-16.2016](https://doi.org/10.1523/JNEUROSCI.0810-16.2016)) — macaque MD network includes insular (interoceptive) cluster as first-class member.

**Falsifier path:** Phase 2 ARM_1a / b / c sub-arms test whether the
multi-stream default is necessary or whether single-stream suffices on
SD-054. PASS at ARM_1a alone would weaken the multi-stream commitment
for V3 scope (engineering-overhead-without-benefit).

### R2 — Discrete heads vs continuous gating

**Default: N=2 heads at Phase 1.** Substrate-constrained: SD-054 reef-vs-
forage is a 2-mode partition by experimental construction, so 2 heads is
the right Phase 1 commitment regardless of biology.

**Caveat (Pull A SYNTHESIS verdict 3):** Rigotti et al. 2013's mixed-
selectivity finding argues PFC's biological mechanism is high-dimensional
continuous mixed selectivity, not discrete head selection. ARC-062's
two-head architecture is a low-dimensional approximation suitable for
SD-054 but expected to break at multi-strategy scaling (Phase 4 / GAP-E).

**Falsifier path:** Phase 4 / GAP-E multi-strategy scaling probe is the
test. ARM_1 (2 heads) failing on a 3+ strategy substrate routes the
diagnosis toward ARC-063 V4 strong reading (distributed CandidateRule
field with continuous tolerance gates).

### R3 — Gating site

**Default: Phase-1 commitment to score_bias level (option iii, current
SD-033a substrate).** Engineering reasons dominate: SD-033a is wired,
`rule_state` buffer exists, gradient path through E3 score-aggregation
is clean.

**Justification (Pull A SYNTHESIS verdict 2):** All three sites are
biologically real; the architectural commitment is a routing choice.
- Option (i) BG-side score-aggregation: Gurney/Humphries/Redgrave 2015 *PLoS Biology* ([DOI 10.1371/journal.pbio.1002034](https://doi.org/10.1371/journal.pbio.1002034)) — cortico-striatal action-reinforcement interface.
- Option (ii) trajectory-proposal hippocampal preplay: Pfeiffer & Foster 2013 *Nature* ([DOI 10.1038/nature12112](https://doi.org/10.1038/nature12112)) — goal-biased forward sequence in rat CA1.
- Option (iii) PFC top-down score_bias: Miller & Cohen 2001; Bongard & Nieder 2010 *PNAS* ([DOI 10.1073/pnas.0909180107](https://doi.org/10.1073/pnas.0909180107)) — PFC rule-coding units controlling information flow.

**Falsification chain:** PASS at option (iii) → close commitment_closure
GAP-1; FAIL at option (iii) → route discriminator to (i) BG-side first
(cheaper retry), then (ii) trajectory-proposal-level, then ARC-063 V4
strong reading.

### R4 — Phase 2 acceptance threshold tolerance window

**Default: multi-signature tolerance window with 4 acceptance criteria,
PASS rule = at least 2 of 4 hold across seeds with no contradictory
signal.** Specific criteria captured in the Phase 2 deliverable table
above (C1 density-tracking, C2 state-dependence, C3 risk-type
dissociation, C4 cross-seed variation).

**Justification (Pull B SYNTHESIS R4 verdict):**
- Lima & Bednekoff 1999 *Am Nat* ([DOI 10.1086/303202](https://doi.org/10.1086/303202)) — canonical theory: allocation tracks temporal risk pattern; chronic-high-risk reduces refuge-use (counterintuitive prediction distinguishing rule-following from naive policy).
- Beauchamp & Ruxton 2010 *Am Nat* ([DOI 10.1086/657437](https://doi.org/10.1086/657437)) — theoretical reassessment: even canonical theory has caveats; field has retained spirit while weakening specifics.
- Sundell et al. 2004 *Oecologia* ([DOI 10.1007/s00442-004-1490-x](https://doi.org/10.1007/s00442-004-1490-x)) — vole field test: 1/5 predictions replicated; partial-replication is the realistic empirical baseline.
- Balaban-Feld et al. 2019 *Oecologia* ([DOI 10.1007/s00442-019-04395-z](https://doi.org/10.1007/s00442-019-04395-z)) — direct fish-refuge state-dependent allocation (highest mapping fidelity to SD-054).
- Eccard et al. 2020 *Oecologia* ([DOI 10.1007/s00442-020-04773-y](https://doi.org/10.1007/s00442-020-04773-y)) — individual variation + risk-type dissociation in voles.
- Crowell et al. 2016 *Ecol Evol* ([DOI 10.1002/ece3.1940](https://doi.org/10.1002/ece3.1940)) — refuge-distance gradient + species variation.

**Sharper FAIL signatures** (any one is unambiguous):
- Total invariance across all four criteria — the unambiguous monomodal-
  collapse signature MECH-309 predicts.
- Refuge-use *increases* monotonically with chronic high-risk regimes —
  biologically inverted; naive "always-flee-when-hazard-present" policy.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-07-29 - Status-table reconcile: five rows were reporting completed work as outstanding; GAP-I- added; no status invented

**Docs-only. No experiments queued, no claims.yaml edit, no manifest touched.**
This plan had logged no decision since 2026-05-18 (72 days) while its node
frontmatter kept advancing, so the markdown Status table had drifted badly out
of step with the records governance actually maintains.

Root pattern, and the reason this is a recurring defect rather than a one-off:
**the YAML `closure_plan` frontmatter is kept current by every governance cycle
(each writes a `governance_<date>` key and bumps `last_updated`), but the
markdown Status table is a hand-maintained duplicate of the same state with no
such ritual.** So the table silently becomes the stalest description of the
work while remaining the thing labelled "the resume primitive" -- which is
exactly what a cold-start session reads first. Every correction below was taken
FROM the node record or from verified run evidence; nothing was re-adjudicated.

Reconciled:

- **GAP-D** `in-progress` -> `done`. The node has been `done` since 2026-05-29
  (`governance_2026_05_29`): V3-EXQ-598b ran 20260527T120345Z and confirmed the
  E3 optimiser does include `rule_bias_head.parameters()` (C1 frozen_silent
  PASS + C2 trainable_nonzero PASS). The row still said "Validation V3-EXQ-598
  queued"; 598 has also run (FAIL / non_contributory, reviewed).
- **GAP-H** "Blocking on: V3-EXQ-603 re-queued; awaiting runner" -> the real
  remaining legs. **V3-EXQ-603 ran on 2026-05-21, the same day the row was
  written** (FAIL / non_contributory, reviewed). All five owner-EXQs on the row
  (544, 545, 604, 605, 603) have run. Node stays `partial`, correctly: the
  Q-044/MECH-314 leg is satisfied by 604c (later demoted by
  `failure_autopsy_V3-EXQ-604c_2026-07-20`), while the Q-045/MECH-313/MECH-260
  leg is held on V3-EXQ-603i and closure on the GAP-B successor.
- **GAP-I** `partial` -> `blocked_pending_substrate`, and the **2026-06-23 SPLIT
  was never reflected in the table at all** -- MECH-316/317 moved to a child
  node `GAP-I-`, which existed in frontmatter but had no row. Added one.
- **GAP-J** `open` -> `blocked` (node record, 2026-05-17). Its gate text was
  already correct.
- **GAP-K** "Blocking on: V3-EXQ-543c-successor" -> the sibling nodes. That
  successor **is V3-EXQ-628 and it landed PASS 2026-06-02**; the row's own body
  said so while its gate cell did not. Per `resume_condition`, do not re-queue
  that slice.

On the two `TBD` owners the reconcile brief asked about: **both were kept, and
deliberately.** GAP-I and GAP-J are blocked on GAP-B delivering non-inert gating
/ differentiated rule_state; until that lands there is no experiment to author,
so an id cannot be minted. The wording was changed from bare "TBD" to "none
assignable -- gated on GAP-B", because "TBD" reads as *unassigned work awaiting
someone's attention* when the truth is *no work is authorable yet*. For GAP-J
specifically: the 543 lineage did continue (543h/i/j/k/l all ran) but none of
those is the additive-logit-vs-multiplicative-gate comparison the node needs, so
resolving its "TBD (543g-successor)" to any existing id would be wrong.

### 2026-05-18 - GAP-L lit-pull DISCHARGED: socially-scaffolded rule-population biology grounded (ARC-077 / MECH-337 / MECH-338); lit gate closed, caregiver-substrate gate still open

Trigger: the GAP-L hard prerequisite added in the same-day registration
entry below. Per the standing biology-before-formal-definitions rule,
ARC-077 / MECH-337 / MECH-338 were registered as structural slots with
lit_conf=0 and could not be implemented or promoted until a
caregiver-scaffolding / cued-recall / context-dependent
rule-acquisition lit-pull was discharged. This session (`/lit-pull`,
session gap-l-litpull-socially-scaffolded) discharges exactly that
gate and nothing more.

Work done. New cross-cutting literature dir
`evidence/literature/targeted_review_socially_scaffolded_rule_population`,
8 entries (record.json + summary.md), tagged ARC-077/MECH-337/MECH-338,
covering the full GAP-L minimum-coverage set:

- **Csibra & Gergely 2009** (Trends Cogn Sci) -- natural pedagogy /
  ostensive cueing -> MECH-337/ARC-077, supports, conf 0.80.
- **Wood, Bruner & Ross 1976** (J Child Psychol Psychiatry) --
  scaffolding + Vygotsky ZPD operationalization -> ARC-077/MECH-337,
  supports, conf 0.78.
- **Tomasello, Carpenter, Call, Behne & Moll 2005** (Behav Brain Sci)
  -- shared intentionality / joint attention / social referencing
  (the enabling precondition) -> ARC-077/MECH-337, supports, conf 0.74.
- **Tulving & Thomson 1973** (Psychol Rev) -- encoding specificity (the
  formal core of cued retrieval) -> MECH-338, supports, conf 0.82.
- **Godden & Baddeley 1975** (Br J Psychol) -- environmental
  context-dependent recall; **2021 powered pre-registered replication
  FAILED** -> MECH-338, supports-but-fragile, conf 0.58 (logged with
  the contra).
- **Nakazawa et al. 2002** (Science) -- CA3 NMDA pattern completion =
  the partial-cue retrieval substrate -> MECH-338, supports, conf 0.78.
- **Heyes 2016** (Perspect Psychol Sci) -- COUNTERWEIGHT: the receptive
  machinery may be constructed, not innate; bounds a strong framing of
  MECH-337, not the effect -> mixed, conf 0.70.
- **Spelke & Kinzler 2007** (Dev Sci) -- COUNTERWEIGHT: core knowledge
  / endogenous-maturational structure bounds how much rule structure is
  socially sourced -> ARC-077, mixed, conf 0.66.

Index rebuilt (literature entries 1458). claims.yaml lit_conf set as a
**parallel** signal (NOT blended into exp confidence; lit and exp
evidence are not co-equal): ARC-077=0.74, MECH-337=0.78, MECH-338=0.75
(reasoned aggregates, conservative vs the indexer parallel
literature_confidence 0.868/0.878/0.813 in claim_evidence.v1.json --
discounted for the two principled mixed counterweights and the
structural-slot-only status). literature_anchors added to all three
claims; evidence_quality_note updated on each.

Decision / posture. The LIT gate is **closed**; ARC-077/MECH-337/
MECH-338 **remain candidate** -- discharging the lit-pull explicitly
does NOT promote them (exp_conf=0; the biology-before-formal rule is a
gate on registration validity, not a promotion lever). The **second
hard gate is untouched and still OPEN**: the pathway requires a
caregiver/teacher-agent substrate that does not exist in V3
(single-agent); scaffolded exposure needs a second agent or an
ostensive-cue-delivering environment. GAP-L node status -> `done` for
the lit gate with the substrate gate explicitly flagged as separately
unresolved. No ARC-062 posture change; GAP-B remains blocked and owned
by V3-EXQ-543i/543j (out of scope for this session). The Heyes
counterweight notably *reinforces* the substrate gate (a constructed,
not innate, channel must be built deliberately).

### 2026-05-18 - ARC-063 brought forward (V4 -> V3) + socially-scaffolded rule-population pathway registered (ARC-077 / MECH-337 / MECH-338); GAP-L lit-pull gate added

Trigger (user, this session): "So the Blocked ARC-062 weak route means I
think I now need to: create ARC-063 CandidateRule field / context-bound
rule population; connect to cue pipeline / hippocampal rollout /
caregiver-scaffolded exposure." Scope pinned via AskUserQuestion (4
questions): (1) scope = bring ARC-063 forward + register the sub-cluster;
(2) 543j gate = proceed in parallel on the independent-need basis, NO
ARC-062 posture change; (3) biology = register slot now, flag lit-pull as
hard prereq; (4) framing = "you decide from the architecture".

Finding that reframed the request: **ARC-063 already existed** (registered
2026-05-08 as the V4-deferred strong-reading persistent flag), already
sketching the CandidateRule field, tolerance gate, hippocampal-rollout-
eligibility, evidence-trace records, sleep/waking asymmetry. So this was
not a from-scratch creation but an elaborate-and-bring-forward, plus two
genuinely-new commitments (cue pipeline + caregiver-scaffolded exposure;
hippocampal rollout was already an ARC-063 face).

Architecture decision (framing, delegated). Registered the socially-
scaffolded / cue-driven context-bound population as a **new peer pathway
ARC-077**, NOT a sub-mechanism of ARC-063. Reasoning: ARC-063 is the
*field* that HOLDS candidate rules; MECH-309's core point is that
gradient/Bayesian learners do not invent the hypothesis space, so "where
do candidate rules COME from" is architecturally primary, and the cluster
already partitions rule-*sources* by pathway (ARC-062 top-down, ARC-064
bottom-up, ARC-065 upstream diversity). Caregiver-scaffolded population is
the third source -- biologically the dominant one -- so it is peer to
ARC-062/ARC-064 and feeds the ARC-063 field rather than living inside it.
Three faces of the field made explicit: population/"in" = MECH-337
(caregiver-scaffolded, context-bound by construction); select/"cue
pipeline" = MECH-338 (cue-driven context-bound retrieval, feeds the
existing ARC-063 Tolerance-Principle gate); express/"out" = hippocampal-
rollout-eligibility, already an ARC-063 commitment (cross-referenced, not
re-registered).

Applied (single-pass, REE_assembly): claims.yaml -- ARC-063
implementation_phase v4 -> v3, v3_pending false -> true,
brought_forward_utc 2026-05-18, bring-forward evidence_quality_note,
stale MECH-310..313 sub-claim list corrected (MECH-312/313 are now taken
by unrelated claims -- must not be reused), notes V3-Pending-Gate text
updated; ARC-077 + MECH-337 + MECH-338 registered (645 -> 648 claims) as
structural slots with implementation_prerequisites HARD ORDERING GATE;
MECH-309.depends_on += ARC-077; ARC-062 notes CROSS-REF added (explicit
NO posture change -- still candidate / substrate_ceiling /
pending_retest_after_substrate / narrow_supports_flag). Architecture doc
rule_apprehension_layer.md preamble + new "Socially-scaffolded rule-
population pathway" section + corrected sub-claim landscape. Plan-doc:
scope_claims += ARC-077/MECH-337/MECH-338; GAP-L node added (this gate);
status-table row; this entry.

GAP-L (the gate). Two independent HARD gates before ANY implementation:
(1) caregiver-scaffolding / cued-recall / context-dependent rule-
acquisition biology lit-pull (Csibra & Gergely; Vygotsky ZPD;
Wood/Bruner/Ross; Tomasello; joint attention / social referencing;
Godden & Baddeley; Tulving & Thomson) -- standing biology-before-formal-
definitions rule; (2) a caregiver/teacher-agent substrate, which DOES
NOT EXIST in V3 (single-agent). lit_conf=0; must not promote past
candidate until GAP-L discharged.

NO ARC-062 posture change. GAP-B stays blocked, owned by V3-EXQ-543i
(/failure-autopsy of the diff-OFF non-reproduction) + the in-flight
V3-EXQ-543j cross-machine confirmation. ARC-063 was brought forward on
the independent-need rationale (moral-residue attribution + clinically-
realistic failure modes are needed regardless of the weak-route
verdict), explicitly NOT a declaration that the weak route is dead.

### 2026-05-18 - Closure-map reconciliation: confirmed failure_autopsy_V3-EXQ-543h applied; GAP-B in-progress -> blocked, owner 543h -> 543i

Trigger: the 2026-05-18 governance cycle (REE_assembly a6fda79367; WORKSPACE_STATE
2026-05-18T16:30Z) applied the confirmed `failure_autopsy_V3-EXQ-543h` to the
ARC-062/MECH-309 crystallization-falsifier cluster. The plan-doc frontmatter
(last committed 2026-05-17 20:07, 8bab1d7d75) still described V3-EXQ-543h as the
in-flight owner awaiting completion, so the closure map (`/api/closure`) was
rendering GAP-B as `in-progress` one cycle behind the governed reality. This is
a reconcile-only pass -- no new experiments, no claim edits (governance already
applied those); only the plan-doc node/status-table/decision-log are brought in
line with claims.yaml + the autopsy.

Governed reality applied to GAP-B:

1. The whole **543f / 543g / 543h** MECH-309/ARC-062 falsifier cluster is
   `non_contributory`, `epistemic_category=substrate_ceiling`. Root cause:
   GatedPolicy head-differentiation does not robustly persist under
   outcome-coupled REINFORCE -- gated arms collapse to inert intermittently.
2. **Cross-machine proof** (161cb95a90, 422c7e7f6c): the identical 543g config
   was ACTIVE on host-A only and INERT on cloud-3 + cloud-4 (bit-identical to
   ARM_0). 543g `_144716Z` 'weakens ARC-062' is therefore a 1/3 minority-basin
   artifact -- 543g overall `non_contributory` and **its supersession of its
   predecessor is voided**. 543h resolved to pre-registered grid branch (c)
   (no repro -> substrate/seed drift, non_contributory); the 543h
   INV-074/MECH-334 branch-(b) per_claim 'weakens' was corrected to
   `non_contributory`. 543h ran cloud-4 2026-05-18, runner never pushed the
   manifest, result recovered (e8a2788f71).
3. All **seven** cluster manifests marked `evidence_direction=superseded` by
   **V3-EXQ-543i**. claims.yaml ARC-062 / MECH-309 / INV-074 / MECH-334 carry
   `evidence_quality_note` + `epistemic_category=substrate_ceiling` +
   `pending_retest_after_substrate`. `narrow_supports_flag` set: ARC-062 /
   MECH-309 have ZERO reliable contributory trained-policy evidence -- voiding
   the cluster is NOT conflict resolution for either claim.
4. Substrate fix landed: **GatedPolicy differential-heads robustness fix**
   (`use_differential_heads`; MECH-333 implementation_note; REE_assembly
   b99aefbe69). **V3-EXQ-543i** validates it -- `diff_on_escape=true` confirms
   `use_differential_heads` resolves head-collapse -- BUT
   `diff_off_reproduced_collapse=false`, so 543i is **FLAGGED FOR
   /failure-autopsy** (diff-OFF contrast non-reproduction unexplained) and
   carries no `evidence_direction` pending that post-mortem.
5. `substrate_queue` ARC-062 entry updated with the autopsy `failure_record`.

Plan-doc changes (this pass):

- GAP-B: `status` in-progress -> **blocked**; `owner_exq` V3-EXQ-543h ->
  **V3-EXQ-543i**; `last_updated` -> 2026-05-18; title rewritten to the cluster
  outcome; `resume_condition` prepended with the 2026-05-18 governance block
  (prior 2026-05-17 text demoted to PRIOR, retained).
- GAP-C / GAP-D: `substrate_note` validation-EXQ gate re-pointed from the
  superseded **V3-EXQ-543f** to "the V3-EXQ-543i /failure-autopsy + a
  contributory post-substrate (differential-heads) GAP-B retest";
  `last_updated` -> 2026-05-18. Substrate itself unchanged (still implemented,
  484/484 PASS).
- Status table: GAP-B / GAP-C / GAP-D rows updated to match.

RESUME primitive: GAP-B is blocked until (1) the V3-EXQ-543i /failure-autopsy
explains the diff-OFF non-reproduction, then (2) a contributory post-substrate
(differential-heads) retest of the MECH-309/ARC-062 falsifier. GAP-C/GAP-D
validation EXQs stay deferred until that retest is contributory. GAP-J / GAP-K
(both blocked-on-GAP-B, owner "543g/543c-successor TBD") are one level removed
and left as-is this pass -- their GAP-B dependency already routes them correctly;
flagged for the next owner-EXQ refresh.

### 2026-05-17 - V3-EXQ-543g FAIL (dACC corrupts gated weights) routed to INV-074/MECH-334 crystallization; substrate landed + V3-EXQ-543h 2x2x2 queued

**Result.** V3-EXQ-543g (the 543d/g 2x2 SP-CEM factorial + GAP-B option-2
first-action one-hot head input + outcome-coupled REINFORCE P1 loss) ran to
completion and registered **FAIL / weakens ARC-062**:
`reef_fraction` ARM_0_baseline=0.278, ARM_1_dacc_only=0.174,
ARM_2_gated_only=**0.444 (best)**, ARM_3_both=**0.243 (regresses BELOW
gated-only)**. **D2 (ARM_3-ARM_2 >= +0.10) FAILED, delta=-0.200**; D3 PASS
delta=+0.069. Confirmed by a local backward-compat dry-run of the unmodified
543g script during the 543h build (identical arm means), so the signature is
reproducible, not seed noise.

**Diagnosis.** The 543f one-hot head-input fix cleared the 543b-e inert-gating
bottleneck -- the gate now expresses itself (no probe-gate FAIL). The new
failure mode is different: the **dACC training signal corrupts the
gated-policy discrimination ARM_2 established, via shared-return gradient
flow**. The gated policy is never crystallized before dACC's perturbation is
introduced, so dACC's gradient destroys the discrimination (the
heterosynaptic-depression analog -- O'Dell 2025, cited in INV-074's
literature anchors: the dominant pathway *actively depresses* competitors).
This is the experimental signature of the **missing critical-period closure
mechanism (MECH-334)**.

**Routing (user task 2026-05-17).** The INV-074 / MECH-333 / MECH-334 /
ARC-075 / Q-052 cluster (registered 2026-05-17, commit 3bd35da308) was
registered for exactly this failure mode.

1. **/implement-substrate** landed the Phase-3 crystallization hook:
   `GatedPolicy.crystallize()` freezes head_0/head_1/discriminator and adds a
   zero-init plastic expansion MLP (**Nikishin et al. 2023 NeurIPS plasticity
   injection**; forward = `frozen_gated(x) + expansion(x.detach())` -- the
   `.detach()` blocks the routed-diversity gradient from the crystallized
   discrimination); `ResidueField.snapshot_ewc_anchor()` + `ewc_penalty()`
   apply a Fisher-weighted quadratic write-protect anchored to the Phase-3
   checkpoint (**Kirkpatrick et al. 2017 EWC**; established-basin Fisher proxy
   `|anchor_w|*active_mask` -- NOT a hard freeze, faithful to MECH-334 "high
   resistance to overwriting established basins");
   `InfantCurriculumScheduler(on_phase3_entry=...)` fire-once hook. Everything
   behind `REEConfig.crystallize_at_phase3` (default OFF, bit-identical;
   484/484 contracts PASS; the unmodified 543g dry-run reproduced the prior
   signature exactly). ree-v3 `f8b93e3`; REE_assembly `f71b6a7da0`
   (claims.yaml implementation_note on MECH-333/334/ARC-075;
   `docs/architecture/critical_period_crystallization.md`).

2. **/queue-experiment** queued **V3-EXQ-543h** (ree-v3 `ab2dd30`): a 2x2x2
   factorial (`use_gated_policy x use_dacc x crystallize_at_phase3`), 8 arms x
   3 seeds = 24 runs, `supersedes V3-EXQ-543g`. xtal-OFF arms (ARM_0-3) are an
   exact 543g reproduction (dry-run verified bit-identical); xtal-ON arms
   (ARM_4-7) add the full closure regime, firing the closure at the P1
   open-window-closes boundary (`CRYSTALLIZE_P1_OPEN_FRACTION=0.5`), rebuilding
   the REINFORCE optimizer to `gated_policy.expansion_parameters()` only, and
   adding `residue.ewc_penalty()` (lambda=0.1) to the P1 loss.

**Pre-check (Pathak et al. 2017 ICM self-defeat; reported per task).** Audit
of the routed diversity signals: **MECH-314b** (uncertainty, reads
`e3._running_variance`) and **MECH-314c** (learning-progress, EMA of
`|PE_t-PE_{t-K}|` fed `e3._running_variance`) are forward-model-error-
dependent -- 314c is the canonical Pathak ICM self-defeat case -- and decay to
~0 before Phase-3 crystallization fires, so they cannot establish competitive
weight on a fresh expansion layer. **MECH-313** (constant softmax-temperature
lift), **MECH-314a** (residue-RBF novelty; Wittmann 2008 striatal novelty
RPE-independent by design), **MECH-320-primary** (avg-reward-rate EWMA; Niv
2007 -- only the non-load-bearing `gate_pe` secondary modulator is F-adjacent),
and **dACC / MECH-260** (state-dependent recency) are F-robust. **Arm
adjustment:** 543h holds MECH-314 in novelty-only config (314a ON, 314b/314c
OFF) on the xtal arms so the test is not diluted by a confounded null channel.
Crucially, dACC -- the exact 543g corrupting signal -- is NOT F-error-
dependent, so the crystallization hypothesis is cleanly testable.

**SCHEDULER-GATE ADAPTATION (transparent deviation).** The production driver
for the closure is `InfantCurriculumScheduler(on_phase3_entry=...)`. Its hard
episode-min gate is `PHASE_EP_MIN[3]=2000`; the GAP-B falsifier runs ~108
episodes/arm, so the production scheduler cannot organically reach Phase 3
here. 543h instantiates the scheduler with the IDENTICAL closure (validates
the production wiring contract) but fires that closure at the falsifier's
open-window-closes boundary. The crystallization SUBSTRATE PRIMITIVE is the
scientific object under test; the scheduler episode gate is a deployment
driver, not testable in a compressed falsifier.

**RESIDUE-EWC SCOPING (honest).** In the 543 falsifier the residue field is
accumulated via `.data` writes (add_residue / update_valence), NOT
gradient-trained, so the policy-side plasticity injection is the LOAD-BEARING
crystallization factor for the D2_xtal hypothesis. The residue EWC term is
included per MECH-334, is non-inert (lambda=0.1, anchored at the boundary),
recorded in the manifest; its behavioural effect in this specific falsifier is
limited.

**Acceptance + interpretation grid (pre-registered).** PRIMARY **D2_xtal =
ARM_7_both_xtal - ARM_6_gated_only_xtal >= +0.10** (with crystallization,
dACC-on-top-of-gated no longer regresses -- D2 PASSes where 543g had D2 FAIL
delta=-0.200). SECONDARY **repro = ARM_2 > ARM_3** (543g signature reproduced
on the OFF arms). PASS = D2_xtal AND repro AND not xtal_harms_gated_only.
Branch recorded in `metrics.acceptance.interpretation_branch`:
(a) D2_xtal PASS + repro -> crystallization rescues the gradient
interference; **Q-052 resolves toward (B) structural; close GAP-B + unblock
GAP-C/D**. (b) D2_xtal FAIL + repro -> defect isolated to dACC's own
architecture, NOT gradient interference (narrower diagnostic); GAP-B stays
in-progress, route to dACC-architecture review. (c) no repro -> substrate /
seed drift; non_contributory across all claims. (d) xtal degrades gated-only
-> plasticity injection itself harmful; escalate /diagnose-errors. claim_ids
`[ARC-062, MECH-309, INV-074, MECH-334]`; `evidence_direction_per_claim`
emitted.

**Handoffs / flags.** (i) V3-EXQ-543g is still in `experiment_queue.json` with
status `claimed`; it was NOT mutated (scope discipline + concurrency: never
silently mutate another session's / runner's claim) -- flagged for governance
/ runner reconciliation (its result already exists; 543h supersedes it).
(ii) V3-EXQ-543g run_id should be added to `reviewed_run_ids` at the next
governance pass (it is a completed FAIL, now routed). GAP-C/GAP-D substrate
stays pre-positioned; their validation EXQs remain deferred until a
contributory 543h result.

### 2026-05-17 - GAP-J depends_on corrected to [GAP-B]; stale owner_exq updated

GAP-J `depends_on: []` was a documentation bug. The additive-logit-vs-multiplicative-gate
comparison (MECH-312's core test) is not interpretable while gating is inert -- a contributory
GAP-B result is a prerequisite. Added `depends_on: ["arc_062_rule_apprehension:GAP-B"]`.
`owner_exq` updated from stale `V3-EXQ-543b/c` (all non_contributory for inert-gating reasons
unrelated to combination-rule architecture) to `TBD (543g-successor)`.

### 2026-05-17 - V3-EXQ-543e FAIL non_contributory diagnosed (H3 confirmed): route to pre-registered option 2 (ARC-062 head-input augmentation)

V3-EXQ-543e ran to completion on DLAPTOP-4.local 2026-05-16T23:42:42Z ->
2026-05-17T01:02:03Z (real run, `exit_reason: ok`, `actual_secs=4760.7`,
NOT a crash) and registered **FAIL** with
`evidence_direction: non_contributory`,
`per_claim {ARC-062: weakens, MECH-309: non_contributory}` (pre-registered
`_compute_per_claim_direction` grid; NOT force-mapped). reef_fraction
ARM_0=ARM_1_dacc_only=0.6918, ARM_2_gated_only=ARM_3_both=0.5600; D1 and
D2 deltas exactly 0.0, D3=-0.1317; probe-gate FAIL all 3 seeds in both
gated arms -- the same inert-gating signature as 543b/c/d.

Per the memory rule (non_contributory results need /diagnose-errors, not
force-mapping) the user routed this to /diagnose-errors. A direct
diagnostic harness replicated 543e's exact ARM_2 (gated ON, dacc OFF) P0
stepping path and instrumented
`agent.hippocampal.get_last_propose_diagnostics()` plus the pairwise L2
spread of the exact `candidate_features` tensor the probe uses
(`cat([c.world_states[1] for c in candidates[:8]])`). The three
hypotheses were discriminated:

- **H1 (SP-CEM not engaging at probe time): FALSE.**
  `candidate_unique_first_action_classes` mean **4.95**,
  `candidate_first_action_entropy` mean **1.26**, 32 candidates/propose.
  `support_preserving_active=0/22` is the EXPECTED signature when
  stratified-elites delivers diversity without the injection path
  (V3-EXQ-567's own notes record exactly this). The candidate population
  is genuinely first-action-diverse.
- **H2 (probe-feature masking / 543b Cause-1 repeat): FALSE.**
  `world_states[0]` pairwise meanL2 = **0.0 exact** (confirms the
  world_states[1] fix is correctly in place -- the script is not reading
  the identical pre-action z_world); `world_states[1]` pairwise meanL2
  ~ **0.013**, ~1000x larger than 543b's ~1.2e-5. The probe features are
  non-degenerate.
- **H3 (genuine substrate finding): CONFIRMED.** `world_states[1]` vector
  norm/candidate 0.6705; cross-candidate per-dim std 0.001473; ratio
  **0.0022 (0.22%)**. SP-CEM/stratified produces ~5 distinct first-action
  classes, but E2's world-forward model compresses that categorical
  diversity to 0.22% of the z_world signal magnitude before it reaches
  the z_world-only ARC-062 `GatedPolicy` head. The head cannot convert a
  0.22%-relative signal into behavioural divergence; the probe correctly
  detects inert-gating. (Secondary: only ~9-10% of steps generate fresh
  candidates via an E3 tick; the rest return the MECH-057a cached set --
  expected heartbeat behaviour, not the bottleneck.)

**Interpretation.** 543e is the FIRST run in the 543 lineage where the
2026-05-11 candidate-distinguishability confound is **provably absent**.
With that confound removed, the persistent inert-gating is a clean,
confound-free isolation of the ARC-062 head's z_world-only input contract
as the architectural bottleneck. The substrate (SP-CEM/stratified) is
sound but the head is under-fed: the discriminating signal lives in
action space (4.95 classes) but not in the head's z_world input space.
The script's pre-registered grid maps the probe-gate short-circuit to
`non_contributory` (a conservative pre-registration authored when the
substrate confound was still suspected); the underlying finding is the
substrate-level result the MECH-309 / ARC-062 narrative predicts. The
`non_contributory` manifest direction is left as-is and NOT force-mapped
-- contributory weight is captured by this decision-log entry and the
autopsy artifact, not by relabelling.

**Routing decision: pre-registered option 2 (ARC-062 head-input
augmentation).** Of the three pre-registered FAIL routes (D1-only ->
ARC-062 substrate-rationale review; option 2 head-input augmentation;
ARC-062 retirement / ARC-063 V4 escalation), the diagnosis directly
selects option 2 and quantitatively justifies it: feed the first-action
one-hot (≈5 distinct classes, the strong signal) directly into the
`GatedPolicy` head input rather than relying on the 0.22%-relative
z_world projection. ARC-062 substrate-rationale retirement is explicitly
NOT recommended -- the substrate is under-fed, not redundant; the
mechanism is sound and option 2 is a small, well-scoped contract change.

**Next action.** /implement-substrate: augment the ARC-062
`GatedPolicy` head input with the first-action one-hot (a change to the
ARC-062 head input contract registered in ree-v3/CLAUDE.md -- belongs
under /implement-substrate, not /queue-experiment). Then re-issue the
falsifier as **V3-EXQ-543f** via /queue-experiment: the canonical 543d
2x2 factorial and the SP-CEM substrate are unchanged; only the head
input contract changes. supersedes V3-EXQ-543e. GAP-B stays
`in-progress`, blocked on the option-2 substrate change; GAP-C / GAP-D
stay `open`, sequenced after a contributory falsifier PASS.

**Artifacts.** `evidence/planning/failure_autopsy_EXQ-543e_2026-05-17.md`
+ `.json`. Diagnostic harness `/tmp/diag_543e_spcem.py` (throwaway, not
committed). claims.yaml NOT modified; review_tracker.json NOT modified
(diagnose-errors boundary -- V3-EXQ-543e is a completed FAIL now
diagnosed; flag for the next governance/review pass to add the run_id to
`reviewed_run_ids`).

### 2026-05-16 - V3-EXQ-543e queued: MECH-309 monomodal-collapse falsifier re-issued on the SP-CEM substrate (GAP-B open -> in-progress)

Executes the next action set by the 2026-05-16 closure-map reconciliation
entry below. The CEM-candidate-distinguishability gate having been
satisfied by V3-EXQ-567 PASS (ARC-065 SP-CEM), the MECH-309
monomodal-collapse falsifier was re-issued via the /queue-experiment
skill as **V3-EXQ-543e** (`v3_exq_543e_arc062_spcem_falsifier.py`),
supersedes V3-EXQ-543d.

**Design decision: substrate correction, not redesign.** 543e is a
lettered iteration of the 543 falsifier line per the EXQ versioning
policy -- the scientific question (MECH-309 logical necessity) is
unchanged; the prior 543b/c/d runs were invalidated because they ran on
the OLD collapsed CEM. The canonical 543d 2x2 factorial design is kept
verbatim: arms (ARM_0 gated/dacc OFF, ARM_1 dacc-only
suppression_weight=0.5, ARM_2 gated-only, ARM_3 both), the pre-registered
D1-D4 cross-arm grid, PASS=D2 AND D3, the FAIL-routing tree,
claim_ids=[ARC-062, MECH-309], and the per-claim evidence-direction grid
are all unchanged. The SINGLE change is that the shared
`_make_agent_and_env` `from_dims` call now enables support-preserving CEM
on **all four arms** (it is the fixed substrate, not a factorial axis):
`use_support_preserving_cem=True`,
`support_preserving_stratified_elites=True`,
`support_preserving_ao_std_floor=0.2`,
`support_preserving_min_first_action_classes=2` -- the exact
configuration V3-EXQ-567 validated PASS for ARC-065 (lifted natural
selected_action_entropy 0.0124 -> 0.49, candidate support 1.00 -> 2.80).
No further architectural decision among the three 2026-05-11 options was
required -- the "substrate redesign" branch was effectively taken and
validated by the ARC-065 SP-CEM line, as recorded in the reconciliation
entry below.

**Evidence-validity note.** The 543b/c/d evidence remains
non_contributory / weakens and is explicitly NOT force-mapped: it was
collected on the invalidated collapsed-CEM substrate where the ARC-062
gated heads had no candidate-feature variance to discriminate on
(~1e-4..1e-5 spread). V3-EXQ-543e is the FIRST contributory test of the
MECH-309 monomodal-collapse claim.

**Verification.** /queue-experiment code-review pass + smoke dry-run:
exit 0; 12 verdict lines (4 arms x 3 seeds); 36 `[train] ep N/M` progress
lines with the loop-bound `total_train_episodes` denominator; 12
`Seed/Condition` boundary lines; `gated_policy`/`dacc` toggling correctly
per arm; SP-CEM flags independently verified reaching
`config.hippocampal` in all 4 arms; D1-D4 printout works; ASCII-only;
`validate_experiments.py` runner-conformance PASS; `validate_queue.py`
PASS. Queued (priority 1, DLAPTOP-4.local affinity matching the 543b/c/d
precedent, 540 min, episodes_per_run=108, seeds=3, conditions=4) and
auto-claimed by runner DLAPTOP-4.local at 2026-05-16T23:42:41Z.

**Next action.** On 543e completion, review the outcome and route per
the pre-registered D-grid: PASS (D2 AND D3) closes GAP-B (`in-progress ->
done`) and unblocks GAP-C / GAP-D Phase 3 wiring (discriminator ->
SD-033a LateralPFCAnalog; commitment_closure GAP-1); FAIL D1-only routes
to ARC-062 substrate-rationale review; FAIL all-D-null routes to option 2
head-input augmentation (/implement-substrate). GAP-C / GAP-D remain
`open`, correctly sequenced after the falsifier result.

### 2026-05-16 - Closure-map reconciliation: ARC-065 SP-CEM (V3-EXQ-567) satisfies the GAP-B CEM-candidate-distinguishability gate

Staleness pass triggered after a closure-map review found the plan
status tables 5-8 days behind the runner (now at V3-EXQ-581).

The 2026-05-11 GAP-B bottleneck was: CEM candidate collapse leaves
candidate-feature variance too low for the ARC-062 gated heads to
discriminate, so the MECH-309 monomodal-collapse falsifier line
(V3-EXQ-543b superseded; 543c / 543d non_contributory) could not
deliver. V3-EXQ-567 (PASS, evidence_direction=supports, ARC-065) is the
support-preserving CEM fix: ARM_1 (SP-CEM + stratified + ao_std_floor)
vs ARM_0 (normal CEM) lifts natural selected_action_entropy
0.0124 -> 0.4965 (delta 0.484) and candidate support 1.007 -> 2.810.
That is exactly the candidate-feature variance the 2026-05-11 gate
required. The "substrate redesign" branch of the 2026-05-11 three-way
decision was effectively taken and validated by the ARC-065 SP-CEM line
(V3-EXQ-567 / 573; V3-EXQ-568 differentiable-CEM substrate SD-055 5/5 UC).

Action taken: GAP-B status blocked -> open; owner_exq set to a re-issued
MECH-309 monomodal-collapse falsifier on the SP-CEM substrate (via
/queue-experiment, not yet queued). GAP-C / GAP-D remain `open`,
correctly sequenced after the falsifier re-run. The 543b/c/d evidence
stays non_contributory/superseded (run under the old collapsed CEM) and
must NOT be force-mapped -- the re-run on SP-CEM is the contributory test.

### 2026-05-11 - V3-EXQ-543c FAIL (probe-gate FAIL, non_contributory): isolated-substrate replication confirms ARM_1c inert-gating; superseded by V3-EXQ-543d 2x2 factorial (already running on DLAPTOP-4.local)

V3-EXQ-543c ran 2026-05-11T19:02Z (DLAPTOP-4.local) and registered FAIL with
`evidence_direction: "non_contributory"` per the per-claim grid -- both
ARC-062 and MECH-309 mapped to `non_contributory`. The acceptance grid
recorded `probe_gate_arm_failed=true` with `n_inert_gating_seeds_arm1c=3`
(all 3 seeds in ARM_1c flagged `p1_inert_gating_detected: true`) and the
overall result keyed off the probe gate: only `C4_cross_seed_variation` of
the four substantive criteria passed; `C1_density_tracking` was
`non_contributory_phase2a_corrected_single_density`; `C2_state_dependence`,
`C3_risk_type_dissociation`, and the `pass_rule_met` all FAIL. Per the
pre-registered D-criteria interpretation in the manifest's
`evidence_direction_per_claim`, probe-gate FAIL is the second of the three
pre-registered outcomes, and routes ARC-062 + MECH-309 to `non_contributory`
(neither supports nor weakens) rather than to a `weakens` reading.

**Interpretation (per pre-registered grid):** ARM_1c (full three-stream
gated heads) exhibits the same inert-gating signature 543b surfaced. The
mean `tv_distance` across all 12 probe windows in ARM_1c remains in the
1e-7 to 1e-9 range across all 3 seeds -- well below
`INERT_GATING_THRESHOLD = 0.05`. Per-seed `mean_reef_fraction`,
`rho_drive_vs_reef`, `forage_hazard_rate`, `transit_hazard_rate`, and
`risk_type_ratio` are **floating-point-identical** between ARM_0 and
ARM_1c for every seed pair (seed 0: reef=0.0/0.0, rho=0.164/-0.128;
seed 1: reef=0.87/0.87, rho=-0.049/-0.049; seed 2: reef=0.0/0.0,
rho=0.223/0.223). ARM_1c is a strict replication of the 543b finding on
a different substrate (SD-054 bipartite reef-vs-forage with the post-543b
`world_states[1]` Cause-1 fix incorporated): when ARC-062 runs in
architectural isolation from the MECH-260 + SD-032a/b + SD-033a/b cluster
it was designed to live in, the gated-policy heads cannot produce
behavioural divergence even with the script-level bug fixed.

**Supersession:** V3-EXQ-543d is the natural successor. It is **already
queued and running on DLAPTOP-4.local** (queued 2026-05-11T19:11Z by
parallel session `queue-v3-exq-543d-2026-05-11T1911Z`, claim_id ARC-062,
540 min estimate, picks up after V3-EXQ-540a finishes ~20:30Z). 543d is a
2x2 factorial of `(use_gated_policy, use_dacc)` with MECH-260 anti-recency
`suppression_weight=0.5` on the dACC-ON arms -- testing directly whether
the 543c inert-gating signature reflects (a) actual ARC-062 substrate
failure or (b) absence of BG cluster wiring. **The 543d outcome
supersedes the 543c interpretation.** Per the 543d pre-registered D-grid:
- PASS (D2 AND D3) -> cluster-wiring is the missing piece, both
  substrates contribute -> ARC-062 weak-reading sustained; 543c's
  isolated-substrate inert-gating attributable to missing dACC.
- D1-only PASS -> dACC alone explains alternation; ARC-062 substrate
  redundant; route to ARC-062 substrate-rationale review.
- All-D-null FAIL -> route to option (2) head-input augmentation per the
  2026-05-11 (earlier) decision-log entry on GAP-B blocked-status.

**No new GAP-B status change from 543c alone.** GAP-B remains
`blocked` per the prior 2026-05-11 entry. The CEM-candidate-
distinguishability substrate-readiness diagnostic that was named as the
gate to unblock GAP-B is **partially addressed** by 543d as a
load-bearing-by-cluster falsifier; if 543d clears PASS, the substrate-
readiness diagnostic remains needed only as an explanatory artifact (the
question "what made the difference" rather than "is the substrate
testable"). If 543d FAILs all-D-null, the substrate-readiness diagnostic
escalates to required-before-next-step.

**Files touched in this session:** `arc_062_rule_apprehension_plan.md`
(this decision-log entry); review tracker; WORKSPACE_STATE.md. No
claims.yaml edits; no claim status change (ARC-062 / MECH-309 statuses
unchanged -- evidence is non_contributory, neither supports nor weakens).
The 543c manifest already carries
`evidence_direction_per_claim: {ARC-062: non_contributory,
MECH-309: non_contributory}` and `failure_signatures: []`, so no per-claim
override edit needed. No script written; supersession handled at the
queue level by V3-EXQ-543d (already pushed by parallel session
`queue-v3-exq-543d`). The next plan-doc edit on GAP-B will be authored
after 543d completes.

### 2026-05-11 - GAP-B status `in-progress -> blocked`: V3-EXQ-543b diagnose-errors surfaced CEM-candidate-distinguishability as upstream bottleneck

V3-EXQ-543b ran on Mac 2026-05-10T13:25Z--17:26Z (240 min) and registered
`non_contributory` for ARC-062 / MECH-309 / SD-029 with the
`inert_gating_detected` short-circuit firing on every one of 3 seeds at
MID_TRAINING_EP=30. The behavioural-divergence probe recorded
`mean_tv_distance = max_tv_distance = min_tv_distance = 0.0` (exact float
zero) across **all** 3 seeds x 12 probe windows x 32 probe states.
Exact zero across that variation is not numerical noise -- it is
structural. A diagnose-errors session 2026-05-11T06:35Z--06:44Z (TASK_CLAIMS
session_id `diagnose-v3-exq-543c-2026-05-11T0635Z`) traced the failure to
two distinct causes:

**Cause 1 (script-level bug):** `candidate_features` was built by stacking
`candidates[i].world_states[0]` across the first N_PROBE_CANDIDATES
candidates. By E2FastPredictor convention (`ree_core/predictors/e2_fast.py:316`),
`world_states[0] = initial_z_world` -- the pre-action z_world, IDENTICAL
across all K candidates from a single CEM proposal step. So
`candidate_features` was a [K, world_dim] tensor with K copies of the
same row. Consequence chain: `head_0(features)` and `head_1(features)`
each emit the same scalar across every K row -> `gated_score_bias =
w*h0 + (1-w)*h1` is constant in K -> `softmax(-constant_vector / T)`
is uniform -> TV distance vs the bypass-uniform softmax is exactly
0 for every probe state, every seed, every probe window. The
diversification loss `(head_0_bias - head_1_bias)^2.mean()` was
non-zero only because of the symmetry-broken bias init at
`gated_policy.py:217` (head_0.bias = +0.05, head_1.bias = -0.05);
gradients flowed only into those scalar bias terms (clamped at +/-0.1
by `bias_scale`), never into feature-conditional weights, so the heads
could never learn per-state specialisation regardless of episode count.

**Cause 2 (substrate-level finding, surfaced by direct numerical probe
after the Cause-1 fix was written):** with `world_states[0]` replaced by
`world_states[1]` (first POST-action predicted z_world per candidate),
the pairwise max-diff across 8 candidates becomes **1.2e-5** at t=1,
growing to 2.8e-3 by t=30 -- distinguishable in principle but
microscopic. Resulting `gated_score_bias` varies by ~4e-7 across K;
TV-distance vs bypass ~8.6e-8, still well below `INERT_GATING_THRESHOLD=
0.05`. The deeper finding: at init the CEM proposer produces 8
candidates that all share argmax-first-action=3 with continuous-action
vectors differing only ~1e-4. E2 world_forward is a small-residual
model so post-action z_world diverges by only ~1e-5 at t=1. The ARC-062
substrate is being asked to discriminate between candidates that are
**structurally near-indistinguishable** at the input it consumes
(z_world-only). 543b's "inert gating" signal was over-attributed to
the script bug; even with the bug fixed, the substrate-readiness
premise of the falsifier is in doubt.

**Three architectural options surfaced for resolution:**

  1. **Land Cause-1 fix only (microscopic) and rerun.** Cheap probe; high
     probability of another inert-gating result. Use the result to
     formally retire the "world_states-only head input is sufficient"
     assumption and route to a substrate redesign. Risk: another 4-hour
     non-informative runner slot; result will be hard to disentangle
     from the substrate-design question (substrate intrinsically inert
     vs features-not-distinguishable-enough).

  2. **Augment GatedPolicy head input with first-action.** Concatenate
     the candidate's first-action one-hot to the head input
     (head input dim grows from `world_dim` to `world_dim + action_dim`).
     This is no longer a one-line script fix -- it changes the GatedPolicy
     contract registered in CLAUDE.md and modifies the ARC-062 Phase-1
     substrate. Belongs under `/implement-substrate`, not
     `/diagnose-errors`.

  3. **Env-side diversification: design the world to definitely have the
     signals.** (User direction, 2026-05-11.) Build the substrate so that
     the ARC-062 head consumes inputs that are guaranteed-distinguishable
     across the candidate pool by construction. Concrete instantiations
     to evaluate: (a) extend SD-054 reef partition so reef-vs-forage
     contrast forces actively-different first-action argmaxes per
     candidate; (b) inject env-side stochasticity at episode start so the
     initial z_world carries policy-relevant variance the proposer must
     pass through; (c) curriculum-level perturbation ensuring multiple
     candidate trajectories are individually-distinguishable at t=1.
     This option turns the question "can the substrate produce divergence
     under free parameters" into "given a world where divergence is
     structurally necessary for survival, does the substrate produce
     it" -- a sharper falsifier than the current SD-054 single-density
     setup.

**Decision:** GAP-B status moves from `in-progress` to `blocked`. The
next step is **not** to re-queue the falsifier. A substrate-readiness
diagnostic must characterise CEM-proposer candidate-distinguishability
at init and during training (first-action entropy, continuous-action
L2 spread, world_states-1 pairwise distance, scaled across P0 / P1
training) before any one of the three options is chosen. The
substrate-readiness diagnostic will be authored via
`/queue-experiment` in a separate session (user direction). The plan-
of-record GAP-B `unblocks_claims` field is tightened to
`[MECH-309, ARC-062]`; SD-029 dropped because the SD-054 substrate is
not SD-029's measurement substrate (claim_ids accuracy rule applies
to plan-doc dependency edges too).

Files touched in this session: `arc_062_rule_apprehension_plan.md`
(this entry + GAP-B YAML node status / title / owner_exq /
unblocks_claims / resume_condition + closure-map row); REE_assembly
commit + push pending below. No claims.yaml edits; no claim status
changes (ARC-062 / MECH-309 / SD-029 statuses unchanged). No
substrate-side code touched. Removed in cleanup: scratch
`v3_exq_543c_arc062_phase3_optimized_falsifier_features_fix.py`
script + its dry-run manifest + dry-run signal file (diagnose-errors
session never queued).

Cross-plan links: `commitment_closure:GAP-1` (SD-033a bias head
training) remains blocked transitively via GAP-C (which is itself
blocked on GAP-B). `arc_062:GAP-I` (MECH-318 empirical retire-vs-
promote) remains gated on V3-EXQ-543c-successor; the substrate-
readiness diagnostic does NOT count as that successor.

### 2026-05-10 - GAP-K close: MECH-319 simulation-mode rule-write-gate substrate landed

Third of four ARC-064/ARC-065 child substrates landed today (after
MECH-313 noise-floor + MECH-314 structured-curiosity earlier the same
day; MECH-318 absorption-check is the fourth, completed mid-day with
VERDICT (B) PARTIALLY ABSORBED). MECH-319 substrate is a unified
arbitration-layer simulation-mode write gate that consolidates the
categorical replay-tag gating logic across the existing arbitration-
write call sites (GatedPolicy.forward, LateralPFCAnalog.update) and
exposes a single seam for V3-EXQ-543c-successor falsifier control via
the `admit_writes` inverse-debug flag.

**Module landed.** `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py`
(`SimulationModeRuleGate` + `SimulationModeRuleGateConfig` +
`SimulationModeRuleGateDiagnostics`). Pure-arithmetic regulator (no
`nn.Module` inheritance, no learned parameters); sibling to
`GABAergicDecayRegulator` (SD-036) and `BroadcastOverrideRegulator`
(SD-037). Single primitive `effective_simulation_mode(simulation_mode,
site) -> bool` translating `(master_on, admit_writes, caller_sim)`
into the final admit/block decision per the truth table:

| master | admit_writes | caller_sim | output |
|--------|--------------|------------|--------|
| OFF    | (any)        | (any)      | identity (caller_sim) |
| ON     | False        | False      | False (admit waking) |
| ON     | False        | True       | True  (block sim, MECH-319 normal) |
| ON     | True         | False      | False (admit waking; flag inert) |
| ON     | True         | True       | False (admit sim, V3-EXQ-543c falsifier) |

Idempotent for waking calls regardless of `admit_writes` -- the
falsifier-control asymmetry surfaces only at `caller_sim=True` (replay
paths, ghost-goal probes, DMN passes). Per-site diagnostic counters
(`gated_policy`, `lateral_pfc`, `default`) on `n_calls_total`,
`n_waking_admitted`, `n_simulation_blocked`, `n_simulation_admitted`.

**Config wired through REEConfig + REEConfig.from_dims.**
`use_simulation_mode_rule_gate: bool = False` (master, bit-identical
OFF). `simulation_mode_rule_gate_admit_writes: bool = False`
(V3-EXQ-543c falsifier inverse-debug flag). Construction raises
`ValueError` on `admit_writes=True` without master ON (loud-not-silent
guard against mis-configuration -- the falsifier flag is meaningless
without the substrate to gate).

**Agent wiring at two existing arbitration-write call sites in
`REEAgent.select_action`:** (1) GatedPolicy block: literal
`simulation_mode=False` replaced by
`gate.effective_simulation_mode(False, site=SITE_GATED_POLICY)` and
passed to `gated_policy.forward(...)`. (2) LateralPFCAnalog block:
consult gate via `eff_sim = gate.effective_simulation_mode(False,
site=SITE_LATERAL_PFC)`; skip `lateral_pfc.update(...)` when
`eff_sim=True`, else proceed with existing MECH-261 mode-conditioned
EMA. `compute_bias` still runs (arbitration RECEIVES the bias even
during simulation; only the write-back into `rule_state` is gated).
Per-episode `reset()` clears diagnostic counters.

**MECH-094 NOT modified per Pull 3 R1 + Pull 4 R3 KEEP-AS-IS verdicts.**
The gate is a pre-call coordinator that wraps the `simulation_mode`
argument that callers ALREADY pass. With MECH-319 disabled, every
arbitration-write call site behaves bit-identically to its pre-MECH-319
form. This is the load-bearing architectural invariant -- MECH-094
names the principle (categorical phi(z) write gate keyed to a
hypothesis tag), MECH-319 names the substrate-level instantiation at
the rule-arbitration layer (SWR machinery as the categorical signal,
arbitration-weight updates as the function-site).

**Backward compatibility verified.** 288/288 contract + preflight
tests PASS with master OFF (regression-clean; suite was 273
pre-MECH-319, plus 15 new MECH-319 contracts in
`tests/contracts/test_mech_319_simulation_mode_rule_gate.py`).

**Validation experiment.** V3-EXQ-546 substrate-readiness diagnostic
queued. Six sub-tests UC1-UC5 + UC3b precondition (instantiation +
diagnostic keys; master-OFF backward-compat; truth-table coverage
across the 6 valid `(master, admit_writes, caller_sim)` combinations;
precondition raises `ValueError`; select_action wiring contract --
gate sees waking calls from both `gated_policy` and `lateral_pfc`
sites after one `act_with_split_obs` tick, `n_simulation_*` counters
remain zero on the waking path; MECH-094 invariance -- master-OFF and
master-ON-with-waking-caller produce bit-identical wiring outputs).
Smoke 6/6 PASS 2026-05-10 (manifest scrubbed; runner will write the
canonical PASS manifest from the queued entry).

**Phase 1 vs Phase 2.** Substrate landing only. The behavioural test
that flips `admit_writes=True` and routes a replay-driven invocation
through the rule-arbitration layer is V3-EXQ-543c-successor, deferred
until the MECH-313 / MECH-314 / MECH-318 sibling substrates have
landed AND a replay/DMN call site emerges that exercises
`caller_sim=True` against the wired arbitration sites. Today's commit
exposes the seam and counters; the falsifier validation is downstream.

**Lit-pull synthesis decision.** Existing Pull 3 SYNTHESIS
(`evidence/literature/targeted_review_mech_312_arbitration_divergences/`,
8 entries, lit_conf 0.866 on MECH-094) was judged sufficient -- it
explicitly resolves R1 GENUINE-NOVELTY-CONFIRMED (conf 0.72) with the
substrate-availability anchors (Joo & Frank 2018 SWR review + Foster
& Wilson 2006 reverse replay discriminable signature), and Pull 4 R3
gives the KEEP-AS-IS recommendation that MECH-094 stays as the
architectural principle while MECH-319 instantiates it at the
substrate level. No additional implementation-detail lit-pull
commissioned for this substrate landing.

**Out of scope (separate spawned tasks):** MECH-313 / MECH-314 /
MECH-318 (separately scoped per spawn -- all complete same day);
V3-EXQ-543c-successor falsifier authoring (downstream of this
substrate AND the MECH-313/314/318 sessions).

**Files touched:** `ree-v3/ree_core/regulators/simulation_mode_rule_gate.py`
(NEW); `ree-v3/ree_core/regulators/__init__.py` (export);
`ree-v3/ree_core/utils/config.py` (`REEConfig` fields + `from_dims`
kwargs); `ree-v3/ree_core/agent.py` (import + `__init__`
instantiation + `select_action` GatedPolicy + LateralPFC call-site
wiring + `reset` hook); `ree-v3/tests/contracts/test_mech_319_simulation_mode_rule_gate.py`
(NEW, 15 tests); `ree-v3/experiments/v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness.py`
(NEW); `ree-v3/experiment_queue.json` (V3-EXQ-546 appended);
`ree-v3/CLAUDE.md` (MECH-319 SD entry appended); `REE_assembly/docs/architecture/mech_319_simulation_mode_rule_gate.md`
(NEW); `REE_assembly/docs/claims/claims.yaml` (MECH-319 status
`candidate -> candidate_substrate_landed` + evidence_quality_note +
notes update); `REE_assembly/docs/assets/data/claims.json` (rebuilt
by `build_claims_json.py`); `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md`
(GAP-K row + this decision-log entry); `WORKSPACE_STATE.md`;
`TASK_CLAIMS.json`.

### 2026-05-10 - GAP-I MECH-318 absorption check done: VERDICT (B) PARTIALLY ABSORBED into SD-033a + ARC-062 cluster

MECH-318 (`rule_state_abstraction_substrate` / meta-RL recurrent task-state
representation, Wang 2018 + Duan 2016 RL^2) was registered 2026-05-10 with the
provisional flag `registration_provisional_pending_meta_rl_absorption_check`.
This session ran the architectural absorption check that flag commissioned --
auditing the existing `ree-v3` substrate against the five Wang 2018 / Duan 2016
load-bearing properties before committing to a new substrate landing.

Memo: `REE_assembly/docs/architecture/mech_318_absorption_check.md`.

Three candidate substrates audited:

1. **E1 LSTM** (`ree-v3/ree_core/predictors/e1_deep.py` E1DeepPredictor +
   ContextMemory). Recurrent topology yes; trained-on-rule-discrimination NO;
   per-episode `reset_hidden_state()` so cross-episode continuity NO; bias on
   action selection only indirect (associative prior into HippocampalModule;
   SD-016 cue_terrain_proj into E3). Subtotal: topology-only absorption,
   functional role no.
2. **SD-033a LateralPFCAnalog rule_state buffer** (`ree-v3/ree_core/pfc/
   lateral_pfc_analog.py`). Closest match to "rule-state representation that
   biases action selection". Recurrence-as-EMA per Choice A3 (gate-modulated
   EMA, not LSTM/GRU). Bias head currently frozen-random with last Linear
   zeroed (Choice A2; phased training deferred). rule_state buffer reset per
   episode (V4 extension if cross-episode required). MECH-261 mode-conditioned
   write-gate registry generalises MECH-094 hypothesis tag at the rule-state
   slot.
3. **MECH-269 anchor sets + per-region V_s** (`ree-v3/ree_core/hippocampal/
   anchor_set.py`). Discrete-symbolic state-label encoding via
   `(scale, segment_id, stream_mixture)` keying with dual-trace preservation
   (Bouton 2004). Closer to Schuck 2016 / Wilson 2014 OFC-cognitive-map biology
   than to Wang 2018 RL^2. Architecturally adjacent rather than competing with
   the SD-033a + ARC-062 arm.

Mapping the five Wang 2018 properties onto existing substrate:

- W1 recurrent topology: absorbed (E1 LSTM topology + SD-033a EMA recurrence).
- W2 trained across many tasks: NOT ABSORBED. No multi-task training distribution
  exists in V3 (SD-054 is single-context). This is a *training methodology +
  environment* gap, not a substrate gap.
- W3 hidden state encodes task identity: absorbed by ARC-062 Phase 1
  gated_policy multi-stream (z_world, z_self, z_harm_a) context discriminator
  (per-tick rule-context discrimination, trained on score-aggregation gradient)
  + SD-033a rule_state buffer (substrate-ready, content-empty until Phase 3
  GAP-C wires the discriminator output into the rule_state update path).
- W4 biases action selection: absorbed by SD-033a `compute_bias()` and ARC-062
  gated_policy heads; both compose additively into `dacc_score_bias` before
  E3.select().
- W5 cross-episode hidden-state continuity (the defining RL^2 property): NOT
  ABSORBED. All three candidate substrates reset per episode. SD-033a's notes
  field already records "Cross-episode carry-over is NOT implemented (V3
  simplification; V4 extension if required)". This is likely V4-scope.

**Verdict: (B) PARTIALLY ABSORBED.** The within-V3 portion of MECH-318
(W1 + W3 + W4) is borne by the SD-033a + ARC-062 + ARC-062-Phase-3 cluster.
The within-episode part of Wang 2018 instantiates cleanly on the existing
substrate once Phase 3 GAP-C wires the discriminator into the rule_state
update path. The cross-episode RL^2 part (W5) and the multi-task training
property (W2) remain as MECH-318's legitimate residual scope IF the empirical
verdict turns out to require a dedicated substrate.

NO NEW V3 SUBSTRATE COMMISSIONED. The empirical retire-vs-promote verdict
is deferred to a V3-EXQ-543c-successor on multi-rule-context substrate,
sequenced after:
- ARC-062 Phase 2 GAP-B PASS (V3-EXQ-543b)
- ARC-062 Phase 3 GAP-C wiring closure (discriminator -> SD-033a rule_state)
- A multi-rule-context substrate (SD-054 extension to >=2 reef configurations,
  or equivalent) so the falsifier can exercise the within-episode adaptation
  signature MECH-318 names.

If post-Phase-3 the SD-033a + ARC-062 cluster produces the within-episode
rule-state-adaptation behavioural signature on multi-rule-context substrate,
MECH-318 retires as `superseded` with `superseded_by: SD-033a + ARC-062
(cluster)`. If the cluster fails the signature, MECH-318 promotes to
`candidate -> active` and motivates a dedicated substrate landing (likely
V4-scope given the W5 gap).

Files touched:
- `REE_assembly/docs/architecture/mech_318_absorption_check.md` (new memo)
- `REE_assembly/docs/claims/claims.yaml` (MECH-318 title + evidence_quality_note
  + notes update; status retained `candidate` pending empirical verdict)
- `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md` (GAP-I
  status row + this entry)
- `REE_Working/TASK_CLAIMS.json` (session claim)
- `WORKSPACE_STATE.md`

Out of scope (separate spawned tasks):
- MECH-313 / MECH-314 / MECH-319 substrates (separately scoped per spawn).
- MECH-316 (`cross_episode_regularity_extraction`, Schapiro 2017 CLS +
  Stachenfeld 2017 SR) absorption check.
- MECH-317 (`behavioural_pattern_compression`, Smith & Graybiel + option-critic)
  absorption check.
- The V3-EXQ-543c-successor experiment authoring (downstream of this verdict
  AND ARC-062 Phase 2 + Phase 3 closure AND multi-rule-context substrate).

Forward-link from the absorption-check memo: until the V3-EXQ-543c-successor
verdict lands, MECH-318's within-episode functional weight is borne by
- SD-033a LateralPFCAnalog rule_state buffer (`ree-v3/ree_core/pfc/
  lateral_pfc_analog.py`; design doc `REE_assembly/docs/architecture/
  sd_033a_lateral_pfc_analog.md`)
- ARC-062 Phase 1 GatedPolicy + context discriminator (`ree-v3/ree_core/
  policy/gated_policy.py`; V3-EXQ-542 5/5 PASS 2026-05-09)
- ARC-062 Phase 3 GAP-C wiring (this plan-of-record's Phase 3 / GAP-C row;
  blocked on Phase 2 GAP-B PASS via V3-EXQ-543b).

### 2026-05-10 - GAP-H further partial close: MECH-314 structured-curiosity substrate cluster landed

Second of the four ARC-065 child substrates landed (MECH-313 noise-floor
landed earlier the same day). Resolves the Pull 1 SYNTHESIS R1 BOTH-CHANNELS-
NEEDED commitment: with MECH-313 + MECH-314 both substrate-landed, ARC-065
carries the full cluster commitment for behavioural-diversity generation.
Remaining ARC-065 / ARC-064 children (MECH-318, MECH-319) continue as
separate spawned tasks.

Substrate:
- Module: `ree-v3/ree_core/policy/structured_curiosity.py`
  (StructuredCuriosity + StructuredCuriosityConfig). Pure-arithmetic, no
  learned parameters, no `nn.Module` inheritance; sibling to MECH-313
  NoiseFloor in the `ree_core.policy` package.
- Three sub-flavours implemented as a single module with master + 3
  independently-togglable sub-flavour switches (per Pull 1 R3 verdict NOT
  to collapse them prematurely; Q-044 holds the resolution path):
    - MECH-314a striatal novelty: per-candidate min-distance from candidate's
      first-step z_world to nearest ACTIVE ResidueField RBF center, normalised
      by candidate-pool mean norm. Genuinely per-candidate [K].
    - MECH-314b frontopolar uncertainty: `e3._running_variance` scalar
      broadcast across [K] (Phase 1; per-candidate refinement deferred to
      Phase 2 follow-on requiring an E1 forward-variance head).
    - MECH-314c learning progress: EMA of `|PE_t - PE_{t-K}|` (Schmidhuber
      first-difference) where PE feed is `e3._running_variance` per tick;
      broadcast scalar across [K] (Phase 1; per-candidate refinement deferred).
- Config: `REEConfig.use_structured_curiosity` (default False; bit-identical
  OFF master) + `use_curiosity_novelty` / `_uncertainty` / `_learning_progress`
  (defaults True) + per-sub-flavour weights (default 0.05 each) + `bias_scale`
  clamp (default 0.1, mirrors `lateral_pfc_bias_scale`) + LP EMA alpha (0.1)
  and window K (5). All wired through `REEConfig.from_dims()`.
- Algorithm: per waking tick, `compute_score_bias` returns `[K]` non-positive
  tensor (lower-is-better convention; curiosity makes novel/uncertain/LP-rich
  candidates more attractive). Composed additively into `dacc_score_bias` in
  `REEAgent.select_action()` immediately after the MECH-295 liking-bridge
  block and BEFORE the MECH-313 noise-floor temperature lift (curiosity
  affects scores; noise floor affects temperature; orthogonal).
- LP feed: `update_prediction_error(pe_scalar=e3._running_variance,
  simulation_mode=False)` called after each `e3.select` cycle in
  `select_action`; advances the 314c LP buffer for next tick.
- MECH-094: `compute_score_bias(simulation_mode=True)` returns `zeros[K]` and
  increments only the simulation-skip counter; `update_prediction_error(
  simulation_mode=True)` no-op on the LP buffer. Match the
  SD-035 / MECH-279 / `gated_policy` / MECH-313 simulation_mode pattern.

Architectural-placement note: a separate `StructuredCuriosity` module at
the `e3.select()` call site, in parallel with MECH-313 NoiseFloor and the
GatedPolicy bias chain. The same Phase-1 placement-vs-consolidation note
that MECH-313 carries applies here -- whether the policy-layer regulators
ultimately consolidate into one module is OPEN pending MECH-318 / MECH-319
substrates and Q-043 / Q-044 calibration. The separate-module choice keeps
each sub-flavour independently togglable, which is what Q-044 needs.
Re-evaluate at the point Q-044 / Q-043 are queued.

Phase 1 honest-scoping caveat: 314a is genuinely per-candidate. 314b and
314c are state-dependent global scalars broadcast across [K] in Phase 1.
The architectural shape is correct (bonus magnitude varies with global
uncertainty / LP; substrate exposes the falsification surface), and Q-044's
three-arm ablation IS a flag-set decision -- the substrate guarantees each
sub-flavour can be turned on/off independently. What Phase 1 does NOT
deliver: distinguishable behavioural signatures per sub-flavour at the
candidate-selection level (broadcast-scalar 314b/c shifts every candidate's
score by the same amount and does not change selection ordering). Per-
candidate refinement of 314b (E1 forward-variance head) and 314c (per-
candidate LP estimate) is a Phase 2 follow-on, deferred until Q-044
surfaces concrete need.

Lit-pull synthesis decision: Pull 1 (`evidence/literature/
targeted_review_arc_065_behavioral_diversity_generation/SYNTHESIS.md`,
9 entries, lit_conf 0.78-0.82) judged sufficient -- it explicitly resolves
R1 BOTH-CHANNELS-NEEDED (Wilson 2014 + Faisal 2008 + Friston 2015), R3
PROMOTE-TO-CLUSTER + sub-flavour split with biological anchors per
sub-flavour (Wittmann 2008 striatal novelty for 314a; Daw 2006 + Friston
2010/2015 EFE for 314b; Schmidhuber 1991 + Pathak 2017 for 314c, flagged
"least biologically anchored / potentially-discardable-if-314a+314b-suffice"),
and R4 continuous-in-computation-triggered-in-dominance. Magnitudes
intentionally not pinned by the lit-pull (Q-043 calibration sweep is the
empirical route; Q-044 three-arm ablation is the sub-flavour independence
falsifier). No additional implementation-detail lit-pull commissioned.

Validation: V3-EXQ-545 substrate-readiness diagnostic (UC1 instantiation;
UC2 master-OFF backward-compat; UC3 sub-flavour flag-set isolation --
314a-only / 314b-only / 314c-only / all-off-master-on each behave correctly,
which is the architectural prerequisite making Q-044 three-arm ablation a
flag-set decision; UC4 select_action wiring contract; UC5 MECH-094
simulation gate). 5/5 PASS smoke 2026-05-10 (manifest scrubbed; runner
will write the canonical PASS manifest from the queued entry).

Contract tests: `tests/contracts/test_mech_314_curiosity.py` 13/13 PASS
(C1 default-off no-op; C2 each sub-flavour fires independently; C3
additive composition; C4 MECH-094 simulation gate; C5 backward-compat
config matrix; reset clears LP buffer + diagnostics; input validation).
Full contracts suite 273/273 PASS (was 253 + 13 new + 7 preflight
unchanged) -- regression-clean; bit-identical OFF guarantee holds.

Status: claims.yaml MECH-314 + MECH-314a + MECH-314b + MECH-314c
all `candidate -> candidate_substrate_landed`; v3_pending: true retained
on all four pending Q-044 three-arm ablation. `evidence_quality_note`
on each entry extended with the substrate-landing implementation note +
Phase-1 honest-scoping caveat for the broadcast-scalar sub-flavours.

Out of scope (separate spawned tasks):
- MECH-318 (rule-state abstraction substrate -- ARC-064 child).
- MECH-319 (simulation-mode rule-write gating).
- Q-043 weight calibration sweep.
- Q-044 three-arm ablation experiment itself (queued AFTER substrate
  landing AND MECH-318/319 absorption checks).
- Q-045 4-arm ablation experiment (MECH-313 vs MECH-260 collapse).
- V3-EXQ-543c (curiosity + meta-RL recurrent baselines arm class).
- Phase 2 per-candidate refinement of 314b/c.

Files touched (this session):
- ree-v3/ree_core/policy/structured_curiosity.py (new, ~330 lines).
- ree-v3/ree_core/policy/__init__.py (export).
- ree-v3/ree_core/utils/config.py (REEConfig fields + from_dims kwargs).
- ree-v3/ree_core/agent.py (import + __init__ instantiation + reset hook
  + select_action score_bias composition + LP feed after e3.select).
- ree-v3/tests/contracts/test_mech_314_curiosity.py (new, 13 tests).
- ree-v3/experiments/v3_exq_545_mech314_structured_curiosity_substrate_readiness.py (new).
- ree-v3/experiment_queue.json (V3-EXQ-545 appended).
- REE_assembly/docs/architecture/mech_314_structured_curiosity_bonus.md (new).
- REE_assembly/docs/claims/claims.yaml (MECH-314 + 314a/b/c status +
  evidence_quality_note + parent notes update).
- REE_assembly/docs/assets/data/claims.json (rebuilt by build_claims_json.py).
- REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
  (GAP-H row + this decision-log entry).
- WORKSPACE_STATE.md, TASK_CLAIMS.json.

### 2026-05-10 - GAP-H partial close: MECH-313 noise-floor substrate landed

First of the four ARC-065 child substrates (MECH-313 noise-floor / MECH-314
structured-curiosity / MECH-318 / MECH-319) landed. Resolves the Pull 1
SYNTHESIS R2 LOAD-BEARING tag for the LC-NE-tonic analog channel; remaining
ARC-065 children continue as separate spawned tasks.

Substrate:
- Module: `ree-v3/ree_core/policy/noise_floor.py` (NoiseFloor + NoiseFloorConfig).
  Pure-arithmetic regulator (no learned parameters; no nn.Module inheritance);
  matches the SD-035 / SD-036 / SD-037 regulator pattern.
- Algorithm at the e3.select() call site in REEAgent.select_action():
  `effective_T = max(baseline_T + noise_floor_alpha, noise_floor_min_temperature)`.
- Config: `REEConfig.use_noise_floor` (default False; bit-identical OFF) +
  `noise_floor_alpha` (default 0.1; SAC-entropy-bonus analog) +
  `noise_floor_min_temperature` (default 1.0; matches existing E3 baseline).
  Wired through `REEConfig.from_dims()`.
- MECH-094 honoured via `compute_effective_temperature(simulation_mode=True)`
  returning baseline unchanged + simulation-skip counter only.

Phase-1 instantiation choice (NOT a settled architectural commitment) --
deviation from the original notes-field implementation hint ("SAC-style
entropy regularisation in the existing GatedPolicy module's per-head
softmax temperature; one-line config addition; no separate substrate
component required"): a SEPARATE NoiseFloor module at the e3.select()
call site rather than per-head temperature inside GatedPolicy. Phase-1
reasoning: MECH-313 is state-independent and currently must fire on
baseline E3 selection too (which the per-head approach inside GatedPolicy
would miss with GatedPolicy disabled). Whether the policy-layer regulators
ultimately consolidate into one module is OPEN pending MECH-314 /
MECH-318 / MECH-319 implementations -- those substrates may make different
placement choices that motivate revisiting MECH-313's placement (MECH-314
structured-curiosity in particular may fit naturally inside GatedPolicy
as a per-head bonus, in which case MECH-313 may want to co-locate). Re-
evaluate at the point Q-045's 4-arm ablation is queued (i.e. once MECH-314
is also landed and the whole ARC-065 surface is visible). The Phase-1
module surface + config knobs are stable; what could move is the file
location and call site. Hint updated in claims.yaml notes field with the
same softening.

Validation:
- V3-EXQ-544 substrate-readiness diagnostic, 5/5 PASS smoke (UC1
  instantiation; UC2 master-OFF backward-compat; UC3 lift-arithmetic
  sweep across alpha/min_temperature; UC4 select_action wiring contract
  via act_with_split_obs; UC5 MECH-094 simulation gate). Manifests
  scrubbed; runner will write the canonical PASS manifest from the
  queued entry.
- 11 contract tests in `tests/contracts/test_mech_313_noise_floor.py`
  PASS; full contracts suite 253/253 PASS (regression-clean -- bit-
  identical OFF guarantee holds).

Status: claims.yaml MECH-313 `status: candidate -> candidate_substrate_landed`
with `v3_pending: true` retained until Q-045 behavioural validation runs.
Design doc `REE_assembly/docs/architecture/mech_313_stochastic_noise_floor.md`
landed.

What this enables:
- Q-045 4-arm ablation (both-OFF / 313 only / 260 only / both ON) on
  V3-EXQ-543b/c successors -- the falsifier of whether MECH-313 and
  MECH-260 collapse into a single anti-monostrategy substrate.
- Q-043 parametric sweep on `noise_floor_alpha` and
  `noise_floor_min_temperature` (downstream of Q-045 if MECH-313 is
  shown load-bearing).
- The 2026-05-10 sleep-substrate reclassification cohort (V3-EXQ-418m /
  436b / 500b / 503b) gains one of the two upstream channels needed
  for non-degenerate waking diversity.

Out of scope (separate spawned tasks):
- MECH-314 / MECH-314a/b/c structured-curiosity substrates.
- MECH-318 / MECH-319 substrates.
- The Q-045 4-arm ablation experiment itself (queued AFTER MECH-314
  also lands so the 4-arm matrix can be exercised meaningfully).

Files touched: `ree-v3/ree_core/policy/noise_floor.py` (new),
`ree-v3/ree_core/policy/__init__.py` (export), `ree-v3/ree_core/utils/config.py`
(REEConfig fields + from_dims kwargs), `ree-v3/ree_core/agent.py` (import +
__init__ instantiation + reset hook + select_action e3.select effective-T
override), `ree-v3/tests/contracts/test_mech_313_noise_floor.py` (new, 11
tests), `ree-v3/experiments/v3_exq_544_mech313_noise_floor_substrate_readiness.py`
(new), `ree-v3/experiment_queue.json` (V3-EXQ-544 appended),
`REE_assembly/docs/architecture/mech_313_stochastic_noise_floor.md` (new),
`REE_assembly/docs/claims/claims.yaml` (MECH-313 status + notes update),
`REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md` (GAP-H
status row + this entry), `REE_assembly/WORKSPACE_STATE.md`,
`REE_Working/TASK_CLAIMS.json`.

### 2026-05-10 - Pending FAIL triage: ARC-065 dependents reclassified non_contributory

Triggered by user observation: with ARC-065 (behavioral-diversity-generation
pathway) registered as a foundational upstream cluster on 2026-05-10, a number
of completed experiments that appeared to have FAILed are actually
non_contributory because they require behavioural diversity AS INPUT (not as
output) and the agent is presently in monomodal collapse without ARC-065
substrate landed.

Reclassifications (all in REE_assembly/evidence/experiments/):

- **V3-EXQ-418l** (SD-017 sleep action_bias_div discriminative pair):
  with_action_bias_div = without_action_bias_div = 0.000450 bit-identical
  every seed; signed_diff = 0.0; abs_diff = 0.0; slot_diversity also
  bit-identical. Sleep cannot diversify what was never diverse.
  Reclassified `evidence_direction: weakens -> non_contributory`.
- **V3-EXQ-436a** (SD-017 + ARC-045 + MECH-166 sleep refinement of
  context-conditioned harm threshold): waking and SWS_THEN_REM produced
  bit-identical slot_cosine_sim and harm_rate_dangerous in every seed
  (seed 42: waking 0.000966 = SWS_THEN_REM 0.000966 for slot; waking
  0.003697 = SWS_THEN_REM 0.003697 for harm_dang). Sleep refinement of
  bit-identical waking content can only produce bit-identical sleep
  content. Reclassified `evidence_direction: weakens -> non_contributory`
  for all three claims.
- **V3-EXQ-530c** (ARC-016 dynamic-precision precision-to-commit pathway):
  ARM_0 (use_dacc=False) and ARM_1 (use_dacc=True) bit-identical at
  commit_rate=1.0 and precision=211.85. Precision-to-commit pathway
  cannot register signal under saturated commit policy. Reclassified
  `evidence_direction: weakens -> non_contributory`. Supersedes the
  morning-digest /diagnose-errors deferral with the upstream-substrate
  explanation; Q-042 contract test C0 (rv differs from precision_init)
  was passed -- the issue is downstream behavioural saturation, not
  rv liveness.

NOT reclassified -- one pending FAIL:

- **V3-EXQ-141d** (MECH-111 novelty drive ablation): per_seed_action_
  divergence ~56% (actions DO diverge), but mean_entropy_gap = 7.4e-15
  and mean_cell_gap = -0.67. This experiment IS the diversity-generator
  test, not a diversity consumer. Kept `evidence_direction: weakens`
  against MECH-111 specifically (falsifies the strong reading: novelty-
  bonus-alone-produces-diversity), but added cross-link note tying its
  FAIL pattern to ARC-065 R1 BOTH-CHANNELS-NEEDED verdict (novelty
  bonus alone insufficient without LC-NE-tonic noise floor MECH-313).
  Read together with the cluster registration, this run is informative
  evidence FOR the multi-channel cluster shape.

Precedent for the pattern: SD-029 retest cohort (V3-EXQ-433 / 433a /
433b / 470 reclassified non_contributory 2026-04-25 .. 2026-05-08
because monomodal policy could not generate balanced agent-vs-env
event distributions for C2 / C3 measurement; substrate -- scheduled_
external_hazard env knob -- was in place). Today's reclassification
generalises that precedent from "substrate-not-generating-balanced-
events" to "substrate-not-generating-behavioural-diversity-period",
which is the ARC-065 cluster's whole reason to exist.

How this came about (root-cause reflection): ARC-065 was registered
2026-05-10 (today) but the experiments above were authored across
2026-05-08 .. 2026-05-09, before the cluster existed. The sleep_
substrate_plan.md GAP-2 owner-EXQ list (265a + 418l + 436a + 500a +
503a) was framed against an implicit assumption that the agent would
have natural waking diversity for sleep to refine. The 543/543b
sequence and the cluster registration revealed that the assumption
was load-bearing and not yet substantiated. There is no question of
"work that should have been blocked" in a strict sense -- the gating
claim (ARC-065) did not exist when the experiments were authored.
What was missing was a registered upstream behavioural-diversity
precondition. Now that ARC-065 is registered, we have the gate.

What is now blocked given ARC-065:

| Plan / cohort | Blocking | Resume condition |
|---|---|---|
| sleep_substrate_plan.md GAP-2 (Phase 2 owner-EXQ list 418l + 436a + 500a + 503a) | upstream-blocked by ARC-065 substrate | V3-EXQ-543b/c PASS demonstrating non-degenerate behavioural diversity in waking phase, then re-queue 418m / 436b / 500b / 503b under the diversity-substrate stack |
| arc_062 GAP-B (already ran_inconclusive) | already in V3-EXQ-543b pickup | unchanged -- 543b is the falsifier path |
| arc_062 GAP-C / GAP-D (Phase 3 wiring) | downstream of GAP-B / V3-EXQ-543b PASS | unchanged |
| Future ARC-016 / dACC precision-to-commit retests | upstream-blocked by ARC-065 substrate | ARC-065 substrate produces non-degenerate cross-seed commit-rate variation, then re-queue V3-EXQ-530d |
| Future SD-029 retests | upstream-blocked by ARC-065 (and MECH-269 V_s -- pre-existing) | ARC-065 + MECH-269 V_s both landed |

Sub-plan note for rule apprehension: ARC-065 cluster is a SIBLING
plan to arc_062 rather than a sub-plan. The dependency direction is
ARC-065 (foundational, depends_on []) -> ARC-062 (top-down rule
selection, presupposes diversity to choose between) and ARC-064
(bottom-up rule extraction, presupposes diversity to extract patterns
from). The arc_062 plan-doc currently contains the cluster
registration in its decision log (2026-05-10 entry above this one);
if ARC-065 / ARC-064 substrate work grows beyond what the arc_062
status table can absorb, the appropriate move is to spin up
`arc_065_behavioral_diversity_plan.md` and `arc_064_bottom_up_rule_
extraction_plan.md` as siblings to this plan, with cross-plan-link
fields wiring them into the gap inventories. Defer until V3-EXQ-543b
PASS clarifies which substrate ARC-065 actually needs.

Files touched: REE_assembly/evidence/experiments/v3_exq_418l_*,
v3_exq_436a_*, v3_exq_530c_*, v3_exq_141d_* manifests
(evidence_direction + evidence_direction_per_claim +
evidence_direction_note); REE_assembly/evidence/experiments/review_
tracker.json (4 reviewed_run_ids appended; last_review_utc forwarded;
discussion_notes session-block appended); arc_062_rule_apprehension_
plan.md (this entry); sleep_substrate_plan.md (GAP-2
upstream-block note); WORKSPACE_STATE.md; TASK_CLAIMS.json.

### 2026-05-10 - Cluster registration session: ARC-064 + ARC-065 + MECH-312 sub-MECH split + MECH-319 registered

Major architectural commitment session. Eighteen new claim entries
landed in `docs/claims/claims.yaml` (claims.json count 591 -> 609);
governance pipeline ran clean (1017 runs / 1278 lit entries / 282
proposals; 7 indexed pending review). No experiment scripts written
this session per scope-discipline (V3-EXQ-543b/c authoring is the next
session).

**New cluster anchors (architectural commitments, both v3_pending):**

- **ARC-065** — `behavioral_diversity_generation_pathway`
  (multi-substrate distributed: LC-NE tonic + frontopolar curiosity
  + striatal novelty + hippocampal trajectory sampling). Per Pull 1
  PROMOTE-TO-CLUSTER (conf 0.82) + Pull 4 R4 HYBRID-naming. Logically
  upstream of both ARC-062 top-down and ARC-064 bottom-up rule
  pathways: trainers do not invent diversity any more than they
  invent rules.
- **ARC-064** — `bottom_up_behavioral_pattern_extraction_pathway`
  (hippocampal_CLS_bi_pathway + dorsolateral_striatum_chunking +
  OFC_cognitive_map analog). Per Pull 2 PROMOTE-AS-SEPARATE-CLUSTER
  (conf 0.84) + Pull 4 R4 HYBRID-naming. Architectural counterpart
  to ARC-062: where ARC-062 receives a context cue and selects a
  policy mode, ARC-064 receives observed-behaviour and extracts
  cross-episode regularities. Both presuppose ARC-065 upstream.

**New mechanism claims (all candidate, v3_pending):**

ARC-065 children:
- **MECH-313** — `stochastic_noise_floor` (max_entropy_policy_
  regularisation_LC_NE_tonic_analog). Distinct from MECH-260 dACC
  anti-recency; Q-045 falsifies the collapse question.
- **MECH-314** — `structured_curiosity_bonus`
  (frontopolar_uncertainty_driven_exploration_expected_free_energy_
  analog). Parent of three sub-flavours that Pull 1 R3 explicitly
  recommended NOT to collapse prematurely:
  - **MECH-314a** novelty_bonus_striatal_analog (Wittmann 2008)
  - **MECH-314b** uncertainty_driven_curiosity_frontopolar_analog
    (Daw 2006 + Friston EFE)
  - **MECH-314c** learning_progress_curiosity_intrinsic_motivation_
    analog (Schmidhuber/Pathak; least biologically anchored —
    flagged as potentially-discardable if 314a + 314b suffice)

ARC-064 children:
- **MECH-316** — `cross_episode_regularity_extraction`
  (episodic_RL_successor_representation_CLS_monosynaptic_analog;
  Schapiro 2017 + Stachenfeld 2017)
- **MECH-317** — `behavioural_pattern_compression`
  (option_formation_striatal_chunking_analog; Smith & Graybiel +
  Bacon/Harb/Precup option-critic)
- **MECH-318** — `rule_state_abstraction_substrate`
  (meta_RL_recurrent_task_state_representation; Wang 2018 + Duan
  2016 RL^2). Flagged registration_provisional_pending_meta_rl_
  absorption_check — may be absorbed into existing latent stack
  if V3-EXQ-543c absorption check shows the recurrent state
  already supports rule-state abstraction.

MECH-312 sub-MECH split (Pull 3 R5, conf 0.78):
- **MECH-312** (parent, reworded as
  `rule_arbitration_multi_variable_multi_channel_dynamic_within_
  session`) — registered as fresh parent claim with multiplicative-
  gate as architectural-default-pending-empirical-validation per
  Pull 3 R4 (conf 0.74); additive-logit baseline is the
  falsifying alternative in V3-EXQ-543b/c.
- **MECH-312a** uncertainty_reliability_weighting (Daw 2005 / Lee
  2014; LOW divergence)
- **MECH-312b** practice_maturity_weighting (Smith & Graybiel +
  Stachenfeld 2017 SR maturation; LOW-MEDIUM divergence)
- **MECH-312c** affective_stream_modulation_of_arbitration_REE_
  novel (SD-010/011 anchored structurally; functional consequence
  is REE-novel; MEDIUM-HIGH divergence)
- **MECH-312d** V_s_freshness_modulation_per_region_REE_novel
  (Behrens 2007 + Bouton 2004 nearest cousins; per-region scope
  + rule-trust function REE-novel; HIGH divergence)
- **MECH-312e** controllability/agency modulation (Gershman 2021
  anchor) — DEFERRED per Pull 3 R5 pending V3 substrate
  availability; flagged in MECH-312 evidence_quality_note.

REE-novel arbitration substrate:
- **MECH-319** — `simulation_mode_rule_write_gating_categorical_
  replay_tag` (SWR_machinery_substrate_REE_novel_function).
  Per Pull 3 R1 GENUINE-NOVELTY-CONFIRMED (conf 0.72) + Pull 4 R3
  KEEP-AS-IS. Substrate-availability premise is well-anchored
  (Joo & Frank 2018 SWR review + Foster & Wilson 2006 reverse
  replay); the specific REE function (categorical write-gate at
  the arbitration layer keyed to a simulation-mode tag) is the
  REE-novel claim. **MECH-094 NOT MODIFIED** per Pull 3 R1 + Pull 4
  R3 KEEP-AS-IS — MECH-094 names the architectural principle;
  MECH-319 is its substrate-level instantiation at the arbitration
  layer.

**New open questions:**
- **Q-043** — relative-weight calibration of MECH-313 vs MECH-314
  (parametric sweep on V3-EXQ-543b)
- **Q-044** — independence of MECH-314a/b/c sub-flavours (three-arm
  ablation; defer empirical resolution)
- **Q-045** — MECH-313 vs MECH-260 collapse question (4-arm
  ablation: both-OFF / 313-only / 260-only / both-ON on V3-EXQ-543b)

**MECH-315 absorption (no new claim):** Per Pull 2 R5 verdict (conf
0.74), MECH-315 candidate (proposal-diversity-channel via
hippocampal trajectory sampling, Pfeiffer & Foster 2013) is
ABSORBED into existing MECH-292 ranked ghost-goal bank + MECH-293
awake ghost-goal probes substrate. NOT registered as a separate
claim. Cross-reference notes added to MECH-292 + MECH-293
evidence_quality_note.

**HYBRID-naming convention rationale (Pull 4 R4):** Cluster claims
carry titles that name BOTH the REE-internal architectural-function
name AND the literature anchors, making the cluster machine-grep-
able under both REE-native search ("behavioral diversity",
"bottom-up rule discovery") and literature-search ("MaxEnt RL",
"frontopolar curiosity", "successor representation", "option-
critic", "OFC cognitive map", "contention-scheduling-arbitration").
Pull 4 R4 distributed claim names across KEEP-AS-IS (4 genuine REE
divergences), RENAME-TO-EXISTING (none applied this session — all
literature-anchored claims went HYBRID), and HYBRID (the bulk of
new registrations).

**DEFERRED candidates flagged for follow-up lit-pulls (NOT
registered as claims this session):**

- **Candidate MECH-320** — `interrupted_task_resumption_substrate`
  + V_s context-saving extension + reconciliation-rule Q-claim.
  Per memory entry `project_interrupted_task_resumption_gap.md`:
  REE has world-staleness invalidation but no Zeigarnik-style
  "agent was working on X, got interrupted, resume when capacity
  allows" mechanism. Anchors: Zeigarnik 1927 + Altmann & Trafton
  2002 + Cai 2009 + Mason & Macrae 2007 + Christoff 2009.
  Deferred from this registration session pending dedicated
  lit-pull commission.
- **Candidate ARC-XXX** — `imagination_learning_constraint_
  principle`. Per memory entry `project_imagination_learning_
  constraints.md`: explicit ARC-level commitment articulating
  LICIT (consistency, plan-optimisation, schema integration) vs
  FORBIDDEN (world-model updates, prediction validation, novel-
  fact generation) classes of learning from imagination.
  Currently implicit in MECH-094 / MECH-272 / MECH-273 substrate
  gating; needs explicit articulation as architectural commitment.
  Anchors: Stickgold 2013 + Cai 2009 + Schapiro 2017 CLS +
  confabulation literature + FEP epistemic value. Deferred
  pending dedicated lit-pull commission.

**Forward link.** V3-EXQ-543b and V3-EXQ-543c are the next-session
authoring targets via `/queue-experiment` skill. V3-EXQ-543b is
the noise-floor + gating arm class (Q-043 weight sweep + Q-045
4-arm ablation + multiplicative-gate vs additive-logit baseline);
V3-EXQ-543c is the curiosity + meta-RL recurrent baselines arm
class (MECH-314a/b/c absorption check + MECH-318 latent-stack
absorption check). Per Pull 4 R5 sequencing recommendation, the
two scripts split the original V3-EXQ-543b 5-arm protocol so
each script remains reviewable and falsifiable in isolation.

**Status table updates.** Five new gap rows registered (GAP-H
ARC-065 cluster + GAP-I ARC-064 cluster + GAP-J MECH-312-cluster +
GAP-K MECH-319 + status-value `registered` introduced for
claims-registered-but-experiments-not-yet-queued items).

**Cross-references.** ARC-063 V4 strong-reading evidence_quality_
note still references MECH-310/311/312/313 sub-claims-to-register
placeholder list; that placeholder list is now stale (MECH-312/313
are registered with different functional content per Pull 1-4
verdicts). Out of scope for this session per the prompt's "DO NOT
MODIFY MECH-094" rule (which extended in spirit to ARC-063 stale
cross-references); flag for separate cleanup session.

### 2026-05-10 - V3-EXQ-543b authored + queued (Phase 3-corrected falsifier)

V3-EXQ-543b authored same session as the reclassify decision. Script
`ree-v3/experiments/v3_exq_543b_arc062_phase3_optimized_falsifier.py`
implements the four corrections from the reclassify entry (CORRECTION A
gated_policy params in optimizer; CORRECTION B phased training P0=40 / P1=60 /
P2=8; CORRECTION C behavioral-divergence probe with mid-training inert-gating
short-circuit; CORRECTION D hardened C3 with transit-rate floor and nanmean).

P1 training-pressure honest scope. Per the design-trade discussion in this
session: rigorous REINFORCE on environmental reward would require accessing
E3 raw candidate scores at decision time and re-running gated_policy forward
with grad on cached features at episode end -- doable but adds significant
agent.py modification surface for one experiment. The 543b script instead
uses a SCAFFOLDING DIVERSIFICATION LOSS in P1 (negative head-pair output L2
+ negative discriminator output variance, sampled over a static probe buffer
collected during P0). This guarantees gated_policy parameters MOVE under any
non-trivial gradient pressure, satisfying the "in optimizer" requirement
from the reclassify spec. The behavioral-divergence probe (CORRECTION C) is
the architectural test: does the parameter movement translate to
context-conditional behavioral divergence on SD-054? If yes, the C2/C3/C4
acceptance grid applies. If no (probe TV-distance below 0.05 at mid-P1),
the seed/arm is marked non_contributory_inert_gating. Full REINFORCE-on-
environmental-reward is deferred to Phase 3 GAP-C/D when the discriminator
is wired into SD-033a LateralPFCAnalog.update() and the bias head joins the
composite E3 optimizer (commitment_closure GAP-1).

Smoke verification (`--dry-run`, p0_eps=3 / p1_eps=4 / p2_eps=2,
steps_per_episode=30, 3 seeds x 2 arms): script runs end-to-end in 175s,
manifest writes correctly, sentinel emitted, ARM_1c probe collects 32 states
with applicable=True. Probe mean_tv=0.0 in dry-run is expected (only 4 SGD
steps total; contract test C4 needed 200 SGD steps to see >5x head
divergence). Full run has P1=60 episodes x 4 SGD steps/ep = 240 steps,
above the 200 demonstrated to produce divergence.

Substrate readiness: ARC-062 GatedPolicy (landed 2026-05-09 GAP-A done) is
the only V3 substrate this experiment depends on. No additional substrate
work required. The MECH-313 / MECH-314 / MECH-318 / MECH-319 substrate gap
identified in the cluster-registration session is NOT in this experiment's
scope -- per the reclassify spec, V3-EXQ-543b is the corrected Phase 2
falsifier on the existing GatedPolicy substrate alone. The cluster-
registration session's expanded V3-EXQ-543b/c definitions (Q-043 noise-
floor sweep, Q-045 4-arm ablation, MECH-314a/b/c absorption check, MECH-318
absorption check) are deferred to follow-on experiments after the
underlying substrate lands via /lit-pull + /implement-substrate sessions
for MECH-313, MECH-314 (a/b/c), MECH-318, MECH-319.

Queue entry: Mac (DLAPTOP-4.local), priority=2, estimated_minutes=120,
episodes_per_run=108, seeds=3, conditions=2, supersedes=V3-EXQ-543. Smoke
PASS; validate_queue OK.

Status table updated: GAP-B `ran_inconclusive -> queued`; owner-EXQ
V3-EXQ-543b retained.

### 2026-05-10 - GAP-B reclassified non_contributory; jump to Phase 3 design (V3-EXQ-543b)

V3-EXQ-543 ran (3062s elapsed, manifest
`v3_exq_543_arc062_phase2a_monomodal_collapse_falsifier_20260509T214517Z_v3.json`).
Script declared `outcome=PASS, pass_rule_met=true (n_criteria_passed=2: C3+C4)`.
On review the PASS was reclassified `non_contributory` for all three tagged
claims (MECH-309, ARC-062, SD-029). Three independent issues, each sufficient
on its own to disqualify the result as a falsifier of MECH-309:

1. **C3 (risk-type dissociation) is a divide-by-near-zero artifact.** ARM_1c
   seed 0 had `transit_hazard_rate=0.0` (zero transit-regime hazards), so
   `risk_type_ratio = forage_rate / ~0 = 74883`. The arm-mean (24961) is
   dominated by that single seed. Per-seed ratios for ARM_1c are
   `[74883, 0.022, 0.024]` -- two of three seeds are *below* ARM_0's mean of
   0.082. C3 measured degenerate-trajectory geometry, not a behavioral
   dissociation between forage and transit risk weighting.
2. **ARM_1c seed 2 is byte-identical to ARM_0 seed 2.** Every reported metric
   matches exactly: mean_reef_fraction (0.26598), rho_drive_vs_reef (-0.0283),
   hazard rates, n_steps, per_episode_reef_fractions, warmup rewards. With
   gated_policy params intentionally NOT in the optimizer (Phase 2a tested
   structural-sufficiency-at-init) and `disc_init_scale=0.1` producing
   sigmoid-near-0.5 gating, the gating layer was inert for this seed -- the
   same RNG stream produced identical trajectories. The "random init breaks
   symmetry" assumption was too weak.
3. **C2 (state dependence) -- the criterion most directly tied to MECH-309's
   rule-apprehension prediction -- FAILED.** ARM_1c mean_abs_rho=0.111 vs
   ARM_0=0.291; the gated arm shows *less* state-dependent reef behavior, not
   more. ARM_1c per-seed reef-fractions `[0.0, 0.0006, 0.266]` indicate seeds
   0/1 abandoned reef-foraging entirely while seed 2 was the inert-gating
   clone of baseline.

**Design defect.** Phase 2a-at-init tested whether a randomly-initialised
gating layer could produce structural sufficiency without training. That is
not what MECH-309 predicts -- MECH-309 says trainers / agents *weight rules
they do not invent*, which means rule apprehension is a learning-time
acquisition under selection pressure, not an at-init property. With untrained
gating + sigmoid-near-0.5 init, the only two outcomes available were
(i) inert gating clones baseline (seed 2) or (ii) random-init noise disrupts
baseline without producing context-conditional behavior (seeds 0/1). Neither
falsifies MECH-309. Phase 2b density-gradient and Phase 2b R1 input-ablation
sub-arms inherit the same defect and are skipped.

**Skip-to-Phase-3 decision.** Successor V3-EXQ-543b becomes GAP-B owner and
moves directly to Phase 3 design: gated_policy params *in* the optimizer,
phased training schedule, with the additional instrumentation from session
feedback below. GAP-C and GAP-D scopes partially absorb into 543b
(specifically: gated_policy + bias-head added to E3 optimiser is a
prerequisite of any meaningful training-time test of MECH-309). Remaining
GAP-C work after 543b PASS is the explicit `LateralPFCAnalog.update()`
wiring of the discriminator output.

**Session feedback -- "rough-and-ready behavioral divergence check."** The
session insight: if rule apprehension is itself a *quick rough-and-ready
rule* (the MECH-309 framing), then we are missing a *quick rough-and-ready
means of ensuring the rule apprehended is behaviourally different.* The
EXQ-543 result demonstrates the gap: end-of-run reef-fraction / rho /
risk-ratio statistics are too far downstream to detect inert gating until
~50 minutes of compute have been spent. Worse, when they do detect it, the
signal is contaminated by random-init disruption.

V3-EXQ-543b will add a **behavioral-divergence probe**: every N training
episodes (default N=5), sample policy action distributions at a fixed set of
probe states under (a) `use_gated_policy=True` and (b) the baseline policy,
then report mean action-mismatch rate (or KL divergence). The probe states
should span the SD-054 reef context (high-density reef, transit corridor,
mixed) so that any context-conditional gating shows up as divergence on the
context-discriminative subset and convergence elsewhere. Pre-registered
inert-gating threshold: if mean mismatch rate stays below 0.05 by mid-
training, flag the run as inert-gating and short-circuit (mark
`non_contributory: inert_gating_detected_during_training`). This is the
"rough-and-ready" instrumentation -- it does not assert MECH-309 itself, but
it ensures the substrate is actually generating differentiable behavior
before the downstream falsifier metrics are even read.

Acceptance for V3-EXQ-543b: same C2/C3/C4 + F1/F2 grid as 543, *plus* the
divergence-probe gate. Run is `non_contributory` if probe gate fails
(inert gating, no behavioral signal to interpret). Run is a clean falsifier
attempt if probe gate passes (mean mismatch >= 0.05 by mid-training across
seeds), in which case C2/C3/C4/F1/F2 are interpreted on their original
acceptance grid. C3 dissociation calculation will be hardened against the
divide-by-near-zero artifact (require `transit_hazard_rate > 0.05` for the
per-seed ratio to enter the arm-mean; otherwise the seed contributes
`np.nan` and the arm-mean uses `np.nanmean`, with seed-count reported).

Status table updated: GAP-B `queued -> ran_inconclusive`, owner-EXQ shifted
to V3-EXQ-543b (to be queued same session). GAP-C/GAP-D last-updated
forwarded to 2026-05-10 with the partial-absorption note.

### 2026-05-09 - GAP-A done (Phase 1 substrate landed; V3-EXQ-542 5/5 PASS)

Phase 1 substrate landed. New module
[ree-v3/ree_core/policy/gated_policy.py](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/policy/gated_policy.py)
implements `GatedPolicy` (N=2 scoring heads sharing E3 candidate features +
3-stream context discriminator on `(z_world, z_self, z_harm_a)`) plus
`GatedPolicyConfig` and `GatedPolicyOutput`. Symmetry-broken init on the
heads' last-Linear bias (+/- `head_init_bias_offset` default 0.05) so the
two heads can differentiate from step 0 under any training pressure.
`disc_init_scale=0.1` keeps the discriminator output near 0.5 at init,
avoiding early head over-commitment.

REEConfig flag `use_gated_policy` (default False, bit-identical OFF) wired
through `REEConfig.from_dims` with per-knob defaults (`gated_policy_n_heads=2`,
`gated_policy_disc_hidden=24`, `gated_policy_disc_init_scale=0.1`,
`gated_policy_head_hidden=32`, `gated_policy_bias_scale=0.1`,
`gated_policy_head_init_bias_offset=0.05`).

REEAgent wiring composes `gated_policy_score_bias` additively into
`dacc_score_bias` immediately before the MECH-295 block, parallel to the
dACC / lateral_pfc / ofc composition pattern. **No connection to SD-033a
in Phase 1** -- that wiring is Phase 3 (closes commitment_closure GAP-1)
per the plan-of-record. Per-episode `reset()` clears diagnostic counters
on the GatedPolicy module (no persistent state to clear; module is
stateless across ticks).

5 contract tests in
[ree-v3/tests/contracts/test_gated_policy.py](https://github.com/Latent-Fields/ree-v3/blob/main/tests/contracts/test_gated_policy.py)
landed: C1 default-off no-op + C2 backward-compat + C3 discriminator output
in [0, 1] across diverse latents + C4 head differentiation under training
pressure (output-divergence metric, >5x growth on held-out batch after 200
SGD steps) + C5 MECH-094 simulation_mode gate. All 5 PASS; full ree-v3
preflight + contracts 249/249 PASS (244 prior + 5 new). Bit-identical OFF
guarantee verified.

V3-EXQ-542 substrate-readiness diagnostic 5/5 PASS (Mac runner,
2026-05-09T20:22:11Z, `v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z.json`).
Five sub-tests UC1-UC5 cover forward-pass instantiation, master-OFF
no-op, discriminator input sensitivity, head differentiation under
training pressure, and MECH-094 simulation gate. UC2 z_world pixel-match
across flag-off vs flag-on dropped from acceptance criteria because the
GatedPolicy `nn.Linear` inits consume the global RNG between paths so
the rest of the agent's randomly-initialised weights diverge by
construction; substrate-level backward-compat (flag OFF -> module is
None; flag ON -> module instantiates without raising; both sense() clean)
is the right contract at the substrate layer, and the pixel-level no-op
is exercised by contract test C1 against a single agent that never
instantiates GatedPolicy. UC3 threshold for discriminator output range
set to 0.001 (above floating-point noise floor; substantial discriminator
variation is a Phase-2 training signal, not a Phase-1 init signal --
disc_init_scale=0.1 deliberately keeps the sigmoid output flat near 0.5
at init).

GAP-A status `open` -> `done` in YAML frontmatter and body status table;
`last_updated` 2026-05-09; owner_exq populated as V3-EXQ-542. Phase 2
(GAP-B monomodal-collapse falsifier on SD-054) remains `open` and is the
next-thing-to-queue (separate session per the plan-of-record's six-phase
sequencing -- do not bundle Phase 2 EXQ in this same session).

Cross-plan link: commitment_closure_plan.md GAP-1 remains `blocked` on
both arc_062 GAP-A (now done) and arc_062 GAP-B (still open). GAP-1
unblock cascade requires Phase 2 PASS (then Phase 3 wires discriminator
into SD-033a `LateralPFCAnalog.update()` source vector + adds bias-head
parameters to E3 optimiser).

### 2026-05-09 - Plan registered

Plan-of-record `arc_062_rule_apprehension_plan.md` registered as a sibling
to `commitment_closure_plan.md` / `sleep_substrate_plan.md` /
`sd033_governance_plan.md` / `goal_pipeline_plan.md` /
`self_attribution_plan.md`. Seven gaps surfaced and sequenced into six
phases. R1 / R2 / R3 / R4 open questions resolved with biology-anchored
defaults from two preceding lit-pulls (Pull A targeted_review_arc_062_
rule_apprehension/ 8 entries 2026-05-09T19:19Z; Pull B
targeted_review_arc_062_refuge_forage_ecology/ 6 entries 2026-05-09T19:34Z).

Cross-plan link to `commitment_closure_plan.md` GAP-1 established: the
SD-033a bias-head training problem (load-bearing in commitment_closure)
is now reframed as downstream of this plan's Phase 3 (GAP-C + GAP-D).
The original commitment_closure GAP-1 Phase 1 deliverables are rewritten
to drop the oracle-supervised "rule-cue gridworld" curriculum (which
MECH-309 says cannot exist honestly in REE) in favour of joint training
through ARC-062's discriminator-driven gradient path.

substrate_queue.json edits: ARC-062 entry added with priority 2,
ready=true, status=candidate_v3_pending, design_doc pointing at this
plan, implementation_hint summarising Phase 1 deliverables. MECH-309 and
ARC-063 are diagnostic / V4-deferred and do not need substrate_queue
entries.

The closure-tab visualisation will pick up this plan automatically as a
new column on the next /api/closure poll.

### 2026-05-08 - Cluster registered (pre-plan)

MECH-309 / ARC-062 / ARC-063 cluster registered in claims.yaml from the
SD-054 substrate-purpose-validation discussion. SD-054 substrate carried
behavioural diversity under heuristic policy (V3-EXQ-522 substrate-
ceiling PASS) but every SD-029 retest under trained policy
(V3-EXQ-433e/433f/523/523a/523b) returned non_contributory for the same
reason: insufficient agent-caused trials, monomodal V_s monostrategy
substrate-ceiling pattern. Diagnosis: substrate is not the bottleneck;
the trained policy lacks a rule-apprehension layer. MECH-309 reframes
monomodal collapse from a training failure into the predicted equilibrium
output of an architecture whose only learners are updaters.

---

## Cross-plan link with commitment_closure_plan.md

This plan and `commitment_closure_plan.md` share two load-bearing claims:

1. **SD-033a bias head training (commitment_closure GAP-1).** The
   commitment_closure plan's Phase 1 originally proposed a phased pre-
   training-on-rule-cue-curriculum approach. That approach presupposed
   an oracle `rule_cue_id` label that the architecture (per MECH-309)
   says cannot exist honestly in REE. With ARC-062 in place, the bias
   head trains jointly with E3 via the existing score-aggregation
   gradient path, with the rule signal arriving from ARC-062's
   discriminator rather than from an oracle. The commitment_closure
   GAP-1 row is reframed as `blocked` on this plan's GAP-A and GAP-B.

2. **MECH-094 / MECH-261 mode-conditioning generalisation.** The MECH-261
   write-gate registry on SD-032a SalienceCoordinator generalises the
   MECH-094 hypothesis-tag write gate to the apprehension layer. ARC-062
   discriminator output flows through this same registry (when wired to
   SD-033a's `update()` per Phase 3, the gate-modulated EMA on
   `rule_state` consumes `write_gate("sd_033a")` which is itself mode-
   conditioned). Internal-replay mode (`write_gate("sd_033a") = 0.05`)
   blocks the apprehension layer from updating on replay content -- the
   same MECH-094 invariant the closure operator relies on.

Sessions that touch *both* plans (e.g. discriminator-output-routing
to the closure operator's mode-conditioning gate) should update the
[Status table](#status-table) on both this plan and the commitment_
closure plan.

---

## Resume ritual

When picking up rule-apprehension cluster work after a deviation:

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
7. If the work touches the [commitment_closure_plan.md](./commitment_closure_plan.md)
   cross-link concerns (SD-033a bias head training, MECH-261 mode-
   conditioning), update both plans' status tables.

Sessions that do NOT touch rule-apprehension cluster work do not need to
read this document. Sessions that DO touch this work read this document
before any code or experiment edit.

---

## See also

- [evidence/planning/commitment_closure_plan.md](./commitment_closure_plan.md) — sibling plan; GAP-1 SD-033a bias head training is downstream of this plan's Phase 3
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) — sibling plan; GAP-G cross-link for sleep-vs-waking refinement (V4 deferred)
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) — OCD-specific test-battery sub-plan (sibling to commitment_closure)
- [evidence/planning/self_attribution_plan.md](./self_attribution_plan.md) — sibling plan
- [evidence/planning/goal_pipeline_plan.md](./goal_pipeline_plan.md) — sibling plan
- [evidence/planning/substrate_queue.json](./substrate_queue.json) — ARC-062 entry added by this plan registration
- [evidence/literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md](../literature/targeted_review_arc_062_rule_apprehension/SYNTHESIS.md) — Pull A 8 entries (R1 / R2 / R3 verdicts)
- [evidence/literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md](../literature/targeted_review_arc_062_refuge_forage_ecology/SYNTHESIS.md) — Pull B 6 entries (R4 verdict)
- [docs/architecture/rule_apprehension_layer.md](../../docs/architecture/rule_apprehension_layer.md) — 2026-05-04 thought-intake
- [docs/architecture/sd_054_reef_enrichment_substrate.md](../../docs/architecture/sd_054_reef_enrichment_substrate.md) — SD-054 reef substrate spec
- [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) — SD-033a substrate spec (Phase 3 wiring target)
