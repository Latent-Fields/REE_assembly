---
title: "SD-MECH267-CEM-SELECTION-FIX: Mode-Content Wash-Out Fix"
parent: "Memory & Hippocampus"
grandparent: Architecture
nav_order: 12
---

# SD-MECH267-CEM-SELECTION-FIX: Mode-Content Wash-Out Fix

**Claim ID:** SD-MECH267-CEM-SELECTION-FIX
**Subject:** hippocampal.cem_mode_selection
**Status:** IMPLEMENTED
**Registered:** 2026-08-12
**Implemented:** 2026-08-14
**Depends on:** MECH-267 (mode_noise_scale), SD-MECH267-HORIZON-DEPTH, SD-055 (differentiable CEM) -- all IMPLEMENTED
**Blocks:** MECH-267 content-persistence retest (the C1 condition of V3-EXQ-869)

## Problem

MECH-267 gives the hippocampal CEM proposer two mode-conditioning facets --
`mode_noise_scale` (proposal breadth) and `mode_horizon_scale` (scoring-window depth).
V3-EXQ-869 / 869a / 923 (30 seeds each, confirmed autopsies
`failure_autopsy_V3-EXQ-869_2026-08-02` and `failure_autopsy_V3-EXQ-923_2026-08-12`)
established that mode-conditioned proposal **content is present at
`num_cem_iterations=1`** (C0 manipulation check PASS, mean pairwise `raw_std` mode gap
0.031-0.092) but **washes out to a mode-independent optimum by production
`num_cem_iterations=3`** (C1 FAIL: gap ~1e-5 to ~6e-6, 0/30 seeds show the predicted
mode ordering, vs FLOOR_PRODUCTION = 0.01). Neither facet, alone or together (869a),
survives the iterative refit.

**Mechanism (confirmed in `ree_core/hippocampal/module.py`):** `mode_noise_scale`
multiplies `ao_std` exactly **once**, seeding CEM iteration 0, before the loop. Each
iteration then (a) re-derives both `ao_mean` and `ao_std` purely from the selected
elites -- discarding the mode seed -- and (b) selects those elites with
`_score_trajectory`, whose ranking criterion (ARC-007 residue terrain + optional
wanting/curiosity) is **mode-independent**. So across iterations the distribution
converges to a mode-independent value optimum and the mode signal is gone.

Two remaining fix loci were named by the 923 autopsy and left **deliberately unscoped**
(a 2026-08-12 user decision): H2 (a mode-dependent value-function term) and H3
(partition/persist CEM pools per mode). On 2026-08-14 the user chose to **build both**
as independent flags and re-measure C1 at iters=3 for each.

## Solution

Two independent, deliberately-orthogonal fixes, each gated by the existing
`mode_conditioning_enabled` switch, each **no-op at its default** (existing experiments
bit-identical). Neither is wired through `REEConfig.from_dims`, mirroring the existing
mode facets -- experiments set them directly on `HippocampalConfig` (see
`experiments/v3_exq_462_mech267_rule_binding.py::_make_hippocampal`).

### H2 -- `mode_value_weight` (mode-dependent ranking term)

`HippocampalConfig.mode_value_weight: Dict[str, List[float]] = {}`. A per-mode weight
vector over the **world-state dimensions** (`z_world`, length `world_dim`).
`_score_trajectory` gains an optional `operating_mode` param; when mode conditioning is
on, `operating_mode` is supplied, and the map is non-empty:

```
w = sum_m operating_mode[m] * mode_value_weight[m]        # [world_dim]
terrain_score = terrain_score - dot(w, mean_z_world_along_trajectory)
```

Subtracted (lower score = better; same sign convention as `wanting_weight`). This keeps
the elite-selection **ranking** mode-differentiated on every refit iteration, so
mode-specific content is retained rather than averaged away.

**Why z_world, not the residue valence components:** the V3-EXQ-869/923 wash-out regime
constructs a **fresh** `ResidueField` whose valence head returns identically zero
(verified: `evaluate_valence` -> all-zero on random states, abs-max 0.0). A
valence-keyed term would be inert in the exact test. `z_world` is always non-trivial and
is the same space the terrain score already ranks over. The term is also active
**independently of** `wanting_weight`/`curiosity_weight` (both 0.0 in the wash-out
experiments), so it bites in the C1 condition.

