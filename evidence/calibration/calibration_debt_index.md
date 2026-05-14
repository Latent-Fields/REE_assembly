# Calibration Debt Index

**Created:** 2026-05-13  
**Updated:** 2026-05-14  
**Source spec:** `docs/thoughts/2026-05-13_calibration_debt.md`  
**Scope:** Substrates that have passed contract tests (or partial implementation) but remain behaviourally unvalidated due to calibration, seam, or read-side-consumer problems.

Purpose: prevent premature retirement of mechanisms that passed substrate tests but have not yet received adequate effect-size, timing, sign, threshold, or read-side-consumer calibration.

---

## Calibration failure types

A substrate enters calibration debt when at least one of the following is true:

| # | Code | Description |
|---|------|-------------|
| 1 | silent-by-default | Module exists but default flag leaves it silent |
| 2 | gate-open-zero-signal | Gate is open but signal remains zero |
| 3 | small-effect | Signal exists but effect size is too small |
| 4 | write-no-read | Signal writes but is not read downstream |
| 5 | score-bias-no-action | Score bias exists but action selection is unchanged |
| 6 | contract-not-behavioural | Local contract tests pass but behavioural tests fail |
| 7 | saturated-metric | Metric saturated at 0 or 1, making effect invisible |
| 8 | mismatched-convention | Action/no-op/stream conventions mismatched |
| 9 | conservative-threshold | Thresholds never swept after initial conservative choice |
| 10 | uncalibrated-weights | Multiple substrates active but relative weights uncalibrated |

---

## Calibration ladder

Substrates must clear each rung before a behavioural experiment is interpretable.

| Rung | Gate | Description |
|------|------|-------------|
| 0 | module-exists | Module present in code |
| 1 | flag-on | Flag enabled, no crash |
| 2 | signal-nonzero | Internal signal non-zero |
| 3 | gate-open | Downstream gate open |
| 4 | write-fires | Write-site fires |
| 5 | read-consumes | Read-side consumer reads signal |
| 6 | score-changes | Score or latent changes |
| 7 | action-changes | Action or replay changes |
| 8 | metric-changes | Behavioural metric changes |
| 9 | claim-testable | Downstream claim becomes testable |

---

## Main index

Columns: claim_id | substrate_status | last_exp (outcome) | rung_failed | failure_signature | likely_calibration_class | next_sweep | priority | downstream_unblocks

### Priority 1 — project multipliers

