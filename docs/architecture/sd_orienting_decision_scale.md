---
status: implemented
status_asof: 2026-08-10
status_claim: SD-ORIENTING-DECISION-SCALE
---

# SD-ORIENTING-DECISION-SCALE: pag.defensive_orienting_response.decision_normalization

**Claim ID:** SD-ORIENTING-DECISION-SCALE
**Subject:** pag.defensive_orienting_response.decision_normalization
**Status:** IMPLEMENTED
**Registered:** 2026-08-10 (as a `substrate_queue.json` entry, from `failure_autopsy_V3-EXQ-910_2026-08-10.md`)
**Implemented:** 2026-08-10
**Depends on:** SD-099 (the defensive-orienting gate this fix lives inside; already IMPLEMENTED)
**Blocks:** MECH-489 valence-gating sub-claim re-test (the trigger-alignment sub-claim already
  stands as fairly falsified per `failure_autopsy_V3-EXQ-910_2026-08-10.md` and does not need
  re-testing)

## Problem

`failure_autopsy_V3-EXQ-910_2026-08-10.md` found that SD-099's Component 4/5 block
(`ree_core/agent.py` `select_action()`, the approach/withdraw/resume decision on override) compared
two structurally incommensurable quantities as if they were on the same scale:

- `_do_harm_val` -- the L2 norm of `z_harm_s` (SD-010 sensory-discriminative harm latent). A
  norm is structurally non-negative and, in practice, carries a persistent nonzero ambient level
  even absent any real harm event (residual latent activation).
- `_do_benefit` -- `residue_field.evaluate_benefit(z_world)` (ARC-030 benefit-terrain RBF read).
  Near-zero everywhere except very close to a previously-accumulated benefit center.

Comparing these two raw magnitudes structurally biases every override toward `withdraw`: the
harm norm's ambient floor routinely exceeds the benefit value's near-universal near-zero floor,
independent of the actual valence of whatever triggered the orienting episode. V3-EXQ-910
demonstrated this directly: 206 logged overrides, decision_alignment split 0 approach / 0 resume
/ 206 withdraw -- a 100%-one-sided result fully explained by the scale mismatch alone, with no
dependence on real event valence.

This is a `complicated (buildable)` node (per the work-graph debt vocabulary), not a probe-gated
unknown: the mechanism, the bug, and the fix shape were all fully specified by the autopsy and
`substrate_queue.json`'s `implementation_hint`.

## Solution

### Normalization: z-score each channel against its own running distribution

Rather than comparing raw magnitudes, each channel is normalized against its own ambient
distribution before comparison:

```
z_channel = (value_now - running_mean_channel) / (running_mad_channel + scale_floor)
```

where `running_mean`/`running_mad` (mean absolute deviation, an EMA proxy for scale) are tracked
per channel (harm, benefit), continuously, at the AGENT level -- not inside
`DefensiveOrientingGate`, which deliberately never touches the residue field (SD-099: "the
gate... nothing reaches into the residue field. The action-decision... is resolved by the AGENT").

This is the first of the two options `substrate_queue.json`'s `implementation_hint` named
("z-score each against its own running distribution, or compare signed valence rather than
norm-vs-value"). A pure ratio-to-baseline normalization (the codebase's other established idiom,
`phasic_surprise_burst.py`'s `trigger_ratio * eff_baseline`) was considered and rejected for this
specific comparison: a ratio blows up near a zero baseline (benefit's ambient level is frequently
exactly 0 absent any nearby center) and does not handle "below baseline" symmetrically. Z-scoring
against mean + MAD handles both directions cleanly and gives a dimensionless, directly-comparable
quantity for two channels with genuinely different units and dynamic ranges.

### Baseline update: frozen while orienting is active

The two baselines update every waking tick **while NOT orienting**, and freeze at their
pre-episode value for the duration of an active orienting episode -- exactly mirroring
`DefensiveOrientingGate`'s own onset-baseline freeze (see `defensive_orienting.py`'s docstring):
without freezing, the very elevation that triggered the episode would pull its own baseline
toward itself over the episode's duration, shrinking the z-score right at the moment the override
decision needs it to be sharp. This is load-bearing, not cosmetic -- identical reasoning to the
onset-detector's own freeze, applied to a new consumer.

### Data flow

```
z_harm_s norm (current tick, already computed for the trigger channel)   -\
benefit = residue_field.evaluate_benefit(z_world) (current tick, NEW      +-> update running
  per-tick evaluation -- previously only computed at override time)      -/    mean/MAD (agent,
                                                                                 frozen while
                                                                                 orienting active)
                                                                                     |
                                                                                     v
                                        (on override) z_harm = (harm_val - harm_mean) / (harm_mad + floor)
                                                       z_benefit = (benefit - benefit_mean) / (benefit_mad + floor)
                                                       z_benefit > z_harm + eps -> approach
                                                       z_harm > z_benefit + eps -> withdraw
                                                       else -> resume
```

### Config (REEConfig; all present at all three sites -- dataclass field, `from_dims()` parameter,
`from_dims()` assignment)

