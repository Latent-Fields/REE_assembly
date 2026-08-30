# Gerber et al. 2014 -- pain-relief learning in flies, rats and man

## What the paper did

This is a six-author review pulling together three literatures that rarely sit on the same page:
Drosophila olfactory conditioning, rodent fear and relief conditioning, and human pain-offset
paradigms. Its organising move is a single observation, which the authors put memorably: a painful
event is *Janus-faced*. There are two things worth remembering about it -- what brought it about,
and what made it cease. Cues presented before a shock acquire negative valence and drive avoidance;
cues presented after the same shock acquire positive valence and are subsequently approached. The
review then asks how those two memories are organised relative to one another, and situates the
answer inside the threat-imminence model of defensive behaviour.

## What it says about SD-050

SD-050's architectural self-description is that it is "adjacent to MECH-091 but opposite polarity":
MECH-091 fires on an upward z_harm_a spike, SD-050 on a sustained downward drop. That is a design
decision, and until now it has been argued for rather than evidenced. This review is the biological
warrant for it, and the warrant is unusually strong because it is conserved across three phyla with
no shared neuroanatomy to speak of. Onset and offset are not two readings of one signed quantity;
they are two events, separately encoded, carrying opposite valence, and dissociable by the timing
of the cue relative to the aversive episode. A single signed readout off z_harm_a would not
reproduce that structure. Two comparators of opposite polarity would.

It is worth being precise about what this does *not* license, because the temptation to over-read a
convenient review is exactly how architectural claims acquire unearned confidence. The review
establishes that an offset event exists and is separately learnable. It says nothing whatsoever
about the detector form -- non-trainable, FIFO, rolling window, threshold on a latent norm. Those
are SD-050's actual content, and they remain unevidenced by this paper.

## Limitations and where the mapping strains

The strain is in the signal, not the architecture. Every paradigm reviewed here delivers an
electric shock with an experimenter-controlled offset: a step change back to baseline, sharp,
unambiguous, and externally scheduled. REE's z_harm_a is none of those things. Measured on
V3-EXQ-664 it spans roughly 7.18 to 7.42 within an episode -- a near-constant encoder offset with a
small functional component riding on it. A fly whose shock stops has a trough to detect. REE, on the
current substrate, does not. So this review supports the claim that there is something worth
detecting while leaving completely open whether it is detectable *here*, which is precisely SD-086's
territory and precisely why SD-050's falsifier is currently uninterpretable.

There is a second, quieter gap. In these paradigms relief valence is established by *conditioning a
cue* to the offset, not by the organism detecting the offset for its own sake. The detection is
inferred from the conditioning. A system that registered relief-completion but never paired it with
anything would show none of the reviewed effects, and the review gives no way to tell those two
architectures apart.

## Confidence

0.78. Source quality is high and the cross-phylum convergence is the sort of thing that earns
transfer credit rather than merely asking for it. Mapping fidelity is good for the polarity-pair
architecture and poor for everything else SD-050 asserts. Transfer risk is held at 0.35 -- moderate
rather than low -- entirely because of the step-change-versus-continuous-signal mismatch, which is
not a quibble but the live blocker on this whole claim.
