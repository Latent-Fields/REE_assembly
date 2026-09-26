# Probe DCH2 / N5b (audit H2 stage 1): does an unexpected-uncertainty statistic, fed by regime-surviving probe bouts, detect the action-map shift that N5's surprise gate missed?

- **Status: PRE-REGISTRATION (sections 1-3 and addendum 3a), committed before any registered seed (841-852) ran.** Calibration seed 840 (P-b, timing, threshold calibration on its no-shift cells) ran first and is disclosed in 3a. Results follow in sec 4.
- Session `bt0926-dch2` (orchestrator `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dcd2-h2-shift-detector`. User-approved 2026-09-26 (probe only).
- **Spec:** audit H2, `dynamic_control_audit_20260926.md` sec B (e3cafebab3). Context: `n5_ach_gated_unfreeze_probe_20260926.md` (b26d8e8d9d; harness reused), `dynamic_control_discrimination_plan_20260926.md` (41cfe94841; DCD2: signal validity first).
- **Code:** ree-v3 `4070b0efa4` (tag `archive/coupled-loop-repair-4070b0e`), private detached worktree `.scratch/wt-dch2`. **No `ree_core` edit**: the shift, the probe actions, both statistics and g are harness-side.
- **Probe:** `probes/dch2/dch2_probe.py` (one process = one seed, every cell), analyser `probes/dch2/dch2_analyze.py`.
- **Evidence domain reachable: D1** (a detector's separation of shift from no-shift on the clamped pair). No consumer, no behaviour. Stage 2 (D2) only if stage 1 separates and budget remains.

## 1. Premises re-measured before registering

| # | premise (source) | re-measured on `4070b0efa4` | verdict |
|---|---|---|---|
| P1 | the N5 action-map shift is an env-side overwrite of `_action_map` (N5 P2) | `CausalGridWorld.step` reads `dx, dy = self._action_map[action]` (`ree_core/environment/causal_grid_world.py:2532`); a move is blocked only by a wall (`:2566`); `_action_map` is built at `:981` and is not reset per episode (`:1879` comment) | holds. The probe overwrites the running env's `_action_map` mid-episode with N5's fixed derangement `SHIFT_P = [2, 3, 1, 0]` (stay unchanged) |
| P2 | a probe action can be injected without an env reset and still be recorded with its executed action | the E2 member stores the pending action from `agent._last_action` at `observe()` (`ree_core/utils/waking_trainer.py:466-485`), which runs in `update_residue` AFTER `env.step` (`agent.py:12409`, `experiments/_harness.py:354`); the `on_action` hook fires before `env.step` (`_harness.py:347-352`) | holds. An env proxy executes the probe class and sets `agent._last_action` to it; the member's source tag is set in `on_action`, so each record carries its executed action and its source. The agent still runs its own selection on probe steps (cost matched) |
| P3 | no native ACh / MECH-398 signal exists to drive a detector (N5 P1) | `git grep` for `MECH-398`, `acetylcholine`, `cholinergic` in `ree_core/`: zero hits | holds; both statistics are harness-side |
| P4 | the W3 gate (a) is disc4_h1 >= 0.47 AND k = 10 (N5) | `4070b0e`'s own commit subject: "W3 contract: member gate (a) is disc4_h1 >= 0.47 ALONE (k conjunct dropped; k kept as a readout)" | **corrected**: P-a uses disc4_h1 >= 0.47 alone; k is reported |
| P5 | reset-init raises the W3 pass rate (audit H2 P-a; 9/15 -> 13/15) | the four knobs exist at `4070b0e` (`ree_core/utils/config.py:175ff`), default OFF | the probe sets all four ON on the reference and the agent (cgdisc's `set_knobs`), and still pre-screens |
| P6 | N5's babble-source baseline (400 records drawn from the retained set) is a fair "expected uncertainty" model for probe records | the retained set is the head's own training data: its errors are in-sample, so fresh probe records would read as surprising with no shift at all | **corrected**: both per-source baselines are initialised from a held-out baseline-calibration life (sec 2), out of sample, identical for every cell |

## 2. Design (pre-registered)

**Per seed, shared phase (N5 phase 1 verbatim, reset-init ON):** reference `build_B` (world_dim 32 = deployed, alpha_world 0.3); held-out TE_orig (the W3 test set: 3000 uniform-random steps, env k = 120..134); `E2WorldMember` (lr 3e-4, batch 32, MSE, grad_clip 1.0, retained cap 5000, reencode); W2a babbling 2400 steps -> FROZEN retained set; 3000 updates; 1200 native `StepHarness` steps x 8 updates at the 25% retained mix.

**P-a (pre-screen, per seed):** disc4_h1 on TE_orig at the end of the shared phase >= 0.47. A failing seed runs no cells and is reported as rejected.

**Seeds:** calibration seed 840 (not registered; P-b and timing, run with `--force`). **Registered: the first 5 seeds of 841, 842, ..., 852 that pass P-a**, in that order. If fewer than 5 of the 12 pass, the verdict is CANNOT_DETERMINE (P-a unmet).

**Baseline calibration life (once per seed, from the snapshot, trainer frozen):** 600 steps, original map, env k = 40.., the 8% probe schedule. Per-source (on-policy / probe) mean and variance of `ac` from the snapshot head = the expected-uncertainty model's initial state, the same for every cell.

**Cells (each from the snapshot, `R.seed_all(S + 700)`, env k = 61..):** N = 1200 adult steps, native 200-step episodes, **clamped g = 0.1** (member lr 3e-5, 8 updates per step, on-policy records trained as in N5's clamped cell; the retained set stays FROZEN; **probe records are scored only and never trained on**; no unfreeze anywhere).
- **shift** cells: at adult step **T_S = 700** (mid-episode: episodes start at 600 and 800) the running env's `_action_map` is overwritten with the derangement, and every later env is built shifted. **no-shift** cells: never. Shift and no-shift cells of a seed are identical up to T_S.
- **probe schedule** B steps in every 100: steps with (t mod 100) >= 100 - B are probe steps (the agent selects, the env executes a `StructuredBabbler` action: 5 classes, runs 1-4, reset at the start of each bout; same env, no reset). **OFF: B = 0. ON8 (registered): B = 8, 8% of steps, under the 10% ceiling (F3).** ON25 (report-only, for F3 only): B = 25.
- Cells per seed: shift/no-shift x {OFF, ON8, ON25} = 6.

**Per record** (each stored transition): `pe` = log one-step MSE of the member head under the executed action; `ac` = `pe` minus the log MSE of the best alternative class (N5's action-contrastive error). z = (ac - mu_src) / sd_src, per source; the source baseline is then EMA-updated (alpha_b = 0.005, N5's value). Both statistics read the same z stream:
- **MAG (N5's gate statistic, verbatim):** s = EMA(z, 0.05) over the merged stream; arousal a = EMA(1[s > 0.75], 0.05); g_would = 0.1 + 0.9 a; **alarm = rising edge of (s > 0.75 AND g_would > 0.5)** (N5's unfreeze coincidence).
- **CP (unexpected uncertainty; change-point):** a one-sided CUSUM per source, C = max(0, C + z - K), K = 0.5; **alarm when C > H = 5**, then C = 0. (For N(0,1) z this pair gives a nominal in-control run length of about 930 records and about 10 records to detect a 1-SD mean shift; nominal only.) A never-reset copy gives the threshold-free score.
- MAGps (report-only, attribution): MAG's rule run separately per source.

**DVs (scored only by the analyser; the condition is never visible to either statistic):**
- latency window W = [T_S, N) = [700, 1200) (500 steps; it holds 5 ON8 bouts, 40 probe records).
- per condition X = statistic x probe level, over the registered seeds: hit = the shift cell alarms in W; false alarm (FA) = the no-shift cell alarms in W; **sep_X = (hits - FAs) / n_seeds**.
- threshold-free: **AUROC_X** of the window score (MAG: max s in W; CP: max rise of the never-reset per-source CUSUM inside W, max over sources) over shift vs no-shift cells, pooled over seeds.
- false opens per 1000 steps in no-shift cells (whole adult phase); latency of the first alarm in W.
- **wrong-reason control (rate-matched random trigger):** for each seed, a Bernoulli trigger at that seed's pooled alarm rate for X (alarms per step over its shift + no-shift cells); 20,000 simulated 5-seed draws give p_rand = P(random sep >= observed sep).
- P-b / informativeness, every step: executed class, source, **informative** (the original and shifted maps give different displacements from the current cell, i.e. at least one of the two target cells is passable), moved.

**P-b rule (stated before the calibration seed ran):** on calibration seed 840, if the on-policy stream's informative fraction is >= 0.5 x the probe stream's (pooled over its cells), the on-policy stream already carries map information, the probe arm is unnecessary, and the design is re-planned before any registered seed (addendum). Otherwise proceed.

## 3. Verdict rules, cost and stop rules (pre-registered)

**A condition X "separates" iff sep_X >= 0.6 AND AUROC_X >= 0.80 AND p_rand < 0.05.** Comparison margin between conditions: 0.4 in sep.

Verdict, in this order:
1. **CANNOT_DETERMINE** if fewer than 5 registered seeds pass P-a, or a precondition channel is degenerate (for example ac variance ~0 in either source, probe records not arriving, the shift not live).
2. If CP-ON8 separates:
   - MAG-ON8 also separates and sep(CP-ON8) - sep(MAG-ON8) < 0.4 -> **F2** (the gain belongs to the probe, ARC-156; the statistic adds nothing measurable).
   - else, CP-OFF separates and sep(CP-ON8) - sep(CP-OFF) < 0.4 -> **STATISTIC-ONLY** (named here in advance: the change-point statistic separates without probes; the probe leg is not needed. P-b should have caught this).
   - else -> **SUPPORTED** (at D1: an unexpected-uncertainty statistic fed by probe evidence detects the shift; neither magnitude with probes nor CP without probes does).
3. If CP-ON8 does not separate:
   - CP-ON25 or MAG-ON25 separates -> **F3** (detection needs a probe budget above the 10% ceiling: continuous babbling, not detection).
   - else -> **F1** (with probes ON the change-point statistic separates no better than magnitude; no detector found at this budget).

Report-only, not verdict: MAG-OFF (N5's own configuration, expected not to separate), MAGps, latencies, false opens per 1000 steps.

**Stage 2** (endogenous vs oracle-timed wholesale quarantine, F4, D2) runs only if the verdict is SUPPORTED, STATISTIC-ONLY or F2 and the ~2.5 h compute cap has room; it would be pre-registered in an addendum before it runs.

**Cost and lock.** One seed ~ shared phase (~4 min) + calibration life + 6 cells x ~1.5 min: ~14 min of Mac CPU, split into holds of <= 12 min (the process releases the Mac probe lock at a cell boundary, waits 45 s, re-acquires). 2 torch threads. A P-a-rejected seed costs ~4 min. If the ~2.5 h compute cap is reached before 5 registered seeds complete, the verdict is reported over the seeds completed as **INTERIM**, never silently. ON25 cells are the first thing dropped if the budget binds (they are report-only).

## 3a. Addendum (P-b fired on calibration seed 840; re-plan before any registered seed)

Registered after calibration seed 840 ran and **before** any of 841-852 ran. Seed 840 is not a registered seed and never enters the verdict. Its files: `probes/dch2/results/CALIB_s840.{json,log}`. It missed P-a (disc4 0.433) and was run with `--force` for P-b, timing and the in-control behaviour of the statistics.

**P-b result: the rule fires.** The native policy IS concentrated and wall-pressing (class 0 on 74-91% of on-policy steps, class 2 on most of the rest; the agent moves on only 8-21% of on-policy steps). But 55-96% of on-policy steps are map-informative (per cell and period; the probe stream: 62-80%). The on-policy fraction is far above the rule's 0.5 x the probe fraction. **N5's wall-pressing account (sec 4.2 there: "a blocked move produces the same next state under both maps") is wrong for this shift.** Under a derangement, a move blocked by a wall under the original map is usually passable under the shifted map, and vice versa, so pressing a wall is informative about the map. (Head-level display, seen while checking P-b: on seed 840, map-informative on-policy records after the shift have mean z +0.43 / +0.56 in the shift cells vs +0.06 / +0.11 in the no-shift cells, probes OFF / ON8. This was looked at before registration and is disclosed here.)

**Second calibration finding: the nominal CUSUM thresholds are unusable.** The in-control z stream is strongly autocorrelated (the policy repeats one action against one wall for many steps). With K = 0.5, H = 5 the CUSUM alarmed 31-41 times per 1,200 no-shift steps (nominal: about one per 930 records). N5's fielded MAG threshold (0.75) alarmed 2-7 times per 1,200 no-shift steps. At those rates a 500-step window always holds a false alarm, so neither statistic could separate for a reason unrelated to the question.

**Re-plan (all fixed now, before any registered seed):**
1. The stage-1 cells, seeds rule, schedule, window and DVs of sec 2 are kept unchanged. The statistics are recomputed post hoc from the stored per-record z stream (`probes/dch2/dch2_stats.py`; the recompute reproduces the online alarm counts exactly on all 6 seed-840 cells at the original thresholds). No rerun is needed, and nothing an agent sees changes.
2. **Thresholds recalibrated on seed 840's three NO-SHIFT cells only** (3,600 steps; its shift cells were not scored). Rule: the smallest value on a grid with <= 1 pooled alarm. **CP: K = 0.5, H = 45** (grid 5..80; 45 gives 1). **MAG: threshold 1.2** (grid 0.75..2.0; 1.2 gives 1; alphas and the g > 0.5 arousal coincidence unchanged). The two statistics are thereby matched on false-alarm rate. N5's 0.75 is kept as a report-only condition (MAGn5).
3. **The probe factor is kept** as a control on evidence *quality*, because it costs nothing extra and probe records sample all classes. **Its interpretation changes:** P-b has refuted the premise that the on-policy stream is starved of map evidence here, so a probe effect, if any, can no longer be read as ARC-156's "regime-surviving evidence *availability*". The outcome P-b predicts is STATISTIC-ONLY or F1.
4. **Verdict tree refined** (sec 3 step 2, first bullet). When CP-ON8 and MAG-ON8 both separate within the margin, the verdict is **F2 only if neither statistic separates with probes OFF**. Otherwise it is **F1** (both statistics separate with and without probes: the change-point statistic adds nothing over a calibrated magnitude statistic). All other rules stand. CP-ON8 not separating while MAG-ON8 does is F1.
5. Everything else stands: separation criteria (sep >= 0.6, AUROC >= 0.80, p_rand < 0.05), margin 0.4, the 10% budget ceiling, stage 2 only after separation, the INTERIM rule.
