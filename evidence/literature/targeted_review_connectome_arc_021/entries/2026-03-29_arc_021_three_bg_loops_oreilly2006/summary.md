# O'Reilly & Frank (2006) -- PBWM: Three Distinct Learning Channels in PFC-BG

## What the paper did

O'Reilly and Frank present the PBWM (Prefrontal Cortex Basal Ganglia Working Memory) model, a computational architecture in which the basal ganglia implement selective gating of prefrontal cortex working memory representations. The central puzzle the paper addresses is the homunculus problem in executive function: how does a system know when to update, what to update, and when to commit to an action, without an infinite regress of controllers? Their answer is that the BG implement a dopamine-modulated reinforcement learning signal that trains separate Go/NoGo gating in distinct PFC stripes. Each stripe can be independently updated or maintained, and each stripe's learning is driven by the same RL mechanism but applied to its own dedicated pathway.

## Key findings relevant to ARC-021

The paper's core architectural lesson is that separate PFC stripes require separate gating channels, and that mixing signals across channels degrades performance. When maintenance gating and output gating are collapsed into a single channel, the system cannot hold information stable while simultaneously selecting a different representation for output -- the interference is not merely quantitative but qualitative. The authors show that each stripe effectively implements its own actor-critic loop, with the BG learning when that stripe should be updated based on task-contingent reward signals. This is the computational signature of learning-channel separation: each channel's credit assignment is local, and credit from one channel cannot substitute for credit in another.

## How this translates to REE (ARC-021)

ARC-021 asserts that the three BG-like corticostriatal loops (sensorimotor, associative, limbic in the biological literature) require distinct learning channels -- that E1 sensory prediction error, E2 motor-sensory error, and E3 harm/goal error cannot be collapsed without misattributing credit. The PBWM paper provides the computational precedent for exactly this kind of argument. Its demonstration that parallel, independently gated PFC stripes with separate learning pathways outperform a collapsed architecture is the formal analogue of what ARC-021 requires at the level of the three engines. If you merge the channels, you get interference. The lesson transfers from WM gating to error signal routing.

## Limitations and caveats

The paper's channels are specifically about working memory maintenance versus output gating -- a cognitive architecture distinction within PFC. It does not directly model the three anatomical loops (sensorimotor, associative, limbic) that form the empirical backbone of ARC-021. To close the gap, you need anatomical papers (Haber 2003) that show these loops are physically distinct and that their cortical projections carry incommensurable information. PBWM demonstrates the functional necessity of separation but cannot on its own establish that the three REE engines correspond to biologically distinct pathways. Additionally, PBWM uses a single dopamine signal across channels -- the separation is achieved by pathway specificity, not by having three chemically distinct neuromodulators. Whether the REE error signals (sensory, motor-sensory, harm) have the same channel-specific routing or require qualitatively distinct neuromodulatory systems is an open question.

## Confidence reasoning

Confidence is set at 0.72. The source quality is high -- this is a flagship paper in computational cognitive neuroscience, widely reproduced and extended. The mapping fidelity is moderate: the learning-channel-separation principle is directly relevant, but the anatomical grounding of three loops specifically requires additional papers. The transfer risk is moderate: the argument about channel interference is general enough to transfer to REE's three-engine design, but the specific claim that sensory, motor-sensory, and harm channels are incommensurable (MECH-069) requires direct experimental evidence that PBWM does not provide.
