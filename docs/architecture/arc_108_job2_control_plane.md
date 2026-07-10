---
title: "ARC-108 JOB-2: the dopaminergic control-plane DRIVER pair"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 2
status: candidate
status_asof: 2026-07-10
status_claim: ARC-108
---

# ARC-108 JOB-2: the dopaminergic control-plane DRIVER pair

**Claim ID:** ARC-108 (the unified dopamine substrate; JOB-2 = the control-plane driver)
**Subject:** control_plane.dopaminergic_commit_maintain_decommit_driver
**Status:** IMPLEMENTED 2026-06-22 (V3-minimal slice; substrate -- PROMOTES NOTHING)
**Implementation phase:** v3 (user-ratified pull-forward 2026-06-22)
**Depends on:** ARC-108 JOB-1 step-1 (signed-RPE `delta_t = R_t - V-hat_t`, ree-v3 `ae907b5`);
the closure-exclusive de-commit eval substrate (`closure_exclusive_decommit_eval`, ree-v3 `e52158d`);
MECH-090 (beta-gate latch), MECH-342 (maintenance-release), SD-034 (closure operator), the
natural-commit latch-hold (`use_natural_commit_latch_hold`).
**Design-of-record:** `REE_assembly/evidence/planning/unified_dopamine_substrate_design_2026-06-22.md`
secs 3-6 / 10. **JOB-1 companion:** `docs/architecture/dopamine_into_gating.md`.

## Problem

REE built the commit/maintain/de-commit *machinery* -- the MECH-090 bistable beta-gate, the
natural-commit latch-hold, the SD-034 closure operator, the de-commit refractory -- and ran it off
hand-specified arithmetic readiness signals (`running_variance`, score margin, refractory timers).
The assembly-map A.6 biology check established the missing piece: in the brain **dopamine drives
all four phases of action commitment**, and REE never gave its control plane that neuromodulator.
Two specific deviations result:

- **Deviation B6 / the 460h monolithic hold.** Maintenance is a **flat** bistable hold: while a
  natural commit is armed the beta latch is re-asserted *unconditionally* each tick. A flat hold
  has no intrinsic decay term, so nothing stops it running ~2400 steps -- it monopolises, every
  other channel drowns.
- **The parked rung-6 de-commit non-dissociability.** The de-commit side (SD-034 closure +
  refractory timer) fires on a *clock*, not on outcome content, so it cannot be dissociated from
  the commit it releases -- exactly the property the rung-6 retests kept failing to produce by
  timer engineering.

In the brain neither is a tuned constant: maintenance is a **DA ramp scaled to goal-proximity x
value** that peaks-then-declines (Howe 2013; Mohebi 2019), so it *cannot* monopolise; de-commit is
**lateral-habenula -> RMTg -> DA-inhibition = a negative RPE** (Matsumoto 2007; Hong 2011; Sosa
2021), a *content-driven* "worse than expected" trigger.

## Solution -- the DRIVER pair (compose, don't replace)

The design-of-record decision (sec 4): **COMPOSE with the MECH-090/342/SD-034 machinery -- keep
the gate, closure operator, and refractory as the safety-bearing plumbing -- REPLACE only the flat
maintenance DRIVER and ADD the de-commit DRIVER.** The machinery still decides *whether* a hold or
release is permitted; dopamine decides *how strongly* and *when*, inside that envelope. No parallel
module (ARC-106 G2). Both pieces are no-op-default -> bit-identical OFF, waking-only (MECH-094).

### (c) `rho_t` maintenance ramp -- replaces the flat-hold maintenance driver

`ree_core/policy/rho_maintenance_ramp.py` (`RhoMaintenanceRamp`, pure-arithmetic, no params).

- **`rho_t = goal_proximity(z_world) x value`**, formed from quantities REE already has (no new
  substrate): `GoalState.goal_proximity` in [0,1] x the benefit valuation feeding F
  (`E3.benefit_eval_head`, clamped >= 0). Built by `REEAgent._compute_rho_t`.
- The ramp tracks a running proximity **peak** and **self-limits** -- returns release -- once
  `rho_t` has declined from the peak by `>= release_margin * peak` (or fallen below `hold_floor`),
  after an onset grace that lets it climb to the peak first.
- **Wiring (the targeted replacement):** at the natural-commit latch-hold re-assertion site in
  `REEAgent.select_action`, when `use_rho_maintenance_ramp` is on the *unconditional* re-assert is
  replaced by a ramp-gated one -- the ramp's self-limit is ADDED as a yield condition. **All the
  existing latch-hold yields are kept** (refractory active / MECH-091 threat interrupt / rung-6
  duration release / max-ticks = the safety plumbing). The ramp only decides *when the hold ends*.
- **Why this is the B6 fix and not a parameter tune:** a flat hold never crosses the decline test
  (it has no decline term), so it never self-limits -- the 460h monopoly. A proximity-scaled
  `rho_t` peaks at the goal and declines past it **by construction**, so the hold self-limits
  structurally. "Structural bounding works, parametric tuning does not" (assembly map C1).
- **Precondition (loud `ValueError`):** `use_rho_maintenance_ramp` requires
  `use_natural_commit_latch_hold` (the hold this ramp drives).

### (d) habenula negative-`delta_t` de-commit -- a new SD-034 abort input

`ree_core/governance/closure_operator.py` (`ClosureOperator.habenula_tick`).

