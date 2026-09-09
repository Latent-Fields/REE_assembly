# Forward replay coordinated with prefrontal cortex: the rollout substrate ARC-054 presupposes

**Claim tested:** ARC-054 (D_V trajectory selection over planning horizon H) · **Direction:** supports · **Confidence:** 0.68

## What the paper did

Shin, Tang and Jadhav recorded simultaneously from dorsal CA1 and medial prefrontal cortex in rats learning a W-track spatial alternation task, and tracked how hippocampal-prefrontal replay coordination changed across learning. Two findings matter here. First, replay is not a hippocampal soliloquy: replay events are accompanied by structured, coordinated prefrontal ensemble activity, which means the sequences are being *read* by a downstream structure and not merely rehearsed. Second, the balance shifts with learning -- reverse replay dominates early, consistent with retrospective credit assignment, and forward replay becomes prominent as behaviour becomes memory-guided, consistent with prospective evaluation of where the animal might go.

## Why this bears on ARC-054

ARC-054 commits E3 to selecting trajectories by a criterion evaluated *over a rollout* -- J(pi) = sum over k of gamma^k times the predicted verisimilitude at t+k -- rather than over the current state. Before that claim can be about anything, a rollout mechanism has to exist: something that internally generates candidate future trajectories at decision time. The claim's own notes call this "hippocampal rollout evaluation", so it is not an incidental implementation detail; the claim names the substrate.

This paper is good evidence that the substrate is there and has the right shape. Forward sequences are generated. They are generated during awake behaviour at decision-relevant moments, not only offline. And they are coupled to a prefrontal partner, which is precisely the generator/evaluator split ARC-054's architecture assumes when it puts rollout generation and E3 scoring in different places. The framing the authors themselves use -- an internal cognitive search over past and possible future trajectories -- is close to what ARC-054 needs.

## What it does not show, and this is the crux

The paper evidences rollout *generation*. It says nothing about rollout *scoring*.

ARC-054's whole distinguishing content is the scoring rule. Its claim is not that the brain simulates futures -- that is now uncontroversial -- but that futures are ranked by predicted temporal-depth verisimilitude rather than by predicted reward, and that ranking by instantaneous coherence alone creates short-term coherence traps. Nothing here discriminates between D_V-scoring and ordinary reward-scoring. A rat running forward replay toward a reward site is exactly as consistent with a value-of-reward account as with a coherence-persistence account. So this entry supports the architectural precondition while leaving the claim's actual novelty entirely untested, and I have set mapping fidelity at 0.60 to reflect that.

There is a second, subtler gap. The retrospective-to-prospective shift is measured across learning stages, in aggregate. It is not a demonstration that on any given trial the forward replay *selected* the trajectory subsequently taken. That trial-level question is exactly where the literature gets contested -- see the Gillespie 2021 entry in this same directory, which I pulled deliberately as the counterweight.

Domain transfer is also real: rodents, spatial navigation, one task. ARC-054 is a general claim about E3 selection over arbitrary trajectories.

## Confidence reasoning

Source quality is high at 0.85 -- simultaneous dual-region ensemble recording with a within-animal learning comparison, in Neuron, from a group whose replay decoding methodology is well established. Mapping fidelity 0.60 and transfer risk 0.40 are what pull the aggregate down to 0.68. Because ARC-054 is an `arch_commitment` about a *selection rule*, I weighted mapping fidelity heavily, and the honest summary is: this makes the mechanism ARC-054 needs available, and does nothing to show ARC-054's criterion is the one it uses.
