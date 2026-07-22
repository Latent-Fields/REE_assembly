---
status: candidate
status_asof: 2026-07-20
status_claim: SD-076
---

# SD-076: precision.waking_confidence_inflation

**Claim ID:** SD-076
**Subject:** precision.waking_confidence_inflation
**Registered:** 2026-07-20
**Implemented:** 2026-07-20
**Depends on:** ARC-016 (dynamic precision / running_variance)
**Blocks:** MECH-173 (REM-suppression overconfidence), MECH-204 Phase 7 validation

## Problem

`E3TrajectorySelector.update_running_variance()` maintains `_running_variance`
(rv) as a symmetric EMA of the observed squared prediction error. rv is
therefore a *faithful* tracker of true prediction error: rv ~= true error **by
construction**.

This makes an entire class of claim unmeasurable. MECH-173 predicts that
REM/recalibration suppression raises overconfidence, measured as

    overconfidence_index = (true_error_ref - mean_running_variance) / true_error_ref

If rv tracks true error faithfully, this index is pinned near zero regardless
of what is ablated. V3-EXQ-774 measured exactly that: `ARM_REM_SUPPRESSED`
scored `-0.000148` and `ARM_RECALIB_OFF` scored `-0.000918` -- both
indistinguishable from zero, and the load-bearing criterion
`suppressed_arm_absolutely_overconfident` recorded `false`.

The confirmed `failure_autopsy_V3-EXQ-774_2026-07-17` adjudicated this
`substrate_ceiling` and named the missing piece directly: the substrate
"cannot express absolute overconfidence -- the F1 setpoint is a lagging
low-pass of the agent's own running_variance with no waking confidence-
inflation source to correct."

The deeper point: **MECH-204's entire corrective function presupposes a
daytime drift source it did not have.** "Sleep recalibrates waking precision
drift" is only a testable claim if waking precision can drift. Without a
drift source, a null result on any MECH-204 consumer is a tautology, not
evidence.

## Solution

Asymmetric EMA in `update_running_variance`. When
`E3Config.use_waking_confidence_inflation` is True:

```python
if error_var < self._running_variance:            # improving
    alpha = min(1.0, self._ema_alpha * (1.0 + asym))    # believe it FAST
else:                                             # worsening
    alpha = max(0.0, self._ema_alpha * (1.0 - asym))    # believe it SLOWLY
rv_new = (1 - alpha) * self._running_variance + alpha * error_var
self._running_variance = max(floor, rv_new)
```

Good news is incorporated quickly, bad news slowly, so rv settles *below* the
true error mean. That is a systematic, directional, and correctable
under-estimate of one's own error -- the operational definition of
overconfidence.

