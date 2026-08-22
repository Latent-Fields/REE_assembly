---
closure_plan:
  id: inference_belief_state_v4
  generation: v4
  title: "Inference / belief-state affordance layer (the inference pipeline)"
  registered: 2026-06-10
  last_updated: 2026-06-16
  scope_claims: [ARC-004, ARC-007, ARC-018, MECH-022, MECH-033, ARC-062, ARC-063, SD-057, SD-059, MECH-358, Q-044, INV-035, INV-036]
  sibling_plans: [object_representation_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. The "inference pipeline" is the
    user-named integrative function that constructs latent state HYPOTHESES and
    inferred AFFORDANCE fields from partial observation, memory, cues, rules,
    affective gradients, and E2 rollouts, so E3 can select trajectories under
    partial observability. It is NOT a new organ: every ingredient already
    exists or is planned (ARC-004 L-space, ARC-007/ARC-018 hippocampal
    completion + rollout, MECH-022 hypothesis injection, MECH-033 E2 kernel
    chaining, ARC-062/063 rule apprehension, SD-057 cue recall, SD-059/MECH-358
    escape-affordance bridge, Q-044 epistemic value). The missing work is the
    NAMED integrative loop and its belief-state representation. V4 has no
    experiments yet, so every node carries owner_exq: null and the drift checker
    stays dormant. The value here is the readiness_gate per node = the V3-era
    prerequisites that must land before each V4 step is honest to build.
    generation: v4 keeps these nodes OUT of the V3 closure percentage. A node
    graduates from roadmap to closure-tracked by gaining an owner_exq once its
    first V4 experiment is queued. Trigger: V3-EXQ-603k ARM_HARM_ON_MIDLINE,
    where harm valuation passes on favourable navigation but fails when the
    creature must INFER a route to safety from partial evidence.
  nodes:
    - id: "inference_belief_state_v4:INF-1"
      title: "Name + route the inference layer (V3 architecture note, no substrate)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-091"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "V3 ALREADY HAS the ingredients: ARC-004 (L-space), ARC-007 (path completion), ARC-018 (rollout + viability mapping), MECH-022 (hypothesis injection), MECH-033 (E2 kernel chaining) -- all implementation_phase: v3"
        - "DECISION this node forces: register the umbrella ARC claim that NAMES inference as a distinct integrative function (bridge, not organ) and pins its depends_on to the ingredient claims above; V3 scope is name+route ONLY, no belief-state code"
        - "Guard from intake section 14: do not explode V3 scope; 603k midline is routing PRESSURE, not a demand for full implementation"
      last_updated: 2026-06-13
      completion_note: "Intake section 7 sketches the umbrella ARC. The umbrella distinguishes inference (select/combine/apply rules under uncertainty) from rule apprehension (supply candidate regularities). This is the parent every node below specialises. Registered as candidate, not promoted -- naming changes no V3 behaviour. Reconciled 2026-06-13: claim(s) ARC-091 registered in claims.yaml; this design commitment/prohibition is the deliverable and is landed -- downstream nodes remain blocked on their substrate."
    - id: "inference_belief_state_v4:INF-2"
      title: "Inferred state must not collapse to perceived observation (invariant)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["INV-078"]
      depends_on: ["inference_belief_state_v4:INF-1"]
      cross_plan_link: []
      readiness_gate:
        - "V3 state invariants already present: INV-035 (state not defined by sensory appearance) + INV-036 (state must support transition prediction, valence/antigoal tagging, uncertainty)"
        - "This node EXTENDS those: under partial observability the perceived scene is EVIDENCE for state, not identical to state; the gap is the missing how-is-state-inferred step (intake 4.1)"
        - "Provenance constraint (intake section 8 final candidate): inferred/imagined trajectories must remain provenance-tagged until enacted and updated by committed outcome"
      last_updated: 2026-06-10
      completion_note: "Two invariant candidates folded here: inferred-state-not-observation and inferred-trajectory-provenance-tagging. Both are corollaries of existing INV-035/036 but make the inference-specific obligation explicit. Invariants, not substrate -- no experiment owns them; they constrain the substrate nodes below."
    - id: "inference_belief_state_v4:INF-3"
      title: "Belief-state hypothesis set (top-k latent-state hypotheses with precision)"
      phase: 2
      status: blocked
      blocker_class: v3_substrate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-385"]
      depends_on: ["inference_belief_state_v4:INF-1", "inference_belief_state_v4:INF-2"]
      cross_plan_link: []
      blocking_on: "MECH-022 hypothesis injection is the V3 generator (control-plane gated). The belief-SET (multiple competing hypotheses each with confidence + predicted transitions, scored by E3 instead of a single collapsed state) is the V4 extension; cannot build the set until the single-hypothesis injection path is exercised and instrumented in V3."
      readiness_gate:
        - "V3 generator present: MECH-022 (hippocampal hypothesis injection gated by control plane) + ARC-007 pattern completion produce candidate hypotheses"
        - "V3 rollout present: ARC-018 explicit rollouts + post-commitment viability mapping; MECH-033 E2 kernels seed the rollouts"
        - "V4 cutover: a BOUNDED set of competing hypotheses (top-k), each carrying confidence/precision, predicted transitions, goal/antigoal relations, uncertainty; E3 evaluates trajectories OVER the set, not over one collapsed state (intake section 8)"
      last_updated: 2026-06-16
      completion_note: "Intake section 8 + 12 (InferredStateHypothesis schema). V3-minimal form = top-k state hypotheses + confidence weights + uncertainty flags. V4-fuller = structured belief distribution, hypothesis generation from hippocampal completion, updating from action/outcome evidence. This is the core representational step of the layer. READINESS NOTE 2026-06-16: the injection-path half of the blocker has partly cleared -- MECH-022 advanced candidate->provisional and now carries one genuine instrumented experiment (claim_evidence.v1.json genuine_exp_count=1, exp_conf=0.311, mixed) and ARC-018/ARC-007/MECH-033 rollout+completion are all active. The single-hypothesis injection path is therefore exercised and instrumented, but the one run is mixed/fail (not cleanly confirmed), so this stays blocked rather than graduating; revisit once MECH-022 has a clean PASS confirming the injection path before opening the top-k belief-SET extension."
    - id: "inference_belief_state_v4:INF-4"
      title: "Inferred affordance field (afford. not directly perceived; biases E3 candidates)"
      phase: 2
      status: blocked
      blocker_class: v3_substrate
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-386"]
      depends_on: ["inference_belief_state_v4:INF-3"]
      cross_plan_link:
        - "object_representation_v4:OBJ-4"
      blocking_on: "Affordances must be grounded in object->action binding (cross-plan OBJ-4 / ARC-082), whose V3 path SD-016 cue_action_proj is inert (V3-EXQ-449 found 0.0 gradient; SD-055 differentiable-CEM restores it). Inferred affordances over an ungrounded action space are vacuous."
      readiness_gate:
        - "V3 rule field present: ARC-062 (weak-reading gated policy) live; ARC-063 (CandidateRule field) V3-tractable design landed 2026-06-04 -- supplies the rule-content input to inferred affordances"
        - "V3 cue recall present: SD-057 object-bound incentive-salience layer (L6 cue-recall MECH-CUEWANT deferred to its phase-2 pass) -- supplies cue traces"
        - "Cross-plan grounding gate: object_representation_v4 OBJ-4 (ARC-082 tools/affordances) + SD-055 differentiable-CEM must restore the cue_action_proj gradient before afforded actions are meaningful"
      last_updated: 2026-06-10
      completion_note: "Intake section 8 + 12 (InferredAffordance schema). Combines cues + hippocampal traces + E2 rollouts + CandidateRuleField + affective gradients + control-plane precision into affordances the agent does not directly perceive, biasing E3 candidate trajectories WITHOUT overwriting perception. Design constraint: inferred affordances are hypotheses, corrigible by outcome."
    - id: "inference_belief_state_v4:INF-5"
      title: "Safety-route inference (infer route to safety from partial map/cue/gradient)"
      phase: 3
      status: blocked
      blocker_class: v3_substrate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-387"]
      depends_on: ["inference_belief_state_v4:INF-3", "inference_belief_state_v4:INF-4"]
      cross_plan_link: []
      blocking_on: "SD-059/MECH-358 escape-affordance bridge is candidate + pending_retest_after_substrate (2026-06-09 autopsy: retest gated on a Stage-H nav/survival-competence leg + MECH-303/304 threat-absence predictor wired; safety half 0/3 on V3-EXQ-603i). Safety-ROUTE inference cannot be built until the scalar escape-affordance bridge it generalises is itself substrate-confirmed."
      readiness_gate:
        - "V3 bridge present-but-unconfirmed: SD-059 + MECH-358 supply per-first-action-class relief/safety credit (the scalar precursor); these must clear their pending_retest_after_substrate gate first"
        - "V3 trigger: V3-EXQ-603k ARM_HARM_ON_MIDLINE -- the arm that exposed danger-sense-without-route; intake interpretation rule (section 10): midline failure is NOT harm-pathway falsification unless route inference was developmentally available and still unused"
        - "V4 step: generalise scalar action-class credit into a ROUTE inferred from partial map (ARC-007/ARC-018) + cue (SD-057) + gradient evidence; fair developmental version must first EXPOSE reef/safety geography, landmarks, hazard gradients, safe-route traces (intake section 10)"
      last_updated: 2026-06-10
      completion_note: "Intake section 8 (safety-route inference) + section 10 (603k interpretation). This is the behavioural payoff that motivates the whole plan: the creature can smell danger (harm valuation, ARM_HARM_ON_NAV passes) but cannot yet infer the cave exit (ARM_HARM_ON_MIDLINE struggles). The directed escape that SD-059/MECH-358 only scalar-credit is here inferred as a route."
    - id: "inference_belief_state_v4:INF-6"
      title: "Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)"
      phase: 3
      status: blocked
      blocker_class: lit_gap
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-388"]
      depends_on: ["inference_belief_state_v4:INF-3"]
      cross_plan_link: []
      blocking_on: "Q-044 (are striatal-novelty / uncertainty-curiosity / learning-progress three substrates or one?) is OPEN. Generalising curiosity into survival-relevant uncertainty reduction is unsound until the curiosity sub-flavour structure it builds on is adjudicated."
      readiness_gate:
        - "V3 curiosity machinery present: Q-044 cohort (MECH-314a striatal novelty / MECH-314b frontopolar uncertainty / MECH-314c learning-progress) -- but the sub-flavour independence question is unresolved (Q-044 status: open)"
        - "V4 generalisation: epistemic value is not ONLY play/curiosity; under partial observability it is a VIABILITY function -- assign action pressure to uncertainty-reducing transitions even when not immediately reward/harm-optimal (intake section 6.3)"
        - "Active-inference framing (intake 6.3): pragmatic + epistemic value; in a dangerous midline state the intelligent action may be one that TESTS where safety is"
      last_updated: 2026-06-10
      completion_note: "Intake section 8 (epistemic action pressure) + 6.3 (active inference / Q-044). The bridge from EXPLORE-when-safe curiosity to PROBE-under-threat survival inference. Examples: sample a safer-looking direction to disambiguate map; pause/replay before commitment; approach a landmark to resolve a route hypothesis."
    - id: "inference_belief_state_v4:INF-7"
      title: "Inference failure-mode register + biology grounding (lit-pulls)"
      phase: 2
      status: open
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: ["Q-070", "MECH-434"]
      depends_on: ["inference_belief_state_v4:INF-1"]
      cross_plan_link: []
      readiness_gate:
        - "Biology grounding (project rule feedback_biology_before_formal_definitions): L1 hippocampal-prefrontal replay (intake 5.1); L2 cognitive-map / relational inference (intake 5.2); L3 pattern-completion vs preplay safety (intake 5.3); L4 POMDP belief-state + Dreamer latent world models (intake 6.1/6.2); L5 active inference / epistemic value (intake 6.3)"
        - "Failure-mode register (intake section 9): failure-to-infer-hidden-danger, failure-to-infer-hidden-safety, overconfident-wrong-hypothesis, premature-collapse, hypothesis-proliferation (apophenia/paranoia), cue-hijack, rule-overreach, map-over/under-generalisation, epistemic-freezing, anti-epistemic-panic"
        - "These map onto EXISTING state-abstraction failure modes (context loss, uncertainty collapse, valence mis-tagging, overmerge, oversplit, threat-spreading) -- the register links new modes to the existing taxonomy rather than inventing a parallel one"
      last_updated: 2026-06-13
      lit_pull_note: "DONE 2026-06-13 via /lit-pull (session lit-pull-inf7-belief-state-inference). 8 literature_evidence/v1 entries under evidence/literature/targeted_review_belief_state_inference grounding all 5 strands: L1 Pfeiffer&Foster 2013 (prospective replay, supports 0.78), L2 Whittington 2020 TEM (relational map, 0.76), L3 Kay 2020 (cycling-between-possible-futures, 0.80 -- highest fidelity: MECH-385 belief-set + INV-078 provenance), L4 Kaelbling 1998 POMDP (belief-not-observation, 0.70, MECH-385) + Hafner 2023 DreamerV3 (latent imagination, 0.65), L5 Friston 2015 active inference (epistemic value, 0.70, MECH-388); failure register grounded by Sterzer 2018 predictive-coding-psychosis (0.74) + Ross 2015 JTC meta-analysis (mixed 0.62). Failure-mode register MAPPED onto the existing MECH-126 state-abstraction taxonomy (synthesis table): 9/11 modes reduce to context-loss/uncertainty-collapse/valence-mis-tag/overmerge/oversplit/threat-spreading; the 2 epistemic-balance modes (epistemic-freezing / anti-epistemic-panic) form a genuinely-new commitment-timing axis -> surfaced PROPOSAL-FIRST (recommend keeping inside Q-070 as a sub-axis note, NOT a new MECH while substrate absent). Tags Q-070 + ARC-091 (+ MECH-385/388/INV-078 where mapping is direct). literature_confidence only; exp_conf 0; PROMOTES NOTHING; no V3 experiment queued."
      completion_note: "Intake sections 5, 6, 9. The lit grounding must precede the belief-state substrate (project rule: biology before formal definitions, canonical failures SD-003/SD-010). The failure-mode register doubles as the diagnostic-design source for the eventual V4 safety-route-inference experiment family (intake section 11)."
---
# Inference / Belief-State Affordance Layer -- V4 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** name and sequence the user's "inference pipeline" -- the integrative
function that constructs latent state HYPOTHESES and inferred AFFORDANCE fields
from partial observation, memory, cues, rules, affective gradients, and E2
rollouts, so that E3 can select trajectories under partial observability. Pin
each step's V3-era readiness gate so the V4 substrate slots in against a
registered spine instead of being demanded prematurely by a single hard
experiment arm.

This is a *forward roadmap*, not a closure map: V4 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant. The value is the
**readiness gates** -- for each inference step, exactly which V3-era
prerequisites (claims/tracks/experiments) must land before the V4 substrate step
is honest to build.

---

## One-line framing

> REE already has state, map, memory, cue, rule, prediction, valuation, and
> commitment. What is unnamed is the integrative loop that turns partial
> evidence into a SET of state hypotheses and inferred affordances under
> uncertainty -- the step that lets the creature, smelling danger, INFER the
> cave exit rather than only avoid the smell. ARM_HARM_ON_NAV passes (harm
> valuation works); ARM_HARM_ON_MIDLINE struggles (route inference is the next
> intelligence layer becoming visible). This plan names that layer and pins its
> gates.

---

## The inference pipeline (steps, not organs)

| Step | Node | Seeds / new claim | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| name + route | INF-1 | NEWCLAIM umbrella ARC; ARC-004/007/018, MECH-022/033 | V3 names / V4 builds | ingredient claims all live; register umbrella, no code |
| state != observation | INF-2 | NEWCLAIM invariant(s); INV-035/036 | V3 invariant extension | extend existing state invariants; add provenance-tag rule |
| belief-state set | INF-3 | NEWCLAIM belief_state_hypothesis_set; MECH-022, ARC-018 | V3 generator / V4 set | MECH-022 injection + ARC-018 rollout exercised first |
| inferred affordance field | INF-4 | NEWCLAIM inferred_affordance_field; ARC-062/063, SD-057 | V4 | cross-plan OBJ-4 grounding (SD-016/SD-055) |
| safety-route inference | INF-5 | NEWCLAIM safety_route_inference; SD-059/MECH-358 | V4 | SD-059/358 must clear pending_retest_after_substrate |
| epistemic action pressure | INF-6 | NEWCLAIM epistemic_action_pressure; Q-044 | V4 | Q-044 sub-flavour question adjudicated |
| failure register + biology | INF-7 | NEWCLAIM register; L1..L5 lit-pulls | cross-cutting | biology-before-definitions; map to existing failure taxonomy |

---

## What this plan deliberately does NOT pull into V3

- **No belief-state substrate code in V3.** Intake section 14 is explicit: do
  not explode V3 scope. V3's only inference action is to NAME the layer
  (INF-1), register the state-inference invariants (INF-2), and use 603k midline
  as routing pressure -- not as a demand for immediate full implementation. The
  belief-state SET, inferred affordance field, safety-route inference, and
  epistemic action pressure are all V4.
- **603k ARM_HARM_ON_MIDLINE failure is NOT harm-pathway falsification.** The
  interpretation rule (intake section 10) is load-bearing: a midline failure
  where ARM_HARM_ON_NAV passes reads as "harm valuation supported; safety-route
  inference not yet available / not yet developmentally fair," a PROGRESS
  result. Do not let this plan be cited to weaken SD-059/MECH-358 or the harm
  pathway.
- **No promotions, no claim status changes.** Registering this roadmap changes
  no V3 behaviour. The new claims it proposes are candidate/version-scoped and
  wired into depends_on; whether to BUILD any V4 step is a later decision gated
  on its readiness_gate.
- **Rule apprehension is a prerequisite, not a replacement.** ARC-062/063 supply
  candidate regularities (priors + availability gates); inference selects,
  combines, and applies them. This plan does not absorb or duplicate the
  rule-apprehension layer.

---

## Source artefacts

| Artefact | Role |
|---|---|
| evidence/planning/thought_intake_2026-06-09_inference_belief_state_affordance_layer.md | PRIMARY source: the inference-pipeline intake (sections 7-12 sketch the candidate claims) |
| claims.yaml ARC-004 / ARC-007 / ARC-018 / MECH-022 / MECH-033 | the L-space + hippocampal completion/rollout + injection + kernel-chaining ingredients (all implementation_phase: v3) |
| claims.yaml ARC-062 / ARC-063 | rule-apprehension layer (weak live; strong V3-tractable design landed 2026-06-04) -- prior input to inferred affordances |
| claims.yaml SD-057 | object-bound incentive-salience / cue-recall (L6 MECH-CUEWANT deferred) -- cue-trace input |
| claims.yaml SD-059 / MECH-358 | escape-affordance bridge (candidate, pending_retest_after_substrate) -- scalar precursor to safety-route inference |
| claims.yaml Q-044 | curiosity sub-flavour independence (open) -- gate on epistemic action pressure |
| claims.yaml INV-035 / INV-036 | state-not-appearance + navigable-state invariants -- extended by INF-2 |
| V3-EXQ-603k | the trigger run: ARM_HARM_ON_NAV vs ARM_HARM_ON_MIDLINE split |

---

## V4 belief-state system -- design notes (grounded 2026-06-13)

The INF-7 lit-pull (`evidence/literature/targeted_review_belief_state_inference`,
biology-before-formal-definitions) is not just confidence bookkeeping -- it pins
the **design constraints** the eventual V4 belief-state substrate must satisfy.
These are the claims V4 will be built on, each with its grounding and its
non-negotiable shape. Nothing here is built in V3.

1. **Representation = a bounded SET, not a single state and not a full posterior
   (MECH-385).** Grounded by Kay 2020 (hippocampus holds competing futures in
   sub-second alternation) + Kaelbling 1998 (policy must map a belief over hidden
   states, not the observation). *Design:* top-k latent-state hypotheses, each
   carrying confidence/precision, predicted transitions, goal/antigoal relations,
   and uncertainty (the `InferredStateHypothesis` schema, intake S12). Explicitly
   an approximation -- REE does NOT import exact POMDP belief-updating (Kaelbling
   caveat) and does NOT reward-collapse the way Dreamer does (Hafner caveat).

2. **Provenance = hypotheses stay tagged as inferred until enacted (INV-078).**
   Grounded by Kay 2020 (cycling = refusing to collapse early) + pattern-completion-
   is-hypothesis (intake 5.3). *Design:* inferred/imagined trajectories carry a
   provenance tag; they bias selection but do NOT overwrite perception or write
   residue history until a committed outcome updates them. This is the guard
   against inference becoming hallucinated certainty.

3. **Generation = hippocampal completion/replay as a PROSPECTIVE hypothesis source.**
   Grounded by Pfeiffer & Foster 2013 (pre-navigation sequences depict future paths
   to goals) + Whittington 2020 TEM (the map is relational and generalises).
   *Design:* MECH-022 injection + ARC-007 completion + ARC-018 rollout feed the set;
   ARC-004 L-space supplies relational generalisation -- with map over/under-
   generalisation (-> MECH-126 overmerge/oversplit) as the named failure axis.

4. **Action side = inferred affordance field, corrigible by outcome (MECH-386).**
   Grounded by Hafner 2023 (latent imagination can drive behaviour) but with REE's
   stream-separation kept. *Design:* affordances bias E3 candidates without
   overwriting perception; gated on cross-plan OBJ-4 object->action grounding
   (SD-016/SD-055) so the action space is not vacuous.

5. **Epistemic value as a first-class action term (MECH-388).** Grounded by Friston
   2015 (policy value = pragmatic + epistemic). *Design:* assign action pressure to
   uncertainty-reducing transitions even when not immediately reward/harm-optimal;
   gated on Q-044 curiosity sub-flavour adjudication before generalising curiosity.

6. **Commitment timing as a GOVERNED parameter (MECH-434 -- registered 2026-06-13).**
   Grounded by Cisek 2009 (urgency-gating = timing is a tunable gain), Mobbs 2020 +
   Arnsten 2009 (threat/arousal collapses deliberation = anti-epistemic-panic pole,
   inverted-U), Hauser 2017 (raised threshold / over-gathering in OCD = epistemic-
   freezing pole, the mirror of Ross 2015 JTC). *Design:* an urgency/threshold over
   the belief-set, THREAT-modulated, with an inverted-U optimum, sitting at the
   MECH-385/MECH-388 -> MECH-061/MECH-090 seam. Plausibly implemented via a future
   LC-NE-analog gain modulator (MECH-433, the cross-plan neuromodulator gap). This
   is the one register axis that did NOT reduce to MECH-126.

7. **Failure register = the diagnostic-design source (Q-070).** The eventual V4
   safety-route-inference experiment family (intake S11) should instrument every
   register mode: 9 map onto MECH-126 (context-loss/uncertainty-collapse/valence-
   mis-tag/overmerge/oversplit/threat-spreading), 2 onto MECH-434 (freezing/panic).
   Each diagnostic must probe BOTH poles of timing, not just premature commitment.

8. **What stays OUT of V3 (unchanged).** No belief-state code in V3; 603k
   ARM_HARM_ON_MIDLINE is routing PRESSURE, not harm-pathway falsification; no
   promotions (every claim here is `substrate_conditional`, exp_conf 0).

---

## Decision log

- **2026-06-13** -- INF-7 lit-pull executed (8 entries) + design noting. All 5
  biology/ML strands (L1 Pfeiffer&Foster 2013 / L2 Whittington TEM 2020 / L3 Kay
  2020 / L4 Kaelbling 1998 + Hafner DreamerV3 2023 / L5 Friston 2015) and the
  failure register (Sterzer 2018, Ross 2015) grounded; `lit_pull_status` none->done.
  Failure-mode register mapped onto the existing MECH-126 taxonomy (9/11 modes);
  the residual **epistemic-freezing <-> anti-epistemic-panic** axis registered at
  user direction as **MECH-434** (epistemic commitment timing), with its own
  grounding pull (Cisek 2009 / Mobbs 2020 / Arnsten 2009 / Hauser 2017) and cross-ref
  to MECH-433 (LC-NE-analog) as candidate implementer. `literature_confidence` only
  -- exp_conf stays 0, PROMOTES NOTHING. V4 belief-state design-notes section added
  above. No V3 experiment queued.

- **2026-06-10** -- Plan registered as a V4 forward-roadmap in the
  generation-segmented closure pipeline (sibling to object_representation_v4).
  Seven nodes seeded from the 2026-06-09 inference-pipeline intake. Readiness
  gates pinned per step against live V3 seed claims; `generation: v4` set so the
  V3 closure % is unaffected. No claims.yaml edits -- the seven new candidate
  claims (umbrella ARC + state invariant(s) + belief-state set + inferred
  affordance field + safety-route inference + epistemic action pressure +
  failure register) are returned as proposed_claims for the orchestrator to
  register, with NEWCLAIM placeholders in the node unblocks_claims lists.
