# Human Decision Brief: MECH-267

Cycle: `2026-04-29`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `provisional`
- Subject: hippocampal / mode conditioned proposals
- Architecture anchor: `evidence/planning/sd033_governance_plan.md`
- Upstream dependencies: `SD-004           # HippocampalModule (the substrate whose proposal function is modified)`, `SD-032a          # SalienceCoordinator (source of operating_mode signal)`, `MECH-261         # mode-conditioned write-gate registry (this mechanism is the read-side analogue)`, `MECH-092         # micro-quiescence replay (one mode whose proposals this specialises)`

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
- Why this lane is open: overall_conf=0.927, conflict_ratio=0, exp_entries=9, lit_entries=5; directions supports=13, weakens=0, mixed=1, unknown=0, conflict_ratio=0
- Options:
  - Promote now (clear canonical status, risk under-tested edge cases)
  - Hold pending stress-test replication (better stress confidence, slower closure)
  - Split claim scope before promotion (clearer boundaries, added doc work)

## Evidence Snapshot

- Latest decision state: status=`applied`, recommendation=`hold_pending_v3_substrate`, timestamp=`2026-04-25T15:42:09.107851Z`.
- Recent decision history:
  - 2026-04-25T15:42:09.107851Z: status=`applied`, recommendation=`hold_pending_v3_substrate`, decision_needed=Hold — V3 substrate required before meaningful evidence can be collected

## Human Decision Prompt

- Promotion/conflict lane decision to resolve now: Promotion review: provisional -> stable
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `evidence/planning/sd033_governance_plan.md`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
