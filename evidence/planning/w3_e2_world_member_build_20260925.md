# W3 build: `E2WorldMember` on `integration/coupled-loop-repair` (default-OFF), FROZEN retained babbling state, A1 O15 wiring

- **Status: BUILT on the branch, member gate PASS (D1).** Session `bt0925-w3` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260925-coupled-w3-e2world-build`. Written 2026-09-25.
- **Code:** ree-v3 `integration/coupled-loop-repair` @ `042895a` (W3 commit on top of the branch rebased onto `origin/main` `2ea0e3c`: W1-alt ASP `645fd54`, W1 codec `b3f30a8`). Nothing on `main` changed. All knobs default OFF.
- **Plan of record:** `coupled_loop_repair_campaign_plan.md` sec 3 W3 (GFLAG-0485 leg (i)); A1 draft `coupled_a1_preregistration_draft_20260925.md` sec 5.4 (E7 / O7) and sec 6.7 (O15).
- **Evidence domain: D1.** The head discriminates actions on a held-out set and its gradient reaches and moves the group. Nothing here shows that E3 or behaviour changes (D2/D3); that is N3 / W4 / A1.

## 1. Premises re-measured before building

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | T1 and W2a are on main, not on the branch (brief) | branch was `e4dc1a5` on base `21c86cb`; main `2ea0e3c` carries T1 `d9a865e` + W2a `2ea0e3c` | holds. Rebased the branch onto main (2 conflicts, `waking_trainer.py` + `config.py`, resolved keep-both). ASP + W1 codec + trainer/T1/W2a contracts after the rebase: **85 passed, 2 xfailed** (the ASP-R strict xfails already recorded) |
| P2 | "`E2WorldMember`, stepping the native `compute_e2_world_loss`" (plan W3; design row 4) | `compute_e2_world_loss` (agent.py) is SD-056 **InfoNCE** over the agent's own `_world_experience_buffer`. The L2R bar it is gated on was measured with **single-step MSE** (`babble_probe.py` `train_head`, the tier-1 recipe). On the fixed contract dataset the InfoNCE objective through the same member gives disc4_h1 0.407 / 0.407 and **k = 0** on 2/2 seeds (MSE: 0.673 / 0.653, k = 10) | **corrected.** Default objective = MSE (`waking_trainer_e2_world_objective="mse"`); `"infonce"` is kept as a knob. The native loss cannot be called unchanged anyway: its buffer has neither babbling nor raw obs |
| P3 | "stored as raw obs, re-encoded at replay" (plan P8) | `sense()` is stateful: `z_world = alpha * new + (1 - alpha) * prev` (stack.py SD-008) plus the SD-007 prev-action input. Re-encoding one raw obs from a fresh state is **not** the live latent | handled: each record stores a warm-up window (auto `W = ceil(log 1e-4 / log(1 - alpha_world))`: 26 at the from_dims default 0.3, 4 at 0.9) and re-encodes from `latent_stack.init_state`, exactly as `sense` after `reset`. Measured: max abs diff to the live z_world 3e-8 at episode-start windows, <= 1e-3 truncated (contract W3-08) |
| P4 | W2a has no consumer yet (brief) | holds (`git grep` on 2ea0e3c: nothing calls `StructuredBabbler`) | this build is its consumer: a driver executes `agent.structured_babbler.next_action()` with `record_executed_action`, after `waking_trainer.set_e2_world_source("babble")` |
| P5 | A1 O7 "W3 buffer format" open | A1 sec 5.4 E7 draft: store the **executed action as fed to E2**; plan: raw obs re-encoded (P8) | **decided, the stated defaults:** raw obs re-encoded at replay (so the encoder member W6a cannot stale the buffer) and `agent._last_action` as fed to E2 (one-hot under ASP, the bounded decode under the codec). Both variants get the same format by construction |

## 2. What was built (branch only; `ree_core/**` + contracts)

- **`E2WorldMember`** (`ree_core/utils/waking_trainer.py`), registered when `waking_trainer_enabled` and `waking_trainer_e2_world_enabled` are both True.
  - Group: `e2.world_transition` + `e2.world_action_encoder` (the tensors `world_forward` reads). Guard-armed like every member.
  - **Raw capture:** `REEAgent.sense` hands its raw inputs to `WakingTrainer.on_sense` (one guarded call; `None` trainer at defaults means no call). `observe` (from `update_residue`) completes the previous tick's pending transition, so a record is (obs_{t-1}, a_{t-1}, obs_t) with its warm-up window, the SD-007 prev-actions, the live z pair, source and the member's waking-step index. No pair crosses `on_env_reset`.
  - **Buffers:** on-policy deque (`waking_trainer_buffer_max`); **retained set: append-only list, cap `retained_max` (5000), FROZEN** (no on-policy data ever evicts or overwrites it; over-cap candidates are counted in `retained_dropped`, not stored). W2b's UNFROZEN state is not built.
  - **Mix:** a pure-retained batch while the on-policy buffer holds less than a batch (the babbling epoch), then `round(B * 0.25)` retained + the rest on-policy; pure on-policy with no retained set. Realised counts in `n_drawn_retained` / `n_drawn_on_policy`.
  - **Re-encode:** batched by window length, under `no_grad` (no gradient reaches the encoder: guard G5 reports no leak), through the CURRENT `body/world_obs_encoder -> latent_stack.encode`. Each record caches its z against the `_version` of every read-path tensor, so a frozen encoder costs one encode per record and any optimizer step / `load_state_dict` on the read path forces a fresh encode (contract W3-08c). Disabled when `volatility_signal_dim > 0` (a non-parameter input). `replay_latent="stored"` replays the live z instead (the N2 stored-z arm).
  - **Loss:** MSE of `world_forward` (default) or native InfoNCE; per-member `grad_clip` (1.0, L2R recipe) and `updates_per_step` (replay ratio) are trainer hooks that no other member defines.
- **A1 O15 wiring:** (i) `export_retained()` returns the FROZEN set in insertion order, each record with its `step` index and `source` (the INT-v log); (ii) `append_external(records)` stores another arm's transitions now, `schedule_external(records)` releases each when this member's waking-step counter reaches its logged `step` (INT-v-BABBLE-DATA). Both are harness-callable; no further branch hook is needed.
- **Knobs (3 sites: dataclass, `from_dims`, `PROBED`):** `waking_trainer_e2_world_enabled` (False), `_lr` 3e-4, `_batch_size` 32, `_replay_frac` 0.25, `_retained_max` 5000, `_reencode_window` 0 (auto), `_replay_latent` "reencode", `_objective` "mse", `_grad_clip` 1.0, `_updates_per_step` 1.

## 3. Member gate: the L2R bar re-measured on this member (plan W3 (a)-(e))

**Protocol** (`probes/w3/w3_l2r_member_probe.py`): the babbling probe's own env, agent build (`build_B`, world_dim 32, alpha_world 0.3), held-out test set (3000 uniform-random {0..3} steps, k = 120..134) and `evaluate()`, seeds 106-110. The member does everything the probe's hand-rolled loop did: W2a babbling (5 classes incl. stay, run length {1..4}) over Phase-0 episodes k = 0..11 into the FROZEN set (2282-2293 retained), 3000 member updates, then 1200 native closed-loop `StepHarness` steps (k = 50..55) with 8 member updates per step (9600; probe 9000) at the 25% retained mix, re-encoded. **SHUF twin:** retained babbling actions relabelled by a FIXED class permutation (plan Decision log 14:19Z item 3). **B0** is the probe's published on-policy head; it is valid here because this run's INIT disc equals the published INIT disc exactly on 5/5 seeds (same encoder, same test set). Ran on a snapshot of origin/main `2ea0e3c` + the W3 diff; seed 106 re-run on the final branch tree reproduces 0.5233 exactly (ASP / codec OFF).

| seed | stratum | pre disc4 / k | **post disc4 / k** | disc5 | retention | SHUF post disc4 / k | t30/t0 | late step growth (median / max) |
|---|---|---|---|---|---|---|---|---|
| 106 | benign | 0.433 / 9 | **0.523 / 10** | 0.463 | 1.71 | 0.130 / 10 | 1.09 | 1.001 / 1.027 |
| 107 | trapped | 0.443 / 8 | **0.477 / 10** | 0.403 | 1.24 | 0.143 / 10 | 1.10 | 1.001 / 1.011 |
| 108 | trapped | 0.463 / 7 | **0.460 / 10** | 0.437 | 0.955 | 0.190 / 10 | 1.06 | 1.004 / 1.013 |
| 109 | trapped | 0.440 / 7 | **0.513 / 10** | 0.443 | 1.58 | 0.127 / 9 | 1.26 | 1.012 / 1.047 |
| 110 | trapped | 0.473 / 9 | **0.510 / 10** | 0.480 | 1.41 | 0.147 / 9 | 1.20 | 1.012 / 1.028 |

| gate | rule | result |
|---|---|---|
| (a) | disc4_h1 >= 0.47 and k = 10 on >= 4/5 | **PASS 4/5** (s108 0.460 misses by 0.010) |
| (b) | retention >= 0.5 on >= 4/5 | **PASS 5/5** (0.96-1.71; L2R 1.31-1.53) |
| (c) | SHUF does not reach (a) | **PASS** (0/5; 0.127-0.190, below chance: the relabelled replay teaches the wrong map) |
| (d) | guard PASS | **PASS** 10/10 runs, no leak |
| (e) | rollout t30 bounded, no x1.2/step growth | **PASS** (t30/t0 1.06-1.26; late per-step growth <= 1.047) |
| FROZEN | retained set byte-identical after the whole post phase | 10/10 |

- Compared with the probe's L2R (0.473-0.553, k = 10 on 5/5): the member is ~0.03 lower on the median. The likely reason is that 1/5 of W2a's babbling goes to the stay class, which disc4 does not score (the probe babbled over {0..3} only). This is stated, not tested.
- **Reported (plan):** E3 `_running_variance` at run end 4e-6 to 1.4e-4 (real arms). The commit rate could not be read: `e3._committed_trajectory` stays `None` in this build, so the column reads 0.00 and is **not** evidence about ARC-016. The consumer reading belongs to N3 / W4.
- **Behaviour (not a gate):** post-phase actions stay concentrated (modal class 42-94% of steps; >= 81% on 3/5 seeds), as expected with E3's valuation at chance until W5 (N3-pre).

## 4. Contracts (`tests/contracts/test_w3_e2_world_member.py`, 19)

W3-01 OFF: nothing constructed, the sense hook is never reached, an ON trainer without the knob keeps the T1 set. W3-02: recording raw obs with a never-firing cadence is byte-identical to OFF over 3 episodes. W3-03: every update, re-encode included, is RNG-neutral (the spy is not blind). W3-04: group = 6 tensors, guard PASS, all moved, no leak. W3-05: a disconnected loss raises / fails the moved-check. W3-06: FROZEN survives 120 on-policy steps while the on-policy deque evicts (not blind to a one-element edit); the cap counts drops and never evicts. W3-07: pure-retained 80/0, then exactly 25.0% retained, pure on-policy 0/80 with no retained set. W3-08: re-encode matches the live z (<= 1e-5 at episode-start windows, <= 1e-3 truncated; the window-0 canary exceeds 1e-3), tracks an encoder change, and serves a frozen encoder from the cache. W3-09: export -> `append_external` round-trips byte-identically, re-encodes to the donor's z and trains; `schedule_external` releases at the logged steps. W3-10: **the L2R bar on a small FIXED dataset** (size-8 env, alpha_world 0.9, 2400 W2a babbling, 3000 + 1200 x 8 updates against a 90%-one-class on-policy stream): real disc4 0.673, k = 10 PASS; shuffled twin 0.213 FAIL (`probes/w3/results/small_fixed_dataset_runs.txt`). W3-11: knobs via `from_dims`, bad values raise, InfoNCE / stored modes train, TRAIN-mode rollout with all four members ON has no autograd error.

- **Test half:** all 19 FAIL on the pre-build tree (origin/main `2ea0e3c` with only the test file copied in; `probes/w3/results/prebuild_test_half.txt`).
- **Local runs:** 19/19 pass on the draft tree; the Mac-local contracts gate on the branch commit is recorded in section 6.

## 5. What this unblocks

- **ASP gate (c) is now runnable.** Its bounded-rollout check is "read with the W3 head" (design sec 4). That head can now be trained natively on the branch (recipe: the section 3 probe). Not run here. The section 3 (e) readout uses random one-hot 30-step rollouts, a form close to ASP candidates: t30/t0 1.06-1.26 and median late per-step growth <= 1.012. That is below G-ASP (c)'s 1.05 bound and inside [0.5, 2], but it is an indicator, not the gate.
- **N3 proper is now runnable** on the W3 member head (pinned probe; plan sec 4), with the twin fixed as class relabelling, as used here. DISC_0.5 is the lead candidate.
- **N2 is runnable once W6a lands:** `replay_latent` "reencode" vs "stored" are its two buffer arms, and the cache already re-encodes as soon as the encoder moves.
- **W2b:** retained records are plain dicts in an append-only list. The UNFROZEN rule would add a per-entry flag and a replacement path. Not built.

## 6. Landing

- ree-v3 `integration/coupled-loop-repair`: rebased onto main, `--force-with-lease` against `e4dc1a5`, W3 commit `042895a`. Mac-local contracts gate (`REE_PRECOMMIT_CONTRACTS_TARGET=local`, under the Mac probe lock): **5898 passed, 25 skipped, 3 xfailed** (24 m 33 s; lock held 20:25:16Z-20:50:07Z); pushed 2026-09-25T20:50Z (`e4dc1a5 -> 042895a`, forced update of the rebase). `git show --stat 042895a` = the 5 W3 files only.
- Probe scripts and results: `evidence/planning/probes/w3/`.
