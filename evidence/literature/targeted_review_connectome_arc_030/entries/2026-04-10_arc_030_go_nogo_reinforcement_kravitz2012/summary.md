# Summary: Kravitz et al. 2012 -- Distinct Roles for Direct and Indirect Pathway Neurons in Reinforcement

**Claim tested:** ARC-030 (symmetric Go/NoGo sub-channels required; pure NoGo produces behavioral flatness)

**Source:** Kravitz AV, Tye LD, Kreitzer AC. "Distinct roles for direct and indirect pathway striatal neurons in reinforcement." Nature Neuroscience 2012;15(6):816-8. DOI: 10.1038/nn.3100

## What they did

The same Kravitz/Kreitzer group extended optogenetic striatal stimulation (D1-Cre and D2-Cre mice) from motor behavior to reinforcement learning. Mice could trigger optogenetic stimulation of either D1 or D2 MSNs via a nose-poke. They tracked acquisition and persistence of self-stimulation behavior (approach reinforcement) versus avoidance of the stimulation port (punishment).

## Key findings

- D1 MSN (direct/Go pathway) stimulation: induced persistent reinforcement -- animals continued to seek stimulation across sessions; approach behavior was stably learned.
- D2 MSN (indirect/NoGo pathway) stimulation: induced transient punishment -- animals briefly avoided the port but failed to sustain learned avoidance; no persistent reinforcement signal emerged.
- The two sub-channels carry qualitatively distinct information: Go produces persistent approach learning; NoGo produces only transient aversive signaling.
- This is not a simple sign-flip: Go and NoGo are not equivalent with opposite polarity.

## REE relevance

This paper directly addresses the non-interchangeability of Go and NoGo sub-channels at the reinforcement-learning level. ARC-030 requires both channels because they carry non-redundant information. A pure-NoGo architecture would lose the persistent reinforcement signal entirely, leaving only transient punishment -- which corresponds to a quiescent, behaviorally flat agent that can signal harm but cannot approach goals.

The qualitative asymmetry (persistent vs. transient) maps directly onto the REE distinction between goal-approach (z_goal salience, driven by benefit exposure) and harm avoidance (z_harm salience). Both signals are needed; neither substitutes for the other.

## Limitations

This study used self-stimulation in dorsomedial striatum rather than naturalistic cost-benefit approach/avoidance. The 'transient' punishment effect with D2 stimulation may partly reflect rapid extinction or stimulation protocol differences rather than fundamental informational asymmetry. However, the within-session vs. across-session contrast was robust.
