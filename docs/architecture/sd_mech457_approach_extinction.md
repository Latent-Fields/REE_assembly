---
title: "SD-mech457_approach_extinction: experiments/_lib approach-drive extinction-on-contact"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 26
---

# SD-mech457_approach_extinction: experiments/_lib approach-drive extinction-on-contact

**Claim ID:** mech457_approach_extinction (substrate node; not a claims.yaml claim)
**Subject:** experiments/_lib.mech457 approach-drive extinction-on-contact
**Status:** IMPLEMENTED
**Registered:** 2026-07-25
**Implemented:** 2026-07-25
**Depends on:** mech457_consummatory_act (IMPLEMENTED 2026-07-25), the V3-EXQ-781 approach
primitive (`use_approach_primitive`/`approach_coef`)
**Blocks:** H-consummation-binding (the last open retention leg of the `competence_floor`
question, MECH-457)
**Design doc:** `evidence/planning/mech457_retention_portfolio_2026-07-18.md` (leg 4),
`evidence/planning/competence_floor_reposing_2026-07-25.md`, `sd_mech457_consummatory_act.md`

## Problem

Leg 4 of the MECH-457 retention portfolio (H-consummation-binding) tests whether V3-EXQ-781's
drive-side null was an artefact of a missing consummatory act. 781 found an appetitive approach
drive *earned* at 0.707 while raw-view foraging was *suppressed* to 0.200 from a 2.983 control --
approach without consummation. The leg-4 treatment arm needs an approach drive that
**extinguishes on resource contact and hands off to a distinct CONSUME act**, contrasted against
781's non-extinguishing terminal drive.

The `mech457_consummatory_act` env node (2026-07-25) built the ENV half: a distinct CONSUME
action, `transition_type="resource_contact"` on contact (zero benefit reward, resource
retained), and the `on_consumable_resource` flag in `info`. But **nothing consumed that signal.**
781's approach primitive is an intrinsic reward computed in `train_a2c`:

```
appr = approach_coef * resource_proximity(obs_dict)   # added unconditionally, every step
```

`resource_proximity` reads `obs_dict`, which does **not** carry `on_consumable_resource` (that
flag lives in `info`), and `train_a2c` never threaded `info` to the approach hook. A
repository-wide grep confirmed **no consumer of `info['on_consumable_resource']`** exists outside
the env that sets it. So the drive could not extinguish on contact, and the leg-4 treatment arm
was not buildable at the driver level.

### Correcting the consummatory_act design doc's claim

`sd_mech457_consummatory_act.md` (lines 30-33, 70-76) stated the "drive half was already built"
via the "already-wired `goal.py` drive machinery reacting to `resource_contact` /
`on_consumable_resource`". That is **incorrect for this experiment's path**:

- `goal.py`'s drive is the **homeostatic** per-axis system (`drive_ema_alpha`, `drive_floor`,
  `per_axis_restoration_fraction`). It is a *different* system from 781's approach primitive.
- `goal.py` does **not** reference `on_consumable_resource` or `resource_contact` anywhere.
- `goal.py` is **not imported or invoked** in the mech457 bootstrap-explorer path. `GOAL_DIM = 2`
  in that path is a relative (dx, dy) spatial-navigation vector to a target cell, not a
  physiological drive.

The env correctly *emits* the affordance signal; this SD supplies the missing *consumer* of it
for 781's approach primitive.

## Solution

A single default-OFF knob threads the env's affordance flag into the approach-reward
computation. The OFF path is byte-identical to the pre-change non-extinguishing drive.

Modules: `experiments/_lib/mech457_bootstrap_explorer.py`,
`experiments/_lib/mech457_explorer_classes.py`. The mechanism lands in `experiments/_lib/**`, so
it enters the arm-fingerprint `substrate_hash` (a consummatory-ON extinguishing cell can never
collide with a pre-change cell).

- **Config:** `BootstrapExplorerConfig.approach_extinguishes_on_contact: bool = False`, declared
  in `as_slice()`. The env's `consummatory_act_enabled` is a **direct env constructor kwarg** set
  by the driver in `env_kwargs` (this config does not build the env), not a config field.
- **Wiring:** `train_bootstrap_explorer` forwards `cfg.approach_extinguishes_on_contact` to
  `train_a2c` alongside `approach_drive`/`approach_coef`.
- **Extinction (`train_a2c`):** in the approach block, on any tick where
  `info["on_consumable_resource"]` is True the approach reward is zeroed:

  ```python
  appr = approach_coef * approach_drive(obs_dict)
  if approach_extinguishes_on_contact and info.get("on_consumable_resource", False):
      appr = 0.0   # drive terminates on arrival; hand off to CONSUME
  shaped += appr
  ```

  `info` is the post-step info from `env.step()`, so `on_consumable_resource` reflects the agent's
  final standing cell for that tick.
- **Half-wired is an error (`train_a2c` raises).** `approach_extinguishes_on_contact=True`
  requires (1) an `approach_drive` (`use_approach_primitive=True`) -- extinction with no drive is
  the control wearing the treatment label; (2) the env built with `consummatory_act_enabled=True`
  -- otherwise `on_consumable_resource` is always False and extinction silently never fires. This
  mirrors the probe / kl-anchor half-wired guards.

