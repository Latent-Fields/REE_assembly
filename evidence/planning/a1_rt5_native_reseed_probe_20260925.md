# A1 RT-5 closer: NATIVE vs reseeded-NATIVE noise, tie-break ON (and A1 seed-screen pilot)

- **Status: RESULTS APPENDED 2026-09-25T16:49Z (sec 5-8).** Pre-registered 2026-09-25T14:56Z; the pre-registration landed as REE_assembly `59c3b43746` before any probe seed ran. Secs 1-4 are unchanged from that commit, apart from this status line.
- **Verdict in one line.**
  - The benign reward (0.90), benign contacts (1.6), trapped reward (2.4) and trapped contacts (4.8) floors ARE lower bounds on the measured NATIVE-reseed noise. For the trapped floors the margin is 5-7x.
  - The benign reward-change floor (1.44) is NOT a lower bound: it is 3.4x the measured 0.43.
  - **The larger finding is that the measured noise itself breaks A1 as designed.**
    - The benign superiority margin becomes about 1.7 per 100, which is above P1b's reachable gain.
    - A1's balloon guard fires on trapped reward, trapped contacts and (at the point estimate) benign contacts.
    - The trapped stratum is not a property of the env seed: 2 of 9 reseeds of a trapped seed are trapped.
  - See sec 6-7.
- **Session:** `bt0925-rt5`, headless worker of `orchestrate-20260924-breakthrough`. chip_ref `chip-20260925-a1-rt5-native-reseed-probe`.
  - Resume note (2026-09-25T18:05Z): `bt0925-rt5` wrote secs 5-8 at 16:50Z and hit the usage wall before committing. Resumed as `bt0925-rt5b`, which re-verified before committing: the committed results files are byte-identical to the scratch outputs; the scripts are byte-identical to the pre-registered copies at `59c3b43746`; the per-seed sha1 prefixes match; every number in secs 5-6 matches `RT5_analysis.out`. `bt0925-rt5b` changed nothing else, apart from replacing one `<sha>` placeholder in sec 7.2 item 1.
- **Question (A1 prereg `coupled_a1_preregistration_draft_20260925.md` sec 6.3, sec 14 O1, sec 15 RT-5).** The accepted A1 floors come from a T2 agent with a 4-channel weight walk, not from NATIVE reseeded with tie-break ON. The draft asserts that these floors are lower bounds on the target noise. It does not measure it. This probe measures the target quantity directly: 2 x RMS of per-seed deltas NATIVE - NATIVE-Rk, with the env seed fixed and the agent seed varied, in A1's regime and windows. It then asks, for each floor: is floor <= measured?
- **Scope.** Read-only on shared code. No `ree_core` edit, no queue entry, no edit to the A1 draft. The recommended edits to the A1 draft are listed in sec 7. Evidence domain: **D1** (a closed-loop noise measurement; no intervention on a consumer).
- **Code:** ree-v3 `origin/main` @ `aa147695073f2a9bbded26166d42bfe720f35315` (a detached throwaway worktree). Scripts: `probes/a1_rt5/` (`rt5_native_reseed_probe.py`, `run_rt5.py`, `analyze_rt5.py`, `with_lock.sh`). They were run from `.scratch/breakthrough-20260924/rt5/`, where the worktree sits at `./ree-v3-wt`.

