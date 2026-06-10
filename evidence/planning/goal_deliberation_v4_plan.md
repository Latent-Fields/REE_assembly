---
closure_plan:
  id: goal_deliberation_v4
  generation: v4
  title: "Multi-slot Goal Deliberation, Counterfactual Branching, Interrupted-task Resumption (V4 roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [SD-046, SD-033e, MECH-264, MECH-265, SD-027, SD-028, MECH-254, MECH-255, Q-068]
  sibling_plans: [goal_pipeline, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 substrate step is honest to build. generation: v4
    keeps these nodes OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, and check_closure_drift.py are all
    generation-aware). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V4 experiment is queued. The spine of
    this plan is the move from V3's single-stream goal pipeline
    (one z_goal, one ghost-goal-bank rank, one committed trajectory per tick)
    to a frontopolar-analog deliberation layer that holds MULTIPLE goals,
    tracks the value of the unchosen alternative, and can interrupt, park, and
    RESUME a task across capacity windows.
  nodes:
    - id: "goal_deliberation_v4:GDL-1"
      title: "Single-slot vs multi-slot fork (the first design decision: does V4 widen GoalState to N>=2?)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [SD-046]
      depends_on: []
      cross_plan_link: ["goal_pipeline:GAP-2"]
      readiness_gate:
        - "V3 goal pipeline is SINGLE-STREAM: one z_goal, one SD-039 ghost-goal-bank rank, one E3-committed trajectory per heartbeat (goal_pipeline GAP-1 substrate landed 2026-05-11)"
        - "DECISION the fork forces: does the V4 substrate hold N>=2 simultaneously-active goal slots (SD-046 multi-slot GoalState, each with per-slot z_goal + drive coupling + age + persistence), or stay single-slot and only ADD a counterfactual-value monitor over the one stream? Every node below assumes the multi-slot answer; if V4 stays single-slot, GDL-3/4/5 collapse into a thinner monitor-only design"
        - "The single-stream pipeline must itself be honest first: goal_pipeline GAP-2 (cue/wanting -> action authority -> benefit-contact) is the live V3 bottleneck and is NOT yet closed (foraging/benefit-contact leg still substrate-blocked, 2026-06-10). A multi-slot arbitrator over a pipeline that cannot reliably commit ONE goal would be vacuous"
      last_updated: 2026-06-10
      completion_note: "SD-046 is candidate / implementation_phase v4. This node is the design decision, not the build: choosing multi-slot is the precondition for the dACC-style cross-slot arbitrator and for every deliberation pillar below. Genuine architectural fork, not a missing flag."
    - id: "goal_deliberation_v4:GDL-2"
      title: "PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [SD-033e]
      depends_on: ["goal_deliberation_v4:GDL-1"]
      cross_plan_link: []
      blocking_on: "Gated on the V3 operating_mode primitive being behaviourally exercisable: SD-032a discrete operating_mode + MECH-259 switch threshold landed (V3-EXQ-446/455 PASS), but the alternative-mode behaviour they unlock is V_s-monostrategy-limited until SD-032b dACC + the goal_pipeline GAP-2 contact leg land. A disengage-to-explore module has nothing to switch BETWEEN until alternative modes are real."
      readiness_gate:
        - "V3 HOOKS present: SD-032a operating_mode vocabulary (discrete-mode primitive, landed) + SD-033c vmPFC value-integration (implementation_phase v3) -- SD-033e reserves its hooks via operating_mode and consolidates SD-033c's chosen-option value signal"
        - "SD-033e adds the UNCHOSEN side: it mediates transitions between external engagement and internally-generated deliberation and enables disengagement from the current task to explore alternatives -- requires at least two distinguishable engagement modes to exist behaviourally (SD-032b dACC + alternative-mode behaviour, currently monostrategy-blocked)"
        - "MECH-163 multi-step hippocampal planning (implementation_phase v3) -- shared V4-entry gate; deliberation over alternatives presupposes multi-step rollout of each alternative"
      last_updated: 2026-06-10
      completion_note: "SD-033e (candidate, v4): the frontopolar module that maintains counterfactual-value estimates for alternatives, mediates engage<->deliberate transitions, and monitors relative importance across active goals. V3 reserves the hooks; this node tracks the V4 substrate build once alternative modes are behaviourally real."
    - id: "goal_deliberation_v4:GDL-3"
      title: "PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-264]
      depends_on: ["goal_deliberation_v4:GDL-1", "goal_deliberation_v4:GDL-2"]
      cross_plan_link: []
      blocking_on: "Gated on GDL-2 (the SD-033e module that hosts the counterfactual estimate) and on a credible per-alternative value read, which presupposes the goal_pipeline GAP-2 z_goal-not-collapsed substrate (490-cohort autopsies show z_goal collapses and per-candidate bias range goes to 0.0 on the current substrate -- a counterfactual estimate over collapsed alternatives is uninformative by construction)."
      readiness_gate:
        - "V3 has the CHOSEN-option value signal (SD-033c vmPFC value integration, v3); MECH-264 adds a PARALLEL running estimate of the value of UNCHOSEN alternatives, with a threshold-sensitive switch-to-alternative signal when the counterfactual exceeds the chosen value by a margin"
        - "Requires non-degenerate per-alternative value: goal_pipeline GAP-4 / MECH-295 autopsies (490j..490k) found mech295_bias_range_mean=0.0 (per-candidate bias uniform) -- the V4 counterfactual monitor needs the substrate to deliver a real cross-alternative value spread first (substrate_queue scaffolded_sd054_onboarding)"
        - "MECH-264 lesion-analogue should reproduce the Mansouri 2015 over-focus phenotype -- needs the multi-goal arena (GDL-1 multi-slot) to be instantiable"
      last_updated: 2026-06-10
      completion_note: "MECH-264 (candidate, v4): the switch-to-alternative mechanism that turns SD-033e from a passive value-store into an actor. Honest only once alternatives carry distinguishable value (GAP-2/GAP-4 substrate) and the SD-033e host exists (GDL-2)."
    - id: "goal_deliberation_v4:GDL-4"
      title: "PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-265, SD-046]
      depends_on: ["goal_deliberation_v4:GDL-1", "goal_deliberation_v4:GDL-2"]
      cross_plan_link: []
      blocking_on: "Gated on GDL-1 (multi-slot GoalState must exist to monitor relative importance ACROSS slots) and GDL-2 (SD-033e hosts the relative-importance representation). Single-slot V3 has nothing to compare across."
      readiness_gate:
        - "SD-046 multi-slot GoalState: each slot generates its own ghost-goal-bank rank, ghost-probe budget, and proposer trajectories; a dACC-style arbitrator selects which slot's best trajectory commits this tick -- requires the GDL-1 multi-slot decision AND a working single-slot ghost-goal-bank to replicate per slot (SD-039 landed v3)"
        - "MECH-265 maintains relative importance across the active goal set (parallel, not pairwise) for flexible switching -- this is the read the arbitrator consumes; lesion analogue = Mansouri 2015 over-focus + novel-rule impairment"
        - "SD-032b dACC implementation (currently V_s-monostrategy-blocked) is the closest V3 arbitrator substrate; the V4 cross-slot arbitrator is its multi-goal generalisation"
      last_updated: 2026-06-10
      completion_note: "MECH-265 + SD-046 (both candidate, v4): the relative-importance read and the arbitrator that consumes it. The arbitrator is the load-bearing new machinery of multi-slot deliberation -- it is what makes N>=2 goals coexist without thrashing."
    - id: "goal_deliberation_v4:GDL-5"
      title: "PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:interrupted_task_resumption_mechanism"]
      depends_on: ["goal_deliberation_v4:GDL-1", "goal_deliberation_v4:GDL-4"]
      cross_plan_link: ["goal_pipeline:GAP-2"]
      blocking_on: "Gated on a V3 demonstration that the interrupt->resume span is the actual failure mode: register the resumption mechanism as a candidate MECH only when a V3 autopsy (640+) shows hazard-interrupt WITHOUT resume (per thought_intake_2026-06-05 step 2). Until then it is a prose gap with a placeholder."
      readiness_gate:
        - "V3 has the CLOSURE side of the action arc (MECH-061 commit-boundary token v3; MECH-057a completion gate; beta gate) and world-staleness invalidation (V_s, goal_pipeline GAP-6 done) -- but NOT the 'was working on X, got interrupted, resume when capacity allows' span (memory project_interrupted_task_resumption_gap)"
        - "The event-arc spine (thought_intake_2026-06-05_cross_version_missing_bits): action = initiate -> persist -> INTERRUPT -> reorient -> RESUME -> closure. The interrupt->reorient->resume span is the underdeveloped one; resumption needs a parked goal slot to return to, hence the SD-046 multi-slot dependency (GDL-1) and the arbitrator that re-prioritises it (GDL-4)"
        - "Multi-step hippocampal planning (MECH-163) to reconstruct the parked task context on resume"
      last_updated: 2026-06-10
      completion_note: "PROSE-ONLY gap today (no claim). MECH-320 in claims.yaml is a tonic-vigor / opportunity-cost mechanism (v3, candidate_substrate_landed) and is NOT the resumption mechanism, despite the memory note's 'candidate MECH-320 sketch' phrasing -- do not reuse that ID. Proposing NEWCLAIM:interrupted_task_resumption_mechanism: a parked-goal persistence + capacity-keyed re-prioritisation hypothesis that closes the event-arc interrupt->resume span."
    - id: "goal_deliberation_v4:GDL-6"
      title: "PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberation"
      phase: 2
      status: blocked
      severity: medium
      owner_exq: null
      unblocks_claims: [SD-027, SD-028, MECH-254, MECH-255]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-1"]
      blocking_on: "Gated on the V3 attention substrate being more than the MECH-089 packaging op: SD-027 asserts a SELECTION gate UPSTREAM of packaging, and there is no boundary-gate primitive in V3 code today (selection is currently implicit in E3). It is a parallel V4 substrate, not on the GDL-2..GDL-5 critical path, but it is what makes multi-goal deliberation tractable under capacity limits."
      readiness_gate:
        - "V3 HOOKS: MECH-089 theta-gamma packaging (formats content for E3) + SD-026 z_goal write channel (v3, transport) -- SD-027/SD-028 sit UPSTREAM (which content is selected) and ALONGSIDE (the template object), distinct from both"
        - "SD-027 pulvinar-TRN boundary gate + MECH-254 top-k selection (precision x z_goal template gain x NA salience); SD-028 attentional template as a first-class precision-space object + MECH-255 vmPFC-dlPFC template compiler"
        - "Cross-link object_representation_v4:OBJ-1 -- the template's content keys on whatever the object fork resolves (type/token); the attentional template and the object-file co-evolve"
      last_updated: 2026-06-10
      completion_note: "SD-027/SD-028/MECH-254/MECH-255 (all candidate, v4): the capacity-limited access architecture. Deliberation over N>=2 goals is only bounded if access to E3 is gated; this pillar supplies the bound. Parallel to the deliberation core, hence depends_on [] (no upstream GDL node) but cross-linked to the object fork."
    - id: "goal_deliberation_v4:GDL-7"
      title: "Graded action-status vocabulary -- decide whether deliberation needs an explicit simulated!=intended!=committed annotation (Q-068)"
      phase: 4
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: [Q-068]
      depends_on: ["goal_deliberation_v4:GDL-3", "goal_deliberation_v4:GDL-5"]
      cross_plan_link: []
      readiness_gate:
        - "Q-068 is an OPEN QUESTION (answer_state): does REE need an explicit graded action-status vocabulary (simulated != rehearsed != intended != committed != acted, + a self_reference_frame), or do MECH-094 simulation/commit write-profiles (v3) + MECH-061 commit-boundary token (v3) already carry the distinction?"
        - "The question becomes decidable only once counterfactual branching (GDL-3) and parked/resumed tasks (GDL-5) exist: deliberation over unchosen alternatives is exactly where 'simulated vs intended vs committed' must be machine-distinguishable, and resumption needs to know a parked task's prior action-status"
        - "Resolve by working through whether the existing write-profiles disambiguate the new deliberation states; if not, register the vocabulary as a first-class annotation"
      last_updated: 2026-06-10
      completion_note: "Q-068 (candidate, v4, open_question): deferred until the deliberation pillars create states that actually stress the existing write-profile vocabulary. Answering it earlier would be premature -- the distinguishing pressure does not exist in single-stream V3."
