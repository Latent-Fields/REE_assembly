---
closure_plan:
  id: self_attribution
  title: "Self-Attribution Comparator Loop"
  registered: 2026-05-08
  last_updated: 2026-09-04
  scope_claims: [SD-013, SD-029, SD-030, SD-031, ARC-033, ARC-058, MECH-256, MECH-257, MECH-258, MECH-260]
  sibling_plans: [behavioral_diversity_isolation, conversion_ceiling_campaign, sleep_substrate, goal_pipeline]
  nodes:
    - id: "self_attribution:GAP-1"
      title: "ARC-033 vs ARC-058 path arbitration (forensic 445h read)"
      phase: 1
      status: blocked
      severity: high
      owner_exq: V3-EXQ-445h
      unblocks_claims: [ARC-033, ARC-058, MECH-258, MECH-260]
      depends_on: []
      cross_plan_link: ["behavioral_diversity_isolation:GAP-I", "self_attribution:GAP-2"]
      fork: "ARC-033 (independent per-stream comparator) vs ARC-058 (shared-trunk comparator) -- competing architectures, discriminated by the 3-arm ablation OFF / ON_INDEPENDENT / ON_SHARED. Modelled as a FORK annotation, NOT two work-nodes: it is ONE experiment with three arms, so splitting into per-path boxes would inflate the blocked count without reflecting separable work. The arbitration becomes measurable only once the shared monostrategy blocker lifts (see cross_plan_link to behavioral_diversity_isolation:GAP-I)."
      blocking_external: ["conversion_ceiling_campaign:FULLSTACK -- the co-armed full-stack arm demonstrating that the committed-action-diversity conversion survives OFF the reef-bipartite env (the genuine unblock; GAP-1 is not a separate gap from GAP-2 and unblocks WITH it)", "behavioral_diversity_isolation:GAP-I -- the F-dominance committed-selection variance monopoly (MECH-439), the root the superseded monostrategy blocker folds into"]
      resume_condition: "Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include ON_SHARED produced bit-identical metrics between ON_INDEPENDENT and ON_SHARED (harm_a_forward_r2 and mean_score_bias_abs floating-point-identical per seed across both arms) under action_class_entropy=0.0 monostrategy. The architectural arbitration is unmeasurable for the same V_s monostrategy reason as GAP-2 -- both forward models converge to predicting a near-degenerate z_harm_a signal. GAP-1 is not a separate gap from GAP-2. GATE RE-POINTED 2026-08-18 by the steward D-007 adjudication -- plan-frontmatter only, NO status change, the node stays blocked, and blocking_external now names the live gate rather than three that have since cleared. PRIOR GATE TEXT (retained for reconstruction, a citation and NOT a live gate) -- the pre-2026-08-18 blocking_external read sleep_substrate:GAP-1 Phase 1 PASS, MECH-269 V_s monostrategy landing, MECH-307 conjunction architecture = goal_pipeline:GAP-1, all three of which have since cleared or proved satisfied-but-insufficient exactly as recorded in governance_2026_06_09 and the 2026-07-29 status-table reconcile."
      steward_2026_08_18: "GATE RE-POINTED (steward D-007 P1 adjudication, session metaworker-chip-20260817-d007-selfattr-stale-gates; plan-frontmatter + decision-log ONLY -- no claims.yaml edit, no experiment queued, no status change, node stays blocked). D-007 fired P1/strong because EVERY gate node this node named had cleared, making the stated rationale entirely vacuous. Verified against origin/master: sleep_substrate:GAP-1 done; MECH-307 conjunction architecture = goal_pipeline:GAP-1 done; MECH-269 V_s monostrategy landing satisfied 2026-05-17 by V3-EXQ-583 (ARC-065 SP-CEM as main-path default) one day after the gate was written. NONE of that unblocks the node, and the reason was already on record twice: governance_2026_06_09 and the 2026-07-29 status-table reconcile both found SP-CEM necessary-but-insufficient, because 543l / 598b / the 614e autopsy show the candidate pool collapses at the z_world layer UPSTREAM of SP-CEM, so stratified sampling has nothing to stratify. WHY THE FINDING SURVIVED THOSE TWO ADJUDICATIONS: the 2026-07-29 reconcile rewrote the markdown status-table row and the decision log but NOT the frontmatter, and D-007 reads blocking_external + resume_condition -- so the correction existed in prose while the machine-read gate stayed stale for 20 days. This edit carries the ALREADY-MADE adjudication into the frontmatter; it originates no new judgement. Live gate is now behavioral_diversity_isolation:GAP-I (in-progress) -> conversion_ceiling_campaign:FULLSTACK (assembling), matching the 2026-07-29 row verbatim. Prior gate text retained in resume_condition. Standing prohibitions unchanged and re-affirmed: do NOT re-queue the SD-029/MECH-256 retest before FULLSTACK lands, and do NOT plumb SP-CEM harder -- it is already the default and is empirically insufficient."
      last_updated: 2026-08-18
      governance_2026_06_23: "CROSS-PLAN EDGE + FORK ANNOTATION (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). GAP-1's operative gate -- the shared monostrategy / behavioural-diversity blocker -- lived only in blocking_external (which does NOT render as a map edge) and in resume_condition prose ('GAP-1 is not a separate gap from GAP-2'). Added cross_plan_link to behavioral_diversity_isolation:GAP-I (the F-dominance root the monostrategy blocker now folds into) + self_attribution:GAP-2 (its sibling, same gate), so the convergence is drawn. Added a `fork` field making the ARC-033-vs-ARC-058 competing-architecture arbitration explicit (kept as an annotation, not split into two blocked work-nodes -- it is one 3-arm experiment). No status change (stays blocked)."
      governance_2026_06_19: "Stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-445h_2026-06-19 (confirmed, parallel session) reclassified ARC-058 / MECH-258 / MECH-260 at the MANIFEST level (substrate_action=none for all targets): SD-032b non_contributory/substrate_ceiling, MECH-258 supports, MECH-260 non_contributory/substrate_ceiling, ARC-058 non_contributory. That is the SD-032b dACC-analog substrate's OWN ceiling, NOT the ARC-033-vs-ARC-058 path-arbitration measurability gate THIS node tracks -- GAP-1 stays BLOCKED on the same three upstream prerequisites (sleep_substrate:GAP-1 Phase 1 PASS, MECH-269 V_s monostrategy landing in the main agent path, MECH-307 conjunction architecture). The 445h autopsy's claims.yaml epistemic_category recommendations (SD-032b/MECH-260 -> substrate_ceiling) were NOT surfaced in this cycle's reviewed walk and remain to be applied as a separate /governance-or-apply follow-up (manifests already carry the corrections, so scoring is correct). last_updated bumped to acknowledge."
      governance_2026_06_18: "Stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-460e_2026-06-17 (confirmed) reclassified MECH-260 in this node's unblocks set -- the same SD-034 closure-control-plane / foraging-competence substrate family as the 2026-06-06 / 06-04 / 06-03 notes below, NOT the ARC-033 vs ARC-058 path-arbitration measurability gate this node tracks. GAP-1 stays BLOCKED on the same three upstream prerequisites (sleep_substrate:GAP-1 Phase 1 PASS, MECH-269 V_s monostrategy landing in the main agent path, MECH-307 conjunction architecture). last_updated bumped to acknowledge."
      governance_2026_06_09: "Re-adjudicated with GAP-2 (user-directed gap-A substrate re-read). Two of GAP-1's three blocking_external prerequisites are DONE (sleep_substrate:GAP-1 PASS; MECH-307 conjunction architecture = goal_pipeline:GAP-1 done). The third -- 'MECH-269 V_s monostrategy landing [in the main agent path]' -- is the SAME stale-then-insufficient item corrected on GAP-2: ARC-065 SP-CEM became the main-path default 2026-05-17 (V3-EXQ-583) but the V3-EXQ-614e autopsy + 543l show it does not break monostrategy (candidate pool collapses at z_world). So GAP-1's monostrategy prerequisite is re-pointed to the behavioural-diversity substrate stack (GAP-A candidate_summary_source=e2_world_forward + SD-056 + modulatory authority, behaviourally validated via V3-EXQ-660 / 569-lineage), identical to GAP-2's re-pointed gate. GAP-1 'is not a separate gap from GAP-2' (resume_condition) so it unblocks WITH GAP-2 when that stack lands behaviourally. Status stays BLOCKED. No status/claims change."
      governance_2026_06_06: "Stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-621a_2026-06-06 (confirmed) reclassified MECH-260 in this node's unblocks set. 621a is the scaffolded SD-054 onboarding vacuous-pass correction (goal-achievement / foraging-competence substrate-readiness family, no confidence move) -- same class as the 2026-06-04 / 2026-06-03 notes below, NOT the ARC-033 vs ARC-058 path-arbitration measurability gate this node tracks. GAP-1 stays BLOCKED on the same three upstream prerequisites. last_updated bumped to acknowledge."
      governance_2026_06_04: "Stale-since-review acknowledgement only (no status change). The 2026-06-04 *b-cohort autopsy (failure_autopsy_V3-EXQ-460b-461b-464b-466b_2026-06-04) again re-touched MECH-260 (460b non_contributory/substrate_ceiling) -- same goal-achievement/foraging-competence substrate-ceiling family as the 2026-06-03 notes below, NOT the ARC-033 vs ARC-058 path-arbitration measurability gate this node tracks. GAP-1 stays BLOCKED on the same three upstream prerequisites. last_updated bumped to acknowledge."
      governance_2026_06_03: "Closure-drift stale-since-review acknowledgement only (no status change). Flagged because confirmed autopsies post-dating last_updated reclassified MECH-260 (failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03, failure_autopsy_V3-EXQ-603d_2026-06-01), which is in this node's unblocks set. Neither changes GAP-1: it remains BLOCKED on the same three upstream prerequisites (sleep_substrate:GAP-1 Phase 1 PASS, MECH-269 V_s monostrategy landing in the main agent path, MECH-307 conjunction architecture). The MECH-260 reclassifications are goal-pipeline / commitment foraging-competence substrate-ceiling findings, not the ARC-033 vs ARC-058 path-arbitration measurability gate this node tracks. Case 3 (legitimately non-terminal); last_updated bumped to acknowledge."
      governance_2026_05_29: "Drift report freshness bump only; status remains BLOCKED. The three blocking_external prerequisites (sleep_substrate:GAP-1 Phase 1 PASS, MECH-269 V_s monostrategy landing, MECH-307 conjunction architecture) are all unchanged this cycle. The 598b / 543l substrate-ceiling readings from this cycle confirm the monostrategy gate has not lifted on ARC-065 substrate."
      governance_2026_05_30: "IGW-20260530-017 inter-governance-brief routed this node as a methodology-fix (re-queue V3-EXQ-445i three-arm OFF/ON_INDEPENDENT/ON_SHARED). 2026-05-30T07:32Z verification STOPPED before queueing: (a) 445h two-arm forensic re-confirmed at script line 83 + manifest config.conditions; (b) V3-EXQ-567 PASS (2026-05-15 ARC-065 supports) explicitly demonstrates SP-CEM lifts entropy ONLY in ARM_1 (SP-CEM + stratified sampling + ao_std_floor) -- ARM_0 (normal CEM = the default code path 445-cohort scripts use) reproduces the same monostrategy signature 445h shows (selected_action_class_entropy=0.0, single-action action_counts, support_preserving_active_steps=0); (c) use_support_preserving_cem=True default in ree_core/utils/config.py is a naming coincidence -- the actual SP-CEM activation requires the V3-EXQ-567 ARM_1 knob bundle to be plumbed through to the default agent path, which is the work the 2026-05-29 governance note refers to as 'monostrategy gate has not lifted on ARC-065 substrate'. Re-queueing a three-arm methodology fix under default config would reproduce the bit-identical-arms substrate-ceiling signature and waste a runner session. GAP-1 stays BLOCKED on the SAME upstream substrate gates as GAP-2 (sleep_substrate:GAP-1 Phase 1 PASS + MECH-269 V_s landing-in-main-agent-path + MECH-307 conjunction architecture). The /inter-governance-brief workset description for this node should be amended to drop the methodology-fix framing; the node is NOT a re-queueable EXQ at this time. ID PROVENANCE (appended 2026-08-15, docs-only): V3-EXQ-445i was NEVER MINTED and must not be read as an owed successor -- the id was only ever the workset item's PROPOSED label for the re-queue this verification stopped, and no queue entry (current or historical), script, manifest or runner_status entry was ever created under it. The decision not to mint it IS the finding above. Do not queue it; a future arbitration gets a fresh id from /queue-experiment."
      governance_2026_05_31: "Drift report freshness bump only. Today's governance cleared ARC-065 v3_pending + pending_retest_after_substrate via V3-EXQ-614a + V3-EXQ-569d + V3-EXQ-615 PASS convergence (behavioural diversity / SP-CEM stack now substrate-validated). However the three upstream blocking_external prerequisites for GAP-1 are unchanged: sleep_substrate:GAP-1 Phase 1 PASS, MECH-269 V_s monostrategy landing in the main agent path (NOT the same as ARC-065 SP-CEM clearance -- the 445-cohort scripts use the default agent path, not the SP-CEM bundle), MECH-307 conjunction architecture. Status remains BLOCKED. Case 3 in closure-drift terms (legitimately non-terminal pending upstream substrate)."
    - id: "self_attribution:GAP-2"
      title: "SD-029 / MECH-256 retest under full substrate stack"
      phase: 2
      status: blocked
      severity: high
      owner_exq: TBD
      unblocks_claims: [SD-029, MECH-256, ARC-033, SD-013]
      depends_on: ["sleep_substrate:GAP-1", "goal_pipeline:GAP-1"]
      cross_plan_link: ["behavioral_diversity_isolation:GAP-A", "behavioral_diversity_isolation:GAP-I", "conversion_ceiling_campaign:FULLSTACK"]
      blocking_external: ["conversion_ceiling_campaign:FULLSTACK -- the co-armed full-stack arm demonstrating that the committed-action-diversity conversion survives OFF the reef-bipartite env; this is the genuine unblock adjudicated in governance_2026_06_23, NOT the diversity layer on its own", "behavioral_diversity_isolation:GAP-I -- F-dominance committed-selection variance monopoly (MECH-439), still in-progress", "behavioral_diversity_isolation:GAP-B -- Theory 2 / Layer B, E3 scoring collapse of diverse candidates, still partial"]
      steward_2026_08_18: "GATE RE-POINTED (steward D-007 P2 adjudication, same session and same docs-only authority as GAP-1; no status change, node stays blocked). D-007 fired because blocking_external AND resume_condition both named behavioral_diversity_isolation:GAP-A, which is done (V3-EXQ-569i PASS 2026-06-17). THIS IS THE TRAP THE PLAN NAMES BY NAME AND IT WAS NOT WALKED INTO: governance_2026_06_23 records that a naive GAP-A done -> unblock GAP-2 read is the same env-conditional trap the axis_b autopsy caught, because the 2026-06-20 V3-EXQ-625e autopsy showed the 569i conversion is ENV-CONDITIONAL and does not propagate to a threat-engaged candidate pool. The live gate is therefore conversion_ceiling_campaign:FULLSTACK (assembling), with behavioral_diversity_isolation:GAP-I (in-progress) and :GAP-B (partial) the outstanding upstream layers -- exactly what cross_plan_link has drawn since 2026-06-23 and what the 2026-07-29 row states. Both fields were re-pointed, not just blocking_external: the resume_condition clause RE-POINTED GATE -- resume once ... GAP-A/GAP-B land ... was itself a live gate assertion naming a cleared node. Prior gate text retained in resume_condition. NO experiment queued -- a retest now would re-derive the known monostrategy non_contributory result."
      last_updated: 2026-08-18
      governance_2026_06_23: "RE-ADJUDICATE vs GAP-A=done + EDGE DRAW (session closure-map-enhance-20260623T043407Z; plan-frontmatter only, NO claims.yaml/queue change). The re-pointed gate (behavioral_diversity_isolation:GAP-A/GAP-B behaviourally-validated) has PARTIALLY fired: GAP-A is now status=done (V3-EXQ-569i PASS 2026-06-17, committed-action diversity reaches behaviour). BUT this does NOT unblock GAP-2: the 2026-06-20 V3-EXQ-625e autopsy showed the 569i conversion is ENV-CONDITIONAL and does NOT propagate to a threat-engaged candidate pool -- a naive 'GAP-A done -> unblock GAP-2' read is the same env-conditional trap the axis_b autopsy caught. The genuine unblock is the conversion_ceiling_campaign FULLSTACK arm demonstrating conversion survives off the reef-bipartite env. The operative gate lived only in blocking_external (non-rendering); added cross_plan_link to behavioral_diversity_isolation:GAP-A (now done), :GAP-I (the F-dominance root), and conversion_ceiling_campaign:FULLSTACK (the real unblock) so the dependency is drawn. Status stays blocked. NO experiment queued (a retest now would re-derive the env-conditional ceiling)."
      resume_condition: "RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PATH DEFAULT 2026-05-17 (ree-v3 CLAUDE.md 'ARC-065 SP-CEM Main-Path Landing'; six HippocampalConfig + from_dims defaults flipped use_support_preserving_cem/stratified_elites True + ao_std_floor 0.2; validated V3-EXQ-583 default-wiring equivalence 20260517T092510Z). Taking the gate literally would unblock GAP-2 now -- but that is WRONG: SP-CEM-in-main-path is necessary-but-NOT-sufficient and re-issuing the SD-029/MECH-256 retest on it would reproduce the known monostrategy non_contributory result. Empirical proof of insufficiency: sleep_substrate:GAP-2 records 'V3-EXQ-543l ran 2026-05-26 with [SP-CEM] live and still collapsed to inert monomodal equilibrium'; the V3-EXQ-614e autopsy located the real bottleneck UPSTREAM of CEM scoring -- all K candidates collapse to identical z_world after one E2 world-forward step (cand_world_pairwise_dist=0.0000), so SP-CEM stratified sampling cannot break monostrategy. The fix is the GAP-A candidate_summary_source=e2_world_forward re-sourcing (landed 2026-06-07, opt-in; readiness V3-EXQ-649 PASS 2026-06-07) + SD-056 e2 action-conditional divergence + the modulatory-bias-selection-authority gate -- the SAME behavioural-diversity stack the sd_037_axis_b chain and arc_062 GAP-B now wait on. RE-POINTED GATE, updated 2026-08-18 -- resume once conversion_ceiling_campaign:FULLSTACK demonstrates that a BEHAVIOURALLY-validated (not readiness-only) non-monostrategy policy generates balanced agent-vs-env event distributions in the MAIN agent path OFF the reef-bipartite env, with behavioral_diversity_isolation:GAP-I (in-progress) and behavioral_diversity_isolation:GAP-B (partial) the outstanding upstream layers, and the V3-EXQ-660 MECH-341 committed-class diversity + 569-lineage falsifier as the behavioural readout. PRIOR GATE TEXT (retained for reconstruction, a citation and NOT a live gate) -- the pre-2026-08-18 wording of this gate and of blocking_external named behavioral_diversity_isolation:GAP-A/GAP-B behaviourally-validated in the main agent path, and behavioral_diversity_isolation:GAP-A then went done on the V3-EXQ-569i PASS of 2026-06-17 WITHOUT unblocking this node, exactly as recorded in governance_2026_06_23 where the 2026-06-20 V3-EXQ-625e autopsy found that conversion ENV-CONDITIONAL. Only then re-issue the SD-029/MECH-256 retest via /queue-experiment WITH that full stack enabled (candidate_summary_source=e2_world_forward + SP-CEM + modulatory authority). Do NOT 'plumb SP-CEM harder' -- it is already the default and is empirically insufficient. See 2026-06-09 re-adjudication note + sleep_substrate:GAP-2 (identical gate) + behavioral_diversity_isolation:GAP-A."
      governance_2026_06_09: "Re-adjudicated the 2026-05-16 monostrategy gate against the landed GAP-A candidate-diversity substrate (user-directed). FINDING: the literal precondition (SP-CEM in main agent path) was satisfied 2026-05-17 (V3-EXQ-583), one day after the gate was written, so the gate had been silently stale for ~3 weeks. But the gate's INTENT (break monostrategy so SD-029 C2/C3 are measurable) is NOT met by SP-CEM alone -- 543l/598b/614e prove the candidate pool collapses at the z_world layer upstream of SP-CEM. Re-pointed the gate to the behavioural-diversity substrate stack (GAP-A e2_world_forward + SD-056 + modulatory authority), behaviourally-validated, which is the same live frontier the sd_037_axis_b chain + arc_062 GAP-B + sleep_substrate:GAP-2 converge on. NO experiment queued (a retest now would be vacuous); NO claims.yaml/scoring change. GAP-1 carries the same correction (its blocking_external 'MECH-269 V_s monostrategy landing in the main agent path' is the same re-pointed item)."
    - id: "self_attribution:GAP-3"
      title: "MECH-257 dual-function 3-arm ablation re-queue"
      phase: 3
      status: blocked
      severity: medium
      owner_exq: TBD
      unblocks_claims: [MECH-257, MECH-094]
      depends_on: ["self_attribution:GAP-1", "self_attribution:GAP-2"]
      last_updated: 2026-06-25
      governance_2026_06_04: "Stale-since-review acknowledgement only (no status change). Flagged because the 2026-06-04 *b-cohort autopsy (failure_autopsy_V3-EXQ-460b-461b-464b-466b_2026-06-04) reclassified MECH-094 (466b non_contributory/substrate_ceiling), which is in this node's unblocks set. That is a goal-achievement substrate-ceiling result on the closure/residue-discharge path; MECH-094 itself remains stable. It does not change GAP-3, which stays BLOCKED on its upstream prerequisites (self_attribution:GAP-1/GAP-2). last_updated bumped to acknowledge."
      governance_2026_06_25: "Stale-since-review acknowledgement only (no status change; session governance-cycle-20260625T0420Z). Re-flagged for the SAME reason as governance_2026_06_04: a closure/residue-discharge autopsy (now failure_autopsy_V3-EXQ-466d_2026-06-24, applied by governance-cycle-20260624T2249Z) reclassified MECH-094 -> non_contributory and DROP-TAGGED it from the scored set precisely to PROTECT its stable status (conf 0.868). MECH-094 itself is unweakened. It does not change GAP-3, which stays BLOCKED on its upstream prerequisites (self_attribution:GAP-1/GAP-2) -- those are unmet, so the MECH-257 dual-function 3-arm ablation re-queue cannot proceed regardless of the MECH-094 reclassification. last_updated bumped to acknowledge."
    - id: "self_attribution:GAP-4"
      title: "Nociceptive-comparator lit-pull (PAG/RVM/ACC)"
      phase: 4
      status: done
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-256, SD-029]
      depends_on: []
      last_updated: 2026-05-17
      completion_note: "Lit-pull complete 2026-05-17. Two new entries written: (1) De Preter & Heinricher 2024 (Trends in Neurosciences, PMID 38749825) in targeted_review_connectome_mech_256 -- mixed 0.74 -- establishes that PAG/RVM implements CONTEXTUAL PRECISION-GATING via ON/OFF cells (behavioural-state gating, opioid-mediated), NOT efference-copy comparator. (2) Seymour 2019 (Neuron, PMID 30897355) in targeted_review_sd_029 -- mixed 0.61 -- frames pain as precision-weighted prediction-error signal for RL/control; computationally convergent with MECH-256 at Marr level 2 but distinct at implementation level. ARCHITECTURAL VERDICT: OPTION A applies (comparator-class behaviour confirmed on nociceptive streams). Existing Lalouni 2020 entry (SD-029 corpus) already established the behavioural evidence (40% self-pain attenuation). PAG/RVM is NOT the substrate for the efference-copy comparator -- it implements a parallel precision-gating layer (contextual, motivational). The MECH-256 per-step efference-copy comparator operates at spinal dorsal horn / somatosensory cortex level (corticospinal collateral corollary discharge). SD-029 inherits MECH-256's lit_conf. No separate design doc needed -- the comparator metaphor on z_harm_s is NOT over-specified, but an architectural note should distinguish E2_harm_s (efference-copy, spinal/cortical) from PAG/RVM contextual gain control (parallel, not competing). MECH-256 lit_conf post-pull: 0.867 (mixed entries push it down slightly from 0.87 baseline but the existing supports dominate). SD-029 lit_conf: 0.858."
    - id: "self_attribution:GAP-5"
      title: "SD-030 z_self materialisation (V4)"
      phase: 5
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [SD-030]
      depends_on: []
      cross_plan_link: ["self_model_v4:SELF-2"]
      last_updated: 2026-08-15
      governance_2026_08_15: "SPLIT: SD-031 REMOVED from this node into the new self_attribution:GAP-6 (plan-frontmatter only; NO claims.yaml change, NO experiment queued, no status change to any pre-existing node). This node was registered 2026-05-08 bundling SD-030 (z_self) and SD-031 (z_world) as one V4-deferred placeholder, and was the only node in this plan never revisited since registration. SD-031 was RESCOPED v4 -> v3 on 2026-06-06 (claims.yaml SD-031 notes: implementation_phase v3, v3_pending true; substrate E2WorldForward landed the same day) and this node was never updated to match, so the plan that OWNS SD-031 went on calling it V4-deferred for ten weeks while four other artefacts called it V3 -- see GAP-6's own note for the full reconciliation. SD-030 alone is correctly V4 and this node keeps it. Added cross_plan_link to self_model_v4:SELF-2 ('Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)'), which is the node that actually owns the SD-030 build; the edge previously existed only one-way (SELF-2 names SD-030 and this plan in prose, nothing pointed back), so the V3->V4 hand-off did not render as a map edge."
    - id: "self_attribution:GAP-6"
      title: "SD-031 z_world causal-footprint comparator: V3 discriminative validation"
      phase: 6
      status: blocked
      severity: medium
      owner_exq: null
      unblocks_claims: [SD-031]
      depends_on: []
      cross_plan_link: ["self_attribution:GAP-2", "conversion_ceiling_campaign:FULLSTACK", "multi_agent_ecology_v5:MAE-3", "self_model_v4:SELF-2"]
      blocking_external: ["world_dim >= 128 in the validation config (E2WorldForward hard-asserts this; the dim=32 default yields a vacuous zero attribution gap)", "ARC-065 behavioural diversity active in the main agent path -- balanced agent-caused vs externally-caused world events; the SAME re-pointed diversity gate GAP-2 waits on (behavioral_diversity_isolation:GAP-I -> conversion_ceiling_campaign:FULLSTACK)"]
      resume_condition: "Both halves of the claims.yaml SD-031 evidence_quality_note gate must hold before the discriminative/attribution arm is queued: world_dim >= 128 AND behavioural diversity live in the main agent path. The claim registry states this as a prohibition, not a preference -- 'running before both halves are in place reproduces the dim=32 + monostrategy + (formerly) unbuilt-comparator confound' -- so this node is genuinely blocked and NOT an open queueable item, despite the substrate being built and the smoke being clean. Do NOT read the passing activation smoke as licence to queue: it was a single-config activation check, not the discriminative arm. The behavioural-diversity half is the same gate as GAP-2, so GAP-6 unblocks WITH GAP-2; the world_dim half is a config knob and is satisfiable the moment the diversity half lands. GATE RE-POINTED 2026-08-18 by the steward D-007 adjudication -- plan-frontmatter only, NO status change, the node stays blocked, and the diversity half of blocking_external now names only the outstanding chain. PRIOR GATE TEXT (retained for reconstruction, a citation and NOT a live gate) -- that half previously read behavioral_diversity_isolation:GAP-A/GAP-I -> conversion_ceiling_campaign:FULLSTACK, and behavioral_diversity_isolation:GAP-A has since gone done WITHOUT unblocking anything, for the env-conditional reason recorded in governance_2026_06_23 on GAP-2. [2026-09-04 governance amend, user decision, cycle governance-20260904-1347: the behavioural-diversity half is CLEARED FOR THE COMPARATOR-ONLY READOUT by a construction-balanced design (RandomPolicy collection with balanced agent-caused vs externally-caused events, scored offline -- V3-EXQ-995 PASS, V3-EXQ-1001 FAIL/mixed, confirmed failure_autopsy_V3-EXQ-1001_2026-09-04); a comparator-only discriminative arm built that way MAY be queued. The gate still blocks any design reading the residual from the LIVE agent loop until ARC-065 lands. Node stays blocked: no owner_exq yet; the 1001 successor portfolio is chipped by governance.]"
      steward_2026_08_18: "GATE RE-POINTED (steward D-007 P2 adjudication, same session and same docs-only authority as GAP-1/GAP-2; no status change, node stays blocked). Notable because this node was created only 2026-08-15 and already named a cleared gate: its diversity half was written as the chain behavioral_diversity_isolation:GAP-A/GAP-I -> conversion_ceiling_campaign:FULLSTACK, and GAP-A had been done since 2026-06-17 -- i.e. the node inherited GAP-2 gate text that was already stale when it was copied. That is not a new blocker, it is the same 20-day frontmatter lag as GAP-1/GAP-2, propagated forward one hop. GAP-A dropped from the chain; the outstanding chain GAP-I -> FULLSTACK is unchanged, and the world_dim >= 128 half is untouched and still unmet-by-default. Both halves of the claims.yaml SD-031 evidence_quality_note prohibition therefore still hold, so GAP-6 remains genuinely blocked and NOT an open queueable item -- the passing activation smoke is still not licence to queue the discriminative arm. Prior gate text retained in resume_condition."
      last_updated: 2026-09-04
      governance_2026_08_15: "NEW NODE, split out of GAP-5 (plan-frontmatter only; NO claims.yaml change, NO experiment queued, no pre-existing node's status changed). WHY: SD-031 is v3_pending V3 work whose ONLY owning closure node was GAP-5, and GAP-5 is `deferred` -- which generate_closure_snapshot.py DEFERRED_STATUSES excludes from the V3 progress denominator outright. A live V3 claim therefore had no V3 closure path and was invisible to the closure accounting: not counted done, not counted remaining, not visible as a gap. SIX artefacts were consulted and FIVE agree SD-031 is V3, against GAP-5 alone: (1) claims.yaml SD-031 -- implementation_phase v3, v3_pending true, live_status reading candidate/v3_pending, with an explicit rescope note dated 2026-06-06 ('Rescoped v4 -> v3 ... the implementation_phase field is a prediction, not a permission gate'); (2) self_model_v4_plan.md 'What this plan deliberately does NOT pull into V3' -- '**SD-031 (world-stream self-attribution) stays a V3 item.** It is the V3-tractable comparator and is NOT pulled into this V4 plan as work ... Only SD-030 (the z_self motor-proprioceptive stream) is V4'; (3) self_model_v4:SELF-2 readiness_gate -- 'V3 BEGINNING present: self-attribution on the z_world causal-footprint stream runs (SD-031, V3-pending)'; (4) multi_agent_ecology_v5:MAE-3 readiness_gate -- 'the self-vs-world comparator (SD-031 / MECH-256) is the V3 BEGINNING; the self-vs-OTHER comparator is the V5 extension'; (5) substrate_queue.json sd_id SD-031 -- status `implemented`, unblocks_claims [MECH-256, zworld-granularity-retest], i.e. a BUILT substrate awaiting a retest, which is not the shape of a V4 placeholder. SUBSTRATE STATE (not a design gap): E2WorldForward built 2026-06-06 at ree-v3/ree_core/predictors/e2_world.py, config LatentStackConfig.use_e2_world_forward (default False); activation smoke the same day at world_dim=128 gave world_forward_r2 0.969 with a correct attribution gap (self-caused residual ~2.0 vs externally-caused ~22.6); failure_autopsy_V3-EXQ-783_2026-07-18 then validated the instrument (diagnostic_no_direction/instrument_validated_cause_discriminated). What is missing is only the discriminative arm under the two-part gate above. CLOSURE EFFECT, stated because it is visible on the dashboard, and MEASURED by A/B regeneration of generate_closure_snapshot.py against origin/master with and without this split (not estimated): 72.6% -> 71.9%, remaining 31 -> 32, done unchanged at 62. This ADDS one blocked node (weight 0.1) to the V3 denominator. That is the point -- the previous figure was overstated by hiding a real V3 item inside a deferred V4 node, and surfacing it is a correction, not a regression. NOTE for anyone reconciling against the committed dashboard: docs/closure_dashboard.md was last generated 2026-08-13 and reads 71.0% / 92 non-deferred / 59 done; that baseline is stale (other plans have since landed work), which is why the A/B above was run rather than differencing against the committed number."
