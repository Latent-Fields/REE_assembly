# A harm prediction error with its own address

Glascher et al. dissociates model error from reward. MECH-034 needs model error dissociated from
*harm*, and reward is not harm with a minus sign -- at least not in REE, where residue is asymmetric,
persistent and non-erasable in a way no appetitive value estimate is. Roy and colleagues supply the
missing half.

They combined an instrumental pain-avoidance task with an axiomatic approach to identifying
prediction-error signals in fMRI. The axiomatic method is worth pausing on, because it is what makes
this more than another regressor-correlation study: rather than asking which voxels correlate with a
modelled PE term, it asks whether a candidate signal satisfies the formal properties any genuine PE
must have (the right ordering across outcome and expectation conditions). The periaqueductal gray
passed. Dynamic causal modelling then placed vmPFC, supported by putamen, as the source of an
expected-value input into PAG, with PAG conveying the resulting error outward to orbitofrontal,
anterior mid-cingulate and dorsomedial prefrontal cortex -- regions that regulate behaviour rather
than regions that maintain a world model.

## The mapping

Two things transfer to REE. The first is the existence claim: harm-related learning runs on its own
circuit, with its own error computation, not as a signed variant of the reward machinery. That is the
architectural precedent for treating residue as a distinct write path rather than a component of one
generic post-action error signal, which is what MECH-034 needs to be true.

The second is the routing. The PE does not terminate in a model-updating structure; it goes to
prefrontal regions concerned with behavioural regulation. MECH-034's confirming criterion asks for
exactly this kind of consequence asymmetry -- residue should raise trajectory cost and persist, while
staleness should route to replay and re-sampling and decay with re-visitation. Roy et al. shows the
harm half of that asymmetry has a biological analogue. The vmPFC-to-PAG expected-value input is also,
as far as I can tell, the nearest thing in the literature to what ARC-035 posits: stored residue being
converted into an *anticipatory* signal available at trajectory-evaluation time, rather than only a
retrospective correction.

## Where I would push back on my own reading

The paper has no harm-free mismatch condition. It establishes that the harm PE has distinct
circuitry; it does not establish that the harm circuit stays quiet when the world model is violated
without harm. That off-diagonal is the thing MECH-034 actually stands or falls on, and no paper in
this pull tests it within subjects. Supporting the double dissociation from this entry therefore
requires chaining it to a separate mismatch-side source, and a chained inference across two
literatures is weaker than one experiment that ran both manipulations.

There is also a construct gap I do not want to smooth over. This is nociceptive pain. REE's harm and
violation outcomes include ethical violation with no nociceptive content at all. Whether a PAG-like
harm-error architecture generalises to violations that hurt nobody's body is a genuinely open
question, and it is the largest single leap in this record -- hence transfer risk at 0.40.

## Confidence

0.68, direction `supports`. Methodologically strong, structurally apt, but doing only half the job
MECH-034 asks of it.
