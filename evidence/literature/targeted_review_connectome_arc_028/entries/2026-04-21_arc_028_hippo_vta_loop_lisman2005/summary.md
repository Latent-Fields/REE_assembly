# Lisman & Grace 2005 -- Hippocampal-VTA Loop

**Claim tested:** ARC-028 (HippocampalModule completion signal -> BetaGate wiring)
**Direction:** supports | **Confidence:** 0.70

## What the paper did

Lisman and Grace proposed a functional loop between the hippocampus and the midbrain dopaminergic neurons of the VTA. The central claim is that the hippocampus detects newly arrived information that is not already stored in long-term memory -- generating a "novelty signal." This novelty signal travels a specific anatomical route: from the subiculum (hippocampal output) through the nucleus accumbens (NAc) and ventral pallidum (VP) to the VTA. At the VTA, this hippocampal signal combines with salience and goal information to drive novelty-dependent dopamine neuron firing. The dopamine is then released back into the hippocampus (the "upward arm" of the loop), enhancing LTP and facilitating encoding of the novel information into long-term memory.

## Key findings relevant to ARC-028

The anatomical route identified by Lisman and Grace is precisely the circuit that ARC-028 commits to in REE: subiculum -> NAc -> VP -> VTA -> dopamine release. The paper establishes that this is a real, functional loop, not merely a projection list -- hippocampal state information (novelty, in this case) causally drives VTA dopamine firing via this pathway. This directly grounds ARC-028's claim that HippocampalModule can emit a signal that, via the NAc-VP-VTA circuit, triggers dopamine release capable of modulating downstream BG gates (BetaGate).

## REE translation

In REE, ARC-028 replaces the novelty signal with a trajectory-completion signal. When HippocampalModule finishes generating a trajectory to a goal (or reaches its planned length), it emits a completion event. This event should activate the subiculum-analog output of the HippocampalModule, driving the NAc-analog, which disinhibits the VTA-analog, releasing dopamine. The dopamine then suppresses beta synchrony in the striatum (BetaGate), releasing the propagation gate (MECH-090) and enabling BetaGate to permit the next trajectory cycle. Lisman and Grace 2005 provides the anatomical and functional justification for each link in this chain.

## Limitations and caveats

The signal transmitted through this circuit in the paper is novelty, not completion. Novelty is a mismatch signal (expected vs. received); trajectory completion is a success signal (trajectory reached its planned terminus). Whether these two signals are routed through the same circuit, or whether completion signals take a different path (e.g., direct cortico-striatal projections from goal-related cortex, bypassing hippocampus), is not addressed. The paper also focuses primarily on the upward dopaminergic arm (VTA -> hippocampus for memory consolidation), with the downward arm (hippocampus -> VTA) described mostly at the circuit level rather than with direct recording evidence.

## Confidence reasoning

The anatomical circuit is well-established and this is the canonical reference for it. The mapping is reasonably direct for ARC-028's architectural purpose. The confidence penalty reflects the signal-content discrepancy (novelty vs. completion) -- a real gap that requires independent experimental justification before concluding that completion events use this circuit.
