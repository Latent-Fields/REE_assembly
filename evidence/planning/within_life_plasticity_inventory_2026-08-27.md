# Within-Life Plasticity Inventory -- ree-v3 long-life / observational / Fishtank drivers

**Date:** 2026-08-27T20:05Z
**Session:** `determined-archimedes-f75804` (chip `chip-20260827-plasticity-inventory`)
**Audited tree:** `ree-v3` @ `9cfaf4a` (working tree clean for `ree_core/**` and every audited driver;
one untracked file, see §8.3). Every line number below is against that revision.
**Status:** audit artifact. **READ-ONLY on `ree-v3` -- nothing in this pass modified an experiment
script, a queue entry, or a config default.**

## 0. What this is, and what it is for

`GOV-CAPCONTRACT-1` (`REE_assembly/docs/claims/claims.yaml`, registered 2026-08-27 in `cbac6ceea6`)
requires every organism-level experiment to declare **which forms of change were permitted during
the run**. Its own notes make this inventory a precondition for its own implementation: without it
the `requires_plasticity` field has no vocabulary to declare against.

`ARC-135` (`claims.yaml:88337`) supplies the second vocabulary: "long life" is at least **four
separable continuities**, which can be held or broken independently. Referred to below as:

| id | continuity |
|----|------------|
| **C1** | cognitive / affective / mnemonic state |
| **C2** | parameter / plasticity |
| **C3** | body / homeostatic |
| **C4** | ecological / world |

This document answers, per driver and per state class: **can it change during a life, what in the
code decides that, and which continuity does it belong to.**

**Every cell is grounded in a `file:line` citation, or is written `UNDETERMINED` with a statement of
what was looked at.** An honest UNDETERMINED is a finding; a plausible guess is a defect, because
GOV-CAPCONTRACT-1 exists precisely because assumed capability produced uninterpretable nulls.

---

## 1. Driver set -- how it was chosen

Selected by a **functional** criterion, not by filename: a driver that runs a persistent agent over
an extended observation ("a life") in the Fishtank/CausalGridWorldV2 ecology. Enumerated by
(a) every file under `ree-v3/experiments/` referencing `_observational_run`, (b) every
`*_fishtank_*` / `*_showcase` driver that instantiates and runs an agent, and (c) the 929/933
sleep-entry lineage named in the routing chip. 19 drivers:

| # | driver | family | life phase |
|---|--------|--------|------------|
| 1 | `v3_exq_906_full_stack_observational_fishtank.py` | **906-orig** | curriculum -> `_observational_run` (8 x 500 steps) |
| 2 | `v3_exq_906a_full_stack_observational_fishtank.py` | **906-continuity** | curriculum -> continuous multi-segment |
| 3 | `v3_exq_906b_full_stack_observational_fishtank.py` | **906-continuity** (canonical impl) | curriculum -> continuous multi-segment |
| 4 | `v3_exq_906c_full_stack_observational_fishtank.py` | **906-continuity** (imports 906b) | as 906b |
| 5 | `v3_exq_909_sleep_dv_fishtank_multifiring.py` | 906b config, own loop | curriculum -> forced multi-fire sleep eval |
| 6 | `v3_exq_910b_mech489_orienting_decision_at_override_tick_retest.py` | **906-continuity** (monkeypatch wrapper) | as 906b |
| 7 | `v3_exq_911_ecology_enrichment_fishtank.py` | **906-continuity** (imports 906b) | as 906b |
| 8 | `v3_exq_912_uncensored_survival_fishtank.py` | **906-continuity** (imports 906b) | as 906b, 60 segments |
| 9 | `v3_exq_913_developmental_ecology_fishtank.py` | 906b config, own loop, sleep as ARM | curriculum -> continuous multi-segment |
| 10 | `v3_exq_920_uncensored_survival_single_life_fishtank.py` | **906-continuity** (imports 906b), `EVAL_EPISODES=1` | curriculum -> ONE continuous life |
| 11 | `v3_exq_929_sleep_gap9_within_life_trigger.py` | **gap9** | single continuous life, no curriculum |
| 12 | `v3_exq_933_sleep_gap9_need_arm.py` | **gap9** | single continuous life, no curriculum |
| 13 | `v3_exq_933a_sleep_gap9_entry_pressure_fix.py` | **gap9** | single continuous life, no curriculum |
| 14 | `v3_exq_665_curriculum_affective_fishtank_showcase.py` | 665-observational | curriculum -> eval showcase |
| 15 | `v3_exq_471_best_agent_fishtank_showcase.py` | **showcase** | `_warmup_train` -> `_eval_agent` |
| 16 | `v3_exq_524_reef_fishtank_showcase.py` | **showcase** | `_warmup_train` -> `_eval_agent` |
| 17 | `v3_exq_664_affective_fishtank_showcase.py` | **showcase** | `_warmup_train` -> `_eval_agent` |
| 18 | `v3_exq_916_relief_safety_fishtank_showcase.py` | **showcase** | `_warmup_train` -> `_eval_agent` |
| 19 | `v3_exq_916a_relief_safety_fishtank_showcase.py` | **showcase** | `_warmup_train` -> `_eval_agent` |

**Family grouping is proven by import, not asserted.** 906c/911/912/920 import `_make_config` and
`_observational_run` *verbatim* from 906b (`906c:138-148`, `911:161-171`, `912:193-201`,
`920:278-286`); 909 and 913 import `_make_config` and run their own loop (`909:165-172`,
`913:256-266`); 910b replaces `_fishtank906b._observational_run` with a telemetry-tapping wrapper
that calls the original (`910b:330-352`). Where a family shares one implementation, the cited line
is that implementation's -- that is what actually executes.

