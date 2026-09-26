# H0 probe: is the episode reset a hidden regime controller? (dynamic-control audit H0)

- **Status: PRE-REGISTRATION (committed before the scored runs).** Results are appended below this section in a later commit; nothing in this section is edited after the scored runs start.
- **Written:** 2026-09-26T13:41Z. Session `bt0926-h0` (orchestrator `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-h0-reset-hidden-controller`. Probe only: no `ree_core` edit, nothing queued, no chip, no `claims.yaml` edit, no plan edit.
- **Spec:** H0 in `dynamic_control_audit_20260926.md` (e3cafebab38) and DRAFT-DCD-1's `what_would_answer` there. R1 = `REEAgent.reset()` (`dynamic_control_audit_imposed_regimes_20260926.md`, 26eeccf71d8). Harness reused from `probes/modetrace/modetrace_probe.py` (`mode_switch_cea_mechanism_trace_20260925.md`, e2bbd2a98e).
- **Code under test:** ree-v3 `origin/main` @ **`436a988742`**, private detached worktree `.scratch/wt-h0`. Harness-side only.
- **Probe script:** `probes/h0/h0_reset_probe.py` (committed with the results; the scratch copy is `.scratch/breakthrough-20260924/h0/`).

## 1. Ecology (fixed)

- The modetrace **A1** configuration: `use_dacc=True`, `salience_affinity_input_cap=2.0`, `use_external_task_drive` OFF, plus the EXP-0787 probe flags (harm stream + affective harm stream, amygdala/CeA, broadcast override, salience coordinator, **PAG freeze gate**, closure operator, lateral PFC, habenula de-commit), `alpha_world=0.9`.
- **All four EMA reset-init knobs ON** (`use_zworld/zself/shared/zharm_ema_reset_init`; campaign convention GFLAG-0559; precondition P3).
- Untrained agent, `world_dim = self_dim = 32` (deployed values), driven by `experiments/_harness.StepHarness` (`train_mode=True`). `CausalGridWorldV2(size=10, num_hazards=3, num_resources=3, max_episode_steps=100)`; one external hazard injected at every step `t % 30 == 15` (as modetrace). Mac CPU, `torch.set_num_threads(2)`.

## 2. Pre-registered parameters

| item | value |
|---|---|
| seeds | **31, 32, 33** (fresh: modetrace used 11-13; the plumbing pilot used 99) |
| ticks per life | **600 env steps** per (arm, seed); one agent object for the whole run, weights never reset |
| episode length | `max_episode_steps = 100`; an episode also ends on death (health <= 0), which the untrained agent reaches in ~20-40 steps |
| k (endogenous-exit window) | **k = 8 env steps** (the campaign's post-reset exclusion window, GFLAG-0560). An exit is *endogenous* only if it is more than 8 steps from every env boundary (and, in arm C, from every forced controller reset) |
| arm C rate | A's measured env-boundary rate for the same seed (boundaries / 600), drawn per non-boundary step from an independent RNG (`random.Random(10000 + seed)`), so uncorrelated with env boundaries by construction |

## 3. Arms

- **A (imposed):** `agent.reset()` at every env boundary, unchanged.
- **B (body-only):** at every env boundary the harness snapshots the agent's plain state (a generic walk over every `ree_core` sub-object's non-parameter attributes and buffers), calls `agent.reset()`, diffs, and **restores every changed path classified `controller`**. The env layout and the body still reset. Classification rules (in the script, `classify()`):
  - `body` (still reset in B): the latent state `_current_latent`, `latent_stack`, `e1` hidden state, `clock`, `theta_buffer`, committed trajectories/candidates (`e3._committed_trajectory`, `_closure_committed_*`, `_persistent_committed_trajectory`, `_committed_candidates`, `beta_gate._held_policy_state`), the last selection result, step counters, `_harm_this_episode`, `_harm_replay_buffer`, `_last_action`, and every previous-tick cache (`*_prev*`). These are bound to the old body position or old layout.
  - `cache` (not restored): per-tick output caches rewritten every tick (`_dacc_last_*`, `_salience_last_tick`, any `_last_output`).
  - `diagnostic` (not restored): MECH-287 per-episode instrument bookkeeping (`pag_freeze_gate._episode_*`).
  - `memory` (not restored): boundary-time memory writes (sleep loop, exploration buffer, residue, policy chunking, MECH-287 rows).
  - `controller`: everything else `reset()` changed.
- **Exactly what B preserves** (the realized `controller` set in this config, from the pilot; the scored runs report the realized set per run and any deviation is stated): 26 state paths in 9 objects (the union over the pilot's A and B runs) --
  - `salience` (SD-032a coordinator): `_operating_mode`, `_input_signals`, `_current_mode`, `_last_trigger`;
  - `dacc` (SD-032b; reached as `closure_operator.dacc`, the same object as `agent.dacc`): `_pe_ema`, `_action_history`, `_last_pe_unsaturated`;
  - `lateral_pfc` (reached as `closure_operator.lateral_pfc`): buffer `rule_state`, `_last_effective_eta`, `_last_gate`; `closure_operator._last_rule_state`;
  - `beta_gate`: `_beta_elevated`, `_committed_run_length`;
  - `pag_freeze_gate`: `_freeze_active`, `_ticks_in_freeze`, `_duration_above_threshold`;
  - `bla`: `_last_arousal_tag`, `_last_encoding_gain`, `_window_onset_step`, `_window_peak_gain`; `cea._last_low_freq_mag`;
  - `broadcast_override`: `_override_signal`, `_threat_window`, `_last_raw`, `_last_sustained`, `_n_ticks`;
  - plus `_ncl_mech091_fired` when it has fired.
  - **Subset statement:** DC-B counts ~55 states in `reset()` (`agent.py:4101-4552`). Most belong to modules that are OFF (`None`) in this config and so hold no state. B covers **every** `reset()`-changed controller path in this config, not a hand-picked subset. Named exclusions are the body/cache/diagnostic/memory classes above. `serotonin` and agent `_pe_ema` were not changed by `reset()` in the pilot (no state moved), so they are not in the set.
- **C (wrong-reason):** B, plus a **full controller reset** at random steps: `agent.reset()` then restore of every non-`controller` path (the inverse of B: controllers cleared, body/env untouched).
- **Secondary, conditional (`Bonly:<x>`):** A, but only `controller` paths through object `x` are restored. Run for `x = salience` and `x = dacc` **only if** B differs from A beyond the band on the mode regime (sec 5), to attribute the effect. Not a verdict input.

## 4. Readouts (per arm, per seed)

- **R-mode (primary regime):** coordinator register `current_mode != external_task` (the absorbing regime modetrace found). Occupancy (fraction of env steps), native entries/exits, exits at a reset call, exits within k of an env boundary, endogenous exits, native entries within k *after* a boundary or forced reset, native switches per episode and per life.
- **R-commit (within-probe control):** E3 `committed_now` (`running_variance < bar`). rv persists across `reset()` in every arm, so the prediction is **no A/B difference** (|occupancy difference| <= 0.10). A larger difference means the harness manipulation itself perturbs the loop.
- **R-freeze (conditional leg):** PAG `_freeze_active`. **Included in the verdict only if the harm stack's P1 holds** (ARC-155 P1: raw `||z_harm_a||` separates hazard-adjacent (Manhattan d <= 1) from far (d >= 2) states at **d' >= +0.5**, hazard-adjacent higher), measured in arm A on >= 2 of 3 seeds. Otherwise the freeze leg is reported as telemetry and **omitted from the verdict**. (The pilot measured d' of -0.8 to -1.0 on seed 99, i.e. the wrong sign; stated here so the reader knows the leg is likely to be omitted.)
- **Outcomes:** harm per tick, benefit per tick, mean episode length, deaths (the "does a controller benefit from persisting" readout, DRAFT-DCD-1 input; not a verdict).
- **Arm C:** exits and entries at forced clears, split by whether the clear lands within k of a world change (env boundary or hazard injection).

## 5. Verdict rule (R-mode; R-freeze too if its P1 holds)

- **Probe precondition P1 (non-degeneracy):** the regime is entered at least once per life under A (>= 1 native entry in 600 steps) on the seed. A seed failing it is CANNOT_DETERMINE for that regime.
- **Noise band.** B is *within the band of A* on a seed when both hold: |occ_B - occ_A| <= 0.10, and |exits_B - exits_A| <= max(3, 0.5 x exits_A) (exits per 600-step life, all exits counted).
- **SUPPORTED** (the H0 prediction: B absorbs): on >= 2/3 seeds, occ_B > occ_A + 0.10 **and** B has <= 1 exit per life (near zero), while >= 80% of A's exits occur at a reset call.
- **FALSIFIED:** on >= 2/3 seeds B is within the band of A (the regime enters and exits on its own at A's rates; the reset is bookkeeping for it).
- **MIXED:** anything else, reported per regime and with the mechanism named. One outcome is flagged in advance because the pilot (seed 99, 120-300 steps, not scored) showed it: under B the register **never entered** the regime (occupancy 0.00 vs 0.06-0.21 in A), i.e. the reset may drive the regime's *entries* as well as its exits. That outcome (occ_B < occ_A - 0.10 with native entries collapsing) means the boundary IS a hidden regime controller but the "stays absorbed" prediction is FALSIFIED; it is scored **MIXED** with that statement, not SUPPORTED.
- **CANNOT_DETERMINE:** P1 fails on >= 2/3 seeds, or the manipulation check fails (B leaves any `controller` path changed by `reset()` unrestored, i.e. `restore_skipped` non-empty for controller paths).
- n = 3 seeds stands in for DRAFT-DCD-1's ">= 4/5"; the verdict is stated as n = 3.

## 6. Disclosed before scoring

- A plumbing pilot on seed 99 (120-300 steps, arms A/B/C) was run to fix the snapshot/restore code and to enumerate the realized preserved set (sec 3). Its numbers are not scored. It showed: under A, all R-mode exits occurred at the reset call; under B, no R-mode entry at all; R-commit occupancy 0.97 in every arm; the PAG freeze gate active 5-9% of steps with native releases in every arm; z_harm_a d' negative.
- Domain reachable: **D2** (reset scope changes native consumers: the mode register, freeze gate, commit gate). D3 only if outcomes move.

---

# RESULTS (appended after the scored runs; sections 1-6 above are unchanged from the pre-registration commit 4d49c2c40a)

- **Written:** 2026-09-26T16:05Z. Code ree-v3 `436a988742`. Script `probes/h0/h0_reset_probe.py`; verdict arithmetic `probes/h0/verdict.py`; raw rows `probes/h0/results/main.jsonl` (+ `main300.jsonl`, `pilot*.jsonl`).
- **Evidence domain reached: D2** for the mode register (removing the reset's controller clears changes what the native coordinator does, in the predicted direction on exits). Not D3: outcome differences are small and unattributed (sec R5).

## R0. Plain-language result

The episode reset is the **only** thing that ever takes the salience coordinator out of its "internal_planning" mode. Across all 37 exits in the imposed arm (3 seeds), every one happened at the reset call itself; there were zero exits anywhere else in any arm. With the reset's controller-clearing removed (body-only reset), the register switched once per *life* and never left, as H0 predicted. But the exits the reset produces are mostly one-step blips: on two of three seeds the coordinator re-entered internal_planning on the very next tick, so the time spent in the regime barely changed (+0.03, +0.01). Only on the seed where re-entry was slow (seed 33) did persistence raise occupancy a lot (+0.45). The PAG freeze gate, by contrast, exits on its own: the reset did no exit work for it. The commit gate (the control) was identical in every arm.

**Verdict (pre-registered rule, n = 3): MIXED.** Mode regime: MIXED on seeds 31 and 32 (exits collapse to zero, occupancy within band), SUPPORTED on seed 33. Freeze leg: omitted from the verdict (its P1 failed, R3); as telemetry it is FALSIFIED-shaped on 3/3 (reset is bookkeeping for it). Commit control: no A/B difference on 3/3 (manipulation check passes).

## R1. Deviations from the pre-registration (all stated before the affected data were read)

1. **Seeds 32 and 33 ran 300 steps, not 600.** The Mac load average was 50-72 on 8 cores during the first holds (unlocked `sdc_latch_driver_probe.py` x4, `v3_exq_1109`, `cg_probe.py` from other sessions). A31 took 1294 s wall and B31 1885 s for 600 steps. To finish within the time cap, the remaining A/B runs were cut to 300 steps before any seed-32/33 result existed. Seed 31 is at the pre-registered 600. The band rule is applied unchanged; its absolute exit floor (3) is therefore more lenient at 300 steps. The 300-step rows are in `main300.jsonl`; `verdict.py` reads the union.
2. **Lock-hold cap.** A31's single hold ran 21.8 min (over the 15-min cap) before I switched drivers. Every later run used a driver that SIGSTOPs the probe at 14 min, releases the lock, pauses >= 45 s, re-takes and SIGCONTs (`probes/h0/run_main3.sh`, `run_batch.sh`). No lock was ever broken; every release was verified.
3. **Preserved set.** The realized arm-B set over the scored runs is 27 paths, not the pilot's 26: `closure_operator._stable_tick_count` was also changed by `reset()` in the scored runs (classified `controller` by the unchanged rule, so preserved); `salience._last_trigger` did not change in the scored B runs. `restore_skipped` was empty in every run (manipulation check passes). Two large containers were fingerprint-skipped, not copied: `_e2_transition_buffer` and `closure_operator.residue._harm_history` (memory, not controller; `reset()` does not clear residue, `agent.py:4102`).
4. **Secondary `Bonly:<x>` arms: not run.** The pre-registered trigger fired (B's exits left the band on 2/3 seeds), but the attribution is available at D0 and the time cap did not allow it: the only exit route is `SalienceCoordinator.reset()` writing `self._current_mode = "external_task"` unconditionally (`ree_core/cingulate/salience_coordinator.py:485`), called from `REEAgent.reset()` (`ree_core/agent.py:4181`). The native path to external_task (`:693`, `current_mode = soft_argmax` under the three trigger conditions) never fired in any arm.
5. **Arm C (wrong-reason control): NOT RUN in the scored set.** After the core A/B runs the Mac probe lock was held continuously by other workers (bt0926-cgdisc, bt0926-dch2) and C_31 never got a hold before the ~3 h cap. Arm C ran only in the unscored pilot (seed 99). Its question is answered at D0 instead (R4).

## R2. Mode regime (primary): per seed

| seed | steps | occ A | occ B | d | exits A (at reset call) | exits B | endogenous exits A / B | native entries A (within k after a boundary) / B | switches per episode A / B | switches per life A / B | call |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 31 | 600 | 0.862 | 0.895 | +0.033 | 27 (27/27) | 0 | 0 / 0 | 28 (27) / 1 | 0.875 / 0.028 | 28 / 1 | MIXED |
| 32 | 300 | 0.763 | 0.770 | +0.007 | 7 (7/7) | 0 | 0 / 0 | 8 (8) / 1 | 0.800 / 0.100 | 8 / 1 | MIXED |
| 33 | 300 | 0.233 | 0.683 | +0.450 | 3 (3/3) | 0 | 0 / 0 | 3 (1) / 1 | 0.600 / 0.200 | 3 / 1 | SUPPORTED |

Reading it:

- **P1 (regime entered at least once per life under A): holds 3/3.**
- **The reset is the sole exit (3/3, 37/37 exits).** Endogenous exits (more than k = 8 steps from any boundary) are 0 in both arms on every seed. The within-life reversal count of zero that modetrace reported (sec 1b, A1) is reproduced; here it is shown to be the whole story: without the reset nothing exits.
- **"One switch per life" under B (3/3).** B's register entered internal_planning once (at t = 63 / 69 / 95) and stayed for the rest of the life. `n_switches == n_episodes` (modetrace sec 1a) is the reset's signature; under B it becomes 1 per life.
- **Why occupancy barely moves on seeds 31/32.** After the reset forces external_task, the next coordinator tick re-enters internal_planning: 27/28 and 8/8 of A's entries fall within k steps after a boundary (seed 31 exits at 78, 91, 120, ... are followed by entries at 79, 92, 122, ...). The inputs that put the register in internal_planning (the dACC PE alarm coupled to its own affinity, modetrace sec 1d) are still present after the body reset, so the forced external_task visit lasts about one tick. On seed 33 the post-reset re-entry was slow (2 of 3 entries more than k after a boundary; long episodes, 4 boundaries in 300 steps), so persistence added 0.45 occupancy.
- **So the reset's control work on this regime is real but mostly cosmetic.** It supplies every exit, but in two of three lives the exits are one-tick excursions that do not return the organism to external_task in any lasting way. The imposed regime's apparent "recoverability" (a switch per episode) is an artefact of counting, not of recovery.
- **The pilot's alternative (reset drives entries too) did not recur.** On pilot seed 99 (not scored) B never entered the regime in 120-300 steps. In the scored runs B entered once on every seed, at about the same step as A's first entry (63 vs 70, 69 vs 68, 95 vs 95). The first entry is native, not reset-driven.

## R3. Freeze leg (omitted from the verdict; telemetry)

- **Harm-stack P1 (ARC-155: `||z_harm_a||` hazard-adjacent vs far, d' >= +0.5 in arm A on >= 2/3 seeds): FAILED.** d' = -0.185 (s31), -0.198 (s32), +0.825 (s33): 1/3. The freeze leg is omitted from the verdict as pre-registered.
- **Telemetry, for the record:** the PAG gate was active 6-24% of steps in this untrained config and exited on its own. Of 142 / 49 / 17 freeze exits in A, only 13 / 4 / 2 were at the reset call. B was within band on 3/3 (occupancy +0.007 / +0.010 / +0.010; exits 145 / 51 / 20). For this gate in this config the reset is bookkeeping: its exit (`freeze_active(t) = ... AND z_harm_a(t) > exit_threshold`, `ree_core/pag/freeze_gate.py:15-18`) reads a quantity that keeps moving during a freeze in an untrained agent. This does **not** contradict ARC-156's freeze instance (V3-EXQ-1106/1107, trained agents, `z_harm_a` constant during the freeze): the ARC-156 condition, an exit input that the regime starves, is absent here because the untrained `z_harm_a` is not constant.

## R4. Commit control and arm C

- **Commit gate (within-probe control): identical in every arm, 3/3** (occupancy 0.993 / 0.987 / 0.987 in A and B; 0 exits). E3 running variance is not cleared by `reset()`, so the body-only manipulation does not perturb what the reset does not touch. Manipulation check passes. (This is also a reminder that the commit gate is absorbing in its own right: rv < 0.40 from about the first tick and never leaves, GFLAG-0346's shape, with or without the reset.)
- **Arm C: not scored (R1.5); answered at D0 plus pilot.** The question was whether exits come from clearing per se or from clearing at a world change. The code answers it: `SalienceCoordinator.reset()` sets `_current_mode = "external_task"` unconditionally (`salience_coordinator.py:485`), with no input that could distinguish a world change. Any clear, at any time, produces an exit. The unscored pilot cannot discriminate: on seed 99 (120 steps) its single C exit came from a forced clear at t = 109 that happened to fall within k of an env boundary, and the register re-entered at t = 110. So, at D0 only, the regime's exits come from clearing per se. The confirming half of DRAFT-DCD-1 ("C restores A's exits only when its resets land near world changes") is therefore not met, by construction.

## R5. Which controllers benefit from persisting (DRAFT-DCD-1 input; not a verdict)

| seed | harm/tick A / B | benefit/tick A / B | mean episode length A / B |
|---|---|---|---|
| 31 | 0.0608 / 0.0692 | 0.0069 / 0.0047 | 18.8 / 16.7 |
| 32 | 0.0380 / 0.0369 | 0.0046 / 0.0035 | 30.0 / 30.0 |
| 33 | 0.0128 / 0.0131 | 0.0023 / 0.0011 | 60.0 / 60.0 |

- **No controller showed a benefit from persisting.** Benefit per tick was lower under B on 3/3 seeds, but the amounts are a handful of resource contacts per life, harm is mixed, and episode counts are identical on seeds 32/33. I treat this as **no detectable behavioural effect** (D1 at most), not as harm from persistence. It is consistent with modetrace sec 1c (the mode register has no behavioural consumer). The persisted dACC action history (MECH-260 suppression) is the one preserved state with a direct path to candidate scores, and it could be the source of any real difference; this was not attributed (R1.4).
- For DRAFT-DCD-1 this means: in this config, persisting the controllers does not make a regime *recover*; it only removes a spurious exit. A persistence policy therefore cannot be motivated by these controllers' behaviour here. What it would buy is honest telemetry (one switch per life instead of one per episode) and the removal of a world-changed hint (DC-B R1) that this regime never used.

## R6. What this changes (recommendations only; nothing applied)

- **H0's falsifier did not fire, and its confirming pattern held only on exits.** The pre-registered verdict is **MIXED**: the reset is the hidden controller of this regime's exits (3/3, D2), but because the regime re-enters immediately, the exits carry almost no control work (occupancy in band on 2/3). A regime that looks recoverable in multi-episode drivers is, for the mode register, not recoverable at all; the drivers' switch counts measure the reset.
- **For ARC-156's instance list:** the mode register's absorbing exit is a starvation instance (no native exit in any arm), and the reset is its only terminator. The freeze gate is **not** an ARC-156 instance in an untrained agent in this config (it exits natively); ARC-156's freeze instance remains the trained-agent case (1106/1107).
- **For A1 (and any multi-episode driver that reads mode switches):** switch counts per episode are a reset artefact; count switches per life, and exclude the tick after each boundary.
- **Single next action (not taken):** the same A/B contrast on a trained agent (935a curriculum) with `use_external_task_drive` ON and OFF, reading within-life reversals. That tells whether any native exit survives training, which is the D-question modetrace sec 3 already assigns to the mode-governance-engagement row.

## R7. Uncertainty

- n = 3 seeds, untrained agents, short lives (episodes of 17-60 steps end mostly in death). Seeds 32/33 at 300 steps.
- The first native entry of B coincided with A's first entry on every seed, so the pilot's "B never enters" is a seed-99, short-run observation, not a scored result.
- The body/controller split is a rule, not a law: the latent state, E1 hidden state and committed trajectories were treated as body and reset in B. A different split (for example persisting the latent EMA) could change the dACC input after a boundary and so the re-entry latency.
