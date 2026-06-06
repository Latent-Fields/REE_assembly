# Parasympathetic reactivation has its own kinetics, set by baseline tone (Cunha et al. 2015)

According to PubMed. [DOI](https://doi.org/10.1186/s40064-015-0882-1) -- *SpringerPlus* 4:100.

**What the paper did.** Twenty healthy men performed three maximal cardiopulmonary exercise tests
(cycling, walking, running) in randomised order. Recovery was characterised by heart-rate recovery
(HRR at 1-3 min post-exercise) and by the root-mean-square of successive R-R differences computed
in consecutive 30-s windows (rMSSD30s), giving a *trajectory* of parasympathetic reactivation
rather than a single endpoint.

**The relevant finding.** Parasympathetic reactivation is a process with measurable **kinetics** --
a rate at which vagal control returns -- and that rate is conditioned by the agent's baseline:
delta-rMSSD into recovery correlated positively with resting HF, rMSSD, and SDNN and negatively
with resting LF:HF. Recovery was also modality-dependent (faster after cycling than walking or
running). Recovery is therefore neither instantaneous nor a fixed constant; it is a
state-conditioned rate.

**How it maps to REE.** This speaks to the *smallest-form* question for the candidate claim. If
endogenous rebound is to be modelled in REE, this paper supports doing it as an offset-triggered
**transient multiplier on a recovery rate** -- boosting the MECH-219 `z_harm_a` `recovery_rate` and
the SD-032e `drive_bias` leak -- scaled by the agent's current state, rather than as a flat decay
constant or an instantaneous reset. The baseline-tone dependence maps onto making the rebound boost
a function of current accumulator/drive level (which also dovetails with the load-proportionality
property the MECH-355 design pass insists on).

**Limitations and caveats.** The stressor is maximal physical exercise, not an aversive or
psychological event; parasympathetic reactivation after exertion is not the same physiology as
recovery from an aversive episode. I use this paper only for the *generic* point that autonomic
recovery has a tunable, baseline-conditioned rate -- never for any quantitative parameter value.
Sample is healthy young men, narrowing transfer further.

**Confidence.** 0.60, direction supports. The "recovery is a tunable, baseline-conditioned rate"
principle is well-measured here, but the exercise-recovery context and the lack of any aversive
component mean it carries the highest transfer risk of the four entries; it earns its place as the
kinetics/smallest-form anchor, not as direct evidence about aversive-state recovery.
