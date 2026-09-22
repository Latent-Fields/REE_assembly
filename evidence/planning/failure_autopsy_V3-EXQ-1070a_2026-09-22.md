# Failure autopsy -- V3-EXQ-1070a (ARC-029 env operating-point feasibility)

Status: **confirmed** (Step 8 gate held 2026-09-22, user present; Step 7c red-team `fable` cross-model **CONTESTED**, revisions applied)
Target: `v3_exq_1070a_arc029_env_operating_point_feasibility_20260920T155046Z_v3` -- diagnostic, **FAIL**, self-route `substrate_not_ready_requeue`, indexer `precondition_unmet`. ree-cloud-2, 5h00m10s, 5 rungs x 3 quantiles x 2 seeds = 30 cells. Supersedes V3-EXQ-1070.

## 1. Facts

Dry-run gate: `check_dry_run_citations.py` over both cited run_ids -- 0 dry, 2 clean. `validate_recording.py` -- OK, always-core complete (`substrate_hash`, `config`, `seeds`, `machine`, `elapsed_seconds`, `recording_schema` all present). `validate_experiments --checks dry_run_unreachable_criterion` -- silent on this driver (it fires only on the unrelated `543*` ARC-062 family).

**All four scored criteria PASSED.** D1 ladder swept episode length 2.8418 (>= 2.0); D2 bar confirmed in force 1.0 (>= 0.95); D3 joint feasible region 3 rungs / 22 cells (reported, not gating); D4 lineage control 6 (reported, not gating).

**Five of six readiness preconditions met.** The single red one is the whole FAIL:

| precondition | measured | threshold | dir | met |
|---|---|---|---|---|
| variance_tracking_bar_in_force_somewhere | 1.0 | 0.95 | lower | yes |
| commit_gate_window_filled_in_some_cell | 30 | 1 | lower | yes |
| training_collapsed_running_variance | 1.2803 | 0.5 | lower | yes |
| **training_tick_budget_equalised** | **2.278592375366569** | **2.0** | **upper** | **NO** |
| all_rungs_tick_budgetable | 0 | 0 | upper | yes |
| driver_never_writes_running_variance | 0 | 0 | upper | yes |

`outcome` is `all(preconditions) AND ladder_non_degenerate` (driver `:1406`, `:1234`) -- D2/D3/D4 have no path to it. `TRAIN_TICK_SPREAD_CEILING = 2.0` is a bare module constant (`:538`) whose only provenance is a restating inline comment; it is reused verbatim from V3-EXQ-1070.

**This is the SECOND consecutive run in this lineage to fail this same gate** (1070 measured 3.9588). The repair worked partially and not enough: the two-stage per-(rung, seed) pilot cut the spread 3.9588 -> 2.2786 and carried all 30 cells to completion, where 1070 decided at block 5 of 10 after 12 of 30 cells.

### Realised training ticks (`n_p0_ticks + n_p1_ticks`, per rung x seed)

| rung | seed 0 | seed 42 | rung mean |
|---|---|---|---|
| L0_lineage_control | 1298 | **1023** (MIN) | 1160.5 |
| L1 | 1091 | 2063 | 1577.0 |
| L2 | 2047 | 1456 | 1751.5 |
| L3 | 1158 | 1352 | 1255.0 |
| L5_extreme | 1262 | **2331** (MAX) | 1796.5 |

2331 / 1023 = 2.278592375366569 -- recomputed independently from `arm_results`, matches the manifest exactly.

## 2. The gate is sound; only its one-line description is compressed

The precondition reads "max/min REALISED total training ticks **across rungs**", and computes `max/min` over the 10 (rung, seed) cells (`:1152-1155`). Across **rung means** the figure is 1.5480, under the ceiling; across **cells** it is 2.2786.

A first draft of this autopsy read that as a construct/statistic mismatch wanting two bounds. **That is withdrawn.** The driver at `:60-67` had already considered exactly this:

> *(b) Gate on the per-rung MEAN instead of the per-cell spread, on the argument that only between-rung variation confounds the manipulation. 1070's per-rung means are 1294 / 1736 / 685 / 614 / 668, a spread of **2.83** -- still over the ceiling. **It also relaxes the precondition, which the repair brief forbids.***

and names between-seed variance as the second error source it is deliberately targeting ("realised ticks vary up to **2x BETWEEN SEEDS at one rung**"). So the per-cell denominator is the intended construct. Only the compressed one-line description says "across rungs". **Do not relax the ceiling or switch it to per-rung means.**

## 3. The gate is nonetheless correctly red

