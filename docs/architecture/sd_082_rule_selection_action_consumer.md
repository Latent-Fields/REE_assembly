---
status: candidate_substrate_landed
status_asof: 2026-08-30
status_claim: SD-082
---

# SD-082: pfc.lateral_pfc.rule_selection_action_consumer

**Claim ID:** SD-082
**Subject:** pfc.lateral_pfc.common_mode_invariant_trained_rule_to_action_readout
**Registered:** 2026-07-26
**Implemented:** 2026-07-26
**Depends on:** SD-008, SD-066, SD-077, SD-033a (ARC-062 GAP-D trainable bias head), ARC-063, SD-078
**Blocks:** V3-EXQ-822a (SD-078 rule-selection consumer re-run); the SD-078 downstream-consumer promotion gate (candidate_substrate_landed -> provisional).

## Problem

SD-078 landed and validated (V3-EXQ-806 PASS) a common-mode-invariant context key
for the ARC-063 CandidateRuleField: with centering, the rule POOL de-collapses and
a differentiated `rule_state` is produced (V3-EXQ-822: `on_rule_state_diff_mean`
0.644 vs 0.0, `c1_pass`, `max_live` 16 vs 1). But V3-EXQ-822 (the consumer test that
gates SD-078 promotion) found that the differentiated `rule_state` was **behaviourally
silent**: propagation to the per-candidate action bias was a **structural zero on both
arms** -- `on_prop_delta_mean = off_prop_delta_mean = exactly 0.0` -- and readiness gate
(d) `propagation_non_vacuity` failed. Even a full-scale 70-episode P1 REINFORCE did not
un-zero the SD-033a bias head. Autopsy: `failure_autopsy_816c-822_2026-07-26`
(REE_assembly origin/master afb2df901e), routed to `/implement-substrate`.

### Root cause (reproduced 2026-07-26)

The SD-033a lateral-PFC bias head (`LateralPFCAnalog.compute_bias`) reads the **raw**
per-candidate `z_world` summaries and bounds its output with a **hard clamp**
`bias_raw.clamp(-bias_scale, +bias_scale)` (`bias_scale = 0.1`). Under SD-008 z_world
under-differentiation, those candidate summaries sit in a ~0.98-cosine **common-mode
cone** (V3-EXQ-822 measured `zworld_cone_min_cosine` 0.963): they are nearly collinear
and dominated by a single large shared vector. The head output is then dominated by that
common mode, so **every** candidate's raw output exceeds `bias_scale` in the **same
direction** and the hard clamp maps them all to the **identical rail**. Two consequences:

1. **Propagation is erased.** Zeroing `rule_state` (the propagation counterfactual)
   leaves every candidate on the same clamp rail, so `compute_bias(rule_state) ==
   compute_bias(0)` exactly -> `prop_delta = 0.0` for every candidate on every tick.
   This is the SD-008 common-mode pathology SD-078 repairs upstream, re-appearing in the
   **downstream read-out**.
2. **The head cannot train.** A saturated hard clamp has a **flat region with zero
   gradient**, so `d bias / d head_params = 0` and the P1 REINFORCE gradient dies at the
   clamp -- no amount of REINFORCE budget moves the head (the observed 70-episode null).

