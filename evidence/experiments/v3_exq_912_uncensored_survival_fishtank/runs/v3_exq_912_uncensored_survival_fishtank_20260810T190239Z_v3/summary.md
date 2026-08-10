# V3-EXQ-912 -- Uncensored Survival-to-Death Fishtank Successor

**Status:** FAIL (diagnostic characterization run -- not scored against any claim)
**Purpose:** large-n (n=60 segments across 1 seeds) characterization
of the health_depleted death-time distribution on the 906b ecology tier, replacing the prior
906b/906c/911 lineage's single-run, mostly-censored n=8 point estimates (75%/87.5%/100%
right-censored respectively) with a proper survival-analysis treatment. See module docstring
for the substrate-readiness finding (the per-segment 500-step cap is a hardcoded substrate
constant, not a driver-configurable parameter) that shaped this run's actual design, and for
why 906b's ecology tuning was deliberately reused instead of 911's (which produced ZERO deaths
in its own 8-segment eval).

- harm-pathway train steps (total): 3968
- z_goal activated at eval: True
- eval steps (total): 29529  across 60 segments/seed x up to 500 steps
- **segments: 60 total -- uncensored (genuine) deaths: 4 -- censored (hit 500-step cap): 56 -- pct_right_censored: 0.933**
  (compare 906b 75%, 906c 87.5%, 911 100%)
- uncensored survival times (steps, pooled across seeds): min=261.0 median=390.5 mean=382.25 max=487.0
- cumulative lived steps (both seeds, sum of realized_steps across all segments): 29529
- events: block=1136 limb_damage=267 external_hazard=245 world_rule_shift=118
- sleep cycles fired: 6
- freeze fires (eval, motor-override relaxed): 0
- safe-spawn retries (total): 6  (segments exhausted: 0)

## Eval channel mean / max-std
- z_harm_s: mean=0.1965 max_std=0.03724 (varies)
- z_harm_un: mean=0.3895 max_std=0.06913 (varies)
- z_harm_a: mean=3.6788 max_std=2.11369 (varies)
- drive: mean=0.3329 max_std=0.19848 (varies)
- z_goal: mean=0.0034 max_std=0.02886 (varies)
- vigor: mean=0.0000 max_std=0.00000 (FLAT)
- override: mean=0.6767 max_std=0.04434 (varies)
- z_block: mean=0.0026 max_std=0.02684 (varies)
- excite: mean=22.0370 max_std=13.95010 (varies)
- dread: mean=1.7679 max_std=1.17418 (varies)

## Lifetime affective occupancy (per seed, non-gating, SENT-2 hygiene -- see module docstring)
- seed 0: n_measured=29529 frac_dread_above_p75=0.2499915337464865 frac_z_harm_a_above_p75=0.2499915337464865 frac_harm_event=0.06180365064851502 frac_in_reef=0.263266619255647

The `_episode_log.json` companion is THINNED per the module docstring ("EPISODE-LOG SIZE
MANAGEMENT") -- full per-step records are kept only for the first 3
segments/seed and every genuinely-died segment; other censored segments are stored as a
per-segment summary. Every statistic in THIS manifest is computed from the full, unthinned
in-memory data, so thinning does not bias any reported number.

## For a future reader (or `/failure-autopsy`) on THIS run

If `n_uncensored_deaths_total` is near zero despite reusing 906b's (not 911's) ecology, the
906b ecology tier's death rate may itself have drifted, or this run's larger n surfaced a
genuine within-life adaptation effect (fewer deaths later in a life than earlier -- see the
organism-lifespan review Section 7's flagged, currently-unresolved within-life-development
question; this run's per-segment `cumulative_step_start`/`cumulative_step_end` markers make
that a checkable follow-on without re-running anything). If `pct_right_censored_pooled` is
still high, the next lever is the substrate follow-on named in this docstring
(parameterize CausalGridWorldV2's per-episode step cap), not another lettered increase to
EVAL_EPISODES, which cannot remove the 500-step ceiling.
