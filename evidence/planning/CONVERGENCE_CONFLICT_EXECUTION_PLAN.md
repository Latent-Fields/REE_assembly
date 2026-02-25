# Convergence Conflict-Driven Execution Plan

Date: 2026-02-23
Owner: ree-governance
Scope: non-JEPA intake probes in `REE_convergence` with direct relevance to active REE architecture pressure.

## Why This Order

This queue is ordered against the highest-pressure REE conflict signatures:

- `MECH-060`: `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break`, `mech060:commitment_reversal_spike`
- `MECH-058`: `mech058:anchor_separation_collapse`, `mech058:ema_drift_under_shift`
- `Q-017`: `q017:control_axis_stability_drop`, `q017:control_axis_entropy_collapse`, `q017:control_axis_policy_loss_spike`
- `MECH-057`, `Q-013`, `Q-014`: `ledger_editing`, `domination_lock_in`

Execution mode for this cycle: documentation-preflight run records only (no fabricated behavioral metrics).

## Execution Queue (Non-JEPA)

| Priority | Intake | Probe ID | Axis | Primary REE pressure targets | Signature focus |
|---|---|---|---|---|---|
| 1 | Active Inference | `ACTIVE-INF-P-001` | control-plane | `MECH-060`, `Q-017` | control-boundary contamination, separability drift |
| 2 | RAG | `RAG-P-002` | control-plane | `MECH-060`, `Q-017` | provenance gating before commitment, contamination under confidence noise |
| 3 | MuZero | `MUZERO-P-002` | prefrontal | `Q-017` (with follow-on to `MECH-060`) | search budget sensitivity, planning/execution boundary risk |
| 4 | RT-2 | `RT-2-P-003` | control-plane | `Q-017`, `MECH-060` | delay-tolerance control instability, action boundary failures |
| 5 | DreamerV3 | `DREAMER-V3-P-004` | control-plane | `Q-017`, `MECH-058` | control gain instability, horizon/normalization sensitivity |
| 6 | DreamDojo | `DREAMDOJO-P-004` | control-plane | `Q-017`, `MECH-060` | runtime control robustness, cross-axis contamination |
| 7 | DNC | `DNC-P-001` | memory | `MECH-057`, `Q-013`, `Q-014` | memory write/read pathway dependence and lock-in risk patterns |
| 8 | GNN planning | `GNN-PLAN-P-002` | E2 | `MECH-058`, `Q-017` | depth sensitivity and transition stability under perturbation |
| 9 | Multimodal agents | `MM-AGENT-P-002` | adapters | `MECH-060`, `MECH-057` | planner/executor adapter boundary ambiguity and control leakage |

## Round-Trip Intent

1. Execute ready non-JEPA probes in `REE_convergence`.
2. Build/validate promotion packets for non-JEPA intakes.
3. Handoff packets into `REE_assembly` inbox and mirror receipts/queue status.
4. Rebuild convergence intake queue and run governance cycle.

## Execution Result (2026-02-23)

Run records present for all non-JEPA ready probes:

- `sources/active-inference/artifacts/ACTIVE-INF-P-001/runs/ACTIVE-INF-P-001-RUN-001.md`
- `sources/rag/artifacts/RAG-P-002/runs/RAG-P-002-RUN-001.md`
- `sources/dreamdojo/artifacts/DREAMDOJO-P-004/runs/DREAMDOJO-P-004-RUN-001.md`
- `sources/muzero/artifacts/MUZERO-P-002/runs/MUZERO-P-002-RUN-001.md`
- `sources/rt-2/artifacts/RT-2-P-003/runs/RT-2-P-003-RUN-001.md`
- `sources/dreamer-v3/artifacts/DREAMER-V3-P-004/runs/DREAMER-V3-P-004-RUN-001.md`
- `sources/dnc/artifacts/DNC-P-001/runs/DNC-P-001-RUN-001.md`
- `sources/multimodal-agents/artifacts/MM-AGENT-P-002/runs/MM-AGENT-P-002-RUN-001.md`
- `sources/gnn-planning/artifacts/GNN-PLAN-P-002/runs/GNN-PLAN-P-002-RUN-001.md`

Cross-repo handoff summary:

- Non-JEPA packets pushed to `REE_assembly` inbox: 9
- Packet validation: 10/10 valid, 10/10 gate-ready (including existing JEPA packet)
- Queue state after governance cycle:
  - `convergence_total=10`
  - `convergence_ready=10`
  - `convergence_gate_failures=0`
  - `convergence_placeholder=0`

Remaining human step:

- Review/adjudicate convergence intake queue items and emit packet receipts for newly submitted non-JEPA packets.
