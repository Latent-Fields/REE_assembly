# Probe C: commit-gate discrimination -- signal validity (C0), operating point (C1), escape evidence (C2)

- **Status: DONE (S1, 5/5 seeds; S2 cut, addendum 1b).** Verdicts: **C0 `neither = H-SV` (registered rule; STOP)**, **C1 `CANNOT_DETERMINE` (C0 stop)**, **C2 `CANNOT_DETERMINE`** (no exposure reference separates on >= 4/5). Domain reached **D1** (C2 clamp contrasts are D2 on what evidence arrives, descriptive only). Sections 0-1 were committed before any registered seed (`4d9980b439`), addendum 1b before any DV was read (`e8edf4c68a`); results are sec 2-4.
- **Session:** `bt0926-cgdisc` (orchestrator `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dcd2-commit-gate-disc`. Written 2026-09-26T14:47:15Z (pre-registration).
- **Spec:** `dynamic_control_discrimination_plan_20260926.md` (41cfe94841) sec 2 Family C, sec 3 rows C0/C1/C2, sec 4.1. Inputs read in full: `commit_gate_read_int_vs_native_20260926.md` (a417b6f578), `dynamic_control_audit_20260926.md` sec H1 (e3cafebab3), `n5_ach_gated_unfreeze_probe_20260926.md` (b26d8e8d9d).
- **Code under test:** `ree-v3` `4070b0efa4` (tag `archive/coupled-loop-repair-4070b0e`, the `integration/coupled-loop-repair` line: W3 E2WorldMember + W6a + W4), private detached worktree `.scratch/wt-cgdisc`. **No `ree_core` edits and no commits to ree-v3.** The realised-error signal, every alternative bar, the policy clamps, the probe actions and both world changes are probe-side (`StepHarness` hooks and an env proxy). Every file:line below is on this sha.
- **Probe:** `probes/cgdisc/cg_probe.py` (one process = one seed), analysis `probes/cgdisc/cg_analyze.py`. Mac, 2 torch threads, under the shared `mac_probe.lock` (acquired before any compute; one hold for S1, one for S2; release verified).
- **Evidence domain reachable:** D1 for C0 and the offline C1 bars (the quantity exists, moves, separates); D2 for the C2 clamps (the gate/policy intervention changes what the native E3 selector executes and what evidence arrives). No reward/outcome reading (D3 is not attempted: E3 valuation is at chance before W5).

## 0. Premise audit (re-measured on 4070b0efa4 before registering)

| # | premise (brief) | re-measured | verdict |
|---|---|---|---|
| a | rv's raw input has mixed semantics by k = ticks since the last E3 tick | D0: `REEAgent.update_residue` passes `self._current_latent.z_world` (the PRE-step latent of this tick) to `E3TrajectorySelector.post_action_update` (`agent.py:12218-12223`); there `predicted_world = ref_trajectory.world_states[1]` with `ref_trajectory = self._committed_trajectory or self._last_selected_trajectory` and `prediction_error = actual_z_world - predicted_world` (`e3_selector.py:5020-5024`). So k=0 (E3 tick): z_t vs E2's prediction of z_{t+1} from z_t = predicted displacement; k=1: z_{t+1} vs that prediction = a real one-step error of the E3-tick action; k>=2: stale. D1: measured per life in sec 3 (bucketed raw input vs the probe's realised error on the same ticks) | D0 holds; D1 in sec 3 |
| b | rv is never reset per episode | D0: no reset of `_running_variance` in `E3TrajectorySelector`; D1: `agent.reset()` leaves it unchanged (probe logs before/after on every seed) | D0 holds; D1 in sec 3 |
| c | the 0.40 crossing is init-set (precision_init 0.5, alpha 0.05) | D0: `commitment_threshold 0.40`, `precision_ema_alpha 0.05`, `precision_init 0.5` (`config.py:1308-1310`); gate `committed = commit_variance < effective_threshold` (`e3_selector.py:4318-4328`). 0.95^4 x 0.5 = 0.407, 0.95^5 x 0.5 = 0.387. D1: rv over the first native ticks of each seed's S1 dose | D0 holds; D1 in sec 3 |
| d | the ARC-029(D) bar's q / window are raise-if-unset sentinels | D0: `commit_threshold_quantile = -1.0`, `commit_threshold_quantile_window = -1` (`config.py:1600-1601`); `_build_commit_gate_window` raises `ValueError` unless 0 < q < 1 and w >= 2 (`e3_selector.py:873-910`). D1: the probe arms the lever on a default config and records the raise | D0 holds; D1 in sec 3 |

Also re-measured: the estimator is `exp(trend_now + quantile_q(residuals of a least-squares line on log(v) over the window))`, strictly causal (the current tick is appended AFTER the decision), and it returns `None` (absolute bar in force) during warmup or on a degenerate window (`e3_selector.py:912-1024`). The probe reuses this method verbatim on its own series (a stub carrying only `_commit_gate_variance_window` and `config.commit_threshold_quantile`), so the OWN bar is the native estimator, not a re-implementation.

## 1. Design (pre-registered)

**Development (per seed), the W3 member protocol exactly as N5 phase 1:** `build_B` agent (`world_dim` 32 = deployed, `alpha_world` 0.3), **all four reset-init knobs ON** (`use_{zworld,zself,shared,zharm}_ema_reset_init`, set on `config.latent` and the latent stack's config before any tick), `E2WorldMember` (lr 3e-4, batch 32, MSE, grad_clip 1.0, retained 5000, `reencode`), W2a babbling 2400 steps -> FROZEN retained set, 3000 member updates, then the native closed-loop dose.
- **Stage S1 = the W3 standard dose:** 1200 native `StepHarness` steps x 8 member updates (25% retained mix).
- **Stage S2 = a longer dose:** S1 continued by 1200 more native steps x 8 updates (2400 native steps total, 2x). Run on 3 seeds only -- **763, 764, 765** (held-out seeds, so the S2 set tests seed AND stage transfer) -- the brief's first budget cut, taken up front (sec 1a). If the Mac budget runs out, S2 is cut from the last seed backwards and the S2 set is reported with its actual n, never silently.
- **Pre-screen (W3 disc4):** W3 member gate (a) on the W3 held-out test set, `disc4_h1 >= 0.47` (the 4070b0e contract: disc4 alone, k a readout), read at the end of S1.

**Seeds.** Five fresh seeds, registered in this order: **761, 762, 763, 764, 765** (not 0-2, 106-110, 531-535, 611-615, 721-725, 790, 799). The W3 disc4 pre-screen is **recorded, not used to drop seeds** (screening replacements until 5 pass would cost ~15 min of Mac per failing candidate at the current load, and W3's recipe passes ~50%; sec 1a). Every verdict is computed on all 5 AND, separately, on the screen-passing subset; where they differ, both are reported and the all-5 verdict is the registered one. **Tuning seeds = 761, 762; held-out = 763, 764, 765.** (Calibration seed 790 was a code/timing smoke only, sec 1a.)

**Test lives.** From the S1 (and later S2) snapshot, each life is **one continuous life** of 330 ticks in a fresh 12x12 phase-0 env (`max_episode_steps` 430, so no step-cap boundary). **Health is pinned at 1.0 around every env step** (probe-side, every life), so no life ends in death; hazard contact still delivers its harm signal. (The functional smoke's scripted-random lives died twice in 60 ticks without this.) A `done` that still occurs is logged, reset, and the 8 ticks after it excluded. **Trainer frozen during a life** (no member updates; E2 fixed), so after a change the model stays wrong and the only question is whether the signal and gate see it. Env seed, torch/numpy RNG and probe RNG are identical across every life of a (seed, stage), so a change life and its no-change life are identical up to the change tick.
- **Hidden change at tick 200** (scoring only; no controller reads it):
  - `perm`: the N5 action-map derangement (`SHIFT_P = [2, 3, 1, 0]` over the 4 move classes, stay unchanged) written into `env._action_map` mid-life;
  - `layout` (the second kind): implemented (`relayout()`: every hazard and resource moved to a fresh random empty interior cell mid-life, no reset) and exercised in the smoke, but **cut from the registered run** under the brief's second budget cut (sec 1a).
  - `none`: no change (the null life for every AUROC).
- **Policy clamps** (probe sets `e3.config.commitment_threshold` each tick before `select_action`: 1e9 -> committed, -1 -> uncommitted; the modulations are multiplicative, so neither can flip):
  - **NAT** native gate (rv vs 0.40); **FC** forced committed (argmin); **FS** forced sampling (softmax); **CP** forced committed + probe actions: on each tick with probability 0.05 the executed action is replaced (env proxy) by a uniform random move class, the agent's selection untouched;
  - **RND** (added after the calibration, sec 1a): gate forced committed, but EVERY executed action replaced by a uniform random move class -- the evidence-available reference (the Family F plan's scripted-diversity reference, applied here). The agent still senses, selects and updates rv every tick, so both inputs are defined;
  - (an OWN closed-loop arm -- the realised-input own-scale bar driving the gate -- is implemented in the script and exercised in the smoke, but **not run**: no verdict depends on it and it did not fit the budget; C1 is evaluated offline.)
- **Signals logged every tick:** `RAW_MIX` = rv's raw input (`e3_prediction_error`), `EMA_MIX` = rv; `RAW_REAL` = realised one-step error `mean((z_{t+1} - E2.world_forward(z_t, a_t))^2)` for the action actually executed at t (logged at t+1, when it exists), `EMA_REAL` = its EMA at rv's own alpha (0.05).
- **Lives run:** S1: RND, NAT, CP, FS x {perm, none} (8 lives per seed); FC x {perm, none} on seed 761 only, to verify FC == NAT when the native gate is committed on every tick (same RNG, and every committed decision identical -- byte-identical traces in the smoke), after which NAT stands in for FC on every seed where NAT's committed fraction is exactly 1.0 (else C2 is CANNOT_DETERMINE for want of an FC arm). S2 (seeds 763-765): RND, NAT x {perm, none}. Both budget cuts (S2 to 3 seeds, layout kind) are taken up front; no control is cut.

**Exclusions (every DV):** ticks 0-59 of every life (3 EMA time constants at alpha 0.05) (covers the EMA / policy-switch transient; rv itself carries over from development, so the precision_init decay window lies in the development phase -- it is measured there, premise c) and 8 ticks after any env reset.

**Windows:** pre = ticks [60, 200); post = [201, 200+K] with K = 50 (C0, C1) and K2 = 120 (C2).

### C0 signal validity
- Per (seed, stage, policy, kind, signal): A = AUROC(post vs pre) in the change life; A_null = the same windows in the no-change life; D = A - A_null. **A signal separates on a seed iff A >= 0.70 and D >= 0.15.** An input (mix = RAW_MIX or EMA_MIX; realised = RAW_REAL or EMA_REAL) separates on a seed if either form does.
- **Primary cell: RND, S1, perm** (diverse executed actions make the evidence available by construction; the native loop's hiding of it is C2's question, not C0's -- FS was the planned primary but did not diversify executed actions in the calibration, sec 1a). An input separates iff it separates on >= 4/5 registered seeds.
- **Verdict:** realised separates and mix does not -> `SEPARATES-realised-only`; both -> `both`; mix only -> `mixed-only` (reported as such); neither -> **`neither = H-SV`, STOP** (C1/C2 not interpreted; route E2/W3).
- Reported, not verdict: A_pair = AUROC of the change life's post-window values against the no-change life's values at the same ticks (the lives are identical before the change, so this isolates the change's effect on the signal); hit-FA (hit = any post-window value above the pre-window 99th percentile; FA = fraction of disjoint 50-tick pre-windows with an exceedance), all other cells (FS, NAT, CP), S2.

### C1 operating point (only on an input that separates in C0; the EMA form, as the native gate reads rv)
- Offline decisions on the RND lives (the C0 primary cell; D1): uncommitted iff x >= bar.
- **Bars:** ABS 0.40; **FIXED-TUNED**: grid = quantiles {0.50, 0.75, 0.90, 0.95, 0.99, 0.999} of the pooled pre-window values of the two tuning seeds at S1 (RND-perm); choose the grid bar maximising mean appropriateness over the tuning seeds (tie -> the higher bar); **freeze it**; **OWN**: native ARC-029(D) estimator, q 0.90, window 60 ticks (3x the EMA time constant, per the estimator's own guidance), strictly causal, warmup -> 0.40.
- **Appropriateness** = P(uncommitted | post K window) - P(uncommitted | pre window). False de-commit = P(uncommitted | pre) and P(uncommitted | the same post window of the no-change life). Occupancy reported; under OWN it is ~q by construction and is **never a DV**.
- **Controls:** RANDOM = Bernoulli commitment matched to OWN's occupancy (1000 draws; p95); SHUF = the OWN rule on a time-permuted copy of the input (the brief's "time-shuffled input"); SHUFBAR (report only) = true input vs a bar from the permuted history (the audit's arm D); ORACLE = 1.0.
- **Criterion** crit = max(0.20, 0.5 x A_tune). On an evaluation set (HO-S1 = the 3 held-out seeds at S1; S2 = all seeds run at S2), a bar **keeps** appropriateness iff it reaches crit on >= ceil(2n/3) seeds. OWN **beats controls** iff A_OWN > A_SHUF + 0.15 and A_OWN > RANDOM p95 on >= ceil(2n/3) seeds.
- **Verdict:** A_tune < 0.20 -> `CANNOT_DETERMINE` (no fixed bar is appropriate even in-sample, transfer untestable). Else `H1 SUPPORTED` iff on some set FIXED loses AND OWN keeps AND OWN beats both controls; else `H1 WEAKENED` iff FIXED keeps on every set run (a tuned bar that transfers weakens H1); else `CONTENT-BLIND` iff OWN beats controls on no set; else `CANNOT_DETERMINE (mixed)`.

### C2 escape evidence (S1, perm, K2 = 120)
- DV per clamp: D_all = A - A_null of RAW_REAL over all scored ticks; for CP also **D_probe** over the probe-evidence ticks only (the tick after each probe action), and FC scored on the same tick positions (so a CP win is the probe, not the position).
- **Exposure reference X** = FS if FS separates on >= 4/5 seeds, else RND (labelled in the result; the brief's comparator is FS, and RND replaces it only if sampling itself exposes nothing).
- **Verdict:** X fails to separate on >= 4/5 -> `CANNOT_DETERMINE` (no evidence even with diverse actions: that is H-SV, already C0's stop); FC separates on >= 4/5 AND FC's D >= X's D - 0.10 on >= 4/5 -> **`H2 NOT-NEEDED`**; FC fails on >= 4/5 AND CP's probe-tick detection separates on >= 3/5 -> **`H2 SUPPORTED`** (commitment occupancy is unchanged by construction; executed actions differ from selections on ~5% of ticks, reported); else `CANNOT_DETERMINE (mixed)`. With ~7 probe-evidence ticks per window the per-seed CP test is noisy (with ~6 vs ~7 ticks, a null seed reaches A >= 0.70 with probability ~0.10 by the normal approximation, before the null-life D requirement); a pooled cross-seed rank test is reported alongside, not as the verdict.
- Reported per arm: executed-action entropy (bits over 5 classes) pre and post (Q-111's action-diversity precondition), commitment occupancy, the mix-input version of every C2 cell.

### Noise bands and margins (all fixed here)
Separation A >= 0.70 and D >= 0.15; C1 crit max(0.20, 0.5 x A_tune), control margin 0.15 and RANDOM p95; C2 FC-vs-FS closeness 0.10. Seed-count rules as stated above.

### 1a. Calibration disclosure
Seed 790 (not registered) was run twice before registering: (i) a timing smoke with a reduced development phase (1 babbling episode, 300 updates, 200 native steps) and the original 660-tick lives; killed after two lives; (ii) a functional smoke of every arm at 60-tick lives. What they changed, before any registered seed:
- **FS does not diversify executed actions.** Forced sampling executed move class 1 on 628/660 and 620/660 ticks (FS-perm / FS-none; histogram [0, 628, 0, 31, 1]): softmax sampling over this agent's candidate set yields almost the same first action. So FS cannot be the "evidence available by construction" cell -> the RND arm was added and made the C0 primary cell and the C1 evaluation cell. (The smoke's agent was under-developed; whether the registered agents' FS diversifies is measured and reported per seed.)
- **Cost.** 81-86 s per 660-tick life and 68 s per 200 dose steps (0.34 s per dose step), under a Mac load average of 33-46 on 8 cores (four other-worker processes running outside the probe lock at the time); scripted-random lives cost ~2-4x a native life. The full factorial as first drafted (~53 min per seed) does not fit the 2.5 h cap -> lives shortened to 330 ticks (change at 200, 60-tick exclusion), S2 cut to 3 seeds and to 1200 extra steps (2x rather than 3x), the layout kind cut, the OWN closed-loop arm not run, FC run on one seed only to verify FC == NAT, and the pre-screen made a recorded covariate rather than a seed filter.
- **Death.** The scripted-random lives hit health depletion twice in 60 ticks -> health pinned (above).
- **FC == NAT.** In the smoke the FC and NAT lives were byte-identical in raw_mix, rv, raw_real, executed actions and committed state.
- Also confirmed in the smoke: premise d (the lever raises with the default q = -1.0) and premise c (rv 0.475, 0.451, 0.429, 0.407, 0.387 on the first five native ticks of a fresh agent: first below 0.40 at index 4).

### 1b. Addendum (budget cut, registered 2026-09-26T15:10:17Z, while seed 761 was mid-run; no result had been read)

- **Measured cost on seed 761:** the S1 dose (1200 native steps x 8 updates) took **975 s** (0.81 s per step; N5 measured ~0.07 s per step for the same protocol on a quiet machine). At that rate each seed's development alone is ~17 min and one S2 dose another ~16 min, so the registered plan (5 seeds at S1 + S2 on 3) needs well over the 2.5 h cap, before counting the lock time shared with `bt0926-h0`.
- **Cut, taken now:** **S2 is dropped on all seeds** (the brief's first cut, taken to its end). Consequence, stated in advance: C1's stage transfer is untested; C1 is decided on the HO-S1 set only, so the best C1 verdict available is about **seed** transfer at S1 (e.g. "H1 WEAKENED (HO-S1 only)"), and "stage transfer" is reported CANNOT_DETERMINE. No control, arm, window, margin or rule changes.
- **Stop rule:** seeds run in registration order (761 -> 765). If the cap is reached first, the verdicts are reported over the seeds completed, labelled **INTERIM**, with the seed-count rules applied to the completed n (>= 4/5 becomes >= ceil(0.8 n); >= 3/5 becomes >= ceil(0.6 n)), never silently.
- **Lock hygiene (no effect on results):** from seed 762 the process also rotates the lock between dose episodes (max hold 600 s + one episode), because seed 761's development phase held it ~18 min in one piece, over the 15 min limit.

## 2. Results (seeds 761-765, stage S1; `probes/cgdisc/cg_probe.py` + `cg_analyze.py`; raw per-seed JSON and logs in `.scratch/breakthrough-20260924/cgdisc/results/`, not committed)

**Plain summary.** A hidden mid-life re-mapping of the agent's four move actions is **not reliably visible** in either error signal, even when the agent's actions are made uniformly random: it separates on 2/5 seeds in the primary cell, by either input. Where the change is visible, the current mixed input (rv's raw input and rv itself) and the realised one-step error see it **together** -- the realised input adds nothing the mixed one lacks. The E2 world head that both signals read predicts the next latent barely better than "nothing changes" (error/persistence 0.97-1.02 at h1 on every seed), which is the likely reason. By the registered rule this is **H-SV: stop here, route to E2/W3.** H1 (bar scale) and H2 (escape evidence) are not testable at this site until the upstream signal carries the change.

### 2.1 Development readouts (pre-screen recorded, not used to drop seeds)

| seed | S1 disc4_h1 (bar 0.47) | k | E2 err / persistence, h1 | rv at snapshot | FS executed-action histogram (perm life, classes 0-4) |
|---|---|---|---|---|---|
| 761 | 0.523 (pass) | 10 | 0.974 | 1.7e-05 | [33, 110, 0, 15, 172] |
| 762 | 0.490 (pass) | 0 | 1.006 | 7.2e-06 | [9, 3, 268, 0, 50] |
| 763 | 0.433 (fail) | 2 | 0.996 | 1.9e-05 | [0, 167, 151, 0, 12] |
| 764 | 0.423 (fail) | 0 | 1.017 | 5.2e-06 | [328, 0, 0, 2, 0] |
| 765 | 0.440 (fail) | 1 | 0.988 | 1.4e-05 | [0, 0, 1, 288, 41] |

2/5 pass the W3 disc4 bar (N5 found 2/5 too). The screen-passing subset (761, 762) gives the same verdicts (sec 3).

### 2.2 Premises, D1 (sec 0 table)

- **(a) Corrected.** rv's raw input is **not** the realised one-step error of the executed action at k = 1, or at any k. Median ratio raw input / realised error in the NAT no-change life, by k = ticks since the last E3 tick (k0 / k1 / k2 / k3 / k4 / k5+): 761: 3.04 / 1.94 / 3.40 / 4.76 / 7.55 / 9.34; 762: 1.94 / 4.59 / 7.08 / 8.92 / 11.17 / 11.94; 763: 1.06 / 1.09 / 1.10 / 1.12 / 1.14 / 1.22; 764: 1.08 / 1.04 / 1.07 / 1.12 / 1.09 / 1.12; 765: 1.12 / 1.23 / 1.33 / 1.45 / 1.52 / 1.61. Agreement within 1% on at most 15% of ticks in any bucket. The growth with k (staleness) is confirmed. The k = 1 mismatch has a D0 reason not in the brief: E3 candidates carry **continuous** action vectors (`generate_random_actions` returns `torch.randn`, `e2_fast.py:858-864`; `hippocampal/module.py:947` "continuous action vectors ... downstream argmax class"), `world_states` are rolled out by `world_forward` under those vectors (`e2_fast.py:830-831`), and the body executes only the vector's class. So `world_states[1]` is E2's prediction for an action vector that is never executed, even one tick after selection.
- **(b) Holds.** `agent.reset()` leaves `_running_variance` unchanged on all 5 seeds (logged before/after).
- **(c) Holds.** A fresh agent's rv on its first native ticks is 0.475, 0.451, 0.429, 0.407, 0.387 on every seed: first below 0.40 at index 4, fully set by `precision_init` 0.5, alpha 0.05 and the bar. After development rv is 5e-6 to 2e-5, so the 0.40 bar sits **4.3-4.9 orders of magnitude** above it (the commit-gate read measured 1-2 orders at a different config: 8x8 env, `alpha_world` 0.05, no W3). The native gate was committed on 100% of ticks in every NAT life.
- **(d) Holds.** Arming the lever on a default config raises `ValueError` ("commit_threshold_quantile is -1.0; it must be set explicitly").
- **FC == NAT** verified on seed 761: byte-identical raw input, rv, realised error, executed actions and gate state in both lives. NAT's committed fraction was exactly 1.0 on every seed, so NAT stands in for FC throughout.

### 2.3 C0: separation (K = 50). Cell entries: A / A_null / D (A_pair); * = separates (A >= 0.70 and D >= 0.15)

| seed | cell | RAW_MIX | EMA_MIX (= rv) | RAW_REAL | EMA_REAL |
|---|---|---|---|---|---|
| 761 | RND | 0.75 / 0.39 / 0.36 (0.82) * | 0.92 / 0.63 / 0.29 (0.94) * | 0.73 / 0.43 / 0.30 (0.81) * | 0.83 / 0.47 / 0.35 (0.98) * |
| 761 | NAT | 0.33 / 0.11 / 0.22 (0.85) | 0.04 / 0.00 / 0.04 (0.95) | 0.37 / 0.08 / 0.30 (0.95) | 0.06 / 0.00 / 0.06 (1.00) |
| 761 | FS | 0.50 / 0.43 / 0.07 (0.52) | 0.63 / 0.78 / -0.16 (0.27) | 0.38 / 0.25 / 0.12 (0.59) | 0.19 / 0.05 / 0.14 (0.62) |
| 761 | CP | 0.74 / 0.29 / 0.45 (0.87) * | 0.75 / 0.15 / 0.60 (0.97) * | 0.67 / 0.33 / 0.34 (0.85) | 0.50 / 0.06 / 0.45 (0.86) |
| 762 | RND | 0.54 / 0.59 / -0.05 (0.44) | 0.40 / 0.52 / -0.11 (0.39) | 0.74 / 0.80 / -0.06 (0.37) | 0.73 / 0.74 / -0.01 (0.41) |
| 762 | NAT | 0.32 / 0.32 / -0.00 (0.47) | 0.14 / 0.12 / 0.01 (0.67) | 0.39 / 0.53 / -0.15 (0.26) | 0.43 / 0.35 / 0.07 (0.63) |
| 762 | FS | 0.59 / 0.62 / -0.02 (0.50) | 0.62 / 0.35 / 0.26 (0.95) | 0.43 / 0.89 / -0.46 (0.14) | 0.88 / 0.83 / 0.06 (0.67) |
| 762 | CP | 0.32 / 0.26 / 0.05 (0.59) | 0.35 / 0.24 / 0.12 (0.73) | 0.40 / 0.38 / 0.01 (0.61) | 0.43 / 0.22 / 0.21 (0.82) |
| 763 | RND | 0.83 / 0.62 / 0.21 (0.80) * | 0.97 / 0.82 / 0.14 (0.96) | 0.82 / 0.59 / 0.23 (0.77) * | 0.99 / 0.87 / 0.12 (0.95) |
| 763 | NAT | 0.87 / 0.29 / 0.58 (1.00) * | 0.87 / 0.00 / 0.87 (1.00) * | 0.89 / 0.17 / 0.72 (1.00) * | 0.91 / 0.00 / 0.91 (1.00) * |
| 763 | FS | 0.99 / 0.80 / 0.20 (0.97) * | 0.93 / 0.33 / 0.60 (1.00) * | 1.00 / 0.95 / 0.05 (1.00) | 0.99 / 0.55 / 0.44 (1.00) * |
| 763 | CP | 0.63 / 0.11 / 0.52 (0.82) | 0.58 / 0.00 / 0.58 (0.96) | 0.71 / 0.20 / 0.51 (0.83) * | 0.62 / 0.04 / 0.58 (0.92) |
| 764 | RND | 0.57 / 0.70 / -0.13 (0.35) | 0.90 / 0.99 / -0.09 (0.07) | 0.57 / 0.63 / -0.06 (0.44) | 0.88 / 0.95 / -0.07 (0.22) |
| 764 | NAT | 0.99 / 0.55 / 0.44 (1.00) * | 0.97 / 0.16 / 0.81 (1.00) * | 1.00 / 0.50 / 0.50 (1.00) * | 1.00 / 0.04 / 0.96 (1.00) * |
| 764 | FS | 0.82 / 0.05 / 0.78 (0.99) * | 0.95 / 0.58 / 0.37 (1.00) * | 0.82 / 0.02 / 0.80 (1.00) * | 0.97 / 0.00 / 0.97 (1.00) * |
| 764 | CP | 0.96 / 0.83 / 0.14 (0.83) | 1.00 / 0.94 / 0.06 (0.91) | 0.98 / 0.70 / 0.28 (0.91) * | 1.00 / 0.90 / 0.10 (0.99) |
| 765 | RND | 0.53 / 0.71 / -0.18 (0.30) | 0.80 / 0.98 / -0.17 (0.13) | 0.69 / 0.72 / -0.03 (0.44) | 0.76 / 0.82 / -0.05 (0.39) |
| 765 | NAT | 0.90 / 0.90 / 0.00 (0.50) | 0.64 / 0.64 / 0.00 (0.50) | 1.00 / 1.00 / 0.00 (0.50) | 0.93 / 0.93 / 0.00 (0.50) |
| 765 | FS | 0.97 / 0.97 / 0.00 (0.50) | 0.99 / 0.99 / 0.00 (0.50) | 0.99 / 0.99 / 0.00 (0.50) | 0.99 / 0.99 / 0.00 (0.50) |
| 765 | CP | 0.76 / 0.86 / -0.11 (0.38) | 0.94 / 0.95 / -0.01 (0.69) | 0.89 / 0.97 / -0.08 (0.11) | 0.99 / 0.99 / 0.00 (0.22) |

Tally, primary cell RND: mix separates 2/5 (761, 763), realised 2/5 (761, 763); need 4/5. **C0 = `neither = H-SV`.** Every other cell is also 2/5 or less for each input (NAT 2/5 each; FS 2/5 each; CP mix 1/5, realised 2/5).

### 2.4 What the pattern says (D1 readings; not verdict-bearing)

1. **No provenance effect.** The realised input never separates where the mixed input fails in the primary cell, and in every cell the two inputs rise and fall together (A_pair for both is high on the same seeds). Swapping rv's raw input for a realised error would not, on this evidence, make the gate information-bearing. The earliest break sits upstream of provenance.
2. **E2 is at persistence.** E2's h1 error is 0.97-1.02 of the "nothing changes" error on every seed, and disc4 is 0.42-0.52 (chance 0.25). A permutation of action labels can only raise the error by as much as E2's prediction depends on the action. Under uniform random actions it did so on 761 (the lowest ratio, 0.974) and 763 (0.996), but not on 765 (0.988), so the ratio alone does not order the seeds; on 762, 764 and 765 the change did not even raise the error at the same ticks of the paired no-change life (A_pair 0.07-0.44). This is the N5 finding (surprise blind to the same shift, 5/5 seeds) reproduced on the E3-side signal.
3. **Where the native loop "sees" the change, it is content-free.** NAT separates strongly on 763 and 764 (rv itself: A 0.87 / 0.97, D 0.87 / 0.81). Both are seeds where the committed loop repeats one move class (NAT entropy 1.0 and 0.34 bits) and the re-mapping turns it into a different displacement, e.g. a blocked move into movement. Any model at persistence level would flag that. On 765 the repeated class stays blocked under both maps and the change and no-change lives are **identical** after the change (A_pair 0.50 on every signal).
4. **Even where rv carries the change, the absolute gate cannot read it.** On 763 and 764 rv rises relative to its own recent past, at a scale of 1e-6 to 1e-5 against a bar of 0.40. That is a scale observation (H1-shaped), recorded but not interpreted as C1 evidence, because C1 is gated on C0 by the registered stop rule.
5. **Forced sampling does not diversify behaviour.** FS executed one class on 81-99% of ticks on 4/5 seeds (histograms, sec 2.1; entropy 0.06-1.53 bits against RND's 2.0). Setting the gate to "uncommitted" changes selection from argmin to softmax over a candidate set whose first actions are nearly all the same class. The action-diversity precondition (Q-111) therefore fails in the **candidate repertoire**, not at the commit gate.

### 2.5 C1: not run (registered stop)

Not interpreted: C0 found no input that separates on >= 4/5 seeds. Descriptive only (from the analysis output, `results/analysis_n5.txt`): the absolute 0.40 bar had appropriateness 0.00 and occupancy 1.00 in every life, because no signal comes within four orders of magnitude of it.

### 2.6 C2: CANNOT_DETERMINE (registered rule), with a descriptive table

RAW_REAL, K2 = 120: A / A_null / D; executed-action entropy pre -> post (bits); * = separates.

| seed | RND | NAT (= FC) | FS | CP, all ticks | CP, probe-evidence ticks (n pre/post) | FC at the same ticks |
|---|---|---|---|---|---|---|
| 761 | 0.79 / 0.56 / 0.23 *; 1.99 -> 1.99 | 0.45 / 0.36 / 0.09; 1.81 -> 0.63 | 0.54 / 0.24 / 0.31; 1.53 -> 1.49 | 0.73 / 0.40 / 0.33 *; 2.00 -> 1.70 | 0.90 / 0.50 / 0.40 * (8/6) | 0.35 / 0.23 / 0.13 |
| 762 | 0.82 / 0.84 / -0.02; 2.00 -> 1.99 | 0.27 / 0.60 / -0.33; 1.14 -> 0.97 | 0.41 / 0.93 / -0.52; 0.88 -> 0.98 | 0.35 / 0.53 / -0.18; 1.17 -> 1.12 | 0.28 / 0.50 / -0.22 (9/2) | 0.17 / 0.39 / -0.22 |
| 763 | 0.73 / 0.56 / 0.17 *; 1.97 -> 1.99 | 0.91 / 0.13 / 0.78 *; 1.02 -> 1.03 | 1.00 / 0.98 / 0.02; 1.10 -> 1.10 | 0.80 / 0.34 / 0.46 *; 1.00 -> 0.98 | 0.64 / 0.45 / 0.19 (7/6) | 0.95 / 0.26 / 0.69 |
| 764 | 0.59 / 0.61 / -0.02; 1.98 -> 2.00 | 1.00 / 0.51 / 0.49 *; 0.34 -> 0.00 | 0.88 / 0.02 / 0.86 *; 0.06 -> 0.00 | 0.98 / 0.53 / 0.45 *; 0.43 -> 0.73 | 0.93 / 0.75 / 0.18 * (4/7) | 1.00 / 0.82 / 0.18 |
| 765 | 0.80 / 0.81 / -0.02; 1.99 -> 1.99 | 1.00 / 1.00 / 0.00; 0.37 -> 0.79 | 0.99 / 0.99 / 0.00; 0.51 -> 0.59 | 0.89 / 0.98 / -0.09; 1.10 -> 0.89 | 0.94 / 0.96 / -0.01 (9/8) | 1.00 / 1.00 / 0.00 |

Tally: exposure reference RND separates on 2/5 (FS 1/5), so the registered rule returns **CANNOT_DETERMINE**: the evidence the escape question needs does not exist on most seeds, even under uniform random actions. Pooled probe-tick AUROC (report only): 0.83 in the change lives against 0.70 in the no-change lives (29 post / 37 pre ticks).

One seed shows the H2 shape cleanly, and it is recorded as an instance, not a verdict. On 761 the committed loop hides a change that random actions expose (NAT D 0.09 against RND D 0.23). Sparse probes at 5% restore detection on the probe-evidence ticks (A 0.90 against a null 0.50) while the forced-committed loop, scored at the same tick positions, does not (0.35). On 761 the native loop's executed-action entropy also fell from 1.81 to 0.63 bits after the change.

## 3. Verdicts

| leg | verdict (all 5 seeds, registered) | screen-passing subset (761, 762) |
|---|---|---|
| **C0** | **`neither = H-SV`** (RND: mix 2/5, realised 2/5; need 4/5). STOP | `neither = H-SV` (1/2 each) |
| **C1** | **`CANNOT_DETERMINE`**: registered stop after C0. Stage transfer was also cut (addendum 1b) | same |
| **C2** | **`CANNOT_DETERMINE`**: the exposure reference separates on only 2/5, so there is no evidence for commitment to hide or surface on most seeds. One seed (761) is an H2-shaped instance | same |

**Domain reached:** D1 (the signals were measured and the change's effect on them scored). The C2 clamps are interventions on the gate that change what is executed and what evidence arrives (D2 for "commitment changes the evidence stream"). They are descriptive here because the registered rule did not reach them.

## 4. Routing and limits

- **Route (per the plan's C0 row): E2/W3, not the commit gate.** At the W3 standard dose the one-step E2 head that rv reads is at persistence level (0.97-1.02) and weakly action-conditioned. No choice of bar, input provenance or escape probe can make the gate appropriate to a change that its input does not register. This agrees with N5 (b26d8e8d9d) and extends it from the member's own surprise to E3's rv.
- **Two corrections for the plan's Family C table** (for the orchestrator; the plan is not edited here):
  - (i) rv's raw input is not a realised error of the executed action even at k = 1, because E3 rolls out continuous action vectors and the body executes only their class (sec 2.2 a);
  - (ii) in the W3-trained `build_B` agent the rv-to-bar gap is 4-5 orders of magnitude, not two.
- **Separate finding worth an owner:** forced sampling does not produce action diversity: 1-2 classes on 4/5 seeds. The diversity precondition (Q-111) fails in the candidate repertoire. A gate or H1 fix at the commit site would not restore diversity.
- **Limits:**
  - S1 only; stage transfer untested (addendum 1b).
  - Lives are 330 ticks with a 140-tick pre-window and a 50-tick post-window.
  - The trainer is frozen during lives (upper bound on separability).
  - Health is pinned (no deaths).
  - The layout-redraw kind and the OWN closed-loop arm were cut before registration.
  - 3/5 seeds miss the W3 disc4 bar, but the two passing seeds give the same verdicts.
  - The per-seed CP probe test uses 4-9 ticks per window.
- **Cost disclosure:**
  - The Mac load average reached 33-72 during seed 761 (other workers' processes, some outside the lock). Seed 761's development took 975 s; the same step took 91-188 s later in the run.
  - Seed 761's first development hold ran ~18 min, over the 15 min limit, before in-dose rotation was added (addendum 1b).
  - Probe processes stayed alive while waiting to re-acquire the lock (sleeping in kqueue, no compute). The only compute outside a held lock was the first timing smoke's reference build (~seconds), which was killed and fixed before any registered seed.
