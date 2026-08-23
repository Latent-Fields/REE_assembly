---
title: "SD-057: drive.object_bound_incentive_salience"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 15
status: candidate/v3_pending
status_asof: 2026-07-10
status_claim: SD-057
---

# SD-057: drive.object_bound_incentive_salience

**Claim ID:** SD-057
**Subject:** drive.object_bound_incentive_salience
**Status:** IMPLEMENTED 2026-06-04 (v1 = L2+L3+L4 core; phase-2 L6+L7 IMPLEMENTED 2026-06-04)
**Registered:** 2026-06-04
**Depends on:** SD-049 (multi-resource heterogeneity + per-type identity tag + per-axis drive), SD-015 (z_resource object-type encoder), SD-012 (homeostatic drive), MECH-306 (sustained-drive trace), MECH-230 (z_goal latent structure -- AMENDED by this SD)
**Blocks (substrate-readiness):** MECH-229 (wanting!=liking behavioural dissociation), MECH-117 (wanting/liking trajectory dissociation, non-degenerate retest), ARC-030 (approach-avoidance symmetry, goal-conditioned readout); goal_pipeline:GAP-7 L9 acceptance (514k currently 0.0)

GAP-7 plan-of-record node: `evidence/planning/goal_pipeline_plan.md`.
Source intake: `evidence/planning/thought_intake_2026-06-01_goal_wanting_liking_stream_repair.md` sections 8-9 (L0-L9 closure map).
Lit anchor: `evidence/planning/literature_synthesis_2026-06-01_object_bound_incentive_salience.md`.

## Problem

The goal stream commits a "mistaken abstraction" (intake section 2): `GoalState.update` (`ree-v3/ree_core/goal.py:148`) writes the agent's current world/resource latent into a SINGLE slow attractor on a scalar benefit gate:

```python
effective_benefit = benefit_exposure * z_goal_seeding_gain * (1 + drive_weight * drive_trace)
if effective_benefit > benefit_threshold:
    z_goal <- (1 - alpha_goal) * z_goal + alpha_goal * seed_latent   # seed = z_resource or z_world
```

`agent.update_z_goal` (`agent.py:4938`) chooses `seed_latent = z_resource` (SD-015 object-type latent) when available, else `z_world`. But z_goal is still ONE attractor, OVERWRITTEN on every contact by whatever type was last contacted. This conflates four things biology keeps separate (intake section 2; lit A1 Berridge/Robinson 1998):
- **liking** (hedonic impact at consumption) with **wanting** (incentive salience attributed to a cue/object);
- a **goal location** (where) with a **goal object/affordance** (what).

Consequence: the wanting target always equals the liking target. The L9 `wanting_liking_dissoc_fraction` is **0.0 on every arm and seed** (V3-EXQ-514l, `..._20260602T170106Z_v3`; intake section 4). The substrate has the endpoints (benefit pulse L0, z_goal L4, approach bridge MECH-295 L6) but is **missing the middle layer**: object-identity binding (L2) and a per-object incentive token (L3).

**Important reframe (failure record, 2026-06-03 autopsy of V3-EXQ-632 / 514l):** the 0.0 dissociation is currently CONFOUNDED by a foraging-competence ceiling (GAP-2): ~0.2% contact rate (23 contacts / 818 samples), so there is almost no reward-contact history to express a dissociation in. EXQ-632 seed-42 (the one foraging seed) was a CLEAN positive (z_goal_norm=3.0115 at contact, persists to t50, 0.0 under ablation). So single-object formation WORKS when contact happens. L2-L3 is the genuinely-missing middle layer, but its **behavioural** L9 validation is gated on GAP-2 supplying reliable contact. This SD's own validation is therefore a forced-contact MECHANISM diagnostic (decoupled from GAP-2, mirroring how V3-EXQ-626b decoupled the L1 positive control from GAP-2).

## Solution

Insert a per-object incentive layer between the benefit pulse and z_goal:

