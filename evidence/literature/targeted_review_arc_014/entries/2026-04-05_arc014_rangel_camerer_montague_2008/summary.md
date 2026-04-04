# Rangel, Camerer & Montague 2008 -- Neurobiology of Value-Based Decision Making: ARC-014 Mapping

**Source:** Rangel, A., Camerer, C. & Montague, P.R. (2008). A framework for studying the neurobiology of value-based decision making. *Nature Reviews Neuroscience*, 9(7), 545-556. DOI: [10.1038/nrn2357](https://doi.org/10.1038/nrn2357)

---

## What the Paper Does

Rangel, Camerer and Montague 2008 propose a five-process framework for value-based decision making in the brain. The framework is intended to integrate computational, behavioural, and neuroscientific accounts of how agents select actions based on value signals. The five processes are:

1. **Representation**: the decision problem is constructed (state, available options, constraints).
2. **Valuation**: subjective values are assigned to available actions.
3. **Action selection**: one action is chosen based on computed values.
4. **Outcome evaluation**: after the action is executed and its outcome received, the brain measures the desirability of what was obtained.
5. **Learning and updating**: the outcome evaluation signal is used to update processes 1-4 to improve future decisions.

The framework is explicitly sequential: processes 1-3 occur before action execution; processes 4-5 occur after. This is not merely a temporal ordering but a structural claim: outcome evaluation (process 4) requires an enacted outcome to evaluate -- it cannot occur before the action is completed.

## Key Findings Relevant to ARC-014

The critical structural feature of Rangel et al.'s framework for ARC-014 is the **selection-to-evaluation discontinuity**: process 3 (action selection) terminates with action initiation; process 4 (outcome evaluation) begins after action completion and outcome receipt. These are functionally distinct processes:

- Process 3 computes expected values over hypothetical action options and selects among them.
- Process 4 computes actual value of the received outcome and compares it to the prediction.

A system that collapsed these two processes would confuse the expected value of an option (computed in deliberation) with the actual value of the realised outcome (computed in evaluation). This is precisely the confusion that ARC-014's pre/post-commit boundary prevents: pre-commit trajectories are evaluated as hypothetical options (process 3 territory); post-commit consequences are evaluated as realised outcomes (process 4 territory).

The authors specifically note that outcome evaluation in process 4 measures "the desirability of outcomes that have been received" -- not outcomes being considered. This after-the-fact structure is the neuroscientific analogue of what ARC-014 calls offline attribution: the phi(z) update happens after the action is enacted (post-commit), not during deliberation (pre-commit).

## REE Mapping to ARC-014

ARC-014's commitment architecture maps onto the process 3 / process 4 transition in Rangel et al.'s framework:

- Pre-commit (simulation channel, Default Mode): corresponds to processes 1-3. Trajectories are hypothetical options being evaluated. No phi(z) write. The hypothesis tag (MECH-094) routes all pre-commit computation away from the phi(z) write pathway.
- Post-commit (realised-outcome channel): corresponds to processes 4-5. Consequences are real. phi(z) update is enabled. Offline attribution passes (MECH-029, MECH-092) occur here.

The architectural necessity claim in ARC-014 -- that offline attribution is necessary rather than optional -- maps onto Rangel et al.'s structural claim that outcome evaluation (process 4) cannot occur before action completion. A system that evaluated outcomes during deliberation would be doing something incoherent (evaluating unreceived outcomes as if received). For REE, a system that wrote to phi(z) during pre-commit simulation would accumulate ethical residue from imagined actions -- the architectural failure that leads to PTSD-like residue contamination when the hypothesis tag fails (MECH-076).

The Rangel et al. five-process framework also grounds the learning-update necessity: process 5 (learning update) requires the outcome from process 4, which requires the action from process 3. The sequential dependency is architecturally enforced. This supports ARC-014's claim that attribution after commitment is not optional -- it is what learning requires.

## Neural Substrates from Rangel et al.

The paper identifies key substrates for each process:

- Valuation (process 2): vmPFC, OFC, striatum, amygdala.
- Action selection (process 3): dlPFC, DLPFC, BG (selection loop).
- Outcome evaluation (process 4): vmPFC, OFC, striatum (prediction error, DA signal).
- Learning updates (process 5): dopamine-mediated synaptic plasticity, hippocampus for episodic update.

The hippocampal involvement in learning updates (process 5) is directly relevant to REE: offline attribution passes (MECH-029, MECH-092) involve hippocampal replay of post-commit trajectories to consolidate phi(z) updates. Rangel et al.'s inclusion of hippocampus in the learning-update process supports this architecture.

## Limitations and Confidence Reasoning

Rangel et al.'s framework is descriptive and does not argue for the architectural necessity of the pre/post separation in the sense ARC-014 requires. The boundary could in principle be graded rather than categorical. The phi(z) write-gating and hypothesis-tag mechanism are REE-specific additions. The paper provides structural support for the pre/post distinction and the necessity of post-action outcome evaluation, but does not constitute direct evidence for ARC-014's categorical commitment boundary. Confidence: 0.65.

*Based on article available via PubMed (PMID: 18545266) and Nature Reviews Neuroscience. Caltech preprint also available.*