## 1. Premises re-measured (14:50-14:56Z)

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | A1's floors: reward 0.90 benign / 2.4 trapped; contacts 1.6 / 4.8; reward change 1.44 (benign) | A1 draft sec 6.3 table and skeleton `FLOORS`, `origin/master` (draft head `a5fbbcac2b`) | holds. **Units:** `floor_grounding.py` computes contacts as a **per-100 rate over the 600-step LAST window** (`LAST600_contacts_per100`), so 1.6 means 9.6 contacts per 600 steps. A1 sec 0/V1 says "contacts per 600-step window", which reads like a count. This probe uses the per-100 rate, as the skeleton's `contacts_LAST` does |
| P2 | Reward change = LAST - FIRST over 600-step windows (0-599, 2400-2999) | A1 sec 8 P4; skeleton `window_stats`. The floor itself was derived from half2 - half1 over 750-step halves and scaled by sqrt(1.25) | holds. The probe measures the A1 form directly (LAST600 - FIRST600) |
| P3 | Env seed and agent seed must be split (A1 Q6) | `CausalGridWorldV2` draws from `self._rng = default_rng(seed)` and `_traj_pair_rng` (seeded from the env seed). `run_zworld_p0` uses private `torch.Generator`s seeded from its `seed` arg (`ree_core/latent/zworld_p0.py:513,580`) and does not touch the global RNG | holds. The probe builds the env with `env_seed` first, then calls `seed_all(agent_seed)`, and passes `agent_seed` to the warmup recipe, its `RandomPolicy`, and the harness fallback RNG |
| P4 | NATIVE = default `REEConfig` at world_dim 32 | `REEConfig.from_dims` default `world_dim=32` (`ree_core/utils/config.py:8163`); asserted in-run | holds. `from_dims` warns that `alpha_world` defaults to 0.3 (below the SD-008 floor of 0.9). NATIVE keeps the default, as A1's "all flags off" implies |

**Timing smoke, disclosed.** Before this pre-registration was written, one smoke ran on env seed **1999**. It is outside the probe range and is not used in any result. It was NATIVE, dev 300, closed loop 700. Measured: about 0.03 s per step; the P0a warmup took about 1 s. **Observed:** NATIVE chose action class 1 on 692 of 700 closed-loop steps. The default agent's policy is close to a fixed single action. This is why the noise ordering cannot be argued from the T2 analog: a near-deterministic policy may produce either very small reseed spread (every reseed does the same thing) or very large spread (each reseed locks onto a different action).

## 2. Pre-registered design

**Env seeds (fresh):** 2001, 2002, ... up to 2040, screened in ascending order. This range is disjoint from 42-290 (earlier probes, 1105, 1105a) and from A1's own range (301 upward, ceiling 80 seeds plus reserves). It is a **pilot** of the A1 screen: it gives the NATIVE stratum rate and the per-step cost. It is not the A1 screen, which must run on the pinned W6 sha.

**Per env seed s, arms k = 0..3, agent_seed = s + 10,000 x k** (A1 `AGENT_SEED_OFFSET`; k = 0 is NATIVE, k = 1..3 are NATIVE-R1..R3, as in A1 sec 5.1). The protocol is identical in every arm, and follows A1 sec 4:
1. `env = CausalGridWorldV2(size=8, num_hazards=2, num_resources=3, max_episode_steps=200, proximity_approach_magnitude_tiebreak=True, seed=s)`, constructed before any agent seeding.
2. `seed_all(agent_seed)`; `agent = REEAgent(REEConfig.from_dims(body_obs_dim, world_obs_dim, action_dim))`; eval mode throughout. No trainer; NATIVE has none.
3. Developmental epoch: **2,400** native waking steps (`StepHarness(train_mode=False, seed=agent_seed)`), reset on done. For NATIVE this learns nothing; it only advances env, residue and goal state, as it will in A1.
4. SD-070 P0a encoder warmup: 20 episodes x 50 steps, `RandomPolicy(agent_seed)`, `ZWorldP0Config(preservation_weight=1000.0)`, on a dedicated env built with `seed=s`, recipe seed = agent_seed (the rollout-record protocol A1 sec 4 cites).
5. Closed loop: `env.reset(); agent.reset()`, then **3,000** steps with eval `StepHarness`, reset on done. Recorded per step: `harm_signal`, `transition_type`, done and done_cause, and the action class.

