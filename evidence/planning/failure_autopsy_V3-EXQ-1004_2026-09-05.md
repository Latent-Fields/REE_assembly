# Failure autopsy (diagnostic adjudication) -- V3-EXQ-1004, SD-WAYPOINT-FIELD validation

- **Status:** `confirmed`
- **Generated (UTC):** 2026-09-05T02:38:25Z (STAGING MODE draft, headless; produced for governance session `governance-20260905`)
- **Confirmed (UTC):** 2026-09-05T09:35:20Z by `governance-20260905 (user gate, inline route A)`, after a cross-model Step 7c red-team pass (verdict CONTESTED -- see section 11b) and the Step 8 human gate.
- **Gate decision (binding):** release the `corrupting` Step 2.5c gate, set the substrate entry to `implemented_validated`, and route V3-EXQ-884a alongside the consumer-reach fan-out.
- **Scope:** single
- **Target:** `v3_exq_1004_sd_waypoint_field_validation_20260904T214702Z_v3` (queue_id `V3-EXQ-1004`)
- **Trigger:** `experiment_purpose: diagnostic` -- ALL diagnostics require this skill, PASS or FAIL, flagged or not. This run is an unflagged, clean, load-bearing-criterion PASS with `unmet_preconditions: []`, which is exactly the case the blanket trigger exists for.
- **Dry-run gate:** `check_dry_run_citations.py` on the target run_id, `V3-EXQ-1004`, and the prior MECH-428 run: `0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown`. `dry_run_checked: true`, `excluded_dry_run_ids: []`.

---

## 1. Facts (no interpretation)

### 1a. What the run is

Post-build validation of the **SD-WAYPOINT-FIELD** observable landed in campaign C3.2 (`ree-v3` `7719385`, 19 contracts; design doc `REE_assembly/docs/architecture/sd_waypoint_proximity_field.md`). The substrate_queue entry `waypoint-proximity-field-observable` names `validation_experiment: V3-EXQ-1004` explicitly and sits at `status: implemented_pending_validation`, `status_phase: validation_owed`, `severity: corrupting`.

The defect being validated away: in `subgoal_mode` a waypoint reaches the agent **only** as entity-type channel 6 of the 5x5x7 local view (radius 2), so a target more than two cells away is absent from the observation entirely. Every navigation-dependent DV in `subgoal_mode` therefore sits at random-walk level while the manifest reads as a clean "this mechanism has no effect" null -- the definition of `corrupting`.

Four arms, 5 seeds (42-46), 20 eval episodes x 400 steps, 24000 demonstrations, 300 BC steps:

| Arm | visits/ep | sequences/ep | distinct cells/ep | BC accuracy | obs_dim |
|---|---|---|---|---|---|
| `random_floor` | 1.29 | 0.01 | 70.6 | -- | -- |
| `oracle_ceiling` (scripted, env ground truth, never reads the field) | 60.23 | 19.79 | 90.8 | -- | -- |
| `cloned_field_off` | 4.07 | 0.23 | 71.4 | 0.575 | 50 (zero-padded) |
| `cloned_field_on` | 57.71 | 18.87 | 91.1 | 0.841 | 50 |

Criteria: **C1** (load-bearing) ON-minus-OFF visit lift `>= 15.0` on `>= 3` of 5 seeds -- **met 5/5**. **C2** sequence lift `>= 5.0` -- met 5/5. **C3** imitation-accuracy lift `>= 0.05` -- met 5/5. Preconditions: `dv_headroom_waypoint_visit_lift` measured **56.3** against threshold 15.0 (ratio 3.75) on the **ORACLE** control (the arm that navigates from env ground truth and never reads the field); `baseline_not_blocked` 1.0; `eval_policy_not_stationary` 1.0. `field_live_frac` 1.0 on every seed, `field_range_mean` 0.470. Self-route label `waypoint_field_converts_to_navigation`; outcome PASS; `unmet_preconditions: []`.

### 1b. What the field actually is

`ree_core/environment/causal_grid_world.py::CausalGridWorld._get_observation_dict`, lines ~3893-3937. A 25-dim (5x5) agent-centred patch of the global field `f(cell) = 1 / (1 + waypoint_field_decay * d(cell, target))`, `d` = Manhattan distance (torus-aware when `self.toroidal`), target = `self.waypoints[self._next_waypoint_idx]`.

**The field is computed from ENVIRONMENT GROUND TRUTH**, not from REE's own `z_goal` / anchor machinery. It is sourced from `self.waypoints` and never from `self.grid` (deliberately, so the SD-094 marker-erasure defect cannot propagate into it), and appended LAST in `world_parts` so the prefix slice constants in `latent/stack.py` / `latent/zworld_p0.py` are unaffected.

### 1c. What the learners are

There is **no REE agent in this run.** Both learner arms are `ActorCriticPolicy` instances used as behaviour-cloning classifiers over a hand-sliced observation vector:

- **OFF:** `world_state[:175][6::7]` -- the radius-2 waypoint entity channel, 25 dims, **zero-padded to 50** so both nets are byte-identical at init for a given seed.
- **ON:** the same 25 dims **plus** `obs_dict["waypoint_proximity_field_view"]`, 50 dims.

Demonstrations are identical across arms (same oracle, same seeds, same states). The only manipulation is the *content* of the trailing 25 dims. Eval is a **sampled** rollout (`torch.multinomial` over softmaxed logits) as the primary DV, with argmax recorded as secondary.

### 1d. Recording provenance

`validate_recording.py --paths <manifest>`: **1 manifest with always-core gaps -- missing `elapsed_seconds`** (advisory). Everything else in the rec/v1 always-core is present: `recording_schema`, `substrate_hash`, `substrate_commit`, `machine` (`ree-cloud-4`), `machine_class` (`linux-x86_64-py3.10-torch2.12.0+cpu`), full `config` (22 declared knobs), explicit `seeds`.

Two further provenance notes:

- `substrate_commit.dirty: true`, `dirty_count: 1`, on `experiments/_lib/baselines/arc019_curriculum_gating.py` -- outside this driver's import graph, and `substrate_hash` is present, so substrate identity is adequately pinned.
- The primary DV is a `torch.multinomial`-sampled rollout, so per-cell values are **not** bit-reproducible across machine classes ([memory] `reference-cross-machine-class-contract-divergence`). Judge any reproduction on effect size, not on exact values. At a 53.6-visit lift this is a footnote, not a threat.

### 1e. A dead-lettered field (mechanical, load-bearing for the disposition)

The manifest carries `claim_directions: {"INV-086": "supports", "MECH-428": "supports"}` and **no `evidence_direction` and no `evidence_direction_per_claim` at all**. `build_experiment_indexes.py` reads `evidence_direction` / `evidence_direction_per_claim` and contains **no reference to `claim_directions` anywhere** (verified by grep over `evidence/experiments/scripts/` and `scripts/`). The run-pack manifest confirms the consequence: `evidence_direction = unknown`, `evidence_direction_per_claim = {}`.

