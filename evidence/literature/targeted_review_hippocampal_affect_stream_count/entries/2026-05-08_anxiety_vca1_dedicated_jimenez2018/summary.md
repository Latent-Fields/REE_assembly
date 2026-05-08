# Jimenez et al. 2018 — Anxiety Cells in a Hippocampal-Hypothalamic Circuit

**Source:** Neuron, [DOI 10.1016/j.neuron.2018.01.016](https://doi.org/10.1016/j.neuron.2018.01.016) (PubMed PMID 29397273). According to PubMed.

## What the paper did

The authors used freely-moving Ca2+ imaging and projection-target-specific optogenetics in mice to dissect what ventral hippocampus does during anxiogenic experience. They imaged dorsal CA1 (which is canonically place-cell territory) and ventral CA1 (which has been linked to mood and emotion), and they used target-defined viral strategies to image cells defined by whether they projected to the lateral hypothalamic area (LHA) versus the basal amygdala (BA).

## Key findings relevant to the SD-011 generalization

Three results stack:

1. *Dorsal/ventral split.* Dorsal CA1 is enriched in classical place cells; ventral CA1 is enriched in "anxiety cells" — cells activated by anxiogenic environments (open arms of an elevated plus maze, open field) and required for avoidance behaviour.
2. *Projection-target specificity.* The anxiety cells are enriched in the vCA1 population projecting to LHA — *not* the population projecting to BA. Same source region, different downstream channels, different functional identity.
3. *Causal pathway dissection.* Optogenetic activation of vCA1->LHA terminals increased anxiety and avoidance, while activation of vCA1->BA terminals impaired contextual fear memory. The two pathways are functionally separable.

This identifies anxiety/sustained threat as a distinct affect channel from acute fear (Moita 2004) and from reward (Gauthier & Tank 2018), with its own anatomical substrate.

## REE translation

For the SD-011 generalization, this is the most important architectural finding in the lit-pull. It says:

- *The hippocampal map is multi-channel along multiple axes simultaneously.* Channels can be defined by subregion (dorsal vs ventral), by projection target (LHA vs BA), and by identity-preservation across remapping (Gauthier & Tank). These are independent design dimensions.
- *Anxiety encoding is "modulated firing" not remapping.* These cells fire more in anxiogenic environments — their identity isn't tied to a specific place field that reorganizes. This widens the architectural taxonomy: the count of map-tagged affect channels depends on whether you require remapping or accept modulated-firing-by-projection-target.

For V3/V4, this argues that affect channels in our latent architecture should be characterized by both the source-side identity (z_harm_a vs z_harm_s in SD-011) and the projection-side write-channel (which downstream module receives the signal — analogous to LHA vs BA). The SD-011 architecture currently focuses on source-side identity; the projection-side dimension is largely unexploited.

## Limitations and caveats

Anxiety cells in this paradigm show modulated firing rather than canonical place-field remapping. By a strict remapping criterion, anxiety doesn't qualify as a privileged map channel; by a dedicated-population-with-projection-specificity criterion, it does. The paper does not record across days to test whether the anxiety encoding stabilizes, so the persistence question (cf. Wang 2012 for fear) is open.

## Confidence

0.82 — high-quality Neuron paper with optogenetic causal manipulation. Mapping fidelity to the SD-011 generalization is bounded by the fact that the encoding mechanism (modulated firing) differs from the reward/fear remapping cases. This is exactly the architectural complication the SYNTHESIS needs to address.
