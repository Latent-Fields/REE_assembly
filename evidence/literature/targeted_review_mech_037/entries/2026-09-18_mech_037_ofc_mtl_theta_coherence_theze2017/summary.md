# Simultaneous reality filtering and encoding (Thézé et al. 2017)

## What the paper does

The starting observation is one of those that seems obvious only after someone says it: any
thought, whether it refers to the present or is an imagination, is itself encoded as a new memory
trace. So if the *result* of the online reality filter were encoded along with the thought, that
would explain how we later distinguish memories of real events from memories of imaginings without
any effort at all. The authors tested the timing this would require, using high-density evoked
potentials across two runs of a continuous recognition task built to impose encoding and
reality-filtering demands simultaneously. Encoding was indexed by the MTL-emanating signal to
immediately repeated stimuli; filtering by the ability to reject second-run stimuli that had not
yet appeared in that run.

Encoding set in at about 210 ms, some 35 ms before reality filtering; both ended at about 330 ms.
Both were characterised by increased theta-band coherence -- in the medial temporal lobe during
encoding, in orbitofrontal cortex during filtering. The authors propose an OFC-MTL interaction that
lets thoughts be re-encoded while they are being filtered, and suggest the combined influence at
200-300 ms leaves a trace that supports effortless later reality monitoring.

## Why it bears on MECH-037

Across the rest of this pull, the pattern is that everything REE nominates as an input to the fast
gate -- temporal ordering, source context -- turns out on measurement to be a slow process arriving
after the gate has already run. That is a problem for MECH-037, whose whole pathway is hippocampal
trace signal to precision down-weighting to commitment licensing. This paper is the one piece of
evidence pointing the other way: the medial temporal side *is* active inside the gate's window, and
is theta-coupled to the orbitofrontal filter across it. If MECH-037's pathway is going to survive
contact with the human literature, this is the mechanism it will have to lean on.

But I want to be precise about what the result licenses, because the temptation to over-read it is
strong. The MTL signal here indexes encoding of the thought currently being evaluated. It is not a
read-out of prior trace support for that thought. MECH-037's operational checklist says the gate's
inputs are "hippocampal trace presence, temporal ordering confidence, and recency flags" -- a
retrieval story. What this paper shows is closer to the opposite: the gate and the trace-writer are
running concurrently, 35 ms apart, ending together, and interacting.

## The architectural suggestion I think this carries

If the timing is right, the design REE should be considering is not "consult the trace store, then
license commitment" but something more coupled: commitment and inscription as one operation, with
the filter shaping what gets written rather than reading what was written. That is interesting
because it is *already in* `papez_circuit.md`, under the affective retrieval-augmentation heading --
"precision- and valence-modulated retrieval under viability constraints before E3 commitment" --
and it does not match the operational checklist a few lines above it. The claim currently contains
two architectures. This paper favours the second one. Resolving which REE means is a prerequisite
for writing a falsifier that could fail.

## Limitations and confidence

This is the most speculative entry here and I have weighted it accordingly. The abstract does not
state N. Attributing scalp-EEG theta coherence to the medial temporal lobe is a strong claim from a
method with poor depth resolution. Coherence establishes coupling and not direction, so nothing
here licenses "MTL gates OFC" over the reverse or over a common driver. The authors themselves
present the interaction as a proposal -- the title ends in a question mark, which I take as an
honest signal rather than a stylistic one. And the target construct, reality *monitoring* of past
events, is adjacent to rather than identical with the online commitment gate MECH-037 describes.
Confidence 0.58, direction `supports`: it supports the existence of the pathway the claim needs,
weakly, and in a form that would require the claim to be rewritten before it could be tested.
