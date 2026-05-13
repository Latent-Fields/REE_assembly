# Morning Agenda -- 2026-05-13

Generated: 2026-05-13T04:21:11Z

---

## Queue Status

- Total pending: **0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- **ALERT: Queue EMPTY -- runner has nothing to claim.**
- Last queued item (V3-EXQ-540e) FAILed 2026-05-12 18:15Z. No supersession entry was appended; the MECH-307 default-recalibration line is currently paused on a result.

---

## Experiments Awaiting Review (7 indexed / 5 runner-only)

### V3-EXQ-540c -- mech307_readsite_probe -- **PASS** (diagnostic)
- **Claims tested:** MECH-295 (candidate, exp_conf=0.000, hold_pending_v3_substrate), MECH-307 (candidate_substrate_landed, exp_conf=0.471)
- **Purpose:** structural read-site introspection. evidence_direction=mixed by routing (diagnostic, claim-side direction set non_contributory).
- **Governance impact if confirmed:** confirms the MECH-307 substrate populates read sites cleanly (predicate cleared on 94.66% of candidates at half-tier thresholds) but the drive_level gate (legacy 0.1 floor) and z_beta_arousal gate (legacy 0.6 floor) sat above the achievable ceiling -- the V3-EXQ-540a/540b conj_fire_rate=0 was a default-value calibration problem, not a substrate failure.
- **Why it matters:** 540c is the diagnostic that motivated the 2026-05-12 default-value recalibration committed in `ree-v3` 4f5d9ca. The recalibration is being re-validated by 540e (below).

### V3-EXQ-540e -- mech307_default_fix_validation -- **FAIL** (diagnostic, supersedes V3-EXQ-540d)
- **Claims tested:** MECH-093, MECH-205, MECH-216, MECH-295, MECH-307, SD-014 (all candidates; MECH-307 status candidate_substrate_landed)
- **Purpose:** behavioural revalidation of the 540a 3-arm decomposition under the new mech295_min_drive_to_fire=0.01 / mech307_conjunction_z_beta_threshold=0.3 defaults. evidence_direction=mixed (per-claim routing).
- **Governance impact if confirmed:** the recalibration was supposed to clear the floor (dry-run 540e showed ARM_2_full conj_fire_rate=0.155). Full-run FAIL means the floor is cleared at dry-run scale but C1 substrate dissociation and/or C2 conjunction-fires-only-in-ARM_2 did not hold at full scale. **This is the loudest review item -- goal_pipeline:GAP-1 closure plan claims this clears, but 540e disagrees. Needs interpretation before the next supersession is queued.**

### V3-EXQ-540a -- mech307_optionb_3arm_conjunction_decomposition -- FAIL (diagnostic, supersedes V3-EXQ-540)
- **Claims tested:** same as 540e
- **Outcome:** mixed direction. Predecessor of the entire MECH-307 default-recalibration arc. 540c was the read-site probe that diagnosed it.

### V3-EXQ-540b -- mech307_conjunction_threshold_sweep -- FAIL (diagnostic, supersedes V3-EXQ-540a)
- **Claims tested:** MECH-295, MECH-307
- **Outcome:** threshold sweep -- ARM_default (0.6/0.3/0.6) vs ARM_half (0.3/0.15/0.3) vs ARM_low (0.1/0.05/0.1) vs ARM_floor (0.01/0.005/0.01). conj_fire_rate=0 at every tier -- confirmed by 540c the drive_level gate was the structural blocker, NOT the predicate thresholds.

### V3-EXQ-549 -- arc066_tonic_vigor_discriminative_pair -- FAIL
- **Claims tested:** ARC-066 (candidate, exp_conf=0.322, pending_user hold), MECH-320 (candidate_substrate_landed, exp_conf=0.322, pending_user hold)
- **Purpose:** first behavioural test of MECH-320 tonic-vigor substrate (substrate-landed 2026-05-10). evidence_direction=weakens for both claims (per-claim routing).
- **Result signal:** action_density is 1.0 in both ARM_OFF and ARM_ON (every tick is non-noop already), so the pearson_r vigor-action-density correlation can't separate the arms. Likely a methodology gap (env has no noop attractor) rather than a substrate failure.
- **Governance impact if confirmed weakens:** ARC-066 / MECH-320 stay at exp_conf 0.322 with one weakens entry. The substrate-landed status survives; the discriminative-pair design needs a noop-attractor env.

