# Human Decision Brief: MECH-266

Cycle: `2026-04-29`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `provisional`
- Subject: salience / asymmetric mode hysteresis
- Architecture anchor: `evidence/planning/sd033_governance_plan.md`
- Upstream dependencies: `SD-032a          # SalienceCoordinator (the mode register whose hysteresis this augments)`, `MECH-259         # salience-network switch threshold (symmetric-threshold mechanism this extends)`, `SD-033           # governance cluster`

## How It Functions In The Architecture

- # SD-033 Governance Plan
- Registered: 2026-04-20
- Status: active
- Scope: translate the 2026-04-20 GAP MEMO + OCD thought set into claims, lit-pulls, and an EXQ test battery that together close the "governance layer inert" gap identified in the memo.

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Promotion review: provisional -> stable
- Recommendation: `promote_to_stable`
- Decision status: `pending_user`
- Why this lane is open: overall_conf=0.881, conflict_ratio=0, exp_entries=4, lit_entries=6; directions supports=9, weakens=0, mixed=1, unknown=0, conflict_ratio=0
- Options:
  - Promote now (clear canonical status, risk under-tested edge cases)
  - Hold pending stress-test replication (better stress confidence, slower closure)
  - Split claim scope before promotion (clearer boundaries, added doc work)

## Evidence Snapshot

- Latest decision state: status=`applied`, recommendation=`hold_pending_v3_substrate`, timestamp=`2026-04-25T15:42:09.107849Z`.
- Recent decision history:
  - 2026-04-25T15:42:09.107849Z: status=`applied`, recommendation=`hold_pending_v3_substrate`, decision_needed=Hold — V3 substrate required before meaningful evidence can be collected

## Human Decision Prompt

- Promotion/conflict lane decision to resolve now: Promotion review: provisional -> stable
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `evidence/planning/sd033_governance_plan.md`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
