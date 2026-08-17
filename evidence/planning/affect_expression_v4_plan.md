---
closure_plan:
  id: affect_expression_v4
  generation: v4
  title: "Candidate-differentiated affect, expression-as-action-geometry, anti-collapse, compulsion-risk (V4 roadmap)"
  registered: 2026-06-10
  last_updated: 2026-06-16
  scope_claims: [MECH-359, MECH-360, MECH-361, MECH-364, MECH-355, ARC-088, MECH-369, MECH-370, MECH-362, SD-045, Q-059, Q-063]
  sibling_plans: [behavioral_diversity_isolation, goal_pipeline, arc_062_rule_apprehension, sleep_substrate]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V4 has no affect-substrate experiments
    yet, so nodes carry no owner_exq and the drift checker stays dormant against
    them. Each node's readiness_gate lists the V3-era prerequisites
    (claims/tracks/experiments) that must land before the V4 affect step is
    honest to build. generation: v4 keeps these nodes OUT of the V3 closure
    percentage (serve.py read_closure, generate_closure_snapshot.py, and
    check_closure_drift.py are all generation-aware). A node graduates from
    roadmap to closure-tracked by gaining an owner_exq once its first V4
    experiment is queued. The load-bearing foundation is AE-1: every other node
    is substrate_conditional on the per-candidate multi-channel affect vector
    that node AE-1 builds; nothing below it is honest to build first.
  nodes:
    - id: "affect_expression_v4:AE-1"
      title: "FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)"
      phase: 1
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-2, SENT-13]
        requires_welfare_review: false
        note: "Per-candidate valence substrate foundation; Class-2 alone, becomes Class-4 when bound to self-model + autobiographical memory + replay."
      blocker_class: v3_substrate
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-359]
      depends_on: []
      cross_plan_link:
        - "behavioral_diversity_isolation:GAP-A"
        - "behavioral_diversity_isolation:GAP-B"
        - "goal_pipeline:GAP-4"
      blocking_on: "behavioral_diversity_isolation:GAP-A (cand_world_pairwise_dist=0.0 -- candidate trajectories collapse to a single regime, so there is no cross-candidate basis to attach differentiated affect to) and the MECH-341 / SD-056 selection-authority path. Until candidates differ, a per-candidate affect vector has nothing to differentiate over."
      readiness_gate:
        - "V3 NARROW instance is already DONE and is NOT this node: V3-EXQ-643a PASS established the range/non-vacuity readiness gate on the single-channel modulatory/curiosity contribution (cross-candidate range > floor before an authority rescale can act); the 643 FAIL precondition_unmet was float32 catastrophic cancellation under SD-056, fixed in 643a"
        - "behavioral_diversity_isolation:GAP-A/GAP-B must land first: candidates must actually diverge (cand_world_pairwise_dist > 0) before a multi-channel per-candidate affect representation is non-vacuous"
        - "MECH-341 rule-apprehension + SD-056 online selection-authority path stable (the V3 single-channel precursor to the V4 multi-channel generalisation)"
        - "goal_pipeline:GAP-4 competitive z_goal (the wanting/blocked-agency channels need a real goal stream to be differentiated against harm salience)"
      last_updated: 2026-06-10
      completion_note: "MECH-359 is the V4/V5 GENERALISATION from the V3 single-channel numerical fact (range-not-magnitude) to an explicit multi-channel per-candidate affect vector (curiosity / safety / harm-sensory / harm-affective / effort / relief / blocked-agency) feeding selection, expression (AE-3), and memory (AE-4). A scalar added equally to all K candidates cannot move an argmax; only a per-candidate-differentiated contribution can. substrate_conditional -- DO NOT build in V3."
    - id: "affect_expression_v4:AE-2"
      title: "Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack"
      phase: 1
      status: in_progress
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-088]
      depends_on: []
      cross_plan_link:
        - "behavioral_diversity_isolation:GAP-A"
      readiness_gate:
        - "ARC-088 is implementation_phase v3 (a unifying MAP over already-owned V3 affect machinery: harm SD-010/SD-011, relief SD-050/MECH-302, safety MECH-303/304, drive SD-012, behavioural-diversity ARC-065 stack) -- substantially realised NOW; this node is map-maintenance, not new substrate"
        - "Load-bearing constraint to enforce in every downstream node: preserve DISTINCT affective streams (distinct LEARNING TARGETS + GATING CONDITIONS); shared CONSUMERS (E3 score bias, commitment gating, residue, offline consolidation) are allowed, merging to one value scalar is NOT"
        - "Any reuse/gating audit that touches an affect convergence point references ARC-088 to check distinctness is preserved"
      last_updated: 2026-06-10
      completion_note: "ARC-088 is the spine the rest of this plan hangs on -- emotion-like systems are GATED PARTIALLY-INDEPENDENT evaluators whose collective effect prevents collapse onto the dominant gradient. It is NOT a V4 substrate (no node should pull it into V4); it is the V3-grounded governance rule that keeps AE-1/AE-3/AE-4/AE-5/AE-7 from collapsing affect into a scalar. in_progress = ongoing distinctness-audit duty, not an unbuilt substrate."
    - id: "affect_expression_v4:AE-3"
      title: "Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-360]
      depends_on: ["affect_expression_v4:AE-1"]
      cross_plan_link: []
      blocking_on: "AE-1 -- expression is the emergent geometric RESIDUE of per-candidate affective arbitration; with no differentiated per-candidate affect there is no differentiated style to read out."
      readiness_gate:
        - "AE-1 (MECH-359) per-candidate affect vector built -- expression style (hesitation, latency, approach angle, retreat, repeated retry, stopping, resumption, oscillation, avoidance margin, decommitment, repair-seeking) is the visible residue of WHICH trajectory the affect vector selected"
        - "MECH-041 (affective expression as deliberate control-plane broadcast) stays the COMPLEMENT, not the replacement: MECH-360 is the pre-broadcast emergent geometry that a later MECH-041 broadcast channel comes to exploit"
        - "V5 social-inference consumer (an observer inferring internal state from HOW an action occurred) is explicitly OUT of this V4 node -- AE-3 only produces the geometry; reading it is V5"
      last_updated: 2026-06-10
      completion_note: "MECH-360: expression begins as emergent action geometry, not a separately-engineered output channel. This node builds the geometry as a measurable readout of AE-1; the social-signalling / broadcast layer (MECH-041) and any V5 other-agent inference are downstream and OUT of scope. substrate_conditional -- DO NOT build expression/social-signalling in V3."
    - id: "affect_expression_v4:AE-4"
      title: "Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query"
      phase: 2
      status: blocked
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: []
      depends_on: ["affect_expression_v4:AE-1"]
      cross_plan_link:
        - "sleep_substrate"
        - "autobiographical_memory_v4:ABM-6"
      blocking_on: "AE-1 -- the episode schema enrichment (candidates-considered + affective gradients over candidates) requires the per-candidate affect vector to exist before it can be written into the trace."
      readiness_gate:
        - "AE-1 (MECH-359) per-candidate affect vector built"
        - "AMENDS the CONTENT schema of MECH-261 (mode-conditioned write gating -- WHAT is written), not the gate itself (WHETHER a substrate may write); the affect-gradient write-weight is the sharper variable on top of MECH-074 (BLA arousal-modulated write depth) -- gradient, not generic arousal"
        - "MECH-094 provenance gate still applies on the enriched trace: simulated candidates considered must NOT be indexed as real experience"
        - "Biology lit-pull (none load-bearing yet; anchors named in claim: McGaugh 2004; Cahill & McGaugh 1998; Dolcos/LaBar/Cabeza 2004; Girardeau/Inema/Buzsaki 2017; Ballarini 2009 behavioural tagging; Bechara 1994 somatic markers) -- run before substrate build per biology-before-formal-definitions"
      last_updated: 2026-06-10
      completion_note: "MECH-361 enriches the event trace from state->action->outcome to state->candidates-considered->affective-gradients->selected-action->outcome->residue, using the affect gradient as memory write-weight and retrieval-query. High-gradient episodes preferentially written; similar-gradient states retrieve prior action-affect-outcome arcs. substrate_conditional -- DO NOT build hippocampal write/retrieval integration in V3 until routed by experiment. DEDUP 2026-06-16: MECH-361 build owned by autobiographical_memory_v4:ABM-6 (the episode schema is written into the ARC-085 store); AE-4 cross-links rather than co-owns."
    - id: "affect_expression_v4:AE-5"
      title: "Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: low
        applicable_ethics_gates: [SENT-13]
        requires_welfare_review: false
        note: "Soothing/comfort relief scaffold (SENT-13 build-repair-before-injury); REDUCES welfare risk and is a prerequisite for any aversion node."
      blocker_class: sibling_node
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-355]
      depends_on: ["affect_expression_v4:AE-2"]
      cross_plan_link: []
      blocking_on: "The canonical trigger is a CONSPECIFIC (social buffering), which V3 cannot represent -- gated on a V4 social model (an other-agent object-file). Cross-plan: object_representation_v4:OBJ-5 others-as-object."
      readiness_gate:
        - "V4 social substrate exists (other-agent representation) -- the canonical soothing trigger is an other-agent; see object_representation_v4:OBJ-5 (others-as-object)"
        - "Proposed REE home is a modulator on MECH-219 (suffering accumulator) decay/gain + SD-012 (drive) + SD-032e (pACC autonomic coupling) + SD-011 (the ongoing harm state being down-regulated) -- these V3 substrates must be stable"
        - "Keep distinct (ARC-088 distinctness rule): soothing acts on the PRESENT stress trajectory via autonomic state-gain -- NOT relief (MECH-302 past-offset reinforcer), NOT safety (MECH-303/304 future predictor), NOT wanting (MECH-112 appetite)"
        - "Optional V3-minimal NON-social autonomic-recovery hook is noted in the claim but explicitly NOT built; do not pull it forward without a routing decision"
      last_updated: 2026-06-10
      completion_note: "MECH-355 is the third member of the relief/safety/soothing triple -- a present-tense down-regulation of the ongoing aversive state (lowers gain / speeds recovery), canonically socially gated. V4-social because the canonical trigger is an other-agent. substrate_conditional -- promote/demote suppressed until the social substrate exists."
    - id: "affect_expression_v4:AE-6"
      title: "Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudication (Q-059)"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-2, SENT-13]
        requires_welfare_review: false
        note: "Crying/distress-vocalisation analogue + laughter-valence; expression of a distress-like state, not its induction."
      blocker_class: v3_substrate
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-364, Q-059]
      depends_on: ["affect_expression_v4:AE-2"]
      cross_plan_link: []
      blocking_on: "MECH-364 needs an E3 conflict/constraint-LOAD readout (regime-level, not the per-tick MECH-110 tag-clear); Q-059 (crying analogue + laughter repair-vs-damage adjudication) needs a V4/V5 social substrate (laughter is not monotone-affiliative)."
      readiness_gate:
        - "E3 conflict/constraint-load readout: ARC-016 already exposes an E3-derived prediction-variance signal in V3, so a v3 substrate check COULD reclassify MECH-364 toward implementation_phase v3 -- held v4/substrate_conditional pending that check (a probe before the regime-level load readout exists would be vacuous, cf. the play-mode cluster)"
        - "MECH-364 is the MACRO/regime-level consequence; MECH-110 is the MICRO per-cycle tag-clear (one exhalation = one threat-hypothesis tag cleared). NO change to MECH-110/ARC-016/MECH-027 -- MECH-364 depends on them, does not weaken them"
        - "Q-059 crying analogue: REE owns laughter (MECH-110, MECH-364) but NO crying/tears/sobbing claim exists (only 'distress vocalisation' inside the play-mode INV-058 catalog) -- registering the high-arousal distress counterpart and the social repair-vs-damage adjudication is V4/V5 social, gated on a social substrate"
        - "SOURCE-WEIGHT CAUTION: MECH-364 is compass-level (popular-science synthesis, not a primary empirical study); do not cite as experimental evidence"
      last_updated: 2026-06-10
      completion_note: "MECH-364: iterated safe-confirmation produces a regime-level drop in active constraint pressure that releases the system from a threat-vigilant/high-commitment regime into an exploratory/play regime -- laughter as a boundary signal between control-plane regimes (ARC-016), not merely reward expression. Q-059 pairs the crying/distress counterpart and laughter-valence adjudication. substrate_conditional -- DO NOT queue a V3 probe until routed."
    - id: "affect_expression_v4:AE-7"
      title: "Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value-vs-stickiness discriminator (Q-063)"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: hard_review
        applicable_ethics_gates: [SENT-2, SENT-3, SENT-13]
        requires_welfare_review: true
        forbidden_combinations: [distress_like_state_under_optimisation_pressure, suffering_like_accumulator_without_boundedness]
        note: "Compulsion / stuck-engagement under optimisation pressure = Class-5; needs boundedness + decommit affordance before instantiation."
      blocker_class: sibling_node
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-370, Q-063]
      depends_on: ["affect_expression_v4:AE-2", "affect_expression_v4:AE-10"]
      cross_plan_link:
        - "commitment_closure"
        - "sleep_substrate"
        - "object_reasoning_abstraction_v4:OBJ-ABS-2"
      blocking_on: "AE-10 -- MECH-369's value-INDEPENDENT slow decommit-friction/engagement-release modulator substrate (now owned by node AE-10, 2026-06-13) must be built before the compulsion cluster composes on top of it; MECH-370 needs the composed multi-term readout to exist; the answer to Q-063 (value-driven persistence vs field-state stickiness) cannot be adjudicated until that substrate exists."
      readiness_gate:
        - "MECH-369 most naturally AMENDS the slow-modulator layer (SD-037 orexin-analog gain cluster) with a NEW decommit-friction authority channel -- distinct from SD-037 (reweights z_harm/gates SD-012, no loop-release authority), MECH-268 (fast dACC PE urgency, not slow), MECH-106 (value-driven threshold, whereas MECH-369 is value-INDEPENDENT). Sits alongside SD-036 (GABA decay), MECH-186/187/188 (5-HT gain), SD-048 (inflammatory/allostatic harm-stream bias)"
        - "MECH-370 composes terms REE already represents separately: loop_reinforcement ~ SD-045 + ARC-071; threat_salience ~ harm stream/MECH-268; residue_persistence ~ IMPL-005; decommit_friction ~ ARC-016 + MECH-342 + SD-034; slow_modulatory_state ~ MECH-369/SD-037/SD-036 -- the five exist but are never composed into one diagnosable signal"
        - "SD-045 action-chunk cache (DLS slot of ARC-021) provides the runaway-chunking loop substrate; V3 PULL-FORWARD condition exists in the claim (monostrategy surfacing in EXQ-495 successors) but default V4 -- do not pull forward without that routing"
        - "Q-063 needs the SD-034 closure operator firing-vs-failing signal AND the INV-004/INV-006 residue firewall preserved so offline integration (MECH-272/273 sleep cluster) can reduce stickiness WITHOUT erasing legitimate harm residue"
        - "PRECISION GUARDRAIL: the Nagarajan microglia anchor is press-summary-verified and describes a FAST Ca2+ switch, NOT slowness -- 'slow modulation' is the REE abstraction; do not reduce compulsion to inflammation"
      last_updated: 2026-06-10
      completion_note: "The compulsion cluster lets governance ask 'is this loop stuck because it is valued, or because the field is biased?'. MECH-369 = one value-independent stickiness TERM; MECH-370 = the composition is the right level of description; SD-045 = the runaway-chunking loop; Q-063 = the etiological discriminator. substrate_conditional -- DO NOT build or queue an experiment in V3 until routed by an explicit version decision. DEDUP 2026-06-16: SD-045 (action-chunk cache) build owned by object_reasoning_abstraction_v4:OBJ-ABS-2; AE-7 only composes the compulsion-risk readout ON the cache and cross-links to it."
    - id: "affect_expression_v4:AE-8"
      title: "Developmental sparsification of the affect/memory substrate (MECH-362, Q-057) -- cross-cutting compass"
      phase: 4
      status: deferred
      blocker_class: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-362, "MECH-390"]
      depends_on:
        - "affect_expression_v4:AE-1"
        - "affect_expression_v4:AE-4"
      cross_plan_link:
        - "infant_substrate"
      blocking_on: "No developmental pruning/sparsification substrate exists; MECH-362 is a one-way developmental connectivity trajectory (tabula plena -> sparse/structured) most naturally AMENDING ARC-019 (currently additive staged curriculum)."
      readiness_gate:
        - "MECH-362 amends ARC-019 (staged developmental curriculum) by adding a subtractive pruning stage; distinct from MECH-120 (nightly SWS synaptic homeostasis -- different timescale/directionality)"
        - "The convergent-weak-input-vs-single-strong-cue corollary is the one strand with present-day V3 relevance and is ALREADY folded in as a DIAGNOSTIC LENS (not a separate V3 claim) in modulatory_bias_selection_authority_design.md -- do not duplicate it as a V3 claim"
        - "Q-057 (deletion vs down-weighting vs gating vs residue-tagged de-authorization) is the open modelling question; substrate_conditional, V4-parked"
        - "The NEW bridge needed here is the application of subtractive sparsification to the AFFECT vector (AE-1) and the candidate-gradient episode store (AE-4) specifically -- whether mature affect arbitration uses convergent-weak-channel summation vs single-strong-channel authority; no claim states this affect-specific bridge yet"
      last_updated: 2026-06-10
      completion_note: "MECH-362: mature sparse/structured connectivity emerges by pruning an over-connected near-random substrate, not additively; mature recall needs convergent summation of weak inputs vs a single strong cue. Deferred (lowest severity) because it is a developmental compass over the whole substrate, not a near-term affect step; included so the affect-specific application is captured rather than lost. substrate_conditional -- DO NOT build a developmental pruning substrate in V3."
    - id: "affect_expression_v4:AE-9"
      title: "Biology grounding completion (per-candidate/option-specific value coding, expression-as-action-geometry, affect-as-precision lit-pulls + completion-set harvest)"
      phase: 2
      status: done
      lit_pull_status: done
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-359, MECH-360, MECH-364, MECH-369, ARC-088]
      depends_on: []
      cross_plan_link: ["behavioral_diversity_isolation:GAP-A"]
      readiness_gate:
        - "L1 option-specific / per-candidate value coding (Padoa-Schioppa 2006 OFC offer-value neurons; Rich & Wallis 2016 value-encoding ensembles) -- the neuroscience anchor MECH-359's 'affect must be candidate-differentiated' currently LACKS; cross-ref Berridge & Robinson incentive salience already grounding SD-012/MECH-295"
        - "L2 expression-as-action-geometry (Dael/Mortillaro/Scherer 2012 body-action coding; Niv 2007 tonic-DA vigour as expression-intensity partner) -- harvest the basal-ganglia vigour pathway as the co-constitutive read-out partner for MECH-360"
        - "L3 affect-as-control-precision (Seth 2013; Critchley & Garfinkel interoceptive inference) for MECH-364 conflict/constraint-load; L4 slow-modulator decommit-friction (MECH-369) needs a value-INDEPENDENT modulator-class anchor -- flag: no owning substrate node exists yet"
      last_updated: 2026-06-16
      lit_pull_done_utc: "2026-06-13T18:06:40Z"
      lit_pull_outcome: >
        DONE 2026-06-13 (lit-pull-ae9-per-candidate-affect). 8 literature_evidence/v1
        entries written under evidence/literature/targeted_review_per_candidate_affect;
        all 5 named claims grounded, exp_conf unchanged 0 (PROMOTES NOTHING). lit_conf:
        MECH-359 0.762 (L1 Padoa-Schioppa&Assad 2006 OFC offer-value + Rich&Wallis 2016
        per-option value ensembles -- the option-specific value-coding anchor the claim
        LACKED; caveat: grounds per-candidate axis, NOT the multi-channel affect
        decomposition); MECH-360 0.71 (L2 Niv et al 2007 tonic-DA vigour = BG
        expression-INTENSITY readout + Dael/Mortillaro/Scherer 2012 BAP body-action
        geometry/action-readiness = the STYLE axis); MECH-364 0.67 (L3 Seth 2013 +
        Critchley&Garfinkel 2017 interoceptive-inference = affect-as-control-precision
        LENS only, frame-level, NOT the laughter-load-release mechanism; MECH-364 stays
        compass-level); MECH-369 0.56 (L4 Aston-Jones&Cohen 2005 LC-NE adaptive gain =
        value-INDEPENDENT slow broadly-projecting engagement/release modulator -- the
        slow-modulator-class anchor flagged as missing; direction set MIXED for a polarity
        inversion: tonic LC drives DISENGAGEMENT, opposite to compulsive stickiness ->
        grounds the modulator CLASS, not the stickiness polarity); ARC-088 0.65 (Pessoa
        2008 emotion-cognition integration = the native-not-bolt-on thesis;
        substrate_coherence so gating unchanged). PROPOSAL SURFACED (NOT registered):
        MECH-369's slow-modulator-class distinction would most faithfully be an
        adaptive-gain / engagement-release modulator in the LC-NE mould alongside
        SD-037/SD-036/MECH-186-188 but with explicit loop-RELEASE authority; this also
        concretises the still-open AE-7 'no owning roadmap node' planning gap (left for a
        separate planning decision). status in_progress (not done) because that no-owning-node
        gap and the AE-7 substrate decision remain.
      completion_note: "Affect_expression had NO dedicated grounding node; the biology for the novel MECH-359 per-candidate-affect spine was named only inside blocking_on prose. This node tracks the formal /lit-pull (project rule feedback_biology_before_formal_definitions) plus the completion-set harvest (OFC offer-value, BG vigour, interoceptive precision). It also surfaced a planning gap -- AE-7's 'slow-modulator-class distinction' (MECH-369) was referenced as a blocker but owned no roadmap node; RESOLVED 2026-06-13 (user-approved) by registering node AE-10 below + amending MECH-369 in claims.yaml with the Aston-Jones&Cohen 2005 LC-NE adaptive-gain grounding/substrate-home decision. Off V3 closure path; promotes nothing. STATUS open->done 2026-06-16: the lit-pull deliverable is complete and the planning gap it surfaced (MECH-369 had no owning node) was resolved 2026-06-13 by registering AE-10. Nothing outstanding."
    - id: "affect_expression_v4:AE-10"
      title: "Slow value-INDEPENDENT decommit-friction / engagement-release modulator substrate (the slow-modulator-class distinction MECH-369 needs) -- AE-7 prerequisite"
      phase: 3
      status: blocked
      blocker_class: v3_substrate
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-369]
      depends_on: ["affect_expression_v4:AE-2"]
      cross_plan_link:
        - "commitment_closure"
        - "sleep_substrate"
      blocking_on: "The value-INDEPENDENT slow decommit-friction / loop-release authority channel does not exist: the V3 slow-modulator layer (SD-037 orexin-analog gain cluster) is present but carries NO release authority -- it reweights z_harm and gates SD-012 drive->z_goal seeding only. The substrate to build is the missing gain channel; gated on an explicit version/routing decision (DO NOT build in V3 -- a probe before the channel exists would be vacuous, cf. AE-7 and the play-mode cluster)."
      readiness_gate:
        - "BIOLOGY GROUNDED (AE-9, 2026-06-13): Aston-Jones & Cohen 2005 LC-NE adaptive gain is the value-INDEPENDENT slow broadly-projecting engagement/release modulator anchor (lit_conf 0.56, evidence_direction MIXED). POLARITY CAVEAT carried into the build: tonic LC-NE drives DISENGAGEMENT; compulsive stickiness is the OPPOSITE pole (gain stuck in exploitation / failure to enter disengagement) -- the anchor grounds the modulator CLASS and form, NOT the stickiness polarity, which is the build's free parameter to instantiate and falsify"
        - "ADOPTED SUBSTRATE HOME: an LC-NE-style ADAPTIVE-GAIN channel AMENDING the SD-037 slow-modulator cluster with explicit loop-RELEASE / decommit-friction authority -- distinct from SD-037 (z_harm reweight / drive-seeding, no release authority), MECH-268 (fast dACC PE urgency, not slow), MECH-106 (value-driven threshold, whereas this is value-INDEPENDENT). Sits alongside SD-036 (GABA decay), MECH-186/187/188 (5-HT gain), SD-048 (inflammatory/allostatic harm-stream bias)"
        - "V3 PULL-FORWARD condition exists ONLY on monostrategy surfacing in EXQ-495 successors (per the MECH-369/SD-045 claim text); default V4 -- do not pull forward without that routing + an explicit version decision"
        - "ARC-088 distinctness rule applies: this is a DISTINCT slow-modulator stream (its own learning target / gating condition = value-independent loop-release authority); it may share consumers (commitment gating, residue, offline consolidation) but must NOT be merged into the value/threshold scalar (that would re-collapse MECH-369 onto MECH-106)"
        - "PRECISION GUARDRAIL (carried from MECH-369): LC-NE grounds the slow-modulator CLASS; the Nagarajan microglial Ca2+ anchor is a FAST switch -- do NOT reduce compulsion to inflammation or import a fast mechanism as the slow modulator"
      last_updated: 2026-06-13
      completion_note: "AE-10 gives MECH-369's value-independent slow decommit-friction / engagement-release modulator its own owning roadmap node (the 'no owning node' gap AE-9 surfaced). It is the substrate PRIMITIVE the compulsion cluster (AE-7: MECH-370 composed readout / SD-045 chunk-cache / Q-063 discriminator) composes on top of -- AE-7 now depends_on AE-10. Biology now grounded (Aston-Jones&Cohen 2005 LC-NE adaptive gain, AE-9 lit-pull) and the SD-037-cluster adaptive-gain substrate home adopted in claims.yaml MECH-369. blocker_class v3_substrate because the build is an enrichment of the V3 SD-037 slow-modulator layer (a new loop-release gain channel), but it stays implementation_phase v4 / substrate_conditional: DO NOT build in V3 until an explicit version decision (and the monostrategy-surfacing pull-forward trigger) fires. PROMOTES NOTHING."