---
# Multi-slot Goal Deliberation -- V4 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the move from V3's single-stream goal pipeline to a
frontopolar-analog deliberation layer -- multi-slot GoalState (SD-046),
counterfactual-value tracking + switch gate (SD-033e / MECH-264), cross-goal
relative-importance monitoring + dACC arbitrator (MECH-265), capacity-limited
E3 access + attentional template (SD-027/028/254/255), and the underdeveloped
interrupt->reorient->resume span of the event-arc (Zeigarnik resumption) -- so
V4 substrate work slots in against a registered spine instead of bolting a
multi-goal arbitrator onto a pipeline that cannot reliably commit one goal.

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them. The
value here is the **readiness gates** -- for each pillar, exactly which V3-era
prerequisites (claims/tracks) must land before the V4 substrate step is honest
to build.

---

## One-line framing

> V3 deliberates over ONE goal stream: one z_goal, one ghost-goal-bank rank, one
> committed trajectory per heartbeat. The frontopolar lobe in biology does the
> opposite -- it holds the alternative you DIDN'T pick, monitors the relative
> importance of several active goals at once, and lets you disengage to explore.
> That whole capacity is reserved-but-absent in REE (SD-033e hooks only). This
> plan sequences its construction, and pins each step to the V3 prerequisite that
> must land first -- because a counterfactual monitor over a collapsed z_goal, or
> an arbitrator over a single slot, is vacuous by construction.