```
benefit pulse + resource_type_at_agent (k) + per_axis_drive   [SD-049, exists]
   │
   ├─(L2 MECH-344 BIND-obj) on contact: bind benefit to type k →
   │      IncentiveTokenBank.update(k, benefit, z_resource_snapshot)
   ▼
IncentiveTokenBank  (L3 MECH-345 INCENT-token)   [NEW; stateful, NO trained params]
   per type k:  base_value[k]   (slow-decay EMA of received benefit; revaluable)
                z_object[k]      (stored z_resource identity embedding)
   wanting[k] = base_value[k] * (1 + kappa_weight * drive_axis[k])   ← multiplier relocated to recall
   │
   ├─(L4 MECH-346 GOALPTR; MECH-230 amend) k* = argmax_k wanting[k]
   │      z_goal seeded FROM z_object[k*]   (NOT raw z_world / last-contacted z_resource)
   ▼
E3 goal_proximity (e3_selector.py:461) → now object-discriminative (z_goal is object-bound)
```

### L2 -- MECH-344 (benefit -> object-identity binding)
On a contact, the benefit pulse is bound to the SD-049 per-type tag `k` (`resource_type_at_agent` / `sd049_consumed_type_tag_this_tick`, 1..n_resource_types) rather than written as a raw scalar gate. Concretely: `IncentiveTokenBank.update(k, benefit, z_object=z_resource)` writes into the type-`k` bank entry. This is the associative `object -> benefit` node (lit B1 Cardinal/Everitt 2002; the BLA-analog identity-binding node). v1 keys on the SD-049 tag (lit E3: minimal object-centric substrate already present); a learned affordance embedding is the upgrade path, not v1.

### L3 -- MECH-345 (per-object incentive token / wanting amplitude)
A per-type bank (dict keyed by tag). Each entry holds:
- `base_value[k]` -- a slowly-decaying, **revaluable** cached incentive value (lit A2 Robinson/Berridge 1993 persistence + object-directedness; lit B5 Balleine/Dickinson 1998 revaluation-sensitive, NOT write-once). Updated on contact by EMA toward received benefit; decays slowly between contacts.
- `z_object[k]` -- the stored z_resource identity embedding for that type.

**Wanting amplitude** for object `k` at recall = `base_value[k] * kappa(per_axis_drive[k])`, computed at cue/recall time -- the Zhang 2009 (lit A4) `V = r * kappa(drive)` mechanism, with the `(1 + drive_weight * drive_trace)` multiplier RELOCATED from the GoalState seeding gate onto the stored per-object value. Drive is **per-axis** (SD-049: hunger/thirst/curiosity), so wanting for food is amplified by hunger, water by thirst -- giving identity-matched, drive-specific wanting (specific PIT; lit B2 Corbit/Balleine 2005/2011).

### L4 -- MECH-346 (z_goal written from the token pointer; MECH-230 amend)
z_goal is written FROM the most-wanted object's stored embedding: `k* = argmax_k wanting[k]`; `seed_latent = z_object[k*]`. z_goal keeps its role as an E1 conditioning vector (lit E2 UVFA) and as the E3 goal_proximity target; only the SOURCE changes (lit E1 SF/SR what/where factorization; lit B3 Schoenbaum 2009 z_goal encodes outcome identity). MECH-230's seeding firing-gate semantics are UNCHANGED -- the benefit/drive event still gates whether z_goal updates; the bank only determines WHICH object's embedding is the seed.

**The dissociation falls out:** liking = benefit at the object being consumed now (k_contact); wanting = z_goal points at k* = argmax(base_value x per-axis-drive), which can be a DIFFERENT object (e.g. just ate food while thirsty -> z_goal points at water). So wanting_target != liking_target becomes structurally expressible for the first time.

### Phase-2 (L6 + L7) -- IMPLEMENTED 2026-06-04

Both no-op-default, bit-identical OFF, no trained parameters (no phased training).