---
# Candidate-differentiated affect, expression, anti-collapse, compulsion-risk -- V4 Roadmap

**Registered:** 2026-06-10
**Generation:** v4 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the V4/V5 affect substrate -- the per-candidate
multi-channel affect vector (MECH-359) and everything that hangs off it:
expression as emergent action geometry (MECH-360), the candidate-gradient
episode schema (MECH-361), the soothing modulator (MECH-355), laughter as a
regime-transition discharge plus its crying counterpart (MECH-364 / Q-059),
the compulsion-risk cluster (MECH-369 / MECH-370 / SD-045 / Q-063), and the
developmental-sparsification compass (MECH-362) -- against the V3-era
prerequisites that must land first, with the anti-collapse MAP (ARC-088) as the
governing distinctness rule throughout.

This is a *forward roadmap*, not a closure map: V4 has no affect-substrate
experiments yet, so nodes carry no `owner_exq` and the drift checker stays
dormant against them. The value here is the **readiness gates** -- for each
affect step, exactly which V3-era prerequisites (claims/tracks) must land
before the V4 substrate step is honest to build. `generation: v4` keeps these
nodes out of the V3 closure percentage.

---

## One-line framing

> Affect already exists in REE as a set of partially-independent V3 evaluators
> (harm, relief, safety, drive, blocked-agency, curiosity, commitment-release)
> whose collective job is anti-collapse (ARC-088, already realised in V3). What
> does NOT yet exist is the representational upgrade that makes affect
> *carve*: a per-candidate, multi-channel affect VECTOR (MECH-359). Once
> candidates actually differ (the open V3 blocker) and affect is differentiated
> over them, the same structure becomes visible as behaviour (MECH-360),
> memorable as an event (MECH-361), socially regulable (MECH-355), and
> diagnosable when it goes wrong (compulsion cluster MECH-369/370). This plan
> sequences those steps and pins their V3 readiness gates.

