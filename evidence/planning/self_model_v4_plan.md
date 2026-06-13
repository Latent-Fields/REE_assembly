---
closure_plan:
  id: self_model_v4
  generation: v4
  title: "Self-Model Integration (finish self-attribution; self-as-object cutover)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [ARC-081, MECH-214, MECH-215, SD-030, INV-064]
  sibling_plans: [object_representation_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no experiments yet, so nodes
    carry no owner_exq and the drift checker stays dormant against them. Each
    node's readiness_gate lists the V3-era prerequisites (claims/tracks) that
    must land before the V4 self-model step is honest to build. generation: v4
    keeps these nodes OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, and check_closure_drift.py are all
    generation-aware). This plan is the OBJ-3 sibling of object_representation_v4:
    that plan tracks self-as-object from the OBJECT-FILE side (z_self as a
    privileged ARC-080 slot); this plan tracks the SELF-MODEL side -- the
    DR-10..DR-14 integration audit, self-attribution completion, and the
    maturational sequencing that makes the cutover honest. A node graduates from
    roadmap to closure-tracked by gaining an owner_exq once its first V4
    experiment is queued.
  nodes:
    - id: "self_model_v4:SELF-1"
      title: "z_self promoted from body-state latent to a stateful self-model (DR-13 temporal depth)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-081]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-3"]
      readiness_gate:
        - "V3 BEGINNING present (no gate): SD-005 z_self/z_world split is implemented -- z_self exists today as a single-MLP + EMA body-state latent"
        - "DR-13 is the first cutover step: replace the single hidden layer + EMA with recurrence or E1 feedback so z_self carries a temporal self-model, not an instantaneous body snapshot"
        - "Without temporal depth there is no stateful subject for the later DR-10/DR-11/DR-12 self-object integration to attach to"
      last_updated: 2026-06-10
      completion_note: "DR-13 from v4_spec V4-2. This is the substrate floor for the whole plan: z_self must be a stateful self-model before it can be a privileged object-file slot (OBJ-3) or the subject of agentive prediction (MECH-215). No V3 substrate change; the EMA stays as the V3 self latent."
    - id: "self_model_v4:SELF-2"
      title: "Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [SD-030]
      depends_on: ["self_model_v4:SELF-1"]
      cross_plan_link: []
      blocking_on: "SD-030 (E2 self-forward-model) is V4-deferred because V3 has no clean z_self stream with its own forward model -- E2 currently operates on z_gamma (combined self/world). Gated on SELF-1 materialising z_self as a first-class latent with a forward model."
      readiness_gate:
        - "V3 BEGINNING present: self-attribution on the z_world causal-footprint stream runs (SD-031, V3-pending) and the comparator mechanism MECH-256 is owned; SD-003's counterfactual-E2 self-attribution was superseded by MECH-256 + SD-029 (the comparator survives the supersession)"
        - "SD-030 CUTOVER: residual_self = z_self_observed - E2_self(z_self_{t-1}, a_actual) -- the Blakemore-tickle / Shergill-force / Wolpert cerebellar-internal-model domain -- requires an E2_self forward model on the SELF-1 stateful z_self"
        - "Biology grounding is strongest for this stream (Blakemore 1998 tactile cancellation, Shergill 2003 force, Wolpert & Flanagan 2001 motor forward models); the lit anchors already exist in sd_030 doc"
      last_updated: 2026-06-10
      completion_note: "This is the user-named 'finish self-attribution' work. V3 has the world-stream comparator (SD-031) and the general mechanism (MECH-256); the missing piece is the motor-proprioceptive self-stream comparator (SD-030), which is blocked until z_self has its own forward model. Three-stream attribution (self/world/harm) is only complete once SD-030 lands."
    - id: "self_model_v4:SELF-3"
      title: "z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability"
      phase: 3
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-215, ARC-081]
      depends_on: ["self_model_v4:SELF-1"]
      cross_plan_link: ["object_representation_v4:OBJ-3"]
      readiness_gate:
        - "V3 LIMIT: E3.score_trajectory() currently evaluates entirely in z_world space -- there is no z_self term in viability"
        - "DR-10 cutover: score_trajectory must read z_self so capacity/affect/damage state gate which trajectories are viable for THIS agent"
        - "Implementation surface: E3.score_trajectory; depends on SELF-1 stateful z_self existing as the subject of the viability estimate"
      last_updated: 2026-06-10
      completion_note: "DR-10 from v4_spec V4-2. Partially V3-tractable per v4_spec but the cohort coheres around the V4 self-model. Unblocks the (1) prerequisite of MECH-215 (a stable z_self as the subject of viability planning) and is the E3-scoring half of the ARC-081 object-file cutover."
    - id: "self_model_v4:SELF-4"
      title: "E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability"
      phase: 3
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-215]
      depends_on: ["self_model_v4:SELF-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 LIMIT: E3 trusts E2 unconditionally; high E2 prediction error does not currently down-weight a trajectory's confidence"
        - "DR-12 cutover: wire E2 forward-PE -> E3 confidence so that low-confidence (poorly-modelled) regions discount their own viability estimates"
        - "v4_spec notes DR-12 is the most V3-tractable of the five (partly addressable in V3); it is sequenced here as the cheapest cutover step and a natural pilot"
      last_updated: 2026-06-10
      completion_note: "DR-12 from v4_spec V4-2. Together with DR-10 this is the (DR-10 + DR-12) pair that unblocks MECH-215 (self-model prerequisite for agentive prediction: the E2 self-transition accuracy half). The most landable DR; can be the first V4 experiment to gain an owner_exq."
    - id: "self_model_v4:SELF-5"
      title: "z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals"
      phase: 4
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-214]
      depends_on: ["self_model_v4:SELF-1", "self_model_v4:SELF-3"]
      cross_plan_link: ["goal_pipeline"]
      blocking_on: "z_goal currently lives entirely in z_world space (GoalState seeds from z_world_current). Self-state goals (energy restoration, pain avoidance) are unrepresentable until z_self is a stateful, scorable latent (SELF-1 + SELF-3)."
      readiness_gate:
        - "V3 WIRING AUDIT (MECH-214, 2026-04-07): z_goal lives purely in z_world; V3 grid world conflates location with reward, so z_world-only goals are adequate and the failure mode is structurally invisible"
        - "DR-11 cutover: a z_self-domain goal channel so a goal can name a self-state (restore energy, avoid pain) rather than only a world location"
        - "MECH-214 (goal referent must be E1-representable) is the claim this unblocks; the self-state goal channel is the E1-self-schema side of E1-representability"
      last_updated: 2026-06-10
      completion_note: "DR-11 from v4_spec V4-2. Cross-links goal_pipeline because z_goal is shared substrate. Gated on a scorable z_self (SELF-3) -- a self-state goal is meaningless if E3 cannot score viability against z_self. The addiction mapping (pursuit of a z_goal proxy without hedonic grounding) only becomes measurable once self-state and world-location goals dissociate."
    - id: "self_model_v4:SELF-6"
      title: "Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure"
      phase: 4
      status: blocked
      blocker_class: v3_substrate
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-214]
      depends_on: ["self_model_v4:SELF-5"]
      cross_plan_link: []
      blocking_on: "CausalGridWorldV2 conflates location with reward, so the MECH-214 addiction failure mode (wanting fires on an E1-unrepresented satisfaction state) is structurally invisible. Requires a new env where proxy content and hedonic content can come apart."
      readiness_gate:
        - "V3 LIMIT: the grid world makes proxy == hedonic by construction; you cannot show a goal pursued without its satisfaction state being reached"
        - "DR-14 cutover: an environment that dissociates proxy cue from hedonic outcome (the SD-022-style body-state extension generalised), so DR-11 self-state goals have a domain in which they can fail correctly"
        - "Gated on SELF-5: a proxy/hedonic split env is only meaningful once z_self-domain goals exist to be the things that decouple"
      last_updated: 2026-06-10
      completion_note: "DR-14 from v4_spec V4-2. This is the measurement substrate that makes MECH-214's central clinical prediction (anhedonia/incoherent-wanting as E1-self poverty, not pure dopaminergic disorder) experimentally surfaceable. Env work, not core-model work; sequenced last because it presupposes the DR-11 goal channel."
    - id: "self_model_v4:SELF-7"
      title: "Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar"
      phase: 5
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [INV-064]
      depends_on:
        - "self_model_v4:SELF-1"
        - "self_model_v4:SELF-3"
      cross_plan_link: ["object_representation_v4:OBJ-5"]
      blocking_on: "MECH-163 multi-step hippocampal planning (the shared V4-entry gate; V3-EXQ-495 queued) AND a stable self (SELF-1 + SELF-3). INV-064 asserts E1->E2->E3 maturation order; the self-object cutover must not run ahead of E1/E2 self-schema differentiation."
      readiness_gate:
        - "INV-064 is emergent on ARC-001/002/003/ARC-019 and carries pending_substrate_reconfirmation (lowest-status substrate is provisional ARC-019); reconfirm before citing as a sequencing authority"
        - "MECH-163 multi-step hippocampal planning PASS is the V3 full-completion gate that also gates the others-as-object pillar (object_representation_v4:OBJ-5 / DEV-NEED-021)"
        - "Sequencing rule: the self-object cutover (SELF-1..SELF-6) must be demonstrably stable before others-as-object work begins -- a stable self is a DEV-NEED-021 prerequisite for otherness inference"
      last_updated: 2026-06-10
      completion_note: "INV-064 is not a substrate step but a sequencing invariant: it pins the order self -> world -> others and forbids building the social pillar before the self is stable. This node is the honesty gate between this plan and the social roadmap; it depends on the shared MECH-163 V4-entry gate, not on new self-model code beyond SELF-1/SELF-3."
    - id: "self_model_v4:SELF-8"
      title: "Biology grounding completion (self-as-object body-ownership, agency/forward-model self, interoceptive self lit-pulls + completion-set harvest)"
      phase: 2
      status: open
      lit_pull_status: none
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-214, MECH-215, SD-030, INV-064, ARC-081]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-6"]
      readiness_gate:
        - "Shares object_representation_v4:OBJ-6 L4 self-as-object pull (Gallagher/Botvinick) -- this node adds the self-model-INTEGRATION-specific strands rather than duplicating it"
        - "L1 body-ownership (Botvinick & Cohen 1998 rubber-hand; Tsakiris 2010 neurocognitive model) + L2 sense-of-agency / efference-copy self (Blakemore & Frith; forward-model self-prediction) -- the direct anchors for SD-030 E2 self-forward-model and MECH-215"
        - "L3 interoceptive self (Craig 2009; Seth) for the MECH-214 wanting-on-an-E1-unrepresented-satisfaction-state failure mode; harvest the insula partner + TPJ self/other boundary as the cross-link to the V5 social tier"
      last_updated: 2026-06-13
      completion_note: "Self_model had NO grounding node; self-as-object integration imports body-ownership / agency / interoception constructs with no formal /lit-pull (project rule feedback_biology_before_formal_definitions). Cross-references OBJ-6 L4 to avoid duplication; tracks the integration-specific strands + completion-set harvest (insula interoceptive-self, TPJ self/other boundary). Off V3 closure path; promotes nothing."
