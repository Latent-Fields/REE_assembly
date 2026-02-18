# Conflict: Valence Vectors vs μ/κ Stability Overlays

## Conflicting Claim IDs

- Q-008
- MECH-035
- MECH-048
- MECH-055

## Verbatim Excerpts (with preserved sources)

From `docs/architecture/control_plane.md`:
> "Should REE retain a dedicated valence vector ... or can μ/κ stability overlays subsume the functional role of valence?"

From `docs/architecture/control_plane.md`:
> "REE should keep three affect-related control axes distinct."

## Why They Conflict (or What Would Reconcile Them)

Q-008 asks whether valence can be absorbed by μ/κ overlays, while MECH-055 currently requires separation between
hedonic stability overlays and valence appraisal. The conflict is whether that separation is architectural necessity
or temporary scaffolding pending better calibration evidence.

## Reconciliation Question

Is valence appraisal required as an independent axis for ranking and replay, or can a μ/κ-based regime model recover
those functions without loss of behavioral discrimination?

---

## Status

Resolved on 2026-02-18.

Resolution summary:
- Valence remains a dedicated affective appraisal stream.
- μ/κ overlays remain stability/commitment modulators and do not replace valence ranking semantics.
- Remaining work is calibration and orthogonality testing, not axis collapse.

Resolution note:
- `docs/conflicts/resolutions/2026-02-18_valence-vs-mu-kappa.md`