---

## The roadmap (one foundation, then its consumers)

| Step | Node | Claim(s) | Phase leaning | The V3 readiness gate |
|---|---|---|---|---|
| FOUNDATION -- per-candidate affect vector | AE-1 | MECH-359 | V4 (load-bearing) | behavioral_diversity_isolation GAP-A/B (candidates must diverge) + MECH-341/SD-056 + goal_pipeline GAP-4 |
| anti-collapse MAP (governing rule) | AE-2 | ARC-088 | V3 (realised) | distinctness audit over the V3 affect stack; no new substrate |
| expression = action geometry | AE-3 | MECH-360 | V4 | AE-1 built; MECH-041 kept as complement; V5 inference out |
| candidate-gradient episode schema | AE-4 | MECH-361 | V4 | AE-1 built; amends MECH-261 content schema; MECH-094 provenance |
| soothing modulator | AE-5 | MECH-355 | V4-social | V4 other-agent substrate (OBJ-5); MECH-219/SD-012/SD-032e stable |
| laughter discharge + crying analogue | AE-6 | MECH-364, Q-059 | V4/V5 | E3 regime-load readout (ARC-016 check); social substrate for Q-059 |
| slow decommit-friction modulator substrate | AE-10 | MECH-369 | V4 | enrich SD-037 slow-modulator layer with a value-independent loop-release gain channel; grounded by Aston-Jones&Cohen 2005 LC-NE adaptive gain (AE-9) |
| compulsion-risk cluster (composes on AE-10) | AE-7 | MECH-370, SD-045, Q-063 | V4 | AE-10 built; composed readout (MECH-370); SD-034/INV-004/006 firewall |
| developmental sparsification | AE-8 | MECH-362, Q-057 | V4 (compass) | amends ARC-019; affect-specific bridge is the new piece |

