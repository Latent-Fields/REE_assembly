# V3-EXQ-910b -- MECH-489 (SD-099) valence-gating retest, decision counted at the override tick

Seeds: [0, 1, 2]. Arms: ['orienting_off', 'orienting_on']. Scored arm: orienting_on (eval_episodes=48).

## Corrected readout (at the override tick, synchronously)
- n_override_ticks: 21
- decision_counts: {'approach': 19, 'withdraw': 2, 'resume': 0} (sum 21)
- fresh orienting ticks: 11025; latched: 56173

## Legacy per-env-step readout (the defect this run fixes), same run
- n_overrides_latched: 125
- decision_counts_latched_sum: 684
- realized inflation ratio (overrides): 5.9523809523809526
- realized inflation ratio (decisions): 32.57142857142857

## Structural negative control (orienting_off)
- n_override_ticks: 0 (must be 0 by construction)

## Interpretation label: orienting_valence_gating_non_degenerate
## Outcome: PASS
