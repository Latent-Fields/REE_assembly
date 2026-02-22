# Weekly Dispatch - ree-v2

Generated: `2026-02-22T16:07:31.965256Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v2`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`
- Architecture epoch: `ree_hybrid_guardrails_v1`
- Epoch start (UTC): `2026-02-15T15:31:31Z`
- Epoch policy source: `evidence/planning/planning_criteria.v1.yaml`

## Proposals

| proposal_id | claim_id | priority | experiment_type | dispatch_mode | decision_deadline_utc | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXP-0016` | `ARC-018` | `high` | `claim_probe_arc_018` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for ARC-018 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0017` | `Q-007` | `high` | `claim_probe_q_007` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for Q-007 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0018` | `MECH-056` | `high` | `trajectory_integrity` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for MECH-056 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0019` | `MECH-033` | `high` | `claim_probe_mech_033` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for MECH-033 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0020` | `ARC-007` | `high` | `claim_probe_arc_007` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for ARC-007 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0021` | `MECH-059` | `high` | `jepa_uncertainty_channels` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for MECH-059 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0022` | `ARC-016` | `high` | `claim_probe_arc_016` | `targeted_probe` | `n/a` | Reduce uncertainty for ARC-016 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0023` | `MECH-025` | `high` | `claim_probe_mech_025` | `targeted_probe` | `n/a` | Reduce uncertainty for MECH-025 via targeted experiment runs. | At least 2 additional runs with distinct seeds.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v2`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0016` / `ARC-018` / `claim_probe_arc_018` (mode=discriminative_pair)
- `EXP-0017` / `Q-007` / `claim_probe_q_007` (mode=discriminative_pair)
- `EXP-0018` / `MECH-056` / `trajectory_integrity` (mode=discriminative_pair)
- `EXP-0019` / `MECH-033` / `claim_probe_mech_033` (mode=discriminative_pair)
- `EXP-0020` / `ARC-007` / `claim_probe_arc_007` (mode=discriminative_pair)
- `EXP-0021` / `MECH-059` / `jepa_uncertainty_channels` (mode=discriminative_pair)
- `EXP-0022` / `ARC-016` / `claim_probe_arc_016` (mode=targeted_probe)
- `EXP-0023` / `MECH-025` / `claim_probe_mech_025` (mode=targeted_probe)

Contract to follow exactly:
- `evidence/experiments/INTERFACE_CONTRACT.md`

Epoch tagging requirements:
- Stamp every new run `manifest.json` with `"architecture_epoch": "ree_hybrid_guardrails_v1"`.
- Keep `timestamp_utc` aligned with the current epoch window (`>= 2026-02-15T15:31:31Z`).

Acceptance checks per proposal:
- Use discriminative pairs (primary vs explicit ablation/control), not broad profile sweeps.
- Use matched shared seeds across pair conditions and pre-register thresholds before execution.
- At least 2 additional runs with distinct seeds unless stricter pair checks are specified in proposal acceptance checks.
- Experiment Pack validates against v1 schema.
- Each emitted manifest includes `architecture_epoch=ree_hybrid_guardrails_v1`.
- Result links to claim_ids_tested and updates matrix direction counts.

Output required:
- concise run table: run_id, seed, status, key metrics, evidence_direction
- list of generated run pack paths
```
