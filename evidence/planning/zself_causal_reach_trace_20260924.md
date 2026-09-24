# z_self causal-reach trace: the earliest broken edge is downstream of the training gap

- **Written:** 2026-09-24T18:15Z by `bt0924-zself-trace` (Worker A, breakthrough integration pass, orchestrator `orchestrate-20260924-breakthrough`), chip `chip-20260924-zself-causal-reach-trace`.
- **Code base:** a throwaway ree-v3 worktree at `origin/main` **`00210b562c`**. Every `file:line` below refers to that commit.
- **Probes:** `REE_assembly/evidence/planning/probes/zself/` (`zs_common.py`, `probe1_loss_reach.py`, `probe2_intervention.py`, `probe3_objectives.py`, `probe4_closed_loop.py`). Compact results are in `zself_probe_results_summary.json` in the same directory. Each probe was run with cwd = the worktree and `torch.set_num_threads(2)`.
- **Configs:** self_dim = world_dim = 32 (deployed values) in both.
  - **A** = the V3-EXQ-1078 config: DR-13 ON, coupling 0.15, per-stream V_s, `CausalGridWorldV2` size 10, 2 hazards.
  - **B** = the V3-EXQ-724 all-ON production stack: `x724._base_config_kwargs + _all_on_extra_kwargs` with its size-12 reef env. DR-13 is OFF, as in production.
- **Held build:** `chip-20260924-sd-zself-training-path-build` (`sd_zself_training_path`) inherits Sections 6-8.

## 0. Headline

**The earliest broken NATIVE edge for z_self is downstream of the training gap.** At act time, no native consumer turns z_self into a change in selection. This holds untrained, E1/E2-trained, after a working z_self objective, and in the production all-ON stack.

- **z_self, one-tick intervention:**
  - Swap, zero, matched-norm noise or permute on z_self changed the committed action at **0 of 68 E3 ticks** after a working z_self objective.
  - It changed the action at 0/56 in production config B, and at <=1/56-1/66 in config A.
  - E3 scores moved 0.15-1.0%. That is at the control-vs-control determinism floor (mean up to 0.67%).
- **z_self, persistent closed-loop intervention:** zeroing or noising z_self on every tick for whole episodes changed **0 actions in 12/12 episodes**, and harm was identical.
- **z_world canary, the same harness:**
  - One-tick: noise/swap/permute changed 4-30% of E3-tick actions.
  - Closed loop: the first action divergence came at tick 0-6.
- **So the harness is sound, and the z_self negative is real.**

The one native consumer that does respond to z_self is **E1**: a z_self swap moves the E1 prior 0.6% before training and 5-7% after the forward-model objective (D2 at E1). But E1's output reaches selection only through `hippocampal.terrain_prior`. That is an MLP no loss in `ree_core` trains, and it sets only the CEM initial action-object mean. E3 scores `world_states` only. The designed z_self->E3 consumer (DR-10) is OFF by default, and it is an injection seam with no z_self-derived producer.

**Consequence for the held build.** Building the P0 z_self objective first produces a trained self-state that E1 reads and nothing behavioural uses. The objective is still worth building, and one form clearly works (Section 5). But the build's acceptance cannot include behavioural consequence. The missing consumer is a separate `complicated (buildable)` node the orchestrator should see: a z_self -> per-candidate valuation producer.

Domain reached:

| Chain | Domain | What was established |
|---|---|---|
| z_self -> selection | **D3-negative** | Closed-loop intervention changes nothing |
| z_self -> E1 prediction | **D2** | E1 responds to the intervention |
| z_self objective (fwd) | **D1 + D2 at E1** | Held-out information gain; E1 response rises about 10x |
| z_world -> E1 and E3 selection | **D2 reached**, with a D3-direction signal | See Section 4 |

## 1. Premises re-measured (and corrected)

