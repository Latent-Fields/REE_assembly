# On the role of population heterogeneity in emergent communication (Rita, Strub, Grill, Pietquin & Dupoux, ICLR 2022)

## Why this entry exists

The Galke et al. 2022 entry in this directory reported that the group-size effect "does not fully replicate" in neural agents, and the entry's own limitation section flagged that this phrase was doing quiet work -- unquantified, with no statement of which simulations were compared against which human studies, and no way to tell a measured failure from an untested assumption. This is the paper the phrase points at. The failure is measured.

## What the paper did

A population-based Lewis reconstruction game: a speaker sees an object with four attributes, emits a message, and a listener must reconstruct every attribute. Populations are built as N speakers plus N listeners, with one of each sampled uniformly at random at every training step. LSTM agents, Adam, policy-gradient speaker objective, six seeds per configuration, public code. The authors are explicit about the target: "we adopt a setting close to Raviv et al. (2019a)'s when computationally modeling human population."

They then measured four things against population size: speaker synchronisation, negative entropy, topographic similarity (their compositionality proxy) and test-set generalisation.

## What it found

Nothing, or slightly worse than nothing. Spearman correlations with population size: **-0.44, -0.15, -0.52, -0.14**. Synchronisation and compositionality stayed roughly flat; entropy and generalisation deteriorated. Variance across seeds did not shrink either, so the large-group consistency effect that is so striking in the human data is absent too. Their summary is blunt and worth quoting because it is the fact this pull was sent to establish: "we empirically show that the community size is not a structuring factor in language emergence by or in itself in the classic homogeneous Lewis setting."

Then the repair. They asked what the simulation assumes that human communities do not, and answered: homogeneity. Every agent trains at the same rate, with the same capacity, under the same sampling. When they varied learning speed -- first as a speaker/listener ratio in a minimal N = 2 population, then distributed log-normally across a larger population -- the group-size effect appeared. And the controlling variable was **relative**, not absolute: "emergent language properties are only altered by the relative difference of learning speeds between speaker and listener, and not by their absolute values."

## What this does to ARC-099

**The satisfiable-but-inert worry is confirmed, with numbers.** ARC-099 is not a mechanism claim; it is an enumerated contract, and the worst thing that can happen to such a contract is that an item passes while delivering nothing. That is what a Spearman of -0.15 on compositionality against population size means. A V6 ecology that instantiates partner variation by adding more identically-configured agents is the exact configuration measured here.

**But the missing ingredient is of a kind the inventory has no instance of.** This is the finding that should change how ARC-099 is amended, and it is a different finding from the two Galke et al. proposed. What was absent was not a capability -- not memory, not attribution, not repair. It was a property of the population's *learning dynamics*: speakers and listeners adapting at different relative rates. Every one of ARC-099's fourteen items is a capability or an ecology feature checkable by inspection. None of them is a statement about how fast the agents in the ecology learn relative to each other. If Rita et al. are right, a gate that certifies all fourteen and is silent about learning-rate asymmetry will pass an ecology that cannot bootstrap, and will pass it cleanly.

**Two of the paper's stated design assumptions are themselves evidence for Galke et al.'s reading.** The authors list four homogeneity assumptions built into the standard population game. One is that "agents cannot be differentiated, i.e., agents have no information about the identity of their partners" -- so what these simulations call partner variation is variation among anonymous, interchangeable partners, which is not what a human in Raviv's experiment experiences at all. The other is structural: N speakers and N listeners are disjoint sets, so no agent ever occupies both roles. Role alternation is not tested and found unnecessary here; it is absent by construction. Galke et al. were right that this is how the field builds these things, and one can see it in the method section of the paper that measures the null.

## What the pull was asked to establish, answered

*Is the failure to replicate in neural agents measured or asserted?* Measured, here, in the homogeneous Lewis setting, with correlations and seeds reported. But the broader literature is mitigated rather than uniformly null, and this paper is the honest place to see that: Tieleman et al. 2019 report a small but consistent regularisation effect from populations, Cogswell et al. 2019 a slight compositionality gain in some settings, Graesser et al. 2019 no correlation at all. "Fails to replicate in neural agents" is a fair summary of a mixed and under-powered literature, not a settled fact -- and it is now accompanied by a demonstration that the effect can be made to appear on demand.

## Limitations

One game family, one architecture family, populations up to about twenty per role, six seeds. Compositionality is measured by topographic similarity, which Chaabouni et al. 2022 report stops correlating with generalisation in larger and more complex settings -- so a null on that metric is softer evidence than it looks. And the diagnosis cuts against over-reading the null: if the failure is an artefact of how this subfield models populations, a V6 ecology built differently might never have had the problem. That is a reason to treat the result as a warning about a specific construction, not as a law about artificial agents.

## Confidence

0.77, `mixed`. Source quality 0.72, mapping fidelity 0.80, transfer risk 0.35. Mixed because the paper both confirms the worry and dissolves it: the human condition does not transfer by default, and does transfer once a further property is supplied. The transfer risk is the lowest in this directory because nothing has to cross a species boundary -- an artificial ecology reasoning about artificial ecologies is as short an inference as this pull offers.