---

## What this plan deliberately does NOT pull into V3

- **ARC-088 is NOT a V4 substrate node.** It is `implementation_phase: v3` -- a
  unifying MAP over already-owned V3 affect machinery, substantially realised
  today. AE-2 tracks the ongoing *distinctness-audit duty* (preserve distinct
  affective streams; allow shared consumers, forbid scalar merge), not an
  unbuilt substrate. No node pulls ARC-088 forward; it governs the others.
- **The V3 NARROW range-not-magnitude fact is already DONE and is not MECH-359.**
  V3-EXQ-643a PASS established the cross-candidate-range readiness gate on the
  single-channel modulatory contribution. MECH-359 (AE-1) is the V4/V5
  GENERALISATION to an explicit multi-channel per-candidate representation --
  not a re-statement of the V3 numerical fact. The per-candidate-collapse root
  cause stays owned by `behavioral_diversity_isolation` (GAP-A/GAP-B).
- **No expression / social-signalling / crying substrate in V3.** AE-3 produces
  geometry only; reading it (V5 social inference) is out. MECH-355 and Q-059 are
  V4-social (canonical trigger is an other-agent V3 cannot represent).
- **No compulsion probe in V3.** The five compulsion-risk terms exist piecemeal
  but the unified readout (MECH-370) and the value-independent stickiness
  authority channel (MECH-369) have no substrate; a probe today would be
  vacuous.
