# Marshall et al. 2016 — Pharmacological Fingerprints of Contextual Uncertainty

**Source:** Marshall L, Mathys C, Ruge D, de Berker AO, Dayan P, Stephan KE, Bestmann S. *PLoS Biology* 14(11):e1002575 (2016). [DOI](https://doi.org/10.1371/journal.pbio.1002575). PMID 27846219, PMCID PMC5113004. According to PubMed.

## What the paper did

128 healthy adults performed a probabilistic serial reaction time task -- a learning paradigm with both within-context noise (cues are stochastic) and across-context drift (the underlying probabilities change). Subjects were assigned in a double-blind, double-dummy design to one of four arms: placebo, noradrenergic blockade (propranolol), cholinergic blockade (biperiden), or dopaminergic blockade (amisulpride). Behavioural choices were fit with a hierarchical Bayesian learning model that explicitly represents three distinct uncertainty quantities: trial-level noise, context-level volatility, and the meta-level probability of context change. The pharmacological manipulations selectively perturbed different uncertainty computations.

## Why it matters for Q-041

This is the most rigorous empirical answer to Q-041's architectural question I could find. The result is specifically not "one supervisor" and not "scattered loci" but a multi-channel architecture: at least three pharmacologically dissociable systems each contributing a different sub-quantity to the global uncertainty computation. NE primarily perturbed learning under unexpected environmental change -- the regime-shift detection arm. ACh primarily perturbed the attribution of uncertainty between within-context noise and contextual switches -- the noise-vs-context discriminator. DA primarily perturbed the use of uncertainty representations for fast adaptive responses, but not the uncertainty computations themselves -- the policy-coupling arm.

Mapped onto REE: ARC-016 dynamic precision, SD-032c AIC interoceptive baseline EMA, SD-032d PCC stability scalar, and SD-032e pACC drive bias all live closest to the DA channel in this taxonomy -- they take a precision/uncertainty quantity and use it to modulate fast adaptive responses (commit thresholds, salience gain, drive). The NE channel (regime-shift detection) and the ACh channel (noise-vs-context attribution) are missing as architectural slots in REE. So the Marshall result implies REE has not even a single one of the supervisor's three channels in the integrative position; it has only the broadcasters in the policy-coupling position.

This is the strongest evidence I could find that Q-041's first motivating gap (cross-substrate volatility tracking) is real. The brain has dedicated, dissociable architecture for it. REE does not.

## Mapping to REE

The pharmacological dissection results transfer as architectural slots, not as substrate. Receptor blockade is not equivalent to channel lesion; the result establishes that the channels are dissociable, not that they are independent. The hierarchical Bayesian model used to define the three uncertainty quantities is one of several possible parameterisations -- if you fit a different model, you find different channels. The architectural pattern that does transfer cleanly: the brain implements meta-stability across substrates with a small number of dissociable system-level channels rather than with either a single executive supervisor or with fully local adaptive loci. REE should consider naming the missing channels (regime-shift detection, noise-vs-context attribution) as architectural slots even if the substrate underlying them is left underdetermined.

## Caveats

The sample is large but the experimental design relies on the hierarchical Bayesian model being a faithful description of what the brain actually computes. If the brain implements uncertainty computations in a way that does not factor as Mathys's HGM does, the apparent channel selectivity could be a model artefact. Pharmacological doses were single doses in healthy adults, far from the chronic-load regime Q-041's third gap (setpoint drift) actually targets. The paper does not address sleep-mediated writeback at all.

## Confidence reasoning

0.72 mixed for Q-041. Source quality high (0.85) -- PLoS Biology, large sample, rigorous double-blind double-dummy pharmacology. Mapping fidelity high-moderate (0.72) -- the paper directly tests the architectural question Q-041 raises and proposes a specific multi-channel answer. Transfer risk moderate (0.30) -- pharmacology to REE substrate is one architectural step removed, and the HGM parameterisation is one of several possible. Direction is mixed because the paper neither supports nor weakens the strong "single supervisor" reading -- it supports a third position (small number of dissociable channels) that REE should take seriously as the architectural target.
