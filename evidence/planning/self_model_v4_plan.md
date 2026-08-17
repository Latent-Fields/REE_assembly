---
closure_plan:
  id: self_model_v4
  generation: v4
  title: "Self-Model Integration (finish self-attribution; self-as-object cutover)"
  registered: 2026-06-10
  last_updated: 2026-08-10
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
      status: done
      ethical_metadata:
        welfare_relevance: high
        applicable_ethics_gates: [SENT-3, SENT-13]
        requires_welfare_review: false
        forbidden_combinations: [self_model_plus_inescapability]
        note: "Self-continuity ingredient; with valence + autobiographical memory + inescapability + replay it forms the prohibited Class-4 combination."
      severity: load-bearing
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
      unblocks_claims: [ARC-081]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-3"]
      readiness_gate:
        - "V3 BEGINNING present (no gate): SD-005 z_self/z_world split is implemented -- z_self exists today as a single-MLP + EMA body-state latent"
        - "DR-13 is the first cutover step: replace the single hidden layer + EMA with recurrence or E1 feedback so z_self carries a temporal self-model, not an instantaneous body snapshot"
        - "Without temporal depth there is no stateful subject for the later DR-10/DR-11/DR-12 self-object integration to attach to"
      last_updated: 2026-07-01
      build_2026_07_01: "SUBSTRATE BUILT 2026-07-01 (user-directed, to unblock SELF-3/DR-10 after the same-day IGW-165 reconcile). /implement-substrate landed the HYBRID DR-13 lever in ree-v3: (1) ree_core/latent/self_recurrence.py NEW SelfRecurrenceCell (GRUCell over z_self -- the light dedicated self-recurrence; explicit/inspectable/lesionable/perturbation-isolated: only z_self flows through it, a +5.0 perturbation of prev.z_self leaks 0.0 into z_world -- contract C5); (2) LatentStack.encode() REPLACES the z_self EMA step ONLY (z_world/beta/theta/delta untouched) with h=SelfRecurrenceCell(z_self_instant, prev.z_self) blended toward the E1 generative prediction of z_self, z_self=(1-c)*h+c*self_e1_anchor, c=LatentStackConfig.self_recurrence_e1_coupling (THE recorded residual tunable: 0=pure recurrence/Option A, 1=pure E1-feedback/Option B, 0.15 light default=HYBRID); (3) anchor = E1 predicted-next z_self cached at agent _e1_tick (side-effect-free) + threaded via sense() -- the volatility_signal precedent, v1 caller/agent-supplied per the SELF-4 scope pattern; (4) LatentState.self_recurrence_diag readout {active, state_departure, e1_coupling, anchor_present}. Master switch use_self_recurrence (default False -> module not instantiated + verbatim legacy EMA -> BIT-IDENTICAL OFF). Full suite 1336 passed / 4 pre-existing failures (confirmed identical on the clean tree via git stash) + 11 new contracts tests/contracts/test_dr13_self_recurrence.py. generation:v4 -- off the V3 closure %. PROMOTES NOTHING (ARC-081 gets an implementation_note only; stays candidate/v4/v3_pending). Design doc docs/architecture/dr13_self_recurrence_temporal_depth.md; ree-v3/CLAUDE.md SD-implemented entry. VALIDATED: owner_exq=V4-EXQ-002 (DR-13 self-recurrence substrate-readiness falsifier; diagnostic, PROMOTES NOTHING) queued ree-v3 main 4c24214 + a cloud runner claimed and ran it same session -> PASS (run v4_exq_002_dr13_self_recurrence_falsifier_20260701T065002Z_v4, on origin/master; label dr13_self_recurrence_delivers_stateful_subject; full 3-seed: min_state_departure 1.15 >> floor [recurrence LIVE], carries_history 3/3, perturbation-isolated 3/3 [0.0 z_world leak], E1-anchor blend live 3/3; C1/C2/C3 all pass). Secondary/context (NOT a gate): untrained GRU raw history-retention 0.168 vs fixed-alpha EMA 0.219 -- trained superiority over the EMA is the DR-10 consumer question, as designed. The DR-13 self subject is substrate-VALIDATED. NOTE: the PASS manifest is a fresh pending_review item for the next /governance to formally mark reviewed (diagnostic, claim_ids=[], scores no claim). This build CLEARS SELF-3's blocker (SELF-3 flipped blocked->open same day)."
      completion_note: "DR-13 from v4_spec V4-2. This is the substrate floor for the whole plan: z_self must be a stateful self-model before it can be a privileged object-file slot (OBJ-3) or the subject of agentive prediction (MECH-215). MECHANISM RESOLVED 2026-06-14 (interactive IGW design-fork session): HYBRID -- z_self gains temporal depth via a light DEDICATED self-recurrence REGULARISED by E1 generative feedback (both motifs committed, not one). The recurrence supplies the stability-isolated, lesionable subject DR-10/11/12 + INV-064 attach to; the E1-feedback regulariser keeps it consistent with the E-stream generative account (SD-030/DR-12 stay E-stream-native). Residual sub-question = the regularisation-coupling strength (light = preserves stability-isolation; strong = collapses toward pure E1-feedback). Decision recorded on ARC-081 notes. SUBSTRATE NOW BUILT 2026-07-01 (see build_2026_07_01) -- the design decision of 2026-06-14 is now realised in ree-v3 as a no-op-default lever; PROMOTES NOTHING (ARC-081 stays candidate/v4/substrate_coherence). Validation = the DR-13 falsifier queued via /queue-experiment."
    - id: "self_model_v4:SELF-2"
      title: "Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)"
      status: blocked
      blocker_class: sibling_node
      severity: load-bearing
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
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
      status: in_progress
      severity: load-bearing
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
      unblocks_claims: [MECH-215, ARC-081]
      depends_on: ["self_model_v4:SELF-1"]
      cross_plan_link: ["object_representation_v4:OBJ-3"]
      build_2026_07_01: "SUBSTRATE BUILT 2026-07-01 (user-approved graduation via AskUserQuestion, same session as the SELF-1 DR-13 build that unblocked it; caller-supplied v1). /implement-substrate landed the DR-10 lever in ree-v3, mirroring the DR-12/SELF-4 pattern on the SAME e3_selector machinery: e3_selector.py _self_viability_penalty helper + score_trajectory(self_viability=...) monotone penalty block + select(self_viability_per_candidate=[K]) per-candidate threading + 4 diagnostics (self_viability_active/weight/range/penalty_range); E3Config 4 no-op fields (use_self_viability_weighting default False, self_viability_weight 0.0, mode 'linear', scale 1.0) + REEConfig.from_dims passthrough; agent _injected_self_viability + set_injected_self_viability() seam + version-layering-guarded select_action passthrough. A per-candidate self-viability COST (from the DR-13 stateful z_self: capacity/affect/damage) discounts trajectories less viable for the current bodily state; no learned params; master switch default False -> bit-identical OFF. Full suite 1344 passed / 4 pre-existing failures (clean-tree-confirmed) + 8 new contracts tests/contracts/test_dr10_z_self_viability.py (OFF/weight-0/no-signal bit-identical; differential flips selection; uniform argmin-invariant; linear==cost + saturating bounded-monotone + negative clamped). generation:v4, PROMOTES NOTHING (MECH-215/ARC-081 stay candidate/v4). v1 self-viability source = caller/agent-supplied (user-chosen); ecological z_self-derived auto-source (allostatic z_self-deviation x per-candidate demand, or a learned z_self->viability head needing phased training + SELF-2 per-candidate self-transition) is the documented follow-on. Design doc docs/architecture/dr10_z_self_in_e3_viability.md; ree-v3/CLAUDE.md SD-implemented entry. owner_exq=V4-EXQ-003 assigned at queue time. status open->in_progress until the V4-EXQ-003 falsifier is reviewed."
      resume_condition: "AWAITING V4-EXQ-003 RUN + REVIEW (DR-10 pilot). On PASS (a decisive per-candidate self-viability changes selection vs OFF): the z_self-in-E3 viability wiring is live; the ecological z_self-derived auto-source is the next build, and DR-10 + DR-12 (SELF-4) together are the MECH-215 unblock (governance-scored experiments then remain). On inert-wiring (FALSIFIER fired under met preconditions): /failure-autopsy. On substrate_not_ready_requeue: re-queue at adequate power. Status stays in_progress until that review."
      unblocked_2026_07_01: "SELF-1 DR-13 substrate BUILT 2026-07-01 (a materialised stateful z_self via the light self-recurrence + E1-feedback anchor -- see self_model_v4:SELF-1 build_2026_07_01). This CLEARS the blocker that the 2026-07-01 IGW-165 morning reconcile named (SELF-3 was blocked->open here): the stateful z_self that E3.score_trajectory must read as the subject of viability now EXISTS in ree-v3 (behind LatentStackConfig.use_self_recurrence). SELF-3 is now buildable: /implement-substrate the DR-10 z_self viability term on top of the stateful z_self (enable use_self_recurrence + add a z_self read to score_trajectory so capacity/affect/damage STATE gates viability), then /queue-experiment the DR-10 falsifier. owner_exq assigned at queue time. Left `open` (ready to build), NOT auto-graduated -- a V4 build graduation is a user decision per the SELF-4 graduation_decision precedent."
      readiness_gate:
        - "V3 LIMIT: E3.score_trajectory() currently evaluates entirely in z_world space -- there is no z_self term in viability"
        - "DR-10 cutover: score_trajectory must read z_self so capacity/affect/damage state gate which trajectories are viable for THIS agent"
        - "Implementation surface: E3.score_trajectory; depends on SELF-1 stateful z_self existing as the subject of the viability estimate"
      last_updated: 2026-07-01
      completion_note: "DR-10 from v4_spec V4-2. Partially V3-tractable per v4_spec but the cohort coheres around the V4 self-model. Unblocks the (1) prerequisite of MECH-215 (a stable z_self as the subject of viability planning) and is the E3-scoring half of the ARC-081 object-file cutover. STATUS RECONCILE 2026-07-01 (IGW-20260701-165, plan lane): flipped status open -> blocked (blocker_class: sibling_node). Verified still-true against source: e3_selector.score_trajectory() F/M/goal scorers operate entirely over z_world (SD-005) -- there is no z_self term in viability (the SELF-4/DR-12 build added a PE-magnitude confidence weight, not a z_self term), so DR-10 is genuinely unbuilt. The node read as actionable-open because its sole depends_on (SELF-1) flipped done 2026-06-14 and drift/workset tooling saw a satisfied dependency (SELF-5/SELF-7 were surfacing `Blocked by: SELF-3 [open]`) -- but SELF-1 `done` is DESIGN-resolved only (the EMA stays the V3 latent; BUILD is the V4 DR-13 cutover, unqueued, no owner_exq). SELF-3 needs that materialised stateful z_self, so the honest status is blocked on the SELF-1 substrate build, matching SELF-5/SELF-7 and SELF-4's 2026-06-16 note. PROMOTES NOTHING; queues nothing; no graduation (a V4 build graduation needs user adjudication per the SELF-4 graduation_decision precedent). No claims.yaml edit; MECH-215/ARC-081 stay candidate/v4. UNBLOCKED SAME DAY 2026-07-01 (user directed the SELF-1 DR-13 substrate be built): SELF-1 substrate landed in ree-v3, so SELF-3 flipped blocked->open -- the stateful z_self subject now exists (see unblocked_2026_07_01). SELF-3 is now the buildable DR-10 step on top of it."
    - id: "self_model_v4:SELF-4"
      title: "E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability"
      status: in_progress
      severity: medium
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
      unblocks_claims: [MECH-215]
      depends_on: ["self_model_v4:SELF-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 LIMIT: E3 trusts E2 unconditionally; high E2 prediction error does not currently down-weight a trajectory's confidence"
        - "DR-12 cutover: wire E2 forward-PE -> E3 confidence so that low-confidence (poorly-modelled) regions discount their own viability estimates"
        - "v4_spec notes DR-12 is the most V3-tractable of the five (partly addressable in V3); it is sequenced here as the cheapest cutover step and a natural pilot"
      last_updated: 2026-06-17
      resume_condition: "AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that scores against MECH-215. On dr12_wiring_inert (FALSIFIER fired under met preconditions): DR-12 buys nothing -> /failure-autopsy. On substrate_not_ready_requeue: re-queue at adequate power. Status stays in_progress until that review."
      build_2026_06_17: "BUILT (first-ever V4 substrate build; user-approved graduation_decision_2026_06_16). (1) /implement-substrate landed the no-op-default E2-forward-PE -> E3 confidence down-weight lever in ree-v3 ree_core/predictors/e3_selector.py score_trajectory() (use_pe_confidence_weighting / pe_confidence_weight / pe_confidence_mode + select(e2_forward_pe_per_candidate=[K]) per-candidate threading + diagnostics), E3Config + from_dims, agent set_injected_e2_forward_pe seam. Bit-identical OFF; 8/8 DR-12 contracts + full suite 1059 passed (1 pre-existing control_vector C4 flake). Landed ree-v3/main f5eba3b + 394ccf4 (config.py+agent.py swept intact into concurrent 42895f6, also on origin). Design doc docs/architecture/dr12_pe_conditioned_e3_confidence.md (swept into 9216447c2f). PROMOTES NOTHING -- MECH-215 untouched (candidate/v4); claims.yaml not modified. (2) /queue-experiment landed V4-EXQ-001 (DR-12 pilot, ree-v3/main 394ccf4; coordinator-DB confirmation pending) -- controlled caller-supplied-PE wiring falsifier, 3-arm OFF/DIFFERENTIAL/UNIFORM, smoke 3/3 seeds PASS. PRECEDENTS SET (first V4 experiment): architecture_epoch='ree_self_model_v1' (per v4_spec.md:267, parallel to V3 ree_hybrid_guardrails_v1; per-V4-track epoch like the ree_multi_agent_v1 example); run_id suffix '_v4'; V4-EXQ-NNN queue namespace (validate_queue.py queue_id pattern widened V3-EXQ -> V<gen>-EXQ). owner_exq=V4-EXQ-001 assigned HERE (at queue time, not before). VERIFIED generation-aware: check_closure_drift.py:497 skips non-v3 plans (so this owned generation:v4 node is NOT drift-flagged), and generate_closure_snapshot.py:260-263 + serve.py read_closure segment v4 out of the V3 overall_* -- a generation:v4 node carrying an owner_exq does NOT pollute the V3 closure %. v1 source is caller-supplied (controlled probe); ecological region-PE auto-source is the documented follow-on."
      completion_note: "DR-12 from v4_spec V4-2. Together with DR-10 this is the (DR-10 + DR-12) pair that unblocks MECH-215 (self-model prerequisite for agentive prediction: the E2 self-transition accuracy half). The most landable DR; can be the first V4 experiment to gain an owner_exq. READINESS NOTE 2026-06-16 (V4-roadmap tractability audit): this node's gate is now SATISFIED. Its only depends_on (SELF-1) flipped open->done 2026-06-14, and the DR-12 cutover keys off E2 forward-PE magnitude (present in V3 today on the z_gamma forward model), NOT off a materialised stateful z_self -- so unlike SELF-3/SELF-5 it does not wait on the SELF-1 substrate build. This is the buildable-now graduation candidate; user adjudication needed to assign an owner_exq (does NOT graduate automatically). Annotation only -- no owner_exq added, no work scheduled."
      graduation_decision_2026_06_16: "GRADUATION APPROVED (user, 2026-06-16 V4 tractability pass) -- SELF-4 is the first V4 node cleared to build. Build path (owner_exq assigned WITH the experiment, not before, to keep check_closure_drift.py dormant against this generation:v4 node until a real run exists): (1) /implement-substrate -- add a no-op-default confidence-by-PE lever in ree-v3 e3_selector.score_trajectory() that down-weights a trajectory's viability/confidence as a monotone function of E2 FORWARD-PE magnitude in that trajectory's region (E2 forward-PE is already produced on the z_gamma forward model; E3 already consumes E1-novelty + running-variance PE, so this is a new lever on existing machinery, bit-identical OFF). (2) /queue-experiment -- DR-12 pilot, architecture_epoch per v4_spec.md:267 (own V4 epoch parallel to ree_hybrid_guardrails_v1). FALSIFIER: if PE-conditioned confidence weighting does not change trajectory selection in high-PE (poorly-modelled) regions vs the unconditional-trust baseline, DR-12 buys nothing and the wiring is inert. unblocks MECH-215 (E2 self-transition-accuracy half). Cheapest possible V3->V4 cutover; proves the cutover pattern for the rest of the roadmap. NOT YET BUILT -- this records the decision; the implement-substrate+queue chain is the next step."
    - id: "self_model_v4:SELF-5"
      title: "z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals"
      status: blocked
      blocker_class: sibling_node
      severity: high
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
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
      status: blocked
      ethical_metadata:
        welfare_relevance: hard_review
        applicable_ethics_gates: [SENT-2, SENT-8, SENT-10, SENT-13]
        requires_welfare_review: true
        forbidden_combinations: [negative_valence_without_relief]
        note: "Proxy/hedonic dissociation deliberately surfaces a wanting-without-satisfaction distress-like state; needs relief pathway + boundedness (no valley without a bridge)."
      blocker_class: v3_substrate
      severity: high
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
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
      status: blocked
      ethical_metadata:
        welfare_relevance: low
        applicable_ethics_gates: [SENT-13]
        requires_welfare_review: false
        note: "Maturational-sequence honesty gate IS a SENT-13 assembly-routing instance: self-stability must precede the social/other pillar."
      blocker_class: sibling_node
      severity: high
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
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
      status: done
      lit_pull_status: done
      severity: medium
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
      unblocks_claims: [MECH-214, MECH-215, SD-030, INV-064, ARC-081]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-6"]
      readiness_gate:
        - "Shares object_representation_v4:OBJ-6 L4 self-as-object pull (Gallagher/Botvinick) -- this node adds the self-model-INTEGRATION-specific strands rather than duplicating it"
        - "L1 body-ownership (Botvinick & Cohen 1998 rubber-hand; Tsakiris 2010 neurocognitive model) + L2 sense-of-agency / efference-copy self (Blakemore & Frith; forward-model self-prediction) -- the direct anchors for SD-030 E2 self-forward-model and MECH-215"
        - "L3 interoceptive self (Craig 2009; Seth) for the MECH-214 wanting-on-an-E1-unrepresented-satisfaction-state failure mode; harvest the insula partner + TPJ self/other boundary as the cross-link to the V5 social tier"
      last_updated: 2026-06-14
      completion_note: "Self_model had NO grounding node; self-as-object integration imports body-ownership / agency / interoception constructs with no formal /lit-pull (project rule feedback_biology_before_formal_definitions). Cross-references OBJ-6 L4 to avoid duplication; tracks the integration-specific strands + completion-set harvest (insula interoceptive-self, TPJ self/other boundary). Off V3 closure path; promotes nothing. LIT-PULL DONE 2026-06-13 (targeted_review_self_model_integration, 6 entries): L1 body-ownership = Botvinick & Cohen 1998 (rubber-hand, ARC-081/SD-030, 0.61) + Tsakiris 2010 (neurocognitive model, ARC-081/SD-030/MECH-215/INV-064, 0.66 -- harvests right-TPJ self/other + right-posterior-insula ownership partners); L2 sense-of-agency/efference-copy = Blakemore/Wolpert/Frith 2002 (comparator model, SD-030/MECH-215, 0.70 -- strongest mapping) + Frith/Blakemore/Wolpert 2000 (parietal predicted-state vs prefrontal intention dissociation, SD-030/MECH-215, 0.68); L3 interoceptive self = Craig 2009 (AIC re-represents interoception, MECH-214/MECH-215, 0.60 -- anterior-insula partner) + Seth 2013 (interoceptive inference = MECH-214 satisfaction-referent-as-modelled-quantity, MECH-214/MECH-215/INV-064, 0.64). lit_conf raised SD-030 0.831 / MECH-215 0.828 / INV-064 0.725 / ARC-081 0.718 / MECH-214 0.71; ALL exp_conf 0.0, plausible_unproven -- PROMOTES NOTHING. Did NOT duplicate OBJ-6 L4 self-as-object (Gallagher/Botvinick object-file) -- that remains OBJ-6's tracking. COMPLETION-SET PARTNERS surfaced proposal-first (NOT auto-registered): (a) insula as the interoceptive-self locus -- two independent strands converge (Tsakiris right-posterior-insula ownership + Craig AIC interoceptive awareness); (b) right-TPJ self/other boundary as the V5 social-tier cross-link; (c) candidate design note that the self-model is ONE predictive-comparator form over TWO streams (motor-self SD-030 + interoceptive-self MECH-214), per Seth's unification. See decision log 2026-06-13. STATUS RECONCILE 2026-06-14: the biology /lit-pull deliverable was confirmed already landed (6 entries on disk under targeted_review_self_model_integration, lit_conf attached to all 5 scope claims, present in evidence/literature/INDEX.md); only the node status lagged. Flipped status open->done as a reconcile (lit_pull_status was already done). NO claims.yaml edit and NO lit-pull re-run -- re-running would duplicate the existing directory, which the skill forbids. exp_conf stays 0.0 on every scope claim; PROMOTES NOTHING."
    - id: "self_model_v4:SELF-9"
      title: "Own-future-option uncertainty: does REE need an explicit self-model of its OWN future option-space (second-order uncertainty over its developmental/decision branches) to avoid premature irreversible commitment, or do the object-level MECH-454 option-value cost + the existing de-commit/ghost-trace machinery suffice?"
      status: assembling
      lit_pull_status: pending
      severity: low
      live:
        as_of: "2026-07-12"
        from: "failure_autopsy_V3-EXQ-740a_2026-07-12"
        verdict: "non_contributory/measurement_degeneracy"
        next: "routing=claim-synthesis"
        brake: "not_fired"
        needs_review: false
      join:
        bears_on: []
        scope_claims: ["ARC-081", "MECH-214", "MECH-215", "SD-030", "INV-064"]
      unblocks_claims: []
      depends_on: []
      cross_plan_link: []
      assembly_status: queued
      readiness_gate:
        - "what_would_answer: build MECH-454 WITHOUT a self-future-model and test in a setting where the load-bearing uncertainty is about REE's OWN future capability/branch (not the world's). If MECH-454 + de-commit (MECH-090/091/342, SD-034, ARC-108-JOB-2) + ghost-trace (MECH-292/SD-039) ALONE prevent premature foreclosure -> the explicit self-future-model is UNNECESSARY (close this node). If REE still forecloses because it cannot represent uncertainty about its OWN future options -> the explicit V4 self-model is REQUIRED (route to the self-model build)."
        - "NON-DEGENERACY: the decisive uncertainty must genuinely be about the SELF's future option-set, not re-expressible as object/world uncertainty MECH-454 already handles -- else the question is vacuous (MECH-454 subsumes it)."
      last_updated: 2026-08-10
      governance_2026_08_10: "Dangling-link fix (/governance cycle queue-depth-low-ops-aac785, check_closure_links.py; frontmatter only, no other change). depends_on: [MECH-454] pointed at a claims.yaml claim id, not a closure-map node -- `depends_on` is scoped to node/plan references and no such node exists, so it read as dangling. MECH-454's relationship to this node is already fully documented in the title, readiness_gate and completion_note below; depends_on cleared to [] (this node has no actual closure-map blocker -- status stays assembling)."
      completion_note: "Folded in 2026-06-24 from a /thought-digestion pass (user disposition: fold the meta-level into this plan rather than mint a standalone claim). Origin = a meta-discussion of a temporal-reasoning failure (collapsing an unknown future distribution into a confident point and prematurely foreclosing a cheap reusable option); the OBJECT-LEVEL fix is registered as MECH-454 (candidate / substrate_conditional / v3), this node tracks the V4 META-LEVEL leg (REE reasoning about the unknowability of its OWN future). Distinct from SELF-3 / SELF-4 (DR-10 z_self-in-E3 / DR-12 E2-PE confidence -- object-level self-state in scoring); this is SECOND-ORDER uncertainty over the self's FUTURE option-space. Lit cluster to anchor when this node activates (the MECH-454 lit-pull is queued first; this node's prospective-cognition strands are deferred): constructive episodic simulation (Schacter & Addis; Hassabis & Maguire; Buckner & Carroll) + OFC counterfactual / foregone-option coding (Boorman; Kolling). OFF the V3 closure %; PROMOTES NOTHING."
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
- **2026-06-13** -- SELF-8 biology-grounding /lit-pull executed
  (`evidence/literature/targeted_review_self_model_integration`, 6 entries).
  L1 body-ownership (Botvinick & Cohen 1998; Tsakiris 2010), L2
  sense-of-agency/efference-copy (Blakemore/Wolpert/Frith 2002;
  Frith/Blakemore/Wolpert 2000), L3 interoceptive self (Craig 2009; Seth 2013).
  lit_conf raised on all five scope claims (SD-030 0.831, MECH-215 0.828,
  INV-064 0.725, ARC-081 0.718, MECH-214 0.71); **exp_conf unchanged at 0.0 on
  every claim -- `plausible_unproven`, promotes nothing.** Deliberately did
  NOT duplicate `object_representation_v4:OBJ-6` L4 self-as-object
  (Gallagher/Botvinick object-file framing) -- that grounding remains OBJ-6's
  to track; this node added only the integration-specific strands. lit_pull_status
  none -> done. **Completion-set partners surfaced PROPOSAL-FIRST (not
  registered)** -- to be adjudicated by the user before any claims.yaml edit:
  1. *Insula as the interoceptive-self locus.* Two independent strands of the
     pull converge on insular cortex -- Tsakiris's right posterior insula
     (subjective body-ownership) and Craig's anterior insula (interoceptive
     awareness / the basis of feelings). Candidate: a MECH-214 grounding note
     naming the interoceptive self-channel's biological anchor, or a small
     interoceptive-self-channel substrate item. NOT a new INV.
  2. *Right-TPJ self/other boundary as the V5 social-tier cross-link.*
     Tsakiris's incorporeability test (right TPJ) is the seat of the
     self/other distinction the eventual social pillar (ARC-082 others-as-object
     / DEV-NEED-021) will need. Candidate: a cross-plan link note from this
     plan / object_representation_v4:OBJ-5 to a future V5 social grounding node;
     INV-064's self-before-others sequencing already gates it.
  3. *One comparator, two streams (design note).* Seth 2013 unifies the motor-self
     (SD-030 predicted-vs-observed self-state) and the interoceptive-self
     (MECH-214 satisfaction-state inference) under one predictive-comparator
     form. Candidate: a design note (not a claim) that the V4 self-model should
     instantiate a single comparator architecture over both streams rather than
     two unrelated subsystems -- a cleaner, more biologically defensible SD-030
     + MECH-214 build order. Falsifiable revert: if the two streams need
     materially different comparator dynamics, split them.
