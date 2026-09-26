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

**Status: FINAL over N=15 (reduced from the pre-registered 20; DOSE probe run on 4 of the pre-registered 5 seeds).** Both reductions are the pre-registered cost/stop-rule exercised, not a change to the recipe or the predictor list -- stated here, not silently. Written 2026-09-26T04:16Z. Code sha `1b013d613b3e00fc7fbf8bd414dca1cb1d388308` (tag `archive/coupled-loop-repair-1b013d6`, unchanged from pre-registration). Bug found and fixed before any DOSE-probe seed ran (does not affect the 15 main-sweep results, which never take the cache path): the `--b0-cache` loader in `probes/w3rel/w3rel_probe.py` read `b0c["B0"]["disc4_h1"]`, but the cache file stores `B0` as a bare float; fixed to `B0 = b0c["B0"]`.

**Seeds run: 901-915 (15 of the pre-registered 901-920).** Reduction reason: seed cost varies far more than the pre-registration's smoke estimate (~4.5-5 min/seed) predicted -- a hazard-trapped seed's B0 recompute (`gen_POL`) and post-phase both cost much more per step (many early episode terminations -> many `env.reset()` calls): seed 901 alone took 714s vs the smoke's 124s at a 6x smaller post. Observed range 137s-714s per registered-seed real-arm-plus-B0 cost; average ~300s. At the observed rate, 20 seeds plus a 5-seed DOSE probe would have exceeded the ~2h probe budget and left no room for write-up inside the session's ~3h cap; stopped at 15 main-sweep seeds + 4 DOSE seeds instead.

### Pass rate

| N | pass | pass rate | Wilson 95% CI |
|---|---|---|---|
| 15 | 9 | 0.600 | [0.357, 0.802] |

(Clopper-Pearson exact CI not computed: scipy unavailable in this environment; Wilson is the pre-registered primary interval.)

**Every one of the 15 seeds hit k=10 on the real arm** (the reference-encoder discrimination test's full mark count); the pass/fail split is decided entirely by the disc4_h1 >= 0.47 threshold, exactly as W3/N2/N3 already found ("k = 10 in every row, so the bar is decided by disc4"). Guard PASS 15/15, FROZEN-retained-unchanged 15/15, rollout (e) bounded 15/15 -- no anomalies to report.

### Predictor separation (Cohen's d, pass-group mean minus miss-group mean; threshold |d| >= 0.8)

| predictor | pass mean | miss mean | d | separating? |
|---|---|---|---|---|
| **B0 disc4** | 0.3278 | 0.2706 | **1.227** | **YES** |
| INIT disc4 | 0.2522 | 0.2539 | -0.089 | no |
| babble entropy | 1.6071 | 1.6077 | -0.245 | no |
| babble stay-share | 0.1897 | 0.1949 | -0.561 | no |
| babble wall-push share of moves | 0.2475 | 0.2448 | 0.136 | no |
| post entropy | 0.7439 | 0.5482 | 0.532 | no |
| post stay-share | 0.0894 | 0.1268 | -0.191 | no |
| post wall-push share of moves | 0.8059 | 0.8181 | -0.088 | no |

**B0 disc4 is the one separating predictor**, and it is available BEFORE the babbling/pre/post phases even run (it needs only a 2400-step native rollout + 3000-update head fit, ~85-300s depending on hazard stratum). A seed whose on-policy-data head already discriminates somewhat better than average is more likely to end up over the bar after the W3 member's own babbling+replay training. This is descriptive (d=1.23 on 9 vs 6 seeds) -- not causally tested here; a held-out replication or a B0-conditioned re-sample would be the next step, not run here (scope).

**N5's untested wall-push hypothesis is NOT supported by this predictor list.** Neither babble-phase nor post-phase wall-push share separates pass from miss (|d| < 0.15 both). Action entropy and stay-share also do not separate. This does not resolve N5's mechanism claim about WHY the on-policy stream carries little map information (that was about within-run signal quality for a shift-detection gate, a different question) -- it says only that the STATIC pre-registered summary statistics of the babble/post action distribution do not predict THIS gate's pass/fail across seeds.

### A1 hazard stratum (from this run's own post-phase `done` flags, no extra rollout)

| stratum | n | pass | rate | Wilson 95% CI |
|---|---|---|---|---|
| hazard_trapped | 5 | 4 | 0.800 | [0.376, 0.964] |
| benign | 10 | 5 | 0.500 | [0.237, 0.763] |

Intervals overlap substantially -- **not called separating** under the pre-registered non-overlap rule, despite the point-estimate gap (0.80 vs 0.50). N=15 is too small to resolve this; more seeds would be needed. Directionally consistent with N2's finding that hazard-trapped seeds banked more gain over the W3 dose (both 611-615 hazard-trapped seeds and this sample's hazard-trapped seeds show higher post-disc4 on average), but not established here at a pre-registered confidence level.

### DOSE probe (report-only; post=2400, real arm only, cached B0/INIT; 4 of the 5 planned seeds -- 910 not run, time budget)

| seed | post=1200 disc4 (miss) | post=2400 disc4 | post=2400 gate (a) | reading |
|---|---|---|---|---|
| 901 | 0.4567 | 0.4933 | **PASS** | dose-limited: recovers with more post-phase training |
| 903 | 0.3900 | 0.4667 | miss (closer: 0.0033 short) | partially dose-limited: improves but does not clear the bar in 2x the steps |
| 906 | 0.4567 | 0.4833 | **PASS** | dose-limited: recovers |
| 909 | 0.4333 | 0.4333 | miss (unchanged to 4 decimal places) | NOT dose-limited: doubling post steps does not move this seed at all |

**2 of 4 misses are dose-limited (recover fully by post=2400), 1 is partially dose-limited (closes most of the gap but not all), 1 shows no dose response.** So a fixed post=1200 dose materially undercounts the recipe's reliability ceiling -- at least some of the 40% miss rate at post=1200 is an artifact of the fixed dose, not a property of the seed. But it is not the whole story: seed 909's flat non-response rules out "just train longer" as a universal fix. The dose-response is seed-dependent, and this probe (N=4) is far too small to say what fraction of misses are dose-limited in general.

### Reading (what this changes, what it doesn't)

- The W3 member gate as currently specified (post=1200, fixed threshold 0.47) has a real per-seed miss rate, plausibly ~30-45% (Wilson CI [0.36, 0.80] on this N), not the ~20% (4/5) the original 5-seed W3 record suggested. That record's own seeds (106-110) were not randomly representative of this rate by chance, or the 5-seed W3 sample was favourable; either way, downstream consumers (N3, N5, any future A1 work built on "the W3 head reliably clears the bar") should treat a single fresh seed's pass as ~60% likely, not close to certain.
- B0 disc4 (a cheap, pre-training-outcome signal) is a real, if modest-N, predictor of which seeds will pass -- useful for a future design that wants to screen seeds or understand WHY some fail, but not evidence of a mechanism (D1 only; no intervention performed on B0 itself).
- The dose finding says the fixed post=1200 gate threshold conflates "will never reach 0.47 under this recipe" with "would reach it given more on-policy steps" -- a genuine ambiguity in what a single-dose PASS/FAIL means for reliability claims built on this gate.
- Nothing here touches E3, consumption, or behaviour (still D1). This is upstream of N3/W4/A1 exactly as scoped.

Probe scripts: `probes/w3rel/w3rel_probe.py`, `probes/w3rel/analyze.py`. Raw results: `probes/w3rel/results/` (not committed alongside -- see close note; scratch copy at `.scratch/breakthrough-20260924/w3rel/results/`).
