# SD-014: hippocampus.valence_vector_node_recording -- wanting/liking write-path decouple

**Claim ID:** SD-014
**Subject:** hippocampus.valence_vector_node_recording (VALENCE_WANTING write-path)
**Status:** IMPLEMENTED (incentive-sensitization decouple, 2026-08-07)
**Registered:** 2026-08-07
**Depends on:** ARC-036, SD-011, SD-012, MECH-030 (all IMPLEMENTED)
**Blocks:** SD-014 representational-separability retest (V3-EXQ-887 successor); EXP-0098 wanting/liking dissociation programme

## Problem

SD-014 requires each hippocampal map node to store a 4-component valence vector
`V = [w, l, h, s]` in which **wanting (w) and liking (l) are separately recoverable
scalars** -- grounded in the genuinely independent mesolimbic-dopamine (wanting) and
opioid/endocannabinoid (liking) pathways (Berridge & Robinson 1998; Smith, Berridge &
Aldridge 2011). A composite `w + l` or `max(w, l)` scalar would lose the
approach-despite-diminished-reward failure mode that is the empirical signature of the
split.

**V3-EXQ-887 (2026-08-04) delivered SD-014's first genuine experimental evidence: a
confirmed, non-degenerate, root-caused FAIL.** The wall-independent instrument measured
`|Spearman(wanting, liking)| = 0.93-0.97` across all three seeds (C2 requires `<= 0.90`),
and `C1` functional drive-gating tau `0.867-0.889` (requires `<= 0.85`). The autopsy
(`failure_autopsy_2026-08-05_pending_review_batch.md` #3) read the root cause from source:

- `ree_core/agent.py::update_liking()` writes **VALENCE_LIKING** from raw
  `benefit_exposure` (threshold-gated at `liking_threshold`).
- `ree_core/agent.py::update_benefit_salience()` writes **VALENCE_WANTING** from
  `serotonin.benefit_salience(benefit_exposure) = tonic_5ht * benefit_exposure` -- a
  smoothed/EMA-calibrated transform of the **same** `benefit_exposure` input.

Both channels are therefore monotone functions of one shared signal. Rank collinearity is
near-guaranteed by construction: the `tonic_5ht` multiplier is slowly varying and does not
reliably re-order nodes relative to their liking. This is NOT the independent
dopamine/opioid architecture the claim is grounded in; it is one signal read through two
transforms. Registered eliminated `H-wanting-liking-separable-drive-gated` in
`evidence/planning/hypothesis_space_registry.v1.json`. /governance 2026-08-07 RATIFIED
"accept weakens; decouple the VALENCE_WANTING write-path".

## Solution

Introduce an **incentive-sensitization** mechanism on the VALENCE_WANTING write path so
wanting can diverge from raw hedonic magnitude over repeated exposure. Per Smith, Berridge
& Aldridge (2011): repeated mesolimbic dopamine activation progressively **sensitizes**
the incentive system so the same cue elicits more *wanting* -- **without** increasing
*liking*.

### Mechanism

A per-node, slowly-accumulating, saturating **sensitization gain** `g_i` is stored
alongside the valence vector. On each qualifying VALENCE_WANTING write at the nearest
active center `i`:

```
g_i  <-  min(sensitization_max, g_i + sensitization_rate * drive_level)      # BEFORE the write
w_i  +=  benefit_salience * (1 + sensitization_coupling * g_i)                # amplified write
```

`drive_level` is the homeostatic depletion signal `1 - energy` (SD-012), obtained by the
caller as `REEAgent.compute_drive_level(body_obs)`. Because `g_i` is driven by
`drive_level` -- a signal **orthogonal** to the node's benefit magnitude that
VALENCE_LIKING reads -- the stored wanting becomes a function of
`(hedonic magnitude) x (cumulative drive-coupled exposure history)`, while liking stays
`(hedonic magnitude)` only. Nodes visited often under high drive develop amplified wanting
relative to their hedonic magnitude (the SD-014 incentive-trap signature `w >> l`); nodes
with high hedonic contact but low drive-coupled exposure keep high liking and a low wanting
boost. The rank collinearity V3-EXQ-887 measured is broken along the drive axis.

This is exactly the dissociation the SD-014 claim notes already specify -- `w <- ... *
(1 + drive_weight * drive_level)`, "`l` updated by outcome, `w` updated by approach drive"
-- expressed as a **saturating learnable gain that grows over training** (the sensitization
phenomenon), rather than a fixed per-step drive multiplier.

### Modules affected

| File | Change |
|------|--------|
| `ree_core/utils/config.py` (`REEConfig`) | New no-op-default fields: `incentive_sensitization_enabled` (False), `sensitization_rate` (0.05), `sensitization_max` (4.0), `sensitization_coupling` (1.0); mirrored in `REEConfig.from_dims()`. |
| `ree_core/residue/field.py` (`RBFLayer`) | New buffer `sensitization_gain: [num_centers]` (zeros); new `update_sensitization_gain(center_idx, increment, gmax) -> float` (accumulate + saturate). |
| `ree_core/residue/field.py` (`ResidueField`) | Extract `_nearest_active_center(z_world)` helper (shared with `update_valence`); new `update_wanting_sensitized(z_world, salience, drive_level, rate, gmax, coupling)`. |
| `ree_core/agent.py` (`REEAgent.update_benefit_salience`) | New optional `drive_level=0.0` arg; routes the WANTING write through `update_wanting_sensitized()` when `incentive_sensitization_enabled`, else the legacy `update_valence(VALENCE_WANTING)` path unchanged. |

### Config params

| Param | Default (no-op) | Enable value | Purpose |
|-------|-----------------|--------------|---------|
| `incentive_sensitization_enabled` | `False` | `True` | master switch |
| `sensitization_rate` | `0.05` | -- | gain increment per unit drive per exposure |
| `sensitization_max` | `4.0` | -- | saturation ceiling on `g_i` |
| `sensitization_coupling` | `1.0` | -- | multiplier of `g_i` in the wanting amplification |

### Data flow

```
body_obs -> compute_drive_level (SD-012) ---------------------------+
benefit_exposure -> serotonin.benefit_salience -> salience --+      |
                                                             v      v
agent.update_benefit_salience(benefit_exposure, drive_level)
   if incentive_sensitization_enabled:
      ResidueField.update_wanting_sensitized
         -> RBFLayer.update_sensitization_gain (per-node g_i, saturating)
         -> RBFLayer.update_valence(VALENCE_WANTING, salience*(1+coupling*g_i))
   else:
      ResidueField.update_valence(VALENCE_WANTING, salience)   # legacy, unchanged
```

## Architecture Context

The valence store lives in `RBFLayer.valence_vecs` (`[num_centers, VALENCE_DIM]`, `field.py`),
written at the nearest active center by `ResidueField.update_valence` since SD-014's
original build (commit `9dba0d6d`); MECH-307 widened `VALENCE_DIM` 4 -> 6 (2026-05-11). The
sensitization gain is a parallel per-center buffer, so it inherits the same place-addressed
semantics. The VALENCE_LIKING write path (`update_liking`) and the VALENCE_HARM /
VALENCE_SURPRISE paths are **untouched** -- this change is confined to the VALENCE_WANTING
write. SD-012 (homeostatic drive) supplies `drive_level`; SD-011 (affective harm) and
MECH-030 (SWR replay) consume the resulting vector unchanged.

## Backward compatibility

Master switch defaults `False`: `update_benefit_salience()` is bit-identical to the prior
implementation, the `sensitization_gain` buffer stays zero and is never consulted, and the
new `drive_level` argument is ignored. The gain also stays inert if the feature is enabled
but the caller never supplies a non-zero `drive_level` (e.g. legacy drivers). Confirmed by
smoke test: OFF-path wanting write equals `benefit_salience` exactly, gain sum `0.0`.

## Phased training / MECH-094

- **Phased training: NOT required.** The sensitization gain is a non-gradient EMA-style
  accumulator (a registered buffer updated under `torch.no_grad()`), not an `nn.Module`
  head trained by backprop on latent targets. There is no encoder head to collapse under
  joint training, so the P0 -> P1 -> P2 protocol does not apply.
- **MECH-094: does not apply.** This is a WAKING write path. `update_wanting_sensitized`
  honours the same `hypothesis_tag` gate as `update_valence` (simulated/replay content is
  skipped), so no simulation/replay content updates real valence.

## What This SD Enables

- The SD-014 representational-separability retest: V3-EXQ-887's validated wall-independent
  instrument (C1 functional drive-gating tau `<= 0.85`, C2 `|Spearman(w,l)| <= 0.90`, C3
  replay-set Jaccard `<= 0.80`) re-run with `incentive_sensitization_enabled=True` and
  `drive_level` threaded into the wanting write. Queued as the successor experiment.
- The EXP-0098 wanting/liking dissociation programme, which the composite-scalar collapse
  would have made unmeasurable.

## Related Claims

- **ARC-036** -- the architectural parent (valence-vector node recording).
- **SD-011** (affective harm stream), **SD-012** (homeostatic drive), **MECH-030** (SWR
  replay) -- dependencies.
- **MECH-203** (tonic 5-HT benefit salience) -- supplies the `benefit_salience` base the
  sensitization amplifies.
- **MECH-124** (consolidation-mediated option contraction) -- SD-014's `w/h` early-warning
  signal, now measurable given a non-collinear store.

## References

- Berridge, K. C., & Robinson, T. E. (1998). What is the role of dopamine in reward:
  hedonic impact, reward learning, or incentive salience? *Brain Research Reviews.*
- Smith, K. S., Berridge, K. C., & Aldridge, J. W. (2011). Disentangling pleasure from
  incentive salience and learning signals in brain reward circuitry. *PNAS.*
- Mattar, M. G., & Daw, N. D. (2018). Prioritized memory access explains planning and
  hippocampal replay. *Nature Neuroscience.*
