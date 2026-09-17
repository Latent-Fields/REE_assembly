# Activity-dependent downscaling of subthreshold synaptic inputs during slow-wave-sleep-like activity

## What the paper did

The synaptic homeostasis hypothesis holds that synapses are potentiated during waking and downscaled
during sleep. Gonzalez-Rueda and colleagues put their finger on the awkward part of that story, which
they state plainly: it is not obvious how the same plasticity rules could produce both outcomes.
Their answer is that the rules are gated by cortical dynamics. Recording whole-cell in vivo from
urethane-anaesthetised mice, which show slow-wave-sleep-like activity, and driving presynaptic input
optogenetically, they found that Down states support conventional spike-timing-dependent plasticity,
while Up states are biased toward depression -- presynaptic stimulation alone is enough to weaken a
connection. Critically, that weakening is not applied indiscriminately. Connections that contribute
to postsynaptic spiking are protected from it. The authors identify two computational consequences:
improved signal-to-noise ratio, and preservation of previously stored information.

## Why this is the comparator paper

MECH-018's confirming design is unusual in a way I think is to its credit. It does not ask whether
sleep integration changes the residue field; it asks whether integration beats a specific
alternative -- a naive-decay arm applying uniform multiplicative attenuation to all weights. The
reasoning behind that arm is stated in the claim: uniform decay would satisfy the compression and
traversability readouts while violating preservation. It would look like a success and be a
forgetting.

The question that arm implicitly raises is whether compression-with-a-floor is even a coherent
operation, or whether REE is asking for something no mechanism delivers. This paper answers that.
Biological sleep-associated downscaling is activity-dependent and input-specific, and the stated
payoff is exactly the pair MECH-018 wants: better signal-to-noise, stored information preserved. So
the operation REE is reaching for has a neural existence proof. That does not make `integrate` right
-- it only says the target is not incoherent. Given how much of REE's sleep work rests on the
assumption that consolidation both compresses and preserves, having that assumption grounded in a
whole-cell in vivo result rather than in a theoretical framework seems worth the entry.

## The problem with porting the protection rule

Here is where I think this paper is most useful to us, and it is not in the supporting direction.
The protection criterion is postsynaptic spiking -- a connection is spared if it recently
participated causally in driving its target. That is a beautiful rule for a cortex, because the
thing being protected is the thing still in use.

REE's residue field has no such signal at sleep time. A harm centre the agent laid down long ago and
has not revisited generates no analogue of postsynaptic drive. If `integrate` were written to
protect residue by any obvious proxy for recent activity -- recency, visit frequency, replay
probability -- it would preferentially preserve recent harm contexts and quietly let dormant ones
decay. For most memory systems that would be a reasonable, even desirable, forgetting curve. For
this one it is the wrong answer: MECH-018 exists because residue is supposed to be the thing that
cannot be erased, and the oldest injuries are exactly the ones whose persistence the claim is about.
So the mechanism transfers as an existence proof and does NOT transfer as an implementation recipe.
Whoever wires the WRITEBACK call site should be explicit about what plays the role of the protection
criterion, because taking the obvious one imports a preservation-floor violation.

## Limitations

Urethane anaesthesia produces slow-wave-sleep-like activity, not sleep; the extension to natural
sleep cycles is an inference. This is mouse cortex, and the mapping to a residue field is structural
analogy throughout. And the operation demonstrated is depression plus protection -- compression with
a floor -- which gives no purchase at all on centre-merging, the step MECH-018's own substrate note
flags as possibly missing from `integrate` and needed for readout (iii).

## Confidence

0.60. High source quality, a directly relevant computational result, but a deliberately high
transfer-risk penalty. The confidence sits above the naive component mean because what actually
transfers -- that selective, floor-preserving downscaling is a real neural operation and not a
convenient fiction -- is robust to most of the transfer risk that drags the components down.
