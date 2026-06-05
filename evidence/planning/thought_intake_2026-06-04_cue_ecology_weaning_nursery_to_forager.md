# Thought intake: cue ecology and the nursery-to-forager weaning arc

**Date:** 2026-06-04
**Status:** intake (plan-of-record framing; not yet a registered claim cluster)
**Origin:** user thought on the V3-EXQ-638 cue-recall bridge, 2026-06-04, after the
early live read showed `cue_fires=0` in the cue-on arm.
**Anchors:** SD-057 / MECH-347 (cue-recall), `scaffolded_sd054_onboarding`,
`goal_pipeline:GAP-2` (foraging-contact ceiling), MECH-295 (approach bridge),
SD-012 / MECH-216 (drive-modulated wanting), SD-049 (per-type tags + per-axis drive).

---

## 1. The developmental arc this is about

REE-v3 has a **failure-to-thrive / nursery-to-forager bottleneck** (`goal_pipeline:GAP-2`):
Stage-0 forced feeding forms `z_goal`, Stage-0b protected consolidation preserves it,
but autonomous foraging / contact / completion in the wild (P1/P2) stays unreliable
(2/3 seeds die or never make benefit contact). The cue-recall bridge (SD-057 L6) was
introduced as the lever meant to break that: a perceived resource cue retrieves its
incentive token and pulls `z_goal` toward it *before* contact, bootstrapping the first
approach.

The intended weaning sequence:

> nursery feeding -> protected consolidation -> **body-state cue + food cue -> cue-recall
> wanting -> approach -> real contact** -> autonomous foraging.

The question this intake frames: **does REE-v3 need a richer cue ecology to walk that
arc, and if so, which part is missing?**

## 2. Two layers, not one (the load-bearing distinction)

The `cue_fires=0` symptom forces a split that must not be conflated:

- **Layer 1 -- token FORMATION (does the cue have anything to recall?).** The cue can
  only fire if the incentive-token bank holds a token for the perceived type. If the
  bank is empty, the cue is silent for a *wiring* reason, not an *ecology* reason.
- **Layer 2 -- cue MEANING / behavioural AUTHORITY (does a fired cue change behaviour,
  and should it, given body state?).** Even with a populated bank, a purely
  exteroceptive cue ("a resource is nearby") may fire without producing approach, or may
  fire when the agent has no need. The proposed fix is that the cue should mean *"this
  perceived thing matters for my current body/drive state because it has restored me
  before"* -- i.e. interoceptive need bound to external affordance.

Jumping to Layer 2 before settling Layer 1 risks "fixing" the bridge for the wrong reason
and masking the wiring bug. The 638 read pointed at Layer 1 first, and the audit confirmed it.

## 3. What the V3-EXQ-638 audit found (2026-06-04)

Code-confirmed root cause (Layer 1): the `IncentiveTokenBank` was **empty** entering
P1/P2. `agent.cue_recall_wanting` returns 0 at `k not in bank._base_value`. Stage-0
forced feeding *did* pass `resource_type` into `update_z_goal`, but it used the
ACTUALLY-CONTACTED type (`_contacted_resource_type(obs)`), which is almost always `None`
because forced feeding is decoupled from standing on a typed cell -- so the L2 bank-bind
(`bank.update`, gated `resource_type>0`) was never reached. Tokens otherwise only bind on
real P1/P2 typed contact -- the very GAP-2 contact the cue was meant to bootstrap
(**chicken-and-egg**). A bare `except: pass` made the zero undiagnosable.

**Fix landed** (`scaffolded_sd054_onboarding` amend 2026-06-04b, commit a9ef0be,
no-op-default, bit-identical OFF):
- Instrumented the cue path (per-non-fire reason attribution + bank/proximity/drive
  diagnostics; `except: pass` -> visible `exception:<Type>`).
- New flag `scaffold_stage0_bind_incentive_token`: Stage-0 forced feed binds the token to
  the **strongest-perceived** type (identical perception to recall) so the bank is
  non-empty entering the wild.
