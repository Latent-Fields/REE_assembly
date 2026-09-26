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
