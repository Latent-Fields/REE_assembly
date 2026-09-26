# Probe N5: does ACh-gated unfreeze revise W3's retained memory only when it should? (2x2 on the W3 member)

- **Status: DONE -- verdict CANNOT_DETERMINE** (pre-registered rule 1: the shared pre-shift state missed the W3 bar on 3/5 seeds). On every seed, including the two evaluable ones, the shift half also fails: the gate does not detect the shift (it opens as often without one), and even an oracle unfreeze does not re-learn the shifted map to the bar in N = 1200. Sections 1-3 were committed before any registered seed ran (`815a8164bf`); addendum 3a before its runs (`3a9f2afa44`). Session `bt0926-n5` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260926-coupled-n5-ach-unfreeze-probe`. Written 2026-09-26T00:24Z.
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

## 3a. Addendum (exploratory, NOT verdict-bearing), registered 2026-09-26T00:33Z after seed 721 only

Seed 721 showed the report-only `shift_oracle` (1200 babbling steps at g = 1, FIFO replacing 1143 of 2293 retained entries) reaching only 0.367 on the shifted map. To tell whether the W2b revision rule must invalidate the whole contradicted retained set rather than replace it FIFO, one extra report-only cell runs on seeds 721 and 722 after the five registered seeds, as a separate process (`probes/n5/n5_probe_explore.py`, identical to `n5_probe.py` except the added mode): **`shift_oraclefull`** -- at the shift, all on-policy records are flushed AND the whole pre-shift retained set is quarantined (removed from replay); then N = 2400 babbling steps at g = 1 (a full re-development epoch, the size of the original babbling phase) with 8 updates per step. Readout: the post-shift bar on TE_shift and gate (a) on TE_orig. It does not enter the verdict.

## 4. Results (seeds 721-725, all five complete; `probes/n5/results/N5_s72{1..5}.{json,log}`, summary `probes/n5/summarize_n5.py`)

Per seed: disc4_h1 / k on the shifted map (TE_shift) and the original map (TE_orig), retention on the original map, and the gate's behaviour. Bar = disc4_h1 >= 0.47 and k = 10. k = 10 in every row, so the bar is decided by disc4 throughout.

| seed | pre-shift TE_orig (bar) | cell | TE_shift | TE_orig | retention | bouts / unfreeze events (first coincidence step) | replaced / flushed |
|---|---|---|---|---|---|---|---|
| 721 | **0.537 (yes)** | shift_gated | 0.223 | 0.533 | 1.26 | 3 / 2 (360) | 572 / 1761 |
| | | shift_clamped | 0.170 | 0.540 | 1.30 | 0 | 0 |
| | | noshift_gated | 0.203 | **0.563** | **1.43** | 3 / 3 (472) | 573 / 1759 |
| | | noshift_clamped | 0.177 | 0.540 | 1.30 | 0 | 0 |
| | | shift_oracle | 0.367 | 0.433 | 0.70 | 6 / 1 (0) | 1143 / 1192 |
| 722 | **0.470 (yes)** | shift_gated | 0.240 | 0.517 | 1.19 | 4 / 2 (33) | 765 / 1214 |
| | | shift_clamped | 0.230 | 0.517 | 1.19 | 0 | 0 |
| | | noshift_gated | 0.203 | **0.513** | **1.17** | 2 / 2 (590) | 252 / 2089 |
| | | noshift_clamped | 0.223 | 0.527 | 1.24 | 0 | 0 |
| | | shift_oracle | 0.393 | 0.400 | 0.54 | 6 / 1 (0) | 1140 / 1182 |
| 723 | 0.413 (no) | shift_gated | 0.320 | 0.437 | 1.34 | 3 / 1 (599) | 573 / 1790 |
| | | shift_clamped | 0.237 | 0.483 | 1.68 | 0 | 0 |
| | | noshift_gated | 0.220 | 0.463 | 1.54 | 2 / 2 (587) | 199 / 2166 |
| | | noshift_clamped | 0.243 | 0.480 | 1.66 | 0 | 0 |
| | | shift_oracle | 0.353 | 0.407 | 1.12 | 6 / 1 (0) | 1145 / 1194 |
| 724 | 0.443 (no) | shift_gated | 0.213 | 0.427 | 1.33 | 6 / 3 (17) | 950 / 1388 |
| | | shift_clamped | 0.200 | 0.413 | 1.17 | 0 | 0 |
| | | noshift_gated | 0.173 | 0.427 | 1.33 | 3 / 3 (162) | 573 / 1661 |
| | | noshift_clamped | 0.213 | 0.427 | 1.33 | 0 | 0 |
| | | shift_oracle | 0.253 | 0.393 | 0.92 | 6 / 1 (0) | 1144 / 1194 |
| 725 | 0.460 (no) | shift_gated | 0.223 | 0.477 | 1.47 | 4 / 3 (274) | 747 / 1575 |
| | | shift_clamped | 0.190 | 0.477 | 1.47 | 0 | 0 |
| | | noshift_gated | 0.180 | 0.457 | 1.27 | 1 / 1 (104) | 190 / 1262 |
| | | noshift_clamped | 0.177 | 0.480 | 1.50 | 0 | 0 |
| | | shift_oracle | 0.320 | 0.427 | 0.97 | 6 / 1 (0) | 1139 / 1173 |

Guard (d) PASS in every cell (closed in the shared phase, before the snapshot). Rollout (e) bounded in 24/25 cells (s723 `shift_oracle` fails it).

**Verdict tally (pre-registered):** pre-shift bar 2/5 (721, 722; s725 missed by 0.010, s724 by 0.027, s723 by 0.057) -> **rule 1 fires: CANNOT_DETERMINE.** For the record: clamped re-learns 0/5 (the other CANNOT_DETERMINE limb does not fire); shift half 0/5; no-shift half 2/5 (fails exactly on the 3 seeds that never had the bar; retention >= 0.5 on 5/5, 1.17-1.54).

### 4.1 What the result says, by half

- **Shift half fails on every seed, including the two evaluable ones -- so the pre-registered CANNOT_DETERMINE does not hide a PASS.** `shift_gated` never gets above 0.320 on the shifted map (0.213-0.320; chance 0.25) and keeps the OLD map (0.427-0.533) -- the same as `shift_clamped` (0.170-0.237 / 0.413-0.540).
- **(i) Detection: the gate does not see the shift.** The clean test of a detector is the clamped pair (identical g = 0.1, no unfreeze; only the env differs). Fraction of steps with the action-contrastive surprise above threshold, shift vs no-shift: 0.11 vs 0.29, 0.05 vs 0.14, 0.06 vs 0.06, 0.20 vs 0.16, 0.11 vs 0.05 (721-725): higher WITH the shift on 2/5. Mean on-policy z (ac): shift -0.12 / +0.03 / +0.03 / +0.21 / +0.15 vs no-shift +0.13 / -0.03 / -0.16 / +0.10 / -0.13. The report-only PE detector (the brief's example signal) never crosses its threshold in any cell of any seed (would-coincide 0 everywhere) and its mean on-policy z does not separate either. So in the gated cells the gate opened after the shift on 5/5 seeds but **also opened without a shift on 5/5 seeds** (1-3 spurious unfreeze events each, 190-573 retained entries replaced, 1262-2166 on-policy records flushed): it fires at a base rate, not at the shift.
- **(ii) Revision: even a perfect, sustained unfreeze does not re-learn the map in N = 1200.** `shift_oracle` (on-policy flushed at the shift, every step a babbling step at g = 1, ~1140 of ~2290 retained entries FIFO-replaced by new-map babble, 9600 updates) reaches 0.253-0.393 on the shifted map (0/5 at the bar) and loses the old one (0.393-0.433). With half the retained set still carrying the old map, the replay mix is contradictory. FIFO replacement at bout rate is too slow for a whole-map change at this dose.
- **No-shift half: no spurious destabilisation of the map, despite spurious unfreezes.** Where the bar existed before the adult phase (721, 722), `noshift_gated` kept it (0.563, 0.513) with retention 1.43 / 1.17, even after 2-3 spurious bouts. That is expected and weak evidence: a spurious re-babble on an unchanged map writes the same map back. The cost of the false alarms is the flushed on-policy working buffer (1262-2166 records per seed), not the map.
- **W3 gate robustness (side finding).** The W3 member protocol reached the L2R bar on 2/5 fresh seeds here (0.413-0.537) and missed on calibration seed 799 (0.453), against 4/5 on W3's seeds 106-110. Across these 9 seeds the bar (0.47) sits near the recipe's median, not its floor.

### 4.2 Why the surprise cannot see this shift (D1 reading, partly untested)

- Measured: neither statistic separates shift from no-shift on on-policy data, and the head's action discrimination on uniform data is only ~0.45-0.54 (chance 0.25). A one-step error can only register a re-mapped action to the extent the head's prediction depends on the action, and here that dependence is weak relative to state-to-state variation of the error.
- Not measured (hypothesis): the native policy is concentrated (W3: modal class 42-94% of steps) and presses into walls, where a blocked move produces the same next state under both maps, so much of the on-policy stream carries no information about the map at all. The probe did not log displacement per on-policy step; that is the check that would confirm it.

**Evidence domain: D1.** No consumer or behaviour reading.

### 4.3 Addendum result (exploratory, not verdict-bearing): wholesale revision does re-learn

`shift_oraclefull`, seed 721 only (`probes/n5/results/N5X_s721.{json,log}`): on-policy flushed and the whole pre-shift retained set (2293) quarantined at the shift, then 2400 babbling steps at g = 1 (19200 updates). **Shifted map 0.523 / k 10 -- meets the bar**; original map 0.193 / k 10 (below chance: the old map is fully overwritten, as it should be after a real re-map). Rollout bounded. So the revision half of W2b works when the contradicted retained set is invalidated wholesale and a full developmental babbling epoch refills it; FIFO replacement at bout rate (`shift_oracle`, 0.25-0.39) does not. One seed, not replicated: seed 722 was not run (time cap). The first attempt crashed at the final retained-error readout (index past the refilled set's length; `N5X_s721_crash1.log`); the readout was guarded and the seed re-run unchanged otherwise.

## 5. What this means for W2b (for the orchestrator)

- **W2b is not buildable as specified.** Its two halves were tested separately and only one has a working form:
  - **Detection / g signal: none found.** The member's own one-step error does not see an action-map shift, raw (the brief's example) or action-contrastive, on 5/5 seeds; both fire at base rates unrelated to the shift. The native candidate (E3 `last_instantaneous_pe`, `e3_selector.py:1036-1052`) is the same quantity as the raw PE detector here and has no native ACh/MECH-398 consumer on `1b013d6`.
  - **Revision: wholesale, not FIFO.** Quarantine the pre-onset retained set and re-babble a full epoch (0.523 on s721); partial FIFO replacement leaves a contradictory replay mix (0/5 at the bar).
- **What g should be driven by (proposal, untested):** a detector chosen by the clamped-pair separation test before any build. The obvious candidate is **active probing** -- short periodic W2a babbling probes (all classes, not wall-concentrated) scored action-contrastively against the retained-set baseline -- because the on-policy stream is the part that carries no map information. Probe N5b should test that detector (clamped pair, shift vs none) and the wholesale revision rule together, on seeds whose pre-shift state meets the W3 bar.
- **Decision for the user / orchestrator (not taken here):** whether W6's integrated preset waits for W2b, or ships with the retained set FROZEN (W3's state, which N5 shows is stable under no shift, with no unfreeze path).
