# E3 evaluation edge: does a learned consequence value give directed benefit-seeking?

- **STATUS: INTERIM (seed 42 only, 5 arms), 2026-09-24T20:26:42Z.** Seeds 43/44 and two extra arms (E5/E6, the native benefit recipe) are running. Nothing below is a verdict yet.
- Session: `bt0924-evaluation` (Worker F, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-e3-evaluation-edge-test`.
- Follows: `e2_rollout_divergence_and_proposal_state_dependence_20260924.md` ADDENDUM 3 (origin `1b09b81b4d`), the partitioned R5/COV/R2 closed-loop test.
- Code under test: ree-v3 `origin/main` @ `44c55300ca` (private detached worktree; the same commit as ADDENDUM 3). All file:line citations are against it.
- Probe: `.scratch/breakthrough-20260924/evaluation/evaluation_edge_probe.py`. It imports ADDENDUM 3's harness unchanged (`partitioned_repair_probe.py`, `balanced_replay_probe.py`, `encoding_vs_objective_probe.py`, `rollout_fidelity_probe.py`) and runs its preamble in the same RNG order. Regime B: CausalGridWorldV2 8x8, 2 hazards, 3 resources, world_dim 32 (deployed). SD-070 encoder at 20x50 steps, preservation 1000. Mac CPU, 2 threads, one process at a time, ~13 min per seed.

## Premises re-measured

1. **The E0 NATIVE and E1 FULL canaries reproduce ADDENDUM 3 bit-for-bit on seed 42.** Reward per 100 steps is -8.762 and -0.778, harm events per 100 are 68.5 and 8.5, and the executed-action counts are identical to `PART_s42.json`. So the arms below differ from ADDENDUM 3's only by the evaluators.
2. **"No loss in ree_core trains harm_eval_head" holds, but ree_core does have a benefit loss.** `REEAgent.compute_benefit_eval_loss` (`agent.py:11701`) is an MSE of `benefit_eval(z_world)` on `benefit_exposure`, which is body_state[11], the resource-proximity field the agent observes. ree_core never calls it; about 17 landed drivers do (for example `v3_exq_074c_...py:258-265`). The brief's premise that the benefit head might have no landed recipe is corrected here. Arms E5/E6 (running) use that recipe. E2-E4 use the contact-label analogue the brief asked for.
3. **The benefit channel is off by default and gated.** `benefit_eval_enabled` is False (`config.py:1327`). Even when enabled, `score_trajectory` subtracts B only after `_benefit_samples_seen >= 50` (`e3_selector.py:695`, gate at `:1737-1739`). Only `record_benefit_sample` increments that count (`:1209-1216`), and nothing in ree_core calls it.
4. **The env's benefit shaping never fires in this regime.** `benefit_approach` occurs 0 times in 3,000 labelled steps on seed 42. `hazard_approach` wins every tie when both proximity fields are active (`causal_grid_world.py:2736`; its module docstring `:47-53` says benefit_approach is "structurally unreachable" at default multi-source configs unless `proximity_approach_magnitude_tiebreak=True`). So every positive reward here is a resource CONSUMPTION, and every "harm event" in ADDENDUM 3's outcome table is mostly a hazard-PROXIMITY step (for example, native run: 726 hazard_approach against 317 contacts).

## Evaluators (agent's own experience only)

- **Labels** come from the env reward stream the agent receives: reward < 0 means harm, reward > 0 means benefit. No env internals are used. Label state = the encoded ARRIVAL state z_{t+1}. That is what E3 scores under the depth-2 limit (`world_states[1]`). This deviates from V3-EXQ-1061, which labels the pre-step theta_z (`v3_exq_1061_...py:520-528`).
- **Data:** two runs through the agent's own SD-070 encoder, pooled. One is a native waking run of 1,500 steps (head A, E3 selecting). The other is a uniform-random-action run of 1,500 steps, the same kind of data the COV head is trained on. 80/20 train/held-out split.
- **Harm head:** V3-EXQ-1061's BCE recipe (`v3_exq_1061_...py:557-575`): class-balanced batches, k = min(16, npos, nneg) per class, Adam 1e-3, clip 1.0, at least 8 per class. Run offline for 1,500 updates.
- **Benefit head (E2-E4):** the same recipe on benefit labels.
- **E4 control:** the same z's, with harm and benefit labels permuted independently across the training timesteps, so the label marginals are the same.
- **Weights:** `lambda_ethical` 1.0 and `benefit_weight` 1.0 (defaults). `rho_residue` stays at 0.5.

| seed 42 | native run: harm / benefit labelled | random run: harm / benefit | harm head held-out AUC | benefit head held-out AUC | shuffled AUC (harm / benefit) |
|---|---|---|---|---|---|
| counts | 1043 (317 contacts) / **4** | 1259 (109 contacts) / **37** | 0.82 (n+ 481) | 0.83 (**n+ 4**) | 0.48 / 0.30 |

**The data-coverage edge, first finding.** Across 3,000 own-experience steps the agent consumed a resource 41 times, and only 4 of those came from its own policy. The training split holds 37 positives. **So the native warmup gate (50) stays SHUT, and E3 would never use the trained benefit head.** For E2-E4 the gate was forced open (`_benefit_samples_seen := 50`), and this is labelled wherever it matters. The benefit head's held-out AUC rests on 4 positives and is not a reliable number.

## Seed 42 closed loop (600 steps, fresh agent per arm, as ADDENDUM 3)

| arm | reward / 100 | harm events / 100 (contacts) | benefit events / 100 (contacts) | episodes ended | action entropy | majority share | choice quality vs env-Q (chance 0.20) |
|---|---|---|---|---|---|---|---|
| E0 NATIVE | -8.76 | 68.5 (107) | 0.67 (4) | 45 | 0.70 | 0.59 | 0.24 (always class 2) |
| E1 FULL (R5b+COV+R2) | **-0.78** | **8.5 (8)** | 0.00 (0) | 5 | 0.72 | 0.81 | 0.20 |
| E2 FULL+EVAL | -1.62 | 17.8 (17) | 0.50 (3) | 9 | 1.06 | 0.63 | 0.18 |
| E3 EVAL-only | -8.72 | 67.2 (106) | 0.67 (4) | 45 | 0.72 | 0.58 | 0.24 (always class 2) |
| E4 FULL+SHUF | -6.53 | 52.8 (75) | 0.50 (3) | 33 | 0.77 | 0.57 | 0.24 |

Scorer reach was confirmed by call counters on `compute_harm_cost_fallback` and `compute_benefit_score`. Both are called on every E3 scoring pass in E2-E4 (5,472 to 13,728 calls per arm), and the benefit gate is open in those arms.

Interim reading (seed 42 only):
- **Not directed success.** E2 adds 3 benefit contacts against FULL's 0, but harm doubles (8.5 -> 17.8 per 100; contacts 8 -> 17).
- **E2 beats E4 by a wide margin.** Trained evaluators on the same data do much less damage than permuted ones (-1.62 vs -6.53). So the trained heads carry real signal into E3. But an added evaluator term, trained or not, disrupts the residue-based harm avoidance FULL relies on.
- **Evaluation alone does nothing without R5/R2.** E3 is indistinguishable from NATIVE (-8.72 vs -8.76; same action profile).
- **Choice quality does not improve** (E2 0.18 vs E1 0.20).
- 3 against 0 benefit contacts is within noise.
