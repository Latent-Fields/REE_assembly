# Heteroscedastic aleatoric uncertainty: per-input noise beats a global term (Kendall & Gal 2017)

**Claim under test:** SD-063 — E2's world-forward should carry a *conditional* (per-input) predictive-uncertainty head feeding E3 commitment gating, rather than E3 relying only on a temporally-smoothed global running-variance EMA.

## What the paper did

Kendall and Gal (NeurIPS 2017) is the canonical reference distinguishing *aleatoric* uncertainty (input-dependent observation noise, irreducible with more data) from *epistemic* uncertainty (model uncertainty, reducible with more data). Their aleatoric formulation has the network predict, per input, both a point estimate and an observation-noise variance `σ²(x)`, trained by minimising a Gaussian negative log-likelihood. They note this loss behaves as "learned loss attenuation": the network can down-weight the contribution of inputs it flags as noisy, making training robust to heteroscedastic noise. Empirically, adding the input-conditional aleatoric head yields state-of-the-art results on monocular depth regression and semantic segmentation, beating an equivalent model that assumes a fixed (homoscedastic) global noise level.

## Why it bears on SD-063

The load-bearing sentence of SD-063 is that E3's running-variance EMA is a *temporally-smoothed global* spread whose predicted uncertainty does not correlate with realized per-prediction error (`precision_error_corr ~ 0.0` by construction), and that E2 should instead carry a *per-input* spread. Kendall & Gal supply the foundational ML grounding for that exact distinction: an input-conditional aleatoric head recovers "this input is noisier than that one" structure that a global noise scalar cannot represent, and capturing that structure improves the downstream task. This is precisely the qualitative gain SD-063 wants — conditioning the commit gate on where *this* E2 prediction is uncertain, not on a running average across recent, unrelated predictions.

## Where the mapping strains

The head form is the catch. Kendall & Gal use a Gaussian log-variance MLE head — the same family as the `hetero_gaussian` arm that *lost* to `quantile_pinball` in V3-EXQ-712. The "learned attenuation" that makes their loss robust is the `1/σ²(x)` gradient scaling that later work (Stirn et al. 2023; Seitzer et al. 2022, both in the companion entry) shows can bias the *mean* estimate — points get high predicted variance to explain away poor mean fits rather than to improve them. So this paper supports the *direction* (input-conditional uncertainty beats a global term) while implicitly cautioning against the specific mechanism if it were wired jointly into E2. A second strain: their aleatoric uncertainty is genuine observation noise on a supervised target. SD-063's E2 predicts a *latent next-state* whose variance includes an agent-caused component (the SD-031 residual) that the uncertainty head must *not* absorb — a disentanglement problem this vision setting never has to solve.

## Confidence

**0.68, supports.** Source quality is very high; this is the reference that made the aleatoric/epistemic split standard vocabulary. Mapping fidelity is solid on the "per-input vs global" axis that is SD-063's core, but only moderate overall because the head form is the one SD-063 rejected and the task domain lacks the latent-agency-residual complication. It grounds the *principle* firmly; combined with the Chua PETS entry it establishes that conditional forward-model uncertainty is a well-validated design pattern, while the Stirn and Chung entries mark exactly why SD-063 chose the quantile form over this one.
