# Strange, Witter, Lein & Moser (2014) -- multiple organisations, but not higher-order ones

## What the paper says

The dominant story about the hippocampal long axis was a dichotomy: dorsal/posterior does memory and space, ventral/anterior does anxiety. This review argues the dichotomy needs revision, and does so by putting two kinds of evidence side by side that disagree about what kind of object the axis is. Gene expression shows multiple functional domains with sharply demarcated borders -- discrete. Anatomy and electrophysiology show continuous variation -- gradients. The proposed reconciliation is that long-axis gradients are superimposed on discrete functional domains.

## Why it is in this folder, and why its confidence is low

The Q-084 source thought listed seven candidate biological predictions, and routed the underlying question -- does the biological hippocampal system support multiple partially distinct relational organisations? -- to literature rather than registering it, on the grounds that it is out-of-domain for REE. Prediction 4 was that longitudinal differences correspond to different levels of spatial, temporal, contextual or abstract granularity. Prediction 1 was that different subregions preferentially encode different relation types. This review is the standard reference on the first of those.

It substantiates the coarse claim. The hippocampus is not running one uniform relational computation along its length, and the multiple-organisations hypothesis is not fanciful. That is worth having on file.

But I want to be clear about what it does not do, because the temptation to let it count for more is exactly the kind of thing this record exists to prevent. Q-084's registered proposition is about structure *above a pairwise relation* -- metapaths, hyperedges, simplicial relations. Anatomical and functional differentiation along an axis is an orthogonal kind of variation. Multiple organisations existing does not entail that any of them is higher-order; you can have ten distinct organisations all of which are pairwise. So this paper speaks to the background hypothesis and is nearly silent on the claim.

Even against prediction 1 it is indirect. The domains the review distinguishes are granularity and affective-versus-spatial function. They are not relation *types* in the sense the thought meant -- causal dependency, event membership, shared goal relevance, harm structure. Nobody has cut the hippocampus along that partition.

## A design caution worth carrying

The gradients-superimposed-on-domains finding is a useful corrective for REE. If I were tempted to implement multiple relational organisations as clean discrete modules -- one per relation type -- the biology says that is over-committing. What it offers is discrete domains *and* continuous gradients at once. REE's existing scale-tagged anchors are closer to the gradient reading than to the modular one, which is mild support for the current design and an argument against a modular refactor. That belongs to MECH-469's territory (relation types not collapsible to one adjacency) more than to Q-084's.

## Confidence

0.60, with mapping fidelity at 0.42 doing the work of holding it down. The source is excellent and the finding is real; it is simply adjacent to the claim rather than on it. I have filed it deliberately rather than omitting it, because the source thought explicitly asked for this literature, but I would not want it counted as evidence that higher-order relational structure is required. It is not that.
