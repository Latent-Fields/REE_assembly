# Literature Summary: 2026-03-19_arc017_vestibular_lopez_blanke2011_thalamocortical

## Claims Tested

- `ARC-017`

## Source

- Lopez C, Blanke O (2011). *The thalamocortical vestibular system in animals and humans*. Brain Research Reviews, 67(1–2), 119–146.
- DOI: `10.1016/j.brainresrev.2010.12.002`
- URL: `https://pubmed.ncbi.nlm.nih.gov/21223979/`

## Source Wording

The vestibular system provides signals about 3D head rotations and translations via vestibular nuclei → multiple thalamic nuclei → vestibular cortex (PIVC, parietal, MST, frontal, hippocampus). Thalamic relay neurons are multisensory, integrating vestibular with proprioceptive and visual signals. Vestibular projections influence self-motion perception, spatial navigation, internal models of gravity, and bodily self-consciousness.

## REE Translation

**ARC-017 (VESTIBULAR stream tag)**: The vestibular system has a dedicated thalamocortical pathway that is anatomically distinct from the proprioceptive pathway (S1) and the exteroceptive WORLD pathway. VESTIBULAR feeds z_self's spatial orientation and self-motion components via PIVC and posterior parietal/MST projections — grounding the egocentric frame used by E2 for motor-sensory prediction. The hippocampal projection confirms vestibular signals contribute to the spatial map (relevant for ARC-007), since path integration requires self-motion signals from the vestibular system. The early multisensory nature of thalamic vestibular neurons (integrating vestibular + proprioceptive + visual) means VESTIBULAR is already partially fused with SELF_SENSORY at the thalamic stage — supporting the ARC-017 description of VESTIBULAR feeding SELF_SENSORY alongside proprioception.

## Caveat

Biological PIVC maps to a dedicated vestibular cortex that has no direct equivalent in REE's current architecture. The mapping to z_self is REE-specific. The multisensory thalamic integration means the VESTIBULAR stream is not purely vestibular even at early stages.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.85`
