---
closure_plan:
  id: behavioral_diversity_isolation
  title: "Behavioural Diversity Isolation"
  registered: 2026-05-25
  last_updated: 2026-06-14
  scope_claims: [ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076]
  sibling_plans: [arc_062_rule_apprehension, commitment_closure, sleep_substrate, sd033_governance, goal_pipeline, self_attribution]
  nodes:
    - id: "behavioral_diversity_isolation:GAP-A"
      title: "Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)"
      phase: "FP-2 matched-entropy falsifier ran TWICE (569f, 569g) -> both FAIL/non_contributory (r1a_entropy_only_artefact); blocked on the shared E3 selection-authority commit-coupling"
      status: in-progress
      severity: medium
      owner_exq: "V3-EXQ-569g FAIL/non_contributory 2026-06-11T22:49Z (r1a_entropy_only_artefact; supersedes 569f) is the lineage FRONTIER. PREDECESSORS: V3-EXQ-569f FAIL/non_contributory 2026-06-10T00:12Z (r1a_entropy_only_artefact; supersedes 569d); V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30"
      unblocks_claims: [ARC-065]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-H", "arc_062_rule_apprehension:GAP-B", "sd_037_axis_b:P1b"]
      last_updated: 2026-06-15
      governance_2026_06_15: "682-GATED ROUTE CONSUMED -- CONVERSION amend IMPLEMENTED (session gapa-682-gated-conversion-amend-20260615T0441Z). GATE CHECK: V3-EXQ-682 LANDED PASS 2026-06-15T03:25Z (no_collapse_reproduced; coordinator DB + evidence manifest). It answers the governance_2026_06_14_pm2 step (1) -- residual per-seed upstream re-collapse on seeds 43/44? -- with NO: ARM_1_E2WF applied in-arm route_range 0.204 (active_frac 1.0, summaries_none_frac 0.0, summary_pairwise_dist 0.065 >= floor, projected_range 0.204), AND it held on seed 43 (applied route 0.21, the seed where 569g's CONVERSION fell below the controls). ALL FOUR collapse causes ruled out -> NO upstream fix needed; clean Branch A. STEP (2) DONE: /implement-substrate landed the modulatory-bias-selection-authority CONVERSION amend on ree-v3 main (e3_selector.py + config.py), two no-op-default levers, bit-identical OFF (1036 contracts + 7/7 preflight PASS, 4 new conversion contracts): (a) modulatory_authority_normalize_basis range|std (std anchors to gain*raw_score_std -> near-decisive not just near-tie; gain sweepable; safety: keep gain<1.0 additive) + (b) use_modulatory_shortlist_then_modulate + margin (F filters to a near-tie set, modulatory channel arbitrates within -> safety-preserving at any strength). STEP (3): V3-EXQ-684 readiness sweep queued (claim-free; gain x {range,std} x shortlist vs a VERIFIED-LIFTING matched-noise control; committed entropy MOVES with channel range AND beats the control). STEP (4): V3-EXQ-569h (GAP-A falsifier with an IN-ARM applied-route-range non-vacuity gate) is GATED on 684 PASS -- NOT pre-queued on a guessed config (a guess risks the false-weakens the diagnose-first discipline guards against). ARC-065 stays provisional / non_contributory / pending_retest_after_substrate; MECH-341 untouched; NO claims.yaml change (substrate-only). xref MECH-341/ARC-062/MECH-309/MECH-294 (one shared conversion fix). Node STAYS in-progress (substrate amend landed; falsifier gated on readiness). NOTE for downstream: on 569h PASS, sd_037_axis_b:P1b (queue V3-EXQ-625d) + self_attribution:GAP-2 become workable (per governance_2026_06_14_pm)."
      governance_2026_06_14_pm2: "NEXT STEP IS 682-GATED (corrected autopsy, user-directed 'keep 682 running'). failure_autopsy_V3-EXQ-569g_2026-06-14 was REWRITTEN (REE_assembly master 32ae997878) -- the prior 20:14Z version (a8fd6ae7d2) MISREAD arm_results[0/1/2] (the three SEEDS of ARM_0_PROPOSER, ~0 by design) as 'all three arms route_range=0.0' and wrongly routed diagnose-first/action=none. CORRECTED FINDING: ARM_1_E2WF applied in-arm modulatory_channel_route_range 0.18 (3/3 seeds; route_range_per_arm_mean.ARM_1_E2WF 0.179852 = the readiness probe) at the live select tick -- so the 06-10 route-range amend SOLVED REACH (range reaches the E3 authority accumulator). The RESIDUAL gap is CONVERSION: ARM_1 committed entropy 0.615 is NOT strict-above proposer/matched-noise 0.704 (1/3 seeds). Cause = the gap-relative ADDITIVE authority at gain 0.5 (e3_selector.py:938-944, modrange = 0.5*raw_score_range), subdominant to the F-dominated primary (88-89% of E3 variance, V3-EXQ-571); upstream-magnitude sweeps (667/640a) are washed out because the authority range-renormalizes its input. EXACT NEXT STEP, GATED ON V3-EXQ-682 LANDING (the in-arm route-range collapse diagnostic, claim_ids=[], already queued): (1) READ 682 first -- does it show a residual per-seed upstream re-collapse on the seeds where ARM_1 fell BELOW the controls (seeds 43/44)? (2) /implement-substrate the modulatory-bias-selection-authority gain/contrast amend per the autopsy: (a) a contrast/normalization rescale (or modulatory_authority_gain bump) so the routed per-candidate range MOVES the committed argmax against the F-dominated primary -- if 682 shows a residual upstream collapse, fix that too; (b) shortlist-then-modulate arbitration (F filters to a near-tie set, modulatory channel arbitrates within it) is the pre-registered FALLBACK the gain sweep discriminates. (3) a substrate-readiness validation (claim_ids=[]) showing committed-action entropy MOVES with channel range AND beats a VERIFIED-LIFTING matched-noise control (569g's ARM_2 temperature control under-lifted: entropy == proposer). (4) THEN V3-EXQ-569h as the real FP-2 falsifier with an IN-ARM (not probe-only) applied-route-range non-vacuity gate. Do NOT re-queue a matched-entropy falsifier before the gain/contrast amend (would reproduce r1a_entropy_only_artefact). ARC-065 stays provisional / non_contributory / pending_retest_after_substrate; xref MECH-341/ARC-062/MECH-309/MECH-294 (one shared conversion fix). This SUPERSEDES the diagnose-first framing in governance_2026_06_14 + the route-range-into-selection framing in resume_condition (route-range REACH is done; conversion is the residual)."
      governance_2026_06_14_pm: "DOWNSTREAM CROSS-PLAN DEPENDENT registered: sd_037_axis_b:P1b is upstream_blocked on THIS node's committed-action-diversity demonstration. On the GAP-A 569-lineage falsifier PASS (and/or the ARC-062 falsifier on the modulatory-bias-selection-authority substrate) confirming scoring-layer diversity reaches committed action, ALSO revisit sd_037_axis_b:P1b -> queue the redesigned successor V3-EXQ-625d (joint composite via the scaffolded_sd054_onboarding scheduler path + authority channel + MECH-341/SD-056, sharpened C3a/C3b). Reverse link to the existing P1b->GAP-A/B forward link (P1b reconciled blocked_pending_substrate -> upstream_blocked 2026-06-14, commit b4c062022c). Discoverability/link edit ONLY -- no status/owner_exq/unblocks_claims/claims.yaml change to this node."
      governance_2026_06_14: "DRIFT RECONCILE (read-only-report follow-up; session reconcile-bdiv-cluster-drift-20260614T1911Z). The 2026-06-09 frontmatter was STALE: it declared V3-EXQ-569f 'IN FLIGHT' but 569f had already RUN and a successor 569g had also RUN, neither absorbed. ABSORBED NOW: (1) V3-EXQ-569f LANDED FAIL/non_contributory 2026-06-10T00:12Z, interpretation.label=r1a_entropy_only_artefact -- ALL readiness preconditions MET (consumed-summary spread 0.196 >> 0.05 floor; C1 e2.world_forward divergent PASS) but the load-bearing C_R1B_selected_entropy_strict_above_matched_noise=FALSE; selected-action entropy BIT-IDENTICAL 0.549141 across PROPOSER / E2WF / MATCHED-NOISE; 0/3 seeds strict-above-both. (2) V3-EXQ-569g LANDED FAIL/non_contributory 2026-06-11T22:49Z (supersedes 569f; SAME label r1a_entropy_only_artefact) -- the autopsy-routed redesign that ADDED the modulatory_channel_route_range readiness gate (the V3-EXQ-662 statistic: does the channel range REACH the bias the authority rescales). That gate PASSED (0.180>=0.01) and consumed-spread passed (0.057>=0.05, marginal) yet C_R1B STILL false: even with the routed channel confirmed reaching the authority accumulator, committed entropy is not strictly above matched noise. Both runs are non_contributory (NOT weakens) -- they do NOT move ARC-065 (already provisional / substrate_ceiling). ADJUDICATION (confirmed failure_autopsy_569f-661-654a_2026-06-10, status=confirmed): ARC-065 + MECH-341 + MECH-294 + ARC-062 share ONE structural ceiling -- the V3 E3 committed-action / selection-authority coupling is INVARIANT to per-candidate upstream range (range present in the representation, no behavioural conversion; bit-identity = decorative channel). The FP-2 matched-entropy falsifier CANNOT score a contributory result on the current substrate. Real next action is /implement-substrate on the existing modulatory-bias-selection-authority entry (route channel range INTO the committed-action selection), THEN a readiness validation, THEN a 569h falsifier -- NOT another matched-entropy re-queue. Node STAYS in-progress (substrate-blocked, non-governance-weighting). No claims.yaml / scoring edits (569f/569g already non_contributory). last_updated 2026-06-09 -> 2026-06-14."
      governance_2026_06_07_pm: "GAP-A VALIDATED READY -- the documented resume condition is MET. V3-EXQ-649 (arc065_gapa_shared_candidate_summary_source) PASSed 2026-06-07T13:14Z: load-bearing C2 (e2_world_forward lifts consumed cand_world_summaries spread over the proposer source) PASS with ARM_1 consumed-summary spread 0.090 >= the 0.05 floor; the precondition_unmet adjudication flag was an indexer upper-bound false-positive (fixed on origin 4cad6af514/639e9e0a59). Confirmed by failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07 (status=confirmed; applied this /governance cycle). Status advanced blocked_pending_substrate -> in-progress. R1.a/R1.b matched-entropy work can now resume (queue V3-EXQ-569a successor) AND the cluster's downstream retests are unblocked: V3-EXQ-604c (MECH-314-family, supersedes the pre-fix non_contributory 604b), the MECH-341 committed-class diversity re-test (within-class-REPRESENTATIVE-diversity readout per autopsy Learning #2, GAP-B node), and the ARC-062/063 GAP-B falsifier. Companion curiosity-channel probe V3-EXQ-648a also confirmed load-bearing-ready (C2 PASS). ARC-065 substrate_queue entry amended (gapA_status=ready_validated; 604b + 649 failure_records appended)."
      substrate_landed_2026_06_07: "SHARED-CHANNEL E2-world-forward per-candidate signal preservation LANDED 2026-06-07 via /implement-substrate (session implement-substrate-arc065-gapa-e2wf-candidate-pool-20260607T0803Z), routed by failure_autopsy_V3-EXQ-614e_2026-06-07. The 614e autopsy relocated the committed-class-diversity bottleneck from the authority gate (GAP-B, resolved by V3-EXQ-643a) to this node (GAP-A candidate-pool class collapse; cand_world_pairwise_dist=0.0000). Fix: ree-v3 REEConfig.candidate_summary_source (proposer|e2_world_forward, default proposer/bit-identical) re-sources the SHARED cand_world_summaries consumed by lateral_pfc/ofc/mech295/gated_policy/tonic_vigor from the SD-056-trained e2.world_forward(z0,a_i) -- the shared-channel sibling of the curiosity-only MECH-314a Phase-2 fix (648a) and the generalisation of the GatedPolicy-only ARC-062 GAP-B first-action-onehot fix to ALL E3-side bias channels. agent.py _candidate_world_summaries helper consulted at all 5 cand_world_summaries fresh-build sites; 889 contracts + 7 preflight PASS (bit-identical OFF); 6 new contracts test_arc065_gapa_candidate_summary_source.py; 614e --dry-run unchanged. Status STAYS blocked_pending_substrate until the substrate-readiness validation V3-EXQ-649 (claim_ids=[]; candidate_summary_source=e2_world_forward + cand_world_pairwise_dist readiness precondition + shared-bias-channel per-candidate range readout) PASSes. On 649 PASS the node's R1.a/R1.b matched-entropy work can resume AND the MECH-341 committed-class diversity re-test (within-class-REPRESENTATIVE-diversity readout, NOT committed-class entropy per autopsy Learning #2) unblocks. Detector depends on a trained e2.world_forward (SD-056); the 649 readiness precondition guards vacuity (substrate_not_ready_requeue on an under-trained e2)."
      governance_2026_05_29: "Drift report freshness bump only; status remains in_progress / blocked_pending_substrate. The /implement-substrate work on the E2-world-forward per-candidate signal preservation (SD-056 contrastive next-state landed 2026-05-29 in ree-v3 main 041a974; substrate-readiness validation queued as V3-EXQ-613 by the sibling implement-substrate session) is now in flight. Next-step V3-EXQ-569a matched-entropy FP-2 falsifier will be queued post-V3-EXQ-613 PASS via /queue-experiment. IGW-20260528-008 remains stale pending V3-EXQ-613 outcome."
      resume_condition: "682-GATED NEXT STEP 2026-06-14 -- see governance_2026_06_14_pm2 for the AUTHORITATIVE corrected route (route-range REACH is DONE: ARM_1 applied route_range 0.18 in-arm; the residual is the gain-bounded additive CONVERSION). On V3-EXQ-682 landing -> read it -> /implement-substrate the gain/contrast amend ((a) contrast/normalization or gain bump; (b) shortlist-then-modulate fallback) -> readiness validation vs a verified-lifting matched-noise control -> V3-EXQ-569h with an in-arm route-range gate. The text below is RETAINED for history but its 'route channel range INTO selection' framing is SUPERSEDED (that reach is now achieved). SUBSTRATE-BLOCKED 2026-06-14. The FP-2 matched-entropy falsifier has now RUN TWICE on the 649-validated stack and CANNOT score a contributory result on the current substrate: V3-EXQ-569f (2026-06-10) and V3-EXQ-569g (2026-06-11, +route-range readiness gate) BOTH landed FAIL/non_contributory r1a_entropy_only_artefact (readiness MET, C_R1B selected-entropy-strict-above-matched-noise FALSE, committed entropy bit-identical across proposer/E2WF/matched-noise). Do NOT queue another matched-entropy falsifier (569h) on the current substrate -- it will reproduce r1a_entropy_only_artefact. RESUME path (per confirmed failure_autopsy_569f-661-654a_2026-06-10): (a) /implement-substrate the existing modulatory-bias-selection-authority entry so the routed per-candidate channel range RESCALES the committed-action selection (the shared A+B ceiling: range present, no behavioural conversion); (b) a substrate-readiness validation EXQ (claim_ids=[]) showing committed-action entropy MOVES with channel range; (c) THEN queue V3-EXQ-569h as the real FP-2 falsifier. ARC-065 is already provisional, so this is a falsifier/confirmation, not a promotion gate. HISTORY: V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path). V3-EXQ-569 matched-entropy sweep ran 2026-05-16 and was reclassified non_contributory at governance review: all 6 arms produced identical entropy (~0.496) because bias_fraction=0 for all diversity components -- the structured-vs-random comparison was never activated. V3-EXQ-571 PASS diagnostic confirmed F (forward model) dominates 88-89% of E3 score variance and ALL bias_fractions are machine-epsilon. V3-EXQ-573 10-arm bias-scale sweep (1x/5x/10x) reproduced the identical-arms collapse at 10x scale -> reclassified non_contributory; bias channel does not propagate at scale. V3-EXQ-609 per-candidate spread decomp (methodology fork from 571) surfaced curiosity emitting zero per-candidate vector. Root cause documented 2026-05-25 in evidence/planning/v3_exq_571_root_cause_2026-05-25.md: score_bias plumbing is correct, but the per-candidate signal is STRUCTURALLY ZERO -- all K candidates produce identical z_world after one E2 world-forward step (cand_world_pairwise_dist=0.0000) despite differing first actions. Same root cause as the 2026-05-17 ARC-062 GAP-B autopsy; that fix was scoped only to GatedPolicy. R1.a/R1.b cannot fire while the bias channel structurally carries no per-candidate variance. The /implement-substrate fix landed 2026-06-07 (SHARED-channel candidate_summary_source=e2_world_forward, re-sourcing cand_world_summaries from the SD-056-trained e2.world_forward) and V3-EXQ-649 PASS validated readiness (consumed-summary spread 0.090>=0.05). NEXT STEP DONE 2026-06-09: V3-EXQ-569f queued (ree-v3 db812e6) as the matched-entropy FP-2 falsifier successor on the 649 stack -- 3-arm single-variable design toggling candidate_summary_source (ARM_0 proposer / ARM_1 e2_world_forward / ARM_2 matched-noise T=2.5), claim_ids=[ARC-065], PRIMARY DV selected_action_class_entropy; R1.b PASS = ARM_1 strictly above BOTH matched-noise and proposer per matched seed (>=2/3) with readiness + e2-divergence floors met (supports); readiness/C1 unmet -> non_contributory (substrate_not_ready_requeue); readiness met + no lift -> weakens (R1.a entropy-only-artefact). On 569f landing: governance applies R1.a/R1.b to ARC-065. IGW-20260528-008 (this node's owning IGW item) advances from substrate-blocked to falsifier-in-flight."
    - id: "behavioral_diversity_isolation:GAP-B"
      title: "Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)"
      phase: "660 base PASS/supports established the binary within-class preserver; MECH-341 RATIFIED candidate->provisional (v3_pending CLEARED 2026-06-14, commit 80f4fcf250, user-directed). Only remaining unblocks strand = ARC-062 falsifier, gated on the shared GAP-A selection-authority substrate (569g->682-gated)"
      status: partial
      severity: load-bearing
      next_owner_exq: "NONE OWED on MECH-341 -- RATIFIED to provisional (2026-06-14). The graded-confirmation lineage RAN AND WAS RETIRED: V3-EXQ-660a (CEM pool-size dose-response K=16/32/64/128) landed FAIL 2026-06-11T03:26Z (C_GRADED graded on only 1/3 seeds) and its windowed-readout redesign V3-EXQ-660b landed FAIL 2026-06-11T13:43Z (C_GRADED 0/3 seeds; sensitivity gate cleared only marginally 0.0568 + non-monotonically); confirmed failure_autopsy_V3-EXQ-660b_2026-06-11 reclassified BOTH non_contributory (measurement_test_design_defect) and RETIRED the graded-in-K falsifier (it over-specifies a PRESERVATION claim) -- NO 660c. The STANDING GAP-B evidence is V3-EXQ-660 base PASS/supports (within-class-representative-diversity lift 4.862 vs legacy 4.781 nats; binary within-class preserver). MECH-341 exp_conf rose 0.794->0.871 (>0.62 gate) and the ratification DECISION is now MADE: commit 80f4fcf250 (2026-06-14T21:12Z, user-directed) cleared v3_pending + pending_retest_after_substrate and promoted MECH-341 candidate->provisional, ratifying the binary preserver as sufficient V3 evidence (the thin ~0.08-nat lift accepted; the committed-action CONVERSION caveat -- preserved diversity does not yet reach committed action per failure_autopsy_569f-661-654a -- carried in MECH-341's dated note + tracked downstream on GAP-A, NOT as a MECH-341 retest). The ONE remaining strand is ARC-062 (still candidate / v3_pending in unblocks_claims): it needs its own falsifier, gated on the SAME modulatory-bias-selection-authority substrate as GAP-A (per a6705dbb50, the 569g next step is 682-gated). Do NOT re-queue a graded within-class confirmation; do NOT re-open the MECH-341 ratification."
      owner_exq: "V3-EXQ-660b TERMINAL FAIL 2026-06-11T13:43Z is the lineage FRONTIER (reclassified non_contributory / measurement_test_design_defect at governance cycle #5; the graded-in-K falsifier is RETIRED, no 660c; NOT a weakens) -- owner_exq leads with the frontier letter as of the 2026-06-12 closure-drift reconcile (advancing 660 -> 660b, the same convention as this cycle's 514m->514n / 485e->485f advances) so the structural lineage-advanced flag clears; the STANDING GAP-B EVIDENCE is UNCHANGED = predecessor V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z for MECH-341 (within-class-representative-diversity lift 4.862 vs legacy 4.781 nats; the binary within-class preserver is established). Owner re-pointed 660b -> 660 at governance cycle #5 2026-06-11 per confirmed failure_autopsy_V3-EXQ-660b: the graded-in-pool-size ratification the 660a/660b lineage was chasing is REMOVED AS A GATE (graded-in-K over-specifies a PRESERVATION claim), not outstanding -- no 660c. RETIRED graded-falsifier lineage: V3-EXQ-660b TERMINAL FAIL/weakens 2026-06-11T13:43Z (windowed-readout redesign of 660a, supersedes 660a; both readiness gates passed yet C_GRADED 0/3 seeds, sensitivity gate cleared only marginally 0.0568 + non-monotonically) was reclassified non_contributory (measurement_test_design_defect) at cycle #5, NOT a weakens; V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS"
      unblocks_claims: [MECH-341, ARC-062, ARC-065]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-B", "sd_037_axis_b:P1b"]
      last_updated: 2026-06-14
      governance_2026_06_14c: "RATIFICATION RESIDUAL RECONCILE (session reconcile-mech341-ratification-residual-20260614T2230Z). The MECH-341 ratification landed via commit 80f4fcf250 (2026-06-14T21:12Z, user-directed) which edited ONLY claims.yaml + claims.json -- it did NOT update this closure node or the decision ledger, leaving residual drift the subsequent governance cycle (a2d949d506) also did not sweep: the pipeline regenerates DERIVED files from claims.yaml (so promotion_demotion_recommendations.md correctly dropped MECH-341's hold row) but it does NOT edit hand-authored closure-node prose, and decision_state.v1.json kept echoing the stale 2026-05-31 applied hold because the promotion bypassed the decision_log. FIXED HERE: (1) this node's phase/next_owner_exq/resume_condition updated to record MECH-341 candidate->provisional / v3_pending CLEARED, leaving ARC-062 as the sole open strand (gated on the GAP-A 569g->682 selection-authority substrate); (2) recorded the ratification in decision_log.v1.jsonl (promote_to_provisional / applied) so decision_state.v1.json stops showing MECH-341 as hold_pending_v3_substrate. Supersedes the incidental 'MECH-341 stays candidate / v3_pending' clauses in the same-day _pm and earlier notes. Node STAYS partial (ARC-062 open). NO claims.yaml edits (ratification already authoritative)."
      governance_2026_06_14_pm: "DOWNSTREAM CROSS-PLAN DEPENDENT registered: sd_037_axis_b:P1b is upstream_blocked on the committed-action-diversity demonstration shared by GAP-A/GAP-B. On the GAP-A 569-lineage falsifier PASS (and/or the ARC-062 falsifier on the modulatory-bias-selection-authority substrate) confirming scoring-layer diversity reaches committed action, ALSO revisit sd_037_axis_b:P1b -> queue V3-EXQ-625d (joint composite). Reverse link to the existing P1b->GAP-A/B forward link (P1b reconciled to upstream_blocked 2026-06-14, commit b4c062022c). Link edit ONLY -- MECH-341 stays candidate / v3_pending; no status/scoring/claims.yaml change."
      governance_2026_06_14: "DRIFT RECONCILE (read-only-report follow-up; session reconcile-bdiv-cluster-drift-20260614T1911Z). The governance NOTES were reconciled (06-11c retired the graded falsifier) but three FIELDS were still stale and surfaced in the closure_status.md snapshot: (1) phase: still read 'temperature-graded confirmation + governance ratification owed'; (2) next_owner_exq: still described V3-EXQ-660a as 'QUEUED / the OWED graded confirmation'; (3) resume_condition: still listed 'a temperature-GRADED within-class confirmation' as resume path (a). ALL THREE corrected to the post-660b reality: the graded-in-K falsifier RAN (660a FAIL, 660b FAIL) and is RETIRED non_contributory (no 660c); MECH-341 = established BINARY within-class preserver (660 base PASS, exp_conf 0.871) held candidate / v3_pending; the only remaining items are a governance ratification DECISION (not an experiment) + ARC-062's falsifier (shared selection-authority substrate). NO claims.yaml / manifest / scoring edits; MECH-341 stays candidate / v3_pending=true. Node STAYS partial. last_updated 2026-06-13 -> 2026-06-14."
      governance_2026_06_13: "Closure-drift stale-since-review ACKNOWLEDGE (governance cycle 2026-06-13T20:12Z). Flagged only because failure_autopsy_V3-EXQ-655_2026-06-13 reclassified MECH-341 (in this node's unblocks set) to non_contributory/substrate_ceiling. Does NOT change GAP-B: 655 is a distinct INV-074-cluster task-shift necessity test, and MECH-341's standing within-class-diversity-preservation evidence (V3-EXQ-660 base PASS) is untouched; the reclassification is consistent with the node already being substrate-blocked. last_updated bumped to acknowledge; node STAYS partial. No owner_exq / status / claims.yaml changes."
      governance_2026_06_12: "Closure-drift stale-since-review RECONCILE (governance cycle 2026-06-12; supersedes the same-day acknowledgement-only note). The morning cycle bumped last_updated but LEFT owner_exq pinned to base V3-EXQ-660, so the stale-since flag PERSISTED: the closure_drift `lineage_advanced` branch is purely STRUCTURAL (not date-gated) -- it fires whenever owner_exq's leading EXQ id pins an earlier lineage letter than a same-stem sibling with terminal evidence (660b), and no last_updated bump can clear it (verified: the node was already last_updated=2026-06-12 and still flagged). FIX: advanced owner_exq's leading id 660 -> 660b (the lineage frontier), matching the convention used for the OTHER stale nodes this cycle (goal_pipeline:GAP-2 514m->514n, commitment_closure:GAP-8 485e->485f) where owner_exq points at the frontier letter even when that letter is a non_contributory FAIL. This is a POINTER advance only -- the STANDING GAP-B EVIDENCE is UNCHANGED: predecessor V3-EXQ-660 base PASS/supports remains the MECH-341 within-class-representative-diversity result (lift 4.862 vs legacy 4.781 nats; binary within-class preserver established), and the 660a/660b graded-in-K falsifier lineage stays RETIRED non_contributory (measurement_test_design_defect per confirmed failure_autopsy_V3-EXQ-660b; NOT a weakens; no 660c). 660b manifest evidence_direction=non_contributory + node Case-3 self-tag keep the owner-pass in Suppressed (not Drifted). NO claims.yaml / manifest / scoring edits; MECH-341 stays candidate / v3_pending=true (uncleared). Node STAYS partial. Re-ran check_closure_drift.py: stale_since_review 1 -> 0, drifted_nodes 0."
      governance_2026_06_11b: "WINDOWED-READOUT REDESIGN RAN + FLAGGED FOR AUTOPSY; owner_exq repointed 660a -> 660b (lineage advance per closure-drift stale-since-review). V3-EXQ-660b (the 660a successor routed by failure_autopsy_V3-EXQ-660a; windowed H(rep|class) over fixed 50-tick windows + a readout-sensitivity readiness gate; supersedes 660a) LANDED FAIL/weakens 2026-06-11T13:43Z (manifest v3_exq_660b_mech341_within_class_pool_size_graded_windowed_readout_20260611T134330Z_v3). The redesign WORKED as instrumentation: BOTH readiness gates PASSED -- input availability rises 4.99->33.84 across K AND the sampled windowed-H range across K = 0.0568 >= the 0.05 floor (the 660a saturation defect is fixed; readout is demonstrably sensitive) -- and criteria_non_degenerate.C_GRADED=true. Yet the load-bearing C_GRADED still scored 0/3 seeds: per-seed deltas (sampled-legacy) are noise around zero, non-monotone, mostly negative (seed 43 all negative; seed 42 {-0.05,+0.10,-0.03,-0.01}; seed 44 {-0.03,+0.04,+0.04,+0.04}). By 660b's own pre-registration (both gates met -> a flat lift is a GENUINE weakens) this would weight MECH-341's graded sub-axis. DISPOSITION (governance cycle #4): USER FLAGGED 660b for /failure-autopsy rather than stamping weakens inline -- it is the 3rd readout iteration on this same graded sub-axis (660 temperature byte-identical -> 660a saturated -> 660b windowed) and the sensitivity gate cleared only MARGINALLY (0.0568) and NON-MONOTONICALLY (windowed-H by K = 0.987/1.044/1.020/1.037), so the autopsy must adjudicate genuine-falsification-of-the-graded-sub-axis vs below-resolution / MECH-341-is-binary-not-graded BEFORE any evidence stamp. 660b LEFT PENDING (not marked reviewed, no evidence_direction override this cycle); the manifest's self-emitted weakens stands until the autopsy adjudicates. MECH-341 stays candidate / v3_pending=true / pending_retest_after_substrate; 660's core within-class-lift PASS (score-layer diversity-preservation role, 614a/569d) is preserved regardless. Node STAYS partial. NEXT: /failure-autopsy V3-EXQ-660b."
      governance_2026_06_11c: "AUTOPSY APPLIED + GRADED FALSIFIER RETIRED. Confirmed failure_autopsy_V3-EXQ-660b_2026-06-11 consumed at governance cycle #5 2026-06-11T20:16Z. V3-EXQ-660b weakens -> non_contributory (measurement_test_design_defect) on flat+nested run-pack manifests + narrow_supports_flag + pending_retest; scoring-excluded. Two compounding reasons the weakens does not hold: (1) the readout-sensitivity gate cleared only MARGINALLY (windowed-H range 0.0568 vs 0.05) and NON-MONOTONICALLY (windowed-H by K = 0.987/1.044/1.020/1.037 -- positive control does not track K), so a flat lift is not a clean negative; (2) graded-in-pool-size OVER-SPECIFIES MECH-341's diversity-PRESERVATION assertion (binary preserve-or-collapse, not a K-graded dose-response). Three convergent iterations (660 inert temperature -> 660a saturated -> 660b marginal/non-monotone) RETIRE the graded-in-K falsifier: no 660c. owner_exq re-pointed 660b -> 660 (the standing PASS); the within-class lever is recorded as a BINARY load-bearing preserver and the graded ratification is removed as a gate, NOT outstanding. ALSO corrected a latent scoring bug surfaced this cycle: the NESTED 660a run-pack manifest still read weakens (an earlier cycle reclassified only the FLAT 660a manifest; the indexer scores from nested runs/**/manifest.json) -- mirrored the already-decided non_contributory onto the nested manifest. Net MECH-341 genuine_exp weakens 2 -> 0, supports 3; exp_conf 0.794 -> 0.871, still v3_pending -> promotion HELD. No substrate_queue entry (input availability rose correctly 4.99->33.84; not a substrate gap). No demotion; MECH-341 stays candidate / v3_pending / pending_retest_after_substrate. Node STAYS partial (v3_pending uncleared; the within-class GRADED sub-axis is unestablished and retired-as-gate). last_updated 2026-06-11 (same-day reconcile)."
      governance_2026_06_11: "GRADED CONFIRMATION RAN + FLAGGED FOR AUTOPSY. V3-EXQ-660a (the owed graded-confirmation successor; CEM pool-size dose-response K=16/32/64/128, supersedes nothing -- 660 stays standing evidence) LANDED FAIL/weakens 2026-06-11T03:26Z (manifest v3_exq_660a_mech341_within_class_pool_size_graded_confirmation_20260611T032653Z_v3). Preconditions MET: non-vacuity within-class availability rises 4.99->33.8 across K (the axis MOVES, unlike the inert temperature knob), CEM pool honored. C_GRADED FAILED: per-seed dose-response graded on only 1/3 seeds (seed 42 monotone, margin 0.347, graded; seeds 43/44 non-monotone, margins 0.057/0.319) -- needs >=2/3. Self-route FAIL_lift_not_graded_fixed_structural_artifact_independent_of_pool_size: the ~0.08-nat within-class lift 660 established is real + load-bearing but does NOT scale with available within-class diversity. DISPOSITION (governance 2026-06-11T05:50Z): USER FLAGGED 660a for /failure-autopsy -- the 1/3-graded result is treated as not-yet-explained; adjudicate whether the weakens should weight MECH-341 or be scoped to the graded sub-axis (660's core within-class lever PASS is preserved either way) BEFORE any evidence stamp. 660a LEFT PENDING (not marked reviewed, no evidence_direction override applied this cycle); the manifest's self-emitted weakens stands until the autopsy adjudicates. MECH-341 stays candidate / v3_pending=true / pending_retest_after_substrate (promote/demote suppressed regardless). Node STAYS partial: 660 base supports absorbed + standing; the graded ratification 660a was to deliver is NOT achieved (and is now an autopsy work-item, not a re-queue). last_updated bumped 2026-06-10 -> 2026-06-11. NEXT: /failure-autopsy V3-EXQ-660a."
      governance_2026_06_10: "V3-EXQ-660 LANDED 2026-06-10T04:41Z PASS / supports (manifest v3_exq_660_mech341_within_class_representative_diversity_20260610T044109Z_v3; evidence_direction_per_claim[MECH-341]=supports; reviewed). The owed GAP-B action is DONE at the run level and folded into claims.yaml the same day: the [2026-06-10 governance: V3-EXQ-660 supports, v3_pending HELD] note on MECH-341 records C1 substrate-operative + within-class branch active + multi-rep available (majority); C2 within-class-REPRESENTATIVE-diversity lift PASS (swept 4.862 vs legacy 4.781 nats); committed-CLASS (across-class) entropy flat = EXPECTED negative control (secondary, not a gate). This is the corrected-readout retest the 614e autopsy Learning #2 required (H(rep_signature | committed_class), NOT committed-class entropy). The resume_condition's C1+C2 branch fired -- but governance HELD v3_pending rather than clearing it, on two caveats: (1) the lift margin is THIN (~0.08 nats vs 0.05 threshold); (2) the three temperature arms T=0.5/1.0/2.0 produce BYTE-IDENTICAL within-class entropy (4.861916; 196/1105/255 samples) -- the lever fires but is INSENSITIVE to temperature magnitude (only legacy-vs-any-sweep differs). So 660 confirms the within-class sub-axis is LOAD-BEARING but does not yet show a graded, ratifiable response. DISPOSITION: MECH-341 stays candidate / v3_pending=true (no promotion, no auto-flip of the within-class default); 660 supersedes 614e (already non_contributory). Node STAYS partial: the run is absorbed (not pending, not lost), but v3_pending is not cleared and ARC-062 in unblocks_claims is untouched. Plan-doc reconcile only -- claims.yaml + manifest + review_tracker already current; no claims/scoring edits this session. last_updated bumped 2026-06-09 -> 2026-06-10."
      governance_2026_06_09_pm: "V3-EXQ-660 QUEUED via /queue-experiment 2026-06-09T21:33Z (session queue-mech341-gapb-within-class-rep-diversity-20260609T2117Z) -- the owed GAP-B action, unblocked by V3-EXQ-649 GAP-A readiness PASS + the 614e autopsy Learning #2. Forked from 614e with the CORRECTED matched readout: PRIMARY DV C2 = within_class_rep_cond_entropy = H(rep_signature | committed_class), where rep_signature is the post-first-action argmax signature of agent.e3._last_selected_trajectory (which within-class representative is selected inside the committed class), expected to RISE with the swept within-class temperature {None=legacy argmin,0.5,1.0,2.0}. Committed-class (across-class) entropy is now only a SECONDARY negative-control (expected flat per 614e; NOT a gate). All 4 arms arm GAP-A (candidate_summary_source=e2_world_forward), authority (use_modulatory_selection_authority=True gain=0.5), SP-CEM, MECH-341, SD-056. C1 non-vacuity gate (within-class branch fires AND committed class offers >=2 distinct representatives, majority swept-arm seeds) asserts the SAME within-class-representative axis C2 routes on; C1 FALSE self-routes substrate_not_ready_requeue -> non_contributory (protects MECH-341 from a false weakens). Evidence-direction: C1-fail->non_contributory / C1+C2->supports / C1 + C2-fail->weakens. ree-v3 main bf06d8a; ingested into coordinator /queue/active. NO claims.yaml/governance edit; MECH-341 stays candidate / v3_pending. Node stays partial pending the run + a later /governance fold-in. last_updated bumped."
      governance_2026_06_09: "Closure-drift stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-654_2026-06-09 (confirmed, applied this cycle) touches ARC-062, which is in this node's unblocks_claims. That autopsy adjudicates the arc_062 GAP-B *rule-apprehension* falsifier (V3-EXQ-654) as non_contributory / substrate_ceiling (CandidateRuleField per-episode cold-start; C1c readiness FAIL gated out the DV) and does NOT reclassify ARC-062's status (stays candidate / substrate_ceiling / v3_pending) -- so it does not change this node's disposition. This node's real outstanding work is the distinct MECH-341 within-class-representative-diversity retest on the GAP-A-ready substrate (still owed, not queued). Node stays partial; last_updated bumped to acknowledge."
      governance_2026_06_08: "Plan-drift reconcile. The prior 2026-06-08 freshness note for V3-EXQ-610f remains true but incomplete. The V3-EXQ-542a overlap is also a false-positive for this node (ARC-062 substrate-readiness lineage, not the 614-lineage MECH-341 question). V3-EXQ-614e has now been autopsied and applied: non_contributory substrate_ceiling, MECH-341 not weakened, and the bottleneck moved upstream to GAP-A. GAP-A readiness is now validated by V3-EXQ-649 PASS, so this node stays partial with the next real action being a MECH-341 GAP-A-ready retest using the within-class-representative-diversity readout."
      governance_2026_06_07: "Lineage advance: V3-EXQ-614e (manifest v3_exq_614e_mech341_within_class_temperature_authority_on_20260607T070701Z_v3) landed 2026-06-07T07:07Z and supersedes 614d -- the FIRST within-class-temperature behavioural test on the now-VALIDATED modulatory-bias-selection-authority substrate (V3-EXQ-643a PASS, float32 catastrophic-cancellation fix). Unlike 614d (lever ACTIVE but ZERO committed-action authority), 614e ran with use_modulatory_selection_authority=True+gain=0.5 so the lever is OPERATIVE: C1 substrate-operative=True (within-class branch + Site-2 authority normalization fire; ARM_0 committed entropy non-degenerate) AND C3 readiness=True, yet C2 (committed_class_entropy rises with within-class temperature) STILL =False across all arms. So even with operative committed-action authority, within-class temperature produces NO committed-class diversity lift -- the fourth convergent committed-action-authority/no-lift instance on this node. Script self-emitted evidence_direction=weakens on MECH-341; /governance 2026-06-07 DEFERRED it weakens->non_contributory (manifest + runpack edited, index rebuilt: MECH-341 reverts to 2 supports:0 weakens, exp_conf 0.809) and ROUTED 614e to /failure-autopsy (user directive) to adjudicate clean-falsifier-of-MECH-341 vs monostrategy/GAP-B substrate-ceiling (no class diversity for E3 scoring to preserve). 614e NOT marked reviewed -- stays pending as the autopsy work-list. MECH-341 stays candidate / v3_pending=true; no confidence move. Node stays partial. last_updated bumped."
      governance_2026_06_06: "Closure-drift stale-since-review acknowledgement only (no status change). Flagged because failure_autopsy_V3-EXQ-608-611c_2026-06-06 (confirmed) reclassified MECH-341 in this node's unblocks set. That autopsy adjudicates the 611c substrate-readiness PASS as vacuous-pass-class (gate carried by a temperature-invariant C2 + near-vacuous C3; fires != preserves) and the 608/611 self-route epsilon as a measurement-design defect; routing=governance-record-only, recommended_substrate_queue_entry.action=none (the modulatory-bias-selection-authority gate already lists MECH-341 in unblocks_claims and gates the efficacy re-test). MECH-341 stays candidate / v3_pending=true; no confidence move. This is the SAME committed-action-authority finding already captured in governance_2026_06_03 (614d third convergent instance) -- node disposition unchanged, stays partial owed to the newly-implemented authority substrate. last_updated bumped to acknowledge."
      governance_2026_06_03: "614c lineage RESOLVED -- this row no longer waits on 614c. (1) V3-EXQ-614c ran 2026-06-01T12:45Z FAIL (manifest v3_exq_614c_mech341_stratified_within_class_temperature_sweep_20260601T124509Z_v3), reclassified evidence_direction=non_contributory per failure_autopsy_V3-EXQ-614c_2026-06-01 (status=confirmed): both failing criteria are test-design defects -- C2 vacuous score-layer-argmin metric is temperature-invariant; C1 mis-specified per-seed band vs cross-seed mean; C3 substrate-readiness PASS 3/3 (instrumentation_defect, NOT substrate_ceiling). Already in review_tracker reviewed_run_ids + discussed_experiment_dirs; pending_retest gated on the corrected harness. (2) Corrected-harness successor V3-EXQ-614d (supersedes 614c) ran 2026-06-03T12:01Z and was reviewed same day (session review-614d-mech341-20260603T144832Z): interpretation_label PASS_C1_C3_only_within_class_active_no_committed_class_lift; evidence_direction=mixed; experiment_purpose=diagnostic (scoring-excluded). C1 (cross-seed mean vs 614b ALL_ON 0.80 band) PASS; C3 (within-class branch fires 3/3 seeds, 159-1030 samples) PASS; C2 (committed-class temperature lift) FAIL -- committed-class entropy byte-identical 1.056572 at T=0.5/1.0/2.0 (legacy 1.057734), 0/3 paired-lift seeds per arm. FINDING: the within-class temperature lever is ACTIVE but has ZERO committed-action authority -- the THIRD convergent instance of the modulatory-bias-selection-authority gap (604a curiosity, 624a vigor, 614d within-class temperature; scoring-layer signals do not reach the committed argmax). This retroactively corrects the governance_2026_06_01 hope that the SD-056 amend would transitively unblock the cross-plan beneficiaries: the amend stabilised the substrate but the within-class lever alone does not deliver committed diversity. DISPOSITION (user-approved): MECH-341 stays candidate / v3_pending=true -- do NOT clear; dated note added to MECH-341. SUBSTRATE: the modulatory-bias-selection-authority gate CLEARED 2026-06-03; that substrate was IMPLEMENTED 2026-06-03T15:20Z via /implement-substrate (session implement-substrate-modulatory-bias-selection-authority-20260603T145832Z; approach b gap-relative scaling: E3Config.use_modulatory_selection_authority + modulatory_authority_gain=0.5 + min_range_floor=1e-6; e3_selector.select additive-chain + MECH-341 bonus rescaled to gain*raw_score_range; e3_score_diversity.stratified_select across-class unit-range normalization = the 614d C2 fix; primary scores unmodified; 734/734 contracts + 7/7 preflight PASS flag-OFF bit-identical) -- substrate_queue entry modulatory-bias-selection-authority now status=implemented_pending_validation (ready=false), MECH-341 added to its unblocks_claims, 614d added as 3rd failure_record, implementation_hint unified across MECH-314 curiosity / MECH-320 vigor / MECH-341 within-class temperature (one shared committed-action-authority bottleneck, build the arbitration channel once). NEXT STEP: queue the modulatory-bias-selection-authority substrate-readiness validation EXQ via /queue-experiment (priority-1 substrate_queue lane) -- NOT a re-spec'd 4-arm within-class sweep on the current substrate (614d already proved the within-class lever has no committed authority pre-authority-substrate). After that validation passes, queue the MECH-341 committed-class diversity re-test. Status stays partial: 614c/614d fully absorbed (NOT pending, NOT lost) but MECH-341 not cleared and the committed-action authority is owed to the newly-implemented substrate; do NOT promote to done. Plan-doc reconcile only -- no claims.yaml/manifest/scoring edits this session (MECH-341 dispositions + substrate_queue edits already landed under the 614d review + /implement-substrate sessions)."
      governance_2026_06_01: "V3-EXQ-614b FAIL (manifest v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended_20260531T182040Z_v3) confirmed C1 structurally degenerate (B_only Rung-1 majority=False; per-seed frac_pre_ge2=0.0 -- CEM proposer collapses to single-class candidate pools without SP-CEM Layer A) AND C2 necessity_delta 0.087 just below pre-amend 0.1 threshold. C3 ALL_ON Rung-1 PASSed at 0.800 nats (highest of any 614-lineage run -- positive substrate-readiness for SD-056 amend at behavioural-runtime horizon). Failure-autopsy V3-EXQ-616 Sections 7 + 10 named the contingent path: stratified_temperature default + A-vs-B partial-redundancy probe; this path activated by 614b FAIL_C1. MECH-341 amend landed 2026-06-01 via /implement-substrate (session implement-substrate-mech-341-amend-stratified-temp-ab-probe-20260601T063226Z): (a) E3ScoreDiversity gains stratified_within_class_temperature: Optional[float] = None lever -- within each first-action class, when set, sample representative via softmax(-class_scores / T); legacy argmin when None (bit-identical OFF). Decoupled from existing across-class stratified_temperature (default 1.0; unchanged). (b) A-vs-B partial-redundancy probe lever satisfied by the existing independent flags use_support_preserving_cem (Layer A) and use_e3_score_diversity (Layer B) -- compose to A_only / B_only / BOTH / NEITHER. No new code flag added (would be redundant); the lever IS the existing flag composition. NO flip of use_differentiable_cem default (SD-055 safety note preserved). 655/655 contracts + 7/7 preflight PASS post-amend with master OFF and amend OFF. Validation: V3-EXQ-614c queued 2026-06-01 (4-arm within-class temperature sweep {None=legacy, 0.5, 1.0, 2.0} on SD-056-amended baseline). Cross-plan: amend transitively unblocks arc_062_rule_apprehension:GAP-B (V3-EXQ-543l successor cohort) under shared SD-056-amended substrate. Status remains partial pending 614c outcome; do NOT promote to done."
      governance_2026_05_31: "V3-EXQ-614a landed 2026-05-30T19:32Z PASS (manifest v3_exq_614a_mech341_p3_behavioural_falsifier_3arm_20260530T193245Z_v3) with interpretation_label PASS_C2_C3_only_mech341_load_bearing_in_stack_only per behavioral_diversity_isolation_plan R2.c rule. Routing under the script's 4-row interpretation grid: 'PASS via C2+C3 only -> /governance MECH-341 supports load-bearing + Q-054 entropy_bias_scale sweep'. Governance cycle 2026-05-31 applied evidence_direction_per_claim[MECH-341]=supports + evidence_direction_per_claim[ARC-065]=supports to claims.yaml. Companion PASSes in same cycle: V3-EXQ-569d (floor-recal FP-2 falsifier supersedes 569c) and V3-EXQ-615 (Rung-1 matched-entropy on rescued substrate). ARC-065 v3_pending + pending_retest_after_substrate cleared. MECH-341 stays candidate / v3_pending=true pending V3-EXQ-569e mechanism-dissociation autopsy interpretation (569e was a Pathway A vs B diagnostic FAIL flagged for /failure-autopsy). NEXT STEP per interpretation grid: queue Q-054 entropy_bias_scale sweep via /queue-experiment (Q-054 sweep across entropy_bias_scale magnitudes to determine the load-bearing scale range of mech341). GAP-B status flipped 'blocked' -> 'partial' 2026-05-31T11:08Z after closure-drift walk with operator: load-bearing evidence collected on MECH-341 (supports) + ARC-065 (supports, v3_pending cleared) -- 1-of-3 unblocks_claims closed + partial-PASS on the principal claim is more accurately 'partial' (CLOSURE_STATUS_WEIGHTS=0.5) than 'blocked' (0.1). Remaining work (Q-054 sweep V3-EXQ-616 queued same session + Phase P4 11-arm matrix + V3-EXQ-569e autopsy on MECH-341) is forward-progress, not re-block. Still NOT 'done': MECH-341 stays candidate / v3_pending=true pending 569e autopsy + Q-054 magnitude-load result; ARC-062 not yet addressed by this owner. Drift script tightened in the same session to read manifest evidence_direction so the GAP-1 / GAP-2 false positives stop firing."
      governance_2026_05_31_midday: "Case 3 in closure-drift terms: legitimately non-terminal partial. Midday governance applied V3-EXQ-569e autopsy verbatim (verdict=INSTRUMENTATION_FAILURE; diagnostic, non-weighting; evidence_direction_per_claim[ARC-065]=mixed, [MECH-341]=mixed; SD-056 multistep amend landed at 11:25Z with V3-EXQ-617 substrate-readiness PASS at 11:31Z); MECH-341 v3_pending=true preserved pending the SD-056 amend-and-re-run cycle on the corrected substrate. V3-EXQ-616 Q-054 entropy_bias_scale sweep also queued same morning is the second outstanding forward-progress item. GAP-B partial status remains correct; do NOT promote to done."
      governance_2026_05_31_afternoon: "V3-EXQ-614b queued 2026-05-31T12:32Z via /queue-experiment as the amend-and-re-run leg of the SD-056 amend-and-re-run cycle flagged in the midday note. Re-runs the 614a 3-arm behavioural falsifier (ARM_0 B_only / ARM_1 ablate_B / ARM_2 ALL_ON) on the SD-056-amended substrate. User-confirmed via AskUserQuestion 2026-05-31T12:31Z: BOTH SD-056 amend levers ON in all 3 arms (Lever (a) multi-step contrastive h=5 + Lever (b) per-step output norm clamp ratio=2.0; t=1 contrastive also ON), held constant across the diversity-axis comparison so R2.c interpretation is not confounded by amend on/off being correlated with A/B/C/D axis state. Acceptance criteria UNCHANGED (C1/C2/C3 + PASS = C1 OR (C2 AND C3)); 4-row interpretation grid UNCHANGED with header note clarifying that under the amended substrate PASS via C1 (R2.c MECH-341 isolation) is now the load-bearing target since 614a established PASS via C2+C3. Cross-plan: same Layer-B substrate stabilisation unblocks arc_062_rule_apprehension:GAP-B (V3-EXQ-543l successor cohort) under shared SD-056-amended substrate -- note flagged in queue entry rationale. Sibling concurrent /queue-experiment session for V3-EXQ-569a (ARC-065 GAP-A) holds disjoint script path; coordinated via user-approved re-read-before-write protocol. Status remains partial pending 614b outcome + 569e autopsy claim-narrowing + Q-054 magnitude-load result."
      resume_condition: "MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated commit-coupling fix; see GAP-A resume_condition + a6705dbb50). Do NOT re-open the MECH-341 ratification and do NOT re-queue a graded within-class confirmation. HISTORY (MECH-341 strand, now closed): PARTIAL 2026-06-10. V3-EXQ-660 LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-queue it; its C1+C2 branch fired and governance is folded into claims.yaml. The within-class-representative sub-axis is load-bearing-CONFIRMED; v3_pending was HELD on two caveats: thin lift margin (~0.08 nats vs 0.05) and byte-identical entropy across T=0.5/1.0/2.0 (lever fires but is temperature-INSENSITIVE). The graded-confirmation route is RETIRED -- V3-EXQ-660a (pool-size dose-response) + V3-EXQ-660b (windowed redesign) BOTH FAILed and confirmed failure_autopsy_V3-EXQ-660b_2026-06-11 reclassified them non_contributory and removed graded-in-K as a gate (it over-specifies a PRESERVATION claim; no 660c). So the path is NOT another experiment but (a) a governance ratification DECISION on whether the established binary within-class preserver (660 base PASS, exp_conf 0.871) clears v3_pending despite the thin ~0.08-nat lift AND despite preservation being a scoring-layer property that does NOT reach committed action (the shared selection-authority ceiling, per failure_autopsy_569f-661-654a) -- governance has HELD it; or (b) clearing that ceiling via the GAP-A modulatory-bias-selection-authority substrate fix so the preserved diversity demonstrably reaches behaviour, then ratify. Until then MECH-341 stays candidate / v3_pending=true. Separately, ARC-062 (in unblocks_claims) remains unaddressed by this owner. Ignore V3-EXQ-542a/610f overlap flags for this node; they do not change the 614-lineage question."
    - id: "behavioral_diversity_isolation:GAP-C"
      title: "Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)"
      phase: "P1"
      status: in-progress
      severity: medium
      owner_exq: "V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling"
      unblocks_claims: [MECH-313, MECH-260, Q-045]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-H"]
      last_updated: 2026-06-15
      governance_2026_06_15: "603p GATE-CHECK -> BLOCKED-ON-603p (session gapc-603p-gatecheck-603q-spec-20260615T0439Z). Coordinator DB (run-state authority) checked for V3-EXQ-603p: status=claimed by ree-cloud-2 (claimed 2026-06-14T23:36:59Z), live heartbeat state=running ~42.6% (run 5/12, Seed 44/ARM_REGIME_0p12) as of 2026-06-15T04:38Z, results table EMPTY (no manifest in evidence/experiments/, no outcome) = NOT yet run. Per the follow-on Branch-C rule: V3-EXQ-603q is NOT queued and the located parameter is NOT guessed. CORRECTS THE STALE 06-14 FRAMING below: 603o is NOT 'NOT yet queued' -- it RAN 2026-06-11 (manifest v3_exq_603o_escape_affordance_bridge_behavioural_redesign_20260611T213609Z_v3) carrying both 603l-autopsy fixes (headroom: num_hazards 4->6 / proximity_harm 0.10->0.15; CONTINUOUS mean-survival primary metric) and self-routed substrate_not_ready_requeue, failing ONLY the harm_landscape_discriminative_on_base gate (harm_eval_range >= 0.02 on 1/3 seeds at proximity_harm=0.15) while the continuous bridge lift was already STRONG (both arms ~50.3 vs base ~18.65). V3-EXQ-603p (claim-free diagnostic, claim_ids=[], prio 285; queued 2026-06-14) is the diagnose-first locator for that one failing gate: BASE-arm-only, 4 cells x 3 seeds, Stage-H only, proximity_harm {0.10 positive-control, 0.12, 0.15} at harm_lr=1e-3 + a {0.15, harm_lr=3e-3} training-strength rescue cell, keyed on the same harm_eval_range >= 0.02 statistic. DURABLE 603q SPEC (fires once 603p LANDS with a usable result = Branch A): (1) extract the LOCATED PARAMETER from 603p -- the proximity_harm value (and/or harm_lr) at which harm_eval_range >= 0.02 clears on >=2/3 seeds; (2) /queue-experiment V3-EXQ-603q = the corrected SD-059/MECH-358 escape-affordance-bridge EVIDENCE re-run (experiment_purpose=evidence, NOT a diagnostic): the 603o design (full bridge ON vs base arms; CONTINUOUS survival metric retained, NOT the saturating binary median>=75 gate) with proximity_harm/harm_lr set to the located value so harm_landscape_discriminative_on_base now clears on >=2/3 seeds as a non-vacuity precondition (self-route substrate_not_ready_requeue if unmet); PRIMARY DV best-bridge continuous-survival strictly > base on >=2/3 seeds -> supports settles SD-059/MECH-358; (3) re-evaluate claim_ids from scratch per the accuracy rule -- tag [SD-059, MECH-358] only if the run produces interpretable bridge signal for them. BRANCH-B OFF-RAMP (do NOT queue 603q): if 603p's 0.10 POSITIVE CONTROL fails harm_eval_range>=0.02 on >=2/3 seeds, the harm pathway/metric is broken (not a regime issue) -> route to /failure-autopsy or /implement-substrate on the Stage-H harm-valuation pathway. AFTER 603q (flag only, NOT this session): the Q-045/MECH-313/MECH-260 4-arm tonic-noise ablation (MECH-313 OFF / 313-only / 260-only / both-ON) is the actual GAP-C falsifier (degeneracy pre-check warranted -- a non-propagating noise channel would reproduce the GAP-A r1a_entropy_only_artefact outcome). Interim 603p heartbeat lines show the 0.10 control PASSing on seed 42 (harm_range 0.1665, floor 0.02) -- encouraging but 1/3 seeds, NOT a verdict; not acted on. Node STAYS in-progress (non-governance-weighting); MECH-313/MECH-260/Q-045 retest still owed; SD-059/MECH-358 unchanged; 603l manifest untouched. Plan-doc edit ONLY; no claims.yaml/experiment/runner. last_updated 2026-06-14 -> 2026-06-15."
      governance_2026_06_14: "DRIFT RECONCILE (read-only-report follow-up; session reconcile-bdiv-cluster-drift-20260614T1911Z). The resume_condition field was STALE: it still said 'IN FLIGHT 2026-06-08 on V3-EXQ-603i', but the entire 603i/j/k/l/m/n lineage has resolved. ABSORBED: (1) V3-EXQ-603l (4-arm escape-affordance bridge behavioural retest) landed FAIL/weakens (bridge_insufficient_env_survivable), and confirmed failure_autopsy_V3-EXQ-603l_2026-06-10 reclassifies it non_contributory (NOT weakens) -- a test-design / measurement ceiling, not a bridge failure: the 603k harm-pathway-training readiness fix OVER-corrected, raising ARM_BASE_IA_ONLY to the binary survival ceiling G_H=1.0 (3/3), making the primary best_bridge>base structurally unsatisfiable; the bridge fired non-vacuously and the both-arm showed ~35% longer mean hazard-stage survival, invisible to the binary gate. THIS RECONCILE APPLIES that reclassification to the 603l manifest (weakens->non_contributory + EQN note) + adds the dated note to SD-059/MECH-358, and rebuilds the index. (2) V3-EXQ-603m (full scaffolded G1/G2/G3 gate) FAILed at G0 only; corrected-G0 re-run V3-EXQ-603n landed PASS/non_contributory/diagnostic (label goal_formed_diversity_undetermined; G0-G3 all non-degenerate; harm pathway discriminative; reached-P2-alive 2/3) -- the scaffolded-curriculum gate is now CLEAR. So BOTH gates the 06-13 note named (603l autopsy + 603n scaffolded-gate clearing) are now satisfied. OWED next (NOT yet queued): the bridge REDESIGN EXQ (603o per the 603l autopsy: headroom-restoring hazard regime where base sits at G_H~0.33-0.67 + a CONTINUOUS survival metric) settles SD-059/MECH-358, THEN the Q-045/MECH-313/MECH-260 4-arm tonic-noise ablation. Node STAYS in-progress (non-governance-weighting); MECH-313/MECH-260/Q-045 retest still owed. last_updated 2026-06-13 -> 2026-06-14."
      governance_2026_06_13: "Closure-drift stale-since-review ACKNOWLEDGE (governance cycle 2026-06-13T20:12Z). Flagged only because failure_autopsy_V3-EXQ-655_2026-06-13 reclassified MECH-313 (in this node's unblocks set) to non_contributory/substrate_ceiling. Does NOT change GAP-C: 655 is a distinct INV-074-cluster task-shift necessity test; GAP-C's Q-045/MECH-313/MECH-260 retest stays gated on the 603l autopsy + 603n scaffolded-gate clearing. The reclassification is consistent with the node already being substrate-blocked. last_updated bumped to acknowledge; node STAYS in-progress. No owner_exq / status / claims.yaml changes."
      governance_2026_06_10_pm: "Closure-drift acknowledge (session governance-20260610T1600Z). Both gates GAP-C waits on have now LANDED but neither is CLEARED, so the node stays in-progress: (1) the 4-arm bridge re-test V3-EXQ-603l landed FAIL/weakens (SD-059/MECH-358) but the weakens rests on a survivability ceiling (BASE G_H already 1.0; bridge credits + clears G_H 2/3 non-vacuously, preconditions all MET) -- user FLAGGED for /failure-autopsy this cycle (possible discrimination-ceiling artifact vs genuine weakens), so the bridge verdict is NOT yet settled and the ready-flip is NOT taken; (2) the full scaffolded G1/G2/G3 gate V3-EXQ-603m landed FAIL at G0 only (Stage-0 nursery z_goal>0.4 held 1/3; G1 survival 3/3, G2 contact 3/3, G3 ecological z_goal 2/3 all PASS; non-vacuity MET) -- confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10 ruled G0 a measurement/developmental-sequencing artifact and routed the corrected-G0 re-run V3-EXQ-603n (queued this cycle). NOTE the closure-drift lineage-advanced flag pins 603m as a 'later sibling' of owner_exq 603k: 603m/603n is the scaffolded-curriculum readiness lineage (owned at goal_pipeline:GAP-2), distinct from 603k's Stage-H harm-pathway leg; owner_exq stays 603k. Q-045/MECH-313/MECH-260 retest stays gated on the 603l autopsy verdict + the 603n corrected-G0 scaffolded gate clearing. No claims.yaml / manifest edits."
      governance_2026_06_10: "Substrate-reconcile WP-A (session substrate-reconcile-603jk-WP-A-20260610T0631Z): both 603j/603k PASS manifests re-verified directly and the substrate_queue entries reconciled to match -- escape-affordance-bridge status pending_implementation -> IMPLEMENTED/safety-half-validated (ready stays false; behavioural validation V3-EXQ-603l in flight owns the ready flip), scaffolded_sd054_onboarding status updated to harm-pathway-survival-leg VALIDATED (ready stays false; residual = foraging/benefit-contact P2 leg + Stage-0 z_goal>0.4 holds on only 1/3 seeds). GAP-C unchanged: stays in-progress + non-governance-weighting, Q-045/MECH-313/MECH-260 retest still gated on the full 4-arm 603l bridge re-test landing AND on the full scaffolded G1/G2/G3 gate. No claims.yaml / manifest edits."
      governance_2026_06_09_pm: "V3-EXQ-603k LANDED PASS 2026-06-09T18:14Z (Stage-H harm-pathway readiness; claim_ids=[], non_contributory; reviewed). The PRIMARY nav/survival-competence ceiling is now resolved at the harm-pathway level: harm pathway trained 6242 steps, ARM_HARM_OFF_NAV nav-control still dies (G_H 0.0), harm_eval(z_world) range lifted to 0.133 (vs 603i flat ~0.002), load-bearing G_H clears 2/3, criteria_non_degenerate all true. With 603j (safety-half) this makes BOTH escape-affordance-bridge readiness prereqs green; the full 4-arm SD-059/MECH-358 bridge behavioural re-test is queued via chip. GAP-C stays in-progress + non-governance-weighting: the Q-045/MECH-313/MECH-260 behavioural retest stays gated on that full bridge re-test landing (and on the full scaffolded G1/G2/G3 gate, which 603k's narrow harm-pathway probe does not by itself satisfy). last_updated current."
      governance_2026_06_09: "Closure-drift stale-since-review reconcile. owner_exq repointed off the in-flight V3-EXQ-603i to absorb its terminal outcome + the later sibling 603j. 603i FAILed non_contributory/substrate_ceiling (escape-affordance bridge validation, claim_ids=[]; autopsy applied prior cycle) -- two co-equal substrate gaps, neither a bridge verdict. The SECONDARY gap (safety-half starvation) is now closed at the readiness layer: V3-EXQ-603j (escape_bridge_safety_half_readiness) PASSed 2026-06-09 (trained MECH-303/304 safety_signal 0.89 >= 0.5 floor + under-threat gate 0.58 >= 0.1; claim_ids=[], non_contributory, reviewed this cycle) -- the SD-059 safety half can now credit non-vacuously. The PRIMARY nav/survival-competence ceiling is being addressed by V3-EXQ-603k (Stage-H harm-pathway training). GAP-C stays in-progress and non-governance-weighting; the Q-045/MECH-313/MECH-260 behavioural retest stays gated on the full 4-arm escape-affordance bridge re-test, which is gated on the 603k nav-competence leg landing. last_updated bumped."
      governance_2026_06_08: "Plan-drift reconcile. The old prereq (2)/(3) resume list is obsolete. The scaffolded_sd054_onboarding survival/hazard leg has progressed through the Stage-H and escape-affordance-bridge amendments; the current active validation is V3-EXQ-603i, claimed on ree-cloud-1 at 2026-06-08T13:57:39Z, diagnostic claim_ids=[]. Status moves blocked_pending_substrate -> in-progress. GAP-C remains non-governance-weighting until 603i returns; only a PASS/non-vacuous readiness result unblocks the Q-045/MECH-313/MECH-260 behavioural retest."
      substrate_landed_2026_05_31: "Prereq (3) substrate change landed via /implement-substrate-infant-curriculum-h-pos-recal-20260531T123353Z (cross-link IGW-20260531-009). InfantCurriculumScheduler.H_POS_FRAC_OF_MAX recalibrated 0.70 -> 0.20 in ree-v3/experiments/infant_curriculum.py (Path (a) per failure_autopsy_V3-EXQ-591_2026-05-27 section 7). 0.20 * ln(144) ~= 0.99 sits inside the observed rolling-mean H_pos band 0.03-1.08 with ~9% margin above observed max. Path (b) alternative-gate (z_goal-norm / residue-coverage) NOT taken: z_goal collapses to ~1e-7 across 591 arms (blocked on prereq (2) goal_pipeline:GAP-4) and residue_coverage saturates trivially per autopsy. 3 contract tests added (test_infant_curriculum_gap9.py C11 trio: default-within-band, synthetic-P0-trajectory-advances, marginal-clearance). infant_substrate_expansion.md Section 6.1 (Phase 0 exit condition) updated. Status remains blocked_pending_substrate because prereq (2) z_goal-collapse blocker on goal_pipeline:GAP-4 / V3-EXQ-490g cohort is still load-bearing. When (2) clears, V3-EXQ-603d / 591b can queue immediately -- (3) is no longer the gate."
      resume_condition: "BLOCKED-ON-V3-EXQ-603p 2026-06-15 -- see governance_2026_06_15 for the AUTHORITATIVE current route (603o RAN 2026-06-11; 603p diagnostic claimed+running on ree-cloud-2, not yet landed; on 603p landing -> extract the located proximity_harm/harm_lr -> /queue-experiment V3-EXQ-603q evidence re-run, OR Branch-B off-ramp if the 0.10 positive control fails). The text below is RETAINED for history; its '(1) /queue-experiment the bridge REDESIGN 603o (NOT yet queued)' instruction is SUPERSEDED (603o is consumed). READINESS GATES CLEARED 2026-06-14. The 603i/j/k/l/m/n lineage has resolved: 603j (safety-half) + 603k (Stage-H harm pathway) PASS readiness; 603n PASS clears the scaffolded G1/G2/G3 curriculum gate; 603l (bridge behavioural retest) reclassified non_contributory (test-design/measurement ceiling per failure_autopsy_V3-EXQ-603l_2026-06-10 -- 603k over-corrected base to the binary survival ceiling, removing the bridge's headroom). HISTORY (SUPERSEDED by governance_2026_06_15 -- 603o RAN 2026-06-11, 603p diagnostic in-flight): (1) the bridge REDESIGN 603o carried BOTH autopsy fixes -- a harder/intermediate hazard regime so ARM_BASE_IA_ONLY sits at G_H~0.33-0.67 with measurable headroom, AND a CONTINUOUS survival metric (mean/median hazard-stage episode length, time-to-first-death) replacing the saturating binary median>=75 gate; PASS = best-bridge continuous-survival strictly > base on >=2/3 seeds, readiness met -> settles SD-059/MECH-358. (2) THEN /queue-experiment the Q-045 4-arm tonic-noise ablation (MECH-313 OFF / 313-only / 260-only / both-ON), the actual GAP-C falsifier; degeneracy pre-check warranted (a non-propagating noise channel would reproduce the GAP-A r1a_entropy_only_artefact outcome). 603i/j/k/l/m/n are diagnostic (claim_ids=[]) or reclassified non_contributory and do not move claim confidence by themselves."
    - id: "behavioral_diversity_isolation:GAP-D"
      title: "Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)"
      phase: "P1"
      status: done
      severity: medium
      owner_exq: "V3-EXQ-550 FAIL/supports MECH-269 (2026-05-11T20:18Z, diagnostic-probe; scoring_excluded); V3-EXQ-601 PASS/supports MECH-269b (2026-05-21T12:02Z, diagnostic-probe; scoring_excluded); R4.b stamped 2026-05-29; Q-040b behavioural sufficiency continues under goal_pipeline:GAP-4"
      unblocks_claims: [MECH-269, MECH-269b, Q-040]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-29
      governance_2026_05_29: "R4.b stamped this session per user authorisation (options i+ii+iii: plan-doc close + MECH-269/269b evidence_quality_note + drift-script extension). The supporting runs (V3-EXQ-550 + V3-EXQ-601) sit in claim_evidence.v1.json with evidence_direction=supports but flagged scoring_excluded=diagnostic_probe (both manifests carry experiment_purpose=diagnostic), so the standard /governance pipeline cannot auto-promote MECH-269 / MECH-269b off the hold_pending_v3_substrate recommendation -- the stamp is a governance-level recognition of the R4.b reading on the diagnostic evidence, not an experimental_confidence move. MECH-269 / MECH-269b remain v3_pending=true. The non-diagnostic behavioural sufficiency test (Q-040b) is owned by goal_pipeline:GAP-4 / V3-EXQ-490g Tier-1 retest cohort and is the path to lifting v3_pending. Drift-script extended to flag pending_governance_stamp on future plan-nodes so this manual-stamp loop closes automatically next time."
      resume_condition: "CLOSED 2026-05-29. R4.b stamped on V3-EXQ-550 + V3-EXQ-601 diagnostic evidence per behavioral_diversity_isolation_plan.md decision-rules (Theory 4 promoted; V_s pathology confirmed). Theory 4 contribution to the isolation matrix is now established at the diagnostic-probe level. Follow-up sufficiency work continues under goal_pipeline:GAP-4 (V3-EXQ-490g cohort); do NOT re-open GAP-D for that work -- it has its own closure node. Reopen GAP-D only if (a) the supports-MECH-269 per-claim direction on the V3-EXQ-550 manifest is later revised, or (b) a non-diagnostic falsifier at Layer D produces a contributory result that directly contradicts R4.b."
    - id: "behavioral_diversity_isolation:GAP-E"
      title: "Theory 5 (deferred): proposal-distribution bias (re-enters candidate set on R_X.c)"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["behavioral_diversity_isolation:GAP-A", "behavioral_diversity_isolation:GAP-B", "behavioral_diversity_isolation:GAP-C", "behavioral_diversity_isolation:GAP-D"]
      last_updated: 2026-05-25
      resume_condition: "Re-enters candidate set only if R_X.c fires -- i.e. the full 4-substrate stack (Layers A+B+C+D ON) still fails Rung 1 at ALL_ON. Until then, retained as secondary candidate but no falsifier is owed."
    - id: "behavioral_diversity_isolation:GAP-F"
      title: "Theory 6 (deferred): MECH-260 anti-recency contribution to behavioural diversity"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-260]
      depends_on: ["behavioral_diversity_isolation:GAP-C"]
      last_updated: 2026-05-25
      resume_condition: "Partially covered by Q-045 4-arm ablation (MECH-313 OFF / 313 only / 260 only / both ON) under GAP-C's V3-EXQ-603c retest. Promote to non-deferred only if the 4-arm result needs a dedicated MECH-260-vs-MECH-313 redundancy follow-up per R_X.b."
    - id: "behavioral_diversity_isolation:GAP-G"
      title: "Theory 7 (deferred): MECH-314 curiosity weight (Goldilocks calibration)"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-314, MECH-314a]
      depends_on: ["behavioral_diversity_isolation:GAP-B"]
      last_updated: 2026-05-25
      resume_condition: "V3-EXQ-590a annotated pending_retest_after_substrate (MECH-111 broadcast novelty was scalar EMA -> argmax-invariant null on selection). Re-queue as V3-EXQ-590b is gated on MECH-314a per-candidate RBF novelty implementation AND behavioural diversity landing (i.e. resolution of GAP-B). Until both gates clear, theory 7 stays deferred and its falsifier is not queued."
    - id: "behavioral_diversity_isolation:GAP-H"
      title: "Theory 8 (deferred): z_goal config-default confound"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["behavioral_diversity_isolation:GAP-D"]
      last_updated: 2026-05-25
      resume_condition: "Confound check on V3-EXQ-550 (Theory 4). If GAP-D's R4-rule application surfaces an ARM_ON >> ARM_OFF asymmetry that maps to z_goal config-default rather than V_s substrate pathology (R4.a), this node becomes the dedicated re-run with z_goal matched across arms. Until GAP-D's R4 disposition lands in governance, theory 8 stays deferred."
