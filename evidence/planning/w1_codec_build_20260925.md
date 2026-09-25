# W1 codec build record: joint codec + bounded decode + image-matched iteration 0 (default-OFF, integration branch)

- **Status: BUILT on `integration/coupled-loop-repair`**, default-OFF, bit-identical when OFF. Session `bt0925-w1codec` (headless build worker, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-coupled-w1-codec-build`. Written 2026-09-25.
- **Scope built:** campaign plan (`coupled_loop_repair_campaign_plan.md`) sec 3 W1 parts (1)-(3); member gates (a)-(d) as contracts. **Out of scope:** part (4), `terrain_prior` on a grounded target (probe N4, gated on W4), and gate (e) (needs W3/W4; its consumer-mediated leg is reported-until-W5, rec-20260925-a16786f5).
- **Branch commit:** ree-v3 **`e4dc1a5`** (pushed to origin `integration/coupled-loop-repair`, fast-forward with lease from `1a16595`), on top of W1-alt's ASP commit (`1a16595`). Files: `ree_core/hippocampal/module.py`, `ree_core/utils/config.py`, `ree_core/utils/waking_trainer.py`, `ree_core/utils/waking_trainer_codec.py` (new), `tests/contracts/test_w1_codec.py` (new), `tests/test_flag_inertness.py` (3 PROBED entries). Nothing else is on the branch (plan sec 6).
- **Evidence domain: D1** for gates (a)-(d): contract-level, deployed dims (world_dim = self_dim = 32, action_dim 5, K = 32, H = 30 via from_dims, 3 CEM iterations). No closed-loop run, no D2/D3 claim.

## 1. Premises re-measured

| premise (source) | re-measured on the draft tree (base `21c86cb` + W1-alt staged) | status |
|---|---|---|
| decode at `module.py:644-647`, consumed at `:2280`; iteration 0 at `:2151` (plan, main at the probe sha) | drifted: `_decode_action_objects` now ~`:655-700` (ASP call counter added), CEM decode at ~`:2745`, iteration-0 init at ~`:2605`; ghost-probe decode (`_mech293`) also uses `ao_std = 1` and the decoder | holds in content, lines moved |
| encoder image norm ~0.29-0.36; iteration-0 samples ~3.9 (~12x) | untrained, deployed dims: image median 0.304; iteration-0 O-norm median 3.86 -> ratio **12.7** | holds |
| a CE-trained decoder on the frozen encoder diverges in the CEM loop | trained codec with the knobs OFF: decoded norm 17 -> 69 -> 296 over 3 iterations (growth x4.0, x4.3) | holds (same shape) |
| the encoder does not feed E2's world prediction | `rollout_with_world` steps `world_forward(z_world, action)` on the RAW action; `action_object_head` only produces `traj.action_objects` (read by the hippocampal refit and E3's cue-bias term) | holds; training the encoder changes no world prediction |
| `e2.action_object_head` is outside `FROZEN_BY_DESIGN` | yes; guard group needs no allowlist entry | holds |

## 2. What was built

**Knobs (5, all default OFF / inert), at all config sites.**
- `HippocampalConfig.use_codec_bounded_decode` (part 2) and `HippocampalConfig.use_codec_iter0_image_match` (part 3): dataclass, `from_dims` kwargs, `from_dims` assignment.
- `REEConfig.waking_trainer_codec_enabled`, `waking_trainer_codec_lr` (1e-3), `waking_trainer_codec_code_l2` (1e-3) (part 1): dataclass + `from_dims` pop (the C1/T1 waking-trainer pattern). Read only when `waking_trainer_enabled`.
- The iteration-0 knob is named `use_*` so the flag-inertness registry scanner (`use_*` / `*_enabled`) sees it.

**(1) Joint codec member** (`ree_core/utils/waking_trainer_codec.py`, `CodecMember`, registered in `WakingTrainer.__init__` behind its knob).
- Group = every `e2.action_object_head.*` + `hippocampal.action_object_decoder.*` tensor (8 tensors); one Adam optimizer; the C1 guard armed for the first `waking_trainer_guard_min_steps` updates; the trainer's private RNG and python/numpy state restore (C1 machinery, unchanged).
- Objective, per replay batch of recorded `z_world` and EVERY class c: `CE(decoder(E2.action_object(z, onehot(c))), c) + code_l2 * mean ||o||^2`. Gradient reaches both maps (trace candidate 2, the joint codec). **Labels are enumerated by the member, not read from executed actions**, because the agent's own replay can lack whole classes (ADDENDUM 2) and a decoder never shown a class cannot emit it. Only the agent's own sensed `z_world` is recorded.
- The code-norm penalty exists because pure CE can always lower its loss by inflating `||o||`. Measured: with `code_l2 = 1e-3` the image median rises to 2.85 at 300 steps, then falls back to 1.10 (1000 steps) and 0.33 (3000 steps) as CE saturates. So the scale is transient, not runaway. Part (3) tracks whatever scale the image has, so no gate depends on it.
- No cue bias (SD-016 `action_bias`) in the objective: it is additive in O after the encoder. Stated as a limit.

**(2) Bounded decode** (`HippocampalModule._decode_action_objects` -> `_bounded_onehot` -> `_StraightThroughOneHot`).
- Forward: an EXACT one-hot of the decoder's argmax. Norm 1, which is the action space E2's world head is trained on. Backward: the softmax Jacobian (matches `torch.softmax` autograd to 3e-8), so any gradient path that reached the raw logits still reaches the decoder.
- A custom autograd function, not `hard + soft - soft.detach()`: that expression rounds, so its forward values are 1 +- ulp, not exactly one-hot. Contract K3 caught this on the first draft.
- argmax is deterministic and draws no RNG (not `torch.multinomial`, which differs across the fleet's machine classes).
- Applies at every decode call site: the CEM loop and the MECH-293 ghost probes. The propose diagnostic `action_object_decoder_raw_output_stats` summarises `traj.actions`, so with the knob ON it reports the bounded (one-hot) vectors that actually reach the rollout, not raw logits.

**(3) Iteration-0 sampling matched to the encoder image** (`HippocampalModule._encoder_image_init`).
- Iteration 0 samples from a diagonal Gaussian fit to `{E2.action_object(z_world, onehot(c), action_bias)}` over the `action_dim` classes. The mean is the image centroid; the std is the per-dim population spread across classes (floor 1e-6), broadcast over H.
- It is the same map the rollout re-encodes with, so the same points the elite refit moves toward. It runs under no_grad and draws no RNG.
- **Decision (recorded):** `terrain_prior` is NOT called on this path. Its output is an absolute point in O, its only trainer today is driver-side BC of E3's own picks (circular), and its untrained mean has median norm 0.25, so it cannot be mixed in without its own scale question. Routing a grounded prior back in is part (4), settled by probe N4. This is the orchestrator-delegated "obvious decision", taken headless.

**Not changed:** the SP-CEM `ao_std` floor (0.2 per dim, absolute) on iterations 1-2, and the ASP path. With ASP ON, the codec loop runs 0 iterations and never decodes, so both hippocampal codec knobs are inert. They do not raise; see finding F3.

## 3. Contracts (`tests/contracts/test_w1_codec.py`, 13 tests)

| test | pins | pre-build tree (`21c86cb` + W1-alt, file copied in) | build |
|---|---|---|---|
| K1 knobs default False + from_dims round trip | 3-site rule | FAIL (AttributeError) | PASS |
| K2 OFF = pre-build codec path | OFF decode == raw decoder output; iteration 0 reads terrain_prior once/call; the new helpers raise if touched and the pool/world states/RNG are unchanged; ON trainer with codec OFF holds only `harm_eval` | FAIL | PASS |
| K3 bounded decode | exact one-hot forward (values in {0,1}, row sum 1, argmax = raw argmax, max norm 1.0 at inputs 40x out of range); gradient non-zero on every decoder tensor | FAIL | PASS |
| K4 ON is RNG-count neutral | knobs ON leave the global torch RNG where OFF leaves it | PASS **by design** (a preservation pin; from_dims swallows the unknown kwargs, so both arms are OFF); FAILS under mutation M3 | PASS |
| GA gate (a) guard | group == exactly the encoder + decoder tensors; guard **PASS**; all 8 tensors move; losses finite | FAIL | PASS |
| GA' not blind | a decoder-only loss (codes detached = trace candidate 1) makes the guard FAIL and the trainer raise, naming `action_object_head` | FAIL | PASS |
| GB gate (b) round trip | after 1000 member updates on 160 z_world states (uniform-random play, seed 1), held-out (60 states) per-class accuracy **1.00 / 1.00 / 1.00 / 1.00 / 1.00** (bar 0.95) | FAIL | PASS |
| GB' not blind | the untrained codec on the same instrument: **0.0 / 0.0 / 0.0 / 0.0 / 1.0** (every class decodes to class 4: the bias-class pinning) -> FAIL | FAIL | PASS |
| GC gate (c) | trained codec, knobs ON: decoded norm / one-hot norm **1.00 / 1.00 / 1.00**, growth 1.0, 1.0 (I1 `codec_ranges`, strict no-growth rule) | FAIL | PASS |
| GC' not blind | the same trained codec, knobs OFF (pre-build path): decoded **17.0 -> 68.5 -> 295.7**, growth x4.03, x4.32 -> FAIL | FAIL | PASS |
| GD gate (d) | iteration-0 O-norm / image median: untrained **1.02**, trained **0.94** (knobs ON) | FAIL | PASS |
| GD' not blind | knobs OFF: untrained **12.69**, trained **3.50** -> FAIL | FAIL | PASS |
| P probes | each hippocampal knob ON changes the pool's actions; codec knob registers the group | FAIL | PASS |

- **Pre-build run:** 12 FAIL, 1 PASS (K4, by design). Runner: `.scratch/breakthrough-20260924/w1codec/mini_runner2.py` (no-pytest runner, module fixtures; the Mac does not run pytest).
- **Mutations (test half, non-vacuity):**
  - M1: bounded decode returns raw logits -> GC, GD, K3, P fail (4).
  - M2: iteration-0 std reverted to 1 -> GD fails.
  - M3: one extra `torch.rand` on the ON path -> K4 fails.
  - Scripts: `.scratch/breakthrough-20260924/w1codec/` (umbrella, not committed).
- **OFF bit-identity against the pre-build tree** (Mac, torch 2.10): a 30-tick train-mode StepHarness rollout (actions, z_world, float state_dict, RNG) plus 4 full propose pools (actions + world states) plus the final RNG state, for 2 configs (default; `waking_trainer_enabled=True`), hash identically on the pre-build tree and the build: `bb446d4d...3ea4f43` both (`w1codec/off_identity.py`).
- **Shared-file check:** W1-alt's `test_action_space_proposals.py` on the build tree gives 33 pass, 2 xfail (its two strict xfails), 0 fail. Also green locally on the build tree: `test_waking_trainer.py` 12/12, `test_exp0155...` 10/10 (after rewording a `config.py` comment that contained the scanned token, the same trap ASP hit), `test_action_object_roundtrip_not_an_action_source.py` 9/9, `test_ao_decoder_injection_free_stats.py` 8/8, `test_hippocampal_candidate_support.py` 10/10, `test_mech131...` 9/9, `test_grad_reach_guard.py` 8/8, `test_flag_inertness.py::test_flag_registry_is_current` PASS.
- **Commit gate:** Mac-local pre-commit hook (`REE_PRECOMMIT_CONTRACTS_TARGET=local`, under the Mac lock) on the committed tree: tests/contracts **5849 passed, 25 skipped, 3 xfailed**, 0 failed (22 min). The rebased tree is byte-identical, file by file, to the draft tree the local numbers above were measured on (W1-alt's final commit equals the staged state the draft was built on).

## 4. Member gate status (plan sec 3 W1)

| gate | status | evidence |
|---|---|---|
| (a) guard PASS on the codec group | **PASS (D1, contract)**. The prior group does not exist yet (part 4) | GA, GA' |
| (b) held-out round trip >= 0.95 per class | **PASS (D1, contract)**: 1.00 on every class | GB, GB' |
| (c) decoded norm in [0.5, 2] x one-hot over 3 CEM iterations, no growth | **PASS (D1, contract)**: exactly 1.0 by construction of the bounded decode, on the trained codec | GC, GC' |
| (d) iteration-0 O-norm in [0.5, 2] x image median | **PASS (D1, contract)**: 1.02 untrained / 0.94 trained | GD, GD' |
| (e) informative D2 (containment + consumer-mediated leg) | **NOT ASSESSED**: needs W3/W4 (and the prior, part 4); the consumer leg is reported-until-W5 | - |

## 5. Findings (reported, not acted on)

- **F1. Pool diversity (descriptive, 8 states, one seed, not a gate).** First-action classes per pool with the trained codec: knobs ON 5,4,5,5,5,5,5,5; knobs OFF (pre-build path) 3,5,5,4,4,5,2,5. The untrained pre-build pool held 2-3 classes. Variation is NOT evidence of choice-relevance: a shuffled decoder varied the pool as often as an honest one (criterion P, `a369f411ff8`). Gate (e) is the test.
- **F2. The SP-CEM std floor dominates iterations 1-2.** With the knobs ON, the iteration-1/2 O-norm is ~2.4x the image on a long-trained codec (0.79 vs 0.33 at 3000 steps) and ~1.1x at 1000 steps (1.20 vs 1.10). The cause is the absolute `support_preserving_ao_std_floor = 0.2` per dim, not the codec. Decoded norms stay 1.0 because the decode is bounded, so no gate is affected. But on a small-scale image, refit samples are floor-dominated. Whether the floor should be image-relative is a W1 / N4 question; it was not changed here, because iteration 0 was the brief's scope.
- **F3. Codec knobs are inert under ASP.** ASP never decodes and runs 0 codec iterations. INT-ACT and INT-CODEC are separate presets, so this is correct. If the W6 preset ever sets both, the codec knobs silently do nothing. A construction-time raise, like ASP's own exclusions, is a one-line follow-up if the preset owner wants it.
- **F4. Encoder image scale is transient under the joint objective** (sec 2 (1)): 0.30 -> 2.85 (300 steps) -> 1.10 (1000) -> 0.33 (3000). Part (3) follows it by construction. Any other O reader calibrated on a fixed scale (E3's cue-bias term reads `traj.action_objects` when `action_bias` is present; it is None at defaults) would see it move during training. `waking_trainer_codec_code_l2` is the lever.

## 6. Not done

- Part (4) (`terrain_prior` grounded target; N4), gate (e), and the prior group's guard.
- No closed-loop or behavioural measurement; no probe beyond the contract-scale numbers above; no queue entry, no registry row, no A1 edit.
- The non-contract remainder suite was not run: the change is default-OFF and pinned bit-identical, and the commit gate ran the contracts.
