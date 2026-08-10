# V3-EXQ-910a -- MECH-489 (SD-099) Defensive-Orienting Decision Retest

Seeds: [0, 1]. Arms: ['orienting_off', 'orienting_on'].

## Pass criterion (a): ground-truth event -> trigger alignment (ON arm)
- limb_damage_injected: n_events=72 alignment_rate=0.0
- external_hazard_injected: n_events=58 alignment_rate=0.0
- world_rule_shift_occurred: n_events=29 alignment_rate=0.0

## Pass criterion (b): behaviour-coupling vs 12b baseline
See interpretation.on_arm_coupling / interpretation.baseline_12b in the manifest.

## Pass criterion (c) [NEW, decisive for this re-queue]: decision_alignment non-degenerate
See interpretation.decision_alignment in the manifest.

## Outcome: FAIL
