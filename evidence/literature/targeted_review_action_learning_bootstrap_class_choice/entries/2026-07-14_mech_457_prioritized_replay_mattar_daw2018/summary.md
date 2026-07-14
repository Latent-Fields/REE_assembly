# Prioritized memory access explains planning and hippocampal replay

**Class surveyed:** MEMORY / REVERSE-REPLAY CREDIT | **Evidence direction:** supports | **Confidence:** 0.75

**Source:** Marcelo G. Mattar, Nathaniel D. Daw (2018). *Prioritized memory access explains planning and hippocampal replay.* Nature Neuroscience 21:1609-1617 DOI: 10.1038/s41593-018-0232-z

Mattar & Daw give a normative theory in which replay accesses memories in order of *utility* -- the expected extra reward from improved future choices -- decomposed into a 'gain' term (propagate a newly-encountered outcome backward, producing reverse replay) and a 'need' term (evaluate imminent choices forward, producing forward replay). The single prioritised-access rule reproduces the empirical reverse-replay-after-reward phenomenology and unifies planning, learning and consolidation.

The relevance to REE is a concrete, cheap upgrade to an existing mechanism. REE already has a backward_credit_sweep; this paper supplies the *priority rule* it should use -- order updates by utility / TD-error rather than uniformly or by recency alone -- so that in a sparse forage task the sweep concentrates learning on exactly the reward-relevant transitions. This is the neuroscience-grounded version of prioritised sweeping / prioritised experience replay.

It is orthogonal to the novelty class (a scheduling policy over credit updates, not a reward term) and it *extends* rather than duplicates REE's sweep. In a small gridworld the priority queue is tiny, so this is a high-value, low-cost increment: 'make the credit sweep we already have smarter' rather than 'add a parallel novelty mechanism'.

Confidence 0.75: a well-grounded normative model that fits neural data, though not itself a floor->competent benchmark. Together with Foster & Wilson it argues that the credit-assignment lever -- which REE already partly owns -- is a stronger bet than more novelty for converting discovered reward into competence.
