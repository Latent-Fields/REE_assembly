# SD-102: policy.epistemic_deficit_accumulator

**Claim ID:** SD-102
**Subject:** policy.epistemic_deficit_accumulator (MECH-482's own substrate)
**Status:** IMPLEMENTED
**Registered:** 2026-08-29
**Depends on:** MECH-314 (ARC-065 structured curiosity), MECH-314b (SD-063 E2WorldUncertaintyHead,
  ree-v3 `88287f11c6`), the ARC-065 GAP-A per-candidate slot (ree-v3 `c0e0ce8`, `per_candidate_learning_progress`
  parameter on `StructuredCuriosity.compute_score_bias`)
**Blocks:** MECH-483 (ORNT-3, orient/survey regime), Q-089 (ORNT-4, cold-start split), and (partially,
  alongside other unmet deps) ARC-121 / MECH-485 / MECH-487 / MECH-493

## Problem

MECH-314c (learning-progress curiosity) has had a `per_candidate_learning_progress` slot in
`StructuredCuriosity.compute_score_bias` since 2026-08-08 (ree-v3 `c0e0ce8`), but no live source to
fill it -- callers pass `None` and 314c stays the Phase-1 uniform `lp_ema` broadcast. The design doc
(`mech314bc_percandidate_extension_staged_2026-08-08.md` section 2) is explicit that manufacturing a
per-candidate 314c shape from data that does not carry genuine learning-progress information "would
recreate the exact 604a / 624a / 614d / 640a vacuous-channel failure class this codebase is scarred
by" -- the honest per-candidate 314c source is MECH-482 itself, whose own claims.yaml non-degeneracy
precondition is a **persistent, target-bound** (not per-tick-recomputed, not global-scalar)
uncertainty substrate.

Both prior gates on building MECH-482 are cleared as of 2026-08-23
(`orienting_epistemic_deficit_v3_plan.md` ORNT-2 node): the design doc received its owed user review
(2026-08-22), and the SD-063 `E2WorldUncertaintyHead` phased online training loop landed
(ree-v3 `88287f11c6`) with a corrected readiness discriminator
(`e2_world_uncertainty_last_pvar_relative_spread`, NOT the originally-proposed
`last_uncertainty_dev_range`, which an untrained head also passes). The residual 2x2
diversity/authority-rescale validation (V3-EXQ-949) ran PASS/supports on 2026-08-25. The 2026-08-27
work-graph debt classification pass (`work_graph_debt_classification_20260827.md` addendum v1.1,
user-directed routing) chips this build as `chip-20260827-mech482-accumulator-build`.

## Solution

### Why "target-bound" cannot be a per-tick recomputed vector

314a (novelty) and the 314b Phase-2 per-candidate path are both recomputed fresh every tick from the
CURRENT candidate pool -- there is no cross-tick memory. MECH-482's own claim text requires the
opposite: "an unresolved, consequential uncertainty accumulates across time steps even as raw novelty
and instantaneous prediction error fall to baseline" and "quenches ... rather than only reducing raw
uncertainty" on resolution. A per-tick-recomputed signal structurally cannot rise across ticks while
its own instantaneous inputs fall -- it has no persistence. The accumulator therefore needs genuine
cross-tick state, keyed by *where in z_world space* the deficit was observed (a "target"), not by the
CEM candidate index (which is a fresh, arbitrary K-slot identity every tick).

The precedent for exactly this shape already exists in the codebase: `ResidueField`'s RBF centers are
a persistent, spatially-indexed accumulator (value keyed by location, populated by realized events,
read out via nearest-center lookup at candidate-scoring time). `EpistemicDeficitAccumulator` reuses
that same two-phase shape (post-hoc UPDATE at a realized location; pre-hoc READOUT via nearest-target
match against the current candidate pool) rather than inventing a new persistence primitive, and
reuses `ResidueField`'s default RBF bandwidth (1.0) as the target-match-radius default so the two
spatial accumulators are calibrated to the same z_world scale.

### Candidate inputs (conservative subset, per claims.yaml MECH-482 notes and this chip's brief)

claims.yaml's MECH-482 note lists five candidate inputs; this landing implements the three the chip
brief scopes to, each already live in the agent with no new training infrastructure:

1. **Candidate-specific predictive uncertainty** -- `E2WorldUncertaintyHead.predictive_variance(z0, a)`
   (the same SD-063 head 314b's Phase-2 path reads), evaluated batch-of-1 on the REALIZED
   `(z_world_prev, action_taken)` pair at UPDATE time.
2. **Persistent prediction error** -- `||z_world_now - e2.world_forward(z_world_prev, action_taken)||`,
   the REALIZED point-forward error. Unlike the existing 314c `_lp_ema` (an EMA of the RATE OF CHANGE
   of a global PE scalar), this is the raw, spatially-local error magnitude at the specific target the
   accumulator is updating -- genuinely "persistent" because it keeps contributing to that target's
   deficit every time the target recurs, not just once.
3. **Predictive-system disagreement** -- `||e2.world_forward(z0, a) - head.forward(z0, a)[median]||`:
   the L2 distance between E2FastPredictor's point prediction (MSE-trained) and
   E2WorldUncertaintyHead's median quantile prediction (pinball-trained). These are two INDEPENDENTLY
   PARAMETERIZED predictive systems over the same `(z_world, action)` input (SD-063's own docstring:
   "shares NO parameters with E2WorldForward or the encoder") -- a genuine disagreement signal that
   needs no new ensemble-training infrastructure. (MECH-441's `ModelDisagreementEnsemble` was
   considered and REJECTED as the disagreement source: it is a separate, not-yet-built-by-default
   claim (`n_heads<=1` -> not instantiated) gated on its own blocked_substrate falsifier (ARC-110 /
   V3-EXQ-707), and using it here would inject an undeclared cross-claim dependency MECH-482's
   claims.yaml `depends_on` does not list.)

NOT implemented in this landing (explicitly out of scope, per the chip's narrowed candidate-input
list and the honest-scoping precedent set by the 314bc design doc): failed-replay-resolution and
competence-blocking-uncertainty inputs (both require memory/replay infrastructure this integration
point does not have visibility into), and the full `importance x uncertainty x expected_resolvability
x persistence` multiplicative formula from the claim's title (no `importance` or
`expected_resolvability` signal exists anywhere in the current substrate; manufacturing one would be
exactly the vacuous-channel risk the design doc warns against). **v1 scope is a persistence-weighted
ADDITIVE combination of the three available proxies; the multiplicative formula and the two
memory-coupled inputs are open follow-on, not silently dropped.**

### Data flow

```
UPDATE (post-hoc, once per waking tick, at the START of sense() -- mirrors
_train_e2_world_uncertainty's cadence and reuses its (z_world_prev, action_taken) cache):

  z_world_prev (cached from tick N-1) + action_taken (tick N-1's realized action)
      -> e2.world_forward(z0, a)              [point prediction]
      -> head.forward(z0, a) -> median quantile [independent prediction]
      -> head.predictive_variance(z0, a)        [uncertainty]
  z_world_now (tick N's observed latent)
      -> combine: deficit_input = w_u*uncertainty + w_d*disagreement + w_pe*persistent_pe
      -> EpistemicDeficitAccumulator.update(z_world_prev, deficit_input)
         -> nearest existing target within match_radius: EMA-update its deficit
         -> else: allocate a new target (evict lowest-deficit target if at capacity)

READOUT (pre-hoc, at candidate-scoring time, select_action()):

  candidate_world_summaries [K, world_dim] (this tick's K live candidates)
      -> EpistemicDeficitAccumulator.readout(...)
      -> per-candidate nearest-target lookup (read-only) -> [K] persistent deficit vector
      -> StructuredCuriosity.compute_score_bias(per_candidate_learning_progress=...)
      -> LatentState-external (curiosity is a policy-layer module, not a LatentState field;
         same integration site as 314a/b)
```

### Config changes (all no-op defaults; REEConfig, mirrors curiosity_* flat-field convention)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `curiosity_learning_progress_source` | Literal["broadcast","epistemic_deficit"] | "broadcast" | EXISTING field (reserved 2026-08-08); this landing fills the "epistemic_deficit" branch |
| `epistemic_deficit_max_targets` | int | 16 | bounded persistent-target capacity |
| `epistemic_deficit_match_radius` | float | 1.0 | "same target" L2 distance threshold in z_world space (matches ResidueField's default RBF bandwidth) |
| `epistemic_deficit_ema_alpha` | float | 0.1 | persistence/decay smoothing (matches `curiosity_lp_ema_alpha` convention) |
| `epistemic_deficit_uncertainty_weight` | float | 1.0 | UPDATE combination weight, candidate-specific uncertainty |
| `epistemic_deficit_disagreement_weight` | float | 1.0 | UPDATE combination weight, predictive-system disagreement |
| `epistemic_deficit_persistent_pe_weight` | float | 1.0 | UPDATE combination weight, persistent prediction error |

`curiosity_learning_progress_source` staying `"broadcast"` is bit-identical (no accumulator
instantiated at all -- mirrors `self.e2_world_uncertainty` and `self.curiosity`'s own None-when-off
pattern). All internal weights are O(1); final magnitude is still governed downstream by the EXISTING
`curiosity_learning_progress_weight` and the shared `curiosity_bias_scale` clamp -- this landing adds
no new clamp.

### Backward compatibility

With `curiosity_learning_progress_source="broadcast"` (default): `self.epistemic_deficit` stays
`None`, `_curiosity_per_candidate_learning_progress()` returns `None` immediately, `_update_epistemic_
deficit()` is a no-op (checks the same None), and `compute_score_bias`'s `per_candidate_learning_
progress` argument is `None` exactly as before this landing. Bit-identical.

### Readiness gate (binding)

Per this chip's brief and the corrected ARC-065 gate (`mech314bc_..._2026-08-08.md` section 5,
2026-08-23 correction): `_curiosity_per_candidate_learning_progress` REFUSES (returns `None` ->
Phase-1 broadcast fallback) unless the K-candidate batch read of
`head.predictive_variance(...)` yields `e2_world_uncertainty_last_pvar_relative_spread > 0` this
tick. A refusal calls `EpistemicDeficitAccumulator.mark_vacuous_readout()` (self-report, observable
via `get_state()["n_vacuous_readouts"]` / `last_readout_vacuous"`) rather than silently returning
zeros. The UPDATE path is NOT gated on this (it accumulates unconditionally on every waking tick,
mirroring `update_prediction_error`'s always-on cadence) -- an untrained head simply contributes a
near-uniform `deficit_input` that does not discriminate targets much, which is harmless bookkeeping;
it is only the READOUT fed to `compute_score_bias` that must refuse a vacuous channel.

### MECH-094

`EpistemicDeficitAccumulator.update()` takes a `simulation_mode` flag (no-op when True, mirrors
`StructuredCuriosity.update_prediction_error`); `_update_epistemic_deficit()` passes
`simulation_mode=bool(new_latent.hypothesis_tag)`, the same guard `_train_e2_world_uncertainty` uses.
`readout()` runs only from the waking `select_action()` call site (never invoked under
`simulation_mode=True`, same as `_curiosity_per_candidate_uncertainty`). No memory/replay write
surface -- MECH-094 hypothesis_tag on WRITTEN content does not apply (this is a waking online read/
accumulate, same posture as the SD-063 head itself).

### Phased training

Not applicable -- `EpistemicDeficitAccumulator` is pure arithmetic (no `nn.Module`, no learned
parameters), the same posture as `StructuredCuriosity` itself. It reads (never trains) the already
phased-trained SD-063 head.

### Episode lifecycle

`reset()` clears all persistent targets, called from the same per-episode reset path
`StructuredCuriosity.reset()` uses. This mirrors 314c's own per-episode LP-EMA reset ("a fresh task /
environment can have a fresh learning curve") -- MECH-482 is architecturally 314c's genuine source, so
it inherits the same episode-scoping convention. Whether the deficit should persist ACROSS episode
boundaries (a longer-timescale memory) is an open calibration question for a follow-on, not resolved
by this landing.

### ML/AI engineering notes

- **Failure mode defended against:** unbounded target growth. `max_targets` (default 16) with
  lowest-deficit eviction bounds memory; matches the finite-capacity-with-eviction pattern any
  online spatial-memory structure needs (the RND/Plan2Explore literature's own bounded-buffer
  discipline, cited already in MECH-441's docstring for the same reason).
- **Numerical consideration:** the guarded `mean > 1e-12` pattern from
  `E2WorldUncertaintyHead._last_pvar_relative_spread` is reused verbatim for reading
  `last_pvar_relative_spread` off `get_state()` (never re-derived) so there is exactly one place a
  divide-by-near-zero could occur, already guarded.
- **What NOT done:** no attempt to build a differentiable / learned target-matching function
  (e.g. a learned key-value memory). A simple nearest-neighbor L2 match against a bounded list is
  the same complexity class ResidueField already uses in this exact codebase at this exact
  world_dim scale (32-64), and importing a heavier mechanism would be the over-engineering Layer 7
  warns against for a 2-3-layer-MLP-scale substrate.

## Architecture Context

Sibling to MECH-314a/b (structured_curiosity.py) and MECH-441 (model_disagreement.py) under ARC-065.
Fills the `per_candidate_learning_progress` slot the 2026-08-08 GAP-A landing reserved. Does not
consolidate into `StructuredCuriosity` itself (kept as a separate persistent-state module, mirroring
the existing `ResidueField` / `StructuredCuriosity` separation of concerns: one owns spatial
persistence, the other owns score-bias composition) -- consistent with the "conservative path: extend
the existing curiosity stream rather than a separate DECISION module" instruction in claims.yaml
(this is a data-source extension feeding an EXISTING integration slot, not a new action-selection
pathway).

## What This SD Enables

Fills MECH-482's non-degeneracy precondition (target-bound, non-global-scalar, per-candidate/per-
region uncertainty substrate). Downstream: ORNT-3 (MECH-483 orient/survey regime) and ORNT-4 (Q-089
cold-start split) both name MECH-482 as their sole architectural prerequisite in the closure plan,
though each also has other unmet `depends_on` entries in claims.yaml (MECH-483 additionally needs
MECH-395/MECH-320/ARC-065-completion; Q-089 additionally needs MECH-457) -- this landing does not by
itself unblock either claim's `v3_pending` flag (see claims.yaml update in this landing's commit).

## Related Claims

MECH-482 (this SD's own claim), MECH-314/314a/314b/314c (parent + siblings), MECH-483/Q-089
(downstream), ARC-065 (parent architectural slot), SD-063 (the uncertainty-head keystone this landing
reads from).

## Validation experiment

Queued via `/queue-experiment` (diagnostic purpose) -- see the queue entry note for the EXQ id and
acceptance criteria (feature ON vs OFF, readiness-gated, non-vacuous-readout assertion).
