# Schomers, Garagnani & Pulvermuller (2017) -- Neurocomputational Consequences of Evolutionary Connectivity Changes in Perisylvian Language Cortex

**Claim tested:** MECH-038 (arcuate-like sequence-to-motor channel nudges language emergence)
**Direction:** supports | **Confidence:** 0.78

## What the paper did

Schomers and colleagues built two neurobiologically constrained networks of perisylvian cortex that are identical in
every respect except one: their long-range connectivity. The first replicates the connectivity pattern established by
macaque tract-tracing -- essentially a chain of next-neighbour links between auditory and articulatory-motor areas. The
second adds the human-specific "jumping links": direct higher-order connections between *non-adjacent* areas, the
structural signature of the expanded human arcuate fasciculus. Both networks were then trained on auditory-articulatory
patterns, and the question was what function emerged.

Only the human-connectivity network developed verbal working memory -- the capacity to hold a syllable or word form in
reverberant activity after the input has gone. The control point I find most persuasive is the negative one: giving the
monkey-connectivity network *more training* did not produce the capacity. It is not a learning-rate story. What the
human links buy is reduced sensorimotor path length, and path length is what the emergent function turns out to depend
on.

## How this bears on MECH-038

MECH-038 is, stripped down, a routing claim: that a fast channel from sequence representations into motor affordances
predisposes a system toward symbolic use, without adding a language module. This paper runs that manipulation. It holds
architecture, training regime and capacity fixed and varies only whether the fast route exists. That is an unusually
clean prior for the ON-versus-LESION arms MECH-038 specifies, and it says the contrast should be non-null, for the
reason the claim gives (path length), rather than for some confounded reason (more parameters, more compute).

It also gives the REE build a hint about *where* to put the channel. In the model, what the jumping links connect is
auditory sequence representation to articulatory motor pattern. The REE analog named in the claim -- multi-content theta
packet into E2 affordances over signalling actions -- is the same shape, and this paper suggests the shortening of the
path is the operative variable rather than the bandwidth per se.

## Limitations and where the mapping strains

The dependent variable is verbal working memory in a single network. MECH-038's readouts are all inter-agent:
referential consistency against a shuffled-referent baseline, coordination success rate, time-to-first-consistent-use.
There is no second agent here, no referent, and no coordination pressure, so nothing in the paper speaks to whether
sequence-maintenance capacity converts into emergent *communication*. Having the substrate for symbol handling and
using symbols to coordinate with another agent are not the same achievement, and the gap between them is precisely
where REE's own experiment would have to do its work.

There is a second tension worth stating plainly rather than smoothing over. MECH-038 predicts a *nudge*: the lesioned
arm should still show some emergence, just less and later. In Schomers et al. the monkey-connectivity network shows
essentially none of the target capacity, and no amount of training rescues it. Read literally against the claim's own
criteria, that is the "required module" pattern listed as *falsifying* the nudge framing. I do not think it settles the
question -- a modelled capacity either forms or does not, whereas a coordination behaviour can partially succeed, so
the all-or-nothing shape may be an artefact of what is being measured. But it is a real signal that the dorsal channel
may be more load-bearing than "nudge" concedes, and the REE experiment should be powered to detect that outcome rather
than assume it away.

## Confidence reasoning

Source quality 0.85: J Neurosci, an established modelling line, and the negative control (extra training does not
substitute) is the kind of thing that makes a simulation result worth taking seriously. Mapping fidelity 0.75, high by
the standards of this corpus because the manipulation genuinely is the claim's manipulation. Transfer risk 0.35: this
is model-to-model transfer between two architectures that share no implementation, which is not obviously safer than
animal-to-human. Aggregate 0.78, weighted toward mapping fidelity as the claim is architectural.