| Premise (source) | Re-measured | Verdict |
|---|---|---|
| DR-13 doc: the GRU "trains via the existing E1/E2 z_self prediction losses" | probe 1: E1 -> `e1` only (28 tensors), E2-self -> `e2` (8), E2-world -> `e2` (6). 0 z_self-path tensors. | **False** (confirms 1078) |
| Build chip / autopsy: "no loss reaches self_encoder" | probe 1: the **undetached world-side** auxiliaries do reach `self_encoder` (4 tensors) + `self_precision_logit` through the z_beta top-down path (`stack.py:1411-1440`, `1444`). These are `harm_eval(live z_world)` and SD-018 `compute_resource_proximity_loss(live latent)`. They never reach the GRU or `self_topdown`. | **Partly false.** The true statement is that no loss reaches the GRU, and none is a z_self objective. |
| Production drivers train the z_self path somewhere | The all-ON recipe (`experiments/_lib/allon_training.py:572-579`) builds its optimizer groups over e2 (18), lpfc bias head (4) and ofc deval head (4). SD-070 `world_path_parameters` (`zworld_p0.py:468-478`) covers 5. **0 z_self-path members** across all of them. P0h trains the affective harm encoder only. | False: nothing trains z_self in production |
| MECH-113 `compute_self_maintenance_loss` pushes on z_self | NO GRAD. It reads `_current_latent.z_self` (`agent.py:12821`), which is detached at `agent.py:5855`. | Confirms GFLAG-0400 (known) |
| Detach sites cited in autopsy/pre-flight (~5721, ~6155-6172) | Drifted. At `00210b5` they are `agent.py:5855` (`_current_latent = new_latent.detach()`), `6294` (`_self_experience_buffer`) and `11397` (`record_transition`). | Line drift only |
| GFLAG-0414 / autopsy: "z_self reaches no behaviour (DR-10 inert)" | Re-measured with interventions (Section 3), and extended to the production stack and to trained z_self. | **Confirmed and generalised** |

## 2. LOSS -> PARAMETERS (probe 1; seed 42; 40 grad-enabled StepHarness ticks)

z_self path = `body_obs_encoder`, `split_encoder.self_encoder`, `self_topdown`, `self_precision_logit`, `self_recurrence.cell` (GRU).

The synthetic `sum(live z_self)` row is the upper bound: the graph exists on the live latent `sense()` returns (`agent.py:6226`). Every stored copy is detached.

| Loss / optimizer | Stepped by | z_self-path tensors with nonzero grad |
|---|---|---|
| E1 `compute_prediction_loss` | 1078 P0; many drivers | 0 (replay over detached buffers, `agent.py:6294-6295`) |
| E2 `compute_e2_loss` | 1078 P0 | 0 (`_e2_transition_buffer` detached, `agent.py:11397-11399`) |
| E2 `compute_e2_world_loss` | sleep / some drivers | 0 |
| SD-056 e2 contrastive | all-ON P0b | not in optimizer (e2-only group + clip) |
| lpfc / ofc REINFORCE heads | all-ON P1 | not in optimizer |
| SD-070 `ZWorldP0Trainer` | all-ON P0a | not in optimizer (world path only) |
| SD-011 `compute_harm_accum_loss(live latent)` | P0h / some drivers | 0 (reaches 6 affective-encoder tensors) |
| SD-018 `compute_resource_proximity_loss(live latent)` | some drivers | **self_encoder x4 + self_precision_logit** (top-down); GRU 0 |
| `harm_eval(live z_world)` | e.g. the ARC-021 MERGED spark | **self_encoder x4 + self_precision_logit**; GRU 0 |
| MECH-113 self-maintenance (w=1) | 075 / 142 lineage | no graph at all |
| SYNTHETIC `sum(live z_self)` | none | 11 incl. GRU (the path exists) |
| SYNTHETIC `sum(_current_latent.z_self)` | none | no graph |

Distinction asked for:

- **GRU and `self_topdown`:** not in any production optimizer, and no loss reaches them.
- **`self_encoder`:** in the optimizer only in `agent.parameters()` drivers such as 1078. It receives gradient there only from undetached world-side auxiliaries, and 1078 steps none of them. So it had zero grad in 1078.
- **E1/E2 losses:** grad is detached upstream.

## 3. Z_SELF -> NATIVE CONSUMERS

### 3a. Read sites (code, D0)