---
# Self-Model Integration -- V4 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** finish self-attribution and sequence the self-as-object cutover --
turn z_self from a V3 body-state latent into a V4 stateful self-model that
(a) closes the per-stream attribution topology, (b) enters E3 viability
scoring, (c) carries self-state goals, and (d) is sequenced honestly behind
the maturational invariant so the social pillar cannot run ahead of a stable
self.

This is the **self-model side** of the ARC-081 self-as-object pillar. The
sibling plan `object_representation_v4` tracks the same pillar from the
OBJECT-FILE side (z_self promoted to a privileged ARC-080 token-keyed slot,
node OBJ-3). The two meet at the DR-10..DR-14 cutover: OBJ-3 supplies the
"it is an object-file slot" framing; this plan supplies the "here is the
working self-model the slot points at." It is a *forward roadmap*, not a
closure map: V4 has no experiments yet, so nodes carry no `owner_exq` and the
drift checker stays dormant. The value here is the **readiness gates** -- for
each DR step, exactly which V3-era prerequisites must land first.

---

## One-line framing

> The self already BEGINS in V3 -- z_self exists (SD-005), self-attribution
> runs on the world stream (SD-031 / MECH-256, after SD-003's supersession),
> action-space discovery is the MECH-277 + ARC-059 stage-1 + ARC-074
> babbling line. What is NOT done is the CUTOVER: z_self has no temporal
> depth, no E2_self forward model, no role in E3 viability, no self-state
> goal channel, and no env that can show a self-state goal failing. The five
> DR-10..DR-14 gaps ARE that cutover; INV-064 forbids running it ahead of a
> stable self.

---

## The cutover sequence (DR-10..DR-14 mapped to nodes)

| DR / gate | Node | Claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| DR-13 temporal depth | SELF-1 | ARC-081 | V4 (floor) | SD-005 z_self live; replace EMA with recurrence/E1 feedback |
| finish self-attribution | SELF-2 | SD-030 | V4 (blocked) | SD-031 world-stream + MECH-256 live; needs E2_self on z_self |
| DR-10 z_self in E3 scoring | SELF-3 | MECH-215, ARC-081 | V3-straddle / V4 | E3.score_trajectory is z_world-only today |
| DR-12 E2-PE -> E3 confidence | SELF-4 | MECH-215 | most V3-tractable | E3 trusts E2 unconditionally; cheapest cutover |
| DR-11 z_self-domain goals | SELF-5 | MECH-214 | V4 (blocked) | z_goal is z_world-only; needs scorable z_self |
| DR-14 proxy/hedonic env | SELF-6 | MECH-214 | V4 (blocked) | grid world conflates location with reward |
| INV-064 sequencing gate | SELF-7 | INV-064 | V4-entry gate | MECH-163 PASS + stable self; reconfirm emergent flag |

---

## What this plan deliberately does NOT pull into V3

- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour. z_self stays the SD-005 single-MLP + EMA
  body latent in V3; E3.score_trajectory stays z_world-only; z_goal stays in
  z_world. The first real cutover step (DR-13 / DR-12) is V4 and must not
  enter V3 closure.
- **SD-031 (world-stream self-attribution) stays a V3 item.** It is the
  V3-tractable comparator and is NOT pulled into this V4 plan as work --
  it is the live BEGINNING that SELF-2 builds the missing self-stream half
  onto. Only SD-030 (the z_self motor-proprioceptive stream) is V4.
- **The object-file-slot framing is OBJ-3's job, not this plan's.** This plan
  does not re-litigate "is the self an object?" (ARC-081 / OBJ-3 owns that);
  it builds the working self-model the slot will reference. No ARC-080 /
  object-file substrate is duplicated here.
- **No new claims.** Every node maps to an existing claim (ARC-081, SD-030,
  MECH-214, MECH-215, INV-064) or an existing DR audit item. This area is
  already fully reaped.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/v4_spec.md](../../docs/architecture/v4_spec.md) section V4-2 | DR-10..DR-14 self-model integration enumeration + claims-unblocked map |
