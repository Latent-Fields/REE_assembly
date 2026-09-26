# Probe N5: does ACh-gated unfreeze revise W3's retained memory only when it should? (2x2 on the W3 member)

- **Status: PRE-REGISTERED** (sections 1-3 committed before any registered seed ran). Session `bt0926-n5` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260926-coupled-n5-ach-unfreeze-probe`. Written 2026-09-26T00:24Z.
- **Code:** ree-v3 `1b013d6` (tag `archive/coupled-loop-repair-1b013d6`, `integration/coupled-loop-repair` with W3 `7428da3` + W6a + W4), throwaway detached worktree `.scratch/wt-n5`. **No `ree_core` edits**: g, surprise, unfreeze and the env shift are all harness-side.
- **Plan of record:** `coupled_loop_repair_campaign_plan.md` sec 3 W2 (W2b unfreeze rule), sec 4 N5 row, W2b status row. Upstream: W3 record `w3_e2_world_member_build_20260925.md` (f82cb986c5); W3 probe code reused (`probes/w3/w3_l2r_member_probe.py`), B0 recompute recipe from N2 (`probes/n2`).
- **Probe:** `probes/n5/n5_probe.py` (one process = one seed, all cells), lock wrapper `probes/n5/with_lock.sh` + `lock_acquire.py`, results `probes/n5/results/`.
- **Evidence domain reachable: D1** (a member-trained head's discrimination on held-out data under a harness-side gain/unfreeze rule). No consumer (E3) or behaviour claim.

## 1. Premises re-measured before registering

| # | premise (source) | re-measured on `1b013d6` | verdict |
|---|---|---|---|
| P1 | an existing ree_core ACh / MECH-398 / MECH-207 signal could drive g (brief) | `git grep` for `MECH-398`, `MECH-207`, `acetylcholine`, `cholinergic`, `ach_gain` in `ree_core/`: **zero hits**. Nearest native surprise signals: E3 `last_instantaneous_pe` (`ree_core/predictors/e3_selector.py:1036-1052`, written by `update_running_variance`, fed at `:5019-5025` from the selected trajectory's `world_states[1]` vs the observed z_world) -- read only by SD-069 `phasic_surprise_burst` (`ree_core/agent.py:10370-10378`); MECH-205 `surprise = pe - pe_ema` (`agent.py:12308-12313`, behind `surprise_gated_replay`, default OFF). Neither scales any learning rate or gates any buffer, and E3's PE is undefined during a babbling bout (no E3 selection) | **no usable native g.** g is implemented HARNESS-SIDE as a scalar on the member's optimizer lr and on retained-set write permission (sec 2) |
| P2 | "the SD-MEL-PRODUCER action-map permutation" exists and is the shift to use (plan N5 row) | `CausalGridWorld._maybe_shift_world_rule` (`ree_core/environment/causal_grid_world.py:2110-2143`) applies `world_rule_shift_depth` random transpositions to `self._action_map` (all 5 keys, stay included), read by `step()` at `:2532`; `_action_map` persists across `reset()` (`:1879-1880`) | holds. The probe applies the same operation (overwrite the effective `_action_map`) but with a **fixed derangement of the 4 move classes** (`SHIFT_P = [2, 3, 1, 0]`, stay unchanged) on every env built after the shift step, so every seed gets the same, maximal shift of the classes disc4 scores (a random transposition can hit stay, which disc4 does not score). Live check (calibration seed 799): empirical modal displacement per class orig `{0:(-1,0),1:(1,0),2:(0,-1),3:(0,1),4:(0,0)}` -> shifted `{0:(0,-1),1:(0,1),2:(1,0),3:(-1,0),4:(0,0)}` |
| P3 | W3's protocol and B0 are reproducible for fresh seeds (W3 record; N2 P4) | reused verbatim: W3 member probe phase (babble 2400 -> 3000 updates -> 1200 native steps x 8 updates, 25% retained, re-encode); B0 recomputed with N2's `--n-eps 12` recipe | holds (calibration ran end to end) |
| P4 | the whole agent can be snapshot so all cells start identical | `copy.deepcopy(agent)` raises `TypeError: cannot pickle 'module' object` (a module reference inside the agent graph -- the same crash N2 hit) | handled: modules are shared by reference during the deepcopy (`copy._deepcopy_dispatch[types.ModuleType]`); every other object, trainer + member buffers + optimizer + RNG state included, is copied. Each cell asserts `member._agent is copy` |
| P5 | "surprise = E2-world one-step error on the retained set above threshold" (plan sec 3 W2b) | a retained-set error cannot rise at a shift until the head has already moved toward the new map (the retained entries are old-map data the head fits), and under a low g the head barely moves -- so it lags and is confounded with g itself | **corrected:** the surprise reads INCOMING experience (each newly recorded transition). Retained-set error is reported, not gated on |

### Calibration (seed 799, not a registered seed; disclosed before any registered seed runs)

`probes/n5/results/CALIB_s799.{log,json}` (run by the pre-change revision of `n5_probe.py`: PE gate, `lronly` cell; its arguments are recorded in the JSON `args`), n_adult 1800, gate = **the brief's example signal** ("PE": the member head's log one-step MSE on each new transition, z-scored per source against an EMA baseline, s = EMA(z, 0.2), threshold 2, arousal integrator EMA(1[s>2], 0.05), g = 0.1 + 0.9 a, unfreeze iff s > 2 AND g > 0.5):

- pre-shift (end of the W3 protocol): orig disc4 0.453 / k 10 (bar missed by 0.017; W3 s108 also missed at 0.460); on the shifted map 0.273.
- **The PE detector is blind to the shift.** On-policy z after the shift: mean -0.10, p(z>2) 0.037, max 2.6; with no shift: mean -0.05, p(z>2) 0.054, max 3.2. The gate never opened in `shift_gated` (s max 1.84, 0 bouts), so `shift_gated` == `shift_clamped` exactly (shift-map disc4 0.287). In `noshift_gated` it opened **once, spuriously** (step 419: 192 retained entries replaced, 1590 on-policy records flushed); the original map was still kept (0.467 / k 10).
- `shift_lronly` (g = 1, no unfreeze; on-policy + the FROZEN old-map retained set): shift-map disc4 **0.247** (no re-learn at all), orig 0.487 -- plasticity gain alone does not revise the map.
- Reading: the action-dependent part of the one-step error is small against the error's state-to-state variance at this head (disc4 ~0.47, chance 0.25), and the concentrated native policy spends many steps in blocked moves where the maps agree. A raw PE magnitude cannot carry this shift.

Changes made because of the calibration, **before any registered seed**: (1) the gating surprise becomes an **action-contrastive** statistic (sec 2), with the PE detector kept as a report-only readout in every cell; (2) a report-only **oracle** cell replaces `lronly` (lronly is answered by the calibration) -- it separates "the gate did not open" from "revision cannot reach the bar in N"; (3) N reduced 1800 -> 1200 and checkpoints dropped (cost; sec 3).

## 2. Design (pre-registered)

**Shared developmental phase per seed (g = 1), identical for all cells:** the W3 member-gate protocol (`probes/w3`): babbling-probe env (CausalGridWorldV2 size 12, new env per 200-step episode), `build_B` agent (world_dim 32 = deployed, alpha_world 0.3), `E2WorldMember` (lr 3e-4, batch 32, MSE, grad_clip 1.0, retained cap 5000, `reencode`), W2a babbling 2400 steps -> FROZEN retained set (~2280), 3000 updates, 1200 native `StepHarness` steps x 8 updates at the 25% retained mix. Then the agent (trainer, member, buffers, optimizer) is snapshot; every cell restarts from the snapshot with `R.seed_all(S + 700)`.

**Shift step:** adult-phase step 0 (immediately after the snapshot). Shift cells build every adult-phase env with the deranged map; no-shift cells with the original map. Env seeds `k = 61..` (same indices in every cell).

**Adult phase: N = 1200 waking steps, 8 member updates per step (9600 updates) in every cell.** Bout steps count toward N, so env steps and updates are matched across cells.

**g and surprise (harness-side).** For each newly recorded transition (on-policy or babble), before that step's updates, from the record's live z pair (the encoder is frozen, so live z == re-encoded z):
- `pe` = log MSE under the executed action; `ac` = `pe` minus the log MSE of the **best alternative** action class (> 0: another action explains the transition better than the one executed -- the online analogue of disc).
- per-source baselines (on-policy / babble): mean and variance from the snapshot head over the last 400 on-policy records and 400 random retained records; EMA-updated (alpha_b 0.005) only while FROZEN.
- **gating detector = `ac`:** z = (ac - mu) / sd; s = EMA(z, 0.05); arousal a = EMA(1[s > 0.75], 0.05); **g = 0.1 + 0.9 a** (gated), **g = 0.1** (clamped); member lr = 3e-4 x g.
- **Unfreeze (MECH-207 coincidence):** s > 0.75 AND g > 0.5 (never in clamped). On unfreeze: the running native episode ends; on-policy records recorded before the current surprise onset (the last upward crossing of s) are dropped; a W2a babbling bout of 200 steps runs (lr = 3e-4 x g), each babble record REPLACING the oldest retained entry (FIFO; set size constant). After a bout, another bout if the coincidence still holds, else re-FREEZE and resume the native policy.
- report-only in every cell: the `pe` detector's s (EMA 0.2, threshold 2) and whether ITS coincidence would have fired, and for `ac` the same counts.

**Cells:** `shift_gated`, `shift_clamped`, `noshift_gated`, `noshift_clamped` (the 2x2), plus report-only `shift_oracle`: unfrozen for the whole adult phase with g = 1 -- all on-policy records flushed at step 0 and every step a babbling bout step replacing retained entries (the upper bound of the revision mechanism at this N, given perfect and sustained detection).

**Seeds (fresh):** 721, 722, 723, 724, 725 (not 106-110, 531-535, N2's 611-615, calibration 799).

**Readouts (end of the adult phase, `babble_probe.evaluate`, reference encoder):**
- **post-shift bar** = W3 gate (a) on **TE_shift**: disc4_h1 >= 0.47 and k = 10. TE_shift = the W3 held-out test generator (3000 uniform-random {0..3} steps, env k = 120..134) run with the shifted map, encoded by the reference.
- **no-shift stability** = W3 gate (a) on **TE_orig** (the W3 test set) AND retention (b) (post - B0) / (pre - B0) >= 0.5, with pre = the post-babbling head (W3 definition) and B0 recomputed (N2 recipe).
- also: gate (a) on the other map, pre-shift readout (end of shared phase, TE_orig and TE_shift), bouts, unfreeze events, first coincidence step, replaced / flushed counts, retained-set MSE, g trace, guard, (e) rollout.

**Verdict (pre-registered, in this order):**
1. **CANNOT_DETERMINE** if the shared pre-shift state misses gate (a) on TE_orig on >= 2/5 seeds ("gated fails to reach the bar pre-shift"), or if `shift_clamped` reaches the post-shift bar on >= 2/5 seeds ("clamped re-learns anyway").
2. **PASS** iff BOTH halves hold on >= 4/5 seeds: (shift half) `shift_gated` meets the post-shift bar AND `shift_clamped` does not, on the same seed; (no-shift half) `noshift_gated` meets gate (a) on TE_orig AND retention >= 0.5.
3. **FAIL** otherwise, naming which half; for a shift-half FAIL, the oracle cell and the detector counts name whether the gate did not open (detection) or revision did not reach the bar in N (mechanism / dose).

Also stated (report-only, not verdict): spurious unfreeze events in `noshift_gated` ("only when it should"); the PE detector's shift/no-shift separation on 5 seeds.

## 3. Cost / stop rules

One seed (B0 + test sets ~150 s, shared phase ~80 s, 5 cells x ~90 s) is ~11 min of Mac wall under one lock hold (2 torch threads). **Reductions fixed before registering:** N = 1200 (not the calibration's 1800) and no mid-run checkpoints, because the Mac probe lock is shared with N2 (5 x ~21 min holds) and another worker. If the ~2.5 h cap is reached before all 5 seeds run, the verdict is reported over the seeds completed, labelled INTERIM, never silently. Lock: mkdir `mac_probe.lock`, owner file written only after the mkdir succeeded, released after each seed; the waiter retries every 30 s and also immediately on a change to the lock's parent directory (kqueue) -- a holder that re-acquires back-to-back otherwise starves a 30 s poller; >= 800 MB free + inactive required before acquiring.

## 3a. Addendum (exploratory, NOT verdict-bearing), registered 2026-09-26T00:36Z after seed 721 only

Seed 721 showed the report-only `shift_oracle` (1200 babbling steps at g = 1, FIFO replacing 1143 of 2293 retained entries) reaching only 0.367 on the shifted map. To tell whether the W2b revision rule must invalidate the whole contradicted retained set rather than replace it FIFO, one extra report-only cell runs on seeds 721 and 722 after the five registered seeds, as a separate process (`probes/n5/n5_probe_explore.py`, identical to `n5_probe.py` except the added mode): **`shift_oraclefull`** -- at the shift, all on-policy records are flushed AND the whole pre-shift retained set is quarantined (removed from replay); then N = 2400 babbling steps at g = 1 (a full re-development epoch, the size of the original babbling phase) with 8 updates per step. Readout: the post-shift bar on TE_shift and gate (a) on TE_orig. It does not enter the verdict.

## 4. Results

(pending)
