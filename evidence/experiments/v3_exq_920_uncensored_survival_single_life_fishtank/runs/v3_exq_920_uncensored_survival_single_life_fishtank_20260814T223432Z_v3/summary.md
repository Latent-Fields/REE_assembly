# V3-EXQ-920 -- Uncensored Survival-to-Death Fishtank, TRUE Single-Life Design

**Status:** PASS (diagnostic characterization run -- not scored against any claim)
**Purpose:** TRUE single-continuous-life (8 independent lives, one per seed,
each up to 20000 steps with NO segment-boundary respawn) characterization of the
health_depleted death-time distribution on the 906b ecology tier. Supersedes V3-EXQ-912's
segment-count-scaling workaround: that run's own "SUBSTRATE READINESS FINDING" section
named the per-episode step-cap literal as a substrate gap; this run consumes the now-landed
`max_episode_steps` kwarg (SD-FISHTANK-MAX-EPISODE-STEPS, ree-v3 9d3d148ff8) to implement
option (a) from organism_lifespan_development_review_906_lineage_2026-08-10.md Section 10
item 1 literally, as originally described, rather than as an approximation.

- harm-pathway train steps (total): 96883
- z_goal activated at eval: True
- eval steps (total): 13718  across 8 single-life continuous segments
- **lives: 8 total -- uncensored (genuine) deaths: 8 -- censored (hit 20000-step ceiling): 0 -- pct_right_censored: 0.000**
  (compare V3-EXQ-912's segment-count-scaling design: 93.3% right-censored at n=60 segments/seed x 1 seed)
- uncensored survival times (steps, one per genuinely-died seed): min=628.0 median=1831.0 mean=1714.75 max=2527.0
- cumulative lived steps (sum of realized_steps across all seeds' single lives): 13718
- events: block=557 limb_damage=136 external_hazard=122 world_rule_shift=52
- sleep cycles fired (during eval): 0 (EXPECTED 0 -- see module docstring "SLEEP-CADENCE DESIGN NOTE": a single-episode eval has no non-zero segment boundary to trigger sleep_loop.notify_episode_end())
- freeze fires (eval, motor-override relaxed): 0
- safe-spawn retries (total, at each life's single spawn): 1  (lives exhausted: 0)

## Eval channel mean / max-std
- z_harm_s: mean=0.1937 max_std=0.06724 (varies)
- z_harm_un: mean=0.3844 max_std=0.09919 (varies)
- z_harm_a: mean=3.4537 max_std=2.63832 (varies)
- drive: mean=0.7265 max_std=0.33357 (varies)
- z_goal: mean=0.0657 max_std=0.12633 (varies)
- vigor: mean=0.0000 max_std=0.00233 (varies)
- override: mean=0.7337 max_std=0.11395 (varies)
- z_block: mean=0.0841 max_std=0.32393 (varies)
- excite: mean=1.2707 max_std=2.12133 (varies)
- dread: mean=0.0951 max_std=0.10588 (varies)

## Per-seed single-life outcome
- seed 0: realized_steps=1944 done_cause=health_depleted kept_full_in_log=True
- seed 1: realized_steps=1432 done_cause=health_depleted kept_full_in_log=True
- seed 2: realized_steps=1846 done_cause=health_depleted kept_full_in_log=True
- seed 3: realized_steps=1008 done_cause=health_depleted kept_full_in_log=True
- seed 4: realized_steps=2527 done_cause=health_depleted kept_full_in_log=True
- seed 5: realized_steps=628 done_cause=health_depleted kept_full_in_log=True
- seed 6: realized_steps=2517 done_cause=health_depleted kept_full_in_log=True
- seed 7: realized_steps=1816 done_cause=health_depleted kept_full_in_log=True

## Lifetime affective occupancy (per seed, non-gating, SENT-2 hygiene -- see module docstring)
- seed 0: n_measured=1944 frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.047839506172839504 frac_in_reef=0.26800411522633744
- seed 1: n_measured=1432 frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.061452513966480445 frac_in_reef=0.22416201117318435
- seed 2: n_measured=1846 frac_dread_above_p75=0.24972914409534128 frac_z_harm_a_above_p75=0.2502708559046587 frac_harm_event=0.043878656554712896 frac_in_reef=0.2361863488624052
- seed 3: n_measured=1008 frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.07142857142857142 frac_in_reef=0.9186507936507936
- seed 4: n_measured=2527 frac_dread_above_p75=0.2489117530668777 frac_z_harm_a_above_p75=0.25009893153937474 frac_harm_event=0.038781163434903045 frac_in_reef=0.30193905817174516
- seed 5: n_measured=628 frac_dread_above_p75=0.25 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.09076433121019108 frac_in_reef=0.07165605095541401
- seed 6: n_measured=2517 frac_dread_above_p75=0.24990067540723082 frac_z_harm_a_above_p75=0.24990067540723082 frac_harm_event=0.03734604688120779 frac_in_reef=0.15812475168851808
- seed 7: n_measured=1816 frac_dread_above_p75=0.2444933920704846 frac_z_harm_a_above_p75=0.25 frac_harm_event=0.040198237885462555 frac_in_reef=0.4779735682819383

The `_episode_log.json` companion is THINNED per the module docstring ("EPISODE-LOG SIZE
MANAGEMENT") -- full per-step records are kept only for the first 2
seeds and every seed whose life genuinely ended health_depleted; other censored lives are
stored as a per-life summary. Every statistic in THIS manifest is computed from the full,
unthinned in-memory data, so thinning does not bias any reported number.

## For a future reader (or `/failure-autopsy`) on THIS run

If `n_uncensored_deaths_total` is near zero despite the 40x step-budget calibration in the
module docstring, either this ecology tier's death rate has drifted since V3-EXQ-912, or
within-life competence genuinely improves with sustained exposure enough to suppress death
well past 500 steps (organism_lifespan_development_review_906_lineage_2026-08-10.md Section
7's own flagged-but-unresolved question) -- this run's own death-time distribution, where
deaths occur, is now direct within-life-competence-vs-time evidence with no segment-boundary
confound. If `pct_right_censored_pooled` stays high, the next lever is a larger EVAL_STEPS
ceiling (a driver-level config change, not a substrate gap) -- not a return to segment-count
scaling. Separately, this run's design surfaces (does not resolve) whether REE's sleep
substrate should trigger on elapsed time/fatigue within an unbroken life rather than only at
experimenter-imposed recording-chunk boundaries -- see module docstring "SLEEP-CADENCE DESIGN
NOTE".