| Consumer | Read site | Default | Reaches selection? |
|---|---|---|---|
| E1 input `[z_self, z_world]` | `agent.py:6288-6290` -> `e1(...)` `6362` | ON | only via e1_prior -> `hippocampal.terrain_prior` (`module.py:562-606`, used `2150`): the CEM initial ao_mean. No loss in ree_core trains `terrain_prior`. |
| E2 self rollout in proposals | `agent.py:6598` -> `module.py:2285` -> `e2_fast.py:821, 838` | ON | **No.** E3 scores `world_states` (`e3_selector.py:1305-1321`). z_self couples to the z_world rollout only via `cross_stream_binder` (`e2_fast.py:156-159, 819-828`), default None. |
| DR-10 self-viability in E3 | `e3_selector.py:1792ff`; flag `config.py:2132` | OFF (v4) | Injection seam only. `set_injected_self_viability` (`agent.py:4249-4262`) says the z_self-derived producer is "the documented follow-on". **No producer exists.** |
| GatedPolicy discriminator | `agent.py:8350-8352` | OFF (ON in all-ON B) | Measured 0 reach in B (Section 3b); GFLAG-0414 records rank-invariance |
| TPJ efference comparator | `agent.py:4185-4221`; `config.py:4621` | OFF | agency readout |
| Blocked agency (MECH-353) | `agent.py:4441-4624`; `config.py:6236` | OFF | readout |
| ContextMemory write / SD-CM-LIVETAP | `agent.py:5800-5804`, `5843` | write ON (detached), tap OFF | memory content only |
| MECH-089 theta buffer | `agent.py:6382` | ON | `summary()` returns z_world only (`agent.py:6503`) |
| Event segmenter, BLA remap, escape-affordance learners | `agent.py:5898`, `5655-5704`, `5398`, `5450`, `9164`, `9224` | OFF | n/a |
| Stateful z_self -> z_beta/z_theta/z_delta | none: the shared stack reads the INSTANTANEOUS first-pass encoder output (`stack.py:1411-1412`) | n/a | No |

### 3b. Intervention (probe 2, D2; probe 4, D3)

**Design:**

- Fork (agent, env, harness) by deepcopy at each branched tick and restore the torch/numpy/python RNG.
- Replace one stream in `LatentStack.encode()`'s output for that tick. Every reader sees it: live latent, `_current_latent`, buffers, E1, proposals.
- Compare with a matched-RNG control, plus a control-vs-control determinism replay.
- Interventions:
  - zero;
  - matched-norm random direction (dedicated Generator, so the global RNG is untouched);
  - swap with the same stream from another episode of the same agent;
  - dimension permutation. This stands in for "shuffle across batch": batch is 1.
- Action change is counted at E3 ticks. Between E3 ticks the committed plan executes (`clock.py:142-151`, `e3_steps_per_tick` 10).

**One-tick branch.** Each cell is committed-action change rate at E3 ticks / E3 score rel-L2 change / E1 prior rel change.

| Condition (seeds; E3 ticks) | z_self zero | z_self noise | z_self swap | z_self permute | z_world zero | z_world noise | z_world swap | z_world permute |
|---|---|---|---|---|---|---|---|---|
| A untrained (42,43,45; 56) | 1.8% / 0.25% / 25% | 1.8% / 0.31% / 31% | 1.8% / 0.38% / 5.0% | 1.8% / 0.45% / 31% | 1.8% / 0.57% / 14% | 7.1% / 3.1% / 21% | 7.1% / 3.0% / 3.3% | 10.7% / 3.9% / 22% |
| A E1/E2-trained (42,43; 66) | 0 / 0.19% / 22% | 0 / 0.27% / 22% | 1.5% / 0.34% / 0.6% | 1.5% / 0.41% / 22% | 1.5% / 1.4% / 11% | 7.6% / 4.2% / 11% | 7.6% / 4.5% / 1.7% | 6.1% / 6.7% / 11% |
| A fwd-objective + E1/E2 (42,43; 68) | 0 / 0.77% / 66% | 0 / 0.85% / 70% | **0 / 0.93% / 6.3%** | 0 / 1.0% / 68% | 1.5% / 1.7% / 4.6% | 4.4% / 3.9% / 4.5% | 4.4% / 4.3% / 0.4% | 5.9% / 6.6% / 4.3% |
| **B production all-ON, untrained (42,43; 56)** | **0** / 0.15% / 20% | **0** / 0.16% / 27% | **0** / 0.23% / 3.0% | **0** / 0.25% / 27% | 23% / 2.0% / 15% | 30% / 3.7% / 23% | 14% / 3.7% / 1.6% | 29% / 5.3% / 22% |

**Notes on the table:**

