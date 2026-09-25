# W6a build: `WorldEncoderMember` on `integration/coupled-loop-repair` (default-OFF) -- SD-070 P0a trained through the LIVE sense path

- **Status: BUILT on the branch; member-level reach checks PASS (D1).** Session `bt0925-w6a` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260925-coupled-w6a-world-encoder-build`. Written 2026-09-25T22:41:21Z.
- **Code:** ree-v3 `integration/coupled-loop-repair` @ `9b322d5`. That is the W6a commit on top of the branch rebased onto `origin/main` `07b5fe6` (clean rebase: ASP `3d6972b`, W1 codec `20aa34a`, W3 `7428da3`). Nothing on `main` changed. All knobs default OFF.
- **Plan of record:** `coupled_loop_repair_campaign_plan.md` sec 3 W-trainer (W6a, user decision Q4c; buffer-staleness requirement P8), sec 4 N2. This is the build `SD-ZWORLD-SENSE-PATH-PARITY` was registered for (plan sec 7 item 6).
- **Evidence domain: D1.** Gradient reaches the sense path, the weights move, and the sensed z_world becomes un-collapsed and decodable. Nothing here shows that any consumer (E2, E3) or behaviour changes (D2/D3). That is N2 / A1.

## 1. Premises re-measured before building

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | SD-070 P0a (`run_zworld_p0`) trains a path the agent never senses (SD-ZWORLD-SENSE-PATH-PARITY) | `ZWorldP0Trainer._z_world_path` = `split_encoder.world_encoder(world_state)` * precision (`ree_core/latent/zworld_p0.py`); `REEAgent.sense` = `world_obs_encoder` (Linear 250x250 + ReLU) -> `latent_stack.encode` (split encoder + top-down + SD-007 + SD-008 EMA) (`agent.py` sense, `enc_world = self.world_obs_encoder(obs_world)`) | holds. Only drivers call the recipe (`experiments/_lib/zworld_p0_warmup.py`), once, offline |
| P2 | "the ZSelfP0 `_native_chain` pattern (863d23d)" | `ree_core/latent/zself_p0.py` `_native_chain`: fresh detached `init_state`, per-step `cat(body_obs_encoder, world_obs_encoder)` -> `latent_stack.encode` with `prev_action`, gradient through the chain | holds; reused as the member's forward |
| P3 | branch head `042895a`, "rebase onto current main" (brief) | origin/main had moved 2 commits (`2801c3e` queue snapshot, `07b5fe6` contract cache), neither touches `ree_core/**` | clean rebase, no conflicts (W3 -> `7428da3`) |
| P4 | W3's re-encode cache "is exactly what W6a invalidates" (W3 record f82cb986c5) | `E2WorldMember._read_path` = every parameter + buffer of `body_obs_encoder`, `world_obs_encoder`, `latent_stack`; cache keyed on their `_version` | holds; contract W6a-06 shows it |
| P5 | "every trained group under the guard" | the sensed z also reaches the depth stack (`beta/theta/delta_encoder`, `*_to_*`, `world_topdown`; census 940c690c9dd #13, DEFERRED) and, via top-down, the z_self path (`body_obs_encoder`, `self_encoder`) -- probe `probes/w6a/encode_side_effects.py` | **scoped.** Those are not in the group: G5 leak (report-only), pinned to exactly those families; `.grad` restored after each update (see sec 2) |
| P6 | `latent_stack.encode` side effects when re-run inside a live agent | no module attribute or `state_dict` entry changes over a 5-step grad chain (`probes/w6a/encode_side_effects.py`) | holds; the chain is safe to run between live ticks |

## 2. What was built (branch only; `ree_core/**` + contracts)

- **`WorldEncoderMember`** (new `ree_core/utils/waking_trainer_world_encoder.py`), registered when `waking_trainer_enabled` and `waking_trainer_world_encoder_enabled` are both True, **after** the W3 member so W3's next replay re-encodes through the encoder this member just stepped. Imported only when ON.
  - **Recording:** raw sensory inputs via the existing `WakingTrainer.on_sense` hook (no new agent hook); one record per waking tick = the tick plus up to W preceding ticks of the same episode (W = `auto_reencode_window(alpha_world)`: 26 at 0.3, 4 at 0.9), the SD-007 prev-actions, and the tick's four scene-structure targets. Deque of `waking_trainer_buffer_max` records: **the member's own buffer ages out and is re-encoded on every update, so it can never go stale.**
  - **Forward (the trained path):** `init_state` -> for each recorded tick `cat(body_obs_encoder, world_obs_encoder)` -> `latent_stack.encode(..., prev_action, harm streams, volatility)` WITH gradient -> the last tick's sensed `z_world`. These are the same module objects `sense` calls, so a step changes the very next `sense` output (W6a-04). The chain reproduces the live latent: max abs diff 3e-8 at episode-start windows, 1.2e-5 at the auto window (alpha 0.3), 1.8e-6 (alpha 0.9); a 1-tick window gives 0.087 (canary).
  - **Objective = the SD-070 P0a recipe, reused, not re-derived** (`ZWorldP0Config` defaults): 4 grounding CE heads (`scene_structure_targets`; `balanced_class_weights` over the current buffer) + VICReg variance (25) / covariance (50) (`variance_covariance_penalty`) + world_obs reconstruction (10) + the SD-018 proximity MSE only when the stack has `resource_proximity_head` (it does not at defaults). The heads are the trainer's, built under a forked seeded RNG (no global draw), outside `state_dict`. The SD-018-amend field leg and SD-106 preservation leg (both default 0.0 in the recipe) are not carried; `world_encoder_skip` is trained if present.
  - **Group (17 tensors at defaults):** `world_obs_encoder.0.{weight,bias}` + `latent_stack.split_encoder.world_encoder.{0,2}.{weight,bias}` + `world_precision_logit` + 10 head tensors. Grad clip 1.0 on the encoder path only (SD-070 `max_grad_norm`), via a new optional member hook `clip_parameters`.
- **Trainer (`waking_trainer.py`), two opt-in hooks, byte-identical for every existing member:** `clip_parameters()` (clip a subset) and `restore_outside_grads` (snapshot every non-group agent parameter's `.grad` before the member's backward, restore it after the step). Without the second, W6a's backward would leave accumulating gradient on the depth stack / z_self path and would add to a driver's own pending gradients there. The guard observes before the restore, so leaks are still reported.
- **Knobs (3 sites: dataclass, `from_dims`, `PROBED`):** `waking_trainer_world_encoder_enabled` (False), `_lr` 1e-3, `_batch_size` 64, `_window` 0 (auto), `_grad_clip` 1.0, `_updates_per_step` 1.

## 3. Contracts (`tests/contracts/test_w6a_world_encoder_member.py`, 12)

W6a-01 OFF: nothing constructed at defaults; an ON trainer without the knob holds `["harm_eval"]` and never constructs the member. W6a-02: member ON with a never-firing cadence (records every tick, heads built) is byte-identical to OFF over a multi-episode rollout incl. torch/numpy/python RNG. W6a-03: group exact (7 encoder + 10 head tensors), guard PASS, all 17 moved, every update RNG-neutral, leak set non-empty and entirely within the deferred families, no stale `.grad` left on any non-group tensor; W6a-03b: a driver's pending grad on a depth-stack tensor is untouched by a W6a update. W6a-04: under the member `world_obs_encoder` AND `world_encoder` AND the precision logit move and `sense` of a fixed observation changes (> 1e-4); with the knob OFF (trainer ON, same rollout) none moves and the change is exactly 0. W6a-05: the chain reproduces the live latent (<= 1e-5 / <= 1e-3; 1-tick canary > 1e-3). W6a-06: with W3 ON (`reencode`), a frozen encoder is served from W3's cache; one W6a step changes the read-path key and W3's next re-encode is fresh and different. W6a-06b: W3 `stored` returns the byte-identical stored z after a W6a step (stale by design, the N2 arm) while a re-encode of the same records moves. W6a-07a/b: a detached loss raises (guard armed) / fails the moved-check (disarmed). W6a-07c: **the old defect** (SD-070's direct `world_encoder(world_state)`, bypassing `world_obs_encoder`) fails the guard, naming `world_obs_encoder`. W6a-08: knobs plumb; a TRAIN-mode rollout with every member ON (e1, e2_self, codec, e2_world, world_encoder) has no autograd error.

- **Test half.** (i) On the pre-build tree (`7428da3`, the test file copied in) all 12 fail (collection ImportError; the file imports the module directly rather than `importorskip`, which would have SKIPPED -- a blind spot fixed before landing). (ii) **Mutants** (`probes/w6a/mutants.py`, `probes/w6a/results/mutants_result.txt`), each re-introducing one defect into the build: M1 pre-projection trained as a detached side-copy -> W6a-03, W6a-04 red; M2 chain output detached -> W6a-03, -04, -06 red; M3 heads built on the global RNG -> W6a-02 red; M4 no outside-grad restore -> W6a-03, -03b red. Unmutated control 12/12 green.
- **OFF identity across trees** (`probes/w6a/xtree_off_identity.py`, `results/xtree_off_identity_result.txt`): the same 60-step TRAIN-mode rollout on the pre-build and build trees gives an identical sha256 over actions, z_world, final `state_dict` and all three RNG states, both at defaults and with the trainer ON with harm_eval + E1 + E2-self + codec + W3 (W6a knob OFF).
- **Targeted regression on the rebased tree:** ASP, grad-reach guard, W2a, W1 codec, W3, waking trainer, T1, W6a and `test_flag_inertness.py`: **189 passed, 2 xfailed** (the recorded ASP-R strict xfails).

## 4. Member readout (D1, report-only; not a pre-registered gate)

`probes/w6a/w6a_member_readout.py`: 8x8 CausalGridWorldV2 (3 hazards, 2 resources), world_dim = self_dim = 32 (deployed), uniform-random policy, 2000 waking steps through `sense` + `update_residue` (trainer ON; W6a ON vs OFF = untrained encoder), then frozen, 1200 held-out steps on fresh env seeds. PR = participation ratio of the SENSED z_world; BA = held-out balanced accuracy of a logistic probe (episode-split) for the four scene-structure targets.

| seed | alpha_world | W6a | PR (sensed z) | BA hazard_present | BA resource_present | BA hazard_dist | BA resource_dist | mean norm z | world_obs_encoder rel. change |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.9 | OFF | 7.67 | 0.659 | 0.778 | 0.516 | 0.574 | 0.44 | 0.000 |
| 1 | 0.9 | ON | 15.14 | 0.978 | 0.998 | 0.986 | 0.999 | 6.33 | 1.664 |
| 2 | 0.9 | OFF | 7.21 | 0.758 | 0.708 | 0.561 | 0.590 | 0.53 | 0.000 |
| 2 | 0.9 | ON | 14.20 | 0.987 | 0.998 | 0.991 | 1.000 | 7.30 | 1.744 |
| 3 | 0.9 | OFF | 8.00 | 0.731 | 0.681 | 0.542 | 0.521 | 0.50 | 0.000 |
| 3 | 0.9 | ON | 14.10 | 0.993 | 1.000 | 0.997 | 0.995 | 7.12 | 1.717 |
| 1 | 0.3 | OFF | 1.34 | 0.685 | 0.758 | 0.520 | 0.561 | 0.39 | 0.000 |
| 1 | 0.3 | ON | 14.85 | 0.875 | 0.917 | 0.788 | 0.815 | 4.60 | 2.229 |
| 2 | 0.3 | OFF | 1.26 | 0.634 | 0.703 | 0.507 | 0.548 | 0.46 | 0.000 |
| 2 | 0.3 | ON | 12.11 | 0.847 | 0.879 | 0.751 | 0.834 | 4.01 | 2.332 |
| 3 | 0.3 | OFF | 1.24 | 0.727 | 0.675 | 0.549 | 0.546 | 0.43 | 0.000 |
| 3 | 0.3 | ON | 11.32 | 0.868 | 0.883 | 0.740 | 0.825 | 4.29 | 2.265 |

Chance: presence 0.50; distance 0.33 (3 classes scored). ON: 1937 member updates per run, guard PASS on 6/6. Wall time per ON run: ~42 s at alpha 0.9 (window 4), ~430-520 s at alpha 0.3 (window 26), batch 64.

- **Reading.** Through the sense path the recipe does what it did offline: no collapse, and the sensed z_world carries the grounding targets on held-out episodes. The SD-070 anti-collapse gate (PR >= 2 and >= 0.5x untrained) is met on 6/6 runs. PR roughly doubles at alpha 0.9 (7.2-8.0 -> 14.1-15.1). Held-out BA reaches 0.98-1.00 on all four targets, against 0.52-0.78 untrained.
- **Finding at the from_dims default alpha_world 0.3:** the UNTRAINED sensed z_world is already effectively one-dimensional (PR 1.24-1.34). That is not the case for the direct-path z_world SD-070 measured. The SD-008 EMA over a random pre-projection collapses it. W6a lifts PR to 11.3-14.9. BA is lower than at alpha 0.9 (0.74-0.92), which is consistent with the last frame carrying only 30% of the sensed latent (module docstring). So any consumer reading the sensed z_world at alpha 0.3 with an untrained encoder reads a near-1-D signal. Stated, not tested further here.
- **Cost.** At alpha 0.3 (window 26), batch 64, one update is ~0.22-0.27 s on the Mac; at alpha 0.9 (window 4) it is ~0.02 s. A 9,600-update N2 arm at alpha 0.3 is therefore ~40 min of member compute per seed. Size N2 for a cloud worker, or reduce `_batch_size` / `_window` and pre-register the change.
- **Scale shift, stated because N2 turns on it.** The VICReg variance hinge drives the sensed z_world norm from ~0.5 to ~6-7 (~14x). Every consumer calibrated on the untrained scale sees a different input: the W3 E2 world head (its L2R bar was measured at the untrained scale), harm_eval, the codec, E1, E3's scorer. That is exactly N2's question and is not assessed here.

## 5. Interaction with W3, and what N2 can now run

- **W3 `replay_latent` modes.** With W6a OFF the two modes are the same up to the re-encode truncation (<= 1e-3), so the distinction carries no information. With W6a ON they diverge: **`"reencode"` (the default) is the meaningful mode.** Its targets and inputs track the current encoder (W6a-06). **`"stored"` becomes meaningful only as N2's stale-latent control arm** (W6a-06b).
- **N2 is now runnable** (status `ready`). All three pre-registered arms are configuration only, on one branch sha: (1) frozen encoder = W6a OFF; (2) encoder trained through the read path with raw-obs re-encode = W6a ON + W3 `reencode`; (3) encoder trained with stored-z replay = W6a ON + W3 `stored`. Not run here: it needs its own pre-registered pinned probe (L2R protocol, 5 seeds).
- **Other members' staleness (P8), stated, not changed.** `HarmEvalMember` and `CodecMember` replay stored z_world, and `E1Member` replays the agent's own stored experience buffers. All three go stale while W6a trains. Which policy each needs (re-encode or bounded age) is part of N2 (plan sec 3). W6a's own buffer is re-encoded on every update.

## 6. Landing

- ree-v3 `integration/coupled-loop-repair`: rebased onto main `07b5fe6` (clean), W6a commit `9b322d5`, pushed with `--force-with-lease` against `042895a` (2026-09-25T22:41Z; `042895a -> 9b322d5`, forced update of the rebase). `git show --stat 9b322d5` = the 5 W6a files only. Nothing pushed to `main`, apart from the gate's own validation-cache record (`389154f`, the standard gate side effect). Since the rebase, main has moved only by that record and a queue snapshot (`c6ed496`), neither touching `ree_core/**`, so no second rebase was needed.
- **Mac-local contracts gate** (`REE_PRECOMMIT_CONTRACTS_TARGET=local`, under the Mac probe lock 22:15:12Z-22:40:56Z): **5910 passed, 25 skipped, 3 xfailed** (24 m 37 s).
- Probe workers bt0925-n3 / bt0925-aspc read the branch at the pinned sha `042895a`. A rebase does not disturb them, but `042895a` is no longer on the branch. Their pins resolve only while the sha stays reachable, so the orchestrator may want an `archive/` tag on it if they are re-run later (not done here: tags are an orchestrator call).

- Probe scripts and results: `evidence/planning/probes/w6a/`.