---

# Behavioural Diversity Isolation Plan (REE-v3)

**Created:** 2026-05-25T11:46:33Z
**Author session:** diversity-isolation-plan-20260525T114633Z
**Status:** draft (plan-of-record)
**Sibling to:** [`behavioral_diversity_acceptance_criteria.md`](behavioral_diversity_acceptance_criteria.md)
**Related claims:** ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a/b/c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076

---

## Purpose

The acceptance-criteria doc (sibling) defines **what counts as success** for behavioural
diversity in REE-v3. This document defines **how we isolate which of the candidate failure
mechanisms is load-bearing** when diversity fails. The two are complementary:

| Doc | Question answered |
|-----|-------------------|
| `behavioral_diversity_acceptance_criteria.md` | When can we say diversity is real and useful? |
| `behavioral_diversity_isolation_plan.md` (this) | When diversity is absent, which substrate layer is responsible? |

The isolation plan is needed because **diversity failure is multi-causal**: ARC-065 already
commits the architecture to a distributed pathway (LC-NE tonic + frontopolar curiosity +
striatal novelty + hippocampal trajectory sampling), and multiple layers can independently
suppress the observed action-class entropy. Without an isolation matrix, a Rung-1 FAIL is
under-determined: we don't know which substrate to fix next.

---