---

## The pillars (one deliberation primitive, five faces)

| Pillar | Node | Claim(s) | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| (fork) single vs multi-slot | GDL-1 | SD-046 | V4 (first decision) | single-stream pipeline GAP-2 must commit ONE goal first |
| 1 -- frontopolar module | GDL-2 | SD-033e | V4, V3 hooks | SD-032a operating_mode + SD-033c value (alt modes monostrategy-blocked) |
| 2 -- counterfactual switch | GDL-3 | MECH-264 | V4 | non-degenerate per-alternative value (GAP-4/MECH-295 bias_range=0.0 today) |
| 3 -- relative-importance + arbitrator | GDL-4 | MECH-265, SD-046 | V4 | multi-slot (GDL-1) + SD-032b dACC (monostrategy-blocked) |
| 4 -- interrupt/resume (Zeigarnik) | GDL-5 | NEWCLAIM | V4, V3 trigger | closure side exists (MECH-061/057a); interrupt->resume span absent |
| 5 -- capacity access + template | GDL-6 | SD-027/028/254/255 | V4 (parallel) | MECH-089 packaging + SD-026 transport; no boundary-gate primitive yet |
| graded action-status | GDL-7 | Q-068 | V4 (deferred Q) | decidable only after GDL-3 + GDL-5 stress the write-profiles |

