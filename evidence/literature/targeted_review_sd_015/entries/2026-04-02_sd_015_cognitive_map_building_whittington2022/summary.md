# Whittington et al. (2022) — How to Build a Cognitive Map

## What the paper does

Whittington, McCaffary, Bakermans, and Behrens review computational models of the hippocampal formation, distilling principles for how cognitive maps are constructed. The review covers the Tolman-Eichenbaum Machine, Clone-Structured Causal Graphs, successor representations, and related models. A key theme is how the hippocampus composes spatial structure with sensory/object identity to create maps that support flexible, goal-directed behavior. The review discusses landmark cells — hippocampal neurons that fire for specific objects irrespective of spatial location — and how these compose with place/grid cell spatial codes to enable navigation.

## Relevance to SD-015

SD-015 claims that goal-directed navigation requires a dedicated z_resource encoder that captures object-type features invariant to spatial location. Whittington et al. provide evidence that the biological navigation system implements a version of this principle: sensory/object identity enters the hippocampal map through a separate stream from spatial structure. Landmark cells encode "what is here" while grid/place cells encode "where am I" — and these are composed within the hippocampal formation for goal-directed planning.

This supports the core architectural claim: the navigation system needs separate object-identity and spatial inputs. You cannot derive "what to seek" from "where things were" when objects change location (as resources do after respawn in CausalGridWorldV2, and as objects do in natural environments).

## A complication worth noting

The review reports that in deep RL agents trained on navigation, 65.8% of hippocampal-analogue units develop conjunctive coding (modulated by both space and landmark position), while only 6.4% are pure landmark cells. This suggests that while the *input* streams may be separate, the *downstream* representation rapidly re-binds them. For REE, this implies E3's trajectory scoring may need z_resource and z_world jointly — the separation is at the encoder level (supporting SD-015), but the downstream consumer should receive both.

This is consistent with the experimental finding in EXQ-085l: ResourceEncoder successfully learns position-invariant features (C1/C3 PASS), but benefit_ratio remains low (C2 FAIL) because the action-selection integration does not properly compose z_resource with spatial planning.

## Confidence reasoning

High source quality (Nature Neuroscience, leading group). The compositional cognitive map framework directly supports SD-015's input separation claim. Confidence is moderated because the conjunctive coding finding subtly complicates the claim — the separation is necessary at input but insufficient alone, which is consistent with but not identical to SD-015's framing. Transfer risk from hippocampal models to REE's E3 is moderate.
