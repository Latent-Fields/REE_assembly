# Reverse replay of behavioural sequences in hippocampal place cells during the awake state

**Class surveyed:** MEMORY / REVERSE-REPLAY CREDIT | **Evidence direction:** supports | **Confidence:** 0.72

**Source:** David J. Foster, Matthew A. Wilson (2006). *Reverse replay of behavioural sequences in hippocampal place cells during the awake state.* Nature 440:680-683 DOI: 10.1038/nature04587

Foster & Wilson report that during awake pauses immediately after spatial experience, hippocampal place-cell sequences replay in temporally *reversed* order -- most-recent-location first, running back toward the start. They explicitly propose this reverse ordering is suggestive of a role in evaluating event sequences in the manner of reinforcement-learning models: reverse replay is the biological substrate of backward credit assignment from an outcome.

For the class-choice this is the biological anchor of the memory/credit route. A per-step novelty bonus has no way to propagate a terminal reward back along the trajectory that earned it; reverse replay is exactly that operation. It is the archetype of the backward_credit_sweep REE already implements.

The composition consequence is the important one: this is not a new subsystem to add but a validation that REE's existing sweep is the right primitive. The buildable move is to ensure the sweep fires on the forage-reward episode and back-propagates value along the actually-visited trajectory in the gridworld -- a wiring/configuration task, not a new module. It is categorically orthogonal to the novelty cluster (credit-assignment vs coverage reward), so it composes cleanly.

Confidence 0.72: strong, canonical biological grounding, but indirect for the specific floor->competent claim (it is observational neuroscience, not an RL benchmark). Its role is to justify strengthening machinery REE already owns rather than duplicating the curiosity class.
