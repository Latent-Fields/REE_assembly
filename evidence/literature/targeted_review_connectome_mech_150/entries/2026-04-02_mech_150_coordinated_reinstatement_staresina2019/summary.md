# Staresina et al. (2019) — Coordinated Representational Reinstatement in Hippocampus and Lateral Temporal Cortex

## What the paper does

Using intracranial recordings in epilepsy patients, Staresina and colleagues reveal the temporal dynamics of episodic memory retrieval. They demonstrate a double dissociation: early reinstatement of item-context associations in the hippocampus (~500ms post-cue) precedes later reinstatement of item information in lateral temporal cortex. The hippocampal reinstatement correlates with high gamma power increases, suggesting an intrahippocampal pattern completion process that then "ignites" cortical reinstatement.

## Relevance to MECH-150

This paper establishes the causal ordering that MECH-150's architecture assumes: the hippocampal analogue (ContextMemory) retrieves associative context first, and this context then drives downstream cortical processing. In REE:

1. **E1 ContextMemory queried with z_world** (hippocampal cue-indexed retrieval) produces associative context
2. This context feeds **E2 action biasing** (MECH-151) and **E3 terrain scaling** (MECH-152)

The temporal cascade (hippocampal pattern completion -> cortical reinstatement) validates this information flow direction. If the ordering were reversed (cortical processing first, hippocampal binding later), MECH-150's architecture would be biologically backward.

## The timescale mismatch

The ~500ms retrieval-to-reinstatement delay is interesting but problematic for REE. MECH-150 assumes context retrieval is effectively instantaneous within a forward pass. In biology, the pattern completion process involves recurrent dynamics that take measurable time. This suggests either: (a) REE's feedforward approximation loses important dynamics, or (b) the biological timescale reflects implementation details (oscillatory synchronization) rather than computational necessity.

For the current V3 substrate, the feedforward approximation is probably acceptable — the key insight is the information flow direction, not the timing.

## Confidence reasoning

Excellent source quality (intracranial recordings, Nature Communications). The temporal ordering directly supports MECH-150's architectural claim. Confidence moderated by the feedforward vs recurrent mechanism gap.