| Param | Default | Purpose |
|-------|---------|---------|
| `orienting_decision_baseline_ema_alpha` | `0.02` | EMA rate for the new mean/MAD baselines (matches the existing `orienting_surprise_ema_alpha`/`orienting_harm_s_ema_alpha` timescale) |
| `orienting_decision_scale_floor` | `0.01` | floor added to the MAD denominator before dividing, to avoid blow-up when a channel (typically benefit) has had almost no observed variance yet |
| `orienting_decision_epsilon` | `0.25` (CHANGED from `0.01`) | margin, now in z-score units (was raw-magnitude units) |

**`orienting_decision_epsilon`'s default change is a deliberate part of this fix, not an
oversight of the "never change existing defaults" rule.** The parameter is entirely inert unless
`use_defensive_orienting=True` (default `False`), and the only run that ever exercised it under
the old semantics (V3-EXQ-910) is exactly what this fix corrects -- there is no passing
experiment or test whose behaviour depends on the old value under the old (broken) comparison.
Keeping the numeral `0.01` while changing the units it applies to would be arbitrary, not
backward-compatible; `0.25` (quarter-sigma) is a considered first-pass margin for the new units,
explicitly first-pass and subject to revision by the validation experiment below.

### Backward compatibility

With `use_defensive_orienting=False` (default), none of this code path executes -- `evaluate_benefit`
is not called per-tick, the new baseline state stays at its `__init__` zero-values, and
`orienting_decision_epsilon`'s new default value is never read. Confirmed via a direct `REEAgent`
smoke test: `agent.defensive_orienting is None` and all new `_orienting_decision_*` attributes
stay at their initialized values when the master switch is off.

### Phased training / MECH-094

Not applicable -- pure scalar arithmetic (an EMA mean and an EMA mean-absolute-deviation per
channel), no `nn.Module`, no trainable parameters, no gradient flow. Same category as SD-099
itself. The new per-tick `evaluate_benefit` call and the new baseline-update block sit inside the
SAME `if self.defensive_orienting is not None:` guard SD-099's existing code already uses, so
MECH-094 (simulation-mode) behaviour is unchanged from SD-099's existing treatment of that guard.

## Amend 2026-08-20: post-override decision-window persistence (`decision_counts` defect)

**Status:** IMPLEMENTED 2026-08-20. `ree_core/agent.py::select_action`. This amend discharges the
SECOND `failure_record` on `substrate_queue.json`'s `SD-ORIENTING-DECISION-SCALE` entry
(severity `degrading`). The FIRST -- the norm-vs-benefit scale mismatch documented above -- was
fixed on 2026-08-10 and is untouched.

### The defect

