# Reward value-based gain control: divisive normalization in parietal cortex (Louie, Grattan & Glimcher, 2011)

## What the paper does

Louie and colleagues recorded from single neurons in macaque lateral intraparietal cortex while
manipulating the reward values associated with saccade targets. The design lets them ask a sharp
question: does an LIP neuron encode the value of the target in its response field absolutely, as
rational choice theory would assume, or relative to the values of the alternatives on offer? The
answer is unambiguously relative. The response to a fixed in-field value falls as the value of
out-of-field targets rises, the effect appears in baseline firing as well as in stimulus-driven
activity, and the functional form that captures it is divisive normalization -- the same equation
that describes contrast gain control in visual cortex.

## Why this one matters more than the sensory literature

The V3-EXQ-935 autopsy's stated hazard for this pull is that a reviewer returns papers about
divisive normalization in early sensory cortex and transports them to an aggregate control-plane
salience vector. This paper is the closest thing in the corpus to a rebuttal of that hazard, because
its subject is already a decision circuit. LIP is not computing contrast; it is computing something
that feeds action selection. If the brain's solution to "this input's dynamic range would otherwise
swamp its competitors" is adaptive divisive gain control even in a value-coding decision area, then
the burden of argument shifts: a hard truncation in REE's SalienceCoordinator is the unusual choice,
not the conservative one.

The specific bearing on MECH-259 is worth stating precisely. MECH-259 says the coordinator fires a
whole-system mode switch when precision-weighted salience of an input exceeds a threshold. A
threshold test is only as informative as the quantity it tests. If the affinity input has already
been clipped at the cap, then every sufficiently large input is indistinguishable from every other,
and the threshold can only report "at ceiling". The V3-EXQ-935a measurement -- `ext_margin_mean`
linear in cap at R-squared 0.9996-0.9999 for the near-constant-probability seeds -- is that failure
mode caught in the act: the margin is tracking the *parameter*, not the signal. Louie et al. show
that the biology does not make this trade; it compresses instead.

## Where it stops, and the cost it also documents

Two mismatches keep this below a strong endorsement. LIP's normalization pool is the set of
available targets -- the very things being chosen -- and that pool changes from trial to trial,
which is where the adaptive-range benefit comes from. REE's mode set is fixed at four, so an
input-side normalization inherits none of that. And firing rates are non-negative, whereas REE's
affinity input is signed and its current clamp is symmetric about zero; the sign-preserving
saturating form REE would actually need is not the operation validated here.

The paper also, with some candour, names its own cost. The authors close by observing that
normalization in decision circuits "provides a possible mechanistic basis for behavioral
context-dependent violations of rationality". That is not a caveat bolted on by me; it is the
mechanism's known downstream consequence, and the next entry in this review is the group's own
demonstration of it.

## Confidence

0.76. Strong, direct, well-placed evidence for the operator family in a decision circuit, discounted
for a pool mismatch and a sign mismatch that a build would have to resolve by design choice rather
than by reading this paper.