---

## The event-arc spine (why interrupt/resume is its own pillar)

Action is not a point event; it is an arc:
`initiate -> persist -> interrupt -> reorient -> resume -> complete / fail / abandon`
(thought_intake_2026-06-05_cross_version_missing_bits). REE has the BEGINNING
(cue/commit, MECH-061) and the END (completion gate MECH-057a, V_s staleness
invalidation), but the **interrupt -> reorient -> resume** span is the
underdeveloped one -- exactly the gap memory `project_interrupted_task_resumption_gap`
records. In a single-slot pipeline there is nowhere to park an interrupted task;
resumption needs a multi-slot GoalState (GDL-1) to hold the parked goal and a
cross-slot arbitrator (GDL-4) to re-prioritise it when capacity returns. That is
why GDL-5 is the deliberation layer's load-bearing extension, not a separate
plan. Per the intake's own gating rule, the resumption MECH is registered only
when a V3 autopsy (640+) routes there (hazard-interrupt without resume); until
then it is `NEWCLAIM:interrupted_task_resumption_mechanism`.

---

## What this plan deliberately does NOT pull into V3

- **No widening of the V3 goal pipeline to multi-slot.** SD-046 multi-slot
  GoalState is V4. The live V3 work (goal_pipeline GAP-2) must make the SINGLE
  stream honestly commit-and-contact first; a multi-slot arbitrator over a
  pipeline that cannot commit one goal is vacuous. Containment per
  `feedback_ree_assembly_externalised_cognition` (keep V4 off the V3 race).
