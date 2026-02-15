# 2026-02-15 Sensory-to-Learning Loop Conformance Audit

## Scope

Conformance trace from sensory ingress to durable learning/update routing, cross-checked against:

- `ARC-017` sensory stream tags,
- `ARC-003` / `MECH-061` / `MECH-062` commitment boundary and gate family,
- `MECH-060` pre/post error split,
- `MECH-063` orthogonal control-axis telemetry,
- `IMPL-023` / `IMPL-025` hook-surface implementation contracts.

## Findings

1. **Resolved:** hook-tier mismatch for bridge families.
- Contract text required v2 bridge families for commit boundary, tri-loop arbitration, and control-axis telemetry.
- Registry previously exposed only v3-planned hooks for related surfaces.
- Fix applied by adding v2-required bridge hooks:
  - `HK-007` `commit_boundary_token_export`
  - `HK-008` `tri_loop_gate_trace_export`
  - `HK-009` `control_axis_telemetry_export`

2. **Resolved:** v2 spec did not enumerate bridge hooks in the v2-required section.
- Fix applied by adding explicit bridge coverage bullets in `Cross-Version Hooks Required in v2`.

## Residual Interface Gaps (flagged, not patched)

1. **Schema-level gap:** experiment-pack schemas do not yet include concrete payload schema sections for `HK-007/008/009` fields.
- Current contracts define hook key expectations, but there is no versioned JSON schema for these bridge payload envelopes.

2. **Semantic gap:** sensory tag provenance from `ARC-017` is not yet a required adapter-signal export surface.
- `jepa_adapter_signals.v1.json` validates latent/trace streams, but not explicit per-step tagged-stream presence/quality (`WORLD/HOMEOSTASIS/HARM/SELF_SENSORY`).

3. **Attribution continuity gap:** no explicit required metric currently checks commit-boundary-to-post-commit join success rate.
- Existing metrics include leakage and calibration proxies, but not a direct `commit_id` join completeness metric.

## Suggested Next Retune Targets

- Add a hook payload schema document for `HK-007/008/009` envelope keys.
- Extend adapter-signal schema with optional then required `stream_tag_quality` block in a versioned migration.
- Add metrics such as `commit_boundary_join_coverage_rate` and `tri_loop_trace_coverage_rate` to v2 readiness checks.
