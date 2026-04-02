# DiCarlo & Cox (2007) — Untangling Invariant Object Recognition

## What the paper does

DiCarlo and Cox present a graphical framework for understanding the computational problem of object recognition. They argue that the core challenge is "manifold untangling": each object traces a complex manifold in pixel space as viewing conditions change, and the ventral visual stream progressively transforms these tangled manifolds into linearly separable representations in inferotemporal (IT) cortex. The key insight is that single-neuron invariance is not the goal — rather, the population code in IT achieves an "untangled" format where object identity can be read out by a simple linear classifier regardless of position, scale, or pose.

## Relevance to SD-015

SD-015 claims that goal-directed navigation requires a dedicated z_resource encoder that captures object-type features invariant to spatial location, separate from z_world. DiCarlo & Cox provide the canonical biological evidence for this design principle: the primate brain implements exactly such a separation, with the ventral stream (V1 → V2 → V4 → IT) progressively stripping spatial information to produce object identity representations, while the dorsal stream preserves spatial layout for action guidance.

The parallel is direct: z_world in REE encodes the full scene including agent position and spatial layout (analogous to dorsal/spatial processing), while the proposed z_resource encoder would extract what kind of resource is present independent of where it appears — analogous to ventral/IT object identity processing.

## Mapping caveats

The analogy is motivational rather than mechanistically tight. REE's CausalGridWorldV2 presents resource information in a structured channel (resource_field_view) — a 10x10 grid with explicit resource positions. The "untangling" problem is dramatically simpler than biological vision: there are no viewpoint transformations, occlusions, or lighting changes. A 2-layer MLP can likely extract resource type from this input without needing the hierarchical, multi-stage architecture that biology requires.

The deeper question is whether the *principle* — that goal representations must encode "what to seek" independently of "where it was" — transfers to REE's setting. The experimental evidence (EXQ-085 series) confirms it does: z_world at contact encodes the full scene and has no predictive value for future resource locations after respawn. This is the REE analogue of the position-dependence problem that the ventral stream solves.

## Confidence reasoning

High source quality (canonical review, >3000 citations). The principle of separating identity from location is well-established and clearly supports SD-015. Confidence is moderated by the gap between biological visual processing complexity and REE's grid world simplicity — the design decision is motivated by the principle but not mechanistically constrained by it.
