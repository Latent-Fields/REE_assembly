# What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? (Kendall & Gal, 2017)

## What the paper did

Kendall and Gal separated two things that deep learning had been running together. *Aleatoric*
uncertainty is noise inherent in the observation -- a blurry pixel is blurry no matter how much data
you collect. *Epistemic* uncertainty is uncertainty in the model itself, and it can be explained away
given enough data. They built a framework combining both, and for the aleatoric half the recipe is
simple and now standard: add a second output head so the network predicts a variance alongside its
mean, and train under a heteroscedastic Gaussian likelihood. The resulting loss down-weights terms
the network says are noisy, which they call learned attenuation, and it gave state-of-the-art results
on per-pixel semantic segmentation and depth regression.

## Why it is in an ARC-052 directory

Because it is, almost word for word, the implementation ARC-052's notes propose: "HarmEncoder and
AffectiveHarmEncoder each output (z, log_sigma); E3 weights inputs by exp(-log_sigma)." That is the
heteroscedastic head with attenuated weighting. So the first thing this entry does is retire a
feasibility worry -- the mechanism trains, it does not destabilise learning, and on real tasks it
helps. Nobody needs to prove that a precision head is buildable.

The second thing it does is more useful, and it is why this entry is recorded as mixed rather than
supporting. ARC-052 makes two clauses, and the log_sigma head answers only one of them. Clause (2),
that z_harm_a precision falls when the threat state is volatile, is genuinely an aleatoric statement:
the accumulated estimate is noisier right now, and a variance head trained on the right signal can
represent that. Clause (1) is not. "z_harm_s precision increases with forward model accuracy -- when
E2_harm_s predictions are good, the PE is more informative" is a claim about the *model's* competence
improving, which is exactly the quantity Kendall and Gal define as epistemic and exactly the quantity
they say a likelihood-trained variance head does not capture. Aleatoric sigma does not shrink as the
model gets better; that is the definition. A single log_sigma head cannot implement clause (1) as
written.

This is worth flagging now rather than after a build, because the fix is cheap and known. Lee et al.
(2014), the companion entry here, derives system reliability from the dispersion of the forward
model's own prediction errors -- an epistemic quantity, computed from signals REE already produces.
Clause (1) wants that estimator; clause (2) wants a learned variance head. Treating them as one
mechanism because both are called "precision" would produce a substrate that quietly computes the
wrong thing in the sensory stream while looking correct in the affective one.

## The failure mode hiding inside "loss attenuation"

There is a second warning here that the paper presents as a feature. A network permitted to predict
its own variance has two ways to lower its loss: predict better, or declare the input noisy. On
segmentation benchmarks the second is desirable -- it is robustness to label noise. In a harm stream
it is not obviously desirable at all. The inputs a harm encoder finds hardest to predict are
plausibly the ones carrying the most information about novel threat, and an encoder that learns to
mark those as low-precision has learned to remove exactly them from E3's attribution and commit
gating. Nothing in ARC-052 currently guards against this. If a precision head is built, the
distribution of sigma over high-PE inputs should be instrumented from the first experiment, and a
sigma that rises monotonically with prediction difficulty should be treated as a result to explain,
not a healthy prior.

## Limitations

Supervised computer vision, dense ground-truth targets, benchmark metrics. The performance results
transfer to REE not at all -- they establish that the mechanism is sound engineering in a setting
with a supervised likelihood, which z_harm_s and z_harm_a do not have. What does transfer is the
aleatoric/epistemic distinction, because that is a property of the estimator rather than of the
domain, and it is the part of this entry that should actually change what gets built.

## Confidence

0.60, direction mixed. Supports feasibility of the proposed mechanism; weakens the claim that the
proposed mechanism implements clause (1).