---
# Self-Attribution Comparator Loop Plan

**Registered:** 2026-05-08
**Status:** active
**Scope:** the self-attribution comparator pipeline -- the layer that
turns reafferent latent streams into an agency signal. Covers SD-003
(superseded predecessor), MECH-256 (general single-pass forward-model
comparator, stream-agnostic), SD-029 (concrete z_harm_s instantiation),
MECH-257 (dual-function single-substrate E2: comparator vs evaluator,
controller-gated), SD-013 (interventional training for E2_harm_s),
ARC-033 (independent-per-stream E2_harm_s), ARC-058 (shared
HarmForwardTrunk + per-stream HarmForwardHead, COMPETING with ARC-033),
MECH-258 (precision-weighted pain PE, E2_harm_a forward), MECH-260 (dACC
bias suppression, shared with the dACC bundle), SD-031 (z_world
causal-footprint, **V3** since the 2026-06-06 rescope -- substrate built,
validation gated), and the V4-deferred per-stream successor SD-030
(z_self motor-proprioceptive).

**Generation split (reconciled 2026-08-15).** Self-attribution spans three
generations and each tier now has exactly one owning node:

| Stream | Claim | Generation | Owning node |
|---|---|---|---|
| z_harm_s (harm) | SD-029 / MECH-256 | **V3** | `self_attribution:GAP-1/2/3` |
| z_world (causal footprint) | SD-031 | **V3** | `self_attribution:GAP-6` |
| z_self (motor-proprioceptive) | SD-030 | V4 | `self_attribution:GAP-5` -> `self_model_v4:SELF-2` |
| self-vs-**OTHER** | MECH-095 / MECH-099 | V5 | `multi_agent_ecology_v5:MAE-3` |

