# Omer, Maimon, Las & Ulanovsky 2018 — Social Place-Cells in the Bat Hippocampus

**Source:** Science, [DOI 10.1126/science.aao3474](https://doi.org/10.1126/science.aao3474) (PubMed PMID 29326274). According to PubMed.

## What the paper did

Egyptian fruit bats were trained on a spatial observational-learning task in which an observer bat watched a demonstrator bat navigate to a goal location, then mimicked the route. The authors recorded single units in dorsal CA1 of the observer bat while it tracked the demonstrator. The experimental question was sharp: does the observer's hippocampus represent the position of the *other* bat, and if so, is that representation distinct from how it represents inanimate moving objects?

## Key findings relevant to the SD-011 generalization

Three results stack:

1. *Social position is encoded.* A subpopulation of dorsal CA1 neurons represented the position of the other bat, in allocentric coordinates.
2. *Self/other are partially shared.* About half of these "social place cells" also represented the observer's own position — i.e. they doubled as classical place cells. The other half were dedicated to social position.
3. *Social ≠ inanimate.* Some neurons encoded the position of inanimate moving objects, but their representation was distinct from the conspecific representation. So social tracking is not a byproduct of generic moving-object encoding — it has its own cell-class.

This identifies social/conspecific position as a third privileged map channel beyond reward (Gauthier & Tank) and fear (Moita 2004).

## REE translation

For the SD-011 generalization, social position is the cleanest non-affective channel that nonetheless gets dedicated map slots. It complicates the "affect-channel" framing: the privileged-channel mechanism may not be specific to valence at all, but to *behaviourally relevant object classes more broadly*. Conspecifics happen to be among the most behaviourally relevant objects in a social species, so they get a slot. Reward, threat, anxiety, and conspecific-position are then four members of a more general "behaviourally privileged channel" set.

For V3/V4, this argues that the architectural slot logic in SD-011 (z_harm_s + z_harm_a) might be one instance of a broader pattern: the hippocampal map admits N parallel channels, where N is determined by what classes of object are behaviourally privileged enough to merit their own population. This widens the design space beyond "affect channels" to include any class of high-relevance object.

## Limitations and caveats

Bats are an unusual model — echolocation provides exceptionally precise allocentric position estimates that may not transfer to species without that sensory advantage. The observer-demonstrator paradigm is constrained: only one demonstrator, no distractors, no aversive component. Whether the social-place-cell population scales to multiple conspecifics or to social *valence* (familiar vs novel, dominant vs subordinate) is unaddressed. The companion paper Danjo 2018 in rats addresses some of these.

## Confidence

0.80 — Science paper, careful controls, replicated across observers. Transfer risk slightly elevated by bat-specifics but the core architectural claim (social position has dedicated map cells) is convincing.
