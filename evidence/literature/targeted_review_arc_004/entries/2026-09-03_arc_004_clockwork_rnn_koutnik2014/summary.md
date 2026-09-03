# A Clockwork RNN

Koutnik, Greff, Gomez & Schmidhuber (ICML 2014) modify the standard RNN by partitioning the
hidden layer into modules, each of which processes input at its own temporal granularity and
computes only at its prescribed clock rate -- module `i` updating every `2^(i-1)`-th step.
The spacing is hand-set and exponential, not learned. The result is a network with *fewer*
parameters than a standard RNN, faster evaluation, and better performance on the two tasks
tested (audio signal generation and TIMIT spoken-word classification), where it outperformed
both RNN and LSTM baselines.

ARC-004 carries two separable assertions, and this paper cuts opposite ways on them, which is
why it is logged as mixed rather than pushed into one direction. On the first -- that L-space
is layered and differentiated -- it is support, and reasonably good support: explicitly
stratifying a recurrent state by temporal granularity is functionally worth doing, and it
buys both accuracy and parameter efficiency. That is a design-level argument for why a
multi-timescale latent stack is a sensible architectural commitment in the first place, which
is the half of ARC-004 the 2026-09-01 governance disposition kept.

On the second -- that the differentiation is *by timescale*, in the specific emergent sense
ARC-004's precondition demands -- it bears against. CW-RNN got its multi-timescale behaviour
by prescribing the rates. That is precisely the built-in rate split the precondition
explicitly disclaims, and the paper offers no evidence that comparable stratification arises
from architecture alone at a shared rate. Placed beside Chaudhuri et al. 2015 in this same
pull -- identical time constants, graded connectivity, serial hierarchy, emergent hierarchy
-- the two bracket the open question rather neatly. Prescribing rates is one sufficient
route. Serial coupling with a structural gradient is another. A shared-rate *parallel* stack,
which is what `LatentStack.encode` currently is, is on neither.

I want to be careful not to over-read the negative half, because the temptation is real. The
paper never ran a shared-rate control. It therefore establishes that prescribing rates
*works*; it does not establish that emergence *fails*. Reading its silence as a negative
result about emergence would be exactly the kind of over-claim the ARC-004 record has already
had to correct once, when the MECH-058 precedent was found to be wrong in three respects.
Treat this as one route demonstrated, not another route refuted.

The distance is also structural. Updating a module every `2^(i-1)` steps is a hard gate on
updates -- nothing like an exponential moving average with a smoothing constant -- so the two
architectures mean different things by "setting a timescale", and the comparison is between
routes rather than between matched systems. The tasks are supervised sequence problems from
2014 with era-appropriate baselines; nothing here concerns latent world-models, unsupervised
representation stacks, or the autocorrelation-persistence measure ARC-004 specifies.

Recorded as `mixed` at 0.58.
