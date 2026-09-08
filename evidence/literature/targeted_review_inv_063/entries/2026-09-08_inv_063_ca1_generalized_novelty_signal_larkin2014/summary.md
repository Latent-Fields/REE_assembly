# CA1 broadcasts a generalized novelty signal (Larkin, Lykken, Tye, Wickelgren & Frank, 2014)

## What the paper did

Larkin and colleagues recorded simultaneously from hippocampal CA1 and CA3 in freely behaving rats
performing an object-place recognition task, and introduced novelty in two forms: familiar objects
moved to new locations, and novel objects in unexpected places. They asked what pattern of
hippocampal activity supports the animal's well-documented behavioural preference for exploring
what has changed.

Three findings, and the order matters. Novelty substantially altered CA1 activity but left CA3 -- one
synapse upstream -- essentially unchanged. The CA1 place-cell firing-rate increases persisted during
sharp-wave ripples, the windows in which stored experience is replayed. And, unexpectedly to the
authors, the increases were not confined to the regions of the environment that had actually changed.
Their conclusion is stated crisply: CA1 broadcasts the *presence* of novelty rather than signalling
*what* is novel, while simultaneously becoming more plastic.

## Why this entry is marked mixed rather than supporting

Both directions here are real, and collapsing them into one label would misrepresent the paper.

On the supporting side, INV-063's leg A predicts that as environmental intake falls, surprise-gated
replay has progressively less to prioritise -- and the mechanism that would have to be true for that
prediction to be coherent is that environmental novelty modulates the material available to replay.
This paper shows exactly that, and shows it at the right place: the rate elevation persists *into
sharp-wave ripples*. That is the biological counterpart of what our MECH-205 instrument measures when
it counts VALENCE_SURPRISE residue writes and reads the realised surprise weight at the replay call.
It is reassuring that the instrument is pointed at something with a genuine analogue.

On the weakening side -- and this is why I think the entry matters more than a straightforward
supporting citation would -- INV-063 asserts four *function-specific* thresholds, each insufficiency
starving a different offline function. A generalized broadcast is close to the opposite architecture.
It is undifferentiated: novelty is present, the system becomes more plastic everywhere, and the
downstream consumers are not separately addressed. That is F3, the third pre-registered falsifying
outcome in our own what_would_answer: both legs degrade in lockstep, the specific content is
unsupported, and what survives is "less input, less offline benefit", which the claim text itself
describes as close to trivial. Finding that outcome already reported in the mammalian system the
claim is modelled on should raise our prior on F3 before we run anything.

## The mapping I am not entitled to

The generalization result is about *spatial* specificity -- was the elevated firing confined to the
changed locations? INV-063's specificity claim is across *functions* -- do Types 1/2 replay and E1
world-model updating have separate thresholds? Those are different axes, and I am arguing by
structural analogy: a system that does not resolve novelty by location at the replay-eligible stage
seems unlikely to resolve it by downstream consumer. That is a reasonable prior and it is not a
demonstration, and this entry should be cited as raising the prior on F3 rather than as establishing
it. It is also waking ripple activity, not NREM sleep replay, and there is no memory-performance
dependent variable anywhere in the design.

## One design warning worth carrying forward

The novelty modulation was present in CA1 and absent in CA3, one synapse apart. Where in a
processing hierarchy you read the intake signal determines whether you see it at all. For our leg B
-- across-sleep improvement in world-forward prediction error -- that means a flat result would not
by itself distinguish "no starvation effect" (the F1 outcome) from "measured one stage too early in
the E1 pathway". Worth pre-registering which readout point we consider diagnostic, before the run
rather than after.

## Confidence

0.55, over an entry that genuinely bears both ways. Source quality is high (0.82): simultaneous
CA1/CA3 recording from Loren Frank's laboratory, with the CA3 null acting as an internal specificity
control rather than leaving the CA1 effect isolated. Mapping fidelity (0.55) is limited by the axis
mismatch above. The number should be read as "this is solid evidence that cuts both ways", not as
uncertainty about what the paper found.

According to PubMed: [DOI 10.1002/hipo.22268](https://doi.org/10.1002/hipo.22268), PMID 24596296,
PMC4065199.
