# Daw, Niv & Dayan 2005 -- Uncertainty-based Competition: MECH-163 Mapping

**Source:** Daw, N.D., Niv, Y. & Dayan, P. (2005). Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. *Nature Neuroscience*, 8(12), 1704-1711. DOI: [10.1038/nn1560](https://doi.org/10.1038/nn1560)

---

## What the Paper Does

Daw, Niv and Dayan 2005 provide the normative computational account of why both model-based (goal-directed) and model-free (habitual) systems coexist in the brain and how the brain arbitrates between them. The paper's central question is: given that both systems exist, how does the brain decide which one to trust at any given moment?

The authors propose a Bayesian arbitration mechanism: the brain weights the two systems according to their relative uncertainty about the current situation. The model-based system is more accurate in novel or changing environments (it can simulate correct values from the world model) but more uncertain in stable, well-practised situations (where it may have incomplete or inaccurate models). The model-free system is accurate in stable situations where its cached values reflect true statistics but uncertain in novel contexts where its caches are stale. The brain deploys the system with lower uncertainty -- effectively a Bayesian model selection over the two controllers.

## Key Theoretical Contributions

1. **Normative justification for dual-system architecture**: the paper shows analytically that the co-existence of model-free and model-based systems is computationally rational, not a design accident. A pure model-free agent would be inflexible; a pure model-based agent would be computationally intractable in large state spaces. The hybrid achieves better performance than either alone.

2. **Arbitration mechanism**: uncertainty-weighted competition provides a principled account of when each system dominates. Familiar, stable tasks -> model-free dominates. Novel, changing environments -> model-based dominates. This explains why practice builds habits (model-free takes over as uncertainty drops) and why novel situations invoke deliberative planning (model-based invoked when model-free uncertainty is high).

3. **Anatomical predictions**: the prefrontal-dorsolateral striatal competition maps onto the anatomical dissociation, with arbitration potentially mediated by their differential precision signals.

## Key Findings for MECH-163

The core finding for MECH-163 is the necessity argument: **neither system is universally sufficient**. Model-free alone fails in novel contexts where cached values are inaccurate (high model-free uncertainty); model-based alone is computationally intractable and would make familiar, well-practiced tasks inefficiently slow. The dual system is not a redundancy but an architectural solution to a genuine computational trade-off.

For MECH-163, this translates directly: the habit system (SNc/dorsal-striatum) alone cannot handle ethical agency because novel harm contexts have high model-free uncertainty -- the cached values simply do not include the new harm associations. The planned system (E3 hippocampal) alone would make every familiar resource-approach episode require full trajectory simulation -- prohibitively expensive. Both are necessary.

The uncertainty-based arbitration also explains the pathological cases MECH-163 is designed to address: when the planned system is unavailable or suppressed (e.g., E3 lesion, SD-012 homeostatic failure preventing z_goal seeding), the habit system takes over even in novel harm contexts where its uncertainty should be high -- precisely the context-blind harm production MECH-163 predicts.

## REE Mapping to MECH-163

The Daw et al. framework maps onto MECH-163's dual-system architecture as its computational foundation. The Bayesian arbitration corresponds to REE's uncertainty-weighted commitment gating: E3 takes over from cached approach when the situation is novel or harm-salient. The model-free dominance in familiar environments corresponds to REE's habit system handling routine approach efficiently.

The one architectural difference: REE's E3 hippocampal system is more explicitly spatialised and multi-step than Daw et al.'s model-based system (which is framed as tree-search over a state-transition model). The hippocampal terrain representation (z_world, residue field) is the REE implementation of the model-based world model, with added spatial and harm-gradient structure.

## Limitations and Confidence Reasoning

This is a computational theory paper -- predictions are not directly tested with neural or behavioural data in this work itself. The arbitration mechanism remains a theoretical proposal, subsequently supported by empirical work (e.g., Daw et al. 2011, fMRI). The harm-attribution and ethical agency dimensions of MECH-163 are entirely REE extensions. Confidence: 0.79.

*Based on article available via PubMed (PMID: 16286932) and Nature Neuroscience.*