- Smoke: Stage-0 `token_bank_size_end` 0 -> 2; P1 `cue_fires` 0 -> 34.

## 4. The Layer-2 signal already visible

In the activation smoke, P1 `drive_peak = 0.037` -- the agent is **well-fed** when the
cue fires, so it fires with only modest amplitude. This is exactly the Layer-2 territory:
a purely exteroceptive cue fires on "resource perceived" regardless of need. A
need-gated cue should fire *hard* only when **depleted body state AND external resource
cue AND a matching restoration token** coincide. The instrumentation now measures
`drive_peak` and reserves `n_interoceptive_need_cues` / `n_joint_cues` for this layer.

## 5. The discriminator: what V3-EXQ-638a settles

638a re-runs 638 with the formation fix on (`scaffold_stage0_bind_incentive_token=True`),
3 seeds. Outcomes route the next move:

| 638a result | Reading | Next |
|---|---|---|
| Cue fires AND P2 contact lifts (>=2/3) | Formation gap was the whole story | Promote the cue bridge; close the GAP-2 contact lever for this path |
| Cue fires but **no contact lift** | Cue has no behavioural authority -- the Layer-2 (interoceptive meaning / approach coupling) bridge is the real missing piece | Build interoceptive need-gating + 638b arms |
| Cue still does not fire | Formation fix insufficient (perception / token / wiring) | Re-audit via the new `cue_nonfire_reason_counts` (now diagnosable) |

The value of the instrumentation is that every branch is now *attributable* rather than a
bare zero.

## 6. Layer-2 design sketch (NOT yet implemented; next pass)

Bind, at Stage-0 forced feeding, a richer token: `(resource_type, body/drive state,
restoration benefit)`. At P1/P2, allow cue recall to acquire full authority only when:
**(a)** an external resource cue is perceived, **AND (b)** current interoceptive
drive/body-state indicates need, **AND (c)** a matching restoration token exists.
Body/drive cues: energy depletion (`obs_body[3]`), drive trace (SD-012), benefit absence,
"needs restoration" state. This BINDS internal need to external affordance; it does not
replace external cueing.

Biological grounding to pull when this layer is built (Layer-2 lit pull, check existing
`targeted_review_2026-06-01_object_bound_incentive_salience` first):
- Berridge & Robinson -- incentive salience is *state-dependent* (cue-triggered wanting
  amplified by relevant physiological state).
- Toates -- motivational-state x incentive-stimulus interaction.
- Cabanac -- alliesthesia (a stimulus is wanted/pleasant conditionally on internal state).
- Conditioned-place-preference drive-dependence; Zhang/Berridge computational
  `kappa(drive) * V_hat` (already the shape REE uses in SD-012 / MECH-216 / MECH-295).

REE already instantiates drive-modulation elsewhere (SD-012 `effective_benefit =
benefit * (1 + drive_weight * drive)`, MECH-216 `W_m = kappa(drive) * V(salience)`,
MECH-295 drive->liking->approach), so the Layer-2 cue gate is consistent with the
existing substrate rather than a new primitive.

## 7. Methodological commitment

Do **not** tune to pass. The goal is to determine whether REE-v3 needs a richer
(interoceptive + exteroceptive) cue ecology for weaning, and to keep each layer's failure
*attributable*. The formation fix made the cue capable of firing; whether a fired cue is
behaviourally consequential -- and whether it needs body-state meaning to be so -- is the
open scientific question 638a (then 638b) is designed to answer.

## 8. Captured future follow-up: safe weaning as its own layer (routing only)

**Status: captured future follow-up / routing guidance only. NOT new V3 scope, NOT an
active work item, and NOT a change to any current experiment's acceptance criteria. It
becomes actionable only if the result pattern below appears.**

The two layers above (formation, then interoceptive need-gating / behavioural authority)
both ask whether a cue can *produce contact*. They do not yet name a distinct later step:
whether cue-guided contact can occur **safely** -- without survival collapse, reckless
hazard approach, or dependence on excessive scaffold support. Make that step explicit in
the weaning arc:

