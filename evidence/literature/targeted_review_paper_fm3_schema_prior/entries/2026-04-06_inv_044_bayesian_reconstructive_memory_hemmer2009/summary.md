# Hemmer & Steyvers (2009) — Integrating episodic memories and prior knowledge at multiple levels of abstraction

**Source:** Hemmer P, Steyvers M. Integrating episodic memories and prior knowledge at multiple levels of abstraction. *Psychonomic Bulletin and Review* 2009; 16(1): 80–87. DOI: [10.3758/PBR.16.1.80](https://doi.org/10.3758/PBR.16.1.80)

## What the paper argues

Hemmer and Steyvers present a Bayesian account of reconstructive memory in which recalled estimates of a perceived property (in their case, the size of a seen fruit or vegetable) are a weighted combination of the noisy episodic trace and prior knowledge operating at multiple hierarchical levels: the specific object prior (how big is this particular apple typically?) and the superordinate category prior (how big are fruits typically?). When the episodic trace is reliable, recall approximates the actual seen value. When the trace is noisy or weak, recall is pulled toward the prior. This prior pull is not a bias in the pejorative sense -- it is rational Bayesian inference from the best available information.

The empirical result is that recall is systematically shifted toward prior expected values, and the magnitude of the shift is well-predicted by the hierarchical Bayesian model. Both levels of prior operate in parallel, with the more specific level dominating when available. The model accounts for individual differences in recall bias through variation in estimated prior precision.

## How this connects to FM3 (prior quality constrains posterior quality)

Hemmer and Steyvers formalise something the FM3 argument presupposes: that the quality of episodic attribution (posterior inference) is bounded above by the quality of the prior. When the prior is tight and well-calibrated -- when the schema is installed -- posterior estimates are accurate even under substantial episodic noise. When the prior is flat -- when the schema is absent or degenerate -- the posterior loses the episodic signal and defaults to the global category mean, which carries no context-specific information.

This maps onto INV-044's prior-before-posterior constraint as follows: an agent attempting to simultaneously construct its schema (install the prior) and perform episodic attribution (compute the posterior) faces the problem that its prior is uninformative at the moment attribution is attempted. The Bayesian model predicts that under these conditions, attribution will be systematically regressed to the global mean -- losing the context-specific information that the attribution was supposed to capture. The more specific and well-formed the schema, the more information is preserved in the posterior. A schema under construction is, by definition, not yet specific or well-formed.

The hierarchical structure of Hemmer and Steyvers's prior (object-level and category-level, operating in parallel) also maps onto REE's nested context structure: general schema topology (which distinctions are relevant) and specific slot content (what evidence belongs to each slot) are analogous to category-level and object-level priors respectively. Installing the category-level prior first (schema topology) enables the object-level attribution (slot-filling) to proceed with appropriate constraints.

## Honest caveats

The paper's empirical paradigm is perceptual reconstruction of object sizes -- a far cry from causal attribution of contextual evidence to context slots. The 'prior' in Hemmer and Steyvers is a statistical distribution over a continuous property (size), not a structural schema specifying which context distinctions are relevant. The extension to REE's context slot attribution requires importing the Bayesian principle into a qualitatively different domain.

The paper also does not study what happens when the prior is being constructed at the same time as the posterior is computed -- it only demonstrates the prior-shapes-posterior direction from pre-established priors. The FM3 claim that simultaneous co-computation produces a degenerate prior is an inference from the Bayesian formalism, not a result directly demonstrated here. One could imagine an adaptive system that holds the prior fixed while computing the posterior and then updates the prior -- the failure mode requires making explicit why this separation is not achievable online.

That said, Hemmer and Steyvers provide the most direct behavioural and computational demonstration that prior quality is a determinant of recall quality -- which is necessary (though not sufficient) for the FM3 argument. The Bayesian Account of Reconstructive Memory paper (Topics in Cognitive Science, 2009, same authors) extends the same argument to natural scenes and is a complementary reference.

## Why cite this in §3

Sanders et al. (2020) establish the formal Bayesian argument at the level of context inference (hidden state inference). Hemmer and Steyvers establish empirically that prior quality constrains recall quality in human memory -- providing the behavioural grounding for the claim that a degenerate prior produces degenerate attribution, not just theory. For a paper arguing from first principles that offline phases are architecturally necessary, having human behavioural evidence that prior quality shapes posterior quality (even in a simplified perceptual domain) strengthens the empirical case.
