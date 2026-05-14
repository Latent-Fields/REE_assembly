# Moss 2020 - Cross-Entropy Method Variants for Optimization

[arXiv](https://arxiv.org/abs/2009.09043) - arXiv:2009.09043.

## What the paper did

Moss studies variants of the Cross-Entropy method for optimization, focusing on expensive objectives and local-minima convergence. The paper uses surrogate modeling and Gaussian mixture models as ways to improve exploration of the design space when ordinary CE can concentrate too narrowly.

## Why this matters for ARC-065

The paper is relevant because REE's failure is a support-collapse failure. A unimodal refit can lose alternatives; a mixture proposal is one established way to keep multiple basins represented. That said, V3-EXQ-563b should not jump straight to a full mixture proposer. The immediate action space is small, the failure is first-action support, and the diagnostic question is whether a minimal support-preserving guard touches the live proposal path.

The design implication is therefore conservative: treat mixture CEM as a later option if minimal support preservation fails. Do not register a permanent architecture decision from this source.

## Limitations and confidence

This is a preprint, not a mature MPC benchmark or neuroscience anchor. It does not address action-object decoding. Confidence is 0.54: enough to justify a design note saying mixture proposals are plausible, not enough to justify implementing them now.
