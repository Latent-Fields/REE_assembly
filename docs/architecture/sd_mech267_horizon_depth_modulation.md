---
title: "SD-MECH267-HORIZON-DEPTH: Mode-Conditioned Horizon-Depth Modulation"
parent: "Memory & Hippocampus"
grandparent: Architecture
nav_order: 14
status: implemented
status_asof: 2026-08-02
status_claim: MECH-267
---

# SD-MECH267-HORIZON-DEPTH: Mode-Conditioned Horizon-Depth Modulation

**Claim ID:** SD-MECH267-HORIZON-DEPTH
**Subject:** `hippocampal.mode_conditioned_horizon_depth`
**Status:** IMPLEMENTED 2026-08-02
**Registered:** 2026-08-02
**Depends on:** SD-004 (HippocampalModule), SD-032a (SalienceCoordinator / operating_mode),
MECH-267 (mode-conditioned noise-scale — the sibling mechanism this SD completes)
**Blocks:** MECH-267 content-persistence retest (V3-EXQ-869's C1 gate) with both
mechanisms active.

---

## Problem

MECH-267's own claim registration and 2026-04-20 `implementation_note` name **two**
mechanisms for mode-conditioned hippocampal trajectory proposals: a noise-scale
modulation (built 2026-04-20) and a horizon-depth modulation. Only the first was
built at the time; the second was explicitly deferred ("V4 reconsideration could
add explicit horizon modulation alongside the existing noise-scale mechanism"),
even though the *original* 2026-04-27 lit-pull recommendation was for horizon
modulation specifically (operating_mode should modulate look-ahead horizon at
proposal generation), with noise-scale adopted instead as "a different mechanism
with similar effect."

**Experimental evidence that the deferred mechanism is needed:** V3-EXQ-869
(2026-08-02, 30 seeds, pre-registered, confirmed failure autopsy
`REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-869_2026-08-02.json`,
USER-CONFIRMED) tested MECH-267 content persistence under production CEM
settings. C0 (manipulation check, `num_cem_iterations=1`) cleanly PASSED —
noise-scale conditioning is correctly wired and produces mode-differentiated
proposal content (gaps 0.031-0.092 vs 0.015 floor). C1 (production settings,
`num_cem_iterations=3`) FAILED — the effect washes out to noise (gaps -0.004 to
+0.004 vs 0.01 floor, 0/30 seeds show the predicted ordering). The autopsy's
mechanistic reading: CEM's iterative elite-refit converges toward a
mode-independent value optimum, and an initial-distribution-only perturbation
(noise-scale changes only the starting `ao_std`) cannot survive that many
refit iterations. This is consistent with noise-scale-only being structurally
insufficient, not with the underlying claim being biologically wrong — and it
directly motivates building the claim's own second, still-unbuilt mechanism.

**Biological grounding:** State/task-dependent scaling of look-ahead depth
during hippocampal replay and theta-sequence deliberation is independently
well-evidenced (Pfeiffer & Foster 2013; Olafsdottir et al. 2018; Mattar & Daw
2018; and directly, **Wikenheiser & Redish 2015**, which found deliberative /
vicarious-trial-and-error theta sequences extend further ahead than
fast-locomotion theta sequences during active task engagement — i.e. look-ahead
*depth*, not just proposal *breadth*, is state-dependent).

---

## Solution

### Why this is a scoring-window modulation, not a rollout-length change

`HippocampalModule.propose_trajectories` samples action-object sequences of
shape `[batch, config.horizon, action_object_dim]` from a distribution whose
mean is produced by `terrain_prior`, a fixed-width `nn.Linear(hidden_dim,
action_object_dim * horizon)` head. `config.horizon` is therefore a
**structural network dimension fixed at construction time**, not a runtime
knob — a per-mode change to the physical rollout length would require a
different network output width per mode, which is out of scope for a
backward-compatible, no-architecture-change SD (and was not what V3-EXQ-869's
finding calls for).

What CEM elite-refit actually optimises against is the **score** used to rank
candidates each iteration (`HippocampalModule._score_trajectory`, ARC-007
strict terrain-only evaluation over the rolled-out `world_states` sequence).
This SD modulates *how many of the already-rolled-out steps count toward that
score* — the **look-ahead depth used for candidate evaluation** — per
operating mode. A mode with a short evaluation window is myopic: it selects
candidates that look good over the near term only. A mode with the full
window evaluates candidates over the entire available horizon. This is the
"horizon depth" the claim's own text and the lit-pull describe, implemented
without touching rollout mechanics or network shape — matching the additive,
scalar-multiplier style of the sibling `mode_noise_scale` mechanism.

Because the window can only ever be a **fraction of the fixed structural
horizon** (never longer than `config.horizon`), "longer" for
`internal_planning`/`offline_consolidation` means the *full* available
horizon (fraction 1.0 — the deepest look-ahead the network can express),
while "shallower" for `external_task` means a smaller fraction.

### Config changes

`HippocampalConfig` (`ree_core/utils/config.py`), companion field to the
existing `mode_noise_scale`:

```python
mode_horizon_scale: Dict[str, float] = field(default_factory=lambda: {
    "external_task":         0.5,
    "internal_planning":     1.0,
    "internal_replay":       0.7,
    "offline_consolidation": 1.0,
})
```

Gated by the **same** `mode_conditioning_enabled` master switch as
`mode_noise_scale` — this is the second facet of one mechanism (MECH-267),
not a separate feature, so it shares the switch rather than adding config
sprawl. A mode present in `operating_mode` but absent from
`mode_horizon_scale` defaults to multiplier `1.0` (full horizon, no-op),
exactly mirroring `mode_noise_scale`'s missing-mode convention.

### Data flow

```
operating_mode (SD-032a SalienceCoordinator, dict[str, float])
    -> HippocampalModule._compute_mode_horizon_scale()
       (weighted average of config.mode_horizon_scale over operating_mode,
        same reduction as _compute_mode_noise_scale; None when
        mode_conditioning_enabled is False or operating_mode is None)
    -> effective_horizon = clamp(round(config.horizon * horizon_frac), 1, config.horizon)
    -> HippocampalModule._score_trajectory(trajectory, max_horizon=effective_horizon)
       (truncates world_states to the first max_horizon+1 states — initial
        state plus max_horizon steps — before the ARC-007 terrain-only score;
        None => full trajectory, current behaviour, unchanged)
    -> CEM elite selection ranks candidates by the mode-windowed score
    -> elite refit still targets the FULL H-step action-object sequence
       (only the ranking criterion is windowed, not the search space)
```

`_score_trajectory` gained an optional `max_horizon: Optional[int] = None`
parameter. All four pre-existing call sites (line-of-sight scoring diagnostics,
support-preserving elite selection, ghost-candidate scoring) call it with no
argument and are therefore bit-identical. Only the per-candidate CEM scoring
call inside `propose_trajectories`'s main loop passes `max_horizon`, and it
passes `None` whenever mode conditioning is disabled or `operating_mode` is
not supplied — so the truncation branch is never entered in that case.

### Backward compatibility

With `mode_conditioning_enabled` at its default (`False`), or when
`operating_mode` is not supplied to `propose_trajectories`, both
`_compute_mode_noise_scale` and `_compute_mode_horizon_scale` return `None`,
`effective_horizon` stays `None`, and `_score_trajectory` takes its original,
untruncated path. **Bit-identical to pre-SD behaviour.** Existing experiments
using MECH-267's noise-scale mechanism (V3-EXQ-462, 465, 869) with
`mode_conditioning_enabled=True` but no `mode_horizon_scale` override will
newly also apply the default horizon fractions above — this is an intended
behaviour change for consumers who already opted into mode conditioning, and
is exactly what V3-EXQ-869's C1 retest (Step 8 below) is designed to measure.

### MECH-094

No new simulation/replay content is written to memory by this SD — it only
changes which portion of an already-computed rollout contributes to CEM
elite-selection scoring. Not subject to the `hypothesis_tag` requirement.

### Phased training

No new encoder head is added; `terrain_prior`'s output width is unchanged.
Phased training does not apply.

---

## What This SD Enables

- Completes MECH-267's own two-mechanism claim text (noise-scale + horizon-depth).
- Unblocks the MECH-267 content-persistence retest gated by
  `pending_retest_after_substrate: true` (claims.yaml, set 2026-08-02) — a
  same-question re-queue of V3-EXQ-869's C1 condition with both mechanisms
  active, to be queued separately via `/queue-experiment`.

## Related Claims

MECH-267 (parent claim), SD-032a (operating_mode source), MECH-261 (write-gate
registry, read-side analogue), MECH-092 (micro-quiescence replay, one of the
conditioned modes).