| claim_id | substrate_status | last_exp (outcome) | rung_failed | failure_signature | calib_class | next_sweep | downstream_unblocks |
|----------|-----------------|-------------------|-------------|-------------------|-------------|------------|---------------------|
| **ARC-065** diversity stack (umbrella) | partial: MECH-313 + MECH-314 component readiness PASSed; V3-EXQ-563a confirms E3 score-bias seam is alive when first-action support exists; normal CEM support remains the primary bottleneck | V3-EXQ-563a scaffold actuator retest (PASS/non_contributory 2026-05-14): scaffold support present, forced nonzero bias applied, action_0_fraction shifted from 0.0 to 1.0 under strong forced bias | **pre-Rung 7**: Layer 1 CEM candidate-support collapse in the normal proposer; post-CEM motivation can only act on alternatives supplied by HippocampalModule/CEM | V3-EXQ-563: candidate_first_action_entropy=0.0 all arms, forced_bias_abs_mean=0.0 even in forced-nonzero arm because target class absent. V3-EXQ-563a: min_candidate_unique_first_action_classes=5 and forced_bias_abs_mean=100.0 under scaffold, proving E3 can use score_bias when support exists | upstream CEM collapse blocking measurement + uncalibrated score-bias magnitude (10) | V3-EXQ-563b queued: compare normal CEM, scaffold support, support-preserving CEM, and weak forced-bias dose response; do not claim agency solved until natural selected_action_entropy/task diversity improves | sleep experiments, ARC-062 rule apprehension, SD-029 |
| **MECH-313** stochastic noise floor | landed: V3-EXQ-544 supports (2026-05-10) | V3-EXQ-544 (supports 2026-05-10) | none at substrate level | Not yet tested in integration with MECH-314 / MECH-320 | uncalibrated-weights (10) | noise_floor_alpha + noise_floor_min_temperature sweep in ARC-065 combined arm | ARC-065, ARC-062 |
| **MECH-314** structured curiosity | partial: V3-EXQ-545 non_contributory; per-candidate novelty Phase 1 only; broadcast uncertainty/learning-progress pending | V3-EXQ-545 (non_contributory 2026-05-10) | Rung 6: score bias may not discriminate at current scale | Curiosity bias not discriminating at substrate readiness scale; broadcast phases not yet activated | small-effect (3) + uncalibrated-weights (10) | curiosity_novelty_weight + curiosity_bias_scale sweep; per-candidate vs broadcast comparison | ARC-065, sleep, ARC-062 |
| **MECH-320** tonic vigor | landed: V3-EXQ-547 non_contributory (substrate readable; v_t not moving); V3-EXQ-549 non_contributory (discriminative pair); sign/scale root cause confirmed 2026-05-14; v_t_floor fix implemented in substrate | V3-EXQ-563a scaffold actuator retest (PASS/non_contributory 2026-05-14) confirms forced actuator seam is live once candidate support exists; natural MECH-320 v_t remains sign/scale blocked | **Rung 2 confirmed** plus proposal-surface blocker: reward_signal = -float(score), E3 score ~70, v_raw approx -70, v_t = max(0, -70) = 0; candidate collapse prevents fair behavioural readout of small natural biases | v_raw sign inverted (E3 lower-is-better score is large positive; negation makes v_raw deeply negative; ReLU gate zeroes it). V3-EXQ-563a proves forced score_bias can move action under scaffold support, but natural v_t/bias scale remains unresolved | gate-open-zero-signal (2) + mismatched-convention (8) + upstream candidate support (7) | V3-EXQ-563b queued for weak forced-bias dose response after candidate-support repair; natural MECH-320 sign/scale still requires separate fix/calibration | ARC-065, action selection, wanting/approach pipeline |
| **GOAL-PIPELINE** (MECH-216 / MECH-307 / ARC-030) | partial: modules wired (V3-EXQ-559a liveness PASS); end-to-end behaviourally inert | V3-EXQ-560 goal-stream selectivity/score-decomp (non_contributory 2026-05-13); candidate collapse, score rank-constant | **Rung 5/6**: write fires, score rank-constant; candidate collapse upstream blocks measurement | approach_commit_rate=0; action entropy 0.0; candidate unique action classes=1.0 all arms; z_goal norm rises on seeding but no action shift; score/bias rank-constant across candidates | score-bias-no-action (5) + write-no-read (4) + upstream candidate collapse (7) | goal-stream calibration ladder (8 rungs): forced z_goal -> forced VALENCE_WANTING -> forced schema_salience -> reactive wanting -> predictive wanting -> sustained drive -> MECH-295 bridge -> full naturalistic | resource-seeking, wanting/liking dissociation, approach-side BG, later ethical development, MECH-295 |
| **SD-017** sleep phase substrate | partial: loop scaffold landed; Phase B-E flags default-false; routing weights written but not consumed | V3-EXQ-418l SD-017 action-bias diversity phase2 (non_contributory 2026-05-09); V3-EXQ-265a methods validation phase2 (PASS 2026-05-09) | **Rung 5**: read-side consumer; routing weights written but not downstream-consumed | Phase B-E flags default-false; routing weights not consumed; sleep fires too infrequently; waking behavior monomodal -- nothing useful to consolidate | silent-by-default (1) + write-no-read (4) + driver-frequency | Phase B-E enablement check -> routing-consumer check -> step-size sweep -> cycle-count sweep; requires ARC-065 waking diversity first | rule consolidation, memory consolidation, goal consolidation, INV-049 sleep-necessity claim |

### Positive calibration exemplar (RESOLVED)

