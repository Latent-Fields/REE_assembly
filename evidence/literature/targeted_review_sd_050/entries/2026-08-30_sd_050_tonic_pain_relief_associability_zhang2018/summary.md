# Zhang et al. 2018 -- relief learning under tonic pain, and what governs it

## What the paper did

Two human experiments, static and dynamic escape-learning paradigms, in which subjects learned to
terminate an ongoing tonic pain state. Behavioural, physiological and fMRI data were fitted with
reinforcement-learning models. Active relief-seeking turned out to be an RL process with prediction
errors in dorsal putamen. The result the authors foreground, however, is upstream of that: an
uncertainty or *associability* signal in pregenual anterior cingulate cortex both sets the relief
learning rate and, remarkably, endogenously and parametrically modulates the level of ongoing tonic
pain. The circuit reduces the pain while learning about how to escape it.

## Two readings, pulling in opposite directions

This is the only paper in the pull that engages the regime REE is actually in. Every other relief
study here uses a shock with a clean offset. Zhang and colleagues use *tonic* pain -- sustained,
slowly varying, closer in character to a z_harm_a that sits between 7.18 and 7.42 and refuses to
move. So the first reading is supportive, and it matters: relief remains a discrete, separately
signalled, learnable event even when the aversive background is tonic. The near-constancy of REE's
harm channel is therefore not by itself grounds to abandon the relief-completion event. Whatever is
wrong with SD-050's falsifier, it is not that relief events are meaningless under tonic aversion.

The second reading cuts the other way, and cuts at the specifics. SD-050's comparator is
*non-trainable*: a fixed rolling window, a fixed drop threshold, a fixed minimum initial norm, all
applied to a latent norm. The quantity that governs relief learning in this study is nothing like
that. It is a learned associability signal -- an adaptive estimate of how predictable the relief
currently is -- which modulates its own sensitivity as learning proceeds. That is an argument, and a
reasonably direct one, for SD-086's proposed trained scalar head over SD-050's fixed FIFO. It is
falsifier branch (c) in the claim's own `what_would_answer` field, arriving from the literature
rather than from an experiment.

## The bidirectional coupling, which the comparator cannot express

One detail deserves separate mention because it is easy to skim past. The pgACC signal does not just
read the pain -- it *modulates* it. Relief learning and pain level are coupled in both directions.
SD-050's comparator is strictly feed-forward off z_harm_a; it observes and cannot write back. If it
turns out that REE's harm channel becomes non-degenerate only when something downstream is allowed
to modulate it -- if the flatness is partly a consequence of nothing ever pushing back -- then the
comparator is architecturally incapable of producing the conditions it needs to fire. I do not think
that is established, and I am not asserting it. But it is a hypothesis this paper makes available
and SD-086's saturation investigation has not yet ruled out.

## Limitations

The gap I keep returning to is that this study models relief *learning* -- acquiring escape
behaviour and the RL signals that support it -- while SD-050 specifies relief *detection*, deciding
that a period of suffering has ended. The comparator sits upstream of everything modelled here. So
the weakening force of this entry is an argument about detector form, not a measurement of SD-050's
detector, and I have scored mapping fidelity at 0.55 to say so. The association between a pgACC
associability signal and a trainable head on z_harm_a is conceptual; human thermal pain tells us
nothing directly about whether an artificial latent norm carries analogous structure.

## Confidence

0.66, filed as `mixed` rather than forced to `weakens`. The tonic-regime survival of relief events
is genuine support for SD-050's premise, and collapsing that into the detector-form objection would
misrepresent what the paper shows.
