# Thoughts: E2 Kernel to Hippocampal Rollout Interface

Status: processed

Processed in:
- `docs/architecture/hippocampal_systems.md` (MECH-033)
- `docs/architecture/e2.md` (ARC-002)
- `docs/architecture/trajectory_selection.md` (IMPL-016)

---

Related claims: ARC-018, ARC-002, ARC-001, ARC-005, MECH-033

E2 should be framed as a **forward-prediction kernel** (short-horizon conditional transitions), not a trajectory
generator. Hippocampal systems chain those kernels into explicit multi-step rollouts, under E1 constraints and
control-plane rollout parameters (H, N, temperature).

## Possible affected components

- E2 forward-prediction interface (ARC-002)
- Hippocampal rollout generator (ARC-018)
- Trajectory selection implementation (IMPL-016)
