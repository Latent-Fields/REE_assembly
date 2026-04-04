# Summary: Friston (2005)

**Citation:** Friston K. "A theory of cortical responses." *Philos Trans R Soc Lond B Biol Sci* 360(1456):815-836. DOI: [10.1098/rstb.2005.1622](https://doi.org/10.1098/rstb.2005.1622)

## What the paper did

Foundational theoretical paper establishing hierarchical cortical responses as the output of a generative model that minimises free energy (surprise) via empirical Bayes. Derived the computational and architectural constraints that follow from this framework and showed how they explain a wide range of cortical phenomena.

## Key findings

1. **Bidirectional connections are architecturally necessary** -- hierarchical free-energy minimisation requires both generative (top-down, backward) and recognition (bottom-up, forward) connections. Neither direction alone is sufficient.
2. **Backward connections carry predictions; forward connections carry prediction errors** -- the functional asymmetry between descending (predictions) and ascending (errors) connections is derived from, not added to, the free-energy minimisation framework.
3. **Context-sensitive empirical Bayes** -- the hierarchy allows priors to be constructed dynamically from the context provided by higher levels, rather than fixed in advance. Higher levels supply the prior for lower levels.
4. **Explains MMN, repetition suppression, P300** -- the predictive hierarchy naturally accounts for these canonical neurophysiological phenomena as prediction error signals.

## Relevance to ARC-045

Friston 2005 provides the computational foundation for the bidirectionality that ARC-045 claims is architecturally necessary:
- **Hippocampus-to-neocortex (SWS direction) = recognition model / prediction error channel:** Hippocampal replay carries attribution estimates that are, in effect, prediction errors relative to the neocortical schema -- updating the schema prior.
- **Neocortex-to-hippocampus (waking/REM direction) = generative model / prediction channel:** Neocortical schema provides top-down predictions that bias what hippocampus replays and encodes -- the prior shaping attribution.
- **Attribution mapping convergence = free-energy minimisation** in the hippocampal-neocortical hierarchy. This convergence requires both directions: neither generative alone (top-down only) nor recognition alone (bottom-up only) can minimise free energy.

The paper derives that the functional asymmetry between backward (driving + modulatory) and forward (driving only) connections is not arbitrary but a necessary architectural consequence of hierarchical Bayesian inference.

## Limitations for REE mapping

- Addresses sensory cortical hierarchy; transfer to hippocampal consolidation requires domain extension
- Does not address sleep phases, offline consolidation, or SWS/REM distinction
- Schema/attribution distinction is implicit in the generative/recognition architecture but not the paper's explicit focus