### V3-EXQ-550 -- zgoal_monostrategy_falsifier -- FAIL
- **Claims tested:** MECH-269 (candidate, exp_conf=0.000, v3_pending)
- **Purpose:** diagnostic falsifier of "MECH-269 V_s monostrategy hold on SD-029 is substrate-level vs config-default." evidence_direction=supports (the FAIL branch SUPPORTS substrate-level reading at no-training depth).
- **Governance impact if confirmed supports:** strengthens MECH-269's substrate-level reading. Per-session note already recorded in self_attribution_plan.md decision log 2026-05-11. **Already reviewed in the 2026-05-11 EXQ-550 / EXQ-543c session (see TASK_CLAIMS); flagging here because pending_review.md still lists it.**

### V3-EXQ-543d -- arc062_mech260_factorial_falsifier -- FAIL (supersedes V3-EXQ-543c)
- **Claims tested:** ARC-062 (candidate, exp_conf=0.322), MECH-309 (candidate, exp_conf=0.000)
- **Purpose:** 2x2 factorial (use_gated_policy x use_dacc) on bipartite SD-054. evidence_direction=non_contributory.
- **Governance impact:** non_contributory means no claim-side direction is applied. The 2026-05-11 EXQ-543c review session already routed the inert-gating finding to arc_062_rule_apprehension_plan.md GAP-B. 543d strict-replicates that -- per-claim direction map kept non_contributory.

### Runner-only / index-stale (5)
- **V3-EXQ-552** FAIL (forced-exploration-warmup; pipeline-entropy companion to 551a)
- **V3-EXQ-555** PASS (seed-7 env-vs-agent factorisation diagnostic)
- **V3-EXQ-557** PASS (agent-seed sweep, monostrategy basin in agent-init space)
- **V3-EXQ-558** PASS (clean seed-pair readout/rank diagnostic seed 7 vs seed 42)
- **V3-EXQ-540c** ERROR row -- IGNORE: the systemctl-killed full-scale run already has a clean PASS manifest indexed under v3_exq_540c_mech307_readsite_probe/. Index is stale on this row only; re-running `build_experiment_indexes.py` should clear it.

---

## Errors to Diagnose (4 of 8 ERROR rows, after filtering scrubbed manifests)

After cross-referencing against pending and completed queue_ids, eight ERROR rows have no letter-successor. Of these:

- **V3-EXQ-008** (2026-03-17) -- archaeology; not blocking. Skip unless governance-pipeline cleanup pass.
- **V3-ONBOARD-smoke-EWIN-PC** (2026-04-05) -- onboarding smoke, no scientific bearing. Skip.
- **V3-EXQ-455a** (2026-04-23) -- needs `/diagnose-errors`. Claim ownership unclear from row alone; check the script header.
- **V3-EXQ-495** (2026-04-28) -- MECH-163 V3 full-completion gate; needs `/diagnose-errors`.
- **V3-EXQ-244a** (2026-05-06) -- needs `/diagnose-errors`.
- **V3-EXQ-538** (2026-05-08) -- needs `/diagnose-errors`; sibling of the 5-EXQ manifest-leak cohort (see CLAUDE.md "Manifest-leak in conflict-recovery (fixed 2026-05-09)" -- the fix landed AFTER 538 ERRORed, so re-running it may now succeed without code changes).
- **V3-EXQ-542** (2026-05-09) -- ARC-062 Phase 1 substrate-readiness. **Script-level PASS (5/5 sub-tests) confirmed in CLAUDE.md and 2026-05-09 commit -- runner ERROR is the manifest-scrub issue noted in CLAUDE.md ("manifests scrubbed; runner will write the canonical PASS manifest from the queued entry"). Likely identical resolution path to V3-EXQ-544.**
- **V3-EXQ-544** (2026-05-10) -- MECH-313 noise-floor substrate-readiness. Same situation as 542 -- script-level PASS, runner-ERROR is the scrubbed-manifest issue. **The MECH-313 manifest scrub issue may be the same root cause as V3-EXQ-538's manifest-leak -- worth one focused diagnose-errors session covering 538 / 542 / 544 together.**

