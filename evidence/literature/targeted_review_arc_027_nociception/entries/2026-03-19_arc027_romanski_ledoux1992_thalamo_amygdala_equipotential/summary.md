# Literature Summary: 2026-03-19_arc027_romanski_ledoux1992_thalamo_amygdala_equipotential

## Claims Tested

- (none scored) -- formerly `ARC-027`; see *Scoring exclusion* below. The ARC-027 association survives in this entry's directory name and `tags` (`arc-027`, `formerly_claim_ids_tested:ARC-027`).

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

## Scoring exclusion (2026-09-01 governance, GFLAG-0085)

[2026-09-01 governance, govapply-20260901, GFLAG-0085] UNTAGGED FROM ARC-027's SCORED EVIDENCE, deliberately -- this record is NOT defective and is NOT being disowned. ARC-027 is a FUSED claim: its own what_would_answer separates an OUT-OF-DOMAIN neuroanatomy leg (LeDoux's 'low road') from the one testable REE leg (harm-signal PRECEDENCE in the pipeline), and states of this record and its two siblings that they are 'the claim's biological GROUNDING, not its falsifier, and must never be scored as though a V3 run confirmed or weakened it.' They were nonetheless the ONLY three literature entries attached to ARC-027, so they alone produced literature_confidence 0.821, which cleared the 0.55 lit gate and -- combined with 6 experimental entries that are ALL SD-010's, 0 independent -- put ARC-027 in the confirmed_established quadrant on evidence its own text says cannot bear on it. Removing the claim_ids_tested tag is the minimal fix: it stops the scoring without losing the association, which survives in this record's directory name, in its `tags` ('arc-027'), and by name in ARC-027's own prose (all three papers are cited there). Precedent for fixing a join rather than a record: GFLAG-0032, build_experiment_indexes.py:3613-3629. If a claim is ever registered for the neuroanatomy question itself, retag to that.

Provenance of this section: migrated 2026-09-08 (session admiring-heisenberg-6c7b32, chip-20260907-arc027-lit-schema-fix) from two `record.json` top-level keys, `scoring_exclusion_note` and `formerly_claim_ids_tested`, which the closed `literature_evidence/v1` schema rejects. Per `INTERFACE_CONTRACT.md`, prose lives here and the per-entry label lives in `tags` (`scoring_excluded:gflag-0085`, `formerly_claim_ids_tested:ARC-027`). Meaning unchanged.
