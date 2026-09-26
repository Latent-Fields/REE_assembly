# U4: sensed z_world near-collapse is the EMA's zero-initialized episode reset, not a data-driven event; low PR at alpha_world 0.3 is a separate, only-partly-overlapping effect

- **Status: MEASURED, 5 seeds x 3 alpha_world values (0.3/0.9/1.0), untrained agent, native policy. Verdict: RESET-EMA ARTEFACT for the per-tick spike; PARTIAL for the low-PR finding.** Session `bt0926-u4` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-zworld-near-collapse-rootcause`. Written 2026-09-26.
- **Question being closed:** U4 in `w3_step1_spike_attribution_20260925.md` sec 5 -- why the sensed z_world occasionally near-collapses (single-tick `||z_world||` at the 0-1st percentile), and why w6a found the untrained sensed z_world "already effectively one-dimensional" (PR 1.24-1.34) at alpha_world 0.3.
- **Code:** `ree-v3` `origin/main` at `e72e9630008a2218e9d22b99ff9f87d32a29837f`, detached throwaway worktree `.scratch/breakthrough-20260924/u4/ree-v3-wt`. Read-only, no `ree_core` edits.
- **Evidence domain: D1** for the norm/PR measurements (the quantities are measured and decoded from a live rollout). The reset-ratio identity (sec 3) is additionally **D0-provable from the code alone** (a pure algebraic consequence of `init_state`'s zero z_world + the EMA blend) and is confirmed to floating-point precision by measurement, not merely asserted.

## 1. Premises re-measured

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | "native policy episodes" (brief) means the agent's OWN action selection, not a scripted/uniform-random driver (contrast with `w6a_member_readout.py`'s uniform-random `drive()`) | Used `REEAgent.act_with_split_obs` (full E1 prior + E3 candidate generation + selection) per tick; confirmed it internally calls `sense()` exactly once per tick (`agent.py:5993` `world_obs_encoder`, `:6061` `latent_stack.encode`) and stores the resulting `LatentState` at `self._current_latent` (`agent.py:6694`, `.detach()`-ed) -- read directly, with NO second `sense()` call (which would double-advance the stateful EMA and corrupt the trajectory). | holds; `_current_latent.z_world_raw` survives `.detach()` (`ree_core/latent/stack.py:796` `LatentState.detach()`) so both the pre- and post-EMA values are available from one call per tick. |
| P2 | w6a's "untrained sensed z_world is already effectively one-dimensional (PR 1.24-1.34)" (`w6a_world_encoder_member_build_20260925.md` sec 4) was measured under a uniform-random policy over 1200 held-out steps, single-seed PR | Reproduced independently here under the AGENT'S OWN native policy (a structurally different driver), per-seed, at alpha_world=0.3: PR 1.129-1.668 across seeds 106-110 (sec 4). | **holds, and independently corroborated** under a different policy -- the low PR at alpha 0.3 is not an artefact of the uniform-random driver. |
| P3 | SD-008 (`config.py:78-91`, `:153-157`) attributes the >=0.9 requirement to "EMA double-smoothing suppresses event responses" -- a claim about event-driven variance, not stated as a claim about single-tick collapse spikes or about overall PR | Re-read at `ree_core/utils/config.py:83-91` (warning text) and `:153-157` (field comment): the text is scoped to *event responsiveness*, and does not mention episode-reset or PR. This record's finding is therefore additive detail, not a restatement or a contradiction. | **holds; no governance_flag needed** (nothing here contradicts SD-008 -- it corroborates and sharpens the mechanism for one of the two symptoms SD-008's remedy already covers). |

## 2. Method

- **Env:** `CausalGridWorldV2(size=8, num_hazards=3, num_resources=2, hazard_harm=0.5, seed=...)`, matching `w6a_member_readout.py`'s construction.
- **Agent:** `REEConfig.from_dims(..., self_dim=32, world_dim=32, alpha_world=<0.3|0.9|1.0>)` (deployed dims, `ree_core/utils/config.py:140-141` confirms 32/32 is also the class default), `REEAgent(cfg)` fresh (no waking trainer -- the untrained substrate w6a's own comparison used, `waking_trainer_enabled` defaults False). Per seed x alpha: `torch.manual_seed(seed)`, `np.random.seed(seed)` before construction (so the 5 seeds are 5 different random weight draws, not 5 replays of one network).
- **Drive:** 8 episodes x up to 40 ticks per seed (env resets on `done`), tick sequence = `agent.act_with_split_obs(obs_body, obs_world)` (native E1+E3 selection) -> read `agent._current_latent` (no extra `sense()` call) -> `env.step(a)`.
- **Per tick recorded:** `||z_world||` (post-EMA, `LatentState.z_world`), `||z_world_raw||` (pre-EMA, pre-SD-007-reafference-correction, captured at `ree_core/latent/stack.py:1524` before the EMA blend at `:1675` -- alpha-independent by construction, since the reafference predictor's own history input is `prev_state.z_world_raw`, itself pre-EMA, so the raw path never depends on `alpha_world` at all), the tick's environment TRIGGER, and the action class.
- **Trigger labelling** (from the transition INTO this tick): `reset` (tick 0 of an episode, `prev_state = init_state()` -> `z_world=0` zero vector, `ree_core/latent/stack.py:1278` + `:1416-1417`); else from the PRECEDING step's `harm_signal` (env contract: "negative = harm, positive = benefit", `causal_grid_world.py:2482`) and position delta (`env.get_agent_position()`, `:5476`): `hazard` (harm_signal<0), `benefit` (harm_signal>0), `wallpush` (position unchanged, action != the canonical stay class `CAUSAL_GRID_WORLD_STAY_ACTION_CLASS`), `noop` (position unchanged, action == stay class -- none observed here, untrained policy essentially never selects "stay"), `move` (normal transition -- none reached the collapse bucket at any alpha, so not tabulated below).
- **Collapse bucket:** ticks at or below the 1st percentile of `||z_world||`, pooled across all 5 seeds, per alpha (matching the brief's "0-1st percentile" framing).
- **PR:** participation ratio (`(sum eig)^2 / sum(eig^2)` of the mean-centred covariance), computed PER SEED (not pooled -- pooling across seeds mixes 5 differently-initialized random encoders and inflates PR by adding genuine between-seed direction diversity; pooled PR is reported too, for transparency, but is not the comparison point against w6a's per-seed figure).
- Script: `probes/u4/u4_zworld_collapse_probe.py` (committed alongside this record). Raw per-alpha JSON (summary + all rows incl. raw 32-d vectors): `probes/u4/results/u4_alpha_{0p3,0p9,1p0}.json`.

## 3. Results: the near-collapse spike is the reset-zero-EMA identity, near-exactly

| alpha | n ticks (5 seeds) | n reset ticks | median &#124;&#124;z_world&#124;&#124; | p1 (1st pctile) | p1/median | reset_ratio mean (=&#124;&#124;z_world&#124;&#124;/&#124;&#124;z_world_raw&#124;&#124; at t=0) | max abs err vs alpha |
|---|---|---|---|---|---|---|---|
| 0.3 | 875 | 40 | 0.4519 | 0.1346 | 0.298 | 0.30000 | 4.1e-08 |
| 0.9 | 938 | 40 | 0.4823 | 0.4045 | 0.839 | 0.90000 | 1.0e-07 |
| 1.0 | 956 | 40 | 0.4846 | 0.4326 | 0.893 | 1.00000 | 0.0 |

**The reset-ratio identity holds to floating-point precision at every alpha, on every one of the 120 reset ticks measured (40 x 3 alphas):** `||z_world(t=0)|| = alpha_world x ||z_world_raw(t=0)||`, because `prev_state.z_world = 0` at episode start (`init_state`, `stack.py:1278`) and reafference correction is skipped at `t=0` (`stack.py:1528`, `(prev_state.timestamp or 0) > 0` is False), so the EMA blend at `stack.py:1675` degenerates to `alpha_world * z_world_raw + (1-alpha_world) * 0`. This is a D0-derivable fact confirmed empirically, not a new mechanism inferred from correlation.

**Trigger composition of the 0-1st-percentile collapse bucket, per alpha:**

| alpha | n collapse | reset | hazard | wallpush | benefit | reset enrichment (collapse-rate / base-rate) |
|---|---|---|---|---|---|---|
| 0.3 | 9 | 9 (100%) | 0 | 0 | 0 | **21.9x** |
| 0.9 | 10 | 10 (100%) | 0 | 0 | 0 | **23.5x** |
| 1.0 | 10 | 1 (10%) | 6 (60%) | 3 (30%) | 0 | 2.4x |

At the DEPLOYED default (alpha_world=0.3) and at 0.9, the near-collapse bucket is **100% episode-reset ticks** -- not hazard proximity, not resource pickup, not wall-pushes, and not "the EMA's first few ticks" as a broader window (no non-t=0 tick entered the bucket at either alpha). Removing the EMA (alpha=1.0) makes the bucket revert to the ordinary low tail of the raw encoder's own output (mostly hazard/wallpush ticks, matching their ~27%/68% base rates reasonably well, enrichment only 2.4x for reset) -- confirming the EMA-from-zero mechanism is causal, not a confound: turn it off and the reset-domination of the collapse bucket collapses too.

**The raw (pre-EMA) encode at the collapsing reset ticks is itself unremarkable.** Mean percentile of `||z_world_raw||` (within the OVERALL raw-norm distribution) at the collapse ticks: 0.101 (alpha 0.3), 0.111 (alpha 0.9), 0.006 (alpha 1.0, tautological since raw==post-EMA there). At 0.3 and 0.9 the raw encode sits around the 10th percentile -- ordinary, not extreme -- while the POST-EMA value for that same tick is forced into the 0-1st percentile purely by the 70%/10% collapse toward the hard-zero prior state. **The spike is manufactured by the EMA's episode-boundary condition, not present in what the encoder itself produced.**

## 4. Results: the low PR at alpha 0.3 is only PARTLY the same mechanism

| alpha | seed | PR incl. reset ticks | PR excl. reset ticks |
|---|---|---|---|
| 0.3 | 106 | 1.341 | 1.688 |
| 0.3 | 107 | 1.276 | 1.573 |
| 0.3 | 108 | 1.449 | 1.955 |
| 0.3 | 109 | 1.668 | 2.377 |
| 0.3 | 110 | 1.129 | 1.242 |
| 0.9 | 106 | 3.981 | 3.515 |
| 0.9 | 107 | 4.677 | 4.020 |
| 0.9 | 108 | 5.006 | 4.639 |
| 0.9 | 109 | 6.184 | 5.870 |
| 0.9 | 110 | 3.809 | 3.169 |
| 1.0 | 106 | 3.494 | 3.298 |
| 1.0 | 107 | 4.487 | 4.101 |
| 1.0 | 108 | 4.905 | 4.742 |
| 1.0 | 109 | 6.144 | 6.055 |
| 1.0 | 110 | 3.015 | 2.906 |

Per-seed PR at alpha 0.3 (1.13-1.67, incl. reset) independently corroborates w6a's uniform-random-policy figure (1.24-1.34) under a structurally different (native-policy) driver -- P2 holds. Pooled-across-seed PR (3.28 at both 0.3 and 0.9 pooled) is reported in the raw JSON but is **not** a like-for-like comparison to w6a's per-seed number: pooling 5 differently-initialized random encoders adds genuine between-seed direction diversity that inflates PR regardless of alpha, and both alpha values land at ~3.28-3.49 pooled despite being 3-4x apart per-seed -- the pooled figure is dominated by cross-seed variation, not by alpha.

**Removing the 40 reset ticks entirely does not close the PR gap.** At alpha 0.3, excluding reset ticks RAISES per-seed PR modestly (1.24-2.38, still far below the 2.9-6.1 range at alpha 0.9/1.0 excluding the same tick type). So the reset-EMA artefact from sec 3 explains only a minority of the low-PR effect: even on ordinary (non-reset) ticks, alpha 0.3's heavier smoothing (effective memory ~1/alpha ~ 3.3 ticks vs ~1.1 ticks at alpha 0.9) suppresses the untrained encoder's per-tick (event-driven) variance far more than whatever slow/persistent component survives, and that surviving component occupies few effective dimensions for a random, untrained projection. This is the general mechanism SD-008's own comment already names ("EMA double-smoothing suppresses event responses") -- this record's contribution is confirming that the SAME general low-alpha smoothing effect, not only the reset artefact, is the dominant driver of the overall PR collapse, and separating that from the distinct, exactly-quantified reset-tick spike mechanism in sec 3.

## 5. Verdict

- **Per-tick near-collapse spike (0-1st percentile &#124;&#124;z_world&#124;&#124;), at the deployed alpha_world=0.3: RESET-EMA ARTEFACT, exactly mechanised, not a data-driven event.** 100% of collapse ticks are episode-reset ticks (21.9x enrichment); the identity `||z_world(t=0)|| = alpha_world * ||z_world_raw(t=0)||` holds to <1e-7 absolute error; the raw pre-EMA encode at those ticks is unremarkable (~10th percentile); turning the EMA off (alpha=1.0) makes the collapse bucket revert to the genuine low tail of the raw encoder, no longer reset-dominated. Domain: D0 (algebraic) confirmed by D1 (measured).
- **Low PR (~1-D) at alpha_world 0.3: PARTIALLY the same mechanism, MOSTLY a separate general-smoothing effect.** Excluding reset ticks only mildly raises PR and the alpha-0.3 vs alpha-0.9/1.0 gap (1.2-2.4 vs 2.9-6.1) survives their removal. Domain: D1.
- **Fix, by symptom:** the reset spike is removed (both alphas: 0.9 and 1.0) or shrunk to the encoder's ordinary distribution (alpha>=0.9, where the shrink factor is 0.9 not 0.3) simply by raising alpha_world -- no new mechanism is needed beyond what SD-008 already prescribes. The low-PR effect needs the SAME lever (alpha>=0.9, per-seed PR 3.0-6.2 vs 1.1-1.7) for a partial fix, and w6a's own W6a training (PR 11.3-15.1 at alpha 0.3) for a much larger one -- training the encoder, not just raising alpha, is what actually breaks the untrained low-dimensionality, consistent with w6a sec 4's own reading.

## 6. Route

This corroborates and sharpens **SD-008** (`claims.yaml` id SD-008, status stable, `alpha_world >= 0.9` for event responsiveness) -- it adds a distinct, exactly-quantified sub-mechanism (the episode-reset zero-init EMA spike) to the phenomenon SD-008's remedy already covers, and separates it from the (mostly-independent) general-smoothing low-PR effect that w6a's own build already addresses by training. Nothing here contradicts a registered claim, so **no `governance_flag.py` raised** (brief: at most one, only if a registry note is contradicted). No `claims.yaml` edit, no queue, no plan edit, per brief.

## 7. Not done

- **Why the untrained encoder's "surviving slow component" is itself low-dimensional** (sec 4's residual, non-reset PR gap) is stated, not further decomposed -- would need e.g. a matched-window moving-average control (average the last `k=round(1/alpha)` raw ticks with EQUAL weight, vs the true exponential-weight EMA) to isolate whether the shape of the smoothing kernel matters or only its effective memory length.
- No consumer-mediated (D2/D3) check of whether a downstream module (E1, E3) actually reacts differently to a reset-tick spike vs an ordinary tick -- out of scope per the brief (probe only).
- `noop` (deliberate "stay") ticks were never observed in this native-policy sample (the untrained E3 essentially never selects "stay"); the wallpush/noop distinction in the tick-type table is therefore unexercised here.