## Architecture Context

Completes the DRIVE half of leg 4; the `mech457_consummatory_act` env node is the ENV half.
Orthogonal to the three other manipulation nodes (`mech457_distributional_critic` = value
estimator; `mech457_policy_kl_anchor` = update constraint; `mech457_bc_aux_schedule` = auxiliary
persistence): this node changes only the appetitive-drive termination on the action-space /
consumption binding, preserving the portfolio's anti-alias partition. The leg still reads the
`mech457_retention_trajectory_probe` DV (post-installation competence trajectory), adjudicated
from V3-EXQ-780's ~20.933 install point.

## Blast radius

Additive and default-OFF. With `approach_extinguishes_on_contact=False` the extinction branch
never fires -- byte-identical to the pre-change non-extinguishing drive (contract E1 asserts
weight-identity; V3-EXQ-788 dry-run confirmed the `train_bootstrap_explorer` path unchanged).
Editing `experiments/_lib/**` changes the `substrate_hash` for the mech457 lineage, so
pre-change baseline arm fingerprints are correctly refused for reuse across the change -- expected
and identical in kind to the `mech457_consummatory_act` and `mech457_retention_trajectory_probe`
landings. The already-completed retention legs (788/789/792a) are unaffected (their manifests are
recorded; reuse-refusal only affects future runs), and the leg-4 lineage is a new consummatory-ON
(action_dim 6) lineage that could not reuse the 5-action baselines anyway.

## What This SD Enables

`H-consummation-binding` becomes buildable as a two-arm `/queue-experiment` leg: an extinguishing
approach drive (`consummatory_act_enabled=True` in env_kwargs +
`approach_extinguishes_on_contact=True`) that hands off to CONSUME, versus 781's non-extinguishing
terminal drive control, adjudicated on the post-installation competence trajectory. Prediction
directions: competence still flat under the extinguish-and-hand-off arm => the binding is **not**
what 781 lacked (H eliminated); competence retained under the consummatory arm but not the
non-extinguishing control => 781's drive-side null was a consummatory-act artefact.

## MECH-094 / phased training

- **MECH-094:** N/A. No simulation, replay, or non-waking memory write.
- **Phased training:** not required. No encoder head trained on a latent signal; this is a
  reward-shaping / drive-termination wiring change.

## Validation

Contracts `tests/contracts/test_mech457_approach_extinction.py` (E1-E6, 7 tests, all pass in
3.72s locally): default-OFF byte-identical on trained weights; extinction fires and changes the
learned policy on a consummatory env with proven contact (non-degeneracy: OFF drive fired +
contact occurred); both half-wired guards raise; `as_slice()` declares the knob and defaults it
False; the config-level half-wired guard fires through `train_bootstrap_explorer`; ASCII-only
sources. The mech457 contract regression surface (bootstrap-explorer, retention-probe, kl-anchor,
distributional-critic + arm-fingerprint / inert-knob lints) passes 96/96 with the change. The
behavioural **H-consummation-binding** experiment (V3-EXQ-821) is the validation run, queued via
`/queue-experiment`.

## Companion build: consummatory-aware reference/demonstrator policies

The leg-4 experiment uses the **retention (BC-install) framing** (architect decision 2026-07-25):
BC-install the raw-view policy to its competence band, then RL-refine under the approach drive
and measure whether the installed competence is RETAINED under an extinguishing vs a
non-extinguishing drive, on the `mech457_retention_trajectory_probe` DV. That framing needs a
demonstrator and readiness anchors that can forage in the consummatory env, which the hand-coded
greedy policies could not (they return "stay" on the target cell and never CONSUME). Built the
same day in `experiments/_lib/capability_eval.py`: a shared `_consummatory_consume_action(env)`
helper applied to `OraclePolicy` and `LocalViewGreedyPolicy`, returning the CONSUME index when the
env is in consummatory mode and the agent stands on a resource cell (gated; byte-identical no-op
otherwise). Measured: in the D3 consummatory env `local_view_greedy` forages ~13.5/ep and
`greedy_oracle` ~13.0 (vs ~17.9 / ~18.7 non-consummatory -- CONSUME costs one step per resource),
so the consummatory achievable ceiling / install band is ~13, **not** the non-consummatory 20.933;
the leg records the live consummatory anchors as denominators. Contracts:
`tests/contracts/test_consummatory_aware_policies.py` (CG1-CG4). This is why the demonstrator-free
781 framing (which needs no BC install) was the buildable-without-it alternative; the retention
framing was chosen and this companion build unblocks it.

## Related Claims

MECH-457 (candidate / v3_pending -- this node promotes/demotes/gates nothing), INV-088, and the
sibling nodes `mech457_consummatory_act`, `mech457_distributional_critic`,
`mech457_policy_kl_anchor`, `mech457_bc_aux_schedule`, `mech457_retention_trajectory_probe`.
