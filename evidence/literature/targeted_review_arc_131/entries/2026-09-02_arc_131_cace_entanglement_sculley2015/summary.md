# Sculley et al. (2015) -- CACE, and the limits of what a position paper can evidence

**Claim tested:** ARC-131 (installability is a competence dissociable from isolated component-level validation)
**Direction:** supports | **Confidence:** 0.48

## What the paper did

This is a practitioner account of running machine-learning systems in production, framed through the
software-engineering notion of technical debt. It catalogues ML-specific debt sources -- boundary
erosion, hidden feedback loops, undeclared consumers, data dependencies, configuration debt -- and
in the section relevant here, entanglement. Because ML models mix signals, no input is ever really
independent: "Machine learning systems mix signals together, entangling them and making isolation of
improvements impossible." If the input distribution of one feature changes, "the importance,
weights, or use of the remaining features may all change", and adding or removing any feature does
the same. The authors name this the CACE principle -- Changing Anything Changes Everything -- and
extend it beyond input signals to hyper-parameters, learning settings, sampling methods, convergence
thresholds and data selection.

## Why it bears on ARC-131

ARC-131 says a component-level PASS establishes that an operation is possible but not that the whole
agent can enter the states where the mechanism operates, nor that it remains competitive once other
mechanisms are enabled. CACE is a strikingly close restatement of the premise, and the value here is
in *who* is saying it. This is a mature engineering discipline, working on a completely different
substrate, arriving independently at the conclusion that isolated component validation does not
survive composition -- and building process around that conclusion rather than treating it as an
excuse. That independence is the argument against reading ARC-131 as a REE-local rationalisation for
inconvenient nulls. Three of the seven operating-condition channels ARC-131 enumerates (input state
distribution, scale and weighting of competing signals, configuration coupling) appear here in the
same causal role.

## Limitations and caveats

I want to be blunt about this entry's evidential weight, because it would be easy to let a famous
paper do more work than it can. Nothing in it is measured. There are no controls, no counterfactual,
and no quantification of how often isolated validation actually fails to transfer. It is a
retrospective account of one organisation's experience, and it should be weighted as
consensus-of-practice rather than as evidence. The confidence is set deliberately below 0.5 to make
that visible in the aggregate: ARC-131's case is not stronger for counting this as a fourth
supporting study, and the arithmetic in `claim_evidence.v1.json` should reflect that.

There is a second, more substantive limit. CACE is a claim about the difficulty of *attribution*
under composition -- you cannot cleanly isolate what a change did. ARC-131 makes a stronger claim:
*non-expression*, that the mechanism may never operate at all. The second does not follow from the
first. A system in which every component runs but their contributions cannot be disentangled
satisfies CACE completely and says nothing about installability. The non-expression half of ARC-131
is carried by the Csordas and Shazeer entries in this directory; this entry should not be read as
evidencing it, and I have said so in the record's `mapping_caveat` so that a future governance pass
does not silently promote it.

The granularity also differs. The entangled units here are features inside one model; ARC-131
concerns typed mechanisms composed into an agent. The mapping is by analogy of structure, not shared
substrate.

## Confidence reasoning

Source quality 0.55 -- peer-reviewed at NIPS, enormously influential, but scored on what the paper
*is* (an unmeasured experience report) rather than on its citation count, which reflects resonance.
Mapping fidelity 0.65: the general form matches well, the granularity does not, and the
attribution/non-expression gap is real. Transfer risk 0.45. Aggregate 0.48 -- kept just under the
0.5 line on purpose, as the calibration guide's "weak/ambiguous mapping" band, because the honest
description of this entry is that it tells us a serious discipline shares REE's premise, not that it
tests it.
