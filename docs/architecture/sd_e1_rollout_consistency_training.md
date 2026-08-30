---
title: "SD-e1-rollout-consistency-training: e1.transition.action_conditioning + rollout_consistency"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 13
---

# SD-e1-rollout-consistency-training: e1.transition.action_conditioning + rollout_consistency

**Claim ID:** SD-e1-rollout-consistency-training
**Subject:** `predictors.e1_deep.E1DeepPredictor.transition`
**Status:** ITEM 1 IMPLEMENTED (2026-08-29) / ITEM 2 PENDING
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

## Solution -- ITEM 2 (pending)

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
