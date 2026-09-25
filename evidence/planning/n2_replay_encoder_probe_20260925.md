# Probe N2: does W3's retained replay keep the L2R bar while W6a trains the world encoder through the read path? (Q4c, P8)

- **Status: PRE-REGISTERED** (this section committed before any registered seed ran). Session `bt0925-n2` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260925-coupled-n2-replay-probe`. Written 2026-09-25T23:11:26Z.
- **Code:** ree-v3 `9b322d5` (tag `archive/coupled-loop-repair-9b322d5`, the W6a commit on `integration/coupled-loop-repair`), throwaway detached worktree `.scratch/wt-n2`. No `ree_core` edits. All three arms are configuration only on this sha.
- **Plan of record:** `coupled_loop_repair_campaign_plan.md` sec 4 N2 row, sec 1 P8, sec 3 W-trainer (buffer-staleness requirement) and W3 member gate (a)-(e). Upstream records: W3 `w3_e2_world_member_build_20260925.md` (f82cb986c5), W6a `w6a_world_encoder_member_build_20260925.md` (eb055574c05).
- **Probe:** `probes/n2/n2_probe.py` (one invocation = one seed x arm x twin), runner `probes/n2/run_seed.sh`, results `probes/n2/results/`.
- **Evidence domain this probe can reach: D1** (a member-trained head's discrimination on held-out data, read in the encoder space it will actually be consumed in). No consumer (E3) or behaviour reading is claimed; that is N3 / W4 / A1.

## 1. Premises re-measured before registering

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | the three arms are configuration only on one sha (W6a record sec 5) | on `9b322d5`: the probe constructs `E2WorldMember(replay_latent="reencode" or "stored")` and `WorldEncoderMember(...)` directly, W3 registered before W6a (as `WakingTrainer.__init__` does, `waking_trainer.py` ~L706-735); `replay_batch` uses the stored `z_live` only in `stored` mode (`waking_trainer.py` ~L618-640) | holds |
| P2 | "~0.25 s per W6a update" (W6a record sec 4) | timing smoke, seed 106 (not registered), 200 post steps: `frozen` 11 s, `stored` 59 s, `reencode` 123 s. W6a itself costs ~0.25 s per update, as stated. But in `reencode` every W6a step invalidates W3's cache, so the 8 W3 updates per step re-encode their batch (26-tick chains). The `reencode` arm therefore costs ~2x the `stored` arm | holds for W6a; the `reencode` arm total is ~0.6 s per waking step |
| P3 | W3's protocol is reproducible on this sha (W3 record sec 3: s106 reproduced 0.5233 on the branch tree) | canary seed 106, arm `frozen`, 1200 post steps, B0 recomputed by `--b0-only`: pre 0.4333 / k 9, post **0.5233 / k 10**, retention **1.711**, t30/t0 1.09, guard PASS, FROZEN intact. Every value equals W3's published s106 row. Pre disc4 was also 0.4333 in the `reencode` and `stored` smokes (babble + pre are identical across arms). In `frozen` the current-space readout equals the reference-space readout (norm ratio 1.00). `evaluate_sd(sd=None)` is asserted equal to `babble_probe.evaluate` on every run | holds (harness canary PASS) |
| P4 | B0 = "the babbling probe's on-policy-data head" is recomputable for fresh seeds | the first recompute gave 0.2967 against the published 0.3067. The published runs used `--n-eps 12` (2400 POL transitions), not the script default 25. After the correction the recompute reproduces B0 0.3067, the benign class and the POL run statistics exactly on 9b322d5 | **corrected** (n_eps 12) |
| P5 | "W6a scales z_world norm 10-14x and raises PR from ~1.2 to 11-15" (W6a record: 1937 updates, 8x8 env) | in this env, after only 200 W6a updates (`stored` smoke): test-set norm x8.5, PR 1.40 -> 5.10, `world_obs_encoder` relative weight change 0.81 | holds in direction; most of the shift happens early |

**Disclosure, stated before the registered seeds run.** The timing smoke of arm 3 (`stored`, seed 106, 200 post steps; not a registered seed or dose) completed its readout: current-space disc4 0.270 / k 0, rollout unbounded (t30/t0 58), retained stored-z relative staleness 0.93. The `reencode` smoke crashed at the readout and produced none. (The crash was a `deepcopy` of the agent; it is fixed by reading through the agent itself after the trainer is detached.) So this pre-registration is written after seeing one short, non-registered arm-3 run. The decision rule below is the brief's, unchanged by it. Smoke logs: `probes/n2/results/smoke/`.

## 2. Design (pre-registered)

**Protocol = the W3 member-gate probe, reused verbatim** (`probes/w3/w3_l2r_member_probe.py`): the babbling probe's env (CausalGridWorldV2 size 12, Phase-0 kwargs, new env per 200-step episode), `build_B` agent (world_dim 32 = deployed, alpha_world 0.3 = from_dims default), held-out test set (3000 uniform-random {0..3} steps, k = 120..134), `evaluate()`; W2a babbling 2400 steps (12 episodes) into the FROZEN retained set; 3000 W3 member updates (pre phase); then the post phase: **600** (not W3's 1200; see Cost) native closed-loop `StepHarness` steps (k = 50..) with 8 W3 updates per step at the 25% retained mix. W3 member knobs as in the W3 gate (lr 3e-4, batch 32, MSE, grad_clip 1.0, retained cap 5000).

**Arms (config only, one sha):**

| arm | W6a `WorldEncoderMember` | W3 `replay_latent` |
|---|---|---|
| 1 `frozen` (control) | OFF (encoder frozen at random init) | `reencode` (= the W3 gate config) |
| 2 `reencode` | ON | `reencode`: stored raw obs re-encoded through the CURRENT read path at replay |
| 3 `stored` | ON | `stored`: the z sensed at record time (goes stale as the encoder moves) |

W6a: from_dims defaults (lr 1e-3, batch 64, window auto = 26 at alpha 0.3, grad_clip 1.0), 1 update per waking step, registered after W3 (so W3's next replay sees the encoder W6a just stepped). **W6a records every sensed tick (babble + post) but trains only in the post phase** -- the waking run -- so babbling and the pre phase are byte-identical across arms (checked: pre disc4 must be equal across the three arms of a seed). **Twin per arm:** `shuf` = retained babbling actions relabelled by W3's FIXED class permutation [1,2,3,4,0]; everything else identical.

**Seeds (fresh):** 611, 612, 613, 614, 615 (not 106-110, not 531-535). **B0** (retention baseline) is recomputed per seed with the babbling probe's own recipe (`babble_probe` POL: 12 native episodes k = 25.. (the published `--n-eps 12`), `train_head` 3000 updates) -- the published B0 exists only for 106-110. Canary: seed 106 recomputed B0 and the frozen arm must reproduce the published values (sec 1).

**Readout, at the END of the waking run, in the CURRENT encoder's latent space (PRIMARY):** the test-set raw streams are re-encoded through the end-of-run read path (the agent itself after the run, trainer detached, `sense` after `reset` per episode -- `babble_probe.encode_segs`), and the post head is scored with `evaluate()` on those latents. For arm 1 the current space is the reference space (identity check).

**Per-run gate legs (the W3 member gate, read in the current space):**
- (a) disc4_h1 >= 0.47 and k = 10.
- (b) retention (post_cur - B0) / (pre - B0) >= 0.5 (pre and B0 in the reference space, where they were trained/measured).
- (c) the arm's `shuf` twin does NOT meet (a).
- (d) guard PASS on the W3 group (W6a's guard reported, not gating here: it is W6a's own member gate).
- (e) bounded rollout from current-space test starts, 30 random one-hot actions, 40 starts: max over starts of the late (steps 21-30) mean per-step norm growth < 1.2 and median t30/t0 < 5.

**Arm keeps the bar** iff: (a) on >= 4/5 seeds; (b) on >= 4/5; (c) its twin meets (a) on <= 1/5; (d) all runs; (e) on >= 4/5.

**Decision (pre-registered, evaluated in this order):**
1. **CANNOT_DETERMINE** if arm 1 (control) misses (a) on >= 2 seeds.
2. **HOLDS-REENCODE** if arm 2 keeps the bar (sub-label **HOLDS-BOTH** if arm 3 also keeps it: then the cheaper stored policy is also adequate at this dose).
3. **HOLDS-STORED-ONLY** if arm 3 keeps the bar and arm 2 does not.
4. **NEITHER** otherwise: name which leg breaks, per arm.

**Secondary readouts (pre-registered, NOT gating):**
- (S1) **scale-normalised variant:** disc4_h1 / k with the error metric standardised per latent dimension by the current-space test-set SD (pred and target both divided). Note, stated before running: disc4 (an argmin over classes) and k (median err / median persistence) are already invariant to a *uniform* rescaling of the latent space, so a pure 10-14x scale shift can break (a) only through the head's training dynamics, not at the readout. S1 additionally removes per-dimension anisotropy (VICReg equalises dimension variances). If a leg breaks in the primary but not in S1, the break is attributed to scale/anisotropy of the metric; if it breaks in both, to the head's fit.
- (S2) the post head read in the REFERENCE (untrained-encoder) space -- whether the head still speaks the old space.
- (S3) latent scale / PR of the test set before vs after, `world_obs_encoder` relative weight change, W6a's last loss terms.
- (S4) staleness: median relative difference between the stored z and the current re-encode, on 256 retained and 256 on-policy records.
- Behaviour counts and reward (not gates).

**Also reported (D0, reasoned from the result):** whether `HarmEvalMember`, `CodecMember` and `E1Member` -- which replay stored latents -- need the same policy.

**Cost / stop rules:** At W3's 1200 post steps, one seed (B0 + 3 arms x 2 twins) takes ~45 min of Mac wall (P2), over the brief's ~20 min per seed. **Pre-registered reduction: the post phase is 600 waking steps** (3 episodes, k = 50..52). The rate stays at 8 W3 updates per step, with the same replay ratio and mix, so the post phase has 4800 W3 updates instead of 9600, plus 600 W6a updates. This deviates from the W3 gate dose and is fixed before any registered seed runs. It gives the on-policy stream less time to erode the babbling map in every arm, the control included. It also gives W6a 600 updates rather than ~2000; P5 shows most of the scale shift is already present at 200. Expected ~22 min per seed, one lock hold per seed. Runs are serial under the Mac probe lock (2 torch threads). If a seed exceeds ~20 min of Mac wall, the post phase is shortened for the remaining seeds and that is stated in sec 3 (never silently).
