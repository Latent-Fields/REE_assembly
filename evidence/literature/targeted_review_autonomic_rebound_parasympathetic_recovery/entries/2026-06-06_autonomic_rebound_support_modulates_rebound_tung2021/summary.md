# Emotional support modulates vagal rebound -- one recovery axis, two inputs (Tung et al. 2021)

According to PubMed. [DOI](https://doi.org/10.1111/psyp.13808) -- *Psychophysiology* 58(6):e13808.

**What the paper did.** In 191 pregnant women, Tung et al. recorded heart rate and HRV (RMSSD)
across the preparation, task, and recovery phases of the Trier Social Stress Test, and used
piecewise growth-curve modelling to separate the *reactivity* slope from the *recovery* slope.
They then asked how recent life stress and reported emotional support related to each slope.

**Two findings, both useful.** First -- and structurally important -- recovery (vagal rebound) was
modelled as a *distinct slope* from reactivity, confirming that recovery is its own isolable axis
rather than the back-half of the reactivity curve. Second, life stress predicted greater HRV
reactivity *and* greater vagal rebound, but the rebound association held **only among women
reporting high emotional support**. So a social input (emotional support) was a proximate modulator
of the very recovery axis that, in Mezzacappa, fires endogenously at stressor offset.

**Why this is the load-bearing paper for the architecture.** It is exactly the double-edged anchor
the design pass needs. It shows that the endogenous offset-triggered rebound (the candidate sibling
claim) and social soothing (MECH-355) **converge on one recovery variable** -- they are dissociable
by *trigger* (internal offset vs conspecific), not by *effector*. That is the precise warrant for
the recommendation in `mech_355_soothing_update_rule_and_scope_design_2026-06-05.md`: register the
endogenous rebound as a **separate sibling** that shares the MECH-219 `recovery_rate` / SD-032e
`drive_bias`-leak target with MECH-355, rather than folding either into the other. One target, two
inputs, kept clean.

**Limitations and caveats.** The experimental lever here is *social* (emotional support), so this
paper most directly evidences the MECH-355 soothing input; it supports the endogenous-rebound claim
only at the level of "rebound is a discrete recovery axis that multiple inputs can drive." It does
not isolate a non-social trigger -- which is itself the methodological lesson: an
endogenous-rebound test in REE must hold social inputs absent to avoid confounding the sibling with
MECH-355. The sample (pregnant women) and the TSST (an inherently social-evaluative stressor)
further bound transfer.

**Confidence.** 0.70, direction **mixed**. Strong on "recovery is its own axis" and on the
shared-variable/distinct-trigger architecture; discounted because its manipulation is the social
(MECH-355) side, not the endogenous trigger the candidate claim is about.