- **L6 -- MECH-347 `incentive.cue_triggered_wanting`** (cue-recall path). A
  PERCEIVED cue/object type (NO benefit pulse) retrieves its incentive token and
  nudges z_goal toward that object's stored embedding BEFORE consumption --
  identity-matched (pulls toward THIS cue's object), drive-specific (amplitude =
  `base_value[k]*(1+kappa*per_axis_drive[k])`). New `GoalState.cue_pull(z_object,
  strength)` (a directional nudge with no benefit gate and NO token revaluation)
  + `agent.cue_recall_wanting(cue_type, drive_level, simulation_mode)`. The
  downstream E3 goal_proximity + MECH-295 approach bridge (unchanged) then raise
  pre-consummatory approach toward the cued object. Config (GoalConfig):
  `use_cue_recall` (False; requires use_incentive_token_bank), `cue_recall_gain`
  (0.05, separate from alpha_goal), `cue_recall_min_proximity` (0.0, auto-perception
  floor). Trigger: the substrate primitive `cue_recall_wanting` is callable
  directly (forced-cue diagnostic); the StepHarness auto-derives the
  strongest-perceived type from the SD-049 per-type proximity field views
  (`resource_field_view_<name>`) and fires it each step when use_cue_recall is set.
  Biology: Berridge 2009 cue-triggered wanting; Corbit/Balleine specific PIT;
  Schultz DA-transfer-to-cue. MECH-094: `simulation_mode=True` is a no-op (replay
  must not move z_goal via a cue).

