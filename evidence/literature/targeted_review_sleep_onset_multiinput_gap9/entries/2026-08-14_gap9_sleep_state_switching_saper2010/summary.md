# Saper, Fuller, Pedersen, Lu & Scammell 2010 -- Sleep state switching

According to PubMed: Saper CB, Fuller PM, Pedersen NP, Lu J, Scammell TE. *Neuron* 2010;68(6):1023-1042. [DOI 10.1016/j.neuron.2010.11.032](https://doi.org/10.1016/j.neuron.2010.11.032) (PMID 21172606).

## What the paper argues

The authoritative review of sleep-wake switching circuitry, by the group that proposed the flip-flop switch model. It integrates hypothalamic and brainstem anatomy with the dynamics those circuits produce, and extends the same treatment to the REM/NREM switch.

## Core claims

**The switch.** Sleep-wake transitions arise from **mutual inhibition** between the ventrolateral preoptic nucleus and the monoaminergic arousal groups. Mutual inhibition of this form is sharply **bistable** -- a slight advantage to either side is amplified until the other shuts down -- which produces the fast, complete state transitions observed, but is intrinsically **unstable** near the operating point.

**The stabiliser.** Orexin neurons sit **outside** the switch and stabilise it, holding it in the wake state; their position outside is what lets them stabilise rather than merely bias it. Loss of orexin produces narcolepsy's state instability; a switch stuck on the wake side produces insomnia.

**The regulators.** Switching is governed by **homeostatic, circadian, and allostatic** processes.

## Why this matters for GAP-9

Two contributions, and the first is the organising claim of the whole synthesis.

**1. The three-way decomposition is stated in the source literature.** The synthesis's Verdict 1 argues that sleep onset has inputs of three different logical types -- accumulated need, permissive gate/clock, and an allostatic risk term -- rather than one drive scalar. Saper's triad *is* that decomposition, from the field's canonical review. This is what licenses treating safety as a separate type rather than folding it in as another addend, and it means the synthesis is not inventing a taxonomy to suit REE's convenience.

**2. Switch-plus-external-stabiliser is the recommended shape for MECH-286.** The paper's architecture is a sharp bistable permit *plus* a continuous term acting on it from outside. Applied to REE: retain a boolean permit as the **outer backstop** (catastrophic threat only, threshold high) and let a **continuous** term do the ordinary graded work -- rather than trying to get graded behaviour out of the boolean condition by tuning `threat_tonic_threshold`, which the bistability analysis predicts will chatter near the operating point. REE already has both pieces: MECH-286 is the switch, and SD-037's `override_signal` is already the orexin-analog stabiliser and already MECH-286's first gate term. So the recommendation is largely to use what is there in the shape the biology uses it.

## Where the paper's coverage ends

This is a circuit-level review, and the flip-flop dynamics are a consequence of specific mutual-inhibition connectivity that REE does not implement. REE's sleep entry is a **procedural call**, not a dynamical attractor, so bistability would have to be *imposed by construction* rather than emerging from the wiring -- the architectural recommendation transfers, the dynamical mechanism does not. Worth noting that the codebase is not unfamiliar with the idiom: `BetaGate` (MECH-090 commitment) is already a bistable gate, so the pattern has local precedent. The review also predates the local-sleep synthesis this pull draws on elsewhere and treats sleep state as global, which sits in tension with Krueger 2008 and Vyazovskiy 2011 (sibling entries); that tension is real in the field and is not resolved here.

## Confidence reasoning

Source quality 0.95 -- *Neuron* review by the originators of the model, heavily cited, integrating anatomy with dynamics and with clinical validation through narcolepsy and insomnia. Mapping fidelity 0.85 for the architectural recommendation and the regulator taxonomy; substantially lower for the dynamics, which do not transfer to a procedural call. Transfer risk 0.22. Confidence 0.90.

## Failure signatures for the cluster

1. **Permit chatter near threshold.** If REE folds a graded safety response directly into MECH-286's boolean AND -- by tuning `threat_tonic_threshold` toward the operating point rather than adding a separate continuous term -- the bistability analysis predicts rapid permit/refuse oscillation across steps. Diagnostic: count permit-state flips per unit time with the threshold near the observed `z_harm_a` operating range; a high flip rate is the signature of a missing stabiliser.

2. **Stabiliser folded into the switch.** If the SD-037 override term is treated as just another AND condition rather than as an external stabiliser with its own continuous influence, the architecture loses the property that makes the biological switch usable. This is a design-review signature rather than a runtime one.
