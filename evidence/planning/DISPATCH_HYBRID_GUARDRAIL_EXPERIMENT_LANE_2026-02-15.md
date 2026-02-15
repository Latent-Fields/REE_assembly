# Dispatch: Hybrid Guardrail Experiment Lane (2026-02-15)

Generated: `2026-02-15T15:32:00Z`

## Purpose

Execute the conflict-resolution experiment lane under the updated hybrid guardrail contract:
- uncommitted trajectory rehearsal remains pre-commit only,
- durable updates require commit-boundary attribution,
- guardrail metrics must gate acceptance.

## Target Proposals

### ree-v2
- `EXP-0004` / `ARC-018` / `claim_probe_arc_018`
- `EXP-0006` / `MECH-033` / `claim_probe_mech_033`
- `EXP-0029` / `Q-011` / `trajectory_integrity`

### ree-experiments-lab
- `EXP-0011` / `MECH-056` / `trajectory_integrity`
- `EXP-0013` / `MECH-058` / `jepa_anchor_ablation`
- `EXP-0014` / `MECH-059` / `jepa_uncertainty_channels`
- `EXP-0015` / `MECH-060` / `commit_dual_error_channels`
- `EXP-0034` / `Q-017` / `control_axis_ablation`

## Guardrail Contract (must pass)

- `ledger_edit_detected_count == 0`
- `domination_lock_in_events == 0`
- `explanation_policy_divergence_rate <= 0.05`
- pre/post-commit contamination checks stay within failure thresholds:
  - `mech060:precommit_channel_contamination`
  - `mech060:postcommit_channel_contamination`
  - `mech060:attribution_reliability_break`
  - `mech060:commitment_reversal_spike`

## Execution Prompt

```md
You are Codex operating in the target producer repo (`ree-v2` or `ree-experiments-lab`).

Goal: execute the listed proposals under the hybrid guardrail contract and emit Experiment Packs.

Required checks:
- At least 2 additional runs per proposal with distinct seeds.
- Contract-valid experiment artifacts.
- Guardrail metrics and contamination hooks reported explicitly.

After run completion:
1. Commit and push packs.
2. In `REE_assembly`, run:
   - `python3 evidence/planning/scripts/sync_weekly_handoffs.py --full-run --run-ingestion`
   - `python3 evidence/planning/scripts/run_governance_cycle.py`
```