So the self-routed `supports` never reached the registry -- and neither would a correct read-across value have. This is a driver-side emission bug, not an indexer bug.

---

## 2. Central question 1 -- is the PASS real, or does the design make ON win by construction?

**Verdict: the PASS is real and non-vacuous, but it is LOW-SURPRISE by construction, and what it validates is narrower than "converts to navigation" reads.**

### 2a. Why it is not vacuous

The red-team family in play is *"a gate or criterion that cannot discriminate by construction, graded adequate."* Four things keep C1 out of that family:

1. **C1 is a difference, and the free variable is ON, not OFF.** The OFF arm's low ceiling *is* structural -- beyond radius 2 the oracle's action is not a function of the OFF observation, so a behaviour clone cannot recover it. But that is the *pre-registered floor*, the blocked baseline the build exists to lift, not a rigged control. The question C1 asks is whether the ON reader can decode and act on the field, and that was genuinely uncertain a priori.
2. **The headroom gate is denominated on a control that never reads the field.** `dv_headroom` uses the ORACLE arm, and on the *same statistic C1 routes on* (the `MIN_SEEDS`-th largest per-seed lift, not the mean and not the max). This is the treatment-as-control category error avoided, explicitly and correctly.
3. **The off-ramps were reachable and did not fire.** `field_decodable_but_did_not_convert` (C3 met, C1 not) would have separated information-arrival from behavioural conversion; `learner_capacity_not_field_reach` (oracle above floor, neither learner above it) would have separated the channel from the reader. Both branches exist in `_score()` and both were live.
4. **The two tautological anchors were DELETED rather than re-tuned** (driver comment F6: `waypoint_field_live` and `waypoint_field_carries_gradient` were both unfailable, and both were anchored to constants the author wrote). Field liveness and range are still *recorded* (`field_means`) but not gated on. That is the correct response to an unfailable gate and it is worth crediting explicitly.

### 2b. Why it is nonetheless low-surprise, and what the honest reading is

The field is an **analytic function of the same environment ground truth the demonstrator oracle uses to choose its action.** The oracle is a greedy step toward `self.waypoints[self._next_waypoint_idx]`; the field is a monotone decreasing kernel over Manhattan distance to that same cell. The ON reader's learning problem is therefore a near-linear local-argmin decode of the demonstrator's own decision rule over a 5x5 patch. The prior probability that a 128-hidden-unit MLP fails that at 24000 demonstrations was low.

So: "the waypoint field converts to navigation" is **true, and is a statement about the environment's observation interface**, not about REE's substrate. It establishes that the channel is *wired, live, decodable, and behaviourally sufficient for a supervised reader*. It is not a tautology -- but it is a build validation with a small evidential surplus over the build's own contract tests, and it should be recorded as such rather than as a scientific finding.

### 2c. The gap between validation-specified and validation-delivered

The substrate entry's own `implementation_hint` specified the validation shape: *"DV = waypoints visited and sequences completed by the agent's OWN policy, with NO scripted walk and NO widened completion tolerance ... everything else held at the 977 probe configuration (subgoal_mode, 3 waypoints, `waypoint_visit_reward=0`, 12x12, 400 steps, seeds 42/43/44 plus at least two more)."*

V3-EXQ-1004 deviates in three material ways. **Each deviation is argued from a measurement in the driver docstring, and each argument is sound** -- this is a well-built experiment, and the deviations are the reason it is informative rather than a structural null:

| Deviation | Driver's justification | Assessment |
|---|---|---|
| `waypoint_visit_reward = 0.2`, not 0 | at zero reward *neither* learner arm has a gradient toward a waypoint, so both return the floor and the null is a property of the objective -- the same structural-null class that BLOCKED V3-EXQ-963b | Correct. Reproducing the 977 constant would have made the ablation vacuous by construction. |
| hazards / resources / energy_decay zeroed | instrumented reward composition on this geometry: hazard_approach -0.745, env_caused_hazard -0.578, resource +0.712 against waypoint +0.400, so a reward-maximiser rationally ignores waypoints in BOTH arms | Correct, and the measurement is in the docstring. Consequence: the validated regime is a **navigation-isolated bench**, not the ecological `subgoal_mode` regime the blocked DVs live in. |
| behaviour-cloned reader, not the agent's own RL policy | an A2C reader was built FIRST and reported at 0.00 (OFF) / 0.10 (ON) visits/ep at 400 training episodes, because a random policy visits ~1 waypoint/ep so the +0.2 reward is almost never experienced | Correct as a design choice. **But the A2C figure carries much less weight than the draft of this artifact gave it:** it is docstring-only (seed 42 only, never committed, no manifest) and measured BEFORE the SD-094 contamination gate, on a self-contaminating env in which not moving was reward-optimal. Cloning removes the exploration problem; it does not solve it -- and the A2C number does not establish that an RL consumer *cannot* solve it. |

The third row is the load-bearing one, but its force is *the gap*, not the anecdote. **The consumer the blocked claims actually need -- a REE agent, `world_state` -> `z_world` encoder -> E1/E2/E3, reinforcement-trained under sparse reward -- was NOT tested by this run.** So the inference "the substrate block on INV-086/MECH-428 experiments is lifted" rests on an unstated premise (that a REE consumer can exploit the channel) which this run did not test.

**Red-team correction (F2), applied throughout this artifact.** The draft called the A2C figure "the most important fact in this autopsy" and used it as evidence *for* H1. It cannot bear that: it is docstring-only (seed 42 only, never committed, no manifest) and measured BEFORE the SD-094 contamination gate, on a self-contaminating env in which not moving was reward-optimal -- the driver's own SD-094 gate comment records that on the pre-gate env every arm ended `health_depleted` at 44-134 steps against a declared 400 and per-episode contamination (~-1.2) outweighed the waypoint reward (~+0.04) by 30:1, so wall-pinning was survival-optimal. A reader that stays at the floor under an objective where staying still is optimal is not evidence that reward sparsity is the residual blocker. The correct status of the consumer-reach question is **untested, with one confounded anecdote that motivates it** -- which is what the fan-out (section 7a) is for. A cheap confirmer exists: one seed of an A2C reader on the post-gate isolated bench (the driver already imports `ActorCriticPolicy`; `_build_env` is in hand; budget comparable to one 1004 seed).

**This is not a defect in V3-EXQ-1004.** It is a scope statement that must be written into the substrate entry, or the release condition and the validation delivered silently diverge.

### 2d. One disclosed measurement dependency

The primary DV is the **sampled** rollout because under argmax the field-OFF clone pins: 0.29 visits/ep (below the 1.29 random floor) and 5.96 distinct cells/ep against a `MIN_DISTINCT_CELLS` floor of 5.0. Both readouts are recorded, and the choice is argued (F2: an argmax policy on an under-trained net emits a constant action and pins against a wall -- a degenerate eval protocol, not a channel verdict).

