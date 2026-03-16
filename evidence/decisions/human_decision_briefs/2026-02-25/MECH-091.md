# Human Decision Brief: MECH-091

Cycle: `2026-02-25`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: basal ganglia / salient event phase reset
- Architecture anchor: `docs/architecture/control_plane_heartbeat.md#mech-091`
- Upstream dependencies: `ARC-023`, `MECH-090`

## How It Functions In The Architecture

- ## Salient events phase-reset the E3 heartbeat clock (MECH-091)
- Claim Type: mechanism_hypothesis
- Subject: basal_ganglia.salient_event_phase_reset
- Status: candidate
- Claim ID: MECH-091

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Recommendation: `hold_pending_v3_substrate`
- Decision status: `pending_user`
- Why this lane is open: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Options:
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.

## Evidence Snapshot


## Human Decision Prompt

- Promotion/conflict lane decision to resolve now: Hold — V3 substrate required before meaningful evidence can be collected
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `docs/architecture/control_plane_heartbeat.md#mech-091`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
