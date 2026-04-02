# Rolls (2021) — Learning Invariant Object and Spatial View Representations in the Brain Using Slow Unsupervised Learning

## What the paper does

Rolls presents the VisNet computational model showing how the brain learns two fundamentally different types of invariant representation through the same slow unsupervised learning principle: (1) position-invariant object representations in the ventral visual stream (IT cortex), and (2) allocentric spatial view representations in the parietal cortex and posterior cingulate cortex. Both types of representation are then available to the hippocampus for episodic memory and spatial navigation. The model demonstrates that hierarchical competitive learning with temporal continuity constraints naturally produces these separate invariant codes.

## Relevance to SD-015

SD-015 claims that goal-directed navigation needs a separate z_resource encoder for position-invariant object features, distinct from z_world. Rolls' model provides direct computational-neuroscience support: the brain implements exactly this architectural separation, with ventral stream object identity representations and dorsal/parietal spatial representations converging on hippocampus as separate inputs. Crucially, Rolls shows that both streams feed the same downstream system (hippocampus/navigation) but encode qualitatively different information — what an object is versus where things are in allocentric coordinates.

This maps onto REE's architecture where z_resource (what kind of resource, invariant to location) and z_world (full scene spatial layout) would both feed E3's trajectory scoring, but carry non-redundant information necessary for goal-directed approach.

## Mapping caveats

The learning mechanism differs substantially. Rolls' VisNet uses slow unsupervised learning exploiting temporal continuity in visual experience — objects move smoothly, so representations that change slowly are invariant. REE's ResourceEncoder is trained with supervised or BCE objectives on structured grid observations. The architectural principle transfers (separate encoders for what vs where), but the claim that this separation naturally emerges from unsupervised learning does not apply to REE's supervised training regime.

Additionally, Rolls' spatial representations are allocentric (world-centered), while z_world in REE is an egocentric observation centered on the agent. The coordinate frame difference means the specific computational challenges differ.

## Confidence reasoning

Rolls is a leading figure in computational models of ventral stream processing. The paper directly addresses the what/where separation and its role in hippocampal navigation — closely aligned with SD-015's architectural claim. Confidence is moderated by the learning mechanism gap and the coordinate frame difference.
