# MECH-094: Split Failure Modes — Confabulation, Psychosis, Hallucination

> Paste this into a new Claude Code session as your opening message.
> Created: 2026-04-14

## Prompt

Task: MECH-094 currently says "tag loss = PTSD/psychosis mechanism." This is clinically imprecise. The hypothesis_tag write gate has at least three distinct failure modes that need separate claims:

1. **Confabulation**: hypothesis_tag lost on simulation memories — simulated events get written to hippocampal terrain as if they actually happened. The agent "remembers" things it only imagined. This is the closest to what MECH-094 currently describes. Maps to Korsakoff's / frontal confabulation in clinical neurology.

2. **Psychosis/delusion**: a different mechanism entirely — likely involving DA-related belief updating or precision-weighting errors where prior beliefs override sensory evidence. NOT the same as tag loss. The agent believes things that contradict its sensory input.

3. **Hallucination**: sensory prediction overwhelming sensory input — the generative model produces percepts without corresponding stimuli. Yet another mechanism. The agent perceives things that aren't there.

These are mechanistically distinct in psychiatry (the user is a consultant psychiatrist). They should map to distinct mechanisms in REE.

Session goal: (1) Read MECH-094 in REE_assembly/docs/claims/claims.yaml and docs/architecture/default_mode.md. (2) Determine which failure mode MECH-094 actually describes (likely confabulation). (3) Register new MECH claims for the other two failure modes with appropriate mechanistic accounts. (4) Update MECH-094's notes to clarify it covers confabulation specifically. (5) Check if any existing claims already cover psychosis or hallucination mechanisms.
