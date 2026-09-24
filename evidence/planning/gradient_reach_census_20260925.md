# Gradient-reach census of the native agent: which parameters are silently untrained?

- **Written:** 2026-09-24T23:55Z. Session `bt0925-census` (Worker K, breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-gradient-reach-census`.
- **Scope:** probe only. Nothing lands in ree-v3, nothing is queued, no registry is edited, no chips are spawned.
- **Code under test:** ree-v3 `origin/main` @ **`863d23d65a`** (private detached worktree; includes the new `run_zself_p0`). All `file:line` citations are against that sha.
- **Probes:** `REE_assembly/evidence/planning/probes/census/`.
  - `census_instr.py`: global, non-perturbing instrumentation. It wraps `Optimizer.__init__`, adds a global optimizer step pre-hook, wraps `Tensor.backward` with a grad diff, and adds a `TorchFunctionMode` parameter-read tracer plus forward hooks.
  - `census_probe.py <recipe> <seed>`: runs one recipe.
  - `callsite_probe.py`: act-time call sites.
  - `summarize.py` and `matrix.py`: roll-ups.
  - Raw per-tensor JSON: `results/census_<recipe>_s42.json`.
  - To reproduce, put a ree-v3 worktree at `863d23d` named `ree-v3-wt` next to the scripts.
- **Run conditions:** Mac CPU, `torch.set_num_threads(2)`, seeds 42 and 43. Each recipe took 1-31 s of training.
- **Dims:** `world_dim = self_dim = 32`, the deployed value, in every recipe. `world_obs_dim` is set by each recipe's env, so `world_obs_encoder` has 62,750 or 90,300 parameters.
- **Evidence domains:**
  - **D1:** which tensors each recipe's losses reach and its optimizers move; which tensors are read on the act path.
  - **D0:** the consumer citations.
  - **Not D2.** Being read at act time is not the same as changing the selected action. This census says where random weights sit on the decision path, not how much each one matters.

## 0. Headline

1. **At `REEConfig` defaults the agent does no gradient learning while awake.**
   - 40 `StepHarness` ticks in train mode construct **0 optimizers**.
   - 99.9% of parameters (716,769 of 717,825) never change.
   - The only thing that moves is `residue_field.rbf_field`, and it moves by a non-gradient harm-accumulation rule.
   - ree_core has 13 native `compute_*_loss` methods. Only 4 carry gradient at defaults: E1 `compute_prediction_loss`, the E2 self head, the E2 world head, and `benefit_eval_head`. **Nothing native ever steps them.** The sleep-gated trainers are default-off (`config.py:7515`, `:7535`).
   - So **every trained parameter in REE is trained by a driver-built optimizer**, and each recipe trains a different subset.
2. **Every recipe leaves at least 6 randomly initialised modules on the act path.** No recipe trains everything the agent reads when it acts. This is the pattern tonight found five times by accident; here it is found by one systematic pass.
3. **New, not covered by any registered row:**
   - **(a) `E3.harm_eval_head` is untrained in 4 of 5 recipes**, including the all-ON production family.
     - It is read on every E3 tick through `compute_harm_cost_fallback` (`e3_selector.py:1386 <- :1678`).
     - The comment at that site says "TRAINED harm_eval_head".
     - No native waking loss exists for it. Only the tier1 driver loop trains it.
   - **(b) The all-ON recipe (14 of 69 recent drivers) trains no E1 and no E2 self head.** Both are read on every tick. E2 self is in the e2 optimizer, but its grad is `None` at 24/24 steps: the dead-optimizer pattern.
   - **(c) The beta/theta/delta depth stack plus its top-down connectors (22.6k params) is random in 4 of 5 recipes.** It is read on every `sense()` and is added top-down into z_world and z_self (`stack.py:1015-1017`, `:1430`/`:1438 <- agent.py:5224`).
   - **(d) `terrain_prior` is untrained in all 5 recipes and has no row of its own.**

## 1. Premises re-measured

| Premise (brief / earlier records) | Re-measured here | Verdict |
|---|---|---|
| `action_object_decoder` is never trained, anywhere; dead-optimizer pattern | Untrained in 5/5 recipes. Under V3-EXQ-1078's `Adam(agent.parameters())` it is in the optimizer, with grad `None` at **80/80** steps and parameter delta 0. | **Confirmed.** This is the canary, and it passes. |
| The DR-13 self GRU is untrained under E1/E2 | `latent_stack.self_recurrence`: grad `None` at 80/80 steps under the 1078 E1+E2 recipe (DEAD-OPT). It **does** train under `run_zself_p0` (863d23d). | **Confirmed.** Canary passes, and the positive control also passes. |
| The E2 world head is untrained in >= half of drivers | DEAD-OPT under the 1078 recipe (grad `None` 80/80) and untrained at native defaults. TRAINED under tier1 and all-ON. | **Consistent** with GFLAG-0485. |
| The z_world encoder is untrained "in regimes without SD-070 P0" | Tier1 `warmup_train` (V3-EXQ-1083) has **no** SD-070 P0, yet it trains `split_encoder.world_encoder` and the whole depth stack. The SD-018 proximity aux loss flows through the live latent into its `latent_stack.parameters()` optimizer (`goal_pipeline_tier1.py:537`, `:570`). Only the 1078-style E1/E2 recipe and native defaults leave it untrained. | **Corrected.** The right split is "trained by SD-070 P0 or by a live-latent aux loss", not "SD-070 or nothing". |
| `terrain_prior` is trained by drivers only | Untrained in all 5 recipes here. The 042-family driver-only BC trainer was not re-run; see `action_decoder_training_trace_20260924.md`. | **Confirmed** for these recipes. |
| All-ON optimizer groups are e2 (18), lpfc (4) and ofc (4), plus SD-070 P0a (17) (Worker A) | Exactly those 4 optimizers are constructed. P0h is opt-in and off. | **Confirmed.** |

## 2. Recipes

The census covers native defaults plus 4 driver recipes. The drivers were picked among recent fleet-run drivers so the set spans the recipe families.

A grep-based tally over the 69 drivers `v3_exq_1030..1097`:
- all-ON (`allon_training`): 14
- own hand-rolled loop: 23
- no training call visible in the driver: 24, not traced further
- SD-070-only: 3
- tier1: 3
- `committed_mode_curriculum`: 1
- `Adam(all)`: 1

| tag | recipe | fleet run it reproduces | optimizers (construction site) |
|---|---|---|---|
| N | native `REEConfig.from_dims` defaults | none (native baseline) | none |
| A | V3-EXQ-1078 P0 verbatim: DR-13 config; `Adam(agent.parameters())` on E1 + E2 losses | `v3_exq_1078_..._20260923T182046Z` | 1 (all 141 tensors) |
| B | V3-EXQ-1083: mech477 `build_arm_agent(ARM_ON)` + `goal_pipeline_tier1.warmup_train` | `v3_exq_1083_..._20260924T172346Z` | 4: e1, e2 world, harm_eval, latent_stack aux (`goal_pipeline_tier1.py:529/530/535/537`) |
| C | all-ON stack (`x1002._make_agent`) + `x734._train_all_on_agent` with SD-070 P0a (the 1043b/1002/1008/1010 path) | `v3_exq_1043b_..._20260922T204547Z` | 4: `zworld_p0.py:577`, `allon_training.py:572/574/578` |
| Z | 1078 DR-13 config + `run_zself_p0` (863d23d; no driver uses it yet) | none (new) | 1 (`zself_p0.py:724`, 17 tensors) |

**Budgets are deliberately tiny** (2 episodes x 40-60 steps; all-ON p0 = p1 = 1). This measures reach, not training quality. Every recipe optimizer stepped at least once. Backward counts: A 80; B 14-47 per site; C 16/24/1/1; Z 8.

**Seed stability.** Every per-tensor class and every read flag is **identical at seed 43** across all 5 recipes (0 differences).

All-ON was also re-run at 6 x 100 P1 steps (`census_allon_long_s42.json`). That run resolves the one budget-limited tensor group, `lateral_pfc.rule_bias_head` (section 4).

## 3. Census table

Tensors are grouped at depth 2. Codes:
- **T** = TRAINED: in an optimizer, nonzero grad at a step, moved.
- **D** = DEAD-OPTIMIZER: in an optimizer, grad `None` or 0 at every step, never moved.
- **O** = ORPHAN: in no optimizer, never moved.
- **G** = non-gradient update.
- **M(...)** = mixed tensor counts.
- **-** = module not built in that config.

"read at act" means the module's parameters were touched during 12 act steps (`sense -> e1 tick -> generate_trajectories -> select_action`, `no_grad`), in the listed recipes.

| module | params | N | A 1078 | B 1083 | C all-ON | Z zself-P0 | read at act (recipes) |
|---|---:|---|---|---|---|---|---|
| `latent_stack.split_encoder` | 25761 | O | D | M(D2/T14) | M(O11/T7) | M(O7/T7) | N,A,B,C,Z |
| `latent_stack.beta_encoder` | 9472 | O | D | T | O | O | N,A,B,C,Z |
| `latent_stack.theta_encoder` | 6816 | O | D | T | O | O | N,A,B,C,Z |
| `latent_stack.delta_encoder` | 4224 | O | D | T | O | O | N,A,B,C,Z |
| `latent_stack.delta_to_theta` / `theta_to_beta` / `beta_to_split` | 2096 | O | D | T | O | O | N,A,B,C,Z |
| `latent_stack.{self,world,beta,theta,delta}_predictor` | 8384 | O | D | D | O | O | none |
| `latent_stack.self_recurrence` (DR-13 GRU) | 6336 | - | **D** | - | - | T | A,Z |
| `latent_stack.harm_encoder` / `affective_harm_encoder` | 10369 | - | - | D | O | - | none |
| `e1.transition_rnn` / `output_proj` / `prior_generator` | 408928 | O | T | T | **O** | O | N,A,B,C,Z |
| `e1.context_memory` | 59840 | O | M(D2/T8) | M(D2/T8) | O | O | N,A,B,C,Z |
| `e2.self_transition` / `self_action_encoder` | 25534 | O | T | O | **D** | O | N,A,B,C,Z |
| `e2.world_transition` / `world_action_encoder` | 9022 | O | **D** | T | T | O | N,A,B,C,Z |
| `e2.action_object_head` | 6928 | O | D | O | D | O | N,A,B,C,Z |
| `residue_field.rbf_field` | 1056 | G | G | G | O* | O* | N,A,B,C,Z |
| `residue_field.neural_field` | 6337 | O | D | O | O | O | N,A,B,C,Z |
| `e3.harm_eval_head` | 2177 | O | **D** | T | **O** | O | N,A,B,C,Z |
| `e3.reality_scorer` / `harm_cost_fallback_scorer` / `benefit_eval_head` / `harm_eval_z_harm_head` | 8708 | O | D | O | O | O | none |
| `hippocampal.terrain_prior` | 70368 | O | D | O | O | O | N,A,B,C,Z |
| `hippocampal.action_object_decoder` | 2821 | O | **D** | O | O | O | N,A,B,C,Z |
| `body_obs_encoder.0` | 306 | O | D | O** | O | T | N,A,B,C,Z |
| `world_obs_encoder.0` | 90300 | O | D | O** | O | O** | N,A,B,C,Z |
| `lateral_pfc.delta_proj` / `world_proj` | 1056 | - | - | - | O (by design) | - | C |
| `lateral_pfc.rule_bias_head` | 1601 | - | - | - | D (grad exactly 0) | - | C |
| `ofc.state_bias_head` | 1601 | - | - | - | O (by design, output zeroed) | - | C |
| `ofc.devaluation_bias_head` | 1601 | - | - | - | T | - | none in 12 steps |
| `gated_policy.head_0` / `head_1` / `discriminator` | 4147 | - | - | - | **O** | - | C |
| `ofc.outcome_proj`, `lateral_pfc.discriminator_proj` | 560 | - | - | - | O | - | none |

Notes on the table:
- \* The rbf_field has no harm event inside the tiny C/Z budgets. It is a non-gradient rule by design (G), not a defect.
- \*\* **Gradient reaches the module, but the module is in no optimizer.**
  - In B, the tier1 aux loss reaches `world_obs_encoder` / `body_obs_encoder`, but they are top-level agent attributes, not `latent_stack` members. So the aux optimizer (`goal_pipeline_tier1.py:536`) omits them and the gradient is discarded.
  - In Z, the P0s loss also reaches the depth stack and `world_obs_encoder`, which its 17-tensor optimizer deliberately excludes.
- **Share of parameters never moved:**
  - N: 99.9%
  - A: 31.6% DEAD-OPT, plus 2 dead context_memory tensors
  - B: 27.9% ORPHAN plus 2.1% DEAD-OPT
  - C: 90.8% ORPHAN plus 4.6% DEAD-OPT
  - Z: 96.0% ORPHAN (Z is a single-module warmup by design)

**Native act-time call sites** (`callsite_probe.py`; identical in N and C unless noted):

| module | call site |
|---|---|
| decoder | `hippocampal/module.py:646 <- :2280` (192 calls per 12 steps) and `:816 <- :2767` |
| terrain_prior | `module.py:607 <- :2150` |
| harm_eval_head | `e3_selector.py:1386 <- :1678` (64) |
| E2 world / self / action-object heads | `e2_fast.py:221 <- :822`, `:198 <- :821`, `:691 <- :813` (5760 each) |
| neural_field | `residue/field.py:661 <- e3_selector.py:1406` and `<- module.py:1775` |
| depth stack | `stack.py:1430`/`:1438 <- agent.py:5224`; `world_topdown` at `stack.py:1017 <- :1444` |
| obs pre-projections | `agent.py:5188`/`:5189` |
| E1 | `e1_deep.py:1296 <- :2063` |
| gated_policy (C only) | `gated_policy.py:591`/`:535 <- agent.py:8350` |
| ofc.state_bias_head (C only) | `ofc_analog.py:320 <- agent.py:8603` |
| lpfc.rule_bias_head (C only) | `lateral_pfc_analog.py:473 <- agent.py:8542` |

## 4. Random (DEAD-OPT or ORPHAN) modules read on the act path: the list that matters

Every row below is a random projection sitting in the decision path under the named recipes. "Covered" means a registered row or flag already owns it.

| # | module | untrained under | covered by | status |
|---|---|---|---|---|
| 1 | `hippocampal.action_object_decoder` | N A B C Z (all) | GFLAG-0488 (decoder half), SD-080 (encoder half) | covered |
| 2 | `e2.action_object_head` | all | SD-080 | covered |
| 3 | `hippocampal.terrain_prior` | all 5 (trained only by the 042-family BC driver) | named only inside `sd_zself_training_path` text and the GFLAG-0488 trace; **no row of its own** | **gap** (extend GFLAG-0488/SD-080 scope, or a sibling row) |
| 4 | `residue_field.neural_field` | all (native trainer `field.py:1262` is flag-gated) | `residue-cost-untrained-neural-field` (pending_implementation) | covered |
| 5 | `world_obs_encoder` | all | SD-ZWORLD-SENSE-PATH-PARITY. Its spike measured the random `Linear+ReLU` as benign for z_world decodability (`zworld_sense_path_parity_spike_20260916.md` sec 2). | covered; measured benign at D1 |
| 6 | `body_obs_encoder` | all except Z | `sd_zself_training_path` / 863d23d | covered |
| 7 | `latent_stack.self_recurrence` (DR-13) | A (and any E1/E2-only recipe) | `sd_zself_training_path` / 863d23d | covered; Z trains it |
| 8 | `split_encoder.world_encoder` | N, A | SD-070 (and tier1's aux loss) | covered |
| 9 | `e2.world_transition` | N, A, Z | GFLAG-0485 (R1 native waking objective) | covered |
| 10 | **`e3.harm_eval_head`** | N, **A, C**, Z | none found. SD-E3-SCORER-COMPLETION covers `reality_scorer` / `harm_cost_fallback_scorer`; SD-PP-B9 covers the harm-forward head. | **NEW gap** |
| 11 | **E1** (transition_rnn, prior_generator, output_proj, context_memory) | N, **C (all-ON)**, Z | none. E1's selection reach is through `terrain_prior` (#3), per `zself_causal_reach_trace_20260924.md` | **NEW gap** (recipe-level) |
| 12 | **`e2.self_transition` / `self_action_encoder`** | N, B, **C (DEAD-OPT: in the e2 optimizer, grad `None` 24/24)** | none | **NEW gap** (recipe-level) |
| 13 | **depth stack**: `beta/theta/delta_encoder`, `delta_to_theta`, `theta_to_beta`, `beta_to_split`, `split_encoder.world_topdown` / `self_topdown` | N, A, C, Z (trained only by the tier1 aux loss) | none by name. SD-ZWORLD-SENSE-PATH-PARITY measured "top-down + reafference + EMA" as ~0 cost to z_world decodability. That measures one consumer. The z_beta consumers themselves (SD-036, MECH-307, ARC-071 rows) were not checked here. | **NEW gap**, lower priority |
| 14 | `gated_policy.head_0` / `head_1` / `discriminator` | C | ARC-062 / SD-082 rows mention gated_policy. Its only trainer found is the `exq610` baseline REINFORCE (driver-only). Not confirmed that those rows own training. | **check coverage** |
| 15 | `lateral_pfc.rule_bias_head` | C: in its optimizer, but grad is **exactly 0** (not `None`) at 1/1 and 6/6 REINFORCE steps | SD-082 (implemented_pending_validation). Consistent with the known constant-candidate-summary degeneracy (`lateral_pfc_analog.py:429-440`), which makes the softmax shift-invariant. Mechanism not verified here. | covered (D1 only) |

Rows that look random but are **frozen by design** (documented, not defects):
- `lateral_pfc.delta_proj` / `world_proj`: "frozen-random; not trained in landing" (`lateral_pfc_analog.py:233-236`).
- `ofc.state_bias_head`: its last layer is zeroed when `train_state_bias_head=False`, so it outputs 0 (`ofc_analog.py:201-215`).
- `residue_field.rbf_field`: non-gradient accumulation.

Inert rows (never read at act, never trained, so not on the decision path in these configs; no action):
- the five `latent_stack.*_predictor` heads
- `e3.reality_scorer`, `harm_cost_fallback_scorer`, `benefit_eval_head`, `harm_eval_z_harm_head`
- the harm encoders
- `ofc.outcome_proj`, `lpfc.discriminator_proj`

**Driver-only training** (parameters that drivers train but ree_core never steps natively), measured here:
- E1: A, B. ree_core has the loss but nothing steps it.
- `e2.world_transition`: B, C. The native trainer is sleep-gated and default-off.
- `e3.harm_eval_head`: B only. There is no native loss at all.
- The depth stack: B only, via the aux loss.
- `split_encoder.world_encoder`: B, C. The SD-070 trainer class is in ree_core, but only drivers invoke it.
- The DR-13 GRU and `body_obs_encoder`: Z only. Same pattern: a ree_core trainer that drivers invoke.
- lpfc / ofc bias heads: C.
- From the trace, not re-run: `terrain_prior` (042 family).

Only `residue_field.rbf_field` changes under ree_core's own control.

## 5. Canaries (a census is a negative instrument)

- **Negative canaries.** Each must re-find a known untrained module. All pass:
  - `action_object_decoder` untrained in 5/5 recipes, as DEAD-OPT with grad `None` 80/80 under A.
  - The DR-13 GRU untrained under the E1/E2 recipe A (DEAD-OPT, `None` 80/80).
  - The E2 world head untrained under A (the Worker D B-harness condition).
  - `terrain_prior` untrained in 5/5.
- **Positive canaries.** The instrument must see training when it happens. All pass:
  - E1 moves under A and B.
  - The GRU moves under Z. So a GRU delta is visible, and the A negative is real.
  - `world_encoder` moves under the C P0a.
  - `harm_eval_head` moves under B.
- **Read-detector canaries.** All pass:
  - The decoder is read (call site `module.py:2280`, as cited by the decoder trace).
  - The GRU is read under DR-13.
  - The five `*_predictor` heads are never read. They are the negative control, and the reads are consistent with them having no act-path call site.
- **Denominators:** 137 / 141 / 149 / 185 / 141 tensors classified for N/A/B/C/Z. Every tensor gets a class; there is no cannot-determine bucket left.
  - One native loss, `compute_schema_readout_loss`, returns `NO_GRAD` at defaults.
  - Eight native losses return a constant 0 with empty reach at defaults: self_maintenance, event_contrastive, resource_proximity, resource_field, resource_encoder, resource_identity, harm_nonredundancy, harm_accum. Their heads or flags are off.

## 6. Limits

- **Reach, not influence (D1).** "Read at act" means parameters were touched on the act path. Whether perturbing each module changes the committed action (D2) was not measured here. For z_self it is known to be no (Worker A). For the decoder it is known to be yes (Worker J).
- The act pass is 12 steps. A module used only on rare events (devaluation, harm contact, sleep) can read "not read" when it is in fact read. A "read" flag is stronger evidence than a "not read" flag.
- Budgets are tiny. A class of TRAINED means the recipe can move the tensor, not that it trains it well.
- The recipe-family tally is grep-based. The 24 "no visible training" drivers were not traced; they may import other trainers.
- The 042-family terrain_prior BC trainer and the `committed_mode_curriculum.run_p0_warmup` recipe (V3-EXQ-1089) were not run. By code, the latter builds E1 plus E2-world optimizers only (`committed_mode_curriculum.py:266-269`), so its class pattern should match A for E1 and B for the world head. That is D0, unmeasured.
- B used one familiar layout. C used the x1002 rung env.

## 7. What would warrant a substrate_queue row (route: `/governance`; nothing registered here)

1. **(systemic, recommended first) A native waking trainer.** ree_core owns no waking optimizer, so which modules get trained is left to whichever recipe a driver uses, and every recipe leaves act-path modules random. One row, owning the waking optimizer set in the agent loop, would subsume items 10-12 and GFLAG-0485's R1.
   - Classification: `complicated (buildable)`.
   - Hazard: the naive `Adam(agent.parameters())` form reproduces recipe A's 31.6% DEAD-OPT. The row must state, per module, which loss reaches it.
2. **`E3.harm_eval_head` has no native trainer.** It is untrained in 4/5 recipes, including all-ON, and read at every E3 tick under a comment asserting it is trained. `complicated (buildable)`.
3. **The all-ON recipe omits E1 and the E2 self head.** This is a recipe-level evidence discrepancy (`governance_flag.py --flag-type evidence_discrepancy` on the all-ON-family claims) more than a substrate build. It is subsumed by item 1 if item 1 lands.
4. **`terrain_prior` has no row of its own.** Extend GFLAG-0488 / SD-080 so the codec repair covers the proposal prior too, or add a sibling row.
5. **The depth stack (z_beta/theta/delta) is random in 4/5 recipes.** Registration-only until a consumer-reach check (D2) on the z_beta consumers shows it matters. This is `complex (probe-gated)`.
6. **Check whether ARC-062 / SD-082 own `gated_policy` head training** in the all-ON family. If they do not, register it.

Already covered, so no new row: decoder (GFLAG-0488), `action_object_head` (SD-080), DR-13 GRU and `body_obs_encoder` (`sd_zself_training_path` / 863d23d), `world_encoder` (SD-070), E2 world head (GFLAG-0485), `neural_field` (`residue-cost-untrained-neural-field`), `world_obs_encoder` (SD-ZWORLD-SENSE-PATH-PARITY), `reality_scorer` / `harm_cost_fallback_scorer` (SD-E3-SCORER-COMPLETION), harm encoders (`sd_zharm_a_warmup_optimizer_group`), `lpfc.rule_bias_head` (SD-082).

Bearing on **MECH-523** ("designated compression sites are systematically UNTRAINED"): consistent, and broader. The pattern is not confined to compression sites. At defaults it covers every learned module except the residue RBF. Under the production recipes it covers 28-91% of parameters, including modules on the act path.
