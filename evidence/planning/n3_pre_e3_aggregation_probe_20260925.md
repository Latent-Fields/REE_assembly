# N3-pre: which E3 horizon aggregation tracks true consequence? (proxy W3 head; pre-registered probe)

- **STATUS: FINAL (2026-09-25T14:16Z). RESULTS are appended at the end.** The pre-registration (committed 13:34Z as `7ba36ff63d`) is unchanged; only this status line was updated. **Pre-registered verdict: CANNOT_DETERMINE**, because the shuffled twin is at chance on 3/5 seeds, not the required 4/5. Descriptively, **no aggregation passes (a)-(c) on >= 4/5 seeds**. Gate (a) is met only by D1 (5/5), which SD-081 forbids, and by DISC_0.5 (4/5). Gate (b) is capped by E3's valuation, not by aggregation: the oracle one-step pick is at chance. Gate (c) does not separate real from shuffled under any aggregation.
- **PROVISIONAL for W4.** The world head here is a harness-trained PROXY of the W3 `E2WorldMember` (the same L2R recipe, trained by probe code), not the member itself. Whatever this selects, N3 proper must re-confirm it with the real W3 member on the branch.
- Session `bt0925-n3pre` (orchestrate-20260924-breakthrough), chip_ref `chip-20260925-coupled-n3-preprobe`. Brief: `.scratch/breakthrough-20260924/Z_n3.md`. Campaign plan: `coupled_loop_repair_campaign_plan.md` sections 3 (W3, W4) and 4 (N3).
- Code: ree-v3 `origin/main` @ `5f965cff83` in a private detached worktree. No ree_core edits.
- **I1 instruments not used, because they do not exist yet.** `experiments/_lib/coupled_acceptance.py` is not on origin/main at `5f965cff83` (re-measured 13:28Z). So this probe reuses the committed probe code: `probes/babble/babble_probe.py` (L2R recipe, discrimination metric), `probes/rollout/balanced_replay_probe.py` (cloned-env true next z, ADDENDUM 2 Measure 2), and `probes/rollout/partitioned_repair_probe.py` (env-Q, ADDENDUM 3).
- Probe script: `probes/n3pre/n3pre_probe.py` (committed with the results).

## Premises re-measured before pre-registering (D0 code read)

