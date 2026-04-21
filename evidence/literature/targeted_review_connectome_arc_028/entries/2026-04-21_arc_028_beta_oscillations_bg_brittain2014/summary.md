# Brittain, Sharott & Brown 2014 -- Beta Oscillations in Cortico-BG Loops

**Claim tested:** ARC-028 (HippocampalModule completion signal -> BetaGate wiring)
**Direction:** supports | **Confidence:** 0.73

## What the paper did

Brittain, Sharott and Brown reviewed the functional role of beta-band (13-30 Hz) oscillatory synchrony in cortico-basal ganglia circuits. The paper proposes that the degree of beta synchronization in BG networks acts as a computational gating variable: high beta synchrony = "immutability promoting" state that locks in incumbent behavior and limits the circuit's capacity to process novel action selection demands; suppressed beta = "mutability promoting" state that opens computation space for alternative actions. The paper grounds this hypothesis in Parkinson's disease pathology (where dopamine depletion pathologically elevates beta, causing akinesia) and in pharmacological and DBS data showing that restoring dopamine (or disrupting beta with high-frequency stimulation) restores motor flexibility.

## Key findings relevant to ARC-028

This paper provides the biological mechanism for what REE calls BetaGate. Three findings are directly relevant:

1. **Beta as a gate, not just noise**: Beta synchrony specifically constrains action selection capacity -- high beta maintains incumbent trajectories and suppresses competing ones. This is exactly what BetaGate does: elevated beta = committed trajectory locked in; release = new CEM selection cycle enabled.

2. **Dopamine suppresses beta**: In Parkinson's, dopamine depletion = pathological beta. L-DOPA restores normal beta suppression and restores motor flexibility. This establishes the causal chain that ARC-028 depends on: completion signal -> dopamine -> beta suppression -> BetaGate release.

3. **Beta at sequence boundaries**: The paper reviews evidence that beta transiently suppresses around movement initiation and reappears during movement maintenance. This temporal profile maps onto ARC-028's design: beta falls when a new trajectory is initiated (gate opens), rises during committed execution (gate closed), and should fall again at trajectory completion (when the next gate cycle begins).

## REE translation

ARC-028 needs HippocampalModule completion to trigger BetaGate release via dopamine. Brittain et al. 2014 establishes the mechanism for the final step: dopamine suppresses beta synchrony, releasing the gate. Lisman-Grace and Sesack-Grace papers establish the circuit from hippocampus to VTA to dopamine. Together, the three papers form a complete mechanistic chain: HippocampalModule -> subiculum-NAc-VP-VTA -> dopamine -> beta suppression -> BetaGate release.

## Limitations and caveats

The paper's evidence base is primarily Parkinson's disease pathology, where beta is chronically elevated due to dopamine depletion. Normal beta dynamics during reward-based sequence completion in healthy animals are less well characterized. It is possible that physiological beta modulation by hippocampal completion signals operates through different mechanisms (e.g., direct cortical input to striatum, not only dopamine) or that the magnitude of beta suppression triggered by a completion signal is smaller and less reliable than the pathological contrast used in the paper. The mapping to REE's discrete BetaGate (binary open/close) is also an idealization of what may be a graded oscillatory phenomenon.

## Confidence reasoning

This is the most direct paper available for the BetaGate mechanism itself. The confidence of 0.73 reflects good mechanistic alignment (beta-as-gate is exactly BetaGate), slightly penalized because the primary evidence base is Parkinson's pathology and the normal-function inference requires extrapolation.
