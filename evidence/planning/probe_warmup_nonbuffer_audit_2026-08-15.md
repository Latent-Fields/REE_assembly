# probe_warmup / maturation_curriculum non-buffer state audit

**Status: COMPLETE. Headline: `measure_action_mass` is NOT non-destructive, the mechanism
is eval-rollout data leaking into the training buffer, and at V3-EXQ-784's real scale it
flips the saturation verdict on 2 of 6 comparable cells. This is an experimental-validity
defect on an already-executed, PASSED run -- raised via `governance_flag.py`. The
warm-start CACHE the chip was written about is not implicated: no executed run ever took
a cache hit.**

Chip: `chip-20260815-probewarmup-nonbuffer-gap`. Session:
`metaworker-chip-20260815-probewarmup-nonbuffer-gap`. Box: `ree-cloud-5`.
Substrate audited: `ree-v3` at the worktree's `main` (see commit trailer).

Motivating finding (from the chip brief): the preservation Increment-2 de-risking spike
(`ree-v3/tests/contracts/test_preservation_midlife_spike.py`, 2026-08-15) established that
`nn.Module.state_dict()` silently drops every non-parametric store hanging off `REEAgent`,
and enumerated ~10 agent-side stores. The chip asked whether
`experiments/_lib/probe_warmup.py` -- which does save/restore of exactly this kind on a
live experiment path -- carries the same hazard beyond the `agent.e3` scalars its
`_E3_NONBUFFER_STATE` names.

---

## Answer, in order of what a reader needs

### 1. The cache-HIT-vs-MISS framing does not reach any executed run

`warm_agent()` -- the function that `torch.save`s `agent.state_dict()` +
`e3_nonbuffer` into a warm-start cache blob and reloads it later -- has **exactly two
call sites in the repo**, and neither is an executed experiment:

| caller | status |
|---|---|
| `experiments/_scratch/sd075_warmup_rescue_spike.py` | scratch spike, never queued, no manifest |
| (nothing else) | -- |