- **Determinism:** control replays gave the identical action in 100% of every run.
- **E3 score determinism floor:** mean 0.015% / 0.10% / 0.67% / 0.07%, max up to 5.5% (A fwd-trained).
- **The A-untrained 1.8% z_self rate** is one tick. The same tick also flips under z_world-zero, so it is a near-tie, not z_self reach.
- **Candidate first-step world-state change:**
  - z_self: 1-5%. It reaches through the terrain prior -> CEM mean, and gets washed out by CEM/scoring.
  - z_world: 3-27%.
- **Natural z_self spread** (mean pairwise distance / mean norm, over one episode): A 0.04-0.06, B 0.17-0.29, A fwd-trained 0.07-0.14. Untrained, z_self is nearly a constant (effective rank ~1.1-1.2, Section 5).

**Closed loop (probe 4).** z_self or z_world is replaced on EVERY encode for a whole episode (up to 150 ticks), with matched start and RNG.

| Condition | z_self zero / noise | z_world zero / noise |
|---|---|---|
| B production (42,43 x 3 eps) | **0 action differences, identical harm, 6/6 eps** | first divergence tick 0-3; 36-67% of actions differ; harm changes |
| A fwd-trained (42,43 x 3 eps) | **0 action differences, identical harm, 6/6 eps** | seed 43: diverges tick 1-6, 43-55% differ, harm changes 3/3 eps. Seed 42: 1/3 eps diverge (that seed's policy is near-stationary: constant harm -0.10, so the canary is weak there). |

**Reading:**

- z_self -> action is **absent**. The 0/68 one-tick result puts a 95% upper bound of ~4.4% per E3 tick. Zero differences over ~600 closed-loop ticks is stronger.
- z_self -> E1 is **present** (D2), and training z_self amplifies it.
- The break sits between E1's output and selection, and more fundamentally in the absence of any z_self-reading valuation term. **Earliest broken native edge = "z_self -> candidate valuation".**
  - (i) The only live route is E1 -> e1_prior -> an **untrained** `terrain_prior` MLP that sets only the CEM initial mean.
  - (ii) The E2 self-rollout that every candidate carries is **computed and discarded** by scoring.
  - (iii) DR-10, the designed consumer, is OFF and has **no z_self-derived producer**.

## 4. CURRENT_FRONT row -- D2 for z_world (answered at no extra design cost)

**D2 reached for z_world, at two native consumers, in both configs.**

- **E1 prior:** 4-23% relative change under zero/noise/permute (lowest after the fwd objective, when E1 leans more on z_self).
- **E3 selection:** score change 1.4-6.7%. Committed action changed at 4-30% of E3 ticks under noise/swap/permute (1.5-23% under zero). The swap (real alternative content, not destruction) changed 4-14%.
- **D3-direction signal:** persistent z_world intervention changes the closed-loop action sequence and harm.

**Scope limit, stated plainly:** this shows the encoded z_world is **used** by E1 and E3. It does not show which **content** is used, so it does not answer the H-F "content discarded at encode" question. A content-specific D2 needs a targeted edit, for example swapping only the resource-relevant subspace. That was not done here.

## 5. OBJECTIVE-FORM EVIDENCE (probe 3; config A; seeds 42 and 43)

**Design:**

- Each objective is a **phased trainer** that runs its OWN forward passes through the native encode path (`body_obs_encoder` -> `LatentStack.encode` incl. top-down, precision and the GRU; no E1 anchor).
- Input is recorded random-policy chunks (B=16 x L=16) with a fresh detached init state per chunk. No graph survives an optimizer step, so the retained-graph / in-place hazard is avoided by construction. This is the SD-070 pattern.
- The optimizer holds only the z_self path + the objective's own head.
- 300 updates, Adam 1e-3. Then E1/E2 P0 (1078 recipe, 6 x 100 steps).
- For `anchor`, the order is E1/E2 P0 first, then the objective.
- Held-out readout: a native `sense()` stream on env seed+1000, random actions, 10 x 60 ticks. Ridge probe, 5-fold grouped by episode. D1 only.

Each cell is seed 42 / seed 43.

| Candidate | GRU max delta | self_encoder max delta | R2 next body core | R2 current body core | R2 action(t-2) (memory) | eff. rank | z norm | E1 prior change, swap | action change |
|---|---|---|---|---|---|---|---|---|---|
| base (E1/E2 only) | 0 / 0 | 0 / 0 | 0.456 / 0.233 | 0.544 / 0.298 | 0.100 / 0.051 | 1.21 / 1.13 | 0.78 / 0.64 | 0.7% / 0.5% | 0 |
| **(i) fwd: head([z_self_t, a_t]) -> body_{t+1}** | 0.303 / 0.274 | 0.262 / 0.369 | **0.660 / 0.638** | **0.812 / 0.815** | **0.170 / 0.244** | **2.61 / 1.91** | 2.35 / 2.60 | **6.6% / 5.4%** | 0 |
| (ii) contr: temporal InfoNCE on successive z_self | 0.271 / 0.294 | 0.250 / 0.250 | 0.668 / 0.553 | 0.804 / 0.694 | 0.177 / 0.091 | 1.47 / 1.79 | 1.56 / 1.17 | **113% / 36%** (E1 swamped) | 0 |
| (iv) livetap: E2-self loss through LIVE z_self (both ends undetached) | 0.109 / 0.125 | 0.149 / 0.178 | 0.336 / 0.208 | 0.346 / 0.208 | 0.012 / 0.013 | 1.73 / 1.33 | **0.16 / 0.13** | 0.1% / 0.1% | 0 |
| (iii) anchor: live z_self_{t+1} -> detached E1-predicted z_self | 0.209 / 0.135 | 0.185 / 0.174 | 0.067 / 0.033 | 0.078 / 0.047 | 0.003 / 0.001 | **1.02 / 1.03** | 0.83 / 0.64 | 0.2% / 0.1% | 0 |

Reading the columns:

- **Ceiling.** Predicting from the raw instantaneous body_obs_t gives R2 next-body 0.815 / 0.802 and action(t-2) -0.03 / -0.03. So any action(t-2) R2 > 0 is genuinely **recurrent** content the instantaneous observation lacks.
- **Action-change column.** It has only 5 E3 ticks per candidate. For fwd, the powered test is Section 3b (0/68 one-tick, 0/6 closed-loop).
- **(a) Attributable parameter change.** Every candidate moves both the GRU and `self_encoder`, so any of them passes the build's current contract test. That is exactly why the contract test is **not sufficient**.
- **(b) Held-out information.**
  - fwd and contr both raise it clearly: next-body R2 +0.2-0.4, current +0.27-0.52, memory +0.07-0.19.
  - livetap and anchor **collapse** the self-state and **destroy** information. livetap shrinks the z norm 5x and drives its loss to 3e-7, the trivial solution. anchor drives effective rank to 1.02 and R2 to ~0.05.
  - (iii) and (iv) are the same shape: a learned predictor whose target is the trainable latent itself, with no stop-gradient/EMA target to prevent collapse. **Letting the existing E1/E2 losses train through a live tap is the collapse route, not a fix.**
- **(c) Consumer response.** fwd raises E1's sensitivity to a real alternative self-state about 10x, from 0.6% to 6%. contr raises it 50-200x, to the point that the E1 prior is dominated by z_self (zero-intervention change 103-151%). None of them changes action, because of Section 3.

## 6. Ranking and what each form does to later INV-069 / MECH-113 measurements

1. **(i) fwd, body forward model: recommended.** It has the best information gain with the least distortion, the highest effective rank, recurrent memory content (action(t-2) R2 0.17-0.24 vs 0.05-0.10), and a moderate, interpretable E1 coupling. It does **not** optimise any INV-069 DV directly.
   - Caveat for INV-069 arm (a): the self-state is now driven by a body-prediction objective, so "restoration after a burst" is partly re-encoding of the body input. The WWA's generic-contraction null (same architecture at random init + a recurrence-lesioned ablation) becomes load-bearing, not optional.
   - MECH-113: D_eff now has room to move (effective rank 1.2 -> 1.9-2.6).
2. **(ii) contr, temporal InfoNCE: viable for information, but it biases the DV.** Its objective is successive-z_self similarity, and that is what INV-069's V_s consecutive-difference coherence proxy reads. So it **trains the coherence DV directly**, and any later coherence PASS on it is circular. It also swamps E1 (the prior becomes z_self-dominated). Use it only if INV-069 is re-posed on a DV it does not touch.
3. **(iii) anchor and (iv) livetap: reject as sole objectives.** They collapse the self-state. A collapsed z_self makes INV-069 coherence trivially maximal and MECH-113 D_eff trivially minimal. Both would read as success and be vacuous.

## 7. What a trained z_self would need to carry, and for whom

- **E1**, the only D2 consumer, would need body state (position, health, energy, footprint) and short action/body history. The fwd objective supplies exactly these.
- **A behavioural consumer does not exist.** The natural one is DR-10: a **per-candidate self-viability cost** derived from z_self and the candidate's E2 self-rollout, which is already computed per candidate (`e2_fast.py:838`) and discarded. That would use:
  - body-state trajectory under each candidate: health/energy depletion, damage;
  - temporal context from the GRU (recent damage, recent failed actions).

  Building it is the edge that would let a trained z_self change behaviour. It is currently v4-scoped, and it is not in `substrate_queue.json`.

## 8. USER DECISION (named options) and recommendation

The held build's objective form, and whether it goes first:

| Option | What it does | Consequence |
|---|---|---|
| **O1** | Build `sd_zself_training_path` with the **fwd** objective, as scoped | D1 + D2-at-E1. INV-069's coherence leg can then run on a trained substrate against the null. No behavioural consequence is possible. |
| **O2** | Build the downstream consumer first (an ecological z_self -> per-candidate self-viability producer feeding DR-10 or E3) | It would read an untrained, near-constant z_self (effective rank ~1.1), so it would have nothing to use yet. Not recommended first. |
| **O3 (recommended)** | O1 now with the fwd objective. **Plus** register the missing consumer edge as its own substrate_queue row (orchestrator/governance decision), and state in the build and in the DR-13 doc correction that INV-069/MECH-113 retests on it measure **self-state quality and E1 use only, not behavioural self-reach**. | The objective is cheap, it is needed by any consumer, and it has a clean winner. The behavioural gap is surfaced rather than hidden. |
| **O4** | contr instead of fwd | Only if INV-069's DV is re-posed away from consecutive-difference coherence (circularity). |

Do **not** adopt (iii) or (iv): measured collapse on 2/2 seeds.

## 9. Acceptance criteria the repair must inherit (carried from the brief, sharpened by the measurements)

1. **Nonzero, attributable change.** Native training produces nonzero, correctly attributable change in the GRU AND `self_encoder`, with the flag ON and bit-identity with it OFF.
   - The test must FAIL on pre-change code.
   - Necessary, not sufficient: all four candidates pass it, including the two that collapse.
2. **A non-collapse check.** Held-out z_self effective rank and norm must not fall below the untrained baseline (probe 3 `z_eff_rank`, `z_norm_mean`).
3. **Held-out information gain.** It must show on native experience that was NOT used for training: next-body and a history target (e.g. action(t-2)) above the untrained baseline, and the history target above the raw-instantaneous-observation ceiling.
4. **At least one native consumer responds to intervention on the changed self-state.** Today that can only be E1: a swap response above the untrained baseline.
   - Behavioural consequence (D3) is **not** an achievable acceptance criterion until a z_self-reading valuation consumer exists (Section 7). The build must say so rather than silently omit it.
   - A probe-only improvement is D1, not closure.

## 10. Uncertainty, stated plainly

- **Scale.** These are small, Mac-scale runs: 2-3 seeds, 300 objective updates, 6 x 100 E1/E2 steps. The ranking of fwd vs contr on information is close. The collapse of (iii) and (iv), and the z_self behavioural null, are not close.
- **Configs.** Only two configs were tested, one world family each. Config B was untrained with z_self: the production recipe never trains it, so this is representative. Its all-ON heads were also untrained, and GatedPolicy was only tested at init.
- **Seed-42 canary.** In A fwd-trained seed 42 the closed-loop canary is weak (near-stationary policy). Seed 43 and config B carry the canary.
- **What was not probed:**
  - Whether `terrain_prior` would transmit z_self if trained. It has no loss, so this is moot for native behaviour today.
  - Every default-OFF consumer individually. They are listed in 3a from code only.
- **Nondeterminism.** A small residual in E3 scores (control-vs-control max 5.5%) was never enough to flip an action in any run. Its source was not traced.
- **Claim overlap.** `task_claim.py open` reported a scope-overlap NOTE: an older active claim `metaworker-science-20260924-inv109-hash-spike` names paths including this one. The note was not arbitrated and no conflict was found on disk.