| [docs/architecture/sd_030_e2_self_forward_model.md](../../docs/architecture/sd_030_e2_self_forward_model.md) | SD-030 E2 self-forward-model + Blakemore/Shergill/Wolpert lit anchors |
| [docs/architecture/arc_080_object_representation_primitive.md](../../docs/architecture/arc_080_object_representation_primitive.md) | ARC-081 self-as-object pillar (the object-file-slot side; sibling plan) |
| claims.yaml ARC-081 / MECH-214 / MECH-215 / SD-030 / INV-064 | scope claims (all `implementation_phase: v4` except INV-064 candidate) |
| claims.yaml SD-005 / MECH-277 / ARC-059 / ARC-074 / SD-031 / MECH-256 | the V3 BEGINNINGS (readiness, not nodes) |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap, sibling to
  `object_representation_v4` (OBJ-3 cross-link) and `goal_pipeline` (DR-11
  z_goal cross-link). Nodes seeded one-per-DR (SELF-1..SELF-6) plus SELF-7
  for the INV-064 sequencing gate and SELF-2 for the SD-030
  self-attribution-completion step. Readiness gates pinned per DR.
  `generation: v4` set so the V3 closure % is unaffected. No claims.yaml
  edits. Area assessed as fully reaped -- zero new claims proposed.
- **2026-06-10** -- Noted SD-003 (the original counterfactual-E2
  self-attribution DD) is `superseded_by: [MECH-256, SD-029]` since
  2026-04-18; the self-attribution mechanism continuity lives on in MECH-256,
  so SELF-2's readiness gate cites MECH-256/SD-031, not the superseded SD-003.
