# de Boer, Kroese, Mannor & Rubinstein 2005 - A Tutorial on the Cross-Entropy Method

[DOI](https://doi.org/10.1007/s10479-005-5724-z) - *Annals of Operations Research* 134(1):19-67.

## What the paper did

This is the canonical tutorial treatment of the Cross-Entropy method. The paper presents CE/CEM as a stochastic optimization method: sample candidate solutions from a parameterized distribution, score them, select an elite subset, and update the sampling distribution toward the elite subset. It covers the method's use in combinatorial optimization, multi-extremal optimization, rare-event simulation, and machine learning.

## Why this matters for ARC-065

The paper gives the clean algorithmic explanation for the V3-EXQ-563 finding. If the elite subset contains only one first-action class, then the next refit step has no reason to preserve absent first-action classes. Collapse is not a mysterious E3 or motivation failure; it is an expected failure mode of an optimizer whose purpose is to concentrate probability mass around elite samples.

For REE, the immediate implication is diagnostic rather than architectural. Candidate first-action support must be measured before behavioural outcomes can be interpreted. A behavioural FAIL under support collapse should be marked non-contributory for goal, curiosity, vigor, and E3 score-bias mechanisms because those mechanisms were not given a choice surface.

## Limitations and confidence

This is not a paper about hippocampal planning, biological exploration, or action-object decoding. It does not prescribe a REE repair. It does, however, make one engineering conclusion hard to avoid: if support disappears at the elite-refit boundary, the repair has to touch proposal generation or elite preservation, not only downstream scoring. Confidence is 0.68: strong for CEM mechanics, moderate for ARC-065 translation.