Verified in isolation: in the common-mode cone regime, the hard clamp gives
`prop_delta = 0.0` and head gradient-norm `0.0`; the SD-082 fix gives `prop_delta`
~0.005 (5x the 1e-3 floor) and gradient-norm ~6.1. The measured zero is `0.0`-not-`None`
(a real measured zero, not the instrument's None-on-failure fallback) while the same
instrument returns `0.644` for `rule_state` differentiation -- a genuine substrate gap.

## Solution

A trained, common-mode-invariant read-out consumer for the SD-033a bias head, behind a
single no-op-default master flag. `ree_core/pfc/lateral_pfc_analog.py`
(`LateralPFCConfig.rule_readout_consumer`, `readout_init_scale`). When
`rule_readout_consumer=True`, `compute_bias` does two things (both dormant by default):

**(i) Center the candidate-summary input.** Subtract the mean summary across the
candidate set (the common mode) before the head, when there are >= 2 candidates. This
mirrors SD-078's upstream centering of the CandidateRuleField context key: the head then
sees the **differentiated residual**, so the SD-008 cone no longer saturates every
candidate to the same rail. This is what makes propagation non-vacuous (robust, ~0.019 in
probe; ~0.005 through the real trained head).

**(ii) Smooth scaled-tanh bound.** Replace the hard clamp with
`bias = bias_scale * tanh(bias_raw / bias_scale)`. Same magnitude bound as the clamp
(`|bias| < bias_scale`, so the bias still cannot dominate the E3 objective -- the SD-033a
signature-(iii) guarantee is preserved), but **smooth and monotone everywhere**, so the
rule_state's marginal contribution is never erased by a flat region and the head stays
**gradient-trainable** under REINFORCE.

**Init scaling (secondary).** When `rule_readout_consumer` and `train_rule_bias_head` are
both True, the head's LAST Linear weight+bias are multiplied by `readout_init_scale`
(default 0.25) at init so the initial raw output sits in tanh's responsive band
(`|raw| < bias_scale`) rather than deep in saturation -- larger initial gradient and a
non-vacuous first-tick propagation. `readout_init_scale = 1.0` disables the rescale.

### Config plumbing

- `LateralPFCConfig.rule_readout_consumer: bool = False`, `readout_init_scale: float = 0.25`
  (`ree_core/pfc/lateral_pfc_analog.py`).
- `REEConfig.lateral_pfc_rule_readout_consumer: bool = False`,
  `lateral_pfc_readout_init_scale: float = 0.25` -- plumbed through all three `from_dims`
  sites (dataclass field, signature, assignment) and read in `agent.py`'s
  `LateralPFCConfig` build (`getattr`-fallback, so an absent flat REEConfig attr is
  bit-identical).

### Data flow

```
CandidateRuleField (SD-078 centered context key)
    -> differentiated rule_state  [ARC-063 GAP-B: crf_source REPLACES the EMA source]
    -> LateralPFCAnalog.rule_state  [1, rule_dim]
compute_bias(candidate_world_summaries):            <-- SD-082 read-out consumer
    summaries := candidate_world_summaries
    if rule_readout_consumer and K>=2:              # (i) common-mode subtraction
        summaries := summaries - summaries.mean(0)
    bias_raw := rule_bias_head(cat([rule_state, summaries]))
    if rule_readout_consumer:                        # (ii) gradient-preserving bound
        bias := bias_scale * tanh(bias_raw / bias_scale)
    else:
        bias := clamp(bias_raw, -bias_scale, bias_scale)   # landing path (bit-identical)
    -> E3 per-candidate score_bias (composed additively with dACC / OFC bias)
```

## Architecture Context

This completes the SD-033a signature-(iv) "training-dependent emergence" of the bias head
-- the trained-head variant that the SD-033a landing (`sd_033*`) explicitly **deferred**
(DESIGN ALTERNATIVE A2: "A trained-head variant is a deliberate V3 choice deferred to a
later ablation") -- specifically for the SD-078 rule-selection consumer path. The
centering lever (i) is the same common-mode-subtraction principle SD-078 established for
the CandidateRuleField context key, applied one stage downstream at the read-out.
Biological grounding: corticostriatal rule-to-action mapping -- a selected rule/context
representation must gate a motor bias for the selection to have behavioural consequence;
selection without a trained read-out to action is inert (autopsy biological_reference).

## What This SD Enables

- **V3-EXQ-822a** (this SD's validation): the SD-078 consumer test can finally exercise
  the rule_state -> action-bias path. With `lateral_pfc_rule_readout_consumer=True` on
  both arms, propagation is non-vacuous, so readiness gate (d) can pass and the ON/OFF
  (crf_cue_centering) contrast on the executive-bias DV becomes measurable.
- The SD-078 promotion gate (candidate_substrate_landed -> provisional), which is held
  pending a downstream-consumer test.

## ML/AI engineering notes (Layer 7)

- **Failure mode addressed:** saturated hard-clip has a dead-gradient flat region -- a
  well-known trainability failure. The standard fix for a bounded-but-trainable output is
  a smooth squashing nonlinearity (scaled tanh), as used for bounded action outputs in
  squashed-Gaussian policies (DDPG/SAC). REE adaptation: the tanh is scaled so the bound
  magnitude equals `bias_scale` exactly, preserving the SD-033a "bias cannot dominate E3"
  guarantee. Biological compatibility: a smooth saturating gain is a more faithful model
  of a neural bias projection than a hard rail.
- **Numerical:** `readout_init_scale` keeps the initial raw output in tanh's responsive
  band so the first gradient is not vanishingly small; without it, full-magnitude random
  init lands deep in saturation (small gradient) even with tanh.
- **NOT imported:** no change to the SD-033a architecture, ontology, or the rule_state
  update path; this is a read-out + input-conditioning fix only.

## Phased training

**Required.** The bias head trains in P1 (encoder + CandidateRuleField frozen; REINFORCE
on the head only), P2 is the frozen eval/measurement window. This matches the existing
V3-EXQ-822 P0/P1/P2 protocol and the 598b/654f bias-head REINFORCE pattern.

## MECH-094

Not applicable. The read-out is a pure forward read of `rule_state` -> action bias; it
writes no content to memory during any non-waking state. `rule_state` itself is
gate-protected via MECH-261 (`write_gate("sd_033a")`), and the head trains only in waking
P1. No `hypothesis_tag` semantics apply to this read-out.

## Related Claims

SD-033a (lateral-PFC-analog, the bias head this completes), SD-078 (centered
CandidateRuleField context key, the upstream fix this consumes), ARC-063 (CandidateRuleField,
GAP-B/GAP-D), SD-008 (z_world under-differentiation, the common-mode source), SD-066 / SD-077
(EMA-baseline centering precedents).

## Failure record (defines validation acceptance)

- `v3_exq_822_sd078_rule_selection_consumer_20260726T112152Z_v3` (FAIL, precondition):
  `on_prop_delta_mean = off_prop_delta_mean = 0.0` (structural zero, both arms) while
  `on_rule_state_diff_mean = 0.644`. **Acceptance for V3-EXQ-822a:**
  `on_prop_delta_mean >= 0.001` (readiness_prop_nonvac) with an ON>OFF propagation contrast.

## Amendment (2026-08-29 / landed 2026-08-30): the "structural zero" was never measured; the real defect

`failure_autopsy_V3-EXQ-822c_2026-08-29.md` (confirmed) overturned the 822b attribution.
`n_prop_samples` was `0` in **all 18 cells** across V3-EXQ-822/822a/822b: the drivers'
`_candidate_summaries()` called only `agent._candidate_world_summaries(candidates)`, which
returns `None` on the default `candidate_summary_source="proposer"` -- so the reported
"structural zero" was the empty-list default of `statistics.fmean(prop_deltas) if
prop_deltas else 0.0`, never a real measurement, in every prior run of this lineage.

With the measurement gap fixed (822c), the REAL defect is one level upstream of
`compute_bias` and is structural: the per-candidate summary every "proposer"-default caller
builds is `trajectory.world_states[:, 0, :]`, but `E2FastPredictor.rollout_with_world` seeds
`world_states = [initial_z_world]` -- index 0 is the rollout's **shared initial world
state**, bit-identical across all K candidates by construction. SD-082's own centering step
then annihilates this constant to float32 cancellation noise
(`rule_summary_magnitude_ratio` 2.8e6-4.5e6, ~4000x the 1e3 in-range ceiling, in every
822c cell, both arms). Severity **corrupting**: on the default config, `prop_delta` clears
the 1e-3 non-vacuity floor (0.001662) while carrying zero candidate-discriminating
information -- an authentic-looking but meaningless number.

**Fix landed (this amendment).** Two independent, both no-op-default, changes:

1. **`ree_core/utils/config.py` / `ree_core/agent.py`**: `candidate_summary_source` gains a
   third value, `"proposer_post_action"` (default stays `"proposer"`, bit-identical). Still
   proposer-rollout-based (not `"e2_world_forward"`, which is a different fix for a different
   problem -- see the field's own docstring), but
   `agent._proposer_post_action_summaries()` reads `world_states[:, 1:, :].mean(0)` (the
   POST-ACTION states, reflecting each candidate's own action sequence) instead of
   `world_states[:, 0, :]`, at zero extra model calls. Falls back to the t=0 state only for a
   degenerate zero-horizon rollout. Because `_candidate_world_summaries()` is the single
   shared source for every E3-side bias channel (lateral_pfc / ofc / mech295 / gated_policy /
   tonic_vigor), this fixes the same structural defect for all of them uniformly when opted
   in, exactly as `"e2_world_forward"` already does -- not just for lateral_pfc.
2. **`ree_core/pfc/lateral_pfc_analog.py::compute_bias`**: a centering-degeneracy guard
   (`LateralPFCConfig.candidate_summary_degeneracy_floor`, default `1e-4`). Whenever
   `rule_readout_consumer` centers a >=2-candidate summary, it now always records
   `candidate_summary_norm_pre_centering` / `_post_centering` and flags (never raises)
   `candidate_summary_degenerate` when the post-centering norm collapses to float-noise
   scale relative to the pre-centering norm -- purely diagnostic, never changes the returned
   bias value. This makes the exact 822c failure mode directly measurable going forward
   instead of only inferable from `rule_summary_magnitude_ratio` post hoc.

Contract: `ree-v3/tests/contracts/test_sd082_candidate_summary_post_action_amend.py` (22
tests -- authored during the verify-and-land pass that landed this branch, since the
substrate build died mid-verification before committing them; run alongside the existing
14-test `test_sd082_rule_readout_consumer.py`, both green on the full contract suite).
Validation experiment: V3-EXQ-822d **planned but not yet queued** (a `/queue-experiment`
follow-on session is needed -- see `substrate_queue.json`'s SD-082 entry), which would set
`candidate_summary_source="proposer_post_action"` (never rely on the None-returning
default) and assert `n_prop_samples > 0` as a readiness gate -- the exact measurement
starvation that let three prior runs silently measure nothing for a month.

Per the autopsy: SD-082's centering mechanism is **not falsified by this history -- it was
untested**, because its input never carried the cross-candidate variance it was designed to
preserve.
