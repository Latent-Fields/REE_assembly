---
closure_plan:
  id: drives_motivation_v4
  generation: v4
  title: "Drives & Motivation (V4 forward roadmap)"
  registered: 2026-06-10
  last_updated: 2026-08-05
  scope_claims: [SD-012, MECH-216, MECH-295, MECH-111, MECH-347, ARC-073, SD-057]
  sibling_plans: [goal_pipeline, object_representation_v4, orienting_epistemic_deficit_v3]
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
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["SD-060", MECH-111]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 LIVE single-axis homeostatic drive: SD-012 (drive_level = 1.0 - energy from obs_body[3]; drive_weight=2.0 scales effective_benefit) -- one axis only (food/energy)"
        - "V3 has scattered intrinsic-drive seeds NOT unified into a register: MECH-111 curiosity/novelty (EMA -> E3 routing currently broken, EXQ-141b/590a); SD-012 homeostatic; ARC-073 play competence-saturation drive pressure"
        - "DECISION the register forces: which axes are first-class (exploration / play / social / learning / grooming-rest in addition to depletion), and is each a scalar drive_level on its own homeostatic-style integrator or a derived/contextual signal?"
      last_updated: 2026-06-14
      completion_note: "Per thought_intake_2026-06-04_non_terminal_need_launch.md S2: nursery scaffolding + weaning arc already exist; the genuinely NEW framing is treating non-food needs as a register of first-class drive axes rather than one energy scalar. This is the precondition for arbitration (DRV-2) and for the orienting drive (DRV-4) to have a need to gate on. RECONCILED 2026-06-14 (plan reconcile -> done): the load-bearing architectural commitment is registered. SD-060 (claims.yaml; design_decision, candidate, substrate_conditional, v4, v3_pending) captures the drive-register framing verbatim -- title + functional_restatement name it as genuinely-NEW framing, 'each non-terminal need becomes a first-class drive axis carried as its own homeostatic-style integrator', explicitly 'the precondition for arbitration (DRV-2, MECH-394) and the orienting drive (DRV-4, MECH-395)'; depends_on [SD-012, MECH-111, ARC-073] wires the single-axis baseline plus the two scattered seeds the register unifies. MECH-111 (curiosity/novelty intrinsic seed) is registered and correctly cross-referenced as one of the unified seeds. No claims.yaml amendment needed (user-confirmed 2026-06-14). The open which-axes-first-class / scalar-integrator-vs-derived DECISION is correctly left in the readiness_gate as a V4 build-time decision, not a registration-completeness condition. Registration IS the deliverable for this phase-1 node; the V4 substrate build stays gated (substrate_conditional, DO NOT build in V3)."
    - id: "drives_motivation_v4:DRV-2"
      title: "Multidrive arbitration / orchestration policy (which drive wins when several are active)"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-394", "MECH-435", MECH-295]
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
      status: closed
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-394", "SD-060"]
      depends_on: ["drives_motivation_v4:DRV-1"]
      cross_plan_link: []
      readiness_gate:
        - "Project rule feedback_biology_before_formal_definitions: commission a biology lit-pull BEFORE registering the arbitration MECH (drive competition / hypothalamic drive hierarchy / opportunity-cost theories: Berridge incentive salience already in SD-012/MECH-295; need lateral-hypothalamus / dopamine tonic-vigour / Pezzulo 2014 exploratory-vs-homeostatic / Niv 2007 opportunity-cost-of-time)"
        - "L-non-terminal-needs: ethology of non-feeding drives (grooming, play, exploration) as homeostatically-regulated systems, not just deficit-reduction"
      last_updated: 2026-06-13
      completion_note: "GROUNDED 2026-06-13 via /lit-pull -> evidence/literature/targeted_review_drive_arbitration/ (5 literature_evidence/v1 entries). MECH-394 lit_conf 0->0.855, SD-060 lit_conf 0->0.755 (exp_conf stays 0; promotes nothing -- both substrate_conditional V4). Entries: Burnett et al. 2016 (Neuron, hunger-driven motivational state competition: contextual, satiation-graded suppression of rival drives -- the existence proof for MECH-394's soft-competitive orchestration AND SD-060's multi-axis register); Niv Daw Joel & Dayan 2007 (Psychopharmacology, tonic-DA opportunity-cost-of-time: the common-currency term arbitration needs); Pezzulo Rigoli & Friston 2015 (Prog Neurobiol, priors-as-drives / precision-weighted soft competition -- resolves the claim's loose 'Pezzulo 2014' citation; cross-ref ARC-073 exploratory-vs-homeostatic); McFarland & Sibly 1975 (Phil Trans R Soc B, behavioural final common path -- foundational ethology, source of REE's 'candidate'/'competitiveness' vocabulary, anchors the WTA pole MECH-394 argues against); Mu et al. 2020 (Nat Commun, grooming as behavioural-homeostatic de-arousal -- one worked non-feeding homeostatic integrator for SD-060). Biology-before-formal-definitions satisfied: MECH-394 (already registered candidate) and the DRV-2 policy it precedes are now grounded ahead of any V4 build. REGISTERED 2026-06-13 (was proposal-first; registered at user direction): MECH-435 -- a candidate partner sub-claim (component of MECH-394, substrate_conditional V4) that arbitration is priced in a common opportunity-cost-of-time currency (a global tonic vigour signal above per-axis benefit terms), motivated by Niv 2007 -- the currency MECH-394 currently leaves unspecified. Wired into MECH-394.depends_on + DRV-2 unblocks_claims; Niv 2007 entry now tags MECH-394 + MECH-435. Honest caveat carried into the record: Niv's signal sets vigour of a chosen action, and a global scalar with no cross-axis gradient cannot by itself carve WHICH drive wins (ties to the live candidate-differentiated-affect concern). Original grounding-debt note preserved: the arbitration policy (DRV-2) instantiates a formal competition mechanism; per the biology-before-formal-definitions rule it must be grounded before registration to avoid the SD-003 / SD-010 philosophy-right / mechanism-wrong failure mode."
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
**Generation:** v4 (forward roadmap; excluded from the V3 closure %) for DRV-1/2/3/5.
**DRV-4 (orienting) MOVED OUT 2026-08-13:** the node previously lived here as
DRV-4, RE-SCOPED 2026-08-07 to note it was V3 assembly-sequence work
mis-filed under a generation:v4 plan. That mis-filing was never actually
fixed (a plan's `generation` applies to every node in it -- there is no
node-level override in serve.py / generate_closure_snapshot.py /
check_closure_drift.py), so MECH-395 stayed excluded from V3 closure
tracking even after its own claims.yaml `implementation_phase` read v3. Per
/governance 2026-08-12 audit + user-directed disposition 2026-08-13
(session curiosity-orienting-closure-gap-27d495), DRV-4's node now lives at
`orienting_epistemic_deficit_v3:ORNT-1` in the new
`orienting_epistemic_deficit_v3_plan.md`, alongside MECH-482/483/Q-089
(which had no owning node anywhere) and MECH-489/SD-099 (also absent from
every plan despite SD-099 already being implemented). DRV-1/2/3/5 remain
genuinely V4 here (no live V3 thread motivates pulling them forward; user
confirmed 2026-08-13 -- "the other drives I am not sure about").
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
| 3 -- orienting drive | MOVED 2026-08-13 -> `orienting_epistemic_deficit_v3:ORNT-1` | SD-057/MECH-347/MECH-295 (NEW MECH) | V3 assembly-sequence, now tracked in a v3-generation plan | V3-EXQ-812 successor clears the candidate-proximity readiness precondition AND shows cue-to-action authority; then resume the orienting diagnostic |
| 4 -- launch profile | DRV-5 | scaffolded_sd054_onboarding (NEW criterion) | deferred / transfer-world | only when transfer-world work is scheduled |

