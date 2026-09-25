# A ree_core-owned native waking trainer with a gradient-reach guard -- design (no build)

- **Status: FINAL.** Interim (step 1, the module -> loss map) was `6457bcd40a`; sections 2-7 added at 2026-09-25T00:15Z. Session `bt0925-trainer` (Worker L, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-native-waking-trainer-design`.
- **Scope:** design plus a canary probe of the guard only. No ree_core edit, nothing queued, no registry edit, no chips. Options are presented for the user and `/governance`; nothing is decided here.
- **Code under test:** ree-v3 `origin/main` @ **`863d23d65a`** (private detached worktree; the same sha as the census). Every `file:line` below is against that sha.
- **Inputs:** `breakthrough_pass_synthesis_20260925.md` (08c6ed0c53), `gradient_reach_census_20260925.md` (940c690c9dd) and its raw JSON under `probes/census/results/`, `action_decoder_training_trace_20260924.md` (622716398d4), `action_decoder_training_causal_probe_20260925.md` (a369f411ff8).
- **Evidence domain of this step: D0** (code read) plus the census's D1 reach classes, re-read from its raw JSON where a row depends on them.

## 0. Premises re-measured before building on them

| Premise (brief / census) | Re-measured | Verdict |
|---|---|---|
| ree_core has native losses for E1, E2-self and E2-world, but nothing native steps them | `compute_prediction_loss` `agent.py:11595`, `compute_e2_loss` `:12841`, `compute_e2_world_loss` `:12859` exist. The only ree_core caller of the E2-world loss is the sleep consolidation pass behind `use_sleep_world_forward_consolidation=False` (`config.py:7535`). | Confirmed. |
| Those three losses are replay losses over **detached** buffers, so a trainer that steps them cannot hit a retained-graph error | Buffers are appended detached: `agent.py:6294-6295` (z_self / z_world), `:6299` (action one-hot), `:11407-11411` (`record_transition`, explicitly detached because an undetached action "propagates through E3's graph ... modified by an inplace operation"). | Confirmed. This is the property the whole design leans on. |
| "grad None at a step" is the dead-optimizer signature | **Corrected for the guard.** In census recipe A, E1 and E2-self tensors read `none` on their first 1-2 steps, then `nonzero` for 78-79 steps. Cause: the zero-loss sentinel `next(module.parameters()).sum() * 0.0` (`agent.py:11601`, `:12843`) returns before the replay buffers fill. It gives the first tensor grad `zero` and the others grad `None`. A guard that fires on "None at any step" would false-alarm on every healthy warm start. The dead signature is **no nonzero grad over the whole window**. | Guard spec in section 3 uses the window form. |
| The census's dead entries are the decoder, DR-13 GRU and E2 world head (under A) | Also dead under A, and not named in the census headline: `e1.context_memory.write_gate.*` (grad `None` 80/80). The write happens under `torch.no_grad()` (`e1_deep.py:381-384`), so this is a **structurally non-gradient path**, not a defect of the recipe. | Frozen-by-design (non-gradient write). It goes on the guard's allowlist with its reason. Without that entry the guard would fire on correct code. |
| The SD-070 P0 trainer trains the z_world path that `sense()` uses | `ZWorldP0Trainer._z_world_path` (`zworld_p0.py:457-466`) feeds **raw** `world_obs` to `split_encoder.world_encoder`. `agent.sense()` feeds `world_obs_encoder(obs_world)` (`agent.py:5189`). | Known and registered (SD-ZWORLD-SENSE-PATH-PARITY, `registered_no_build_owed_hygiene_path_divergence`). Carried as a caveat. A native trainer should train through the path the agent actually reads (section 2). |

## 1. Module -> loss map

Columns:
- **loss that should train it**
- **exists?** R = in ree_core with a native caller; L = in ree_core as a loss/trainer, but only drivers invoke it; D = driver-only; N = no loss anywhere
- **needs live latents?** P = phased/replay-safe: runs over recorded, detached observations or latents, so it is retained-graph-safe by construction (SD-070 / ZSelfP0 pattern). V = needs the live, undetached tick graph.
- **owner row**
- **census class** (N / A / B / C / Z) from `gradient_reach_census_20260925.md` section 3.

### 1a. Act-path modules that a waking trainer should own

| # | module (act-time call site, census) | loss that should train it | exists? | live? | owner row | census N/A/B/C/Z |
|---|---|---|---|---|---|---|
| 1 | `e1.transition_rnn` / `output_proj` / `prior_generator` (`e1_deep.py:1296 <- :2063`) | E1 multi-step latent prediction (`compute_prediction_loss`, `agent.py:11595`) | **L**: loss native, nobody steps it | **P**: replay over detached `_self/_world_experience_buffer` | none. Census #11 (all-ON trains no E1); GFLAG-0491 | O/T/T/**O**/O |
| 2 | `e1.context_memory` read path (`query_proj`, `key_proj`, `value_proj`, `output_proj`, `memory`) | same as #1 (gradient reaches it through `read()`) | L | P | none (as #1); write-path rows SD-016 / contextmemory-write-addressing | O/M/M/O/O |
| 3 | `e2.self_transition` / `self_action_encoder` (`e2_fast.py:198 <- :821`) | E2 motor-sensory forward model (`compute_e2_loss`, `agent.py:12841`) | L. Its buffer is filled only by `record_transition` (`agent.py:11395`), which **the harness** calls (`experiments/_harness.py:228`), not the agent. | P | none. Census #12 (all-ON: in the e2 optimizer, grad `None` 24/24) | O/T/O/**D**/O |
| 4 | `e2.world_transition` / `world_action_encoder` (`e2_fast.py:221 <- :822`) | SD-056 world-forward InfoNCE (`compute_e2_world_loss`, `agent.py:12859`, over `world_forward_contrastive_loss` `e2_fast.py:355`) | L: sleep-only caller, default off (`config.py:7535`). Tier1 uses its own MSE instead (`goal_pipeline_tier1.py:530`). | P | GFLAG-0485 (R1). **Coupled:** own-replay action coverage starves it (0485 addendum 2). | O/**D**/T/T/O |
| 5 | `e3.harm_eval_head` (`e3_selector.py:1386 <- :1678`, every E3 tick) | regression of `harm_eval_head(z_world)` on `abs(harm_signal)` | **D**: tier1 only (`goal_pipeline_tier1.py:535`; buffer append `:580`). No ree_core loss. The target reaches the agent natively through `update_residue(harm_signal)` (`agent.py:11196`). | P: replay of (detached z_world, harm) | **none**. Census #10 NEW; GFLAG-0491 | O/**D**/T/**O**/O |
| 6 | `latent_stack.split_encoder.world_encoder` (+ `world_precision_logit`, SD-106 skip) | SD-070 P0a scene-structure CE + proximity + preservation (`ZWorldP0Trainer`, `zworld_p0.py:401`; optimizer `:577`) | L: ree_core class, drivers invoke it (`experiments/_lib/zworld_p0_warmup.py:255`) | P: raw-obs buffer (`zworld_p0.py:435-451`) | SD-070; parity caveat SD-ZWORLD-SENSE-PATH-PARITY | O/D/M/M/M |
| 7 | `body_obs_encoder`, `split_encoder.self_encoder`, `latent_stack.self_recurrence` (DR-13) | ZSelfP0 body forward model (`ZSelfP0Trainer`, `zself_p0.py:298`; optimizer `:724`) | L: ree_core class; no driver uses it yet | P: raw-obs episode buffer, chunk-local graph (`zself_p0.py:486-511`) | `sd_zself_training_path` (ree-v3 863d23d, `implemented_pending_validation`) | GRU: -/**D**/-/-/T |
| 8 | `e2.action_object_head` (the O encoder; `e2_fast.py:691 <- :813`) | consequence-grounding loss on o_t (SD-080's proposal) and/or codec tie `decode(encode(a)) ~ a` | **N** | P: the (z, a) pairs are in the replay buffers | SD-080 (`pending_implementation`) | O/D/O/D/O |
| 9 | `hippocampal.action_object_decoder` (`module.py:646 <- :2280`, 192 calls / 12 steps) | `CE(decoder(E2.action_object(z, a).detach()), a)`. Probe-built in a369f411ff8: fits held-out 1.000, but FAILS alone. | **N** in ree_core (probe-only) | P | GFLAG-0488 / GFLAG-0490. **Coupled codec:** untrained decoder, unbounded decode used as the action, iteration-0 sampling ~12x off-range | O/**D**/O/O/O |
| 10 | `hippocampal.terrain_prior` (`module.py:607 <- :2150`) | today: driver-only behavioural cloning to E3's own pick (`v3_exq_042_hippocampal_terrain_training.py:129`), which is **circular** (trace Q2). It should be an outcome-grounded target. | **D** (042 family) | P: (z_world, e1_prior, selected O) are replayable | **none of its own**. Census #3 gap; extend SD-080 / GFLAG-0488 | O/D/O/O/O |
| 11 | depth stack: `beta/theta/delta_encoder`, `delta_to_theta`, `theta_to_beta`, `beta_to_split`, `world_topdown` / `self_topdown` (`stack.py:1430`/`:1438 <- agent.py:5224`; `:1017 <- :1444`) | its **designed** objective has no loss. `LatentStack.predict` (`stack.py:1704-1711`) and the five `*_predictor` heads (`:1256-1260`) exist, but no `compute_*_loss` calls `predict`. It is reached only incidentally, by live-latent aux losses (SD-018 proximity, `agent.py:11790`, tier1 aux optimizer `goal_pipeline_tier1.py:536-537`). | **N** for its own objective | V today. P possible: re-encode stored obs sequences through `latent_stack.encode`, the way ZSelfP0's `_native_chain` does. | none. Census #13, `complex (probe-gated)` until a z_beta consumer D2 check | O/D/T/O/O |
| 12 | `gated_policy.head_0` / `head_1` / `discriminator` (all-ON only; `gated_policy.py:591`/`:535 <- agent.py:8350`) | REINFORCE on selection + `GatedPolicy.p1_training_auxiliary_loss` (`gated_policy.py:630`) | L (aux loss) + D (REINFORCE, driver-built in the `v3_exq_610*` family) | V (REINFORCE on the tick's selection log-prob) | unconfirmed (ARC-062 / SD-082). Census #14 | -/-/-/O/- |
| 13 | `lateral_pfc.rule_bias_head` (all-ON; `lateral_pfc_analog.py:473 <- agent.py:8542`) | REINFORCE via score_bias (`lateral_pfc_analog.py:494-501` docstring) | D (`allon_training.py:574`) | V | SD-082 (`implemented_pending_validation`). Grad **exactly 0** in the all-ON run (constant-candidate-summary degeneracy, `lateral_pfc_analog.py:429-440`). | -/-/-/D/- |
| 14 | `ofc.devaluation_bias_head` (all-ON) | REINFORCE (`allon_training.py:578`) | D | V | SD-033b | -/-/-/T/- |

### 1b. Not waking-trainer targets

| module | why | guard treatment |
|---|---|---|
| `residue_field.rbf_field` | non-gradient harm-accumulation rule | **FROZEN-BY-DESIGN** (non-gradient) |
| `residue_field.neural_field` | Its trainer already exists inside `ResidueField.integrate()` (`field.py:1262`, flag-gated) and runs off detached harm history. It is an integrate/sleep-phase trainer, not a waking one. Its consumer reach is D2-negative (GFLAG-0479). | owned by `residue-cost-untrained-neural-field`; **excluded** from waking groups, with that reason |
| `e1.context_memory.write_gate` (and `write_content` when present) | The write runs under `torch.no_grad()` (`e1_deep.py:381-384`), so there is no gradient path by construction. Addressing is trained only by the opt-in write-addressing loss (`agent.py:11689`). | **FROZEN-BY-DESIGN** (non-gradient write) unless `contextmemory_write_addressing_loss_weight > 0` |
| `lateral_pfc.delta_proj` / `world_proj` | "frozen-random; not trained in landing" (`lateral_pfc_analog.py:233-236`) | **FROZEN-BY-DESIGN** |
| `ofc.state_bias_head` when `train_state_bias_head=False` | last layer zeroed, output 0 (`ofc_analog.py:201-215`) | **FROZEN-BY-DESIGN** |
| `world_obs_encoder` (`agent.py:5189`) | No loss trains it. ZSelfP0's gradient reaches it, but that optimizer excludes it on purpose. The parity spike measured the random `Linear+ReLU` as benign for z_world decodability (D1 only). | **DECISION** for the user: FROZEN-PENDING (allowlisted with the parity citation), or trained by moving SD-070 P0a onto the sense path (option note in section 2) |
| `latent_stack.*_predictor`, `e3.reality_scorer`, `harm_cost_fallback_scorer` (gated out, `e3_selector.py:1390`), `harm_eval_z_harm_head`, harm encoders (own row `sd_zharm_a_warmup_optimizer_group`), `ofc.outcome_proj`, `lpfc.discriminator_proj` | not read at act in any census recipe | **INERT**. Not in any waking group, so the guard does not see them. An inert module is a coverage question, not a guard question. |
| `e3.benefit_eval_head` | Native loss exists (`compute_benefit_eval_loss`, `agent.py:11701`), but it reads `_current_latent` at the current tick, not a replay batch. Not read at act at defaults. | Belongs to the grounded-valuation lane (50b679abb8). Joins a waking group only when that channel is enabled; it would need buffering to be replay-safe. |

### 1c. What the map says, in one paragraph

Of the 14 act-path rows:
- **Five have a native loss that nothing steps** (#1-4, E1 and E2): L, phased-safe, cheap to own.
- **Two have a ree_core phased trainer that only drivers call** (#6 SD-070, #7 ZSelfP0).
- **Three have no loss anywhere and are the coupled codec plus the prior** (#8-10): SD-080, GFLAG-0488/0490, and the terrain_prior gap.
- **One has a driver-only loss whose target the agent already receives natively** (#5 harm_eval_head: the cheapest new native loss in the set).
- **Three are REINFORCE-style and need the live selection graph** (#12-14, all-ON only).
- **One has no designed objective wired at all** (#11, the depth stack, probe-gated).

So a native trainer can own **#1-7 without writing any new objective except the harm_eval regression**. #8-10 cannot be owned until the codec objective is designed, and #11-14 are separate questions.

## 2. Architecture options

All three options share the section 1 map, and each is armed with the section 3 guard.

**The measured cost numbers** come from `trainer_cost_probe.py`:
- Setup: native defaults, `world_dim` 32, CausalGridWorldV2 seed 42, Mac CPU with 2 threads, median of 30.
- One act tick costs **174.8 ms**. E1 update 12.0 ms; E2-self 0.31 ms; E2-world 0.35 ms; harm_eval 0.16 ms. All four together are **12.9 ms, 0.07x an act tick**.
- The three native replay losses are live at defaults after 60 ticks (`requires_grad` True): E1 0.0109, E2-self 0.0035, E2-world 2.72.

**RNG.** All three native replay losses sample from the **global** torch RNG with no generator argument:
- `torch.randint` at `agent.py:11608`
- `torch.randperm` at `:12848` and `:12911`

So any ON-mode trainer shifts every later act-path draw, including E3's `multinomial`, unless it is wrapped. Measured:
- A bare `compute_prediction_loss` changes the global RNG state (`rng_neutral_without_wrapper False`).
- Wrapping the update in `torch.random.fork_rng()`, with the trainer's own private generator state swapped in and saved back, leaves the global state byte-identical (`rng_neutral_with_fork_rng True`).
- This needs **no loss-signature change**.

### (i) `WakingTrainer`: an agent-owned object, per-module optimizer groups, stepped on a fixed cadence from the agent's own replay

**Shape.**
- Built only when `use_native_waking_trainer=True`.
- It holds one optimizer per group (sketched in the sketch below):
  - `e1`: map row 1, plus 2
  - `e2_self`: row 3
  - `e2_world`: row 4
  - `harm_eval`: row 5, a new regression over a (z_world, |harm|) replay buffer the trainer fills
  - `zworld_p0` and `zself_p0`: rows 6-7, the existing ree_core trainer classes re-run at a slow cadence (or once, at the first K ticks) from buffers the trainer fills
- Each group lists its tensors **by name**, and the guard checks the list against the map.

**Driving.** It is stepped from inside `agent.update_residue()` (`agent.py:11196`). That is the one per-step consequence entry: the StepHarness contract calls it exactly once per env step (`experiments/_harness.py:19`, `:361`), and it already receives `harm_signal`. It steps every `K` ticks (a config value).
- The trainer records its own E2-self transitions from `_current_latent` and `_last_action`. It does not depend on the harness's `record_transition` (`_harness.py:228`), so a driver that skips that call cannot silently starve the group. This is design point 3 in section 5.

**Assessment.**

| Axis | Assessment |
|---|---|
| RNG / bit-identity OFF | Structural absence: no object, no buffer, no draw. The OFF arm stays bit-identical. |
| RNG ON | `fork_rng` with a private generator (measured neutral above). The act path then draws exactly the numbers it would have drawn without the trainer; only the weights differ. |
| Retained graph | **None by construction.** Every group trains from detached replay (`agent.py:6294-6299`, `:11407-11411`) or from raw-obs re-encodes (`zworld_p0.py:435-451`, `zself_p0.py:486-511`). The guard's leak report confirms this for E1: 0 leaked tensors under an E1-only group, seeds 42 and 43. |
| Sleep interaction | `CrossModuleConsolidator` builds fresh optimizers per call over E1 and E2 (`cross_module_consolidation.py:215-219`). Fresh Adam state per call means no shared-moment conflict. The trainer must pause during a sleep cycle so both are never stepping in the same tick. The sleep `e2` group is itself a documented dead-optimizer case ("delta == 0.0 on every seed", `config.py:7520-7534`), so the guard should wrap sleep groups too. |
| Cost | ~0.07x an act tick at K = 1 (measured); ~0.01x at K = 8. |
| Closes the loop? | **Yes for rows 1-5.** Weights change during waking from experienced consequence, which is the native "experience -> update -> later behaviour" link the census found missing. |

### (ii) Phased P0 trainers only (extend the SD-070 / ZSelfP0 pattern module by module)

**Shape.** Add `E1P0Trainer`, `E2P0Trainer` and `HarmEvalP0Trainer` classes in ree_core, alongside `ZWorldP0Trainer` / `ZSelfP0Trainer`. Each has an `observe()`, a `train()` and a holdout report. Drivers (or a ree_core `run_all_p0()` helper) call them once, before the evaluated phase.

| Axis | Assessment |
|---|---|
| RNG / bit-identity OFF | Uses the existing pattern: private `torch.Generator` / `random.Random` (`zworld_p0.py:580`, `zself_p0.py:697`). OFF is bit-identical. |
| Retained graph | None, as in (i). |
| Sleep interaction | None. The trainers run before deployment. |
| Cost | Zero per tick. A one-off batch cost at warmup. |
| Closes the loop? | **No.** Training ends before the evaluated phase, so experience during that phase changes no weight. Behaviour depends on the warmup distribution, not on the agent's own experience. Choosing this option means the "experienced consequence -> learning" link stays open by design. It also keeps the monostrategy starvation: GFLAG-0485's E2 action coverage cannot improve from what the agent later does. |
| Where it wins | Reproducibility, holdout readouts, and it already exists for rows 6-7. |

### (iii) Online per-tick losses inside the agent, on live latents

**Shape.** Inside `sense()` / `select_action()`, compute each module's loss on the live, undetached tick graph and step it every tick.

| Axis | Assessment |
|---|---|
| RNG | A draw every tick, so ON can never be RNG-neutral without the same wrapper as (i). OFF is fine. |
| Retained graph | **The dominant hazard.** `_last_action` is undetached by default and carries the previous tick's selection graph into this tick's z_world through SD-007 reafference (`agent.py:5212-5222`, `detach_carried_prev_action=False` at `config.py:6124`). `record_transition`'s docstring records the exact failure this produces: "propagates through E3's graph ... modified by an inplace operation" (`agent.py:11402-11406`). Every live-latent loss has to cut that path first, and that cut is itself a behaviour-visible change to the gradient graph (ARC-021 H2). |
| Sleep interaction | Must be disabled in sleep, where there is no tick graph. |
| Cost | Every tick, with the full encoder in the graph. The most expensive option. |
| What only it can do | Train the three REINFORCE heads (map rows 12-14), and train the depth stack and encoders through the path the agent actually reads (rows 6, 11, and `world_obs_encoder`). |
| Closes the loop? | Yes, with the most machinery and the highest breakage risk. |

A **hybrid** is option (i), with (ii)'s classes as scheduled members, and (iii) restricted to rows 12-14 behind their own flags. That hybrid is what the recommendation in section 6 describes.

## 3. The guard (load-bearing)

### 3a. What it asserts

It asserts per trainer group, over a window of N optimizer steps. The prototype is `grad_reach_guard_proto.py` (probe-only, not a ree_core module).

| id | assertion | why this form |
|---|---|---|
| G1 REACH | every non-allowlisted tensor gets a **nonzero, finite** grad on >= 1 step in the window; grad `None` and grad exactly 0 both count as "not reached" | Not "None at any step". The native zero-loss sentinel yields `None` or 0 while buffers fill (section 0), and the naive form falsely flagged all **30/30** healthy E1 tensors (A_e1, seeds 42 and 43). "Exactly 0" is included because `lateral_pfc.rule_bias_head` is in its optimizer with grad exactly 0 (census, 6/6 steps). |
| G2 MOVED | every reached tensor changed value over the window | catches "gets gradient, but no stepping optimizer holds it or lr is 0" |
| G3 ALLOWLIST | every allowlisted (frozen-by-design) tensor did **not** get gradient; a stale entry FAILS | An allowlist is itself a negative instrument: an over-broad entry would hide a dead module forever. |
| G4 NON-VACUOUS | group non-empty, >= `min_steps` steps, >= 1 tensor checked; otherwise **CANNOT_DETERMINE**, never PASS | CLAUDE.md "Negative instruments", remedy 1: an explicit cannot-determine category |
| G5 LEAK | tensors outside every group that the group's losses reached. Reported, not failed. | The census `**` case: gradient discarded, as with ZSelfP0 reaching the depth stack and `world_obs_encoder` |

The frozen-by-design allowlist is in section 1b:
- `residue_field.rbf_field`
- `e1.context_memory.write_gate` / `write_content`
- `lateral_pfc.delta_proj` / `world_proj`
- `ofc.state_bias_head` (conditional)

Each entry carries its file:line reason. `world_obs_encoder` is **not** on it until the user decides (section 1b).

### 3b. The canary probe (the one runnable thing in this pass)

Setup:
- Probe: `guard_canary_probe.py <case> <seed>`.
- It runs the census recipes verbatim against a private worktree at `863d23d65a`, attaching a guard to every optimizer the recipe builds via `register_step_pre_hook`.
- `world_dim` = `self_dim` = 32. Seeds 42 and 43. Raw JSON: `results/guard_*_s{42,43}.json`.

| case | what it is | guard verdict (s42 / s43) | caught | status-quo check "some param in the optimizer moved" |
|---|---|---|---|---|
| **A_all** | V3-EXQ-1078: `Adam(agent.parameters())` on E1+E2 losses, 80 steps | **FAIL / FAIL**. 101 dead tensors (228,803 params) of 137 checked; 4 allowlisted. | **`hippocampal.action_object_decoder` (canary 1: yes, both seeds)**, plus the DR-13 GRU, E2 world head, `action_object_head`, terrain_prior, harm_eval_head, neural_field, depth stack, obs encoders | **PASS**: blind |
| **allon**, e2 optimizer (`allon_training.py:572`) | all-ON P0 e2 optimizer, 24 steps | **FAIL / FAIL** | **`e2.self_transition` + `self_action_encoder` (canary 2: yes, both seeds)**, plus `e2.action_object_head` | **PASS**: blind |
| allon, SD-070 P0a (`zworld_p0.py:577`) | 17 tensors, 12-16 steps | PASS / PASS | - | PASS |
| allon, lpfc bias (`:574`) | 1 step at this budget | FAIL (grad exactly 0) at `min_steps=1`. At the design's `min_steps=8` this budget is **CANNOT_DETERMINE**. The census 6 x 100 run showed 6/6 exactly-zero steps, so the FAIL is real but not established by this run. | `lateral_pfc.rule_bias_head` | **FAIL** |
| allon, ofc deval (`:578`) | 1 step | PASS (at `min_steps=1`) | - | PASS |
| **A_e1** (negative control) | the same agent, but `Adam(e1)` on `compute_prediction_loss` only, with the allowlist | **PASS / PASS**: 28 checked, 2 allowlisted, 0 leaked | - (no false alarm) | PASS |
| A_e1, no allowlist | same, allowlist removed | FAIL / FAIL on exactly `e1.context_memory.write_gate` (2 tensors) | shows each allowlist entry is necessary and specific | - |
| **A_stale** | A_e1 with a planted wrong allowlist entry (`e1.transition_rnn`) | **FAIL**: 12 stale-allowlist tensors | G3 works | - |
| **zselfp0** (positive control) | `run_zself_p0`, 17-tensor optimizer, 8 steps | **PASS / PASS**. Leak reported (G5): depth stack (7 modules) + `world_obs_encoder`, matching the census `**`. | - | PASS |
| vacuous | empty group; a 3-step window with `min_steps` 8 | **CANNOT_DETERMINE** for both; the full 8-step window PASSes | G4 works | - |

**Reading.**
- The guard catches both named canaries on both seeds.
- It passes the correctly scoped groups (E1-only, SD-070 P0a, ZSelfP0).
- It refuses to pass an empty or too-short window.
- It fails a planted stale allowlist entry.
- The check a driver can see today ("the optimizer's weights moved") passes on both defective recipes. That is exactly how this defect stayed silent across ~13 decoder drivers and 14 all-ON drivers.
- The existing `experiments/_lib/zworld_encoder_guard.py` snapshots `latent_stack` only (its docstring, METHOD), so by construction it cannot see the decoder, the E2 heads or harm_eval (D0).

**Evidence domain of the guard result: D1.** It shows reach, not influence. That is the right domain for a guard.

### 3c. Specification as a contract test (`tests/contracts/test_waking_trainer_grad_reach.py`, proposed, not written)

1. **Coverage.** Derive the act-path parameter set by running the census's read tracer (`ParamReadMode` over a 12-step no-grad act pass) at deployed dims. Assert that the act-path set is a subset of (trainer groups ∪ allowlist ∪ DEFERRED).
   - DEFERRED is a dict of `module prefix -> registered row id`: SD-080, GFLAG-0488, the terrain_prior row, the depth stack row, the SD-082 / ARC-062 heads, SD-ZWORLD-SENSE-PATH-PARITY.
   - A DEFERRED entry without a row id FAILS. Deferral is visible debt, not a silent exemption.
   - The derived act-path set must be non-empty and must contain the pinned members `hippocampal.action_object_decoder` and `e3.harm_eval_head`. That guards the derivation itself against vacuity (CLAUDE.md "the test half").
2. **Reach.** With the trainer ON for N ticks (N >= `min_steps` x K), every group verdict is PASS. Any CANNOT_DETERMINE is a test **failure**, not a skip.
3. **Pinned canaries** (remedy 2, a known-baseline canary):
   - the guard, applied to the V3-EXQ-1078 recipe, returns FAIL naming `hippocampal.action_object_decoder`;
   - applied to the all-ON e2 optimizer recipe, it returns FAIL naming `e2.self_transition`;
   - a planted stale allowlist entry FAILs.
   If the guard ever stops catching these, it has broken, and the test says so.
4. **RNG and bit-identity.**
   - Trainer OFF: a K-step rollout's actions, latents and final global RNG state hash equal to the pre-change baseline.
   - Trainer ON: the global RNG state is identical before and after every trainer update.
5. **How it FAILS on the pre-change code (measured / derived here).**
   - At `863d23d65a` there is no trainer, so (1) fails: at native defaults the act-path set is essentially all of it, and the groups are empty (census N: 0 optimizers).
   - (3) is already demonstrated above.
   - The old guard still PASSES on the defect: the status-quo "weights moved" check passes A_all and the all-ON e2 optimizer (measured), and `zworld_encoder_guard` cannot see those modules (D0).

**Runtime.** The same `GradReachGuard` runs inside the trainer, armed for each group's first N steps and re-armed on any config change. On FAIL it **raises**, because a dead group must stop the run, not annotate the manifest. After the window it disarms (the check is structural), so its steady-state cost is zero. Optionally, `experiments/_lib` gets a detection-only wrapper that existing drivers can attach to their own optimizers, writing the verdict into the manifest. That would retro-audit the ~40 recipe families without touching them.

## 4. Sequencing against the coupled defects (synthesis section 4)

### 4a. What can land on `main` alone

These are single-session, default-off or pure-instrument changes, each independently testable.

| # | change | why it is safe alone | test |
|---|---|---|---|
| M1 | `GradReachGuard` in ree_core (for example `ree_core/training/grad_reach_guard.py`) plus the contract test's canary and vacuity parts (3c.3, 3c.5) | pure instrument; changes no behaviour | canaries FAIL as pinned; controls PASS |
| M2 | `WakingTrainer` skeleton, default OFF, owning groups `e1`, `e2_self`, `e2_world` (all native losses already exist) with the guard armed | bit-identical OFF by structural absence; ON trains only modules whose losses already exist | 3c.2 and 3c.4 |
| M3 | `harm_eval` native regression group (map row 5) | new loss, but its target is already delivered to `update_residue`; OFF bit-identical | the guard PASSes on the group; held-out MSE beats a shuffled-target control |

These three make the **learner** exist. They do **not** repair the loop by themselves: E1, E2 and harm_eval trained on the agent's own monostrategy replay inherit that replay's action starvation (GFLAG-0485 addendum 2).

### 4b. What must land together on `integration/<slug>` (ree-v3, `ree_core` code plane only)

Each item below either failed alone or exposed the next defect it had been masking (synthesis section 4). CLAUDE.md's exception applies: the change spans several sessions, and its acceptance is joint.

1. **The whole codec, not the decoder alone** (GFLAG-0488/0490, SD-080):
   - an encoder objective for `e2.action_object_head`;
   - a decoder tied to it;
   - **bounded** decode before it is used as the rollout action (the post-hoc trace: decoded norm 50 -> ~370-1080 over 3 CEM iterations);
   - iteration-0 sampling inside the encoder's image (~12-13x off-range today);
   - `terrain_prior` trained against a grounded target, not E3 behavioural cloning.
   - These become new trainer groups (codec, prior) under the same guard.
   - Alternative, on the table in the synthesis: action-space proposals, which delete the codec instead of repairing it.
2. **E2 world-head action coverage.** Exploration coverage, not class-balanced replay (that repair is falsified).
3. **Grounded main-channel valuation.** The relative-to-null reward-hacking detector comes first (the harm-floor detector missed its positive control). Then channel calibration against grounded outcome.
4. **The rollout-depth question** (GFLAG-0485 / 0486): E3 scores on the informative depth, and the commit gate's input is fixed.
5. **Turning `use_native_waking_trainer` ON in the integrated config**, with every group (M2/M3 plus the codec and prior) guard-green.

M1-M3 land on `main` first. The branch is cut after them, so the branch's trainer is the one already on trunk.

### 4c. Pre-registered closed-loop acceptance criterion (proposed; to be fixed by the user / `/queue-experiment` before any run)

- **Seeds:** >= 5 fresh seeds. Each seed is classified **hazard-trapped** (>= 10 NATIVE early terminations in the first 600 steps) or **benign**, from NATIVE alone, written to a sidecar before any other arm is read. This is the decoder probe's protocol.
- **Arms:**
  - NATIVE: all flags off.
  - INTEGRATED: the branch config, trainer ON.
  - INTEGRATED-SHUF: identical, but every *grounding* target is permuted across timesteps with the class marginals kept. That covers the harm/benefit valuation targets, the decoder labels and the prior's grounding target.
  - INTEGRATED-FROZEN: the same config, trainer OFF after warmup. This isolates "learning during waking" from "better architecture".
- **Precondition, not a criterion:** every trainer group's guard verdict is PASS in every INTEGRATED arm. A guard FAIL makes the run **invalid** and it is re-run after the fix. It is never scored as a scientific FAIL.
- **P1, grounded outcome:** INTEGRATED env reward per 100 steps over the last 600 closed-loop steps exceeds NATIVE's on >= 4/5 benign seeds by more than max(2 x SD of the per-seed NATIVE-vs-reseeded-NATIVE delta, an absolute floor fixed at pre-registration), and is not worse on hazard-trapped seeds.
- **P2, not undirected:** in the benign stratum, INTEGRATED TRUE harm contacts per 100 steps (`agent_caused_hazard`, `env_caused_hazard`, `env_caused_multisource`) do not exceed NATIVE's by more than the same margin rule. Three tests tonight showed diversity without grounding buys harm.
- **P3, shuffled control:** INTEGRATED beats INTEGRATED-SHUF on P1 on >= 4/5 seeds.
- **P4, the loop closes:** INTEGRATED's reward gain from the first to the last 600-step window exceeds INTEGRATED-FROZEN's on >= 4/5 seeds. Later behaviour is changed by experience, which is the link this whole pass is about.
- **Reported, no criterion:** action entropy and class coverage, E2 action discrimination (addendum-1 metric), proposal state-dependence (m4), per-group held-out losses.

## 5. Read-only pre-flight on this design

Every loss relied on has a producer that runs, and every consumer is real.

| Row | Producer (file:line, runs?) | Consumer (read at act?) | Verdict |
|---|---|---|---|
| E1 | `compute_prediction_loss` `agent.py:11595`, over buffers filled natively in `sense()` (`:6294-6299`). **Ran:** loss 0.0109, `requires_grad`; guard PASS on E1-only, 2 seeds. | `e1_deep.py:1296 <- :2063` (census, read in N/A/B/C/Z) | GREEN |
| E2-self | `compute_e2_loss` `agent.py:12841`. **Ran:** 0.0035. Buffer filled by `record_transition`, which the harness calls, not the agent. | `e2_fast.py:198 <- :821` inside rollouts. But z_self has **no valuation consumer** (GFLAG-0481, 0/68 ticks). | AMBER. Buffer source must move into the trainer; D2 value is doubtful until 0481 is resolved. |
| E2-world | `compute_e2_world_loss` `agent.py:12859`. **Ran:** 2.72, `requires_grad`. | `e2_fast.py:221 <- :822`; E3 scoring and the ARC-016 gate input | AMBER. Trainable; action-blind under own-replay coverage until 4b.2 lands. |
| harm_eval | No native loss (to be written, M3). Target producer: `update_residue(harm_signal)` `agent.py:11196`, called once per step (`_harness.py:361`). Driver precedent trains it (census B: T). | `e3_selector.py:1386 <- :1678`, every E3 tick | GREEN (buildable; producer and consumer both real) |
| SD-070 P0a | `ZWorldP0Trainer` `zworld_p0.py:401`. **Ran:** guard PASS, 2 seeds. | `split_encoder.world_encoder` read every `sense()` | AMBER: SD-ZWORLD-SENSE-PATH-PARITY (trains on raw obs; the agent reads through `world_obs_encoder`) |
| ZSelfP0 | `ZSelfP0Trainer` `zself_p0.py:298`. **Ran:** guard PASS, 2 seeds. | GRU / `self_encoder` read under DR-13 | AMBER: same z_self consumer gap (GFLAG-0481) |
| codec / prior (rows 8-10) | **no loss exists** in ree_core | decoder `module.py:646 <- :2280` (192 calls per 12 steps); prior `:607 <- :2150` | RED until 4b.1 designs the objective |
| depth stack (row 11) | **no designed loss is wired** (`LatentStack.predict` `stack.py:1704`, no caller) | `stack.py:1430/1438 <- agent.py:5224` | RED, and probe-gated (z_beta consumer D2 owed) |
| REINFORCE heads (rows 12-14) | driver-only; `rule_bias_head` grad exactly 0 | all-ON only | RED for (i)/(ii); (iii)-only |

**Per option:**
- **(i): AMBER overall.** GREEN on the 4 rows it can own at once (E1, E2-self buffer fix, E2-world, harm_eval). RED on nothing it claims. RED rows are deferred with row ids by construction of 3c.1.
- **(ii): RED against the loop question** (no waking learning), GREEN as infrastructure.
- **(iii): RED as the general mechanism** (retained-graph hazard at `agent.py:5212-5222`), AMBER for the REINFORCE subset.

## 6. Options for the user and `/governance` (recommendation stated; nothing decided)

**D1. Trainer architecture.**
- (i) WakingTrainer.
- (ii) phased P0 only.
- (iii) online per-tick.
- hybrid: (i) spine, (ii) classes as scheduled members, (iii) only for REINFORCE heads.
- **Recommendation: the hybrid.** (ii) alone cannot close the experience -> update link. (iii) as a general mechanism re-imports the ARC-021 H2 graph hazard for no gain on rows 1-5.

**D2. Cadence and driver.** Where the trainer is stepped:
- stepped from `update_residue()` every K ticks;
- a separate `agent.waking_learn()` the harness must call;
- episode-end only.

**Recommendation:** `update_residue()`. Every StepHarness driver then gets it, with no driver edit. K is a config value, with a default of 1 during bring-up.

**D3. `world_obs_encoder`.**
- (a) FROZEN-PENDING allowlist entry, citing the parity spike's D1-benign measurement;
- (b) train it by moving SD-070 P0a onto the actual sense path (`body/world_obs_encoder -> latent_stack.encode`, as ZSelfP0's `_native_chain` does).

**Recommendation:** (b), folded into the SD-ZWORLD-SENSE-PATH-PARITY row, because it removes a train/serve mismatch.

**D4. Guard on FAIL:** raise (stop the run) or warn (annotate the manifest). **Recommendation: raise when the trainer is ON; warn-only in the `_lib` retro-audit wrapper for existing drivers.**

**D5. Landing.** M1-M3 on `main` first, then an `integration/<slug>` branch for the section 4b set. Alternatively, everything on the branch.

**Recommendation:** M1-M3 on `main` first. They are default-off or pure-instrument, and landing the guard first gives every later session the instrument.

**Registry consequences (to route via `/governance`; none made here):**
- the native trainer row (the census section 7 item 1; subsumes the E1 / E2-self / harm_eval gaps, GFLAG-0491);
- a harm_eval native-loss row, or fold it into the trainer row;
- terrain_prior's own row, or an SD-080 / GFLAG-0488 scope extension;
- the guard as a contract.

## 7. Limits

- The guard result is D1: reach, not influence.
- The budgets are tiny: 80 steps for A, 24 for the all-ON e2 group, 1 step for the all-ON P1 heads, whose verdicts are therefore not established here.
- Cost numbers are one Mac, 2 threads, native defaults, one seed.
- The G5 leak counts in the all-ON case can include stale grads from a *different* optimizer's backward within the same tick, because the recipe does not zero every module. They are reported, not relied on.
- The acceptance criterion in 4c is a proposal. Its margins and absolute floor are left to pre-registration.
- Nothing about the codec objective itself is designed here. That is the 4b.1 build's job.

## Probes and reproduction

**Scripts.** Copies are committed under `REE_assembly/evidence/planning/probes/trainer/`; originals are in `.scratch/breakthrough-20260924/trainer/`.
- `grad_reach_guard_proto.py`
- `guard_canary_probe.py`
- `trainer_cost_probe.py`

**Raw JSON:** `probes/trainer/results/guard_*_s{42,43}.json`.

**To reproduce:**
1. Put a ree-v3 worktree at `863d23d65a`, named `ree-v3-wt`, next to the scripts.
2. Run `/opt/local/bin/python3 guard_canary_probe.py {A_all|A_e1|A_stale|allon|zselfp0|vacuous} <seed>`, and `trainer_cost_probe.py`.

Each case takes < 1 min on the Mac.

## Addendum 2026-09-25: guard landed as an instrument (M1 only)

- **Session:** `bt0925-guard` (Worker M, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-grad-reach-guard-instrument`. **Evidence domain: D1** (a reach instrument). It shows that gradient reaches a tensor and the tensor moves. It does not show influence on any consumer.
- **Landed on ree-v3 `main` @ `ec1f5697f1`.** Two new files; no other file is touched:
  - `ree_core/utils/grad_reach_guard.py`: `check_grad_reach()`, `GradReachGuard`, `GradReachResult` / `TensorReach`, and `FROZEN_BY_DESIGN`.
    - The allowlist cites census 940c690c9dd plus this record's section 1b. Anchors were re-verified at ree-v3 `dbc6db8`.
    - **This is a pure instrument.** Nothing imports it, it raises nothing (it returns the verdict), no default changes, and there is no trainer and no call site.
    - Its observations run under `fork_rng`, so calling it does not change the RNG state (tested).
    - `optimizers=None` observes every optimizer that steps, through torch's global step pre-hook. That covers recipes that build their optimizer internally, for example `ZSelfP0Trainer.train()`.
  - `tests/contracts/test_grad_reach_guard.py`: 8 tests on the real `REEAgent` (dims 16, 6x6 grid).
    - (a) **Canary:** the V3-EXQ-1078 naive `Adam(agent.parameters())` recipe returns FAIL, naming `hippocampal.action_object_decoder`. The result matches the section 3b A_all row: 101 dead of 137 checked.
    - (b) **Canary:** the all-ON e2 optimizer plus `_e2_contrastive_step`, used verbatim from `experiments/_lib/allon_training.py` on a native-config agent. This is the smallest recipe that reproduces the E2-self dead entry. It returns FAIL, naming `e2.self_transition` and `e2.self_action_encoder` (and `e2.action_object_head`).
    - (c) `ZSelfP0Trainer` returns PASS on 17 tensors. The G5 leak onto the depth stack and `world_obs_encoder` is reported and pinned.
    - (d) The vacuous cases (zero steps, no optimizers, a global hook with nothing stepping, a short window, an all-allowlisted group) return CANNOT_DETERMINE and are asserted to be not PASS.
    - (e) The allowlist is necessary and specific: without it the check FAILs on exactly `write_gate`, and a planted wrong entry FAILs as stale.
    - (f) Byte-neutral.
    - The status-quo check "some weight in the optimizer moved" is pinned **green** on both canaries.
- **Tests ran on the hub, not the Mac.** All runs are from a worktree at base `dbc6db8` plus the two files:
  - `remote_pytest.sh tests/contracts/test_grad_reach_guard.py -q`: **8 passed in 8.72s**.
  - preflight plus the six ree_core/corpus-scanning lints: 129 passed.
  - `tests/contracts -q -k "import or config or lint"`: 1104 passed, 4 skipped.
  - The ree-v3 pre-commit gate (`precommit_contracts.sh`, full `tests/contracts` on the hub): **5670 passed, 50 skipped, 1 xfailed** (rc 0, 31 min).
- **Blind-spot measurement.** Three deliberately broken guards were each run against the unchanged test bodies. The runner (`.scratch/breakthrough-20260924/guard/guard_direct_runner.py`) calls the bodies directly, without pytest, on the Mac. None of the broken variants was committed.
  - grad `None` treated as nonzero: **5/8 tests fail**.
  - `result()` always returns PASS: **4/8 fail**.
  - CANNOT_DETERMINE removed: **1/8 fail**, which is test (d).
  - The restored guard passes 8/8, and its sha is unchanged.
  - The old guard is the status-quo "weights moved" check, and it stays green on both canaries, as asserted inside (a) and (b).
- **Still open. Nothing here decides these:**
  - **Q4a / D1:** the trainer architecture, and whether a trainer ships at all.
  - **Q4b / D2:** cadence and driver.
  - **Q4c / D3:** `world_obs_encoder`. It is deliberately **not** allowlisted, so its untrained state stays visible, reported as G5 leak or dead.
  - **Q4d / D4:** raise vs warn on a FAIL. The guard only returns the verdict.
  - M2 and M3, the `_lib` retro-audit wrapper, and the section 3c coverage test are not built.
  - GFLAG-0491 is untouched.

## Addendum (bt0925-wtrainer, 2026-09-25): Skeleton + harm_eval landed (default-OFF)

- **Session / chip:** `bt0925-wtrainer`, chip_ref `chip-20260925-waking-trainer-skeleton-build` (Worker O, `orchestrate-20260924-breakthrough`). User decisions applied (ledger rec-20260925-3677487d / 6eb5db00): D1 = the hybrid (Q4a); D5 = skeleton + harm_eval on `main`, default OFF (Q4b); D4 = the guard RAISES when the trainer is ON (Q4d, orchestrator under delegation). D3 (`world_obs_encoder`) out of scope.
- **Landed:** ree-v3 `origin/main` @ **`cc20be5`**. Files: `ree_core/utils/waking_trainer.py` (new), `ree_core/agent.py` (built at the end of `__init__` only when enabled; one guarded call in `update_residue` via `_waking_trainer_step`), `ree_core/utils/config.py` (7 additive fields + `from_dims` pops), `tests/contracts/test_waking_trainer.py` (new). Guard: `ree_core/utils/grad_reach_guard.py` from worker M (ree-v3 `ec1f5697f1`), imported, not vendored.
- **Flags** (all default no-op): `waking_trainer_enabled=False`, `waking_trainer_every_k=1`, `waking_trainer_harm_eval_lr=1e-3`, `waking_trainer_batch_size=16`, `waking_trainer_buffer_max=2000`, `waking_trainer_guard_min_steps=8` (0 disarms), `waking_trainer_seed=0`.
- **What it is.** `WakingTrainer` (plain object, not an `nn.Module`): member registry, one Adam per member group, a K-tick cadence on its own waking-tick counter, each update inside `torch.random.fork_rng` with a private torch RNG state swapped in and saved back (python `random` / numpy restored too), `torch.enable_grad()` so eval-mode (`no_grad`) harnesses still train. Waking-only: skipped when `hypothesis_tag` (MECH-094). ONE member registered: `HarmEvalMember` (map row 5). SD-070 P0 / ZSelfP0 / E1 / E2 are NOT registered; `WakingTrainerMember` is the seam for the coupled campaign.
- **harm_eval loss, and one premise corrected.** Section 1a row 5 says "regression of `harm_eval_head(z_world)` on `abs(harm_signal)`". `harm_signal` is the env reward (negative = harm, positive = benefit; `experiments/_harness.py` StepResult), so `abs` would train benefit steps as harm. The precedent the row cites (`goal_pipeline_tier1.py` harm_eval buffer append) clamps: target = `max(-harm_signal, 0)`. The build uses the clamp. Input: `agent._current_latent.z_world` detached (the latent sensed before the action whose consequence `harm_signal` is), the same pairing as the precedent; replay (P), not live latents; MSE on the head's sigmoid output.
- **Guard wiring.** One `GradReachGuard` per group, allowlist = the guard's explicit `FROZEN_BY_DESIGN` table (no entry overlaps the harm_eval group), armed for the group's first `waking_trainer_guard_min_steps` optimizer steps, observed before each `opt.step()`. At window close: FAIL raises `WakingTrainerReachError`; CANNOT_DETERMINE after a full window also raises (distinct message); then disarms.
- **Tests** (`tests/contracts/test_waking_trainer.py`, CPU-small, world_dim = self_dim = 32, 20 ticks): W1 OFF builds nothing (constructor patched to raise; `agent.waking_trainer is None`); **W2 OFF byte-identity**: a default-config StepHarness rollout equals the same rollout with `_waking_trainer_step` replaced by the pre-change behaviour (no call) on actions, per-tick z_world, full state_dict and torch/numpy/python RNG states; **W2b** the W2 comparison DETECTS an OFF hook that draws one `torch.rand` (not blind); W3i ON with a never-firing cadence is byte-identical to OFF (recording draws nothing); W3ii every ON update leaves global torch/numpy/python RNG identical; **W4 reach**: group == the 4 `e3.harm_eval_head` tensors, all move, guard PASS (`n_checked` 4); **W4b blind-spot measured**: with the loss disconnected (zero-sentinel, or detached prediction) and the guard disarmed, W4's own moved-check FAILS (0/4 moved) although the optimizer stepped >= 8 times; **W5** same disconnected losses with the guard armed: guard FAILs and the trainer raises `WakingTrainerReachError` naming `e3.harm_eval_head`; W5b allowlist == `FROZEN_BY_DESIGN`, no overlap with the group; W6 all 7 knobs land through `from_dims`. `tests/test_flag_inertness.py`: `waking_trainer_enabled` added to PROBED (its registry-currency test requires it); no existing assertion changed.
- **Default-OFF bit-identity, measured across trees (Mac, not a contract):** `bitid_probe.py` (scratch, `.scratch/breakthrough-20260924/wtrainer/`), 60 train-mode StepHarness ticks, grid 10, 3 hazards, world_dim = self_dim = 32, seed 42 (and 43): pre-change tree (clean origin/main `4cce9b8`, also `dbc6db8` and `6de633c` before each rebase) vs this build at default config -- identical action string, z_world hash, 200-key state_dict hash, torch/numpy/python RNG hashes and harm sum.
- **Liveness (D1), `liveness_probe.py` seed 42, 300 eval-mode ticks, grid 10, 4 hazards:** OFF vs ON (`waking_trainer_every_k=1`): harm_eval loss 0.154 (first 10 updates) -> 0.018 (last 10), 285 updates, guard PASS; the head's mean output on the rollout's own z_world falls 0.49 -> 0.09. It does NOT separate harm ticks from safe ticks (0.0936 vs 0.0929): at this budget it has learned the base rate, not a discrimination. The ON action stream first diverges from OFF at tick 66 (the head is read on the act path), direction not assessed -- no behavioural claim.
- **Full remote suite on the landed commit:** `remote_pytest.sh` (all six roots) on the rebased content (base `4cce9b8` + this change): hub, **6901 passed, 53 skipped, 1 xfailed, exit 0** (run `DLAPTOP-4-32603-20260925T080145Z-154196583`). After the final rebase onto `1fc8816`/`c3e38ca` (MECH-279 fix touched agent.py/config.py): `tests/contracts` on the hub **5729 passed, exit 0** (the landing commit's own gate, run `DLAPTOP-4-42066-20260925T101824Z`) plus the other five roots and `tests/` non-contract **1179 passed, exit 0** (hub, run `DLAPTOP-4-31276-20260925T100721Z`); bit-identity re-measured vs `c3e38ca`, seeds 42 and 43. The last rebase over `c763b60` + queue snapshots touched none of this change's files. An earlier worker-4 run showed 4 failures in `test_runner_merge_peer_status_source.py` / `test_validate_queue_burned_id_source.py` (real-corpus tests); the same 4 fail identically on clean origin/main `4cce9b8` on worker-4 (pre-existing, box-environment-dependent) and pass on the hub.
- **Domain: D1** (gradient reaches the harm_eval group, its weights move, guard PASS). No behavioural effect is claimed. Queue: nothing. Registry: untouched (GFLAG-0491's disposition belongs to `/governance`).
