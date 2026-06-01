# Failure Autopsy: V3-EXQ-592e (MECH-090 readiness conjunction validation)

**Generated:** 2026-06-01T19:09:47Z
**Scope:** single
**Status:** confirmed
**Autopsy session:** failure-autopsy-v3-exq-592e-20260601T190500Z
**Routing decision:** `/queue-experiment` for V3-EXQ-592f, a minimal commitment-state transition authority probe. No claim-registry, manifest, review-tracker, substrate-queue, or queue edits were applied in this session.

## 1. Target and facts

| Field | Value |
|---|---|
| Queue id | V3-EXQ-592e |
| Run id | `v3_exq_592e_mech090_readiness_conjunction_validation_20260601T180923Z_v3` |
| Manifest | `REE_assembly/evidence/experiments/v3_exq_592e_mech090_readiness_conjunction_validation_20260601T180923Z_v3.json` |
| Script | `ree-v3/experiments/v3_exq_592e_mech090_readiness_conjunction_validation.py` |
| Claim ids | `["MECH-090"]` |
| Experiment purpose | `diagnostic` |
| Supersedes | V3-EXQ-592d |
| Outcome | FAIL |
| Manifest evidence_direction | `does_not_support` |

592e was the corrected successor to 592d. It fixed the 592d commit-entry-count measurement defect by shifting C1 to a hold-rate criterion and forcing an uncommitted P2 entry. It did not rerun the old bad predicate.

Per-arm aggregate facts from the manifest:

| Arm | hold_rate | total_commits | score blocks | nav blocks | beta-elevated fraction from per-cell totals |
|---|---:|---:|---:|---:|---:|
| ARM_0 baseline both off | 1.000 | 0 | 0 | 0 | 1.000 |
| ARM_1 score-margin only | 1.000 | 0 | 1793 | 0 | 0.000 |
| ARM_2 nav-competence only | 1.000 | 0 | 0 | 150 | 0.921 |
| ARM_3 both gates on | 1.000 | 0 | 2088 | 150 | 0.000 |

Acceptance facts:

- C1 baseline hold-rate fired: PASS.
- C2 score-margin discrimination: FAIL, because ARM_1 hold_rate stayed 1.0 despite 1793 score-margin blocks.
- C3 nav-competence discrimination: FAIL, because ARM_2 hold_rate stayed 1.0 despite 150 nav blocks.
- C4 conjunction suppresses and recovers: FAIL, because ARM_3 hold_rate stayed 1.0 despite both gates firing.
- All arms had total_commits = 0 / commit_rate = 0.0, so entry counts remain unusable as the primary signal.

## 2. Actual code path

592e sets `cfg.heartbeat.beta_gate_bistable = True` in the arm config. That makes the not-yet-elevated transition tick the key admission point.

Score-margin gate:

- The official score-margin block counter is in `BetaGate.should_admit_elevation()`: when `use_commit_readiness_gate=True` and `margin < commit_readiness_floor`, it increments `mech090_n_elevation_blocked` and returns false.
- In bistable mode, `REEAgent.select_action()` calls `should_admit_elevation()` only under `result.committed and not beta_gate.is_elevated`.
- Therefore score-margin blocks are admission/elevation blocks. In bistable mode they do not test already-elevated maintenance unless the harness first releases or prevents elevation.

Navigation-competence gate:

- `CommitReadiness.is_above_floor()` reads the current readiness scalar.
- `REEAgent.select_action()` computes `_readiness_admits` whenever the conjunction is on and `result.committed` is true.
- If `_readiness_admits` is false, `commit_readiness.notify_block()` increments `n_blocks_emitted`.
- The block counter can rise even in an already rv-low committed-selection regime, but the failed predicate is only AND-composed into the elevation call. It does not itself call `beta_gate.release()` or clear `e3._committed_trajectory`.

Commitment release paths:

- `BetaGate.release()` exists and is used by separate release mechanisms: hippocampal completion, urgency interrupt, V_s anchor invalidation, relief completion, conditioned safety, contextual safety, and the SD-034 closure operator.
- No current score-margin or nav-readiness failure path releases an already-elevated beta latch in the bistable branch.

State measurement issue:

- `E3TrajectorySelector.select()` sets `e3._committed_trajectory` whenever `running_variance < commit_threshold`, before BetaGate admission is considered.
- 592e's hold_rate counts `agent.e3._committed_trajectory is not None`. That measures the upstream rv-low E3 selection state, not necessarily BetaGate policy-output hold.
- This is why ARM_1 and ARM_3 can have hold_rate = 1.0 while beta-elevated fraction = 0.0: E3 keeps selecting committed trajectories, but BetaGate elevation is blocked.

## 3. Autopsy question

Did 592e fail because the readiness predicates failed to fire, or because predicate firing did not control commitment state?

The predicates did fire. The missing element is causal authority over hold/release.

More precisely: 592e shows that score-margin and nav-readiness predicates are measurable and active, and score-margin can suppress beta elevation when the latch is not yet elevated. It does not show that either predicate can release, suppress, or clear an already-held committed state. The next diagnostic must test that state transition directly.

## 4. What failed and what did not

What failed:

- The primary discrimination criteria failed: gates did not reduce the script's committed-state occupancy metric.
- The 592e hold-rate metric conflated upstream rv-low E3 selection with BetaGate commitment maintenance.
- The tested configuration did not demonstrate maintenance/release authority for either readiness predicate.

What did not fail:

- The readiness predicates did not fail to fire. ARM_1 and ARM_3 had thousands of score-margin blocks; ARM_2 and ARM_3 had nav blocks.
- The 592d C1 measurement defect did not recur in the same form. 592e correctly moved away from entry counts as the sole criterion.
- MECH-090 base policy-output gating did not globally fail: beta elevation was fully suppressed in ARM_1 and ARM_3, showing the score-margin admission gate can affect BetaGate elevation when not already elevated.
- The biological R-c interpretation is not directly falsified. The code currently implements admission gating, while the observed failure is about maintenance/release authority.

Why this is more informative than 592d:

- 592d's failure was dominated by an unmeetable transition-edge count predicate. It could not tell whether the gates mattered.
- 592e shows that the gates are firing in the corrected measurement regime, yet committed-state occupancy as measured by the script is not discriminative.
- The per-cell beta-elevation totals sharpen the failure: score-margin gates can suppress beta elevation without clearing E3's rv-low committed-trajectory marker. That localises the problem to the boundary between readiness predicates, BetaGate latch state, and E3 committed-trajectory state.

Dominant diagnosis:

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | partial | `claim_ids=["MECH-090"]` is accurate, but 592e tested admission plus an upstream E3 hold proxy more than true already-held release authority. |
| Biological reference | clear | BG beta gating, action readiness, affordance preparation, and dopaminergic readiness remain the correct reference cluster. |
| Prerequisites | present for entry gating; untested for maintenance | R-c score-margin and nav axes are implemented; release authority is separate and not coupled to readiness failure. |
| Implementation | partial integration | The predicates are wired to elevate/admit; no readiness-failure path releases an already elevated bistable latch. |
| Environment | not load-bearing | A full ecological environment is not needed for the next question. |
| Measurement | misleading | `e3._committed_trajectory` occupancy is upstream of BetaGate admission and can remain 1.0 while beta elevation is 0.0. |
| Integration | admission coupled, maintenance not demonstrated | The state-machine boundary is the unresolved interface. |
| Scale | adequate for diagnosis | The next test should be smaller, not larger. |

Recommended evidence read for 592e: keep as `does_not_support` for MECH-090 R-c state-authority as currently integrated, with an evidence-quality note that this is not a clean conceptual falsification of MECH-090. It is a direct integration failure: predicate activity lacks demonstrated authority over commitment maintenance/release.

