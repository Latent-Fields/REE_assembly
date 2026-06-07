# ControlVector Logging (four-signal control adjudication, recommendation B)

**Subject:** telemetry.control_vector_logging
**Status:** IMPLEMENTED
**Registered:** 2026-06-07
**Depends on:** MECH-320 (tonic vigor), MECH-313 (noise floor), SD-032b dACC (EVC effort term), E3 selector
**Blocks (informs):** ARC-068 first-class opportunity-cost separation (post-green-board)

## Problem

A four-signal control adjudication (2026-06-07) asked whether REE-v3 realises four
separable control signals:

1. **Value** (V_outcome) -- is this outcome worth obtaining/avoiding?
2. **Effort cost** (C_effort) -- how much work/control must be paid?
3. **Opportunity cost of time** (C_time) -- what is lost by not acting / by no-op delay?
4. **Vigor / activation** (G_vigor) -- how forcefully/quickly to act?

Code adjudication found that **opportunity-cost-of-time is not an independent control
signal**. It is collapsed into MECH-320's single average-reward-rate scalar `v_t`:
`tonic_vigor.compute_score_bias` applies `-w_action*v_t` to action candidates (vigor) and
`+w_passive*v_t` to no-op candidates (opportunity cost). Both halves are `w * v_t` for the
**same** `v_t` (see `ree_core/policy/tonic_vigor.py` docstring: *"mathematically equivalent
to a single signed scalar applied to the action-vs-no-op contrast"*). ARC-068
(`opportunity_cost_no_op_penalty`) is a registered claim with **no implementation** -- its
lit-pull is still pending. So the two signals cannot dissociate in direction.

The remaining signals: V_outcome is the primary E3 score axis (fully realised); C_effort is
present as the Shenhav EVC form in the dACC bundle (`mode_ev = payoff - control_required *
candidate_effort`) but with a thin horizon-length effort proxy; G_vigor is the action half of
MECH-320 plus the MECH-313 noise-floor temperature lift.

## Solution (recommendation B: logging only, no causal change)

A read-only, default-OFF telemetry struct that makes the four signals separately inspectable
and **exposes the C_time<->G_vigor collapse** by logging both halves alongside their shared
`v_t`. Pure telemetry -- no change to scoring or selection.

- **Config:** `REEConfig.use_control_vector_logging` (default `False`; also a `from_dims`
  kwarg). Bit-identical when off (the assembly block is skipped).
- **dACC bundle** (`ree_core/cingulate/dacc.py`): two additive keys -- `control_required`
  (float) and `effort_term` (`control_required * candidate_effort`, `[K]`) -- so C_effort is
  readable without re-deriving it from `payoff - mode_ev`. No existing consumer reads them.
- **E3 selector** (`ree_core/predictors/e3_selector.py`): `self.last_raw_scores` -- the
  pre-bias per-candidate scores (the value axis). Stored alongside `last_scores`.
- **Agent** (`ree_core/agent.py`): the MECH-320 `tv_bias` action/no-op split + `v_t` /
  `w_action` / `w_passive` are cached in the tonic-vigor block; after `e3.select` returns,
  `REEAgent._assemble_control_vector()` writes `self._last_control_vector`. Read directly by
  experiment scripts (the V3-EXQ-571 `_last_score_bias_decomp` pattern).

### `_last_control_vector` schema

```
{
  "step": int,
  "V_outcome": {mean, range, std, value_mean(=-mean), present},     # E3 pre-bias scores
  "C_effort":  {mean, range, std, control_required, present},        # dACC EVC effort term
  "C_time":    {potential(=w_passive*v_t), realised_mean, n_noop_candidates, present},
  "G_vigor":   {potential(=w_action*v_t), realised_mean,
                noise_floor_temp_lift, n_action_candidates, present},
  "shared":    {tonic_vigor_v_t, tonic_vigor_v_raw, w_action, w_passive, collapse_note},
  "authority": {modulatory_authority_active, modulatory_authority_scale_factor,
                e3_raw_score_range_mean},
}
```

`shared.tonic_vigor_v_t` is logged explicitly so that `C_time.potential` and
`G_vigor.potential` are both computable as `w * v_t` for one scalar -- the collapse made
inspectable. `authority` records whether the modulatory bias actually had selection authority
this tick (modulatory-bias-selection-authority substrate), because MECH-320's bias has
near-zero authority until V3-EXQ-643a validates.

## Validation

- Smoke + 4 contract tests (`tests/contracts/test_control_vector_logging.py`): C1 default-OFF
  no population; C2 ON populates the four signals; C3 collapse relationship
  (`C_time/G_vigor == w*v_t`, same `v_t`); C4 bit-identical OFF-vs-ON action stream.
- Stage-B diagnostic experiment: re-run a MECH-320-ON config with logging enabled and measure
  the rank-correlation between logged `C_time` and `G_vigor` across ticks. Pre-registered
  prediction: rho ~ 1.0 (they are `w*v_t` for one `v_t`). This converts the collapse from a
  code-reading inference into a measured fact -- the evidence governance needs before deciding
  whether ARC-068 should get its own scalar.

## Deferred (post-green-board roadmap)

- **C** -- a first-class opportunity-cost signal causally modulating commit pressure. Blocked
  on (a) the pending ARC-068 lit-pull and (b) MECH-320 regaining selection authority
  (V3-EXQ-643a / SD-056 / ARC-065 GAP-A). The MVT patch-leaving paradigm is the validating
  falsifier.
- **D** -- a full four-axis causal ControlVector. Larger; deferred further.

## Related

MECH-320 (tonic vigor / the collapse site), ARC-066 (parent family), ARC-068 (the unbuilt
opportunity-cost claim), MECH-313 (noise floor / G_vigor temperature lift), SD-032b dACC
(C_effort source), modulatory-bias-selection-authority (authority context), V3-EXQ-571
(`_last_score_bias_decomp` pattern this extends), V3-EXQ-624a (the documented MECH-320 v_t
sign/scale issue this telemetry surfaces).
