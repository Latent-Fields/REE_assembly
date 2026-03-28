# Friston et al. 2012 — Dopamine, Affordance and Active Inference

**Source:** Friston KJ, Shiner T, FitzGerald T, Galea JM, Adams R, Brown H, Dolan RJ, Moran R, Stephan KE, Bestmann S (2012). *PLoS Computational Biology* 8(1):e1002327. [DOI: 10.1371/journal.pcbi.1002327](https://doi.org/10.1371/journal.pcbi.1002327)

---

## What the paper did

The paper develops a Bayesian account of how dopamine enables affordance-based motor behaviour in the context of active inference. Rather than treating dopamine as a reward prediction error signal in the classical reinforcement learning sense, Friston and colleagues propose that dopamine encodes the *precision* of proprioceptive prediction errors — the inverse variance, or confidence, of the expected sensory outcomes of action. They implement this in a hierarchical generative model of sequential motor tasks and show that varying tonic dopamine (precision) produces qualitatively different behavioural profiles, including a simulated Parkinsonian deficit when dopamine is depleted.

## Key findings relevant to ARC-016

The central mechanism is that prediction error precision modulates the weight with which errors update action. High precision means sensory mismatches (errors) have strong influence on action policies; low precision means prior beliefs dominate and the agent resists change. This creates a continuum from open, responsive action (high precision / low variance) to rigid, inertial action (low precision / high variance). Crucially, the precision parameter is not a fixed property of the system — it is dynamically adjusted based on the estimated reliability of sensory channels, creating a variance-driven control regime switch.

This directly grounds ARC-016's claim that prediction variance drives a commitment threshold. In the REE architecture, E3's prediction variance plays the same functional role as dopamine-encoded precision: when prediction variance is low (E3 is confident), the relative threshold is easily crossed and the BetaGate commits; when prediction variance is high (E3 is uncertain), the threshold is harder to cross. EXQ-018b's finding — that a 40% reduction in E3-derived variance precision produced a proportional 40% reduction in commit rate — is the REE experimental instantiation of this precision-weighting mechanism.

## Translation to REE / ARC-016

ARC-016 claims a "precision-to-commitment circuit": E3-derived prediction variance → relative threshold → BetaGate → action_selection. Friston et al. provide the theoretical grounding for why such a circuit is not merely an engineering choice but a canonical Bayes-optimal solution. A system that uses prediction variance to gate action is implementing the correct inference: commit when you are confident, withhold when you are uncertain. The dopamine-as-precision model extends this to the motor hierarchy, showing the same principle applies at multiple levels — from proprioceptive (E1 analog) to goal-directed (E3 analog) action.

## Limitations and caveats

The mapping from global dopaminergic modulation to REE's local, circuit-specific E3-derived variance computation requires an inferential step. Friston's model uses a single tonic precision parameter across the motor hierarchy, whereas ARC-016 requires that precision be locally computed by E3 and used to set a specific threshold for cognitive commitment, not motor execution. The affordance framing is also motor-specific: the paper's primary domain is voluntary limb movement, not the higher-level deliberation-to-commitment transition REE models. These are parallel implementations of the same principle, not the same mechanism.

## Confidence reasoning

Confidence 0.76. Source quality is high (PLoS Comp Bio, Friston lab, extensive peer-cited work). Mapping fidelity is good but not perfect: the global/local precision distinction and motor/cognitive distinction introduce real uncertainty. Transfer risk is moderate. The paper earns a place in this batch because it provides the best-available computational grounding for the precision-weighting half of ARC-016 — a derivation from first principles showing why variance-driven threshold gating is Bayes-optimal.

*According to PubMed, this article is available at PMID 22241972. [DOI: 10.1371/journal.pcbi.1002327](https://doi.org/10.1371/journal.pcbi.1002327)*
