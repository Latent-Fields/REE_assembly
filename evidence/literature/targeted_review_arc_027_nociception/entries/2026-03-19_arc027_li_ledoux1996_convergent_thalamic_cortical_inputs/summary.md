# Literature Summary: 2026-03-19_arc027_li_ledoux1996_convergent_thalamic_cortical_inputs

## Claims Tested

- `ARC-027`

## Source

- Li XF, Stutzmann GE, LeDoux JE (1996). *Convergent but temporally separated inputs to lateral amygdala neurons from the auditory thalamus and auditory cortex use different postsynaptic receptors*. Learning & Memory, 3(2–3), 229–242.
- DOI: `10.1101/lm.3.2-3.229`
- URL: `https://pubmed.ncbi.nlm.nih.gov/10456093/`

## Source Wording

Individual lateral amygdala neurons receive convergent inputs from the auditory thalamus (~12ms latency) and auditory cortex (~22ms latency). Thalamic transmission depends on both AMPA and NMDA receptors; cortical transmission uses only AMPA receptors. The NMDA involvement gives the thalamic synapse temporal integration and Hebbian plasticity properties absent from the cortical input.

## REE Translation

**ARC-027**: The parallel thalamic and cortical pathways to the amygdala are not just anatomically distinct — they are computationally distinct. The thalamic (low-road) synapse has NMDA-mediated temporal integration capacity, while the cortical (high-road) synapse does not. This deepens ARC-027: the HARM stream is not a redundant copy of the E1 world-model signal; it has its own processing properties. In REE implementation, the harm-detection module should have its own temporal integration logic — it is not equivalent to reading z_world from E1 at any time step.

## Caveat

Auditory fear conditioning circuit, not nociceptive circuit directly. Receptor mechanism generalization to the spinothalamic → posterior thalamic → amygdala nociceptive route is plausible but not directly evidenced in this study.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.82`
