---
title: "SD-e1-rollout-consistency-training: e1.transition.action_conditioning + rollout_consistency"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 13
---

# SD-e1-rollout-consistency-training: e1.transition.action_conditioning + rollout_consistency

**Claim ID:** SD-e1-rollout-consistency-training
**Subject:** `predictors.e1_deep.E1DeepPredictor.transition`
**Status:** ITEM 1 IMPLEMENTED (2026-08-29, VALIDATED by V3-EXQ-965 2026-08-30) / ABSOLUTE-VS-RESIDUAL BRANCH CLOSED (substrate 2026-09-01, V3-EXQ-968 returned no material difference) / ITEM 2 SUBSTRATE IMPLEMENTED 2026-09-01 (candidate 1; validation experiment owed)
**Registered:** 2026-08-03 (substrate_queue.json)
**Depends on:** none unresolved (probe-gating discharged by V3-EXQ-954, 2026-08-29)
**Blocks:** INV-088, MECH-135 (both carry `pending_retest_after_substrate: true`)

## Problem

V3-EXQ-108b measured E1's long-horizon rollout evaluator as degenerate:
`e1coe_score_var` = 1.65e-13 / 2.25e-14 against a `C3_VAR_THRESHOLD` of 0.002, and
`CR_rollout/CR_real` ~ 3e-6 against a `CR_ROLLOUT_COLLAPSE_RATIO` of 0.1. Forty distinct
candidate action sequences produced near-identical imagined endpoints.

Two mechanisms were simultaneously present in the code and either would produce collapse:

- **(a) horizon mismatch** -- E1 is trained at `horizon=1` and used at `horizon=30`, with no
  objective term covering steps 2..30.
- **(b) action-blindness** -- E1's transition takes no action at all. `forward()` and
  `predict_long_horizon()` have no action parameter, and inside `predict_long_horizon` the
  LSTM seed is `cat([zeros(self_dim), prior])`, so the real `z_self` never reaches the LSTM
  and the entire action signal is squeezed through one `world_dim`-wide `prior_generator`
  projection.

The commissioned literature review
(`evidence/literature/targeted_review_e1_forward_model_rollout_consistency/SYNTHESIS.md`,
2026-08-03) confirmed (a) as a named, well-studied failure family with four grounded
training-objective levers -- and then found that **every one of those four levers
presupposes an action-conditioned transition**. If (b) dominates, all four are misdirected.

## The probe that settled it

**V3-EXQ-954** (2026-08-29, PASS, diagnostic; confirmed autopsy
`evidence/planning/failure_autopsy_V3-EXQ-954_2026-08-29.md`) ran the synthesis Section 4
pre-registered discrimination. Pre-registered decision rule: (a) predicts smooth degradation
with depth and health at h=1; (b) predicts already-floored at h=1 plus near-zero direct
per-action divergence.

Observed, both seeds in perfect agreement:

| Measurement | Value | Bar |
|---|---|---|
| `cr_ratio` at h=1 | 4.76e-07 / 5.39e-07 | 0.1 |
| `cr_ratio` at h=30 | 6.05e-06 / 8.16e-06 | 0.1 |
| `CR_real` (denominator) at every h | 0.17 - 0.24 | 1e-4 |
| one-step per-action probe ratio | 1.23e-06 / 8.77e-07 | -- |

Floored **before any compounding could occur**, with a flat-to-mildly-rising depth profile
and a healthy horizon-matched denominator. The (b) signature exactly; the (a) signature
absent.

**Red-team attribution pass** (`redteam_954.md`), replicating the recipe with the driver's
own functions: trained E2 per-action `z_self` divergence = **2.8e-2** (~5% of `||z_self||`)
against **5.6e-6** at the E1 output -- a **~5,000x attenuation inside E1**, decomposing as
`prior_generator` ~7x and **LSTM + output_proj ~675x, the dominant crush**. E2 is exonerated.

**Consequence: the work order inverts.** Action-conditioning the transition is item 1; the
multi-step / rollout-consistency objective is item 2. The objective change remains a real
second item precisely because the dominant crush is at the LSTM+output_proj stage, which an
interface change alone may not reach.

## Solution -- ITEM 1 (implemented 2026-08-29)

Action-condition E1's transition. Three `E1Config` knobs, all no-op at default:

| Param | Type | Default | Purpose |
|---|---|---|---|
| `action_conditioned_transition` | bool | `False` | master switch |
| `action_dim` | int | `4` | one-hot action width; mirrors `E2Config.action_dim` |
| `action_cond_unzero_self_slot` | bool | `True` | fill the zeroed `z_self` LSTM slot with the real `z_self`; **inert unless the master switch is on** |

