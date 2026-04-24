# Bryden, Johnson, Tobia, Kashtelyan & Roesch 2011 -- ACC attention-for-learning

## Source
Bryden DW, Johnson EE, Tobia SC, Kashtelyan V, Roesch MR. Attention for learning signals in anterior cingulate cortex. J Neurosci 31(50):18266-18274. DOI: 10.1523/JNEUROSCI.4715-11.2011

## Finding
Rat ACC single units encode two distinguishable dynamics: (1) reward prediction errors on trials with unexpected value (upshifts and downshifts), and (2) an attention-for-learning signal (elevated activity on trials SUBSEQUENT to unexpected outcomes, consistent with the Pearce-Hall account of how surprise drives learning). ACC activity during cue sampling also tracks reward size but not delay. The ACC error signal is context-dependent and gain-modulated -- not an unsaturated raw error.

## Why it maps to MECH-268
MECH-268 asserts that the dACC-analog (SD-032b) pe signal saturates under repeated identical outcomes via a FIFO outcome-history mechanism, so that sustained conflict does not generate unbounded pe.

Bryden et al. support the architectural premise that biological ACC pe is NOT a raw unsaturated error signal -- it is dynamically modulated by context (attention-for-learning elevates after surprise; stays low under expectedness). This is the general shape MECH-268 requires: ACC error output is gated / shaped by a dynamic variable, not pure pe.

However, the paper does NOT directly demonstrate habituation under repeated identical outcomes. Its paradigm tests change-points (value shifts), not sustained identical-outcome streams. The specific saturation claim of MECH-268 remains undertested by this evidence.

## Important mapping caveat re: plan citation
The 2026-04-20 sd033_governance_plan.md cites "Bryden 2019" for dACC habituation biology. That exact citation does not resolve on PubMed. Bryden et al 2011 (Roesch lab, ACC electrophysiology) is the closest available paper and appears to be what the plan intended. This substitution is flagged in the mapping_caveat -- if the user intended a different paper (e.g. a review that cites Bryden 2011), that should be pulled in a follow-up.

## Confidence: 0.58 (mixed)
- source_quality 0.78 (J Neurosci, Roesch lab, clean recording, replicated phenomena)
- mapping_fidelity 0.45 (supports architectural premise, not the specific saturation dynamic)
- transfer_risk 0.55 (rodent ACC -> REE dACC-analog; plan-citation substitution adds additional uncertainty)

## Key limitations
- Paradigm tests change-point attention, not sustained repeated-outcome habituation. The specific MECH-268 dynamic is empirically unresolved at this timescale.
- The attention-for-learning framing (Pearce-Hall) is compatible with gain-modulation of an underlying raw pe rather than saturation of the pe itself. MECH-268 may be the wrong mechanism description if gain-modulation is the better account.
- Plan-citation substitution introduces uncertainty: if the user had a specific Bryden 2019 paper in mind, this entry may not be the intended evidence.

## Failure signatures
- If ACC pe is better described as gain-modulated by an external attention variable (Pearce-Hall-style) rather than saturated by its own outcome history, MECH-268 is framed incorrectly.
- If the saturation timescale MECH-268 assumes is longer than typical task episodes (hundreds of repeated outcomes), Bryden 2011-style paradigms cannot detect it and the mechanism needs a different empirical target.
- If the plan-cited "Bryden 2019" is a real separate paper with direct saturation evidence, this entry is a substitution stand-in; a targeted follow-up should replace it.