P1 is feasible in **30/30** cells and the quantile bar is contract-pinned to fire at ~q (`tests/contracts/test_commit_threshold_variance_tracking.py`), so P1 carries no information here. **`harm_snr >= 10` is the sole binding discriminator**: all 30 cells clear the absolute harm floor by >= 6.3x, and the 22 jointly-feasible cells are exactly the 22 P3-feasible ones.

In all three rungs where feasibility varies by seed, the higher-tick seed is the worse one (L2 s0 2047 -> 0/3 vs s42 1456 -> 3/3; L5 s42 2331 -> 0/3 vs s0 1262 -> 2/3; L3 s42 1352 -> 2/3 vs s0 1158 -> 3/3). **Stated honestly: at n = 3 informative rungs that is p = 0.125 under a coin-flip null.** And the mechanism is better attributed to **episode length** -- the manipulated variable -- than to training depth: episode length predicts low `harm_snr` across all 5 rungs, tick count across only 4, with L0 reversed. The gate's redness does not rest on either: a pre-registered equalisation condition was violated, which disqualifies the between-cell comparison regardless. **The identity of the feasible-rung set must not be cited.**

## 4. The residual this autopsy drafted, and withdrew

An earlier draft offered a "narrow citeable residual": L0 and L1 jointly feasible on both seeds across within-rung tick ratios of 1.2688 and 1.8909, with per-cell `harm_snr` 27.763-59.765 and 13.524-23.588 against a floor of 10, while all 8 infeasible cells sit within 12% of that floor. The numbers are correct. **The inference is withdrawn in full**, on red-team F1, for three independent reasons:

1. **The P3 half was never in dispute.** GFLAG-0371 already records mean reward/step at the lineage env as -0.12 to -0.29, "20-100x ABOVE the recalibrated band P3 worries about".
2. **The P1 half is the pre-rejected one.** It is contract-pinned (the detrended quantile bar fires ~q by design) and is obtained only by filling a window spanning 38.8 episodes at L0 -- which GFLAG-0371 rejects in terms: *"Filling the window would pool rv across ~35 episode boundaries, so it would not be the within-run distribution the estimator is specified against."*
3. **Wrong arm.** 1070a is the STATIC arm (`breath_period=0`, MECH-108 OFF, asserted `:679`); ARC-029's P1 is specified for the ALTERNATING arm.

This is the same error `failure_autopsy_V3-EXQ-1070_2026-09-20` made and withdrew -- rescuing a reading from a run whose own `routes_to` says no env verdict is licensed. The draft asserted it was "deliberately NOT a P1 rescue" because it rested on P3; that defence fails precisely because P3 was already granted. **The run's `routes_to` is right without qualification.**

## 5. The M4 bind, measured

| rung | mean ep len | window span (episodes) | harm_snr | feasible |
|---|---|---|---|---|
| L0_lineage_control | 5.61 | 38.8 | 42.111 | yes |
| L1 | 10.67 | 26.8 | 18.285 | yes |
| L2 | 15.94 | 19.5 | 11.213 | no |
| L3 | 11.98 | 21.7 | 11.505 | yes |
| L5_extreme | 14.62 | 17.3 | 9.611 | no |

Softening the env lengthens episodes, which shrinks the span of the 200-select-call window the commit quantile is **estimated** over -- and simultaneously drives `harm_snr` through the P3 floor. **The minimum span in any of the 30 cells is 15 episodes.** This is the P1/P3 bind of `arc029_exq1066_prereg_derivation_20260919.md` M4, measured rather than argued.

**This is a validity caveat on the bar, not a claim that P1 is unreachable.** P1's own gating statistics are met everywhere and are episode-segmented (`committed_step_fraction` 0.471-0.549; `mean_committed_run_length` 3.52-9.38 vs a floor of 3.0); the cross-episode view is carried separately as `mean_committed_run_length_flat` (driver `:877`, "descriptive: the cross-episode view, so the boundary effect is visible"). What is cross-episode is the window the *threshold* is estimated over. `failure_autopsy_V3-EXQ-1070_2026-09-20` raised the same caveat and withdrew a P1 rescue over it; this run reproduces it across a full 30-cell sweep.

## 6. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear (protected) | upstream of ARC-029's falsifier; P1's gating halves met in every cell |
| Biological reference | clear | BG go/no-go commitment vs deliberative modes; `targeted_review_arc_029` present |
| Prerequisites | present | bar in force 1.0 on 30/30; window filled 30/30; rv collapse 1.28 decades worst cell |
| Implementation | complete | for the lever under test |
| Environment | partial | cannot shorten the estimation window without pushing harm_snr through the P3 floor |
| Measurement | **under-instrumented (DOMINANT)** | pilot mispredicts P1 ticks/episode 0.5629x-2.1499x; threshold estimated over 15-39 episodes |
| Integration | coupled | |
| Scale | likely insufficient | 2 seeds, so every within-rung split rests on n=1 vs n=1 |