---

## Governance Agenda (11 recommendations pending_user)

All are `hold_pending_v3_substrate` for new claims registered 2026-05-09 .. 2026-05-12. No promote/demote actions blocked on user input today; the queue is just acknowledging the v3_pending flag on the new ARC-065 / ARC-066 cluster.

| claim_id | current_status | recommendation |
|---|---|---|
| ARC-066 | candidate | hold_pending_v3_substrate |
| ARC-067 | candidate | hold_pending_v3_substrate |
| ARC-068 | candidate | hold_pending_v3_substrate |
| ARC-070 | candidate | hold_pending_v3_substrate |
| ARC-071 | candidate | hold_pending_v3_substrate |
| MECH-320 | candidate_substrate_landed | hold_pending_v3_substrate |
| Q-043 | open | hold_pending_v3_substrate |
| Q-044 | open | hold_pending_v3_substrate |
| Q-045 | open | hold_pending_v3_substrate |

(Plus rolling pending_user fills on the same ARC-065 cluster as new substrates land.)

---

## Active Plans Heartbeat (6 plans)

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| arc_062_rule_apprehension_plan | 2 | 1 | 0 | 0 | 2026-05-11 |
| commitment_closure_plan | 3 | 2 | 0 | 0 | 2026-05-12 |
| goal_pipeline_plan | 2 | 2 | 0 | 0 | 2026-05-11 |
| sd033_governance_plan | 0 | 0 | 0 | 0 | N/A (all done) |
| self_attribution_plan | 1 | 3 | 0 | 0 | 2026-05-11 |
| sleep_substrate_plan | 4 | 1 | 0 | 0 | 2026-05-10 |

All plans are fresh: no stale rows, every active plan has a decision-log entry within the past 4 days. No PLAN STALING flags fire.

**Cross-plan dependency to watch:** commitment_closure:GAP-1 (SD-033a bias-head training) is blocked on arc_062 GAP-A (done) + GAP-B (blocked on CEM-candidate-distinguishability substrate-readiness diagnostic; owner_exq=TBD). GAP-B is the next substrate-readiness EXQ to queue if the bipartite SD-054 layout extension (landed 2026-05-11) is to be exercised behaviourally.

---

## Literature Pull Candidates (Top 2)

| # | Claim | Subject | Priority | Existing entries |
|---|---|---|---|---|
| 1 | MECH-320 | tonic_vigor_coupling_score_bias | medium | 0 |
| 2 | Q-019 | Three-Gate BG Architecture lit extraction | medium | 1 |

evidence_backlog.v1.json surfaced only 2 medium-priority literature items. Most other cluster lit-pulls already exist under `evidence/literature/targeted_review_*`.

---

## Serve.py Status

- **RUNNING** on port 8000 (Python pid 38826).

---

## Blocked Items

- No `TASK_CLAIMS` collision blocked governance.sh -- pipeline ran clean.
- V3-EXQ-540c runner-only ERROR row is a known index-stale duplicate (canonical PASS manifest exists in v3_exq_540c_mech307_readsite_probe/); a follow-up `build_experiment_indexes.py` run should clear it.
- **Suggested next moves:**
  1. Review and decide on V3-EXQ-540e (the MECH-307 default-recalibration FAIL is the most consequential pending item).
  2. Queue the arc_062 GAP-B CEM-candidate-distinguishability substrate-readiness diagnostic on the bipartite SD-054 substrate (closes the dependency to commitment_closure:GAP-1).
  3. One `/diagnose-errors` session covering V3-EXQ-538 / 542 / 544 (likely shared manifest-scrub / manifest-leak root cause now that the 2026-05-09 conflict-recovery fix is in place).
  4. Refill the queue -- runner has been idle since 18:15Z 2026-05-12 with no claimable items.
