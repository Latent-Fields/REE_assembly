# Rushworth, Noonan, Boorman, Walton, Behrens (2011). Frontal Cortex and Reward-Guided Learning and Decision-Making. *Neuron*.

## What the paper does

This is the Neuron review that, for most of the following decade, people cited when they needed the phrase "vmPFC computes expected value and ACC does credit assignment." Rushworth and colleagues pull together lesion, fMRI, and single-unit data from rodents, macaques, and humans to ask a clean question: the frontal lobes are doing several different things in reward-guided decision-making, and which subregion is doing which? The answer, as they develop it, is a set of dissociations more robust than the field had any right to expect.

## Findings

The core dissociation, simplified: OFC and vmPFC represent the expected value of options *before* the action is chosen. The signal is continuous -- vmPFC tracks value across the deliberation window, not only at the moment of choice -- and it scales with the decision variable the animal is actually using. ACC, by contrast, supports action-outcome learning, effort cost integration, and, most importantly for our question, credit assignment: when an outcome arrives, ACC is where the comparison between expected and actual gets processed into an update on the action that produced it. Lateral PFC does rule selection and inhibition and sits partly outside this loop. The dissociation is not perfect -- vmPFC and ACC signals overlap in ways that lesion studies can disentangle but neuroimaging often cannot -- but it is the cleanest functional segregation the frontal decision literature has produced.

There is a detail that matters for the REE reading. The vmPFC value signal exists before the action; the ACC credit-assignment signal exists after the outcome. That is not a statement about when those regions happen to be active; it is a statement about what they compute, and the temporal structure is intrinsic to the function.

## REE mapping

This is the clearest piece of literature I have seen for the evaluator/comparator dissociation at the readout level. The SD-003 successor has to decide whether pre-action value estimation (evaluator mode) and post-action attribution (comparator mode) share a substrate or split into two substrates. The Rushworth review says: at least at the level of readout circuitry in frontal cortex, they split. vmPFC is the evaluator readout; ACC is the comparator readout. That maps onto a distinction REE needs -- but with a caveat (below).

For ARC-018, this is the downstream completion of the Kay and Pezzulo story. The hippocampus proposes rollouts; vmPFC/OFC scores them pre-action; the animal commits; ACC updates on the realised outcome. That three-stage picture is almost architecturally identical to what the SD-003 successor architecture will need.

For MECH-102 (violence as terminal error correction), the relevance is indirect but real. If the normal mode of action selection is vmPFC-mediated continuous evaluation of candidate futures, then terminal-error-correction behaviour implies either the evaluator's inputs have collapsed (no coherent future states to score) or its output bandwidth has collapsed (no gradient left between options). Both are interpretable in Rushworth's framework; the review does not address violence but it gives us the normal-mode baseline against which terminal-mode failures can be read.

## Where the mapping is imperfect

The review dissociates *readout* circuitry; it does not commit to whether the evaluator and comparator share the same forward model. This is exactly where the SD-003 successor question lives. vmPFC could read off the hippocampal forward model; ACC could read off the same model in a different mode; or ACC could use a separate comparator circuit with its own state representation. The Rushworth review does not adjudicate this, and the mapping caveat in the record field is meant to record that honestly.

A second limit: the review is about reward-guided learning. REE's SD-003 successor concerns the harm stream (SD-010/SD-011), which is architecturally separate in REE but not demonstrably separate at the frontal-cortex level in this review. Transferring the evaluator/comparator dissociation from reward to harm is an additional inferential step the paper does not underwrite.

## Confidence reasoning

Source quality high -- Neuron review, senior authors, canonical synthesis. Mapping fidelity good for the evaluator-vs-comparator readout distinction, softer for the forward-model-substrate question. Transfer risk moderate: the result is for reward, not harm, and the forward-model-sharing question is not addressed. Confidence 0.72 -- strong but not a direct test of REE's central architectural question.