The consequence to state plainly: the OFF arm's headline **4.07 visits/ep is a sampling-entropy figure, not learned navigation.** Its argmax counterpart is 0.29. This *strengthens* the blocked-baseline premise (the OFF reader learned essentially nothing usable), but "OFF beats random 3x" must not be read as "the radius-2 channel supports navigation".

One point the draft under-stated (red-team H3): **under argmax the run would have been UNMEASURABLE, not failed.** Seed 42's OFF reader reached 4.95 distinct cells/ep against the `MIN_DISTINCT_CELLS` floor of 5.0, so `eval_policy_not_stationary` would have read 4/5 = 0.8 < 1.0 and the run would have self-routed `substrate_not_ready_requeue`. The sampled protocol is therefore what makes the run *measurable at all*, not merely what keeps the OFF DV off the wall. It does not move the verdict: ON under argmax is 59.28 visits/ep, a C1 lift of ~59, so the ON result is protocol-invariant.

---

## 3. Claim-layer map -- central question 2

### INV-086 `goal_maintenance_feedback_necessity`

`claim_type: invariant`, `invariant_type: emergent`, `emergent_from: [ARC-030, SD-014]`, `pending_substrate_reconfirmation: true`, `status: candidate`, `epistemic_category`: **absent**, `depends_on: [INV-065, INV-034, MECH-116, MECH-217, ARC-030, SD-014]`.

`what_would_answer` requires: a regime where **MECH-116 working-memory maintenance has MEASURABLY DECAYED** (the non-degeneracy precondition -- the bare-goal control must itself show decay, since unscaffolded `z_goal` already persists ~1000 steps), then **ablating ALL intermediate feedback channels** (MECH-216/217 proxy-wanting + MECH-426 progress-velocity + MECH-427 subgoal-credit) and showing superordinate-goal completion collapses while restoring any single channel rescues it.

V3-EXQ-1004 instantiates **none** of this: no REE agent, no `z_goal`, no MECH-116 LSTM maintenance, no feedback channel, no ablation, no distractor/horizon/effort load. **Not exercised.**

### MECH-428 `subgoal_bootstrapped_goal_seeding`

`claim_type: mechanism`, `status: candidate`, `implementation_phase: v3`, `pending_retest_after_substrate: true`, `epistemic_category`: **absent**, `depends_on: [INV-086, MECH-427, ARC-051, MECH-112, MECH-230]`.

`what_would_answer` requires: a seeding-sparse regime (`z_goal_norm < 0.1`, the GAP-2 condition) in which subgoal-attainment + cross-level credit raises `z_goal_norm` materially above the unscaffolded baseline toward the 626b forced-seed reference, with a **working forced-seed positive control in the SAME harness** as the non-degeneracy guard.

V3-EXQ-1004 has no `z_goal`, no `credit_subgoal_attainment` call, and no forced-seed control. **Not exercised.**

Its `implementation_note` still records that EXP-0390's 3-arm driver is "STILL NEEDED" -- **that note is STALE and must not be cited as current** (red-team F1/H7). It is dated `SD-092 (2026-08-02)`, the day *before* the driver landed. The driver exists: `ree-v3 experiments/v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding.py`, docstring line 7 `Proposal: EXP-0390`; the proposal itself is `status: executed`, `executed_by: V3-EXQ-884`. Governance should refresh the `implementation_note` in the same pass as the `evidence_quality_note`.

### The driver agrees

The driver's own docstring closes with, verbatim: *"experiment_purpose: diagnostic -- this validates the BUILD (is the channel usable), not INV-086's or MECH-428's own hypotheses. claim_ids are carried as read-across only: a PASS lifts the substrate block those claims' experiments were failing under, it does not score them."*

That is exactly right, and it is exactly what `claim_directions: supports` fails to say. The prose disclaimer lives in a docstring nothing downstream reads; the mechanically honest emission would have been `evidence_direction_per_claim: {"INV-086": "non_contributory", "MECH-428": "non_contributory"}` plus an `evidence_direction_note`.

**Both claim tags are PERIPHERAL co-tags.** Per-claim `recommended_epistemic_category` is declared (`standard` for both) so the re-derive-brake counter's per-claim short-circuit applies and neither reading counts toward a ceiling.

### Neighbours read briefly

- **MECH-427** `cross_level_subgoal_credit` (candidate, one PASS at V3-EXQ-883) -- the maintenance-direction sibling. Not tagged here and correctly so; SD-092's primitive is not exercised by this run.
- **ARC-051** `multi_level_wanting_goal_hierarchy` (candidate, `implementation_phase: v3`, `epistemic_category: standard`, zero experimental evidence) -- the parent architecture. Untouched.

---

## 4. Biological-reference triage

The closest reference is an **exteroceptive distal-target gradient**: chemotaxis, beacon-taxis, a place-field distance-to-goal signal -- an environmental affordance that renders an out-of-view goal perceptible at range. Organisms genuinely have these, and the absence of one is a real environmental impoverishment, so the build is a faithful correction rather than a formal-definition import.

`is_formal_import: false`; `lit_status: present` (`evidence/literature/targeted_review_proxy_progress_goal_maintenance` -- Bandura & Schunk 1981, Carver & Scheier 1990, Sutton 1988, already grounding INV-086/MECH-427/MECH-428). **No `/lit-pull` is owed by this run.**

The divergence that matters is at the **consumer** layer, not the channel layer: real organisms acquire gradient-following by reinforcement under sparse reward, whereas this validation supplies a supervised imitation target derived from the same ground truth that generates the gradient -- which removes the very exploration problem the field was partly meant to relieve. That is the honest biological caveat, and it is the same finding as section 2c.

