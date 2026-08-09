---
status: candidate
status_asof: 2026-08-09
status_claim: SD-099
---

# SD-099: pag.defensive_orienting_response

**Claim ID:** SD-099
**Subject:** pag.defensive_orienting_response
**Registered:** 2026-08-09
**Depends on:** MECH-279 (PAG freeze-gate, distinct sibling mechanism), MECH-205 (VALENCE_SURPRISE
  write path), SD-010/SD-011 (harm-stream separation, the two trigger channels), SD-014/ARC-036
  (valence vector + benefit terrain, the resolution-read channels), ARC-030/MECH-117 (benefit
  terrain), MECH-395/MECH-482/MECH-483 (adjacent orienting-territory claims -- distinguished, not a
  dependency; see Related Claims)
**Blocks:** MECH-489 (the candidate mechanism this SD implements); corroborates/targets the
  Section-4 affect->behaviour temporal-decoupling finding and the 12e directional-organisation gap
  (`observational_review_V3-EXQ-906b_2026-08-09.md`)

## Problem

`observational_review_V3-EXQ-906b_2026-08-09.md` Section 11b established that REE has **no
orienting / startle / reorienting mechanism at all** -- a tree-wide grep for
`orient|reorient|startle|fright` across `ree_core/` returned nothing but one incidental string.
The existing `pag/freeze_gate.py` (MECH-279) freezes on *accumulated harm/suffering*
(`z_harm_a * duration_above_threshold > theta_freeze`) -- it responds to harm being **experienced**,
not to **noticing** something sudden and unidentified. There is no pathway from "something
unexpected just happened" to "arrest, investigate, then act on what I found."

This gap is the substrate-level counterpart of the review's central novel finding (Section 4 /
12a): affect channels vary but are **temporally decoupled** from behaviour (`is_committed`=0/3909
across the whole 906b run; surprise-spike -> behaviour-change couplings are diffuse, not sharp).
12e additionally showed that movement during classifier-labelled `approach`/`avoid` modes is
essentially uncorrelated with the nearest resource/hazard position (mean cosine 0.019 / -0.053) --
there is no mechanism that latches onto and steers toward a **specific identified stimulus**.
Building the fright -> freeze -> reorient -> override -> approach/withdraw/resume chain is exactly
the missing coupling mechanism.

**Two pre-build findings shape this design and must be read before the trigger/registration
decisions below** (both from the same review, Section 12):

- **12h (trigger calibration risk):** the naive design implied by 11b/12b -- fire on
  `residue_surprise > p90(0.040)` of the overall step distribution -- **under-fires on the
  ground-truth injected events it exists to catch**. Event-triggered `residue_surprise` at
  `limb_damage_injected` (n=28) is 0.0054, *below* the 0.0139 global baseline; at
  `external_hazard_injected` (n=31) it is 0.0239, above baseline but still below the proposed 0.040
  cutoff; at `world_rule_shift_occurred` (n=15) it is 0.0072, below baseline with only a delayed
  dread/excite rise by t+3. A single-channel absolute-threshold design on `residue_surprise` alone
  cannot catch `limb_damage_injected` at any threshold, because its population mean response is
  *below* ambient.
- **12j (adjacent-claim reconciliation):** `claims.yaml` already carries MECH-482
  (`epistemic_deficit`, a persistent target-bound accumulator, explicitly defined **against**
  "transient prediction error") and MECH-483 (`orient/survey`, a diffuse regime driven by
  MECH-482), both `candidate`/`v3_pending`/"DO NOT build in V3" pending GAP-A (a target-bound
  uncertainty substrate not yet built). This SD's trigger is the opposite end of the timescale --
  a **phasic** spike, not a persistent accumulator -- and its input signal (`residue_surprise`) is
  already computed every step, independent of GAP-A. The gate does not extend to this SD; see
  Related Claims for the required cross-referencing.

## Solution

### Trigger channel derivation (resolves 12h; do not revert to the naive single-channel design)

