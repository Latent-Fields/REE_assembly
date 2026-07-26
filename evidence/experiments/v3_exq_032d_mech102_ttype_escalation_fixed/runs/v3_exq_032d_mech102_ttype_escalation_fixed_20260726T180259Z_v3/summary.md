# V3-EXQ-032d -- MECH-102: Energy Escalation Ladder (ttype split, random policy, CORRECTED)

**Status:** PASS
**Claims:** MECH-102, ARC-024, SD-003
**Supersedes:** V3-EXQ-032b (missing _e1_tick / record_transition calls -- both
E1/E2 losses were permanently zero-gradient stubs; see module docstring)
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Policy:** RANDOM (avoids EMA-avoidance failure mode of EXQ-032)
**Split:** transition_type -> none / hazard_approach / contact
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## Design Rationale

EXQ-032 used E3-guided (harm-minimizing) policy and split by harm_exposure EMA.
FAIL: the ethical policy was so effective that harm_exposure never exceeded 0.20
(n_high=0). No viability threat was measurable.

EXQ-032b replaced:
1. **Policy**: random -> agent naturally enters all ttype states
2. **Split**: harm_exposure EMA -> transition_type (directly reflects state-space energy)

but never called agent._e1_tick() / agent.record_transition(), so its E1/E2 training
buffers never reached the length-2 floor those losses require, and its PASS/supports
result reflected an untrained E1/E2/encoder stack. EXQ-032d adds exactly those two
calls (n_e1_ticks=6858, n_record_transitions=6358
this run) and changes nothing else.

## Results -- Energy Escalation Ladder

| State Energy Level | causal_sig | n steps |
|---|---|---|
| none (safe locomotion) | -0.046891 | 137 |
| hazard_approach (medium) | 0.006128 | 1155 |
| contact (high -- agent+env) | 0.002390 | 69 |

- **world_forward R2**: 0.9462

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: causal_sig_contact > causal_sig_none (escalation from safe to contact) | PASS | 0.002390 vs -0.046891 |
| C2: causal_sig_approach > causal_sig_none (gradient precedes contact) | PASS | 0.006128 vs -0.046891 |
| C3: causal_sig_contact > 0.001 (positive signal at contact) | PASS | 0.002390 |
| C4: world_forward_r2 > 0.05 | PASS | 0.9462 |
| C5: n_contact >= 50 | PASS | 69 |

Criteria met: 5/5 -> **PASS**

