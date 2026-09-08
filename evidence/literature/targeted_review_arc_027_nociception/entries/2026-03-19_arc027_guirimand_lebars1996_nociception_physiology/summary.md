# Literature Summary: 2026-03-19_arc027_guirimand_lebars1996_nociception_physiology

## Claims Tested

- (none scored) -- formerly `ARC-027`; see *Scoring exclusion* below. The ARC-027 association survives in this entry's directory name and `tags` (`arc-027`, `formerly_claim_ids_tested:ARC-027`).

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

## Scoring exclusion (2026-09-01 governance, GFLAG-0085)

[2026-09-01 governance, govapply-20260901, GFLAG-0085] UNTAGGED FROM ARC-027's SCORED EVIDENCE, deliberately -- this record is NOT defective and is NOT being disowned. ARC-027 is a FUSED claim: its own what_would_answer separates an OUT-OF-DOMAIN neuroanatomy leg (LeDoux's 'low road') from the one testable REE leg (harm-signal PRECEDENCE in the pipeline), and states of this record and its two siblings that they are 'the claim's biological GROUNDING, not its falsifier, and must never be scored as though a V3 run confirmed or weakened it.' They were nonetheless the ONLY three literature entries attached to ARC-027, so they alone produced literature_confidence 0.821, which cleared the 0.55 lit gate and -- combined with 6 experimental entries that are ALL SD-010's, 0 independent -- put ARC-027 in the confirmed_established quadrant on evidence its own text says cannot bear on it. Removing the claim_ids_tested tag is the minimal fix: it stops the scoring without losing the association, which survives in this record's directory name, in its `tags` ('arc-027'), and by name in ARC-027's own prose (all three papers are cited there). Precedent for fixing a join rather than a record: GFLAG-0032, build_experiment_indexes.py:3613-3629. If a claim is ever registered for the neuroanatomy question itself, retag to that.

Provenance of this section: migrated 2026-09-08 (session admiring-heisenberg-6c7b32, chip-20260907-arc027-lit-schema-fix) from two `record.json` top-level keys, `scoring_exclusion_note` and `formerly_claim_ids_tested`, which the closed `literature_evidence/v1` schema rejects. Per `INTERFACE_CONTRACT.md`, prose lives here and the per-entry label lives in `tags` (`scoring_excluded:gflag-0085`, `formerly_claim_ids_tested:ARC-027`). Meaning unchanged.
