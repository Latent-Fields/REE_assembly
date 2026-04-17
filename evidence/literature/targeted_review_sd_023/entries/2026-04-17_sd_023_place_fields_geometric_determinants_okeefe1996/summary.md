# O'Keefe & Burgess 1996 -- Geometric determinants of place fields

## What the paper did

O'Keefe and Burgess (1996) recorded hippocampal CA1 place cells in rats placed inside rectangular boxes that varied systematically in the length of one or both walls. The experiment was designed to isolate which environmental features control the spatial firing fields (place fields) of hippocampal neurons. By holding all other factors constant and manipulating only wall geometry, they could determine whether place cells respond to global room shape, local wall distances, or some combination.

## Key findings

Place field position and shape are determined by distances from nearby walls. Each place field can be modelled as a sum of gaussian tuning curves, with each gaussian component oriented perpendicular to a particular wall and peaked at a fixed distance from that wall. When the box was stretched along one axis, place fields elongated proportionally. Even entirely neutral environmental geometry (walls with no reward or cue markings) structures the entire spatial map. A flat uniform environment produces poorly anchored spatial representations. Uninstructed geometric structure is necessary and sufficient to create a stable hippocampal spatial representation.

## REE translation

SD-023 argues that CausalGridWorldV2 requires neutral landmark objects with characteristic gradient fields to give world_obs environmental texture. O'Keefe and Burgess (1996) provides canonical biological grounding: in biological systems, the hippocampal world model is anchored to environmental features with no intrinsic reward value. A uniform environment produces poorly differentiated spatial representations. The same principle applies to E1's LSTM world model: a uniform world_obs provides no temporal or spatial structure for E1 to develop distinct state representations across locations. Adding gradient-emitting landmark objects is directly analogous to the walls that anchor place cell firing.

## Limitations

The evidence uses walls (extended planar boundaries) rather than discrete objects with gradient fields. The REE Landmark A/B design uses zone-bounded gradients, which are geometrically different from wall-perpendicular tuning curves. O'Keefe and Burgess (1996) addresses spatial encoding, not temporal prediction -- the claim that E1's LSTM will use gradient texture for temporal forward modelling requires extrapolation not directly evidenced here.

## Confidence reasoning

Source quality is extremely high (O'Keefe foundational place-cell work, Nature, Nobel Prize lineage). Mapping fidelity for the ecological principle (neutral environmental features structure hippocampal spatial maps) is good. Transfer risk is moderate because the REE use case is temporal LSTM prediction, not spatial map formation.
