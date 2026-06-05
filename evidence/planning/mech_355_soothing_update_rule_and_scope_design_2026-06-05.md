# MECH-355 soothing/comfort -- update-rule + scope design pass

**Date:** 2026-06-05
**Status:** design pass only. NO substrate code, NO claims.yaml status change. MECH-355 stays
`candidate` / `implementation_phase: v4` / `epistemic_category: substrate_conditional`
(promote/demote suppressed).
**Claim:** MECH-355 (`affect.soothing_comfort_autonomic_state_gain_modulator`),
`docs/claims/claims.yaml`.
**Routing input:** `evidence/literature/targeted_review_affect_stream_relief_safety_soothing/verdict.md`
("What this pull does NOT settle": (a) the exact update rule, (c) whether a non-social V3 hook is
worth building -- "needs a design pass, not more lit").
**Register row:** `docs/architecture/affect_primitives.md`, "Extension Primitive (V4-social;
V3-minimal hook optional): soothing / comfort".
**Cross-link (V4 ethics cluster):** `evidence/planning/thought_intake_2026-05-31_musings_on_v4.md`.
**Honours:** `feedback_biology_before_formal_definitions` (the philosophy-right / mechanism-wrong
guard that motivated the three-way relief/safety/soothing split in the first place).

---

## 0. What soothing IS, and the three things it is NOT (carried in from the verdict)

Soothing/comfort is a **present-tense, state-gain / recovery modulator** that lowers the
magnitude or speeds the recovery of the *currently active* aversive/stress trajectory,
canonically gated by a conspecific (social buffering; Hostinar/Sullivan/Gunnar 2014;
Heinrichs 2003 oxytocin x social support). It must stay dissociable from:

| Primitive | Time reference | Computational role | Why soothing != it |
|---|---|---|---|
| **Relief** (MECH-302, SD-050) | **past** (event-locked to aversive offset) | reinforcement teaching signal | relief *detects* the offset and writes a reinforcer; soothing *causes* the descent and writes no reinforcer |
| **Safety** (MECH-303/304, SD-051/052) | **future** (prediction over a horizon) | learned inhibitory predictor / gate | safety predicts threat is absent; soothing makes no prediction -- it acts on load already present |
| **Wanting** (MECH-112) | -- (appetitive) | approach/appetite | soothing down-regulates an aversive state; it is not appetite |

The design must preserve all three dissociations under ablation, or it has reproduced the
SD-010 -> SD-011 / SD-003 "collapse distinct biological systems into one REE primitive" failure.

---

## 1. The substrate the verdict named -- read precisely

The verdict's proposed home is loosely "MECH-219 (suffering accumulator) decay + SD-012 (drive) +
SD-032e (pACC autonomic coupling)". Inspecting the V3 code sharpens this into three concrete,
separable surfaces:

1. **MECH-219 z_harm_a hysteretic integrator** (`claims.yaml` MECH-219; the affective-load
   accumulator). A leaky integrator over `z_harm_un` (SD-019a) with **asymmetric onset and
   recovery** parameters, accumulation-rate **controllability-gated** by SD-019b. Two distinct
   knobs exist: the *onset/accumulation* rate and the *recovery/decay* rate.

2. **SD-032e pACC autonomic write-back** (`ree-v3/ree_core/cingulate/pacc_analog.py`). A slow EMA
   `drive_bias` accumulator of `tanh(||z_harm_a||) * drive_scale`, clipped to `[-cap, +cap]`,
   read out as `effective_drive(base) = clip(base + drive_bias, 0, 1)`. Crucially, the live tick
   only ever drives `drive_bias` toward `>= 0` (target = `tanh(norm)` or `0`); the **negative half
   of the cap range is currently unreachable**. There is an `offline_decay` hook (default `0.0`)
   that relaxes `drive_bias` toward 0 on offline entry, explicitly reserved for "a distinct
   sleep-recalibration claim".

3. **SD-012 base drive** (`ree-v3/ree_core/goal.py` `GoalState.update`). `drive_level = 1 - energy`,
   EMA-smoothed into `_drive_trace`, scaling `effective_benefit`. This is a **genuine homeostatic
   deficit (hunger)**.

