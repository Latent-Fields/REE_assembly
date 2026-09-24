# E2 world-rollout divergence and proposal state-invariance: undertraining artefact or structural defect?

- **STATUS: INTERIM** (first written 2026-09-24T18:15Z, updated 18:30Z, under an account usage-window cutoff; updated in place as cells land -- see "Done / not done" at the end)
- Session: `bt0924-rollout` (Worker D, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-e2-rollout-divergence-remeasure`
- Re-measures: Worker B `residue_consumer_reach_world_dim32_20260924.md` ("E2 world rollout diverges x1.2/step, 0.49 -> 327") and Worker C `monostrategy_type_a_vs_b_discrimination_20260924.md` ("proposal majority class identical at all 40 states").
- Code under test: ree-v3 `origin/main` @ `86594ec5eb`, private detached worktree. All file:line citations are against that commit.
- Probe: `evidence/planning/probes/rollout/rollout_fidelity_probe.py` (one cell per invocation), tabulated by `probes/rollout/summarize_rollout.py`; raw per-cell JSON in `probes/rollout/results/`. Mac CPU, `torch.set_num_threads(2)`, one process at a time.
- Evidence domains reached: **D1** (rollout fidelity by horizon; proposal class share) and **D2** (E3's own J re-scored under native depth truncation and a deep-step shuffle, on the same candidate sets). D3 not run.

## Verdict so far

1. **B's divergence reproduces exactly (0.486 -> 326, x1.209/step) and is an artefact of an UNTRAINED E2 world head.** B's warmup trains E1 and E2's z_self head only (`compute_e2_loss`, `agent.py:12830-12846`); the world head's parameter delta is **0.0000**. The growth is the random-init residual map `z + MLP(z, a)` iterated 30 times. **But that untrained head is a real production condition:** ree_core has NO waking objective for E2's world head (its only native trainer, `compute_e2_world_loss`, `agent.py:12849`, runs in sleep behind `use_sleep_world_forward_consolidation`, default False, `config.py:7476`). Whether it is trained is up to each driver; at most 30 of the 60 most recent drivers do.
2. **Train the head and the blow-up recedes with dose (t30 norm 326 -> 3.6 -> 1.0), but the prediction never becomes informative.** Fidelity **k = 0 in all 7 cells**: two recipes, 0-3000 head steps (20-100 episodes in C's recipe), clamp on or off. The open-loop rollout is 5-800x worse than predicting "nothing changes" one step out, and its predicted displacement is orthogonal (regime B) or anti-aligned (C's recipe, cos -0.17 to -0.28) to the actual one. One positive: in C_100 the executed first action is ranked correctly at h = 1 (95% vs 25% chance); by h = 3 that is gone.
3. **E3's choice is driven by exactly those uninformative deep steps (D2).** Truncating E3's own J to the first 1-5 steps changes the selected candidate 78-100% of the time; swapping steps > d with another candidate's changes it 100% of the time; >98% of J's cross-candidate variance comes from steps > 5 in every cell. The channel that carries it is F with the untrained head and the residue term (plus harm in C's recipe) once the head is trained. The SD-056 clamp bounds the norm and changes none of this.
4. **C's state-invariant proposal reproduces at world_dim 32 in both recipes and at every dose, and is NOT caused by the rollout.** Majority first-action class identical at 30/30 states; restricting CEM scoring to 1-10 steps changes nothing; the terrain_prior's initial mean alone decodes to the majority class at all 30 states, before any rollout is scored.
5. **Earliest broken edge:** E2 multi-step prediction is broken and sits upstream of the residue repair and of E3's choice. Generation (the proposal map) is broken independently of it. And the encoded z_world may be the deeper limit: it moves 0.0002-0.006 per step against a norm of ~0.48, with 1.4-2.9% of that explained by the executed action. Step 6 names the test that separates "E2 cannot learn" from "z_world gives E2 nothing to learn".

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
| B_BWF_3000 +clamp | 1.79 | 0.93 (1.055) | 0.0038 vs 0.0002 vs 0.028 | 15.6 / 13.8 / 18.9 / 100 | 0.07 | 0.12 / 0.01 | **0** |
| C_20 (1061 recipe) | 1.61 | 10.8 (1.159) | 0.051 vs 0.0056 vs 0.068 | 9.1 / 12.3 / 20.6 / 356 | 0.08 | **-0.28** / -0.09 | **0** |
| C_100 (1061 recipe) | 2.69 | 3.16 (1.125) | 0.051 vs 0.0055 vs 0.065 | 9.2 / 11.5 / 16.4 / 88 | 0.09 | **-0.17** / -0.15 | **0** |

Action discrimination (M2b; added after the first cells): swap the FIRST action of the executed sequence for each one-hot class, keep the rest; is the executed class's rollout the one closest to what actually happened? chance = 1/action_dim.

| cell | h=1 | h=3 | h=5 |
|---|---|---|---|
| B_BWF_3000 +clamp (A=5, chance 0.20) | 0.007 (mean rank 3.97 of 0..4) | 0.007 | 0.007 |
| C_100 (A=4, chance 0.25) | **0.947** (rank 0.11) | 0.00 (rank 1.66) | 0.02 |

Readings:
1. **The norm blow-up is an untraining artefact, and dose-responsive once the head is trained.** B regime t30 norm 326 -> 3.6 -> 1.0 over 0 / 600 / 3000 world-head steps; C regime 10.8 -> 3.2 over 20 -> 100 episodes. The clamp removes it by construction (pins the norm at 2x the start).
2. **The rollout never becomes informative: k = 0 in every cell, trained or not, clamped or not.** The best cell (B_BWF_3000) is still 5x worse than "nothing changes" one step out, and only 14% of starts beat persistence. Direction is uninformative (cos 0.01-0.15) in regime B and **anti-aligned** in C's regime (cos -0.17 to -0.28 at h=1-3: the model predicts movement the wrong way). C's recipe does not improve from 20 to 100 episodes at h=1 (abs error 0.051 both).
3. **The one positive:** in C_100 the model ranks the executed first action correctly at h=1 (95% vs 25% chance) -- the action effect is encoded one step out, even though magnitude and direction are wrong. It is gone by h=3 (0%). In regime B (monostrategy: 295/298 executed actions were one class) there is no action discrimination at all, and the executed action is ranked worst.
4. **Confound, stated:** the waking agent is monostrategy (one class for 88-99% of executed steps) and in regime B barely moves (actual one-step displacement 0.0002-0.0012 against a visited norm of 0.49), so persistence is nearly perfect by construction. Cells re-run with a uniform-random action stream (M2R) are below/pending; they are the fair fidelity test.
5. Consistent with two landed runs in other regimes: V3-EXQ-1075 (`skill_vs_identity` negative on every arm) and V3-EXQ-1081 (persistence-relative skill 0.06-0.21 at h=1, negative after sleep). No regime yet measured has an E2 world head that beats copying its input.

## Step 4: does it matter to the consumer (D2) -- E3's own J on the recorded candidate sets

Every recorded E3 candidate set (42-80 selects per cell, up to 60 re-scored) re-scored with `E3.score_trajectory` (`e3_selector.py:1621`) under: FULL; TRUNC_d = native SD-081 depth limit `_score_depth_limit = d+1` (`e3_selector.py:1304-1322`); SHUF_d = world steps > d replaced by a deranged other candidate's steps. `native selected == J argmin` 0.83-1.00, so J's argmin is (almost always) the selection.

| cell | J cross-candidate spread carried by (std) | TRUNC argmin = FULL, d = 1 / 3 / 5 / 10 | SHUF argmin = FULL, d<=3 / 10 | J variance from steps > 5 |
|---|---|---|---|---|
| B_B_600 | F 3.41 (of J 3.39) | 0.02 / 0.00 / 0.00 / 0.00 | 0.00 / 0.00 | 1.00 |
| B_B_600 +clamp | residue 0.005, harm 0.001 (J 0.006) | 0.02 / 0.10 / 0.17 / 0.26 | 0.00 / 0.12 | 0.75 |
| B_BWF_600 | residue 2.08 (J 2.10) | 0.10 / 0.10 / 0.15 / 0.40 | 0.00 / 0.00 | 1.00 |
| B_BWF_3000 | residue 0.733 (J 0.735) | 0.03 / 0.08 / 0.10 / 0.24 | 0.00 / 0.00 | 1.00 |
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
| B_B_600 +clamp | 0.882 (0.881) | 2.30 | class 1 at 30/30 | class 1 at 30/30 | 1.9% |
| B_BWF_3000 +clamp | 0.885 (0.884) | 2.27 | class 1 at 30/30 | class 1 at 30/30 | 0.9% |
| C_20 | 0.679 (0.678-0.679) | 2.33 | class 2 at 30/30 | class 2 at 30/30 | 2.1% |
| C_100 | 0.681 (0.681) | 2.33 | class 2 at 30/30 | class 2 at 30/30 | 2.6% |

(z_world itself varies 16-20% per dimension across the same 30 states.)

- **C's finding reproduces at world_dim 32, in both regimes, at every dose:** majority class identical at 30/30 states, ~2.3 classes per pool (the SP-CEM floor token). In C's own regime the BC-trained terrain_prior (loss 1.88 -> 0.38 from 20 to 100 episodes) does not make it state-dependent.
- **It is not caused by the rollout.** Restricting CEM scoring to the first 1-10 steps moves the majority share by <= 0.004 and never changes the majority class; world-head training and the clamp change nothing.
- **It is fixed before any rollout is scored.** The terrain_prior's initial action-object mean (`hippocampal/module.py:562-610`), decoded through `action_object_decoder`, already gives the majority class at all 30 states. Its state variation is 0.9-2.6% of its magnitude against 16-20% in z_world: the proposal map compresses state variation away. In regime B terrain_prior and the decoder have no training objective at all (B's Q1; docstring at `hippocampal/module.py:700-745`; `action_object_invariance_spike_2026-07-22.md`); in C's regime they are trained to imitate E3's selections, and E3's selections are themselves driven by uninformative deep rollout steps (Step 4) and are one class 74-87% of the time. That behavioural-cloning loop is a candidate mechanism for why training does not add state dependence -- **correlation only, not tested causally here.**

## Step 6: verdict

| Finding (source) | Verdict | Basis |
|---|---|---|
| E2 world rollout diverges x1.2/step, 0.49 -> 327 (Worker B) | **Harness artefact of an UNTRAINED head -- but the untrained head is a real production condition.** | B's warmup never reaches `world_transition` (delta 0.0); training the head removes the blow-up dose-dependently (t30 326 -> 3.6 -> 1.0). ree_core has no waking objective for the head, so every driver that does not train it (up to half of recent drivers) runs exactly B's divergent rollout. |
| E2 multi-step prediction is informative (implicit premise of every z_world scorer) | **Structural failure, not undertraining, over the doses measured** | k = 0 in all 7 cells (0 to 3000 head steps; two recipes; clamp on/off): the rollout never beats persistence at any horizon, direction is uninformative or anti-aligned. C's recipe does not improve 20 -> 100 episodes. (10000-step dose and random-policy fidelity pending -- see Done/not done.) |
| Deep rollout steps matter to the consumer (brief step 4) | **They drive it** (D2) | Truncating E3's J to steps <= 5 changes the argmin 78-100%; swapping deep steps changes it 100%; >98% of J's discriminating variance is in steps > 5. |
| Proposal majority class state-invariant (Worker C) | **Structural in both recipes, and NOT caused by the rollout** | 30/30 states, all doses, clamp on/off; CEM scoring window 1-10 changes nothing; the terrain_prior mean alone fixes the class before any rollout is scored. |

**Is E2 multi-step prediction the earliest broken edge?** It is broken, and it sits upstream of both the residue repair and E3's choice: whatever channel wins E3's J reads the deepest, least faithful rollout steps. But two things sit at or before it and must not be skipped:
1. **Proposal (generation) is broken independently of the rollout** -- the candidate pool's first action is fixed by a state-compressing, untrained-or-self-imitating proposal map before E2 is consulted. So "prediction of alternatives" fails on both halves: the alternatives proposed are not state-conditioned, and their predicted consequences are not informative.
2. **The representation may be the deeper limit.** The encoded z_world moves 0.0002-0.006 per step against a norm of ~0.48, and only 1.4-2.9% of that displacement is explained by the executed action (M2c, monostrategy-confounded). An E2 cannot beat persistence on a latent whose step changes are this small and this weakly action-coupled. That is the known observation -> z_world binding constraint (`cross_plan_root_cause_synthesis_20260902.md`, 39 of 43 nodes). This probe cannot separate "E2's objective fails" from "z_world gives E2 nothing to predict"; the discriminating test is named below.

**Smallest mechanistically honest repair candidates (none built):**
- (R1) **A native waking objective for E2's world head** (the single-step MSE drivers already hand-roll, moved into the agent loop). Fixes the untrained-head divergence that half the drivers run. It does NOT fix fidelity: every trained cell here is still k = 0.
- (R2) **Match the scored horizon to measured fidelity** (native SD-081 `_score_depth_limit` for E3, `max_horizon` for CEM): stops E3 choosing on the least faithful steps. Honest only as a guard: with k = 0 there is no faithful depth to match to, so it makes E3 myopic rather than informed.
- (R3) **A multi-step (rollout-consistency) objective for E2's world head**, the E2 analogue of `SD-e1-rollout-consistency-training` ITEM 2. That lineage's own evidence (V3-EXQ-976: accuracy objectives DAMP per-action divergence at depth; V3-EXQ-1000: contrastive endpoints diverge without fidelity) says a pure accuracy or pure contrastive term will not do it alone.
- (R4) **Rollout normalisation (the SD-056 clamp).** Measured here: bounds the norm, leaves k = 0 and leaves E3 reading the deep steps. Not a repair of fidelity.
- (R5) **A state-conditioned proposal map** (terrain_prior/decoder trained on something other than imitation of E3's own picks). Separate from R1-R4; needed whatever E2 does.

**What would discriminate** (all cheap, all `complex (probe-gated)`):
- R1-vs-representation: train E2's world head on a latent where action effects are large and known (a fixed PCA-32 of the world observation -- the representation 1010/1002 found carries more action-relevant structure than trained z_world, 0.878 vs 0.678 oracle-action agreement), same data, and measure k. If k > 0 there, the representation is the earliest broken edge and E2 repairs are premature; if k stays 0, E2's objective/architecture is.
- R2: re-run M3 with E3 depth-limited to d = 1..3 and measure closed-loop harm/benefit (D3). If behaviour does not change, the deep-step drive is irrelevant noise for behaviour; if it improves, R2 is worth a flag.
- R5: pool class share vs state with terrain_prior trained on a state-conditioned target (e.g. the class of the best candidate under a TRUNC_1 score) against the BC target, matched steps.

## Done / not done (INTERIM)

- DONE: step 1 (no checkpoint; dose series used); step 2 canary; steps 3-5 in 7 cells (regime B: head untrained 600, trained 600/3000, clamp on untrained 600 and trained 3000; regime C at world_dim 32: 20 and 100 episodes); step 6 verdict on that evidence.
- RUNNING (one process at a time): B_BWF_10000 (dose extension); random-policy fidelity M2R on BWF_3000, C_20 and the untrained head; a second seed (42) for BWF_3000.
- NOT DONE: D3 (closed loop); the discriminating tests in step 6.