- **No early registration of the resumption mechanism.** Per the event-arc
  intake's own rule, register the Zeigarnik MECH only when a V3 autopsy routes
  there. Today it is a placeholder, not a claim.
- **MECH-320 is NOT the resumption mechanism.** It is a tonic-vigor /
  opportunity-cost score bias (v3, substrate-landed). The memory note's
  "candidate MECH-320 sketch" phrasing predates MECH-320's actual registration on
  a different subject; do not reuse that ID for resumption.
- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour and does not touch the V3 closure %.

---

## Source artefacts

| Artefact | Role |
|---|---|
| claims.yaml SD-046 / SD-033e / MECH-264 / MECH-265 | multi-slot + frontopolar deliberation cluster (all candidate, v4) |
| claims.yaml SD-027 / SD-028 / MECH-254 / MECH-255 | capacity-limited E3 access + attentional template cluster (candidate, v4) |
| claims.yaml Q-068 | graded action-status vocabulary open question (candidate, v4) |
| [evidence/planning/thought_intake_2026-06-05_cross_version_missing_bits.md](thought_intake_2026-06-05_cross_version_missing_bits.md) | the event-arc spine + per-version closure-question framing |
| memory project_interrupted_task_resumption_gap | the Zeigarnik resumption gap (REE has staleness invalidation, not resume) |
| [evidence/planning/goal_pipeline_plan.md](goal_pipeline_plan.md) | sibling V3 plan; GAP-2 (contact) is the live prerequisite for GDL-1 |
| claims.yaml SD-032a / SD-032b / SD-033c / MECH-163 / MECH-061 / MECH-057a | V3 hooks the deliberation layer reserves or extends |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap, sibling to
  object_representation_v4 and to the V3 goal_pipeline plan. Nodes seeded from
  the SD-033e / SD-046 deliberation cluster and the SD-027/028 access cluster.
  Readiness gates pinned per pillar; the load-bearing gate throughout is that the
  single-stream V3 pipeline (goal_pipeline GAP-2) must reliably commit-and-contact
  ONE goal before a multi-slot arbitrator is honest. `generation: v4` set so the
  V3 closure % is unaffected. The interrupt->resume span registered as a
  prose-only NEWCLAIM placeholder (NEWCLAIM:interrupted_task_resumption_mechanism)
  per the event-arc intake's gating rule -- NOT folded onto MECH-320, which is a
  distinct tonic-vigor mechanism. No claims.yaml edits.