A second, softer point worth recording: the field encodes distance to the *currently pending* waypoint and is recomputed every tick from ground truth. It is therefore an *external* substitute for goal maintenance, not an instance of it. Nothing in this run requires the agent to *hold* a goal across an interval, which is precisely what INV-086 is about.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not exercised** | Neither claim's `what_would_answer` regime is instantiated. Driver says so itself. |
| Biological reference | **clear** | Exteroceptive distal-goal gradient; environmental affordance, not REE's goal machinery. |
| Developmental / dependency prerequisites | **present for this run; NOT present for the blocked claims' own tests** | SD-094 `implemented_validated` and explicitly enabled (`subgoal_arrival_position_check=True`, `hazard_free_contamination_gate=True`); `use_proxy_fields` + `subgoal_mode` enforced by the env. But INV-086's EXP-0705 names two further **unbuilt** prerequisites -- an E3-scoring consumer of `_z_goal_parent` (`chip-20260902-zgoal-parent-e3-consumer`) and a `VALENCE_WANTING` write path not requiring a harm-allocated residue centre -- so two of its three single-channel restore arms are DV-invariant by construction (section 8). |
| Implementation completeness | **complete** | On-demand computation from `self.waypoints`; appended last so prefix slices are safe; 19 contracts; `field_live_frac` 1.0 on 5/5 seeds. |
| Environment adequacy | **partial** | Deliberately de-ecologised: hazards/resources/energy zeroed, `waypoint_visit_reward` 0.2 not 0. Each deviation argued from measurement; consequence is a navigation-isolated bench, not the ecological regime the blocked DVs live in. |
| Measurement adequacy | **adequate, with a disclosed protocol dependency** | Sampled eval primary because argmax pins the OFF reader; both recorded. OFF's 4.07 is sampling entropy, not learned navigation. Under argmax the run would have been *unmeasurable* (seed 42 OFF at 4.95 distinct cells/ep vs a 5.0 floor -> `substrate_not_ready_requeue`), so the protocol choice buys measurability, not just headroom; the ON result is protocol-invariant. Plus the `elapsed_seconds` recording gap. |
| Integration adequacy | **isolated by design** | No REE agent. `world_state` -> `z_world` -> E1/E2/E3 consumer path untouched. |
| Scale / capacity | **adequate for the question asked; not adequate for the consumer question** | 5 seeds / 24000 demos / 300 BC steps is ample for the decode. The consumer question is simply **untested** here. The abandoned A2C reader (0.00 / 0.10 visits/ep at 400 episodes) is docstring-only (seed 42 only, never committed, no manifest) and measured BEFORE the SD-094 contamination gate, on a self-contaminating env in which not moving was reward-optimal, so it motivates that question rather than answering it. |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads | Established? |
|---|---|---|
| MECHANISM FAILED | Implementation completeness = `complete` | mechanism: **established** (as adequate -- nothing failed) |
| MEASURES FAILED | Measurement adequacy = `adequate` with disclosed dependency | measures: **partial** |
| ENVIRONMENT FAILED | Environment adequacy = `partial` | environment: **partial** |
| REE FAILED | all three | **false** |

**Net classification: NOT_APPLICABLE -- this is a PASS and no organism-level REE failure is asserted anywhere in this artifact.** Recorded per GOV-FAILLOC-1 so the read is on the record rather than assumed: had the ON arm failed, MEASURES and ENVIRONMENT are both only `partial`, so the correct read would have been **MIXED**, never REE FAILED.

---

## 6. Central question 3 -- does this lift MECH-428's `pending_retest_after_substrate`?

**The named substrate defect is fixed. The flag should STAY `true`, because the retest has not run -- and the retest is a two-kwarg edit away, not a new build.**

The V3-EXQ-884 autopsy (`failure_autopsy_V3-EXQ-884_2026-08-03`, confirmed) set `pending_retest_after_substrate: true` and routed `/implement-substrate` to create **one** substrate entry, SD-094, covering two defects: waypoint-arrival detection clobbered by the agent's own grid-position marker, and an undisabled ambient self-contamination mechanic. It did **not** name a waypoint field -- that entry came from the V3-EXQ-977 / EXP-0705 adjudication (session `fable-queue-refill-20260902`) on 2026-09-04 (red-team F4). Current state:

- **SD-094**: `status: implemented_validated`, `implementation_landed` `ree-v3 a95e103dc5`, 33/33 contract tests. V3-EXQ-1004's `_build_env` sets **both** resulting flags (`subgoal_arrival_position_check=True`, `hazard_free_contamination_gate=True`) and the driver's own instrumentation confirms the effect: before the gate, every arm ended `health_depleted` at 44-134 steps against a declared 400. With it, episodes run the full 400.
- **`waypoint-proximity-field-observable`**: landed 2026-09-04 and reader-validated by this run -- but a *separate* lineage (see above), and, as it turns out, **not on the 884a code path at all**.

### 6a. What actually gates the MECH-428 retest (red-team F1 -- the draft of this section was WRONG)

The draft asserted that "EXP-0390's 3-arm driver ... has never been built" and that "the retest has still never run and its driver has still never been built". **Both statements are false, and the second was drafted into text governance was being asked to write verbatim into `claims.yaml`.** The facts:

1. **The driver exists and has run.** `ree-v3 experiments/v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding.py` IS the EXP-0390 3-arm NO-SUBGOAL / SUBGOAL-BOOTSTRAP / FORCED-SEED driver (docstring line 7: `Proposal: EXP-0390`; `ARMS = ["NO_SUBGOAL", "SUBGOAL_BOOTSTRAP", "FORCED_SEED"]`). The proposal record reads `status: executed`, `executed_by: V3-EXQ-884`. It ran on 2026-08-03 and FAILed -- that failing run is what the 884 autopsy adjudicated.
2. **The confirmed 884 autopsy already specified the retest**, verbatim: *"`pending_retest_after_substrate: true` -- re-queue V3-EXQ-884 (new letter, e.g. 884a) once the fix lands, with the additional fix of recording real episode length + done cause in the manifest."* Replacing that with "build a `scaffolded_sd054` driver" would be a governance-side re-scoping of a confirmed disposition, and the draft did it inside a block labelled *context only, no state change*.
3. **SD-WAYPOINT-FIELD is not on 884a's path.** 884 SCRIPTS the walk (`_scripted_action`, docstring lines 25-30/69-80), so the agent never navigates by perception in that design; the substrate entry's own `failure_record` says the same from the other side ("883/884 script the walk rather than let the policy navigate"). 884a needs **SD-094 only**.
4. **The real gate is a two-kwarg edit.** 884's `_build_env` passes `size`, `num_hazards=0`, `num_resources=0`, `subgoal_mode=True`, `num_waypoints`, `seed` -- and sets **neither** `subgoal_arrival_position_check` **nor** `hazard_free_contamination_gate` (0 hits for either across the file). Both default off. So a *verbatim* 884a re-queue would reproduce the 884 failure exactly. Setting the two kwargs and re-queueing under a new letter is `complicated (buildable)`, minutes of work -- and it is precisely the default-off trap the waypoint entry's own `implementation_hint` warns about.