**Interface.** `predict_long_horizon(current_state, horizon=None, actions=None)` and
`forward(current_state, horizon=None, z_goal=None, actions=None)`. `actions` accepts either
`[batch, action_dim]` (one action held across the whole rollout) or
`[batch, horizon, action_dim]` (a per-step action sequence -- what a candidate-sequence
evaluator supplies). Both shapes are needed by existing consumers.

**Dedicated input channel, not a projection.** When the master switch is on,
`transition_rnn` is constructed with `input_size = total_dim + action_dim` and the per-step
input is `cat([state_i, action_encoder(a_i)])`. The rejected alternative -- projecting
`[state, action]` back down to `total_dim` before the LSTM, as `goal_input_proj` (MECH-116)
does for goals -- would re-impose a width-64 squeeze on exactly the signal this SD exists to
un-squeeze. The failure mode has a recorded precedent in this same file: the EXQ-449a comment
at `e1_deep.py:251-256` records `cue_action_proj` output at per-channel std ~2.7e-8 because
its input was swamped. A dedicated channel has no mixing bottleneck at the interface.

**Un-zeroing the `z_self` slot.** Under `action_cond_unzero_self_slot`, the LSTM seed becomes
`cat([current_state_self_half, prior])` instead of `cat([zeros, prior])`. Kept on its own
sub-flag so the two defects named above are separately ablatable -- a validation experiment
can attribute any movement to the action channel or to the un-zeroing, not merely to "the
flag".

**Data flow.**

```
env action -> one-hot -> REEAgent._action_experience_buffer
   -> E1.action_encoder  (Linear(action_dim, action_dim), E2's convention)
   -> per-step LSTM input  cat([state_i, a_enc_i])      [dedicated channel]
   -> transition_rnn -> output_proj -> predictions
```

**Buffer alignment (subtle, pinned by contract).** `REEAgent.sense()` can only observe
`a_{t-1}` -- the action that produced the current observation. So the action stored alongside
`state_t` is the one that *led to* `state_t`, and the action leading `state_i -> state_{i+1}`
is the one stored alongside `state_{i+1}`. `compute_prediction_loss` therefore slices
`action_buf[start_idx+1 : end_idx]`. An off-by-one here trains the model on the wrong
conditioning and would look like success at the shape level while learning nothing.

**Missing-action instrumentation.** With the master switch on and `actions=None`, the
transition falls back to a zero action vector (so legacy internal callers such as
`integrate_experience` keep working) and increments
`E1DeepPredictor._action_cond_missing_calls`. A validation experiment asserts this counter is
0 on the paths it measures -- otherwise an ON arm can silently be an OFF arm, which is exactly
the vacuity class the 108/108a history warns about.

**Backward compatibility.** With `action_conditioned_transition=False`: no `action_encoder` is
constructed, `transition_rnn.input_size` is unchanged, no construction-time RNG is consumed
for the new path, and `predict_long_horizon` takes the pre-existing branch verbatim.
Bit-identical.

**Not required:** phased training (no new head trains on a moving latent target; the action
encoder trains under the existing `compute_prediction_loss` MSE). **MECH-094:** not
applicable -- this SD adds no new content-to-memory write path.

## Solution -- ITEM 2 (candidate 1 substrate landed 2026-09-01; validation owed)

The multi-step / rollout-consistency training objective. Candidate ranking from the
synthesis, Section 3, all of which presuppose item 1 and none of which should be adopted
before item 1's validation reports:

1. **Multi-step latent consistency over an action-conditioned transition (TD-MPC-style)** --
   strongest template; transposes to E1's deterministic MSE without reinterpretation. Must be
   additive: E1 is a general world model with several consumers, not a task-oriented model.
2. **Scheduled multi-step unrolling (DaD)** -- cheapest, correct distribution-shift diagnosis,
   no architecture change; not expected to move C3 alone.
3. **Direct sequence-conditioned endpoint model (Asadi)** -- best fit to what the evaluator
   actually consumes, but `|A|^H` generalisation at horizon 30 is unresolved, and it would be
   an added head, not a fix to E1.
4. **Latent overshooting (PlaNet)** -- grounded but **not endorsed by its own ablation** for
   deterministic-RNN architectures. Do not adopt by default.
5. **Contrastive next-state** -- de-prioritised; no long-horizon anchor found, and the one
   relevant comparison (TD-MPC) went the other way.

