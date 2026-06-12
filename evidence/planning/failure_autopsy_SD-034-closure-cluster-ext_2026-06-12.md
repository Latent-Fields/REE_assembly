# Failure Autopsy -- SD-034 closure-cluster COHORT EXTENSION (461c / 464c / 466c / 467c / 629b)

- generated_utc: 2026-06-12T23:16:13Z
- scope: cluster extension (5 FAILs)
- status: confirmed (2026-06-12T23:16Z; user AskUserQuestion adjudication -- separate mode-governance substrate gap for 464c/467c; readiness-requeue for 629b; new sibling file).
- parent: `failure_autopsy_SD-034-closure-cluster_2026-06-12.{md,json}` (confirmed; 460c + 468c reclassified non_contributory + substrate_ceiling + pending_retest by the 2026-06-12 PM governance cycle). That file named these five siblings to "fold into this cluster as they arrive." They have arrived; this file is the extension.
- targets (all on the 603n `scaffolded_sd054_onboarding` foraging-competent substrate; all passed the foraging_contact_guard EXCEPT 629b):
  - V3-EXQ-461c -- run `v3_exq_461c_mech090_sd033a_delayed_reward_persistence_behavioural_20260612T213304Z_v3` -- claim_ids [MECH-090, SD-033a, SD-034]
  - V3-EXQ-464c -- run `v3_exq_464c_mech266_competing_goals_behavioural_20260612T115222Z_v3` -- claim_ids [MECH-266, SD-032a]
  - V3-EXQ-466c -- run `v3_exq_466c_sd034_satisficing_residue_discharge_behavioural_20260612T131423Z_v3` -- claim_ids [SD-034, MECH-094]
  - V3-EXQ-467c -- run `v3_exq_467c_mech266_mode_stickiness_behavioural_20260612T155846Z_v3` -- claim_ids [MECH-266, SD-032a]
  - V3-EXQ-629b -- run `v3_exq_629b_mech342_ecological_maintenance_release_evidence_20260612T155004Z_v3` -- claim_ids [MECH-342]

---

## 0. Headline -- the cohort is NOT one cluster; it splits three ways

The parent cluster_pattern is: *the SD-034 closure control-plane is wired and its proximal events partially fire/are reachable, but on the 603n foraging-competent agent it has no behavioural authority over the MECH-090 latch.* Two of the five siblings (461c, 466c) reproduce that pattern exactly. The other three do **not** belong to the closure control-plane; they expose two **distinct** substrate gaps. All five are nonetheless the **same epistemic verdict**: `non_contributory` + `substrate_ceiling` + `pending_retest_after_substrate`, **NOT a weakens / NOT a falsification.** None of the five tested its claims under conditions where they could express.

| Sub-cluster | Runs | One-line shape | Substrate route |
|---|---|---|---|
| **A. Closure control-plane** | 461c, 466c | closure done-token / closure-coupled resolution never fires despite env completions + beta elevated -- parent's exact pattern | substrate_queue `commitment-closure-control-plane` (parent's entry) |
| **B. Mode-governance never engages** | 464c, 467c | MECH-266 exit-rails have no authority because external_task mode is never occupied; the n_switches non-vacuity gate passed *vacuously* (it counts episode-boundary settles, not genuine mode competition) | **separate** substrate gap (genuine external_task mode-competition + occupancy-keyed non-vacuity gate) |
| **C. Readiness requeue** | 629b | contact-guard fail (1/3 seeds forage-competent); on the one competent seed MECH-342 *did* show release authority | `scaffolded_sd054_onboarding` nav/survival-competence ceiling (Stage-H) -- **not** the closure plane |

This is convergent iterative substrate engineering across three distinct mechanism axes, NOT granularity debt on any one claim. No `/claim-synthesis`.

---

## 1. Sub-cluster A -- closure control-plane (461c, 466c)

### 461c facts (MECH-090 latch + SD-033a rule persistence + SD-034 closure)

Pre-registered criteria (script `=== INTERPRETATION GRID ===`): C1 `ARM_HOLD_ON n_delay_windows >= 1 AND mean_persistence_ratio >= 0.5`; C2 `ARM_HOLD_ON n_closure_coupled_resolutions >= 1` (SD-034 couples to resolution); C3 hold extends window vs no-hold.