**Deliberately excluded:** `v3_exq_948_observation_interface_re_representation_probe.py`,
`v3_exq_939/939a` (MECH-303 vigilance), `v3_exq_921` -- these use fishtank-lineage *components* but
are short-horizon mechanism probes, not long-life drivers. `v3_exq_524a`, `v3_exq_471a`,
`v3_exq_475*`, `v3_exq_483*`, `v3_exq_490*`, `v3_exq_620/625*`, `v3_exq_786*`, `v3_exq_862*` mention
"fishtank" in prose only.

---

## 2. State-class vocabulary (the deliverable's primary output)

The chip's nine state classes, with the machine-usable slug each should carry in a
`requires_plasticity` declaration:

| class | slug | what it is |
|---|---|---|
| (a) | `parameters` | any `nn.Parameter` updated by an optimizer step |
| (b) | `policy_value` | an actor/critic policy or value head (MECH-457 `action_critic`) |
| (c) | `e1_representations` | E1 encoder/LSTM weights and their latent structure |
| (d) | `e2_action_conditional` | E2 world-forward / action-conditional structure (SD-056) |
| (e) | `context_memory` | `E1.ContextMemory.memory` slot contents |
| (f) | `hippocampal_buffers` | exploration buffer, anchor sets, per-stream V_s, staleness map |
| (g) | `residue_affective` | RBF residue field weights/centers, affective credit tables |
| (h) | `ema_control_state` | EMAs, accumulators, gates, counters, learned scalars |
| (i) | `offline_sleep_updates` | any change made by an SWS/REM cycle |

**This supersedes the six-mode `PLASTICITY_MODES` stub currently in
`ree-v3/experiments/_lib/capability_contract.py`**, which is a verbatim transcription of the claim
title and says of itself that it is "NOT the inventory". (Cited by symbol, not line: that file is
untracked and being actively written by a parallel session -- it grew from 1202 to 1266 lines during
this audit, so any line number here would be stale within the hour.) The mapping, so adoption is
unambiguous:

| stub mode | replace with |
|---|---|
| `parameters` | `parameters` (unchanged) |
| `policy_value` | `policy_value` (unchanged) |
| `e1_e2_representations` | **split** -> `e1_representations` + `e2_action_conditional` |
| `memory_state` | **split** -> `context_memory` + `hippocampal_buffers` |
| `residue_ema_state` | **split** -> `residue_affective` + `ema_control_state` |
| `offline_updates` | `offline_sleep_updates` (renamed; sleep is the only offline path in V3) |

The splits are not cosmetic. In every driver audited, `context_memory` and `hippocampal_buffers`
have **opposite** answers, and so do `residue_affective` and `ema_control_state`. A single
`memory_state` mode cannot express what these runs actually permit.

---

## 3. Substrate facts that hold across ALL 19 drivers

These are properties of `ree_core`, established once and cited once; the per-driver tables in §4
inherit them.

### 3.1 Two independent freeze mechanisms, not one

**(i) `torch.no_grad()`** around the per-step body. **(ii) `agent.eval()`** -- `nn.Module.training
== False`. All 19 drivers apply BOTH to the observed life. The second is routinely overlooked and
gates behaviour the first does not:

- `agent.py:4160` -- `if not self.training: return` disables the **SD-063 online E2-world-uncertainty
  head update** entirely.
- `agent.py:4258` -- `if not self.training: return` disables the **MECH-074d BLA attribution head**
  supervised step.
- `e1_deep.py:394` -- `if not self.training: return selection_scores.argmin()` **changes the
  ContextMemory write-address policy** from stochastic `gumbel_learned` to deterministic argmin.
  Eval mode is not merely "don't learn" here; it is a different addressing algorithm.
- `e1_deep.py:924` -- same for the SD-016 cue-slot tagger.

### 3.2 `torch.enable_grad()` appears NOWHERE in `ree_core/`, and `torch.is_grad_enabled()` nowhere in the tree

Tree-wide scan of `ree-v3` (excluding `__pycache__` and `.claude/worktrees/`): `enable_grad` occurs
in exactly **two** experiment scripts -- `v3_exq_140_mech094_hypothesis_tag_gate_pair.py:312` and
`v3_exq_211_mech153_arc042_supervised_labeling.py:280`, **neither a long-life driver** -- and in one
docstring, `experiments/_lib/ofc_head_cache.py:308`. `torch.is_grad_enabled()` and
`torch.set_grad_enabled()` occur **zero times anywhere**.

Consequence, and it is the load-bearing one: **no `ree_core` module re-enables gradient inside a
driver's `no_grad` block.** Modules that own their own optimizer (§3.3) are therefore inert there,
and nothing in the tree can observe or report that it happened.

### 3.3 Six `ree_core` modules own an optimizer and could in principle learn online

| module | optimizer | backward |
|---|---|---|
| `ree_core/amygdala/attribution_head.py` | `:392`, `:396` | `:530` |
| `ree_core/latent/cross_stream_binder.py` | `:163` | `:318` |
| `ree_core/pfc/e2_escape_affordance_linker.py` | `:387` | `:497` |
| `ree_core/pfc/trainable_escape_affordance_learner.py` | `:287` | `:380` |
| `ree_core/policy/model_disagreement.py` | `:121` | `:212` |
| `ree_core/predictors/e2_world_uncertainty.py` (SD-063) | `:364` | `:416` |

Two failure modes when these are reached inside a driver's `no_grad`:

- **Silent skip.** `ree_core/sleep/cross_module_consolidation.py:172` --
  `if not torch.is_tensor(loss) or not loss.requires_grad: return False`. Under `no_grad` the loss
  never requires grad, so the update is skipped and the run reports success. The same
  `if <loss>.requires_grad:` idiom guards every optimizer step in the showcase drivers
  (e.g. `916a:634,638,707,724,731`).
