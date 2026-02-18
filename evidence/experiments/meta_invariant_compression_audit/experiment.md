# Experiment: meta_invariant_compression_audit

## What it tests

- Whether the reduced meta-invariant layer (INV-019..INV-023) still covers all critical failure boundaries.
- Whether selection/rehearsal channels remain separated from irreversible durable write paths.
- Whether authority stratification, commit-token gating, heterogeneous trust axes, and offline recalibration remain
  simultaneously satisfied.

## Failure modes it detects

- `rehearsal_to_durable_write_bypass`
- `external_to_constraint_store_write`
- `commit_without_token_boundary`
- `precision_axis_scalar_collapse`
- `offline_recalibration_suppressed`

## Minimum metrics to emit

- `rehearsal_to_durable_write_bypass_count`
- `external_to_constraint_store_write_count`
- `commit_without_token_count`
- `precision_scalar_collapse_index`
- `offline_recalibration_skip_rate`
- `fatal_error_count`

## Design implications

<!-- AUTO-DESIGN-IMPLICATIONS:START -->
If INV-019..INV-023 pass while lower-level checks also pass, keep the compressed meta-layer as a review contract only.
If any compressed metric fails while lower-level checks pass, the compression mapping is incomplete and must be revised.
<!-- AUTO-DESIGN-IMPLICATIONS:END -->
