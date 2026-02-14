# Cross-Repo Contract Sync Policy

Purpose: keep producer repos aligned with `REE_assembly` Experiment Pack contracts and weekly handoff format.

## Scope

- Contract owner: `REE_assembly`
- Producer repos: `ree-v2`, `ree-experiments-lab`, `ree-v1-minimal`
- Contract artifacts:
  - `evidence/experiments/INTERFACE_CONTRACT.md`
  - `evidence/experiments/schemas/v1/manifest.schema.json`
  - `evidence/experiments/schemas/v1/metrics.schema.json`
  - `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`
- Weekly handoff format artifact:
  - `evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`

## Weekly Cadence (staggered)

- Monday: `ree-v2` qualification handoff
- Tuesday: `ree-experiments-lab` stress handoff
- Wednesday: `ree-v1-minimal` parity/backstop handoff
- Thursday: `REE_assembly` ingestion + governance cycle
- Friday: decision packet + next dispatches

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

## Weekly Handoff Contract (Producer Requirement)

Each producer repo must publish one weekly handoff report using:

- `evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`

Required handoff packet fields:

- producer metadata (`producer_repo`, `producer_commit`, `week_of_utc`, `generated_utc`)
- contract sync section (`ree_assembly_commit`, contract lock path/hash)
- CI gate status section (schema validation, deterministic seed replay, hook coverage where applicable, remote export/import where applicable)
- run-pack inventory table (`experiment_type`, `run_id`, `seed`, `status`, key metrics, `evidence_direction`, `execution_mode`, `compute_backend`, `runtime_minutes`, pack path)
- claim coverage summary and recurring failure signatures
- blockers/open issues for next cycle

## CI Requirement

Each producer CI must fail if either is true:

- emitted run packs violate required contract fields;
- local lock-file schema hashes differ from current vendored/expected contract schema files.
- required weekly handoff report is missing required template sections/columns.

No weekly handoff should be submitted while CI gate status is red.

## Change Procedure

1. Update contract docs/schemas in `REE_assembly`.
2. Update handoff template if reporting contract changed.
3. Update `docs/changelog.md` with contract change note.
4. Dispatch update prompts to producer repos.
5. Producers update emitter + CI + lock file + weekly handoff formatter.
6. Producers emit one sample run pack and validate.
7. Re-run REE_assembly ingestion to confirm no contract FAIL signatures.

## Drift Handling

- Ingestion-level drift is surfaced as FAIL signatures:
  - `contract:jepa_adapter_signals_missing`
  - `contract:jepa_adapter_signals_version`
  - `contract:jepa_adapter_signals_invalid`
- Drift is resolved by producer patch + lock file refresh, never by weakening ingestion checks.
