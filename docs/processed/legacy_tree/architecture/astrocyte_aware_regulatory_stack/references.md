# References

This document provides an annotated list of key references on astrocytes, neuromodulation, and their computational roles. It supports the claims made in the Astrocyte-aware Regulatory Stack documentation.

## Format

Citations follow a simple consistent style: Author(s), "Title," *Journal* **Volume** (Year): Pages. [Optional: DOI or URL]

## General audience summary

**Quanta Magazine article on astrocytes**

- Cepelewicz, J., "The Brain Cells That Can 'Taste' Danger," *Quanta Magazine* (2023).  
  [https://www.quantamagazine.org/the-brain-cells-that-can-taste-danger-20231016/](https://www.quantamagazine.org/the-brain-cells-that-can-taste-danger-20231016/)
  
  **Summary:** Accessible overview of recent discoveries about astrocyte roles in sensing and responding to neural activity, metabolic state, and neuromodulatory signals. Emphasizes the shift from viewing astrocytes as passive support cells to recognizing them as active computational participants.

## Primary neuroscience sources

### Astrocyte calcium signaling and neuromodulation

- Bazargani, N., & Attwell, D., "Astrocyte calcium signaling: the third wave," *Nature Neuroscience* **19** (2016): 182–189.  
  [https://doi.org/10.1038/nn.4201](https://doi.org/10.1038/nn.4201)
  
  **Summary:** Reviews the evidence for astrocytic Ca²⁺ signaling as a computational substrate. Discusses spatial and temporal dynamics, triggers (neurotransmitter spillover, neuromodulators), and functional consequences (gliotransmitter release, modulation of synaptic transmission). Clarifies what is established vs. controversial.

- Paukert, M., Agarwal, A., Cha, J., Doze, V. A., Kang, J. U., & Bergles, D. E., "Norepinephrine controls astroglial responsiveness to local circuit activity," *Neuron* **82** (2014): 1263–1270.  
  [https://doi.org/10.1016/j.neuron.2014.04.038](https://doi.org/10.1016/j.neuron.2014.04.038)
  
  **Summary:** Demonstrates that noradrenaline (norepinephrine) modulates astrocytic calcium signaling in a state-dependent manner. Shows that astrocytes integrate neuromodulatory signals with local synaptic activity, supporting the "meta-regulatory" framing (monoamines bias astrocytic state, which then modulates synaptic function).

### Astrocytes and synaptic plasticity

- Henneberger, C., Papouin, T., Oliet, S. H., & Rusakov, D. A., "Long-term potentiation depends on release of D-serine from astrocytes," *Nature* **463** (2010): 232–236.  
  [https://doi.org/10.1038/nature08673](https://doi.org/10.1038/nature08673)
  
  **Summary:** Shows that astrocytes release D-serine (a co-agonist of NMDA receptors), which is required for the induction of long-term potentiation (LTP) in hippocampal synapses. Establishes astrocytes as regulators of synaptic plasticity, not just synaptic transmission.

- Papouin, T., Dunphy, J., Tolman, M., Foley, J. C., & Haydon, P. G., "Astrocytic control of synaptic function," *Philosophical Transactions of the Royal Society B* **372** (2017): 20160154.  
  [https://doi.org/10.1098/rstb.2016.0154](https://doi.org/10.1098/rstb.2016.0154)
  
  **Summary:** Comprehensive review of astrocytic modulation of synaptic transmission and plasticity. Discusses mechanisms (gliotransmitter release, regulation of extracellular ion concentrations, control of neurotransmitter reuptake) and functional implications (gain control, temporal integration, learning rate modulation).

### Astrocytes and metabolic constraints

- Magistretti, P. J., & Allaman, I., "A cellular perspective on brain energy metabolism and functional imaging," *Neuron* **86** (2015): 883–901.  
  [https://doi.org/10.1016/j.neuron.2015.03.035](https://doi.org/10.1016/j.neuron.2015.03.035)
  
  **Summary:** Reviews the astrocyte-neuron lactate shuttle hypothesis and the role of astrocytes in coupling neural activity to metabolic supply. Establishes astrocytes as mediators between computational demand and energetic availability—directly relevant to the "care budget" concept.

### Astrocytic networks and spatial coupling

- Giaume, C., Koulakoff, A., Roux, L., Holcman, D., & Rouach, N., "Astroglial networks: a step further in neuroglial and gliovascular interactions," *Nature Reviews Neuroscience* **11** (2010): 87–99.  
  [https://doi.org/10.1038/nrn2757](https://doi.org/10.1038/nrn2757)
  
  **Summary:** Describes gap junction coupling between astrocytes (forming a syncytium) and its functional consequences. Discusses how astrocytic networks can integrate signals over spatial scales beyond individual cells, supporting the "regulatory field" framing.

## Review articles (broader context)

- Araque, A., Carmignoto, G., Haydon, P. G., Oliet, S. H., Robitaille, R., & Volterra, A., "Gliotransmitters travel in time and space," *Neuron* **81** (2014): 728–739.  
  [https://doi.org/10.1016/j.neuron.2014.02.007](https://doi.org/10.1016/j.neuron.2014.02.007)
  
  **Summary:** Reviews the concept of "gliotransmission" (signaling from astrocytes to neurons via release of glutamate, ATP, D-serine, etc.). Emphasizes the spatial and temporal scales of gliotransmission (slower and more diffuse than neuronal signaling), consistent with the "slow regulatory substrate" framing.

- Allen, N. J., & Lyons, D. A., "Glia as architects of central nervous system formation and function," *Science* **362** (2018): 181–185.  
  [https://doi.org/10.1126/science.aat0473](https://doi.org/10.1126/science.aat0473)
  
  **Summary:** Broad review of glial (including astrocyte) roles in brain development, function, and plasticity. Positions astrocytes as integral to neural computation, not auxiliary support.

## Theoretical / computational perspectives

- Manninen, T., Havela, R., & Linne, M. L., "Computational models for calcium-mediated astrocyte functions," *Frontiers in Computational Neuroscience* **12** (2018): 14.  
  [https://doi.org/10.3389/fncom.2018.00014](https://doi.org/10.3389/fncom.2018.00014)
  
  **Summary:** Reviews computational models of astrocytic calcium dynamics and their functional roles. Useful for understanding what timescales and spatial scales are appropriate for modeling \(R(x,t)\) in the regulatory field framework.

- De Pittà, M., & Berry, H., Eds., *Computational Glioscience*, Springer (2019).  
  [https://doi.org/10.1007/978-3-030-00817-8](https://doi.org/10.1007/978-3-030/00817-8)
  
  **Summary:** Edited volume covering computational approaches to modeling astrocytes and their interactions with neurons. Includes chapters on astrocyte-neuron networks, metabolic coupling, and information processing in glial networks. Relevant for future implementation of the regulatory field.

## Neuromodulation and regulatory control (broader context)

- Marder, E., "Neuromodulation of neuronal circuits: back to the future," *Neuron* **76** (2012): 1–11.  
  [https://doi.org/10.1016/j.neuron.2012.09.010](https://doi.org/10.1016/j.neuron.2012.09.010)
  
  **Summary:** Classic review of neuromodulation in neural circuits. Emphasizes that neuromodulation is context-dependent, history-dependent, and mediated by multiple interacting systems (not simple "knobs"). Conceptually consistent with the regulatory stack framing, though does not focus specifically on astrocytes.

- Shine, J. M., "Neuromodulatory influences on integration and segregation in the brain," *Trends in Cognitive Sciences* **23** (2019): 572–583.  
  [https://doi.org/10.1016/j.tics.2019.04.002](https://doi.org/10.1016/j.tics.2019.04.002)
  
  **Summary:** Reviews how monoaminergic systems (dopamine, noradrenaline, serotonin, acetylcholine) modulate large-scale network dynamics (integration vs. segregation). Complements the astrocytic perspective by showing that monoamines have spatially and temporally extended effects mediated by complex substrates (which may include astrocytes).

## Epistemic status of astrocyte-aware regulatory stack

**Established neuroscience:**

- Astrocytes sense neural activity and release gliotransmitters.
- Astrocytic Ca²⁺ dynamics modulate synaptic transmission and plasticity.
- Astrocytes express monoamine receptors and respond to neuromodulatory signals.
- Astrocytes are coupled via gap junctions, forming spatially extended networks.
- Astrocytes mediate metabolic supply to neurons.

**Hypothesis / active research:**

- The "regulatory field" \(R(x,t)\) as a unified computational abstraction (this is a simplification for modeling purposes, not a claim about a single biophysical variable).
- The precise timescales and spatial scales of astrocytic modulation in behaving animals (much of the evidence comes from slice preparations or anesthetized animals).
- Whether astrocytic dynamics can be considered a quasi-independent "layer" of computation or are better understood as tightly coupled to neuronal dynamics.

**REE-specific framing:**

- The mapping of astrocytic control to REE concepts (precision, care budget, inertia) is **an architectural hypothesis**. It is informed by neuroscience but is not a direct empirical claim.

## How to cite this documentation

If you use the astrocyte-aware regulatory stack framing in your work, please cite:

- This repository: Latent Fields, *Reflective-Ethical Engine (REE)*, GitHub, [https://github.com/Latent-Fields/Reflective-Ethical-Engine-assembled](https://github.com/Latent-Fields/Reflective-Ethical-Engine-assembled)
- This module: "Astrocyte-aware Regulatory Stack," in *Reflective-Ethical Engine (REE)*, docs/astrocyte_aware_regulatory_stack/ (2024).

And consider citing the key neuroscience references listed above that support the claims made in this documentation.

## Further reading

For readers interested in deeper dives:

- **Active Inference and Free Energy:** Friston, K., "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience* **11** (2010): 127–138. (Contextualizes precision control in the broader predictive processing framework that REE builds on.)
- **Astrocytes and learning:** Santello, M., Toni, N., & Volterra, A., "Astrocyte function from information processing to cognition and cognitive impairment," *Nature Neuroscience* **22** (2019): 154–166. (Reviews astrocytic roles in learning and memory, relevant to REE's plasticity and care budget concepts.)
- **Metabolic constraints on computation:** Laughlin, S. B., & Sejnowski, T. J., "Communication in neuronal networks," *Science* **301** (2003): 1870–1874. (Discusses energetic costs of neural computation, providing context for why metabolic constraints matter in REE.)
