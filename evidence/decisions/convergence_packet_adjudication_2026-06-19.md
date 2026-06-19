# Convergence Packet Adjudication Batch (June demand-driven)

- Date (UTC): `2026-06-19T18:58:28Z`
- Outcome: `accepted` for all three June demand-driven packets
- Scope: interface-level intake lineage only; candidate claims already registered
  directly into `docs/claims/claims.yaml` (see Decision Basis)

## Packets

- `CPKT-RULE-DISTINGUISHABILITY-20260617` / `CRCT-RULE-DISTINGUISHABILITY-20260619` / source=`REE_convergence` (CDQ-001)
- `CPKT-TONIC-EXPLORATION-NOISE-20260618` / `CRCT-TONIC-EXPLORATION-NOISE-20260619` / source=`REE_convergence` (CDQ-002)
- `CPKT-QUALITY-DIVERSITY-20260618` / `CRCT-QUALITY-DIVERSITY-20260619` / source=`REE_convergence` (CDQ-003)

## Decision Basis

- All three packets are schema-valid and gate-ready
  (`validate_convergence_promotion_packet.py --check-gate-readiness`, 2026-06-19).
- These are the first convergence packets since the 2026-02-24 batch; this
  adjudication re-activates the `REE_convergence -> REE_assembly` handoff pipeline
  (`convergence_demand_pipeline:HANDOFF-REACTIVATE`).
- **Direct-registration supersedes the tool register step.** Under the June
  demand-driven model (`evidence/planning/convergence_demand_pipeline_plan.md`),
  the value-add Register step registers version-scoped candidate claims DIRECTLY
  into `docs/claims/claims.yaml`, wired into the target node's `depends_on` with an
  architecture-doc stub, rather than via an automated handoff register step. That
  registration already landed for all three rows:
  - CDQ-001: **MECH-437** (maintenance-side consolidation/refactor) + **MECH-438**
    (construction-side separable-key codebook), candidate/substrate_conditional/
    generation:v4, wired into the arc_062 cluster (landed master `dcca2cb`).
  - CDQ-002: **MECH-440** (state-conditioned self-annealing noise floor, NoisyNet
    analog extending MECH-313) + **MECH-441** (model-disagreement directed
    curiosity, RND/Plan2Explore analog extending MECH-314),
    candidate/substrate_ceiling/v3.
  - CDQ-003: **MECH-442** (behavioral-descriptor committed-selection archive,
    MAP-Elites analog on the E3 commit locus), candidate/substrate_conditional/
    generation:v3.
- Acceptance here records queue/handoff adjudication lineage ONLY. The receipt is
  the cross-repo acknowledgment artifact; it does NOT promote any claim and does
  NOT re-register or duplicate the claims above (the handoff tool copies packets
  and mirrors receipts; it never writes to `claims.yaml`). Decide-whether-to-build
  remains a later, normal governance step.

## Follow-up

- Receipts mirrored back to `REE_convergence/handoff/packets/receipts/` via
  `run_cross_repo_handoff.py --pull-receipts`.
- The candidate claims enter the normal promotion pipeline; none blocks the V3
  critical path (CDQ rows carry `blocks_v3_critical_path: false`).
- MED rows (CDQ-002/003) Mine/Register are complete; LOW rows CDQ-004 (blocked on
  V3-EXQ-625d) and CDQ-005 (MuZero adapter Register) remain open and out of scope
  for this batch.