The ~675x LSTM+output_proj crush is item 2's real target. A related suspect surfaced while
building item 1 and is recorded here rather than acted on: `output_proj` predicts the
**absolute** next state, where E2 uses a residual `z + delta(z, a)` parameterisation. If the
item-1 ON arm still shows crushed per-action divergence at the E1 output, that
parameterisation is the next thing to test.

### The absolute-vs-residual branch -- FIRED (substrate landed 2026-09-01)

That branch condition is **met**. V3-EXQ-965 (confirmed autopsy, 2026-08-30) validated
ITEM 1 -- the dedicated `actions=` channel produces real per-action divergence at the E1
output on a trained model (ON arms 1.46e-03..2.19e-03 mean pairwise L2 against an A_off arm
at exactly 0.0) and `cr_ratio(h=1)` rises 6455x-9775x to 2.67e-03..3.96e-03 -- and the ON arm
is nonetheless still **25-37x short** of the 0.1 evaluator bar, with `e1coe_score_var` 5-7
orders below 0.002. So the ON arm does still show crushed divergence relative to what the
evaluator consumes, which is exactly the condition this branch was pre-registered against.

(Scope caveat, carried from the autopsy: that reading rests on the run's recorded
pairwise/`cr_ratio` data, **not** on its own C1 criterion, which divides by an analytically
zero control and is uninterpretable. Do not cite the 57809x figure. And note this does
**not** make MECH-135 / INV-088 retestable -- the bars are still missed by wide margins.)

**Substrate, landed 2026-09-01.** `E1Config.output_proj_residual` (default `False`) switches
each rollout step in `predict_long_horizon` from

```python
predicted = self.output_proj(output.squeeze(1))            # absolute next state
```

to

```python
predicted = state_i + self.output_proj(output.squeeze(1))  # E2's z + delta(z, a) form
```

in **both** rollout branches -- the ITEM 1 action-conditioned one and the legacy one -- so
`forward()` and `predict_long_horizon()` (the two `substrate_paths` on this entry) are both
covered by the one change. The form is copied from `e2_fast.py`'s `self_forward` /
`world_forward` rather than invented; no scaling, gate, or extra module is introduced.

The knob is **independent of `action_conditioned_transition`** on purpose: it parameterises
the state recurrence, not the action channel, and the discrimination is an A/B *on* the
ITEM 1 ON arm, so both knobs must be separately settable.

No module and no parameter is added in either setting, so unlike `action_encoder` there is
no construction-time RNG asymmetry to defend against -- verified by loading the pre-change
`e1_deep.py` alongside the new one and confirming, from the same seed, identical parameters
and bit-identical rollouts across three configuration shapes (legacy; ITEM 1 ON with a held
action; ITEM 1 ON with `action_cond_unzero_self_slot=False`).

Contract: `ree-v3/tests/contracts/test_e1_output_proj_residual.py`. It pins OFF against a
hand-rolled replication of the legacy loop (not a frozen constant), parameter identity across
the flag, the h=1 algebraic identity `ON == seed + OFF` (which catches a knob wired to the
wrong residual base, where a looser "the numbers moved" check would not), non-vacuity in both
branches, gradient still reaching `output_proj`, and `from_dims` reachability. It deliberately
does **not** assert that residual beats absolute -- that is the experiment.

### The A/B result -- V3-EXQ-968, 2026-09-01: NO MATERIAL DIFFERENCE

The A/B was queued and run the same day
(`v3_exq_968_sd_e1_output_proj_residual_ab_20260901T162647Z_v3`, outcome PASS,
`experiment_purpose: diagnostic`, `evidence_direction: non_contributory`). Both arms
ITEM 1 ON, 2 seeds, absolute vs residual `output_proj`.

Interpretation label: **`residual_no_material_difference`**.

| seed | `cr_ratio(h=1)` absolute | `cr_ratio(h=1)` residual | residual/absolute lift |
|---|---|---|---|
| 42  | 2.673e-03 | 5.909e-03 | **2.21x** |
| 123 | 2.717e-03 | 9.227e-04 | **0.34x** |