- **Hard raise.** `ree_core/sleep/self_model_aggregator.py:275` calls `loss.backward()` with no such
  guard. Under `no_grad` this raises `RuntimeError`. Since the audited runs completed, that path was
  not reached -- but **nothing in any driver declares or verifies that**, which is exactly
  GOV-CAPCONTRACT-1's point.

### 3.4 `agent.reset()` is a *partial* clear, with documented exceptions

`ree_core/agent.py:3232-3629`. Docstring `:3233`: *"Does NOT reset residue (invariant)."* State
explicitly documented as **persisting across episodes**:

| state | line | note in source |
|---|---|---|
| residue field | `3233` | invariant |
| SD-063 online head weights | `3461-3463` | "THE HEAD ITSELF PERSISTS ... learning is cumulative" |
| MECH-357 `avoidance_efficacy` | `3468-3471` | "developmental acquisition does not un-learn at episode boundaries" |
| MECH-358 affordance tables | `3475-3479` | "persist across episodes (developmental acquisition)" |
| trainable escape learner | `3486-3489` | "learned relief/safety predictions persist" |
| E2 escape-affordance linker | `3492-3496` | "Learned readout heads + viability index persist" |
| BLA attribution head weights | `3512-3515` | "learned weights PERSIST across episodes on purpose" |
| SD-032e PACC `_drive_bias` | `3314-3318` | "architectural purpose is cross-episode accumulation" |
| ARC-071 policy chunking | `3415-3422` | `end_episode()` not `reset()` -- "SLOW cross-episode process" |
| MECH-276 attribution buffer | `3453-3456` | "buffer itself PERSISTS across episodes" |
| ARC-108 `w_chan` / `V-hat_t` | `3258-3259` | eligibility trace cleared; weights persist |

Everything else in that 390-line method is cleared per episode.

### 3.5 ContextMemory has exactly three write paths, and two are OFF by default

| path | site | gate | default |
|---|---|---|---|
| waking per-tick | `agent.py:5000-5023` | `sd016_writepath_mode in ("sense_only","both")` | `"off"` (`config.py:419`) |
| training-time | `agent.py:10260-10264` | `sd016_writepath_mode in ("train_only","both")` | `"off"` |
| **SWS offline schema** | `agent.py:11702` (in `run_sws_schema_pass`, `:11487`) | `sws_enabled` + buffer >= 2 (`:11560,11569`) | `sws_enabled=False` (`config.py:3046`) |

**None of the 19 drivers sets `sd016_writepath_mode`** (verified by scan across all 19 plus
`scaffolded_sd054_onboarding.py`, `v3_exq_664`, `v3_exq_665`, `v3_exq_724`; the only scripts in the
corpus that set it are `907`, `908`, `922`, `922a` -- all to `"off"` -- and `943`, `946`, which set
it deliberately for ContextMemory experiments). So in every driver here, **the SWS pass is the only
live ContextMemory write path.**

The write itself is a `.data` mutation under the module's own `no_grad` (`e1_deep.py:238,272-273`),
so it is **unaffected by a driver's `no_grad` and by `agent.eval()`** -- with the exception of the
address policy (§3.1).

### 3.6 The residue field is plastic under any grad mode

