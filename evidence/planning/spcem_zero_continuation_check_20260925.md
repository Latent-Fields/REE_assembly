# SP-CEM zero-continuation check (2026-09-25)

Session `bt0925-spcem`, chip `chip-20260925-spcem-zero-continuation-check`, orchestrator `orchestrate-20260924-breakthrough`.
Code refs are file:line at **ree-v3 origin/main `1a61800`** (detached throwaway worktree).

**Status: complete.** D0 confirmed. D1 confirmed (zero tails measured in every native token, 85/85 states). D2: the token's construction, not its class, puts it **dead last** in E3's ranking. Swapping in an on-manifold head and tail moves it to the top of the pool, and holding its class for the whole horizon changes E3's native selection rate of that class by about 10x on 2 of 3 seeds. Worker C's *descriptive* finding holds ("the token never beats the best of ~31"). The *mechanism* Worker C gave for it (an order statistic over roughly exchangeable scores) does **not** hold for tokens. Governance flag raised (sec 4).

## Verdict (short)

| finding | domain | result |
|---|---|---|
| F1. The default-ON SP-CEM tokens are one-hot at t=0 with exact zeros at t=1..29, and E3 scores all 31 states | D0 + D1 | **confirmed**. `token_tail_abs_max = 0.0` at every token state, all 3 seeds |
| F2. The native token ranks last of 32 in E3's scores | D1 | **85/85 token states, 3/3 seeds (mean rank 31.00)**. It beats the majority MEAN at **0/85** states and the majority BEST at 0/85 |
| F3. The loss is caused by the construction, not by the class | D2 | a **majority-class** token with the same construction (one-hot(maj) + zeros) is also rank 31 at 85/85 states |
| F4. Which part of the construction costs what depends on the seed | D2 | seed 11: mostly the one-hot HEAD; seed 23: mostly the zero TAIL; seed 37: both (table below) |
| F5. An on-manifold class-c alternative is competitive | D2 | pm_bt (the best majority candidate with only its t=0 argmax swapped to c) has mean rank 0.00 / 7.53 / 2.06 and beats the majority mean at 100% / 93% / 100% of states |
| F6. Holding the token's class for the whole horizon changes native E3 selection of that class | D2 | selected class = token class: control 0 / 1 / 1 states vs hold 0 / 9 / 13 (of 21 / 30 / 34). The effect has the opposite sign on seed 11, where hold is also rank 31 |
| F7. E3's scores on off-manifold action inputs are not interpretable as content | D2 | "hold" (one-hot at every step) is rank 31 on seed 11 but rank 0 on seeds 23 and 37. Action-magnitude-driven rollouts flip sign by seed |
| Closed-loop consequence (does fixing the tokens change behaviour/outcome) | -- | **not reached (no D3)** |

## Source premises, re-measured

- `action_space_proposals_design_20260925.md` (P2, sec 7): "the default-ON SP-CEM floor tokens have zero-vector continuations" and "Worker C read 'token never beats the best of ~31' as an order-statistic effect; the off-manifold continuation is an unconsidered second cause". It cited `config.py:2966` for the default. **Line drift:** at `1a61800` the default is `config.py:3020` (dataclass) / `:9141` (from_dims). The content of the premise holds (below).
- Worker C's record: `monostrategy_type_a_vs_b_discrimination_20260924.md` sec 2.3 reading 4 ("A token beats a typical majority candidate at 10-35% of states. It never beats the best of ~31, which is what one sample against the minimum of 31 samples predicts ... E3 is not shown to reject the alternative on content"). Probe `probes/repertoire/probe_p3p4_candidate_vs_selection.py`, 1061 intact arm, seeds 11/23/37.

## 1. D0 -- code trace