12h's own text authorises reconsidering the channel/combination, not just lowering the threshold
("or reconsider the trigger channel/combination... or combine `residue_surprise` with the
mode-change signal, which responds more reliably"). Using the *classifier's* `mode` signal as an
architectural trigger input was rejected: Section 11a is explicit that `mode` is a post-hoc,
fixed-precedence bucketer over telemetry thresholds, not a substrate control state -- reusing it as
a trigger for a new core mechanism would smuggle the same non-mechanism dependency the review
critiques elsewhere back into the substrate.

Instead this SD uses **two already-computed, already-phasic substrate channels**, each matched to
the class of "sudden, unexpected, could-be-harmful" event it actually responds to, per the review's
own diagnostic data:

1. **`residue_surprise`** (unsigned `VALENCE_SURPRISE`, residue index 3; `ree_core/agent.py`
   `update_residue()`, `surprise = max(0, pe_mag - pe_ema)`) -- prediction-error onset. 12b/12h show
   this responds (weakly, sub-p90) to `external_hazard_injected` and (delayed) to
   `world_rule_shift_occurred`: genuine epistemic surprise about the *world*, not yet manifest as
   damage.
2. **`z_harm_s`** norm (SD-010 sensory-discriminative harm latent, `LatentState.z_harm`) -- 12g
   established this channel (distinct from the chronic, non-phasic `z_harm_a` that MECH-279/vigor
   already read) shows "a textbook appropriate phasic harm response": clean event-locked rise,
   peak one step after a harm event, smooth decay over ~10 ticks. 12g explicitly names this as the
   channel a trigger mechanism would want, as the direct complement to residue_surprise for
   nociceptive events (`limb_damage_injected`) that residue_surprise's own data shows it cannot
   catch.

**Trigger fires (positive-derivative / onset detector, per 11b step 1 -- NOT an absolute
threshold) when EITHER channel's current value exceeds its own slow rolling EMA baseline by more
than a configured delta.** This is a genuine onset detector (rises relative to recent ambient
level, not a fixed statistical cutoff of the overall distribution) and is deliberately two-channel
so no single ground-truth event class is structurally unreachable the way `residue_surprise`-alone
is for `limb_damage_injected`. Default deltas are seeded from the review's own event-triggered
numbers (external_hazard delta ~0.010 on `residue_surprise`; z_harm_s phasic bump ~0.006-0.02 per
12g's table) and are explicitly first-pass, config-exposed, and subject to revision by the
validation experiment (Step 8) -- this SD does not claim the seeded defaults are final calibration,
only that the *channel choice and detector shape* are grounded in 12g/12h rather than picked blind.

### The five components (11b/11d; all first-class, none deferred)

Module: `ree-v3/ree_core/pag/defensive_orienting.py` (`DefensiveOrientingGate` /
`DefensiveOrientingConfig` / `DefensiveOrientingOutput`). Matches the pure-scalar, non-trainable,
stateful-arithmetic pattern of `ree_core/pag/freeze_gate.py` (MECH-279) -- no `nn.Module`, no
learned parameters, no gradient flow. Deliberately a **separate, parallel** gate, not a
modification of `PAGFreezeGate`: the two freeze causes (chronic suffering-lock vs phasic
orienting-arrest) are architecturally distinct per 11b step 2, and keeping them separate preserves
`freeze_gate.py`'s existing behaviour bit-for-bit.

1. **Trigger** -- phasic onset (above) gated additionally by low identification confidence (the
   gate refuses a new trigger while already orienting; confidence resets to 0 on trigger).
2. **Phasic freeze (orienting arrest)** -- `orienting_active` commits on trigger. Held open-ended
   (no fixed timer -- `max_orienting_duration=0` default, mirroring `freeze_gate.py`'s own
   `max_freeze_duration=0` "no cap" convention) until epistemic sufficiency (component 4).
3. **Orienting reflex (return path to planned action)** -- modelled as an `identification_confidence`
   accumulator in [0,1] that rises **faster as the triggering channel's elevation decays back
   toward its baseline** (`confidence += rise_rate * (1 - residual_excess)`), not on a clock. This
   is the "attend to the stimulus until it resolves" dynamic: a sustained, non-decaying elevation
   never resolves (confidence stalls), a spike that a decays quickly resolves fast. Without this
   component freeze has no epistemic exit (11b step 3 -- load-bearing, not a deferred polish).
4. **Freeze override** -- fires when `identification_confidence >= sufficiency_threshold`.
   Releases `orienting_active`, distinct from the existing SD-037 orexin `override` channel (a
   different mechanism entirely -- broadcast recruitment vs freeze-release-on-epistemic-sufficiency).
5. **Action decision (approach / withdraw / resume)** -- resolved by the **agent**, not the gate
   (keeps the gate itself residue-field-independent, mirroring `freeze_gate.py`'s own "pure
   arithmetic over scalars" scope). On the override tick, the agent reads
   `residue_field.evaluate_benefit(z_world)` (ARC-030, always available regardless of the
   MECH-307 split-surprise flag) against `z_harm.norm()` (SD-010, always available) at the
   *current* z_world: `benefit > harm + eps -> approach`; `harm > benefit + eps -> withdraw`;
   otherwise `resume` (no bias, ordinary action selection proceeds unmodified). This is a
   deliberate substitute for reading the MECH-307 `VALENCE_POSITIVE_SURPRISE`/`NEGATIVE_SURPRISE`
   split, which is off by default and would make the decision step inert in most configurations;
   benefit-terrain-vs-harm is always-on and directly answers "did the identified thing turn out
   good or bad."

**Full pipeline:** `surprise/harm onset -> freeze -> orient/identify (confidence accumulates as
elevation decays) -> (knows enough) override releases freeze -> valence-gated
approach|withdraw|resume`.

### Data flow

```
z_harm (SD-010, LatentState.z_harm, current tick)          -\
residue_surprise (MECH-205 "surprise", cached from the       +-> DefensiveOrientingGate.tick()
  PREVIOUS tick's update_residue() call)                    -/        |
                                                                        v
                                              DefensiveOrientingOutput(orienting_active,
                                                trigger_fired, override_fired,
                                                identification_confidence, ticks_in_orienting)
                                                        |
        trigger_fired==True: capture z_world -> self._orienting_trigger_z_world
                                                        |
        override_fired==True: read benefit_terrain(z_world) vs z_harm.norm()
                               -> decision in {approach, withdraw, resume}
                                                        |
     decision != resume: per-candidate score_bias = decision_sign * scale *
       ||candidate.world_states[-1] - trigger_z_world||   (existing E3Selector.select()
       score_bias hook -- "lower is better"; composed additively into dacc_score_bias
       via the SAME idiom every other score_bias contributor in select_action() already uses)
       held for post_override_bias_ticks ticks, then cleared
                                                        |
     orienting_active==True (this tick, read after e3.select()): action forced to the SAME
       no-op mechanism PAGFreezeGate already uses (pag_freeze_noop_action_class), OR'd with
       the existing chronic-freeze constraint
```

### Config (REEConfig; all no-op defaults; bit-identical OFF)

| Param | Default | Purpose |
|-------|---------|---------|
| `use_defensive_orienting` | `False` | master switch (agent does not instantiate when False) |
| `orienting_surprise_ema_alpha` | `0.02` | slow EMA rate for the `residue_surprise` baseline |
| `orienting_harm_s_ema_alpha` | `0.02` | slow EMA rate for the `z_harm_s` norm baseline |
| `orienting_surprise_onset_delta` | `0.010` | trigger when `residue_surprise - baseline` exceeds this (seeded from 12h's external_hazard event delta) |
| `orienting_harm_s_onset_delta` | `0.010` | trigger when `z_harm_s_norm - baseline` exceeds this (seeded from 12g's phasic-bump range) |
| `orienting_confidence_rise_rate` | `0.15` | per-tick confidence gain scaled by `(1 - residual_excess)` |
| `orienting_confidence_floor_rise` | `0.0` | optional unconditional per-tick confidence floor rise (0.0 = purely decay-driven, matching 11b's "not a fixed timer") |
| `orienting_sufficiency_threshold` | `0.8` | confidence level at which override fires |
| `orienting_max_duration` | `0` | optional safety-valve tick cap (0 = no cap, mirrors `pag_max_freeze_duration=0`) |
| `orienting_decision_epsilon` | `0.01` | benefit-vs-harm margin below which the decision is `resume` (neither) |
| `orienting_decision_bias_scale` | `1.0` | score_bias magnitude scale for approach/withdraw |
| `orienting_post_override_bias_ticks` | `5` | how many ticks the approach/withdraw score_bias stays active after override |
| `orienting_noop_action_class` | reuses `pag_freeze_noop_action_class` | no separate knob -- deliberately shares the existing no-op class so both freeze causes constrain to the same "hold still" action |

### MECH-094

`simulation_mode=True` (replay / DMN content) returns a zeroed `DefensiveOrientingOutput` and does
**not** update the EMA baselines, `identification_confidence`, or the trigger/override counters --
mirrors `freeze_gate.py`'s own MECH-094 gate exactly. Replay content must not commit the agent into
an orienting-arrest state, and must not silently advance identification progress that only real
waking perception should earn.

### Phased training

Not applicable -- this is a non-trainable, pure-arithmetic control-state gate (no encoder head, no
parameters, no gradient flow), same category as `PAGFreezeGate` and `PhasicSurpriseBurst` (SD-069).

### Backward compatibility

With `use_defensive_orienting=False` (default), the agent does not instantiate the gate, the two
new call sites in `select_action()`/`update_residue()` are no-ops (guarded by
`self.defensive_orienting is not None`), and no other config default changes. Existing experiments
run bit-identically.

## Architecture Context

SD-099 is the phasic, unidentified-stimulus sibling of MECH-279 (chronic, accumulated-suffering
freeze) -- same PAG-analog freeze mechanism family, disjoint trigger and disjoint duration
semantics, composed via OR at the action-constraint site so either cause can hold the agent still.
It is also the mechanism that gives the Section 3/12g phasic `z_harm_s` and MECH-205
`residue_surprise` channels a behavioural consumer they did not previously have (12g/12h both note
these channels carry a clean phasic signal with no purpose-built downstream reader). The
approach/withdraw resolution reuses `E3Selector.select()`'s existing `score_bias` hook (already the
composition point for every other agent-level directed-bias contributor in `select_action()`)
rather than inventing a new action-selection pathway.

## What This SD Enables

- Closes the Section 11b/12e gap: a mechanism that latches onto and steers toward/away from a
  **specific identified stimulus location**, where none existed before (12e: `approach`/`avoid`
  mode movement direction was uncorrelated with the nearest resource/hazard, mean cosine
  0.019/-0.053).
- Gives the Section 4 / 12a temporal-decoupling finding (affect varies but does not organise
  behaviour; `is_committed`=0/3909) a direct organism-level intervention to test: post-build, the
  surprise-onset->freeze and post-identification dread->withdraw/excite->approach couplings should
  move well past the pre-build incidental baselines (12b: P(moved@t+1|spike)=44.3% vs 24.0%
  unconditional; P(mode-change@t+1|spike)=15.4% vs 11.1%).
- Validation experiment (MECH-489, Step 8) targets the exact ground-truth event set 12h identified
  as the naive design's failure mode (`limb_damage_injected`, `external_hazard_injected`,
  `world_rule_shift_occurred`).

## Related Claims

**MECH-489** (candidate mechanism this SD implements). **MECH-279** (PAG freeze-gate -- sibling,
chronic/suffering-driven, disjoint trigger, composed via OR at the action-constraint site, NOT
modified by this SD). **MECH-205** (VALENCE_SURPRISE write path -- source of the `residue_surprise`
trigger input). **MECH-395** (pre-approach orienting/surveying -- cue-triggered, need-gated,
resolves a vector for an ALREADY-IDENTIFIED cue; SD-099 is upstream of this in principle -- SD-099
fires on an UNIDENTIFIED stimulus and its own resolution is what would hand off to something
MECH-395-shaped, not the same mechanism). **MECH-482** (`epistemic_deficit` -- persistent
target-bound accumulator, explicitly defined against transient prediction error; SD-099's trigger
is exactly the transient/phasic case MECH-482 excludes by definition, and SD-099's input signal
(`residue_surprise`) is already computed every step, independent of MECH-482's GAP-A gate --
distinct mechanism, not a duplicate, per Section 12j). **MECH-483** (`orient/survey` -- diffuse
regime driven by MECH-482's accumulator, no specific cue or location; SD-099's orienting-arrest is
CUE-LOCATED (`self._orienting_trigger_z_world`) and phasic, the opposite of MECH-483's diffuse and
chronic character -- distinct mechanism, not a duplicate, per Section 12j). **SD-010/SD-011** (harm
stream separation -- the two channels this SD's trigger and decision steps read). **SD-014/ARC-036,
ARC-030/MECH-117** (valence vector, benefit terrain -- the resolution-read channels for the action
decision). **SD-037** (broadcast override regulator -- explicitly distinct "override" channel per
11b step 4, not reused here). **SD-069** (phasic surprise burst -- sibling non-trainable phasic
regulator pattern on a different consumer, the E3 softmax temperature rather than the freeze gate).
