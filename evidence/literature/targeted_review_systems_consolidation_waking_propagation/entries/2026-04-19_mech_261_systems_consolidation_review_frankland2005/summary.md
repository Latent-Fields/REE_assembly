# Frankland & Bontempi (2005) -- The organization of recent and remote memories

## What the paper does

This is the canonical Nature Reviews Neuroscience synthesis of systems consolidation
theory. It integrates rodent lesion work, human amnesic cases, and early functional
imaging data into a single framework: recently acquired memories depend on the medial
temporal lobe (MTL), and over days to months the trace becomes progressively dependent
on distributed neocortical networks. Hippocampal-cortical dialogue -- particularly
during sleep -- is the proposed mechanism that drives this redistribution. The authors
also carefully flag the tension between "standard consolidation theory" (the hippocampus
eventually releases its role) and "multiple trace theory" (the hippocampus retains a
role for rich episodic detail indefinitely).

## Relevance to MECH-261

MECH-261 asserts that a single operating-mode variable from the salience-network
coordinator (SD-032a) gates which substrates may write. The biological licence for
any such claim depends on the prior claim that the write-eligible substrates *do
differ by mode* -- otherwise mode gating has no downstream consequence. Frankland
and Bontempi provide exactly that foundation: the write-eligible substrate during
initial acquisition is hippocampus-centric, the write-eligible substrate during
long-term stabilisation is cortex-centric, and the handoff is driven by offline
hippocampal-cortical dialogue. In REE terms, this maps to: external_task acquires
into hippocampal-analog structures (MECH-092 waking SWR, ARC-038), internal_replay
and offline_consolidation progressively re-express that trace in cortical-analog
substrates (ARC-039 entorhinal grid loop), and it is the mode variable that governs
which pathway is live at a given moment.

## Caveats and mapping risks

The most important caveat is that Frankland and Bontempi describe a *graded,
time-extended* process. A memory trace does not flip from hippocampal to cortical --
it redistributes over weeks. MECH-261's discrete operating-mode variable
(external_task / internal_planning / internal_replay / offline_consolidation) is
an abstraction over this continuous biology. The translation is defensible as
long as the V3 implementation accepts that the mode variable controls *which
pathway is eligible*, not *how much consolidation has happened so far* -- the
latter is a separate, slower process that rides on top of the mode gating.

A second caveat: this paper is heavily sleep-focused. The waking-consolidation
bridge that the user explicitly asked about is downstream of Frankland and Bontempi
and requires the newer awake-SWR literature (Carr/Jadhav/Frank 2011, Tambini/Davachi
2019) to complete. Over-reliance on this paper alone biases MECH-261 toward
sleep-only consolidation, which would be a substantive error because INV-049 and
MECH-092 already commit the architecture to waking micro-quiescence replay.

## Confidence reasoning

Source quality is high -- this is one of the most-cited systems-consolidation
reviews in the field, written by two researchers whose labs have continued to
produce the primary data. Mapping fidelity is moderate because the paper does not
use a mode-variable framing; it describes anatomical redistribution. Transfer
risk is moderate -- treating graded hippocampal-cortical handoff as discrete mode
gating is an abstraction, not a mistranslation, but it requires the accompanying
awake-SWR evidence to stand up. Aggregate confidence 0.68: this is necessary
foundational grounding for MECH-261, but is insufficient alone.