**Default flags** (`ree_core/utils/config.py`, HippocampalConfig): `horizon = 10` (:2961) -- **but `REEConfig.from_dims` overwrites it with `e2.rollout_horizon = 30` (:9733, :1023), so every from_dims-built agent (every experiment driver, including 1061) runs H = 30: one one-hot step and 29 zero steps**, `num_candidates = 32` (:2962), `use_support_preserving_cem = True` (:3020), `support_preserving_min_first_action_classes = 2` (:3021), `support_preserving_stratified_elites = True` (:3029), `support_preserving_ao_std_floor = 0.2` (:3038), `use_action_class_scaffold_candidates = False` (:2984). from_dims mirrors them (:9133-9145).

**Where the tokens are built.** `HippocampalModule.propose_trajectories` (`hippocampal/module.py:2037`) runs the CEM loop, then, AFTER the loop and after MECH-293 ghost mixing, calls `_inject_support_preserving_candidates` (:2530-2538, def :1576). It fires only when the final pool has fewer than `target = min(action_dim, max(2, 2)) = 2` distinct first-action classes (:1614-1615, :1419-1432) -- i.e. exactly when the CEM returned a pool whose every candidate has the same argmax first action. It then builds tokens with `_build_action_class_scaffold_candidates` (:1627-1631, def :1361-1398):

```
actions = torch.zeros(batch, horizon, action_dim)   # :1376-1382
actions[:, 0, cls] = 1.0                            # :1383
traj = self.e2.rollout_with_world(z_self, z_world, actions, compute_action_objects=True, action_bias=...)  # :1384-1390
```