| claim_id | substrate_status | last_exp (outcome) | resolution |
|----------|-----------------|-------------------|------------|
| **MECH-204** precision recalibration | resolved: default step updated 0.1 -> 0.25 | V3-EXQ-541c step-size sweep extended cycles (PASS 2026-05-09) after V3-EXQ-541b FAIL | conservative-threshold (9) fixed by sweep: 16-cycle exposure vs 8-cycle was the discriminating variable |

---

### Priority 2 — close specific high-value seams

| claim_id | substrate_status | last_exp (outcome) | rung_failed | failure_signature | calib_class | next_sweep | downstream_unblocks |
|----------|-----------------|-------------------|-------------|-------------------|-------------|------------|---------------------|
| **ARC-062** rule apprehension | partial: gated-policy substrate + SD-054 bipartite readiness PASSed (V3-EXQ-548); monomodal-collapse falsifier blocked | V3-EXQ-543d ARC-062/MECH-260 factorial falsifier (non_contributory 2026-05-12); V3-EXQ-543c bipartite falsifier (non_contributory 2026-05-11) | **pre-Rung 2**: input variance failure upstream | Total-variation distance exactly zero across seeds/windows/probe states; CEM candidates near-indistinguishable; policy head cannot learn distinct rules on identical inputs | uncalibrated-weights (10) upstream in candidate generation | candidate-distinguishability diagnostic (first-action entropy, L2 spread, world_states[1] pairwise distance) -> activate ARC-065 -> re-test | rule-based safety, SD-033 OCD-axis, Q-043/044/045 |
| **SD-015** resource identity | partial: proximity regression worked; z_world outperforms z_resource for goal alignment (V3-EXQ-322a) | V3-EXQ-322a z_resource vs z_world goal-alignment comparison (approximate: z_world > z_resource) | Rung 6: signal exists but wrong mixture ratio | z_resource contributes but z_world dominates; hybrid seeding not yet tested; calibration may be mixture, not strength | uncalibrated-weights (10) | hybrid seed sweep: z_goal_seed = a*z_resource + (1-a)*z_world, a in {0.0, 0.25, 0.5, 0.75, 1.0} | wanting/liking dissociation, multi-resource identity, goal representation |
| **SD-049** resource encoder Phase 2 | partial: Phase 1 env PASS (V3-EXQ-513); Phase 2 hybrid encoder implemented; V3-EXQ-514f behavioural validation non_contributory | V3-EXQ-514f Phase 2 reef behavioural validation (non_contributory 2026-05-12) | TBD per 6-row interpretation grid in verdict.md | identity-recovery and wanting!=liking dissociation not yet demonstrated; candidate collapse may be the same upstream blocker as goal pipeline | see verdict.md 6-row grid | V3-EXQ-514f review per interpretation grid -> derive next experiment per applicable row | SD-015, MECH-229, MECH-230 |
| **MECH-295** approach bridge | partial: isolation tests PASSed; cascade behavioural validation inert under realistic policy state | V3-EXQ-560 (non_contributory 2026-05-13; approach inert in full goal-stream diagnostic) | **Rung 5/6/7** cascade failure | cue activation zero under realistic policy; drive-to-approach cascade inert; isolation PASS but upstream goal state doesn't propagate through | write-no-read (4) + score-bias-no-action (5) | MECH-295 cascade ladder: cue injection -> liking-stream injection -> drive-scaled liking -> naturalistic cue -> lesion bridge | ARC-030, goal approach, wanting/liking dissociation |
| **MECH-260** anti-recency | present: active in ARC-065 diversity stack | V3-EXQ-543d factorial (non_contributory 2026-05-12; candidates indistinguishable, MECH-260 contribution unmeasurable) | blocked by same pre-Rung 2 upstream as ARC-062 | Cannot assess MECH-260 contribution when candidates are indistinguishable | uncalibrated-weights (10) -- upstream blocking | ablation arm in ARC-065 matched-entropy sweep (MECH-260 on/off) | ARC-062, ARC-065 |