### 1.1 A required sharpening: soothing must NOT touch base SD-012 drive

A soothed but hungry agent is **still hungry**. Soothing must not fake energy repletion. The
verdict's "SD-012 drive" element is therefore correctly read as *"the SD-032e `drive_bias` that
rides on top of SD-012 `drive_level`"* -- the **affective/autonomic sensitisation component** of
drive -- **not** the energy-derived base. Routing soothing through `drive_bias` (SD-032e) and
**never** through `drive_level` (SD-012 base) is a load-bearing design constraint: it keeps
soothing an *affective-state* modulator, not a homeostatic-deficit eraser. (This also keeps it
clear of wanting/MECH-112, which reads the deficit-scaled benefit.)

So the operative targets reduce to **two slow affective accumulators**: the MECH-219 `z_harm_a`
load and the SD-032e `drive_bias` autonomic baseline. SD-012 base drive is read-only to soothing.

---

## 2. Question 1 -- the UPDATE RULE

Let `S(t) in [0, 1]` be the soothing signal (V4: from the conspecific-buffering model; an
endogenous V3 sibling driver is discussed in section 3). Three candidate rules:

### Option A -- gain reduction (attenuate accumulation of *incoming* aversive signal)
- MECH-219: `onset_rate_eff = onset_rate * (1 - lambda_S * S)` (or scale the SD-019b accumulation
  gate). SD-032e: `target = tanh(norm) * drive_scale * (1 - lambda_S * S)`.
- **For:** structurally identical to a *second* controllability-style gate on MECH-219's existing
  accumulation term -- minimal new machinery, reuses the SD-019b insertion point. Maps to the
  Heinrichs-2003 finding that oxytocin x support **suppresses the cortisol response to a new
  stressor**.
- **Against (decisive for primacy):** it acts on **future** accumulation, not the load already
  present. Soothing's defining time-reference is the *present* trajectory; gain-reduction alone
  leaves an already-high `z_harm_a` untouched and only blunts further rises. Worse, reducing the
  accumulation of *expected/future* harm is **prediction-adjacent** -- it drifts toward the safety
  (MECH-303/304) computational role, exactly the collapse the verdict forbids.

### Option B -- decay acceleration (speed the *recovery* of state already present) -- RECOMMENDED
- MECH-219: `recovery_rate_eff = recovery_rate * (1 + mu_S * S)` (recovery side only; onset
  untouched). SD-032e: an active waking analog of the dormant `offline_decay` hook --
  `drive_bias *= (1 - leak_S * S)` per waking tick.
- **For:**
  - Acts on the **present** load -- matches soothing's time-reference exactly; the verdict's own
    canonical phrasing is "**speeds the recovery** of the active aversive trajectory".
  - **Load-proportional by construction** (see 2.1) -- the central safety property.
  - **Onset/sensory-preserving:** touching only the recovery side leaves MECH-219 onset, `z_harm_s`
    (SD-010) and `z_harm_un` (SD-019a) intact. A soothed agent still *detects* a fresh injury at
    full sensitivity and can still act on ongoing sensory harm; only the lingering suffering-load
    and autonomic sensitisation decay faster. This mirrors SD-021's discipline (attenuate
    `z_harm_s` under commitment, let `z_harm_a` persist) with **inverse selectivity**.
  - **Clean dissociation from relief:** relief (MECH-302) *fires on* `d||z_harm_a||/dt < 0`
    (offset detection) and writes a reinforcer. Decay-acceleration soothing **causes** that
    derivative to go more negative. Soothing is therefore the *upstream cause* and relief the
    *downstream readout/reinforcer* -- they compose without collapsing (under soothing, relief
    fires **earlier**; soothing itself writes no reinforcer). Falsifiable and elegant.
  - **Clean dissociation from safety:** acts on present accumulated state, requires no prediction
    over any horizon.
- **Against / mitigations:** over-aggressive recovery could mask a *persistent* real hazard.
  Mitigated by the onset/sensory-preserving selectivity above (the agent still feels and avoids
  ongoing sensory harm; only affective load + autonomic baseline relax). Note the intended
  behavioural consequence on MECH-091: faster `z_harm_a` decay lowers urgency-interrupt
  probability -- i.e. a soothed agent is **less likely to panic-abort** a committed plan, which is
  the behaviourally correct signature of social buffering, **a feature, not a bug**.