- **2026-06-14** -- SELF-1 (z_self -> stateful self-model, DR-13) MECHANISM
  RESOLVED in an interactive IGW design-fork session. ARC-081 already commits the
  stateful self-OBJECT cutover, so the *whether* was settled; SELF-1 forced only
  the mechanism of temporal depth, which ARC-081 / v4_spec V4-2 left open
  ("recurrence OR E1 feedback"). **DECISION: HYBRID** -- z_self gains a light
  DEDICATED self-recurrence whose dynamics are REGULARISED by E1 generative
  feedback, committing both motifs. The recurrence supplies the explicit,
  lesionable, perturbation-isolated subject that DR-10/11/12 integration and the
  INV-064 maturational-stability gate attach to (a free-running shared E1 latent
  cannot be stability-isolated for the self); the E1-feedback regulariser keeps it
  consistent with the E-stream generative account so it does not become a parallel
  self-model divorced from the world-model -- SD-030 (E2_self, SELF-2) and DR-12
  (E2-PE -> E3) stay E-stream-native and wire onto the regularised self-latent.
  Honest cost: more machinery than either pure option, and the
  regularisation-coupling strength becomes a tunable (light coupling preserves the
  stability-isolation benefit; strong coupling collapses toward pure E1-feedback
  Option B) -- that strength is the residual sub-question, not re-litigated here.
  Recorded on ARC-081 `notes`. SELF-1 flipped open->done; node + frontmatter
  last_updated 2026-06-14. **DESIGN decision only -- NO V3 substrate change (the
  single-MLP + EMA stays the V3 self latent); PROMOTES NOTHING** (ARC-081 stays
  candidate / architectural_commitment (substrate_coherence) / v4 / v3_pending).
