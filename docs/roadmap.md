---
title: Roadmap
nav_order: 6
---

# Roadmap

**Claim Type:** implementation_note
**Scope:** Program phases, repository roles, and phase-gate criteria
**Depends On:** IMPL-020, IMPL-021, IMPL-022, MECH-057, MECH-058, MECH-059, MECH-060
**Status:** candidate
**Claim ID:** IMPL-008
<a id="impl-008"></a>

---

## Status Snapshot (2026-05-17T01:11Z -- nightly docs sync; sleep_substrate GAP-6/GAP-8 complete + GAP-3 unified master flag; infant_substrate GAP-2/3/5/6 env substrates; ARC-067/068 child-MECH design complete (MECH-330 + MECH-331; ARC-068 collapses into MECH-320); calibration-debt diversity sprint diagnoses ARC-065 developmental warm-start failure; governance Proposal G2 backward-traceability checker wired; pending_review 0)

- **SDs / MECHs / substrate landings since the 2026-05-13T01:10Z nightly:**
  - **sleep_substrate GAP-6 + GAP-8** 2026-05-15 -- StepHarness write-path audit (e1_input scaled by anchor_weight in run_sws_schema_pass) + MECH-272 anchor-channel consumer (mean_anchor threaded through SleepLoopManager._run_cycle -> run_sleep_cycle). V3-EXQ-565 GAP-8 routing-consumer full-runner PASS 2026-05-15T18:03Z (arm0_applied_mean=1.0, arm1~0.6, C1/C2/C3 all True). sleep_substrate_plan.md GAP-6/GAP-8 open -> done; Rung 5 cleared in calibration_debt_index.md.
  - **sleep_substrate GAP-3** 2026-05-16 -- unified `REEConfig.use_sleep_aggregation_cluster` field + enable_sleep_aggregation_cluster() resolving the eight Phase A-E sub-flags consistently from __post_init__ + end of from_dims (mirrors use_mech307_conjunction / enable_goal_stream). OR-only; MECH-204 + anchor-set / e2_harm_s prereqs deliberately NOT bundled. V3-EXQ-581 owner-EXQ dry-run 6/6 PASS (C1-C5 all four phases fire end-to-end under one flag; C6 ARM_CLUSTER==ARM_EXPLICIT proves pure ergonomics). The 2026-05-16 GAP-4-entry GAP-8/GAP-3 conflation corrected (V3-EXQ-565 is GAP-8's owner-EXQ).
  - **infant_substrate GAP-2/3/5/6** 2026-05-16 -- CausalGridWorldV2 env substrates: microhabitat Voronoi zones (V3-EXQ-577 FAIL, C2 zone_map_coverage diagnosed as a test-design false-negative -- per-episode missing_012 over-constraint vs stochastic Voronoi+ecotone design; substrate functionally validated by C1/C3/C4; V3-EXQ-577a corrected-C2 routed), transient-benefit patches for z_goal seeding (V3-EXQ-578 PASS), pos/zone telemetry (GAP-5), residue-coverage telemetry (ResidueField.get_coverage_telemetry; V3-EXQ-580 PASS 3/3 seeds, ARM_1 harm-gradient coverage 0.77-0.94 >> ARM_0 binary 0.23). claims.yaml not modified (governed by full infant pipeline).
  - **ARC-067 / ARC-068 child-MECH design** 2026-05-16 -- two-child split for ARC-067: MECH-330 idle_aversion_acute_restlessness_accumulator (engagement-rate EWMA -> z_harm_a write; 3-input estimator commit-transitions / deliberation-depth / residue-write-rate; Wilson 2014 + Danckert 2018 anchors) + MECH-331 idle_aversion_chronic_anhedonic_flatness_substrate (frontostriatal effort-allocation integrator seeded by sustained MECH-330 non-discharge; apathy archetype per Husain-Roiser 2018; preserves MECH-295 hedonic experience). ARC-068 collapses into MECH-320 per the ARC-068 lit-pull R3 verdict (Niv 2007 mathematical symmetry -- the MECH-320 w_passive term IS the ARC-068 implementation). 635 claims; biology-before-formal-definitions gate now fully clear for the non_deficit_action_drives family.
  - **governance Proposal G2** 2026-05-16 -- `scripts/check_backward_traceability.py` (PyYAML + regex; checks developmental-keyword claims against developmental_needs_register.md Claim IDs; exits 1 on WARNING, `--warn-only` exits 0; `SKIP_TRACEABILITY=1` bypass) wired into governance.sh Step 4b after build_claims_json.py as a hard gate. Current gap: 141 developmental claims, 115 untraced (register coverage ongoing).
- **Diagnostic / experimental results (calibration-debt diversity sprint, 2026-05-16):**
  - V3-EXQ-569 FAIL -- all arms entropy ~0.496, zero diversity lift.
  - V3-EXQ-570 PASS -- E2 is not the bottleneck (rollout ratio 52.1).
  - V3-EXQ-571 PASS -- F (forward-model) term dominates 88-89% of E3 temporal variance; ALL MECH-313/314/320 + dACC / lateral_pfc / ofc / gated_policy / mech295 diversity-bias components contribute ~0. e3_selector.py + agent.py instrumented with default-OFF score-decomposition flags (349/350 contracts; the one failure pre-existing + unrelated).
  - V3-EXQ-573 NULL -- ARC-065 bias-scale 5-10x sweep, all 10 arms bit-for-bit identical.
  - Replay analysis register updates: DEV-NEED-030 (stage-aware replay scheduling) + DEV-NEED-031 (MECH-124 prevention gate); 6 EXP-IDEV-001..006 proposals (317 total); INV-049 evidence_quality_note updated with the infant-content-poverty / waking-consolidation-failure / SWR-immaturity substrate diagnosis (not a theory failure).
- **Runner activity since the 2026-05-13T01:10Z nightly:** central `evidence/experiments/runner_status.json` reports 681 -> **718 cumulative completions (+37)**; all-time breakdown 134 -> **163 PASS** / 271 -> **285 FAIL** / 76 -> **77 ERROR** / **193 UNKNOWN** (unchanged); last_updated 2026-05-17T01:11:14Z.
- **Queue depth:** 0 -> **0 items (empty `items: []`)**. The 2026-05-15/16 substrate + governance waves drained the queue; the active goal_pipeline:GAP-3 SD-012 sustained-drive EMA session (TASK_CLAIMS gap3-sustained-drive-ema-20260517T004727Z) holds the next substrate slot.
- **Pending review:** 0 -> **0 items** (pending_review.md regenerated 2026-05-16T20:52:59Z; last review 2026-05-16T18:22:30Z). The 2026-05-15T18:55Z governance cycle walked 5 indexed + 1 runner-only (EXQ-563/563a/563b/565 + 564 cleared; supersession cleanup applied 563->563a->563b), applied 9 hold_pending_v3_substrate (ARC-066/067/068, ARC-070/071, MECH-320, Q-043/044/045), confirmed 0 indexed pending; substrate_queue.json timestamp updated (48 ready, 32 blocked, 38 implemented).
- **Bottleneck note (shift):** the **ARC-065 behavioural-diversity developmental warm-start failure** is now the dominant scientific blocker, superseding the pure V_s-monostrategy framing. V3-EXQ-573's bit-for-bit-identical 10-arm 5-10x bias-scale sweep diagnosed the MECH-314a / MECH-320 diversity biases as literally zero at cold start (not miscalibrated -- MECH-313 temperature is irrelevant on near-uniform random-network scores). The right response is a developmental warm-start curriculum (DEV-NEED-029 ARC-065 warm-start gate, PROPOSED), not more bias-scale sweeps. `docs/architecture/developmental_experiment_priorities.md` (created 2026-05-16) synthesises 7 lit-pull topics + the FAIL/PASS pattern + DEV-NEED register and ranks 10 experiments: **EXQ-ISEF-001 (harm-gradient curriculum) is Rank 1, gating everything downstream**. Q-043/044/045 and INV-049 retests must be deferred until the warm-start gate is established via EXQ-ISEF-001..006.

### Immediate Work Queue (This Cycle, 2026-05-17)

1. **goal_pipeline:GAP-3 SD-012 sustained-drive EMA** -- active session (TASK_CLAIMS gap3-sustained-drive-ema-20260517T004727Z): Option-1 sustained-drive EMA in goal.py + config.py + discriminative alpha-sweep EXQ via /queue-experiment + contract test. Plan-of-record goal_pipeline_plan.md GAP-3.
2. **EXQ-ISEF-001 harm-gradient curriculum (Rank 1)** -- the developmental-experiment-priorities gate. Establishes the warm-start curriculum that DEV-NEED-029 requires before MECH-314a / MECH-320 diversity biases are non-zero at cold start. Gates EXQ-ISEF-002..006 and the deferred Q-043/044/045 + INV-049 retests.
3. **V3-EXQ-577a outcome watch** -- infant_substrate GAP-2 corrected-C2 microhabitat validation (the 577 C2 false-negative redraw guard + corrected acceptance per the failure autopsy).
4. **V3-EXQ-581 full-runner watch** -- sleep_substrate GAP-3 unified-master-flag end-to-end validation (dry-run 6/6 PASS; runner DLAPTOP-4.local auto-claimed).
5. **Governance walk** -- next governance / morning-digest session should re-confirm 0 pending and absorb the calibration-debt sprint results (EXQ-569/570/571 + EXQ-573 NULL) into the ARC-065 / MECH-313/314/320 evidence_quality_notes if not already done.

---

## Status Snapshot (2026-05-13T01:10Z -- nightly docs sync; MECH-307 default-value recalibration landed (`min_drive_to_fire` 0.1 -> 0.01 + `conjunction_z_beta_threshold` 0.6 -> 0.3) after V3-EXQ-540d read-site probe PASS diagnosed substrate-ceiling drive-floor / z_beta-ceiling pattern; V3-EXQ-540e MECH-307 default-fix validation queued and dry-run PASS with first non-zero `conj_fire_rate=0.155`; V3-EXQ-461 EXP-0157 delayed-reward persistence PASS closes commitment_closure_plan.md GAP-2 at substrate-readiness level; V_s-monostrategy diagnostic cohort queued (V3-EXQ-555/556/557/558 agent-init basin localisation + V3-EXQ-554a decoder/elite-refit localization); runner_remote_control `_rrc` NameError fix landed; pending_review 0 -> 11 stale-index)

- **SDs / MECHs / substrate fixes landed since the 2026-05-12T01:10Z nightly:**
  - **MECH-307 default-value recalibration** 2026-05-12 -- two bridge config defaults lowered after V3-EXQ-540d (re-queue of V3-EXQ-540c killed by the 2026-05-12T06:10Z systemctl restart) confirmed at 10x scale (1087 bridge calls / 34784 candidate-reads) that the V3-EXQ-540a / 540b conj_fire_rate=0 cohort was caused by two config defaults sitting above the achievable substrate ceiling under standard env config. `mech295_min_drive_to_fire` 0.1 -> 0.01 (drive_level max=0.030 / mean=0.016 / frac>0.1=0.000 across 1087 reads -- legacy floor never crossed); `mech307_conjunction_z_beta_threshold` 0.6 -> 0.3 (z_beta_arousal max=0.545 / mean=0.518 -- legacy floor above achievable ceiling). Half-tier predicate components (0.3 / 0.15 / 0.3) clear 94.66% of candidates if both gates allowed it through -- substrate writes populate read sites cleanly. Changes landed across 4+3 declaration sites (bridge dataclass + REEConfig dataclass + REEConfig.from_dims kwarg + REEAgent getattr fallback). Two contract test assertions updated to match new defaults (`test_mech_295_liking_bridge.py` default check + `test_mech307_consumer_conjunction.py` default check + the C4 low-z_beta-blocks scenario uses `z_beta_arousal=0.1` instead of 0.4 to remain below the new 0.3 default). 314/314 contracts + 7/7 preflight PASS with new defaults. Backward compat: callers that explicitly set either flag are unaffected. Deferred follow-on (separate session): Option-b semantic fix at `mech295_liking_bridge.py:343` (currently reads `v[:, 3]` legacy unsigned-magnitude rather than `v[:, 4]` VALENCE_POSITIVE_SURPRISE under Option-b semantics; design-doc fidelity bug, not a behavioural blocker).
  - **V3-EXQ-461 EXP-0157 delayed-reward persistence substrate-readiness PASS** 2026-05-12T18:18Z on DLAPTOP-4.local closing commitment_closure_plan.md GAP-2 at substrate-readiness level (full behavioural delayed-reward arm remains blocked on GAP-3 CausalGridWorldV2 env extensions). Evidence supports MECH-090 + SD-033a + SD-034 at substrate-readiness level: baseline Hold delay suppression / release, weakened passthrough contrast, SD-033a / MECH-261 replay-gated persistence, strengthened Hold threshold, sd_033a mode-gate table, and SD-034 terminal closure release.
  - **runner_remote_control _rrc NameError fix landed** 2026-05-12T06:14Z (ree-v3 commit b46c89c). Hoisted `runner_remote_control` import to module top-level so the `_push_remote_heartbeat` closure inside `experiment_runner.run_experiment` resolves `_rrc` via module globals rather than the `main()` local scope (closure ran on a heartbeat thread called from a module-level function, raising `NameError: name '_rrc' is not defined` every tick on both Hetzner cloud workers). Likely introduced by commit ccaabee (heartbeat carries progress + recent_lines for remote progress bars). ree-cloud-1 (91.98.130.117) + ree-cloud-2 (116.203.216.181) systemd services restarted clean via SSH; preflight 7/7 PASS on each; both runners back to idle main-loop polling with no NameError post-restart.
- **Strategic note:** the 2026-05-12 wave is dominated by **two convergent investigations on the V_s-monostrategy substrate ceiling**. (a) MECH-307 consumer-conjunction-read recovery: V3-EXQ-540b threshold sweep FAIL -> V3-EXQ-540d read-site probe PASS diagnoses substrate-ceiling drive-floor + z_beta-ceiling -> default-value recalibration -> V3-EXQ-540e behavioural validation queued (PASS expected; would clear goal_pipeline:GAP-1). (b) V_s monostrategy basin geometry localisation in agent-init space: V3-EXQ-552 forced-exploration warmup discovered that seed=7 sustains action_class_entropy~0.68 while seeds 42 / 17 collapse to 0.0 at identical code; V3-EXQ-555 2x2 (env_seed, agent_seed) factorisation queued + smoke-PASSed factorisation invariants; V3-EXQ-557 30-cell agent-seed sweep queued; V3-EXQ-556 8-arm module-init swap diagnostic queued (per-submodule seeded init monkey-patch -- though smoke surfaced a replication-failure pattern at the smoke-depth boot loop, prompting V3-EXQ-558 clean seed-pair readout/rank diagnostic without the monkey-patch); V3-EXQ-554a decoder + elite-refit collapse localization re-queued after the 06:10Z restart. The two threads share the same monostrategy floor and inform one another -- if 540e PASSes, the consumer-side blocker is downstream of (and possibly independent of) the seed-anomaly basin.
- **Runner activity since the 2026-05-12T01:10Z nightly:** central `evidence/experiments/runner_status.json` reports 674 -> **681 cumulative completions (+7)**. All-time breakdown: 136 -> **134 PASS (-2)** / 270 -> **271 FAIL (+1)** / 75 -> **76 ERROR (+1)** / 193 -> **193 UNKNOWN (+0)**. V3 subset 652 runs (125 PASS / 258 FAIL / 76 ERROR / 193 UNKNOWN). The negative PASS delta is reconciliation indexing (some prior PASS entries reclassified per evidence_direction_per_claim review; manifest content unchanged). New entries since last nightly: V3-EXQ-540c (ERROR, SIGTERM at restart), V3-EXQ-540d (PASS, MECH-307 read-site probe), V3-EXQ-461 (PASS, EXP-0157 delayed-reward persistence). The other ~4 entries are indexer-side surfacing of earlier completions newly included after the post-2026-05-11 governance walk.
- **Queue depth:** 1 -> **0 items (empty `items: []`)**. Yesterday's V3-EXQ-540b (MECH-307 consumer-conjunction threshold sweep) completed FAIL; today's wave (V3-EXQ-554a / 555 / 556 / 557 / 558 monostrategy diagnostics + V3-EXQ-540e MECH-307 default-fix validation) were all pre-claimed by runners before the nightly read so the central queue file is empty at this snapshot. substrate_queue.json unchanged from yesterday (the day's substrate landing was the MECH-307 default-value recalibration, which is a config tweak rather than a new substrate so does not surface a new entry).
- **Pending review:** 0 -> **11 items** (1 PASS / 6 FAIL / 4 runner-only). The pending_review.md regenerated 2026-05-12T18:15Z surfaced V3-EXQ-549 / 550 / 543d / 540a / 540b / 540e FAILs plus V3-EXQ-540c MECH-307 readsite probe PASS (which is the manifest the V3-EXQ-540d re-queue produced -- same script name, runner output bookkeeping displays the queue_id but the indexer reads the script's output_file). Runner-only stale-index items: V3-EXQ-552 (FAIL), V3-EXQ-555 (PASS), V3-EXQ-557 (PASS), V3-EXQ-540c (ERROR). All eleven are governance-walk eligible but accumulated because no governance walk has fired today; the next morning-digest / governance run will drain them.
- **Plan-of-record progressions (2026-05-12):** commitment_closure_plan.md GAP-2 status `open -> done` at substrate-readiness level (V3-EXQ-461 EXP-0157 PASS); full behavioural arm is gated on GAP-3 CausalGridWorldV2 env extensions. goal_pipeline_plan.md GAP-1 v3_pending behavioural-validation gate is still v3_pending pending V3-EXQ-540e outcome (PASS clears it; the 2026-05-11 GAP-1 status `open -> done` covered the substrate landing not the behavioural validation).
- **Bottleneck note:** the **V_s-monostrategy substrate ceiling** continues to be the dominant scientific bottleneck. Three concurrent threads share that floor (V_s basin geometry localisation via V3-EXQ-555 / 556 / 557 / 558; MECH-307 consumer-side recalibration via V3-EXQ-540e; ARC-062 Phase 3 wiring via V3-EXQ-543d). The V_s basin geometry thread is now the load-bearing diagnostic -- if a single submodule's seed-7 init is sufficient to escape monostrategy (R1 result on V3-EXQ-556), that localises the substrate-ceiling cause to one specific weight initialisation distribution; if it's conjunctive (R2), every submodule's init contributes; if it's no individual module (R3-R5), the agent-side seed effect is more diffuse than per-module init differences alone explain.

### Immediate Work Queue (This Cycle, 2026-05-13)

1. **V3-EXQ-540e outcome watch** -- MECH-307 default-fix behavioural validation queued on DLAPTOP-4.local. Dry-run smoke at 6 ep / 1 seed produced ARM_2_full `conj_fire_rate=0.155` (first non-zero conjunction firing since substrate landed). PASS routes to clearing goal_pipeline:GAP-1 v3_pending behavioural-validation gate and unblocking GAP-2 SD-049 Phase 2 V3-EXQ-514 behavioural validation. FAIL routes to a structural read-site audit + the deferred Option-b semantic fix at `mech295_liking_bridge.py:343` (`v[:, 3]` -> `v[:, 4]`).
2. **V3-EXQ-555 outcome watch** -- 2x2 (env_seed, agent_seed) factorisation diagnostic localising whether the V3-EXQ-552 seed-7 entropy anomaly is env-side, agent-side, conjunctive, or either-sufficient. Pre-registered 5-row interpretation grid (R1 env_side_only / R2 agent_side_only / R3 conjunctive / R4 either_sufficient / R5 replication_failure).
3. **V3-EXQ-557 outcome watch** -- 30-cell agent-seed sweep at fixed env_seed=42 bounding the size of the monostrategy basin in agent-init space. Builds on V3-EXQ-555 by characterising how many agent-init seeds escape (R1 deep_collapse_basin >= 80% collapsed; R2 bimodal; R3 mostly_diverse; R4 continuous_spread).
4. **V3-EXQ-556 + V3-EXQ-558 outcome watch** -- 8-arm module-init swap (V3-EXQ-556 via class-level `__init__` monkey-patch with per-module seed override; smoke surfaced a replication-failure pattern that V3-EXQ-558 routes around by reusing the V3-EXQ-555 factored-seed helper for a clean seed-pair readout/rank diagnostic instead). Pre-registered 6-row grid: R1 single_module_sufficient / R2 multi_module_conjunctive / R3 latent_stack_only / R4 e3_only / R5 hippocampal_only / R6 replication_failure.
5. **V3-EXQ-554a outcome watch** -- decoder + elite-refit collapse localization (5 measurement points M0-M4 inside `HippocampalModule.propose_trajectories` via experiment-side monkey-patch). Pre-registered 5-row interpretation grid: R1 decoder_collapse / R2 elite_refit_collapse / R3 noise_shape_irrelevant / R4 e2_rollout_collapse / R5 other.
6. **Governance walk for the 11 pending_review items** -- next morning-digest / governance session should drain V3-EXQ-549 / 550 / 543d / 540a / 540b / 540e FAILs plus V3-EXQ-540c read-site probe PASS plus the four stale-index runner-only items (552 / 555 / 557 / 540c). Re-run `python scripts/generate_pending_review.py` to confirm 0 pending after the walk.

---

## Status Snapshot (2026-05-12T01:10Z -- nightly docs sync; MECH-307 Option-b Gap-1 substrate landing closes goal_pipeline:GAP-1; SD-054 bipartite layout extension; MECH-323 + MECH-324 ARC-071 child claims registered; governance cycle applied 16 hold_pending_v3_substrate decisions and reclassified the V_s monostrategy cohort; self_attribution_plan GAP-1 inverted to monostrategy substrate-ceiling; V3-EXQ-550 z_goal monostrategy falsifier FAIL at no-training depth; V3-EXQ-551/551a pipeline-entropy diagnostic localised entropy=0.0 cliff to CEM proposer; pending_review 0 -> 0)

- **SDs / MECHs landed / claims registered since the 2026-05-11T01:10Z nightly:**
  - **MECH-307 Option-b Gap-1 substrate landing** 2026-05-11. Per user override 2026-05-11 (option-b over the design-doc default option-a), the SD-014 valence vector is extended from 4 to 6 components with new constants VALENCE_POSITIVE_SURPRISE=4 and VALENCE_NEGATIVE_SURPRISE=5; MECH-205 PE write site dispatches between three paths (Option-b split / Option-a signed-single-channel / legacy unsigned magnitude) routing surprise by concurrent harm_signal sign while ALSO writing magnitude to legacy VALENCE_SURPRISE for backward-compat. New convenience master `use_mech307_conjunction` (default False) flips all three substrate-side sub-flags (use_mech307_split_surprise + use_mech307_schema_multichannel + use_mech307_predicted_location_write) via REEConfig.__post_init__. 309/309 contracts + 7/7 preflight PASS with master OFF. Field-level smoke verified: split-channel writes accumulate correctly under MECH-094 simulation gate. SD-014 6-channel amendment retained as registered fallback. **Closes goal_pipeline_plan.md GAP-1**; GAP-2 (SD-049 Phase 2 behavioural validation under MECH-307-fixed substrate) unblocked.
  - **SD-054 bipartite layout extension** 2026-05-11. Three new `CausalGridWorldV2.__init__` kwargs (`reef_bipartite_layout`, `reef_bipartite_axis`, `reef_bipartite_agent_band_radius`) that partition reef and food cells into disjoint geometric halves with the agent spawning in a midline band. Forces reef-bound vs forage-bound trajectories to have categorically opposite first-action argmaxes by construction -- targets the CEM-candidate distinguishability bottleneck surfaced by V3-EXQ-543b diagnose-errors. V3-EXQ-548 substrate-readiness PASS 2026-05-11 confirmed 1.27x structural divergence uplift (0.633 -> 0.807); legacy mode bit-identical OFF.
  - **MECH-323 + MECH-324 ARC-071 child claims registered** 2026-05-11. MECH-323 `policy.composition.chunk_accumulator_formation` (striatum/DLS-analog formation operator -- joint AND trigger over repetition count + outcome-variance + evaluative gate with V_s-positive secondary preference; Sutton 1999 options-framework structure; MECH-094-strict default + MECH-322 sleep-replay carve-out). MECH-324 `policy.composition.chunk_maintenance_dissolution` (IL/vmPFC-analog maintenance operator -- four-state lifecycle FORMING / CRYSTALLISED / DISSOLVING / DISSOLVED with crystallisation counter + outcome-variance dissolution gate + replay-origin accelerated-dissolution per MECH-322). ARC-071 substrate now FULLY SPECIFIED at the claim level (formation + maintenance + sleep-replay carve-out); substrate-level implementation in ree_core deferred to a separate /implement-substrate session; first three-arm validation EXQ deferred until substrate landed. claim count 618 -> 619 -> 620.
- **Strategic note:** the 2026-05-11 wave is dominated by the **V_s monostrategy substrate-ceiling** thread. Three concurrent diagnostic / falsifier sessions converged on the same underlying issue: (a) V3-EXQ-550 z_goal monostrategy falsifier FAIL at no-training depth (action_class_entropy=0.0 in BOTH arms; z_goal pipeline wired-but-inert with z_goal_update_calls=1200 + z_goal_norm_peak=0.0 across all ARM_ON seeds); (b) self_attribution_plan GAP-1 forensic read inverted from arbitration-data to substrate-ceiling (V3-EXQ-445/445b produced floating-point-identical metrics across architectural arms -- bit-identical signature of trajectory determinism under V_s monostrategy); (c) V3-EXQ-551 + V3-EXQ-551a pipeline-entropy diagnostic PASS localised the entropy=0.0 cliff to the CEM proposer stage. V3-EXQ-553 orthogonal CEM seeding is the substrate-side fix under test; V3-EXQ-552 forced-exploration warmup is the parallel training-data-narrowness vs substrate-collapse falsifier. The MECH-307 conjunction architecture lands its Gap-1 substrate the same day, but V3-EXQ-540a's C2 consumer-conjunction-read FAIL signals the consumer-side thresholds need recalibration (V3-EXQ-540b 4-arm sweep queued and claimed by Mac). ARC-062 Phase 3 wiring continues to be the architectural side gate (V3-EXQ-543c FAIL on probe-gate; V3-EXQ-543d 2x2 factorial of {gated_policy x dACC} with MECH-260 anti-recency at 0.5 queued).
- **Runner activity since the 2026-05-11T01:10Z nightly:** central `evidence/experiments/runner_status.json` reports 665 -> **674 cumulative completions (+9)**. All-time breakdown: 136 PASS (+5) / 270 FAIL (+4) / 75 ERROR (+0) / 193 UNKNOWN (-2). V3 subset 639 runs (116 PASS / 257 FAIL / 73 ERROR / 193 UNKNOWN). PASS deltas (+5): V3-EXQ-548 SD-054 bipartite substrate-readiness, V3-EXQ-551 + V3-EXQ-551a pipeline-entropy diagnostic, V3-EXQ-547 MECH-320 tonic vigor substrate-readiness (carried over from the 2026-05-10 wave indexer-side surfacing). FAIL deltas (+4): V3-EXQ-550 z_goal monostrategy falsifier, V3-EXQ-543c ARC-062 Phase 3 falsifier, V3-EXQ-540a MECH-307 3-arm gap decomposition, V3-EXQ-141c MECH-111 novelty-drive RNG-desync indexer-side surfacing.
- **Queue depth:** 0 -> **1 item** at this nightly read. V3-EXQ-540b (MECH-307 consumer-conjunction threshold sweep, claimed by DLAPTOP-4.local 2026-05-12T01:07Z; 4 arms varying the wanting / liking / z_beta consumer thresholds with substrate fully ON in every arm). Concurrent runs not yet in the queue at this read (queue-then-claim races): V3-EXQ-543d (ARC-062 Phase 3 2x2 factorial), V3-EXQ-549 (ARC-066 / MECH-320 discriminative pair), V3-EXQ-552 (forced-exploration warmup), V3-EXQ-553 (orthogonal CEM seeding).
- **Pending review:** 0 -> **0 items**. The 2026-05-11T20:10Z `review-exq550-543c` session walked V3-EXQ-550 + V3-EXQ-543c FAILs; both reclassified per pre-registered grids without claim weighting changes (V3-EXQ-550 evidence_direction_per_claim FAIL supports MECH-269 V_s monomodal hold at no-training depth; V3-EXQ-543c non_contributory ARC-062 Phase 3 wiring inert under the SD-054 bipartite substrate before V3-EXQ-543d redesign). Earlier in the day, the 2026-05-11T17:13Z governance cycle walked 3 indexed pending + 5 unclaimed + 2 runner-only pending experiments and applied 16 `hold_pending_v3_substrate` recommendations covering 5 ARC (ARC-066/067/068/070/071) + 3 Q (Q-043/044/045) + 8 section-level duplicates.
- **Plan-of-record progressions (2026-05-11):** goal_pipeline_plan.md GAP-1 status `open -> done` via MECH-307 Option-b substrate landing; self_attribution_plan.md GAP-1 status `open -> blocked` (monostrategy substrate-ceiling, same blocker as GAP-2); arc_062_rule_apprehension_plan.md GAP-B resume_condition recorded V3-EXQ-543c FAIL diagnosis (probe-gate + ARC-062 architectural-isolation); SD-049-PHASE-3 SD-032 consumer cascade migration remains deferred per goal_pipeline_plan.md GAP-5; substrate_queue.json grew with the new entries reflecting today's substrate landings + cluster registrations.
- **Renderer / tooling improvement:** closure tab in serve.py / closure.html now distinguishes resolved-lineage edges from active blockers (faded dotted rendering when `depends_on` predecessor is `done` or `deferred*`; tooltip surfaces `blocked on` / `resume when` rows above phase/severity; resume_condition free-text passthrough). CLOSURE_VERSION bumped 2026-05-09.3 -> 2026-05-11.1.
- **Bottleneck note:** the **V_s-monostrategy substrate ceiling** is now the dominant scientific bottleneck across at least four open-claim threads (SD-029 self-attribution; SD-032b dACC arbitration; ARC-062 rule apprehension; MECH-307 consumer-conjunction read). V3-EXQ-553 orthogonal CEM seeding is the immediate substrate-side test (proposer-stage entropy cliff). Underneath that, the **ARC-070 / ARC-071 R6 SAFETY-CRITICAL governance decision** on MECH-094 hypothesis_tag strict-vs-relaxed gating for the chunking write path now has BOTH substrate slots specified (MECH-323 formation + MECH-324 maintenance) -- the governance call is the gate before any implement-substrate session.

### Immediate Work Queue (This Cycle, 2026-05-12)

1. **V3-EXQ-540b outcome watch** -- MECH-307 consumer-conjunction threshold sweep currently running on DLAPTOP-4.local. PASS routes to a 540c behavioural retest at the chosen threshold; PARTIAL C1-PASS-C2-FAIL routes to a structural read-side audit (suspect: kernel-decay reading nearby zeros, RBF center drift, or write/read site z_world mismatch).
2. **V3-EXQ-553 orthogonal CEM seeding outcome watch** -- proposer-stage substrate-side test of the V_s monostrategy cliff localised by V3-EXQ-551/551a. PASS clears the proposer-as-cliff-variable reading; FAIL routes to downstream stage 2/3 review.
3. **V3-EXQ-552 forced-exploration warmup outcome watch** -- parallel training-data-narrowness vs substrate-collapse falsifier on the V3-EXQ-550 monostrategy finding.
4. **V3-EXQ-543d outcome watch** -- ARC-062 Phase 3 wiring 2x2 factorial of {gated_policy x dACC} with MECH-260 anti-recency=0.5. PASS = cluster wiring is the missing piece (both substrates contribute).
5. **ARC-070 / ARC-071 R6 SAFETY-CRITICAL governance decision** -- dedicated session for the MECH-094 hypothesis_tag strict-vs-relaxed call for chunking writes; both MECH-323 + MECH-324 substrate slots now registered, the governance verdict gates any /implement-substrate session.
6. **MECH-323 / MECH-324 substrate implementation** -- after the R6 verdict lands, the ree_core substrate work for the formation + maintenance operators is the next architectural pass.

---

## Status Snapshot (2026-05-11T11:35Z -- scheduled PM /lit-pull + /update-docs; Q-045 lit-pull adds 5 entries / lit_conf 0.9 / evidence_quadrant plausible_unproven; R1 verdict COUPLED-NOT-COLLAPSED extends Q-045 resolution categories; MECH-260 anchor flagged missing in arc_065 Pull 1 RECOVERED via Scholl 2015; no SD / MECH status changes)

- **Literature additions since the 2026-05-11T01:10Z nightly snapshot:**
  - **Q-045 dedicated lit-pull** -- 5 entries landed in `evidence/literature/targeted_review_q_045/` covering the LC-NE tonic noise (MECH-313) vs dACC anti-recency (MECH-260) substrate-independence question. Tervo et al. 2014 (Cell, [DOI 10.1016/j.cell.2014.08.037](https://doi.org/10.1016/j.cell.2014.08.037)) R1 LOAD-BEARING: LC-NE input drives ACC stochastic-mode switching with ACC engagement SUPPRESSED during stochastic mode -- the two substrates are coupled at the circuit level, neither fully independent nor fully collapsed. Scholl et al. 2015 (J Neurosci, [DOI 10.1523/JNEUROSCI.0396-15.2015](https://doi.org/10.1523/JNEUROSCI.0396-15.2015)) R2 substrate-distinctness CONFIRMED + recovers MECH-260 anchor flagged missing in arc_065 Pull 1 synthesis 2026-05-10. Kennerley et al. 2006 (Nat Neurosci, [DOI 10.1038/nn1724](https://doi.org/10.1038/nn1724)) causal lesion complement. Meder et al. 2017 (Nat Commun, [DOI 10.1038/s41467-017-02169-w](https://doi.org/10.1038/s41467-017-02169-w)) multi-timescale value spectrum reinforces substrate-distinctness from a third angle. Yu & Dayan 2005 (Neuron, [DOI 10.1016/j.neuron.2005.04.026](https://doi.org/10.1016/j.neuron.2005.04.026)) theoretical anchor.
- **Verdicts and design refinements:**
  - **R1 COUPLED-NOT-COLLAPSED** (mixed-direction evidence from Tervo 2014) -- MECH-313 and MECH-260 substrate-distinct AND circuit-coupled; resolution categories EXTENDED to include "DIRECTIONALLY COUPLED" as a fourth category alongside the three originally registered (mutually load-bearing / 313-dominant / 260-dominant).
  - **R4 LOAD-BEARING design refinement** -- current Q-045 4-arm ablation is INSUFFICIENT to expose the Tervo asymmetry; needs extension to 8-cell (4-arm x 2-LC-amplitude) OR addition of LC -> ACC coupling ablation. both-ON should NOT be linear superposition of singletons.
  - **R5 substrate-readiness precondition** -- SD-054 reef substrate temporal-horizon must be verified BEFORE 4-arm authorisation; Kennerley-style across-trial integration only emerges with sufficient temporal horizon and a single-tick outcome substrate cannot dissociate MECH-260 from MECH-313 in the Kennerley sense.
- **Indexer delta:** literature entries 1326 -> **1331** (+5); claim_evidence.v1.json Q-045 entry: literature_confidence 0.0 -> **0.9**, overall_confidence 0.0 -> 0.9, evidence_quadrant `plausible_unproven`, direction_counts 4 supports + 1 mixed.
- **Hygiene win:** recovers the MECH-260 Scholl 2015 anchor that the ARC-065 Pull 1 synthesis flagged as un-retrievable 2026-05-10 (citation-lookup ambiguity resolved by author + journal + year combination via PubMed author-field search).
- **Governance impact:** Q-045 evidence_quality_note extended in claims.yaml with R1-R5 verdicts + reference to `targeted_review_q_045/synthesis.md`. NO claim status changes (Q-045 remains `open`; MECH-313 remains `candidate_substrate_landed`; MECH-260 remains `substrate_landed`). validate_claims --strict OK 68 invariants; build_claims_json wrote 618 claims.
- **Bottleneck note (unchanged from 2026-05-11T01:10Z):** ARC-062 Phase 3 wiring pass + ARC-064/ARC-065/ARC-066 child-MECH cluster behavioural validation remain the immediate gate. Q-045 4-arm ablation is now better-scaffolded but still gated on the Phase 3 redesign + the SD-054 substrate-readiness precondition R5 surfaces.

### Immediate Work Queue (This Cycle, 2026-05-11 -- PM addendum to nightly)

1. **Carry-forward from nightly:** all 6 items unchanged (ARC-062 Phase 3 wiring redesign + Q-043/044/045 behavioural ablation cohort design + ARC-070/071 R6 SAFETY-CRITICAL governance + MECH-321 substrate + ARC-067/068 child-MECH design + V3-EXQ-141c diagnose-errors).
2. **Q-045 design extension follow-on** -- before queueing the Q-045 4-arm ablation, decide whether to extend it to the 8-cell (4-arm x 2-LC-amplitude) form per R4 verdict OR add a dedicated LC -> ACC coupling ablation arm. Sequence the SD-054 multi-trial-outcome-dependency substrate-readiness diagnostic (R5 precondition) BEFORE the 4-arm authorisation.

---

## Status Snapshot (2026-05-11T01:10Z -- nightly docs sync; four ARC-064/ARC-065/ARC-066 child substrates land (MECH-313 noise floor + MECH-314 structured curiosity + MECH-319 simulation-mode rule-write gate + MECH-320 tonic vigor coupling); two new architectural cluster registrations (ARC-066/067/068 non_deficit_action_drives + ARC-069/070/071 policy_primitive_granularity); MECH-163 depends_on +ARC-071 per ARC-071 lit-pull R3 verdict; ARC-062 Phase 3 falsifier V3-EXQ-543b FAIL on Mac; pending_review 2 -> 0; runner_status.json single-file deprecated -- per-machine aggregate now reported)

- **SDs / MECHs moved to Implemented since the 2026-05-10T01:10Z nightly snapshot:**
  - **MECH-313 (ARC-065 child) stochastic noise floor (LC-NE tonic / SAC analog)** IMPLEMENTED 2026-05-10. Module `ree_core/policy/noise_floor.py` (NoiseFloor + NoiseFloorConfig). Pure-arithmetic regulator (no learned parameters); sibling to MECH-314 / MECH-318 / MECH-319 in the ree_core.policy package. Single primitive `noise_floor.compute_effective_temperature(baseline_temperature, simulation_mode)` returns `max(baseline_T + noise_floor_alpha, noise_floor_min_temperature)` -- SAC-entropy-bonus analog (Haarnoja 2018) on E3 softmax temperature. State-independent; complement to MECH-104 phasic spike. Distinct from MECH-260 dACC anti-recency (state-dependent); Q-045 falsifies whether they collapse. Phase-1 instantiation choice = SEPARATE module at the e3.select() call site (revisit at Q-045 4-arm ablation). MECH-094: simulation_mode=True returns baseline temperature unchanged + increments skip counter only. V3-EXQ-544 substrate-readiness 5/5 PASS UC1-UC5 smoke (manifest PASS; runner outcome flag ERROR per the substrate-readiness false-ERROR stdout sentinel pattern, fixed mid-day via the diagnose-errors session that landed `verdict:` print across 542/544/545). 11 contract tests in tests/contracts/test_mech_313_noise_floor.py PASS.
  - **MECH-314 (ARC-065 child) structured curiosity bonus + 3 sub-flavours (314a/b/c)** IMPLEMENTED 2026-05-10. Module `ree_core/policy/structured_curiosity.py` (StructuredCuriosity + StructuredCuriosityConfig). Pure-arithmetic, no learned parameters; sibling to MECH-313 NoiseFloor. Three sub-flavours implemented as a single module with master + 3 independently-togglable sub-switches per Pull 1 R3 verdict: 314a striatal novelty (per-candidate min-distance from candidate's first-step z_world to nearest active ResidueField RBF center, normalised by candidate-pool mean norm); 314b frontopolar uncertainty (e3._running_variance scalar, broadcast across [K] in Phase 1); 314c learning progress (EMA of `|PE_t - PE_{t-K}|`, broadcast scalar in Phase 1). Composed AFTER MECH-295 liking-bridge block and BEFORE MECH-313 noise_floor temperature lift (orthogonal axes). Phase 1 honest-scoping caveat: 314b/c are state-dependent broadcast scalars; per-candidate refinement deferred to Phase 2 follow-on. Q-044's three-arm ablation IS a flag-set decision -- the substrate guarantees each sub-flavour can be turned on/off independently. MECH-094: simulation_mode=True returns zeros[K] + increments skip counter only. V3-EXQ-545 substrate-readiness 5/5 PASS UC1-UC5 (ran twice on Mac + cloud-2 via multi-machine race). 13 contract tests in tests/contracts/test_mech_314_curiosity.py PASS; 273/273 contracts + 7/7 preflight PASS with master OFF.
  - **MECH-319 (arc_062 GAP-K) simulation-mode rule-write gate** IMPLEMENTED 2026-05-10. Module `ree_core/regulators/simulation_mode_rule_gate.py` (SimulationModeRuleGate + SimulationModeRuleGateConfig + SimulationModeRuleGateDiagnostics). Substrate-level instantiation of MECH-094 at the rule-arbitration layer per Pull 3 SYNTHESIS R1 GENUINE-NOVELTY-CONFIRMED + Pull 4 R3 KEEP-AS-IS verdicts. Pure-arithmetic regulator (sibling to GABAergicDecayRegulator and BroadcastOverrideRegulator). Single primitive `gate.effective_simulation_mode(simulation_mode, site) -> bool` with truth-table semantics: master OFF identity passthrough; master ON + admit_writes=False blocks sim writes (MECH-319 normal); master ON + admit_writes=True (V3-EXQ-543c-successor falsifier control) admits sim writes. Two existing arbitration-write call sites in REEAgent.select_action() consult the gate when instantiated: GatedPolicy block (replace literal simulation_mode=False with gate.effective_simulation_mode call) + LateralPFCAnalog block (skip update() when blocked, compute_bias still runs). Per-site diagnostic counters on {gated_policy, lateral_pfc, default}. Construction raises ValueError on admit_writes=True without master ON (loud-not-silent guard). MECH-094 NOT modified per KEEP-AS-IS verdict. V3-EXQ-546 substrate-readiness 6/6 PASS UC1-UC5 + UC3b precondition (ran twice on Mac + cloud-2 via multi-machine race); 15 contract tests in tests/contracts/test_mech_319_simulation_mode_rule_gate.py PASS; 288/288 contract + preflight tests PASS with master OFF. claims.yaml MECH-319 candidate -> candidate_substrate_landed; v3_pending: true retained pending V3-EXQ-543c-successor falsifier with admit_writes=True. arc_062 GAP-K closed (registered -> substrate_landed).
  - **MECH-320 (ARC-066 child) tonic vigor coupling score bias (mesolimbic-DA-vigor analog)** IMPLEMENTED 2026-05-10. Module `ree_core/policy/tonic_vigor.py` (TonicVigor + TonicVigorConfig + TonicVigorOutput). First child mechanism for ARC-066 (the non_deficit_action_drives architectural family). Pure-arithmetic regulator (sister to MECH-313 NoiseFloor + MECH-314 StructuredCuriosity in ree_core.policy). Composed AFTER MECH-314 curiosity (orthogonal axis at the candidate-feature level) and BEFORE MECH-313 noise_floor (orthogonal regulator at the temperature level). Algorithm: `v_t = max(0, slow EWMA over realised E3 score) * gate_energy * gate_drive * gate_pe`; `bias[i] = -w_action*v_t` on action classes / `+w_passive*v_t` on noop class (additive primary; multiplicative gain falsifiable secondary via tonic_vigor_form="multiplicative" -- distinguishable on a held-out non-uniform-|score| batch). TARGET-FREE: bias applies regardless of whether any z_goal is currently active -- closes the "well-fed-safe-familiar agent has no positive gradient to act" gap that ARC-066 registered. Defaults: half_life=100 (long-window per R4 verdict), w_action=w_passive=0.1, bias_scale=0.1, gate_energy_min=0.2, gate_drive_max=0.7, gate_pe_max=1.0, noop_class=0. MECH-094: simulation_mode=True on either compute_score_bias or update_score_receipt returns zeros + increments skip counter only. V3-EXQ-547 substrate-readiness 6/6 PASS UC1-UC6 on cloud-2 2026-05-10T20:56Z; 28 contract tests in tests/contracts/test_mech_320_tonic_vigor.py PASS; 309/309 contracts + 7/7 preflight PASS with master OFF. claims.yaml MECH-320 candidate -> candidate_substrate_landed.
  - **ARC-066 / ARC-067 / ARC-068 cluster registration (non_deficit_action_drives family)** 2026-05-10. Three architectural-slot claims registered as the family principle that behaviour comes from surplus capacity AND from deficits, not deficits alone: ARC-066 tonic_vigor_coupling (capacity -> action bias); ARC-067 idle_aversion_boredom (sustained low-engagement is aversive); ARC-068 opportunity_cost_no_op_penalty (waiting carries cost). Three companion lit-pulls landed: ARC-066 lit_conf 0.789 supports (LC-NE substrate REJECTED, mesolimbic DA-vigor LOAD-BEARING per Niv 2007 + Salamone & Correa 2012 + Beierholm 2013); ARC-067 lit_conf 0.85 supports; ARC-068 lit_conf 0.806 supports-direction-dominant (R1 SEPARATE-AT-ARCHITECTURE-VIA-KERNEL not via substrate; R3 ARC-066 + ARC-068 collapse LICENSED at implementation layer per Niv 2007 mathematical symmetry but slot-level separation preserved for psychiatric failure-mode dissociation). Anchored in `docs/architecture/non_deficit_action_drives.md`. MECH-320 (ARC-066 first child) substrate landed same day; ARC-067 / ARC-068 child-MECH design pending.
  - **ARC-069 / ARC-070 / ARC-071 cluster registration (policy_primitive_granularity family)** 2026-05-10. Three architectural-slot claims registered as the family principle that the unit of policy operated on is itself dynamic (not fixed): ARC-069 parent (policy_hierarchy_dynamic_regranularisation); ARC-070 decomposition-on-prediction-failure (zoom in / re-segment when an imagined chunk fails to ground); ARC-071 composition-via-repeated-grounding (zoom out / chunking). Two companion lit-pulls landed: ARC-070 lit_conf 0.88 supports (R2 LOAD-BEARING SHARED SUBSTRATE -- ARC-070 implemented as bidirectional extension of MECH-288 event_segmenter, NOT a new module; Schacter 2008 constructive-episodic-simulation core network supplies empirical anchor); ARC-071 lit_conf 0.848 supports (R3 LOAD-BEARING -- CONFIRMED ARC-071 IS the missing transition mechanism in MECH-163 dual_goal_directed_systems, MECH-163 depends_on extended +ARC-071 the same day; R6 SAFETY-CRITICAL escalation -- biology does NOT cleanly gate chunking write path against replay/imagined sequences per Albouy 2013, ARC-071's pre-registered MECH-094 hypothesis_tag=False strict-gating MORE CONSERVATIVE than biology, governance decision pending). Anchored in `docs/architecture/policy_primitive_granularity.md`. MECH-321 (ARC-070 first child mechanism, policy.decomposition_via_event_segmenter) registered candidate / v3_pending the same day with depends_on ARC-070 + MECH-288 + MECH-269 + MECH-094.
- **Strategic note:** today landed four child substrates in three distinct architectural clusters (ARC-064 GAP-K MECH-319 + ARC-065 MECH-313/314 + ARC-066 MECH-320), plus two new architectural-slot cluster registrations (ARC-066/067/068 non_deficit_action_drives + ARC-069/070/071 policy_primitive_granularity), plus MECH-321 as ARC-070 first child. The substrate-readiness diagnostics for all four child substrates passed today; behavioural validation of the ARC-066 + ARC-065 cohorts (Q-043 / Q-044 / Q-045 cross-cohort ablation) is the next-up scientific work and will exercise the V3-EXQ-543c-successor admit_writes=True falsifier substrate. ARC-062 Phase 3 wiring (gated_policy bias-head into E3 optimizer + discriminator -> SD-033a `LateralPFCAnalog.update()` source vector) was attempted in V3-EXQ-543b on Mac (~4h, FAIL); commitment_closure_plan.md GAP-1 remains blocked pending Phase 3 design refinement.
- **Runner activity since the 2026-05-10T01:10Z nightly:** the 665 figure cited at the prior nightly was a single-machine read (Mac local). The single-file `runner_status.json` no longer exists -- per the multi-machine coordination policy each machine writes to `evidence/experiments/runner_status/<hostname>.json`. Per-machine aggregate as of 2026-05-11T01:10Z: 555 DLAPTOP-4.local + 28 Daniel-PC + 77 EWIN-PC + 222 ree-cloud-1 + 163 ree-cloud-2 = **1045 cumulative**. Cumulative cross-machine breakdown: 241 PASS / 463 FAIL / 105 ERROR / 236 UNKNOWN. **+10 cumulative-by-machine completions today** (deduped: 8 unique experiments because V3-EXQ-545 + V3-EXQ-546 each ran twice via the multi-machine claim race): V3-EXQ-543b (ARC-062 Phase 3 falsifier on Mac, FAIL ~4h); V3-EXQ-544 (MECH-313 noise floor) substrate-readiness "false ERROR" with manifest PASS; V3-EXQ-545 (MECH-314 structured curiosity) PASS x2 on Mac + cloud-2; V3-EXQ-546 (MECH-319 simulation-mode rule-write gate) PASS x2 on Mac + cloud-2; V3-EXQ-547 (MECH-320 tonic vigor coupling) PASS on cloud-2; V3-EXQ-514h + V3-EXQ-514i (SD-049 Phase 2 behavioural successors) PASS on cloud-1; V3-EXQ-141c (MECH-111 novelty-drive RNG-desync) FAIL on cloud-2.
- **Queue depth:** 0 -> **0 items (empty `items: []`)** at this nightly read; today's queue churn (V3-EXQ-543b + 544/545/546/547 + 514h/i + 141c) all completed during the day. substrate_queue.json grew 69 -> 78 entries with the new ARC-064 / ARC-065 / MECH-313 / MECH-314 / MECH-316 / MECH-317 / MECH-318 / MECH-319 / SD-054 entries reflecting today's substrate landings + cluster registrations. ARC-062 entry status updated `candidate_v3_pending -> phase_1_implemented`.
- **Pending review:** 2 -> **0 items**. The 2026-05-10T12:24Z governance cycle walked the 3 PASS pending experiments (V3-EXQ-500a SD-017 readiness probe + V3-EXQ-543 ARC-062 Phase 2 falsifier already-non_contributory + V3-EXQ-503a SD-017 sleep discriminative pair) and applied 13 pending_user recommendations via decision_log.v1.jsonl appends (10 hold_pending_v3_substrate on ARC-062, ARC-064, ARC-065, MECH-309, MECH-312, MECH-313, MECH-316, MECH-317, MECH-318, SD-054 newly registered v3_pending claims; 3 hold_candidate_resolve_conflict on ARC-045, MECH-166, MECH-204). The 2026-05-10T12:18Z diagnose-errors session also added the four held ERRORs (V3-EXQ-538 / 495 / 449c / 455a) to discussed_experiment_dirs with explicit rationale.
- **Plan-of-record progressions (2026-05-10):** arc_062_rule_apprehension_plan.md GAP-K closed (MECH-319 substrate landed); GAP-I MECH-318 absorption check VERDICT B partial (no new V3 substrate; empirical retire-vs-promote deferred to V3-EXQ-543c-successor on multi-rule-context substrate); 14 lit entries added across two ARC-066/067/068 lit-pulls + two ARC-070/071 lit-pulls + one ARC-068 lit-pull = ~30 lit entries lifting cluster lit_conf 0.0 -> 0.8+ across all 6 newly registered architectural-slot claims. 2 new umbrella architecture docs (`non_deficit_action_drives.md` + `policy_primitive_granularity.md`).
- **Bottleneck note:** the **ARC-062 Phase 3 wiring pass + ARC-064/ARC-065/ARC-066 child-MECH cluster behavioural validation** is the immediate gate. Phase 3 wiring was attempted in V3-EXQ-543b on Mac (~4h, FAIL); design needs refinement before another attempt; commitment_closure_plan.md GAP-1 remains blocked. The four ARC-064/ARC-065/ARC-066 child substrates all landed substrate-readiness PASS today; the next move is the Q-043 / Q-044 / Q-045 cross-cohort behavioural ablation. Underneath those, the **ARC-070/071 R6 SAFETY-CRITICAL governance decision** (MECH-094 hypothesis_tag strict-vs-relaxed for chunking write path, escalated by the ARC-071 lit-pull synthesis) and the **non_deficit_action_drives + policy_primitive_granularity child-MECH design cycles** are the architectural-side gates that flow from today's two cluster registrations. The monostrategy / reef-recovery thread continues to be the underlying scientific bottleneck pending ARC-062 Phase 3 + the rule-apprehension cluster's behavioural validation cohort.

### Immediate Work Queue (This Cycle, 2026-05-11)

1. **ARC-062 Phase 3 wiring redesign** -- V3-EXQ-543b FAILed at ~4h; design needs refinement before another attempt. Closes commitment_closure_plan.md GAP-1.
2. **Q-043 / Q-044 / Q-045 behavioural ablation cohort design** -- now that all four ARC-064/ARC-065/ARC-066 child substrates have landed (MECH-313 / MECH-314 / MECH-319 / MECH-320), queue the cross-cohort relative-weight calibration (Q-043) + sub-flavour independence (Q-044) + MECH-313 vs MECH-260 collapse falsifier (Q-045) on the V3-EXQ-543c-successor admit_writes=True falsifier substrate.
3. **ARC-070/071 R6 SAFETY-CRITICAL governance decision** -- dedicated session for the MECH-094 hypothesis_tag strict-vs-relaxed decision for the chunking write path. Touches MECH-094 / ARC-071 / MECH-292/293 / sleep_substrate / SD-039. ARC-071 child-MECH design is gated on this verdict.
4. **MECH-321 substrate work** -- after MECH-288 event_segmenter.py input_stream label extension lands, MECH-321 (ARC-070 first child mechanism) substrate is a thin policy-side BoundaryEvent consumer per the ARC-070 R2 bidirectional-substrate verdict.
5. **ARC-067 / ARC-068 child-MECH design** -- cycle through the same design-doc + lit-pull-driven cycle as ARC-066 / MECH-320 used today.
6. **V3-EXQ-141c diagnose-errors** -- pending_review=0 at nightly close but the 141c FAIL on cloud-2 is the immediate /diagnose-errors candidate per the bit-identical-arms measurement-validity pattern; it shares the V3-EXQ-141d governance-deferred status but landed on a different machine.

---

## Status Snapshot (2026-05-10T01:10Z -- nightly docs sync; ARC-062 Phase 1 lands gated-policy heads + context discriminator; Phase 2 GAP-B monomodal-collapse falsifier PASS; MECH-204 step-size sweep cohort PASS; sleep_substrate GAP-2 Tier-1 cohort 3 PASS + 2 FAIL drains the queue; pending_review 1 -> 2)

- **SDs / MECHs moved to Implemented since the 2026-05-09T01:10Z nightly snapshot:**
  - **ARC-062 Phase 1 (gated-policy heads + context discriminator)** IMPLEMENTED 2026-05-09 -- `arc_062_rule_apprehension_plan.md` GAP-A. New `ree_core/policy/gated_policy.py` (GatedPolicy + GatedPolicyConfig + GatedPolicyOutput): N=2 scoring heads sharing E3 candidate features (symmetry-broken init on heads' last-Linear bias) + 3-stream context discriminator on (z_world, z_self, z_harm_a) per Pull A SYNTHESIS R1 (multi-stream input) at score_bias level per R3; n_heads=2 substrate-constrained per R2 (raises ValueError otherwise). disc_init_scale=0.1 keeps sigmoid output near 0.5 at init; bias clamped to [-bias_scale, +bias_scale]. NO connection to SD-033a in Phase 1 -- that wiring is Phase 3 (closes commitment_closure_plan.md GAP-1). REEAgent.select_action composes gated_policy_score_bias additively into dacc_score_bias before the MECH-295 block. MECH-094 simulation_mode=True returns zeros and increments only the skip counter. 5 contract tests `tests/contracts/test_gated_policy.py` (C1-C5); full ree-v3 suite 249/249 PASS. Substrate-readiness V3-EXQ-542 5/5 manifest PASS UC1-UC5 on Mac 2026-05-09T20:22Z (runner outcome flag ERROR with manifest verdict PASS per the substrate-readiness pattern).
  - **ARC-062 Phase 2 GAP-B (monomodal-collapse falsifier on SD-054 reef)** PASS 2026-05-09 -- V3-EXQ-543 on Mac in ~50min: ARM_0 use_gated_policy=False vs ARM_1c use_gated_policy=True with full 3-stream discriminator at ARM_1_med density (hazard_food_attraction=0.7, n_reef_patches=3, reef_patch_radius=2, n_hazards=4, size=12). PASS rule >=2 of {C2 state-dependence (Spearman binned drive-vs-reef abs >= 0.20 AND ARM_1c |rho| > ARM_0 |rho|), C3 risk-type dissociation (forage_hazard_rate / transit_hazard_rate >= 0.50 relative magnitude), C4 cross-seed variation (CoV(reef_visit_fraction) >= 0.10)} with no F1 (total invariance / monomodal-collapse signature) or F2 (biologically inverted: rho > +0.40 monotone refuge-use under chronic high-drive). Phase 3 wiring pass (discriminator -> SD-033a `LateralPFCAnalog.update()` source vector + adds bias-head parameters to E3 optimiser) is the next-up consumer; closes commitment_closure_plan.md GAP-1.
  - **MECH-204 step-size sweep cohort** PASS 2026-05-09 -- V3-EXQ-541a / 541b / 541c on DLAPTOP-4.local / Mac. Companion EXP-0171 step-size sweep gated on V3-EXQ-541 PASS surfaced as a 3-arm cohort step values {0.05 / 0.10 / 0.25 / 0.50}; 541c PASS at 16-cycles (the wider-cycle dose-response sweep) with ARM_4 step=0.5 clearing the C4 5% threshold at 9.03% and ARM_3 step=0.25 at 4.51% (high-end defensible; supported the default bump from 0.1 -> 0.25 in the 2026-05-09T13:36Z sleep-substrate-phase1-closure session).
  - **Sleep_substrate_plan.md GAP-2 Tier-1 successor cohort** completed 2026-05-09 -- 5 EXQs queued in series (265a, 500a, 503a, 436a, 418l) with the validated Phase 2 substrate template (sd016_writepath_mode='off', sd016_diversification_weight=0.5, use_per_stream_vs=True, use_anchor_sets=True, use_sd039_anchor_payload=True). Outcomes: V3-EXQ-265a PASS 20:12Z (sleep-on signed |diff| > 0.05 in >=2/3 seeds across SWS / SWS_THEN_REM contrasts), V3-EXQ-500a PASS 20:41Z (single-arm SD-017 sleep-phase readiness probe), V3-EXQ-503a PASS 21:46Z (FULL_4_PHASE_ON vs NO_SLEEP_BASELINE discriminative pair with C4 cross-arm |M2 diff| > 0.20 calibrated from --dry-run smoke), V3-EXQ-436a FAIL 21:52Z (3 conditions x 5 seeds multi-claim ['SD-017', 'ARC-045', 'MECH-166'] with per-seed distribution diagnostics; failure routes to /diagnose-errors per-seed-distribution-grid not substrate retraction), V3-EXQ-418l FAIL 21:53Z (SD-016 action_bias_div retest single-claim ['SD-017']; failure routes to /diagnose-errors). 4 of 5 successors clear; sleep_substrate_plan.md GAP-2 row update happens after governance walks the failures.
- **Strategic note:** the 2026-05-09 wave drained the queue completely. The empty queue is the natural inflection point for governance to walk the cohort and dispatch GAP-2 row update + ARC-062 Phase 3 wiring + the two FAIL diagnostic root-cause cycles before any new behavioural EXQs are queued.
- **Runner activity since the 2026-05-09T01:10Z nightly:** 654 -> **665 completions (+11)**. Cumulative breakdown 124 -> **131 PASS** / 263 -> **266 FAIL** / 72 -> **73 ERROR** / 195 -> **195 UNKNOWN**. PASS deltas (+7): V3-EXQ-541a/541b/541c MECH-204 step-size cohort, V3-EXQ-265a sleep-on signed-diff PASS, V3-EXQ-500a SD-017 readiness probe PASS, V3-EXQ-503a discriminative pair PASS, V3-EXQ-543 ARC-062 Phase 2 falsifier PASS. FAIL deltas (+3): V3-EXQ-436a multi-claim sleep cohort, V3-EXQ-418l SD-016 action_bias_div retest, plus one carryover FAIL surfaced in the indexer. ERROR delta (+1): V3-EXQ-542 (manifest verdict PASS but runner outcome ERROR per substrate-readiness pattern).
- **Queue depth:** 1 -> **0 items (empty `items: []`)**. V3-EXQ-540 (MECH-307 3-arm gap decomposition, queued 2026-05-08, claimed by Mac 2026-05-09T00:00Z) is no longer in the queue at this read -- presumed run earlier in the 2026-05-09 wave; verify against runner_status. Next-up substrate work in `evidence/planning/substrate_queue.json` remains SD-049 Phase 2 z_resource encoder follow-on (ready=True priority=2) and the ARC-062 Phase 3 wiring pass that closes commitment_closure_plan.md GAP-1 (now unblocked by the V3-EXQ-543 Phase 2 PASS).
- **Pending review:** 1 -> **2 items**. V3-EXQ-530c (ARC-016 precision-commit StepHarness retest, carry-over from 2026-05-08T22:34Z governance, deferred to /diagnose-errors per the bit-identical-arms measurement-validity pattern) plus V3-EXQ-141d (MECH-111 novelty-drive RNG-desync, also FAIL deferred to /diagnose-errors). Both are deferred not awaiting a governance walk.
- **Plan-of-record progressions (2026-05-09):** sleep_substrate_plan.md Phase 1 closure landed (GAP-1 status open -> done; default `rem_precision_recalibration_step` bumped 0.1 -> 0.25 in REEConfig backed by V3-EXQ-541c PASS; Phase 7 reframed deferred-conditional -> deferred-to-V4-unless-future-evidence-reverses); Phase 2 (SD-017 retest cohort) Tier-0 status correction `blocked` -> `open` (EXQ-418e A2_div_only had cleared slot_diversity 0.5 threshold cleanly back on 2026-04-27); arc_062_rule_apprehension_plan.md registered as a sibling plan-of-record + GAP-A done + GAP-B queued; commitment_closure_plan.md GAP-1 reframed `open` -> `blocked` on arc_062_rule_apprehension:GAP-A/B; substrate_queue.json ARC-062 entry added at queue tail (priority 2, ready=true); SD-033 governance plan-doc bookkeeping closure (CHK-PUSH open -> done; closure-graph 87.5% -> 100%); 14 lit entries added across two ARC-062 lit-pulls (8 entries on lateral PFC rule-context modulation + 6 entries on refugia-vs-forage behavioural ecology) lifting cluster lit_conf 0.0 -> 0.890 across MECH-309 / ARC-062 / ARC-063 with SD-054 picking up 6 direct-tagged entries.
- **Bottleneck note:** the **ARC-062 cluster (MECH-309 / ARC-062 / ARC-063 / SD-054 rule-apprehension cluster registered 2026-05-08)** is now the governance-side gate. Phase 3 wiring (discriminator -> SD-033a + bias-head into E3 optimiser) is the architectural next step; commitment_closure GAP-1 unblock cascades through it. Underneath, the **monostrategy / reef-recovery thread** is no longer the dominant scientific bottleneck -- the rule-apprehension cluster has displaced it as the load-bearing diagnostic for whether REE V3 needs a non-Bayesian rule-creator architectural slot or whether the V3 weak reading (gated-policy heads) is sufficient. The two FAILs in the sleep_substrate GAP-2 Tier-1 cohort (V3-EXQ-436a / 418l) are the only items on the governance-walk side that need /diagnose-errors per-seed-distribution diagnostics before the GAP-2 row can flip done.

### Immediate Work Queue (This Cycle, 2026-05-10)

1. **Sleep_substrate_plan.md GAP-2 row update** -- 4 of 5 Tier-1 successors PASS (265a / 500a / 503a + the prior 265a anchor); the row can flip `in-progress` -> `done` once the 436a / 418l FAILs are walked through /diagnose-errors and either superseded or accepted as-tagged.
2. **ARC-062 Phase 3 wiring pass** -- discriminator output threaded into SD-033a `LateralPFCAnalog.update()` source vector + adds gated_policy bias-head parameters to E3 optimiser. Closes commitment_closure_plan.md GAP-1. Phase 2 PASS (V3-EXQ-543) clears the gate.
3. **V3-EXQ-530c + V3-EXQ-141d /diagnose-errors** -- two pending_review FAILs both deferred to root-cause diagnosis under the bit-identical-arms measurement-validity pattern.
4. **V3-EXQ-540 MECH-307 outcome** -- if the run completed during the 2026-05-09 wave, governance walks the C1/C2/C3 acceptance grid + ARM_3 SD-014 6-channel fallback decision. If runner_status shows it surfaced UNKNOWN, the manifest needs review per the substrate-readiness pattern.
5. **Next-substrate decision** -- with the queue empty and SD-049 Phase 2 follow-on + ARC-062 Phase 3 + V3-EXQ-495 V3-full-completion-gate all eligible, governance picks the load-bearing next move.

---

## Status Snapshot (2026-05-09T01:10Z -- nightly docs sync; sleep-substrate Phase 1 lands MECH-204 recalibration consumer; MECH-307 conjunction architecture in V3-EXQ-540 3-arm gap decomposition; governance cycle applies MECH-307 hold + Q-040 narrow-open with three sub-questions; pending_review 0 -> 1)

- **SDs / MECHs moved to Implemented since the 2026-05-08T01:11Z nightly snapshot:**
  - **MECH-204 sleep substrate Phase 1** IMPLEMENTED 2026-05-08 -- `sleep_substrate_plan.md` GAP-1. SerotoninModule.compute_recalibration_target() exposes the captured precision_at_rem_entry zero-point reference; E3TrajectorySelector.recalibrate_precision_to(target, step) applies Option A linear interpolation `new_rv = (1-step)*rv + step*(1.0/(target+1e-6))`; WRITEBACK-phase sibling step in SleepLoopManager._run_cycle runs independently of MECH-273 self-model gradient. New REEConfig fields use_rem_precision_recalibration (default False; bit-identical OFF) + rem_precision_recalibration_step (default 0.1 per plan-of-record Q1). Contract suite test_mech204_precision_recalibration.py 9/9 PASS covering C1 surface, C2 default-OFF, C3 sleep_loop-ON / recalibration-OFF no-metrics, C4 arithmetic, C5/C6 zero-target / zero-step no-op, C7 capture-only regression guard, C8 WRITEBACK firing end-to-end, C9 drift movement. Full preflight + contracts 237/237 PASS. V3-EXQ-541 validation ran 2026-05-08T23:43Z with runner-level FAIL outcome and result_summary "verdict: PASS" -- governance walk reconciliation pending.
  - **MECH-307 anticipatory affect conjunction architecture (consumer side)** IMPLEMENTED 2026-05-08 -- MECH295LikingBridge.compute_conjunction_score_bias() reads SD-014 valence + z_beta arousal at per-candidate predicted-imminent locations and applies a negative approach bias when the four-way conjunction holds. New REEConfig flag use_mech307_consumer_conjunction_read (default False; bit-identical OFF). Wired into REEAgent.select_action() additively with the legacy m295_bias. test_mech307_consumer_conjunction.py 8/8 PASS; full contract suite 221/221 + 7/7 preflight PASS.
  - **Rule-apprehension cluster registration** 2026-05-08 -- MECH-309 (monomodal-collapse-as-equilibrium-without-rule-apprehender, mechanism_hypothesis candidate); ARC-062 (V3 weak reading, implementation_phase=v3, v3_pending=true); ARC-063 (V4 strong reading, implementation_phase=v4); SD-054 reef enrichment substrate (renamed from SD-050 to disambiguate; v3_pending flipped to true). docs/thoughts/2026-05-04_Waking_rule_apprehension_later_sleep_schema.md promoted to docs/architecture/rule_apprehension_layer.md as canonical anchor. EXP-0171 three-arm discriminative proposal queued.
  - **Plan-of-record registration wave (2026-05-08)** -- four new evidence/planning/*_plan.md docs registered as resume primitives across multi-session work: sleep_substrate_plan.md (8-gap inventory + 7-phase sequencing for SD-017 / MECH-204 / sleep cluster), commitment_closure_plan.md (10-gap inventory + 8-phase sequencing for SD-034 / MECH-090/091 / MECH-260 / MECH-266/267/268 / SD-033a/b cluster, with sd033_governance_plan.md retained as OCD-specific test-battery sub-plan), self_attribution_plan.md (5-gap inventory + 5-phase sequencing for SD-029 / MECH-256 / MECH-257 / SD-013 / ARC-033 / ARC-058 / MECH-258 / MECH-260 + V4 SD-030/SD-031), goal_pipeline_plan.md (6-gap inventory + 6-phase sequencing for SD-012 + SD-014 + SD-015 + SD-018 + SD-049 + MECH-216 + MECH-229/230 + MECH-117/295/307 + ARC-030/032/036/051). Substrate_queue back-fills: MECH-267 + MECH-268 + SD-018 (queue 61 -> 68 entries).
- **Strategic shift (2026-05-08):** sleep substrate flagged as the top-priority unblocker. Per user direction, "we may not make progress elsewhere until progress is made there." Sleep_substrate_plan.md Phase 1 now landed; Phase 2 (SD-017 retest cohort gated on EXQ-418e SD-016 div-loss A2/A3 arms) and Phase 7 (deferred-conditional MECH-204 Option B broadcast read at action-selection time) remain ahead. The plan converges with goal_pipeline_plan at the SD-049 sleep-on cohort boundary (V3-EXQ-514 family with use_sleep_loop / sws_enabled / rem_enabled flags).
- **Runner activity since the 2026-05-08T01:11Z nightly:** 631 -> **654 completions (+23)**. Cumulative breakdown 120 -> **124 PASS** / 255 -> **263 FAIL** / 72 -> **72 ERROR** / 184 -> **195 UNKNOWN**. Notable PASS: V3-EXQ-244a stale-ERROR -> PASS reconciliation (manifest at runs/v3_exq_244a.../manifest.json was already PASS / supports MECH-165; runner SIGTERM'd on ree-cloud-2 after writing manifest but before bookkeeping success); V3-EXQ-514g StepHarness wider-seed sweep PASS on ree-cloud-1; V3-EXQ-106a SD-011 harm_obs_a temporal persistence re-validation PASS (3.2s on ree-cloud-1). Notable FAIL: V3-EXQ-539 MECH-307 4-arm substrate-readiness (substrate counters PASS but C5 behavioural FAIL -- legacy MECH-295 cue path does not read the conjunction signal; led to V3-EXQ-540 3-arm gap decomposition with consumer-conjunction-read ON in all arms); V3-EXQ-541 MECH-204 Phase 1 validation (FAIL outcome flag; in-script verdict PASS -- governance walk reconciliation pending); V3-EXQ-526 Q-034 reef threshold sweep; V3-EXQ-454a ARC-016 adaptive commitment under reef.
- **Queue depth:** 7 -> **1 item**. Only V3-EXQ-540 (MECH-307 3-arm gap decomposition + Path B consumer conjunction read; ARM_0_off / ARM_1_signed_pe / ARM_2_full; priority=5; machine_affinity=DLAPTOP-4.local; 70 episodes x 3 seeds x 3 conditions; estimated 90 min) is currently queued, claimed by Mac at 2026-05-09T00:00:27Z. ARM_3 SD-014 6-channel fallback DEFERRED.
- **Pending review:** 0 -> **1 item**. The 2026-05-08T22:34Z governance cycle walked 10 indexed pending FAILs (4 superseded predecessors EXQ-537/537b/537c/141c flipped to superseded; 3 already-triaged accepted as-tagged; 530c held for /diagnose-errors per bit-identical-arms measurement-validity pattern; 537d + 539 accepted as-tagged). 9 run_ids added to reviewed_run_ids. The 2026-05-08T22:38Z pending_review.md regeneration shows V3-EXQ-530c as the only remaining pending item.
- **Governance decisions applied 2026-05-08T22:34Z (2 pending_user resolved):**
  - **MECH-307** hold_pending_v3_substrate decision logged; v3_pending=true; V3-EXQ-540 is the queued discriminative validation. evidence_quality_note appended to MECH-307 in claims.yaml capturing the EXQ-539 read + consumer-conjunction-read landing + EXQ-540 queued chain.
  - **Q-040** narrow_open_question applied -- decomposed into Q-040.a (factorial 2x2 of {MECH-269b OFF/ON} x {SD-032b OFF/ON} on EXQ-483a retest, load-bearing arbitration), Q-040.b (alternative-hypothesis isolator: MECH-295 liking-stream wiring? cross-witness EXQ-536b force-arm probe), Q-040.c (mechanism quantification: dACC weight delta proportional to |precision-weighted forward-PE|? EXQ-475a-conditions retest). Empirical resolution gated on StepHarness migration + MECH-307 substrate landing + MECH-269b V_s-rollout-gate.
- **Manifest reclassifications (2026-05-08):** 4 flips (537/537b/537c/141c -> superseded) with evidence_direction_per_claim mapped to superseded for each tagged claim, evidence_direction_note appended documenting the lettered successor (537d for the 537 chain, 141d for 141c). 11 manifests in the prior `fix-update-z-goal-bug` cohort patched with [update_z_goal_typeerror_swallowed] note (4 superseded, 7 trace-only); evidence_quality_note added to 8 affected claims (Q-040, MECH-269b, MECH-295, SD-037, MECH-280, MECH-281, SD-036, MECH-279).
- **Substrate fixes (2026-05-08):** ree-v3/runner_remote_control.py active-claim guard broadened from `evidence/experiments/` substring to `evidence/` substring after a 2026-05-08T~18:25Z silent autostash revert of an evidence/planning/substrate_queue.json edit (matching the 2026-04-29 EXQ-232 evidence/experiments/ incident signature). Contract test_active_claim_evidence_guard.py 8/8 PASS. ree-v3/experiment_runner.py REE_QUEUE_ID + REE_RUNNER_SIGNAL_DIR env-leak fix: child subprocess no longer inherits stale parent shell env when queue_id is falsy or signal_dir is None; 6-test contract test_runner_env_isolation.py PASS.
- **Bottleneck note:** the **sleep-substrate Phase 1 validation + MECH-307 conjunction-architecture cluster** is the immediate gate. V3-EXQ-541 outcome reconciliation (FAIL flag with verdict PASS) is the first governance task; whether step=0.1 default is calibrated correctly for the C1/C2/C3 acceptance grid or whether EXP-0171 step-size sweep needs to fire ahead of the C5 behavioural arm. V3-EXQ-540 outcome (in flight on Mac) decides whether the four-gap conjunction architecture is the right fix or whether the SD-014 6-channel fallback (ARM_3, deferred) becomes the natural follow-on. Underneath those, the **monostrategy / reef-recovery thread** remains the dominant scientific bottleneck, now reframed by the rule-apprehension cluster registration (MECH-309 / ARC-062 / ARC-063) -- whether the missing primitive is a V3 gated-policy architectural slot or a V4 distributed CandidateRule field with tolerance gate.

### Immediate Work Queue (This Cycle, 2026-05-09)

1. **V3-EXQ-540 outcome watch** (MECH-307 3-arm gap decomposition, Mac, ~90 min). C1 substrate-readiness counter dissociation, C2 conjunction-fire rate >= 0.10 in ARM_2 only, C3 approach_commit_rate ARM_2 >= ARM_0 + 0.10 in 2/3 seeds AND ARM_2 > ARM_1. Outcome dispatches whether four-gap conjunction architecture is the right fix or whether SD-014 6-channel fallback (ARM_3) becomes the natural follow-on.
2. **V3-EXQ-541 MECH-204 Phase 1 governance walk reconciliation** -- runner-level FAIL outcome with manifest result_summary "verdict: PASS" needs reconciliation. Step=0.1 calibration check; potential EXP-0171 step-size sweep gate before the C5 behavioural arm.
3. **V3-EXQ-530c /diagnose-errors** (single pending_review item; bit-identical-arms measurement-validity pattern, deferred from 2026-05-08 governance cycle for diagnostic root-cause).
4. **Plan-of-record Phase progression** -- sleep_substrate_plan Phase 2 (SD-017 retest cohort gated on EXQ-418e SD-016 div-loss A2/A3 arms producing slot_diversity >= 0.5), commitment_closure_plan Phase 1 (SD-033a bias-head training), self_attribution_plan Phase 1 (V3-EXQ-445h forensic read; not gated on substrate work), goal_pipeline_plan Phase 1 (already in progress via MECH-307 / V3-EXQ-540).
5. **Rule-apprehension cluster activation** -- EXP-0171 three-arm discriminative proposal (ARM_0 baseline / ARM_1 reef-only / ARM_2 reef + gated-policy stub) gated on V3-EXQ-540 outcome.
6. **StepHarness audit** of governance write paths (shared concern across sleep_substrate_plan GAP-6 and commitment_closure_plan GAP-10 -- combine when either reaches its respective phase).

---

## Status Snapshot (2026-05-08T01:11Z -- nightly docs sync, quiet runner day; bug-fix retest cohort kicked off; MECH-295 goal-seeding diagnostic queued; pending_review back to 0; Q-041 registered)

- **No new SD / MECH structural landings since the 2026-05-07T01:12Z nightly snapshot.** The 2026-05-07/08 sessions were governance / triage / bug-fix-retest construction, not architectural substrate work. Two concrete substrates landed in the experimental tooling: `ree-v3/experiments/_harness.py` StepHarness (canonical sense / update_z_goal / update_residue sequence; kwargs-only call shape; no bare-except wrappers) + `ree-v3/experiments/_metrics.py` canonical extractors (extract_dacc_score_bias reads the actual [K] tensor passed to E3.select, not the raw bundle slice) -- both fix the 2026-05-07T23:30Z `fix-update-z-goal-bug` cohort's update_z_goal positional/kwarg TypeError + bare-except silent-swallow class. 189/189 contract tests PASS post-fix.
- **Queue depth:** 0 -> **7 items** (3 claimed + 4 pending). The 2026-05-07T20:35Z `bugfix-requeue-433f-483b-476c-490f-445h-514f-523b` session wrote and queued seven lettered-iteration corrected scripts fixing two ree_core bugs (Bug 1 BreathOscillator disabled, Bug 2 `_committed_step_idx` saturation in non-bistable path; 476c also required an agent.act() -> sense()/select_action() API migration). Three are now claimed and running -- V3-EXQ-433f (SD-029 reef comparator on ree-cloud-1), V3-EXQ-483b (SD-037 broadcast override 4-arm on ree-cloud-2), V3-EXQ-514f (SD-049 Phase 2 reef behavioural validation on DLAPTOP-4.local). V3-EXQ-523b (SD-029 reef-unblocked comparator) is pending. Two MECH-295 goal-seeding follow-ons from the `goal-seeding-diagnostic-followup-2026-05-07T2255Z` session are pending: V3-EXQ-536a (per-step instrumentation dispatching H_a drive-collapse-on-contact / H_b threshold never crossed / H_c update fires but z_goal does not grow) and V3-EXQ-536b (z_goal_inject force-arm via MECH-188 hook isolating upstream-vs-downstream blocker). V3-EXQ-537 (SD-029/MECH-256 single-pass residual replacing the V3-EXQ-535a two-pass cf_gap) is pending after the 2026-05-08T00:15Z multi-sense audit reclassified V3-EXQ-535a non_contributory for both SD-029 and MECH-256.
- **Runner activity since the 2026-05-07T01:12Z nightly:** 628 -> **631 completions (+3)**. Cumulative breakdown 120 -> **120 PASS** / 255 -> **255 FAIL** / 72 -> **72 ERROR** / 181 -> **184 UNKNOWN**. The three new completions are V3-EXQ-535a (SD-029 P3 eval-fix attempt; reclassified non_contributory in the multi-sense audit -- script computes two-pass cf_gap not the single-pass residual the spec requires), the V3-EXQ-530b ARC-016 precision-commit rename-rerun (renamed from V3-EXQ-530 to bypass the runner_status.json completed-record skip after the original SIGTERM ERROR; runner claimed it on DLAPTOP-4.local within 21 seconds), and the V3-EXQ-433f / V3-EXQ-483b queue claims that flowed through but are still in flight at this nightly read. All three surface as UNKNOWN result codes pending the next governance walk.
- **Pending review:** 32 -> **0 items**. The active governance cycle (claim governance-2026-05-06T2156Z, opened 2026-05-06T21:56Z) finished walking the 32-item accumulation overnight (status: done per WORKSPACE_STATE.md Recent Work and the 2026-05-08T00:43Z pending_review regeneration showing 0 items). The 2026-05-07T23:00Z `rv-pinned-cluster-review` session walked the EXQ-514d/514e/524/530/536 substrate-bug cluster (root cause: experiments call select_action() but never agent.update_residue(), so post_action_update() / running_variance update never fires; precision pinned at 1/0.5; current_precision=1.999996 constant). The 2026-05-08T00:15Z `triage-7-weighting-multi-sense` audit cleared 7 weighting scripts after the multi-sense bug uncovered: SUPERSEDED EXQ-124 (env.reset mid-episode + double-sense weakening MECH-033), EXQ-143 (eval-time double-sense asymmetric across hopfield ON/OFF arms weakening MECH-118), EXQ-490f (cohort bug); trace-noted (direction kept) EXQ-108 / EXQ-375 / EXQ-047i/j/k -- evidence_quality_note added to MECH-033, MECH-118, MECH-135, MECH-073, MECH-095, SD-005. 983 runs indexed.
- **Q-041 registered (2026-05-07T22:25Z):** `register-threshold-supervisor` session formalised the unified meta-level threshold supervisor research direction (default-toward-Q approach: scattered adaptive loci ARC-016 / SD-032c/d/e / MECH-040 / MECH-204 inventoried; supervisor SD/MECH cluster deferred until evidence directs); `docs/architecture/threshold_supervisor_survey.md` written with timescale-spread table from per-step EMA (~10 steps) up to pACC drive_bias (~347-step half-life) plus three architectural gaps (cross-substrate volatility tracking, MECH-204 sleep-writeback absent, joint setpoint drift); EXP-0170 added to manual_proposals.v1.json as low-priority exploratory_probe testing cross-substrate threshold coherence under sustained drive_level=0.9 vs 0.5 baseline (PCA-based primary analysis, gated on V_s-monostrategy substrate clearing). claims 580 -> 581, proposals 266 -> 267, 68 invariants validated.
- **Bottleneck note:** the **bug-fix retest cohort + MECH-295 goal-seeding diagnostic** is the immediate gate. Whether the BreathOscillator + saturating-step-idx fix recovers behavioural acceptance under SD-029 / SD-037 / SD-049 Phase 2 will be answered by V3-EXQ-433f / 483b / 514f as they land. Underneath that, the EXQ-536 z_goal_active_fraction=0.0 finding ("goal seeding is upstream-blocked OR commit chain is inert even with seeded z_goal") is the load-bearing diagnostic queued ahead -- V3-EXQ-536a / 536b will dispatch root cause for the MECH-295 wired-but-inert pattern that survived V3-EXQ-490c + V3-EXQ-490e FAILs. The monostrategy / reef-recovery thread (whether reef substrate alone is sufficient under SD-029 / SD-032b / SD-032c / Q-034 / MECH-112 / ARC-016 / MECH-257 / SD-049 Phase 2 or whether downstream calibration is required) remains the dominant underlying scientific bottleneck.

### Immediate Work Queue (This Cycle, 2026-05-08)

1. **Bug-fix retest cohort runtime watch** -- V3-EXQ-433f (SD-029 reef comparator, ree-cloud-1, ~250 min), V3-EXQ-483b (SD-037 broadcast override 4-arm, ree-cloud-2, ~250 min), V3-EXQ-514f (SD-049 Phase 2 reef behavioural validation, DLAPTOP-4.local, ~100 min) running concurrently. Outcome dispatches whether the BreathOscillator + saturating-step-idx fix is the recovery lever for the monostrategy-blocked predecessors.
2. **V3-EXQ-536a / 536b MECH-295 goal-seeding diagnostic** -- whichever runner picks these up first dispatches root cause for the EXQ-536 z_goal_active_fraction=0.0 finding (H_a drive-collapse on contact, H_b benefit threshold never crossed, H_c update fires but z_goal does not grow; vs upstream seeding versus downstream commit chain).
3. **V3-EXQ-537 SD-029/MECH-256 single-pass residual** -- supersedes V3-EXQ-535a. Replaces the two-pass cf_gap with the SD-029 / MECH-256 spec single-pass residual ||z_obs - E2(z_prev, a_actual)||. ARM_0 baseline dropped (no ext events). ARM_1 intact + ARM_2 action-scrambled falsification. P2 graduation raised to 0.85 with interventional training (SD-013) enabled. C1 forward_r2 threshold relaxed to 0.85 to accommodate reef_food_ext-induced noise.
4. **rv-pinned cluster architectural follow-up** -- the 2026-05-07T23:00Z review surfaced an architectural hazard: experiments that call `select_action()` but never `agent.update_residue()` leave the BG gate silently dormant (precision pinned, running_variance never updates). Either document the update_residue() loop contract explicitly or move rv update into select_action() so the gate cannot be silently dormant; consider Q-claim.
5. **EWIN-PC + ree-cloud-1/2 SIGTERM coincidence** -- the 2026-05-06T09:28-09:29Z three-EXQ kill pattern noted in the previous nightly recurs in the form of a runner_status ERROR record blocking V3-EXQ-530 force_rerun (had to rename to V3-EXQ-530b to bypass). Supervisor / restart strategy on the cloud workers warrants follow-up.
6. **Active governance cycle close-out** -- claim governance-2026-05-06T2156Z is now done per the 2026-05-08T00:43Z pending_review=0 regeneration; final claims.yaml / claims.json deltas land in the next nightly snapshot.

---

## Status Snapshot (2026-05-07T01:12Z -- nightly docs sync, 2026-05-06 in-flight wave drained the queue + 32-item pending_review accumulation under active governance walk)

- **No new SD / MECH structural landings since the 2026-05-06T01:35Z nightly snapshot.** All architectural substrate work captured in the previous nightly (SD-019a / SD-050-comparator / SD-050 reef substrate / SD-051 / SD-052 / SD-049 Phase 2 hybrid encoder) remains current. Today's repo activity was experimental: the 2026-05-06 morning's "write backlog EXQ-528-534" pass + EXQ-244a + EXQ-535 SD-029 P1 target fix + manifest-correction wave (EXQ-452a duplicate marked superseded; EXQ-433c marked superseded; EXQ-433e re-tagged from bespoke `inconclusive_insufficient_events` to canonical `non_contributory`) + the EXQ-418k canonical run_id restoration pass (manifests + dir + source scripts 418j/418k all corrected; bare-timestamp run_id phantom eliminated) + the indexer backlog literature-evidence epoch-filter parity fix + the Q-019 disconfirming-balance lit pull (4 weakens entries: Redgrave 1999 unified-selection; Mink 1996 focused selection; GPR 2001 Part I selection+control decomposition; Wouterlood 2018 cross-loop dopaminergic linkage; lit_conf 0.884 -> 0.776; quadrant unchanged plausible_unproven).
- **Runner activity since the 2026-05-06T01:35Z nightly:** 608 -> **628 completions (+20)**. Cumulative breakdown 117 -> **120 PASS** / 253 -> **255 FAIL** / 70 -> **72 ERROR** / 168 -> **181 UNKNOWN**. Three new PASSes -- V3-EXQ-528 SD-029 comparator-trained (the 60-episode trained-comparator clears the SD-029 graduation gate -- supersedes the older fixed-2000-step EXQ-523 substrate-readiness baseline), V3-EXQ-533 MECH-102 harm-stream ablation (substrate-ceiling demote may flip to standard-PASS depending on the governance walk), V3-EXQ-534 SD-016 cue terrain training (continues the 2026-04-25 Path 1 diversification-loss thread). Two new ERRORs -- V3-EXQ-244a MECH-165 reverse replay diversity validation and V3-EXQ-530 ARC-016 precision-commit circuit -- both SIGTERM cloud kills at 2026-05-06T09:28-09:29Z (coincident infrastructure event on ree-cloud-1 / ree-cloud-2 -- already noted in the morning's diagnose-errors staging report).
- **Queue depth:** 9 -> **0 (empty `items: []` 2026-05-07T01:12Z)**. The reef-superseding wave + the diagnostic-ablation backlog all completed through the day, with V3-EXQ-535 SD-029 P1 target fix the last item to be claimed (DLAPTOP-4.local at 21:48Z); on completion the runner pushed an empty queue.
- **Pending review:** 4 -> **32 items** (7 PASS / 14 FAIL / 11 runner-only ERROR/UNKNOWN/smoke). Pending_review was regenerated by governance.sh at 2026-05-06T21:57Z immediately after the active governance cycle (claim governance-2026-05-06T2156Z) opened. The new accumulation reflects the entire 2026-05-06 wave landing in pending_review faster than the prior governance cycle could clear, plus three carry-overs from the 2026-05-05 reef-superseding wave (V3-EXQ-454a / 452a / 525). The active governance cycle is mid-walk at this nightly read (~3h old, well within the 6-hour stale-after-hours window).
- **Active governance cycle (claim governance-2026-05-06T2156Z, opened 2026-05-06T21:56Z):** holds REE_assembly governance files (claims.yaml / claims.json / review_tracker.json / pending_review.md / promotion_demotion_recommendations.md / experiment_proposals.v1.json / substrate_queue.json) plus WORKSPACE_STATE.md and TASK_CLAIMS.json. Final decisions land downstream of this nightly snapshot. The two PASSes flagged above (EXQ-528 SD-029 comparator-trained, EXQ-533 MECH-102 harm-stream ablation) plus EXQ-534 SD-016 cue terrain training are the obvious promotion-candidates the walk lands first; the FAILs distribute across SD-005 (532) / SD-015 (531) / SD-016 (418k) / Q-034 (526) / MECH-098 (529) / MECH-112 (527) / MECH-256+SD-029 (535).
- **Bottleneck note:** the 32-pending-review accumulation is the immediate gate. Underneath that, the **monostrategy / reef-recovery thread** remains the dominant scientific bottleneck -- whether reef substrate alone is sufficient to recover behavioural acceptance under the SD-029 / SD-032b / SD-032c / Q-034 / MECH-112 / ARC-016 / MECH-257 / SD-049 Phase 2 cluster, or whether downstream calibration is also required. Three FAILs in the 2026-05-06 wave (V3-EXQ-526 Q-034, V3-EXQ-527 MECH-112 twice, V3-EXQ-535 SD-029 P1) sharpen that question -- the reef substrate is in place but several downstream behavioural acceptance criteria are still not landing.

### Immediate Work Queue (This Cycle, 2026-05-07)

1. **Active governance walk completion (32 items)** -- 7 PASS to verify-and-close (V3-EXQ-418f SD-016 attention uniformity probe carry-over, V3-EXQ-523a SD-029 reef comparator, V3-EXQ-525 SD-003 attribution anchor PASS variant, V3-EXQ-528 SD-029 comparator-trained, V3-EXQ-244a MECH-165 -- governance must classify since the run errored, V3-EXQ-533 MECH-102, V3-EXQ-534 SD-016 cue terrain); 14 FAIL to walk (the reef-superseding wave + V3-EXQ-525 + V3-EXQ-445g + V3-EXQ-517b + V3-EXQ-527 + V3-EXQ-526 + V3-EXQ-418k + V3-EXQ-532 + V3-EXQ-529 + V3-EXQ-531 + V3-EXQ-535); 11 runner-only ERROR/UNKNOWN/smoke to triage (V3-EXQ-244a, V3-EXQ-418j, V3-EXQ-445g, V3-EXQ-514d, V3-EXQ-514e, V3-EXQ-517b, V3-EXQ-524, V3-EXQ-530, V3-EXQ-531, V3-EXQ-533, V3-EXQ-534).
2. **EVB-PINNED-Q019 backlog item** -- the pinned status note still reads "No literature extracted yet" (registered 2026-02-27). Its reading list has been fully satisfied since Feb and the corpus is now bias-corrected (4 weakens added 2026-05-06). A future cleanup should either un-pin or rewrite the status_reason; not blocking.
3. **SD-049 Phase 2 z_resource encoder** -- still flagged ready=True priority=2 in `substrate_queue.json`. V3-EXQ-514c / 514d / 514e completed; whether the encoder identity expansion + phased training protocol P0/P1/P2 + SD-032 consumer cascade migration to read `obs_dict['per_axis_drive']` are next is a governance-walk decision.
4. **MECH-X commit_boundary + MECH-Y attribution_rigidity_setpoint registration** -- still pending user signoff on the 2026-05-03 commit-boundary-belief-lock lit-pull verdict (REGISTER WITH MODIFICATION).
5. **V3-EXQ-490d Q-040b staleness-into-gate factorial** -- still drafted-but-unqueued pending design refinement.
6. **V3-EXQ-495 V3-full-completion-gate re-run plan** -- still deferred until the Q-040b cluster-successor lands.
7. **MECH-095 / MECH-102 substrate-enrichment review** -- SD-047 unblocks a successor experiment that exploits the multi-source dynamics substrate; the V3-EXQ-533 MECH-102 PASS may flip the substrate-ceiling classification on MECH-102. Governance walk decides.
8. **EWIN-PC + ree-cloud-1/2 SIGTERM coincidence (2026-05-06T09:28-09:29Z)** -- two simultaneous cloud-worker kills (V3-EXQ-244a + V3-EXQ-530) plus one slightly earlier on V3-EXQ-495 are now a recurring pattern; supervisor / restart strategy on the cloud workers warrants follow-up.

---

## Status Snapshot (2026-05-06T11:31Z -- afternoon update, scheduled ree-lit-pull-pm: Q-019 disconfirming-balance lit pull + 627 runner completions + 18-item pending_review)

- **Q-019 disconfirming-balance lit pull (2026-05-06T11:21Z, scheduled ree-lit-pull-pm).** The pinned EVB-PINNED-Q019 backlog item was registered 2026-02-27 with a 6-paper reading list now satisfied; the genuine remaining gap was a confirmation-bias signature in the 16-entry corpus (11 supports / 5 mixed / **0 weakens**). Pulled 4 disconfirming entries:
  - **Redgrave / Prescott / Gurney 1999** (Neuroscience, [10.1016/s0306-4522(98)00319-4](https://doi.org/10.1016/s0306-4522(98)00319-4)) -- canonical unified-selection thesis (BG = single centralised selection device). conf=0.78.
  - **Mink 1996** (Prog Neurobiol, [10.1016/s0301-0082(96)00042-1](https://doi.org/10.1016/s0301-0082(96)00042-1)) -- focused selection / surround-inhibit + focal-disinhibit on shared GPi/SNr output. conf=0.74.
  - **Gurney / Prescott / Redgrave 2001 Part I** (Biol Cybern, [10.1007/PL00007984](https://doi.org/10.1007/PL00007984)) -- GPR computational model: selection + control decomposition explicitly contra direct/indirect partitioning. conf=0.70.
  - **Wouterlood et al. 2018** (J Neurosci Res, [10.1002/jnr.24242](https://doi.org/10.1002/jnr.24242)) -- empirical cross-loop dopaminergic linkage from medial ventral striatum (limbic) to nigrostriatal cells projecting to dorsolateral striatum (sensorimotor); rules out strict three-loop segregation in the strongest form. conf=0.72.
- **Effect on Q-019 evidence:** entries 16 -> 20; direction_counts 11s/5m/0w -> **11s/5m/4w**; lit_conf 0.884 -> **0.776**; quadrant unchanged (plausible_unproven). Total lit entries 1179 -> 1183. The corpus is now properly balanced for governance to weigh option (A) single-gate against option (B) three-loop without the prior selection bias. REE_assembly pushed (75de72dc3).
- **Substrate / SD status: no change since the morning 2026-05-06T01:35Z snapshot.** Lit pull does not touch ree-v3 SD implementation, queue state, or runner_status.
- **Runner activity since the morning 2026-05-06 snapshot:** 608 -> **627 completions** (+19 runs since the morning 04:28Z snapshot; cumulative breakdown 120 PASS / 255 FAIL / 72 ERROR / 180 UNKNOWN). Queue depth: 0 pending (everything has been claimed / completed); pending_review now lists **18 items** (3 PASS / 10 FAIL / 5 runner-only ERROR/UNKNOWN/smoke). The pending_review backlog grew because the morning's queued backlog (EXQ-528/531/533/534) plus the in-flight reef-superseding wave (514c/d/e, 517b, 523a, 526, 527) have been completing through the afternoon faster than they have been reviewed.

### Immediate Work Queue (This Cycle, 2026-05-06 afternoon)

1. **Pending_review walk (18 items)** -- 3 PASS to verify-and-close (V3-EXQ-418f SD-016 attention uniformity probe, V3-EXQ-523a SD-029 reef comparator, V3-EXQ-525 SD-003 attribution anchor); 10 FAIL to walk (the reef-superseding wave + V3-EXQ-525 + V3-EXQ-445g + V3-EXQ-517b + V3-EXQ-527 + V3-EXQ-526 + V3-EXQ-418k); 5 runner-only ERROR/UNKNOWN to triage via /diagnose-errors (V3-EXQ-445g, V3-EXQ-514d, V3-EXQ-517b, V3-EXQ-514e, V3-EXQ-418j).
2. **Q-019 governance position** -- with 4 weakens entries now in the corpus, the question genuinely shifts from "three-gate vs single-gate" to "strict-segregation vs unified-with-topographic-inputs vs softer-multi-loop-with-cross-talk". Strict segregation is the version Wouterlood 2018 directly disproves; the remaining viable hypotheses have smaller arbitration distance from each other than the existing corpus suggested. Q-019 was not promoted/demoted by this lit pull -- the substrate-level question remains open and the next move is experimental, not bibliographic.
3. **EVB-PINNED-Q019 backlog item** -- the pinned status note still reads "No literature extracted yet" (registered 2026-02-27). Its reading list has been fully satisfied since Feb and the corpus is now bias-corrected. A future cleanup should either un-pin or rewrite the status_reason; not blocking.

## Status Snapshot (2026-05-06 -- nightly docs sync, post-2026-05-04/05/06 reef-enrichment supersession wave: SD-019a / SD-051 / SD-052 / SD-050 reef substrate landings + reef-superseding monostrategy-blocked predecessors queued + INV-054 lit supplement + indexer backlog literature epoch-filter parity fix)

- **SDs / MECHs moved to Implemented since the 2026-05-04 nightly snapshot:**
  - **SD-019a** (`harm_stream.immediate_affective_valence`) IMPLEMENTED 2026-05-04 --
    third-tier z_harm_un EMA between fast z_harm_s and slow z_harm_a (~5-step rise
    at alpha=0.2); AIC + E3 short-horizon urgency redirect when use_harm_un;
    SD-021 descending modulation deliberately does NOT attenuate z_harm_un so
    controllability parity matches Loffler 2018; non-trainable EMA buffer; bit-
    identical OFF (184/184 contracts PASS with flag OFF). V3-EXQ-518 dry-run
    PASS, queued (4-arm, 9 acceptance criteria UC0a-b/UC1a-d/UC2a-b/UC3).
  - **SD-051 / MECH-304** (`safety_prediction.cue_specific_conditioned_inhibition_substrate`)
    IMPLEMENTED 2026-05-04 -- ConditionedSafetyStore non-trainable EMA prototype of
    z_world at MECH-302 event ticks + per-step decay forgetting; cosine similarity ->
    sigmoid -> commitment-release gate when beta elevated. New ree_core/safety/
    package. V4-deferred items: approach attractor toward safety-signaling cues
    + contrastive cue-specific learning (require V4 multi-step planning + trainable
    encoder head). V3-EXQ-519 substrate-readiness queued; 6 of 9 sub-tests PASS,
    C6 surfaced upstream MECH-302 event-source dependency now under retest in
    V3-EXQ-517a/b.
  - **SD-052 / MECH-303** (`safety_prediction.contextual_passive_substrate`)
    IMPLEMENTED 2026-05-04 -- slow vmPFC/hippocampal-analog: ResidueField extended
    with safety_terrain_rbf_field + accumulate_safety + evaluate_safety; per-step
    accumulation when z_harm_a.norm() < harm_threshold AND not hypothesis_tag;
    commitment release when mean evaluate_safety >= release_threshold; same RBF
    pattern as ARC-030/MECH-117 benefit_terrain but separate field. V3-EXQ-520
    4-arm substrate-readiness diagnostic dry-run PASS 10/10.
  - **SD-050 reef enrichment substrate** IMPLEMENTED 2026-05-04 in CausalGridWorldV2
    -- corner-adjacent Manhattan-radius reef safe zones (hazards excluded; 5x5
    reef_field_view scent gradient appended to world_state, world_obs_dim
    250->275) + food-attracted hazard drift bias (probability hazard_food_attraction).
    Two behavioral attractors -- "flee to reef" vs "forage" -- to break the single
    fixed route. V3-EXQ-521 substrate-readiness PASS 7/7; V3-EXQ-522 PASS
    zone_transitions=48.9 between attractors. NB: SD-050 ID is currently shared
    with the suffering-derivative comparator (also 2026-05-04); reconcile in a
    future cleanup.
- **Strategic decision (2026-05-05): reef-enrichment supersession wave.** The
  monostrategy-audit-2026-05-05T0712Z full-scan over failed experiments identified
  monostrategy as the dominant blocker across SD-029 / SD-032b / SD-032c /
  SD-049-Phase-2 / Q-034 / MECH-112 / MECH-257 / ARC-016 / SD-016. Rather than
  env-tune per EXQ, the lever is to swap in the SD-050 reef substrate as the
  env-entropy precondition under all affected predecessors. Reef-superseding
  versions queued: V3-EXQ-433e (SD-029 reef comparator), 445e/f/g (SD-032b dACC
  reef), 325f (SD-032c AIC descending reef), 452a (MECH-257 dual-function E2
  reef), 454a (ARC-016 adaptive commitment reef), 514c (SD-049 Phase 2 reef
  behavioural validation), 526 (Q-034 reef threshold sweep), 527 (MECH-112
  goal-directed reef + identity encoder). Three already FAILed and are on
  pending_review (454a, 452a, 525 SD-003 attribution anchor); whether reef alone
  is sufficient is the live question for the next governance walk.
- **Indexer fix landed 2026-05-05:** backlog literature-evidence epoch filter
  brought into parity with the matrix builder. One-line change at
  `evidence/experiments/scripts/build_experiment_indexes.py:3002` mirroring the
  matrix's stated `Literature entries are not epoch-filtered` policy. Symptom:
  morning lit-pulls kept flagging MECH-057, MECH-062, Q-019 as
  `missing_literature_evidence` despite well-populated targeted_review directories
  (lit_conf 0.78-0.89). Fix: `if entry.get("source_type") == "literature" or
  is_applicable(entry):`. Verification: governance.sh ran clean. MECH-057
  lit_count 0->7, lit_conf 0.0->0.827, evidence_needed lit->experimental.
  MECH-062 dropped from backlog (confirmed_established). Q-019 pinned entry
  preserved. missing_literature_evidence reasons across backlog 3 -> 1 (only
  EVB-0131 onboarding phantom remains). Backlog item count 196 -> 205 because
  more claims now correctly register entries and trigger real signals (low_exp_conf
  etc) where previously they were silently lit-blank.
- **Manifest correction wave 2026-05-05T22:15Z:** EXQ-445g + EXQ-523a queued
  (dacc_bias_max_abs=2.0 fix supersedes 445f, evidence_direction_per_claim
  reset). EXQ-445f manifest evidence_direction_per_claim["SD-032b"] corrected
  from "mixed" to "does_not_support" (entropy=0.0 all seeds, C2 wins=0).
  EXQ-523 flat JSON + per-run manifest evidence_direction corrected from
  "supports" to "non_contributory" with per-claim overrides + note +
  superseded_by added. Both run IDs marked reviewed in review_tracker.json.
  Governance pipeline ran clean (0 EXQ-523 warnings).
- **Lit-pull supplement 2026-05-05:** INV-054 depressive maintenance loop +3
  entries (Jacobson 1996 BA RCT conf=0.78; van de Leemput 2014 PNAS bistable
  mood attractors conf=0.84; Tang 1999 sudden gains conf=0.76); INV-054
  lit_conf 0.762 -> 0.858. LIT-0086 (ARC-029) and LIT-0088 (MECH-072) already
  well-covered (6 entries each), no new work needed.
- **Experiment activity since the 2026-05-04 nightly snapshot:**
  - **+23 runner completions** (585 -> 608; 113 -> 117 PASS / 248 -> 253 FAIL /
    67 -> 70 ERROR / 157 -> 168 UNKNOWN). +4 PASS spans V3-EXQ-485a SD-033b
    multi-mode landing PASS, V3-EXQ-503 carry-over, V3-EXQ-521 reef substrate
    readiness PASS, V3-EXQ-522 reef behavioral diversity PASS.
  - **Pending review queue regenerated 2026-05-05T22:12Z: 4 items.** 3 FAIL
    (V3-EXQ-454a ARC-016 reef, V3-EXQ-452a ARC-033/MECH-257 reef, V3-EXQ-525
    SD-003 attribution anchor) + 1 ERROR (V3-EXQ-418j SD-016 reef env-entropy
    fix; runner-only). The 2026-05-04T22:01Z governance walk had cleared
    pending_review after walking ARC-026 / MECH-093 promotions and the
    V3-EXQ-485a SD-033b multi-mode PASS; the 4-item residue is the post-walk
    accumulation from the reef-superseding wave + the SD-003 attribution anchor.

### Immediate Work Queue (This Cycle, 2026-05-06)

1. **Reef-superseding pending_review walk** -- 3 FAILs on the queue:
   V3-EXQ-454a (ARC-016 adaptive commitment under reef -- whether reef restores
   the env-entropy needed for adaptive commitment to behave dissociably from
   fixed-threshold), V3-EXQ-452a (ARC-033 / MECH-257 / SD-013 dual-function
   E2 under reef -- whether the comparator-vs-evaluator gating dissociation is
   recoverable under reef behavioural diversity), V3-EXQ-525 (SD-003 attribution
   anchor on post-SD-011 substrate -- corrected output schema superseding EXQ-205).
   The governance question for each is: "Is reef alone the missing precondition,
   or does the architecture also need calibration?" The next session walks
   these decisions.
2. **V3-EXQ-418j ERROR** -- SD-016 reef env-entropy fix runner-only ERROR;
   diagnose-errors should triage whether this is a reef substrate integration
   issue or a script-level bug.
3. **Active in-flight queue (9 items)** -- V3-EXQ-524 (reef fishtank showcase
   episode log) + V3-EXQ-514c claimed by ree-cloud-2 (SD-049 Phase 2 reef
   behavioural validation) + V3-EXQ-514d claimed by DLAPTOP-4.local (BG gating
   diagnostic) + V3-EXQ-514e (BG gating seaweed diagnostic) + V3-EXQ-517b
   (MECH-302 relief-completion longer episodes, supersedes 517a) + V3-EXQ-523a
   (SD-029 reef comparator with adaptive graduation gate, supersedes 523) +
   V3-EXQ-526 (Q-034 reef threshold sweep, supersedes 451) + V3-EXQ-527
   (MECH-112 goal-directed reef + identity encoder).
4. **SD-049 Phase 2 z_resource encoder upgrade** -- still flagged ready=True
   priority=2 in `substrate_queue.json`. V3-EXQ-514c is the in-flight
   behavioural validation; once it lands, the encoder identity expansion +
   phased training protocol P0/P1/P2 + SD-032 consumer cascade migration to
   read `obs_dict['per_axis_drive']` are next.
5. **MECH-X commit_boundary + MECH-Y attribution_rigidity_setpoint
   registration** -- still pending user signoff on the 2026-05-03
   commit-boundary-belief-lock lit-pull verdict (REGISTER WITH MODIFICATION).
6. **V3-EXQ-490d Q-040b staleness-into-gate factorial** -- still drafted-but-
   unqueued pending design refinement in light of V3-EXQ-490c + V3-EXQ-490e
   FAILs.
7. **V3-EXQ-495 V3-full-completion-gate re-run plan** -- still deferred until
   the Q-040b cluster-successor lands.
8. **MECH-095 / MECH-102 substrate-enrichment review** -- SD-047 unblocks a
   successor experiment that exploits the multi-source dynamics substrate;
   design / proposal not yet drafted.
9. **SD-051 / SD-052 substrate-readiness completion** -- V3-EXQ-519 6-of-9
   PASS upstream-blocked by MECH-302 event source (under retest in V3-EXQ-517a/b);
   V3-EXQ-520 SD-052 dry-run PASS, awaiting full run.

---

## Status Snapshot (2026-05-04 -- nightly docs sync, post-2026-05-03 substrate-enrichment wave: SD-047 / SD-048 / SD-049 Phase 1 / SD-050 (MECH-302) substrate landings + ARC-026 / MECH-093 promotions + relief-completion + commit-boundary-belief-lock lit-pulls)

- **SDs / MECHs moved to Implemented since the 2026-05-03 nightly snapshot:**
  - **SD-047** (`environment.multi_source_dynamics`) IMPLEMENTED 2026-05-03 in
    CausalGridWorld via flat kwargs (3 concurrent stochastic sources at
    distinct scales: AR(1) weather field + Poisson transient hazards + mobile
    drift sources; 4-arm noise-sweep lever; substrate-ceiling unblock for
    MECH-095 TPJ agency-detection; bit-identical OFF + per-source ablation;
    activation smoke ARM_2 calibration ratio 1.95:1 within 1:1-2:1 SD-doc
    target band). V3-EXQ-509 PASS 7/7 within minutes of queueing on Mac.
    SD-047 promoted candidate -> provisional, v3_pending removed.
  - **SD-048** (`body.interoceptive_noise_dynamics`) IMPLEMENTED 2026-05-03 in
    CausalGridWorldV2 (3 concurrent agent-independent body-state noise
    sources on harm_obs_a readout: autonomic Gaussian + sensitisation
    Poisson + fatigue AR(1); Level 2 counterpart to SD-047 at body-state
    layer; substrate-ceiling unblock for ARC-058 / ARC-033 arbitration).
    V3-EXQ-511 6/7 with C1b sub-threshold at scale=0.25 -- the 2026-05-03
    governance walk accepted this as the SD-doc's calibration-off-but-
    architecture-holds row (under-calibration on ARM_1, not architectural
    failure); evidence_direction reclassified weakens -> non_contributory
    with manifest note. SD-048 stays candidate / v3_pending pending V3-EXQ-512
    ARC-058 comparator-gap behavioural successor.
  - **SD-049 Phase 1** (`environment.multi_resource_heterogeneity`) IMPLEMENTED
    2026-05-03 in CausalGridWorld (3 qualitatively distinct resource types incl
    non-homeostatic novelty channel + per-axis homeostatic drive vector
    parallel to legacy agent_energy via configurable max/mean/sum combiner +
    curriculum-introduction hook keyed on cross-episode _global_step;
    world_obs_dim 250 -> 325 default 3-type; benefit profiles
    sigmoidal_saturating / sharp_saturation / novelty_decay; substrate-roadmap
    H-priority #2; lit-anchored sd_049 lit_conf=0.898 across 5 PubMed entries).
    V3-EXQ-513 PASS 13/13 incl curriculum gates CC1/CC2 within minutes.
    Phase 2 z_resource encoder identity expansion + SD-032 consumer cascade
    + V3-EXQ-514 behavioural validation tracked in
    `evidence/planning/substrate_queue.json` as SD-049-PHASE-2 ready=True
    priority=2; v3_pending stays true on SD-049 until Phase 2 lands.
  - **SD-050 / MECH-302** (`relief.completion_event_reuses_goal_achievement_pipeline`)
    IMPLEMENTED 2026-05-04 -- SufferingDerivativeComparator on z_harm_a
    stream; reuses MECH-057a beta-gate release + MECH-094 categorical
    VALENCE_LIKING tag write; non-trainable; sense() ticks comparator,
    select_action() consumes event flag; bit-identical OFF; MECH-094
    simulation_mode gate. V3-EXQ-515 comparator logic PASS 7/7 on Mac.
    V3-EXQ-516 agent-loop integration diagnostic queued (4-arm:
    ARM_0 OFF backward-compat / ARM_1 event fires / ARM_2 valence write /
    ARM_3 flat signal no false fires; ~1 min). MECH-302 / MECH-303
    registered candidate / v3_pending earlier the same day from the
    relief-completion pre-registration lit-pull verdict.
- **Promotions (2026-05-03T02:38Z governance walk):**
  - **ARC-026 (`capacity_scaling.world_dim_cohort`) candidate -> provisional.**
    Two PASS pillars on different methodologies: EXQ-232 (full goal-conditioned
    agent) + V3-EXQ-507 (capacity-sweep weak-reading replication via
    random-action policy). conflict_ratio=0.286 below provisional gate.
  - **MECH-093 (`control_plane.zbeta_rate_modulation_dissociable`) candidate
    -> provisional.** Three PASS pillars: EXQ-097b step-level + EXQ-396b
    cross-experiment + V3-EXQ-505 substrate-level z_beta x salience
    factorial dissociation directly driving MultiRateClock. Resolves the
    EXQ-097 encoding-artifact conflict.
- **Lit-pull wave 2026-05-03 (3 sessions, 23 PubMed-sourced entries):**
  - **Relief-completion mechanism** (8 entries): Tanimoto 2004 + Andreatta
    2012 LOAD-BEARING + Navratilova 2012 + Bromberg-Martin 2010 +
    Brischoux 2009 + Ramirez 2015 (M1 reward-circuit substrate for
    relief event); Kreutzmann 2020 + Meyer 2019 (M2/parallel substrate
    for safety-cue prediction). Verdict: hybrid-leaning-Model-1 conf 0.80.
    Outcome: MECH-302 (relief-completion event reuses goal-achievement
    pipeline) + MECH-303 (safety-cue parallel predictive substrate) both
    registered candidate / v3_pending in claims.yaml; 8 entries cross-tagged.
    MECH-302 lit_conf=0.904; MECH-303 lit_conf=0.780.
  - **SD-049 multi-resource heterogeneity pre-implementation lit-pull**
    (5 entries): Berridge 2018 + Smith & Berridge 2007 + Kidd & Hayden 2015
    LOAD-BEARING (non-homeostatic novelty channel) + Shutts/Spelke 2009 +
    Matthews/Tye 2016 falsifier-adjacent (V3/V4 division of labor for
    social wanting). SD-049 lit_conf 0.0 -> 0.898.
  - **Commit-boundary belief-lock pre-registration lit-pull** (7 entries):
    Izuma 2010 PNAS conf 0.86 + Colosio 2017 J Neurosci conf 0.78 (cognitive
    dissonance + post-decisional consolidation); Saravanan 2010 BJP conf 0.68
    (insight in psychosis -- evidence indirect because clinical literature
    does not separate enacted from non-enacted delusional content);
    Gudjonsson 2016 Cortex conf 0.80 (forensic / pressured-internalized
    false confession with diary case); Sterzer 2018 Biol Psychiatry conf 0.84
    (predictive-coding orthogonality cross-check explicitly flagging
    emergence-vs-persistence asymmetry as unresolved); **Voigt 2018 J
    Neurosci conf 0.88 LOAD-BEARING + Tandetnik 2021 Cortex conf 0.82**
    (neural substrate of revising acted-upon vs non-acted-upon beliefs;
    cleanly DISSOCIATE two substrates -- commit-record strength via
    hippocampus AND executive-conflict-resolution gain via frontal cortex).
    Verdict: REGISTER WITH MODIFICATION as two-mechanism cluster
    MECH-X commit_boundary_belief_lock + MECH-Y attribution_rigidity_setpoint
    (two-parameter substrate where pathological lock requires both
    substrates engaged at high gain, while pathological permeability /
    confabulation territory requires commit-record weakness regardless of
    executive engagement). All 7 entries tagged placeholder
    MECH-CBBL-PROPOSED to avoid inflating registered-claim lit_conf.
    Awaiting user signoff before MECH registration.
- **Governance walks 2026-05-03 (two sessions):**
  - **2026-05-03T02:38Z walk** (post-V3-EXQ-504..508 cohort): 5 indexed
    pending walked; 2 PASS / 3 FAIL on raw scoring; 4 reclassifications
    applied; 2 promotions (ARC-026, MECH-093 -- see above);
    SD-023 hold continued; MECH-057b / MECH-263 / Q-037 V3-pending hold
    continued; pending_user 5 -> 0; pending_review 6 -> 0; 8 manifest
    files edited, claims.yaml status+EQN updates for ARC-026 and MECH-093,
    6 decision_log entries appended.
  - **2026-05-03T23:56Z walk** (post-substrate-enrichment wave): 3 substrate-
    readiness diagnostics walked + 1 deferred runner-only ERROR.
    EXQ-509 SD-047 PASS 7/7 (clean close); EXQ-511 SD-048 FAIL 6/7
    accepted as non_contributory per SD-doc interpretation grid;
    EXQ-513 SD-049 Phase 1 PASS 13/13; V3-EXQ-495 MECH-163 deferred
    (SIGTERM infrastructure kill on ree-cloud-1 at 4h of ~40h, exit code
    -15; defer until Q-040b cluster-successor lands). MECH-302 / MECH-303
    / SD-049 pending_user holds applied (all hold_pending_v3_substrate,
    correctly held). 0 pending_user remaining. review_tracker updated,
    substrate_queue updated, claims.json rebuilt.
- **Experiment activity since the 2026-05-03 nightly snapshot:**
  - **+11 runner completions** (574 -> 585; 113 PASS unchanged / 247 -> 248
    FAIL / 66 -> 67 ERROR / 148 -> 157 UNKNOWN). The +11 covers
    V3-EXQ-509/511/513/515 substrate-readiness PASSes (UNKNOWN runner
    result codes with PASS manifest verdicts), V3-EXQ-495 ERROR on
    ree-cloud-1, and indexer-surfaced carry-overs from the dedup sweep.
  - **Pending review queue regenerated 2026-05-04T01:17Z: 2 items
    (both PASS).** Both 2026-05-03 governance walks cleared their indexed
    pending sets at write time; the 2026-05-04 nightly indexer surfaced
    two PASS runs that completed after the 23:56Z walk: **V3-EXQ-512**
    (SD-048 ARC-058 / ARC-033 comparator-gap behavioural successor;
    deferred at the 23:56Z walk but ran on Mac 2026-05-04T00:57Z and
    PASSed) and **V3-EXQ-515** (MECH-302 suffering-derivative comparator
    substrate readiness; PASS indexer-surfaced 2026-05-04T01:17Z).
    Only V3-EXQ-516 (MECH-302 agent-loop integration diagnostic) remains
    queued; SD-049 Phase 2 follow-on remains the next substrate task with
    ready=True.

### Immediate Work Queue (This Cycle, 2026-05-04)

1. **V3-EXQ-516 result review** -- the queued MECH-302 agent-loop
   integration diagnostic (~1 min) is the only currently-queued
   experiment. Once it runs, governance walks the 4-arm acceptance
   (ARM_0 OFF backward-compat / ARM_1 event fires / ARM_2 valence write /
   ARM_3 flat signal no false fires) and decides whether MECH-302 is
   ready to flip from candidate / v3_pending to provisional, or whether
   a behavioural successor is needed.
2. **SD-049 Phase 2 z_resource encoder upgrade** -- the highest-priority
   substrate task in the queue (`substrate_queue.json` SD-049-PHASE-2,
   ready=True, priority=2). 5-step phase_2_scope: (a) z_resource encoder
   identity expansion (one-hot or learned embedding); (b) phased training
   protocol P0/P1/P2; (c) SD-032 consumer cascade migration to read
   `obs_dict['per_axis_drive']`; (d) SD-012 emergent-invariant
   pending_substrate_reconfirmation flag; (e) V3-EXQ-514 4-arm behavioural
   validation pre-registered acceptance (goal_resource_r lift +
   identity-recovery probe + wanting != liking trajectory dissociation,
   with Woo/Spelke-style falsifier branch routing MECH-229 to
   substrate_conditional with V4-1 dependency on flat-failure).
3. **MECH-X commit_boundary + MECH-Y attribution_rigidity_setpoint
   registration** -- pending user signoff on the 2026-05-03
   commit-boundary-belief-lock lit-pull verdict (REGISTER WITH MODIFICATION
   as two-mechanism cluster). Once registered, the 7 placeholder-tagged
   entries cross-tag to the new claims and the per-mechanism lit_conf
   surfaces in the indexer.
4. **V3-EXQ-490d Q-040b staleness-into-gate factorial** -- still drafted-
   but-unqueued pending design refinement in light of the V3-EXQ-490c +
   V3-EXQ-490e FAILs. The use_vs_gate_staleness_lookup OFF vs ON contrast
   at matched 0.4 thresholds remains the falsifiable test of the Q-040b
   strong reading via the 2026-04-29 MECH-284 wiring.
5. **V3-EXQ-495 V3-full-completion-gate re-run plan** -- the 2026-05-03
   ree-cloud-1 SIGTERM ERROR (4h of ~40h) was governance-deferred until
   the Q-040b cluster-successor lands. Re-run plan needs a more robust
   compute target (longer-running cloud capacity or ree-cloud-2 / EWIN-PC)
   given the ~40h horizon.
6. **MECH-095 / MECH-102 substrate-enrichment review** -- now that SD-047
   is implemented and V3-EXQ-509 PASSed, the MECH-095 substrate-ceiling
   unblock path is open: a successor experiment that exploits the
   multi-source dynamics substrate (rather than re-running V3-EXQ-506 on
   the legacy substrate) is the right next step. Design / proposal not
   yet drafted.
7. **SD-048 V3-EXQ-512 ARC-058 comparator-gap behavioural successor** --
   deferred from the 2026-05-03 governance walk pending the
   `evidence_direction: non_contributory` partial-PASS interpretation.
   The body-noise calibration ratio is now within the SD-doc target band
   at ARM_2 (2.39:1); the behavioural test of whether the comparator gap
   widens with the noise substrate ON is the architectural question.
8. **V3 enrichment H-priority queue** -- substrate_roadmap.md still flags
   foreclosure primitives, multi-resource heterogeneity (Phase 2), and
   long-horizon dynamics as H-priority. Multi-resource Phase 1 landed
   2026-05-03; Phase 2 is next-up. Foreclosure primitives + long-horizon
   dynamics remain at design-doc / SD-candidate stage.

---

## Status Snapshot (2026-05-03 -- nightly docs sync, post-2026-05-02 governance walk: SD-011 stable + SD-012 provisional + Phase-3-wave-2 epistemic_category schema + substrate_roadmap + v4_spec + Q-037/038/039 lit-pull)

- **SDs / MECHs moved to Implemented since the 2026-05-02 nightly snapshot:**
  none in the substrate sense -- all substrate work landed in earlier waves.
  The 2026-05-02 work is governance / evidence / planning-artifact work
  layered on top of the existing run set.
- **Promotions (2026-05-02T09:30Z queue walk):**
  - **SD-011 (`harm_stream.dual_nociceptive_streams`) provisional -> stable.**
    exp_conf=0.871, lit_conf=0.871, 7 exp + 23 lit, conflict_ratio=0.148
    (under the 0.20 stable gate). 25 supports / 2 weakens / 3 mixed across
    the largest single-claim corpus in the registry. EXQ-178b
    (harm_fwd_r2=0.742) and EXQ-323a body-damage substrate cleared the
    dissociation that had held it at provisional.
  - **SD-012 (`environment.homeostatic_drive`) candidate -> provisional.**
    exp_conf=0.714, lit_conf=0.874, 5 exp + 16 lit, conflict_ratio=0.20.
    18 supports / 2 weakens / 1 mixed. Substrate has been implemented since
    2026-04-02 (drive_weight=2.0 default in REEConfig.from_dims) -- this
    promotion is the registry catching up to the substrate.
  - Bug fix included as part of this walk (commit 81de5101c, 2026-05-01):
    indexer recommendations function was counting scoring_excluded entries
    (diagnostic_probe / non_contributory / superseded) into the gate's
    exp_conf computation. Phase 3 cutover surfaced this -- spurious
    promotion recommendations for 5 claims with exp_conf=0 in the matrix
    were appearing pre-fix. After fix: pending_user 17 -> 15. After SD-011
    + SD-012 promotions: 15 -> 13.
  - Decision_log appended 2 entries (SD-011 stable, SD-012 provisional)
    with full rationale citing exp/lit/conflict numbers and the gate
    criteria each cleared. validate_claims --strict still PASSes 68/68
    invariants.
- **Phase 3 wave 2 governance schema landed 2026-05-02T11:30Z
  (epistemic_category formalisation):**
  - New `epistemic_category` field on `claims.yaml`, OPTIONAL, with 7
    canonical values: `standard`, `substrate_coherence`, `answer_state`,
    `substrate_ceiling`, `substrate_conditional`, `derivational`,
    `out_of_domain`.
  - `_resolve_epistemic_category(claim_type, invariant_type, explicit)`
    helper in `build_experiment_indexes.py`: explicit value wins; falls
    back to Phase 2 inference (architectural_commitment + universal-invariant
    -> substrate_coherence; open_question -> answer_state; else standard).
    Smoke-tested 10/10 cases.
  - `_recommendation_for_claim` dispatches via the resolver: only `standard`
    runs exp_conf gates; everything else suppresses promote/demote;
    `narrow_open_question` fires only for `answer_state` (so derivational /
    out_of_domain Q-claims stop getting "narrow this" recommendations).
  - `_load_claim_registry` parses optional `epistemic_category` field.
    `validate_claims.py` warn-only validates explicit values against the
    canonical set; invalid falls back to inference (does not crash).
  - **13 annotated claims backfilled with explicit categories:**
    MECH-095, MECH-102 -> `substrate_ceiling`;
    Q-025, Q-026, Q-027 -> `derivational`;
    Q-028, Q-029 -> `substrate_ceiling`;
    Q-030 -> `standard`;
    Q-031, Q-032 -> `out_of_domain`;
    Q-037, Q-038, Q-039 -> `substrate_conditional`.
  - **Result:** pending decision queue dropped from 16 to 4 items (all 13
    annotated claims correctly suppressed by their category; remaining
    items are pre-existing V3-pending holds + SD-023 conflict alert).
    validate_claims --strict still PASS 68/68.
  - `CLAUDE.md` "Claim-type evidence gating" section rewritten as
    "Epistemic categories (Phase 3 wave 2)" with the full mapping table
    and dispatch consequences.
- **Substrate roadmap planning artifact landed 2026-05-02
  (`docs/architecture/substrate_roadmap.md`):**
  - Gathers V3 enrichment work into one planning document.
  - Documents 10 in-flight enrichments landed 2026-04-01..2026-05-02
    (SD-022, SD-023, SD-029, SD-035, SD-036, SD-037, MECH-269 family,
    sleep aggregator, ghost-goal substrate, MECH-295 liking-bridge).
  - Enumerates 7 outstanding V3 enrichments:
    - **3 H-priority:** foreclosure primitives, multi-resource
      heterogeneity, long-horizon dynamics.
    - **2 M-priority:** multi-source environmental dynamics,
      differentiated coping channels V3-lite.
    - **2 L-priority.**
  - Each substrate feature mapped to the claims it would unblock and the
    SD candidate that would register it.
- **V4 spec planning artifact landed 2026-05-02
  (`docs/architecture/v4_spec.md`):**
  - Initial deliberate spec-first artifact for V4 substrate work.
  - 4 V4 primitive additions:
    - **V4-1** multi-agent ecology
    - **V4-2** self-model integration (DR-10..DR-14 from ree-v3 CLAUDE.md)
    - **V4-3** long-horizon dynamics + persistent identity
    - **V4-4** richer action repertoire
  - V4-bound claim cohort: ~12 claims explicitly waiting for V4 substrate.
  - Process gating: Phase A (this document, draft 2026-05-02). Phase B
    onwards gated on V3 full completion (MECH-163 PASS) + governance
    authorization.
  - Migration sketch: V4 substrate is additive; V3 continues for V3
    claims; V4 evidence carries distinct architecture_epoch.
- **Substrate-ceiling annotation walk 2026-05-02T10:35Z (13 claims
  annotated, no status changes):** MECH-095 (TPJ agency-detection,
  9 exp / 7 sup / 4 wk / 5 mix, conflict=0.727) and MECH-102
  (violence-as-terminal, 24 exp / 10 sup / 11 wk / 12 mix, conflict=0.952)
  flagged as substrate_ceiling -- both held at active. Diagnosis:
  CausalGridWorldV2 too coarse to deliver the distinctions these claims
  assert. 11 Q-claims (Q-025..032 / 037..039) walked and categorised
  per the mapping above. Pattern across the cohort: existing
  `narrow_open_question` recommendation collapses 4-5 distinct epistemic
  situations with different next-step implications -- now machine-readable
  via the `epistemic_category` field.
- **Weekend lit-pull 2026-05-02T10:00Z (Q-037 / Q-038 / Q-039,
  9 PubMed-sourced entries):**
  - **Q-037** (psychosis substrate dissociability between MECH-094 /
    MECH-222 / MECH-065+223): Lavalle 2020 (dissociable source-monitoring
    OCD vs SCZ, supports MECH-094/MECH-222 dissociation), Corlett 2025
    (20-yr aberrant salience review; argues MECH-065 may need to split
    into multiple sub-mechanisms), Oulton 2018 (PTSD memory amplification
    reality monitoring, supports MECH-094 tag-loss). lit_conf 0.0 -> 0.823.
  - **Q-038** (D_V temporal-depth representational status):
    Pilkiw 2018 (distributed tonic+phasic temporal codes, supports
    option B), Guan 2024 (abstract interval-invariant subsecond
    structure via double training, supports option A), Gherman 2018
    (VMPFC localised early confidence signal, supports option A by
    analogy). lit_conf 0.0 -> 0.795.
  - **Q-039** (neuromodulators / control-plane vars regulating TCL
    integration window): Fan 2020 (ACh-driven L1 winner-take-all +
    temporal high-pass filter), Xiang 2023 (LC NA neurons phase-lock to
    infra-slow rhythms organising gamma), Kumagai 2023 (VNS
    double-dissociation: ACh selectively modulates gamma/beta, NA
    selectively modulates theta -- cleanest dissociation evidence on
    the table). lit_conf 0.0 -> 0.84.
  - All three claims quadrant: `plausible_unproven` (high lit, no exp).
  - Indexer ran: literature_entries 1113 -> 1122.
- **`/diagnose-errors` cleanup 2026-05-02T18:06Z:** marked 3 obsolete
  unaddressed-error entries discussed in `review_tracker.json`
  (V3-EXQ-008 obsolete March SD-003 era; V3-ONBOARD-smoke-EWIN-PC
  contributor onboarding for inactive machine; V3-ONBOARD-smoke-ree-cloud-1
  Hetzner CX22 onboarding for inactive cloud machine). Remaining 2
  unaddressed errors confirmed intentional NotImplementedError sentinels
  (V3-EXQ-455a + V3-EXQ-449c) waiting on V3-EXQ-476 cascade gate +
  named consumer wiring -- not bugs.
- **Experiment activity since the 2026-05-02 nightly snapshot:**
  - **No new runner completions.** runner_status.json totals unchanged
    at 574 (113 PASS / 247 FAIL / 66 ERROR / 148 UNKNOWN).
  - Pending review queue regenerated 2026-05-02T18:08Z: **1 item**
    (V3-EXQ-490e FAIL on Q-040, carried over from 2026-04-30 governance
    walk; V3-EXQ-503 PASS reviewed 2026-05-01T20:40Z in the Phase 3
    cutover session; 3 obsolete ERROR entries cleared 2026-05-02T18:06Z).

### Immediate Work Queue (This Cycle, 2026-05-03)

1. **V3-EXQ-490e FAIL discussion** -- still the last open pending_review
   item. Floor-relaxation arm has been ruled out as a Q-040b recovery
   path (combined with the V3-EXQ-490c FAIL on the matched-smoke-threshold
   factorial); the next-up falsification of the Q-040b strong reading
   is the staleness-into-gate test (V3-EXQ-490d toggle of
   use_vs_gate_staleness_lookup OFF vs ON at matched 0.4 thresholds via
   the 2026-04-29T11:00Z MECH-284 wiring).
2. **MECH-095 / MECH-102 demotion recommendations** -- now flagged
   `substrate_ceiling` (Phase 3 wave 2 schema); demotion-action
   suppressed by the new gating, but both still need a careful
   substrate-enrichment vs status-revision review at the next governance
   walk. The right response is substrate enrichment rather than more
   experiments on the existing substrate.
3. **V3-EXQ-490d successor design + queueing** -- still the
   highest-priority substrate-validation run after the V3-EXQ-490e FAIL.
   Design refinement needed in light of the 490e FAIL before queueing.
4. **V3-EXQ-495 V3-full-completion-gate queueing decision** -- still
   deferred. The MECH-163 dual-systems test depends on Q-040 / Q-040b
   resolution; queueing locked behind the cluster-successor outcome.
5. **EXP-0174 env-complexity-gate scripting + queueing** -- the
   2026-04-29T19:09Z proposal is unblocking for SD-016 retest path
   (env-entropy precondition) plus sleep / self-model aggregation
   retests (MECH-273 / MECH-275). Manual_proposals entry reserved;
   script not yet written.
6. **OCD Layer 2 / 3 escalation (MECH-290 ablation; SD-046 multi-slot
   GoalState pull-forward)** -- still on the live escalation list after
   EXQ-498 disconfirmed Layer 1; design / queueing not yet started.
7. **Aggregator-floor flag governance review** -- now a 6th-consecutive-
   cycle flag at the next governance walk; cap-aware aggregator review
   with recommendation either (a) accept the floor as architecturally
   reasonable for narrow-open-question Q-claims, or (b) tune the floor
   downward to expose per-paper confidence variance more faithfully.
8. **V3 enrichment H-priority queue** -- substrate_roadmap.md flagged
   foreclosure primitives, multi-resource heterogeneity, and long-horizon
   dynamics as H-priority outstanding. None scheduled yet; design-doc /
   SD-candidate registration is the gating step.

---

## Status Snapshot (2026-05-02 -- nightly docs sync, post-Phase-2-cohort-closure + Option-E-Phase-3-cutover + duplicate-manifest-sweep)

- **SDs / MECHs moved to Implemented since the 2026-04-30 nightly snapshot:**
  none in the substrate sense -- the substrate work is stable. The 2026-05-01
  wave is governance / evidence / production-gate cutover work, plus the
  Phase 2 cohort closing experiment (SD-017 discriminative pair).
- **Phase 2 cohort CLOSED on the experimental-evidence side
  (2026-05-01T20:15Z; reviewed 2026-05-01T20:40Z):**
  - **V3-EXQ-503 / EXP-0171a (SD-017 sleep-phase discriminative pair)** PASS
    3/3 seeds on Mac (~0.32s; runner result code UNKNOWN but manifest verdict
    PASS). Closes the SD-017 evidence gap left by V3-EXQ-500 -- the
    substrate-readiness probe was diagnostic_probe and excluded from scoring,
    so SD-017 sat at exp_conf=0.000 / plausible_unproven despite lit_conf=0.901.
    Three pre-registered metrics M1 cumulative_sws_writes (ARM_A>=N_CYCLES,
    ARM_B==0); M2 ctxmem_state_change Frobenius norm (ARM_A>=0.10,
    ARM_B<=1e-6 -- magnitude probe agnostic to slot-diversity-direction since
    SWS write can REDUCE diversity by clustering slots around real prototype
    geometry; the dry-run originally treated direction as the signal and FAILed
    C1 inverted, redesign was to switch to magnitude); M3 cumulative_rem_rollouts
    (ARM_A>=N_CYCLES, ARM_B==0). ARM_A: sws_writes=24, ctxmem_delta=4.50-5.03,
    rem_rollouts=18 across all seeds; ARM_B: zeros across the board.
  - **Governance impact:** SD-017 quadrant flipped plausible_unproven ->
    confirmed_established; exp_conf 0.000 -> 0.775. **All four EXP-0170/171/171a/
    172/173 Phase 2 standard-gating cohort claims (MECH-094, SD-017, SD-035,
    MECH-062) are now confirmed_established under the new Phase 3 production
    gates.**
- **Lit/Exp Decoupling (Option E) Phase 3 cutover landed 2026-05-01:**
  promotion / demotion gate logic now drives on `experimental_confidence`
  directly instead of the legacy `overall_confidence` blend. Specifics:
  - `decision_criteria.v1.yaml`: `min_overall_confidence` -> `min_exp_conf`,
    `max_overall_confidence` -> `max_exp_conf`. Legacy keys still accepted via
    the `_t(d, new_key, legacy_key, default)` helper for one-cycle backwards
    compat.
  - `planning_criteria.v1.yaml`: retired `low_overall_confidence: 0.55`;
    replaced with `low_exp_conf: 0.55` and `lit_only_above_cap: 0.50`.
  - `build_experiment_indexes.py:_decision_for_claim` reads
    `claim_meta["experimental_confidence"]` directly. Recommendation rationale
    strings now report `exp_conf=…, lit_conf=…, overall_confidence_legacy=…`.
  - **Claim-type evidence gating brought INTO production** (was Phase 1 shadow-
    only). `substrate_coherence` (ARC + universal invariant) and `answer_state`
    (open_question) skip exp_conf-based promote/demote -- they fire
    conflict-resolution alerts and narrow_open_question only. `standard` gating
    (mechanism_hypothesis / design_decision / implementation / emergent or
    grey_zone invariant) fires the full set. Indexer `_load_claim_registry`
    now parses `invariant_type` from claims.yaml.
  - `CLAUDE.md` rewrote "Lit/Exp Decoupling Shadow" as "Lit/Exp Decoupling
    (Option E) -- Phase 3 Cutover Done 2026-05-01" with the full three-phase
    history.
  - **Diff against pre-cutover snapshot of `promotion_demotion_recommendations.md`:**
    +2 actionable demotion recommendations surfaced (MECH-095, MECH-102 -- both
    `mechanism_hypothesis` whose lit_conf was masking insufficient exp_conf
    under the legacy blend); 0 prior recommendations lost. All 4 Phase 2
    standard-gating claims still confirmed_established under the new gates
    (MECH-094 exp=0.770; SD-017 exp=0.775; SD-035 exp=0.770; MECH-062
    exp=0.770). Q-claim narrow_open_question recommendations and ARC
    conflict-resolution alerts all preserved.
  - **Quadrant distribution after cutover:** 194 plausible_unproven;
    68 confirmed_established; 3 speculative; 1 novel_discovery.
- **Duplicate-manifest sweep landed 2026-05-01 (31 phantoms / 25 clusters):**
  - **Phase 1** -- 8 Tier-1 clusters (span < 2h between identical-signature
    emissions). Latest emission kept canonical, older copy marked
    evidence_direction=superseded with span-in-minutes and identical-signature
    sha1 in note. Claims that should see conflict_ratio movement on next index
    build: MECH-220, SD-012, MECH-112, ARC-032, MECH-116, MECH-090, ARC-016,
    SD-005, MECH-071, INV-034.
  - **Phase 2** -- 10 Tier-2 clusters (span 2-24h). 6 of 10 had no intervening
    commit on the experiment script and were auto-superseded; the other 4 had
    substantive commits between emissions and were flagged for manual review at
    `evidence/experiments/dedup_review/phase2_manual_review.md` (074f, 497, 496, 223).
    Claims that should see conflict_ratio movement: ARC-007, SD-004, MECH-033,
    MECH-072, SD-003, SD-007, SD-008, MECH-096, ARC-023.
  - **Phase 3** -- 10 Tier-3 clusters traced to **runner regex bug active
    2026-03-27..03-30, fixed by commit 071f1fc**. Bug caused runner to mis-parse
    "Done. Outcome: PASS/FAIL" as UNKNOWN, leading to silent re-runs of
    completed experiments. Convention: **kept OLDEST emission (legitimate
    original observation), superseded all later emissions (regex-bug-period
    replays).** 12 phantom entries marked. Claims that should see conflict_ratio
    movement: ARC-032, MECH-116, MECH-112, MECH-117, Q-007, ARC-024, MECH-071,
    SD-003, MECH-111, Q-021, MECH-113, MECH-118, MECH-119, Q-022, ARC-029, ARC-030.
  - **Per-run manifest mirroring** -- URGENT FIX: Phase 1/2/3 supersessions
    were originally applied to flat-JSON files at `<exp_type>/<run_id>.json`
    but the indexer reads `<exp_type>/runs/<run_id>_v3/manifest.json`. Mirrored
    the supersession decisions to per-run manifests so the indexer actually
    sees them. 31 per-run manifests across 25 clusters; 5 of 31 EXQ-232 ARC-026
    manifests required re-application as their flat JSONs had been wiped by
    runner auto-sync between 2026-04-29 and 2026-05-01.
  - **Phase 5 dedup guard** -- added
    `_detect_and_mark_duplicate_emissions()` to `build_experiment_indexes.py` as
    in-memory dedup guard with back-off when manual supersessions present;
    WARN logs emitted to stderr per duplicate. Smoke test passed (4s, 31 dups
    caught across 13 experiment_types, mostly old V2 epoch-excluded synthetic
    runs plus 4 new v3 clusters worth manual review: 074f, 133, 223, 484).
- **Experiment activity since the 2026-04-30 nightly snapshot:**
  - Runner-status totals refreshed: **574 completed (113 PASS / 247 FAIL /
    66 ERROR / 148 UNKNOWN; +2 vs 2026-04-30 = V3-EXQ-490e FAIL +
    V3-EXQ-503 EXP-0171a SD-017 discriminative PASS).** V3-EXQ-490e MECH-295
    seeding-strengthening successor (Q-040b BASELINE-vs-RELAXED on activation-
    floor + drive_to_liking_gain knobs with MECH-295 bridge ON in both arms)
    **FAIL on Mac 2026-05-01T03:19Z (~6h)** -- floor-relaxation alone does not
    recover approach_commit; combined with the V3-EXQ-490c FAIL the Q-040b
    strong reading remains weakened.
  - Pending review queue regenerated 2026-05-02T08:51Z: **1 item**
    (V3-EXQ-490e FAIL on Q-040). The 2026-04-30T20:54Z governance walk reviewed
    the four Phase 2 cohort PASSes (V3-EXQ-499/500/501/502) plus the
    V3-EXQ-490c FAIL, dropping pending_review to 0+0 before the 490e FAIL and
    the V3-EXQ-503 PASS re-populated it; only V3-EXQ-490e remains open
    (V3-EXQ-503 PASS reviewed 2026-05-01T20:40Z in the Phase 3 cutover session).

### Immediate Work Queue (This Cycle, 2026-05-02)

1. **V3-EXQ-490e FAIL discussion** -- last open pending_review item.
   Floor-relaxation arm has been ruled out as a Q-040b recovery path
   (combined with the V3-EXQ-490c FAIL on the matched-smoke-threshold
   factorial); the next-up falsification of the Q-040b strong reading
   is the staleness-into-gate test (V3-EXQ-490d toggle of
   use_vs_gate_staleness_lookup OFF vs ON at matched 0.4 thresholds via
   the 2026-04-29T11:00Z MECH-284 wiring).
2. **V3-EXQ-490d successor design + queueing** -- still the highest-priority
   substrate-validation run on the substrate side after the V3-EXQ-490e FAIL.
   Design refinement needed in light of the 490e FAIL before queueing.
3. **V3-EXQ-495 V3-full-completion-gate queueing decision** -- still
   deferred. The MECH-163 dual-systems test depends on Q-040 / Q-040b
   resolution; queueing locked behind the cluster-successor outcome.
4. **EXP-0174 env-complexity-gate scripting + queueing** -- the
   2026-04-29T19:09Z proposal is unblocking for SD-016 retest path
   (env-entropy precondition) plus sleep / self-model aggregation retests
   (MECH-273 / MECH-275). Manual_proposals entry reserved; script not
   yet written.
5. **OCD Layer 2 / 3 escalation (MECH-290 ablation; SD-046 multi-slot
   GoalState pull-forward)** -- still on the live escalation list after
   EXQ-498 disconfirmed Layer 1; design / queueing not yet started.
6. **MECH-095 / MECH-102 demotion recommendations** -- newly surfaced
   by the Phase 3 cutover (both `mechanism_hypothesis` whose lit_conf
   was masking insufficient exp_conf under the legacy blend); both need
   review at the next governance walk. No actionable promotions or
   demotions other than these two surfaced by the cutover.
7. **Aggregator-floor flag governance review** -- 5th-consecutive-cycle
   flag at the next governance walk; cap-aware aggregator review with
   recommendation either (a) accept the floor as architecturally
   reasonable for narrow-open-question Q-claims, or (b) tune the floor
   downward to expose per-paper confidence variance more faithfully.

---

## Status Snapshot (2026-04-30 -- nightly docs sync, post-Phase-2-claim-type-gating cohort PASS wave)

- **SDs / MECHs moved to Implemented since the 2026-04-29 PM snapshot:**
  none in the substrate sense (the same-day MECH-269b + MECH-284
  staleness-into-VsRolloutGate wiring landed at 06:03Z and was already
  captured in the 2026-04-29 PM snapshot below). The day's primary
  signal is on the **experimental-evidence side**: the 2026-04-29 PM
  Phase 2 claim-type-gating reckoning surfaced four standard-gating
  MECH/SD claims that needed first-pass experimental signal, all four
  scripts were written + smoke-tested + queued + executed in one
  session, and **all four PASSed in 3/3 seeds**.
- **Phase 2 claim-type evidence gating landed (2026-04-29T15:47Z):**
  `scripts/generate_option_e_shadow.py` extended with `_evidence_gating(meta)`
  classifying every claim into `standard | substrate_coherence |
  answer_state` based on `claim_type` (and `invariant_type` for
  invariants). Discrepancy / impl_no_exp / low_exp / lit_only_above_cap
  flags now fire only for `standard`-gating claims; the suppressed
  buckets surface separately for transparency. Headline numbers:
  discrepancies 183 -> 135 (48 ARC + universal invariant + Q dropped
  out of actionable), impl_no_exp 15 -> 4 (the 4 genuinely-testable
  MECH/SD claims that needed experiments), low_exp 50 -> 32,
  lit_only_above_cap 142 -> 107. CLAUDE.md "Claim-type evidence
  gating" section documents the rules + restate-Q-as-MECH/SD path.
- **Phase 2 cohort experiments (4 PASS in 3/3 seeds; pending review):**
  - **V3-EXQ-499 / EXP-0170 (MECH-094 hypothesis-tag write-gate
    discriminative pair)** -- substrate-level forced-injection design
    avoiding the V3-EXQ-140 non_contributory failure mode. ARM_A passes
    `hypothesis_tag=True` for sim events (gate active per MECH-094);
    ARM_B passes False (gate ablated, the tag-loss / write-channel
    disinhibition pathology). N_REAL=50 + N_SIM=50 deterministic events
    at disjoint z_world locations. Three pre-registered metrics with
    PASS criteria all met >= 2/3 seeds: ARM_A contam=0.000, confab=0.000,
    MI=0.693 (perfect log(2)); ARM_B contam=1.000, confab=0.640, MI=0.000.
    **Governance impact:** MECH-094 quadrant flipped
    `plausible_unproven` -> `confirmed_established`;
    experimental_confidence 0.000 -> 0.775; overall_confidence
    0.866 -> 0.843 (slight dip from legacy blend now weighting the new
    exp signal). First standard-gating experimental evidence for
    MECH-094 -- prior 9 entries excluded as
    diagnostic_probe / non_contributory.
  - **V3-EXQ-500 / EXP-0171 (SD-017 sleep-phase substrate-readiness
    diagnostic)** -- nine prior FAIL/non_contributory entries on SD-017
    led to a fresh substrate-readiness gate before any behavioural
    retest. PASS.
  - **V3-EXQ-501 / EXP-0172 (SD-035 amygdala analog vs binary)** --
    discriminator between SD-035's analog amygdala substrate and a
    degenerate binary toggle. PASS.
  - **V3-EXQ-502 / EXP-0173 (MECH-062 tri-loop gate coordination)** --
    truly fresh-start MECH-062 evidence (zero priors); first tri-loop
    coordination test on the V3 substrate. PASS.
  - manual_proposals.v1.json: EXP-0170/171/172/173 status -> executed.
- **Experiment activity since the 2026-04-29 PM snapshot:**
  - Runner-status totals refreshed: **572 completed (113 PASS / 246 FAIL /
    66 ERROR / 147 UNKNOWN; +4 vs 2026-04-29 PM = V3-EXQ-499/500/501/502
    Phase 2 cohort)**.
  - Pending review queue regenerated 2026-04-29T19:32Z: **5 items**
    (4 PASS V3-EXQ-499/500/501/502 + 1 FAIL V3-EXQ-490c carried over).
- **EXP-0174 env-complexity-gate proposal** added to manual_proposals.v1.json
  at 19:09Z (high-priority diagnostic targeted_probe for SD-016 / SD-023 /
  MECH-273 / MECH-275 testing whether enriched environments produce enough
  z_world information for SD-016 retrieval and sleep / self-model aggregation
  retests; experiment_proposals + index regenerated; no queue entry reserved
  or appended).

### Immediate Work Queue (This Cycle, 2026-04-30)

1. **Governance walk on the 5 pending review items** -- the 4 Phase 2
   cohort PASSes (V3-EXQ-499/500/501/502) now carry first-pass standard-
   gating experimental evidence for MECH-094 / SD-017 / SD-035 / MECH-062;
   re-score against the lit/exp decoupled regime (overall_confidence_decoupled
   = exp_conf) and check whether any quadrant flip is promotion-relevant.
   The V3-EXQ-490c FAIL remains pending discussion with successor V3-EXQ-490d
   already scoped.
2. **V3-EXQ-490d successor design + queueing** -- still the highest-priority
   substrate-validation run on the substrate side. Toggle
   use_vs_gate_staleness_lookup OFF vs ON at matched 0.4 thresholds,
   2 arms x 3 seeds, MECH-269b V_s gating ON + MECH-295 bridge ON in
   both arms. C4 severance acceptance criterion is the falsifiable test
   of the Q-040b strong reading after the 490c FAIL.
3. **V3-EXQ-495 V3-full-completion-gate queueing decision** -- still
   deferred. The MECH-163 dual-systems test depends on Q-040 / Q-040b
   resolution; queueing locked behind the EXQ-490d outcome.
4. **EXP-0174 env-complexity-gate scripting + queueing** -- the
   2026-04-29T19:09Z proposal is unblocking for SD-016 retest path
   (env-entropy precondition) plus sleep / self-model aggregation retests
   (MECH-273 / MECH-275). Manual_proposals entry reserved; script not
   yet written.
5. **OCD Layer 2 / 3 escalation (MECH-290 ablation; SD-046 multi-slot
   GoalState pull-forward)** -- still on the live escalation list after
   EXQ-498 disconfirmed Layer 1; design / queueing not yet started.
6. **Aggregator-floor flag governance review** -- 5th-consecutive-cycle
   flag at the next governance walk; cap-aware aggregator review with
   recommendation either (a) accept the floor as architecturally
   reasonable for narrow-open-question Q-claims, or (b) tune the floor
   downward to expose per-paper confidence variance more faithfully.

---

## Status Snapshot (2026-04-29 PM -- post-V3-EXQ-490c FAIL + Q-032 lit-pull + MECH-269b staleness wiring)

- **SDs / MECHs moved to Implemented since the 2026-04-29 nightly snapshot:**
  none in the substrate sense. One non-trivial wiring extension landed at
  06:03Z: **MECH-269b + MECH-284 staleness-into-VsRolloutGate wiring** (a
  Q-040b strong-reading enabler; effective_vs = raw_vs - staleness[s] under
  use_vs_gate_staleness_lookup, with HippocampalModule.compute_per_stream_staleness
  aggregating max-over-active-anchors-whose-stream_mixture-includes-stream).
  Bit-identical to legacy raw-V_s path when flag OFF; 8/8 contract tests
  PASS (191/191 full preflight + contracts). Successor V3-EXQ-490d can now
  drop the smoke-threshold override and exercise C4 severance
  (use_vs_gate_staleness_lookup OFF vs ON at matched 0.4 thresholds) as the
  falsifiable test of the strong reading.
- **Experiment activity since the nightly snapshot:**
  - **V3-EXQ-490c** (MECH-269b V_s gating + MECH-295 liking-bridge factorial;
    Q-040b behavioural sufficiency arm) **completed FAIL on Mac
    2026-04-29T08:34Z (~2.6h)**. Preliminary reading: under matched smoke-
    threshold overrides (0.85/0.85/0.95), MECH-269b ON + MECH-295 ON
    jointly do NOT recover approach_commit. Q-040b strong reading is NOT
    supported in this configuration. Pending review; governance decision
    pending.
  - Successor **V3-EXQ-490d** scoped (not queued): drop smoke-threshold
    override; toggle use_vs_gate_staleness_lookup OFF vs ON at matched 0.4
    thresholds in a 2-arm 3-seed factorial; C4 severance becomes the
    falsifiable test of whether MECH-284 staleness shifts effective_vs
    enough to fire the gate at biologically realistic V_s readings.
  - Runner-status totals refreshed: **568 completed (111 PASS / 245 FAIL /
    66 ERROR / 146 UNKNOWN; +1 vs nightly = V3-EXQ-490c)**.
  - Pending review queue regenerated 11:36Z: **1 item** (V3-EXQ-490c
    runner-only FAIL pending discussion).
- **Lit-pull progress 2026-04-29 (3 sessions, 15 entries):**
  - **AM (08:41Z) Q-029 + Q-030**: 5 entries each. Q-029 loneliness-as-
    ethical-harm-derivable-from-INV-029 lit_conf=0.875 (Holt-Lunstad x2,
    Wang 2023 Nat Hum Behav, Zajner/Bzdok UK Biobank, Eisenberger AnnRevPsych).
    Q-030 z_resource/z_world separation/fusion permutations lit_conf=0.874
    (Staresina PrC/PhC, Lee/Inah GIST, Howard/Kahnt OFC identity vs vmPFC
    value, Kim DG-disrupted spatial-object binding, Locatello Slot Attention).
  - **PM (11:19Z) Q-032**: 5 entries; PSG SWS/REM ratio as pharmacodynamic
    biomarker for sleep-medication dementia outcomes; lit_conf=0.839.
    Limb (a) PSG predicts dementia at the individual level: Himali 2023
    JAMA Neurol (Framingham within-person SWS-decline x 17y dementia HR
    1.27, 0.82); Winer/Mander/Walker 2020 Curr Biol (NREM SWA <1Hz
    forecasts AB accumulation with cross-metric specificity, 0.78);
    Suh 2019 J Alzheimers Dis (KLOSCAD short REM-per-cycle predicts MCI
    conversion at 4y, 0.62 exploratory). Limb (a)/(c) multi-metric
    architectural signature: D'Rozario 2020 Sleep Med Rev (10-study
    meta-analysis MCI fingerprint, 0.72). Limb (b)/(c) field treats PSG
    SWS as legitimate trial endpoint: Eyob 2024 J Alzheimers Dis (REST
    trazodone protocol, 0.45). Synthesis verdict: limb (a) well-supported;
    limb (c) PD-biomarker proposal architecturally defensible; limb (b)
    drug-class differential SWS preservation -> differential cognitive
    outcomes still empirically open pending REST results.
  - **Aggregator floor flag continues (4th consecutive cycle):** per-paper
    confidences 0.45-0.82 averaging ~0.68; claim-level lands 0.83-0.88.
    Floor effect now visible across Q-027/Q-028/Q-029/Q-030/Q-031/Q-032.
    Worth flagging at the next governance walk for cap-aware aggregator
    review.
- **Indexer state:** literature entries 1098 -> 1113 across the day's three
  lit-pull sessions (+15); claim_evidence.v1.json + evidence_backlog.v1.json
  regenerated 11:29Z.

### Immediate Work Queue (This Cycle, 2026-04-29 PM)

1. **V3-EXQ-490d successor design + queueing** -- the highest-priority
   substrate-validation run. Toggle use_vs_gate_staleness_lookup OFF vs ON
   at matched 0.4 thresholds, 2 arms x 3 seeds, MECH-269b V_s gating ON +
   MECH-295 bridge ON in both arms (inherits 490c stack). C4 severance
   acceptance criterion becomes the falsifiable test of the Q-040b strong
   reading after the 490c FAIL.
2. **V3-EXQ-490c review + governance decision** -- the run sits in the
   pending-review queue (1 item). Decision tree: classify as inconclusive
   pending V3-EXQ-490d, or accept FAIL as evidence against the strong
   reading and re-route Q-040b to ghost-goal / planning-arm hypotheses.
3. **V3-EXQ-495 V3-full-completion-gate queueing decision** -- still
   deferred. The MECH-163 dual-systems test depends on Q-040 / Q-040b
   resolution; queueing locked behind the EXQ-490d outcome.
4. **OCD Layer 2 / 3 escalation (MECH-290 ablation; SD-046 multi-slot
   GoalState pull-forward)** -- the EXQ-498 disconfirmation of OCD Layer
   1 leaves Layers 2 and 3 as the live escalation paths; design /
   queueing not yet started.
5. **SD-016 env-entropy precondition resolution** -- SD-016 remains parked
   pending env-entropy precondition; broader env-enrichment scoping work
   (CausalGridWorldV2 extension) not yet started.
6. **Aggregator-floor flag governance review** -- 5th-consecutive-cycle
   flag at the next governance walk; cap-aware aggregator review with
   recommendation either (a) accept the floor as architecturally
   reasonable for narrow-open-question Q-claims, or (b) tune the floor
   downward to expose per-paper confidence variance more faithfully.

---

## Status Snapshot (2026-04-29 -- nightly docs sync, post-2026-04-28 governance cycle)

- **SDs / MECHs moved to Implemented since the 2026-04-28 PM snapshot:** none.
  No new substrate landings; the day's activity was dominated by the
  2026-04-28T23:04Z governance cycle and a six-experiment diagnostic wave
  (V3-EXQ-498 OCD Layer 1 / V3-EXQ-418f-h SD-016 / V3-EXQ-490b MECH-269b)
  that produced no PASSing substrate signals but did shrink the open
  hypothesis space substantially.
- **Governance promotions / status changes 2026-04-28T23:04Z** (10 user-
  approved decisions across 20 walked items):
  - **4 promotions candidate -> provisional:** MECH-266 (asymmetric per-mode
    hysteresis), MECH-267 (mode-conditioned hippocampal proposals),
    MECH-268 (dACC conflict saturation), SD-034 (governance closure
    operator).
  - **SD-033b v3_pending true -> false** based on V3-EXQ-485 substrate-landing
    PASS UC1-UC5; status remains candidate (behavioural MECH-263
    devaluation + task-role discrimination signatures deferred to
    environment-extension EXQs).
  - **2 holds preserved** as `hold_pending_v3_substrate`: MECH-057b
    (hippocampal candidacy gate; functional signature deferred) and
    MECH-263 (OFC functional signatures; signatures (a)/(b) explicitly
    DEFERRED in V3-EXQ-485 manifest notes).
  - **6 narrow-open Q-claim evidence_quality_note refreshes** capturing
    the 2026-04-28 lit-pull cluster + 5th-consecutive aggregator-floor
    caveat: Q-025 / Q-026 / Q-027 / Q-028 / Q-031 / Q-040.
- **Manifest edits applied this cycle:**
  - V3-EXQ-485 (4 manifests) MECH-263 supports -> non_contributory per
    claim_ids accuracy rule (experiment tests SD-033b substrate wiring
    only; MECH-263 functional signatures explicitly deferred in
    manifest notes).
  - Replica supersession: kept canonical EXQ-484 (20260427T054449Z),
    EXQ-485 (20260427T054454Z), EXQ-493 (20260427T080304Z); marked
    4+3+2 deterministic re-runs evidence_direction='superseded' to
    avoid 5x/4x/3x over-weighting.
  - V3-EXQ-418g SD-016 does_not_support -> non_contributory (env-entropy
    precondition gap traced via EXQ-418f probe + EXQ-418h FAIL;
    substrate-side fixes work as designed but cue_context produces zero
    behavioural delta because z_world is near-constant batch-wise).
- **Diagnostic wave 2026-04-28 (6 experiments, all FAIL/UNKNOWN):**
  - **V3-EXQ-498** OCD Layer 1 closure-threshold sweep -- non_contributory.
    Layer 1 hypothesis (sweeping closure_rule_delta_threshold attenuates
    V3 baseline monostrategy) DISCONFIRMED. Escalates to Layer 2
    (MECH-290 ablation diagnostic) or Layer 3 (SD-046 multi-slot
    GoalState pull-forward).
  - **V3-EXQ-418f** SD-016 attention-uniformity probe -- diagnostic only.
    Localised the EXQ-418d/418e ln(16) uniform-rail bottleneck to query
    selectivity (not slot content): A2_div_only achieved
    slot_diversity=0.9999 but attn_entropy stayed at the uniform rail
    and contributed zero behavioural delta vs A0_off.
  - **V3-EXQ-418g** SD-016 selectivity-first 4-arm -- non_contributory.
    Substrate-side fixes (learnable temperature + entropy regulariser)
    work as designed: C1+C2+C3 PASS (B1/B3 attn_entropy=0.000, B2/B3
    slot_diversity=1.000). C4+C5 FAIL with action_class_entropy~1.1e-10
    IDENTICALLY across ALL FOUR arms because cue_context produces zero
    behavioural delta when z_world is near-constant across the batch
    (cos~0.998 in 418f).
  - **V3-EXQ-418h** env-entropy precondition probe -- FAIL. SD-023
    landmarks-on alone does NOT supply enough cross-context z_world
    variance under the current env (H1 cos_cross<0.95 not robust across
    seeds). Routes to broader env-enrichment scoping.
  - **SD-016 parked** pending env-entropy precondition. substrate_queue
    status: parked_pending_env_entropy_precondition. validation_experiment
    rerouted to EXQ-418h family pending broader env scoping.
  - **V3-EXQ-490b** MECH-269b VsRolloutGate substrate-readiness probe
    -- FAIL outcome under UNKNOWN result code, governance classified
    inconclusive. Q-040a effective PASS at threshold-overridden smoke
    (vs_gate_e1/e2_threshold=0.85, snapshot_refresh=0.95 so the gate
    fires under typical Phase 1 V_s dynamics). Q-040b stale-stream-
    discrimination FAIL points at MECH-295 drive->liking->approach
    bridge as the still-open dependency. The MECH-295 bridge landed
    2026-04-26 (V3-EXQ-493 PASS), so the successor combines
    MECH-269b VsRolloutGate ON with MECH-295 bridge ON in a single
    factorial. Successor EXQ pending design.
- **Lit-pulls landed 2026-04-28 (PM, 5 EVB-IDs from morning agenda):**
  16 new entries across MECH-025b (3) + MECH-172 (5, new dir) + Q-019 (2
  top-up; saturated dir) + INV-043 (3) + MECH-187 (3). Indexer rebuilt to
  1098 lit entries (+16). Post-rebuild: MECH-025b lit=0.82 (was 0.0);
  MECH-172 lit=0.894 (was 0.0); Q-019 lit=0.887 (~unchanged, saturated);
  INV-043 lit=0.841 (was 0.65); MECH-187 lit=0.863 / overall=0.829.
  Morning-agenda label drift flagged (4 of 5 mismatched between
  agenda's claim labels and resolved EVB-IDs); aggregator floor effect
  flagged for 5th consecutive cycle (per-paper 0.55-0.86 averaging
  ~0.74 but claim-level 0.82-0.89).
- **Pipeline state:** validate_claims --strict OK 68 invariants;
  claims.json rebuilt 571; index 915 runs / 482 types; pending_review
  0+0. Substrate queue 52 items (32 implemented + 2
  implemented_but_failing_validation + 1 parked + 17 pending/blocked).
  10 proposals flipped to executed across MECH-261/262/263/295/SD-033a/
  SD-033b/SD-034/MECH-266/267/268/Q-040.
- **Experiment count:** 567 runner-side completions per
  `runner_status.json` 2026-04-28T21:12Z read (111 PASS / 244 FAIL /
  66 ERROR / 146 UNKNOWN). +6 over the 2026-04-27 read covering the
  2026-04-28 diagnostic wave above.
- **Pending review:** 0 items per `pending_review.md` regenerated
  2026-04-28T23:11Z (was 15 at 2026-04-28T04:18Z). Cleared by the
  2026-04-28T23:04Z governance cycle.
- **Queue (`experiment_queue.json` 2026-04-29): 1 item, claimed by
  ree-cloud-2.**
  - **V3-EXQ-490b** completed 2026-04-28T21:09Z UNKNOWN/FAIL; awaiting
    queue cleanup. Governance-classified inconclusive; combined
    EXQ-490b/MECH-295 successor pending design.
  - **V3-EXQ-495** drafted but not yet queued. THE V3-full-completion
    gate run; queueing decision deferred until the EXQ-490b/MECH-295
    successor lands.
- **Current first-paper-gate bottleneck:** the EXQ-490b/MECH-295 combined
  successor is the next-up substrate-validation run. V3-EXQ-495 (V3 full-
  completion gate / MECH-163 hippocampally-planned arm) remains the
  headline first-paper-gate run. The EXQ-483 wired-but-inert pattern
  remains the open behavioural-recovery thread for the SD-037 / MECH-269b
  / MECH-295 cluster. SD-016 parked pending env-entropy precondition.
  OCD Layer 1 disconfirmed (escalation to Layer 2 / Layer 3).

---

## Status Snapshot (2026-04-28 PM — afternoon docs sync, lit-pull wave + queue refresh)

- **SDs / MECHs moved to Implemented since the 2026-04-28 nightly snapshot:** none.
  No new substrate landings between 01:21Z and 11:30Z; runner_status.json
  unchanged at 561 completions (109 PASS / 242 FAIL / 66 ERROR / 144 UNKNOWN
  per the 2026-04-27T08:04Z read).
- **Experiment count (per `runner_status.json` 2026-04-27T08:04Z):** 561 total
  (unchanged since morning). Pending review queue regenerated 2026-04-28T04:18:29Z
  carries **15 items** -- 12 PASS (V3-EXQ-484 / 485 / 493 across multiple
  machine/timestamp runs indexed after the 2026-04-27T14:55 /diagnose-errors
  run_id naming-bug fix) and 3 runner-only UNKNOWN entries for the same three
  queue IDs awaiting next governance walk. The queue grew from 6 at the
  2026-04-27T14:47:47Z regen because each per-machine/per-timestamp PASS now
  indexes as a distinct run; underlying queue IDs unchanged.
- **Lit-pull wave 2026-04-28 (5 pulls totalling 25 entries; medium-priority
  backlog largely closed):**
  - Q-031 (anticholinergic burden / dementia / REM-mediation): 5 entries, new
    dir `targeted_review_q_031/` (PM scheduled task, this snapshot). Gray 2015
    ACT cohort + Coupland 2019 QResearch (cumulative-dose limb both supports);
    Pase 2017 Framingham (REM% --> incident dementia, REM-specific not NREM);
    Kim & Jeong 1999 (transdermal scopolamine suppresses phasic REM, n=8 acute
    substrate); Grace-Vanstone-Horner 2014 J Neurosci mixed -- pontine SubC
    ACh blockade does NOT abolish REM; weakens strong pathway-1, suggests
    REM-theta integrity may be the right mediator rather than REM%.
    lit_confidence=0.87 (was not in claim_evidence map). **Q-031c
    mediation-analysis sub-question has no published direct test** -- flagged.
  - Q-027 / Q-028 (irreversible harm / axiom conflict): 5 entries (AM
    scheduled task; Sunstein 2006, Tarsney-Thomas-MacAskill 2024 SEP, IEP
    Precautionary, McConnell 2022 SEP, Williams 1965).
  - theta-abstraction-scaling: 5 entries -- new MECH claims registered:
    MECH-299 (theta_cycle_content_scales_with_substrate_vocabulary; V4 firm),
    MECH-300 (cognitive_map_traversal_at_active_abstraction_level; V4 firm),
    MECH-301 (waking_quiescent_replay_via_mech285_priority_sampling; V4
    default with V3 PULL-FORWARD CONDITION).
  - action-policy-decomposition: 5 entries (Mussa-Ivaldi 2000 / Daw 2005 /
    Graybiel 2008 / Botvinick 2009 / Dolan & Dayan 2013); synthesis verdict
    flags habit / action-chunk substrate (level 2-3 of biological
    decomposition) as missing in V3 -- highest-priority extension for OCD
    modelling and potential monostrategy contributor. Filed as candidate SD.
  - hpc-type-prototype: 5 entries (Quiroga 2005 / Schapiro 2017 / Schapiro
    2016 / Constantinescu 2016 / Hennies 2017). Verdict: parsimonious REE
    extension is a NEW INPUT PROJECTION onto existing AnchorSet machinery
    (Constantinescu shared-cognitive-map reading) plus an explicit
    prototype-readout operator running BOTH waking and sleep, NOT a fully
    separate codebook substrate.
- **Aggregator floor flag (recurring; third consecutive surfacing today):**
  per-paper confidences for low/medium-anchored Q-claims average 0.62-0.74
  but claim-level lit_confidence aggregates to 0.85-0.88 (Q-031 0.87;
  Q-027 0.66; Q-028 0.63 morning). Worth flagging next governance walk for a
  cap-aware aggregator review -- the floor effect is causing claim-level
  numbers to read as more lit-supported than the per-paper scoring intends.
- **Queue refresh (3 new diagnostics queued today, 2026-04-28):**
  - **V3-EXQ-498** OCD Layer 1 closure-threshold sweep (SD-034 parameter
    diagnostic; 4-arm × 3 seeds; psychiatric_failure_modes.md OCD section
    Layer 1 hypothesis test; PASS/FAIL routes to Layer 2 / Layer 3
    escalation). claim_ids=['SD-034']. ~60 min.
  - **V3-EXQ-418f** SD-016 attention-uniformity diagnostic probe (single-seed
    instrumentation of EXQ-418d/e ln(16) uniform-rail bottleneck). ~15 min.
  - **V3-EXQ-418g** SD-016 Path 4 query-selectivity-first 4-arm with new
    learnable temperature + attention-entropy loss substrate hooks landed
    2026-04-28; B0_off / B1_sel_only / B2_div_only / B3_sel_plus_div × 3
    seeds; tests Path 4 hypothesis that query selectivity (not slot content)
    is the bottleneck. ~90 min.
- **Current bottleneck unchanged:** V3-EXQ-495 (V3 full-completion gate /
  MECH-163 hippocampally-planned arm) is the headline run; V3-EXQ-490b is the
  smaller upstream factorial for Q-040a; V3-EXQ-498 is now the proximate
  short-runtime diagnostic that can land before the 25h V3-EXQ-495 budget
  decision.

---

## Status Snapshot (2026-04-28 — nightly docs sync, post-2026-04-27 substrate wave)

- **SDs / MECHs moved to Implemented since the 2026-04-27 morning snapshot:**
  - **SD-039 module-level write-site population layer**
    (`hippocampal.anchor_goal_payload_population`) -- the deferred follow-on
    to the SD-039 substrate. `REEAgent.sense()` builds `AnchorGoalPayload`
    once per tick from GoalState (z_goal_snapshot), ResidueField
    VALENCE_WANTING (wanting_strength), BLA arousal_tag,
    mean(per_stream_vs) (last_vs), max staleness_accumulator
    (staleness_at_write), and threads it through both
    `HippocampalModule.tick_anchor_set` (boundary-event write/remap path)
    and `apply_invalidation_broadcasts_to_regions` (MECH-287 broadcast
    invalidation refresh). MECH-094 simulation-mode gate at
    `build_goal_payload` returns None on replay/DMN paths.
    `REEConfig.from_dims(use_sd039_anchor_payload=...)` propagates to
    `AnchorSetConfig.use_sd039_anchor_payload`. V3-EXQ-494 6/6 PASS
    (UC1-UC6: module importable; master OFF no-op; population fires 7/7
    anchors with max goal_match 0.9999; dual-trace preservation 6 inactive
    + 1 active; falsifiable signature Phase A mean=0.0 vs Phase B
    mean=0.998 with 3/3 above 0.3; MECH-094 simulation gate replay-path
    zero anchors).
  - **MECH-292 ranked ghost-goal bank**
    (`hippocampal.unresolved_goal_ghost_bank`) -- pure-arithmetic derived
    view over the SD-039 dual-trace anchor pool. New module
    `ree_core/hippocampal/ghost_goal_bank.py` (GhostGoalBank,
    GhostGoalBankConfig, GhostGoalBankEntry). Ranking formula
    `ghost_priority = w_w*wanting + w_m*goal_match + w_s*staleness +
    w_r*recoverability` with `goal_match_floor=0.05` rumination guard
    (anchors with no payload OR goal_match below floor are invisible).
    Default pool: include_inactive=True, include_active=False. ValueError
    preconditions on `use_anchor_sets=True` AND
    `use_sd039_anchor_payload=True`. 6 sub-knobs surfaced through
    `REEConfig.from_dims`. V3-EXQ-496 5/5 PASS (UC1 module surface; UC2
    master OFF no-op; UC3 6 admitted entries with max_priority 1.609,
    monotone-decreasing; UC4 Phase A goal-inactive all below floor /
    Phase B goal-active admitted with goal_match component dominant on
    top entry; UC5 components sum to priority within float epsilon).
  - **MECH-293 waking ghost-goal probe search**
    (`hippocampal.awake_ghost_goal_probe_search`) -- read-side consumer
    of MECH-292. `HippocampalModule.propose_trajectories()` extended with
    a minority-budget ghost-seeded branch over the highest-priority bank
    entries' `anchor.z_world` rather than the agent's current `z_world`.
    Each ghost trajectory carries `hypothesis_tag=True` and metadata for
    downstream provenance routing; `record_committed_trajectory` strips
    the tag at commit boundary. `mech293_ghost_fraction=0.2` default;
    `mech293_replace_lowest_ranked=True` preserves total candidate
    count. ARC-007 strict preserved -- goal-match enters via MECH-292's
    external ranking, not a hippocampal value head. ValueError
    precondition on `use_mech292_ghost_bank=True`. V3-EXQ-497 5/5 PASS
    (UC1 module surface; UC2 master OFF n_ghost=0; UC3 ghost branch fires
    n_ghost_admitted=4 max_priority=1.61 mean_goal_match_at_seed=0.998
    reason='ok'; UC4 hypothesis_tag preserved on every ghost + 28
    value-flat candidates default-clean; UC5 budget-arithmetic
    clamp/cap/min-floor across 3 arms).
- **MECH-163 V3 full-completion-gate substrate prerequisites cleared.**
  All three substrate landings (SD-039 population layer, MECH-292,
  MECH-293) cleared 2026-04-27. V3-EXQ-495 (HABIT / PLANNED / ABLATED
  × A_DETOUR / B_NOVEL_CONTEXT × 7 seeds; THE V3-full-completion-gate
  metric: PLANNED-HABIT benefit-post-block gap >= 0.30 in detour, >= 4/7
  seeds) is queued and is now the headline run; ~25h on Mac / ~40h on
  ree-cloud-1; machine_affinity=any.
- **/diagnose-errors fixes 2026-04-27:**
  (1) V3-EXQ-484 / 485 / 493 run_id naming-bug fix: source scripts emitted
  run_id ending in raw timestamp instead of `_v3` suffix; sync_v3_results.py
  skipped them. Patched all three sources to construct run_id as
  `f"{experiment_type}_{ts}_v3"`; existing flat JSONs renamed + run_id
  field corrected; sync_v3 now picks them up cleanly; the 3 PASSes are
  now indexed pending awaiting next governance walk.
  (2) V3-EXQ-490 c1 gate-firing precondition root cause: VsRolloutGate's
  hold trigger (V_s < 0.4) is unreachable under typical Phase 1 V_s
  dynamics because the identity-prediction proxy stays near 0.9-1.0
  under aligned latents. Per user decision (smoke threshold-override
  path), queued V3-EXQ-490b (vs_gate_e1/e2_threshold=0.85,
  snapshot_refresh=0.95); claim_ids=['Q-040'] only (MECH-269b dropped
  because at smoke thresholds the gate fires regardless of stream
  staleness; skill rule 3 "err toward fewer tags"); supersedes
  V3-EXQ-490a. Q-040b (behavioural sufficiency) remains gated on Phase 2
  forward-predictor V_s OR a substrate change wiring `staleness_accumulator`
  into `VsRolloutGate.gate()`.
- **Lit-pulls landed 2026-04-27:** sequential sweep of 6 outstanding
  task_inbox lit-pulls (16 new entries across 6 claim directories) plus
  cowork-orchestrated 5-parallel lit-pull wave still in flight at snapshot
  time (EVB-0122 MECH-281, EVB-0123 Q-040, EVB-0124 SD-037, EVB-0125
  MECH-057, EVB-0126 MECH-263). SD-033a A2/A3 lit-pull resolution
  brought MECH-262 lit_conf to 0.884; SD-033a lit_conf 0.87.
- **Contracts suite:** 183/183 contracts + 7/7 preflight PASS with all
  flags OFF after the 2026-04-27 wave (was 164/164 + 7/7 on 2026-04-26
  before the wave). +12 MECH-293 contracts + remaining new SD-039
  population / MECH-292 / MECH-293 contracts. Bit-identical-when-OFF
  guarantee preserved across the entire wave.
- **Experiment count:** 561 runner-side completions per
  `runner_status.json` 2026-04-27T08:04Z read (109 PASS / 242 FAIL /
  66 ERROR / 144 UNKNOWN). +10 over the 2026-04-26 morning snapshot
  covering V3-EXQ-494 / 496 / 497 substrate-readiness PASSes plus
  V3-EXQ-484 / 485 / 493 PASS recovery after the run_id naming-bug fix.
- **Pending review:** 6 items per `pending_review.md` regenerated
  2026-04-27T14:47:47Z (3 PASS + 3 runner-only ERROR/UNKNOWN/smoke for
  V3-EXQ-484/485/493). The 2026-04-27T14:11 governance cycle walked 9
  indexed pending + 4 runner-only and applied: SD-039 / MECH-292 /
  MECH-293 substrate-readiness PASS clusters preserved as
  `hold_pending_v3_substrate` pending behavioural validation; V3-EXQ-433d
  SD-029 / MECH-256 reclassified `non_contributory`; V3-EXQ-418e SD-016
  keeps `does_not_support` on path-1 div_weight=0.5; V3-EXQ-490
  MECH-269b/Q-040 (×2 runs) reclassified `non_contributory`. Q-040
  narrowed: split into Q-040a (precondition) and Q-040b (behavioural
  sufficiency). Substrate queue: SD-039 status flipped to implemented;
  MECH-292 + MECH-293 added as implemented; MECH-269b added as
  implemented_but_failing_validation; SD-016 received V3-EXQ-418e
  failure_record. Index rebuilt to 898 runs / 474 types. Next
  governance cycle gates on V3-EXQ-490b + V3-EXQ-495 outcomes.
- **Queue (`experiment_queue.json` 2026-04-28): 2 items pending**, both
  unclaimed.
  - **V3-EXQ-495 pending** -- MECH-163 V3 full-completion gate; THE
    discriminative test for the VTA / hippocampally-planned arm of
    MECH-163 dual goal-directed systems. 3 conditions (HABIT value-flat
    proposals; PLANNED ghost-seeded proposals via MECH-293; ABLATED no
    goal anywhere) × 2 paradigms (A_DETOUR mid-episode blockage on the
    cached short corridor; B_NOVEL_CONTEXT cross-episode env swap to
    seed=137) × 7 seeds. P0 100ep encoder warmup + P1 100ep full
    pipeline + P2 50ep evaluation. Acceptance C1 (PLANNED ghost branch
    fires) + **C2 PLANNED-HABIT benefit-post-block gap >= 0.30 in detour,
    >= 4/7 seeds (THE V3-full-completion criterion)** + C3 (HABIT >=
    ABLATED in standard episodes) + C4 (PLANNED.prox_r2 >= 0.7) + C5
    (PLANNED.harm within 10% of HABIT). KL_PLANNED_HABIT first-step-
    action-distribution divergence recorded as diagnostic. Fishtank-viz
    per-step recording on FISHTANK_RECORD_SEED=42. machine_affinity=any;
    estimated_minutes=1500 (~25h Mac, ~40h ree-cloud-1).
  - **V3-EXQ-490b pending** -- MECH-269b VsRolloutGate substrate-
    readiness probe; Q-040a precondition; supersedes V3-EXQ-490a.
    Smoke-only threshold override (vs_gate_e1/e2_threshold=0.85,
    snapshot_refresh=0.95) so the gate fires under typical Phase 1 V_s
    dynamics. PASS confirms substrate wiring (Q-040a precondition);
    Q-040b (behavioural sufficiency) stays gated on Phase 2 forward-
    predictor V_s or a substrate change. claim_ids=['Q-040'] only.
    machine_affinity=any; estimated_minutes=320.
- **Current first-paper-gate bottleneck:** V3-EXQ-495 is the headline
  V3-full-completion-gate run -- all three substrate prerequisites
  cleared 2026-04-27, leaving only the runtime-budget decision. C2
  PLANNED-HABIT benefit-post-block gap is THE gate metric. V3-EXQ-490b
  is the smaller upstream factorial for Q-040a (MECH-269b substrate-
  wiring precondition only). The EXQ-483 wired-but-inert pattern
  remains an open thread for the SD-037 / MECH-269b / MECH-295 cluster:
  V3-EXQ-484 / 485 / 493 all cleared as substrate-readiness PASSes on
  2026-04-27 (post run_id naming-bug fix), validating SD-033a / SD-033b
  / MECH-295 substrate landings; behavioural recovery of approach_commit
  awaits the combined-cluster successor EXQ. Open promotion blockers
  documented in claims.yaml: MECH-294 within-cycle-vs-cross-cycle
  binding (Kay 2020 challenge); MECH-295 strong-vs-weak liking-bridge
  necessity (weak reading committed provisionally). SD-035 BLA
  hippocampal consumer wiring for retrieval_bias / remap_signal still
  deferred until V3-EXQ-474 behavioural signature confirmed.
- **Substrate queue completeness pass 2026-04-27T18:20Z** (post-
  reconcile): final state 52 queue items = 32 implemented + 3
  implemented_but_failing_validation + 17 genuinely-pending/blocked,
  after a back-fill pass added 13 entries that had landed in substrate
  but were absent from `evidence/planning/substrate_queue.json` (SD-034,
  SD-035, MECH-266, MECH-272, MECH-273, MECH-275, MECH-279, MECH-284,
  MECH-285, MECH-287, MECH-288, MECH-290, MECH-295). All entries carry
  full schema (title, design_doc, depends_on_unresolved, unblocks_claims,
  implementation_hint, priority, implementation_status, implemented_utc,
  implemented_session, validation_experiment, metric_trajectory).

---

## Status Snapshot (2026-04-27 — nightly docs sync, post-2026-04-26 substrate wave)

- **SDs / MECHs moved to Implemented since the 2026-04-26 morning snapshot:**
  - **SD-039 substrate** (`hippocampal.anchor_goal_snapshot_payload`) -- dual-trace
    `AnchorGoalPayload` dataclass (z_goal_snapshot + wanting_strength + arousal_tag
    + last_vs + staleness_at_write + payload_written_step) + refresh-on-invalidate
    semantic preserving payload across `mark_inactive` + `Anchor.goal_match` cosine
    helper + `AnchorSet.query_by_goal_match` active+inactive dual-trace getter for
    the MECH-292 consumer. Module-level write-site population (from GoalState /
    VALENCE_WANTING / amygdala arousal tags) + V3-EXQ-494 falsifiable validation
    deferred to a follow-on session. 10/10 contract tests S1-S10 PASS.
  - **SD-033b** (`pfc.ofc_analog`) -- OFC-analog as MECH-261 second consumer.
    Gate-modulated EMA `state_code [1, state_dim]` with eff_eta = update_eta *
    write_gate("sd_033b"); zeroed-last-Linear bias head -> initial bias exactly
    zero; per-mode gate weights external_task=1.0 / internal_planning=0.5 /
    internal_replay=0.05 / offline_consolidation=0.3. Behavioural MECH-263
    signatures (devaluation, same-sensory / different-task-role discrimination)
    deferred to env-extension EXQs. V3-EXQ-485 5-sub-test landing diagnostic
    smoke PASS.
  - **MECH-269b** (`cortical_world_model.regional_verisimilitude_rollout_gating`)
    -- read-side consumer of MECH-269 Phase 1 `per_stream_vs` at the E1
    `_e1_tick` site (before total_state cat / e1(...) call / extract_cue_context)
    and the per-tick E2_harm_a forward call site. Held substitution swaps
    current latent for snapshot when V_s[s] < per-side threshold (default 0.4
    on both sides; refresh threshold 0.5; 0.4-0.5 dead-band Schmitt-trigger
    hysteresis). Precondition use_per_stream_vs=True (raises ValueError
    otherwise). Q-040 factorial validation queued as V3-EXQ-490.
  - **MECH-295 weak-reading bridge** (`regulators.mech295_liking_bridge`) --
    drive -> liking-stream -> approach_cue substrate. Two integration sites:
    (a) `update_z_goal()` writes anticipatory liking pulse to VALENCE_LIKING
    at the GOAL location (NOT current z_world), distinct from update_liking()
    consummatory; (b) `select_action()` reads per-candidate goal_proximity,
    computes drive*proximity, negates (E3 lower-is-better), composes
    additively with dacc_score_bias before e3.select(). Severed-bridge
    falsification arm at cue gain=0; weak-necessity reading committed
    provisionally. V3-EXQ-493 6-sub-test diagnostic (incl. UC5 SEVERED-BRIDGE
    COLLAPSE) smoke PASS.
- **Architectural commitments registered 2026-04-26:**
  - **ARC-054 v4 -> v3 promotion** -- D_V trajectory selection promoted in
    rollout-horizon synaptic-EMA form (no TCL substrate dependency at V3);
    V4 form (phase-coherent V(t) integration via ARC-053 + MECH-225/226/228)
    remains v4-by-design. Design doc:
    `docs/architecture/dv_temporal_depth_v3_form.md`. V3-EXQ-491 validation queued.
  - **MECH-271 V3 substrate plan** -- hypothesis tag as downstream routing
    committed for V3 in synaptic form (discrete routing table + audit hook for
    confabulation-vs-psychosis dissociation); V4 ephaptic-field-strength
    routing remains v4-by-design. Plan doc:
    `docs/architecture/mech_271_routing_v3_substrate_plan.md`. V3-EXQ-492
    routing 4-arm queued behind the MECH-269b lock release.
  - **V3/V4 phase substrate boundary memo** added directly above this snapshot
    enumerating the architectural deferral table -- ARC-053 / MECH-225 /
    MECH-226 / MECH-227 / MECH-228 / MECH-270 stay v4-by-design, the imaginary-
    plane / phase-channel deferral question is open, and the conditions under
    which a V4 promotion revisit triggers are documented.
- **New claims registered 2026-04-26 (cingulate cluster lit-pull pass):**
  MECH-294 (theta-burst multi-content packet; Kay 2020 cross-cycle alternation
  flagged as direct architectural challenge -- explicit promotion blocker),
  MECH-269b (symmetric V_s gating; Q-040 factorial parent), MECH-295
  (drive-amplified liking-stream as approach-cue bridge; weak provisional
  reading), Q-040 (V_s-generalisation-necessary-for-dACC question).
- **Lit-pulls landed 2026-04-26:** targeted_review_mech294_theta_burst_packet
  (7 entries, sparse-but-not-falsifying), targeted_review_mech269b_vs_rollout_
  gating (7 entries, mean conf 0.69; symmetric-application novelty flagged),
  targeted_review_mech295_liking_approach_bridge (6 entries, mean conf 0.77;
  strong-vs-weak necessity flagged for user resolution). Plus 5 MECH-280
  literature_evidence/v1 entries written into the existing
  targeted_review_sd_037_orexin_kinetics/ folder (de Araujo Salgado 2023
  Neuron, Marino 2020 PNAS, Johnson 2012 Prog Brain Res, Sakurai 2014 NRN,
  Mileykovskiy 2005 Neuron); MECH-280 lit_conf 0 -> 0.878. Plus
  targeted_review_ghost_goal_search (7 entries) -- the seed for SD-039 /
  MECH-292 / MECH-293 / ARC-060 registration earlier in the day.
- **Contracts suite:** 164/164 contracts + 7/7 preflight PASS with all flags
  OFF after the 2026-04-26 wave (was 150/150 + 7/7 on 2026-04-25 before the
  wave). Bit-identical-when-OFF guarantee preserved across SD-039 substrate
  + SD-033b + MECH-269b + MECH-295.
- **Experiment count:** 551 runner-side completions per `runner_status.json`
  2026-04-26 read (109 PASS / 241 FAIL / 66 ERROR / 135 UNKNOWN; v3 subset
  93 PASS / 228 FAIL / 66 ERROR / 135 UNKNOWN). +1 over the 2026-04-26
  morning snapshot.
- **Pending review:** 0 items as of `pending_review.md` regenerated
  2026-04-26T16:19:34Z (down from 1 on the 2026-04-26 morning snapshot). The
  2026-04-26T15:39 governance cycle reclassified V3-EXQ-483a manifest
  `supports -> non_contributory` per-claim (SD-037 / MECH-280 / MECH-281
  remain `hold_pending_v3_substrate`); same wired-but-inert pattern as the
  V3-EXQ-471 / 478 / 480 cluster. 9 `hold_pending_v3_substrate` decisions
  applied via apply_decision_batch.py: ARC-051, ARC-060, MECH-269b, MECH-291,
  MECH-292, MECH-293, MECH-294, MECH-295, SD-039.
- **Queue (`experiment_queue.json` 2026-04-27): 6 items**.
  - **V3-EXQ-433d in flight** -- SD-029 / MECH-256 event-conditioned
    comparator with the EXQ-479 calibrated curriculum (interval=10,
    num_hazards=2, hazard_harm=0.02, adjacent_only=True); STEPS_PER_EP
    bumped 120 -> 200; supersedes V3-EXQ-433c. Auto-claimed by
    `DLAPTOP-4.local` 2026-04-26T15:01Z.
  - **V3-EXQ-418e pending** -- SD-016 Path 1 4-arm
    A0_off / A1_writes_only / A2_div_only / A3_writes_plus_div ablation;
    supersedes V3-EXQ-418d.
  - **V3-EXQ-484 pending** -- SD-033a distractor-resistance under MECH-261
    internal_replay gate; 3-arm deterministic at the SalienceCoordinator +
    LateralPFCAnalog interface (no agent loop). Smoke PASS 2026-04-26.
  - **V3-EXQ-485 pending** -- SD-033b OFC-analog landing diagnostic;
    5 sub-tests paralleling EXQ-456. Smoke PASS 2026-04-26.
  - **V3-EXQ-490 pending** -- MECH-269b symmetric V_s gating
    substrate-readiness diagnostic; Q-040 factorial ON_OFF vs ON_ON arms
    with use_broadcast_override + use_dacc + drive_weight=2.0 + full V_s
    invalidation circuit + use_vs_commit_release ON; only manipulated
    variable is use_vs_rollout_gating. ~50-55 min/arm.
  - **V3-EXQ-493 pending** -- MECH-295 weak-reading bridge validation;
    6 sub-tests including UC5 SEVERED-BRIDGE COLLAPSE falsifiable signature.
    Smoke PASS 2026-04-26.
- **Current first-paper-gate bottleneck:** V3-EXQ-490 + V3-EXQ-493 jointly
  dissect the EXQ-483 wired-but-inert pattern. Q-040 factorial dispatches:
  V3-EXQ-490 PASS (gate fires AND approach_commit recovery AND non-zero
  dacc_score_bias) -> cortical-side V_s gating dominates and SD-037 reopens.
  V3-EXQ-490 FAIL on C2/C3 with C1 PASS -> evidence redirects at MECH-295
  as the dominant blocker. V3-EXQ-493 separately validates the liking-bridge
  mechanism + the severed-bridge collapse falsification. Both PASS -> joint
  contribution and a combined-cluster behavioural EXQ follows. V3-EXQ-433d
  gates the SD-003 successor track; V3-EXQ-418e gates the SD-016
  cue_action_proj forward-path re-validation. Open promotion blockers
  documented in claims.yaml: MECH-294 within-cycle-vs-cross-cycle binding
  (Kay 2020 challenge); MECH-295 strong-vs-weak liking-bridge necessity
  (weak reading committed provisionally). SD-035 BLA hippocampal consumer
  wiring for retrieval_bias / remap_signal still deferred until V3-EXQ-474
  behavioural signature confirmed.
- **Governance:** Mid-day governance cycle 2026-04-26T15:39 walked 1 indexed
  pending (V3-EXQ-483a) and applied the 9 `hold_pending_v3_substrate`
  decisions listed above. SD-037 substrate_queue refreshed with
  implementation_status `implemented_but_failing_validation` and a
  cross-pointer to MECH-295 as the likely root cause; SD-039 added as a new
  ready substrate-queue entry (ghost-goal anchor payload). Predecessor
  V3-EXQ-483 manifest reclassified `non_contributory -> superseded`. Index
  rebuilt to 889 runs / 468 types. Next governance cycle gates on
  V3-EXQ-490 + V3-EXQ-493 outcomes.

---

## V3/V4 Phase Substrate Boundary -- Architectural Commitment (2026-04-26)

The V3 working-model uses a **synaptic approximation** of regional verisimilitude (V_s),
its temporal-depth integration (D_V), its routing realisation (MECH-271), and its fast-
broadcast invalidation (MECH-287). The full phase-channel substrate -- ARC-053 Temporal
Coherence Loop, MECH-225 oscillatory cross-frequency multiplexing, MECH-226 TCL biophysical
substrate (inferior olive + cerebellum + thalamus + cortex), MECH-228 ephaptic field-level
coherence support, MECH-227 anaesthesia-collapse model, MECH-270 ephaptic substrate of V_s
-- stays **v4-deferred by architectural commitment, not by substrate prerequisite**.

The architectural bet: the synaptic V3 form is **sufficient for V3 working-model deliverables**
(closed-loop agent with V_s invalidation runtime, D_V-aware rollout selection, hypothesis-
tag-as-routing). The V4 phase substrate **refines, not replaces**, the V3 form.

**Two v4-held claims have V3 forms landing now**:

- **ARC-054** (D_V trajectory selection) -- V4 form (phase-coherent V(t) integration)
  remains v4. **V3 form** (rollout-horizon synaptic EMA over V_s readout) promoted to
  v3 2026-04-26. Design doc: `docs/architecture/dv_temporal_depth_v3_form.md`.
- **MECH-271** (hypothesis tag as downstream routing) -- V4 form (phase-channel routing
  via ephaptic field strength) remains v4. **V3 substrate landing plan** committed
  2026-04-26: discrete routing table + audit hook for confabulation-vs-psychosis
  dissociation. Plan doc: `docs/architecture/mech_271_routing_v3_substrate_plan.md`.

Full V4 deferral table, what the synaptic forms cover and don't cover, the imaginary-
plane (phase-channel) deferral question, and the conditions under which a V4 promotion
revisit triggers: `docs/architecture/v3_v4_phase_substrate_boundary.md`.

Governance hook: the v4-held claims currently produce `hold_pending_v3_substrate`
recommendations, which is incorrect labelling for these specifically -- they are
v4-by-design, not v4-by-prerequisite. A separate governance-tooling session should add
a `held_v4_by_architectural_commitment` recommendation type that reads from the boundary
doc.

---

## Status Snapshot (2026-04-26 — nightly docs sync, post-2026-04-25 substrate wave)

- **SDs moved to Implemented since the 2026-04-25 snapshot:**
  - **SD-037** (`regulators.broadcast_override`) -- orexin/hypocretin-analog
    BroadcastOverrideRegulator. Scalar `override_signal` in [0,1] driven by
    SD-012 `drive_level` + sustained-threat rolling-window magnitude over
    `z_harm`, EMA-smoothed. Consumed at three sites: PAG freeze-gate
    `exit_threshold` scaled by `(1 + alpha_override * override_signal)`;
    SalienceCoordinator `update_signal("override_signal", ...)` biases
    operating-mode aggregate toward `external_task`; GoalState seeding
    amplified `effective_drive *= (1 + (override_goal_seeding_gain - 1) *
    override_signal)`. MECH-094 simulation_mode gate: `tick(simulation_mode=
    True)` returns cached signal unchanged. Failure-mode predictions:
    PWS-hyperphagia analog (saturated override -> >=2x approach-commit
    rate); narcolepsy/cataplexy analog (lost override -> <30% approach-
    commit); catatonic lock-in escape (raises PAG exit_threshold under
    sustained drive+harm).
  - **Sleep Aggregation Cluster Phase A** (`SleepLoopManager` scaffolding) --
    wraps the existing SD-017 surface (`run_sleep_cycle` / `enter_sws_mode`
    / `run_sws_schema_pass` / `enter_rem_mode` / `run_rem_attribution_pass`
    / `exit_sleep_mode`). New `SleepPhase` enum (6 phases: WAKING /
    SLEEP_ENTRY / SWS_ANALOG / PHASE_SWITCH / REM_ANALOG / WRITEBACK) +
    `SleepCycleState` dataclass. Master flag `use_sleep_loop` (default
    False) + `sleep_loop_episodes_K` (default 1) + `sleep_loop_require_
    passes` (default True). `notify_episode_end()` hooked at start of
    REEAgent.reset() so sleep operates on the final waking state.
  - **MECH-285 Sleep Phase B** (`sleep.replay_sampler`) -- SleepReplaySampler.
    At SLEEP_ENTRY freezes `StalenessAccumulator.snapshot()`, then draws N
    seeds from `AnchorSet.all_with_dual_trace()` (active + inactive,
    Bouton 2004 dual-trace preserved) with `softmax(staleness/temperature)`
    priority. Stateless within cycle; uniform-fallback when no accumulator.
    Phase B is no-op consumer -- draws land in `mech285_*` metrics only.
  - **MECH-272 Sleep Phase C** (`sleep.routing_gate`) -- RoutingGate. State-
    conditioned channel weights `{anchor_channel, probe_channel}` flipping
    across SWS_ANALOG / REM_ANALOG / WAKING rows per the design-doc table.
    Per-draw `RoutedEvent`s surfaced as `mech272_*` cycle metrics.
  - **MECH-275 Sleep Phase D** (`sleep.bayesian_aggregator`) -- BayesianAggregator.
    Per-domain per-region Gaussian posteriors over residuals; conjugate
    mean-and-variance update gated by `RoutedEvent.probe_channel *
    probe_gain` (probe<=0 skipped, counted as `mech275_n_skipped_zero_
    probe`). Snapshot+decay contract: `snapshot()` deep-copies live
    posteriors at PHASE_SWITCH (frozen pre-REM); `decay_factor` multiplies
    live variance per cycle. Place-domain default with `(scale, segment_
    id)` region key matching MECH-284.
  - **MECH-273 Sleep Phase E** (`sleep.self_model_writeback`) -- SelfModel
    Aggregator subclass of MECH-275 specialised on SD-003 `causal_sig`
    posterior. `offline_gradient_pass(e2_harm_s, replayed_regions, n_steps,
    domain='self', use_snapshot=True)` reads posterior means from
    `last_snapshot` (SWS-only frozen copy at PHASE_SWITCH); constructs
    synthetic batch at E2_harm_s input dims; trains via Adam at
    `waking_lr * offline_lr_scale` for n_steps bounded MSE steps.
    MECH-094 exception scoped: optimiser constructed locally over
    `e2_harm_s.parameters()` only -- no other module's params touched.
    NEW API: `StalenessAccumulator.partial_decay(replayed_regions,
    decay_factor=0.5)` multiplicatively decays only supplied region keys
    (clamped, drops below `drop_epsilon`).
  - **SD-016 Path 1** (`e1.context_memory_diversification_loss`) -- auxiliary
    mean-squared-off-diagonal-cosine loss on normalised ContextMemory
    slot vectors. Provides gradient pressure for slot symmetry-breaking
    missing in EXQ-418d 4-arm writepath ablation (FAILed across all
    arms with `attn_entropy_mean ~2.76` near uniform reference 2.7726
    and bimodal seed pattern: seed 42 ~0.46 div, seeds 43/44 collapse
    <1e-4). Smoke verified `slot_div` climbs 0.2->0.5->1.0 across arms;
    new `sd016_diversification_weight` config wired through E1Config +
    REEConfig.from_dims (default 0.0 -- backward compatible).
- **Contracts suite:** 150/150 PASS (143 contracts + 7 preflight) with all
  flags OFF after the 2026-04-25 wave (was 91/91 contracts + 7 preflight
  before the wave). Bit-identical-when-OFF guarantee preserved across
  SD-037 + 5 sleep phases + SD-016 Path 1.
- **Experiment count:** 550 runner-side completions per `runner_status.json`
  2026-04-26 read (108 PASS / 241 FAIL / 66 ERROR / 135 UNKNOWN; v3 subset
  92 PASS / 228 FAIL / 66 ERROR / 135 UNKNOWN). +5 completions over the
  2026-04-25 snapshot.
- **Pending review:** 1 item as of `pending_review.md` regenerated
  2026-04-26T00:44:10Z (down from 13 on the 2026-04-25 snapshot). The
  remaining item is V3-EXQ-483 FAIL whose successor V3-EXQ-483a is in
  flight.
- **Queue (`experiment_queue.json` 2026-04-26): 2 items**.
  - **V3-EXQ-483a in flight** -- SD-037 broadcast-override 4-arm with
    WARMUP_EPISODES=200 + substrate-readiness fallback acceptance;
    supersedes V3-EXQ-483. Auto-claimed by `DLAPTOP-4.local`
    2026-04-25T23:29Z. EXQ-483 confirmed substrate-readiness
    (override 0.0 -> 0.56 mean / 0.62 max in ON arms; PAG releases
    5.3 -> 9.0-9.3) but behavioural metrics were uninterpretable
    because `approach_commit=0.0` in ALL arms including the
    SD-036-only baseline. Two changes: (1) `WARMUP_EPISODES 60 -> 200`
    to give baseline arm enough exposure to potentially produce
    non-zero approach behaviour; (2) acceptance logic adds substrate-
    readiness fallback path used only when baseline arm yields no
    behavioural signal (override_mean > 0.30 AND PAG release ratio
    ON_ON/ON_OFF > 1.30). Behavioural path remains preferred when
    baseline is non-zero.
  - **V3-EXQ-418e pending** -- SD-016 Path 1 4-arm A0_off / A1_writes_only
    / A2_div_only / A3_writes_plus_div ablation; supersedes V3-EXQ-418d.
    Acceptance C1 `attn_entropy<2.65` AND C2 `div>0.10` ALL 3 SEEDS AND
    C3 behavioural delta `>=0.20` AND C4 A1 replicates 418d FAIL. C2
    raised from 2/3 to 3/3 because 418d showed bimodal seed pattern --
    substrate-level fix must escape collapse on every seed.
- **Current first-paper-gate bottleneck:** V3-EXQ-483a SD-037 validation
  (in flight) gates the orexin-analog failure-mode signature -- PWS-
  hyperphagia (saturated override -> >=2x approach-commit), narcolepsy/
  cataplexy (lost override -> <30% approach-commit), and the V3-EXQ-471
  catatonic-lock-in escape signature. V3-EXQ-418e SD-016 Path 1 validation
  is the parallel SD-016 cue_action_proj design-rethink resolution path
  -- if Path 1 lifts the bimodal seed pattern across all 3 seeds, the
  diversification-loss substrate is the answer; if it does not, deeper
  ContextMemory write-architecture redesign is required. SD-032 cluster
  behavioural follow-through remains the primary cingulate-track blocker
  (V3-EXQ-445a/b/c FAILed; V3-EXQ-325d FAILed with zero between-arm
  gradient on the SD-032c AIC-analog descending-modulation arm); the
  cluster awaits the next governance cycle pass.
- **Governance:** No governance cycle run in this nightly window. Next
  cycle should ingest V3-EXQ-483a + V3-EXQ-418e outcomes, the SD-035 /
  MECH-266 landings, and the 2026-04-24 + 2026-04-25 substrate waves.

---

## Status Snapshot (2026-04-25 — nightly docs sync, post-Phase-3 wave)

- **SDs moved to Implemented since the 2026-04-24 snapshot:**
  - **MECH-284 Phase 3** (`hippocampal.staleness_accumulator`) -- region-indexed
    staleness with per-tick leak (default `leak_factor=0.995`), attribution_mode
    `equal` / `stream_overlap`, `staleness_clip=1.0`, `lookup_by_anchor_key`
    getter consumed by MECH-269 online hysteresis. Integration site:
    `HippocampalModule.tick_anchor_set` peek-not-drains the
    `_broadcast_event_queue` so MECH-287 broadcast events propagate
    transparently.
  - **MECH-269 online hysteresis swap** (`AnchorSet.tick_hysteresis` accepts
    optional `staleness_lookup`; orthogonal flag `use_mech284_hysteresis`,
    default OFF). With both flags ON, `V_s_anchor = V_s(r) - staleness[r]`
    drives anchor-reset; default OFF preserves the Phase 2 internal proxy
    so the substrate is non-invasive.
  - **MECH-290** (`hippocampal.backward_trajectory_credit_sweep`) -- Foster &
    Wilson 2006 reverse replay. `record_committed_trajectory` at BetaGate
    elevation; `backward_credit_sweep` at completion-signal release;
    per-step credit = `outcome_quality * gamma^(T-1-t)` ->
    `ResidueField.update_valence(VALENCE_WANTING)`. Reset on episode
    boundary.
- **Contracts suite:** 91/91 PASS with all flags OFF (was 85/85 before the
  Phase 3 wave); preflight 7/7 PASS; bit-identical to the pre-Phase-3 HEAD
  with master switches off. Activation smokes -- ARM0/1/2 for MECH-284 and
  end-to-end direct-wiring tests for MECH-290 -- all PASS 2026-04-24.
- **Experiment count:** 545 runner-side completions per
  `runner_status.json` 2026-04-25 read (108 PASS / 239 FAIL / 66 ERROR /
  132 UNKNOWN; v3 subset 88 PASS / 226 FAIL / 64 ERROR / 132 UNKNOWN).
  Indexer carries 881 indexed runs as of the 2026-04-24 cowork rebuild;
  indexer-vs-runner gap is the historical pre-runner_status archive plus
  per-seed manifests collapsed to single queue entries. Next indexer
  rebuild is gated on V3-EXQ-478 returning.
- **Pending review:** 13 items as of `pending_review.md` regenerated
  2026-04-24T11:54:11Z (down from 25 on the 2026-04-23 snapshot;
  cowork-a wave reviewed V3-EXQ-433c / 449b / 447a and resolved several
  unknowns).
- **Queue:** EMPTY (`experiment_queue.json` `items: []` as of
  2026-04-25T01:14Z). Active waterfall:
  - **V3-EXQ-478 in flight** -- MECH-284 Phase 3 validation diagnostic,
    OFF vs ON x 2 seeds; metrics `freeze_recommit_count`,
    `anchor_reset_count`, `mean_staleness_peak`, `action_class_entropy`.
    Auto-claimed by `DLAPTOP-4.local` 2026-04-24T13:22Z; runner_status
    carries it as UNKNOWN pending completion. PASS unlocks the
    previously gated V3-EXQ-445d / 449c / 455a / 476 cascade. FAIL
    forces a Phase 3 redesign before the cascade proceeds.
  - **V3-EXQ-479 next-up** -- SD-029 fix2 superseding 470a; queued by
    cowork-2026-04-24-a with the curriculum / agent-caused-elicitation
    correction.
  - V3-EXQ-476 / 476a / 476b returned ERROR/UNKNOWN before MECH-284
    Phase 3 was available; 476a and 476b queued in
    `discussed_experiment_dirs` for review.
  - V3-EXQ-449c / 445d / 455a all errored under the pre-MECH-284
    substrate and await V3-EXQ-478 PASS before re-queueing.
  - V3-EXQ-418c remains needs_user_review (SD-016 cue_action_proj
    design rethink open, anchored on the 2026-04-24 V3-EXQ-477
    `key_proj.bias` dominance diagnosis).
  - V3-EXQ-137 FAILed 2026-04-24T02:21Z (MECH-097 PPS commit locus,
    instrumentation-fix); V3-EXQ-477 FAILed 2026-04-24T08:06Z (SD-016
    ContextMemory slot-store / attention-uniformity diagnostic).
- **Current first-paper-gate bottleneck:** V3-EXQ-478 (MECH-284 Phase 3
  validation, in flight) gates the V_s-gated cascade. SD-032 cluster
  behavioural follow-through remains the primary cingulate-track blocker
  (V3-EXQ-445a / 445b / 445c all FAILed; V3-EXQ-325d FAILed with zero
  between-arm gradient on the SD-032c AIC-analog descending-modulation
  falsification signature; V3-EXQ-454 FAILed on ARC-016 adaptive
  commitment_threshold). SD-016 cue_action_proj forward-path is now in
  the design-rethink anchor (V3-EXQ-477 FAIL diagnosed `key_proj.bias`
  dominance as the substrate-level problem), gating V3-EXQ-418c.
  Governance-cycle pass remains pending for the SD-032 behavioural
  FAILs, the SD-035 / MECH-266 landings, the V_s invalidation runtime
  substrate landings, and the 2026-04-24 Phase 3 wave.

---

## Status Snapshot (2026-04-24 — nightly docs sync, queue refresh)

- **No new SDs or governance decisions this session** (nightly docs-only sync
  following experiment queue refresh by PM session 2026-04-23).
- **Queue refresh:** queue grew from the 2026-04-23 PM snapshot's "3 claimed
  items" (V3-EXQ-447 / 451 / 445a -- all since cleared) to **6 items (1 claimed,
  5 pending)**:
  - **V3-EXQ-476** (pending, priority 70, `diagnostic`) -- MECH-269 V_s
    validation entropy probe, cascade gate for the V_s-gated cascade track
    (EXQ-445d / EXQ-449c / EXQ-455a). Baseline agent + V_s flags ON vs OFF;
    measure action_class_entropy. PASS = ON entropy > OFF entropy by >=0.1
    in >=2/2 seeds. Queued 2026-04-24 -- this is the end-to-end validation
    item that the 2026-04-23 snapshot flagged as "planned but not yet queued"
    for the 2026-04-22 V_s invalidation runtime substrate wave.
    FAIL/INCONCLUSIVE means MECH-284 Phase 3 consumer must land before
    downstream cascade can run.
  - **V3-EXQ-449c** (pending, priority 50, `evidence`, 150 min) -- MECH-074b
    BLA retrieval bias V_s-gated ablation; `depends_on: V3-EXQ-445d`. PASS =
    action_class_entropy ON - OFF >= 0.1 AND harm_rate reduced in >=2/3 seeds.
  - **V3-EXQ-433c** (**claimed DLAPTOP-4.local 2026-04-23T23:23:48Z**,
    priority 55, `evidence`, 90 min) -- SD-029 event-conditioned MECH-256
    comparator with curriculum ON + scripted agent-caused elicitation;
    supersedes V3-EXQ-433b. Fix: SD-029 curriculum enabled in P0 / P1 / eval
    (scheduled_external_hazard_enabled=True, interval=25, prob=1.0,
    adjacent_only=False); deterministic move onto an adjacent hazard when
    trials_collected['agent_caused_hazard'] is short; C0 sufficiency gate
    (n_agent / n_env >= 20 in >=3/4 seeds). If C0 fails, outcome=FAIL but
    per-claim evidence_direction='inconclusive_insufficient_events' (not
    'weakens') so governance scores are not corrupted by a trials-shortage
    run. Re-opens the SD-003 successor track.
  - **V3-EXQ-449b** (pending, priority 52, `diagnostic`, 30 min) -- SD-016
    cue_action_proj consumer fix verification (z_world residual concat);
    supersedes V3-EXQ-449a. EXQ-449a localised the collapse to a
    uniform-attention bottleneck inside extract_cue_context (ContextMemory
    slots init at randn*0.01 so key_proj's bias dominates; all keys look
    identical; softmax = uniform entropy 2.7726; bmm(uniform, v) constant
    across batch -> cue_context constant -> cue_action_proj output had
    per-channel std ~2.7e-8 in g2). Fix (predictors/e1_deep.py): cue_action_proj
    input changed from `cue_context` alone (latent_dim=64) to
    `[cue_context, z_world]` (concat, latent_dim+world_dim=96). cue_terrain_proj
    left unchanged. Same three-regime protocol as 449a (g1 supervised-active,
    g2 frozen, g3 detach-bypassed); acceptance pivots from "find the offender"
    to "verify the offender is gone". Smoke-test 2026-04-23 dry-run (P0=2
    P1=3 eval=4 ep): g2 per-channel std = 2.957e-3, primary_pass=True.
    Unblocks V3-EXQ-418c.
  - **V3-EXQ-418c** (pending, priority 50, `evidence`, 60 min) -- SD-016+SD-017
    context-conditioned action with cue_action_proj consumer fix active;
    supersedes V3-EXQ-418b. Re-run of EXQ-418a using the SAME script (fix is
    upstream in e1_deep.py and activates automatically when sd016_enabled=True,
    which 418a already sets). EXQ-418/418a/418b all FAILed three times with
    action_bias_divergence=0.0 under the broken substrate.
  - **V3-EXQ-137** (pending, priority 40, `evidence`, 180 min) -- MECH-097
    PPS commit locus: PPS_LOCUS_ON vs ABLATED, backlog EVB-0137.
    Instrumentation fixed 2026-04-24 (verdict print, outcome field,
    timestamp_utc, EXPERIMENT_PURPOSE); smoke-test PASS.
- **Experiment count:** 844 runs (indexer rebuilt 2026-04-23 PM; runner_status.json
  last_updated 2026-04-23T20:23:18Z, 527 runner-side completions: 235 FAIL /
  108 PASS / 62 ERROR / 122 UNKNOWN; no new completions in runner_status.json
  since the 2026-04-23 snapshot). Next indexer rebuild will refresh once
  V3-EXQ-476 and the other newly-queued runs return.
- **Pending review:** 25 items as of pending_review.md regenerated
  2026-04-23T17:49:07Z (24 PASS, 0 FAIL, 1 UNKNOWN for V3-EXQ-471). PASS
  queue is dominated by the SD-033 cluster landings (EXQ-456, 460, 462-468)
  across multiple timestamps; the UNKNOWN clears on the next indexer rebuild.
- **Current first-paper-gate bottleneck:** V_s invalidation runtime end-to-end
  validation is now the next gate. V3-EXQ-476 cascade-gate entropy probe is
  queued; PASS unlocks V3-EXQ-449c and the downstream V_s-gated cascade
  (EXQ-445d / 455a). SD-032 cluster behavioural follow-through remains the
  primary cingulate-track blocker (V3-EXQ-445a / 445b / 445c all FAILed;
  V3-EXQ-325d FAILed with zero between-arm gradient on the SD-032c AIC-analog
  descending-modulation falsification signature; V3-EXQ-454 FAILed on ARC-016
  adaptive commitment_threshold). The SD-003 successor track is re-opened by
  V3-EXQ-433c now that the agent_caused_hazard r2=0.0 from V3-EXQ-433b has
  been diagnosed as a curriculum-sufficiency issue (0 agent-caused trials
  collected in every seed because the env relied on organic elicitation)
  rather than a MECH-256 architectural failure. SD-016 cue_action_proj
  forward-path is now unblocked by the V3-EXQ-449b verification (2026-04-23
  dry-run g2 per-channel std = 2.957e-3, primary_pass=True), which in turn
  re-enables V3-EXQ-418c.

---

## Status Snapshot (2026-04-23 PM — lit-pull + docs sync)

- **Literature pull completed: MECH-074a/c/d (PM session 2026-04-23T11:24Z–11:34Z).**
  Six new entries added to `evidence/literature/targeted_review_connectome_mech_074/`:
  - **MECH-074a** (3 entries): Paré 2003 (connectome_mechanistic_review, conf=0.80);
    Roozendaal et al. 1999 PNAS (behavioral_animal, conf=0.82 — direct beta-adrenergic
    gate evidence); Bass & Manns 2015 (electrophysiology_lfp, conf=0.72 — BLA
    stimulation → CA3-CA1 gamma synchrony → STDP circuit mechanism).
  - **MECH-074c** (2 entries): Ciocchi et al. 2010 Nature (electrophysiology_single_unit,
    conf=0.78 — CeL required for fear acquisition, CeM drives output, GABAergic
    disinhibition); Walker & Davis 2008 (connectome_mechanistic_review, conf=0.75 —
    CeA(M) rapid phasic output vs BNST sustained fear, directly grounds the
    fast_prime vs MECH-046 distinction).
  - **MECH-074d** (1 entry): Redondo et al. 2014 Nature (behavioral_animal, conf=0.62,
    mixed — DG engram can switch valence, BLA engram cannot; supports BLA attribution
    stability but does not directly test PE-triggered partial remap amplitude).
  `claim_evidence.v1.json` updated: MECH-074a lit_conf=0.840, MECH-074c lit_conf=0.782,
  MECH-074d lit_conf=0.560. Index rebuilt: 923 literature entries across 443 experiment
  types.
- **Experiment count:** 844 runs (indexer rebuilt 2026-04-23 PM; prior session spec
  showed stale count of 525 — now corrected in spec and README).
- **Pending review:** 0 indexed pending; 10 runner-only UNKNOWN (V3-EXQ-456, 460,
  462–468, 471, 447 — all from V_s invalidation runtime / SD-032 cluster landings;
  will clear after next indexer rebuild with those results indexed).
- **No new SDs or governance decisions this session** (docs-only sync pass following
  the PM lit-pull).

---

## Status Snapshot (2026-04-23)

- **V_s invalidation runtime substrate wave LANDED 2026-04-22.** Six substrates
  landed in a coordinated 2026-04-22 session implementing the architecture doc
  `REE_assembly/docs/architecture/v_s_invalidation_runtime.md`:
  - **SD-036 GABAergic cross-stream decay regulator**
    (`ree_core/regulators/gabaergic_decay.py`) -- broadly-projecting tonic decay
    applied out-of-place across registered latent streams (z_harm tau=0.05,
    z_harm_a tau=0.02, z_beta tau=0.03 by default; drive accumulator intentionally
    excluded). Global `gaba_tone` multiplier in [0, 2] models benzo-analog (>1)
    and withdrawal / chronic-stress analog (<1). Wired in `agent.sense()` right
    after `LatentStack.encode()` so all downstream consumers see the decayed
    latent on the same tick.
  - **MECH-279 PAG freeze-gate** (`ree_core/pag/freeze_gate.py`) -- committed-
    freeze substrate keyed on `duration_above_threshold * z_harm_a > theta_freeze`
    (default 2.0). Exit threshold scales with SD-036 `gaba_tone`, so the same
    GABAergic system gates BOTH freeze entry AND freeze exit (architectural
    prediction: GABA agonists treat freeze catatonia). Action-class no-op
    injection during freeze; simulation_mode gated.
  - **MECH-269 base / Phase 1 per-stream V_s**
    (`ree_core/hippocampal/module.py::update_per_stream_vs`) -- foundation
    observable: identity-prediction proxy EMA over registered streams
    (`z_world / z_self / z_harm_s / z_harm_a / z_goal / z_beta`); seeds at 1.0
    on first tick, drops on latent change. Forward-predictor routing (SD-007
    reafference for z_world, SD-011 harm forward for z_harm_s) reserved for
    Phase 2 consumer wiring.
  - **MECH-288 event segmenter Phase 2**
    (`ree_core/hippocampal/event_segmenter.py`) -- two-scale boundary detector:
    fast `pe_threshold` on `(z_world, z_self)` (window=200, threshold=0.65) +
    slow BOCPD-Gaussian on `(z_goal,)` (hazard=1/40, posterior_threshold=0.5,
    top-k=20). Emits BoundaryEvents with nested outer.inner segment IDs; slow
    fire forces outer+=1, inner=0 and suppresses same-tick fast; `force_boundary`
    API for scripted injection. BOCPD uses underflow-robust Adams & MacKay 2007
    recursion with Welford online variance.
  - **MECH-287 invalidation trigger Phase 2 iv**
    (`ree_core/regulators/invalidation_trigger.py`) -- BoundaryEvent subscriber
    re-emitting graded BroadcastEvents (`strength = posterior * gain`; NO
    binary thresholding of strength). Phasic/tonic guardrail (Aston-Jones &
    Cohen 2005; Clewett 2025 failure signature 2) via rolling mean over
    `tonic_window=50` past-tick posteriors; suppresses phasic broadcast when
    tonic estimate exceeds `tonic_threshold=0.5`. Verdict-3 architectural
    commitment (V_s foundation lit-pull synthesis): the trigger IS the
    subscriber, not an independent CA1/CA3 mismatch comparator stage -- the
    biological two-stage loop is collapsed to a subscription on the MECH-288
    boundary queue. Dissociation contract C5 verifies: lesioning the segmenter
    silences the trigger regardless of its internal tonic state.
  - **MECH-269 Phase 2 ii AnchorSet** (`ree_core/hippocampal/anchor_set.py`) --
    scale-tagged anchor store keyed on `(scale, segment_id, stream_mixture)`.
    Dual-trace preservation per Bouton 2004: remap on the same
    `(scale, stream_mixture)` marks the outgoing anchor INACTIVE and retains
    it in `all_anchors()`; never erased. k=5 consecutive-below-threshold
    hysteresis on `V_s_anchor = avg(V_s over mixture) - staleness`
    (staleness monotonic in tick - last_accessed). FIFO soft-cap at 128
    active anchors per scale. BoundaryEvent consumer via
    `tick_anchor_set(latent_state, events)`; Phase 2 stream_mixture stand-in is
    `tuple(sorted(per_stream_vs.keys()))` at anchor-creation tick (learned
    attribution-head version reserved for Phase 3 MECH-284).
  - **MECH-269 Phase 2 iii T4 per-region V_s** (extended module.py) -- promotes
    flat `per_stream_vs[stream] -> float` to
    `per_region_vs[(scale, segment_id)][stream] -> float` keyed on active
    AnchorSet regions. Two reset paths: (1) passive hysteresis via
    `tick_anchor_set` marking anchors inactive; (2) explicit via
    `apply_invalidation_broadcasts_to_regions(broadcasts)` dropping region V_s
    and mark_inactive'ing the matching anchor on MECH-287 BroadcastEvents
    (keyed on `source_scale`, `source_segment_id_old`). Peek-not-drain on the
    broadcast queue preserves events for Phase 3 MECH-284 staleness accumulator
    consumer. Idempotent on repeated broadcasts.
  All six landed via 85/85 contracts + 7/7 preflight PASS with flags OFF
  (bit-identical to legacy), plus dedicated contract tests for each phase:
  MECH-269 Phase 1 (5 tests), MECH-288 (7 tests), MECH-287 (5 tests incl.
  verdict-3 dissociation C5), MECH-269 Phase 2 ii (9 tests incl. 2 integration
  smokes for agent-level flag behaviour), MECH-269 Phase 2 iii T4 (6 tests
  incl. 1 integration smoke). Activation smokes confirmed expected signatures:
  CeA synthetic threat -> graded mode_prior/fast_prime; BLA synthetic arousal
  -> inverted-U cap; BLA synthetic PE-spike -> Moita 2004 remap; default agent
  + Phase 1 flag ON seeds `per_stream_vs` at 1.0 and drops on perturbation;
  forced fast boundary installs anchor under segment_id "0.1" and populates
  per-region V_s under the new region key. Design doc:
  `docs/architecture/v_s_invalidation_runtime.md`; anchor-selection doc:
  `docs/architecture/hippocampal_anchor_selection.md`. End-to-end combined-
  cluster validation (V3-EXQ-476: matched re-run of EXQ-475 with the full
  circuit on) is planned; not yet queued as of 2026-04-23.
- **Experiments:** 525 total completions unchanged since 2026-04-22 snapshot
  (runner_status.json last_updated 2026-04-22T01:11Z) -- the V_s invalidation
  runtime wave landed via contract tests + activation smokes only. PASS/FAIL
  breakdown: 108 PASS / 234 FAIL / 62 ERROR / 121 UNKNOWN. Next indexer
  rebuild will refresh after V3-EXQ-476 and the pending SD-032 / SD-003
  successor results land.
- **Pending review:** 10 items as of 2026-04-22T23:12:38Z (down from 46 at the
  2026-04-21T19:54Z snapshot). All 10 are runner-UNKNOWN because the index is
  stale ahead of the next indexer rebuild (`python evidence/experiments/
  scripts/build_experiment_indexes.py` from `REE_assembly/` root clears them).
  Queue IDs: V3-EXQ-456 / 460 / 462 / 463 / 464 / 465 / 466 / 467 / 468 / 471.
- **Current first-paper-gate bottleneck:** SD-032 cluster behavioural follow-
  through remains the primary gate. V3-EXQ-445a (SD-032b dACC full-pipeline
  fix for the EXQ-445 monostrategy collapse + terrain-prior inversion,
  claimed EWIN-PC) is the decisive test still in flight; V3-EXQ-445b / 445c
  have both FAILed and V3-EXQ-325d FAILed on the SD-032c descending-
  modulation falsification signature. V3-EXQ-447 (SD-032d deterministic
  validation, claimed ree-cloud-2) and V3-EXQ-451 (Q-034 hazard/resource
  threshold retest, claimed EWIN-PC) are the remaining two claimed
  experiments. SD-003 successor track (V3-EXQ-433a MECH-256/SD-029 FAIL,
  V3-EXQ-452 MECH-257 dual-function E2 diagnostic FAIL) and ARC-007 path-
  memory track (V3-EXQ-397c) remain alive. Secondary bottleneck: V_s
  invalidation runtime end-to-end validation deferred -- V3-EXQ-476
  (combined-cluster re-run of EXQ-475 with the full circuit on) is planned
  but not yet queued.

---

## Status Snapshot (2026-04-22)

- **SD-035 amygdala analogue LANDED 2026-04-21.** BLA + CeA peer modules
  (`ree_core/amygdala/bla.py`, `ree_core/amygdala/cea.py`) non-trainable
  arithmetic. BLA instantiates MECH-074a inverted-U encoding_gain (Roozendaal
  2011), MECH-074b content-selective retrieval_bias (LaBar & Cabeza 2006
  per-trace weight vector, not scalar), and MECH-074d attribution-gated
  PE-spike remap (Moita 2004). CeA instantiates MECH-046 pre-softmax
  mode-prior (LeDoux 1996 "low road" / Pessoa & Adolphs 2010, distinct from
  SD-032c AIC which biases mode-SWITCH threshold rather than mode
  SELECTION) and MECH-074c fast_prime (Mendez-Bertolo 2016 ~75 ms subcortical
  pulse with cortical confirmation window). CeA mode_prior + fast_prime are
  injected into SalienceCoordinator via update_signal each select_action
  tick. BLA retrieval_bias / remap_signal hippocampal consumer wiring is
  deferred until V3-EXQ-474 confirms behavioural signature. Validation:
  V3-EXQ-473 CeA mode-prior PASS (5 acceptance criteria), V3-EXQ-474 BLA
  encoding+remap PASS (5 acceptance criteria), both substrate-readiness
  diagnostics per EXQ-445 lesson. 33/33 preflight+contract tests PASS with
  use_amygdala_analog=False (backward compat preserved). Governance:
  MECH-046 / MECH-074 / MECH-074a/c/d / SD-035 show hold_pending_v3_substrate
  pending completion. Design doc: `docs/architecture/sd_035_amygdala_analog.md`;
  literature synthesis: `evidence/literature/targeted_review_amygdala_analog/
  synthesis.md`.
- **MECH-266 asymmetric per-mode hysteresis LANDED 2026-04-21.** Schmitt-trigger
  per-mode enter_thresholds / exit_thresholds dicts layered atop the MECH-259
  symmetric switch_threshold in
  `ree_core/cingulate/salience_coordinator.py`. Empty-dict default preserves
  legacy behaviour; over-binding/OCD axis reproducible at exit_threshold near 0
  (stuck-in-mode), under-binding/depression axis reproducible with lower
  enter_threshold. Setters: `set_enter_threshold`, `set_exit_threshold`,
  `set_hysteresis_ratio` (uniform exit-rail convenience). Validation:
  V3-EXQ-464 competing-goals 5-arm + V3-EXQ-467 mode-stickiness 5-arm
  parametric sweep both smoke-PASS all sub-tests. Full behavioural
  competing-goals runs deferred pending CausalGridWorldV2 dual simultaneously
  active resource-cue extension.
- **SD-029 curriculum-level balanced hazard-event support LANDED 2026-04-21.**
  `scheduled_external_hazard_enabled` + `scheduled_external_hazard_interval` +
  `scheduled_external_hazard_prob` + `scheduled_external_hazard_adjacent_only`
  flags in CausalGridWorldV2 schedule hazard injection (relocate or spawn) at
  cells adjacent to the agent (or any empty cell when adjacent_only=False).
  Preserves the self- vs externally-caused taxonomy: the agent did not
  initiate the encounter. `info["external_hazard_injected"]` /
  `info["external_hazard_event_count"]` tags always present. Unblocks C3/C4
  event-conditioned SNR measurement for the MECH-256/SD-029 comparator track
  which had been failing on per-seed event-count imbalance. Validation:
  V3-EXQ-470 SCHEDULED vs BASELINE ablation queued.
- **SD-033e frontopolar-analog V4-reserved stub LANDED 2026-04-21.**
  `ree_core/pfc/frontopolar_analog.py` (FrontopolarAnalog +
  FrontopolarConfig) mirrors the SD-033a contract: no-op behind
  `use_frontopolar_analog=False`; raises NotImplementedError when enabled
  (until design doc lands). Last nn.Linear of both heads (MECH-264
  counterfactual-value, MECH-265 relative-importance) zero-initialised.
  `tests/contracts/test_sd_033e_stub.py` 7-contract test added (importable,
  default backward-compat, enabled-raises-NotImplementedError, zero-init,
  reset safety, get_state stub marker). Three V4-reserved experiment
  proposals appended to manual_proposals.v1.json (EXP-0165 / 0166 / 0167).
  Path-clear for the design-doc + dual-active-goal env extension that
  unlocks behavioural testing.
- **Hippocampal anchor-vs-probe cluster REGISTERED 2026-04-21.** MECH-269
  (regional-verisimilitude anchor selection in hippocampal proposer -- per-
  stream V_s gates anchor eligibility; probe channel inverts the gate for
  curiosity-driven seeding; anchored rollouts update ARC-018 viability map,
  probes do not until realized-experience validation); MECH-270 (ephaptic
  field coherence as candidate biological substrate for V_s readout);
  MECH-271 (MECH-094 hypothesis_tag as routing signature: anchored replay
  routes to E1 consolidation / SD-033a PFC, probe replay routes to BLA /
  NAc -- tag is a routing flag, not a source-side marker). MECH-269 lit-pull
  confidence jumped 0.783 -> 0.852 on 2026-04-21 after Pfeiffer & Foster 2013
  (direct evidence: hippocampal sequences start at current location, progress
  to goal, compositional) was added. Design doc:
  `docs/architecture/hippocampal_anchor_selection.md`. MECH-270 future
  directions: standalone-paper candidate.
- **Sleep/waking state-gated routing REGISTERED 2026-04-21.** MECH-272
  (state-gated anchor/probe routing: waking=anchor-dominant decision-support;
  sleep=probe-dominant Bayesian schema restructuring); MECH-273 (sleep-
  dependent aggregation of SD-003 single-episode self-attribution into stable
  self-model); MECH-274 (V4-reserved: other-attribution sleep-dependent
  aggregation via ARC-010 empathy / mirror-modelling;
  implementation_phase: v4). Design doc `hippocampal_anchor_selection.md`
  extended with sleep/waking section and V4 other-attribution reservation.
- **Scientist-agent developmental-ordering cluster REGISTERED 2026-04-21.**
  ARC-059 (three-stage developmental ordering self -> objects -> others
  refining ARC-019), MECH-275 (sleep-phase general Bayesian aggregation
  mechanism -- MECH-273/274 become specialisations of MECH-275), MECH-276
  (scientist-agent principle: waking-phase counterfactual-backed attribution
  via deliberate intervention), MECH-277 (action-space discovery via motor
  experimentation, stage-1 specialisation), MECH-278 (object-schema formation
  via experimental action, stage-2 specialisation). Design doc:
  `docs/architecture/scientist_agent_developmental_ordering.md`.
  MECH-273/274 depends_on updated with MECH-275.
- **Experiment counts: 525 total completions** (runner_status.json last_updated
  2026-04-22T01:11Z): 108 PASS / 234 FAIL / 62 ERROR / 121 UNKNOWN, up from
  495 / 105 PASS / 227 FAIL at the 2026-04-20 snapshot. New PASSes since the
  2026-04-21 snapshot: V3-EXQ-473 SD-035 CeA mode-prior, V3-EXQ-474 SD-035
  BLA encoding+remap, V3-EXQ-455 SD-032a coordinator behavioural, plus
  V3-EXQ-456 SD-033a landing (PASS), V3-EXQ-460/466 SD-034 landings,
  V3-EXQ-462/465 MECH-267, V3-EXQ-463/468 MECH-268, V3-EXQ-464/467 MECH-266.
  New FAILs since the 2026-04-21 snapshot include V3-EXQ-397c (ARC-007 harder
  env, 2 attempts), V3-EXQ-445b/c (SD-032b variants), V3-EXQ-133 (MECH-091),
  V3-EXQ-126 (MECH-104), V3-EXQ-325d (SD-032c AIC), V3-EXQ-452/453/454
  (MECH-257 / MECH-261 landing / ARC-016 adaptive), V3-EXQ-433a (MECH-256/
  SD-029 comparator scripted-eval). Fresh indexer rebuild pending.
- **Pending review count: 46** (as of pending_review.md generation
  2026-04-21T19:54:57Z): 8 PASS / 19 FAIL / 19 ERROR-UNKNOWN-smoke. Governance
  cycle pending to absorb the SD-032 cluster behavioural FAILs, the SD-035
  amygdala landings, the MECH-266 hysteresis extension, and the
  MECH-269/270/271 + MECH-272/273/274 + MECH-275/276/277/278 + ARC-059
  registrations.
- **Queue drained to 3 items -- all claimed.** V3-EXQ-447 (SD-032d
  deterministic validation, ree-cloud-2, claimed 2026-04-19), V3-EXQ-451
  (Q-034 hazard/resource threshold retest, EWIN-PC, claimed 2026-04-20),
  V3-EXQ-445a (SD-032b dACC full-pipeline fix, EWIN-PC, claimed 2026-04-20).
  All other queued entries from the 2026-04-21 snapshot have since landed
  as PASS/FAIL entries in runner_status.json.
- **Current bottleneck.** SD-032 cluster behavioural follow-through remains
  the primary first-paper-gate blocker: V3-EXQ-445a is the decisive test
  after the 445b / 445c monostrategy + terrain-inversion variants FAILed.
  SD-003 successor track (V3-EXQ-433a MECH-256/SD-029 FAIL, V3-EXQ-452
  MECH-257 dual-function diagnostic FAIL) is alive. ARC-007 path-memory
  track remains open (V3-EXQ-397c claimed on DLAPTOP-4.local). SD-035
  first-pass hippocampal consumer wiring for BLA retrieval_bias / remap
  deferred until V3-EXQ-474 behavioural signature confirmed; that work and
  the MECH-266 full behavioural competing-goals arm both depend on the
  CausalGridWorldV2 dual simultaneously active resource-cue extension.

## Immediate Work Queue (This Cycle)

- Design and queue the **EXQ-490b/MECH-295 combined-cluster successor**.
  Post-2026-04-28-governance, EXQ-490b alone is inconclusive: Q-040a
  substrate-wiring effective PASS at the threshold-overridden smoke;
  Q-040b stale-stream-discrimination FAIL points at the MECH-295
  drive->liking->approach bridge as the remaining blocker. The MECH-295
  bridge landed 2026-04-26 (V3-EXQ-493 PASS), so the successor combines
  MECH-269b VsRolloutGate ON with MECH-295 bridge ON in a single
  factorial. Resolves the EXQ-483 wired-but-inert pattern by isolating
  the dominant cause of the observed approach_commit collapse and is
  the next-up substrate-validation run before V3-EXQ-495 commits.
- Land V3-EXQ-495 (MECH-163 V3 full-completion gate -- VTA /
  hippocampally-planned arm) once the EXQ-490b/MECH-295 successor
  resolves. All three substrate prerequisites already cleared
  2026-04-27 (SD-039 population layer V3-EXQ-494 PASS; MECH-292
  V3-EXQ-496 PASS; MECH-293 V3-EXQ-497 PASS). 3 conditions (HABIT /
  PLANNED / ABLATED) × 2 paradigms (A_DETOUR / B_NOVEL_CONTEXT) × 7
  seeds. **C2 PLANNED-HABIT benefit-post-block gap >= 0.30 in detour,
  >= 4/7 seeds is THE V3-full-completion criterion.** Estimated ~25h
  on Mac / ~40h on ree-cloud-1; machine_affinity=any. Queueing-and-
  running is a deliberate runtime-budget decision.
- Escalate OCD post-Layer-1 disconfirmation to **Layer 2 (MECH-290
  ablation diagnostic)** or **Layer 3 (SD-046 multi-slot GoalState
  pull-forward)**. V3-EXQ-498 reclassified non_contributory in the
  2026-04-28T23:04Z governance cycle (Layer 1 closure-threshold
  sweep produced no entropy delta vs DEFAULT in 2/3 seeds at any of
  TIGHT / LOOSE / VERY_LOOSE rails). Layer 2 tests whether ablating
  MECH-290 backward credit sweep recovers behavioural diversity;
  Layer 3 tests whether multi-slot GoalState pull-forward resolves
  the monostrategy.
- Resolve **SD-016 env-entropy precondition** by extending CausalGridWorldV2
  beyond the current SD-023 landmarks-on path. EXQ-418f/g/h established
  that the cue_context machinery works as designed but the env doesn't
  supply cross-context z_world variance (cos~0.998 batch-wise; H1
  cos_cross<0.95 not robust at landmarks-on alone). substrate_queue
  status: parked_pending_env_entropy_precondition. Once env enrichment
  lands, queue EXQ-418i 4-arm reusing EXQ-418g substrate matrix on the
  enriched env config.
- Run the next governance cycle once the EXQ-490b/MECH-295 successor +
  V3-EXQ-495 land: rebuild `claim_evidence.v1.json`, regenerate
  `pending_review.md`, ingest the V3-full-completion-gate outcome.
  Resolve the open promotion blockers: MECH-294 within-cycle-vs-cross-
  cycle binding (Kay 2020 challenge); MECH-295 strong-vs-weak
  liking-bridge necessity (weak reading committed provisionally).
- Pending re-queue under fresh IDs: V3-EXQ-433d / V3-EXQ-418e /
  V3-EXQ-490 / V3-EXQ-498 successors -- only when their predecessor
  `non_contributory` / `does_not_support` reclassifications resolve via
  substrate progress (Phase 2 forward-predictor V_s for MECH-269b;
  div_weight sweep at 1.0 / 2.0 / 5.0 for SD-016 path-1; MECH-269/
  MECH-269b V_s landing for SD-029 monomodal phenotype; Layer 2 / Layer 3
  for OCD post-Layer-1-disconfirmation).
- **Aggregator floor flag (5th consecutive cycle):** worth a cap-aware
  aggregator review. Per-paper confidences for low/medium-anchored
  Q-claims average 0.55-0.86 but claim-level lit_confidence aggregates
  to 0.82-0.89. Flagged in 6 narrow-open Q-claim evidence_quality_note
  refreshes this cycle.
- Add a `held_v4_by_architectural_commitment` recommendation type to the
  governance tooling so v4-by-design claims (ARC-053 / MECH-225 / MECH-226 /
  MECH-227 / MECH-228 / MECH-270 / MECH-274 / MECH-276 / MECH-277 /
  MECH-278 / ARC-059) stop producing the misleading
  `hold_pending_v3_substrate` recommendation.
- First-pass hippocampal consumer wiring for SD-035 BLA retrieval_bias and
  remap_signal once V3-EXQ-474 behavioural signature confirmed (deferred
  from 2026-04-21 landing pass).
- Continue Sleep Aggregation Cluster wiring: BG / E3 replay-prio consumers
  reading MECH-284 staleness alongside MECH-269 V_s; downstream consumers
  of the MECH-272 RoutingGate (HippocampalRouter / E1 ContextMemory) and
  MECH-273 SelfModelAggregator outputs.
- Move MECH-266 OCD/depression-axis competing-goals behavioural variants
  (EXQ-464b / EXQ-467b) off hold once the CausalGridWorldV2 dual
  simultaneously active resource-cue env extension lands.
- SD-033e design doc + dual-active-goal env extension to unlock the three
  V4-reserved proposals (EXP-0165 / 0166 / 0167).

---

## Status Snapshot (2026-04-21)

- **SD-033a lateral-PFC-analog / MECH-261 primary consumer LANDED 2026-04-20.**
  `ree_core/pfc/lateral_pfc_analog.py` (LateralPFCAnalog, LateralPFCConfig).
  Instantiates MECH-262 rule-selective persistence: gate-modulated EMA
  rule_state ([1, rule_dim]) with eff_eta = update_eta * write_gate("sd_033a"),
  source = delta_proj(z_delta) + world_pool_weight * world_proj(z_world).
  Frozen-random bias head with last nn.Linear zeroed at init -> initial
  bias exactly zero (bit-identical with head untrained; training-dependent
  emergence deferred). Per-mode gate weights from the MECH-261 spec table:
  external_task=1.0, internal_planning=1.0, internal_replay=0.05,
  offline_consolidation=0.3. V3-EXQ-456 landing diagnostic PASS (five
  sub-tests: instantiation, gate-modulated update rate, bias reaches E3
  with zero-init contract, backward compat, reset clears rule_state).
  Design doc: `docs/architecture/sd_033a_lateral_pfc_analog.md`.
- **SD-034 governance closure operator + MECH-268 dACC conflict-saturation +
  MECH-267 mode-conditioned hippocampal proposals LANDED 2026-04-20..2026-04-21.**
  SD-034 closure operator (`ree_core/governance/closure_operator.py`)
  coordinates a five-part "done" token at rule-completion events:
  (a) MECH-090 beta release, (b) MECH-260 No-Go FIFO injection on the
  just-completed action class, (c) ResidueField.discharge_domain(z_world,
  factor, radius) rule-domain multiplicative RBF decay with 1e-6 sign-aware
  floor (invariant: residue cannot be erased), (d) SalienceCoordinator
  closure_event signal re-biasing affinity toward internal_planning,
  (e) dACC PE reset / optional pe_cap install (MECH-268). Completion
  detector: rule_state delta < threshold for N consecutive ticks AND
  beta elevated AND current_mode in allowed_closure_modes AND
  write_gate("sd_033a") >= min. Mode conditioning is the falsifiability
  predicate vs pure MECH-090 + MECH-260 + MECH-094 tuning. MECH-267
  (`ree_core/hippocampal/module.py`) threads operating_mode through
  HippocampalModule.propose_trajectories with per-mode CEM-noise multipliers.
  MECH-268 (`ree_core/cingulate/dacc.py`) adds an outcome-history FIFO +
  f_sat attenuation on the dACC bundle; closure_event resets the buffer.
  Landing smokes all PASS: V3-EXQ-460 SD-034 closure wiring (6 sub-tests),
  V3-EXQ-466 ResidueField.discharge_domain (5 sub-tests: near attenuation,
  far spared, invariant preserved, end-to-end, distant-z spares), V3-EXQ-462
  MECH-267 rule binding, V3-EXQ-465 MECH-267 intrusive-simulation filtering,
  V3-EXQ-463 + V3-EXQ-468 MECH-268 saturation-and-reset. Behavioural
  variants with full E3 task loop + tolerance-band completion env deferred
  (depend on phased rule_state training + env variant not yet on the
  roadmap). Anchor: `evidence/planning/sd033_governance_plan.md`;
  source: `docs/thoughts/2026-04-20_ocd4.md` + GAP MEMO "REE-V3 is not
  missing cognition, it is missing governance."
- **SD-032 cluster behavioural follow-through: FAIL across four first-pass
  behavioural gates.** V3-EXQ-445 FAIL (SD-032b 3-arm ablation hit the
  monostrategy + terrain-inversion fishtank_viz signature under all three
  configs; dACC score_bias entropy delta under the C2 gate); V3-EXQ-325d
  FAIL (SD-032c AIC descending modulation, does_not_support); V3-EXQ-454
  FAIL (ARC-016 adaptive commitment threshold, weakens). V3-EXQ-455 PASS
  (SD-032a salience-network coordinator behavioural: supports SD-032a /
  MECH-259 / MECH-261 on the synthetic high-PE injection path). V3-EXQ-452
  FAIL (MECH-257 dual-function E2 diagnostic), V3-EXQ-453 FAIL (MECH-261
  write-gate landing diagnostic -- SD-032e-relevant). Net reading:
  the salience-coordinator substrate and its write-gate registry are
  structurally sound in isolation, but the end-to-end dACC / AIC / ARC-016
  behavioural loop does not yet clear even the first behavioural gates on
  CausalGridWorldV2. EXQ-445 has three successors queued (a/b/c) targeting
  monostrategy + terrain inversion via MECH-260 suppression, ARC-058
  shared-trunk, and foraging-value wiring respectively. EXQ-325b re-scoped
  as EXQ-325d produced does_not_support; AIC->descending pathway remains
  open under drive-regime contrast.
- **SD-016 forward-path diagnostic: V3-EXQ-449 FAIL confirmed
  cue_action_proj receives exactly 0.0 gradient under the original
  "implicit via E3 trajectory selection" claim** (C1 PASS, 2 seeds, ~1.7k
  steps; CEM argmax non-differentiable + detach at agent.py:694). C2 arm
  added supervised MSE loss against E2.action_object(z_world, a_executed)
  .detach() -- weights trained (grad ~0.013, delta ~0.21) but
  action_bias_divergence stayed at 0.0, indicating a downstream blocker
  between cue_action_proj and E3.select. V3-EXQ-449a queued to instrument
  the full forward path and identify the specific blocker before any
  EXQ-418b successor is written. cue_action_proj is now treated as
  CURRENTLY UNGROUNDED: sd016_enabled=True experiments should expect
  action_bias_divergence ~= 0.0 on the action path; cue_terrain_proj
  remains valid (trained via terrain_loss).
- **Recent landing MECH-267 + MECH-268 substrate smokes all PASS.**
  V3-EXQ-462 (MECH-267 rule binding) supports [MECH-267, SD-033a,
  MECH-262]. V3-EXQ-465 (MECH-267 intrusive-simulation filtering)
  supports [MECH-267, MECH-094, MECH-261]. V3-EXQ-463 + V3-EXQ-468
  (MECH-268 conflict-saturation) supports outcome-history FIFO + f_sat
  attenuation + closure-event buffer reset. V3-EXQ-456 (SD-033a landing)
  supports [SD-033a, MECH-261, MECH-262].
- **~715 V3 runs indexed** (indexer rebuild 2026-04-20T19:49Z wrote
  `claim_evidence.v1.json` with 630 V3 run-dirs + 77 flat V3 manifests =
  707 post-epoch; ~9 further V3 manifests written since rebuild covering
  SD-033a / SD-034 / MECH-267 / MECH-268 landings and the SD-032 cluster
  behavioural follow-through). Fresh claim_evidence.v1.json rebuild
  pending after this cycle's wave of results. Queue at snapshot time:
  14 active items, 4 claimed -- V3-EXQ-447 (SD-032d ree-cloud-2),
  V3-EXQ-451 (Q-034 retest EWIN-PC), V3-EXQ-445a (SD-032b full-pipeline
  fix EWIN-PC), V3-EXQ-397c (ARC-007 harder-env DLAPTOP-4). Pending
  queue: V3-EXQ-445b/c (SD-032b variants), V3-EXQ-456 (SD-033a landing,
  now PASS), V3-EXQ-449a (SD-016 forward-path probe), V3-EXQ-133 /
  V3-EXQ-126 (MECH-091 / MECH-104 discriminative pairs), V3-EXQ-460 /
  463 / 466 / 468 (SD-034 + MECH-268 landing smokes, all PASS).
  runner_status.json last_updated stale at 2026-04-20T14:39:30Z
  (495 completions: 105 PASS / 227 FAIL / 62 ERROR / 101 UNKNOWN);
  the live machine-side completion log is ahead of that snapshot.
- **Pending review count: 6** (as of pending_review.md generation at
  2026-04-20T05:50:27Z; stale -- regeneration pending after this cycle).
  Items: FAIL EXQ-397 (ARC-007/SD-004 path memory), FAIL EXQ-433a
  (MECH-256/SD-029 scripted-eval comparator), FAIL EXQ-445 (SD-032b
  behavioural); PASS EXQ-446 (SD-032a coordinator landing); ERROR
  V3-EXQ-445 + V3-EXQ-325c to clear.
- **Governance cycle 2026-04-19T21 (post-SD-032 landing) carry-forward.**
  Promoted MECH-094 to provisional; applied 12 `hold_pending_v3_substrate`
  decisions for the SD-032 cluster and dependents; reclassified EXQ-395 /
  EXQ-418a / EXQ-430 as non_contributory substrate-gap symptoms. No new
  governance cycle run today -- the SD-032 behavioural FAILs and the
  SD-033a/SD-034/MECH-267/MECH-268 landings are the input set for the
  next cycle.
- **Current bottleneck: SD-032 cluster behavioural escape from
  monostrategy + terrain-inversion, SD-033 governance cluster behavioural
  validation, SD-016 forward-path blocker identification, SD-003
  successor track.** Regression suite PRs 1-5 landed (preflight +
  contracts + deferred changed; `/api/regression/preflight` serve.py
  endpoint; explorer preflight badge; pre-commit contracts hook).

## Immediate Work Queue (This Cycle)

- Land results for the four claimed experiments: V3-EXQ-447 (SD-032d
  deterministic validation, ree-cloud-2), V3-EXQ-451 (Q-034 retest,
  EWIN-PC), V3-EXQ-445a (SD-032b full-pipeline fix, EWIN-PC),
  V3-EXQ-397c (ARC-007 path memory harder-env, DLAPTOP-4).
- Review pending_review.md after its next regeneration -- expected to
  cover EXQ-397 / EXQ-433a / EXQ-445 FAILs plus EXQ-446 PASS and the
  two ERROR clears (V3-EXQ-445, V3-EXQ-325c).
- Queue and land V3-EXQ-449a (SD-016 forward-path instrumentation
  probe) as the prerequisite for any EXQ-418b successor.
- Land V3-EXQ-445b/c (SD-032b monostrategy + terrain-inversion
  variants) once V3-EXQ-445a returns.
- Behavioural variants for SD-034 / MECH-267 / MECH-268 still need a
  tolerance-band completion env + phased rule_state training plan
  before any behavioural EXQ can be written; the landing-diagnostic
  smokes (V3-EXQ-460/462/463/465/466/468) have all PASSed.
- Next governance cycle: ingest the SD-032 behavioural FAILs, the
  SD-033 cluster landings, and the MECH-094 provisional persistence;
  rebuild `claim_evidence.v1.json`; regenerate `pending_review.md`.

---

## Status Snapshot (2026-04-20)

- **SD-032 cingulate integration cluster fully IMPLEMENTED 2026-04-19 (a/b/c/d/e).**
  In order of landing: SD-032b dACC/aMCC-analog adaptive control (Croxson/Shenhav/Kolling
  bundle -> DACCtoE3Adapter shim -> E3.select score_bias; ARC-033 vs ARC-058 shared-trunk
  as constructor-switch alternative), then SD-032a salience-network coordinator (soft
  operating_mode vector + MECH-259 Schmitt-trigger switch threshold + MECH-261 dict-keyed
  write-gate registry, 8 default targets, V4 register_target() extensibility), then
  SD-032c AIC-analog (drive- and mode-aware harm_s_gain subsumes SD-021 descending
  modulation; EXQ-325a bit-identical DESCENDING==CONTROL signature resolved), then
  SD-032d PCC-analog metastability scalar (modulates MECH-259 effective_threshold by
  drive_level / success EMA / time-since-offline; single integration point for MECH-092
  within-session quiescence and INV-049 cross-session sleep via enter_offline_mode), then
  SD-032e pACC-analog slow-EMA autonomic coupling (drive_bias write-back from z_harm_a,
  MECH-094 hypothesis_tag gated, alpha=0.002 default ~347-step half-life inside Guo 2018
  ACC mGluR5 LTP envelope). All modules under ree_core/cingulate/, backward-compatible
  master switches default False.
- **MECH-094 promoted candidate -> provisional (governance-2026-04-19T21).** First
  concrete write-gate wiring established by V3-EXQ-448 pACC hypothesis_tag skip PASS;
  12 supports / 0 opposing, confidence 0.856. Feeds the MECH-261 mode-conditioned
  generalisation.
- **SD-033 PFC subdivision cluster registered 2026-04-19.** SD-033 parent + SD-033a-e
  (lateral-PFC / premotor-analog / vmPFC-analog / OFC-analog / frontopolar parallel-goal
  deliberation) + MECH-262/263 + MECH-264/265 (frontopolar counterfactual-value and
  relative-importance monitoring). V3-pending; primary write target for MECH-261
  operating-mode-conditioned writes. Prong D frontopolar lit-pull (6 entries, mean conf
  0.81, Boorman 2009 / Mansouri 2017 load-bearing) broadened SD-033e from Koechlin
  branching to parallel-goal deliberation; reserved V4 operating-mode renamed
  deliberative_branching -> parallel_goal_deliberation (zero schema cost — mode names
  are dict keys). Design docs: `docs/architecture/sd_032_cingulate_integration_substrate.md`,
  `docs/architecture/sd_033_pfc_subdivision_architecture.md`.
- **Regression suite PRs 1-3 landed (ree-v3).** Three-layer architecture:
  (1) preflight (tests/preflight/, runner imports + queue integrity + machine boot; wired
  into experiment_runner.py startup with `--skip-preflight` escape hatch);
  (2) contracts (tests/contracts/ with C1 agent boot, C2 8-flag boot matrix, C3 seed
  determinism, C4 BG gating MECH-090/091, C5 imagined/acted isolation MECH-094, C6/C7/C8
  SD-032 dACC/AIC/PCC/pACC wiring; 24/24 pass in ~14s);
  (3) deferred changed layer stubbed via scripts/run_regression_suite.py. Serve.py
  `/api/regression/preflight` endpoint with 60s memoisation added (REE_assembly commit
  2cb1c9559). Contracts test wiring only, never thresholds from EXQ evidence.
- **EXQ-433 reclassified non_contributory; EXQ-433a scripted-eval successor queued**
  (2026-04-19). Root cause of EXQ-433 FAIL: event-distribution collapse in 3/4 seeds
  (seed 91: 303/0 agent/env, seeds 13/42: ~100/1-2). MECH-256 C1 forward_r2=0.983-0.9998
  unaffected. EXQ-433a uses CausalGridWorldV2.reset_to() for deterministic placement +
  30-trial scripted harness per event type; balanced 3/3/3/3 event counts in smoke;
  supersedes EXQ-433.
- **Governance cycle 2026-04-19T21 (post-SD-032 landing).** Promoted MECH-094 to
  provisional; held SD-020 at provisional; applied 12 `hold_pending_v3_substrate` batch
  (MECH-256/258/259/260/261/264/265, SD-029/032a/b/d/e); reclassified 3 FAIL manifests
  as non_contributory substrate-gap (EXQ-395 MECH-220, EXQ-418a SD-017, EXQ-430 INV-010
  — all addressable by SD-032 cluster); marked 7 experiments reviewed. Retest
  eligibility post-cluster: V3-EXQ-325b (SD-032c falsification signature); V3-EXQ-430a
  (MECH-261 offline-write-gating); V3-EXQ-418b pending diagnostic of SD-016
  cue_action_proj wiring. 5 SD-032 entries added to substrate_queue.json as implemented;
  EXP-0121 and EXP-0132 marked executed.
- **MECH-261 mode-gating lit-pull (2026-04-20T06:30Z).** 5 entries
  (Latchoumane 2017 SO-spindle-ripple triple coupling; Maingret 2016 hippocampo-cortical
  coupling reorganises mPFC; Helfrich 2018 MFC atrophy disperses SO-spindle coupling;
  Klinzing/Niethard/Born 2019 review; Boyce 2016 REM theta optogenetic). V4-staging
  findings: per-mode gate weights load-bearing; carrier rhythm is biological realisation
  of gate in SWS and REM; gate locus and write target may overlap in mPFC; within-REM
  target selection remains open. 795 literature entries, 805 runs indexed at lit-pull
  rebuild.
- **704 runs indexed (630 dirs + 74 flat); 831 queue-level completions across
  five machines** (252 PASS / 480 FAIL / 88 ERROR / 11 UNKNOWN). Queue: 2 items, both
  claimed — V3-EXQ-445 (SD-032b 3-arm ablation OFF / ON-independent / ON-shared-trunk,
  DLAPTOP-4.local) and V3-EXQ-447 (SD-032d deterministic validation, ree-cloud-2).
- **Current bottleneck: SD-032 cluster behavioural validation + SD-003 successor
  follow-through.** V3-EXQ-445 is the first behavioural gate on SD-032b (C2 dACC
  score_bias produces >=0.1 nats entropy delta in either ON arm). V3-EXQ-433a supersedes
  EXQ-433 as the MECH-256/SD-029 comparator test on scripted balanced events. 3 pending
  review (EXQ-397 FAIL ARC-007/SD-004 path memory, EXQ-433a FAIL MECH-256/SD-029
  scripted-eval comparator, V3-EXQ-325c ERROR).

## Immediate Work Queue (This Cycle)

- Land results for V3-EXQ-445 (SD-032b behavioural) and V3-EXQ-447 (SD-032d deterministic);
  both are the first post-landing validation gates for the cingulate cluster.
- Review EXQ-397 (ARC-007/SD-004 path memory) and EXQ-433a (MECH-256/SD-029 scripted
  comparator) in the next governance pass; clear V3-EXQ-325c ERROR.
- Queue SD-032 cluster retests now unblocked by substrate arrival: V3-EXQ-325b (SD-032c
  falsification signature), V3-EXQ-430a (MECH-261 offline-write-gating), and V3-EXQ-418b
  (gated on SD-016 cue_action_proj wiring diagnostic).
- MECH-261 V4 staging decisions tracked against the 2026-04-20 mode-gating lit-pull
  (carrier-rhythm gate implementation, within-REM target selection).

---

## Status Snapshot (2026-04-18)

- **SD-003 superseded.** After 28 accumulated FAILs across the two-pass counterfactual
  architecture, SD-003 was flipped to `superseded` with `superseded_by: [MECH-256, SD-029]`.
  New claims registered: MECH-256 (general single-pass forward-model comparator,
  stream-agnostic; Frith/Shergill/Haggard/Blakemore biology), MECH-257 (dual-function
  single-substrate E2: comparator vs evaluator, controller-gated), SD-029 (concrete
  z_harm_s instantiation of MECH-256), SD-030 (z_self stream, V4-deferred), SD-031
  (z_world stream, V4-deferred). Architecture doc:
  `docs/architecture/self_attribution_per_stream.md`. claims.yaml: 491 claims (+5).
- **V3-EXQ-433 queued (SD-003 successor test, next-up).** Event-conditioned single-pass
  comparator test on z_harm_s: residual = z_harm_s_observed − E2_harm_s(z_harm_s_{t−1},
  a_actual). SD-013 interventional training (fraction=0.5) during P1; P2 uses event-density
  controller that extends up to 200 episodes until ≥20 env-caused and ≥20 agent-caused
  hazards per seed (fixes EXQ-431 sample starvation). Criteria: C1 forward_r2 ≥ 0.9, C2
  self/ext attenuation ratio ∈ [0.3, 0.7] (Shergill), C3 approach SNR > 3, C4 density
  floor; PASS needs 3/4 seeds. Substrate prerequisites (ARC-033, SD-013, SD-011) all
  implemented — SD-029 is a read-mode claim over existing substrate.
- **Governance cycle 2026-04-18 (governance-2026-04-18-15z).** 2 `pending_user`
  recommendations applied as `hold_pending_v3_substrate`: SD-014 (implementation_phase=v3,
  4 supports/0 weakens lit-only) and SD-023 (override of indexer's promote_to_provisional
  to hold, with EXQ-332a indexed non_contributory). Pipeline clean (validator OK 68/68,
  772 runs indexed). **Pending review cleared: 0.**
- **New lit-pulls (wave 1):** LIT-0092 (MECH-104 LC-NE volatility; Sara 2009 Nat Rev
  Neurosci filled triangulation), LIT-0097 (INV-053 depression attractor; Huys/Daw/Dayan
  2015 added as HDD contrast class — HDD and INV-053 are complementary not identical).
  Plus three lit-pulls informing SD-003 successor design (comparator, evaluator, mode
  distinction modes). Literature entries: 741 (+14).
- **New experiments queued (wave 2):** V3-EXQ-434 (INV-053 depression attractor replication,
  5-seed LONG_HORIZON), V3-EXQ-435 (INV-054 phase-transition recovery, sustained-crossing
  criterion, supersedes EXQ-278), V3-EXQ-436 (SD-017 sleep phase ablation redesign with
  context-conditioned harm threshold, supersedes EXQ-242).
- **ree-cloud-2 onboarded.** Second Hetzner cloud worker (CX22 nbg1, IPv4 116.203.216.181)
  brought online. Parameterised systemd service template; cloud-scaler.yml extended to a
  two-server loop (ree-worker-1/ree-cloud-1 + ree-worker-2/ree-cloud-2); validator
  whitelist extended; contributor JSON registered. First real claim was V3-EXQ-355b
  (ARC-038 schema assimilation) rather than the dedicated smoke, because the runner's
  iteration order put the smoke behind any-affinity items — de facto pipeline verification.
- **772 runs indexed; 517 queue-level completions in runner_status.json**
  (102 PASS / 238 FAIL / 63 ERROR / 114 UNKNOWN).
- **Current bottleneck: SD-003 successor architecture validation + first-paper gate.**
  Active queue (17 items): V3-ONBOARD-smoke-ree-cloud-2, V3-EXQ-433 (SD-029 event-conditioned
  comparator, next-up), V3-EXQ-326, V3-EXQ-330a, V3-EXQ-328b, V3-EXQ-326a, V3-EXQ-407,
  V3-EXQ-332, V3-EXQ-321c, V3-EXQ-325b, V3-EXQ-355b, V3-EXQ-418b, V3-EXQ-434, V3-EXQ-435,
  V3-EXQ-436, V3-EXQ-406b, V3-EXQ-429b.

---

## Status Snapshot (2026-04-17)

- **New substrate: SD-016 (frontal cue-indexed integration) implemented 2026-04-16.** E1 queries ContextMemory via z_world using world_query_proj; cue_action_proj provides affordance bias to E2; cue_terrain_proj provides (w_harm, w_goal) terrain precision weights to E3. Config: E1Config.sd016_enabled (default False, backward compatible). Design doc: `REE_assembly/docs/architecture/sd_016_frontal_cue_integration.md`. Validation experiment V3-EXQ-418a queued with terrain_loss fix.
- **Governance 2026-04-16 completed: 16 experiments reviewed.** 5 PASS: EXQ-049a (MECH-090 bistable concordance, Layer 1+2 regression), EXQ-365 (MECH-104 surprise gate, 5-seed), EXQ-353 (ARC-033/SD-003/SD-013 interventional vs observational counterfactual), EXQ-323a (SD-019 affective nonredundancy on SD-022 substrate), EXQ-328a (MECH-090 bistable + SD-012). 11 FAIL/non_contributory/inconclusive including EXQ-385/418 (INV-049/SD-017, identical per-seed data — SHY collapse root cause identified), EXQ-355 (ARC-038 optimizer contamination), EXQ-330a (SD-013, later PASS in EXQ-330a — already confirmed 2026-04-15), EXQ-324a (SD-020 inconclusive, eval termination bug). 9 manifest reclassifications. 4 fix scripts written and queued (EXQ-418a, EXQ-385a, EXQ-355a, EXQ-324b).
- **EXQ-321a FAIL (2026-04-17):** MECH-090 bistable gate still failing. Root causes: 4-bug chain (shared training deepcopy on autograd tensors, spike timing vs E3-tick alignment, bistable config silently dropped via **kwargs). EXQ-321b queued with all 4 fixes; dry-run 3/3 seeds PASS.
- **766 runs indexed** (per morning digest 2026-04-17). **2 pending review** (EXQ-321a FAIL + UNKNOWN runner entry).
- **SD-016 lit-pull (2026-04-17):** Additional 3 entries added to targeted_review_sd_019 (wind-up/central sensitization, Craig 2003 interoception/insula, pain asymbolia). SD-022 lit-pull added 2 entries. Index now 706 lit entries total.
- **Deployment gating note added (2026-04-17):** V3 is treated as a sandbox-only scientific substrate. High-capability or externally connected REE deployment is gated on V4 social/developmental completion. See `docs/governance/deployment_gating.md`.
- **Current bottleneck: first-paper gate.** Active queue (18 items): EXQ-326 (SD-015/MECH-216/SD-012 wanting nav fix), EXQ-330a (SD-013 claimed), EXQ-321b (MECH-090 bistable fix), EXQ-325a (SD-021 descending modulation claimed), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-328b (MECH-230 claimed), EXQ-326a (SD-015/MECH-229 nav), EXQ-406 (INV-053), EXQ-407 (MECH-231), EXQ-396 (ARC-016), EXQ-397 (ARC-007), EXQ-429 (INV-044), EXQ-430 (INV-010), EXQ-418a (SD-016+SD-017 fix), EXQ-385a (INV-049 SHY fix), EXQ-355a (ARC-038 optimizer fix), EXQ-324b (SD-020 eval fix).

---

## Status Snapshot (2026-04-15)

- **New substrate today: MECH-090 Layer 1 (trajectory stepping) + MECH-091 Layer 2 (urgency interrupt) implemented.** REEAgent now steps through committed_trajectory.actions[idx] via _committed_step_idx counter (Layer 1). Layer 2: when beta elevated and z_harm_a.norm() > urgency_interrupt_threshold (default 0.8), gate releases and step counter resets. Both wired in agent.py + E3Config.urgency_interrupt_threshold in config.py (2026-04-15).
- **New claims registered 2026-04-14: MECH-232 (DA representational expansion as approach mechanism), MECH-233 (asymmetric valence encoding: BLA tags vs VTA expands), ARC-057 (curiosity-approach emergence from DA-expanded map).** Architecture doc: hippocampal_valence_asymmetry.md. MECH-231 promoted candidate->provisional (conf from EXQ-407 PASS, 164x E2/E1 slope ratio).
- **EXQ-330a PASS (2026-04-15):** SD-013 contrastive counterfactual at interventional_fraction=0.5. forward_r2=0.999, cf_gap confirmed. Advances SD-013 evidence (already provisional conf=0.788).
- **EXQ-327 PASS (2026-04-14):** MECH-163 goal-conditioned navigation paper gate confirmed.
- **EXQ-365 PASS (2026-04-14):** MECH-104 surprise gate (5-seed) confirmed.
- **494 experiments completed.** 100 PASS, 236 FAIL, 51 ERROR, 107 UNKNOWN.
- **0 pending review** (as of 2026-04-15).
- **Current bottleneck: first-paper gate.** Active queue (16 items): EXQ-323a (SD-019 nonredundancy), EXQ-326 (SD-015 wanting gradient nav), EXQ-330a (claimed), EXQ-353 (SD-003 interventional vs observational), EXQ-321a (MECH-090 bistable gate retest), EXQ-325a (SD-021 descending modulation retest), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-328b (claimed), EXQ-326a, EXQ-406 (INV-053), EXQ-407 (MECH-231), EXQ-396a (ARC-016 dual-bug fix), EXQ-396 (ARC-016 sweep), EXQ-397 (ARC-007 path memory), EXQ-418 (SD-017 + SD-016 context action).

---

## Status Snapshot (2026-04-14)

- **Key governance outcome: SD-013 promoted candidate->provisional (2026-04-13b governance).** conf=0.788, 5 supports/1 weakens. SD-013 (interventional training bias) now provisional. 7 experiments reclassified non_contributory.
- **New claim class registered: EXT-001 through EXT-007.** External AI/LLM failure mode catalogue with REE mechanism mappings (sycophancy, hallucination, reward hacking, goal misgeneralization, causal attribution gap, other-model collapse, context amnesia). claims.yaml: 454 claims total.
- **MECH-231 registered** (E2 short-horizon discriminative pair, cowork-2026-04-13-e). EXQ-407 queued.
- **EXQ-406 queued** (INV-053 depression attractor replication, 5-seed LONG_HORIZON characterisation, ~240 min).
- **~481 experiments completed.** 96 PASS, 235 FAIL, 51 ERROR, 99 UNKNOWN.
- **2 pending review** (as of 2026-04-14T04:18:29Z): v3_exq_326_wanting_gradient_nav_fix FAIL (MECH-216/SD-012/SD-015); V3-EXQ-326 UNKNOWN.
- **Current bottleneck: first-paper gate.** Active queue (17 items): EXQ-326, EXQ-332, EXQ-330a, EXQ-353, EXQ-322a, EXQ-328a, EXQ-321a, EXQ-325a, EXQ-365, EXQ-355, EXQ-395, EXQ-375, EXQ-385, EXQ-328b, EXQ-326a, EXQ-406 (INV-053 depression attractor), EXQ-407 (MECH-231 E2 short-horizon).

---

## Status Snapshot (2026-04-13)

- **Key governance outcome: EXQ-354 PASS (2026-04-13).** MECH-112 behavioral wanting/liking
  dissociation confirmed with SD-015 wiring (3/3 seeds). MECH-112 split into MECH-229
  (behavioral wanting/liking dissociation, active) and MECH-230 (latent z_goal structure,
  candidate). 7 dry-run FAILs from earlier sessions reclassified as non_contributory. SD-012
  design doc updated to IMPLEMENTED.
- **Five new experiments queued (2026-04-13):** V3-EXQ-355 (ARC-038 schema assimilation),
  V3-EXQ-365 (MECH-104 surprise gate, 5-seed), V3-EXQ-375 (MECH-073 valence geometry),
  V3-EXQ-385 (INV-049 offline consolidation necessity / sleep ablation), V3-EXQ-395
  (MECH-220 harm hub behavioral probe). Plus EXQ-328b (MECH-230 full run) and EXQ-326a
  (SD-015 + MECH-229 nav fix).
- **SDs moved pending->implemented since last snapshot:** SD-013 (interventional training),
  SD-015 (ResourceEncoder), SD-017 (minimal sleep infrastructure), SD-018 (resource proximity
  supervision), SD-019 (affective nonredundancy constraint), SD-020 (affective harm surprise PE),
  SD-021 (descending pain modulation), SD-022 (directional limb damage), SD-023 (environmental
  gradient texture). Also: ARC-033, MECH-090 bistable gate, MECH-120 SHY wiring, MECH-203/204
  serotonin substrate, MECH-205 surprise-gated replay fix, MECH-216 E1 predictive wanting.
- **481 experiments completed.** 96 PASS, 235 FAIL, 51 ERROR, 99 UNKNOWN.
- **0 pending review** (as of 2026-04-13T07:19:18Z).
- **Current bottleneck: first-paper gate.** Active queue (16 items): EXQ-327 (MECH-163
  goal-conditioned nav paper gate), EXQ-326a (SD-015 + MECH-229 nav fix), EXQ-353 (ARC-033/
  SD-003/SD-013 interventional vs observational counterfactual), EXQ-321a (MECH-090 bistable
  gate retest), EXQ-325a (SD-021 descending modulation retest), EXQ-365 (MECH-104 surprise
  gate), EXQ-355 (ARC-038), EXQ-395 (MECH-220), EXQ-375 (MECH-073), EXQ-385 (INV-049 sleep
  ablation), and fix iterations EXQ-322a/328a/330a/332/328b/326a.

---

## Status Snapshot (2026-04-06)

- **SD-011/SD-012 Full E3 Integration (2026-04-05).** z_harm_a now flows through the complete
  agent loop: agent.sense() -> LatentStack.encode() -> E3.select(). New E3Config parameters:
  urgency_weight (z_harm_a.norm() lowers commit threshold, D2 avoidance escape, capped by
  urgency_max=0.5) and affective_harm_scale (amplifies lambda_ethical by accumulated threat).
  E3.compute_harm_forward_cost() replaces deprecated HarmBridge path, rolling z_harm_s step-by-step
  through trajectory actions via ResidualHarmForward. Agent.compute_drive_level(obs_body) added
  as canonical SD-012 static method. All new parameters default to 0.0/None for full backward
  compatibility.
- **EXQ-247 queued:** 4-arm ablation validating full SD-011/SD-012 E3 integration. Tests
  urgency_weight and affective_harm_scale jointly with drive_weight across ablation conditions
  (FULL vs NO_URGENCY vs NO_AFFECT vs BASELINE). 3 seeds x 200 train + 50 eval x 200 steps.
- **New claims registered (2026-04-06 thought-intake sessions):** INV-049 (Offline Update
  Necessity Principle -- offline phases are a mathematical necessity for model-building agents),
  INV-050 (three-drive sleep regulation), INV-051 (optimal novelty range), MECH-178
  (noradrenergic REM suppression pathway), MECH-179 (MEL type-specificity), MECH-180
  (novelty-driven adaptive sleep), MECH-181 (cognitive reserve as update-loop maintenance),
  Q-033 (actigraphy MEL forecasting).
- **~198 experiments run.** 51 PASS, 123 FAIL, 22 ERROR, 2 UNKNOWN. 22 experiments
  currently queued (EXQ-223 through EXQ-247 series plus EWIN-PC onboarding smoke).
- **0 pending review** (as of 2026-04-04T18:45:00Z).
- **Current bottleneck: first-paper gate.** Active queue: EXQ-074e/234 (wanting/liking),
  EXQ-076e/235 (goal conditioning), EXQ-195 (SD-003 z_harm_s counterfactual), EXQ-247
  (SD-011/012 full integration), and sleep-architecture experiments (EXQ-242--246).

---

## Status Snapshot (2026-04-04)

- **SD-014 implemented (2026-04-04): hippocampal valence vector node recording.** 4-component
  valence vector V=[wanting, liking, harm_discriminative, surprise] added to RBFLayer and
  ResidueField (ree_core/residue/field.py). Each RBF center stores a valence_vecs buffer
  [num_centers, 4] updated incrementally per visit. MECH-094 gate applies: hypothesis_tag=True
  blocks valence updates. Prerequisite for ARC-036 and replay prioritisation via drive state.
- **ARC-028 + MECH-105 implemented (2026-04-04): hippocampal-BetaGate completion coupling.**
  HippocampalModule.compute_completion_signal() maps best trajectory score to a sigmoid
  dopamine-analog value. BetaGate.receive_hippocampal_completion() releases beta when signal
  >= threshold (0.75). Implements the Lisman & Grace 2005 subiculum->NAc->VP->VTA loop.
- **~292 experiment scripts authored.** EXQ-001 through EXQ-223 series. 0 pending review
  as of 2026-04-03 (all discussed). EXQ-125 currently running on DLAPTOP-4.local (ARC-029).
- **Governance clean.** 0 pending review items (generated 2026-04-03T21:39:23Z).
  Last governance cycle: 2026-04-03 (cowork-2026-04-03-b, 14 experiments reviewed;
  ARC-022 promoted to provisional).
- **Current bottleneck: first-paper gate experiments.** EXQ-223 PASS confirmed the minimal
  E1+E2+hippocampus core loop. Active queue: EXQ-074e (MECH-112/117 wanting/liking),
  EXQ-076e (MECH-116 E1 goal conditioning), EXQ-195 (SD-003 z_harm_s counterfactual),
  EXQ-125 (ARC-029 committed mode, running). SD-015 resource indicator in progress.

---

## Status Snapshot (2026-04-03)

- **EXQ-223 PASS: Minimal mind confirmed (2026-04-03).** The REE core loop —
  E1 (associative world model) + E2 (fast transition model) + HippocampalModule
  (trajectory proposal) + multinomial go/no-go + raw harm/reward signals — is sufficient
  for stable navigation, harm avoidance, and resource acquisition. 3/3 criteria met across
  all 3 seeds (harm_ratio 0.29–0.39; REE takes ~4.5× as much reward as random). The
  ablation strips the deliberative architecture entirely: commitment_threshold=−1.0 (always
  uncommitted), z_goal disabled, benefit_eval disabled. What remains is the predictive
  associative core alone — and it works. This is the first experimental confirmation that
  the E1+E2+hippocampus triad constitutes a minimal functional mind. **The circuit topology
  is a named-structure match to the zebrafish larva (5–7 dpf)**: dorsal pallium (E1) →
  cerebellum (E2) → lateral pallium (hippocampal module) → optic tectum + reticulospinal
  neurons (go/no-go) → lateral habenula (harm signal). The larva has no mature prefrontal
  cortex — no commitment architecture — matching the ablation exactly. It is the only
  vertebrate whose entire ~100,000-neuron CNS has been functionally imaged during free
  behaviour (Ahrens et al., 2013, *Nature Methods*; Portugues et al., 2014, *Neuron*).
  This match was derived from functional-architecture arguments, not from biology.
  Episode visualiser (`episode_viewer.html`) added to the explorer for trajectory playback.
  Full circuit table and references: see changelog 2026-04-03.
- **SD-011 and SD-012 both implemented.** SD-011 (dual nociceptive streams: z_harm_s +
  z_harm_a) validated at EXQ-178b PASS (2026-03-30). SD-012 (homeostatic drive modulation)
  implemented 2026-04-02: drive_weight default raised from 0.0 to 2.0, enabling
  effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level). Step 3.1
  substrate debt now substantially resolved (SD-008/009/010/011/012 all done).
- **~198 experiments run.** EXQ-001 through EXQ-212+ series. 51 PASS, 123 FAIL, 22 ERROR
  as of 2026-04-03. Breadth of FAIL reflects aggressive experimentation on a developing
  substrate -- each FAIL cluster was analyzed and resolved before the next iteration.
- **Breath oscillator and z_beta pathway wired (2026-04-02).** BreathOscillator integrated
  into core commitment decision (MECH-108). rv -> z_beta volatility pathway wired for Q-007.
  14 substrate-limited experiments marked scoring_excluded. EXQ-199--203 queued to re-run
  MECH-025/Q-007/MECH-029/MECH-026/MECH-057a on corrected substrate.
- **ARC-033 ResidualHarmForward promoted to ree_core (2026-04-02).** E2_harm_s forward model
  now in `ree_core/latent/stack.py`, enabling EXQ-195 (SD-003 z_harm_s counterfactual).
  EXQ-195 queued; this is the critical SD-003 re-validation step on the new harm pipeline.
- **Governance cycle active.** 36 experiments pending review (2026-04-03). PASS cluster
  includes SD-011 validation (EXQ-178b), terrain work (SD-015), and several MECH-1xx claims;
  FAIL cluster being classified (evidence vs diagnostic). Governance session in progress.
- **Current bottleneck: first-paper gate experiments.** SD-011/012 substrates cleared; next
  priority is EXQ-074e (MECH-112/117 wanting/liking), EXQ-076e (MECH-116 E1 goal
  conditioning), EXQ-195 (SD-003 z_harm_s counterfactual), and EXQ-182a (oracle ceiling
  for habit-system goal lift).

---

## Status Snapshot (2026-03-31)

- **V3 first-paper gate clarified.** `ree-v3` completion for the first paper is now
  explicitly scoped to the **waking, single-agent substrate**. Sleep, social extension,
  language/communication, nth-order ethics, and full psychiatric modelling are **not**
  blockers for V3 completion.
- **Immediate focus is the approach/goal side.** Harm/attribution substrate has advanced
  materially (SD-003 architecture, SD-005, SD-010, SD-011, ARC-033), but the main remaining
  V3 risk is still positive attractor behavior rather than harm avoidance.
- **Hard V3 completion gates for paper 1:** (1) post-SD-011 SD-003 works on `z_harm_s`,
  not only the legacy `z_world` form; (2) harm/attribution substrate is stable enough to
  treat as platform rather than ongoing rescue work; (3) SD-012 + MECH-112 yield genuine
  behavioral goal lift, not only `z_goal` activation; (4) ARC-030 is demonstrated as
  dual evaluation of the same trajectories by harm and goal channels inside one selector;
  (5) matched-seed reruns and at least one task variant confirm robustness; (6) governance
  state remains clean enough that review/index/claim status are aligned.
- **First-paper claim remains narrow.** Target claim is: REE architectural separation yields
  attributable, harm-avoiding, goal-directed agency in a waking single-agent substrate.
- **Deferred to V4/V5:** consolidation/sleep mechanisms, integrated self/other modelling,
  structured communication, and emergent ethical behavior in multi-agent settings.
  *(Note 2026-04-02:* The V4 deferral of social work reflects a precise architectural
  constraint: INV-043 establishes that testing whether ethical capacity is
  *developmentally activated* — not merely architecturally present — requires a
  multi-agent substrate with modelled caregiving. V3 tests the machinery (ARC-043
  Layer 6); INV-043 testing requires Layers 2-4 to be exercised socially.
  See `docs/architecture/developmental_curriculum.md#inv-043`.*)*

---

## Status Snapshot (2026-03-26)

- **V2 complete.** Series closed after EXQ-028 (2026-03-19). Governance cycle applied 7
  decisions, V3-pending gate lifted.
- **V3 active.** ~96 experiments run (through EXQ-096a). SDs 004–010 implemented.
  SD-010 (harm stream separation) unblocked the prior FAIL cluster: EXQ-056c/058b/059c all PASS.
- **SD-011 is the current bottleneck.** Dual nociceptive streams (z_harm_s + z_harm_a) are
  required for the SD-003 counterfactual redesign. EXQ-093/094 confirmed that
  `HarmBridge(z_world → z_harm)` has bridge_r2=0 (architectural impossibility by SD-010 design).
  ~10 experiments are blocked pending SD-011. Design doc: `sd_011_dual_nociceptive_streams.md`.
- **SD-012 registered.** Homeostatic drive modulation for z_goal seeding — required for
  EXQ-085+ (wanting/liking experiments) and for any goal-directed behavior validation.
  Design doc: `sd_012_homeostatic_drive.md`.
- **New claims registered (2026-03-24/25):** INV-032–038 (approach/avoidance symmetry,
  epistemic self-monitoring, goal maintenance, state definition, stored/active distinction,
  EVR pattern). ARC-030–035. SD-011/012. MECH-112–134.
- **Currently queued:** EXQ-074b (MECH-112/117 wanting/liking, supersedes EXQ-074) and
  EXQ-076b (MECH-116/ARC-032 goal conditioning, supersedes EXQ-076).
- **MECH-124 diagnostic:** When reviewing EXQ-074b/076b results, check whether z_goal
  salience is competitive with harm salience — if not, this is a V4 early risk indicator
  (consolidation-mediated option-space contraction).
- **0 pending review** as of 2026-03-25 (all experiments discussed and marked in
  review_tracker.json).
- **Phase gate:** SD-011 implementation → re-run blocked experiments → governance cycle.
- **Step 3.1 (Substrate Debt Resolution)** is the current active step; SD-008/009/010 are
  done; SD-011/012 remain.

---

## Status Snapshot (2026-03-20) — archived

- **V2 complete.** All three hard-stop criteria triggered after EXQ-028. Governance cycle
  run 2026-03-19: 7 decisions applied, V3-pending gate lifted, ARC-024 and SD-010
  registered.
- **V3 active.** 73 experiments run (through EXQ-059). Substrate SDs 004/005/006/007
  implemented. EXQ-030b PASS validated V3-form SD-003 attribution pipeline
  (attribution_gap=0.035, world_forward_r2=0.947). Current focus: SD-010 implementation
  (harm stream separation) to unblock ~10 pending FAILs.
- **Q-020 adjudicated:** ARC-007 strict (2026-03-16). HippocampalModule generates
  value-flat proposals; terrain sensitivity is a consequence of navigating
  residue-shaped z_world, not a separate hippocampal value signal.
- **17 pending FAILs** awaiting review (generated 2026-03-20). Root cause cluster:
  fused z_world containing harm signal → SD-010 substrate debt.
- `REE_assembly` is the canonical governance + specification repo. Current V3 roadmap
  is in §REE-v3 below; `v2_v3_transition_roadmap.md` is now historical.

---

## Status Snapshot (2026-02-28) — archived

- `REE_assembly` is the canonical governance + specification repo.
- `ree-v1-minimal` has served as the qualification harness: 8 genuine experiments
  completed (EXQ-000 through EXQ-007), 4 PASS, 4 informative FAIL (substrate-limited).
- Substrate debt items SD-001, SD-002, SD-003 registered. V1 has reached saturation
  for the claims it was designed to test. Further V1 runs (EXQ-008/009) complete the
  current evidence cycle; extended-seed reruns (EXQ-010–013) are low-priority confidence
  accumulation.
- V2 cutover gates passed 2026-02-18 but cutover was deferred. Correct decision: V2
  specification needs redesigning (Step 2.0, below) before implementation begins.
- JEPA integration guidance remains convergence-first: source-method details live in
  `REE_convergence`; `REE_assembly` keeps REE-first canonical contracts and adjudication
  outputs.

---

## Roadmap Discipline

**Each step must be completed in sequence. Before starting the next step:**

1. Record what was learned (update GOVERNANCE_STATE.md, substrate debt register, any
   affected claims).
2. Update this roadmap to reflect that learning — revise subsequent steps if the
   evidence changes what they should be.
3. Make the update-roadmap action explicit in the exit criteria of every step.

The roadmap is not a fixed plan; it is a living document that is deliberately updated at
each step boundary. Steps may be added, split, or reordered as understanding grows.

## V3 Completion Gate For First Paper (2026-03-31 clarification)

This section records the current planning boundary for when `ree-v3` should be considered
"complete enough" for the first real paper.

**Paper-1 target claim**

REE should support a narrow, defensible claim:

- A waking, single-agent REE substrate can learn stable self/world attribution, harm avoidance,
  and genuine goal-directed behavior from architectural separation rather than a monolithic
  reward objective.

**Must-pass gates**

- **Post-SD-011 SD-003 works in the current architecture.** Counterfactual attribution must
  succeed on the sensory-discriminative harm stream (`z_harm_s`), not only on the older
  `z_world` formulation.
- **Harm/attribution substrate is stable.** SD-005, SD-010, SD-011, and ARC-033 must be
  reliable enough to function as substrate rather than as active rescue work.
- **Goal-directed behavior is behaviorally real.** SD-012 and MECH-112 must produce a genuine
  GOAL_PRESENT vs GOAL_ABSENT behavioral lift, not just `z_goal` seeding.
- **Approach and avoidance compete in one selector.** ARC-030 must be demonstrated as dual
  evaluation of the same candidate trajectories by harm and goal channels inside a shared
  commitment process.
- **Results survive reruns.** Matched-seed reruns and at least one task variant must confirm
  the core behavior is not a one-task artifact.
- **Governance state is clean.** Review tracking, claim status, and experiment indexing must
  remain aligned enough for the evidence story to be legible to an external reader.

**Two-tier V3 completion (2026-04-02 clarification)**

V3 completion has two levels with distinct gates:

*V3 first-paper gate* (sufficient for Paper 1 claim):
- Habit-system goal-directed behavior demonstrated: SD-012 activates approach drive;
  EXQ-182a oracle confirms the environment is near-optimal for habit-level policy;
  goal-lift experiment (EXQ-074e successor) shows GOAL_PRESENT > GOAL_ABSENT behavioral
  lift with ARC-030 harm/goal competition in one selector.

*V3 full completion gate* (required before V4 entry):
- **HippocampalModule multi-step trajectory planning validated.** This is a V4
  prerequisite, not merely a V4 feature. V4's social extension ("sharing joys and
  sorrows", INV-029 benefit gradient) requires planning trajectories that affect
  another agent's z_harm_a accumulation and benefit_exposure over time. One-step
  greedy cannot reach this: it can approach its own resources but cannot plan paths
  that sustain another's joy or reduce another's sorrow over multi-step trajectories.
  The VTA/hippocampal system (MECH-163) must be validated in V3 to provide the
  planning substrate that V4 social cognition will depend on.
- All V3 first-paper gates passed.

See MECH-163 (dual goal-directed systems: habit vs hippocampally-planned).

**Explicit non-blockers for V3 *first-paper* completion**

- Sleep/offline consolidation mechanisms.
- Integrated self/other social modelling.
- Full language integration; simple future communication primitives are enough.
- nth-order multi-agent ethics tests.
- Full computational-psychiatry coverage.

**Deferred to V4/V5 / later papers** *(requires V3 full completion gates first)*

- Sleep-like consolidation as a load-bearing mechanism.
- Social coupling and other-modelling inside core substrate — **specifically requires
  hippocampal multi-step planning (MECH-163 VTA/planned system) from V3 full gate**.
- Structured communication between agents.
- Emergent ethical behavior in multi-agent settings.
- Stronger psychiatric modelling beyond single-agent perturbation analogs.
- **INV-043 (caregiver requirement)** — requires multi-agent substrate with modelled
  caregiving. V3 cannot test whether ethical capacity is *motivationally activated*
  (vs merely architecturally present). This is a first-class V4 research question.
- **MECH-158 (love-exclusion failure mode)** — requires developmental multi-agent
  substrate to test whether absence of love-experience collapses ethical motivation.
- **MECH-159 (intergenerational moral progress)** — requires multi-generation agent
  infrastructure. V5 scope or later.

*The distinction between V3 and V4 is not only scope but epistemological level:
V3 tests whether the machinery works. V4 tests whether the machinery develops correctly.
The ARC-043 stack makes this precise: V3 exercises Layers 6-9; V4 must exercise Layers
2-5 dynamically, with caregiving, developmental phases, and social residue.*

**Deployment constraint:** V3 may be used as a sandboxed scientific substrate, but
serious capability scale-up or external-world connectivity is deferred until V4
social/developmental completion. Language alone is not treated as sufficient
safety. See `docs/governance/deployment_gating.md`.

---

## Phase Definitions

### REE-v1 ✓ (completed purpose: qualification baseline)

**Primary role:** validate whether proposed mechanisms produce expected directional
effects under controlled conditions.

**Outcome:** useful for signal discovery and contract hardening. Not sufficient as final
architecture target due to stress-lane conflicts, limited environment breadth, and
accumulated substrate debt (SD-001, SD-002, SD-003). Four genuine PASSes confirm core
signal structure; four informative FAILs confirm substrate resolution limits, not
architecture failures.

**Post-V1 learning incorporated into roadmap:**
- E2/hippocampus conflation (SD-001) prevents clean mechanistic isolation
- E1/E2 mutual constitution (SD-002) reframes timescale-separation interpretation
- E2 self-attribution substrate (SD-003) is an unmet V2 design requirement
- V1 stateless grid cannot surface persistent agent causal footprint
- MECH-057 (control completion) requires multi-step environment with genuine commitment
  pressure; needs richer substrate before further testing

---

### REE-v2 ✓ (completed purpose: V2 qualification)

**V2 series closed after EXQ-028 (2026-03-19).** All three hard-stop criteria met.
Governance cycle completed 2026-03-19.

#### Step 2.0 — V2 Redesign ✓

**Primary role:** Produce an updated V2 specification that incorporates V1 learning.
The original V2 spec (representation-interface contract) remains in scope, but the
design must now account for SD-001/002/003 and explicitly address what V2 must deliver
to make future self-attribution and self-modelling experiments possible.

**In-scope:**
- Redesign V2 architecture to resolve SD-001: E2 separated as pure transition MLP,
  HippocampalModule created as distinct component of E3 complex
- Revise V2 entry criteria to include SD-003 requirements (see below)
- Produce first-pass V2 implementation spec: subsystem boundaries, required metrics,
  failure gates
- Define the persistent-causal-footprint environment requirement (SD-003)
- Capture mutual constitution (SD-002) in architecture documents

**Out-of-scope:**
- Implementation (code changes happen in Step 2.1 onward)
- New V1 experiments beyond EXQ-008/009

**Exit criteria:**
- Updated V2 implementation spec document exists with SD-001/002/003 addressed
- V2 entry criteria revised (see below)
- This roadmap updated with Step 2.1–2.5 refined based on redesign output
- GOVERNANCE_STATE.md SD-003 entry complete ✓ (done 2026-02-28)

**Outcome:** ✓ Complete. V2 spec produced (`docs/architecture/ree_v2_spec.md`). SD-001/002/003
addressed in design. Steps 2.1–2.5 scoped.

---

#### Step 2.1 — E2 Separation (SD-001 resolution) ✓

**Primary role:** Refactor E2 into a pure fast transition model. Create HippocampalModule
as a distinct component of the E3 complex. Close SD-001.

**In-scope:**
- `E2FastPredictor` → pure forward predictor: `forward(z, a) → z_next` (cerebellum-like)
- `HippocampalModule` (new) → trajectory proposal by navigating affective terrain; not
  by running transition predictions
- Counterfactual E2 querying made architecturally possible: `e2.forward(z, a_cf)`
- SD-001 closed in GOVERNANCE_STATE.md

**Out-of-scope:**
- Full E3 complex redesign (Step 2.2+)
- Self-attribution experiments (Step 2.4)

**Exit criteria:**
- E2 callable independently with arbitrary action input
- HippocampalModule exists as separate class
- Existing EXQ PASS results replicated on refactored substrate (parity check)
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. E2 is a pure fast transition MLP on z_self. HippocampalModule
created as distinct E3 component. SD-001 closed.

---

#### Step 2.2 — Representation Interface Contract ✓

**Primary role:** Lock stable representation-interface contract for sensing adapters
and E1/E2 latent prediction. This is the original primary V2 role, now sequenced after
E2 separation.

**In-scope:**
- Sensor adapters mapped to JEPA-like context/target latent interfaces
- E1/E2 representation-reference integration contract (`IMPL-022`)
- Stable output streams for latent prediction error and uncertainty
- Run-pack/adapter-signal compliance and calibration metrics

**Out-of-scope:**
- Full control-plane completion
- Hippocampal/E3 commitment architecture
- Full ethical arbitration dynamics

**Exit criteria:**
- Representation-interface contract stable across qualification and stress lanes
- Uncertainty/error streams calibrated and non-gamed across distribution shifts
- No unresolved adapter contract drift
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. MECH-059 PASS confirmed E1 precision and E3 confidence are
structurally independent. Representation interface stable.

---

#### Step 2.3 — Persistent Causal Environment ✓

**Primary role:** Upgrade the environment substrate so that persistent agent causal
footprint is present — actions at step N affect the landscape at step N+k in ways
that require disambiguation from independent environment change. This is the
prerequisite for SD-003 experiments.

**In-scope:**
- Environment design where agent-caused and environment-caused transitions are
  structurally distinct and must be separated for correct attribution
- Validation that E2 (now pure transition model from Step 2.1) can be queried
  counterfactually against this environment

**Out-of-scope:**
- Full self-attribution claim testing (Step 2.4)

**Exit criteria:**
- Environment exists with persistent agent causal footprint
- Baseline experiments confirm agent-caused / environment-caused distinguishability
- Roadmap updated with any discoveries

**Outcome:** ✓ Complete. CausalGridWorld implemented with persistent agent causal
footprint. EXQ-018 PASS confirmed agent-caused/environment-caused distinguishability.

---

#### Step 2.4 — Self-Attribution Substrate ✓ (V2 partial; V3 form validated)

**Primary role:** Implement and test counterfactual E2 querying for self-modelling.
First genuine experiments on self-attribution claims. Close SD-003.

**In-scope:**
- Counterfactual E2 queries integrated into agent decision loop
- First genuine experiments isolating agent-caused vs environment-caused harm
- Self-attribution claim coverage (claims to be identified during Step 2.0 redesign)
- SD-003 closed in GOVERNANCE_STATE.md

**Exit criteria:**
- At least one genuine PASS on a self-attribution claim
- E2 counterfactual querying demonstrated experimentally
- Roadmap updated with any discoveries

**Outcome:** ✓ Partial / hard stop. EXQ-027 FAIL triggered V2 hard stop: E2 cannot
discriminate agent-caused harm in z_gamma; SD-005 substrate required. V2
self-attribution experiments concluded. V3-form SD-003 validated at EXQ-030b PASS
(2026-03-18): attribution_gap=0.035, world_forward_r2=0.947. Full SD-003 achieved on
V3 substrate with z_world separation.

---

#### Step 2.5 — V2 Qualification ✓

**Primary role:** Genuine experiment coverage across core V2 claims. Sufficient evidence
to make V3 entry decision.

**Exit criteria:**
- Representation interface stable across qualification and stress lanes (from Step 2.2)
- Self-attribution substrate tested (from Step 2.4)
- Governance confidence above provisional thresholds for core V2 claims
- **Roadmap updated with V1+V2 learnings before V3 begins**
- V3 entry decision made explicitly

**Outcome:** ✓ Complete. V2 series closed after EXQ-028. 15 genuine V2 experiments
(EXQ-014–028): 5 structural-separation PASSes, 9 FAILs (all substrate-limited by
z_gamma conflation or SD-004 absence). Governance cycle 2026-03-19: 7 decisions
applied. V3 entry formally made.

---

### REE-v3 ← **current phase** (control completion + full attribution)

**Primary role:** Implement full attribution pipeline, control-plane heartbeat architecture,
and E3 commitment/accountability on the z_self/z_world split substrate (SD-004/005).

#### Step 3.0 — V3 Substrate Implementation ✓

SD-004 (E2 action objects; HippocampalModule navigates action-object space O), SD-005
(z_gamma → z_self + z_world split), SD-006 (asynchronous multi-rate heartbeat,
time-multiplexed phase 1), SD-007 (ReafferencePredictor for perspective-corrected
z_world). Q-020 adjudicated: ARC-007 strict (2026-03-16). CausalGridWorld extended
to V3 environment. EXQ-030b PASS: SD-003 attribution pipeline validated.

#### Step 3.1 — Substrate Debt Resolution ← **current step**

**In-scope:**
- SD-008: alpha_world ≥ 0.9 in LatentStackConfig ✓ (validated EXQ-040)
- SD-009: event-contrastive CE auxiliary loss for z_world encoder ✓ (EXQ-020 PASS)
- SD-010: harm stream separation ✓ (EXQ-056c/058b/059c PASS)
- SD-011: dual nociceptive streams (z_harm_s + z_harm_a) ← **current focus**
- SD-012: homeostatic drive modulation for z_goal seeding ← **next**

**Exit criteria:**
- SD-011 implemented and EXQ-093/094 successors run on dual-stream substrate
- SD-003 counterfactual redesigned for z_harm_s pipeline and validated
- SD-012 implemented; EXQ-085 successors (wanting/liking) runnable with functional z_goal
- Pending FAIL cluster (~10 experiments) reviewed after SD-011 implementation

#### Step 3.2 — V3 Claim Qualification

**In-scope:**
- ARC-016: E3-derived dynamic precision + end-to-end commitment→behavior behavioral distinction
- MECH-025: action-doing mode probe on V3 substrate
- MECH-057b: completion gate retest
- Q-007: valence-precision interaction
- SD-006: multi-rate loop validation at scale (ARC-023, MECH-089–093)
- MECH-090: beta-gated policy propagation
- ARC-024: harm attribution with SD-010 substrate
- Full V3-EXQ series (V3-EXQ-001 through V3-EXQ-010 as designed in transition roadmap)

**Exit criteria:**
- Governance confidence above provisional thresholds for core V3 control claims
- V3-pending claims adjudicated (ARC-007, ARC-016, ARC-018, MECH-025, MECH-033, Q-007)
- **Roadmap updated with V1+V2+V3 learnings before V4 begins**

#### Step 3.3 — V3 Governance Cycle and V4 Entry Decision

**Exit criteria to start V4:**
- Robust separation of exploratory simulation vs committed learning
- Stable behaviour under adversarial trajectory pressure
- Governance confidence above provisional thresholds for core control claims
- V4 entry decision made explicitly

---

### REE-v4 (later: social and institutional complexity)

**Primary role:** Scale to richer multi-agent coupling, language-mediated coordination,
and institutional constraints.

**Exit criteria:** To be defined during V3, informed by what V3 delivers.

---

## V2 Entry Criteria (revised 2026-02-28)

Original criteria (all still required):
- Representation-interface contract stable across qualification and stress lanes
- Uncertainty/error streams calibrated and non-gamed across distribution shifts
- No unresolved adapter contract drift

Added from V1 learning:
- **SD-001 resolved**: E2 implemented as pure isolatable transition model; HippocampalModule
  exists as separate component of E3 complex
- **SD-003 requirement**: Counterfactual E2 querying architecturally possible
  (`e2.forward(z, a_counterfactual)` callable independently)
- **Persistent causal environment**: environment substrate provides persistent agent
  causal footprint, enabling agent-caused vs environment-caused transition disambiguation

---

## Repository Roles

- `REE_assembly`: canonical claims, architecture docs, evidence matrix, governance outputs.
- `ree-v3`: **primary qualification lane** for V3 experiments and claim coverage. Default
  branch: `main`. Results go to `REE_assembly/evidence/experiments/`.
- `ree-v2`: transitional reference. V2 series complete (EXQ-014–028). No new experiments.
- `ree-v1-minimal`: legacy baseline/reference harness. No new mechanism development.
- `ree-experiments-lab`: **ARCHIVED** 2026-02-26. Synthetic scaffolding only; do not use.

---

## Immediate Work Queue (This Cycle)

**Current step: SD-003 Successor Validation + First-Paper Gate (as of 2026-04-18)**

SD-004 through SD-023 all implemented. ARC-033, MECH-090 (bistable + Layer 1 trajectory
stepping), MECH-091 Layer 2 urgency interrupt, MECH-120, MECH-203/204, MECH-205, MECH-216
implemented. **SD-003 superseded 2026-04-18** by MECH-256 + SD-029 + MECH-257. Governance
cycle 2026-04-18 applied 2 hold_pending_v3_substrate (SD-014, SD-023). 0 pending review.
Second Hetzner worker (ree-cloud-2) onboarded.

1. **V3-EXQ-433** (SD-029 event-conditioned single-pass comparator on z_harm_s — decisive
   test of the new self-attribution topology after SD-003 supersession; next-up priority=60).
2. **V3-ONBOARD-smoke-ree-cloud-2** (second Hetzner worker calibration smoke).
3. **V3-EXQ-321c** (MECH-090 bistable vs legacy gate hold rate, spike-aligned E3-tick fix).
4. **V3-EXQ-325b** (SD-021 descending pain modulation retest, E2 world-forward training fix).
5. **V3-EXQ-330a** (SD-013 contrastive counterfactual retest).
6. **V3-EXQ-418b** (SD-016+SD-017 context-conditioned action: SHY fix + terrain_loss).
7. **V3-EXQ-326 / V3-EXQ-326a** (SD-015 wanting-gradient nav and MECH-229 behavioral
   dissociation fix).
8. **V3-EXQ-434 / V3-EXQ-406b** (INV-053 depression attractor replication; 5-seed
   LONG_HORIZON characterisation).
9. **V3-EXQ-435** (INV-054 phase-transition recovery, sustained-crossing criterion,
   supersedes EXQ-278).
10. **V3-EXQ-436** (SD-017 sleep phase ablation redesign with context-conditioned harm
    threshold, supersedes EXQ-242).
11. **V3-EXQ-429b** (INV-044 Bayesian prior-before-posterior; SWS-ordered vs REM-only).
12. **V3-EXQ-407** (MECH-231 E2 short-horizon efference-copy discriminative pair).

---

## ARC-057 Environment-Complexity Gate (2026-04-14)

**Status: PARKED.** ARC-057 (curiosity-approach emergence) cannot be faithfully tested
in the current CausalGridWorld. The mechanism requires an environment where
representational expansion at a location captures genuinely additional information --
near-fractal complexity where zooming in reveals more structure. Grid cells are
informationally flat: a cell is a cell. See `docs/architecture/hippocampal_valence_asymmetry.md`.

**What this blocks:** Faithful testing of approach-via-representational-expansion (MECH-232),
the valence encoding asymmetry (MECH-233), and the curiosity-approach emergence (ARC-057).

**What this does NOT block:** The threat/avoidance side (harm residue field, BLA-pathway
logic) remains fully testable. All existing V3 architecture work continues. The claims
are registered and constrain future design even without experiments.

### Proxy mechanism policy

Any experiment testing approach behavior in the grid world will necessarily use a **proxy
mechanism** for the approach signal (e.g., explicit wanting gradient, DA-modulated place
priority, or direct goal-location bias). This is acceptable for testing downstream
architecture (commitment gating, trajectory selection, E3 evaluation) but carries a
contamination risk:

**Results obtained with a proxy approach mechanism may not generalize to an ARC-057-enabled
agent.** The proxy is a commanded gradient; ARC-057 is emergent from representational
expansion + curiosity. The downstream architecture may develop implicit dependencies on
proxy properties (e.g., gradient smoothness, signal strength, spatial extent) that the
real mechanism would not provide.

### Tagging requirements

1. **Any experiment that tests approach behavior** must declare in its docstring and
   manifest notes which proxy mechanism it uses for the approach signal.
2. **Tag**: experiments using a proxy approach mechanism should include `approach_proxy`
   in their tags. This enables future filtering when ARC-057 becomes testable.
3. **Evidence interpretation**: PASS results for claims that depend on approach behavior
   should carry an `evidence_quality_note` stating the proxy was used and results may not
   transfer to ARC-057-enabled substrate.
4. **Re-validation queue**: when a richer environment becomes available, all `approach_proxy`
   tagged experiments form the re-validation backlog.

### What "richer environment" requires

- More sensory input channels (visual texture, object features, spatial micro-structure)
- Larger latent spaces to encode location-dependent detail
- Significantly more compute for training
- Location-dependent information density (some areas genuinely have more to discover)

This is a V5+ concern. V3 and V4 proceed with proxy mechanisms and honest tagging.

---

## Open Questions

- **SD-010 HarmEncoder architecture**: should z_harm be a separate stream alongside
  z_world and z_self, or should it route through z_world after SD-010? The `l_space.md`
  architecture suggests a four-stream model (z_self, z_world, z_beta, z_harm).
- **ARC-016 E3-derived precision**: EXQ-038 FAIL — root cause (precision invariance)
  needs analysis before designing the next precision-regime experiment.
- **SD-006 phase 2**: time-multiplexed multi-rate is phase 1; true asynchronous
  execution (thread-based or event-loop) is still open. HTA (hierarchical temporal
  abstraction) is the recommended direction but not yet designed.
- **ARC-057 environment substrate**: what is the minimum environment complexity that
  would enable faithful testing of curiosity-approach emergence? Is a continuous 2D
  world with procedural texture sufficient, or does it require full 3D/visual input?
  See ARC-057 gate section above.

---

## Related Claims

- IMPL-008, IMPL-020, IMPL-021, IMPL-022
- MECH-057, MECH-058, MECH-059, MECH-060, MECH-063
- ARC-024, MECH-069, MECH-070, MECH-089, MECH-090, MECH-100, MECH-101, MECH-102
- SD-010 (harm stream separation)

## References

- `docs/architecture/jepa_ree_hybrid_diagram_spec.md`
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `evidence/GOVERNANCE_STATE.md` (substrate debt register: SD-001, SD-002, SD-003)
- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/planning/CUTOVER_REE_V2_READINESS.md`
