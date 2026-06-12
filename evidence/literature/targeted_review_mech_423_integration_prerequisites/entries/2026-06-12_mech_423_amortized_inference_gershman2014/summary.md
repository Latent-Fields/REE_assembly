# Gershman & Goodman (2014) — the converged shared posterior is the channel through which cross-module corrections flow

**Claim grounded:** MECH-423 (cross-model super-additivity) — readiness condition R2 (a converged / amortized inference loop must be running).
**Direction:** supports. **Confidence:** 0.64.

## What the paper did

Gershman and Goodman introduced "amortized inference" as a framework for how an agent answers many related probabilistic queries efficiently. The observation is that re-running inference from scratch for each query — recognising the same scene from a new viewpoint, say — is computationally wasteful when the queries share structure. Amortization reframes inference as a learned regression: train a *recognition model* q(z|x) that maps an observation directly to an approximate posterior over the latent variables, paying the cost once and reusing it across queries. They argue the brain operates in exactly this regime. This paper is the canonical reference behind the recognition-network half of the VAE and the modern amortized-inference literature.

## Why it speaks to MECH-423

MECH-423's mechanism — prediction-error corrections from one module propagating to the others — only works through a *shared posterior* over the L-space latent. If the latent is not actually inferred to a stable value, there is no common variable for the corrections to travel through. Gershman & Goodman supply the prerequisite: the inference that produces that shared posterior must be run, and run well. In REE terms, readiness condition R2 says the inference loop must reach convergence (or, if the substrate uses an amortized recognition map, that map must be trained past its *amortization gap* — the systematic discrepancy between the amortized posterior and the true one) before the integrated-vs-isolated comparison can carry any meaning.

The concrete value here is that the amortization gap turns R2 into something *measurable*. The readiness gate can require that the change in the inferred latent per inference step at readout has fallen below a small threshold (the loop has converged), and that the recognition map's held-out reconstruction/ELBO has plateaued (the amortization gap has closed enough). Below that, a null result on EXP-0380 is most parsimoniously explained by an unconverged inference loop feeding each module an under-determined latent — integrated approximately equals isolated, not because integration fails, but because the channel it would use is not yet open.

## Limitations and mapping caveats

The paper is about the structure and efficiency of inference, not about multi-module super-additivity. It justifies *why* a converged shared posterior is a prerequisite and names the failure mode, but it does not demonstrate that a converged loop produces super-additive gains. It is a CogSci proceedings paper — influential and widely cited, but lighter peer review than a journal. So this entry grounds readiness condition R2 specifically, and its confidence reflects that scoped role.

## Confidence reasoning

Source quality 0.70 (canonical and influential, but a proceedings piece). Mapping fidelity 0.62 — it maps cleanly onto REE's learned-latent inference but addresses the prerequisite rather than the super-additive effect. Overall 0.64, the lowest in the set, appropriate for a conceptual anchor that supplies a measurable convergence criterion without itself testing the claim.