### Option C -- setpoint shift (subtract a fixed offset from the read)
- e.g. `effective_drive = clip(base + drive_bias - S_offset, 0, 1)`; or `z_harm_a_eff =
  max(0, z_harm_a - S_offset)`.
- **For:** one-line fit to SD-032e's existing `effective_drive` read.
- **Against (rejected as primary):** **state-independent** in a dangerous way. A fixed subtractive
  offset pushes a *calm* agent (`drive_bias ~ 0`) sub-baseline -- the **sedation** failure mode,
  not soothing. A hug when already calm does not make you hypo-aroused; soothing's effect must be
  *proportional to current load* and **zero on an unstressed agent**. To make setpoint-shift safe
  you must gate it by current load -- at which point it **is** decay-acceleration with extra steps.
  The subtractive clamp on `z_harm_a` is additionally brittle (clips/loses signal).

### 2.1 The decisive property -- load-proportionality (soothing != sedation)
Because decay-acceleration acts **multiplicatively on the recovery/leak of existing accumulated
state**, `S` has **zero effect when there is nothing accumulated** (`z_harm_a ~ 0`,
`drive_bias ~ 0`). A calm agent cannot be driven sub-baseline. This is the formal guarantee that
distinguishes soothing from sedation, and it is exactly the property Option C lacks and Option A
only partially provides. It falls out of Option B for free.

### 2.2 Recommendation
**Primary rule = decay-acceleration (Option B)**, applied to the **recovery side** of the two slow
affective accumulators:
- MECH-219: `recovery_rate_eff = recovery_rate * (1 + mu_S * S)` (onset untouched).
- SD-032e: `drive_bias *= (1 - leak_S * S)` per waking tick (active analog of the dormant
  `offline_decay` hook; this is also the first principled use of the **negative-relaxation**
  direction the cap already permits but the live tick never reaches).
- **Untouched:** SD-012 base `drive_level`, `z_harm_s` (SD-010), `z_harm_un` (SD-019a).

**Optional secondary face (default-OFF, togglable) = a small gain-reduction term on the SD-032e
accumulation *write only*:** `target = tanh(norm) * drive_scale * (1 - lambda_S * S)`. This is the
Heinrichs-2003 "oxytocin x support suppresses the cortisol **response**" face. Keep it:
- **separable and default-off** (the MECH-314a/b/c precedent of one module + independently
  togglable faces), so the V4 validation can dissociate which face carries the load; and
- **on the SD-032e autonomic write, NOT on MECH-219 onset**, so it never blunts nociceptive
  detection. The gain-reduction face is the one that flirts with safety-prediction territory;
  keeping it ablatable lets the validation **prove** soothing is not a safety signal in disguise
  (ablate the gain face -> peak `z_harm_a` to a new stressor is unchanged with soothing ON; only
  recovery speed differs).

**Reject setpoint-shift (Option C) as primary** (sedation failure mode; duplicates B once
load-gated). **Reject gain-reduction (Option A) as primary** (acts on future not present;
prediction-adjacent / safety-collapse risk) -- but retain its narrow, autonomic-write-only form as
the optional, ablatable secondary face above.

### 2.3 Where soothing reads/writes (summary)
- **Input** `S(t) in [0,1]`: V4 from the conspecific-buffering model; (optional V3 sibling driver:
  section 3).
- **Writes (primary):** MECH-219 recovery-rate multiplier; SD-032e `drive_bias` leak.
- **Writes (optional secondary, default-off):** SD-032e accumulation-target gain.
- **Never writes:** SD-012 `drive_level`, `z_harm_s`, `z_harm_un`.
- **MECH-094:** soothing is a waking-stream modulator. A soothing input arriving during
  replay/simulation (`hypothesis_tag=True`) must be **skipped**, identical to the SD-032e
  `tick(hypothesis_tag=...)` convention. Replay must not relax the agent's real affective load.

---

## 3. Question 2 -- SCOPE (is a non-social V3-minimal autonomic-recovery hook worth building?)

