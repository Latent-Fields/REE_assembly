# Literature Summary: 2026-03-19_arc027_romanski_ledoux1992_thalamo_amygdala_equipotential

## Claims Tested

- `ARC-027`

## Source

- Romanski LM, LeDoux JE (1992). *Equipotentiality of thalamo-amygdala and thalamo-cortico-amygdala circuits in auditory fear conditioning*. Journal of Neuroscience, 12(11), 4501–4509.
- DOI: `10.1523/JNEUROSCI.12-11-04501.1992`
- URL: `https://pubmed.ncbi.nlm.nih.gov/1331362/`

## Source Wording

Selective lesions show that either the thalamo-amygdala pathway (fast, coarse signal direct from auditory thalamus to lateral amygdala) or the thalamo-cortico-amygdala pathway (slower, refined signal via auditory cortex) is individually sufficient for auditory fear conditioning. Both must be destroyed together to disrupt conditioning. The two pathways are equipotential and parallel — they carry overlapping information via different routes with different temporal properties.

## REE Translation

**ARC-027 (nociception as parallel sensory pathway)**: This is the experimental proof-of-concept for the low-road/high-road architecture. The HARM stream does not require E1 (cortical) processing to reach the amygdala-equivalent harm-detection system. A direct thalamic route operates in parallel and is independently sufficient. In REE terms: harm_eval cannot be a head on z_world precisely because the biological HARM stream bypasses the cortical world-model formation stage. The thalamic route for nociception (spinothalamic → posterior thalamic nuclei VPM/Po → lateral amygdala) follows the same parallel architecture demonstrated here for auditory stimuli.

The EXQ-043/044 calibration collapses are explained by this finding: trying to train harm_eval through E1's world model processing pipeline is asking the slow cortical pathway to do the work of the dedicated fast thalamic pathway.

## Caveat

Experiment uses auditory conditioned stimuli, not nociception directly. The nociceptive thalamo-amygdala projection (VPM/Po → lateral amygdala) follows the same architectural logic but via anatomically distinct thalamic nuclei. The parallel-pathway principle is directly transferable; the specific nociceptive anatomy requires supporting evidence from other sources.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.88`