**Failure location (GOV-FAILLOC-1): MIXED -- MEASURES, with ENVIRONMENT partial.** MECHANISM established, so a REE-failed read is not available. Not chargeable to REE or to ARC-029.

## 7. Withdrawn during drafting

Recorded rather than deleted, because each was tested and did not hold. Two were caught by my own reading before the gate; two by the cross-model red-team after it.

1. **"The Step-4 refusal of `v3_exq_1066` is falsified by `bar_in_force` = 1.0"** -- and the routing built on it (re-queue 1066 at L0/L1). The refusal (GFLAG-0371) is a multi-clause bind; this run falsifies only the `bar_in_force` clause, and that was already recorded in the prereg addendum *before* 1070a ran. 1066 is not awaiting a re-queue: it **ran and ERRORed** 2026-09-20T15:08:23Z (ree-cloud-3), its diagnosis is owned by an active claim, and chip `chip-20260921-diagnose-exq-1066` is claimed by a live session. It could not have run at L0/L1 as written in any case -- `WARM_EPISODE_CAP=30` against the 39 episodes needed at L0, env hard-coded to the lineage kwargs, and a P3 that counts harm EVENTS rather than SNR.
2. **"ARC-029's P1 is unreachable anywhere on this ladder."** Conflated the window a statistic is *estimated over* with the statistic a precondition *gates on*. P1's gating halves are episode-segmented and met in every cell.
3. **The L0/L1 narrow residual** -- see section 4. Withdrawn in full (red-team F1).
4. **"The gate's construct and its statistic have come apart."** Downgraded to a documentation nit (red-team F4) -- the per-cell denominator is deliberate and per-rung means are a pre-registered forbidden relaxation.

## 7b. Step 7c red-team

- **Model:** `fable` -- cross-model (this session drafted on Opus 5).
- **Verdict: CONTESTED.** Disposition survived: direction `non_contributory`, category `standard`, failure-location MIXED/not-chargeable, routing `governance-note-only`.
- **Changed:** F1 residual withdrawn in full (`narrow_supports_flag` true -> false); F2/F2(iv) on the 1066 bind and its live ownership; F3 mechanism re-attributed to episode length; F4 gate-mismatch downgraded; hygiene -- static arm, so the predecessor's "P1 as registered was not measured" applies here too.
- **Cheap confirmers run:** GFLAG-0371 read verbatim; driver `:60-67` and `:679` read; tick spread and per-rung/per-seed feasibility recomputed independently from `arm_results`.

## 8. Routing -- `governance-note-only`

**User decision at the Step 8 gate: settle the construct first.** No further ARC-029 env run is queued until `/governance` answers the open question below. A third feasibility letter (V3-EXQ-1070b -- repair the PILOT, which is where the error is, and add a mid-run abort) was offered and **not** taken: it would deliver a clean feasible-rung boundary on an operational P1 that is contract-pinned, cross-episode, and measured on the static arm, i.e. a clean answer to a question ARC-029 did not ask. **Do not relax the ceiling or switch it to per-rung means** -- the driver forbids both (`:60-67`). `substrate_ceiling` was explicitly considered and **not** stamped -- the argument for it was withdrawn (section 7), and stamping it would move ARC-029 into `_EPI_SUPPRESS_PROPOSAL` and make it not-v3-testable.

**Open question for governance.** Is ARC-029's commitment bar intended to be a within-run drift-tracking quantile, or a cross-episode one? Answering it decides whether the next ARC-029 step is an experiment or a substrate build. M4 argues a narrower window is blocked below W ~ 50 by the rv EMA time constant (~20 select calls), so it is not a knob.

Per CLAUDE.md this autopsy does **not** `spawn_task` its own routing, and must not chip the 1066 ERROR -- that work is already owned.

## 9. Brake, granularity, debt class

- **Re-derive brake: does NOT fire.** ARC-029 ceiling count 0 under R1-R3 (6 targets tag the claim, none reads `substrate_ceiling`); an instrument defect owing no substrate build does not count. Noted for the reader: the brake is not the only recurrence signal here -- this is the second consecutive run to fail the same named precondition after a targeted repair, which the ceiling brake is not designed to catch.
- **Granularity trigger: does NOT fire.** `granularity_debt_cluster.py ARC-029`: 6 targets, alignment distribution `unclear=6`, none `weakened` -> measurement/implementation debt, not granularity debt.
- **Debt class:** `complex (probe-gated)` -> `mystery (known data)`. The data to settle the estimator question is already on disk; what is wrong is the frame, not the sample size.
