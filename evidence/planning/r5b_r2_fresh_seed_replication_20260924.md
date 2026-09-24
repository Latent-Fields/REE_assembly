# Fresh-seed replication of ADDENDUM 3's R5b + R2 closed-loop harm-avoidance result

- **STATUS: FINAL.** 2026-09-24T23:08:37Z.
- Session `bt0924-replication` (Worker I, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260924-r5b-r2-fresh-seed-replication`.
- Replicates: `e2_rollout_divergence_and_proposal_state_dependence_20260924.md` ADDENDUM 3 (session `bt0924-rollout-d`, Worker D), which found FULL (R5b + R2, COV present but shown unnecessary) beats NATIVE on env reward in 2 of 3 seeds (43, 42, 44), with R5 and R2 each necessary in 2 of those 3 seeds and COV not necessary.
- Code under test: ree-v3 `origin/main`, private detached worktree at `863d23d65a9093de2a7a02482e9d78f4bf6f5702`. **Confirmed no diff** on `ree_core/predictors/e3_selector.py`, `ree_core/hippocampal/{module,config}.py`, `ree_core/environment/causal_grid_world.py`, `experiments/_harness.py` between ADDENDUM 3's commit (`44c55300ca`) and this worktree's HEAD -- the repairs under test are byte-identical to ADDENDUM 3's.
- Probe: `.scratch/breakthrough-20260924/replication/partitioned_repair_probe_r2.py` -- **a copy of ADDENDUM 3's `probes/rollout/partitioned_repair_probe.py`, unchanged except the `ARMS` dict** (see "Deviation from ADDENDUM 3's script" below) and, for one post-hoc diagnostic run only, an additive instrumentation line (see "Post-hoc diagnostic"). Same `--wake 600`, `--probe-steps 200`, `--ncont 6`, `--clen 4` defaults; same Regime B env (`world_dim` 32, `CausalGridWorldV2`, SD-070-trained encoder, 20x50 P0 warmup, preservation 1000); tiebreak OFF (the harness's `build_B` never passes `proximity_approach_magnitude_tiebreak`, so it sits at `causal_grid_world.py`'s default `False`, same as ADDENDUM 3). Results: `probes/rollout/results/PART_s{47,48,49,50,51}.json` (landed alongside this record) and the pre-registered-original copies at `.scratch/breakthrough-20260924/replication/results_preregistered_original/` (not committed -- scratch only).
- Evidence domain reached: **D3** (closed-loop env reward under a real policy difference) on this one regime, one encoder budget, 600 steps. Does **not** show generalisation to: other regimes/env configs, other world_dim, longer horizons, a trained harm-eval or benefit-eval head, or robustness beyond 5 seeds.

## PRE-REGISTRATION (verbatim from the chip prompt, fixed before any run)

- Seeds: 47, 48, 49, 50, 51 (fresh; none of 42/43/44/45/46).
- Arms: NATIVE; FULL (R5b `use_action_class_scaffold_candidates` + R2 `_score_depth_limit=2`); FULL-minus-R5; FULL-minus-R2. (COV dropped -- shown unnecessary.)
- Primary DV: env reward per 100 steps; secondary: harm contacts per 100 steps (true contacts; report hazard-proximity steps separately, per Worker F's correction), early terminations, action entropy.
- Criterion R (replication): FULL reward > NATIVE reward on >= 4 of 5 seeds AND FULL harm contacts < NATIVE on >= 4 of 5 seeds.
- Criterion N (necessity): dropping R5 and dropping R2 each lose >= half of FULL's reward gain over NATIVE on >= 3 of 5 seeds.
- Undirected-noise flag: any seed where FULL raises action entropy but lowers reward vs NATIVE is reported as undirected noise (the seed-43 pattern), with its NATIVE entropy.
- No additional arms, no tuning, no re-running seeds.

## Deviation from ADDENDUM 3's script (disclosed, minimal)

ADDENDUM 3's `ARMS` dict was `{"FULL": (r5=1,cov=1,r2=1), "FULL-R5": (0,1,1), "FULL-COV": (1,0,1), "FULL-R2": (1,1,0), "NATIVE": (0,0,0)}`. This worker's pre-registration defines a different arm set (COV dropped throughout, per ADDENDUM 3's own finding that COV is not necessary), so the `ARMS` dict was edited to:

```python
ARMS = {"FULL": (1, 0, 1), "FULL-minus-R5": (0, 0, 1), "FULL-minus-R2": (1, 0, 0), "NATIVE": (0, 0, 0)}
```

Every arm here loads the native-replay-trained head (`cov=0`, ADDENDUM 2 arm A); the COV-trained head is still trained by the unmodified harness code and its `choice_quality` cells are still computed (dead weight, kept to minimise the diff), but no arm in `ARMS` uses it. No other line of the closed-loop mechanics, training budgets, env config, or probe-state logic was touched. This is the only change made before the pre-registered runs.

## Per-seed results (600 steps per arm, fresh agent per arm, no carry-over)

| seed | arm | reward/100 | harm events/100 | benefit events/100 | episodes ended | action entropy | executed-action majority share | proposal majority share (20 states) |
|---|---|---|---|---|---|---|---|---|
| 47 | FULL | -0.522 | 8.00 | 0.50 | 5 | 1.088 | 0.48 | 0.603 |
| 47 | FULL-minus-R5 | -0.204 | 2.67 | 0.17 | 3 | 0.117 | 0.98 | 0.684 |
| 47 | FULL-minus-R2 | -0.089 | 4.33 | 0.33 | 3 | 0.928 | 0.64 | 0.603 |
| 47 | NATIVE | -0.065 | 3.67 | 0.33 | 3 | 0.667 | 0.71 | 0.680 |
| 48 | FULL | -0.291 | 6.00 | 0.33 | 4 | 0.637 | 0.80 | 0.492 |
| 48 | FULL-minus-R5 | -0.201 | 2.67 | 0.00 | 3 | 0.249 | 0.93 | 0.545 |
| 48 | FULL-minus-R2 | -0.008 | 2.33 | 0.50 | 3 | 0.949 | 0.56 | 0.492 |
| 48 | NATIVE | -0.070 | 2.67 | 0.33 | 3 | 0.535 | 0.77 | 0.548 |
| 49 | FULL | -0.078 | 3.17 | 0.33 | 3 | 0.565 | 0.82 | 0.820 |
| 49 | FULL-minus-R5 | -0.208 | 3.17 | 0.00 | 3 | 0.467 | 0.83 | 0.930 |
| 49 | FULL-minus-R2 | -0.029 | 2.50 | 0.17 | 3 | 0.789 | 0.66 | 0.820 |
| 49 | NATIVE | -0.286 | 3.00 | 0.00 | 3 | 0.075 | 0.99 | 0.927 |
| 50 | FULL | -2.241 | 24.33 | 1.50 | 14 | 1.046 | 0.58 | 0.684 |
| 50 | FULL-minus-R5 | -7.570 | 63.17 | 0.67 | 39 | 1.091 | 0.53 | 0.778 |
| 50 | FULL-minus-R2 | -0.613 | 6.17 | 0.00 | 5 | 0.236 | 0.95 | 0.683 |
| 50 | NATIVE | -8.701 | 67.83 | 0.83 | 44 | 0.936 | 0.57 | 0.778 |
| 51 | FULL | +0.014 | 1.33 | 0.17 | 3 | 0.590 | 0.73 | 0.867 |
| 51 | FULL-minus-R5 | +0.016 | 1.33 | 0.17 | 3 | 0.688 | 0.55 | 0.969 |
| 51 | FULL-minus-R2 | -0.157 | 4.67 | 0.50 | 3 | 0.910 | 0.60 | 0.867 |
| 51 | NATIVE | +0.014 | 1.33 | 0.17 | 3 | 0.633 | 0.67 | 0.969 |
| mean | FULL | **-0.623** | 8.57 | 0.57 | | 0.785 | | |
| mean | FULL-minus-R5 | -1.634 | 14.60 | 0.20 | | 0.522 | | |
| mean | FULL-minus-R2 | **-0.179** | 4.00 | 0.30 | | 0.762 | | |
| mean | NATIVE | -1.822 | 15.70 | 0.33 | | 0.569 | | |

At 600 steps/arm and max 200 steps/episode, anything above 3 episodes ended is an early termination signal; seed 50 (all arms) and seed 47 FULL are the only cases materially above that floor.

## Criterion R (replication): FAIL

FULL reward > NATIVE reward on >= 4/5 seeds AND FULL harm events < NATIVE on >= 4/5 seeds.

| seed | FULL reward | NATIVE reward | reward win? | FULL harm/100 | NATIVE harm/100 | harm win? |
|---|---|---|---|---|---|---|
| 47 | -0.522 | -0.065 | NO | 8.00 | 3.67 | NO |
| 48 | -0.291 | -0.070 | NO | 6.00 | 2.67 | NO |
| 49 | -0.078 | -0.286 | YES | 3.17 | 3.00 | NO (barely) |
| 50 | -2.241 | -8.701 | YES | 24.33 | 67.83 | YES |
| 51 | +0.0142124 | +0.0142124 | YES (float-noise margin, ~5e-10; harm events tied 1.33=1.33) | 1.33 | 1.33 | NO (tied) |

**Reward wins: 3/5 (need >=4). Harm wins: 1/5 (need >=4). Criterion R FAILS on both legs**, and fails badly on the harm leg specifically -- FULL has *more* harm events than NATIVE on 3 of 5 seeds (47, 48, 49) and is tied on a 4th (51); seed 50 is the only seed where FULL clearly reduces harm. Note seed 51's "win" is a rounding-level tie (both arms and FULL-minus-R5 produced nearly identical trajectories -- see "undirected noise" section), not a real effect.

## Criterion N (necessity): FAIL

Dropping R5, and dropping R2, each lose >= half of FULL's reward gain over NATIVE (`G = FULL_reward - NATIVE_reward`) on >= 3/5 seeds.

| seed | G = FULL-NATIVE | drop-R5: G_R5 | frac of G lost dropping R5 | R5 necessary? | drop-R2: G_R2 | frac of G lost dropping R2 | R2 necessary? |
|---|---|---|---|---|---|---|---|
| 47 | -0.456 (no gain -- FULL is worse) | -0.139 | n/a | n/a | -0.024 | n/a | n/a |
| 48 | -0.221 (no gain) | -0.132 | n/a | n/a | +0.062 | n/a | n/a |
| 49 | +0.208 | +0.078 | 0.63 | YES | +0.257 | -0.23 (dropping R2 *helps*) | NO |
| 50 | +6.460 | +1.131 | 0.82 | YES | +8.088 | -0.25 (dropping R2 *helps*) | NO |
| 51 | ~+0.0000 (no real gain) | +0.0017 | n/a | n/a | -0.171 | n/a | n/a |

**Only 2 of 5 seeds (49, 50) show FULL actually gaining over NATIVE at all**; the necessity question is only well-posed on those two. On those two, **R5 is necessary in 2/2** but that is 2/5 against the pre-registered >=3/5 threshold, so **R5: FAIL**. **R2 is necessary in 0/2** -- on both seeds where FULL has a real gain, dropping R2 alone (FULL-minus-R2) does *better* than FULL itself (s49: -0.029 vs -0.078; s50: -0.613 vs -2.241), so **R2: FAIL**, and in the opposite direction from ADDENDUM 3 (which found R2 necessary in 2/3 seeds there). Averaged over all 5 seeds, FULL-minus-R2 (mean reward -0.179) beats FULL (mean reward -0.623) outright. **Criterion N FAILS on both legs.**

## Undirected-noise flag

Any seed where FULL raises action entropy but lowers reward vs NATIVE:

- **Seed 47**: FULL entropy 1.088 > NATIVE entropy 0.667; FULL reward -0.522 < NATIVE reward -0.065. **Flagged.** NATIVE entropy = 0.667.
- **Seed 48**: FULL entropy 0.637 > NATIVE entropy 0.535; FULL reward -0.291 < NATIVE reward -0.070. **Flagged.** NATIVE entropy = 0.535.
- Seed 49: FULL entropy 0.565 > NATIVE entropy 0.075, but FULL reward -0.078 > NATIVE reward -0.286 (reward improved) -- not flagged.
- Seed 50: FULL entropy 1.046 > NATIVE entropy 0.936, but FULL reward improved -- not flagged.
- Seed 51: FULL entropy 0.590 < NATIVE entropy 0.633 (lower, not raised) -- not flagged.

**2 of 5 seeds (47, 48) show the undirected-noise pattern**, matching the seed-43 pattern from ADDENDUM 3 (there, one of three seeds).

## Post-hoc diagnostic (not pre-registered) -- true harm contacts vs hazard-proximity steps

Mid-run, the orchestrator flagged that an instrumented re-run of a seed is only acceptable as a clearly labelled post-hoc diagnostic, that Criteria R/N above must come strictly from the original five pre-registered runs (they do -- the table above and both verdicts are computed only from `results_preregistered_original/PART_s{47..51}.json`, backed up before any re-run), and that a divergent-vs-reproduced check must be reported rather than silently substituted.

**Why this was run at all:** the pre-registration's secondary DV explicitly asked for "harm contacts per 100 steps (true contacts; report hazard-proximity steps separately, per Worker F's correction)" (`e3_evaluation_edge_test_20260924.md`, Worker F: `CONTACT = {agent_caused_hazard, env_caused_hazard, env_caused_multisource}` vs the separate `hazard_approach` transition type). ADDENDUM 3's unmodified harness does not distinguish these -- `harm_events_per_100` is `(reward < 0).sum()`, which sums true contacts and graduated hazard-proximity reward steps (`causal_grid_world.py:2634-2647` contact branches vs `:2739` proximity-only branch) together. All "harm contacts" numbers in the tables above are this conflated quantity, not the pre-registered "true contacts" definition.

**What was done:** one additive instrumentation line was added to `closed_loop_rewards` (tally `info["transition_type"]` into a `Counter`; does not read or write anything else, does not touch RNG, policy, env config, or any existing computation) and **only seed 47** was re-run with it, writing over `results/PART_s47.json` (the pre-registered original for seed 47 had already been copied to `results_preregistered_original/` first, so no data was lost). Seeds 48-51 were **not** re-run; only seed 47's original run had already been kicked off with this instrumentation attached before the orchestrator's message landed, so it is reported here as the one post-hoc data point rather than discarded.

**Reproduction check:** the instrumented re-run's `reward_per_100`, `harm_events_per_100`, and `action_entropy` are **bit-identical** to the pre-registered original on all 4 arms (verified by direct float comparison, e.g. FULL reward `-0.5217127249141535` both times). The instrumentation is confirmed non-perturbing.

**What it shows, seed 47 only:**

| arm | harm_events/100 (conflated, pre-registered metric) | true harm contacts/100 | hazard-proximity steps/100 |
|---|---|---|---|
| FULL | 8.00 | 1.00 | 7.00 |
| FULL-minus-R5 | 2.67 | 0.50 | 2.17 |
| FULL-minus-R2 | 4.33 | 0.17 | 4.17 |
| NATIVE | 3.67 | 0.17 | 3.50 |

On seed 47, decomposing the metric does **not** change the direction of the finding: FULL still has *more* true harm contacts than NATIVE (1.00 vs 0.17) and *more* hazard-proximity steps (7.00 vs 3.50) -- both components of the conflated metric point the same way FULL was already found to be worse. This is only 1 of 5 seeds, so it cannot be generalised, but it weighs against the possibility that the conflated metric was masking a true-contacts-only win for FULL. **This diagnostic does not change either pre-registered verdict (both already FAIL on the original metric).**

**Flag for future work (not landed as a claim or code change):** the harness's `harm_events_per_100` field conflates true contacts and hazard-proximity steps throughout ADDENDUM 3 and this replication. A run intending to test the pre-registered "true contacts" DV specifically should carry this decomposition from the start, for every arm and seed, not add it post-hoc to one seed.

## Domain and what this does NOT show

**D3 reached**: this is a closed-loop, env-grounded result (the environment's own `harm_signal` reward stream under a real, unmodified policy difference), not a decodability or intervention-on-a-proxy claim.

**What it does not show:**
- **Only one regime** (Regime B: `CausalGridWorldV2`, size 8, 2 hazards, 3 resources, `world_dim` 32, the deployed dim where it matters) and **one encoder budget** (SD-070, 20 episodes x 50 steps, preservation 1000). No claim about other regimes, other grid sizes/hazard densities, or other encoder training schedules.
- **600 steps per arm, 5 seeds.** Short-horizon; seed 50's 44-episode NATIVE run (hazard-heavy start) alone accounts for most of the magnitude in the mean row, exactly as ADDENDUM 3 warned for its own seed 42.
- **No benefit-seeking claim.** Benefit events are low and not clearly directed by any arm (FULL mean 0.57/100 vs NATIVE 0.33/100, but FULL-minus-R2 alone is comparable at 0.30/100 -- consistent with ADDENDUM 3's finding that E3's default J has no trained benefit channel).
- **No generalisation beyond these 5 seeds.** The seeds were chosen to be disjoint from ADDENDUM 3's (42-46) specifically to test whether the effect generalises, and the answer here is that it does not replicate at the pre-registered thresholds.

## Read-out

1. **The R5b+R2 (no-COV) FULL configuration does NOT replicate on fresh seeds at the pre-registered thresholds.** Reward wins 3/5 (need 4), harm wins 1/5 (need 4). On 3 of 5 fresh seeds (47, 48, 49-barely) FULL has *more* harm events than NATIVE, the opposite of ADDENDUM 3's headline direction.
2. **Necessity of R5 is directionally consistent with ADDENDUM 3 but underpowered here**: necessary on both seeds where FULL shows a real gain (49, 50), but that is 2/5 against the pre-registered 3/5 bar, and 3 of 5 seeds show no real FULL gain to test necessity against at all.
3. **Necessity of R2 does NOT replicate and reverses direction**: on both gain seeds, dropping R2 alone outperforms FULL. This is the sharpest new finding here -- ADDENDUM 3 called R2 necessary on 2 of 3 seeds; on this fresh seed set R2 looks actively harmful when combined with R5, at least in the mean.
4. **Undirected noise (FULL raises entropy, lowers reward) recurs on 2 of 5 fresh seeds** (47, 48), a higher rate than ADDENDUM 3's 1 of 3, reinforcing that R5's coverage scaffold is not state-conditioned and does not reliably convert into directed harm avoidance without a favourable seed.
5. **Read plainly**: ADDENDUM 3's positive result (2 of 3 seeds, both hazard-heavy) looks like it was seed-dependent rather than a general repair. The pattern that DOES hold across both records is that when the NATIVE agent already starts in a hazard-heavy trap (ADDENDUM 3 s42, this record's s50), R5+R2 substantially helps; when NATIVE starts benign or moderately hazardous (ADDENDUM 3 s43/s44, this record's s47/s48/s49/s51), R5's added movement more often adds harm than removes it. That is a narrower, conditional claim than ADDENDUM 3's "sufficient in 2 of 3 seeds" framing, and it did not hold up as stated against fresh seeds.

## Limits

5 seeds, 600 steps per arm, one encoder budget, Regime B only -- same limits ADDENDUM 3 stated for itself. The true-harm-contacts-vs-hazard-proximity decomposition exists for 1 of 5 seeds only (post-hoc). Choice-quality-vs-env-Q data was collected (own-replay head, full horizon and depth-1) but not used in either pre-registered criterion; it is in the raw JSON for anyone who wants it (`pick_is_Qbest` ranges 0.0-0.32 against 0.20 chance across the 5 seeds, consistent with ADDENDUM 3's finding of a weak, repair-independent evaluator). No claim, registry, or queue entry was touched -- this is a probe-only record per the worker brief.
