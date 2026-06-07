# REE-v3 Closure Status (snapshot)

Generated: 2026-06-07T04:20:59Z

GENERATED FILE -- do not edit by hand. This is a static, server-free snapshot of the closure map that serve.py serves live at `/api/closure` -> `/closure`. It is rebuilt from the `closure_plan` frontmatter of every `evidence/planning/*_plan.md` (auto-discovered, not whitelisted). Regenerate with `python scripts/generate_closure_snapshot.py` (runs automatically in `governance.sh`).

ACCURACY: this snapshot reports each node's self-declared `status`. Whether that status matches the actual terminal state of its experiments is audited separately by `check_closure_drift.py` -> [`closure_drift.md`](closure_drift.md). Read both together.

## Overall

- Weighted progress: **70.6%** across 67 non-deferred nodes in 10 plan(s) with closure frontmatter.
- Remaining (open/in-progress/blocked/partial): **24** nodes.
- Deferred (not required for v3 closure): 15 nodes.
- Done: 43 nodes.
- Status tally: blocked=7  blocked_pending_substrate=9  deferred=15  done=43  in_progress=4  open=1  partial=2  upstream_blocked=1

## Plans

| plan | title | nodes | progress | status counts | last_updated |
|------|-------|-------|----------|---------------|--------------|
| `sd_037_axis_b_sustained_threat_curriculum_plan.md` | SD-037 Axis (b): Sustained-Threat Env Curriculum | 4 | 10% | blocked:3 blocked_pending_substrate:1 | 2026-06-05 |
| `self_attribution_plan.md` | Self-Attribution Comparator Loop | 5 | 32% | blocked:3 deferred:1 done:1 | 2026-06-04 |
| `behavioral_diversity_isolation_plan.md` | Behavioural Diversity Isolation | 8 | 42% | blocked_pending_substrate:2 deferred:4 done:1 partial:1 | 2026-06-03 |
| `arc_062_rule_apprehension_plan.md` | Rule Apprehension | 12 | 58% | blocked:1 blocked_pending_substrate:2 deferred:3 done:4 in_progress:1 partial:1 | 2026-05-30 |
| `goal_pipeline_plan.md` | Goal Pipeline (wanting / liking / drive cascade) | 7 | 58% | blocked_pending_substrate:1 deferred:1 done:3 in_progress:1 open:1 | 2026-06-04 |
| `infant_substrate_plan.md` | Infant Substrate Expansion | 15 | 82% | blocked_pending_substrate:3 done:12 | 2026-05-30 |
| `commitment_closure_plan.md` | Commitment / Closure / Mode-Governance | 11 | 85% | deferred:3 done:6 in_progress:2 | 2026-06-04 |
| `sleep_substrate_plan.md` | Sleep Substrate | 8 | 87% | deferred:1 done:6 upstream_blocked:1 | 2026-05-31 |
| `sd033_governance_plan.md` | SD-033 Governance (OCD test battery sub-plan) | 8 | 100% | done:8 | 2026-05-29 |
| `sd_037_axis_a_consumer_input_recalibration_plan.md` | SD-037 Axis (a): Consumer-Input-Threshold Recalibration | 4 | 100% | deferred:2 done:2 | 2026-06-05 |

## Remaining work to close v3 (24)

Ordered by phase, then severity. This is the answer to "what is left."