### 3.1 Recommendation: DEFER the soothing substrate to V4-social; do NOT build a V3-minimal soothing hook.

The **mechanism** above (decay-acceleration) is trigger-agnostic -- the substrate is identical
whether `S(t)` comes from a conspecific (V4) or an endogenous process (V3). So the question is
entirely about the **trigger**, and that is where V3 fails:

Every candidate endogenous V3 trigger for a *soothing* signal is either redundant or
collapse-inducing:
- **Time-since-stressor-offset / autonomic rebound** -- arguably already what the MECH-219 passive
  `recovery_rate` *is*. Making it "active" without a new driver is just retuning an existing
  parameter; it does not instantiate a distinct claim.
- **A safe-context signal** -- that is MECH-303 contextual safety terrain. Folding soothing's
  trigger into safety is **exactly the collapse the verdict forbids**.
- **Reef/refuge contact** (SD-054) -- environmental safety again; safety-adjacent.

The thing that makes soothing *distinct* -- a conspecific actively down-regulating your *present*
stress -- is precisely the thing V3 cannot represent. A V3-minimal soothing hook would therefore
be either (i) indistinguishable from tuning the existing `recovery_rate`, or (ii) smuggling safety
in as the trigger and contaminating the claim. Both are the philosophy-right / mechanism-wrong
failure mode this lineage exists to avoid. The claim is registered `substrate_conditional` / V4
/ promote-demote-suppressed for exactly this reason; building a V3 hook now would generate evidence
that cannot cleanly weight the V4-social claim (different trigger) and risks contamination. It is
also off the V3 critical path, which the user flagged for this whole stream.

**So: pre-register the mechanism (section 2) now as trigger-pluggable; build the substrate at
V4-social.**

### 3.2 The nuance worth surfacing: a *separate*, non-soothing V3 gap -- the parasympathetic-poor asymmetry

There **is** a legitimately distinct, non-social, non-safety V3 substrate gap hiding under this
question, and it should be named so it is not lost:

REE's V3 control stack is **sympathetic-rich, parasympathetic-poor**. The escalation/opening side
is dense -- MECH-219 onset, SD-032e accumulation, SD-037 orexin override, MECH-091 urgency, MECH-279
PAG freeze. The **recovery/closing side is thin**: `z_harm_a` relaxes only via its passive
`recovery_rate`, and `drive_bias` relaxes only passively toward 0 (and the only active relaxation,
SD-032e `offline_decay`, defaults 0 and fires offline). There is **no active waking
parasympathetic-recovery process** that accelerates return-to-baseline after a stressor ends.

That gap is real and V3-tractable, and it is *mechanistically the same update rule as soothing*
(decay-acceleration) -- but with an **endogenous, offset-triggered driver** rather than a social
one. The natural trigger is the **stressor-offset signal REE already computes**: the `z_harm_a`
derivative going negative (the very signal MECH-302 relief detects). An "autonomic rebound /
endogenous parasympathetic recovery" mechanism would: detect own-stressor offset -> transiently
raise the MECH-219 recovery-rate / SD-032e leak -> faster return-to-baseline. No conspecific, no
safety prediction.

**Recommendation:** if the user wants to close the parasympathetic-poor asymmetry, do it as a
**separate candidate sibling claim** ("endogenous parasympathetic recovery / autonomic rebound",
offset-triggered, V3-tractable), governed on its own evidence. **Do NOT fold it into MECH-355.**
MECH-355 stays the V4-social, conspecific-gated claim. This:
- keeps the social claim clean (its trigger is the conspecific; that is its scientific content);
- gives the user a clean V3 path to close a genuine substrate asymmetry, if desired, without
  contaminating the soothing claim;
- respects the verdict's "optional V3-minimal hook **noted but not built**" and
  `feedback_biology_before_formal_definitions`.

This sibling is a *suggestion surfaced, not started* (scope discipline). It is gated on an explicit
user decision and, if pursued, its own lit-pull (autonomic rebound / parasympathetic recovery
literature) before registration -- soothing's social oxytocin/HPA anchors do not transfer to an
endogenous offset-triggered mechanism.

---

