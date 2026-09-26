# W3 reliability sweep: how reliably does the W3 L2R-bar recipe pass over fresh seeds, and what predicts a miss? (probe only, pre-registration)

- **Status: PRE-REGISTERED, committed BEFORE any registered seed runs.** Session `bt0926-w3rel` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260926-w3-reliability-sweep`. Written 2026-09-26T02:16Z.
- **Plan of record:** upstream of `coupled_loop_repair_campaign_plan.md` sec 3 W3 / sec 4 N3, N5. This probe does not change the W3 member gate; it measures the gate's own reliability across fresh seeds and looks for cheap pre-training predictors of a miss.
- **Code:** ree-v3 tag `archive/coupled-loop-repair-1b013d6` (W3 `7428da3` + W6a `9b322d5` + W4 `1b013d6`; W4 is not exercised here), throwaway detached worktree `.scratch/breakthrough-20260924/w3rel/ree-v3-wt`. **No `ree_core` edits.**
- **Recipe reused byte-identically** from `probes/w3/w3_l2r_member_probe.py` (bt0925-w3): babbling-probe env (`CausalGridWorldV2` size 12, Phase-0 kwargs, new env per 200-step episode), `build_B` agent (world_dim 32 = deployed, alpha_world 0.3), held-out test set (3000 uniform-random {0..3} steps, k = 120..134), `evaluate()`. W2a `StructuredBabbler` (5 classes incl. stay, runs {1..4}, seed `S*13+1`) over Phase-0 episodes k = 0..11 into the FROZEN retained set (~2280-2290), 3000 member updates (pre phase), then **post = 1200** native closed-loop `StepHarness` steps (k = 50..55), member source `on_policy`, **8 member updates per step** at the 25% retained mix, re-encoded. SHUF twin: retained babbling actions relabelled by the FIXED permutation [1,2,3,4,0]. Probe script: `probes/w3rel/w3rel_probe.py` (adds instrumentation only; the trained-object construction, hyperparameters and update loop are unchanged from `w3_l2r_member_probe.py`).
- Evidence domain targeted: **D1** (does a natively-trained head clear a fixed discrimination bar on held-out data, and how often). No E3/behaviour claim (D2/D3) -- that is N3/W4/A1.

## 1. Premises re-measured before registering

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | the W3 recipe is reproducible on fresh seeds without drift | smoke run seed 9001 (not a registered seed; post=200, tiny) reproduced the same code path end to end: member built, guard PASS, FROZEN retained set intact, disc4/k/retention/rollout all computed. Not a registered result (`results/SMOKE_s9001.json`) | holds |
| P2 | the A1 hazard stratifier (`experiments/_lib/coupled_acceptance.classify_stratum`) is cheap from this run's own instruments | it reads only this run's post-phase `done` flags (window=600 of the 1200 post steps already run) -- no extra rollout | holds, used as the stratifier (see sec 2) |
| P3 | B0 needs a per-seed recompute (no published B0 exists for fresh seeds) | confirmed: `babble_probe`'s published `BAB_s*.json` covers only seeds 106-110. Recompute uses the same recipe N2 used (`babble_probe.gen_POL(seed, n_eps=12, 25)` -> `encode_segs` -> `train_head` 3000 updates), which N2 validated reproduces the published B0 exactly on seed 106 (`n2_replay_encoder_probe_20260925.md` P3) | adopted verbatim |

## 2. Design (fixed before any registered seed runs)

**Seeds (fresh, 20):** 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920. Checked against every committed probe seed list found by grep in `evidence/planning/`: not 106-110 (W3/babble), 531-535 (N3), 611-615 (N2 reduced-dose), 721-725 + 799 (N5), 811-815 (N2 amendment A1 full-dose / N2q).

**Per seed, one process (`probes/w3rel/w3rel_probe.py`):**
1. Fresh reference build (`build_B(seed)`, frozen random-init encoder), held-out test set, INIT disc4/k (untrained head).
2. **B0** (recorded before training outcome is known): `babble_probe`'s own on-policy-data head, `gen_POL(seed, n_eps=12, offset=25)` (2400 native waking steps) -> `encode_segs` -> `train_head` (3000 updates). Also yields `hazard_class_babble` (benign/hazard-trapped by `babble_probe`'s own POL-based rule, reported alongside the A1 stratifier below -- these are two different classifiers and are NOT conflated).
3. **real arm:** babbling (2400 steps) -> FROZEN retained set -> 3000 member updates (pre) -> 1200 native post steps, 8 updates/step, 25% retained mix, re-encoded -> `evaluate()` (post disc4/k/disc5).
4. **shuf arm:** identical, with the retained babbling actions relabelled by the fixed permutation before the pre-phase updates (the W3 gate's twin).
5. Recorded **during** both arms, before the post-phase outcome is read: babble-phase and post-phase action-class distribution (5 classes: 0-3 move, 4 stay) -- `entropy` (`babble_probe.entropy`, natural-log Shannon entropy over the 5-class counts), `stay_share` (fraction of steps that are class 4), `wallpush_share_of_moves` (fraction of non-stay steps where `env.agent_x, env.agent_y` is unchanged after the step -- a blocked/no-displacement move; N5's untested hypothesis, `n5_ach_gated_unfreeze_probe_20260926.md` sec 4.2).
6. **A1 hazard stratum** (`experiments/_lib/coupled_acceptance.classify_stratum`, `window=600, early_len=200, min_early=10`), read from the run's OWN post-phase `done` flags (first 600 of the 1200 post steps) -- no extra rollout, cheap by construction.
7. Guard PASS/FAIL, FROZEN-retained-unchanged check, rollout (e) (t30/t0, late per-step growth) -- same instruments as the W3 gate, reported not gated (see below).

**Gate read per seed (real arm only; the W3 gate definition, unchanged):** pass iff post disc4_h1 >= 0.47 AND k == 10. Guard PASS and FROZEN-intact are asserted (not part of the pass/fail read; a violation on any seed is reported as an anomaly, not silently folded into a miss).

**Predictors (pre-registered list, fixed before any registered seed; no post-hoc addition):**
1. B0 disc4
2. INIT disc4
3. babble-phase action entropy
4. babble-phase stay-class share
5. babble-phase wall-push share of moves
6. post-phase action entropy
7. post-phase stay-class share
8. post-phase wall-push share of moves
9. A1 hazard stratum (hazard-trapped vs benign)

**Analysis (fixed before any registered seed):**
- **Pass rate**: k/20 with a **Wilson score 95% interval** (continuity-uncorrected), reported alongside the plain Clopper-Pearson exact interval for comparison.
- **Predictor separation**: for predictors 1-8 (continuous), Cohen's d (pass-group mean minus miss-group mean, pooled SD) plus the raw group means; for predictor 9 (categorical), pass rate within each stratum with its own Wilson interval. **A predictor is called "separating" only if |d| >= 0.8 (large, Cohen's convention) or the two strata's Wilson intervals for predictor 9 do not overlap** -- fixed thresholds, not tuned after seeing the data. If the miss count is 0 or 20 (no variance in the outcome), predictor separation is reported as **CANNOT_DETERMINE** for that predictor (a group of size 0 has no mean/variance to compare), not silently as "no effect".
- **DOSE probe (report-only, not part of the pass-rate verdict):** of the seeds that MISS gate (a) at post=1200, the FIRST 5 in seed order are re-run with **post=2400** (real arm only, same B0/INIT cached from the post=1200 run, everything else identical) to see whether the miss is dose-limited (recipe unchanged; N2 showed the symmetric result that cutting post from 1200 to 600 breaks the control's pass rate 4/5 -> 1/5, `n2_replay_encoder_probe_20260925.md` sec 3). If fewer than 5 seeds miss, all missing seeds get the dose probe. If zero seeds miss, the dose probe is skipped and that is stated (not a violation of pre-registration -- the probe's own condition did not obtain).

## 3. Cost / stop rules

Smoke (seed 9001, post=200, not registered): B0 ~83s, real arm (pre+post+rollout) ~19s, shuf arm ~19s -> ~124s total. At post=1200 (registered dose), the real/shuf arms are the dominant cost (the original W3 gate measured ~93s per arm at this dose with no B0 attached); expected **~4.5-5 min per seed** (B0 ~85s + real ~95s + shuf ~95s). For 20 seeds: **~1.5-1.7h** of Mac wall, batched at up to ~3 seeds (~15 min) per lock hold with a 45s pause between holds, under `mac_probe.lock` (>= 800 MB free+inactive checked before each acquire, 2 torch threads). The DOSE probe (5 seeds, real arm only, post=2400, B0/INIT cached) is expected to add **~15-20 min**.

**If the ~2h probe cap is reached before all 20 seeds complete, the seed count is reduced (not the recipe or the predictor list), and this is stated in the results section below as INTERIM over N < 20 seeds, never silently.**

## 4. Results

*(to be appended after the registered seeds run; this section is empty at pre-registration commit time)*
