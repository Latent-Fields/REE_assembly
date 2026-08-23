---
title: "SD-mech457_consummatory_act: environment.consummatory_act"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 27
---

# SD-mech457_consummatory_act: environment.consummatory_act

**Claim ID:** mech457_consummatory_act (substrate node; not a claims.yaml claim)
**Subject:** environment.consummatory_act
**Status:** IMPLEMENTED
**Registered:** 2026-07-25
**Implemented:** 2026-07-25
**Depends on:** (none unresolved)
**Blocks:** H-consummation-binding (the last open retention leg of the `competence_floor` question, MECH-457); INV-088
**Design doc:** `evidence/planning/mech457_retention_portfolio_2026-07-18.md` (leg 4), `evidence/planning/competence_floor_reposing_2026-07-25.md`

## Problem

The `competence_floor` question (MECH-457) asks why an installed competent foraging policy is
not retained under continued RL. Three of its four retention legs resolved by 2026-07-25
(V3-EXQ-788 PASS distributional critic; V3-EXQ-792a PASS KL-anchor consolidation; V3-EXQ-789
FAIL/eliminated auxiliary-decay). The fourth, **H-consummation-binding**, is motivated by
V3-EXQ-781's load-bearing positive finding: an approach drive was *earned* at **0.707** while
raw-view foraging was *suppressed* to **0.200** from a **2.983** control, tight across all three
seeds -- **approach without consummation**. The hypothesis is that 781's drive-side null was
itself an artefact of a **missing consummatory act**: its terminal drive was
*non-extinguishing*, so there was no mechanism for an approach drive to terminate correctly on
arrival and hand off to a distinct act of consuming.

The substrate could not express this. In the base environment, consumption is **automatic on
cell entry**: the move branch of `CausalGridWorldV2.step()` bumps health/energy, restores the
homeostatic drive, and removes the resource the instant the agent steps onto its cell. There is
no way for contact to *afford* consumption without *effecting* it, and therefore no way for an
approach drive to extinguish on contact while consumption remains a separate, learnable action.
The **drive half** of the leg was already built -- extinction-on-contact is the default
(`per_axis_restoration_fraction = 1.0` drives the axis to 0) and the anti-extinction knobs
(`goal.py` `drive_ema_alpha`, `drive_floor`) are wired. Only the **consummatory act** was
missing.

## Solution

Add a distinct, no-move **CONSUME** action so that entering a resource cell **affords** rather
than **effects** consumption. Gated behind a single default-OFF flag; the OFF path is
byte-identical to the pre-change auto-consume-on-entry environment.

Module: `ree_core/environment/causal_grid_world.py`.

- **Config:** `CausalGridWorldV2(..., consummatory_act_enabled: bool = False)` -- a direct env
  constructor kwarg (not a `REEConfig` field; the env is built by the experiment driver). Class
  attribute `CONSUME_ACTION = 5`.
- **Action space:** the `action_dim` property returns `len(ACTIONS) + 1` (== 6) when enabled,
  else `len(ACTIONS)` (== 5, bit-identical). Actor heads size themselves from `env.action_dim`
  (e.g. `mech457_explorer_classes.py`), so enabling the flag grows every actor head 5 -> 6 with
  no further wiring. `CONSUME_ACTION` is **not** a member of `ACTIONS` / `_action_map`, so the
  world-rule-shift permutation can never turn it into a movement; `step()` dispatches it
  explicitly as a no-move (dx=dy=0).
- **Contact affords (ON):** moving onto a resource cell sets `transition_type =
  "resource_contact"`, delivers **zero** benefit reward, restores **no** homeostatic drive, and
  **retains** the resource in `self.resources` / `_resources_by_type` / `_resource_type_grid`.
  The `on_consumable_resource` info flag is set. On leaving an un-consumed resource cell the grid
  marker is restored to `resource` so the cell stays consistent with `self.resources` and a
  return visit re-affords.
- **Consummatory act (ON):** the CONSUME action, while the agent stands on a resource cell (tested
  against `self.resources`, robust to the "agent"-overwritten grid marker), effects consumption
  via the shared helper `_consume_resource_at(cx, cy)`: benefit reward, health/energy restore,
  per-axis drive restore, SD-049 typing / removal, respawn, proximity-field recompute. CONSUME
  off a resource is a clean no-op, indistinguishable from a stay.
- **Shared code path (anti-divergence):** the 118-line benefit / removal / drive-restore /
  respawn / field-recompute block was factored out of the legacy inline resource branch into
  `_consume_resource_at`, called by BOTH the legacy auto-consume-on-entry path (OFF) and the
  CONSUME action (ON). Consumption is therefore the **same operation** whichever way it is
  reached; only the **timing** differs. This is what keeps the leg a *binding* test and not a
  *consumption* change.

### Reward binding (the operational content)

The benefit reward is bound to the consummatory **act**, not to arrival: contact yields 0 reward;
CONSUME delivers it. This is the operational meaning of "affords rather than effects" and is what
lets an approach drive extinguish on contact while consuming remains a separate, learnable action.