---

## What this plan deliberately does NOT pull into V3

- **No new drive axes are added to ree-v3 now.** SD-012's single food/energy
  axis stays the only live homeostatic drive. The register (DRV-1) is a V4
  design decision; registering this roadmap changes no V3 behaviour.
- **The orienting drive IS now registered, AND now closure-tracked (updated
  2026-08-13):** MECH-395 (narrow, cue-triggered orienting; registered
  2026-06-10) and MECH-482/MECH-483/Q-089 (broader epistemic-deficit-driven
  orienting cluster; registered 2026-08-05) all exist in claims.yaml. What
  has NOT happened is a substrate build for any of them -- the V3-EXQ-640/640a
  diagnostics ran and did NOT discriminate for orienting; they routed to a
  shared E3 selection-authority ceiling instead. These four claims are now
  owned by nodes in `orienting_epistemic_deficit_v3_plan.md` (moved out of
  this plan 2026-08-13, see the frontmatter `Generation` note above) rather
  than by this plan -- do not re-register nodes for them here.
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
| evidence/planning/orienting_epistemic_deficit_v3_plan.md | new v3-generation sibling plan owning MECH-395/482/483/Q-089/MECH-489/SD-099 (moved out of DRV-4 here, 2026-08-13) |

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
- **2026-06-13** -- DRV-3 grounding node CLOSED. Biology-before-formal-definitions
  lit-pull complete (5 entries under
  evidence/literature/targeted_review_drive_arbitration/): Burnett 2016 (multidrive
  competition, contextual hierarchy), Niv 2007 (opportunity-cost-of-time common
  currency), Pezzulo/Rigoli/Friston 2015 (priors-as-drives, precision-weighted soft
  competition), McFarland & Sibly 1975 (behavioural final common path / candidate
  competition), Mu 2020 (grooming as behavioural-homeostatic de-arousal). MECH-394
  lit_conf 0->0.855, SD-060 lit_conf 0->0.755; exp_conf stays 0 (lit/exp decoupled),
  promotes nothing -- both remain substrate_conditional V4. DRV-2 (the arbitration
  policy MECH-394 instantiates) is now grounded ahead of registration/build. ONE
  proposal-first partner sub-claim surfaced to the user, NOT auto-registered: a
  common opportunity-cost-of-time currency for arbitration (global tonic vigour
  signal above per-axis benefit terms, motivated by Niv 2007), carrying the honest
  caveat that a gradient-free global scalar cannot alone carve which drive wins
  (links the candidate-differentiated-affect concern). No claims.yaml edits in the
  grounding pass (lit/exp decoupled; proposal-first).