### H3 -- `mode_partitioned_cem` (persistent mode breadth)

`HippocampalConfig.mode_partitioned_cem: bool` (landed 2026-08-14 default `False`; flipped
to production default `True` 2026-08-26, see "Production Default Landing" below). When
True (and mode conditioning enabled and `operating_mode` supplied), the mode-conditioned
noise scale is **re-applied
to the freshly-refit `ao_std` once per CEM iteration**, in both the legacy argsort-refit
and the SD-055 differentiable-refit branches, so each mode-conditioned proposal keeps its
own persistent breadth instead of converging to the mode-blind elite spread. Because
`ao_std` is recomputed from scratch from the elites each iteration, the re-scale applies
once per iteration and does **not** compound. For a single mode-conditioned proposer
call (the C1 measurement setup) this is equivalent to a per-mode candidate pool whose
elites never mix across modes.

### Diagnostics

`_last_mode_value_weight_active` (bool) and `_last_mode_partitioned_cem` (bool) on the
module record whether each facet engaged on the last proposer call; both False under
default config. Used as manipulation checks in the validation experiment.

## Architecture Context

The THIRD and FOURTH facets of MECH-267, alongside `mode_noise_scale` (2026-04-20) and
`mode_horizon_scale` / SD-MECH267-HORIZON-DEPTH (2026-08-02). Not a learning module: no
new `nn.Module`, no parameters, no phased training. MECH-094 N/A -- only the CEM ranking
criterion / proposal breadth for an already-computed rollout changes; no new
simulation/replay content is written to memory.

## What This SD Enables

Re-measurement of V3-EXQ-869's C1 condition (production `num_cem_iterations=3`) to test
whether a mode-dependent value term (H2) and/or persistent mode breadth (H3) keeps the
mean pairwise `raw_std` mode gap above FLOOR_PRODUCTION = 0.01, which the noise-scale and
horizon-depth facets do not. Validation experiment: OFF control / H2-only / H3-only /
BOTH arms.

Smoke (untrained field, single seed, indicative only): H3 lifted the tight-vs-broad mode
`raw_std` gap from 2.1e-06 (OFF, washed-out control) to 0.0172 (ON), clearing the 0.01
floor; H2's `z_world`-keyed term shifts elite ranking (a scored trajectory moved
0.355 -> -0.268) but its `raw_std` effect is the open question the formal multi-seed
validation answers.

## Production Default Landing (2026-08-26)

V3-EXQ-927/928 (30 seeds) resolved the two no-op-default flags this doc introduced:

- **H2 (`mode_value_weight`) -- confirmed NULL** on the C1 wash-out target (paired
  +0.0015, t=+0.48). Left at its default `{}` (dormant, not retired -- a null on the C1
  metric is not evidence the z_world-keyed ranking term is inert everywhere, and the
  field still has its own contract coverage exercising it directly).
- **H3 (`mode_partitioned_cem`) -- rescues the extreme-pair contrast** (H3-OFF control
  +0.0167, t=+4.34, 24/30 seeds positive; OFF washed out as predicted, manipulation
  confirmed on 480/480 cells). Default **flipped False -> True** 2026-08-26
  (chip-20260825-mech267-cem-flip-default), so production runs now get the validated
  fix without needing to opt in. Still gated on `mode_conditioning_enabled` AND
  `operating_mode` being supplied -- bit-identical for every caller that does not
  already enable mode conditioning with an operating mode.

**Residual, not closed by this landing**: V3-EXQ-928's ORDERED four-mode gradient check
(`per_arm_all_adjacent_gaps_clear_floor`) is FALSE in all four arms -- adjacent gaps
+0.00729 / +0.00750 / -0.00116, the last INVERTED. Only the broad-minus-tight
extreme-pair contrast is rescued; the full ordered-gradient wash-out that motivated this
SD is not restored. `failure_record` on `SD-MECH267-CEM-SELECTION-FIX` in
`substrate_queue.json` carries this open item forward.

## Related Claims

MECH-267, SD-MECH267-HORIZON-DEPTH, SD-055, ARC-007;
`failure_autopsy_V3-EXQ-923_2026-08-12`, `failure_autopsy_V3-EXQ-869_2026-08-02`,
`failure_autopsy_927-928-mech267-cluster_2026-08-16`.
