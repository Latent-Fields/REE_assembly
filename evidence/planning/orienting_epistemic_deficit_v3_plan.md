---
closure_plan:
  id: orienting_epistemic_deficit_v3
  title: "Orienting & Epistemic-Deficit Cluster (V3 closure)"
  registered: 2026-08-13
  last_updated: 2026-08-13
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
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-482"]
      depends_on: []
      cross_plan_link: []
      last_updated: 2026-08-13
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
        claims.yaml MECH-489 carries pending_retest_after_substrate: true --
        SD-ORIENTING-DECISION-SCALE (ree-v3 agent.py select_action()
        Component 4/5) landed 2026-08-10, fixing the norm-vs-value scale
        mismatch failure_autopsy_V3-EXQ-910_2026-08-10 identified. The clean
        valence-gating retest is now queued as V3-EXQ-910b (ree-v3 4d77ec9,
        status pending, supersedes V3-EXQ-910a), which also repairs the
        decision_counts readout to count at the override tick only rather
        than once per env step. Blocked on that run actually executing and
        its criteria being adjudicated -- no manifest exists yet. The
        trigger-alignment sub-claim already stands as fairly falsified
        (V3-EXQ-910/910a) and does not need re-testing.
      resume_condition: >
        Resume once V3-EXQ-910b's manifest lands under
        REE_assembly/evidence/experiments/ and its pre-registered criteria
        are adjudicated (C1: sum(decision_counts) == n_override_ticks
        exactly; C2: decision_alignment non-degenerate, >= 2 of the 3
        decision classes non-zero). A pass advances this node toward
        closure; a fail/mixed outcome routes to a failure autopsy before
        any further retesting is queued.
      last_updated: 2026-08-21
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
| `ORNT-2` | MECH-482 epistemic_deficit accumulator | open | high | GAP-A (substrate_queue.json) unclaimed |
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