---

### Priority 3 — later refinement after primary streams alive

| claim_id | substrate_status | likely_calibration_class | unblocked_by | notes |
|----------|-----------------|--------------------------|--------------|-------|
| **MECH-314b** uncertainty curiosity (broadcast) | Phase 1 only; broadcast phase pending | uncalibrated-weights (10) | MECH-314 Phase 1 calibration | Per-candidate uncertainty requires environment exposure data |
| **MECH-314c** learning-progress curiosity (broadcast) | Phase 1 only; broadcast phase pending | uncalibrated-weights (10) | MECH-314 Phase 1 calibration | Requires time-series of per-candidate loss trajectories |
| **SD-032 / drive consumer cascade** | partial | write-no-read (4) | GOAL-PIPELINE calibration | Per-axis drive signals written but consumer cascade incomplete |
| **sleep arousal-triggered entry** | not yet landed | silent-by-default (1) | SD-017 sleep substrate calibration | Entry-frequency calibration blocked until basic sleep loop is validated |
| **multi-strategy rule scaling** | not yet tested | small-effect (3) | ARC-062 calibration | Requires ARC-062 to first produce distinguishable rule-specific behaviour |

---

## Calibration status template

Per-substrate block format for detailed tracking:

```yaml
calibration_status:
  substrate_landed: true
  contract_tests_pass: true
  behavioural_effect_seen: false
  default_active: false
  gate_open_in_failed_run: unknown      # true/false/unknown
  signal_nonzero_in_failed_run: unknown # true/false/unknown
  read_side_consumed: unknown           # true/false/unknown
  effect_size_sweep_done: false
  saturation_checked: false
  sign_convention_checked: false
  identity_mapping_checked: false
  rung_reached: 3                       # highest rung confirmed
  recommended_next_step: calibration_ladder
```

---

## Work packages

| Package | Focus | Status |
|---------|-------|--------|
| **A** (this doc) | Calibration registry | **done 2026-05-13** |
| **B** | ARC-065 / MECH-320 combined heartbeat: candidate support and bias-scale calibration | V3-EXQ-563a PASS/non_contributory 2026-05-14 confirms E3 forced score-bias seam when scaffold support exists; normal CEM candidate support is primary bottleneck; V3-EXQ-563b queued for support-preserving CEM and forced-bias dose response |
| **C** | Goal-stream calibration ladder: forced -> naturalistic | pending |
| **D** | Sleep calibration: Phase B-E flags, routing-consumer check, cycle-count sweep | pending -- requires ARC-065 first |
| **E** | ARC-062 input distinguishability: candidate variance, TV distance, head separability | pending |

### Work Package B target experiment

Six arms for the ARC-065 / MECH-320 combined heartbeat:

```
ARM_0: baseline (no diversity modules)
ARM_1: MECH-313 noise floor only
ARM_2: MECH-314 structured curiosity only
ARM_3: matched-entropy random noise (entropy-controlled control)
ARM_4: MECH-313 + MECH-314 + MECH-320 combined
ARM_5: all combined + MECH-260 anti-recency
```

Acceptance: structured curiosity must produce more useful behavioural diversity than matched entropy alone.

Primary metrics: action_class_entropy, state_coverage, trajectory_diversity, rule-relevant transition count, hazard excess, commitment collapse, sleep-refinable variation.

### Work Package C target sequence (goal-stream ladder)

```
Rung 1: forced z_goal injection
Rung 2: forced VALENCE_WANTING write
Rung 3: forced schema_salience
Rung 4: reactive resource-proximity wanting
Rung 5: predictive wanting
Rung 6: sustained-drive sweep
Rung 7: MECH-295 bridge sweep
Rung 8: full naturalistic run
```

Each rung must prove one seam: write-site fires, read-site consumes, score bias moves, action selection moves, resource contact occurs, z_goal seeds, replay consolidates.

---

*Index is a standing artefact. Update last_exp column and rung_failed when new calibration experiments complete.*