- **2026-06-14** -- SELF-8 STATUS RECONCILE (separate IGW session from the SELF-1
  fork above). The biology /lit-pull deliverable was confirmed **already landed on
  2026-06-13** (6 entries on disk under
  `evidence/literature/targeted_review_self_model_integration`; lit_conf attached to
  all five scope claims SD-030 0.831 / MECH-215 0.828 / INV-064 0.725 / ARC-081
  0.717 / MECH-214 0.71; present in `evidence/literature/INDEX.md`); only the node
  `status` lagged at `open` while `lit_pull_status` was already `done`. Flipped
  SELF-8 `status: open -> done` as a pure reconcile + bumped node `last_updated`.
  **Did NOT re-run /lit-pull** -- the existing directory already grounds the L1
  body-ownership / L2 agency-efference-copy / L3 interoceptive-self strands, and the
  skill forbids a second directory for a claim that already has one. **NO claims.yaml
  edit; exp_conf stays 0.0 on every scope claim; PROMOTES NOTHING.** The three
  completion-set partners surfaced 2026-06-13 (insula interoceptive-self locus;
  right-TPJ self/other boundary as the V5 cross-link; one-comparator-two-streams
  design note) remain PROPOSAL-FIRST, unadjudicated -- not registered by this
  reconcile.