| Criterion | load-bearing | passed | reading |
|---|---|---|---|
| precondition `foraging_contact_guard` | gate | **met** (1.0) | substrate engaged |
| precondition `committed_windows_engaged` (n_windows>0) | gate | **met** (0.667 == floor) | committed Hold windows DID form -- the exact n_windows=0 gap the *b cohort scored is closed |
| C1 delay-windows + persistence >= 0.5 | yes | **FAIL** | persistence is measured at closure-coupled resolution ticks; with C2=0 there is nothing to measure |
| C2 `n_closure_coupled_resolutions >= 1` | yes | **FAIL** | the SD-034 closure coupling never fires (= parent 460c `n_closures=0`) |
| C3 hold extends window vs no-hold | yes | **FAIL** | downstream of the unfired closure |

Failed criterion type: **discrimination** (C2 is the SD-034 signature). The 461c precondition advanced beyond 460c (it verified Hold windows formed), but it still verified the **wrong** thing for the load-bearing claim: it checked window-formation, not **closure-coupled-resolution-trigger-availability**. Same V3-EXQ-642 wrong-precondition lesson as the parent.

### 466c facts (SD-034 closure + MECH-094 residue discharge)

Criteria: C1 `n_closures >= 1` (ON); C2 `discharge_events >= 1`; C3 OFF arm no closure/no discharge.

| Criterion | load-bearing | per-seed (ON) | passed |
|---|---|---|---|
| precondition `commitment_and_completion_engaged` | gate | beta_elevated 268/376/128, n_sequence_completions 11/6/5 | **met** (1.0) |
| C1 `n_closures >= 1` | yes | **0 / 0 / 0** | **FAIL** |
| C2 `discharge_events >= 1` | yes | 0 / 0 / 0 | **FAIL** (downstream of closure) |
| C3 OFF no-closure no-discharge | yes | -- | PASS |

466c is a **near-exact clone of parent 460c**: the ClosureOperator done-token never fires on any seed despite real env `sequence_completions` and beta elevated. The completion non-vacuity gate verified env-completion-availability, not closure-trigger-availability (parent Section 4 root cause, code-confirmed in `ree-v3/ree_core/governance/closure_operator.py`: the done-token fires only via the automatic rule_state-stability conjunction -- unmet on the untrained/zeroed `rule_bias_head` + SP-CEM perturbation -- or via the env->`emit_closure()` hook, which the `*c` experiments do not wire).

### A read

Both express the parent's structural property: **closure done-token / coupled-resolution is decoupled from the agent's real task completions.** SD-034 (provisional / v3_pending=false), MECH-090 (active), SD-033a (rule persistence), MECH-094 (residue discharge) -- none could express because the trigger was unreachable. `non_contributory` + `substrate_ceiling` + `pending_retest_after_substrate`. NO demotion of SD-034; NO weaken of MECH-090/SD-033a; MECH-094 not exercised. Routes to the parent's `commitment-closure-control-plane` substrate_queue entry (route env `sequence_complete` -> `emit_closure` + de-commitment hold + train `rule_bias_head`).

---

## 2. Sub-cluster B -- mode-governance never engages (464c, 467c)

### 464c facts (MECH-266 asymmetric exit-rail + SD-032a SalienceCoordinator)

Criteria: C1 `ARM_ASYM fraction_in_external_task >= ARM_SYM fraction + 0.1`; C2 `ARM_ASYM n_switches <= ARM_SYM`; C3 `ARM_SYM n_switches >= 1`.

Per-seed (all 3, both arms): **`fraction_in_external_task = 0.0`**; `mode_step_counts = {external_task: 0, internal_planning: ~2020, internal_replay: 0, offline_consolidation: 0}`; `n_switches = 15`, `n_episodes = 15`.

