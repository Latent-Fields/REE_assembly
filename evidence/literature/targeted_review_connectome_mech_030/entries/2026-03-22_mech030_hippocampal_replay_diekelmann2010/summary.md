# Literature Summary: 2026-03-22_mech030_hippocampal_replay_diekelmann2010

## Claims Tested

- `MECH-030`

## Source

- Diekelmann S, Born J (2010). *The memory function of sleep*. Nature Reviews Neuroscience.
- DOI: `10.1038/nrn2762`
- URL: `https://www.nature.com/articles/nrn2762`

## Source Wording

During NREM slow-wave sleep, hippocampal sharp-wave ripples (SWRs) reactivate ensemble representations of recently
acquired experience. These SWR-associated hippocampal reactivations are temporally coupled with thalamo-cortical sleep
spindles (12-15 Hz), which are themselves nested within cortical slow oscillations (~0.75 Hz). This three-frequency
nesting creates a replay-to-cortex transfer window: the UP state of the slow oscillation opens a brief period in which
hippocampal replay (SWR) can drive neocortical spindle-mediated long-term potentiation, progressively reducing
hippocampal dependence and transferring the memory trace to distributed cortical networks. This process is blocked
during active waking -- tonic cholinergic drive during wakefulness suppresses hippocampal-to-cortical transmission and
prevents premature consolidation.

REM sleep plays a complementary role: it is associated with offline reprocessing of emotional and fear-related memories,
dampening affective tone while preserving factual content, and may serve a precision recalibration function for
emotionally valenced material.

## REE Translation

MECH-030 specifies that REE's sleep/offline consolidation mode operates via DMN-like hippocampal-cortical replay while
suppressing online commit signals. Diekelmann & Born supply the biological blueprint at each structural point:

1. **Replay is internally generated and offline.** SWR replay requires no new sensory input. This matches the
   requirement that MECH-030's consolidation phase is not driven by incoming task demands.

2. **Commit signals are suppressed during consolidation.** High cholinergic tone during waking prevents hippocampal-
   cortical transfer; the offline phase requires this suppression. In REE terms, the commit boundary must be protected
   during consolidation -- no new irreversible action commitments may be issued while the system is in sleep/consolidation
   mode (see ARC-020).

3. **Consolidation recalibrates which representations survive.** The replay process is selective -- prioritized
   by novelty, emotional salience, and relevance. This maps onto MECH-030's function of recalibrating mode
   boundaries and contextualising ethical residue: residue that is spurious or misattributed is candidates for
   downscaling, while genuine harm traces are preserved.

4. **Multi-timescale structure.** The three-frequency nesting (slow oscillation / spindle / SWR) provides a
   biological precedent for MECH-030's requirement that offline consolidation operates on slower timescales
   than online action.

## Caveat

MECH-030 is explicitly V4 scope in REE -- the sleep mode is not implemented in V1, V2, or V3 substrates. This entry
provides architectural motivation, not experimental validation. The biological consolidation timescale (hours of sleep,
across multiple nights for strong memories) is unlikely to be reproducible in any near-term REE experiment; the
computational analog will require careful re-specification. The specific role of REM sleep in emotional memory
recalibration (relevant to residue contextualisation) has a less settled mechanistic account than NREM consolidation and
should be treated with more caution in REE architectural decisions.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.88`