| plan | node | title | status | phase | sev | owner_exq | active blocker | last_updated |
|------|------|-------|--------|-------|-----|-----------|----------------|--------------|
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P1b` | Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under | blocked_pending_substrate | 1 | load-bearing | V3-EXQ-625c | RESUME the Phase 1b gate (or its successor) once the behavioural-diversity substrate amend | 2026-06-05 |
| self_attribution_plan.md | `self_attribution:GAP-1` | ARC-033 vs ARC-058 path arbitration (forensic 445h read) | blocked | 1 | high | V3-EXQ-445h | Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that | 2026-06-06 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-B` | MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 devi | blocked_pending_substrate | 2 | load-bearing | V3-EXQ-543l | 2026-05-27 GOVERNANCE UPDATE: V3-EXQ-543l ran 20260526T023059Z FAIL branch-e at escalated  | 2026-06-04 |
| commitment_closure_plan.md | `commitment_closure:GAP-4` | OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction | in_progress | 2 | high | V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 | MECH-090 R-c commit-entry readiness conjunction substrate LANDED in two passes (2026-05-28 | 2026-06-04 |
| goal_pipeline_plan.md | `goal_pipeline:GAP-2` | SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor) | blocked_pending_substrate | 2 | high | V3-EXQ-514l | RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queu | 2026-06-05 |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P2` | Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b ma | blocked | 2 | high |  | depends_on: sd_037_axis_b:P1b | 2026-06-05 |
| self_attribution_plan.md | `self_attribution:GAP-2` | SD-029 / MECH-256 retest under full substrate stack | blocked | 2 | high | TBD | Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-C | 2026-05-16 |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassifi | upstream_blocked | 2 | high | V3-EXQ-265a | Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_aut | 2026-05-31 |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P3` | Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lif | blocked | 3 | high |  | depends_on: sd_037_axis_b:P2 | 2026-06-05 |
| self_attribution_plan.md | `self_attribution:GAP-3` | MECH-257 dual-function 3-arm ablation re-queue | blocked | 3 | medium | TBD | depends_on: self_attribution:GAP-1, self_attribution:GAP-2 | 2026-06-04 |
| goal_pipeline_plan.md | `goal_pipeline:GAP-4` | MECH-295 drive->liking->approach cascade Tier-1 retest cohort | in_progress | 4 | high | V3-EXQ-490k TERMINAL 2026-06-04 (modulatory-suff | Tier-1 cohort TERMINAL (V3-EXQ-490j landed 2026-05-31, see last_updated_note): MECH-295 be | 2026-06-04 |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P4` | Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on th | blocked | 4 | high | V3-EXQ-483f | depends_on: sd_037_axis_b:P3 | 2026-06-05 |
| infant_substrate_plan.md | `infant_substrate:GAP-11` | EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison | blocked_pending_substrate | 4 | medium | V3-EXQ-588b | V3-EXQ-588 FAIL reviewed 2026-05-20 (failure_autopsy_V3-EXQ-588_2026-05-19 confirmed): non | 2026-05-30 |
| infant_substrate_plan.md | `infant_substrate:GAP-13` | EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal nove | blocked_pending_substrate | 4 | medium | V3-EXQ-590 | V3-EXQ-590 ran 20260525T084057Z procedural PASS but evidence_direction=pending_retest_afte | 2026-05-30 |
| infant_substrate_plan.md | `infant_substrate:GAP-14` | EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion sat | blocked_pending_substrate | 4 | medium | V3-EXQ-591 | 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-un | 2026-05-30 |
| goal_pipeline_plan.md | `goal_pipeline:GAP-7` | Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 | open | 7 | load-bearing |  | STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 c | 2026-06-05 |
| commitment_closure_plan.md | `commitment_closure:GAP-8` | SD-033b behavioural validation (devaluation + perceptual discrimination) | in_progress | 7 | medium | V3-EXQ-485c + V3-EXQ-485b (co-equal sibling diag | depends_on: commitment_closure:GAP-3 | 2026-06-04 |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341) | partial | P3 substrate validated -> behavioural falsifier next | load-bearing | V3-EXQ-614d (terminal 2026-06-03: PASS C1/C3, FA | V3-EXQ-608 P2 diagnostic landed 2026-05-26T02:58Z PASS majority R2a_e3_collapse_confirmed_ | 2026-06-06 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-H` | ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-0 | partial | 2-3 | medium | V3-EXQ-544 + V3-EXQ-545 (done); V3-EXQ-604 + V3- | <!-- TODO: revise resume_condition to reflect V3-EXQ-544a state --> V3-EXQ-604/605 manifes | 2026-06-06 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-I` | ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorpt | blocked_pending_substrate | 2-3 | medium | V3-EXQ-606b | BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creat | 2026-06-03 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-K` | MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidenc | in_progress | 2-3 | medium | V3-EXQ-546 (done, diagnostic/non_contributory);  | depends_on: arc_062_rule_apprehension:GAP-B, arc_062_rule_apprehension:GAP-H, arc_062_rule | 2026-06-06 |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-A` | Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM  | blocked_pending_substrate | P1 falsifier blocked -> upstream substrate work | medium | V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_ | <!-- TODO: revise resume_condition to reflect V3-EXQ-544a + V3-EXQ-569c state --> V3-EXQ-5 | 2026-05-30 |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-C` | Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog) | blocked_pending_substrate | P1 | medium | V3-EXQ-544/545 substrate PASS 5/5 (2026-05-10);  | Cluster-absorbed (591 autopsy section 6: fourth member of the substrate-uniform z_goal-zer | 2026-05-31 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-J` | MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / | blocked | 2-3 | low |  | depends_on: arc_062_rule_apprehension:GAP-B | 2026-05-17 |

## Deferred -- not required for v3 closure (15)

| plan | node | title | status | reason / blocker |
|------|------|-------|--------|------------------|
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-E` | Multi-strategy scaling probe (>2 strategies) -- distinguishes ARC-062 weak from  | deferred | depends_on: arc_062_rule_apprehension:GAP-B |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-F` | Clinical / failure-mode tests (trauma-schema / paranoid-rule-field / depressive- | deferred | depends_on: arc_062_rule_apprehension:GAP-E |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-G` | Sleep-vs-waking refinement asymmetry tests -- ARC-063 falsifiable predictions (c | deferred | depends_on: arc_062_rule_apprehension:GAP-E |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-E` | Theory 5 (deferred): proposal-distribution bias (re-enters candidate set on R_X. | deferred | Re-enters candidate set only if R_X.c fires -- i.e. the full 4-substrate stack (Layers A+B |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-F` | Theory 6 (deferred): MECH-260 anti-recency contribution to behavioural diversity | deferred | Partially covered by Q-045 4-arm ablation (MECH-313 OFF / 313 only / 260 only / both ON) u |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-G` | Theory 7 (deferred): MECH-314 curiosity weight (Goldilocks calibration) | deferred | V3-EXQ-590a annotated pending_retest_after_substrate (MECH-111 broadcast novelty was scala |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-H` | Theory 8 (deferred): z_goal config-default confound | deferred | Confound check on V3-EXQ-550 (Theory 4). If GAP-D's R4-rule application surfaces an ARM_ON |
| commitment_closure_plan.md | `commitment_closure:GAP-6` | MECH-260 vs SD-034 No-Go pulse boundary unclear (V4 flag) | deferred | depends_on: commitment_closure:GAP-4 |
| commitment_closure_plan.md | `commitment_closure:GAP-7` | MECH-091 phase-reset deferred (SD-006 phase 2) | deferred | ext: SD-006 phase 2 async heartbeat |
| commitment_closure_plan.md | `commitment_closure:GAP-9` | SD-033c/d/e graph-consolidation incomplete | deferred |  |
| goal_pipeline_plan.md | `goal_pipeline:GAP-5` | SD-049 Phase 3 consumer cascade migration (read-side fidelity) | deferred | depends_on: goal_pipeline:GAP-4 |
| sd_037_axis_a_consumer_input_recalibration_plan.md | `sd_037_axis_a:P3` | Phase 3 -- verification diagnostic: confirm recalibrated thresholds lift consume | deferred | depends_on: sd_037_axis_a:P2 |
| sd_037_axis_a_consumer_input_recalibration_plan.md | `sd_037_axis_a:P4` | Phase 4 -- V3-EXQ-483f behavioural validation (4-arm 2x2 OFF_OFF/ON_OFF/OFF_ON/O | deferred | depends_on: sd_037_axis_a:P3 |
| self_attribution_plan.md | `self_attribution:GAP-5` | SD-030/SD-031 z_self / z_world materialisation (V4) | deferred |  |
| sleep_substrate_plan.md | `sleep_substrate:GAP-5` | Sleep entry K-episode deterministic (no arousal trigger) | deferred | ext: V4 SD-037 arousal substrate |

## Done (43)

- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-A` -- ARC-062 substrate not implemented (gated-policy heads + learned context discriminator)
- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-C` -- ARC-062 discriminator output not routed to SD-033a LateralPFCAnalog.update() source vector
- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-D` -- E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias
- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-L` -- Biology lit-pull prerequisite for the socially-scaffolded rule-population sub-cluster (ARC
- `behavioral_diversity_isolation_plan.md` `behavioral_diversity_isolation:GAP-D` -- Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)
- `commitment_closure_plan.md` `commitment_closure:GAP-1` -- SD-033a bias head untrained (Go-side mechanically silent)
- `commitment_closure_plan.md` `commitment_closure:GAP-10` -- StepHarness audit of governance write paths
- `commitment_closure_plan.md` `commitment_closure:GAP-11` -- Phased rule_state training curriculum (GAP-3 deliverable 4 -- committed-mode elicitation)
- `commitment_closure_plan.md` `commitment_closure:GAP-2` -- EXP-0157 (V3-EXQ-461) delayed-reward persistence PASS
- `commitment_closure_plan.md` `commitment_closure:GAP-3` -- CausalGridWorldV2 env extensions (tolerance/counter-evidence/dual-cue)
- `commitment_closure_plan.md` `commitment_closure:GAP-5` -- MECH-090 V_s commit-release pathway (V3-EXQ-481 FAIL)
- `goal_pipeline_plan.md` `goal_pipeline:GAP-1` -- MECH-307 anticipatory-affect conjunction architecture
- `goal_pipeline_plan.md` `goal_pipeline:GAP-3` -- SD-012 sustained-drive amendment (EMA Option 1 + drive_floor Option 2)
- `goal_pipeline_plan.md` `goal_pipeline:GAP-6` -- MECH-269b V_s staleness-corrected consumer migration
- `infant_substrate_plan.md` `infant_substrate:GAP-1` -- Harm gradient env feature (harm_gradient_enabled, graduated harm proximity signal without 
- `infant_substrate_plan.md` `infant_substrate:GAP-10` -- EXQ-ISEF-001: harm gradient vs binary-contact residue geography formation speed
- `infant_substrate_plan.md` `infant_substrate:GAP-12` -- EXQ-ISEF-003: microhabitat zones vs homogeneous geography (latent state diversity)
- `infant_substrate_plan.md` `infant_substrate:GAP-15` -- Gate update: replace single z_goal.norm criterion in developmental_curriculum.md with 7-cr
- `infant_substrate_plan.md` `infant_substrate:GAP-2` -- Microhabitat zones env feature (microhabitat_enabled, zone_A/B/C resource+hazard density m
- `infant_substrate_plan.md` `infant_substrate:GAP-3` -- Transient benefit patches env feature (transient_benefit_enabled, stochastic high-salience
- `infant_substrate_plan.md` `infant_substrate:GAP-4` -- Stochastic attractor audit (enumerate CausalGridWorldV2 sources of irreducible randomness;
- `infant_substrate_plan.md` `infant_substrate:GAP-5` -- H_pos / zone_coverage telemetry (Shannon entropy of position histogram per episode, per-zo
- `infant_substrate_plan.md` `infant_substrate:GAP-6` -- residue_coverage_pct metric (fraction of grid cells with \|residue\| > threshold; harm_ben
- `infant_substrate_plan.md` `infant_substrate:GAP-7` -- traj_pairwise_cosine_mean metric (edit/cosine distance across stored trajectories; volumet
- `infant_substrate_plan.md` `infant_substrate:GAP-8` -- post_sleep_z_goal_retention metric (z_goal.norm ratio before/after sleep integration; repl
- `infant_substrate_plan.md` `infant_substrate:GAP-9` -- 4-phase infant curriculum scheduler (config hook for phase-gated parameter switching; Phas
- `sd033_governance_plan.md` `sd033_governance:CHK-ANCHOR` -- Anchor doc + auto-memory + task_inbox lit-pulls
- `sd033_governance_plan.md` `sd033_governance:CHK-CLAIMS` -- SD-034 + MECH-266/267/268 registered in claims.yaml
- `sd033_governance_plan.md` `sd033_governance:CHK-EXP_PROPOSALS` -- 9 EXP proposals (EXP-0156..0164; V3-EXQ-460..468 reserved)
- `sd033_governance_plan.md` `sd033_governance:CHK-MECH266` -- MECH-266 Schmitt-trigger asymmetric hysteresis + sub-tests PASS
- `sd033_governance_plan.md` `sd033_governance:CHK-MECH267` -- MECH-267 mode-conditioned hippocampal proposals + sub-tests PASS
- `sd033_governance_plan.md` `sd033_governance:CHK-MECH268` -- MECH-268 dACC PE saturation + EXP-0159/0164 sub-tests PASS
- `sd033_governance_plan.md` `sd033_governance:CHK-PUSH` -- REE_assembly + ree-v3 pushed; WORKSPACE_STATE + TASK_CLAIMS closed
- `sd033_governance_plan.md` `sd033_governance:CHK-SD034` -- SD-034 ClosureOperator implemented + EXP-0156/0162 substrate-readiness PASS
- `sd_037_axis_a_consumer_input_recalibration_plan.md` `sd_037_axis_a:P1` -- Phase 1 -- substrate-readiness diagnostic: log per-step consumer-input distributions (BLA/
- `sd_037_axis_a_consumer_input_recalibration_plan.md` `sd_037_axis_a:P2` -- Phase 2 -- deterministic p70 recalibration rule over the Phase-1 manifest; emit per-knob o
- `self_attribution_plan.md` `self_attribution:GAP-4` -- Nociceptive-comparator lit-pull (PAG/RVM/ACC)
- `sleep_substrate_plan.md` `sleep_substrate:GAP-1` -- MECH-204 precision recalibration consumer (F1 closure; V3-EXQ-541c PASS, cycle-count dose-
- `sleep_substrate_plan.md` `sleep_substrate:GAP-3` -- Phase B-E master flags default-False (cluster silent) -- unified use_sleep_aggregation_clu
- `sleep_substrate_plan.md` `sleep_substrate:GAP-4` -- MECH-273 offline gradient uses synthetic batch (replace with replay-derived)
- `sleep_substrate_plan.md` `sleep_substrate:GAP-6` -- StepHarness audit: SWS / REM write paths vs canonical sense/update sequence
- `sleep_substrate_plan.md` `sleep_substrate:GAP-7` -- Multi-episode driver pattern not standardised (sleep cycles fire once at K=1)
- `sleep_substrate_plan.md` `sleep_substrate:GAP-8` -- MECH-272 routing weights flip but HippocampalRouter does not consume them

## Plans WITHOUT closure_plan frontmatter (1)

These `*_plan.md` files exist but carry no `closure_plan` block, so their gaps are invisible to the structured closure map (they show as empty placeholder cards in the dashboard). Retrofit frontmatter to fold them in.

- `evidence/planning/arm_reuse_fingerprint_plan.md`

