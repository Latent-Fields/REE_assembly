# Cavanagh et al. (2011), "Subthalamic nucleus stimulation reverses mediofrontal influence over decision threshold"

**Claim tested:** MECH-004 (control-plane signal-to-knob wiring map)
**Direction:** supports | **Confidence:** 0.75

## What the paper did

Fourteen Parkinson's patients with implanted subthalamic electrodes performed a probabilistic
reinforcement-learning task, then faced test pairs that were either low-conflict (a good option
against a bad one) or high-conflict (two similarly good options, or two similarly bad ones).
Each patient was tested twice, on and off stimulation -- a within-subject causal manipulation,
which is rare in this literature. EEG supplied mediofrontal theta as the conflict index and a
hierarchical drift-diffusion model supplied the readout, letting the authors ask not just
"were they slower?" but which parameter of the decision process moved.

Off stimulation, the expected pattern: on high-conflict trials, greater mediofrontal theta
predicted a higher decision threshold and adaptive slowing (P = 0.01) -- the system demanded
more evidence before committing. On stimulation, the relationship did not weaken. It inverted
(P = 0.045). Greater theta now predicted a *lower* threshold and faster, more impulsive
responding. The parameter that moved was specifically the threshold, not the drift rate.

## What it says about MECH-004

This entry bears on the map's S6 section, which is unusual in being explicitly unfinished. S6
proposes a selection-conflict signal -- the decision-gap between the top candidates at commit
time, already computed inside E3 as `gap_norm` for MECH-439's conflict-graded commit temperature
-- and proposes routing it as a fast escalation input to K5 and K10. The map justifies this by
direct analogy to the STN hyperdirect pathway, citing Frank 2006 and Wiecki & Frank 2013, and
then declines to build it: MECH-488 holds the wiring because both `gap_norm` and the receiving
gate are independently degenerate under the current F-dominance regime.

Cavanagh et al. are the causal human test of the analogy the map is leaning on, and it survives.
Interrupting STN does not merely correlate with reduced conflict-induced slowing; it abolishes
and reverses it. That is what a necessary link in a routing pathway looks like, and it is
stronger warrant than the correlational and modelling work the map currently cites. Nothing here
lifts the MECH-488 hold -- that hold is about degeneracy internal to REE's own selection
dynamics, and no external paper can speak to it -- but it does raise the prior that the proposed
wiring is worth building once MECH-439 clears, and it moves S6 from architectural speculation to
a proposal with causal human evidence behind it.

## The correction, which is the more useful half

The evidence supports a different destination knob than the map names, and I think this is worth
more to REE than the confirmation is.

What STN disruption changes is a *graded decision threshold* inside an evidence-accumulation
process: how much evidence is required before committing. MECH-004 routes S6 to K10, defined as
"hard veto threshold: catastrophic interrupt trigger". Those are not the same mechanism and they
do not fail the same way. Raising an evidence requirement is continuous, recoverable, and
proportionate to the conflict that triggered it; tripping a catastrophic veto is none of those.
On this evidence the natural destination for S6 is K3 (commitment depth) or K9 (action
readiness), plausibly with K5 escalation -- and the K10 leg is unsupported. If S6 is eventually
built to the map as written, it would be built to a routing that the literature the map itself
cites does not underwrite.

There is a second design consequence hiding in the inversion result. When the pathway was
disrupted, behaviour did not fall back to conflict-blind responding. It became
conflict-*anti*-correlated: the conflict signal was still generated and was now driving the gate
the wrong way, producing impulsivity precisely when caution was called for. A conflict-to-gate
route is therefore not fail-safe, and an REE implementation of S6 needs a defined behaviour for
the degraded case rather than an assumption that a broken link is equivalent to an absent one.
That seems especially pertinent given MECH-488's finding that the receiving gate is already
degenerate.

## Limitations and caveats

The sample is fourteen Parkinson's patients with implanted electrodes -- a population with
pre-existing basal ganglia pathology and chronic dopaminergic medication, which is exactly the
population in which one can do this experiment and exactly the population from which
generalisation is least clean. The authors are candid that STN-DBS is not anatomically confined:
field spread and antidromic stimulation of cortex are both possible, so "STN is necessary" is
better read as "this stimulation site is necessary". They also leave open whether the
mediofrontal-STN interaction is direct or routed through inferior frontal gyrus.

Finally, the conflict manipulated here is reinforcement-value similarity between two learned
options. That is a decision-gap at selection time, which maps well onto what `gap_norm` computes
-- but whether the same mechanism engages for other senses of contestedness the map might want
S6 to cover is simply untested.

## Confidence reasoning

0.75. Source quality 0.82: methodologically the strongest design in this pull -- within-subject
causal manipulation in humans with a model-based single-parameter readout, in a top venue --
discounted for n=14 and the patient-cohort confounds. Mapping fidelity 0.72: the signal side maps
closely (value-similarity conflict really is a decision-gap), while the knob side is off by one,
supporting a graded threshold rather than the hard veto the map specifies. Transfer risk 0.40 for
the clinical-to-healthy and human-to-artificial-agent steps, offset because the transferred
quantity is computational -- a threshold in an accumulator -- rather than anatomical.
