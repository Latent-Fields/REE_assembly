# Failure autopsy -- V3-EXQ-1039 (diagnostic PASS)

- **Status:** `confirmed` -- Step 8 gate held with the user 2026-09-16 (account-handover walkthrough session; recorded 2026-09-16T13:06:22Z; red-team CONTESTED, findings applied before the gate). See "Step 8 gate outcome" at the end. Originally: Status: `awaiting_human_confirmation` -- STAGING-MODE DRAFT. Routing is NOT finalised. ...

- Generated: `2026-09-16T12:21:45Z`
- Scope: single
- Target run: `v3_exq_1039_mech428_inv086_waypoint_field_consumer_drive_signal_20260915T025330Z_v3`
- Queue id: `V3-EXQ-1039` | purpose: `diagnostic` | outcome: **PASS**
- Self-route label: `training_signal_does_not_convert_h1_not_supported`
- Claims (read-across co-tags only): `INV-086`, `MECH-428`
- Machine `ree-cloud-2`, class `linux-x86_64-py3.10-torch2.12.0+cpu`, elapsed 11272.6 s
- Substrate hash `5a74d5279d7c7753...`, substrate commit `45237ec3` (clean, branch main), `substrate_stable_across_run: true`

**Why this artifact exists at all.** The run is a clean PASS with no indexer adjudication flag. Trigger 2
of `/failure-autopsy` applies regardless: `experiment_purpose: "diagnostic"` -- ALL of them, PASS or FAIL,
flagged or not. The manifest's `interpretation.label` is a hypothesis about what the run found, never a
verdict, and for a diagnostic PASS the central question is always whether the result held for a real
reason or a degenerate one. It did not hold for a real reason. That is the finding below.

**Staging reason.** Written headless by a dispatched autopsy session. The **Step 8 interactive gate is
held by the coordinating session and is OWED** before this routing is acted on. **Step 9b was drafted only**
-- `hypothesis_space_registry.v1.json` was not written; the intended Mode-B non-resolution append is recorded
in the JSON under `hypothesis_space_ledger_pending`.

**REVISION, 2026-09-16.** Step 7c has now RUN: a cross-model adversarial pass by **Fable 5.1** (this draft
was written on Opus 5), returning **CONTESTED**. The headline survived every recompute; seven findings
changed the recommendations. **Every confirmer was re-run independently by this session before anything was
applied** -- all seven hold, none was rejected, two corrected errors of mine (an over-stated multiplier and
a wrong speculation about a diagnostic flag), and one partial disagreement is recorded rather than dropped.
What changed: two new 1039a readiness preconditions, a third routing item (a cross-artifact correction
against the now-CONFIRMED sibling 1030), a fourth hypothesis in 3f, a new section 3g, and several corrected
numbers and claims. What did **not** change: the vacuity verdict, the failure-location read, and both
per-claim dispositions. Full record: section 12 and the JSON's `red_team` block. Status stays
`awaiting_human_confirmation`.

**Path note, because it affects how much you should trust the numbers below.** The `REE_assembly` main
checkout is ref-wedged (34 behind / 50 ahead of `origin/master`). Every governance artifact cited here --
`claims.yaml`, `substrate_queue.json`, `hypothesis_space_registry.v1.json`, the three prior autopsies, the
literature records -- was read via `git show origin/master:<path>`, never from the working tree. The
re-derive-brake corpus scan was run over a `git archive origin/master evidence/planning` mirror, after
confirming that 5 autopsy JSONs on disk differ from origin (`failure_autopsy_V3-EXQ-063a_2026-09-14`,
`-1028_2026-09-15`, `-729_2026-09-14`, `-829a_2026-09-01`, `-964b_2026-09-16`). A disk-based scan would
have been unreliable. Manifests and drivers were read from disk, which is safe -- they are not in the
wedged set. No file inside any repo was written by this session.

---

## 1. Step 2a -- dry-run gate (run BEFORE any metric was read)

`scripts/check_dry_run_citations.py` was executed over every id this artifact cites:

| id | dry? |
|---|---|
| `v3_exq_1039_..._20260915T025330Z_v3` (target) | clean |
| `v3_exq_1030_..._20260914T125657Z_v3` (sibling leg) | clean |
| `v3_exq_1004_..._20260904T214702Z_v3` | clean |
| `v3_exq_884_..._20260803T022131Z_v3` | clean |
| queue ids `V3-EXQ-1039 / 1030 / 1004 / 884` | clean |

Result: `0 dry cited, 0 dry in named families, 0 ambiguous, 4 clean, 0 unknown`, exit 0.
Family sweep `--family v3_exq_1039`: **0 dry / 1 real**.
`dry_run_checked: true`, `excluded_dry_run_ids: []`. The stamp is earned -- the checker script was
actually run (it imports `generate_pending_review._is_dry_run` rather than reading the raw field), which
is what GOV-DRY-1 requires and what a manual field read does not substitute for.

Driver-side reachability: `validate_experiments.py --checks dry_run_unreachable_criterion` reports 11
warnings fleet-wide, **none of them on this driver**. Per the lint's own guidance a silent result is a
net, not an all-clear, so the driver's `--dry-run` reduction block was also read by hand: `DRY_SEEDS=[42]`,
`DRY_RL=3`, `DRY_STEPS=10`, `DRY_EVAL=2`. No criterion in this driver is gated on an absolute mid-training
episode index, so no latch is structurally unsettable in the smoke. Nothing here is dry anyway.

## 2. Step 2b -- facts, no interpretation

### Recording provenance

`ree-v3/validate_recording.py --paths <manifest>` returns **OK -- 1 complete, 0 always-core gaps**. All of
`recording_schema` (`rec/v1`), `substrate_hash`, `substrate_commit`, `machine`, `machine_class`,
`elapsed_seconds`, full `config`, and explicit `seeds` `[42, 43, 44]` are present. A `substrate_ceiling`
reading would therefore have been falsifiable on this manifest -- which matters, because this autopsy does
**not** reach for one.

One advisory finding, and it is on the nose: **`combination_rule` names criteria the manifest does NOT
record**. The rule string names `C0/C0b/C0c/C0d/R1/R2/C1`, but the manifest carries no `criteria` block at
all -- only `interpretation.preconditions` (the six readiness/premise gates) and
`criteria_non_degenerate: {"C1": true}`. C1's own measured value, bar and pass/fail never reach the
manifest. A reader cannot discharge governance Step 2b's threshold-arithmetic clause without opening the
driver source. This is the first of three recording gaps and the mildest.

### What the run did

Three treatment arms x three seeds, plus two anchors, field ON in every arm, navigation-isolated env
(`num_hazards=0`, `num_resources=0`, `energy_decay=0.0`, SD-094 contamination gate on):

- `sparse_rl` -- stock waypoint reward only; `_train_all_on_agent(p0=0, p1=90)`, unmodified.
- `shaped_rl` -- identical call on the same env wrapped in `_ShapedWaypointEnv`, which adds a monotone
  non-negative per-step progress bonus `max(0, manhattan_prev - manhattan_next)` at `SHAPING_COEF = 1.0`.
- `demo_warmstart` -- 25 episodes of auxiliary oracle-supervised cross-entropy on the lateral-PFC bias
  head, then the identical 90-episode RL procedure.
- `greedy_oracle`, `random_walk` -- anchors.

Budget: `zworld_p0=20`, `p0_warmup=25`, `rl=90`, `n_demo=25`, `eval=10`, `steps_per_episode=80`.
DV: `waypoints_visited_per_ep`.

### The numbers

| arm | seed 42 | seed 43 | seed 44 | mean |
|---|---|---|---|---|
| `greedy_oracle` | 12.0 | 10.8 | 12.0 | **11.6** |
| `random_walk` | 0.6 | 0.3 | 0.6 | 0.5 |
| `sparse_rl` | 0.4 | 0.2 | 0.0 | 0.2 |
| `shaped_rl` | **0.4** | **0.2** | **0.0** | **0.2** |
| `demo_warmstart` | 0.5 | 0.2 | 0.1 | 0.267 |

`distinct_cells_per_ep`, same layout:

| arm | seed 42 | seed 43 | seed 44 |
|---|---|---|---|
| `greedy_oracle` | 50.4 | 53.2 | 53.6 |
| `random_walk` | 24.8 | 24.3 | 27.6 |
| `sparse_rl` | 25.3 | 9.2 | 8.3 |
| `shaped_rl` | **25.3** | **9.2** | **8.3** |
| `demo_warmstart` | 28.8 | 9.2 | 9.0 |