- **No developmental pruning substrate in V3.** The one V3-relevant strand
  (convergent-weak-input corollary) is already a diagnostic lens in
  `modulatory_bias_selection_authority_design.md`; do not duplicate it.
- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour.

---

## Source artefacts

| Artefact | Role |
|---|---|
| docs/architecture/candidate_differentiated_affective_gradients.md | MECH-359/360/361 home doc |
| docs/architecture/emotion_as_anti_collapse_architecture.md | ARC-088 unifying map |
| docs/architecture/slow_modulatory_state_and_compulsive_loops.md | MECH-369/370 + Q-063 home doc |
| docs/architecture/laughter_social_load_release.md | MECH-364 + Q-059 home doc |
| docs/architecture/developmental_pruning_and_sparse_memory_cognifold.md | MECH-362 + Q-057 home doc |
| docs/thoughts/2026-06-06_Candidate-differentiated_affective_gradients.md | the seed thought (per-candidate affect must carry cross-candidate range) |
| evidence/planning/behavioral_diversity_isolation_plan.md | GAP-A/GAP-B -- the V3 candidate-collapse blocker AE-1 waits on |
| evidence/planning/modulatory_bias_selection_authority_design.md | V3 single-channel precursor + the developmental diagnostic lens |
| claims.yaml MECH-359/360/361/355/364/369/370/362, ARC-088, SD-045, Q-059/Q-063/Q-057 | the scope claims |