1. **The E3 score is not additive per step.** In `e3_selector.py` @ `5f965cff83`:
   - F (`compute_reality_cost`, :1493) is the MEAN over steps of the squared z_world step.
   - M (`compute_harm_cost_fallback`, :1520) is a SUM over states of `harm_eval_head`.
   - Phi_R (`compute_residue_cost`, :1555 -> `residue/field.py:721`) is a SUM over states.
   - Every term reads its states through `_get_world_states` (:1473), which truncates to `_score_depth_limit` states (SD-081's knob).
   So a per-step weighting cannot be defined term by term without choosing semantics for F. I define every aggregation on the native scorer's own depth-limited scores (below), which the SD-081 knob already exposes. That keeps the aggregation implementable in ree_core as a weighting over depth-limited reads of the one scorer.
2. **Depth-1 IS the habit read.** The dual-system HABIT pathway sets `_score_depth_limit = max(2, dualsystem_habit_depth)` (:2088), and `dualsystem_habit_depth` defaults to 2 (`config.py:2438`). Limit 2 = current state + one step, which is exactly the ADDENDUM 2 "depth-1" read. So **a depth-1 planned aggregation makes planned == habit and fails SD-081's P1 by construction.** It can be measured but cannot be selected.
3. **Candidate pools.** Native pool size is 32 (`num_candidates`, `config.py:970`); rollout horizon 30 (`config.py:969`), so each candidate carries 31 z_world states.
4. The addendum-2 / babbling harness functions (`encode_next`, cloned-env true z, `score`) are reused unchanged. A 7-state smoke on **non-registered seed 520** (`results/SMOKE_s520.json`, tiny sizes: N = 400, P = 200, 200 pre-updates) validated the pipeline: every head gets gradient; cloned-env validation max |diff| 0.0; the batched scorer equals per-candidate `score_trajectory` exactly (canary 0.0); and J at limit 31 equals the unlimited J exactly (canary 0.0). That smoke is the only execution before this commit; its numbers are not results.

## Design (fixed)

**Regime.** The babbling probe's: Phase-0 env CausalGridWorldV2 size 12 (`babble_probe.make_env`, env seed = seed*160 + k); native z_world read path of `build_B(seed)`, world_dim 32 (deployed dim); random-init encoder, **frozen** (never trained). Mac, `torch.set_num_threads(2)`, one process at a time.

**Seeds: 521, 522, 523, 524, 525** (fresh; not in any committed probe result or record found by grep).

**Data (per seed).**
- D_L2: 2,400 transitions (12 episodes of 200, k = 0..11). Class uniform over **{0..4} including stay (4)**, held for a run length uniform on {1,2,3,4}. (The babbling probe's L2 used {0..3}; the W3 recipe says all 5 classes.)
- D_SHUF: D_L2 with its action labels permuted across timesteps.
- TE4: 3,000 held-out uniform {0..3} steps (k = 120..134), the babbling probe's test set unchanged, for the L2R bar.
- TEW: 3,000 held-out uniform {0..4} steps (k = 160..174), for disc5 and the per-depth fidelity weights (H up to 30).

**Heads.**
- **REAL (proxy W3 head, the L2R recipe):** from the init head, 3,000 updates on D_L2 (batch 32, Adam 3e-4, clip 1.0, single-step MSE); then a post phase of P = 1,200 closed-loop steps (fresh `build_B` agent with the same frozen encoder, native E3, head live, env episodes k = 50..55) with 9,000 online updates spread evenly, each batch 25% D_L2 replay + 75% on-policy.
- **SHUF (label-shuffled twin):** identical protocol, but every action label it trains on is uninformative: D_SHUF in the pre-phase and in the 25% replay, and on-policy labels resampled independently of the transition (same label marginal, correspondence destroyed).
- **INIT:** the untrained head, the reference for pick-flip.
- **B0' (descriptive only):** 3,000 updates on REAL's own post-phase on-policy transitions. Retention = (disc4(REAL) - disc4(B0')) / (disc4(REAL_pre) - disc4(B0')). This stands in for W3 gate (b), whose B0 needs a separate on-policy collection that this probe does not run.

**Probe states.** A fresh agent with the REAL head live runs native waking in env episode k = 100 for 320 harness steps. Every 8 steps, at the StepHarness `on_action` hook:
- the native CEM pool is recorded (torch RNG saved and restored around `propose_trajectories`);
- for each class c in {0..4} the env is deep-copied and stepped, and the true next z_world is encoded through sense()'s own encoder call, side-effect-free (validated against the next tick's sensed z_world);
- **env-Q(c)** = mean over 6 random continuations of the summed env reward (`harm_signal`) of [c, then 4 uniform-random steps] (the ADDENDUM 3 estimator).
Expected ~35 states. **If a seed yields fewer than 20, it is re-run with 640 steps (resources rule only).** All heads are scored on the same states and pools, on the probe agent after the run (its residue field as at the end of the run; stated, as in ADDENDUM 2).

**Aggregations.** For each head and candidate, J_L = the native `E3.score_trajectory` with `_score_depth_limit = L`, for L = 2..31 (31 = full). The increment for depth d (d = 2..30) is Delta_d = J_{d+1} - J_d.
| id | definition | nominal planned depth |
|---|---|---|
| **D1** | J_2 | 1 step (== habit read) |
| **DISC_0.5** | J_2 + sum_d 0.5^(d-1) Delta_d | 30 (effective ~2) |
| **DISC_0.8** | J_2 + sum_d 0.8^(d-1) Delta_d | 30 (effective ~5) |
| **FIDW** | J_2 + sum_d w_d Delta_d, with w_d = 1 iff THIS head's median rollout error at depth d beats persistence on TEW, else 0 (step 1 always kept) | the deepest weighted d |
| **FULL** | J_31 (current behaviour) | 30 |

**Candidate sets.**
- **Scaffold pool** (ADDENDUM 2 Measure 2, derived from the recorded native pool): pool[0]'s action sequence with step 0 replaced by one-hot c, one candidate per class c = 0..4. J_true(c) = the E3 score of the one-step trajectory [z0, true z1(c)]. This is the primary set for gates (a) and (b), because it is the one set where every first action is represented (the native pool is dominated by 1-3 decoder-bias classes; smoke median 3 distinct first classes of 32). It is also the shape of W1-alt's stratified action-space pool.
- **Native pool** (32 recorded candidates): primary for gate (c), as in the babbling probe's D2 reach, which is the non-discriminating 70-100% reading that (c) exists to fix. Secondary (descriptive): Spearman of native-pool J against J_true of each candidate's first-action class.

## Criteria (fixed; W4 member gates, per aggregation)

Per seed and per aggregation, with differences taken REAL minus SHUF:
| id | quantity | per-seed pass | aggregation passes if |
|---|---|---|---|
| **(a)** | mean over states of Spearman(J_pred, J_true) on the scaffold pool (states where it is defined) | diff > 0.15, and >= 10 states defined for both heads | >= 4/5 seeds |
| **(b)** | P(argmin J_pred on the scaffold pool is in the env-Q-best set), over states with non-constant Q | diff > 0.10, and >= 10 informative states | >= 4/5 seeds |
| **(c)** | P(argmin over the native pool differs from the INIT head's argmin under the same aggregation) | diff > 0.15 | >= 4/5 seeds |

**SD-081 compatibility.** An aggregation is compatible iff its nominal planned depth is > the habit read's (limit 2, i.e. 1 step).
- D1: **incompatible by construction.**
- DISC_0.5 / DISC_0.8 / FULL: compatible nominally.
- FIDW: compatible iff the REAL head has w_d = 1 for some d >= 2 on >= 4/5 seeds.
- Descriptive for all: how often the aggregation's native-pool pick agrees with the habit (D1) pick, and their mean Spearman. An agreement near 1.0 means the planned/habit contrast is degenerate in practice even where it is nominally allowed; I will flag agreement > 0.9.

**Selection rule.** The SIMPLEST aggregation, in the order **D1 < DISC_0.5 < DISC_0.8 < FIDW < FULL**, that passes (a), (b) and (c) AND is SD-081-compatible. If D1 passes it is reported as passing-but-incompatible and not selected. If only D1 passes, the verdict is **D1_ONLY_SD081_CONFLICT** (a decision for the orchestrator/user, not taken here). If nothing passes: **NONE_PASS**.

**CANNOT_DETERMINE (whole probe)** if any of:
1. the proxy head fails its own L2R bar: REAL disc4_h1 (TE4) >= 0.47 **and** fidelity k (H = 10, TE4) = 10, on >= 4/5 seeds (W3 gate (a));
2. the shuffled twin is not at chance: SHUF disc4_h1 (TE4) <= 0.32 **and** disc5_h1 (TEW) <= 0.27, on >= 4/5 seeds (chance 0.25 / 0.20; this also covers W3 gate (c));
3. an instrument canary fails on any seed: cloned-env validation max |diff| > 1e-5, the depth decomposition (J_31 vs unlimited J) > 1e-5, the batched-vs-single scorer canary > 1e-5, or fewer than 20 probe states after the re-run rule.

**Known-baseline canary (descriptive, not a gate).** Under FULL, SHUF's pick-flip vs INIT should be high (>= 0.5 on >= 3/5 seeds), reproducing the babbling probe's non-discriminating D2 (`0ac69c87446`: 70-100% for real and shuffled alike). If it does not reproduce, I will say so and weigh gate (c) accordingly.

**Also reported:** per head, disc4_h1 / disc5_h1 / k (TE4), k30 and the per-depth fidelity (TEW), rollout norms at t1 and t30 against the true norm (W3 gate (e) analog), retention vs B0' (descriptive), and post-phase reward / harm / action entropy.

**No tuning, and no extra arms or seeds after seeing results.** Post-hoc diagnostics will be labelled as such.

**Domains.** (a) and (b) are D2 (intervening on the head / aggregation changes the native consumer's ranking, read against cloned-env consequence). (c) is D2 reach. Nothing here is D3: no closed-loop outcome is compared across aggregations.

**Limits known in advance.** J_true is E3's own one-step score (its F term favours small moves; `harm_eval_head` is untrained in this build), so (a) partly measures self-consistency. (b) is the env-grounded gate, with a noisy Q (6 x 4-step random continuations). The encoder is random-init and frozen. The proxy head is not the W3 member. 5 seeds, ~35 states each.

## RESULTS (2026-09-25T14:16Z; full tables in `probes/n3pre/results/SUMMARY.txt`, raw `N3_s52{1..5}.json`)

### Run log (resources only; `results/decisions.log`)

- Seeds 521-525 ran one at a time from 13:35Z to 13:55Z, with free+inactive+speculative memory at 1,268-1,552 MB at each start. There were no memory waits.
- Each seed took 2-3 min, except s525 at ~10 min, because its post phase ended 174 episodes early.
- Every seed gave 46-56 probe states, all Q-informative, so the re-run rule was never triggered.
- Nothing else was changed.

### Proxy head and shuffled twin (the preconditions)

| seed | REAL disc4_h1 / k (TE4) | REAL disc5 (TEW) / k30 | SHUF disc4 / disc5 (TEW) | INIT disc4 | B0' disc4 | retention vs B0' | REAL t1 / t30 / true norm |
|---|---|---|---|---|---|---|---|
| 521 | **0.483 / 10** | 0.422 / 26 | 0.263 / 0.260 | 0.220 | 0.300 | 1.31 | 0.38 / 0.44 / 0.36 |
| 522 | **0.470 / 10** | 0.368 / 30 | 0.290 / **0.274** | 0.247 | 0.300 | 1.46 | 0.38 / 0.48 / 0.35 |
| 523 | **0.477 / 10** | 0.365 / 23 | **0.327** / 0.191 | 0.263 | 0.297 | 1.10 | 0.43 / 0.60 / 0.40 |
| 524 | **0.527 / 10** | 0.378 / 21 | 0.300 / 0.250 | 0.253 | 0.313 | 2.46 | 0.43 / 0.48 / 0.42 |
| 525 | **0.547 / 10** | 0.420 / 17 | 0.240 / 0.203 | 0.283 | 0.240 | 1.08 | 0.44 / 0.74 / 0.40 |

- **The proxy head meets its L2R bar on 5/5 seeds.** disc4_h1 is 0.470-0.547 with k = 10, which matches the babbling probe's L2R (0.473-0.553).
  - Descriptive retention against B0' is 1.08-2.46 on 5/5 seeds.
  - The rollout norm stays bounded (t30 of 0.44-0.74 against a true norm of 0.35-0.42). The INIT head diverges to 238-940.
  - With stay included, 5-class discrimination is 0.365-0.422 (chance 0.20).
- **The shuffled twin is at chance on 3/5 seeds. The pre-registered bar needs 4/5, so this fails.**
  - s523: disc4 0.327, against a limit of <= 0.32.
  - s522: disc5 0.274, against a limit of <= 0.27.
  - Both misses are small, and SHUF stays well below REAL on every seed (disc4 0.24-0.33 against 0.47-0.55). Even so, the pre-registered rule makes the whole probe **CANNOT_DETERMINE**.
- The twin's residual above chance most plausibly comes from the post phase. Its on-policy labels are resampled from the buffer's marginal, and on seeds where the agent almost always takes one class (s522: class 3 in 1,194 of 1,200 steps; s523: 1,045 of 1,200), the resampled label nearly always equals the true one. Shuffling therefore cannot destroy the correspondence there. This is a flaw in the twin's design (post-hoc reading, not tested).
- **Instrument canaries.**
  - Cloned-env validation max |diff| was 0.0 on every seed.
  - The depth decomposition matched exactly: J at limit 31 equals the unlimited J (0.0).
  - **The batched-vs-single scorer canary exceeded the pre-registered 1e-5** on s522 (2.4e-4) and s523 (1.5e-5). The post-hoc check below shows this is float32 rounding: at most 1.3e-5 relative to |J|, which reaches 19-419. The absolute threshold was mis-set.
  - This canary does not change the verdict, because the shuffled-twin precondition already fails.
- Post-phase behaviour, for context:
  - s522 and s523 are near-monostrategy (class 3 at 87-99%).
  - s525 is hazard-trapped: the agent stays (class 4) at 100 harm events per 100 steps, with 174 early terminations, for both REAL and SHUF.

### W4 member gates per aggregation (descriptive under CANNOT_DETERMINE; REAL / SHUF, and the difference)

| agg | (a) Spearman(J_pred, J_true), diff > 0.15 | (b) pick in env-Q-best, diff > 0.10 | (c) native pick-flip vs INIT, diff > 0.15 | SD-081 |
|---|---|---|---|---|
| **D1** | **5/5**: REAL 0.22-0.71 vs SHUF -0.20 to 0.04 (diff +0.22 to +0.80) | 2/5 (diff 0.00 to +0.48) | 1/5: REAL 0.79-1.00 vs SHUF 0.68-1.00 | **incompatible (== habit read)** |
| **DISC_0.5** | **4/5**: REAL 0.08-0.67 (diff -0.12 to +0.81) | 2/5 | 0/5 | compatible; habit-pick agreement 0.00-0.57 |
| DISC_0.8 | 1/5 | 1/5 | 0/5 | compatible |
| FIDW | 0/5: REAL -0.50 to -0.01 | 2/5 | 0/5 | compatible nominally, but weights reach depth 17-30 (see below) |
| FULL | 0/5: **REAL -0.50 to -0.08, while SHUF is +0.03 to +0.47** | 2/5 | 0/5 (canary reproduced: SHUF flip >= 0.5 on 5/5) | compatible |

**Pre-registered verdict: CANNOT_DETERMINE (the shuffled twin is at chance on only 3/5 seeds; the float canary also exceeded its threshold on 2 seeds).** No aggregation would have been SELECTED even without that: none passes (a), (b) and (c) together on >= 4/5 seeds.

### POST-HOC diagnostic (NOT pre-registered; `n3pre_posthoc.py`, `results/N3PH_*.json`, `POSTHOC_SUMMARY.txt`)

- **Why run it.** The verdict was already fixed at CANNOT_DETERMINE. I re-ran the identical pipeline to ask why (b) and (c) fail. The pre-registered metrics **reproduced bit-for-bit on 5/5 seeds**.
- **Gate (b) is capped by valuation, not by aggregation.**
  - The ORACLE pick scores E3 on the TRUE next state of each class, with no head and no aggregation involved. It lands in the env-Q-best set at 0.09 / 0.20 / 0.22 / 0.19 / 0.12, against chance ~0.20.
  - So under the default E3 valuation (F penalises displacement; `harm_eval_head` is untrained; no benefit channel), even perfect one-step prediction does not choose on env consequence. No aggregation can pass (b) until valuation is grounded.
  - This reproduces ADDENDUM 3's read-out point 3 on fresh seeds with an action-covered head. It places (b)'s blocker in **W5**, not W4.
- **Gate (c) does not discriminate, whatever the candidate set.**
  - Measured on the scaffold pool, (c) passes on at most 2/5 seeds under any aggregation (0/5 for D1).
  - Measured as the native pick's first-action CLASS, it passes on 0/5 for every aggregation.
  - The reference head is INIT, which diverges (t30 norm 238-940). Swapping in ANY trained head (REAL or SHUF) therefore rewrites every rollout. So "flip vs INIT" measures "the head changed and became bounded", not "the head carries action information".
  - As specified, (c) cannot be passed by any aggregation: it is a gate-design defect. A discriminating form would need a reference that is trained and bounded but action-blind (e.g. the SHUF twin itself), or it should count flips TOWARD the true-better choice.
- **FIDW is FULL in disguise here.** The REAL head beats persistence out to depth 17-30 (k30), so FIDW weights nearly every step. Beating persistence (bounded mean dynamics) is not the same as carrying action information. Weighting by fidelity-vs-persistence is therefore the wrong criterion for W4.
- **The one clean positive finding.** The steep aggregations make E3's ranking track its own one-step consequence far better with the real head than with the shuffled one:
  - D1: 5/5 seeds, diff up to +0.80.
  - DISC_0.5: 4/5 seeds.
  - gamma >= 0.8, FIDW and FULL wash this out, and FULL anti-tracks with the real head.
  - This replicates ADDENDUM 2 Measure 2 (depth-1 rho 0.24-0.53, full -0.18 to 0.01) on 5 fresh seeds, with the W3-recipe head and its shuffled twin.
  - **DISC_0.5 is the simplest SD-081-compatible aggregation with this property.** Its planned pick differs from the habit pick at 43-100% of states, so the contrast is not degenerate.

### What this means for W4 / N3 (the orchestrator decides; no decision taken here)

1. **Aggregation.** On the one gate aggregation can affect (a), the candidate is **DISC_0.5**; D1 is excluded by SD-081. It is NOT selected: the pre-registered verdict is CANNOT_DETERMINE, and it fails (b) and (c).
2. **W4's member gate cannot pass as written, with any aggregation.**
   - (b) is capped at chance by valuation (oracle 0.09-0.22), so it depends on W5 (grounded valuation), not W4.
   - (c) is non-discriminating by construction: it is referenced to the divergent INIT head.
   - Options for the gate owner:
     - (i) re-reference (c) to a trained, bounded, action-blind head, or re-define it as flips toward the true-better choice;
     - (ii) move (b) from W4's gate to the integrated gate after W5;
     - (iii) keep the gate as is and accept that W4 cannot pass until W5 lands.
3. **Fix the shuffled twin before N3 proper.** Resampling on-policy labels from a near-monostrategy buffer does not destroy the label correspondence. Use a fixed label permutation over classes (a class relabelling), or a uniform label draw.
4. The float canary threshold should be relative (about 1e-5 of |J|), not absolute.

### Domains and limits

- D2 for (a) and (b): changing the head or aggregation changed the native consumer's ranking, read against cloned-env consequence. D2 reach for (c). No D3.
- PROVISIONAL: a proxy head, not the W3 member. Random-init frozen encoder, world_dim 32, size-12 Phase-0 env.
- The Q estimator is noisy (6 x 4-step random continuations).
- J_true is E3's own one-step score, so (a) is partly self-consistency.
- 46-56 states per seed. s525 is hazard-trapped.

### Reproduction

- Scripts are in `evidence/planning/probes/n3pre/`: `n3pre_probe.py`, `n3pre_posthoc.py`, `summarize_n3pre.py`, `summarize_posthoc.py`, `run_all.sh`, `run_posthoc.sh`.
- They expect two siblings:
  - `probes_src/`: copies of `probes/rollout/{rollout_fidelity_probe,balanced_replay_probe,encoding_vs_objective_probe}.py` and `probes/babble/babble_probe.py`;
  - `ree-v3-wt`: a detached worktree of ree-v3 @ `5f965cff83`.
- One seed: `python3 n3pre_probe.py --seed S --out results/N3_sS.json`. Mac CPU, 2 threads, one process at a time.