`experiments/v3_exq_784_sd074_probe_warmup_desaturation_budget_sweep.py` -- the ONE
executed consumer of this module (run `v3_exq_784_..._20260718T222045Z_v3`, PASS,
2.0 h on `ree-worker-1`) -- imports `measure_action_mass`, `reapply_candidate_capture`,
`saturation_regime`, `WarmupRecipe` and `D_SAT_*`. It does **not** import `warm_agent`,
and it does not use the cache at all: it trains ONE agent incrementally and reads at
each budget checkpoint (`incremental_warmup_shared_agent_across_budget_checkpoints` is
stamped on every cell's `arm_fingerprint.reuse_ineligible_reasons`).

So **there is no cache-HIT/cache-MISS divergence on any run in the evidence record**,
because no run on the record ever took a cache hit.

### 2. The live exposure is a different, sharper one: `measure_action_mass` is not non-destructive

`measure_action_mass()` documents itself as "NON-DESTRUCTIVE, IN BOTH DIRECTIONS THAT
MATTER ... the caller gets back bit-identically the agent it passed in", and restores
`agent.state_dict()` plus the four declared `_E3_NONBUFFER_STATE` scalars.

Measured on `ree-cloud-5` against 784's exact config
(`REEConfig.from_dims` + `use_control_vector_logging=True`,
`hippocampal.use_action_class_scaffold_candidates=True`, both regulators OFF):

* **state_dict round-trip is clean** -- 0 of 200 tensors differ after a read.
* **21 non-`state_dict` attributes are left changed** by a single 40-step read
  (of 421 tracked plain-Python attributes across the agent's module tree).
* **17 of those survive `agent.reset()`**, i.e. can reach the next read or the next
  training leg. `agent.reset()` is called at every episode start by
  `_lib/sample_driven_rollout.run_cell_until_samples`, which is why the
  episode-scoped ones are harmless.

### 3. The channel that actually matters: eval data leaks into the training set

The load-bearing survivors are the agent's experience buffers, not the E3 scalars:

```
agent._self_experience_buffer     114 -> 154 entries   (a 40-step read)
agent._world_experience_buffer    114 -> 154
agent._e2_transition_buffer       111 -> 147
agent.e3.residue_field._harm_history  27 -> 73
agent._z_goal_writer_calls        114 -> 154
```

`experiments/_lib/goal_pipeline_tier1.warmup_train` calls
`agent.compute_prediction_loss()` on every training tick, and that function
(`ree_core/agent.py:9970`) samples a **random window** out of
`_world_experience_buffer` / `_self_experience_buffer`:

```python
buf_len   = len(self._world_experience_buffer)
start_idx = int(torch.randint(0, max(1, buf_len - 1), (1,)).item())
```

So a probe read (a) grows the buffer, changing the sampled index range, and (b) puts
**eval-rollout observations into the training pool**. Both buffers are capped at 1000
entries (`ree_core/agent.py:5319`, `del buf[:-1000]`).

At 784's realised scale this is not marginal. Measured probe reads in the replicated
ladder are **1081 and 1401 env steps** (seeds 11 and 17, budget 0), against training
legs of 400 / 600 / 1500 steps (4 / 6 / 15 episodes x 100 steps). A read of >1000 steps
**completely displaces the buffer**: after the budget-0 read, 100% of the E1 training
pool is probe-read data, and the following 4-episode training leg only dilutes it back
to ~60% read-derived.

Confirmed causally at small scale (single agent, restored between conditions, RNG pinned
at every stage boundary, determinism control passing exactly): after
`read -> train 2 episodes -> read`, the residue-carrying and fully-restored arms
diverge in **16 of 200 weight tensors** (all `e1.*`, chiefly `e1.context_memory.*`),
max |dw| = 1.49e-3. The effect on the dependent variable at that scale was
2.8e-8 -- negligible. Whether it stays negligible at 784's real scale is what the
full ladder A/B answers; see section 5.

### 4. `_E3_NONBUFFER_STATE` is itself partly wrong

Three separate defects in the declared list, independent of the buffer channel above:

* `_last_error_var` **does not exist anywhere in `ree_core`** (grep: zero hits). It is a
  dead entry; the docstring's "SD-069 instantaneous-PE source, if present" describes
  `e3._last_instantaneous_pe`, which is the real attribute and is **not** captured.
* `e3._volatility_estimate` (Q-007 LC-NE tonic volatility, `e3_selector.py:340`) is
  live-mutated by a read and is **not** captured.
* `e3._fp_alt_world_endpoint` / `_fp_chosen_world_endpoint`,
  `e3._persistent_committed_trajectory` and `e3._last_selected_trajectory` are likewise
  mutated and uncaptured.

**Under 784's config all four are inert**, which is why the small-scale DV effect was
~1e-8 rather than large:

* `volatility_estimate` is read only at `agent.py:4289`, gated on
  `config.latent.volatility_signal_dim > 0` -- default `0` (`config.py:230`).
* `last_instantaneous_pe` is read only when
  `config.phasic_burst_signal_source == "instantaneous_pe"` -- default
  `"running_variance"` (`config.py:3674`) -- and `agent.phasic_burst` is `None` under
  this config anyway.

They are therefore **latent** defects: correct today by accident of config, wrong for
any future consumer that turns either knob on. The phantom `_last_error_var` should be
replaced by `_last_instantaneous_pe` regardless, since it silently captures nothing.

### 5. Ladder A/B at 784's real scale -- the verdict flips

Replicated 784's per-seed ladder at its real configuration (budgets `[0, 4, 10, 25]`,
`train_steps_per_episode=100`, `read_steps_per_episode=300`, `probe_selects=150`,
`probe_max_env_steps=4000`, env `size=8 / hazards=2 / resources=3`, both regulators OFF),
twice per seed:

* **arm A "as-is"** -- exactly what 784 does: each read leaves its residue behind.
* **arm B "restored"** -- identical, except the agent's full non-`state_dict` attribute
  tree is captured before each read and restored after it.

RNG is re-pinned to a fixed derived seed at every stage boundary (before each training
leg and before each read), so both arms see identical randomness and the ONLY difference
is the agent state each stage starts from. Two seeds, ~100 min each on `ree-cloud-5`.

| seed | budget | A as-is | B restored | delta | A regime | B regime |
|---|---|---|---|---|---|---|
| 11 | 0  | 0.998871 | 0.998871 | **0** (control) | ceiling | ceiling |
| 11 | 4  | 0.902603 | 0.963654 | 0.061051 | headroom | **ceiling** |
| 11 | 10 | 0.892603 | 0.903844 | 0.011241 | headroom | headroom |
| 11 | 25 | 0.924767 | 0.889263 | 0.035504 | headroom | headroom |
| 17 | 0  | 0.991775 | 0.991775 | **0** (control) | ceiling | ceiling |
| 17 | 4  | 0.668805 | 0.814611 | 0.145806 | headroom | headroom |
| 17 | 10 | 0.880680 | 0.968924 | 0.088244 | headroom | **ceiling** |
| 17 | 25 | 0.931594 | 0.824576 | 0.107018 | headroom | headroom |

**The budget-0 rows are the harness control and they are bit-identical**, as they must be:
budget 0 has no preceding read, so there is no residue for the two arms to differ on. That
they agree to all 16 digits is what licenses reading the other six rows as a real effect
rather than as ladder-level nondeterminism.

**Every one of the six post-first-read cells differs**, by 0.011 to 0.146 on a `[0,1]`
dependent variable whose decision thresholds are 0.05 and 0.95. **Two of the six flip the
saturation regime** (seed 11 at budget 4; seed 17 at budget 10).

That matters because 784's headline is exactly a count of regime classifications:
`informative_yield` = fraction of seeds in `headroom`, gated at `> 0.5` and compared
against the V3-EXQ-777a baseline of 0.286. A cell that flips `headroom` <-> `ceiling`
moves that number directly, and here the cell-level flip rate is 2/6.

**The perturbation is not a consistent bias, which makes it worse rather than better.**
Four cells move toward ceiling under restoration and two move away (seed 17 budget 25:
A 0.9316 vs B 0.8246, i.e. the as-is arm is the more saturated one). So this is
uncontrolled noise injected into the DV, not an offset that could be argued to cancel
across seeds.

**Scope of this claim, stated precisely.** This replication is not bit-identical to the
landed 784 run: 2 seeds rather than 14, a pinned env seed where 784 used OS entropy at
construction, and RNG re-pinned at stage boundaries (which 784 does not do -- it is what
makes the A/B a controlled comparison). What it establishes is **sensitivity**: the
residue can and does change 784's per-cell verdict at its real operating scale. It does
**not** establish that 784's reported `informative_yield` is wrong by any particular
amount. Establishing that requires re-running 784 itself with the restore in place, which
is the recommendation below.

---

## Recommendation

1. **Governance:** treat V3-EXQ-784's `informative_yield` / `target_met` as
   **provisional**. The run is not invalid on its face -- the saturation phenomenon it
   measures is real and the budget-0 control cells are uncontaminated by construction --
   but every post-budget-0 cell was read from an agent whose E1 training pool had been
   displaced by probe-read data, and 2 of 6 replicated cells changed verdict. Raised as a
   governance flag rather than adjudicated here.

2. **Fix `measure_action_mass`, and do NOT do it by extending `_E3_NONBUFFER_STATE`.**
   Hand-listing attribute names is precisely how the E3-only version came to be partial,
   and the load-bearing state is not in E3 at all -- it is the agent-level experience
   buffers. The fix should be the census pattern from S2 of
   `tests/contracts/test_preservation_midlife_spike.py`: partition the attribute surface
   into restored / config-derived / telemetry and pin it, so a NEW attribute fails the
   contract until someone classifies it.

3. **A partial fix is worse than none here, so land it as one gated change.** Replacing
   the phantom `_last_error_var` with the real `_last_instantaneous_pe` and adding
   `_volatility_estimate` is a two-line change that fixes nothing measurable (both are
   inert under every config that uses this module today) while making the docstring's
   "non-destructive" claim look freshly audited. Whatever lands must address the buffer
   channel or it should not land at all.

4. **This is executable-code plane** (`experiments/_lib/` is pulled by the fleet), so any
   change is gated on the contract suite per CLAUDE.md "Running the test suite". Not
   attempted from this headless chip.

5. **`maturation_curriculum` needs no change** -- see the negative result below.

---

## Which of the chip's 10 stores are actually live

Constructed a `REEAgent` under 784's exact config and inspected:

| store the chip named | under 784's config |
|---|---|
| `e3` | **LIVE** (`E3TrajectorySelector`) |
| `serotonin` | **LIVE** (`SerotoninModule`) -- reset every episode by `agent.reset()` |
| `residue_field` | **LIVE** (`ResidueField`); `_harm_history` grows across the read |
| `super_ordinal_goal_memory` | `None` -- not constructed |
| `goal_state` | `None` -- not constructed |
| `gated_policy` | `None` -- not constructed |
| `incentive_bank` | attribute does not exist on `REEAgent` |
| `visitation_counter` | not on the agent; lives at `agent.hippocampal.visitation_counter` (**LIVE**; `_next_idx` advances during a read) |
| `anchor_set` | attribute does not exist on `REEAgent` |
| `staleness_accumulator` | attribute does not exist on `REEAgent` |
| `ghost_goal_bank` | attribute does not exist on `REEAgent` |

So only **3 of the 10** named stores are exposed on this path, plus one
(`visitation_counter`) that is exposed at a different attribute path than the chip
assumed. The remaining 6 are excluded because they are not constructed under the
configs that use this module -- stated explicitly rather than silently, per the chip's
instruction.

The chip's implicit assumption that the store list is the right unit was too narrow in
a different direction, though: the census found **421** plain-Python attributes across
the agent's module tree, and the ones that actually carry a probe read forward are
**agent-level** buffers (`_self_experience_buffer`, `_world_experience_buffer`,
`_e2_transition_buffer`), which are on none of the ~10-store lists.

---

## `maturation_curriculum`: same shape, NO exposure

`experiments/_lib/baselines/maturation_curriculum.py` `mature_and_collect_world` /
`mature_and_collect_harm` do `torch.save`/`load` of `agent.state_dict()` (resp.
`harm_encoder_state`) with **no non-buffer capture at all** -- a strictly wider gap than
`probe_warmup`'s. It is nevertheless **not exposed**, for a structural reason:

* The **dataset is cached alongside the weights**, so `collect_world_dataset` (the only
  thing on that path that calls `agent.sense()` / `agent.reset()`) never runs on a HIT.
  A HIT agent's non-buffer state is therefore fresh-construction; a MISS agent's is
  post-warmup+collect. They genuinely differ.
* But every consumer touches only **parameters**:
  * `_e2_forward_r2(agent, data)` -> `agent.e2.world_forward(Zprev, A)` under
    `no_grad()`, on cached tensors. Pure parameter forward.
  * `_train_eval_head(...)` / `_train_dv_kfold(...)` -> re-initialises
    `agent.e3.harm_eval_head` / `benefit_eval_head` / `harm_eval_z_harm_head` from
    `fresh_head_inits` (captured **before** maturation, identically on both paths), with
    `torch.manual_seed(EVAL_TRAIN_SEED)` and a pinned split, then trains on cached
    tensors.

Consumers checked: `v3_exq_744a`, `v3_exq_746`, `v3_exq_746a`, `v3_exq_746b`,
`v3_exq_746c`. (`v3_exq_744` does **not** call the shared module -- it has its own
inline `_collect_frozen_dataset`; the grep hit was a docstring reference.)

No consumer reads any non-`state_dict` attribute of the returned agent, so the HIT/MISS
non-buffer difference cannot reach a reported number. **This is a complete negative
result: do not add a non-buffer capture to `maturation_curriculum` on the strength of
the `probe_warmup` finding.** If a future consumer starts stepping the returned agent
(`sense`/`select_action`/`step`) rather than only forwarding through its parameters,
that conclusion lapses and this file is the record of why.
