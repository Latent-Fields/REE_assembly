# Cortical mechanisms of action selection: the affordance competition hypothesis

Cisek's 2007 paper argues against the serial picture in which the brain first builds a
representation of the world, then decides, then computes a motor plan. His claim is that
neurophysiology does not look like that. Instead, sensory information is processed to
specify *in parallel* several potential actions that are currently available; those
candidates compete within fronto-parietal cortex while biasing signals accumulate from
prefrontal regions and the basal ganglia, until the competition resolves into one response.
The dorsal visual system is cast as the specifier of currently-available actions. He backs
this with a computational model of parietal-premotor competition that reproduces qualitative
features of the recorded neural dynamics along with several behavioural phenomena.

For ARC-002 the attraction is architectural rather than mechanistic. ARC-002 places
affordance prediction in E2 -- the *fast* forward stream -- rather than in a deliberative
evaluator, and REE's wider architecture assumes a division of labour where E2 offers what is
doable and E3 selects among it. Cisek's hypothesis is the neural form of both bets at once:
the fast dorsal pathway specifies what is currently possible, and value-based biasing arrives
from elsewhere. The parallelism is the part with the most direct bearing on measurement. It
says the substrate holds a *set* of currently-viable actions simultaneously, which is exactly
the shape ARC-002's confirming readout assumes -- a per-action-class viability pattern, of
the kind already implemented narrowly for threat and escape in
`ree_core/pfc/e2_escape_affordance_linker.py` and which the claim proposes generalising.

There is a mismatch here that I do not think should be smoothed over, because it is the
whole of what ARC-002 asserts beyond its neighbours. Cisek's dorsal stream *specifies*
actions. It is nowhere characterised as a forward *predictor*. A direct sensorimotor
transformation from state to available actions -- no forward model anywhere in the loop --
would satisfy every result cited in this paper. So the identification of the dorsal specifier
with E2's action-conditioned prediction is REE's inference, not Cisek's finding, and this
entry cannot be used to argue that affordances are computed *by prediction*. It supports the
placement of affordance representation in the fast stream, and the parallel-set structure of
that representation; it is silent on the predictive mechanism.

The supporting evidence is also thinner than the hypothesis. It is a review-and-model paper,
the neurophysiology it marshals is largely correlational, and it comes mostly from macaque
reaching tasks where "affordance" means a small set of spatially-defined reach targets. That
is a considerably thinner notion than ARC-002's context-dependent action viability -- and
notably, reach targets do not obviously satisfy the claim's own non-degeneracy precondition,
which demands actions that are available or effective only in some states.

Recorded as `supports` at 0.6. Source quality is high for its type and the architectural
alignment is real, but mapping fidelity is the binding constraint: specification is not
prediction, and the gap between them is where ARC-002 lives.
