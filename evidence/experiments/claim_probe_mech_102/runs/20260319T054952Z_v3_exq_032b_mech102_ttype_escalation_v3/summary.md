# V3-EXQ-032b — MECH-102: Energy Escalation Ladder (ttype split, random policy)

**Status:** PASS
**Claims:** MECH-102, ARC-024, SD-003
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Policy:** RANDOM (avoids EMA-avoidance failure mode of EXQ-032)
**Split:** transition_type → none / hazard_approach / contact
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## Design Rationale

EXQ-032 used E3-guided (harm-minimizing) policy and split by harm_exposure EMA.
FAIL: the ethical policy was so effective that harm_exposure never exceeded 0.20
(n_high=0). No viability threat was measurable.

EXQ-032b replaces:
1. **Policy**: random → agent naturally enters all ttype states
2. **Split**: harm_exposure EMA → transition_type (directly reflects state-space energy)

The random policy is not less ethical — MECH-102 is about the *environment constraining
the option space*, not about unethical choices. With random policy, when the agent
happens to step into a hazard (agent_caused_hazard), that action had higher causal_sig
than alternatives (step away). The escalation ladder tests whether state-level energy
(ttype) predicts action-level consequentiality (causal_sig).

## Results — Energy Escalation Ladder

| State Energy Level | causal_sig | n steps |
|---|---|---|
| none (safe locomotion) | -0.031631 | 113 |
| hazard_approach (medium) | 0.005507 | 1136 |
| contact (high — agent+env) | 0.016950 | 71 |

- **world_forward R²**: 0.9481

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: causal_sig_contact > causal_sig_none (escalation from safe to contact) | PASS | 0.016950 vs -0.031631 |
| C2: causal_sig_approach > causal_sig_none (gradient precedes contact) | PASS | 0.005507 vs -0.031631 |
| C3: causal_sig_contact > 0.001 (positive signal at contact) | PASS | 0.016950 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9481 |
| C5: n_contact >= 50 | PASS | 71 |

Criteria met: 5/5 → **PASS**
