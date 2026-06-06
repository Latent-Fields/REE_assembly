# Vagal rebound and recovery from psychological stress (Mezzacappa et al. 2001)

According to PubMed. [DOI](https://doi.org/10.1097/00006842-200107000-00018) -- *Psychosomatic Medicine* 63(4):650-7.

**What the paper did.** Across two experiments, healthy adults performed acute stressors
(cold pressor, mental arithmetic, Stroop) while heart rate, heart-period variability (a vagal
index), pre-ejection period (a sympathetic index), blood pressure, and baroreflex sensitivity
were recorded across baseline, task, and recovery windows. The recovery period was the object of
interest, not the reactivity peak.

**The finding that matters here.** Recovery was not the mirror-image relaxation of the stress
response. Heart-period variability rose *above baseline* in the first minute of recovery -- a
"vagal rebound" -- and it did so *despite continued pre-ejection-period shortening*, i.e. while
sympathetic drive was still elevated. Recovery from stress is therefore an **active
parasympathetic process layered on top of a still-decaying stress signal**, not the passive
fade-out of the stressor. This is precisely the dissociation the candidate REE claim rests on:
an endogenous, offset-triggered recovery process distinct from the passive decay of the aversive
accumulator.

**How it maps to REE.** The candidate "endogenous parasympathetic recovery / autonomic rebound"
mechanism proposes a transient boost to the *recovery side* of REE's slow affective accumulators
-- the MECH-219 `z_harm_a` `recovery_rate` and the SD-032e `drive_bias` leak -- fired at stressor
offset (the `z_harm_a` derivative going negative). Mezzacappa's "rebound rises while sympathetic
is still elevated" is the empirical warrant for separating that active-recovery boost from the
passive `recovery_rate` and from the still-elevated accumulation side. It also tells us the
trigger is *offset*, the same event MECH-302 relief consumes -- which is a feature, not a
confound: one upstream offset event can fan out to a reinforcement readout (relief) and a
recovery-rate boost (rebound), with different outputs.

**Limitations and caveats.** REE has no separate sympathetic and parasympathetic effectors, so
the paper's two-branch cardiac story is being compressed onto REE's single accumulation-vs-recovery
axis. The measures are cardiac autonomic indices in humans, not a latent suffering accumulator;
the claim borrows the *active-recovery principle*, not the cardiac specifics. Critically, the
rebound was *reduced* in men and in those with a family history of cardiovascular disease -- so it
is a gated, individual-difference-laden process, which argues that the REE analog should be a
parameterised/gated mechanism rather than an automatic reflex.

**Confidence.** 0.80. The active-recovery-distinct-from-passive-decay principle is exactly on
target and replicated across tasks; I dock it for the human-cardiac-to-latent-substrate transfer
and for the single-axis compression of the dual-branch physiology.