> nursery feeding -> token formation -> cue recall -> contact lift -> **safe weaning** ->
> autonomous foraging.

**Routing rule.** If 638a or 638b shows cue fires AND contact lift but **survival worsens
or hazard exposure increases**, that is *not* a cue-recall failure and must not be read as
one (the cue did its job: it produced approach). Route it instead to a separate
**"safe-weaning scaffold" / "hazard-safe cue-guided approach"** follow-up -- a later
diagnostic that would test whether cue-guided contact can be sustained without survival
collapse, reckless hazard approach, or reliance on excessive scaffold support. This is the
weaning-arc analogue of: a pup that has learned to approach food but not yet to do so
without getting eaten.

This keeps the 638a/638b discriminator (sections 5-6) clean -- those experiments test
*recall -> contact*; the safe-weaning layer tests *contact -> autonomous survival* -- and
prevents a survival regression from being misattributed to the cue bridge.

## 8b. 638a result + measurement-gap correction (added 2026-06-05)

638a returned **C1 PASS + C3 FAIL** (cue fires 1050/180/446 in P2, token bank
0->3, but contact does not lift). Section 5 routes this branch straight to
"Cue has no behavioural authority -> build interoceptive need-gating + 638b."
The 638a data forces a correction before that build:

1. **The cue is not behaviourally neutral -- it is mildly counterproductive.**
   ARM_CUE_ON contact `[0.0, 0.0, 0.267]` is <= ARM_OFF `[0.0, 0.197, 0.648]` on
   EVERY matched seed (0/3 show ON > OFF). Wild seeding alone reaches contact;
   firing the cue produced less. **Displacement hypothesis:** cue recall pulls
   z_goal toward a weak token (`matched_token_strength ~ 0.2`, 0.023 on seed 44)
   and may overwrite the stronger wild-seeded attractor -- net-negative authority,
   not merely a missing one.
2. **drive_peak = 0.28 on the zero-contact seed 42** (depleted, not well-fed),
   with 1050 fires and a matched token, still 0 contact. This WEAKENS the pure
   interoceptive reading (Section 4's "well-fed so the cue fires soft") as the
   proximate cause of the seed-42 zero.
3. **638a cannot discriminate** cue-to-action authority / gradient-following /
   interoceptive / orienting / hazard-interrupt, because it logged no post-cue
   action trace -- only `n_cue_recall_fires` and `contact_rate`, nothing between.

**Consequence (user-confirmed 2026-06-05):** do NOT build the 638b interoceptive
substrate yet. The smallest next step is a **measurement-only** post-cue
action/gradient diagnostic (proposed **V3-EXQ-640**) that re-runs the ablation
behaviourally unchanged with per-cue-fire instrumentation (`post_cue_z_goal_norm_delta`,
`cue_action_bias_magnitude`, `post_cue_selected_action_approach_rate`,
`post_cue_manhattan_distance_delta_to_resource`, `salience_interrupt_count_after_cue`,
`cue_to_first_gradient_improving_move_latency`). **640 GATES 638b.** Full diagnosis,
branch ranking, and discriminator map in
`failure_autopsy_V3-EXQ-638a_2026-06-05.{md,json}`.

## 9. Cross-references

- `scaffolded_sd054_onboarding` cue-recall bridge + formation-fix amend (ree-v3/CLAUDE.md).
- SD-057 / MECH-347 (L6 cue-recall) / MECH-348 (L7 dACC readout); `goal.py`
  `IncentiveTokenBank`, `agent.cue_recall_wanting`.
- `goal_pipeline:GAP-2` (foraging-contact ceiling), `goal_pipeline:GAP-7` (object-bound
  incentive-salience layer).
- V3-EXQ-638 (cue-silent FAIL), V3-EXQ-638a (formation-fix validation), V3-EXQ-638b
  (planned: OFF / EXTERNAL_ONLY / INTEROCEPTIVE+EXTERNAL arms).
- SD-012 / MECH-216 / MECH-295 (existing drive-modulation the Layer-2 gate aligns with).