> **CORRECTION (2026-07-25).** The original wording of this section, and the "drive half was
> already built" claim in the Problem section, asserted that extinction happens "via the
> already-wired `goal.py` drive machinery reacting to `resource_contact` /
> `on_consumable_resource`." That is **incorrect for the leg-4 experiment's path.** `goal.py`'s
> drive is the *homeostatic* per-axis system (`drive_ema_alpha` / `drive_floor` /
> `per_axis_restoration_fraction`); it is a different system from V3-EXQ-781's approach primitive,
> it does not reference `on_consumable_resource`, and it is not imported anywhere in the mech457
> bootstrap-explorer path (`GOAL_DIM = 2` there is spatial navigation, not a physiological drive).
> The env emits the `on_consumable_resource` affordance flag, but **nothing consumed it** -- 781's
> approach primitive reads `obs_dict`, which does not carry the flag. The drive-side consumer that
> the leg-4 treatment arm actually needs was built separately as
> **`sd_mech457_approach_extinction.md`** (IMPLEMENTED 2026-07-25): a default-OFF
> `approach_extinguishes_on_contact` knob that threads `info['on_consumable_resource']` into
> `train_a2c`'s approach block. This env node remains correct and unchanged; only the claim that
> the drive half was already wired is corrected here.

### Known minor limitation

The proprioceptive last-action one-hot in `body_state` (`body[5..8]`, 4 slots for actions 0-3)
already aliases the stay action (4) to slot 0 ("up"); the CONSUME action (5) aliases the same
way. Giving CONSUME a dedicated slot would change `body_obs_dim` and break every existing
experiment's `observation_dim`, so it is intentionally left aliased. The agent selects CONSUME
via a distinct policy-head logit (`action_dim` grew), which is what the leg needs; the
proprioceptive encoding of *which* no-move action was last taken is secondary to the DV.

## Blast radius

INVASIVE by design. Enabling the flag grows `action_dim` 5 -> 6, which re-keys every actor head
(`action_dim` on the actor) and **busts every cached arm fingerprint** for consummatory-ON
lineages -- reuse correctly refuses across the change. Pre-change lineages keep the 5-action
space and valid fingerprints because the flag defaults OFF. No running experiment is affected:
with the default (OFF) the environment, its observation dimension, and its consumption dynamics
are byte-identical to before this SD.

## Architecture Context

Leg 4 of the MECH-457 retention portfolio (`mech457_retention_portfolio_2026-07-18.md`). It
consumes the shared `mech457_retention_trajectory_probe` instrument (built 2026-07-19) -- the
DV is the **post-installation competence TRAJECTORY**, not a terminal readout (terminal-only
measurement is exactly what kept the retention deficit invisible for ten legs; V3-EXQ-780 is the
worked failure). It is orthogonal to the three other manipulation nodes
(`mech457_distributional_critic` = value estimator; `mech457_policy_kl_anchor` = update
constraint; `mech457_bc_aux_schedule` = auxiliary persistence): this node changes only the
**action space / consumption binding**, preserving the portfolio's anti-alias partition.

## What This SD Enables

`H-consummation-binding` becomes a `/queue-experiment` target: an approach drive gated to
EXTINGUISH on resource contact and hand off to a CONSUME act, versus V3-EXQ-781's
non-extinguishing terminal drive, adjudicated on the post-installation competence trajectory.
Prediction directions: competence still flat under the extinguish-and-hand-off arm => the binding
is **not** what 781 lacked (H eliminated); competence retained under the consummatory arm but not
the non-extinguishing control => 781's drive-side null was a consummatory-act artefact.

## MECH-094 / phased training

- **MECH-094:** N/A. This SD adds no simulation, replay, or non-waking memory write; no
  `hypothesis_tag` content is produced.
- **Phased training:** not required. This SD adds no encoder head trained on a latent signal; it
  is an action-space / environment-dynamics change.

## Validation

Substrate readiness is validated by `tests/contracts/test_mech457_consummatory_act.py` (7
contracts C1-C7): action_dim 5/6; OFF legacy auto-consume; ON contact-affords (retain, zero
reward, no restore); ON CONSUME effects consumption; CONSUME-off-resource == stay; un-consumed
departure restores the grid marker; and consumption is path-independent (OFF entry vs ON CONSUME
deliver identical reward/health restore -- shared `_consume_resource_at`). The consumption
refactor is regression-covered by the existing SD-049 / MECH-307 / SD-057 / SD-037 consumption
contracts (70 pass on the hub, ree-v3 base 120efac). The behavioural **H-consummation-binding**
experiment is a follow-up `/queue-experiment` target (not queued in the build pass).

## Related Claims

MECH-457 (candidate / v3_pending -- this node promotes/demotes/gates nothing), INV-088, and the
sibling nodes `mech457_distributional_critic`, `mech457_policy_kl_anchor`,
`mech457_bc_aux_schedule`, `mech457_retention_trajectory_probe`.
