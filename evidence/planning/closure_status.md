# REE-v3 Closure Status (snapshot)

Generated: 2026-06-10T19:56:05Z

GENERATED FILE -- do not edit by hand. This is a static, server-free snapshot of the closure map that serve.py serves live at `/api/closure` -> `/closure`. It is rebuilt from the `closure_plan` frontmatter of every `evidence/planning/*_plan.md` (auto-discovered, not whitelisted). Regenerate with `python scripts/generate_closure_snapshot.py` (runs automatically in `governance.sh`).

ACCURACY: this snapshot reports each node's self-declared `status`. Whether that status matches the actual terminal state of its experiments is audited separately by `check_closure_drift.py` -> [`closure_drift.md`](closure_drift.md). Read both together.

## Overall

- Weighted progress: **75.9%** across 75 non-deferred nodes in 11 plan(s) with closure frontmatter.
- Remaining (open/in-progress/blocked/partial): **23** nodes.
- Deferred (not required for v3 closure): 14 nodes.
- Done: 52 nodes.
- Status tally: blocked=8  blocked_pending_substrate=6  deferred=14  done=52  in_progress=6  partial=2  upstream_blocked=1

## Plans

| plan | title | nodes | progress | status counts | last_updated |
|------|-------|-------|----------|---------------|--------------|
| `sd_037_axis_b_sustained_threat_curriculum_plan.md` | SD-037 Axis (b): Sustained-Threat Env Curriculum | 4 | 10% | blocked:3 blocked_pending_substrate:1 | 2026-06-05 |
| `self_attribution_plan.md` | Self-Attribution Comparator Loop | 5 | 32% | blocked:3 deferred:1 done:1 | 2026-06-04 |
| `behavioral_diversity_isolation_plan.md` | Behavioural Diversity Isolation | 8 | 57% | deferred:4 done:1 in_progress:2 partial:1 | 2026-06-08 |
| `arc_062_rule_apprehension_plan.md` | Rule Apprehension | 12 | 61% | blocked:1 blocked_pending_substrate:1 deferred:3 done:4 in_progress:2 partial:1 | 2026-06-09 |
| `goal_pipeline_plan.md` | Goal Pipeline (wanting / liking / drive cascade) | 7 | 70% | blocked_pending_substrate:2 deferred:1 done:4 | 2026-06-04 |
| `commitment_closure_plan.md` | Commitment / Closure / Mode-Governance | 11 | 87% | deferred:2 done:7 in_progress:2 | 2026-06-04 |
| `arm_reuse_fingerprint_plan.md` | Arm-Reuse Fingerprint (baseline-arm reuse via substrate fingerprint) | 7 | 87% | blocked:1 done:6 | 2026-06-10 |
| `sleep_substrate_plan.md` | Sleep Substrate | 8 | 87% | deferred:1 done:6 upstream_blocked:1 | 2026-05-31 |
| `infant_substrate_plan.md` | Infant Substrate Expansion | 15 | 88% | blocked_pending_substrate:2 done:13 | 2026-05-30 |
| `sd033_governance_plan.md` | SD-033 Governance (OCD test battery sub-plan) | 8 | 100% | done:8 | 2026-05-29 |
| `sd_037_axis_a_consumer_input_recalibration_plan.md` | SD-037 Axis (a): Consumer-Input-Threshold Recalibration | 4 | 100% | deferred:2 done:2 | 2026-06-05 |

## Remaining work to close v3 (23)

Ordered by phase, then severity. This is the answer to "what is left."

