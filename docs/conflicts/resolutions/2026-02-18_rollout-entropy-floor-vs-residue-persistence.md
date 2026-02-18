# Resolution: Rollout Entropy Floor vs Residue Persistence

## Conflict Reference(s)

- `docs/conflicts/rollout_entropy_floor_vs_residue_persistence.md`

## Resolution Decision

REE resolves this by update-locus separation. Minimum rollout-diversity controls are allowed only at pre-commit
sampling/replay policy and offline recovery scheduling. They cannot erase residue geometry, flatten post-commit harm
traces, or bypass harm gating. Residue persistence remains invariant; entropy-floor controls act as anti-collapse
guards for candidate generation rather than moral-reset mechanisms.

## Claims Affected (IDs)

- Q-011
- INV-006
- ARC-011
- MECH-056
- IMPL-017

## Superseded Claims

- None. Conflict resolved by placement and authority-boundary clarification; Q-011 is retained as a legacy question ID.

## Canonical Docs Updated (paths)

- `docs/architecture/hippocampal_systems.md`
- `docs/conflicts/rollout_entropy_floor_vs_residue_persistence.md`
- `docs/conflicts/README.md`
- `docs/claims/claims.yaml`
- `docs/claims/claim_index.md`

## Open Follow-Ups

- Continue empirical calibration of diversity-floor magnitude and trigger thresholds in experiment lanes without
  changing residue invariants.