---

## Decision log

- **2026-06-10** -- Plan registered as a V4 forward-roadmap (Tier V4 =
  individual mind, partitioned from V5 social / V6 linguistic). Nodes seeded
  from the candidate-differentiated affect cluster. AE-1 (MECH-359) pinned as
  the load-bearing foundation: blocked on `behavioral_diversity_isolation`
  GAP-A/GAP-B (candidates must diverge before per-candidate affect is
  non-vacuous). ARC-088 placed as the governing distinctness MAP (AE-2), not a
  V4 substrate. Readiness gates pinned per node. `generation: v4` set so the V3
  closure % is unaffected. No claims.yaml edits.
- **2026-06-10** -- Proposed one new bridge claim
  (`affect_developmental_sparsification_bridge`, AE-8) for the prose-only gap:
  applying subtractive developmental sparsification (MECH-362) specifically to
  the affect vector (AE-1) and the candidate-gradient episode store (AE-4) --
  i.e. whether mature affect arbitration uses convergent-weak-channel summation
  vs single-strong-channel authority. MECH-362 names the general principle but
  no claim states the affect-specific application.
- **2026-06-13** -- AE-9 biology-grounding lit-pull DONE (8 entries under
  `evidence/literature/targeted_review_per_candidate_affect`; lit_conf only,
  PROMOTES NOTHING). MECH-359 0.762 (Padoa-Schioppa&Assad 2006 + Rich&Wallis
  2016), MECH-360 0.71 (Niv 2007 + Dael/Mortillaro/Scherer 2012), MECH-364 0.67
  (Seth 2013 + Critchley&Garfinkel 2017, frame-level only), MECH-369 0.56 MIXED
  (Aston-Jones&Cohen 2005 LC-NE adaptive gain, polarity caveat), ARC-088 0.65
  (Pessoa 2008). `lit_pulls_owed` 12->8.
- **2026-06-13** -- Registered node **AE-10** (user-approved follow-up to AE-9):
  the value-INDEPENDENT slow decommit-friction / engagement-release modulator
  substrate MECH-369 needs now has its own owning roadmap node, closing the
  'no owning node' planning gap AE-9 surfaced. AE-7 (compulsion cluster
  MECH-370/SD-045/Q-063) now `depends_on` AE-10 and MECH-369 moved out of AE-7's
  `unblocks_claims` into AE-10's. **claims.yaml MECH-369 amended** (not a new
  claim ID): adopted the LC-NE-style adaptive-gain / engagement-release framing
  (SD-037-cluster amendment carrying explicit loop-release authority) as the
  substrate home, with the Aston-Jones&Cohen 2005 grounding + polarity caveat;
  added `roadmap_node: affect_expression_v4:AE-10`. NO promotion/demotion --
  exp_conf stays 0, MECH-369 stays candidate / v4 / substrate_conditional; the
  build still requires an explicit version decision (DO NOT build in V3). Mirror
  in `docs/architecture/slow_modulatory_state_and_compulsive_loops.md#mech-369`.