| plan | node | title | status | phase | sev | owner_exq | active blocker | last_updated |
|------|------|-------|--------|-------|-----|-----------|----------------|--------------|
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P1b` | Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under | blocked_pending_substrate | 1 | load-bearing | V3-EXQ-625c | RESUME the Phase 1b gate (or its successor) once the behavioural-diversity substrate amend | 2026-06-05 |
| self_attribution_plan.md | `self_attribution:GAP-1` | ARC-033 vs ARC-058 path arbitration (forensic 445h read) | blocked | 1 | high | V3-EXQ-445h | Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that | 2026-06-09 |
| arm_reuse_fingerprint_plan.md | `arm_reuse_fingerprint:P1-auto` | First AUTOMATED index-HIT in the wild -- next genuinely-needed iteration (610g / | blocked | 1 | low | V3-EXQ-610g (or 643c) -- pending; 610g gated on  | No standalone work warranted -- the automated index-HIT rides on the next genuinely-needed | 2026-06-10 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-B` | MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP | in_progress | 2 | load-bearing | V3-EXQ-654a QUEUED 2026-06-09 (priority 250, mac | BOTH routed steps are now DONE (see governance_2026_06_09_amend_and_requeue): the crf_pers | 2026-06-09 |
| commitment_closure_plan.md | `commitment_closure:GAP-4` | OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction | in_progress | 2 | high | V3-EXQ-460b/461b/463b/464b/466b/467b/468b (Phase | LIVE BLOCKER (2026-06-10): GAP-4 is gated on the scaffolded_sd054_onboarding goal-achievem | 2026-06-10 |
| goal_pipeline_plan.md | `goal_pipeline:GAP-2` | SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor) | blocked_pending_substrate | 2 | high | V3-EXQ-514l | RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queu | 2026-06-10 |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P2` | Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b ma | blocked | 2 | high |  | depends_on: sd_037_axis_b:P1b | 2026-06-05 |
| self_attribution_plan.md | `self_attribution:GAP-2` | SD-029 / MECH-256 retest under full substrate stack | blocked | 2 | high | TBD | RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblocka | 2026-06-09 |
| sleep_substrate_plan.md | `sleep_substrate:GAP-2` | SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassifi | upstream_blocked | 2 | high | V3-EXQ-265a | Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_aut | 2026-05-31 |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P3` | Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lif | blocked | 3 | high |  | depends_on: sd_037_axis_b:P2 | 2026-06-05 |
| self_attribution_plan.md | `self_attribution:GAP-3` | MECH-257 dual-function 3-arm ablation re-queue | blocked | 3 | medium | TBD | depends_on: self_attribution:GAP-1, self_attribution:GAP-2 | 2026-06-04 |
| sd_037_axis_b_sustained_threat_curriculum_plan.md | `sd_037_axis_b:P4` | Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on th | blocked | 4 | high | V3-EXQ-483f | depends_on: sd_037_axis_b:P3 | 2026-06-05 |
| infant_substrate_plan.md | `infant_substrate:GAP-13` | EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal nove | blocked_pending_substrate | 4 | medium | V3-EXQ-590 | Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; | 2026-06-09 |
| infant_substrate_plan.md | `infant_substrate:GAP-14` | EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion sat | blocked_pending_substrate | 4 | medium | V3-EXQ-591 | 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-un | 2026-06-10 |
| goal_pipeline_plan.md | `goal_pipeline:GAP-7` | Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 | blocked_pending_substrate | 7 | load-bearing |  | STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 c | 2026-06-10 |
| commitment_closure_plan.md | `commitment_closure:GAP-8` | SD-033b behavioural validation (devaluation + perceptual discrimination) | in_progress | 7 | medium | V3-EXQ-485d (trained-OFC-head substrate-readines | Trained-OFC-head SUBSTRATE landed 2026-06-09 (ree-v3 382db2c): OFCConfig.train_state_bias_ | 2026-06-09 |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-B` | Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341) | partial | 660 landed PASS/supports -> temperature-graded confirmation + governance ratification owed | load-bearing | V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41 | PARTIAL 2026-06-10. V3-EXQ-660 has LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-q | 2026-06-10 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-H` | ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-0 | partial | 2-3 | medium | V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MEC | PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validate | 2026-06-08 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-I` | ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorpt | blocked_pending_substrate | 2-3 | medium | V3-EXQ-606b | BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creat | 2026-06-03 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-K` | MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidenc | in_progress | 2-3 | medium | V3-EXQ-546 (done, diagnostic/non_contributory);  | IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence s | 2026-06-08 |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-A` | Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM  | in_progress | substrate validated ready -> FP-2 falsifier work resumes | medium | V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared- | IN FLIGHT 2026-06-09 on V3-EXQ-569f (queued via /queue-experiment; supersedes V3-EXQ-569d) | 2026-06-09 |
| behavioral_diversity_isolation_plan.md | `behavioral_diversity_isolation:GAP-C` | Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog) | in_progress | P1 | medium | V3-EXQ-603k (Stage-H harm-pathway training; queu | IN FLIGHT 2026-06-08 on V3-EXQ-603i. Do not queue the Q-045/MECH-313/MECH-260 retest until | 2026-06-10 |
| arc_062_rule_apprehension_plan.md | `arc_062_rule_apprehension:GAP-J` | MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / | blocked | 2-3 | low |  | depends_on: arc_062_rule_apprehension:GAP-B | 2026-05-17 |

## Deferred -- not required for v3 closure (14)

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
| goal_pipeline_plan.md | `goal_pipeline:GAP-5` | SD-049 Phase 3 consumer cascade migration (read-side fidelity) | deferred | depends_on: goal_pipeline:GAP-4 |
| sd_037_axis_a_consumer_input_recalibration_plan.md | `sd_037_axis_a:P3` | Phase 3 -- verification diagnostic: confirm recalibrated thresholds lift consume | deferred | depends_on: sd_037_axis_a:P2 |
| sd_037_axis_a_consumer_input_recalibration_plan.md | `sd_037_axis_a:P4` | Phase 4 -- V3-EXQ-483f behavioural validation (4-arm 2x2 OFF_OFF/ON_OFF/OFF_ON/O | deferred | depends_on: sd_037_axis_a:P3 |
| self_attribution_plan.md | `self_attribution:GAP-5` | SD-030/SD-031 z_self / z_world materialisation (V4) | deferred |  |
| sleep_substrate_plan.md | `sleep_substrate:GAP-5` | Sleep entry K-episode deterministic (no arousal trigger) | deferred | ext: V4 SD-037 arousal substrate |

## Done (52)

- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-A` -- ARC-062 substrate implemented and readiness-validated (gated-policy heads + learned contex
- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-C` -- ARC-062 discriminator output not routed to SD-033a LateralPFCAnalog.update() source vector
- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-D` -- E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias
- `arc_062_rule_apprehension_plan.md` `arc_062_rule_apprehension:GAP-L` -- Biology lit-pull prerequisite for the socially-scaffolded rule-population sub-cluster (ARC
- `arm_reuse_fingerprint_plan.md` `arm_reuse_fingerprint:GATE` -- Section 9.0 hard prerequisite -- cross-instance determinism gate (610 OFF baseline minted 
- `arm_reuse_fingerprint_plan.md` `arm_reuse_fingerprint:MINT` -- Baseline pre-minting -- canonical baseline modules + low-priority cloud mint experiments f
- `arm_reuse_fingerprint_plan.md` `arm_reuse_fingerprint:P0` -- Phase 0 -- instrument only: arm_fingerprint lib (substrate content-hash + per-cell fingerp
- `arm_reuse_fingerprint_plan.md` `arm_reuse_fingerprint:P1-build` -- Phase 1 consumer machinery -- arm_fingerprint_index.json writer, try_reuse_cell refuse-by-
- `arm_reuse_fingerprint_plan.md` `arm_reuse_fingerprint:P1-cite` -- First live use -- explicit-cite consumer (V3-EXQ-647) reuses all three 646 OFF-baseline ce
- `arm_reuse_fingerprint_plan.md` `arm_reuse_fingerprint:P1-fix` -- Driver-script_path coupling fix -- include_driver_script_in_hash so a consumer with its ow
- `behavioral_diversity_isolation_plan.md` `behavioral_diversity_isolation:GAP-D` -- Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)
- `commitment_closure_plan.md` `commitment_closure:GAP-1` -- SD-033a bias head untrained (Go-side mechanically silent)
- `commitment_closure_plan.md` `commitment_closure:GAP-10` -- StepHarness audit of governance write paths
- `commitment_closure_plan.md` `commitment_closure:GAP-11` -- Phased rule_state training curriculum (GAP-3 deliverable 4 -- committed-mode elicitation)
- `commitment_closure_plan.md` `commitment_closure:GAP-2` -- EXP-0157 (V3-EXQ-461) delayed-reward persistence PASS
- `commitment_closure_plan.md` `commitment_closure:GAP-3` -- CausalGridWorldV2 env extensions (tolerance/counter-evidence/dual-cue)
- `commitment_closure_plan.md` `commitment_closure:GAP-5` -- MECH-090 V_s commit-release pathway (V3-EXQ-481 FAIL)
- `commitment_closure_plan.md` `commitment_closure:GAP-9` -- SD-033c/d/e graph-consolidation incomplete
- `goal_pipeline_plan.md` `goal_pipeline:GAP-1` -- MECH-307 anticipatory-affect conjunction architecture
- `goal_pipeline_plan.md` `goal_pipeline:GAP-3` -- SD-012 sustained-drive amendment (EMA Option 1 + drive_floor Option 2)
- `goal_pipeline_plan.md` `goal_pipeline:GAP-4` -- MECH-295 drive->liking->approach cascade Tier-1 retest cohort
- `goal_pipeline_plan.md` `goal_pipeline:GAP-6` -- MECH-269b V_s staleness-corrected consumer migration
- `infant_substrate_plan.md` `infant_substrate:GAP-1` -- Harm gradient env feature (harm_gradient_enabled, graduated harm proximity signal without 
- `infant_substrate_plan.md` `infant_substrate:GAP-10` -- EXQ-ISEF-001: harm gradient vs binary-contact residue geography formation speed
- `infant_substrate_plan.md` `infant_substrate:GAP-11` -- EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison
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

## Plans WITHOUT closure_plan frontmatter (0)

These `*_plan.md` files exist but carry no `closure_plan` block, so their gaps are invisible to the structured closure map (they show as empty placeholder cards in the dashboard). Retrofit frontmatter to fold them in.

_None -- every plan doc is mapped._

## V4 / V5 forward roadmap (excluded from v3 closure %)

Forward-roadmap plans (`generation: v4` / `v5`). These are NOT closure maps -- V4/V5 have no experiments yet, so their nodes carry no `owner_exq` and do not count toward the V3 closure percentage. Each node's gate is the V3-era prerequisite that must land first.

- **V4**: 8.0% across 85 non-deferred nodes in 13 plan(s).

| gen | plan | node | title | status | sev | gate (readiness) | last_updated |
|-----|------|------|-------|--------|-----|------------------|--------------|
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-1` | FOUNDATION -- per-candidate multi-channel affect vector substrate (MEC | blocked | load-bearing | V3 NARROW instance is already DONE and is NOT this node: V3-EXQ-643a PASS established the  | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-1` | Memory-type taxonomy decision (Q-060): distinct autobiographical-event | open | load-bearing | V3 owns only the episodic<->semantic axis (MECH-121 NREM SWR episodic->semantic transfer)  | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-2` | Graded action-status + self-reference-frame vocabulary decision (Q-068 | open | load-bearing | V3 already enforces the coarse boundary: MECH-094 simulation/commit write-profiles + MECH- | 2026-06-10 |
| v4 | drives_motivation_v4_plan.md | `drives_motivation_v4:DRV-1` | Non-terminal drive register (drives beyond hunger/thirst as first-clas | open | load-bearing | V3 LIVE single-axis homeostatic drive: SD-012 (drive_level = 1.0 - energy from obs_body[3] | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-1` | Single-slot vs multi-slot fork (the first design decision: does V4 wid | open | load-bearing | V3 goal pipeline is SINGLE-STREAM: one z_goal, one SD-039 ghost-goal-bank rank, one E3-com | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-1` | GATE -- multi-step hippocampally-planned system validated in V3 (MECH- | blocked | load-bearing | MECH-163 dual-system discrimination demonstrated in V3 (habit SNc/dorsal-striatum model-fr | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-1` | Name + route the inference layer (V3 architecture note, no substrate) | open | load-bearing | V3 ALREADY HAS the ingredients: ARC-004 (L-space), ARC-007 (path completion), ARC-018 (rol | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-2` | Inferred state must not collapse to perceived observation (invariant) | open | load-bearing | V3 state invariants already present: INV-035 (state not defined by sensory appearance) + I | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-1` | Allocation-gate decision stage on MECH-261 (integrate / partial_overla | open | load-bearing | V3 OWNS THE GATES already: MECH-094 (hypothesis tag = categorical write gate, stable), MEC | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-1` | Substrate-vocabulary expansion is the gating fork (atomic-only V3 has  | open | load-bearing | V3 substrate vocabulary is FIXED at z_world + atomic actions (per MECH-299 notes: no secon | 2026-06-10 |
| v4 | object_representation_v4_plan.md | `object_representation_v4:OBJ-1` | Type-vs-token-vs-anchor representational fork (the first design decisi | open | load-bearing | V3 LIVE object work is TYPE-level: SD-049 per-type tag + classifier head; SD-015 location- | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-1` | Smell-vs-sight adaptor-depth fork (the first design decision) | open | load-bearing | V3 LIVE perception is the near-raw / gradient end: smell-like sensing, gradient-only world | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-1` | Opening-vs-closure asymmetry framing + the V3-conservative-is-insuffic | open | load-bearing | CLOSURE side already built: INV-074 (crystallization necessity, universal invariant), MECH | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-1` | z_self promoted from body-state latent to a stateful self-model (DR-13 | open | load-bearing | V3 BEGINNING present (no gate): SD-005 z_self/z_world split is implemented -- z_self exist | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-2` | Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across | in_progress | high | ARC-088 is implementation_phase v3 (a unifying MAP over already-owned V3 affect machinery: | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-2` | Explicit active-separation operation (separate != failed-integration)  | blocked | high | MECH-147 DG pattern separation must land (V4): non-redundant sparse encoding of similar z_ | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-1` | V3 reduced form -- MECH-384 self-narration trace surface (the seed the | open | medium | MECH-384 is the ONLY V3-compatible instantiation: implementation_phase v3, epistemic_categ | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-2` | Biology grounding lit-pull (Hensch / Bear-Singer / Froemke / Kilgard / | open | medium | Project rule feedback_biology_before_formal_definitions: commission this /lit-pull BEFORE  | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-2` | Unified autobiographical event-token store (ARC-085): ONE self-tagged  | blocked | load-bearing | ARC-007 retrospective replay (paths through residue-field terrain) -- present in V3, desig | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-3` | PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed  | blocked | load-bearing | V3 play substrate must land first: ARC-049 play_frame_tag in LatentState (L2 continuous si | 2026-06-10 |
| v4 | drives_motivation_v4_plan.md | `drives_motivation_v4:DRV-2` | Multidrive arbitration / orchestration policy (which drive wins when s | blocked | load-bearing | V3 LIVE drive->approach plumbing the policy must compose over: MECH-295 (drive->liking->ap | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-2` | PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module  | blocked | load-bearing | V3 HOOKS present: SD-032a operating_mode vocabulary (discrete-mode primitive, landed) + SD | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-2` | PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040) | blocked | load-bearing | MECH-163 planned system validated (HPL-1): there must be a model-based trajectory proposer | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-3` | Belief-state hypothesis set (top-k latent-state hypotheses with precis | blocked | load-bearing | V3 generator present: MECH-022 (hippocampal hypothesis injection gated by control plane) + | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-4` | Raw-episode-preservation invariant (consolidation_output MUST NOT repl | open | load-bearing | ARC-007 (hippocampal path store/replay residue field, architectural_commitment) IS the raw | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-2` | PILLAR A -- action-chunk cache (SD-045): the first reusable-unit subst | blocked | load-bearing | ARC-021 three-BG-loop framework present (chunk cache lives in the dorsolateral-loop slot) | 2026-06-10 |
| v4 | object_representation_v4_plan.md | `object_representation_v4:OBJ-2` | PILLAR 1 -- token-instance object-file substrate (permanence through o | open | load-bearing | Reactivate ARC-006 / MECH-044 / MECH-045 (object-file + relational binding + object-file p | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-2` | PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientati | open | load-bearing | V3 gradient-only sensing already approximates a smell-like primitive (follow / escape / st | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-3` | PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate | blocked | load-bearing | MECH-333 open-phase core (pre-window F-gradient attenuation / PV-analog competitive gating | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-2` | Finish self-attribution: complete the per-stream comparator topology ( | blocked | load-bearing | V3 BEGINNING present: self-attribution on the z_world causal-footprint stream runs (SD-031 | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-3` | Expression as emergent action geometry (MECH-360) -- the readout side  | blocked | high | AE-1 (MECH-359) per-candidate affect vector built -- expression style (hesitation, latency | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-4` | Candidate-gradient hippocampal episode schema (MECH-361) -- affect gra | blocked | high | AE-1 (MECH-359) per-candidate affect vector built | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-4` | Inferred affordance field (afford. not directly perceived; biases E3 c | blocked | high | V3 rule field present: ARC-062 (weak-reading gated policy) live; ARC-063 (CandidateRule fi | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-3` | False-linking-risk / reality-coherence cost term (the single aspect wi | open | high | MECH-094 (sim-vs-real confabulation gate) is the nearest reality-coherence machinery V3 ha | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-3` | PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed an | blocked | high | MECH-269 AnchorSet / V_s substrate live in V3 (SD-040 adds a type-key projection alongside | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-4` | PILLAR B -- state-conditional plasticity-gain architectural commitment | blocked | high | ARC-075 (infant-curriculum plasticity-magnitude asymmetry, candidate, implementation_phase | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-7` | Layer-specificity adjudication (one global scalar vs per-substrate gat | open | high | Open question: does plasticity-gain modulate identically across encoder / residue / hippoc | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-8` | Biology grounding completion (Vygotsky private speech, DMN, label-as-c | deferred | medium | Current state: architectural-analogy anchors only (Vygotsky private speech; Lupyan/Swingle | 2026-06-10 |
| v4 | drives_motivation_v4_plan.md | `drives_motivation_v4:DRV-3` | Drive-arbitration biology grounding (multidrive competition / drive hi | open | medium | Project rule feedback_biology_before_formal_definitions: commission a biology lit-pull BEF | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-6` | PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD | blocked | medium | V3 HOOKS: MECH-089 theta-gamma packaging (formats content for E3) + SD-026 z_goal write ch | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-7` | Inference failure-mode register + biology grounding (lit-pulls) | open | medium | Biology grounding (project rule feedback_biology_before_formal_definitions): L1 hippocampa | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-7` | Gated-write-authority on consolidation (over-frequent rewriting is a f | blocked | medium | INV-049 (offline-update necessity, universal invariant) is the complementary law: offline  | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-8` | Biology + source grounding completion (allocation-policy lit DONE; con | in_progress | medium | Allocation-gate lit DONE 2026-06-06: VERDICT at evidence/literature/targeted_review_contex | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-8` | Biology grounding completion for the abstraction substrates (chunking  | in_progress | medium | L-type type-prototype substrate (Quiroga 2005, Schapiro 2016/2017, Constantinescu 2016, He | 2026-06-10 |
| v4 | object_representation_v4_plan.md | `object_representation_v4:OBJ-6` | Biology grounding completion (object-files / permanence / affordances  | in_progress | medium | L1 object-files & feature-binding (Kahneman/Treisman/Gibbs 1992; Treisman & Gelade 1980 FI | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-6` | Adaptor-maturity curriculum gate: each sense admitted when its adaptor | open | medium | ARC-019 staged developmental curriculum (provisional) -- the existing curriculum-stages cl | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-7` | Biology grounding completion (perceptual-manifold / colour-geometry /  | open | medium | L1 perceptual-manifold / similarity geometry (Schrodinger colour theory completion, the so | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-3` | Provenance-bearing event token + one-way committed-vs-imagined gate (M | blocked | load-bearing | MECH-094 (simulation-mode vs real-experience distinction; failure = confabulation) -- the  | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-5` | Safety-route inference (infer route to safety from partial map/cue/gra | blocked | load-bearing | V3 bridge present-but-unconfirmed: SD-059 + MECH-358 supply per-first-action-class relief/ | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-3` | z_self enters E3 viability scoring (DR-10): bodily state modulates tra | open | load-bearing | V3 LIMIT: E3.score_trajectory() currently evaluates entirely in z_world space -- there is  | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-7` | Compulsion-risk substrate -- slow modulator (MECH-369) + composed read | blocked | high | MECH-369 most naturally AMENDS the slow-modulator layer (SD-037 orexin-analog gain cluster | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-4` | Imagination-learning licit/forbidden principle (ARC-level, folded into | open | high | REE owns substrate components implicitly enforcing what learning is licit from imagination | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-4` | PILLAR -- private speech as external cognitive-control surface (MECH-3 | blocked | high | INV-034 goal-maintenance target (the thing private speech regulates) must be the live arbi | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-5` | PILLAR -- developmental compression ladder (MECH-381): externalise-the | blocked | high | INV-060 + MECH-197 play-type progression (sensorimotor->constructive->pretend->rule-based- | 2026-06-10 |
| v4 | drives_motivation_v4_plan.md | `drives_motivation_v4:DRV-4` | Orienting/surveying drive: pre-approach active-sensing control state | blocked | high | V3 LIVE upstream cue chain the orienting mode sits between: SD-057 / MECH-347 cue-triggere | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-3` | PILLAR 2 -- counterfactual-value tracking and switch-to-alternative ga | blocked | high | V3 has the CHOSEN-option value signal (SD-033c vmPFC value integration, v3); MECH-264 adds | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-4` | PILLAR 3 -- relative-importance monitoring across competing goals + dA | blocked | high | SD-046 multi-slot GoalState: each slot generates its own ghost-goal-bank rank, ghost-probe | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-5` | PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's w | blocked | high | V3 has the CLOSURE side of the action arc (MECH-061 commit-boundary token v3; MECH-057a co | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-3` | DG-equivalent pattern separation before rollout proposal (MECH-147) | blocked | high | SD-004 action-object hippocampal map backbone present (v3) and the MECH-033 kernel-chainin | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-4` | Pure time cells -- temporal scaffolding for E3 credit assignment (MECH | blocked | high | ARC-018 rollout viability module + ARC-039 offline replay live (both v3): E3 must already  | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-5` | CA1 mismatch novelty gate on rollout injection (MECH-149) | blocked | high | differentiable CA1 mismatch signal computable in the latent stack (E1 prediction error at  | 2026-06-10 |
| v4 | inference_belief_state_v4_plan.md | `inference_belief_state_v4:INF-6` | Epistemic action pressure (information-gathering as survival-relevant, | blocked | high | V3 curiosity machinery present: Q-044 cohort (MECH-314a striatal novelty / MECH-314b front | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-5` | Provenance + contradiction-flag + rollback layer on consolidated memor | blocked | high | MECH-068 (consolidation selectivity lives in the operator, candidate) is the on-point prec | 2026-06-10 |
| v4 | memory_lifecycle_v4_plan.md | `memory_lifecycle_v4:MEM-6` | Retrieval-scope vs action-authority split (reflection-retrieval != act | open | high | MECH-257 (E2_x dual-function: retrospective comparator vs prospective rollout-scoring, can | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-4` | PILLAR B retrieval -- prototype-readout operator + type-V_s gating (ME | blocked | high | SD-040 type-keyed AnchorSet entries exist (MECH-296 softmax-attention readout has nothing  | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-5` | PILLAR C -- option library (SD-042): named reusable subroutines (init- | blocked | high | ARC-021 three-BG-loop framework present (option arbitration slot) | 2026-06-10 |
| v4 | object_representation_v4_plan.md | `object_representation_v4:OBJ-3` | PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged obj | open | high | V3 BEGINNING present (no gate): SD-005 z_self split, SD-003 self-attribution, MECH-277 + A | 2026-06-10 |
| v4 | object_representation_v4_plan.md | `object_representation_v4:OBJ-4` | PILLAR 3 -- tools/affordances object->action binding (ARC-082) | blocked | high | V3 grounding track (straddles V3, owned separately): EXP-0155 instrumentation of SD-016 cu | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-3` | PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metr | blocked | high | Reactivate / extend MECH-103 (per-modality encoder pathway) on a genuine V4 multimodal inp | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-4` | Metric-origin fork: per-sense perceptual metric LEARNED from similarit | open | high | Q-065 part (1): for each modality, is the perceptual metric self-organised from the statis | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-5` | Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-soc | blocked | medium | V4 social substrate exists (other-agent representation) -- the canonical soothing trigger  | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-6` | Laughter regime-transition discharge (MECH-364) + crying/distress-voca | blocked | medium | E3 conflict/constraint-load readout: ARC-016 already exposes an E3-derived prediction-vari | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-6` | ACh permissive write-gate on the surprise buffer (MECH-207) | blocked | medium | MECH-205 surprise buffer + MECH-206 CA1 PE comparator present (sleep_substrate stack) | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-5` | PILLAR C -- PV-interneuron inhibitory-maturation window-closure clock | deferred | medium | Biology-faithful refinement of MECH-333 closure / MECH-334: a time-since-onset accumulator | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-4` | E2 prediction error modulates E3 confidence (DR-12): PE-magnitude sign | open | medium | V3 LIMIT: E3 trusts E2 unconditionally; high E2 prediction error does not currently down-w | 2026-06-10 |
| v4 | plasticity_neuromodulation_v4_plan.md | `plasticity_neuromodulation_v4:PLW-6` | PILLAR D -- BDNF-analog trophic window-duration knob (lowest priority) | deferred | low | The duration knob sits ON TOP of the gain knob (PLW-3) and the closure clock (PLW-5); both | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-6` | PILLAR D -- theta-packaging + cognitive-map traversal scale to the act | blocked | load-bearing | MECH-089 theta-gamma packaging primitive + MECH-294 theta-burst-as-E3-packet sibling confi | 2026-06-10 |
| v4 | perceptual_adaptors_v4_plan.md | `perceptual_adaptors_v4:PA-5` | PILLAR C -- cross-modal negotiation currency: making heterogeneous sen | blocked | load-bearing | Q-065 part (2): how are smell's gradient geometry, sight's perceptual manifold, touch's bo | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-5` | Event-level write-authority gate over the durable model-update path (M | blocked | high | MECH-261 (mode-conditioned write CHANNEL gating via SD-032a) -- gates the channel per oper | 2026-06-10 |
| v4 | object_representation_v4_plan.md | `object_representation_v4:OBJ-5` | PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-f | blocked | high | MECH-163 multi-step hippocampal planning (V4 social-entry gate) | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-5` | z_self-domain goal representation (DR-11): self-state goals representa | blocked | high | V3 WIRING AUDIT (MECH-214, 2026-04-07): z_goal lives purely in z_world; V3 grid world conf | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-6` | Proxy/hedonic dissociating environment (DR-14): substrate that surface | blocked | high | V3 LIMIT: the grid world makes proxy == hedonic by construction; you cannot show a goal pu | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-6` | Candidate-gradient episode content schema (MECH-361): affect gradient  | blocked | medium | MECH-261 (mode-conditioned write gating) -- MECH-361 amends its CONTENT schema (WHAT is wr | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-6` | Distancing operator (MECH-382): first/third-person reframe as an arbit | blocked | medium | ARC-005 precision-routing control plane (the thing the reframe acts through) live | 2026-06-10 |
| v4 | developmental_dmn_v4_plan.md | `developmental_dmn_v4:DMN-7` | Labels as top-down perceptual-control signals (MECH-383): self-directe | blocked | medium | ARC-005 precision-routing control plane + the distributed precision-selection cluster (MEC | 2026-06-10 |
| v4 | drives_motivation_v4_plan.md | `drives_motivation_v4:DRV-5` | Non-terminal failure-grade taxonomy as a transfer-world launch profile | deferred | medium | V3 LIVE scaffold substrate it formalises: scaffolded_sd054_onboarding (nursery / protected | 2026-06-10 |
| v4 | goal_deliberation_v4_plan.md | `goal_deliberation_v4:GDL-7` | Graded action-status vocabulary -- decide whether deliberation needs a | deferred | medium | Q-068 is an OPEN QUESTION (answer_state): does REE need an explicit graded action-status v | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-7` | Schema-primed rapid assimilation (INV-039) | blocked | medium | stable, dense residue-field map from sustained V3 training (a sparse/unstable map reverts  | 2026-06-10 |
| v4 | hippocampal_planning_v4_plan.md | `hippocampal_planning_v4:HPL-8` | Improvement-tier enrichments -- compression, dual-mode construction, a | deferred | medium | MECH-230/236/238 V3 navigation substrate present (metric-space goal encoding) -- the base  | 2026-06-10 |
| v4 | object_reasoning_abstraction_v4_plan.md | `object_reasoning_abstraction_v4:OBJ-ABS-7` | Developmental sparsification policy for the abstraction substrates (Q- | deferred | medium | ARC-019 + MECH-362 developmental-pruning substrate present (Q-057's depends_on) | 2026-06-10 |
| v4 | affect_expression_v4_plan.md | `affect_expression_v4:AE-8` | Developmental sparsification of the affect/memory substrate (MECH-362, | deferred | low | MECH-362 amends ARC-019 (staged developmental curriculum) by adding a subtractive pruning  | 2026-06-10 |
| v4 | self_model_v4_plan.md | `self_model_v4:SELF-7` | Maturational-sequence honesty gate (INV-064): self-stability must prec | blocked | high | INV-064 is emergent on ARC-001/002/003/ARC-019 and carries pending_substrate_reconfirmatio | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-7` | Switchable episodic perspective tag (MECH-366): participant/observer v | blocked | medium | SD-005 (z_self/z_world split) -- nearest existing substrate, but represents self-vs-world  | 2026-06-10 |
| v4 | autobiographical_memory_v4_plan.md | `autobiographical_memory_v4:ABM-8` | Consolidation write-paths the store must respect (MECH-252 / MECH-253  | deferred | medium | MECH-252 (SWS consolidates goal-value PE into stored goal-representation CONTENT, not atte | 2026-06-10 |

