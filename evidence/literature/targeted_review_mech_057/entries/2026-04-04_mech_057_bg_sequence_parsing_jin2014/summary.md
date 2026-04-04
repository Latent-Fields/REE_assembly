# Literature Summary: 2026-04-04_mech_057_bg_sequence_parsing_jin2014

## Claims Tested

- `MECH-057a` (Committed action sequences suppress sensory precision reweighting until execution completes)

## Source

- Jin X, Tecuapetla F, Costa RM (2014).
  *Basal ganglia subcircuits distinctively encode the parsing and concatenation of action sequences.*
  Nature Neuroscience, 17(3), 423-430. [DOI: 10.1038/nn.3632](https://doi.org/10.1038/nn.3632)
- PMID: 24464039 | PMC: PMC3955116

## What Was Studied

Jin et al. trained mice to execute learned rapid action sequences (lever-press sequences with defined ordering and timing) while recording single neurons across dorsal striatum. They specifically probed direct pathway (dSPN) and indirect pathway (iSPN) neurons and asked how each class encoded the temporal structure of the sequence.

## Key Findings

Two broad neural populations emerged. One encoded sequence boundaries: activity rose at the start and fell at the sequence's end (or the reverse), providing a parsing signal -- a discrete marker of where one sequence ends and another could begin. The other encoded the sustained execution state: activity was either tonically elevated or tonically suppressed throughout the whole sequence, regardless of which individual elements were being executed.

Crucially, dSPN and iSPN populations behaved differently during sequence performance, though both were active at initiation. During sustained execution, the two pathways diverged: this is the neural signature of the BG committing to a sequence and maintaining that commitment state until the final parsing event signals completion.

This two-population structure -- boundary detectors plus sustained execution encoders -- provides cellular-level evidence for the kind of gating architecture MECH-057a requires: the BG does not simply toggle open/closed at action onset; it maintains a committed state throughout a sequence, with dedicated neurons tracking that the sequence is not yet done.

## Mapping to MECH-057a

MECH-057a needs BG to enforce a committed-sequence state from initiation through to completion. The Jin et al. architecture is the substrate for this. Neurons encoding the complete sequence as a unit -- rather than step-by-step -- are the cellular correlates of the MECH-057a commitment gate. The indirect pathway's distinct mid-sequence behaviour is particularly relevant: iSPNs, which via the indirect pathway would suppress thalamic disinhibition and thus block new motor programs from being released, show differentiated sustained activity during sequence execution. This is consistent with the indirect pathway keeping the "gate closed" to competing motor programs (and, by extension, competing sensory inputs that could abort the sequence).

The link to sensory precision suppression specifically is inferential -- Jin et al. measured motor output and BG activity, not sensory processing. But the circuit substrate for sequence-level commitment is well established here.

## Caveats

The paper works in dorsal striatum of rodents performing a well-learned lever-press sequence. Generalisation to the broader cortico-striato-thalamo-cortical loop (which MECH-057a requires for sensory precision suppression at the cortical level) is an inference. The paper also does not address beta oscillations or precision weighting -- it characterises the cellular architecture. Its relevance to MECH-057a is indirect: it establishes that the BG has the circuit substrate for sequence-level gating, but does not test whether that gating suppresses sensory precision.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.65`
- Rationale: Strong evidence for sequence-level BG gating architecture; indirect but mechanistically coherent support for MECH-057a's committed-sequence suppression claim.
