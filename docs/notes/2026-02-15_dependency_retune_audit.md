# 2026-02-15 Dependency Retune Audit

**Scope:** `MECH-060`, `MECH-061`, `MECH-062`, `MECH-063`, `Q-015`, `Q-016`, `Q-017`, `IMPL-023`, `IMPL-025`

## Audit Method

1. Enumerate upstream `depends_on` edges for each scoped claim.
2. Enumerate downstream claims that directly depend on each scoped claim.
3. Compare claim headers vs registry status/depends-on alignment.
4. Patch only concrete mismatches or missing direct dependency expression needed for architectural clarity.

## Upstream/Downstream Trace (post-retune)

- `MECH-060`
  - Upstream: `ARC-003`, `ARC-005`, `ARC-015`, `INV-012`, `MECH-057`
  - Downstream: `MECH-061`, `IMPL-023`
- `MECH-061`
  - Upstream: `ARC-003`, `ARC-015`, `INV-012`, `MECH-060`
  - Downstream: `MECH-062`, `Q-015`, `IMPL-023`, `IMPL-025`
- `MECH-062`
  - Upstream: `ARC-003`, `ARC-005`, `MECH-061`
  - Downstream: `Q-016`, `IMPL-023`, `IMPL-025`
- `MECH-063`
  - Upstream: `ARC-005`, `MECH-039`, `MECH-040`, `MECH-055`
  - Downstream: `Q-017`, `IMPL-023`, `IMPL-025`
- `Q-015`
  - Upstream: `MECH-061`, `ARC-003`, `ARC-015`
  - Downstream: none
- `Q-016`
  - Upstream: `MECH-062`, `ARC-003`, `ARC-005`
  - Downstream: none
- `Q-017`
  - Upstream: `MECH-063`, `ARC-005`, `MECH-055`
  - Downstream: none
- `IMPL-023`
  - Upstream: `IMPL-008`, `IMPL-021`, `IMPL-022`, `MECH-057`, `MECH-058`, `MECH-059`, `MECH-060`, `MECH-061`, `MECH-062`, `MECH-063`
  - Downstream: `IMPL-024`, `IMPL-025`
- `IMPL-025`
  - Upstream: `IMPL-022`, `IMPL-023`, `MECH-061`, `MECH-062`, `MECH-063`
  - Downstream: none

## Findings and Actions

- Header/registry status mismatch found and fixed:
  - `MECH-061`, `MECH-062`, `MECH-063` headers now match registry status (`candidate`).
- Hook-surface dependency gap found and fixed:
  - `IMPL-025` now directly depends on `MECH-061/062/063`.
  - Hook-surface contract now explicitly specifies v2 bridge hook families tied to those claims.
- No additional dependency cycles introduced.

## Validation Snapshot

- total claims: 141
- missing dependencies: 0
- missing location/anchor: 0
- cycles: 0
