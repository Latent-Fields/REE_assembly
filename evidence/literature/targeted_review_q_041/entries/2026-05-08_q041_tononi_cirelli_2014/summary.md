# Tononi & Cirelli 2014 — Sleep and the price of plasticity

**Source:** Tononi G, Cirelli C. *Neuron* 81(1):12-34 (2014). [DOI](https://doi.org/10.1016/j.neuron.2013.12.025). PMID 24411729, PMCID PMC3921176. According to PubMed.

## What the paper did

This is the canonical statement of the Synaptic Homeostasis Hypothesis (SHY). The authors argue, with a decade of accumulated empirical evidence, that the function of sleep -- particularly slow-wave sleep -- is to globally renormalise synaptic strength. During wakefulness, learning drives a net potentiation across many synapses; this is metabolically expensive, saturates the dynamic range of plasticity, and degrades the signal-to-noise of subsequent learning. Sleep spontaneously down-selects synapses in an activity-dependent way, restoring the aggregate distribution of weights to a sustainable baseline. The renormalisation is global, simultaneous, and serves several functions at once -- energy, memory consolidation, integration, and restoration of plasticity headroom.

## Why it matters for Q-041

Q-041's second motivating gap is sleep-mediated writeback: REE has captured the precision-zero-point snapshot at REM entry (MECH-204) but lacks the writeback path that uses it to recalibrate waking thresholds. SHY is a positive existence proof. The brain does have a global recalibration arm; it does fire at the sleep-bout timescale; and it does touch many substrates simultaneously rather than fine-tuning each one separately. Whatever Q-041's eventual architecture, the sleep arm of the answer is constrained by SHY in the following way: the recalibration is not a fine-grained per-substrate update; it's a coarse global step that resets headroom across the whole system at once.

This favours a hybrid reading of Q-041. REE almost certainly does not need a single waking-time supervisor that aggregates across SD-032c/d/e and ARC-016 in real time. But REE almost certainly does need a sleep-bout-scale arm that resets all of them coherently. The current REE substrate has neither -- it has only the fast per-substrate EMAs.

## Mapping to REE

There is a level-of-description gap to be honest about. SHY is a hypothesis at the level of synaptic weight; REE's threshold supervisor is one architectural level above that, at the level of decision/commit/release thresholds. The translation is not literal; it requires assuming that the biological pattern (global, sleep-timescale, activity-dependent renormalisation of accumulated change) transfers to a computational pattern (global, sleep-timescale recalibration of accumulated threshold drift). The transfer is plausible -- in computational models, a system without periodic global renormalisation will accumulate drift exactly the way SHY predicts biological systems would -- but it is one step beyond what the paper directly establishes.

Where this maps in REE substrate: INV-049 (sleep necessity) is already registered as the offline phase needed for model-building agents. MECH-204 captures the precision zero-point at REM entry. SD-049 (registered in the planning queue) is the closest design slot for the writeback arm; EXQ-538 (queued, gated on EXQ-537) tests the sleep-on variant of the same paradigm. Tononi & Cirelli give the architectural prediction REE's sleep arm should be tested against: thresholds across substrates should track each other tighter when the sleep loop is on than when it is off, especially under chronic load.

## Caveats

SHY is a hypothesis, not a settled finding. Alternative theories of sleep function -- active replay (Stickgold, Walker), glymphatic clearance (Xie, Nedergaard 2013), metabolic restoration -- emphasise different mechanisms. They are not necessarily exclusive of SHY, but the field is not unified around any single account. Some empirical predictions of SHY are contested (e.g., the literal "down-selection" picture; see Frank 2012/2018). The right move for REE is to map SHY's architectural pattern (global, sleep-timescale recalibration) as a candidate slot, while leaving the specific mechanism underdetermined -- replay, renormalisation, or both.

## Confidence reasoning

0.80 supports for Q-041. Source quality very high (Neuron review by hypothesis originators, foundational reference, hundreds of citations of follow-on empirical work). Mapping fidelity high-moderate (0.75): SHY is the right architectural slot but described one level below REE's threshold question. Transfer risk low-moderate (0.25): the architectural pattern transfers cleanly even if the specific synaptic mechanism does not. Tagged also against INV-049 because the paper is foundational to REE's sleep-necessity claim, not just to Q-041.
