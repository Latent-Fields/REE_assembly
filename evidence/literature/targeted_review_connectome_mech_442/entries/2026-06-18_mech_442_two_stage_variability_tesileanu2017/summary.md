# Tesileanu, Olveczky & Balasubramanian 2017 -- a basal-ganglia variability generator feeding a separate motor selector

*According to PubMed.* Tesileanu, Olveczky & Balasubramanian 2017, *eLife* ([DOI](https://doi.org/10.7554/eLife.20944)).

## What the paper did
This is a theory paper deriving the rules for efficient *two-stage* learning, using birdsong as the worked example. In the songbird, LMAN (the output of a basal-ganglia-related circuit) both induces vocal exploration -- the variability -- and contributes a corrective bias to the vocal output; that bias is gradually consolidated downstream in RA, a motor-cortex analog. Using stochastic gradient descent the authors derive how the tutor circuit's teaching signal should match the student circuit's plasticity rule for learning to be efficient, and show that mismatches impair it.

## Key findings relevant to MECH-442
The architectural claim is the convergence-relevant one: the structure that *generates diversity* (LMAN) is separate from, and upstream of, the structure that *produces the committed motor output* (RA), and the two are coupled through a consolidation process over time. This is the same separation the Kao & Brainard lesion study shows empirically, here given a formal RL treatment. It supports MECH-442's premise that REE's diversity-preserving structure should sit on the generation side (ARC-065) plus a dedicated variability mechanism (MECH-313), feeding the committed selector -- not be a property of the argmax itself.

## How it translates to REE
It reinforces locating MECH-442's "archive" upstream of / in parallel with the commit gate, with its contribution consolidated over training. The model's cautionary result -- that a mismatch between the tutor (variability) signal and the downstream plasticity rule impairs learning -- is a useful design warning: an REE diversity-injection coupled to committed selection has to be matched to the downstream learning/consolidation path, or it degrades rather than helps. That maps onto the REE concern that diversity reaching committed action must be *usable* (no F-quality regression), not merely present.

## Limitations and confidence
This is a model, not a measurement, and it addresses tutor-student consolidation rather than per-niche-elite retention specifically. It supports the separation-of-generator-from-selector architecture but is agnostic between a MAP-Elites archive and a simpler variability-injection-plus-bias account. Source quality is good (eLife, the Olveczky group); mapping fidelity is moderate; transfer risk is moderate. Net confidence 0.68, direction supports -- architecture-level corroboration that the diversity structure is upstream of the commit.