## 4. Falsification signatures (for the eventual V4-social validation; not run here)

With the recommended decay-acceleration rule and the gain-reduction face default-off:
1. **Recovery acceleration:** after a *matched* stressor offset, `z_harm_a` and `drive_bias`
   return to baseline **faster** with soothing ON than OFF; **onset and peak unchanged**.
2. **Load-proportionality (soothing != sedation):** soothing has **no measurable effect** on a
   never-stressed agent (zero accumulated state -> nothing to decay).
3. **Dissociation from relief:** MECH-302 relief fires **earlier** under soothing (soothing
   accelerates the descent relief detects), but soothing itself writes **no reinforcer**.
4. **Dissociation from safety (gain-face ablation):** with the optional gain-reduction face OFF,
   **peak** `z_harm_a` to a *new* stressor is unchanged with soothing ON (only recovery speed
   differs) -- proving soothing is not a safety predictor blunting expected harm. Enabling the
   gain face is the *only* licensed touch on a not-yet-fully-realised signal, and it is the
   Heinrichs response-suppression face, explicitly distinct from prediction.
5. **Sensory preservation:** ongoing `z_harm_s` / `z_harm_un` and avoidance behaviour to a present
   sensory hazard are unchanged with soothing ON.

---

## 5. Decision summary

| Question | Decision |
|---|---|
| **Update rule** | **Decay-acceleration** (recovery-side) on MECH-219 `recovery_rate` + SD-032e `drive_bias` leak. Optional default-off, ablatable **gain-reduction** face on the SD-032e accumulation *write only* (Heinrichs response-suppression). Reject setpoint-shift (sedation) and gain-reduction-as-primary (prediction-adjacent). |
| **Substrate target sharpening** | Route through SD-032e `drive_bias` (affective/autonomic component) + MECH-219 recovery; **never** through SD-012 base `drive_level`, `z_harm_s`, or `z_harm_un`. |
| **Key safety property** | Load-proportional by construction (multiplicative on existing-state recovery) -> zero effect on a calm agent -> soothing != sedation. |
| **Scope** | **Defer soothing substrate to V4-social** (every V3 endogenous trigger is redundant with `recovery_rate` or collapses into safety/refuge). Pre-register the trigger-pluggable mechanism now. |
| **Surfaced sibling (not started)** | A *separate* V3-tractable "endogenous parasympathetic recovery / autonomic rebound" claim (offset-triggered; same update rule, endogenous driver) to close the sympathetic-rich/parasympathetic-poor asymmetry -- gated on user decision + its own lit-pull; **not** folded into MECH-355. |
| **MECH-355 status** | Unchanged: `candidate` / `v4` / `substrate_conditional`. This is a design pass only. |

---

## 6. Cross-references
- `evidence/literature/targeted_review_affect_stream_relief_safety_soothing/verdict.md` (routing
  verdict; "what this pull does NOT settle" items (a) + (c)).
- `docs/architecture/affect_primitives.md` -- soothing Extension-Primitive row (this design
  resolves its "V4 substrate + update rule are later design decisions" placeholder).
- `claims.yaml` MECH-355 (soothing), MECH-219 (z_harm_a hysteretic integrator -- recovery-side
  target), SD-032e (pACC `drive_bias` -- leak target), SD-012 (base drive -- **excluded** target),
  MECH-302/SD-050 (relief -- upstream/downstream dissociation), MECH-303/304 + SD-051/052 (safety
  -- the collapse to avoid), MECH-112 (wanting -- orthogonal), SD-019a/SD-019b (z_harm_un + onset
  controllability gate), SD-021 (descending-modulation selectivity precedent), MECH-091 (urgency
  interrupt -- intended downstream behavioural consequence), MECH-094 (waking-only write gate).
- `evidence/planning/thought_intake_2026-05-31_musings_on_v4.md` -- **V4 ethics cluster**
  cross-link: soothing (other-agent down-regulates *your* present stress) and that cluster's
  social-repair primitives both sit in the V4-social tier that requires the other-agent model;
  the surfaced "endogenous parasympathetic recovery" sibling is the V3-side complement, kept off
  the V4 social line just as that cluster is kept off the V3 line.
