# Barbano et al. 2016 -- LH GABA -> VTA, frequency-dependent feeding vs reward

According to PubMed ([DOI](https://doi.org/10.1523/JNEUROSCI.3799-15.2016)), Barbano and colleagues at the NIDA intramural program used selective optogenetic stimulation of GABAergic LH projections to the VTA in sated mice and asked whether this single pathway produces feeding, reward, or both, and how the two effects relate.

The clean result: stimulation at 5 Hz strongly induced eating with weaker reward; stimulation at 40 Hz strongly induced place preference (reward) with weaker feeding; intermediate frequencies produced intermediate effects on both. The two effects emerge from one anatomically defined projection, demultiplexed downstream by firing rate. Mean preferred duration of self-stimulation was 61.6 s for 40 Hz reward stimulation and 45.6 s for 5 Hz feeding stimulation.

For REE, this paper is informative not for what it directly shows about override but for what it constrains about the architecture of any LH-analog drive output. If a single broadcast pathway can carry two distinct computational signals demultiplexed by temporal pattern, then in V3 a single drive_level scalar can in principle perform double duty (seeding z_goal at one rate, modulating z_beta arousal at another) without requiring separate output channels. This is architecturally cheap and matches the spec's preference for parsimony.

The major caveat is that all experiments are in food-sated animals under exogenous optogenetic drive. Whether the same frequency-dependent mapping holds under endogenous hunger -- and whether it holds when the LH must override threat-driven AgRP suppression as in the de Araujo Salgado 2023 paradigm -- is untested here. So the paper supports broadcast-modulator architecture only indirectly.

Confidence 0.7. The mapping is suggestive rather than direct. I include this paper because LH-VTA is one of the canonical hypothalamic broadcast pathways, and its frequency-multiplexed behaviour is a useful constraint on REE's drive_level implementation.
