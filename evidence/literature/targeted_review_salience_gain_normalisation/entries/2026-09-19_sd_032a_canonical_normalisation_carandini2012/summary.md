# Normalization as a canonical neural computation (Carandini & Heeger, 2012)

## What the paper does

This is the field's anchor review for divisive normalization. Carandini and Heeger assemble the
case that normalization -- dividing a neuron's driving input by a common factor that includes the
summed activity of a pool of neurons -- is not a quirk of primary visual cortex but a computation
the brain reaches for repeatedly. They trace it from its origin as an account of V1 contrast
responses through the retina, the olfactory bulb of both flies and mammals, the modulatory effects
of visual attention, multisensory integration, and the encoding of value in decision-related
cortex. The claim is deliberately strong: normalization is *canonical*, in the sense that it is the
same operation applied to different problems rather than a family of superficially similar ones.

## The finding that bears on the question

The question this pull was commissioned to answer is narrow. In
`ree_core/cingulate/salience_coordinator.py` the SalienceCoordinator bounds an unbounded affinity
input with a hard symmetric box clamp -- `value = max(-cap, min(cap, value))` -- applied per-signal
before the per-mode affinity weight. The `mode-governance-engagement` substrate_queue entry is
titled for replacing that clamp with a saturating or normalizing operator. Does the biology
adjudicate?

On the operator *family*, it does, and cleanly. Every bounding operation Carandini and Heeger
document is smooth and saturating. Nothing in the survey is a truncation. This is not an
accident of measurement: the normalization form preserves a monotonic, if compressed, relationship
between input and output across the whole input range, whereas a clip maps every input above the
cap to the identical output. In REE's case that difference is not cosmetic. The V3-EXQ-935a
diagnostic found `ext_margin_mean` linear in cap at R-squared 0.9996-0.9999 on the seeds whose
external_task probability is near-constant -- which is the signature of an input that is *always*
at the cap, so the cap value, not the signal, is what the softmax sees. Under a saturating operator
that degeneracy cannot arise: two large-but-different dacc_pe values would still produce two
different logits.

## What it does not settle, and why that matters here

The honest reading stops short of endorsing the substrate build. Every system in this review is a
population of like-coded units -- orientation channels, odour channels, targets in a value map --
and the normalization pool is drawn from that population. REE's affinity_weights pool is a handful
of heterogeneous named scalars with incommensurate units: a prediction error, a foraging value, a
[0,1] engagement drive. The review licenses "saturating beats truncating"; it does not tell us
that the *pooled divisive* form, with its cross-signal coupling, is right for an aggregate control
variable feeding a four-way softmax over operating modes. Those are two different substrate
changes, and the entry's title currently does not distinguish them.

There is also a placement question the review quietly raises. Normalization as described operates
on a population *response* -- it is an output-stage or recurrent operation. REE's clamp is an
input-stage transform applied before the weights. A faithful import would normalize the mode logits
against each other, not bound each input signal independently. That is a larger and more
consequential change than the one the queue entry is titled for.

## Confidence

0.78. The source could hardly be better and the direction of the evidence is unambiguous within its
own domain. I have held it below 0.8 because the mapping does one real piece of work that the paper
itself does not do: carrying a principle established for sensory and value populations across to a
discrete control-plane gate. That carry is the thing the V3-EXQ-935 autopsy explicitly warned
against converting into a build ahead of the literature, and this entry is not, on its own, the
warrant for doing so.
