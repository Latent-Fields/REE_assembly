# E2 world-rollout divergence and proposal state-invariance: undertraining artefact or structural defect?

- **STATUS: FINAL for this pass + ADDENDUM (encoding vs E2 objective discriminator, end of file)** (interim versions 18:15Z-18:45Z; final 2026-09-24T18:57:06Z). Limits in "Done / not done".
- Session: `bt0924-rollout` (Worker D, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-e2-rollout-divergence-remeasure`
- Re-measures: Worker B `residue_consumer_reach_world_dim32_20260924.md` ("E2 world rollout diverges x1.2/step, 0.49 -> 327") and Worker C `monostrategy_type_a_vs_b_discrimination_20260924.md` ("proposal majority class identical at all 40 states").
- Code under test: ree-v3 `origin/main` @ `86594ec5eb`, private detached worktree. All file:line citations are against that commit.
- Probe: `evidence/planning/probes/rollout/rollout_fidelity_probe.py` (one cell per invocation), tabulated by `probes/rollout/summarize_rollout.py`; raw per-cell JSON in `probes/rollout/results/`. Mac CPU, `torch.set_num_threads(2)`, one process at a time.
- Evidence domains reached: **D1** (rollout fidelity by horizon and policy; action discrimination; proposal class share) and **D2** (E3's own J re-scored under native depth truncation and a deep-step shuffle, on the same candidate sets). D3 not run.

## Verdict

1. **B's divergence reproduces exactly (0.486 -> 326, x1.209/step) and is an artefact of an UNTRAINED E2 world head.** B's warmup trains E1 and E2's z_self head only (`compute_e2_loss`, `agent.py:12830-12846`); the world head's parameter delta is **0.0000**. The growth is the random-init residual map `z + MLP(z, a)` iterated 30 times. **But that untrained head is a real production condition:** ree_core has NO waking objective for E2's world head (its only native trainer, `compute_e2_world_loss`, `agent.py:12849`, runs in sleep behind `use_sleep_world_forward_consolidation`, default False, `config.py:7476`). Whether it is trained is up to each driver; at most 30 of the 60 most recent drivers do.
2. **Train the head and the blow-up disappears with dose** (t30 norm 326 -> 3.6 -> 1.0 -> 0.52 at 0 / 600 / 3000 / 10000 steps). Norm divergence: **undertraining (untraining) artefact.**
3. **Fidelity is ON-POLICY and action-blind.** The trained rollout tracks where z_world drifts under the policy it was trained on in some cells (k = 5-15 steps beating persistence: seed 42 waking; seed 43 and C's recipe under a uniform-random policy) and fails in others (k = 0 in all monostrategy waking cells where the agent barely moves, and seed 42 under random actions). **What it never does is tell actions apart:** swapping the first action for each alternative, the executed one is the closest prediction at chance level under random actions (0.18-0.33 vs 0.20-0.25 chance, n = 18-28, three trained cells), and near 0 in the monostrategy cells. One exception: C_100 at h = 1 on-policy (0.95 vs 0.25), gone by h = 3. The untrained head is k = 0 everywhere. **Prediction of alternatives -- which is what candidate scoring needs -- is not delivered at any dose measured (0-10000 head steps).** Error vs persistence is still falling at 10000 steps, so slow undertraining of on-policy fidelity is not excluded; action-blindness shows no dose trend.
4. **E3's choice is driven by the deep rollout steps (D2), in all 11 cells.** Truncating E3's own J to the first 1-5 steps changes the selected candidate 78-100% of the time; swapping steps > d with another candidate's changes it 100% of the time; >98% of J's cross-candidate variance comes from steps > 5 (75% in the one clamp cell where J's spread collapses). Channel: F with the untrained head, residue (plus harm in C's recipe) once trained. Since the rollout does not carry action-specific consequence, E3 is discriminating candidates on action-conditional extrapolation error. The SD-056 clamp bounds the norm and changes none of this.
5. **C's state-invariant proposal reproduces at world_dim 32 in both recipes, both seeds and every dose, and is NOT caused by rollout depth.** Majority first-action class identical at 30/30 states in all 9 cells measured; restricting CEM scoring to 1-10 steps changes nothing; the terrain_prior's initial mean is already one class at all 30 states before any rollout is scored (its state variation 0.4-2.6% of magnitude vs 15-27% in z_world). Whether the step-1 score contributes was not isolated.
6. **Earliest broken edge (D1, named with its uncertainty):** upstream of E2 there is a stronger candidate. Under uniform-random actions, **only 2.3-3.1% of the encoded z_world's per-step displacement is explained by which action was taken** (eta-squared, 4 cells, action independent of state by construction). A latent whose step changes are ~97% action-independent gives any forward model almost nothing action-conditional to learn, which is exactly the action-blindness in item 3. So the chain reads: observation -> z_world does not encode action consequence (candidate earliest edge) -> E2 cannot predict alternatives (measured) -> E3 ranks candidates on deep-step extrapolation noise (measured, D2); and, independently, the proposal is not state-conditioned (measured). This probe cannot separate "z_world lacks action consequence" from "E2 fails to learn it"; step 6 names the test that does.

## Step 1: is there a production-trained agent at world_dim=32?

**No production checkpoint on the current substrate exists anywhere reachable from the Mac.** Searched: every `*.pt/*.pth/*.ckpt/*.safetensors` under `REE_Working` (one unrelated MECH-268 pilot snapshot), `~/.ree_maturation_prefix_cache/` (18 files: harm-encoder-only curriculum legs, no E2), `~/.ree_probe_warmup_cache/` (37 SD-074 `probe_warmup.v1` agent snapshots, world_dim 32 -- `e2.world_transition.0.weight` (128, 37) -- warmed 0-40 episodes x 300 steps, written 2026-07-19..09-09 on older substrate for the EXQ-777/784 telemetry lineage). The arm-reuse plan banks RESULTS, not weights (`arm_reuse_fingerprint_plan.md` scope excludes checkpoint reuse), and experiment drivers do not save agents. Fell back to the brief's DOSE series on the current substrate.

What "production-trained" can mean here, measured rather than assumed: there is no single production training recipe. Of the 60 most recent drivers (`v3_exq_1028`..`1097`), at most 30 train `world_transition` (grep for a world-head training call in the driver or in an imported `_lib` trainer); the other 30 contain no such call, so wherever they score E2 rollouts they score a random-init world head (not checked per driver). ree_core supplies no waking loss for it. Drivers that do train it use single-step MSE (`goal_pipeline_tier1.warmup_train`, V3-EXQ-1061's 042-derived loop) or SD-056 InfoNCE (`allon_training`).

## Step 2: canary -- does B's measurement reproduce, and did B measure the production path?

| Cell | recipe | world head param delta | cand. z_world norm p50 t0 / t1 / t5 / t10 / t20 / t30 | late growth/step |
|---|---|---|---|---|
| B_B_600_s43 (B's exact cell) | B's warmup, 600 steps | **0.0000** | 0.486 / 0.68 / 2.37 / 6.8 / 48.7 / 326 | 1.209 |
| B's own record (s43) | same | not measured | 0.49 / 0.68 / 2.37 / 6.80 / 48.8 / 327 | ~1.2 |

- **Reproduces to three figures.** Norms are read from the candidate `world_states` that `E3.score_trajectory` receives inside `E3.select` (hook on the call at `e3_selector.py:3288`), i.e. the production consumer path. B hooked `ResidueField.evaluate_trajectory` from `compute_residue_cost` -- the same tensors (`e3_selector.py:1386-1394` reads them through `_get_world_states`, `:1304`). B measured the right path.
- **What B's harness did not do: train the thing it measured.** B's warmup is `Adam(agent.parameters())` on `compute_prediction_loss() + compute_e2_loss()`; the first is E1 (`agent.py:11584`), the second is z_self-only (`agent.py:12830-12846`). World head delta 0.0 -> B's "same warmed or unwarmed" observation is explained: both cells ran the random-init head. The rollout is `z_{t+1} = z_t + world_transition([z_t, W_a a_t])` (`e2_fast.py:201-222`, loop `:822`), an untrained residual MLP; its fixed-point-free drift compounds at ~1.2x.

## Step 3: rollout fidelity (D1) -- dose series at world_dim 32 (deployed)

Recipes. **B** = B's warmup (world head untrained). **BWF** = B's warmup PLUS the canonical single-step world_forward MSE (Adam 3e-4, batch 32, buffer 2000, clip 1.0; `goal_pipeline_tier1.py:518-599`). **C** = V3-EXQ-1061's own builder + warmup at world_dim = self_dim = 32 (5x5 grid, 1 hazard, 2 resources; world_forward single-step MSE lr 1e-3 every 4 steps, terrain_prior + decoder trained by behavioural cloning of E3's selections, `v3_exq_1061_...py:395-560`). **+clamp** = SD-056 lever (b) `e2_rollout_output_norm_clamp_enabled` ratio 2.0 (`e2_fast.py:789-`; default False `config.py:927`; armed by ~82 drivers).

Open-loop fidelity: from up to 150 visited z_world_t, native `E2.rollout_with_world` with the EXECUTED action sequence, compared to the actual encoded z_world_{t+h}. Persistence = ||z_t - z_{t+h}||; chance = distance to a random visited state; cos = cosine(predicted displacement, actual displacement). **k = deepest h at which the median rollout error is below the median persistence error.**

| cell | world-head delta | t30 cand. norm (growth/step) | abs err h=1 vs persistence vs chance | err/persistence h=1 / 5 / 10 / 30 | frac starts beating persistence h=1 | cos h=1 / 5 | **k** |
|---|---|---|---|---|---|---|---|
| B_B_600 (untrained) | 0.0 | 326 (1.209) | 0.39 vs 0.0007 vs 0.029 | 571 / 368 / 535 / 1.6e4 | 0.00 | 0.05 / 0.09 | **0** |
| B_B_600 +clamp | 0.0 | 0.96 (1.000, pinned at 2x t0) | 0.39 vs 0.0005 vs 0.033 | 816 / 276 / 131 / 44 | 0.00 | 0.12 / -0.02 | **0** |
| B_BWF_600 | 0.73 | 3.58 (1.160) | 0.012 vs 0.0007 vs 0.040 | 16.4 / 14.3 / 25.8 / 289 | 0.10 | 0.04 / 0.04 | **0** |
| B_BWF_3000 | 1.66 | 1.00 (1.062) | 0.0059 vs 0.0012 vs 0.045 | 4.97 / 5.02 / 5.84 / 33 | 0.14 | 0.15 / 0.04 | **0** |
| **B_BWF_10000** | 2.25 | 0.52 (1.004) | 0.0027 vs 0.0007 vs 0.037 | 3.93 / 2.32 / 2.12 / 11.4 | 0.13 | 0.04 / 0.07 | **0** |
| B_BWF_3000 **seed 42** | 1.66 | 0.69 (1.041) | agent moves (2 actions); n = 20 starts | 0.58 / 0.97 / 1.84 / 42 | 0.60 | 0.88 / 0.76 | **5** |
| B_BWF_3000 +clamp | 1.79 | 0.93 (1.055) | 0.0038 vs 0.0002 vs 0.028 | 15.6 / 13.8 / 18.9 / 100 | 0.07 | 0.12 / 0.01 | **0** |
| C_20 (1061 recipe) | 1.61 | 10.8 (1.159) | 0.051 vs 0.0056 vs 0.068 | 9.1 / 12.3 / 20.6 / 356 | 0.08 | **-0.28** / -0.09 | **0** |
| C_100 (1061 recipe) | 2.69 | 3.16 (1.125) | 0.051 vs 0.0055 vs 0.065 | 9.2 / 11.5 / 16.4 / 88 | 0.09 | **-0.17** / -0.15 | **0** |

Action discrimination (M2b; added after the first cells): swap the FIRST action of the executed sequence for each one-hot class, keep the rest; is the executed class's rollout the one closest to what actually happened? chance = 1/action_dim.

| cell | h=1 | h=3 | h=5 |
|---|---|---|---|
| B_BWF_10000 (A=5, chance 0.20) | 0.007 (rank 3.95) | 0.00 | 0.00 |
| B_BWF_3000 +clamp (A=5, chance 0.20) | 0.007 (mean rank 3.97 of 0..4) | 0.007 | 0.007 |
| C_100 (A=4, chance 0.25) | **0.947** (rank 0.11) | 0.00 (rank 1.66) | 0.02 |

**Waking cells are policy-confounded.** The waking agent is monostrategy (one action class on 74-99% of executed steps) and in regime B seed 43 it barely moves (actual one-step displacement 0.0002-0.0012 against a visited norm of 0.49), so persistence is nearly perfect by construction. The fair test is a **uniform-random action stream** (M2R: agent.sense only, no selection, actions one-hot and independent of state). Starts need 31 steps inside one episode, and random-policy episodes are short, so n is small (11-28 starts) -- read these as indicative.

| cell (random policy) | n | err/persistence h=1 / 5 / 10 / 30 | frac beating persistence h=1 | cos h=1 / 5 / 10 | **k** | executed first action closest (h=1 / 3 / 5; chance) | actual dz explained by action (eta^2) |
|---|---|---|---|---|---|---|---|
| B_B_600 (untrained) | 11 | 16.5 / 39.8 / 85 / 3.5e3 | 0.00 | 0.13 / 0.18 / 0.27 | **0** | 0.09 / 0.36 / 0.46 (0.20) | 0.026 |
| B_BWF_3000 s43 | 24 | 0.57 / 0.87 / 1.48 / 16 | 0.67 | 0.85 / 0.77 / 0.65 | **6** | 0.25 / 0.21 / 0.21 (0.20) | 0.024 |
| B_BWF_3000 s42 | 28 | 2.87 / 3.64 / 5.49 / 113 | 0.29 | 0.37 / 0.16 / 0.02 | **0** | 0.18 / 0.21 / 0.29 (0.20) | 0.031 |
| C_20 (1061 recipe) | 18 | 0.34 / 0.42 / 0.58 / 7.9 | 0.89 | 0.96 / 0.92 / 0.84 | **15** | 0.33 / 0.17 / 0.22 (0.25) | 0.023 |

Readings:
1. **The norm blow-up is an untraining artefact, dose-responsive once the head is trained.** B regime t30 norm 326 -> 3.6 -> 1.0 -> 0.52 over 0 / 600 / 3000 / 10000 world-head steps (late growth 1.209 -> 1.004); C regime 10.8 -> 3.2 over 20 -> 100 episodes. The clamp removes it by construction (pins the norm at 2x the start).
2. **Waking fidelity is k = 0 in every monostrategy cell, trained or not, clamped or not** -- but that is largely the confound above. Error relative to persistence falls with dose there (h=1: 571 -> 16 -> 5.0 -> 3.9 at 0 / 600 / 3000 / 10000 steps). Where the agent does move (seed 42, two actions) the trained head beats persistence out to k = 5 on-policy (cos 0.88 at h=1).
3. **Under random actions the trained rollout tracks z_world's drift in 2 of 3 trained cells (k = 6 and 15; cos 0.84-0.96 at h=1) and fails in the third (seed 42, k = 0).** The untrained head is k = 0. So fidelity is real but policy-dependent: the head learns the dynamics of the actions the agent takes, and generalises to other actions only sometimes.
4. **The rollout does not tell actions apart.** Under random actions the executed first action's rollout is the closest to what happened at chance level (0.18-0.33 vs 0.20-0.25) in all three trained cells; in the monostrategy waking cells it is near 0 (ranked last). The one exception is C_100 on-policy at h = 1 (0.95 vs 0.25), gone by h = 3. Where the rollout is accurate, it is accurate about the action-INDEPENDENT drift.
5. **The encoded z_world barely carries action consequence.** Under random actions only 2.3-3.1% of the per-step displacement variance is explained by the action taken (eta-squared of the class-mean displacement; action independent of state by construction). There is little action-conditional signal for any forward model to learn. This is the strongest single number in the record for where the loop is first broken, and it is D1 only.
6. Consistent with two landed runs in other regimes: V3-EXQ-1075 (`skill_vs_identity` negative on every arm) and V3-EXQ-1081 (persistence-relative skill 0.06-0.21 at h = 1, negative after sleep).

## Step 4: does it matter to the consumer (D2) -- E3's own J on the recorded candidate sets

Every recorded E3 candidate set (42-180 selects per cell, up to 60 re-scored) re-scored with `E3.score_trajectory` (`e3_selector.py:1621`) under: FULL; TRUNC_d = native SD-081 depth limit `_score_depth_limit = d+1` (`e3_selector.py:1304-1322`); SHUF_d = world steps > d replaced by a deranged other candidate's steps. `native selected == J argmin` 0.83-1.00, so J's argmin is (almost always) the selection.

| cell | J cross-candidate spread carried by (std) | TRUNC argmin = FULL, d = 1 / 3 / 5 / 10 | SHUF argmin = FULL, d<=3 / 10 | J variance from steps > 5 |
|---|---|---|---|---|
| B_B_600 | F 3.41 (of J 3.39) | 0.02 / 0.00 / 0.00 / 0.00 | 0.00 / 0.00 | 1.00 |
| B_B_600 +clamp | residue 0.005, harm 0.001 (J 0.006) | 0.02 / 0.10 / 0.17 / 0.26 | 0.00 / 0.12 | 0.75 |
| B_BWF_600 | residue 2.08 (J 2.10) | 0.10 / 0.10 / 0.15 / 0.40 | 0.00 / 0.00 | 1.00 |
| B_BWF_3000 | residue 0.733 (J 0.735) | 0.03 / 0.08 / 0.10 / 0.24 | 0.00 / 0.00 | 1.00 |
| B_BWF_10000 | residue 0.096 (J 0.096) | 0.06 / 0.13 / 0.17 / 0.23 | 0.00 / 0.00 | 0.99 |
| B_BWF_3000 seed 42 | residue 5.64 (J 5.64) | 0.07 / -- / 0.05 / -- | 0.00 / -- | 1.00 |
| B_BWF_3000 +clamp | residue 0.94 (J 0.94) | 0.05 / 0.09 / 0.07 / 0.07 | 0.00 / 0.00 | 1.00 |
| C_20 | residue 0.857, harm 0.253 (J 0.74) | 0.02 / 0.02 / 0.08 / 0.30 | 0.00 / 0.00 | 0.98 |
| C_100 | residue 2.10, harm 0.274 (J 1.92) | 0.05 / 0.08 / 0.22 / 0.27 | 0.00 / 0.00 | 0.98 |

- **The deep steps DRIVE E3's choice in every cell** -- the worse of the brief's two outcomes. Scoring only the first 1-5 steps (where the rollout is least wrong) picks a different candidate 78-100% of the time; swapping in another candidate's deep steps changes the pick 100% of the time for d <= 3 in every cell. 98-100% of the cross-candidate variance E3 discriminates on lives in steps > 5 (75% in the one cell where the clamp flattens everything and J spread collapses to 0.006).
- **The channel that carries it depends on the regime, the input does not.** Untrained head: F (`compute_reality_cost`, `e3_selector.py:1324-1349`, mean squared step displacement, so the largest-drift steps dominate). Trained head: F's spread collapses (<=0.0014) and the residue term takes over, with harm_eval second in C's regime: both read z_world at the deep steps, where rollouts have left the visited manifold (B's Q2). This is the scale-monopoly pattern already recorded for V3-EXQ-936/936a/571b, traced one step upstream to its input.
- **The clamp does not fix it.** It bounds the norm but leaves k = 0, and with the head trained, E3 still reads >99% of its discrimination off steps > 5.

## Step 5: proposal state-dependence (C's P3 measure) on the same agents

`hippocampal.propose_trajectories` at 30 states along the waking run; first-action class via `candidate_first_action_class` (`hippocampal/module.py:669`). Arms: native, and CEM elite scoring restricted to `max_horizon = d` (1, 2, 3, 5, 10) through `_score_trajectory`'s own window argument (`hippocampal/module.py:1691`, `:1770-1773`).

| cell | majority share native (window 1..10) | classes/pool | majority class across 30 states | terrain_prior mean alone -> first-action class | ao-mean state variation / magnitude |
|---|---|---|---|---|---|
| B_B_600 | 0.883 (0.882-0.883) | 2.27 | class 1 at 30/30 | class 1 at 30/30 | 2.3% |
| B_BWF_600 | 0.883 (0.883) | 2.27 | class 1 at 30/30 | class 1 at 30/30 | 1.6% |
| B_BWF_3000 | 0.883 (0.885-0.887) | 2.23-2.27 | class 1 at 30/30 | class 1 at 30/30 | 0.9% |
| B_BWF_10000 | 0.883 (0.883) | 2.27 | class 1 at 30/30 | **class 2** at 30/30 | 0.6% |
| B_BWF_3000 seed 42 | 0.754 (0.754) | 2.27 | class 4 at 30/30 | class 4 at 30/30 | 0.4% |
| B_B_600 +clamp | 0.882 (0.881) | 2.30 | class 1 at 30/30 | class 1 at 30/30 | 1.9% |
| B_BWF_3000 +clamp | 0.885 (0.884) | 2.27 | class 1 at 30/30 | class 1 at 30/30 | 0.9% |
| C_20 | 0.679 (0.678-0.679) | 2.33 | class 2 at 30/30 | class 2 at 30/30 | 2.1% |
| C_100 | 0.681 (0.681) | 2.33 | class 2 at 30/30 | class 2 at 30/30 | 2.6% |

(z_world itself varies 15-27% per dimension across the same 30 states.)

- **C's finding reproduces at world_dim 32, in both regimes, at every dose:** majority class identical at 30/30 states, ~2.3 classes per pool (the SP-CEM floor token). In C's own regime the BC-trained terrain_prior (loss 1.88 -> 0.38 from 20 to 100 episodes) does not make it state-dependent.
- **It is not caused by the rollout.** Restricting CEM scoring to the first 1-10 steps moves the majority share by <= 0.004 and never changes the majority class; world-head training and the clamp change nothing.
- **Its state-invariance is present before any rollout is scored.** The terrain_prior's initial action-object mean (`hippocampal/module.py:562-610`), decoded through `action_object_decoder`, is itself one class at all 30 states in every cell, and equals the pool majority in 8 of 9 cells (at 10000 steps the CEM's noisy samples around that mean decode to a different, but equally state-invariant, class -- so the mean alone is not the whole mechanism; sampling through the decoder is part of it). Its state variation is 0.9-2.6% of its magnitude against 16-20% in z_world: the proposal map compresses state variation away. In regime B terrain_prior and the decoder have no training objective at all (B's Q1; docstring at `hippocampal/module.py:700-745`; `action_object_invariance_spike_2026-07-22.md`); in C's regime they are trained to imitate E3's selections, and E3's selections are themselves driven by uninformative deep rollout steps (Step 4) and are one class 74-87% of the time. That behavioural-cloning loop is a candidate mechanism for why training does not add state dependence -- **correlation only, not tested causally here.**

## Step 6: verdict

| Finding (source) | Verdict | Basis |
|---|---|---|
| E2 world rollout diverges x1.2/step, 0.49 -> 327 (Worker B) | **Harness artefact of an UNTRAINED head -- but the untrained head is a real production condition.** | B's warmup never reaches `world_transition` (delta 0.0); training the head removes the blow-up dose-dependently (t30 326 -> 3.6 -> 1.0). ree_core has no waking objective for the head, so every driver that does not train it (up to half of recent drivers) runs exactly B's divergent rollout. |
| E2 multi-step prediction is informative (implicit premise of every z_world scorer) | **Norm: artefact. On-policy drift: partly learned (k 5-15 in 3 of 7 trained measurements). Action-conditional consequence: NOT learned at any dose (0-10000 head steps) -- structural at the budgets measured, and the latent itself carries ~2-3% action-explained displacement** | Step 3 tables; action discrimination at chance under random actions in all trained cells |
| Deep rollout steps matter to the consumer (brief step 4) | **They drive it** (D2) | Truncating E3's J to steps <= 5 changes the argmin 78-100%; swapping deep steps changes it 100%; >98% of J's discriminating variance is in steps > 5. |
| Proposal majority class state-invariant (Worker C) | **Structural in both recipes (every dose), and NOT caused by rollout depth** | 30/30 states, all doses, clamp on/off; CEM scoring window 1-10 changes nothing; the proposal map is state-invariant before any rollout is scored (terrain_prior mean one class at 30/30 in every cell). |

**Is E2 multi-step prediction the earliest broken edge?** Its action-conditional half is broken, and it sits upstream of both the residue repair and E3's choice: whatever channel wins E3's J reads the deepest rollout steps, which carry no action-specific information. But two things sit at or before it and must not be skipped:
1. **Proposal (generation) is broken independently of the rollout** -- the candidate pool's first action is fixed by a state-compressing, untrained-or-self-imitating proposal map before E2 is consulted. So "prediction of alternatives" fails on both halves: the alternatives proposed are not state-conditioned, and their predicted consequences are not informative.
2. **The representation is the stronger candidate for the earliest edge.** Under uniform-random actions only 2.3-3.1% of z_world's per-step displacement is action-explained (4 cells, unconfounded by policy). An E2 cannot beat persistence on a latent whose step changes are this small and this weakly action-coupled. That is the known observation -> z_world binding constraint (`cross_plan_root_cause_synthesis_20260902.md`, 39 of 43 nodes). This probe cannot separate "E2's objective fails" from "z_world gives E2 nothing to predict"; the discriminating test is named below.

**Smallest mechanistically honest repair candidates (none built):**
- (R1) **A native waking objective for E2's world head** (the single-step MSE drivers already hand-roll, moved into the agent loop). Fixes the untrained-head divergence that half the drivers run. It does NOT give action discrimination: every trained cell here is at chance on it.
- (R2) **Match the scored horizon to measured fidelity** (native SD-081 `_score_depth_limit` for E3, `max_horizon` for CEM): stops E3 choosing on the least faithful steps. Honest only as a guard: the faithful depth is policy-dependent (0-15) and in no cell action-discriminative, so it makes E3 myopic rather than informed.
- (R3) **A multi-step (rollout-consistency) objective for E2's world head**, the E2 analogue of `SD-e1-rollout-consistency-training` ITEM 2. That lineage's own evidence (V3-EXQ-976: accuracy objectives DAMP per-action divergence at depth; V3-EXQ-1000: contrastive endpoints diverge without fidelity) says a pure accuracy or pure contrastive term will not do it alone.
- (R4) **Rollout normalisation (the SD-056 clamp).** Measured here: bounds the norm, leaves waking k = 0 and leaves E3 reading the deep steps. Not a repair of fidelity.
- (R5) **A state-conditioned proposal map** (terrain_prior/decoder trained on something other than imitation of E3's own picks). Separate from R1-R4; needed whatever E2 does.

**What would discriminate** (all cheap, all `complex (probe-gated)`):
- R1-vs-representation: train E2's world head on a latent where action effects are large and known (a fixed PCA-32 of the world observation -- the representation 1010/1002 found carries more action-relevant structure than trained z_world, 0.878 vs 0.678 oracle-action agreement), same data, and measure k. If k > 0 there, the representation is the earliest broken edge and E2 repairs are premature; if k stays 0, E2's objective/architecture is.
- R2: re-run M3 with E3 depth-limited to d = 1..3 and measure closed-loop harm/benefit (D3). If behaviour does not change, the deep-step drive is irrelevant noise for behaviour; if it improves, R2 is worth a flag.
- R5: pool class share vs state with terrain_prior trained on a state-conditioned target (e.g. the class of the best candidate under a TRUNC_1 score) against the BC target, matched steps.

## Done / not done

- DONE: step 1 (no checkpoint on the current substrate; dose series used); step 2 canary; steps 3-5 in 11 cells (regime B: untrained head 600 steps; trained 600 / 3000 / 10000; clamp on untrained 600 and trained 3000; seed 42 at 3000; C's recipe at world_dim 32, 20 and 100 episodes; random-policy fidelity on four of them); step 6.
- NOT DONE: D3 (closed loop); a larger random-policy sample (n 11-28 starts per cell -- the k values under random actions are indicative, not tight); more seeds (seed 43 and 42 disagree on random-policy k); the discriminating tests in step 6.
- Run log (all from `/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/rollout/`, worktree `ree-v3-wt` @ `86594ec5eb`): `rollout_fidelity_probe.py --regime B --recipe {B,BWF} --dose {600,3000,10000} --seed {43,42} [--clamp]` and `--regime C --dose {20,100} --seed 11`; defaults wake 300, H 30, n-starts 150, max-selects 60, n-states 30, depths 1,2,3,5,10. `_v2` cells are re-runs of the same config with the M2b/M2c/M2R readouts (bit-identical on the shared metrics). Wall 48-830 s per cell.

## ADDENDUM (2026-09-24, session `bt0924-rollout-b`): encoding or E2 objective? The discriminator

- Commissioned by the orchestrator as the follow-on this record proposed. Code: ree-v3 `origin/main` @ `07de5a282e`, a fresh private worktree. Its only ree_core difference from `86594ec5eb` is two E3 kwargs guards in `agent.py`, which this probe does not reach. `e2_fast.py` and `latent/` are unchanged.
- Probe: `probes/rollout/encoding_vs_objective_probe.py` (reuses `build_B` / `warm_B` from `rollout_fidelity_probe.py` verbatim). Results: `probes/rollout/results/ENC_*.json`. Regime B: CausalGridWorldV2 8x8, world_dim 32, seeds 43 and 42. Wall 5-75 s per cell after warmup.
- **Design.** All data use **uniform-random one-hot actions**, so the action is independent of state by construction. Train: ~7,600 transitions (~390 episodes, median length 19). Test: ~2,850 transitions from different episodes.
  - **Step 1 (ceiling).** Action signal per step is measured two ways: eta-squared of the displacement by action, and held-out accuracy of a linear softmax decoder that reads the action from the displacement (chance 0.20). It is measured in three latents: the RAW world observation (250-d); a FIXED PCA-32 of RAW (fit on 3,000 random-policy steps from a different env seed, then frozen; 86% of variance; rescaled to z_world's mean norm); and z_world from `agent.sense`.
  - **Step 2.** A fresh `E2FastPredictor` world head (same architecture) is trained with the dose series' optimiser (Adam 3e-4, batch 32, clip 1.0, single-step MSE) for 3,000 and 10,000 steps on each latent. It is evaluated on held-out episodes with the native `rollout_with_world`: fidelity k (H = 10, or 20 in one cell), and action discrimination (executed first action closest to outcome, chance 0.20).
  - **Added control.** The same transitions, but each training batch drawn 95% or 99% from ONE action class. That is the distribution the monostrategy agent generates for itself: 88-99% of waking steps were one class in the main record's cells.

### A correction first: in regime B, "z_world at the dose points" is ONE encoder, the random-init one

Encoder (`latent_stack`) parameter delta after B's 600-step warmup is **0.0000**, and after BWF 3,000 it is also **0.0000**. Neither recipe reaches the encoder: E1 and world_forward train on detached z_world. So the main record's dose series varied only the E2 head, and every cell in it scored a **frozen random projection** as z_world. This is the same defect `experiments/_lib/zworld_p0_warmup.py` documents for the x728/x737 driver family ("z_world stays a FROZEN RANDOM PROJECTION"). Encoder-trained arms were therefore added with SD-070's own recipe (`run_zworld_p0`, RandomPolicy): 20x50 steps at preservation 1000 (V3-EXQ-1093's setting), and 60x50 at the default config. Encoder deltas were 2.66 and 5.59 (encoder norm 17.7). Not measured: whether V3-EXQ-1061's recipe trains the encoder.

### Step 1: the ceiling (uniform-random actions)

| latent | eta-squared (dz by action) | linear action decode, held-out (chance 0.20) | step / state norm |
|---|---|---|---|
| RAW world obs | 0.072-0.073 | **0.86-0.88** | 3.4 / 6.3 |
| PCA-32 (fixed) | 0.099-0.103 | **0.78-0.80** | 0.33 / 0.44 |
| z_world, random-init encoder (all regime-B dose points; seeds 43, 42) | 0.011-0.012 | **0.51-0.52** | 0.016 / 0.48 |
| z_world, SD-070 P0 20x50 (pres 1000) | 0.011 | 0.52 | 0.031 / 0.92 |
| z_world, SD-070 P0 60x50 (default) | 0.034 | 0.52 | 0.082 / 1.36 |

**The observation is not action-blind**, so the stop condition does not fire. **The encoding loses a large share of the action signal:** linear decodability drops from 0.79 (PCA) to 0.51-0.52 (z_world), and eta-squared drops about 9x. The SD-070 encoder training at these budgets does not recover it (decode 0.52 in both arms).

### Step 2: a fresh E2 world head on each latent

| latent (cell) | budget, batch distribution | **k** (H cap) | err/persistence h=1 / 5 / 10 | cos h=1 | **executed action closest, h = 1 / 3 / 5** (chance 0.20) |
|---|---|---|---|---|---|
| PCA-32 (s43) | 3000 uniform | >=10 (**20** at H=20) | 0.50-0.52 / 0.52-0.53 / 0.54-0.56 | 0.87-0.88 | **0.77-0.78 / 0.62-0.63 / 0.51-0.52** |
| PCA-32 (s43) | 10000 uniform | >=10 | 0.42 / 0.48 / 0.51 | 0.91 | **0.82 / 0.67 / 0.54** |
| PCA-32 (s42) | 3000 / 10000 uniform | >=10 | 0.50 / 0.42 at h=1 | 0.87 / 0.90 | 0.74 / 0.79 at h=1; 0.49 at h=5 |
| z_world random enc (s43 x4 cells, s42) | 3000 uniform | 9 to >=10 (**16** at H=20) | 0.43-0.71 / 0.46-0.71 / 0.63-1.01 | 0.63-0.90 | **0.36-0.49 / 0.35-0.42 / 0.29-0.36** |
| z_world random enc (s43 x3, s42) | 10000 uniform | >=10 | 0.58-0.64 / 0.55-0.62 / 0.64-0.69 | 0.71-0.81 | **0.46-0.53 / 0.44-0.48 / 0.37-0.44** |
| z_world SD-070 P0 (20x50; 60x50) | 10000 uniform | >=10 | 0.56; 0.65 at h=1 | 0.84; 0.74 | 0.43; 0.48 at h=1 |
| PCA-32 (s43, s42) | 3000, **95% one class** | >=10 (20) | 0.66-0.67 at h=1 | 0.56-0.58 | 0.69-0.75 / 0.49-0.51 / 0.37-0.40 |
| z_world (s43 x2, s42, P0) | 3000, **95% one class** | 8-13 | 0.47-0.75 at h=1 | 0.62-0.89 | 0.31-0.35 / 0.25-0.35 / 0.24-0.33 |
| PCA-32 (s43, s42) | 3000, **99% one class** | **0** | **1.28-1.41 / 1.35-1.69** | 0.11-0.15 | **0.25-0.29 / 0.20-0.23 / 0.20-0.21** |
| z_world (s43, s42, P0) | 3000, **99% one class** | **0** | **3.75-5.52 / 4.67-9.33** | 0.20-0.36 | **0.17-0.23 / 0.16-0.23 / 0.16-0.23** |

### Read-out: none of the three pre-registered cases fits cleanly, and the evidence points to a fourth

1. **E2's objective and architecture work** when given action-diverse data. On BOTH latents the unchanged single-step-MSE head beats persistence out to k >= 9-20 (vs k = 0 in the main record), with cos 0.7-0.9. It discriminates the executed action well above chance on both: 0.74-0.82 on PCA-32 and 0.36-0.53 on z_world at h = 1, still 0.29-0.54 at h = 5. So it is not "bad on both", and R1/R3 (a new E2 objective) is **not** where the earliest defect lies.
2. **The encoding is a real, secondary loss.** On identical data and budget, E2 on z_world discriminates actions at roughly half the rate it achieves on PCA-32 (0.36-0.53 vs 0.74-0.82 at h = 1), matching the step-1 ceiling (decode 0.51 vs 0.79). That is "worse on z_world", not "bad on z_world". The observation -> z_world encoder (a frozen random projection in every regime-B cell; SD-070 training at these budgets does not recover the signal) roughly halves the attainable action discrimination. It is not what makes E2 action-blind.
3. **What reproduces the main record's failure is the TRAINING DISTRIBUTION.** Draw the same transitions 99% from one action class and E2 collapses on BOTH latents to exactly the main record's signature: k = 0, worse than persistence (1.3-5.5x at h = 1), cos 0.11-0.36, discrimination at chance (0.16-0.29). At 95% it survives (above chance, k >= 8). The waking agent's own data is 88-99% one class. Main-record cell recipes BWF and C trained E2 on that data, and both came out action-blind with k = 0 on-policy.
4. **So the earliest broken edge for "prediction of alternatives" is the monostrategy loop, not E2 and not (primarily) the encoder.** The state-invariant proposal (main record, step 5) makes the agent act one way; E2 trains on that one action, so it never learns the others; its alternatives are then uninformative, and E3 ranks candidates on uninformative deep steps (step 4). The self-imitating terrain_prior in V3-EXQ-1061's recipe closes the loop. The encoder loss is an independent ceiling that halves what a fix could reach.
5. **Domain: D1 only.** These are prediction-quality measurements of freshly trained heads. None of these heads was put back in front of E3, and no behaviour was measured. The causal claim "monostrategy data -> action-blind E2" is an intervention on the training distribution (D2-shaped for E2 as consumer of its training data); "-> E3 choice" is inferred from the main record's step 4, not re-measured with these heads.

Limits: H capped at 10 (20 in one cell) because random-policy episodes are short (median 19), so "k >= 10" is a floor, not a value. There are two seeds. PCA-32 was rescaled to z_world's norm, but its per-step displacement is 75% of its norm against 3% for z_world, and the MSE objective sees that difference; the ratio metrics are scale-free, the learning dynamics are not. The skew control uses action class 1 only. V3-EXQ-1061's recipe was not re-tested here.

**What this changes in step 6 (repair ranking, none built).**
- (R6, new, first): **action-diverse data for E2's world head.** Options are an exploration or random-action fraction in its training buffer, class-balanced replay (the sleep trainer `compute_e2_world_loss`, `agent.py:12859` (`min_batch_classes=1` at `:12941`) @ `07de5a282e`, replays distinct transitions but deliberately sets `min_batch_classes=1` and does not balance action classes, so it would inherit the skew), or training in a phase before commitment. The discriminating test: re-run the main record's step 3/4 with the head trained on class-balanced replay of the agent's own buffer. If E3's truncation sensitivity then drops (steps <= k start carrying J's variance), the loop is confirmed at D2.
- R5 (state-conditioned proposal) is upstream of R6 and would remove the cause rather than compensate for it.
- R1 (native waking world-head objective) is still needed, since up to half of recent drivers never train the head. It must come with R6, or it will reproduce the 99%-skew failure.
- The encoder (SD-070 / representation) is a real but second-order ceiling. R3/R4 are demoted: the objective works when fed diverse data, and the clamp addresses only the norm.

