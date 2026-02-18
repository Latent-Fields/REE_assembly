# Resolution: Valence Vectors vs Mu/Kappa Stability Overlays

## Conflict Reference(s)

- `docs/conflicts/valence_vectors_vs_mu_kappa_overlays.md`

## Resolution Decision

REE retains affective channel separation. Valence stays as a dedicated affective appraisal stream used for ranking and
replay biasing, while mu/kappa overlays remain commitment-stability and switching-pressure modulators. Mu/kappa does
not absorb valence semantics. The unresolved part is calibration and orthogonality testing, which remains tracked under
control-plane tuning questions rather than this structural separation conflict.

## Claims Affected (IDs)

- Q-008
- MECH-035
- MECH-048
- MECH-055
- IMPL-017

## Superseded Claims

- None. Conflict resolved by establishing canonical separation boundaries; Q-008 is retained as a legacy question ID.

## Canonical Docs Updated (paths)

- `docs/architecture/control_plane.md`
- `docs/conflicts/valence_vectors_vs_mu_kappa_overlays.md`
- `docs/conflicts/README.md`
- `docs/claims/claims.yaml`
- `docs/claims/claim_index.md`

## Open Follow-Ups

- Keep orthogonality/collapse-risk calibration under `Q-017` and associated control-axis ablation evidence.
