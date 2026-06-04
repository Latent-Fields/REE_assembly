# Failure Autopsy (cluster) -- V3-EXQ-460b / 461b / 464b / 466b

- **Generated (UTC):** 2026-06-04T05:54:00Z
- **Scope:** cluster (4 FAILs)
- **Status:** confirmed (interactive gate answered)
- **Routing (confirmed):** implement-substrate -> AMEND existing `scaffolded_sd054_onboarding`
- **Recommended epistemic_category:** `substrate_ceiling`
- **Recommended evidence reclassification:** `weakens` -> `non_contributory` + `pending_retest_after_substrate` for all tagged claims

---

## 1. Scope

Four pending FAILs, all "behavioural successor" experiments (the `b` suffix) to
substrate-readiness diagnostics that hand-poked the mechanism APIs directly:

| Run | queue_id | Claims | Predecessor (hand-poke) diagnostic |
|---|---|---|---|
| `v3_exq_460b_sd034_verified_but_not_released_behavioural_20260603T231621Z_v3` | V3-EXQ-460b | SD-034, MECH-260, MECH-261 | V3-EXQ-460 (poked emit_closure UC1-UC6) |
| `v3_exq_461b_mech090_sd033a_delayed_reward_persistence_behavioural_20260604T001229Z_v3` | V3-EXQ-461b | MECH-090, SD-033a, SD-034 | V3-EXQ-461 -- **PASS** (diagnostic) |
| `v3_exq_464b_mech266_competing_goals_behavioural_20260604T012553Z_v3` | V3-EXQ-464b | MECH-266, SD-032a | V3-EXQ-464 (poked per-mode Schmitt rails) |
| `v3_exq_466b_sd034_satisficing_residue_discharge_behavioural_20260604T035511Z_v3` | V3-EXQ-466b | SD-034, MECH-094 | V3-EXQ-466 (poked discharge_domain UC1-UC5) |

All run the real `committed_mode_curriculum` (P0 warmup -> P1 consolidation ->
P2 eval) on `CausalGridWorldV2` with the GAP-3 tolerance-band completion
primitive. 3 seeds each, `n_seeds_pass = 0`.

## 2. Facts -- the shared fingerprint: closure never fires in the live loop

| Exp | Positive arm needed | Observed | Failed criterion |
|---|---|---|---|
| 460b | `n_closures>=1`, beta_release>=1, nogo_install>=1 | `n_closures=0` in **every** arm; `total_beta_elevated == total_committed_steps` (beta latched 100% of committed steps, never releases) | discrimination C1/C2/C3 |
| 461b | Hold window -> delayed resolution -> closure <=2 ticks | `n_windows=0` everywhere -- beta never releases, so no resolution event ever forms | discrimination C1/C2 |
| 466b | `n_closures>=1`, `discharge_events>=1` | `n_closures=0`, `discharge_events=0`, `mean_residue_weight_reduction=0`; C3 (closure-OFF==0) passes **trivially** | discrimination C1/C2 |
| 464b | sticky-rail occupancy asymmetry vs a switching baseline | 100% `external_task` occupancy, **0 switches**, 0 steps in internal_planning/replay/consolidation; C3 baseline-non-vacuous guard fires (symmetric baseline has 0 switches) | discrimination C1 + C3 vacuous |

**Substrate-ceiling tells.** 466b-C3 and 464b-C2 pass *trivially* (closure-OFF
trivially has zero closures; sticky-arm trivially has <= symmetric switches when
both are zero) while every *discrimination* criterion fails. Negative-control
passes, discrimination fails -- the canonical substrate-ceiling fingerprint.

**The commitment machinery itself works.** `p1_commitment_emerged=true` on
multiple seeds (460b seed43/44, 461b seed43, 464b all seeds, 466b seed43); the
MECH-090 beta latch engages and stays elevated. What is absent is the
**completion event**: the committed agent never tolerance-completes a waypoint,
so the SD-034 ClosureOperator has no rule-completion "done" token to emit.
Everything downstream of closure -- beta release (MECH-090), targeted No-Go
install (MECH-260), residue discharge (MECH-094), delayed-resolution coupling
(SD-033a), and mode arbitration around task completion (MECH-266/SD-032a) --
therefore cannot express.

**Load-bearing contrast:** V3-EXQ-461 (the hand-poke diagnostic) **PASSED**;
its behavioural twin 461b FAILED. The mechanism's API is correct when poked
directly; the live loop simply never produces the triggering condition. This is
implementation-complete + environment-inadequate, not a claim falsification.

## 3. Claim-layer map

| Claim | type / status | Did the test let it express? |
|---|---|---|
| SD-034 | design_decision / provisional | No -- closure operator never received a completed-rule token (substrate is `implemented`; predecessor hand-poke passes) |
| MECH-090 | mechanism_hypothesis / active | No -- latch engaged but no resolution/release window ever formed |
| MECH-094 | mechanism_hypothesis / stable | No -- no closure -> no residue discharge |
| MECH-260 | mechanism_hypothesis / candidate (v3_pending) | No -- No-Go install is gated on a closure event that never fired |
| MECH-261 | mechanism_hypothesis / stable | No -- depends on the same closure/consolidation chain |
| MECH-266 | mechanism_hypothesis / provisional | No -- asymmetry unmeasurable against a degenerate no-switch baseline |
| SD-032a | design_decision / stable | No -- salience coordinator never left external_task (no internal modes entered) |
| SD-033a | design_decision / candidate (v3_pending) | No -- rule-state persistence unmeasurable with no Hold-resolution window |

