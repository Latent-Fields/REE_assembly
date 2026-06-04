# Kovach et al. 2012 -- Frontopolar cortex credits recent reward trends to update the active model

**Claim touched:** ARC-063 element (iv), specifically the recency-weighted credit channel the refinement loop needs. Cross-ref MECH-309.

## What the paper did
Eight patients with anterior-prefrontal (frontopolar, FPC) lesions and healthy controls performed a four-armed bandit. Model-based analysis revealed a selective deficit: the lesion group could not extrapolate the *most recent* reward trend (the comparison between the two latest outcomes that controls used to anticipate the next), yet their general ability to learn from cumulative past reward was intact. The authors propose FPC selects and updates models of reward contingency in dynamic environments.

## Why it matters for ARC-063
ARC-063's waking refinement (split/merge/retire rules) acts on *recent* evidence -- a rule that has just started accumulating exceptions should lose availability before its lifetime statistics shift. That requires a recency-weighted credit channel distinct from slow cumulative accumulation. Kovach shows the brain factors exactly these apart, and localises the recent-trend, model-updating credit to frontopolar cortex. This grounds the *frontal substrate* for crediting the currently-active rule/model on recent outcomes -- the channel that makes ARC-063's evidence traces actionable for fast refinement rather than only slow consolidation.

## The honest caveat
What FPC credits is a reward-*contingency model*, not a labelled rule object; the mapping treats "active contingency model" as the analog of "active CandidateRule", which is defensible but an extension. And the rule-level inference is lesion/correlational, not a direct mechanistic readout of rule-credit. I have set the direction to *mixed* and confidence mid accordingly: it supports the existence and frontal localisation of a recency-weighted credit channel, while not demonstrating credit to a discrete rule.

## Confidence
0.55 -- mixed. Grounds the recency-weighted, model-updating credit channel (and its dissociation from cumulative learning) that ARC-063 needs, with the contingency-model-vs-rule-object gap kept explicit.