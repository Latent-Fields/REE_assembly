# Is Phase-0 babbling a sufficient and durable source of action coverage for E2's world head? (pre-registered probe)

- **STATUS: PRE-REGISTRATION ONLY (2026-09-25T07:45Z). No registered seed has been run.** Results will be appended below this section, and the pre-registered numbers here will not be edited.
- Session `bt0925-babble` (Worker Q, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-babbling-e2-coverage-probe`. Campaign question (synthesis section 7b, `5dc586f53e`; GFLAG-0504): should the coupled campaign use a one-off developmental babbling epoch, a retained babbling replay, or a standing babbling floor?
- Brief: `Q_babble.md`, plus the user's AMENDMENT of 07:34Z (dose axis, post-babbling phase, DR criterion, BEH outcome). Both are folded in here before any run.
- Code: ree-v3 `origin/main` @ `6de633cea5`, in a private detached worktree. Probe: `.scratch/breakthrough-20260924/babble/babble_probe.py` (committed with the results). It reuses the addendum-1/2 harness functions (`rollout_fidelity_probe.build_B`, `balanced_replay_probe.{get_head,set_head,encode_next,collect_probe_states,score}`) from `evidence/planning/probes/rollout/`.

## Premises re-measured before pre-registering (D0 code read, plus one timing pilot)

1. **"Phase 0 is random-policy stepping" is FALSE as a description of the generator.** That phrase is the `infant_warmup.py:14` docstring. In every driver that actually runs Phase 0 (the V3-EXQ-591 lineage: `v3_exq_591_isef005_curriculum_vs_flat_v3.py:293-296`, `v3_exq_591h_isef005_phase01_gate_live_v3.py:386-389`, and V3-EXQ-996), the action comes from **`agent.act_with_split_obs`**. That is the agent's own native E3 selection, taken as `argmax % ACTION_DIM` with `ACTION_DIM = 4` (`v3_exq_591_...:87`). The env has 5 actions, so class 4 is never emitted.
   - The build is the 591c diversity-armed agent: novelty_bonus_weight 0.5, MECH-313 noise floor, MECH-314 structured curiosity, alpha_world 0.9, world_dim 32 (the `from_dims` default) (`591h:290-310`).
   - The env is CausalGridWorldV2 at size 12 with resource_respawn_on_consume, new env each episode with seed = seed*160+ep, and 200 steps per episode.
   - The scheduler's Phase-0 env_kwargs are all-False, which equals the env defaults (`causal_grid_world.py:753,766,794`). Its Phase-0 novelty override (0.5) equals the build's baseline, and 591h does not apply residue_scale_factor. So **Phase 0 is the native policy under the 591c build. Nothing distinguishes it from on-policy behaviour except that no training happens.**
   - It is the only Phase-0 generator in the code, so it is the one used here, as the brief instructs.
   - Budget: Phase 0 lasts at least PHASE_EP_MIN[1] = 100 episodes x 200 = **20,000 transitions** (`infant_curriculum.py:53`). The H_pos gate can only lengthen it.
2. Timing pilot, on **non-registered seed 99** for harness sizing only (`bab_pilot_timing.py`). This was the only execution before this commit.
   - The 591c agent took class 1 on 300/300 steps, with h_pos 0.0.
   - Cost: 0.050 s per act step (591c); 0.063 s per native waking step (build_B); 0.0003 s per sense().
   - Both envs are 12 body / 250 world / 5 actions, so one encoder can read both.
3. E2 world head = `e2.world_transition` + `e2.world_action_encoder` (census `940c690c9dd`, row 101). The drivers' optimizer for it: Adam 3e-4, batch 32, clip 1.0, single-step MSE (`goal_pipeline_tier1.py:518-599`; addendum 1).

## Design (fixed)

**One env family, one encoder, only the action source varies.**
- Env: the real Phase-0 env. That is CausalGridWorldV2(size=12, resource_respawn_on_consume=True, pos/traj telemetry, Phase-0 env_kwargs), rebuilt every 200-step episode, with episode seed = seed*160 + k.
- Latent: the **native z_world read path** of the addendum-1 agent build (`build_B(seed)`: world_dim 32, deployed dims). Each episode's observation stream goes through that agent's own `sense()`, with `agent.reset()` at episode boundaries (the addendum-1 `collect` convention).
  - The encoder is random-init. No encoder training happens in Phase 0 or regime B, so this is the read path "at that point".
  - Every post-phase agent is a fresh build from the same seed. The probe asserts that its encoder parameters equal the reference's exactly.
- Secondary latent: a fixed PCA-32 of the raw world observation. It is fit on 3,000 uniform-random steps from separate env seeds and rescaled to z_world's mean norm (the addendum-1 ceiling). It applies to the open-loop heads only.
- Seeds: **106, 107, 108, 109, 110** (fresh). One process at a time, `torch.set_num_threads(2)`.

**Datasets** (N = 5,000 transitions each; see the deviation below):
- **D_L1 = D_BAB**: the real Phase-0 generator (591c agent, native act, 591h loop incl. `update_residue`/`update_z_goal`, scheduler novelty override), episodes k = 0..24.
- **D_L0**: same env seeds and episode structure. The action is a fixed class c0 with p = 0.8 (c0 drawn from {0..3} by the seed); otherwise it is uniform over the other three of {0..3}, iid per step.
- **D_L2**: same env seeds. A class is drawn uniformly from {0..3} and held for a run length drawn uniformly from {1,2,3,4}; this repeats.
- **D_BAB_SHUF**: D_L1 with its action labels permuted across timesteps (same class marginals).
- **D_POL**: native on-policy transitions, N = 5,000. The build_B agent runs StepHarness native waking with its untrained (init) world head, in episodes k = 25..49.
- Each dose reports its action-class entropy (nats) and mean run length.

**Heads.** Each arm gets a fresh E2 world head, which is the reference agent's init head. Training: 3,000 updates, batch 32, uniform sampling with replacement, Adam 3e-4, clip 1.0, single-step MSE on (z_t, one-hot class, z_{t+1}), action one-hot width 5.
- Harness gate, per head: `.grad` must be non-None on the world_transition and world_action_encoder parameters at update 1, and the parameter delta must be > 0. I report the fit (last-200 loss vs identity MSE).
- **If B1 does not fit or gets no gradient, I stop: that is a harness failure, not a result.**

**Arms.**
- Open-loop: **B0** (D_POL), **B1 = L1_pre** (D_L1), **B1S** (D_BAB_SHUF), **L0_pre**, **L2_pre**.
- Post-babbling phase. It is the same for every arm: P = 1,200 closed-loop steps (6 episodes, k = 50..55, the same env seeds for every arm). A FRESH build_B agent runs native E3 selection with the arm's head in place. The head keeps training online on the agent's own on-policy transitions, 9,000 updates in total (3x the babbling training exposure), spread evenly over the P steps. Batches are drawn from all on-policy transitions so far and start once there are 64 of them. There is no further babbling.
  - **L0_post, L1_post (= B2), L2_post**: the DR / BEH arms.
  - **B3**: L1_pre head, with every batch 25% from D_L1 and 75% on-policy.
  - Secondary, added now before any run: **L2R** = L2_pre with a 25% D_L2 replay mix. It is the retention test for a genuinely diverse babble source. **NB** = the untrained init head, trained on-policy only (the no-babbling baseline for BEH).
- **Deviation stated up front:** the brief says N = the Phase-0 budget (20,000) and N_post = 3 x N = 60,000 transitions per arm. At the measured Mac cost (0.05-0.063 s per act step), that would take ~9 h for 5 seeds. So:
  - N = 5,000, which is the first 25 of Phase 0's >= 100 episodes. Phase 0 does no learning, so its policy is stationary apart from residue and z_goal state.
  - The forgetting pressure is kept at 3x in gradient EXPOSURE (9,000 on-policy updates vs 3,000 babbling updates), drawn from 1,200 distinct on-policy transitions rather than 15,000.
- **Drop order if the cap is hit:** NB, then L2R, then B3, then D2. The DR arms are never dropped.

**Primary metric (the addendum-1 action discrimination).** It is measured on a held-out test set: 3,000 uniform-random-action steps over classes {0..3} (episodes k = 120..134), encoded through the same read path.
- For up to 300 test starts: swap the first action for each class in {0..3} and roll out with the native `E2.rollout_with_world`. The score is **whether the executed class's rollout is closest to the actual z_world at h = 1**. Chance = 0.25.
- Also reported: h = 3 and h = 5, the 5-class version, and fidelity k (H = 10; deepest h at which the median error beats persistence).

**Hazard stratification (fixed before looking at any other arm).** A seed is **hazard-trapped** iff its D_POL collection run (the native on-policy arm) has >= 3 early terminations per 1,000 steps (done before the 200-step episode end) OR >= 10 harm events per 100 steps. Otherwise it is **benign**. All verdicts are reported per seed and stratified.

## Criteria (fixed)

Let disc(X) = the h = 1 executed-closest rate over 4 classes on the test set (z_world latent).
- **M_S** = max(0.05, SD over the 5 seeds of disc(B0)).
- **M_DR** = max(0.05, SD over the 5 seeds of disc(L1_post)).

| id | criterion | verdict rule | domain |
|---|---|---|---|
| **S** sufficiency | disc(B1) - disc(B0) > M_S **and** disc(B1) - disc(B1S) > M_S | PASS in >= 4/5 seeds; otherwise FAIL | D1 |
| **R** retention | ret = (disc(B2) - disc(B0)) / (disc(B1) - disc(B0)) >= 0.5 | Evaluated only if S PASSES; otherwise CANNOT_DETERMINE. PASS in >= 4/5 seeds (a seed whose B1 gain <= M_S counts as fail) | D1 |
| **R3** retained replay | the same ratio with disc(B3) | Evaluated only if S PASSES and R FAILS; otherwise CANNOT_DETERMINE (reported descriptively) | D1 |
| **DR** dose-response (amendment) | after the post phase: disc(L0_post) < disc(L1_post) < disc(L2_post) strictly, **and** disc(L2_post) - disc(L0_post) > M_DR | PASS in >= 4/5 seeds; otherwise FAIL | D1 |

**Secondary and descriptive only. None of these is a gate, and none can replace a verdict above.**
- The PCA-32 column for S.
- The DR ordering by MEASURED dose entropy. Label order and entropy order may differ if the native L1 is less diverse than L0.
- L2 retention: (disc(L2_post) - disc(B0)) / (disc(L2_pre) - disc(B0)) against L2R's ratio. This is the one-off-vs-replay question for a genuinely diverse source.
- **D2 reach**: 20 probe states from a native waking run (init head, episodes k = 100..). At each, the native CEM pool is re-rolled with each head, and I record whether E3's `score_trajectory` argmin differs from its argmin under the native (init) head. Compare B1 against B1S, and also L2_pre and L2_post.
- **Depth-1 diagnostic column** (the evaluation-edge record, addendum 2 M2): at the same probe states, a cloned env gives the true next z_world for each class 0..4. I report Spearman(E3 J_pred, J_true) at full horizon and at depth 1, for the post-phase heads.
- **BEH** (amendment; a pre-registered prediction with a direction test, not a gate). Over the last 50% of the post phase (600 steps) I report:
  - env reward per 100 steps (the sum of `harm_signal`)
  - TRUE harm contacts (harm_signal < 0 events) and benefit contacts (harm_signal > 0 events)
  - executed-action entropy
  - early terminations
  All are stratified trapped/benign. **The user's prediction: reward L2 > L1 > L0, and harm L2 <= L0.** I report the per-seed ordering and the number of seeds matching it.
- **INTERPRETATION RULE (the user's, stated up front).** The pass found that >98% of E3's score variance comes from rollout steps > 5, which carry no action information, and that E3's main channels have no grounded valuation.
  - A null BEH with a PASSING DR does NOT falsify the developmental claim. It localises the block downstream, at E3 aggregation or valuation. The depth-1 column is the diagnostic for that.
  - A positive BEH is strong evidence.
  - If DR itself fails, the developmental claim is not supported at this scale.
- **No tuning, and no extra arms or seeds after seeing results.** Any post-hoc diagnostic will be labelled as such.
- **Unmeasurable here:** whether babbled data carries any value signal; nothing about valuation; D3 beyond the 600-step BEH window.

## PRE-REGISTRATION AMENDMENT 1 (2026-09-25T08:00Z, committed before any registered seed ran)

- **Why.** A smoke run on **non-registered seed 99** (`results/SMOKE_s99.log`; N = 400, P = 400) validated the pipeline end to end:
  - every head gets gradient (`grad_nonnull` True, 9,000 post updates done);
  - the probe states validate;
  - D2 and depth-1 are computed.

  It also measured the step cost under the current laptop contention (load average ~17, two other probes running): **0.14-0.19 s** per native waking step, against 0.063 s in the pilot. At N = 5,000 with all six post arms, that is ~2.5-3 h of compute for 5 seeds, which exceeds the cap.
- **Changes, fixed before any registered seed:**
  1. **N = 2,400** transitions per dataset (Phase-0 episodes k = 0..11 for the babbling doses; k = 25..36 for D_POL). P stays at 1,200 and POST_UPD at 9,000, so the forgetting exposure is now 3x the babbling training exposure in updates, and 0.5x N in distinct on-policy transitions.
  2. **B3 is dropped from the start**, per the orchestrator's stated drop order ("drop B3 first, keep B2"). R3 therefore reports CANNOT_DETERMINE (dropped for budget) whenever its precondition holds.
     - In disclosure: on the smoke seed the native generator emitted class 1 on 400/400 steps, so a 25% replay of it would add no action coverage.
     - **L2R is kept**: it is the only arm that tests retained replay of a diverse babble source.
     - NB is kept. If the running time exceeds ~22 min per seed, NB is dropped for the remaining seeds, and the record will say which.
  3. Nothing else changes: criteria, margins, seeds, metric and the interpretation rule are all as above.
