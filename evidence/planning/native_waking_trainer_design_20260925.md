# A ree_core-owned native waking trainer with a gradient-reach guard -- design (no build)

- **Status: INTERIM (step 1 of 5: module -> loss map).** Written 2026-09-25T00:05Z. Session `bt0925-trainer` (Worker L, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-native-waking-trainer-design`.
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