So the correct reading: the retest is **owed, cheap, and specified** -- and the flag stays `true` until 884a scores. No successor manifest to the `20260803T022131Z` run exists in `evidence/experiments/` (checked). Whether a *scripted-walk* 884a is a fully satisfying MECH-428 test is a legitimate scientific argument (884's own docstring concedes the behavioural clause is outside its scope), but that argument must be made explicitly against the confirmed 884 disposition -- never by asserting the driver does not exist.

The consumer-reach question of section 2c is a **separate, newly-opened** question (section 7a), not a gate on 884a.

**Bears-on, out of scope, recorded so it is not lost:** SD-094's `queue_accuracy_correction_2026_08_25` states that *"V3-EXQ-884 (MECH-428) subsequently RAN to completion and returned FAIL/weakens"*. But V3-EXQ-884 **is** the failing run in that entry's own `failure_record`, and no successor exists. The correction reads as though a retest has happened when none has -- which, if believed, would justify clearing exactly the flag section 6 says to keep.

---

## 7. Repair pathway, node classification, and routing

**Node class: `complex (probe-gated) / puzzle (known rules)`.** The frame is well-posed and the missing item is a fact -- *where does the residual blockage on navigation-dependent `subgoal_mode` DVs live?* -- so the route is a spike, and because there are **two live hypotheses** it should be a portfolio rather than one sequential re-pose (GOV-FANOUT-1).

**Routing: `/queue-experiment`, on TWO distinct routes** (plus a governance-side `amend` to the substrate entry as bookkeeping):

1. **`/queue-experiment V3-EXQ-884a`** -- the MECH-428 retest the confirmed 884 autopsy already specified. Two-kwarg edit to the EXISTING EXP-0390 driver (`subgoal_arrival_position_check=True`, `hazard_free_contamination_gate=True` in `_build_env`; also record real episode length + done cause), then re-queue under the new letter. `complicated (buildable)`. `pending_retest_after_substrate` stays `true` until 884a scores. This route is NOT the fan-out below and must not be folded into it.
2. **`/queue-experiment` (a new EXQ number)** -- the two-leg consumer-reach fan-out below, for the new scientific question this PASS opens.

**Explicitly NOT recommended:** a power-bump of the 1004 bench (more seeds, more BC steps, longer eval). That would re-measure a question already answered at a headroom ratio of 3.75 with 5/5 seeds.

### 7a. Fan-out portfolio (pre-registered, not queued here)

| Leg | Axis | Sketch | Declared null |
|---|---|---|---|
| **H1** objective/exploration | `drive` | Hold field ON and consumer fixed; vary ONLY the training signal (stock sparse waypoint reward vs shaped/proximity-credited vs demonstration-warm-started). Do NOT re-vary field ON/OFF -- that leg is resolved. | visits/ep flat across training signals, i.e. sparsity is not the residual blocker |
| **H2** observation interface | `representation` | Freeze a `z_world` encoder on this geometry; measure whether the pending waypoint's direction is linearly decodable from `z_world` with the field ON vs OFF, against the 0.575 -> 0.841 raw-observation decodability lift 1004 already established as the upstream reference. | the `z_world` decodability lift is indistinguishable from zero while the raw-observation lift is large -- which locates the loss at the encoder, not the environment |

H2 is prior-consistent with [memory] `project_v3_binding_constraint_observation_interface` (the observation -> `z_world` -> E1/E2 interface as the binding V3 constraint on 39/43 nodes), which is why it belongs in the portfolio rather than being assumed away.

### 7b. Substrate queue -- `amend`, not `create`

Target: **`waypoint-proximity-field-observable`** (existing). **User gate decision, 2026-09-05: RELEASE.** Amendments, detailed in the JSON:

1. **Status and gate are ONE lever, not two decisions (red-team F3).** `/queue-experiment` Step 2.5c gates iff the entry's status is OPEN, and CLOSED is exactly `('implemented', 'implemented_validated', 'validated', 'wontfix', 'closed_aleatoric')`. There is no independent gate switch: the status **is** the switch. The draft presented "move status off pending" and "release the gate" as two amendments and then re-asked them as two separate Step 8 questions -- they are one question. Set `status: implemented_validated`, clear `status_phase`.
2. **Record the validation SCOPE explicitly** (section 2c): validated as decodable-and-behaviourally-sufficient *for a supervised reader*; **not** validated for the reinforcement-trained REE consumer path. The user accepted delivered-vs-specified (a BC-cloned reader on an isolated bench, against the specified "agent's OWN policy at the 977 config") as sufficient for the **observable's correctness** -- which is exactly what the corrupting gate on `causal_grid_world.py::_get_observation_dict` protected. Consumer reach is now tracked as an open scientific question (`waypoint_field_consumer_reach`), not as a substrate defect.
3. **`severity` CHANGES: `corrupting` -> `degrading`** -- stated as a deliberate classification change rather than a silently repeated field (red-team H1). Justification: the observable is validated as decodable, so a navigation DV can no longer sit pinned at chance while the manifest reads as a clean "no effect" null -- the corrupting signature is gone. Consumer reach is open, but an open question is not a correctness defect. A gate is still warranted at `degrading` because the consumer path is genuinely unvalidated; it simply no longer STOP-gates. **`substrate_paths` is UNCHANGED.**
4. **Why release was not a symmetric judgement call.** This was the **only open `corrupting` entry** whose `substrate_paths` name `causal_grid_world.py` (`SD-MECH303-THRESHOLD-SOURCING` and `mech357` also list the module but are `degrading`), and Step 2.5c matches at **module** granularity on a module ~1,201 drivers import. A hold would therefore have STOP-gated every new `/queue-experiment` whose driver imports it -- including **both legs of this artifact's own H1/H2 fan-out**, which run on this geometry by construction. The draft offered "a hold is also defensible" without saying it blocked its own routing. The release un-gates the fan-out.

`resolves_prior_failure_record`: the 977 item, `resolved`. The defect it names is demonstrably no longer true (18.87 sequences/ep on 5/5 seeds against its target of ">= 1 sequence on >= 2 of 3 seeds"; 0.23 without the field). Three caveats carried in the note rather than hidden by the closure: the completing policy is a behaviour clone, not the REE agent, so "the agent's own unscripted policy" is met only in the weak sense; the record's literal `target` (">= 1 sequence on >= 2 of 3 seeds") is met by the **OFF** arm too under the sampled protocol (0.15-0.35 sequences/ep x 20 episodes on 5/5 seeds), so "target met" is non-discriminating at this bench and the closure must lean on the ON-vs-OFF lift alone (red-team H4); and the record's `run_id` (`v3_exq_977_inv086_goal_maintenance_feedback_necessity`) has **no manifest** -- it names a scratchpad one-tick probe (`probe_nav_977.py`, session `fable-queue-refill-20260902`), while the V3-EXQ-977 manifest that does exist is `v3_exq_977_arc052_harm_stream_conditional_precision`, a different experiment. The record is substantively right; only its id is unresolvable.

### 7c. Recording gap (recording-debt, not measurement-debt)

`elapsed_seconds` existed at run time and was simply not stamped. Per the Experimental Recording Standard (`evidence/planning/experimental_recording_standard_2026-07-12.md` Section 3b), the fix is **recording it in the successor** via `experiments/_lib/manifest_core.stamp_recording_core(...)` -- **not** a re-run of V3-EXQ-1004, which would reproduce a settled result at full cost for a timestamp. Impact is low for this adjudication (the verdict rests on effect sizes) but non-zero for the follow-up, which will want to compare the BC and RL training regimes on cost.

### 7d. Re-derive brake and granularity trigger

- **Re-derive brake: does NOT fire.** R1-R3 recipe run 2026-09-05 over the confirmed corpus: **MECH-428 = 1 hit** (`failure_autopsy_V3-EXQ-884_2026-08-03`), **INV-086 = 0 hits**. This autopsy adds 0 to either, because its per-claim categories are declared `standard` and the counter's per-claim short-circuit excludes them. Below the threshold of 2, so no re-queue is refused -- which is substantively correct: MECH-428 has never had a single test that was not `precondition_unmet`. (Hygiene, red-team H5: the one counted slug carries the out-of-enum stamp `precondition_unmet` that this autopsy separately flags, so the counter is treating an out-of-enum category as a hit. Counted anyway and said out loud; below threshold either way.)
- **Granularity-debt recurrence trigger: does NOT fire.** `granularity_debt_cluster.py`: MECH-428 = 1 tagging target (`failure_autopsy_V3-EXQ-884_2026-08-03`, `claim_alignment: unclear`), alignment distribution `unclear=1`, **no target reads `weakened`** -- the reader's own verdict is measurement/implementation debt, not granularity debt. INV-086 = 0 tagging targets. Neither claim meets the two conditions (>=1 `weakened` target AND structurally different signatures).

---

## 8. Central question 4 -- recommended manifest / claims disposition

**For governance to write. This skill does not write any of it.**

### Manifest -- write BOTH the flat manifest and the run pack

The flat manifest currently carries only `claim_directions`, which the indexer does not read; the **run pack** manifest carries `evidence_direction: unknown` with an empty `evidence_direction_per_claim`, and the indexer *drops* `unknown`. A flat-only write would leave the pack's `unknown` standing, so the adjudication would never reach the registry. Write to both (`recommended_manifest_write` in the JSON):

- flat: `evidence/experiments/v3_exq_1004_sd_waypoint_field_validation_20260904T214702Z_v3.json`
- pack: `evidence/experiments/v3_exq_1004_sd_waypoint_field_validation/runs/v3_exq_1004_sd_waypoint_field_validation_20260904T214702Z_v3/manifest.json`

| Field | Recommended value |
|---|---|
| `evidence_direction` | `non_contributory` |
| `evidence_direction_per_claim` | `{"INV-086": "non_contributory", "MECH-428": "non_contributory"}` |
| `evidence_direction_note` | see the drafted `recommended_evidence_quality_note` in the JSON (reproduced in section 8a) |
| `claim_directions` | leave as recorded; it is a driver-authored field the indexer does not read. Do **not** hand-edit the run's history. |

Setting `evidence_direction_note` also sets `direction_explicitly_set` in the indexer, which is the intended outcome: this direction is a deliberate adjudication, not an inference.

### Claims (`claims.yaml`)

| Claim | direction | epistemic_category | diagnostic_evidence_adjudicated | status |
|---|---|---|---|---|
| INV-086 | `non_contributory` | `standard` (currently **absent**) | `true` | none -- stays `candidate` |
| MECH-428 | `non_contributory` | `standard` (currently **absent**) | `true` | none -- stays `candidate`; `pending_retest_after_substrate` **stays true** |

`standard` is the correct category for both -- it is what the resolver infers for an emergent invariant and for a mechanism, and reaching for `substrate_ceiling` or `substrate_conditional` would be wrong in both directions (it would suppress GOV-GRAN-1 surfacing and mark the claims not-v3-testable at exactly the moment they became more testable).

**But state the justification precisely (red-team F4).** The draft justified `standard` as "the substrate gate that was suppressing these claims' experiments has just been lifted". What was lifted is the **observation-layer** gate. For INV-086 specifically the gate is *not* lifted: EXP-0705's `blocked_note` names **three** builds in priority order and only the first has landed --

1. the waypoint proximity field (landed; validated by this run);
2. **an E3-scoring consumer of `_z_goal_parent`** (`chip-20260902-zgoal-parent-e3-consumer`) -- MECH-427 cross-level credit has none anywhere in `ree_core` (only the write hook at `agent.py ~:10145`), so a MECH-427 restore arm is DV-invariant by construction;
3. **a `VALENCE_WANTING` write path not requiring a harm-allocated residue centre** -- MECH-216/217 writes drop silently in `ResidueField.update_valence` when no centre is active, and centres are allocated only on `harm_signal < 0`, so both channels starve in the hazard-free regime.

INV-086's `what_would_answer` requires restoring **any single channel** (MECH-216/217, MECH-426, MECH-427) to rescue completion; with (2) and (3) unbuilt, two of those three restore arms are DV-invariant by construction. **INV-086's experiment stays `blocked_substrate` after this PASS**, and its note must say so.

### 8a. Drafted `evidence_quality_note` (exact text, for governance to write)

> [2026-09-05, V3-EXQ-1004, PASS, diagnostic] Build validation of the SD-WAYPOINT-FIELD observable (ree-v3 7719385), NOT claim evidence. Four arms at 5 seeds: random 1.29 visits/ep, oracle 60.23, cloned-reader field-OFF 4.07, cloned-reader field-ON 57.71; sequences 0.23 (OFF) vs 18.87 (ON); imitation accuracy 0.575 vs 0.841; field_live_frac 1.0. C1 (load-bearing, ON-minus-OFF >= 15 visits/ep) met 5/5 seeds against a dv_headroom precondition denominated on the ORACLE control (56.3 achievable against a 15.0 threshold, ratio 3.75). The PASS is real and non-vacuous -- the OFF arm is zero-padded to the ON width so both nets are byte-identical at init, the oracle never reads the field, and the pre-registered off-ramps could have separated "decodable but did not convert" from "did not convert" -- but it is LOW-SURPRISE by construction: the field is an analytic function (1/(1+0.25d) over the 5x5 agent-centred patch) of the same environment ground truth the demonstrator oracle uses to choose its action, so the ON reader's task is a near-linear local-argmin decode of the demonstrator's own decision rule. What is established is that the channel is wired, live, decodable and behaviourally sufficient FOR A SUPERVISED READER. What is NOT established, and what INV-086/MECH-428 actually need, is that a REE agent -- z_world encoder into E1/E2/E3, reinforcement-trained under sparse reward -- can exploit it: the same driver reports an A2C reader on this task at 0.00 (OFF) / 0.10 (ON) visits/ep after 400 training episodes, which is why the reader was switched to behaviour cloning. Neither claim was exercised (no REE agent, no z_goal, no feedback-channel ablation, no forced-seed control), so both are non_contributory; the manifest's self-routed claim_directions of "supports" must not be applied.

For MECH-428, append the corrected retest sentence (the draft's version mis-attributed the field to the 884 autopsy and asserted an unbuilt driver -- see sections 6a and 11b):

> *The substrate defect named by failure_autopsy_V3-EXQ-884_2026-08-03 is FIXED (SD-094, implemented_validated). The SD-WAYPOINT-FIELD observable -- which came from the V3-EXQ-977 / EXP-0705 adjudication, not from the 884 autopsy -- landed 2026-09-04 and is reader-validated by V3-EXQ-1004, but 884 scripts the walk, so that observable is not on the retest's code path. `pending_retest_after_substrate` stays true because the retest itself has not run: EXP-0390's 3-arm driver EXISTS (experiments/v3_exq_884_mech428_subgoal_bootstrapped_goal_seeding.py; proposal EXP-0390 status executed, executed_by V3-EXQ-884) and the confirmed 884 autopsy's instruction is to re-queue it as 884a once the fix landed. The remaining gate is a two-kwarg edit: 884's _build_env sets neither subgoal_arrival_position_check nor hazard_free_contamination_gate, both default-off, so a verbatim re-queue would reproduce the 884 failure.*

Governance should also refresh MECH-428's stale `implementation_note` ("STILL NEEDED", dated 2026-08-02) in the same pass.

---

## 9. Learning extracted

1. **`claim_directions` is a dead-lettered manifest field.** `build_experiment_indexes.py` reads `evidence_direction` / `evidence_direction_per_claim` and has no reference to `claim_directions` anywhere. This driver emits only `claim_directions`, so the run lands in the index at `evidence_direction: unknown` (confirmed in the run pack). A driver intending a per-claim direction must emit `evidence_direction_per_claim`.
2. **A build-validation diagnostic that carries claim tags "as read-across only" still arrives at governance carrying `supports`,** because the scoring maps the load-bearing criterion onto every `claim_id`. The prose disclaimer lives in a docstring nothing downstream reads. The mechanically honest emission is `evidence_direction_per_claim: {<claim>: non_contributory}` plus an `evidence_direction_note`.
3. **Validating an OBSERVATION channel with a supervised clone of a ground-truth oracle answers the perceivability question and dodges the exploration question in one move.** Legitimate and well-argued here -- an A2C alternative was tried and reported an uninformative null, though that figure is docstring-only (seed 42 only, never committed, no manifest) and measured BEFORE the SD-094 contamination gate, on a self-contaminating env in which not moving was reward-optimal, so it motivates the consumer question rather than settling it -- but it means the substrate entry's release condition and the validation actually delivered are different statements, and the difference must be written into the entry or the gap disappears.
4. **The pre-registered off-ramps are a model of keeping a validation falsifiable.** `field_decodable_but_did_not_convert` and `learner_capacity_not_field_reach` were both reachable and neither fired. Likewise the F6 decision to **DELETE** two tautological readiness anchors rather than re-tune them: a gate that cannot fail certifies nothing.
5. **Recording gap:** `elapsed_seconds` absent from an otherwise complete rec/v1 manifest. Recording-debt, not measurement-debt -- fix in the successor via `stamp_recording_core`, never by re-running.
6. **Provenance oddity (carry, do not repair here):** the substrate entry's `failure_record` cites `run_id v3_exq_977_inv086_goal_maintenance_feedback_necessity`, which has no manifest -- it names a scratchpad probe. The V3-EXQ-977 manifest that exists is a different experiment (`arc052_harm_stream_conditional_precision`).
7. **An autopsy can silently RE-SCOPE a confirmed prior disposition by asserting a missing artifact.** The draft of this artifact said EXP-0390's driver "has never been built", which replaced the confirmed 884 autopsy's cheap instruction (re-queue as 884a) with an expensive new build -- inside a block labelled *context only, no state change*, and inside text governance was asked to write verbatim into `claims.yaml`. The check is mechanical and costs seconds: before writing "X was never built", grep the proposal's `executed_by` and the driver docstring's `Proposal:` line.
8. **Bears-on (out of scope):** (a) the prior MECH-428 autopsy stamped `recommended_epistemic_category: precondition_unmet`, which is **out of the `claims.yaml` enum** -- the behaviour-preserving value for that reading is `standard`; (b) SD-094's `queue_accuracy_correction_2026_08_25` asserts a MECH-428 retest that never happened (section 6).

---

## 10. Mechanical checks run

| Check | Result |
|---|---|
| `check_dry_run_citations.py` (target + V3-EXQ-1004 + the prior 884 run) | 0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean |
| `validate_recording.py --paths <manifest>` | 1 always-core gap: **missing `elapsed_seconds`** (advisory) |
| `granularity_debt_cluster.py MECH-428` | 1 target, alignment `unclear=1`, **no `weakened`** -> trigger does NOT fire |
| `granularity_debt_cluster.py INV-086` | 0 targets -> trigger does NOT fire |
| Re-derive brake R1-R3 recipe | MECH-428 = 1 hit, INV-086 = 0 hits -> **does not fire** (threshold 2) |
| `autopsy_pre_routing_checks.py --json` (Step 7b, run against the landed artifact with its sibling `.md` present) | **0 fires**; `inapplicable`: **C6** and **C7** (this manifest has no top-level `arm_results` array -- its 4 arms x 5 seeds are stored as arm-keyed dicts inside `per_seed[]`). See section 11. |

---

## 11. Step 7b disposition, and what was NOT run

**0 fires.** C1-strict, C2-strict, C3, C5 and C6-narrow all evaluated and silent. Recorded dispositions:

- **C1-strict, C2-strict, C3 and C5 all evaluated and were silent.** The claim-keyed checks (C1/C2/C3) could look, because `claim_ids` is non-empty and both ids resolve -- so their silence is a real negative, not a structural blindness. C5 evaluated once the sibling `.md` existed (the first run, against the scratchpad draft with no `.md`, reported C5 `inapplicable` for that reason alone).
- **C6 and C7 `inapplicable`** -- both want a top-level `arm_results` array; this manifest stores its 4 arms x 5 seeds as arm-keyed dicts inside `per_seed[]`. That is a *shape* miss, not a clean bill, so the cross-arm dissent checks **could not look** and section 2d does their job by hand: the one metric that dissents between readouts is the OFF arm's visit count (**4.07 sampled vs 0.29 argmax**), which is disclosed in the driver and does not contradict any prose absolute in this artifact. Its mirror image -- a metric constant where the design requires it to vary -- was also checked by hand: `field_live_frac` is 1.0 on every ON cell (correct: the field is live whenever a waypoint is pending) and `steps_per_ep` is 400.0 on every cell of every arm (correct: the SD-094 contamination gate restores the declared budget, and this constancy is the *evidence* that gate works, not a degeneracy).
- **`inapplicable` is not "no fire".** Recorded here rather than folded into the fire count.

**Step 7c (adversarial red-team pass) was not run in the staging dispatch, and WAS run before confirmation** -- see section 11b. The staged draft's own prediction of its two most exposed arguments was half right: section 2b (low-surprise) held, section 7b amendment 3 (gate release) was contested and reshaped, and the two largest defects (F1, F2) were in sections 6 and 2c, which the draft did not flag as exposed. Note separately that the driver itself carries a **fable red-team pass at authoring time** -- "REVISE with 8 findings", 7 fixed and re-measured, 1 moot after the clone redesign -- which is why the design is as hardened as it is; that pass audited the *experiment*, not this *adjudication*.

---

## 11b. Step 7c red-team pass (cross-model) and the Step 8 gate

**Model:** `fable-5.1` (cross-model). **Verdict: CONTESTED.** Findings file: `/private/tmp/claude-501/-Users-dgolden-REE-Working/2b29825c-bcaa-4275-97dc-f77b3fd5a682/scratchpad/redteam_1004.md`. Every number in the artifact was independently recomputed from the flat manifest's `per_seed` cells and **all matched to the printed precision** (visits 1.29 / 60.23 / 4.07 / 57.71; C1 lift 53.64 on 5/5; C2 0.23 vs 18.87; C3 0.575 vs 0.841; dv_headroom 56.3, ratio 3.753).

### Findings ATTACKED AND HELD (defended dispositions)

| # | Disposition | Why it holds |
|---|---|---|
| D1 | `non_contributory` for **both** claims | MECH-428's asserted mechanism is cross-level credit into a `z_goal`; the run has no REE agent, no `z_goal`, no credit call, no forced-seed control. The corpus convention set by the confirmed 884 autopsy is that precondition *status* is not mechanism evidence -- so "precondition now reachable" is `non_contributory` for the same reason "precondition unmet" was. INV-086 touches none of its `what_would_answer` regime. |
| D2 | The PASS is real; **"low-surprise by construction"** is the right grade, not weaker | The OFF ceiling is structural (`ws[:175][6::7]` is all-zero beyond radius 2); ON could genuinely have failed on re-pointing/timeout/stale-cache defects, and both off-ramps were live. The oracle's `abs(dx) >= abs(dy)` tie-break is *not* recoverable from the field, which is why BC accuracy is 0.84 rather than ~1.0 -- near-tautological, not fully tautological. |
| D3 | `resolved` (not `superseded`) on the 977 failure_record item | The skill's own definition: something was fixed and the named failure mode is closed. One caveat added (H4, above). |
| D4 | `pending_retest_after_substrate` stays **true** | The flag records that a retest is OWED; clearing the blockers makes it RUNNABLE, not done. (The draft's *reason* was wrong -- see F1 -- but the value is right.) |
| D5 | `claim_directions` is dead-lettered | 0 occurrences across the indexer, `REE_assembly/scripts`, `serve.py`, `ree-v3` runner and `_lib`. Run-pack `evidence_direction` is `unknown`, which the indexer drops. |

### Findings APPLIED (defects, all folded into this artifact)

- **F1 -- "EXP-0390's driver was never built" is FALSE, and silently re-scoped a confirmed retest.** Sections 3, 6/6a, 7, 8a, the JSON `per_claim_recommendation.MECH-428.change`, and the `mech428_subgoal_bootstrap_seeding` decision-block refresh were all rewritten. The retest gate is a two-kwarg edit + re-queue as **V3-EXQ-884a**, now an explicit route.
- **F2 -- the A2C 0.00/0.10 anecdote was over-weighted.** Caveated in 2c, 2d, section 5 (scale), section 9, the JSON `four_layer_diagnosis.scale`, `recommended_evidence_quality_note`, `fanout_recommendation`, and **removed as H1's registry basis** in favour of the caveated wording.
- **F3 -- the substrate amend split ONE lever into two decisions.** Status *is* the Step 2.5c gate. Reshaped as one decision, taken at the gate: **release**. See 7b.
- **F4 -- mis-attribution + omitted INV-086 blockers.** SD-WAYPOINT-FIELD came from the 977/EXP-0705 adjudication, not the 884 autopsy; INV-086's two further unbuilt blockers are now named in section 8, the four-layer prerequisites row, and INV-086's recommended note.
- **Hygiene H1-H8** applied as wording/consistency fixes: H1 (severity change stated explicitly, `substrate_paths` unchanged), H2 (seed/pre-gate qualifiers on the A2C figure), H3 (argmax = unmeasurable, section 2d), H4 (the 977 `target` is non-discriminating), H5 (the brake counts an out-of-enum stamp), H6 (`n_control_values: 0` is an unpopulated field, not an absent control), H7 (MECH-428's `implementation_note` is stale), H8 (this section).

### Step 8 gate -- the user's binding decisions (2026-09-05)

1. `non_contributory` + `standard` for both claims, `diagnostic_evidence_adjudicated: true` -- **accepted** (unchanged).
2. Substrate gate -- **RELEASE**: `status: implemented_validated` with the scope note; `severity` `corrupting` -> `degrading`.
3. Delivered-vs-specified validation scope -- **accepted as sufficient for the observable's correctness**, which is what the gate protected.
4. `pending_retest_after_substrate` on MECH-428 -- **stays `true`**; note corrected per F1/F4.
5. Fan-out portfolio -- **approved** as a draft pre-registration, plus the separate **V3-EXQ-884a** route.
6. Manifest write -- **approved** on BOTH the flat manifest and the run pack.

---

## 12. Step 8 gate -- RESOLVED 2026-09-05 (the questions as posed, with their answers)

1. **Accept `non_contributory` + `standard` for both claims**, against the manifest's self-routed `supports`? -- **YES.** Both `non_contributory`, both `standard`, `diagnostic_evidence_adjudicated: true`.
2 & 3. **These were ONE question, not two** (red-team F3): the entry's status *is* the Step 2.5c gate. **Answer: RELEASE.** `status: implemented_validated` with the scope note; `severity` `corrupting` -> `degrading`; `substrate_paths` unchanged. The delivered validation (a BC-cloned reader on an isolated bench) was accepted as sufficient for the **observable's correctness**, which is what the corrupting gate protected. Consumer reach becomes an open question, not a substrate defect -- and the release un-gates this artifact's own H1/H2 fan-out, which a hold would have STOP-gated.
4. **Confirm `pending_retest_after_substrate` stays `true` on MECH-428** (section 6) -- **YES, stays true**; the drafted note was CORRECTED first (sections 6a, 8a) and the retest routed as **V3-EXQ-884a**.
5. **Approve the two-leg fan-out portfolio** (section 7a) and its pre-registration as the NEW question `waypoint_field_consumer_reach` -- **YES**, still **drafted only** in `hypothesis_space_ledger_pending` for the next `/governance` walk to apply. H1's registry `basis` no longer cites the A2C anecdote as evidence. The `mech428_subgoal_bootstrap_seeding` touch stays **context-only**: no hypothesis added, `initial_frozen_count` unchanged at 1, its one leg's `adjudicating_runs` refreshed to name V3-EXQ-884a. Governance must still confirm `drive` and `representation` are present in `axis_families.map`, or add the rows in the same edit.
6. **Manifest write** (added at the gate): write `evidence_direction`, `evidence_direction_per_claim` and `evidence_direction_note` to BOTH the flat manifest and the run pack -- **approved** (`recommended_manifest_write` in the JSON).

Per the Step 8 rule, this session does **not** `spawn_task` the routing's own follow-on: governance chips it after ratifying the disposition -- both the V3-EXQ-884a re-queue and the consumer-reach fan-out.