In every case the experiment did **not** test the claim under conditions where it
could have expressed itself. The manifest `evidence_direction: weakens` is the
wrong layer -- this is an environment/test-bed gap, not pressure on the claims.

## 4. Biological-reference triage

The closest reference is the basal-ganglia "completion / done" signal and the
beta-band drop at the end of a committed motor sequence (commitment release).
That signal is, biologically, *contingent on a completable task*: an animal in a
barren environment with no reachable goal never produces the completion-linked
beta drop either. The REE mechanisms here are faithful translations (not
formal-definition imports), and the failure exactly matches the missing-dependency
signature: the dependency that is absent is **goal achievement at runtime**, not
the closure mechanism. No `/lit-pull` is indicated.

## 5. Four-layer diagnosis (applies to all four)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | test never let claims express; "weakens" misattributes the layer |
| Biological reference | clear | completion/closure requires a completable task; barren-env analog |
| Prerequisites | **missing** | goal-achievement layer (SD-054 onboarding / foraging competence) not yet runtime-functional |
| Implementation | **complete** | predecessor hand-poke diagnostics pass; SD-034 substrate `implemented` |
| Environment | **inadequate** | produces commitment but no goal completion / no mode diversity |
| Measurement | adequate | criteria correctly report nothing fired (464b-C3 guard even caught the vacuous baseline) |
| Integration | partially coupled | commitment + latch couple; closure-trigger chain never armed |
| Scale/capacity | adequate | not a budget/depth issue |

## 6. Cluster pattern

| Experiment | Claim | Negative-control / trivial criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| 460b | SD-034 | (closure-OFF arm) | C1/C2/C3 all fail (`n_closures=0` even ON) | closure never fires |
| 461b | MECH-090/SD-033a | -- | C1/C2 fail (`n_windows=0`) | no resolution window forms |
| 466b | SD-034/MECH-094 | C3 trivially passes | C1/C2 fail (`n_closures=0`, `discharge=0`) | no closure -> no discharge |
| 464b | MECH-266/SD-032a | C2 trivially passes | C1 fails; C3 vacuous-baseline guard fires | monostrategy: no internal modes |

**Reading (confirmed with user):** this is **one structural property, not four
independent bugs.** The `committed_mode_curriculum` + `CausalGridWorldV2` + GAP-3
tolerance-band completion does not yet produce completed waypoints / goal
achievements at runtime, so every OCD-axis behavioural mechanism that triggers
*on* closure/completion cannot express. 464b's monostrategy is the same root one
layer out: with no reachable goals there is no internal_planning/replay mode to
switch into, so the mode-arbitration contrast is measured against a degenerate
no-switch baseline. This folds into the already-diagnosed
`scaffolded_sd054_onboarding` goal-pipeline ceiling (603e / 626a / 634b cluster):
z_goal stays at zero-init; the survival/foraging-competence + benefit-input
prerequisite is the missing layer. The goal-*wiring* is verified closed; goal
*achievement* is the gap.

## 7. Learning extracted

- Behavioural successors of passing hand-poke diagnostics are a clean detector of
  the environment/test-bed ceiling: API-correct + loop-silent = the trigger
  condition is never produced, not the mechanism wrong.
- The SD-034 closure layer is gated end-to-end on goal completion; until the
  goal-pipeline produces completions, the entire OCD-axis behavioural battery
  (460b/461b/464b/466b and any sibling closure-triggered test) is blocked on the
  same substrate and should not be re-run before `scaffolded_sd054_onboarding`
  validates.
- **Illusory-conflict caveat (required).** Reclassifying to non_contributory must
  be paired with `pending_retest_after_substrate`. SD-034's surviving support is
  narrow -- a single hand-poke / substrate-readiness pathway (V3-EXQ-460/461/466
  diagnostics); there is no independent behavioural confirmation yet. Governance
  must not read the removal of these weakens-rows as conflict resolution.

## 8. Routing (confirmed)

- **All four:** implement-substrate, `action = amend`, `target_sd_id =
  scaffolded_sd054_onboarding`. Append four failure records (Section 9 JSON).
  Recommend governance broaden that entry's `unblocks_claims` to add SD-034,
  MECH-090, MECH-094, MECH-261, MECH-266, SD-032a, SD-033a (MECH-260 already
  present). No new substrate entry -- the gap is already queued at priority 1.
- Recommend governance set, per tagged claim, `evidence_direction:
  non_contributory` + `pending_retest_after_substrate: true` and write the
  drafted `evidence_quality_note` below.

### Drafted evidence_quality_note (governance to write, per claim)

> Behavioural successor V3-EXQ-460b/461b/464b/466b ran to completion but could
> not test this claim: in the live committed_mode_curriculum loop the agent
> commits (beta latch engages) but never tolerance-completes a waypoint, so the
> SD-034 closure event never fires (n_closures=0 in every arm, including the
> positive arm) and no closure-triggered behaviour (beta release, No-Go install,
> residue discharge, delayed-resolution coupling, mode switching) can express.
> Predecessor hand-poke diagnostic passes (V3-EXQ-461 PASS), so the mechanism API
> is correct; the gap is the goal-achievement/foraging-competence layer tracked
> by substrate_queue `scaffolded_sd054_onboarding`. Reclassified non_contributory
> + pending_retest_after_substrate; do not read as claim pressure. Surviving
> support is narrow (single hand-poke pathway) -- not conflict resolution.

## 9. Machine-readable

See `failure_autopsy_V3-EXQ-460b-461b-464b-466b_2026-06-04.json`.
