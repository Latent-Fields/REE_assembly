# Cross-Repo Contract Sync Policy

Purpose: keep `ree-v1-minimal` and `ree-experiments-lab` aligned with REE_assembly Experiment Pack contracts.

## Scope

- Contract owner: `REE_assembly`
- Producer repos: `ree-v1-minimal`, `ree-experiments-lab`
- Contract artifacts:
  - `evidence/experiments/INTERFACE_CONTRACT.md`
  - `evidence/experiments/schemas/v1/manifest.schema.json`
  - `evidence/experiments/schemas/v1/metrics.schema.json`
  - `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`

## Version Rules

- `schema_version` constants are immutable once published.
- Additive optional fields may be introduced within the same major version.
- Any new required field or breaking semantic change requires a new schema major (`/v2` etc.).

## Sync Contract (Producer Requirement)

Each producer repo must keep a lock file:

- `contracts/ree_assembly_contract_lock.v1.json`

Required fields:

- `ree_assembly_repo`
- `ree_assembly_commit`
- `contract_version` (e.g. `experiment_pack/v1`)
- `schema_files` (path -> sha256)
- `last_synced_utc`

## CI Requirement

Each producer CI must fail if either is true:

- emitted run packs violate required contract fields;
- local lock-file schema hashes differ from current vendored/expected contract schema files.

## Change Procedure

1. Update contract docs/schemas in `REE_assembly`.
2. Update `docs/changelog.md` with contract change note.
3. Dispatch update prompts to producer repos.
4. Producers update emitter + CI + lock file.
5. Producers emit one sample run pack and validate.
6. Re-run REE_assembly ingestion to confirm no contract FAIL signatures.

## Drift Handling

- Ingestion-level drift is surfaced as FAIL signatures:
  - `contract:jepa_adapter_signals_missing`
  - `contract:jepa_adapter_signals_version`
  - `contract:jepa_adapter_signals_invalid`
- Drift is resolved by producer patch + lock file refresh, never by weakening ingestion checks.
