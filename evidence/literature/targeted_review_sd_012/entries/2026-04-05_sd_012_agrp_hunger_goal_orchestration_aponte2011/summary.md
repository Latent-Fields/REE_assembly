# Summary: Aponte et al. 2011 — AgRP neurons sufficient to orchestrate feeding behavior

**Entry:** 2026-04-05_sd_012_agrp_hunger_goal_orchestration_aponte2011
**Claim tested:** SD-012 (homeostatic drive modulation of goal seeding)
**Evidence direction:** supports
**Confidence:** 0.80

## Paper

Aponte, Y., Atasoy, D. & Sternson, S.M. (2011). AGRP neurons are sufficient to orchestrate feeding behavior rapidly and without training. *Nature Neuroscience*, 14, 351-355. DOI: 10.1038/nn.2739

## Core finding

Optogenetic activation of approximately 800 hypothalamic AgRP (agouti-related peptide) neurons in sated mice evoked voracious, goal-directed food-seeking and consumption within minutes. Behavior was selective (food over water, food over non-food objects) and required no prior training. Under normal satiety, these neurons are suppressed and spontaneous food-seeking is absent.

This is a direct causal demonstration that hunger-state neurons (AgRP) are *sufficient* to reinstate complete goal-directed feeding behavior in an otherwise non-motivated (sated) animal.

## Relevance to SD-012

SD-012 proposes: `effective_benefit = raw_benefit * (1.0 + drive_weight * drive_level)`

The Aponte et al. finding maps to this as follows:
- **AgRP neuron firing rate = biological correlate of drive_level**
- **Sated state** (drive_level ~ 0): AgRP neurons suppressed, no goal-directed food seeking
- **Hungry state** (drive_level ~ 1): AgRP neurons active, full goal-directed cascade engaged
- **Forced AgRP activation in sated mice**: artificially injecting drive_level = 1 into an otherwise low-drive animal restores goal orchestration immediately

This is the exact operation that SD-012's scaling term performs: drive_level amplifies the effective benefit signal, enabling z_goal to cross the seeding threshold. Forcing drive_level to 1 (via AgRP activation) in the biological system is analogous to what SD-012 does computationally.

## Key caveat

The paper measures behavioral output (feeding), not internal goal representations (z_goal). The mapping is strong in principle but operates at a different measurement level. Additionally, AgRP is a hunger-specific circuit; REE's drive_level is a generic need-state scalar.

## Evidence class

Causal intervention (optogenetics in mice, Nature Neuroscience).