`failure_autopsy_V3-EXQ-910a_2026-08-11` established that `decision_counts` was untrustworthy
(sum 206 against a theoretical max of `n_overrides x orienting_post_override_bias_ticks` = 21 x 5
= 105, and byte-identical to V3-EXQ-910's total despite half the override count) but stated
plainly that it "could not fully pin the exact failure mode" -- no per-step episode logs were
retained for either run. It was pinned statically instead, in
`evidence/planning/mech489_decision_counts_defect_staged_20260817.md` section 2(d):

> Outside `reset()`, the ONLY clear of `_orienting_decision` sat INSIDE the score-bias
> application block, gated on five conditions including `_orienting_decision_ticks_remaining > 0`
> and `_orienting_decision in ("approach", "withdraw")`. A `"resume"` decision sets
> `ticks_remaining = 0` and is excluded by BOTH, so it could never reach the clear and persisted
> for the rest of the episode. Likewise, any tick on which `candidates` was empty or lacked
> `world_states` froze the countdown without clearing, making `orienting_post_override_bias_ticks`
> a LOWER BOUND on persistence rather than a bound.

Both leaks are now confirmed by direct live measurement rather than inference --
`tests/contracts/test_orienting_decision_window_expiry.py` run against the pre-amend `agent.py`
records `resume` surviving every sampled tick, and a `withdraw` countdown pinned at 5 across
seven consecutive block executions with the bias gate closed (i.e. frozen, not merely slow).

**Why this had to be fixed BEFORE the owed retest, not after.** V3-EXQ-910 and 910a both recorded
`resume = 0`, so the `"resume"` leak has never yet fired. It becomes active precisely at the moment
the Component 4/5 scale fix starts working -- so a retest run against the pre-amend substrate would
have corrupted its own counter *only in the branch that indicates success*, biasing the measurement
toward the null in a way no reader could detect from the manifest.

### The fix

The countdown/expiry moves out of the score-bias application block into its own **unconditional**
step, gated only on `_orienting_decision is not None`, placed BEFORE the Component 4/5 override
block so it acts on the *previous* tick's decision. The score-bias APPLICATION stays conditional
on exactly the same five conditions as before.

```
(per E3 tick, inside `if self.defensive_orienting is not None:`)

  gate.tick() -> DefensiveOrientingOutput
  trigger_fired  -> capture _orienting_trigger_z_world           (unchanged)
  EXPIRY STEP    -> if _orienting_decision is not None:          (NEW, unconditional)
                        ticks_remaining -= 1
                        if ticks_remaining <= 0: decision = None; ticks_remaining = 0
  override_fired -> set decision + ticks_remaining               (unchanged)
  bias gate open -> apply per-candidate score_bias               (unchanged, still conditional)
```

**Happy-path behaviour is unchanged.** With the bias gate open on every tick, decrementing at the
top of each subsequent tick applies the bias on exactly `orienting_post_override_bias_ticks` block
executions (the override tick plus N-1 following) -- identical to the old
decrement-after-applying placement. What changes is only that the window now also expires on
ticks where the bias gate does NOT open, and that a `"resume"` decision expires after one block
execution instead of never.

`"resume"` is deliberately expired on the NEXT block execution rather than on the tick it is set:
clearing it eagerly (e.g. by placing the expiry after the bias block) would make `"resume"`
invisible to any per-step readout -- reproducing the degenerate `resume = 0` reading the retest
exists to escape.

### Persistence-window denomination

**`orienting_post_override_bias_ticks` is denominated in E3 TICKS, not env steps.** This is now
stated rather than left implicit, because the name and this document's earlier prose both invite
the env-step reading.

The whole SD-099 block sits downstream of `select_action()`'s non-E3-tick early return, so at the
default `heartbeat.e3_steps_per_tick = 10` a nominal 5-tick window spans **~50 env steps**. That
is existing behaviour, retained deliberately and not changed by this amend:
`DefensiveOrientingGate.tick()` is only ever called from this one block, so every other SD-099
tick quantity (`orienting_max_duration`, `orienting_confidence_rise_rate`, `ticks_in_orienting`)
already counts these same E3 ticks. Re-denominating this one parameter in env steps would make it
the sole env-step quantity in the mechanism.

**This is a design choice, not a bug fix, and it changes behaviour if reversed** -- so it was
surfaced to the user as a decision chip
(`chip-20260820-orienting-bias-ticks-denomination`) rather than decided silently. If the env-step
reading is preferred, the change is to divide the window by `clock.e3_steps_per_tick` at the point
it is set, and to restate this section; nothing else in the amend depends on which way it goes.

One residual, recorded rather than papered over: if `use_e3_reselection_shortcircuit` is enabled
(default `False`), the ARC-071 chunk short-circuit returns from `select_action()` before this
block on some E3 ticks, so those ticks consume no window. That is arguably correct -- E3 does not
deliberate on such a tick, so there is no candidate set to bias -- but it means the window is
denominated in *executed* E3 deliberations, not in wall-clock E3 ticks, whenever that flag is on.

### Driver half (NOT in this amend)

The staged doc's section 3 splits the defect across substrate and driver. Only the substrate half
is implemented here. The driver half -- counting the decision at the override tick only, in the
same synchronous block that increments `n_overrides`, and emitting `n_latched_ticks` alongside the
row count per `/queue-experiment` Step 3.5 -- belongs to the owed MECH-489 valence-gating retest
and must go through `/queue-experiment`, not a hand-edit. `EVB-0610` / `EXP-0033` therefore stays
`blocked_substrate` until that half lands too; its `release_condition` names both halves.

### Tests

`ree-v3/tests/contracts/test_orienting_decision_window_expiry.py` (5, time-independent, real
`REEAgent` over a real `CausalGridWorldV2` rollout -- only the gate's verdict is scripted).
Verified differentially: 3 of the 5 FAIL against the pre-amend `agent.py`. The 2 that pass in both
are the invariance controls (SD-099 master switch OFF stays bit-identical inert; `reset()` remains
the episode-boundary clear), which are what stop a later session widening this expiry into a
behaviour change.

## What This SD Enables

Unblocks re-testing MECH-489's valence-gating sub-claim (Components 4/5), which
`failure_autopsy_V3-EXQ-910_2026-08-10.md` found NOT fairly tested (confounded by this bug, not
falsified). The trigger-alignment sub-claim (Components 1-3) already stands as fairly falsified
per its own pre-registered signature and does not need re-testing. `claims.yaml` MECH-489's
`pending_retest_after_substrate: true` flag is scoped to the valence-gating sub-component only.

## Related Claims

**MECH-489** (the mechanism whose Component 4/5 this fixes). **SD-099** (the parent gate;
UNCHANGED by this fix -- `defensive_orienting.py` was not modified, only `agent.py`'s consumption
of its output). See `failure_autopsy_V3-EXQ-910_2026-08-10.md` for the original finding and
routing recommendation ("implement-substrate -- SD-ORIENTING-DECISION-SCALE... recommend a 910a
re-queue after the fix lands, scoped to re-test valence-gating only").
