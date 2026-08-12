# V3-EXQ-921 -- MECH-490 Sleep Commit-Gate Persistence (V3-EXQ-913 successor)

**Status:** PASS (mechanical run-health verdict)
**MECH-490 evidence_direction:** non_contributory
**Purpose:** spawn-matched + commit-variance-instrumented sleep-vs-no-sleep ablation,
testing whether post-sleep action-sequence coherence gains (if real) covary with E3
commit-gate engagement, per MECH-490's confirming/falsifying signature.

- harm-pathway train steps (total, all seed/arm): 101906
- layout continuity confirmed (all seed/arm): True
- sleep cycles fired -- WITH_SLEEP arm: 14  NO_SLEEP arm: 0
- matched sleep-firing-vs-no-sleep-control comparisons obtained: 14 across 6 seeds
- spawn_match_rate: 0.786 (floor 0.8) -- non_degenerate=False
- commit_gate_instrumented: True
- sign-test p-values: mean_run_length=1.0  reversal_rate=0.14599609375  turning_entropy=1.0  tortuosity=0.79052734375
- commit-gate covariance (Pearson r, mean_run_length_delta vs commit_gate_engagement_rate_delta): -0.3726138820698475
- coherence_lift_significant: False   covaries_with_commit_gate: False
- eval steps (total): 135110  across 24 segments/(seed,arm) x up to 500 steps
- events: block=5306  freeze fires (motor-override relaxed): 0
- safe-spawn / continuity-spawn retries (total): 57  (segments exhausted: 0)

## Eval channel mean / max-std
- z_harm_s: mean=0.2440 max_std=0.13332 (varies)
- z_harm_un: mean=0.3775 max_std=0.12918 (varies)
- z_harm_a: mean=2.3969 max_std=3.25374 (varies)
- drive: mean=0.9184 max_std=0.25413 (varies)
- z_goal: mean=0.0082 max_std=0.04997 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.7735 max_std=0.05614 (varies)
- z_block: mean=0.0244 max_std=0.24756 (varies)
- excite: mean=245.9763 max_std=5173.19292 (varies)
- dread: mean=19.6900 max_std=286.14375 (varies)

## Sleep-vs-no-sleep matched comparisons (per seed)
- seedseed0: n_sleep_firings=2 fired_at_segments=[8, 18]
- seedseed1: n_sleep_firings=2 fired_at_segments=[4, 14]
- seedseed2: n_sleep_firings=2 fired_at_segments=[6, 16]
- seedseed3: n_sleep_firings=3 fired_at_segments=[3, 13, 23]
- seedseed4: n_sleep_firings=3 fired_at_segments=[1, 11, 21]
- seedseed5: n_sleep_firings=2 fired_at_segments=[4, 14]

## Lifetime affective occupancy (per seed/arm, non-gating, SENT-2 hygiene)
- seed0_with_sleep: frac_dread_above_p75=0.24997836059897863 frac_z_harm_a_above_p75=0.24997836059897863 frac_harm_event=0.08543235523240716 frac_in_reef=0.29879684930321126
- seed0_no_sleep: frac_dread_above_p75=0.25004623636027373 frac_z_harm_a_above_p75=0.25004623636027373 frac_harm_event=0.08831144812280377 frac_in_reef=0.3256889217680784
- seed1_with_sleep: frac_dread_above_p75=0.0 frac_z_harm_a_above_p75=0.24997773621871938 frac_harm_event=0.08210882536289964 frac_in_reef=0.18176151037492208
- seed1_no_sleep: frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.0425 frac_in_reef=0.20883333333333334
- seed2_with_sleep: frac_dread_above_p75=0.2499577488592192 frac_z_harm_a_above_p75=0.24843670779111035 frac_harm_event=0.04495521379077235 frac_in_reef=0.279956058813588
- seed2_no_sleep: frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.10836575875486382 frac_in_reef=0.23200389105058367
- seed3_with_sleep: frac_dread_above_p75=0.24941905499612704 frac_z_harm_a_above_p75=0.2500215164816249 frac_harm_event=0.059213357431792756 frac_in_reef=0.22902143041569842
- seed3_no_sleep: frac_dread_above_p75=0.2500495933346558 frac_z_harm_a_above_p75=0.2500495933346558 frac_harm_event=0.09234278912914104 frac_in_reef=0.31362824836341996
- seed4_with_sleep: frac_dread_above_p75=0.2493655895787515 frac_z_harm_a_above_p75=0.25004229402808326 frac_harm_event=0.057858230417864996 frac_in_reef=0.2983420740991372
- seed4_no_sleep: frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.0505 frac_in_reef=0.22608333333333333
- seed5_with_sleep: frac_dread_above_p75=0.2500215461518573 frac_z_harm_a_above_p75=0.2500215461518573 frac_harm_event=0.055675256399207104 frac_in_reef=0.41377230026717227
- seed5_no_sleep: frac_dread_above_p75=0.25004866653688923 frac_z_harm_a_above_p75=0.24927000194666146 frac_harm_event=0.07397313607163714 frac_in_reef=0.3339497761339303

## For a future reader (or `/failure-autopsy`) on THIS run

If `spawn_match_rate` is below 0.8, the shared-candidate-order fix
still left too many boundaries with genuinely divergent hazard/resource occupancy between
arms (hazard drift can differ enough by segment>1 to exclude the shared first choice in
one arm but not the other) -- a successor could canonicalize the occupied-set reference
(e.g. always filter against the ep0 canonical hazard/resource set rather than each arm's
live drifted set) to raise the match rate further. If `n_sleep_firing_matched_comparisons`
is small despite 6 seeds, the K=10 cadence did not fire enough within 24 segments for some
seeds -- lower `sleep_loop_episodes_K` or raise `EVAL_EPISODES` in a successor. This run
does NOT attempt the transfer test or blinded umpire (Section 13d items 4-5) -- those are
gated on THIS run producing `coherence_lift_significant=True`.
