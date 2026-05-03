# Asai (2016): Agency Judgment as a Signal-to-Noise Function

This is the most directly relevant paper for the SD-047 substrate-
ceiling diagnosis I have found. Asai presented healthy participants
with a continuously morphed visual feedback of their own reaching
movements, varying along a self-versus-other axis. Agency ratings were
collected at each level of the morph. The headline finding is that the
*slope* of the regression line of agency rating against self-other
discriminability — not the intercept, not the mean — captures the
comparator's competence, and that schizotypal participants exhibit
shallower slopes producing both over- and under-attribution errors
symmetrically depending on which side of the discriminability midpoint
the stimulus sits.

This is exactly the substrate-ceiling argument transposed to humans.
The MECH-095 comparator's `cf_gap_event / cf_gap_quiet` ratio in
V3-EXQ-506 is the same shape as Asai's discriminability slope: a
measure of how strongly the comparator's counterfactual difference
tracks the agent's actual contribution to state change. V3-EXQ-506's
finding that C4 PASSes while C1-C3 fail is, on Asai's framing, what
you would predict if the comparator's input range is too narrow:
agency-correlated cases (the C4 baseline) separate trivially, but the
intermediate cases that require fine S/N discrimination (C1-C3)
collapse because the env never delivers stimuli in the regime where
the slope could be measured.

What this means for SD-047 implementation is more pointed than I
initially appreciated. Asai's data implies a non-monotonic relationship
between env noise and comparator performance: too little noise and the
comparator never sees the regime where its slope is informative; too
much noise and the agent's signal is overwhelmed and slope flattens
again. The 1:1-2:1 env:agent change-rate calibration target in the
SD-047 design doc is therefore not a rough ballpark — it is load-
bearing. A naive implementation that ramps env noise without
calibration would risk pushing the comparator past the optimum and
producing *worse* MECH-095 performance, which would superficially
read as "SD-047 failed" but actually be a calibration failure.

The framing also reframes what counts as a falsification of SD-047.
If implementation produces an inverted U on agency-detection
performance as multi-source intensity increases — improving up to a
point, then degrading — that is *consistent* with Asai and supports
SD-047. If implementation produces a flat curve at all noise levels,
that weakens SD-047 because it implies the comparator was either
always working (substrate ceiling was wrong) or always broken
(architecture issue, not substrate). The pre-registered
discriminative-pair experiment in the SD-047 design doc should add
intermediate noise levels rather than just ON-vs-OFF.

Confidence reasoning: source quality is solid for a behavioural study
(peer-reviewed, N=104, well-controlled paradigm). Mapping fidelity is
high because Asai's slope variable is structurally the same as
cf_gap_ratio. Transfer risk is moderate because the modality differs
(visual morphing vs gridworld hazard fields) but the substrate-ceiling
principle is what transfers, not the modality. Net confidence ~0.83 —
the highest of the SD-047 lit-pull, and the paper most likely to need
to re-read at implementation time.

According to PubMed, [DOI: 10.1016/j.psychres.2016.10.082](https://doi.org/10.1016/j.psychres.2016.10.082).
