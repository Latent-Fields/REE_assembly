# Human Decision Brief: MECH-263

Cycle: `2026-04-29`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: pfc / ofc state space specific outcome
- Architecture anchor: `evidence/literature/targeted_review_pfc_subdivision_architecture/synthesis.md`
- Upstream dependencies: `SD-033b          # substrate this mechanism instantiates`, `MECH-261         # write-gate context for outcome/model updates`

## How It Functions In The Architecture

- # PFC Subdivision Architecture — Three-Prong Synthesis
- Literature pull scoping the PFC subdivision substrate that REE's claim graph currently references but does not properly register. Runs over three prongs: (A) lateral-PFC rule representation — load-bearing for MECH-261; (B) OFC vs vmPFC dissociation — resolving existing lumping in ARC-035 and MECH-151/152; (C) premotor/SMA sequence control and frontopolar branching — V3/V4 scoping.

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Recommendation: `hold_pending_v3_substrate`
- Decision status: `pending_user`
- Why this lane is open: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=8, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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
- Architecture anchor: `evidence/literature/targeted_review_pfc_subdivision_architecture/synthesis.md`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