**Windows (as A1):** FIRST = closed-loop steps 0-599, LAST = 2,400-2,999, with per-100 rates over each 600-step window. The full A1 protocol is affordable, so there is no shrink: about 5,400 agent steps per arm at about 0.03 s per step, so about 3 min per arm and about 11-12 min per admitted seed.

**Stratum (A1 sec 3 rule, from NATIVE alone):** `hazard_trapped` iff NATIVE has >= 10 episodes that end inside closed-loop steps 0-599 with length < 200. Otherwise `benign`. Each reseed's own stratum is also recorded, for information only; A1 scores reseed deltas under NATIVE's stratum.

**Admission and stop rule (driver `run_rt5.py`):**
- The first **3 benign** and the first **3 hazard_trapped** env seeds in screen order are admitted. They get NATIVE to 3,000 plus R1-R3 in full.
- A seed whose stratum quota is already full is screen-only: NATIVE stops after closed-loop step 599.
- Stop when both quotas are full, at seed 2040, or when the cumulative child compute wall reaches **85 min**. The budget is checked before each new seed starts.
- 3 seeds x 3 reseeds = 9 deltas per stratum, which clears A1's `MIN_DELTAS_PER_STRATUM` of 8. Quota 3 rather than A1's 5 is the budget shrink. The brief's budget is about 75 min of Mac wall, and A1 itself will measure with 5 seeds.
- Execution: one child process per env seed, 2 torch threads, under the shared Mac CPU lock (`mkdir .../mac_probe.lock`, retried every 30 s; >= 800 MB available) (`with_lock.sh`).

**Metrics:** the A1 DVs per arm: reward_LAST, reward_FIRST, reward change (LAST - FIRST), true harm contacts in LAST (per 100), grounded component G in LAST (per 100: reward on contact and consumption steps), and consumptions in LAST. Also reported: the modal action class and its share, and reseed stratum concordance.

## 3. Pre-registered analysis and verdict rule (`analyze_rt5.py`)