## 5. V3-EXQ-592f experiment plan

**Title:** MECH-090 commitment-state transition authority probe

**Purpose:** diagnostic, with direct MECH-090 claim relevance. The test is not a full ecological behavioural experiment; it is a controlled state-machine probe of whether failed readiness can release or suppress an already-held committed state.

**Core harness:** build a minimal `REEAgent` with `beta_gate_bistable=True`, score-margin gate ON, nav-readiness conjunction ON, and a monkeypatched/stubbed `E3TrajectorySelector.select()` that returns controlled `SelectionResult` objects. Use real `REEAgent.select_action()`, real `BetaGate`, and real `CommitReadiness`.

**Forced state:** before perturbation, set:

- `agent.beta_gate.elevate()`
- `agent.e3._committed_trajectory = dummy_trajectory`
- `agent.e3._running_variance = 0.0` or another rv-low value
- `agent._committed_step_idx = 0`
- nav readiness high and score margin high

**Stages:**

| Stage | Forced inputs | Expected if MECH-090 has maintenance authority |
|---|---|---|
| A forced committed baseline | score margin above floor; nav readiness above floor; beta elevated; E3 rv-low | beta_elevated_fraction and committed pointer fraction >= 0.8 before perturbation |
| B score-margin failure while already committed | score margin below 0.05; nav readiness passing | direct score-below-floor count rises; beta elevation or committed pointer occupancy drops, or a decommit transition occurs |
| C nav-competence failure while already committed | nav readiness below 0.3; score margin passing | nav block count rises; beta elevation or committed pointer occupancy drops, or a decommit transition occurs |
| D both gates fail while already committed | score margin below floor and nav readiness below floor | strongest suppression/release; no weaker than the single-gate stages |
| E recovery | restore score margin and nav readiness above floors | beta elevation and/or committed-state occupancy can re-enter; no permanent lockout |

**Inputs forced:**

- `forced_score_margin`: pass e.g. 0.10, fail e.g. 0.00 or 0.01.
- `forced_scores`: two-score tensor whose sorted margin encodes the target margin.
- `forced_nav_readiness`: pass e.g. 1.0, fail e.g. 0.0.
- `forced_result_committed`: true for all stages, so rv-low E3 selection is held constant.
- `initial_beta_elevated`: true for B/C/D to ensure this is a maintenance/release probe, not another admission probe.

**Outputs measured:**

- Direct gate inputs: observed score margin, score-below-floor count, readiness value, readiness-below-floor count.
- Official counters: `mech090_n_elevation_blocked`, `mech090_n_elevation_admitted`, `n_blocks_emitted`.
- State occupancy: `beta_elevated_fraction`, `e3_committed_pointer_fraction`, `result_committed_fraction`, `policy_hold_count`, `policy_propagation_count`.
- Transitions: beta true-to-false release count, false-to-true re-entry count, committed-pointer true-to-false count, step-index reset count.
- Recovery: restored-gate beta/e3 occupancy after perturbation.

**Acceptance criteria:**

- C1 forced baseline: `baseline_beta_elevated_fraction >= 0.8` and `baseline_e3_committed_pointer_fraction >= 0.8`.
- C2 score-margin release authority: `direct_score_margin_below_floor_count > 0` and either `beta_elevated_fraction` decreases by at least 0.5 from baseline, or `e3_committed_pointer_fraction` decreases by at least 0.5 from baseline, or `decommit_transition_count >= 1`.
- C3 nav-competence release authority: `nav_competence_blocks > 0` and either `beta_elevated_fraction` decreases by at least 0.5 from baseline, or `e3_committed_pointer_fraction` decreases by at least 0.5 from baseline, or `decommit_transition_count >= 1`.
- C4 conjunction authority: both direct gate-failure counters are positive, and suppression in Stage D is at least as strong as the strongest single-gate suppression from B/C.
- C5 recovery: after gates are restored, `beta_elevated_fraction` rises to at least 0.8 of baseline and no permanent lockout occurs. If no suppression occurred in B/C/D, recovery is recorded as not evaluable and the overall result cannot PASS.
- C6 no-vacuity: each forced perturbation must actually alter the predicate input. If a forced input does not cross its threshold, the result is INVALID / harness failure, not FAIL.

