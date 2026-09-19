# Bounded rationality in C. elegans explained by circuit-specific normalization (Cohen et al., 2019)

## What the paper does

The authors build choice assays for a nematode with 302 neurons and test whether its olfactory
decisions obey Independence of Irrelevant Alternatives. Mostly they do -- which is itself worth
noting, since the interesting result is a conditional rather than a blanket failure. Violations
appear when the circuit of olfactory sensory neurons is *asymmetric*, and the authors can induce
irrationality by genetically manipulating the asymmetry between the AWC neurons. A
normalization-based model of value coding and gain control accounts for the pattern: particular
constraints on how information is coded produce bounded rationality.

## Why a worm is in a review about a salience coordinator

Because it isolates a variable the other entries leave fixed, and it happens to be a variable REE
directly controls.

Louie et al. (2013) establish that normalization imports choice-set dependence. What they do not
tell us is what makes it worse or better. Cohen et al. do: asymmetry in the input circuit. Symmetric
circuit, mostly rational choices. Asymmetric circuit, IIA violations that the normalization model
predicts.

Now look at `SalienceCoordinator.config.affinity_weights`. It is a mapping from each named input
signal to a per-mode weight dictionary, and those weights are unequal by construction --
`dacc_pe` does not argue equally for `external_task`, `internal_planning`, `internal_replay` and
`offline_consolidation`, and it is not supposed to. That asymmetry is the design. It is also, on
Cohen et al.'s account, the configuration in which a normalizing gain control stops being benign.

## The question this reframes

The `mode-governance-engagement` queue entry is titled "Replace the hard affinity-input box clamp
with a saturating/normalizing bounding operator; grade the commitment term; decide the production
default". Read alongside this paper, that title asks the wrong first question. The prior question is
whether the affinity weight map's asymmetry is compatible with a pooled operator at all -- because a
normalizing operator applied over an asymmetric map may be *worse* than a clamp over the same map,
and nothing in the entry's current framing would surface that.

There is a second, subtler point. Because most of the worm's choices were rational, the pathology is
conditional and configuration-specific. An REE build could not therefore infer from one clean
occupancy result that the operator is safe; the effect would show up only in particular corners of
the configuration space. That is an argument for instrumenting the asymmetry explicitly rather than
testing the operator behaviourally and declaring victory.

## Honesty about the gap

This is the weakest mapping in the review and I would not want it read as anything else. A
302-neuron nematode running a chemotaxis assay and a four-mode operating-state coordinator in a
simulated agent are alike in the *shape* of the computation and in nothing else. The paper offers no
quantitative threshold for how much asymmetry is too much, so it cannot predict anything about REE's
numbers. What it does is name a variable nobody in this thread has been looking at, and that is why
it earns its place.

## Confidence

0.63, direction mixed. High source quality, genuinely low mapping fidelity, and the highest transfer
risk of the six. Included as a hazard flag with its own limitations on the record.
