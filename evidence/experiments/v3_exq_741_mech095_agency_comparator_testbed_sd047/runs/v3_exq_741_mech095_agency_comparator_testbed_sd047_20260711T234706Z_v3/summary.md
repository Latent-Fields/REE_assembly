# V3-EXQ-741 -- MECH-095 Agency-Comparator VALID TEST-BED on SD-047

**Status:** FAIL
**Claims:** MECH-095
**Decision:** woo_spelke_route_substrate_conditional_v4_1
**evidence_direction:** weakens
**Seeds:** [42, 7, 123, 99]
**Sweep:** ARM_0 OFF / ARM_1 0.25x / ARM_2 1.0x / ARM_3 4.0x (key contrast ARM_0-vs-ARM_2)
**Valid arms (both guards):** ['ARM_0', 'ARM_1', 'ARM_2', 'ARM_3']  peak=ARM_0
**B_beats_A:** True (mean valid impr A=-0.114 B=+0.003)
**Baseline carries contact:** True

## Per-arm results

| arm | intensity | recall_base | recall_A | recall_B | impr_A | impr_B | n_self/world_min | n_no_contact_min | arm_valid |
|---|---|---|---|---|---|---|---|---|---|
| ARM_0 | 0.00 | 0.750 | 0.778 | 0.768 | +0.028 | +0.018 | 164/5 | 11 | YES |
| ARM_1 | 0.25 | 0.796 | 0.718 | 0.761 | -0.078 | -0.034 | 114/5 | 10 | YES |
| ARM_2 | 1.00 | 0.824 | 0.753 | 0.834 | -0.071 | +0.010 | 103/7 | 7 | YES |
| ARM_3 | 4.00 | 0.647 | 0.624 | 0.662 | -0.024 | +0.014 | 68/7 | 4 | YES |

## Interpretation

- **woo_spelke_route_substrate_conditional_v4_1**
- Read-out (B) vs gradient-label (A): B > A (read-out is the better functional translation).
- If FLAT/all-valid-no-improvement -> Woo/Spelke: route MECH-095 substrate_ceiling -> substrate_conditional (V4-1 multi-agent ecology).
