# Striatal indirect pathway mediates exploration via collicular competition

**Lee & Sabatini (2021) — Nature**
DOI: [10.1038/s41586-021-04055-4](https://doi.org/10.1038/s41586-021-04055-4)
*Based on articles retrieved from PubMed*

## What the paper did

Lee and Sabatini used optogenetics and in vivo electrophysiology in mice performing a simple lateralized licking task to dissect the causal role of indirect striatal projection neurons (iSPNs) in action suppression and exploration. By activating or silencing iSPNs with light, they could observe not just behavioral consequences but also the downstream circuit changes in the superior colliculus (SC), the midbrain output structure that translates basal ganglia gating into directional motor commands.

## Key findings

Activating iSPNs suppressed contraversive licking and promoted ipsiversive licking -- precisely what a no-go gate should do. The mechanism, however, was more interesting than simple suppression: iSPN activation suppressed ipsilateral SC but excited contralateral SC, and the reason was inter-collicular competition. Each hemisphere of the SC inhibits the other; when the indirect pathway depresses one SC, the other is released from inhibition and can drive action in the opposite direction. Inactivating iSPNs impaired both suppression of previously-rewarded (now devalued) licking and exploratory licking -- showing that the indirect pathway is necessary not just to say no to the current action but to enable the shift toward alternatives.

## REE translation

Q-016 asks what arbitration policy prevents coupling collapse when REE's three cortico-striatal loops disagree. Lee and Sabatini's findings give one concrete answer: the indirect pathway does not implement binary go/no-go suppression -- it implements competitive disinhibition. When the no-go gate fires, it does not simply silence downstream action representations; it shifts competition in a way that makes an alternative action more likely. Translated to REE's tri-loop architecture: a sound arbitration policy should preserve the competitive structure rather than hard-suppressing the losing loop's signal. If the sensorium loop (E1) loses a conflict to the planning loop (E3), the right policy is not to zero out the sensorium loop's contribution -- it is to reduce its gate priority while releasing the winning loop's representation to drive behavior. Hard suppression risks coupling collapse because the silenced loop loses its ability to contribute when the winning loop's preferred action becomes infeasible. Soft competitive arbitration keeps all loops contributing at some weight, with the winner temporarily dominant.

## Limitations

The collicular competition mechanism is anatomically specific to the oculomotor/orienting system. REE's tri-loop conflict involves interactions between cognitively, affectively, and motorically distinct representations that may not converge through a single downstream bottleneck like SC. The mouse licking task does not involve any conflict between loops at different timescales or with different error signals -- the REE-specific challenge of incommensurable error signals (MECH-069) is not probed here. It is also possible that the inter-collicular competition observed is a special feature of the orienting system rather than a general principle of BG arbitration.

## Confidence reasoning

I rate this 0.73. The causal optogenetic evidence is among the cleanest available for this domain, and the competitive-disinhibition mechanism is directly relevant to the coupling-collapse concern in Q-016. The confidence penalty comes from species transfer and from the specificity of the collicular mechanism -- the general principle (keep competition alive, don't hard-suppress) is well-supported, but whether the same circuit motif applies to REE's higher-order tri-loop conflicts requires further evidence.