**Read this carefully, and do not compress it into a direction.** The two seeds disagree in
SIGN: residual is ~2.2x better on seed 42 and ~0.34x, i.e. worse, on seed 123. Neither
approaches the pre-registered `lift_factor_abs_floor` of **3.0** (derived from the absolute
arm's own cross-seed noise, `measured_absolute_arm_noise_ratio` 1.016). Both
`residual_materially_exceeds` and `residual_materially_below` are **false** on both seeds.
That sign-inconsistency against an unmet floor is exactly why the label is "no material
difference" -- it is **not** a finding that residual is worse, and **not** a finding that
residual is better. All five readiness preconditions were met (encoder trained,
`CR_real(h=1)` non-degenerate at 40 surviving samples, `missing_action_calls` = 0,
`direct_action_supply_fraction` = 1.0, `cr_ratio(h=1)` finite), so this is a real
comparison that returned null, not a vacuous one.

**Consequence.** The doc's own pre-registered cheap branch is now spent, and it did not
relieve the crush. `output_proj_residual` stays in the substrate, default-off, as a
characterised null rather than a recommendation. ITEM 2 is the remaining route, and the
~675x LSTM+output_proj crush remains its target -- now known not to be a mere
parameterisation artefact.

### ITEM 2 substrate -- candidate 1, landed 2026-09-01

`E1DeepPredictor.rollout_consistency_loss(initial_state, targets, actions=None,
horizon=None, horizon_weights_decay=None, simulation_mode=False)`, gated by four
`E1Config` knobs, all no-op at default:

| Param | Type | Default | Purpose |
|---|---|---|---|
| `e1_rollout_consistency_enabled` | bool | `False` | master switch |
| `e1_rollout_consistency_weight` | float | `1.0` | caller-side scaling; the helper returns the UNWEIGHTED horizon-mean |
| `e1_rollout_consistency_horizon` | int | `5` | rollout depth the objective covers |
| `e1_rollout_consistency_horizon_weights_decay` | float | `1.0` | `w_t = decay ** t`; 1.0 = uniform, <1.0 = TD-MPC discounting |

The objective rolls the transition out autoregressively from `initial_state` under
`actions` and penalises per-step deviation from the OBSERVED latent trajectory:
`L = sum_t (w_t * MSE(pred_t, targets[:, t, :])) / sum_t w_t`.

**What this adds over `REEAgent.compute_prediction_loss`, which is the question that
nearly stopped this build.** That method ALREADY rolls E1 out autoregressively to
`prediction_horizon` and MSEs the whole trajectory, and post-ITEM-1 it already supplies the
executed action sequence (agent.py, the `_e1_actions` slice). So the multi-step FORM was
present on the agent-loop path before this landing, and candidate 1 is not the greenfield
build the ranked list makes it sound like. Two things were genuinely missing:

1. **The per-step discount.** `F.mse_loss` over the stacked rollout weights every horizon
   step equally. Under an autoregressive rollout deep-step error is larger by construction,
   so a flat mean lets the deepest steps dominate the gradient; `decay < 1.0` is TD-MPC's
   actual form. At `decay=1.0` this helper reduces to the flat form to within float32 reduction-order error (the helper reduces per-step then weights; F.mse_loss reduces over all elements at once -- mathematically equal, different summation order, measured 6.4e-08 RELATIVE at worst and bit-identical on the legacy branch) --
   so the discount is the only behavioural axis added. The contract asserts that identity
   at `rtol=1e-6`, NOT bit-exactly: an earlier revision asserted bit-identity and was
   machine-class flaky, passing on `ree-worker-4` while failing on `darwin-arm64`. A
   float32-eps tolerance still catches every real defect here, since a wrong denominator,
   a t=1 weight origin, or a dropped step is wrong by a FACTOR.
2. **Reachability.** `compute_prediction_loss` is only reachable through the agent loop, and
   **every driver in this SD's own lineage bypasses it**, training E1 directly and
   single-step teacher-forced: `F.mse_loss(e1_pred[:, 0, :], total_curr.detach())` at
   V3-EXQ-954:312, V3-EXQ-965:409 and V3-EXQ-968:431. So the multi-step objective has never
   once been exercised in the lineage that motivated this SD. The doc's Problem section
   states defect (a) as "E1 is trained at `horizon=1`" -- that is true of these DRIVERS, not
   of the substrate, and the distinction was not previously recorded here.

**Not phased-training-gated:** no new head trains on a moving latent target; the objective
trains existing `transition_rnn` / `output_proj` weights. **MECH-094:** carried anyway as a
`simulation_mode` gate returning zero, matching SD-056's helper convention -- replay / DMN
paths cannot recruit the objective.

**`compute_prediction_loss` is deliberately NOT rewired.** Agent-loop wiring would change a
path several hundred experiments depend on, for no consumer that exists yet; it is held
until the validation experiment reports.

Contract: `ree-v3/tests/contracts/test_e1_rollout_consistency_loss.py` (24 tests). It pins
the flat-form identity at `decay=1.0` (at float32-eps tolerance, and the docstring says why not bit-exactly), the discount's SIGN (against a target whose
error is concentrated at the deep end, so an inverted exponent fails), that gradient reaches
BOTH `output_proj` and `transition_rnn` (the ~675x crush's location -- an objective that
cannot deliver gradient there cannot move it), that deep-step-only error still produces
gradient (otherwise this is a single-step loss wearing a horizon argument), hidden-state
save/restore, the MECH-094 gate, grad-connected degenerate returns, horizon clamping,
fail-closed shape validation, and all three `from_dims` wiring sites. It deliberately does
**not** assert that multi-step beats single-step -- that is the experiment.