| Criterion | passed | reading |
|---|---|---|
| precondition `mode_switching_engaged` (sym n_switches>=1) | **met** (1.0) | **VACUOUS** -- see below |
| C1 asym task-occupancy > sym + 0.1 | **FAIL** | external_task occupancy is structurally 0 in BOTH arms; the criterion can never discriminate |
| C2 asym switches <= sym | PASS | both = 15 (degenerate tie) |
| C3 sym n_switches >= 1 | PASS | the vacuous gate |

**Code-grounded vacuity (script `_eval_competing_goals`, e3-loop `total_switches += 1` on `cur_mode != prev_mode`):** `prev_mode` is seeded to `coord.current_mode` at each episode start; the agent settles into `internal_planning` on tick 1 and stays there the whole episode. So `total_switches` counts **one episode-initial settle per episode** -> `n_switches == n_episodes == 15`. This is **not** genuine mode competition. The mode-switching non-vacuity gate (`sym n_switches >= 1`) was meant to certify "mode governance engaged" but it certified an episode-boundary artifact. **The MECH-266 asymmetric exit-rail acts on the transition *out of external_task*; the agent never *enters* external_task, so the rail has no mode to bind, and C1 (task-occupancy contrast) is pinned at 0-vs-0 by construction.**

### 467c facts (MECH-266 uniform exit-rail dose-response)

Criteria: C1 `mean_dwell monotone non-increasing in r`; C2 `low-r dwell >= 2.0 * high-r dwell`; C3 high-r `n_switches >= 1`.

Per-seed `condition_results`: `mean_dwell` non-monotone across r (e.g. seed 42: 59.8 / 67.9 / 76.0 / 92.3 / 67.75); **`n_switches = 12` for every ratio, `n_episodes = 12`.** `mean_dwell ~= total_steps / n_runs` (e.g. 1423/24 = 59.3 ~ 59.8) -- an **episode-length artifact**, not a genuine in-mode dwell. The hysteresis ratio cannot move dwell because there are no genuine mode switches to lengthen/shorten (`n_switches == n_episodes` again).

### B read

464c and 467c are **one structural property, not two bugs**: *on the 603n foraging substrate the SalienceCoordinator + MECH-266 rails never receive the varying salience signals that drive genuine mode competition, so external_task mode is never occupied and the MECH-266 dose-response / over-binding contrast cannot express.* The non-vacuity gates (keyed on `n_switches`) certified episode-boundary settles as "mode governance engaged" -- the V3-EXQ-642 wrong-precondition pattern again, at the mode-occupancy layer instead of the closure-trigger layer. `non_contributory` + `substrate_ceiling` + `pending_retest_after_substrate`. NO weaken of MECH-266 (candidate) or SD-032a. This is a **distinct substrate gap** from the closure plane (user-adjudicated 2026-06-12): the substrate must drive genuine external_task occupancy on the foraging agent **and** the retest's non-vacuity gate must key on contested-mode-occupancy reachable (e.g. `min(fraction_in_external_task) > floor` across arms), **not** `n_switches`.

---

## 3. Sub-cluster C -- readiness requeue (629b)

### 629b facts (MECH-342 maintenance-release)

Self-routed `evidence_direction: non_contributory`, `interpretation.readiness_route: substrate_not_ready_requeue`, `acceptance.route_reason: contact_guard_unmet`.

| Gate | measured | threshold | met |
|---|---|---|---|
| `foraging_contact_guard` | 0.333 (seed 43 only; 42/44 fail z_goal-at-contact-peak 0.0 / 0.371 < 0.4) | 0.667 | **NO** |
| C1 baseline_commits | 0.0 | 1.0 | NO (precondition) |
| C2 degradation_occurred | 0.0 | 1.0 | NO (precondition) |
| C3/C4/C5 (release authority / no-false-abort / distinct-from) | -- | -- | `criteria_non_degenerate` **all false** |

