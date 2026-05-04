# Ballesta & Padoa-Schioppa 2019 -- Labeled-line identity coding in OFC

## What the paper did

Ballesta and Padoa-Schioppa recorded from OFC neurons in macaques performing sequential-offer juice-choice tasks. The experimental question they were addressing was whether the simultaneous-offer and sequential-offer paradigms recruit the same underlying neural circuitry, and how the neuronal populations underlying value comparison are organised. The architectural finding most relevant to SD-049 is buried in the methods and discussion: OFC neurons "encoded good identities and values in a juice-based representation (labeled lines)" -- i.e. distinct neural populations fire for distinct juice identities, and within each population the firing rate carries the value of *that* identity, not values of other identities. The decision mechanism, they argue, involves circuit inhibition where each offer-value indirectly inhibits the population encoding the opposite outcome.

## Why I pulled it for SD-049

This is the most direct biological precedent in the slate for option A: one-hot identity slot concatenated with magnitude latent. OFC's labeled-line architecture is exactly that pattern at the cellular level -- a population per identity (the labeled line / one-hot slot), with within-population firing-rate coding of value/magnitude (the magnitude latent). If REE's z_resource encoder is supposed to map onto OFC's biological role of carrying outcome-identity information into downstream decision circuits, the labeled-line precedent supports option A.

This paper is a useful counterweight to the distributed-substrate evidence from Schapiro (2016, 2017). Hippocampus learns distributed temporal-community structure, but OFC -- the structure REE's `update_z_goal()` actually maps onto for the wanting/liking dissociation MECH-229 cares about -- looks labeled-line. If z_resource is biologically OFC-analog rather than hippocampus-analog, option A is the better-grounded choice.

## What this paper cannot adjudicate

The labeled-line organisation in OFC could itself be the read-out of a distributed substrate upstream. Howard et al. 2015 (cross-tag entry in this lit-pull) used MVPA in human OFC and found identity-specific patterns -- which is consistent with both interpretations: distinct populations carry distinct identities (labeled line, supports option A), OR distributed pattern-based identity encoding read out by the distinct populations (consistent with option B/C). Single-unit electrophysiology is more decisive than MVPA on the labeled-line question because it can isolate which specific neurons fire for which specific identity, but the upstream-substrate question remains open.

The juice-based paradigm is also task-trained. The animals have been trained on a small set of juice options that are categorically distinct in the experimenter's frame, and OFC has had time to learn the labeled lines. SD-049's default 3 types (food, water, novelty) are similarly categorically distinct, but novelty is non-homeostatic and may not slot into a labeled-line architecture as cleanly as a homeostatic axis would. This is a Phase 2 implementation question worth flagging.

## Confidence and verdict contribution

Source quality is high (Padoa-Schioppa is a leading OFC electrophysiologist; the labeled-line claim has held up across his lab's work for over a decade). Mapping fidelity is high because "good identity" in this paper is precisely the variable z_resource wants to carry. Transfer risk is moderate -- macaque OFC vs REE substrate is a non-trivial leap, but the architectural primitive (per-identity populations) is general enough that the precedent transfers cleanly.

This entry is a primary support for option A. Combined with Quiroga's sparse-readout precedent, it argues that the biological identity-coding architecture in regions REE most directly maps onto (OFC, MTL readouts) is consistent with one-hot slot + magnitude rather than dense learned embedding. The Schapiro entries pull in the opposite direction by arguing for distributed substrate; the verdict has to weigh which architectural reading is more load-bearing for REE's specific needs.
