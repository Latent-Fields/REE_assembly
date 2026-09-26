# Probe E: where does the W3 E2 world head lose the action off-reset? ENV / REPRESENTATION / PREDICTION / PROVENANCE

- **Status: PRE-REGISTERED.** Sections 0-3 are committed before any registered seed runs. Results go in sec 4 and later.
- **Session:** `bt0926-e2edge` (orchestrator `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dcd2-e2-offreset-edge`. Written 2026-09-26T18:33:14Z.
- **Why:** Probe C (`commit_gate_discrimination_probe_20260926.md`, 6f45386213) found that a hidden action-map shift is invisible to both error signals. The cause it named was the W3 E2 world head, which predicts about as well as "nothing changes" (error/persistence 0.97-1.02). `w3_k_excluding_reset_ticks_20260926.md` (370c222e20) found the same thing: W3 only ties persistence at >= 8 ticks after a reset (ratio 0.97-1.03). N5 (b26d8e8d9d) found the same too. Under the DCD2 plan (41cfe94841), this is the earliest broken edge for the commitment family. All four inputs were read in full.
- **Question:** off-reset (>= 8 ticks after any reset), is the action-conditional information lost at the environment, at z_world, at E2's learning, or at the action code E2 is fed?
- **Code under test:** `ree-v3` `4070b0efa4` (tag `archive/coupled-loop-repair-4070b0e`: W3 E2WorldMember + W6a + W4), private detached worktree `.scratch/wt-e2edge`.
  - No `ree_core` edits. No ree-v3 commits.
  - Every counterfactual, oracle and scoring step runs probe-side.
  - Every file:line below is on this sha.
- **Probe:** `probes/e2edge/e2edge_probe.py` (one process = one seed). Mac, 2 torch threads, under the shared `mac_probe.lock`:
  - the lock is acquired before any compute, and each hold is capped at 600 s plus at most one episode;
  - the process waits 180 s after each of its own releases before re-acquiring;
  - release is verified.
- **Evidence domain reachable: D1.** Quantities are measured, decoded and fitted on held-out data. No consumer intervention is attempted.

## 0. Premise audit (re-measured on 4070b0efa4 before registering)

| # | premise | re-measured | verdict |
|---|---|---|---|
| a | the brief asks for "one untrained-encoder reference" | D0: the W3 protocol builds the agent with `BB.fresh_agent(S, ref_enc)`, which asserts the encoder equals the random-init reference (`babble_probe.py:327-334`). The trainer holds only the `E2WorldMember`, and that member's gradient cannot reach the encoder (`waking_trainer.py:371-374`: "that is W6a's group"). W6a is not in the W3 member protocol. **So the deployed W3 z_world encoder IS an untrained random init, frozen.** D1: `encoder_unchanged_after_W3` is logged per seed | **corrected.** The "untrained-encoder reference" is the deployed encoder itself. The probe adds three references: a SECOND random init (`build_B(S+1000)`, "ZU"); the pre-EMA z_world ("ZR"); and a linear PCA-32 of the raw world obs fitted on TRAIN ("PCA", information-preserving at the same width) |
| b | in the native loop E2 is fed a continuous candidate vector while the env executes its class | D0: `agent.py:12122` sets `_last_action = result.selected_action`. The E2 member records `agent._last_action` as the transition's action (`waking_trainer.py:479`, docstring `:367`: "the executed action a_t AS FED TO E2"). The env executes `action.argmax()` (`causal_grid_world.py:2487-2488`). Candidate first actions are continuous (probe C, `e2_fast.py:858-864`). Babbling records a one-hot (`record_executed_action`). D1: the one-hot fraction of the member's retained and on-policy records, and of the vectors fed in a frozen native life, is logged per seed | D0 holds; D1 in results |
| c | W3's E2 only ties persistence off-reset | re-measured here on fresh seeds as the E2_POST row (t >= 8) | measured |
| d | a counterfactual next observation can be produced faithfully | `deepcopy(env).step(c)` for c = 0..4 before every real step, with the python/numpy/torch global RNG saved and restored (the env draws from its own `self._rng`, `causal_grid_world.py:1604`, which the deepcopy carries). **Canaries:** CF(executed class) must equal the actual next obs on every tick. The TEST obs sequence must be identical to the W3 held-out generator `BB.gen_policy(S, 15, 120, pol_uniform(S*7+3))`. Smoke (seed 939): 0 mismatches, identical | holds (smoke); re-checked per seed |
| e | a counterfactual z is the z the native read path would produce | `encode_lat` replicates `sense()`'s encoder call (`agent.py:6068`, `latent_stack.encode(enc, prev_latent, prev_action=None, ...)`; the reference agent never acts, so its `_last_action` is None). **Canary:** encode(CF(executed)) must equal `sense().z_world`. Smoke: max abs diff 0.0 | holds (smoke); re-checked per seed |
| f | z_world does not depend on the previous action in this build | `latent_stack.reafference_predictor is None` is logged (SD-007 off -> `prev_action` unused, `stack.py:1524-1542`) | logged per seed |

## 1. Design (pre-registered)

**Development per seed:** the W3 member protocol exactly as probe C / N5 phase 1:
- `build_B` (`world_dim` 32 = deployed, `alpha_world` 0.3);
- **all four reset-init knobs ON** (campaign preset);
- `E2WorldMember` (lr 3e-4, batch 32, MSE, grad_clip 1.0, retained 5000, `reencode`);
- W2a babbling 2400 steps -> FROZEN retained set, 3000 updates (**head E2_PRE**);
- 1200 native `StepHarness` steps x 8 updates at a 25% retained mix (**head E2_POST**, the W3 head);
- **E2_INIT** = the untrained head (reference).
- The W3 standard `evaluate()` (disc4/k/ratio, all ticks) is recorded, not used to drop seeds.

**Data (per seed):**
- **TEST** = the W3 held-out generator verbatim: 15 episodes of uniform-random move classes {0..3}, env k 120-134, policy seed S*7+3, ~3000 steps. Each step also carries the 5 counterfactual next obs.
- **TRAIN** (for the fitted oracles) = the same generator on env k 300-314, policy seed S*7+5.
- **ON-POLICY** = >= 800 steps of the E2_POST agent in its native closed loop, trainer frozen, env k 170+. Logged per step: the vector `_last_action` fed to E2, and the executed class.
- Every set is encoded by the reference agent's native read path (`sense()` after `reset()` per segment, as `BB.encode_segs`).

**Window (every DV): off-reset = transitions t -> t+1 with t >= 8 ticks since that segment's reset.** Near-reset (t < 8) and all ticks are reported as references, not verdicts.

**Spaces:**
- **OBS** = raw `world_state` (250-d; egocentric 5x5x7 local view + contamination + ...);
- **ZW** = z_world (deployed);
- references ZR, ZU and PCA (premise a).

**Predictors (per space):**
- **PERS:** x_{t+1} := x_t.
- **Exact counterfactual indices (no fitting):**
  - **ID** = identifiability of a_t from x_{t+1} under the true dynamics: the argmin over the 4 counterfactuals, ties split;
  - **AC** = median ||x^a - mean_c x^c|| / median ||x^a - x_t||, the share of the step that depends on the action;
  - **R_cfblind** = the best action-blind prediction under a uniform prior.
- **RIDGE_ACT** = per-class linear map on Δx from [x_t, 1] (equivalent to a full action interaction), fitted on TRAIN off-reset, lambda chosen on a 20% validation split.
- **RIDGE_BLIND** = a pooled map (action-blind twin).
- **RIDGE_SHUF** = per-class maps on permuted labels (control).
- **MLP_ACT** (z-spaces only) = 2x128 ReLU on [standardised x_t, onehot a_t] -> Δx, Adam, 2500 steps, best-validation checkpoint. **MLP_SHUF** is its twin on permuted labels.
- **All fitted models are ORACLE CEILINGS: fitted on TRAIN, scored on TEST only.**
- **E2 heads (ZW):** `rollout_with_world` h = 1 with zero z_self, the `evaluate()` call form. Canary: this probe's disc4 on `evaluate()`'s own 300 starts must equal `evaluate()`'s `disc4_h1`.
- **ORACLE_BUF (ZW):** RIDGE_ACT and MLP_ACT fitted on the E2 member's own buffer (retained + on-policy `z_live` pairs, argmax of the stored action), scored on TEST. This is "the same buffer".

**Metrics, the same for every predictor:**
- **R** = median ||pred(x_t, a_t) - x_{t+1}|| / median ||x_t - x_{t+1}||, the W3 `err_over_pers_h1` form;
- **disc4** = P(argmin over c in 0..3 of ||pred(x_t, c) - x_{t+1}|| = a_t), ties broken at random, chance 0.25;
- **R_twin** = R of the predictor's action-blind twin: RIDGE_BLIND for ridge, MLP_SHUF for MLP, and the class-average of the predictor itself for E2;
- **ES** = action sensitivity: median ||pred(a) - mean_c pred(c)|| / median ||x^a - mean_c x^c||;
- all of the above per executed class 0..3.

**"Carries the action and beats persistence" (margin fixed here):** R <= 0.90 AND disc4 >= 0.50 AND R <= R_twin - 0.05.
- 0.90 sits 7-13 points outside the 0.97-1.03 off-reset band measured by probe C and W3k.
- 0.50 is above the W3 bar (0.47) and 2x chance.
- The twin margin requires the gain to come from the action.

## 2. Decision rule (per seed, rungs in causal order)

1. **ENV** fails iff OBS RIDGE_ACT does not meet the criterion. Then persistence is near-optimal at the observation level for a learner that sees (o_t, a_t). The exact ID/AC indices are reported alongside.
2. **REPRESENTATION** fails iff neither ZW RIDGE_ACT nor ZW MLP_ACT meets it. The observation carries the action; z_world does not (or not recoverably from z_t).
3. **PREDICTION** fails iff E2_POST (ZW, one-hot) does not meet it. Sub-attribution:
   - (3a) if E2_PRE meets it AND the member's on-policy records are < 50% one-hot -> **PROVENANCE (training)**: the native dose's continuous action code degraded a head that had learned it;
   - (3b) otherwise **PREDICTION**, labelled **data** if ORACLE_BUF (best of ridge/MLP) also fails the criterion (the buffer lacks it) and **learner** if ORACLE_BUF meets it while E2 does not.
4. **PROVENANCE (use)** fails iff, on ON-POLICY off-reset transitions, E2_POST's R with the fed vector exceeds its R with the executed one-hot by >= 0.05 AND the one-hot R <= 0.90.
5. Otherwise **none**.

- **Seed verdict** = the first failing rung.
- **Probe verdict** = the label shared by >= ceil(2n/3) of the completed seeds (n >= 3). Otherwise **MIXED**, with the per-seed list. With n < 3 the verdict is **INTERIM**.
- Also report-only: **ZW_FROM_Z_OBS**, a per-class ridge predicting z_{t+1} from [z_t, obs_t]. It asks whether z_t lacks current-view detail that the observation has. Added after the smoke, before registration.
- Note: AC and R_cfblind coincide by construction, because x^a = x_{t+1} when the CF canary holds. They are one index, reported once.
- Reported, not verdict-bearing: every rung on every seed (not only the first failure), the ZR/ZU/PCA references, near-reset and all-tick windows, per-class tables, and the probe-C premise (b) D1 fractions.

**Seeds (fresh, registered in this order):** **931, 932, 933, 934**. Not 0-2, 106-110, 531-535, 611-615, 721-725, 761-765, 790, 798, 799, 850 or 901-915. The smoke used 939, unregistered.

**Add-on (report-only, untagged, not verdict-bearing): Q-113 precondition P1.**
- Balanced accuracy of linearly decoding two co-present cues from a frozen representation, on TEST off-reset ticks after fitting on TRAIN (L-BFGS logistic, class-weighted):
  - hazard in the 5x5 view;
  - resource in the 5x5 view;
  - their 4-way joint.
- Representations: ZW (frozen z_world), ZU, PCA32, and **RANDPROJ** (an untrained random linear projection of the same `world_state` to 32 d; the V3-EXQ-1002-style control).
- Q-113's own bar is 0.80 and above the untrained-projection control. Per premise a, the deployed encoder is itself untrained, so this comparison is structurally near-degenerate here. That is reported, not interpreted. **Not tagged to any claim.**

## 3. Cost / stop rules

- Smoke (seed 939, reduced sizes) measured the phases (sec 3a).
- Budget cap ~2.5 h of compute. Seeds run in registration order, one process each, from a nohup'd runner.
- If the cap is reached, the verdict is over the completed seeds, labelled INTERIM when n < 3, never silently.
- No arm, window, margin or rule changes after this commit. A crash is fixed and the seed re-run from scratch; the crash is disclosed.

### 3a. Smoke disclosure (seed 939, not registered)

The smoke ran at reduced sizes: 2 test and 2 train episodes, 1 babbling episode, 300 updates, 200 native dose steps, 200 on-policy steps. Wall time was 339 s, of which 59 s were under lock in phase 0-2 and 9 s under lock for scoring. It is a code, canary and timing check only. Its numbers are from an under-developed head and are **not** results.
- **Canaries all held:** TEST equals the W3 generator; CF(executed) mismatches 0; encode_next vs sense max abs diff 0.0 for both encoders; this probe's disc4 equals `evaluate()`'s disc4_h1 exactly (0.4083 / 0.4083); the encoder was unchanged after the W3 protocol; the reafference predictor is None; alpha_world is 0.3.
- **Premise b, D1 (smoke):** the retained (babbling) records are 100% one-hot; the on-policy records are 30% one-hot, with a median action-vector norm of 0.34. In a frozen native life the vector fed to E2 was one-hot on 45% of ticks, and its argmax equalled the executed class on 100% of ticks.
- **What the smoke changed before registration:**
  - a print fix (an exact 0.0 printed as -1);
  - the report-only ZW_FROM_Z_OBS predictor was added.
  - No rule, margin, window or seed changed.
