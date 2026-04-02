# Hirokawa et al. (2025) — A Cognitive Map for Value-Guided Choice in vmPFC

## What the paper does

This Cell paper reports single-unit recordings from macaque vmPFC during value-guided choice. The key finding challenges the standard view: vmPFC neurons do not simply encode chosen value or value difference (as fMRI studies suggest). Instead, they encode options as positions in a compositional reward-magnitude x reward-probability space — a cognitive map for value. Choice between options resembles trajectory navigation between locations in this 2D space, analogous to how hippocampal spatial maps support physical navigation.

## Relevance to ARC-041

ARC-041 proposes that E1's cue-indexed retrieval feeds E3's terrain precision scaling (MECH-152) — the cue context modulates how E3 weights harm and goal dimensions. The cognitive map finding is provocative: it suggests that the biological equivalent of E3's terrain weighting may operate through a structured representational space rather than simple multiplicative scaling.

If vmPFC represents options as locations in a value map, then ARC-041's terrain_weight signal [w_harm, w_goal] could be understood as defining the axes of this map — the cue context determines the coordinate system within which options are evaluated. This is architecturally richer than the current MECH-152 implementation (linear projection to 2D weights).

## A complication for ARC-041

The paper finds little evidence for explicit value-comparison codes during the choice period. This challenges the implicit assumption in MECH-152 that terrain weights directly modulate E3 scoring through multiplicative gating. The biological mechanism may be more about representational geometry (where options fall in value space) than about gain modulation (amplifying/suppressing harm vs goal channels).

## Confidence reasoning

Highest-tier venue (Cell), excellent methodology. Supports the principle that frontal value representations are structured and compositional (aligning with ARC-041's cue-weighting concept). Confidence moderated by the substantial differences between the experimental paradigm (discrete option choice) and REE's spatial navigation context.
