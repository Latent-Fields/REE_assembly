# A1 RT-5 closer: NATIVE vs reseeded-NATIVE noise, tie-break ON (and A1 seed-screen pilot)

- **Status: PRE-REGISTERED 2026-09-25T14:56Z. Nothing below sec 3 has been run on a probe seed.** Results are appended in sec 5 onwards, after this pre-registration is on `origin/master`.
- **Session:** `bt0925-rt5`, headless worker of `orchestrate-20260924-breakthrough`. chip_ref `chip-20260925-a1-rt5-native-reseed-probe`.
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