**Failure routing:**

- Direct inputs fail to cross thresholds: `INVALID`, `claim_ids=[]`, `evidence_direction=non_contributory`, route to `/diagnose-errors` on harness.
- Inputs cross thresholds but official counters do not move: diagnostic FAIL showing the predicate is not consulted in that already-elevated state; route to implementation audit before any behavioural retest.
- Counters move but beta/e3 state does not release or suppress: `does_not_support` or `weakens` MECH-090 R-c state-authority, depending on governance convention; route to implement-substrate design for readiness-to-release coupling or explicit R-b fallback.
- Release occurs but recovery fails: FAIL for lockout; route to release/re-entry calibration.
- PASS: supports MECH-090 state-machine authority and permits, but does not itself execute, the next ecological behavioural validation.

**Claim ids policy:**

- Use `claim_ids=["MECH-090"]` if the harness exercises real `REEAgent.select_action()`, `BetaGate`, and `CommitReadiness` as described.
- Use `claim_ids=[]` only if the implementation falls back to testing standalone instrumentation rather than the actual MECH-090 state-machine path.

**Estimated runtime:** 1-5 minutes locally; queue estimate 10 minutes to leave room for manifest writing and validation.

## 6. Minimal implementation plan

Files already inspected:

- `REE_assembly/evidence/experiments/v3_exq_592e_mech090_readiness_conjunction_validation_20260601T180923Z_v3.json`
- `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-592d_2026-06-01.md`
- `ree-v3/experiments/v3_exq_592e_mech090_readiness_conjunction_validation.py`
- `ree-v3/ree_core/heartbeat/beta_gate.py`
- `ree-v3/ree_core/policy/commit_readiness.py`
- `ree-v3/ree_core/agent.py`
- `ree-v3/ree_core/predictors/e3_selector.py`
- `ree-v3/ree_core/utils/config.py`
- `ree-v3/tests/contracts/test_mech090_readiness_conjunction.py`
- `REE_assembly/docs/claims/claims.yaml`
- `REE_assembly/docs/architecture/mech_090_commit_entry_predicate.md`
- `REE_assembly/evidence/planning/commitment_closure_plan.md`
- `ree-v3/experiment_queue.json`
- `CLAUDE.md`, `REE_assembly/CLAUDE.md`, and `ree-v3/CLAUDE.md`

Files to change in a later `/queue-experiment` pass:

- New script: `ree-v3/experiments/v3_exq_592f_mech090_commitment_state_transition_probe.py`
- Queue append: `ree-v3/experiment_queue.json`

Harness design:

- Construct a minimal `REEAgent` with R-c gates enabled and `beta_gate_bistable=True`.
- Build a two-candidate dummy trajectory set using `Trajectory` from `ree_core.predictors.e2_fast`.
- Monkeypatch `agent.e3.select` to return a controlled `SelectionResult` with forced scores, forced committed=true, and a selected dummy action.
- Run short stage loops through `agent.select_action(candidates, {"e3_tick": True})`.
- Before B/C/D, force beta elevated and an E3 committed pointer so the test starts from an already-held state.
- Record both direct predicate inputs and official counters so "not consulted while elevated" is a first-class diagnostic result.

Manifest fields required:

