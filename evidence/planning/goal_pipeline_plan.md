---
closure_plan:
  id: goal_pipeline
  title: "Goal Pipeline (wanting / liking / drive cascade)"
  registered: 2026-05-08
  last_updated: 2026-06-15
  scope_claims: [SD-012, SD-014, SD-015, SD-018, SD-049, MECH-117, MECH-216, MECH-229, MECH-230, MECH-295, MECH-306, MECH-307, MECH-455, ARC-030, ARC-032, ARC-036, ARC-051]
  related_threads:
    - thread: goal_maintenance_feedback
      claims: [INV-086, MECH-426, MECH-427, INV-087, ARC-105, MECH-428]
      registered: 2026-06-12
      gap2_link: >
        MECH-428 (subgoal_bootstrapped_goal_seeding, EXP-0390) directly addresses
        this plan's GAP-2 blocker: when DIRECT z_goal seeding is sparse (unscaffolded
        z_goal_norm < 0.1 -- the foraging/benefit-contact-ceiling failure), reliably-
        attainable subgoals + MECH-427 cross-level credit can BOOTSTRAP the z_goal
        attractor bottom-up, measured against the 626b forced-seed positive control.
        INV-086 was widened 2026-06-12 to a TWO-AXIS fragility claim (sparse feedback
        = maintenance fragility; sparse SEEDING = formation fragility) so the umbrella
        covers MECH-428's formation direction.
      note: >
        Long-horizon goal-MAINTENANCE cluster (distinct from the reachability spine
        INV-065/MECH-216/217/ARC-051 this plan already scopes), reaped 2026-06-12 from
        the proxy/progress intake and lit-grounded by
        evidence/literature/targeted_review_proxy_progress_goal_maintenance.
        INV-086 = umbrella (feedback-scaffolded maintenance, scoped PAST MECH-116
        working-memory maintenance); MECH-426 progress-velocity (folds on-path
        inference; EXP-0384); MECH-427 cross-level subgoal-credit (EXP-0385);
        INV-087 proxy-tethering/Goodhart guard (EXP-0386, V3-EXQ-674 E3-probe family);
        ARC-105 granularity-matched hierarchy (V4, substrate_conditional). NOT
        gap-owned -- tracked here for goal-pipeline locality; promote to a GAP node
        only if one becomes a closure blocker.
  nodes:
    - id: "goal_pipeline:GAP-1"
      title: "MECH-307 anticipatory-affect conjunction architecture"
      status: done
      severity: load-bearing
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      unblocks_claims: [MECH-307, SD-014]
      depends_on: []
      last_updated: 2026-05-21
      completion_note: "Substrate landed 2026-05-11. Gap 1 Option-b split channels; Gaps 2/3/4 2026-05-08. Canonical substrate-readiness V3-EXQ-540g PASS 2026-05-15. substrate_queue closed IGW-20260521-023 2026-05-21. GAP-2/GAP-4 behavioural retests are downstream queue items."
    - id: "goal_pipeline:GAP-2"
      title: "SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      unblocks_claims: [SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030]
      depends_on: ["goal_pipeline:GAP-1"]
      cross_plan_link: ["infant_substrate:GAP-14"]
      blocked_by: "CLEARED. The foraging-competence / benefit-contact ceiling that previously blocked this node was de-risked by the SD-057 channel-write clearance (V3-EXQ-681 PASS) and then exercised end-to-end by V3-EXQ-514o, which ported the full 603n lever stack so contact + WL-channel-write fire during real foraging (n_scored_wl_steps 5/6/7) -- the L9 wanting!=liking dissociation now scores 0.80 behaviourally."
      last_updated: 2026-06-15
      governance_2026_06_15b: "MECH-229 CLAIM-STATUS follow-on (does NOT reopen this node; GAP-2 stays done -- the closure was on the 514o PASS, independent of the claim's status label). The MECH-229 substrate-ceiling lift (governance_2026_06_15) left the claim at PROVISIONAL. The automated provisional->stable gate needs min_experimental_entries=4; MECH-229 has only 3 genuine experimental entries (exp_conf 0.868 already clears the 0.80 floor), so the engine will not auto-promote. User decision 2026-06-15 ('queue confirmatory run then promote'): V3-EXQ-514p (confirmatory replication of 514o, independent seeds 45/46/47, claim_ids=[MECH-229]) QUEUED + coordinator-ingested 2026-06-15 (dry-run smoke PASS) as the 4th genuine entry. ON 514p PASS -> promote MECH-229 provisional->stable WITH the derive-only reconcile (record_decision.py promote_to_stable + rebuild index). See MECH-229 evidence_quality_note 2026-06-15 follow-on. A 514p contact_guard_unmet self-route is substrate-marginal, NOT a weakens -- promotion just waits for a clean 4th entry."
      governance_2026_06_15: "CLOSED (Case 1 -- PASS, no follow-up). V3-EXQ-514o LANDED PASS/supports 2026-06-15: the object-bound wanting!=liking dissociation (the terminal L9 acceptance criterion that every prior governance note named as GAP-2's sole residual) scores mean_object_bound_wl_dissoc_fraction=0.80 (>= 0.6 pre-registered) with n_scored_wl_steps 5/6/7 across seeds (the 681-C4 liking-source fix cured 514n's n_scored=0), both readiness gates met, non_degenerate=true. MECH-229 recorded as a genuine supports (exp_conf 0.868); at governance 2026-06-15 the MECH-229 substrate_ceiling + pending_retest_after_substrate were LIFTED on the strength of this PASS. owner_exq advanced 514n -> 514o; status open -> done. This also clears the sole residual of the GAP-7-gated L9 acceptance (see goal_pipeline:GAP-7)."
      governance_2026_06_14: "SD-057 channel-write substrate-clearance condition (named in governance_2026_06_12 'a further successor is owed once the SD-057 channel-write substrate clears') is now MET. The 514o precursor V3-EXQ-681 (SD-057 wanting!=liking channel-write forced-contact microdiagnostic, claim_ids=[], decoupled from foraging like 626b) PASSED on ree-cloud-3 2026-06-14T20:14:58Z (manifest v3_exq_681_sd057_wl_channel_write_forced_contact_microdiagnostic_20260614T201458Z_v3, label sd057_wl_channel_write_validated; C1 instrument-separates + C2 forced-dissociation n_scored_wl_steps=40 / wl_dissoc 0.5 / distinct_tokens 2 / drive_spread 1.0 + C3 null-parity 0.0 + C4 co-timing-structural; readiness_met). This RETIRES the 514n n_scored_wl_steps=0 / run_bank_populated=false residual as a substrate concern -- the IncentiveTokenBank populates and scores WL steps when contact is forced. GAP-2's remaining residual is now ONLY the harness/contact-guard side: the 514o L9 behavioural successor (port the 603n lever stack so z_goal_norm_at_contact_peak>0.4 clears >=2/3 in the 514 harness, letting the now-proven channel-write fire during real foraging) is DE-RISKED but not yet written/queued. GAP-2 STAYS open (Case 3). owner_exq unchanged (681 is a claim-free precursor, not the lineage owner). No claims.yaml status change."
      governance_2026_06_12: "Closure-drift stale-since-review acknowledgement (governance cycle 2026-06-12). Flagged because owner_exq pinned V3-EXQ-514m but the substrate-faithful successor V3-EXQ-514n has since RUN and been reviewed (FAIL/non_contributory, MECH-229 scoring-excluded; substrate_queue SD-049-PHASE-2 amended by the batch9 cycle). owner_exq advanced 514m -> 514n. GAP-2 STAYS open (Case 3): the wanting!=liking dissociation acceptance criterion is still the residual; 514n self-routed below its same-statistic WL non-vacuity gate (substrate_not_ready_requeue), so a further successor is owed once the SD-057 channel-write substrate clears. No claims.yaml status change."
      governance_2026_06_11c: "AUTOPSY CONFIRMED + APPLIED (governance cycle #4). failure_autopsy_V3-EXQ-514m_2026-06-11 (status=confirmed, user-adjudicated) consumed: the 514m MECH-229 C_WL wanting!=liking dissoc=0.0 on all 3 seeds (zero variance) is adjudicated a VACUOUS FAIL (measurement_test_design_defect), NOT a falsification. The DV compares the SD-014 residue VALENCE_WANTING/VALENCE_LIKING channels, but the run's config omits valence_liking_enabled/tonic_5ht_enabled/schema_wanting_enabled and the custom eval loop never writes them, so |w-l|>0.1 can never fire independent of behaviour; the contact guard verifies foraging but not channel-write. APPLIED: MECH-229 per-claim weakens reclassified non_contributory on the flat+nested manifests, stays scoring-excluded (pending_retest_after_substrate_per_claim=[MECH-229]); claims.yaml MECH-229 quality note prepended + narrow_supports_flag=true; failure_autopsy_ref added. NO demotion; substrate_queue action=none (instrumentation defect, SD-057 substrate already landed). MECH-230 supports (recorded cycle #3) is unaffected and sound. GAP-2 STAYS open (Case 3): the wanting!=liking dissociation acceptance criterion is still the residual, now owned by the substrate-faithful retest V3-EXQ-514n (SD-057 object-bound wanting-target!=liking-target dissociation, MECH-346 most-wanted z_goal pointer, use_incentive_token_bank already on, with a same-statistic WL non-vacuity readiness gate) -- OWED via /queue-experiment, not yet queued; owner_exq stays V3-EXQ-514m until 514n is queued. NEXT: /queue-experiment V3-EXQ-514n."
      governance_2026_06_11b: "STAGE B (behavioural validation) RAN, did NOT close GAP-2 -- owner_exq advanced V3-EXQ-514l -> V3-EXQ-514m (governance cycle #3). V3-EXQ-514m (the SD-049 Phase-2 behavioural curriculum successor, on the now-ready scaffolded_sd054_onboarding substrate, foraging-contact guard 2/3 seeds) FAILed: of the three DVs, C_ID identity-recovery PASS (probe acc 0.926) and C_ANOVA per-axis drive PASS (F_max 1096) but C_WL wanting!=liking dissociation = 0.0 on ALL 3 seeds. SPLIT outcome applied: MECH-230 SUPPORTS (clean structured-z_goal evidence on its awaited substrate -> claims.yaml pending_retest_after_substrate CLEARED + supporting note; first genuine non-degenerate support) ; MECH-229 weakens FLAGGED for /failure-autopsy and SCORING-EXCLUDED this cycle (pending_retest_after_substrate_per_claim=[MECH-229]; consequential weakens on a no-other-support provisional claim + 660a-style readout-defect candidate: consumption-phase identity probe under-sampled n=5/6/8, dissoc exactly 0.0 across seeds -- pre-registered failure_signature = absent similarity structure). 514m supersedes 514l (predecessor stays non_contributory, supersession note added). GAP-2 STAYS open: the wanting!=liking dissociation acceptance criterion is the residual, now blocked on the /failure-autopsy diagnosis of MECH-229. RESUME: on confirmed failure_autopsy_V3-EXQ-514m, apply its routing (readout redesign vs absent-similarity-structure substrate enrichment) then re-issue the dissociation arm via /queue-experiment. No further claims.yaml status changes this cycle. The substrate-readiness STAGE A note below stands. This node is Case 3 in closure-drift terms (legitimately non-terminal pending the /failure-autopsy diagnosis of the 514m wanting!=liking arm and its successor dissociation EXQ; the 514m owner manifest is terminal but the residual acceptance criterion is not)."
      governance_2026_06_11: "STAGE A (substrate-readiness) CLEARED -- status blocked_pending_substrate -> open (session substrate-reconcile-603n-readiness-flip-20260611T0135Z). V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z; supersedes 603m; claim_ids=[], non_contributory, reviewed 2026-06-11) -- the corrected-G0 re-validation routed by failure_autopsy_V3-EXQ-603m_2026-06-10. Per the autopsy 'retime, don't loosen' steer, G0 (Stage-0 forced-feed positive control) was recalibrated to a floor of 0.3 (GoalState is zero-init pre-feed, so peak>0.3 is a materially-above-baseline lift at the least-mature developmental stage) while the load-bearing ECOLOGICAL gate G3 stayed at 0.4; all four legs cleared each >=2/3 (G0 3/3, G1 survival 2/3, G2 contact, G3 ecological consumption-gated z_goal>0.4); non-vacuity met (harm_eval range 0.011>0.005, G_H 3/3, reached-P2-alive). substrate_queue.scaffolded_sd054_onboarding.ready FLIPPED true 2026-06-11 (readiness_flip_2026_06_11). The substrate block is LIFTED; the gap now closes on STAGE B -- re-issue the SD-049 Phase-2 behavioural validation (V3-EXQ-514l successor, MECH-229/MECH-230-tagged, with a foraging-contact-rate guard) via /queue-experiment. No claims.yaml / manifest edits; substrate_queue + plan-node reconcile only."
      governance_2026_06_10: "Substrate-reconcile WP-A (session substrate-reconcile-603jk-WP-A-20260610T0631Z): V3-EXQ-603k LANDED PASS 2026-06-09 (Stage-H harm-pathway readiness; claim_ids=[], non_contributory, reviewed) CLEARED the scaffolded_sd054_onboarding SURVIVAL/hazard-avoidance leg (ARM_HARM_ON_NAV G_H 2/3 + P1 survival 3/3; OFF nav-control dies; harm_eval range 0.133). This DE-RISKS but does NOT unblock GAP-2: GAP-2's specific blocker is the FORAGING/benefit-contact leg (P2 contact + P2 z_goal>0.4), which 603k's survival probe does not exercise; Stage-0 z_goal>0.4 also held on only 1/3 seeds. substrate_queue.scaffolded_sd054_onboarding stays ready=false (status updated to 'harm-pathway-survival leg VALIDATED'; residual = foraging/benefit-contact). status STAYS blocked_pending_substrate; resume_condition unchanged (full three-leg gate, each >=2/3 seeds). No claims.yaml / manifest edits; substrate_queue reconcile only."
      readiness_diagnostic_2026_06_10: "Readiness-gate eval + remaining-diagnostic queue (session scaffolded-sd054-readiness-gate-eval-20260610T0652Z, depends-on WP-A above). CONFIRMED the post-603k readiness gate is only PARTIALLY met from substrate_queue.scaffolded_sd054_onboarding.ready_blocked_by: P1 survival CLEARED (3/3, 603k) but Stage-0 z_goal>0.4 held on 1/3 (0.486/0.385/0.385), and the P2 benefit-contact + P2 z_goal>0.4 legs were UNEXERCISED by 603k's survival-only probe. Per per-claim accuracy (only queue what the substrate can now deliver interpretable signal for), did NOT queue the SD-049 GAP-2 / MECH-229 / MECH-230 / MECH-260 behavioural retests -- the substrate cannot yet deliver an interpretable P2 read (a P2-contact-zero would be 'died/under-formed before contact', not 'foraging incompetence'). INSTEAD queued the remaining readiness diagnostic V3-EXQ-603m (full curriculum Stage-0->Stage-0b->P0->Stage-H->P1->P2 with scaffold_train_harm_pathway=ON + the 2026-06-05 foraging-competence amend ON; the 603g full-curriculum harness + the 603k harm-pathway-ON config; supersedes 603g; claim_ids=[], priority 275, machine_affinity any; on origin + ingested into coordinator DB). 603m PASS rule = G0 (Stage-0 z_goal>0.4) AND G1 (P1 survival) AND G2 (P2 contact) AND G3 (P2 consumption-gated z_goal>0.4), each >=2/3 seeds; non-vacuity preconditions = harm-pathway-discriminative (harm_eval range > 0.005) AND reached-P2-alive (P1 survival >=2/3), else self-routes substrate_not_ready_requeue (never a foraging verdict). 603m is the run that exercises the residual foraging/benefit-contact + Stage-0-z_goal legs; on 603m PASS substrate_queue.ready flips true and the GAP-2 behavioural retests unblock. status STAYS blocked_pending_substrate; owner_exq stays V3-EXQ-514l (behavioural owner, distinct from the 603m readiness gate); resume_condition unchanged. No claims.yaml / manifest / substrate_queue edits (the WP-A session owns substrate_queue this cycle)."
      governance_2026_06_05: "Foraging-competence RESIDUAL IMPLEMENTED 2026-06-05 (ree-v3 harness layer; session implement-substrate-scaffolded-sd054-foraging-competence-20260605T2015Z). The residual the substrate_queue title names after the 634c split is landed: (1) scaffold_auto_reconcile_gating_to_seeding -- the contact-gating skip/seed decision now DERIVES its floor from the live GoalConfig (benefit_threshold / (gain*(1+drive_weight*drive_floor))) so the scaffold's 'seeds' boolean tracks GoalState.update's actual firing (removes the 634b hand-matched-magic-number anti-correlation); (2) scaffold_p1_reef_spawn_hold_fraction -- graded P1 reef-spawn weaning keeps the agent spawning in the reef refuge band for the early held fraction of P1 (a survival/foraging lever complementing the SD-057 cue-recall CONTACT lever); (3) substrate_readiness_from_results feeds the consumption-event-gated z_goal_norm_at_contact_peak (632-style) as the CANONICAL G3 input so a carried-nursery-trace non-foraging seed reads g3=0. All no-op-default, bit-identical OFF; 79/79 scaffold contracts (9 new C11) + 7/7 preflight PASS; 634c dry-run unchanged. substrate_queue.ready STAYS false: the runtime gates (z_goal_at_contact>0.4, P1 survival, P2 contact, each >=2/3 seeds) require a full-scale substrate-readiness run, queued via /implement-substrate Step-8 /queue-experiment. RESUME condition unchanged (below). No claims.yaml / manifest edits."
      governance_2026_06_03: "Closure-drift reconcile to the 2026-06-03 evening /governance cycle (commit 8c85f06e5a). status blocked -> blocked_pending_substrate; owner_exq 514g -> 514l (current terminal of the lineage). Three confirmed same-day failure-autopsies converge here: V3-EXQ-514l (SD-049/SD-015/MECH-229/MECH-230) + V3-EXQ-632 (MECH-230) + V3-EXQ-634 (nursery readiness, claim_ids=[]) all classified non_contributory + epistemic_category=substrate_ceiling + pending_retest_after_substrate, ONE structural property = foraging-competence / ecological reward-contact ceiling. 632 seed-42 is a CLEAN positive (z_goal_norm=3.0115 at contact, persists to t50, absent under ablation) confirming the goal-stream wiring is sound; the failures are seeds that never made benefit contact. 634 readiness run: Stage-0 forced-feed positive control PASSES 3/3 (z_goal>0.4) but wean-to-wild G1 survival / G2 contact / G3 z_goal all fail -- the amend is necessary-but-insufficient, so substrate_queue.ready stays false. This node is now behind a substrate-enrichment step (survival-foraging-competence scaffold), not a re-queue of the 514 lineage. No claims.yaml / manifest / substrate_queue edits this session (plan-doc reconcile only; those writes landed in the governance cycle). Prior resume_condition retained below verbatim."
      resume_condition: "RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queue.ready=true: Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds), then re-issue the SD-049 Phase 2 behavioural validation (MECH-229/MECH-230-tagged, with a foraging-contact-rate guard) via /queue-experiment. PRIOR (2026-05-16, verbatim -- now SUPERSEDED by the 2026-06-03 foraging-competence finding): Monostrategy root cause has a validated substrate fix (V3-EXQ-567 PASS, supports ARC-065: SP-CEM lifts natural action entropy 0.012->0.497, candidate support 1.007->2.810). V3-EXQ-550 settled that the blocker is NOT z_goal wiring. Retest unblockable once SP-CEM lands in the main agent action path; re-issue the SD-049 Phase 2 behavioural validation via /queue-experiment then. See 2026-05-16 decision-log entry."
    - id: "goal_pipeline:GAP-3"
      title: "SD-012 sustained-drive amendment (EMA Option 1 + drive_floor Option 2)"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      unblocks_claims: [SD-012, MECH-216, MECH-306, ARC-051]
      depends_on: []
      last_updated: 2026-05-20
      completion_note: "V3-EXQ-582a PASS 2026-05-19T01:45Z (drive_floor sweep; floor=0.9 first-PASS arm A1-A4). Option 1 (drive_ema_alpha) substrate landed but V3-EXQ-582 FAIL (drive near-zero all episode). Option 2 (drive_floor) validated. MECH-306 registered 2026-05-20. Operating recommendation for downstream EXQs: drive_floor=0.9 with drive_ema_alpha=1.0 unless a combined arm is pre-registered."
    - id: "goal_pipeline:GAP-4"
      title: "MECH-295 drive->liking->approach cascade Tier-1 retest cohort"
      status: done
      severity: high
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      unblocks_claims: [MECH-295, ARC-030, MECH-117, Q-040]
      depends_on: ["goal_pipeline:GAP-1", "goal_pipeline:GAP-3"]
      last_updated: 2026-06-09
      completion_note: "Closed by governance decision 2026-06-09 (user-approved): re-scope MECH-295 to the modulatory reading and close, rather than continue blocking on the substrate-ceilinged V3-EXQ-490L successor. Rationale: (1) the behavioural-NECESSITY reading is terminally FALSIFIED (V3-EXQ-490j: severed bridge + drive amplification still produced approach_commit_rate=1.0 in 3/3 seeds via parallel first-class pathways MECH-216/290/307/tonic_5ht); (2) the MODULATORY reading is substrate-supported (490j substrate-firing layer C6/C7/C9); (3) the only remaining test -- behavioural SUFFICIENCY of the modulatory contribution (argmin-flip) -- was attempted by V3-EXQ-490k and defeated BY CONSTRUCTION (mech295_bias_range_mean=0.0) by the shared collapsed-candidate-pool / weak-z_goal substrate ceiling OWNED ELSEWHERE (scaffolded_sd054_onboarding, in flight via the 603-line Stage-H programme), NOT by this node. That optional modulatory-sufficiency retest is now tracked on MECH-295 (epistemic_category=substrate_ceiling, pending_retest_after_substrate=true) as a NON-GAP-BLOCKING future test, not a V3 closure requirement. MECH-295 stays candidate (no promotion -- substrate-firing support is not behavioural validation). claims.yaml functional_restatement + evidence_quality_note updated this session."
      governance_2026_06_09: "DECISION (user-approved): reverses the 2026-06-04 am/pm 'queue a successor (490L)' stance. 490k already executed that path and confirmed it cannot run on the current substrate; the blocking substrate is owned by scaffolded_sd054_onboarding, so coupling GAP-4 closure to 490L just chains it to a separate long-running substrate programme. Re-scope + close is the correct call: necessity falsified, modulatory reading stands and is substrate-supported. No promotion/demotion. Downstream goal_pipeline:GAP-5 (deferred, low severity) depends on GAP-4 and is now unblocked-in-principle but stays deferred."
      governance_2026_06_04_pm: "DECISION (user-approved /governance 2026-06-04 afternoon AskUserQuestion): the modulatory-sufficiency successor queued by the morning decision (V3-EXQ-490k) RAN and was autopsied (confirmed failure_autopsy_V3-EXQ-490k). 490k could NOT test the narrowed-modulatory reading: ROW_2_fires_but_never_flips -- the MECH-295 cue fires on all 3 seeds (mech295_fired_ticks=145) but argmin_flip_ticks=0 because mech295_bias_range_mean=0.0 (per-candidate bias uniform across candidates -> subtracting it cannot change the argmin BY CONSTRUCTION), defeated by upstream collapsed candidate z_world + weak z_goal (goal_norm_peak=0.193). Applied: manifest weakens->non_contributory; MECH-295 epistemic_category=substrate_ceiling + pending_retest_after_substrate=true + dated evidence_quality_note; narrow_supports_flag=true (zero behavioural-sufficiency across 490g/h/i/j/k); substrate_queue AMEND scaffolded_sd054_onboarding (+490k failure_record; MECH-295 already in unblocks). GAP-4 stays in-progress (Case 3, pending the V3-EXQ-490L successor on enriched substrate with a pre-registered mech295_bias_range_mean>0 guard). owner_exq advanced 490j->490k. No claim re-scope -- MECH-295 stays candidate until 490L lands on a substrate that can actually exercise the modulatory reading."
      governance_2026_06_04: "DECISION (user-approved /governance 2026-06-04 AskUserQuestion): resolve the 490j-terminal drift by QUEUEING A MODULATORY-SUFFICIENCY SUCCESSOR, not by closing now. 490j established the modulatory-not-necessary reading at the substrate-firing layer, but MECH-295's modulatory contribution has NOT yet been shown behaviourally consequential (a positive-control arm where removing/adding the modulatory bridge changes approach BEHAVIOUR, not just write-sum / cue-bias substrate signals). GAP-4 stays in-progress pending that successor EXQ. NEXT ACTION: author a modulatory-sufficiency positive-control successor to V3-EXQ-490j via /queue-experiment (owner_exq advances when queued). This is Case 3 in closure-drift terms (legitimately non-terminal pending a successor EXQ). No claims.yaml edit this cycle -- MECH-295 stays as-is until the successor lands (do NOT re-scope the claim text pre-emptively)."
      last_updated_note: "2026-06-03 closure-drift sync: absorbed V3-EXQ-490j terminal result (was recorded as merely 'claimed'). 490j severed-bridge baseline FALSIFIES the weak-reading behavioural-NECESSITY claim for MECH-295 -- ARM_0 severed bridge + drive amplification still produced approach_commit_rate=1.0 in 3/3 seeds via architecturally first-class PARALLEL REE drive->approach pathways (MECH-216/MECH-290/MECH-307/tonic_5ht), so MECH-295 is not necessary for approach. The SUBSTRATE-FIRING layer supports the narrowed MODULATORY MECH-295 reading (C6 anticipatory_write_peak 0.287/0.0066/0.069; C7 approach_cue_bias_peak 0.396/0.054/0.427; C9 write_sum 80.2/0.58/...). Net: GAP-4 stays in-progress -- the Tier-1 cohort has now established the modulatory-not-necessary reading, but full MECH-295 cascade behavioural validation (a positive-control arm where the modulatory contribution is behaviourally consequential, not just substrate-firing) is not yet demonstrated; needs a governance decision on whether to (a) re-scope MECH-295 to the modulatory reading and close, or (b) queue a modulatory-sufficiency successor. Flag surfaced for user. Prior 2026-05-31 scope clarification (below) still holds: GAP-4 owns MECH-295 Phase 4 only, NOT GAP-C prereq (2) z_goal-collapse owner (`scaffolded_sd054_onboarding`)."
      scope_clarification_2026_05_31: "GAP-4 OWNS the MECH-295 cascade behavioural validation (Phase 4) ONLY. It does NOT own the `goal-pipeline training regime produces non-trivial z_goal in default config` prereq (2) referenced by behavioral_diversity_isolation:GAP-C / failure_autopsy_V3-EXQ-591_2026-05-27 section 7. That prereq is owned by the `scaffolded_sd054_onboarding` substrate-design memo (`evidence/planning/sd_054_scaffolded_onboarding_substrate_design.md`, 2026-05-29) + substrate_queue entry `scaffolded_sd054_onboarding` (status=pending_implementation) + IGW-20260531-029. Triage memo: `evidence/planning/z_goal_collapse_triage_2026-05-31.md`. The 490 cohort operates with the gap4 substrate (drive_floor=0.9 + drive_ema_alpha=1.0 + goal_stream=True) where z_goal IS active across all runs (490j ARM_1 goal_active_fraction=1.0); it CANNOT close prereq (2)."
      resume_condition: "Tier-1 cohort TERMINAL (V3-EXQ-490j landed 2026-05-31, see last_updated_note): MECH-295 behavioural-necessity falsified, modulatory reading substrate-supported. NEXT is a governance decision (re-scope MECH-295 to modulatory + close GAP-4, OR queue a modulatory-sufficiency behavioural successor). Background substrate context: GAP-3 done (MECH-306 + V3-EXQ-582a PASS). ARC-065 SP-CEM default landed 2026-05-17 (V3-EXQ-567). Tier-1 StepHarness retest cohort (V3-EXQ-490g / 471a / 475a / 524a) active; V3-EXQ-483c ran 2026-05-23 FAIL non_contributory (measurement gap: use_dacc=True omitted from all 4 arm configs; dacc is None; C2 cannot fire -- failure_autopsy_V3-EXQ-483c_2026-05-23). V3-EXQ-483d queued 2026-05-24 (PAG/override_signal C2 criterion + goal_norm_peak C3 + use_dacc cluster fix). MECH-307 4-arm discriminative pair still pending but GAP-1 substrate is landed. SCOPE: prereq (2) of behavioral_diversity_isolation:GAP-C is owned at `scaffolded_sd054_onboarding`, NOT this node; see scope_clarification_2026_05_31 above."
    - id: "goal_pipeline:GAP-5"
      title: "SD-049 Phase 3 consumer cascade migration (read-side fidelity)"
      status: done
      severity: low
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      unblocks_claims: []
      depends_on: ["goal_pipeline:GAP-4"]
      last_updated: 2026-06-15
      completion_note: "Closed superseded-by-implementation 2026-06-15. The cascade migration was BUILT + LANDED (ree-v3 main 2026-05-31T13:00Z, 'SD-049 Phase 3 SD-032 consumer cascade') independent of this node's documented deferral trigger ('Phase 4 PASSes Tier-3 + reveals a drive-cascade fidelity gap', which never fired -- GAP-4 closed 2026-06-09 by re-scope/falsification, not a Tier-3 fidelity-gap). All seven named consumers now carry the optional per_axis_drive kwarg (ree_core/cingulate/{aic_analog,pcc_analog,pacc_analog,dacc,salience_coordinator}.py, ree_core/regulators/{broadcast_override,mech295_liking_bridge}.py), preserving bit-identical OFF when per_axis_drive is None; causal_grid_world surfaces obs_dict['per_axis_drive'] under per_axis_drive_enabled. Readiness validated by V3-EXQ-618 (2026-05-31T17:59Z, experiment_purpose=diagnostic, all 4 acceptance criteria PASS: C1 per_axis_drive evolves min_peak=0.027>floor 0.02; C2 no crashes; C3 AIC reads per-axis mean_l1=5.92; C4 MECH-295 axis routes mean_l1=0.169). 618 is tagged evidence_direction=non_contributory because a substrate-readiness diagnostic does not behaviourally test SD-049/MECH-295; that is correct and does NOT block GAP-5 closure (GAP-5 is a refactor with no load-bearing dependent claim -- unblocks_claims:[]). NOTE: the *behavioural* validation of the Phase 3 cascade (V3-EXQ-619, reserved/not-queued, replicates V3-EXQ-514g structure on the Phase 3 substrate) is owned by goal_pipeline:GAP-2, NOT this node -- 619's downstream_owed lists the GAP-2 cluster (SD-049/SD-015/MECH-229/MECH-230/MECH-117/ARC-030/ARC-032/Q-030). The original 'fidelity refactor for its own sake' justification was never demonstrated necessary; the cascade got pulled forward as substrate plumbing for GAP-2's behavioural line, which is the correct place its remaining behavioural test now lives. No claims.yaml/scoring edit (refactor, no dependent claim)."
    - id: "goal_pipeline:GAP-6"
      title: "MECH-269b V_s staleness-corrected consumer migration"
      status: done
      severity: medium
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      unblocks_claims: [MECH-269b]
      depends_on: []
      blocking_external: ["external V_s invalidation runtime evolution"]
      last_updated: 2026-05-17
      completion_note: "Substrate fully implemented: HippocampalConfig.use_vs_gate_staleness_lookup, VsRolloutGate.gate() per_stream_staleness path, agent.py end-to-end wiring, HippocampalModule.compute_per_stream_staleness(). V3-EXQ-490b C1 PASS (gate fires); V3-EXQ-490c/e/f completed Q-040 factorial (MECH-295 dominant cause of catatonic-lock, not MECH-269b alone). Monostrategy confound resolved at substrate level by ARC-065 SP-CEM landing as default 2026-05-17. Q-040b behavioral sufficiency of staleness correction alone is a claims-level question continuing under v_s_invalidation_runtime.md; GAP-6 goal_pipeline dependency is satisfied."
    - id: "goal_pipeline:GAP-7"
      title: "Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit"
      status: done
      severity: load-bearing
      live:
        as_of: "2026-09-02"
        from: "failure_autopsy_V4-EXQ-002-003_2026-09-02#V3-EXQ-259"
        verdict: "superseded/standard"
        next: "routing=governance-note-only"
        brake: "fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["SD-012", "SD-014", "SD-015", "SD-018", "SD-049", "MECH-117", "MECH-216", "MECH-229", "MECH-230", "MECH-295", "MECH-306", "MECH-307", "MECH-455", "ARC-030", "ARC-032", "ARC-036", "ARC-051"]
      blocked_by: []
      unblocks_claims: [MECH-229, MECH-230, MECH-117, ARC-030]
      depends_on: ["goal_pipeline:GAP-2"]
      proposed_claims: ["REGISTERED 2026-06-04 as SD-057 -- the placeholders below all landed: MECH-344 (L2 benefit->object-identity binding, was MECH-BIND-obj)", "MECH-345 (L3 per-object slow-decay revaluable incentive token, was MECH-INCENT-token)", "MECH-346 (L4 z_goal seeded from most-wanted-object pointer; amends MECH-230; was MECH-GOALPTR)", "MECH-347 (L6 cue-triggered pre-consummatory wanting / cue-recall, was MECH-CUEWANT)", "MECH-348 (L7 dACC object-discriminative goal readout, was MECH-CONSUME -- folded into the SD-057 phase-2 pass per the L7 audit, not queued standalone)"]
      registered: 2026-06-03
      last_updated: 2026-06-15
      governance_2026_06_15: "CLOSED (Case 1 -- PASS via the GAP-2 close). The entire L2-L8 substrate was BUILT (L1 626b PASS; L2-L4 SD-057 v1 / V3-EXQ-636 PASS; L6-L7 SD-057 phase-2 / V3-EXQ-637 PASS) and the only unfinished criterion was the TERMINAL L9 wanting!=liking dissociation, gated on goal_pipeline:GAP-2 supplying reliable foraging contact (per reclassified_2026_06_10). V3-EXQ-514o LANDED PASS/supports 2026-06-15 -- object-bound wanting!=liking dissociation 0.80 with the channel-write firing during real foraging -- which closed GAP-2's L9 and therefore this node's sole residual. status blocked_pending_substrate -> done; owner_exq set to the 514o run that closed it; blocked_by cleared."
      source_artefact: "evidence/planning/thought_intake_2026-06-01_goal_wanting_liking_stream_repair.md section 8 (L0-L9 closure map) + section 9 (proposed plan-of-record updates); lit anchor evidence/planning/literature_synthesis_2026-06-01_object_bound_incentive_salience.md"
      ratified_2026_06_03: "User ratified the section-9 GAP-7 proposal into the plan-of-record this session. Closure thesis (intake section 8): the goal stream's broken links are L2-L3 (the benefit signal at contact is never bound to OBJECT IDENTITY and there is no per-object incentive-salience / wanted-object TOKEN -- the substrate writes raw z_world/z_resource at contact with no binding step and no per-object wanting amplitude), plus the measurement/wiring around L1 (forced-seed positive control) and L7 (dACC/E3/commitment consumer readout, where dACC does NOT read z_goal directly). L0/L1/L5 are substrate-present; L6/L8 are present-but-starved. The minimal repair is the L2-L3 layer + a clean L1 positive control + an L7 wiring audit -- NOT a new mature goal ecology. Cross-evidence: V3-EXQ-623 (MECH-104 volatility interrupt) is the positive control that REE DOES turn a correctly-wired signal into behavioural consequence, so the goal-stream fault is upstream (signal never produced / never object-bound), not 'REE cannot convert signal to behaviour'. The 626 harness bug (Class-1 separation: positive-control arms with z_goal not actually engaged) must be fixed before L1/L7 are measurable. Distinct from GAP-2 (which is the developmental foraging-competence ceiling -- get the agent to CONTACT resources); GAP-7 is what happens to the benefit signal ONCE contact occurs (bind it to an object, mint an incentive token, read it out). The two are sequential: GAP-2 supplies reliable contact, GAP-7 makes that contact object-bound and behaviourally consequential. This node carries the L0-L9 closure map embedded in the plan body below."
      resume_condition: "STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 cue-recall + dACC-readout layer ARE BUILT AND REGISTERED -- see l2l3_l6_l7_landed_2026_06_04 below. The earlier draft of this field (now superseded) instructed the NEXT session to build the L2-L3 substrate from scratch ('no SD/MECH doc yet; proposed_claims are placeholders, NOT registered in claims.yaml'); that instruction was STALE and mis-scoped a 2026-06-05 session toward re-building SD-057 as a duplicate. It is corrected here: the substrate landed 2026-06-04 as SD-057 (design doc docs/architecture/sd_057_object_bound_incentive_salience.md Status=IMPLEMENTED) with MECH-344(L2)/345(L3)/346(L4)/347(L6)/348(L7) registered (candidate) in claims.yaml and implemented in ree_core (goal.py IncentiveTokenBank + GoalState.cue_pull, agent.cue_recall_wanting, cingulate/dacc.py DACCAdaptiveControl candidate_goal_proximity, e3_selector goal_proximity). The L7/MECH-CONSUME readout-wiring was folded INTO SD-057 phase-2 (MECH-348) exactly as the L7 audit recommended, not queued standalone. Prior sub-deliverables also stand: L1 forced-seed positive control CLOSED (l1_2026_06_03; V3-EXQ-626b PASS, reviewed) and the L7 consumer-readout AUDIT DONE (l7_audit_2026_06_04). NEXT deliverable is NO LONGER a substrate build -- it is BEHAVIOURAL VALIDATION of the already-built substrate, which is in-flight or gated: (a) V3-EXQ-637 (SD-057 forced-cue L6-L7 diagnostic, claim_ids=[]) full-run review; (b) the cue-recall behavioural-authority thread V3-EXQ-638a->640->640a (640a in-flight 2026-06-05, cue-authority gain sweep) per the Decision-log 2026-06-05 entry; (c) the TERMINAL L9 wanting!=liking dissociation acceptance (514l C6 currently 0.0), which depends on goal_pipeline:GAP-2 supplying reliable foraging contact and is therefore the sole remaining critical-path dependency, owned by scaffolded_sd054_onboarding / goal_pipeline:GAP-2 -- do NOT re-build SD-057 to chase it."
      reclassified_2026_06_10: "status open -> blocked_pending_substrate (blocked_by goal_pipeline:GAP-2). Scoping close-out of the last open closure node. RATIONALE: the entire GAP-7 L0-L8 substrate is BUILT (L1 626b PASS; L2-L4 SD-057 v1 / V3-EXQ-636 PASS; L6-L7 SD-057 phase-2 / V3-EXQ-637 PASS) and the cue-recall behavioural-authority sub-thread is SETTLED -- so this node is NOT a live 'open' build node; the only unfinished criterion is the TERMINAL L9 wanting!=liking dissociation, which is gated on goal_pipeline:GAP-2 foraging contact. blocked_pending_substrate (matching how goal_pipeline:GAP-2 itself is tagged) is the honest status. NOT V4-deferred: GAP-7/SD-057 binds incentive salience to the SD-049 per-TYPE tag (type-level identity V3 already has, implementation_phase v3); the V4 object-representation spine (ARC-080 token-instance object-file + ARC-081/082/083, all implementation_phase v4 -- ARC-080 lists SD-057 as a CONSUMER, not a prerequisite) is a separate concern GAP-7 deliberately does not depend on. 640a CORRECTION (supersedes the 2026-06-05 'IN-FLIGHT' decision-log framing below): V3-EXQ-640a LANDED 2026-06-06 and was autopsied (failure_autopsy_V3-EXQ-640a_2026-06-06, confirmed, user-gated). The autopsy CORRECTED the naive read: the per-fire cue_zgoal_pull_norm ~0 is a SATURATION artifact (cue fires every step; absolute z_goal_at_cue_fire ~0.5 vs 0.42 OFF -> the cue DOES reach z_goal), NOT a cue_pull-primitive weakness. The real L6 bottleneck is z_goal->approach PROPAGATION (MECH-295 / E3 goal_proximity selection authority) -- the same modulatory-bias 'drowning' shape as the 604a/624a/614d cluster. Routing was applied: implement-substrate (amend) on substrate_queue 'modulatory-bias-selection-authority' (now status implemented, ready) carrying the 640a failure record; V3-EXQ-638b interoceptive build stays GATED (do-not-build, hard-constraint confirmed). epistemic_category substrate_ceiling on the propagation layer + pending_retest_after_substrate. GAP-2 PROGRESS (2026-06-10): scaffolded_sd054_onboarding V3-EXQ-603m CLEARED the load-bearing ecological legs (P1 survival 3/3, P2 contact 3/3, P2 consumption-gated z_goal 2/3); failed only the G0 nursery positive control (autopsied measurement/developmental-sequencing artifact), residual = corrected-G0 re-validation V3-EXQ-603n (queued). RESUME unchanged: on GAP-2 substrate_queue.ready=true, re-issue the L9 MECH-229/MECH-117/ARC-030 behavioural retest via /queue-experiment. No claims.yaml / substrate_queue / manifest / experiment edits this session (plan-doc frontmatter + decision-log refresh only)."
      l1_2026_06_03: "L1 (forced seed -> non-zero, stable z_goal) re-established as a passing diagnostic, GAP-2-independent. (1) The 626 Class-1 harness defect (the bespoke loop never called agent.update_z_goal) is CLOSED -- 626a wired update_z_goal; the 2026-06-03 cluster autopsy V3-EXQ-603e-626a-622 confirms 'the goal-pipeline WIRING layer is closed and verified'. (2) The forced-seed L1 positive control passes at the UNIT level: ree-v3/tests/contracts/test_goalstate_forced_seed_positive_control.py 6/6 (forced supra-threshold seed -> non-zero, direction-stable z_goal). (3) V3-EXQ-626b (queued + ingested into coordinator DB 2026-06-03; supersedes 626a; claim_ids=[], diagnostic) adds a genuine FORCED-SEED positive-control arm to the developmental-window diagnostic itself -- benefit forced supra-threshold fed to update_z_goal every step (run_stage0_nursery pattern), DECOUPLED from foraging -- plus a no-benefit negative control and a z_goal-off parity control, so the harness can SEE a non-zero stable z_goal dependent ONLY on the harness fix + GoalState gate, NOT on the GAP-2 foraging-competence substrate. Dry-run smoke PASS (C1 forced-seed formation >=0.4 / C2 stability / C3 negative-control no-seed / C4 OFF-parity all True at 2-ep dry budget). FULL RUN NOW LANDED + REVIEWED (2026-06-04): manifest v3_exq_626b_..._20260603T211703Z_v3.json outcome=PASS with all four acceptance criteria green at full budget -- C1 formation 3/3 seeds (peaks 0.464/0.551/0.615, floor 0.4); C2 stability 3/3 (last-window medians 0.457/0.543/0.595, floor 0.1); C3 negative control 3/3 (no-benefit arm peaks all 0.0, ceiling 0.05 -- proves the forced seed IS the signal, not a loop artifact); C4 z_goal-off parity 3/3 (peaks all 0.0). In review_tracker.json (v3_exq_626b) and walked in the 2026-06-04 governance cycle (c28e0ba209, '626b positive control' among the 4 PASS); not in pending_review.md. L1 is therefore CLOSED, not merely queued. KEY CORRECTION the L1 work makes precise: 626a's experiment-level positive control FAILED only because its ARM_A drew benefit from ecological foraging, so seeds that never foraged (a GAP-2 leak) showed z_goal=0 -- that is GAP-2's foraging-competence ceiling, NOT a harness defect. The forced-seed control removes that confound. L2-L3 object-binding + L7 consumer-readout audit remain open (node stays status:open)."
      l7_audit_2026_06_04: "L7 (consumer-readout wiring audit) sub-deliverable DELIVERED as a source audit -- the 'does dACC/E3/commitment actually read z_goal' question is now answered with file:line precision against ree-v3/ree_core. FINDING: z_goal reaches behaviour through exactly ONE behaviourally-consequential path, and it is narrow. (1) WRITE: GoalState.update() / .with_injection() (ree_core/goal.py:148,240); exposed as the z_goal tensor via the .z_goal property (goal.py:144) and as the goal_proximity()=1/(1+MSE(z_world,z_goal)) scalar (goal.py:226). (2) E3 (the action-selection scorer) reads z_goal ONLY via goal_proximity -- a scalar -- gated on config.goal_weight>0 (ree_core/predictors/e3_selector.py:461,618-629; MECH-112/MECH-117 wanting term). This is the SOLE path by which z_goal biases which action is chosen. (3) E1 reads the z_goal TENSOR directly as LSTM conditioning (ree_core/agent.py:2642,2653; MECH-116) -- but that shapes world-model prediction, not action choice directly. (4) Action selection injects a norm FLOOR via with_injection (agent.py:3109, MECH-188) but still routes through the same goal_proximity scalar. (5) dACC does NOT read z_goal or goal_state at all -- forward() takes only drive_level:float + per_axis_drive (ree_core/cingulate/dacc.py:325-335); the plan's 'dACC does NOT read z_goal directly' claim is CONFIRMED. (6) The entire cingulate / regulator / governance / policy stack is z_goal-BLIND: salience_coordinator, broadcast_override (SD-037), pag/freeze_gate (MECH-279), policy/gated_policy (ARC-062), pfc/lateral_pfc_analog (SD-033a), pfc/ofc_analog (SD-033b), governance/closure_operator (SD-034) -- all read drive_level (collapsed scalar) / per_axis_drive / z_harm / z_world, never z_goal. (7) Indirect non-action consumers: ghost_goal_bank (MECH-292) and ghost-probes (MECH-293) read z_goal via stored cosine-matched snapshots. STRUCTURAL CONCLUSION (the audit's real payload): the only readout that makes a non-zero z_goal behaviourally consequential is the E3 goal_proximity term -- proximity of z_world to a SINGLE z_goal attractor point in z_world space. There is structurally NO surface today that could express per-object wanting, because z_goal is one attractor and proximity is to that point, not to an object identity. So the L7 'wire the missing readouts' sub-step is NOT a standalone no-new-substrate task as originally scoped: wiring dACC (the natural 'is this goal worth the effort' site) to read z_goal would only hand it the same single-attractor proximity scalar. L7-wiring is therefore ENTANGLED with and DOWNSTREAM of L2-L3 (object-binding + per-object incentive token) -- the readout cannot be made object-discriminative until there is an object-bound token to read. RECOMMENDATION surfaced for user: fold the MECH-CONSUME (L7) readout-wiring into the L2-L3 /implement-substrate design rather than queueing it standalone; the audit half of the L7 deliverable is done. Node stays status:open (L2-L3 substrate + the now-folded L7 wiring remain)."
      l2l3_l6_l7_landed_2026_06_04: "L2-L3-L4 (v1) AND L6-L7 (phase-2) SUBSTRATE LANDED + REGISTERED 2026-06-04 -- this closes the substrate-build half of GAP-7 and supersedes the build instruction the earlier resume_condition draft carried. Registered as SD-057 (drive.object_bound_incentive_salience; design doc docs/architecture/sd_057_object_bound_incentive_salience.md Status=IMPLEMENTED; claim status candidate). The proposed placeholder claims all became real claims.yaml entries: MECH-BIND-obj -> MECH-344 (L2 benefit->object-identity binding on the SD-049 per-type tag); MECH-INCENT-token -> MECH-345 (L3 per-object slow-decay revaluable incentive token, at-recall drive-specific wanting = base_value*(1+kappa*per_axis_drive)); MECH-GOALPTR -> MECH-346 (L4 z_goal seeded FROM the most-wanted object's stored embedding; amends MECH-230); MECH-CUEWANT -> MECH-347 (L6 cue-recall: a perceived cue with no benefit pulse retrieves its token and nudges z_goal pre-consummatorily, identity-matched + drive-specific); MECH-CONSUME -> MECH-348 (L7 dACC object-discriminative goal readout: dACC reads per-candidate goal_proximity so its effort/value computation is goal-conditioned, resolving the L7-audit 'dACC was z_goal-blind' finding -- FOLDED into SD-057 phase-2, not queued standalone, exactly as the L7 audit recommended). Implementation (ree-v3, default-OFF bit-identical, no trained params): goal.py IncentiveTokenBank + GoalState.cue_pull; agent.cue_recall_wanting; cingulate/dacc.py DACCAdaptiveControl.forward candidate_goal_proximity -> DACCtoE3Adapter bias; e3_selector goal_proximity. Commits: ree-v3 53f6427 (v1) + 24f31e5 (phase-2); REE_assembly claims 1f12a8e60f (v1) + e79ef7207e (phase-2). Contracts: v1 6/6 + 747/751; phase-2 5/5 + 750/757; 7/7 preflight. Validation: V3-EXQ-636 (L2-L4 mechanism) PASS full-run 4/4 (binds 2 types; 5/6 wanting!=liking events ON vs 0 OFF; legacy seeding intact); V3-EXQ-637 (L6-L7 forced-cue diagnostic, claim_ids=[], GAP-2-decoupled) queued, dry-run PASS 4/4. The substrate-build half of GAP-7 (L2-L8 mechanism) is therefore COMPLETE; node stays status:open ONLY for the L9 behavioural acceptance, which is GAP-2-gated (foraging contact) -- see the corrected resume_condition above. Frontmatter corrected 2026-06-05T20:17Z after a session was mis-scoped off the stale field; no claims.yaml/substrate/experiment edits in that correction (plan-doc frontmatter only)."