- **2026-06-14** -- DRV-1 node RECONCILED open -> done (plan reconcile). The
  phase-1 load-bearing architectural commitment is registered: SD-060 (the
  non-terminal drive register) captures the genuinely-new drive-axes-as-
  first-class-register framing verbatim (title + functional_restatement +
  depends_on [SD-012, MECH-111, ARC-073] wiring the single-axis baseline and the
  two scattered seeds the register unifies), and MECH-111 (curiosity/novelty
  seed) is registered and cross-referenced as one of the unified seeds.
  Registration IS the deliverable for this node; the which-axes-first-class /
  scalar-integrator-vs-derived DECISION stays a V4 build-time choice in the
  readiness_gate, and the substrate build stays gated (substrate_conditional, DO
  NOT build in V3). No claims.yaml amendment needed (user-confirmed). Node +
  frontmatter last_updated -> 2026-06-14; inter-governance workset regenerated
  (DRV-1 no longer a ready plan-reconcile item).
- **2026-06-13** -- MECH-435 REGISTERED at user direction (the proposal-first
  partner surfaced above). Candidate, claim_type mechanism_hypothesis,
  epistemic_category substrate_conditional, implementation_phase v4, v3_pending:
  common opportunity-cost-of-time arbitration currency (global tonic vigour signal
  above the per-candidate MECH-295 score_bias), grounded by Niv 2007. Wired:
  MECH-435.depends_on=[SD-060, SD-012, MECH-295], related_claims=[MECH-394,
  MECH-359]; added to MECH-394.depends_on and to DRV-2 unblocks_claims; Niv 2007
  lit entry re-tagged MECH-394 + MECH-435 (MECH-435 lit_conf seeded from it,
  exp_conf 0 -> promotes nothing). Load-bearing caveat encoded in the claim:
  necessary-but-insufficient currency TERM, paired with a per-axis-differentiated
  benefit gradient (MECH-359). Falsification condition stated. promote/demote
  suppressed (substrate_conditional V4).