## Layer model: where diversity can collapse

Diversity must survive all four layers between candidate generation and observable action.
Failure at any one layer reproduces the monostrategy phenotype downstream.

```
                  ARC-065 distributed diversity-generation pathway
                                    |
                                    v
   [ Layer A: PROPOSAL ]  hippocampal trajectory sampling, CEM candidate pool
                                    |
                                    v
   [ Layer B: SCORING ]    E3 score aggregation across trajectory classes
                                    |
                                    v
   [ Layer C: ACTION-SELECT ]  softmax / argmax over E3-ranked candidates
                                    |
                                    v
   [ Layer D: REPRESENTATION ] V_s anchor sets / regional verisimilitude
                                    | (feeds back into Layer A on next tick)
                                    v
                              observable action stream
```

**Layer D feedback note.** Layer D is not strictly downstream of A-C in a single tick --
state representation in tick t+1 depends on what was committed in tick t. Stale V_s
representations therefore amplify monostrategy across episodes even when Layers A-C are
behaving correctly within any one tick. This is why MECH-269 reads as "monostrategy"
upstream of the action-selection stack despite acting on representations.

---

## The 4 theories (top of the candidate field)

Drawn from the 8-mechanism survey 2026-05-25 (see prior conversation / governance log).
Theories 5-8 (proposal-distribution bias, MECH-260 anti-recency, curiosity weight, z_goal
config-default confound) are retained as secondary candidates but not the focus of this
plan.