- `schema_version`, `run_id`, `queue_id`, `experiment_type`, `architecture_epoch`, `timestamp_utc`, `experiment_purpose`, `claim_ids`, `supersedes`.
- `stage_metrics` keyed by A/B/C/D/E.
- `direct_gate_inputs` with observed forced margins/readiness values and threshold-crossing counts.
- `official_gate_counters` from `BetaGate.get_state()` and `CommitReadiness.get_state()`.
- `state_occupancy` with beta elevation, E3 committed pointer, policy hold/propagate, and result.committed fractions.
- `transition_counts` with beta release, beta re-entry, committed-pointer drop, and recovery counts.
- `vacuity_checks` and an `INVALID` outcome path if inputs were not actually changed.
- `acceptance` C1-C6 and `diagnostic_interpretation`.
- `evidence_direction_note` explaining whether the result tests MECH-090 directly or only instrumentation.

Smoke test:

- Run `/opt/local/bin/python3 experiments/v3_exq_592f_mech090_commitment_state_transition_probe.py --dry-run`.
- Verify the dry-run manifest has all stages, forced inputs cross thresholds, and no acceptance criterion can pass on zero perturbation.
- Run `/opt/local/bin/python3 validate_queue.py` after queue append.
- Run the repo experiment validation helper if available in the queue session.

Rollback plan:

- The script should not modify `ree_core`.
- If the harness cannot force or observe state transitions through `REEAgent.select_action()`, do not queue as MECH-090 evidence. Either keep it as `claim_ids=[]` instrumentation or stop and route to `/diagnose-errors` on harness construction.
- If queue validation fails, remove the V3-EXQ-592f queue entry and leave the new script unqueued until fixed.

## 7. Queue proposal

```json
{
  "queue_id": "V3-EXQ-592f",
  "title": "MECH-090 commitment-state transition authority probe",
  "script": "experiments/v3_exq_592f_mech090_commitment_state_transition_probe.py",
  "experiment_type": "v3_exq_592f_mech090_commitment_state_transition_probe",
  "experiment_purpose": "diagnostic",
  "experiment_purpose_note": "Diagnostic, not full ecological behaviour: directly tests MECH-090 state-machine authority over an already-held committed state using controlled forced gate inputs.",
  "claim_ids": ["MECH-090"],
  "supersedes": "V3-EXQ-592e",
  "priority": 35,
  "estimated_minutes": 10,
  "machine_affinity": "any",
  "status": "pending",
  "note": "Do not compare commit-entry counts alone. PASS requires direct suppression/release of already-held beta/e3 commitment state plus recovery after readiness returns. INVALID if forced inputs do not cross thresholds."
}
```

## 8. Recommended governance note

Draft evidence-quality note for MECH-090, to be applied only by `/governance` if accepted:

V3-EXQ-592e (2026-06-01, supersedes V3-EXQ-592d) FAILed after correcting the 592d commit-entry-count defect. C1 baseline hold-rate fired, and both readiness predicates were measurable: ARM_1 score-margin blocks=1793, ARM_3 score-margin blocks=2088, ARM_2/3 nav-competence blocks=150 each. The failure is therefore not predicate silence. The informative result is that predicate firing did not produce discriminative committed-state occupancy under the script's hold-rate measure: all arms had hold_rate=1.0 and total_commits=0. Per-cell beta-elevation totals localise the issue further: score-margin gating can suppress BetaGate elevation when the latch is not elevated (ARM_1/3 beta-elevated fraction 0.0), but E3's rv-low committed-trajectory marker remains present because it is set upstream of BetaGate admission. Current code confirms the R-c predicates are wired to admission/elevation sites; no readiness-failure path releases an already-elevated bistable latch or clears E3 committed state. This is a direct integration/state-authority gap, not a clean conceptual falsification of MECH-090. Route to V3-EXQ-592f, a controlled state-machine probe of whether failed readiness can release/suppress an already-held committed state and recover when readiness returns.

## 9. Final concise verdict

592e showed that MECH-090 predicates fire but lack demonstrated authority over commitment maintenance/release. 592f must directly test whether failed readiness can release or suppress an already-held committed state, and whether commitment can recover when readiness returns.
