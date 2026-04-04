# Summary: Sanders, Wilson & Gershman (2020)

**Citation:** Sanders H, Wilson MA, Gershman SJ. "Hippocampal remapping as hidden state inference." *eLife* 9. DOI: [10.7554/eLife.51140](https://doi.org/10.7554/eLife.51140)

## What the paper did

Formalised hippocampal remapping as Bayesian hidden state inference. The animal maintains a posterior distribution over discrete latent contexts (hidden states), and the hippocampal map at any moment reflects beliefs about which context is currently active. The framework was applied to a range of classical remapping phenomena and validated against rodent place cell data.

## Key findings

1. **Remapping reflects posterior beliefs about hidden state**, not a direct readout of objective environmental change. Partial remapping = high posterior uncertainty over context identity.
2. **Context schema (prior) must precede posterior inference.** The model requires a pre-formed prior over context partitions; without it, observations cannot be assigned to context slots. The prior encodes which environmental distinctions are structurally relevant.
3. **Online joint estimation of prior and posterior is degenerate.** The hidden state inference framework shows that prior construction and posterior attribution are nested computations: the prior is a prerequisite input to the posterior calculation, not a co-product of it.
4. Bayesian nonparametric extension (CRP prior) allows new contexts to be created, but this creation process is itself a prior-update operation that must be committed before subsequent attribution.

## Relevance to INV-044

This paper is the primary grounding for INV-044. It demonstrates formally that:
- **Schema formation (which distinctions matter)** = prior construction = maps onto the SWS-analog phase
- **Causal attribution (which evidence belongs to which slot)** = posterior inference = maps onto the waking/REM-analog phase

A system attempting to perform both simultaneously faces the degenerate-prior problem: the prior being constructed is incomplete at the moment attribution is attempted, producing a flat posterior. This is architecturally equivalent to the claim in INV-044 that co-computing prior construction with online encoding produces a degenerate prior that makes attribution uninformative regardless of training duration.

## Limitations for REE mapping

- Does not directly implement a co-computing system to empirically demonstrate the degeneracy prediction
- Spatial context is the example domain; generalisation to abstract causal attribution slots is inferred from the Bayesian formalism, not tested
- The CRP extension allows incremental schema growth, but still requires prior commitment before slot-filling
