# Michon et al. 2019 -- replay count scales with reward magnitude

## What the paper did

Rats performed a well-learned spatial memory task in a familiar context. The experimenters manipulated reward size at specific locations and measured post-learning behaviour together with hippocampal CA1 activity during the intervening rest periods. A closed-loop protocol allowed ripple-specific disruption of post-learning SWR events to test causal contribution.

## Key findings relevant to MECH-285

Two results are load-bearing. First, the proportion of replay events was positively correlated with both reward size and task demand -- a graded, quantitative relationship rather than a stepwise one. Second, ripple-specific disruption during post-learning rest abolished the selective enhancement of memory for highly rewarded locations. This is causal: replay proportion mediates the memory-selective effect, and disrupting the ripple substrate removes the behavioural signature.

## Translation to REE

MECH-285's priority-shape question is whether accumulated V_s staleness biases replay priority in a quantitative (proportional) or qualitative (threshold-gated) fashion. Both are implementable -- proportional implies a softmax or power-weighted sampler; threshold implies a categorical flag. Michon et al. give the closest direct biological answer: in the reward-priority arm, replay-event count scales with reward size in a graded fashion. If MECH-285 inherits its topology from the reward-priority arm, the default sampler should be a continuous-weighted distribution, not a binary flag. This aligns with Mattar & Daw 2018's normative EVB prediction and with the general principle that biological priority signals are graded rather than step-like.

The ripple-disruption result constrains the architecture further: the priority signal is implemented in SWR scheduling itself, not in encoding-time gain or retrieval-time filtering. For MECH-285 this localises the priority readout at the right place in the pipeline -- MECH-285 is a bias on replay scheduling, not on schema-update magnitude at the consumer end.

## Limitations and caveats

The priority signal tested here is reward magnitude, which maps onto the dopaminergic salience arm (MECH-074b lineage). MECH-285 predicts that epistemic staleness is a *dissociable* second priority signal. Michon et al. do not test the staleness arm, so the "proportional priority" verdict translates to MECH-285 only by assuming both arms share a common readout topology. The task is also in a familiar context, so novelty/staleness is not manipulated. A cleaner test would pit low-arousal high-novelty conditions against high-arousal low-novelty and measure whether the graded replay-count signature survives in the former.

## Confidence reasoning

Strong methods (closed-loop ripple disruption is the gold standard for causal SWR claims). Mapping fidelity high for the priority-shape verdict, lower for the dissociation verdict. Transfer risk low for shape, moderate for dissociation. Aggregate confidence 0.80.
