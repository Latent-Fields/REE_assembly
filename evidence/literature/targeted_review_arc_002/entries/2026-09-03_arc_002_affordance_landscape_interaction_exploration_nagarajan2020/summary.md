# Learning Affordance Landscapes for Interaction Exploration in 3D Environments

Nagarajan & Grauman (NeurIPS 2020) put an embodied agent into unmapped AI2-iTHOR homes with
an egocentric RGB-D camera and a discrete high-level action space, and train it to discover
what the environment permits. The agent is rewarded for maximising successful interactions
and, in the same loop, trains an image-based affordance segmentation model mapping image
regions to the likelihood that each action succeeds there. The two halves feed each other:
the affordance model densifies an otherwise very sparse exploration reward, and the
exploration supplies the interaction outcomes the affordance model learns from. The result
is a policy that prepares an agent for downstream tasks -- find a knife, put it in the drawer
-- in kitchens it has never seen.

This is the closest working analogue I have found to what ARC-002's confirming test asks
for: a learned readout that predicts, per state, which actions are viable, scored against
ground-truth interaction success. That much supports the claim. The object ARC-002 says E2
should produce is a real, learnable, transferable thing, not a notional one, and someone has
built it and shown it pays.

The way they had to build it is what makes this entry mixed rather than supporting. The
affordance model here is trained by an *explicit interaction-success signal*, harvested by a
policy specifically rewarded for interacting. It does not fall out of passive action-conditioned
dynamics prediction; the whole architecture exists because discovering the affordance landscape
turned out to need dedicated exploration. Read back against ARC-002, that is a warning about
the mechanism. If viability structure required a viability-specific training signal here, it
is a live possibility that E2's world-forward and contrastive objectives (SD-056's
`cand_world_pairwise_dist`, `world_forward_contrastive_loss`) will not produce it either --
which is precisely ARC-002's falsifying branch, E2 behaving as a generic dynamics predictor
indexed by action with no distinct "what can I do here" structure. The paper does not test
that branch, but its design implicitly anticipates and engineers around it.

There is a second, structural distance. Their affordance model sits over *perception* -- a
segmentation network on egocentric RGB-D -- not over a forward model's predicted next state.
So strictly this is evidence about affordance learnability, not about whether forward
prediction carries affordance structure, and the architecture that works here is not the
architecture ARC-002 asserts. The setting also supplies unusually clean supervision: the
simulator's interaction API says whether an action succeeded, which is a luxury REE's
environments do not offer.

One honesty note on provenance. No quantitative results are recorded in this entry, because
none were verifiable from the abstract and metadata pages retrieved on 2026-09-03 -- the
assessment rests on the paper's design and stated conclusions. If this entry ever becomes
load-bearing for a governance decision, the full text should be read and the record amended.

Recorded as `mixed` at 0.55.
