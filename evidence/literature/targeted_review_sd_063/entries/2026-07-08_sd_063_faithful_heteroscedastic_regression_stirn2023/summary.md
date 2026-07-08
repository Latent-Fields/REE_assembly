# Faithful heteroscedastic regression: why the Gaussian head corrupts the mean (Stirn et al. 2023)

**Claim under test:** SD-063 — E2's world-forward should carry a *conditional* (per-input) predictive-uncertainty head feeding E3 commitment gating. The v3_pending gate requires that a wired-in head (a) keep its CRPS / per-point error-correlation advantage under *joint* training and (b) *not* explain away the SD-031 E2WorldForward agency residual.

## What the paper did

Stirn, Wessels, Schertzer, Pereira, Sanjana and Knowles (AISTATS 2023) diagnose a pathology in the de-facto method for neural heteroscedastic regression: minimising a Gaussian negative log-likelihood where the network predicts both mean `μ(x)` and input-dependent variance `σ²(x)`. The mean gradient is scaled by `1/σ²(x)`. This means high-variance inputs contribute weak mean gradients, so the model is biased toward fitting low-noise regions — and, worse, it can assign *high* variance to points it predicts poorly simply to attenuate their loss, rather than improving the mean. Stirn et al. (citing Seitzer et al. 2022) call this a "rich-get-richer" dynamic: low-variance points keep providing the largest learning signal and get richer, while poorly-fit points are explained away by inflated variance. They prove and empirically confirm that the resulting mean estimates are significantly *less accurate* than an equally-expressive mean-only (MSE) model. Their fix is a stop-gradient / Newton-step modification (a sibling of Seitzer's β-NLL) that shields the shared trunk from the variance head's gradient, provably recovering a "faithful" mean equal to the mean-only baseline while keeping best-in-class variance calibration.

## Why it bears on SD-063 — and why it is *mixed*

This paper cuts both ways, which is why I score it `mixed`.

**Supporting side.** It gives the mechanistic reason the `hetero_gaussian` arm *underperformed* the `quantile_pinball` arm in the V3-EXQ-712 diagnostic that motivated SD-063. The Gaussian-NLL head is not a neutral choice — it actively degrades the point predictor. So SD-063's decision to prefer the distribution-free quantile/pinball form over the Gaussian form is well-founded: the pinball loss has no `1/σ²(x)` term and does not induce this particular rich-get-richer cycle.

**Cautioning side.** The pathology is fundamentally about *coupling a conditional-uncertainty head to the mean through a shared trunk and optimising them jointly* — which is exactly what a wired-in E2 uncertainty head does. V3-EXQ-712 trained detached heads on a frozen encoder (effectively single-phase P1); SD-063 explicitly flags that this does *not* validate the joint-training case. Stirn et al. are precisely the evidence that the joint case is where things break: the concern that the head might corrupt E2's mean, or absorb the agent-caused component of next-state variance (the SD-031 residual) instead of improving the forward prediction, is not hypothetical hand-wringing — it is the documented failure mode of the whole family of conditional-variance heads under joint training.

## Where the mapping strains

The sharpest, theorem-backed result is specific to the Gaussian parameterisation. The quantile/pinball head SD-063 actually builds does not carry the `1/σ²` gradient weighting, so it is *not* automatically subject to this exact pathology. This makes the paper a warning-by-analogy for SD-063's chosen form rather than a direct measurement of it. Whether a pinball head coupled to E2's encoder preserves the mean and leaves the SD-031 residual intact is the empirical question SD-063's own validation experiment must answer — the literature raises the flag but cannot lower it.

## Confidence

**0.70, mixed.** High-quality AISTATS analysis (theorem plus broad empirics across UCI, a CRISPR genomics task, and image regression). Mapping fidelity is high because it speaks directly to both of SD-063's open validation conditions. Transfer risk is moderate: the definitive result is Gaussian-specific while SD-063's head is quantile-based, so the hazard transfers as a live caveat, not as a proven defect of the chosen form. Net effect on the claim: it strengthens the *form choice* while sharpening — not resolving — the *joint-training risk* that keeps SD-063 v3_pending.
