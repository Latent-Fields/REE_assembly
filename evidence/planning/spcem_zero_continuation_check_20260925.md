# SP-CEM zero-continuation check (2026-09-25)

Session `bt0925-spcem`, chip `chip-20260925-spcem-zero-continuation-check`, orchestrator `orchestrate-20260924-breakthrough`.
Code refs are file:line at **ree-v3 origin/main `1a61800`** (detached throwaway worktree).

**Status: D0 section complete; D1/D2 probe IN PROGRESS (this record is committed early and amended).**

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

(in progress)

## 3. Worker C's order-statistic conclusion, re-read

(in progress)