`shaped_clears_n_seeds = 0`, `demo_clears_n_seeds = 0`, `min_seeds_required = 2`.

### Expected vs observed, and which criterion decided

The driver's declared null for H1 is *flatness across training signals*. C1 (lift of a dense arm over
`sparse_rl` by at least `LIFT_MARGIN_FRAC = 0.20` of the `(oracle - random)` span, on at least 2 of 3
seeds) **did not clear on either dense arm**, and because not-clearing IS the declared null, the run scores
**PASS** and self-routes `training_signal_does_not_convert_h1_not_supported`.

So no criterion "failed" in the ordinary sense. The adjudication question is not *which criterion failed*
but **whether the null that was met is a measurement or an artefact of a manipulation the consumer never
absorbed.**

### All six preconditions passed

| precondition | kind | measured | threshold | met |
|---|---|---|---|---|
| `greedy_oracle_clears_floor` | readiness | 10.8 | 4.0 | yes |
| `zworld_encoder_trained_majority_cells` | readiness | 1.0 | 0.5 | yes |
| `achievable_span_clears_floor` | readiness | 11.1 | 2.0 | yes |
| `lpfc_bias_head_trainable_majority_cells` | readiness | 0.667 | 0.5 | yes |
| `sparse_rl_stays_blocked` | premise | 0.2 | 4.385 | yes |
| `treatment_arms_move` | eval_protocol | 8.3 | 8.0 | yes |

`non_degenerate: true`, `degeneracy_reason: ""`, `criteria_non_degenerate: {"C1": true}`.

A clean sweep. That is precisely what makes this run worth an autopsy rather than a rubber stamp.

---

## 3. The finding

### 3a. `shaped_rl` is bit-identical to its own control, on every channel, in every seed

Read the two tables above again. `sparse_rl` and `shaped_rl` agree to the recorded decimal on
`waypoints_visited_per_ep` (0.4 / 0.2 / 0.0), on `distinct_cells_per_ep` (25.3 / 9.2 / 8.3), on
`sequences_completed_per_ep` (0.0 throughout), and on the `zworld_encoder_trained` and
`lpfc_bias_head_moved` flags. Ten eval episodes per cell, three seeds, two independently trained policies:
identity at that resolution is not a small effect. It is the **absence of any effect on committed
behaviour**.

Say *committed behaviour*, not *parameters*, and mean it: the parameters **did** change in both arms on
seeds 43 and 44 (`lpfc_bias_head_moved: True`). Section 3f gives routes by which changed parameters leave
behaviour unchanged. (`lpfc_candidate_summary_degenerate` is deliberately **not** in the identity list
above -- it is a never-computed constant in this config, see 3f item 2.)

**And the two arms were not given similar training signals.** The shaping bonus was measured directly for
this autopsy, by instantiating the driver's exact env configuration and running the driver's own
`_pending_waypoint_manhattan` accumulator over 30 episodes (3 seeds x 10 episodes, 80 steps):

| seed | unshaped return / ep | shaped return / ep | ratio | rewarded steps / 800 |
|---|---|---|---|---|
| 42 | 0.1200 | 30.42 | 253x | 6 -> 298 |
| 43 | 0.0600 | 29.46 | 491x | 3 -> 284 |
| 44 | 0.1200 | 30.52 | 254x | 6 -> 304 |
| **mean** | **0.1000** | **30.13** | **301x** | **5 -> 295** |

**Quote the order of magnitude, not the multiplier.** An earlier draft of this artifact said `~1115x` from
a single RNG draw; the cross-model red-team pass (F6) caught it and this recompute -- using the driver's
*own* anchor RNG, `np.random.RandomState(seed + 777)`, exactly as `_make_random_eval_act` seeds it --
reproduces the red team's 250-500x range instead. The multiplier is unstable because the denominator is a
handful of 0.2-per-visit events. The **step counts** are the stable statement and they are the stronger
one: 3-6 rewarded steps per 800 becomes ~300.

A policy that never moves still accrues ~1.5 bonus per episode, because `sequence_commitment_timeout = 20`
respawns a fresh randomised waypoint every 20 uncredited steps, `_dist_prev` is not reset on respawn, and
the distance can therefore jump downward on that tick. **That matters for the repair, not just as trivia:
it means "arm returns differ" can go green on a policy that never moved, so returns-differ is a necessary
but not a sufficient absorption precondition** (section 14 item 1 is paired with item 2 for this reason).

So `shaped_rl`'s learner was credited with a per-episode return **two-plus orders of magnitude** larger
than `sparse_rl`'s, and produced a policy that behaves identically. The plumbing is fine --
`_ShapedWaypointEnv.step` returns the shaped scalar in the position `_train_all_on_agent` reads
(`allon_training.py:452`, `_flat, _harm_signal, done, info, obs_dict = env.step(action)`;
`:455`, `ep_reward += harm_signal`), and `_pending_waypoint_manhattan`'s `getattr` defaults were checked
against a live env (`waypoints`, `_next_waypoint_idx`, `agent_x`, `agent_y` all present). The reward
reached `ep_reward`. It did not reach behaviour.

### 3b. `demo_warmstart` learned exactly nothing, and the manifest says so in one number

`demo_ce_final_loss` per seed: **3.465735912322998**, 3.465975761413574, 3.464894533157348.

`ln(32) = 3.4657359027997265`. `num_candidates = 32` (`ree_core/utils/config.py:889`).

Seed 42's value equals `ln(K)` to seven decimals -- float32 identity -- **after 232 applied optimizer
steps** (`demo_n_labelled_ticks: 232`, every one of them a `zero_grad / backward / clip / step` cycle at
`lr=1e-3`). A cross-entropy pinned at chance means the bias head's output stayed uniform across all 32
candidates. And on that same seed `lpfc_bias_head_moved` reads **False** -- 232 backward-and-step calls
moved the last-linear weight norm by less than `1e-9`. That is the arithmetic signature of an
*exactly zero* gradient, not a small one.

Seeds 43 and 44 sit within 1e-3 of `ln(32)` after 14 and 22 applied steps. Their labelling was also
starved: `demo_n_target_defaulted` 186 and 178 against `demo_n_target_matched` 14 and 22, i.e. on ~90% of
eligible ticks no candidate's first action matched the oracle direction and the update was (correctly)
skipped.

### 3c. The gate built for exactly this signature passed

This is the part that should travel furthest.

The driver went through a Step 4.5 cross-model red-team (fable-5.1). Finding **F3** said, verbatim in the
queue note: *"nothing certified the ONE component every arm's training signal actually trains (the
lateral-PFC bias head, zero-initialised last layer) ever receives a non-zero gradient -- the dry-run's own
`demo_ce_final_loss == ln(K)` signature at authoring scale was consistent with an exactly-zero gradient."*

The red team named the signature. The fix added readiness precondition **C0d**
(`lpfc_bias_head_trainable_majority_cells`), which tests `|weight_norm_after - weight_norm_before| > 1e-9`
plus `LateralPFCAnalog`'s `candidate_summary_degenerate` flag, on a majority of treatment cells.

C0d **passed at 0.667** while the named signature was present on all three seeds and while seed 42's head
provably did not move at all.

