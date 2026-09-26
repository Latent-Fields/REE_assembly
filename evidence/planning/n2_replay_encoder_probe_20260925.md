# Probe N2: does W3's retained replay keep the L2R bar while W6a trains the world encoder through the read path? (Q4c, P8)

- **Status: RUN -- VERDICT CANNOT_DETERMINE** (control arm missed (a) on 4/5 at the pre-registered reduced dose; sec 3). Pre-registration (secs 1-2) committed `025fc6a5cfe` before any registered seed ran. Session `bt0925-n2` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260925-coupled-n2-replay-probe`. Written 2026-09-25T23:11:26Z.
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

## 3. Result (written 2026-09-26T01:24:56Z; sections 1-2 unchanged since the pre-registration commit `025fc6a5cfe`)

### VERDICT: **CANNOT_DETERMINE** (pre-registered rule 1: the control arm misses (a) on 4/5 seeds)

The frozen-encoder control meets (a) on **1/5** seeds (614 only). Rule 1 needs >= 2 misses and gets 4, so N2 is **not decided** at the pre-registered dose. The control's miss is not a harness fault. The canary reproduces W3 exactly (P3). Twins fail 5/5, guard PASS 5/5, FROZEN intact 5/5, (b) retention 5/5, (e) bounded 5/5. The control fails only the 0.47 threshold of (a): post disc4 0.377-0.517, k = 10 on 5/5.

**Why the control missed: the pre-registered dose cut** (post 600 instead of W3's 1200; sec 2 Cost). At the W3 dose the post phase ADDS discrimination over pre on 4/5 seeds (W3 seeds 106-110: pre 0.433-0.473 -> post 0.460-0.523). At 600 steps, post is at or below pre on 4/5 seeds (611 0.447 -> 0.417, 612 0.507 -> 0.427, 613 0.440 -> 0.440, 615 0.413 -> 0.377; 614 0.507 -> 0.517). The fresh seeds' pre values sit in W3's range. So the gain W3 banked comes from the second half of its on-policy phase, which the cut removed. **The reduced dose was chosen to fit a Mac probe and it broke the control. I made that call; the brief's rule was applied as written.**

### Per-run table (primary = current-encoder space; S1/S2 secondary, not gating)

| seed | stratum | arm | pre disc4/k | **post disc4/k (current)** | disc5 | retention | SHUF post disc4/k | (e) t30/t0, late max | S1 std disc4/k | S2 ref-space disc4/k | norm x | PR ref->cur | woe drift | stale ret/onp | guard |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 611 | benign | frozen | 0.447 / 8 | **0.417 / 10** | 0.383 | 0.79 | 0.160 / 10 | 1.39, 1.064 | 0.447 / 10 | 0.417 / 10 | 1.00 | 1.30->1.30 | 0.000 | 0.00 / 0.00 | e2_world:PASS |
| 612 | hazard-trapped | frozen | 0.507 / 8 | **0.427 / 10** | 0.347 | 0.57 | 0.180 / 9 | 1.39, 1.078 | 0.413 / 9 | 0.427 / 10 | 1.00 | 1.27->1.27 | 0.000 | 0.00 / 0.00 | e2_world:PASS |
| 613 | hazard-trapped | frozen | 0.440 / 9 | **0.440 / 10** | 0.393 | 1.00 | 0.140 / 10 | 1.10, 1.018 | 0.407 / 10 | 0.440 / 10 | 1.00 | 1.25->1.25 | 0.000 | 0.00 / 0.00 | e2_world:PASS |
| 614 | hazard-trapped | frozen | 0.507 / 10 | **0.517 / 10** | 0.470 | 1.06 | 0.167 / 9 | 1.49, 1.064 | 0.500 / 7 | 0.517 / 10 | 1.00 | 1.52->1.52 | 0.000 | 0.00 / 0.00 | e2_world:PASS |
| 615 | hazard-trapped | frozen | 0.413 / 9 | **0.377 / 10** | 0.320 | 0.69 | 0.170 / 10 | 1.37, 1.053 | 0.390 / 10 | 0.377 / 10 | 1.00 | 1.36->1.36 | 0.000 | 0.00 / 0.00 | e2_world:PASS |
| 611 | benign | reencode | 0.447 / 8 | **0.520 / 10** | 0.470 | 1.51 | 0.133 / 0 | 2.87, 1.236 | 0.520 / 10 | 0.230 / 0 | 8.94 | 1.30->7.45 | 1.442 | 0.94 / 0.31 | e2_world:PASS,world_encoder:PASS |
| 611 | benign | stored | 0.447 / 8 | **0.257 / 0** | 0.223 | -0.33 | 0.290 / 0 | 3.19, 1.498 | 0.267 / 0 | 0.363 / 0 | 8.84 | 1.30->7.75 | 1.479 | 0.93 / 0.33 | e2_world:PASS,world_encoder:PASS |

Aggregates: `frozen` n = 5: (a) 1/5, (b) 5/5, twin meets (a) 0/5, (d) 5/5, (e) 5/5. `reencode` and `stored` **n = 1 (seed 611 only)**.

**Run order, stated.** Seed 611 ran all six runs in one lock hold (23:40-00:01Z). The Mac probe lock was then held by other workers for ~53 min. To reach the decision within the ~3 h cap, the remaining seeds were **reordered** (rule unchanged): B0 + the control arm (real and shuf) for 612-615 ran in one hold (00:54-01:23Z). The control's second miss (612, 01:04Z) already fixed the verdict under rule 1, so the W6a arms for 612-615 were not run. No run was discarded. Every completed run is in `probes/n2/results/`.

### What seed 611 shows (n = 1, D1, descriptive only, not a verdict)

| arm | post disc4 / k (current space) | S2: same head, reference space | (e) late growth max | test-set norm x | PR | stored-z staleness (retained / on-policy) |
|---|---|---|---|---|---|---|
| frozen | 0.417 / 10 | 0.417 / 10 | 1.064 | 1.00 | 1.30 | 0 / 0 |
| reencode | **0.520 / 10** (twin 0.133 / 0) | 0.230 / 0 | **1.236** | 8.94 | 1.30 -> 7.45 | 0.94 / 0.31 |
| stored | **0.257 / 0** (twin 0.290 / 0) | 0.363 / 0 | 1.498 | 8.84 | 1.30 -> 7.75 | 0.93 / 0.33 |

- **Re-encode tracked the moving encoder on this seed.** 600 W6a updates moved `world_obs_encoder` by 1.44x its norm, scaled the sensed test-set z_world 8.9x and raised PR 1.3 -> 7.5. The W3 head, replaying raw obs re-encoded through the current path, still discriminates in the new space (0.520, k 10, above the frozen control's 0.417 on the same seed). It no longer speaks the old space (S2 0.230). Its shuffled twin fails (0.133 / k 0). One leg broke: (e), late per-step growth max 1.236 against the 1.2 bound (median 1.057, t30/t0 2.87 < 5). So the rollout from the new, larger-norm states is less contractive. Whether that recurs is a 1-seed question.
- **Stored replay collapsed the head on this seed.** disc4 0.257, k 0, retention < 0, rollout unbounded (late max 1.50). The retained babbling z were sensed by the untrained encoder and are 0.93 relative-distance from what the current encoder produces for the same observations. Even the on-policy buffer (<= 600 ticks old) is 0.33 stale. The head is trained on a mix of two incompatible latent spaces and reads neither (S2 0.363 / k 0). The non-registered smoke on seed 106 (sec 1 disclosure) showed the same after 200 W6a updates.
- **S1 (scale-normalised) is not the explanation for anything here.** On 611 the per-dimension standardised readout gives the same pass/fail as the primary in all three arms (reencode 0.520 / 10, stored 0.267 / 0). As stated at pre-registration, disc4 and k are invariant to a uniform rescaling, so the 9x scale shift can act only through training. It is harmless under re-encode and fatal under stored-z, and that difference is a staleness effect, not a metric artefact.

### Harm_eval / codec / E1 (D0, reasoned from 611 + code; not measured on those members)

`HarmEvalMember.observe` stores the tick's DETACHED `z_world` (`waking_trainer.py` HarmEvalMember). `CodecMember` stores z_world. `E1Member` replays the agent's own detached experience buffers (W6a record sec 5). All three are the `stored` policy by construction. On 611, stored z went 0.93 stale for babble-age records and **0.33 stale even for records <= 600 ticks old** at 1 W6a update per tick. A bounded-age buffer would therefore have to be much shorter than the default `waking_trainer_buffer_max` 2000 to stay near current. That shrinks the harm_eval head's rare-positive sample count, which it cannot afford. **Reasoned recommendation: all three need the raw-obs re-encode policy (as W3 has), not bounded age**, or W6a must be phased so the encoder is frozen while they train. This is reasoned from one seed and code (D0/weak D1). It is not a measured result about those heads.

### What would decide N2 (the next action; an orchestrator call)

Re-run **the same pre-registered design at the W3 dose (post 1200, 9600 W3 updates, ~1200 W6a updates)**, with no change to the rule. The Mac cost is ~45 min per seed (P2): ~13 min per `reencode` run, ~6 min per `stored` run. That is a **cloud-worker** job, or a Mac job only with a reserved multi-hour lock window. The probe takes `--post`; `run_seed.sh` needs only `--post 1200`. To reuse seeds 611-615, pre-register the dose change as an amendment first. Seed 611's arm-2/arm-3 split (0.520 vs 0.257) predicts HOLDS-REENCODE with an open question on (e). It is one seed at a reduced dose and is not credited as the answer.

### Evidence domain reached

**D1.** Head discrimination on held-out data in the encoder space it is consumed in, plus measured latent staleness. No E3 consumer or behaviour reading (N3 / W4 / A1).

### Landing

- Pre-registration `025fc6a5cfe` (before any registered seed). This results section is appended in a separate commit, with the result JSON/logs, `summarize_n2.py` and `results/summary.txt` under `probes/n2/`.
- Plan sec 2 N2 row updated (status + one-line result). Nothing else in the plan changed.
