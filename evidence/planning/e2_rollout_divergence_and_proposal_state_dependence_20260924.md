# E2 world-rollout divergence and proposal state-invariance: undertraining artefact or structural defect?

- **STATUS: INTERIM** (written 2026-09-24T18:1xZ under an account usage-window cutoff; updated in place as cells land -- see "Done / not done" at the end)
- Session: `bt0924-rollout` (Worker D, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-e2-rollout-divergence-remeasure`
- Re-measures: Worker B `residue_consumer_reach_world_dim32_20260924.md` ("E2 world rollout diverges x1.2/step, 0.49 -> 327") and Worker C `monostrategy_type_a_vs_b_discrimination_20260924.md` ("proposal majority class identical at all 40 states").
- Code under test: ree-v3 `origin/main` @ `86594ec5eb`, private detached worktree. All file:line citations are against that commit.
- Probe: `evidence/planning/probes/rollout/rollout_fidelity_probe.py` (one cell per invocation), tabulated by `probes/rollout/summarize_rollout.py`; raw per-cell JSON in `probes/rollout/results/`. Mac CPU, `torch.set_num_threads(2)`, one process at a time.
- Evidence domains reached: **D1** (rollout fidelity by horizon; proposal class share) and **D2** (E3's own J re-scored under native depth truncation and a deep-step shuffle, on the same candidate sets). D3 not run.

## Verdict so far (one paragraph)

B's number reproduces exactly (0.486 -> 326, x1.209/step), but **it is not an undertraining trend and not a structural property of a trained E2: in B's harness the E2 world head is never trained at all.** `REEAgent.compute_e2_loss()` trains only the z_self head (`agent.py:12830-12846`, `predict_next_self`); nothing in B's warmup reaches `e2.world_transition` (measured parameter delta **0.0000** after 600 steps). The x1.2/step growth is the random-init residual map `z + MLP(z,a)` iterated 30 times. That is the stale premise to correct. **The structural fact underneath it is real and larger:** ree_core has NO waking objective for E2's world head at all -- the only native trainer is `compute_e2_world_loss()` (`agent.py:12849`), reached only from sleep consolidation behind `use_sleep_world_forward_consolidation` (default False, `config.py:7476`; `sleep/phase_manager.py:777-785`). Whether the rollout E3 scores is trained is decided by each driver: only 30 of the 60 most recent drivers contain a world-head training call directly or via an imported `_lib` trainer (a grep, so an upper bound). Once the head IS trained with the canonical single-step MSE (`experiments/_lib/goal_pipeline_tier1.py:518-599`), the norm blow-up recedes with dose (x1.16 late-step growth at 600 steps, x1.06 at 3000; t30 norm 3.6 -> 1.0) -- so the divergence is dose-responsive -- **but the prediction never becomes informative: at every dose and every horizon the open-loop rollout is WORSE than predicting "nothing changes" (fidelity k = 0), and the predicted displacement is nearly orthogonal to the actual one (cos 0.03-0.15).** And E3 does read the deep steps: in every cell, >99% of the cross-candidate variance of E3's J comes from rollout steps beyond d=5, and replacing steps > d with another candidate's steps changes E3's argmin 100% of the time. **So the consumer's choices are driven by rollout content that carries no information about actual consequence.** The proposal state-invariance is a separate defect, upstream of the rollout: restricting CEM scoring to the first d steps leaves the pool unchanged (majority class 1 at 30/30 states in every arm), and the terrain_prior's own mean decodes to class 1 at all 30 states before any rollout is scored.

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

## Step 3: rollout fidelity (D1) -- dose series, regime B (CausalGridWorldV2 8x8, world_dim 32 = deployed)

Recipe BWF = B's warmup PLUS the canonical single-step world_forward MSE (Adam 3e-4, batch 32, buffer 2000, clip 1.0). Open-loop: from 150 visited z_world_t, native `E2.rollout_with_world` with the EXECUTED actions, compared to the actual encoded z_world_{t+h}. Persistence baseline = ||z_t - z_{t+h}||; chance = distance to a random visited state. k = deepest h at which median rollout error < median persistence error.

| cell | world-head delta | wf loss (last 50) | t30 cand. norm | late growth | err/persistence h=1 / 5 / 10 / 30 | frac starts beating persistence h=1 | cos(pred delta, actual delta) h=1 / 5 | **k (beats persistence)** |
|---|---|---|---|---|---|---|---|---|
| B_B_600 (untrained head) | 0.0 | -- | 326 | 1.209 | 571 / 368 / 535 / 1.6e4 | 0.00 | 0.05 / 0.09 | **0** |
| B_BWF_600 | 0.73 | 3.9e-6 | 3.58 | 1.160 | 16.4 / 14.3 / 25.8 / 289 | 0.10 | 0.04 / 0.04 | **0** |
| B_BWF_3000 | 1.66 | 7.6e-7 | 1.00 | 1.062 | 4.97 / 5.02 / 5.84 / 33 | 0.14 | 0.15 / 0.04 | **0** |

Readings:
1. **The norm blow-up is an undertraining (in fact untraining) artefact.** It shrinks monotonically with world-head training dose (t30 326 -> 3.6 -> 1.0).
2. **The prediction is uninformative at every horizon and every dose measured.** The rollout never beats persistence (k = 0 in all cells). It beats the random-state baseline only out to h = 3 (600) / 7 (3000), and only because the visited manifold is tiny: the actual one-step displacement is ~0.0025 against a visited norm of 0.49, and a random visited state is only ~0.02 away. Direction is essentially orthogonal (cos 0.03-0.15). "Norm bounded, direction uninformative" is the better description at dose; it is not a bounded-direction blow-up.
3. This matches two landed findings from other regimes: V3-EXQ-1075 (`skill_vs_identity` negative on every arm, OFF -5.48; per-step displacement ~0.014 at world_dim 16) and V3-EXQ-1081 (held-out persistence-relative skill 0.06-0.21 at h=1 before sleep, negative after). The E2 world head does not beat copying the input, one step out, in any regime yet measured.

## Step 4: does it matter to the consumer (D2) -- E3's own J on the recorded candidate sets

Every recorded E3 candidate set (44-61 selects per cell) re-scored with `E3.score_trajectory` under: FULL; TRUNC_d = native SD-081 depth limit `_score_depth_limit = d+1` (`e3_selector.py:1304-1322`); SHUF_d = world steps > d replaced by a deranged other candidate's steps. `native_sel == J argmin` 0.98-1.00, so J's argmin is the selection.

| cell | J spread (std) carried by | TRUNC argmin same as FULL, d = 1 / 3 / 5 / 10 | SHUF argmin same, any d | share of J cross-candidate variance from steps > d (d<=5) |
|---|---|---|---|---|
| B_B_600 | F (reality/coherence) std 3.41 of 3.39 | 0.02 / 0.00 / 0.00 / 0.00 | 0.00 | 1.00 |
| B_BWF_600 | residue std 2.08 of 2.10 | 0.10 / 0.10 / 0.15 / 0.40 | 0.00 | 1.00 |
| B_BWF_3000 | residue std 0.733 of 0.735 | 0.03 / 0.08 / 0.10 / 0.24 | 0.00 | 1.00 |

- **The deep steps DRIVE E3's choice** (the worse of the brief's two outcomes). Truncating the score to the steps where the rollout is least wrong changes the selection 60-100% of the time; swapping in another candidate's deep steps changes it 100% of the time, at every d tested.
- Which channel carries it depends on the dose: with the untrained head it is F (`compute_reality_cost`, `e3_selector.py:1324-1349`: mean squared step displacement, so the steps with the largest drift dominate); once the head is trained the F spread collapses (0.00017) and the residue term takes over (its query points leave the manifold at depth, B's Q2). This is the channel-monopoly-by-scale pattern already recorded for 936/936a/571b, now traced to its input: whichever channel is largest reads the deepest, least faithful rollout steps.
- Candidate discriminability: >99% of J's cross-candidate variance lives in steps > 5 in every cell. The first 5 steps, where the rollout is closest to the manifold, carry <1% of what E3 discriminates on.

## Step 5: proposal state-dependence (C's P3 measure) on the same agents

`hippocampal.propose_trajectories` at 30 states along the waking run; first-action class via `candidate_first_action_class` (`hippocampal/module.py:669`). Arms: native, and CEM elite scoring restricted to `max_horizon = d` via `_score_trajectory`'s own window argument (`hippocampal/module.py:1691`, `:1770-1773`).

| cell | arm | majority share | classes/pool | majority class across 30 states | terrain_prior mean alone -> class |
|---|---|---|---|---|---|
| B_B_600 | native / window 1..10 | 0.883 / 0.882-0.883 | 2.27 | class 1 at 30/30 | class 1 at 30/30 |
| B_BWF_600 | native / window 1..10 | 0.883 / 0.883 | 2.27 | class 1 at 30/30 | class 1 at 30/30 |
| B_BWF_3000 | native / window 1..10 | 0.883 / 0.885-0.887 | 2.23-2.27 | class 1 at 30/30 | class 1 at 30/30 |

- C's finding reproduces at world_dim 32 in regime B: the majority class is state-invariant (30/30), with ~2 classes per pool (the SP-CEM floor token).
- **It is not caused by the rollout.** Restricting CEM scoring to the first 1-10 steps moves the majority share by <= 0.004 and never changes the majority class. World-head training (0 -> 3000 steps) does not change it either.
- **It is set before any rollout is scored:** the terrain_prior's initial action-object mean (`hippocampal/module.py:562-610`) decoded through `action_object_decoder` gives class 1 at all 30 states. The state variation of that mean is 0.9-2.3% of its magnitude, against 16-17% per-dim variation in z_world itself. terrain_prior and the decoder have no native training objective (B's Q1; `candidate_first_action_class` docstring `:700-745`; `action_object_invariance_spike_2026-07-22.md`). In regime B they are at random init, so the CEM starts at one fixed action-object ball whose argmax class is the decoder's bias class, and 3 CEM iterations never leave it.

## Done / not done (INTERIM)

- DONE: step 1 (no checkpoint; dose series used), step 2 canary, step 3 fidelity at doses 0/600/3000 (seed 43), step 4 D2 in the same cells, step 5 in regime B.
- RUNNING / QUEUED (one process at a time): C's regime at world_dim 32 (V3-EXQ-1061 builder + its warmup, which DOES train terrain_prior by behavioural cloning and world_forward) at 20 and 100 episodes; SD-056 lever (b) norm clamp ON for the untrained and 3000-step heads (82 drivers arm it); a 10000-step dose; the M2b/M2c action-discrimination readouts (added after the first three cells).
- NOT DONE: second seed; D3.