So **every token carries an exact one-hot at step 0 and exact zero action vectors at steps 1..H-1** (29 of 30 steps at the from_dims horizon; 9 of 10 on a bare HippocampalConfig). The rollout is real: E2 is run on those zero actions, so the token's world_states after step 1 are E2's prediction under a zero action vector -- an input that no real candidate ever supplies (real candidates' actions are continuous `action_object_decoder` outputs, :2280 / :612-647). The token's step 0 is off-manifold too: a hard one-hot, where real candidates carry a continuous decoder vector.

Token count: `need = target - present = 1` (one token, the lowest-index missing class, :1621-1624) replacing the worst-scoring (by the hippocampal `_score_trajectory`) real candidate (:1650-1663). The tokens are **not** CEM samples and are never scored in the CEM elite refit (injection is after the loop).

**Consumers of the tokens.**
1. `REEAgent.generate_trajectories` -> `propose_trajectories` (`agent.py:7005`) -> the pool that `select_action` (`agent.py:7468`) passes to `E3Selector.select` (`e3_selector.py:3339`). E3 scores every candidate via `_get_world_states` (:1473-1491), which returns the **full horizon** unless `_score_depth_limit` is set; the default is None (:654) and only the dual-system habit path sets it (:2088, `use_dualsystem_arbitration=False` default, config.py:2462). So on the default path the token's E3 score reads all H+1 = 31 predicted z_world states: harm = sum over steps of `harm_eval_head` (:1538-1548), reality = mean squared z_world transition (coherence, :1506-1512), residue over the sequence (:1562-1566), benefit summed over steps (:1573-1577). **29 of the 30 transitions the token is judged on are consequences of zero actions.**
2. Propose diagnostics: `_excluding_injected` / `_excluding_synthetic` summaries (:2671-2760) filter them out of centroid stats; the headline field includes them.
3. MECH-057b promotion: tokens are exempt from completion-verification suppression (`_PROMOTION_EXEMPT_SOURCES`, :119-130, used :3469).
4. The diagnostic scaffold (`use_action_class_scaffold_candidates`, default False) and the R5b scaffold described in the design record use the same builder, so the same construction applies to them.

**D0 verdict: CONFIRMED.** The default-ON SP-CEM tokens roll out on all-zero action continuations after step 0, and the default E3 scores them over the full horizon. Domain D0 (code-read only). Whether this changes the token's rank is the D1/D2 question below.

## 2. D1/D2 -- probe

**Script:** `evidence/planning/probes/spcem/probe_spcem_zero_continuation.py` (outputs `probe_spcem_seed{11,23,37}.json` in the same directory). It imports V3-EXQ-1061's own `build_agent` / `warmup_train` from the detached worktree @ `1a61800`. **Config** matches Worker C's cell: intact arm (ch1 = ch2 = True), production ao_std floor 0.2, grid 5, 1 hazard, 2 resources, `self_dim = world_dim = 16` (**not** the deployed 32), `action_dim = 4`, from_dims defaults (H = 30, K = 32). Warmup is 20 episodes x 100 steps, followed by 40 probe states along a random walk. `torch.set_num_threads(2)`, one process, ~85-130 s per seed on the Mac. At every state: `torch.manual_seed(seed*1000+s)` and then the bare `hippocampal.propose_trajectories(theta_z, z_self)` (Worker C's path). Only the injected token (`metadata.source == support_preserving_cem_injected`) is swapped; the other 31 candidates are held fixed. Each variant is rolled through native `e2.rollout_with_world` from the same `(z_self, theta_z)`. Then bare `e3.select(pool, temperature=1.0)` runs under a fixed torch seed per state.

**Fidelity checks.**
- The control rebuilt through the probe's own rollout reproduces the native token's E3 score exactly at every state (`control_rebuilt_matches_native = True`, 3/3 seeds).
- The rebuilt control is scored LAST and the native control FIRST, so this check also rules out cross-call E3 state drift. The drift check was needed because deepcopying E3 is impossible (non-leaf tensors in its state).
- E3's commit gate was closed at every state (Worker C's rows show `committed_flag` = 0/40, 3/3 seeds). Selection therefore ran through the uncommitted `softmax(-scores/T)` + `torch.multinomial` path (`e3_selector.py:4133`, `:4689`). That is why "selected" is a probabilistic readout next to "argmin".

**Arms** (c = token class, maj = pool majority class, bm = the E3-best majority candidate at this state, bt = bm's own actions at t=1..29, pm head = bm's t=0 vector with its maj and c entries swapped, so the argmax becomes c (verified at 100% of states) while the magnitude stays on the decoder's manifold):

| arm | t=0 | t=1..29 |
|---|---|---|
| control (native) | one-hot(c) | zeros |
| hold | one-hot(c) | one-hot(c) |
| sampled | one-hot(c) | actions[1:] of a random real pool candidate |
| oh_bt | one-hot(c) | bt |
| pm_z | pm head (argmax c) | zeros |
| pm_bt | pm head (argmax c) | bt |
| maj_oh_z (construction control) | one-hot(maj) | zeros |
| maj_oh_bt (construction control) | one-hot(maj) | bt |

**Magnitudes.** Real candidates' decoded step-0 max entry averages 0.16 / 0.21 / 0.14 (seeds 11 / 23 / 37). Their tail per-step action norm averages 0.19 / 0.24 / 0.17. The token's step 0 is a unit one-hot, **5-7x** the real per-entry scale, and its tail is exactly 0.

**Token states:** the injection fired (exactly 1 token) at 21 / 30 / 34 of 40 states. At the other 19 / 10 / 6 states the CEM pool **natively** held >= 2 first-action classes: the minority class was a real CEM sample (usually a single one), not a token.

**Results** (mean over token states; rank 0 = best of 32; gap = token score minus best-majority score, lower = better):

| arm | s11 rank | s11 beats maj mean | s23 rank | s23 beats maj mean | s37 rank | s37 beats maj mean | beats maj BEST (s11/s23/s37) |
|---|---|---|---|---|---|---|---|
| **control** | **31.00** | **0.00** | **31.00** | **0.00** | **31.00** | **0.00** | 0 / 0 / 0 |
| hold | 31.00 | 0.00 | 0.00 | 1.00 | 0.00 | 1.00 | 0 / 1.00 / 1.00 |
| sampled | 31.00 | 0.00 | 22.93 | 0.20 | 31.00 | 0.00 | 0 / 0 / 0 |
| oh_bt | 30.57 | 0.00 | 9.80 | 0.83 | 31.00 | 0.00 | 0 / 0 / 0 |
| pm_z | 13.76 | 0.71 | 31.00 | 0.00 | 31.00 | 0.00 | 0 / 0 / 0 |
| **pm_bt** | **0.00** | **1.00** | **7.53** | **0.93** | **2.06** | **1.00** | **1.00** / 0.03 / 0 |
| maj_oh_z | 31.00 | 0.00 | 31.00 | 0.00 | 31.00 | 0.00 | 0 / 0 / 0 |
| maj_oh_bt | 30.81 | 0.00 | 22.27 | 0.17 | 17.91 | 0.35 | 0 / 0 / 0 |

Mean score std across the pool (control): 0.41 / 1.05 / 0.26. The control's mean gap to the majority best is 2.2 / 6.3 / 1.5, i.e. **5-6 pool SDs**. That is far outside what "one draw against the minimum of 31 exchangeable draws" produces. Under exchangeability the token's expected rank would be ~15.5 and it would beat the mean about half the time.

**Reading.**
1. **F2/F3.** The native token is always last, and a token of the MAJORITY class built the same way is also always last. The construction is being scored, not the class. The zero tail was the brief's hypothesis. It is **one** of two off-manifold features: the unit one-hot head is the other. On seed 11 the head dominates (pm_z, which keeps the zeros, climbs to rank 13.8; oh_bt, which keeps the one-hot, stays at 30.6). On seed 23 the tail dominates (oh_bt 9.8, pm_z 31). On seed 37 both are needed (only pm_bt escapes).
2. **"Sampled continuation" alone does not rescue.** The brief's intervention (continuations = held / sampled) is `hold` / `sampled`. `sampled` (one-hot head + a real tail) stays at rank 31 / 22.9 / 31. `hold` is seed-dependent (F7). The design record's INT-ACT candidate builder keeps "the first step is the exact one-hot e_c" with sampled continuations (`action_space_proposals_design_20260925.md` sec 2.1 step 1, sec 2.3 row 5 "sidestepped"). On this evidence that design **only half-sidesteps** the problem: the one-hot head is itself off-manifold, 5-7x the decoder's scale, and on seeds 11 and 37 it alone keeps a class-c candidate at the bottom. Owner: the INT-ACT design record (W1 build).
3. **F5.** When class c is offered on the decoder's manifold, E3 ranks it at or near the top: pm_bt is rank 0 on seed 11 (it beats the best majority candidate at every state, head-to-head against the same tail), 7.5 on seed 23 and 2.1 on seed 37. E3 does **not** reject class-c first actions on content in this regime.
4. **F6 (native consumer, D2).** Holding the token's class moves native E3 selection of that class from ~1/30 to 9/30 (seed 23) and from 1/34 to 13/34 (seed 37). On seed 11 there is no effect, consistent with F7.
5. **F7.** E3's preference among off-manifold constructions flips sign across seeds (hold: last on seed 11, first on 23 and 37). A hand-built candidate's E3 score therefore measures how E2 extrapolates off-manifold action inputs, not what the class is worth. That caution applies to every scaffold that uses `_build_action_class_scaffold_candidates` (SP-CEM floor, the diagnostic scaffold, the R5b scaffold).

**Limits.**
- Toy dims (16, not the deployed 32).
- 20 warmup episodes (1061's undertraining caveat still applies).
- Bare `e3.select` path only (Worker C showed that path matches the full agent path in this regime; not re-checked here).
- One regime (1061 intact arm).
- No usefulness oracle: pm_bt winning says E3 *would* take class c. It does not say class c is *better* in the ecology.
- Selection is multinomial and uncommitted, so "selected" rates are noisy at n = 21-34 states.
- Domain D2 (the native E3 ranking and its sampled selection move under intervention). **Not D3.**

## 3. Worker C's order-statistic conclusion, re-read

Worker C, `monostrategy_type_a_vs_b_discrimination_20260924.md` sec 2.3 readings 3-5 and the Type-A verdict, taken claim by claim:

| Worker C statement | status after this check | domain |
|---|---|---|
| "A token candidate never beats the best of the ~31 majority candidates (0/40 on 3/3 seeds)" | **holds.** 0/85 token states at `1a61800` | D1 |
| "...even though it beats the majority's MEAN score at 10-35% of states" | **does not hold for the tokens.** Native tokens beat the majority mean at 0/85 states. Plausible reconciliation, **not verified**: Worker C's probe did not read `metadata.source`, so its "off-class" set mixed tokens with native minority CEM samples. Here such native minorities occur at 35/120 states, and those may be what beat the mean. The commit (`00210b5` vs `1a61800`) and the per-state random walk also differ, so the two runs do not map state-for-state | D1 |
| "That is an order-statistic effect of the imbalance ... under roughly exchangeable scores" | **refuted for the tokens.** The token is last (rank 31.00), 5-6 pool SDs behind the best, not an exchangeable draw. A majority-class token built the same way is also last. The loss is **construction-driven** (off-manifold one-hot head + zero tail). The order-statistic reading may still apply to the native minority candidates, which this probe did not score | D2 |
| "The only alternatives are the SP-CEM floor's tokens" | **partly stale at `1a61800`.** 35/120 probe states had a native (non-token) minority class. For the 85 token states it holds | D1 |
| "E3 is not shown to reject the alternative on content" | **holds, and is strengthened.** On-manifold class-c versions (pm_bt) rank 0 / 7.5 / 2.1 | D2 |
| "The imbalance alone produces the monostrategy" | **does not hold as stated.** Two causes stack: (i) the CEM proposes one class (Type A at generation, unchanged), and (ii) the floor's rescue candidate is constructed so that E3 can never pick it by score. Rebalancing with more one-hot/zero-tail tokens (or a per-class quota filled by them) would **not** rescue selection. The rescue must be on-manifold | D2 |
| Verdict "Type A at generation; link is pool class balance and state-conditioning of the proposal, not E3 and not commitment" | **holds in direction, needs a clause.** The SP-CEM floor's "pool support 2.0 classes" is doubly nominal: the second class is present but unselectable by construction. P3 ("candidate generation non-degenerate: nominal yes, effective no") should cite this mechanism as well as the imbalance | D2 |

**What this changes downstream.**
1. Any record that counts SP-CEM floor support (pool classes = 2.0) as available alternatives. Worker C's P3 row, and the V3-EXQ-567 PASS metric `selected_action_entropy`, count classes present, not classes that can win by score.
2. The INT-ACT design (sec 2.2 point 2 above): its one-hot head is the same off-manifold construction.
3. Every experiment that reads the diagnostic `use_action_class_scaffold_candidates` scaffold's E3 scores as content: F7 says those scores are not content.

**Options for the owners** (not decided here; changing default behaviour is `/governance`'s call, per the design record):
- (a) Build the SP-CEM floor token from a real candidate with only its t=0 argmax swapped (the `pm_bt` construction, on the decoder's manifold).
- (b) Build it from a CEM re-sample conditioned on class c.
- (c) Keep the construction, but exclude synthetic candidates from E3 score-based selection claims and report them separately.

**Next single action:** hand F2/F3/F5 to the repertoire / ARC-065 owner via the governance flag below. The cheapest decisive follow-up is to repeat this probe at world_dim 32 with a trained agent (the 1061 full warmup) before any default change.

## 4. Governance flag

**GFLAG-0555** (claim ARC-065, `stale_note`), raised by `bt0925-spcem`. It carries F2/F3/F5 and points at Worker C's sec 2.3 mechanism reading. No `claims.yaml`, `ree_core`, or queue edits were made in this session.