- A negative phasic RPE -- the **same** signed `delta_t = R_t - V-hat_t` the ARC-108 JOB-1 slice
  computes in `e3_selector.post_action_update` (reused, not recomputed) -- is a new **internal
  scalar** abort input to the SD-034 closure operator. When `delta_t` is below
  `habenula_delta_threshold` ("worse than expected") AND beta is elevated, `habenula_tick` fires
  the **same 5-part `_fire`** the operator already runs (beta release + No-Go + residue discharge +
  salience + PE cap) and installs the de-commit refractory.
- **ADDED alongside** the existing rule-stability detector (`tick`) and the refractory-timer
  release -- the operator/refractory/No-Go machinery is NOT replaced. The abort is **content-driven**
  (fires on outcome valence, not the clock) and **dissociable** from the latch's own refractory
  state -- the exact property timer engineering could not produce.
- **Internal scalar only.** The routed GPi->habenula efferent drain stays V4.
- **`delta_t` reuse plumbing:** `post_action_update` computes `delta_t` + advances the shared
  `V-hat_t` whenever JOB-1 learned gating **or** `use_habenula_decommit` is on (broadened from the
  JOB-1-only gate; the JOB-1 path is bit-identical), and emits `habenula_delta_t`.
  `REEAgent.update_residue` routes it into `closure_operator.habenula_tick` and, on a fire, tears
  down the committed program (beta released, `_committed_trajectory=None`, hold disarmed).

## Config (REEConfig + from_dims; all no-op default, bit-identical OFF)

| Flag | Default | Purpose |
|---|---|---|
| `use_rho_maintenance_ramp` | `False` | master, ramp maintenance driver (requires the latch-hold) |
| `rho_hold_floor` | `0.05` | release when `rho_t` below floor |
| `rho_release_margin` | `0.5` | release when declined `>= margin * peak` past the proximity peak |
| `rho_onset_grace_ticks` | `3` | let the ramp rise to its peak before it can self-limit |
| `use_habenula_decommit` | `False` | master, negative-RPE de-commit (requires `use_closure_operator`) |
| `habenula_decommit_delta_threshold` | `0.0` | fire when `delta_t <` this (worse-than-expected) |

`use_habenula_decommit` is mirrored onto `E3Config.use_habenula_decommit` (so
`post_action_update`, which reads the E3Config, computes the signed RPE) and forwarded onto
`ClosureOperatorConfig.habenula_abort_enabled` / `habenula_delta_threshold` via the
`closure_decommit_hold_ticks` getattr-fallback build pattern.

## MECH-094 / ARC-106

- **MECH-094 (waking-only).** The ramp's `tick(simulation_mode=True)` never self-limits and does
  not advance the peak. `habenula_tick(hypothesis_tag=True)` is a no-op (a replay/DMN outcome must
  not abort a waking commitment); `delta_t` is computed only on the waking `update_residue` path.
- **ARC-106 (brain-like construction).** Grounding ladder: rho ramp = Howe 2013 / Mohebi 2019
  proximity-scaled DA ramp (peaks-then-declines -> cannot monopolise); habenula = Matsumoto 2007 /
  Hong 2011 / Sosa 2021 lateral-habenula negative-RPE. Load-bearing-vs-decorative: the proximity
  *decline* (not a fixed timeout) and the `delta_t` *sign* (not magnitude) are the load-bearing
  pieces -- a flat ramp / an unsigned signal collapses the mechanism. **No silent divergence:** the
  V3 slice renders D1/D2 as a single asymmetric gain (the opponent-population split is ARC-109, V4)
  and the habenula as an internal scalar (the routed efferent drain is V4); both are named V4 cuts.
  **Psychiatric failure mode:** a ramp that never declines -> perseverative monopoly (OCD-spectrum
  / the 460h monolith); a habenula that aborts on any noise -> avolition / learned-helplessness
  over-de-commit; absent habenula -> failure to disengage from a worsening commitment.

## Validation

`PROMOTES NOTHING.` ARC-108 stays `candidate` / `substrate_conditional` / `implementation_phase:
v3`. The substrate-readiness gate is the contract suite
(`tests/contracts/test_arc108_job2_control_plane.py`, C1-C8: bit-identical OFF, the ramp
peaks-then-declines self-limit where a flat hold monopolises, the habenula fires the SD-034 closure
on a negative `delta_t` and is dissociable from the refractory, `delta_t` reuse with JOB-1
unchanged, MECH-094 no-ops). The **sec-7.2 L0/L1/L2 control-plane falsifier** -- ramp-releases-where-
flat-latch-monopolises (D1), release content-driven not a re-parameterised timer (D2), habenula
de-commit dissociable (D3), on the `closure_exclusive_decommit_eval` substrate -- is a **separate
`/queue-experiment` chip**, sequenced after this build.

## See also

ARC-108 JOB-1 (`dopamine_into_gating.md`; the shared `delta_t`/`V-hat_t`), MECH-450 (the coupled
recurrent-settling step -- the maintenance ramp's selection-side twin, design sec 5), MECH-090 /
MECH-342 / SD-034 (the machinery this composes with), the natural-commit latch-hold + closure-
exclusive de-commit eval (`natural_commit_occupancy_release.md`; the substrate the ramp drives and
the falsifier runs on), ARC-109 (D1/D2 split, V4), ARC-106 (the grounding framework), MECH-439 (the
F-dominance front JOB-1 attacks at selection while JOB-2 attacks the duration/de-commit face).
