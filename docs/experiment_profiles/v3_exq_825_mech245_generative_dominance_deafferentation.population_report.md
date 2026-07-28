# Population Report: V3-EXQ-825 / MECH-245

This report lists fields that were absent, empty, or placeholder-valued in repository artifacts and therefore could not be populated directly from their preferred structured location. Sources: `REE_assembly/scripts/generate_experiment_profile.py`; `REE_assembly/templates/experiment_profile.md`.

## Required Fields

| Field | Value | Source |
|---|---|---|
| source_commit | `0130028a457f45bdfd7951968395336bbbbb3fb1` | generator Git-history fallback |
| result_commit | `4710a1a128df2118a3a6473860ba1f059490bd4a` | generator Git-history fallback |
| claim | `MECH-245` | claim registry |
| reproduction command | present | source script docstring |
| evidence_direction | `supports` | flat manifest |
| limitations | present | source script caveat sections |

## Missing Or Placeholder Fields

| Field | Repository status | Fallback used | Source |
|---|---|---|---|
| `flat_manifest.source_commit` | missing in manifest; populated from git history fallback | `0130028a457f45bdfd7951968395336bbbbb3fb1` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1` |
| `run_pack.manifest.source_repo.commit` | empty string in run pack; populated from git history fallback | `0130028a457f45bdfd7951968395336bbbbb3fb1` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| `flat_manifest.source_hash` | absent; SHA-256 and git blob IDs computed from repository files | `computed content hash` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1` |
| `flat_manifest.commit_sha` | absent; SHA-256 and git blob IDs computed from repository files | `computed content hash` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1` |
| `flat_manifest.code_hash` | absent; SHA-256 and git blob IDs computed from repository files | `computed content hash` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1` |
| `run_pack.manifest.environment.dynamics_hash` | recorded as unknown; no fallback located | `not populated` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| `run_pack.manifest.environment.reward_hash` | recorded as unknown; no fallback located | `not populated` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| `run_pack.manifest.environment.observation_hash` | recorded as unknown; no fallback located | `not populated` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| `run_pack.manifest.environment.config_hash` | recorded as unknown; no fallback located | `not populated` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| `run_pack.manifest.reproduction` | absent; command extracted from source script docstring | `/opt/local/bin/python3 experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
| `manifest.limitations` | absent as a structured field; documented caveats extracted from source script | ``ree-v3/experiments/v3_exq_825_mech245_generative_dominance_deafferentation.py:70-89`` | `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3.json:1`; `REE_assembly/evidence/experiments/v3_exq_825_mech245_generative_dominance_deafferentation/runs/v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3/manifest.json:1-49` |