### Config

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_waking_confidence_inflation` | bool | `False` | master switch |
| `waking_confidence_inflation_asymmetry` | float | `0.0` | asymmetry in [0, 1); 0.0 = symmetric |
| `waking_confidence_rv_floor` | float | `0.01` | floor on inflated rv |

**Bit-identical OFF by construction, not by arithmetic.** The OFF branch
evaluates the original symmetric expression unchanged rather than re-deriving
it at `asymmetry = 0`. Verified by explicit float equality over an 80-step
trace (UC1), not by approximate comparison.

**The floor is load-bearing, not hygiene.** rv feeds an *absolute* commit
threshold (`running_variance < commit_threshold`, ARC-016) and
`current_precision = 1 / (rv + 1e-6)`. Unbounded downward drift would both pin
the agent permanently "committed" and explode precision. The floor applies
only on the inflation path.

### Headroom repair (2026-07-22)

**The floor is load-bearing, but an ABSOLUTE floor is the wrong kind of
quantity, and 0.01 is the wrong value for this substrate.** V3-EXQ-794 measured
the un-inflated operating point at `rv = 0.005420` (`ARM_OFF_OFF`) and
`arm_true_error_ref` at ~0.0037, so the floor sat **1.8x above the operating
point and 2.7x above true error**. `max(0.01, rv)` therefore clamped on the
first tick inflation bit and never released: `rv_final` finished at **exactly
0.010000** on all four inflation arms, and `overconfidence_score` was
**bit-identical to 15 significant figures** (`-1.004111904519277`) at asymmetry
0.6 *and* 0.8.

Two doses producing one value is a **saturation signature, not a null**. Neither
SD-076 nor MECH-204 was tested: SD-076's lever hit the clamp, and MECH-204's
Phase-7 correction had no drift to correct
(`d_broadcast_under_drift_at_operative.per_seed` is empty). The recorded
`does_not_support` for SD-076 was withdrawn and revised to `non_contributory` by
`failure_autopsy_V3-EXQ-794_2026-07-22`.

**Why the validation smoke above passed 6/6 anyway** — the property worth
carrying forward. It used a synthetic error sequence with true mean **0.05**,
~13x the substrate's real error scale, where 0.01 *is* a floor with headroom. An
absolute constant validated at one scale silently became a clamp at another.
That is why the repair is a **relative** bound rather than a smaller absolute
one, and why the new contracts run at the *measured* 794 scale.

**The sign is not the bug.** The autopsy listed a wrong-sign inflation as
candidate cause (b). It is ruled out: inflation drove rv *down* correctly, into
a floor that happens to sit *above* the OFF arm, so the run's
`inflation_lowers_rv` precondition saw rv rise.

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `waking_confidence_rv_floor_relative_frac` | float | `0.0` | `0.0` keeps the absolute floor. `>0` makes the bound that fraction of `_wci_symmetric_rv_ref` |
| `waking_confidence_rv_floor_mode` | str | `"hard"` | `"hard"` = the original clip; `"soft"` = softplus approach |
| `waking_confidence_rv_floor_softness` | float | `0.25` | knee width as a fraction of the effective floor; inert while `"hard"` |

`_wci_symmetric_rv_ref` is a symmetric EMA of the same squared error at the same
alpha, advanced only on the inflation path — i.e. **the counterfactual
un-inflated rv**, "what rv would have been without inflation". The bound then
reads: *inflation may not push rv below `frac` x the un-inflated counterfactual*.
This guarantees headroom at any substrate error scale — the property the absolute
floor lacked — and caps `overconfidence_score` at `1 - frac`, a bound relative to
reality, which is also the biologically correct shape: confidence inflation is
bounded by the organism's own error experience, not by a constant.

**Why soft, beyond the biology.** The softplus is **strictly monotonic**
(`d/d rv_new = sigmoid(.) > 0` everywhere), so two distinct doses can never map
to one value. A residual saturation can then only *shrink* a dose separation,
never collapse it to an exact tie — a mis-set floor degrades to a small LO/HI gap
the `dose_saturation` lint can see, instead of the bit-identical arms that made
794 unadjudicable without an autopsy.

Smoke at the measured 794 scale (true error 0.0037), 14/14 PASS: the **old**
config reproduces the defect exactly (`LO == HI == 0.01`); the repaired config
gives `rv_final` 0.0025377 (LO) vs 0.0021031 (HI) — dose-ordered, separated, and
both genuinely overconfident (+0.314 / +0.432). Contracts:
`ree-v3/tests/contracts/test_sd076_rv_floor_headroom.py` (17), which pin the
**defect** as well as the repair, so a future "simplification" back to an
absolute hard floor fails there rather than in a run.

Behavioural validation: **V3-EXQ-794a**, a same-question re-run of the identical
2x2 (the design was sound; only the drift source needed repair).

## Architecture Context

SD-076 is the *source* of precision drift; MECH-204 (F1 per-cycle WRITEBACK
recalibration) and MECH-204 Phase 7 / Option B (per-step broadcast anchor) are
the *corrections*. They are complementary halves of one loop and were built in
the same pass (2026-07-20) for that reason -- but they are separate claims and
must be independently ablatable, which is why this carries its own SD id rather
than riding on the MECH-204 entry.

Sign convention: SD-076 pushes rv **down** (overconfidence); MECH-204
recalibration pulls rv **toward the cumulative zero-point reference**. On a
well-calibrated agent these approximately cancel; the experimental signal is in
the arms where one is ablated.

## Biological Grounding

Optimism / positive-outcome bias in waking belief updating: humans
preferentially incorporate better-than-expected information about their own
performance and under-weight worse-than-expected information. This asymmetry is
the standard account of why self-assessment drifts optimistic over a waking
period, and it is the drift that the sleep-recalibration literature underlying
MECH-204 (Hobson-Hong-Friston 2014; Walker & Stickgold 2006) presupposes.

Note this is a *functional* translation, not a mechanism claim about a specific
neuromodulator. The asymmetric-alpha implementation is the simplest form that
produces the required directional drift; a richer account (e.g. valence-gated
learning rates) is V4 scope.

## What This SD Enables

- **MECH-173** becomes measurable at all: `suppressed_arm_absolutely_overconfident`
  can now be true or false on the evidence rather than false by construction.
- **MECH-204 Phase 7 / Option B** gets a non-tautological validation target.
- Any future claim about *miscalibration* (as opposed to inaccuracy) in the V3
  substrate.

## Validation

Smoke (2026-07-20, 6/6 PASS): with `asymmetry=0.6` on an alternating error
sequence with true mean 0.05, `overconfidence_index` moves from **-0.164**
(OFF, underconfident) to **+0.273** (ON, genuinely overconfident). The OFF
value reproduces the sign and rough magnitude of V3-EXQ-774's measured
`ARM_FULL_SLEEP = -0.2097`, which is direct evidence that the diagnosis in the
autopsy was correct.

Behavioural validation: queued as the MECH-204 Phase 7 retest (see
`evidence/planning/sleep_substrate_plan.md` Phase 7 status row).

## Related Claims

MECH-173, MECH-204, ARC-016, Q-042, SD-069 (`last_instantaneous_pe` reads the
same pre-smoothing error signal and is unaffected by this change).
