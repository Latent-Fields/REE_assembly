# Literature Summary: 2026-03-19_arc027_li_ledoux1996_convergent_thalamic_cortical_inputs

## Claims Tested

- (none scored) -- formerly `ARC-027`; see *Scoring exclusion* below. The ARC-027 association survives in this entry's directory name and `tags` (`arc-027`, `formerly_claim_ids_tested:ARC-027`).

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

## Scoring exclusion (2026-09-01 governance, GFLAG-0085)

[2026-09-01 governance, govapply-20260901, GFLAG-0085] UNTAGGED FROM ARC-027's SCORED EVIDENCE, deliberately -- this record is NOT defective and is NOT being disowned. ARC-027 is a FUSED claim: its own what_would_answer separates an OUT-OF-DOMAIN neuroanatomy leg (LeDoux's 'low road') from the one testable REE leg (harm-signal PRECEDENCE in the pipeline), and states of this record and its two siblings that they are 'the claim's biological GROUNDING, not its falsifier, and must never be scored as though a V3 run confirmed or weakened it.' They were nonetheless the ONLY three literature entries attached to ARC-027, so they alone produced literature_confidence 0.821, which cleared the 0.55 lit gate and -- combined with 6 experimental entries that are ALL SD-010's, 0 independent -- put ARC-027 in the confirmed_established quadrant on evidence its own text says cannot bear on it. Removing the claim_ids_tested tag is the minimal fix: it stops the scoring without losing the association, which survives in this record's directory name, in its `tags` ('arc-027'), and by name in ARC-027's own prose (all three papers are cited there). Precedent for fixing a join rather than a record: GFLAG-0032, build_experiment_indexes.py:3613-3629. If a claim is ever registered for the neuroanatomy question itself, retag to that.

Provenance of this section: migrated 2026-09-08 (session admiring-heisenberg-6c7b32, chip-20260907-arc027-lit-schema-fix) from two `record.json` top-level keys, `scoring_exclusion_note` and `formerly_claim_ids_tested`, which the closed `literature_evidence/v1` schema rejects. Per `INTERFACE_CONTRACT.md`, prose lives here and the per-entry label lives in `tags` (`scoring_excluded:gflag-0085`, `formerly_claim_ids_tested:ARC-027`). Meaning unchanged.
