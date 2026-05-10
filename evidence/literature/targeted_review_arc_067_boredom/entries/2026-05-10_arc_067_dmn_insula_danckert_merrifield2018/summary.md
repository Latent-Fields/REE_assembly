# Danckert & Merrifield 2018 — Boredom, sustained attention and the default mode network

[DOI](https://doi.org/10.1007/s00221-016-4617-5) · PMID 26979438 · *Experimental Brain Research* 236(9):2507-2518

## What the paper argues

Healthy participants underwent fMRI under four conditions: resting state, a sustained-attention task, video-induced boredom, and video-induced interest/engagement. The DMN posterior regions showed common correlated activation across all conditions, but the boredom and sustained-attention conditions were distinguishable from rest by anticorrelated anterior insula (AIC) activity — when DMN regions were active, AIC was deactivated. The authors interpret boredom as a failure to engage executive control networks during a monotonous task.

## Why this matters for ARC-067

This is the load-bearing R3 paper for the routing-channel verdict. The AIC has a long lineage in the affective-salience and interoception literature (Critchley and colleagues): it integrates bodily-state and salience signals into a unified affective representation. AIC-deactivation under boredom is therefore consistent with the agent failing to assign affective salience to the current task — which is precisely the engagement-failure signature ARC-067 names.

For routing, this supports the choice between the two pre-registered options. Option A (route boredom-aversive through z_harm_a / affective harm stream / SD-011) is anatomically clean: SD-011 is the REE analog of the AIC-affective-stream pathway, and Danckert's finding shows that boredom IS in the AIC functional territory (negatively, via deactivation). Option B (separate engagement-rate scalar converging on a downstream consumer of z_harm_a) is more architecturally complex without obvious biological gain. The verdict is **Option A**: route through z_harm_a / AIC analog, with the engagement-rate estimator producing positive valence inputs that, when below threshold, allow a slow accumulator to fire on the same channel as actual harm.

The DMN-AIC anticorrelation pattern also constrains the R1 verdict. Boredom is not absence of mental activity (DMN is engaged) but absence of *executive* engagement specifically. This favours the Westgate & Wilson 2018 attentional reading and constrains the engagement-rate estimator: attentional / executive proxies (E3 deliberation depth, commit transitions per episode) are biologically supported; pure novelty proxies (MECH-314a inverse-frequency) are not the right substrate for ARC-067.

## Limitations and confidence

fMRI BOLD signals are slow, indirect, and group-averaged — the AIC-deactivation effect is a population-level signature, not a mechanistic localisation. The boredom induction was video-based passive viewing, which differs from both Wilson 2014's enforced-disengagement paradigm and the open-ended foraging case ARC-067 targets. Translation from BOLD signature to REE substrate routing requires bridging assumptions: that AIC activity in humans corresponds to SD-011 / z_harm_a in REE, and that DMN regions correspond to default-state / no-op-trajectory processing. Confidence aggregate 0.72 — solid source quality for fMRI work; mapping fidelity good for the routing verdict; transfer risk moderately elevated for the cross-substrate mapping.

## Failure signature it would falsify

An ARC-067 substrate that routes the engagement-rate aversive through the homeostatic-deficit substrate (SD-012) rather than the affective harm stream (SD-011) would predict a different network-level signature than Danckert observes — predicting that an REE-fMRI analog (residue-write distribution, channel utilisation patterns) should not match the boredom signature. Conversely, if boredom is implemented through MECH-216 predictive-wanting variants (target-conditioned), the network signature should look more like striatal/vmPFC reward-circuit activity than the AIC-deactivation Danckert observes — confirming that ARC-067 must be mechanistically distinct from MECH-216, as the registration already specifies.
