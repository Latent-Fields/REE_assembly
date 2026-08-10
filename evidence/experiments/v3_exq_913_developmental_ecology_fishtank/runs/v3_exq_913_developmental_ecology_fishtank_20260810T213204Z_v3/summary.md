# V3-EXQ-913 -- Developmental-Ecology Fishtank Successor

**Status:** PASS (diagnostic readiness characterization -- not scored against any claim)
**Purpose:** combined layout-continuity + probabilistic-habitat-cue (microhabitat zones) +
sleep-vs-no-sleep ablation successor to the V3-EXQ-906 lineage, addressing three findings
from the organism-level Fishtank reviews as one successor (see module docstring for full
routing + substrate-readiness reasoning, including why microhabitat zones were used instead
of the correction document's own "landmark" suggestion).

- harm-pathway train steps (total, all seed/arm): 25045
- layout continuity confirmed (all seed/arm): True
- microhabitat zone map active (all seed/arm): True
- sleep cycles fired -- WITH_SLEEP arm: 5  NO_SLEEP arm: 0
- matched sleep-firing-vs-no-sleep-control comparisons obtained: 5
- eval steps (total): 45718  across 24 segments/(seed,arm) x up to 500 steps
- events: block=1828  freeze fires (motor-override relaxed): 0
- safe-spawn / continuity-spawn retries (total): 13  (segments exhausted: 0)
- segments with resources fully exhausted (total, across seed/arm): 55

## Eval channel mean / max-std
- z_harm_s: mean=0.2189 max_std=0.17187 (varies)
- z_harm_un: mean=0.3473 max_std=0.09998 (varies)
- z_harm_a: mean=2.4540 max_std=2.07246 (varies)
- drive: mean=0.9216 max_std=0.23802 (varies)
- z_goal: mean=0.0079 max_std=0.04588 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.7723 max_std=0.04944 (varies)
- z_block: mean=0.0385 max_std=0.19810 (varies)
- excite: mean=87.7645 max_std=1240.24850 (varies)
- dread: mean=7.4590 max_std=127.43938 (varies)

## Within-life development (organism review Section 7, now unconfounded by layout continuity)
- seed0_with_sleep: n_segments=24 r(segment,harm_rate)=0.402993295656142 r(segment,benefit_rate)=-0.5677711588410671 r(segment,mode_entropy)=-0.612812084452875
- seed0_no_sleep: n_segments=24 r(segment,harm_rate)=0.022924461679906107 r(segment,benefit_rate)=-0.13480889618207406 r(segment,mode_entropy)=-0.10180913333969814
- seed1_with_sleep: n_segments=24 r(segment,harm_rate)=0.35107794433062833 r(segment,benefit_rate)=-0.6490262627348669 r(segment,mode_entropy)=-0.65895740874199
- seed1_no_sleep: n_segments=24 r(segment,harm_rate)=0.22048286284689259 r(segment,benefit_rate)=0.016012086215593805 r(segment,mode_entropy)=-0.24508227059694948

## Sleep-vs-no-sleep matched comparisons (per seed)
- seedseed0: n_sleep_firings=3 fired_at_segments=[1, 11, 21]
- seedseed1: n_sleep_firings=2 fired_at_segments=[9, 19]

## Zone-conditioned field statistics (per seed/arm) -- resource_field / hazard_field mean by microhabitat zone
- seed0_with_sleep: {'1': 0.28652332671038755, '3': 0.2887730885475764, '2': 0.759546200304036, '0': 0.1698149445243478}
- seed0_no_sleep: {'1': 0.10552069507238845, '3': 0.09222968806932261, '2': 0.17673895744302257, '0': 0.060845833928254156}
- seed1_with_sleep: {'0': 1.2121959628878465, '3': 0.5508104706996609, '2': 0.3631348757979412, '1': 0.16404298334938638}
- seed1_no_sleep: {'0': 3.022536535061265, '2': 1.6707507175324798, '3': 2.6510161758637896, '1': 2.896306834033457}

## Lifetime affective occupancy (per seed/arm, non-gating, SENT-2 hygiene -- see module docstring)
- seed0_with_sleep: frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.06200069468565474 frac_in_reef=0.3601076762764849
- seed0_no_sleep: frac_dread_above_p75=0.24997659395187716 frac_z_harm_a_above_p75=0.24997659395187716 frac_harm_event=0.09390506506881378 frac_in_reef=0.2704802921074806
- seed1_with_sleep: frac_dread_above_p75=0.25004202386955793 frac_z_harm_a_above_p75=0.24844511682635737 frac_harm_event=0.06219532694570516 frac_in_reef=0.3076987729030089
- seed1_no_sleep: frac_dread_above_p75=0.2500215090768304 frac_z_harm_a_above_p75=0.2500215090768304 frac_harm_event=0.039404628753333906 frac_in_reef=0.258453067194356

## For a future reader (or `/failure-autopsy`) on THIS run

If `n_sleep_firing_matched_comparisons` is near zero, the K=10 cadence did not fire within
this run's 24 segments for some seeds -- increase EVAL_EPISODES or lower
sleep_loop_episodes_K in a successor rather than re-running unchanged. If
`total_resource_exhausted_segments` is large, DEV_NUM_RESOURCES=24 was not enough headroom
for a fully-foraging life at this ecology's consumption rate -- raise it (still with
resource_respawn_on_consume=False, per the module docstring's zone-dilution reasoning) in a
successor. The `zone_habitat` block's per-zone resource_field means are the check for
whether the probabilistic-habitat-cue manipulation left a perceptible trace in what REE
actually senses; SD-025/MECH-314 per-tick logging (module docstring "SCOPE, NOT ADDED") is
the concrete next step for testing whether REE exploits it, not merely whether it exists.
