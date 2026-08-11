# V3-EXQ-920 -- Uncensored Survival-to-Death Fishtank, TRUE Single-Life Design

**Status:** FAIL (diagnostic characterization run -- not scored against any claim)
**Purpose:** TRUE single-continuous-life (1 independent lives, one per seed,
each up to 20000 steps with NO segment-boundary respawn) characterization of the
health_depleted death-time distribution on the 906b ecology tier. Supersedes V3-EXQ-912's
segment-count-scaling workaround: that run's own "SUBSTRATE READINESS FINDING" section
named the per-episode step-cap literal as a substrate gap; this run consumes the now-landed
`max_episode_steps` kwarg (SD-FISHTANK-MAX-EPISODE-STEPS, ree-v3 9d3d148ff8) to implement
option (a) from organism_lifespan_development_review_906_lineage_2026-08-10.md Section 10
item 1 literally, as originally described, rather than as an approximation.

- harm-pathway train steps (total): 4038
- z_goal activated at eval: True
- eval steps (total): 1475  across 1 single-life continuous segments
- **lives: 1 total -- uncensored (genuine) deaths: 1 -- censored (hit 20000-step ceiling): 0 -- pct_right_censored: 0.000**
  (compare V3-EXQ-912's segment-count-scaling design: 93.3% right-censored at n=60 segments/seed x 1 seed)
- uncensored survival times (steps, one per genuinely-died seed): min=1475.0 median=1475.0 mean=1475.0 max=1475.0
- cumulative lived steps (sum of realized_steps across all seeds' single lives): 1475
- events: block=60 limb_damage=14 external_hazard=9 world_rule_shift=5
- sleep cycles fired (during eval): 0 (EXPECTED 0 -- see module docstring "SLEEP-CADENCE DESIGN NOTE": a single-episode eval has no non-zero segment boundary to trigger sleep_loop.notify_episode_end())
- freeze fires (eval, motor-override relaxed): 0
- safe-spawn retries (total, at each life's single spawn): 0  (lives exhausted: 0)

## Eval channel mean / max-std
- z_harm_s: mean=0.1668 max_std=0.03095 (varies)
- z_harm_un: mean=0.3303 max_std=0.05288 (varies)
- z_harm_a: mean=3.2508 max_std=1.24368 (varies)
- drive: mean=0.6864 max_std=0.33580 (varies)
- z_goal: mean=0.0678 max_std=0.11146 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.7167 max_std=0.09124 (varies)
- z_block: mean=0.0800 max_std=0.20534 (varies)
- excite: mean=2.7221 max_std=1.86577 (varies)
- dread: mean=0.1619 max_std=0.12642 (varies)

## Per-seed single-life outcome
- seed 0: realized_steps=1475 done_cause=health_depleted kept_full_in_log=True

## Lifetime affective occupancy (per seed, non-gating, SENT-2 hygiene -- see module docstring)
- seed 0: n_measured=1475 frac_dread_above_p75=0.2501694915254237 frac_z_harm_a_above_p75=0.2501694915254237 frac_harm_event=0.06779661016949153 frac_in_reef=0.2922033898305085

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
