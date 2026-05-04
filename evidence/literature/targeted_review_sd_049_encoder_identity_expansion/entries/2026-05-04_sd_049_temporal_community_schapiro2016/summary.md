# Schapiro et al. 2016 -- Temporal community structure as distributed hippocampal coding

## What the paper did

Schapiro, Turk-Browne, Norman, and Botvinick exposed human subjects to sequences of fractal images whose transitions followed a community-graph structure: items grouped into densely connected sub-graphs ("communities") with sparse connections across groups, but no variance in transition probability between adjacent items. So the regularity is genuinely higher-order -- you cannot predict the next item from the previous-item-and-its-immediate-statistics, you have to learn the graph topology. The fMRI analysis showed that hippocampus develops representations whose similarity structure mirrors the underlying community grouping: items within the same community become more representationally similar after exposure, items across communities less similar.

## Why I pulled it for SD-049

This is the cleanest published evidence that hippocampus learns distributed similarity-preserving representations of structured stimulus sets. The architectural reading transfers directly to the SD-049 question: if z_resource is supposed to carry similarity structure across types (food and water are both consummatory; novelty is non-homeostatic), the biological architecture that does that natively is distributed embedding, not labeled-line. Option A's one-hot identity slot cannot represent similarity structure by construction -- the identities are orthogonal axes. Option B's learned low-D embedding can represent it; option C's hybrid does too via the embedding read-out side.

This entry weakens option A. It is not decisive against option A as the *encoder* choice -- you can still have one-hot encoder slots downstream of a distributed substrate, and Quiroga's concept cells are exactly that pattern. But it does say: if REE wants z_resource itself to carry similarity, only option B or C will produce it.

## What this paper is NOT saying

The community-structure paradigm is sequential statistical learning over an unsupervised stream. SD-049's z_resource is trained on a supervised identity signal (the resource type at the agent's cell). These are different kinds of learning problems, and the architectural fit between them is partial. A supervised identity-classifier head can be trained directly on top of a one-hot identity slot (option A) without ever needing to learn similarity structure -- and that may be enough for the immediate validation experiment (V3-EXQ-514 acceptance: identity-recovery > 0.6, goal_resource_r ≥ 0.5).

So the question this paper poses for the verdict is: does REE need similarity structure at z_resource right now, or does it just need identity discriminability? If similarity structure is needed (e.g. for downstream wanting/liking dissociation where the agent is supposed to "want novelty while liking food" -- a similarity-distance computation), option B/C is the right move. If only discriminability is needed, option A suffices and is engineering-cheaper.

## Confidence and verdict contribution

Source quality is high (Schapiro lab, peer-reviewed Hippocampus, replicated in their 2017 Phil Trans modeling paper). Mapping fidelity is moderate -- the architectural primitive transfers, but the specific learning task is different. Transfer risk substantial. Aggregate 0.78.

Verdict contribution: this is the strongest single argument for option B (similarity-preserving learned embedding) in the slate. Combined with the Schapiro 2017 hybrid-architecture entry, it makes the case that the substrate REE's z_resource interfaces with is distributed-and-similarity-preserving regardless of whether z_resource itself is implemented as one-hot. That argues for option C hybrid: keep the supervision-target-friendly one-hot slot of option A, but back it with a learned-embedding substrate so the similarity structure is preserved at the read-out interface.