- **L7 -- MECH-348 `incentive.dacc_object_discriminative_readout`** (consumer
  wiring). The 2026-06-04 audit found dACC z_goal-blind. Now that z_goal is
  object-bound (L4), dACC reads it: `DACCAdaptiveControl.forward` gains optional
  `candidate_goal_proximity [K]` -> bundle `goal_readout`; `DACCtoE3Adapter` adds
  `bias -= dacc_goal_readout_weight * goal_readout` (proximity-to-z_goal high ->
  favoured), independent of dacc_weight so a goal-conditioned consumer works even
  if the legacy dACC bias is off. Wired in `select_action` by passing the
  per-candidate goal_proximity (to the object-bound z_goal) into dACC. Config:
  REEConfig `use_mech_consume` (False; requires use_dacc) + `dacc_goal_readout_weight`
  (0.0; DACCConfig). Biology: Balleine & O'Doherty 2010 (approach_commit should be
  goal-conditioned). MECH-094: waking action selection only.

  - **L7 AMEND -- `arc005_dacc_adapter_goal_proximity_training` calibration fix
    (IGW-20260801-199, 2026-08-01).** V3-EXQ-848 (the first run to exercise L7's
    `candidate_summary_source="e2_world_forward"` fix from the same 2026-07-31
    diagnosis session) found `dacc_adapter`'s goal-readout response was still
    negligible relative to the other score_bias channels. Two separate, independent
    gaps, not one:
    (1) **wiring gap**: `dacc_goal_readout_weight` stays at its 0.0 default unless a
    caller sets it, and V3-EXQ-848's own driver never did -- so the goal-readout term
    contributed exactly 0.0 in that run, on top of whatever else was wrong.
    (2) **calibration gap, confirmed by direct instrumentation** (not by re-running
    the throwaway diagnosis-session probe, which was never committed and did not
    reproduce under the live driver's own settings): `GoalState.goal_proximity()` is
    bounded `[0,1]` by construction and is NOT floor-pinned near zero -- instrumenting
    `REEAgent.select_action` on V3-EXQ-848's exact per-cell config (seed=1, level=1.0,
    content=A) showed raw proximity values in the range 0.3-0.8 with genuine
    per-candidate-set spread of ~0.003-0.03. The spread is small relative to the
    nominal `[0,1]` range because `z_goal`'s operating norm (~0.08 in the probed cell;
    exactly 0.0, i.e. `goal_state.is_active()==False`, for the entire episode in at
    least one other cell -- reward never clears `benefit_threshold` there) is
    calibrated independently of, and typically much smaller than, the `[0.6, 1.5]`-ish
    operating norm of the `e2_world_forward` candidate summaries it is compared
    against -- so the MSE-sum distance is dominated by `||z_world||^2`, a units
    mismatch, not a broken or "untrained" consumer (`DACCtoE3Adapter` has no
    `nn.Parameter` anywhere -- there is nothing to train). The same
    `goal_state.goal_proximity(_candidate_world_summaries(...))` call already backs
    MECH-295's `compute_approach_cue_score_bias` (agent.py ~6794/6810), so this is a
    general property of the `e2_world_forward`-summary path, not dACC-specific.
    **Fix**: new `dacc_goal_readout_normalize` flag (`DACCConfig` / `REEConfig`,
    default `False`, no-op) rescales `candidate_goal_proximity` to the candidate
    set's own `[0,1]` range via min-max BEFORE the `dacc_goal_readout_weight`
    multiply (agent.py, immediately after the existing `goal_proximity()` call at the
    L7 site), so score_bias reflects the set's relative proximity spread -- what
    actually matters for influencing an argmin -- rather than its calibration-diluted
    absolute magnitude. A near-flat candidate set (max-min <= 1e-9) is left
    unrescaled rather than divided by ~zero. Bit-identical when the flag is off (the
    only default-changing action is a future validation experiment's driver setting
    both `dacc_goal_readout_weight` and this flag, mirroring V3-EXQ-637's
    `dacc_goal_readout_weight=0.5` precedent). No new validation experiment was
    queued as part of landing this substrate change (out of this session's scope);
    a successor to V3-EXQ-848 exercising both flags is recommended follow-on work.

- **MECH-436 `drive.wanting_drive_state_modulation`** (drive-coupling leg, split
  from MECH-229 on 2026-06-16 via `/claim-synthesis`). The finer claim that wanting
  is not only dissociable from liking (MECH-229 leg a, established by V3-EXQ-514o)
  but additionally **drive-state-modulated**: the most-wanted object tracks the
  currently-most-depleted drive axis (incentive-salience amplitude
  `~ base_value*(1+kappa*per_axis_drive)`, the L6 MECH-347 term) even when the
  liking/consummatory target does not. `candidate`, `epistemic_category:
  substrate_ceiling` -- the V3 P2 foraging env produces near-flat per-axis drive
  (spread ~0.006, far below the most_wanted argmax-moving regime), so the response is
  to ENRICH the V3 substrate via the SD-049-PHASE-2 differential-depletion /
  kappa-scaling env amend. This is a **V3** amend: SD-049 is `implementation_phase: v3`
  and already provides the per-axis homeostatic drive system, so the conditioning
  substrate is V3 and MECH-436 is **not** V4-blocked. The pre-registered V4-1
  multi-agent-ecology is a richer OPTIONAL home for the same differential-depletion
  pressure, not the blocker; MECH-436's dependency stops at the V3 env layer
  (differential depletion) and does NOT reach the V4 drive-arbitration policy
  (MECH-394/435) that sits above per-axis drive. Owning falsifier: V3-EXQ-514r
  (overshoot flips most_wanted => env/magnitude artifact => build the V3 amend, NOT a
  weakens; overshoot fails to flip => genuine weakens, no enrichment helps).
  Lit-grounded by `targeted_review_connectome_mech_347` (Berridge 2006 / Smith 2011 /
  DiFeliceantonio 2016 incentive salience). DO NOT build the substrate amend until
  514r resolves.

## Architecture Context

Sits between SD-012/MECH-306 (drive + sustained-drive trace -> benefit pulse, L0) and the existing E3 goal_proximity consumer (MECH-117/MECH-112 wanting term). Reuses the SD-049 per-type tag + per-axis drive and the SD-015 z_resource encoder unchanged. Closest existing per-item precedent is the SD-039 AnchorGoalPayload / MECH-292 ghost-goal bank (per-anchor z_goal snapshot), but that is an inactive-anchor retrospective store; the incentive token bank is a concurrent, drive-revaluable, per-OBJECT-TYPE store on the waking goal-seeding path.

Distinct from neighbours: MECH-186/187/188 are serotonergic MAINTENANCE of wanting tone, explicitly NOT the binding gap (lit D2). ACh/plasticity-window is out of scope (lit D3). PFC maintenance (MECH-116, L5) is present-but-untuned, not the gap.

## What This SD Enables

- The L9 wanting!=liking dissociation acceptance (`wanting_liking_dissoc_fraction`, currently 0.0) becomes structurally expressible -> unblocks MECH-229 non-degenerate retest, MECH-117 non-degenerate retest, ARC-030 goal-conditioned readout.
- Behavioural validation of L9 remains gated on GAP-2 (foraging contact); this SD validates the MECHANISM under a forced-contact diagnostic decoupled from GAP-2.

## Implementation (v1)

**Config (GoalConfig, all no-op defaults; bit-identical OFF):**
| Param | Type | Default | Purpose |
|---|---|---|---|
| `use_incentive_token_bank` | bool | False | master switch |
| `incentive_decay` | float | 0.005 | per-object base_value slow decay (matches decay_goal) |
| `incentive_value_alpha` | float | 0.1 | EMA rate for revaluation on contact |
| `incentive_drive_kappa_weight` | float | 2.0 | relocated drive_weight for value x kappa(drive) at recall |
| `incentive_use_per_axis_drive` | bool | True | drive-specific wanting (food<->hunger) vs scalar drive |

**New code:**
- `ree_core/goal.py`: `IncentiveTokenBank` class (dict keyed by type tag; `update(k, benefit, z_object)`, `decay()`, `wanting(per_axis_drive, scalar_drive)`, `most_wanted(...) -> (k*, z_object, amp)`, `is_empty()`, `reset()`, `state_dict()/load_state_dict()`). `GoalState` gains an optional `bank` member, instantiated when `use_incentive_token_bank`.
- `ree_core/agent.py` `update_z_goal`: gains optional `resource_type: Optional[int] = None` kwarg. When the bank is enabled AND `resource_type` is provided AND z_resource is available: `bank.update(resource_type, benefit_exposure, z_resource)`; then `seed_latent = bank.most_wanted(per_axis_drive)[1]` (the most-wanted object's embedding) instead of the raw single z_resource snapshot. The GoalState.update firing gate (benefit/drive threshold) is UNCHANGED.

**Backward compatibility:** with `use_incentive_token_bank=False` (default) OR `resource_type` not supplied, `update_z_goal` takes the legacy single-attractor path bit-identically. The bank is a stateful EMA dict -- **no trainable parameters**, so NO phased training is required for v1 (a learned-affordance-embedding upgrade WOULD need P0/P1/P2).

**MECH-094:** the bank updates only on WAKING contact (via `update_z_goal`, which experiment loops call on the waking stream). It writes no content during simulation/replay/sleep, so `hypothesis_tag` does not apply. Guardrail: if a future revision updates the bank during replay, the tag becomes required.

## Validation (honest about the GAP-2 gate)

The behavioural L9 acceptance (`wanting!=liking trajectory fraction >= 0.6`, identity-recovery probe > 0.6, per-axis-drive ANOVA p<0.01) is GATED on GAP-2 supplying foraging contact. The SD's own validation experiment is therefore a **forced-contact mechanism diagnostic** (mirroring V3-EXQ-626b's L1 decoupling): forced contacts on TWO resource types at OPPOSING drive states (e.g. sated-on-food + thirsty), bank ON vs OFF, measuring whether z_goal can point at a DIFFERENT object than the one just consumed (`wanting_target != liking_target > 0` with bank ON; `= 0` with bank OFF). Acceptance criteria from the failure record (goal_pipeline_plan.md): forced-seed formation, negative-control no-seed, OFF-parity, and a non-zero wanting!=liking event count under the bank. Full behavioural L9 stays behind GAP-2.

## Related Claims

MECH-344 (L2 BIND-obj), MECH-345 (L3 INCENT-token), MECH-346 (L4 GOALPTR; MECH-230 amend). Phase-2: MECH-347 (L6 cue-triggered wanting / cue-recall), MECH-348 (L7 dACC object-discriminative readout). Unblocks MECH-229, MECH-117, ARC-030. Reuses SD-049, SD-015, SD-012, MECH-306, MECH-295 (approach bridge, L6 downstream), dACC/SD-032b (L7 host). Neighbours not to conflate: MECH-186/187/188 (5-HT maintenance), MECH-116 (PFC maintenance), MECH-292/293 (ghost-goal bank, inactive-anchor store).

> **Cross-ref (ARC-080 object-representation umbrella, 2026-06-04).** The
> `IncentiveTokenBank` is **one of three per-item object stores** in the substrate,
> mapped under [ARC-080](arc_080_object_representation_primitive.md): this bank
> (keyed by resource **TYPE tag**), the SD-039 / MECH-292 / MECH-293 ghost-goal
> bank (keyed by spatial **ANCHOR** -- already distinguished above), and the dormant
> ARC-006 / MECH-045 object-file buffer (keyed by entity **TOKEN**;
> [entities_and_binding.md](entities_and_binding.md)). This SD's `z_object` is a
> detached `z_resource` clone -- a **type-level** identity, not a token-instance
> object-file; ARC-080 records that generalising it to a token-keyed object-file
> (which would let the same store serve permanence, tools, self, and other) is a
> V4 / late-V3 substrate step, NOT a V3-closure item. SD-057 stays resource-bound
> for V3.
