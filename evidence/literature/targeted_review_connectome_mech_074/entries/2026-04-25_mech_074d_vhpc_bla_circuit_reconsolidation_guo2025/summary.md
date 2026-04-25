# Guo et al. 2025 — vCA1-BLA Circuit for US Reconsolidation (MECH-074d)

**Source:** Guo D, Wang Z, Liu F, Chen W, Gao X, Huang S, Tabarak S, Yao Y, Zhang S, Shi J, Lu L, Han Y. "A ventral hippocampus-basolateral amygdala circuit regulates the unconditioned stimulus retrieval-induced reconsolidation of remote fear memory." *Journal of Advanced Research* 2025. DOI: 10.1016/j.jare.2025.10.015

## What the paper did

Guo et al. investigate the neural circuitry underlying reconsolidation of remote (> 28-day-old) contextual fear memories in rats. They show that pharmacological disruption of reconsolidation following unconditioned stimulus (US = footshock) retrieval — unlike conditioned stimulus retrieval — produces lasting, reinstatement-resistant memory erasure for remote memories. Using retrograde tracing, fiber photometry, and chemogenetics (DREADDs), they identify the ventral hippocampal CA1 (vCA1) → BLA pathway as specifically engaged during US retrieval-induced reconsolidation but not CS retrieval. Chemogenetic inhibition of vCA1-BLA after US retrieval disrupts remote fear memory with long-term efficacy; activation of vCA1-BLA blocks propranolol's reconsolidation-blocking effect.

## Key findings relevant to MECH-074d

Three findings are particularly important for MECH-074d. First, the US-specificity of vCA1-BLA engagement: the circuit is activated by harm-PE reactivation (US = the harm event itself), not by mere context-CS recall. This supports MECH-074d's claim that the remap_signal requires an active harm-PE (||z_harm_a - E2_harm_a_pred|| > threshold), not passive context retrieval. Second, the bidirectional chemogenetic dissection confirms that the vCA1-BLA connection is causally necessary for remote fear memory reconsolidation — establishing the circuit substrate for the BLA-hippocampus update loop that MECH-074d relies on. Third, resistance to reinstatement in the inhibition condition suggests that the vCA1-BLA circuit specifically governs the memory's re-lability window, which maps onto MECH-074d's remap_signal gating the plasticity window.

## Translation to MECH-074d

MECH-074d's remap_signal is triggered by harm-PE spike and flows BLA → HippocampalModule. Guo et al. show the biological circuit in the reverse direction is equally important (vCA1 → BLA) and is specifically engaged by harm events, not just context retrieval. This establishes the harm-PE trigger criterion as biologically sound — the vCA1-BLA pathway is selectively sensitive to harm reactivation. The full loop (vCA1 → BLA → back to HPC) is the biological substrate for the attribution-gated update: hippocampus feeds BLA with contextual information about which latent codes were active during harm, BLA evaluates PE amplitude, and then modulates hippocampal plasticity via return projections.

## Limitations and caveats

The paper focuses on ventral HPC (motivational/affective axis), not dorsal HPC (spatial/planning axis where E3's viability map operates). Whether the same circuit governs remapping in dorsal CA1 — which is the REE substrate — is not addressed. The remap_signal in MECH-074d flows BLA → hippocampus; Guo et al. characterise vCA1 → BLA as the key direction for reconsolidation. The return BLA → HPC projection (MECH-074d's remap_signal direction) is anatomically known but not the focus of this study.

## Confidence

0.74. Strong chemogenetic circuit evidence; US-specificity finding directly supports harm-PE trigger criterion. Confidence limited by ventral vs dorsal HPC distinction and directionality mismatch (vCA1 → BLA rather than BLA → HPC).
