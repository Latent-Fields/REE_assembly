# JUCAL: Jointly Calibrating Aleatoric and Epistemic Uncertainty — Heiss et al. (2026)

## Relevance to Q-013

Q-013 asks a deceptively practical question: can a deterministic JEPA architecture, by tracking the dispersion of its latent predictions, provide uncertainty estimates good enough to replace explicit stochastic uncertainty heads for REE's precision routing? The REE adjudication is hybridize -- suggesting that some combination might work. JUCAL provides evidence that the hybridize answer requires more care than might initially appear.

## What the paper shows

Heiss and colleagues address the uncertainty calibration problem in ensemble classifiers. They observe that classical temperature scaling -- the standard post-hoc calibration method -- fails when aleatoric uncertainty (variability due to genuine data noise) and epistemic uncertainty (variability due to model ignorance) are present simultaneously, because a single scalar cannot correctly re-weight two structurally distinct sources. Their proposed remedy, JUCAL, applies two separate scaling constants jointly optimised on a validation set. Compared to temperature scaling, JUCAL reduces negative log-likelihood and prediction set size by up to 15-20% without requiring access to model internals or additional training.

The result generalises a principle that has been argued informally for some time: aleatoric and epistemic uncertainty are not the same thing, they respond differently to additional data, and treating them as a single quantity produces systematically miscalibrated confidence estimates.

## The challenge for Q-013

JEPA's latent variable z is designed to capture the unpredictable component of a prediction -- in LeCun's framing, z encodes what the context representation cannot determine. This is at least partly an aleatoric signal (irreducible future uncertainty), but it also contains epistemic components (cases where the model lacks information). If precision routing in REE requires distinguishing these -- routing low-confidence inputs to E3 for harm evaluation vs. routing uncertain-but-low-risk inputs to a simpler evaluator -- then a single derived dispersion measure from z cannot be reliably calibrated for that purpose without additional structural apparatus.

JUCAL's finding does not prove that deterministic JEPA plus derived dispersion cannot work; it shows that calibrating the required distinction is non-trivial even for architectures (ensembles) that have structural access to both uncertainty types. For a single deterministic JEPA forward pass, the structural access is more limited still.

## Calibration note

Confidence is 0.65 -- the paper has not yet undergone peer review as of this entry, and the mapping to JEPA requires several analogical steps. The direction is weakens rather than contradicts: the evidence challenges the easy version of the hybridize answer (dispersion alone is sufficient) without foreclosing a more carefully engineered version (dispersion plus explicit calibration head). The evidence is best read as a demand for specificity in the Q-013 hybridize proposal, not as a decisive objection.
