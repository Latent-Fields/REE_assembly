# Literature Summary: 2026-03-19_arc027_guirimand_lebars1996_nociception_physiology

## Claims Tested

- `ARC-027`

## Source

- Guirimand F, Le Bars D (1996). *Physiology of nociception*. Annales françaises d'anesthésie et de réanimation, 15(7), 1048–1079.
- DOI: `10.1016/S0750-7658(96)89477-9`
- URL: `https://pubmed.ncbi.nlm.nih.gov/9180983/`

## Source Wording

Nociception involves dedicated peripheral afferents (unmyelinated C fibres and fine myelinated Aδ fibres), ascending via spinothalamic and spinoreticular tracts to supraspinal sites including the parabrachial area, PAG, and the amygdala and hypothalamus as motivational and neuroendocrine targets. Cortical nociceptive processing (cingulate, insular, somatosensory cortex) represents a secondary layer above these subcortical harm-detection substrates.

## REE Translation

**ARC-027**: Nociception is not an aspect of general exteroceptive sensory processing — it has dedicated peripheral fibres, dedicated spinal pathways, and reaches the amygdala-equivalent harm-detection substrate *before* cortical world-model processing. This confirms that deriving harm_eval from z_world (E1's cortical output) is architecturally incorrect: the HARM stream feeds the harm-detection system at a subcortical stage. The descending pain-modulation system (PAG, raphe magnus) provides the biological analog for top-down modulation of the HARM stream by commitment state and context — consistent with MECH-094 (hypothesis tag gating).

## Caveat

General review; the direct posterior-thalamus → amygdala nociceptive projection is mentioned but not the primary focus. Useful for establishing the dedicated-afferent and ascending-pathway claims but less specific than Romanski & LeDoux 1992 for the parallel-architecture argument.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.80`