**On the one guard-passing seed (43), the mechanism worked:** `ARM_1_RELEASE_ON` degraded window -- `decommit_beta_releases = 19`, `decommit_pointer_drops = 15`, `decommit_transitions = 34`, `mech342_fires = 1`, `beta_elevated_occupancy = 0.217` -- vs `ARM_0_RELEASE_OFF` holding `beta_elevated_occupancy = 1.0`, `decommit_transitions = 0`. So MECH-342 maintenance-release **did** exert release authority under sustained degraded readiness on the competent seed. The run fails only because 2/3 seeds never forage-competently (contact-guard), so the across-seed acceptance self-routes requeue. The `score_margin_floor` recalibration (0.001) from `failure_autopsy_V3-EXQ-629_2026-06-03` is already applied in the pre-registered thresholds; the failure here is strictly **upstream** of it (foraging competence, not score-margin calibration).

### C read

629b is a **readiness requeue, not a closure-cluster member** (user-adjudicated). It routes to the `scaffolded_sd054_onboarding` nav/survival-competence ceiling (Stage-H leg, goal_pipeline:GAP-2) -- the same foraging-competence gate that SD-058/MECH-357 + SD-059/MECH-358 target -- **not** the commitment-closure-control-plane entry. `non_contributory` + `pending_retest_after_substrate`. Carry a **`narrow_supports_flag`**: the seed-43 positive MECH-342 signal is real but single-seed / single-pathway and must not be cited as behavioural support until the contact guard clears on >= 2/3 seeds. MECH-342 stays candidate / v3_pending.

---

## 4. Four-layer diagnosis (whole cohort)

| Layer | A (461c/466c) | B (464c/467c) | C (629b) |
|---|---|---|---|
| Claim alignment | intact -- closure/persistence/discharge not let to express | intact -- MECH-266 dose-response/over-binding not let to express | intact -- MECH-342 not fairly across-seed; positive on competent seed |
| Biological reference | clear (OFC completion cells; missing completion->closure coupling) | clear (task-set switch governance; mode never contested) | clear (BG de-commitment under degraded readiness; works when foraging) |
| Dependency prerequisites | missing (env `sequence_complete` -> `emit_closure` unwired; untrained rule_bias_head) | missing (no salience drive of genuine external_task occupancy) | missing (foraging competence on 2/3 seeds) |
| Implementation completeness | partial (symbol-without-functional-role: closure wired, trigger decoupled) | partial (rails wired, contested mode never entered) | complete (mechanism fired on the competent seed) |
| Environment adequacy | adequate (completions emitted) | **inadequate for the test** (no external_task pressure on this substrate) | adequate-but-agent-incompetent |
| Measurement adequacy | misleading (precondition checked window-formation not closure-trigger) | misleading (n_switches gate counts episode settles -- VACUOUS) | adequate (self-routed correctly) |
| Integration adequacy | isolated (done-token does not reach latch occupancy) | isolated (coordinator does not reach mode occupancy) | n/a -- never reached commitment on 2/3 seeds |
| Scale / capacity | adequate | adequate | foraging-competence ceiling |

Recommended `epistemic_category` for all five: **substrate_ceiling** (the substrate has the wiring the claims assert but does not carry the information at the granularity/engagement the claims assert). 629b is the contact-guard variant (substrate_not_ready_requeue), still substrate_ceiling-class.

---

## 5. Learning extracted

- **The non-vacuity gate keeps checking the wrong precondition (recurring V3-EXQ-642 pattern, now at three layers).** Parent: env-completion-availability vs closure-trigger-availability. 461c: window-formation vs closure-coupled-resolution-availability. 464c/467c: `n_switches>=1` (episode settles) vs genuine-external_task-occupancy. Every readiness gate in this lineage must verify the *load-bearing claim's actual trigger is reachable*, not a proxy that co-occurs.
- **`n_switches == n_episodes` is the mode-governance vacuity tell.** When the switch counter equals the episode count and `fraction_in_external_task == 0.0`, the coordinator never entered the contested mode; the dose-response/over-binding criteria are pinned by construction. A future MECH-266 retest must gate on `min_across_arms(fraction_in_external_task) > floor`.
- **A FAIL that fires the mechanism on the competent seed is positive-leaning evidence for the dependency, not against the claim.** 629b seed-43 (decommit_transitions=34, mech342_fires=1, occupancy 1.0->0.217) shows MECH-342 has authority once foraging clears -- a `narrow_supports` signal that strengthens the "readiness-driven release" reading and points the fix at nav-competence, not at MECH-342.
- **The cohort is convergent iterative substrate engineering across three axes, not granularity debt.** Each sub-cluster is a different, code-identified missing coupling; no single claim is circled with N different signatures. No `/claim-synthesis`.