- **2026-06-17** -- SELF-4 (DR-12) BUILT -- the FIRST-EVER V4 substrate build,
  executing the user-approved `graduation_decision_2026_06_16`. (1) `/implement-substrate`
  landed the no-op-default E2-forward-PE -> E3 confidence down-weight lever in
  `ree-v3/ree_core/predictors/e3_selector.py` `score_trajectory()` (per-candidate
  threading via `select(e2_forward_pe_per_candidate=...)`; bit-identical OFF; 8 DR-12
  contracts + full suite 1059 passed). (2) `/queue-experiment` landed **V4-EXQ-001**
  (DR-12 pilot; controlled caller-supplied-PE wiring falsifier; smoke 3/3 seeds PASS).
  SELF-4 `status: open -> in_progress`, `owner_exq: null -> V4-EXQ-001` (assigned at
  queue time, per the build-path rule). **PRECEDENTS for the V4 generation:**
  `architecture_epoch = ree_self_model_v1` (parallel to V3's `ree_hybrid_guardrails_v1`;
  per-V4-track epoch like v4_spec's `ree_multi_agent_v1` example); `run_id` suffix
  `_v4`; `V4-EXQ-NNN` queue namespace (`validate_queue.py` pattern widened
  `V3-EXQ` -> `V<gen>-EXQ`). **VERIFIED the generation-aware consumers keep V3 clean**
  with an owned generation:v4 node: `check_closure_drift.py:497` skips non-`v3` plans
  (no false drift flag); `generate_closure_snapshot.py:260-263` + `serve.py read_closure`
  segment v4 out of `overall_*` (no V3 closure-% pollution). **PROMOTES NOTHING in V3** --
  MECH-215 stays candidate/v4; no claims.yaml edit. v1 PE source is caller-supplied
  (controlled probe); the ecological region-PE auto-source is the documented follow-on.
  Substrate doc: `docs/architecture/dr12_pe_conditioned_e3_confidence.md`.
- **2026-07-01** -- SELF-3 (DR-10 z_self-in-E3 viability) STATUS RECONCILE
  (IGW-20260701-165, plan lane). SELF-3 was `status: open` and surfacing in the
  inter-governance workset as a top-tier actionable item (`Plan gap open on
  self_model_v4`), with SELF-5/SELF-7 both showing `Blocked by: SELF-3 [open]`.
  That was drift: SELF-3's sole `depends_on` (SELF-1) flipped `done` on
  2026-06-14, so tooling read the dependency as satisfied -- but SELF-1 `done`
  is a **DESIGN** resolution only (HYBRID recurrence + E1 regulariser mechanism
  chosen; the single-MLP + EMA stays the V3 self latent; the DR-13 substrate
  BUILD is unqueued, no `owner_exq`). Verified still-true against source that
  DR-10 is genuinely unbuilt: `e3_selector.score_trajectory()` F/M/goal scorers
  operate entirely over `z_world` (SD-005); the SELF-4/DR-12 build added a
  PE-magnitude confidence weight, **not** a `z_self` viability term. SELF-3
  needs the materialised stateful z_self as the subject of the viability
  estimate (its readiness-gate bullet 3 + completion_note; MECH-215 wants a
  *stable* z_self), which is exactly the SELF-1 substrate build that SELF-4's
  2026-06-16 readiness note names (`unlike SELF-3/SELF-5, [SELF-4] does not wait
  on the SELF-1 substrate build`). **Flipped SELF-3 `status: open -> blocked`**,
  added `blocker_class: sibling_node` + a `blocking_on` field, bumped node +
  frontmatter `last_updated` -> 2026-07-01. Now consistent with SELF-5/SELF-7
  (same real blocker: `stateful, scorable latent = SELF-1 + SELF-3`); on the
  next workset regen SELF-5/SELF-7 will read `Blocked by: SELF-3 [blocked]`.
  A shallow EMA-based z_self term is `partially V3-tractable` per v4_spec but
  scores against an instantaneous body snapshot, not the capacity/affect/damage
  STATE DR-10 requires -- noted in `blocking_on`, not acted on. **PROMOTES
  NOTHING; queues nothing; NO graduation** (a V4 build graduation needs user
  adjudication per the SELF-4 `graduation_decision_2026_06_16` precedent). No
  claims.yaml edit; MECH-215 / ARC-081 stay candidate / v4.
- **2026-07-01** -- SELF-1 (DR-13 z_self temporal depth) **SUBSTRATE BUILT**
  (user-directed, same day, to unblock SELF-3 after the morning IGW-165
  reconcile). `/implement-substrate` landed the HYBRID DR-13 lever in ree-v3:
  a light DEDICATED self-recurrence (`ree_core/latent/self_recurrence.py`
  `SelfRecurrenceCell`, a GRUCell over z_self) whose output is blended toward
  the E1 generative prediction of z_self (E1 predicted-next z_self cached at
  `_e1_tick`), blend weight `LatentStackConfig.self_recurrence_e1_coupling`
  (the recorded residual tunable: 0 = pure recurrence / Option A, 1 = pure
  E1-feedback / Option B, **0.15 light default = HYBRID**). The lever lives in
  `LatentStack.encode()` and **replaces the z_self EMA step ONLY** (z_world /
  z_beta / z_theta / z_delta untouched); master switch
  `use_self_recurrence` (default False -> module not instantiated + verbatim
  legacy EMA -> **bit-identical OFF**). The self subject is perturbation-isolated
  (only z_self flows through the cell; a +5.0 perturbation of `prev.z_self`
  leaks 0.0 into z_world -- contract C5). Full suite **1336 passed / 4
  pre-existing failures** (confirmed byte-identical on the clean tree via
  `git stash`) + **11 new contracts**
  (`tests/contracts/test_dr13_self_recurrence.py`). `generation:v4` -- off the
  V3 closure %. **PROMOTES NOTHING** (ARC-081 gets an `implementation_note`
  only; stays candidate / v4 / v3_pending; MECH-215 unchanged). **SELF-1
  `last_updated` -> 2026-07-01 + `build_2026_07_01` record.** **This build
  CLEARS SELF-3's blocker**: the stateful z_self it needs as the subject of
  viability now exists -> **SELF-3 flipped blocked -> open** (buildable DR-10
  step; left open, not auto-graduated -- graduation is a user call per the
  SELF-4 precedent). SELF-5 / SELF-7 stay blocked (now on SELF-3 alone).
  `owner_exq` for both SELF-1 and SELF-3 assigned at queue time. Design doc:
  `docs/architecture/dr13_self_recurrence_temporal_depth.md`;
  `ree-v3/CLAUDE.md` SD-implemented entry. Validation = the DR-13 falsifier
  queued via `/queue-experiment` (separate step).
- **2026-07-01** -- SELF-3 (DR-10 z_self enters E3 viability scoring) **SUBSTRATE
  BUILT** (user-approved graduation via AskUserQuestion, same session as the
  SELF-1 DR-13 build that cleared its blocker; caller-supplied v1). Executed the
  minute the DR-13 stateful z_self existed. `/implement-substrate` landed the
  DR-10 lever in ree-v3 **mirroring the DR-12/SELF-4 pattern on the SAME
  `e3_selector` machinery**: `_self_viability_penalty` helper +
  `score_trajectory(self_viability=...)` monotone penalty block +
  `select(self_viability_per_candidate=[K])` per-candidate threading + 4
  diagnostics; `E3Config` 4 no-op fields (`use_self_viability_weighting` default
  False) + `REEConfig.from_dims` passthrough; agent `_injected_self_viability` +
  `set_injected_self_viability()` seam + version-layering-guarded `select_action`
  passthrough. A per-candidate self-viability COST derived from the DR-13
  stateful z_self (capacity/affect/damage) discounts trajectories less viable for
  the current bodily state; **no learned parameters**; master switch default
  False -> **bit-identical OFF**. Full suite **1344 passed / 4 pre-existing
  failures** (clean-tree-confirmed) + **8 new contracts**
  (`tests/contracts/test_dr10_z_self_viability.py`). `generation:v4`, **PROMOTES
  NOTHING** (MECH-215 + ARC-081 stay candidate/v4; both get implementation_notes
  only). **SELF-3 `status: open -> in_progress`, `owner_exq -> V4-EXQ-003`**
  (assigned at queue time), `build_2026_07_01` + `resume_condition` added. v1
  self-viability source = **caller/agent-supplied** (user-chosen AskUserQuestion);
  the ecological z_self-derived auto-source (allostatic z_self-deviation x
  per-candidate demand, or a learned z_self->viability head needing phased
  training + SELF-2's per-candidate self-transition) is the documented follow-on.
  DR-10 + DR-12 (SELF-4) are the two halves of the MECH-215 unblock. Design doc
  `docs/architecture/dr10_z_self_in_e3_viability.md`; `ree-v3/CLAUDE.md`
  SD-implemented entry. Validation = the DR-10 pilot **V4-EXQ-003** queued via
  `/queue-experiment`.
