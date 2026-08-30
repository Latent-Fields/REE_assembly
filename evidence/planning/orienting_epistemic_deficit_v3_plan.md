---
closure_plan:
  id: orienting_epistemic_deficit_v3
  title: "Orienting & Epistemic-Deficit Cluster (V3 closure)"
  registered: 2026-08-13
  last_updated: 2026-08-30
  scope_claims: [MECH-395, MECH-482, MECH-483, Q-089, MECH-489, SD-099]
  sibling_plans: [drives_motivation_v4, goal_pipeline]
  registered_note: >
    NEW plan doc (session curiosity-orienting-closure-gap-27d495, 2026-08-13,
    chip-20260813-curiosity-orienting-closure-map-gap). Closes a closure-map
    ownership gap surfaced by /governance 2026-08-12 (session
    sd-016-h3-algorithm-3370cd; WORKSPACE_STATE.md 21:32:43Z entry):
    MECH-482 (epistemic_deficit accumulator), MECH-483 (orient/survey third
    primitive regime), and Q-089 had NO owning closure node anywhere in any
    *_plan.md (prose-only mentions in drives_motivation_v4_plan.md's
    frontmatter/decision-log). MECH-489 and SD-099 (defensive-orienting
    phasic chain) were absent from every *_plan.md entirely, despite SD-099
    already being IMPLEMENTED (ree_core/pag/defensive_orienting.py,
    2026-08-09) and MECH-489 already carrying real experimental evidence
    (V3-EXQ-910/910a) -- both 0%-credited in V3 closure purely because
    nothing owned them. MECH-395 (narrow, cue-triggered orienting) WAS
    owned, by drives_motivation_v4:DRV-4, but that plan is generation:v4
    (excluded from V3 closure tracking) even though MECH-395's own
    claims.yaml implementation_phase was reclassified v4->v3 on 2026-08-07
    (session elegant-ishizaka-ddd4f6) -- a live plan/claims
    self-inconsistency. Confirmed by reading serve.py,
    generate_closure_snapshot.py and check_closure_drift.py: none of the
    three closure-tracking consumers support a node-level `generation`
    override, only plan-level, so flipping drives_motivation_v4_plan.md's
    whole `generation` to v3 was rejected as the fix -- it would have
    incorrectly pulled DRV-1 (drive register)/DRV-2 (arbitration)/DRV-3
    (arbitration grounding)/DRV-5 (failure-grade taxonomy) into V3 closure
    tracking, which the plan's own text and the user both confirm are
    genuinely V4 work with no live V3 thread. User-directed disposition
    (AskUserQuestion, 2026-08-13): move MECH-395/DRV-4 alone out of
    drives_motivation_v4_plan.md into this new v3 plan; register
    MECH-482/483/Q-089/MECH-489/SD-099 here too as one unified plan -- the
    six form one connected family (MECH-489.depends_on in claims.yaml names
    all the others). DRV-1/2/3/5 stay in drives_motivation_v4_plan.md as
    genuinely-v4 roadmap, per explicit user direction ("the other drives I
    am not sure about"). No claims.yaml edits made by this registration --
    every claim's `status`/`implementation_phase` field is unchanged; this
    is closure-map registration only, not a promotion/demotion, and does
    not itself authorize building MECH-482/483/Q-089 in V3 (both still say
    DO NOT build yet in their own claims.yaml registration notes).
  nodes:
    - id: "orienting_epistemic_deficit_v3:ORNT-1"
      title: "Pre-approach orienting/surveying mode (cue-triggered, narrow vector resolution)"
      phase: 1
      status: blocked
      blocker_class: v3_assembly_sequence
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-395"]
      depends_on: []
      cross_plan_link: ["drives_motivation_v4:DRV-1"]
      last_updated: 2026-08-13
      completion_note: >
        MOVED from drives_motivation_v4:DRV-4 (2026-08-13, this plan's
        registration) -- content and blocker are unchanged from DRV-4,
        only its closure-map home changed (DRV-4 lived in a generation:v4
        plan, excluding MECH-395 from V3 closure tracking despite
        claims.yaml already reading implementation_phase: v3 since
        2026-08-07). Gate is the shared E3 selection-authority /
        cue-authority ceiling: V3-EXQ-638a + V3-EXQ-640 + V3-EXQ-640a
        (post-cue action/gradient instrumentation + gain sweep) routed to
        this ceiling, not to orienting; V3-EXQ-812 (2026-07-24, MECH-295
        cue-authority direct test) FAILED on the candidate_proximity_evaluable
        readiness precondition (measured 0.0), same candidate-pool-collapse
        confound as the GAP-A cluster. Resume the orienting diagnostic
        (snail-race method: orient_mode_entries_after_cue, survey_steps,
        heading_entropy, gradient_information_gain) once a cue reliably
        reaches action selection. See failure_autopsy_V3-EXQ-640_2026-06-05.md
        and failure_autopsy_V3-EXQ-640a_2026-06-06.md for the diagnostic
        history; drives_motivation_v4_plan.md's decision log retains the
        full narrative up to the move.
    - id: "orienting_epistemic_deficit_v3:ORNT-2"
      title: "epistemic_deficit: persistent target-bound model-inadequacy accumulator"
      phase: 1
      status: in_progress
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-482"]
      depends_on: []
      cross_plan_link: []
      blocking_on: >
        MECH-482's own claims.yaml non-degeneracy precondition -- a substrate
        where target-bound uncertainty is tracked PER-CANDIDATE rather than as
        a global scalar -- is still UNMET, and the reason now sits one step
        further down than "GAP-A unclaimed". Verified against live ree-v3
        2026-08-22: the ARC-065 GAP-A per-candidate SLOT is present
        (agent.py `_candidate_epistemic_values`, config fields
        `curiosity_uncertainty_source` / `curiosity_learning_progress_source`,
        landed 2026-08-08 c0e0ce8), but BOTH sources default to "broadcast"
        (bit-identical off) and neither has a genuine signal behind it.
        314b's genuine source, the SD-063 E2WorldUncertaintyHead, IS
        instantiated on the agent (config-gated `use_e2_world_uncertainty`,
        agent.py 573-586) but is UNTRAINED; the phased P0->P1->P2 training
        loop that would make it live is follow-on item 1 of
        mech314bc_percandidate_extension_staged_2026-08-08.md and has never
        been chipped (scan of all 1435 TASK_CHIPS.json entries on 2026-08-22:
        zero chips naming SD-063 / e2_predictive_variance / head training
        since the 2026-08-08 slot landing). 314c's genuine source IS this
        node -- config.py:4030-4037 reserves the enum value
        "epistemic_deficit" and falls back to broadcast, so the substrate
        names the hole without filling it. That keystone is ALSO unowned in
        the closure map: no *_plan.md mentions SD-063 /
        E2WorldUncertaintyHead / e2_predictive_variance anywhere, and
        behavioral_diversity_isolation:GAP-A is `done` and scoped to a
        different concern (CEM elite-pool collapse, Theory 1 / Layer A).
        ARC-065 in substrate_queue.json remains ready:false, and that
        queue's own 2026-08-21 next_implement_substrate reconcile concluded
        no implement-substrate build is ready fleet-wide. The design doc
        itself is still status AWAITING USER REVIEW, unchanged since
        2026-08-08.
      reconcile_2026_08_27: >
        GATES-CLEARED CORRECTION (session f-dominance-regime-retest-ddbe10,
        debt-classification sweep; plan-frontmatter only, NO status change,
        nothing queued). The resume_condition below lags this plan's own
        status table: both 2026-08-22 gates CLEARED (design doc reviewed;
        SD-063 E2WorldUncertaintyHead training loop landed ree-v3
        88287f11c6), and the readiness criterion as written was FALSIFIED --
        use `_last_pvar_relative_spread`, not `last_uncertainty_dev_range`
        (see the status-table row for ORNT-2, updated 2026-08-23). Residual
        before the accumulator build: the 2x2 diversity validation
        (chip-20260823-mech314bc-2x2-diversity-validation, resolved done ->
        experiment queued; V3-EXQ-949 mech314b authority-rescale validation
        RAN PASS/supports 2026-08-25). The accumulator build itself is
        complicated (buildable) and is chipped as
        chip-20260827-mech482-accumulator-build with a STOP-CHECK on the
        validation state. Classification record:
        evidence/planning/work_graph_debt_classification_20260827.md.
      resume_condition: >
        Two-step gate; neither step is owned today. (1) The design doc
        mech314bc_percandidate_extension_staged_2026-08-08.md receives its
        owed user review, releasing its follow-on routing. (2) The SD-063
        E2WorldUncertaintyHead training loop lands and a run demonstrates
        readiness -- `last_uncertainty_dev_range > 0` under
        `curiosity_uncertainty_source=e2_predictive_variance` -- establishing
        that per-candidate target-bound uncertainty is genuinely
        discriminative rather than the near-uniform vector an untrained head
        returns (the MECH-353 / V3-EXQ-642 vacuous-comparison lesson, which
        agent.py's readiness gate exists to refuse). Only once (2) holds is
        MECH-482's non-degeneracy precondition met and the accumulator build
        legitimately startable; flip to in_progress at that point. Until
        then status stays `open`, and the correct next action is clearing
        gate (1) -- a governance/user decision, NOT a build.
      last_updated: 2026-08-30
      governance_2026_08_30: >
        STATUS FLIP OPEN -> IN_PROGRESS (governance cycle 2026-08-30 PM, session
        governance-20260830-1549) -- the flip this node's own status-table row had been
        explicitly holding for /governance. The MECH-482 EpistemicDeficitAccumulator LANDED
        2026-08-29 (ree-v3 b69a1b8, SD-102, chip-20260827-mech482-accumulator-build): wired in
        agent.py behind curiosity_learning_progress_source == "epistemic_deficit" (default
        broadcast, bit-identical OFF), readiness-gated on the CORRECTED
        e2_world_uncertainty_last_pvar_relative_spread > 0 with mark_vacuous_readout(); 18/18
        MECH-482 contracts green on the hub. Both 2026-08-22 gates in resume_condition below are
        therefore DISCHARGED and that text is superseded by reconcile_2026_08_27 plus this entry
        -- read those two, not the resume_condition, for current state.
        VALIDATION STATE: V3-EXQ-964 ran FAIL / non_contributory (C2 structurally unsatisfiable --
        n_targets never exceeds 1, so the readout is a constant vector); confirmed
        failure_autopsy_V3-EXQ-964_2026-08-30, governance-ratified 28d14475a5. So the BUILD is done
        and the VALIDATION is not: the node is in_progress, not done. What is owed is the
        multi-target readiness follow-on, substrate_queue entry
        sd_epistemic_deficit_multitarget_readiness (p2, degrading, created by that same cycle) --
        which as of this cycle has NO chip and NO IGW ledger entry, i.e. is currently UNOWNED.
        Chipped by this cycle. MECH-482 stays substrate_conditional / candidate; no claims.yaml
        change from this reconcile.
      completion_note: >
        Registered in claims.yaml 2026-08-05 (thought-digestion, "Epistemic
        Deficit and Orienting" intake), no owning closure node until this
        plan. DO NOT build in V3 yet per its own claims.yaml registration
        note. UPDATED 2026-08-13 (this session, found while checking for
        follow-on work): the GAP-A architectural SLOT (extend MECH-314b/314c
        to per-candidate treatment) already LANDED 2026-08-08 (ree-v3
        c0e0ce8, bit-identical off) -- but that slot is capability
        infrastructure, not MECH-482's actual source. Its own design doc
        (evidence/planning/mech314bc_percandidate_extension_staged_2026-08-08.md)
        explicitly routes MECH-482's genuine per-candidate accumulator as
        follow-on, still unbuilt, status AWAITING USER REVIEW as of
        2026-08-08 (not yet actioned by any chip as of this note). status:
        open correctly reflects that the accumulator itself has not been
        claimed/started; flip to in_progress once the design doc is
        reviewed and a build begins.
        2026-08-22 reconcile (IGW-20260822-154, session pending-task-009a3a):
        node re-verified against live ree-v3 substrate, claims.yaml,
        substrate_queue.json and the chip ledger. status STAYS open -- and is
        correct. The accumulator is confirmed unbuilt: the only occurrences
        of `epistemic_deficit` anywhere in ree_core are the reserved config
        enum value (utils/config.py:4030-4037, "not yet built in V3;
        currently falls back to broadcast") plus comments at agent.py:7587
        and policy/structured_curiosity.py:421,537 naming MECH-482 as the
        missing per-candidate learning-progress source. What this pass
        changes is not the status but the BLOCKER'S PRECISION: the
        2026-08-13 note rightly said the GAP-A slot is capability
        infrastructure rather than MECH-482's source, but left the actual
        gate unnamed, and the summary table below still read "GAP-A
        (substrate_queue.json) unclaimed" -- stale in both halves, since the
        slot LANDED on 2026-08-08 and ARC-065 is not merely unclaimed but
        ready:false. The real gate is now recorded explicitly in the new
        `blocking_on` / `resume_condition` fields (same shape ORNT-6 gained
        on 2026-08-21). Nothing in the 9 days since 2026-08-13 advanced this
        node: no chip, no claim and no substrate change touches MECH-482. No
        claims.yaml edits were made, consistent with this plan's
        registration posture.

        2026-08-22 UPDATE, same day, after the design-doc review (chip
        chip-20260822-sd063-head-training-keystone / -curiosity-budget-split-
        eligibility): GATE (1) OF resume_condition IS NOW CLEARED. The user
        reviewed mech314bc_percandidate_extension_staged_2026-08-08.md (which
        had been AWAITING USER REVIEW for 14 days -- this node's reconcile is
        what surfaced it) and the outcome is SPLIT. Follow-on item 1, the
        SD-063 E2WorldUncertaintyHead training loop -- gate (2), the keystone
        -- was AUTHORISED and is chipped as
        chip-20260822-sd063-head-training-keystone, so this node's blocker now
        has a named owner for the first time. Section 4's budget-split
        resolution was NOT ratified (user: constitutional / basal-ganglia
        eligibility may answer it better than a single test; anchors ARC-008
        and MECH-062, both partly-unbuilt) and is routed to
        chip-20260822-curiosity-budget-split-eligibility as a DESIGN PASS. That
        second thread does NOT gate this node: training the head and measuring
        last_uncertainty_dev_range is independent of how the shared curiosity
        budget is eventually allocated. status stays `open` -- the accumulator
        itself is still unbuilt and gate (2) has only just been chipped, not
        landed. Flip to in_progress when that build starts; if the trained head
        turns out NOT to satisfy the readiness gate
        (last_uncertainty_dev_range ~ 0), that is a real finding that re-routes
        this node rather than advancing it.

        2026-08-23 UPDATE -- GATE (2) LANDED, AND THE GATE CRITERION ITSELF WAS
        FALSIFIED. chip-20260822-sd063-head-training-keystone is DONE: the
        phased P0->P1->P2 online training loop for the SD-063
        E2WorldUncertaintyHead landed (ree-v3 88287f11c6, evidence REE_assembly
        15a87417bb), default OFF and bit-identical off, 18 new contracts, gate
        green at 4145 passed. It TRAINS (pinball 0.189 -> 0.069 on a synthetic
        heteroscedastic world, predictive_variance strictly monotone in true
        per-action noise scale; 216 P1 updates per real CausalGridWorldV2
        rollout across 3 seeds). So both gates named on 2026-08-22 are now
        cleared. TWO findings supersede this node's stated readiness criterion:

        (a) THE READINESS CRITERION DOES NOT DISCRIMINATE. resume_condition
        above names `last_uncertainty_dev_range > 0` as the signal that
        per-candidate uncertainty is genuinely discriminative. It is not: an
        UNTRAINED head passes it on 320/320 ticks in 3/3 seeds, with a LARGER
        absolute range than a trained one (untrained 6.8e-4..1.27e-3 vs trained
        4.0e-4..5.7e-4) -- training LOWERS overall predicted spread while
        RAISING relative differentiation (max/min across action classes:
        trained 10.2-11.8x, untrained 1.15-1.28x). The real discriminator is
        the new `_last_pvar_relative_spread` (untrained 0.14-0.26, trained
        1.81-2.37, non-overlapping), added with a negative-control contract
        pinning why. Its proposed >=1.0 threshold is UNVALIDATED and
        deliberately not pinned. Read this node's 2026-08-22
        resume_condition as historical on that point: the shape of the argument
        was right (refuse a vacuous channel) and the specific metric was wrong.
        The staged design doc's section 5 carries the same wrong criterion and
        its correction is covered by
        chip-20260823-mech314bc-2x2-diversity-validation.

        (b) A THIRD GATE APPEARED AND HAS ALREADY BEEN PROBED. The candidate
        pool carries only ~2.0-2.4 distinct first-actions of K=32, identical
        trained vs untrained, so the head's ~10x differentiation can express at
        most a 2-valued vector where 314b is consumed (the V3-EXQ-614e
        monostrategy collapse, one layer down). Training the head was NECESSARY
        BUT NOT SUFFICIENT. The build session classified the next move as
        `complex (probe-gated)` rather than `complicated (buildable)` -- a spike
        on first-action diversity, not a build -- and THAT SPIKE HAS SINCE RUN:
        the ceiling is a CONFIG KNOB
        (`support_preserving_min_first_action_classes`), not an intrinsic
        proposer property. So it converts to `complicated (buildable)`, and the
        owed work is now a 2x2 validation (314b ON/OFF x diversity floor
        default/raised), chipped as
        chip-20260823-mech314bc-2x2-diversity-validation. Any validation MUST
        carry distinct-first-action count as a covariate or it risks reading a
        proposer-diversity null as a 314b null.

        status STAYS `open`. MECH-482's accumulator is still unbuilt -- the
        keystone cleared the way to its precondition, it did not build the
        accumulator, and follow-on item 2 (the accumulator itself) was
        explicitly held out of scope by the build. Flip to in_progress when the
        accumulator build starts. NOT re-chipped here: the validation and the
        section-5 correction are both already owned by the chip named above.

        2026-08-29 UPDATE (chip-20260827-mech482-accumulator-build,
        /implement-substrate, user-directed routing per
        work_graph_debt_classification_20260827.md addendum v1.1, which
        found both this node's gates cleared and chipped the accumulator
        build with a STOP-CHECK on the residual 2x2 validation state --
        confirmed cleared, V3-EXQ-949 PASS/supports 2026-08-25). THE
        ACCUMULATOR IS NOW BUILT: SD-102, ree-v3
        ree_core/policy/epistemic_deficit.py (EpistemicDeficitAccumulator),
        landed and pushed to origin/main. Fills the per_candidate_
        learning_progress slot; bit-identical OFF (curiosity_learning_
        progress_source stays "broadcast" by default); readiness-gated on
        e2_world_uncertainty_last_pvar_relative_spread > 0 per this node's
        own 2026-08-23 correction. Conservative scope: 3 of MECH-482's 5
        claims.yaml-listed candidate inputs (candidate-specific predictive
        uncertainty, persistent prediction error, predictive-system
        disagreement -- NOT failed-replay-resolution or competence-blocking-
        uncertainty), additive combination (NOT the full multiplicative
        importance x uncertainty x resolvability x persistence formula in
        the claim's title -- no importance/resolvability signal exists in
        the V3 substrate to combine multiplicatively). Full design + scoping
        rationale: REE_assembly/docs/architecture/sd_102_epistemic_deficit_
        accumulator.md. 18 new contracts green + 75 existing MECH-314/SD-063
        contracts re-run green (no regression). Validation experiment
        V3-EXQ-964 queued (EXPERIMENT_PURPOSE=diagnostic -- substrate
        readiness: does the accumulator populate and can it change candidate
        selection -- NOT MECH-482's own claim hypothesis, which needs a
        later evidence-purpose experiment once the substrate question is
        answered). claims.yaml MECH-482 gets an implementation_note only;
        v3_pending STAYS true (only the substrate-existence half of the
        non-degeneracy precondition is met -- the empirical half,
        cross-seed/cross-condition variance non-zero, awaits V3-EXQ-964).
        STATUS FLIP LEFT TO GOVERNANCE, per this chip's own brief: this note
        records the landing but does NOT flip ORNT-2's status field from
        `open` to `in_progress` -- that is /governance's call to make (next
        cycle should apply it, now that the accumulator build has genuinely
        started/landed, distinguishing this from the still-correct
        2026-08-23 "flip when the build starts" instruction above, which
        this update satisfies the precondition for without itself pulling
        the trigger).

    - id: "orienting_epistemic_deficit_v3:ORNT-3"
      title: "orient/survey: third primitive behavioural regime (diffuse, epistemic_deficit-driven)"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-483"]
      depends_on: ["orienting_epistemic_deficit_v3:ORNT-2"]
      cross_plan_link: []
      last_updated: 2026-08-13
      completion_note: >
        Registered in claims.yaml 2026-08-05 (thought-digestion), no owning
        closure node until this plan. DO NOT build in V3 yet. Driven by
        MECH-482's accumulator (ORNT-2); no independent build path exists
        ahead of that landing. Distinct from ORNT-1/MECH-395: diffuse and
        precedes cue identification, vs. MECH-395's narrow, already-identified-
        cue vector resolution.
    - id: "orienting_epistemic_deficit_v3:ORNT-4"
      title: "Open Q: does epistemic-deficit-driven orienting explain the cold-start competence split?"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: ["Q-089"]
      depends_on: ["orienting_epistemic_deficit_v3:ORNT-2", "orienting_epistemic_deficit_v3:ORNT-3"]
      cross_plan_link: []
      last_updated: 2026-08-13
      completion_note: >
        Registered in claims.yaml 2026-08-05 (thought-digestion), no owning
        closure node until this plan. No experiment proposal minted yet
        (substrate not V3-tractable as stated -- needs MECH-482/483 to exist
        first). Citation ambiguity flagged at registration and left
        unresolved: the intake's cited runs (V3-EXQ-875a/882a) are tagged in
        pending_review.md to MECH-471/MECH-472, not to MECH-457 (Q-089's
        depends_on target), recorded as related_claims rather than silently
        resolved.
    - id: "orienting_epistemic_deficit_v3:ORNT-5"
      title: "Defensive-orienting response: PAG-analog phasic gate (DefensiveOrientingGate)"
      phase: 1
      status: done
      severity: high
      owner_exq: null
      unblocks_claims: ["SD-099"]
      depends_on: []
      cross_plan_link: []
      last_updated: 2026-08-13
      completion_note: >
        IMPLEMENTED 2026-08-09 (session 906b-defensive-orienting-v3) via
        /implement-substrate -- ree_core/pag/defensive_orienting.py
        (DefensiveOrientingGate / DefensiveOrientingConfig /
        DefensiveOrientingOutput), a separate gate composed via OR with
        MECH-279's PAGFreezeGate, config-gated (use_defensive_orienting,
        default False, bit-identical off). Had NO owning closure node until
        this plan despite being fully built -- previously 0%-credited in V3
        closure purely by omission. status: done reflects the GATE build
        itself being complete; validation of its behaviour against
        ground-truth injected events is tracked separately at ORNT-6
        (MECH-489), which is the claim actually under active test.
    - id: "orienting_epistemic_deficit_v3:ORNT-6"
      title: "MECH-489 validation: defensive-orienting phasic behavioural chain"
      phase: 2
      status: in_progress
      severity: high
      owner_exq: "V3-EXQ-910b"
      unblocks_claims: ["MECH-489"]
      depends_on: ["orienting_epistemic_deficit_v3:ORNT-5"]
      cross_plan_link: []
      blocking_on: >
        V3-EXQ-910b RAN 2026-08-22 and is CONFIRMED-AUTOPSIED
        (failure_autopsy_V3-EXQ-910b_2026-08-23) as of the 2026-08-25
        governance cycle. C1 (sum(decision_counts) == n_override_ticks)
        PASSED exactly (21==21, unclassified=0) -- the decision_counts
        logging defect is validated fixed (SD-ORIENTING-DECISION-SCALE
        flipped implemented_pending_validation -> implemented_validated).
        But C1 also surfaced an unresolved instrument-correctness residual:
        the same-run legacy per-env-step readout diverges from the new
        override-tick readout by 5.95x (overrides) / 32.57x (decisions) --
        expected in direction (it is exactly the inflation the fix removes)
        but not itself independently cross-checked against a third
        measurement, so the combination rule (AND over C1 + C2) forces the
        overall read to MIXED rather than a clean supports. MECH-489
        claims.yaml: pending_retest_after_substrate flipped true -> false
        (the substrate blocker this node names is fully cleared); status
        stays candidate, evidence mixed. No further substrate build is
        owed by this finding; the autopsy's routing (implement-substrate)
        was discharged by resolving the SD-ORIENTING-DECISION-SCALE
        failure_record entry, not by a new build.
      resume_condition: >
        The claims.yaml substrate blocker is cleared; this node is not
        blocked on any further build. Remaining open question is whether
        the MIXED read (driven by the C1 legacy-vs-new-tap discrepancy,
        not by C2 valence-gating) warrants a further discriminating
        instrument-correctness check before this node can close, or
        whether MECH-489's mixed evidence is simply the standing read
        going forward. Left for a future governance/claim-synthesis pass
        to decide; no chip raised (this is a governance-owned disposition
        question, not a build).
      last_updated: 2026-08-25
      governance_2026_08_25: >
        Case 3 in closure-drift terms: V3-EXQ-910b has landed and been
        confirmed-autopsied, but its outcome is genuinely MIXED (not a
        PASS advancing toward closure and not a non_contributory/
        superseded/inconclusive direction that would auto-suppress) --
        the node legitimately stays non-terminal pending the disposition
        question in resume_condition, not because anything is still
        building.
      completion_note: >
        Had NO owning closure node until this plan despite real experimental
        evidence existing (V3-EXQ-910, V3-EXQ-910a; failure_autopsy_V3-EXQ-
        910a_2026-08-11 verdict: mixed -- trigger-alignment falsification
        reconfirmed with no new weight, and the new decision_alignment
        criterion FAILED but its underlying decision_counts measurement is
        independently broken (2x theoretical max, byte-identical to 910's
        total despite different override counts), so not usable as evidence
        either way). status: in_progress reflects this being actively
        tested, not merely registered and not stalled. Queue the 910a
        follow-on retest via /queue-experiment once ready.

        2026-08-21 refresh (chip-20260821-ornt6-owner-exq-stale-after-910b):
        the owed retest is now queued as V3-EXQ-910b (ree-v3 4d77ec9,
        status pending, supersedes V3-EXQ-910a) -- owner_exq and
        blocking_on updated accordingly and a resume_condition added. No
        manifest exists yet under evidence/experiments/, so this is a
        re-owning of the node, not a status advance; status stays
        in_progress.
---

# Orienting & Epistemic-Deficit Cluster -- V3 Closure Plan

**Registered:** 2026-08-13
**Status:** active
**Scope:** the six-claim orienting/epistemic-deficit family that had either no
closure-map owner at all (MECH-482, MECH-483, Q-089, MECH-489, SD-099) or an
owner filed under the wrong generation (MECH-395, previously
drives_motivation_v4:DRV-4). Spans two distinct timescales/triggers:
cue-triggered narrow orienting + diffuse epistemic-deficit-driven survey
(ORNT-1..4), and phasic, unidentified-onset defensive orienting
(ORNT-5/ORNT-6) -- registered together because MECH-489 (ORNT-6) explicitly
depends on both clusters plus MECH-279/MECH-205.

## One-line framing

> Six claims, one invisible gap: three (MECH-482/483/Q-089) had never been
> wired into any closure map, and two (MECH-489/SD-099) were absent even
> though one is already built and the other already has mixed experimental
> evidence. Registering them here does not change what's built or tested --
> it changes whether the V3 closure percentage can see it.

## Remaining work to close (5 of 6; ORNT-5 done)

| node | title | status | severity | active blocker |
|------|-------|--------|----------|-----------------|
| `ORNT-1` | MECH-395 pre-approach orienting (moved from DRV-4) | blocked | high | shared E3 selection-authority / cue-authority ceiling (V3-EXQ-812 successor) |
| `ORNT-2` | MECH-482 epistemic_deficit accumulator | in_progress | high | both 2026-08-22 gates CLEARED (doc reviewed; SD-063 training landed ree-v3 88287f11c6). Readiness criterion falsified -- use `_last_pvar_relative_spread`, not `dev_range`. Owed: 2x2 diversity validation (chip-20260823-mech314bc-2x2-diversity-validation). ACCUMULATOR BUILT 2026-08-29 (ree-v3 b69a1b8, SD-102, chip-20260827-mech482-accumulator-build) -- status FLIPPED to `in_progress` by /governance 2026-08-30 PM. Validation V3-EXQ-964 FAIL/non_contributory (C2 structurally unsatisfiable; autopsy confirmed + governance-ratified 28d14475a5); follow-on substrate entry sd_epistemic_deficit_multitarget_readiness created and CHIPPED 2026-08-30 PM |
| `ORNT-3` | MECH-483 orient/survey regime | open | medium | depends on ORNT-2 |
| `ORNT-4` | Q-089 cold-start-split question | open | medium | depends on ORNT-2 + ORNT-3 |
| `ORNT-6` | MECH-489 defensive-orienting validation | in_progress | high | 910a retest owed (substrate fix landed 2026-08-10) |

## Decision log

- **2026-08-13** (session curiosity-orienting-closure-gap-27d495,
  chip-20260813-curiosity-orienting-closure-map-gap): plan registered.
  Findings, code trace, and user-approved disposition are recorded in full
  in `registered_note` above. No claims.yaml edits; closure-map registration
  only. Closure-% impact of this registration (before -> after; regenerate
  `closure_status.md` for the authoritative figure): six nodes newly enter
  the V3 denominator (one moved from a v4 plan, five newly registered), of
  which only one (ORNT-5) is `done` and one (ORNT-6) is `in_progress` --
  the other four score 0.0-0.1, so the reported V3 closure percentage is
  expected to DROP by several points. This is the intended, honest
  correction: the prior percentage was overstated by omitting real
  remaining and in-progress work, not by overcounting done work.

- **2026-08-22** (session `pending-task-009a3a`, IGW-20260822-154, lane
  plan / reconcile): **ORNT-2 reconciled; status unchanged (`open`), blocker
  restated.** Re-verified the node against live `ree-v3`, `claims.yaml`,
  `substrate_queue.json` and the chip ledger. Three findings, all recorded on
  the node itself:
  1. **The accumulator is confirmed unbuilt**, so `open` is right. The only
     `epistemic_deficit` occurrences in `ree_core` are the *reserved* config
     enum value (`utils/config.py:4030-4037`, which explicitly falls back to
     `broadcast`) and comments at `agent.py:7587` /
     `policy/structured_curiosity.py:421,537` naming MECH-482 as the missing
     per-candidate learning-progress source.
  2. **The summary-table blocker was stale in both halves.** It read "GAP-A
     (substrate_queue.json) unclaimed"; in fact the GAP-A per-candidate slot
     LANDED 2026-08-08 (ree-v3 `c0e0ce8`) and ARC-065 is not merely unclaimed
     but `ready:false`. The node's own `completion_note` had already caught
     the first half on 2026-08-13; the table had not been updated to match.
     Both now agree.
  3. **The real gate is one step further down, and is unowned.** MECH-482's
     non-degeneracy precondition needs per-candidate target-bound uncertainty
     to be *live*, not merely *possible*. The slot is capability; the genuine
     314b source (SD-063 `E2WorldUncertaintyHead`) is instantiated on the
     agent but UNTRAINED, and its phased P0->P1->P2 training loop -- follow-on
     item 1 of `mech314bc_percandidate_extension_staged_2026-08-08.md`, and
     that doc's own "actual keystone" -- has **never been chipped** (scan of
     all 1435 `TASK_CHIPS.json` entries: zero chips naming SD-063 /
     `e2_predictive_variance` / head training since 2026-08-08). It is also
     unowned by the closure map: **no** `*_plan.md` mentions SD-063 /
     `E2WorldUncertaintyHead` / `e2_predictive_variance` at all, and
     `behavioral_diversity_isolation:GAP-A` is `done` and scoped to a
     different concern (CEM elite-pool collapse). Captured in new
     `blocking_on` / `resume_condition` fields, the same shape ORNT-6 gained
     on 2026-08-21.

  Nothing in the 9 days since 2026-08-13 advanced this node. **No
  `claims.yaml` edits**, consistent with this plan's registration posture;
  closure percentage is unchanged (no node status moved).

  *Separate finding, recorded but NOT actioned here (out of this item's
  scope, and `claims.yaml` is governance-only):* four of this plan's six
  scope claims -- MECH-395, MECH-482, MECH-483, Q-089 -- still carry
  `location: evidence/planning/drives_motivation_v4_plan.md` in
  `claims.yaml`, stale since the 2026-08-13 move into this plan. Verified
  **not** a closure-percentage bug: none of the three closure-tracking
  consumers (`generate_closure_snapshot.py`, `check_closure_drift.py`,
  `serve.py`) reads the `location` field -- node ownership is bound via
  `unblocks_claims` in this frontmatter. It is navigational drift only.
  `check_closure_drift.py` reports `drifted_nodes=0` for this plan.
