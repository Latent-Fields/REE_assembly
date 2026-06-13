---
closure_plan:
  id: drives_motivation_v4
  generation: v4
  title: "Drives & Motivation (V4 forward roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [SD-012, MECH-216, MECH-295, MECH-111, MECH-347, ARC-073, SD-057]
  sibling_plans: [goal_pipeline, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. The
    value here is the readiness_gate field per node: the V3-era prerequisites
    (claims / tracks / experiments) that must land before each V4 motivation
    step is honest to build. Node status is open / blocked / in_progress /
    deferred (never done -- these are unbuilt). generation: v4 keeps these nodes
    OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, check_closure_drift.py are generation-aware).
    A node graduates from roadmap to closure-tracked by gaining an owner_exq
    once its first V4 experiment is queued. Scope: the motivational layer beyond
    the single homeostatic food/energy axis -- a register of non-terminal needs,
    arbitration across simultaneously-active drives, and the orienting/surveying
    drive that scaffolds cue ecology before object-bound wanting.
  nodes:
    - id: "drives_motivation_v4:DRV-1"
      title: "Non-terminal drive register (drives beyond hunger/thirst as first-class axes)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["SD-060", MECH-111]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 LIVE single-axis homeostatic drive: SD-012 (drive_level = 1.0 - energy from obs_body[3]; drive_weight=2.0 scales effective_benefit) -- one axis only (food/energy)"
        - "V3 has scattered intrinsic-drive seeds NOT unified into a register: MECH-111 curiosity/novelty (EMA -> E3 routing currently broken, EXQ-141b/590a); SD-012 homeostatic; ARC-073 play competence-saturation drive pressure"
        - "DECISION the register forces: which axes are first-class (exploration / play / social / learning / grooming-rest in addition to depletion), and is each a scalar drive_level on its own homeostatic-style integrator or a derived/contextual signal?"
      last_updated: 2026-06-10
      completion_note: "Per thought_intake_2026-06-04_non_terminal_need_launch.md S2: nursery scaffolding + weaning arc already exist; the genuinely NEW framing is treating non-food needs as a register of first-class drive axes rather than one energy scalar. This is the precondition for arbitration (DRV-2) and for the orienting drive (DRV-4) to have a need to gate on."
    - id: "drives_motivation_v4:DRV-2"
      title: "Multidrive arbitration / orchestration policy (which drive wins when several are active)"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-394", MECH-295]
      depends_on: ["drives_motivation_v4:DRV-1"]
      cross_plan_link: []
      blocking_on: "Requires the DRV-1 register (multiple simultaneously-active drive axes) to exist before an arbitration policy across them is meaningful; today only the single SD-012 axis is live, so there is nothing to arbitrate."
      readiness_gate:
        - "V3 LIVE drive->approach plumbing the policy must compose over: MECH-295 (drive->liking->approach bridge, narrowed to modulatory; substrate_ceiling), MECH-216 (E1 schema-readout wanting), MECH-290 (backward credit sweep), MECH-307 (anticipatory liking)"
        - "V3 LIVE single-axis competition precedent: ARC-073 play-to-real transition by competence saturation (d(PE)/dt) OR homeostatic-vs-synthetic-goal pressure (Pezzulo 2014 exploratory-vs-homeostatic ratio) -- the seed of a competition rule, but only between play and one homeostatic axis"
        - "Cross-plan: goal_pipeline arbitration of z_goal seeding/override must be settled before drive arbitration layers on top"
        - "DECISION: arbitration mechanism (soft-competitive disinhibition vs weighted blend vs WTA) and the orchestration variables (context, satiation level per axis, inter-drive competition, developmental phase)"
      last_updated: 2026-06-10
      completion_note: "thought_intake_2026-06-04_non_terminal_need_launch.md frames drives as 'orchestrated over context / satiation / competition / dev-phase'. REE already has single-axis competition (ARC-073) and a vocabulary for soft-competitive arbitration (Q-016 tri-loop cluster) but no policy that arbitrates ACROSS a multidrive register. New claim proposed."
    - id: "drives_motivation_v4:DRV-3"
      title: "Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)"
      phase: 2
      status: open
      lit_pull_status: none
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-394", "SD-060"]
      depends_on: ["drives_motivation_v4:DRV-1"]
      cross_plan_link: []
      readiness_gate:
        - "Project rule feedback_biology_before_formal_definitions: commission a biology lit-pull BEFORE registering the arbitration MECH (drive competition / hypothalamic drive hierarchy / opportunity-cost theories: Berridge incentive salience already in SD-012/MECH-295; need lateral-hypothalamus / dopamine tonic-vigour / Pezzulo 2014 exploratory-vs-homeostatic / Niv 2007 opportunity-cost-of-time)"
        - "L-non-terminal-needs: ethology of non-feeding drives (grooming, play, exploration) as homeostatically-regulated systems, not just deficit-reduction"
      last_updated: 2026-06-10
      completion_note: "The arbitration policy (DRV-2) instantiates a formal competition mechanism; per the biology-before-formal-definitions rule it must be grounded before registration to avoid the SD-003 / SD-010 philosophy-right / mechanism-wrong failure mode. This node tracks that grounding debt."
    - id: "drives_motivation_v4:DRV-4"
      title: "Orienting/surveying drive: pre-approach active-sensing control state"
      phase: 3
      status: blocked
      blocker_class: v3_gate
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-395"]
      depends_on: ["drives_motivation_v4:DRV-1"]
      cross_plan_link: []
      blocking_on: "Gated on the live cue-recall diagnostic thread: register the orienting MECH only if V3-EXQ-640+ shows the discriminating pattern (cue fires, no contact, AND no orienting/surveying occurs). 640 must first separate missing-orienting from raw cue-to-action-authority failure."
      readiness_gate:
        - "V3 LIVE upstream cue chain the orienting mode sits between: SD-057 / MECH-347 cue-triggered wanting (cue recall fires), MECH-295 drive->liking->approach (assumes an approach vector already exists)"
        - "V3 LIVE distinct neighbours to keep separate: MECH-111 curiosity/novelty (broad info-seeking, not cue-triggered local sampling), attention/precision-selection (content weighting, not motor active-sensing)"
        - "Live diagnostic thread: V3-EXQ-638a (cue fires, contact does not lift) + V3-EXQ-640 (post-cue action/gradient instrumentation) -- the routing-table discriminator in thought_intake_2026-06-04_orienting_surveying_drive.md S5"
        - "Snail-race method: build the orient/survey DIAGNOSTIC (orient_mode_entries_after_cue, survey_steps, heading_entropy, gradient_information_gain) BEFORE any orienting substrate"
      last_updated: 2026-06-10
      completion_note: "thought_intake_2026-06-04_orienting_surveying_drive.md S3/S4: a cue-triggered, need-gated, pre-approach active-sensing mode -- distinct from curiosity, cue recall, and approach. It is what FINDS the approach vector MECH-295 assumes. Currently a routing hypothesis; the gate is the 640 result pattern. New claim proposed."
    - id: "drives_motivation_v4:DRV-5"
      title: "Non-terminal failure-grade taxonomy as a transfer-world launch profile"
      phase: 4
      status: deferred
      blocker_class: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["Q-071"]
      depends_on: ["drives_motivation_v4:DRV-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 LIVE scaffold substrate it formalises: scaffolded_sd054_onboarding (nursery / protected consolidation / forced feeding, Stage-0/0b); goal-pipeline stages; the cue-ecology weaning arc"
        - "DEFERRED gate: only actionable when transfer-world / new-ecology work is actually scheduled; the four-grade taxonomy (terminal / soft / developmental / autonomous) becomes the acceptance scaffold for a launch profile then, not before"
        - "Open Q the deferral protects: forgiveness-vs-drive tradeoff (how forgiving can the world be before depletion stops producing meaningful drive) -- empirical, transfer-world"
      last_updated: 2026-06-10
      completion_note: "thought_intake_2026-06-04_non_terminal_need_launch.md S1/S5: the failure-grade taxonomy + minimal-launch-kit are NOVEL framing but explicitly self-scoped as future transfer-world design, off the V3 critical path. Deferred (not open) to honour the intake's containment instruction; the orienting drive (DRV-4) is the one launch-kit primitive with a live V3 thread."
---
# Drives & Motivation -- V4 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the motivational layer beyond REE's single homeostatic
food/energy axis -- a register of non-terminal needs (DRV-1), an arbitration
policy across simultaneously-active drives (DRV-2) and its biology grounding
(DRV-3), the orienting/surveying drive that scaffolds cue ecology before
object-bound wanting (DRV-4), and the non-terminal failure-grade taxonomy that
turns those drives into a transfer-world launch profile (DRV-5).

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant against them. The
value here is the **readiness gates** -- for each motivation step, exactly which
V3-era prerequisites (claims / tracks / experiments) must land before the V4
substrate work is honest to build.

---

## One-line framing

> REE has ONE drive that orchestrates behaviour: SD-012 homeostatic food/energy.
> Curiosity (MECH-111), play-pressure (ARC-073), and cue-triggered wanting
> (MECH-347) exist as isolated seeds with no shared register, no arbitration
> across them, and no pre-approach orienting mode between "something matters" and
> "move toward it". This plan registers the spine -- a non-terminal drive
> register, a multidrive arbitration policy, and the orienting drive -- and pins
> each step's V3 readiness gate.

---

## The motivation steps (in dependency order)

| Step | Node | Seed / claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| 1 -- drive register | DRV-1 | SD-012 + MECH-111/ARC-073 (NEW register) | V4 first decision | unify scattered drive seeds into first-class axes |
| 2 -- arbitration | DRV-2 | MECH-295/216/290/307 + ARC-073 (NEW policy) | V4 | DRV-1 register exists; goal_pipeline arbitration settled |
| 2 -- grounding | DRV-3 | NEW arbitration claim | cross-cutting | drive-competition / opportunity-cost biology lit-pull |
| 3 -- orienting drive | DRV-4 | SD-057/MECH-347/MECH-295 (NEW MECH) | V4, gated on 640 | EXQ-640 shows cue-fires-no-contact-no-orienting |
| 4 -- launch profile | DRV-5 | scaffolded_sd054_onboarding (NEW criterion) | deferred / transfer-world | only when transfer-world work is scheduled |

---

## What this plan deliberately does NOT pull into V3

- **No new drive axes are added to ree-v3 now.** SD-012's single food/energy
  axis stays the only live homeostatic drive. The register (DRV-1) is a V4
  design decision; registering this roadmap changes no V3 behaviour.
- **The orienting drive is NOT registered as a claim yet.** Per
  `thought_intake_2026-06-04_orienting_surveying_drive.md`, it is a routing
  hypothesis whose gate is the V3-EXQ-640 result pattern. DRV-4 is `blocked` on
  that diagnostic; do not build an orienting substrate before 640 discriminates
  missing-orienting from cue-to-action-authority failure.
- **The failure-grade taxonomy stays deferred (transfer-world).** DRV-5 is
  explicitly self-scoped by its intake as future new-ecology work, off the V3
  critical path. It is `deferred`, not `open`, to honour that containment.
- **MECH-295 / goal-pipeline GAP work is owned elsewhere.** MECH-295's
  modulatory re-scope and GAP-4 closure live in `goal_pipeline`; this roadmap
  consumes the drive->approach bridge, it does not re-litigate it.

---

## Source artefacts

| Artefact | Role |
|---|---|
| evidence/planning/thought_intake_2026-06-04_non_terminal_need_launch.md | non-food drives + orchestration + failure-grade taxonomy + minimal launch kit |
| evidence/planning/thought_intake_2026-06-04_orienting_surveying_drive.md | orienting/surveying as pre-approach active sensing + routing table |
| claims.yaml SD-012 | live single-axis homeostatic drive (the substrate this builds beyond) |
| claims.yaml MECH-111 / ARC-073 | scattered intrinsic-drive seeds (curiosity, play-pressure) to unify into DRV-1 |
| claims.yaml MECH-295 / MECH-216 / MECH-290 / MECH-307 | the drive->approach pathways DRV-2 must arbitrate over |
| claims.yaml SD-057 / MECH-347 | cue-triggered wanting -- the chain DRV-4 inserts an orienting step into |
| evidence/planning/goal_pipeline_plan.md | sibling plan owning z_goal seeding/override arbitration |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap (drives & motivation
  area of the V4 = individual-mind tier). Nodes seeded from SD-012 + the two
  2026-06-04 non-terminal-need / orienting-drive intakes. Readiness gates pinned
  per step. Three NEW prose-only capabilities flagged for claim registration via
  proposed_claims (non_terminal_drive_register, multidrive_arbitration_policy,
  pre_approach_orienting_mode) plus a transfer-world design criterion
  (non_terminal_failure_profile). `generation: v4` set so the V3 closure % is
  unaffected. No claims.yaml edits.