### Why candidate 1 and NOT a rollout-endpoint contrastive

A contrastive objective over candidate action SEQUENCES was designed and deliberately not
built (2026-09-01). It would have been named `e1_rollout_sequence_divergence_*`, never
"next-state contrastive", because it is genuinely a **different objective** from the
synthesis's de-prioritised #5: #5 constrains the one-step transition `f(z, a)`, whereas this
would constrain the **iterated map** under action sequences -- which is what the C3
evaluator actually consumes (it scores 40 sequences, not 40 single actions). So #5's "the
one relevant comparison (TD-MPC) went the other way" does not settle it.

It was rejected on the OTHER half of #5's objection. *"No long-horizon anchor found"* applies
to a long-horizon contrastive with **more** force, not less: extending contrastive to long
horizon is precisely the unanchored move, where a t=1 next-state contrastive at least has
Srivastava 2021 behind it (the verdict that grounded SD-056's t=1 landing). And the in-repo
precedent that looked like a warrant does not survive checking: E2's SD-056 multi-step
contrastive amend (`e2_fast.py`, 2026-05-31) is **built but never validated** --
`e2_action_contrastive_multistep_enabled` is `true` in **zero** runs across the entire
evidence corpus, measured 2026-09-01. It shows the shape is implementable, not that it works.

The remaining argument for preferring it over candidate 1 was that an accuracy objective
"already trains" the crushed weights and so would not move them. **That was intuition, not
measurement, and it is recorded as such**: no experiment in this lineage has ever trained E1
with a multi-step objective at all, so there is no observation of what one does to the
crush; and the phrase described `compute_prediction_loss`, code this lineage never executes.
Candidate 1 is the doc's ranked-strongest AND the untried one. A null on it narrows ITEM 2's
real target and buys the departure to a contrastive with evidence rather than intuition.

## Architecture Context

E1 is the long-horizon world model; E2 is the fast motor-sensory transition model. SD-056
already established action-conditional divergence preservation on E2's `world_forward`; this
SD brings E1's transition to the same interface standard. E1's other consumers --
`generate_prior` (HippocampalModule terrain conditioning, SD-002), MECH-151 `action_bias`,
MECH-216 schema salience -- all read the per-step trajectory and are unaffected by an
additive input channel.

## What This SD Enables

- **INV-088** (`inv088_evaluator_degeneracy_cause`) and **MECH-135**, both currently
  `pending_retest_after_substrate: true`, become retestable once item 1 lands.
- Any evaluator that scores candidate action sequences through E1 -- the C3 measurement in the
  108 lineage is the canonical consumer.
- Item 2, which is misdirected without item 1.

## Related Claims

INV-088, MECH-135, SD-056 (E2 action-conditional divergence preservation), SD-002
(associative prior into HippocampalModule), MECH-116 (E1 goal conditioning -- the in-file
precedent for optional conditioning), MECH-151, MECH-216, SD-016 (ContextMemory read path).

## Evidence

- `evidence/planning/failure_autopsy_V3-EXQ-108b_2026-08-03.md` -- the original collapse.
- `evidence/planning/failure_autopsy_V3-EXQ-954_2026-08-29.md` -- the discriminating probe
  and the red-team attribution; the basis for the item-1-before-item-2 ordering.
- `evidence/literature/targeted_review_e1_forward_model_rollout_consistency/SYNTHESIS.md` --
  the four objective levers and the code-verified observation that all four presuppose an
  action-conditioned transition.
- `evidence/experiments/v3_exq_968_sd_e1_output_proj_residual_ab_20260901T162647Z_v3.json` --
  the absolute-vs-residual A/B; PASS, `residual_no_material_difference`, seeds disagreeing in
  direction against an unmet 3.0 pre-registered floor. Closes the doc's own pre-registered
  branch as a characterised null.