- Per stratum (NATIVE's), per metric, the measured noise is `M = 2 x RMS` of all per-seed deltas NATIVE - NATIVE-Rk, pooled over that stratum's admitted seeds. This is the A1 sec 6.2 margin form without the floor. A seed-level bootstrap 90% interval (2,000 resamples of admitted seeds, `default_rng(0)`) is reported alongside it.
- Verdict for each metric that has an accepted floor (reward_LAST b/t, contacts_LAST b/t, reward change b):
  - **CANNOT_DETERMINE** if that stratum has fewer than 8 deltas, or any admitted seed has fewer than 2 completed reseeds (A1's own CD rule). The report states how many seeds were screened and admitted.
  - **LOWER_BOUND** if floor <= M: the floor is at or below the target noise, as the A1 draft asserts. The runtime term dominates, and the floor binds only on a degenerate stratum.
  - **NOT_LOWER_BOUND** if floor > M: the floor exceeds the measured target noise, so in A1 the floor, not the measured noise, would set the margin.
  - The suffix `_WITHIN_CI` is added when the floor lies inside the bootstrap 90% interval. That verdict is then within sampling noise at n = 3 seeds.
- **Reading by criterion kind (fixed now):**
  - A NOT_LOWER_BOUND **superiority** floor (reward, change) makes P1b/P3/P4 stricter than NATIVE's noise warrants. That is conservative, and it costs power.
  - A NOT_LOWER_BOUND **non-inferiority** floor (contacts; the trapped reward floor used by P1t) makes P2/P1t more lenient than the noise warrants. That is the direction RT-5 worries about.
  - A LOWER_BOUND verdict on a superiority floor with M >> floor means the floor is irrelevant; the runtime term governs.
  - A LOWER_BOUND verdict on a non-inferiority floor with M > 3 x floor means A1's balloon guard would fire (`margin_ballooned`). This is reported as a predicted A1 CANNOT_DETERMINE.
- No criterion here moves an A1 verdict. The output is a recommendation list for the A1 draft (sec 7), and the owner of the floors is the user.

## 4. Stop rules

No interim reading of deltas. Strata and timings may be read as seeds land. The driver is not edited after the first probe seed starts. A crash is logged as `crashed`, and the next seed continues. A crashed seed is never admitted.

## 5. Results (run 14:57-16:48Z; analysis `analyze_rt5.py` exactly as pre-registered)

**Run facts.**
- 8 env seeds screened (2001-2008): 5 benign and 3 hazard_trapped by NATIVE's stratum. Stop reason: both quotas full.
- Admitted: benign 2002, 2003, 2004; trapped 2001, 2007, 2008. No crash. The driver was not edited.
- Compute: 5,206 s, about 87 min (the budget check fires only before a new seed starts; the last admitted seed began at 4,271 s). Lock waiting on the shared Mac lock came on top of that: the first seed waited about 25 min.
- **Pilot trapped rate is 3/8 = 0.375**, against the 0.21 (4/19) A1 sec 3 assumes from the T2 screen. This is NATIVE, not T2.
- Per full arm (5,400 agent steps), measured on the shared Mac: 123-439 s, median about 180 s, i.e. 0.023-0.08 s per step. A NATIVE screen to step 599 took 70-240 s.
- Raw per-seed JSONs are scratch-only, 1.3 MB in total, at `.scratch/breakthrough-20260924/rt5/results/RT5_s<seed>.json`. sha1 prefixes: 2001 `9980fed4`, 2002 `c5b23ae2`, 2003 `46fbc774`, 2004 `029d6c0c`, 2005 `d3d3703d`, 2006 `0eafe4f0`, 2007 `b3424cb1`, 2008 `2a790e31`.
- Committed next to this record: `probes/a1_rt5/results/{RT5_log.json, RT5_analysis.json, RT5_analysis.out}`.

**Per-arm values (per 100 steps; L = LAST 2400-2999, F = FIRST 0-599).** "Own" is the arm's own A1-rule stratum; "modal" is the modal action class and its share over the closed loop.

| env seed (NATIVE stratum) | arm | own | reward F | reward L | change | contacts L | G L | modal |
|---|---|---|---|---|---|---|---|---|
| 2002 (benign) | NATIVE | b | -0.11 | +0.05 | +0.16 | 0.00 | +0.06 | a1 0.52 |
| | R1 | b | -0.59 | -0.63 | -0.04 | 3.00 | -1.13 | a0 0.79 |
| | R2 | b | -0.74 | -0.82 | -0.08 | 3.17 | -1.06 | a1 0.73 |
| | R3 | **t** | -1.81 | -1.82 | -0.01 | 5.50 | -2.06 | a0 0.87 |
| 2003 (benign) | NATIVE | b | -0.72 | -0.74 | -0.02 | 2.00 | -0.62 | a0 0.82 |
| | R1 | b | -0.15 | -0.06 | +0.10 | 0.67 | -0.12 | a0 0.80 |
| | R2 | b | -0.49 | -0.20 | +0.29 | 1.33 | -0.31 | a1 0.48 |
| | R3 | b | -0.72 | -0.44 | +0.29 | 2.00 | -0.77 | a2 0.55 |
| 2004 (benign) | NATIVE | b | +0.04 | +0.18 | +0.14 | 0.00 | +0.17 | a2 0.99 |
| | R1 | b | -1.07 | -0.77 | +0.30 | 2.50 | -0.88 | a0 0.88 |
| | R2 | b | +0.06 | +0.02 | -0.03 | 0.17 | +0.02 | a3 0.85 |
| | R3 | b | +0.17 | +0.14 | -0.03 | 0.00 | +0.12 | a1 0.88 |
| 2001 (trapped, 58 early) | NATIVE | t | -9.88 | -10.25 | -0.36 | 28.67 | -11.35 | a4 0.64 |
| | R1 | **b** | -0.05 | +0.02 | +0.07 | 0.00 | 0.00 | a0 1.00 |
| | R2 | **b** | -0.34 | -0.44 | -0.10 | 1.67 | -0.66 | a2 0.51 |
| | R3 | t | -4.34 | -6.29 | -1.94 | 17.50 | -6.94 | a3 0.54 |
| 2007 (trapped, 22 early) | NATIVE | t | -3.40 | -2.71 | +0.69 | 8.33 | -3.01 | a2 0.61 |
| | R1 | t | -1.47 | -1.39 | +0.07 | 4.83 | -1.72 | a2 0.71 |
| | R2 | **b** | +0.04 | +0.17 | +0.13 | 0.00 | +0.06 | a2 0.97 |
| | R3 | **b** | -0.57 | -0.92 | -0.35 | 2.83 | -0.87 | a0 0.49 |
| 2008 (trapped, 40 early) | NATIVE | t | -6.60 | -6.89 | -0.29 | 19.67 | -7.60 | a4 0.49 |
| | R1 | **b** | -0.90 | -0.90 | -0.01 | 3.00 | -0.96 | a0 0.78 |
| | R2 | **b** | -0.29 | -0.10 | +0.19 | 0.50 | -0.11 | a0 0.91 |
| | R3 | **b** | +0.08 | +0.13 | +0.04 | 0.00 | +0.06 | a2 0.73 |

## 6. Verdicts against the accepted floors (pre-registered rule, sec 3)

M = 2 x RMS of the per-seed deltas NATIVE - NATIVE-Rk. There are 9 deltas per stratum (3 seeds x 3 reseeds), which clears A1's CD threshold of 8. The interval is a seed-bootstrap 90% interval.

| metric (per 100) | stratum | accepted floor | measured M | boot 90% | M / floor | verdict | A1 balloon guard (M > 3 x floor)? |
|---|---|---|---|---|---|---|---|
| reward, LAST | benign | 0.90 | **1.70** | [1.08, 2.14] | 1.9 | **LOWER_BOUND** | not guarded (superiority) |
| reward, LAST | trapped | 2.4 | **12.68** | [8.37, 15.85] | 5.3 | **LOWER_BOUND** | **fires** (12.7 > 7.2) |
| contacts, LAST | benign | 1.6 | **5.07** | [2.18, 6.83] | 3.2 | **LOWER_BOUND** | **fires at the point estimate** (5.07 > 4.8; the CI straddles) |
| contacts, LAST | trapped | 4.8 | **35.40** | [23.6, 44.1] | 7.4 | **LOWER_BOUND** | **fires** (35.4 > 14.4) |
| reward change L - F | benign | 1.44 | **0.43** | [0.36, 0.49] | 0.30 | **NOT_LOWER_BOUND** (the CI excludes the floor) | - |

Reported, no floor:
- benign: G_LAST 1.96, consumptions 0.69, reward_FIRST 1.51;
- trapped: change 1.48, G_LAST 13.9, consumptions 1.08, reward_FIRST 12.6.

Other readouts:
- **Reseed stratum concordance with NATIVE's stratum:** benign 8/9; **trapped 2/9**.
- **Between-seed SD of NATIVE reward_LAST:** benign 0.50; trapped 3.77.

**RT-5 answer (as asked).** Four of the five floors are lower bounds on the measured target noise, as the A1 draft argued. The benign change floor is not.
- **Reward and contact floors.** The ordering the draft argued holds. The draft's argument was that a weight walk perturbs less than a reseed. That argument is correct, but it understates the gap: the reseed noise is 1.9-7.4x the floor.
- **The change floor.** NATIVE learns nothing in the closed loop, so each agent's reward level is stable across the run (F close to L), and the level differences between reseeds cancel in LAST - FIRST. The T2 analog did change over its run, so its half-to-half change noise was larger. The 1.44 floor therefore binds against NATIVE's noise. For P4 the relevant noise is INT-vs-INT, and A1's INT-v-R1 term measures that directly. So a NATIVE-based "lower bound" statement for P4 is uninformative in both directions.

**Mechanism (D1, from the per-arm table).**
- The default NATIVE agent is close to a fixed-action policy. Its modal action share is 0.49-1.00, median about 0.78, and **which** action it prefers changes with the agent seed (a0-a4 all appear).
- Reseeding therefore changes *where the agent goes*, and with it the hazard exposure. So the "hazard_trapped" condition is largely a property of the (env seed, agent init) pair: NATIVE trapped with 58 early terminations on seed 2001, while two of its three reseeds are benign with <= 2.
- This is the stratum-concordance number above, and it is what inflates the trapped deltas: the trapped NATIVE arm is compared against reseeds that are not trapped.

## 7. Consequences for A1 (D0 arithmetic on the measured numbers) and recommended edits

**7.1 What the measured noise does to A1's criteria, assuming INT noise is no smaller than NATIVE's.** A1's margins are max(runtime 2 x RMS, floor). The runtime term will be about the measured M, so:
- **P1b (primary) becomes practically unreachable.**
  - The benign superiority margin is about 1.70 (CI 1.08-2.14), not 0.90.
  - NATIVE's benign LAST reward averages -0.17 here. The benign ceiling is about +0.45 of consumption plus at most about 0.2 of shaping (A1 sec 6.4). Across all 12 benign-stratum arms here the highest LAST reward was +0.18.
  - So the maximum achievable gain is about 0.6-0.8 per 100, below even the CI's lower end of 1.08.
  - **A1 as designed would return FAIL "gain too small for the margin" nearly by construction** (A1 sec 8.1 signature). The same arithmetic applies to P3 in the benign stratum.
- **P1t, P2t and probably P2b become `CANNOT_DETERMINE: margin_ballooned`** (A1 sec 6.2): trapped reward 5.3x its floor, trapped contacts 7.4x, benign contacts 3.2x (point estimate).
  - Since A1's PASS needs all 8 sub-criteria, a CD on P1t/P2 means **no variant can PASS**, independently of P1b.
- **P4 is unaffected by this probe's direction.** The NATIVE change noise (0.43) is below the floor, so the 1.44 floor or the INT-R1 term governs. O6 (headroom) stands as written.
- **The stratum premise is weak.** A1 sec 3 treats "hazard_trapped" as an env-seed property, classified once from NATIVE. Here only 2/9 trapped-seed reseeds stay trapped.
  - An INT arm starts from a different init even at the same agent seed (A1 sec 3 caveat). So on a trapped env seed, an INT arm may be untrapped for reasons unrelated to its mechanism.
  - That favours INT on P1t and P2t, which is the lenient direction for a non-inferiority test.
- Caveats:
  - n = 3 seeds per stratum;
  - NATIVE on ree-v3 `origin/main` @ `aa14769`, not a W6 pin. NATIVE is all flags off, so the branch should not change it, but this is not verified;
  - INT arms may be less action-collapsed than NATIVE and hence less noisy. That is unmeasured, and A1's INT-R1 term would measure it.

**7.2 Recommended edits to `coupled_a1_preregistration_draft_20260925.md`** (NOT applied here; the owner of the floors, the margin rule and the stratum rule is the user):
1. **sec 1 table:** add Q12. "RT-5: NATIVE-vs-reseeded-NATIVE spread, tie-break ON, measured (this record, `evidence/planning/a1_rt5_native_reseed_probe_20260925.md` sec 6; results commit = the commit that added sec 5-8): 2 x RMS benign reward 1.70, trapped reward 12.7, benign contacts 5.07, trapped contacts 35.4, benign change 0.43 (9 deltas per stratum)." Verdict: **corrected**.
2. **sec 6.3:** replace the paragraph "The doc's claim that these are lower-bound noise estimates ... (asserted, not shown; RT-5 open)" with the measured verdicts from sec 6 above:
   - reward and contact floors: lower bounds, 1.9-7.4x below the measured noise;
   - change floor: NOT a lower bound (0.43 < 1.44).
   Also replace the "Expected consequence" bullet with the measured one: the runtime term dominates in every reward and contact cell.
3. **sec 6.3 units:** the V1 row and sec 0 say contacts are "per 600-step window". The floors are per-100 rates over the 600-step window (`floor_grounding.py` `LAST600_contacts_per100`). State "per 100 steps, over the LAST 600-step window".
4. **sec 6.4 (headroom), new paragraph:** with the measured benign superiority margin of about 1.7 and a maximum benign gain of about 0.6-0.8, P1b is not reachable at 5 seeds under the per-seed ">= 4/5 exceed margin" rule. Add this as open item **O11: A1 power**, owner the user, before queueing. Options for the user, none taken here:
   - (a) replace the per-seed exceed-margin count with a paired test on the mean INT - NATIVE delta across seeds, e.g. mean delta > 2 x SE, which shrinks with n;
   - (b) replicate NATIVE and each INT arm over K agent seeds per env seed and compare arm means (the noise scales as 1/sqrt(K); cost x K);
   - (c) raise the number of benign seeds;
   - (d) reduce the policy's init-dependence (see 5) before A1, i.e. accept that today's NATIVE comparator is dominated by init "personality".
5. **sec 3 (stratum):** record the 2/9 concordance. Add open item **O12**: define `hazard_trapped` as an env-intrinsic property, or score the trapped stratum per (env seed, agent seed) pair. Candidate options:
   - classify from a fixed-seed RandomPolicy rollout on the env seed, so agent init cannot move it;
   - or require that INT and NATIVE share the init of their common modules (construct the NATIVE module set first from the agent seed, and initialise INT-only modules from a separate generator). This reduces NATIVE-vs-INT init noise, but not NATIVE-vs-NATIVE-Rk noise.
6. **sec 6.2 balloon guard:** add "predicted to fire (measured): trapped reward, trapped contacts, benign contacts at the point estimate". Under the current rules A1 would therefore return CANNOT_DETERMINE on P1t/P2t/P2b. This is linked to O11/O12.
7. **sec 3 screen / sec 9:** the pilot trapped rate is 3/8 (0.375) under NATIVE, vs the 0.21 used. The expected screen length for 7 trapped seeds drops from about 33 to about 19 seeds (small n; re-measure on the pin).
8. **sec 11 cost:** measured NATIVE full arm (5,400 steps) 123-439 s on the shared Mac (0.023-0.08 s per step), and 70-240 s for a screen to step 599. That is below the draft's 0.18-0.24 s per step for trapped seeds, which came from the T2 agent. It is NATIVE only; INT arms are unmeasured.
9. **sec 14:** O1 (RT-5) -> **CLOSED (measured)**, pointing to this record. Add O11 (power) and O12 (stratum is agent-dependent).
10. **sec 15 RT-5 row:** disposition "OPEN" -> "MEASURED: 4 of 5 floors are lower bounds, the change floor is not. The measured noise makes P1b unreachable and ballooned P1t/P2 (O11, O12)".

## 8. Premises corrected by this record

- "The floors are lower bounds" (A1 sec 6.3, asserted). **Measured:** true for reward and contacts, false for the benign reward change.
- "The runtime 2 x SD will probably exceed the floors in the benign stratum" (A1 sec 6.3). **Measured true**, and it exceeds them by enough to make P1b unreachable (7.1).
- "hazard_trapped" as an env-seed property (A1 sec 3, implicit). **Measured weak** under NATIVE: 2/9 reseed concordance in the trapped stratum.
- Trapped base rate 0.21 (T2 screen). **NATIVE pilot:** 0.375 (3/8).
- Per-step cost of trapped seeds, 0.18-0.24 s (T2). **NATIVE:** 0.023-0.08 s per step.