- **2026-08-05** -- MECH-482 (epistemic_deficit accumulator) and MECH-483
  (orient/survey behavioural regime) REGISTERED from the 2026-08-05
  "Epistemic Deficit and Orienting" thought intake (thought-digestion/-intake
  session). Both candidate, mechanism_hypothesis, epistemic_category
  substrate_conditional, implementation_phase v4, v3_pending: MECH-482 is a
  persistent target-bound model-inadequacy accumulator distinguished from
  MECH-314a/b/c (novelty/uncertainty/learning-progress) and MECH-313 (noise
  floor); MECH-483 is a third primitive behavioural regime (orient/survey,
  alongside approach/avoid) hypothesised to be gated by MECH-482, distinguished
  from MECH-395 (cue-triggered narrow orienting for a specific vector, vs.
  MECH-483's diffuse pre-cue survey). Both carry falsification conditions with
  explicit non-degeneracy preconditions; conservative reading stated in the
  intake -- extend the existing curiosity stream (MECH-314 family), do not add
  a wholly separate module. Also registered Q-089 (open_question): whether
  epistemic-deficit-driven orienting explains the observed cold-start
  competence split, framed by the intake as one hypothesis among several. Q-089
  wires depends_on=[MECH-457] as the conceptual match for the "some seeds enter
  a competent regime, others don't" framing, but flags a citation ambiguity:
  the intake's own cited runs (V3-EXQ-875a/882a) are tagged in
  pending_review.md to MECH-471/MECH-472, not MECH-457 -- recorded as
  related_claims rather than silently resolved. No experiment proposal minted
  (substrate not V3-tractable as stated); no claims.yaml promotion (digestion,
  not governance). DO NOT build in V3.
- **2026-08-07** (session `elegant-ishizaka-ddd4f6`, user-directed reclassification) --
  Traced the actual current status of the diagnostic thread DRV-4/MECH-395's gate
  named (V3-EXQ-640): it ran, plus a follow-on gain sweep (640a) and a July retest
  (V3-EXQ-812, 2026-07-24). None discriminated for orienting; all three routed to a
  shared E3 selection-authority / cue-authority ceiling (same shape as the
  MECH-314/320/341 modulatory-bias-drowning cluster; 812 failed on a
  candidate-pool-collapse readiness precondition, still open). DRV-4's
  `blocking_on`/`readiness_gate` text updated above to reflect this -- it had gone
  stale for two months, still describing 640 as a future diagnostic.
  Separately traced what MECH-482 (epistemic_deficit) actually needs --
  target-bound/per-candidate uncertainty -- against `substrate_queue.json`'s
  GAP-A entry (extend MECH-314b/314c to per-candidate treatment): same
  capability, already scoped, priority 1, unclaimed, its main blocker (a clamp
  saturation bug) cleared 2026-07-21. `substrate_queue.json` amended in this
  session to fix its own stale `ready_blocked_by` text and record this link.
  **Reclassification decision (user-directed):** MECH-395, MECH-482, MECH-483,
  and Q-089 should carry `implementation_phase: v3` / `version_relevance: v3`
  (not `v4`), because V3 is not a closed substrate being tested against a fixed
  spec -- it is still being assembled, and these claims are gated on identified,
  partially-cleared, IN-PROGRESS V3 assembly work (the selection-authority
  thread; the GAP-A per-candidate extension), not on a separate future
  generation. `v3_pending: true` and `DO NOT build YET` both stay -- the
  reclassification changes which roadmap these show up on and whether they
  count toward V3 closure tracking, not their buildability today. The
  claims.yaml edit itself is PENDING as of this note: `claims.yaml` was held by
  a concurrent active claim (session `cool-torvalds-a82359`, thought-digestion,
  claimed 2026-08-07T13:32:33Z) at write time, so the amendment was drafted and
  handed to the user rather than applied. See WORKSPACE_STATE.md Recent Work
  for the drafted diff and its landing status.
- **2026-08-13** (session `curiosity-orienting-closure-gap-27d495`,
  chip-20260813-curiosity-orienting-closure-map-gap, user-directed): the
  2026-08-07 claims.yaml amendment above DID land at some point (MECH-395
  now reads `implementation_phase: v3` in claims.yaml), but this plan's own
  `generation: v4` frontmatter was never updated to match, so DRV-4/MECH-395
  stayed excluded from V3 closure tracking for another 6 days -- a live
  plan/claims self-inconsistency, surfaced by /governance 2026-08-12
  (session sd-016-h3-algorithm-3370cd). Traced with the user: none of
  serve.py / generate_closure_snapshot.py / check_closure_drift.py support a
  node-level `generation` override (only plan-level), so flipping this
  whole plan's generation to v3 was rejected -- it would have incorrectly
  pulled DRV-1 (done)/DRV-2 (blocked)/DRV-3 (closed)/DRV-5 (deferred) into
  V3 tracking despite the plan's own text (and the user, explicitly) saying
  those four remain genuinely V4 ("I am not sure about" them). DRV-4's node
  MOVED to `orienting_epistemic_deficit_v3:ORNT-1` in a new v3-generation
  plan, `orienting_epistemic_deficit_v3_plan.md`, alongside MECH-482
  (epistemic_deficit accumulator) / MECH-483 (orient/survey regime) /
  Q-089 (cold-start-split question) -- all three previously prose-only
  here, with no owning node anywhere -- and MECH-489/SD-099
  (defensive-orienting), which were absent from every `*_plan.md` despite
  SD-099 already being implemented (2026-08-09) and MECH-489 already
  carrying real experimental evidence (V3-EXQ-910/910a). User's stated
  rationale for keeping the cluster together and pulling it into v3
  ownership: "I am very sure the information hunger and the three
  associated curiosity drive like systems are needed" for commitment to
  work properly, tying to the standing basal-ganglia-commitment research
  thread (see `project_bg_commitment_over_f_dominance_route` memory) --
  noted here for continuity; not acted on further in this session (out of
  this audit's scope). DRV-1/2/3/5 nodes and their content are otherwise
  UNCHANGED by this edit. No claims.yaml edits.
