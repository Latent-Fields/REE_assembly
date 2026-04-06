# Mnemonic prediction errors bias hippocampal states

**Bein, Duncan & Davachi, 2020, Nature Communications**

## What the paper does

Bein et al. used high-resolution fMRI of hippocampal subfields while participants retrieved learned room images from memory and were then shown probe images containing 0 to 4 changes from the learned version. This allowed parametric manipulation of prediction error magnitude while measuring hippocampal subfield connectivity.

## Key findings relevant to MECH-205

The critical finding is a bidirectional connectivity shift proportional to prediction error magnitude: CA1-entorhinal connectivity *increased* with more changes (more encoding of the surprising input), while CA1-CA3 connectivity *decreased* with more changes (less retrieval of the now-erroneous memory prediction). This is not a simple novelty response — it is a structured switching of hippocampal processing mode, gated by how much the current experience deviates from the stored prediction.

This maps onto the biological implementation of the CA1 comparator: CA3 completes the pattern from partial cues (generating the prediction), entorhinal cortex carries the incoming sensory signal (the actual experience), and CA1 computes the difference. When the difference is large, CA1 suppresses CA3 and amplifies entorhinal input — in other words, it flags the episode as surprising and prepares it for encoding as a new memory trace rather than retrieval of the old one.

## Mapping to MECH-205's contrastive causal structure

MECH-205 claims that surprising episodes are cached in a surprise buffer and later replayed offline with contrastive variations. Bein et al. provide the biological mechanism for the online step that *populates* that buffer: CA1 detects the mismatch between CA3 prediction (anchor) and entorhinal input (actual), and proportionally tags the episode by its deviation magnitude. This is precisely what MECH-205 needs: a mechanism that converts prediction error magnitude into a priority signal for offline replay.

The CA1-CA3 suppression is also relevant to the contrastive structure: during replay, the hippocampus needs to hold the anchor (what CA3 predicted) alongside the actual surprising input — the contrast between them is the learning signal. The connectivity shift suggests CA1 is designed to hold both simultaneously and weight them by prediction error.

## Limitations

The study measures online waking perception, not offline replay. Whether the same CA1-entorhinal / CA1-CA3 connectivity balance persists into the offline replay phase — or whether it is reconstructed during SWRs — is not addressed. The room-image paradigm with discrete countable changes is a simplification; naturalistic continuous prediction errors may engage the mechanism differently.

## Confidence reasoning

Nature Communications, high-resolution hippocampal subfield fMRI with parametric manipulation of prediction error magnitude. Maps well onto the online mismatch detection step; less directly onto the offline contrastive replay structure. Overall confidence 0.72.
