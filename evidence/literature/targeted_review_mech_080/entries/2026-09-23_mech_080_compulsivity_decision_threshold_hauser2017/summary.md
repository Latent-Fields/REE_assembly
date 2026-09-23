# Increased decision thresholds across the compulsivity spectrum (Hauser et al., 2017)

## What the paper did

Hauser and colleagues took a population-representative cohort (NSPN) rather than a
case-control clinical sample, scored each subject on psychiatric symptom dimensions, and had
them perform a sequential information-gathering task: draw evidence one item at a time, pay
for draws in the costly condition, decide when you have seen enough. They then fit a
decision-theoretic model in which the stopping point is set by an accumulating cost or
urgency term that eventually overwhelms the value of another draw.

Subjects high on the compulsivity dimension drew more before committing. The model localised
this not to a statically elevated bound but to a *delayed emergence of urgency* -- impatience
arrived later, so the accumulation ran longer. Crucially, the effect was specific: it loaded
on compulsivity and not on the other symptom dimensions measured in the same subjects.

## What this does and does not do for MECH-080

This is the strongest external support I found for the *shape* of MECH-080, and the clearest
external problem for its *content*. I want to separate those cleanly, because a governance
pass that reads only the direction field will get this wrong in one direction or the other.

The shape: MECH-080 bets that you do not need three disorder-specific mechanisms to get
three commitment phenotypes -- that one parameter family, differently set, produces premature
commitment at one end and over-withheld commitment at the other, and that these settings are
what psychiatric categories are tracking. Hauser et al. demonstrate exactly half of that in
humans: one threshold parameter, dimensionally graded, producing over-withholding that loads
on a real symptom axis, with no disorder-specific apparatus. That is a non-trivial external
vindication of the claim's reductive strategy.

The content: MECH-080 assigns extension-bias -- chronically elevated uncertainty, threshold
too high, suppressed commitment -- to *anxiety*, and assigns OCD to a quite different
mechanism, attractor lock-in in a deep basin. This paper puts extended gathering on
*compulsivity*, the dimension that OCD loads on, and explicitly not on the affective
dimensions. If the paper is right, MECH-080's three-way arm assignment is wrong in at least
one arm, and possibly collapses: the disorder the claim routes to lock-in turns out to
present with the phenotype the claim routes to anxiety.

## The mechanism detail that matters for any REE experiment

The delayed-urgency finding is not a footnote. MECH-080's manipulation spec contemplates
setting a threshold; Hauser's subjects did not have a different bound, they had a different
*time course* of the pressure to commit. Those are different interventions in REE too: a
raised static commit threshold and a slowed urgency ramp produce different trajectories and
different DVs, and only the second is what this paper actually evidences. If a future
V3 experiment for MECH-080 ever becomes runnable, it should manipulate the urgency ramp and
not only the bound, or it will be testing something the literature does not speak to.

## Confidence

0.62, `mixed`. The source is good -- population-representative, dimensional, well-modelled,
and the specificity analysis is the kind that makes a result hard to dismiss. What holds the
number down is mapping fidelity at 0.55: this is a threshold on external evidence sampling,
not on internal rollout depth, and REE keeps those in different places. The `mixed` direction
is load-bearing and should not be smoothed to `supports` on the strength of the first half.
