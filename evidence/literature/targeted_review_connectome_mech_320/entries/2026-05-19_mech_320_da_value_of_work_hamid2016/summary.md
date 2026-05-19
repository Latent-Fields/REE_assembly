# Hamid et al. (2016) — Mesolimbic dopamine signals the value of work

*According to PubMed. Nat Neurosci 19(1):117-26 (published online 2015-11-23). [DOI](https://doi.org/10.1038/nn.4173) · PMID 26595651 · PMC4696912.*

## What the paper did

Where Niv (2007) gave the formalism and Salamone & Correa (2012) gave the identity, Hamid and colleagues went and measured the thing. Using microdialysis and fast-scan cyclic voltammetry — two methods with complementary time resolutions — plus optogenetic manipulation in rats performing an adaptive decision task, they tracked nucleus accumbens dopamine across timescales. Minute-by-minute dopamine tracked reward rate and motivational vigor; second-by-second dopamine encoded a temporally discounted value function. When they changed dopamine directly, willingness to work changed immediately, and preceding choices were reinforced. Their synthesis: dopamine carries a single, fast-evolving decision variable — the reward available for investment of effort — and that one variable is read out for both learning and motivation.

## Why it matters for MECH-320

This is the empirical keystone. MECH-320 posits `v_t`, a slow EWMA over the realised E3-score stream, scaling an additive action-vs-no-op bias in trajectory scoring. Hamid et al. show the biological correlate of exactly that: a slowly-varying, reward-rate-coupled signal that sets motivational vigor, and whose experimental perturbation immediately moves willingness to work. The minute-scale covariation is, almost literally, a measurement of `v_t`. For a claim that has so far had zero literature entries and a `directional_conflict_alert`, this is the kind of direct, causal, gold-standard evidence that should move the needle.

## The honest tension

I have not filed this as an unqualified win, and the reason is the paper's own headline. Hamid et al. argue for *one* shared decision variable doing double duty for learning and motivation. MECH-320, by contrast, is built to be *distinct* — from learning-rate effects, from MECH-313's noise floor, from target-conditioned wanting. The biology here is, if anything, *less* modular than the REE decomposition. That does not weaken the vigor-coupling claim — the coupling is precisely what they measure — but it should make us honest that the clean architectural separation REE draws is a modelling commitment the biology does not obviously endorse. I have logged this as a failure signature rather than smoothing it over, because it is the place a future conflict could surface (e.g., if an experiment finds REE's vigor term inseparable from its learning dynamics, this paper would be the precedent).

## Confidence

0.85, `supports`. Source quality is very high (Nature Neuroscience; the Berke lab; two neurochemical methods plus causal optogenetics). Mapping fidelity is high — it is the most direct measurement of the reward-rate-to-vigor coupling available — discounted modestly by the single-shared-variable framing and the usual rodent-to-REE transfer. Together with Niv (2007) and Salamone & Correa (2012), MECH-320 now has formalism, identity, and measurement; the residual uncertainty is about modularity, not about whether the vigor signal exists.
