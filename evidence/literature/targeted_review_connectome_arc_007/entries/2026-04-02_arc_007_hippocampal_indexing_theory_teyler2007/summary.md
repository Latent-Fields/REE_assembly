# Teyler & Rudy (2007) — The Hippocampal Indexing Theory: Why the Hippocampus Doesn't Need to Compute Value

**Claims tested:** ARC-007
**Evidence direction:** supports | **Confidence:** 0.80

---

## What the paper did

Teyler and Rudy's 2007 paper is an update of the original hippocampal memory index theory formulated by Teyler and DiScenna in 1986. The original theory proposed that the hippocampus was anatomically and functionally positioned to capture sparse indices of neocortical activity patterns generated during behavioral episodes. The hippocampus does not store the full rich content of an episode — that remains distributed across cortical regions. Instead, it stores a compressed index sufficient to reactivate the cortical pattern from a partial cue. The 2007 update integrates two decades of subsequent evidence, including the finding that hippocampal indexing can occur for non-spatial content, accommodates rapid one-shot learning (now explained via BTSP-type mechanisms), and expands the account of contextual dependency and interference effects.

## Key findings relevant to ARC-007

The indexing theory's architectural implications for ARC-007 are direct and explicit. The hippocampus, on this account, is:

1. A **structural navigator** — it stores the index structure of episodic trajectories, not their content.
2. An **episodic retrieval engine** — it reactivates the cortical pattern when given a partial cue, enabling pattern completion.
3. **Not an evaluator** — the hippocampus stores the index; evaluation of the retrieved content is downstream. There is nothing in the index architecture that requires or implies value computation.

This is the canonical theoretical grounding for ARC-007's "no value computation" constraint. The hippocampus in indexing theory stores what happened (the trajectory), not whether it was good or bad (the evaluation).

## REE translation

In REE terms, the hippocampal trajectory traces (ARC-007) are indexed representations of paths through z_world — the action sequence, the state transitions, the temporal structure. The viability scores, residue accumulations, and harm/goal evaluations are stored in the residue field (φ(z)) and computed by E3. The hippocampus provides the index to the trajectory; E3 retrieves it and evaluates it. This division is architecturally clean and well-grounded in indexing theory.

The key prediction from indexing theory that bears on Q-020: if hippocampal cells that appear to encode reward (Gauthier & Tank 2018, Knudsen & Wallis 2021) are reinterpreted as stable anatomical relays for subcortical value signals (BLA, VTA) rather than as computational value representations, they are consistent with indexing theory. A relay channel that delivers BLA value signals to HPC for consolidation purposes (MECH-074) does not constitute value computation by the hippocampus — it is part of the write mechanism that shapes the index, not part of what the index computes.

## Limitations and caveats

Indexing theory is a functional architecture theory, not a mechanistic account. It does not specify how the index is implemented neurally at the cell or synaptic level (BTSP, pattern separation, theta sequences). The competing predictive map theory (Stachenfeld et al. 2017, also in this review set) offers an alternative framing in which the hippocampus actively predicts future states — a view that might imply more computation than pure indexing. The two theories are not mutually exclusive but they assign different roles to hippocampal processing. For REE, the indexing theory supports ARC-007 as formulated; the predictive map theory would require more careful specification of what "prediction" means in REE's z_world architecture.
