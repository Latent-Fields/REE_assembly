# Sleep preferentially consolidates negative aspects of human memory

## What the paper did

Denis, Sanders, Kensinger and Payne recruited over 250 participants -- deliberately many more than
this literature is accustomed to -- and ran a well-established scene-memory task across a sleep or
wake delay. Participants encode scenes in which an emotionally negative object sits on a neutral
background; memory for the object and for the background are then probed separately. The
long-standing claim in this area is that sleep does not merely preserve emotional memory but
selectively preserves it, trading away the neutral context it arrived in. That claim had been
challenged on exactly the grounds the authors name in their abstract: underpowered studies, mixed
results, poor generalisability. This paper is the replication that criticism demanded, and the
effect held. Sleep selectively benefited memory for negative objects at the expense of their paired
neutral backgrounds. A second large experiment asked whether the same held for positive material: it
did not. Positive objects were remembered better than their backgrounds, but sleep did not modulate
that difference.

## Why this bears on MECH-018

Of the six papers in this pull, this is the one that most directly measures what MECH-018 asks to be
measured. The claim's second readout is a specificity ratio: residue at harm contexts divided by
residue at equidistant matched non-harm contexts, with a pre-registered ceiling before sleep so that
over-generalisation is measurable, and a RISE after. Denis and colleagues have, in human behavioural
terms, that exact quantity -- retention of the emotional item over retention of its matched neutral
partner -- and they report that it rises across sleep and not across wake.

This matters for a second reason, which the claim itself flags. MECH-018's whole confirming design
turns on beating a NAIVE-DECAY arm: uniform multiplicative attenuation would satisfy the compression
and traversability readouts by violating the preservation one. A dissociation between two components
of the same encoded episode is the cleanest behavioural evidence that biological sleep is not doing
uniform decay. Whatever operates here is selective, and the selectivity is keyed to affective
salience. That is the right shape for `integrate` and the wrong shape for `discharge_domain`.

## Limitations, and one that cuts deeper than it first appears

Three caveats, in ascending order of seriousness. First, no polysomnography: this is a sleep-versus-
wake delay design, so it cannot say the effect belongs to REM or to slow-wave sleep, and it
therefore cannot speak to MECH-018's substrate question of whether an integration operation running
inside a cycle is what produces the effect. Second, the valence asymmetry is unexplained and
unpredicted. MECH-018's residue is a harm-signal field, so negative-specificity is convenient for
REE, but a claim that predicts a general salience-weighted operation should have predicted the
positive case too, and would have been wrong.

The third is the one I think governance should hold onto. The finding is a benefit "at the expense
of" the background. The specificity ratio rises partly because the numerator is held up and partly
because the denominator falls. A residue field could reproduce that signature by attenuating
everything, merely attenuating non-harm regions slightly faster -- which passes readout (ii) while
failing readout (i)'s preservation floor. MECH-018 already anticipates this by requiring a floor
check at the recorded harm z_world locations rather than assuming the field's own "cannot be erased"
invariant. This paper is a reminder that the two readouts have to be scored jointly and in absolute
terms, never as a ratio alone. A ratio is not a preservation proof.

## Mapping caveat

Object-and-background is an associative pair, bound by experimental construction. REE's
over-generalisation problem is geometric: RBF kernels centred on harm locations bleed into
neighbouring non-harm locations in z_world, and specificity has to be recovered against that metric
structure rather than against a designed pairing. The hard part of MECH-018 -- can integration
sharpen a field without erasing it -- lives in that geometry, which this paradigm does not have.

## Confidence

0.72. High source quality, a direct and well-chosen readout, and a result that is specifically a
replication answering the strongest published objection to this literature. Held back from 0.8 by
the absence of sleep staging and by the geometric mismatch between a scene-pair paradigm and a
continuous residue field.