| # | Theory | Layer | Primary claim | Falsifier EXQ | Status |
|---|--------|-------|---------------|---------------|--------|
| 1 | CEM elite-pool collapse to one action class | A | ARC-065 (SP-CEM child) | V3-EXQ-567 / V3-EXQ-569 | landed 2026-05-17 (main-path); matched-entropy control pending |
| 2 | **E3 scoring collapses diverse candidates to one** | **B** | **MECH-341 (new)** | **TBD (this plan, design below)** | **unclaimed gap until 2026-05-25** |
| 3 | Missing tonic noise floor (LC-NE analog) | C | MECH-313 | V3-EXQ-543b ARM_MECH313_only | substrate landed, matched-entropy gate pending |
| 4 | V_s regional verisimilitude staleness | D | MECH-269 / 269b | V3-EXQ-550 (live falsifier) | falsifier in flight |

**Headline gap.** Theory #2 (E3 scoring) is the highest residual leverage because the other
three either have landed substrate (#1, #3) or have an active falsifier (#4). MECH-341
registered in this pass closes the claim-side of the gap; the experiment design (Section 5)
closes the test-side.

---

## Isolation matrix

Each row is an experiment arm; each column is a substrate ON/OFF. A run produces the row
of outcomes; comparison across rows pins the contribution of each substrate. The matrix is
designed so that *any single substrate ablation against the all-ON baseline gives a
single-substrate contribution estimate*; the all-OFF arm is the Rung-0 substrate-naive
baseline that anchors ARC-065's architectural commitment.

| Arm | SP-CEM (A) | E3 score-diversity (B) | Noise floor MECH-313 (C) | V_s active MECH-269 (D) | Use |
|-----|:----------:|:---------------------:|:------------------------:|:----------------------:|-----|
| BASE_OFF | off | off | off | off | Rung 0 baseline / ARC-065 architectural-necessity check |
| ALL_ON | **on** | **on** | **on** | **on** | Rung 1 target (matched-entropy controlled) |
| A_only | on | off | off | off | Theory 1 contribution (SP-CEM proposal lift in isolation) |
| B_only | off | **on** | off | off | Theory 2 contribution (E3 scoring lift in isolation) |
| C_only | off | off | **on** | off | Theory 3 contribution (noise floor in isolation) |
| D_only | off | off | off | **on** | Theory 4 contribution (V_s in isolation) |
| ablate_A | off | on | on | on | Marginal cost of removing SP-CEM |
| ablate_B | on | off | on | on | Marginal cost of removing E3 diversity preservation |
| ablate_C | on | on | off | on | Marginal cost of removing noise floor |
| ablate_D | on | on | on | off | Marginal cost of removing V_s |
| MATCHED_NOISE | off | off | T=2.5 uniform | off | FP-2 control: structured-vs-noise comparison for acceptance doc Rung 1 |

**Pragmatic note.** The full 11-arm matrix is not required in a single run. Sequencing
(Section 6) reduces this to a phased programme of 3-arm and 4-arm experiments that each
answer one question.

**Layer-B substrate gap.** "E3 score-diversity ON" requires MECH-341 substrate to exist;
until it lands, B columns are vacuously OFF and theories 1/3/4 are the only testable axes.
MECH-341 substrate work is a prerequisite for the full matrix.

---

## Decision rules

Each rule has the form `if (observation) -> (decision)`. Rules are applied in order; the
first matching rule wins.

### Theory 1 (CEM elite-pool collapse)

- **R1.a** If V3-EXQ-569 matched-entropy control shows SP-CEM entropy = noise-matched entropy on
  all diversity metrics (entropy, coverage, trajectory_class_count): theory 1 is **not
  load-bearing on its own**. ARC-065 SP-CEM child substrate marked `non_contributory` for
  diversity (separate from its non-collapse role). Promote attention to theories 2-4.
- **R1.b** If V3-EXQ-569 shows SP-CEM strictly > matched noise on trajectory_class_count
  (FP-2 cleared): theory 1 confirmed as a real contributor; advance to Rung 2 testing.

### Theory 2 (E3 scoring collapse) -- this plan's primary new test

- **R2.a** If pre-MECH-341 trajectory_class_count >= 2 in CEM candidates but post-E3-scoring
  selected class count = 1 for >= 80% of timesteps (measured on SP-CEM-ON, MECH-269-ON
  baseline): theory 2 is confirmed as a real diversity-collapse site. MECH-341 substrate
  becomes priority.
- **R2.b** If post-E3 selected class count tracks pre-E3 candidate class count within +/- 1
  on average: theory 2 is **not load-bearing**. E3 is preserving the diversity it receives;
  the collapse must be at A or C or D. MECH-341 retains as architectural commitment but no
  substrate work is triggered.
- **R2.c** If theory 2 confirmed AND MECH-341 substrate lands AND `B_only` arm produces
  trajectory_class_count >= 2 with first_action_entropy > 0.3: MECH-341 provisional
  promotion candidate.

### Theory 3 (noise floor)

- **R3.a** If MECH-313 ON alone (`C_only` arm) produces matched-entropy-distinguishable lift
  on trajectory_class_count but not on coverage: theory 3 contributes to per-tick entropy
  but not to strategic diversity. Retain MECH-313 as Layer-C substrate but escalate
  attention to theories 2/4.
- **R3.b** If ablate_C arm (drop MECH-313 from ALL_ON) drops trajectory_class_count below 2
  while Rung 1 metrics for ALL_ON pass: MECH-313 is necessary-and-sufficient at Layer C;
  promote on Rung 2 PASS.
- **R3.c** If ablate_C arm leaves Rung 1 metrics unchanged from ALL_ON: MECH-313 is
  redundant under combined substrate -- candidate for de-prioritisation pending broader
  ablation matrix.

### Theory 4 (V_s representation staleness)

- **R4.a** If V3-EXQ-550 ARM_ON >> ARM_OFF on relevant diversity metrics: confounded by
  z_goal config default; V_s pathology not confirmed; theory 4 demoted. Re-run with z_goal
  matched across arms before re-evaluating.
- **R4.b** If V3-EXQ-550 ARM_ON ≈ ARM_OFF: V_s substrate pathology confirmed; theory 4
  promoted; MECH-269 follow-up substrate work prioritised.
- **R4.c** If V3-EXQ-550 ARM_ON crashes: separate substrate bug surfaces; classify as
  failure_autopsy candidate; theory 4 status unchanged until autopsy resolves.

### Cross-theory escalation rules

- **R_X.a** If ALL_ON arm produces Rung 1 PASS but `A_only`, `B_only`, `C_only`, `D_only`
  all individually FAIL Rung 1: diversity is **emergent across substrates** (INV-074
  plasticity-crystallization invariant fires); no single Layer is load-bearing. Promote
  ARC-065 on multi-arm evidence.
- **R_X.b** If two single-substrate arms (e.g., `A_only` and `C_only`) each PASS Rung 1
  independently: substrates are **partially redundant**; revisit Q-045 (MECH-313 vs
  MECH-260 independence) and propose new Q-claim on A-vs-C redundancy.
- **R_X.c** If ALL_ON FAILS Rung 1: the four-substrate stack as currently specified is
  insufficient; **expand candidate set** to theories 5-8 (proposal-distribution bias,
  MECH-260 anti-recency, MECH-314 curiosity weight, z_goal config-default) before further
  Layer-A/B/C/D refinement.

---

## Experiment sequencing

Layer-B (MECH-341) substrate does not yet exist, so the full isolation matrix cannot run
in one pass. Phased approach:

### Phase P1 -- Pre-existing-substrate isolation (executable now)

**Arms:** BASE_OFF, A_only, C_only, D_only, ALL_ON (excluding Layer-B). MATCHED_NOISE
arm for FP-2 control. **6 arms.**

**Target:** Pin which of theories 1, 3, 4 is load-bearing under the current main-path
substrate. Apply R1, R3, R4 decision rules.

**Falsifiers reused:** V3-EXQ-567 (A_only effect already measured), V3-EXQ-569 (matched
noise, queued), V3-EXQ-550 (D_only effect, in flight).

**Required new EXQ:** A 6-arm P1 isolation run combining all three substrates on a single
SD-054 episode set, so the cross-substrate comparison is on matched data. Recommend
queueing as **V3-EXQ-TBD (P1 layer isolation, 6 arms)** -- queue via `/queue-experiment`
skill, not directly.

### Phase P2 -- E3 scoring diagnostic (executable now; no substrate needed)

**Arms:** ALL_ON_now (A+C+D, no MECH-341), instrumented to log:
- per-tick: pre-E3 CEM candidate trajectory_class_count
- per-tick: post-E3 selected trajectory_class_count
- per-tick: E3 score distribution across distinct classes (mean, std, top-2 gap)

**Target:** Apply R2.a / R2.b. **No substrate change**, just instrumentation. If R2.a
fires: MECH-341 substrate work is justified and prioritised. If R2.b fires: MECH-341 stays
architectural-only.

**Required new EXQ:** **V3-EXQ-TBD (P2 E3 score-collapse diagnostic, instrumentation only)**.
Same SD-054 episode set as P1; can be a single-arm probe.

### Phase P3 -- MECH-341 substrate build + B-axis test

**Trigger:** P2 confirms R2.a.

**Substrate work:** Implement MECH-341 (one of: entropy bonus over candidate classes at
E3 aggregation; class-stratified argmax with proportional sampling within class; jittered
tie-breaking when top-K E3 scores are within epsilon). Specific design open -- see
"Substrate design options" below.

**Arms (post-build):** B_only, ablate_B, ALL_ON (now including B). **3 arms.**

**Target:** Apply R2.c. Promote MECH-341 if `B_only` produces Rung 1-comparable diversity
in isolation OR if ablate_B drops Rung 1 metrics significantly.

### Phase P4 -- Full matrix (post-MECH-341 landing)

Run the 11-arm matrix on a downstream env (CausalGridWorld or a new substrate) for
replication and to apply R_X rules.

**Design doc staged 2026-05-31:** [`v3_exq_p4_11arm_isolation_design_2026-05-31.md`](v3_exq_p4_11arm_isolation_design_2026-05-31.md)
fully specifies the 11 arms, R_X.a/b/c acceptance grid, data plan, V3 substrate
tagging requirements, and Python skeleton (forked from
`ree-v3/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py`).
Reserved queue ID: **V3-EXQ-618** (priority 90, one rung below V3-EXQ-616).

**Gating EXQ:** P4 fires AFTER **V3-EXQ-614b** PASSes (the MECH-341 amend-and-re-run
cycle on the SD-056-amended substrate, queued 2026-05-31T12:32Z @ priority 250).
Informed by V3-EXQ-616 (Q-054 entropy_bias_scale sweep -- sets
`MECH341_ENTROPY_BIAS_SCALE`) and V3-EXQ-569a (GAP-A R1.b matched-entropy FP-2 --
sets A_only expectation). Plan-doc's original blocker text ("Blocked on Rung 2
SD-054 clearance + MECH-341 landed") is now satisfied at the diagnostic-probe level
(GAP-B partial-PASS via R2.c on V3-EXQ-614a establishes the Rung-2 reading;
MECH-341 substrate landed 2026-05-27 + amend landed 2026-05-31). The remaining
gate is the behavioural confirmation that 614b PASSes on the amended substrate.

Submission protocol in design-doc Section 11. Design doc stays `status: STAGED`
until 614b PASSes; submission session updates to `status: SUBMITTED` with
queue-time decisions recorded.

---

## Substrate design options for MECH-341 (when P3 triggers)

The claim asserts that E3 must preserve trajectory-class diversity across its scoring step.
There are at least three plausible implementations:

1. **Entropy bonus over candidate classes.** E3 score = harm_score + lambda * H(class | candidates).
   Penalises homogenisation of the candidate pool at scoring time. Risk: lambda is another
   tuning knob; matched-noise control needed.
2. **Class-stratified argmax with within-class proportional sampling.** Stratify candidates
   by first-action class; pick best within each class; sample across classes proportional
   to their best-in-class scores. Preserves all surviving classes; biases toward best
   representative of each. **Amend 2026-06-01:** within-class step gains an
   optional temperature `stratified_within_class_temperature` (`None` = legacy
   argmin bit-identical; positive `T` = sample within each class via
   `softmax(-class_scores / T)`). Decoupled from the existing across-class
   `stratified_temperature` so the A-vs-B partial-redundancy probe can
   dissociate within-class and across-class layers in V3-EXQ-614c.
3. **Jittered tie-breaking near top.** Standard argmax, but when top-K scores are within
   epsilon, sample uniformly across them. Cheapest implementation; only affects diversity
   when E3 scores are nearly tied (which is precisely when diversity is being lost).

These three options are not mutually exclusive (could combine 1+3). Pre-implementation
governance: which to try first should be decided after P2 results, since P2's per-tick E3
score distribution data will tell us whether the collapse is happening at near-ties
(option 3 sufficient) or at large score gaps (option 1 or 2 required).

---

## Status table (resume primitive)

| Theory | Layer | Claim | Substrate status | Falsifier | Result | Decision |
|--------|-------|-------|------------------|-----------|--------|----------|
| 1 CEM collapse | A | ARC-065 (SP-CEM child) | landed 2026-05-17 main-path; **E2-world-forward per-candidate signal collapse identified 2026-05-25 (root cause doc)** | V3-EXQ-567 / V3-EXQ-569 / V3-EXQ-571 / V3-EXQ-573 / V3-EXQ-609 | 567 PASS (entropy 0.012->0.497); 569 + 573 non_contributory (bias channel structurally zero); 570/571/609 diagnostics landed | **R1 falsifier blocked**: per-candidate bias signal structurally zero (all K cands -> identical z_world after one E2 step). Awaiting E2-world-forward substrate fix; V3-EXQ-569a queued after substrate lands |
| 2 E3 scoring | B | **MECH-341** (registered 2026-05-25) | **IMPLEMENTED 2026-05-27 (options 1+2 togglable); RETUNE 2026-05-28 (stratified_select on both branches + lambda/scale defaults); AMEND 2026-06-01 (stratified_within_class_temperature lever + A-vs-B probe naming)** | V3-EXQ-608 P2 (PASS R2a 2026-05-26); V3-EXQ-611c PASS 2026-05-29; V3-EXQ-614a PASS_C2_C3_only 2026-05-30; V3-EXQ-614b FAIL_no_criterion 2026-05-31 (per-claim non_contributory MECH-341 + ARC-065 via /governance); V3-EXQ-616 FAIL_no_floor_under_max_swept_scale 2026-05-31 (per-claim non_contributory Q-054 + MECH-341 via /governance); V3-EXQ-614c queued 2026-06-01 | 608 R2a fired; substrate + retune validated; 614b structural ARM_0 degeneracy without SP-CEM Layer A; 616 mathematically rules out scale-axis isolation of MECH-341 under SP-CEM-OFF; amend landed adding within-class proportional sampling lever | await V3-EXQ-614c manifest -- C1 regression-guard + C2 within-class lift or C3 substrate-readiness; PASS clears MECH-341 v3_pending |
| 3 noise floor | C | MECH-313 | landed | V3-EXQ-543b ARM_MECH313 (pending Q-045 retest) | autopsy 603b: substrate operative but design-blocked | retest via 603c (training-phase fix) |
| 4 V_s stale | D | MECH-269 / 269b | substrate-ready (IGW-021); MECH-269b staleness wiring landed | V3-EXQ-550 (z_goal probe); V3-EXQ-601 (MECH-269b staleness gate) | 550 FAIL/supports MECH-269 2026-05-11T20:18Z; 601 PASS/supports MECH-269b 2026-05-21T12:02Z; both reviewed; both diagnostic-probe (scoring_excluded) | **R4.b STAMPED 2026-05-29** (V_s pathology supported on diagnostic evidence; theory 4 promoted). Closure node done. MECH-269 / MECH-269b stay v3_pending=true; Q-040b behavioural sufficiency continues under goal_pipeline:GAP-4 (V3-EXQ-490g cohort) |

**Update cadence:** every time a P-phase experiment lands, update this table in-place with
the result and the decision-rule outcome. This is the resume primitive across sessions.

### 2026-05-29 GAP-D R4.b stamp (CLOSED)

R4.b stamped this session per user authorisation (options i+ii+iii: plan-doc close +
MECH-269 / MECH-269b evidence_quality_note in claims.yaml + drift-script extension).

**Why the manual stamp.** The supporting runs (V3-EXQ-550 + V3-EXQ-601) sit in
`claim_evidence.v1.json` with `evidence_direction=supports` but flagged
`scoring_excluded=diagnostic_probe` (both manifests carry `experiment_purpose=diagnostic`).
The indexer correctly excludes diagnostic-probe runs from `experimental_confidence`, so
MECH-269 / MECH-269b show `exp_conf=0.0` and the standard `/governance` pipeline can only
recommend `hold_pending_v3_substrate` (applied). Auto-promotion via the experimental
gate is therefore architecturally unavailable for diagnostic-probe evidence.

R4.b is a **governance-level recognition** of the V_s-pathology reading on the diagnostic
evidence -- a different kind of stamp than a confidence-driven promotion. It promotes the
theory within the isolation-plan reasoning (Theory 4 contribution to the isolation matrix
is established) without claiming the v3_pending substrate gate has cleared.

**What did NOT change.** MECH-269 / MECH-269b remain `v3_pending: true` in claims.yaml.
The non-diagnostic behavioural sufficiency test (Q-040b) is owned by
`goal_pipeline:GAP-4` / V3-EXQ-490g Tier-1 retest cohort, and is the path to lifting
v3_pending. Promotion off `hold_pending_v3_substrate` waits on a non-diagnostic experimental
result.

**What did change.**
- This node: `status: pending_governance_stamp` -> `done`; `last_updated: 2026-05-29`.
- claims.yaml: `evidence_quality_note` added to MECH-269 + appended to MECH-269b citing
  the R4.b stamp on the diagnostic-probe supports-direction.
- scripts/check_closure_drift.py: `NON_TERMINAL_STATUSES` extended to include
  `pending_governance_stamp`, so future plan-nodes parked at this status get flagged
  automatically on the next /governance cycle (closes the manual-stamp loop).

**Prior disposition (2026-05-28, by igw-011-gapd-doc-sync).** R4.b reading was applied to
the status table by that session under `pending_governance_stamp`. The 2026-05-29 stamp
above completes that disposition; the prior R4.a/R4.b/R4.c decision-rule walk is preserved
in the manifest interpretation grid and in the V3-EXQ-550 manifest `evidence_direction_note`.

---

---

## New claims registered with this plan (2026-05-25)

| Claim | Title (abbreviated) | Type | Status |
|-------|---------------------|------|--------|
| MECH-341 | e3_scoring_preserves_trajectory_class_diversity | mechanistic_implementation | candidate, v3_pending |
| Q-054 | minimum trajectory-class diversity floor for ARC-062 (was proposed as Q-046) | open_question | open |
| Q-055 | sleep consolidation: diversity-preserving vs eroding (was proposed as Q-047) | open_question | open |
| INV-076 | behavioural diversity as structural prerequisite for ethical counterfactual evaluation (was proposed as INV-074 -- ID taken 2026-05-17 by plasticity-crystallization invariant) | invariant (universal) | candidate |

Q-054, Q-055, INV-076 supersede the 2026-05-15 "proposed new claims" in the
acceptance-criteria doc (Q-046, Q-047, INV-074); their original IDs were never registered
and INV-074 was subsequently taken by a different, broader claim about plasticity
crystallization. The new IDs preserve the original scientific intent under the next
available IDs in their respective ranges.

---

## What this plan does NOT do

- **Does not redefine acceptance criteria.** The Rung 0-4 framework in the sibling
  acceptance-criteria doc is authoritative. This plan layers an isolation analysis on top of
  it.
- ~~**Does not commit to a MECH-341 implementation.** P2 diagnostic results determine which
  of the three design options (Section "Substrate design options") to build.~~ Superseded
  2026-05-27: V3-EXQ-608 P2 majority `R2a_e3_collapse_confirmed_large_gap` (large-gap,
  ruling out option 3 jittered tie-breaking) routed the substrate-design phase to options
  1 + 2. Both landed as togglable sub-flavours under one master in
  `ree-v3/ree_core/predictors/e3_score_diversity.py`. Design doc:
  `REE_assembly/docs/architecture/mech_341_e3_score_diversity_preservation.md`.
- **Does not address theories 5-8.** Those remain candidate mechanisms and re-enter the
  candidate set only if R_X.c fires (full 4-substrate stack insufficient).
- **Does not queue experiments directly.** All EXQ entries flagged here go through
  `/queue-experiment` for code-review + smoke-test discipline.

---

*This document is the plan-of-record for behavioural diversity ISOLATION (which substrate*
*layer is responsible when diversity fails). For acceptance criteria, see the sibling*
*`behavioral_diversity_acceptance_criteria.md`.*
