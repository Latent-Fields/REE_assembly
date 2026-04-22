# Reagh et al 2018 -- Functional Imbalance of alEC and DG/CA3 Underlies Age-Related Object Pattern Separation Deficits

According to PubMed ([DOI](https://doi.org/10.1016/j.neuron.2018.01.039)).

## What the paper does

Reagh and colleagues used high-resolution fMRI to examine entorhinal-hippocampal circuit function in cognitively normal older adults, specifically during an object mnemonic discrimination task that requires distinguishing previously seen items from similar lures. They found a specific hypoactivity in anterolateral entorhinal cortex commensurate with behavioural deficits on the object pattern separation task. The same older adults showed *hyperactivity* in DG/CA3, and the ratio between alEC and DG/CA3 activity tracked individual differences in mnemonic discrimination performance. Spatial pattern separation showed only subtle deficits; the alEC pathway is selectively object-related.

## Why it matters for V_s invalidation

This paper is the empirical anchor that ties the Yassa-Stark 2011 pattern-separation framework to a behavioural readout that has the right shape for a V_s input. Mnemonic discrimination -- the ability to register that the current input is meaningfully different from a previously stored representation -- is the operation a V_s accumulator needs from its upstream circuitry. If the local schema label is going to drop because the anchored representation no longer fits the inputs, the circuit needs to first compute that the current input is genuinely different from what the anchor predicts. That computation is what mnemonic discrimination measures.

The Reagh result also gives us a candidate failure substrate distinct from the DA/LHb trigger failures discussed earlier in this pull. Aging-related alEC hypoactivity produces mnemonic discrimination deficits without (necessarily) damaging the broadcast trigger circuits. If V_s reads from an alEC-DG/CA3 axis, then this is a substrate where the local interference signal can fail before it ever reaches the accumulator -- a third failure mode beyond "broadcast trigger never fires" (LHb hypoactivity) and "accumulator integration broken" (OFC lesion).

## Mapping caveats

The behavioural task is object discrimination, not regional schema invalidation. Whether alEC operates the same way at the spatial-regional-schema scale that V_s requires is an extrapolation. There is some evidence that the medial entorhinal pathway carries spatial-schema information separately from alEC's object-schema information; the Reagh result might generalise, but it is not directly tested here. The architectural reading should be conservative: alEC is a candidate input substrate for object-related V_s, mEC for spatial-regional V_s, and the literature does not yet connect both pathways into a unified accumulator.

## Clinical resonance

This is the cleanest substrate-failure mapping for normal aging and early Alzheimer's. Older adults with intact reward-PE biology can still show schema-rigidity if the alEC input pathway is degraded. Clinically this maps to the often-noted observation that older patients can know perfectly well that a routine has stopped working (the trigger fires) and yet keep returning to it (the accumulator never updates effectively because the interference signal is degraded). It is a different failure mode from the depression-style blunting of the broadcast itself.

## Confidence reasoning

Source quality moderate-high (Neuron, well-executed fMRI, modest sample). Mapping fidelity moderate (0.58) because the behavioural proxy is one step removed from V_s. Transfer risk low (0.30). Aggregate 0.62.
