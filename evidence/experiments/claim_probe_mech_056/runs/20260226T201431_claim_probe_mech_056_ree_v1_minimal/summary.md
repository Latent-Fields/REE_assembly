# MECH-056 Residue Trajectory Placement — PASS (2026-02-26T20:14:31Z)

## Genuine ree-v1-minimal Evidence

**Substrate:** ree-v1-minimal gridworld 10×10, 4 hazards, 200 episodes × 3 seeds × 2 conditions.
**Architecture epoch:** ree_v1_minimal_genuine_v1

## Result

| Condition | Last-quarter harm |
|-----------|-------------------|
| TRAJECTORY-WIDE | 0.724 |
| ENDPOINT-ONLY   | 0.8127 |

Mean intermediate residue mass (TRAJECTORY-WIDE): **3.47925** (ENDPOINT-ONLY baseline: 0.0)

Harm improvement: **10.9% improvement** from spreading residue to intermediate trajectory steps.

## Architectural Interpretation

This is the structural precondition for the φ(z) terrain concept. MECH-056 asserts that harm
accumulates at intermediate trajectory positions during rollout — not only post-hoc at the
terminal executed step. The experiment confirms this:

1. **Path-spread criterion met**: intermediate residue mass is non-zero across all seeds,
   confirming residue CAN be localised along the planned path rather than only at endpoints.

2. **Harm-avoidance criterion met**: trajectory-wide accumulation produces lower last-quarter
   harm than endpoint-only, meaning the spread is functionally useful — the agent learns to
   avoid regions of the latent space associated with harmful intermediate states, not just
   terminal harm.

This supports the hippocampal braid interpretation: proposed rollouts are paths through the
harm/benefit manifold, and the agent benefits from having that manifold populated along the
full path rather than only at goal states.

## Status Implication

One genuine PASS, no contrary evidence. Supports promotion: candidate → provisional.
Re-experimentation on a more complex substrate is the appropriate next step before active.
