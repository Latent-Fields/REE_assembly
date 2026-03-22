# V3-EXQ-047c — SD-005: Latent Information Separation Probe

**Status:** FAIL
**Claim:** SD-005 — z_gamma split into z_self (motor-sensory) and z_world (environmental)
**Design:** Linear probes on frozen representations — action decodability vs event decodability
**alpha_world:** 0.9  |  **Warmup:** 400 eps  |  **Eval:** 50 eps  |  **Probe steps:** 200  |  **Seed:** 0

## Design Rationale

Prior tests (EXQ-047, 047b) measured downstream task performance (R², attribution_gap).
Both failed because the CausalGridWorld task is too easy — both split and unified reach R²>0.94.
This experiment instead probes information routing directly: does z_self carry more
action-correlated signal, and z_world more event-correlated signal, in the split condition?

## Probe Results

| Probe | Split | Unified | Δ |
|---|---|---|---|
| Action accuracy ← z_self | 0.190 | 0.190 | +0.000 |
| Action accuracy ← z_world | 0.226 | 0.226 | +0.000 |
| Event accuracy ← z_world | 0.831 | 0.831 | +0.000 |
| Event accuracy ← z_self | 0.826 | 0.826 | +0.000 |

Action dissociation (split): -0.036  (z_self − z_world for action)
Event dissociation (split): +0.005  (z_world − z_self for event)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: action_self > action_world + 0.10 (z_self more action-selective, split) | FAIL | 0.190 vs 0.226 |
| C2: event_world > event_self + 0.10 (z_world more event-selective, split) | FAIL | 0.831 vs 0.826 |
| C3: action_self_split > action_self_unified + 0.05 (split improves action routing) | FAIL | 0.190 vs 0.190 |
| C4: event_world_split > event_world_unified + 0.05 (split improves event routing) | FAIL | 0.831 vs 0.831 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: action_acc_self=0.190 not > action_acc_world=0.226 + 0.10 (z_self not more action-selective than z_world)
- C2 FAIL: event_acc_world=0.831 not > event_acc_self=0.826 + 0.10 (z_world not more event-selective than z_self)
- C3 FAIL: action_acc_self_split=0.190 not > action_acc_self_unified=0.190 + 0.05 (split not improving action-routing vs unified)
- C4 FAIL: event_acc_world_split=0.831 not > event_acc_world_unified=0.831 + 0.05 (split not improving event-routing vs unified)
