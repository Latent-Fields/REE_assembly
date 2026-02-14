# Dispatch: REE-v2 Bootstrap First Prompt

Generated: `2026-02-14`  
Target repo: `ree-v2` (new repository bootstrap)

Use the following prompt as the first outbound initialization message in the new `ree-v2` thread.

````md
You are Codex operating in `ree-v2`.

Goal: bootstrap `ree-v2` as the REE qualification harness for substrate claims, with contract-compatible outputs for REE_assembly ingestion.

Lane policy:
- `ree-v2` = qualification lane (primary)
- `ree-experiments-lab` = stress/falsification lane (unchanged)
- `ree-v1-minimal` = temporary parity backstop during migration

Anchor claims and meanings:
- `MECH-058`: slow EMA target-anchor + fast predictor separation for stable substrate learning.
- `MECH-059`: explicit uncertainty/precision stream separation from generic prediction error.
- `MECH-060`: dual error channels pre-commit vs post-commit (planning/control vs attribution/learning).
- `MECH-056`: trajectory-first residue placement before representational distortion.
- `IMPL-022`: JEPA-based substrate contract for E1/E2 integration.

Contract sources in REE_assembly (treat as normative):
- `/Users/dgolden/Documents/GitHub/REE_assembly/docs/architecture/ree_v2_repo_bootstrap_spec.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/docs/architecture/jepa_e1e2_integration_contract.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/docs/architecture/hook_surface_contract.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/docs/architecture/hook_registry.v1.json`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/manifest.schema.json`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/metrics.schema.json`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`

## Required deliverables (exact)

1. Repository scaffolding:
- `contracts/schemas/v1/manifest.schema.json`
- `contracts/schemas/v1/metrics.schema.json`
- `contracts/schemas/v1/jepa_adapter_signals.v1.json`
- `contracts/hook_registry.v1.json`
- `contracts/ree_assembly_contract_lock.v1.json`
- `src/ree_v2/sensor_adapter/adapter.py`
- `src/ree_v2/latent_substrate/{encoder.py,target_anchor.py,predictor.py}`
- `src/ree_v2/signal_export/{adapter_signals.py,metrics_export.py}`
- `src/ree_v2/hooks/{registry.py,emitter.py}`
- `src/ree_v2/experiments/profiles.py`

2. Validation scripts:
- `scripts/validate_experiment_pack.py`
- `scripts/validate_hook_surfaces.py`
- `scripts/check_seed_determinism.py`

3. CI workflow:
- `.github/workflows/qualification-ci.yml` with required jobs:
  - schema validation
  - deterministic seed replay check
  - hook surface coverage check

4. Qualification profile config and run support for:
- `trajectory_integrity` (`MECH-056`)
- `jepa_anchor_ablation` (`MECH-058`)
- `jepa_uncertainty_channels` (`MECH-059`)
- `commit_dual_error_channels` (`MECH-060`)

5. One contract-compliant smoke run pack per profile under:
- `evidence/experiments/<experiment_type>/runs/<run_id>/`
with required files:
- `manifest.json`
- `metrics.json`
- `summary.md`
- `jepa_adapter_signals.v1.json` for JEPA-backed runs

## Required acceptance checks (must run and report)

1. Schema gate:
```bash
python3 scripts/validate_experiment_pack.py --runs-root evidence/experiments
```
Must pass with zero schema errors.

2. Deterministic replay gate:
```bash
python3 scripts/check_seed_determinism.py --profile all --max-abs-delta 1e-6
```
Must pass with no key drift and no metric deltas above tolerance.

3. Hook gate:
```bash
python3 scripts/validate_hook_surfaces.py --registry contracts/hook_registry.v1.json
```
Must verify `HK-001..HK-006` presence and `HK-101..HK-104` stubs.

4. Pack acceptance:
- Every smoke run pack includes `claim_ids_tested`, `evidence_class`, `evidence_direction`.
- Required metrics for each claim appear with stable snake_case keys.
- Failure signatures are emitted with the canonical IDs in the bootstrap spec when triggered.

## Output report (required)

Return:
1. A file checklist with PASS/FAIL per required deliverable.
2. Acceptance-check command outputs summarized as PASS/FAIL with key errors (if any).
3. A smoke-run table:
   - `experiment_type`
   - `run_id`
   - `seed`
   - `status`
   - key metrics
   - evidence direction
4. A short migration note describing parity status vs `ree-v1-minimal`.

Constraints:
- Keep scope focused on bootstrap surfaces only.
- Do not refactor unrelated architecture/design docs.
- Keep interfaces concrete and schema-stable (`v1` contracts).
````
