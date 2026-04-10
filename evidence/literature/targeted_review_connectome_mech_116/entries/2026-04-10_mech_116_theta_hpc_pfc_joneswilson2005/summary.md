# Summary: Jones & Wilson 2005

**Title:** Theta rhythms coordinate hippocampal-prefrontal interactions in a spatial memory task

**Authors:** Jones MW, Wilson MA

**Year:** 2005 | **Venue:** PLoS Biology | **DOI:** 10.1371/journal.pbio.0030402 | **PMID:** 16279838

---

## Core Finding

Using simultaneous CA1 hippocampus and mPFC tetrode recordings in rats performing a T-maze spatial alternation task (requiring working memory) vs. linear track running (no memory required), Jones and Wilson demonstrated that:

1. Hippocampal-mPFC spike correlations are selectively enhanced at theta frequencies (4-12 Hz) during working memory use
2. Both CA1 and mPFC neurons show enhanced theta phase-locking during memory-demanding trials
3. This enhancement is task-specific -- not present during locomotion-matched linear track running

## Relevance to MECH-116

This paper is foundational for the ThetaBuffer architecture (ARC-032) that MECH-116 relies upon. MECH-116's claim requires that hippocampal theta oscillations carry goal context to E1 across delay periods. Jones and Wilson show that this coupling channel is dynamically engaged specifically when working memory maintenance is behaviourally required, not tonically active. This supports the architectural prediction that the ThetaBuffer is a task-contingent coupling mechanism, not a continuous broadcast.

## Key Mechanism

Theta rhythms provide a temporal coordination mechanism that allows hippocampus and mPFC to exchange information at specific phases of the theta cycle during memory-demanding behavior. The coordination is at the population level (spike correlations) and at the single-unit level (phase-locking) -- suggesting both routing (which neurons communicate) and timing (when they communicate) are regulated by theta.

## Limitations / Transfer Risks

- Spatial task (T-maze alternation); goal-content may be location rather than abstract intention
- Direction of coupling (hippocampus driving mPFC vs. reciprocal vs. mPFC driving hippocampus) not isolated
- Confound between memory-related and locomotion-related theta during T-maze vs. linear track comparison
- Short delay period; does not test persistence of theta coupling over longer goal-maintenance intervals

## Evidence Direction: supports MECH-116

Provides mechanistic grounding for the task-contingent ThetaBuffer coupling that MECH-116 requires. The selectivity for working-memory-requiring behavior supports the claim that hippocampal-frontal theta coupling underlies goal-context maintenance, not general arousal or locomotion.