---

## 6. Routing (per run; governance applies -- this skill does not write claims.yaml/manifests/review_tracker/substrate_queue)

| Run | evidence_direction | epistemic_category | pending_retest_after_substrate | narrow_supports_flag | substrate action |
|---|---|---|---|---|---|
| 461c | non_contributory | substrate_ceiling | true | false | amend `commitment-closure-control-plane` (append failure record) |
| 466c | non_contributory | substrate_ceiling | true | false | amend `commitment-closure-control-plane` (append failure record) |
| 464c | non_contributory | substrate_ceiling | true | false | **create** `mode-governance-engagement` substrate gap (drive genuine external_task occupancy + occupancy-keyed non-vacuity gate) |
| 467c | non_contributory | substrate_ceiling | true | false | amend the new `mode-governance-engagement` entry (append failure record) |
| 629b | non_contributory | substrate_ceiling (substrate_not_ready_requeue) | true | **true** (seed-43 MECH-342 authority) | amend `scaffolded_sd054_onboarding` nav-competence ceiling (append failure record); NOT the closure plane |

- Mark all five runs reviewed in `review_tracker.json`.
- NO demotion of SD-034 (provisional holds), MECH-090, SD-033a. NO weaken of MECH-266 / SD-032a / MECH-342 / MECH-094 (all stay candidate / v3_pending). NO `/claim-synthesis`.
- Successor experiments (`*d`) are deferred to `/queue-experiment` AFTER the respective substrate amends land, each with a readiness gate on the *actual* trigger (closure-coupled-resolution reachable for A; external_task occupancy reachable for B; contact-guard >= 2/3 for C) and a non-cap-pinned DV.

### Draft evidence_quality_note per run (governance writes; do not write here)

- **461c** (MECH-090 / SD-033a / SD-034): non_contributory, substrate_ceiling, pending_retest_after_substrate. Cohort extension of the SD-034 closure cluster. Committed Hold windows formed (n_windows>0, the *b-cohort gap closed) but n_closure_coupled_resolutions=0 on the foraging agent, so SD-033a rule-persistence (measured only at closure resolutions) and the SD-034 coupling could not express. Same env->emit_closure-unwired / untrained-rule_bias_head root cause as 460c. Not a falsification.
- **466c** (SD-034 / MECH-094): non_contributory, substrate_ceiling, pending_retest_after_substrate. Near-clone of 460c -- n_closures=0 on 3/3 seeds despite n_sequence_completions=11/6/5 and beta elevated; the residue-discharge (MECH-094) is strictly downstream of an unfired closure. Not a falsification.
- **464c** (MECH-266 / SD-032a): non_contributory, substrate_ceiling, pending_retest_after_substrate. fraction_in_external_task=0.0 both arms all seeds; the mode-switching non-vacuity gate passed vacuously (n_switches=15==n_episodes counts the per-episode settle into internal_planning, not genuine competition). The asymmetric exit-rail has no mode to bind. Distinct mode-governance substrate gap, not the closure plane. Not a falsification.
- **467c** (MECH-266 / SD-032a): non_contributory, substrate_ceiling, pending_retest_after_substrate. mean_dwell is an episode-length artifact (total_steps/n_runs) and n_switches=12==n_episodes -- genuine mode competition never occurred, so the hysteresis dose-response cannot express. Same mode-governance gap as 464c. Not a falsification.
- **629b** (MECH-342): non_contributory, substrate_not_ready_requeue, pending_retest_after_substrate, narrow_supports_flag. Contact guard failed (1/3 seeds forage-competent); on the one competent seed (43) MECH-342 maintenance-release fired (decommit_transitions=34, mech342_fires=1, beta occupancy 1.0->0.217 in the degraded window vs OFF 1.0) -- a narrow single-seed positive that points the fix at the scaffolded_sd054_onboarding nav-competence ceiling, NOT the closure plane. Not a falsification.
