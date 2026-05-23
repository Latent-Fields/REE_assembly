# REE_assembly Active Governance Handoff

Generated: `2026-05-23T20:37:23.222226+00:00`  
Git HEAD: `c97272cf51027c61d24f12d59e29ac18b07520a7`  
Verification: **FAIL**

## Summary

10 experiments pending review; (5 PASS / 3 FAIL); 2 experiment(s) in flight; workset: 26 ready / 6 blocked

## Next Action

> Determine V3-EXQ-543k's fate: check per-machine runner_status files and coordinator panel. If manifest is on a remote machine, wait for sync. If the run was pruned or never ran, add an explicit disposition note in roadmap.md. Then re-queue if needed.

## Blocked Items (Verification Gate)

- **[EXQ_DRAINED_WITHOUT_MANIFEST_OR_DISPOSITION]** V3-EXQ-543k is mentioned as drained in the roadmap Status Snapshot but no manifest was found in evidence/experiments/. Roadmap context: 'V3-EXQ-543k drained this window -- the 2026-05-21T14:13Z force_rerun re-queue is no longer in the queue, but no fresh 54'
  - Action: Determine V3-EXQ-543k's fate: check per-machine runner_status files and coordinator panel. If manifest is on a remote machine, wait for sync. If the run was pruned or never ran, add an explicit disposition note in roadmap.md. Then re-queue if needed.

## Open Risks

- WARN [CENTRAL_RUNNER_STATUS_STALE]: evidence/experiments/runner_status.json last_updated 2026-05-21T14:26:59.490765+00:00 is 54.2h old (threshold: 12.0h). P
- WARN [HEARTBEAT_STATUS_DIVERGENCE]: Machine ree-cloud-1: heartbeat says state=running current_exq=V3-EXQ-591, but runner_status says idle=True current=null.
- BLOCK [EXQ_DRAINED_WITHOUT_MANIFEST_OR_DISPOSITION]: V3-EXQ-543k is mentioned as drained in the roadmap Status Snapshot but no manifest was found in evidence/experiments/. R

## In-Flight Experiments

- **V3-EXQ-591** on `ree-cloud-1` (47%) -- EXQ-ISEF-005: 4-phase infant curriculum vs flat parameter baselines (GAP-14)
- **V3-EXQ-590a** on `ree-cloud-3` (55%) -- EXQ-ISEF-004 rerun: novelty bonus Goldilocks calibration with checkpoint/resume

## Unresolved Failures (Pending Autopsy)

- `v3_exq_597b_mech258_pe_vs_raw_post_spcem_20260521T131756Z_v3` -- autopsy: pending
- `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T142648Z_v3` -- autopsy: pending
- `v3_exq_603_q045_mech313_mech260_four_arm_ablation_20260521T204222Z_v3` -- autopsy: pending

## Relevant Files

- `evidence/verification/governance_verification_latest.json`
- `evidence/experiments/pending_review.md`
- `docs/roadmap.md`
- `evidence/planning/inter_governance_workset.v1.json`
- `evidence/experiments/runner_heartbeats/`
- `evidence/experiments/runner_status/`