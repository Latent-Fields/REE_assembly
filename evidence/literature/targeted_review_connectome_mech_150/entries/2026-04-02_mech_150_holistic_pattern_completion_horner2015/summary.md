# Horner et al. (2015) — Evidence for Holistic Episodic Recollection via Hippocampal Pattern Completion

## What the paper does

Horner and colleagues use fMRI to demonstrate that hippocampal pattern completion supports holistic episodic recollection. Participants encode complex events composed of multiple elements (locations, people, objects). At retrieval, presenting a partial cue (one pairwise association) triggers reinstatement of the entire event, including elements incidental to the immediate task. Crucially, the degree of incidental element reinstatement correlates with hippocampal activity, establishing that the hippocampus performs content-addressable retrieval: a partial cue triggers recall of the full associative context.

## Relevance to MECH-150

MECH-150 claims that E1's ContextMemory, when queried with z_world alone (not the full [z_self, z_world] state), produces a cue-indexed association context that selectively activates stored associations relevant to the current sensory context. This is architecturally analogous to hippocampal pattern completion:

- **z_world as partial cue:** Just as presenting one element of an encoded event triggers retrieval of all associated elements, querying ContextMemory with z_world alone should retrieve the full associative context relevant to that world state.
- **Selective activation:** The output encodes which stored associations are most activated by the current exteroceptive cues — paralleling how hippocampal reinstatement is graded (stronger reinstatement = more hippocampal activity).

## Mapping caveats

The biological mechanism (CA3 recurrent attractor dynamics) differs fundamentally from MECH-150's implementation (trained feedforward projections with world_query_proj). Hippocampal pattern completion is auto-associative; ContextMemory is hetero-associative (input z_world -> output cue context). The principle transfers but the computational architecture is substantially different.

Additionally, EXQ-181b established that ContextMemory does NOT spontaneously develop differentiated cue content from unsupervised training — a supervised context-labeling objective is required. This is consistent with the biological need for encoding (the hippocampus must bind elements during the original experience), but the specific training regime differs.

## Confidence reasoning

High source quality (Nature Communications, leading memory research group). The pattern completion principle is directly relevant. Confidence moderated by the mechanistic gap between hippocampal auto-association and E1's trained projection architecture.
