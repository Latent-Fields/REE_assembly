# E3 evaluation edge: does a learned consequence value give directed benefit-seeking?

- **STATUS: FINAL for this pass, 2026-09-24T21:10Z.** Interim (seed 42, 5 arms) was `81da9c5963`. Limits are under "Done / not done".
- Session: `bt0924-evaluation` (Worker F, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-e3-evaluation-edge-test`.
- Follows: `e2_rollout_divergence_and_proposal_state_dependence_20260924.md` ADDENDUM 3 (origin `1b09b81b4d`), the partitioned R5/COV/R2 closed-loop test.
- Code under test: ree-v3 `origin/main` @ `44c55300ca`, in a private detached worktree. It is the same commit as ADDENDUM 3, and all file:line citations are against it.
- Probes: `probes/evaluation/evaluation_edge_probe.py` (closed loop, 7 arms), `probes/evaluation/eval_split_probe.py` (evaluator on true vs predicted arrival states), and `probes/evaluation/summarize_eval.py`. Raw JSON is in `probes/evaluation/results/`.
  - Both probes import ADDENDUM 3's harness unchanged from `probes/rollout/`: `partitioned_repair_probe.py`, `balanced_replay_probe.py`, `encoding_vs_objective_probe.py`, `rollout_fidelity_probe.py`. Copy them next to the probes to re-run.
  - Both probes run ADDENDUM 3's preamble in the same RNG order.
- Regime B: CausalGridWorldV2 8x8, 2 hazards, 3 resources, world_dim 32 (the deployed value), SD-070 encoder at 20x50 steps with preservation 1000.
- Run conditions: Mac CPU, 2 threads, one process at a time. Wall time was 4.5-13 min per seed for the closed loop and 2-8 min per seed for the split.
- **Domain reached: D3** on env reward for the closed loop (3 seeds), and **D2** for the evaluator -> E3-pick edge (term spread and drop-evaluator flip rate; evaluator on true vs predicted states).

## Verdict

1. **Evaluation is NOT the next broken edge by the brief's criterion. Directed success happened in 0 of 3 seeds.**
   - Trained harm and benefit evaluators on top of FULL (arm E2) raised benefit contacts in 2 of 3 seeds, but harm got worse in those same 2 seeds:
     - s42: harm 8.5 -> 17.8 per 100 steps; benefit contacts 0 -> 3.
     - s44: harm 3.0 -> 18.7; benefit contacts 1 -> 4.
   - In the third seed (s43) the agent froze: harm fell (7.3 -> 2.2), benefit went to 0, and entropy went 0.72 -> 0.05.
   - Mean over the 3 seeds, FULL vs E2: reward -0.46 vs -0.91 per 100 steps; harm events 6.3 vs 12.9; benefit events 0.11 vs 0.39.
   - E2 beat the shuffled-label control E4 on benefit in 1 of 3 seeds.
2. **The benefit gains are undirected, and the trained HARM head drives them, not the benefit head.**
   - E5 swaps in the native benefit recipe. That recipe's benefit term has negligible cross-candidate spread (std 0.0001-0.0004 against 0.009-0.015 for E2's head).
   - E5 still reproduces E2's behaviour, including the higher benefit contacts (12 across seeds vs E2's 7 and FULL's 2).
   - Harm contacts rise in step with benefit contacts (E5 36 and E2 25, vs FULL 12). This is the same "more movement, more contacts of every kind" signature ADDENDUM 3 saw on seed 43.
3. **The evaluators do reach E3's choice (D2), but only under the depth limit.**
   - With R2 active, the trained harm term's cross-candidate spread (0.015-0.045) is 2-11x the residue term's (0.004-0.083). Removing the evaluator terms from J changes E3's pick on 20-93% of probe states.
   - Without R5/R2 (arm E3, full horizon), the evaluator terms change the pick on 0-3% of states, and behaviour matches NATIVE in all 3 seeds. So evaluation does not work without R5/R2: the 30-step aggregation and residue swamp it, as ADDENDUM 3 predicted.
4. **The upstream edge is DATA COVERAGE for benefit. Prediction is a second loss, in series.**
   - **Coverage.** The agent's own policy consumed a resource 0, 4 and 10 times in 1,500 steps (s43 / s42 / s44). The env's benefit shaping never fires in this regime (item P4 below). With a random-action run added, the training split holds 37-52 benefit positives, so the native warmup gate (50) stays SHUT on 2 of 3 seeds. In default use, E3 never consumes a trained benefit head.
   - **Prediction.** Where benefit is evaluable at all, the loss continues downstream. The trained benefit head ranks the TRUE next state of each action with Spearman 0.34 on s44 (27 states with a benefit-yielding action), but on E2's PREDICTED next state its Spearman is 0.00, with pick rate 0.11 against a true-state rate of 0.30.
   - **Harm contrast.** The harm evaluator survives prediction on 2 of 2 informative seeds: 0.55-0.65 on s44 and 0.26-0.38 on s42. That is because hazard proximity is a slowly varying property of the state, whereas benefit (entering one resource cell) is a one-action, one-step event. E2's action-conditional prediction does not carry it: the predicted cross-action spread of z1 is 0.009-0.011 against a true spread of 0.017-0.024. This is ADDENDUM 1-2's action-blindness, now shown to matter for benefit specifically.
5. **The failure signature constrains what comes next.** A learned consequence value is necessary (E3's J has no other benefit channel), but it is not sufficient, for three reasons in series:
   - (i) a rare-event data-coverage floor under the agent's own policy;
   - (ii) E2 predictions that do not separate the one action that reaches the resource;
   - (iii) a J in which any added term with a spread of about 0.01 overrides the residue-based harm avoidance that FULL relies on. E4 on seed 42 shows this: a PERMUTED benefit head alone took harm from 8.5 to 52.8, while E6, with the same permuted harm head and a flat benefit head, stayed near FULL at 5.2.

## Premises re-measured (and corrected)

- **P1. The canaries hold.** E0 NATIVE and E1 FULL reproduce ADDENDUM 3's `PART_s{42,43,44}.json` NATIVE and FULL arms bit-for-bit on all 3 seeds: same reward, harm and benefit counts, and executed-action counts. A second full run of seed 42 reproduces E0-E4 bit-for-bit (`EVAL_s42_run1.json` vs `EVAL_s42.json`).
- **P2. Corrected: ree_core has a benefit loss.** `REEAgent.compute_benefit_eval_loss` (`agent.py:11701`) is an MSE of `benefit_eval(z_world)` on `benefit_exposure`, which is body_state[11], the resource-proximity field in the agent's own observation. ree_core never calls it; about 17 landed drivers do (for example `v3_exq_074c_...py:258-265`). The brief's premise that no landed recipe might exist is wrong.
  - Arms E5/E6 use this recipe.
  - It failed to learn here. Held-out correlation with exposure was 0.16 / -0.03 / -0.09, and the target variance was only about 1e-4, so exposure is almost always near 0 at this density. The resulting term is flat: cross-candidate std 0.0001-0.0004.
- **P3. The harm-head premise holds, and the benefit channel is gated.**
  - "No loss in ree_core trains harm_eval_head" holds: there is no `harm_eval_head.parameters()` reference in `ree_core/`.
  - The benefit channel is off by default (`benefit_eval_enabled=False`, `config.py:1327`).
  - When enabled, it is gated on `_benefit_samples_seen >= 50` (`e3_selector.py:695`; gate at `:1737-1739`). That counter is incremented only by `record_benefit_sample` (`:1209-1216`), which nothing in ree_core calls.
- **P4. Benefit shaping is structurally absent.**
  - `benefit_approach` occurred 0 times in 9,000 labelled steps, because `hazard_approach` wins every tie when both proximity fields are active (`causal_grid_world.py:2736`; the module docstring at `:47-53` calls benefit_approach "structurally unreachable" at default multi-source configs unless `proximity_approach_magnitude_tiebreak=True`).
  - So every positive reward here is a resource CONSUMPTION.
  - "Harm events" in ADDENDUM 3's outcome table (and here) are mostly hazard-PROXIMITY steps. For example, seed 42's native run had 726 `hazard_approach` steps against 317 contacts. This document reports contacts separately.

## Evaluators (the agent's own experience only)

- **Labels** come from the env reward the agent receives: reward < 0 is harm, reward > 0 is benefit. No env internals are used.
- **Label state** is the encoded ARRIVAL state z_{t+1}, because that is what E3 scores under the depth-2 limit (`world_states[1]`). This deviates from V3-EXQ-1061, which labels the pre-step theta_z (`v3_exq_1061_...py:520-528`).
- **Data**, pooled with an 80/20 train/held-out split:
  - a native waking run of 1,500 steps (head A, E3 selecting);
  - a uniform-random-action run of 1,500 steps, the kind of data the COV head is trained on.
  - Both runs go through the agent's own SD-070 encoder, in fresh envs with seeds s+21 and s+23.
- **Harm head:** V3-EXQ-1061's BCE recipe (`v3_exq_1061_...py:557-575`): class-balanced k = min(16, npos, nneg), Adam 1e-3, clip 1.0, at least 8 per class. Run offline for 1,500 updates.
- **Benefit head (E2/E4):** the same recipe on benefit labels.
- **Benefit head (E5/E6):** the native MSE-on-exposure recipe, batch 32, 1,500 updates.
- **Shuffled controls (E4/E6):** the same z's, with labels permuted across training timesteps, so the marginals are the same.
- **Weights:** `lambda_ethical` 1.0, `benefit_weight` 1.0, `rho_residue` 0.5 (defaults).
- **Benefit gate:** forced to 50 for E2-E4 where the positive count fell short. For E5/E6 it was set to the number of exposure>0 samples (396-848), so it was natively open there.

| seed | own policy: harm / benefit labelled (per 1,500) | random run: harm / benefit | harm head held-out AUC | benefit head held-out AUC (held-out n+) | benefit positives in train (native gate 50) |
|---|---|---|---|---|---|
| 42 | 1043 / **4** | 1259 / 37 | 0.82 | 0.83 (4) | 37 -- **shut** |
| 43 | 55 / **0** | 1254 / 50 | 0.93 | 0.81 (9) | 41 -- **shut** |
| 44 | 266 / **10** | 1246 / 50 | 0.86 | 0.70 (8) | 52 -- open |

## Closed loop (600 steps; fresh agent per arm from the same seed; `evaluation_edge_probe.py --seed s`)

Cells read: reward/100 steps / harm events/100 (harm contacts) / benefit events/100 (benefit contacts) / episodes ended / action entropy / choice quality vs env-Q (chance 0.20).

| arm | seed 42 | seed 43 | seed 44 | mean reward / harm / benefit (total harm contacts, benefit contacts) |
|---|---|---|---|---|
| E0 NATIVE | -8.76 / 68.5 (107) / 0.67 (4) / 45 / 0.70 / 0.24 | -0.17 / 1.8 (1) / 0.00 (0) / 3 / 0.03 / 0.03 | -1.30 / 19.0 (12) / 0.67 (4) / 7 / 1.01 / 0.17 | -3.41 / 29.8 / 0.44 (120, 8) |
| E1 FULL (R5b+COV+R2) | -0.78 / 8.5 (8) / 0.00 (0) / 5 / 0.72 / 0.20 | -0.46 / 7.3 (3) / 0.17 (1) / 3 / 0.72 / 0.03 | -0.14 / 3.0 (1) / 0.17 (1) / 3 / 1.13 / 0.34 | **-0.46 / 6.3 / 0.11 (12, 2)** |
| **E2 FULL+EVAL** (contact BCE) | -1.62 / 17.8 (17) / 0.50 (3) / 9 / 1.06 / 0.18 | -0.17 / 2.2 (1) / 0.00 (0) / 3 / 0.05 / 0.15 | -0.95 / 18.7 (7) / 0.67 (4) / 6 / 1.14 / 0.27 | -0.91 / 12.9 / 0.39 (25, 7) |
| E3 EVAL-only (NATIVE+evaluators) | -8.72 / 67.2 (106) / 0.67 (4) / 45 / 0.72 / 0.24 | -0.17 / 1.8 (1) / 0.00 (0) / 3 / 0.02 / 0.05 | -1.38 / 22.2 (10) / 0.50 (3) / 8 / 1.01 / 0.17 | -3.42 / 30.4 / 0.39 (117, 7) |
| E4 FULL+SHUF (E2 labels permuted) | -6.53 / 52.8 (75) / 0.50 (3) / 33 / 0.77 / 0.24 | -0.06 / 3.0 (1) / 0.33 (2) / 3 / 0.21 / 0.03 | -0.22 / 2.3 (2) / 0.17 (1) / 3 / 0.69 / 0.07 | -2.27 / 19.4 / 0.33 (78, 6) |
| E5 FULL+EVAL, native benefit recipe | -2.03 / 18.3 (25) / 0.67 (4) / 11 / 0.74 / 0.20 | -0.17 / 2.0 (1) / 0.00 (0) / 3 / 0.03 / 0.15 | -1.02 / 20.8 (10) / 1.33 (8) / 6 / 1.13 / 0.29 | -1.07 / 13.7 / 0.67 (36, 12) |
| E6 FULL+SHUF, native benefit recipe | -0.22 / 5.2 (2) / 0.17 (1) / 3 / 0.57 / 0.20 | -0.61 / 5.8 (7) / 0.17 (1) / 5 / 0.27 / 0.03 | -0.32 / 9.5 (2) / 0.50 (3) / 3 / 0.88 / 0.29 | -0.38 / 6.8 / 0.28 (11, 5) |

**Scorer reach** was checked with call counters on `compute_harm_cost_fallback` and `compute_benefit_score`. Both fire on every E3 scoring pass in E2-E6 (2,528-13,728 calls per arm), and the benefit gate is open in those arms.

**J term spread at the probe states** (mean cross-candidate std on the 5-class scaffold at the arm's depth; `terms` in the JSON), with the flip rate when the evaluator terms are dropped from J:

| seed | residue (all FULL arms) | E2 harm / benefit, flip | E4 harm / benefit, flip | E5 harm / benefit, flip | E3 (full horizon) residue / harm / benefit, flip |
|---|---|---|---|---|---|
| 42 | 0.083 | 0.019 / 0.015, 0.20 | 0.003 / 0.016, 0.27 | 0.019 / 0.0004, 0.31 | 153 / 5.1 / 2.3, 0.00 |
| 43 | 0.004 | 0.045 / 0.014, 0.93 | 0.004 / 0.004, 0.03 | 0.045 / 0.0001, 1.00 | 1.9 / 2.8 / 2.0, 0.03 |
| 44 | 0.008 | 0.015 / 0.009, 0.39 | 0.001 / 0.008, 0.88 | 0.015 / 0.0001, 0.54 | 5.3 / 0.25 / 0.26, 0.00 |

## Readings against the brief's three questions

1. **Is evaluation the next broken edge? E2 > E1 and E2 > E4 on benefit, with harm not worse?**
   - E2 > E1 on benefit in 2 of 3 seeds, but harm is worse in both of those.
   - E2 > E4 on benefit in 1 of 3 seeds (s42 tie, s43 E4 higher, s44 E2 higher).
   - **Directed success in 0 of 3 seeds.** Choice quality against env-Q does not improve: E2 vs E1 is 0.18 vs 0.20, 0.15 vs 0.03 and 0.27 vs 0.34, all near or below chance.
   - E2 does beat E4 on overall reward on s42 (-1.62 vs -6.53). But E6, with the same shuffled harm head, matches FULL. So what E4 shows is fragility to an added benefit-head term, not that the trained heads carry value.
2. **Is it sufficient without R5/R2 (E3 vs E2)?** No. E3 matches NATIVE on all 3 seeds (reward -8.72 / -0.17 / -1.38 vs -8.76 / -0.17 / -1.30). At full horizon, dropping the evaluator terms changes the pick on 0-3% of states. The deep steps (residue, plus two heads reading off-manifold extrapolations) swamp them. R2 is a precondition for any evaluator to act.
3. **What does the failure signature constrain?** See the verdict, items 4-5, and the split below.

## Split: is the evaluator failing, or the prediction it reads? (D2; `eval_split_probe.py --seed s`)

- Probe states: every 3rd step of a 600-step native waking run (201-219 states per seed, all distinct).
- At each state the env is cloned, and each of the 5 action classes is stepped for its TRUE immediate reward and TRUE encoded arrival state (encode_next, validated in ADDENDUM 2).
- Each head is then compared on the true arrival state and on E2's PREDICTED one: the COV head, `world_forward(z0, onehot c)`, which is what E3 reads at depth 2.
- Metrics: Spearman against true immediate harm or benefit across classes, using average ranks for ties, and the rate at which the head's best class is in the true-best set.

| seed | harm head, trained: rho true / pred (pick true / pred) | untrained | shuffled | benefit head, trained: rho true / pred (pick true / pred), n states with benefit available | predicted vs true cross-action z1 spread |
|---|---|---|---|---|---|
| 42 | 0.38 / 0.26 (0.44 / 0.43) | -0.05 / -0.10 (0.16 / 0.23) | 0.19 / 0.14 | -0.26 / 0.14 (0.05 / 0.22), n = 41 | 0.011 vs 0.024 |
| 44 | 0.55 / 0.65 (0.53 / 0.75) | 0.13 / 0.03 (0.27 / 0.52) | -0.17 / -0.13 | 0.34 / 0.00 (0.30 / 0.11), n = 27 | 0.009 vs 0.017 |
| 43 | (degenerate: agent near-stationary, 97% one class) | | | n = 3 | 0.009 vs 0.017 |

- **The harm head works through E2's prediction.** Its ranking of immediate harm survives prediction (s42 0.26, s44 0.65; untrained -0.10 and 0.03). Hazard proximity is a slowly varying property of the state. Even so, in the closed loop it produced MORE harm than FULL's residue on s42 and s44. Its training label is about 77% "near a hazard", so it penalises proximity broadly. It overrides the residue term (flip 20-93%), and residue carries the contact-specific memory that made FULL work. That mechanism is inferred, not isolated.
- **The benefit head fails at both stages.** On s42 it is anti-aligned even on TRUE states (rho -0.26, pick 0.05). That head was trained on 37 positives, and its held-out AUC of 0.83 rested on 4. On s44 it ranks true states (0.34) but not predicted ones (0.00; pick 0.11 vs 0.30). E2's predicted cross-action spread is about half the true one, and the one action that enters the resource cell is not separated.

## Named options for the orchestrator (none built; `complex (probe-gated)` unless stated)

- **(O1) Benefit data coverage first.** Candidates:
  - an exploration or random-action fraction feeding the evaluator buffer;
  - turning on the env's own benefit gradient (`proximity_approach_magnitude_tiebreak=True`, an env flag rather than a substrate change) so that approach steps become labelled experience;
  - a denser benefit label (exposure), which failed here as a regression target at this density.

  The discriminating test is to re-run E2 with the tie-break on. If benefit labels go from about 40 to hundreds and E2 then shows directed benefit, coverage was the binding edge.
- **(O2) E2 must separate actions for one-step consequence.** This is ADDENDUM 1-2's action-blindness, now shown to matter for benefit specifically (harm survives because it is state-level). There is no new repair beyond COV and the encoder ceiling already named.
- **(O3) Commensurability in J under R2.** At depth 2 the residue spread is 0.004-0.08, so any evaluator term of about 0.01 dominates it. A native evaluator would need calibrated channel weighting (the `use_e3_channel_commensurability` machinery exists, `e3_selector.py:1714`) rather than raw weights of 1.0. This is `complicated (buildable)` as a probe arm and was not run.
- **(O4) A native waking trainer for harm_eval / benefit_eval.** There still is none in ree_core. Building one is premature until O1 is resolved: the harm head trained here made harm worse, and the benefit head is data-starved.

**Single next action:** run the O1 discriminator, E2 with `proximity_approach_magnitude_tiebreak=True`, 3 seeds, in the same harness. It is about 30 minutes of Mac time and answers whether coverage or prediction is the binding edge for benefit.

## Done / not done

- **DONE:**
  - canaries on 3 seeds (bit-identical to ADDENDUM 3), plus a determinism re-run of seed 42;
  - arms E0-E4 as briefed, plus E5/E6 (the native benefit recipe and its shuffle) on seeds 42/43/44;
  - label counts, held-out AUCs and gate status;
  - term spread and drop-evaluator flip rates;
  - the true-vs-predicted split on 3 seeds.
- **NOT DONE:**
  - the O1 discriminator;
  - a commensurability arm;
  - pre-step (1061-exact) label placement, which is a deviation and stated as one;
  - more than 600 closed-loop steps or more than 3 seeds;
  - online (in-loop) evaluator training. Offline training on 3,000 steps of own experience stands in for a driver's in-loop cadence.
- **Other limits:**
  - The forced benefit gate on 2 of 3 seeds is non-native, and is labelled wherever it matters.
  - Benefit event counts are small (0-8 contacts per arm per seed), so the benefit columns are noisy.
  - "Harm events" include hazard-proximity steps; contacts are reported separately.
  - Heads were trained on argmax one-hot actions, while runtime actions are continuous (inherited from ADDENDUM 2-3).
- **Run log** (from `.scratch/breakthrough-20260924/evaluation/`, worktree @ `44c55300ca`): `run_eval.sh 43 44 42`, `run_split.sh 43 44 42`.

## ADDENDUM 1 (2026-09-24T21:25Z, session `bt0924-evaluation-b`): single factor `proximity_approach_magnitude_tiebreak=True`

- **Commissioned by the orchestrator** as the O1 discriminator.
- **Code and harness:** ree-v3 `origin/main` @ `44c55300ca` (re-fetched; unchanged), with the same harness and budget as above.
- **The one change:** `evaluation_edge_probe.py --tiebreak 1 --force-gate 0 --arms E1_FULL,E2_FULL_EVAL,E4_FULL_SHUF` (via `run_tb.sh 43 44 42`).
  - The flag is applied by wrapping the probe's only env constructor (`rollout_fidelity_probe.py:93`), so it covers the encoder P0, the replay, the label runs, the probe states and every arm. The probe asserts that it is set.
  - The benefit gate is NATIVE: `_benefit_samples_seen` = the number of benefit positives in the training split. Nothing is forced.
- **Output:** results in `probes/evaluation/results/TB_s{42,43,44}.json`, tabulated by `summarize_tb.py`.
- **Wall time:** 3-6 min per seed.

**What the flag changes (confirmed live).**
- The flag is read at `causal_grid_world.py:2733`.
- **When both proximity fields are above threshold,** the step is classified by whichever raw field is larger (`hazard_wins = h_field_val >= r_field_val`), not always as hazard.
- **A benefit-won step** pays `+0.03 * resource_field` (`proximity_benefit_scale`, `:340`) and does not drain health. Before this change, the same step paid `-0.05 * hazard_field` and drained health.
- **Unchanged:** observations, dynamics and the contact rewards. The env's reward stream is therefore itself different from the main record, so T1 is the baseline here, not the earlier FULL arm.

Arm mapping: **T1** = FULL (R5b+COV+R2, untrained evaluators); **T2** = FULL + trained evaluators (the E2 recipe); **T3** = FULL + the same evaluators trained on label-permuted data (the E4 recipe). Each arm runs 600 steps on a fresh agent from the same seed.

### Coverage: labelled benefit positives and the native gate

| seed | own-policy run (1,500 steps): benefit reward steps (consumptions + benefit-approach) | random run (1,500): benefit steps (consumptions) | benefit positives in the training split | **native gate (50) open without forcing?** | benefit head held-out AUC | harm head AUC |
|---|---|---|---|---|---|---|
| 42 | 573 (10 + 563) | 873 (36) | 1136 | **yes** | 0.70 | 0.63 |
| 43 | 82 (3 + 79) | 831 (46) | 737 | **yes** | 0.90 | 0.81 |
| 44 | 158 (16 + 142) | 797 (41) | 766 | **yes** | 0.81 | 0.71 |

- **Coverage rose about 20-30x.** The main record had 37-52 positives, and the gate was shut on 2 of 3 seeds. Here E3's benefit channel switches on natively on all 3 seeds.
- **The new positives are almost all benefit-APPROACH (proximity) steps.** Resource consumption is still rare: 3-16 per 1,500 own-policy steps.

### Closed loop, counts per 600 steps (harm contacts / hazard-proximity steps split out, as corrected in the main record)

| seed | arm | env reward / 100 | harm contacts | hazard-proximity steps | resource consumptions | benefit-approach steps | episodes ended | choice quality vs env-Q (chance 0.20) |
|---|---|---|---|---|---|---|---|---|
| 42 | T1 FULL | -0.43 | 8 | 4 | 0 | 36 | 4 | 0.25 |
| 42 | **T2 FULL+EVAL** | **-2.07** | **39** | **25** | 7 | **98** | 14 | 0.27 |
| 42 | T3 FULL+SHUF | -0.03 | 2 | 1 | 1 | 18 | 3 | 0.25 |
| 43 | T1 FULL | -0.10 | 5 | 8 | 4 | 19 | 4 | 0.05 |
| 43 | **T2 FULL+EVAL** | -0.10 | 6 | 8 | 1 | **56** | 3 | 0.12 |
| 43 | T3 FULL+SHUF | -0.02 | 1 | 0 | 0 | 12 | 3 | 0.10 |
| 44 | T1 FULL | -0.38 | 6 | 0 | 0 | 19 | 3 | 0.29 |
| 44 | **T2 FULL+EVAL** | **-1.26** | **22** | **31** | 5 | **76** | 11 | 0.17 |
| 44 | T3 FULL+SHUF | +0.02 | 3 | 5 | 3 | 14 | 3 | 0.24 |

J term spread at the probe states (mean cross-candidate std, depth 2):

| seed | residue | T2 trained harm / benefit | T3 shuffled harm / benefit |
|---|---|---|---|
| 42 | 0.034 | 0.009 / 0.009 | 0.002 / 0.002 |
| 43 | 0.0008 | 0.055 / 0.034 | 0.001 / 0.001 |
| 44 | 0.004 | 0.014 / 0.019 | 0.002 / 0.001 |

### Read-out against the pre-registered criterion

The criterion: benefit up AND harm not worse vs T1, AND T2 > T3, on at least 2 of 3 seeds.

- **Benefit up vs T1: 3 of 3 seeds.** Benefit-approach steps go 36 -> 98, 19 -> 56 and 19 -> 76 (about 2.7-4x). Consumptions go 0 -> 7 (s42), 4 -> 1 (s43) and 0 -> 5 (s44), so consumption rises on 2 of 3 seeds.
- **T2 > T3 on benefit: 3 of 3 seeds** (98 vs 18, 56 vs 12, 76 vs 14 approach steps). In the main record this held on only 1 of 3 seeds. With coverage, the trained benefit head now carries real, label-specific, directed signal into behaviour.
- **Harm not worse vs T1: 1 of 3 seeds** (s43: contacts 6 vs 5, proximity steps 8 vs 8, reward equal). On s42 harm contacts go 8 -> 39 and proximity steps 4 -> 25; on s44, contacts 6 -> 22 and proximity steps 0 -> 31. Env reward is worse on both (-0.43 -> -2.07; -0.38 -> -1.26), and early terminations rise (4 -> 14; 3 -> 11).
- **Directed success: 1 of 3 seeds (s43 only). The criterion is NOT met.**
- **Choice quality vs env-Q does not move consistently.** T2 vs T1 is 0.27 vs 0.25, 0.12 vs 0.05 and 0.17 vs 0.29.

**Which pre-registered outcome this is: neither cleanly. The evidence points to the third constraint already named.**

1. **Coverage WAS binding for the benefit head.** With labels available, the gate opens natively, the head learns (AUC 0.70-0.90), and it moves behaviour toward resources, beating the shuffled control on 3 of 3 seeds. That is the part of the main record's failure that was coverage.
2. **E2 prediction is NOT the binding edge for approach-benefit.** T2's benefit effect is directed and survives E2's prediction. That fits the main record's split: state-level proximity signals, like hazard proximity, survive prediction. Consumption is a one-step, one-action event, and it rose on only 2 of 3 seeds with counts of 1-7. So action-blindness for consumption specifically is not excluded, and not tested further here (no added factors).
3. **What now fails is harm, and the signature is the fragility / commensurability finding.**
   - In T2 the evaluator terms have spreads of 0.009-0.055. On 2 of 3 seeds that matches or exceeds the residue term's spread (0.0008-0.034), which is what gives FULL its harm avoidance.
   - The agent now pursues resources through hazard regions. Resources and hazards are co-located, which is why the tie-break is needed at all. Nothing in J is weighted to trade benefit against harm contact.
   - T3's shuffled heads have near-flat spreads (0.001-0.002) and leave FULL's harm avoidance intact, even improving it slightly. So the harm cost comes from a strong, informative added term overriding residue, not from "any trained head".
   - In the main record, a shuffled benefit head with spread 0.016 did the same damage (s42 harm 8.5 -> 52.8 events per 100). Across both runs, whichever added term has spread of about 0.01 or more takes over E3's pick under R2.
   - **This affects ANY added score term under R2,** including a future native evaluator, goal or curiosity term: its weight relative to residue decides whether harm avoidance survives.

**The constraint (stopping here, no further factors).** With benefit coverage supplied, the evaluation edge becomes functional: native gate, directed approach, beats the control. Behaviour is then limited by **score commensurability in E3 under R2**. The raw-weight sum `lambda_ethical * M + rho_residue * Phi - benefit_weight * B` (all at defaults, `e3_selector.py:1710-1751`) has no calibrated trade-off between the new value terms and the residue-borne harm memory. So the benefit gain is bought with 3-5x more harm contacts on 2 of 3 seeds.

The next discriminator, for the orchestrator to decide and not run here: T2 with `use_e3_channel_commensurability` (`e3_selector.py:1714`), or with evaluator weights scaled so their spread matches residue's. The criterion stays the same.

**Limits.**
- Benefit labels are now about 95% proximity steps, so "benefit" in this addendum mostly means approach, not consumption. Consumption counts are 0-7 per arm.
- 3 seeds; 600 steps per arm; offline evaluator training on 3,000 own-experience steps.
- The flag changes the env's reward stream, so T1 is not the main record's FULL.
- Harm head AUC is lower here (0.63-0.81 vs 0.82-0.93) because hazard-approach labels are now split with benefit-approach.

## ADDENDUM 2 (2026-09-24T21:40Z, session `bt0924-evaluation-c`): single factor `use_e3_channel_commensurability=True`

- **Commissioned by the orchestrator** as the next single factor. Native machinery only; no hand-set weights.
- **Code:** ree-v3 `origin/main` @ `44c55300ca` (re-fetched; unchanged).
- **Harness:** the same as ADDENDUM 1, with the tie-break on throughout and the benefit gate native.
- **Run:** `evaluation_edge_probe.py --tiebreak 1 --comm 1 --force-gate 0 --arms E1_FULL,E2_FULL_EVAL,E4_FULL_SHUF` via `run_comm.sh 43 44 42`, summarised by `summarize_comm.py`.
- **Results:** `probes/evaluation/results/COMM_s{42,43,44}.json`.
- **Canary:** on all 3 seeds the preamble (encoder, heads, evaluators, label counts) is identical to ADDENDUM 1's TB runs, so the flag is the only difference. C1 = T1 + flag, C2 = T2 + flag, C3 = T3 + flag.

### What the operator actually does on origin/main (read before running)

- **What it normalises.** Five additive channels are normalised: `f_weighted`, `harm_weighted`, `residue_weighted`, `benefit_weighted` and `goal_weighted` (`_COMMENSURABILITY_CHANNELS`, `e3_selector.py:149-155`). **Residue is one of them.** Each channel's per-candidate WEIGHTED term (for example `rho_residue * Phi`) is divided by that channel's own running scale before the sum (`:1728-1730`, benefit `:1750`, goal `:1769`).
- **Which statistic.** The scale is an EMA (alpha 0.05, `config.py:1090`) of the channel's CROSS-CANDIDATE standard deviation of the raw weighted term within one `select()` tick (`_update_channel_scale_estimates`, `:1584-1631`).
- **Running, not per-tick.** The estimate is folded in after each tick's scoring, so every tick is scored against earlier ticks' estimates.
- **Warmup and floors.** Channels keep unit scale for the first 20 ticks (`config.py:1097`; `_commensurability_scale`, `:1567-1582`). A channel whose scale is at or below the 1e-12 absolute floor (`config.py:1106`) also keeps unit scale.
- **Producer: self-contained, no external supplier needed.**
  - `score_trajectory` captures the raw terms (`:1714-1726`).
  - `E3.select` collects them per candidate from its main candidate loop (`:3280-3314`) and folds them in once per tick (`:3320`).
  - The SD-081 habit loop is deliberately excluded from the estimate.
  - Not wired through `from_dims`; it is set per arm on `agent.e3.config`, as its docstring (`config.py:1080-1083`) says.
- **Live in every arm.** 72-111 estimate updates per 600-step arm; `engaged=True` in all 9 arms.
- **Prior status of the operator** (`docs/architecture/sd_e3_channel_commensurability.md`): validated only at the ELIGIBILITY stage (V3-EXQ-1012c PASS, 3 of 5 channels). Its original readiness target, per-channel variance shares, was ruled an arithmetic identity of the operator (GFLAG-0234): Var(term/s) is about 1 per channel by construction. This probe's closed loop is its first behavioural test in this regime.

### Closed loop (600 steps; with the flag vs the ADDENDUM 1 run without it)

Cells read: harm contacts / hazard-proximity steps / resource consumptions / benefit-approach steps / env reward per 100 steps.

| seed | C1 = T1 + flag | C2 = T2 + flag | C3 = T3 + flag | T1 (no flag) | T2 (no flag) | T3 (no flag) |
|---|---|---|---|---|---|---|
| 42 | 9 / 6 / 0 / 31 / -0.54 | **15** / 7 / 3 / **67** / -0.63 | 2 / 2 / 1 / 19 / -0.03 | 8 / 4 / 0 / 36 / -0.43 | 39 / 25 / 7 / 98 / -2.07 | 2 / 1 / 1 / 18 / -0.03 |
| 43 | 5 / 5 / 3 / 25 / -0.12 | **3** / 2 / 0 / **45** / +0.04 | 0 / 2 / 1 / 15 / +0.12 | 5 / 8 / 4 / 19 / -0.10 | 6 / 8 / 1 / 56 / -0.10 | 1 / 0 / 0 / 12 / -0.02 |
| 44 | 11 / 27 / 3 / 41 / -0.65 | **11** / 17 / 2 / **44** / -0.58 | 13 / 6 / 3 / 57 / -0.59 | 6 / 0 / 0 / 19 / -0.38 | 22 / 31 / 5 / 76 / -1.26 | 3 / 5 / 3 / 14 / +0.02 |

Choice quality against env-Q (chance 0.20), scored at the arm's own running scales with the flag on vs off, C1 / C2 / C3:

| seed | with the flag | without |
|---|---|---|
| 42 | 0.25 / 0.25 / 0.25 | 0.25 / 0.27 / 0.25 |
| 43 | 0.05 / 0.10 / 0.07 | 0.05 / 0.12 / 0.10 |
| 44 | 0.27 / 0.27 / 0.32 | 0.29 / 0.17 / 0.24 |

### Criterion (pre-registered): C2 benefit up vs C1, AND C2 harm contacts not worse than C1, AND C2 > C3 on benefit, on at least 2 of 3 seeds

"Benefit" below = consumptions + approach steps.

| seed | benefit C2 vs C1 | harm contacts C2 vs C1 | benefit C2 vs C3 | pass? |
|---|---|---|---|---|
| 42 | 70 vs 31, up | **15 vs 9, worse** | 70 vs 20, yes | no |
| 43 | 45 vs 28, up | 3 vs 5, not worse | 45 vs 16, yes | **yes** |
| 44 | 46 vs 44 (+2, noise) | 11 vs 11, not worse | **46 vs 60, no** | no |

**Directed success on 1 of 3 seeds (s43). The criterion is NOT met.**

### Term spreads with and without the flag (the mechanism check)

**Closed loop.** The arm's own running estimate is the RAW mean cross-candidate spread per channel over its 72-111 ticks (C2), the direct measure of which term dominates without normalisation:

| seed | F | harm (trained) | residue | benefit (trained) |
|---|---|---|---|---|
| 42 | 4.5e-4 | 6.6e-3 | **3.2e-4** | 3.7e-3 |
| 43 | 9.5e-4 | 1.6e-2 | **4.1e-4** | 1.1e-2 |
| 44 | 2.8e-3 | 3.6e-2 | **9.3e-4** | 7.3e-2 |

- **Without the flag, the evaluator terms out-spread residue about 10-80x in the closed loop,** which is the domination ADDENDUM 1 blamed for the harm cost.
- **With the flag, each channel is divided by exactly these numbers.** So their average normalised spread is about 1 each by construction; that is the identity noted in the design doc. The mechanism claim "stops one term dominating" therefore holds ON AVERAGE by arithmetic. What it does to behaviour is the test.
- In C1 the UNTRAINED harm head's raw spread (4e-5 to 3e-4) is scaled up in the same way, because it clears the 1e-12 floor.

**Probe states** (scaffold, 5 one-class candidates, depth 2), mean cross-candidate std; flag-off raw -> flag-on normalised (at the arm's running scales), then the drop-evaluator flip rate off -> on:

| seed | arm | F | harm | residue | benefit | drop-evaluator flip |
|---|---|---|---|---|---|---|
| 42 | C2 | 0.0004 -> 0.97 | 0.009 -> 1.3 | 0.034 -> 108 | 0.009 -> 2.5 | 0.17 -> 0.00 |
| 43 | C2 | 0.0003 -> 0.28 | 0.055 -> 3.5 | 0.0008 -> 1.9 | 0.034 -> 3.0 | 0.05 -> 0.05 |
| 44 | C2 | 0.0001 -> 0.05 | 0.014 -> 0.41 | 0.004 -> 4.6 | 0.019 -> 0.27 | 0.54 -> 0.05 |
| 42 / 43 / 44 | C1 (untrained harm) | | 0.0001 -> 1.7 / 0.38 / 0.29 | 0.034 -> 97 / 3.1 / 2.3 | | |

**Caveat on the probe-state rows.** They mix the arm's running scales with the MASTER agent's residue field, which accumulated over all of the master's runs. This is inherited from ADDENDUM 3's choice-quality harness. So residue's normalised magnitude there is inflated, especially on s42. The residue-dominance and flip-rate readings are indicative only; the closed-loop rows above are clean.

### Failure signature (stopping here, as instructed)

1. **The operator moves harm the right way, but only part of the way, and it takes the benefit gain with it.**
   - Compared with T2 (no flag), C2's harm contacts fall 39 -> 15, 6 -> 3 and 22 -> 11, and reward improves on all 3 seeds (-2.07 -> -0.63, -0.10 -> +0.04, -1.26 -> -0.58).
   - But benefit-approach falls 98 -> 67, 56 -> 45 and 76 -> 44.
   - The evaluator's margin over C1 shrinks (+62 -> +39, +34 -> +17, +57 -> +2).
   - On s44, trained and shuffled evaluators become indistinguishable, and C3 even out-benefits C2 (60 vs 46).
   - On s42, harm is still worse than C1 (15 vs 9 contacts).
2. **Variance standardisation is not value calibration.** The operator equalises channels by their cross-candidate SPREAD, not by what their differences are worth.
   - **An untrained channel gets full authority.** The untrained harm head (nothing in ree_core trains it) has raw spread 4e-5 to 3e-4. That clears the 1e-12 floor, so the operator scales it up to parity with residue.
   - **C1 on s44 shows the cost.** Compared with T1 (no flag), harm contacts go 6 -> 11, hazard-proximity steps 0 -> 27, and reward -0.38 -> -0.65. The only thing that changed is that the operator gave noise a vote.
   - **A trained but label-shuffled head gets parity the same way,** which is how C3 catches up with C2 on s44.
3. **Residue's authority becomes bursty.** Its running scale is the mean of a spread that is near 0 on most ticks and large near harm memory. Dividing by that mean makes residue very strong exactly where it is active. This is consistent with the harm reduction versus T2, but it also flattens the evaluator's influence at those states (probe-state flip 0.17 -> 0.00 on s42 and 0.54 -> 0.05 on s44, subject to the caveat above).
4. **What this constrains.** With benefit data supplied, the problem is not that one term dominates by units; the native operator fixes that, as arithmetic guarantees. The problem is that E3 has no signal for how much each channel's differences are WORTH:
   - a trained evaluator, an untrained one and a shuffled one all get equal weight once their spreads are equalised;
   - residue's contact memory and the evaluators' learned values are not traded against realised outcome.

   The native candidate for that is outcome-driven channel weighting: the ARC-108 learned channel gating, `use_learned_channel_gating` (`config.py:1444`), with per-channel `w_chan` updated by a three-factor RPE rule (`e3_selector.py:708`). That is for the orchestrator to decide, with its own producer-trace check first. It was not run here: no further factors.

**Limits.**
- 3 seeds; 600 steps per arm.
- Benefit is mostly approach steps (consumption 0-3 per arm).
- The probe-state spreads carry the master-residue confound described above.
- The s44 C2 benefit rise over C1 (+2) is within noise.
- The flag's running scales start fresh in each arm (fresh agent), so the first 20 E3 ticks of every arm are unnormalised.
