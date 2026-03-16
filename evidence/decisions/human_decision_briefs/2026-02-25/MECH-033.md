# Human Decision Brief: MECH-033

Cycle: `2026-02-25`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: hippocampus / kernel chaining interface
- Architecture anchor: `docs/architecture/hippocampal_systems.md#mech-033`
- Upstream dependencies: `ARC-018`, `ARC-002`, `ARC-001`, `ARC-005`, `ARC-021`
- Downstream dependents: `ARC-021`, `MECH-069`, `MECH-070`, `MECH-081`

## How It Functions In The Architecture

- ## E2 Kernel → Hippocampal Rollout Interface (MECH-033)
- Claim Type: mechanism_hypothesis
- Scope: How E2 forward-prediction kernels seed hippocampal rollouts
- Depends On: ARC-018, ARC-002, ARC-001, ARC-005, ARC-021
- Status: candidate (demoted from provisional 2026-03-15 — see V3 pending note)

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Recommendation: `hold_pending_v3_substrate`
- Decision status: `pending_user`
- Why this lane is open: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Options:
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.

## Evidence Snapshot

- Latest decision state: status=`applied`, recommendation=`retain_ree`, timestamp=`2026-02-15T18:46:42.773429Z`.
- Recent decision history:
  - 2026-02-15T18:46:42.773429Z: status=`applied`, recommendation=`retain_ree`, decision_needed=Model adjudication outcome selection

## Human Decision Prompt

- Promotion/conflict lane decision to resolve now: Hold — V3 substrate required before meaningful evidence can be collected
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `docs/architecture/hippocampal_systems.md#mech-033`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