`ree_core/residue/field.py:171-172, 247-248` mutate `centers.data` / `weights.data` inside the
module's own `torch.no_grad()` (`:170, :240, :325, :346`). Pure arithmetic; no gradient involved.
Same for the MECH-357 gate (`infralimbic_avoidance_gate.py:326-332`, a plain Python float) and the
MECH-358 bridge (`escape_affordance_bridge.py:65` -- *"Non-trainable: pure arithmetic over scalars +
per-action-class credit lists"*). **These are the only channels that are unconditionally plastic
during an observed life in every driver audited.**

### 3.7 The hippocampal exploration buffer is never written in any of these drivers

`agent.py:3687` is the **sole** writer of `HippocampalModule._exploration_buffer`
(`hippocampal/module.py:2864-2889`). It sits inside `_flush_exploration_episode`
(`agent.py:3650`), whose first statement is `if not self.config.replay_diversity_enabled: return`
(`agent.py:3656`). Default `False` (`config.py:3084`), and **no driver in this inventory sets it**
(906b sets `surprise_gated_replay=True`, `906b:403`, which is an unrelated flag, `config.py:3026`).

Consequence: `_segment_boundary_consolidate` (`906b:438-446`) calls `_flush_exploration_episode()`
at every segment boundary as its first action, and that call is **a no-op in this configuration**.

### 3.8 Sleep fires, but its replay-driven writeback is not constructed

`SleepLoopManager._run_cycle` (`sleep/phase_manager.py:392`) drives its Bayesian aggregator and
`SelfModelAggregator` off `self.replay_sampler` (`:436-470`). The sampler is constructed only when
`use_mech285_sampler` is on AND an anchor set exists (`agent.py:2701-2713`); the flag defaults False
and **no driver here sets it**. So `replay_sampler is None`, `_run_cycle` takes the `else` branch
(`:470-471`), `sws_routed_draws` is empty, and the `SelfModelAggregator.offline_gradient_pass`
(the one genuine offline **parameter** update, `self_model_aggregator.py:268-276`) is never invoked.
`use_cross_module_consolidation` likewise defaults False (`config.py:6217`) with
`cross_module_consolidation_steps: int = 0` (`config.py:6219`).

**What sleep still does** is `agent.run_sleep_cycle()` (`phase_manager.py:557` ->
`agent.py:11852`), whose SWS pass writes ContextMemory (§3.5) and whose REM pass runs attribution
(`agent.py:11736`). So in these drivers sleep changes `context_memory` and `ema_control_state`, and
changes **no parameter**.

### 3.9 MECH-457 (actor/critic) is absent from every driver

`use_actor_critic` defaults False (`config.py:6232`); `agent.action_critic` is constructed only under
it (`agent.py:408`); `actor_critic_step` raises without it (`agent.py:9701-9702`). **No driver in
this inventory sets it**, and none calls `actor_critic_step` / `actor_critic_parameters`. Row (b) is
therefore *structurally absent*, not merely frozen -- a stronger statement than "frozen", and a
different one for interpretation.

`use_gated_policy=True` IS set corpus-wide (`v3_exq_724:400`, inherited by the 906 family), but no
optimizer in any audited training phase covers `agent.gated_policy.parameters()` (§3.10), so those
weights remain at initialisation for the entire run.

### 3.10 What the training phases actually optimise

- **906 family / 665 curriculum** (`scaffolded_sd054_onboarding.py`): `agent.e1.parameters()`
  (`:2277,2382,2492,2606,2741`), `e2.world_transition` + `e2.world_action_encoder`
  (`:2278-2280` etc.), harm pathway = `latent_stack` + `e3.harm_eval_head` +
  `e3.harm_eval_z_harm_head` + `e2_harm_s` (`:1332-1338`, `:2428/2435`), and
  `lateral_pfc.bias_head_parameters()` (`:2453`).
- **Showcase family** (`471:233-250`, `524:198-209`, `664:375-386`, `916:499-510`, `916a:582-593`):
  `agent.e1.parameters()`, `e2.world_transition`+`world_action_encoder`,
  `e3.harm_eval_head`, `latent_stack.parameters()`.

Neither set covers `gated_policy`, `action_critic`, `ofc`, the E3 selector proper, or any of the six
self-optimizing modules in §3.3.

### 3.11 `env.reset()` restores body and re-randomises the world

`ree_core/environment/causal_grid_world.py:1548-1549` sets `agent_health = 1.0`,
`agent_energy = 1.0`; `:1486` re-shuffles the spawn pool, from which hazards, resources and the
agent are re-placed. `done` is `health_depleted or step_cap_reached` (`:3121-3123`).

**Therefore C3 (body/homeostatic) and C4 (ecological/world) are BROKEN at every segment boundary in
every multi-segment driver here** -- including the ones that deliberately preserve C1. This is
ARC-135's central case, present in the substrate exactly as the claim describes.

---

## 4. Per-family tables

Legend for "can it change during a life": **YES** / **NO** / **COND** (conditional -- condition
stated) / **VACUOUS** (the mechanism runs but has no state to act on) / **UNDETERMINED**.

### 4.1 Family `906-continuity` -- drivers 906a, 906b, 906c, 910b, 911, 912, 920

Shared implementation: `v3_exq_906b_full_stack_observational_fishtank.py`, `_make_config` `:380-436`,
`_observational_run` `:448-760`, `_segment_boundary_consolidate` `:438-446`. `agent.eval()` at
`906b:484`; per-step `torch.no_grad()` at `906b:532,562,581`.

| class | can it change? | what decides it (`file:line`) | continuity |
|---|---|---|---|
| (a) `parameters` | **NO** | `906b:484` `agent.eval()` + `906b:532,562,581` `torch.no_grad()`; no optimizer exists in `_observational_run`; SD-063 gated off by `agent.py:4160`; BLA head by `agent.py:4258` | **C2** |
| (b) `policy_value` | **NO (absent)** | `use_actor_critic` unset -> `agent.py:408` never constructs `action_critic`; `config.py:6232` default False | **C2** |
| (c) `e1_representations` | **NO** (weights) / within-episode only (LSTM hidden) | weights: as (a). `e1.reset_hidden_state()` at `agent.py:3249` runs only at `ep_idx==0` (`906b:507`) | **C2** / **C1** |
| (d) `e2_action_conditional` | **NO** | `e2.world_transition` / `world_action_encoder` optimised only in the curriculum (`scaffolded:2278-2280`); frozen in eval | **C2** |
| (e) `context_memory` | **COND -- only during a sleep cycle** | waking paths dead (`sd016_writepath_mode="off"`, `config.py:419`; §3.5). SWS write at `agent.py:11702`, reachable because `sws_enabled=True` (`906b:421`) and sleep fires via `_segment_boundary_consolidate` -> `notify_episode_end` (`906b:445`, `phase_manager.py:218`) on the K=10 cadence (`906b:249`) | **C1** |
| (f) `hippocampal_buffers` | exploration buffer **NO**; anchor/V_s/segmenter/staleness **YES** | buffer: `agent.py:3656`, `replay_diversity_enabled` unset (§3.7). Others: enabled via `use_per_stream_vs`/`use_event_segmenter` (`v3_exq_724:396`, `906b:415`) and **not cleared at segment boundaries**, because `_segment_boundary_consolidate` deliberately omits `agent.reset()` (`906b:438-441`) | **C1** |
| (g) `residue_affective` | **YES** | `agent.update_residue` (`agent.py:9963`) called every step (`906b`, in-loop); `field.py:171-172,247-248` are `.data` mutations under the module's own `no_grad`; never cleared (`agent.py:3233`). MECH-357 efficacy `infralimbic_avoidance_gate.py:326-332` (enabled `906b:400`), MECH-358 credit tables (`906b:415`) | **C1** |
| (h) `ema_control_state` | **YES** | dozens of accumulators/EMAs updated per step; NOT cleared at boundaries 2..N because `agent.reset()` is skipped there (`906b:504-511`) | **C1** |
| (i) `offline_sleep_updates` | **COND -- state yes, parameters NO** | cycle fires (`906b:445`); ContextMemory + REM attribution run; but `replay_sampler is None` (`agent.py:2701-2713`, `use_mech285_sampler` unset) so `SelfModelAggregator.offline_gradient_pass` is never called, and `cross_module_consolidation_steps=0` (`config.py:6219`) | **C1**, not **C2** |

**Continuity declaration for this family: C1 HELD across segments, C2 BROKEN (frozen), C3 BROKEN
(`causal_grid_world.py:1548`), C4 BROKEN (`:1486`)** -- via `_safe_reset(env)` at `906b:499`.

Per-driver deviations within the family:

- **906a / 906b / 906c / 910b / 911 / 912** -- identical to the table. 912 runs 60 segments instead
  of 8, so C3/C4 are broken 60 times.
- **920** -- `EVAL_EPISODES=1`. `ep_idx` never exceeds 0, so `_segment_boundary_consolidate` is never
  called (`906b:504-511`), hence **no sleep can fire during the life** (stated in the driver's own
  docstring, `920:9-18`). Row (e) becomes **NO** and row (i) becomes **NO** for 920. C3/C4 are
  **HELD** for 920 -- the single case in this inventory where all four continuities hold, at the
  cost of removing the only within-life ContextMemory write path.
- **910b** -- a telemetry wrapper; it replaces `_fishtank906b._observational_run` with a function
  that calls the original (`910b:330-352`), so its profile is 906b's by construction.

### 4.2 Driver `906` (original) -- `v3_exq_906_full_stack_observational_fishtank.py`

`agent.eval()` at `906:378`; `no_grad` at `906:404,423`; **`agent.reset()` at `906:381`, every
episode**.

Identical to §4.1 with one decisive difference: because `agent.reset()` runs at every episode
boundary, the ~340 lines of per-episode clearing in `agent.py:3246-3629` execute 8 times.

| class | 906 vs 906-continuity | what decides it |
|---|---|---|
| (f) `hippocampal_buffers` | **CLEARED per segment** | `agent.py:3568-3629` (`reset_per_stream_vs`, `reset_event_segmenter`, `reset_anchor_set`, `reset_staleness_accumulator`) invoked via `906:381` |
| (h) `ema_control_state` | **CLEARED per segment** (except the §3.4 exceptions) | `agent.py:3246-3629` via `906:381` |
| (e), (g), (i) | unchanged | residue survives by `agent.py:3233`; sleep still fires, via `agent.py:3243-3244` inside `reset()` |

**Continuity declaration for 906: C1 BROKEN at every segment boundary** (except residue and the
§3.4-listed persisters), C2/C3/C4 BROKEN as in §4.1. 906a's docstring "CONTINUITY REDESIGN" is
precisely the fix for this, and 906 vs 906a is the cleanest natural experiment on C1 in the corpus.

### 4.3 Family `gap9` -- drivers 929, 933, 933a

`929:158` / `933:180` / `933a:202` `agent.eval()`; per-step `torch.no_grad()` at `929:167`,
`933:190`, `933a:212`. No curriculum, no training phase of any kind. Config is minimal
(`929:126-141`): sleep flags only.

| class | can it change? | what decides it (`file:line`) | continuity |
|---|---|---|---|
| (a) `parameters` | **NO** | `929:158` eval + `929:167` `no_grad`; no optimizer anywhere in the file; **the agent is never trained at all** -- it runs from random initialisation | **C2** |
| (b) `policy_value` | **NO (absent)** | `use_actor_critic` unset (`929:127-137`). Additionally **no policy is exercised**: the action is uniform-random (`929:169-171`, `933:192-194`, `933a:214-216`) | **C2** |
| (c) `e1_representations` | **NO** | as (a); `_e1_tick` is never called (see (e)) | **C2** |
| (d) `e2_action_conditional` | **NO** | as (a); SD-056 not enabled in `_build_config` | **C2** |
| (e) `context_memory` | **NO -- and the sleep path is VACUOUS** | Waking paths off (`sd016_writepath_mode` unset). The SWS path exists but returns early: `run_sws_schema_pass` reads `_world_experience_buffer` (`agent.py:11564`) and returns at `agent.py:11569` when `n_buf < 2`. That buffer is appended **only in `_e1_tick`** (`agent.py:5468-5470`), and `_e1_tick` is called only from the agent's own `act`/`step` methods (`agent.py:9830,9860,9882`) or by a driver explicitly -- **the gap9 loop calls neither**, only `agent.sense(...)` and `agent.update_residue(...)` | **C1** |
| (f) `hippocampal_buffers` | **NO** | `replay_diversity_enabled` unset; `use_anchor_sets` / `use_event_segmenter` / `use_per_stream_vs` unset in `929:127-137` | **C1** |
| (g) `residue_affective` | **YES** | `agent.update_residue` called every step (`929:173`); `field.py:171-172` `.data` mutation. MECH-357/358 are **not enabled** here, so only the RBF field moves | **C1** |
| (h) `ema_control_state` | **YES** | MEL accumulator (`agent.py:10005-10013`), `steps_since_sleep` (`phase_manager.py:293`), `e3.post_action_update` (`agent.py:9992`). 933/933a additionally inject synthetic PE directly (`933:201-203`, `933a:222-224`) | **C1** |
| (i) `offline_sleep_updates` | **VACUOUS -- fires, changes nothing** | Trigger fires via `notify_waking_step` (`agent.py:10031` <- `phase_manager.py:251`). But: SWS returns early (see (e)); `replay_sampler is None` (§3.8); and the whole cycle executes **inside the driver's `no_grad`** (`929:167`) because `update_residue` is its call site -- so any gradient path within it is silently skipped (`cross_module_consolidation.py:172`) or would raise (`self_model_aggregator.py:275`) | -- |

**Continuity declaration for gap9: C1 HELD (agent never reset), C2 BROKEN (never trained at all),
C3/C4 BROKEN at each `env.reset()` respawn (`929:181`).**

These three drivers are *correctly designed for what they test* -- V3-EXQ-929's PASS gate is
`sleep_cycles_fired` and the arm-attribution split, which is a pure trigger-reachability question.
The finding here is not that they are wrong; it is that **their sleep cycles are structurally
incapable of changing any state**, so no result from them can bear on any claim about what sleep
*does*.

### 4.4 Family `showcase` -- drivers 471, 524, 664, 916, 916a

Two-phase: `_warmup_train` with `agent.train()` and four optimizers (`916a:582-599`; also
`471:233-256`, `524:198-215`, `664:375-392`, `916:499-516`) -> `_eval_agent` with `agent.eval()`
(`916a:798`; `471:450`, `524:417`, `664:563`, `916:693`) and per-step `no_grad`.

**"The life" is the eval phase.** Rows below describe the eval phase; the warm-up column records
what was plastic before it.

| class | change during the LIFE? | plastic during warm-up? | what decides it (`file:line`) | continuity |
|---|---|---|---|---|
| (a) `parameters` | **NO** | YES | `916a:798` eval; optimizers live in `_warmup_train` only (`916a:582-593`); every step guarded by `if <loss>.requires_grad:` (`916a:707,724,731`) which is False under the eval-phase `no_grad` | **C2** |
| (b) `policy_value` | **NO (absent)** | NO (absent) | `use_actor_critic` unset in all five | **C2** |
| (c) `e1_representations` | **NO** | YES | `optim.Adam(agent.e1.parameters(), lr=LR_E1)` (`916a:582`) -- warm-up only | **C2** |
| (d) `e2_action_conditional` | **NO** | YES | `916a:583-587` (`world_transition` + `world_action_encoder`) -- warm-up only | **C2** |
| (e) `context_memory` | **NO** | YES, by gradient only | `sd016_writepath_mode` unset -> both explicit write paths dead (§3.5); `sws_enabled` not set by 471/524/664/916/916a, so the SWS path is unreachable too. Gradient reaches `ContextMemory.memory` (`e1_deep.py:127`, an `nn.Parameter`) via `agent.e1.parameters()` during warm-up | **C1** |
| (f) `hippocampal_buffers` | **NO** | NO | `replay_diversity_enabled` unset (§3.7); no anchor-set flags | **C1** |
| (g) `residue_affective` | **YES** | YES | `field.py:171-172` `.data` mutation, grad-mode-independent | **C1** |
| (h) `ema_control_state` | **YES**, but cleared at each eval episode boundary | YES | `_eval_agent` calls `agent.reset()` per episode -> `agent.py:3246-3629` | **C1** |
| (i) `offline_sleep_updates` | **NO** | NO | `sws_enabled` / `rem_enabled` / `use_sleep_loop` not set; `agent.sleep_loop is None` -> `agent.py:3243` is a no-op | -- |

**Continuity declaration for showcase: C1 BROKEN per eval episode, C2 BROKEN, C3/C4 BROKEN per
episode.**

### 4.5 Drivers 665, 909, 913 (own loop, 906-lineage config)

- **665** (`v3_exq_665_curriculum_affective_fishtank_showcase.py`): `agent.eval()` at `665:333`,
  `no_grad` at `665:353,373`; `agent.reset()` per eval episode. Rows identical to §4.2 (906
  original) except that 665 sets `use_instrumental_avoidance=True` (`665:223`) and does **not** set
  the sleep flags -- so **(e) `context_memory` is NO** and **(i) is NO** for 665. Its curriculum
  (`_run_curriculum`, `665:238`) is the same `scaffolded_sd054_onboarding` trainer the 906 family
  uses, so warm-up plasticity matches §3.10.
- **909** (`v3_exq_909_sleep_dv_fishtank_multifiring.py`): imports `_make_config` from 906b
  (`909:165-172`) so the substrate is 906b's; `agent.eval()` at `909:300`; `no_grad` at
  `909:337,355`. It exists to **force** multiple sleep firings, overriding the K=10 cadence
  (`909:11`). Row (e) **YES via sleep, more often than 906b**; row (i) **state yes, parameters NO**
  -- the §3.8 argument is unchanged, since 909 does not set `use_mech285_sampler` either. This is
  the one driver in the inventory where within-life ContextMemory change is *frequent*.
- **913** (`v3_exq_913_developmental_ecology_fishtank.py`): 906b config with **sleep as an
  experimental ARM** -- `cfg.use_sleep_loop = bool(sleep_enabled)` (`913:340`), and the driver's own
  docstring records that in the OFF arm "`SleepLoopManager` is never constructed" (`913:12`).
  `agent.eval()` at `913:455`; `no_grad` at `913:506,525,863`. Rows follow §4.1, with
  **(e) and (i) = COND on the arm**: in the OFF arm both become **NO**, making 913 the cleanest
  existing within-life contrast on `context_memory` plasticity in the corpus.

---

## 5. The compact 19 x 9 matrix

`Y` = can and does change; `N` = cannot; `Ns` = cannot, structurally absent; `Yv` = mechanism runs
but is vacuous; `S` = only during a sleep cycle; `A` = depends on the experimental arm; `Ep` =
changes but is cleared at every episode boundary.

| driver | a params | b policy | c E1 | d E2 | e ctxmem | f hippo | g residue | h EMA | i sleep |
|---|---|---|---|---|---|---|---|---|---|
| 906 | N | Ns | N | N | S | Ep | Y | Ep | S |
| 906a | N | Ns | N | N | S | Y | Y | Y | S |
| 906b | N | Ns | N | N | S | Y | Y | Y | S |
| 906c | N | Ns | N | N | S | Y | Y | Y | S |
| 909 | N | Ns | N | N | S | Y | Y | Y | S |
| 910b | N | Ns | N | N | S | Y | Y | Y | S |
| 911 | N | Ns | N | N | S | Y | Y | Y | S |
| 912 | N | Ns | N | N | S | Y | Y | Y | S |
| 913 | N | Ns | N | N | A | Y | Y | Y | A |
| 920 | N | Ns | N | N | **N** | Y | Y | Y | **N** |
| 929 | N | Ns | N | N | N | N | Y | Y | **Yv** |
| 933 | N | Ns | N | N | N | N | Y | Y | **Yv** |
| 933a | N | Ns | N | N | N | N | Y | Y | **Yv** |
| 665 | N | Ns | N | N | N | Ep | Y | Ep | N |
| 471 | N | Ns | N | N | N | N | Y | Ep | N |
| 524 | N | Ns | N | N | N | N | Y | Ep | N |
| 664 | N | Ns | N | N | N | N | Y | Ep | N |
| 916 | N | Ns | N | N | N | N | Y | Ep | N |
| 916a | N | Ns | N | N | N | N | Y | Ep | N |

**Column (a) is `N` for all nineteen. No long-life driver in `ree-v3` permits any parameter change
during the observed life.**

### 5.1 Continuity matrix (ARC-135)

| driver | C1 cognitive | C2 parameter | C3 body | C4 world |
|---|---|---|---|---|
| 906 | BROKEN per segment | BROKEN | BROKEN per segment | BROKEN per segment |
| 906a/b/c, 909, 910b, 911, 912, 913 | **HELD** | BROKEN | BROKEN per segment | BROKEN per segment |
| 920 | **HELD** | BROKEN | **HELD** | **HELD** |
| 929, 933, 933a | **HELD** | BROKEN (never trained) | BROKEN per respawn | BROKEN per respawn |
| 665, 471, 524, 664, 916, 916a | BROKEN per episode | BROKEN | BROKEN per episode | BROKEN per episode |

**C2 is BROKEN in all nineteen.** No experiment in this family currently holds parameter continuity
across a life, which is what ARC-135 means by "an organism observed for many ticks with parameters
frozen is not developing."

---

## 6. Which drivers cannot support a within-life-learning claim

This is the operational payoff. On the evidence above:

### 6.1 Cannot support ANY claim requiring within-life learning of ANY kind

**None of the nineteen can support a claim requiring within-life *parametric* learning** (§5,
column a). For claims that would accept *non-parametric* within-life acquisition, the following are
still unable to support them, because the non-parametric channels are also absent or vacuous:

| driver | why |
|---|---|
| **929, 933, 933a** | Agent is never trained at all; actions are uniform-random (`929:169-171`); `_e1_tick` is never called, so ContextMemory, hippocampal buffers and the SWS pass are all unreachable (§4.3). The only state that moves is the RBF residue field and a handful of EMAs. Their sleep cycles change **nothing** (`Yv`). |
| **471, 524, 664, 916, 916a** | Sleep substrate absent (`sleep_loop is None`); ContextMemory write paths all dead; hippocampal buffers never written; `agent.reset()` per eval episode clears the EMA/control plane. Residue is the sole surviving channel, and it is reset-immune only by `agent.py:3233`. |
| **920** | Holds all four continuities -- but by removing the segment boundary it also removes the only within-life ContextMemory write path (`906b:504-511`, its own docstring `920:9-18`). Residue + EMA + hippocampal state only. |
| **665** | Same as the showcase family plus `agent.reset()` per eval episode; no sleep. |

### 6.2 Can support a *narrow* within-life claim, about non-parametric state only

**906a, 906b, 906c, 909, 910b, 911, 912, 913 (ON arm)** are the only drivers where a claim about
within-life change has a live mechanism: they hold C1 across segments and their sleep cycles do
change `context_memory` and `ema_control_state` (§4.1 rows e/f/h/i). Even here the claim must be
scoped to **memory-state and control-state acquisition**, never to parameter learning, and never to
the sleep cycle's *parameter* consolidation, which is not constructed (§3.8).

**913 is the best-instrumented of these**, because sleep is an explicit arm (`913:340`), giving a
within-driver contrast rather than a cross-driver one.

### 6.3 The correct null-interpretation rule for the existing corpus

Any past FAIL or null from drivers 1-19 that was read as *"the organism did not acquire X"* should be
re-read as *"the organism could not acquire X parametrically"* whenever X is parametric -- which is
GOV-CAPCONTRACT-1's fifth GOV-FAILLOC-1 bucket. This inventory does **not** re-adjudicate any
specific past run; doing so is `/failure-autopsy` and `/governance` work and is deliberately not
attempted here.

---

## 7. Findings recorded, not acted on

Per the chip's read-only constraint, each of these is recorded for separate routing.

**F1 -- `_flush_exploration_episode` is a no-op in the entire 906 family.** `_segment_boundary_consolidate`
(`906b:438-446`) calls it as one of only two boundary actions, with the comment "MECH-165: consolidate
+ bound buffer growth". It returns immediately at `agent.py:3656` because `replay_diversity_enabled`
is False (§3.7). Either the flag should be set or the call and its comment are misleading. **Not a
crash; a silent structural no-op that reads as an active consolidation step.**

**F2 -- the gap9 sleep cycle runs inside the driver's `no_grad`.** `notify_waking_step` is invoked
from `agent.update_residue` (`agent.py:10031`), and all three gap9 drivers call `update_residue`
inside `with torch.no_grad():` (`929:167/173`, `933:190/203`, `933a:212/224`). Any future
parameter-updating sleep pass reached from that call site will be **silently skipped**
(`cross_module_consolidation.py:172`) or **raise** (`self_model_aggregator.py:275`). This is latent:
it does not bite today only because §3.8 leaves those passes unconstructed.

**F3 -- `agent.eval()` silently changes the ContextMemory write-address algorithm.** `e1_deep.py:394`
returns `selection_scores.argmin()` in eval mode regardless of `write_selection`. A run configured
for `gumbel_learned` addressing that then observes under `agent.eval()` is measuring argmin
addressing. Relevant to V3-EXQ-943/946, which are the corpus's ContextMemory-addressing experiments.

**F4 -- correction to a figure in the source claim's notes.** GOV-CAPCONTRACT-1's registered notes
state that parameter-delta witnesses "exist ad hoc in 4 experiment scripts". Re-measured this pass:
there is a **shared helper**, `experiments/_lib/zworld_encoder_guard.py:79`
(`latent_stack_weight_delta`), consumed by at least 728, 728b, 734, 737, 742, 808, 813, 948, plus a
second shared guard `experiments/_metrics.py:662` (`assert_policy_trained`), plus ad-hoc witnesses in
449/449a/449b, 465, 485d-485m, 499, 633, 696, 702, 722, 809, 817, 817a, 822b, 826/826a, 862/862a,
939/939a -- ~30 scripts, not 4. **The sharper and still-true statement is the one that matters here:
zero of the nineteen long-life drivers has a parameter-delta witness.** The primitives to build one
already exist and need not be written from scratch.

**F5 -- `use_gated_policy=True` is set corpus-wide but nothing trains it.** `v3_exq_724:400`, inherited
by the whole 906 family; no optimizer in `scaffolded_sd054_onboarding.py` or in any showcase driver
covers `agent.gated_policy.parameters()` (§3.10). ARC-062 gating therefore operates at random
initialisation in every run in this inventory.

**F6 -- 906 vs 906a is an unexploited natural experiment on C1.** Same substrate, same curriculum,
same eval env; the sole difference is `agent.reset()` per segment (`906:381`) versus
`_segment_boundary_consolidate` (`906b:504-511`). ARC-135 asks exactly which continuities matter, and
this pair isolates C1 with everything else fixed.

---

## 8. Method, scope, and what this audit did NOT establish

### 8.1 UNDETERMINED cells

- **Whether `self_model_aggregator.offline_gradient_pass` would raise if reached from a gap9 driver.**
  Established: it calls `loss.backward()` with no `requires_grad` guard (`self_model_aggregator.py:275`)
  and the gap9 call site is inside `no_grad` (§F2). *Not* established by execution -- the path is
  unreachable today (`agent.py:2793-2802` requires `use_mech273_self_model`, unset), so this was not
  observed, only read.
- **Whether `_world_experience_buffer` is genuinely empty in gap9 runs.** Established by tracing every
  call site of `_e1_tick` (`agent.py:9830,9860,9882`, plus explicit driver calls such as `906:404`) and
  confirming the gap9 loops call neither. *Not* established by instrumenting a run.
- **Per-run realised behaviour of every EMA in row (h).** Row (h) is asserted at the level of "the
  reset method does / does not clear it" (`agent.py:3232-3629`). Which EMAs actually move in a given
  run is a per-run measurement this audit did not make.
- **The showcase family's exact curriculum coverage of `e3` sub-heads.** `916a:588` optimises
  `agent.e3.harm_eval_head.parameters()`; whether other `e3` submodules carry trainable parameters
  that no optimizer covers was not exhaustively enumerated.

### 8.2 Method notes

Config defaults were read from the dataclass definitions in `ree_core/utils/config.py`, then checked
against each driver's own kwargs and post-construction assignments. Where a driver imports another's
`_make_config`, the import was verified line-by-line rather than assumed (§1). No run was executed;
this is a static audit of `ree-v3 @ 9cfaf4a`.

### 8.3 Coordination note -- a parallel session is building the consumer

`ree-v3/experiments/_lib/capability_contract.py` is present **untracked** in the shared checkout and
is being written right now: 1202 lines when first read at 2026-08-27T20:00Z, 1266 lines twelve
minutes later. It implements GOV-CAPCONTRACT-1's preflight -- chip item 4 of the intake's §7 -- and
the comment block above its `PLASTICITY_MODES` tuple explicitly names *this file's path* as the
inventory it is waiting on, describes its own vocabulary as a stub, and states that validation
against it is "advisory, NEVER a gate". §2 above is written to be adopted by it directly. **That file
was read and not modified**, per CLAUDE.md's read-modify-write rule; it is cited by symbol rather
than by line for the reason given in §2.

---

## 9. Cross-references

- `GOV-CAPCONTRACT-1`, `ARC-135` -- `REE_assembly/docs/claims/claims.yaml` (`ARC-135` at `:88337`)
- `evidence/planning/thought_intake_2026-08-27_developmental_integration_and_readiness_programme.md` §3a, §6
- `evidence/planning/developmental_readiness_investigation_2026-08-12.md` §2, §3 -- the Levels 0-7
  matrix; this inventory supplies the per-driver detail behind its "Gradient-based weight learning
  during a life: Level 1 = N" row
- `evidence/planning/organism_lifespan_development_review_906_lineage_2026-08-10.md` -- the review that
  routed 912 and 920
- `evidence/planning/sleep_substrate_plan.md` -- GAP-9, SD-SLEEP-ENTRY-PRESSURE
- `ree-v3/experiments/_lib/capability_contract.py` (in flight, untracked), `_lib/precondition_gate.py`,
  `_lib/canonical_profile_fingerprint.py`, `_lib/zworld_encoder_guard.py:79`, `_metrics.py:662`