The V3 rows are **not** multi-agent-dependent: the comparator's contrast
class is *self-caused vs environment-caused*, and the environment side is
supplied by the scheduled-external-hazard curriculum, not by another agent.
Only the fourth row -- attributing causation to a *structurally distinct
other* -- needs a multi-agent substrate, and it is already held in the V5
tier (`generation: v5`, out of the V3 closure percentage). See the
[2026-08-15 decision-log entry](#2026-08-15---is-self-attribution-multi-agent-dependent-no-for-the-v3-tier-and-the-multi-agent-part-is-already-v5)
for the adjudication.

This plan is the durable resume-point for self-attribution work across
sessions. When work pauses to handle adjacent paths (e.g. sleep
substrate, MECH-307 conjunction architecture, V_s monostrategy), the
deviation is logged in the [Decision log](#decision-log) below with a
resume condition.

---

## One-line framing

> SD-003 cost 28 FAILs over six months. The successor layer (MECH-256
> single-pass comparator with SD-029 as the V3 instantiation) is
> wired end-to-end on z_harm_s, but every empirical attempt to
> distinguish self-caused from externally-caused harm has been
> reclassified non_contributory because the policy is monomodal and
> the substrate-level architectural choice (per-stream vs shared
> trunk) has not been arbitrated.

The comparator scaffolding is in place: ARC-033 forward model passes
C1 (forward_r2 ~0.998, EXQ-330a / EXQ-166e), interventional training
(SD-013) is implemented and supported by EXQ-353, the env-level
balanced-hazard curriculum (SD-029 implementation_note) shipped
2026-04-21, and the dACC bundle (MECH-258 + MECH-260) consumes the
comparator output.

What is missing:

1. The **architectural arbitration** between ARC-033 (independent per-
   stream forward models) and ARC-058 (shared HarmForwardTrunk +
   per-stream heads). V3-EXQ-445 was designed as the three-arm
   ablation for this; its result interpretation is Phase 1 below.
2. **Single-pass comparator validation on z_harm_s under balanced events**
   (SD-029 / MECH-256 C2 + C3). Five consecutive runs (EXQ-433 / 433a /
   433b / 470 / 433d / 433f / 537 / 537a / 523b) reclassified
   non_contributory under V_s monostrategy. Gated on MECH-269 V_s landing
   AND on MECH-204 sleep-substrate Phase 1 (per substrate_queue
   unblocks_claims).
3. **MECH-257 dual-function controller gating** (one E2_x substrate read
   in two modes, comparator vs evaluator, arbitrated by a controller
   signal). EXQ-452 reclassified non_contributory under the same V_s
   substrate gap. Phase 3 below.

The gap is not "more design"; the gap is the architectural arbitration
(Phase 1) and the substrate readiness (Phase 2 + Phase 3) that the
plans of record for sleep and goal pipeline are jointly unblocking.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| 2026-04-18 SD-003 supersession decision (claims.yaml SD-003 supersession_note) | Closes the two-pass counterfactual era; opens the single-pass comparator era; promotes MECH-256 + SD-029 |
| 2026-04-18 three-pull literature synthesis | Frith 2000 + Shergill 2003 + Blakemore 1998 + Haggard 2017 (single-pass comparator); Mattar & Daw 2018 + Diba & Buzsaki 2007 + Dragoi & Tonegawa 2011 + Kay 2020 + Pezzulo 2014 + Shenhav 2013/2016 (dual-function single-substrate evaluator); Horing & Buchel 2022 (shared-trunk AIC unsigned aversive PE) |
| [docs/architecture/self_attribution_per_stream.md](../../docs/architecture/self_attribution_per_stream.md) | Per-stream topology: SD-029 (V3 z_harm_s), SD-031 (**V3** z_world -- rescoped from V4 on 2026-06-06), SD-030 (V4 z_self); MECH-256 stream-agnostic mechanism; MECH-257 dual-function gating |
| [docs/architecture/sd_013_e2_harm_s_interventional_training.md](../../docs/architecture/sd_013_e2_harm_s_interventional_training.md) | Interventional training spec for E2_harm_s |
| [docs/architecture/sd_032_cingulate_integration_substrate.md](../../docs/architecture/sd_032_cingulate_integration_substrate.md) | dACC bundle consumer of MECH-258 precision-weighted PE; MECH-260 bias-suppression spec |
| ree-v3 V3-EXQ-445 / 445a / 445b / 445c / 445h scripts | Three-arm ablation: dACC-OFF vs dACC-ON-independent (ARC-033) vs dACC-ON-shared-trunk (ARC-058) |
| EXQ-433 / 433a / 433b / 470 / 433d / 433f / 537 / 537a / 523b governance reads (SD-029 evidence_quality_note) | Five consecutive non_contributory under V_s monostrategy; substrate-ceiling pattern |
| EXQ-452 governance read (MECH-257 evidence_quality_note) | Dual-function gated-readout cannot resolve under monomodal policy |
| substrate_queue.json MECH-204 entry unblocks_claims `[Q-041, Q-042, INV-049, SD-029, MECH-256, MECH-111, SD-049]` | Sleep-substrate Phase 1 is the upstream gate for SD-029 / MECH-256 retest |

---

## Existing substrate (do not duplicate)

Wired and behaving correctly:

| Component | Location | Status |
|---|---|---|
| ARC-033 E2_harm_s forward model | `ree-v3/ree_core/predictors/e2_harm_s.py` (`E2HarmSForward`) | C1 forward_r2 ~0.998 confirmed (EXQ-330a, EXQ-166e PASS 6/6) |
| SD-013 interventional training for E2_harm_s | `ree-v3/ree_core/predictors/e2_harm_s.py` `compute_interventional_loss` | EXQ-353 PASS supports; provisional |
| MECH-258 E2_harm_a forward model + precision-weighting | `ree-v3/ree_core/predictors/e2_harm_a.py` (`E2HarmAForward`); `ree_core/cingulate/dacc.py` PE bundle | EXQ-445h C1 wins 2/3 seeds; first clean supports |
| MECH-260 dACC bias-suppression FIFO | `ree-v3/ree_core/cingulate/dacc.py` `record_action`/`forward` suppression channel | EXQ-445h C3 wins 3/3 seeds |
| ARC-058 shared HarmForwardTrunk + HarmForwardHead | `ree-v3/ree_core/latent/stack.py` (`HarmForwardTrunk`, `HarmForwardHead`); E2_harm_a/E2_harm_s constructor switch via `shared_trunk` | scaffolded; arbitration via V3-EXQ-445 three-arm ablation pending |
| SD-029 balanced-hazard curriculum | ree-v3 CausalGridWorldV2 `scheduled_external_hazard_*` knobs (2026-04-21); info-dict `external_hazard_event_count` | env substrate landed; behavioural test blocked by V_s monostrategy |
| Comparator residual readout | `ree-v3/ree_core/agent.py` self-attribution path consuming E2_harm_s reafferent residual | end-to-end wired; awaits balanced events |

---

## Gap inventory

Six gaps, ordered by leverage (GAP-6 added 2026-08-15 by splitting SD-031
out of GAP-5). Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | ARC-033 vs ARC-058 architectural arbitration unresolved (independent-per-stream vs shared-trunk + heads); only V3-EXQ-445h has produced a clean partial read | load-bearing | ARC-033 retire-or-confirm; ARC-058 retire-or-promote; MECH-257 single-substrate philosophy |
| **GAP-2** | SD-029 single-pass C2/C3 unmeasurable while policy is monomodal (5 consecutive non_contributory: EXQ-433/433a/433b/470/433d/433f/537/537a/523b) | high | MECH-256 empirical promotion; SD-029 candidate -> provisional; INV-049/Q-041/Q-042 confidence on the comparator side |
| **GAP-3** | MECH-257 dual-function controller-gated readout untestable under monomodal policy (EXQ-452 non_contributory) | high | MECH-257 falsification one way or the other; arbitrates "two substrates per stream" parameter doubling |
| **GAP-4** | Q1: nociceptive-transfer caveat -- comparator literature evidences mechanism on sensorimotor / tactile / force streams; extension to nociceptive streams plausible (PAG/RVM descending modulation shares efference-copy structure) but not directly demonstrated; main mapping risk | medium | architectural confidence in MECH-256 generalisation across reafferent streams |
| **GAP-5** | SD-030 (z_self) is a V4-deferred placeholder; the motor-proprioceptive stream is not testable until z_self is a first-class latent with its own forward model | low (V4 deferred) | per-stream topology completeness; not in V3 scope |
| **GAP-6** | SD-031 (z_world causal-footprint comparator) is **V3** and its substrate is BUILT (`E2WorldForward`, 2026-06-06) with a clean activation smoke, but the discriminative arm is un-run: it needs `world_dim >= 128` **and** balanced agent-vs-env world events, and the claim registry forbids running it before both hold | medium | SD-031 candidate -> provisional; completes the V3 half of the per-stream topology; supplies the "V3 BEGINNING" that `self_model_v4:SELF-2` and `multi_agent_ecology_v5:MAE-3` both build onto |

---

## Sequenced plan

Six phases. Each phase is small, verifiable, and unblocks at least one
downstream claim. Phases are ordered by what each unblocks. Where work
depends on adjacent non-self-attribution paths (sleep substrate Phase 1,
goal pipeline dACC bundle, V_s monostrategy fix), that is called out
inline and tracked as the upstream gate in the
[Status table](#status-table).

### Phase 1: V3-EXQ-445 three-arm ablation result interpretation (GAP-1)

**Status (2026-05-11): blocked on same substrate gates as Phase 2.**
Forensic read of EXQ-445h surfaced that the arbitration data does not
exist in any 445-iteration, and the bit-identical pattern in the
iterations that did include ON_SHARED is the same V_s monostrategy
substrate ceiling that has been reclassifying the SD-029 cohort
non_contributory. See [Decision log -- 2026-05-11](#2026-05-11-gap-1-monostrategy-inversion)
below.

ARC-033 and ARC-058 are registered as competing architectural
commitments. V3-EXQ-445 was designed as the three-arm ablation that
arbitrates them: dACC-OFF (baseline) vs dACC-ON-independent (ARC-033
path) vs dACC-ON-shared-trunk (ARC-058 path).

**Two findings invert the original Phase 1 plan:**

1. EXQ-445h is two-arm only -- `CONDITIONS = ["OFF", "ON_INDEPENDENT"]`
   ([v3_exq_445h_sd032b_dacc_reef.py:83](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_445h_sd032b_dacc_reef.py)).
   The ARC-058 arm was silently dropped after EXQ-445b. EXQ-445a/c/d/f/g/h
   all run `use_shared_harm_trunk=False` hard-coded. The "latest in the
   series" that the plan keyed on has no shared-trunk data.
2. The earlier three-arm runs (EXQ-445 + EXQ-445b two timestamps) show
   floating-point-identical metrics between ON_INDEPENDENT and ON_SHARED
   per seed:
   - seed=42: harm_a_forward_r2=0.9371525719237495,
     mean_score_bias_abs=3374526.2593920277 (both arms)
   - seed=7:  harm_a_forward_r2=0.918056702809114,
     mean_score_bias_abs=954306.9917550903 (both arms)
   - seed=13: harm_a_forward_r2=0.8406720867479271,
     mean_score_bias_abs=86130.61802364363 (both arms)

   The two architectures (ARC-033 path uses `ResidualHarmForward`;
   ARC-058 path uses `HarmForwardTrunk + HarmForwardHead`) are genuinely
   different module trees with different parameter counts. The only way
   to produce floating-point-identical training metrics is for the
   architectural distinction to not actually exercise -- which under
   `action_class_entropy=0.0` across every seed in every condition is
   exactly what monostrategy predicts: trajectories are deterministic
   given seed alone, both forward models consume the same near-degenerate
   z_harm_a stream, and both trivially fit it. The original EXQ-445
   pass-criteria `c4_arc033_vs_arc058_diagnostic` actually recorded
   `mean_r2_independent == mean_r2_shared == 0.8986271204935968` exactly;
   the "winner_suggested_by_forward_r2: ARC-058_shared" tag was
   meaningless because the test was non-discriminative.

GAP-1 is therefore not a separate gap from GAP-2. The architectural
arbitration requires balanced agent-vs-env event distributions for the
two architectures to produce different forward_r2 readouts. Under V_s
monostrategy that distribution does not exist, and the bit-identicality
is the substrate-ceiling signature.

**Revised Phase 1 deliverables (post-2026-05-11):**

1. **Reclassify EXQ-445 + EXQ-445b ARC-033/ARC-058 entries**:
   evidence_direction_per_claim for ARC-033 and ARC-058 -> non_contributory
   with evidence_quality_note pointing at action_class_entropy=0.0 +
   bit-identical-across-arms signature. MECH-258 / MECH-260 / SD-032b
   reads are kept as recorded (those criteria are about within-arm
   behaviour, not cross-arm arbitration) but inherit the same
   substrate-ceiling caveat -- they reflect what an untrained-policy
   monostrategy run can fit, not what the dACC bundle does when the
   policy actually exercises both event classes.
2. **Resume condition (same as GAP-2)**: when sleep_substrate_plan Phase 1
   PASSes AND MECH-269 V_s lands AND MECH-307 conjunction architecture
   lands, queue a fresh three-arm ablation (NOT a 445-letter iteration --
   the 445h template is two-arm) on the full substrate stack. Acceptance
   criteria identical to Phase 2 (balanced events; C2 partial attenuation;
   C3 SNR) PLUS the cross-arm comparator: shared-trunk forward_r2 must
   differ from independent-per-stream forward_r2 by more than the
   per-seed run-to-run noise floor to be discriminative.
3. **Caveat (preserved from original plan)**: SD-032b does_not_support
   running may stem from substrate gaps not yet inventoried
   (previous-valence-on-unexpected, MECH-307 conjunction architecture,
   sleep substrate). Per the 2026-05-08 governance note in MECH-260
   evidence_quality_note: do NOT advance toward demote until the
   candidate-gap inventory broadens.

Phase 1 originally claimed to be **not gated** on Phase 2 / Phase 3
substrate work because it read a result that had already been collected.
The 2026-05-11 finding inverts that: the result that was collected does
not actually contain arbitration data, and the substrate gaps that block
Phase 2 also block Phase 1.

Acceptance (updated): ARC-033 + ARC-058 entries in claims.yaml +
substrate_queue retain their candidate status with evidence_quality_note
recording the substrate-ceiling finding. The architectural verdict is
deferred to the same resume window as Phase 2.

### Phase 2: MECH-256 single-pass comparator validation under balanced events (GAP-2)

The C2 + C3 measurements that SD-029 + MECH-256 need (residual
attenuation on self-caused vs externally-caused harm + approach-event
SNR) cannot be made while the policy is monomodal. EXQ-433 / 433a /
433b / 470 / 433d / 433f / 537 / 537a / 523b form a five-instance
substrate-ceiling pattern: in each, the C0 trials-sufficient gate fails
because the agent runs in either "exploit only" or "avoid only" mode
and produces near-zero counts on the opposite class. EXQ-433f
(2026-05-08 diagnose-errors) added a fifth confirmation that even
SD-050 reef enrichment (`reef_enabled=True`, `n_reef_patches=3`,
`hazard_food_attraction=0.7`) does not break monostrategy at 8x8 scale.

**Upstream gates** (from substrate_queue MECH-204 unblocks_claims +
governance 2026-04-22 hold):

- **MECH-204 sleep-substrate Phase 1** (precision recalibration consumer
  in [sleep_substrate_plan.md](sleep_substrate_plan.md) Phase 1).
  Sleep_substrate_plan Phase 4 (MECH-273 real replay-derived training
  targets) writes back to E2_harm_s using SD-003 / SD-029 causal_sig as
  evidence -- the self-attribution loop is the **consumer** of the sleep
  loop's writeback. The relationship is bidirectional: sleep needs SD-029
  to train its writeback target, and SD-029 needs sleep recalibration to
  break the V_s monostrategy that makes its events unbalanced.
- **MECH-269 V_s landing** (waking-side V_s invalidation runtime
  Phase 1-3 already landed 2026-04-22 -- 2026-04-24; what is missing is
  the V_s-driven action selection coupling that produces balanced
  agent-vs-environment event distributions).
- **MECH-307 anticipatory-affect conjunction architecture** (added to
  substrate_queue priority=1 2026-05-08; gates the goal-pipeline
  commit-chain that, when fixed, may break monostrategy upstream of V_s).

Deliverables:

1. **Resume condition.** When sleep_substrate_plan Phase 1 PASS landed
   (post-REM `_running_variance` measurably moved toward zero-point
   reference in ON arm) AND MECH-269 V_s landed AND MECH-307 conjunction
   architecture lands, re-queue an SD-029 / MECH-256 retest with the
   full substrate stack on (`use_per_stream_vs=True`,
   `use_anchor_sets=True`, `use_sd039_anchor_payload=True`,
   `use_sleep_loop=True`, sleep recalibration ON,
   `scheduled_external_hazard_enabled=True`).
2. **Acceptance per retest:** C0 trials-sufficient gate PASS on >=3/4
   seeds (>=20 agent_caused_hazard trials AND >=20 env_caused_hazard
   trials per seed); C1 forward_r2 >= 0.9; C2 residual partially
   attenuated for self-caused vs externally-caused (Shergill partial-
   attenuation pattern, **not binary**); C3 approach-event SNR >
   threshold.
3. **Diagnostic non_contributory bookkeeping.** When a retest still
   produces monostrategy events, the verdict is `non_contributory` per
   the governance pattern, not `weakens`. Distinguishes substrate-
   ceiling from mechanism-falsification.

Phase 2 is gated on three upstream substrates landing. The plan-doc
records the gate explicitly so a future session does not re-queue an
SD-029 retest before sleep / V_s / MECH-307 close.

### Phase 3: MECH-257 dual-function controller-gated readout (GAP-3)

MECH-257 claims that E2_harm_s (and E2_harm_a, and any E2_x) is a
single substrate read in two modes -- retrospective comparator
(attribution) and prospective rollout-scoring (evaluation) -- arbitrated
by a controller signal (V3 candidate: commitment boundary state /
hypothesis tag MECH-094; V4 candidate: dACC EVC signal following
Shenhav 2013/2016, or heartbeat-phase gating per ARC-023). The
falsifiable branch: if a single substrate cannot support both modes
(training for evaluator degrades comparator performance or vice versa),
MECH-257 is refuted and the architecture must split into two substrates
per stream, doubling parameter count.

EXQ-452 (governance 2026-04-22) was reclassified non_contributory: dual-
function gated-readout test cannot resolve under V_s monostrategy because
both reads operate over the same locked policy and mode-specific
performance differences cannot manifest.

**Upstream gates:** Phase 2 PASS (need balanced events for both modes
to be exercised) + Phase 1 verdict (need to know whether E2_x is one
substrate or two before testing single-substrate vs split-substrate).

Deliverables:

1. **Re-queue MECH-257 dual-function ablation** after Phase 2 PASS.
   Three arms: (a) comparator-only training, (b) evaluator-only training,
   (c) joint training. Measure mode-specific performance under each
   training regime.
2. **Acceptance:** if joint training produces comparable per-mode
   performance to mode-split baselines, MECH-257 supports (single
   substrate sufficient). If joint training degrades performance >X%
   on either mode, MECH-257 weakens (split required).
3. **Controller signal selection.** V3 default: hypothesis tag MECH-094
   gates which mode is active. Phase 3b (deferred): if V4 controller
   candidates (dACC EVC, heartbeat-phase gating) become available,
   re-test the controller arbitration.

### Phase 4: nociceptive-transfer arbitration (GAP-4) -- Q1

Open question Q1 (registered in this plan): can the comparator
mechanism, evidenced biologically on sensorimotor / tactile / force /
oculomotor / electrosensory streams, generalise to a nociceptive
stream? Plausible (descending pain modulation in PAG/RVM shares the
efference-copy structure; ACC/insula pain self-vs-other attribution
in Frith 2000 and the descending pain modulation literature) but not
directly demonstrated in the four canonical comparator papers
(Frith 2000, Shergill 2003, Blakemore 1998, Haggard 2017). This is
the main mapping risk for SD-029 specifically.

Deliverables:

1. **Targeted lit-pull** on nociceptive comparator / efference-copy
   evidence. Anchor papers: Fields 2004 (PAG/RVM descending
   modulation), Wager 2013 (anticipatory pain modulation), Seymour
   2019 (pain as precision-weighted control signal), descending pain
   modulation reviews 2020-2025. Open question: does the nociceptive
   stream have a comparator-class circuit, or does it use a different
   mechanism (e.g. precision gating without efference-copy
   cancellation)?
2. **Architectural read.** If lit converges on comparator-class
   nociceptive circuit, MECH-256 generalisation to z_harm_s is
   confirmed and SD-029 inherits MECH-256's lit_conf. If lit
   diverges (precision-only, no efference cancellation), SD-029 needs
   its own design doc separate from MECH-256 and the comparator
   metaphor on z_harm_s is over-specified.

Phase 4 is **not gated** on substrate work -- it is a literature pull
that can land in parallel with Phase 1 / Phase 2.

### Phase 5: SD-030 V4 placeholder maintenance (GAP-5)

SD-030 (z_self motor-proprioceptive comparator) is V4-deferred. No V3
evidence expected. Phase 5 is **passive** -- the plan-doc tracks it for
completeness so that V4 work resumes from a known state.

**Scope corrected 2026-08-15:** this phase previously also covered SD-031
(z_world). It no longer does -- SD-031 was rescoped v4 -> v3 on 2026-06-06
and now has its own V3 node, [Phase 6 / GAP-6](#phase-6-sd-031-z_world-comparator-v3-discriminative-validation-gap-6).
Keeping SD-031 here was hiding a live V3 claim inside a `deferred` node,
which the closure snapshot excludes from the V3 denominator entirely.

Deliverables (V4 only): when z_self becomes a first-class latent with its
own forward model, instantiate MECH-256 on it and run per-stream C1/C2/C3
acceptance. Until then, SD-030 remains candidate / V4-deferred in
claims.yaml. The build itself is owned by `self_model_v4:SELF-2`
("Finish self-attribution: complete the per-stream comparator topology"),
which this node now cross-links to; do not duplicate that work here.

GAP-5 is intentionally NOT in the V3 scope of this plan.

### Phase 6: SD-031 z_world comparator V3 discriminative validation (GAP-6)

SD-031 is the z_world (causal-footprint) instantiation of MECH-256 --
"I moved the block", "the door opened because of me". It is **V3**, not
V4: rescoped 2026-06-06 on the ground that it is a named dependency of a
V3-completion retest, with claims.yaml recording the general principle
that "the `implementation_phase` field is a prediction, not a permission
gate".

**The substrate is already built** -- this is a validation gap, not a
design or build gap:

| Piece | State |
|---|---|
| `E2WorldForward` | Built 2026-06-06, `ree-v3/ree_core/predictors/e2_world.py` |
| Config knob | `LatentStackConfig.use_e2_world_forward` (default `False`) |
| Activation smoke (2026-06-06, `world_dim=128`) | `world_forward_r2` 0.969; self-caused residual ~2.0 vs externally-caused ~22.6 -- a correct attribution gap |
| Instrument validity | `failure_autopsy_V3-EXQ-783_2026-07-18` -- `instrument_validated_cause_discriminated` |

**Why it is nonetheless `blocked`, and why the clean smoke is not licence
to queue.** The claims.yaml `evidence_quality_note` states a two-part gate
as a prohibition: validation must run at `world_dim >= 128` **AND** with
ARC-065 behavioural diversity active (balanced agent-caused vs
externally-caused events), because "running before both halves are in
place reproduces the dim=32 + monostrategy + (formerly) unbuilt-comparator
confound". The smoke was a single-config activation check, not the
discriminative arm.

- The **`world_dim >= 128`** half is a config knob (`E2WorldForward`
  hard-asserts it; at the dim=32 default the comparator yields a vacuous
  zero attribution gap). Satisfiable on demand.
- The **behavioural-diversity** half is the *same* re-pointed gate GAP-2
  waits on: `behavioral_diversity_isolation:GAP-A`/`:GAP-I` ->
  `conversion_ceiling_campaign:FULLSTACK`. Not satisfiable on demand.

So GAP-6 unblocks **with GAP-2**, and the honest debt vocabulary is
`complex (probe-gated)` on the diversity half, `complicated (buildable)`
on the world_dim half.

Deliverables:

1. **Queue the discriminative/attribution arm** once FULLSTACK lands, at
   `world_dim >= 128` with `use_e2_world_forward=True` and behavioural
   diversity live. Co-schedule with the GAP-2 SD-029 retest where
   practical -- both need the identical substrate stack and the identical
   balanced-event precondition, so one run configuration serves both
   streams.
2. **Acceptance:** balanced agent-caused vs externally-caused world-event
   counts (the C0-equivalent gate); `world_forward_r2 >= 0.9`; a
   self-caused vs externally-caused residual gap that survives at
   `world_dim >= 128` and is not reproducible at `world_dim = 32`
   (the dim control is what separates a real comparator read from the
   known granularity artefact).
3. **Non-contributory bookkeeping:** if the retest still shows unbalanced
   events, the verdict is `non_contributory`, not `weakens` -- same
   substrate-ceiling-vs-falsification discipline as Phase 2.

Do **not** queue this before both halves hold; the confound is documented
and the run would be vacuous.

---

## Status table

The resume primitive. Updated every session that touches self-
attribution work. See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | blocked | **GATE RE-POINTED — reconciled 2026-07-29 (docs-only). Two of the three gates named below HAVE CLEARED: `sleep_substrate:GAP-1` is `done`, and "MECH-307 conjunction architecture" = `goal_pipeline:GAP-1`, also `done`.** The node nonetheless stays legitimately `blocked`, on a *re-pointed* third gate, not on the original three (node record `governance_2026_06_09` + `governance_2026_06_23`): "MECH-269 V_s monostrategy landing in the main agent path" was itself stale-then-insufficient — ARC-065 SP-CEM became the main-path default 2026-05-17 (V3-EXQ-583), one day after the gate was written, but 543l / 598b / 614e prove the candidate pool collapses at the z_world layer *upstream* of SP-CEM, so SP-CEM alone does not break monostrategy. The live gate is the behavioural-diversity stack behaviourally validated in the main agent path, tracked via `behavioral_diversity_isolation:GAP-A` (now `done`) / `:GAP-I` (`in-progress`), and ultimately `conversion_ceiling_campaign:FULLSTACK` (`assembling`) — because the 2026-06-20 V3-EXQ-625e autopsy showed the 569i conversion is ENV-CONDITIONAL and does not propagate to a threat-engaged candidate pool, so "GAP-A done -> unblock" is a trap. GAP-1 "is not a separate gap from GAP-2" and unblocks with it. **Prior gate text (retained for reconstruction):** specifically: SP-CEM ARM_1 knob bundle (stratified sampling + ao_std_floor + activation gating) plumbed into the default agent path that 445-cohort + SD-029 retest cohort use; `use_support_preserving_cem=True` default in config.py is a naming coincidence and is NOT the activation gate (V3-EXQ-567 ARM_0 confirms this) | After upstream gates close, queue a fresh three-arm ablation (NOT 445h -- that script is two-arm) that exercises ARC-033 vs ARC-058 under balanced events. 2026-05-11 forensic read surfaced substrate-ceiling, not arbitration data; 2026-05-30 STOP verification disproved the methodology-fix framing -- see Decision log | none assignable (the 3-arm ARC-033-vs-ARC-058 arbitration cannot be authored until the re-pointed diversity gate lands; not "TBD pending attention") | 2026-08-18 (row reconcile; node record 2026-08-18) |
| GAP-2 | 2 | blocked | **GATE RE-POINTED — reconciled 2026-07-29 (docs-only), same correction as GAP-1: of the three gates named here, `sleep_substrate:GAP-1` and MECH-307 (= `goal_pipeline:GAP-1`) are both `done`, and the MECH-269 / SP-CEM one was satisfied 2026-05-17 yet proved insufficient.** Live gate per node record `governance_2026_06_23`: `conversion_ceiling_campaign:FULLSTACK` (`assembling`) demonstrating the conversion survives off the reef-bipartite env; `behavioral_diversity_isolation:GAP-A` is `done` but that alone does NOT unblock (the 2026-06-20 V3-EXQ-625e autopsy found the 569i conversion env-conditional). **Prior gate text (retained):** sleep_substrate_plan Phase 1 PASS + MECH-269 V_s landing + MECH-307 conjunction architecture | Re-queue the SD-029 / MECH-256 retest **with the full stack enabled** (candidate_summary_source=e2_world_forward + SP-CEM + modulatory authority) once FULLSTACK lands — NOT before: a retest now would re-derive the known monostrategy non_contributory result. Do **not** "plumb SP-CEM harder"; it is already the default and is empirically insufficient. | none assignable until the FULLSTACK arm lands | 2026-08-18 (row reconcile; node record 2026-08-18) |
| GAP-3 | 3 | blocked | `self_attribution:GAP-1` + `self_attribution:GAP-2` — both still blocked (on the re-pointed diversity/FULLSTACK gate above), so this row's gate is genuinely unmet and unchanged | After GAP-1 / GAP-2 clear, re-queue the MECH-257 dual-function 3-arm ablation. **Reconciled 2026-07-29 (docs-only): status and gate confirmed CORRECT — only the date was stale.** The node record was refreshed twice since (`governance_2026_06_04`, `governance_2026_06_25`), both stale-since-review acknowledgements: closure/residue-discharge autopsies (466b, then `failure_autopsy_V3-EXQ-466d_2026-06-24`) reclassified MECH-094 -> non_contributory and drop-tagged it from the scored set precisely to PROTECT its `stable` status (conf 0.868). **MECH-094 itself is unweakened** and neither reclassification changes GAP-3. | none assignable (blocked upstream) | 2026-07-29 (row reconcile; node record 2026-06-25) |
| GAP-4 | 4 | done | (none) | Lit-pull complete: 2 entries written (De Preter & Heinricher 2024 Trends Neurosci; Seymour 2019 Neuron). Verdict: Option A -- MECH-256 generalises to z_harm_s; SD-029 inherits lit_conf; PAG/RVM implements parallel precision-gating (NOT efference-copy); no separate SD-029 design doc needed | n/a (lit-pull) | 2026-05-17 |
| GAP-5 | 5 | deferred V4 | z_self materialisation in V4 | none in V3. **Scope corrected 2026-08-15: SD-031 split out to GAP-6** -- this row covered SD-030 *and* SD-031 from 2026-05-08 and was never updated when SD-031 was rescoped v4 -> v3 on 2026-06-06, so a live V3 claim sat inside a `deferred` node and was excluded from the V3 closure denominator. SD-030's build is owned by `self_model_v4:SELF-2`, now cross-linked | n/a | 2026-08-15 |
| GAP-6 | 6 | blocked | **Two-part gate, per the claims.yaml SD-031 `evidence_quality_note`, which states it as a prohibition rather than a preference:** (a) `world_dim >= 128` -- a config knob, satisfiable on demand (`E2WorldForward` hard-asserts it; the dim=32 default yields a vacuous zero attribution gap); (b) ARC-065 behavioural diversity live in the main agent path (balanced agent-caused vs externally-caused world events) -- **the same re-pointed gate as GAP-2**, i.e. `behavioral_diversity_isolation:GAP-I` (`in-progress`) -> `conversion_ceiling_campaign:FULLSTACK` (`assembling`). **Gate re-pointed 2026-08-18 (row reconcile, docs-only), matching the frontmatter the steward D-007 adjudication landed the same day:** this row previously put `behavioral_diversity_isolation:GAP-A` at the head of that chain, but GAP-A has been `done` since the V3-EXQ-569i PASS of 2026-06-17 -- i.e. it was already cleared when this node was split out of GAP-5 on 2026-08-15, inheriting GAP-2's stale gate text one hop forward. As on GAP-1/GAP-2, GAP-A being `done` does NOT unblock: the 2026-06-20 V3-EXQ-625e autopsy found the 569i conversion ENV-CONDITIONAL, so "GAP-A done -> unblock" is a trap. It drops out of the chain as a cleared-and-non-unblocking gate, not as a satisfied one -- the outstanding chain GAP-I -> FULLSTACK is unchanged and the `world_dim` half is untouched, so both halves of the SD-031 prohibition still hold. GAP-6 therefore stays `blocked` and still unblocks WITH GAP-2. Substrate is NOT the blocker: `E2WorldForward` built 2026-06-06, activation smoke clean at world_dim=128 (`world_forward_r2` 0.969, self-caused residual ~2.0 vs externally-caused ~22.6), instrument validated by `failure_autopsy_V3-EXQ-783_2026-07-18` | Queue the discriminative arm once FULLSTACK lands, at `world_dim >= 128` + `use_e2_world_forward=True` + diversity live, with a `world_dim = 32` control arm to separate a real comparator read from the known granularity artefact. **Co-schedule with the GAP-2 SD-029 retest** -- identical substrate stack, identical balanced-event precondition. Do NOT queue before both halves hold: the confound is documented and the run would be vacuous, and the clean 2026-06-06 smoke is an activation check, not the discriminative arm | none assignable until the FULLSTACK arm lands | 2026-08-18 (row reconcile; node created 2026-08-15)  **[2026-09-04 governance amend: construction-balanced (RandomPolicy, offline-scored) comparator-only designs clear the diversity half -- see frontmatter resume_condition; V3-EXQ-995 / 1001 ran under that reading.]** |

Status values: `open`, `in-progress`, `blocked`, `paused`, `done`, `deferred`.
A `paused` row carries a resume condition in the [Decision log](#decision-log).

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 | (new design_doc set on MECH-256, MECH-257, MECH-258, ARC-058, SD-029) | ARC-033, ARC-058, MECH-258, MECH-260 | self_attribution_per_stream.md, sd_032_cingulate_integration_substrate.md |
| GAP-2 / Phase 2 | SD-029 (priority=1, status=implemented), MECH-256 (new), MECH-204 (priority=1; **sleep upstream gate**) | SD-029, MECH-256, ARC-033, SD-013 | self_attribution_per_stream.md |
| GAP-3 / Phase 3 | MECH-257 (new) | MECH-257, MECH-094 | self_attribution_per_stream.md, control_plane_heartbeat.md |
| GAP-4 / Phase 4 | n/a (lit-pull only) | MECH-256, SD-029 | self_attribution_per_stream.md |
| GAP-5 / Phase 5 | SD-030 (priority=3, V4) | SD-030 | sd_030_e2_self_forward_model.md |
| GAP-6 / Phase 6 | SD-031 (priority=3, **status=`implemented`**, `unblocks_claims: [MECH-256, zworld-granularity-retest]`) | SD-031 | sd_031_e2_world_forward_model.md |

### Cross-plan boundaries

This plan **consumes** writeback from
[sleep_substrate_plan.md](sleep_substrate_plan.md): Phase 4 of the sleep
plan (MECH-273 real replay-derived training targets) constructs training
tuples `(z_harm_s, a, posterior-corrected residual)` from the cycle's
routed events; the `self`-domain posterior uses **SD-003 / SD-029
causal_sig as evidence**. The self-attribution comparator output is what
makes MECH-273 informative on the self domain. Without a working
comparator (this plan's Phase 1 + Phase 2), MECH-273 writes synthetic
batches and its empirical promotion is impossible.

This plan **provides input to** the goal pipeline (cross-link to
`goal_pipeline_plan.md` -- not yet written; expected sibling plan-of-
record). The dACC bundle (MECH-258 precision-weighted PE channel +
MECH-260 bias suppression channel) consumes the comparator output as
its `pe` field; the comparator's quality bounds the goal pipeline's
commit quality. When the comparator residual is uninformative (Phase 2
blocked), `dACC.pe` is dominated by raw forward-model loss rather than
agency signal, and the goal pipeline's commit-chain decisions are
correspondingly noisy.

The SD-029 single-pass comparator + Q-041 unified threshold supervisor
are gated on MECH-204 (sleep_substrate_plan Phase 1) per substrate_queue
unblocks_claims -- this is reflected explicitly in the
[Status table](#status-table) GAP-2 row.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-08-18 - Steward D-007: GAP-1/GAP-2/GAP-6 frontmatter gates named nodes that had cleared; all three re-pointed, all three stay `blocked`

**Docs-only -- this plan file only. No claims.yaml edit, no substrate_queue edit,
no experiment queued, no manifest touched, no node status changed. All three
nodes remain `blocked`.** Session
`metaworker-chip-20260817-d007-selfattr-stale-gates` (headless), adjudicating
three steward D-007 findings.

**What fired, and against what.** Run against `origin/master` (the local
`ree-cloud-5` checkout is chronically diverged, so the adjudication was done in
a throwaway worktree pinned to origin; the plan file was byte-identical there,
but the *gate-source* plans were not, and their 2026-08-16 governance-apply
state is what the statuses below were read from):

| finding | node | gates named | cleared |
|---|---|---|---|
| P1 strong | `GAP-1` | `sleep_substrate:GAP-1` | **all of them** |
| P2 weak | `GAP-2` | `behavioral_diversity_isolation:GAP-A` / `:GAP-B` | `GAP-A` |
| P2 weak | `GAP-6` | `:GAP-A` / `:GAP-I` -> `conversion_ceiling_campaign:FULLSTACK` | `GAP-A` |

**The answer is not an unblock, and two of the three findings sit exactly on the
trap this plan names by name.** D-007 is a documentation-accuracy detector; a
cleared gate is not an unblocked node. `behavioral_diversity_isolation:GAP-A` is
`done` (V3-EXQ-569i PASS, 2026-06-17), and `governance_2026_06_23` already
recorded that reading that as an unblock "is the same env-conditional trap the
axis_b autopsy caught" -- the 2026-06-20 V3-EXQ-625e autopsy found the 569i
conversion ENV-CONDITIONAL, not propagating to a threat-engaged candidate pool.
For GAP-1, `sleep_substrate:GAP-1` and MECH-307 (= `goal_pipeline:GAP-1`) are
both `done` and the third prerequisite, "MECH-269 V_s monostrategy landing", was
satisfied 2026-05-17 by V3-EXQ-583 -- one day after it was written -- and was
insufficient anyway, because 543l / 598b / the 614e autopsy put the candidate-pool
collapse at the z_world layer *upstream* of SP-CEM.

**Why this survived two prior adjudications, which is the actually new finding
here.** The 2026-06-09 re-adjudication and the 2026-07-29 status-table reconcile
had *already* made this exact call. But 2026-07-29 rewrote the **markdown status
table** and this decision log and left the **YAML frontmatter** alone -- and
`blocking_external` / `resume_condition` are what D-007, the closure map and
every other machine consumer actually read. So the correction lived in prose
while the machine-read gate stayed stale for 20 days, and GAP-6 (created
2026-08-15) then *inherited* GAP-2's already-stale chain, propagating it one hop
forward. **This entry originates no new judgement; it carries the existing one
into the frontmatter.** The lesson for future reconciles is narrow and worth
stating: re-pointing a gate in the status table is not re-pointing the gate.

**What changed.** `blocking_external` on all three nodes, plus GAP-2's
`resume_condition` (whose clause "RE-POINTED GATE: resume once
`behavioral_diversity_isolation:GAP-A/GAP-B` land ..." was itself a live gate
assertion naming a cleared node -- `blocking_external` alone would not have been
enough). The live gate is now, on all three:
`behavioral_diversity_isolation:GAP-I` (`in-progress`) ->
`conversion_ceiling_campaign:FULLSTACK` (`assembling`), which is verbatim what
the 2026-07-29 row and the `cross_plan_link` edges have said since 2026-06-23;
GAP-2 additionally retains `:GAP-B` (`partial`), which is still outstanding and
so was not dropped. GAP-6's `world_dim >= 128` half is untouched and still
unmet-by-default. Prior gate text is retained verbatim in each
`resume_condition`, in the same "retained for reconstruction" form the
2026-06-23 and 2026-07-29 entries use. Node records added as
`steward_2026_08_18` (not `governance_*`: this was a steward adjudication, not a
governance cycle, and it carried none of that cycle's authority).

**Standing prohibitions re-affirmed, unchanged.** Do **not** re-queue the
SD-029 / MECH-256 retest before FULLSTACK lands -- it would re-derive the known
monostrategy `non_contributory` result and burn a runner session. Do **not**
"plumb SP-CEM harder"; it is already the main-path default and is empirically
insufficient. GAP-6's two-part `claims.yaml` SD-031 prohibition still holds in
both halves, so the passing activation smoke remains no licence to queue the
discriminative arm.

**Verification.** D-007 re-run on the edited tree: 3 findings -> **0**,
reported `resolved` (suppressed count unchanged at 24, so they cleared on the
merits rather than being suppressed), and the finding ids changed because the
named-gate set changed. D-008 stayed at 0 across the `last_updated` bumps.

### 2026-08-15 - Is self-attribution multi-agent-dependent? NO for the V3 tier -- and the multi-agent part is already V5. Split SD-031 out of the deferred V4 node.

**Docs-only, this plan file only. No claims.yaml edit, no substrate_queue edit,
no experiment queued, no manifest touched. No pre-existing node changed status.
One node's scope narrowed (GAP-5) and one node created (GAP-6).**

**The question.** Prompted by the 2026-08-15 morning digest, which flagged
`self_attribution` as one of two V3-level plans "worth a look" among the worst
plan-staling (72d, 3 blocked/high) while noting in the adjacent sentence that
"most of the V5/V6 cluster is blocked behind the same missing multi-agent
substrate". The question raised: is self-attribution *also* multi-agent-gated,
and if so should it be recast to V4/V5 -- with whatever node splits keep the V3
closure path intact?

**Answer to the question as asked: NO, and the recast is already done.**

1. **The V3 tier is not multi-agent-dependent.** The comparator's contrast class
   is *self-caused vs environment-caused*, and the environment side is supplied
   by the SD-029 scheduled-external-hazard curriculum -- an env schedule, not
   another agent. The mechanism (MECH-256: `residual = z_x_observed -
   E2_x(z_x_{t-1}, a_actual)`) is efference-copy vs reafference, a single-agent
   sensorimotor computation, and its four canonical anchors (Frith 2000,
   Shergill 2003, Blakemore 1998, Haggard 2017) are all single-agent paradigms.
   Nothing in GAP-1/2/3's recorded blockers is social: all three are gated on the
   monostrategy / behavioural-diversity stack (re-pointed to
   `conversion_ceiling_campaign:FULLSTACK`), documented at length in the
   2026-06-09, 2026-06-23 and 2026-07-29 entries.

2. **The genuinely multi-agent part of self-attribution ALREADY sits in V5, and
   is already tagged correctly.** `multi_agent_ecology_v5:MAE-3` ("Agency
   detection with a structurally-distinct OTHER") states the boundary in its own
   readiness_gate: *"the self-vs-world comparator (SD-031 / MECH-256) is the V3
   BEGINNING; the self-vs-OTHER comparator is the V5 extension this node adds on
   top of it."* That plan carries `generation: v5`, so those nodes are already
   held out of the V3 closure percentage. Attributing causation to an identified
   *other* needs a multi-agent substrate; distinguishing self from not-me does
   not.

3. **The V4 part is likewise already placed** -- `self_model_v4:SELF-2` ("Finish
   self-attribution: complete the per-stream comparator topology (SD-030 z_self
   stream)"), which that plan calls "the user-named 'finish self-attribution'
   work".

So the three-tier split the question asks for pre-exists and is correct. What
was **missing was the back-edges**: both successors pointed at this plan, and
nothing pointed forward, so the V3 -> V4 -> V5 hand-off did not render as map
edges. GAP-5 and GAP-6 now carry `cross_plan_link` to `self_model_v4:SELF-2` and
`multi_agent_ecology_v5:MAE-3`. (Same defect class, and same fix, as the
2026-06-23 entry: "the operative gate lived only in `blocking_external`
(non-rendering) ... so the convergence is drawn".)

**`multi_agent_ecology_v5_plan.md` was deliberately NOT edited.** MAE-3's
`cross_plan_link: ["self_attribution"]` is a whole-**plan** reference, which
`check_closure_links.py` documents as a sanctioned, intentional pattern
("or -- if it is a deliberate back-pointer ... an intentional whole-plan
reference"), **not** a dangling node id. It looked like a defect worth
narrowing to `self_attribution:GAP-6` now that a matching node exists; it is
not one, and the forward edges added on this side already draw the
relationship. Do not "fix" it.

**The real defect found, running the OPPOSITE way to the hypothesis.** Checking
the generation boundary surfaced a misfiling in the other direction:
**SD-031 (z_world causal-footprint comparator) is a live V3 claim whose only
owning closure node was `deferred` V4** -- so it was excluded from the V3
progress denominator outright (`generate_closure_snapshot.py`
`DEFERRED_STATUSES`) and was invisible to the closure accounting: not done, not
remaining, not visible as a gap.

Six artefacts were checked; five say V3, and only GAP-5 said V4:

| Artefact | Reading |
|---|---|
| `claims.yaml` SD-031 | `implementation_phase: v3`, `v3_pending: true`, `candidate/v3_pending`; explicit **"Rescoped v4 -> v3 on 2026-06-06"** note |
| `self_model_v4_plan.md` (deliberate-exclusions section) | "**SD-031 (world-stream self-attribution) stays a V3 item** ... Only SD-030 ... is V4" |
| `self_model_v4:SELF-2` readiness_gate | "V3 BEGINNING present: self-attribution on the z_world ... stream runs (SD-031, V3-pending)" |
| `multi_agent_ecology_v5:MAE-3` readiness_gate | "SD-031 / MECH-256 is the V3 BEGINNING" |
| `substrate_queue.json` SD-031 | `status: implemented`; `unblocks_claims: [MECH-256, zworld-granularity-retest]` -- a built substrate awaiting a retest |
| **`self_attribution:GAP-5`** | **"SD-030/SD-031 ... materialisation (V4)", `status: deferred`** |

**Mechanism of the error, which is mundane and worth naming so it is not
mistaken for a judgement call:** GAP-5 was registered 2026-05-08, when SD-031
genuinely *was* V4. SD-031 was rescoped on 2026-06-06. GAP-5 was the **only node
in this plan never revisited since registration** -- every other node carries at
least one `governance_*` acknowledgement -- so the rescope never propagated to
the node that owns it. The plan's own resume-ritual discipline touched the
blocked nodes repeatedly and skipped the deferred one, which is exactly where a
silently-stale generation tag can hide.

**What changed.** GAP-5 narrowed to SD-030 only (still `deferred` V4, correctly).
New `self_attribution:GAP-6` owns SD-031 as V3, `status: blocked`. GAP-6 is
blocked, not open, on the claims.yaml gate stated as a prohibition: `world_dim >=
128` **and** live behavioural diversity, since "running before both halves are in
place reproduces the dim=32 + monostrategy + (formerly) unbuilt-comparator
confound". The diversity half is the *same* gate as GAP-2, so **GAP-6 unblocks
with GAP-2 and should be co-scheduled with the SD-029 retest** -- one substrate
configuration serves both streams.

**Closure effect, measured not estimated.** `generate_closure_snapshot.py` was
regenerated against `origin/master` twice -- once with the plan file as-committed,
once with this split -- on the same base, same run:

| | overall | done | remaining | deferred |
|---|---|---|---|---|
| Baseline (no split) | 72.6% | 62 | 31 | 13 |
| **With split** | **71.9%** | 62 | **32** | 13 |

One added `blocked` node (weight 0.1) in the V3 denominator, so the headline goes
*down* 0.7 pp. That is the correction, not a regression -- the previous figure was
overstated by holding a real V3 item inside a deferred V4 node. Net effect on the
actual question asked: **V3 closure is preserved and made honest**; no V3 work was
pushed out to V4/V5, and nothing was pulled in from them.

*Reconciliation warning:* the committed `docs/closure_dashboard.md` was generated
2026-08-13 and reads 71.0% / 92 non-deferred / 59 done. That baseline is **stale**
-- other plans landed work in the intervening two days -- so differencing against
it gives the right *delta* by luck and the wrong *absolute*. Hence the A/B above.

**Not done here, deliberately.** No claims.yaml edit (SD-031's metadata is
already correct -- it was the plan that was wrong). No experiment queued (GAP-6
is genuinely blocked). `MECH-099` is `implementation_phase: v3` while sitting in
the v5 `MAE-3` node -- noted, not adjudicated: it is a `multi_agent_ecology_v5`
question, and that plan's `generation: v5` already holds it out of the V3
percentage, so nothing is mis-counted today.

### 2026-07-29 - Status-table reconcile: GAP-1/2/3 were listing gates that have since CLEARED; nodes stay blocked, on a re-pointed gate

**Docs-only. No experiments queued, no claims.yaml edit, no manifest touched.
No node status changed -- all three remain `blocked`.**

This plan had logged no decision since 2026-05-30 (60 days), and all three open
rows named `TBD (post-substrate-gates)` as owner, which invited the reading
"blocked on three unmet gates, nobody assigned". **The answer to the question
that reading raises -- have the gates cleared? -- is: two of the three have.**

- `sleep_substrate:GAP-1` ("Phase 1 PASS") is **`done`**.
- "MECH-307 conjunction architecture" = `goal_pipeline:GAP-1`, also **`done`**.
- "MECH-269 V_s monostrategy landing in the main agent path" was satisfied
  **2026-05-17** (ARC-065 SP-CEM became the main-path default, V3-EXQ-583) --
  *one day after the gate was written*, so it had been silently stale for
  roughly three weeks.

None of that unblocks the work, and the node records already say why (the
2026-06-09 re-adjudication and `governance_2026_06_23`): the gate's *intent* was
"break monostrategy so SD-029 C2/C3 become measurable", and SP-CEM alone does
not achieve it -- 543l, 598b and the 614e autopsy show the candidate pool
collapses at the z_world layer **upstream** of SP-CEM, so stratified sampling has
nothing to stratify. The gate was therefore RE-POINTED to the behavioural-
diversity stack, and now to `conversion_ceiling_campaign:FULLSTACK`
(`assembling`): `behavioral_diversity_isolation:GAP-A` is `done` (V3-EXQ-569i
PASS), but the 2026-06-20 V3-EXQ-625e autopsy found that conversion is
ENV-CONDITIONAL and does not propagate to a threat-engaged candidate pool, so
"GAP-A done -> unblock GAP-2" is precisely the trap the axis_b autopsy caught.

So the rows were rewritten to name the *live* gate rather than three superseded
ones, and the owners changed from `TBD` to "none assignable" -- for the same
reason recorded in the arc_062 reconcile: there is no experiment to author yet,
which is a different state from an unassigned one. Explicitly retained: do
**not** re-queue the SD-029/MECH-256 retest before FULLSTACK lands (it would
re-derive the known monostrategy `non_contributory` result), and do **not**
"plumb SP-CEM harder" -- it is already the default and is empirically
insufficient. GAP-3's gate (`GAP-1` + `GAP-2`) was verified still unmet and
unchanged; only its date was stale.

### 2026-05-30 - GAP-1 STOP on methodology-fix re-queue: SP-CEM substrate default-off in 445-cohort agent path {#2026-05-30-gap-1-stop-methodology-fix}

IGW-20260530-017 (inter-governance-brief workset item, top priority on the
self_attribution lens) routed this node as a methodology-fix path:
"a methodology re-run that simply restores the dropped ON_SHARED arm does
NOT need monostrategy resolution -- ARC-065 SP-CEM substrate is already
landed (V3-EXQ-567 PASS 2026-05-15, selected_action_entropy 0.012->0.497)
and produces enough policy diversity for the C2/C3 measurements."

Verification today disproved the framing's premise before any new EXQ was
queued. Three findings:

1. **445h two-arm read re-confirmed** (predecessor 2026-05-11 finding still
   accurate): `CONDITIONS = ["OFF", "ON_INDEPENDENT"]` at
   [v3_exq_445h_sd032b_dacc_reef.py:83](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_445h_sd032b_dacc_reef.py);
   `use_shared_harm_trunk=False` hardcoded at line 127; manifest
   `config.conditions` matches; manifest per-seed
   `action_class_entropy=0.0` across all 6 seed/arm cells; manifest
   `action_counts` shows pure single-action monostrategy per seed
   (seed=42 -> action 0 only; seed=7 -> action 2 only; seed=13 -> action 4
   only).

2. **V3-EXQ-567 PASS does NOT mean SP-CEM is on the default agent path.**
   The 567 manifest's ARM_0 (`ARM_0_normal_cem`) shows the SAME
   monostrategy signature as 445h: per-seed
   `selected_action_class_entropy` = 0.0 / 0.0 / 0.03795 and
   `support_preserving_active_steps = 0` across all three seeds. The
   PASS verdict is `ARM_1_support_preserving - ARM_0_normal_cem`
   (ARM_1 mean 0.4897 vs ARM_0 mean 0.0127). The SP-CEM mechanism EXISTS
   and WORKS, but is activated in ARM_1 specifically by the
   SP-CEM + stratified-sampling + ao_std_floor knob bundle. ARM_0 is the
   default code path that the 445-cohort scripts use.

3. **`use_support_preserving_cem: bool = True` in
   `ree_core/utils/config.py:762` is a naming coincidence.** The field is
   defaulted True but its activation is gated on the additional knob
   bundle that ARM_0 of 567 does not set. Hence 567 ARM_0 shows
   `support_preserving_active_steps = 0` even though the field defaults
   True. The 2026-05-29 governance note in the GAP-1 closure_plan row's
   `governance_2026_05_29` field (598b / 543l substrate-ceiling readings
   from this cycle) is the SAME phenomenon from a different cohort.

**Conclusion: substrate gate IS load-bearing for GAP-1.** Re-queueing a
three-arm methodology fix (the workset-routed V3-EXQ-445i) under the
current default config would reproduce the bit-identical-arms
substrate-ceiling signature surfaced in 2026-05-11, waste a runner
session, and create a fourth misleading PASS-shaped "winner_suggested" tag
on a non-discriminative test. GAP-1 stays `blocked` on the SAME upstream
gates as GAP-2 -- the framing distinction the workset item drew between
"methodology fix" and "substrate gate" does not hold.

> **Id provenance -- `V3-EXQ-445i` was NEVER MINTED (recorded 2026-08-15, docs-only).** The id
> appears in this plan only as the label the IGW-20260530-017 workset item *proposed* for the
> three-arm re-queue that the 2026-05-30 verification then STOPPED before queueing. Nothing was
> ever created under it: no queue entry in `ree-v3` current or historical
> (`git log -S"V3-EXQ-445i" --all -- experiment_queue.json` is empty), no script under
> `ree-v3/experiments/`, no manifest under `evidence/experiments/`, no `runner_status.json` entry.
> It is therefore **not an owed successor that someone dropped** -- the decision *not* to mint it
> is itself the finding recorded above, and that finding still stands. Do not queue it. The
> three-arm ARC-033-vs-ARC-058 arbitration stays `none assignable` (see the Status table) until
> the re-pointed diversity/FULLSTACK gate lands, at which point `/queue-experiment` mints a fresh
> id.

Actions taken this session:
- GAP-1 closure_plan node `last_updated` bumped to 2026-05-30; new
  `governance_2026_05_30` field records the STOP verification.
- This decision-log entry written.
- NO new EXQ queued.
- NO claims.yaml / substrate_queue.json / manifest / review_tracker
  edits.
- /inter-governance-brief workset description for IGW-20260530-017
  should drop the methodology-fix framing on its next regen so future
  sessions do not re-spawn this work. (The /inter-governance-brief
  generator reads this plan-doc and the closure_plan
  `governance_2026_05_30` field will reach the next workset regen.)
- The real unblock path for GAP-1 is the SAME unblock path for GAP-2:
  the SP-CEM ARM_1 knob bundle (stratified sampling + ao_std_floor +
  the activation gating that ARM_0 of 567 lacks) must be plumbed into
  the default agent path that 445-cohort scripts and the SD-029 retest
  cohort use. That is substrate work, owned by the ARC-065 substrate_queue
  entry, NOT by a 445i methodology re-queue.

### 2026-05-17 - GAP-4 DONE: nociceptive-comparator lit-pull complete; architectural verdict Option A

Lit-pull for self_attribution:GAP-4 complete. Two papers added:

1. **De Preter & Heinricher 2024** (*Trends in Neurosciences*, PMID 38749825, DOI 10.1016/j.tins.2024.04.006) -- `targeted_review_connectome_mech_256`. Mixed 0.74. The PAG/RVM implements behavioural-state-gated precision control of nociception via ON/OFF cells (opioid tone, motivational context), NOT efference-copy forward-model comparator. This establishes that the "PAG/RVM shares efference-copy structure" posit in the plan was not borne out mechanistically: the PAG/RVM system is a contextual precision-gating layer, not a per-step motor-prediction subtraction site.

2. **Seymour 2019** (*Neuron*, PMID 30897355, DOI 10.1016/j.neuron.2019.01.055) -- `targeted_review_sd_029`. Mixed 0.61. Pain as precision-weighted prediction-error signal for RL/control. Computationally convergent with MECH-256 at Marr level 2 (both use prediction-error logic for harm signals) but distinct at implementation: Seymour's framework addresses multi-trial learned-expectation priors; MECH-256/SD-029 addresses per-step efference-copy forward-model residual.

**Architectural verdict: OPTION A** (plan sec. Phase 4, "if lit converges on comparator-class nociceptive circuit"):

- Self-generated pain IS attenuated by an efference-copy comparator mechanism (established behaviourally by Lalouni 2020, already in SD-029 corpus, ~40% threshold shift).
- The PAG/RVM does NOT implement this comparator -- it implements a parallel precision-gating layer.
- The efference-copy substrate is most likely at: (a) spinal dorsal horn via corticospinal collateral corollary discharge to dorsal horn interneurons, and/or (b) somatosensory cortex (S1/insula) forward-model subtraction.
- MECH-256 generalises to z_harm_s (the nociceptive reafferent stream). SD-029 inherits MECH-256's lit_conf.
- No separate design doc needed for SD-029. The comparator metaphor is NOT over-specified.
- Architectural note: add a clarifying sentence to any SD-029 / MECH-256 design docs noting that E2_harm_s's efference-copy comparator operates at spinal/cortical level; the PAG/RVM precision-gating is a parallel modulatory layer that adjusts expected-precision of z_harm_s based on motivational state (separate mechanism, not competing).

GAP-4 closed. Phase 4 of the plan is DONE.

### 2026-05-16 - Closure-map reconciliation: SD-029 / MECH-256 retest monostrategy gate has a validated substrate fix (ARC-065 SP-CEM)

Staleness pass (status tables 5-8 days behind runner, now V3-EXQ-581).

GAP-2 (SD-029 / MECH-256 retest) carries
`blocking_external: ["MECH-269 V_s monostrategy landing"]`; GAP-1 and
GAP-3 inherit the same gate (GAP-1 resume_condition: "Same upstream
substrate gates as GAP-2"). Reconciled evidence:
- V3-EXQ-550 FAIL (supports MECH-269): confirms the monostrategy
  reading at no-training depth -- a monomodal policy cannot generate the
  balanced agent-vs-env event distributions the SD-029 C2/C3 metrics
  need.
- V3-EXQ-567 PASS (supports ARC-065): support-preserving CEM lifts
  natural action entropy 0.012 -> 0.497 and candidate support
  1.007 -> 2.810 -- the validated mechanism that produces the policy
  diversity the retest requires.

The "MECH-269 V_s monostrategy landing" blocking_external now has a
concrete satisfier path (ARC-065 SP-CEM, V3-EXQ-567). GAP-1/2/3 stay
`blocked` (retest not yet run) but are unblockable once SP-CEM lands in
the main agent path; GAP-2 blocking_external + last_updated updated
accordingly.

### 2026-05-11 - GAP-1 monostrategy inversion {#2026-05-11-gap-1-monostrategy-inversion}

Phase 1 forensic read of V3-EXQ-445h, performed today, surfaced that the
arbitration data the plan keyed on does not exist. Two findings:

1. **EXQ-445h is two-arm only.** Script line 83 of
   [v3_exq_445h_sd032b_dacc_reef.py](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_445h_sd032b_dacc_reef.py)
   sets `CONDITIONS = ["OFF", "ON_INDEPENDENT"]`. The ON_SHARED arm was
   silently dropped after the EXQ-445b iteration; EXQ-445a/c/d/f/g/h all
   run `use_shared_harm_trunk=False` hard-coded. The 2026-05-08 plan-
   registration step referred to "EXQ-445h forensic read" because the
   manifest's c1_mech258 / c2_sd032b / c3_mech260 grid reads as if it had
   the data; the underlying script does not.
2. **EXQ-445 and EXQ-445b (which retained the three-arm shape) show
   floating-point-identical metrics across ON_INDEPENDENT and ON_SHARED**
   per seed (harm_a_forward_r2 and mean_score_bias_abs both bit-identical
   across the two architectural arms, varying only across seeds). Under
   `action_class_entropy=0.0` in every condition for every seed, the
   policy is monomodal -- the trajectory through the env is deterministic
   given seed alone, so both forward-model architectures consume the same
   z_harm_a stream and trivially fit a near-degenerate target. The
   architectural distinction between `ResidualHarmForward` (ARC-033) and
   `HarmForwardTrunk + HarmForwardHead` (ARC-058) is unmeasurable because
   the input distribution does not exercise it. The EXQ-445
   `c4_arc033_vs_arc058_diagnostic` field even records this:
   `mean_r2_independent == mean_r2_shared == 0.8986271204935968` exactly;
   the "winner_suggested_by_forward_r2: ARC-058_shared" tag is
   meaningless because the test is non-discriminative.

Conclusion: **GAP-1 is the same V_s monostrategy substrate ceiling that
blocks GAP-2.** The 9 non_contributory reclassifications already logged
for SD-029 (EXQ-433 / 433a / 433b / 470 / 433d / 433f / 537 / 537a /
523b) are the same blocker -- EXQ-445 and EXQ-445b just didn't get
reclassified the same way at original-review time because c1_mech258
PASSed at the same trivial-fit signature.

Actions taken this session:
- GAP-1 status `open` -> `blocked` with same upstream gates as GAP-2
  (sleep_substrate Phase 1 PASS + MECH-269 V_s landing + MECH-307
  conjunction architecture).
- EXQ-445 and EXQ-445b (two timestamped runs) manifests updated:
  evidence_direction_per_claim for ARC-033 and ARC-058 -> non_contributory
  with evidence_quality_note pointing at the bit-identicality +
  action_class_entropy=0.0 signature. MECH-258 / MECH-260 / SD-032b reads
  preserved (within-arm criteria) but inherit the substrate-ceiling
  caveat.
- Phase 1 narrative section updated to record the inversion. The "not
  gated on Phase 2/3" claim is removed; the revised acceptance is to
  queue a fresh three-arm ablation (NOT a 445-letter iteration) post-
  substrate-gates with both balanced-events acceptance AND a cross-arm
  discriminability floor.
- No new EXQ queued. Queueing EXQ-445i would burn a runner session on
  the same blocker.

### 2026-05-08 - Plan registered

Plan created in conversation with user. SD-003 supersession history
(2026-04-18) treated as background context; this plan covers the
successor layer (MECH-256 + SD-029 + MECH-257) and its competing
architectural commitments (ARC-033 vs ARC-058). Six gaps surfaced and
sequenced into six phases (GAP-6 added 2026-08-15). Cross-plan boundaries with
sleep_substrate_plan (consumer of writeback) and goal_pipeline_plan
(provider of dACC PE input) made explicit.

### 2026-04-18 - SD-003 superseded by MECH-256 + SD-029

Recorded in claims.yaml SD-003 supersession_note. Reasons: (1) 28 FAILs
across V2+V3 iterations on the two-pass counterfactual architecture
since z_world -> z_harm_s stream migration; (2) biological precedent
gap -- Frith 2000, Shergill 2003, Blakemore 1998 evidence single-pass
comparator (`residual = observed - E2(prev_state, a_actual)`), not
two-pass counterfactual; (3) three-pull lit synthesis 2026-04-18
converged on single-pass comparator with one E2 substrate read in two
modes (MECH-257). Existing evidence chain (EXQ-030b/115/166a/195/353/431)
remains in the historical record; new V3 evidence accrues to SD-029.
ARC-033 forward model component carried forward unchanged.

### 2026-04-19 - ARC-058 registered as competing claim against ARC-033

Horing & Buchel 2022 (J Neurosci) "modality-general neural code for
aversive stimulus representation in the anterior insula" is the
biological grounding: anterior insula encodes unsigned aversive PE
shared across pain, loud noise, and other aversive modalities; dorsal
posterior insula carries modality-specific signed PE. ARC-058 holds
that a SHARED HarmForwardTrunk encodes the unsigned modality-
independent substrate while stream-specific HarmForwardHeads produce
signed per-modality readouts; ARC-033 holds independent per-stream
forward models. Falsifiable via V3-EXQ-445 three-arm ablation. MECH-257
(single-substrate dual-function) is the sibling philosophical claim.

### 2026-04-22 - SD-029 retest cohort reclassified non_contributory under V_s monostrategy

EXQ-433/433a/433b/470 reclassified non_contributory (governance
2026-04-22). Substrate gap is V_s monostrategy: monomodal policy cannot
generate balanced agent-vs-env event distributions for C2/C3
measurement. Hold candidate pending MECH-269 V_s landing.

### 2026-04-27 - EXQ-433d adds fourth confirmation

V3-EXQ-433d FAIL (2026-04-27): 4-seed run with EXQ-479 calibrated
curriculum. agent_caused_hazard=0/0/0/0 in all 4 seeds. Same monomodal
phenotype. Reclassified non_contributory.

### 2026-05-08 - EXQ-433f adds fifth confirmation; SD-050 reef enrichment does not break monostrategy

V3-EXQ-433f (2026-05-08 diagnose-errors): C0 trials-sufficient gate
FAILed in 3/4 seeds (agent_caused_trials 15/7/20/3 vs target 20). SD-050
reef enrichment (`reef_enabled=True`, `n_reef_patches=3`,
`hazard_food_attraction=0.7`) intended to break monostrategy on 8x8
grid but did not produce balanced events at this scale. Hold remains
gated on MECH-269 / MECH-269b V_s landing; reef-substrate tweaks are
not the unblock.

### 2026-05-08 - Sleep substrate identified as upstream gate

Per 2026-05-08 governance and substrate_queue MECH-204 entry's
unblocks_claims, the sleep loop is the load-bearing upstream substrate
for SD-029 / MECH-256 retest. The relationship is bidirectional: sleep's
MECH-273 writeback consumes SD-029 causal_sig, and SD-029 retest
requires sleep recalibration to break the V_s monostrategy. This plan
records the gate; sleep_substrate_plan Phase 1 is the trigger.

---

## Open questions

Numbered for reference from future sessions.

- **Q1 (Phase 4)**: Does the comparator mechanism generalise to
  nociceptive streams? Comparator literature evidences mechanism on
  sensorimotor / tactile / force / oculomotor / electrosensory streams.
  Extension to nociceptive plausible (PAG/RVM descending modulation
  shares efference-copy structure; ACC/insula pain self-vs-other
  attribution) but not directly demonstrated in the four canonical
  comparator papers (Frith 2000, Shergill 2003, Blakemore 1998,
  Haggard 2017). Default proposed: schedule a targeted lit-pull on
  nociceptive comparator / descending pain modulation
  (anchor papers: Fields 2004, Wager 2013, Seymour 2019, plus
  2020-2025 reviews). Resolves to either "MECH-256 generalises ->
  SD-029 inherits lit_conf" or "MECH-256 + nociceptive needs separate
  design doc -> SD-029 has its own architectural commitment".
- **Q2 (Phase 1)**: For the ARC-033 vs ARC-058 verdict, what
  forward_r2 degradation threshold should trigger ARC-058 retirement?
  Default proposed: degradation > 5% on z_harm_s forward_r2 in the
  shared-trunk path vs the independent-per-stream path is sufficient
  to weaken ARC-058. Less than 5% with a usable shared-PE signal
  weakens ARC-033 in favour of parameter parsimony.
- **Q3 (Phase 3)**: For MECH-257 controller signal selection in V3,
  is the hypothesis tag (MECH-094) sufficient, or does the controller
  need additional state (commitment boundary, heartbeat phase from
  ARC-023, dACC EVC at V4)? Default proposed: V3 uses MECH-094 only;
  V4 layered controllers added in a follow-up plan-doc when ARC-023
  + Shenhav-EVC substrates become available.
- **Q4 (Phase 2)**: When SD-029 retest finally produces balanced
  events, is the partial-attenuation pattern (Shergill 2003) the
  correct C2 acceptance, or should C2 require near-binary
  discrimination? Default proposed: partial attenuation is the
  biologically grounded acceptance per Shergill 2003 (~50% partial,
  not binary); a binary requirement would over-specify the comparator.

---

## Resume ritual

When picking up self-attribution work after a deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that
   was `paused` or `in-progress`.
3. If `blocked`, check whether the upstream gate has fired:
   - GAP-2 / Phase 2: read [sleep_substrate_plan.md](sleep_substrate_plan.md)
     status table for Phase 1 PASS + check substrate_queue.json
     MECH-269 / MECH-307 entries.
   - GAP-3 / Phase 3: check Phase 2 status here AND Phase 1 verdict.
4. If `in-progress`, find the most recent decision-log entry for that
   phase and continue from the last concrete action.
5. Update the row's `Last updated` field and `Status` if it changes.
6. Append a new decision-log entry for any architectural choice made
   during the resumed session.

Sessions that do NOT touch self-attribution work do not need to read
this document. Sessions that DO touch SD-003 / SD-029 / MECH-256 /
MECH-257 / SD-013 / ARC-033 / ARC-058 / MECH-258 / MECH-260 / SD-030 /
SD-031 read this document before any code or experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite
entries die with the session; WORKSPACE_STATE.md is recent-work, not
strategic; substrate_queue.json is granular but does not capture phase
ordering or decision rationale. This document is the single source of
truth for self-attribution strategy.

---

## See also

- [docs/architecture/self_attribution_per_stream.md](../../docs/architecture/self_attribution_per_stream.md)
- [docs/architecture/sd_013_e2_harm_s_interventional_training.md](../../docs/architecture/sd_013_e2_harm_s_interventional_training.md)
- [docs/architecture/sd_032_cingulate_integration_substrate.md](../../docs/architecture/sd_032_cingulate_integration_substrate.md)
- [docs/architecture/sd_003_experiment_design.md](../../docs/architecture/sd_003_experiment_design.md) (historical / superseded)
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) Phase 4 cross-boundary
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) plan-doc precedent
- [evidence/planning/substrate_queue.json](./substrate_queue.json) MECH-204 priority=1 (sleep gate); SD-029 priority=1; MECH-307 priority=1
- evidence/planning/goal_pipeline_plan.md (sibling plan-of-record; consumes comparator output via dACC bundle; not yet written at registration time)
- evidence/planning/commitment_closure_plan.md (sibling plan-of-record; in-progress in parallel session)