---
# Goal Pipeline Plan (wanting / liking / goal-seeding)

**Registered:** 2026-05-08
**Status:** active
**Scope:** close the substrate gaps that prevent the
drive -> wanting -> liking-bridge -> approach-cue loop from producing measurable
behavioural effect. The cohort SD-012, SD-014, SD-015, SD-018, SD-049 (Phase 1 +
Phase 2 + deferred Phase 3), MECH-216, MECH-229, MECH-230, MECH-117, MECH-295,
MECH-307, ARC-030, ARC-032, ARC-036, ARC-051 is wired end-to-end at the module
level but the integration produces the wired-but-inert pattern recurring across
EXQ-471 / EXQ-483 / EXQ-490 / EXQ-514 / EXQ-536 / EXQ-538.

This plan is the durable resume-point for goal-pipeline work across sessions.
When work pauses for adjacent paths (sleep substrate, V_s monostrategy, Tier-1
StepHarness retests), the deviation is logged in the [Decision log](#decision-log)
with a resume condition.

---

## One-line framing

> The drive-to-approach pipeline has all its modules. Drive amplification,
> wanting EMA, schema readout, ResourceEncoder identity, liking-bridge,
> per-axis homeostatic drive, ghost-goal bank, dACC bias, BG action selection
> -- each component passes its unit tests and its substrate-readiness
> diagnostic in isolation. End-to-end the loop produces approach_commit_rate=0
> across every diagnostic that probes it. The fault is at the seams, not in
> the components.

The pattern is named in the substrate_queue.json failure records: cue-side gain
fires on direct injection (EXQ-493 UC4), liking-bridge collapses correctly when
severed (EXQ-493 UC5), the encoder's identity head trains
(SD-049 Phase 2 hybrid encoder PASS smoke), but the conjunction of (a) signed
anticipatory affect, (b) drive-modulated cue salience, (c) per-axis goal-identity
disambiguation, and (d) anticipatory write-at-predicted-location does not
produce a behaviourally distinguishable approach signal.

The gap is not "more design". It is the integration audit + the four-gap
conjunction fix + the sustained-drive amendment + the behavioural validations
that have been deferred behind each successive substrate landing.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| 2026-05-08 governance-cycle-friday-pm session | Strategic redirect: MECH-307 + MECH-295 added to substrate_queue priority=1; SD-049 / SD-029 / SD-032b / MECH-269b-followup-A failure records updated with EXQ-490f / EXQ-514f / EXQ-536b confounds |
| 2026-05-08 register-mech307-and-sd014-amendment session | MECH-307 registered as candidate / v3_pending; SD-014 evidence_quality_note records both proposals (conjunction fix vs 6-channel amendment) |
| [docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md) | MECH-307 four-gap conjunction architecture; comparative analysis vs SD-014 6-channel amendment fallback |
| [docs/architecture/sustained_drive_anticipatory_wanting.md](../../docs/architecture/sustained_drive_anticipatory_wanting.md) | SD-012 amendment scoping (drive collapse at contact); three options (sustained-drive EMA, decoupled wanting, insatiability floor) |
| [docs/architecture/goal_wanting_signal_chain.md](../../docs/architecture/goal_wanting_signal_chain.md) | Provenance map: world_obs -> ResourceEncoder -> z_resource -> z_goal seeding -> VALENCE_WANTING -> E3 score -> action |
| [docs/architecture/mech_295_drive_liking_approach_bridge.md](../../docs/architecture/mech_295_drive_liking_approach_bridge.md) | MECH-295 weak-reading bridge: cue-side gain = f(drive * goal_proximity); severed-bridge falsifier |
| [docs/architecture/sd_049_multi_resource_heterogeneity.md](../../docs/architecture/sd_049_multi_resource_heterogeneity.md) | SD-049 Phase 1 / Phase 2 / Phase 3 implementation note; 4-arm validation grid + Woo/Spelke falsifier branch |
| [docs/architecture/sd_015_z_resource_encoder.md](../../docs/architecture/sd_015_z_resource_encoder.md) | z_resource encoder identity head + magnitude head (Phase 2 hybrid Option C verdict) |
| substrate_queue.json MECH-307 (priority=1) + MECH-295 (priority=1) entries | Names MECH-307 four-gap conjunction as the top-priority unblocker for the goal pipeline per 2026-05-08 governance |
| EXQ-493 MECH-295 weak-bridge validation (6/6 PASS, 2026-04-27/28) | Cue-side bias produces monotone-negative score_bias; severed-bridge collapses to 0; UC1-UC6 pass. Confirms the bridge is wired correctly in isolation |
| EXQ-490f / EXQ-514f / EXQ-536b failure records | Cascade-broken-beyond-rv pattern; force-arm probe with z_goal_inject=0.3 + action-time fraction=1.0 -> approach_commit_rate=0.0 |

---

## Existing substrate (do not duplicate)

Wired and behaving correctly in isolation:

| Component | Location | Status |
|---|---|---|
| SD-012 homeostatic drive (single-axis collapse) | `ree-v3/ree_core/goal/goal_state.py` GoalState.update() | implemented; drive_weight=2.0 default |
| SD-014 4-component valence vector (w/l/h/s) | `ree-v3/ree_core/residue/` ResidueField | candidate; channels written |
| SD-015 z_resource encoder (magnitude head) | `ree-v3/ree_core/latent/stack.py` ResourceEncoder | implemented Phase 1; identity head landed Phase 2 |
| SD-018 resource proximity supervision | `ree-v3/ree_core/latent/stack.py` SplitEncoder.resource_proximity_head | implemented |
| SD-049 Phase 1 multi-resource env-only substrate | `ree-v3/ree_core/environment/causal_grid_world.py` flat-kwargs | phase_1_implemented 2026-05-03 (V3-EXQ-513 PASS 13/13) |
| SD-049 Phase 2 hybrid encoder (identity + magnitude) | `ree-v3/ree_core/latent/stack.py` ResourceEncoder identity_head + LatentState.identity_logits | phase_2_implemented 2026-05-04; V3-EXQ-514 behavioural validation pending |
| MECH-216 E1 schema readout / predictive wanting | `ree-v3/ree_core/predictors/e1_deep.py` schema_readout_head + agent.update_schema_wanting() | implemented; schema_wanting_enabled flag default False |
| MECH-229 wanting/liking behavioural dissociation | E3 + VALENCE_WANTING + VALENCE_LIKING residue channels | active (10 seeds, 3 experiments PASS); evidence is z_world fallback seeding (degenerate per SD-049 failure record) |
| MECH-230 z_goal latent structure | GoalState.update() + z_resource seeding | provisional; v3_pending |
| MECH-295 drive -> liking-bridge -> approach cue | `ree-v3/ree_core/regulators/mech295_liking_bridge.py` | implemented 2026-04-26; V3-EXQ-493 6/6 PASS isolation; cascade behavioural validation deferred |
| MECH-117 wanting/liking dissociation in benefit_eval_head vs z_goal_latent | `ree-v3/ree_core/agent.py` benefit_eval_head + GoalState.update() | candidate; pending_retest_after_substrate (gate: SD-015 + sleep substrate) |
| ARC-030 BG approach-avoidance symmetry (Go + NoGo) | E3 + BG action selection | candidate; ARC-030's path forward is held under SD-012 / sustained-drive resolution |
| ARC-032 hippocampal theta-frequency goal communication | MECH-089 ThetaBuffer + agent goal context | candidate; theta-bypass ablation never run |
| ARC-036 multidimensional valence map | hippocampus + ResidueField 4-channel structure | candidate |
| ARC-051 multi-level wanting hierarchy (contact + schema + replay) | residue field VALENCE_WANTING field | candidate; depends on MECH-216 + MECH-217 + SD-018 firing in concert |

---

## Gap inventory

Six gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | MECH-307 four-gap conjunction architecture not landed: VALENCE_SURPRISE unsigned, MECH-216 writes only VALENCE_WANTING (no z_beta arousal coupling, no anticipatory liking), MECH-216 writes at current rather than predicted z_world | load-bearing | Q-040, SD-049 Phase 2 behavioural acceptance, SD-015 unblock chain, MECH-111, SD-032b, SD-018, MECH-112, MECH-295 cascade behavioural validation |
| **GAP-2** | SD-049 Phase 2 V3-EXQ-514 behavioural validation never PASSed: 514f reclassified non_contributory as pre-MECH-307 affect-stream confound; identity-recovery + wanting!=liking dissociation acceptance criteria untested under MECH-307-fixed substrate | load-bearing | SD-015, MECH-229 (non-degenerate retest), MECH-230, MECH-117 retest, MECH-216 retest, ARC-030, ARC-032, Q-030 |
| **GAP-3** | SD-012 sustained-drive amendment: drive_level collapses to ~0.005 at exact step the agent contacts a resource (energy resets toward 1.0); multiplier (1 + 2*0.005) cancels almost all benefit amplification SD-012 was intended to provide | high | MECH-295 cascade non-collapse, MECH-216 schema wanting threshold crossing, SD-014 wanting EMA non-degeneration, ARC-030 approach drive |
| **GAP-4** | MECH-295 cascade behavioural validation deferred: V3-EXQ-493 isolation 6/6 PASS confirms substrate, but EXQ-490f / EXQ-536a/b force-arm probe shows downstream cascade inert under realistic policy state (cue_fires=0 at relaxed activation floors; approach_commit_rate=0 even at z_goal_inject=0.3 + action-time fraction=1.0) | high | EXQ-471 catatonic-lock factorial diagnosis (Q-040), MECH-295 promotion, SD-029 substrate retest |
| **GAP-5** [DONE 2026-06-15] | SD-049 Phase 3 SD-032 consumer cascade reading per_axis_drive directly: AIC, PCC, pACC, dACC adaptive control, salience-coordinator, override-regulator, MECH-295 liking-bridge migrated from goal_state._last_drive_level (collapsed scalar) to the optional per_axis_drive vector. BUILT + LANDED ree-v3 main 2026-05-31; V3-EXQ-618 readiness PASS (4/4). | medium | SD-032b cascade fidelity, MECH-258 + MECH-260 calibration; refactor not on acceptance-criterion path for any current claim. Behavioural validation (V3-EXQ-619) owned by GAP-2. |
| **GAP-6** | MECH-269b-followup-A staleness-corrected V_s in VsRolloutGate.gate: lower-priority follow-on after V3-EXQ-490b clears; gates the V_s monostrategy resolution that interacts with goal-pipeline behavioural tests | medium | SD-029 retest cohort (cross-plan with sleep_substrate_plan via V_s invalidation runtime) |
| **GAP-7** | Object-bound incentive-salience layer missing: at resource contact the benefit signal is written as raw z_world / z_resource with no binding to object IDENTITY (L2) and no per-object wanting amplitude / incentive TOKEN (L3); plus measurement/wiring gaps at L1 (forced-seed positive control, blocked by the 626 harness bug) and L7 (dACC does not read z_goal directly). This is the "what happens to benefit ONCE contact occurs" gap, sequential to GAP-2's "get the agent to contact at all" | load-bearing | MECH-229 non-degenerate retest, MECH-230, MECH-117, ARC-030; L9 wanting!=liking dissociation (514k currently 0.0) |

GAP-3 (sustained-drive amendment) is intentionally separated from GAP-1 even
though both touch SD-012 / MECH-216. Reason: GAP-1 is the four-gap conjunction
fix at the affect-write site; GAP-3 is the drive-multiplier fix at the
goal-seeding site. They interact (the same EXQ-536b force-arm probe documents
both confounds) but the fixes are independently small and independently
falsifiable. Sequencing them serially keeps each PASS interpretable.

---

## Sequenced plan

Six phases. Each phase is small, verifiable, and unblocks at least one
downstream item. Phases are ordered by leverage and by what each unblocks.
Where work depends on adjacent paths (sleep substrate, V_s monostrategy,
StepHarness retest cohort), that is called out as a deviation in the
[Decision log](#decision-log).

### Phase 1: MECH-307 four-gap conjunction architecture (GAP-1)

Top priority per substrate_queue priority=1. Without this, every downstream
behavioural test of the goal pipeline confounds the conjunction-architecture
fault with the test's own claim.

Deliverables:

1. Gap 1: signed VALENCE_SURPRISE. Either (a) store signed PE in VALENCE_SURPRISE
   (negative for negative PE, positive for positive PE), with consumers reading
   sign or magnitude as needed; or (b) split into VALENCE_POSITIVE_SURPRISE and
   VALENCE_NEGATIVE_SURPRISE as separate channels. Default: (a) behind config
   flag `surprise_signed` (~5 lines, one field semantics change).
2. Gap 2: MECH-216 schema readout writes partial VALENCE_LIKING amplitude in
   addition to VALENCE_WANTING, AND raises z_beta arousal proportional to
   schema_salience. Two write sites added next to existing VALENCE_WANTING write
   in `agent.py:3753-3757`.
3. Gap 3: subsumed by Gap 2 architecturally (z_beta arousal write is the same
   line as the schema_salience-driven liking write); named separately because
   the z_beta path has a distinct downstream consumer (MECH-093 E3 heartbeat).
4. Gap 4: MECH-216 writes at the predicted z_world (E1's forward prediction),
   not the current z_world. Replace `self._current_latent.z_world` at
   `agent.py:3754` with the cached `e1_prior` predicted next-state z_world.
5. ~40 lines of code total per the 2026-05-08 design doc estimate.
6. Validation EXQ: 4-arm discriminative-pair experiment per the design doc
   Validation Experiment section. Acceptance: arm with all four gaps fixed
   produces non-zero `cue_fires + dacc_bias + approach_commit` in the relaxed
   floors arm relative to baseline; arm with any one gap re-disabled
   collapses to baseline (the conjunction-architecture falsifier).

Fallback (per docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md):
if MECH-307 conjunction fix does not produce the expected derived states, the
SD-014 6-channel amendment (add VALENCE_EXCITEMENT + VALENCE_DREAD as discrete
channels) is the architectural fallback. The amendment is registered in
SD-014's evidence_quality_note but not yet applied to the registry pending
MECH-307 outcome.

Phase 1 is the gate for everything else in this plan. Phases 2-6 do not start
until Phase 1's discriminative validation arm PASSes.

### Phase 2: SD-049 Phase 2 V3-EXQ-514 behavioural validation under MECH-307-fixed substrate (GAP-2)

V3-EXQ-514f reclassified non_contributory 2026-05-08 because the affect-stream
mixed harm + benefit surprise (classifier_loss 0.015-0.023 vs target <0.005;
probe_acc 0.48-0.53 vs target >0.70). The retest under signed VALENCE_SURPRISE
is the discriminative evidence on whether SD-049 Phase 2 hybrid encoder
delivers the goal_resource_r lift / identity-recovery / wanting!=liking
trajectory dissociation acceptance criteria.

Deliverables:

1. V3-EXQ-514g (or successor letter): re-queue V3-EXQ-514's 4-arm sweep with
   MECH-307 four-gap conjunction landed. Phased training preserved per Phase 2
   verdict (P0 joint -> P1 freeze classifier -> P2 evaluate). Pre-registered
   acceptance per design doc Validation Experiment section: ARM_2 -> ARM_0
   `goal_resource_r` lift >= 0.4 (target 0.066 -> >= 0.5); identity-recovery
   linear-probe accuracy > 0.6 in ARM_2; wanting_target != liking_target
   trajectory fraction >= 0.6 in ARM_2 (near zero in ARM_0 / ARM_1); per-axis
   drive ANOVA on z_goal cluster IDs p < 0.01 in ARM_2. Five-row interpretation
   grid + Woo/Spelke-style falsifier branch routing MECH-229 to
   substrate_conditional with V4-1 multi-agent ecology dependency on flat-failure.
2. Acceptance gates promotion of MECH-229 (non-degenerate retest, per SD-049
   failure record), MECH-230 (z_goal latent structure), MECH-117 (wanting /
   liking dissociation in benefit_eval_head vs z_goal_latent), MECH-216 (E1
   schema-conditioned wanting), and the SD-049 v3_pending clearance.
3. Row-6 falsifier branch (joint ARM_2 + ARM_3 failure): routes MECH-229 to
   substrate_conditional with V4-1 multi-agent ecology dependency. This is
   not a Phase 3 trigger (Phase 3 is the consumer-cascade refactor; the row-6
   branch is a substrate-ceiling escalation).

### Phase 3: SD-012 sustained-drive amendment (GAP-3)

Per `sustained_drive_anticipatory_wanting.md`, the multiplier
`(1 + drive_weight * drive_level)` cancels at contact because energy resets
toward 1.0 the moment a resource is consumed. Three substrate options listed
in increasing order of architectural change.

Deliverables:

1. Option 1 (cheapest): sustained-drive EMA. Replace instantaneous `drive_level`
   in the multiplier with a slow EMA (`drive_ema_alpha` config knob, default
   0.05; first PASS arm). Bit-identical OFF when alpha=1.0.
2. Option 2 (decoupled wanting): wanting amplitude as separate state from
   drive_level, updated at schema-cue events (MECH-216 fires) and at contact,
   decaying on a slow timescale independent of energy reset. Tracks the
   Berridge / Robinson sustained motivational state account.
3. Option 3 (insatiability floors): chronic homeostatic deficits maintain a
   baseline wanting tone independent of recent consumption. Most disruptive;
   requires a per-axis "deficit-history" buffer.
4. Validation: discriminative experiment landing Option 1 first; Options 2-3
   gated on Option 1 outcome.
5. Acceptance: max_effective_benefit > benefit_threshold (currently 0.1) at
   contact under realistic policy state, with the persistent attractor seeding
   on the Phase 1 corrected substrate. Falsifier: drive_ema_alpha sweep
   producing monotone seeding-rate vs alpha curve.

The lit-pull anchored in `sustained_drive_anticipatory_wanting.md` is a
companion task; the substrate amendment lands first, the lit-pull cites
biology in parallel.

### Phase 4: MECH-295 cascade behavioural validation (GAP-4)

V3-EXQ-493 confirms MECH-295 substrate is wired correctly in isolation (UC1-UC6
PASS). The cascade (drive amplification -> liking-stream gain -> approach cue)
fails in realistic experiments because the upstream wiring (Phase 1) and the
drive multiplier (Phase 3) prevent the bridge's input from ever firing.

Deliverables:

1. V3-EXQ-490g (or successor letter): re-queue Q-040 cascade test with Phase 1
   + Phase 3 landed. Acceptance: non-zero cue_fires + dacc_bias +
   approach_commit in relaxed-floor arm relative to baseline (the explicit
   target documented in MECH-295 failure record for EXQ-490f).
2. EXQ-471a / EXQ-475a / EXQ-483c / EXQ-490g / EXQ-524a Tier-1 retest cohort
   under StepHarness: re-queue the cohort with the canonical
   sense / update_z_goal / update_residue sequence + Phase 1 + Phase 3
   landed. The StepHarness migration was landed 2026-05-08 in
   `ree-v3/experiments/_harness.py`; the retest cohort consumes that
   migration. Tier-1 PASS gates Tier-2 (514f-style retest) and Tier-3
   (490e/f, 524, 536-cluster) per the 2026-05-08 governance redirect.
3. Acceptance gates promotion of MECH-295 to provisional and clears the
   EXQ-471 catatonic-lock factorial diagnosis (Q-040).

### Phase 5: SD-049 Phase 3 SD-032 consumer cascade (GAP-5)

> **STATUS 2026-06-15: DONE (superseded-by-implementation).** The cascade was
> built + landed (ree-v3 main 2026-05-31T13:00Z) and validated-ready by
> V3-EXQ-618 (4/4 acceptance criteria PASS, non_contributory readiness
> diagnostic), independent of the obsolete "Phase 4 Tier-3 fidelity-gap"
> trigger described below. The *behavioural* validation of the cascade
> (V3-EXQ-619, reserved) is owned by GAP-2, not GAP-5. See the GAP-5 frontmatter
> `completion_note`. The narrative below is preserved as the original design.

Cleanup-of-substrate-coverage refactor. Migrate AIC, PCC, pACC, dACC adaptive
control, salience-coordinator, override-regulator, MECH-295 liking-bridge from
reading `goal_state._last_drive_level` (collapsed scalar) to optionally reading
`obs_dict['per_axis_drive']` directly when SD-049 per-axis is on.

Deliverables:

1. Per-consumer migration order: start with MECH-295 liking-bridge (simplest);
   then salience-coordinator; then dACC; then AIC / PCC / pACC. Each consumer
   preserves bit-identical OFF when `per_axis_drive` is None or SD-049 per-axis
   is OFF.
2. Each consumer's `tick()` function gains an optional
   `per_axis_drive: Optional[Sequence[float]]` kwarg.
3. Test suite run after each consumer.
4. Trigger pending_substrate_reconfirmation flag on SD-012-emergent invariants
   per the invariant-types governance rule (the cascade changes how SD-012's
   drive_level interface is consumed across the cluster).
5. No new validation experiment required if Phase 5 is purely a refactor (no
   behavioural change); a regression run on the V3-EXQ-514 successor may be
   sufficient to confirm bit-identical OFF and activation correctness.

Phase 5 was intentionally low-priority. Per the queue entry's `ready_blocked_by`
field, "Cascade is a cleanup-of-substrate-coverage refinement, not an
acceptance-criterion prerequisite." None of the goal-pipeline acceptance
criteria require Phase 5 to land; Phases 1-4 are sufficient. The original gate
was "land only if Phase 4 PASSes a Tier-3 retest and reveals a remaining
drive-cascade fidelity issue." That gate never fired -- GAP-4 closed 2026-06-09
by re-scope/falsification, not a Tier-3 fidelity-gap. The cascade was instead
pulled forward 2026-05-31 as substrate plumbing for the GAP-2 behavioural line
(514g -> 618 -> 619), built + validated-ready (V3-EXQ-618), and GAP-5 is now
closed superseded-by-implementation (see the STATUS banner above).

### Phase 6: MECH-269b-followup-A staleness-corrected V_s in VsRolloutGate (GAP-6)

Lower-priority follow-on per substrate_queue. Tracked here because
goal-pipeline behavioural tests (Phase 4 Tier-3 cohort, SD-029 retest) interact
with V_s monostrategy: a monomodal policy cannot generate balanced
agent-vs-env event distributions for C2/C3 measurement, and reef enrichment
(SD-050) did not break monostrategy at this scale.

Deliverables:

1. Wire `MECH-284 StalenessAccumulator.snapshot()` correction into
   `VsRolloutGate.gate(...)` so the gate's V_s reading is staleness-corrected
   at use time, not just snapshot time. Implementation hint already in
   substrate_queue.json MECH-269b-followup-A entry.
2. Validation: V3-EXQ-490b (already pending in queue) is the primary
   diagnostic. Acceptance: Q-040 factorial cleanly distinguishes MECH-269b
   vs MECH-295 as dominant cause of the EXQ-471 catatonic-lock signature.
3. Phase 6 is independently scheduled by the V_s invalidation runtime work in
   sleep_substrate_plan / sd033_governance_plan; this plan tracks its
   dependency rather than owning the implementation.

### Phase 7: Object-bound incentive-salience layer + L1/L7 measurement repair (GAP-7)

Ratified 2026-06-03 from `thought_intake_2026-06-01_goal_wanting_liking_stream_repair.md`.
GAP-2 closes the *developmental* failure ("the agent never reliably contacts a
resource, so z_goal is never seeded"). GAP-7 closes the *representational /
wiring* failure that sits immediately downstream: once contact DOES occur, the
benefit signal is not bound to an object and is not read out consequentially.
The two are sequential -- GAP-2 supplies reliable contact, GAP-7 makes that
contact object-bound and behaviourally consequential.

The closure thesis (intake section 8): the broken links are **L2-L3** (object
binding + incentive token), plus the **measurement/wiring** around **L1**
(forced-seed positive control) and **L7** (consumer readout). L0/L1/L5 are
substrate-present; L6/L8 are present-but-starved. The minimal repair is the
L2-L3 layer + a clean L1 positive control + an L7 wiring audit -- NOT a new
mature goal ecology.

Deliverables (ordered by what is unblocked-first):

1. **L1 harness positive control + 626a Class-1 fix** (no new substrate). The
   626 harness bug let "positive control" arms run with z_goal not actually
   engaged (Class-1 separation). Fix the harness so a forced supra-threshold
   seed produces a non-zero, stable z_goal that the test can SEE, then
   re-establish the L1 positive control. This is the genuinely-unblocked entry
   point (depends on the 626a harness fix, not on the GAP-2 foraging substrate).
2. **L7 consumer-readout wiring audit** (no new substrate, mostly). Audit
   whether dACC / E3 / commitment actually read z_goal (today dACC does NOT
   read z_goal directly); document and wire the missing readouts so a non-zero
   z_goal is consequential. `PROP: MECH-CONSUME`.
3. **L2-L3 object-bound incentive-salience layer** (`/implement-substrate`
   design-discovery; no SD/MECH doc yet). Add (L2) a binding step that ties the
   benefit pulse to object IDENTITY rather than raw z_world/z_resource, and
   (L3) a per-object wanting amplitude / incentive token that decays slowly.
   Proposed placeholder claims `MECH-BIND-obj`, `MECH-INCENT-token`,
   `MECH-GOALPTR` (L4 z_goal-from-token-pointer), `MECH-CUEWANT` (L6
   cue-triggered pre-consummatory wanting) -- NOT yet registered in claims.yaml.
4. **Validation:** the L9 wanting != liking dissociation acceptance
   (514k currently 0.0) is the terminal acceptance, and depends on both L2-L3
   landing AND GAP-2 supplying reliable foraging contact.

Cross-evidence anchor: V3-EXQ-623 (MECH-104 volatility interrupt) is the
positive control proving REE DOES convert a correctly-wired signal into
behavioural consequence (discriminative signal + behavioural de-commitment,
8/8). So the goal-stream fault is upstream (signal never produced / never
object-bound), NOT "REE cannot convert signal to behaviour."

#### Closure map for the goal stream (L0-L9)

Embedded into the plan-of-record from intake section 8. Each link carries its
substrate status today and the diagnostic / claim that owns it.

| # | Link | Substrate today | Owning diagnostic (proposed) | Claim(s) |
|---|---|---|---|---|
| L0 | benefit pulse exists & crosses threshold | `env.benefit_exposure` + GoalState gate; GAP-3 PASS (582a) | Stage 0 unit | SD-012, MECH-306 |
| L1 | forced seed -> non-zero, stable z_goal | `GoalState.update` (exists) | **Stage 0 unit** (no new code; blocked by 626 harness bug) | MECH-230 |
| L2 | benefit binds to **object identity** (not location) | **MISSING** (writes raw z_world / z_resource at contact, no binding step) | **Stage 1** | **PROP: MECH-BIND-obj** |
| L3 | incentive-salience / wanted-object **token** | **MISSING** (no per-object wanting amplitude) | **Stage 1-2** | **PROP: MECH-INCENT-token** |
| L4 | z_goal written FROM token/affordance pointer | partial (z_resource seeding is closest) | **Stage 1** | MECH-230 amend; **PROP: MECH-GOALPTR** |
| L5 | persistent goal maintenance | slow attractor + E1 LSTM (MECH-116) | Stage 0/1 decay check | MECH-116, ARC-032 |
| L6 | cue-triggered wanting BEFORE consumption | MECH-295 bridge (isolation PASS) but no cue-recall path | **Stage 2** | MECH-295; **PROP: MECH-CUEWANT** |
| L7 | consumer readout (dACC/E3/commitment) non-zero & consequential | E3 goal_weight + MECH-295 + MECH-307; dACC does NOT read z_goal directly | **Stage 3** | **PROP: MECH-CONSUME** |
| L8 | pre-consummatory approach bias | beta gate + approach_commit | Stage 3 | ARC-030, MECH-229 |
| L9 | wanting != liking dissociation | NOT shown (514k = 0.0) | Stage 2-4 (after L2-L3) | MECH-117, MECH-229 |

**Closure thesis:** broken links are L2-L3 + measurement/wiring at L1 and L7.
L0/L1/L5 substrate-present; L6/L8 present-but-starved. Minimal repair = L2-L3 +
clean L1 positive control + L7 wiring audit. Not a new mature goal ecology.

---

## Status table

The resume primitive. Updated every session that touches goal-pipeline work.
See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | done | (substrate landed 2026-05-11; substrate_queue closed IGW-20260521-023 2026-05-21) | **DATE RECONCILED 2026-07-31 (docs-only, no status change): row was frozen at 2026-05-11; node record (`last_updated`) has since advanced to 2026-05-21.** Per node `completion_note`: canonical substrate-readiness V3-EXQ-540g PASSED 2026-05-15; substrate_queue closed IGW-20260521-023 2026-05-21. GAP-2/GAP-4 behavioural retests are downstream queue items owned by those gaps, not this one. **Prior row text (2026-05-11) retained below.** Queue 4-arm discriminative pair via /queue-experiment under master flag use_mech307_conjunction=True. **NOTE 2026-05-11 (EXQ-550 review):** V3-EXQ-550 FAIL sustains MECH-269 V_s monostrategy substrate-level reading at no-training depth; same run surfaced wired-but-inert z_goal pipeline (1200/1200 update_z_goal calls, z_goal_norm_peak=0.0) -- see decision-log 2026-05-11 entry. V3-EXQ-551 (pipeline-entropy diagnostic) + V3-EXQ-552 (forced-exploration warmup) queued by parallel sessions to narrow mechanism before trained-z_goal follow-up. | V3-EXQ-540g (substrate-readiness PASS 2026-05-15) | 2026-07-31 (row reconcile; node record 2026-05-21) |
| GAP-2 | 2 | done | (none) | **ROW RECONCILED 2026-07-31 (docs-only): status was `blocked`, node record has been `done` since 2026-06-15.** V3-EXQ-514o LANDED PASS/supports 2026-06-15 -- the terminal L9 object-bound wanting!=liking dissociation scored `mean_object_bound_wl_dissoc_fraction=0.80` (>= 0.6 pre-registered), n_scored_wl_steps 5/6/7 across seeds, both readiness gates met, non_degenerate=true, with the channel-write firing during real foraging. MECH-229 recorded as a genuine supports (exp_conf 0.868); its substrate_ceiling + pending_retest_after_substrate were LIFTED at the 2026-06-15 cycle. This also closed `goal_pipeline:GAP-7`'s sole residual (see that row). See node `governance_2026_06_15`. | V3-EXQ-514o (PASS 2026-06-15, reviewed) | 2026-07-31 (row reconcile; node record 2026-06-15) |
| GAP-3 | 3 | done | (none) | Closed 2026-05-20: V3-EXQ-582a PASS (floor=0.9); MECH-306 registered; Option 1 EMA not discriminative winner (582 FAIL). | V3-EXQ-582a | 2026-05-20 |
| GAP-4 | 4 | in-progress | Q-040.c (dACC weight-delta vs precision-weighted PE) unresolved | **ROW RECONCILED 2026-07-31 (chip-20260729-goal-gap4-row-reconcile): NOT a blind reconcile-to-done, per user decision.** The node frontmatter (`goal_pipeline:GAP-4`) has read `status: done` since 2026-06-09 -- but that closure was a **re-scope**, not a full clearance of everything the row's Owner-EXQ column named: `governance_2026_06_09` re-scoped MECH-295 to the modulatory reading and closed the GAP on the strength of V3-EXQ-490j falsifying behavioural-NECESSITY (severed-bridge approach_commit_rate=1.0 in 3/3 seeds via parallel first-class pathways) and 490k confirming the modulatory-sufficiency retest is defeated by a substrate ceiling owned elsewhere. Of the row's original owner-EXQs: **V3-EXQ-490g** was re-lettered forward (490g->h->i->j->k) and its question WAS answered -- the 2026-06-09 closure rests on 490j/490k's evidence; this part of the row was simply stale, not open. **V3-EXQ-471a** is superseded by V3-EXQ-490b (same StepHarness-corrected retest, ran under the 490 lineage instead). **V3-EXQ-475a** ran (SD-036 GABAergic decay retest, claims SD-036/MECH-279) but does NOT cover Q-040's third sub-question -- claims.yaml Q-040's 2026-05-08 decomposition explicitly names "EXQ-475a-conditions retest measuring dACC weight delta as a function of |precision-weighted forward-PE|" (Q-040.c) as a still-outstanding test, and no run in this cohort computes that correlation. Q-040 itself stays `status: open` in claims.yaml with Q-040.c as its named residual. **Successor queued 2026-07-31: V3-EXQ-475b** (`v3_exq_475b_q040c_dacc_pe_weight_delta_correlation.py`) -- 475a-conditions gap4-operating substrate (gaba decay + PAG freeze + dACC ON) factorial on MECH-269b `use_vs_rollout_gating` OFF/ON, measuring per-step Spearman rho of dACC's precision-weighted PE (`bundle["pe"]`) against its behavioural-adjustment magnitude (`\|\|agent._dacc_last_bias\|\|`), with gate-firing (P1) and dACC-engagement (P2) preconditions gating a substrate_not_ready_requeue self-route before any verdict is read. `validate_experiments.py --strict` clean; `--dry-run` smoke ran end-to-end (self-routed substrate_not_ready_requeue at smoke scale, as expected -- the V_s gate needs full episode count to cross its hold trigger, matching the 490/490a precedent). **Queue write deferred**: `ree-v3/experiment_queue.json` was under an active TASK_CLAIMS lock (`elastic-merkle-e0cca8` -> `frosty-satoshi-2e7cbc` in succession) for the whole of this session; see WORKSPACE_STATE.md follow-up. This row stays `in-progress` until 475b is queued AND lands with a verdict. **UPDATE 2026-08-10 (/governance cycle queue-depth-low-ops-aac785, row-date-sync only, status/prose otherwise unchanged): V3-EXQ-475b RAN 2026-08-01, non_contributory (z_harm_a wiring config bug). Successor V3-EXQ-862 (2026-08-02) and V3-EXQ-862a (2026-08-03, confirmed failure_autopsy_dacc-cluster-862a-870a_2026-08-03) also landed non_contributory -- third consecutive non-engagement finding, each a different config/threshold bug (475b: z_harm_a wiring; 862: dacc_weight=0 consumer gain; 862a: the ON/OFF manipulation itself never crosses, since it borrows the 490b threshold rather than a z_harm_a-calibrated one). 862a's confirmed routing calls for a further requeue with a z_harm_a-calibrated threshold + a preflight non-engagement assertion -- not yet queued as of this cycle. Q-040 stays `status: open` in claims.yaml with Q-040.c still the named residual. Row correctly stays `in-progress`; current owner is the not-yet-queued 862a-routed successor, not 475b.** | V3-EXQ-490g/h/i/j/k (superseded by 490j/490k, closed the necessity/sufficiency reading), V3-EXQ-471a (superseded by V3-EXQ-490b), V3-EXQ-475b (RAN non_contributory 2026-08-01, superseded by 862/862a), **862a-routed successor (current owner, Q-040.c, not yet queued)** | 2026-08-10 (row reconcile; 475b/862/862a landed, next successor still owed) |
| GAP-5 | 5 | done | (superseded-by-implementation) | Closed 2026-06-15: cascade BUILT + LANDED (ree-v3 main 2026-05-31T13:00Z) independent of the obsolete 'Phase 4 Tier-3 fidelity-gap' trigger; all 7 consumers carry the per_axis_drive kwarg; V3-EXQ-618 readiness diagnostic PASS (4/4 criteria, non_contributory). Behavioural validation (V3-EXQ-619, reserved) is owned by GAP-2, not GAP-5. See frontmatter completion_note. | V3-EXQ-618 | 2026-06-15 |
| GAP-6 | 6 | done | (none) | Substrate implemented (use_vs_gate_staleness_lookup wired end-to-end). V3-EXQ-490b C1 PASS; 490c/e/f factorial shows MECH-295 dominant cause. Monostrategy resolved by ARC-065 SP-CEM default 2026-05-17. Q-040b behavioral sufficiency continues under v_s_invalidation_runtime.md. | V3-EXQ-490b | 2026-05-17 |
| GAP-7 | 7 | done | nothing (`blocked_by: []`) | **CLOSED 2026-06-15 — this row was frozen at 2026-06-10 and is reconciled here (2026-07-29, docs-only) to the node record `governance_2026_06_15`.** Closure (Case 1, PASS via the GAP-2 close): the entire L2-L8 substrate was built and the only unfinished criterion was the TERMINAL L9 wanting!=liking dissociation, gated on `goal_pipeline:GAP-2` supplying reliable foraging contact. **V3-EXQ-514o LANDED PASS/supports 2026-06-15** — object-bound wanting!=liking dissociation `mean_object_bound_wl_dissoc_fraction=0.80` (>= 0.6 pre-registered), n_scored_wl_steps 5/6/7 across seeds, both readiness gates met, non_degenerate=true, with the channel-write firing during real foraging — which closed GAP-2's L9 and therefore this node's sole residual. MECH-229 recorded as a genuine supports (exp_conf 0.868); its substrate_ceiling + pending_retest_after_substrate were LIFTED at the 2026-06-15 cycle. status blocked_pending_substrate -> done; blocked_by cleared. **All four owner-EXQs below have run and are reviewed** (636, 637, 626b, 640a) — the row's prior `blocked_pending_substrate` did not mean "waiting on those". **Prior row text (2026-06-10, retained for reconstruction):** **L1 CLOSED + L7 AUDIT DONE + L2-L3-L4 SUBSTRATE LANDED 2026-06-04.** L1: 626b forced-seed positive control PASS (full-run, reviewed). L7 audit: only E3 goal_proximity reads z_goal consequentially; dACC/cingulate/policy/governance stack z_goal-blind; L7 wiring folded into L2-L3 (nothing object-bound to read until then). **L2-L3-L4 LANDED: SD-057 (ree-v3 53f6427; claims 1f12a8e60f) -- IncentiveTokenBank in goal.py binds benefit to SD-049 object identity (L2 MECH-344), accrues a per-object slow-decay revaluable token with at-recall per-axis drive-specific wanting (L3 MECH-345), and seeds z_goal FROM the most-wanted object's embedding (L4 MECH-346; amends MECH-230). Default-OFF bit-identical, no trained params. Contracts 6/6 + 747/751 + 7/7 preflight.** V3-EXQ-636 (L2-L4 mechanism) PASS full-run 4/4 (binds 2 types, 5/6 wanting!=liking events ON, 0 OFF, legacy seeding intact). **PHASE-2 (L6+L7) LANDED 2026-06-04: SD-057 phase-2 (ree-v3 24f31e5; claims e79ef7207e) -- L6 MECH-347 cue-recall (GoalState.cue_pull + agent.cue_recall_wanting: a perceived cue raises wanting for the matched object before benefit, identity-matched/drive-specific; downstream MECH-295 approach + E3 goal_proximity unchanged) + L7 MECH-348 dACC object-discriminative readout (per-candidate goal_proximity -> dACC bundle goal_readout -> DACCtoE3Adapter bias; dACC no longer z_goal-blind). Default-OFF bit-identical, no trained params. Contracts: phase-2 5/5 + 750/757 + 7/7 preflight.** Validation V3-EXQ-637 (forced-cue diagnostic, claim_ids=[], decoupled from GAP-2) queued; dry-run PASS 4/4 (C1 cue fires; C2 identity-matched z_goal direction cos=1.0; C3 goal_readout reaches dACC; C4 OFF parity). **The full GAP-7 closure map (L0-L9 substrate) is now built. NEXT: (a) 637 full-run PASS; (b) the GAP-2-gated L9 behavioural retest of MECH-229/MECH-117/ARC-030 -- now the sole remaining critical-path dependency, owned by scaffolded_sd054_onboarding / goal_pipeline:GAP-2.** **RECLASSIFIED 2026-06-10 open -> blocked_pending_substrate (blocked_by goal_pipeline:GAP-2): substrate L0-L8 built, only the GAP-2-gated L9 remains, so this is not a live build node. The L6 cue-recall sub-thread is SETTLED -- V3-EXQ-640a landed 2026-06-06 + autopsied (failure_autopsy_V3-EXQ-640a_2026-06-06): the cue REACHES z_goal (per-fire pull ~0 is a saturation artifact; absolute z_goal_at_cue_fire ~0.5 vs 0.42 OFF), and the bottleneck is z_goal->approach selection-authority propagation = the 604a/624a/614d modulatory-bias 'drowning' shape; routed to substrate_queue modulatory-bias-selection-authority (implemented); 638b stays gated. GAP-2 itself nearly cleared 2026-06-10 (V3-EXQ-603m: survival 3/3 + contact 3/3 + consumption-gated z_goal 2/3; residual = G0-artifact re-val 603n queued). NOT V4: SD-057 binds to the SD-049 per-TYPE tag (V3); the ARC-080 token-instance object-file spine is the separate V4 concern that lists SD-057 as a consumer.** | **V3-EXQ-514o (L9, PASS 2026-06-15 — the run that closed the node)**; V3-EXQ-636 (L2-L4, PASS, reviewed) + V3-EXQ-637 (L6-L7, PASS, reviewed); 626b (L1, PASS, reviewed); 640a (L6 propagation, ran 2026-06-06, autopsied, reviewed) | 2026-07-29 (row reconcile; node record 2026-06-15) |

Status values: `open`, `in-progress`, `blocked`, `paused`, `done`, `deferred`,
`tracked`. A `paused` row carries a resume condition in the
[Decision log](#decision-log). A `tracked` row indicates the implementation is
owned by another plan; this plan only consumes the result.

---

## Test cohort

The discriminative experiments by phase. EXQ IDs are pre-registered where
landed; "TBD" indicates the queue-experiment skill must allocate the next
letter at write time.

### Phase 1 cohort (MECH-307 conjunction)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| TBD | MECH-307 4-arm conjunction discriminative pair (all-four-gaps-fixed vs each-gap-removed) | non-zero cue_fires + dacc_bias + approach_commit in all-fixed arm; collapse to baseline in each lesioned arm | not queued |

### Phase 2 cohort (SD-049 Phase 2 behavioural under MECH-307)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| V3-EXQ-514g (TBD letter) | SD-049 Phase 2 reef behavioural validation under MECH-307-fixed substrate | classifier_loss < 0.005; probe_acc > 0.70; goal_resource_r lift ARM_2-ARM_0 >= 0.4; wanting!=liking trajectory fraction >= 0.6 in ARM_2; per-axis-drive ANOVA p < 0.01 | gated on Phase 1 PASS |

### Phase 3 cohort (SD-012 sustained-drive amendment)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| V3-EXQ-582 | Option 1 drive_ema_alpha sweep {0.01,0.02,0.2,1.0} | A1-A4 on alpha=0.02 arm | FAIL 2026-05-17 (escalate Option 2) |
| V3-EXQ-582a | Option 2 drive_floor sweep {0.0,0.3,0.6,0.9,1.2} | A1-A4 on floor=0.9 arm | PASS 2026-05-19 (GAP-3 done) |

### Phase 4 cohort (Tier-1 StepHarness + Q-040 cascade retest)

| EXQ | Subject | Prior verdict | Re-run trigger |
|---|---|---|---|
| V3-EXQ-490g | Q-040 cascade test under MECH-307 + SD-012 amendment + StepHarness | EXQ-490f non_contributory (pre-MECH-307 confound) | Phase 1 + Phase 3 PASS |
| V3-EXQ-471a | EXQ-471 catatonic-lock factorial under StepHarness | EXQ-471 non_contributory (pre-MECH-307 + drive collapse confound) | Phase 1 + Phase 3 PASS |
| V3-EXQ-475a | EXQ-475 retest under StepHarness | EXQ-475 superseded (update_z_goal TypeError) | Phase 1 + Phase 3 PASS |
| V3-EXQ-483c | EXQ-483 SD-037 retest under StepHarness | EXQ-483 superseded (update_z_goal TypeError) | Phase 1 + Phase 3 PASS |
| V3-EXQ-524a | EXQ-524 retest under StepHarness | EXQ-524 superseded (update_z_goal TypeError) | Phase 1 + Phase 3 PASS |

Tier-1 acceptance per experiment: non-zero approach_commit_rate in the relaxed-floor
arm relative to baseline; cue_fires > 0; dacc_bias non-zero. Tier-2
(514f-style retest) and Tier-3 (490e/f, 524, 536-cluster) gated on Tier-1
PASS, per the 2026-05-08 governance redirect.

### Phase 5 cohort (SD-049 Phase 3 consumer cascade)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| V3-EXQ-618 | per-axis drive consumer-cascade readiness: per_axis_drive evolves; no crash; AIC reads per-axis; MECH-295 axis routes | C1 min_peak>0.02; C2 no crash; C3/C4 L1>0 | DONE 2026-05-31 -- 4/4 PASS (non_contributory readiness diagnostic); cascade landed ree-v3 main 2026-05-31 |

### Phase 6 cohort (MECH-269b-followup-A)

| EXQ | Subject | Acceptance | Status |
|---|---|---|---|
| V3-EXQ-490b | Q-040 factorial distinguishing MECH-269b vs MECH-295 as dominant cause of EXQ-471 catatonic-lock | clean factorial separation in 2x2 design | already pending in queue |

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 | MECH-307 (priority=1) | MECH-307; SD-014 (fallback amendment) | anticipatory_affect_conjunction_vs_dual_channel.md |
| GAP-2 / Phase 2 | SD-049-PHASE-2 | SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030 | sd_049_multi_resource_heterogeneity.md |
| GAP-3 / Phase 3 | SD-012 + MECH-306 (drive_floor validated) | SD-012, MECH-306, MECH-216, ARC-051 | sustained_drive_anticipatory_wanting.md |
| GAP-4 / Phase 4 | MECH-295 (priority=1) | MECH-295, ARC-030, MECH-117, Q-040 | mech_295_drive_liking_approach_bridge.md |
| GAP-5 / Phase 5 | SD-049-PHASE-3 (DONE 2026-06-15; landed ree-v3 main 2026-05-31, V3-EXQ-618 readiness PASS) | SD-032b (read-side fidelity); no acceptance gate | sd_049_multi_resource_heterogeneity.md |
| GAP-6 / Phase 6 | MECH-269b-followup-A (priority=1) | MECH-269b | v_s_invalidation_runtime.md |

The substrate_queue.json design_doc field updates are made in the same session
as this plan registration: MECH-307, MECH-295, SD-049 (Phase 1 main), SD-049-PHASE-2,
SD-049-PHASE-3, MECH-269b-followup-A all updated to point to this plan as the
canonical sequencing reference, in addition to their existing mechanism-specific
design docs (those remain the authoritative single-claim references; the plan
is the umbrella).

### Boundary with sleep_substrate_plan.md

The SD-049 sleep-on cohort (V3-EXQ-514 family configured with `use_sleep_loop=True`,
`sws_enabled=True`, `rem_enabled=True`) sits at the boundary of both plans:

- **goal_pipeline_plan.md owns the SD-049 substrate** (Phase 1 env-only,
  Phase 2 hybrid encoder, Phase 3 consumer cascade), the wanting/liking
  behavioural acceptance criteria, and the wanting != liking trajectory
  fraction validation.
- **sleep_substrate_plan.md owns the sleep-loop side of validation**: the
  SleepLoopManager Phase A/B/C/D/E scaffolding, MECH-204 precision
  recalibration consumer, MECH-272 routing-gate downstream consumer wiring,
  MECH-273 replay-derived training targets, MECH-285 staleness-priority
  sampling.

When V3-EXQ-514 successors are configured with sleep flags ON, both plans'
acceptance criteria apply. The sleep flags are not part of the Phase 1 / Phase 2
goal-pipeline validation acceptance (which can run with `use_sleep_loop=False`);
they are part of the V3 full-stack validation that gates SD-049's promotion
beyond v3_pending and the SD-017 + MECH-204 + sleep cluster's full
end-to-end validation. Either plan may sequence a V3-EXQ-514 successor with
its respective flag stack; the other plan's status table tracks the dependency
under a `tracked` row.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-07-29 - GAP-7 row reconcile: table said `blocked_pending_substrate`, node has been `done` since 2026-06-15

**Docs-only. No experiments queued, no claims.yaml edit, no manifest touched.**

The GAP-7 Status-table row was frozen at 2026-06-10, showing
`blocked_pending_substrate` with all four owner-EXQs (636, 637, 626b, 640a)
listed. All four had in fact run and been reviewed well before that date -- the
`blocked_pending_substrate` never meant "waiting on those", it meant the
TERMINAL L9 wanting!=liking dissociation was gated on `goal_pipeline:GAP-2`
supplying reliable foraging contact. The row simply never recorded that the gate
then cleared.

Per node record `governance_2026_06_15`, the node has been **`done`** since
2026-06-15 (Case 1, PASS via the GAP-2 close): **V3-EXQ-514o landed PASS /
supports**, `mean_object_bound_wl_dissoc_fraction=0.80` against a pre-registered
>= 0.6, n_scored_wl_steps 5/6/7 across seeds, both readiness gates met,
`non_degenerate=true`, with the channel-write firing during real foraging.
MECH-229 was recorded as a genuine supports (exp_conf 0.868) and its
`substrate_ceiling` + `pending_retest_after_substrate` were lifted at that
cycle; `blocked_by` was cleared to `[]`. The row now says `done`, names 514o as
the closing run, and retains the 2026-06-10 text for reconstruction.

**Not touched, and flagged for a governance decision rather than reconciled
here:** the **GAP-4** row still reads `in-progress` / 2026-05-29 while its node
record has been **`done` since 2026-06-09** (user-approved decision: re-scope +
close -- necessity falsified, the modulatory reading stands and is
substrate-supported, and coupling closure to a 490L successor would just chain
it to the separate `scaffolded_sd054_onboarding` programme). Its listed owners
V3-EXQ-490g / 471a / 475a appear in queue history but produced no evidence
artefacts. That divergence was explicitly out of scope for this reconcile and
is left for whoever owns those runs. The **GAP-2** row was likewise left alone.

### 2026-06-05 - GAP-7 cue-recall contact-bridge thread routed (638a -> 640 -> 640a; 638b gated)

**Status:** Plan-of-record catch-up. Node stays `status: open`. This records the
SD-057 L6 cue-recall *behavioural* validation thread -- the GAP-2-gated arm the
phase-2 landing entry below flagged as the sole remaining deliverable -- run via
scaffolded_sd054_onboarding. No substrate change and no claim weighting: all
three experiments are diagnostics (`claim_ids=[]`), and both autopsies below are
already confirmed + governance-consumed (the routing here is recorded, not
re-decided).

**The thread (all on scaffolded_sd054_onboarding, ARM_OFF vs ARM_CUE_ON):**

- **V3-EXQ-638** (cue->contact bridge, first issue): cue-SILENT FAIL, C1 fired 0x.
  Root cause: `IncentiveTokenBank` empty entering P1/P2 (Stage-0 forced feed
  bound no token; `rt=_contacted_resource_type` ~always None). Formation fix
  `scaffold_stage0_bind_incentive_token=True` (ree-v3 a9ef0be) binds the Stage-0
  token to the strongest-perceived type; smoke showed the bank populating.
- **V3-EXQ-638a** (re-issue WITH the formation fix): FAIL, non_contributory.
  C1 cue fires (1050/180/446) + C2 OFF silent + token bank 0->3 all PASS
  (formation fix worked); **C3 contact-lift FAIL** -- ARM_CUE_ON contact
  `[0.0, 0.0, 0.267]` <= ARM_OFF `[0.0, 0.197, 0.648]` on every matched seed,
  drive adequate (0.28) on a zero-contact seed. Measurement-reliability check:
  the `n_cue_recall_fires` aggregation fix (ree-v3 636128a, 2026-06-04 15:50Z)
  PREDATES the 638a manifest (18:36Z), so the cue-fire counts are read through
  the fixed path, not the buggy `getattr(...,0)=0` path -- the numbers are
  reliable. Autopsy `failure_autopsy_V3-EXQ-638a_2026-06-05.{md,json}`
  (d7b316d859): cue is inert-to-counterproductive; 638a CANNOT discriminate
  authority / gradient-following / interoceptive / orienting because no post-cue
  action trace was logged. Routing = measurement-first.
- **V3-EXQ-640** (measurement-only post-cue instrumentation, ree-v3 ffaeda5;
  behaviourally identical to 638a + per-cue-fire trace): SETTLED the branch.
  Autopsy `failure_autopsy_V3-EXQ-640_2026-06-05.{md,json}` (f2a65e1d0d):
  **cue-to-action AUTHORITY missing** -- cue fired 713/296/548x but moved z_goal
  ~0.4% (`cue_zgoal_pull_norm` ~0.002 vs `||z_goal||` ~0.45) and post-cue
  approach == background; ARM_CUE_ON contact == ARM_OFF every seed. The 638a
  DISPLACEMENT hypothesis is REFUTED (z_goal norm at fire equal-or-higher than
  the ARM_OFF attractor norm); the cue is INERT, not counterproductive.
  Interoceptive reading is NOT the proximate cause (seed 42: 713 fires, z_goal
  preserved, zero approach lift). Proximate cause: `cue_recall_gain` 0.2 x weak
  token ~0.2 -> sub-threshold `cue_pull`.
- **V3-EXQ-640a** (cue-authority gain sweep, ree-v3 e4a25e5): **LANDED
  2026-06-06 + AUTOPSIED** (`failure_autopsy_V3-EXQ-640a_2026-06-06`, confirmed,
  user-gated; reviewed). 2-axis factorial `cue_recall_gain` {0.2,1.0,5.0} x
  `incentive_drive_kappa_weight` {2.0,10.0}. The pre-registered "gain=5.0 snaps
  z_goal" framing was CORRECTED by the autopsy: the per-fire
  `cue_zgoal_pull_norm` ~0 is a SATURATION artifact (the cue fires every step, so
  the incremental per-fire delta is ~0 while the ABSOLUTE `zgoal_norm_at_cue_fire`
  ~0.5 sits elevated above the 0.42 OFF reference -- the cue DOES reach z_goal).
  It is therefore NOT the "cue_pull primitive under-powered/clipped" branch. The
  load-bearing finding is the approach lift: across all 6 cells (25x gain x 5x
  kappa) post-cue approach lift over within-run background is flat-to-negative.
  Bottleneck = z_goal->approach PROPAGATION (MECH-295 liking-bridge / E3
  goal_proximity selection authority), the same modulatory-bias "drowning" shape
  as the 604a/624a/614d cluster. Diagnostic, `claim_ids=[]`.

**RESOLVED (updates the gating chain below, which is now stale):** 640a settled
the cue-recall thread. Routing applied (user-confirmed at the 2026-06-06 autopsy
gate): **implement-substrate (amend) on substrate_queue
`modulatory-bias-selection-authority`** (now `status: implemented, ready: true`),
carrying the 640a failure record alongside the MECH-314/320/341 levers. The clean
propagation re-test is `pending_retest_after_substrate` + blocked on GAP-2
foraging competence (so the approach-lift measure is meaningful) -- GAP-2 itself
nearly cleared 2026-06-10 (V3-EXQ-603m survival/contact/consumption legs; residual
G0-artifact re-val 603n queued). **V3-EXQ-638b interoceptive need-gating stays
GATED -- do NOT build** (hard-constraint CONFIRMED by the autopsy: cue authority
over z_goal is present and magnitude is not the bottleneck, so 638b's
cue-firing gate cannot fix a z_goal->approach propagation gap). This closes the L6
cue-recall sub-thread; GAP-7's only remaining criterion is the GAP-2-gated L9
acceptance, and the node was reclassified open -> blocked_pending_substrate on
2026-06-10.

**ORIGINAL gating chain (2026-06-05, now superseded by the RESOLVED note above):**
640a routes the cue-recall
thread. **V3-EXQ-638b (interoceptive need-gating arms:
OFF / EXTERNAL_ONLY / INTEROCEPTIVE+EXTERNAL) stays GATED behind 640a** -- do not
build the interoceptive substrate until the gain sweep settles whether
cue-to-action authority is reachable by strengthening the existing pull. If 640a
shows even a full z_goal snap does not lift contact, the bottleneck is GAP-2
foraging competence (the z_goal->approach->contact leg), not cue-recall, and the
thread hands back to goal_pipeline:GAP-2. This is the L9 wanting!=liking
behavioural-validation arm; MECH-229 / MECH-117 / ARC-030 stay v3_pending until
it resolves.

### 2026-06-04 - GAP-7 phase-2 LANDED (SD-057 L6 cue-recall MECH-347 + L7 dACC readout MECH-348)

**Status:** The full GAP-7 L0-L9 substrate is now built. Node stays `status:
open` -- the only remaining work is the L9 behavioural validation, which is
GAP-2-gated (foraging competence). Same-day follow-on to the L2-L3-L4 landing
(entry below), at user request.

**What landed.** SD-057 phase-2 (ree-v3 24f31e5; REE_assembly claims e79ef7207e):
- **L6 (MECH-347 `incentive.cue_triggered_wanting`):** a PERCEIVED cue (no
  benefit pulse) retrieves its incentive token and nudges z_goal toward that
  object's stored embedding BEFORE consumption -- identity-matched (pulls toward
  the cued object) and drive-specific (`base_value*(1+kappa*per_axis_drive)`).
  New `GoalState.cue_pull` (a directional z_goal nudge with no benefit gate and
  no token revaluation) + `agent.cue_recall_wanting`. The downstream MECH-295
  approach bridge + E3 goal_proximity (unchanged) translate it into
  pre-consummatory approach. The StepHarness auto-derives the strongest-perceived
  type from SD-049 per-type proximity views; the primitive is callable directly
  for forced-cue tests. Berridge 2009 / Corbit-Balleine specific PIT / Schultz
  DA-transfer.
- **L7 (MECH-348 `incentive.dacc_object_discriminative_readout`):** the dACC
  consumer now reads per-candidate goal_proximity to the (object-bound, L4)
  z_goal -- resolving the L7-audit finding that dACC was z_goal-blind.
  `DACCAdaptiveControl.forward` gains `candidate_goal_proximity` -> bundle
  `goal_readout` -> `DACCtoE3Adapter` adds an object-discriminative bias term,
  independent of dacc_weight. Balleine & O'Doherty 2010.

Both no-op-default (use_cue_recall / use_mech_consume), bit-identical OFF, no
trained parameters (no phased training). Contracts: phase-2
`test_sd_057_phase2_cue_recall_consume.py` 5/5 + 750/757 full (7 pre-existing
local-git-env runner fails) + 7/7 preflight. Loud-not-silent preconditions:
use_mech_consume requires use_dacc; use_cue_recall requires use_incentive_token_bank.

**Validation.** V3-EXQ-637 (forced-cue diagnostic, claim_ids=[], decoupled from
GAP-2 like 636/626b): phase-2 ON vs OFF. Dry-run PASS 4/4 -- C1 cue fires; C2
identity-matched z_goal movement (direction cosine = 1.0; raw cosine-to-cued is
degenerate in a non-navigated forced harness because z_object embeddings are
near-identical across types, so the metric is the movement DIRECTION); C3
goal_readout reaches the dACC bundle (len=K, finite); C4 OFF parity (no cue, no
readout). Queued via /queue-experiment.

**State of GAP-7.** L0-L9 substrate complete (L1 closed; L2-L3-L4 + L6-L7 landed;
L7 audit done). The sole remaining deliverable is the **L9 wanting!=liking
behavioural validation**, gated on goal_pipeline:GAP-2 supplying foraging contact
(owned by scaffolded_sd054_onboarding). MECH-229 / MECH-117 / ARC-030 stay
v3_pending until that retest runs.

### 2026-06-04 - GAP-7 L2-L3-L4 substrate LANDED (SD-057 object-bound incentive-salience layer)

**Status:** The GAP-7 middle layer is built. Node stays `status: open` (the L9
behavioural validation is GAP-2-gated, and phase-2 L6/L7 remain). This is the
substantive deliverable the L7 audit (same day, entry below) sequenced as NEXT.

**What landed.** `SD-057: drive.object_bound_incentive_salience` (ree-v3 commit
53f6427; REE_assembly claims commit 1f12a8e60f). An `IncentiveTokenBank`
(`ree-v3/ree_core/goal.py`) inserts a per-object incentive layer between the
benefit pulse and z_goal:
- **L2 (MECH-344):** on contact, benefit binds to the SD-049 per-type identity
  tag k (`resource_type_at_agent`) via `bank.update(k, benefit, z_resource)`
  -- the associative object->benefit node the legacy scalar gate lacked.
- **L3 (MECH-345):** each type accrues `base_value[k]` (slow-decay, revaluable
  EMA of received benefit) + `z_object[k]` (stored z_resource embedding).
  Wanting at recall = `base_value[k] * (1 + kappa * per_axis_drive[k])` --
  the Zhang 2009 multiplier relocated from the seeding gate onto the stored
  per-object value, per-axis so wanting is drive-specific / identity-matched
  (specific PIT).
- **L4 (MECH-346; amends MECH-230):** z_goal seeded FROM the most-wanted
  object's embedding (`argmax_k wanting[k]`) instead of the raw last-contacted
  z_resource. The GoalState firing gate is unchanged -- only the seed SOURCE.

**Why this is the closure of the middle layer.** Liking target (last-contacted)
and wanting target (z_goal -> most-wanted) can now DIFFER -- e.g. contact food
while thirsty -> z_goal points at water. The L9 `wanting!=liking_dissoc_fraction`
(stuck at 0.0 because the single attractor forced wanting==liking) is now
structurally expressible for the first time.

**Validation.** The behavioural L9 acceptance is GATED on goal_pipeline:GAP-2
supplying foraging contact, so SD-057's own validation is a forced-contact
MECHANISM diagnostic decoupled from GAP-2 (mirroring how V3-EXQ-626b decoupled
the L1 positive control): **V3-EXQ-636** (claim_ids=[], diagnostic) -- two
resource types forced under opposing per-axis drive, bank ON vs OFF, testing
`wanting_target != liking_target`. Queued + ingested into the coordinator DB;
dry-run PASS 4/4 (C1 binds 2 types; C2 5/6 wanting!=liking events ON; C3 0
events OFF; C4 legacy seeding intact). Contracts
`test_sd_057_incentive_token_bank.py` 6/6 + 747/751 full + 7/7 preflight;
default-OFF bit-identical, no trained parameters (no phased training).

**Scope held / deferred.** v1 = L2+L3+L4 core (user-confirmed scope). Deferred
to a phase-2 pass within SD-057, NOT registered: L6 cue-recall (MECH-CUEWANT --
re-trigger wanting from a perceived cue before benefit) and L7 dACC readout
wiring (MECH-CONSUME -- give dACC the object-bound goal readout). The L7 audit
established these are downstream of L2-L3, which is now in place.

**NEXT:** (a) V3-EXQ-636 full-run PASS; (b) the GAP-2-gated L9 behavioural
retest of MECH-229 / MECH-117 / ARC-030 (all stay v3_pending until then);
(c) phase-2 L6/L7.

### 2026-06-04 - GAP-7 L1 full-run confirmed closed + L7 consumer-readout audit delivered

**Status:** Two GAP-7 sub-deliverables resolved this session. Node stays
`status: open` (the L2-L3 object-binding + incentive-token substrate, with the
L7 readout-wiring now folded into it, remains). No new substrate written; no
claims registered; this session was audit + bookkeeping only.

**L1 -- full run confirmed (closes the prior "pending review" status).** The
V3-EXQ-626b full run had in fact landed: manifest
`v3_exq_626b_goal_pipeline_forced_seed_positive_control_20260603T211703Z_v3.json`
is `outcome: PASS` with all four acceptance criteria green at full budget:
- C1 positive-control formation: 3/3 seeds clear (peaks 0.464 / 0.551 / 0.615, floor 0.4)
- C2 stability: 3/3 (last-window medians 0.457 / 0.543 / 0.595, floor 0.1)
- C3 negative control: 3/3 (no-benefit arm peaks all 0.0, ceiling 0.05) -- proves the forced seed IS the signal, not a loop artifact
- C4 z_goal-off parity: 3/3 (peaks all 0.0)

It is in `review_tracker.json` (`v3_exq_626b`) and was walked in the 2026-06-04
governance cycle (`c28e0ba209`, "626b positive control" among the 4 PASS); it is
not in `pending_review.md`. So L1 is CLOSED, not merely queued -- the earlier
decision-log "full-run PASS pending a runner + governance review" line is
superseded.

**L7 -- consumer-readout wiring audit delivered (source audit against
ree-v3/ree_core).** The "does dACC / E3 / commitment actually read z_goal"
question is now answered with file:line precision:
- **WRITE / exposure:** `GoalState.update()` / `.with_injection()`
  (`ree_core/goal.py:148,240`); the z_goal tensor via the `.z_goal` property
  (`goal.py:144`); the `goal_proximity()` = 1/(1+MSE(z_world, z_goal)) scalar
  (`goal.py:226`).
- **E3 (action-selection scorer)** reads z_goal ONLY via `goal_proximity` -- a
  scalar -- gated on `config.goal_weight > 0`
  (`ree_core/predictors/e3_selector.py:461,618-629`; MECH-112 / MECH-117 wanting
  term). This is the SOLE path by which z_goal biases which action is chosen.
- **E1** reads the z_goal TENSOR directly as LSTM conditioning
  (`ree_core/agent.py:2642,2653`; MECH-116) -- shapes world-model prediction,
  not action choice directly.
- **Action selection** injects a norm FLOOR (`agent.py:3109`; MECH-188
  `with_injection`) but still routes through the same goal_proximity scalar.
- **dACC reads NEITHER z_goal NOR goal_state** -- `forward()` takes only
  `drive_level: float` + `per_axis_drive` (`ree_core/cingulate/dacc.py:325-335`).
  The plan's "dACC does NOT read z_goal directly" claim is CONFIRMED.
- **The whole cingulate / regulator / governance / policy stack is z_goal-blind:**
  `salience_coordinator`, `broadcast_override` (SD-037),
  `pag/freeze_gate` (MECH-279), `policy/gated_policy` (ARC-062),
  `pfc/lateral_pfc_analog` (SD-033a), `pfc/ofc_analog` (SD-033b),
  `governance/closure_operator` (SD-034) -- all read `drive_level` (collapsed
  scalar) / `per_axis_drive` / z_harm / z_world, never z_goal.
- Indirect non-action consumers: `ghost_goal_bank` (MECH-292) and ghost-probes
  (MECH-293) read z_goal via stored cosine-matched snapshots.

**Audit payload (the architectural finding, not just the map):** the only
readout that makes a non-zero z_goal behaviourally consequential is the E3
goal_proximity term -- proximity of z_world to a SINGLE z_goal attractor point.
There is structurally no surface today that could express *per-object* wanting,
because z_goal is one attractor and proximity is to that point, not to an object
identity. Therefore the L7 "wire the missing readouts" sub-step is NOT a
standalone no-new-substrate task as originally scoped: wiring dACC (the natural
"is this goal worth the effort" site) to read z_goal would only hand it the same
single-attractor proximity scalar. L7-wiring is entangled with and downstream of
L2-L3 (object-binding + per-object incentive token) -- the readout cannot be made
object-discriminative until there is an object-bound token to read.

**Decision:** fold the MECH-CONSUME (L7) readout-wiring into the L2-L3
`/implement-substrate` design rather than queue it standalone. The AUDIT half of
the L7 deliverable is done; the WIRING half is sequenced behind L2-L3. NEXT
GAP-7 deliverable is therefore the L2-L3 object-bound incentive-salience layer
(design-discovery; no SD/MECH doc yet; proposed_claims remain placeholders, NOT
registered). Surfaced to user for the L2-L3 design-session go-ahead.

### 2026-06-03 - GAP-7 L1 landed: forced-seed positive control (V3-EXQ-626b) + 626-class harness defect closed

**Status:** L1 sub-deliverable of GAP-7 delivered. Node stays `status: open`
(L7 + L2-L3 remain). First unblocked GAP-7 step per the ratification: the L1
harness positive control + 626-class Class-1 fix, which depends on the harness
fix NOT on GAP-2.

**What was verified / landed:**

- **626 Class-1 wiring defect CLOSED.** The original 626 bespoke loop never
  called `agent.update_z_goal`, so z_goal stayed at zero-init across all arms.
  626a wired it; the 2026-06-03 cluster autopsy
  `failure_autopsy_V3-EXQ-603e-626a-622` confirms "the goal-pipeline WIRING
  layer is closed and verified."
- **L1 forced-seed positive control passes at the unit level.**
  `ree-v3/tests/contracts/test_goalstate_forced_seed_positive_control.py` is
  6/6 green (forced supra-threshold seed -> non-zero, direction-stable z_goal).
- **V3-EXQ-626b queued + ingested into the coordinator DB** (supersedes
  V3-EXQ-626a; `claim_ids=[]`, `experiment_purpose=diagnostic`). It bakes a
  genuine FORCED-SEED positive-control arm into the developmental-window
  diagnostic itself -- benefit forced supra-threshold fed to `update_z_goal`
  every step (the `run_stage0_nursery` pattern), decoupled from foraging --
  plus a no-benefit negative control (proves the signal is the seed) and a
  z_goal-off parity control. So the harness can SEE a non-zero stable z_goal
  that depends ONLY on the harness fix + the GoalState gate, NOT on the GAP-2
  foraging-competence substrate. Dry-run smoke PASS (C1 forced-seed formation
  >=0.4 / C2 stability / C3 negative-control no-seed / C4 OFF-parity all True).
  **[Updated 2026-06-04: full run landed PASS + reviewed -- see the 2026-06-04
  decision-log entry above. This "pending" status is superseded.]**

**The correction L1 makes precise:** 626a's experiment-level positive control
FAILED on 2/3 seeds only because its ARM_A drew benefit from *ecological
foraging* -- seeds that never foraged (a GAP-2 leak) showed z_goal=0, and the
harness could not separate "signal absent" from "signal present but inert."
That 2/3 failure is GAP-2's foraging-competence ceiling, NOT a harness defect.
626b's forced-seed arm removes the confound so L1 is testable independent of
GAP-2.

**Scope held:** L1 forced-seed positive control + 626-class fix ONLY. Did NOT
touch the L2-L3 object-binding / incentive-token substrate (later
/implement-substrate; placeholders MECH-BIND-obj / MECH-INCENT-token NOT
registered) and did NOT do the L7 audit. No claims.yaml edits.

**Next deliverable: L7 consumer-readout wiring audit** -- audit whether
dACC / E3 / commitment actually read z_goal (today dACC does NOT read z_goal
directly per the closure map) and wire the missing readouts so a non-zero
z_goal is consequential. Then L2-L3.

### 2026-06-03 - GAP-7 ratified into plan + closure map embedded

**Status:** plan-of-record addition. User ratified the GAP-7 proposal that had
been parked in `thought_intake_2026-06-01_goal_wanting_liking_stream_repair.md`
section 9 ("PROPOSALS for the governance owner; this session does not edit the
plan body"). It is now a live node.

**What landed this session:**

- New `goal_pipeline:GAP-7` frontmatter node (status `open`, severity
  `load-bearing`, owner_exq `null`/design-discovery, depends_on
  `goal_pipeline:GAP-2`).
- Gap-inventory row, Phase 7 deliverables section, and status-table row.
- The L0-L9 **closure map** is now embedded in the plan body (Phase 7
  subsection) -- previously it lived only in the intake doc. This is the "in the
  map" half of the request: the /closure renderer reads `closure_plan:`
  frontmatter, and the human-readable L0-L9 link map now travels with the plan.

**The thesis GAP-7 encodes:** the goal stream's broken links are L2-L3 (the
benefit signal at contact is never bound to object IDENTITY and there is no
per-object incentive-salience TOKEN) plus measurement/wiring at L1 (forced-seed
positive control, blocked by the 626 harness bug) and L7 (dACC does not read
z_goal directly). GAP-7 is sequential-downstream of GAP-2: GAP-2 is the
developmental foraging-competence ceiling (get the agent to contact a resource
at all); GAP-7 is what happens to the benefit signal once contact occurs.
V3-EXQ-623 (MECH-104) is the cross-evidence positive control that REE DOES turn
a correctly-wired signal into behaviour, so the fault is upstream, not in
signal->behaviour conversion.

**What is NOT done (deliberately):**

- No claims.yaml registration of `MECH-BIND-obj` / `MECH-INCENT-token` /
  `MECH-GOALPTR` / `MECH-CUEWANT` / `MECH-CONSUME` -- these stay as `proposed_claims`
  placeholders on the node until /implement-substrate design-discovery assigns
  real IDs.
- No substrate_queue entry, no experiment scripts, no queue entries. The L1
  harness positive control + 626a Class-1 fix is the unblocked first deliverable
  and routes through /queue-experiment (or /diagnose-errors for the harness fix)
  in a separate session.

### 2026-05-31 - Scope clarification: prereq (2) of GAP-C (z_goal collapse) is NOT owned by GAP-4

**Status:** documentation correction. No new substrate or experiment work owed by this entry.

`behavioral_diversity_isolation_plan.md` GAP-C `resume_condition` (and earlier mentions in
the closure-distance bookkeeping) listed prereq (2) -- "goal-pipeline training regime
produces non-trivial z_goal in default config" -- as `OPEN ... owned today by
IGW-20260528-016 / goal_pipeline:GAP-4 / V3-EXQ-490g cohort`. The attribution is wrong.

The 2026-05-29 V3-EXQ-490g cohort autopsy explicitly split the cohort into two
structurally distinct clusters (`failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md` section
6). Cluster A (V3-EXQ-483c / 524a / 471a / 475a / 490g/h/i/j) is a GAP-4 Tier-1 library
measurement-gap operating on the gap4 substrate (`drive_floor=0.9, drive_ema_alpha=1.0,
goal_stream=True, use_dacc=True`); the goal pipeline is firing across all runs
(`goal_norm` 0.09-0.36 in 483c; `goal_active_fraction = 1.0` in 490j ARM_1). Cluster B
(V3-EXQ-603c) is the 591 substrate-uniform z_goal-zero family member; it was routed
2026-05-29 to `/implement-substrate` for scaffolded SD-054 onboarding -- a new substrate
(`scaffolded_sd054_onboarding`, design memo `sd_054_scaffolded_onboarding_substrate_design.md`)
that anneals `mech295_min_drive_to_fire` 1.0 -> 0.01 and `mech307_conjunction_z_beta_threshold`
0.6 -> 0.3 across a P0/P1/P2 phased training scheduler against the SD-054 reef as a
scaffolded start-state distribution. The substrate_queue.json entry is `scaffolded_sd054_onboarding`
(priority 1, `status: pending_implementation`); the IGW item is IGW-20260531-029.

The 490 cohort cannot, by configuration, close prereq (2). It does not run in the default
config; it runs in the gap4 config where z_goal is known to fire. Prereq (2) asks whether
the substrate produces z_goal in the DEFAULT config under random-policy training -- a
distinct question with a distinct owner.

**Action taken this session:**

- Added `scope_clarification_2026_05_31` to GAP-4's plan-node frontmatter making explicit
  that GAP-4 owns the MECH-295 cascade behavioural validation (Phase 4) ONLY, not GAP-C
  prereq (2).
- Updated `behavioral_diversity_isolation_plan.md` GAP-C `resume_condition` to point
  prereq (2) ownership at `scaffolded_sd054_onboarding` instead of the 490 cohort.
- Wrote the triage memo `evidence/planning/z_goal_collapse_triage_2026-05-31.md` that
  documents the classification (b) substrate-structural finding, the z_goal code trace
  showing why default config collapses to ~1e-7 (`benefit_threshold=0.1` gate not
  cleared without drive amplification via `drive_floor`), and the confirmation that
  today's other landings (SD-049 Phase 3 commit `3d276e5`, MECH-090 wiring,
  InfantCurriculumScheduler H_POS_FRAC recal commit `da4a1bc`) do not change the
  substrate-design memo's specification.

**What is NOT done:**

- `/implement-substrate` on `scaffolded_sd054_onboarding`. Owned by IGW-20260531-029,
  separate session.
- V3-EXQ-490k or any other queue-experiment routing. The 490 cohort's MECH-295
  narrowing path (per 490j autopsy section 9) is a downstream governance + queue-experiment
  item, orthogonal to prereq (2).
- claims.yaml or substrate_queue.json edits.

### 2026-05-29 - V3-EXQ-490g cohort cluster autopsy landed; GOVERNANCE APPLICATION PENDING

**Status:** autopsy artifact landed; recommendations NOT yet written into the registry.

The V3-EXQ-490g cohort (Tier-1 StepHarness retests for MECH-295 cascade
behavioural validation under GAP-4) produced three FAILs the 2026-05-27
V3-EXQ-591 autopsy did not enumerate: V3-EXQ-483c FAIL mixed 2026-05-21,
V3-EXQ-524a FAIL non_contributory 2026-05-21, V3-EXQ-603c FAIL 2026-05-27.
The 490g letter itself was never queued. Cluster autopsy landed 2026-05-29
on REE_assembly master 12f0dda773 at
`failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.{md,json}`.

**Key finding (overturned the incoming hypothesis):** the three FAILs do
NOT share root cause. 483c and 524a are a GAP-4 Tier-1 library
measurement-gap (goal pipeline IS firing -- goal_norm_peak 0.09-0.36;
bridge_cue_fires 3-34; approach_commit_rate=1.0 saturated -- but C2 measures
a substrate that wasn't enabled and C3 saturates trivially); same Tier-1
library template gap the 2026-05-24 V3-EXQ-483c autopsy already named.
603c IS substrate-uniform z_goal-zero (P0+P1 phased training was
insufficient; most cells aborted at P0 RV-not-converging or Fix D survival
gate). Two structurally distinct clusters; user-confirmed two-fork
disposition (F1) via AskUserQuestion.

**Routing decisions (two forks):**

- **Fork A** (483c, 524a, and the unrun 471a / 475a / 490g letters):
  routing = `/queue-experiment` (Tier-1 library rebuild +
  V3-EXQ-483d successor + the rest of the cohort under the rebuilt
  library). `recommended_substrate_queue_entry.action = none`
  (experiment-script library fix in
  `ree-v3/experiments/_lib/goal_pipeline_tier1.py` +
  `ENV_FISHTANK_KWARGS`, NOT a ree_core/ substrate change). Library
  changes needed: add `use_dacc=True` default; replace `C3_lift_vs_baseline`
  metric (saturates at 1.0 under drive_floor=0.9 + goal_stream + reef)
  with `override_signal_nonzero_steps` (SD-037-specific) or
  `goal_norm_peak delta vs baseline` (cross-claim). Spawned as a session
  chip 2026-05-29.

- **Fork B** (603c): routing = `/implement-substrate`. Cluster-absorbs
  into the 591 substrate-uniform z_goal-zero family per
  `failure_autopsy_V3-EXQ-591_2026-05-27.md` Section 6.
  `recommended_substrate_queue_entry.action = create` for
  `SD-XXX-scaffolded-sd054-onboarding` (governance assigns real ID;
  priority_suggested=1; unblocks Q-045, MECH-313, MECH-260, MECH-295,
  MECH-307, MECH-117, SD-049 Phase 2 behavioural, ARC-030, Q-040).
  User-chosen sub-lever (A2): SD-054 reef + bipartite-horizontal as a
  scaffolded onboarding start-state distribution so the trained policy
  inhabits goal-rich states during training. Substrate-design memo
  (sibling pattern to `e2_action_divergence_substrate_design.md`)
  spawned as a session chip 2026-05-29; the follow-on
  `/implement-substrate` lands the code change once the memo lands.

**Pending governance application (LOAD-BEARING):** the autopsy's
recommended writes have NOT been applied to the registry yet, and
**they will NOT be auto-surfaced by the next `/governance` walk** because
the three manifests already have evidence_direction set and are no longer
in `pending_review.md`. Specifically pending:

1. V3-EXQ-483c manifest: run-level evidence_direction `mixed -> non_contributory`;
   `evidence_direction_per_claim["SD-037"] = "non_contributory"` (was
   `weakens`); evidence_direction_note pointing at this cohort autopsy.
2. V3-EXQ-524a manifest: evidence_direction_note pointing at this
   cohort autopsy (run-level direction stays non_contributory).
3. V3-EXQ-603c manifest: evidence_direction_note pointing at this
   cohort autopsy (cluster-absorb into 591 family).
4. claims.yaml SD-037: append evidence_quality_note per autopsy JSON
   `recommended_evidence_quality_note`; set
   `pending_retest_after_substrate=true`; add `SD-032b` to `depends_on`
   (2026-05-24 483c autopsy flag, reaffirmed here).
5. claims.yaml Q-045 / MECH-313 / MECH-260: append shared
   evidence_quality_note per the autopsy JSON (cluster-absorb into 591
   family); verify `pending_retest_after_substrate=true` is already
   set from the 591 autopsy application and don't double-add.
6. substrate_queue.json: create new `SD-XXX-scaffolded-sd054-onboarding`
   entry verbatim from autopsy JSON
   `targets[V3-EXQ-603c].recommended_substrate_queue_entry`.
7. Rebuild claims.json + run `bash scripts/governance.sh` to reindex.

Governance application spawned as a third session chip 2026-05-29. Once
applied, the next `/inter-governance-brief` cycle will surface
`Implement substrate: SD-XXX (unblocks Q-045)` as a properly-gated IGW
item per the 2026-05-29 prereq-detection symmetric extension (REE_assembly
commit `d8d1aa2707`).

**GAP-4 status table impact:** GAP-4 stays `in-progress`. Closure
requires the Fork A library rebuild + V3-EXQ-490g actually running and
producing a contributory result on the rebuilt library, AND the Fork B
substrate-design + implementation + V3-EXQ-603d-equivalent run. The
breadcrumb here exists so any future goal-pipeline-touching session sees
the autopsy at Step 1 of the resume ritual.

**Cross-cluster cluster note:** the convergent shape "substrate is wired,
substrate IS firing, but the test harness can't see it" (Cluster A,
483c+524a) and "substrate is wired but does not fire because the training
regime never lets it develop" (Cluster B, 603c + 591 family) are
DIFFERENT failure modes. Cluster A is a test-design ceiling at the
experiment-script library layer; Cluster B is a substrate-enrichment
need at the goal-pipeline training-regime layer. The 591 autopsy's
"substrate enrichment vs test-design ceiling" two-readings framing was
correct in posture but underspecified -- both readings can be true
SIMULTANEOUSLY on the SAME substrate, with different downstream
experiment cohorts triggering different sides.

### 2026-05-20 - GAP-3 DONE: V3-EXQ-582a PASS + MECH-306 registered

**Closure.**

V3-EXQ-582a (`v3_exq_582a_gap3_drive_floor_sweep_20260519T014511Z_v3`) PASS on all
pre-registered criteria at `drive_floor=0.9`:

| Criterion | Result |
|-----------|--------|
| A1 mean effective benefit at contact > 0.08 | 0.115 |
| A2 >= 2/3 seeds with seeding fired | 3/3 |
| A3 z_goal active fraction > 0.05 | 0.081 |
| A4 OFF arm zero seedings | 0 (falsifier holds) |

**Option adjudication:** Option 1 (`drive_ema_alpha` sweep, V3-EXQ-582) FAIL -- drive
input near-zero throughout episodes; EMA cannot lift a flat input. Option 2
(`drive_floor`) is the validated sustained-drive path for goal seeding in the
EXQ-536a/582 anchor regime.

**Governance:**

- **MECH-306** `sustained_drive_trace` registered (`candidate_substrate_landed`,
  `v3_pending: true` until GAP-4 cascade retests).
- SD-012 `evidence_quality_note` extended with GAP-3 closure summary.
- Experiment classified non_contributory at manifest level (substrate-readiness
  diagnostic; `claim_ids=[]`); MECH-306 carries the mechanism registration.

**GAP-4 impact:** prerequisite `goal_pipeline:GAP-3` satisfied. Tier-1 MECH-295
cascade retest cohort (490g / 471a / 475a / 483c / 524a) is unblocked for
`/queue-experiment` with `drive_floor=0.9` (and SP-CEM defaults). V3-EXQ-588b
(infant persistent-agent floor diagnostic) remains queued independently.

**Status transitions:** GAP-3 `in-progress` -> `done`; GAP-4 `blocked` -> `in-progress`.

### 2026-05-17 - GAP-6 DONE: MECH-269b staleness-corrected V_s consumer migration closed

**GAP-6 closure.**

The MECH-269b-followup-A substrate (staleness-corrected V_s in `VsRolloutGate.gate()`) is
fully implemented end-to-end:

- `HippocampalConfig.use_vs_gate_staleness_lookup` flag (False default; also exposed via
  `REEConfig.use_vs_gate_staleness_lookup` and wired through `from_dims`)
- `VsRolloutGate.gate()` and `gate_stream()` accept `per_stream_staleness` dict; when
  `use_staleness_lookup=True`, compute `effective_vs = raw_vs - staleness[stream]` before
  threshold comparison
- `REEAgent` passes `self.hippocampal.compute_per_stream_staleness()` to `gate()` calls
  when the flag is on (agent.py lines ~2271 / ~2307 / ~3501)
- `HippocampalModule.compute_per_stream_staleness()` exists and draws from the
  `StalenessAccumulator` (MECH-284 Phase-3, implemented 2026-04-24)

**Experimental lineage (Q-040 factorial):**

| EXQ | Outcome | Finding |
|-----|---------|---------|
| V3-EXQ-490b | FAIL / superseded | C1 PASS (gate fires at override thresholds); C2+C3 FAIL (zero approach_commit, zero dACC score-bias -- MECH-295 dominant, not MECH-269b alone) |
| V3-EXQ-490c | FAIL / superseded | Added MECH-295 liking-bridge ON arm; still catatonic-lock |
| V3-EXQ-490e | FAIL / non_contributory | Strengthened bridge seeding; cue fires confirmed but approach_commit=0 |
| V3-EXQ-490f | FAIL / superseded | Further parametric sweep; monostrategy confound identified as primary block |

**Q-040 factorial verdict:** MECH-295 (liking-bridge) is the dominant cause of the EXQ-471
catatonic-lock, not MECH-269b alone. The staleness gate fires (C1), but behavioral
sufficiency (Q-040b) is blocked by the monostrategy confound, not by missing staleness
wiring.

**Monostrategy resolved:** ARC-065 SP-CEM landed as main-path default 2026-05-17
(WORKSPACE_STATE.md entry). The candidate-generation monostrategy that was confounding
all goal-pipeline behavioural tests (EXQ-471 / 490 / 514 / 536 lineage) is now removed at
the substrate level. This satisfies the "V_s monostrategy resolution" condition that GAP-6
was blocking on.

**Scope boundary:** Q-040b behavioral sufficiency of the staleness correction *alone*
remains a claims-level open question under MECH-269b. It continues under
`v_s_invalidation_runtime.md` (Phase 2 T2 forward-predictor path or the
combined-cluster combined-arm path). The goal_pipeline infrastructure dependency -- that
the monostrategy confound not interfere with Tier-3 behavioural tests -- is satisfied.

**Status transition:** GAP-6 open/tracked -> done.

### 2026-05-17T13:03Z - GAP-3 Option 2 escalation: drive_floor substrate + V3-EXQ-582a queued

V3-EXQ-582 FAILED (all 5 alphas incl. 0.01; diagnostic grid row "No arm clears A1"
-> escalate to Option 2). Root cause: drive_level near-zero throughout the episode
(agent well-fed); EMA cannot help when the EMA INPUT is consistently low. Additionally
POST_WARMUP_CUT=100 masked all contacts (every contact occurred before step 100 in
the 200-step episodes). Option 2 proceeds per the pre-registered diagnostic grid.

**Substrate landed** (ree-v3 466e7db):
- `GoalConfig.drive_floor: float = 0.0` (default, bit-identical OFF)
- `GoalState.update()`: `drive_level_floored = max(drive_level, drive_floor)` applied
  before the EMA -- guarantees trace >= drive_floor in steady state, giving
  `effective_benefit >= benefit * (1 + drive_weight * drive_floor)` at every contact.
- `config.py from_dims()` wired with `drive_floor` kwarg.
- Contract `test_drive_floor_gap3_opt2.py` 7/7 PASS; full suite 484/484 PASS.

**V3-EXQ-582a queued** (priority 1, any machine, supersedes V3-EXQ-582):
- Sweeps `drive_floor` in {0.0, 0.3, 0.6, 0.9, 1.2} x 3 seeds.
- `drive_ema_alpha=1.0` (Option 1 OFF; testing Option 2 in isolation).
- No POST_WARMUP_CUT: floor applies from step 0, no cold-start transient.
- First-PASS arm: floor=0.9 (predicted: effective_benefit ~ 0.03 * 2.8 = 0.084 at
  first contact; accumulates to > 0.1 by the 2nd-3rd contact within an episode).
- Dry-run confirms floor scaling: mean_eff_benefit_on_contact = 0.035 / 0.056 /
  0.077 / 0.098 / 0.119 across floors 0.0 -> 1.2.
- On PASS (A1-A4): GAP-3 done, register MECH-306 via governance.
- On FAIL: follow 582a diagnostic grid (see script docstring). If no floor clears A1
  (incl. 1.2), escalate to Option 3 (MECH-216 schema-driven wanting).

Note: prior session `resume_condition` recommended waiting for V3-EXQ-587/588
(infant substrate contact density gate). User explicitly chose to proceed with
Option 2 now per the EXQ-582 diagnostic grid. The 582a dry-run confirms contacts
DO occur without the warm-start gate (n_contacts > 0 in 40-step eval for 2/3
seeds). The warm-start prerequisite may have been overstated; 582a will resolve it.

**Status:** GAP-3 remains in-progress; owner_exq updated to V3-EXQ-582a.

---

### 2026-05-17 - GAP-3 Q2 RESOLVED + SD-012 sustained-drive EMA (Option 1) substrate landed; V3-EXQ-582 queued

User invoked goal-pipeline GAP-3. GAP-3 was `open`/unstarted (no EMA knob in
goal.py; the design memo's reserved EXQ-539-541 had been reused for MECH-204
work). Surfaced the registered open question **Q2** (the EMA timescale) plus a
plan-of-record inconsistency: the plan body/Q2 proposed knob `drive_ema_alpha`
default 0.05; the design memo used `alpha_drive_trace` operating value 0.02;
the lit synthesis `wanting_liking_sleep_consolidation_synthesis.md` endorses a
30-60 step half-life window and flags 0.05 (~14-step) as too fast.

**User decisions:** (Q2) canonical knob `drive_ema_alpha`, config default 1.0
(bit-identical OFF, non-negotiable), first-PASS arm **alpha=0.02** (lit-
anchored ~35-step half-life), discriminative sweep {0.01, 0.02, 0.2, 1.0};
(implementation sub-choice) **zero-init** the trace rather than first-obs init,
explicitly accepting the ~1/alpha-step per-episode cold-start transient as a
documented confound the validation EXQ accounts for.

**Landed (via /implement-substrate):** `GoalConfig.drive_ema_alpha` (goal.py,
default 1.0); `GoalState.update()` EMA recursion
`_drive_trace = (1-alpha)*_drive_trace + alpha*drive_level` then the SD-012
multiplier uses `_drive_trace`; `GoalState.reset()` zeroes `_drive_trace` (the
Q2 cold-start is per-episode -- caught during code review when tracing the
eval-loop reset() semantics, a substrate gap fixed before queuing);
`REEConfig.from_dims` passthrough mirroring `drive_weight`. Backward compat is
load-bearing and verified: alpha=1.0 -> trace==drive_level regardless of init
(contract C1/C2), full contract+preflight suite 426/426 green, an existing
drive-modulated goal experiment runs unchanged under default config. New
contract `tests/contracts/test_sustained_drive_ema_gap3.py` 7/7 (C1 default,
C2 bit-identical-to-instantaneous, C3 no contact-collapse, C4 ~35-step
half-life, C5 monotone falsifier curve = trace-at-contact post-warmup, C6
zero-init cold-start bound, C7 reset() re-zeroes). Docs reconciled: SD-012 doc
gained a "Sustained-drive amendment" section; the design memo's
`alpha_drive_trace` name marked superseded; ree-v3/CLAUDE.md SD section entry.

**Scope discipline:** `claims.yaml` deliberately NOT modified. Registering
**MECH-306 sustained_drive_trace** (mechanism_hypothesis; EXQ-536a empirical
anchor; lit anchors per the wanting/liking synthesis) is the governance
follow-on, gated on V3-EXQ-582 PASS -- consistent with the recent GAP-closure
convention ("GAP unblocks but does not itself promote").

**Validation:** V3-EXQ-582 (`v3_exq_582_gap3_sustained_drive_ema_sweep`,
diagnostic, claim_ids=[], priority 2) queued -- 4 alpha arms x 3 seeds on the
EXQ-536a goal-seeding regime, ungated per-step `update_z_goal` (substrate-
faithful time-EMA; diverges from 536a's benefit-gate by design), trace read
from `goal_state._drive_trace` post-update, metrics over an all + fixed
post-warmup (cut=100) window. PASS = A1 drive-trace@contact(0.02)>0.10
(vs 536a 0.005) & A2 >=2/3 seeds clear benefit_threshold & A3
z_goal_active_fraction>0.20 & A4 monotone alpha curve with the OFF arm at the
536a value. Script carries the mandatory diagnostic interpretation grid
(Option-2 escalation / regime-drift / downstream-bottleneck routings).

**Status:** GAP-3 open -> in-progress (NOT done -- the EXQ has not run; per
the never-mark-complete-before-artifact rule). On 582 PASS: GAP-3 -> done,
MECH-306 to governance, GAP-4's GAP-3 prerequisite satisfied (GAP-4 still
separately gated on the ARC-065 SP-CEM monostrategy fix). GAP-4
resume_condition updated to reflect Q2 resolved + EMA landed. ree-v3 and
REE_assembly committed.

### 2026-05-16 - Closure-map reconciliation: GAP-2 / GAP-4 monostrategy blocker has a validated substrate fix (ARC-065 SP-CEM)

Staleness pass (status tables 5-8 days behind runner, now V3-EXQ-581).

GAP-2 (SD-049 Phase 2 behavioural) and GAP-4 (MECH-295 cascade Tier-1
retest) have been `blocked` since 2026-05-08 on the z_goal /
monostrategy root cause. Reconciled evidence:
- V3-EXQ-550 FAIL (supports MECH-269): wired z_goal alone does NOT
  break monostrategy (entropy delta ~0 at no-training depth). Settles
  that the blocker is NOT missing z_goal wiring.
- V3-EXQ-551 / 551a / 570 PASS (diagnostic): bottleneck localised to
  E2-rollout / CEM-candidate collapse, not the goal pipeline.
- V3-EXQ-560 / 561 / 562 non_contributory: the diversity stack
  (ARC-065 / MECH-313/314/320 arms) does not break monostrategy under
  the OLD collapsed CEM.
- V3-EXQ-567 PASS (supports ARC-065): SP-CEM lifts natural action
  entropy 0.012 -> 0.497, candidate support 1.007 -> 2.810 -- the
  validated substrate fix for exactly this root cause.

GAP-2 / GAP-4 stay `blocked` (behavioural retest not yet run) but the
resume condition is now precise: gated on SP-CEM landing in the main
agent action path + retest re-issue via /queue-experiment, NOT on
further z_goal wiring (V3-EXQ-550 closed that question). last_updated
bumped on both nodes.

### 2026-05-11 - V3-EXQ-550 FAIL: MECH-269 V_s monostrategy substrate-level reading sustained at no-training depth; new "wired-but-inert z_goal" gap surfaced

V3-EXQ-550 ran 2026-05-11T19:01Z (DLAPTOP-4.local) and registered FAIL on the
pre-registered pass rule `action_class_entropy(ON) - action_class_entropy(OFF)
>= 0.10 in >= 2/3 seeds`. All 3 seeds returned `action_class_entropy = 0.0` in
BOTH arms and per-seed action distributions bit-identical between ARM_OFF and
ARM_ON (seed 42 class "1" 1200/1200 both arms; seed 7 class "2" 1200/1200 both
arms; seed 17 class "2" 1200/1200 both arms). Per the pre-registered
interpretation grid in the manifest's `evidence_direction_note`:
**FAIL supports the substrate-level reading of MECH-269 V_s monostrategy at
no-training depth.** Does NOT rule out that a trained z_goal pipeline would
change the picture; the test was a no-training random-init probe by design.
MECH-269's hold on SD-029 stands at this depth.

**Additional finding NOT in the pre-registered grid (separate substrate gap):**
the diagnostic incidentally surfaced a wired-but-inert pattern in the z_goal
activation path. ARM_ON recorded `z_goal_update_calls = 1200` (every tick of
every seed; the per-step `update_z_goal(info['benefit_exposure'])` plumbed in
the experiment script fired correctly) but `z_goal_norm_peak = 0.0` on every
seed. The goal pipeline is wired and called but functionally inert: GoalState
mutates without ever producing a non-zero `z_goal` norm under this probe's
benefit-exposure feed. Mechanism is unconfirmed (candidates: GoalState
internal threshold gating, benefit_exposure scale mismatch, drive-weight
multiplier zeroing through, missing seeding step). This is distinct from the
action-class-collapse signature MECH-269 captures -- the agent's downstream
selection is still single-action-deterministic, but EVEN IF V_s monostrategy
were broken upstream, the goal pipeline at this no-training depth would not
seed a non-zero z_goal to bias action selection. This is a recurrence of the
wired-but-inert pattern named in the One-line framing section (and previously
seen on EXQ-471 / EXQ-483 / EXQ-490 / EXQ-514 / EXQ-536 / EXQ-538).

**Recommended next moves:**

1. **Trained-z_goal follow-up** (the natural successor to V3-EXQ-550). Same
   ARM_OFF / ARM_ON structure but with P0 + P1 training prior to the action-
   class entropy measurement, so the z_goal pipeline has had a chance to
   accumulate state and the goal-modulated policy has gradient pressure.
   PASS at training depth = z_goal pipeline biases action selection materially
   once trained -> weakens MECH-269 substrate-level reading. FAIL at training
   depth = substrate-level reading survives the strongest available probe
   short of architectural redesign. Deferred to a separate `/queue-experiment`
   session; not authored here.

2. **Diagnostic-first ordering** (concurrent sessions, parallel to this one):
   - **V3-EXQ-551 pipeline-entropy diagnostic** -- characterise what the
     `update_z_goal` -> GoalState -> z_goal-bias-into-action_selection chain
     actually does at no-training-depth: log z_goal norm trajectory, GoalState
     drive trajectory, per-step contribution to action logits, identify where
     in the chain the signal collapses to zero. Owned by a parallel session
     in `ree-v3/`.
   - **V3-EXQ-552 forced-exploration warmup** -- inject epsilon-greedy
     exploration during a warmup phase to escape the random-init action-class
     collapse, then re-measure z_goal ON/OFF entropy delta. Test whether the
     no-training monostrategy is the bottleneck for the z_goal diagnostic
     (orthogonal to whether trained z_goal helps). Owned by a parallel
     session in `ree-v3/`.

   These two diagnostics are queued by parallel sessions concurrent with
   this review (no resource overlap with REE_assembly/ planning docs); their
   outputs route back into this plan via separate decision-log entries.

**Status table impact:** This plan does NOT carry a GAP explicitly named
"z_goal wired-but-inert at no-training depth" -- the pattern was implicit in
GAP-2 / GAP-3 / GAP-4 prerequisites. EXQ-550's incidental finding tightens
the substrate description: any Phase 2/3/4 EXQ that does NOT actively warm
up the goal pipeline (e.g. through training or forced exploration) will
inherit the inert-z_goal signature regardless of substrate quality. Recorded
here rather than as a new GAP row because (a) the candidates EXQ-551 / EXQ-552
will narrow what the actual mechanism is, and (b) the fix path (trained
follow-up + diagnostic-driven mechanism identification) is already covered
by Phase 2 + Phase 3 + Phase 4 cohort triggers. If EXQ-551 / EXQ-552 surface
a distinct architectural gap (e.g. a missing GoalState seeding hook), a new
GAP row will be added in the resolving session.

**Substrate-readiness implications for in-flight work:**
- MECH-269 V_s monostrategy hold on SD-029 is sustained at no-training depth.
  Previous reclassifications of EXQ-433* / EXQ-470 / EXQ-476* / EXQ-537 as
  non_contributory under V_s monostrategy remain correct.
- Other plans' interpretations of "wired but inert" recur (most recently in
  the 2026-05-11 self_attribution_plan GAP-1 inversion: floating-point-
  identical metrics between ARM_INDEPENDENT and ARM_SHARED under
  action_class_entropy=0.0) read the SAME substrate-ceiling signal from a
  different observable.

**Files touched in this session:** `goal_pipeline_plan.md` (this decision-log
entry; status-table GAP-1 row "Next action" notes EXQ-550 finding); review
tracker; WORKSPACE_STATE.md. No claims.yaml edits; no MECH-269 status
change (already candidate / v3_pending under MECH-269b followup). No
`evidence_direction_per_claim` overrides needed -- the manifest's flat
`MECH-269: supports` correctly carries the substrate-level reading. No
script written; concurrent sessions B + C own the diagnostic queue-ups
(V3-EXQ-551 + V3-EXQ-552).

### 2026-05-11 - GAP-1 substrate landed (Option-b for Gap 1 per user override)

Phase 1 substrate (MECH-307 four-gap conjunction architecture) landed end-to-end
in ree-v3. Gap 1 implemented as Option-b (split into VALENCE_POSITIVE_SURPRISE +
VALENCE_NEGATIVE_SURPRISE as separate channels in the residue valence buffer)
per user override 2026-05-11 of the design-doc default Option-a (signed single
channel). Gaps 2, 3, 4 substrate-landed 2026-05-08 unchanged (no rewrite this
session). New REEConfig field `use_mech307_conjunction` is a master convenience
flag whose `__post_init__` resolver propagates to the three substrate-side
sub-flags (`use_mech307_split_surprise`, `use_mech307_schema_multichannel`,
`use_mech307_predicted_location_write`). Path B / consumer-side
`use_mech307_consumer_conjunction_read` NOT auto-set (out of session scope per
"substrate only first" directive).

Modules touched:
- ree-v3/ree_core/residue/field.py (VALENCE_DIM 4 -> 6; new constants
  VALENCE_POSITIVE_SURPRISE=4 and VALENCE_NEGATIVE_SURPRISE=5;
  evaluate_valence return shape [batch, 6]).
- ree-v3/ree_core/utils/config.py (two new REEConfig fields +
  `__post_init__` resolver).
- ree-v3/ree_core/agent.py (MECH-205 PE write site dispatches three paths:
  split / signed / true-legacy; new VALENCE_POSITIVE_SURPRISE /
  VALENCE_NEGATIVE_SURPRISE imports).
- ree-v3/CLAUDE.md ("MECH-307 Anticipatory Affect Conjunction Architecture
  (2026-05-11)" SD-Implemented entry appended).
- REE_assembly/docs/claims/claims.yaml (MECH-307 status candidate ->
  candidate_substrate_landed; evidence_quality_note extended with 2026-05-11
  implementation_note paragraph; v3_pending remains True pending behavioural
  validation).
- REE_assembly/docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md
  (Status block flipped PENDING -> SUBSTRATE LANDED 2026-05-11; Option-b
  paragraph added).

Regression: 309/309 contracts + 7/7 preflight PASS with master OFF
(bit-identical OFF guarantee). The existing
tests/contracts/test_mech307_conjunction_contract.py (12 contracts covering
Gaps 1-4 under their individual flags) PASSed unmodified -- the Option-a
Gap-1 path is preserved behind `use_mech307_signed_pe`.

Direct field-level smoke (2026-05-11):
- VALENCE_DIM=6 buffer allocation verified.
- Split-channel write routing verified: harm_signal < 0 -> NEGATIVE channel;
  harm_signal >= 0 -> POSITIVE channel; magnitude preserved on legacy
  VALENCE_SURPRISE for backward-compat consumers.
- MECH-094 hypothesis_tag=True gate respected (write skipped).

GAP-2 (SD-049 Phase 2 V3-EXQ-514 behavioural validation under MECH-307-fixed
substrate) now unblocked. Phase 2 trigger condition (Phase 1 PASS on the 4-arm
discriminative validation) is the next gate; the 4-arm validation EXQ is the
canonical Phase 1 PASS / fallback adjudicator between MECH-307 conjunction
architecture (first-line) and the SD-014 6-channel amendment (registered
fallback).

Reason for Option-b override: user-directed; rationale not recorded by the
user beyond preference for the architecturally cleaner channel-separation
form. The Option-a path is preserved behind `use_mech307_signed_pe`, so
the 4-arm validation can include an Option-a arm if discriminative testing
between Option-a and Option-b becomes load-bearing for governance.

### 2026-05-08 - Plan registered

Audit conducted in conversation with user as a follow-on to the
2026-05-08 governance-cycle-friday-pm and register-mech307-and-sd014-amendment
sessions. User flagged the goal pipeline as a load-bearing umbrella loop
parallel to sleep_substrate_plan.md, with MECH-307 conjunction architecture
already at substrate_queue priority=1. Six gaps surfaced and sequenced into
six phases. User acknowledged Phase 1 (MECH-307) as the gate for the rest;
GAP-5 / Phase 5 deferred as cleanup-of-substrate-coverage refactor not on
acceptance-criterion path. Plan-doc + status-table + decision-log pattern
adopted, mirroring sleep_substrate_plan.md / sd033_governance_plan.md
precedent.

### 2026-05-08 - Boundary with sleep_substrate_plan.md established

SD-049 sleep-on cohort (V3-EXQ-514 family with use_sleep_loop=True) sits at the
boundary of both plans. Decision: goal_pipeline_plan.md owns the SD-049
substrate + behavioural acceptance criteria; sleep_substrate_plan.md owns the
sleep-loop side of validation. Both plans' "See also" sections cross-reference
each other; either plan may sequence a V3-EXQ-514 successor with its flag stack.
Reason: avoid plan-doc drift where two plans claim ownership of the same EXQ
without explicit boundary.

### 2026-05-08 - MECH-307 vs SD-014 6-channel amendment

MECH-307 four-gap conjunction architecture is the first-line proposal (~40 lines
of code per the 2026-05-08 design doc); SD-014 6-channel amendment (add
VALENCE_EXCITEMENT + VALENCE_DREAD as discrete channels) is the architectural
fallback if MECH-307 conjunction does not produce the expected derived states.
Decision: land MECH-307 first; only escalate to SD-014 6-channel amendment on
Phase 1 falsification (all-four-gaps-fixed arm fails to produce non-zero
cue_fires + dacc_bias + approach_commit relative to baseline). Reason:
biology does not have a "VALENCE_EXCITEMENT neuron type"; the excitement
signal measured in NAcc fMRI is the anatomical convergence of DA RPE +
hippocampal preplay + ANS arousal at one structure -- the conjunction reading is
more biologically faithful than adding a new channel.

### 2026-05-08 - SD-012 sustained-drive amendment scoped as Phase 3, not Phase 1

The sustained-drive amendment (drive_level collapse at contact, per
sustained_drive_anticipatory_wanting.md) overlaps with MECH-307 Gap 4
(MECH-216 writes at current rather than predicted z_world). Both touch SD-012 /
MECH-216. Decision: keep them as separate phases (Phase 1 = affect-write site
fix; Phase 3 = drive-multiplier site fix). Reason: independently small and
independently falsifiable; sequencing serially keeps each PASS interpretable.
EXQ-536b force-arm probe documents both confounds simultaneously; separating
them lets the Phase 1 retest disambiguate.

### 2026-05-08 - Phase 5 deferred as refactor not on acceptance-criterion path

SD-049 Phase 3 SD-032 consumer cascade (GAP-5) is a cleanup-of-substrate-coverage
refactor: migrating AIC, PCC, pACC, dACC, salience-coordinator,
override-regulator, MECH-295 liking-bridge from reading collapsed scalar to
per_axis_drive vector. None of the goal-pipeline acceptance criteria require
Phase 5 to land; Phases 1-4 are sufficient. Decision: defer Phase 5 to "Phase
4 Tier-3 outcome" trigger -- only land if Phase 4 reveals a remaining
drive-cascade fidelity gap. Reason: smallest-step principle; Phase 5 has no
load-bearing dependent claim.

> **SUPERSEDED 2026-06-15 -- see next entry.** This deferral trigger never
> fired (GAP-4 closed 2026-06-09 by re-scope/falsification, not a Tier-3
> fidelity-gap). The cascade was instead pulled forward as substrate plumbing
> for the GAP-2 behavioural line and is now closed done.

### 2026-06-15 - Phase 5 / GAP-5 closed superseded-by-implementation

The SD-049 Phase 3 SD-032 consumer cascade was BUILT + LANDED (ree-v3 main
2026-05-31T13:00Z, "SD-049 Phase 3 SD-032 consumer cascade") independent of the
2026-05-08 "Phase 4 Tier-3 fidelity-gap" deferral trigger above, which never
fired. All seven named consumers now carry the optional `per_axis_drive` kwarg
(`ree_core/cingulate/{aic_analog,pcc_analog,pacc_analog,dacc,salience_coordinator}.py`,
`ree_core/regulators/{broadcast_override,mech295_liking_bridge}.py`), preserving
bit-identical OFF when `per_axis_drive` is None; `causal_grid_world` surfaces
`obs_dict['per_axis_drive']` under `per_axis_drive_enabled`. Readiness validated
by V3-EXQ-618 (2026-05-31T17:59Z, `experiment_purpose=diagnostic`, all 4
acceptance criteria PASS; tagged `evidence_direction=non_contributory` because a
substrate-readiness diagnostic does not behaviourally test SD-049/MECH-295 --
correct, and not a blocker for a refactor with `unblocks_claims:[]`). The
cascade got pulled forward as substrate plumbing for the GAP-2 behavioural line
(514g -> 618 -> 619), NOT for GAP-5's own (never-demonstrated) "fidelity refactor
for its own sake" justification. The remaining *behavioural* validation
(V3-EXQ-619, reserved/not-queued) is owned by goal_pipeline:GAP-2, not this
node. Status -> done; owner_exq -> V3-EXQ-618; no claims.yaml/scoring edit
(refactor, no dependent claim). Discovered during a user-requested read of the
GAP-5 node, which exposed ~6 weeks of frontmatter drift (node still said
`deferred / owner_exq:null / last_updated 2026-05-08` while the work had landed).

---

## Open questions

Numbered for reference from future sessions.

- **Q1**: For Phase 1 Gap 1, prefer signed VALENCE_SURPRISE (single channel,
  preserves backward compat under `abs()`) or split into VALENCE_POSITIVE_SURPRISE
  + VALENCE_NEGATIVE_SURPRISE (cleaner separation, more disruptive). Default
  proposed: signed single channel behind `surprise_signed` config flag. Open:
  whether any downstream consumer needs the channel-level separation rather
  than reading sign-magnitude.
- **Q2**: ~~For Phase 3 Option 1 (sustained-drive EMA), what is the right
  `drive_ema_alpha` default?~~ **RESOLVED 2026-05-17 (user decision).**
  Config *default* = **1.0** (non-negotiable: alpha=1.0 -> trace == drive_level
  every step regardless of init -> bit-identical OFF / backward-compat).
  Canonical knob name = **`drive_ema_alpha`** (the design memo's
  `alpha_drive_trace` is superseded; identical semantics). First-PASS /
  acceptance operating arm = **alpha=0.02** (~35-step half-life), chosen over
  the originally-proposed 0.05 (~14-step) because the lit synthesis
  `wanting_liking_sleep_consolidation_synthesis.md` endorses a 30-60 step
  post-consummatory wanting window and explicitly flags 0.05 as risking the
  documented "trace too fast -> resembles OFF" failure mode. Discriminative
  sweep = **{0.01, 0.02, 0.2, 1.0}** (0.02 first-PASS, 0.01 slow bracket, 0.2
  fast-end falsifier, 1.0 OFF parity). Trace is **zero-initialised**
  (user-chosen over first-obs init): for alpha<1.0 this carries a deliberate
  ~1/alpha-step per-episode cold-start transient -- an accepted, documented
  confound that V3-EXQ-582 accounts for by reporting metrics over a fixed
  post-warmup window. Landed: GoalConfig.drive_ema_alpha; GoalState.update
  EMA recursion; GoalState.reset() zeroes the trace (per-episode cold-start);
  REEConfig.from_dims passthrough; contract test_sustained_drive_ema_gap3.py
  (7/7). Validation: V3-EXQ-582 (queued).
- **Q3**: For Phase 4 Tier-1 cohort, should V3-EXQ-471a / V3-EXQ-475a / V3-EXQ-483c /
  V3-EXQ-490g / V3-EXQ-524a all run together as a Tier-1 batch, or sequentially?
  Default proposed: batch, since they share substrate (MECH-307 + SD-012
  amendment + StepHarness) and discriminate on different downstream pathways.
- **Q4**: For Phase 2 row-6 falsifier branch, MECH-229 routing to
  substrate_conditional with V4-1 multi-agent ecology dependency requires
  V4 substrate work. Open: should goal_pipeline_plan track the V4-1
  escalation path, or is that V4 spec territory? Default proposed: track here
  with a `tracked` row pointing at v4_spec.md, escalate ownership only on
  row-6 hit.
- **Q5**: For Phase 5 (deferred), the Phase 5 trigger is "Phase 4 Tier-3
  outcome reveals a remaining drive-cascade fidelity gap." Open: what is the
  precise diagnostic that would identify the cascade as the residual issue
  rather than (e.g.) E3 / BG selection thresholds? Default proposed: per-axis
  drive ANOVA on z_goal cluster IDs producing p > 0.05 in Phase 4 Tier-3
  ARM_2 (the SD-049 acceptance criterion fails specifically on the per-axis
  drive read-site path).

---

## Resume ritual

When picking up goal-pipeline work after a deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that was
   `paused`, `in-progress`, or `blocked` whose blocker has cleared.
3. If `paused`, find its entry in the [Decision log](#decision-log) and
   confirm the resume condition has fired.
4. If `blocked` and the blocking phase has PASSed, transition to `in-progress`
   and continue from the most recent decision-log entry for that phase.
5. If `in-progress`, find the most recent decision-log entry for that phase
   and continue from the last concrete action.
6. Update the row's `Last updated` field and `Status` if it changes.
7. Append a new decision-log entry for any architectural choice made during
   the resumed session.

Sessions that do NOT touch goal-pipeline work do not need to read this
document. Sessions that DO touch goal-pipeline work read this document before
any code or experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite entries
die with the session; WORKSPACE_STATE.md is recent-work, not strategic;
substrate_queue.json is granular but does not capture phase ordering or
decision rationale. This document is the single source of truth for
goal-pipeline strategy.

---

## See also

- [docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md](../../docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md)
- [docs/architecture/sustained_drive_anticipatory_wanting.md](../../docs/architecture/sustained_drive_anticipatory_wanting.md)
- [docs/architecture/goal_wanting_signal_chain.md](../../docs/architecture/goal_wanting_signal_chain.md)
- [docs/architecture/mech_295_drive_liking_approach_bridge.md](../../docs/architecture/mech_295_drive_liking_approach_bridge.md)
- [docs/architecture/sd_049_multi_resource_heterogeneity.md](../../docs/architecture/sd_049_multi_resource_heterogeneity.md)
- [docs/architecture/sd_015_z_resource_encoder.md](../../docs/architecture/sd_015_z_resource_encoder.md)
- [docs/architecture/approach_avoidance_symmetry.md](../../docs/architecture/approach_avoidance_symmetry.md) (ARC-030, MECH-117, MECH-229, MECH-230 location)
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) -- adjacent plan; SD-049 sleep-on cohort sits at the boundary (see [Boundary with sleep_substrate_plan.md](#boundary-with-sleep_substrate_planmd))
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) plan-doc precedent
- [evidence/planning/substrate_queue.json](./substrate_queue.json) -- MECH-307 / MECH-295 / SD-049-* / MECH-269b-followup-A entries
