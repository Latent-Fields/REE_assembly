# Action-space proposals (W1-alt): the parallel alternative to the codec repair, and its member gate

- **Status: DESIGN ONLY (no build).** Written 2026-09-25T13:10Z by session `bt0925-actspace` (headless design worker, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-action-space-proposals-design`.
- **Nothing was built, queued or registered.** No `ree_core` edit, no queue entry, no registry edit, no chip. The one edit outside this file is a single new status-table row `W1-alt` in `coupled_loop_repair_campaign_plan.md`. No other row was touched.
- **Why this exists.** The user decided (plan, "User decisions", rec-20260925-6a675285) to **pursue both action-space proposals and the codec repair in parallel, and let the evidence decide.** The A1 draft (`coupled_a1_preregistration_draft_20260925.md`, premise Q5 and sec 14.3) found no build row and no member gate for action-space proposals, so its head-to-head could not run. This record supplies both.
- **Evidence domain: D0** (code read plus arithmetic). No probe was run. Every quantity quoted from another record carries that record's sha.
- **Code state.** ree-v3 `origin/main` @ `29e9caa0c1`. Its `ree_core/` is byte-identical to `cc20be5` (`git diff --stat cc20be5 HEAD -- ree_core` is empty), and `cc20be5` is the current head of `origin/integration/coupled-loop-repair` (BR0, no branch commits yet). So every `file:line` below holds on **both** main and the branch. REE_assembly `origin/master` @ `bac11d4085c` when read.
- **Inputs read in full:** `coupled_loop_repair_campaign_plan.md` (W1 gates (a)-(e), W4, sec 5-6, user decisions); `coupled_a1_preregistration_draft_20260925.md`; `monostrategy_type_a_vs_b_discrimination_20260924.md`; `action_decoder_training_trace_20260924.md`; `action_decoder_training_causal_probe_20260925.md` (`a369f411ff8`); `e2_rollout_divergence_and_proposal_state_dependence_20260924.md` with addenda 1-3; `r5b_r2_fresh_seed_replication_20260924.md` (`fc987f3b057`).

## 0. Bottom line

1. **What it is.** A discrete cross-entropy search **in the env's own action space**. Candidates are one-hot action sequences. The first action is **stratified** (every class gets floor(K/A) or ceil(K/A) of the K candidates), and each class's continuation is a per-step categorical, refit to that class's elites over the existing `num_cem_iterations`. It never calls `action_object_decoder` or `terrain_prior`. It has **no trainable parameters**.
2. **What it sidesteps.** All three coupled codec defects in `a369f411ff8`:
   - the untrained decoder, which is never called;
   - unbounded decode fed to E2, because every rollout action is an exact one-hot;
   - iteration-0 off-range sampling, because a categorical has no scale to calibrate.
   It also removes two defects the plan's W1 list does not name:
   - the zero-vector continuations of the existing scaffold and SP-CEM tokens (sec 2.2 row 5, sec 2.3);
   - the train/runtime action-format mismatch (sec 2.2 row 4).
3. **What it does NOT fix:** E3's horizon aggregation (W4), E2 world-head coverage (W3), grounded valuation (W5), and the encoder ceiling. It also shifts every bit of state-dependence onto the rollout and E3, because nothing learned conditions the proposal on state. **Without W3, W4 and W5 it is expected to reproduce R5b's undirected-noise signature on benign seeds** (`fc987f3b057`: 2/5 flagged, harm up on 3/5).
4. **Stale premise corrected.** The brief asked for a gate "on the same footing as W1 gate (e)", in its literal form: pool containment of an env-Q-best first action, compared against a label-shuffled control. **For this proposer that form is degenerate.**
   - A stratified pool contains every first-action class at every state, so containment is 1.0 by construction.
   - The proposer has no labels to shuffle.
   - Even a uniformly random 32-candidate pool misses a given class with probability (4/5)^32 = 7.9e-4.
   So containment would read 1.0 against 1.0 and fail the "> 0.10" margin for a reason unrelated to quality. Sec 4 proposes a **consumer-mediated** form of (e): E3's pick against env Q, with E3 and the head held fixed. It is offered for **both** variants (option A, recommended).
5. **Placement:** BRANCH (`integration/coupled-loop-repair`). It is `ree_core/hippocampal/**` plus config, three default-OFF knobs plus one optional one, and it is bit-identical when OFF. Its instruments go to main (I1). It is **not** a WakingTrainer member and registers no guard group.
6. **Pre-flight: AMBER overall.**
   - The build is GREEN: every seam exists, and it is `complicated (buildable)`.
   - Gate (e) is RED today. It needs W3 and W4 first, and I1 is not on main.
   - A1 integration is AMBER: 9 precise edits are listed in sec 5.
7. **Debt classes:**
   - build: `complicated (buildable)`;
   - member gate (e)/(f): `complex (probe-gated)` -> `puzzle (known rules)` once W4 fixes E3's aggregation;
   - whether a parameter-free proposer is *enough*: that is what A1's head-to-head decides. It is `complex (probe-gated)`, and the run is the probe.

## 1. Premises re-measured

| # | premise (source) | re-measured at `29e9caa0c1` | verdict |
|---|---|---|---|
| P1 | "R5b `use_action_class_scaffold_candidates` is an existing action-space-ish knob" (brief) | `HippocampalConfig.use_action_class_scaffold_candidates` (`config.py:2930`, default False). When on, `_build_action_class_scaffold_candidates` (`hippocampal/module.py:1361-1399`) builds one candidate per class with `actions[:, 0, cls] = 1.0` (`:1383`) and **every later step a zero vector** (tensor zero-initialised at `:1376-1382`). They are prepended after the CEM (`:2547-2563`, `list(scaffold) + all_trajectories[:keep_n]`), and the docstring says "Diagnostic-only" (`:1366`). | **holds, with a correction.** R5b is a post-hoc splice of A tokens into a codec-generated pool, not an action-space proposer. Its continuations are not actions: E2's world head reads the action vector directly (`e2_fast.py:219`), and zero is never an env action |
| P2 | The SP-CEM floor tokens that Worker C saw (the "1 or 2 off-class candidates") are ordinary candidates | `_inject_support_preserving_candidates` (`module.py:1576-`) builds its injected tokens with **the same scaffold builder** (`:1627-1631`), so they also carry zero continuations. `use_support_preserving_cem` is **default True** (`config.py:2966`). | **new finding (D0).** Under a full-horizon E3, the token is scored on 9 steps of zero-action rollout. Worker C read "token never beats the best of ~31" as an order-statistic effect. The off-manifold continuation is an unconsidered second cause. Reported for the owners of MECH-131 and the repertoire record; not pursued here |
| P3 | The decoder is the only codec component on the act path | E2's rollout consumes the **action** vector (`world_forward`, `e2_fast.py:201-222`). The action-object `o_t` is computed alongside (`:819-820`, `compute_action_objects=True`), but by default only the CEM refit reads it (`module.py:2471-2477`). Other readers: the MECH-151 cue-bias term (`e3_selector.py:354`, inert while `action_bias` is None, which is measured `bias_present: false` in `a369f411ff8`), the diagnostics (`:806`), and replay-buffer copies (`:3106`, `:3565`) | **holds.** An action-space proposer can keep `compute_action_objects=True`, so every downstream reader of O still gets a tensor, while no proposal decision depends on O |
| P4 | Executed actions are one-hot | E3 returns `selected_trajectory.actions[:, 0, :]` (`e3_selector.py:4734`), and the env takes its `argmax` (`causal_grid_world.py:2488`). Under the codec that vector is the decoder's continuous output. ADDENDUM 2 measured an executed one-hot fraction of 0.00 | **corrected for the codec path.** INT-CODEC executes (and E2 rolls out) continuous vectors, even after bounded decode, unless W1 makes its bound a one-hot projection. INT-ACT executes exact one-hots. This asymmetry is not in the plan (sec 2.2 row 4, sec 5 edit E7) |
| P5 | "A1 cannot run INT-ASP until a build row and a member gate exist" (A1 draft Q5) | plan sec 2 rows at `bac11d4085c`: W1, N4 and A1 only. No action-space row | **holds.** This record supplies both. The row `W1-alt` is added to the plan |
| P6 | W1 gate (e)'s containment readout can be applied to this proposer | arithmetic, sec 0 item 4 | **false (degenerate).** Replaced in sec 4 |
| P7 | The CEM elite scorer is a separate question from E3's aggregation (plan W4) | `HippocampalModule._score_trajectory` (`module.py:1691`) scores residue terrain over the **full** rollout (`:1775`, `evaluate_trajectory(world_seq).sum()`). It truncates only through `max_horizon`, which is set only under mode conditioning (`:2180-2191`) | **new coupling.** W4 fixes E3's aggregation only. Both variants' CEM refits still rank on deep steps, which ADDENDUM 2 showed carry >98% of the variance and no action information. That is a parity item for the head-to-head (sec 5 edit E6) |

## 2. What "action-space proposals" means here

### 2.1 The algorithm (ASP-E, recommended form)

Notation, at deployed defaults: K = `num_candidates` = 32 (`config.py:2908`); H = `horizon` = 10 (`:2907`); A = `action_dim` (5 in the A1 env, set by `from_dims`); I = `num_cem_iterations` = 3 (`:2909`); elite fraction 0.2 (`:2910`).

1. **Stratify the first action.** Class c gets n_c = floor(K/A) candidates, plus one more for the first K mod A classes in a fixed order. At K = 32 and A = 5 that is 7/7/6/6/6. The first step is the exact one-hot e_c. This removes the 31:1 class imbalance and the order-statistic bias that Worker C measured, by construction.
2. **Continuations.** Each class c keeps its own per-step categorical p_c[t] over A classes for t = 1..H-1, initialised uniform. Each candidate samples its continuation one-hot per step from p_c.
3. **Roll out** through the native `self.e2.rollout_with_world(z_self, z_world, actions, compute_action_objects=True, action_bias=action_bias)`. This is the call shape `module.py:2284-2288` uses. O is still produced for its downstream readers (P3).
4. **Score** each candidate with the existing `self._score_trajectory(traj, max_horizon=W)`, `module.py:1691`. W is set by the knob `action_space_cem_score_horizon`, sec 3.2; None means the full horizon, exactly as the codec CEM uses today.
5. **Refit per class.** Within class c, the elites are the lowest-scoring max(2, round(0.2 x n_c)) candidates (the existing `_MIN_CEM_ELITES` = 2 floor, `module.py:82`). Then p_c[t] <- (1 - floor x A) x the elite frequency at step t, + floor, which keeps every class above `action_space_prob_floor`. Repeat for I iterations.
6. **Return the last iteration's K candidates**, tagged `metadata["source"] = "action_space_cem"`. They then go through the **unchanged** post-CEM section:
   - the MECH-293 ghost block (`:2509`; excluded, see 3.3);
   - the SP-CEM injection (`:2530`). It no-ops, because every class is already present;
   - the R5b scaffold (`:2547`). The INT-ACT preset sets it OFF;
   - the ARC-071 chunk splice (`:2568`);
   - the modulatory-authority block and diagnostics.

Cost: K x I = 96 rollouts per E3 tick, the same count as the codec CEM, with no decoder calls. RNG: categorical draws replace `randn` draws. Consumption differs only when the flag is ON.

### 2.2 Relation to the codec defects

| defect (source) | ASP-E | why |
|---|---|---|
| 1. untrained decoder (`a369f411ff8`, trace Q1) | **sidestepped** | `_decode_action_objects` (`module.py:612-647`) is never called on this path |
| 2. unbounded decode fed to E2 as the rollout action (`:644-647`, consumed at `:2280`) | **sidestepped** | every rollout action is an exact one-hot. max norm 1, the same format E2's world head trains on (W3, babbling W2a) |
| 3. iteration-0 samples ~12x outside the encoder image (`:2151`, `ao_std = ones`) | **sidestepped** | there is no O-space sample. A categorical has no scale |
| (O -> a -> O refit loop, contraction/divergence) | **sidestepped** | the refit is in action space, not the encoder's image |
| 4. train/runtime action-format mismatch (ADDENDUM 2/3 and `a369f411ff8` limits: heads trained on argmax one-hots, runtime actions continuous) | **sidestepped; not in the plan's W1 list** | INT-ACT executes and rolls out one-hots. INT-CODEC's bounded decode (W1 item 2) bounds the norm but does not make the vector one-hot, unless W1 chooses a one-hot projection. W3's buffer policy must say which format it stores (edit E7) |
| 5. zero-vector continuations (R5b scaffold, SP-CEM tokens; P1, P2) | **sidestepped** | continuations are real sampled actions |
| `terrain_prior` has no grounded target (W1 item 4, N4) | **not needed, not solved** | ASP-E does not read `terrain_prior`, so the circular behavioural-cloning target (trace Q2) is irrelevant to it. The price is **no learned state-conditioning at generation** |
| E3 aggregation (W4) | **not fixed** | E3 still scores the pool. ASP makes E3 the *only* place state-dependence can arise |
| E2 world-head coverage (W3) | **not fixed; ASP depends on it more** | same-first-action candidates differ only through the rollout's continuations, and the E3 comparison between classes is only as good as the head |
| grounded valuation (W5), encoder ceiling (ADDENDUM 1) | **not fixed** | downstream of, or orthogonal to, proposal generation |
| CEM elite scorer reads deep steps (P7) | **not fixed by default** | shared with the codec. Parity knob in 3.2 |

### 2.3 Relation to R5b: build new, reuse the helper's shape, do not repurpose the flag

- **Reuse:** the one-hot construction and the `rollout_with_world` call shape of `_build_action_class_scaffold_candidates` (`module.py:1361-1399`). The new method generalises it: stratified counts, and sampled rather than zero continuations.
- **Do not repurpose `use_action_class_scaffold_candidates`.** Its semantics are measured evidence (ADDENDUM 3; `fc987f3b057`), so changing its behaviour would break the reproducibility of those records. It is also a post-hoc splice into a codec pool, which is a different thing. It stays as is. The INT-ACT preset sets it False and asserts that.
- **The zero-continuation defect in the existing builder (P1, P2) is not fixed by this design.** Fixing it would change the behaviour of default-ON SP-CEM. That is an owner decision: MECH-131 / ARC-065 / `/governance`.

### 2.4 Alternatives considered (options, recommendation marked)

| form | first action | continuation | params | verdict |
|---|---|---|---|---|
| **ASP-E (recommended)** | stratified, fixed | per-class categorical CEM | none | full coverage, balanced by construction, no grounded-target question |
| ASP-R | categorical refit too, with a floor | joint categorical CEM | none | the pool's class mix becomes state-dependent (measurable), but it can re-concentrate on a class the way the codec did. Offered as `action_space_first_action_mode = "refit"` on the same build, so the gate probe can compare the two at no build cost |
| ASP-0 | stratified | uniform random, no refit | none | this is the **RANDOM-POOL control** in gate (e), not a variant. If ASP-E cannot beat it, the search adds nothing beyond coverage, and ASP-0 is the simpler equivalent (sec 4, decision U2) |
| ASP-L | learned state-conditioned prior over classes | as ASP-E/R | yes (trainer member + guard group) | **deferred.** It reintroduces exactly the N4 question (which grounded target?). Build it only if A1 shows the parameter-free form fails *because* generation lacks state-conditioning. That would need its own row |
| continuous action-space CEM (a Gaussian over action vectors, softmax-projected) | - | - | none | **rejected.** It is a bounded decode with an identity decoder. It keeps the continuous/one-hot mismatch (defect 4) that the discrete form removes, and a discrete env action set is the textbook case for the categorical cross-entropy method |

## 3. Where it plugs in

### 3.1 Code seam (all `file:line` at `29e9caa0c1` = branch `cc20be5`)

- **Branch point:** `HippocampalModule.propose_trajectories` (`module.py:2037`).
  - When `use_action_space_proposals` is True, it calls a new `_propose_action_space(z_self, z_world, n, action_bias, num_elite_frac)`, which returns `(trajectories, cem_iteration_diagnostics)`. This call replaces:
    - the O-space initialisation (`:2150-2151`);
    - the whole CEM loop (`:2224-2500`: orthogonal seeding, sampling at `:2273-2280`, the O-space refit at `:2413-2498`).
  - Everything from the ghost block (`:2509`) onward is untouched.
  - With the flag False, the existing code runs byte-for-byte.
- **New method location:** next to `_build_action_class_scaffold_candidates` (`module.py:1361`).
- **Diagnostics:** the new path fills the same `cem_iteration_diagnostics` keys where they apply (`pre_refit_first_action_counts`, `post_elite_refit_first_action_counts`, entropies) via the existing `_summarize_trajectories` (`:887`). It adds:
  - `action_space_step0_counts`;
  - `action_space_continuation_entropy[t]`;
  - `action_space_decoder_calls` (always 0; a contract asserts it);
  - `action_space_max_action_norm` (always 1.0).
- **The consumers are unchanged:**
  - `agent._e3_tick` -> `propose_trajectories` (`agent.py:6964-6973`), then `_committed_candidates` (`:6979`);
  - `generate_trajectories` (`:7029`);
  - `select_action` (`:7427`) -> `e3.select` (`agent.py:10464`);
  - `selected_action = actions[:, 0, :]` (`e3_selector.py:4734`);
  - env argmax (`causal_grid_world.py:2488`).

### 3.2 Knobs (default-OFF; all three config sites each)

| knob | default | purpose |
|---|---|---|
| `use_action_space_proposals` | False | master switch |
| `action_space_first_action_mode` | `"stratified"` | `"stratified"` (ASP-E) or `"refit"` (ASP-R). Any other value raises |
| `action_space_prob_floor` | 0.02 (DRAFT) | minimum per-class probability in every refit categorical. It keeps support, much as the SP ao_std floor does in O. Must satisfy `floor x A < 1`, or it raises |
| `action_space_cem_score_horizon` | None | CEM elite scoring window, passed as `_score_trajectory(max_horizon=...)`. None = the full horizon, the same as the codec CEM. The parity item (sec 5 E6) |

The three sites follow the `use_action_class_scaffold_candidates` pattern:
1. the `HippocampalConfig` dataclass field, next to `config.py:2930`;
2. the `REEConfig.from_dims` keyword argument, next to `:9079`;
3. the `from_dims` assignment `config.hippocampal.<knob> = <knob>`, next to `:10774-10776`.

The memory `reference-reeconfig-from-dims-silent-kwargs` applies: a knob missing from any one of the three sites is silently swallowed. The contract must construct through `from_dims` and assert that the value arrived.

### 3.3 Mutual exclusions (raise at `HippocampalModule.__init__`, `module.py:149`)

These are O-space features with no meaning in action space. Mixing one in silently would put the decoder back into the pool, or turn a knob into a silent no-op:
- `use_differentiable_cem` (`config.py:3267`; it carries a gradient to `cue_action_proj` through `ao_mean`);
- `use_orthogonal_cem_seeding` (`:2924`);
- `mode_conditioning_enabled` (`:3079`; it scales `ao_std` and the scoring window);
- `use_mech293_ghost_probes` (`:3433`; `_propose_ghost_seeded` decodes through the decoder at `module.py:2887-2893`).

All four are default False. `mode_partitioned_cem` (`:3261`, default True) is inert without mode conditioning, so it needs no exclusion.

### 3.4 Branch vs main (plan sec 6)

- **Build: BRANCH (recommended).** The change is under `ree_core/**` and is part of the coupled proposal set. A1 pins **one** sha, and that sha must carry both variants for the head-to-head to share a substrate. Gate (e) also needs W3 and W4, which live on the branch.
  - *Admissible alternative:* MAIN-OFF. The build is parameter-free, bit-identical when OFF and trainer-independent, so it meets the MAIN-OFF bar as W2a does, and gates (b)-(d) could then be probed without a pin. It is not recommended, because it would split the two variants across two planes for no gain: the branch is rebased onto main at every step anyway.
- **Instruments: MAIN-I (I1).**
  - the ASP trace (per-iteration step-0 counts, continuation entropy, decoder-call count, max action norm);
  - the RANDOM-POOL control builder (harness-side: K stratified-uniform one-hot sequences rolled out through `agent.e2.rollout_with_world` and handed to `agent.select_action`);
  - the score-permuted control (a probe-side wrapper that permutes `_score_trajectory`'s outputs within a state; no `ree_core` knob);
  - the E3-mediated pick-in-Q-best readout (it shares the env-Q estimator with W1(e) and W4: `q_values` in `REE_assembly/evidence/planning/probes/rollout/partitioned_repair_probe.py:66`, 6 continuations of length 4).

### 3.5 Trainer and guard membership

- **ASP-E and ASP-R have no trainable parameters.** They are therefore **not** a `WakingTrainerMember` (`ree_core/utils/waking_trainer.py:85`), and they register no group with the trainer (`:197`) or the guard.
- The guard (`ree_core/utils/grad_reach_guard.py`) observes only tensors held by observed optimizers (G1-G4). In INT-ACT:
  - the codec and prior groups (W1) are simply **not registered**;
  - `action_object_decoder` and `terrain_prior` are constructed (`module.py:169`, `:178`) but not on the act path. No optimizer holds them, so the guard does not check them. G5 LEAK must report no gradient into them, and a contract asserts that too.
  - This is correct by design, not an allowlist: an allowlist entry would itself need G3's stale check.
- R0 for INT-ACT therefore covers fewer groups than for INT-CODEC. That asymmetry is stated in the A1 edits (E4).
- **ASP-L, if ever built,** would be a member with its own group and guard coverage. Out of scope.

## 4. The member gate (G-ASP), parallel to W1 (a)-(e)

As plan sec 3 says, a member gate is **a precondition of A1, not evidence that the loop works**. It is D1/D2 at most.

| gate | statement | W1 analog | domain |
|---|---|---|---|
| (a) | guard / trainer: no ASP group exists; G5 reports **no** gradient reaching `action_object_decoder` or `terrain_prior` over the gate window; every other group in the preset keeps its own guard PASS | W1 (a) guard PASS | D1 |
| (b) | action validity: over >= 200 E3 ticks per seed, every candidate's `actions` is an exact one-hot at every step (no zero vector, no fractional entry), `action_space_decoder_calls` = 0 and `action_space_max_action_norm` = 1.0 | W1 (b) round trip >= 0.95 (the codec's action-validity check) | D1 |
| (c) | bounded rollouts: the median candidate `world_states` norm at t = H stays within [0.5, 2] x the t = 0 norm, with no per-step growth > 1.05 (today's divergent signature is x1.2/step untrained, ~x3/iteration for trained-decoder decoded norms). Read with the W3 head | W1 (c) decoded-norm bound | D1 |
| (d) | coverage and support: (stratified) every class present in >= 0.99 of final pools, with class counts exactly the stratified n_c; (refit) every class >= 1 candidate in >= 0.95 of pools, and every refit categorical >= `action_space_prob_floor` | W1 (d) iteration-0 range | D1 |
| **(e)** | **informative D2 through the native consumer** (below) | W1 (e) | D2 |
| (f) | not state-invariant: E3's picked first-action class, over >= 20 probe states per seed, has a modal-class share < 0.90 on >= 4/5 seeds. **Creditable only jointly with (e)**: `a369f411ff8` showed a shuffled decoder varies the pool as often as an honest one, so variation alone is not evidence. In refit mode, also report the proposer's own step-0 distribution: mean pairwise TV across states, against the score-permuted control | the monostrategy readout (Worker C, J) | D1, D2 with (e) |

### 4.1 Gate (e): the consumer-mediated form

- **Setting:**
  - the W3 head, and E3 with the W4-chosen aggregation, both frozen and identical across arms;
  - >= 20 cloned-env probe states per seed, 5 seeds, the A1 env (8x8, 2 hazards, 3 resources, tie-break ON, `world_dim` 32);
  - env-Q = the ADDENDUM 3 outcome-3 estimator (6 random 4-step continuations; `q_values`, cited above);
  - Q-best set = the first-action classes within 1e-9 of the max Q.
- **Readout (per state):** is E3's pick from the arm's pool in the Q-best set?
- **Arms (same states, same frozen E3 and head):**
  - `ACT`: the ASP-E pool;
  - `NATIVE-POOL`: today's codec CEM pool (untrained decoder), i.e. the defect being repaired;
  - `RANDOM-POOL`: stratified first action, uniform random continuations, no refit (ASP-0);
  - `PERM`: ASP-E with the CEM elite scores permuted within each state. The machinery runs, but its choices carry no rollout information. This is the analog of "label-shuffled": the same machinery, with the information destroyed.
- **PASS (e) iff, on >= 4/5 seeds:**
  - (e1) `ACT - NATIVE-POOL > 0.10`: the repair matters to the consumer; **and**
  - (e2) `ACT - RANDOM-POOL >= 0`: not worse than an unguided pool.
- **Reported, not gated:**
  - `ACT - PERM`;
  - `ACT - RANDOM-POOL` as a signed number;
  - pool containment of Q-best (expected 1.0, and stated so), for side-by-side comparison with W1(e).
- **Interpretation, fixed in advance:**
  - (e1) PASS with `ACT - RANDOM-POOL` ~ 0 means the gain is **coverage alone**. The search adds nothing beyond it, and ASP-0 is the simpler equivalent (user decision U2).
  - (e1) FAIL with W4 green means stratified coverage does not help E3 choose. INT-ACT is then not ready for A1, and ASP-L becomes the only action-space route.

**Why (e1) and (e2), and not a shuffled-label margin.**
- ASP has no learned content, so it claims only coverage plus on-manifold actions.
- The honest test of that claim is "better for the consumer than the collapsed native pool". The honest bound on it is "no better than a random pool", which would say the search is idle.
- The codec *does* claim learned content, so its own shuffled control stays in W1(e) (option A below).

### 4.2 Same footing with W1(e): options for the user (U1)

| option | W1(e) (codec) | G-ASP (e) | same footing? |
|---|---|---|---|
| **A (recommended)** | keep its containment-vs-shuffled leg (the codec's content check) **and add** the consumer-mediated leg (e1)/(e2) above, with the codec pool in place of ACT | (e1)/(e2) as above | **yes** on the shared leg: both variants must beat NATIVE-POOL through E3 by the same margin, on the same states, against the same frozen E3 |
| B | unchanged (containment vs shuffled) | the literal analog (containment vs PERM) | **no.** ASP reads 1.0 vs 1.0 and fails the margin by construction (sec 0 item 4) |
| C | unchanged | containment, with the class floor and stratification ablated during measurement | **no.** It measures a configuration that is never deployed |

Sequencing: (e) and (f) cannot be read before **W4's gate** passes (plan sec 3: "No D2 reading of any other workstream counts until W4's gate passes"). ADDENDUM 2 showed E3's full-horizon pick is at or below chance with any head. Gates (a)-(d) need only BR0 and can be probed as soon as the build lands.

## 5. A1 integration

### 5.1 Naming (decided here, obvious and recorded)

The variants are **INT-CODEC** and **INT-ACT**. This follows the orchestrator brief. The A1 draft's `INT-ASP` becomes `INT-ACT` everywhere. The build and design name "ASP" (action-space proposals) stays as the name of the mechanism. INT-ACT = the W6 preset with `use_action_space_proposals=True`, `action_space_first_action_mode="stratified"`, the W1 codec and prior members not registered, and `use_action_class_scaffold_candidates=False` (asserted).

### 5.2 Precise edits the A1 draft needs (NOT applied here; the A1 draft's owner applies them)

| id | where in `coupled_a1_preregistration_draft_20260925.md` | edit |
|---|---|---|
| E1 | header, sec 0 row 2, sec 5.1, sec 8.3, sec 13 "tested arms", sec 14.3/14.5, sec 15 "unresolved" | rename `INT-ASP` -> `INT-ACT` (and `-SHUF/-FROZEN/-R1`) |
| E2 | sec 1 Q5 | verdict "gap" -> "closed by `action_space_proposals_design_20260925.md` (design) and plan row `W1-alt` (build, not started)". A1 still waits for the W1-alt build and gate |
| E3 | sec 5.1 INT-ASP row "config" | "W6 preset, action-space proposal variant" -> "W6 preset + `use_action_space_proposals=True`, `action_space_first_action_mode="stratified"`, `action_space_cem_score_horizon` = the value fixed under E6; codec and prior members NOT registered; `use_action_class_scaffold_candidates=False` asserted" |
| E4 | sec 5.3 SHUF list, sec 7 R0 | state that INT-ACT-SHUF has **no** codec decode labels and **no** `terrain_prior` target to permute. It shuffles the harm/benefit targets, the valuation stream (GROUNDED) and the E2-world action labels, babbling included. So INT-ACT-SHUF destroys strictly less than INT-CODEC-SHUF, and R0 covers fewer groups. P3 is per-variant against its own SHUF, so each test stays internally fair. The head-to-head (8.3) reads P1b only, so the asymmetry does not tilt it. **Say this explicitly** |
| E5 | sec 7 R1 "ASP: that variant's own member gate (undefined, Q5)" | -> "INT-ACT: G-ASP (b), (c), (d) of `action_space_proposals_design_20260925.md` sec 4, checked in-run per admitted seed from the propose diagnostics". Parity: R1 for CODEC also checks only (b)-(d). **Both variants' (e) is a pre-A1 member-gate precondition, not an in-run R-check** |
| E6 | new line in sec 4 or 5.1 (parity) | pre-register **one** CEM elite scoring window for both variants: `action_space_cem_score_horizon` for INT-ACT, and the equivalent for the codec CEM, which today has only mode-conditioned `max_horizon` (`module.py:2180-2191`) and so needs the W1 build to expose the same window. Either both use the full horizon (today's behaviour) or both use W4's chosen depth. Unequal windows would confound the head-to-head with P7 |
| E7 | new line in sec 5.1 (parity), cross-ref W3 | pre-register W3's buffer action format for both variants. INT-ACT executes exact one-hots; INT-CODEC executes bounded continuous vectors (P4). The W3 member must store the **executed vector as fed to E2** (not its argmax) in both, or else argmax one-hots in both. Either choice is fair if it is the same. Otherwise the codec's head is trained on a different format from the one it rolls out |
| E8 | sec 6.1 "Reported" | "proposal m4" is degenerate for INT-ACT, because the stratified pool's majority class is undefined. Report instead: (i) E3-picked class modal share across probe states (G-ASP (f)), for both variants; (ii) refit-mode step-0 TV across states, if refit is ever used. Keep m4 for INT-CODEC |
| E9 | sec 8.3 tie rule, sec 14.5 | "ASP wins, because it is simpler (it deletes the codec)" -> "INT-ACT wins, because it is simpler: it removes the decoder and `terrain_prior` from the act path. The modules remain constructed but unused, and it adds no trainable parameters". The substance is unchanged; the old wording overstated "deletes" |

### 5.3 Readiness asymmetry (user decision U3)

W1-alt has no probe-gated part in its build, and its gate (e) needs the same W3 and W4 as W1(e). So W1-alt will probably be gate-ready **before** W1: the codec still has N4 (the grounded prior target) to settle. A1 draft 8.3 makes "either variant INVALID -> A1 INVALID".

| option | effect |
|---|---|
| **(a) hold A1 until both variants pass their gates (recommended)** | keeps the one-sha, same-seed head-to-head the user asked for. Cost: A1 waits for N4 |
| (b) run INT-ACT's arms first under this A1 id, and INT-CODEC later under a lettered id on a later sha | earlier signal, but it loses same-sha comparability (the branch rebases between them) and doubles the NATIVE and screening cost |
| (c) if W1 (b)-(d) fail outright, run A1 with INT-ACT only and record the head-to-head as not run | this is the plan's original contingency, now symmetric |

## 6. Read-only PRE-FLIGHT

Every producer and consumer the build and gate touch, at `29e9caa0c1` (= branch `cc20be5`):

| # | piece | producer / consumer (file:line) | grade | debt class |
|---|---|---|---|---|
| 1 | branch point in `propose_trajectories` | `hippocampal/module.py:2037`; replaces `:2150-2151` and `:2224-2500`; post-CEM `:2509-` untouched | GREEN | complicated (buildable) |
| 2 | one-hot + rollout shape to reuse | `_build_action_class_scaffold_candidates` `module.py:1361-1399`; `e2.rollout_with_world` `e2_fast.py:756` | GREEN | complicated (buildable) |
| 3 | elite scorer with a window argument | `_score_trajectory` `module.py:1691` (`max_horizon`, terrain at `:1775`) | GREEN | complicated (buildable) |
| 4 | E2 consumes the action directly | `world_forward` `e2_fast.py:201-222` (`world_action_encoder` `:219`); O computed at `:819-820` | GREEN | - |
| 5 | O's downstream readers stay fed | `e3_selector.py:354` (MECH-151, inert while `action_bias` is None); `module.py:806`, `:3106`, `:3565` | GREEN | - |
| 6 | config, 3 sites | `config.py:2930` (dataclass), `:9079` (from_dims kwarg), `:10774-10776` (assignment) | GREEN | complicated (buildable) |
| 7 | mutual exclusions | `config.py:3267`, `:2924`, `:3079`, `:3433`; raise at `module.py:149` | GREEN | complicated (buildable) |
| 8 | E3 selection over the pool | `agent.py:6964-6973`, `:6979`, `:7029`, `:7427`; `agent.py:10464` (`e3.select` call); `e3_selector.py:4734` (selected action) | GREEN | - |
| 9 | env consumes argmax | `causal_grid_world.py:2488` | GREEN | - |
| 10 | trainer / guard non-membership | `waking_trainer.py:85`, `:166`, `:197`; `grad_reach_guard.py` G1-G5 | GREEN (no group, by design) | - |
| 11 | contracts: OFF bit-identity; ON: decoder calls 0, `terrain_prior` calls 0, exact one-hots, stratified counts, floor respected, from_dims round trip, mutual-exclusion raises | new `tests/contracts/test_action_space_proposals*.py` on the branch; run via `remote_pytest.sh tests/contracts/<file> -q` | GREEN (buildable) | complicated (buildable) |
| 12 | env-Q estimator | `REE_assembly/.../probes/rollout/partitioned_repair_probe.py:66` (`q_values`); to be ported into I1 | AMBER (not on main) | complicated (buildable) |
| 13 | I1 instruments: ASP trace, RANDOM-POOL, PERM wrapper, E3-mediated pick-in-Q-best | `experiments/_lib/coupled_acceptance.py` is **not on origin/main** (the A1 draft's Q2 finding still holds at `29e9caa0c1`) | AMBER | complicated (buildable) |
| 14 | W3 head, W4 aggregation (preconditions of gate (e)/(f)) | plan rows W3 (not-started), W4 (blocked) | **RED** for (e)/(f) today | W3 complicated (buildable); W4 complex (probe-gated) -> puzzle |
| 15 | cloned-env probe states | `copy.deepcopy(CausalGridWorldV2)` validated max diff 0.0 (ADDENDUM 2) | GREEN | - |
| 16 | `substrate_pin` for gate probes on the branch | `experiments/_lib/substrate_pin.py` (main); N0 done | GREEN | - |
| 17 | whether parameter-free generation suffices for the closed loop | A1 head-to-head | - | complex (probe-gated): the run is the probe |

**Overall: AMBER.**
- The build is GREEN and could start after BR0 (done).
- Gates (a)-(d) are GREEN once the build lands.
- Gates (e)/(f) are RED until W3 and W4 pass and I1 lands.
- A1 integration is AMBER, pending the 9 edits and decisions U1-U3.

## 7. Decisions the user owns (none taken here)

| id | question | options | recommendation |
|---|---|---|---|
| U1 | the form of gate (e), for both variants | A: add the consumer-mediated leg to W1(e) too / B: literal containment for both / C: containment with the floor ablated | **A** (sec 4.2). B is degenerate for ASP, and C measures a configuration that is never deployed |
| U2 | what to do if (e1) passes but ACT ~ RANDOM-POOL | keep ASP-E / switch INT-ACT to ASP-0 (no refit) | decide at gate time. Fix now that ASP-0 wins a tie within 0.05 on pick-in-Q-best, because it is simpler |
| U3 | A1 readiness asymmetry | (a) hold for both / (b) INT-ACT first under a lettered id / (c) INT-ACT only if the codec fails (b)-(d) | **(a)**, because it keeps the head-to-head the user asked for |
| U4 | the CEM elite scoring window, both variants (E6) | full horizon for both / W4's depth for both | W4's depth for both, since it follows the same logic as W4 (ADDENDUM 2: deep steps carry no action information). Needs the W1 build to expose the same window |
| U5 | build placement | BRANCH / MAIN-OFF | **BRANCH** (sec 3.4) |
| U6 | registry | a new `substrate_queue` row for W1-alt, or an amendment folding it into the proposed SD-080 widening | a **new row** (e.g. `action-space-proposal-generation`), `ready: true` after BR0. It is a different mechanism from SD-080 (it deletes rather than trains the codec), so folding it in would blur the head-to-head. `/governance` owns this |

## 8. Other findings (reported; not pursued; not chipped)

- **P2: the default-ON SP-CEM floor tokens have zero-vector continuations** (`module.py:1627-1631` via `:1376-1383`). It bears on Worker C's reading of the 1061 monostrategy (a token "never beats the best of ~31") and on every default-config run that scores SP tokens at depth > 1. The owner is the repertoire / MECH-131 / ARC-065 line. Fixing it changes default behaviour, so it is a `/governance` decision.
- **P4/E7: the codec path's executed action is continuous even after bounded decode.** This is a fourth coupled codec defect that plan W1 does not list. It bears on W1's scope and on W3's buffer design.
- **P7: the CEM elite scorer reads the full horizon in both variants.** W4 as scoped fixes E3 only.

## 9. Done / not done

- **Done:**
  - design sec 2-3;
  - member gate sec 4;
  - A1 edits sec 5 (listed, not applied);
  - pre-flight sec 6;
  - options sec 7;
  - one status row `W1-alt` added to the plan.
- **Not done:**
  - no build, contract, queue entry, registry row or chip;
  - no probe (D0 only);
  - the A1 draft itself was not edited;
  - the other plan rows (including A1's `INT-ASP` wording) were not edited.
- **Uncertainty, stated plainly:**
  - The 0.02 floor and the stratified allocation are DRAFT constants.
  - Whether (e1) can pass at all depends on W4, which is not yet built.
  - Whether a parameter-free proposer is enough for the closed loop is exactly what A1 decides. Nothing here predicts it.
