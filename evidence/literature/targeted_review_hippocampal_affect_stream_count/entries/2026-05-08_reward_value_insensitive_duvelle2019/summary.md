# Duvelle et al. 2019 — Insensitivity of Place Cells to the Value of Spatial Goals

**Source:** Journal of Neuroscience, [DOI 10.1523/JNEUROSCI.1578-18.2018](https://doi.org/10.1523/JNEUROSCI.1578-18.2018) (PubMed PMID 30696727). According to PubMed.

## What the paper did

Long-Evans rats performed a two-choice place-navigation task in which they could navigate to one of two unmarked goal locations and trigger reward delivery. The two goals delivered different reward amounts. The authors recorded single-unit activity in dorsal CA1 and CA3 while sampling place fields. The behavioural test was clean: did rats prefer the higher-value goal (yes — confirming they track value), and did the hippocampal place ensemble track that value (the empirical question)?

## Key findings relevant to the SD-011 generalization

Rats preferred the higher-value goal, confirming behavioural sensitivity to goal value. They replicated the modest goal-related ramping signal in the *out-of-field* firing of place cells during the reward-waiting period. Critically, place fields themselves were *not* modulated by goal value — neither in field rate nor in field location nor in goal-zone overrepresentation. The dorsal place ensemble forms what the authors call a "value-free map."

This is the necessary contrast for Gauthier & Tank 2018: the place ensemble itself does not absorb affect-channel information by simple firing-rate modulation. If the hippocampus tags affect streams, it does so through dedicated subpopulations (or via projection-specific cells, as Jimenez et al. show for anxiety), not by smearing valence across the generic place map.

## REE translation

The SD-011 generalization needs to take a specific architectural shape: privileged channels exist as identity-preserving subpopulations or projection-defined subsets, not as graded modulation of the spatial map. This sharpens the design question for V3/V4 — if we want goal/harm/social/anxiety streams to have hippocampal-map representation, we should not implement them as scalar overlays on z_world place codes. They need their own slots.

## Limitations and caveats

The negative result is restricted to dorsal CA1/CA3 single units in a goal-navigation task with two value levels. Ventral hippocampus, dedicated reward cells (a la Gauthier & Tank), and non-spatial CA1 cells were not the focus of this analysis. So the paper says "*generic* place cells do not track value" — it does not say "the hippocampus does not track value." That is exactly the architectural point: tracking happens in dedicated cells, not in the bulk ensemble.

## Confidence

0.74 — clean experimental design, clear behavioural anchor, dorsal-only sampling. The strength of this entry is that it constrains the *form* the SD-011 generalization can take. Confidence is moderated because the result is regional/cell-type specific and could be read either as "hippocampus is value-blind" (overreach) or "the bulk place map is value-free" (the supported reading).
