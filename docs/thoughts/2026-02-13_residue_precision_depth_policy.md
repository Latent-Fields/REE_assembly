# Residue Precision by L-space Depth

Status: processed

## Thought

Residue pressure should be trajectory-first and depth-ordered. Sensory-space effects should remain reflexive
sampling/reorientation only (no semantic overwrite), while stronger residue effects land in action-consequence and
hippocampal rollout spaces. Slow regime/context shifts belong to consolidation timescales.

A related uncertainty remains: `z_delta` is under-specified and needs targeted literature evidence to define its
functional boundary relative to `z_theta`.

## Architectural Implications

- Formalize trajectory-first precision escalation as depth policy (`z_beta`/`z_theta` first, `z_gamma` bounded,
  `z_delta` tertiary).
- Encode anti-overwrite rule for sensory-space routing.
- Add explicit open question for `z_delta` function and evidence boundary.

Processed in:
- docs/architecture/residue_geometry.md
- docs/architecture/precision_control.md
- docs/architecture/l_space.md
- docs/claims/claims.yaml
- docs/architecture/interfaces.v1.yaml
- docs/claims/interface_ownership.v1.yaml
