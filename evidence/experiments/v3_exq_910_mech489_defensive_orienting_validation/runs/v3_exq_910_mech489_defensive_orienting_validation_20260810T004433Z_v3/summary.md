# V3-EXQ-910 -- MECH-489 (SD-099) Defensive-Orienting Validation

Seeds: [0, 1]. Arms: ['orienting_off', 'orienting_on'].

## Pass criterion (a): ground-truth event -> trigger alignment (ON arm)
- limb_damage_injected: n_events=76 alignment_rate=0.02631578947368421
- external_hazard_injected: n_events=65 alignment_rate=0.015384615384615385
- world_rule_shift_occurred: n_events=30 alignment_rate=0.0

## Pass criterion (b): behaviour-coupling vs 12b baseline
See interpretation.on_arm_coupling / interpretation.baseline_12b in the manifest.

## Outcome: FAIL