**And C0d is weaker still than that.** Its degeneracy half is inert in this configuration:
`_last_candidate_summary_degenerate` is assigned *only* inside
`if self.config.rule_readout_consumer and k >= 2:` (`lateral_pfc_analog.py:429-450`), and
`rule_readout_consumer` defaults `False` (`:181`; `lateral_pfc_rule_readout_consumer: bool = False`,
`config.py:4207`) and is not set by the all-ON recipe -- `grep rule_readout_consumer` over
`v3_exq_724_competence_localization_diagnostic.py` returns nothing, and the probe prints it `False` off the
constructed agent. So the driver read the `__init__` constant (`:293`), `nondegenerate_frac = 1.0` is
vacuous, and **C0d in this run reduces to the weight-norm boolean alone**. (Found by the cross-model
red-team pass, F3; it also corrected a wrong speculation in this artifact's first draft -- see 3f item 2.)

The gate asserts on *correlates of training having occurred*, not on *the manipulation having been
absorbed*. Where a red team names a failure signature, the gate should assert on **that signature** --
here, CE loss materially below `ln(K)` -- not on a proxy for it.

### 3d. C1's non-degeneracy flag cannot see any of this

The driver sets:

```python
criteria_non_degenerate = {"C1": bool(r2["met"])}
```

R2 is `treatment_arms_move`: every treatment cell visits at least `MIN_DISTINCT_CELLS = 8.0` distinct
cells at eval. It is an **eval-policy mobility check**. It observes nothing about the training phase and is
structurally incapable of detecting an unabsorbed manipulation. So `non_degenerate: true` and
`criteria_non_degenerate: {"C1": true}` on this manifest certify nothing whatsoever about the validity of
the null that was reported.

Worth noting on its own terms: R2's worst cell measured **8.3 against a bar of 8.0**. The treatment arms at
seeds 43 and 44 visit 8-9 distinct cells in 80 steps while `random_walk` visits 24-28. The trained arms are
roughly a third as mobile as random. The bar was raised from 4.0 to 8.0 by red-team finding F12 and is
still low enough that a near-stationary policy clears it.

**The first draft recorded that number and drew no inference from it. That was a miss, and the cross-model
pass (F1) called it.** A trained policy less mobile than a random walk, sitting just above the gate that is
supposed to certify it moves, is the signature of an **eval-policy attractor** -- and section 3g gives the
independent evidence that it is one.

### 3e. Why the `demo` arm differs from `sparse` at all, and why that is not evidence of learning

`demo_warmstart` does differ slightly from `sparse_rl` (0.5 vs 0.4 and 28.8 vs 25.3 at seed 42; 0.1 vs 0.0
and 9.0 vs 8.3 at seed 44). It is tempting to read that as the warm-start doing something.

It is not -- **on seeds 42 and 44**. At seed 42 the demo arm's `lpfc_bias_head_moved` is **False** and its
CE is exactly `ln(32)` -- the head demonstrably did not change -- yet the rollout still differs. The 25 demo
episodes consume torch and numpy RNG that the sparse arm does not, shifting the stochastic stream for the
subsequent P1 phase and for eval. So within this manifest there is a direct internal demonstration that
**arm-to-arm differences of this size can be RNG-stream artefacts rather than treatment effects.**

**Scoped to those two seeds deliberately.** The first draft asserted this across the board; the cross-model
pass (F1c) showed it does not hold at seed 43, where `demo_warmstart` is bit-identical to *both* other arms
(0.2 / 9.2) despite 14 applied CE steps, `lpfc_bias_head_moved: True`, and the same 25 episodes of extra RNG
consumption. I record a narrower disagreement than the red team here: seed 43 does not *contradict* the RNG
reading, it shows the RNG-to-behaviour map is not uniform across seeds -- which is itself evidence for the
attractor, and is taken up as such in 3g. What was genuinely wrong was the unqualified generalisation.

### 3g. The rival cause the first draft missed: proposer-pool collapse / an eval-policy attractor

This is the substantive addition from the cross-model red-team pass (F1), and its confirmer was re-run
independently for this revision (`scratchpad/rt1039_probe.py`, ~36 s, reproduced exactly).

**At init, before any training, with K = 32 candidates:**

| seed | E3 ticks | distinct first-action classes | candidate-summary pairwise max dist |
|---|---|---|---|
| 42 | 58 | 4 on 49 ticks, 5 on 9 | 0.0297 - 0.0517 |
| 43 | 25 | **2 on 25 of 25 ticks** | 0.0277 - 0.0462 |

Two distinct first-action classes out of thirty-two candidates is a pool in which no bias on any candidate
can produce more than a binary choice. **This is a registered substrate condition, not a novelty:**
`mech294_coherence_magnitude_strengthening` (GFLAG-0183, 2026-09-09) records the ARC-065 SP-CEM pool as
`floor_clamped_at_2_distinct_first_action_classes ... vs the 4.5 distinct first-action classes MECH-341's
falsifier treats as a diverse pool`, and **SD-061** (`implemented_pending_validation`) is the existing lever
-- a difficulty-gated proposal-entropy regulator whose readout is `candidate_first_action_entropy`.
ARC-065/MECH-314 carry the same shape from a different measurement: *"E2 world-forward compresses K diverse
first-action candidates to identical first-step z_world (verified empirically 2026-05-25:
cand_world_pairwise_dist=0.0000 across K=32 with 2-3 unique argmax action classes)"*.

Three lines of evidence therefore converge on it: the probe (2 classes at seed 43), the manifest (seed-43
eval insensitive even to a shifted RNG stream, 3e), and the eval mobility (8-9 distinct cells against a
random walk's 24-28, 3d).

**Why this changes the recommendation and not the verdict.** Every absorption precondition the first draft
proposed is *training-side*. Under proposer-pool collapse a **fully absorbed** manipulation -- returns
differ, advantage fraction high, CE far below `ln(K)` -- still produces identical eval behaviour. A repaired
1039a gated only on those preconditions could go **fully green and reproduce this very null**, which is
exactly the gate-as-correlate defect this artifact diagnoses in C0d at 3c. Section 14 item 2 is the fix, and
it is paired with item 1 rather than optional.

One honest limit: the probe measures the pool **at init**. It establishes that the collapse condition is
*reachable* in this construction; it does not establish that it held during the scored run, which recorded
nothing about it. That is precisely why the fix is an in-run, per-arm, per-phase precondition and not a
citation of this probe.

### 3f. What is NOT established

**Four** candidate explanations for the failure to convert are live, and this run separates none of them,
because the deciding telemetry was never recorded:

1. **The lPFC head's SHARE of the summed modulatory accum** -- *not*, as the first draft framed it, the
   absolute magnitude bound. `lateral_pfc_bias_scale = 0.1` (`config.py:4183`), and with
   `rule_readout_consumer` False the output is bounded by a **hard clamp** (`lateral_pfc_analog.py:483-485`),
   not the scaled-tanh form (`:479`), which is gated on that same flag. But under
   `use_modulatory_selection_authority: True` with `modulatory_authority_normalize_basis: 'std'`, E3
   rescales the *summed* accum into competition with the raw-score spread -- this run's own diagnostics
   give `score_bias_to_raw_range_ratio` 0.096-0.432, `modulatory_authority_ratio_competitive` 1.0 on most
   ticks, `scale_factor` 0.005-0.018 against `e3_raw_score_range_mean` 0.0024-0.0111. So `|0.1|` is not the
   limiting quantity; lPFC's **share** of an accum that also carries dACC, gated-policy, OFC and MECH-295
   is. The clamp can still bite, but by **saturation** -- a saturated hard clamp contributes a flat,
   rank-free term *and* has exactly zero gradient, as the substrate's own comment records at `:174-179`,
   citing V3-EXQ-822's `prop_delta` of exactly 0.0. (Reframed on red-team F4.)
2. **Exactly-zero gradient into the bias head -- by any of three routes**, which share one signature.
   For the last linear, `dW_k = (p_k - y_k) h_k`, so the gradient vanishes exactly if **(a)** the hidden
   activations are *identical across candidates* (since `sum_k (p_k - y_k) = 0`, both `dW` and `db` vanish),
   or **(b)** the hidden ReLU is *fully dead* (`h = 0` for all K), or **(c)** the hard clamp is *saturated*
   (item 1). Seed 42 positively evidences *some* route (232 applied steps, no weight movement) and the run
   distinguishes none of them. The substrate already tracks `_last_hidden_dead_relu_frac`
   (`lateral_pfc_analog.py:284`, populated `:462-467`, exposed as `hidden_dead_relu_frac` at `:555`) and the
   driver simply does not record it.
   **Correction to the first draft, which was wrong here.** It speculated that the
   `candidate_summary_degenerate` flag was "measured on a different tensor". It is not: the flag is a
   **never-computed `__init__` constant** in this configuration (3c). And the probe shows the summary spread
   is *not* degenerate at init (0.03-0.05 pairwise), so any row-identity during the scored run is
   **P0-induced** -- `E2_TRAIN_IN_P1 = False` (`allon_training.py:101`), so E2 trains in P0 only. That is
   precisely ARC-065/MECH-314's registered finding of E2 world-forward collapsing K candidates to an
   identical first-step `z_world`. (Corrected on red-team F3/F5.)
3. **Budget.** 90 RL episodes, a declared and deliberate first-probe budget ~13x smaller per cell than the
   MECH-457 fan-out precedent.
4. **Proposer-pool collapse / an RNG-insensitive eval-policy attractor** -- section 3g. Added by the
   cross-model red-team pass; it is the one that changes the repair specification, because under it a fully
   absorbed manipulation still converts to nothing.

I record these as an open instrument question, not as a conclusion. That is the honest state.

One more item is **noted and explicitly not rested on**: training calls
`agent.sense(obs_body, obs_world, obs_harm, obs_harm_a, obs_harm_history)` while eval calls
`agent.act(flat)` -> `sense_flat(...)` -> `sense(obs_body, obs_world)` with no harm arguments, under a
config with `latent.use_harm_stream: True` and `latent.use_affective_harm_stream: True`. The queue note
records red-team F11 as CLEAR on train/eval parity; this autopsy does not overturn that, and rests nothing
on it, because whatever level shift it introduces is **common to all three treatment arms** and so cannot
manufacture or mask a between-arm contrast. (Three, not five: `_run_anchor_cell` routes `greedy_oracle` and
`random_walk` through `_oracle_eval_act` / `_make_random_eval_act`, neither of which touches the agent at
all -- the anchors never call `sense` by either path.) Flagged for whoever builds the successor.

---

## 4. Claim-layer map (Step 3)

Read from `origin/master:docs/claims/claims.yaml` on 2026-09-16.

| field | INV-086 | MECH-428 |
|---|---|---|
| title | `goal_maintenance_feedback_necessity` | `subgoal_bootstrapped_goal_seeding` |
| claim_type | invariant (`emergent`, from ARC-030 + SD-014) | mechanism |
| status | `candidate` | `candidate` |
| `epistemic_category` | `standard` | `standard` |
| `diagnostic_evidence_adjudicated` | `true` | `true` |
| retest flag | `pending_substrate_reconfirmation: true` | `pending_retest_after_substrate: true` |
| `implementation_phase` | -- | `v3` |
| `live_status.evidence.from` | `failure_autopsy_V3-EXQ-1004_2026-09-05` | `failure_autopsy_V3-EXQ-1004_2026-09-05` |
| `depends_on` | INV-065, INV-034, MECH-116, MECH-217, ARC-030, SD-014 | INV-086, MECH-427, ARC-051, MECH-112, MECH-230 |

**Did the experiment test the claim under conditions where the claim could express itself? No -- and the
manifest proves it independently of anyone's reading of the driver.**

- INV-086's `what_would_answer` requires a regime where MECH-116 working-memory maintenance has
  *measurably decayed* (the explicit non-degeneracy precondition, since unscaffolded `z_goal` already
  persists ~1000 steps), then ablation of all intermediate feedback channels. Nothing here ablates a
  feedback channel.
- MECH-428's `what_would_answer` requires a seeding-sparse regime (`z_goal_norm < 0.1`) plus a 626b-style
  forced-seed positive control. Neither is present.
- **The decisive independent check:** `z_goal_stream` on this manifest reads `ticks_total: 94434`,
  `ticks_active: 0`, `active_frac: 0.0`, `writer_calls: 81234`, `writer_defect: false`,
  `goal_state_present: true`. `z_goal` existed and was written to, and was **never active in a single tick
  of any arm**. A run in which `z_goal` is never active cannot bear on a `z_goal`-seeding or
  `z_goal`-maintenance claim, whatever the tags say.

The driver declares `evidence_direction_per_claim = non_contributory` for both, unconditionally. That
declaration is accurate, and the tags are *correctly* inherited rather than wrongly inherited -- this is
not an EXQ-048/048b-shaped tagging error. It is an honest read-across co-tag, the third in a row for this
pair (1004, 1030, 1039).

Clinical / out-of-domain check: neither claim is clinical-cohort-scoped, so the V3-EXQ-698 / MECH-175 trap
does not apply and `out_of_domain` is not the route.

Stale-conditional-category check (the V3-EXQ-861 / MECH-180 shape): both claims' current
`epistemic_category: standard` was set by the confirmed 1004 disposition, and neither claim's
`evidence_quality_note` or category prose states a re-check trigger conditional on this run. Nothing stale
to clear.

---

## 5. Biological-reference triage (Step 4)

**Closest reference mechanism.** Dopaminergic reward-prediction-error teaching of a dorsal-striatal actor
against a ventral-striatal value baseline (Schultz/Dayan/Montague 1997; O'Doherty 2004), with the
demonstration arm's nearest analog being observational/imitative acquisition of an action policy routed
through lateral prefrontal rule representation.

**Surrounding systems that reference mechanism depends on:** a parameterised actor the teaching signal
actually reaches; a value baseline; an action-adequate representation for the actor to ride; enough
experience for credit assignment to converge.

**Faithful translation or formal import?** Neither, quite. REINFORCE with an EMA baseline is a legitimate
biologically-motivated policy-gradient family, so this is not an SD-003-shaped formal-definition import.
The divergence is one of **locus**: the teaching signal is applied to two *modulatory bias channels*
bounded at `|0.1|` and `|2.0|`, and E3's own scoring network -- the thing that actually chooses -- receives
no gradient at all. The driver states this itself, clearly and in advance, in its `WHAT THIS IS NOT`
section. Biologically the nearest thing to that arrangement is a prefrontal bias added to an already-learned
striatal action value: in real brains a *modulator* of a learned policy, never the sole substrate of policy
learning.

**Does the failure resemble what would happen biologically if a known dependency were absent? Yes,
exactly.** Ablate the striatal actor and try to teach navigation through prefrontal bias alone, and you get
this: a large reward signal, an intact perceptual channel, and no behavioural conversion. That makes the
result a **discovered prerequisite**, not a falsification of reward density's relevance.

**Literature status: `present`, and checked rather than assumed.**
`evidence/literature/targeted_review_mech_428/` holds three entries, all read on origin/master:

- Florensa, Held, Geng & Abbeel 2018, *Automatic Goal Generation for Reinforcement Learning Agents*
  (ICML; computational_model, supports, conf 0.62) -- adversarial goal generator holding goals at ZPD
  difficulty, producing an automatic curriculum.
- Kulkarni, Narasimhan, Saeedi & Tenenbaum 2016, *Hierarchical Deep Reinforcement Learning* (NeurIPS;
  computational_model, supports, conf 0.66) -- h-DQN meta-controller over intrinsic goals learns under
  very sparse delayed feedback where flat deep RL does not.
- Wood, Bruner & Ross 1976, *The role of tutoring in problem solving* (behavioral_human, supports,
  conf 0.52) -- scaffolding / zone of proximal development.

All three bear on MECH-428's own claim; none addresses the narrow engineering question this run raises
(can a prefrontal bias channel bounded at `|0.1|` convert a reward-density manipulation into committed
navigation). **No `/lit-pull` is commissioned for that gap**: it is settled mechanically by recording the
absorption telemetry, far more cheaply than by literature, and a lit-pull on a question a one-line
instrument change answers would be a misroute.

---

## 6. Four-layer diagnosis (Step 5)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not exercised** | Neither `what_would_answer` regime instantiated; `z_goal` active in 0 of 94434 ticks |
| Biological reference | **partial** | Reference is striatal RPE actor learning; REE applied the signal to two bounded prefrontal/OFC bias channels |
| Developmental / dependency prerequisites | **missing** | A reward-to-behaviour learning path. `sd_actor_critic_action_learning`'s own `current_blocker` already named this before the run |
| Implementation completeness | **partial** | Consumer fully built and the bias does reach E3 scoring at eval (`use_modulatory_selection_authority: True`); the *learning* path is two bounded bias heads, E3's scoring net ungradiented |
| Environment adequacy | **adequate** | Oracle 10.8-12.0 vs random 0.3-0.6; span 11.1 vs floor 2.0. The env is navigable and did not cause this |
| Measurement adequacy | **under-instrumented** | No training-return telemetry; C1's non-degeneracy = R2 eval mobility; C0d passed while its own named signature was present, and its degeneracy half is a never-computed constant; nothing recorded on the conversion side either (first-action diversity, lPFC share of the accum, `hidden_dead_relu_frac`, summary spread) |
| Integration adequacy | **partially coupled** | Train/eval sense-path asymmetry, common to all arms, noted and not rested on |
| Scale / capacity | **likely insufficient** | 90 RL episodes; one of **four** unseparated candidate explanations (3f) |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM FAILED | Implementation completeness (+ Biological reference) | **not established** -- row reads `partial` |
| MEASURES FAILED | Measurement adequacy | **not established** -- row reads `under-instrumented` |
| ENVIRONMENT FAILED | Environment adequacy | **established** -- row reads `adequate` |
| REE FAILED | all three | **false** -- unreachable by construction |

**Net classification: MIXED (MECHANISM + MEASURES) -- not chargeable to REE.**

Stated plainly so it cannot be quoted the other way: nothing in this artifact licenses an organism-level or
claim-level read that REE failed to navigate. The only defensible statement is that **this run did not put
REE in a position to succeed or fail at the thing it set out to measure.**

### Recording-debt vs measurement-debt

Mostly **recording-debt**, which is the cheaper class. Per-arm training return, advantage magnitude, and
the fraction of REINFORCE terms surviving `ADV_MIN_THRESHOLD = 0.005` all *existed at run time* inside
`_train_all_on_agent` and were simply never written to the manifest. Answering "did the shaped arm's
learner receive a denser signal?" therefore requires re-running an 11272-second experiment that already
happened. Per the Experimental Recording Standard
(`REE_assembly/evidence/planning/experimental_recording_standard_2026-07-12.md`, sec 3c family-keyed
payload) the repair is to **record** the readout in the re-run, not to re-run blind -- a blind re-run
reproduces the same blind spot at the same compute cost.

There is a genuine **test-design** component alongside it: C1's non-degeneracy flag needs redefining, and
the absorption check needs promoting from "a number in the manifest" to "a readiness precondition that
self-routes `substrate_not_ready_requeue`".

### Recommended `epistemic_category`

**`standard`** for both claims, blanket and per-claim.

Deliberately not `substrate_ceiling` and not `substrate_conditional`. Neither claim's *answer* is being
asserted to be gated on substrate work by this run, which tested neither of them; and both of those values
sit in `_EPI_SUPPRESS_PROPOSAL` (excluding the claim from GOV-GRAN-1 surfacing) and make the claim
not-v3-testable (starving it of experiment lanes). Stamping either would impose real downstream costs on
two claims this run never touched. `standard` is the enum-correct spelling of "no epistemic suppression
applies", and the failure-mode label -- *vacuous null via unabsorbed manipulation* -- lives in
`recommended_epistemic_category_note` where free text belongs.

Both targets are stamped rather than left null, so GOV-CEIL-1 and GOV-CAT-1 can see them.

---

## 7. Cluster pattern

**Scope stays `single`, deliberately.** But the shape across the portfolio is worth the user's attention at
the gate, and is recorded here rather than adjudicated:

| Leg | Run | Outcome | What actually happened |
|---|---|---|---|
| H2 (`representation` axis) | V3-EXQ-1030 | FAIL | Load-bearing C1 **suppressed** by a mis-specified readiness precondition; the positive control could not certify what it claimed to. Routed `queue-experiment`, repair 1030a. (Staged draft, `awaiting_human_confirmation`.) |
| H1 (`drive` axis) | V3-EXQ-1039 | PASS | Declared null **met vacuously** through a manipulation the consumer provably did not absorb. Routed `queue-experiment`, repair 1039a. |

Two independently designed legs, two independent instrument defects, neither caught before ~3 hours of
compute each, both found only at autopsy. This is not offered as "one structural property" -- the two
defects are genuinely different. What it may indicate is a **design-review gap at `/queue-experiment`**:
neither leg carried a way to certify its own instrument before spending the compute. That is a question
for the user and for that skill, not a claim-layer finding.

Re-adjudicating 1030 here is deliberately **not** done -- it has its own artifact, and folding it in would
double-count it under R1/R2.

---

## 8. Re-derive brake (MOVE-3)

**Does not fire.**

Recipe run 2026-09-16 over a `git archive origin/master evidence/planning` **mirror**, not the working
tree, for the reason given at the top.

| claim | counting hits | detail |
|---|---|---|
| **MECH-428** | **1** | `failure_autopsy_V3-EXQ-884_2026-08-03` (run `v3_exq_884_..._20260803T022131Z_v3`): category `precondition_unmet` + direction `non_contributory` + a `create` substrate entry that owes a build -> counts at R3 step 4 |
| **INV-086** | **0** | -- |

Threshold is 2. `1 < 2` and `0 < 2`.

Scan detail, for audit: the V3-EXQ-1004 target does **not** count for either claim -- it declares
`standard` per-claim, which the counter's per-claim short-circuit at the top of `counts()` excludes. The
staged V3-EXQ-1030 target is correctly **skipped** by the status filter (`awaiting_human_confirmation` is
in `UNSETTLED`). These are the same counts the 1004 and 1030 artifacts each independently recorded.
**This autopsy adds 0 to both**, because it declares `standard` per-claim for both.

So no same-claim re-queue is refused and routing is not forced to `implement-substrate`. That is
substantively right as well as arithmetically right: MECH-428 has still never had a single test that got
past its own precondition, and the V3-EXQ-1039a re-queue recommended below is not a re-test of either claim
-- it is an instrument repair on a claim-free discrimination leg, the same shape 1030 routed for the
sibling leg.

**The brake's spirit still constrains the successor**, and the routing note says so: do not buy more
episodes until you can show that an episode changes something.

## 9. Granularity-debt recurrence trigger

**Does not fire.**

`granularity_debt_cluster.py` run for both claims (targets whose own `claim_ids` name the claim -- not a
filename grep):

- **MECH-428** -- 2 targets across 2 files. `failure_autopsy_V3-EXQ-1004_2026-09-05` (alignment bucketed
  `other`: "not exercised"); `failure_autopsy_V3-EXQ-884_2026-08-03` (bucketed `unclear`). Distribution:
  `other=1, unclear=1`.
- **INV-086** -- 1 target. Distribution: `other=1`.

**No target reads `weakened` in either cluster**, which is the necessary condition. Per the skill's own
rule, a cluster with no `weakened` target is measurement or implementation debt, not granularity debt.

The reader's caution about free-text alignments was followed rather than waved past: both strings were read
in full, and neither carries a buried weakened reading (1004 says the claims were not exercised at all; 884
was a substrate-bug precondition failure). This autopsy adds a third non-weakened target, moving the
distribution further from the trigger, not toward it.

## 10. Fan-out (GOV-FANOUT-1)

**Omitted deliberately**, following the precedent the staged 1030 draft set for the sibling leg, for the
same reason.

There *are* **four** live candidate explanations for the failure to convert (section 3f: lPFC's share of
the modulatory accum; a zero gradient by any of three routes; budget; proposer-pool collapse). But they are
**instrument** hypotheses about why this leg could not be posed -- not rival scientific answers to the
registered question -- and all four are settled by **one** re-run carrying the telemetry and gates of
section 14. That is `complicated (buildable)`, not `complex (probe-gated)`; a fan-out portfolio would be the
wrong instrument. Appending them to the registered question's `hypotheses[]` would grow an
already-registered denominator with instrument legs for no scientific gain -- exactly the padding the
frozen-set invariants exist to prevent.

The H1/H2 portfolio stays at 2. No denominator move.

---

## 11. Step 7b -- mechanical pre-routing checks

`scripts/autopsy_pre_routing_checks.py --artifact <draft>.json --json`, first pass:
**`fire_count: 2`** (C2, C3); `inapplicable: [C5 -- prose-keyed, no sibling .md at that point]`.

**Both fires were ACTED ON, not dismissed.**

**C2-strict** -- *"`action='create'` for `['INV-086','MECH-428']`, but 2 entries already unblocked those
claims and are not mentioned"*: `SD-092` and `waypoint-proximity-field-observable`. The check is keyed on
the *target's* `claim_ids` and cannot see that the recommended entry's `unblocks_claims` is deliberately
empty (it is a shared-library recording gap that gates neither claim). Acted on: both entries are now named
explicitly in the artifact with the reason neither covers this gap -- `SD-092` is MECH-428's own cross-level
subgoal-credit build, already `implemented_*`, and says nothing about whether a training signal reaches a
consumer's parameters; `waypoint-proximity-field-observable` is the environment-side observable
(`implemented_validated`, released `corrupting` -> `degrading` by the confirmed 1004 autopsy) whose
validation opened this portfolio, held ON in every arm here and not re-varied.

**C3 -- STANDS, and is carried to the Step 8 gate. That is the prescribed disposition, not a loose end.**
The fire text: *"`lit_status` declares ABSENT, but 3 literature entries naming MECH-428 already existed."*

It was acted on first. The original draft read `"present for the reference mechanism ... ABSENT for the
narrower question"` -- the ambiguous shape. All three entries were then fetched and read in full on
origin/master (section 5), and `lit_status` was **changed to the flat value `present`**, with the narrow
gap moved into a separate `lit_status_note`.

It still fires, because C3 deliberately concatenates `lit_status` + `lit_status_note` before its substring
test. Its own docstring is explicit: *"C3 cannot read SCOPE ... Do not add a scope heuristic -- the scope
judgement is the reading agent's work."* So any honest statement of a scoped gap keeps it firing **by
design**. The word was **not** removed from the note to silence the tool: that would hide a true statement
in order to satisfy a check whose entire purpose is to surface it.

**Judgement recorded for the user.** The fire is a true positive for the *string* and a correctly-scoped
case on the *merits*. MECH-428's own claim literature is present -- three entries, all read, all
`supports`. What is absent is any entry on the narrow engineering question (can a prefrontal bias channel
bounded at `|0.1|` convert a reward-density manipulation into committed navigation), and this autopsy
deliberately **does not** commission a `/lit-pull` for it, because the absorption telemetry settles it far
more cheaply. **The user should confirm that non-commission at the gate.**

**Second run** (after the C2 fix and after this `.md` existed, so C5 could evaluate):
`fire_count: 1` (C3 only), `inapplicable: []`. C1-strict, C5 and C6-narrow did not fire on either run.

**Reminder for the gate, from the skill:** `inapplicable` is not "no fire", and a Step 7c CONFIRMED must
never be allowed to suppress a 7b fire. The two layers are not nested in either direction.

## 12. Step 7c -- adversarial red-team: RUN, verdict CONTESTED

**Model: Fable 5.1. Cross-model -- this draft was written on Opus 5.** Run by the coordinating session with
this session's reasoning withheld, per the independence rule. Findings:
`scratchpad/redteam_1039.md`; probe: `scratchpad/rt1039_probe.py`.

**VERDICT: CONTESTED.** The headline **survived every recompute**. Seven findings change what the artifact
*recommends*; none disturbs what it *concludes*.

**Every confirmer was re-run independently by this session before anything was applied.** All seven hold.
Nothing was accepted on the red team's assertion alone, and two of the findings correct errors that were
mine.

| # | Class | Disposition | My confirmer |
|---|---|---|---|
| **F1** | ROUTING | **Accepted in full** -- adds two 1039a preconditions, hypothesis (iv) | Probe re-run: seed 43 = **2 distinct first-action classes on 25/25** E3 ticks, seed 42 = 4-5. Manifest: demo seed 43 bit-identical to both arms. `mech294`/SD-061 verified verbatim on origin. |
| **F2** | ROUTING | **Accepted in full** -- adds a third routing item + exact replacement text | `git show origin/master:...1030....json` -> status `confirmed`, `confirmed_utc 2026-09-16T12:22:00Z`, and the string *"RESOLVED NEGATIVE ... (drive is excluded)"* in **both** named fields. |
| **F3** | ASSERTION (corrects **my error**) | **Accepted in full** | `rule_readout_consumer: bool = False` (`:181`), assignment guarded at `:429-450`, `config.py:4207`, x724 grep empty, probe prints `False`. |
| **F4** | Causal meaning unsupported | **Accepted as a reframe** | This run's own `last_score_diagnostics`: ratio 0.096-0.432, authority active, basis `'std'`. |
| **F5** | Unstated premise | **Accepted in full** | `_last_hidden_dead_relu_frac` at `:284/:462-467/:555`; probe spread 0.028-0.052 at init; `E2_TRAIN_IN_P1 = False`; ARC-065/MECH-314 text verbatim. |
| **F6** | Number (corrects **my number**) | **Accepted in full** | Recompute with the driver's anchor RNG: **253x / 491x / 254x, mean 301x**. My 1115x does not reproduce. |
| **F7** | Prose absolute vs cells | **Accepted in full** | Manifest: `lpfc_bias_head_moved: True` in both arms on seeds 43 and 44. |

**Findings rejected: none.** One **partial disagreement is recorded rather than dropped** (F1c): the red
team called the seed-43 demo identity a *contradiction* of section 3e's RNG argument. I record it as a
**narrowing**, not a contradiction -- 3e's claim was that RNG divergence *can* produce differences of this
size (seed 42 evidences that), and seed 43 shows the RNG-to-behaviour map is not uniform across seeds, which
is itself the attractor evidence F1 wants. What was genuinely wrong was my unqualified generalisation
across seeds. The applied fix is identical either way; only the recorded reason differs. Kept visible so a
later reader does not conclude the RNG reading was refuted when it was scoped.

**One finding of my own, surfaced while re-running F3's confirmer** and recorded in `red_team.findings[F3].bonus_finding_by_drafting_session`:
because `rule_readout_consumer` is False, `compute_bias` takes the **hard-clamp** branch
(`lateral_pfc_analog.py:483-485`), and the substrate's own comment at `:174-179` states that *"a saturated
hard clamp has zero gradient, so REINFORCE cannot move the head"*, citing V3-EXQ-822's `prop_delta` of
exactly 0.0. That is a **third** zero-gradient route, now recorded in 3f item 2 alongside F5's two.

---

## 13. Learning extracted

1. A treatment arm and its own control returned **bit-identical values on every recorded behavioural
   channel in every seed** while the treatment carried a per-episode training return **two-plus orders of
   magnitude** larger (250-500x across RNG draws; 301x cross-seed mean; 3-6 rewarded steps per 800 becoming
   ~300). Identity at that resolution is the absence of effect on **committed behaviour** -- not on the
   parameters, which did change in both arms on seeds 43 and 44. The declared null was met for a reason that
   has nothing to do with reward density, and would have been met under *any* reward function whatsoever.
2. `demo_ce_final_loss` = `ln(32)` to seven decimals after 232 applied optimizer steps, with
   `lpfc_bias_head_moved: False` on the same cell: the arithmetic signature of an exactly-zero gradient.
3. **The gate built for this defect passed while the defect was present.** When a red team names a failure
   signature, the gate must assert on *that signature*, not on a correlate of it.
4. A load-bearing criterion's non-degeneracy flag must be able to see the failure mode that would make the
   criterion vacuous. `criteria_non_degenerate = {'C1': r2['met']}` cannot observe the training phase at
   all -- nor the candidate pool.
   **And a diagnostic flag can be a constant.** `lpfc_candidate_summary_degenerate` is assigned only under
   `rule_readout_consumer` (default `False`, unset by the all-ON recipe), so C0d's degeneracy half read an
   `__init__` value and certified nothing. Reading a never-computed flag as a measurement is worse than
   having no flag: it converts an absent check into an apparent pass.
5. **Recording gap, not measurement gap**, on the deciding quantity -- the numbers existed at run time and
   were never written down. The repair is recording X, not re-running blind.
6. **Choosing a consumer for architectural faithfulness can select one that cannot express the
   manipulation.** The driver's reasoning was careful and its `WHAT THIS IS NOT` disclosure was accurate
   and made *in advance*. What was missing was the step from "this consumer's reward-contingent learning is
   two bounded bias heads" to "therefore it may be unable to express *any* drive-axis manipulation, so the
   design needs an absorption precondition before it can produce an interpretable null". The prerequisite
   was already on the record: `sd_actor_critic_action_learning`'s `current_blocker` field read *"action is
   learned only as a thin bias_head REINFORCE over the SD-056 prediction-trained encoder, and that frozen
   prediction latent is action-inadequate (737: 0.217 < raw-obs 0.567 < floor 1.0)"*.
7. **WITHDRAWN ARGUMENT, recorded not deleted.** The obvious repair -- re-pose H1 on the landed first-class
   actor-critic (`ree_core/action_learning/actor_critic.ActorCriticPolicy`, `implemented`, ready true)
   instead of the two-head bias REINFORCE -- was considered and is **not** recommended as the primary
   route. `V3-EXQ-742 mech457_actor_critic_onoff` ran that exact A/B three times (2026-07-13, 07-21,
   07-22), FAILed each time, and self-routed **`deeper_than_action_learning`**. Swapping consumers would
   route the leg into a lineage the corpus has already found insufficient and would confound the drive-axis
   question with the action-learning-substrate question. The cheap move first: make absorption visible on
   the consumer already chosen, and let the telemetry say whether a swap is warranted.
8. **A training-side absorption gate is not sufficient** (section 3g). The eval side has its own way of
   being insensitive: a collapsed candidate pool (2 distinct first-action classes of 32 at seed 43) means no
   bias on any candidate can produce more than a binary choice, so a *fully absorbed* manipulation still
   converts to nothing. A repair gated only on absorption would go green and reproduce this null -- the very
   gate-as-correlate defect this artifact diagnoses in C0d. **A repair whose gate reproduces the defect it
   was written against is not a repair.**
9. **Three distinct routes share one exactly-zero-gradient signature** -- identical hidden rows across
   candidates, a dead hidden ReLU, and hard-clamp saturation -- and naming only one was an unstated premise.
   Distinguishing them is one recording change (`hidden_dead_relu_frac`, already tracked but unrecorded, plus
   the per-tick summary pairwise spread), not three experiments.
10. **When two legs of one portfolio are autopsied by different sessions in the same window, each will cite
    the other's raw outcome before the other's adjudication exists** (section 16). A `PASS` on a diagnostic
    is exactly the shape most likely to be read as a resolution. The standing rule that a self-route label is
    a hypothesis and not a verdict has to be applied to **sibling artifacts**, not only to one's own manifest.
11. Cross-leg observation (section 7), surfaced for the gate, not claimed as a cluster adjudication.

---

## 14. Routing

**`queue-experiment`.**

Node classification: `complicated (buildable)`. The fix is a named build with no open scientific question
-- record the absorption telemetry and gate on it. It is explicitly *not* `complex (probe-gated)`: there is
no missing fact that requires a spike to obtain, only a missing record of facts that already occur.

### Primary -- `/queue-experiment` V3-EXQ-1039a

Same scientific question, same registered leg (`waypoint_field_consumer_reach` / `H-wpfield-objective-sparsity`),
so an **alphabetic suffix, not a new number**. No `1039a` driver exists (checked on disk and in
origin/main `experiment_queue.json`, max id V3-EXQ-1043). Required changes, in priority order. **Items 1
and 2 are a pair: shipping 1 without 2 reproduces the defect this artifact diagnoses.**

1. **An ABSORPTION readiness precondition set**, self-routing `substrate_not_ready_requeue` on failure:
   per-arm mean training return differs materially between `shaped_rl` and `sparse_rl`; the
   non-skipped-advantage fraction (terms surviving `abs(adv) >= ADV_MIN_THRESHOLD`) exceeds a declared floor
   in every treatment cell; `demo_warmstart`'s final CE falls materially below `ln(num_candidates)`.
   *Necessary but not sufficient* -- a stationary policy still accrues ~1.5 shaped return per episode
   (3a), so "returns differ" alone can go green on a policy that never moved.
2. **A CONVERSION-CAPABILITY readiness precondition set**, equally load-bearing and equally self-routing
   (added on red-team F1; confirmer reproduced for this revision):
   - **2a. Candidate first-action diversity.** Distinct first-action classes per E3 tick, recorded **per
     arm and per phase**, must be **>= 3 on a majority of ticks** in every treatment cell.
   - **2b. Eval-side bias-ablation sensitivity.** Evaluate each trained agent twice -- lateral-PFC bias
     head zeroed vs trained -- and require **at least one committed action to differ on at least 2 of 3
     seeds**, else `substrate_not_ready_requeue`.

   *Why:* every precondition in (1) is training-side, and the cells plus a 36-second probe point at a rival
   cause they cannot see (section 3g). Under proposer-pool collapse a fully absorbed manipulation still
   yields identical eval behaviour, so 1039a green on (1) alone would emit the same vacuous null behind a
   clean gate.

   *Existing art to cite, not re-derive:* `mech294_coherence_magnitude_strengthening` (GFLAG-0183; ARC-065
   SP-CEM pool `floor_clamped_at_2_distinct_first_action_classes`); **SD-061**
   (`candidate_first_action_entropy` regulator, `implemented_pending_validation` -- the existing lever);
   ARC-065/MECH-314 (E2 world-forward collapsing K candidates to an identical first-step `z_world`).
   *On the floor:* `>= 3` sits deliberately between the registered 2-class clamp and the 4.5 classes
   MECH-341's falsifier treats as a diverse pool. **4.5 is the arguable stricter alternative -- a gate
   question.**
3. **Record the readouts** named in the substrate entry: per-arm return distribution, advantage magnitude,
   non-skipped fraction, bias-head weight-norm delta as a **float** rather than a boolean,
   `hidden_dead_relu_frac`, per-tick candidate-summary pairwise spread, and -- from E3's existing
   `last_score_diagnostics` -- the lPFC **share** of the summed modulatory accum rather than the absolute
   bias bound.
4. **Replace `criteria_non_degenerate = {'C1': r2['met']}`** with a flag covering C1's actual validity:
   absorption **and** conversion-capability **and** eval mobility, not mobility alone.
5. **Reconsider the 90-episode budget only after (1)-(4).** A power-bump on a design whose manipulation may
   be structurally unable to convert is exactly the sequential-letter burn the re-derive brake exists to
   stop. The brake does not fire here; its spirit applies.

### Secondary -- `/governance` writes a `substrate_queue.json` entry

`action: create`, `sd_id_suggested: sd-allon-training-signal-absorption-telemetry`, priority 2,
**severity `degrading`**, `unblocks_claims: []`, paths
`experiments/_lib/allon_training.py::_train_all_on_agent` (+ the two REINFORCE loss functions).

Severity reasoning, because it is the contestable call: `degrading`, not `corrupting`, on **blast radius**
-- the same argument the confirmed 1004 autopsy and the staged 1030 draft each made. `/queue-experiment`
Step 2.5c matches `substrate_paths` at *module* granularity, and `experiments/_lib/allon_training.py` is
entered by the whole 724/734/737/742/808 all-ON family plus `_lib/mech457_fanout.py`; a `corrupting` stamp
would STOP-gate that entire programme **including the 1039a repair this autopsy routes**. On the merits
`degrading` is also right for the general case: for an experiment using this recipe as a *fixed training
procedure*, the missing telemetry weakens confidence without invalidating anything. It is genuinely
corrupting only for the narrow sub-class whose *manipulation* is on the reward/training-signal channel --
one experiment so far, this one. **Question for the user at the gate:** carve that narrow sub-class out as a
separate `corrupting` entry, or leave it at `degrading` with the note? This autopsy does not assume the
answer.

### Third -- cross-artifact correction against the CONFIRMED V3-EXQ-1030 artifact

Added on red-team F2; confirmer re-run for this revision.
`failure_autopsy_V3-EXQ-1030_2026-09-14` was **confirmed on origin/master at 2026-09-16T12:22:00Z** -- 15
seconds after this draft's own `generated_utc` -- by the user at an interactive Step 8 gate. Its confirmed
prose now asserts, in **both** `targets[0].fanout_recommendation.note` and
`targets[0].in_flight_work_not_to_re_propose[0]`, that V3-EXQ-1039 *"RESOLVED NEGATIVE, which strengthens
the case for re-running THIS H2 leg (drive is excluded)"* -- and hands "drive is excluded" to V3-EXQ-1030a
as a design premise.

**It is not resolved.** This autopsy finds the H1 null vacuous, so H1 is unresolved in *either* direction
and drive is *not* excluded. The contradiction is also **internal to 1030**: its own
`hypothesis_space_ledger_pending` block still reads "0 of 2 resolved", agreeing with this artifact and
disagreeing with its own prose.

**Route:** `governance_flag.py raise --flag-type evidence_discrepancy`, or a direct amend by the session
holding the artifact (`TASK_CLAIMS` shows `account-handover-20260916-walkthrough` holding the registry and
the staged autopsy JSONs including 1030). **This session edits nothing** -- exact replacement text for both
fields, preserving the existing `SUPERSEDED` / `ORIGINAL` tails, is in the JSON's
`cross_artifact_correction.exact_replacement_text`, written to be applied verbatim. If `/governance` chips
V3-EXQ-1030a from 1030's `step8_gate_decisions`, **the chip prompt must not carry "drive is excluded"
forward.**

### Not routed

- **No `/lit-pull`** -- the open question is mechanical, not literature-shaped, and the claim's own
  literature is present (3 entries, section 5). The rival cause added at 3g is likewise already registered
  substrate art (`mech294`, SD-061, ARC-065/MECH-314), not a literature gap.
- **No `/implement-substrate` build against either claim** -- the brake does not fire and neither claim was
  tested.
- **No `/claim-synthesis`** -- the granularity-debt trigger does not fire; no target in either cluster reads
  `weakened`.
- **No `spawn_task`.** Per CLAUDE.md Session Land Protocol step 6 and the skill's Step 8 rule, the routing
  confirmed here is a proposal until `/governance` Step 2b ratifies it. Governance chips it, not this
  session.

### Draft `evidence_quality_note` for governance

The exact text is in the JSON at `targets[0].recommended_evidence_quality_note`. Per-claim dispositions:

| claim | direction | category | `diagnostic_evidence_adjudicated` | status | change tail |
|---|---|---|---|---|---|
| INV-086 | `non_contributory` | `standard` | `true` | none -- stays `candidate` | `-> stamp this artifact` |
| MECH-428 | `non_contributory` | `standard` | `true` | none -- stays `candidate` | `-> stamp this artifact` |

**Why the tails end on a citation stamp rather than a field value.** Both claims' current values were read
from `origin/master:docs/claims/claims.yaml` before the tails were written, per the already-true-tail rule.
INV-086 and MECH-428 *both already carry* `epistemic_category: standard`, `diagnostic_evidence_adjudicated:
true` and `status: candidate`, and MECH-428 already carries `pending_retest_after_substrate: true` -- so
every candidate field tail would be already-true and would clear GOV-APPLY-1 *without anything having been
applied*. What genuinely moves is the provenance: `live_status.evidence.from` currently reads
`failure_autopsy_V3-EXQ-1004_2026-09-05` for both. `stamp this artifact` is therefore not-yet-true and
stays ACTIONABLE until governance applies it.

`MECH-428.pending_retest_after_substrate` **stays `true`**, for the reason the confirmed 1004 autopsy gave
and the staged 1030 draft restated: the SD-094-enabled retest of V3-EXQ-884 as **V3-EXQ-884a has still
never run**, and this run is not it. This autopsy adds no new substrate blocker against MECH-428 -- the
recording-gap entry it recommends does not name MECH-428 in `unblocks_claims`.

## 15. Step 9b -- frozen ledger (DRAFTED ONLY, not applied)

- **Growth-restriction check:** question `waypoint_field_consumer_reach` carries `growth_restriction: ""`
  -- key **present and empty** on origin/master as of 2026-09-16. Empty means no STOP condition, so there is
  nothing to carry verbatim to the Step 8 gate and no redirect-to-a-new-`qid` decision to put to the user.
  Recorded explicitly because an absent check reads identically to a passed one.
- **Mode B (resolve) -- and the resolution is deliberately a NON-resolution.** `H-wpfield-objective-sparsity`
  stays `alive`; `resolving_runs: ["V3-EXQ-1039"]`; `evidence_direction` stays `pending`;
  `met_elimination_bar: false`; `resolved_utc: null`; `adjudicating_runs` extended to
  `["V3-EXQ-1039", "V3-EXQ-1039a"]`. Per the state-mapping table, a run that does not discriminate leaves
  the leg alive with `resolving_runs` and `basis` recorded.
- `control_passed: true` (the positive control `greedy_oracle` cleared `ORACLE_FLOOR` at 10.8-12.0 vs 4.0,
  and the R1 premise held at 0.2 vs a 4.385 bound). `non_degenerate: true` -- **reproducing the manifest's
  own flag faithfully, and qualified in the `basis` rather than silently overridden**, since that flag is
  derived solely from R2 eval mobility and certifies nothing about C1's validity here.
- **Decision block:** `live_gate` and `distance_phrase` updated to record that both legs have now run and
  neither discriminated; a new `observation_bottleneck` recorded for H1 (no validated readout certifies
  that a training-signal manipulation was absorbed). `decidable` stays `false`;
  `decision.decision_log_ref` untouched -- that is a human's entry.
- **No denominator move.** `initial_frozen_count` stays 2, `initial_frozen_count_at_registration` stays 2,
  no hypothesis added or removed, no `fanout_growth_events` or `discovery_growth_events` entry, and
  `fanout_sources` is not extended. Invariants 1, 2, 3, 4 and 7 all preserved.
- **Coordination warning for whoever applies this:** the staged `failure_autopsy_V3-EXQ-1030_2026-09-14`
  carries its **own** unapplied pending block against the **same question**. Apply both in **one** edit --
  both touch the same `decision` block, and applying them separately will leave a stale `distance_phrase`.

---

## 16. What the Step 8 gate needs to decide

**Step 7c ran: Fable 5.1, cross-model (this draft was written on Opus 5). Verdict CONTESTED** -- headline
survived every recompute, seven findings changed the recommendations, all seven confirmers independently
re-run and holding, none rejected, one partial disagreement recorded (section 12).

1. **Is the vacuity verdict accepted?** That a null between two arms which produced literally identical
   committed behaviour under a return difference of two-plus orders of magnitude is a statement about the
   instrument, not about reward density. *(Unchanged by the red-team pass; strengthened by it.)*
2. **THE CROSS-ARTIFACT CORRECTION -- the most consequential item, because another artifact is already
   confirmed and acting on the opposite reading.** `failure_autopsy_V3-EXQ-1030_2026-09-14` was confirmed
   at a user gate 15 seconds after this draft was generated, and asserts that V3-EXQ-1039 *"RESOLVED
   NEGATIVE"* and that *"drive is excluded"*, handing that premise to V3-EXQ-1030a. **This autopsy says H1
   is not resolved in either direction.** 1030's own registry block already agrees with this artifact ("0
   of 2 resolved"), so 1030 is internally inconsistent too. Confirm the `evidence_discrepancy` correction
   and the verbatim replacement text (section 14, JSON `cross_artifact_correction`) -- and confirm that any
   1030a chip does not carry "drive is excluded" forward.
3. **The two NEW 1039a conversion-capability preconditions** (section 14 item 2) -- and specifically the
   first-action-diversity **floor: `>= 3`** as recommended, or MECH-341's stricter **4.5**? The registered
   clamp is at 2; the probe found 2 of 32 at seed 43 and 4-5 at seed 42, so the choice between 3 and 4.5
   decides whether seed 42 would also be gated out.
4. **Severity of the substrate entry** -- `degrading` as recommended, or carve out the narrow
   reward-channel-manipulation sub-class as a separate `corrupting` entry (section 14)?
5. **`create` vs fold-into-`sd_actor_critic_action_learning` as an `amend`** -- this autopsy recommends
   `create` because the two are different kinds of work and because folding the telemetry gap into a build
   whose own validation lineage self-routed `deeper_than_action_learning` would bury it. Governance may
   reasonably disagree.
6. **The cross-leg observation** (section 7): is "neither leg could certify its own instrument before
   spending the compute" worth a `/queue-experiment` design-review change, or is it two unrelated bugs?
   Note this now has a third instance -- 1030's own confirmed prose over-reading a sibling's PASS.
7. **A governance-mechanics point the gate should not discover later.** `live_status.evidence.from` is
   **single-valued**, and both this artifact and the already-confirmed 1030 recommend stamping it on the
   *same two claims* (INV-086, MECH-428) -- 1030 has not been stamped yet, its `from` still reads
   `failure_autopsy_V3-EXQ-1004_2026-09-05`. Whichever stamp lands second wins the field, so **the
   `evidence_quality_note` text of the first must be preserved when the second is applied**, or one of the
   two non_contributory co-tag dispositions becomes unreachable from the claim.

Both Step 7b fires were handled: **C2 discharged**, **C3 stands as a correctly-scoped fire carried here**
(section 11) -- confirm the deliberate non-commission of a `/lit-pull`. Per the skill, the CONTESTED verdict
does **not** suppress the standing C3 fire; the two layers are independent.

## Step 8 gate outcome -- CONFIRMED 2026-09-16T13:06:22Z

CONFIRMED as recommended (Fable cross-model red-team, 7 findings applied): the PASS is a VACUOUS null (shaped_rl bit-identical to sparse_rl on every behavioural channel in 3/3 seeds; demo_warmstart CE = ln(32) with zero gradient; readiness gate C0d passed while the signature was present); direction non_contributory for INV-086 and MECH-428, category standard, both stay candidate, MECH-428 pending_retest_after_substrate stays true, change tails 'stamp this artifact'; substrate CREATE sd-allon-training-signal-absorption-telemetry (degrading); routing queue-experiment (V3-EXQ-1039a with the PAIRED readiness gate: absorption + conversion capability incl. >=3 distinct first-action classes and a bias-head ablation sensitivity check; governance chips it); the confirmed 1030 artifact's 'H1 resolved negative / drive excluded' text AMENDED in this same commit per cross_artifact_correction; Step 7b C3 fire recorded as a deliberate NON-commission of /lit-pull (MECH-428 literature is present). Ledger: H-wpfield-objective-sparsity stays alive with V3-EXQ-1039 recorded; decision block updated (0 of 2 resolved).
